---
type: literature-note
source_url: https://fortune.com/2026/10/14/taser-maker-axon-is-mandating-ai-use-to-speed-up-work-as-its-surveillance-tools-face-scrutiny/
author: John Kell
tags: [axon, ai-mandate, police-surveillance, ai-token-costs]
date_consumed: 2026-10-16
---

## Summary
Axon Enterprise, the Taser maker turned public-safety tech company, is pushing AI tools to law enforcement while facing growing criticism over police surveillance and AI errors. Internally, CTO/CPO Jeff Kunins has mandated a 10% productivity gain for every R&D team, with stock grants for teams exceeding 15%, targeting 25–30% compression of product, design, and engineering work by end of 2026. The newsletter also covers Accenture research showing enterprise AI token bills rising sharply while only 35% of companies can track costs for their largest AI use cases.

## Core Concepts
- **[[Axon Enterprise]]**: Founded as Taser International by [[Rick Smith]] in 1993; now sells body cameras, drones, license plate readers, and AI software, with ten straight quarters of 30%+ revenue growth.
- **[[Jeff Kunins]]**: Axon's chief product and technology officer; frames Axon's role as tech for transparency and accountability.
- **[[Police Surveillance]] backlash**: Misuse of [[Flock Safety]] AI cameras for stalking, wrongful AI-driven arrests, and the Los Angeles City Council delaying an Axon AI license-plate-reader pilot.
- **[[Draft One]]**: Generative AI that turns body-camera audio into police-report drafts; early outputs showed [[Algorithmic Bias]] ("fled" vs. "left the scene" by race), fixed via [[Fine-Tuning]].
- **[[Ethics and Equity Advisory Council]]**: Third-party group advising Axon during product design.
- **[[Axon Assistant]]**: Real-time translation across 50+ languages via body camera.
- **AI redaction**: Nearly a decade of AI blurring bystander faces and plates in footage, replacing frame-by-frame manual work.
- **[[AI Mandate]] with carrot and stick**: Mandatory 10% productivity target per team; stock grants above 15% if the broader team hits the minimum.
- **[[AI Token Costs]]**: [[Accenture]] survey of 750 executives finds ~$2.5B annual token spend, heading toward ~$3.6B in 24 months.
- **[[Model Routing]]**: Accenture's [[Lan Guan]] says only 20% of enterprise workflows suit [[Frontier Models]]; route tasks to the cheapest capable model.
- **News packets**: [[Meta Muse]] models launch; [[Claude]] Haiku 4.5 submitted a false homicide tip; [[Microsoft]] Maia 3000 chip; [[IMF]] warns of AI disruption to jobs and taxation.

## Key Takeaways
- **Revenue Momentum**: Ten consecutive quarters of revenue growth above 30%.
- **Surveillance Scrutiny**: Flock misuse and wrongful arrests fuel an anti-surveillance movement.
- **CEO Concession**: Rick Smith: "the critics aren't all wrong."
- **Bias in Draft One**: LLMs wrote "fled" for Black subjects, "left" for white subjects.
- **Bias Remediation**: Axon fine-tuned models to produce consistent, less biased outputs.
- **Work Compression Target**: 25–30% compression of PM, design, and engineering work by end-2026.
- **Mandatory Floor**: Every team must deliver 10% productivity gains with fewer resources.
- **Stock-Grant Carrot**: Teams exceeding 15% earn stock grants if the team meets 10%.
- **Whole-Effort Scope**: Target covers entire person effort, not just coding.
- **Token Bill Growth**: $1B+ firms spend ~$2.5B on tokens, rising toward $3.6B.
- **Cost Visibility Gap**: Only 35% of companies track costs for their largest AI use cases.
- **Frontier Fit**: Only 20% of enterprise workflows warrant frontier models.
- **Cost Levers**: Open-weight models, observability, chargeback, routing, and cost-aware training.

## 🃏 Review Questions

**Q1**: How is Axon driving internal AI adoption, and what is its target?
**A**: Axon mandates a 10% productivity gain for every R&D team and awards stock grants to teams exceeding 15%, aiming for 25–30% compression of product, design, and engineering work by end of 2026.

**Q2**: What bias problem surfaced in Axon's Draft One, and how was it addressed?
**A**: The LLMs described a white subject as having "left the scene" but a Black subject as having "fled the scene" with otherwise identical facts; Axon fine-tuned the models to make outputs consistent and remove the harmful bias.

**Q3**: What should a CIO do in response to Accenture's token-cost findings?
**A**: Route tasks to the lowest-cost model that achieves the outcome (only ~20% of workflows need frontier models), make AI workflows observable before launch, charge departments for their usage, and train staff in cost-effective AI use.
