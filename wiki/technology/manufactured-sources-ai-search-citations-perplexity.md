---
type: literature-note
source_url: https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/
author: Trellner Research
tags: [ai-search, citation-quality, seo, perplexity]
date_consumed: 2026-09-03
---

## Summary

Trellner Research audited Perplexity's citation behavior across 380 software categories and found that 59.8% of citations pointed to domains outside the top 100,000 most-visited websites. Three coordinated sites — `wifitalents.com`, `worldmetrics.org`, and `gitnux.org` — collectively published 215,128 machine-generated "best software" pages with titles like "Facts & Grounding Page," terminology explicitly aimed at [[AI Retrieval]] systems rather than human readers. The findings expose a new attack surface where adversarial publishers manufacture content to exploit AI citation pipelines rather than traditional search rankings.

## Core Concepts

- **[[Perplexity AI]]**: AI-powered search engine whose citation layer was audited across `sonar` and `sonar-pro` models
- **[[AI Retrieval Grounding]]**: The mechanism by which LLM search tools select and cite web sources — the target of the manufactured content
- **[[Manufactured Grounding Content]]**: Machine-generated pages with zero independent credibility, specifically designed to be indexed and cited by AI retrieval systems
- **[[Citation Quality]]**: Measure of source authority and relevance; 23.4% of Perplexity citations pointed to domains outside the top 1 million websites
- **[[AI Search Optimization]]**: Emerging adversarial SEO discipline aimed at manipulating AI retrieval rather than human search rankings
- **[[Shared Retrieval Layer]]**: Both Perplexity model tiers (sonar, sonar-pro) returned identical citation lists in 289 of 380 categories (Jaccard 0.898), indicating a single shared index

## Key Takeaways

- **59.8% low-authority citations**: Majority of Perplexity's citations come from sites outside the top 100K most-visited.
- **215,128 manufactured pages**: Three coordinated domains published AI-targeted "grounding" pages post-late 2023.
- **Coordinated operation signals**: Same registrar, identical templates, cross-promotional posts across the three sites.
- **Internal inconsistency**: The three sites' rankings disagree — a site's top pick may not appear in another's top five.
- **Broken vendor URLs**: 1.1% of vendor URLs were unreachable; 6.1% redirected to unrelated domains (e.g. gambling portal).
- **One effective system**: Both Perplexity model tiers share a retrieval layer — testing two tiers is not independent sampling.
- **Guideflow citation**: A vendor's own marketing blog received 194 citations — more than Wikipedia's 3 total.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: AI retrieval systems optimized citations for "grounding signals" rather than credibility — publishers exploited that metric by labeling pages "Facts & Grounding," converting a proxy measure into a target to game.
- **[[Adversarial Dynamics]]**: Any sufficiently influential ranking system attracts adversarial optimization; the shift from human search to AI retrieval simply redirects the attack surface rather than eliminating it.

## 🃏 Review Questions

**Q1**: What is the central finding of Trellner Research's Perplexity citation audit?
**A**: 59.8% of Perplexity's citations in software categories pointed to domains outside the top 100,000 most-visited websites, with three coordinated domains manufacturing 215,128 AI-targeted "grounding" pages to exploit citation systems.

**Q2**: What evidence suggests the three grounding sites are coordinated and unreliable?
**A**: They share the same registrar, Cloudflare nameservers, and page templates, contain unrendered template variables in bylines, and their own rankings significantly contradict each other across the same software categories.

**Q3**: How should this finding change how practitioners evaluate AI search tool outputs?
**A**: Outputs from AI search tools like Perplexity should be treated with the same source-authority scrutiny as traditional research — citation count or model confidence does not imply source credibility, and a shared retrieval layer means two model tiers provide no independent corroboration.
