---
type: literature-note
source_url: https://newsletter.pragmaticengineer.com/p/the-revised-rules-of-engineering
author: Gergely Orosz
tags: [engineering-management, leadership, zirp, career-ladders]
date_consumed: 2026-10-23
---

## Summary

Will Larson (CTO, Imprint; former CTO of Carta and Calm) argues that engineering management was profoundly shaped by the zero interest rate period (ZIRP) of the 2010s, creating practices — such as banning managers from making technical decisions, avoiding oncall for senior engineers, and defaulting to hiring over tooling — that are now obsolete. Larson's blunt message is that middle managers must either re-skill (returning to hands-on technical and line-management work) or retire, as the engineering leadership profession as it existed in 2015–2022 will not exist in three years.

## Core Concepts

- [[Will Larson]] — CTO of Imprint; author of *An Elegant Puzzle*, *Staff Engineer*, *The Engineering Executive's Primer*, and *Crafting Engineering Strategy*
- [[ZIRP]] (Zero Interest Rate Period) — shaped 2010s tech management by making talent retention the primary competitive differentiator, pulling leverage to engineers
- [[Tech Lead Manager]] (TLM) — role previously described by Larson as a "career trap"; now in high demand as engineering managers are expected to be technical contributors
- [[Principal-Agent Problem]] — engineers oncall for software they build leads to better reliability; removing oncall from senior engineers degraded software quality
- [[Incentive Alignment]] — Yahoo's "black market" for servers illustrates how well-intentioned accountability mechanisms produce perverse behaviors
- [[Goodhart's Law]] — Digg v4 rewrite was driven by a hard CEO-imposed deadline, leading to performance/reliability failures that alienated users
- [[Conway's Law]] — engineering organization structures and their management norms reflect and reinforce the systems they produce
- [[Parkinson's Law]] — referenced directly in the episode; bureaucratic management tools expand to fill available managerial time

## Key Takeaways

- **ZIRP-Era Relic**: 2010s management practices (engineer-first hiring, no technical decisions by managers) were responses to a talent-scarce market that no longer exists.
- **Hire Less**: "Hiring is the least interesting way to solve every problem" — Larson now tells teams almost never to talk about hiring.
- **Oncall = Quality**: Engineers oncall for their own software build better, more reliable systems; removing oncall was a talent-retention hack with quality costs.
- **TLM in Demand**: Engineering managers managing 12–14 people (vs. 4–8 before) who also write code are now the most sought-after hires.
- **Technical Decisions Return**: EMs no longer told to never make technical decisions; being hands-on and technical is now a baseline expectation.
- **Exec Dual Role**: Great engineering executives must be both bureaucrats (navigate incentives and bureaucracy) and technologists (know what to build and why).
- **Digg v4 Lesson**: Hard CEO deadline, compounded by Python memory leaks from developers unfamiliar with Python, caused reliability catastrophe — though Larson believes Facebook/Reddit would have displaced Digg regardless.
- **Step Back to Move Forward**: Larson voluntarily shrunk from leading 250 engineers at Carta to 25 at Imprint to re-skill; recommends others consider the same.
- **Blunt Warning**: Middle managers who don't re-skill face retirement; the profession "will not exist in three years" in its current form.
- **AI & Flow**: Some engineers are retiring from tech because AI has destroyed the ability to enter "flow"; those focused on outcomes (not process) are thriving.

## 🧠 Core Principles

**T1. Macro-financial conditions shape management norms, and those norms outlast the conditions that created them** — the ZIRP era made talent retention the key competitive lever, producing engineer-centric management practices that became embedded culture; when rates normalized and AI changed leverage dynamics, those norms became liabilities rather than assets.
→ explains: **ZIRP-Era Relic**, **Hire Less**, **TLM in Demand**

**T2. Incentive design shapes behavior more powerfully than intentions** — Yahoo's server approval process meant to create accountability instead created a black market, demonstrating that any control mechanism that makes the desired path more costly than a workaround will produce the workaround. · *model:* [[Incentive Alignment]]
→ explains: **Oncall = Quality**, **Hire Less**

**T3. Removing skin in the game from engineers degrades system reliability** — when senior engineers are shielded from oncall, they lose the feedback signal that drives quality; engineers who experience the pain of their own outages build more reliable software. · *model:* [[Principal-Agent Problem]]
→ explains: **Oncall = Quality**

## 🃏 Review Questions

**Q1**: What is Will Larson's central claim about 2010s engineering management practices?
**A**: They were shaped by ZIRP-era talent scarcity, making retention the dominant concern and producing engineer-centric norms (no manager technical decisions, avoiding oncall for senior engineers) that are now counterproductive in a post-ZIRP, AI-driven environment.

**Q2**: What does the Yahoo server "black market" story illustrate about incentive design?
**A**: When Yahoo cofounder David Filo required personal approval for every server purchase to drive accountability, engineers bypassed the system by trading servers from canceled projects — showing that incentive mechanisms producing perverse workarounds will always be exploited.

**Q3**: What is Larson's practical recommendation for middle managers in today's engineering landscape?
**A**: Retire or re-skill — specifically, return to line management and hands-on technical work rather than pure bureaucratic middle management, as the profession in its 2015–2022 form will not exist in three years due to AI's impact on team leverage.
