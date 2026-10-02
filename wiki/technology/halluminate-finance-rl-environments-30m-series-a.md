---
type: literature-note
source_url: https://www.techtimes.com/articles/328407/20261001/finance-ai-tops-out-51-due-diligence-startup-raises-30m-fix-it.htm
author: Ryan Cook
tags: [reinforcement-learning, rl-environments, finance-ai, ai-startups]
date_consumed: 2026-10-02
---

## Summary

[[Halluminate]], a nine-person San Francisco startup, raised a $30M Series A led by [[Oak HC/FT]] to sell finance-specific [[Reinforcement Learning]] training environments to frontier AI labs, after its own benchmark showed the best models score only 51% on realistic private-equity due diligence. The company argues finance is harder to train on than code because reward functions can't be checked programmatically; instead, expert rubrics built from real anonymized deals serve as the verifier. Its business depends on a "Moore's law of environments": environment complexity has to roughly double every six to eight months to keep producing a useful training signal as models improve.

## Core Concepts

- **[[Halluminate]]**: Founded in 2024 by CEO [[Jerry Wu]] and CTO [[Wyatt Marshall]]. It has raised $38.5M in total, is profitable at nine employees, and reports a mid-eight-figure annualized revenue run rate.
- **[[Westworld Finance Diligence Bench]]**: 88 tasks drawn from anonymized real PE transactions, written and reviewed by deal professionals. Seven frontier models topped out at a 51% average score.
- **[[RL Environments]]**: Interactive simulations where a model attempts a failing task, gets feedback, and iterates. Halluminate turns each observed agent failure pattern into one.
- **[[Reinforcement Learning from Verifiable Rewards]]**: Coding improved quickly because tests give binary, programmable rewards. Finance lacks this, so [[Expert Rubrics]] act as the verifier.
- **[[Long-Horizon Tasks]]**: Agents fail at carrying instructions through to the end of long, messy workflows, not at any single step.
- **Moore's Law of Environments**: Wu's claim that environment complexity must double every 6–8 months to stay at the frontier of model capability.
- **Verticalized Data Research Labs**: Wu's term for depth-over-breadth infrastructure that turns financial expertise into a training signal.
- **Post-Training Infrastructure Market**: Players include [[Scale AI]] (RL Environments product launched in early 2026) and [[Mercor]], which acquired [[Deeptune]] in July 2026, four months after Deeptune's $43M a16z-led Series A.
- **Investors**: [[Oak HC/FT]], led by GP [[Matt Streisfeld]], is a ~$5.3B fintech/healthcare specialist. [[Y Combinator]], Orange Collective, Heavybit, and FT Partners also joined, along with angels from [[Anthropic]], [[OpenAI]], and [[Meta]].

## Key Takeaways

- **Performance Ceiling**: The best frontier model averaged just 51% on PE due diligence.
- **Task Realism**: One task spanned 160 files, 21 emails, and four meeting-note sets.
- **Failure Modes**: Agents omit required changes, misapply methods, or act on superseded info.
- **Verification Gap**: Finance rewards need expert rubrics; programs can't check redlines.
- **Customer Concentration**: Four of the five top closed-source US labs pay Halluminate.
- **Lean Profitability**: Mid-eight-figure run rate with only nine employees.
- **Market Shift**: Nearly half of Scale AI's new data projects now involve RL environments.
- **Escalating Difficulty**: Environments that are too easy or too hard yield no learning signal.
- **Conflict Caveat**: Halluminate designs the benchmark and sells the fix; the 51% figure hasn't been independently validated.
- **Strategy**: Go deeper with frontier labs rather than expand to enterprise buyers.

## 🧠 First Principles & Mental Models

- **[[Zone of Proximal Development]]**: Effective RL environments must keep a model "hard enough to fail, but tractable enough to improve on," the same sweet spot where human learners make the most progress.
- **[[Red Queen Effect]]**: Because frontier models keep improving against them, environments must keep getting harder just to stay useful, which is what makes Halluminate's business an ongoing one.

## 🃏 Review Questions

**Q1**: What core gap does Halluminate's business exist to close?
**A**: Frontier AI models score only 51% on realistic private-equity due diligence. Halluminate sells finance-specific RL training environments to the labs so they can close that gap in long, multi-document professional workflows.

**Q2**: Why are finance RL environments harder to build than coding environments?
**A**: Coding rewards are binary and programmable (run the tests), while judging a correct contract redline depends on current deal terms, provisions meant to survive, and senior-banker judgment. Only expert rubrics built from real anonymized deals can verify that.

**Q3**: What is the "Moore's law of environments," and what risk does it create for Halluminate?
**A**: Environment complexity must roughly double every six to eight months to keep giving improving models a useful training signal. The open question is whether nine people can keep up that pace against competitors like Scale AI's dedicated RL Environments product.
