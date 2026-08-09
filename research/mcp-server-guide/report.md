# Research: MCP Server Guide
*Generated: 2026-08-09 | Scope: Practical + conceptual guide to MCP servers — concepts, building your own, connecting existing servers in Claude Code, comparison with skills/hooks, and decision framework*

## Research Outline

1. MCP Concepts & Architecture — What is MCP, how the protocol works, primitives
2. Using Existing MCP Servers in Claude Code — Setup, configuration, popular servers
3. Building Your Own MCP Server — Step-by-step: Python/Node.js tutorial
4. MCP vs Skills vs Hooks vs Other Alternatives — Community usage, trade-offs
5. Decision Framework — Choosing the right tool for the job

---

## Section 1: MCP Concepts & Architecture

### What is the Model Context Protocol (MCP)?

- **Source**: https://modelcontextprotocol.io/introduction
- **Summary**: MCP is an open-source standard for connecting AI applications (like Claude, ChatGPT, VS Code Copilot) to external data sources, tools, and workflows. Think of it as "USB-C for AI" — a single standardized plug that works across any AI client and any external system. Before MCP, every AI integration was a custom one-off; MCP makes them reusable and composable. Use cases include reading Google Calendar, querying databases, calling APIs, controlling Blender, and more.
- **Relevance**: Foundational introduction to the "what and why" of MCP — essential starting point.

### MCP Architecture Overview

- **Source**: https://modelcontextprotocol.io/docs/concepts/architecture
- **Summary**: MCP has three roles: **MCP Host** (the AI app, e.g. Claude Code), **MCP Client** (created by the host, one per server connection), and **MCP Server** (the program exposing capabilities). The protocol has two layers: a **data layer** (JSON-RPC 2.0 for message structure, tools/resources/prompts primitives, discovery, notifications) and a **transport layer** (how bytes move: stdio for local processes, Streamable HTTP for remote servers). MCP is stateless — every request carries full context. The three server-side **primitives** are: **Tools** (model-invoked executable functions), **Resources** (app-driven data sources), and **Prompts** (user-triggered reusable templates).
- **Relevance**: Defines the mental model — host/client/server roles and when each primitive applies.

### MCP Tools — Protocol Deep Dive

- **Source**: https://modelcontextprotocol.io/docs/concepts/tools
- **Summary**: Tools are model-controlled functions Claude decides to invoke based on context. Each tool has a `name`, `description`, `inputSchema` (JSON Schema), and optional `outputSchema`. Tools are discovered via `tools/list` and invoked via `tools/call`. Results can return text, images, audio, resource links, or structured JSON. Servers can notify clients of tool list changes via `notifications/tools/list_changed`. Security: servers must validate inputs; clients should prompt users for confirmation on sensitive operations. Tools with no parameters use `{"type":"object","additionalProperties":false}`.
- **Relevance**: The most commonly used primitive — deep spec knowledge needed to build production-quality servers.

### MCP Resources

- **Source**: https://modelcontextprotocol.io/docs/concepts/resources
- **Summary**: Resources are **application-controlled** data sources (files, DB schemas, API responses) identified by URI. Unlike tools (which Claude decides to use), resources are explicitly selected by the host application or user. Resources support `resources/list`, `resources/read`, and subscription-based change notifications. They can be text or binary, can use URI templates for parameterization, and support annotations (`audience`, `priority`, `lastModified`) for filtering. Standard URI schemes: `file://`, `https://`, `git://`.
- **Relevance**: Clarifies the resources-vs-tools distinction — resources are passive data, tools are active functions.

### MCP Prompts

- **Source**: https://modelcontextprotocol.io/docs/concepts/prompts
- **Summary**: Prompts are **user-controlled** reusable templates surfaced as slash commands or UI elements. They are defined server-side but *invoked by the user* (not autonomously by the model). A prompt can include static text, embedded resources, and multi-turn message sequences. Discovered via `prompts/list`, fetched via `prompts/get` with arguments. Example: a `code_review` prompt that wraps user-provided code in a structured analysis request.
- **Relevance**: Explains the third primitive — prompts are the MCP equivalent of parameterized slash commands.

---

## Section 2: Using Existing MCP Servers in Claude Code

### Connect Claude Code to Tools via MCP

