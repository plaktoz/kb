---
type: literature-note
source_url: https://www.youtube.com/watch?v=ZMehQM2sEjI
author: Owain Lewis
tags: [ai-agents, terminal-tools, developer-workflow, multi-agent, coordinator-pattern, herdr]
date_consumed: 2026-08-02
---

## Summary

Herdr is a terminal multiplexer built specifically for AI developers who run multiple coding agents concurrently. Unlike tmux or cmux, Herdr registers agents (Claude Code, Codex, etc.) as first-class entities, showing their active/idle state and surfacing completion notifications. Owain Lewis demonstrates a coordinator pattern where a single `/ticket` slash command creates a new Herdr tab, git branch, and worktree per GitHub issue — enabling systematic, parallel, and repeatable agent-driven development.

## Core Concepts

- **[[Herdr]]** — agent-first terminal multiplexer; supports mouse interaction, workspace/project grouping, pane splits, and native agent status tracking
- **[[Terminal Multiplexer]]** — tool for managing multiple terminal panes/tabs in one session; Herdr is the AI-native alternative to tmux/cmux
- **[[Coordinator Pattern]]** — orchestrator agent (Claude Code) receives a ticket number, creates a new tab + git branch + worktree in Herdr, then hands off to a worker agent; scales to parallel tickets
- **[[Git Worktree]]** — per-ticket isolated working directory; core mechanism that allows parallel agent work without branch conflicts
- **[[Agent Skill File]]** — Herdr-specific guide that can be injected into any coding agent's context, teaching it how to control Herdr via CLI
- **[[Milestone Pattern]]** — extension of coordinator pattern: hand an entire milestone (group of related tickets) to the coordinator; it spins up parallel tabs and implements all tasks, then merges

## Key UI and Key Bindings

| Action | Key Binding |
|--------|-------------|
| Escape to terminal / main menu | `prefix` + `Q` |
| Split pane vertically | `prefix` + `V` |
| Split pane horizontally | `prefix` + `-` |
| New tab | `prefix` + `C` |
| Navigate panes (left/right) | `prefix` + `H` / `L` |
| Swap pane order | `prefix` + `Shift` + `L` |
| Show all key bindings | `prefix` + `?` |

- Prefix key: `Ctrl` + `B`
- Mouse click navigation is supported (unusual among multiplexers)

## Coordinator Pattern: `/ticket` Workflow

1. Operator opens Claude Code in a coordinator tab
2. Runs `/ticket <github-issue-number>` (custom slash command)
3. Coordinator:
   - Creates a new Herdr tab named after the issue number
   - Creates a new git branch + git worktree for that issue
   - Spins up a worker agent (Claude Code or Neo) in the new tab
   - Pastes the issue-specific prompt into the worker
4. Operator runs `/ticket <another-issue>` for a second task in parallel
5. Both agents work independently; completion notifications appear in the agent panel

### Key Properties
- **Repeatable**: same workflow every time, no ad-hoc prompting
- **Organized**: each ticket gets its own tab, branch, and worktree — no cross-contamination
- **Scalable**: 5–6 parallel tasks simultaneously is practical
- **Agent-agnostic**: demonstrated with Claude Code and Neo; any CLI agent works

## Agent-Controlled Configuration

- Agents can manage Herdr config directly (e.g., "read this guide and update my config to use the rose pine theme, then reload")
- Herdr provides a structured guide document that can be passed to any agent as context

## Milestone Extension

- Group related tickets into a milestone
- Pass the entire milestone to the coordinator: "implement all tasks in separate tabs, merge when done"
- Appropriate for personal/experimental projects; more oversight needed for production systems

## Key Takeaways

- **Agent-first design**: Herdr treats agents as registered entities with visible state, not just background processes
- **Systemize repetitive flows**: the `/ticket` pattern eliminates ad-hoc variation; repeatability reduces cognitive overhead and errors
- **Parallel work is the unlock**: worktree-per-ticket is the technical primitive that makes true parallelism safe
- **Tool control via agent**: using the agent to configure Herdr itself is a recursive but practical pattern — agents should manage their own environment
- **Graduated autonomy**: small bug fixes → parallel tickets → full milestones; operator stays more in-loop for bigger tasks

## Links

- [[agent-loops-goals-schedules-claude-code-codex]] — Owain Lewis's companion guide on goals, loops, and schedules in Claude Code and Codex
- [[agentic-engineering-subagents]] — subagent patterns for parallel work
- [[12-claude-code-features-every-engineer-should-know]] — Claude Code feature reference
- [[humans-agents-software-engineering-loops]] — "on the loop" oversight model that the coordinator pattern implements
