---
type: literature-note
source_url: https://shattered.io/decart-amazon-three-founders-chip-portability-7-5-billion-unconfirmed-nov-25/
author: Marcus Bell
tags: [amazon, decart, ai-chips, ai-acquisitions]
date_consumed: 2026-11-26
---

## Summary

[[Amazon]] announced on November 23, 2026 that it will buy the proprietary technology behind the [[Decart Optimization Stack]] (DOS) and bring Decart's three named co-founders, researchers and engineers on board. The article argues the deal is less a software purchase than a bet on people who can extract more work from silicon, and that the reported $7.5 billion price, the deal's scope and DOS's future support for rival chips all remain unconfirmed.

## Core Concepts

- **[[Decart]] and DOS**: Software that sits between an AI model and the hardware, tuning models for a given accelerator and helping them switch among [[Nvidia]], Amazon and Google chips.
- **Confirmed vs reported**: Amazon confirmed the technology and people; the ~$7.5B figure is attributed to [[Bloomberg]] via a person familiar, and Reuters cites [[PitchBook]] for a prior valuation near $4B.
- **[[Hardware Portability]]**: Moving a workload between chip families gives its owner leverage in contract negotiations, and gives the provider owning the portability layer a way to steer workloads to its own silicon.
- **[[Trainium]], Inferentia and [[Annapurna Labs]]**: Amazon's training and inference chips; the transaction runs through Annapurna, and Decart has worked with Amazon on Trainium performance since 2025.
- **AI talent grab**: Reuters' framing; Amazon hires [[Dean Leitersdorf]], [[Moshe Shalev]] and Orian Leitersdorf along with the team rather than licensing code.
- **Inference economics**: Serving a model happens on every prompt, so efficiency across a large chip fleet becomes a core cost line.
- **Software layer contest**: Chip makers, cloud providers and neutral tooling firms compete to own the layer between models and chips.

## Key Takeaways

- **Confirmed Scope**: Amazon bought technology and people, not clearly all of Decart or its models.
- **Price Unconfirmed**: ~$7.5B comes from Bloomberg via a source; Amazon disclosed no price.
- **Premium Over Last Mark**: Reported price sits well above Decart's valuation of nearly $4B.
- **Efficiency Is the Pitch**: Amazon says it will lower cost of training and running AI models.
- **Portability Is Leverage**: Switching among chips strengthens buyers' bargaining power with vendors.
- **Neutrality Tension**: Amazon made no commitment to keep supporting rival chips at full strength.
- **Talent Over Code**: Code ages quickly; the engineers' knowledge ages slowly, so Amazon hired the maintainers.
- **Nvidia Stickiness Weakens**: Easier chip switching reduces software familiarity as a vendor advantage.
- **Open Questions**: No delivery date, pricing model, or support plan for Decart's existing customers.

## 🧠 Core Principles

**T1. Portability across suppliers shifts bargaining power** — A workload that can move between vendors' hardware lowers the cost of switching, which gives its owner leverage in every contract and weakens any one vendor's stickiness. · *model:* [[Switching Costs]]
→ explains: Portability Is Leverage, Nvidia Stickiness Weakens, Neutrality Tension

**T2. When one narrow skill gates a large market, the largest participant eventually owns it rather than rents it** — The article argues the pattern repeats because the logic is stable, and Amazon chose to own the capability instead of renting it. · *model:* [[Build vs. Buy]]
→ explains: Efficiency Is the Pitch, Premium Over Last Mark

**T3. Know-how in people outlasts code** — In fast-moving infrastructure, software snapshots age quickly while the understanding of why something works ages slowly, so buyers acquire the people who maintain it. · *model:* [[Tacit Knowledge]]
→ explains: Talent Over Code, Confirmed Scope

## 🃏 Review Questions

**Q1**: What did Amazon confirm about the Decart deal, and what remains unconfirmed?
**A**: Amazon confirmed it will buy the proprietary technology behind DOS and bring in the three co-founders plus researchers and engineers. The ~$7.5B price, the scope of the purchase and the fate of Decart's models are not confirmed.

**Q2**: How does the article attribute the $7.5 billion figure and put it in context?
**A**: Secondary reports attribute it to Bloomberg, citing a person familiar with the matter; Amazon names no price. Reuters, citing PitchBook, says it is well above Decart's last valuation of nearly $4 billion.

**Q3**: What should customers and developers do given the open questions?
**A**: Wait for documentation before changing procurement, ask Amazon for written answers on continued support for non-Amazon chips, and pilot workloads to measure cost per request before committing.
