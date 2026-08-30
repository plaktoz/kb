---
source_url: https://blog.pragmaticengineer.com/the-pulse-we-need-to-talk-about-migrations-with-ai/
author: Gergely Orosz
date: 2026-08-27
---

# The Pulse: We need to talk about migrations with AI

The article examines AI-assisted code migrations, using Asana's Enzyme-to-React Testing Library migration as the central case study.

## The Asana Case

OpenAI claimed Asana "cleared 5 years of engineering work in 2 weeks with Codex" at ~$12K, versus a prior estimate of $6M. Dan Ubilla (Asana's Developer Productivity lead) clarified the full picture:

- Asana had 4,000+ Enzyme files; they'd already migrated ~25% in 2024
- The "5 years" wasn't a dedicated team effort — it reflected how long the *opportunistic, low-priority* migration would realistically take given competing priorities
- The $6M figure was a back-of-envelope estimate assuming manual, per-file effort multiplied by engineer hourly rates

## Airbnb's Comparable Migration (March 2025)

Airbnb migrated 3,500 Enzyme test files in six weeks using LLMs. A phased retry pipeline handled 75% of files in four hours; 97% total after four days; engineers finished the remaining 3% manually.

## Why Enzyme→RTL Is Hard

The two frameworks are philosophically different: Enzyme tests component instances directly, while React Testing Library operates on the rendered DOM. Side-by-side test code shares almost nothing except imports.

## Other AI Migration Examples

- Uber: 600,000 JUnit 4→5 tests (15M lines of code) migrated in four months with two engineers
- Bun: 530,000 lines from Zig to Rust in two weeks for ~$165K in API costs

## Key Takeaway

AI doesn't eliminate engineer involvement — planning, verification loops, and oversight remain essential. But previously "impractical" multi-year migrations are now executable in weeks, and the author notes: "I always dreaded migrations, so I see it as good news that we have a new tool."
