---
source_url: https://weaviate.io/blog/introduction-to-rag
author: Mary Newhauser
date: 2024-10-15
---

# Introduction to LLM RAG - Retrieval Augmented Generation Explained

## Overview

Despite advances in generative LLMs, these models struggle with specialized knowledge tasks, leading to hallucinations — fabricated or inaccurate information presented convincingly. **Retrieval-Augmented Generation (RAG)** addresses this by letting models pull relevant external data at inference time rather than relying solely on training data.

## Limitations of Generative Models

Training datasets are inevitably incomplete — missing niche topics, post-cutoff developments, and proprietary internal data. When models don't know an answer, they often guess, sometimes producing confident but wrong responses.

## What is RAG?

RAG is a framework that augments a generative LLM's general knowledge with task-specific data retrieved from external sources at inference time. External sources can include internal databases, news articles, websites, and repositories. This enables models to:
- Respond more factually
- Cite sources
- Avoid guessing on unfamiliar topics

## RAG Architecture (Three Core Components)

1. **External Knowledge Source** — Non-parametric knowledge stored outside the model, often in vector databases. Examples: company databases, legal documents, medical literature, personal emails/files.

2. **Prompt Template** — A structured format that inserts retrieved context alongside the user query. Acts as the bridge between external data and the model.

3. **Generative LLM** — Receives the augmented prompt and produces a response combining internal knowledge with retrieved data.

## How RAG Works: Two Stages

### Stage 1: Ingestion
Raw external data is cleaned and converted into **embeddings** (vectorized representations), then stored in a vector database for efficient future retrieval.

### Stage 2: Inference
Three steps occur:
- **Retrieval** — The user query is embedded and compared against stored vectors via similarity search; closest matches are returned.
- **Augmentation** — Retrieved data is inserted into the prompt template.
- **Generation** — The LLM produces a fluent, contextually appropriate response using both its internal knowledge and the retrieved content.

## RAG Use Cases

- **Real-time information retrieval** — Accessing current news, stock prices, weather (e.g., ChatGPT-4o web browsing)
- **Content recommendation systems** — Personalizing suggestions by integrating user preference data
- **Personal AI assistants** — Tools like Microsoft Copilot querying emails, documents, and messages conversationally

## Implementation Frameworks

Three major open-source Python libraries:
- **LangChain** — Building blocks for LLM apps; pairs with LangGraph (agentic) and LangSmith (evaluation)
- **LlamaIndex** — External data integrations; maintains LlamaHub component repository
- **DSPy** — Modular optimization of LLM + retrieval model pipelines

## Advanced RAG Techniques

- **Pre-retrieval:** Metadata filtering, chunking strategies
- **Retrieval:** Hybrid search (combining semantic + keyword search)
- **Post-retrieval:** Re-ranking with ranker models, fine-tuning on domain data

### Agentic RAG
AI agents added to the pipeline can reformulate queries, re-retrieve information, handle multi-step reasoning, and iteratively adjust strategies.

### Graph RAG
Uses a knowledge graph to capture relationships between entities across an entire knowledge base, enabling cross-document comparison and summarization — beyond what standard similarity search supports.

## RAG Evaluation

### Component-Level
- **Retriever:** Measured on accuracy (precision of selection) and relevance (alignment with query context)
- **Generator:** Measured on faithfulness (consistency with source documents) and correctness (alignment with ground truth)

### End-to-End
**Answer Semantic Similarity** — compares generated responses against ground truth samples to assess overall pipeline quality.

**RAGAS** is a popular evaluation framework offering metrics for retrieval relevance, generation quality, and faithfulness without requiring human-labeled data.

## RAG vs. Fine-Tuning

Fine-tuning updates model weights on domain-specific data — useful for adopting specific tones or styles, but costly and time-consuming. RAG provides a practical alternative: models access external data dynamically without retraining, making it better suited for applications requiring real-time or frequently updated information.
