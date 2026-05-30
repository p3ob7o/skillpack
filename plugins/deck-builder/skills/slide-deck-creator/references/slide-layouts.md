# Slide layouts — copy-paste reference

The 15 layouts shipped in `assets/starter-deck.html`. Every slide is a `<section class="slide surface-*">` inside the `<deck-stage>` wrapper. The starter deck already contains one example of each — when building a real deck, **delete the layouts you don't need and duplicate the ones you do**, replacing copy.

## Surface rules

- `.surface-white` — default. Use for almost every slide.
- `.surface-blue` — cover + closing only.
- `.surface-black` — section dividers (used sparingly, alternates with white section dividers).

Don't mix surfaces within a section. Don't invent a fourth surface.

## Chrome

Every **content** slide (not cover, not closing) gets the O monogram bottom-left and a page number bottom-right:

```html
<svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
<div class="page-num">07</div>
```

The cover, the closing, and the "Text!" emphasis page get the full AUTOMATTIC wordmark top-left instead:

```html
<svg class="wordmark" aria-hidden="true" viewBox="0 0 1296 432"><use href="#automattic-logotype" /></svg>
```

Both SVGs use `currentColor`, so they automatically render in the correct color for the surface — no need to pick a "white variant."

---

## 1. Cover — blue surface

Wordmark top-left, big display H1, lead paragraph, up to 3 author cards on the bottom row, right-arrow on the right.

```html
<section class="slide surface-blue" data-screen-label="01 Cover">
  <svg class="wordmark" aria-hidden="true" viewBox="0 0 1296 432"><use href="#automattic-logotype" /></svg>
  <div style="margin-top: 200px; flex: 1;">
    <h1 class="t-cover">Title<br/>Second line</h1>
    <p class="t-lead" style="margin-top: var(--s-6); max-width: 1100px;">
      A short subtitle or lead, two lines max.
    </p>
  </div>
  <div style="display: grid; grid-template-columns: repeat(3, 300px) 1fr; gap: var(--s-5); align-items: end;">
    <div style="font-size: 24px; line-height: 1.4;">
      <div style="font-weight: 700;">Name One</div>
      <div style="opacity: 0.85;">Role</div>
      <div style="opacity: 0.85;">City</div>
    </div>
    <!-- repeat 0-2 more author cards -->
    <div style="justify-self: end;" class="arrow-right" aria-hidden="true">→</div>
  </div>
</section>
```

## 2. Intro paragraph + image — white

Long display paragraph (52px) on the left, image placeholder on the right.

```html
<section class="slide surface-white" data-screen-label="02 Intro paragraph">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--s-8); height: 100%; align-items: start;">
    <div style="padding-top: 40px;">
      <h2 class="t-section" style="max-width: 760px;">
        One long sentence in display weight, used as the page's anchor. Keep it to ~30 words.
      </h2>
      <p class="t-foot mt-5" style="max-width: 600px;">
        Optional caption beneath, in muted grey.
      </p>
    </div>
    <div class="image-slot gray" style="width: 720px; height: 820px; justify-self: end;">image placeholder</div>
  </div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">03</div>
</section>
```

## 3. Table of contents — white

Plain numbered list, all in black ink.

```html
<section class="slide surface-white" data-screen-label="03 Table of contents">
  <div style="margin-top: 120px;">
    <ol class="toc" style="display: flex; flex-direction: column; gap: 12px;">
      <li><span class="num">1.</span><span>Introduction</span></li>
      <li><span class="num">2.</span><span>The problem</span></li>
      <li><span class="num">3.</span><span>What changed</span></li>
      <li><span class="num">4.</span><span>The solution</span></li>
      <li><span class="num">5.</span><span>What's next</span></li>
    </ol>
  </div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">04</div>
</section>
```

## 4. TOC with current section in blue — white

Same as #3 but add `class="current"` to the active `<li>`. Useful as a recurring "you are here" marker between sections.

```html
<li class="current"><span class="num">1.</span><span>Introduction</span></li>
```

## 5. Section divider — black surface

White headline top-left, giant blue numeral bottom-right. The numeral can be the section number or just a visual beat.

