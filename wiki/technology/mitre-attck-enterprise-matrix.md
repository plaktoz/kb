---
type: literature-note
source_url: https://attack.mitre.org/
author: MITRE Corporation
tags: [cybersecurity, threat-modeling, adversary-tactics, attack-framework]
date_consumed: 2026-08-20
---

## Summary

[[MITRE ATT&CK]] is a globally-accessible knowledge base cataloguing adversary tactics and techniques derived from real-world observations, used as a foundation for [[Threat Modeling]] across private sector, government, and cybersecurity communities. The Enterprise Matrix organizes adversary behavior into 15 ordered tactics — from initial reconnaissance through final impact — each containing numbered techniques and sub-techniques. It is freely available and widely adopted as a common language for describing and defending against cyber threats.

## Core Concepts

- **[[MITRE ATT&CK]]**: A structured knowledge base mapping the full adversary lifecycle into observable, catalogued behaviors.
- **[[Adversary Tactics]]**: High-level objectives an attacker pursues (e.g., Reconnaissance, Execution, Exfiltration) — the "why" of an attack.
- **[[Adversary Techniques]]**: Specific methods used to achieve a tactic — the "how" (e.g., spear-phishing for Initial Access).
- **[[Threat Modeling]]**: The practice of using ATT&CK to systematically identify and prioritize potential threats to a system.
- **[[Enterprise Matrix]]**: The ATT&CK matrix covering 15 tactics and over 230 techniques for enterprise environments.
- **[[MITRE Corporation]]**: Non-profit that developed and maintains the ATT&CK framework.

## Key Takeaways

- **15 Tactics**: Covers the full kill chain from Reconnaissance (12 techniques) to Impact (15 techniques).
- **Largest tactic — Discovery**: 34 techniques, reflecting how attackers extensively enumerate environments post-compromise.
- **Stealth leads mid-chain**: 30 techniques for evading detection, the second-largest tactic category.
- **Free and open**: Available at no cost, widely adopted as a shared vocabulary across defenders.
- **Sub-techniques exist**: Each technique is further broken down into sub-techniques for granular threat mapping.
- **Real-world grounded**: Techniques are derived from observed adversary behavior, not theoretical attack paths.

## 🧠 First Principles & Mental Models

- **[[Adversarial Thinking]]**: ATT&CK operationalizes thinking from the attacker's perspective — defenders must model adversary goals and methods before they can detect or disrupt them, not just patch known CVEs.
- **[[Taxonomy as Leverage]]**: By naming and numbering techniques consistently, ATT&CK transforms amorphous threat intelligence into a reusable, comparable, and automatable format — the same power that Linnean classification gave biology.

## 🃏 Review Questions

**Q1**: What is the central purpose of MITRE ATT&CK?
**A**: It is a knowledge base of adversary tactics and techniques based on real-world observations, providing a common framework for threat modeling and defense across cybersecurity communities.

**Q2**: Which tactic contains the most techniques in the Enterprise Matrix, and what does that reveal?
**A**: Discovery has 34 techniques — the most of any tactic — reflecting that once inside a network, attackers invest heavily in enumerating systems, credentials, and data before moving laterally or exfiltrating.

**Q3**: How would a defender apply the ATT&CK Enterprise Matrix in practice?
**A**: A defender can map their detection capabilities against the 15 tactics to identify coverage gaps, then prioritize controls or logging rules for high-risk technique clusters (e.g., Stealth with 30 techniques) most relevant to their threat model.
