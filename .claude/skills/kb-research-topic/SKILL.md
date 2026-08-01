---
name: kb-research-topic
description: Grill the user to refine a topic, decompose it into a research outline, search 10–20 supporting articles online, and save a structured report to research/<context-slug>/report.md. Use when the user wants to research a specific topic and build a sourced report ready for wiki ingestion.
---

# Research Topic Prompt

You are a research assistant. Your task is to grill the user about a topic, build a research outline, search for supporting articles, and produce a structured report.

## Phase 1: Grill

Ask the user questions one at a time to nail down the research scope. Always start with these three questions in order:

1. What specifically about this topic are you trying to understand? (narrow the scope)
2. What angle? Options: introductory overview / deep technical dive / current events / investment thesis / other (describe).
3. What will you use this research for?

After each answer, assess whether scope is clear and tight. If the topic remains broad or ambiguous after these 3 questions, ask follow-up questions (up to ~8 total) until scope is unambiguous.

When scope is clear, confirm with the user:
> "Here's what I understand we're researching: [one-line summary of scope and angle]. Is that right?"

Do not proceed to Phase 2 until the user confirms.

## Phase 2: Outline

From the confirmed scope, generate a structured outline of 3–5 sections. Each section is a focused sub-question that together covers the full scope.

Present the outline to the user:

> Here's the research outline:
>
> 1. [Section 1 — focused sub-question]
> 2. [Section 2 — focused sub-question]
> ...
>
> Does this cover what you need, or would you like to adjust any sections?

Do not proceed to Phase 3 until the user confirms the outline.

## Phase 3: Search

For each section in the confirmed outline:

1. Generate 2–3 targeted search queries specific to that section.
2. Use the Tavily MCP tool (`mcp_tavily_tavily-search` or `tavily-search`) if available; otherwise use WebSearch.
3. Collect 3–5 high-quality, relevant articles per section.
4. Open `kbm.log.md` and skip any article whose URL source already appears there.

Target total: 10–20 articles across all sections. Prioritize depth and quality over freshness.

If a section returns no results after all queries, note it and continue with remaining sections.

## Phase 4: Write Report

Derive the context slug: convert the confirmed topic to kebab-case (e.g. "US Semiconductor Tariffs" → `us-semiconductor-tariffs`).

Save to `research/<context-slug>/report.md`. Create the directory if it does not exist.

Use this exact structure — no conversational preamble, start directly with the `#` header:

```markdown
# Research: [Topic]
*Generated: YYYY-MM-DD | Scope: [one-line from Phase 1 confirmation]*

## Research Outline

1. [Section 1]
2. [Section 2]
...

## [Section 1 title]

### [Article title]

- **Source**: https://...
- **Summary**: 2–3 sentences summarizing the article content based on what was fetched
- **Relevance**: one sentence on why this article supports this section

### [Next article title]
...

## [Section 2 title]
...

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://...
- https://...
```

Rules:

- Summaries must be based on fetched article content only — do not invent facts.
- If a section returned no results, write: `*No articles found for this section.*`
- List every unique URL from the report under "Articles to Ingest".

## Phase 5: Log

Append a row to `kbm.log.md` using today's date and the actual output path:

```text
| YYYY-MM-DD | research/<context-slug>/report.md | research |
```
