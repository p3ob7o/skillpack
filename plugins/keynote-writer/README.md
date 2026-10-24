# keynote-writer

Version **1.0.0**. Turn a braindump or transcript into a TED-quality keynote outline.

## What it does

Produces three sections:

1. **FLOW** — a 10–20 bullet narrative arc for the talk
2. **DESIRED TAKEAWAY** — the one sentence you want the audience to leave with
3. **PRESENTATION** — slide-by-slide: ultra-short on-screen text, an AI image prompt, and speaker notes

Speaker notes go through [writewell](../writewell/README.md) when that plugin is installed, so they read like stage notes rather than machine prose. Writewell is recommended for the voice pass — not a hard install dependency.

## Skills

| Skill | Claude Code | Codex / Cursor / Grok Bot |
|-------|-------------|---------------------------|
| `keynote-writer` | `/keynote-writer:keynote-writer` | `/keynote-writer` |

## Install

Shared marketplace steps: [skillpack install](../../README.md#install).

```
# Claude Code
/plugin install keynote-writer@skillpack

# Codex (after marketplace add)
codex plugin add keynote-writer@skillpack

# Cursor / Grok Bot
# Import https://github.com/p3ob7o/skillpack, then install keynote-writer
```

## Usage

Paste raw material — notes, a braindump, or a transcript:

```
[paste your braindump or transcript here]
```

Typical triggers: "turn this into a keynote", "outline a TED talk from these notes", "build a talk from this braindump".

## Structure

```
skills/
  keynote-writer/
    SKILL.md
```
