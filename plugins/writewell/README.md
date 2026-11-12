# writewell

Version **2.0.0**. Generic writing pipeline that strips AI patterns, enforces language discipline, removes clutter, and runs a quality check. It does not apply a personal voice.

For the same pipeline plus your own voice profile, install [writewell-with-voice](../writewell-with-voice/README.md).

## What it does

1. **Strips AI patterns** — significance inflation, promotional language, filler, hedging, chatbot artifacts
2. **Enforces language discipline** — dead metaphors, padded verbs, prefer short words, active voice
3. **Removes clutter** — filler cuts and readability across three revision passes
4. **Checks quality** — sounds like a person, clear purpose, brevity

## Skills

| Skill | Role | Claude Code | Codex / Cursor / Grok Bot |
|-------|------|-------------|---------------------------|
| `writewell` | Main pipeline | `/writewell:writewell` | `/writewell` (skill name) |

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

## Structure

```
skills/
  writewell/
    SKILL.md            # Main writing pipeline
```

## Credits

Writing principles draw from:

- **George Orwell** — "Politics and the English Language"
- **William Zinsser** — "On Writing Well"
- **David Ogilvy** — "Ogilvy on Advertising"
- **Wikipedia** — "Signs of AI writing"
