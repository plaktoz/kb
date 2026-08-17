---
type: literature-note
source_url: https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-confirms-claude-is-down-in-major-outage-affecting-multiple-services/
author: Mayank Parmar
tags: [anthropic, claude, outage, reliability]
date_consumed: 2026-08-17
---

## Summary
[[Anthropic]] confirmed a major outage on August 16, 2026, beginning at 21:58 UTC, that disrupted authentication and degraded performance across [[Claude.ai]], [[Claude Code]], and [[Claude Cowork]] for roughly 40 minutes, while the Claude API and Console stayed operational.

## Core Concepts
- **[[Service Outage]]**: The incident started as an authentication failure preventing sign-in, then broadened into degraded performance across Claude.ai and platform.claude.com.
- **[[Status Page Transparency]]**: Anthropic posted staged updates (investigating → degraded performance → resolution) via its public status page, a common incident-communication pattern for cloud AI providers.
- **[[Blast Radius]]**: The outage hit consumer (Claude.ai), developer (Claude Code), and enterprise (Claude Cowork) surfaces simultaneously, but spared the underlying API/Console — suggesting the fault was in a shared auth/front-end layer rather than model-serving infrastructure.

## Key Takeaways
- **Timeline**: Outage began 21:58 UTC Aug 16; broader degraded-performance update posted at 22:07 UTC.
- **Scope**: Claude.ai, Claude Code, and Claude Cowork were marked "major outage"; Claude API and Console remained operational throughout.
- **Cause**: Anthropic did not disclose a root cause at time of reporting.

## 🃏 Review Questions

**Q1**: What is the core claim of the article?
**A**: Anthropic experienced a major outage on August 16, 2026, that disrupted authentication and access across several of its core products.

**Q2**: Which services were affected, and which stayed up?
**A**: Claude.ai, Claude Code, and Claude Cowork were marked as experiencing a major outage, while the Claude API and Console remained operational.

**Q3**: What does the pattern of affected vs. unaffected services suggest about the failure?
**A**: Since the API/Console stayed up while front-end and auth-dependent products went down, the fault likely originated in a shared authentication or front-end layer rather than core model-serving infrastructure.
