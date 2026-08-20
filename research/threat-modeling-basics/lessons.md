# Lesson Plan: Threat Modeling Basics for Web App Developers

*Source: `research/threat-modeling-basics/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations
*Establish the "what" and "why" before touching any framework or tool — junior developers need the mental model first.*

### Lesson 1: What is Threat Modeling and Why Should Developers Care?
**File:** `lessons/0001-what-is-threat-modeling.html`
**Key concepts:** threat modeling definition · security by design · shift-left security · adversarial thinking
**Source:** https://owasp.org/www-community/Threat_Modeling — defines threat modeling as finding "threats and mitigations within the context of protecting something of value"; emphasises that a threat model is a structured representation of all information affecting an application's security.
**Skill:** Write a one-paragraph answer to "Why should I, as a junior web developer, care about threat modeling?" — in your own words, no jargon, as if explaining to a non-technical teammate.
**Reference doc:** `reference/key-definitions.html`

### Lesson 2: The Four Core Questions Every Threat Model Must Answer
**File:** `lessons/0002-four-core-questions.html`
**Key concepts:** four-question framework · what are we building · what can go wrong · what will we do · did we do a good job · Threat Modeling Manifesto values
**Source:** https://www.threatmodelingmanifesto.org/ — articulates the four questions and the manifesto values (finding real issues over checkbox compliance; a journey over a one-time snapshot); warns against anti-patterns like the "hero threat modeler."
**Skill:** For a login feature on a web app, briefly answer all four questions in bullet points. Focus on the spirit — don't worry about correctness yet.
**Reference doc:** `reference/four-questions-cheatsheet.html`

### Lesson 3: Threat Modeling in the SDLC — When and How Often
**File:** `lessons/0003-threat-modeling-in-sdlc.html`
**Key concepts:** SDLC integration · continuous threat modeling · agile sprint sessions · "little and often" · security as a team sport
**Source:** https://martinfowler.com/articles/agile-threat-modelling.html — advocates 15–30 minute sessions tied to sprint work rather than big-bang workshops; describes threat modeling as "continuous integration for security"; shows how a cross-functional team (developer, product owner, tester) contributes distinct value.
**Skill:** Map the five Microsoft SDL steps (define requirements → diagram → identify → mitigate → validate) onto a sprint cycle. Sketch where each step would land across a two-week sprint.
**Reference doc:** `reference/sdlc-integration-guide.html`

---

## Module 2 — Frameworks
*Introduce the threat identification toolbox in order of importance for a junior web dev: STRIDE first (most commonly used), then PASTA and alternatives.*

### Lesson 4: STRIDE — The Developer's Primary Threat Framework
**File:** `lessons/0004-stride-overview.html`
**Key concepts:** STRIDE acronym · Spoofing · Tampering · Repudiation · Information Disclosure · Denial of Service · Elevation of Privilege · security properties violated
**Source:** https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats — defines each STRIDE category with concrete examples (e.g. Spoofing = using another user's credentials; Tampering = malicious modification of data in transit; Repudiation = users denying actions when audit trails are absent).
**Skill:** Fill in a blank STRIDE table for a "user submits a contact form" feature: for each letter, write one specific threat that could apply to this flow.
**Reference doc:** `reference/stride-quick-reference.html`

### Lesson 5: STRIDE in Action — Walking Through a Web App DFD
**File:** `lessons/0005-stride-in-action.html`
**Key concepts:** data flow diagram · trust boundaries · STRIDE per element · threat per data flow · concrete threat statements
**Source:** https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started — walks through a worked DFD (user → web server → database), shows how the Microsoft TMT auto-generates STRIDE threats, and demonstrates that a tester (Ashish) finding gaps a developer (Ricardo) missed confirms threat modeling is a team activity.
**Skill:** Draw a simple DFD for a web app feature of your choice (user → API → database is fine). Apply STRIDE to at least one data flow arrow and write two specific threat statements (e.g. "SQL injection from internet" not "tampering").
**Reference doc:** *(extend existing reference/stride-quick-reference.html)*

### Lesson 6: PASTA — The Risk-Centric Alternative
**File:** `lessons/0006-pasta-framework.html`
**Key concepts:** PASTA · Process for Attack Simulation and Threat Analysis · 7 stages · risk-centric · attack simulation · when to use PASTA vs STRIDE
**Source:** https://www.imperva.com/learn/application-security/threat-modeling/ — describes PASTA as a seven-stage framework: (1) define objectives → (2) technical scope → (3) application decomposition → (4) threat identification → (5) vulnerability analysis → (6) attack simulation → (7) risk analysis. Positions it as risk-centric vs. STRIDE's design-centric approach.
**Skill:** Compare STRIDE and PASTA side-by-side in a two-column table. For each, write: target user, best phase to apply, and one weakness or limitation.
**Reference doc:** `reference/framework-comparison.html`

### Lesson 7: LINDDUN, CVSS, and Choosing the Right Framework
**File:** `lessons/0007-linddun-cvss-framework-choice.html`
**Key concepts:** LINDDUN · privacy threats · CVSS scoring · low/medium/high/critical · framework selection criteria · OCTAVE · VAST
**Source:** https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html — lists LINDDUN (privacy-focused), OCTAVE (risk/org focus), VAST (DevOps-oriented), and STRIDE + MITRE ATT&CK pairing. Also: https://www.imperva.com/learn/application-security/threat-modeling/ — CVSS as a numerical scoring system for communicating severity.
**Skill:** You are building a web app that collects users' email addresses and browsing history. Which framework would you start with — STRIDE or LINDDUN — and why? Write 3–5 sentences defending your choice.
**Reference doc:** *(extend existing reference/framework-comparison.html)*

---

## Module 3 — The Process
*Step-by-step execution: how to actually run a threat modeling session on a real web app feature.*

### Lesson 8: Step 1 — Building Your Data Flow Diagram
**File:** `lessons/0008-building-a-dfd.html`
**Key concepts:** DFD elements · processes · data stores · external entities · data flows · trust boundaries · assets
**Source:** https://martinfowler.com/articles/agile-threat-modelling.html — describes what to include: components (services, DBs, UIs), users (internal, external, privileged), data flows with directional arrows, trust boundaries, and assets (anything whose loss causes harm). Also: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started — shows DFD stencil conventions (square = external entity, circle = process, parallel lines = data store, dotted red line = trust boundary).
**Skill:** Draw a DFD for a simple user registration flow: browser → registration API → user database → email service. Label each element with the correct DFD symbol type, add one trust boundary, and identify two assets.
**Reference doc:** `reference/dfd-symbol-guide.html`

### Lesson 9: Step 2 — Identifying and Capturing Threats
**File:** `lessons/0009-identifying-threats.html`
**Key concepts:** threat identification · one threat per sticky note · specific vs vague threats · STRIDE per data flow · brainstorming vs structured analysis · threat statement format
**Source:** https://martinfowler.com/articles/agile-threat-modelling.html — shows how to apply STRIDE to each data flow arrow, writing one specific threat per sticky note ("SQL injection from internet" not "tampering"). Also https://owasp.org/www-community/Threat_Modeling — notes that threat identification can use Kill Chains or Attack Trees as alternatives to STRIDE.
**Skill:** Take your DFD from Lesson 8 and write at least five specific threat statements — one per STRIDE category — placed on the relevant data flow arrow. Each statement must name the attacker action and the target component.
**Reference doc:** *(extend existing reference/stride-quick-reference.html)*

### Lesson 10: Step 3 — Prioritizing Threats and the Four Response Strategies
**File:** `lessons/0010-prioritizing-and-responding.html`
**Key concepts:** likelihood × impact matrix · threat prioritisation · mitigate · eliminate · transfer · accept · CVSS scores · response documentation
**Source:** https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html — describes ranking by likelihood × impact, the four response options (mitigate / eliminate / transfer / accept), and that mitigations must be actionable and testable using OWASP ASVS or MITRE CWE as references. Also: https://www.imperva.com/learn/application-security/threat-modeling/ — CVSS scoring for communicating severity.
**Skill:** Take three threats from Lesson 9. For each: assign a likelihood (1–3) and impact (1–3), compute a score, choose a response strategy (mitigate / eliminate / transfer / accept), and write one sentence on what that response looks like in practice.
**Reference doc:** `reference/prioritization-matrix.html`

---

## Module 4 — Outputs and Tooling
*What a finished threat model looks like and how to produce one with free tools.*

### Lesson 11: What a Finished Threat Model Looks Like
**File:** `lessons/0011-threat-model-outputs.html`
**Key concepts:** DFD artifact · ranked threat list · threat register · response strategy per threat · mitigation requirements · attack surface map · validation checklist
**Source:** https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html — five canonical outputs: DFDs, ranked threat list, response strategies, actionable mitigation requirements, formal documentation. Also: https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html — attack surface map as a companion output; the two inform each other continuously.
**Skill:** Using all the work from Lessons 8–10, assemble a mini threat model document: DFD sketch, a threat register table (threat | likelihood | impact | score | response | mitigation note), and a one-sentence validation sign-off.
**Reference doc:** `reference/threat-register-template.html`

### Lesson 12: OWASP Threat Dragon and Microsoft TMT — Getting Started
**File:** `lessons/0012-tooling-threat-dragon-mstmt.html`
**Key concepts:** OWASP Threat Dragon · Microsoft Threat Modeling Tool · rule engine · auto-generated threats · report export · JSON threat model files · when to use which tool
**Source:** https://owasp.org/www-project-threat-dragon/ — open-source tool with a rule engine, STRIDE/LINDDUN support, printable reports, JSON output, available as browser app at threatdragon.com. Also: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started — free Windows desktop tool designed for non-security experts, auto-generates STRIDE threats from DFDs, exports full reports.
**Skill:** Open the OWASP Threat Dragon demo at https://www.threatdragon.com or download Microsoft TMT. Recreate your DFD from Lesson 8 in the tool. Screenshot or describe what threats the rule engine auto-generated. Did it catch anything you missed?
**Reference doc:** `reference/tool-setup-guide.html`

---

## Suggested Teaching Order

Work through modules in sequence: Foundations first to build vocabulary and mindset, then Frameworks to load the threat identification toolkit, then Process to apply it hands-on, and finally Outputs & Tooling to produce shareable deliverables. Each lesson's skill exercise feeds the next — by Lesson 11 you have all the pieces needed to assemble a complete mini threat model.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/key-definitions.html` | Glossary: threat, vulnerability, risk, asset, trust boundary, DFD, mitigation |
| `reference/four-questions-cheatsheet.html` | The four core questions with example answers for a web app login feature |
| `reference/sdlc-integration-guide.html` | Where threat modeling fits in each SDLC phase; sprint cadence suggestions |
| `reference/stride-quick-reference.html` | STRIDE table: letter, threat type, security property violated, web app example |
| `reference/framework-comparison.html` | STRIDE vs PASTA vs LINDDUN vs CVSS comparison table |
| `reference/dfd-symbol-guide.html` | DFD element types with symbols, examples, and what to ask about each |
| `reference/prioritization-matrix.html` | Likelihood × impact scoring grid; four response strategies with examples |
| `reference/threat-register-template.html` | Blank threat register table with column definitions and a filled example row |
| `reference/tool-setup-guide.html` | Step-by-step: open Threat Dragon demo; install Microsoft TMT; first DFD |
