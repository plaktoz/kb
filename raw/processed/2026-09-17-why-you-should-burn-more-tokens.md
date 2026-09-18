---
source_url: https://every.to/context-window/why-you-should-burn-more-tokens
author: Laura Entis
date: 2026-09-17
---

# Why You Should Burn More Tokens

Every CEO Dan Shipper uses more than 3x as many tokens as the next-highest employee. Rather than viewing high token spend as wasteful, he sees low usage as a potential warning sign that people aren't experimenting boldly enough.

The philosophy isn't reckless consumption — it's deliberate experimentation. After costly runs, the team asks three questions: What did it cost? What did it produce? What was learned?

## Key Practices

**Arielle Shipper (Head of Operations)** monitors spend via Slack notifications tied to the company card's auto-refill threshold, then checks the usage leaderboard when charges accelerate unusually.

**Randy Counsman (Head of Video)** burned ~4.5 billion tokens attempting a 3D face model using an unbounded multi-agent Codex setup. His prompt instructed the model to keep improving until done "extremely well" — an ambiguous target. The result was "very janky." He rebuilt the system with a 5-agent cap, dropped a redundant implementer layer, and added concrete visual targets for the judge agent.

**Marcus Moretti (Spiral GM)** stays within Claude Code Max weekly limits by matching model to task complexity:
- Routine work → Sonnet
- Scoped objectives → Opus
- Complex features → Fable 5.1

For complex work, he delegates downward with the instruction: *"use your judgment about delegating to a lower model."*

## Team Model Preferences (Week of Publication)

| Person | Model(s) |
|---|---|
| Katie Parrott | Sol (high) + Claude for writing |
| Arielle Shipper | Sol (medium) — "SOLoyalist" |
| Loren Stewart | Fable 5.1 for thinking; downgraded to Sol for coding |
| Tyler Nishida | Fable 5.1 + Grok 4.6 subagents via Cursor |
| Kieran Klaassen | Fable 5.1 (1M context) + Astra |
