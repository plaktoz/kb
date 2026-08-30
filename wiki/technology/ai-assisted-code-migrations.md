---
type: literature-note
source_url: https://blog.pragmaticengineer.com/the-pulse-we-need-to-talk-about-migrations-with-ai/
author: Gergely Orosz
tags: [ai, code-migration, software-engineering, llm]
date_consumed: 2026-08-30
---

## Summary

Gergely Orosz examines the growing wave of AI-assisted code migrations, using Asana's Enzyme-to-React Testing Library migration as the central case study to reality-check OpenAI's marketing claims. While [[OpenAI]] claimed Asana completed "5 years of work in 2 weeks" for ~$12K, the actual context is more nuanced — the timeline reflected a low-priority opportunistic backlog, not a dedicated team effort. Across multiple companies, [[LLM]]-powered migrations are making previously impractical multi-year tasks executable in weeks, though engineer oversight remains essential throughout.

## Core Concepts

- **[[AI-Assisted Migration]]**: Using [[LLM]] pipelines to automate large-scale codebase refactors that would be impractical manually
- **[[Enzyme]] vs [[React Testing Library]]**: The two frameworks are philosophically different — Enzyme tests component instances directly, while RTL operates on the rendered DOM, making automated translation non-trivial
- **[[Phased Retry Pipeline]]**: Airbnb's strategy of iteratively applying LLM passes to handle progressively harder files (75% in first pass, 97% after four days, final 3% manually)
- **[[OpenAI Codex]]**: The tool Asana used; also the source of the viral (but decontextualized) "5 years in 2 weeks" claim
- **[[Engineering Cost Estimation]]**: The $6M comparison figure was a back-of-envelope estimate assuming full manual per-file effort — not a rigorous projection

## Key Takeaways

- **Asana's real story**: 4,000+ Enzyme files; ~25% already migrated before Codex; "5 years" was opportunistic backlog time.
- **Airbnb**: Migrated 3,500 Enzyme files in six weeks; 97% automated after four days.
- **Uber**: 600,000 JUnit 4→5 tests (15M LoC) in four months with just two engineers.
- **Bun**: 530,000 lines from Zig to Rust in two weeks for ~$165K in API costs.
- **Engineer involvement persists**: Planning, verification loops, and oversight remain essential — AI accelerates, not eliminates.
- **Paradigm shift**: Previously "impractical" multi-year migrations are now executable in weeks.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: OpenAI's "5 years in 2 weeks" framing optimizes for a compelling headline metric — actual engineering throughput is harder to compress into a single number, and the raw claim obscures crucial context about what the "5 years" actually represented.
- **[[Opportunity Cost]]**: The migration backlog wasn't worth doing manually because the opportunity cost of pulling engineers off higher-priority work was too high — AI changes the calculus by collapsing the labor cost asymmetry.

## 🃏 Review Questions

**Q1**: What was misleading about OpenAI's claim that Asana "cleared 5 years of work in 2 weeks with Codex"?
**A**: The "5 years" reflected how long a low-priority, opportunistic migration would take given competing priorities — not a dedicated team estimate. Asana had also already migrated ~25% of the files before Codex was used.

**Q2**: How did Airbnb structure its Enzyme-to-RTL migration pipeline to achieve 97% automation?
**A**: Airbnb used a phased retry pipeline: an initial LLM pass handled 75% of 3,500 files in four hours, reached 97% total after four days of iterative passes, and engineers finished the remaining 3% manually.

**Q3**: What does the Uber and Bun example suggest about the scope of migrations AI can now handle?
**A**: Uber migrated 600,000 JUnit tests with just two engineers in four months, and Bun converted 530,000 lines of Zig to Rust in two weeks — suggesting that even massive, previously decade-scale migrations are now within reach of small teams using LLM tooling.
