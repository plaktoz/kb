---
type: literature-note
source_url: https://zenity.io/press-release/zenity-labs-discloses-agentcorruption-a-chain-of-aws-agentcore-flaws
author: Unknown
tags: [ai-agents, cloud-security, prompt-injection, aws]
date_consumed: 2026-10-10
---

## Summary

Zenity Labs disclosed "AgentCorruption," a chain of flaws in Amazon Bedrock AgentCore that let a single prompt to one public-facing agent escalate into full compromise of every AgentCore agent in the same AWS account and region. The attack combined an overprivileged default IAM role with enumerability weaknesses to steal credentials, source code, and private conversations, and to plant persistent malicious memories. AWS has since made IMDSv2 the default and tightened the default execution role's permissions.

## Core Concepts

- **[[Amazon Bedrock AgentCore]]**: AWS's managed runtime for deploying AI agents, found to share an overprivileged default IAM role across all agents in an account and region.
- **[[Prompt Injection]]**: A single malicious prompt to a public-facing agent triggered the entire attack chain, directing it to query the [[AWS Instance Metadata Service]] (IMDS) for credentials.
- **[[Lateral Movement]]**: The stolen machine credentials, scoped too broadly, let researchers pivot from an internet-facing customer service agent to internal, sensitive agents in the same environment.
- **[[Agent Memory Poisoning]]**: Researchers implanted malicious long-term memories that persistently redirected future conversations to an attacker-controlled destination, surviving beyond the initial compromise.
- **[[Zenity Labs]]**: Security research firm that disclosed the findings at SecTor 2026 in Toronto and responsibly reported them to AWS in December 2025.
- **Least Privilege vs. Agency**: The core tension the researchers highlight — agents need latitude to be useful, while cloud security architecture is built around minimizing access.

## Key Takeaways

- **One prompt, full account takeover**: A single prompt to one public agent exposed all AgentCore agents in the account/region.
- **Root cause**: Default IAM role credentials via IMDS were not scoped to the originating agent.
- **Blast radius**: Attackers could read all conversations, download container images, retrieve source code, and extract API keys, OAuth tokens, and Secrets Manager credentials.
- **Persistence mechanism**: Malicious memories let attackers hijack agent behavior across future sessions, not just a one-time breach.
- **Disclosed Dec. 25, 2025**: AWS responded by defaulting to IMDSv2 and removing cross-agent invocation, conversation-read, and secrets-access permissions from the default role.

## 🧠 First Principles & Mental Models

- **[[Weakest Link Principle]]**: Overall system security is bounded by its least-restricted component — one public-facing agent with an overprivileged shared role became the entry point that collapsed isolation across an entire AWS account and region.
- **[[Defense in Depth]]**: The flaw existed because segmentation assumptions (per-agent isolation) were undermined by a single shared infrastructure layer (the default IMDS-backed role) — a single control failure cascaded because no secondary boundary caught it.

## 🃏 Review Questions

**Q1**: What is the core claim of this research?
**A**: A chain of flaws in AWS Bedrock AgentCore allowed a single prompt sent to one public-facing agent to compromise every AgentCore agent within the same AWS account and region.

**Q2**: What was the key mechanism that enabled account-wide compromise?
**A**: The attacker prompted the agent to query the AWS Instance Metadata Service, retrieving credentials for a default IAM role whose permissions extended to all AgentCore agents rather than being scoped to the single agent.

**Q3**: What should organizations deploying AI agents on cloud platforms take away from this?
**A**: Default execution roles and shared infrastructure must be scoped per-agent, not per-account, since agents need "creative space" that directly conflicts with cloud security's least-privilege default.

