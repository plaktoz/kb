---
name: kb-compound
description: Compound this week's ingested wiki notes back into the vault — maintaining topic files in topics/ that grow richer each run. Mutates the vault directly. Run on Sundays before /kb-weekly-newsletter.
---

# KB Compound

You are a knowledge compounding assistant. Your job is to take this week's ingested notes and permanently enrich the vault by maintaining living topic files — synthesized prose documents that represent the vault's current understanding of each recurring theme.

This skill writes back to the vault. It does not produce a newsletter or digest — use `/kb-weekly-newsletter` for that.

## Step 1 — Determine the week

```bash
python3 .claude/skills/kb-log-rebuild/scripts/kb_log.py week
```

This prints the current ISO `year`, `week`, `monday` and `sunday`. Use them for every lookup below. On a Sunday this is the week that just ended. Run on another day, pass a date in the intended week, e.g. `week 2026-10-18`.

## Step 2 — Gather this week's ingested notes

```bash
python3 .claude/skills/kb-log-rebuild/scripts/kb_log.py rows --activity ingest --since <monday> --until <sunday>
```

Read the note at each entry's `path` fully. Skip entries whose `path` is null. If fewer than 2 notes were ingested this week, print "Fewer than 2 notes ingested this week — nothing to compound." and stop.

## Step 3 — Identify recurring themes

From the collected notes, identify themes that appear in 2 or more notes this week. A theme is a named concept, technology, framework, person, or trend discussed across multiple notes. For each theme, record:

- **Theme name** and proposed topic slug (kebab-case, e.g. `ai-agents`)
- **Notes it appears in this week** (slugs)

## Step 4 — Maintain topic files

For each theme identified in Step 3:

### 4a — Check for an existing topic file

Pick 2–4 search terms for the theme (its name plus close synonyms) and search the topic files:

```bash
python3 .claude/skills/kb-topic-query/scripts/vault_search.py "theme name" synonym --topics --limit 5
```

If `topics/<theme-slug>.md` is listed, or a listed topic file already covers this theme under another slug, proceed to **4c (Update)** with that file.

### 4b — Decide whether to create a new topic file

If no topic file exists, count vault-wide notes on this theme with the same terms:

```bash
python3 .claude/skills/kb-topic-query/scripts/vault_search.py "theme name" synonym
```

- Count the `notes` whose filename, tags or content meaningfully cover the theme. Notes with `filename` or `tags` in `matched` almost always qualify; check body-only matches before counting them
- If **5 or more** vault notes exist: proceed to **4d (Create)**
- If fewer than 5: record "threshold not met (N notes)" in the report and skip this theme

### 4c — Update an existing topic file

1. Read the topic file's `sources:` frontmatter list
2. Identify this week's theme notes that are **not already in the sources list**
3. If no new sources: skip this topic file entirely (do not rewrite, do not log)
4. If new sources exist:
   - Add the new slugs to the `sources:` frontmatter list
   - Update `last_updated:` to today's date
   - Choose the mode (see **Update modes** below), then update the prose body and the `## 🧠 Core Principles` section accordingly
   - Append a new entry to `## Weekly Updates`:
     ```
     ### YYYY-WNN
     - Added: [[slug-1]], [[slug-2]]
     ```

#### Update modes

A topic file can hold 100 or more sources, and the cost of reading them all grows every week. So the default is an **incremental update**, and a full re-synthesis runs only when the file is due for one.

Read `last_rewritten:` in the frontmatter.
- **Missing:** add `last_rewritten: <today>` as the baseline and do an incremental update. Do not rewrite on first sight, or every existing file would be due at once.
- **Less than 8 weeks ago:** incremental update.
- **8 weeks ago or more:** full re-synthesis, then set `last_rewritten:` to today.

**Incremental update.** The existing body already synthesizes the older sources, so don't re-read them.
1. Read the whole topic file, then read every new source note in full.
2. Weave the new sources into the existing prose. Extend a `##` section where a new source fits one, and add a new `##` section for a concept the file doesn't cover yet. Keep existing prose that still holds. Change a sentence only when a new source corrects or contradicts it, and when two sources disagree, say so and attribute each.
3. Re-test each existing principle against the new sources. Add the new slugs to its `→ explains:` list when they support it, and replace or add a principle only when the new sources together with the existing ones give it 2 or more supporting notes. Keep the cap of 5.
4. Open an older source in full only to check a specific claim before you change or extend it.

**Full re-synthesis.** Rewrite the entire prose body and rebuild `## 🧠 Core Principles` from all sources, as **Prose Body Format** and **Core Principles Section** describe. Read each source's `## Summary` and `## Key Takeaways`, and open the full note only when those don't settle a claim. Principles drawn from the rebuild still need 2 or more supporting notes.

