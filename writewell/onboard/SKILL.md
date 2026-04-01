---
name: writewell:onboard
version: 1.0.0
description: |
  Create a personal voice profile for /writewell by analyzing writing samples.
  Provide individual post URLs or a blog homepage URL with a post count.
  Fetches the content, distills the writing style, and generates voice/SKILL.md.
allowed-tools:
  - Read
  - Write
  - Edit
  - WebFetch
  - WebSearch
  - AskUserQuestion
  - Glob
---

# Write Well: Onboard

Create a personal voice profile by analyzing writing samples from the web.

## Input Modes

Ask the user which mode they want to use:

### Mode A: Individual post URLs

The user provides a list of URLs pointing to individual blog posts or articles.
Fetch each one.

### Mode B: Blog homepage + count

The user provides:
1. The URL of a blog's homepage or archive page
2. How many posts to analyze (default: 5)

Fetch the homepage, find links to individual posts (in reverse chronological order),
then fetch that many posts. Use these heuristics to identify post links:

- Look for `<article>` elements, `.post` / `.entry` classes, or similar blog patterns
- Prefer links inside the main content area, not sidebars or footers
- If the page is an archive/index, look for date-ordered links
- If the homepage doesn't list posts directly, look for an `/archive`, `/blog`,
  `/posts`, or `/writing` page and try that instead
- If you can't find individual post links, tell the user and ask them to provide
  direct URLs (fall back to Mode A)

## Analysis

For each fetched post, extract the main prose content (skip navigation, ads, footers).
Then analyze across all posts for these dimensions:

### Sentence structure
- Average sentence length (short/medium/long)
- Sentence variety (uniform vs. mixed lengths)
- Use of fragments vs. complete sentences
- Comma style (sparse vs. liberal)
- Semicolons, colons, em dashes -- how often and for what purpose
- Exclamation marks -- frequency and context

### Paragraph structure
- Typical paragraph length (sentences per paragraph)
- Single-sentence paragraphs (common or rare)
- How paragraphs open (observation, example, question, assertion)
- Persuasive structure patterns

### Tone
- Formality level (casual / professional-warm / formal / academic)
- Humor style (none / dry / playful / self-deprecating)
- Directness (blunt / direct / hedged / indirect)
- How the writer handles disagreement or criticism
- Self-awareness and vulnerability

### Vocabulary
- Signature words and phrases that recur across posts
- Jargon comfort level (avoids it / uses it naturally / leans on it)
- Words and patterns the writer clearly avoids
- Contractions (frequent / occasional / never)

### Openings
- How posts typically begin (thesis / context / anecdote / question / greeting)
- First-sentence patterns

### Closings
- How posts typically end (CTA / question / summary / sign-off / just stops)
- Last-sentence patterns

### Formatting
- Header usage (none / sparse / extensive)
- List style (bullets / numbers / inline)
- Bold/italic usage patterns
- Links -- how they're woven in
- Use of images, tables, code blocks

### Rhetorical devices
- Signature moves (rhetorical questions, analogies, data-heavy arguments, stories)
- Parenthetical asides (frequent / occasional / rare)
- How opinions are signaled vs. facts

### Point of view
- Default pronoun (I / we / you / one)
- When the writer switches POV and why

### Emotional register
- How enthusiasm is expressed
- How criticism is delivered
- How the writer handles admitting mistakes

### Distinctive touches
- Anything unique that doesn't fit the categories above
- Recurring structural patterns
- Cultural or domain-specific references

## Output

Generate `voice/SKILL.md` in the writewell skill directory using this template:

```markdown
---
name: writewell:voice
version: 1.0.0
description: |
  Personal writing voice for [name or description]. Defines sentence structure,
  tone, vocabulary, openings, closings, formatting, rhetorical devices, and
  distinctive touches. Referenced by the main /writewell skill at Part 2.
---

# Personal Voice: [Name]

This file defines the writer's personal style. It is read and applied by the main
`/writewell` skill during Part 2 (Apply personal voice).

Source material: [list the URLs analyzed]

---

## Sentence Structure
[findings]

## Paragraph Structure
[findings]

## Tone
[findings]

## Vocabulary
[preferred words/phrases and words/patterns to avoid]

## Openings
[patterns found, with examples from the source material]

## Closings
[patterns found, with examples from the source material]

## Formatting
[findings]

## Rhetorical Devices
[findings]

## Point of View
[findings]

## Emotional Register
[findings]

## Distinctive Touches
[findings]
```

## Process

1. Ask the user: "Provide a list of post URLs, or a blog homepage URL and how many posts to analyze."
2. Fetch the content using the appropriate mode.
3. If any URL fails to fetch, report it and continue with the ones that worked. Need at least 2 posts to produce a useful profile.
4. Analyze all posts across the dimensions above.
5. Write the voice profile to `voice/SKILL.md` in the writewell skill directory.
6. Show the user a summary of the voice profile -- the key traits that define this writing style, in 5-8 bullet points.
7. Ask if they want to adjust anything before finalizing.

## Important

- The voice file should contain **rules and patterns**, not example text. Write it as instructions that an LLM can follow, not as a literary analysis essay.
- Use concrete examples from the source material to illustrate rules, but frame them as "write like this" not "the author wrote this."
- If the analyzed posts have inconsistent styles (e.g., some formal, some casual), note the contexts where each style appears rather than averaging them out.
- If a voice file already exists, warn the user before overwriting it.
