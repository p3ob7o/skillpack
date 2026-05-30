---
name: wrap-up-session
description: Update CLAUDE.md and DOCUMENTATION.md with changes made during the session before ending.
---

# Wrap Up Session

Update project documentation before ending a session.

**When to use:** Before ending a coding session, especially after making significant changes.

**Workflow:**

1. Run `git diff` and `git log` to identify changes made this session
2. Review what was modified (new files, changed files, deleted files)
3. Look for `CLAUDE.md` and `DOCUMENTATION.md` in the repo root
4. **If they don't exist yet, create them:**
   - `CLAUDE.md` — project instructions, conventions, key commands, and development guidelines. Structure it based on what you learn from the codebase and session.
   - `DOCUMENTATION.md` — project overview, architecture, current status, and what's been built. Capture the state of the project as it stands now.
5. If they already exist, read them and determine what needs updating:
   - New features, components, or files added
   - Changed architecture or project structure
   - New patterns or conventions established
   - Updated commands, scripts, or configuration
   - Progress on next steps or pending items
6. Apply the updates directly — do NOT ask for confirmation first
7. Commit the documentation changes

**Output format:**

```
## Session Wrap-Up

### Changes This Session
{summary of git changes}

### Documentation Updates Applied

**CLAUDE.md:**
- {list of updates, or "No updates needed"}

**DOCUMENTATION.md:**
- {list of updates, or "No updates needed"}
```

## Important Notes

- When creating files from scratch, look at the codebase to populate them meaningfully — don't create empty shells
- When updating existing files, preserve their structure and only touch sections affected by changes
- Keep updates concise and factual
- Commit documentation changes with a descriptive message
