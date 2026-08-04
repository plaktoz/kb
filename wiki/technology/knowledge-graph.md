---
type: literature-note
source_url: https://en.wikipedia.org/wiki/Knowledge_graph
author: Wikipedia contributors
tags: [knowledge-graph, semantic-web, graph-database, entity-alignment]
date_consumed: 2026-08-03
---

## Summary

A knowledge graph is a knowledge base that uses a graph-structured data model to represent entities and their inter-relationships, encoding the free-form semantics underlying those entities. Originally associated with linked open data and search engines, knowledge graphs have expanded into machine learning applications — including [[GraphRAG]] — and scientific domains like genomics and proteomics. Active research areas include entity alignment across heterogeneous graphs, where [[Large Language Models]] have shown recent promise.

## Core Concepts

- **[[Knowledge Graph]]** — a graph-structured knowledge base encoding entities and semantic relationships; used by [[Google]], Bing, WolframAlpha, LinkedIn, and others
- **[[Semantic Web]]** — the broader linked open data ecosystem from which knowledge graphs emerged, built on standards like RDF and OWL
- **[[Graph Neural Network]]** — ML architecture that operates on graph-structured data; has extended knowledge graph use into genomics and systems biology
- **[[GraphRAG]]** — Microsoft Research's 2024 framework integrating LLM-generated knowledge graphs into [[Retrieval-Augmented Generation]] pipelines
- **[[Wikidata]]** — open knowledge graph maintained by the Wikimedia Foundation; a major publicly available implementation
- **[[Neo4j]]** — widely used graph database platform for building and querying knowledge graphs
- **Virtual knowledge graph** — queries an underlying relational database without storing data in a dedicated graph store, reducing migration cost
- **Entity alignment** — the problem of identifying nodes across different graphs that refer to the same real-world entity; an open research challenge

## Key Takeaways

- **Origins**: Term coined by Austrian linguist Edgar W. Schneider in 1972.
- **Mainstream adoption**: Google's 2012 Knowledge Graph brought the concept into consumer search.
- **Modern implementations**: [[YAGO]], [[Wikidata]], [[Neo4j]], GraphDB are leading open/commercial systems.
- **GraphRAG milestone**: Microsoft Research's 2024 GraphRAG linked LLMs to knowledge graph retrieval.
- **Virtual graphs**: Query relational data as a graph without full migration — lowers adoption barrier.
- **Entity alignment**: Matching cross-graph nodes is unsolved; LLMs show promise since 2023.
- **Science applications**: Graph neural networks expanded KG use into proteomics and systems biology.

## 🧠 First Principles & Mental Models

- **[[Abstraction Ladder]]**: Knowledge graphs sit at the highest rung — stripping raw data down to pure relational structure — which is why they transfer across domains from search to genomics without redesign.
- **[[Network Effects]]**: The value of a knowledge graph grows non-linearly with each new entity and relation added, explaining why open projects like Wikidata attract sustained community contribution.

## 🃏 Review Questions

**Q1**: What is a knowledge graph and what distinguishes it from a conventional relational database?
**A**: A knowledge graph uses a graph-structured model to represent entities and their semantic relationships, encoding free-form meaning rather than rigid table schemas.

**Q2**: What is a virtual knowledge graph and why does it matter for adoption?
**A**: A virtual knowledge graph queries an underlying relational database directly rather than migrating data into a graph store, lowering the barrier for organisations that already have relational data.

**Q3**: How has GraphRAG advanced the practical use of knowledge graphs?
**A**: Microsoft Research's 2024 GraphRAG framework integrates LLM-generated knowledge graphs into retrieval-augmented generation pipelines, improving the quality and traceability of AI-generated answers over large corpora.
