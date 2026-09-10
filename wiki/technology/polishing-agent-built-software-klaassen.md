---
type: literature-note
source_url: https://every.to/source-code/how-i-polish-software-that-agents-built
author: Kieran Klaassen
tags: [ai-agents, software-engineering, polish, compound-engineering]
date_consumed: 2026-09-10
---

## Summary

Kieran Klaassen argues that as AI agents automate coding, the irreducible human contribution shifts to **polish** — the embodied judgment about whether something actually *feels* right to use. He describes a workflow where agents ship overnight pull requests and his morning job is evaluating quality, using his `/ce-polish` command to open the running app beside the agent for a tight feedback loop. Crucially, each correction becomes a learned rule the agent applies automatically in future iterations.

## Core Concepts

- **[[Polish as Non-Delegable Work]]** — agents cannot know what you *meant* to build; only the human can judge feel and intent
- **[[Compound Engineering Plugin]]** — Klaassen's open-source plugin enabling the `/ce-polish` workflow: app running beside the agent, hot-reload on every fix
- **[[Agentic Overnight PRs]]** — agents ship pull requests asynchronously; human review is the morning ritual rather than the bottleneck
- **[[Feedback Loop Teaching]]** — each caught error propagates a rule back to the agent, reducing future occurrences automatically
- **[[Spec-Driven Development]]** — polish sharpens planning because you now write specs around anticipated *feel*, not just behavior
- **[[Kieran Klaassen]]** — engineer at Every, author of the compound engineering methodology

## Key Takeaways

- **Polish is non-delegable**: agents can't infer intended feel — only the human can.
- **Tight feedback loop**: use app → notice what's off → tell agent → hot-reload → repeat.
- **Rules accumulate**: first correction requires explicit instruction; thereafter agent self-applies.
- **Planning improves**: specs now encode anticipated feel, not just functional requirements.
- **Review stress drops**: knowing you'll polish later reduces pressure during initial generation.
- **Constraint shifts**: cost of scrapping and replanning "all but disappeared" — bottleneck is now quality, not speed.
- **Wrong-direction animation example**: agent fixed slide-in animation origin after one human flag.

## 🧠 First Principles & Mental Models

- **[[Feedback Loops]]**: The `/ce-polish` workflow operationalizes tight human-agent feedback — each correction is immediately testable via hot-reload, compressing the loop that normally spans days of code review cycles.
- **[[Tacit Knowledge]]**: Polish encodes the designer's tacit knowledge of intended feel, which cannot be fully specified upfront — Klaassen's workflow externalizes this knowledge into agent rules incrementally rather than trying to front-load it all in specs.

## 🃏 Review Questions

**Q1**: What does Klaassen argue is the non-delegable human contribution in an AI-agent coding workflow?
**A**: Polish — the judgment about whether something actually *feels* right — because agents cannot know what you meant to build.

**Q2**: How does the `/ce-polish` feedback loop work mechanically?
**A**: The command opens the running app beside the agent; the human uses the app, notices what's off, tells the agent, and hot-reloads — repeating until the feel is right.

**Q3**: How does catching a polish issue once affect future agent behavior?
**A**: The agent learns the rule from the first correction and applies it automatically afterward, reducing the human's recurring intervention over time.
