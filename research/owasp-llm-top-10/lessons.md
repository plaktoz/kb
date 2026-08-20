# Lesson Plan: OWASP LLM Top 10

*Source: `research/owasp-llm-top-10/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations
*Establishes why LLM security is structurally different from web security before naming any specific vulnerability — the mental model that makes the rest of the course stick.*

### Lesson 1: Why LLM Security Is Different
**File:** `lessons/0001-why-llm-security-is-different.html`
**Key concepts:** trust hierarchy absence · control/data plane confusion · the OWASP LLM Top 10 project
**Source paper:** https://owasp.org/www-project-top-10-for-large-language-model-applications/ — 600+ contributors, 18+ countries; https://learnprompting.org/docs/prompt_hacking/injection — "AI models process all text as a single continuous stream with no built-in trust hierarchy"
**Skill:** Draw a simple diagram of a classic web request (browser → server) and an LLM request (user → LLM), labelling where the trust boundary sits in each — explain in 2–3 sentences why the LLM diagram has no equivalent boundary
**Reference doc:** `reference/owasp-llm-project-overview.html`

### Lesson 2: The Full Attack Surface — All 10 Vulnerabilities at a Glance
**File:** `lessons/0002-attack-surface-all-10.html`
**Key concepts:** v1.1 list · 2026 list · vulnerability categories (input / output / infrastructure) · threat model evolution toward agentic systems
**Source paper:** https://github.com/GenAI-Security-Project/GenAI-LLM-Top10 — 2026 edition restructures list; adds Hidden Context Exposure and Vector & Embedding Weaknesses for agentic systems
**Skill:** Using the v1.1 vs 2026 comparison table, categorise each v1.1 vulnerability as "input-side", "output-side", or "infrastructure" — then identify which 2026 additions are driven by the shift to agentic systems
**Reference doc:** `reference/llm-top10-comparison-table.html`

---

## Module 2 — Input-Side Attacks
*Covers the attacks that enter through the prompt — the #1 ranked vulnerability class in every OWASP LLM edition, and the root-cause enabler for most agentic exploits.*

### Lesson 3: Prompt Injection — Direct Attacks & Jailbreaks (LLM01)
**File:** `lessons/0003-prompt-injection-direct.html`
**Key concepts:** direct prompt injection · jailbreaking · system prompt extraction · ChatML-style content segregation
**Source paper:** https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM01_PromptInjection.md — attack scenarios: support chatbot RCE, system prompt extraction via "repeat your instructions"
**Skill:** Write a test prompt that attempts to extract a hypothetical system prompt from a chatbot, then write the corresponding defensive system-prompt instruction that should resist it — explain why neither is fully reliable on its own
**Reference doc:** `reference/prompt-injection-defense-patterns.html`

### Lesson 4: Indirect Prompt Injection — The RAG & Agentic Threat (LLM01 indirect)
**File:** `lessons/0004-indirect-prompt-injection.html`
**Key concepts:** indirect injection · RAG pipeline attack surface · recursive injection · document delimiter pattern
**Source paper:** https://learnprompting.org/docs/prompt_hacking/injection — indirect type: "malicious instructions hidden in external content the AI reads"; recursive type: "output from one LLM contains injection instructions targeting a second LLM"; real incident: remoteli.io Twitter bot hijacked through injected tweets
**Skill:** Given a RAG chatbot that retrieves web pages and uses their content to answer user questions, write the system-prompt instruction block that wraps retrieved documents as untrusted — and describe one attack scenario that would still succeed despite those instructions
**Reference doc:** `reference/prompt-injection-defense-patterns.html` *(extend)*

### Lesson 5: Training Data Poisoning (LLM03 / LLM05:2026)
**File:** `lessons/0005-training-data-poisoning.html`
**Key concepts:** integrity attack · ML-BOM · DVC · fine-tuning risk · backdoor injection
**Source paper:** https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM03_TrainingDataPoisoning.md — "malicious client input used during training may become embedded in the model itself"; external data sources are highest risk
**Skill:** For a hypothetical chatbot fine-tuned on customer support tickets, list three sources of training data and for each: (a) the poisoning vector, (b) the defense, and (c) whether that defense catches the attack before or after the model is trained
**Reference doc:** `reference/data-pipeline-security.html`

---

## Module 3 — Output, Trust & Infrastructure Vulnerabilities
*Works through the remaining 7 vulnerability classes, grouped by whether they affect outputs, trust assumptions, or the broader infrastructure the LLM sits inside.*

### Lesson 6: Insecure Output Handling (LLM02 / LLM10:2026)
**File:** `lessons/0006-insecure-output-handling.html`
**Key concepts:** zero-trust output · XSS via LLM · SQL injection via LLM · OWASP ASVS · output encoding
**Source paper:** https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM02_InsecureOutputHandling.md — "unsanitized LLM output containing JavaScript rendered in a browser, causing XSS attacks"; "chat-based SQL interface executes DROP TABLE"
**Skill:** Review this pseudo-code snippet — `res.send(llm.complete(userInput))` — and rewrite it with proper output handling: HTML encoding, content type declaration, and a note on why zero-trust applies here
**Reference doc:** `reference/output-sanitization-checklist.html`

### Lesson 7: Sensitive Information Disclosure (LLM06 / LLM02:2026)
**File:** `lessons/0007-sensitive-information-disclosure.html`
**Key concepts:** weight-embedded knowledge · PII leakage · multi-tenant isolation · least-privilege fine-tuning · RAG access controls
**Source paper:** https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM06_SensitiveInformationDisclosure.md — "LLMs do not have true access control for their learned knowledge — information baked in during training can surface unpredictably"; least-privilege fine-tuning principle
**Skill:** For a multi-tenant SaaS chatbot where Tenant A and Tenant B both contributed data to a shared fine-tuned model, describe two attack paths by which Tenant A's data could surface to Tenant B — and the architectural change that closes each path
**Reference doc:** `reference/data-pipeline-security.html` *(extend)*

### Lesson 8: Overreliance & Hallucination Risks (LLM09 / LLM07:2026)
**File:** `lessons/0008-overreliance-hallucination.html`
**Key concepts:** hallucination · package hallucination attack · AI-generated code review · self-consistency · human-in-the-loop
**Source paper:** https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM09_Overreliance.md — "LLM recommends a non-existent code library and a developer installs a malicious lookalike package"; AI-generated code with insecure defaults merged unreviewed
**Skill:** Write a brief policy (3–5 bullet points) for a dev team that uses an LLM coding assistant — specifying when human review is mandatory, how to verify suggested package names, and how to handle security-sensitive code suggestions
**Reference doc:** `reference/human-in-the-loop-patterns.html`

### Lesson 9: Excessive Agency & Insecure Plugin Design (LLM08 + LLM07)
**File:** `lessons/0009-excessive-agency-plugin-design.html`
**Key concepts:** least-privilege tools · excessive functionality/permissions/autonomy · SSRF via plugin · SQL injection via plugin · OAuth2 scoping · human confirmation gate
**Source paper:** https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM08_ExcessiveAgency.md — canonical attack: malicious email → indirect injection → email assistant sends spam; https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM07_InsecurePluginDesign.md — five attack scenarios including SSRF and SQL injection via plugin
**Skill:** Design the tool/plugin contract for an email-reading chatbot: list the exact permissions it needs (read-only vs. send), identify which action must require human confirmation, and write the OAuth2 scope string that enforces this
**Reference doc:** `reference/plugin-security-checklist.html`

### Lesson 10: Supply Chain, Model DoS & Model Theft (LLM05 + LLM04 + LLM10)
**File:** `lessons/0010-supply-chain-dos-theft.html`
**Key concepts:** SBOM · model signing · context window DoS · cost-based DoS · model watermarking · API extraction attack · RBAC for model repos
**Source paper:** https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM05_SupplyChainVulnerabilities.md — PyPi package poisoned to exfiltrate model dev data; backdoored Hugging Face model; https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM04_ModelDoS.md — context window as attack surface; https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM10_ModelTheft.md — systematic API query extraction to build a shadow model
**Skill:** For a production chatbot that uses a third-party pre-trained model loaded from Hugging Face and a Python SDK, list the three highest-risk supply chain components and the specific control you would apply to each before deploying to production
**Reference doc:** `reference/infrastructure-security-checklist.html`

---

## Module 4 — Building Secure LLM Applications
*Synthesises all prior knowledge into actionable workflows — how to test, how to structure defenses, and how a "perfect" chatbot implementation actually looks.*

### Lesson 11: Red Teaming & Audit Methodology
**File:** `lessons/0011-red-teaming-audit.html`
**Key concepts:** red teaming · adversarial inputs · CI/CD security integration · model-layer vs. application-layer threats · promptfoo
**Source paper:** https://www.promptfoo.dev/docs/red-team/ — 5-step methodology: define strategy → generate adversarial inputs → execute in production-like environment → analyze results → remediate and re-test; covers both model-layer and application-layer threats
**Skill:** Using the 12-item OWASP audit checklist from the report, select 3 items and for each: write one specific adversarial test input (or test scenario) you would use to verify the control is working
**Reference doc:** `reference/owasp-audit-checklist.html`

### Lesson 12: Layered Defense Architecture
**File:** `lessons/0012-layered-defense-architecture.html`
**Key concepts:** 5-layer defense model · input validation layer · trust boundary enforcement · output sanitization · hardened service integration · architectural minimalism
**Source paper:** https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/ — NVIDIA AI Red Team 5-layer model; "control and data planes are not separable when working with LLMs — every LLM output must be treated as hostile territory"; https://developers.cloudflare.com/ai-gateway/ — AI Gateway as infrastructure-layer control plane
**Skill:** Draw or describe all 5 layers of the defense model for a simple chatbot that retrieves documents (RAG) and has one tool (web search) — for each layer, name the specific threat it addresses and one concrete implementation step
**Reference doc:** `reference/layered-defense-reference.html`

### Lesson 13: Reference Architecture — Building a Secure AI Chatbot
**File:** `lessons/0013-secure-chatbot-reference-architecture.html`
**Key concepts:** safety system message · metaprompt patterns · untrusted-content delimiters · tool authorization · multi-turn memory security · cost controls · AI Gateway
**Source paper:** https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/system-message — safety system message patterns (always/never directives, conditional logic, example-based technique, scope and boundaries); "adversarial prompting can bypass system messages — they must be paired with output filtering, content classifiers, and access controls"
**Skill:** Write a complete safety system message for a customer support chatbot that: (a) defines role and scope, (b) wraps untrusted user input with delimiters, (c) includes explicit refusal boundaries, and (d) includes one conditional safety rule — then identify which OWASP LLM vulnerability each section of the system message addresses
**Reference doc:** `reference/secure-chatbot-patterns.html`

---

## Suggested Teaching Order

Follow modules in sequence (1 → 2 → 3 → 4). Module 1 is essential groundwork — skipping it means later vulnerabilities feel like an arbitrary list rather than manifestations of the same root architecture problem. Within Module 3, the output-handling lessons (6–8) build toward the agency/plugin lesson (9), which builds toward the infrastructure lesson (10): each layer of the defense stack maps to the prior lesson's attack surface.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/owasp-llm-project-overview.html` | Project history, governance, v1.1 full list with one-line descriptions |
| `reference/llm-top10-comparison-table.html` | v1.1 vs 2026 full comparison with migration notes |
| `reference/prompt-injection-defense-patterns.html` | Direct/indirect/recursive taxonomy, ChatML delimiters, RAG wrapping patterns, known bypass techniques |
| `reference/data-pipeline-security.html` | ML-BOM, DVC, fine-tuning least-privilege, PII scrubbing, multi-tenant isolation |
| `reference/output-sanitization-checklist.html` | Output encoding, ASVS mapping, zero-trust output patterns, XSS/SQLi via LLM |
| `reference/human-in-the-loop-patterns.html` | When to require human review, self-consistency techniques, AI content labeling |
| `reference/plugin-security-checklist.html` | Parameterized inputs, OAuth2 scoping, SSRF prevention, SAST/DAST in CI/CD |
| `reference/infrastructure-security-checklist.html` | SBOM, model signing, RBAC for model repos, rate limiting, watermarking, DLP |
| `reference/owasp-audit-checklist.html` | Full 12-item checklist with test scenarios per item |
| `reference/layered-defense-reference.html` | NVIDIA 5-layer model with implementation examples and tool mappings |
| `reference/secure-chatbot-patterns.html` | Safety system message templates, end-to-end architecture diagram, key chatbot decisions table |
