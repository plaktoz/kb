---
source_url: https://code.visualstudio.com/docs/agents/guides/context-engineering-guide
author: Unknown
date: 2026-08-05
---

# Set up a Context Engineering Flow in VS Code

Context engineering is a systematic approach to giving AI agents targeted project information to improve generated code quality. The workflow has three main steps:

## Step 1: Curate Project-Wide Context

Create Markdown documentation files (`PRODUCT.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md`) and reference them in `.github/copilot-instructions.md`. This file is automatically included in all chat interactions. Keep it concise — "start small" and only add rules when the agent repeatedly makes the same mistakes.

## Step 2: Create an Implementation Plan

Build a `plan-template.md` with sections for architecture/design, tasks, and open questions. Then create a custom planning agent (`.github/agents/plan.agent.md`) configured with read-only codebase tools and optional GitHub MCP server integration. A prompt file variant can add a clarification step before planning begins.

## Step 3: Generate Implementation Code

Reference the saved plan file in a new chat (e.g., `implement #<my-plan>.md`). For structured workflows, a dedicated TDD implementation agent can enforce test-first development patterns.

## Key Best Practices

- **Progressive context building:** Add detail gradually rather than overwhelming the model upfront
- **Separate concerns:** Use distinct agents for planning, coding, and review
- **Handoffs:** Transition between agents using configured handoff prompts
- **Avoid context dumping:** Unfocused, excessive information dilutes the agent's focus
- **Watch credit usage:** Larger context and deeper agent chains increase token consumption
- **Version your setup:** Track changes to instructions/agents via git

A well-tuned setup should reduce back-and-forth corrections, produce more consistent code, and help the AI make better architectural decisions aligned with project goals.
