# Product Requirements Document: Unified Multi-Agent Development System

**Version:** 1.0  
**Date:** October 17, 2026  
**Status:** Draft for Review

---

## Executive Summary

This PRD defines a unified multi-agent development system that synthesizes the enduring principles from five proven systems:

1. **Gas Town** - Multi-agent orchestration with persistent state via git worktrees, hierarchical monitoring, and merge queue verification
2. **BMAD Method** - Structured AI-driven development with right-sized planning, durable context artifacts, and specialized agent perspectives
3. **pstack-claude** - Portable agent skills with runtime flexibility, model policy separation, and workflow routing
4. **Ponytail** - Radical minimalism through "solve before writing" ladder principle, measured impact tracking, and production-focused review
5. **Matt Pocock's Skills** - Engineering fundamentals including grilling for alignment, shared language via glossaries, TDD discipline, and architectural investment

The goal is to create a system that combines distributed coordination, structured workflows, radical minimalism, and engineering fundamentals into a cohesive platform for AI-assisted software development at scale.

### What Problem Does This Solve?

Current AI-assisted development faces several challenges:
- **Context Loss**: Agents lose state on restart, making multi-agent workflows fragile
- **Over-Engineering**: Agents write more code than necessary, increasing maintenance burden
- **Quality Issues**: Without systematic verification, bugs reach production
- **Coordination Chaos**: Multiple agents working without structure create conflicts
- **Human Bottlenecks**: Pure automation loses judgment; pure manual loses speed
- **Vendor Lock-in**: Skills and workflows tied to specific AI tools

This system addresses all these challenges through proven principles from production systems.

---

## Vision

**Build a multi-agent development system that:**
- Scales reliably to 20-30+ concurrent agents
- Persists context across crashes and restarts
- Produces minimal, high-quality code through systematic verification
- Keeps humans in control at critical decision points
- Works across multiple AI runtimes (Claude, Copilot, Codex, Gemini, etc.)
- Measures and optimizes for real impact: code size, cost, time, and quality

---

## Core Principles (Non-Negotiable)

### 1. Context Persistence
All agent work state must survive crashes and restarts through git-backed storage.

### 2. Structured Workflows
Prevent chaos through explicit workflow orchestration and task tracking.

### 3. Systematic Verification
Every change flows through automated quality gates before reaching main.

### 4. Human Control
Humans approve at critical junctures; agents propose and execute.

### 5. Radical Minimalism
Solve before writing; measure the impact of not writing code.

### 6. Measurable Impact
Track code size, cost, time, test coverage, and production reliability.

---

## System Architecture

### High-Level Components

```
┌─────────────────────────────────────────────────────────────┐
│                     Human Interface Layer                    │
│  (CLI, Dashboard, Band UI, Escalation Channels)             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   Orchestration Layer                        │
│  - Mayor (Coordinator)                                       │
│  - Router (Skill Selection)                                  │
│  - Scheduler (Capacity Management)                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Agent Execution Layer                     │
│  - Worker Agents (Polecats)                                  │
│  - Specialized Agents (PM, Architect, UX, Dev, Analyst)     │
│  - Review Agents (Code Review, Audit, TDD)                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   Verification Layer                         │
│  - Refinery (Merge Queue)                                    │
│  - Test Runner (TDD, E2E)                                    │
│  - Minimalism Checker (Ladder Enforcement)                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   Monitoring Layer                           │
│  - Witness (Per-Project Health)                              │
│  - Deacon (Cross-Project Patrol)                             │
│  - Telemetry (OpenTelemetry)                                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Persistence Layer                         │
│  - Git Worktrees (Hooks)                                     │
│  - Issue Tracker (Beads/Dolt)                                │
│  - Decision Artifacts (GLOSSARY.md, ADRs, Specs)            │
│  - Metrics Database (Band Data)                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Detailed Requirements

## 1. Context Persistence System

### 1.1 Git-Backed State Storage

**Why This Matters:**
Traditional AI agents lose all context when they crash or restart. This makes multi-agent workflows fragile - a single crash can lose hours of work. Git worktrees solve this by treating agent state as version-controlled data.

**Requirements:**
- Each agent gets a git worktree (hook) for persistent state
- Work state survives crashes and restarts
- Version-controlled history with rollback capability
- Separation of agent identity (persistent) from sessions (ephemeral)

**How It Works:**
An agent's "hook" is a git worktree - a separate working directory linked to the main repository. When an agent works, it commits state changes to its hook. If the agent crashes, a new session can resume from the last committed state. This is Gas Town's "Propulsion Principle" - the hook IS the assignment.

**Example:**
```
project/.git/worktrees/
  ├── polecat-alice/     # Alice's persistent state
  ├── polecat-bob/       # Bob's persistent state
  └── refinery/          # Merge queue state
