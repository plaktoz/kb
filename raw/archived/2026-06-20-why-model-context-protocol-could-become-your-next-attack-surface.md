# Why Model Context Protocol Could Become Your Next Attack Surface

source_url: https://techscoop.substack.com/p/why-model-context-protocol-could

---

**By Hey Maria — Jun 20, 2026**

### Model Context Protocol helps AI agents connect to tools, APIs, and enterprise data, but it also introduces new security risks.

Model Context Protocol, or MCP, is one of the most important pieces of AI infrastructure.

At a high level, MCP gives AI applications a standardized way to connect to external systems. Instead of every AI assistant, coding agent, internal chatbot, or workflow agent needing a custom integration for every database, SaaS tool, file system, API, or developer platform, MCP creates a common protocol for connecting models to tools and data.

That is why developers like it.

It reduces integration work. It makes agents more useful. It gives AI systems access to context beyond their training data. It allows models to move from "answering questions" to actually performing tasks.

But for SREs and platform engineers, that usefulness is also the warning sign.

The moment an AI agent can connect to enterprise systems, call tools, retrieve files, query databases, or trigger workflows, MCP becomes more than an integration standard.

It becomes part of the attack surface.

And like every new infrastructure layer before it, MCP will create risk not because it is useless, but because it is powerful.

## MCP Is the USB-C Port for AI Agents

The official MCP documentation describes the protocol as an open-source standard for connecting AI applications to external systems. It compares MCP to a USB-C port for AI apps: a standardized way to connect AI systems to data sources, tools, and workflows.

That analogy is useful, but it should also make security teams nervous.

A port is valuable because it connects things. But anything that connects systems can also become a path for abuse.

For enterprise AI, MCP can enable agents to access calendars, documents, databases, search engines, developer tools, internal APIs, cloud resources, and business workflows. That is exactly what makes it attractive for companies trying to deploy AI beyond simple chat.

- A support agent can pull customer history.
- A coding agent can interact with repositories.
- A finance agent can read invoices.
- A platform agent can query infrastructure.
- A security agent can investigate alerts.
- An operations agent can summarize incidents and recommend remediation.

But each of those integrations introduces a trust question:

- Should this agent be allowed to access this system?
- Should it be allowed to take this action?
- What happens if the tool is malicious?
- What happens if the tool description changes?
- What happens if the model is tricked into calling the wrong tool?
- What happens if an attacker hides instructions in data the agent reads?

MCP makes AI systems more capable. It also makes them more connected.

And connected systems need security boundaries.

## The Risk Is Not MCP Alone. It Is MCP Plus Agency.

MCP is not dangerous simply because it connects systems. Enterprises have connected systems for decades through APIs, service accounts, integrations, plugins, webhooks, CI/CD tools, and automation platforms.

The difference is agency.

With traditional integrations, the logic is usually deterministic. A developer writes the code. The system calls a specific API under specific conditions. The workflow may still have bugs, but the decision path is explicit.

With AI agents, the model may decide which tool to use based on a prompt, retrieved context, tool metadata, prior messages, user intent, and other inputs. The action path is more dynamic.

That creates a new class of operational and security risk.

- A model might choose the wrong tool.
- It might pass the wrong parameters.
- It might trust malicious external content.
- It might reveal data in a generated response.
- It might perform an action that is technically allowed but contextually unsafe.
- It might misinterpret a tool's description.
- It might be manipulated by instructions hidden in a document, webpage, issue, ticket, or email.

This is why MCP security is not just an AppSec problem. It is a platform engineering problem.

Platform teams will be the ones asked to standardize how agents connect to tools. SREs will be the ones asked to monitor whether those agents behave safely in production. Security teams will be the ones asked to define what agents are allowed to do. Business teams will be the ones expecting the automation to work.

If MCP becomes the common integration layer for enterprise agents, then MCP governance becomes enterprise infrastructure.

## Tool Poisoning

One of the most important MCP-specific risks is tool poisoning.

Tool poisoning happens when malicious instructions are embedded in a tool's metadata, such as its name, description, schema, or parameters. The user may not see those instructions, but the model can. Since LLMs use tool metadata to decide when and how to call tools, poisoned metadata can manipulate the model into unsafe behavior.

Microsoft describes tool poisoning as a subset of indirect prompt injection where an attacker embeds malicious instructions within MCP tool descriptions. These instructions may be invisible to users but interpreted by the AI model, potentially causing unintended tool calls, data exfiltration, or manipulation.

