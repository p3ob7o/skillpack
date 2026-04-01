---
name: writewell
version: 1.2.0
description: |
  Full writing pipeline: strip AI patterns, enforce language discipline, remove
  clutter, verify quality, and optionally apply a personal voice. Use when editing
  or reviewing any prose that should read like a human wrote it, not a machine.
  Run /writewell:onboard to create your personal voice profile.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebFetch
---

## Voice check — run this FIRST, before anything else

Run this bash command before doing anything:

```bash
SKILL_DIR="$(dirname "$(readlink -f "${BASH_SOURCE[0]:-$0}" 2>/dev/null || echo "$0")")"
test -f "$SKILL_DIR/voice/SKILL.md" && echo "VOICE_OK" || echo "VOICE_MISSING"
```

- If the output is `VOICE_MISSING`: invoke `/writewell:onboard` immediately. Do not proceed.
- If the output is `VOICE_OK`: continue with the pipeline below.

---

# Write Well

A writing pipeline that strips AI patterns, enforces language discipline, removes
clutter, checks quality, and optionally applies a personal voice.

## Task

When given text to rewrite:

1. **Strip AI patterns** (Part 1) - Scan for and remove AI writing patterns
2. **Apply personal voice** (Part 2) - If `voice/SKILL.md` exists, read it and apply the voice rules. If not, skip this step and rely on the general principles in Parts 3-5.
3. **Apply language discipline** (Part 3) - Kill dead metaphors, deflate padded verbs, prefer short words
4. **Remove clutter** (Part 4) - Cut filler, clarify, test readability
5. **Final quality check** (Part 5) - Ensure natural voice, clear purpose, brevity
6. **Preserve meaning** - Keep the core message, data, and intent intact
7. **Check the result** - Read it aloud mentally; it should sound like a real person writing to peers, not a press release

---

# PART 1: AI PATTERN REMOVAL

Strip these patterns before any voice or style work. This section is based on Wikipedia's "Signs of AI writing" guide.

## Content Patterns

### Significance inflation
**Kill phrases:** stands/serves as, is a testament/reminder, pivotal/crucial/key role/moment, underscores/highlights importance, reflects broader, symbolizing, setting the stage for, evolving landscape, indelible mark

Replace with plain statements of fact.

### Notability name-dropping
**Kill phrases:** independent coverage, local/regional/national media outlets, active social media presence

Replace with specific claims from specific sources.

### Superficial -ing analyses
**Kill phrases:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., showcasing...

Delete them or expand with actual sourced detail.

### Promotional language
**Kill phrases:** boasts, vibrant, rich (figurative), profound, groundbreaking, renowned, breathtaking, must-visit, stunning, nestled, in the heart of

Replace with neutral, specific descriptions.

### Vague attributions
**Kill phrases:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources

Name the actual source or delete the claim.

### Formulaic challenges sections
**Kill phrases:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

Replace with specific facts about actual challenges.

## Language Patterns

### Overused AI vocabulary
**Kill words:** Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore (verb), valuable, vibrant

Replace with plain language.

### Copula avoidance
**Kill phrases:** serves as, stands as, marks, represents [a], boasts/features/offers [a]

Use "is," "are," "has" instead.

### Negative parallelisms
**Kill:** "Not only...but..." / "It's not just about..., it's..."

State the point directly.

### Rule of three overuse
Lists of three that feel forced ("innovation, inspiration, and insights") should be trimmed or made natural.

### Synonym cycling
Stop cycling through synonyms for the same noun. Pick the clearest word and reuse it.

### False ranges
**Kill:** "from X to Y" constructions where X and Y are not on a meaningful scale.

## Style Patterns

### Em dash overuse
LLMs overuse em dashes. Replace most with commas or periods. Use em dashes sparingly and only for genuine parenthetical asides.

### Boldface overuse
Remove mechanical bold emphasis. Never bold words mid-sentence for emphasis. Bold is for section labels and headers only.

### Inline-header vertical lists
**Kill:** Lists where items start with bolded headers followed by colons and restated descriptions. Convert to prose or use clean bullet lists without the bold-colon pattern.

### Emojis
Remove all emojis unless the personal voice profile explicitly allows them.

### Curly quotation marks
Replace curly quotes with straight quotes.

## Communication Patterns

### Chatbot artifacts
**Kill:** "I hope this helps," "Of course!", "Certainly!", "Would you like...", "Let me know if...", "Here is a..."

### Knowledge-cutoff disclaimers
**Kill:** "as of [date]," "While specific details are limited/scarce..."

### Sycophantic tone
**Kill:** "Great question!", "You're absolutely right!", "That's an excellent point!"

## Filler and Hedging

### Filler phrases
- "In order to achieve this goal" -> "To achieve this"
- "Due to the fact that" -> "Because"
- "At this point in time" -> "Now"
- "It is important to note that the data shows" -> "The data shows"

### Excessive hedging
- "could potentially possibly be argued" -> "may"

### Generic positive conclusions
**Kill:** "The future looks bright," "Exciting times lie ahead," "journey toward excellence"

Replace with specific next steps or concrete plans.

---

# PART 2: PERSONAL VOICE

If the file `voice/SKILL.md` exists in this skill's directory, read it and apply its
rules at this step. The voice file defines the writer's personal style: sentence
structure, tone, vocabulary, openings, closings, formatting preferences, rhetorical
devices, and distinctive touches.

If no voice file exists, the bash check above will have already redirected to
`/writewell:onboard`. You should not reach this point without a voice file.

---

# PART 3: LANGUAGE DISCIPLINE

These rules attack lazy thinking, not just lazy phrasing. Apply them after stripping
AI patterns and before final revision.

## Think first, then write

