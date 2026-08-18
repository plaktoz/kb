---
source_url: https://www.usetranscribe.io/yt/shZgedW15vg/anthropic-claude-code?format=md
author: Daisy Hollman
date: 2026-08-17
---

# How Anthropic Uses Claude Code: Agentic Software Engineering at Scale

Daisy Hollman, who works on Claude Code at Anthropic, delivered this talk (NDC Conferences, YouTube) covering the evolution of agentic programming tools, customization strategies, and scaling challenges in enterprise software engineering.

## From Chatbot to Agent

The shift from chatbots to agents happened gradually as tool-calling capability expanded. Models went from zero tool calls to a few, until the autonomy level warranted a new label: "agent." Coding agents like Claude Code give models access to shell commands, file editing, and CI tools — essentially what a programmer can do.

## Why Customization Matters

Out of the box, Claude only sees a repo and a shell. But professional software engineering involves team chat, CI dashboards, internal docs, and institutional memory. Daisy's thesis: if the model can't do everything you can do, it can't do your job with you. Customization bridges the gap between what a model knows and what your team knows — she calls this "in-context learning," which she describes plainly as "a really fancy term that basically means text files."

## The Context Window Constraint

Context windows (~1M tokens) haven't scaled as fast as model capabilities. Everything competes for that space: system prompts, tool definitions, file contents, tool results. She compares naive context-stuffing to "running npm on an Arduino" — you must be deliberate about what goes in.

An additional constraint is the KV cache: predictions are far cheaper when prior tokens are identical across calls. Swapping context in and out dynamically (like early Cursor Rules behavior) can become extremely expensive.

## Plugin Primitives and Scalability

| Primitive | How It Works | Scales? |
|-----------|-------------|---------|
| MCP Servers | Adds tool schemas to system prompt | Poor — 20 servers x 15 tools fills context fast |
| Skills | Lazy system prompts expanded on demand | Partial — descriptions always loaded |
| Sub-agents | Offloads to separate context window | Better, but description strings accumulate |
| Hooks | Scripts triggered by events; inject context only when relevant | Yes — zero cost unless fired |

Hooks are her favorite abstraction because they inject nothing unless determined relevant. She contrasts this with unconditional CLAUDE.md injections, which she warns look cheap to implement but are costly at runtime.

## Memory vs. Context Engineering

Model memory (agent-curated text files) should be treated separately from context engineering primitives. She argues future large-scale engineering will require clear separation between these two concepts.

## Feedback Loops Over Smarter Models

Rather than waiting for a better model, tightening feedback loops yields faster improvement. Post-tool-use hooks can deliver "red squiggly"-style inline diagnostics at the moment of a mistake — using tooling teams already have — rather than waiting for a compile step.

## Scaling Through Multiple Agents

2025 was about getting information into models. 2026, she argues, will focus on getting information out — managing many concurrent agents efficiently. She runs agents on persistent work trees (named A-Z), uses slash/loop for scheduled self-wake-ups, and monitors sessions via Claude's "fleet view." Her summary: "Your attention is the smallest box in the system."

## Three Takeaways

1. Give the model access to everything you have access to
2. Be deliberate about what goes into the context window
3. Choose abstractions that scale to real-world, large-codebase engineering
