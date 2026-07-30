---
type: literature-note
source_url: https://blog.bytebytego.com/p/ep209-12-claude-code-features-every
author: Unknown
tags: [claude-code, agentic-rag, rest-api, load-balancing]
date_consumed: 2026-07-29
---

## Summary

This ByteByteGo digest catalogs 12 core [[Claude Code]] features spanning memory ([[CLAUDE.md]]), safety (permissions, checkpoints), extensibility ([[Skills]], [[Hooks]], [[MCP]], [[Plugins]]), and workflow tools (Plan Mode, Slash Commands, Compaction, [[Subagents]]). It also explains how [[Agentic RAG]] extends traditional [[RAG]] by letting an agent select tools and refine retrieval queries, and closes with primers on [[REST API]] principles and seven [[Load Balancer]] use cases.

## Core Concepts

- [[Claude Code]] — agentic coding tool with 12 named features covering memory, safety, and extensibility
- [[CLAUDE.md]] — project memory file read at the start of every session
- [[Plan Mode]] — Claude plans before acting, reviewable before code changes
- [[Skills]] — reusable instruction files Claude follows automatically
- [[Hooks]] — custom shell scripts triggered on lifecycle events like PreToolUse/PostToolUse
- [[MCP]] — connects Claude to external tools like databases and third-party services
- [[Plugins]] — bundle third-party skills, MCPs, and hooks together
- [[Subagents]] — parallel agents spawned to divide complex multi-step workflows
- [[Agentic RAG]] — adds agent decision-making, tool selection, and query refinement to [[RAG]]
- [[REST API]] and [[Load Balancer]] — foundational system design primitives

## Key Takeaways

- CLAUDE.md is read by Claude at the start of every session
- Permissions control which tools Claude can and can't use
- Checkpoints are automatic snapshots to revert unwanted changes
- Compaction compresses long conversations to save tokens
- Subagents divide large workflows and run them simultaneously
- Agentic RAG lets an agent choose tools and refine its own retrieval queries
- Traditional RAG relies on static knowledge with limited adaptability
- Load balancers handle traffic distribution, SSL termination, and health monitoring
- Session persistence ensures a user's requests hit the same server instance
