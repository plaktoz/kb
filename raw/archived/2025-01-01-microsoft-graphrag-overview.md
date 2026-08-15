---
source_url: https://microsoft.github.io/graphrag/
author: Microsoft Research
date: 2025-01-01
---

# Welcome to GraphRAG

## Overview

GraphRAG is "a structured, hierarchical approach to Retrieval Augmented Generation (RAG), as opposed to naive semantic-search approaches using plain text snippets."

It extracts knowledge graphs from raw text, builds community hierarchies, generates summaries, and uses these structures for RAG tasks.

## GraphRAG vs Baseline RAG

Standard RAG uses vector similarity search. GraphRAG improves on this, particularly where baseline RAG struggles:

- Connecting disparate information through shared attributes
- Holistically summarizing concepts across large data collections

## The GraphRAG Process

### Indexing
1. Slice corpus into **TextUnits**
2. Extract entities, relationships, and key claims
3. Hierarchical clustering via the **Leiden technique**
4. Generate bottom-up community summaries

### Query Modes
- **Global Search** – holistic corpus reasoning via community summaries
- **Local Search** – specific entity reasoning, fanning out to neighbors
- **DRIFT Search** – like Local Search, augmented with community context
- **Basic Search** – standard top-k vector search

### Prompt Tuning
Fine-tuning prompts is strongly recommended for best results.

## Versioning
Run `graphrag init --root [path] --force` between minor version bumps to maintain current config format.
