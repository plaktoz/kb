---
type: literature-note
source_url: https://microsoft.github.io/graphrag/
author: Microsoft Research
tags: [graphrag, rag, knowledge-graph, retrieval]
date_consumed: 2026-08-03
---

## Summary

Microsoft GraphRAG is a structured, hierarchical alternative to naive semantic-search RAG that extracts knowledge graphs from raw text, clusters entities into community hierarchies, and uses those structures to answer queries requiring holistic corpus reasoning or relationship-aware retrieval. It is especially effective where baseline RAG fails: connecting disparate information through shared attributes and summarizing concepts across large corpora. The system offers four distinct query modes ranging from global community-level reasoning to standard vector search.

## Core Concepts

- **[[GraphRAG]]**: A structured [[RAG]] approach that builds entity-relationship graphs and community hierarchies from raw text, rather than relying on flat vector similarity search.
- **[[Knowledge Graph]]**: The internal representation GraphRAG builds — entities, relationships, and key claims extracted from sliced text units.
- **TextUnits**: The atomic slices of the source corpus that GraphRAG indexes; analogous to chunks in standard RAG.
- **[[Leiden Technique]]**: A hierarchical community detection algorithm used to cluster entities into nested community structures after graph extraction.
- **Community Summaries**: Bottom-up, LLM-generated summaries of each community cluster, enabling global reasoning without retrieving raw documents.
- **Global Search**: Query mode that reasons holistically over the entire corpus via pre-built community summaries.
- **Local Search**: Query mode that retrieves context for a specific entity and fans out to its neighbors in the graph.
- **DRIFT Search**: An augmented Local Search that also incorporates community-level context alongside entity neighborhood traversal.
- **Basic Search**: Standard top-k vector similarity search, equivalent to naive RAG.

## Key Takeaways

- **GraphRAG vs baseline RAG**: GraphRAG excels at holistic summarization and connecting disparate information through shared attributes.
- **Indexing pipeline**: TextUnits → entity/relationship extraction → Leiden clustering → bottom-up community summaries.
- **Four query modes**: Global (corpus-wide), Local (entity-centric), DRIFT (local + community context), Basic (vector search).
- **Prompt tuning is essential**: Fine-tuning prompts for the domain is strongly recommended for best results.
- **Version management**: Run `graphrag init --root [path] --force` between minor version bumps to keep config format current.

## 🧠 First Principles & Mental Models

- **[[Hierarchical Abstraction]]**: By clustering entities into nested community hierarchies, GraphRAG compresses a large corpus into navigable levels of detail — the same principle that makes indexes faster than full-table scans, applied to semantic retrieval.
- **[[Separation of Concerns]]**: The four query modes expose distinct retrieval strategies rather than forcing one approach for all queries, allowing callers to match retrieval depth to query intent.

## 🃏 Review Questions

**Q1**: What is the central claim of Microsoft GraphRAG and how does it differ from standard RAG?
**A**: GraphRAG takes a structured, hierarchical approach rather than naive semantic similarity search; it builds entity-relationship graphs and community summaries that allow holistic corpus reasoning and connecting disparate information through shared attributes.

**Q2**: What are the four steps in the GraphRAG indexing pipeline?
**A**: The corpus is sliced into TextUnits, then entities, relationships, and key claims are extracted, then hierarchical clustering is applied via the Leiden technique, and finally bottom-up community summaries are generated.

**Q3**: When would you choose Global Search over Local Search in GraphRAG?
**A**: Use Global Search when the query requires holistic reasoning across the entire corpus (answered via community summaries); use Local Search when the query targets a specific entity and its graph neighborhood.
