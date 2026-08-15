---
source_url: https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec.html
author: Marc Brooker
date: 2026-04-09
---

# Spec Driven Development isn't Waterfall

Brooker argues that specification-driven development (as implemented in tools like Kiro) is frequently mischaracterized as a return to waterfall methodology. The core distinction he draws: specs aren't meant to be exhaustive *upfront* designs — they're meant to be *elevated*, living artifacts that sit above implementation and evolve iteratively.

He grounds this in Agile principles, noting that software requirements are inherently dynamic, conflicting, and incomplete. In spec-driven development, **the specification becomes the thing being iterated on**, not the code directly.

Specs are described as explicit statements of requirements and key design decisions, abstracted above implementation. They can incorporate free-form language, structured formats (RFC2119, EARS), or formal methods (TLA+, Lean) where needed. Implementation — increasingly AI-generated — flows *downstream* from the spec.

A key advantage Brooker emphasizes: specs enable AI agents to work **autonomously for extended periods**, giving them a "map" rather than turn-by-turn prompts. This produces higher quality, better-tested code because the agent understands the broader goal.

He concludes that humans remain essential to the *outer loop* — refining specs, navigating trade-offs, and resolving conflicting requirements — while the future of software development moves toward a higher abstraction level, continuing the historical progression from switches → gates → instructions → code.
