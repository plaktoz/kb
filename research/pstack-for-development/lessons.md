# Lesson Plan: pstack for Development

*Source: `research/pstack-for-development/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations: The Problem and the Tool
*Establishes why pstack exists before introducing any commands — context that makes every later skill choice make sense.*

### Lesson 1: The Problem pstack Solves
**File:** `lessons/0001-problem-pstack-solves.html`
**Key concepts:** context amnesia · green build fallacy · agent-as-engineer framing · done conditions
**Source:** https://flaviocopes.com/pstack/ — pstack exists because agents "keep forgetting" guidance on investigation, design, testing, and communication; the fix is structured, durable skill files
**Skill:** Write a "bad" task prompt for an AI agent, then rewrite it using the `/poteto-mode` structure (`goal` / `Done means` / `Keep`). Compare the two side-by-side.
**Reference doc:** `reference/pstack-overview.html`

### Lesson 2: Installing pstack for Claude Code
**File:** `lessons/0002-installing-pstack-claude.html`
**Key concepts:** pstack-claude port · marketplace plugin · SessionStart hook · model config file · skill discovery
**Source:** https://github.com/michael-denyer/pstack-claude — 54 shared skill directories, 31 public slash commands, automatic routing via SessionStart hook
**Skill:** Write the exact three commands to install pstack-claude, enable the session hook, and verify which model is assigned to the `fable` judgment role. Annotate each command with what it does.
**Reference doc:** `reference/pstack-installation.html`

---

## Module 2 — The Core Interface: Routing, Investigation, and Verification
*Covers the three primitives used on every non-trivial task: routing via poteto-mode, investigation via /how, and the verification standard that makes outputs trustworthy.*

### Lesson 3: poteto-mode — The Central Router
**File:** `lessons/0003-poteto-mode-router.html`
**Key concepts:** routing table · playbook selection · autonomy rules · Laziness Protocol · Guard the Context Window
**Source:** https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/poteto-mode/SKILL.md — routing table maps 8 signal types to sub-skills; 21 principles enforced; reversible work auto-proceeds, destructive actions always pause
**Skill:** Given 5 task descriptions (provided in the lesson), classify each into the correct playbook or sub-skill using the routing table. Explain the signal that drove each routing decision.
**Reference doc:** `reference/routing-table.html`

### Lesson 4: Investigation Primitives — /how and /why
**File:** `lessons/0004-how-and-why.html`
**Key concepts:** complexity classification · parallel explorers · synthesis agent · /how vs /why distinction · output sections
**Source:** https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/how/SKILL.md — /how classifies simple vs complex, spawns 2–4 parallel opus explorers for complex questions, synthesises into 5 output sections
**Skill:** For a subsystem you work on, write a `/how` prompt and a `/why` prompt. Predict which complexity path each will take and why. Then identify which output section (Overview / Key Concepts / How It Works / Where Things Live / Gotchas) would answer your actual question.
**Reference doc:** *(extend existing reference/pstack-overview.html)*

### Lesson 5: Verification Philosophy — Prove It Works
**File:** `lessons/0005-verification-philosophy.html`
**Key concepts:** done conditions · real artifact verification · change-type matching · insufficient vs required proof · autonomy extension
**Source:** https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/poteto-mode/SKILL.md — "Prove It Works" principle; verification must match what changed: CLI → run the command, UI → walk the flow, performance → compare traces
**Skill:** Take three past tasks where you accepted "tests are green" as proof. For each, write the correct verification step that would have caught a real regression. Then write a full `/poteto-mode` prompt for one of them with a correct `Done means` clause.
**Reference doc:** `reference/verification-checklist.html`

---

## Module 3 — Quality Multipliers: Arena, Swarm, and Orchestration
*Introduces the tools that make pstack scale beyond what a single agent context can achieve — both for quality (arena) and coverage (swarm).*

### Lesson 6: Arena — Multi-Model Competition
**File:** `lessons/0006-arena-multi-model-competition.html`
**Key concepts:** 6-phase competition · rubric design · cross-judge · graft technique · convergence vs divergence signal
**Source:** https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/arena/SKILL.md — Frame → Fan Out → Cross-Judge → Pick → Graft → Verify; convergence = ship, divergence = reframe; output is 1 artifact + synthesis note
**Skill:** Design an arena run for a real pending decision in your codebase. Write: (1) the artifact definition, (2) a 4-criterion rubric, (3) which models you'd assign as runners and cross-judge, and (4) what "Verify" looks like for this artifact.
**Reference doc:** `reference/arena-rubric-template.html`

### Lesson 7: Swarm — Parallel Coverage
**File:** `lessons/0007-swarm-parallel-coverage.html`
**Key concepts:** partition / race / mixed shapes · self-contained briefs · PASS/ISSUES/BLOCKED · gap handling · isolation via worktrees
**Source:** https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/swarm/SKILL.md — workers receive fully self-contained briefs; PASS/ISSUES/BLOCKED with evidence; missing SHAs rerun once then recorded as gap; gaps never count as passes
**Skill:** Write a swarm brief for a real audit task (e.g. "check all API endpoints for missing auth guards"). Specify: shape (partition/race/mixed), N workers, slice assignment for each worker, done predicate, and reporting format. Then write what a BLOCKED response from a worker would look like.
**Reference doc:** `reference/swarm-brief-template.html`

### Lesson 8: Arena vs Swarm — Choosing the Right Tool
**File:** `lessons/0008-arena-vs-swarm.html`
**Key concepts:** coverage vs quality · single artifact vs aggregated report · when shape matters · Anthropic pattern mapping
**Source:** https://anthropic.com/engineering/building-effective-agents + arena/swarm SKILL.md files — arena maps to evaluator-optimizer, swarm maps to parallelization/voting; Anthropic: "start simple, add complexity only when it demonstrably improves outcomes"
**Skill:** For each of 5 scenarios (provided in the lesson), decide whether to use arena, swarm, a single playbook, or nothing — and write one sentence justifying each choice.
**Reference doc:** *(extend existing reference/pstack-overview.html)*

### Lesson 9: Agentic Architecture Patterns Mapped to pstack
**File:** `lessons/0009-agentic-architecture-patterns.html`
**Key concepts:** prompt chaining · orchestrator-workers · evaluator-optimizer · parallelization/voting · ACI (agent-computer interface) · tool design principles
**Source:** https://anthropic.com/engineering/building-effective-agents — 4 patterns; "spent more time optimizing tools than the overall prompt"; poka-yoke argument design; absolute filepaths; direct API over frameworks
**Skill:** Audit one tool you've built or used in an agent workflow. Apply the 3 ACI principles from the Anthropic article (docstring-quality description, poka-yoke arguments, absolute paths). Write the improved tool description.
**Reference doc:** `reference/agentic-patterns.html`

---

## Module 4 — Autonomous Runs and Continuous Improvement
*Covers how to hand work to agents overnight safely, and — the key goal of this course — how to make the agent system demonstrably better after every session.*

### Lesson 10: Autonomous Runs — Overnight Execution
**File:** `lessons/0010-autonomous-runs.html`
**Key concepts:** autonomous-run playbook · done condition design · decision log · session overrides · rollback guards · when to pause vs proceed
**Source:** https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/poteto-mode/SKILL.md — "Never Block on the Human" for reversible work; force-pushes, deploys, data deletion always pause; "going to bed" or "run until done" extend autonomy
**Skill:** Write a complete autonomous run prompt for a real refactoring task: goal, `Done means` clause, `Keep` clause, decision log instruction, and one explicit rollback guard. Identify which action in your task would trigger a pause even under full autonomy.
**Reference doc:** `reference/autonomous-run-template.html`

### Lesson 11: The /reflect Loop — Making Agents Better Over Time
**File:** `lessons/0011-reflect-continuous-improvement.html`
**Key concepts:** 6-step reflect loop · 3-lens review (judgment/tooling/divergent) · Accepted/Rejected/Backlog · structural check · human approval guardrail · one-offs are not learnings
**Source:** https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/reflect/SKILL.md — mines transcripts through 3 parallel reviewers, synthesises, checks if learnable as a lint rule first, requires human approval; "Skill changes affect every future agent in the org. Do not auto-apply."
**Skill:** Read a recent agent conversation transcript (or recall one). Apply the 3-lens review manually: (1) judgment — what decisions were suboptimal? (2) tooling — what tool calls were inefficient? (3) divergent — what alternative approach was never considered? Write one Accepted learning and one thing that belongs in Backlog instead.
**Reference doc:** `reference/reflect-workflow.html`

### Lesson 12: /automate-me — Building Your Personal Mode
**File:** `lessons/0012-automate-me-personal-mode.html`
**Key concepts:** personal skill authoring · transcript pattern mining · /automate-me · plugin-dev · skill vs preference · when personalisation is durable
**Source:** https://flaviocopes.com/pstack/ + https://github.com/michael-denyer/pstack-claude/blob/main/docs/reference.md — /automate-me reads transcripts and creates a personal mode skill; /reflect after difficult tasks proposes skill improvements (requires approval)
**Skill:** Write 3 recurring patterns from your own agent usage that would be worth encoding as a personal skill. For each, decide: is this a durable, reusable pattern (encode it) or a one-off preference (skip it)? Then draft the SKILL.md frontmatter (name, trigger, behaviour) for the strongest one.
**Reference doc:** *(extend existing reference/reflect-workflow.html)*

---

## Suggested Teaching Order

Work through modules in sequence: foundations before routing, routing before quality multipliers, multipliers before autonomous/improvement. Within Module 3, Lesson 8 (arena vs swarm) deliberately follows both Lesson 6 and 7 so the comparison is grounded. Lesson 11 (/reflect) is last because it requires having gone through enough lessons to have real "transcripts" worth reflecting on.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/pstack-overview.html` | What pstack is, skill taxonomy diagram, when to use vs skip |
| `reference/routing-table.html` | Full poteto-mode routing table (signal → playbook), all 21 principles summary |
| `reference/pstack-installation.html` | Step-by-step install for Claude Code, model config reference, hook setup |
| `reference/verification-checklist.html` | Done-condition templates by change type, insufficient vs required proof table |
| `reference/arena-rubric-template.html` | Blank arena rubric template, 6-phase checklist, convergence/divergence decision guide |
| `reference/swarm-brief-template.html` | Blank swarm brief template, shape decision guide, PASS/ISSUES/BLOCKED format |
| `reference/agentic-patterns.html` | Anthropic 4 patterns, ACI principles, pstack mapping table |
| `reference/autonomous-run-template.html` | Blank autonomous run prompt template, rollback guard checklist, decision log format |
| `reference/reflect-workflow.html` | 6-step reflect diagram, 3-lens review guide, Accepted/Rejected/Backlog format |