```

### 1.2 Decision Artifacts

**Why This Matters:**
Decisions fade from memory. Without documentation, teams repeat discussions, make inconsistent choices, and lose context. Decision artifacts create a durable record that new team members and future agents can reference.

**Requirements:**
- **Product briefs and PRFAQs**: Document product decisions and user value
- **Architecture documents (ADRs)**: Record technical decisions with rationale
- **Specifications**: Bridge product and technical perspectives
- **Project glossary (GLOSSARY.md)**: Define shared language and domain terms
- **Shortcut comments**: Mark deferred work for debt tracking

**How It Works:**
Each type of artifact serves a specific purpose:
- **PRFAQ** (Press Release + FAQ): Describes the product from user perspective before building
- **ADR** (Architecture Decision Record): "We chose X over Y because Z, accepting trade-off T"
- **Spec**: Technical requirements derived from product brief
- **GLOSSARY.md**: "In this codebase, 'session' means X, not Y" - prevents miscommunication
- **Shortcut comments**: `// SHORTCUT: Using simple auth now, add OAuth later` - tracked in debt ledger

This is BMAD Method's "Durable Context Through Artifacts" principle combined with Matt Pocock's shared language approach.

### 1.3 Session Discovery

**Requirements:**
- Agents can query predecessors for context
- Discover previous sessions via event logs
- Enable context recovery without re-reading entire codebase

**Implementation:**
- `.events.jsonl` logs for all agent operations
- Seance-style query interface
- Indexed search across session history

---

## 2. Orchestration System

### 2.1 Mayor (Coordinator)

**Why This Matters:**
In multi-agent systems, someone needs to coordinate work without becoming a bottleneck. The Mayor is your primary interface - you tell it what you want, and it orchestrates the work across multiple agents without doing the implementation itself.

**Requirements:**
- Primary human interface for work coordination
- Orchestrates but doesn't execute (delegation over implementation)
- Creates convoys (work bundles) with dependency tracking
- Spawns and manages worker agents (Polecats)
- Handles escalations from agents

**How It Works:**
You tell the Mayor: "Build authentication system." The Mayor:
1. Breaks it into tasks (login, signup, password reset, session management)
2. Creates a convoy to track these tasks
3. Spawns worker agents (Polecats) for each task
4. Monitors progress and handles escalations
5. Reports completion when all tasks are done

The Mayor never writes code - it coordinates. This is Gas Town's "Delegation Over Implementation" principle.

### 2.2 Router (Skill Selection)

**Requirements:**
- Automatic skill/workflow selection based on request
- Playbooks for common scenarios
- User can override automatic routing

**Implementation:**
- Analyze request and invoke correct workflow
- Support for user-invoked and model-invoked skills
- Configurable routing behavior

### 2.3 Scheduler (Capacity Management)

**Requirements:**
- Prevent API rate limit exhaustion
- Batch agent dispatch under configurable limits
- Deferred dispatch when capacity constrained
- Direct dispatch when capacity available

**Implementation:**
- Configurable concurrency limits
- Queue-based dispatch system
- Real-time capacity monitoring

---

## 3. Agent Execution System

### 3.1 Worker Agents (Polecats)

**Requirements:**
- Spawned for specific tasks
- Ephemeral sessions, persistent identity
- Work assigned via hooks
- Report completion and escalate blockers

**Implementation:**
- Task-specific agent spawning
- Hook-based work assignment
- Completion protocol (gt done)
- Escalation protocol (gt escalate)

### 3.2 Specialized Agents

