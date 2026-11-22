---
type: literature-note
source_url: https://openai.com/index/research-acceleration-jagged-frontier
author: OpenAI
tags: [research-acceleration, coding-agents, recursive-self-improvement, openai]
date_consumed: 2026-11-23
---

## Summary

OpenAI's internal measurements show coding agents completing nearly half of two-to-four-hour research tasks unaided, with agent use surging, but uplift is jagged across task types and humans remain central to the research loop. Safety and Alignment saw the largest increase in researcher effort. OpenAI argues labs should track and publicly report [[Recursive Self-Improvement]] indicators, without intending to pursue full RSI.

## Core Concepts

- **[[Research Acceleration]]**: Measured across inputs (agent use), process (task delegation, workflows) and outputs (code, experiments, capability index).
- **[[Jagged Frontier]]**: Agent success varies sharply by task category and type.
- **[[Coding Agents]] and [[Agent Workdays]]**: Every eight hours of agent use counts as one agent workday.
- **[[Recursive Self-Improvement]] (RSI)**: AI accelerating development of future AI; OpenAI calls for public tracking indicators.
- **[[Research Taste]]**: Developing and vetting ideas; potential bottleneck for RSI.
- **[[Epoch Capabilities Index]] and OpenAI ECI**: Metric for capability progress, built with public and internal benchmarks.
- **[[Safety and Alignment Research]]**: Largest absolute growth in researcher time, tied to the July Hugging Face incident aftermath.

## Key Takeaways

- **Task Success**: Two-to-four-hour task success rose from 23% to 46% (March to October).
- **Longer Tasks**: Four-to-eight-hour task success rose from 13% to 35%.
- **Jagged Uplift**: Monitoring runs 79% success; inference and serving code only 25%.
- **Spend Surge**: Median researcher reached $2,400 daily agent usage; 90th percentile $23,000.
- **Agent Workdays**: Rose from 0.5 to 5.7 per researcher per day.
- **Concurrency**: Over two-thirds of researchers peaked at four or more concurrent agents.
- **Self-Reported Value**: Median researcher would trade 40% of headcount or 30% of compute.
- **Safety Effort**: Safety and Alignment documented workweeks up 77% from January to September.
- **Ideas**: Researchers credit people for most key ideas; Codex contributed to some GPT-6.2 Astra ones.
- **Outputs**: Experiments per experimenter 1.68 times baseline; OECI frontier up 16.4 points per year.

## 🧠 Core Principles

**T1. Overall uplift is capped by the weakest task categories** — When performance is uneven across tasks, the lowest-performing tasks become the bottleneck on total gains. · *model:* [[Theory of Constraints]]
→ explains: Jagged Uplift, Longer Tasks

**T2. Rising activity metrics do not prove faster progress** — Usage, code volume and experiment counts can grow without faster research, so outcome measures such as capability indices are needed. Success rates also blend capability gains with changes in what gets delegated.
→ explains: Spend Surge, Agent Workdays, Outputs

## 🃏 Review Questions

**Q1**: What is OpenAI's main conclusion about AI acceleration of its own research?
**A**: Agents now complete a large and growing share of research tasks unaided, but uplift is jagged and humans remain a core part of the loop. OpenAI also argues labs should publicly report RSI indicators.

**Q2**: What data shows the jagged nature of agent performance?
**A**: Autonomous success was 79% for monitoring training runs and 72% for answering technical questions, but only 25% for inference and serving code and 29% for building evaluation and RL environments.

**Q3**: Why does the report say lower-performing task categories matter?
**A**: While model performance is heterogeneous, weak categories could become bottlenecks to high overall uplift, so improving them or keeping humans on them determines total gains.
