---
source_url: https://www.prnewswire.com/news-releases/cisco-and-openai-launch-shirudo-a-new-project-to-safeguard-agentic-ai-302948685.html
author: Cisco Systems, Inc.
date: 2026-11-23
---

# Cisco and OpenAI Launch Shirudo, A New Project to Safeguard Agentic AI

An industry-first open source project, Shirudo, helps systems defend themselves at machine speed

## News Summary

Defenders can start protecting systems before a permanent patch is in place. Cisco and OpenAI are making that possible through an open source effort to build infrastructure that is secure by default and defends itself.

Shirudo, an open source project built on industry-leading eBPF, helps protect running Linux systems without a reboot while teams roll out a patch.

This marks a shift from human-paced policy updates to self-defending, agent-driven security. AI agents do the legwork across the full stack, from models and data to the kernel and hardware, while people keep the keys and set the boundaries.

SAN JOSE, Calif., Nov. 23, 2026 /PRNewswire/ -- Cisco (NASDAQ: CSCO) and OpenAI today launched an open source effort to make infrastructure secure by default and able to defend itself against today's sophisticated cyber attacks. For too long, security has been a coat of paint. Cisco builds protection into the infrastructure itself, drawing on decades of building and protecting the systems the world depends on. OpenAI brings leading frontier AI research and insight into the attacks coming next. Together, they combine their insight to help anticipate AI-driven threats with the control to stop them.

Defenders must protect every part of their infrastructure, all the time. Attackers only need one machine that hasn't been patched. Shirudo is an important step toward closing that gap. The goal is infrastructure that is hardened from the moment it is built, keeps getting harder to attack, and can be restored to a known-good state if it is compromised.

"There is nothing more important than giving security teams the tools they need to match the speed of the AI-driven threats they are facing. We need self-defending infrastructure that acts at the speed of code, learns in real time, and shields itself until patches are safely rolled out," said Jeetu Patel, Cisco President and Chief Product Officer. "Today, we're proud to announce Shirudo with OpenAI, an important step towards that vision as we continue to collaborate with the wider community to solve the unique challenges of AI safety and security."

"We're giving defenders better models and tools to find and fix vulnerabilities faster, but finding a bug today doesn't mean you can patch every system tomorrow," said Greg Brockman, President and Co-founder of OpenAI. "We are partnering closely with Cisco on Shirudo to help teams protect the systems they need to keep running while they build and roll out a fix. So many teams rely on the same software that it makes sense to build these tools in the open. Now when one team finds a better way to protect a system, others don't have to start from scratch."

## Shirudo: An Open Source Project from Cisco and OpenAI

Shirudo, Japanese for "shield," uses eBPF, a technology that runs small, custom programs inside the operating system kernel without changing its source code. With it, AI agents can find a vulnerability, build a shield, and test that it stops the attack without disrupting the service. Shields go live only when the evidence says they are safe. Every shield is cryptographically signed, so the host can verify it before it runs, even if an attacker has gained administrator access.

In testing against recent critical vulnerabilities "Java4shell" and the PHP flaw, Shirudo was able to write code that detected and blocked attempts to exploit both threats. By utilizing an agentic framework, Shirudo matches the speed of AI-driven attacks as soon as a vulnerability is identified.

Cisco and OpenAI are inviting developers, researchers, and enterprises to help shape what comes next. Contribute a test that reproduces a vulnerability, run a shield against a kernel build you use, or show us where it breaks legitimate traffic. To learn more about Shirudo, visit: https://github.com/shirudo-dev/shirudo.

Join us for a deep dive webinar on December 15.
