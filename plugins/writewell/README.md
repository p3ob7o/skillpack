# writewell

Version **1.5.0**. Writing pipeline that strips AI patterns, enforces language discipline, removes clutter, runs a quality check, and optionally applies a personal voice.

## What it does

1. **Strips AI patterns** — significance inflation, promotional language, filler, hedging, chatbot artifacts
2. **Applies your voice** — when a personal voice profile is present, rewrites in that style
3. **Enforces language discipline** — dead metaphors, padded verbs, prefer short words, active voice
4. **Removes clutter** — filler cuts and readability across three revision passes
5. **Checks quality** — natural voice, clear purpose, brevity

Works without a profile using general principles. Onboard builds a personal voice profile from your posts.

## Skills

| Skill | Role | Claude Code | Codex / Cursor / Grok Bot |
|-------|------|-------------|---------------------------|
| `writewell` | Main pipeline | `/writewell:writewell` | `/writewell` (skill name) |
| `onboard` | Build a personal voice profile | `/writewell:onboard` | `/onboard` (skill name) |

Onboard lives at `skills/onboard/SKILL.md` next to `skills/writewell/SKILL.md`. No host needs an extra skills path.

## Install

Shared marketplace steps for Claude Code, Codex, and Cursor / Grok Bot: [skillpack install](../../README.md#install).

Then install this plugin only:

```
# Claude Code
/plugin install writewell@skillpack

# Codex (after marketplace add)
codex plugin add writewell@skillpack

# Cursor / Grok Bot
# Import https://github.com/p3ob7o/skillpack, then install writewell
```

## Usage

Give it text to rewrite:

```
[paste your draft here]
```

## Personalize

Run onboard with either:

- **Individual post URLs** — links to specific articles or posts
- **A blog homepage + count** — homepage URL and how many recent posts to analyze

Onboard reads the samples, distills style across dimensions (sentence structure, tone, vocabulary, openings, closings, formatting, rhetorical devices), and writes a profile **outside** the plugin. The voice profile is not distributed with the skill.

### Profile lookup order

1. `WRITEWELL_VOICE_PATH` if set (use an absolute path; some hosts do not expand `~`)
2. `$XDG_CONFIG_HOME/writewell/voice.md`, or `~/.config/writewell/voice.md` when `XDG_CONFIG_HOME` is unset
3. Legacy `skills/writewell/voice/SKILL.md` — migration fallback only

The new file is `voice.md`, not `SKILL.md`, and it is not inside a skill folder, so hosts do not register it as a skill. If only the legacy file exists, the skill offers to copy it to the destination (custom path when set, otherwise the per-user default).

The `voice/` folder, its README, and `.gitkeep` remain in the tree for that fallback path but are unused for new profiles.

### One profile on more than one computer

Set `WRITEWELL_VOICE_PATH` to an absolute synced path. Onboard writes that file when the variable is set.

**Claude Code** — `env` in `~/.claude/settings.json`:

```json
{
  "env": {
    "WRITEWELL_VOICE_PATH": "/Users/you/Sync/writewell/voice.md"
  }
}
```

**Codex** — `shell_environment_policy.set` in `~/.codex/config.toml`. A shell `export` alone is not enough while `inherit` is the usual `core` baseline:

```toml
[shell_environment_policy]
set = { WRITEWELL_VOICE_PATH = "/Users/you/Sync/writewell/voice.md" }
```

**Cursor (macOS)** — GUI apps do not load `~/.zshrc`. Set for GUI apps, then restart Cursor:

```
launchctl setenv WRITEWELL_VOICE_PATH /Users/you/Sync/writewell/voice.md
```

**Cursor (Linux)** — export `WRITEWELL_VOICE_PATH` in the environment that starts Cursor. If the sandbox refuses a read outside the project, allow that path.

**Grok Bot** — do not use Bot Secrets (those values are hidden from the bot, including in Shell). Copy the profile to `~/.config/writewell/voice.md` on the Grok Bot computer, or export `WRITEWELL_VOICE_PATH` in a profile that computer's agent actually reads. Update, Recover, and Reset can wipe files and shell profiles; keep a synced copy and restore the path there.

## Structure

```
skills/
  onboard/
    SKILL.md            # Writes the profile outside the plugin
  writewell/
    SKILL.md            # Main writing pipeline
    voice/              # Legacy only; not where new profiles are written
      README.md
      .gitkeep
```

## Credits

Writing principles draw from:

- **George Orwell** — "Politics and the English Language"
- **William Zinsser** — "On Writing Well"
- **David Ogilvy** — "Ogilvy on Advertising"
- **Wikipedia** — "Signs of AI writing"
