---
source_url: https://every.to/source-code/how-i-polish-software-that-agents-built
author: Kieran Klaassen
date: 2026-07-13
---

# How I Polish Software That Agents Built

Klaassen argues that as AI agents automate the coding work itself, the remaining human contribution is **polish** — the judgment call about whether something actually *feels* right.

He describes a workflow where agents ship overnight pull requests, and his morning job is evaluating quality. When an email card animation "slid in from the top of the screen instead of opening from where I'd clicked," he flagged it, the agent fixed it.

His `/ce-polish` command (part of the [compound engineering plugin](https://github.com/EveryInc/compound-engineering-plugin)) opens the running app beside the agent, enabling a tight feedback loop: use the app → notice what's off → tell the agent → hot-reload → repeat.

Key insights:
- **Polish is non-delegable** — agents can't know what *you* meant to build
- It sharpened his *planning* (writing specs around anticipated feel) and made *reviewing* less stressful
- Crucially, polish feeds back into the system: "the first time I caught the wrong-direction animation, I had to say so" — but the agent applied the rule automatically afterward
- The cost of scrapping and replanning has "all but disappeared," shifting the constraint from shipping speed to shipping *quality*
