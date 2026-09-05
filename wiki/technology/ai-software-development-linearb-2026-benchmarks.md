---
type: literature-note
source_url: https://linearb.io/library/ai-in-software-development
author: LinearB Research
tags: [ai-coding, developer-productivity, software-engineering, agentic-ai]
date_consumed: 2026-09-05
---

## Summary
LinearB's 2026 benchmark study of 8.1 million pull requests across hundreds of engineering teams identifies three distinct PR archetypes — fully agentic (AI-opened and AI-reviewed), AI-assisted, and unassisted — and finds that AI-generated PRs have a 32.7% acceptance rate versus 84.4% for manually written code, revealing that agentic AI produces significantly more churn and requires substantial human oversight to reach production quality.

## Core Concepts
- **[[Agentic PRs]]**: Pull requests opened and reviewed entirely by AI agents without human involvement; acceptance rate 32.7% vs. 84.4% for unassisted PRs — the quality gap reveals that AI autonomy does not yet match human judgment in production codebases.
- **[[AI-Assisted Development]]**: Human developers using AI tools (Copilot, etc.) to accelerate writing; occupies a middle ground between fully agentic and unassisted in both acceptance rate and cycle time.
- **[[PR Cycle Time]]**: The time from PR open to merge; AI-generated PRs show longer review cycles despite automated opening, as reviewers spend more time verifying AI output than human-written code.
- **[[Code Review Burden]]**: 81% of developers in Harness 2026 report increased code review time since adopting AI tools; LinearB data corroborates this — AI output requires more scrutiny, not less.
- **[[AI Software Factory]]**: Emerging model where AI agents handle PR generation and initial review; viable but requires architectural changes (test coverage, quality gates) before autonomous AI PRs match human acceptance rates.

## Key Takeaways
- **3 PR archetypes**: fully agentic (AI opens + AI reviews), AI-assisted (human writes + AI assists), unassisted (fully human).
- **AI PR acceptance rate**: 32.7% vs. 84.4% for unassisted — 2.6x quality gap.
- **Dataset**: 8.1 million PRs across enterprise teams in 2026.
- **Review time rising**: 81% of developers report increased code review burden post-AI adoption.
- **Churn cost**: Low-acceptance AI PRs create cycle-time drag; gains from AI speed partially offset by review overhead.
- **The 1-in-3 pattern**: Roughly 1 in 3 AI-generated PRs ships without major revision; the other 2 require human rework.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: When velocity (PRs merged/week) becomes the goal metric, agentic AI optimizes for volume — but 32.7% acceptance rates reveal that output quantity is a poor proxy for engineering progress.
- **[[Automation Bias]]**: Engineers reviewing AI-generated PRs tend to under-scrutinize plausible-looking code, which is why explicit quality gates (not reviewer vigilance alone) are needed to protect codebase integrity.

## 🃏 Review Questions

**Q1**: What is the core finding of LinearB's 2026 AI in Software Development benchmark?
**A**: AI-generated (agentic) pull requests have a 32.7% acceptance rate versus 84.4% for manually written code — a 2.6x quality gap suggesting autonomous AI PRs require substantial human oversight to reach production quality.

**Q2**: What are the three PR archetypes LinearB identified, and what distinguishes them?
**A**: Fully agentic (AI opens and reviews with no human involvement), AI-assisted (human writes with AI tooling support), and unassisted (entirely human) — each representing a different level of AI involvement with distinct quality and cycle-time characteristics.

**Q3**: What does the 32.7% agentic PR acceptance rate imply for engineering teams adopting AI agents?
**A**: Teams should invest in quality gates, automated testing, and review processes that specifically handle AI-generated code at scale, rather than treating agentic PRs the same as human-authored ones.
