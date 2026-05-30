# Design system — palette, type, content rules

The Automattic deck system is typographic, white-and-blue, generously padded, with **one accent color** doing every highlight. Reverse-engineered from the source Automattic presentation template PDF. **Targets 1920×1080**; `deck-stage.js` scales the canvas to fit any viewport.

## The three colors

| Token | Hex | Use |
|---|---|---|
| `--white` | `#FFFFFF` | Default slide surface (most slides). |
| `--blue` | `#4285F4` | Cover + closing surfaces. Section-divider numerals. Page headers. Metric digits. Current TOC item. Attribution. Image placeholders. The occasional emphasis word. **Every accent.** |
| `--black` | `#000000` | Section-divider surface (alternate to blue). Body text on white. |

Greyscale support:
| Token | Hex | Use |
|---|---|---|
| `--ink` | `#111` | Default body text on white surfaces. |
| `--ink-soft` | `#3A3A3A` | Lower-emphasis body. |
| `--ink-mute` | `#8A8A8A` | Footnotes, page numbers, captions. |
| `--rule` | `#E5E5E5` | Hairline table dividers. |
| `--ornament` | `#EFEFEF` | The giant pale grey close-quote behind pull quotes. |

That's it. No additional colors. Don't add a "secondary accent" or a "warning red." The blue does everything.

## Type scale (1920×1080)

| Class | Size | Weight | Role |
|---|---|---|---|
| `t-cover` | 180px | 600 | Cover H1, "Text!" emphasis page. |
| `t-h1` | 110px | 600 | Section divider H1. |
| `t-divnum` | 360px | 600 / blue | Giant numeral on section dividers. |
| `t-h2` / `page-header` | 64px | 600 / blue | Page header (slide titles). |
| `t-section` | 52px | 600 | Multi-line section title (intro paragraph). |
| `t-quote` | 72px | 600 | Pull quotes. |
| `t-mega` | 180px | 600 | Metric numbers (split blue digit + black unit). |
| `t-toc` | 48px | 600 | TOC items. |
| `t-h3` | 32px | 600 | Column sub-headers. |
| `t-lead` | 32px | 400 | Cover subtitle, lead body. |
| `t-body` | 22px | 400 | Body. |
| `t-small` | 18px | 400 | Author cards, captions. |
| `t-foot` | 14px | 400 / muted | Footnote, page number. |
| `t-eyebrow` | 14px | 600 / tracked 0.22em | Chrome labels (wordmark). |

Family: **Inter** at 400/500/600/700. (Substitute for Maison Neue, which is licensed.) Mono: **JetBrains Mono** for code, handoff slides, footnote ornaments.

Tracking: tight on display (`-0.02em` to `-0.05em`). Loose on eyebrow/wordmark (`0.22em`).

## Spacing

8pt grid via `--s-1` (8px) through `--s-8` (128px). Slide gutter: **96px horizontal × 88px vertical**. Most slides use one column with massive whitespace, or a 2/3-column grid with gap `--s-6` (64px) or `--s-7` (96px).

## What the deck does NOT have

- **No drop shadows.** Anywhere.
- **No rounded corners.** Everything is sharp rectangles.
- **No gradients.** Solid fills only.
- **No animations.** Static slides. (The deck's print export is the canonical form.)
- **No icon set.** Bullets are filled discs. The only branded mark is the Automattic O monogram. Right arrows are unicode `→` at 96px / weight 300.
- **No emoji.**
- **No exclamation marks** (with one playful exception: the "Text!" emphasis page).

If you find yourself reaching for any of these, the deck-template style does not need them. Use whitespace and typography instead.

## Content rules

- **Sentence case** for titles. ("Multiple rows and columns to organise your data into" — not Title Case.) Two-line titles are common and intentional; use a hard `<br/>`.
- **Curly quotes are avoided** in pull quotes — the visible quote text has no surrounding quotation marks at all. The giant pale-grey `&rdquo;` ornament behind it does the work of indicating a quote.
- **Numbered TOCs** use the form `1. Introduction` / `2. The problem`. The current section gets `class="current"` (rendered in blue).
- **People are tagged Name / Role / Location.** Name is **bold**, role and location are regular weight, slightly muted.
- **Footnotes are numeric**, set in a small grey block top-right. Pair `<sup>1</sup>` on the metric label with a matching `<li>` in `.footnotes`.
- **Numbers split** as `<span class="num">100</span><span class="unit">B</span>` — num blue, unit black, same size.
- **Tone is plainspoken** and slightly playful. Section blurbs read like notes between teammates ("making the web a better place", "text and images are placeholders, replace content without altering layout").

## Surfaces

| Surface | When to use |
|---|---|
| `.surface-white` | Default. Almost every slide. |
| `.surface-blue` | Cover and closing only. (Optional: emphasis pages, sparingly.) |
| `.surface-black` | Section dividers (alternates with `.surface-white` quiet dividers). |
| `.surface-tint` | Very pale blue (`--blue-tint`). Rare. Use for a "soft" page tint. |

Don't mix surfaces within a single deck section. Don't add a fourth surface.

## Brand marks

The starter deck inlines two SVG symbols, both using `currentColor`:

- `#automattic-o` — the standalone O monogram. Used bottom-left on every content slide.
- `#automattic-logotype` — the full AUTOMATTIC wordmark. Used top-left on the cover and the "Text!" emphasis page, centered on the closing slide.

Because they're `currentColor`, the same symbol renders in the right color on every surface — the surface CSS rule (`color: var(--white)` on `.surface-blue` / `.surface-black`) takes care of it. No black/white file split.

## Known caveats to flag to the user

- **Font is Inter, not Maison Neue.** Maison Neue is licensed (Milieu Grotesque) and not on Google Fonts. Visual rhythm is close but not identical. To use real Maison Neue, drop the webfont files alongside the deck HTML and update `--font-sans`.
- **Logos are Automattic-internal.** Bundled assumes internal/personal use. For external publication, confirm the user has the right to use them.
- **The 15 layouts cover the major patterns** in the source template's 20-slide condensed version. The original 62-page template has more variants; they're all derivable from these same primitives.
