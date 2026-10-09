---
source_url: https://zenity.io/press-release/zenity-labs-discloses-agentcorruption-a-chain-of-aws-agentcore-flaws
author: Unknown
date: 2026-10-08
---

# AgentCorruption: AWS AgentCore Flaws Let One Prompt Hijack All Agents

Zenity Labs Discloses AgentCorruption, a Chain of AWS AgentCore Flaws That Allowed One Prompt to Take Over All AgentCore Agents Within an AWS Account and Region

TORONTO – Oct. 8, 2026 – Zenity Labs today disclosed AgentCorruption, new research identifying a chain of security flaws in Amazon Bedrock AgentCore. Using a single prompt to one public-facing agent, researchers took over all AgentCore agents within the same AWS account and region, accessed private conversations and cloud credentials and persistently manipulated agent behavior. The underlying vulnerabilities discovered by Zenity Labs were systemic to AgentCore and affected any agent equipped with built-in tooling across AWS accounts.

The vulnerabilities gave researchers access to internal agents they were not authorized to use, along with source code, long-term memories, API keys, OAuth tokens and other credentials stored in AWS Secrets Manager. Researchers also implanted malicious memories that directed agents to transmit future conversations to an attacker-controlled destination.

Zenity Labs disclosed the findings in conjunction with the presentation of AgentCorruption at SecTor 2026 in Toronto.

"Cloud security is all about segmentation and least-privilege access. AI agents, however, need their creative space to be useful. Mixing the two creates an inherent conflict," said Michael Bargury, co-founder and CTO of Zenity. "Every company deploying agents in the cloud will run into the same fundamental choices to be made between agency and least privilege. Our research shows the difficulties in getting those just right."

## A Single Agent Could Expose All Agents Across the Entire Region

The attack began when researchers sent a prompt to a public-facing AgentCore agent equipped with a commonly used tool capable of making outbound requests. The prompt instructed the agent to access the AWS Instance Metadata Service (IMDS), which provides temporary credentials to cloud workloads.

AgentCore's infrastructure allowed the agent to reach the IMDS endpoint and retrieve the credentials assigned to its underlying machine. Those credentials belonged to a default AWS Identity and Access Management role whose permissions were not limited to the original agent but instead extended to all AgentCore agents within the same AWS account and region. Researchers could therefore use the credentials obtained from one public-facing agent to access other AgentCore agents throughout the same AWS account and region.

Together, the infrastructure design flaw and overprivileged role turned access to a single agent into an entry point to the organization's wider AgentCore environment. For example, an attacker entering through an internet-facing customer service agent could move laterally to an internal finance agent deployed in the same region, invoke it, and access its data and tools, related credentials and private conversations.

## Further Vulnerabilities and Impact

From this initial public-facing entry point, the researchers continued by exploiting multiple vulnerabilities, combining enumerability weaknesses and internal APIs to achieve devastating impacts:

Discover and invoke all AgentCore agents within the same AWS account and region, including internal and sensitive agents they were not authorized to access

Read all private conversations and long-term memories across agents, users and sessions

Download agent container images, read them in full and retrieve agents' source code

Retrieve API keys, OAuth tokens and other credentials stored in AWS Secrets Manager and environment variables. This includes credentials used by AgentCore agents to connect to enterprise resources and third party services beyond AWS

The researchers also abused the agents' memory functionality to create malicious memories that altered agent behavior and directed all future conversations to an attacker-controlled destination

## Persistent Access Through Agent Memory

The ability to modify agent memory extended the attack beyond one-time access. By planting instructions that remained in memory, researchers demonstrated how an attacker could establish persistence and covertly hijack an agent's goals and behavior across future interactions. Users would continue interacting with what appeared to be a trusted enterprise agent while it operated under attacker-controlled instructions behind the scenes and transmitted conversations to outside destinations.

## Why the Findings Matter

Enterprises are rapidly adopting AI agents, with cloud platforms becoming the default deployment environment. This creates a fundamental security challenge: agents need their creative space to be useful, while cloud security is built around limiting access as much as possible.

AgentCorruption shows what can happen when that balance breaks. A single agent can become an entry point to a much larger environment, allowing attackers to access resources far beyond the agent they initially compromised.

This matters well beyond AgentCore. Enterprises routinely run customer-facing and internal agents side by side in the same cloud environments. These agents often handle sensitive employee and customer data and are connected to powerful tools, business applications and more. As agents gain more autonomy and more access, a single unexpected weakness in one agent could collapse the boundaries of an entire environment, and open paths to data and resources that were never meant to be exposed.

## Responsible Disclosure

Zenity Labs responsibly disclosed the AgentCore findings to AWS on Dec. 25, 2025. Following the disclosure, AWS made IMDSv2 the default for AgentCore deployments. Zenity Labs' testing confirmed that AWS had reduced the default execution role's permissions. This included the removal of the permissions that allowed agents to invoke other agents, read private conversations or access secrets stored in AWS Secrets Manager. Zenity Labs thanks AWS for its collaboration throughout the process.
