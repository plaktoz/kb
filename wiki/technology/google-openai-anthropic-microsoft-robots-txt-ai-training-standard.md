---
type: literature-note
source_url: https://www.techedt.com/google-joins-openai-and-anthropic-in-adopting-new-ai-scraping-controls
author: Joby Jean
tags: [ai-scraping, robots-txt, publishers, web-standards]
date_consumed: 2026-11-02
---

## Summary
Google, OpenAI, Anthropic and Microsoft have committed to support a proposed robots.txt directive, now before the IETF, that lets publishers signal AI-training preferences once instead of per-vendor. It separates AI training from search indexing but cannot undo past scraping. Rollout dates differ by company, and the standard's value depends on wider adoption.

## Core Concepts
- **[[robots.txt]] directive**: A common user-agent section for AI training, written by [[Kevin Kelley]] (Anthropic technical lead for standards) and proposed to the [[Internet Engineering Task Force]] (IETF).
- **[[Google]], [[OpenAI]], [[Anthropic]], [[Microsoft]]**: The four companies backing the shared standard.
- **[[Google-Extended]]**: Google's crawler for Gemini training; Google will map the new directive to it.
- **[[AI Training Crawlers]]**: Each company runs its own crawler names and rules, which makes blocking several of them tedious.
- **[[Search Indexing]] separation**: The directive restricts AI training collection without removing a site from search results.
- **[[Publisher Content Rights]]**: Publishers can block AI training while allowing selected sections, such as a press kit.

## Key Takeaways
- **One Directive**: A single robots.txt section replaces per-company crawler restrictions for AI training.
- **Granular Access**: Publishers can block news articles yet allow a press kit.
- **Search Preserved**: Blocking Google-Extended via the directive does not remove a site from Google Search.
- **No Retroactivity**: It cannot remove content already collected or affect models already trained.
- **Staggered Rollout**: Anthropic supports it now; OpenAI in coming months; Google early 2027; Microsoft 1 February 2027.
- **Adoption Risk**: Smaller AI developers must also respect it for the standard to work.

## 🧠 Core Principles

**T1. Shared standards cut per-party coordination cost** — When many independent actors each use their own identifiers and rules, the burden of expressing one preference falls on the party that must repeat it for each. A common interface lets one instruction reach all participants. · *model:* [[Coordination Problem]]
→ explains: One Directive, Granular Access

**T2. A voluntary standard is only as strong as its adoption** — A preference signal protects only against actors who recognise and honour it, and only going forward. Coverage and compliance decide its real effect. · *model:* [[Network Effects]]
→ explains: No Retroactivity, Staggered Rollout, Adoption Risk

## 🃏 Review Questions

**Q1**: What problem does the proposed robots.txt directive solve?
**A**: Publishers currently must identify each AI company's crawler and write separate restrictions. The directive gives one common section for signalling whether content may be collected for AI training.

**Q2**: How does the directive treat search indexing, and what can it not do?
**A**: It targets AI training only, so Google would apply it to Google-Extended without removing a site from search. It cannot reverse scraping already done or change models already trained.

**Q3**: What determines whether the standard will actually give publishers control?
**A**: Participating companies must implement it on their different timelines (Google in early 2027, Microsoft from 1 February 2027), and smaller AI developers must also respect it.
