# deck-builder

Version **1.0.1**. Two skills for building and presenting single-file HTML slide decks.

## What it does

- **slide-deck-creator** — builds a typography-first deck (white-and-blue, sentence case, one accent color, no animations) as one self-contained HTML file with CSS, JS, and SVG inlined. Fonts and remote images may still load from the network. The starter deck ships **15 layouts**: Cover; Intro paragraph + image; Table of contents; TOC with current section in blue; Section divider (black); Numeric layout; "Text!" emphasis page; Bulleted list; Table; Pull quote; Three columns; Long-form body + images; Numbered data (1–3); Section divider (white/quiet); Closing. Presenter-notes mode (press `P`) adds dual timers and two-way nav sync. Can convert a `.pptx` to web.
- **presenter-notes** — adds a presenter-notes popup (timers, nav sync, rehearsal tools) to an existing HTML deck, whether built by slide-deck-creator or not.

## Skills

| Skill | Claude Code | Codex / Cursor / Grok Bot |
|-------|-------------|---------------------------|
| `slide-deck-creator` | `/deck-builder:slide-deck-creator` | `/slide-deck-creator` |
| `presenter-notes` | `/deck-builder:presenter-notes` | `/presenter-notes` |

## Install

Shared marketplace steps: [skillpack install](../../README.md#install).

```
# Claude Code
/plugin install deck-builder@skillpack

# Codex (after marketplace add)
codex plugin add deck-builder@skillpack

# Cursor / Grok Bot
# Import https://github.com/p3ob7o/skillpack, then install deck-builder
```

## Usage

### slide-deck-creator

```
[describe the deck you want, or point at a .pptx]
```

### presenter-notes

```
[point at your existing HTML deck]
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
