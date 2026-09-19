---
type: literature-note
source_url: https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/
author: Aditya Mehta, Rebecca Bellan
tags: [ai-security, bug-bounty, offensive-security, llm-hacking]
date_consumed: 2026-09-19
---

## Summary

Researchers at startup Hacktron AI used [[Anthropic]]'s [[Claude]] Opus 5 to breach [[OpenAI]]'s systems in an authorized bug-bounty engagement, chaining a Discourse image-processing vulnerability with a memory bug in libheif to reach an internal GitHub repository. Claude Opus 4.8 failed to produce a working exploit, but Opus 5 succeeded within hours of its release. OpenAI awarded $6,500 and patched the vulnerabilities.

## Core Concepts

- [[Hacktron AI]] — three-person startup that ran the authorized bug-bounty engagement against OpenAI
- [[Claude Opus 5]] — the model that succeeded in generating a working exploit where Opus 4.8 had failed, illustrating rapid capability jumps between model generations
- [[Bug Bounty Program]] — authorized framework under which the attack was conducted; distinguishes this from autonomous AI hacking incidents
- [[Discourse]] (community forum software) — first link in the exploit chain; flawed HEIF/HEIC image upload handling triggered a vulnerable processing pipeline
- [[ImageMagick]] / [[libheif]] — the downstream libraries; a pre-existing, unpatched memory bug in libheif enabled code injection despite a developer fix existing (no CVE assigned, so the vulnerable version remained deployed)
- [[OpenAI]] GitHub repository — ultimate target reached by chaining the two vulnerabilities, granting access to employee ChatGPT and Codex accounts

## Key Takeaways

- **Capability threshold**: Opus 4.8 failed; Opus 5 cracked the same problem within hours of release.
- **Low cost barrier**: Security expert Matt Fredrikson noted anyone can do this for $200/month.
- **Exploit chain**: Discourse → ImageMagick → libheif memory bug → code injection → internal GitHub.
- **CVE gap**: Libheif's fix existed but the absence of a CVE kept the vulnerable version in production.
- **Payout**: OpenAI awarded Hacktron $6,500 and has since patched both vulnerabilities.
- **Precedent**: Occurs weeks after OpenAI agents autonomously breached Hugging Face, underscoring AI as both attack tool and attack target.

## 🧠 First Principles & Mental Models

- **[[Capability Overhang]]**: The jump from Opus 4.8 to Opus 5 converting a failed exploit attempt into a hours-long success illustrates that offensive capability gains are discontinuous — a model just below a task threshold provides false assurance that the task is AI-hard.
- **[[Security Through Obscurity]]**: The libheif vulnerability persisted not because it was unpatched by developers but because no CVE was assigned — downstream deployments never received the signal to update, showing that disclosure mechanisms, not just fixes, are part of the security chain.

## 🃏 Review Questions

**Q1**: What was the core finding of Hacktron AI's bug-bounty engagement with OpenAI?
**A**: A three-person team used Claude Opus 5 to chain two vulnerabilities — in Discourse's image upload pipeline and libheif's memory handling — to access OpenAI employee accounts and an internal GitHub repository, earning a $6,500 bounty.

**Q2**: Why did the libheif vulnerability remain exploitable despite a developer fix being available?
**A**: The bug had been patched by libheif's developers but was never assigned a CVE designation, so the vulnerable version remained in use at OpenAI because the lack of a CVE meant downstream operators received no formal patch signal.

**Q3**: What does the Opus 4.8 vs. Opus 5 contrast imply for defenders and security teams?
**A**: A model that currently fails to exploit a given vulnerability is not a permanent ceiling — a successor model released weeks later may succeed quickly, meaning defenders cannot treat today's AI capability limitations as durable security assumptions.
