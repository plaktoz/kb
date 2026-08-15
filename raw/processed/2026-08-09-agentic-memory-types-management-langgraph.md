# Agentic Memory: Types, Management Strategies, and LangGraph Implementation

**Source:** https://www.patronus.ai/ai-agent-development/agentic-memory
**Publisher:** Patronus AI — Chapter 9 of AI Agent Development Series

---

## Overview

Agentic memory lets AI agents store, recall, and use information persistently across interactions by injecting relevant memories into the LLM's context window at inference time. Without it, every LLM call starts fresh — no continuity, no personalization.

---

## Key Memory Types

### Short-Term Memory
Temporary, session-scoped context held in the LLM's context window. Cleared when the session ends. Main challenge: finite token limits require truncation or summarization.

### Long-Term Memory
Persistent storage surviving across sessions, with three sub-types:

| Type | Description | Example |
|------|-------------|---------|
| **Semantic** | Structured facts, preferences, entity relationships | "User prefers concise answers" |
| **Episodic** | Timestamped logs of past events and outcomes | Prior tool failures/successes |
| **Procedural** | Learned skills and behavioral patterns | Auto-include code examples |

---

## How Agentic Memory Differs from Traditional Chatbot Memory

Traditional chatbot memory injects raw conversation history into prompts. Agentic memory is fundamentally different:

- **Storage:** Structured knowledge (facts, preferences) vs. raw message logs
- **Persistence:** Cross-session vs. single-session only
- **Control:** Agent decides what to store/discard vs. fixed developer-configured buffers
- **Recall:** Semantic retrieval of relevant entries vs. full history injection
- **Contradiction handling:** Agent can overwrite outdated facts; traditional systems cannot

---

## Memory Management Strategies

1. **Sliding Window** — Keep only the most recent N messages; simple but risks losing early context
2. **Conversation Summarization** — Compress older history into concise summaries
3. **Fact Extraction** — Pull structured records (e.g., "User prefers Python") from conversations
4. **Retrieval-Augmented Recall** — Store chunks in a vector/knowledge store; retrieve only relevant memories per turn
5. **Hybrid Approaches** — Combine sliding window + summarization + retrieval for production systems

---

## LangGraph Implementation Summary

The article demonstrates a memory-enabled HR assistant RAG agent using:

- **`MemorySaver` checkpointer** for short-term, within-thread memory
- **`InMemoryStore`** for long-term, cross-thread memory

### Three Memory Tools Defined:

```python
@tool
def save_memory(key: str, value: str) -> str:
    """Save or update a piece of information in long-term memory."""
    store.put(("memory",), key, {"content": value})
    return f"Saved to memory: {key} = {value}"

@tool
def recall_memories() -> str:
    """Retrieve all stored memories."""
    memories = store.search(("memory",))
    ...

@tool
def delete_memory(key: str) -> str:
    """Delete a specific memory entry."""
    store.delete(("memory",), key)
```

### Agent System Prompt Pattern:
The agent is instructed to: (1) recall memories first, (2) search policies with that context, (3) save new facts after answering, (4) handle corrections by overwriting existing keys.

---

## Key Behaviors Demonstrated

- **Short-term:** Follow-up questions resolved without re-asking user details within a thread
- **Long-term:** Facts saved in one thread recalled in a completely separate thread
- **Updates:** Calling `save_memory` with an existing key overwrites stale data
- **Deletion:** Targeted removal of specific keys without affecting other stored memories

---

## Best Practices

- Scope memory by user/application using namespaces
- Manage context window token budgets; prioritize relevant memories
- Choose hot-path vs. background writes based on latency requirements
- Implement memory hygiene: deduplicate, consolidate, prune periodically
- Add observability to all memory operations (read, write, update, delete)
- Secure PII and sensitive data with access controls and retention policies

---

## Observability with Patronus AI

The article integrates Patronus AI tracing via `@patronus.traced()` decorator and the `LangChainInstrumentor`. This surfaces the full agent trace — every tool call, memory read/write, and retrieval step — in the Patronus dashboard. The **Percival AI debugger** analyzes traces to detect issues like stale memory recalls or missed memory saves.

---

*Full code available on [GitHub](https://github.com/usmanmalik57/patronus-articles/tree/main/agentic_memory)*
