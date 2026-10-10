---
type: literature-note
source_url: https://www.anthropic.com/news/anthropic-cyber-mission
author: Anthropic
tags: [anthropic, cybersecurity, critical-infrastructure, open-source]
date_consumed: 2026-10-10
---

## Summary

Anthropic launched the Anthropic Cyber Mission, a long-term effort to support cyber defenders, starting with two programs: the Critical Infrastructure Defense Program (CIDP), which brings frontier Claude models and on-site engineers to trusted providers securing power grids, water systems, and transportation networks, and OSS Scanner, a free opt-in service that scans open-source projects with Anthropic's most capable models. The initiative builds on lessons from Project Glasswing, which found 129,000+ verified vulnerabilities but struggled to translate findings into fixes fast enough. Anthropic frames the near-term cyber landscape as favoring attackers, with defense expected to gain the advantage only in roughly two years.

## Core Concepts

- **[[Anthropic Cyber Mission]]**: A new long-term Anthropic commitment to secure critical systems, starting with operational technology and open-source software and expanding to new areas over time.
- **[[Critical Infrastructure Defense Program]] (CIDP)**: Brings [[Claude]] frontier models, on-site Anthropic engineers, and threat research to trusted providers like Accenture, Booz Allen, CrowdStrike, Deloitte, Dragos, Hitachi, Insane Cyber, Nozomi Networks, Palo Alto Networks, PwC, and Rockwell Automation, who secure power, water, and transportation [[Operational Technology]] (OT).
- **[[OSS Scanner]]**: An opt-in service, inspired by Google's OSS-Fuzz, that gives enrolled open-source projects periodic, free, model-generated vulnerability scans with proof-of-concept exploits and suggested fixes, expecting a true-positive rate above 90%.
- **[[Project Glasswing]]**: Anthropic's earlier program that scanned open-source projects and privately disclosed vulnerabilities; it was merged into the expanded [[Cyber Verification Program]] and informed the Cyber Mission's design.
- **[[Operational Technology]]**: Industrial control systems and legacy equipment underlying power, water, and transportation networks that cannot easily be patched and where fixes can take years or decades.
- **[[Defender Advantage Fund]] (0xDAF)**: Anthropic fund launched in August that supports pilot cybersecurity programs and keeps OSS Scanner free, alongside funding to the Python Software Foundation, Alpha-Omega/OpenSSF, and the Apache Software Foundation.

## Key Takeaways

- **Two founding tracks**: CIDP for critical infrastructure, OSS Scanner for open-source code.
- **CIDP partners**: 11 founding organizations spanning consultancies, security vendors, and equipment makers.
- **OSS Scanner accuracy**: Expected true-positive rate above 90%, reports sent without human review.
- **Glasswing track record**: Partners found 129,000+ verified vulnerabilities but fixing lagged discovery by months.
- **OT constraint**: Fixes on running infrastructure can take years, in rare cases decades, to apply safely.
- **Forecast**: Anthropic expects AI to favor defense in about two years, but attackers currently have the edge.
- **Access paths**: Security vendors can join CIDP, maintainers can enroll in OSS Scanner, and any security team can apply to the Cyber Verification Program.

## 🧠 First Principles & Mental Models

- **[[Dual-Use Dilemma]]**: The same frontier model capabilities that find and patch vulnerabilities faster also lower the cost of attack, which is why Anthropic routes defensive power through vetted partners and opt-in disclosure programs rather than open access.

## 🃏 Review Questions

**Q1**: What is the core claim behind the Anthropic Cyber Mission?
**A**: Attackers currently benefit more than defenders from frontier AI, so Anthropic is deploying engineers, tools, and funding specifically to critical infrastructure providers and open-source maintainers to close that gap.

**Q2**: How does OSS Scanner work and what accuracy does Anthropic expect?
**A**: Enrolled open-source projects get periodic scans from Anthropic's most capable models, with each report including a proof-of-concept exploit and suggested fix sent without human review; Anthropic expects a true-positive rate above 90%.

**Q3**: Why does fixing vulnerabilities in critical infrastructure take so much longer than finding them?
**A**: Operational technology often cannot be taken offline to patch, so even once a vulnerability is verified and prioritized, applying a fix safely to running power, water, or transportation equipment can take years or decades.
