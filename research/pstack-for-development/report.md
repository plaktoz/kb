# Research: pstack for Development
*Generated: 2026-09-26 | Scope: A full-coverage guide to pstack — what it is, how it works internally, core usage patterns, advanced agentic integration, and visual mental models for quick knowledge pickup. Aimed at a seasoned engineer building a lesson plan.*

## Research Outline

1. What is pstack? — foundations, the problem it solves, and when to reach for it
2. How pstack works internally — skill routing, subagent delegation, and model assignment
3. Core usage patterns — key commands, reading outputs, common workflows
4. Advanced usage and agentic workflow integration — autonomous runs, multi-model orchestration, CI
5. Visual mental models — diagrams for skill routing, arena competition, swarm fan-out, and the continuous improvement loop

---

## 1. What is pstack? — Foundations, Origins, and When to Reach For It

### pstack: A Deep Dive (Flavio Copes)

- **Source**: https://flaviocopes.com/pstack/
- **Summary**: pstack is a Cursor plugin for rigorous AI agent work created by Lauren Tan (@poteto). It contains 23 workflow skills, 21 engineering principles, 22 task playbooks, and 2 specialized subagents. The core philosophy is "less code, higher quality, and verification" — framing agents like engineers who need explicit guidance on how to investigate, design, test, and communicate, since agents keep forgetting context. The primary entry point is `/poteto-mode`, a router that selects a playbook, creates a task list, delegates to appropriate models, and demands evidence before reporting success. SKILL.md files also work with Claude Code, Codex, and other coding agents beyond Cursor.
- **Relevance**: This is the seed article that defines pstack's purpose, philosophy, and core interface — essential foundation for every section of the lesson plan.

```
THE CORE PROBLEM pstack SOLVES
─────────────────────────────────────────────────────
  Traditional AI agent use:           pstack approach:

  You → Agent → Code                  You → /poteto-mode → Playbook Router
         ↓                                          ↓
    (forgets context)              Selects correct workflow by signal type
         ↓                                          ↓
    Accepts green build           Demands real artifact verification
    as proof                              ↓
                                  Routes to subagents with explicit models
                                          ↓
                                  Returns finished, verified work
─────────────────────────────────────────────────────
```

### pstack-claude: Claude Code Port

- **Source**: https://github.com/michael-denyer/pstack-claude
- **Summary**: An unofficial port of Lauren Tan's Cursor-native pstack adapted for Claude Code, Codex, OpenCode, and Gemini CLI. It preserves playbooks and principles while translating Cursor primitives to other harnesses. Shares 54 skill directories, exposing 31 public slash commands. Installation via Claude Code marketplace: `/plugin marketplace add michael-denyer/pstack-claude` followed by `/plugin install pstack@pstack-claude`. The Claude Code port adds automatic routing via a SessionStart hook that triggers `poteto-mode` when the task touches more than one file, involves architecture, or concerns a bug with unknown cause.
- **Relevance**: Since the user works in Claude Code, this is the actionable installation path and is the version that will be used in practice.

```
WHEN TO REACH FOR pstack vs. SKIP IT
────────────────────────────────────
  Use pstack for:                    Skip pstack for:
  ✓ Multi-file changes               ✗ Single-line typo fix
  ✓ Unknown-cause bugs               ✗ Small config edits
  ✓ Architecture decisions           ✗ Correcting text
  ✓ Runtime forensics                ✗ Routine generation tasks
  ✓ Overnight autonomous runs        ✗ Tasks one agent finishes quickly
  ✓ Deep investigation / audit
────────────────────────────────────
```

---

## 2. How pstack Works Internally — Skill Routing, Subagent Delegation, and Model Assignment

### poteto-mode Skill Definition

