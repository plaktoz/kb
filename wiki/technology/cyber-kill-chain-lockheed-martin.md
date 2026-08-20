---
type: literature-note
source_url: https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
author: Unknown
tags: [cybersecurity, kill-chain, threat-intelligence, intrusion-detection]
date_consumed: 2026-08-20
---

## Summary

[[Lockheed Martin]] developed the [[Cyber Kill Chain]] as part of its [[Intelligence Driven Defense]] model to identify and prevent cyber intrusions. The framework maps the seven sequential steps adversaries must complete to reach their objectives, providing defenders with structured visibility into attack progression. By understanding attacker tactics, techniques, and procedures (TTPs), defenders can interrupt the chain at any phase to neutralize threats.

## Core Concepts

- **[[Cyber Kill Chain]]**: A seven-phase model describing the full lifecycle of a cyber attack — from reconnaissance to achieving adversary objectives.
- **[[Intelligence Driven Defense]]**: Lockheed Martin's overarching security philosophy, using threat intelligence to proactively shape defenses rather than react to incidents.
- **[[Advanced Persistent Threat]] (APT)**: Targeted, coordinated, purposeful attacks by actors with demonstrated intent, opportunity, and capability.
- **[[Tactics, Techniques, and Procedures]] (TTPs)**: The behavioral fingerprint of adversaries; illuminated by the kill chain to improve analyst visibility.
- **[[Cyber COBRA]]**: A Lockheed Martin sub-framework for rating the severity of cyber findings based on contextual factors.
- **[[LM-CIRT]]**: Lockheed Martin's Computer Incident Response Team — handles enterprise-wide detection, assessment, and mitigation of threats, and collaborates with industry and government on network defense.

## Key Takeaways

- **Seven-step model**: Kill chain phases map full adversary lifecycle to improve analyst visibility.
- **APT breakdown**: Advanced = targeted; Persistent = coordinated; Threat = actor with intent + capability.
- **Interrupt anywhere**: Disrupting any phase can prevent adversary from reaching objectives.
- **Threat intelligence integration**: White papers cover applying the framework with threat intelligence platforms.
- **Defendable architectures**: Supporting resources include threat-driven security design principles.
- **Severity rating**: [[Cyber COBRA]] provides contextual scoring for cyber findings.

## 🧠 First Principles & Mental Models

- **[[Kill Chain Thinking]]**: Breaking a complex adversary process into discrete, interruptible steps — the same decomposition principle used in military operations — reveals that no single defense is sufficient, but any successful disruption along the chain prevents mission completion.
- **[[Defense in Depth]]**: The kill chain framework operationalizes layered defense: if an adversary passes one control, subsequent phases offer additional interception opportunities before objectives are achieved.

## 🃏 Review Questions

**Q1**: What is the core purpose of the Cyber Kill Chain framework?
**A**: It maps the seven steps adversaries must complete to reach their objectives, giving defenders structured visibility to identify and interrupt attacks at any phase.

**Q2**: How does Lockheed Martin define an Advanced Persistent Threat (APT)?
**A**: APT stands for Advanced (targeted, coordinated, purposeful), Persistent (sustained and coordinated), and Threat (person(s) with intent, opportunity, and capability to act).

**Q3**: How should defenders apply the Cyber Kill Chain in practice?
**A**: By analyzing adversary TTPs against the seven phases, defenders can interrupt the chain at any step — halting an intrusion before the adversary achieves their objective.
