---
type: literature-note
source_url: https://dbdb.io/browse?type=graph
author: Unknown
tags: [graph-database, database-catalog, nosql, ai-assisted]
date_consumed: 2026-08-03
---

## Summary

DBDB.io (the Encyclopedia of Database Systems) catalogs over two dozen graph database systems spanning from 2000 to 2026, with widely varying project statuses and design characteristics. A notable pattern across the catalog is high abandonment: roughly half of the listed systems have been marked abandoned, while a growing cohort (launched 2023–2026) carries AI-Assisted tags. Multi-model and blockchain-integrated variants represent niche but recurring design directions within the graph database space.

## Core Concepts

- **[[DBDB.io]]** — community-maintained encyclopedia of database systems, cataloging properties such as start year, acquisition status, and feature tags for each system
- **[[Graph Database]]** — database that stores data as nodes and edges; the systems below are the catalog's graph database entries
- **[[Multi-Model Database]]** — systems like [[ArangoDB]], [[AgensGraph]], and [[AionDB]] support graph alongside other models (document, key-value) in a single engine
- **[[AI-Assisted Database]]** — tag applied to systems (e.g., AGEDB, [[ArangoDB]], [[ArcadeDB]], [[DGraph]], FalkorDB, Fluree, GenosDB, Engram) with AI-integrated features such as natural-language query or intelligent indexing
- **[[Blockchain]]-integrated graph databases** — ComposeDB and Fluree combine graph storage with on-chain or decentralized ledger semantics
- **Abandoned projects** — many graph databases (Asami, Blazegraph, CozoDB, CQLite, DegDB, DuctileDB, EliasDB, Fallen-8, FlockDB) have been deprecated or unmaintained, reflecting the difficulty of sustaining niche database projects

## Key Takeaways

- **Oldest entry**: CubicWeb (2000) — the longest-lived graph database listed.
- **High attrition**: ~10+ of ~26 entries are tagged Abandoned, indicating a difficult market to sustain.
- **AI wave (2023–2026)**: FalkorDB, GenosDB, Engram all launched recently with AI-Assisted tags.
- **2026 newcomers**: AionDB, Antfly, and Engram all started in 2026.
- **Acquired systems**: AgensGraph, Blazegraph, and DGraph were acquired by larger entities.
- **Multi-model consolidation**: ArangoDB, AgensGraph, and AionDB combine graph with other data models.
- **Blockchain niche**: Fluree (2017) and ComposeDB (2022) pair graph storage with blockchain — both are now abandoned or inactive.
- **Reference use**: DBDB.io is useful as a discovery catalog, not a comparative benchmark — detailed specs require per-system deep-dives.

## 🃏 Review Questions

**Q1**: What does the DBDB.io graph database catalog reveal about the overall health of the graph database ecosystem?
**A**: The catalog shows a high abandonment rate — roughly half the listed systems are tagged Abandoned — alongside a recent cohort of AI-Assisted entrants from 2023–2026, suggesting ongoing churn and experimentation in the space.

**Q2**: Which graph databases carry the AI-Assisted tag, and what does that tag signify on DBDB.io?
**A**: AGEDB, ArangoDB, ArcadeDB, DGraph, Engram, FalkorDB, Fluree, and GenosDB carry the AI-Assisted tag, indicating each system integrates AI-driven features (e.g., natural-language querying or intelligent indexing) as part of its offering.

**Q3**: How might an engineer use the DBDB.io graph database catalog when evaluating technology choices?
**A**: The catalog serves as a discovery and filtering tool — an engineer can quickly identify which systems are actively maintained (versus abandoned), whether they are multi-model, and when each was founded, then follow up with per-system documentation for deeper evaluation.
