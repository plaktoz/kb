---
type: literature-note
source_url: https://www.youtube.com/watch?v=rmvDxxNubIg
author: AI Engineer
tags: [context-engineering, research-plan-implement, brownfield, coding-agents]
date_consumed: 2026-09-01
---

## Summary

Dex Horthy (HumanLayer) presents advanced context engineering for coding agents in brownfield codebases, arguing that most AI-generated code underperforms because of poor context management rather than model limitations. His team's "research → plan → implement" workflow (now called RPI) plus intentional compaction keeps the context window in the "smart zone" and eliminates slop — demonstrating 2–3x throughput on existing complex codebases.

## Core Concepts

- **[[Smart Zone vs Dumb Zone]]** — the first ~40% of a context window produces quality outputs; beyond ~40% fill, diminishing returns set in; working entirely in the dumb zone (e.g., too many MCPs) produces poor results regardless of model quality
- **[[Intentional Compaction]]** — actively compressing the context window into a markdown file before starting fresh; review, tag, and hand off to a new agent so it starts informed rather than from scratch
- **[[Research → Plan → Implement (RPI)]]** — three-phase workflow: research (find exact files and line numbers relevant to the problem), plan (outline steps with file names, line snippets, and test verification steps), implement (agent executes the plan with minimal context); phases keep the context window small
- **[[Sub-agents for Context Control]]** — sub-agents are not for anthropomorphizing roles (front-end, back-end, QA); they're for forking a fresh context window to do codebase research and returning a succinct answer to the parent
- **[[Mental Alignment]]** — code review's real purpose is keeping a team on the same page about how the codebase is changing and why; at 2–3x output, plans replace diffs as the review artifact; Dex reads plans, not 1000-line PRs
- **[[Spec-Driven Dev]]** ([[Semantic Diffusion]]) — the term has semantically diffused into meaninglessness; some mean a better prompt, some mean a PRD, some mean markdown files during coding; Horthy argues "harness engineering" is the more precise term
- **[[HumanLayer]]** — Dex's company building an agentic IDE to help teams run 99% AI-generated code

## Key Takeaways

- Most AI coding fails not because the model is bad but because the context is wrong: incorrect info > missing info > too much noise
- Trajectory matters: if previous turns show "made mistake → human yelled → made mistake → human yelled," the model's next most likely token is another mistake
- At ~40% context fill, performance degrades; too many MCPs push all work into the dumb zone permanently
- Sub-agents: "go find how this works in the codebase and return just the file name and relevant lines" — radically compresses parent agent context
- Planning prompt output should contain actual code snippets of what will change — reliability increases with plan length until readability suffers; find the sweet spot for your team
- "Do not outsource the thinking" — AI cannot replace thinking, only amplify it; a bad line of research is potentially 100 bad lines of code
- Code translation (Python → Go) works extremely well because the source code IS the spec — lessons for how specs should be written
- Teams are at different ends of a rift: staff engineers who don't adopt AI (slop cleanup duty) vs. mid-levels who use AI heavily; cultural change must come from the top

## 🧠 First Principles & Mental Models

- **[[Signal-to-Noise in Context]]**: Every token in the context window competes for the model's attention; incorrect/irrelevant context is actively worse than missing context because it shapes the probability distribution of the next token in the wrong direction — the model isn't "confused," it's doing its job on bad input
- **[[Leverage Points in Development]]**: Moving human effort earlier in the pipeline (from code review → plan review → research review) is not just faster — each stage upstream multiplies the blast radius of a correction; a wrong assumption in research causes exponentially more rework than a wrong line of code

## 🃏 Review Questions

**Q1**: What is the "dumb zone" and why does it persist even with capable models?
**A**: The dumb zone is the portion of the context window past roughly 40% fill, where model performance degrades; too many MCPs or verbose context loading means the agent is always operating there, producing poor results regardless of model quality.

**Q2**: Why are sub-agents not for anthropomorphizing roles (front-end, QA, etc.)?
**A**: Sub-agents are for context isolation — forking a fresh context window to do expensive codebase search/understanding, then returning only the relevant summary; assigning them human roles conflates organizational structure with a technical tool for managing token budgets.

**Q3**: How does the research → plan → implement workflow protect against slop in brownfield codebases?
**A**: By compacting each phase into a markdown artifact (research doc → plan doc), the implementing agent starts with exactly the relevant files, line numbers, and step-by-step instructions — minimizing hallucination risk and keeping the context window in the smart zone throughout.
