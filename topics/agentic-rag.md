---
type: topic-file
topic: agentic-rag
sources: [rag-graphrag-context-engineering-ai-performance, rag-evolution-simple-retrieval-to-agentic-ai, what-is-agentic-rag, what-is-retrieval-augmented-generation-rag]
last_updated: 2026-08-01
---

# Agentic RAG

Agentic RAG is the current frontier of retrieval-augmented generation — the point in the evolution of AI information systems where the retrieval decision itself moves from static pipeline logic to dynamic LLM judgment, making the model both the generator and the orchestrator of what gets retrieved, when, and from where.

## RAG as the Foundation

[[what-is-retrieval-augmented-generation-rag]] establishes the problem RAG solves: language models encode knowledge in their parameters at training time, making their factual knowledge frozen, uncitable, and prone to hallucination when queried beyond their training distribution. RAG addresses this by externalizing factual memory into a mutable content store — documents, policies, real-time feeds — that the model consults at inference time before generating a response. The retriever fetches the most relevant context, it is injected into the prompt alongside the user's question, and the generator produces an answer grounded in that context. The architectural insight is clean: separate mutable factual memory from durable reasoning capability, so the former can be updated without retraining the latter. The binding constraint, however, is retriever quality — a weak retriever that surfaces irrelevant or outdated context degrades answer quality regardless of how capable the generative model is, making retrieval improvement as important as model scaling.

## The Evolution from Keyword Retrieval to Agentic Systems

[[rag-evolution-simple-retrieval-to-agentic-ai]] traces a five-stage progression that reframes agentic RAG as an incremental maturation rather than a discontinuous break. Keyword retrieval (TF-IDF and BM25) matches query terms to document tokens — high precision for exact matches, blind to synonymy and conceptual relationships. Semantic retrieval introduced vector embeddings that capture meaning over exact wording, enabling query-by-concept rather than query-by-keyword. Standard RAG combined offline embedding (encode documents into a vector database at index time) with online retrieval (query the database at inference time). Advanced RAG added a layer of pipeline sophistication — rerankers to re-score retrieved chunks by relevance, query rewriting to reformulate ambiguous queries before retrieval, and hybrid search combining sparse and dense signals. Agentic RAG is the fifth stage: the LLM itself decides what to retrieve, when in the reasoning chain to retrieve it, and from which of multiple knowledge sources — converting a static pipeline into a dynamic, self-directing retrieval process. As [[rag-evolution-simple-retrieval-to-agentic-ai]] states it, "the hardest problem is not generation but deciding what to look at."

## The LLM as Retrieval Orchestrator

[[what-is-agentic-rag]] makes the structural shift precise: traditional RAG calls the LLM exactly once, for generation. Agentic RAG promotes the LLM to active decision-maker across the entire pipeline — it interprets query semantics to select the right knowledge base from multiple available sources, determines the appropriate output format (prose, chart, code), and routes out-of-scope queries to a failsafe response rather than hallucinating. The key mechanism is intelligent agent routing: the agent uses language understanding to distinguish between, for instance, an internal policy question (route to internal documentation) versus a technical standards question (route to public standards database), without hard-coded conditional logic. This delegation principle mirrors organizational management — routing context-dependent decisions to the actor with the most situational awareness of the specific query. Failsafe routing handles the edge case: when a query falls outside all available knowledge bases, the agent detects the mismatch and returns a graceful abstention rather than confabulating.

## Context Engineering as the Discipline

[[rag-graphrag-context-engineering-ai-performance]] reframes the retrieval problem at a higher level of abstraction: the limiting factor in AI system performance is not model reasoning capability but context quality. A contextually intelligent system built on a less powerful model routinely outperforms a more powerful model operating on poor context — meaning that context architecture is now a first-order engineering concern. The discipline of context engineering involves four pillars: connected access (maintaining traversable relationships between knowledge artifacts, not treating them as isolated documents), the knowledge layer (structured semantic metadata above raw text), precision retrieval (the ability to retrieve exactly the right context and compress it to what the model needs), and runtime governance (controlling what context each request can access based on scope and authorization). This framing explains why two organizations deploying the same base model can achieve radically different output quality — the gap is context architecture, not model selection.

## Advanced Retrieval Architectures

[[rag-graphrag-context-engineering-ai-performance]] introduces GraphRAG as the solution to a fundamental limitation of vector-based retrieval: vector similarity captures semantic proximity but is blind to relationship structure. For queries whose answers require traversing relationships ("what decisions led to this outcome?", "how does concept A connect to concept B?") rather than finding conceptually similar content, GraphRAG's knowledge graph substrate enables relationship-aware retrieval that flat vector retrieval cannot replicate. Zero Copy Federation extends the architecture further — enabling the retrieval layer to query multiple distributed knowledge sources without consolidating them into a single index, preserving source ownership and reducing synchronization overhead. Runtime Governance addresses the authorization layer: as agentic systems gain access to heterogeneous knowledge bases spanning internal and external sources, controlling which context each request can access — and logging what was retrieved for each response — becomes a production safety requirement, not an afterthought.

## Weekly Updates

### 2026-W31
- Added: [[rag-graphrag-context-engineering-ai-performance]], [[rag-evolution-simple-retrieval-to-agentic-ai]], [[what-is-agentic-rag]], [[what-is-retrieval-augmented-generation-rag]]
