---
name: presenter-notes
description: Add a presenter notes popup window to an existing HTML slide presentation. Use when the user has an HTML slide deck (built with the frontend-slides skill or similar) and wants to add presenter notes with timers, navigation sync, and rehearsal tools. Triggers on requests like "add presenter notes", "add speaker notes", "presenter mode", or "/presenter-notes".
---

# Presenter Notes

Add a full-featured presenter notes system to any HTML slide presentation. The notes open in a popup window (press P), stay synced with the main deck via BroadcastChannel, and include dual timers for rehearsal.

## Prerequisites

- An existing HTML presentation with a `SlidePresentation` class (or equivalent) that tracks `currentSlide`, `totalSlides`, and has a `goToSlide(index)` method
- A `<section class="slide">` structure for each slide
- Content source: either the user's outline/notes, or generate notes from the slide content

## Workflow

### 1. Build the PRESENTER_NOTES array

Read the presentation HTML and any outline/notes files. Create one entry per slide:

```javascript
const PRESENTER_NOTES = [
    {
        title: 'Slide Title',     // Short label for the notes window header
        seconds: 30,              // Allocated time (numeric, used by timers)
        notes: [                  // Array of bullet-point talking points
            'First talking point.',
            'Second talking point.',
        ]
    },
    // ... one per slide
];
```

Place this array inside the `<script>` tag, before the `SlidePresentation` class.

### 2. Add BroadcastChannel sync to the main presentation

In the `SlidePresentation` constructor:

```javascript
this.presenterWindow = null;
this.channel = new BroadcastChannel('slide-sync');
this.channel.onmessage = (e) => {
    if (e.data.type === 'goToSlide') {
        this.goToSlide(e.data.index, false); // false = don't re-broadcast
    }
};
```

In `goToSlide(index, broadcast = true)`, add:

```javascript
if (broadcast) {
    this.channel.postMessage({ type: 'slideChanged', index });
}
```

In the IntersectionObserver callback that tracks the current slide, add:

```javascript
this.channel.postMessage({ type: 'slideChanged', index });
```

### 3. Add the P key handler

In `setupKeyboardNav()`, add a case for `'p'` / `'P'` that calls `this.openPresenterNotes()`.

### 4. Implement openPresenterNotes()

This method opens a popup window via `window.open()` and writes a complete HTML document into it using `doc.write()`. See `references/popup-implementation.md` for the full implementation template.

Key architecture decisions:
- **Use `var` (not `let`) for timer state variables** in the popup script. The popup is created via `document.write()` into `window.open()`, and `let` variables have scoping issues with inline `onclick` handlers in this context.
- **Use `<\/script>` (escaped closing tag)** inside the template literal to prevent the outer HTML parser from seeing it.
- **Add popup blocker check**: `if (!this.presenterWindow) { console.warn(...); return; }`
- **Store instance globally**: `window.presentation = new SlidePresentation()` so the P key handler can access it.

### 5. Features checklist

The presenter notes window must include all of these:

- **Dual timers**: Global elapsed + per-slide timer with targets
  - Global target = sum of all slide `seconds` values
  - Slide target = current slide's `seconds` value
  - Slide timer color: default → green (5s before allocated) → red (at/past allocated)
  - Start/Pause/Reset controls
- **Editable timing badge**: Click the pill to change allocated seconds per slide; updates timer thresholds and targets live
- **Slide info header**: Slide number, title, timing badge
- **Bullet-point notes**: From the PRESENTER_NOTES array
- **Next slide preview**: Shows the title of the upcoming slide
- **Two-way navigation sync**: BroadcastChannel keeps main window and notes window in lockstep
- **Keyboard shortcuts**: Arrow keys (navigate), Space (start/pause), R (reset)
- **Dark theme**: Dark background (#1a1a1a), matches presentation aesthetic

## Color reference

Adapt these to the presentation's color palette:

| Element | Default |
|---------|---------|
| Warning (approaching time) | `#9FD5CA` (green) |
| Over time | `#EE6221` (orange-red) |
| Accent (bullet dots, primary button) | `#EE6221` |
| Timer running | `#e0e0e0` |
| Timer idle | `#999` |
| Timer target | `#555` |
