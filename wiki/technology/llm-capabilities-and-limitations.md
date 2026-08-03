# LLM Capabilities and Limitations

**Source:** [Lesson 3B: Capabilities & Limitations — AI Fluency: Framework & Foundations](https://www.youtube.com/watch?v=W5cga7xipRI)
**Author:** Anthropic (Prof. Rick Dakan, Prof. Joseph Feller)

---

## What LLMs Do Well

Modern language models are remarkably versatile across language tasks:

- **Writing & editing** — drafting emails, condensing reports into summaries, explaining complex topics across domains
- **Translation** — across languages, registers, and technical fields
- **Task flexibility** — the same model can write poetry, brainstorm party ideas, explain quantum computing, and analyze business trends — all without retraining
- **Conversational memory** — within a session, models can track context across a conversation and refer back to earlier points
- **Tool access** — many modern LLMs can connect to external tools (web search, file processing, APIs) to extend beyond their training knowledge

The shift between tasks happens fluidly through natural conversation, which is a core differentiator from earlier AI systems.

---

## Key Limitations

### 1. Knowledge Cutoff
LLMs have a **hard cutoff date** — they have no innate knowledge of events after training ended. Like someone who went offline at a specific date, the model cannot know what happened afterward without external tools (e.g., web search or [[what-is-retrieval-augmented-generation-rag|RAG]]).

### 2. Hallucinations
Training does not verify every fact in the training corpus. LLMs can:
- Reproduce inaccuracies present in training data
- Generate plausible-sounding but incorrect statements when patching together learned patterns

This is called **hallucination** — the model states something with confidence that is factually wrong. Unlike a search engine that retrieves existing documents, an LLM generates based on statistical patterns, making confident errors possible.

### 3. Context Window Limits
Every LLM has a maximum **context window** — the amount of information it can process in a single interaction. When the limit is exceeded, information falling outside the window is dropped (typically on a first-in, first-out basis). This constrains processing of large documents or very long conversations. See also: [[a-guide-to-context-engineering-for-llms]].

### 4. Non-Determinism
Unlike traditional software, LLMs are **non-deterministic** by default. The same prompt can yield slightly different answers each time, because the model makes probabilistic choices about the next token based on learned patterns. This is governed by the **temperature** setting:
- High temperature → more creative/varied output
- Low temperature → more predictable/consistent output

Non-determinism is useful for creative tasks but requires awareness when accuracy or reproducibility is critical.

### 5. Reasoning Limitations
Historically, LLMs have struggled with **multi-step mathematical or logical reasoning**. Newer **reasoning models** (also called extended thinking models) are specifically designed to think step-by-step and are showing strong progress, but limitations remain.

### 6. Tool & Data Access Gaps
Even capable models are limited by what they can access. A model without access to a company's internal database cannot help with tasks requiring it — no matter how intelligent it is. Tool access must be explicitly provided.

---

## The Evolving Landscape

Active research is addressing current limitations:

| Limitation | Mitigation in progress |
|---|---|
| Knowledge cutoff | [[what-is-retrieval-augmented-generation-rag\|RAG]] — connects models to external knowledge sources |
| Reasoning | Reasoning/extended thinking models trained to think step-by-step |
| Tool access | Expanding tool-use frameworks (function calling, MCP) |

Some limitations will likely persist for the foreseeable future, even if their exact shape changes.

---

## Human–AI Complementarity

The most effective applications pair human and AI strengths:

| Humans bring | AI brings |
|---|---|
| Critical thinking & judgment | Speed and scale |
| Creativity and ethical oversight | Pattern recognition across vast data |
| Contextual wisdom | Consistent availability and breadth |

Understanding both sides of this pairing — AI fluency — is essential for deciding when and how to incorporate AI effectively into work and daily life.

---

## Related Notes
- [[generative-ai-llm-foundations-how-it-works]]
- [[what-is-retrieval-augmented-generation-rag]]
- [[is-rag-still-needed-long-context-vs-rag]]
- [[a-guide-to-context-engineering-for-llms]]
- [[ai-response-correctness-evaluation-frameworks]]
