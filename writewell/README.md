# writewell

A writing pipeline for Claude Code that strips AI patterns, enforces language discipline, removes clutter, and optionally applies your personal voice.

## What it does

1. **Strips AI patterns** -- removes the telltale signs of LLM-generated text (significance inflation, promotional language, filler, hedging, chatbot artifacts)
2. **Applies your voice** -- if you've created a personal voice profile, it rewrites in your style
3. **Enforces language discipline** -- kills dead metaphors, deflates padded verbs, prefers short words, uses active voice
4. **Removes clutter** -- cuts filler, clarifies, tests readability across three revision passes
5. **Checks quality** -- ensures natural voice, clear purpose, and brevity

## Install

```bash
claude install p3ob7o/skillpack/writewell
```

## Usage

Give it text to rewrite:

```
/writewell

[paste your draft here]
```

## Personalize

The skill works out of the box with general good-writing principles. To make it write in *your* voice:

```
/writewell:onboard
```

This fetches your writing samples from the web and generates a personal voice profile. You can provide:

- **Individual post URLs** -- a list of links to specific articles or blog posts
- **A blog homepage + count** -- the URL of your blog and how many recent posts to analyze

The onboard routine reads your posts, distills your writing style across 11 dimensions (sentence structure, tone, vocabulary, openings, closings, formatting, rhetorical devices, etc.), and writes a `voice/SKILL.md` file that the main skill uses automatically from then on.

## Structure

```
writewell/
  SKILL.md              # Main skill -- the writing pipeline
  onboard/SKILL.md      # Onboarding routine -- creates your voice profile
  voice/SKILL.md        # Your voice profile (generated, not committed)
  voice/README.md       # Explains the voice directory
```

## Credits

The writing principles draw from:

- **George Orwell** -- "Politics and the English Language" (language discipline, dead metaphors, verbal false limbs)
- **William Zinsser** -- "On Writing Well" (clutter removal, revision passes, clarity)
- **David Ogilvy** -- "Ogilvy on Advertising" (writing as action, short words, clear purpose)
- **Wikipedia** -- "Signs of AI writing" (AI pattern detection)
