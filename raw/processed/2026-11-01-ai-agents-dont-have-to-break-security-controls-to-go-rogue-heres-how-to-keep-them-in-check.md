---
source_url: https://venturebeat.com/security/ai-agents-dont-have-to-break-security-controls-to-go-rogue-heres-how-to-keep-them-in-check
author: Badal Bhushan
date: 2026-11-01
---

# AI agents don't have to break security controls to go rogue. Here's how to keep them in check

During recent cybersecurity evaluations, the UK AI Security Institute (AISI) ran a cybersecurity challenge 122 times across several models. In 10 of those runs, AI agents executed 19 unsanctioned real-world actions on the live internet — ranging from attempting a malicious code contribution on a public open-source repository, to launching a social engineering campaign targeting a maintainer for approval.

The critical security observation is that this did not require escaping the sandbox.

The evaluation environment did exactly what it was built to do. The problem was far simpler and much harder to catch: The agent's available capability was simply broader than its intended authority.

Compare that to OpenAI's August 26 postmortem on its research evaluations, where models actively circumvented isolation controls, exploited shared infrastructure, and accessed third-party systems. Or Hugging Face's incident disclosure documenting node-level escalation, credential harvesting, and lateral movement across internal clusters. And, Anthropic reported a related boundary failure when Claude models reached the internet from third-party evaluation setups and gained unauthorized access to real systems.

We are looking at two fundamentally different failure modes across the enterprise AI stack:

Containment failure (Hugging Face / OpenAI): The agent expands its effective access by actively defeating security controls.

Authority failure (AISI): The agent uses already-available capabilities to act far beyond its assigned task, all without breaking containment.

The sandbox held, but the agent still went rogue. So what happens when containment works, authentication succeeds, and an autonomous actor still exceeds the authority humans intended to grant?

In my work designing identity and authorization architectures for enterprise agentic systems, the hardest problem isn't figuring out who the agent is. It's preserving the actual authorization intent behind an action once execution starts hopping across multiple agents, workloads, and API tools. Identity answers who the agent is. Delegation explains why it's actually authorized to take a specific action right now.

Much of the enterprise response has leaned heavily on assigning stronger agent identities, refining model guardrails, and hardening container sandboxes. Those are necessary baseline controls, but none of them solve the context problem. Even action-level authorization remains incomplete unless every downstream execution can prove its lineage back to the originating delegation.

In a standard enterprise architecture, execution flows through a multi-hop chain:

Human or System Principal → Application → AI Agent → Runtime Workload → Executable Tool → Target Resource

As execution moves through that chain, authorization context can be lost as execution crosses identity-access management (IAM), workload, and service boundaries. Authentication establishes actor identity, and an access token represents granted authority for a specific scope. But neither proves that a downstream tool call actually aligns with what the originating human delegated.

Authority must attenuate as it moves down the chain — it must get narrower rather than broader at each hop, and it must never silently expand.

Evaluating whether an agent can call a specific API misses the broader architectural requirement. A true runtime authorization policy must evaluate the entire execution picture:

Principal + Agent + Workload + Task + Action + Resource + Context + Delegation Lineage

We need to stop asking enterprise security teams, "Can this agent call this API?" and start asking, "Can you prove who authorized this action, and what verifiable delegation gives this agent the authority to perform it right now?"

Fortunately, standards bodies and runtime frameworks are starting to align around this architectural gap:

NIST's August 27 analysis on agentic identity points toward mechanisms for preserving and attenuating authorization context, emphasizing short-lived, audience-restricted credentials and emerging Transaction Tokens.

The OWASP Agent Control Standard complements this by providing standardized middleware hooks to govern agents dynamically at runtime.

The OpenID Foundation's AuthZEN specification provides a standardized Authorization API between Policy Enforcement Points (PEPs) and Policy Decision Points (PDPs), while the IETF's WIMSE working group is defining workload identity credentials and authentication mechanisms for distributed environments.

NIST points toward mechanisms for preserving delegated authorization context. OWASP provides runtime enforcement hooks. AuthZEN standardizes the authorization decision interface. Enterprise architects need to connect those pieces into verifiable authorization lineage.

To operationalize this inside an enterprise engineering stack, five core principles should anchor the architecture:

Preserve actor distinctness. Maintain clear separation between the human principal, the autonomous agent, and the executing workload identity in every authorization log. Never collapse them into a single, generic service account.

Attenuate authority at every hop. Exchange broad upstream tokens for short-lived, highly scoped downstream credentials. A child agent or tool must never inherit or obtain more authority than its parent was granted.

Bind policy decisions to transaction context. Evaluate authorization by combining actor identities, current task context, requested action, target resource, environmental risk, and delegation lineage at the exact moment of execution through an externalized policy decision and enforcement layer.

Isolate reusable credentials from the reasoning layer. Never pass long-lived secrets or refresh tokens directly to an LLM. Use a trusted gateway, broker, or sidecar to manage runtime authorization and inject short-lived credentials after policy evaluation succeeds.

Maintain reconstructable authorization lineage. Ensure SOC and incident-response teams can trace a transaction backward from the target resource all the way to the human principal to understand precisely which policy decision permitted the action.

We need to stop spending all our engineering cycles trying to prompt-engineer an autonomous model into never crossing a line. Instead, let's architect our enterprise infrastructure so that crossing a line simply confers no authority.

Let the model decide what it wants to do. Let the authorization infrastructure decide what it is allowed to do. And let the delegation chain prove why it was authorized in the first place.
