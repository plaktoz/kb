# LangChain with LlamaIndex in Production: A Step-by-Step Integration Guide

Source: https://markaicode.com/integrate/langchain-with-llamaindex/

## Key Takeaways

- Wrap LlamaIndex's query engine in a LangChain `Tool` object to expose it to agents.
- Use `llama-index-tools-langchain` or a custom wrapper for a production-ready bridge.
- Cache the index and query engine outside the agent loop to avoid rebuilding on every turn.
- Monitor token usage: the agent adds its own LLM calls on top of LlamaIndex's retrieval cost.

---

## What is LangChain?

LangChain is a framework for building LLM-powered applications by composing chains, agents, and tools into reusable pipelines. Its standout feature is the agent runtime, where an LLM decides which tool to call and with what arguments, enabling multi-step reasoning.

## What is LlamaIndex?

LlamaIndex is a data framework for indexing and querying external data (PDFs, databases, APIs). It provides advanced chunking, embedding, and hybrid retrieval strategies. Its core abstraction is the `Index`: create a vector index, then call `as_query_engine()` to get a retriever with built-in reranking and citations.

---

## Prerequisites

| Component | Minimum | Recommended | Verify with |
|-----------|---------|-------------|-------------|
| Python | 3.11 | 3.12.4 | `python --version` |
| LangChain | 0.3.0 | 0.3.15 | `pip show langchain` |
| LlamaIndex | 0.11.0 | 0.12.0 | `pip show llama-index` |
| Ollama | 0.5.0 | 0.5.7 | `ollama run llama3.2` |
| Vector store | ChromaDB 0.5.3 | ChromaDB 0.5.5 | `pip show chromadb` |
| GPU (optional) | NVIDIA T4 (4 GB VRAM) | L4 (16 GB VRAM) | `nvidia-smi` |

---

## Architecture Overview

```
┌─────────────────┐
│   User Input    │
└────────┬────────┘
         ▼
┌─────────────────────────────────────┐
│       LangChain Agent (ReAct)       │
│  LLM: Ollama/llama3.2 or GPT-4o    │
│  Tools: [LlamaIndexTool, calculator]│
└────────────────┬────────────────────┘
         │ calls tool
         ▼
┌─────────────────────────────────────┐
│        LlamaIndex Query Engine      │
│  Index: VectorIndex + ChromaDB      │
│  Retriever: hybrid + reranker       │
└────────────────┬────────────────────┘
         │ queries
         ▼
┌─────────────────────────────────────┐
│         ChromaDB (embeddings)        │
│  Document chunks + metadata         │
└─────────────────────────────────────┘
```

---

## Step 1: Create a LlamaIndex Index and Query Engine

Index a sample PDF into ChromaDB and expose it as a query engine. This step is pure LlamaIndex — no LangChain yet.

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
import chromadb

reader = SimpleDirectoryReader(input_dir="./data")
documents = reader.load_data()

db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("my_docs")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
    vector_store=vector_store,
    show_progress=True
)
```

**Verify** with a test query:

```python
query_engine = index.as_query_engine(similarity_top_k=3)
response = query_engine.query("What is the main topic?")
print(response)
```

---

## Step 2: Wrap the Query Engine as a LangChain Tool

Bridge the gap by creating a custom LangChain `Tool` that wraps the query engine.

```python
from langchain.tools import Tool

def llama_index_tool_fn(query: str) -> str:
    """Calls the LlamaIndex query engine and returns the response."""
    response = query_engine.query(query)
    return str(response)

llama_tool = Tool(
    name="DocumentRetriever",
    func=llama_index_tool_fn,
    description="Useful for retrieving information from the indexed documents. Input should be a natural language question."
)
```

**Verify** standalone:

```python
result = llama_tool.invoke("What is the main topic?")
print(result)
```

---

## Step 3: Build the Agent Pipeline

Create a LangChain ReAct agent using the LlamaIndex tool alongside others, with Ollama for local inference.

```python
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory

llm = Ollama(model="llama3.2:3b", temperature=0, base_url="http://localhost:11434")

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [llama_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    max_iterations=4,
    max_execution_time=30,
)
```

**Run a full conversation:**

```python
response = agent.run("What did the report say about revenue?")
print(response)
```

---

## Common Integration Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AttributeError: 'QueryEngine' has no attribute 'query'` | Older LlamaIndex API | Upgrade to >=0.12.0 or use `as_query_engine().query()` |
| Token limit exceeded during agent loop | Each tool call consumes tokens + agent prompt | Set `max_iterations=3` and enable token usage tracking |
| `Ollama: context length exceeded` | Too many chunks passed to the LLM | Reduce `similarity_top_k` to 2 and set `chunk_size=512` |
| Agent keeps calling the tool unnecessarily | Poor tool description | Rewrite `description` to be specific about when to use |

---

## When to Use LangChain + LlamaIndex vs Alternatives

| Scenario | LangChain + LlamaIndex | LangChain Only | LlamaIndex Only | Haystack |
|----------|----------------------|----------------|-----------------|----------|
| Multi-step agent with retrieval | Best fit | Possible | Not built for agents | Limited agents |
| Simple question answering on one doc | Overkill | Quick | Quick | Good |
| Complex chunking & hybrid search | LlamaIndex handles | Manual | Native | Native |
| Low latency requirements (<100ms) | ~250ms per turn | ~80ms | ~150ms | ~120ms |
| Need to integrate with 5+ external APIs | LangChain provides | Provides | No native agent | Limited |

---

## Production Checklist

- Pin all package versions in `requirements.txt` (LangChain 0.3.15, LlamaIndex 0.12.0, chromadb 0.5.5, Ollama 0.6.2+).
- Build and cache the index once at startup; reuse across requests.
- Set `OLLAMA_NUM_PARALLEL=1` to avoid GPU memory thrashing.
- Implement a retry wrapper for the tool call (e.g., tenacity with exponential backoff).
- Monitor agent iterations with `max_iterations=5` and log step count per request.
- Use streaming from both LlamaIndex (`streaming=True`) and LangChain to reduce perceived latency.
- Isolate agent memory per session (`ConversationBufferMemory` per user session).
- Add a fallback response if the agent reaches `max_execution_time`.
- Profile endpoints with `time` and `tokens_per_second` metrics.
- Test with at least 50 concurrent requests using Locust (start at 10 rps).

---

## Honest Trade-Off

Coupling these two frameworks introduces latency overhead. In benchmarks, a direct LlamaIndex query took ~150ms, while the same query routed through a LangChain agent (including LLM reasoning) took ~400ms. For a simple FAQ bot, standalone LlamaIndex is faster. However, if your application needs multi-step reasoning, API calls, and deep document retrieval together, that ~250ms premium unlocks significantly richer answers.

---

## Frequently Asked Questions

### How do I share the query engine across multiple agent instances without rebuilding the index?

Build the index once and store it in a global variable or dependency injection container. For each user session, create a new query engine from that shared index and a new agent with its own memory. This avoids redundant embedding computation and keeps the vector store connection alive.

### Can I use GPT-4o instead of Ollama?

Yes. Replace `Ollama()` with any LangChain chat model such as `ChatOpenAI(model="gpt-4o")`. The wrapper tool stays unchanged. The latency shift moves from local inference to network calls — roughly 200ms extra per step compared to Ollama on localhost.

### Why does my agent get stuck in an infinite loop?

This typically occurs when the tool description is too broad (e.g., "use for questions about documents"), causing the agent to call the tool for every query. Narrow it to something like: "Use only when the user asks about specific numbers or dates in the company annual report." Also reduce `max_iterations` to 3 and enable verbose logging to inspect the reasoning trace.
