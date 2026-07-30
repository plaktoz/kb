---
type: literature-note
source_url: https://techscoop.substack.com/p/why-model-context-protocol-could
author: Hey Maria
tags: [mcp, ai-security, prompt-injection, enterprise-governance]
date_consumed: 2026-07-29
---

## Summary
[[Model Context Protocol]] standardizes how AI agents connect to enterprise tools and data, but that same connectivity turns it into a new attack surface once agents can act with autonomy rather than deterministic code paths. The biggest MCP-specific risks are [[Tool Poisoning]] (malicious instructions hidden in tool metadata), [[Indirect Prompt Injection]] via untrusted content the agent reads, and overbroad access tokens that expand blast radius. Enterprises need MCP governed as privileged infrastructure — inventoried, vetted, least-privilege scoped, monitored for drift, and covered by incident response.

## Core Concepts
- **[[Model Context Protocol]] (MCP)** — open standard connecting AI agents to tools/data; described as "the USB-C port for AI agents."
- **[[Tool Poisoning]]** — malicious instructions embedded in a tool's name, description, or schema that the model reads but the user doesn't see; includes "rug pull" attacks where a tool's metadata changes after approval.
- **[[Indirect Prompt Injection]]** — untrusted content (emails, tickets, documents) the agent processes gets misread as instructions, potentially triggering tool misuse or data exfiltration.
- **[[Blast Radius]]** in AI agents — overbroad access tokens/scopes let a single compromised instruction path cause outsized damage; least privilege matters more with models in the loop.
- **[[MCP Supply Chain Risk]]** — third-party/community MCP servers become high-impact dependencies; cites an OX Security-reported SDK vulnerability enabling potential remote code execution.
- **MCP governance layers** — inventory, vetting, least privilege, execution isolation, consent for risky actions, continuous monitoring, drift detection, incident response.

## Key Takeaways
- Agency, not connectivity alone, is what makes MCP riskier than traditional API integrations.
- Treat tool metadata as executable influence, not static documentation.
- Separate data from instruction: external content agents read must stay untrusted input.
- SREs need MCP-specific telemetry: tool-call failure rate, policy-blocked actions, metadata-change events, cost spikes.
- A random developer-installed MCP connector shouldn't automatically join the enterprise agent platform.
- Sensitive/high-risk actions should require human confirmation gated outside the model.