- **Source**: https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/poteto-mode/SKILL.md
- **Summary**: poteto-mode is the central router for pstack. It evaluates the incoming task against a routing table of signals and dispatches to the appropriate playbook or sub-skill. It enforces 21 principles including the Laziness Protocol (bias toward deletion and smallest viable change), Prove It Works (verify real artifacts not proxies), and Guard the Context Window (route bulk work to subagents). Autonomy rules determine when to proceed vs. pause: reversible work proceeds without asking; force-pushes to shared branches, deploys, data deletion, and customer messages always pause. Each role has an explicitly assigned model — hardest judgment tasks go to `fable`, feature/refactoring to `opus`.
- **Relevance**: Understanding poteto-mode's routing logic is the key to understanding how all other pstack skills compose together.

```
POTETO-MODE ROUTING TABLE
─────────────────────────────────────────────────────────────────────────
  Signal detected                        →   Routes to
  ────────────────────────────────────────────────────────────────────
  Nontrivial change or architecture       →   /how skill
  Empirical question (behavior, timing)   →   Prototype playbook
  Code crossing function boundaries       →   /architect skill
  Parallel fan-out needed                 →   /swarm skill
  Contested design choice                 →   /interrogate skill
  Any prose surface                       →   /unslop skill
  PR status request                       →   Babysit playbook
  Landing a green stack                   →   Shipping playbook
  ────────────────────────────────────────────────────────────────────
  Task type             →   Playbook
  ────────────────────────────────────────────────────────────────────
  Read-only question    →   investigation.md
  Reported defect       →   bug-fix.md
  Measured slowness     →   perf-issue.md
  New behavior          →   feature.md
  Structure refactor    →   refactoring.md
  Throwaway sketch      →   prototype.md
  Long autonomous task  →   autonomous-run.md
  Multi-day program     →   orchestrate.md
─────────────────────────────────────────────────────────────────────────
```

### pstack-claude Reference Documentation

- **Source**: https://github.com/michael-denyer/pstack-claude/blob/main/docs/reference.md
- **Summary**: The reference doc details how 54 skill directories are shared across four runtimes (Claude Code, Codex, OpenCode, Gemini CLI), how automatic routing works via SessionStart hooks, and the full model configuration system. Key dependencies include `gh` (GitHub CLI for PR monitoring), Bun (for watch/orchestration scripts), Graphite CLI for stack frontier, and `jq`/`rg` for audit columns. Configuration is stored in `~/.claude/pstack-models.md` and assigns models per role (runners, judgment, implementation). The repo layout separates skills, agents, hooks, and tools cleanly.
- **Relevance**: Explains the plumbing behind pstack — how skills are discovered, models are assigned, and how the system composes across different agent runtimes.

```
pstack INTERNAL ARCHITECTURE
────────────────────────────────────────────────────
  User task
      │
      ▼
  SessionStart hook ──► (auto-routing trigger check)
      │                      │
      │                      ▼
      │              Meets threshold?
      │                 Yes │  No
      │                     │
      ▼                     ▼
  /poteto-mode          Direct skill
      │
      ▼
  Playbook Router
      │
   ┌──┼──────────────┐
   ▼  ▼              ▼
  how  architect   swarm / arena
   │       │           │
   ▼       ▼           ▼
  Explorer  Design   N parallel
  subagents  check   workers
   │       │           │
   └───────┴───────────┘
           │
           ▼
       Synthesis / Verification
           │
           ▼
       Finished, verified output
────────────────────────────────────────────────────
```

---

## 3. Core Usage Patterns — Key Commands, Reading Outputs, Common Workflows

### The `/how` Skill

- **Source**: https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/how/SKILL.md
- **Summary**: `/how` is designed for questions like "how does X work?", code walkthroughs, and ownership queries ("where should this live"). It first classifies complexity: simple questions (single module) get one agent in a single pass; complex questions (multi-file subsystem) spawn 2–4 parallel explorer subagents then a synthesis agent. Output sections are: Overview, Key Concepts, How It Works, Where Things Live, Gotchas. Motivation questions ("why was this built?") are explicitly redirected to `/why`. The skill uses `opus` as default model and produces explanations "fit for a senior engineer building a mental model, not line-by-line annotation."
- **Relevance**: `/how` is the first command to reach for when onboarding to a codebase or understanding a subsystem — it's the investigation primitive that informs all other actions.

