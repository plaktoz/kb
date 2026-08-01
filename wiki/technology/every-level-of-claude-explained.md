---
type: literature-note
source_url: [https://www.youtube.com/watch?v=ZRb7D6R64hM, https://www.youtube.com/watch?v=XTWb5oEfqdY]
author: Nate Herk | AI Automation
tags: [claude-ai, claude-code, agentic-workflows, ai-productivity]
date_consumed: 2026-07-29
---

## Summary

Nate Herk maps five progressive levels of [[Claude]] mastery—from casual chat queries (Level 1) through project-based contextual memory and file creation (Level 2), to computer-operating co-work with skills and scheduled tasks (Level 3), parallel [[Claude Code]] sessions using worktrees and sub-agents (Level 4), and finally fully autonomous cloud routines, hooks, and agent teams running without any human session (Level 5). At each level he identifies the ceiling that stalls most users and provides a specific "cheat code" to break through.

## Core Concepts

- **Level 1 — The Enthusiast**: Treats Claude as a search bar; unlocking move is attaching screenshots (Claude reads images).
- **Level 2 — The Beginner**: [[Claude Projects]] with persistent memory, connectors (Slack, Google Drive, GitHub, Notion), file creation (Excel/PPT/Word), persistent-storage [[Artifacts]], inline visuals, and Microsoft Office add-ins.
- **Level 3 — The Intermediate**: [[Claude Co-work]] (desktop app with file-system access); reusable [[Claude Skills]] (markdown workflow files); scheduled tasks; mobile dispatch; [[Claude Design]] (Figma competitor generating brand-consistent prototypes/landing pages).
- **Level 4 — The Advanced**: [[Claude Code]] in terminal or desktop; [[CLAUDE.md]] file that self-trains over time; plan mode (Shift+Tab twice, with [[Opus Plan]] using Opus for planning and Sonnet for execution); [[Sub-agents]] for parallel specialized tasks; [[Git Worktrees]] for isolated parallel feature branches; [[MCP]] (prefer CLI over MCP when CLI available — 60-70% fewer tokens); `/compact`, `/context`, `/rewind`, `/branch`, `/insights` commands.
- **Level 5 — The Architect**: [[Claude Routines]] (cloud-scheduled Code configs, machine-off); lifecycle [[Hooks]] (pre-tool-use safety rails, post-edit auto-format, stop-notification Slack pings); [[Channels]] (Discord/Telegram/iMessage triggering Claude); [[Headless Mode]] (`claude -p`); [[Agent SDK]] (Python/TypeScript); [[Agent Teams]] (specialized Claudes coordinated by a lead, can message each other via A2A protocol); [[Remote Control]] (phone-to-desktop session bridge); [[Auto Dream]] (background memory consolidation sub-agent pruning stale facts).
- **Boris Cherny** (Claude Code creator at [[Anthropic]]): runs 5 parallel sessions daily; credits the verification loop (Claude tests its own UI via Chrome extension) as 2-3x quality multiplier.
- **[[A2A Protocol]]**: Agent-to-agent communication standard from Anthropic and Google for multi-agent coordination.
- **[[Task Budgets]]**: Beta feature on Opus 4.7 (API-only) — token target for entire run; model self-regulates and wraps up gracefully near budget.
- **Pricing tiers**: Free (basic features with usage limits) → Pro $20/mo (power-user + agentic) → Max $100–$200/mo (heavy/parallel workloads).
- **[[Extended Thinking]]**: Step-by-step reasoning mode; noticeably better for strategic, financial, or multi-step reasoning tasks.
- **[[Research Mode]]**: Autonomous multi-source web research (5–45 min per task) — not a single web search query.
- **Connectors directory**: Full integration list at `claude.ai/directory`; highest ROI connects to where actual work lives (Gmail, Drive, Slack, Notion).

## Key Takeaways

- **Level 1 unlock**: Use screenshots instead of typing out what's on screen.
- **Level 2 unlock**: Create a project with a system prompt and reference docs once; all chats start preloaded.
- **Level 3 unlock**: Claude Co-work gives real file-system read/write to granted folders.
- **Level 4 unlock**: CLAUDE.md self-trains; tell Claude to update it after every mistake.
- **Level 5 unlock**: Trust, not tech — start with low-stakes deterministic routines, observe for weeks, then expand.
- **CLI beats MCP**: When a CLI exists (GitHub, AWS), use it — 60-70% fewer tokens than MCP.
- **Opus Plan mode**: Opus plans, Sonnet executes — halves cost without quality loss.
- **Context management**: Run `/compact` proactively (not when warnings appear); prompt caching drops costs 60-90% on long sessions.
- **Non-coders can ship**: Claude Design → Claude Code pipeline enables idea-to-production with zero code written.
- **Agent teams**: Still experimental but multiple Claudes can debate, share findings, and coordinate via shared task lists.
- **Memory import hack**: Paste memory from ChatGPT directly into Claude's memory system to transfer context cross-platform.
- **Upgrade path**: Start free → hit limits → Pro ($20) → hit Pro limits → Max ($100+).

## 🧠 First Principles & Mental Models

- **[[Progressive Automation]]**: Each level adds one degree of autonomy; Herk's framework mirrors the principle that trust must be earned incrementally before handing off full control — start with supervised, deterministic tasks before deploying autonomous cloud agents.
- **[[Minimum Viable Context]]**: CLAUDE.md and folder structure serve as externalized working memory; the principle that systems perform better when they start every session with the right context rather than rebuilding it from scratch is a direct application of reducing cognitive load.
