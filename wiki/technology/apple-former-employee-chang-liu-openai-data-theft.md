---
type: literature-note
source_url: https://techcrunch.com/2026/08/31/apple-shares-shocking-evidence-against-former-employee-accused-of-stealing-company-data-for-openai/
author: Amanda Silberling
tags: [apple, openai, data-theft, intellectual-property]
date_consumed: 2026-09-01
---

## Summary

Apple filed what it calls "shocking evidence" in its lawsuit against [[OpenAI]], alleging that former employee [[Chang Liu]] used a confidential Apple circuit schematic in his OpenAI work and that OpenAI was knowingly complicit in his improper data access. Liu allegedly exploited a rare authentication bug to maintain post-employment access, and is accused of enlisting a colleague to destroy evidence after learning he was under investigation. Apple is seeking a preliminary injunction to block OpenAI from building hardware derived from Apple's proprietary technology.

## Core Concepts

- **[[Chang Liu]]** — former Apple engineer now at OpenAI; central defendant, accused of using Apple's confidential circuit schematics in his OpenAI work
- **[[Yu-Ting Peng]]** — OpenAI colleague allegedly recruited by Liu to destroy evidence in June 2026
- **[[Apple vs OpenAI Lawsuit]]** — Apple's ongoing litigation against OpenAI over alleged trade secret theft by former employees
- **[[Trade Secret Theft]]** — the legal theory underpinning Apple's claims; Liu's post-employment use of Apple IP constitutes misappropriation
- **[[Preliminary Injunction]]** — Apple's requested remedy: block OpenAI from any hardware work using Apple's technology
- **[[Expedited Discovery]]** — Apple's secondary request, citing concerns that additional former employees may be implicated
- **[[Authentication Bug]]** — a "rare, previously unknown" exploit Liu allegedly used to maintain Apple system access after his employment ended

## Key Takeaways

- **Smoking gun schematic**: Liu used a confidential Apple circuit schematic directly in his OpenAI work.
- **Tool name overlap**: A tool Liu built at OpenAI shares a name with an internal Apple engineering application.
- **OpenAI knew**: Apple alleges OpenAI was "well-aware" Liu had access to Apple data.
- **Evidence destruction**: Liu and colleague Yu-Ting Peng allegedly destroyed evidence in June 2026.
- **Source of evidence**: Liu's old Apple work laptop, handed over by his counsel in August.
- **OpenAI's defense**: Liu accessed Apple files post-employment only to help former colleagues; Apple's poor offboarding is to blame.
- **Apple's rebuttal**: Liu maintained access via a "rare, previously unknown authentication bug."
- **Scale of overlap**: 400+ former Apple employees now work at OpenAI, raising systemic exposure risk.

## 🧠 First Principles & Mental Models

- **[[Principle of Least Privilege]]**: Access should be revoked immediately upon departure; Liu's continued post-employment access via an authentication bug illustrates why fail-safe defaults and zero-trust architectures are foundational — not optional — corporate security controls.
- **[[Insider Threat]]**: The most dangerous IP leakage vector is often someone who once had legitimate access; this case shows the risk persists even after an employee leaves if offboarding processes have gaps.

## 🃏 Review Questions

**Q1**: What is Apple's core allegation against Chang Liu in its lawsuit against OpenAI?
**A**: Apple alleges Liu used a confidential Apple circuit schematic in his OpenAI work, and that OpenAI was "well-aware" of his improper access to Apple data — making both parties potentially liable.

**Q2**: How did Liu allegedly maintain access to Apple's systems after leaving the company?
**A**: Liu exploited "a rare, previously unknown authentication bug," according to Apple; OpenAI countered that Apple's own poor access-management processes during employee departures were to blame.

**Q3**: What does the statistic of 400+ former Apple employees at OpenAI imply for the litigation's scope?
**A**: It suggests the data-theft risk may not be isolated to Liu — Apple requested expedited discovery citing concerns that additional former employees could be implicated, making the case potentially systemic rather than individual.
