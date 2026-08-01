# Agent Skills vs MCP in the Claude Code Era

**Source:** https://www.youtube.com/watch?v=pvxNcQTcIy4 (Tim Berglund, Confluent Developer, 2026-03-10)

## Core distinction

Skills and MCP serve overlapping but distinct purposes. For **local coding agents** (e.g. Claude Code on a laptop), skills can substitute for MCP in many cases. For **agentic microservices** running in the cloud, MCP remains necessary.

## What MCP does

MCP (Model Context Protocol) is an infrastructure layer between an agent and external tools/resources:
- Provides a **standardised interface** the agent can discover and call
- Handles authentication to backend systems
- Exposes both tools (actions) and resources (data reads)

See also: [[mcp-vs-a2a-vs-acp-agent-communication-protocols]], [[what-is-mcp-integrate-ai-agents-with-databases-apis]]

### Recent MCP spec updates (as of early 2026)
- **Resource API in decline** — practitioners discovered tool calls cover resource queries just as well; the resource API sees little adoption in the wild
- **Streamable HTTP** — replaces server-sent events; cleaner to deploy when the MCP server is cloud-hosted
- **OAuth 2.1** — supports the pop-up auth flow for user-facing local agents (e.g. logging into GitHub from Claude Code); headless microservice OAuth is still evolving

## What skills are

A skill is a **directory tree of files** the agent can read at runtime:
- **Root markdown file** — extended prompt with specialised instructions and procedures for a specific task domain
- **Resource sub-directories** — static reference data (e.g. plant information for a landscaping skill)
- **Script sub-directories** — bash or Python scripts the agent can invoke to take local or API-mediated actions

Skills originated as plugins for Claude Desktop and Claude Code. They are file-system artefacts — distributed via GitHub, not hosted in the cloud.

## Where they overlap

A skill script that calls an authenticated CLI can replicate what an MCP tool call would do. For the **local coding agent** use case, this substitution is clean and often simpler:
- CLI auth tokens handle credentials without a separate MCP server
- Everything stays local and file-system native
- Python SDKs are beginning to let custom-built agents consume skills directly

This is why some argue skills render MCP redundant — but the argument only holds for the local agent scenario.

## Where MCP is still required

| Scenario | Skills sufficient? | MCP needed? |
|---|---|---|
| Local coding agent (Claude Code) | Yes, for many tasks | Optional |
| Cloud-hosted agentic microservice | No | Yes |
| Real-time data (Kafka, CRMs, tickets) | No | Yes |
| Multi-agent service mesh | No | Yes |

Agentic microservices need MCP's standardised interface precisely because they cannot rely on a local file system or CLI auth tokens available only on a developer's machine.

## Practical takeaway

Both skills and MCP are essential in 2026. Skills are the right tool when you are **extending a local coding agent**; MCP is the right tool when you are **building cloud-hosted agents or integrating with live enterprise data**.

See also: [[ai-agents-claude-skills-methodology]], [[building-effective-ai-agents-anthropic]], [[12-claude-code-features-every-engineer-should-know]]
