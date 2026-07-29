---
type: literature-note
source_url: https://www.youtube.com/watch?v=JB2P5Gk23VI
author: IBM Technology (Sam Anthony)
tags: [rag, agentic-rag, information-retrieval, semantic-search]
date_consumed: 2026-07-29
---

## Summary

Information retrieval has evolved from simple keyword matching through semantic vector search to [[RAG]], and now into [[Agentic RAG]] where AI agents autonomously decide what to retrieve, when, and from where. Each generation solved the prior era's fundamental limitation — keyword search lacked meaning, RAG was static, and agentic RAG introduces dynamic, multi-step, adaptive reasoning. The hardest problem in AI, the author argues, is not generation but deciding what to look at.

## Core Concepts

- **[[Keyword Search]]**: Uses inverted indices and ranking algorithms like [[TF-IDF]] and [[BM25]] to match words as symbols; cannot understand synonyms, ambiguity, or intent.
- **[[Semantic Search]]**: Represents text as high-dimensional [[Vector Embeddings]] learned by neural networks; captures meaning so that conceptually similar terms cluster together in vector space.
- **[[Hybrid Retrieval]]**: Combines keyword search precision with semantic search recall; became the standard approach before and after RAG adoption.
- **[[RAG]] (Retrieval Augmented Generation)**: Documents are embedded offline into a vector database, retrieved at query time, and used to augment the LLM prompt — giving LLMs external memory without costly retraining.
- **[[Advanced RAG]]**: Adds rerankers, query rewriting, query expansion, and hybrid retrieval to static RAG pipelines; more accurate but still fundamentally predetermined.
- **[[Agentic RAG]]**: An AI [[Agent]] wraps the entire retrieval process, dynamically deciding whether to retrieve, where to search, what sub-questions to ask, when to stop, and how to synthesize — enabling multi-step research and cross-document synthesis.

## Key Takeaways

- **Keyword Search Limitation**: Treats words as symbols, not meaning; requires users to guess exact terms.
- **Semantic Search Leap**: Embeddings enable intent-based retrieval even without exact keyword matches.
- **RAG Grounding Effect**: External memory dramatically reduced hallucinations and unlocked specialized domains.
- **Traditional RAG Weakness**: Single-pass, linear, static — answer quality is ceiling-bounded by retrieval quality.
- **Advanced RAG Improvements**: Reranking, query rewriting, and hybrid retrieval raise accuracy but not adaptability.
- **Agentic RAG Capability**: Agents can invoke APIs, compare sources, validate claims, and refine queries iteratively.
- **Core Insight**: The next step is never better answers — it is systems that know how to find them.

## 🧠 First Principles & Mental Models

- **[[Abstraction Ladder]]**: Each generation of retrieval moves one rung up from mechanical symbol-matching toward genuine semantic understanding, with each rung solving the prior one's fundamental blindspot — a clear instance of progressive abstraction unlocking new capability.
- **[[Separation of Concerns]]**: Agentic RAG cleanly decouples the "what to retrieve" decision from the "how to generate" step, allowing each to improve independently — the same principle that makes modular software systems more robust.