```html
<section class="slide surface-black" data-screen-label="05 Section divider · black">
  <h1 class="t-h1" style="color: var(--white); max-width: 1400px;">
    Section title<br/>second line
  </h1>
  <div style="position: absolute; right: var(--gutter-x); bottom: 120px;" class="t-divnum">2</div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">06</div>
</section>
```

## 6. Numeric layout — white

Blue page header, 3 mega-metrics with split blue digit + black unit, footnotes top-right.

```html
<section class="slide surface-white" data-screen-label="06 Numeric layout">
  <h2 class="page-header" style="max-width: 900px;">
    Here are numbers and the<br/>sources to them
  </h2>
  <div class="footnotes">
    <ol>
      <li>Data taken from source one</li>
      <li>Data taken from source two</li>
      <li>Data taken from source three</li>
    </ol>
  </div>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--s-7); margin-top: auto; padding-bottom: 80px;">
    <div class="metric">
      <div class="value"><span class="num">100</span><span class="unit">B</span></div>
      <div class="label">Metric label<sup>1</sup></div>
    </div>
    <!-- 2 more metrics -->
  </div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">07</div>
</section>
```

Split numbers as `<span class="num">100</span><span class="unit">B</span>` — num is blue, unit is black, same size. Footnote markers are `<sup>1</sup>` on the label, with matching `<li>` in `.footnotes`.

## 7. "Text!" emphasis page — white surface, blue word

Used for big rhetorical beats. Same shape as the cover but inverted (white surface, blue word).

```html
<section class="slide surface-white" data-screen-label="07 Emphasis page">
  <svg class="wordmark" aria-hidden="true" viewBox="0 0 1296 432"><use href="#automattic-logotype" /></svg>
  <div style="margin-top: 220px; flex: 1;">
    <h1 class="t-cover" style="color: var(--blue);">Text!</h1>
    <p class="t-lead mt-6" style="max-width: 900px; color: var(--ink);">
      Short subtitle, two lines max.
    </p>
  </div>
  <!-- optional author cards row, same shape as cover -->
</section>
```

## 8. Bulleted list — white

Left-rail page header, right column of filled-disc bullets.

```html
<section class="slide surface-white" data-screen-label="08 Bulleted list">
  <div style="display: grid; grid-template-columns: 380px 1fr; gap: var(--s-7); margin-top: 60px;">
    <h2 class="page-header">Header</h2>
    <ul class="bullets" style="font-size: 28px; line-height: 1.45; max-width: 1100px;">
      <li>First point — one sentence, two lines max.</li>
      <li>Second point.</li>
      <li>Third point.</li>
      <li>Fourth point.</li>
      <li>Fifth point.</li>
      <li>Sixth point.</li>
    </ul>
  </div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">09</div>
</section>
```

Soft cap: ~6 bullets. More than that, split the slide.

## 9. Table — white

Blue page header + hairline table. Up to 4 data columns + 1 row-header column.

```html
<section class="slide surface-white" data-screen-label="09 Table">
  <h2 class="page-header" style="max-width: 1100px;">
    Multiple rows and columns<br/>to organise your data into
  </h2>
  <table class="data" style="margin-top: var(--s-7);">
    <thead>
      <tr><th></th><th>Col 1</th><th>Col 2</th><th>Col 3</th><th>Col 4</th></tr>
    </thead>
    <tbody>
      <tr><th>Row A</th><td>Do</td><td>Re</td><td>Mi</td><td>Fa</td></tr>
      <!-- more rows -->
    </tbody>
  </table>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">10</div>
</section>
```

## 10. Pull quote — white

Plain quote text + giant pale grey `&rdquo;` ornament behind it + blue attribution. **No surrounding quotation marks on the visible text.** No em-dash on attribution.

```html
<section class="slide surface-white" data-screen-label="10 Pull quote">
  <div class="quote-wrap" style="margin-top: 120px; flex: 1;">
    <div class="quote-ornament" aria-hidden="true">&rdquo;</div>
    <h2 class="t-quote" style="max-width: 1500px;">
      The quote, set plain. No curly quotes around it.
    </h2>
    <div class="mt-5 t-body accent">Attribution Name</div>
  </div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">11</div>
</section>
```

