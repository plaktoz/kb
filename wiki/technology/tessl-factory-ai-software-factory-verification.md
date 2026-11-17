---
type: literature-note
source_url: https://itbrief.co.uk/story/tessl-launches-ai-software-factory-for-engineering-teams
author: Joseph Gabriel Lagonsin
tags: [ai-agents, software-factory, verification, agentic-engineering]
date_consumed: 2026-11-18
---

## Summary

London startup [[Tessl]] launched Tessl Factory, a platform that turns repositories into repeatable agent workflows built from reusable "skills" and verification-bearing "loops". Founder [[Guy Podjarny]] argues the hard problem is no longer assigning work to agents but defining task boundaries, knowing when to stop, and verifying output. Tessl reports 80% of one week's internal PRs needed no hand-editing and cost per PR fell from $75 to $13.

## Core Concepts

- [[Tessl Factory]]: agent-agnostic, model-agnostic platform with a declarative workflow approach.
- [[Agent Skills]] and [[Agentic Loops]]: skills define how agents do a task; loops chain skills with verification steps.
- [[Agentic Software Factory]]: repeatable ticket-to-PR style pipelines rather than a single assistant per developer.
- [[Verification]] and [[AI Agent Governance]]: boundaries, stop conditions and checks against repo rules.
- [[Guy Podjarny]]: Tessl founder, previously founded [[Snyk]] and was CTO at [[Akamai]].
- Initial templates: Ticket to PR, Code Review, Vulnerability Remediation.

## Key Takeaways

- **Funding**: Tessl, founded 2024, has raised $125M (Index, Accel, GV, boldstart).
- **Constraint Shift**: The bottleneck moves from generating code to verifying it.
- **Internal Results**: 80% of one week's PRs needed no human hand-editing.
- **Cost Drop**: Cost per pull request fell from $75 to $13.
- **Governance Focus**: Define task boundaries, stop agents overreaching, verify before production.
- **Gradual Autonomy**: Verification accompanies increased agent autonomy, paced by the team.
- **Trial Incentive**: $200 usage credits offered to first-time teams.

## 🧠 Core Principles

**T1. Relieving one bottleneck exposes the next** — When generation becomes cheap, the binding constraint moves to verification, review and cost control. → explains: Constraint Shift, Governance Focus · *model:* [[Theory of Constraints]]

**T2. Autonomy scales only with verification** — Delegating more to agents is safe only as fast as checks on their output can keep pace. → explains: Gradual Autonomy, Governance Focus · *model:* [[Trust but Verify]]

## 🃏 Review Questions

**Q1**: What is the core claim behind Tessl Factory?
**A**: The constraint in AI-assisted development has shifted from generating code to checking that agent-produced code is reliable, secure and worth the cost. A factory model with verification loops addresses that.

**Q2**: What evidence does Tessl give that the approach works?
**A**: Internally, 80% of one week's pull requests needed no human hand-editing, and cost per PR fell from $75 to $13.

**Q3**: How would a team apply this?
**A**: Define agent tasks as reusable skills, combine them into loops with verification steps, and start with templates such as Ticket to PR, Code Review or Vulnerability Remediation, expanding autonomy gradually.
