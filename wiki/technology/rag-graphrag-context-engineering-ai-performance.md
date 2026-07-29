---
type: literature-note
source_url: https://www.youtube.com/watch?v=pN-LfxNFiTc
author: IBM Technology (Martin Keen)
tags: [rag, graphrag, context-engineering, retrieval]
date_consumed: 2026-07-29
---

## Summary

Martin Keen argues that the primary bottleneck in AI performance is no longer model reasoning but context quality — the ability to retrieve the right data, in the right scope, with the right permissions, at inference time. He introduces [[Context Engineering]] as a discipline with four pillars and positions [[RAG]], [[GraphRAG]], and context compression as complementary precision retrieval strategies within it. The core thesis is that a contextually intelligent system produces dramatically better outcomes than a more powerful model with poor context.

## Core Concepts

- **[[Context Engineering]]**: The practice of designing systems that discover, filter, and deliver the right data to AI models at runtime, respecting governance constraints.
- **[[RAG]] (Retrieval-Augmented Generation)**: Chunks documents into vectors; at query time uses similarity search to retrieve closest matches — effective for simple lookups.
- **[[Agentic RAG]]**: Iterative retrieval — the agent makes an initial fetch, evaluates sufficiency, and loops back for more if needed.
- **[[GraphRAG]]**: Uses a graph structure to navigate context by entity relationships rather than purely semantic similarity; answers "what entities are connected to X and what documents relate to those entities."
- **[[Context Compression]]**: Summarizing and ranking retrieved content to maximize signal-to-noise before it enters the model's context window.
- **[[Zero Copy Federation]]**: Querying data where it lives rather than copying it to a central store, preserving freshness and original access controls.
- **[[Runtime Governance]]**: Enforcing data-access permissions live at retrieval time and response time, not just at system design time.
- **[[Knowledge Layer]]**: A semantic layer that applies entity resolution, relationship mapping, and institutional knowledge on top of raw data to give it meaning.

## Key Takeaways

- **Context is the bottleneck**, not model reasoning — frontier models reason well but fail on relevance.
- **Four pillars of context engineering**: connected access, knowledge layer, precision retrieval, runtime governance.
- **Better context ≠ more context**: precision retrieval filters by intent, role, time, and policy.
- **RAG for simple lookups; GraphRAG for relationship-aware retrieval**; compression for lean delivery.
- **Zero copy federation** keeps data fresh and preserves access controls without duplication.
- **Governance must be live**: enforce permissions at retrieval and response time, not just at design time.
- A **contextually intelligent system** outperforms a more powerful model with poor context.

## 🧠 First Principles & Mental Models

- **[[Signal-to-Noise Ratio]]**: Context compression applies this principle directly — more tokens in the window does not mean better output; only relevant tokens count toward useful inference.
- **[[Separation of Concerns]]**: The four-pillar framework cleanly separates data access, semantic enrichment, retrieval precision, and governance into distinct responsibilities, preventing any single layer from accumulating too much complexity.
