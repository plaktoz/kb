# Lesson Plan: Blue Team vs Red Team in Cybersecurity

*Source: `research/blue-vs-red-team/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations
*Establish the mental models first — who each team is, what they're trying to achieve, and the two shared frameworks (Kill Chain and ATT&CK) that give both sides a common language.*

### Lesson 1: The Adversarial Mindset — What Red Teams Do and Why
**File:** `lessons/0001-red-team-role.html`
**Key concepts:** simulated adversary · TTPs · credential theft · lateral movement · engagement mandate
**Source:** CrowdStrike (crowdstrike.com/cybersecurity-101/red-team-vs-blue-team/) + OffSec (offsec.com/blog/red-team-vs-blue-team/) — red team is a structured adversary simulation, not uncontrolled hacking; follows MITRE ATT&CK TTPs
**Skill:** Write a 3-sentence "attacker brief" for a fictional e-commerce company — state what the red team would target, why, and what success looks like
**Reference doc:** `reference/red-team-overview.html`

### Lesson 2: The Defender's Mandate — What Blue Teams Do and the 1-10-60 Rule
**File:** `lessons/0002-blue-team-role.html`
**Key concepts:** SOC analyst · detection · incident response · 1-10-60 rule · always-on operations
**Source:** CrowdStrike (crowdstrike.com/cybersecurity-101/red-team-vs-blue-team/) — detect in <1 min, assess in <10 min, eject in <1 hour; blue team is continuous, not project-based
**Skill:** Given a fictional alert ("unusual outbound DNS queries at 3am"), write a triage response: what you'd detect, assess, and do within each time window
**Reference doc:** `reference/blue-team-overview.html`

### Lesson 3: The Cyber Kill Chain — 7 Phases as a Shared Attack/Defense Map
**File:** `lessons/0003-cyber-kill-chain.html`
**Key concepts:** reconnaissance · weaponization · delivery · exploitation · installation · C2 · actions on objectives · APT
**Source:** Lockheed Martin Cyber Kill Chain (lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — every adversary must complete all 7 phases; defenders can disrupt the chain at any phase
**Skill:** Take the 2020 SolarWinds breach summary (provided in the lesson) and map each attacker action to a Kill Chain phase
**Reference doc:** `reference/cyber-kill-chain.html`

### Lesson 4: MITRE ATT&CK — The Shared Vocabulary of Attack and Defense
**File:** `lessons/0004-mitre-attack.html`
**Key concepts:** tactics · techniques · sub-techniques · ATT&CK IDs · Enterprise matrix · 15 tactics
**Source:** MITRE ATT&CK (attack.mitre.org) — 15 Enterprise tactics from Reconnaissance through Impact; both teams use the same technique IDs to align attack and detection
**Skill:** Look up two ATT&CK techniques (T1059.001 and T1003.001) and write one detection hypothesis for each: what log event or behavioral signal would reveal this technique?
**Reference doc:** `reference/mitre-attack-primer.html`

---

## Module 2 — Toolchains
*Concrete tools ground abstract concepts. Understanding what each tool does (and why it exists) is required to design LLM automation that replicates or augments these capabilities.*

### Lesson 5: Reconnaissance Tools — Nmap and Network Discovery
**File:** `lessons/0005-nmap-recon.html`
**Key concepts:** port scanning · service fingerprinting · OS detection · attack surface · Zenmap · Ncat
**Source:** Nmap (nmap.org) — standard open-source tool for network discovery; used in the recon phase by red teams and for asset inventory by blue teams
**Skill:** Write a Nmap command to discover all open ports and services on a /24 subnet, then explain what each flag in your command does
**Reference doc:** `reference/recon-tools.html`

### Lesson 6: Exploitation Tools — Metasploit and the Payload Lifecycle
**File:** `lessons/0006-metasploit-exploitation.html`
**Key concepts:** exploit modules · Meterpreter · payload delivery · post-exploitation · C2 sessions · evasion
**Source:** Metasploit (metasploit.com) — world's most-used pentest framework; 400+ exploit modules, Meterpreter-based sessions, evasion primitives; integrates with Rapid7 InsightVM/InsightIDR
**Skill:** Describe in pseudocode the 4-step workflow a red teamer follows when using Metasploit against a known CVE — from module selection through establishing a session
**Reference doc:** `reference/exploitation-tools.html`

### Lesson 7: Web Application Testing — Burp Suite and OWASP WSTG
**File:** `lessons/0007-burp-suite-owasp.html`
**Key concepts:** proxy interception · automated DAST · XSS · SQL injection · CSRF · WSTG test IDs · structured assessment
**Source:** Burp Suite (portswigger.net/burp) + OWASP WSTG (owasp.org/www-project-web-security-testing-guide/) — leading web pentesting platform; WSTG provides versioned test IDs for structured, reproducible assessments
**Skill:** Match 5 OWASP vulnerability classes to the Burp Suite tool best suited to find them (Scanner, Repeater, Intruder, Proxy, Decoder) and write one sentence explaining each pairing
**Reference doc:** `reference/web-testing-tools.html`

### Lesson 8: Blue Team Detection Platform — Elastic SIEM and the Agentic SOC
**File:** `lessons/0008-elastic-siem.html`
**Key concepts:** SIEM · XDR · detection rules · alert triage · human-on-the-loop · agentic investigation
**Source:** Elastic Security (elastic.co/security) — 1,300+ open detection rules; AI agents investigate and draft response plans for analyst approval; model-agnostic (Anthropic, OpenAI, Gemini, on-prem)
**Skill:** Given 3 fictional alert descriptions, write a triage decision for each (benign / malicious / investigate further) and explain your reasoning as if briefing a senior analyst
**Reference doc:** `reference/blue-team-platforms.html`

---

## Module 3 — Overlap and Purple Teaming
*The real security posture of an organization emerges from red/blue collaboration — not from either team working alone. This module makes that loop concrete and quantifiable.*

### Lesson 9: Purple Teaming — Attacking and Defending Together
**File:** `lessons/0009-purple-teaming.html`
**Key concepts:** purple team · tabletop simulation · adversary emulation · real-time sharing · after-action review · continuous engagement
**Source:** CrowdStrike Purple Teaming (crowdstrike.com/cybersecurity-101/purple-teaming/) — unified team attacks and defends simultaneously; shares findings in real time; includes tabletop, emulation, and live combined exercises
**Skill:** Design a 30-minute purple team tabletop exercise for a fictional fintech company — write the attacker's scenario (2 sentences) and 3 detection checkpoints the blue team would verify in real time
**Reference doc:** *(extend reference/red-team-overview.html)*

### Lesson 10: ATT&CK Coverage Mapping — Quantifying the Gap
**File:** `lessons/0010-attack-coverage-mapping.html`
**Key concepts:** coverage assessment · detection gaps · T1059.001 · T1003.001 · measurable posture · log sources · ATT&CK navigator
**Source:** MITRE ATT&CK (attack.mitre.org) — ATT&CK IDs let both teams convert "we found X" and "we detect Y" into a shared, measurable coverage matrix; gaps become an actionable list
**Skill:** Fill in a coverage assessment table for 5 ATT&CK techniques: technique ID, name, whether your fictional org detects it (yes/no/partial), and the log source that would confirm detection
**Reference doc:** *(extend reference/mitre-attack-primer.html)*

---

## Module 4 — LLM Security Automation
*Ground all prior knowledge in the build goal — how LLMs are being applied to red and blue tasks today, and what architecture patterns enable self-serve security tooling.*

### Lesson 11: AI Red Teaming — Adversarial Techniques Against AI Systems
**File:** `lessons/0011-ai-red-teaming.html`
**Key concepts:** prompt injection · training data extraction · adversarial examples · data poisoning · model exfiltration · AI-specific expertise
**Source:** Google AI Red Team (blog.google/.../googles-ai-red-team-the-ethical-hackers-making-ai-safer/) — AI red teaming extends traditional methods with AI-specific attack classes; standard controls still help, but AI expertise is required as complexity grows
**Skill:** Write a brief attacker brief for a fictional LLM-powered customer support chatbot — what would you try to extract, which Google AI Red Team technique applies, and what mitigation would stop it?
**Reference doc:** `reference/llm-security-overview.html`

### Lesson 12: PentestGPT — Autonomous LLM-Driven Penetration Testing
**File:** `lessons/0012-pentestgpt.html`
**Key concepts:** Pentesting Task Tree · cooperating LLM sessions · reasoning/generation/parsing roles · 86.5% benchmark · recon → exploitation pipeline
**Source:** PentestGPT USENIX 2024 (github.com/GreyDGL/PentestGPT) — multi-LLM agent maintains a task tree across recon, exploitation, and reporting; 86.5% success rate on 104-challenge December 2025 benchmark
**Skill:** Sketch a Pentesting Task Tree (plain text bullets) for a web application assessment — assign specific sub-tasks to the reasoning LLM, generation LLM, and parsing LLM respectively
**Reference doc:** *(extend reference/llm-security-overview.html)*

### Lesson 13: PyRIT Architecture — The Attacker + Scorer + Memory Pattern
**File:** `lessons/0013-pyrit-architecture.html`
**Key concepts:** prompt expansion · adaptive scoring · LLM classifier · memory layer · augmentation vs replacement · attacker/scorer pattern
**Source:** Microsoft PyRIT (microsoft.com blog, Feb 2024) — open-source framework; attacker LLM expands prompts, scorer LLM evaluates responses, memory layer enables multi-turn adaptation; compresses weeks of manual work into hours
**Skill:** Design a PyRIT-style architecture (ASCII diagram or labeled list) for a self-serve SQL injection checker — name the target system, the attacker LLM's job, the scorer's evaluation criteria, and what the memory layer tracks
**Reference doc:** `reference/llm-red-team-architecture.html`

### Lesson 14: Agentic SOC — LLM-Assisted Blue Team Automation
**File:** `lessons/0014-agentic-soc.html`
**Key concepts:** agentic alert triage · human-on-the-loop · model-agnostic · detection rule corpus · response plan drafting · scale without burnout
**Source:** Elastic Security agentic SOC (elastic.co/security) — AI agents investigate, correlate, and propose response plans; analysts approve; model-agnostic architecture supports Claude, OpenAI, Gemini, or local models
**Skill:** Write a system prompt for a Claude-powered alert triage agent — specify what role it plays, what inputs it receives (alert type, log excerpt, severity), and what structured output format it should produce
**Reference doc:** *(extend reference/llm-red-team-architecture.html)*

---

## Suggested Teaching Order

Follow the module order: foundations first (lessons 1–4), then tools (5–8), then collaboration (9–10), then build (11–14). The Kill Chain (lesson 3) and ATT&CK (lesson 4) are load-bearing — lessons 9, 10, 12, and 13 all reference them. Do not skip ahead.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/red-team-overview.html` | Red team role, mandate, engagement lifecycle, key practitioners |
| `reference/blue-team-overview.html` | Blue team role, SOC structure, 1-10-60 rule, core activities |
| `reference/cyber-kill-chain.html` | All 7 Kill Chain phases with descriptions and detection opportunities per phase |
| `reference/mitre-attack-primer.html` | ATT&CK structure (tactics → techniques → sub-techniques), how to read technique IDs, Enterprise matrix overview |
| `reference/recon-tools.html` | Nmap flag reference, Zenmap, Ncat, Ndiff — quick-reference for recon tools |
| `reference/exploitation-tools.html` | Metasploit module types, Meterpreter commands, payload lifecycle reference |
| `reference/web-testing-tools.html` | Burp Suite tool index (Proxy, Scanner, Repeater, Intruder, Decoder) + OWASP WSTG category reference |
| `reference/blue-team-platforms.html` | SIEM vs XDR vs EDR comparison; Elastic detection rule anatomy |
| `reference/llm-security-overview.html` | Google AI Red Team attack taxonomy; PentestGPT architecture diagram; PyRIT component reference |
| `reference/llm-red-team-architecture.html` | Attacker+Scorer+Memory pattern; agentic SOC architecture; self-serve tool design checklist |
