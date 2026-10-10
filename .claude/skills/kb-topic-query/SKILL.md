---
name: kb-topic-query
description: Search the local wiki vault for notes related to a topic or question and synthesize what is already known. Use when the user wants to recall or review knowledge from their vault without searching the internet.
---

# KB Topic Query

You are a knowledge retrieval assistant. Your job is to surface what the user already knows about a topic from their local wiki vault — no internet searches.

## Step 1 — Parse the query

Extract the core topic or question from the user's message. Identify 3–5 keywords that best represent it, including synonyms or related terms (e.g. "GLP-1" → also try "semaglutide", "ozempic", "weight loss drug").

## Step 2 — Search the vault

Run two passes:

**Pass 1 — Filename search:**
```bash
find wiki/ -name "*.md" | grep -iE "keyword1|keyword2|keyword3"
```

**Pass 2 — Content search:**
```bash
grep -ril "keyword1\|keyword2\|keyword3" wiki/
```

Merge both result lists and deduplicate. Rank results by:
1. Filename match (higher signal) over content-only match
2. More keyword hits over fewer

Take the top 10. If more than 10 match on filename alone, read all filename matches and drop to content-only matches as needed.

If no files match after both passes, try broader single-word queries. If still nothing, tell the user: "I couldn't find any notes on [topic] in your vault." and offer to run `/kb-research-topic` to build coverage from the internet.

## Step 3 — Read the notes

Read all matched files. For each note, extract:
- Core claims, findings, or arguments
- Key frameworks, models, or named concepts
- Statistics, data points, or named studies
- Existing Obsidian `[[links]]` to related notes
- Any `## 🧠 Core Principles` section, kept with its `→ explains:` lines

## Step 4 — Synthesize and output

Output in this exact order, with no preamble:

---

### What you know about [Topic]

[2–4 sentence flowing summary. Lead with the strongest or most surprising insight. If notes contradict each other, call that out explicitly rather than silently picking one side.]

**Key points**
- [Most important finding or claim] `[[note-slug]]`
- [Second finding] `[[note-slug]]`
- ... (max 8 bullets)

**What it rests on**
- **[Principle]** — [stated as an invariant, 1 sentence] `[[note-slug]]`, `[[note-slug]]`
- ... (max 3 bullets)

**Gaps**
[1–2 sentences on what the vault does NOT cover well. Suggest `/kb-research-topic` if there are obvious holes worth filling.]

---

## Notes

- For **What it rests on**, read `.claude/skills/kb-trunk-branch-extractor/SKILL.md` and apply its method to the notes you read, asking for the **trunk only** output. Start from the notes' own Core Principles sections where they exist. Cite the notes each principle comes from, and leave the section out if nothing qualifies.
- Every claim must trace to a vault note. Do not add facts from your own training data.
- If two notes conflict on the same point, surface the tension: "note-a says X, note-b says Y."
- Keep the summary tight — this is a recall tool, not a report.
- Do not log to kbm.log.md — queries are read-only operations.
