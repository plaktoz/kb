---
type: literature-note
source_url: https://danluu.com/bug-blind/
author: Dan Luu
tags: [software-quality, cognitive-bias, engineering-culture, usability]
date_consumed: 2026-08-30
---

## Summary

Dan Luu argues that most people aren't encountering fewer software bugs — they've developed unconscious workarounds that mask them, creating a pervasive "bug blindness." This blindness afflicts both users and the developers who build broken products, since programmers are especially adept at adapting to problems rather than perceiving them as problems. Quality blindness is treatable: pointing out bugs to receptive people causes them to start noticing independently within weeks.

## Core Concepts

- **[[Bug Blindness]]** — the inability to perceive software defects you encounter regularly, because habitual workarounds have rendered them invisible
- **[[Habitual Workarounds]]** — unconscious compensatory behaviors developed over time that mask underlying software failures (e.g., waiting before typing a Google Docs title, moving a mouse erratically to compensate for debris)
- **[[Dogfooding]]** — the practice of having developers use their own software; Luu argues it backfires because programmers are most skilled at developing workarounds
- **[[Betriebsblindheit]]** — German word meaning "operational blindness to familiar problems"; the exact phenomenon Luu describes
- **[[Blackboard (software)]]** — widely considered among the most disliked software ever, yet its own employees believed users loved it — a canonical example of internal quality blindness
- **[[Advertising Blindness]]** — analogous phenomenon: people don't notice hospital ads despite being surrounded by them; A/B tests prove ads work even when users believe they don't
- **[[LLM Software Quality]]** — LLMs now make it easier to both produce low-quality software and to improve quality, but only if the developer first notices quality is improvable

## Key Takeaways

- **Workarounds, not fewer bugs**: Users aren't hitting fewer bugs; they've learned to compensate unconsciously.
- **"Computer literacy" = workaround library**: A large fraction of tech skill is memorized compensations for broken software.
- **Dogfooding paradox**: Developer self-use helps less than expected — programmers adapt best.
- **Internal perception gap**: Discourse gamed benchmarks; Blackboard employees thought users loved the product.
- **Curable blindness**: Bug awareness spreads through pointing — recipients notice independently within weeks.
- **Reflexive developer defense**: "It's easy, just do [complex sequence]" is a pattern, not a solution.
- **Fan bias**: Enthusiasts systematically overlook flaws in products/teams they're loyal to.

## 🧠 First Principles & Mental Models

- **[[Availability Bias]]**: Developers only notice bugs they personally experience in salient ways; habitual workarounds prevent salience, so bugs stay invisible to the people best positioned to fix them.
- **[[Goodhart's Law]]**: When benchmark scores become the target (as with Discourse artificially slowing real performance to game metrics), the measurement decouples from the underlying quality it was meant to track.
- **[[Adaptation-Level Phenomenon]]**: Repeated exposure to broken behavior recalibrates one's baseline — what was once a noticeable defect becomes the invisible "normal."

## 🃏 Review Questions

**Q1**: What is the core claim of Luu's bug blindness argument?
**A**: People aren't hitting fewer bugs — they've developed unconscious workarounds that mask problems, creating the illusion of quality where none exists.

**Q2**: Why does dogfooding (having developers use their own software) fail to reliably catch bugs?
**A**: Programmers are especially skilled at developing workarounds, so they adapt to problems rather than perceiving them as problems that need fixing.

**Q3**: How can bug blindness be cured, and what evidence does Luu give?
**A**: Simply pointing out bugs to receptive people causes them to start noticing independently within weeks; years later, some report they "see bugs everywhere now."