**Why This Matters:**
Different aspects of software need different expertise. Rather than requiring humans to have expertise in all areas, specialized agents bring distinct perspectives to complex decisions.

**Requirements:**
- **Product Manager**: User needs and product decisions
- **Architect**: Technical design and architecture decisions
- **UX Designer**: User experience and interface design
- **Developer**: Implementation with minimalism enforcement
- **Analyst**: Requirements analysis and clarification

**How It Works:**
For complex features, multiple specialized agents discuss the problem:
1. **Analyst** clarifies requirements through grilling sessions
2. **PM** defines product decisions and user value
3. **UX Designer** designs the user experience
4. **Architect** designs the technical approach
5. **Developer** implements with minimalism enforcement

Each agent has role-specific prompts and capabilities. This is BMAD Method's "Specialized Perspectives Through Agents" principle - bringing expertise without requiring human mastery of all domains.

**Example:**
Building a payment system:
- PM: "Users need to save cards for faster checkout"
- UX: "Show saved cards with last 4 digits, default selection"
- Architect: "Use Stripe's payment methods API, store tokens not cards"
- Developer: "Reuse existing API client, add 3 endpoints, 1 component"

### 3.3 Minimalism Enforcement (The Ladder)

**Why This Matters:**
AI agents tend to over-engineer solutions, writing custom implementations when simpler alternatives exist. Ponytail's benchmarks show that enforcing minimalism reduces code by 53%, cost by 26%, and time by 41% - while maintaining 98% test coverage for risky logic.

**Requirements:**
Before writing any code, agents must climb the ladder and stop at the first rung that holds:
1. **Does it need to exist?** - Skip features nobody asked for
2. **Already in this codebase?** - Reuse existing helpers, components, patterns
3. **Standard library or platform feature?** - Use built-in capabilities
4. **Installed dependency?** - Use what's already there
5. **Can it be one line?** - One line that's clear at a glance
6. **Otherwise** - The minimum code that works

**How It Works:**
The ladder runs AFTER understanding the problem, not instead of it. Agents read the code the change touches and trace the real flow before picking a rung. They're lazy about the solution, never about reading or scope analysis.

**Example:**
User asks for a date picker. Without the ladder: 335 lines (custom calendar component). With the ladder: 10 lines (reuse existing Input component with type="date", browser provides calendar).

---

## 4. Verification System

### 4.1 Refinery (Merge Queue)

**Why This Matters:**
Traditional merging tests PRs in isolation. Two PRs that pass individually can break when combined. The Refinery prevents this by testing the merged result before committing to main, ensuring the main branch stays green.

**Requirements:**
- Bors-style merge queue with bisecting verification
- Batch pending merge requests
- Test merged stack
- Bisect to isolate failures
- Merge only verified work to main

**How It Works (Bors-Style Merge):**
1. **Batch** - Collect all ready-to-merge PRs (e.g., PR-A, PR-B, PR-C)
2. **Merge First** - Combine ALL changes into a temporary branch
3. **Test Together** - Run full test suite on the merged stack
4. **If Green** - Merge all PRs to main at once
5. **If Red** - Bisect to isolate the failing PR:
   - Split batch in half (test A+B, test C)
   - Recursively bisect until culprit found
   - Merge only the good ones

**Example:**
```
Traditional: PR1 ✓, PR2 ✓ → merge both → main ✗ (broken)
Bors-Style:  PR1+PR2 → test together → ✗ → bisect → PR1 ✓, PR2 ✗ → merge PR1 only
```

This is Gas Town's Refinery agent - a merge processor that never writes application code, only merges branches mechanically.

### 4.2 Test-Driven Development

**Why This Matters:**
Tests catch bugs before production, but writing tests for everything wastes time. The key is selective testing: risky logic (branches, loops, parsers, money, security) gets tests; trivial changes don't. This is Ponytail's "Logic Leaves a Test" principle.

**Requirements:**
- Red-green-refactor discipline for risky logic
- Logic with branches, loops, parsers, money, or security leaves a test
- Trivial changes need no test (e.g., renaming, formatting)
- Self-checks for scripts (scripts test themselves)

