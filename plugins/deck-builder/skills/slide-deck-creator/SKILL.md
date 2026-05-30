---
name: slide-deck-creator
description: Create a single-file HTML slide deck in the Automattic typography-first design (white-and-blue, sentence case, one accent color, no animations). Output is one self-contained HTML file with all CSS, JS, and SVG inlined — only fonts and remote images load from the internet. Bundles 15 layout patterns (cover, TOC, section dividers, metrics, bulleted list, table, pull quote, columns, numbered data, closing) plus presenter-notes mode (press P) with dual timers and two-way nav sync. Use when the user wants a slide deck, presentation, talk deck, pitch deck, all-hands deck, or wants to convert a PowerPoint (.pptx) to web — e.g. "make me a slide deck", "build a presentation", "turn this into slides", "create a deck", "convert this pptx". Designed for Automattic internal and external use; output deck is single-file and easy to share.
---

# Slide Deck Creator

Generate a **single-file HTML deck** in the Automattic design system. The output is one `.html` file — all CSS, JS, and SVG inlined; only fonts and any user-supplied remote images load from the network. Includes presenter notes mode (press **P**) out of the box.

This is **one style only.** No style picker, no preset selection. The deck is typography-first, white-and-blue, sentence case, generously padded, no animations, no shadows, no rounded corners, no gradients. If the user wants a different aesthetic, this is the wrong skill — use `frontend-slides` instead.

## Detect mode first

- **New deck** — user describes what they want to present. Go to *Content discovery*.
- **PPT conversion** — user has a `.ppt` or `.pptx`. Read `references/ppt-conversion.md`, run the extractor, confirm structure, then proceed with the standard generate step using the Automattic layouts.
- **Edit existing Automattic deck** — user has a deck previously created by this skill and wants tweaks. Read their HTML, find the slide(s) to change, edit in place. Don't regenerate from scratch.

## Content discovery (new deck)

Before generating anything, get four pieces of context via `AskUserQuestion` (one question per concept, not all at once):

1. **What's the deck about?** (Short description — 1 sentence.)
2. **Who's the audience?** (Internal Automattic team / external partners / public conference / pitch.)
3. **Roughly how many slides?** (Short 5–10 / Medium 10–20 / Long 20+ / Don't know yet.)
4. **Do they have content ready, rough notes, or just a topic?** If content is ready, have them paste it. If rough notes, organize first. If topic only, draft an outline and confirm before building.

Skip questions the user has already answered in their initial request. Don't ask about style — there isn't one to pick.

## Generate the deck

### 1. Read the layouts reference

Read `references/slide-layouts.md` for the 15 layout patterns and `references/design-system.md` for palette, type scale, and content rules. **Do not skip these** — the layouts are not derivable from the design tokens alone.

### 2. Pick a layout per slide

Each slide is one of the 15 layouts. Suggested mapping:

- Slide 1: **Cover** (layout 1, blue surface)
- Slide 2: **TOC** (layout 3) — only for decks of 8+ slides
- Slide N: **Section divider** (layout 5 black, or layout 14 white) — between major sections
- Content slides: pick from layouts 2 (intro paragraph), 6 (metrics), 8 (bullets), 9 (table), 10 (pull quote), 11 (columns), 12 (body + image), 13 (numbered data)
- Last slide: **Closing** (layout 15, blue)

Mix surfaces sparingly. Most slides are white. Black is for occasional section dividers. Blue is for cover + closing.

### 3. Copy and customize the starter

Copy `assets/starter-deck.html` to the user's output path (default: `./deck.html` in current working directory). Then **inside the `<deck-stage>` wrapper, replace the 15 sample `<section>` blocks with the user's actual slides**, using the layout markup from `references/slide-layouts.md`.

The starter file is ~115 KB. Don't try to read it before customizing — it's mostly the inline `deck-stage.js` web component (1700+ lines) which you should never modify. Use bash to copy the file, then `Edit` the specific `<section>` blocks.

### 4. Update the speaker-notes JSON

Replace the placeholder `<script type="application/json" id="speaker-notes">` array with one entry per slide. Schema and full details in `references/presenter-notes.md`. Even if the user hasn't given you real speaker notes, write reasonable placeholders — every slide should have an entry.

### 5. Verify the slide count matches

The `speaker-notes` array must have exactly as many entries as there are `<section class="slide">` elements. Verify by counting both with `grep -c '<section class="slide"' deck.html` and a manual count of the JSON array. Mismatches cause confusing popup behavior.

## Delivery

When the deck is done, tell the user:

```
Your deck is ready: <path>.html

Open in a browser:
- ← → / Space — navigate
- P — open presenter notes (popup with timers, bullets, current + next thumbnails)
- T — toggle the left-rail thumbnail strip (persists per browser)
- R — reset to slide 1
- 1-9 — jump to slide N
- Cmd/Ctrl+P → "Save as PDF" — one slide per page, no extra setup

The deck is a single file. All CSS, JS, and SVG are inlined.
Fonts (Inter + JetBrains Mono) load from Google Fonts.
```

If the user wants to convert it to PDF, mention that the browser's Save-as-PDF produces clean one-slide-per-page output — `deck-stage.js` handles the `@page` rule automatically.

## Hard rules (don't break these)

- **One file out.** The output is a single `.html` file. Don't write sibling `.css` / `.js` / `.svg` files. Don't suggest an "even simpler" output that splits things apart.
- **Don't modify `deck-stage.js`.** The 1700+ line web component in the starter file is the canonical Automattic deck shell. Modify slide content only. If something seems missing, it's almost certainly a layout or content question, not a shell question.
- **One style only.** No alternate color palettes, no font swaps, no animations, no shadows, no rounded corners, no gradients, no emoji. If the user pushes for a non-Automattic look, redirect to `frontend-slides`.
- **Density limits are non-negotiable.** Max ~6 bullets per slide. Max 3 metrics per row. Max 10 lines of code per code slide. Too much content → split into multiple slides.
- **Sentence case for titles.** Two-line titles use a hard `<br/>`. No exclamation marks (except the playful "Text!" emphasis page).
- **No surrounding quotes on pull-quote text.** The giant pale-grey `&rdquo;` ornament does the work of indicating a quote.
- **Numbers split** as `<span class="num">100</span><span class="unit">B</span>` — num blue, unit black, same size.
- **Presenter notes always included.** Don't strip out the popup launcher or the `speaker-notes` JSON tag, even if the user "doesn't need them" — they're tiny and harmless if unused.

## Reference files

| File | Read when |
|---|---|
| `references/slide-layouts.md` | Picking layouts and writing slide markup. **Read on every new deck.** |
| `references/design-system.md` | Questions about palette, type scale, spacing, content rules, or "can I add X?" |
| `references/presenter-notes.md` | Customizing the speaker-notes JSON. Wiring presenter notes into a deck NOT built by this skill. |
| `references/ppt-conversion.md` | Converting a `.ppt` or `.pptx` to a deck. |

## Caveats to flag to the user

- **Font is Inter, not Maison Neue** — Maison Neue is licensed and not on Google Fonts. The visual rhythm is close but not identical.
- **Logos are Automattic-internal.** The bundled SVGs (AUTOMATTIC wordmark, O monogram) assume internal/personal use. For external publication, confirm rights.
- **Popup blocker.** First time the user presses **P**, the browser may block the popup. Tell them to allow popups for the page (or use a `file://` URL) and press again.
