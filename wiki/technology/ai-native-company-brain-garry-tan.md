---
type: literature-note
source_url: https://www.youtube.com/watch?v=eBUyTS7SzV4
author: Garry Tan
tags: [ai-native, company-brain, context-engineering, productivity]
date_consumed: 2026-07-28
---

## Summary

[[Garry Tan]], President of [[Y Combinator]], argues that AI-native companies are achieving 8–400X productivity gains not by using better models, but by "wiring the work" differently — treating AI agents as a managed workforce of skill files and resolver tables. The organizational primitive is a "company brain": a curated knowledge library plus a librarian layer that selects the right context for every task. Companies that build this compound layer own their intelligence; those that don't wake up with amnesia every morning regardless of model quality.

## Core Concepts

- **[[AI-Native Company]]**: An organization designed from day one around skill files, agent workflows, and a company brain — not one that merely bolts AI onto existing processes.
- **[[Skill File]]**: A markdown file encoding one repeatable capability; functions as an employee with a single, clearly defined job.
- **[[Resolver Table]]**: A dispatch table mapping task types to the correct skill files; equivalent to an org chart for agent workflows.
- **[[Company Brain]] / [[GBrain]]**: A curated knowledge layer (library + librarian) that decides which context windows get loaded for any given agent task. Built as open-source by Garry Tan; analogous to Postgres for agents.
- **[[Context Engineering]]**: The discipline of deciding what information enters an agent's context window — framed as the difference between a genius agent and a goldfish agent.
- **[[Latent Space vs. Deterministic Space]]**: Latent space (LLM) handles taste, judgment, and ambiguity; deterministic space (code) handles structured computation. Bugs arise when work is placed in the wrong layer.
- **[[Skillification]]**: The practice of converting any completed one-off agent task into a reusable skill file; Garry Tan's core discipline for compounding institutional knowledge.
- **[[Miller's Law]]** (7 ± 2 working memory): All human institutions — checklists, org charts, filing cabinets — are prosthetics for this cognitive limit. AI agents holding ~1 million tokens break the same constraint at a different scale.
- **[[Y Combinator]]** Winter 2025 batch: 25% of companies had codebases 95% AI-generated; became the fastest-growing, most profitable batch in YC history.

## Key Takeaways

- **400X output claim**: Garry Tan measures his personal coding output at 400X vs. 2013 baseline; floor estimate 8X, median estimate ~80X under skeptical assumptions.
- **Same model, different results**: 2X and 100X engineers use identical [[Claude]] weights — leverage is in workflow wiring, not model choice.
- **Workforce metaphor**: Skill files = employees; resolver tables = org chart; filing rules = internal process; trigger evals = performance reviews.
- **Revenue-per-head records**: [[Emergence (YC S24)]] hit 9-figure ARR with 15 people at $15M ARR; [[Retailo (YC W24)]] hit $60M ARR with ~40 people.
- **400X is org-wide**: The multiplier applies to non-engineers (media, finance, ops) not just developers — YC finance staff collapsed 100 Excel workbooks into a single app; everyone becomes an agent manager who builds skill files and cron jobs.
- **Memory hygiene is critical**: Uncurated brains become "garbage dumps with great search" — provenance, contradiction checks, and active pruning are required.
- **Never do one-off work**: Always skillify completed tasks; asking for something twice is a system failure.
- **Model quality is rented; brain is owned**: Compounding institutional knowledge creates durable moats models cannot replicate.
- **Abundance framing**: Garry Tan closes with a personal anecdote — a father used an 80,000-file company brain to push the frontier of knowledge about his son's rare epilepsy.

## 🧠 First Principles & Mental Models

- **[[Miller's Law]]**: The 7 ± 2 working memory ceiling explains why every pre-AI institution was a prosthetic for human cognition; AI agents holding millions of tokens don't eliminate this limit — they relocate the bottleneck from memory to curation, which is exactly what context engineering solves.
- **[[Compounding Knowledge]]**: Skillifying every task is the organizational equivalent of reinvesting dividends — each captured workflow raises the baseline for future work, creating exponential rather than linear productivity growth over time.
