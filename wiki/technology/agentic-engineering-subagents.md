---
type: literature-note
source_url: https://simonwillison.net/guides/agentic-engineering-patterns/subagents/
author: Simon Willison
tags: [agentic-engineering, subagents, context-management, claude-code]
date_consumed: 2026-07-29
---

## Summary

[[Subagents]] let a coding agent dispatch a fresh copy of itself with a clean context window to handle a bounded task, preserving the parent agent's limited context budget — LLM context limits have not grown much even as model quality has, so managing context carefully remains critical. [[Claude Code]]'s "Explore" subagent, run automatically at the start of most tasks, illustrates the pattern: it investigates a repo and returns a condensed summary rather than forcing the parent agent to read every file itself.

## Core Concepts

- **[[Context Window Preservation]]** — the core reason subagents exist: keeping token-heavy exploration or research out of the parent agent's working context
- **[[Parallel Subagents]]** — running multiple subagents simultaneously (potentially on cheaper/faster models like Claude Haiku) for independent tasks like editing unrelated files, yielding a real speed boost
- **[[Specialist Subagents]]** — subagents customized with their own system prompt and tools to take on a role: code reviewer, test runner, or debugger

## Key Takeaways

- **Context limits plateaued**: models keep improving, but usable context windows haven't grown proportionally — benchmarks often show better quality below 200K tokens even when 1M is available
- **Explore-then-report pattern**: a subagent investigates and returns only the relevant summary, not the raw exploration trace
- **Don't over-fragment**: subagents' main value is preserving root context for token-heavy operations — a root agent can usually review or debug its own output if it has budget to spare
- **Role separation aids objectivity**: a dedicated test-runner or reviewer subagent can hide noisy output and report only what matters
