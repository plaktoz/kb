---
type: literature-note
source_url: https://jp.ibtimes.com/itoki-builds-ai-productivity-model-854-workers-matsuo-institute-104625
author: IBT Staff Reporter
tags: [workplace-analytics, meetings, causal-discovery, deep-work]
date_consumed: 2026-10-03
---

## Summary

Japanese office furniture and workplace services firm [[Itoki]] and the [[Matsuo Institute]] built a data-driven productivity estimation model from 70 types of AI-processed behavioral data covering 854 headquarters employees in December 2025. The key findings are that the number of meetings, more than their total length, worsens next-day mental condition across all job types, and that uninterrupted work blocks of 60+ minutes are linked to improved next-day condition for 88% of workers. The research relies on objective behavioral data and time-series causal discovery rather than subjective surveys, as Japanese firms face pressure to show returns on human capital investment.

## Core Concepts

- **[[VAR-LiNGAM]]**: The time-series [[Causal Discovery]] method at the core of the model. It aims to find causal drivers of productivity rather than just correlations.
- **Behavioral data scope**: 70 indicators made up of 21 location-related, 4 schedule-related, and 45 online communication measures. Message contents were excluded and all data was anonymized.
- **Productivity definition**: Output is defined as the degree to which each employee demonstrates individual capability. It is modeled alongside mental and physical condition and internal workplace relationships.
- **[[Meeting Frequency vs. Duration]]**: Meeting count, not total time, had the stronger effect on next-day mental condition in design/development/planning, sales/service, and administrative roles.
- **[[Uninterrupted Work Blocks]]**: Days with more than 60 minutes free of meetings or other interruptions were followed by improved mental condition for 88% of workers. This empirically supports [[Deep Work]] and [[Time Blocking]].
- **[[Inbound vs. Outbound Communication]]**: Incoming email and chat affected workplace relationships more than outgoing messages. Heavy inflows hurt sales/service workers, while self-initiated communication improved relationship conditions.
- **[[Human Capital Disclosure]]**: Japanese corporate reporting on employee development, engagement, and workplace conditions, which drives demand for evidence of returns on people investments.
- **[[Matsuo-Iwasawa Lab]]**: The University of Tokyo engineering lab that the Matsuo Institute works alongside to put research into wider use.

## Key Takeaways

- **Sample**: 854 Itoki HQ workers, Dec. 1–31, 2025, 70 behavior data types.
- **Meeting count beats meeting length** as a predictor of next-day mental decline.
- **60+ minute uninterrupted blocks**: 88% of workers showed better next-day mental condition.
- **Inbound messages matter more** than outbound for workplace relationships.
- **Sales/service hit hardest** by heavy email and chat inflows.
- **Self-initiated communication** improved internal relationship conditions.
- **No uniform causal link** for office time, break visits, response speed, or connected hours.
- **Method**: objective behavioral data plus VAR-LiNGAM, not employee surveys.
- **Caveat**: the model is transferable, but findings reflect only Itoki's workplace.

## 🧠 First Principles & Mental Models

- **[[Maker's Schedule vs. Manager's Schedule]]**: Makers need long unbroken stretches, and each meeting fragments the day regardless of its length. This matches the finding that meeting count, not duration, drives next-day decline, while 60+ minute uninterrupted blocks improve condition.
- **[[Attention Residue]]**: Every switch into a meeting or incoming message leaves cognitive residue. That explains why the number of interruptions (meetings, inbound messages) matters more than total time spent, and why self-initiated communication doesn't carry the same cost.

## 🃏 Review Questions

**Q1**: What was the central finding of the Itoki and Matsuo Institute productivity research?
**A**: The number of meetings, rather than their total duration, had the stronger negative effect on workers' next-day mental condition across all three job categories. Days with 60+ minutes of uninterrupted work were followed by improved condition for 88% of workers.

**Q2**: How did the study try to identify causes rather than correlations, and what data did it use?
**A**: It applied VAR-LiNGAM, a time-series causal discovery method, to 70 anonymized objective behavior indicators: 21 location, 4 schedule, and 45 online communication measures. It did not use subjective surveys or message contents.

**Q3**: How could a manager apply these findings to team scheduling?
**A**: Reduce the number of meetings, for example by consolidating them, rather than only shortening them, and protect blocks of 60+ minutes free of interruptions. Also limit heavy inbound message loads, especially for sales and service staff, while encouraging self-initiated communication.
