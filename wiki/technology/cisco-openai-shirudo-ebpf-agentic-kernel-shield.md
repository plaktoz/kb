---
type: literature-note
source_url: https://www.prnewswire.com/news-releases/cisco-and-openai-launch-shirudo-a-new-project-to-safeguard-agentic-ai-302948685.html
author: Cisco Systems, Inc.
tags: [ebpf, agentic-security, linux-kernel, open-source, vulnerability-patching]
date_consumed: 2026-11-24
---

## Summary

[[Cisco]] and [[OpenAI]] launched Shirudo, an open source project built on [[eBPF]] that lets running Linux systems be shielded against a known vulnerability without a reboot while a permanent patch is rolled out. The project proposes AI agents that find a vulnerability, build a signed shield and test that it blocks the attack without disrupting service. The press release reports that Shirudo blocked exploit attempts against the Java4shell and a PHP flaw in testing, but the claims come from the vendors themselves.

## Core Concepts

- **[[Shirudo]]**: Open source project whose name is Japanese for "shield"; it runs small custom programs inside the kernel without changing kernel source.
- **[[eBPF]]**: Technology that runs sandboxed programs inside the operating system kernel, which is the mechanism Shirudo uses to block attacks.
- **[[Agentic Security]]**: Security work in which AI agents find vulnerabilities, write defenses and test them, while people set the boundaries.
- **[[Weakest Link Principle]]**: The press release's framing that attackers need only one unpatched machine, so every part of the infrastructure must be protected.
- **[[Signed Security Shields]]**: Each shield is cryptographically signed so the host can verify it before running, even if an attacker has administrator access; shields go live only when the evidence says they are safe.
- **[[Java4shell]]** and the PHP flaw: The two recent critical vulnerabilities used in testing.
- **[[Jeetu Patel]]** and **[[Greg Brockman]]**: Cisco's President and Chief Product Officer and OpenAI's President and Co-founder, quoted in the launch.

## Key Takeaways

- **Shield Before Patch**: Protect running systems while a permanent patch is still being rolled out.
- **No Reboot Needed**: Shirudo works on running Linux systems without a restart.
- **Agents Do the Legwork**: AI agents find, shield and test vulnerabilities at machine speed.
- **Humans Keep the Keys**: People set boundaries while agents act across the stack.
- **One Unpatched Machine**: Attackers only need a single system that hasn't been patched.
- **Signed Shields**: Each shield is cryptographically signed and verified before it runs.
- **Evidence-Gated Deployment**: Shields go live only when testing shows they are safe.
- **Vendor-Reported Tests**: Java4shell and PHP blocking results come from the companies themselves.
- **Open Call for Testers**: Developers are invited to contribute reproducing tests and kernel builds.
- **Webinar December 15**: Deep dive session announced for December 15.

## 🧠 Core Principles

**T1. Protection must cover every component, because one gap is enough** — An attacker who finds one unpatched system can compromise the whole, so defense only works if it is applied everywhere at once. · *model:* [[Weakest Link Principle]]
→ explains: One Unpatched Machine, Shield Before Patch

**T2. A defense must work during the window before a fix is deployed** — When discovering a bug is faster than patching every system, protection has to come from a separate layer that works while the patch is pending.
→ explains: Shield Before Patch, No Reboot Needed, Evidence-Gated Deployment

## 🃏 Review Questions

**Q1**: What is the central claim of the Shirudo launch?
**A**: Infrastructure can be made to defend itself by applying kernel-level shields that protect running systems while a permanent patch is rolled out, rather than waiting for patches to reach every machine.

**Q2**: How does Shirudo decide when a shield is allowed to run?
**A**: Each shield is cryptographically signed so the host can verify it, and shields go live only when the agent's testing shows they block the attack without disrupting the service.

**Q3**: What does the launch imply for teams that run Linux systems?
**A**: Teams can consider a shield-based stopgap during patch rollouts, and they can contribute tests or report where a shield breaks legitimate traffic, though the reported results are the vendors' own claims and need independent checking.
