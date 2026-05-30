---
name: start-session
description: Load project context from CLAUDE.md and DOCUMENTATION.md at the start of a development session.
---

# Start Session

Load project context at the beginning of a development session.

**When to use:** At the start of any coding session to understand the current state of the project.

**Workflow:**

1. Look for `CLAUDE.md` and `DOCUMENTATION.md` in the repo root
2. If neither file exists, **exit quietly** — just say "No session files found" and stop. Don't create anything.
3. If one or both exist, read them
4. Check git status for any uncommitted changes
5. Check recent git log for recent work
6. Provide a concise summary to the user covering:
   - Project name and purpose (from the docs)
   - Current branch and any uncommitted work
   - Recent commits (last 5-10)
   - Key things to know before starting work
   - Any pending items or next steps mentioned in the docs

**Output format:**

```
## Session Started

**Project:** {project name}
**Branch:** {current_branch}
**Status:** {clean/uncommitted changes}

### Recent Activity
{list of recent commits}

### Current State
{summary from docs — what's built, what's in progress}

### Ready to Work
{any pending items, uncommitted work, or next steps}
```

## Important Notes

- Keep the summary short and actionable — don't dump the entire docs
- If only one of the two files exists, work with what's there
- Don't modify any files during start-session
