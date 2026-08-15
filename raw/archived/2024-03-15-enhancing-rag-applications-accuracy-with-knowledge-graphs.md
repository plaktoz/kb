---
source_url: https://www.langchain.com/blog/enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs
author: Tomaz Bratanic (Neo4j), The LangChain Team
date: 2024-03-15
---

# Enhancing RAG-based Application Accuracy by Constructing and Leveraging Knowledge Graphs

## Overview

Graph RAG is emerging as a powerful complement to traditional vector search. Graph databases organize data as nodes and relationships, enabling richer, more contextual retrieval than vector databases alone — which excel at unstructured data but struggle with structured, interconnected information.

This post demonstrates combining structured graph retrieval with vector/keyword search in a single RAG pipeline using **Neo4j** and **LangChain**.

## Knowledge Graph Construction

The hardest part of Graph RAG is building the graph. LangChain's `LLMGraphTransformer` automates this by using LLMs to identify entities and relationships from text.

**Setup:** A Neo4j instance (local or Aura cloud) plus an OpenAI API key.

**Data ingestion:** Elizabeth I's Wikipedia page is loaded and chunked:

```python
raw_documents = WikipediaLoader(query="Elizabeth I").load()
text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=24)
documents = text_splitter.split_documents(raw_documents[:3])
```

**Graph generation:**

```python
llm = ChatOpenAI(temperature=0, model_name="gpt-4-0125-preview")
llm_transformer = LLMGraphTransformer(llm=llm)
graph_documents = llm_transformer.convert_to_graph_documents(documents)
graph.add_graph_documents(graph_documents, baseEntityLabel=True, include_source=True)
```

- `baseEntityLabel=True` — adds `__Entity__` label for better indexing
- `include_source=True` — links nodes back to source documents
- Currently supports only OpenAI and Mistral function-calling models

## Hybrid Retrieval Architecture

The retrieval layer combines three approaches:

1. **Vector search** — semantic similarity over document text
2. **Keyword search** — full-text index matching
3. **Graph traversal** — neighborhood exploration of relevant entities

All three are implemented within Neo4j.

### Unstructured Data Retriever

```python
vector_index = Neo4jVector.from_existing_graph(
    OpenAIEmbeddings(),
    search_type="hybrid",
    node_label="Document",
    text_node_properties=["text"],
    embedding_node_property="embedding"
)
```

### Graph Retriever

Entities are extracted from the user's question using structured output:

```python
class Entities(BaseModel):
    names: List[str] = Field(..., description="All person, organization, or business entities...")
```

A full-text index maps detected entities to graph nodes (with fuzzy ~2-character tolerance), then a Cypher query retrieves their direct neighborhood (up to 50 relationships).

**Example output:**
```
Elizabeth I - BORN_ON -> 7 September 1533
Elizabeth I - MEMBER_OF -> House Of Tudor
Elizabeth I - CHILD_OF -> Henry Viii
```

### Combined Retriever

Both structured (graph) and unstructured (vector/keyword) results are concatenated and passed as context to the LLM.

## RAG Chain

A prompt template wraps the combined context, and the chain supports **query rewriting** for conversational follow-ups:

- Question: *"When was she born?"*
- Rewritten to: *"When was Elizabeth I born?"*
- Answer: *"Elizabeth I was born on 7 September 1533."*

## Summary

The `LLMGraphTransformer` lowers the barrier to knowledge graph creation, making Graph RAG more accessible. The hybrid approach — graph traversal plus vector/keyword search — provides both structured precision and semantic flexibility.

Full code available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/llm/enhancing_rag_with_graph.ipynb).
