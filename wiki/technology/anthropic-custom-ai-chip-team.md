---
type: literature-note
source_url: https://techcrunch.com/2026/08/05/anthropic-is-hiring-an-ai-chip-design-team
author: Rebecca Bellan
tags: [anthropic, ai-chips, custom-silicon, inference-costs]
date_consumed: 2026-08-06
---

## Summary

Anthropic is building a "custom silicon team" to co-design its own AI chips alongside its models, following OpenAI, Google, and Meta into in-house hardware as demand for [[Claude]] outpaces what third-party infrastructure deals can economically supply.

## Core Concepts

- **[[Custom AI Silicon]]**: Chips designed jointly with the models that will run on them, aimed at improving inference speed and efficiency beyond what general-purpose accelerators offer.
- **[[Anthropic]] Infrastructure Strategy**: Currently relies on deals with AWS, Google, Nvidia, and AMD for compute — custom chips are a hedge against the limits of buying capacity from others.
- **[[Samsung]]**: Reported (via The Information) as a potential fabrication partner Anthropic was scouting the prior month.
- **Industry pattern**: OpenAI's Broadcom-built Jalapeño inference chip, Google's long-standing TPU program, and Meta's MTIA accelerators are cited as the precedent Anthropic is now following.

## Key Takeaways

- Anthropic is hiring engineers specifically for a "custom silicon team," per a job listing.
- The move mirrors OpenAI (Jalapeño, unveiled June 2026), Google (TPUs), and Meta (MTIA) — custom chips are becoming standard for frontier AI labs facing hardware supply constraints.
- Anthropic has not confirmed a fabrication partner; Samsung was reported as a candidate the prior month.
- The company declined immediate comment on the hiring push.

## 🃏 Review Questions

**Q1**: What is the core claim of this article?
**A**: Anthropic is assembling a team to design its own AI chips, joining OpenAI, Google, and Meta in building custom silicon rather than relying solely on third-party hardware vendors.

**Q2**: What evidence supports the idea that this is an industry-wide pattern rather than an Anthropic-specific move?
**A**: OpenAI shipped its own Broadcom-built inference chip in June 2026, Google has used custom TPUs for years, and Meta has its own MTIA accelerators — Anthropic's move is the fourth major lab to pursue the same strategy.

**Q3**: What's the practical implication of this move for Anthropic's business?
**A**: Custom co-designed hardware could reduce Anthropic's dependence on purchased compute from AWS, Google, Nvidia, and AMD, and lower the cost of serving rising Claude demand at scale — though it will take years before any custom chip ships.

## Update (Tom's Hardware follow-up, 2026-08-08)

Additional detail from a follow-up report (source: https://www.tomshardware.com/tech-industry/anthropic-to-build-its-own-co-designed-custom-ai-accelerator-for-inferencing-workloads-samsung-reported-to-be-partnering-with-the-claude-ai-maker-for-manufacturing):

- Custom inference silicon can offer up to **65% lower total cost of ownership** than Nvidia GPUs, and is less power-hungry — the core economic case driving the industry-wide shift.
- **Broadcom and Marvell** represent roughly 95% of the ASIC co-design market; Broadcom has a $73B order backlog and expects over $100B in annual AI chip revenue by the end of 2027, while Marvell is expected to earn upwards of $11B from co-design work in 2026 (it already holds Amazon's [[Trainium]] and Microsoft's [[Maia]] contracts).
- **[[Samsung]]** was reported by The Information as a manufacturing partner Anthropic was in talks with — a relatively small player in ASIC co-design, but one that brings scarce advanced memory access.
- **[[TSMC]]** is framed as the biggest overall beneficiary regardless of which lab or partner wins: it produces the majority of the world's cutting-edge silicon and handles CoWoS advanced packaging for HBM integration across nearly all competing chip programs (Google TPU, Amazon Trainium/Inferentia, Meta MTIA, Microsoft Maia, Tesla AI5/AI6).
- No major AI lab is expected to become fully self-reliant on custom silicon — training still requires Nvidia GPUs — but each inference chip installed reduces reliance on Nvidia for that specific workload.
