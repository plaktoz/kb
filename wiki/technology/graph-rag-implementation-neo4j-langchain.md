---
type: literature-note
source_url: https://www.langchain.com/blog/enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs
author: Tomaz Bratanic (Neo4j), The LangChain Team
tags: [rag, knowledge-graphs, neo4j, langchain]
date_consumed: 2026-08-03
---

## Summary

Graph RAG extends traditional [[RAG]] by combining graph traversal with vector and keyword search, enabling richer retrieval from structured, interconnected data. This post demonstrates using [[LangChain]]'s `LLMGraphTransformer` and [[Neo4j]] to automatically extract a knowledge graph from text and query it via a hybrid retrieval pipeline. The hybrid approach provides both structured precision (graph relationships) and semantic flexibility (vector similarity) in a single chain.

## Core Concepts

- **[[Graph RAG]]**: A retrieval strategy that traverses entity relationships in a graph database alongside vector and keyword search, capturing structured connections that embeddings alone cannot.
- **[[LLMGraphTransformer]]**: A LangChain utility that uses an LLM to automatically identify entities and relationships from raw text and store them as graph documents in [[Neo4j]].
- **[[Neo4j]]**: A graph database that supports all three retrieval modes (vector search, full-text keyword index, Cypher-based graph traversal) in one backend.
- **[[Hybrid Retrieval]]**: Concatenating results from structured graph traversal and unstructured vector/keyword search before passing them as context to the LLM.
- **[[Cypher Query Language]]**: The query language used to traverse graph neighborhoods — e.g. fetching up to 50 direct relationships from an entity node.
- **[[Query Rewriting]]**: A conversational enhancement that rewrites ambiguous follow-up questions (e.g. "When was she born?") into fully-specified queries before retrieval.
- **[[Entity Extraction]]**: Structured output (Pydantic model) used to detect named entities in the user's question, which are then matched to graph nodes via a fuzzy full-text index.

## Key Takeaways

- **Graph database stores nodes + relationships**, unlike vector DBs which only store embeddings.
- **`LLMGraphTransformer`** automates knowledge graph construction from unstructured text.
- **Three retrieval modes in Neo4j**: vector search, keyword/full-text, graph traversal — all combined.
- **`baseEntityLabel=True`** adds `__Entity__` label for efficient node indexing.
- **`include_source=True`** preserves links from graph nodes back to source documents.
- **Fuzzy entity matching** (~2-character tolerance) bridges free-text questions to graph nodes.
- **Query rewriting** maintains conversational coherence across multi-turn sessions.
- **Supports only OpenAI and Mistral** function-calling models for graph generation (at time of writing).

## 🧠 First Principles & Mental Models

- **[[Complementary Strengths]]**: Vector search handles semantic vagueness; graph traversal handles structured relationships — combining them addresses each other's blind spots rather than replacing one with the other.
- **[[Locality of Reference]]**: Graph neighborhood retrieval exploits the principle that answers live near the queried entity in relational space, just as spatial locality speeds up cache hits in computing.

## 🃏 Review Questions

**Q1**: What is the core claim of Graph RAG over standard vector-based RAG?
**A**: Graph RAG adds a graph traversal layer that captures structured entity relationships (e.g. "Elizabeth I - CHILD_OF -> Henry VIII"), which vector similarity search cannot represent, yielding more precise contextual retrieval.

**Q2**: How does `LLMGraphTransformer` build the knowledge graph, and what models does it support?
**A**: It uses an LLM to extract entities and relationships from document chunks and stores them as graph documents in Neo4j; at the time of writing it only supports OpenAI and Mistral function-calling models.

**Q3**: How would you apply this hybrid pipeline to a domain-specific knowledge base?
**A**: Load and chunk your domain documents, run them through `LLMGraphTransformer` to populate a Neo4j graph, then wire up the combined retriever (vector + keyword + graph traversal) so the RAG chain can draw on both unstructured similarity and structured entity relationships.
