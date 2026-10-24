# session-manager

Version **1.0.0**. Bookend a development session: load project context when you start, update the docs before you stop.

## What it does

Uses two project context files on every host: `CLAUDE.md` and `DOCUMENTATION.md`.

- **start-session** — loads those files at the beginning of a session
- **wrap-up-session** — updates them with what changed before you end
- **session-manager** — umbrella skill that explains the two-command workflow and when to use each

## Skills

| Skill | Role | Claude Code | Codex / Cursor / Grok Bot |
|-------|------|-------------|---------------------------|
| `session-manager` | Workflow overview | `/session-manager:session-manager` | `/session-manager` |
| `start-session` | Load context | `/session-manager:start-session` | `/start-session` |
| `wrap-up-session` | Update docs at end | `/session-manager:wrap-up-session` | `/wrap-up-session` |

## Install

Shared marketplace steps: [skillpack install](../../README.md#install).

```
# Claude Code
/plugin install session-manager@skillpack

# Codex (after marketplace add)
codex plugin add session-manager@skillpack

# Cursor / Grok Bot
# Import https://github.com/p3ob7o/skillpack, then install session-manager
```

## Usage

1. At session start, run `start-session` so the agent loads `CLAUDE.md` and `DOCUMENTATION.md`.
2. Work as usual.
3. Before ending, run `wrap-up-session` so those files reflect what changed.

Run `session-manager` if you want a short reminder of that workflow.

## Structure

```
skills/
  session-manager/SKILL.md   # Two-command overview
  start-session/SKILL.md     # Load context at start
  wrap-up-session/SKILL.md   # Update docs at end
```
