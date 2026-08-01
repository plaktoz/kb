# Wayfinder: AI Planning Skill for Multi-Session Large Projects

**Source:** Matt Pocock — "/wayfinder: Nothing is too big to plan anymore" (YouTube)
**Category:** [[Technology]] | AI Agents | Developer Workflow | Planning

---

## Core Idea

Wayfinder is an AI planning skill designed to orchestrate large, ambiguous projects across multiple agent sessions. Unlike single-session planning tools, it models the "fog of war" — the reality that you can't see all steps to your destination upfront.

**Key metaphor:** Planning as map-making. You start with a vague destination and gradually chart a route by resolving decisions, running prototypes, and doing research along the way.

---

## The Problem Wayfinder Solves

Conventional AI planning is constrained to a single context window. For large projects this forces you to artificially shrink scope. Wayfinder instead:
- Accepts that destinations are foggy
- Breaks big work into a **map of decision tickets**
- Each ticket gets its own dedicated agent session
- Allows parallel planning where decisions are independent

---

## How It Works

### The Map
Wayfinder creates and manages a **map** of tickets representing every decision needed to reach the destination. The map distinguishes:
- **Frontier**: decisions ready to be made now (all blockers resolved)
- **Fog**: decisions that can't be made yet — pending research, prototypes, or discussion

The map lives in your issue tracker (GitHub Issues, Linear, Jira — tracker-agnostic).

### Four Ticket Types

| Type | Purpose |
|------|---------|
| **Research** | Agent goes off autonomously to gather information; runs in a sub-agent |
| **Prototype** | Creates a working artifact to get high-fidelity feedback before full build |
| **Grilling** | Discussion session to clarify an implementation detail or direction |
| **Task** | Real-world actions the agent can handle or that need human execution |

### Blocking Relationships
Tickets can block other tickets. This models the reality that some decisions depend on others. Wayfinder tracks the frontier so you always know which tickets are actionable next.

---

## Workflow

1. **Invoke Wayfinder with your destination** — describe what you want to achieve
2. Wayfinder grills you, explores the repo/context, and generates an initial map with sub-tickets
3. **Work through tickets** one at a time, each in its own session: call `wayfinder <ticket-url>`
4. Each resolved ticket may unlock new frontier tickets
5. Once the map is complete, generate a **spec** from the map
6. Feed spec into your normal implementation pipeline (spec → tickets → implement → code review)

> Specs in this workflow are *non-persistent destination documents* — close and discard them once the code reflects the decisions. The decision tickets are the primary source of truth.

---

## Prototypes as Anti-Waterfall

A concern with heavy upfront planning is that it resembles waterfall. Wayfinder counters this with prototype tickets:
- Low-fidelity decisions accumulate in the map
- Prototype tickets inject high-fidelity feedback checkpoints
- The spec quality is higher because it's grounded in real artifacts

---

## When to Use Wayfinder

**Use it when:**
- The project is too large to plan in a single session
- You have fog — you don't fully know the path to your destination
- Work spans multiple domains requiring research, prototyping, and discussion

**Skip it when:**
- The work is completable in a single session
- You already know the path clearly

**Non-coding applications:** Works for any ambitious multi-step planning — Pocock has used it for engineering work, course planning, and commissioning a garden office.

---

## Wayfinder vs. Grill-with-Docs

| | Grill-with-Docs | Wayfinder |
|-|----------------|-----------|
| Scope | Single session | Multi-session |
| Planning depth | Light grilling → spec | Deep map → spec |
| Primary source | Spec (summary) | Decision tickets (raw) |
| Prototyping | No | Yes |

Wayfinder replaces the "grill with docs" step in the spec-driven development pipeline for large, foggy work.

---

## Related Notes
- [[agentic-design-patterns-planning]]
- [[ai-agents-claude-skills-methodology]]
- [[agentic-engineering-subagents]]
- [[a-plan-is-not-a-strategy]]
