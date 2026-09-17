---
source_url: https://rohanbansal.com/qorl
author: Rohan Bansal
date: 2026-09-16
---

# Training a 4B model to produce 81% faster query plans than Postgres

Bansal documents an experiment post-training a 4-billion-parameter language model (based on a distilled Qwen variant) to generate PostgreSQL query hints that beat Postgres's default query planner.

## The Core Problem

Query optimization is genuinely hard — join ordering alone is NP-hard. Postgres estimates cardinalities using statistics rather than counting rows directly, relying on uniform distribution assumptions that can fail badly. With selective predicates, a poor join ordering can cause **4x more work** than the optimal ordering.

Postgres can be steered via `pg_hint_plan`, which accepts structured SQL comments directing join algorithms, join order, and scan types. The key insight: rather than beating Postgres on one-off queries, the target is **repeated analytic workloads** where upfront optimization cost amortizes across thousands of runs.

## Methodology

1. **Harness:** An agentic tool-calling framework (`qo-agent`) wrapping Postgres measurement
2. **SFT Phase:** ~500 GPT-6 Astra trajectories used for off-policy distillation into the 4B model via LoRA (~21M trainable parameters)
3. **RL Phase:** Custom GRPO variant with "anchored advantages" — rollout quality measured relative to Postgres default, not just against sibling rollouts

A key reward design fix: plain GRPO was reinforcing plans equivalent to Postgres's default because they beat the group mean. The anchored variant uses `max(0, mean of sibling qualities)` as the baseline, so nothing gets credit unless it genuinely beats Postgres.

## Noise Reduction

Measurement reliability was critical. At 128MB `shared_buffers`, one noisy query showed ~20% phantom speedup/slowdown readings. Raising `shared_buffers` to 2GB dropped the mean no-op error rate from ~5% to ~1.5% and eliminated the bimodal timing distribution, while also making queries ~37% faster overall.

## Results

| Checkpoint | Geo Mean Speedup | Workload Speedup | Regressions |
|---|---|---|---|
| Vanilla 4B | ~0.85x | ~0.85x | 1 |
| After SFT | 1.16x | 1.06x | 5 |
| RL 600 updates | 1.35x | 1.16x | 0 |
| RL 1,200 updates | 1.41x | 1.29x | 2 |
| Best-of-15 (3 rollouts) | **1.81x** | **1.81x** | 0 |

The best-of-15 configuration corresponds to a **44.7% total latency reduction** across 113 JOB queries.

## What the Model Learned

- Preferred nested loops over hash joins
- Favored index scans over sequential/bitmap scans
- Regularly applied `enable_sort=off` and `random_page_cost=1.1`
- Used `Leading` hints (join reordering) and parallelism hints heavily
- Inspected table statistics before proposing candidates in ~87% of searches

## Cost

~$800 for ~95 hours on a 2×H100 Lambda node, plus ~$400 in OpenAI API fees for teacher trajectories. **Total: ~$1,200.**
