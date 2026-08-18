---
type: literature-note
source_url: https://www.usetranscribe.io/yt/shZgedW15vg/anthropic-claude-code?format=md
author: Daisy Hollman
tags: [claude-code, agentic-engineering, context-engineering, multi-agent]
date_consumed: 2026-08-17
---

## Summary

Daisy Hollman from Anthropic's Claude Code team argues that moving from chatbot to agent is about expanding tool access until the model can do everything a programmer can do. Professional customization — giving the model access to team chat, CI dashboards, and internal docs — is the critical gap between out-of-the-box capability and real-world usefulness. By 2026, the challenge shifts from getting information into models to managing many concurrent agents efficiently, with "your attention is the smallest box in the system."

## Core Concepts

- **[[Agentic AI]]**: The shift from chatbot to agent happened as [[Tool Calling]] expanded; once a model can run shell commands, edit files, and use CI tools, it warrants the "agent" label.
- **In-Context Learning**: Daisy's plain definition — "a really fancy term that basically means text files." Customization bridges what a model knows vs. what your team knows via context injection.
- **[[Context Window]] Constraint**: At ~1M tokens, the context window is a finite resource; everything — system prompts, tool definitions, file contents, tool results — competes for space. Naive stuffing is like "running npm on an Arduino."
- **KV Cache Economics**: Predictions are far cheaper when prior tokens are identical across calls. Dynamically swapping context (e.g., early Cursor Rules behavior) can become extremely expensive.
- **[[Claude Code]] Plugin Primitives**:
  - [[MCP Servers]] — Adds tool schemas to system prompt; scales poorly (20 servers × 15 tools fills context fast).
  - Skills — Lazy system prompts expanded on demand; descriptions always loaded.
  - [[Sub-agents]] — Offloads to separate context window; description strings accumulate.
  - Hooks — Scripts triggered by events; inject context only when relevant. Zero cost unless fired — her preferred abstraction.
- **Memory vs. Context Engineering**: Agent-curated memory files (model memory) should be treated as a separate concern from context engineering primitives; conflating them creates confusion at scale.
- **Feedback Loops**: Post-tool-use hooks deliver inline diagnostics ("red squiggly"-style) at the moment of a mistake using existing tooling, tightening the loop without waiting for a smarter model.
- **[[Multi-Agent]] Fleet Management**: Agents run on persistent work trees (named A-Z), slash/loop for scheduled self-wake-ups, monitored via a "fleet view." Attention, not compute, is the bottleneck.

## Key Takeaways

- **Agent = Tool Access**: Models become agents when they can use shell, file, and CI tools.
- **Customization Gap**: Out-of-the-box models can't access team chat, CI, or internal docs — customization closes this.
- **Context Is Finite**: Everything competes for ~1M tokens; be deliberate about what enters the window.
- **KV Cache Cost**: Dynamic context swapping is expensive; prefer stable, append-only context structures.
- **Hooks Win on Scale**: Hooks inject zero tokens unless triggered — best scaling primitive among MCP/Skills/Sub-agents/Hooks.
- **CLAUDE.md Warning**: Unconditional injections look cheap to write but are costly at runtime.
- **Separate Memory from Context**: Future large-scale engineering requires clear separation between model memory files and context engineering.
- **Feedback Over Model Upgrades**: Tighten feedback loops instead of waiting for a smarter model.
- **2025 vs 2026 Shift**: 2025 was about getting information into models; 2026 is about managing information out across many agents.
- **Attention Is the Bottleneck**: "Your attention is the smallest box in the system."

## 🧠 First Principles & Mental Models

- **[[Opportunity Cost]]**: Every token in the context window displaces another; treating context as a scarce resource forces the same prioritization logic as any constrained budget — the value of what's in must exceed the value of what's left out.
- **[[Feedback Loops]]**: Shorter feedback cycles compound learning faster than waiting for a superior tool; post-tool-use hooks are the engineering instantiation of tightening the loop rather than upgrading the learner.

## 🃏 Review Questions

**Q1**: What is the central argument about agent customization in this talk?
**A**: If the model can't access everything you can access — team chat, CI dashboards, internal docs — it can't do your job with you; customization bridges that gap via in-context learning (i.e., text files injected into context).

**Q2**: Why are Hooks preferred over MCP Servers for scaling Claude Code in large codebases?
**A**: Hooks inject zero tokens into the context window unless triggered by a relevant event, whereas MCP Servers unconditionally load tool schemas — 20 servers × 15 tools quickly consumes context budget.

**Q3**: What is the key implication of the "2026 shift" Daisy describes, and how does it change how engineers should work?
**A**: The challenge moves from feeding information into models to orchestrating many concurrent agents efficiently; engineers should treat their own attention as the scarcest resource and design fleet management (persistent work trees, fleet view, scheduled wake-ups) accordingly.
