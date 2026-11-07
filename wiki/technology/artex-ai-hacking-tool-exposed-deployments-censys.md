---
type: literature-note
source_url: https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web
author: Zack Whittaker
tags: [cybersecurity, ai-agents, penetration-testing, misconfiguration]
date_consumed: 2026-11-07
---

## Summary
Censys found more than 800 deployments of Artex, a Chinese-made open source autonomous penetration testing tool, exposed to the web without passwords. Artex has been linked to attacks on the Korean finance industry and on ConnectWise, many of which exploited simple weaknesses like weak passwords and missing multi-factor authentication. The exposure shows that misconfiguration can expose both attackers and their targets.

## Core Concepts
- [[Artex]]: open source system of AI agents for autonomous penetration testing, released in July.
- [[Autonomous Penetration Testing]]: software that automatically probes systems for weaknesses with little human input.
- [[Censys]] and researcher [[Silas Cutler]], who identified the exposed deployments.
- [[Misconfiguration]]: instances publicly reachable although the software does not require it.
- [[Multi-Factor Authentication]]: its absence enabled many linked attacks.
- [[CrowdStrike]] and [[Microsoft]] attribution of attacks to Chinese-speaking or Chinese-linked hackers.
- [[ConnectWise]] attack, which exposed customers' Microsoft cloud environments.
- [[Open Source Software]] dual-use risk after Artex went closed-source.

## Key Takeaways
- **Exposure Scale**: Over 800 distinct Artex deployments were accessible without a password.
- **Exposed Assets**: Open instances reveal attack tools, including implants for persistent access.
- **Linked Attacks**: Artex tied to Korean finance attacks in September and ConnectWise in October.
- **Speed**: Microsoft said defenders had little time to detect and respond.
- **Simple Flaws**: Many attacks used weak passwords and lacked multi-factor authentication.
- **Closed-Source Move**: Artex went closed-source, but dozens of code copies remain online.

## 🧠 Core Principles

**T1. A system is only as secure as its simplest weakness** — Advanced capabilities, offensive or defensive, are undermined by basic gaps such as weak passwords, missing MFA and misconfigured exposure. · *model:* [[Weakest Link Principle]]
→ explains: Exposure Scale, Exposed Assets, Simple Flaws

## 🃏 Review Questions

**Q1**: What did Censys discover about Artex?
**A**: More than 800 distinct Artex deployments, an open source AI penetration testing tool, were reachable from the web without a password. This could let outsiders misuse them for attacks.

**Q2**: How were Artex-linked attacks carried out, and what made them effective?
**A**: Many exploited simple vulnerabilities like weak or known passwords and missing multi-factor authentication. Microsoft said hackers moved so fast in cloud environments that defenders had little time to respond.

**Q3**: What lesson does the exposure offer?
**A**: Simple misconfigurations can expose both the attacker and their targets. Closing the source does not remove already-available copies, so dozens remain usable.
