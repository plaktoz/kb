---
type: literature-note
source_url: https://martinfowler.com/bliki/WaterfallProcess.html
author: Martin Fowler
tags: [waterfall, software-development, methodology, agile]
date_consumed: 2026-08-03
---

## Summary

[[Martin Fowler]] defines Waterfall as a software development style that decomposes effort into sequential phases by activity type (analysis → design → coding → testing), contrasting sharply with iterative and agile approaches. Despite widespread attribution to [[Winston Royce]]'s 1970 paper, the term "waterfall" never appears in that paper — only its cascade diagram became the concept's visual shorthand. The key failure of Waterfall is forcing predictive planning onto requirements that invariably change.

## Core Concepts

- **[[Waterfall Process]]**: Organizes work by activity phase across all features, rather than delivering all activities per feature.
- **[[Iterative Development]]**: The structural opposite of Waterfall — completes all activities (design, code, test) for one feature at a time, enabling early releases and fast feedback.
- **[[Agile Development]]**: Not simply synonymous with iterative; agile specifically requires [[Adaptive Planning]] — updating plans as learning occurs and measuring success by business value, not schedule adherence.
- **[[Predictive Planning]]**: The assumption that requirements can be fully specified and locked upfront — Waterfall's core dependency and its primary failure mode.
- **[[Winston Royce]]**: Author of the 1970 paper most commonly cited as the origin of Waterfall; the paper's cascade diagram was misread as an endorsement of sequential phases.
- **[[Late Integration Problem]]**: Testing and integration arriving at the end of a Waterfall project are the hardest phases to predict and the most expensive to fix.

## Key Takeaways

- **Phase-by-activity**: Waterfall does one activity (e.g., design) for all features before moving on.
- **Iterative alternative**: Iterative does all activities for one feature at a time — early releases possible.
- **False "done" problem**: Early phases appear complete while hidden work remains.
- **Predictive planning fails**: Requirements rarely stay stable; Waterfall assumes they do.
- **Agile ≠ iterative**: Agile requires adaptive planning and business-value measurement, not just iterations.
- **Royce origin myth**: "Waterfall" never appears in Royce's paper — the term was inferred from its diagram.
- **Success metric tell**: Celebrating on-time/on-budget reveals predictive (not adaptive) thinking.

## 🧠 First Principles & Mental Models

- **[[Feedback Loops]]**: Waterfall's fundamental flaw is delaying feedback to the end — testing and integration land last, making the cost of discovering errors catastrophically high. Iterative development is the systems-thinking fix: shorten feedback loops so errors surface while they are still cheap to correct.
- **[[Goodhart's Law]]**: Declaring early phases "done" while work remains hidden is the natural result of tracking phase completion as the target metric — teams optimize for the declared milestone rather than actual progress.

## 🃏 Review Questions

**Q1**: What is the defining structural characteristic of the Waterfall process?
**A**: Waterfall decomposes effort into sequential activity-based phases (analysis, design, coding, testing) applied across all features, rather than delivering all activities for one feature at a time.

**Q2**: Why is the attribution of Waterfall to Winston Royce's 1970 paper considered ironic?
**A**: The word "waterfall" never appears in Royce's paper; the cascade-shaped diagram was misinterpreted as an endorsement of sequential phases, when the paper actually warned against this approach.

**Q3**: How does Fowler distinguish agile from simply iterative development?
**A**: Agile requires adaptive planning — continuously updating plans as learning occurs and measuring success by business value delivered — whereas iterative only means doing all activities per feature in short cycles, without necessarily committing to adaptive planning principles.
