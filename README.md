# skillpack

A plugin marketplace of writing and productivity skills. The same skill files install in Claude Code, Codex, and Cursor / Grok Bot.

## Plugins

| Plugin | Description |
|--------|-------------|
| [writewell](plugins/writewell/) | Writing pipeline that strips AI patterns, enforces language discipline, and applies your personal voice |
| [keynote-writer](plugins/keynote-writer/) | Turn a braindump or transcript into a TED-quality keynote outline with flow, takeaway, and slide-by-slide speaker notes |
| [deck-builder](plugins/deck-builder/) | Build single-file HTML slide decks and add a presenter-notes popup with timers and nav sync |
| [session-manager](plugins/session-manager/) | Load project context at the start of a session and update the docs before ending it |

## Install

Each plugin is one directory under `plugins/`. `skills/<skill>/SKILL.md` is the only copy of that skill. Host manifests point at those directories; they do not duplicate the instructions.

### Claude Code

The catalog is `.claude-plugin/marketplace.json`. In a Claude Code session:

```
/plugin marketplace add p3ob7o/skillpack
/plugin install writewell@skillpack
```

Replace `writewell` with `keynote-writer`, `deck-builder`, or `session-manager`.

Plugin skills run as `/<plugin>:<skill>`, for example `/writewell:writewell`, `/writewell:onboard`, and `/deck-builder:slide-deck-creator`.

Each host discovers `skills/<skill>/SKILL.md` one directory deep. writewell's onboard skill is `skills/onboard/SKILL.md`, so it loads next to `skills/writewell/SKILL.md` with no extra path in the plugin manifest. A generated voice profile is not a skill. It is written outside the plugin, at `WRITEWELL_VOICE_PATH` when that variable is set, otherwise `~/.config/writewell/voice.md`. See the [writewell README](plugins/writewell/README.md#personalize).

### Codex

Codex reads `.agents/plugins/marketplace.json` for the catalog and `.codex-plugin/plugin.json` inside each plugin. Every plugin also has a root `plugin.json` using the Agent Plugins schema. Skills sit one directory under `skills/`, and each Codex manifest points at `./skills/`.

Add the GitHub repository. Do not sparse-checkout only `.agents/plugins`: the plugins themselves live under `plugins/`, and the catalog points at those local paths.

```
codex plugin marketplace add p3ob7o/skillpack
```

Install one plugin from that marketplace:

```
codex plugin add writewell@skillpack
```

In an interactive Codex session, `/plugins` opens the same browser. Start a new session after installing so the bundled skills load.

Codex discovers `skills/<skill>/SKILL.md` one directory deep, including `onboard` and `writewell`. The skill `name` matches its folder.

### Cursor and Grok Bot

Cursor and Grok Bot load Cursor plugins. This repo's catalog is `.cursor-plugin/marketplace.json`. Each plugin has `.cursor-plugin/plugin.json` and the shared `skills/<skill>/SKILL.md` files. A skill folder's `SKILL.md` starts with YAML `name` and `description`. `name` is lowercase kebab-case and matches the folder name.

Import the GitHub repository. In Cursor that is Customize, or Dashboard → Plugins & MCPs → Add Marketplace → Import from Repo:

```
https://github.com/p3ob7o/skillpack
```

Install a plugin at user or project scope. Invoke a skill by typing `/` and its name.

Grok Bot uses the same Cursor plugin packages. Import and install them the same way. A listing on the public Grok Bot marketplace is a separate review at <https://x.ai/bot/marketplace/submit-a-plugin>. Importing this repository does not require that submission.

Cursor's default plugin discovery is `skills/<name>/SKILL.md`. None of these plugins set a `skills` override, so both `writewell` and `onboard` load from that scan.

## Check the manifests

[`scripts/validate-manifests.py`](scripts/validate-manifests.py) fails when the Claude, Codex, and Cursor manifests disagree, or when a `SKILL.md` breaks the shared frontmatter rules. GitHub Actions runs it on push and pull request.

```
pip install jsonschema pyyaml
python3 scripts/validate-manifests.py
```

## License

GPL v2. See [LICENSE](LICENSE).
