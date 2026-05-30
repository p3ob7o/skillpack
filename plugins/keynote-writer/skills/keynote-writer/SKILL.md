---
name: keynote-writer
description: Transform a stream-of-consciousness braindump (often an audio transcript) into a TED-quality keynote outline. Produces three sections — FLOW (10-20 bullet narrative arc), DESIRED TAKEAWAY (one-sentence landing point), and PRESENTATION (slide-by-slide with ultra-short on-screen text, AI image prompt, and exact speaker notes). Use when the user wants to turn raw notes, a braindump, a transcript, or rambling ideas into a structured keynote — e.g. "turn this into a keynote", "outline a TED talk from these notes", "draft a keynote from this transcript", "build me a talk from this braindump". Designed for Paolo's external conference and internal all-hands talks; the final speaker notes are passed through /writewell:writewell so they sound like him on stage.
---

# Keynote Writer

## What this skill does

Turns a messy braindump into a TED-grade keynote outline. The input is usually transcribed audio — stream of consciousness, half-formed ideas, repetitions. The output is a tight narrative with slides and exact speaker notes the user can rehearse from.

This skill produces **content**, not slide files. No .key, .pptx, or HTML — just the structured outline. If the user wants those files generated after, hand off to `frontend-slides`, `pptx`, or `presentations:craft`.

## Pre-flight: calibrate before drafting

Before writing anything, ask:

1. **Keynote length in minutes?** (drives slide count)
2. **Venue, if not obvious from context?** External conference and internal all-hands have different tonal allowances (more polish vs more candor). Skip if already clear.

Slide-count guideline:
- Sparse / thin input → ~1 slide per minute
- Rich / dense input → up to ~2 slides per minute
- Default: pick a number in that band based on input density

## Workflow

Follow these steps in order. Do not start drafting the PRESENTATION section before completing steps 1–3 in your head.

### 1. Find the real takeaway

Read the entire braindump. Determine the single practical takeaway the audience should leave with. One sentence. This becomes the DESIRED TAKEAWAY and the gravitational center every slide pulls toward. If you can't name it, ask the user before continuing.

### 2. Build the narrative arc

Sketch the story end-to-end before any slide. Think TED structure: hook → tension → reframe → resolution → call to action. The arc must land on the takeaway from step 1 — not arrive there by accident.

Cut anything from the braindump that doesn't serve the arc, even if it's a "good" point. Keynotes get killed by good points that don't belong.

### 3. Map the arc to slides

Translate the arc into N slides (where N matches the length/density calibration above). Each slide is one beat of the story. The sequence of slide titles, read alone, should already feel like the talk.

### 4. Fill in each slide

For each slide, produce:
- **Title** — the slide's role in the arc (not a label)
- **On-screen content** — ultra short. A single word, a phrase, or a short sentence. **Never bullet lists. Never extended copy.** What appears behind the speaker.
- **Image description** — a prompt for an AI image generator. Visual, concrete, evocative; specifies subject, style, mood, framing.
- **Speaker notes** — the exact words the speaker will say, written as bullets of **≤16 words each**. These are spoken lines, not written prose. Read them aloud while drafting — if they trip the tongue, rewrite.

### 5. Quality gate

Read the FLOW bullets back-to-back, then read the speaker notes back-to-back. Ask: *Does this land?* If the narrative wobbles, repeats, or arrives at the takeaway by accident — **start over from step 2**. Do not patch a bad arc; rebuild it.

### 6. Voice pass

Invoke `/writewell:writewell` on the final speaker notes so they match the speaker's voice (Paolo, in this setup). On-screen content and image descriptions don't need this — only the spoken lines.

## Output format

Output exactly these three sections, in this order, as Markdown.

```
## FLOW

- [10-word-max bullet, one per slide, 10–20 bullets total]
- ...

## DESIRED TAKEAWAY

[One sentence. The single thing the audience leaves with.]

## PRESENTATION

### Slide 1 — [Title]

**On-screen:** [single word / phrase / short sentence]

**Image:** [AI image generator prompt]

**Speaker notes:**
- [≤16 word spoken bullet]
- [≤16 word spoken bullet]
- ...

### Slide 2 — [Title]
...
```

## Guardrails

- **No bullet lists on slides.** On-screen content is what the audience sees; bullets are a crutch. If you're tempted to put bullets on a slide, that's two slides.
- **No filler slides.** Every slide earns its place in the arc. "Agenda" and "Thank you" slides are usually filler — cut unless explicitly asked.
- **Speaker notes are spoken, not written.** Contractions, short sentences, room for breath. Read them aloud.
- **Don't lift sentences verbatim from the braindump.** The braindump is raw material, not a script. Compress, sharpen, rearrange.
- **The takeaway drives everything.** If a slide doesn't move the audience closer to the takeaway, it doesn't belong.
