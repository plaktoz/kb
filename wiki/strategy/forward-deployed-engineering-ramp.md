---
type: literature-note
source_url: https://builders.ramp.com/post/forward-deployed-engineering
author: Unknown
tags: [forward-deployed-engineering, enterprise-b2b, engineering-org, customer-success]
date_consumed: 2026-08-04
---

## Summary

Forward Deployed Engineering (FDE) places engineers directly with customers throughout the full account lifecycle — from pre-sales to long-tail support — to deliver value at maximum speed. Originally invented by [[Palantir]] post-2003, the model is now standard at [[OpenAI]], [[Anthropic]], [[Ramp]], and many AI startups because enterprise B2B companies grow at roughly twice the rate of non-enterprise peers (~30% vs ~15% CAGR). Ramp's FDE team grew ~10x to 16 engineers after launching in late 2023, evolving from reactive firefighting to proactive platform and AI tooling work.

## Core Concepts

- **[[Forward Deployed Engineering]] (FDE)** — embedding engineers at customer sites or accounts to iterate on real problems with full lifecycle ownership
- **[[Enterprise B2B Moat]]** — per Foundation Capital, "how you integrate, embed, and operate becomes the moat" in enterprise software
- **[[Customer Lifecycle Ownership]]** — FDEs span pre-sales, onboarding, activation, and long-tail support rather than handing off at go-live
- **[[Scoping as a Core Skill]]** — questioning every requirement upfront to prevent multi-month misfires; a 3-engineer-day gap was resolved in a single call via workaround
- **[[Generalization vs. One-Off Hacks]]** — the central FDE judgment call: when to build a scalable solution vs. a quick customer-specific fix
- **[[Extreme Ownership]]** — FDEs treat customer outcomes as personal responsibility, not something to hand off
- **[[AI Tooling in Engineering]]** — the Ramp FDE team uses [[Cursor]] and [[Claude Code]] extensively; AI tools also close engineering skill gaps in hiring

## Key Takeaways

- Enterprise CAGR (~30%) is roughly 2x non-enterprise (~15%), making enterprise the high-value target.
- FDE originated at [[Palantir]] post-2003; now standard at [[OpenAI]], [[Anthropic]], [[Ramp]].
- Ramp FDE team: 2 engineers at launch (late 2023) → 16 FDEs; ~10x growth.
- **Prioritization order**: retention → onboarding/activation → TAM expansion.
- **"Always Be Scoping"**: direct customer contact catches misaligned assumptions before engineering begins.
- Generalize solutions wherever possible — ad-hoc customizations compound into technical debt.
- Speed + ownership = FDE's two non-negotiable traits; "perfect is the enemy of good."
- **Hiring signals**: drive/work ethic is the single strongest predictor; 7 of 16 FDEs are former founders.
- Customer empathy is critical — FDEs navigate tense negotiations, delays, and de-scoping calls.

## 🧠 First Principles & Mental Models

- **[[Extreme Ownership]]**: FDEs take personal accountability for customer outcomes rather than diffusing responsibility across handoffs — this directly reduces the principal-agent gap that degrades most enterprise implementations.
- **[[Inversion]]**: "Always Be Scoping" applies inversion by questioning whether the stated problem is the right problem to solve before investing engineering effort — preventing effort spent on the wrong solution entirely.

## 🃏 Review Questions

**Q1**: What is the core purpose of Forward Deployed Engineering and why is it becoming standard in enterprise AI?
**A**: FDEs embed engineers with customers throughout the full account lifecycle to deliver value at maximum speed; enterprise B2B companies grow at ~30% CAGR vs ~15% for non-enterprise, making deep integration and outcome delivery the competitive moat.

**Q2**: What is the "Always Be Scoping" principle and what problem does it solve?
**A**: FDEs question every customer requirement directly rather than relaying through account executives; this breaks the failure pattern where a multi-month engineering project is scoped based on a misunderstood requirement — in one case, a 3-engineer-day gap was resolved in a single call via a workaround.

**Q3**: How does Ramp prioritize FDE work, and what does that reveal about the operating philosophy?
**A**: The priority order is: serve existing customers first (retention), then accelerate onboarding/activation, then expand product capabilities — reflecting a belief that retaining and activating current customers yields more durable growth than chasing new logo expansion.
