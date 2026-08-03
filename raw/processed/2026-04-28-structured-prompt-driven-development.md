---
source_url: https://martinfowler.com/articles/structured-prompt-driven/
author: Wei Zhang, Jessie Jie Xia
date: 2026-04-28
---

# Structured-Prompt-Driven Development (SPDD)

SPDD is an engineering method developed by Thoughtworks' internal IT teams that treats prompts as "first-class delivery artifacts" — version-controlled, reviewed, and reused alongside code.

The core insight: individual developer speed gains from AI assistants don't automatically translate to team-level throughput. Ambiguous requirements scale quickly, reviews become harder, and production risk grows. SPDD addresses this by making AI-generated changes governable and reviewable.

## Two Core Components

### 1. The REASONS Canvas

A seven-part structured prompt template:

- **R** — Requirements (problem + definition of done)
- **E** — Entities (domain model)
- **A** — Approach (solution strategy)
- **S** — Structure (system placement)
- **O** — Operations (concrete implementation steps)
- **N** — Norms (coding standards, observability)
- **S** — Safeguards (hard constraints, security rules)

### 2. The SPDD Workflow

Key principle: *"When reality diverges, fix the prompt first — then update the code."*

Key commands via the `openspdd` CLI tool:

| Command | Purpose |
|---|---|
| `/spdd-story` | Breaks requirements into INVEST-principle user stories |
| `/spdd-analysis` | Scans codebase, produces domain/risk analysis |
| `/spdd-reasons-canvas` | Generates full REASONS Canvas |
| `/spdd-generate` | Produces code task-by-task per the Canvas |
| `/spdd-prompt-update` | Updates Canvas when requirements change (requirements → prompt → code) |
| `/spdd-sync` | Syncs code changes back to Canvas (code → prompt) |

## Example: Billing Engine Enhancement

The walkthrough demonstrates enhancing a token-billing system from flat-rate pricing to multi-plan, model-aware billing. Six steps:

1. **Create user stories** — `/spdd-story` splits a complex enhancement into discrete stories
2. **Clarify analysis** — developer reviews scope, logic, and definition of done
3. **Generate analysis context** — `/spdd-analysis` scans relevant code and identifies domain concepts, risks, edge cases
4. **Generate structured prompt** — `/spdd-reasons-canvas` produces the full implementation blueprint
5. **Generate & verify code** — `/spdd-generate` produces code; API tests validate behavior; code review addresses logic corrections (prompt-first) vs. refactoring (code-first, then sync)
6. **Generate unit tests** — template-driven approach produces test scenarios, deduplicates against existing tests

The two-track code review approach is notable:

- **Logic corrections** (behavior changes): update prompt → regenerate code
- **Refactoring** (no behavior change): fix code → sync back to prompt

## Three Core Developer Skills

1. **Abstraction First** — design object relationships and boundaries before generating code
2. **Alignment** — make explicit what will and won't be built; agree on constraints upfront
3. **Iterative Review** — treat AI assistance as an engineering loop, not a one-shot draft

## Fitness Assessment (Selected)

| Rating | Scenario |
|---|---|
| ★★★★★ | Scaled, standardized delivery |
| ★★★★★ | High compliance / hard constraints |
| ★★☆☆☆ | Hotfixes or exploratory spikes |
| ★☆☆☆☆ | Poorly defined domains or pure visual/creative work |

## Key Trade-offs

**Benefits:** determinism, traceability, faster reviews, explainability, safer evolution

**Costs:** mindset shift toward "design first," senior expertise needed upfront, automation tooling required to avoid throughput ceilings

The authors acknowledge SPDD currently skews toward expert practitioners but note plans to make it more accessible through reusable asset systems and automated verification at the prompt/spec layer.

## Closing Thought

The article argues the real competition in AI-assisted development isn't model capability — it's engineer cognitive bandwidth: "how clearly we can think, frame problems, and make decisions."
