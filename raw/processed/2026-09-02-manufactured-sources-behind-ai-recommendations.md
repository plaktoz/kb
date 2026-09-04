---
source_url: https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/
title: "Three sites made 215,128 \"best software\" pages for AI. Perplexity cites them"
author: Trellner Research
date: 2026-09-02
---

# Three sites made 215,128 "best software" pages for AI. Perplexity cites them

**Author:** Trellner Research (Report ID: TR-2026-009)
**Date:** September 2, 2026

## Overview

Trellner Research queried two Perplexity models (`sonar` and `sonar-pro`) across 380 software categories, generating 7,534 citations. The central finding: **59.8% of citations point to domains ranked outside the top 100,000 most-visited websites**, and 23.4% don't appear in the top million at all.

## Top Citation Sources

- g2.com (291 citations)
- reddit.com (261)
- guideflow.com (194) — a *vendor's own marketing blog*, not a review site
- gartner.com (158)

Wikipedia received just 3 citations total.

## The "Grounding" Sites

Three domains — `wifitalents.com`, `worldmetrics.org`, and `gitnux.org` — collectively published **215,128 machine-generated "best [category] software" pages**, despite none existing before late 2023. Their homepages carry titles like "Facts & Grounding Page" — terminology aimed at AI retrieval systems, not human readers.

The sites show signs of common operation: same registrar, same Cloudflare nameservers, identical page templates, and cross-promotional blog posts. Notably, their rankings disagree significantly — for "project estimation software," one site's top pick doesn't appear in another's top five at all. Each page lists named editors, yet contains an unrendered template variable reading "Within the next 26 days" in the byline.

## Vendor Homepage Issues

Of 1,502 vendor URLs provided by the models, 17 (1.1%) were unreachable, and 92 (6.1%) redirected to different domains. Two notable misdirections:
- `dryad.co` (given for the Dryad data repository) redirects to an Indonesian gambling portal
- `montecarlo.com` (given for Monte Carlo data tools) leads to a Monaco hotel and casino group

## Limitations

The two model tiers returned **identical citation lists in 289 of 380 categories** (Jaccard overlap of 0.898), indicating a shared retrieval layer — making them effectively one system sampled twice. The study covers only Perplexity; no claims extend to other AI search tools. The researchers also note they did **not test whether removing these sources changes recommendations**.
