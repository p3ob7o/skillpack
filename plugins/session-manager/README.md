# session-manager

Bookend your development sessions: load context when you start, capture what changed before you stop.

## Skills

### session-manager

The umbrella skill — explains the two-command workflow and when to reach for each.

### start-session

Loads project context from `CLAUDE.md` and `DOCUMENTATION.md` at the start of a session, so Claude picks up where you left off.

```
/session-manager:start-session
```

### wrap-up-session

Updates `CLAUDE.md` and `DOCUMENTATION.md` with the changes made during the session before you end it.

```
/session-manager:wrap-up-session
```

## Install

```
/plugin marketplace add p3ob7o/skillpack
/plugin install session-manager@skillpack
```

## Structure

```
skills/
  session-manager/SKILL.md   # The two-command overview
  start-session/SKILL.md     # Load context at the start
  wrap-up-session/SKILL.md   # Update docs at the end
```
