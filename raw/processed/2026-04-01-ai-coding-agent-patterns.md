---
source_url: https://tutorialq.com/ai/production/ai-coding-agent-patterns
author: Mahi Mullapudi
date: 2026-04-01
---

# Building AI Coding Agents — Diff Generation, Context Windows, and Scope Control

The article examines four core subsystems required for production AI coding agents: codebase indexing, context window assembly, diff generation, and scope control.

## Codebase Indexing

Tree-sitter is recommended as the standard parsing library, providing incremental parsing across 100+ languages. The indexing layer extracts functions, classes, and imports into structured symbol tables, then builds file-level summaries and a dependency graph tracking inter-file import relationships.

## Context Window Assembly

The central challenge is selecting relevant context within token budget constraints. The article warns about the "lost in the middle" degradation effect, where irrelevant content harms LLM performance even within large windows. A relevance scoring approach combines multiple signals:

| Signal | Weight |
|---|---|
| Direct mention | 1.0 |
| 1-hop dependency | 0.7 |
| 2-hop dependency | 0.3 |
| Recency | 0.5 |
| Embedding similarity | 0.6 |

## Diff Generation

Three strategies are compared:

- **Unified diff** — low token cost, but LLMs occasionally produce invalid hunks
- **Search-and-replace** — described as "the most reliable for production agents" due to avoiding diff fragility
- **Full-file rewrite** — highest reliability, highest token cost; best for major restructuring

## Scope Control

A `ScopeGuard` pattern checks edits against blocklists (e.g., `.env`, lock files, CI workflows) before application. More sophisticated agents infer allowed scope from the request itself rather than requiring explicit allowlists.

## Error Recovery

LLMs produce invalid code roughly 10–20% of the time on complex edits. The proposed solution is a retry loop: validate syntax after applying edits, then prompt the LLM to fix its own errors, up to a configurable maximum attempt count.
