# skillpack

A plugin marketplace for Claude Code.

## Plugins

| Plugin | Description |
|--------|-------------|
| [writewell](plugins/writewell/) | Writing pipeline that strips AI patterns, enforces language discipline, and applies your personal voice |
| [keynote-writer](plugins/keynote-writer/) | Turn a braindump or transcript into a TED-quality keynote outline with flow, takeaway, and slide-by-slide speaker notes |
| [deck-builder](plugins/deck-builder/) | Build single-file HTML slide decks and add a presenter-notes popup with timers and nav sync |
| [session-manager](plugins/session-manager/) | Load project context at the start of a session and update the docs before ending it |

## Install

Add the marketplace:

```
/plugin marketplace add p3ob7o/skillpack
```

Install a plugin:

```
/plugin install writewell@skillpack
```

## License

GPL v2. See [LICENSE](LICENSE).
