#!/usr/bin/env python3
"""Fail when marketplace manifests drift or a SKILL.md breaks host rules.

Source of truth for plugin name, description, version, license, keywords, and
category is .claude-plugin/marketplace.json. Codex and Cursor manifests must
carry those same values. Skill files are checked against the Agent Skills
rules shared by Claude Code, Codex, and Cursor: https://agentskills.io/specification

Requires PyYAML and jsonschema (see .github/workflows/validate-manifests.yml).
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

import yaml
from jsonschema import Draft7Validator, Draft202012Validator
from jsonschema.exceptions import SchemaError
from referencing import Registry
from referencing.jsonschema import DRAFT7, DRAFT202012

ROOT = Path(__file__).resolve().parents[1]
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CODEX_MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
CURSOR_MARKETPLACE = ROOT / ".cursor-plugin" / "marketplace.json"

SCHEMAS = {
    "claude-marketplace": "https://json.schemastore.org/claude-code-marketplace.json",
    "claude-plugin": "https://json.schemastore.org/claude-code-plugin-manifest.json",
    "cursor-marketplace": "https://raw.githubusercontent.com/cursor/plugins/main/schemas/marketplace.schema.json",
    "cursor-plugin": "https://raw.githubusercontent.com/cursor/plugins/main/schemas/plugin.schema.json",
    "agent-plugin": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
}

ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BACKTICK_PATH_RE = re.compile(r"`([^`\n]+)`")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BODY_HOSTILE = (
    "AskUserQuestion",
    "Skill(command",
    "BASH_SOURCE",
    "frontend-slides",
    "presentations:craft",
)
SLASH_COMMANDS = (
    "/writewell",
    "/presenter-notes",
    "/start-session",
    "/wrap-up-session",
    "/keynote-writer",
    "/deck-builder",
)
INSTALL_POLICIES = {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}
AUTH_POLICIES = {"ON_INSTALL", "ON_USE"}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text())
    except FileNotFoundError:
        fail(f"missing {path.relative_to(ROOT)}")
        return {}
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)}: expected a JSON object")
        return {}
    return data


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "skillpack-validate"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode())


def validator_for(schema: dict):
    schema_id = schema.get("$schema", "")
    if "2020-12" in schema_id:
        dialect = DRAFT202012
        cls = Draft202012Validator
    else:
        dialect = DRAFT7
        cls = Draft7Validator
    registry = Registry().with_resource(schema.get("$id", schema_id or "schema"), dialect.create_resource(schema))
    return cls(schema, registry=registry, format_checker=cls.FORMAT_CHECKER)


def validate_instance(label: str, instance: dict, schema: dict) -> None:
    try:
        validator = validator_for(schema)
        validator.check_schema(schema)
    except SchemaError as exc:
        fail(f"{label}: published schema is not usable ({exc.message})")
        return
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        path = "/".join(str(part) for part in error.path) or "<root>"
        fail(f"{label}: {path}: {error.message}")


def as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return value
    fail(f"expected a string or list of strings, got {value!r}")
    return []


def skill_dirs(plugin_root: Path) -> list[Path]:
    skills_root = plugin_root / "skills"
    if not skills_root.is_dir():
        return []
    return sorted(path.parent for path in skills_root.rglob("SKILL.md"))


def rel_skill(plugin_root: Path, skill_dir: Path) -> str:
    return "./" + skill_dir.relative_to(plugin_root).as_posix()


def is_top_level_skill(plugin_root: Path, skill_dir: Path) -> bool:
    relative = skill_dir.relative_to(plugin_root)
    return len(relative.parts) == 2 and relative.parts[0] == "skills"


def check_skill(skill_md: Path) -> None:
    rel = skill_md.relative_to(ROOT)
    text = skill_md.read_text()
    if not text.startswith("---\n"):
        fail(f"{rel}: missing YAML frontmatter")
        return
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{rel}: unterminated frontmatter")
        return
    try:
        frontmatter = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as exc:
        fail(f"{rel}: invalid YAML: {exc}")
        return
    if not isinstance(frontmatter, dict):
        fail(f"{rel}: frontmatter must be a mapping")
        return

    extra = sorted(set(frontmatter) - ALLOWED_FRONTMATTER)
    if extra:
        fail(f"{rel}: unexpected frontmatter fields: {', '.join(extra)}")

    name = frontmatter.get("name")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
        fail(f"{rel}: name must be 1-64 lowercase letters, digits, and single hyphens")
    elif name != skill_md.parent.name:
        fail(f"{rel}: name {name!r} must match directory {skill_md.parent.name!r}")

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        fail(f"{rel}: description must be a non-empty string")
    elif len(description) > 1024:
        fail(f"{rel}: description is {len(description)} characters; limit is 1024")

    if frontmatter.get("license") != "GPL-2.0":
        fail(f"{rel}: license must be GPL-2.0")

    metadata = frontmatter.get("metadata")
    if metadata is not None:
        if not isinstance(metadata, dict) or not all(
            isinstance(key, str) and isinstance(value, str) for key, value in metadata.items()
        ):
            fail(f"{rel}: metadata must be a map of strings to strings")

    allowed_tools = frontmatter.get("allowed-tools")
    if allowed_tools is not None and not isinstance(allowed_tools, str):
        fail(f"{rel}: allowed-tools must be a space-separated string")

    compatibility = frontmatter.get("compatibility")
    if compatibility is not None and (
        not isinstance(compatibility, str) or not compatibility.strip() or len(compatibility) > 500
    ):
        fail(f"{rel}: compatibility must be a string of 1-500 characters")

    body = text[end + 5 :]
    for needle in BODY_HOSTILE:
        if needle in body:
            fail(f"{rel}: host-specific token {needle!r} is still in the skill body")
    for command in SLASH_COMMANDS:
        if re.search(rf"(?<![A-Za-z0-9./_-]){re.escape(command)}\b", body):
            fail(f"{rel}: slash command {command} is still in the skill body")

    check_relative_paths(skill_md, body)


def check_relative_paths(skill_md: Path, body: str) -> None:
    rel = skill_md.relative_to(ROOT)
    tokens: set[str] = set()
    for match in BACKTICK_PATH_RE.finditer(body):
        tokens.add(match.group(1).strip())
    for match in MARKDOWN_LINK_RE.finditer(body):
        tokens.add(match.group(1).strip())
    for token in sorted(tokens):
        if token.startswith(("http://", "https://", "mailto:")):
            continue
        if any(char in token for char in " *<>{}|$"):
            continue
        path = token.split("#", 1)[0]
        if not path.endswith((".md", ".html")):
            continue
        skill_ref = path.startswith(("references/", "assets/", "scripts/", "onboard/", "voice/", "../")) or path.endswith(
            "SKILL.md"
        )
        if not skill_ref:
            continue
        target = (skill_md.parent / path).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            fail(f"{rel}: path {token!r} escapes the repository")
            continue
        if target.name == "SKILL.md" and target.parent.name == "voice":
            continue
        if not target.is_file():
            fail(f"{rel}: missing referenced file {token}")


def check_manifest_sync(claude_market: dict, codex_market: dict, cursor_market: dict) -> None:
    if claude_market.get("name") != "skillpack":
        fail("Claude marketplace name must stay skillpack")
    if codex_market.get("name") != claude_market.get("name"):
        fail("Codex marketplace name does not match Claude")
    if cursor_market.get("name") != claude_market.get("name"):
        fail("Cursor marketplace name does not match Claude")

    claude_meta = claude_market.get("metadata") or {}
    cursor_meta = cursor_market.get("metadata") or {}
    if cursor_meta.get("description") != claude_meta.get("description"):
        fail("Cursor marketplace description does not match Claude")
    if cursor_meta.get("version") != claude_meta.get("version"):
        fail("Cursor marketplace version does not match Claude")
    if (cursor_market.get("owner") or {}).get("name") != (claude_market.get("owner") or {}).get("name"):
        fail("Cursor marketplace owner does not match Claude")

    display_name = ((codex_market.get("interface") or {}).get("displayName"))
    if display_name != claude_market.get("name"):
        fail("Codex interface.displayName must match the marketplace name")

    claude_plugins = claude_market.get("plugins") or []
    codex_plugins = codex_market.get("plugins") or []
    cursor_plugins = cursor_market.get("plugins") or []
    if [item.get("name") for item in claude_plugins] != [item.get("name") for item in codex_plugins]:
        fail("Codex plugin order or names do not match the Claude marketplace")
    if [item.get("name") for item in claude_plugins] != [item.get("name") for item in cursor_plugins]:
        fail("Cursor plugin order or names do not match the Claude marketplace")

    owner = (claude_market.get("owner") or {}).get("name")
    for claude_entry, codex_entry, cursor_entry in zip(claude_plugins, codex_plugins, cursor_plugins):
        name = claude_entry.get("name")
        plugin_root = ROOT / "plugins" / str(name)
        expected = {
            "name": name,
            "description": claude_entry.get("description"),
            "version": claude_entry.get("version"),
            "license": "GPL-2.0",
            "keywords": claude_entry.get("keywords"),
            "category": claude_entry.get("category"),
        }
        if claude_entry.get("license") != "GPL-2.0":
            fail(f"{name}: Claude marketplace license must be GPL-2.0")
        if claude_entry.get("source") != f"./plugins/{name}":
            fail(f"{name}: Claude source must be ./plugins/{name}")

        compare_entry("Codex marketplace", name, codex_entry, expected)
        source = codex_entry.get("source") or {}
        if source.get("source") != "local" or source.get("path") != f"./plugins/{name}":
            fail(f"{name}: Codex source must be local ./plugins/{name}")
        policy = codex_entry.get("policy") or {}
        if policy.get("installation") not in INSTALL_POLICIES:
            fail(f"{name}: Codex policy.installation is invalid")
        if policy.get("authentication") not in AUTH_POLICIES:
            fail(f"{name}: Codex policy.authentication is invalid")
        if "products" in policy:
            fail(f"{name}: omit Codex policy.products unless a product gate is required")

        if cursor_entry.get("description") != expected["description"]:
            fail(f"{name}: Cursor marketplace description does not match")
        if cursor_entry.get("source") != f"plugins/{name}":
            fail(f"{name}: Cursor source must be plugins/{name}")
        extra_cursor_keys = set(cursor_entry) - {"name", "source", "description"}
        if extra_cursor_keys:
            fail(
                f"{name}: Cursor marketplace entry has fields the published schema rejects: "
                + ", ".join(sorted(extra_cursor_keys))
            )

        claude_plugin = load_json(plugin_root / ".claude-plugin" / "plugin.json")
        compare_manifest("Claude plugin.json", name, claude_plugin, expected, include_category=False)
        if (claude_plugin.get("author") or {}).get("name") != owner:
            fail(f"{name}: Claude author.name must match the marketplace owner")
        declared = as_list(claude_plugin.get("skills"))
        nested = [rel_skill(plugin_root, path) for path in skill_dirs(plugin_root) if not is_top_level_skill(plugin_root, path)]
        for skill_path in nested:
            if skill_path not in declared:
                fail(f"{name}: Claude plugin.json must list nested skill {skill_path}")

        codex_plugin = load_json(plugin_root / ".codex-plugin" / "plugin.json")
        compare_manifest("Codex plugin.json", name, codex_plugin, expected, include_category=False)
        if (codex_plugin.get("author") or {}).get("name") != owner:
            fail(f"{name}: Codex author.name must match the marketplace owner")
        all_skills = [rel_skill(plugin_root, path) for path in skill_dirs(plugin_root)]
        # Codex 0.163 scans skills/ one level deep unless skills is an explicit
        # directory list. A schema-declared root plugin.json wins over
        # .codex-plugin/plugin.json and then ignores that list, so a plugin
        # with a nested skill must not ship one.
        codex_skills = codex_plugin.get("skills")
        if nested:
            if not isinstance(codex_skills, list) or sorted(codex_skills) != sorted(all_skills):
                fail(f"{name}: Codex skills must list every skill directory when one is nested: {all_skills}")
        elif codex_skills != "./skills/":
            fail(f"{name}: Codex skills path must be ./skills/")
        interface = codex_plugin.get("interface") or {}
        if interface.get("displayName") != name:
            fail(f"{name}: Codex interface.displayName must match the plugin name")
        if interface.get("shortDescription") != expected["description"]:
            fail(f"{name}: Codex interface.shortDescription does not match")
        if interface.get("longDescription") != expected["description"]:
            fail(f"{name}: Codex interface.longDescription does not match")
        if interface.get("category") != expected["category"]:
            fail(f"{name}: Codex interface.category does not match")
        if interface.get("developerName") != owner:
            fail(f"{name}: Codex interface.developerName must match the marketplace owner")

        portable_path = plugin_root / "plugin.json"
        if nested:
            if portable_path.exists():
                fail(
                    f"{name}: omit root plugin.json. Codex prefers a schema-declared root manifest "
                    "and then ignores the skills list, so a nested skill would not load."
                )
        else:
            portable = load_json(portable_path)
            compare_manifest("root plugin.json", name, portable, expected, include_category=False)
            extension = ((portable.get("extensions") or {}).get("com.openai") or {})
            portable_interface = extension.get("interface") or {}
            if portable_interface.get("displayName") != name:
                fail(f"{name}: root plugin.json displayName must match the plugin name")
            if portable_interface.get("shortDescription") != expected["description"]:
                fail(f"{name}: root plugin.json shortDescription does not match")
            if portable_interface.get("category") != expected["category"]:
                fail(f"{name}: root plugin.json category does not match")

        cursor_plugin = load_json(plugin_root / ".cursor-plugin" / "plugin.json")
        compare_manifest("Cursor plugin.json", name, cursor_plugin, expected, include_category=True)
        if (cursor_plugin.get("author") or {}).get("name") != owner:
            fail(f"{name}: Cursor author.name must match the marketplace owner")
        listed = as_list(cursor_plugin.get("skills")) if "skills" in cursor_plugin else None
        if nested and listed is None:
            fail(f"{name}: Cursor plugin.json must list nested skills explicitly")
        if listed is not None and sorted(listed) != sorted(all_skills):
            fail(f"{name}: Cursor skills list must be exactly {all_skills}")


def compare_entry(label: str, name: str, entry: dict, expected: dict) -> None:
    for field in ("description", "version", "license", "keywords", "category"):
        if entry.get(field) != expected[field]:
            fail(f"{name}: {label} {field} does not match the Claude marketplace")


def compare_manifest(label: str, name: str, manifest: dict, expected: dict, include_category: bool) -> None:
    for field in ("name", "description", "version", "license", "keywords"):
        if manifest.get(field) != expected[field]:
            fail(f"{name}: {label} {field} does not match the Claude marketplace")
    if include_category and manifest.get("category") != expected["category"]:
        fail(f"{name}: {label} category does not match the Claude marketplace")


def main() -> int:
    claude_market = load_json(CLAUDE_MARKETPLACE)
    codex_market = load_json(CODEX_MARKETPLACE)
    cursor_market = load_json(CURSOR_MARKETPLACE)
    if not errors:
        check_manifest_sync(claude_market, codex_market, cursor_market)

    try:
        schemas = {key: fetch_json(url) for key, url in SCHEMAS.items()}
    except Exception as exc:  # noqa: BLE001 - surface the fetch failure as the validation result
        fail(f"could not fetch a published schema: {exc}")
        schemas = {}

    if schemas:
        validate_instance("Claude marketplace", claude_market, schemas["claude-marketplace"])
        validate_instance("Cursor marketplace", cursor_market, schemas["cursor-marketplace"])
        for plugin_dir in sorted((ROOT / "plugins").iterdir()):
            if not plugin_dir.is_dir():
                continue
            validate_instance(
                f"{plugin_dir.name} Claude plugin.json",
                load_json(plugin_dir / ".claude-plugin" / "plugin.json"),
                schemas["claude-plugin"],
            )
            validate_instance(
                f"{plugin_dir.name} Cursor plugin.json",
                load_json(plugin_dir / ".cursor-plugin" / "plugin.json"),
                schemas["cursor-plugin"],
            )
            portable_path = plugin_dir / "plugin.json"
            if portable_path.is_file():
                validate_instance(
                    f"{plugin_dir.name} root plugin.json",
                    load_json(portable_path),
                    schemas["agent-plugin"],
                )

    for skill_md in sorted((ROOT / "plugins").rglob("SKILL.md")):
        check_skill(skill_md)

    if errors:
        print(f"{len(errors)} manifest/skill error(s):", file=sys.stderr)
        for message in errors:
            print(f"- {message}", file=sys.stderr)
        return 1
    print("manifests and skills match Claude Code, Codex, and Cursor rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
