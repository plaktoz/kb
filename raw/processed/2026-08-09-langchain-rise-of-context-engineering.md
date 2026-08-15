# The Rise of "Context Engineering"

**Author:** Harrison Chase
**Date:** June 23, 2025
**Source:** https://blog.langchain.com/the-rise-of-context-engineering

---

## Definition

Context engineering is building dynamic systems to provide the right information and tools in the right format so an LLM can plausibly accomplish a task.

---

## Core Components

**It's a system** — Context flows from multiple sources: developers, users, prior interactions, tool calls, and external data.

**It's dynamic** — Context isn't static; the logic assembling the final prompt must adapt to changing inputs.

**Right information** — LLMs can't infer what they aren't given. Missing context leads directly to poor outputs.

**Right tools** — Giving the model tools to look up information or take actions is equally important as the information itself.

**Format matters** — A concise, descriptive message outperforms a raw JSON blob. Tool input parameters also affect LLM usability.

**"Can it plausibly accomplish the task?"** — This question helps separate failures caused by missing context from failures caused by model error.

---

## Why It Matters

LLM failures in agentic systems usually stem from one of two causes:

1. The model itself made an error
2. The model lacked appropriate context

As models improve, cause #2 becomes increasingly dominant.

---

## Context Engineering vs. Prompt Engineering

Prompt engineering focuses on clever phrasing; context engineering focuses on providing complete, structured information. Prompt engineering is considered a *subset* of context engineering — even with all the right data, how you assemble it in the prompt still matters.

---

## Examples

- **Tool use** — Providing agents access to external information sources, with results formatted for LLM readability
- **Short-term memory** — Summarizing long conversations for future context windows
- **Long-term memory** — Fetching user preferences from prior sessions
- **Prompt engineering** — Clearly enumerating behavioral instructions
- **Retrieval** — Dynamically fetching and inserting relevant information before the LLM call

---

## Tooling

- **LangGraph** — Offers full control over what steps run and exactly what enters the LLM, enabling precise context construction
- **LangSmith** — Traces agent calls, showing every step and the exact inputs/outputs to the LLM, making it easier to debug context gaps

---

## Key Takeaway

Context engineering isn't new — agent builders have practiced it for years. The term now captures an increasingly critical skill as AI systems grow more complex. The core insight: "communication is all you need," and getting that communication right requires deliberate, dynamic context construction.
