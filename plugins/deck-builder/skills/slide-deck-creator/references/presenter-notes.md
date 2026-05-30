# Presenter notes — schema + integration

Presenter notes are **built into the starter deck**. There's nothing to wire up — they ship in `assets/starter-deck.html` and work out of the box.

## What ships

- A `<script type="application/json" id="speaker-notes">` block with one entry per slide.
- A presenter-notes popup launcher that listens for **P** and opens an 860×900 window.
- A `BroadcastChannel('slide-sync')` keeping the popup and the main deck in lockstep (popup → deck and deck → popup).
- **Current + next slide thumbnails** rendered side-by-side at the top of the popup. Each is an iframe of the deck itself with `?_snthumb=1#N` — a URL flag `deck-stage.js` recognises specifically to suppress its own rail inside presenter popups, leaving just the slide.
- Dual timers (global elapsed + per-slide), per-slide allocated seconds, color-coded warning + over-time states.
- Bullet talking points per slide.

## How to use it as a deck author

When generating a deck from user content, update the `<script type="application/json" id="speaker-notes">` array so it has **exactly one entry per slide**, in slide order.

### Schema

```json
[
  {
    "title": "Short label",
    "seconds": 30,
    "notes": [
      "First spoken bullet.",
      "Second spoken bullet."
    ]
  }
]
```

| Field | Type | Notes |
|---|---|---|
| `title` | string | Shown at the top of the popup. Keep short (~30 chars). |
| `seconds` | integer | Allocated time for this slide. Drives the slide timer's warning threshold (5s before allocated → green) and over-time threshold (at allocated → orange-red). Also summed across all slides into the global target. |
| `notes` | string[] | Bullet talking points. Rendered with blue dots. Aim for 1–5 bullets, ≤16 words each. |

If you don't have real notes yet, ship the array with reasonable placeholders — every slide should have an entry so the popup doesn't drop to `Slide N` fallback titles.

## Keyboard

In the **main deck window**:
- `←` `→` / `PgUp` `PgDn` / `Space` — navigate
- `Home` `End` — first / last slide
- `R` — reset to slide 1
- `1`–`9` — jump to slide N
- **`P` — open presenter notes popup**
- **`T` — toggle the left-rail thumbnail strip** (persists per browser via `localStorage['deck-stage.railVisible']`)

In the **popup window**:
- `←` `→` `↑` `↓` — navigate (the main window follows)
- `Space` — start / pause the timers
- `R` — reset both timers

The popup also has an editable timing badge (click the `30s` pill to change a slide's allocated seconds live).

## How the sync works (don't break it)

`deck-stage.js` dispatches a `slidechange` CustomEvent on the `<deck-stage>` element whenever the active slide changes (including init and reorder/skip mutations). The bundled launcher subscribes to this and rebroadcasts via `BroadcastChannel('slide-sync')`. The popup, also on the same channel, listens for `slideChanged` and updates its UI. When the popup navigates (Prev/Next buttons or arrow keys), it sends `goToSlide` back, and the launcher calls `deck.goTo(index)` on the main window.

`deck-stage.js` itself is untouched by the launcher — no monkey-patching, no internals. The integration is purely the public `slidechange` event + the `goTo()` API.

If you ever need to integrate presenter notes into a deck that doesn't use this skill, the launcher source is at the bottom of `starter-deck.html` (search for `openPresenterNotes`). It's about 200 lines of self-contained JS.

## Popup blocker

The first time the user presses `P`, the browser may block the popup. The launcher logs a warning and returns silently. Tell the user to allow popups for the page (or use a `file://` URL where blockers tend to be off) and press `P` again.

## Color choices

The popup uses a dark theme (`#1a1a1a` background) — appropriate for dimly-lit presenting environments — with the Automattic blue (`#4285F4`) as the primary accent on the Start/Resume button and bullet dots. Warning (approaching allocated time) is `#9FD5CA` green; over-time is `#EE6221` orange-red. These last two are inherited from the original presenter-notes template and provide clearer signaling than blue/white would.
