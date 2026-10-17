---
type: literature-note
source_url: https://www.youtube.com/watch?v=E5-QK3CDVQM
author: Matt Pocock
tags: [ai-agents, sandboxing, typescript, claude-code]
date_consumed: 2026-10-17
---

## Summary

Matt Pocock open-sourced Sand Castle, a TypeScript library for orchestrating AI coding agents in isolated Docker sandboxes, enabling fully AFK (Away From Keyboard) autonomous agent workflows. The library provides a simple `sandcastle.run()` primitive that takes an agent, sandbox, and prompt, and supports parallel multi-agent pipelines with planner → implementer → reviewer → merger patterns.

## Core Concepts

- **[[Sand Castle]]** — Open-source TypeScript library (`npm install ai-hero sand-castle`); orchestrates AI coding agents (Claude Code, Codex, etc.) inside isolated sandboxes
- **AFK agents** — Autonomous coding agents that run without human interaction; require sandboxing to prevent dangerous system access
- **[[Docker]] sandbox** — Primary isolation mechanism; Sand Castle agents run inside Docker containers, limiting blast radius of agent actions
- **`sandcastle.run()`** — Core API: `run({ agent, sandbox, prompt })`; returns a result including commits made; fully programmatic and agent-agnostic
- **Parallel planner-implementer pattern** — Planner agent reads open GitHub issues (filtered by `sand-castle` label), outputs a JSON plan, then spawns parallel implementer agents per issue
- **Reviewer + merger agents** — Reviewer checks each implementer branch; a senior merger agent handles merging all branches back to main, resolving conflicts with AI
- **CLAUDE.md-style prompts** — `!`-prefixed backticks execute shell commands at prompt resolution time (e.g., `git diff`); allows dynamic context injection
- **[[Matt Pocock]]** — TypeScript educator and open-source developer; runs "AI skills for real engineers" newsletter

## Key Takeaways

- **Core primitive is simple**: `sandcastle.run(agent, sandbox, prompt)` is the entire API surface; complexity lives in the prompts and pipeline structure.
- **AFK requires sandboxing**: YOLO mode (no permissions) is dangerous; proper AFK operation needs isolated environments.
- **Agent-agnostic**: Works with Claude Code, Codex, or any agent; switching models is a one-line change.
- **Reviewer pattern adds quality**: Reviewer agent catches implementer mistakes before merge; adversarial review (different model for each role) is possible.
- **GitHub Issues as backlog**: Issues labelled `sand-castle` become the work queue; planner selects only unblocked issues.
- **Templates scaffold everything**: `npx sand-castle init` generates Dockerfile, prompts, and main.ts; five templates including parallel planner with review step.

## 🧠 Core Principles

**T1. Sandboxing is the enabling constraint for autonomous agent operation.** Without isolation, AFK agents cannot be trusted with real systems; with it, the blast radius of any mistake is bounded and agents can be given genuine autonomy. · *model:* [[Activation Energy]]
→ explains: AFK requires sandboxing, Core primitive is simple

**T2. Owning the process beats renting a platform.** By writing the orchestration logic as TypeScript code rather than using a third-party service, developers can compose arbitrary agent topologies without being constrained by a vendor's workflow model.
→ explains: Agent-agnostic, Reviewer pattern adds quality

## 🃏 Review Questions

**Q1**: What problem does Sand Castle solve that existing tools did not?
**A**: Existing AFK agent solutions required third-party services or had unreliable Docker setups; Sand Castle provides a simple TypeScript-native `run()` primitive that orchestrates any agent inside any sandbox, owning the process programmatically.

**Q2**: How does the planner-implementer-reviewer-merger pipeline work?
**A**: A planner agent reads unblocked GitHub issues and outputs a JSON plan; parallel implementer agents each work on one issue in separate Docker sandboxes; reviewer agents check each branch; a merger agent resolves conflicts and merges all branches back to main.

**Q3**: Why is the reviewer agent pattern described as particularly powerful?
**A**: Implementers make mistakes that a fresh-context reviewer reliably catches; running reviewer and implementer as separate agents (optionally with different models) creates an adversarial quality check without requiring human intervention.
