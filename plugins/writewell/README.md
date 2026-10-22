# writewell

A writing pipeline that strips AI patterns, enforces language discipline, removes clutter, and optionally applies your personal voice. It installs from the skillpack marketplace in Claude Code, Codex, and Cursor / Grok Bot.

## What it does

1. **Strips AI patterns** -- removes the telltale signs of LLM-generated text (significance inflation, promotional language, filler, hedging, chatbot artifacts)
2. **Applies your voice** -- if you've created a personal voice profile, it rewrites in your style
3. **Enforces language discipline** -- kills dead metaphors, deflates padded verbs, prefers short words, uses active voice
4. **Removes clutter** -- cuts filler, clarifies, tests readability across three revision passes
5. **Checks quality** -- ensures natural voice, clear purpose, and brevity

## Install

See the [skillpack install steps](../../README.md#install).

Claude Code:

```
/plugin marketplace add p3ob7o/skillpack
/plugin install writewell@skillpack
```

Codex, after `codex plugin marketplace add p3ob7o/skillpack`:

```
codex plugin add writewell@skillpack
```

Cursor and Grok Bot: import `https://github.com/p3ob7o/skillpack` and install writewell.

## Usage

Give it text to rewrite. In Claude Code the command is `/writewell:writewell`. In Codex and Cursor / Grok Bot, invoke the `writewell` skill.

```
[paste your draft here]
```

## Personalize

The skill works out of the box with general good-writing principles. To make it write in *your* voice, run the onboard skill (`skills/onboard/SKILL.md`).

In Claude Code that skill is `/writewell:onboard`. Codex and Cursor / Grok Bot discover the same folder as the `onboard` skill. No host needs an extra skills path.

This fetches your writing samples from the web and generates a personal voice profile. You can provide:

- **Individual post URLs** -- a list of links to specific articles or blog posts
- **A blog homepage + count** -- the URL of your blog and how many recent posts to analyze

The onboard routine reads your posts, distills your writing style across 11 dimensions (sentence structure, tone, vocabulary, openings, closings, formatting, rhetorical devices, etc.), and writes the profile outside the plugin.

Lookup order, on every host:

1. `WRITEWELL_VOICE_PATH`, when that variable is set
2. `$XDG_CONFIG_HOME/writewell/voice.md`, or `~/.config/writewell/voice.md` when `XDG_CONFIG_HOME` is unset
3. The old in-plugin file `skills/writewell/voice/SKILL.md`, only as a migration fallback

The new file is `voice.md`, not `SKILL.md`, and it is not inside a skill folder, so no host registers it as a skill. The default path is the same on macOS and Linux.

If writewell finds a profile only at the old path, it tells you and offers to copy it to the destination (the custom path when set, otherwise the per-user default). `.gitignore` still ignores the old path. The `voice/` folder, its README, and `.gitkeep` are unused for new profiles and can be removed later; they are still in the tree so an existing checkout keeps the fallback path.

## Use one profile on more than one computer

Set `WRITEWELL_VOICE_PATH` to an absolute path of a file you sync or copy onto each machine (your Mac and the Grok Bot computer, for example). onboard writes that file when the variable is set. Use an absolute path. Some hosts store the value literally and do not expand `~`.

Claude Code. Add it to the `env` block of `~/.claude/settings.json`. Claude Code copies the value into its environment as written ([environment variables](https://code.claude.com/docs/en/env-vars)):

```json
{
  "env": {
    "WRITEWELL_VOICE_PATH": "/Users/you/Sync/writewell/voice.md"
  }
}
```

Codex. Add it to `~/.codex/config.toml`. `set` injects the variable into the shell Codex runs. A shell `export` is not enough while `shell_environment_policy.inherit` stays at its usual `core` baseline ([shell environment policy](https://learn.chatgpt.com/docs/config-file/config-advanced)):

```toml
[shell_environment_policy]
set = { WRITEWELL_VOICE_PATH = "/Users/you/Sync/writewell/voice.md" }
```

Cursor on your computer. The agent reads the environment of the Cursor process. A macOS app does not load `~/.zshrc`. Set the variable for GUI apps and restart Cursor:

```
launchctl setenv WRITEWELL_VOICE_PATH /Users/you/Sync/writewell/voice.md
```

On Linux, export `WRITEWELL_VOICE_PATH` in the environment that starts Cursor. If the sandbox refuses a read outside the project, allow that path.

Grok Bot. Do not put the path in Bot Secrets. Those values are hidden from the Bot, including in Shell. Copy the profile to `~/.config/writewell/voice.md` on the Grok Bot computer, or export `WRITEWELL_VOICE_PATH` in a shell profile that computer's agent actually reads. Update, Recover, and Reset can wipe files and shell profiles on that computer; keep the synced copy and restore the path there.

## Structure

```
skills/
  onboard/
    SKILL.md            # Onboarding routine -- writes the profile outside the plugin
  writewell/
    SKILL.md            # Main skill -- the writing pipeline
    voice/              # Legacy folder only. Not where new profiles are written.
      README.md
      .gitkeep
```

## Credits

The writing principles draw from:

- **George Orwell** -- "Politics and the English Language" (language discipline, dead metaphors, verbal false limbs)
- **William Zinsser** -- "On Writing Well" (clutter removal, revision passes, clarity)
- **David Ogilvy** -- "Ogilvy on Advertising" (writing as action, short words, clear purpose)
- **Wikipedia** -- "Signs of AI writing" (AI pattern detection)
