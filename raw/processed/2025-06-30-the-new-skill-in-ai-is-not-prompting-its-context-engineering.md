---
source_url: https://philschmid.de/context-engineering
author: Philipp Schmid
date: 2025-06-30
---

# The New Skill in AI is Not Prompting, It's Context Engineering

## Summary

The AI field is moving beyond prompt engineering toward **Context Engineering** — designing dynamic systems that supply an LLM with the right information, tools, and format at the right moment.

## What Is "Context"?

Context is everything the model sees before generating a response:

- **System Prompt** – behavioral instructions, rules, examples
- **User Prompt** – the immediate request
- **Short-term Memory** – current conversation history
- **Long-term Memory** – persistent knowledge across sessions
- **Retrieved Info (RAG)** – external documents, databases, APIs
- **Available Tools** – callable functions (e.g., `send_email`)
- **Structured Output** – response format definitions

## Why It Matters

The author contrasts two agents given the same vague email: *"just checking if you're around for a quick sync tomorrow."*

A poorly-contextualized agent produces a generic, robotic reply. A well-contextualized agent — armed with calendar data, email history, contact info, and relevant tools — produces something human and actionable.

The core argument: **most agent failures are context failures, not model failures.**

## Defining Context Engineering

> "The discipline of designing and building dynamic systems that provides the right information and tools, in the right format, at the right time."

Key properties:
- It's a **system**, not a static string
- It's **dynamic**, tailored per request
- It prioritizes **relevant** information over raw data dumps
- **Format matters** — concise summaries beat data dumps

## Conclusion

Building reliable agents is less about clever code or frameworks and more about engineering the context window thoughtfully — a cross-functional challenge requiring business understanding, output definition, and careful information structuring.
