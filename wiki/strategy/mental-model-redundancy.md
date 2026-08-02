---
type: literature-note
source_url: https://fs.blog/mental-model-redundancy/
author: Farnam Street
tags: [redundancy, mental-models, systems-thinking, risk-management]
date_consumed: 2026-08-02
---

## Summary

Redundancy — having more than one means to accomplish a task — is a core reliability engineering principle that extends into business, investing, and organizational design. While redundant systems reduce failure probability multiplicatively, they can backfire through added complexity, diffusion of responsibility, or by encouraging riskier behavior. The [[Challenger Disaster]] illustrates how overconfidence in redundant safety components can paradoxically increase catastrophic risk.

## Core Concepts

- **[[Redundancy]]**: In reliability engineering, redundancy means multiple independent paths to success; all must fail before the system fails.
- **[[Margin of Safety]]**: The practice of building well beyond the minimum required threshold — applied by [[Benjamin Graham]], [[David Dodd]], and [[Warren Buffett]] in investing and bridge engineering alike.
- **[[Common-Mode Failure]]**: A flaw in redundant design where a shared vulnerability causes all redundant components to fail simultaneously.
- **[[Diffusion of Responsibility]]**: In organizations (unlike mechanical systems), redundant actors are aware of each other and may reduce individual effort assuming others will compensate — "social shirking."
- **[[Risk Compensation]]**: Adding safety systems can lead individuals to take greater risks, potentially negating the safety gains (e.g., baby-proof caps leading to more poisonings).
- **[[Normalization of Deviance]]**: The gradual acceptance of risky operations as normal when nothing bad has happened yet — a key factor in the Challenger decision-making culture.
- **[[Charlie Munger]]** and **[[Warren Buffett]]** frame redundancy in business as maintaining excess capacity and liquidity buffers so no single adverse event forces a catastrophic decision.

## Key Takeaways

- **Core definition**: Redundancy = more than one functional path; system fails only when all paths fail.
- **Multiplicative safety**: Two independent braking circuits each with 1/10 failure probability yields 1/100 combined failure probability.
- **Complexity cost**: Redundancy adds weight, complexity, and power consumption — it is not a substitute for good initial design.
- **Common-mode error risk**: Redundant components sharing a vulnerability can fail together, negating independence.
- **Social diffusion**: Human redundancy breeds shirking; mechanical redundancy does not.
- **Risk compensation**: People drive faster with seatbelts; NASA launched Challenger trusting the backup O-ring.
- **Buffett's rule**: Always maintain extra liquidity so you are never forced to act under pressure ("never go back to go").
- **Confucius on resilience**: A superior person anticipates danger, ruin, and disorder even in peaceful times.
- **Boeing 777 case**: Mathematical analysis determined two engines safer than three given modern engine reliability and common-mode fire risk.

## 🧠 First Principles & Mental Models

- **[[Margin of Safety]]**: The redundancy mental model is a structural instantiation of margin-of-safety thinking — building in spare capacity so that a single failure never becomes a catastrophe.
- **[[Second-Order Thinking]]**: Redundancy designed to improve safety can, through complexity and behavioral adaptation, produce the opposite effect — a canonical case where stopping at first-order effects ("adding backup = safer") misleads.
- **[[Goodhart's Law]]**: When safety becomes the measured target, actors optimize proxies (checking that a backup exists) rather than actual safety (verifying the backup works under all conditions) — exactly what happened with the Challenger O-ring assumptions.

## 🃏 Review Questions

**Q1**: What is the central claim of the redundancy mental model?
**A**: Redundancy means having more than one means of accomplishing a task so that all paths must fail before the system fails, multiplicatively reducing failure probability.

**Q2**: What are the three key ways redundancy can backfire?
**A**: (1) Common-mode errors where added complexity causes all components to fail together; (2) social shirking where human redundancy diffuses responsibility; (3) risk compensation where people engage in riskier behavior because they trust the safety backup.

**Q3**: How does the Challenger disaster apply this model to organizational decision-making?
**A**: NASA officials reversed their decision to postpone the launch because they were overconfident in the secondary O-ring as a backup, not accounting for the possibility that cold temperatures would degrade both O-rings simultaneously — a textbook common-mode failure compounded by risk compensation.
