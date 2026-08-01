---
type: literature-note
source_url: https://blog.bytebytego.com/p/best-practices-for-building-ai-agents
author: ByteByteGo
tags: [ai-agents, agent-architecture, context-management, system-design]
date_consumed: 2026-07-27
---

## Summary

[[ByteByteGo]] synthesizes production lessons from AI agent systems into four practice areas: context management, control flow, state management, and scope control. The central thesis is that well-built agents are deterministic where possible — using model reasoning only for genuinely ambiguous problems and constraining everything else to explicit scaffolding. This reduces cost, improves reliability, and makes agent behavior auditable.

## Core Concepts

- **[[Context Management]]** — keeping agent context windows clean; separating system context from user context; compression for long-running agents
- **[[Deterministic Scaffolding]]** — using state machines and workflow graphs instead of relying on model reasoning for task sequencing
- **[[State Persistence]]** — storing agent state externally (not in model memory); designing for resume-ability
- **[[Scope Control]]** — principle of least privilege for tool access; explicit capability boundaries; sandboxed execution
- **[[Context Engineering]]** — broader discipline of deliberately assembling everything an LLM sees (instructions, history, retrieved knowledge, tool defs, tool outputs), distinct from just prompt phrasing
- **[[Context Rot]]** — unpredictable performance degradation as input length grows; compounded by uneven attention distribution (RoPE decay)
- **[[Subagent Context Pattern]]** — dispatching subagents with clean context windows for token-heavy work; parallel subagents on cheaper models for independent tasks
- **[[LLM Token Routing]]** — directing each agent step to the cheapest capable model; tiered model selection (top/balanced/background) mapped to task modes
- **[[Tool Poisoning]]** — malicious instructions hidden in tool metadata (name, description, schema) that the model reads but the user doesn't see
- **[[Indirect Prompt Injection]]** — untrusted content an agent reads is misinterpreted as instructions, potentially triggering unintended tool calls or data exfiltration
- **[[Agent-Computer Interface (ACI)]]** — design principles for tool documentation; tools as the interface between model reasoning and the environment

## Key Takeaways

- **Determinism first**: use explicit control flow for structured tasks — reserve LLM reasoning for genuinely ambiguous problems
- **External state**: never rely on model memory across turns; use structured JSON state objects
- **Resume-ability**: agents should restart from last checkpoint without full reruns
- **Checkpoints**: pause and confirm before irreversible actions
- **Least privilege**: tools given to agents should be scoped to what the task actually requires
- **Context limits have plateaued in practice**: benchmarks show better quality below 200K tokens even when 1M is available — effective context length is much smaller than advertised
- **Explore-then-report subagent pattern**: dispatch a fresh subagent to investigate and return only a condensed summary, keeping the parent agent's context budget intact
- **Parallel subagents on cheaper models** (e.g. Haiku) for independent tasks yield real speed and cost gains — don't over-fragment; only worth it when parent context budget is the binding constraint
- **"Lost in the middle" degrades accuracy by 30%+**: a 2025 Chroma study found all 18 tested frontier models degrade when relevant info sits mid-context — place high-priority content at context boundaries
- **Four context strategies: write, select, compress, isolate** — externalize to scratchpad (write), retrieve only relevant chunks (select), summarize history (compress), split across specialized agents (isolate)
- **Multi-agent isolation beats single agent by 90.2%**: Anthropic's research system using isolated Opus 4 + Sonnet 4 sub-agents outperformed a single monolithic agent
- **LLM routing cuts costs 40–70%**: route each agent step to the cheapest model capable of handling it; 80–90% of requests don't need frontier models
- **Route on task type, not a classifier**: planning vs. edit vs. debug is a free, reliable routing signal — no additional model needed
- **Fix a total budget rather than chasing lowest per-token rate**: cheaper tokens drive more usage (Jevons Paradox), so total spend can rise even as unit cost falls
- **Treat tool metadata as executable influence**: tool name, description, and schema are read by the model and can carry injected instructions — vet all tool definitions, especially from third-party MCP servers
- **Indirect Prompt Injection**: treat all external content an agent processes (emails, docs, tickets) as data, never instructions
- **Tool documentation is architecture**: clear absolute paths, edge-case handling, and minimal formatting overhead in tool docs matter as much as agent topology — treat each tool definition like a docstring for a junior developer