- **Source**: https://code.claude.com/docs/en/mcp
- **Summary**: Claude Code supports MCP servers to extend its reach into external systems. You configure servers in `~/.claude.json` (user-level) or `.mcp.json` (project-level). Each server entry specifies `type` (`stdio` or `http`), the command to run it, and any args/env vars. Once connected, Claude can use server tools directly in conversation — e.g., "implement the feature from JIRA issue ENG-4521," "query our PostgreSQL database," "check Sentry for errors." The `/mcp` command in Claude Code shows all connected servers and their status. MCP servers can also act as **channels** that push messages into your session (e.g., reacting to Telegram messages or webhook events while you're away).
- **Relevance**: Practical guide to connecting and using MCP servers without building anything — the quickest hands-on entry point.

### Official Reference MCP Servers

- **Source**: https://github.com/modelcontextprotocol/servers
- **Summary**: Seven actively maintained reference servers: **Everything** (testing/demo), **Fetch** (web content retrieval), **Filesystem** (local file ops), **Git** (repository read/search/manipulate), **Memory** (persistent knowledge graph), **Sequential Thinking** (multi-step reasoning), **Time** (timezone/time conversion). These run via `npx` (TypeScript) or `uvx`/`pip` (Python). Formerly official servers for PostgreSQL, GitHub, Slack, Redis, etc. have been archived and some handed to other maintainers. These are educational examples, not production-hardened tools.
- **Relevance**: Ready-to-use servers to connect immediately for hands-on learning without writing any code.

---

## Section 3: Building Your Own MCP Server

### Build an MCP Server (Official Quickstart)

- **Source**: https://modelcontextprotocol.io/quickstart/server
- **Summary**: The official tutorial walks through building a weather server with two tools (`get_alerts` and `get_forecast`) using either Python (with the `mcp` package via `uv`) or TypeScript (with `@modelcontextprotocol/sdk`). Key steps: (1) install the SDK, (2) create an `mcp.server.Server` instance, (3) declare tools using `@server.list_tools()` and `@server.call_tool()` decorators, (4) connect via `stdio_server()`, (5) register in Claude Desktop's config. The server connects to the US National Weather Service API. The tutorial shows a complete working server in ~50 lines of Python. Testing is done via the **MCP Inspector** (`npx @modelcontextprotocol/inspector`), a browser-based debugger for any MCP server.
- **Relevance**: Canonical hands-on walkthrough — the fastest path from zero to a working custom MCP server.

### Minimal Python MCP Server Pattern

```python
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio as stdio

server = Server("my-server")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="my_tool",
            description="Does something useful",
            inputSchema={
                "type": "object",
                "properties": {
                    "param": {"type": "string", "description": "Input value"}
                },
                "required": ["param"],
            },
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "my_tool":
        result = f"Processed: {arguments['param']}"
        return [types.TextContent(type="text", text=result)]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio.stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream,
            InitializationOptions(server_name="my-server", server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={})))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

*Pattern derived from official quickstart documentation.*

### MCP Tool Design: Stateful Tools Pattern

- **Source**: https://modelcontextprotocol.io/docs/concepts/tools
- **Summary**: MCP is stateless at the protocol level — no session persists between calls. For multi-step stateful workflows (shopping cart, open browser, DB transaction), servers return an explicit **handle** (e.g., `basket_id`) from a creation tool and accept that handle on subsequent calls. The model carries the handle forward in its context. Key design rules: handles should be opaque, short-lived, authorized per-call, and described with their TTL in the tool description so the model can decide when to create new state.
- **Relevance**: Critical pattern for building non-trivial servers — avoids the common mistake of trying to store server-side session state.

---

## Section 4: MCP vs Skills vs Hooks vs Other Alternatives

### Claude Code Skills (Slash Commands)

- **Source**: https://code.claude.com/docs/en/slash-commands
- **Summary**: Skills (formerly "custom commands") are `SKILL.md` files in `.claude/skills/<name>/` that extend what Claude can do by loading instructions only when invoked. They create `/name` slash commands. Skills are **loaded into Claude's context** — they are prompt-level instructions, not code. They can be invoked explicitly (`/deploy`) or automatically by Claude when relevant. A `.claude/commands/deploy.md` file works identically. Skills are ideal for: recurring procedures you keep pasting into chat, checklists, multi-step workflows described in prose, and project-specific knowledge that doesn't belong in `CLAUDE.md`.
- **Relevance**: Most direct alternative to MCP for extending Claude Code — understanding when skills suffice vs. when you need a full MCP server is the core decision.

### Claude Code Hooks vs MCP

- **Source**: https://code.claude.com/docs/en/settings
- **Summary**: Hooks are shell commands/HTTP requests that fire automatically on Claude Code lifecycle events (`ConfigChange`, before/after tool use). They are **deterministic** — unlike asking Claude to do something, a hook always runs. Hooks are reactive side-effects you control; MCP servers are capabilities Claude actively decides to use. Key differences: hooks go one direction (Claude Code → your script), MCP is bidirectional; hooks are event-driven and guaranteed, MCP tools require model judgment; hooks configured in `settings.json`, MCP servers in `~/.claude.json` or `.mcp.json`.
- **Relevance**: Hooks and MCP solve different problems — hooks for automation/enforcement, MCP for interactive capabilities.

### Comparison Matrix

| Dimension | MCP Server | Skills (Slash Commands) | Hooks |
|---|---|---|---|
| **What it is** | Running process exposing tools/resources | Markdown prompt instructions | Shell command on lifecycle events |
| **Invocation** | Claude decides autonomously | User triggers `/name` or Claude auto-detects | Always fires on configured event |
| **Direction** | Bidirectional protocol | Into Claude's context window | Claude Code → your script |
| **Use case** | External APIs, databases, live data | Procedures, checklists, project workflows | Automation, enforcement, side effects |
| **Overhead** | High (process, protocol) | Near-zero (loaded markdown) | Low (shell command) |
| **Cross-client** | Works in any MCP host (VS Code, Cursor, etc.) | Claude Code only | Claude Code only |
| **Persistence** | Server runs continuously | Stateless, per-invocation | Stateless, per-event |
| **Best for** | Real external data/actions needed live | Reusable instructions/procedures | Always-on side effects |

---

## Section 5: Decision Framework

### When to Use Each Extension Pattern

**Use an MCP Server when:**
- You need live, dynamic data from an external system (database query results, current JIRA tickets, live Sentry errors)
- You want to take actions in external systems on Claude's behalf (create PRs, send emails, write to Slack)
- The capability needs to work across multiple AI clients (not just Claude Code — e.g., VS Code Copilot, Cursor, Claude Desktop)
- You're wrapping an existing API or service that requires auth, pagination, or stateful handles
- You want to share the capability with other developers as an installable tool

**Use a Skill (Slash Command) when:**
- The "capability" is really just a reusable set of instructions or a procedure
- No external data or live API is needed — the workflow is entirely within Claude's reasoning
- You keep re-pasting the same multi-step instructions into chat
- It's project-specific workflow knowledge (deploy steps, review checklists, ingest procedures)
- You want low overhead — no server process, no JSON-RPC, just a `.md` file

**Use Hooks when:**
- You want something to happen deterministically on every tool call, not when Claude decides
- Side effects that must always fire: logging, notifications, auto-formatting on file save
- Enforcement: block certain file modifications, require review before committing
- Integration with external monitoring systems that should react to Claude's actions

**Use plain CLAUDE.md when:**
- It's a fact about the project, not a procedure (repo map, naming conventions, key constraints)
- It applies to every conversation, not a specific invoked workflow
- It's short enough not to bloat the context window

### The 3-Question Decision Test

1. **Does it require live data or real-world actions?** → Yes → MCP server. No → consider skills/CLAUDE.md.
2. **Does it need to work across AI clients beyond Claude Code?** → Yes → MCP (it's the cross-client standard). No → skills are simpler.
3. **Must it fire unconditionally, not by Claude's judgment?** → Yes → hooks. No → MCP or skills.

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://modelcontextprotocol.io/introduction
- https://modelcontextprotocol.io/docs/concepts/architecture
- https://modelcontextprotocol.io/quickstart/server
- https://modelcontextprotocol.io/docs/concepts/tools
- https://modelcontextprotocol.io/docs/concepts/resources
- https://modelcontextprotocol.io/docs/concepts/prompts
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/slash-commands
