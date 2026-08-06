---
name: kb-research-company
description: Deep 6-part investment analysis of a company — business model, market, MOAT, financials, management, valuation — saved to research/<ticker>/report.md
when_to_use: When the user wants to research a company for long-term investment analysis. Invoke with /kb-research-company <TICKER>.
---

Run the parallel workflow `.claude/workflows/kb-research-company.js` with the ticker symbol as args.

## Analytical Framework

The report covers 6 parts, each researched by a dedicated agent:

**Part 1: Business Model** — Revenue mechanics, customer base, billing model, cyclicality, CAPEX, R&D, pricing power, industry challenges.

**Part 2: Market and Company Position** — TAM and growth, competitive positioning, differentiation, market share strategy, monopoly assessment, pre-mortem analysis.

**Part 3: MOAT** — Network effects, switching costs, pricing advantage, intangible assets, scale. Durability and trajectory.

**Part 4: Financials** — Margins, quality of earnings, operating leverage, capital allocation, key financial metrics over 5 years.

**Part 5: CEO and Management** — Track record, M&A history, compensation structure and KPI alignment, buyback strategy, ownership, communication style.

**Part 6: Valuation** — Reverse DCF implied growth rate, peer comparison, drivers of current valuation.

**Synthesis** — Bull vs. Bear summary distilling the key investment thesis tension.

## Output

`research/<ticker>/report.md`

## Constraints

- Objective analysis only — no investment recommendations
- Reputable sources only (SEC filings, IR pages, earnings transcripts, established financial news)
- No invented facts or unsupported claims
