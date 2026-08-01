---
type: literature-note
source_url: https://www.youtube.com/watch?v=KBgZsV-0Fdo
author: Tristen O'Brien
tags: [claude, anthropic, claude-code, claude-cowork, claude-dispatch, ai-tools, ai-productivity]
date_consumed: 2026-08-02
---

## Summary

Tristen O'Brien provides a practical map of the six ways to use [[Claude]] — four distinct product modes and two capability add-ons — arguing that most users only access ~15% of Claude's potential by sticking to basic chat. The guide helps users identify which mode matches their actual task.

## Core Concepts

### Four Product Modes

- **[[Claude Chat]]**: The baseline interface at claude.ai — browser, phone, and desktop, all synced. Best for quick conversations, writing, research, and thinking things through. The foundation on which all other modes build.
- **[[Claude Co-work]]**: Desktop app that reads, edits, and saves files on the local machine. Designed for non-coders — operates as a "24/7 personal employee" that takes tasks and executes them on the actual filesystem. Use cases: triage and draft email replies, organize desktop files, generate shopping lists from web lookups and export to PDF. Key distinction from Chat: Co-work touches real files; Chat only talks.
- **[[Dispatch]]**: Assigns a task to Claude from a mobile phone; Claude executes the work on the user's desktop (at home or in the office) and returns a finished result to the phone. The session is continuous and persistent — a task started on the phone can be followed up on the laptop in the same thread without restarting. Enables asynchronous human-AI collaboration across locations.
- **[[Claude Code]]**: Terminal- or desktop-based tool for building real software. Writes code, runs tests, debugs, and delivers a working application as output. Accessible to non-developers: the user describes what they want; Claude handles implementation. Example: the presenter built 150 AI agents without writing code manually.

### Two Capability Add-ons

- **[[Claude Plugins]]**: Pre-built bundles of tools and connectors installable into Claude — analogous to apps in an app store. Work inside Co-work and Claude Code. Examples: Slack integration enables Claude to send/read messages; design plugins extend generative capabilities. Best for extending Claude without building custom integrations.
- **[[Claude Skills]]**: A folder of markdown instructions that teaches Claude how to execute a specific recurring job. Claude reads the skill file whenever that job comes up. Works across Chat, Co-work, and Code. Can be shared or self-authored. Best for any task done more than once — eliminates re-typing instructions every session.

## Key Takeaways

- **Mode selection rule**: Chat → thinking; Co-work → file-based computer tasks; Dispatch → phone-initiated background tasks; Code → building real software.
- **Plugins extend capability breadth**: Add new tool integrations without building anything new.
- **Skills encode repeatable workflows**: One-time setup that persists across all Claude interfaces.
- **Non-coders are now developers**: Claude Code makes software development accessible to anyone who can describe what they want.
- **Dispatch enables async workflows**: Start a task remotely, continue it later on any device — same thread, same context.

## Distinctions from Related Notes

This note focuses on Claude's specific product surface and the conceptual model for choosing between modes. See [[every-level-of-claude-explained]] for a deeper five-level mastery framework including advanced features (hooks, agent teams, routines), and [[claude-ai-full-tutorial-basics-to-agentic-2026]] for a three-tier beginner-to-agentic walkthrough including pricing.

## Related Notes

- [[every-level-of-claude-explained]]
- [[claude-ai-full-tutorial-basics-to-agentic-2026]]
- [[12-claude-code-features-every-engineer-should-know]]
- [[ai-agents-claude-skills-context-windows]]
- [[ai-agents-claude-skills-methodology]]

## First Principles & Mental Models

- **[[Right Tool for the Task]]**: O'Brien's framework is an application of task-tool matching — users fail not because Claude lacks capability but because they reach for the wrong mode. Knowing the tool's affordances is a prerequisite to productivity.
- **[[Progressive Autonomy]]**: The four modes form a gradient from supervised conversation (Chat) to background autonomous execution (Dispatch/Code) — matching the degree of autonomy to the user's trust and task complexity reduces risk while maximizing leverage.
