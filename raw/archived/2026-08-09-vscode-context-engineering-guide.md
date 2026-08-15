# Set up a Context Engineering Flow in VS Code

Source: https://code.visualstudio.com/docs/agents/guides/context-engineering-guide

## Overview

Context engineering is a systematic approach to providing AI agents with targeted project information to improve code quality and accuracy. The workflow uses custom instructions, custom agents, and prompt files.

## The Three-Step Workflow

1. **Curate project-wide context** – add architecture/design docs as persistent AI context
2. **Generate an implementation plan** – use a planning agent to create detailed feature plans
3. **Generate implementation code** – produce code from the plan following your guidelines

---

## Step 1: Curate Project-Wide Context

Create Markdown documentation files in your repo:

- `PRODUCT.md` — product functionality overview
- `ARCHITECTURE.md` — system architecture and design principles
- `CONTRIBUTING.md` — developer guidelines and best practices

Then create `.github/copilot-instructions.md` to auto-include context in all chat interactions:

```markdown
# [Project Name] Guidelines

* [Product Vision and Goals](../PRODUCT.md)
* [System Architecture and Design Principles](../ARCHITECTURE.md)
* [Contributing Guidelines](../CONTRIBUTING.md)

Suggest to update these documents if you find any incomplete or conflicting information.
```

> **Tip:** Start small. Focus on high-level architecture and add rules only when the agent makes repeated mistakes.

---

## Step 2: Create Implementation Plan

### Plan Template (`plan-template.md`)

```markdown
---
title: [Short descriptive title]
version: [optional]
date_created: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
---
# Implementation Plan: <feature>
[Brief description of requirements and goals]

## Architecture and design
Describe high-level architecture and design considerations.

## Tasks
Break down into smaller tasks using Markdown checklist format.

## Open questions
Outline 1-3 open questions that need clarification.
```

### Planning Agent (`.github/agents/plan.agent.md`)

```markdown
---
description: 'Architect and planner to create detailed implementation plans.'
tools: ['web/fetch', 'read/problems', 'search/codebase', 'search/usages', 'todo', 'agent', 'github/github-mcp-server/get_issue']
handoffs:
- label: Start Implementation
    agent: tdd
    prompt: Now implement the plan outlined above using TDD principles.
    send: true
---
# Planning Agent

You are an architect focused on creating detailed and comprehensive implementation plans...

## Workflow
1. Analyze and understand: Gather context from the codebase and documentation.
2. Structure the plan: Use the provided implementation plan template.
3. Pause for review: Iterate and refine based on user feedback.
```

### Optional Clarifying Prompt (`.github/prompts/plan-qna.prompt.md`)

```markdown
---
agent: plan
description: Create a detailed implementation plan.
---
Briefly analyze my feature request, then ask me 3 questions to clarify the requirements. Only then start the planning workflow.
```

Use `/plan-qna add a customer details page...` to invoke this workflow.

---

## Step 3: Generate Implementation Code

For smaller tasks, prompt the agent directly from the plan. For complex features, save the plan to a file (e.g., `my-feature-plan.md`) and reference it:

```
implement #<my-plan>.md
```

### TDD Implementation Agent (`.github/agents/tdd.agent.md`)

```markdown
---
description: 'Execute a detailed implementation plan as a test-driven developer.'
---
# TDD Implementation Agent

## Test-driven development
1. Write/update tests first
2. Implement minimal code to satisfy tests
3. Run targeted tests after each change
4. Run full test suite before moving to next task
5. Refactor while keeping all tests green

## Success criteria
* All planned tasks completed
* Tests passing (unit, integration, full suite)
```

---

## Best Practices

### Context Management
- **Start small and iterate** — avoid context overload
- **Keep context fresh** — stale docs lead to bad suggestions
- **Maintain context isolation** — separate planning, coding, and debugging sessions
- **Be mindful of credit usage** — more context means more token consumption

### Documentation Strategies
- Treat custom instructions and agents as living documents
- Prioritize information that aids architectural decision-making
- Reference external documentation and APIs when relevant

### Workflow Optimization
- Use **handoffs** between planning, implementation, and review agents
- Version your context setup in git
- Use the **Cache Explorer** to verify prompt cache hit rates

### Anti-Patterns to Avoid
- **Context dumping** — unfocused information dilutes AI focus
- **Over-engineering agent chains** — deep subagent nesting multiplies token costs
- **Neglecting validation** — always verify the AI understands context before proceeding

### Measuring Success
- Reduced back-and-forth corrections
- Consistent code following established patterns
- Faster implementation with less context re-explanation
- Better architectural alignment with project goals

---

## Related Resources
- [Instructions files](https://code.visualstudio.com/docs/agent-customization/custom-instructions)
- [Custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents)
- [Prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files)
