---
type: literature-note
source_url: https://pallab29.medium.com/building-a-rag-pipeline-with-llamaindex-a-step-by-step-guide-1c7964e6d06a
author: Pallab Sarangi
tags: [llamaindex, rag, retrieval-augmented-generation, vector-index]
date_consumed: 2026-08-09
---

## Summary

This tutorial walks through building a complete [[Retrieval-Augmented Generation]] pipeline using [[LlamaIndex]], combining [[HuggingFace]] embeddings with Google's [[Gemini]] LLM. The guide covers five stages — environment setup, document loading, index creation, query engine configuration, and querying — producing a system that returns context-grounded answers from local PDFs. The author explicitly configures the prompt to avoid hallucination by instructing the model to say "I don't know" when context is insufficient.

## Core Concepts

- **[[LlamaIndex]]**: Python library focused on connecting external data sources to LLMs; provides high-level abstractions for ingestion, indexing, and querying.
- **[[Retrieval-Augmented Generation]] (RAG)**: Pattern where an LLM is augmented with retrieved external context at inference time to reduce hallucination.
- **[[HuggingFace]] Embeddings**: Open-source embedding models configured via `Settings.embed_model` to vectorize document chunks.
- **[[Gemini]] LLM**: Google's generative model, configured via `Settings.llm` as the generation backbone.
- **`SimpleDirectoryReader`**: LlamaIndex utility that ingests PDF files (and other formats) from a local directory into document objects.
- **`SentenceSplitter`**: LlamaIndex chunker; splits documents into overlapping chunks (chunk_size=512, overlap=10) before indexing.
- **`VectorStoreIndex`**: LlamaIndex index type that stores embedded chunk vectors; supports similarity search at query time.
- **`RetrieverQueryEngine`**: Wires a retriever and an LLM together; `similarity_top_k=5` controls how many chunks are retrieved per query.
- **`PromptTemplate`**: Custom prompt structure injecting retrieved context alongside the user question before calling the LLM.
- **Index Persistence**: `index.storage_context.persist()` saves the built index locally so it can be reloaded without re-embedding.

## Key Takeaways

- **Step 1 — Setup**: Install deps; configure `Settings.embed_model` and `Settings.llm`.
- **Step 2 — Load**: Use `SimpleDirectoryReader` to ingest PDFs as document objects.
- **Step 3 — Chunk**: Apply `SentenceSplitter` (512 tokens, 10-token overlap) before indexing.
- **Step 4 — Index**: Build `VectorStoreIndex` and persist to disk for reuse.
- **Step 5 — Query**: Reload index, attach `PromptTemplate`, configure `RetrieverQueryEngine`, call `.query()`.
- **Hallucination guard**: Prompt explicitly instructs model to say "I don't know" when context is absent.
- **Suggested next steps**: Re-ranking, alternative models, and building a UI on top of the query engine.
- **Source code**: Available at GitHub `above-avg/rag-llama`.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: LlamaIndex cleanly separates ingestion (load → chunk → embed → persist) from inference (retrieve → augment → generate), making each stage independently tunable — the same principle that makes modular software easier to debug and extend.
- **[[Garbage In, Garbage Out]]**: Chunk size and overlap directly constrain retrieval quality; a poorly chunked index will surface misaligned context regardless of model sophistication, so the ingestion configuration is as important as model choice.

## 🃏 Review Questions

**Q1**: What is the core purpose of the LlamaIndex RAG pipeline described in this guide?
**A**: To retrieve relevant chunks from local PDF documents and pass them as context to a generative LLM (Gemini), producing grounded answers that avoid fabrication.

**Q2**: What role does `SentenceSplitter` play, and what parameters does the guide use?
**A**: It chunks ingested documents into overlapping segments before indexing; the guide uses chunk_size=512 with an overlap of 10 tokens to balance context continuity and retrieval precision.

**Q3**: How does the guide prevent the model from hallucinating when context is insufficient?
**A**: A custom `PromptTemplate` explicitly instructs the LLM to respond with "I don't know" rather than generating an answer when the retrieved context does not contain the information needed.
