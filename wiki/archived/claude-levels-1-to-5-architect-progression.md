---
type: literature-note
source_url: https://www.youtube.com/watch?v=ZRb7D6R64hM
author: Nate Herk | AI Automation
tags: [claude, claude-code, agentic-ai, skill-progression, routines, hooks, worktrees, context-window]
date_consumed: 2026-08-02
---

## Summary

Nate Herk maps 400+ hours of Claude usage into a five-level progression from casual enthusiast to autonomous architect. Each level has a concrete ceiling and a cheat code to break through. The upper levels (4–5) focus on [[Claude Code]] engineering patterns — [[CLAUDE.md]], [[Plan Mode]], [[Git Worktrees]], [[Sub-agents]], [[MCP]] token economics — and shift to fully autonomous infrastructure via routines, hooks, and channels that run without a human session.

## Five Levels at a Glance

| Level | Label | Ceiling | Weekly time saved |
|-------|-------|---------|:-----------------:|
| 1 | Enthusiast | Treats Claude as a search bar | ~30 min |
| 2 | Beginner | Copies outputs manually into other tools | 5+ hrs |
| 3 | Intermediate | Bounded by Claude Co-work's safety rails | 10+ hrs |
| 4 | Advanced | Manually babysitting parallel sessions | Variable |
| 5 | Architect | Trust — not technical skill | Compounding |

## Level 1 — Enthusiast

- Opens Claude, asks a question, closes the tab
- Upgrade: paste screenshots instead of typing descriptions — Claude reads images
- Cheat code: create a [[Claude Projects|Project]] with reference docs and a system prompt; every future chat pre-loads that context

## Level 2 — Beginner

Six features stack on top of Projects:
1. **Memory + past chat search** — remembers preferences, decisions, and past conversations across sessions (memory free; search = paid)
2. **Connectors** — OAuth integrations with Slack, Drive, Gmail, GitHub, Notion, Calendar (50+)
3. **File creation** — real Excel/PowerPoint/Word/PDF downloads from chat (free for all plans)
4. **Artifacts with persistent storage** — apps built in chat that remember data between sessions and self-invoke Claude's API; publishable via public link
5. **Inline visuals** — ephemeral charts/diagrams that update live in conversation; free
6. **Microsoft Office add-ins** — Claude reads multi-tab workbooks, slide masters, and brand colors; cross-app context sharing as of April 2026

## Level 3 — Intermediate (Claude Co-work)

Five features define this level:
1. **[[File System Access]]** — isolated VM with read/write access to granted folders
2. **[[Skills]]** — reusable markdown workflow files; 100+ already published (16+ from Anthropic); same skills work across Co-work, Chat, and Claude Code
3. **Scheduled tasks** — `/schedule` saves recurring tasks; machine must be awake (vs. cloud-based Routines at Level 5)
4. **Mobile control** — Dispatch lets you send tasks from phone while Claude works on desktop
5. **[[Claude Design]]** — Anthropic Labs product (included with Pro); describe → Claude builds and designs prototype/deck/landing page; outputs handoff bundles for [[Claude Code]] or Canva

## Level 4 — Advanced (Claude Code)

Five core patterns:
1. **[[CLAUDE.md]]** — project memory file read every session; keep under 200 lines; update it every time Claude makes a mistake so it self-corrects over time
2. **[[Plan Mode]]** — Shift+Tab twice enters plan mode; "Opus Plan" hidden setting uses Opus for planning and Sonnet for execution, halving cost without quality loss
3. **[[Sub-agents]]** — specialist instances for tests, security, docs; each has its own context window; run in parallel; communicate only through the main session
4. **[[Git Worktrees]]** — `claude --worktree <feature>` creates an isolated branch workspace; 3–4 worktrees is the comfortable parallel sweet spot
5. **[[MCP]] token economics** — CLI-first rule: CLI tools use 60–70% fewer tokens than equivalent MCP servers; MCP's tool-search feature (Jan 2025) auto-defers tool loading when overhead crosses 10% of window, cutting overhead 85%

### Context window power moves (Level 4)

- `/compact` — summarize older history proactively, before warnings appear
- `/context` — show token breakdown by section
- Prompt caching is automatic in Claude Code; combined with compaction, costs drop 60–90% on long sessions
- Auto mode (Shift+Tab to cycle) + `/focus` — hides intermediate steps; how Boris Cherny runs five parallel sessions
- Verification loop: pair Claude Code with a browser extension so Claude tests its own UI and iterates until code and UX both pass
- `/commit-push-PR` custom command — execute entire commit/push/PR flow in one command
- `/rewind` (or Escape×2) — drops a failed attempt out of context, reverts to a prior message
- `/BTW` — asks a quick question mid-task without polluting conversation history
- `/branch` (formerly `/fork`) — creates a conversation fork at the current point for trying alternative approaches
- `/insights` — monthly usage report: wasted tokens, repetitive prompts to turn into skills, CLAUDE.md improvements
- `/output style` — swaps Claude Code's personality (code reviewer, no-fluff, documentation writer)

## Level 5 — Architect

Three pillars of autonomous infrastructure:
1. **[[Claude Routines]]** — saved Claude Code configurations that run on Anthropic's cloud; machine can be off; triggered by schedule, API call, or GitHub events (e.g., auto PR review on pull_request.opened)
2. **[[Hooks]]** — custom logic at lifecycle events: `pre-tool-use` blocks dangerous commands, `post-edit` auto-formats touched files, `stop` pings Slack when a long session finishes
3. **[[Channels]]** — two-way control from Discord, Telegram, or iMessage; external events trigger Claude, or you text Claude to work against your real codebase from your phone

### Additional Level 5 capabilities

- **Headless mode** — `claude -p "<prompt>"` with no human session; pipe output to Slack, Datadog, or another agent
- **Agent SDK** — Python/TypeScript libraries to build products on top of Claude Code's engine
- **Remote control** — `/remote-control` + QR code bridges local session to Claude mobile app; session stays on machine, phone is the remote
- **Auto Dream** — background sub-agent that prunes memory files between sessions: deletes contradicted facts, merges duplicates, converts relative dates to absolute ones
- **Task budgets (Opus 4.7 beta)** — token budget for an entire run (thinking + tool calls + output); model self-regulates and wraps up gracefully; API-only for now
- **[[Agent Teams]] (experimental)** — multiple specialized Claudes coordinated by a lead agent; can message each other, share a task list, debate findings; uses A2A protocol alongside MCP

### Trust is the Level 5 bottleneck

The stall at Level 5 is psychological, not technical. Fix: start with a low-stakes routine that only reports to you. Watch it run for weeks before increasing autonomy. Deterministic data-pipeline automations are safe to trust early; non-deterministic skill/agent runs require more observation time.

## Linked Notes

- [[12-claude-code-features-every-engineer-should-know]] — feature catalog covering CLAUDE.md, hooks, plugins, subagents
- [[agentic-engineering-subagents]] — deep dive on subagent context preservation patterns
- [[claude-ai-full-tutorial-basics-to-agentic-2026]] — complementary three-tier overview (Levels 1–3 framing from different author)
- [[agentic-engineer-workflow-parallel-sessions-2026]] — practitioner parallel-session workflow with effort routing
- [[ai-agents-claude-skills-context-windows]] — skills and context window management patterns
- [[agentic-design-patterns-planning]] — planning patterns for agentic loops
