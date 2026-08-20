# Research: OWASP LLM Top 10
*Generated: 2026-08-20 | Scope: Comprehensive overview of the OWASP LLM Top 10 — what each vulnerability is, how it works technically, how to defend against it, how to audit for it, and how a well-secured AI chatbot implements each control in practice.*

## Research Outline

1. OWASP LLM Top 10 — Background & Full List
2. Input-side attacks — Prompt Injection (LLM01) and Training Data Poisoning (LLM03/LLM05:2026)
3. Output & trust failures — Insecure Output Handling (LLM02), Sensitive Information Disclosure (LLM06), and Overreliance (LLM09)
4. System & infrastructure risks — Excessive Agency (LLM08), Insecure Plugin Design (LLM07), Supply Chain (LLM05), Model DoS (LLM04), Model Theft (LLM10)
5. Practical defense & audit checklist
6. Reference architecture: a well-secured AI chatbot

---

## OWASP LLM Top 10 — Background & Full List

### OWASP Top 10 for LLM Applications (Project Page)

- **Source**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **Summary**: The OWASP LLM Top 10 project was started in 2023 by a small group responding to an urgent AI security gap. It has since grown to 600+ contributors across 18+ countries with ~8,000 community members, and is now governed under the broader OWASP GenAI Security Project. The project publishes ranked lists of the most critical security risks in LLM applications. The most current release is the 2026 edition (published August 4, 2026), superseding the widely-cited v1.1 list.
- **Relevance**: This is the canonical starting point — provides the authoritative source, project history, and full vulnerability list for understanding scope and context.

### OWASP GenAI LLM Top 10 — 2026 Edition (GitHub)

- **Source**: https://github.com/GenAI-Security-Project/GenAI-LLM-Top10
- **Summary**: The 2026 edition restructures the list significantly. New entries include "Hidden Context Exposure" (LLM08:2026) and "Unbounded Consumption" replacing the earlier Model DoS framing. Supply Chain moves up in priority, and the scope expands to cover agentic AI systems. The 2026 list: LLM01 Prompt Injection · LLM02 Sensitive Information Disclosure · LLM03 Excessive Agency · LLM04 Supply Chain · LLM05 Data and Model Poisoning · LLM06 Unbounded Consumption · LLM07 Misinformation · LLM08 Hidden Context Exposure · LLM09 Vector and Embedding Weaknesses · LLM10 Improper Output Handling.
- **Relevance**: Covers the current (2026) state of the list and shows how the threat model has evolved toward agentic systems.

**Version comparison at a glance:**

| v1.1 (2023-25) | 2026 Edition |
|---|---|
| LLM01: Prompt Injection | LLM01: Prompt Injection |
| LLM02: Insecure Output Handling | LLM10: Improper Output Handling |
| LLM03: Training Data Poisoning | LLM05: Data and Model Poisoning |
| LLM04: Model Denial of Service | LLM06: Unbounded Consumption |
| LLM05: Supply Chain Vulnerabilities | LLM04: Supply Chain |
| LLM06: Sensitive Information Disclosure | LLM02: Sensitive Information Disclosure |
| LLM07: Insecure Plugin Design | (merged into Excessive Agency / LLM03) |
| LLM08: Excessive Agency | LLM03: Excessive Agency |
| LLM09: Overreliance | LLM07: Misinformation |
| LLM10: Model Theft | (absorbed into Supply Chain / access controls) |
| *(new)* | LLM08: Hidden Context Exposure |
| *(new)* | LLM09: Vector and Embedding Weaknesses |

---

## Input-side Attacks — Prompt Injection & Training Data Poisoning

### LLM01: Prompt Injection — OWASP Official Description

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM01_PromptInjection.md
- **Summary**: Prompt injection occurs when attackers manipulate an LLM through crafted inputs, causing it to execute attacker intentions. **Direct injection** overwrites or extracts the system prompt (jailbreaking). **Indirect injection** embeds malicious instructions in external content (web pages, documents) the LLM reads during retrieval. Attack scenarios range from triggering RCE via a support chatbot plugin, to silently deleting emails, to exfiltrating session history via image URL. Mitigations: least-privilege API access, human-in-the-loop for privileged actions, content segregation (ChatML-style), treating LLM as untrusted actor, input/output monitoring.
- **Relevance**: Prompt injection is the #1 ranked vulnerability in every OWASP LLM edition — it is the root cause that enables most other attacks when combined with agentic systems.

