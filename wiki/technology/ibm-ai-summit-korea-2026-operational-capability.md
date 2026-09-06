---
type: literature-note
source_url: https://finance.biggo.com/news/bb5a38b6-1b17-42ef-a7f3-b1c086a8a30d
author: Unknown
tags: [enterprise-ai, ai-operations, ibm, agentic-ai]
date_consumed: 2026-09-06
---

## Summary

At the IBM AI Summit Korea 2026, IBM Korea President Lee Soo-jung argued that enterprise AI competition has shifted from model quality to operational capability — the ability to connect AI to data, applications, infrastructure, and security at scale. IBM General Manager Nill Sundaresan reinforced this by framing AI agent deployment, governance, and cost management as far harder than building the agents themselves. Korean enterprises including KB Securities, SK Telecom, and Samsung Life Insurance confirmed that data quality foundations and integrated permission management are prerequisites for extracting AI value.

## Core Concepts

- **[[Operational Capability]]** — the competitive differentiator in enterprise AI: connecting AI to data, apps, infrastructure, and security; not model performance itself
- **[[AI-First Enterprise]]** — IBM's framework placing AI at the center of operations, built on four pillars: Intelligence, Action, Operation, and Trust
- **[[AI Agent Identity and Permissions]]** — managing which data agents can access, whose authority they act under, and what actions they can take; requires time-limited, purpose-scoped credentials and [[Principle of Least Privilege]]
- **[[Hybrid Cloud]]** — IBM's approach to running AI securely where data resides, managing workloads distributed across on-premises, public clouds, and multi-application ecosystems
- **[[Real-Time Data Streaming]]** — fresh, continuously generated enterprise data (via [[Confluent]], acquired by IBM) as the prerequisite for agentic AI that can make real-time judgments
- **[[Quantum-Centric Supercomputing]]** — IBM's roadmap combining CPUs, GPUs, and [[Quantum Processing Units (QPUs)]] for complex workloads; quantum as one pillar alongside HPC and AI, not a replacement
- **[[AI Cost Management]]** — tracking AI usage and cloud spend by department, service, and model; measuring outcomes against AI investments as part of the operating model
- [[Nill Sundaresan]] — IBM General Manager of Automation and AI; framed agentic AI operations as primarily an engineering and governance challenge
- [[Lee Soo-jung]] — IBM Korea President; keynoted that operations, not models, determine enterprise AI outcomes

## Key Takeaways

- **Operations over models**: AI competition is won by connecting AI to enterprise systems, not choosing better models.
- **Phase shift**: Enterprise AI has moved past individual productivity gains into redesigning work and decision-making.
- **Agent governance gap**: Deploying agents is easy; governing, securing, and managing them at scale is the hard problem.
- **Data freshness required**: Agentic AI needs continuously generated real-time data — not data refined days or months earlier.
- **Permission management**: Time-limited, purpose-scoped credentials (not long-lived tokens) are essential in multi-agent environments.
- **Cost is operational**: Every AI action incurs cost; usage must be tracked by department, service, and model.
- **Korean enterprise consensus**: KB Securities, SK Telecom, Samsung Life Insurance all agreed data quality and metadata management are foundational.
- **Human verification**: Even in agentic environments, human sign-off at critical decision stages remains necessary.
- **Quantum as complement**: QPUs handle specific complex workloads alongside HPC and AI — not a GPU replacement.
- **AI + cloud are inseparable**: AI strategy and cloud strategy must be treated as one unified infrastructure decision.

## 🧠 First Principles & Mental Models

- **[[Bottleneck Theory]]**: Lee's argument maps directly onto the Theory of Constraints — the model is no longer the bottleneck; operations (data integration, permissions, governance, cost) are. Optimizing the model when operations are the constraint yields no system-level gain.
- **[[Principle of Least Privilege]]**: Sundaresan's call for time-and-purpose-limited agent credentials is a direct application of this security principle to non-human identities — the same logic that governs human access must now govern agent access at scale.

## 🃏 Review Questions

**Q1**: What is the core competitive differentiator in enterprise AI according to IBM Korea's President?
**A**: Operational capability — the ability to connect AI to enterprise data, applications, infrastructure, and security systems and scale it enterprise-wide — not model performance or model selection.

**Q2**: Why is agent identity and permission management a new challenge in the agentic AI era?
**A**: In environments where numerous agents (not just humans) access enterprise systems, organizations must track which data each agent accessed, under whose delegated authority, and what actions were taken — requiring time-and-purpose-limited credentials rather than long-lived tokens.

**Q3**: How should organizations approach AI cost control as part of their operating model?
**A**: Track AI usage and cloud costs by department, service, and model, and measure outcomes against AI investments — treating cost governance as an integral part of operating the AI system, not an afterthought.
