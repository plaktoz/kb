---
source_url: https://docs.typesafe.ai/
author: Unknown
date: 2026-09-26
---

# Introduction — TypeSafe AI (Jev)

## Overview

Jev is TypeSafe's flagship "System One model" — designed for fast, structured decisions that software can consume directly, rather than generating human-readable text.

The core problem it solves: standard LLMs produce text that must be parsed back into structured data. Jev instead evaluates typed *questions* against a *state*, returning typed values, probability distributions, and confidence scores your code can act on immediately.

## The Three Primitives

| Type | Purpose | Output |
|------|---------|--------|
| **Choice** | Select from a list | `choice`, `probabilities`, `confidence` |
| **Score** | Rate against a rubric | `score`, `probabilities`, `confidence` |
| **Noul** | True/false statement | `noul` (0–1) |

All three can be mixed in one API call, evaluated **in parallel and in isolation** against the same state. Key benefit: adding questions has minimal latency impact and avoids "context-rot."

## Design Philosophy

Questions should be atomic and well-scoped — think gut-check judgments a knowledgeable person could make in seconds. Complex multi-factor questions should be decomposed into separate questions, then combined with logic in your own code.

Example: rather than "rate this startup pitch," ask separately about market size, technical feasibility, and differentiation, then combine scores with a custom formula.

> "When priorities shift, change a coefficient in your code rather than rewriting a prompt."