### Prompt Injection Types and Mechanics

- **Source**: https://learnprompting.org/docs/prompt_hacking/injection
- **Summary**: AI models process all text as a single continuous stream with no built-in trust hierarchy — there is no hardware or protocol separation between developer instructions and user input. This is the fundamental architecture problem. Four attack types: (1) **Direct** — attacker text overrides system instructions; (2) **Indirect** — malicious instructions in content the AI reads (RAG documents, web pages); (3) **Code injection** — AI tricked into generating/executing malicious code; (4) **Recursive** — output from one LLM contains injection targeting a second. Notable real incidents: remoteli.io Twitter bot hijacked, API key extraction, system prompt extraction via "repeat your instructions."
- **Relevance**: Explains the root-cause architecture problem and provides a taxonomy of attack types essential for building a complete defensive mental model.

### LLM03: Training Data Poisoning

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM03_TrainingDataPoisoning.md
- **Summary**: Training data poisoning is an integrity attack on pre-training, fine-tuning, or embedding data to introduce vulnerabilities, backdoors, or biases. External data sources are highest risk because the model builder lacks control over their content. Attack vectors include competitors injecting false information into public datasets, insider threats contaminating fine-tuning data, and prompt injection being used as a data collection mechanism (malicious inputs during training get embedded into the model itself). Defenses: ML-BOM (Machine Learning Bill of Materials), DVC for dataset version control, input filters with statistical outlier detection, federated learning, red team exercises throughout the model lifecycle.
- **Relevance**: Particularly important for teams fine-tuning models on proprietary data or using RAG pipelines that ingest external content — the pipeline becomes an attack surface.

---

## Output & Trust Failures — Insecure Output Handling, Sensitive Disclosure, Overreliance

### LLM02: Insecure Output Handling

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM02_InsecureOutputHandling.md
- **Summary**: Insufficient validation of LLM-generated output before it reaches downstream systems enables attackers who control inputs to gain "indirect access to additional functionality." Attack scenarios: (1) passing unvalidated LLM output to an admin plugin triggers unintended actions like shutdowns; (2) a summarizer tool encodes sensitive data and exfiltrates it to an attacker-controlled server; (3) a chat-based SQL interface executes DROP TABLE without scrutiny; (4) unsanitized LLM output with JavaScript rendered in a browser causes XSS. Mitigation: treat model output as untrusted user input (zero-trust), follow OWASP ASVS guidelines, encode output before rendering, validate at every integration layer.
- **Relevance**: Directly affects any chatbot that renders output in a browser or passes LLM responses to downstream systems — XSS and code execution via LLM output are underappreciated risks.

### LLM06: Sensitive Information Disclosure

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM06_SensitiveInformationDisclosure.md
- **Summary**: LLMs can inadvertently reveal confidential data, proprietary algorithms, or PII through their outputs. This includes: one user receiving another user's data in normal operation, adversarial prompt crafting to bypass filters and extract PII, and PII leaking into training data. The key insight is that LLMs do not have true access control for their learned knowledge — information baked in during training or fine-tuning can surface unpredictably. Mitigations: sanitize data before training pipelines, least-privilege fine-tuning (do not train on data that a lower-privileged user could see), enforce access controls on external data sources (RAG), and acknowledge that system-prompt restrictions "may not always be honored."
- **Relevance**: Critical for any chatbot with access to multi-tenant data or fine-tuned on customer-specific content — data isolation is harder than it appears when the knowledge is embedded in model weights.

### LLM09: Overreliance (Hallucination Risk)

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM09_Overreliance.md
- **Summary**: LLMs generate authoritative-sounding but factually incorrect content. Attack surface: a bad actor feeds an LLM-powered news outlet misleading data, spreading disinformation at scale; an LLM recommends a non-existent code library, and a developer installs a malicious lookalike package ("package hallucination" attack); AI-generated code with insecure defaults gets merged unreviewed. Mitigations: cross-check outputs against trusted external sources, voting/self-consistency across multiple model calls, chain-of-thought prompting, task decomposition across multiple agents, clear user-facing labeling of AI-generated content, and mandatory human review in security-critical workflows.
- **Relevance**: Package hallucination is a real supply-chain attack vector for dev-facing chatbots; overreliance on AI-generated code without security review has led to production vulnerabilities.

