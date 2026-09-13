---
source_url: https://withspecific.com/benchmarks/real-swe
author: Specific Labs
date: 2026-09-13
---

# Real-SWE Benchmark

Specific Labs introduced Real-SWE, a benchmark evaluating frontier AI models on private, real-world enterprise codebases licensed from actual companies — not synthetic or public tasks.

## Key Design Principles

- Tasks come from production codebases with genuine business consequences (billing, taxes, customer migration)
- Uses "native harnesses" to reflect how enterprise engineers actually work
- Tasks are "natively out of distribution" — unavailable anywhere on the public internet

## Leaderboard Results (pass@1, averaged over 8 runs/task)

| Rank | Model | Harness | Resolution Rate |
|------|-------|---------|----------------|
| 1 | Fable 5.1 (Anthropic) | Claude Code | 38.8% |
| 2 | GPT-6 Astra (OpenAI) | Codex CLI | 33.8% |
| 3 | Gemini 3.8 Flash (Google) | Gemini CLI | 31.2% |
| 4 | GLM 5.3 (ZAI) | Claude Code | 28.8% |
| =5 | Grok 4.6 (xAI) | Grok Build | 23.8% |
| =5 | Muse Spark 1.3 (Meta) | Muse Code | 23.8% |
| 7 | Kimi K3 | Kimi Code | 18.8% |
| 8 | GPT-5.6 Sol (OpenAI) | Codex CLI | 16.2% |

## Notable Findings

- 6 of 10 tasks have resolution rates below 15%
- "Analytics stream reducer" had a 0% resolution rate across all models
- Median reference solution touches 11 files vs. 6 in FrontierCode/DeepSWE
- "Missed requirements" is the most common failure mode
- Higher cost doesn't guarantee better results — Gemini 3.8 Flash achieved 31.2% at ~$2.50/rollout vs. Fable 5.1's 38.8% at ~$6.96/rollout
- Short rollouts (under 10 min) failed at 71.4%, similar to longer ones (73.4%) — suggesting time isn't the primary bottleneck

## Failure Taxonomy (% of failed runs)

- **Unverified assumption** — guesses about system behavior without checking
- **Missed requirement** — omits required behaviors (Grok 4.6: 67.2% of failures)
- **Integration error** — correct idea, wrong wiring (Gemini 3.8 Flash: 49.1%)
- **Regression** — breaks existing behavior
- **Wrong file** — changes land somewhere the app never calls
