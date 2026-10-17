---
name: kb-research-company
description: Deep 6-part long-term investment analysis of a company — business model, market position, MOAT, financials, management, valuation, plus a Bull vs. Bear synthesis — saved to research/<TICKER>/report.md. Use when the user wants to research a company or ticker for investment analysis, e.g. /kb-research-company AAPL.
---

The ticker is the skill argument (e.g. `/kb-research-company AAPL`). If none was given, ask for one before starting.

If the Workflow tool is available (Claude Code sessions), run it with `name: "kb-research-company"` and `args: "<TICKER>"`. Wait for the workflow to complete, then report the saved report path and any part that came back empty.

**Fallback (no Workflow tool, e.g. Cowork sessions):** Read `.claude/workflows/kb-research-company.js` and, in a single message, dispatch one general-purpose Agent/Task call per research prompt in it (7 total: Parts 1, 2, 3, 4a, 4b, 5, 6), each given the shared analyst persona plus its own part's questions and asked to return its markdown section. After all agents return, merge 4a and 4b into Part 4, then do the workflow's assembly step yourself: save each part to `research/<TICKER>/parts/part-N.md`, write the Bull vs. Bear synthesis, assemble `research/<TICKER>/report.md`, and log the single `research` row with `python3 .claude/skills/kb-log-rebuild/scripts/kb_log.py append`. Don't let sub-agents write the report or the log row. If Agent/Task tooling is also unavailable, research the six parts sequentially yourself.

## Analytical Framework

**Part 1: Business Model** — Revenue mechanics, customer base and concentration, billing model, cyclicality, CAPEX, R&D, pricing power, industry challenges.

**Part 2: Market and Company Position** — TAM and growth, competitive positioning, differentiation, market share strategy, monopoly assessment, pre-mortem analysis.

**Part 3: MOAT** — Network effects, switching costs, pricing advantage, intangible assets, scale. Durability and trajectory.

**Part 4: Financials** — Margins, quality of earnings, operating leverage, key metrics, and capital allocation over 5–10 years (researched as two parts, 4a and 4b).

**Part 5: CEO and Management** — Track record, M&A history, compensation KPIs and alignment, buyback strategy, ownership, communication style.

**Part 6: Valuation** — Reverse DCF implied growth rate, peer comparison, drivers of current valuation.

**Synthesis** — Bull vs. Bear summary distilling the key investment thesis tension.

## Output

- `research/<TICKER>/report.md` — the assembled report
- `research/<TICKER>/parts/part-1.md` … `part-6.md` — per-part staging files
- One `research` row in `kbm.log.md`

## Constraints

- Objective analysis only — no investment recommendations
- Reputable sources only (SEC/EDGAR filings, IR pages, earnings transcripts, established financial news) — no forums or social media
- No invented facts or unsupported claims
- Do not modify `data/investments.md`
