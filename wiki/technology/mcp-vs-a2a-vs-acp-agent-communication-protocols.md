---
type: literature-note
source_url: https://blog.bytebytego.com/p/mcp-vs-a2a-vs-acp-how-ai-agents-actually-talk
author: ByteByteGo
tags: [mcp, a2a, agent-protocols, multi-agent-systems]
date_consumed: 2026-07-27
---

## Summary

[[ByteByteGo]] maps three emerging agent communication protocols that solve different layers of AI interoperability. [[MCP]] (from [[Anthropic]]) standardizes agent-to-tool communication; [[A2A]] (from Google) handles agent-to-agent delegation; [[ACP]] has been merged into A2A. Together, MCP and A2A form the communication infrastructure layer for multi-agent AI systems.

## Core Concepts

- **[[MCP]] (Model Context Protocol)** — Anthropic's protocol for agent-to-tool communication; now supported across Claude, GPT, Gemini
- **[[A2A]] (Agent-to-Agent Protocol)** — Google's protocol for agent-to-agent delegation; includes capability negotiation
- **[[ACP]] (Agent Communication Protocol)** — earlier inter-agent messaging standard; merged into A2A
- **[[Multi-Agent Systems]]** — architectures where multiple specialized agents coordinate to complete complex tasks
- **[[Protocol Interoperability]]** — how standardized protocols reduce integration friction across vendor ecosystems

## Key Takeaways

- **MCP = agent→tool**: use for calling APIs, databases, or external services from an agent
- **A2A = agent→agent**: use for delegating tasks between agents or building agent pipelines
- **ACP is gone**: treat legacy ACP systems as A2A
- **Cross-vendor**: MCP and A2A are both gaining multi-vendor support (Claude, GPT, Gemini, etc.)
- **Infrastructure layer**: MCP + A2A together = the communication stack for agentic AI
