---
type: literature-note
source_url: https://www.ignorance.ai/p/skills-tools-and-mcps-whats-the-difference
author: Charlie Guo
tags: [mcp, ai-tools, skills, function-calling]
date_consumed: 2026-08-03
---

## Summary

This article traces the evolution of AI capability primitives from OpenAI's 2023 function calling through [[Model Context Protocol]] (MCP) to the emerging "Skills" format. The three layers form a distinct stack: Tools provide atomic capabilities, MCP standardizes infrastructure and discovery, and Skills encode domain expertise and sequencing knowledge. Both Anthropic and OpenAI independently converged on nearly identical Skills formats, signaling an emerging standard.

## Core Concepts

- **[[Function Calling]]** — The original AI capability primitive introduced by OpenAI in 2023; describe a function via [[JSON]] schema and the model outputs structured JSON to invoke it. Enabled [[ChatGPT Plugins]], Code Interpreter, and web browsing, but every integration was bespoke with no shared infrastructure.

- **[[Model Context Protocol]]** (MCP) — Anthropic's standardization layer, described as "USB-C for AI systems." MCP servers expose capabilities dynamically so any compliant client ([[Claude]], [[Cursor]], [[ChatGPT]]) can discover and invoke them. Enables community-built connectors for [[Slack]], [[GitHub]], [[Notion]], etc.

- **[[Skills]]** — A `SKILL.md` file with YAML frontmatter (name/description) loaded as a lightweight hint; full markdown instructions load only when relevant. This progressive disclosure avoids bloating the [[Context Window]]. Skills encode *expertise* — the playbook a human expert would follow — rather than raw capabilities.

- **The Capability Stack** — Tools → MCP → Skills form a layered architecture: atomic capabilities, standardized discovery, and domain expertise respectively.

## Key Takeaways

- **Function calling origin**: OpenAI's 2023 function calling described functions via JSON schema for structured invocation.
- **MCP solves interoperability**: Any compliant client can discover and call MCP servers without bespoke integration.
- **MCP remaining gaps**: Security (auditing combined tool access) and judgment (having tools ≠ knowing how to use them well).
- **Skills add expertise layer**: Skills encode sequencing knowledge and expert playbooks, not just raw capabilities.
- **Progressive disclosure**: Skills load full instructions only when relevant, preserving context window space.
- **Cross-vendor convergence**: Anthropic and OpenAI independently arrived at nearly identical Skills formats.
- **Early-era framing**: Today's AI apps are likened to "m.google.com era" mobile sites — AI-native experiences still ahead.
- **Fragmentation expected**: Further standards fragmentation is likely before the ecosystem stabilizes.

## 🧠 First Principles & Mental Models

- **[[Layered Architecture]]**: The Tools → MCP → Skills stack mirrors the OSI model logic — each layer solves a distinct problem (capability, interoperability, expertise) without collapsing concerns, making the system composable rather than monolithic.
- **[[Progressive Disclosure]]**: Skills intentionally surface only minimal hints upfront and expand instructions on demand — a direct application of progressive disclosure to context window management, trading upfront load for targeted relevance.

## 🃏 Review Questions

**Q1**: What is the core thesis distinguishing Tools, MCP, and Skills?
**A**: They form a three-layer stack — Tools provide atomic capabilities, MCP standardizes infrastructure and discovery, and Skills encode domain expertise and sequencing knowledge that guides how tools are used.

**Q2**: What two problems remain unsolved by MCP alone?
**A**: Security (the difficulty of auditing combined tool access across multiple MCP servers) and judgment (having access to tools does not mean the agent knows how to sequence or apply them well).

**Q3**: How does the Skills format address context window bloat?
**A**: A `SKILL.md` file exposes only a lightweight YAML hint (name/description) upfront; full markdown instructions are loaded into context only when the skill is determined to be relevant, preserving context window space for active tasks.
