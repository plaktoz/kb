---
type: literature-note
source_url: https://martinfowler.com/bliki/Yagni.html
author: Martin Fowler
tags: [yagni, software-design, extreme-programming, agile]
date_consumed: 2026-08-03
---

## Summary

YAGNI ("You Aren't Gonna Need It") is an [[Extreme Programming]] principle that warns against building software capabilities presumed needed in the future. [[Martin Fowler]] argues that "presumptive features" — code written for functionality not yet in use — incur real costs even when the feature eventually proves useful, and that roughly two-thirds of planned features fail to improve their intended metrics.

## Core Concepts

- **[[YAGNI]]** — do not implement something until it is actually needed; anticipatory code creates guaranteed costs for uncertain benefits
- **[[Extreme Programming]] (XP)** — the methodology that originated YAGNI as a counterweight to late-1990s upfront planning culture
- **[[Martin Fowler]]** — author and proponent who frames YAGNI in terms of four distinct cost categories
- **Presumptive Features** — code supporting functionality not yet in active use; the primary target of the YAGNI principle
- **[[Evolutionary Design]]** — the design philosophy YAGNI enables: keep code malleable so future features can be added cheaply when actually needed
- **[[Continuous Delivery]]** — one of the enabling practices (alongside refactoring and self-testing code) that makes YAGNI safe to apply

## Key Takeaways

- **Cost of Build**: wasted effort if a presumed feature is never actually needed.
- **Cost of Delay**: other valuable features are deferred while presumptive work is done.
- **Cost of Carry**: premature abstractions add complexity that slows all subsequent work.
- **Cost of Repair**: features built early often need rebuilding as the team learns more.
- **Two-thirds rule**: research suggests ~2/3 of planned features fail to move their intended metrics.
- **Scope boundary**: YAGNI applies to features and abstractions, *not* to refactoring, self-testing code, or changes that reduce complexity.
- **Heuristic**: mentally simulate the refactoring needed to add a feature later — the future cost is often modest.
- **Key quote**: "Yagni is not a justification for neglecting the health of your code base. Yagni requires (and enables) malleable code."

## 🧠 First Principles & Mental Models

- **[[Expected Value Thinking]]**: Because ~2/3 of presumptive features never deliver value, the expected return on building them early is negative — Fowler's four cost categories make the math explicit rather than leaving it implicit.
- **[[Optionality]]**: Keeping code malleable preserves the option to add features later at low cost; building them now destroys that option and locks in speculative decisions made with less information.
- **[[Reversibility Principle]]**: Prefer actions that remain easy to undo or extend; presumptive features are harder to remove than to add, so deferring them keeps future choices open.

## 🃏 Review Questions

**Q1**: What is the core claim of YAGNI and where did it originate?
**A**: YAGNI holds that you should never build software capabilities until they are actually needed; it originated in Extreme Programming as a reaction to over-engineered upfront design.

**Q2**: What are the four cost categories Fowler identifies for presumptive features?
**A**: Cost of build (wasted effort), cost of delay (deferred valuable work), cost of carry (added complexity), and cost of repair (early builds may need rebuilding as requirements become clearer).

**Q3**: What does YAGNI explicitly *not* apply to, and why does that matter?
**A**: YAGNI does not apply to refactoring, self-testing code, or [[Continuous Delivery]] practices — these improve code malleability, which is precisely what makes it safe to defer features and add them cheaply later.
