---
source_url: https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide/
author: Lushbinary Team
date: 2026-06-09
---

# Loop Engineering: Designing Systems That Prompt AI Agents

Loop engineering represents a fundamental shift in how developers work with AI coding agents — moving from manually typing each prompt to designing autonomous systems that do the prompting. The concept was popularized by Google engineer Addy Osmani, drawing on observations from Peter Steinberger and Anthropic's Boris Cherny, who noted his job had become writing loops rather than prompting models directly.

## Core Concept

Rather than steering an agent turn-by-turn, a loop engineer builds an outer control structure that:
- Fires on a schedule
- Discovers and triages work
- Dispatches sub-agents
- Verifies results
- Persists state between runs

## Three-Layer Stack

| Layer | What you optimize | Unit of work |
|---|---|---|
| Prompt engineering | Phrasing a single instruction | One manual turn |
| Context engineering | What surrounds the answer | Conditions around one response |
| Loop engineering | The system deciding what/when to prompt | Self-running multi-turn cycle |

## The Ralph Technique (Origin Story)

Geoffrey Huntley demonstrated the concept early using a plain `while` loop: feed the same prompt against a spec, let the agent do one task and commit, then reset context and repeat. Named after the Simpsons character for being "deterministically simple in an unpredictable world." Key insight: intelligence lives in clear specs and verifiable outcomes, not heroic single sessions.

## Five Building Blocks + Memory

1. **Automations** — scheduled triggers for discovery/triage
2. **Worktrees** — isolated git checkouts preventing agent collisions
3. **Skills** — documented project knowledge so agents stop guessing
4. **Connectors/Plugins** — MCP-based links to real tools (issue trackers, Slack, APIs)
5. **Sub-agents** — separate maker from checker; the model that wrote code shouldn't grade it

**Plus Memory:** A durable external state file (markdown, Linear board, GitHub issues) that survives between runs, since the model forgets everything between sessions.

## Four Loop Rungs (Anthropic's Taxonomy)

| Rung | Trigger | What you hand off |
|---|---|---|
| Turn-based | You, after each reply | Single-step verification |
| Goal-based | Verifiable success condition (`/goal`) | Deciding when work is done |
| Time-based | External schedule/event | Remembering to start work |
| Proactive | The loop itself | Deciding what to work on |

## Stop Conditions: Write Like a Contract

Weak goal: *"Improve test coverage"*
Strong goal: specify end state, required evidence, constraints, and a hard turn/budget ceiling. A separate verifier model should grade completion — not the agent that did the work.

## Tool Implementations

**Claude Code:** `/loop`, `/schedule`, cloud Routines (cron, webhook, GitHub events), `/goal`, hooks, worktree isolation, sub-agents in `.claude/agents/`

**OpenAI Codex:** Automations tab, `/goal` (CLI 0.128.0+), built-in worktrees, TOML-defined sub-agents in `.codex/agents/`

Both tools use MCP for connectors and share nearly identical structural primitives.

## Adoption Maturity Ladder

| Level | Loop behavior | Human involvement |
|---|---|---|
| 0. Manual | Turn-by-turn prompting | Every turn |
| 1. Triage | Scheduled findings, no code changes | Read and act on findings |
| 2. Draft | Branch + worktree drafts | Review/merge every PR |
| 3. Verified PR | Verifier sub-agent gates PRs | Approve; verifier filters |
| 4. Auto-merge | Low-risk changes merge on green | Audit logs, not each change |

## Key Risks

- **Verification gap:** An unattended loop also makes mistakes unattended
- **Comprehension debt:** Code ships faster than human understanding grows
- **Cognitive surrender:** Accepting loop output without judgment — "same action, opposite result" depending on the engineer's intent

The article emphasizes: "Build the loop like someone who intends to stay the engineer, not just the person who presses go."
