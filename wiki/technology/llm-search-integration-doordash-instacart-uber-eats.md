---
type: literature-note
source_url: https://blog.bytebytego.com/p/why-doordash-instacart-and-uber-eats
author: ByteByteGo
tags: [llm-integration, search-architecture, rag, food-delivery-tech]
date_consumed: 2026-07-29
---

## Summary

DoorDash, Instacart, and Uber Eats each integrated LLMs into search differently despite facing the same problem and research base, because each company's pre-existing infrastructure — not model choice — determined the cheapest path forward. DoorDash uses LLMs offline to enrich a knowledge graph while keeping runtime retrieval classical; Instacart layers RAG and a fine-tuned Llama-3-8B for query understanding across head and tail traffic; Uber Eats fine-tuned Qwen as the embedding backbone of a two-tower retrieval system spanning every vertical and language. Across all three, hybrid systems and output guardrails remain the constant.

## Core Concepts

- [[Retrieval-Augmented Generation]] — used as an output-constraining guardrail at DoorDash and as context injection at Instacart
- [[Knowledge Graph]] — DoorDash's structured item/restaurant graph, enriched offline by LLMs
- [[Two-Tower Retrieval]] — Uber Eats' architecture pairing a query encoder and document encoder in a shared embedding space
- [[Fine-Tuning]] — Instacart's Llama-3-8B and Uber Eats' Qwen backbone, both tuned on proprietary interaction data
- [[Matryoshka Representation Learning]] — technique letting Uber Eats truncate embeddings to 256 dimensions with under 0.3% recall loss
- [[Long-Tail Query Problem]] — rare queries that specialized models struggle to serve, handled differently by each company
- [[DoorDash]], [[Instacart]], [[Uber Eats]] — the three companies compared

## Key Takeaways

- DoorDash: LLM stays offline, enriches the graph; ~30% lift in dish-carousel trigger rate
- Instacart: offline RAG for head queries, fine-tuned Llama-3-8B under 300ms for tail queries
- Uber Eats: fine-tuned Qwen embeds every query and document into one shared vector space
- Instacart's query rewrite coverage rose from 50% to over 95% after the redesign
- Integration depth was set by each company's existing infrastructure, not model choice
- Guardrails (constrained vocabularies, similarity filters) are universal across all three systems

## 🧠 First Principles & Mental Models

- [[Path Dependence]] — the article's central thesis is that each company's existing infrastructure, not the available models or research, determined which LLM integration pattern was cheapest and thus chosen.
