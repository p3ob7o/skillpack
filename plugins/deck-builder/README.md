# deck-builder

Two skills for building and presenting HTML slide decks.

## Skills

### slide-deck-creator

Creates a single-file HTML slide deck in a typography-first design (white-and-blue, sentence case, one accent color, no animations). The output is one self-contained HTML file with all CSS, JS, and SVG inlined — only fonts and remote images load from the internet. Bundles 15 layout patterns (cover, TOC, section dividers, metrics, bulleted list, table, pull quote, columns, numbered data, closing) plus a presenter-notes mode (press `P`) with dual timers and two-way nav sync. Can also convert a PowerPoint (`.pptx`) to web.

```
/deck-builder:slide-deck-creator

[describe the deck you want, or point at a .pptx]
```

### presenter-notes

Adds a presenter-notes popup window to an *existing* HTML slide presentation — timers, navigation sync, and rehearsal tools. Use it on a deck built by `slide-deck-creator`, the `frontend-slides` skill, or any HTML deck.

```
/deck-builder:presenter-notes

[point at your existing HTML deck]
```

## Install

```
/plugin marketplace add p3ob7o/skillpack
/plugin install deck-builder@skillpack
```

## Structure

```
skills/
  slide-deck-creator/
    SKILL.md
    assets/starter-deck.html
    references/            # design system, layouts, ppt conversion, presenter notes
  presenter-notes/
    SKILL.md
    references/popup-implementation.md
```
