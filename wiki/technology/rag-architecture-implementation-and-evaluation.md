---
type: literature-note
source_url: https://weaviate.io/blog/introduction-to-rag
author: Mary Newhauser
tags: [rag, retrieval-augmented-generation, vector-database, llm-evaluation]
date_consumed: 2026-08-03
---

## Summary

[[Retrieval-Augmented Generation]] (RAG) is a framework that supplements a generative [[Large Language Model]] with task-specific external data retrieved at inference time, addressing hallucination and knowledge staleness without retraining. The pipeline has two phases — ingestion (embedding and indexing external data) and inference (retrieve, augment, generate) — and is evaluated at both component level (retriever accuracy, generator faithfulness) and end-to-end semantic similarity. For dynamic or frequently updated knowledge domains, RAG is a more practical choice than fine-tuning.

## Core Concepts

- **[[Retrieval-Augmented Generation]] (RAG)**: Framework letting an LLM query external non-parametric knowledge at inference time rather than relying solely on training data.
- **[[Hallucination]]**: LLM behavior of confidently fabricating information when its training data lacks an answer.
- **[[Vector Database]]**: Stores embedded representations of external documents; enables similarity search during the retrieval step.
- **Embeddings**: Vectorized representations of text used to convert both documents and queries into comparable numerical form.
- **Prompt Template**: Structured format that injects retrieved context alongside the user query before passing to the LLM.
- **[[LangChain]]**: Open-source Python framework providing building blocks for LLM apps; paired with LangGraph (agentic) and LangSmith (evaluation).
- **[[LlamaIndex]]**: Python library focused on external data integrations; maintains LlamaHub component repository.
- **[[DSPy]]**: Framework for modular optimization of LLM and retrieval model pipelines.
- **[[Agentic RAG]]**: Extension where AI agents reformulate queries, re-retrieve iteratively, and handle multi-step reasoning within the RAG pipeline.
- **[[Graph RAG]]**: Uses a knowledge graph to capture entity relationships across documents, enabling cross-document comparison beyond similarity search.
- **[[RAGAS]]**: Evaluation framework offering retrieval relevance, generation quality, and faithfulness metrics without requiring human-labeled data.

## Key Takeaways

- **Three RAG components**: External knowledge source, prompt template, generative LLM.
- **Ingestion stage**: Raw data cleaned → embedded → stored in vector database.
- **Inference stage**: Query embedded → similarity search retrieves matches → augmented prompt sent to LLM.
- **Use cases**: Real-time info retrieval, content recommendation, personal AI assistants (e.g., Microsoft Copilot).
- **Advanced retrieval**: Hybrid search combines semantic + keyword search for better recall.
- **Post-retrieval improvement**: Re-ranking with ranker models raises retrieved context quality.
- **RAG vs. fine-tuning**: Fine-tuning adjusts model weights (useful for tone/style); RAG is better for real-time or frequently updated data.
- **Retriever metrics**: Accuracy (precision of selection) and relevance (alignment with query context).
- **Generator metrics**: Faithfulness (consistency with source) and correctness (alignment with ground truth).
- **End-to-end metric**: Answer semantic similarity compared against ground truth samples.

## 🧠 First Principles & Mental Models

- **[[Separation of Memory and Reasoning]]**: RAG externalizes factual memory into a mutable vector store while reasoning stays inside the model — knowledge can be updated without touching model weights, mirroring how humans consult references rather than memorizing everything.
- **[[Garbage In, Garbage Out]]**: Retriever quality is the binding constraint on final answer quality — a perfect generator cannot overcome irrelevant or stale retrieved context, which is why chunking strategy, hybrid search, and re-ranking matter as much as model choice.

## 🃏 Review Questions

**Q1**: What core problem does RAG solve that standard generative LLMs cannot address on their own?
**A**: LLMs are trained on finite datasets and cannot access post-cutoff or proprietary information, leading to hallucination; RAG retrieves relevant external data at inference time so the model responds factually without retraining.

**Q2**: What are the two stages of a RAG pipeline, and what happens in each?
**A**: Ingestion — raw data is embedded and stored in a vector database. Inference — the user query is embedded, matched against stored vectors via similarity search, retrieved context is inserted into a prompt template, and the LLM generates a response.

**Q3**: When should you prefer RAG over fine-tuning for a domain-specific application?
**A**: Choose RAG when the knowledge domain requires real-time or frequently updated information; fine-tuning is better suited for adapting model tone or style to a fixed domain, but is costly and does not scale well with changing data.