This is a serious shift in the threat model.

In a normal API integration, a tool description is documentation. In an agentic workflow, the tool description becomes part of the model's decision environment.

That means metadata is no longer harmless.

A malicious MCP server could advertise a normal-looking tool, such as "summarize document" or "search customer records," while hiding instructions that influence the model to leak data, ignore constraints, or call another tool. A compromised tool could behave safely during review and later change its metadata after approval. This is sometimes described as a "rug pull" attack.

For platform teams, the lesson is simple:

Do not treat MCP tool metadata as static documentation. Treat it as executable influence.

Tool descriptions, schemas, parameters, and server behavior need review, signing, versioning, monitoring, and drift detection. If a tool definition changes after approval, that should trigger a new review.

## Prompt Injection Gets Worse When Agents Have Tools

Prompt injection has been discussed for years, but MCP changes the impact.

A prompt injection attack against a chatbot may produce a bad answer. A prompt injection attack against an MCP-connected agent may trigger tool misuse.

This is where indirect prompt injection becomes especially dangerous. A user may not be attacking the model directly. Instead, the malicious instruction may be hidden in content the agent reads: an email, a webpage, a support ticket, a pull request, a document, a log entry, or a knowledge base article.

When the agent processes that content, it may confuse untrusted text for valid instruction.

Microsoft's MCP security guidance explains that indirect prompt injection can cause unintended actions such as data exfiltration, harmful or misleading content generation, or manipulation of subsequent interactions.

For enterprise teams, this matters because many valuable AI agents are designed to process untrusted inputs.

- A support agent reads customer messages.
- A coding agent reads issues and pull requests.
- A security agent reads alerts and threat intelligence.
- A procurement agent reads vendor documents.
- An executive assistant agent reads emails and calendars.

The more useful the agent, the more likely it is to ingest untrusted content.

That does not mean enterprises should avoid MCP entirely. It means they need to separate data from instruction.

External content should be treated as untrusted input. Tool calls should be constrained by policy. Sensitive operations should require confirmation. High-risk actions should be gated outside the model. Retrieval systems should label source trust levels. Agents should not be allowed to turn arbitrary content into privileged commands.

The model can reason. But the platform must enforce.

## The Blast Radius Problem

One of the biggest risks in MCP deployments is overbroad access.

The official MCP security best practices warn about broad access tokens that carry scopes such as files, databases, or admin permissions. If such a token is stolen, it can enable lateral data access, privilege chaining, and difficult revocation.

That is not just an MCP problem. It is a classic enterprise security problem showing up again in AI infrastructure.

The difference is that AI agents may make permission abuse easier to trigger because they sit between natural language intent and system action.

If an agent has access to too many tools, too much data, or too many environments, a single compromised instruction path can create a large blast radius.

A customer support agent should not have broad database write access. A coding assistant should not have unrestricted access to production secrets. A document summarization agent should not be able to call admin tools. An incident assistant should not be able to restart production services without approval. A local MCP server should not have unrestricted file and network permissions.

Least privilege matters more, not less, when models are involved.

MCP deployments should start with minimal access, then require incremental elevation for higher-risk actions. Tool access should be scoped by task, environment, user, data classification, and business context. If a user asks an agent to perform an action outside its normal scope, the platform should challenge, approve, or deny that request through policy.

The safest MCP architecture assumes the model may be wrong and limits what damage that wrong decision can cause.

## MCP Supply Chain Risk Is Real

MCP also introduces supply chain risk.

As MCP adoption grows, organizations will increasingly rely on third-party MCP servers, community-built connectors, marketplace tools, internal wrappers, SDKs, and hosted integrations. Every one of those components becomes part of the AI supply chain.

Recent research and security reporting have already raised concerns about MCP implementations and ecosystem-level risks. OX Security reported a systemic vulnerability affecting official MCP SDKs across multiple programming languages and claimed it could expose large numbers of servers to remote code execution. The issue was controversial, but the broader lesson is clear: MCP integrations are not just convenience code. They can become high-impact security dependencies.

Security researchers have also analyzed tool poisoning, shadowing, and rug pull attacks in MCP-based systems. One 2025 paper argued that MCP tool descriptors can be manipulated through adversarial instructions, while another 2026 threat-modeling study identified tool poisoning as a prevalent and impactful client-side vulnerability.

For enterprise platform teams, this means MCP servers should be treated like production dependencies.

