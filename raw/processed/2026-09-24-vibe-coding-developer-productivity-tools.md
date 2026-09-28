---
source_url: https://mikemcquaid.com/vibe-coding-developer-productivity-tools/
author: Mike McQuaid
date: 2026-09-24
---

# Vibe Coding Developer Productivity Tools

The piece opens by referencing a prior April 2026 post about the author's agentic workflow using Superset, Fork, and Zed. McQuaid explains he has now moved away from those tools by building his own application called AgentIDE, describing it as "an 'agentic IDE' built by me just for my workflows."

## Agents and Worktrees

McQuaid describes submitting pull requests to Superset to adjust it to his preferences, but lists core issues: his preference for native macOS/Swift tools, his use of a tool called Sandvault that didn't integrate with Superset, a desire to run workflows remotely without trusting third-party services, and a licensing concern — he later "realised (quite late) that Superset isn't under a 'real' (OSI compatible) open source software licence." He notes this reflects no criticism of the Superset team.

## Vibe Engineering

He recruited his brother, more experienced in Swift, to help design the architecture, emphasizing strict compile-time checks, static analysis, and testing. Using "Claude Max and Anthropic's Fable 5 model," he had a working prototype after roughly four hours over one weekend, fully replaced Superset within two weeks, and largely replaced Fork and Zed a week later. The tool relies on several underlying utilities: Sandvault (`sv`) for sandboxing, GitHub's `gh` CLI, a session multiplexer called `herdr`, `mosh` for remote performance, Homebrew (`brew`) for installation, and an iOS SSH client called Moshi. He mentions adopting macOS "Golden Gate Public Beta" and using Apple's local models, later open-sourcing AgentIDE for installation via Homebrew.

## AgentIDE Flow

The tool uses a three-pane layout: a sidebar listing repositories/worktrees with branch/PR status, a middle pane for interacting with sandboxed coding agents (OpenAI Codex or Claude Code), and a right pane for code review, PR viewing, editing, shell access, browsing, and logs. A typical workflow involves creating worktrees from prompts or issues, reviewing agent output, opening PRs, responding to CI/review feedback, and merging.

## Results

McQuaid reports increased productivity, reduced frustration, and benefits extended to coworkers and comaintainers. He reflects that agentic coding has made building personalized tools remarkably accessible, stating he has "not (deliberately) read a single line of Swift code" for the project, relying instead on sandboxing and user-separation for trust boundaries. He also describes building a second tool, MinMaxCal, as a replacement for a paid meeting-reminder app, noting it required minimal maintenance ("less than an hour in months").

## Future

He closes by expressing growing impatience with software friction, a commitment to open-source contribution where possible, and an intention to build personal replacements when contribution isn't feasible, encouraging readers to consider similar approaches for their own workflows.
