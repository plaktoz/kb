---
type: literature-note
source_url: https://mikemcquaid.com/vibe-coding-developer-productivity-tools/
author: Mike McQuaid
tags: [vibe-coding, ai-agents, developer-tools, agentic-ide]
date_consumed: 2026-09-28
---

## Summary

Mike McQuaid describes replacing his prior agentic-coding stack (Superset, Fork, Zed) by building his own native macOS "agentic IDE," AgentIDE, using AI coding agents themselves. He got a working prototype in about four hours over one weekend and fully replaced his previous tools within two to three weeks, crediting agentic coding with making personalized software dramatically more accessible. He closes by encouraging other developers to consider building narrow personal replacements when upstream contribution isn't feasible.

## Core Concepts

- **[[Vibe Coding]]** — building software largely by directing AI coding agents rather than writing code by hand
- **[[AgentIDE]]** — McQuaid's self-built "agentic IDE," a three-pane macOS/Swift app for managing sandboxed coding agents across repos and worktrees
- **[[Mike McQuaid]]** — author; previously used Superset, Fork, and Zed for his agentic workflow before building AgentIDE
- **[[Sandvault]]** — sandboxing utility (`sv`) that AgentIDE relies on for isolating agent execution
- **[[Superset]]** — the third-party agentic tool McQuaid previously used and contributed to, abandoned partly over its non-OSI-compatible license
- **[[Claude Code]]** — one of two coding agents AgentIDE's middle pane supports
- **[[OpenAI Codex]]** — the other coding agent AgentIDE's middle pane supports
- **[[Git Worktree]]** — per-task isolated working directory that AgentIDE creates from prompts or issues
- **[[herdr]]** — session multiplexer used as one of AgentIDE's underlying utilities
- **[[Homebrew]]** — package manager (`brew`) used both to install AgentIDE's dependencies and to distribute AgentIDE itself
- **[[mosh]]** — remote-shell tool used for performant remote sessions, paired with an iOS SSH client called Moshi

## Key Takeaways

- **Fast prototype**: working AgentIDE prototype built in ~4 hours over one weekend.
- **Rapid tool replacement**: fully replaced Superset within two weeks, Fork/Zed a week later.
- **Model and plan used**: built with Claude Max and Anthropic's "Fable 5" model.
- **Licensing concern**: dropped Superset partly because it lacked a "real" OSI-compatible license.
- **Trust via sandboxing**: relied on sandboxing/user-separation rather than reading the Swift code himself.
- **Second tool built**: also built MinMaxCal, a meeting-reminder app needing under an hour of maintenance in months.
- **Open-sourced result**: later open-sourced AgentIDE, installable via Homebrew.

## 🧠 First Principles & Mental Models

- **[[Build vs. Buy]]**: Agentic coding collapses the cost of "build," so McQuaid tips the classic build-vs-buy calculus toward custom personal tools instead of compromising with off-the-shelf software like Superset.

## 🃏 Review Questions

**Q1**: What is the article's core claim about agentic coding tools?
**A**: Agentic coding has made it accessible for a developer to build fully personalized tools — like AgentIDE — tailored precisely to their own workflow, rather than settling for compromises in third-party tools.

**Q2**: What evidence does McQuaid give for how quickly this can happen?
**A**: Using Claude Max and Anthropic's "Fable 5" model with his brother's Swift guidance, he had a working prototype in about four hours over one weekend, and fully replaced Superset within two weeks and Fork/Zed a week after that.

**Q3**: What does McQuaid suggest other developers do with this capability?
**A**: When contributing improvements upstream isn't feasible, he encourages building narrow personal replacements for friction-causing tools, as he did with both AgentIDE and the low-maintenance MinMaxCal app.
