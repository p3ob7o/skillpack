---
name: session-manager
description: Manage development sessions with two commands. Use /start-session to load project context and /wrap-up-session to update documentation before ending.
---

# Session Manager

Orchestrates development session management by coordinating two sub-skills.

## Commands

- `/start-session` - Load project context at the beginning of a session
- `/wrap-up-session` - Update documentation before ending a session

## Workflow

When invoked directly, ask the user which command they'd like to run, then invoke the appropriate sub-skill:

- For starting a session: `Skill(command="start-session")`
- For wrapping up: `Skill(command="wrap-up-session")`
