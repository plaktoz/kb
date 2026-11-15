---
type: literature-note
source_url: https://www.deel.com/deel-works/measure-ai-productivity-adoption-metrics
author: Kaila Caldwell
tags: [ai-productivity, measurement, verification-cost, rework]
date_consumed: 2026-11-16
---

## Summary

[[Kaila Caldwell]] argues that companies measure [[AI Adoption Metrics]] (tool subscriptions, usage, training completion, self-reported skill) but not whether work gets done faster, with less rework. Case studies show apparent time savings of 90% or more shrinking to 12-15% once [[Verification Cost]] and rework are counted, and AI can save one worker time while adding review work for another. Experts recommend baselines, comparable-task before/after comparisons, and pairing volume metrics with failure metrics.

## Core Concepts

- **Adoption vs. impact gap**: A National Bureau of Economic Research study found 69% of firms use AI while 89% of executives reported no labor-productivity impact over three years.
- **[[Verification Cost]]**: Reviewing AI output can consume most of the time apparently saved.
- **Self-report bias**: Surveys measure [[Self-Efficacy]], not productivity; employees overestimate savings (METR study, HostZealot).
- **Downstream work transfer**: Low-quality AI output ("workslop") shifts time to reviewers.
- **[[Failure Twin Metrics]]**: [[Evgenii Arsentev]]'s idea of pairing volume metrics (tickets closed, commits, documents) with rework and defect metrics.
- **Baseline-then-compare method**: [[Joy Papini]] and [[Daniel W. Rasmus]] advise measuring an observable workflow point before and after AI adoption, including new work created.
- **Training gap**: 37.8% of US knowledge workers have had no AI training; mandated use at Meta arrived without formal training.

## Key Takeaways

- **Adoption Surge**: Employer-sponsored AI subscriptions rose from 16% to 33%; training fell seven points.
- **METR Result**: Experienced developers were 19% slower with AI yet believed 20% faster.
- **Skill Self-Assessment**: Only 11% accurately judged their own AI proficiency across 88,753 assessments.
- **Network Data Case**: A 90% apparent saving became about 15% after 15 hours of review.
- **HostZealot Tickets**: Median resolution fell 15.6% (45 to 38 minutes) versus employees' estimated 30%.
- **HasData Result**: Active coding time fell 8 to 5.5 hours; net gain after review only 12.5%.
- **Reviewer Burden**: About 40% received low-quality AI work; each incident cost nearly two hours.
- **Measurement Standard**: "The real unit of measurement should be completed work that survives review."

## 🧠 Core Principles

**T1. Usage and self-reports are proxies, not outcomes** — Adoption, training completion, and self-rated savings measure activity or belief, not whether work improved. Measuring an outcome requires comparing the actual work against a baseline. · *model:* [[Goodhart's Law]]
→ explains: Adoption Surge, METR Result, Skill Self-Assessment, HostZealot Tickets, Measurement Standard

**T2. Cheaper production moves the cost to verification** — When generating output becomes nearly free, the scarce work shifts to checking it, and the net saving is judged over the whole workflow including review and rework.
→ explains: Network Data Case, HasData Result, Reviewer Burden

## 🃏 Review Questions

**Q1**: What is the article's central claim about measuring AI productivity?
**A**: Companies track AI adoption, usage, and training, but these do not establish that work is done faster or with less rework. Productivity must be measured on the work itself.

**Q2**: How did the network-data example show the gap between apparent and real savings?
**A**: An AI agent cut data extraction from about 20 hours to 2, suggesting 90% savings. But 15 hours of review to catch a merged-switch error meant the workflow took about 17 hours, roughly a 15% saving.

**Q3**: How should a company measure whether AI is helping?
**A**: Pick an observable, quantifiable workflow point, set a baseline before AI, and re-measure after adaptation. Pair volume metrics with rework and defect metrics, and track the time spent verifying output.