**How It Works:**
1. **Red**: Write failing test first (defines expected behavior)
2. **Green**: Write minimum code to pass the test
3. **Refactor**: Clean up while keeping tests green

**What Gets Tested:**
- ✓ Conditional logic (if/else, switch)
- ✓ Loops and iteration
- ✓ Parsers and data transformation
- ✓ Money calculations
- ✓ Security checks
- ✗ Simple getters/setters
- ✗ Pure formatting changes
- ✗ Configuration files

This is Matt Pocock's TDD discipline combined with Ponytail's selective testing.

### 4.3 Code Review

**Why This Matters:**
Traditional code review focuses on style and standards. Production-focused review asks: "Will this break in production?" This catches real issues before they cause outages. Ponytail's two-axis review separates concerns: does it meet standards AND does it meet the spec?

**Requirements:**
- **Two-axis review**: Standards (code quality) and Spec (requirements)
- Review like on-call engineer (production impact mindset)
- Check: bugs, security, load, missing tests, performance, what to cut
- Each finding explains: what, problem, fix, consequence

**How It Works:**
Review happens on two parallel dimensions:
1. **Standards Axis**: Code quality, style, patterns, maintainability
2. **Spec Axis**: Does it solve the right problem? Does it meet requirements?

**Production-Impact Checklist:**
- Will this break under load?
- Are there security vulnerabilities?
- What happens if this fails?
- Are error cases handled?
- Is there a rollback plan?
- What can we cut to reduce risk?

Each finding must be actionable: "Line 42: SQL injection risk. Use parameterized query. Could expose user data."

This is Ponytail's production-focused review combined with Matt Pocock's two-axis approach.

### 4.4 Audit

**Requirements:**
- Whole-repo analysis ranked by impact
- Map codebase: entry points, data flow, expected load
- Prioritize findings by business impact
- Tell user what to fix first

**Implementation:**
- Codebase mapping
- Impact-based ranking
- Actionable recommendations
- Regular audit cycles

---

## 5. Monitoring System

### 5.1 Three-Tier Watchdog System

**Why This Matters:**
At scale (20-30+ agents), manual monitoring becomes impossible. A single-tier monitor creates a single point of failure. The three-tier watchdog system provides resilient health monitoring where each tier monitors the one below.

**Requirements:**
```
Daemon (Go process) ← heartbeat every 3 min
└── Boot (AI agent) ← intelligent triage
    └── Deacon (AI agent) ← continuous patrol
        └── Witnesses & Refineries ← per-project agents
```

**How It Works:**
- **Daemon** (Go process): Monitors Boot via heartbeat every 3 minutes. If Boot dies, Daemon restarts it.
- **Boot** (AI agent): Intelligent triage. Monitors Deacon. If Deacon gets stuck, Boot investigates and restarts.
- **Deacon** (AI agent): Continuous patrol across all projects. Monitors Witnesses and Refineries. Dispatches maintenance workers (Dogs) for issues.
- **Witnesses & Refineries**: Per-project agents that monitor worker agents (Polecats) and process merge queues.

Each tier can restart the one below, creating a resilient chain. This is Gas Town's hierarchical monitoring at scale.

### 5.2 Witness (Per-Project Health)

**Requirements:**
- Monitor project-specific agents
- Detect stuck agents
- Trigger recovery (nudge or handoff)
- Manage session cleanup
- Track completion

**Implementation:**
- Health check polling
- Stuck detection heuristics
- Recovery protocols
- Lifecycle management

### 5.3 Telemetry (OpenTelemetry)

**Requirements:**
- Structured logs and metrics for all operations
- Session lifecycle events
- Agent state changes
- Command durations
- Work tracking operations

**Implementation:**
- OTLP-compatible backend
- Structured event schema
- Real-time dashboards
- Historical analysis

---

## 6. Human Interface System

### 6.1 CLI

**Requirements:**
- Primary interface for all operations
- Convoy management
- Agent operations
- Configuration
- Monitoring and health

**Implementation:**
- Comprehensive command set
- Shell completions
- Help system
- Error messages with recovery suggestions

### 6.2 Dashboard

**Requirements:**
- Web-based monitoring interface
- Real-time agent activity
- Convoy status
- Merge queue state
- Escalations
- Metrics and trends

