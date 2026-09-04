---
type: literature-note
source_url: https://every.to/source-code/claude-code-for-product-managers
author: Marcus Moretti
tags: [claude-code, product-management, ai-workflows, solo-operator]
date_consumed: 2026-09-03
---

## Summary

Marcus Moretti, GM of Every's AI writing tool Spiral, describes operating as a solo "two-slice team" — handling code, support, marketing, and product management — entirely enabled by [[Claude Code]]. By offloading execution to Claude, he reduces busywork to the point where creative and strategic thinking reclaim center stage. His conclusion: "product management can now be fun."

## Core Concepts

- **[[Claude Code]]** — an agentic AI coding assistant used here not just for engineering but for the full PM workflow: ticket generation, monitoring, and research.
- **[[Solo Operator Model]]** — a single person covering multiple functional roles (engineering, marketing, support, PM) by leveraging AI as a force multiplier.
- **[[GitHub CLI]] + ticket automation** — Claude generated ~100 detailed tickets from a single roadmap document, each with context, acceptance criteria, and implementation notes.
- **[[MCP (Model Context Protocol)]]** — used via the Arxiv MCP for academic literature surveys; also a product survival criterion (products without MCP support were cancelled from his stack).
- **[[Custom Slash Commands]]** — `/prioritize` to sort backlogs continuously; `/pulse` to deliver analyst-style metric briefings without a traditional dashboard.
- **[[Stylometry]]** — the academic study of writing style, directly informing Spiral's style-transfer feature after a Claude-assisted literature survey.

## Key Takeaways

- **Roadmap → 100 tickets**: One PM-authored roadmap became ~100 detailed GitHub tickets via Claude.
- **No dashboards**: `/pulse` command replaces dashboards with plain-English metric briefings.
- **Bug fix in context**: Fixes happen in the same chat thread where issues surface.
- **Research acceleration**: Arxiv MCP enabled rapid academic literature survey on stylometry.
- **MCP as a survival filter**: Products without MCP integrations were dropped from his stack.
- **SaaS survival thesis**: Unique data ownership + seamless agent integrations = durable product moat.
- **Creative space unlocked**: Eliminating busywork restores PM's capacity for creative thinking.

## 🧠 First Principles & Mental Models

- **[[Leverage Points]]**: Moretti applies leverage at the highest-value bottleneck — strategic thinking — by using Claude to absorb all execution-layer tasks, maximizing output per unit of human attention.
- **[[Constraint Removal]]**: Rather than optimizing within existing constraints (limited headcount), he eliminates the constraint itself by making one person's effective capacity match a multi-person team.

## 🃏 Review Questions

**Q1**: What is Moretti's central argument about Claude Code and product management?
**A**: By delegating nearly all execution tasks (tickets, monitoring, research) to Claude Code, a solo operator can cover a full team's scope and reclaim space for creative thinking.

**Q2**: How does the `/pulse` command replace traditional product dashboards?
**A**: It delivers an analyst-style briefing in plain English — surfacing metrics, grading conversations, and flagging anomalies — within a single command, eliminating the need for separate dashboard tooling.

**Q3**: What implication does this workflow have for SaaS product survival?
**A**: Products that own unique data sources and offer seamless agent/MCP integrations will have durable moats; those lacking MCP support risk being cut from AI-native operators' stacks.
