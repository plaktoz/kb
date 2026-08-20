---
type: literature-note
source_url: https://www.crowdstrike.com/cybersecurity-101/threat-hunting/
author: Kurt Baker
tags: [cyber-threat-hunting, cybersecurity, endpoint-detection, threat-intelligence]
date_consumed: 2026-08-20
---

## Summary

Cyber threat hunting is the proactive practice of searching for malicious actors lurking undetected within a network, operating on the assumption that defenses have already been breached. Hunters employ three main methodologies — hypothesis-driven investigation, IOC/IOA-based investigation, and machine learning-driven anomaly detection — following a trigger-investigate-resolve workflow. Because skilled hunters are scarce and expensive, many organizations turn to managed threat hunting services that combine human expertise, rich telemetry, and threat intelligence for 24/7 coverage.

## Core Concepts

- **[[Cyber Threat Hunting]]** — Proactive search for threats that have slipped past automated defenses, assuming adversaries may already be present.
- **[[Tactics Techniques and Procedures]] (TTPs)** — Behavioral fingerprints of known attackers used in hypothesis-driven hunts.
- **[[Indicators of Compromise]] (IOCs) / [[Indicators of Attack]] (IOAs)** — Tactical threat intelligence artifacts used to catalog known malicious activity.
- **[[Endpoint Detection and Response]] (EDR)** — Core tool used during the investigation step to examine potential compromises at the endpoint level.
- **[[Advanced Persistent Threat]] (APT)** — Long-dwell threat actors that extended data retention and hunting help identify and remove earlier.
- **[[Threat Intelligence]]** — External data cross-referenced with internal telemetry to correlate and contextualize malicious actions.
- **[[CrowdStrike]] Falcon OverWatch** — A managed threat hunting service combining elite analysts, global telemetry, and advanced analytics.
- **[[Machine Learning]] in Security** — Used to detect statistical anomalies across massive datasets, surfacing leads for human analysts.

## Key Takeaways

- **Proactive Posture**: Threat hunting assumes the network is already compromised — not waiting for alerts.
- **Three Methodologies**: Hypothesis-driven, IOC/IOA-based, and ML/analytics-driven investigations.
- **Three-Step Workflow**: Trigger → Investigation → Resolution with feedback into automated tools.
- **Human Expertise is Irreplaceable**: Automated tools are predictable; human hunters catch sophisticated, targeted attacks.
- **Dwell Time Risk**: Attackers can remain hidden for months, harvesting credentials and moving laterally.
- **Managed Services**: Most orgs lack staffing for 24/7 hunting; managed solutions offer expertise at lower cost.
- **Data Retention Matters**: Long-term storage of security logs enables historical context and faster APT removal.
- **Feedback Loop**: Hunt findings improve automated detection tools — reducing future false positives.

## 🧠 First Principles & Mental Models

- **[[Assume Breach]]**: Threat hunting operationalizes the "assume breach" posture — rather than trusting perimeter defenses, hunters treat compromise as the baseline state and search inward, reducing mean time to detect.
- **[[Signal vs. Noise]]**: Unifying log sources and cross-referencing threat intelligence narrows detection scope, directly addressing the core problem of separating meaningful signals from high-volume security noise.

## 🃏 Review Questions

**Q1**: What is the core premise that distinguishes threat hunting from standard automated security monitoring?
**A**: Threat hunting operates on the assumption that adversaries are already present in the network, proactively searching for threats rather than waiting for automated alerts to fire.

**Q2**: What are the three main threat hunting methodologies described, and what triggers each?
**A**: (1) Hypothesis-driven — triggered by newly identified TTPs from crowdsourced attack data; (2) IOC/IOA-based — uses known compromise/attack indicators as triggers; (3) ML/analytics-driven — uses anomaly detection over large datasets to surface investigation leads.

**Q3**: What are the three components of an effective managed threat hunting service, and why do organizations outsource this function?
**A**: The three components are human capital (skilled analysts), wealth of granular data (real-time cloud-scale telemetry), and threat intelligence (cross-referencing internal data with external feeds). Most organizations outsource because qualified threat hunters are scarce, expensive, and hard to staff for continuous 24/7 operations.
