# kb-research-topic Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a `/kb-research-topic` skill that grills the user to refine a topic, decomposes it into a research outline, searches 10–20 supporting articles online, and saves a structured report to `research/<context-slug>/report.md`.

**Architecture:** A prompt file (`skills/Research-topic-prompt.md`) holds all phase instructions; a one-liner SKILL.md wrapper delegates to it — matching the existing `kb-daily`, `kb-weekly`, `kb-compound` pattern. CLAUDE.md is updated to register the new skill and activity type.

**Tech Stack:** Markdown prompt files, Tavily MCP (primary search), WebSearch (fallback), `kbm.log.md` for logging.

## Global Constraints

- Output files go to `research/<context-slug>/report.md` — create directory if absent
- Context slug: kebab-case derived from topic name
- Search: prefer Tavily MCP (`mcp_tavily_tavily-search` or `tavily-search`); fall back to WebSearch
- Deduplication: skip URLs whose source already appears in `kbm.log.md`
- No invented facts — summaries based solely on fetched content
- New log activity type: `research`
- Do not modify `data/` or anything in `.obsidian/`

---

### Task 1: Write `skills/Research-topic-prompt.md`

**Files:**
- Create: `skills/Research-topic-prompt.md`

**Interfaces:**
- Produces: a prompt file that phases through grill → outline → search → write → log
- Consumed by: `.claude/skills/kb-research-topic/SKILL.md` (Task 2)

- [ ] **Step 1: Create the prompt file with Phase 1 (Grill)**

Write `skills/Research-topic-prompt.md` with this exact content for Phase 1:

```markdown
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
```

- [ ] **Step 2: Append Phase 2 (Outline)**

Append to the same file:

```markdown
## Phase 2: Outline

From the confirmed scope, generate a structured outline of 3–5 sections. Each section is a focused sub-question that together covers the full scope.

Present the outline to the user:

> Here's the research outline:
> 1. [Section 1 — focused sub-question]
> 2. [Section 2 — focused sub-question]
> ...
>
> Does this cover what you need, or would you like to adjust any sections?

Do not proceed to Phase 3 until the user confirms the outline.
```

- [ ] **Step 3: Append Phase 3 (Search)**

Append to the same file:

```markdown
## Phase 3: Search

For each section in the confirmed outline:
1. Generate 2–3 targeted search queries specific to that section.
2. Use the Tavily MCP tool (`mcp_tavily_tavily-search` or `tavily-search`) if available; otherwise use WebSearch.
3. Collect 3–5 high-quality, relevant articles per section.
4. Open `kbm.log.md` and skip any article whose URL source already appears there.

Target total: 10–20 articles across all sections. Prioritize depth and quality over freshness.

If a section returns no results after all queries, note it and continue with remaining sections.
```

- [ ] **Step 4: Append Phase 4 (Write)**

Append to the same file:

```markdown
## Phase 4: Write Report

Derive the context slug: convert the confirmed topic to kebab-case (e.g. "US Semiconductor Tariffs" → `us-semiconductor-tariffs`).

Save to `research/<context-slug>/report.md`. Create the directory if it does not exist.

Use this exact structure — no conversational preamble, start directly with the `#` header:

---

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

---

Rules:
- Summaries must be based on fetched article content only — do not invent facts.
- If a section returned no results, write: `*No articles found for this section.*`
- List every unique URL from the report under "Articles to Ingest".
```

- [ ] **Step 5: Append Phase 5 (Log)**

Append to the same file:

```markdown
## Phase 5: Log

Append a row to `kbm.log.md` using today's date and the actual output path:

```
| YYYY-MM-DD | research/<context-slug>/report.md | research |
```
```

- [ ] **Step 6: Verify the file reads cleanly**

Read `skills/Research-topic-prompt.md` and confirm:
- All 5 phases are present in order
- No placeholder text ("TBD", "TODO", incomplete sections)
- Phase 1 ends with explicit user confirmation gate
- Phase 2 ends with explicit user confirmation gate
- Phase 4 output structure matches the spec exactly

---

### Task 2: Write `.claude/skills/kb-research-topic/SKILL.md`

**Files:**
- Create: `.claude/skills/kb-research-topic/SKILL.md`

**Interfaces:**
- Consumes: `skills/Research-topic-prompt.md` (Task 1)
- Produces: an invocable `/kb-research-topic` skill

- [ ] **Step 1: Create the skill directory and SKILL.md**

Create `.claude/skills/kb-research-topic/SKILL.md` with this exact content:

```markdown
---
name: kb-research-topic
description: Grill the user to refine a topic, decompose it into a research outline, search 10–20 supporting articles online, and save a structured report to research/<context-slug>/report.md. Use when the user wants to research a specific topic and build a sourced report ready for wiki ingestion.
---

Read the file `skills/Research-topic-prompt.md` and execute the instructions exactly as written.
```

- [ ] **Step 2: Verify structure matches existing kb-* skills**

Compare against `.claude/skills/kb-compound/SKILL.md` and `.claude/skills/kb-weekly/SKILL.md`:
- Frontmatter has `name` and `description` fields
- Description starts with a verb phrase describing what the skill does
- Body is a single delegation line pointing to the prompt file

---

### Task 3: Update `CLAUDE.md`

**Files:**
- Modify: `CLAUDE.md`

**Interfaces:**
- Consumes: nothing from prior tasks
- Produces: updated documentation so future agents know about the skill and the `research` activity type

- [ ] **Step 1: Add the skill to the skills table**

In `CLAUDE.md`, find the Skills table and add a row after the `Weekly-workflow-prompt.md` row:

```markdown
| `skills/Research-topic-prompt.md` | Grills user to refine a topic, builds a research outline, searches 10–20 articles, saves report to `research/<context-slug>/` |
```

- [ ] **Step 2: Add `research` to valid activity values**

In `CLAUDE.md`, find the line:

```
Valid activity values: `ingest`, `scrape`, `scrape-failed`, `news-fetch`, `newsletter`, `delete`, `reorg`
```

Update it to:

```
Valid activity values: `ingest`, `scrape`, `scrape-failed`, `news-fetch`, `newsletter`, `delete`, `reorg`, `research`
```

- [ ] **Step 3: Verify CLAUDE.md**

Read the updated `CLAUDE.md` and confirm both changes are present with no formatting breaks.

- [ ] **Step 4: Commit all changes**

```bash
git add skills/Research-topic-prompt.md .claude/skills/kb-research-topic/SKILL.md CLAUDE.md
git commit -m "feat: add kb-research-topic skill"
```
