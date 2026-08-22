---
type: literature-note
source_url: https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive
author: Connie Loizos
tags: [ai-biology, drug-discovery, biotech-startup, ai-model-training]
date_consumed: 2026-08-22
---

## Summary

Outer Biosciences, founded by Michael Polansky in 2022, keeps donated human skin tissue alive outside the body for up to a month (versus days for the industry norm) and pairs it with an [[AI Model]] that predicts which untested chemicals will improve a specific skin function, closing a discover-test-refine loop that now produces a new candidate roughly every six weeks.

## Core Concepts

- **[[Living Tissue Model]]**: Human skin sourced from surgical waste (mostly plastic surgery), kept alive via a proprietary nutrient/waste-removal system that preserves "day-zero" molecular programs for up to 30 days, enabling study of slow processes like collagen remodeling and barrier repair that a typical multi-day tissue culture can't capture.
- **[[Closed-Loop AI Discovery]]**: An AI model predicts promising untested chemicals → candidates are tested on living tissue → results (right or wrong) feed back into the model, compounding prediction accuracy over time.
- **[[Data Moat]]**: Because the living-tissue dataset doesn't exist anywhere else (there's no "biology internet" to scrape, unlike text-based AI), the proprietary data itself — not just the model — is the defensible asset.
- **[[On-Premise AI Infrastructure]]**: Outer Biosciences runs all AI work on-premise rather than in the cloud specifically to keep proprietary biological data out of third-party infrastructure.

## Key Takeaways

- **Six-week cadence**: The company now generates a new cosmetic-ingredient candidate roughly every six weeks, versus a couple of leads in 18 months under its earlier "brute force" literature-mining approach.
- **Regulatory path is lighter**: Because Outer Biosciences targets cosmetic (not drug) ingredients, there's no FDA approval — only standardized naming plus OECD-guideline safety testing accepted across 40+ countries.
- **Small addressable ingredient universe**: Only ~120–130 FDA-recognized OTC skin active ingredients exist; adding research-backed cosmetic ingredients brings the total closer to 200 — leaving room for AI-discovered additions.
- **Four of six current leads** are likely to reach commercialization, licensed to beauty/pharma partners rather than sold under Outer Biosciences' own brand.
- **Funding and scale**: ~$23M raised to date (Calm Capital, Brighter Capital, Polansky's own Hawktail); 19 employees, mostly near Cambridge, MA.
- A close competitor, Vivodyne, uses lab-grown synthetic organ tissue (not real donated tissue) paired with predictive AI for drug testing, and has raised ~$80M.

## 🧠 First Principles & Mental Models

- **[[Comparative Advantage]]**: Outer Biosciences deliberately avoids competing on model sophistication (where large AI labs dominate) and instead builds around a proprietary physical asset — living tissue — that can't be replicated by scraping the internet, a first-principles bet on defensibility through unique data generation rather than algorithmic novelty.

## 🃏 Review Questions

**Q1**: What is the core claim of the article?
**A**: Outer Biosciences pairs AI prediction with uniquely long-lived (up to 30-day) living human skin tissue to discover new cosmetic ingredients faster than traditional methods, using the proprietary tissue data itself as a competitive moat.

**Q2**: What specific technical advantage lets Outer Biosciences study effects that competitors can't?
**A**: Its tissue-support system keeps donated skin alive for up to a month instead of the industry-standard few days, enabling observation of slow biological processes — like collagen remodeling and post-sunburn recovery — that unfold over weeks.

**Q3**: Why does Outer Biosciences see its data, not just its AI model, as the core defensible asset?
**A**: Unlike text-based AI trained on scraped internet content, there is no public "biology internet" — its living-tissue experimental data is proprietary and can't be replicated by a competitor without building the same physical infrastructure.
