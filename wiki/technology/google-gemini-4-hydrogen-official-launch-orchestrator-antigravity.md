---
type: literature-note
source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen
author: Koray Kavukcuoglu
tags: [google, gemini, agentic-workflows, model-release]
date_consumed: 2026-11-14
---

## Summary

Google's official launch post introduces [[Gemini 4 Hydrogen]], a fast execution model priced flat at $1.50 per million input and $7.50 per million output tokens across a 1 million-token context window. It surpasses [[Gemini 4 Argon]] on the [[Artificial Analysis Intelligence Index]] (51 vs. 50 at default, 54 at xhigh) and is paired with a new [[Orchestrator]] in [[Google Antigravity]] that switches between models within one session. Hydrogen rolls out to developers, enterprises, the Gemini app and Google Search.

## Core Concepts

- **[[Gemini 4 Hydrogen]]**: Speed-and-efficiency tier for everyday coding and agentic workflows, replacing [[Gemini 3.8 Flash]].
- **[[Gemini 4 Carbon]] and [[Gemini 4 Argon]]**: Frontier models for deep, long-horizon reasoning and architectural judgment.
- **[[Orchestrator]]**: A [[Google Antigravity]] feature that dynamically switches between Carbon and Hydrogen mid-session.
- **[[Multi-Model Workflows]]**: Carbon coordinates while Hydrogen powers worker and verifier agents in isolated workspaces.
- **Thinking levels**: Low, medium, high (default) and a new xhigh tier trading quality against latency and cost.
- **[[Terminal-Bench]]**: Coding benchmark used for both Orchestrator and Flash comparisons.
- **[[Agentic Safety]]**: Reduced overreach, misaligned actions and prompt-injection vulnerability.
- **[[Google Search]] and [[Gemini App]]**: Consumer surfaces upgraded with better intent understanding and wider query fan-out.

## Key Takeaways

- **Pricing**: Flat $1.50 input and $7.50 output per million tokens, whole 1M context.
- **Intelligence**: Scores 51 on Artificial Analysis Index versus Argon's 50; 54 at xhigh.
- **Orchestrator**: Near-Carbon task success with 24% less quota and 19% faster completion.
- **Versus 3.8 Flash**: 2.5x faster, Terminal-Bench 57% vs. 18.2%, 5x fewer fabricated claims.
- **Partner Results**: 2x to 2.8x faster with 12% to 23% fewer tokens.
- **Benchmarks**: Ranks #5 on Agent Arena; 58.8% HLE-Diamond; 52.3% Vals Tax Agent Bench.
- **Safety**: Overreach reduced up to 81%; 94% agent honesty rate; 2.3x more injection-resilient.
- **Availability**: Free Gemini app users get it via auto model selection when appropriate.

## 🧠 Core Principles

**T1. Match model capability to task demands** — Routing deep-judgment work to a frontier model and execution work to a cheaper, faster one achieves near-frontier results at lower cost and latency. · *model:* [[Division of Labor]]
→ explains: Orchestrator, Partner Results

## 🃏 Review Questions

**Q1**: What is Gemini 4 Hydrogen designed for, and how does it relate to Carbon and Argon?
**A**: Hydrogen is built for rapid execution in everyday coding and agentic workflows, while Carbon and Argon handle deep, long-horizon reasoning. It can stand alone or serve as the execution engine alongside them.

**Q2**: What evidence supports Orchestrator's multi-model approach?
**A**: On Terminal-Bench 4.0, Orchestrator reached near-Carbon task success rates while consuming 24% less quota and finishing 19% faster on average.

**Q3**: How would a team use Hydrogen in parallel-agent workflows?
**A**: Carbon acts as the coordinator while Hydrogen powers worker and verifier agents that build and test changes simultaneously across isolated workspaces, shipping faster without raising token costs.