**Implementation:**
- Auto-refreshing UI
- Command palette
- Historical data views
- Export capabilities

### 6.3 Band (Metrics Display)

**Requirements:**
- Non-intrusive metrics display
- Cost per task and per turn
- Token usage and agent time
- Code reuse percentage
- Test status after last change
- Foldable to one line

**Implementation:**
- Runtime-specific integration (Claude Code, etc.)
- Real-time updates
- Historical tracking
- Board view for cross-project metrics

### 6.4 Escalation Channels

**Requirements:**
- Severity-routed escalation
- P0 (Critical) → Immediate human attention
- P1 (High) → Mayor intervention
- P2 (Medium) → Deacon patrol

**Implementation:**
- Escalation creation and tracking
- Notification system
- Resolution workflow
- Escalation history

---

## 7. Runtime Flexibility

### 7.1 Multi-Runtime Support

**Requirements:**
- Claude Code (default, with hooks)
- GitHub Copilot (with executable lifecycle hooks)
- Codex, Gemini, Cursor, Kiro, and others
- Custom agent presets via configuration

**Implementation:**
- Runtime-agnostic skill format
- Runtime-specific adapters
- Hook system for lifecycle events
- Configuration per runtime

### 7.2 Model Policy

**Requirements:**
- Role-based model mapping
- User override capability
- Per-runtime defaults
- Reasoning effort per role

**Implementation:**
- Canonical roles definition
- User override sheet
- Model selection logic
- Effort level configuration

---

## Conflicts and Decision Points

### 🚨 CONFLICT 1: Minimalism vs. Specialized Agents

**Issue:** Ponytail's radical minimalism (solve before writing) conflicts with BMAD's specialized agent approach (PM, Architect, UX, Dev, Analyst).

**Conflict:**
- Ponytail: "The best code is the code never written" - minimize everything
- BMAD: "Different aspects need different expertise" - multiple specialized agents

**Decision Needed:**
- **Option A:** Minimalism First - All agents follow the ladder principle, specialized agents only invoked when ladder fails
- **Option B:** Specialization First - Specialized agents make decisions, minimalism applied during implementation
- **Option C:** Hybrid - Router decides based on task complexity: simple tasks → minimalism only, complex tasks → specialized agents with minimalism enforcement

**Recommendation:** Option C (Hybrid)
- Simple, clear changes: Direct to minimalist implementation
- Medium complexity: Architect + minimalist Developer
- Large initiatives: Full specialized agent panel with minimalism enforcement at implementation

---

### 🚨 CONFLICT 2: Grilling vs. Propulsion Principle

**Issue:** Matt Pocock's grilling sessions (deep questioning before implementation) conflict with Gas Town's propulsion principle (if work is hooked, execute immediately).

**Conflict:**
- Skills: "Grill before implementing" - alignment through deep questioning
- Gas Town: "Hook → Execute" - no confirmation, no questions, no waiting

**Decision Needed:**
- **Option A:** Grilling Always - All work goes through grilling first, then hooks
- **Option B:** Propulsion Always - Hooked work executes immediately, grilling only for new requests
- **Option C:** Conditional - User-initiated work gets grilling, agent-to-agent handoffs execute immediately

**Recommendation:** Option C (Conditional)
- Human → Agent: Grilling session for alignment
- Agent → Agent: Hooked work executes immediately (propulsion)
- Escalations: Grilling at escalation point, then execution

---

### 🚨 CONFLICT 3: Convention Over Configuration vs. Model Policy Separation

**Issue:** BMAD's "convention over configuration" (minimal instructions) conflicts with pstack's model policy separation (role-based model mapping with user overrides).

**Conflict:**
- BMAD: "Delete instructions rather than hedge them" - trust model intelligence
- pstack: "Different roles need different model capabilities" - explicit configuration

**Decision Needed:**
- **Option A:** Convention Wins - Single model, minimal configuration, trust intelligence
- **Option B:** Policy Wins - Explicit role-to-model mapping, user overrides
- **Option C:** Tiered - Default to convention, allow policy overrides for power users

