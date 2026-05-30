# keynote-writer

Transform a stream-of-consciousness braindump — often an audio transcript — into a TED-quality keynote outline.

## What it does

Produces three sections:

1. **FLOW** — a 10–20 bullet narrative arc for the talk
2. **DESIRED TAKEAWAY** — the one sentence you want the audience to leave with
3. **PRESENTATION** — slide-by-slide, each with ultra-short on-screen text, an AI image prompt, and exact speaker notes

The final speaker notes are passed through [writewell](../writewell/) so they sound like you on stage rather than like a machine.

## Install

```
/plugin marketplace add p3ob7o/skillpack
/plugin install keynote-writer@skillpack
```

## Usage

Give it raw material — notes, a braindump, or a transcript:

```
/keynote-writer

[paste your braindump or transcript here]
```

Triggers on things like "turn this into a keynote", "outline a TED talk from these notes", or "build me a talk from this braindump".

## Structure

```
skills/
  keynote-writer/
    SKILL.md    # The keynote outliner
```
