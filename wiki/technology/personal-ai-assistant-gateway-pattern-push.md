---
type: literature-note
source_url: https://www.youtube.com/watch?v=lmmgzIuWEbk
author: Owain Lewis
tags: [ai-agents, personal-assistant, gateway-pattern, messaging, claude-code, codex]
date_consumed: 2026-07-17
---

## Summary

[[Owain Lewis]] replaced Hermes Agent and OpenClaw with **Push**, a minimal Rust gateway that routes messages from Telegram or iMessage to an existing coding agent (Codex, Claude Code, or Pi Agent). The core argument is that the distinctive value of tools like Hermes was the messaging gateway, not the backend — and now that [[Claude Code]] and [[Codex]] natively support background jobs, memory, and phone access, building a custom agent runtime adds complexity without benefit. The critical failure modes of Hermes were automatic memory saving stale/false facts and auto-skill creation generating junk instructions that degraded performance over time.

## Core Concepts

- **[[Personal AI Assistant Gateway Pattern]]** — a lightweight process that polls a messaging platform (Telegram, iMessage) and dispatches incoming messages to a coding agent runtime; no inbound ports or webhooks needed
- **[[Push Gateway]]** — single Rust binary; configures one channel (Telegram/iMessage), an agent runtime, a `soul.md` personality file, an `agent.md` context file, and a jobs directory; all stored in a version-controlled repo
- **[[Automatic Memory Pitfall]]** — agents writing facts to a `memory.md` file after each turn; stale, false, or one-off comments accumulate and confuse subsequent turns; the agent cannot distinguish a current fact from an outdated offhand remark
- **[[Auto-Skill Creation Pitfall]]** — agents generating reusable skill files on the fly; junk skills multiply and force the agent to evaluate whether to load each one every turn, degrading overall performance
- **[[Task List as Control Plane]]** — framing the to-do list as the delegation interface: each item can be picked up by a human or handed to an agent; keeps work visible and reviewable
- **[[Polling vs. Webhook Security]]** — long-polling Telegram means no exposed inbound ports; gateway can run in a private network with no internet-facing surface
- **[[Workspace Integration Pattern]]** — connecting the agent to writing apps (e.g., Passage), task managers (Todoist), email, and GitHub so outputs land in the places the user already checks; avoids context disconnection between agent and workspace
- **[[Soul.md / Agent.md Pattern]]** — `soul.md` defines assistant personality and working style; `agent.md` is read by the coding agent and specifies available tools, priorities, and working rules

## Key Takeaways

- **Coding agents absorbed most of Hermes' features**: background cron jobs, phone access, and memory are now first-class features of Claude Code and Codex — the only unique value Hermes offered was the gateway layer
- **Automatic memory creates noise, not knowledge**: facts saved without human review accumulate errors over time; explicit, version-controlled context files (soul.md, agent.md) are more reliable than autonomous memory writes
- **More skills = worse agent performance**: each skill file is evaluated on every turn; a bloated skill library generates confusion and inconsistency — prefer fewer, well-defined skills
- **Credential management is a hidden cost of custom backends**: building Gmail/OAuth into a self-hosted agent requires managing refresh tokens and secrets; using Codex or Claude Code offloads this to the provider with consumer-grade security
- **Scheduled jobs as version-controlled cron**: defining recurring jobs (email triage, weekly review, research fetch) as plain text in a repo makes them auditable, testable, and portable across machines
- **Task list as the delegation interface**: rather than issuing ad hoc commands, treat the task list as the canonical queue; the agent picks up items and reports back, keeping the human in review mode not execution mode
- **Simple configuration beats featureful configuration**: Hermes and OpenClaw have many options and platforms — Push has two channels, a configurable agent runtime, and a soul file; easier to understand and extend

## Related Notes

- [[agentic-engineering-subagents]] — subagent dispatch and context isolation
- [[best-practices-building-ai-agents]] — deterministic scaffolding, external state, scope control
- [[ai-agents-claude-skills-methodology]] — skill design principles
- [[building-effective-ai-agents-anthropic]] — Anthropic's agent design guidance
