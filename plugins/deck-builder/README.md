# deck-builder

Two skills for building and presenting HTML slide decks.

## Skills

### slide-deck-creator

Creates a single-file HTML slide deck in a typography-first design (white-and-blue, sentence case, one accent color, no animations). The output is one self-contained HTML file with all CSS, JS, and SVG inlined — only fonts and remote images load from the internet. Bundles 15 layout patterns (cover, TOC, section dividers, metrics, bulleted list, table, pull quote, columns, numbered data, closing) plus a presenter-notes mode (press `P`) with dual timers and two-way nav sync. Can also convert a PowerPoint (`.pptx`) to web.

```
[describe the deck you want, or point at a .pptx]
```

In Claude Code the command is `/deck-builder:slide-deck-creator`. Elsewhere, invoke the `slide-deck-creator` skill.

### presenter-notes

Adds a presenter-notes popup window to an *existing* HTML slide presentation — timers, navigation sync, and rehearsal tools. Use it on a deck built by `slide-deck-creator` or any other HTML deck.

```
[point at your existing HTML deck]
```

In Claude Code the command is `/deck-builder:presenter-notes`. Elsewhere, invoke the `presenter-notes` skill.

## Install

See the [skillpack install steps](../../README.md#install).

Claude Code:

```
/plugin marketplace add p3ob7o/skillpack
/plugin install deck-builder@skillpack
```

Codex, after `codex plugin marketplace add p3ob7o/skillpack`:

```
codex plugin add deck-builder@skillpack
```

Cursor and Grok Bot: import `https://github.com/p3ob7o/skillpack` and install deck-builder.

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