**Recommendation:** Option C (Tiered)
- Default: Single model, minimal configuration
- Advanced: Role-based model mapping for users who need it
- Configuration optional, not required

---

### 🚨 CONFLICT 4: Diverse Panel vs. Single Agent Efficiency

**Issue:** pstack's diverse panel (3 models for critical decisions) conflicts with efficiency and cost optimization.

**Conflict:**
- pstack: "Three-model panels improve decision quality through diversity"
- Efficiency: "More models = more cost, more time, more tokens"

**Decision Needed:**
- **Option A:** Always Panel - Critical decisions always use 3 models
- **Option B:** Never Panel - Single model for all decisions
- **Option C:** Selective Panel - User configures which decisions warrant panel

**Recommendation:** Option C (Selective Panel)
- Default: Single model
- Critical decisions (architecture, security, data loss): Optional panel
- User configures panel threshold
- Track panel vs. single-model outcomes

---

### 🚨 CONFLICT 5: Federated Work Coordination vs. Single Workspace

**Issue:** Gas Town's Wasteland (federated work across multiple workspaces) adds complexity that may not be needed initially.

**Conflict:**
- Gas Town: "Federation enables horizontal scaling across workspaces"
- Simplicity: "Start with single workspace, add federation later"

**Decision Needed:**
- **Option A:** Federation from Day 1 - Build Wasteland from the start
- **Option B:** Single Workspace Only - Never implement federation
- **Option C:** Phased Approach - Single workspace MVP, federation in v2

**Recommendation:** Option C (Phased Approach)
- MVP: Single workspace with all other features
- v2: Add Wasteland federation if demand exists
- Design with federation in mind, implement later

---

### 🚨 CONFLICT 6: Test Coverage Requirements

**Issue:** Different systems have different test coverage philosophies.

**Conflict:**
- Ponytail: "Logic leaves a test" - selective testing for risky code only
- Skills: "TDD for all features" - red-green-refactor for everything
- BMAD: "Test generation for verification" - comprehensive test suites

**Decision Needed:**
- **Option A:** Ponytail's Selective - Only risky logic gets tests
- **Option B:** Skills' TDD - Everything gets red-green-refactor
- **Option C:** Tiered - User configures test coverage level per project

**Recommendation:** Option C (Tiered)
- Default: Ponytail's selective testing (risky logic only)
- Strict mode: TDD for all features
- Project-level configuration
- Track test coverage and bug escape rate per mode

---

### 🚨 CONFLICT 7: Shortcut Comments vs. No Comments

**Issue:** Ponytail's shortcut comments conflict with minimalism principle of "comment only the why."

**Conflict:**
- Ponytail: "Mark shortcuts with structured comments for debt tracking"
- Minimalism: "Comment only what code cannot show"

**Decision Needed:**
- **Option A:** Shortcut Comments Always - Track all deferred work
- **Option B:** No Shortcut Comments - Code should be complete or not shipped
- **Option C:** Optional Tracking - User enables shortcut tracking per project

