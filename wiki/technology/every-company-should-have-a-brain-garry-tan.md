---
type: literature-note
source_url: https://www.youtube.com/watch?v=eBUyTS7SzV4
author: Garry Tan
tags: [ai-native, company-brain, context-engineering, skill-files]
date_consumed: 2026-08-01
---

## Summary

Garry Tan, President of Y Combinator, argues that AI has unlocked genuine 400x productivity gains — but only for founders who treat AI as a managed workforce, not mere auto-complete. He maps every component of an agentic system (skill files, resolver tables, trigger evals) onto org-chart equivalents, showing that a lean team encoding operations as executable skills is the new template for company building. The foundational layer beneath all of this is a "company brain" — a curated knowledge library plus a librarian agent — which he believes every company on earth will soon need.

## Core Concepts

- [[AI-Native Company]]: organizations structured from day one around skill files and agents rather than headcount
- [[Company Brain]] / [[GBrain]]: institutional knowledge layer combining a retrieval library with a librarian agent that selects the right context for each task
- [[Skill Files as Employees]]: each skill file encodes one capability, one job — the resolver table is the org chart, trigger evals are performance reviews
- [[Context Engineering]]: deciding which "three books" are open on the agent's desk at any moment; the hard part around [[Retrieval-Augmented Generation]]
- [[Latent Space vs Deterministic Space]]: LLMs handle taste, judgment, and ambiguity; code handles deterministic computation — mixing the two incorrectly is the root of most AI engineering bugs
- [[Skillify]]: Tan's practice of converting any completed one-off task into a reusable skill file before moving on
- [[Garry Tan]] / [[Y Combinator]]
- [[Miller's Law]]: human working memory caps at 7±2 items, which is why all institutions are prosthetics for that limit

## Key Takeaways

- **400x productivity**: Tan went from 14 lines/day in 2013 to ~400x output today — 8x floor, 80x median under skeptical assumptions.
- **Leverage is in wiring, not the model**: 2x and 100x users run the exact same [[Claude]].
- **Skill file = employee**: resolver table = org chart; filing rules = internal process; trigger evals = performance reviews.
- **YC Winter 25 batch**: 25% had 95%+ AI-generated codebases — now the fastest-growing, most profitable batch in YC history.
- **Company examples**: Emergence hit nine figures ARR in 8 months at 15 people; Retail reached $60M ARR with ~40 people.
- **Three books vs seven digits**: AI agents hold ~1M tokens (~1,000 pages); humans hold 7±2 items.
- **Never do one-off work**: always skillify after a completed task — if you ask twice, you failed.
- **Memory hygiene is mandatory**: uncurated brains become confident-but-wrong garbage dumps; provenance + contradiction checks + a librarian are required primitives.
- **Model quality is rented; your brain is owned**: the compounding advantage lives in the knowledge layer, not the model weights.
- **Non-engineers too**: YC's finance team now builds skill files and cron jobs — everyone becomes an agent manager.

## First Principles & Mental Models

- **[[Miller's Law]]**: Human working memory caps at 7±2 items, which is why every institutional structure ever built (checklists, org charts, filing cabinets) exists as a prosthetic — AI agents break this ceiling with million-token contexts, making entirely different organizational designs physically possible.
- **[[Compounding Knowledge]]**: Organizations that encode every completed task as a reusable skill accumulate compounding operational leverage; those doing one-off work reset to zero each morning, regardless of model quality.
