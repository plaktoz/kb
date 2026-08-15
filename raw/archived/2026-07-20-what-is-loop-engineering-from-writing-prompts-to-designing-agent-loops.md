---
source_url: https://smartscope.blog/en/generative-ai/methodology/loop-engineering-agent-loops-2026/
author: Unknown
date: 2026-07-20
---

# What Is Loop Engineering? From Writing Prompts to Designing Agent Loops

Loop engineering is a discipline that emerged in June 2026, sparked by a viral post from Peter Steinberger, and formalized by Addy Osmani. Rather than manually typing each prompt to an AI coding agent, loop engineering means designing the *system* that does the prompting automatically.

The core idea: move the human out of the repetitive "what next?" role and replace that judgment with a structured control system. Boris Cherny (Claude Code lead) described this shift as writing loops that prompt Claude and decide next steps, rather than prompting Claude directly.

## The Four-Layer Progression

| Layer | Era | Focus |
|---|---|---|
| Prompt engineering | ~2024 | Single exchange quality |
| Context engineering | 2025 | Full token environment |
| Harness engineering | Early 2026 | Execution environment |
| Loop engineering | June 2026+ | System driving the harness repeatedly |

## Six Loop Design Elements

- **Trigger** – what starts it
- **Context** – what the agent sees
- **Action** – what it's allowed to do
- **Verification** – how success is measured
- **Memory** – durable state outside the conversation
- **Escalation** – when humans regain control

## Key Cautionary Finding

A real-world field report showed a loop that auto-deleted 129 stale branches successfully, while a PR-monitoring loop generated 43 commits in a single day — most rejected due to scope drift. The takeaway: a poorly designed loop "can mass-produce waste at high speed."

## Central Argument

The hard part isn't autonomy — it's verification, stopping conditions, and human escalation. Building a loop is becoming easy; deciding what responsibility the human retains beforehand is not.
