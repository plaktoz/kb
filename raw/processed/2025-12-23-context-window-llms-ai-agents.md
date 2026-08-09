---
source_url: https://comet.com/site/blog/context-window/
author: Kelsey Kinzer
date: 2025-12-23
---

# Context Window in LLMs: What It Is and Why It Matters for AI Agents

## What Is a Context Window?

A context window is the total information an LLM can hold and reference while generating a response — essentially the model's working memory. Once full, earlier information gets silently dropped.

A context window contains:
- System instructions
- User input and conversation history
- Tool outputs and retrieved documents
- Intermediate results

Tokens are text chunks roughly equal to "four characters or three-fourths of a word." A 100K-token window holds approximately 75,000 words (~250 pages).

### Model Reference

| Model | Context Window |
|-------|---------------|
| GPT-5.1 Thinking | 196K tokens |
| Claude 4.5 Sonnet | 200K tokens |
| Gemini 3 | 1M tokens |

---

## Why It Matters for Agents

Simple LLM apps have predictable, bounded context usage. Agentic workflows are different — context accumulates across every LLM call. A 50-step workflow at 20K tokens per call equals 1 million tokens total. When the window fills, the agent loses critical earlier information mid-workflow.

---

## Common Failure Modes

**1. Silent Degradation** — Agents don't always error out; they continue with incomplete context, producing plausible but wrong results.

**2. Attention Dilution ("Lost in the Middle")** — Research shows LLMs perform better with information at the start or end of context. A 1M-token window doesn't function as 1M tokens of perfect memory.

**3. Inconsistent Behavior** — Workflows that pass short-input tests can break unpredictably with longer real-world inputs.

**4. Cascading Failures** — Dropped early results cause later steps to branch incorrectly, compounding errors across the workflow.

---

## Strategies for Managing Context

### Understand Your Token Budget
Account for all context sources: system prompts (500–2,000 tokens), user input, tool outputs, conversation history, and retrieved documents. Design for worst-case production scenarios, not average test cases.

### Design Workflows to Need Less Context
- Break long workflows into stages with summarization checkpoints
- Compress tool outputs before injecting them (e.g., summarize 100 DB rows to top 5)
- Use semantic caching for repeated retrieval queries
- **Always preserve:** original user intent and recent tool results
- **Compress or drop:** older intermediate results and prior reasoning chains

### Choose the Right Architecture

| Use Long Context When... | Use RAG + Smaller Context When... |
|--------------------------|-----------------------------------|
| Cross-step detail reference is critical | Searching large knowledge bases |
| Relationships between distant info matter | Cost optimization is a priority |
| Full dataset must be "in memory" | Data updates frequently |

Rolling/sliding window approaches work well for long-running conversational agents.

### Monitor Token Usage
Track these metrics:
- Token consumption per workflow step
- Proximity to context limits (regularly hitting 80%+ signals risk)
- Performance degradation as context grows
- Cost per workflow execution broken down by type

---

## Key Takeaways

- Context windows are the LLM's working memory — filling them causes silent information loss
- Agents burn context fast across multi-step workflows
- Failures are often invisible until production
- "Context engineering" — intentional management of what stays in memory — beats simply maximizing context size
- Observability tooling is essential to see what's actually in context at each decision point
