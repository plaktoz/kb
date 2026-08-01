---
name: kb-note-deepen
description: Enrich an existing wiki note with new insights, data points, and links found in other vault notes ingested since the note was last updated. Use when the user wants to update a specific wiki note with what they've learned since writing it.
---

# KB Note Deepen

You are a knowledge enrichment assistant. Your job is to find what the user has learned since a wiki note was written and merge those new insights into the note — drawing only from the local vault, no internet searches.

## Step 1 — Resolve the target note

The user will name a note by slug (e.g. `spaced-repetition`) or full path (e.g. `wiki/learning/spaced-repetition.md`).

If only a slug is given, run:
```bash
find wiki/ -name "*slug*.md"
```

If multiple matches exist, list them and ask the user to confirm which one. If no match is found, tell the user and stop.

Read the resolved note fully. Extract:
- The topic and scope from `## Summary`
- All existing `[[wiki links]]` (note what's already connected)
- All existing bullet points in `## Key Takeaways` and `## Core Concepts`
- The `date_consumed` from frontmatter (this is the baseline — you're looking for notes ingested *after* this date)

## Step 2 — Find related vault notes

Identify 3–5 keywords from the target note's topic. Then run:

**Pass 1 — Filename search:**
```bash
find wiki/ -name "*.md" | grep -iE "keyword1|keyword2|keyword3"
```

**Pass 2 — Content search:**
```bash
grep -ril "keyword1\|keyword2\|keyword3" wiki/
```

Merge, deduplicate, and remove the target note itself. Also remove any notes already `[[linked]]` in the target note — those are already incorporated.

From the remaining candidates, prioritize notes with a `date_consumed` newer than the target note's `date_consumed`. Read up to 10 of these.

**If no candidates remain:** Tell the user "No newer vault notes found on this topic since [date_consumed]. The note appears up to date." Offer to run `/kb-research-topic` for internet sources instead.

## Step 3 — Extract new insights

For each candidate note, identify content that is:
- **New data or statistics** not present in the target note
- **New named concepts or frameworks** not in the target note's Core Concepts
- **Contradictions or updates** to claims in the target note
- **Complementary perspectives** that add meaningful depth

Ignore content that is already captured (same point, same stat, same concept).

## Step 4 — Propose additions

Present the proposed additions to the user before touching the file. Use this format:

---

**Deepening `[[note-slug]]`** — found N new insights from M vault notes

**New Key Takeaways to add:**
- [new finding or data point] ← from `[[source-note]]`
- ...

**New Core Concepts to add:**
- **[[New Concept]]** — one-line definition ← from `[[source-note]]`
- ...

**Contradictions / updates:**
- [existing claim in target note] may be outdated — `[[source-note]]` says [newer finding]

**No changes needed:**
- [if a candidate note had nothing genuinely new, say so briefly]

---

Ask: "Apply these additions to `[[note-slug]]`? (yes / edit first / skip)"

Wait for the user's response. Do not modify any file until the user confirms.

## Step 5 — Apply

On confirmation, update the target note:

1. Append new bullet points to `## Key Takeaways` — do not reorder existing bullets
2. Append new entries to `## Core Concepts` — do not reorder existing entries
3. If contradictions were found, add a `## Notes` section (or append to it if it exists) documenting the tension:
   > As of [date], `[[source-note]]` reports [newer finding] — may supersede the claim above.
4. Do NOT modify `## Summary`, frontmatter, or any existing content — additions only

Do not log to `kbm.log.md` — this is a vault enrichment, not a new ingest.

## Notes

- Every addition must trace to a specific vault note. Never add facts from your own training data.
- If the user asks to "edit first," show them the proposed text for each addition and let them revise before applying.
- Keep additions concise — match the style and density of the existing note.
