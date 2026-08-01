---
type: literature-note
source_url: https://www.youtube.com/watch?v=AbpyqAfxZ8c
author: Owain Lewis
tags: [ai-agents, software-factory, agentic-engineering, ci-cd, github, codex, claude-code]
date_consumed: 2026-07-25
---

## Summary

[[Owain Lewis]] demonstrates a fully automated software factory built with an open-source Rust tool called **Factory**, which polls GitHub issues for labels, spawns agents in isolated Git worktrees, and moves work through triage, implementation, testing, and pull-request stages without manual terminal interaction. The analogy to [[CI/CD]] is central: just as CI/CD automated deployment and raised quality floors for entire teams, software factories can standardize and automate the mechanical portions of the development cycle — particularly bug fixes, dependency upgrades, and well-specified feature tickets. Human judgment remains essential for design, planning, and review.

## Core Concepts

- **[[Software Factory]]** — an automated pipeline where agents handle the full task-to-PR cycle: ticket intake → triage (spec refinement) → implementation → tests → code review → pull request, triggered by GitHub label changes
- **[[Label-Based Triggers]]** — labels (`factory-ready-for-spec`, `factory-ready-to-implement`) on GitHub issues act as state transitions; Factory polls for these labels and dispatches the matching workflow agent
- **[[Git Worktree Isolation]]** — each agent spawn gets its own isolated Git worktree, preventing interference between concurrent tasks; Docker sandbox is the production alternative for full filesystem isolation
- **[[Triage Workflow]]** — an agent reads a vague GitHub issue, researches the codebase, reproduces the problem or clarifies intent, and rewrites the ticket with outcome, context, acceptance criteria, and implementation notes — turning it into an agent-ready spec
- **[[Implement Workflow]]** — a step-by-step prompt script that guides an agent through: read ticket → plan → implement → run tests → review → address CI findings → open PR; ~35 min for a non-trivial change
- **[[Scheduled Bug Finder]]** — a scheduled workflow that spawns an agent to audit the codebase for latent bugs, then opens a GitHub issue with findings; can be run manually or on a cron
- **[[Task-to-PR Skill]]** — a reusable workflow definition (not just a prompt) that encodes the full development process; the agent runs through it step-by-step, ensuring consistency across all contributors
- **[[CI/CD Analogy for Agent Pipelines]]** — before CI/CD, deployments were manual, error-prone, and stressful; CI/CD standardized the release process and raised the quality floor for every developer regardless of seniority; software factories do the same for implementation

## Key Takeaways

- **Workflow definition beats agent capability**: the agents (Codex, Claude Code) are largely commodities at this point — the durable value is the workflow definition that orchestrates what steps to follow, not which agent runs them
- **Label-as-state-machine**: using GitHub labels to move tickets through stages (intake → spec → implement → done) gives a human-readable, version-controlled pipeline state; no proprietary orchestration platform needed
- **Git worktrees for local isolation**: run one worktree per concurrent agent task; each agent gets a clean branch and working directory; merge or discard cleanly after review
- **Triage agent pays for itself**: a vague customer issue or engineer request fed through the triage workflow produces a spec with reproduction steps, affected files, and acceptance criteria — dramatically reducing agent confusion in the implement step
- **Token efficiency through determinism**: Factory only invokes agents when a labeled ticket exists; all polling and state-tracking is deterministic code with near-zero token cost
- **Factory is a quality floor, not a replacement for judgment**: mechanical work (security upgrades, bug fixes, refactors with clear acceptance criteria) maps well to agent pipelines; design decisions, cross-cutting concerns, and novel features still require human-in-the-loop thinking
- **Sandboxing is a hard open problem**: Git worktrees are safe for local use; Docker sandboxes add filesystem isolation for team environments — neither is a complete solution; treat sandboxing strategy as a first-class architectural decision
- **CI/CD raised deployment quality for every skill level — software factories can do the same for implementation**: a junior developer using the same pipeline as a senior engineer gets the same code review, test runs, and PR discipline

## Related Notes

- [[agentic-design-patterns-loops-beat-single-pass]] — iterative loops and multi-pass agent design
- [[humans-agents-software-engineering-loops]] — human-in-the-loop patterns for software engineering
- [[agentic-engineering-subagents]] — subagent dispatch and worktree-style isolation
- [[best-practices-building-ai-agents]] — deterministic scaffolding, scope control, sandboxing
- [[personal-ai-assistant-gateway-pattern-push]] — same author's personal assistant gateway built on the same agent-dispatch philosophy
