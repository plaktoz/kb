---
source_url: https://linearb.io/library/ai-in-software-development
author: LinearB
date: 2026-09-05
---

# AI in software development: what the 2026 data shows

AI in software development is the use of AI tools and autonomous agents to write, review, and ship code across the development lifecycle, and in 2026 it splits into two patterns that behave differently. IDE assistants shape code a developer still owns, while agents open pull requests on their own. LinearB's 2026 Software Engineering Benchmarks Report, built from more than 8.1 million pull requests from 4,800 teams and 163,820 contributors across 42 countries, found that AI pull requests merge within 30 days 32.7% of the time against 84.4% for unassisted pull requests. Adoption is close to universal, and delivery has not followed it.

## Three contribution types, not one category

AI contributions divide into three distinct pull request types:

- **Agentic AI pull requests**: created by agents such as Devin, Copilot Coding Agent, or OpenAI Codex — the agent interprets a task, generates code, commits, and opens the PR
- **AI-assisted pull requests**: human-authored and shaped by AI, developer retains ownership
- **Unassisted pull requests**: authored without substantial AI involvement

| Pull request type | Median size (lines) | P75 size (lines) | Pickup Time P75 (hours) | Review Time P75 (hours) |
| --- | --- | --- | --- | --- |
| Agentic AI | 89 | 293 | 17.6 | 6.4 |
| AI-Assisted | 96 | 408 | 8.3 | 3.2 |
| Unassisted | 26 | 157 | 3.4 | 4.2 |

Two key patterns: AI-assisted PRs are the largest at P75, and review time inverts the pickup order — AI-assisted PRs clear review faster (3.2 hours) than unassisted (4.2 hours), even though they're larger.

## Output rose, acceptance fell

Acceptance rate (share of PRs merged within 30 days) is the metric that separates code produced from code delivered. Manual PRs merge at 84.4% against 32.7% for AI PRs — over 2x lower. The gap holds across every performance tier. Three drivers behind the gap: ownership of agent-created work is unclear, agentic flows are frequently pointed at low-priority backlog, and reviewers hesitate on larger AI changes.

## Why the bottleneck moved to review

Faster code generation moved the constraint downstream. Agentic PRs wait 17.6 hours for pickup against 3.4 hours for unassisted work. Only 39.4% of respondents are "somewhat confident" in AI-generated code quality; 33% are neutral; 19.1% are somewhat unconfident.

Refactor rate at P75 runs 0.37 for unassisted PRs, 0.22 for AI-assisted, and 0.17 for agentic — human-authored work touches existing code at more than 1.5x the rate. AI output skews toward new code paths, creating more surface area with less consolidation.

## What blocks teams from getting value

- **Data readiness**: 15.6% strongly disagree their internal data is high-quality and accessible for AI workflows; 64.5% total indicate data is not ready
- **Policy gap**: 30.5% strongly agree they have a clear AI usage policy; 21.1% strongly disagree
- 88.3% of surveyed organizations use AI-assisted tools daily or a few times a week (vs. 71.6% in early 2024)

Key takeaway: AI amplifies the capability an organization already has. Fix data and policy first; tool adoption follows.
