---
type: literature-note
source_url: https://www.tigergraph.com/blog/graph-database-vs-relational-database/
additional_sources:
  - https://memgraph.com/blog/graph-database-vs-relational-database
author: Victor Lee; Memgraph
tags: [graph-database, relational-database, data-architecture, polyglot-architecture]
date_consumed: 2026-08-03
---

## Summary

Relational databases organize data in tables linked by foreign keys, excelling at transactional and aggregation workloads with decades of ecosystem maturity. [[Graph Database]]s store entities and relationships as native first-class types, making multi-hop traversals far faster than SQL JOINs — an advantage that compounds at scale. The core decision factor is relationship complexity; most organizations end up running both in a [[Polyglot Architecture]].

## Core Concepts

- **[[Relational Database]]**: Tables, rows, and foreign keys. Relationships are reconstructed at query time via SQL JOINs. Examples: [[PostgreSQL]], [[MySQL]], [[Microsoft SQL Server]].
- **[[Graph Database]]**: Uses a labeled property graph model with four core components: **nodes** (entities/vertices), **relationships** (edges/connections), **labels** (categories grouping similar nodes), and **properties** (key/value pairs on nodes or relationships). No JOIN reconstruction required. Examples: [[TigerGraph]], [[Neo4j]], [[Amazon Neptune]], [[Memgraph]].
- **[[Multi-Hop Query]]**: A traversal that follows multiple relationship links in sequence — the type of query where graph databases dramatically outperform relational ones.
- **[[Polyglot Architecture]]**: Running multiple database types together, each handling the workloads it does best.
- **Graph Query Languages**: [[Cypher]]/OpenCypher, [[Gremlin]], [[GQL]] (emerging industry standard), and [[GSQL]] (TigerGraph's SQL-like dialect).
- **ACID Compliance**: A strength of relational databases; ensures transactional integrity for workloads like inventory, order management, and finance.

## Key Takeaways

- **Relational strengths**: Minimal data duplication, ACID compliance, mature SQL ecosystem.
- **Relational weaknesses**: Multi-JOIN queries degrade at scale; rigid schema; poor fit for unstructured data.
- **Graph strengths**: Native relationship traversal; flexible schema; fast at multi-hop patterns.
- **Fraud detection**: Multi-hop pattern detection at 50M tx/day requires ~80ms response — SQL multi-joins cannot meet this.
- **Supply chain win**: Jaguar Land Rover cut evaluation time from 3 weeks to 45 minutes by replacing 23 relational tables with a graph model.
- **Customer 360**: Xandr traversed user journeys across 15 data properties using multi-hop graph queries.
- **7 warning signs for SQL outgrowth**: multiple JOINs routinely needed; query perf degrades with volume; relationship logic lives in app code; fraud patterns missed; weak recommendations; painful schema changes; product roadmap centers on networks/paths.
- **Switching advice**: Start with one high-value relationship-centric use case; expand incrementally rather than doing a full replacement.
- **Three diagnostic questions** (Memgraph): (1) Is your data highly connected? (2) Is retrieval more important than storage simplicity? (3) Does your data model change often? — Yes to any = graph database is likely a better fit.
- **When NOT to use graphs**: Full dataset scans by property value; simple key/value lookups (e.g., fetch user by ID); data dominated by large blobs or long text fields with no relational context.
- **[[GraphRAG]] and agentic AI pipelines**: An emerging use case where graph traversal powers retrieval-augmented generation and multi-step agent reasoning over connected knowledge.

## 🧠 First Principles & Mental Models

- **[[Right Tool for the Job]]**: Graph and relational databases are not substitutes but complements — each optimized for a different structural shape of data. Choosing based on data topology (tabular vs. networked) rather than familiarity prevents the mismatch where the wrong model forces expensive workarounds (JOIN ladders or app-layer graph logic in SQL).
- **[[Marginal Cost Thinking]]**: The cost of each additional JOIN in a relational query grows non-linearly with data volume, while graph traversal cost stays roughly constant per hop. This asymmetry explains why the switching threshold is not about data size but about relationship depth.

## 🃏 Review Questions

**Q1**: What is the central claim about when to choose a graph database over a relational one?
**A**: The core decision factor is relationship complexity — when queries must traverse multiple hops across connected entities, graph databases outperform relational ones, and that advantage grows with data scale.

**Q2**: What concrete performance example illustrates the graph database advantage in fraud detection?
**A**: At 50 million transactions per day, a relational multi-join analysis cannot meet the ~80ms response time requirement for detecting complex fraud schemes — a workload where multi-hop graph pattern detection excels.

**Q3**: How should an organization practically approach switching from relational to graph?
**A**: Full replacement is rarely necessary; instead, identify a single high-value use case centered on relationships, prove it out in a graph database, then expand incrementally while running a polyglot architecture alongside existing relational systems.