- They need provenance.
- They need version pinning.
- They need vulnerability scanning.
- They need approval workflows.
- They need runtime monitoring.
- They need deprecation plans.
- They need an inventory.

A random MCP connector installed by a developer should not automatically become part of an enterprise agent platform. The "npm install" mindset is already risky in traditional software. In agentic AI, it can be worse because the dependency may influence model behavior, access enterprise data, and trigger actions.

## What Secure MCP Governance Looks Like

Microsoft's internal MCP governance approach offers a useful enterprise pattern. Microsoft describes using trusted servers, a living catalog, secure-by-default architecture, server vetting, inventory, isolation, TLS, logging, and consent before changes.

That is the right direction because MCP security cannot rely on one control.

A secure enterprise MCP program should include several layers.

First, create an MCP inventory. Every MCP server should be known, registered, owned, categorized, and risk-rated. Unknown servers should not be allowed to connect to enterprise agents.

Second, vet MCP servers before use. Review the source, maintainer, permissions, schemas, tool descriptions, network behavior, authentication model, and update process. Hosted and local servers should go through different review paths because they carry different risks.

Third, enforce least privilege. Agents and MCP servers should receive only the minimum access needed for the workflow. Avoid wildcard scopes, omnibus permissions, shared credentials, and broad service accounts.

Fourth, isolate execution. Local servers should run with tight file and network permissions. Hosted servers should go through gateways with TLS, logging, and allowlisted outbound calls.

Fifth, require consent and approval for risky actions. Reading a public document is not the same as writing to a database, deleting a resource, modifying code, or changing infrastructure.

Sixth, monitor behavior continuously. Log tool calls, parameters, outputs, user approvals, failed attempts, policy blocks, and metadata changes. Watch for unusual tool invocation patterns, excessive retries, data movement anomalies, and cost spikes.

Seventh, detect drift. MCP tools can change over time. Tool descriptions, schemas, permissions, and server behavior should be monitored for unexpected changes after approval.

Eighth, prepare incident response. Teams need a fast way to disable an MCP server, revoke credentials, block a tool, roll back a connector version, inspect recent activity, and determine whether data was exposed.

Governance has to be operational, not ceremonial.

## What SREs Should Monitor

SREs will need MCP-specific telemetry because traditional service metrics are not enough.

For MCP-connected agents, useful metrics include:

- Tool-call volume
- Tool-call failure rate
- Unauthorized tool-call attempts
- Policy-blocked actions
- High-risk action requests
- Human approval rate
- Tool metadata changes
- Unexpected tool selection rate
- Data access volume by agent
- Token and cost usage by tool
- Latency by MCP server
- Error rate by connector
- Retry loops
- Credential failures
- Scope elevation events

These metrics should feed into dashboards, alerts, and incident reviews.

For example, a sudden spike in failed tool calls may indicate a broken connector. A spike in policy-blocked requests may indicate prompt injection attempts. A sudden increase in data retrieval may suggest exfiltration risk. A tool metadata change may suggest a rug pull. A cost spike may indicate an agent loop.

MCP is not just an integration layer. It is an operational surface.

If it is part of production workflows, it needs SLOs, alerts, ownership, and post-incident analysis.

## Treat MCP as Privileged Infrastructure

The biggest mistake enterprises can make is treating MCP as a developer convenience layer.

It is not just a convenience layer.

It is a privileged integration layer between AI agents and enterprise systems.

That means MCP should be managed like any other critical infrastructure component. Platform teams should provide approved connectors, standard deployment paths, secure defaults, monitoring, identity integration, policy enforcement, and incident controls.

Security teams should threat model MCP servers and agent-tool workflows. SREs should define reliability and safety metrics. Developers should have a golden path that makes the secure option the easiest option.

This is how enterprises avoid the worst outcome: hundreds of MCP servers quietly connecting AI agents to sensitive systems with unclear ownership, inconsistent permissions, and no central visibility.

## The Bottom Line

MCP may become one of the most important standards in enterprise AI because it solves a real problem: connecting AI agents to the tools and data they need to be useful.

But the same thing that makes MCP powerful also makes it risky.

It gives AI systems reach. And reach must be governed.

For SREs and platform engineers, the message is clear: MCP is not just another integration protocol. It is the emerging control plane for how AI agents interact with enterprise systems.

That means MCP security has to be designed before the agent reaches production, not after the first incident.

The future of enterprise AI will not be decided only by who has the best model. It will be decided by who can safely connect that model to real systems.

MCP is the bridge. Now enterprises have to secure the bridge.
