---
type: literature-note
source_url: https://blog.bytebytego.com/p/mcp-vs-a2a-vs-acp-how-ai-agents-actually-talk
author: ByteByteGo
tags: [ai-agents, multi-agent-systems, mcp, a2a]
date_consumed: 2026-08-01
---

## Summary

Three protocols have emerged to solve distinct layers of AI agent interoperability: [[MCP (Model Context Protocol)]] for agent-to-tool communication, [[A2A (Agent-to-Agent Protocol)]] for agent-to-agent delegation, and ACP, which has been merged into A2A. Together, MCP and A2A form the communication infrastructure layer for complex multi-agent AI systems. Standardizing these protocols reduces integration friction and enables cross-vendor ecosystem interoperability.

## Core Concepts

- **[[MCP (Model Context Protocol)]]** — Developed by [[Anthropic]]; standardizes how agents invoke external tools, APIs, databases, and services at the tool-calling layer. Now supported across Claude, GPT, and Gemini ecosystems.
- **[[A2A (Agent-to-Agent Protocol)]]** — Developed by [[Google]]; enables one agent to delegate tasks to another, forming multi-agent pipelines with capability negotiation.
- **[[ACP (Agent Communication Protocol)]]** — Originally a separate inter-agent messaging standard; consolidated into A2A and no longer a distinct protocol.
- **[[Multi-Agent Systems]]** — Architectures where multiple specialized agents collaborate, requiring defined protocols for tool access and peer coordination.
- **Capability Negotiation** — A2A allows agents to advertise their capabilities so orchestrating agents can route tasks appropriately.

## Key Takeaways

- **MCP**: Use when an agent needs to call a tool, API, or database.
- **A2A**: Use when an agent needs to spawn or delegate to another agent.
- **ACP is dead**: Treat any legacy ACP system as A2A going forward.
- **Anthropic built MCP**; **Google built A2A** — protocol ownership is vendor-split.
- **Interoperability layer**: MCP + A2A together are the infrastructure for agentic AI.
- **Cross-ecosystem support**: MCP is now standard across Claude, GPT, Gemini.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: MCP handles agent-tool interaction while A2A handles agent-agent coordination — each protocol owns exactly one layer, preventing conflation of responsibilities and simplifying system design.
- **[[Standardization as Infrastructure]]**: Just as TCP/IP reduced friction for networked applications, MCP and A2A reduce integration cost for multi-agent systems — standards enable compounding ecosystem value across competing vendors.
