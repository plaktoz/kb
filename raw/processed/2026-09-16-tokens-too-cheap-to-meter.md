---
source_url: https://jyn.dev/tokens-too-cheap-to-meter/
author: jyn
date: 2026-09-16
---

# Tokens Too Cheap to Meter

The article argues that AI inference costs are collapsing across multiple dimensions simultaneously.

## Hardware & Software Efficiency

- GPU energy efficiency doubles roughly every two years (logarithmic growth since the 1960s Moore's Law era)
- Inference engines like vLLM improved ~40% in energy efficiency over 15 months
- Intel demonstrated a 2.4x throughput gain purely through software optimization

## Model Architecture Improvements

- Mixture-of-Experts allows models to be "7x smaller while achieving the same benchmark performance"
- Mamba-Transformer hybrids reduce RAM requirements by ~5x, enabling more capable local inference

## Cost Trajectory

The author calculates roughly 2.5 orders of magnitude cost reduction per task over the past year, combining hardware, software, and model efficiency gains.

## Specialized Models

A classifier called Jev prices input at "$42 per billion tokens" with free output — cheap enough that developers are embedding AI directly into Unix-pipe-style CLI tools.

## Key Implications

- Token costs may soon fall below the cost of conventional tool calls (grep, HTML parsing, builds)
- Software moats erode; operational excellence and security become primary value drivers
- Users gain a fourth option beyond use/don't use/switch: *have an LLM build it*
- Quality and access, not raw token volume, become the binding constraints

The author concludes that cheap *intelligence*, not just cheap *compute*, is the coming transition.