---

## System & Infrastructure Risks

### LLM08: Excessive Agency

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM08_ExcessiveAgency.md
- **Summary**: Excessive agency results from three root causes operating independently or together: (1) **Excessive functionality** — tools with more capabilities than needed; (2) **Excessive permissions** — overly broad access rights to downstream systems; (3) **Excessive autonomy** — high-impact actions execute without human approval. The canonical attack: a malicious incoming email triggers indirect prompt injection on an email-reading assistant, causing it to send spam from the user's account. Impact spans confidentiality, integrity, and availability depending on which systems the LLM can reach. Mitigations: minimum necessary tools and permissions, avoid open-ended functions (prefer granular over shell/URL-fetch), require human approval for high-impact actions, rate-limiting, and comprehensive audit logging.
- **Relevance**: As chatbots gain tool use (web browsing, code execution, email/calendar access), excessive agency becomes the primary blast radius multiplier for injection attacks.

### LLM07: Insecure Plugin Design

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM07_InsecurePluginDesign.md
- **Summary**: LLM plugins accept free-text inputs with minimal validation and typically lack cross-plugin authorization tracking. Five attack scenarios: (1) SSRF via redirecting a URL-accepting plugin to an attacker server; (2) unvalidated free-form input for recon and code execution; (3) vector store connection string abuse to pivot databases; (4) SQL injection via raw WHERE clause filtering; (5) indirect prompt injection exploiting weak access controls in a code management plugin. Mitigations: strict parameterized inputs with type/range validation, OWASP ASVS throughout CI/CD (SAST/DAST/IAST), least-privilege access, OAuth2/API keys for auth, explicit user confirmation for sensitive actions, apply OWASP API Security Top 10 to every plugin endpoint.
- **Relevance**: Every tool or plugin connected to an LLM is an API — and an API that receives LLM output as input is vulnerable to every classical web vulnerability amplified by injection.

### LLM05: Supply Chain Vulnerabilities

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM05_SupplyChainVulnerabilities.md
- **Summary**: LLM supply chains span Python dependencies, pre-trained models from public hubs (Hugging Face), plugins, third-party APIs, and training datasets — all are potential compromise vectors. Real-world incidents cited: a vulnerable Python library exploited in the first OpenAI data breach; a PyPi package poisoned to exfiltrate model dev environment data; a backdoored Hugging Face model spreading misinformation. Insider threats from suppliers and T&C changes that quietly opt users into training data collection are also in scope. Mitigations: vet all data suppliers and their privacy policies, SBOM for component inventory, model/code signing when sourcing external models, anomaly detection on supplied models, and continuous monitoring for unauthorized plugins.
- **Relevance**: Using a pre-trained model or third-party LLM API means inheriting that provider's security posture — supply chain hygiene is non-negotiable in production.

### LLM04: Model Denial of Service

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM04_ModelDoS.md
- **Summary**: Attackers consume excessive LLM compute resources, degrading service quality and inflating operating costs. The context window is the primary attack surface — inputs crafted near the context limit, recursive expansion triggers, or floods of complex requests. Scenarios include: automated scripts bombarding the endpoint, webpages that trigger many additional requests during browsing, variable-length input floods near the context limit, and leaked admin tokens enabling abnormal request volumes. Mitigations: input size validation, per-request resource caps, API rate limiting per user/IP, cap on queued actions triggered by LLM outputs, and strict context window size enforcement.
- **Relevance**: Unlike traditional DoS, LLM DoS is economically painful (cost per token) and stealthy — degraded performance may go undetected while costs accumulate.

### LLM10: Model Theft

- **Source**: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM10_ModelTheft.md
- **Summary**: Model theft covers unauthorized access and exfiltration of proprietary model weights, parameters, or architecture. Stolen models enable competitors to launch equivalent services or conduct gray-box adversarial attacks. Five vectors: infrastructure breach (misconfigured storage), insider threat, systematic API query extraction (building a shadow model from outputs), supply chain failure, and side-channel attacks bypassing input filters to harvest weights. Mitigations: RBAC + least privilege for model repositories, network restriction on LLM access to internal resources, centralized model registry with governance, API rate limiting with DLP pattern matching, model watermarking, adversarial robustness training to detect extraction queries, and continuous audit logging.
- **Relevance**: If you've invested in fine-tuning or proprietary model development, the model itself is a high-value IP asset requiring asset-grade protection.

