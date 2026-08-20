---
source_url: https://www.crowdstrike.com/cybersecurity-101/threat-hunting/
author: Kurt Baker
date: 2025-03-04
---

# Introduction to Cyber Threat Hunting

## What is Cyber Threat Hunting?

Threat hunting is the proactive practice of searching for cyber threats lurking undetected within a network. It digs deep to find malicious actors that have slipped past initial endpoint defenses.

After gaining access, an attacker may remain hidden for months — quietly collecting data, seeking confidential material, or harvesting credentials to move laterally. Many organizations lack the detection capabilities to stop such threats once defenses are breached.

---

## Threat Hunting Methodologies

Threat hunters assume adversaries are already present and investigate for unusual behavior. Three main investigative approaches exist:

### 1. Hypothesis-Driven Investigation
Triggered by newly identified threats from crowdsourced attack data, hunters look for whether specific attacker tactics, techniques, and procedures (TTPs) exist in their environment.

### 2. IOC/IOA-Based Investigation
Uses tactical threat intelligence to catalog known indicators of compromise (IOCs) and indicators of attack (IOAs) as triggers for uncovering hidden or ongoing malicious activity.

### 3. Advanced Analytics and Machine Learning
Combines data analysis and machine learning to detect irregularities across massive datasets. Anomalies become hunting leads investigated by skilled analysts.

All three approaches blend human expertise with advanced security technology.

---

## Threat Hunting Steps

### Step 1: The Trigger
Unusual actions flagged by detection tools — or a hypothesis about a new threat — point hunters toward specific systems or network areas.

### Step 2: Investigation
Hunters use tools like EDR (Endpoint Detection and Response) to examine potential compromises. Investigation continues until activity is deemed benign or fully characterized.

### Step 3: Resolution
Findings are communicated to operations and security teams for incident response. Collected data — on both malicious and benign activity — feeds back into automated tools to improve future detection.

---

## Where Threat Hunting Fits

Threat hunting runs in parallel with standard incident detection, response, and remediation. While automated tools generate alerts from raw data, hunters use queries and automation to extract leads from the same data, which skilled analysts then assess for adversary activity.

---

## Should You Use a Managed Threat Hunting Service?

The core challenge is sourcing qualified personnel. Skilled threat hunters are scarce and expensive. Managed services can provide deep expertise and 24/7 vigilance at lower cost.

**Three components of an effective threat hunting service:**

1. **Human Capital** — Automated detection is predictable; today's attackers exploit that. Human hunters remain critical for identifying sophisticated targeted attacks.
2. **Wealth of Data** — Granular system event data must be gathered and stored for full endpoint and network visibility, analyzed in real time via scalable cloud infrastructure.
3. **Threat Intelligence** — Internal data must be cross-referenced with external threat intelligence, using sophisticated tools to correlate malicious actions.

Most organizations aren't equipped to run continuous 24/7 hunting operations, making managed solutions an attractive option.

---

## Extended Data Storage and Threat Hunting

Retaining security data long-term enables hunters to draw on both real-time and historical context. Benefits include:

- Faster discovery of hidden threats
- Improved removal of advanced persistent threats (APTs)
- Better vulnerability prioritization before exploitation

Unifying multiple log sources — security detections and threat intelligence — allows hunters to narrow detection scope, reducing false positives and accelerating response.

---

## CrowdStrike's Managed Threat Hunting

**CrowdStrike Falcon® OverWatch™** offers a 24/7 managed hunting solution combining elite human hunters, vast telemetry, and powerful analytics. The service proactively hunts across CrowdStrike's global customer community to identify sophisticated attacks that would otherwise go undetected — finding breaches days, weeks, or months earlier than automated-only methods.