Either way, the prose-only rule, the traceability rule and the Core Principles rules below apply.

### 4d — Create a new topic file

1. Collect all vault-wide notes on this theme (the 5+ identified in 4b, plus this week's notes)
2. Read them all in full
3. Create `topics/<theme-slug>.md` using the structure below, including the `## 🧠 Core Principles` section (see **Core Principles Section** below) and `last_rewritten:` set to today's date

### Prose Body Format

The body of a topic file is synthesized prose — not bullet lists. Each major concept or sub-theme gets its own `##` section with 2–4 connected sentences that integrate insights from multiple source notes. Write as if explaining the current state of knowledge to a thoughtful reader, not transcribing notes.

- Use `[[wiki-links]]` to reference specific vault notes inline when attributing a specific insight
- Each `##` section should integrate at least 2 source perspectives where possible
- Do not write bullet points in the body — prose only
- Do NOT copy sentences verbatim from source notes; synthesize and connect

### Core Principles Section

After writing the prose body, read `.claude/skills/kb-trunk-branch-extractor/SKILL.md` and apply its method to the full text of all source notes together. Ask for the **trunk with evidence** output, embedded at level 2 with the title `🧠 Core Principles`, and place it after the last prose section and before `## Weekly Updates`.

- **Keep at most 5 principles.** If more qualify, merge principles that rest on the same invariant first; then drop the ones the fewest source notes support.
- **Only include a principle that at least 2 source notes argue, explain, or test.** A principle that only one note supports belongs in that note's own Core Principles section, not in the topic file. A principle the notes merely assume as background doesn't count.
- After `→ explains:`, list the `[[source-slug]]` links of the notes the principle derives from, rather than individual claims.
- Look up model names in `data/mental-models.md` with one distinctive word from the name (`grep -i '<word>' data/mental-models.md`). If a row's Model or Aliases column names the same model, link the name in the **Model** column; otherwise use the model's standard name. Don't edit the list.
- If no principle clears the bar, omit the section. An absent section is better than a forced one.

This section is the one structured exception to the prose-only body, like `## Weekly Updates`. Keep principles out of the prose sections, and keep prose out of this one.

### Topic file template

```markdown
---
type: topic-file
topic: <theme-slug>
sources: [slug-1, slug-2, ...]
last_updated: YYYY-MM-DD
last_rewritten: YYYY-MM-DD
---

# <Theme Name>

[One-sentence framing of what this topic covers and why it matters in the vault.]

## <Concept or Sub-theme 1>

[2–4 sentences synthesizing what the vault knows about this concept, integrating multiple source notes with [[wiki-links]] where specific insights are attributed.]

## <Concept or Sub-theme 2>

[2–4 sentences...]

[Additional ## sections as needed — one per meaningful concept cluster]

## 🧠 Core Principles

**T1. [Principle]** — [stated as an invariant, 1–2 sentences] · *model:* [[Model Name]]
→ explains: [[slug-1]], [[slug-3]], [[slug-4]]

## Weekly Updates

### YYYY-WNN
- Added: [[slug-1]], [[slug-2]]
```

Every claim in the prose body and the Core Principles section must trace to a source note in the `sources:` list. Never add facts from training data.

### Running topics in parallel (optional)

Topic files are independent, so a run with many topics can fan out Agent/Task calls. Each agent reads this skill and updates only its assigned `topics/<slug>.md` files. The coordinator does the Step 5 logging and all git work, so agents never touch `kbm.log.md`.

- Give each agent **at most 2 topics**, and give a topic with 50 or more sources an agent of its own. The run takes as long as the slowest agent, so an agent with 7 topics sets the pace for the whole batch.
- Dispatch the agents in a single message.
- Tell each agent that incremental update is the default and which topics, if any, are due for a full re-synthesis.

## Step 5 — Report and log

After all changes, print a compact summary:

```
## Compound run: YYYY-WNN

**Topic files updated** (N):
- [[topic-slug]] — added X sources, incremental update (or full re-synthesis)

**Topic files created** (N):
- [[topic-slug]] — drew from N source notes

**Themes identified but no action taken** (explain why):
- [theme]: [reason — e.g. threshold not met (3 notes), or no new sources this week]
```

Log one `compound` row for each topic file modified or created, in a single call:

```bash
python3 .claude/skills/kb-log-rebuild/scripts/kb_log.py append --rows - <<'EOF'
[{"file": "topics/ai-agents.md", "activity": "compound"}]
EOF
```

Use the full relative path of each actual topic file. The date defaults to today.
