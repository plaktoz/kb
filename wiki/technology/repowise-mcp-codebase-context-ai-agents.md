---
type: literature-note
source_url: https://www.repowise.dev/blog/mcp/codebase-context-for-ai-agents
author: repowise team
tags: [mcp, codebase-context, ai-agents, code-intelligence]
date_consumed: 2026-08-09
---

## Summary

AI coding agents fail in large repositories not because of model size, but because they lack structured context. Repowise addresses this by building a single indexed knowledge layer from a repo's [[AST]], git history, and dependency graph, then exposing it through 10 task-shaped [[MCP]] tools. Benchmarks on django/django showed a 31.6% reduction in output tokens and nearly half the tool calls compared to a bare agent.

## Core Concepts

- **Prompt-Stuffing Failure Modes**: Naive approaches waste tokens, degrade reasoning as context windows fill, and bury useful signals (churn hotspots, ownership data) inside raw text.
- **Indexed Knowledge Layer**: Repowise indexes [[AST]]s, git history, and dependency graphs into a single queryable layer — rather than feeding raw file contents to agents.
- **[[Model Context Protocol]] (MCP) Tools**: Ten task-shaped tools are exposed — `get_overview`, `get_answer`, `get_context`, `get_symbol`, `search_codebase`, `get_risk`, `get_change_risk`, `get_why`, `get_dead_code`, and `get_health`.
- **Staleness Envelope**: Every tool response includes `index_age_days`, `indexed_commit`, and conditional `stale_warning` flags so agents know when cached context diverges from HEAD.
- **Self-Hostable**: Licensed under AGPL-3.0, keeping source code on-premises; supports 16 programming languages.

## Key Takeaways

- **Root cause of agent failure**: Lack of structured context, not model size or intelligence.
- **Three prompt-stuffing failure modes**: Wasteful tokens, degraded reasoning, hidden signals.
- **10 MCP tools**: Cover overview, symbol lookup, search, risk analysis, dead code, and repo health.
- **Benchmark result**: 31.6% fewer output tokens and tool calls dropped from 7.2 to 3.8 (django/django, n=43).
- **Staleness transparency**: Agents are told explicitly when cached index diverges from current HEAD.
- **16 languages supported**: AGPL-3.0 licensed and self-hostable for on-premises deployments.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Repowise decouples context retrieval (structured index) from reasoning (the agent), allowing each layer to specialize — the same principle behind why databases beat file-scanning for query performance.
- **[[Goodhart's Law]]**: Feeding raw files optimizes for "maximum coverage" rather than agent task success, which is why token waste and reasoning degradation emerge — structured, task-shaped tools replace the proxy metric with the actual signal.

## 🃏 Review Questions

**Q1**: Why do AI coding agents fail in large repositories according to repowise?
**A**: Agents fail because they lack structured context — not due to model size — when raw files are stuffed into prompts rather than serving indexed, task-relevant information.

**Q2**: What benchmark evidence does repowise provide, and what did it measure?
**A**: Tested with Codex on django/django (n=43), repowise reduced output tokens by 31.6% and cut tool calls from 7.2 to 3.8 compared to a bare agent control.

**Q3**: How does the staleness envelope help agents working with repowise?
**A**: Each tool response includes `index_age_days`, `indexed_commit`, and conditional `stale_warning` flags, ensuring agents know when the cached index has diverged from the current HEAD commit.