---

## Practical Defense & Audit Checklist

### LLM Red Teaming Methodology (promptfoo)

- **Source**: https://www.promptfoo.dev/docs/red-team/
- **Summary**: LLM red teaming systematically probes AI systems with adversarial inputs before deployment to quantify vulnerability risk. It covers both model-layer threats (prompt injections, jailbreaks, hallucinations, PII leakage from training data) and application-layer threats (indirect injection, PII via RAG, unauthorized tool access, exfiltration). The methodology: (1) define strategy and vulnerability priorities; (2) generate adversarial inputs with automated tools plus human creativity; (3) execute in a production-like environment; (4) analyze results with deterministic and model-graded metrics; (5) remediate and re-test. Can be integrated into CI/CD for continuous testing.
- **Relevance**: Provides the structured testing process for auditing an LLM application against all OWASP LLM Top 10 categories before and after deployment.

### Layered Defense Architecture Against LLM Vulnerabilities (NVIDIA)

- **Source**: https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/
- **Summary**: NVIDIA's AI Red Team proposes a 5-layer defense model. Layer 1: input validation — detect injection patterns before they reach the LLM. Layer 2: trust boundary enforcement — treat every entity that contributed text to the prompt as a potential attacker; apply the lowest privilege level across all contributors. Layer 3: output sanitization — all LLM output is potentially malicious before passing downstream. Layer 4: hardened external service integration — strict parameterization of API calls, least-privilege service contexts, type/content checking. Layer 5: architectural minimalism — avoid connecting LLMs to external resources; restrict plugins to minimum functionality; multi-service chains require rigorous security review.
- **Relevance**: Translates the OWASP vulnerability list into a concrete, layered defensive architecture applicable to any LLM-based system.

### Cloudflare AI Gateway — Infrastructure-Level Controls

- **Source**: https://developers.cloudflare.com/ai-gateway/
- **Summary**: AI Gateway provides a centralized control plane between your application and LLM providers (OpenAI, Anthropic, Gemini, etc.). Key security features: rate limiting per user/IP to prevent DoS and cost abuse; comprehensive request logging for anomaly detection; caching to reduce upstream exposure; request retry and fallback routing for resilience; analytics for token usage and cost monitoring. Activated with minimal code changes by routing API calls through the Gateway endpoint.
- **Relevance**: Addresses LLM04 (DoS/Unbounded Consumption) and LLM10 (audit logging) at the infrastructure layer — a practical, low-friction first security control to add to any LLM chatbot in production.

**Audit Checklist — mapped to OWASP LLM Top 10:**

| # | Check | OWASP Category |
|---|---|---|
| 1 | System prompt is separated from user input; untrusted content in distinct delimiters | LLM01 |
| 2 | All LLM output is treated as untrusted before rendering or passing downstream | LLM02/LLM10:2026 |
| 3 | Training and fine-tuning data sources are vetted, versioned (DVC), and anomaly-scanned | LLM03/LLM05:2026 |
| 4 | Input size limits enforced; rate limiting per user/IP at API gateway layer | LLM04/LLM06:2026 |
| 5 | SBOM maintained; all model dependencies and plugins are pinned and signed | LLM05/LLM04:2026 |
| 6 | PII/sensitive data scrubbed from training pipelines; access-controlled in RAG | LLM06/LLM02:2026 |
| 7 | All plugins use parameterized inputs; SQL/SSRF protections applied | LLM07 |
| 8 | LLM tools are least-privilege; high-impact actions require human confirmation | LLM08/LLM03:2026 |
| 9 | AI outputs in decision-critical workflows have human review / source verification | LLM09/LLM07:2026 |
| 10 | Model repos RBAC-gated; API call patterns monitored for extraction attempts | LLM10 |
| 11 | Red team exercises conducted pre-deploy and in CI/CD pipeline | All |
| 12 | Comprehensive audit logging of all LLM requests and tool/plugin invocations | All |

---

## Reference Architecture: A Well-Secured AI Chatbot

### Safety System Messages — Microsoft Azure Foundry

