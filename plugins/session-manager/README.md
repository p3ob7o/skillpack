# session-manager

Bookend your development sessions: load context when you start, capture what changed before you stop.

## Skills

### session-manager

The umbrella skill — explains the two-command workflow and when to reach for each.

### start-session

Loads project context from `CLAUDE.md` and `DOCUMENTATION.md` at the start of a session. Those two filenames are the project context files for this workflow on every host.

In Claude Code the command is `/session-manager:start-session`. Elsewhere, invoke the `start-session` skill.

### wrap-up-session

Updates `CLAUDE.md` and `DOCUMENTATION.md` with the changes made during the session before you end it.

In Claude Code the command is `/session-manager:wrap-up-session`. Elsewhere, invoke the `wrap-up-session` skill.

## Install

See the [skillpack install steps](../../README.md#install).

Claude Code:

```
/plugin marketplace add p3ob7o/skillpack
/plugin install session-manager@skillpack
```

Codex, after `codex plugin marketplace add p3ob7o/skillpack`:

```
codex plugin add session-manager@skillpack
```

Cursor and Grok Bot: import `https://github.com/p3ob7o/skillpack` and install session-manager.

## Structure

```
skills/
  session-manager/SKILL.md   # The two-command overview
  start-session/SKILL.md     # Load context at the start
  wrap-up-session/SKILL.md   # Update docs at the end
```
