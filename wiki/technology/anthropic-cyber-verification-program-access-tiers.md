---
type: literature-note
source_url: https://www.anthropic.com/news/cyber-verification-program
author: Anthropic
tags: [anthropic, cybersecurity, ai-safety, dual-use]
date_consumed: 2026-10-07
---

## Summary

[[Anthropic]] has merged [[Project Glasswing]] and its [[Cyber Verification Program]] (CVP) into one expanded offering with three access tiers — Defense, Red Team, and Specialized — that give vetted security professionals advanced cyber capabilities and reduced blocking classifiers on its most capable models. Because cybersecurity is inherently dual use, generally available models keep conservative cyber safeguards, while verified defenders get progressively fewer blocks depending on the scope of their work. Anthropic backs the tier design with [[CyScenarioBench]] results and cites Glasswing's track record of 129,000+ verified vulnerabilities found by partners.

## Core Concepts

- **[[Cyber Verification Program]] (CVP)**: Anthropic's trusted-access program granting reduced safeguards to vetted security teams; now covers [[Claude Opus 5.5]], [[Claude Sonnet 5.5]], [[Claude Mythos 5.1]], and future models.
- **[[Project Glasswing]]**: The prior program giving organizations securing the most critical software access to [[Claude Mythos]]; its members transition to the Specialized tier without reapproval for current models.
- **Defense Access**: For SOC and [[Incident Response]] work, malware [[Reverse Engineering]], and vulnerability analysis/validation; open to company, nonprofit, university and government security teams, critical infrastructure operators of any size, smaller security firms, open-source maintainers, and individual researchers with a disclosure track record. Applications answered within a few days.
- **Red Team Access**: Adds authorized [[Penetration Testing]] and [[Red Teaming]] against systems the org is authorized to test; organizations only (no individuals), review takes a few weeks, with interim Defense enrollment. Real-time blocks remain on ransomware deployment, damaging physical systems, or pen testing high-risk safety systems.
- **Specialized Access**: Fewest cyber blocks; reserved for verified organizations authorized to test life- or market-critical safety systems (flight operating systems, power grids, telecom networks, interbank transfer infrastructure, government administrative networks); every org reviewed in depth with the US government.
- **[[Enterprise Frontier Safeguards]] (EFS)**: A forthcoming (later this fall) solution combining [[Zero Data Retention]] privacy with robust safeguards, letting eligible orgs store data in cloud infrastructure they control.
- **[[Dual-Use Dilemma]]**: The same capabilities that let defenders find and fix vulnerabilities can help attackers exploit them — the rationale for tiered access.
- **[[CyScenarioBench]]**: An evaluation measuring whether models can plan and execute multi-stage cyber operations under realistic constraints, used to test tier-specific safeguards.

## Key Takeaways

- **Program consolidation**: Glasswing and CVP merge into one three-tier offering after six months.
- **GA models stay conservative**: Opus 5.5, Fable 5.1, Sonnet 5.5 block most cyber work by default.
- **GA still useful**: Code review, patching known issues, owned-code vuln finding, alert triage remain allowed.
- **No-CVP baseline**: Every CyScenarioBench task blocked on the first prompt.
- **Defense tier**: 46 of 50 trials blocked at some point; 4 succeeded.
- **Red Team tier**: Zero blocks; Opus 5.5 completed 34 of 50 tasks.
- **Unsafeguarded ceiling**: 67.6% success rate, representative of Specialized Access.
- **Glasswing impact**: Partners found 129,000+ verified vulnerabilities, April–July 2026.
- **Anthropic's own scanning**: 5,500 additional verified open-source vulnerabilities, April–October 2026.
- **Severity**: 33,000+ rated critical or high; true impact estimated at least 5x higher.
- **Speed-up**: Partners said Mythos models accelerated vulnerability finding by months or years.
- **Data retention required**: Enables misuse monitoring; ZDR allowed for existing Fable/Mythos ZDR customers until EFS.
- **Availability**: Claude Platform, Vertex AI, Microsoft Foundry; Bedrock only for EFS-eligible customers.

## 🧠 First Principles & Mental Models

- **[[Dual-Use Dilemma]]**: Since offensive and defensive cyber capability are the same underlying skill, Anthropic cannot gate by capability alone and instead gates by verified identity and authorized scope — making access control, not model training, the primary safety lever.
- **[[Principle of Least Privilege]]**: Each tier grants only the cyber capabilities a role requires (defense → red team → safety-critical testing), with verification burden and security controls scaling alongside the permissions granted.

## 🃏 Review Questions

**Q1**: What is the core change Anthropic made to its Cyber Verification Program?
**A**: It merged Project Glasswing and the CVP into a single expanded program with three tiers — Defense, Red Team, and Specialized Access — each granting progressively fewer cyber blocks on its most capable models based on verified scope of work.

**Q2**: How did CyScenarioBench results validate the tier design?
**A**: Without CVP every task was blocked on the first prompt, Defense Access blocked 46 of 50 trials, and Red Team Access had no blocks with Opus 5.5 completing 34 of 50 tasks — roughly matching its 67.6% unsafeguarded success rate.

**Q3**: Which tier should a regional hospital's security team versus a power-grid testing firm apply for?
**A**: The hospital team defending its own systems fits Defense Access, while an organization authorized to test power-grid safety systems would need Specialized Access, which is reviewed in depth with the US government.
