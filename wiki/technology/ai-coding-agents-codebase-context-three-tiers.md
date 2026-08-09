---
type: literature-note
source_url: https://dev.to/corestory/how-to-give-ai-coding-agents-better-codebase-context-2ac3
author: Michel Ozzello
tags: [ai-agents, codebase-context, rag, code-intelligence]
date_consumed: 2026-08-09
---

## Summary

AI coding agents fail on large codebases not because of model intelligence limits, but because of inadequate context infrastructure. The author proposes three tiers of context solutions — static files, RAG-based retrieval, and persistent code intelligence models — matched to codebase scale. Teams should select the tier appropriate to their repository size rather than defaulting to a one-size-fits-all approach.

## Core Concepts

- **Static Context Files (Tier 1)**: Manually authored markdown files such as `AGENTS.md`, `.cursorrules`, and [[CLAUDE.md]] that agents read before beginning work. Portable and low-cost, but they drift over time and lack architectural depth. An ETH Zurich study found LLM-generated versions *reduced* task success rates while raising inference costs.
- **[[RAG]]-Based Retrieval (Tier 2)**: Systems like [[Sourcegraph Cody]], [[Continue.dev]], and [[Windsurf]] that dynamically index a codebase and retrieve relevant chunks at query time. More scalable than static files, but retrieve raw code rather than understanding it — missing call graphs, data flows, and architectural reasoning.
- **Code Intelligence Models (CIMs) (Tier 3)**: Platforms that build queryable knowledge graphs by analyzing [[AST]]s, call graphs, and business logic. Delivered via [[MCP]] servers, they provide agents with "structured specifications" rather than raw snippets. CoreStory's system applied to a production COBOL codebase yielded nearly 2,000 business specs at an 85%+ validation rate.
- **[[Context Engineering]]**: The broader discipline of providing agents with the right information in the right form — the root cause of agent failure on large codebases is context infrastructure, not model capability.

## Key Takeaways

- **Root cause**: Agent failures on large codebases stem from context infrastructure, not model intelligence.
- **Tier 1 – Static Files**: Best for codebases under 100K lines; low cost, but drifts over time.
- **Tier 2 – RAG**: Best for multi-repo needs; retrieves code snippets, misses architectural reasoning.
- **Tier 3 – CIMs**: Best for 500K+ line enterprise systems or modernization projects.
- **ETH Zurich finding**: LLM-generated static context files reduced task success rates vs. none.
- **CIM validation rate**: CoreStory achieved 85%+ spec validation on a COBOL legacy system.
- **Tiers are complementary**: AGENTS.md + RAG + CIMs can be layered as scale demands increase.

## 🧠 First Principles & Mental Models

- **[[Right Tool for the Job]]**: Each tier solves a different scale problem — applying Tier 3 overhead to a small codebase wastes cost, while using only Tier 1 on an enterprise system guarantees agent failure. Matching solution complexity to problem scale is the core engineering principle here.
- **[[Goodhart's Law]]**: LLM-generated static context files optimized for "covering the codebase" rather than helping agents succeed, which is why the ETH Zurich study found they hurt performance — a proxy metric replaced the actual goal.

## 🃏 Review Questions

**Q1**: What is the primary reason AI coding agents fail on large codebases, according to the article?
**A**: The failure is due to inadequate context infrastructure, not limitations in model intelligence — agents lack the structured understanding of the codebase needed to act correctly.

**Q2**: What distinguishes Tier 3 Code Intelligence Models from Tier 2 RAG systems?
**A**: CIMs build queryable knowledge graphs from ASTs and call graphs, delivering structured business specifications via MCP servers, whereas RAG systems retrieve raw code chunks without capturing architectural reasoning or data flows.

**Q3**: How should a team decide which tier of context infrastructure to adopt?
**A**: Match the tier to codebase scale: static files for under 100K lines, RAG for multi-repo needs, and CIMs for 500K+ line enterprise systems or modernization efforts — the tiers are also complementary and can be layered.
