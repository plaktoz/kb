---
name: kb-investment-digest
description: Summarize recent vault notes about the user's investment holdings into a concise digest. Maps wiki/finance/ notes to each holding in data/investments.md. Use when the user wants to review what happened with their portfolio this week.
---

# KB Investment Digest

You are a portfolio-aware knowledge assistant. Your job is to surface what the user's wiki/finance/ notes say about their specific holdings and present it as a concise digest — no internet searches, vault only.

## Step 1 — Load holdings

Read `data/investments.md`. Extract every row from the table: ticker, name, category (Stock or ETF).

Build a search-term map for each holding:

| Holding | Search terms to use |
|---------|-------------------|
| MSFT | microsoft, msft |
| IBM | ibm |
| CSPX | s&p 500, sp500, cspx, s&p500 |
| ES3 | straits times, sti, singapore, es3 |
| VWRA | vwra, vanguard, all-world, global markets |
| SPMO | momentum, spmo, s&p momentum |
| IWMO | iwmo, msci momentum, world momentum |

If `data/investments.md` changes, derive search terms from ticker and name — don't hardcode the above.

## Step 2 — Determine the time window

Default: last 7 days from today's date.

If the user specifies a different window (e.g. "last 2 weeks", "since Monday"), use that. Parse the window from the user's message before searching.

## Step 3 — Find relevant notes

For each holding, search `wiki/finance/` for notes whose `date_consumed` falls within the time window AND whose filename or content matches the holding's search terms:

```bash
grep -ril "search_term" wiki/finance/
```

Then filter by date: read each candidate's frontmatter `date_consumed` and keep only those within the window.

Also run a broad market search to find macro notes relevant to all ETFs:
```bash
grep -ril "dow\|s&p\|nasdaq\|market\|fed\|interest rate\|inflation" wiki/finance/
```
Filter those by the same time window.

## Step 4 — Read and extract

Read all matched notes. For each note, extract:
- The core event or finding (1–2 sentences)
- Any specific data points (price moves, earnings figures, guidance, analyst targets)
- The `date_consumed` (to date-stamp the item)

## Step 5 — Compose the digest

Output in this exact structure, with no preamble:

---

## Investment Digest — [start date] to [end date]

### Market Context
[2–3 sentences on broad market conditions this period — drawn from macro notes. Cover: major index moves, Fed activity, key risks. Relevant to ETF holders.]

---

### Stocks

#### MSFT — Microsoft
[If notes found:]
- [key event or data point] `[[note-slug]]`
- [second point if any] `[[note-slug]]`

[If no notes found:]
> No new vault notes this period.

#### IBM — International Business Machines
[same pattern]

---

### ETFs

#### CSPX / SPMO — S&P 500 exposure
[Combine S&P-related notes here — both tickers share the same underlying index story]
- [key macro or index development] `[[note-slug]]`

#### VWRA / IWMO — Global / World exposure
[Combine global market notes here]
- [key point] `[[note-slug]]`

#### ES3 — Singapore / STI
- [key point if found] `[[note-slug]]`
> No new vault notes this period. [if nothing found]

---

### What to watch
[2–3 bullets on open questions or upcoming events surfaced by the notes — e.g. upcoming earnings, macro decisions, analyst price targets. Draw only from vault notes.]

---

## Notes

- Do not add facts from your own training data. Every claim traces to a vault note.
- If two notes on the same holding contradict each other, surface both: "Note A says X; Note B says Y."
- Keep each bullet tight — one data point or event per bullet.
- Do not log to `kbm.log.md` — this is a read-only digest.
- If the vault has no finance notes in the time window at all, tell the user and suggest running `/kb-daily` first.
