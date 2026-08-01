---
type: literature-note
source_url: https://techscoop.substack.com/p/why-model-context-protocol-could
author: Hey Maria
tags: [mcp, ai-security, enterprise-ai, prompt-injection]
date_consumed: 2026-08-01
---

## Summary

Model Context Protocol (MCP) is rapidly becoming the standard integration layer connecting AI agents to enterprise tools, databases, and workflows — but its power is precisely what makes it a significant attack surface. Unlike traditional deterministic API integrations, MCP-connected agents make dynamic decisions about tool use, creating a new class of operational and security risks including tool poisoning, indirect prompt injection, and supply chain vulnerabilities. Enterprises must treat MCP as privileged infrastructure — not a developer convenience layer — with governance, least-privilege access, and continuous monitoring baked in from the start.

## Core Concepts

- **[[Model Context Protocol]]** (MCP): Open-source standard that gives AI agents a standardized way to connect to external systems — described as a "USB-C port" for AI apps.
- **[[Tool Poisoning]]**: Malicious instructions embedded in MCP tool metadata (names, descriptions, schemas) that manipulate the model into unsafe behavior without the user seeing them. Can include "rug pull" attacks where tools behave safely at review time, then change metadata later.
- **[[Indirect Prompt Injection]]**: Malicious instructions hidden in content the agent reads (emails, documents, tickets, web pages) that the model may confuse for valid instructions, potentially triggering tool misuse.
- **[[Blast Radius]]**: The scope of damage possible if an agent with overly broad permissions is compromised or manipulated; overbroad access tokens amplify risk dramatically.
- **[[AI Supply Chain Risk]]**: Third-party MCP servers, community connectors, and SDKs become high-impact security dependencies that can influence model behavior, access enterprise data, and trigger actions.
- **[[Least Privilege]]**: Core security principle that agents and MCP servers should receive only the minimum access required; becomes more critical, not less, when models are involved.
- **[[MCP Governance]]**: Operational framework covering inventory, vetting, least privilege, execution isolation, consent workflows, continuous monitoring, drift detection, and incident response for MCP deployments.
- **[[SRE]] Observability**: MCP-specific telemetry needed beyond traditional service metrics — tool-call volume, policy-blocked actions, metadata changes, scope elevation events, and cost anomalies.

## Key Takeaways

- **MCP as Attack Surface**: Every enterprise system MCP connects to expands the agent's attack surface.
- **Agency is the Differentiator**: AI agents choose tools dynamically; traditional integrations are deterministic — this gap creates novel risk.
- **Tool Metadata is Executable**: In agentic workflows, tool descriptions influence model decisions — treat them as executable, not documentation.
- **Prompt Injection Escalates**: Against MCP-connected agents, prompt injection can trigger tool misuse, not just bad answers.
- **Rug Pull Attacks**: A tool can behave safely during approval, then change metadata post-approval to manipulate behavior.
- **Least Privilege is Critical**: A support agent shouldn't have broad DB write access; a coding agent shouldn't touch production secrets.
- **Supply Chain Vigilance**: MCP servers need provenance, version pinning, vulnerability scanning, and runtime monitoring like any production dependency.
- **Governance Layers**: Inventory → vet → least privilege → isolate → consent → monitor → drift detection → incident response.
- **SRE Signals**: Spikes in failed tool calls, policy blocks, data retrieval, or metadata changes are all MCP-specific incident indicators.
- **Design Before Production**: MCP security must be designed in before agents reach production — not retrofitted after an incident.

## 🧠 First Principles & Mental Models

- **[[Principle of Least Privilege]]**: The entire MCP governance framework reduces to this: constrain what agents can reach so a wrong or manipulated decision can only cause bounded damage — the model reasons, but the platform enforces.
- **[[Attack Surface Expansion]]**: Every new integration layer that increases capability increases attack surface proportionally; MCP is powerful precisely because it connects many systems, and that connectivity is the threat vector — the same first-principles reasoning that made USB ports a security concern applies here at the AI infrastructure layer.