## 11. Three columns — white

Page header + 3 sub-headed columns with bullets each.

```html
<section class="slide surface-white" data-screen-label="11 Three columns">
  <h2 class="page-header" style="max-width: 900px;">
    Three columns for<br/>comparing things
  </h2>
  <div class="grid-3 mt-6" style="flex: 1; align-content: start;">
    <div>
      <h3 style="color: var(--ink);">Header one</h3>
      <div class="muted t-small mt-3">Subtitle</div>
      <ul class="bullets mt-4" style="font-size: 20px;">
        <li>Point.</li>
        <li>Point.</li>
      </ul>
    </div>
    <!-- column 2 and 3 -->
  </div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">12</div>
</section>
```

## 12. Long-form body + images — white

Three-column grid: text + screenshot placeholder + photo placeholder.

```html
<section class="slide surface-white" data-screen-label="12 Long-form with images">
  <div style="display: grid; grid-template-columns: 1fr 1fr 480px; gap: var(--s-7); margin-top: 30px; flex: 1;">
    <div>
      <h2 class="page-header">Header</h2>
      <p class="t-body mt-4" style="line-height: 1.55;">
        A short but important paragraph introducing the content. Around 50 words.
      </p>
      <ul class="bullets mt-4" style="font-size: 20px;">
        <li>Point.</li>
        <li>Point.</li>
      </ul>
    </div>
    <div class="image-slot gray">screen capture</div>
    <div class="image-slot">brand photo</div>
  </div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">13</div>
</section>
```

`.image-slot.gray` = grey diagonal-stripe screenshot placeholder. Plain `.image-slot` = solid blue photo placeholder.

## 13. Numbered data (1-3) — white

Page header + 3 blue numerals (1, 2, 3) with paragraphs underneath. Use when you have three ordered points that aren't bullets.

```html
<section class="slide surface-white" data-screen-label="13 Numbered data 1-3">
  <h2 class="page-header" style="max-width: 900px;">
    Header about numbered<br/>data below
  </h2>
  <div class="grid-3 mt-6" style="flex: 1; align-content: start;">
    <div>
      <div class="ord-num">1</div>
      <p class="t-body mt-4" style="line-height: 1.5;">First paragraph.</p>
    </div>
    <div>
      <div class="ord-num">2</div>
      <p class="t-body mt-4" style="line-height: 1.5;">Second paragraph.</p>
    </div>
    <div>
      <div class="ord-num">3</div>
      <p class="t-body mt-4" style="line-height: 1.5;">Third paragraph.</p>
    </div>
  </div>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">14</div>
</section>
```

## 14. Section divider — white (quiet variant)

Just the black headline, no numeral. Use as a closing beat to a section, or anywhere the black variant would feel too loud.

```html
<section class="slide surface-white" data-screen-label="14 Section divider · white">
  <h1 class="t-h1" style="max-width: 1500px; margin-top: 100px;">
    Section title<br/>second line
  </h1>
  <svg class="o-mark" aria-hidden="true"><use href="#automattic-o" /></svg>
  <div class="page-num">15</div>
</section>
```

## 15. Closing — blue

Centered AUTOMATTIC wordmark on full-bleed blue. No page number. No O monogram.

```html
<section class="slide surface-blue" data-screen-label="15 Closing">
  <svg aria-hidden="true" viewBox="0 0 1296 432" style="width: 720px; margin: auto;"><use href="#automattic-logotype" /></svg>
</section>
```

---

## Composing variants

The 15 layouts cover the major patterns. For bespoke needs, compose from the same primitives:

- **More metrics per row** → repeat the `.metric` block in a 4-up or 5-up grid (drop the gap slightly).
- **More numbered items (4-6)** → repeat `.ord-num` in a `grid-4` or `grid-3 grid-3` two-row layout.
- **Code slide** → swap the body for `<pre class="code">…</pre>` (mono, 20px). Up to ~10 lines.
- **Image-only slide** → drop a full-bleed `<div class="image-slot">` filling the canvas inside a white-surface slide. Skip the page header.

Don't invent new tokens. If a slide needs something the design system doesn't have, prefer composition over extension.