- **Source**: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/system-message
- **Summary**: A safety system message (metaprompt) is one layer in a broader defense stack — not a complete solution on its own, but a critical one. Best practice structure: (1) Role and task definition; (2) Scope and boundaries (explicit "do not" instructions); (3) Safety guidelines (prohibited content categories, PII handling); (4) Tool and data constraints. Effective techniques: use "always/never" directives, conditional if-then logic, examples of harmful vs. benign requests, and second-person framing ("You are..."). Key limitation: adversarial prompting can bypass system messages; they must be paired with output filtering, content classifiers, and access controls.
- **Relevance**: Provides the concrete system-prompt patterns and design principles that form the first line of defense in any production AI chatbot.

---

### End-to-End Secure Chatbot Architecture

A "perfect" AI chatbot implementation maps every OWASP LLM control to a concrete architectural layer:

```
User Input
    │
    ▼
[Layer 1: Input Validation & Rate Limiting]
    • Size limits enforced (context window DoS prevention — LLM04)
    • Rate limiting per user/IP (LLM04)
    • PII detection and redaction before LLM (LLM06)
    • Injection pattern detection (LLM01)
    │
    ▼
[Layer 2: LLM Core with Hardened System Prompt]
    • System prompt defines role, scope, explicit refusal guidelines (LLM01)
    • User message wrapped in untrusted-content delimiters (e.g., <user_input>...</user_input>) (LLM01)
    • External/retrieved content explicitly labeled as untrusted in prompt (LLM01 indirect)
    • Model not granted access beyond what the task requires (LLM08)
    │
    ▼
[Layer 3: Output Validation & Sanitization]
    • All LLM output treated as untrusted before rendering (LLM02/LLM10:2026)
    • HTML encoding for browser output (XSS prevention)
    • No raw LLM text passed to SQL, shell, or system API calls
    • Content safety classifier applied to outputs before delivery (LLM09/LLM07:2026)
    │
    ▼
[Layer 4: Tool / Plugin Execution (if agentic)]
    • Each tool is least-privilege: only the access its function requires (LLM07/LLM08)
    • All tool inputs are strictly parameterized — no raw LLM text as SQL/shell (LLM07)
    • High-impact actions (send email, write file, call external API) require user confirmation (LLM08)
    • Tool calls are logged with full context (LLM08)
    │
    ▼
[Layer 5: Infrastructure & Observability]
    • AI Gateway (e.g., Cloudflare) for unified rate limiting, logging, fallback (LLM04/LLM10)
    • Model repository RBAC-gated; API call volume monitored for extraction patterns (LLM10)
    • All dependencies pinned, SBOM maintained, plugin integrity verified (LLM05)
    • Red team tests run in CI/CD pipeline pre-deploy (All)
    │
    ▼
User Response (with AI-generated content labeled)
```

**Key chatbot-specific implementation decisions:**

| Concern | Secure Implementation |
|---|---|
| System prompt confidentiality | Expect it can be extracted; treat it as defense-in-depth, not a secret |
| RAG document injection | Wrap retrieved docs in `<document untrusted="true">` delimiters; instruct model to treat as data not instructions |
| Multi-turn memory | Audit what's stored; never store raw injected content as "trusted memory" |
| Tool authorization | OAuth2 scopes scoped to minimum; re-prompt user before irreversible actions |
| Fine-tuning data | Scrub PII; use DVC; audit for poisoning; least-privilege principle (low-priv content only) |
| Cost controls | Per-user token budgets; input/output limits; monitor for runaway loops |
| Logging | Log all prompts and responses (with PII masking); retain for anomaly detection |

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://owasp.org/www-project-top-10-for-large-language-model-applications/
- https://github.com/GenAI-Security-Project/GenAI-LLM-Top10
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM01_PromptInjection.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM02_InsecureOutputHandling.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM03_TrainingDataPoisoning.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM04_ModelDoS.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM05_SupplyChainVulnerabilities.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM06_SensitiveInformationDisclosure.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM07_InsecurePluginDesign.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM08_ExcessiveAgency.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM09_Overreliance.md
- https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM10_ModelTheft.md
- https://learnprompting.org/docs/prompt_hacking/injection
- https://www.promptfoo.dev/docs/red-team/
- https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/
- https://developers.cloudflare.com/ai-gateway/
- https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/system-message
