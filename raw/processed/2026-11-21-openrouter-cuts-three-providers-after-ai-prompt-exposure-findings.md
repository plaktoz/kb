---
source_url: https://www.unite.ai/openrouter-cuts-three-providers-after-ai-prompt-exposure-findings
author: Miles Okada
date: 2026-11-21
---

# OpenRouter Cuts Three Providers After AI Prompt Exposure Findings

OpenRouter announced on November 22, 2026, that it had off-boarded three inference providers and removed 125 endpoints from eligibility for Zero Data Retention (ZDR), a setting under which prompts and responses are not stored. It also notified all potentially affected customers.

The findings did not show a breach or unauthorized access of OpenRouter itself, the company said. The removals covered providers flagged by researchers and other endpoints withdrawn as a precaution. Its public list links notices from Novita, Phala and Together AI, but does not identify them as the three off-boarded providers; not all affected providers have published notices.

## Canary Tests Revealed Routing and Retention Gaps

In research published on November 19, 2026, Dragos described submitting approximately two million prompts containing unique URLs and canary credentials to widely used AI services from July through November 2026, then monitoring subsequent activity. The tests produced evidence that data from at least three AI providers was exposed, that marketplace resellers viewed and retained customer prompts through standard logging, and that some providers appeared to disregard privacy settings or published policies.

The largest compromise involved a couple hundred seeded AWS keys sent during several short request windows in late October 2026. Some keys came from requests rejected before a model ran, which Dragos interpreted as evidence that copying occurred when requests first reached the provider rather than during model processing. The bait keys were subsequently used for tens of thousands of AWS API calls.

The routing findings matter because every organization along a multi-hop path can see the complete prompt and response. Dragos traced about 2,000 inference routes: several hundred included an unidentified system, while in a handful, a company absent from the advertised path fetched the test image. Dragos also reported that one unnamed Chinese AI lab's systems fetched secret URLs from more than half of prompts sent to its models between July and October 2026, including roughly two-thirds marked no-data-collection or ZDR.

## Provider Notices Describe Separate Incidents

Novita's privacy notice said a routing configuration issue broadened an API forwarding path intended for specific customers, sending some MiniMax requests to MiniMax's official API rather than Novita-hosted infrastructure. Requests made directly through Novita or routed through OpenRouter between May 28, 2026, and November 11, 2026, may have had their contents accessed or retained by a third party. Novita suspended the affected models. The researcher observed accesses to test URLs and hostnames but no use of AWS test-key markers; automated content review may have been involved, an assessment Novita is checking with MiniMax.

Phala's preliminary incident report, published on November 10, 2026, advised users whose DeepSeek V4 Flash 0731 requests were routed to Phala by OpenRouter from 00:00 UTC on October 21, 2026, to 05:35 UTC on November 8, 2026, to treat the contents as exposed and rotate included secrets. The attacker chained a legacy internet-facing service with management interfaces that trusted loopback access without independently authenticating callers. A similar access pattern gave the attacker control of an inference VM, making in-flight request data visible during processing.

Phala confirmed canary misuse only for requests sent on October 21-22, 2026, but kept the wider window because the tests sampled requests and could not reveal every possible data-access event. Containment was completed on November 8, 2026, and a full-platform audit found no evidence of compromise affecting other models or products. The investigation and verification of remediation remain active, with a full root-cause analysis planned.

Together AI disclosed on November 21, 2026 that an unauthorized party downloaded stored prompt samples after an AI coding agent committed a credential for a private Hugging Face repository to the public xorl GitHub repository. Collected for routine software testing with authorization, the samples came from MiniMax M3, GLM-5.2 and Kimi K2.6 requests, primarily on June 24, 2026, July 4, 2026, July 8, 2026, and July 14, 2026. The party searched the samples for credentials to other services and tested them, including five Dragos canary credentials.

Together said it has not identified additional prompt leakage beyond the incident, but its review of affected prompt contents and determination of which customers require direct notification remain ongoing. Its changes include scoped or short-lived credentials, credential checks on all pull requests, ZDR by default for new accounts and updated development rules for AI coding agents.

## Verification Before ZDR Restoration

OpenRouter is adapting the researchers' testing approach for ongoing checks and technically verifying network paths to identify requests and responses that may be forwarded to third parties. Removed endpoints will require appropriate assurances and validation before regaining ZDR eligibility.

Novita is verifying the affected processing paths, pursuing deletion of any retained data with MiniMax and improving Partner API labeling and disclosures of relevant providers' retention policies. For routed inference, the consequence is that ZDR eligibility now rests on validation of the actual request path alongside provider assurances. OpenRouter's continuing checks leave one central operational question: whether ongoing testing can expose undisclosed forwarding and retention failures before they affect customer data.
