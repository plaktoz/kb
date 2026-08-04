---
type: literature-note
source_url: https://en.wikipedia.org/wiki/Graph_database
author: Wikipedia contributors
tags: [graph-database, nosql, data-storage, database-architecture]
date_consumed: 2026-08-03
---

## Summary

A graph database (GDB) uses nodes, edges, and properties to store and query data, with relationships as the central abstraction rather than tables or documents. Unlike [[Relational Database|relational databases]], graph databases store relationships persistently and enable constant-time traversal via index-free adjacency, making them significantly faster for highly interconnected datasets. They are classified as [[NoSQL]] and have evolved from 1960s network model databases to modern ACID-compliant, horizontally scalable systems like [[Neo4j]] and [[Amazon Neptune]].

## Core Concepts

- **[[Graph Database]]** — stores data as nodes, edges, and properties; relationships are first-class citizens persisted directly rather than computed via JOINs
- **[[Index-Free Adjacency]]** — each node stores direct references to neighbors, enabling O(1) adjacent node lookup versus O(log n) for index-based approaches
- **[[Labeled-Property Graph]]** — the dominant graph model; nodes and edges carry names and key-value properties; edges are always directed
- **[[Resource Description Framework]] (RDF)** — alternative graph model using subject-node, object-node, predicate-arc triples; standardized by W3C
- **[[NoSQL]]** — graph databases are classified as NoSQL; they offer flexible schemas where new data can be inserted without breaking existing functionality
- **[[Neo4j]]** — leading ACID-compliant graph database using the Cypher query language; GPLv3/commercial license
- **[[Amazon Neptune]]** — managed AWS graph database service; supports Gremlin, SPARQL, and openCypher
- **[[Cypher]]** — declarative SQL-like query language for Neo4j; also supported by Amazon Neptune as openCypher
- **[[Gremlin]]** — imperative graph programming language; part of Apache TinkerPop
- **[[SPARQL]]** — W3C-standardized query language for RDF databases
- **[[GQL]]** — ISO/IEC 39075 standard graph query language

## Key Takeaways

- **Core Abstraction**: Edges (relationships) are stored persistently — the key distinction from relational models.
- **Performance**: Index-free adjacency gives O(1) neighbor lookup; query time scales with portion queried, not total graph size.
- **Schema Flexibility**: New nodes/edges can be added without altering existing structure or breaking queries.
- **Graph Models**: Two main models — Labeled-Property Graph and RDF; most production systems use LPG.
- **Query Languages**: Cypher (Neo4j), Gremlin (TinkerPop), SPARQL (RDF/W3C), GQL (ISO standard).
- **Graph Categories (Gartner)**: Social, intent, consumption, interest, and mobile graphs cover the major use cases.
- **Migration Caution**: The graph model alone is insufficient justification to replace a relational DB — measurable performance gains of orders of magnitude should be demonstrable first.
- **Relational Databases Still Win**: Bulk operations on large flat datasets remain faster in relational systems.
- **Multi-Model Databases**: [[ArangoDB]] and [[OrientDB]] support key-value, document, and graph in one engine.

## First Principles & Mental Models

- **[[Locality of Reference]]**: Index-free adjacency embeds relationship pointers directly on each node, keeping traversal cost constant regardless of graph size — this is the same principle behind CPU cache locality applied to data storage, where proximity of related data eliminates expensive index lookups.
- **[[Right Tool for the Job]]**: Graph databases excel at relationship-heavy queries (friends-of-friends, shortest paths) but relational databases remain superior for bulk flat-data operations — the core engineering decision is to match the data model to the query shape, not to chase novelty.

## Review Questions

**Q1**: What is the central claim about why graph databases outperform relational databases for interconnected data?
**A**: Graph databases store relationships (edges) persistently with index-free adjacency, enabling O(1) neighbor traversal — relational databases must compute relationships at query time via costly JOIN operations.

**Q2**: How does index-free adjacency work, and what is its complexity advantage?
**A**: Each node stores direct references to its neighboring nodes (a "micro-index"), making adjacent node lookup run in O(1) constant time, compared to O(log n) for traditional index-based lookups; query time also scales with the portion of the graph queried rather than the total graph size.

**Q3**: When should you NOT migrate from a relational database to a graph database?
**A**: When dealing with large flat datasets where bulk operations are the primary workload — relational databases remain faster in those cases, and the graph model alone is insufficient justification; performance gains of orders of magnitude must be demonstrable before migration is warranted.