**Recommendation:** Option A (Shortcut Comments Always)
- Structured comments are metadata, not explanation
- Debt tracking prevents "later" becoming "never"
- Harvesting into ledger provides visibility
- Not a violation of minimalism (it's tracking, not explanation)

---

### ⚠️ DECISION POINT 1: Primary Persistence Mechanism

**Options:**
- **A:** Git worktrees only (Gas Town approach)
- **B:** Beads/Dolt only (structured issue tracking)
- **C:** Both (git for state, Beads for work tracking)

**Recommendation:** Option C (Both)
- Git worktrees for agent state (hooks)
- Beads/Dolt for work tracking (issues, convoys)
- Clear separation of concerns
- Each optimized for its purpose

---

### ⚠️ DECISION POINT 2: Issue Tracker

**Options:**
- **A:** Beads/Dolt (Gas Town approach)
- **B:** GitHub Issues (native integration)
- **C:** Pluggable (support multiple trackers)

**Recommendation:** Option C (Pluggable)
- Default: Beads/Dolt for local-first
- Support: GitHub, GitLab, Jira
- Adapter pattern for tracker integration
- User chooses per project

---

### ⚠️ DECISION POINT 3: Telemetry Backend

**Options:**
- **A:** OpenTelemetry to any OTLP backend
- **B:** Built-in metrics database
- **C:** Optional telemetry (privacy-first)

**Recommendation:** Option C (Optional)
- Default: Local metrics only (Band data)
- Optional: OpenTelemetry export
- User controls data destination
- Privacy-first design

---

### ⚠️ DECISION POINT 4: Installation Method

**Options:**
- **A:** Plugin marketplace (auto-update)
- **B:** Git clone (editable)
- **C:** Both (dual installation paths)

**Recommendation:** Option C (Both)
- Plugin for convenience and auto-update
- Git clone for customization
- Symlink-based shared installation
- User chooses per need

---

### ⚠️ DECISION POINT 5: Default Minimalism Level

**Options:**
- **A:** Lite (minimal enforcement)
- **B:** Full (standard enforcement)
- **C:** Ultra (aggressive enforcement)
- **D:** Off (no enforcement)

**Recommendation:** Option B (Full)
- Default: Full minimalism enforcement
- User can adjust per project
- Track outcomes per level
- Prove minimalism works by default

---

## Success Metrics

### Code Quality Metrics
- **Lines of code reduction:** Target -40% vs. no-skill baseline
- **Test coverage for risky logic:** Target 95%+
- **Bug escape rate:** Track bugs found in production vs. caught by tests
- **Code reuse percentage:** Track reuse vs. new code written

### Performance Metrics
- **Cost reduction:** Target -25% vs. no-skill baseline
- **Time reduction:** Target -35% vs. no-skill baseline
- **Token reduction:** Target -40% vs. no-skill baseline
- **Agent time:** Track total agent time per task

### Reliability Metrics
- **Agent uptime:** Target 99%+ (crashes don't lose work)
- **Merge queue throughput:** Track merges per hour
- **Escalation resolution time:** Track P0/P1/P2 resolution times
- **Context recovery time:** Track time to recover from crash

### Scale Metrics
- **Concurrent agents:** Support 20-30+ agents
- **API rate limit compliance:** Zero rate limit violations
- **Session duration:** Track session length before handoff needed
- **Work completion rate:** Track tasks completed vs. abandoned

---

## Implementation Phases

### Phase 1: Foundation (MVP)
**Duration:** 8-12 weeks

**Deliverables:**
- Git-backed state storage (hooks)
- Basic issue tracking (Beads/Dolt)
- Mayor coordinator
- Worker agents (Polecats)
- Minimalism enforcement (ladder)
- Basic merge queue (Refinery)
- CLI interface
- Single runtime support (Claude Code)

**Success Criteria:**
- 5 concurrent agents working reliably
- Work survives crashes
- Minimalism reduces code by 30%+
- Merge queue prevents broken main

### Phase 2: Specialization
**Duration:** 6-8 weeks

**Deliverables:**
- Specialized agents (PM, Architect, UX, Dev, Analyst)
- Grilling sessions
- Domain modeling (GLOSSARY.md, ADRs)
- TDD enforcement
- Code review (two-axis)
- Audit system
- Router (skill selection)

**Success Criteria:**
- Complex tasks use specialized agents
- Grilling catches misalignment
- Shared language reduces verbosity
- Review catches production issues

### Phase 3: Monitoring
**Duration:** 4-6 weeks

**Deliverables:**
- Three-tier watchdog system
- Witness (per-project health)
- Deacon (cross-project patrol)
- Telemetry (OpenTelemetry)
- Dashboard
- Band (metrics display)
- Escalation system

**Success Criteria:**
- Stuck agents detected and recovered
- 20+ agents monitored reliably
- Real-time visibility into all operations
- Escalations routed correctly

### Phase 4: Scale
**Duration:** 6-8 weeks

**Deliverables:**
- Scheduler (capacity management)
- Multi-runtime support
- Model policy separation
- Session discovery (Seance)
- Pluggable issue trackers
- Advanced merge queue features

**Success Criteria:**
- 30+ concurrent agents
- Zero API rate limit violations
- Works across Claude, Copilot, Codex, Gemini
- Context recovery from any previous session

### Phase 5: Federation (Optional)
**Duration:** 8-10 weeks

**Deliverables:**
- Wasteland (federated work coordination)
- Cross-workspace work claiming
- Reputation system
- Evidence submission
- Multi-dimensional stamps

**Success Criteria:**
- Work distributed across multiple workspaces
- Reputation tracks quality
- Evidence proves completion

---

## Technical Stack

### Core Infrastructure
- **Language:** Go (daemon, CLI, core services)
- **Agent Runtime:** Python (AI agent execution)
- **State Storage:** Git (worktrees for hooks)
- **Work Tracking:** Beads/Dolt (issue tracking)
- **Telemetry:** OpenTelemetry (OTLP)
- **Dashboard:** Go + htmx (web UI)

### Agent Runtimes
- **Primary:** Claude Code (with hooks)
- **Secondary:** GitHub Copilot, Codex, Gemini, Cursor, Kiro
- **Adapter:** Runtime-specific integration layer

### Data Storage
- **Git:** Agent state, decision artifacts
- **Dolt:** Issue tracking, work history
- **SQLite:** Local metrics (Band data)
- **OTLP Backend:** Optional telemetry export

---

## Open Questions

1. **Multi-model panel cost:** How do we balance decision quality vs. cost for diverse panels?
2. **Grilling frequency:** How often should grilling sessions run vs. direct execution?
3. **Test coverage threshold:** What's the right balance between selective and comprehensive testing?
4. **Federation timing:** When is the right time to add Wasteland federation?
5. **Telemetry privacy:** What's the right default for telemetry (on, off, local-only)?
6. **Minimalism enforcement:** Should minimalism be enforced at prompt level or verification level?
7. **Escalation thresholds:** What triggers P0 vs. P1 vs. P2 escalations?
8. **Session handoff:** When should agents hand off vs. continue?

---

## Risks and Mitigations

### Risk 1: Complexity Overload
**Risk:** Combining 5 systems creates overwhelming complexity.  
**Mitigation:** Phased rollout, start with MVP, add features incrementally.

### Risk 2: Conflicting Principles
**Risk:** Unresolved conflicts between systems cause confusion.  
**Mitigation:** Clear decision points documented, user can configure behavior.

### Risk 3: Performance Degradation
**Risk:** Multiple verification layers slow down development.  
**Mitigation:** Parallel execution where possible, configurable verification depth.

### Risk 4: Cost Explosion
**Risk:** Multi-agent coordination and diverse panels increase costs.  
**Mitigation:** Capacity governance, selective panel usage, cost tracking and alerts.

### Risk 5: Adoption Friction
**Risk:** System too complex for new users to adopt.  
**Mitigation:** Sensible defaults, progressive disclosure, excellent documentation.

### Risk 6: Runtime Fragmentation
**Risk:** Supporting multiple runtimes creates maintenance burden.  
**Mitigation:** Runtime-agnostic core, adapter pattern, automated testing across runtimes.

---

## Appendix A: Glossary

- **Hook:** Git worktree for persistent agent state
- **Convoy:** Work bundle with dependency tracking
- **Polecat:** Worker agent spawned for specific task
- **Mayor:** Coordinator agent, primary human interface
- **Witness:** Per-project health monitor
- **Deacon:** Cross-project patrol agent
- **Refinery:** Merge queue processor
- **Ladder:** Minimalism checklist (solve before writing)
- **Grilling:** Deep questioning session for alignment
- **Seance:** Session discovery and context recovery
- **Band:** Non-intrusive metrics display
- **Escalation:** Severity-routed blocker reporting

---

## Appendix B: References

- Gas Town: https://github.com/steveyegge/gastown
- BMAD Method: https://github.com/bmad-code-org/BMAD-METHOD
- pstack-claude: https://github.com/michael-denyer/pstack-claude
- Ponytail: https://github.com/DietrichGebert/ponytail
- Matt Pocock's Skills: https://github.com/mattpocock/skills

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-10-17 | System | Initial draft synthesizing 5 systems |

---

**Next Steps:**
1. Review conflicts and decision points with stakeholders
2. Prioritize Phase 1 features for MVP
3. Create detailed technical design documents
4. Set up development environment and CI/CD
5. Begin Phase 1 implementation
