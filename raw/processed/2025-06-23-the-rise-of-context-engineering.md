---
source_url: https://blog.langchain.com/the-rise-of-context-engineering
author: Harrison Chase
date: 2025-06-23
---

# The Rise of "Context Engineering"

## Summary

Harrison Chase introduces "context engineering" as the practice of building dynamic systems that supply the right information, tools, and formatting so an LLM can plausibly complete a task.

## Core Definition

Context engineering is *not* just static prompt writing — it's a dynamic system drawing from multiple sources: developer instructions, user input, prior interactions, tool outputs, and external data.

## Key Components

- **Right information** — LLMs can't infer missing context; "garbage in, garbage out"
- **Right tools** — agents need access to lookup/action tools when inputs alone are insufficient
- **Right format** — a concise error message outperforms a raw JSON blob; tool parameter design matters
- **"Can it plausibly accomplish the task?"** — a useful diagnostic framing

## Why It Matters

Agent failures typically stem from one of two causes:
1. The model itself erred
2. The model lacked appropriate context

As models improve, cause #2 becomes increasingly dominant.

## Relationship to Prompt Engineering

Chase considers prompt engineering a *subset* of context engineering — the difference being that context engineering handles dynamic, multi-source inputs rather than optimizing for a single static input.

## Examples

- Tool use with well-formatted return values
- Short-term memory via conversation summaries
- Long-term memory via fetched user preferences
- Retrieval-augmented prompting

## Tooling

- **LangGraph** enables full control over agent steps and LLM inputs
- **LangSmith** provides tracing to inspect exactly what context was passed to the model

["12 Factor Agents"](https://github.com/humanlayer/12-factor-agents) by Dex Horthy is cited as a related read, covering principles like "own your prompts" and "own your context building."
