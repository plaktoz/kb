# MCP Server: Synthesis Guide
*2026-08-09 | From concepts to hands-on to deciding when to use it*

---

## The One-Sentence Mental Model

MCP is a standardized protocol that lets an AI app (the **host**, e.g. Claude Code) call tools and read data from any **server** — your own code, a database wrapper, or a third-party service — using the same JSON-RPC wire format every time.

Without MCP: every integration is a custom one-off.
With MCP: write once, plug into any AI client.

---

## Part 1: How It Works

### The Three Players

```
┌─────────────────────────────────────────┐
│  MCP Host (Claude Code / Claude Desktop) │
│  ┌──────────┐  ┌──────────┐             │
│  │ Client 1 │  │ Client 2 │  ...        │
│  └────┬─────┘  └────┬─────┘             │
└───────┼─────────────┼────────────────────┘
        │             │
   Local stdio    Remote HTTP
        │             │
  ┌─────▼──────┐  ┌───▼────────────────┐
  │ Server A   │  │ Server B           │
  │ (Filesystem│  │ (Sentry, JIRA, etc)│
  └────────────┘  └────────────────────┘
```

- **Host** — the AI app. Creates one client per server. Decides which tools to expose to the model.
- **Client** — a connector object inside the host. Maintains a single dedicated connection to one server.
- **Server** — your code (or a third-party's). Exposes capabilities via the MCP protocol.

### The Three Primitives

| Primitive | Controlled by | Analogy | Example |
|---|---|---|---|
| **Tool** | Model — Claude decides when to call | Function/API endpoint | `search_database(query)` |
| **Resource** | Application/user — explicitly selected | File attachment | `file:///schema.sql` |
| **Prompt** | User — triggered via slash command | Parameterized template | `/code-review code=...` |

In practice: **tools are 90% of what you'll build.** Resources and prompts are for richer UX.

### The Wire Protocol (simplified)

MCP runs JSON-RPC 2.0. Three message types:

```
// 1. Discover what the server supports
Client → Server: { "method": "server/discover" }
Server → Client: { "capabilities": { "tools": {}, "resources": {} } }

// 2. List available tools
Client → Server: { "method": "tools/list" }
Server → Client: { "tools": [{ "name": "...", "inputSchema": {...} }] }

// 3. Call a tool
Client → Server: { "method": "tools/call", "params": { "name": "...", "arguments": {...} } }
Server → Client: { "content": [{ "type": "text", "text": "result" }] }
```

Two transports:
- **stdio** — local process, pipes. Zero network overhead. Best for personal dev tools.
- **Streamable HTTP** — remote, OAuth-capable. Best for shared/hosted servers.

---

## Part 2: Connecting Existing Servers (No Code Required)

### Step 1: Find a server

Start with the official reference servers — no setup beyond `npx`/`uvx`:

| Server | What it does | How to run |
|---|---|---|
| `filesystem` | Read/write local files | `npx @modelcontextprotocol/server-filesystem /path` |
| `git` | Read git repos, search history | `uvx mcp-server-git` |
| `fetch` | Fetch web URLs, return as markdown | `npx @modelcontextprotocol/server-fetch` |
| `memory` | Persistent knowledge graph (in-process) | `npx @modelcontextprotocol/server-memory` |
| `time` | Current time, timezone conversion | `uvx mcp-server-time` |

### Step 2: Register it in Claude Code

Add to `~/.claude.json` (user-wide) or `.mcp.json` in the project root (project-scoped):

```json
{
  "mcpServers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/Users/you/projects"]
    },
    "my-remote-server": {
      "type": "http",
      "url": "https://my-server.example.com/mcp",
      "headers": { "Authorization": "Bearer $MY_API_KEY" }
    }
  }
}
```

### Step 3: Verify

```
/mcp
```

Claude Code shows all configured servers and their connection status. Once green, Claude can use those tools in any conversation — just ask naturally: "check the filesystem for any `.log` files in `~/projects`."

---

## Part 3: Building Your Own Server

### Minimal Python Server (copy-paste starter)

```bash
# Prerequisites
pip install mcp   # or: uv add mcp
```

```python
# server.py
import asyncio
import mcp.types as types
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio as stdio

server = Server("my-tools")

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="greet",
            description="Returns a greeting for the given name",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name to greet"}
                },
                "required": ["name"],
            },
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "greet":
        return [types.TextContent(type="text", text=f"Hello, {arguments['name']}!")]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio.stdio_server() as (read, write):
        await server.run(
            read, write,
            InitializationOptions(
                server_name="my-tools",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Register it:
```json
{
  "mcpServers": {
    "my-tools": {
      "type": "stdio",
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

### Debug it with MCP Inspector

```bash
npx @modelcontextprotocol/inspector python server.py
```

Opens a browser UI at `localhost:5173` where you can list tools, call them manually, and see raw JSON-RPC traffic.

### Key Patterns

**Pattern 1 — Wrapping an external API**

```python
import httpx

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "search_docs":
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                "https://api.example.com/search",
                params={"q": arguments["query"]},
                headers={"Authorization": f"Bearer {API_KEY}"}
            )
        return [types.TextContent(type="text", text=resp.text)]
```

**Pattern 2 — Stateful multi-step tools (handle pattern)**

When your tool needs state across calls (e.g. an open DB transaction), return a handle from the first call and require it on subsequent calls:

```python
import uuid

sessions = {}  # In production: use Redis or a DB

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "start_session":
        sid = str(uuid.uuid4())
        sessions[sid] = {"data": []}
        return [types.TextContent(type="text", text=f"Session: {sid}")]

    if name == "append_to_session":
        sid = arguments["session_id"]
        if sid not in sessions:
            return [types.TextContent(type="text", text="Error: session expired, call start_session again")]
        sessions[sid]["data"].append(arguments["item"])
        return [types.TextContent(type="text", text="Added")]
```

The model carries the `session_id` forward — you never rely on connection-level state.

**Pattern 3 — Exposing a resource (read-only data)**

```python
@server.list_resources()
async def list_resources() -> list[types.Resource]:
    return [
        types.Resource(uri="schema://db/users", name="Users table schema", mimeType="text/plain")
    ]

@server.read_resource()
async def read_resource(uri: str) -> str:
    if uri == "schema://db/users":
        return "id INT, name TEXT, email TEXT, created_at TIMESTAMP"
    raise ValueError(f"Unknown resource: {uri}")
```

---

## Part 4: MCP vs. Skills vs. Hooks

### Skills (slash commands) — prompt-layer extensions

Skills are markdown files in `.claude/skills/<name>/SKILL.md`. They load into Claude's context when invoked. No server process, no protocol, no code.

```
.claude/
  skills/
    deploy/
      SKILL.md    # → /deploy command
    review/
      SKILL.md    # → /review command
```

Claude reads the skill's instructions and follows them. Works entirely inside the conversation.

### Hooks — deterministic lifecycle automation

Hooks fire on Claude Code events regardless of what Claude decides. They're shell commands or HTTP calls, not capabilities the model can invoke.

```json
// .claude/settings.json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{ "type": "command", "command": "prettier --write $FILE" }]
    }]
  }
}
```

### The Decision Matrix

```
Does the task need live external data or real-world side effects?
├── YES → Does it need to work across multiple AI clients (VS Code, Cursor, etc.)?
│   ├── YES → MCP server (cross-client standard)
│   └── NO  → MCP server still best; skills can't call APIs
└── NO  → Is it a reusable procedure / workflow / checklist?
    ├── YES → Skill (slash command) — cheaper, simpler
    └── NO  → Add it to CLAUDE.md if it's a project fact

Must it fire unconditionally (not when Claude decides)?
├── YES → Hook (always runs, deterministic)
└── NO  → MCP tool or skill depending on above
```

### When each shines in practice

**MCP server** — you want Claude to query your internal JIRA, PostgreSQL, or monitoring system in real-time, and you'd like this to work in VS Code Copilot too eventually.

**Skill** — you have a 10-step deployment checklist you keep pasting into chat. Turn it into `/deploy` and never paste again.

**Hook** — you want auto-formatting to run every time Claude writes a Python file. Deterministic, zero model judgment.

**CLAUDE.md** — your repo map, coding conventions, and file naming rules. Always in context, no invocation needed.

---

## Part 5: Quick Reference

### JSON-RPC primitives cheat sheet

| Operation | Method | Direction |
|---|---|---|
| Discover server capabilities | `server/discover` | Client → Server |
| List tools | `tools/list` | Client → Server |
| Call a tool | `tools/call` | Client → Server |
| List resources | `resources/list` | Client → Server |
| Read a resource | `resources/read` | Client → Server |
| List prompts | `prompts/list` | Client → Server |
| Get a prompt | `prompts/get` | Client → Server |
| Tool list changed | `notifications/tools/list_changed` | Server → Client |

### Tool definition anatomy

```json
{
  "name": "search_wiki",           // unique within this server
  "title": "Wiki Search",          // human-readable label
  "description": "Searches the local wiki notes and returns matching titles and excerpts",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search terms"
      },
      "limit": {
        "type": "integer",
        "description": "Max results to return",
        "default": 5
      }
    },
    "required": ["query"]
  }
}
```

Good descriptions matter: the model reads `description` to decide when to call the tool. Be specific about what the tool does and when to use it.

### Common mistakes

| Mistake | Fix |
|---|---|
| Storing session state on the server per-connection | Return a handle; let the model carry it |
| Vague tool descriptions | Write as if explaining to a new developer when to use this vs. other tools |
| One giant server with 30 tools | Split by domain; smaller servers are easier to debug and reuse |
| Skipping MCP Inspector | Always test with `npx @modelcontextprotocol/inspector` before wiring into Claude |
| Using MCP when a skill would suffice | If no live data needed and it's just instructions — use a skill |

---

## Related Notes
- [[loop-engineering-guide-safe-autonomous-agents]] — agent loop design patterns
- [[agentic-design-patterns-reflection]] — reflection and multi-step agent patterns
- [[best-practices-building-ai-agents]] — broader agent best practices