Before reaching for words, picture the concrete thing you want to say. What actually
happened? What does the reader actually see? Start from that image and find words to
match it. Never assemble pre-made phrases into sentences -- that produces prose where
the words chose the writer, not the other way around.

## Kill dead metaphors

A metaphor is dead when the reader no longer pictures the image behind it. "Level
the playing field," "move the needle," "low-hanging fruit," "deep dive," "at the
end of the day," "on the same page," "circle back," "double down" -- these are
verbal reflexes, not communication. Either invent a fresh image or state the point
plainly.

Test: can you picture the physical scene the phrase describes? If not, it's dead.
Cut it.

## Deflate verbal false limbs

Simple actions get buried under padded verb phrases. Reverse this:

| Inflated                     | Plain            |
|------------------------------|------------------|
| render inoperative           | break            |
| make contact with            | meet             |
| give rise to                 | cause            |
| have the effect of           | (just state it)  |
| play a leading role in       | lead             |
| take into consideration      | consider         |
| make it possible for         | let / allow      |
| with respect to              | about / on       |
| in the context of            | in               |
| is supportive of             | supports         |

If the plain verb exists, use it.

## Prefer short words

Where a short word says the same thing, use it. "Use" not "utilize." "Help" not
"facilitate." "Start" not "commence." "Show" not "demonstrate." "Try" not "endeavor."
This is not about dumbing down -- it's about removing the padding between the reader
and the meaning.

## Use active verbs

"We decided" not "A decision was made." "The team shipped" not "It was shipped by
the team." Active voice is shorter, clearer, and puts the actor front and center.
Reserve passive only when the actor is unknown or genuinely irrelevant.

## Cut what adds nothing

After writing, go through each sentence and ask: does every word earn its place? If
removing a word doesn't change the meaning, remove it. This applies to:

- Redundant modifiers ("absolutely essential" -> "essential")
- Throat-clearing phrases ("It is worth noting that" -> delete)
- Doubled expressions ("each and every" -> "every")
- Adverbs and adjectives that don't clearly add meaning

## Never use jargon when plain English works

Words like "reconceptualize," "demassification," "attitudinally" are not signs of
sophistication. They are signs of unclear thinking. If you can't explain it in words
a smart colleague would use at lunch, you don't understand it well enough.

## The escape clause

Break any of these rules before writing something that sounds awkward, unnatural,
or barbarous. The point is clear, living prose -- not mechanical rule-following.
When a rule would make the sentence worse, the sentence wins.

---

# PART 4: CLUTTER REMOVAL

Writing improves in direct proportion to the number of things you cut. Apply these
passes after drafting.

## Revision pass 1 -- Cut clutter

- Delete fillers: "very," "in fact," "in order to," "due to the fact that," "it should
  be noted that," "the fact that," "at this point in time."
- Remove redundancy. Say everything once, in the best place. If the same idea appears
  in the intro and the body, kill it in the intro.
- Aim to cut at least 20-30% of the first draft's words. If you can't, you padded
  the draft.

## Revision pass 2 -- Clarify and humanize

- Replace vague phrases with concrete details or examples.
- Ask: "Would I say this aloud to a smart friend?" If not, rewrite.
- Make sure opinions and personality appear somewhere. Writing without a point of view
  is furniture assembly instructions.
- One main idea per paragraph. If a paragraph tries to do two things, split it.

## Revision pass 3 -- Reader test

- Read aloud. Fix any spot where you stumble or get bored.
- Check that the main point is unmistakable by the end.
- Trim the opening and closing again. Make them as lean as possible. The first and
  last sentences carry the most weight -- don't waste them on setup or summary.

---

# PART 5: WRITING AS ACTION

Good writing is not a natural gift. You learn it by doing it and revising it.
These principles govern the final quality check.

## Write the way you talk

If a sentence wouldn't come out of your mouth in conversation, it shouldn't be on
the page. Natural doesn't mean sloppy -- it means without pretension.

## Short words, short sentences, short paragraphs

This is the single most reliable way to improve any piece of writing. Long sentences
bury meaning. Long paragraphs lose readers. Long words signal that the writer is
performing, not communicating.

## Be crystal clear about what you want

Before publishing, make sure the reader knows exactly what you're asking them to do,
think, or decide. If the piece doesn't drive toward a clear action or conclusion,
it's a diary entry, not communication.

## Let it cool, then cut

Never publish the moment you finish writing. Come back to it with fresh eyes. Read
it aloud. What felt clever at drafting time often sounds bloated the next morning.

## Get a second pair of eyes

If it matters, ask someone to read it before you publish. A colleague will catch
what you've gone blind to.

---

## Process

1. Read the input text carefully
2. Identify and remove all AI patterns from Part 1
3. Read `voice/SKILL.md` and apply the personal voice rules.
4. Apply language discipline from Part 3 (kill dead metaphors, deflate false limbs, prefer short words, cut jargon)
5. Run the clutter removal passes from Part 4 (cut filler, clarify, read aloud)
6. Apply the final quality checks from Part 5 (natural voice, clarity of purpose, brevity)
7. Verify the result:
   - Does it start with a direct statement, context, or problem -- not a greeting or question?
   - Are paragraphs short (1-4 sentences)?
   - Are opinions clearly marked as opinions?
   - Are numbers precise, not vague?
   - Is the tone warm but professional, not press-release-y?
   - Does it end with a call to action or concrete next steps -- not a summary?
   - Are there zero emojis and zero chatbot artifacts?
   - Is it clear what the reader should do, think, or decide?
   - If a voice profile exists: does the result match the voice's style?
8. Present the rewritten version

## Output Format

Provide:
1. The rewritten text
2. A brief summary of changes made (what AI patterns were removed, what style adjustments were applied)
