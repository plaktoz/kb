---
type: literature-note
source_url: https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes
author: Sarah Perez
tags: [anthropic, claude-ship, code-review, ai-agents]
date_consumed: 2026-11-25
---

## Summary
Anthropic launched Claude Ship, a suite of AI agents that review, fix and automatically approve routine code changes under team-written policies. The launch targets the review and approval bottleneck created by AI agents generating large amounts of code. Code Review is generally available, while PR Steward and Claude Approvals are in beta for Team and Enterprise plans on GitHub.

## Core Concepts
- [[Anthropic]] and [[Claude Ship]]: a suite of agents covering everything after the pull request.
- [[Code Review]]: already generally available, with Quick, Standard and Deep review settings.
- [[PR Steward]]: fixes failing CI checks, merge conflicts and Code Review feedback, then comments on what changed and how to roll back.
- [[Claude Approvals]]: applies a natural-language approval policy stored as a file in the repository, using signals such as Code Review findings and classifiers.
- [[Human-in-the-Loop]]: teams choose which changes escalate to a human for a decision.
- [[AI Coding Agents]]: generate enough code that review and approval become bottlenecks.

## Key Takeaways
- **Approval Delegation**: Claude Approvals can approve changes automatically based on policies a team writes.
- **Bottleneck Shift**: Agent-written code creates review and approval backlogs before changes go live.
- **Team Dogfooding**: On the Claude Code team, Claude writes most of the code.
- **PR Steward**: Handles failing CI, merge conflicts and review feedback, and comments on rollback steps after each push.
- **Cautious Rollout**: Anthropic suggests observe-only mode, one repository, and monthly spending limits first.
- **Availability**: Claude Team and Enterprise plans, GitHub repositories only; two agents still in beta.

## 🧠 Core Principles

**T1. Bottlenecks move downstream** — When one stage of a pipeline speeds up, the constraint shifts to the next stage, so throughput gains require speeding up the stages after it too. · *model:* [[Theory of Constraints]]
→ explains: Bottleneck Shift, Team Dogfooding, Approval Delegation

## 🃏 Review Questions

**Q1**: What is the core idea behind Claude Ship?
**A**: As AI agents write more code, review and approval become the bottleneck, so Claude Ship extends automation to reviewing, fixing and approving changes after the PR.

**Q2**: How does Claude Approvals decide what to approve?
**A**: It applies an approval policy written in natural language as a file in the repository, drawing on signals such as Code Review findings and the company's own classifiers.

**Q3**: How should a team adopt the beta approval functionality?
**A**: Start in observe-only mode on a single repository with monthly spending limits, and keep control over review settings and which changes escalate to a human.
