---
type: literature-note
source_url: https://userpilot.com/blog/product-strategy
author: Emilia Korczynska
tags: [product-strategy, ai-agents, mcp, saas]
date_consumed: 2026-09-06
---

## Summary

Product strategy in 2026 must now serve two distinct user classes simultaneously: human users and AI agents acting on their behalf. AI-accelerated engineering velocity has collapsed the viable strategy horizon from 12 months to one quarter, while the rapid adoption of [[Model Context Protocol]] (MCP) — reaching 97 million monthly SDK downloads and 28% of the Fortune 500 in production by early 2026 — proved that technology shifts can render annual plans obsolete within months. The core insight is that shipping faster is no longer the constraint; figuring out what's worth building fast enough to keep pace with the build pipeline is.

## Core Concepts

- **Two user classes**: [[Human Users]] and [[AI Agents]] must be planned for in parallel — often within the same account on the same day.
- **[[Model Context Protocol]] (MCP)**: Grew from Anthropic's November 2024 launch to 97M monthly SDK downloads and ~28% Fortune 500 production deployment by Q1 2026; the integration layer for agent-native products.
- **Quarterly strategy cadence**: The 12-month product strategy is obsolete; quarterly refresh is the new minimum viable planning horizon.
- **Stream A / Stream B**: Stream A targets human users with in-app onboarding, discovery, and adoption; Stream B targets agent users with [[API Design]], task-completion metrics, and outcome-based pricing.
- **[[Agentic-Era Pricing]]**: Seat-based pricing breaks when a single agent handles hundreds of tasks per day; pricing shifts to tasks completed, tokens consumed, or outcomes delivered.
- **Engineering velocity vs. user adoption bandwidth**: Shipping velocity increased 7–9x; user attention did not — the win condition is the ratio of shipped features to features users actually adopt.
- **[[In-App Onboarding]]**: Continuous re-onboarding becomes critical at high shipping velocity — the difference between a feature that lands and one that ships into silence is often a single in-app nudge.
- **Kill conditions**: Every feature should have a documented kill condition before it ships; quarterly bottom-quartile culling prevents velocity-driven clutter.

## Key Takeaways

- **Dual user classes**: Plan for both human users and AI agents — same account, same day.
- **Quarterly cadence**: Strategy docs that can't be refreshed in one working day are too long.
- **MCP adoption speed**: 100K → 97M monthly downloads in 16 months; annual plans can't track this.
- **Discovery discipline**: AI makes shipping the wrong thing faster and more expensive to undo.
- **Adoption ratio**: Win condition is features adopted, not features shipped.
- **Continuous onboarding**: High shipping velocity requires continuous in-app re-onboarding, not one-time signup flows.
- **Agent metrics**: Replace DAU/session-length with task completion rates, error rates, latency, cost per action.
- **Seat pricing is dead**: Agents run hundreds of tasks per human seat; price on outcomes, not seats.
- **Netlify data point**: ~80% of Netlify new signups are agents — the agent share of B2B SaaS is already large.
- **Team structure**: Keep most of the team on Stream A (revenue); stand up a small Stream B group sharing the same strategy doc.
- **Automate monitoring, keep judgment human**: Reserve human judgment for which feature deserves a sprint, not dashboard maintenance.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: When shipping velocity becomes the primary win condition, teams optimize for shipped features rather than adopted ones — the article's "ratio of shipped to adopted" reframes the metric to resist this failure mode.
- **[[Innovator's Dilemma]]**: Teams focused on human-user revenue (Stream A) are structurally slow to build agent-native infrastructure (Stream B), leaving the highest-growth surface under-resourced; the two-stream model is a deliberate hedge.
- **[[OODA Loop]]**: The collapse of the strategy horizon from 12 months to one quarter is a direct application of the loop — faster observe-orient-decide-act cycles win when the environment changes faster than annual planning can track.

## 🃏 Review Questions

**Q1**: What is the core argument about product strategy planning horizons in 2026?
**A**: The 12-month strategy is obsolete because MCP adoption and AI-driven engineering velocity can reshape the competitive landscape within a single quarter; quarterly refresh is now the minimum viable cadence.

**Q2**: How did MCP adoption demonstrate the failure of annual planning?
**A**: MCP went from Anthropic's quiet November 2024 launch with ~100K SDK downloads to 97 million monthly downloads and 28% Fortune 500 production deployment by early 2026 — a trajectory no 2025 annual strategy doc anticipated.

**Q3**: How should product teams adapt their metrics and pricing for AI agent users?
**A**: Replace session/DAU metrics with task completion rates, error rates, and cost per action; replace seat-based pricing with outcome- or usage-based models, since a single agent can generate hundreds of tasks against one human seat.
