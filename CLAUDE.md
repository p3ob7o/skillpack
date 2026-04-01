# Skillpack

Plugin marketplace for Claude Code skills. Repo: `p3ob7o/skillpack`

## Conventions

- Branch: `main` (never `master`)
- License: GPL v2
- Plugin names: kebab-case
- Skill files: `SKILL.md` (uppercase)

## Versioning

Versions must be bumped in **three places** simultaneously:
1. `plugins/<name>/skills/<name>/SKILL.md` — frontmatter `version:`
2. `plugins/<name>/.claude-plugin/plugin.json` — `"version"`
3. `.claude-plugin/marketplace.json` — plugin entry `"version"`

## Local/Marketplace Sync

The writewell skill lives in two places:
- **Marketplace** (shared): `~/Documents/skillpack/plugins/writewell/skills/writewell/`
- **Local** (personal): `~/.claude/skills/writewell/`

After editing the marketplace copy, sync to local:
```bash
cp plugins/writewell/skills/writewell/SKILL.md ~/.claude/skills/writewell/SKILL.md
cp plugins/writewell/skills/writewell/onboard/SKILL.md ~/.claude/skills/writewell/onboard/SKILL.md
```

The `voice/SKILL.md` file is personal and should NOT be synced to the marketplace (it's gitignored).

## Adding a New Plugin

1. Create `plugins/<name>/.claude-plugin/plugin.json`
2. Create `plugins/<name>/skills/<name>/SKILL.md`
3. Add a `plugins/<name>/README.md`
4. Add the plugin entry to `.claude-plugin/marketplace.json`
5. Update the table in `README.md`

## Subskills

Claude Code cannot invoke subskills via the Skill tool from within a running skill. Instead, use `Read` to load the subskill file directly (e.g., `onboard/SKILL.md` relative to the skill directory).
