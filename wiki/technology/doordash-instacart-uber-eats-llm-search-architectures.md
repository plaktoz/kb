---
type: literature-note
source_url: https://blog.bytebytego.com/p/why-doordash-instacart-and-uber-eats
author: ByteByteGo
tags: [llm, search, retrieval, production-ai]
date_consumed: 2026-08-01
---

## Summary

DoorDash, Instacart, and Uber Eats each rebuilt their search systems around LLMs yet arrived at three distinct architectures, driven not by model choice but by the infrastructure each company already had. The key design question is how deeply the LLM should sit in the runtime — from offline enrichment at the periphery (DoorDash) to being the core embedding backbone (Uber Eats). Each approach reveals that hybrid systems combining classical retrieval with LLMs remain the practical default in production.

## Core Concepts

- **[[LLM Integration Depth]]**: The spectrum from offline-only LLM enrichment to LLM-as-retrieval-backbone, with query-understanding as a middle layer.
- **[[Knowledge Graph]]**: [[DoorDash]] used a pre-existing structured graph of item attributes (dish type, dietary preference, cuisine); LLMs enriched it offline and parsed queries to link against it.
- **[[Retrieval-Augmented Generation]] (RAG)**: Used as a guardrail by DoorDash — the LLM picks from a retrieved taxonomy shortlist rather than generating free-form output.
- **[[Two-Tower Retrieval]]**: [[Uber Eats]] architecture with separate query and document encoders, fine-tuned [[Qwen LLM]] as the backbone embedding layer, pre-computing document vectors into an [[HNSW]] vector index.
- **[[Fine-Tuning]]**: [[Instacart]] fine-tuned [[Llama-3-8B]] on proprietary data for real-time tail query handling; Uber Eats fine-tuned Qwen for domain alignment across verticals and languages.
- **[[Head vs. Tail Query Distribution]]**: Instacart splits serving — offline RAG-and-cache pipeline for frequent head queries; real-time fine-tuned model for cold-start tail queries.
- **[[Matryoshka Representation Learning]]**: Uber Eats optimization allowing embedding truncation (1536 → 256 dimensions, <0.3% recall loss) to reduce storage and latency.
- **[[Scalar Quantization]]**: int7 instead of float32, halving latency with recall above 0.95.
- **[[Constrained Output Space]]**: DoorDash inverts the standard RAG pattern — RAG defines valid output labels; the LLM selects from them rather than generating freely.

## Key Takeaways

- **DoorDash (LLM at periphery)**: Enriches knowledge graph offline; parses queries into typed chunks at runtime; retrieval stays classical.
- **Instacart (LLM at query layer)**: Unified LLM strategy replacing fragmented FastText/BERT models; head queries via cached RAG, tail via real-time Llama-3-8B.
- **Uber Eats (LLM as backbone)**: Fine-tuned Qwen powers both query and document towers; one model handles all verticals and languages.
- **Infrastructure determines architecture**: Each company's position on the integration-depth spectrum traced directly to what they already had.
- **DoorDash lift**: ~30% increase in trigger rate for popular dish carousels.
- **Instacart results**: Query rewrite coverage jumped from 50% to 95%; tail-query complaints halved; scroll depth cut 6%.
- **Uber Eats efficiency**: ANN tuning cut latency 34% and CPU 17%; quantization halved latency; MRL cut storage ~50%.
- **Hybrid systems are universal**: Classical retrieval, knowledge graphs, and ANN indexes do most of the work everywhere.
- **World knowledge is a head start, not the answer**: Domain context must still be injected via RAG, fine-tuning, or both.
- **Guardrails matter in every production LLM system**: Constrained vocabularies, similarity filters, and taxonomy enforcement keep outputs catalog-aligned.

## First Principles & Mental Models

- **[[Path Dependence]]**: Each company's LLM architecture was constrained by the systems already in production — DoorDash had a knowledge graph, Instacart had fragmented query models, Uber Eats had per-vertical two-tower infrastructure. The optimal solution was local to the existing stack, not globally optimal.
- **[[Pareto Principle]]**: Instacart's head/tail split explicitly acknowledges that ~98% of queries are well-served by cached patterns; engineering effort for the bottom 2% (real-time fine-tuned model) yields disproportionate quality improvements for cold-start coverage.
