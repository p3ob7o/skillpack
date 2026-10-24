# skillpack

A multi-host plugin marketplace. The same skill files install in Claude Code, Codex, and Cursor / Grok Bot.

Marketplace version: **1.0.0**. Repo: [github.com/p3ob7o/skillpack](https://github.com/p3ob7o/skillpack).

Plugins live under `plugins/<name>/`. Each skill keeps one copy of its instructions at `skills/<skill>/SKILL.md`. Host manifests point at those directories — they don't duplicate the skill text.

## Hosts at a glance

| Host | Catalog | Per-plugin manifest | Add marketplace | Install plugin |
|------|---------|---------------------|-----------------|----------------|
| Claude Code | `.claude-plugin/marketplace.json` | `.claude-plugin/plugin.json` | `/plugin marketplace add p3ob7o/skillpack` | `/plugin install <plugin>@skillpack` |
| Codex | `.agents/plugins/marketplace.json` | `.codex-plugin/plugin.json` + root `plugin.json` (Agent Plugins 1.0.0) | `codex plugin marketplace add p3ob7o/skillpack` | `codex plugin add <plugin>@skillpack` |
| Cursor / Grok Bot | `.cursor-plugin/marketplace.json` | `.cursor-plugin/plugin.json` | Import repo URL in the UI | Install at user or project scope |

Default skill discovery on every host is `skills/<name>/SKILL.md`. None of these plugins set a skills override. Skill `name` in YAML frontmatter is lowercase kebab-case and matches the folder name.

## Plugins

| Plugin | Version | Description |
|--------|---------|-------------|
| [writewell](plugins/writewell/README.md) | 1.5.0 | Writing pipeline: strip AI patterns, language discipline, clutter removal, quality check, optional personal voice |
| [keynote-writer](plugins/keynote-writer/README.md) | 1.0.0 | Braindump or transcript → TED-quality outline (flow, takeaway, slide text, image prompts, speaker notes) |
| [deck-builder](plugins/deck-builder/README.md) | 1.0.1 | Single-file HTML decks (typography-first) and presenter-notes mode for existing HTML decks |
| [session-manager](plugins/session-manager/README.md) | 1.0.0 | Load `CLAUDE.md` + `DOCUMENTATION.md` at session start; update them at wrap-up |
| [wordpress-to-spacefast](plugins/wordpress-to-spacefast/README.md) | 1.0.0 | Move WordPress from any host to Spacefast (headless WP, Astro front end, DNS cutover) |

## Install

Add the marketplace once, then install any plugin by name. Replace `<plugin>` with `writewell`, `keynote-writer`, `deck-builder`, `session-manager`, or `wordpress-to-spacefast`.

Plugin-specific setup (for example writewell's voice profile) lives in that plugin's README. Shared host steps stay here.

### Claude Code

```
/plugin marketplace add p3ob7o/skillpack
/plugin install <plugin>@skillpack
```

Invoke skills as `/<plugin>:<skill>`, for example `/writewell:writewell`, `/writewell:onboard`, `/deck-builder:slide-deck-creator`.

### Codex

Add the whole GitHub repository. Don't sparse-checkout only `.agents/plugins`: plugins live under `plugins/`, and the catalog points at those local paths. Skills sit under `skills/`; each Codex manifest points at `./skills/`.

```
codex plugin marketplace add p3ob7o/skillpack
codex plugin add <plugin>@skillpack
```

In an interactive session, `/plugins` opens the same browser. Start a new session after install so the bundled skills load.

### Cursor and Grok Bot

Cursor and Grok Bot use the same Cursor plugin packages. Catalog entries are `name`, `source`, and `description` only.

Import the repo URL:

```
https://github.com/p3ob7o/skillpack
```

In Cursor: Customize, or Dashboard → Plugins & MCPs → Add Marketplace → Import from Repo. Install a plugin at user or project scope. Invoke a skill with `/` plus its skill name.

A listing on the public Grok Bot marketplace is a separate review at [https://x.ai/bot/marketplace/submit-a-plugin](https://x.ai/bot/marketplace/submit-a-plugin). Importing this repository doesn't require that submission.

## Check the manifests

[`scripts/validate-manifests.py`](scripts/validate-manifests.py) checks that Claude, Codex, and Cursor manifests agree and that each `SKILL.md` follows the shared frontmatter rules. It needs `jsonschema` and `pyyaml`. GitHub Actions runs job **Validate manifests** under the workflow name `validate` on push and pull request.

```
pip install jsonschema pyyaml
python3 scripts/validate-manifests.py
```

## License

GPL v2. See [LICENSE](LICENSE).