```
/how DECISION TREE
──────────────────────────────────────────
  /how "how does X work?"
         │
         ▼
    Complexity check
    ┌────┴────┐
  Simple   Complex
    │         │
    ▼         ▼
  1 agent   Decompose → 2-4 angles
    │         │
    ▼         ▼
  Explain   Parallel explorer
    │       subagents (opus)
    │         │
    │         ▼
    │       Synthesis agent
    │         │
    └────┬────┘
         ▼
    Output: Overview → Key Concepts
    → How It Works → Where Things Live
    → Gotchas
──────────────────────────────────────────
```

### The Arena Skill — Multi-Model Competition

- **Source**: https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/arena/SKILL.md
- **Summary**: Arena spawns N parallel candidate subagents at the same task, evaluates all outputs against a 3–6 criterion rubric, cross-judges with a separate readonly judge model (different family preferred), picks the strongest base, then grafts the best ideas from losers into the winner. Six phases: Frame → Fan Out → Cross-Judge → Pick → Graft → Verify. Convergence (candidates agree on shape) signals "ship it." Wild divergence signals an underspecified brief — reframe, don't average. Output is one artifact plus a synthesis note naming base, grafts, rejections, and verification result.
- **Relevance**: Arena is the quality multiplier for non-trivial decisions where a single attempt would lock in the wrong shape — a core pattern for seasoned engineers using agents for high-stakes work.

```
ARENA: 6-PHASE COMPETITION PATTERN
──────────────────────────────────────────────────────────────
  Frame: define artifact + 3-6 criterion rubric
      │
      ▼
  Fan Out: spawn N candidates simultaneously (opus/fable/sonnet)
  ┌──────┬──────┬──────┐
  │ C-1  │ C-2  │ C-3  │   (each: artifact + rationale)
  └──┬───┴──┬───┴──┬───┘
     │      │      │
     └──────┼──────┘
            ▼
  Cross-Judge: readonly judge (different model family)
  scores each candidate against rubric
            │
            ▼
  Pick: strongest base (by extensibility, not feel)
            │
            ▼
  Graft: walk losers → pick 1-2 ideas each → integrate
            │
            ▼
  Verify: test synthesized result
  ┌─────────┴────────────┐
  PASS                 FAIL
  Ship it           Re-frame or
                    fix missed graft
──────────────────────────────────────────────────────────────
  Convergence → ship. Divergence → reframe the brief.
──────────────────────────────────────────────────────────────
```

### The Swarm Skill — Parallel Coverage

- **Source**: https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/swarm/SKILL.md
- **Summary**: Swarm fans out N parallel workers for coverage, races, or gauntlets. Three shapes: partition (separate slices of work), race (identical briefs compete), or mixed. Workers must receive fully self-contained briefs (goal, scope, slice, verification method, reporting format). Workers report `PASS`, `ISSUES`, or `BLOCKED` with evidence — a worker that finds a defect lists every issue it can prove, not just the first. Results missing required SHAs/methods are rerun once, then recorded as gaps (gaps never count as passes). Isolation is via assigned worktrees/output directories since all subagents run on the same machine.
- **Relevance**: Swarm is the parallelization primitive — use it to cover more ground than one agent context can hold, or to run the same verification from N independent angles.

```
SWARM vs ARENA: WHEN TO USE WHICH
──────────────────────────────────────────────────────────
  SWARM                         ARENA
  ─────────────────────         ──────────────────────────
  Purpose: Coverage             Purpose: Quality
  Shape: Partition/Race/Mixed   Shape: Competition + Graft
  Workers: Independent slices   Candidates: Same task, N ways
  Output: Aggregated report     Output: 1 synthesized artifact
  Result: PASS/ISSUES/BLOCKED   Result: Winner + synthesis note
  Use when: large surface area  Use when: single artifact where
  to cover in parallel          wrong shape would be costly
──────────────────────────────────────────────────────────
```

---

