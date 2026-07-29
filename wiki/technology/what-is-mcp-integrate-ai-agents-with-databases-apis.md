---
type: literature-note
source_url: https://www.youtube.com/watch?v=eur8dUO9mvE
author: IBM Technology
tags: [mcp, ai-agents, model-context-protocol, api-integration]
date_consumed: 2026-07-29
---

## Summary

[[Model Context Protocol]] (MCP) is an open-source standard that enables AI agents to connect to external data sources — including databases, APIs, and local files — through a unified transport layer. The architecture separates concerns across three components (host, client, server) so that any agent can discover and invoke tools without tight coupling to specific data backends. MCP standardizes how LLMs request tool execution and receive results, making multi-source agent workflows composable and reusable.

## Core Concepts

- **[[Model Context Protocol]] (MCP)**: Open standard for connecting [[AI Agents]] to external data sources via a protocol-based transport layer.
- **MCP Host**: The top-level application (e.g., chat app, [[IDE]] code assistant) that houses one or more MCP clients.
- **MCP Client**: Lives inside the host; manages communication with MCP servers on behalf of the [[Large Language Model]].
- **MCP Server**: Bridges the client to actual data — relational or [[NoSQL]] databases, REST/GraphQL [[APIs]], or local file systems and code.
- **Transport Layer**: The protocol sitting between host/client and server, enabling host-agnostic, multi-server connections.
- **Tool Discovery**: The host queries MCP servers for available tools before forwarding a user query plus tool list to the [[LLM]], which then selects appropriate tools.
- **Agentic Loop**: After the LLM selects tools, the host calls the relevant MCP server(s); the server executes and returns results; subsequent calls are chained until a final answer is produced.

## Key Takeaways

- **Standard Interface**: MCP decouples agents from specific backends — one client, many servers.
- **Multi-Server Support**: A single host can connect to multiple MCP servers simultaneously.
- **Tool Selection by LLM**: The [[LLM]] decides which tools to invoke based on available tool metadata.
- **Execution Delegation**: The MCP server handles all backend execution (DB queries, API calls, code runs).
- **Composable Workflows**: Subsequent MCP calls chain naturally for multi-step agent tasks.
- **Broad Applicability**: Useful for chat apps, IDE assistants, and any application embedding an [[AI Agent]].
- **Open Source**: MCP is a community standard, not vendor-locked.

## First Principles & Mental Models

- **[[Separation of Concerns]]**: MCP enforces a clean boundary between reasoning (LLM/host), tool routing (client), and execution (server) — each layer can evolve independently, which is why the standard scales across heterogeneous backends without re-engineering the agent.
- **[[Standardization as Leverage]]**: A shared protocol turns N×M integration problems (N agents, M data sources) into N+M problems — exactly the compounding advantage that makes open standards like HTTP or USB so durable.
