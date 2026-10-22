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

The onboard routine reads your posts, distills your writing style across 11 dimensions (sentence structure, tone, vocabulary, openings, closings, formatting, rhetorical devices, etc.), and writes `skills/writewell/voice/SKILL.md`. The main skill reads that same file. A profile already at that path keeps working; onboard updates it in place.

## Structure

```
skills/
  onboard/
    SKILL.md            # Onboarding routine -- creates your voice profile
  writewell/
    SKILL.md            # Main skill -- the writing pipeline
    voice/SKILL.md      # Your voice profile (generated, not committed)
    voice/README.md     # Explains the voice directory
```

## Credits

The writing principles draw from:

- **George Orwell** -- "Politics and the English Language" (language discipline, dead metaphors, verbal false limbs)
- **William Zinsser** -- "On Writing Well" (clutter removal, revision passes, clarity)
- **David Ogilvy** -- "Ogilvy on Advertising" (writing as action, short words, clear purpose)
- **Wikipedia** -- "Signs of AI writing" (AI pattern detection)
