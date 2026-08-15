---
source_url: https://claude.com/blog/getting-started-with-loops
author: Delba de Oliveira and Michael Segner
date: 2026-06-30
---

# Loop Engineering: Getting Started with Loops

The Claude Code team defines loops as "agents repeating cycles of work until a stop condition is met," categorized by trigger mechanism, stop condition, primitive used, and task type.

## Four Loop Types

1. **Turn-based** – User-prompted; Claude stops when it judges the task complete or needs more context. Best for shorter, exploratory tasks. Improve verification by encoding checks into a SKILL.md file with quantitative criteria.

2. **Goal-based (`/goal`)** – User sets explicit success criteria and a turn cap. An evaluator model checks the condition before allowing Claude to stop. Works best with deterministic criteria like test pass rates or score thresholds.

3. **Time-based (`/loop`, `/schedule`)** – Triggered on an interval; suited for recurring work or polling external systems. `/loop` runs locally; `/schedule` moves execution to the cloud.

4. **Proactive** – Event- or schedule-driven with no real-time human involvement. Combines `/schedule`, `/goal`, skills, dynamic workflows, and auto mode for long-running, well-defined recurring work.

## Quality & Cost Tips

- Keep codebases clean; give Claude self-verification tools
- Use second agents for code review
- Match model size to task complexity; pilot before large runs
- Use `/usage`, `/goal`, and `/workflows` commands to monitor token consumption
