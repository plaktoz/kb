---
type: literature-note
source_url: https://claude.dev/blog/solving-code-review-at-anthropic/
author: Addy Osmani
tags: [code-review, ai-agents, software-engineering, anthropic]
date_consumed: 2026-10-17
---

## Summary

The Claude Code team at Anthropic has radically restructured code review so that machines do most of the reading and humans are reserved for decisions only people can make. From June to September 2026, merged PRs more than doubled while revert rates fell over 40%, achieved by layering automated pre-PR review, per-PR AI review, security review, risk-tiered human approval, and fast rollback rather than eliminating human judgment.

## Core Concepts

- **Review's two jobs**: (1) Find and fix issues before shipping; (2) build shared codebase context across the team — machines now handle most of job 1
- **[[CLAUDE.md]] / [[REVIEW.md]]** — Instructional files telling AI reviewers project conventions and what failure looks like per code area; core to reducing noise
- **Layer-by-layer review pipeline**: Pre-PR (subagent review + skills); per-PR AI review; security review; automated CI; risk-tiered human approval; merge queue; fast rollback
- **Vote-based finding verification** — Multiple agents independently flag a finding; it only surfaces if enough agree, filtering false positives before humans see them
- **Risk-tiered human approval** — A change's risk tier (set by a classifier on the diff, not the author) determines review depth; trusted authors on sensitive paths always need a person
- **Review convergence problem** — Agent author + agent reviewer can loop indefinitely; a round cap (3 rounds), diff-only re-review, and no-repeat rules break the cycle
- **"You land it, you own it"** — Accountability norm ensures humans remain responsible for every shipped change regardless of whether an agent wrote it
- **Human jobs that remain**: Direction and scope decisions; risky code (billing, auto-updater, CI); architecture that sets patterns; reading evidence; owning outcomes

## Key Takeaways

- **Volume**: Anthropic's monorepo grew from ~2,500 to ~30,000 daily changes (May to September 2026).
- **Substantive review rate**: Share of PRs getting substantive comments went from 16% to 54% after AI review launched.
- **Merged PRs doubled, reverts fell 40%**: Achieved without removing human judgment — by routing it better.
- **Round cap**: After 3 review rounds, the reviewer stops and asks the author to reconsider the approach.
- **59% old bugs**: ~59% of what the reviewer flagged was code that had been there since the first pass.
- **Agent approval ≠ human approval**: A bot's approval never fills a required human reviewer slot.
- **Code review's second job**: Teams are adapting — ask Claude to explain a module rather than reading trivial diffs.
- **Incidents become evals**: Past PRs that caused incidents feed a daily scorer to keep the reviewer calibrated.

## 🧠 Core Principles

**T1. Move quality gates earlier, not just higher.** Most review now happens before a PR exists; catching issues pre-PR costs far less than catching them post-merge and is more effective than adding gates at the end. · *model:* [[Activation Energy]]
→ explains: Layer-by-layer review pipeline, Merged PRs doubled, reverts fell 40%

**T2. Human attention is the true scarce resource in high-velocity engineering.** Preserving it for decisions machines cannot make — direction, architecture, accountability — is the core design goal, not maximizing automation for its own sake. · *model:* [[Theory of Constraints]]
→ explains: Human jobs that remain, Agent approval ≠ human approval

## 🃏 Review Questions

**Q1**: What is the central goal of Anthropic's code review redesign?
**A**: To minimize the human review time required per change without increasing reverts or incidents — routing human attention only to issues that machines cannot catch.

**Q2**: How does the vote-based finding system reduce noise?
**A**: Multiple independent agents examine the same diff simultaneously; a finding is only surfaced to human reviewers if enough agents agree it is real, filtering false positives before they reach a person.

**Q3**: What is the "review convergence" problem and how is it addressed?
**A**: An AI author and AI reviewer can endlessly exchange fixes and new findings in a feedback loop. The team imposes a round cap (3 rounds), restricts re-review to only the new diff, and bans repeating already-posted findings to force convergence.
