# Design: kb-research-topic skill

## Overview

A skill that takes a user-provided topic, adaptively grills the user to refine scope, decomposes the scope into a research outline, searches online for 10–20 supporting articles, and saves a self-contained report to `research/<context-slug>/report.md`.

## Files

| File | Purpose |
|------|---------|
| `skills/Research-topic-prompt.md` | Full prompt instructions (grill → outline → search → write) |
| `.claude/skills/kb-research-topic/SKILL.md` | One-liner wrapper that delegates to the prompt file |

## Phase 1: Grill (adaptive)

Ask questions one at a time. Always start with these three:
1. What specifically about this topic? (scope narrowing)
2. What angle — overview, deep-dive, current events, investment thesis, other?
3. What will you use this for?

If answers reveal ambiguity or breadth, continue probing. Cap at ~8 questions. End with an explicit scope confirmation: "Here's what I understand we're researching: [summary]. Correct?"

Do not proceed to outline until the user confirms.

## Phase 2: Outline

From the confirmed scope, generate a structured outline of 3–5 sections. Each section is a focused sub-question that together covers the full scope. Present to the user for confirmation or edits before searching. This is the last gate before search.

## Phase 3: Search

For each outline section:
- Run 2–3 targeted queries using Tavily MCP if available, falling back to `WebSearch`
- Collect 3–5 high-quality articles per section
- Total across all sections: 10–20 articles
- Deduplication: check `kbm.log.md` and skip any URL whose source has already been ingested

## Phase 4: Write

**Output path:** `research/<context-slug>/report.md`
- `<context-slug>` is kebab-case derived from the topic (e.g. `us-semiconductor-tariffs`)
- Create the directory if it does not exist

**File structure:**

```markdown
# Research: [Topic]
*Generated: YYYY-MM-DD | Scope: [one-line from grill confirmation]*

## Research Outline
1. [Section 1]
2. [Section 2]
...

## [Section 1 title]
### [Article title]
- **Source**: https://...
- **Summary**: 2–3 sentences
- **Relevance**: why it supports this section

...

## Articles to Ingest
URLs ready for `/kb-scrapecontent` → `/kb-ingest`:
- https://...
- https://...
```

The "Articles to Ingest" section lists all unique URLs from the report so the user can feed them into the existing scrape → ingest pipeline. Once ingested, wiki notes will exist at predictable paths and can be linked from the report manually.

## Phase 5: Log

Append a row to `kbm.log.md`:
```
| YYYY-MM-DD | research/<context-slug>/report.md | research |
```

`research` is a new valid activity type for this skill.

## Constraints

- Do not invent facts or summaries — rely solely on fetched article content
- No conversational preamble in the report file; start directly with the `#` header
- If a search query returns no results for a section, note it in the report under that section heading
- If Tavily is unavailable and WebSearch also fails, note the failure and continue with remaining sections