## 4. Advanced Usage and Agentic Workflow Integration

### Building Effective AI Coding Agents (Anthropic)

- **Source**: https://anthropic.com/engineering/building-effective-agents
- **Summary**: Anthropic's engineering team identifies four architectural patterns for agents: prompt chaining (sequential steps), orchestrator-workers (one LLM dynamically delegates to workers), evaluator-optimizer (generate-evaluate loops), and parallelization (sectioning or voting). For coding agents specifically, verifiability via automated tests is the key advantage — agents iterate using test results as feedback. The team notes they "spent more time optimizing tools than the overall prompt" — tool design (ACI) is as important as prompt engineering. Key practices: absolute filepaths, docstring-quality tool descriptions with examples, poka-yoke argument design, and minimal escaping overhead. Direct API usage over frameworks reduces abstraction layers.
- **Relevance**: Provides the theoretical foundation and patterns that pstack implements in practice — pstack's arena maps to evaluator-optimizer, swarm maps to parallelization/voting, and the verification philosophy directly matches Anthropic's "solutions are verifiable via tests" insight.

```
AGENTIC ARCHITECTURE PATTERNS (Anthropic) MAPPED TO pstack
────────────────────────────────────────────────────────────────────────
  Pattern              pstack equivalent     When to use
  ─────────────────────────────────────────────────────────────────
  Prompt chaining       Playbook (bug-fix,   Fixed, predictable subtasks
                        feature, etc.)
  Orchestrator-Workers  /swarm               Open surface area, N slices
  Evaluator-Optimizer   /arena               Single artifact, iterative
                                             quality improvement
  Parallelization       /swarm (race shape)  Same task, N candidates,
  (voting)                                   confidence via agreement
────────────────────────────────────────────────────────────────────────
```

### The Reflect Skill — Continuous Improvement Loop

- **Source**: https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/reflect/SKILL.md
- **Summary**: `/reflect` mines conversations for durable learnings and routes them into concrete skill edits, creating a feedback loop that improves the agent system over time. Six steps: locate transcript → three parallel reviewers (judgment, tooling, divergent lenses) → synthesize into Accepted/Rejected/Backlog → structural check (can this be a lint rule instead?) → apply with human approval → summary. Critical guardrail: "Skill changes affect every future agent in the org. Do not auto-apply." Small edits go to the parent; substantive changes go to `plugin-dev:skill-development` for draft/test/iterate; new skills are created only via `plugin-dev`. One-offs are not learnings.
- **Relevance**: This is directly what the user is seeking — how to make agentic systems more useful over time. `/reflect` is the explicit mechanism for continuous improvement, making pstack self-improving with human oversight.

```
THE REFLECT CONTINUOUS IMPROVEMENT LOOP
────────────────────────────────────────────────────────────────────
  Conversation ends
        │
        ▼ (triggered by /reflect)
  Locate session transcript
        │
        ▼
  3 parallel reviewers (simultaneously)
  ┌──────────┬──────────┬────────────┐
  │ Judgment │ Tooling  │ Divergent  │
  │ lens     │ lens     │ lens       │
  └────┬─────┴────┬─────┴────┬───────┘
       └──────────┼──────────┘
                  ▼
          Synthesize findings
          Accepted / Rejected / Backlog
                  │
                  ▼
          Structural check:
          Can this be a lint rule/script?
          YES → Backlog  NO → proceed
                  │
                  ▼
          Human approval ← REQUIRED
          (no auto-apply)
                  │
          ┌───────┴────────────┐
          ▼                    ▼
     Small edit           Substantive change
     Parent applies       plugin-dev:skill-development
                          draft → test → iterate
                  │
                  ▼
          Skills updated → future agents behave better
          ↑_____________________________________________↑
                  (loop repeats each session)
────────────────────────────────────────────────────────────────────
```

---

## 5. Visual Mental Models

### pstack Full Skill Map

