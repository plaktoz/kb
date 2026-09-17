---
type: literature-note
source_url: https://rohanbansal.com/qorl
author: Rohan Bansal
tags: [query-optimization, llm-training, postgresql, reinforcement-learning]
date_consumed: 2026-09-17
---

## Summary

Rohan Bansal post-trained a 4-billion-parameter language model (a distilled Qwen variant) to generate `pg_hint_plan` hints that steer PostgreSQL's query planner, beating the default planner by up to 81% (1.81x speedup) on the Join Order Benchmark. The training pipeline combines supervised fine-tuning from GPT-6 Astra teacher trajectories with a custom GRPO variant using "anchored advantages" so the model only receives reward for genuinely outperforming Postgres. Total cost was approximately $1,200 on two H100s over 95 hours.

## Core Concepts

- **[[PostgreSQL]] Query Planning** — join ordering is NP-hard; Postgres uses statistics-based cardinality estimates that break under selective predicates, causing up to 4x more work than optimal.
- **[[pg_hint_plan]]** — a Postgres extension that accepts structured SQL comments to override join algorithms, join order, and scan types.
- **[[Supervised Fine-Tuning]] (SFT)** — ~500 teacher trajectories from GPT-6 Astra distilled into the 4B model via [[LoRA]] (~21M trainable parameters).
- **[[Reinforcement Learning from Human Feedback|RL with Anchored Advantages]]** — a custom [[GRPO]] variant where the baseline is `max(0, mean of sibling qualities)`, ensuring reward only for plans that beat Postgres's default, not just the rollout group mean.
- **[[Agentic Tool-Calling]]** — the `qo-agent` framework wraps Postgres measurement, enabling the model to inspect table statistics before proposing query hints.
- **Noise Reduction** — raising `shared_buffers` from 128MB to 2GB reduced phantom speedup error rates from ~5% to ~1.5% and eliminated bimodal timing distributions.

## Key Takeaways

- **Target workload**: Repeated analytic queries where upfront optimization cost amortizes over thousands of runs.
- **SFT baseline**: After fine-tuning, geo mean speedup reached 1.16x over vanilla Postgres default.
- **RL improvement**: 1,200 RL updates pushed geo mean speedup to 1.41x.
- **Best-of-15**: Sampling 3 rollouts and picking best achieved **1.81x speedup** (44.7% latency reduction) with 0 regressions.
- **Reward fix**: Plain GRPO inadvertently reinforced Postgres-equivalent plans; anchored baseline fixed this.
- **Learned behaviors**: Preferred nested loops, index scans, `enable_sort=off`, `random_page_cost=1.1`, and `Leading` hints.
- **Statistics inspection**: Model checked table statistics before proposing hints in ~87% of searches.
- **Total cost**: ~$1,200 ($800 compute + $400 API for teacher trajectories).

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Plain GRPO rewarded plans that beat the group mean — a proxy for "beating Postgres" — causing the model to reinforce Postgres-equivalent plans; switching to an absolute baseline (anchored advantages) fixed the metric to match the actual goal.
- **[[Amortization]]**: Upfront LLM inference cost is economically justified only for repeated analytic workloads where the query plan is reused thousands of times, not for one-off OLTP queries.

## 🃏 Review Questions

**Q1**: What is the core claim of this experiment?
**A**: A 4B-parameter language model, post-trained with SFT and a custom RL algorithm, can generate `pg_hint_plan` hints that produce query plans up to 81% faster than PostgreSQL's default planner on the Join Order Benchmark.

**Q2**: Why did plain GRPO fail, and how was it fixed?
**A**: Plain GRPO rewarded plans that merely beat the sibling rollout mean, accidentally reinforcing plans equivalent to Postgres's default. The anchored variant uses `max(0, mean of sibling qualities)` as the baseline so only plans that genuinely outperform Postgres receive positive reward.

**Q3**: Under what conditions is this approach practical to deploy?
**A**: It is best suited to repeated analytic workloads where the same query runs thousands of times, so the one-time cost of LLM-generated hint optimization amortizes across many executions.
