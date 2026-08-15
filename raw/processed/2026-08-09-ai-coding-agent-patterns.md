# Building AI Coding Agents — Diff Generation, Context Windows, and Scope Control

**Author:** Mahi Mullapudi
**Date:** April 2026
**Source:** https://tutorialq.com/ai/production/ai-coding-agent-patterns

---

## Overview

AI coding agents require four core subsystems working in concert: codebase indexing, context window assembly, diff generation, and scope control. The article emphasizes that the gap between a simple LLM code call and a production-ready agent is substantial.

---

## 1. Codebase Indexing with Tree-Sitter

Tree-sitter is the recommended parsing foundation — it supports incremental parsing, 100+ languages, and produces concrete syntax trees. The indexing layer runs ahead-of-time (on repo clone or file save) and extracts functions, classes, and imports from each file.

Key outputs from indexing:
- **Symbol extraction** (functions, classes, imports with line/byte ranges)
- **File summaries** — compact one-liners for fast context scanning
- **Dependency graph** — maps which files import which others, enabling "blast radius" analysis when a function changes

---

## 2. Context Window Assembly

Selecting the right context is described as "the hardest problem in coding agents." Even large windows (128K–200K tokens) degrade with irrelevant content — referencing the "Lost in the Middle" research paper.

The selection algorithm:
1. Extract symbols mentioned in the request
2. Expand with 1-hop dependencies
3. Score each file
4. Sort by relevance, pack within token budget

**Relevance scoring signals:**

| Signal | Weight |
|---|---|
| Direct mention | 1.0 |
| 1-hop dependency | 0.7 |
| 2-hop dependency | 0.3 |
| Recency | 0.5 |
| Embedding similarity | 0.6 |

---

## 3. Diff Generation Strategies

Three strategies with distinct trade-offs:

| Strategy | Reliability | Token Cost | Best For |
|---|---|---|---|
| Unified diff | Medium | Low | Small, precise edits |
| Search-and-replace | High | Low | Single-point changes |
| Full-file rewrite | Highest | High | Large restructurings |

Search-and-replace is recommended for production because it avoids unified diff fragility. The implementation validates that the search string appears exactly once — if it matches multiple locations, it requests more context lines for a unique match.

---

## 4. Scope Control

Without guardrails, agents will edit unrelated files including CI pipelines and config. Two approaches:

- **Allowed-file lists** — blocklist includes `.env`, lock files, `.github/workflows`; validate against explicit patterns before applying any edit
- **Scope inference** — better agents derive scope automatically from the request, including files that import mentioned files (since they may need updates too)

---

## 5. Error Recovery

LLMs produce invalid code roughly 10–20% of the time on complex edits. The recovery loop:
1. Apply edits
2. Validate syntax (using Python's `compile()` without execution)
3. If errors exist, send the broken code + error messages back to the LLM for self-correction
4. Retry up to a configurable maximum

---

## Full Pipeline Summary

`User Request → Index Load → Context Assembly → Scope Inference → Prompt Build → LLM Generate → Parse Edits → Scope Check → Apply with Recovery`

---

## References

- [Tree-sitter documentation](https://tree-sitter.github.io/tree-sitter/)
- [OpenAI function calling](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Claude tool use](https://docs.anthropic.com/en/docs/tool-use)
- ["Lost in the Middle" paper](https://arxiv.org/abs/2307.03172)