```
pstack SKILL TAXONOMY
──────────────────────────────────────────────────────────────────────
  ENTRY POINT
  └── /poteto-mode ─── router for all non-trivial tasks

  UNDERSTAND
  ├── /how ─────────── trace how subsystem works (no code changes)
  ├── /why ─────────── search git/PRs/docs for design reasoning
  └── /teach ──────── /how + /why combined

  BUILD / CHANGE
  ├── /architect ───── design types/module shape before coding
  ├── Bug Fix ──────── reproduce → investigate → fix → verify
  ├── Feature ─────── design-first, then implement
  ├── Refactoring ──── structure-preserving change
  ├── Perf Issue ───── profile → identify hotspot → fix → compare traces
  ├── Hillclimb ────── iterative improvement
  └── Prototype ────── throwaway design sketch

  QUALITY MULTIPLIERS
  ├── /arena ──────── N parallel candidates → cross-judge → graft → 1 winner
  ├── /swarm ──────── N parallel workers → aggregate report
  └── /interrogate ── 3 models attempt to break a diff

  LONG-RUNNING / AUTONOMOUS
  ├── Autonomous Run ─ overnight/unattended execution
  ├── Orchestrate ──── multi-day program with decision log
  └── /babysit ──────── monitor PRs, fix CI, manage comments

  SESSION MANAGEMENT
  ├── /recall ──────── reconstruct context from recent transcripts
  └── Pause Safely ─── checkpoint current state before stopping

  CONTINUOUS IMPROVEMENT
  ├── /reflect ──────── mine transcripts → skill edits (human-approved)
  └── /automate-me ──── draft personal mode from your usage patterns

  CLEANUP
  ├── /unslop ──────── remove AI writing tells
  └── /thermo-nuclear-code-quality-review ── strict maintainability audit
──────────────────────────────────────────────────────────────────────
```

### Verification Philosophy Mental Model

```
PSTACK VERIFICATION HIERARCHY
──────────────────────────────────────────────────────────────────
  ❌ Insufficient proof:
     "The build passed"
     "Tests are green"
     "Lint is clean"

  ✓ Required proof (match what changed):
     CLI change      → run the real command
     UI change       → walk the changed flow
     Performance     → compare actual traces (before/after)
     Storage change  → read the value back from storage
     Behavior change → demonstrate against real artifact

  HOW TO WRITE A DONE CONDITION:
  ──────────────────────────────────────────────────────────────
  /poteto-mode <what you observed or want>
  Done means <something the agent can run or inspect>.
  Keep <existing behavior that must not change>.
  ──────────────────────────────────────────────────────────────

  Example (autonomous run):
  "Done means zero old callers, every parser fixture passes,
   and the old API is deleted."
──────────────────────────────────────────────────────────────────
```

### Model Assignment Mental Model

```
PSTACK MODEL ASSIGNMENT BY ROLE
──────────────────────────────────────────────────────────────────
  Task type / Role          Model       Reasoning effort
  ─────────────────────────────────────────────────────────────
  Feature, refactoring      opus        medium
  Judgment and prose        opus        medium–high
  Strongest judgment        fable       xhigh / max
  Bug fix, perf, hillclimb  fable       high
  How explorer              opus        medium
  How explainer             opus        medium
  Arena runners             opus/fable  high
  Arena cross-judge         fable       xhigh (different family)
  Swarm workers             sonnet      low–medium (coverage)
  ─────────────────────────────────────────────────────────────
  Pattern: cheapest model that can reliably do the job.
  Save fable for judgment, synthesis, and hardest decisions.
──────────────────────────────────────────────────────────────────
```

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://flaviocopes.com/pstack/
- https://github.com/michael-denyer/pstack-claude
- https://github.com/michael-denyer/pstack-claude/blob/main/docs/reference.md
- https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/poteto-mode/SKILL.md
- https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/how/SKILL.md
- https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/arena/SKILL.md
- https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/swarm/SKILL.md
- https://github.com/michael-denyer/pstack-claude/blob/main/plugins/pstack/skills/reflect/SKILL.md
- https://anthropic.com/engineering/building-effective-agents
