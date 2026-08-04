# Graph Engineering: Verification Strategies for Multi-Agent Graphs

## Loop Engineering vs. Graph Engineering

**Loop engineering** hands an agent a goal and lets it work sequentially: each step waits on the previous one before starting. Steps with no dependency on each other still serialize, wasting time.

**Graph engineering** decomposes the main task into parallel sub-tasks, each owned by a dedicated agent (node). Data flows between agents via edges. Results:
- **Speed**: multiple agents run concurrently instead of one grinding sequentially.
- **Cost per agent**: cheaper models can handle simpler nodes, avoiding burning expensive models on low-complexity work.
- **Cost overall**: total token consumption is higher — a full fleet of agents burns far more tokens than a single agent. The $20 Claude Code / Codex plans hit limits quickly under graph workloads.

Claude Code's **dynamic workflow** (fan-out to sub-agents) is already a graph in this sense.

## Graph Anatomy

| Component | Definition |
|-----------|-----------|
| **Node** | A single sub-task running in its own isolated context window |
| **Edge** | Controls how one node's output reaches the right downstream node |

### Common Graph Shapes

- **Diamond**: One root task fans out to parallel sub-agents; results converge into a single synthesis agent.
- **Fan-in at barrier**: Multiple agents analyze the same input from different angles; nothing proceeds until all have reported back, then a fix agent runs.

## The Core Verification Problem

With a fleet of agents running concurrently:
- A large volume of output arrives at once — hard to review manually.
- There is no visibility into what caused a failure.
- One wrong agent's output propagates silently into downstream nodes.

Built-in agent self-verification (running tests, checking errors) only catches major failures — it does not enforce code style, architectural standards, or alignment with original requirements.

## Three Tiers of Verification Skills

### 1. Standalone Skills
Run only when explicitly invoked. Designed for deep, post-completion review of finished work. Examples:
- **Thermonuclear code review** (Cursor): fans out agents for multi-angle security review; all findings merged into one report.
- Best built via the **Skill Creator plugin** in Claude Code with a "comprehensive" review instruction.

### 2. Embedded Skills
Fire automatically as part of the running workflow without user prompting. Suitable for enforcing standards on every feature implementation. Key constraint: pre-installed skills (verify, code-review) cannot be auto-invoked — only user-built embedded skills can be wired to fire automatically.

### 3. Skill Chains + Orchestrator
No single skill covers all verification angles. Anthropic's own team chains:
- **code-review** → **simplify** → **verify** → **design** (checks against `design.md`)

To avoid overloading agents, each angle gets its own skill. An **orchestrator skill** sits above the chain: its only job is to spin up a parallel agent per review skill, collect all findings, and return a unified report. When building a graph, you reference only the orchestrator — the fan-out happens automatically.

## Model Quality in Verification

Running a review skill on a cheap model (Haiku) produces a long findings list but poor signal quality — it flags intentional code as errors because it lacks the context to distinguish intent. Running the same skill on Opus produces fewer findings with higher signal.

Inside a graph, a bad reviewer triggers agents to "fix" things that were never broken, burning tokens across every node simultaneously with no visibility into the source. **The review node is the one place where saving tokens costs you everything.**

## Second Opinion Skill

The agent that built the code is the worst reviewer of that code — it judges from the same context it used to build it. A **second opinion skill** launches a separate Claude Code session via the `-p` flag, giving it the code without any prior conversation context. This produces an unbiased review. Tradeoffs:
- Takes significantly longer to return (full separate session startup).
- Worth running on Opus explicitly, since the entire value is a smarter second read.
- Each node in a graph can invoke this, giving every node an independent reviewer.

## Chrome Headless Shell for Visual Verification

Browser-based feature verification normally opens a full Chrome instance — memory-heavy and slow inside a workflow loop. **Chrome headless shell** strips out non-essential browser components while retaining the ability to load pages and take screenshots. Embeds naturally into verification skills; reduces per-check overhead significantly.

## CLAUDE.md and Skill Invocation

Writing project-specific build/test commands into `CLAUDE.md` prevents agents from re-discovering them on every run — a small but compounding efficiency gain at graph scale.

## Source

- Video: [Anthropic Just Fixed Graph Engineering's Greatest Flaw](https://www.youtube.com/watch?v=H7t3uUp3HVw) — AI LABS, July 2026

## Related Notes

- [[loop-engineering-agent-loop-design]]
- [[loop-engineering-guide-safe-autonomous-agents]]
- [[experience-memory-graph-emg-agent-error-correction]]
- [[agentic-design-patterns-reflection]]
- [[ai-agents-claude-skills-methodology]]
- [[agent-skills-vs-mcp-claude-code-era]]
- [[agentic-engineer-workflow-parallel-sessions-2026]]
