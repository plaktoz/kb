---
name: kb-canvas
description: Build an Obsidian canvas for a given topic by linking related wiki notes as file nodes, with LLM-reasoned labeled edges between related pairs. Use when the user wants to visualise a topic as a concept map from their vault.
---

# KB Canvas Builder

You are a knowledge graph visualiser. Given a topic, you find the most relevant wiki notes in the vault, reason about the relationships between them, and produce an Obsidian canvas JSON file that maps out the conceptual landscape.

## Step 1 — Parse the topic

Extract the topic from the user's argument (the text after `/kb-canvas`). Derive 3–5 keywords for matching, including synonyms and closely related terms.

Example: `mental models` → keywords: `mental-model`, `mental model`, `first-principles`, `heuristic`, `cognitive-bias`, `decision`

## Step 2 — Build candidate list from kbm.log.md

Read `kbm.log.md`. Extract every row where the activity column is `ingest`. For each row, parse:
- `date` — the YYYY-MM-DD value in column 1
- `filename` — the value in column 2

Deduplicate by filename (keep the most recent date if a file appears multiple times). Sort the full list by date descending.

## Step 3 — Resolve wiki paths

For each candidate filename: if it starts with `wiki/`, use it directly as the file path. Otherwise (older log entries with raw filenames), run:
```bash
find wiki/ -name "<filename>"
```
Keep only files that are found. Drop any that resolve outside `wiki/`.

## Step 4 — Filter by topic relevance

For each resolved note:
1. Check if the **filename** contains any of the topic keywords (case-insensitive)
2. If not, read the file and check if any `[[wikilink]]` in the note contains a topic keyword

Keep the note if either check passes.

**Cap:** If more than 20 notes match, keep the 20 most recent (by kbm.log.md date) and print:

```
⚠️  <N> notes matched — showing the 20 most recent. Older notes were excluded.
```

If fewer than 2 notes match, tell the user: "Not enough notes found on '[topic]' to build a canvas. Try `/kb-research-topic` to build coverage first."

## Step 5 — Read all matched notes

Read the full content of every note in the filtered set. For each note, record:
- **id** — short unique string (e.g. `n1`, `n2`, …)
- **path** — relative path from vault root, e.g. `wiki/strategy/first-principles-thinking.md`
- **title** — filename without extension, converted from kebab-case to Title Case
- **wikilinks** — all `[[...]]` targets extracted from the note body

## Step 6 — Reason about relationships

For every pair of notes, decide:
1. Is there a meaningful relationship between the two concepts?
2. If yes, which label best describes it: `causes`, `enables`, `contrasts with`, `is a type of`, `supports`, `contradicts`

Use the note content, titles, and wikilinks to make this judgement. If no clear relationship exists, skip the pair (no edge).

Build an edge list:
```
{ fromId, toId, label }
```

Edges are directional — choose the direction that makes the label read naturally left-to-right (e.g. "first-principles-thinking → enables → second-order-thinking").

## Step 7 — Identify the hub node

Count the total edges (in + out) per node. The node with the highest count is the **hub**. If there is a tie, pick the node with the most recent ingest date.

Print: `Hub node: <title> (<N> connections)`

## Step 8 — Compute layout

Node dimensions: 250 wide × 60 tall. Column spacing: 320px. Row spacing: 160px.

```
N    = total node count
cols = ceil(sqrt(N))
rows = ceil(N / cols)
center_col = floor(cols / 2)
center_row = floor(rows / 2)
```

Assign grid positions to all non-hub nodes in any order, filling left-to-right, top-to-bottom — **skipping the center cell** `(center_col, center_row)`. Place the hub at the center cell.

Convert grid positions to pixel coordinates:
```
x = (col - center_col) * 320
y = (row - center_row) * 160
```

## Step 9 — Build the canvas JSON

Construct the Obsidian canvas object:

```json
{
  "nodes": [
    {
      "id": "<node-id>",
      "type": "file",
      "file": "<relative-path-from-vault-root>",
      "x": <integer>,
      "y": <integer>,
      "width": 250,
      "height": 60
    }
  ],
  "edges": [
    {
      "id": "<fromId>-<toId>",
      "fromNode": "<fromId>",
      "toNode": "<toId>",
      "label": "<relationship-label>"
    }
  ]
}
```

File paths must be relative to the vault root (e.g. `wiki/strategy/ooda-loop-decision-cycle.md`), not absolute.

## Step 10 — Determine output path

```
topic-slug = topic text converted to kebab-case, lowercased
today      = current date in YYYY-MM-DD format
base-path  = canvases/<topic-slug>/
filename   = <today>.canvas
```

If `canvases/<topic-slug>/<today>.canvas` already exists, append a sequence number: `<today>-2.canvas`, `<today>-3.canvas`, etc. until the path is unused.

Create the directory if it does not exist:
```bash
mkdir -p canvases/<topic-slug>/
```

Write the canvas JSON to the resolved path.

## Step 11 — Log the activity

Append to `kbm.log.md`:
```
| <today> | canvases/<topic-slug>/<filename> | canvas |
```

## Step 12 — Report to the user

Print a one-paragraph summary:

```
Canvas saved to canvases/<topic-slug>/<filename>
<N> notes · <M> edges · Hub: <hub-title> (<K> connections)
Open the file in Obsidian to explore the concept map.
```
