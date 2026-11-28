---
type: literature-note
source_url: https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes
author: Sarah Perez
tags: [anthropic, claude-ship, code-review, ai-agents]
date_consumed: 2026-11-26
---

## Summary
Anthropic launched Claude Ship, a suite of AI agents that review, fix and automatically approve routine code changes under team-written policies. The launch targets the review and approval bottleneck created by AI agents generating large amounts of code. Code Review is generally available, while PR Steward and Claude Approvals are in beta for Team and Enterprise plans on GitHub.

## Update (2026-11-25 Yahoo Finance report)
A Yahoo Finance report (Anwesha Pattanaik, https://finance.yahoo.com/news/anthropic-launches-claude-ship-beta-102850078.html) adds commercial and access details. Claude Ship is billed by tokens processed, with cost varying by PR size and number, review level and the amount of work PR Steward handles; administrators set spend limits for Code Review and PR Steward. It is not available to organisations with a HIPAA configuration, Zero Data Retention or customer-managed encryption keys. Eligible Claude Enterprise organisations can claim at least $10,000 in credits by 15 January 2027, to be used within 30 days of claiming. Users can invoke it through a new `/ship` command for individual PRs or enable it for entire repositories for automated operation, and it is rolling out to Claude Code and the Claude desktop app. The report stresses that human oversight remains, since teams may require human sign-off for certain changes. PR Steward does not approve or merge PRs; it comments and helps fix issues. The report also notes Anthropic's recent record IPO, raising $81.3bn at a fully diluted valuation of around $1.5tn.

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
- **Token Billing**: Charged by tokens processed; admins set spend limits for Code Review and PR Steward.
- **Excluded Orgs**: Unavailable with HIPAA configuration, Zero Data Retention or customer-managed keys.
- **Launch Credits**: Eligible Enterprise orgs can claim at least $10,000 by 15 January 2027.
- **Access Paths**: `/ship` command per PR, or repository-wide automation.

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
