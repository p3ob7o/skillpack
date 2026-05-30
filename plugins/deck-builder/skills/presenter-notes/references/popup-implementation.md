# Presenter Notes Popup — Full Implementation Template

This is the complete `openPresenterNotes()` method. Adapt colors, fonts, and layout to match the target presentation's design system.

```javascript
openPresenterNotes() {
    if (this.presenterWindow && !this.presenterWindow.closed) {
        this.presenterWindow.focus();
        return;
    }

    this.presenterWindow = window.open('', 'presenter-notes', 'width=600,height=800');
    if (!this.presenterWindow) {
        console.warn('Popup blocked — allow popups for this site and press P again.');
        return;
    }
    const doc = this.presenterWindow.document;
    const notes = PRESENTER_NOTES;
    const totalSlides = this.totalSlides;
    const currentSlide = this.currentSlide;

    doc.write(`<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Presenter Notes</title>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: 'Public Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        background: #1a1a1a;
        color: #e0e0e0;
        padding: 2rem;
        height: 100vh;
        display: flex;
        flex-direction: column;
    }

    .timers {
        display: flex;
        gap: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #333;
        margin-bottom: 1.5rem;
        flex-shrink: 0;
    }
    .timer-block { flex: 1; text-align: center; }
    .timer-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #666;
        margin-bottom: 0.25rem;
    }
    .timer-row {
        display: flex;
        align-items: baseline;
        justify-content: center;
        gap: 0.15em;
    }
    .timer-value {
        font-size: 2.5rem;
        font-weight: 700;
        font-variant-numeric: tabular-nums;
        color: #999;
        transition: color 0.3s;
    }
    .timer-target {
        font-size: 1.1rem;
        font-weight: 400;
        font-variant-numeric: tabular-nums;
        color: #555;
    }
    .timer-value.running { color: #e0e0e0; }
    .timer-value.warning { color: #9FD5CA; }
    .timer-value.over { color: #EE6221; }

    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 1rem;
        margin-bottom: 1.5rem;
        flex-shrink: 0;
    }
    .slide-info {
        display: flex;
        align-items: baseline;
        gap: 0.75rem;
    }
    .slide-num { font-size: 1.5rem; font-weight: 700; color: #fff; }
    .slide-title { font-size: 1rem; color: #999; font-weight: 400; }
    .timing-badge {
        background: #333;
        color: #9FD5CA;
        padding: 0.3em 0.8em;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid transparent;
        width: 4em;
        text-align: center;
        font-family: inherit;
        cursor: pointer;
        outline: none;
    }
    .timing-badge:hover { border-color: #555; }
    .timing-badge:focus { border-color: #9FD5CA; }

    .notes { flex: 1; overflow-y: auto; padding-right: 0.5rem; }
    .notes ul { list-style: none; display: flex; flex-direction: column; gap: 1rem; }
    .notes li {
        font-size: 1.2rem;
        line-height: 1.6;
        color: #ddd;
        padding-left: 1.25rem;
        position: relative;
    }
    .notes li::before {
        content: '';
        position: absolute;
        left: 0; top: 0.65em;
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #EE6221;
    }

    .next-slide {
        flex-shrink: 0;
        margin-top: 1.5rem;
        padding-top: 1rem;
        border-top: 1px solid #333;
    }
    .next-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #666;
        margin-bottom: 0.5rem;
    }
    .next-title { font-size: 1rem; color: #999; }

    .controls {
        flex-shrink: 0;
        display: flex;
        gap: 0.75rem;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid #333;
    }
    button {
        background: #333; color: #ddd; border: none;
        border-radius: 8px; padding: 0.5em 1.25em;
        font-size: 0.9rem; font-family: inherit;
        cursor: pointer; transition: background 0.15s;
    }
    button:hover { background: #444; }
    button.primary { background: #EE6221; color: #fff; }
    button.primary:hover { background: #d4551a; }
    .spacer { flex: 1; }

    .hint {
        margin-top: 0.75rem;
        font-size: 0.7rem;
        color: #555;
        text-align: center;
    }
    kbd {
        background: #333;
        padding: 0.15em 0.4em;
        border-radius: 3px;
        font-family: inherit;
        font-size: 0.85em;
    }
</style>
</head>
<body>
    <div class="timers">
        <div class="timer-block">
            <div class="timer-label">Total</div>
            <div class="timer-row">
                <div class="timer-value" id="pn-global">00:00</div>
                <div class="timer-target" id="pn-global-target"></div>
            </div>
        </div>
        <div class="timer-block">
            <div class="timer-label">This Slide</div>
            <div class="timer-row">
                <div class="timer-value" id="pn-slide">00:00</div>
                <div class="timer-target" id="pn-slide-target"></div>
            </div>
        </div>
    </div>

    <div class="header">
        <div class="slide-info">
            <span class="slide-num" id="pn-num">1 / \${totalSlides}</span>
            <span class="slide-title" id="pn-title">\${notes[0].title}</span>
            <input class="timing-badge" id="pn-timing" value="\${notes[0].seconds}s" />
        </div>
    </div>

    <div class="notes" id="pn-notes">
        <ul id="pn-list"></ul>
    </div>

    <div class="next-slide">
        <div class="next-label">Next</div>
        <div class="next-title" id="pn-next">\${notes[1] ? notes[1].title : '—'}</div>
    </div>

    <div class="controls">
        <button onclick="prev()">&larr; Prev</button>
        <button onclick="next()">Next &rarr;</button>
        <div class="spacer"></div>
        <button class="primary" id="pn-timer-btn" onclick="toggleTimer()">Start</button>
        <button onclick="resetTimers()">Reset</button>
    </div>

    <div class="hint">
        <kbd>&larr;</kbd> <kbd>&rarr;</kbd> navigate &nbsp;&middot;&nbsp;
        <kbd>Space</kbd> start/pause &nbsp;&middot;&nbsp;
        <kbd>R</kbd> reset
    </div>

    <script>
        const notes = \${JSON.stringify(notes)};
        const total = \${totalSlides};
        let current = \${currentSlide};

        /* IMPORTANT: Use var (not let) for timer state — let has scoping
           issues with inline onclick handlers in document.write() popups */
        var globalRunning = false;
        var globalStart = null;
        var globalElapsed = 0;
        var slideStart = null;
        var slideElapsed = 0;
        var tickInterval = null;

        function fmtSec(sec) {
            var m = Math.floor(sec / 60);
            var s = sec % 60;
            return String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
        }

        function fmtTime(ms) {
            var sec = Math.floor(ms / 1000);
            var m = Math.floor(sec / 60);
            var s = sec % 60;
            return String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
        }

        function updateTargets() {
            var globalTotal = notes.reduce(function(sum, n) { return sum + n.seconds; }, 0);
            document.getElementById('pn-global-target').textContent = '/ ' + fmtSec(globalTotal);
            var slideAlloc = notes[current] ? notes[current].seconds : 30;
            document.getElementById('pn-slide-target').textContent = '/ ' + fmtSec(slideAlloc);
        }

        function tick() {
            var now = Date.now();
            var globalEl = document.getElementById('pn-global');
            var slideEl = document.getElementById('pn-slide');

            var gMs = globalElapsed + (globalRunning ? now - globalStart : 0);
            globalEl.textContent = fmtTime(gMs);
            globalEl.className = 'timer-value' + (globalRunning ? ' running' : '');

            var sMs = slideElapsed + (globalRunning ? now - slideStart : 0);
            var sSec = sMs / 1000;
            var allocated = notes[current] ? notes[current].seconds : 30;

            slideEl.textContent = fmtTime(sMs);

            if (sSec >= allocated) {
                slideEl.className = 'timer-value over';
            } else if (sSec >= allocated - 5) {
                slideEl.className = 'timer-value warning';
            } else {
                slideEl.className = 'timer-value' + (globalRunning ? ' running' : '');
            }
        }

        function toggleTimer() {
            var btn = document.getElementById('pn-timer-btn');
            if (globalRunning) {
                globalRunning = false;
                var now = Date.now();
                globalElapsed += now - globalStart;
                slideElapsed += now - slideStart;
                clearInterval(tickInterval);
                btn.textContent = 'Resume';
            } else {
                globalRunning = true;
                var now = Date.now();
                globalStart = now;
                slideStart = now;
                btn.textContent = 'Pause';
                tickInterval = setInterval(tick, 200);
            }
            tick();
        }

        function resetTimers() {
            clearInterval(tickInterval);
            tickInterval = null;
            globalRunning = false;
            globalElapsed = 0;
            globalStart = null;
            slideElapsed = 0;
            slideStart = null;
            document.getElementById('pn-timer-btn').textContent = 'Start';
            document.getElementById('pn-global').textContent = '00:00';
            document.getElementById('pn-global').className = 'timer-value';
            document.getElementById('pn-slide').textContent = '00:00';
            document.getElementById('pn-slide').className = 'timer-value';
        }

        function resetSlideTimer() {
            if (globalRunning) {
                var now = Date.now();
                slideElapsed = 0;
                slideStart = now;
            } else {
                slideElapsed = 0;
            }
            var slideEl = document.getElementById('pn-slide');
            slideEl.className = 'timer-value' + (globalRunning ? ' running' : '');
            tick();
        }

        function render(idx) {
            var changed = idx !== current;
            current = idx;
            var n = notes[idx] || { title: '', seconds: 30, notes: [] };
            document.getElementById('pn-num').textContent = (idx + 1) + ' / ' + total;
            document.getElementById('pn-title').textContent = n.title;
            document.getElementById('pn-timing').value = n.seconds + 's';

            var list = document.getElementById('pn-list');
            list.innerHTML = n.notes.map(function(t) { return '<li>' + t + '</li>'; }).join('');

            var nextNote = notes[idx + 1];
            document.getElementById('pn-next').textContent = nextNote ? nextNote.title : 'End';

            updateTargets();
            if (changed) resetSlideTimer();
        }

        /* BroadcastChannel — two-way sync with main window */
        var channel = new BroadcastChannel('slide-sync');

        function goTo(idx) {
            if (idx < 0 || idx >= total) return;
            render(idx);
            channel.postMessage({ type: 'goToSlide', index: idx });
        }
        function next() { goTo(current + 1); }
        function prev() { goTo(current - 1); }

        channel.onmessage = function(e) {
            if (e.data.type === 'slideChanged') {
                render(e.data.index);
            }
        };

        /* Keyboard nav */
        document.addEventListener('keydown', function(e) {
            switch (e.key) {
                case 'ArrowRight': case 'ArrowDown': e.preventDefault(); next(); break;
                case 'ArrowLeft': case 'ArrowUp': e.preventDefault(); prev(); break;
                case ' ': e.preventDefault(); toggleTimer(); break;
                case 'r': case 'R': e.preventDefault(); resetTimers(); break;
            }
        });

        /* Editable timing badge */
        var timingInput = document.getElementById('pn-timing');
        timingInput.addEventListener('change', function() {
            var val = parseInt(this.value, 10);
            if (isNaN(val) || val < 1) val = notes[current].seconds;
            notes[current].seconds = val;
            this.value = val + 's';
            updateTargets();
        });
        timingInput.addEventListener('focus', function() { this.select(); });

        /* Initial render */
        render(current);
    <\/script>
</body>
</html>`);
    doc.close();
}
```

## Integration points in the main presentation

### Constructor additions

```javascript
this.presenterWindow = null;
this.channel = new BroadcastChannel('slide-sync');
this.channel.onmessage = (e) => {
    if (e.data.type === 'goToSlide') {
        this.goToSlide(e.data.index, false);
    }
};
```

### goToSlide modification

```javascript
goToSlide(index, broadcast = true) {
    this.slides[index].scrollIntoView({ behavior: 'smooth' });
    this.currentSlide = index;
    this.updateUI();
    if (broadcast) {
        this.channel.postMessage({ type: 'slideChanged', index });
    }
}
```

### IntersectionObserver addition

In the navigation observer callback, after updating `this.currentSlide`:

```javascript
this.channel.postMessage({ type: 'slideChanged', index });
```

### Keyboard handler

```javascript
case 'p': case 'P':
    e.preventDefault();
    this.openPresenterNotes();
    break;
```

### Global instance

```javascript
window.presentation = new SlidePresentation();
```
