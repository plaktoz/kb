---
source_url: https://docs.typesafe.ai/concepts/system-one
author: Unknown
date: 2026-09-26
---

# System One — TypeSafe AI

System One models deliver fast, structured, typed decisions for software rather than generating free-form text.

## Core Concept

**Jev** is TypeSafe's flagship System One model. It accepts natural-language input and returns "typed decisions and probabilities rather than generated text."

> Currently accepts text input only (strings, JSON objects, arrays). No images, audio, or video support yet.

## Primitives

| Primitive | Purpose | Output Example |
|-----------|---------|----------------|
| **Choice** | Classify into categories | `"billing"` |
| **Score** | Numeric rating | `1.4` |
| **Noul** | True/false probability | `0.95` |

## Key Differences from LLMs

- Probabilities are "optimized against outcomes to reflect uncertainty"
- No replies, code generation, or reasoning explanations
- Outputs are typed and constrained — predictable for programmatic use

## Typical Workflow

1. Build a state with relevant context
2. Ask multiple independent questions simultaneously
3. Combine typed answers with deterministic code logic
4. Route based on results + confidence scores

## Naming

The name references Kahneman's *Thinking, Fast and Slow* — "System 1 thinking is fast and intuitive."

## Access

Call via client SDKs or `POST /v1/systemone`. Default model: `jev-latest`.
