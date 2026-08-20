# Research: Threat Modeling Basics — What It Is, How It's Done, and What It Produces
*Generated: 2026-08-20 | Scope: Threat modeling fundamentals for a junior developer — covering concepts, frameworks (STRIDE, PASTA, etc.), the end-to-end process, outputs, and tooling, grounded in a web app development context.*

## Research Outline

1. What is threat modeling and why does it matter?
2. Main frameworks and methodologies — STRIDE, PASTA, LINDDUN, DREAD, and Attack Trees
3. The threat modeling process step-by-step in a web app context
4. Outputs and documentation — what a threat model looks like
5. Practical tooling and resources for developers

---

## 1. What is threat modeling and why does it matter?

### OWASP Threat Modeling Cheat Sheet

- **Source**: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- **Summary**: A comprehensive reference on threat modeling as "a structured, repeatable process used to gain actionable insights into the security characteristics of a particular system." It covers the four core questions, the STRIDE framework, the process steps (system modeling → threat identification → response → validation), and an extensive list of tools. It also addresses cloud-specific adaptations and organizational challenges for development teams.
- **Relevance**: The definitive beginner-friendly reference that covers all five research sections in one document — ideal as the backbone of study notes.

### OWASP Threat Modeling — Community Overview

- **Source**: https://owasp.org/www-community/Threat_Modeling
- **Summary**: Defines threat modeling as finding "threats and mitigations within the context of protecting something of value." A threat model is "a structured representation of all the information that affects the security of an application." Stresses that threat modeling should be applied continuously throughout the SDLC, starting high-level and refining as the system grows.
- **Relevance**: Establishes the foundational "why" — threat modeling gives teams "a clear line of sight across a project that justifies security efforts."

### The Threat Modeling Manifesto

- **Source**: https://www.threatmodelingmanifesto.org/
- **Summary**: A community-authored values document that defines the four questions every threat model must answer: What are we working on? What can go wrong? What are we going to do about it? Did we do a good enough job? It articulates values (finding real design issues over checkbox compliance; people over process) and warns against anti-patterns like relying on one "hero" threat modeler or doing it as a one-time snapshot.
- **Relevance**: Sets the mindset for approaching threat modeling as a continuous, collaborative discipline rather than a compliance checklist.

---

## 2. Main frameworks and methodologies — STRIDE, PASTA, LINDDUN, DREAD, and Attack Trees

### Microsoft SDL — STRIDE Framework Reference (Azure Docs)

- **Source**: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
- **Summary**: Defines each STRIDE category with concrete examples: **Spoofing** (using another user's credentials), **Tampering** (malicious modification of data in transit or at rest), **Repudiation** (users denying actions when audit trails are absent), **Information Disclosure** (unauthorized access to files or data in transit), **Denial of Service** (making a web server unavailable), **Elevation of Privilege** (an unprivileged user gaining admin-level access). Each category maps to a security property that is being violated.
- **Relevance**: Provides the clearest definitions of STRIDE — the most widely-used framework for web app threat modeling.

### Imperva — Threat Modeling Methodologies Overview

- **Source**: https://www.imperva.com/learn/application-security/threat-modeling/
- **Summary**: Covers multiple frameworks side by side. STRIDE is Microsoft-originated and applied during early design. PASTA (Process for Attack Simulation and Threat Analysis) is a risk-centric 7-stage framework: (1) define objectives → (2) technical scope → (3) application decomposition → (4) threat identification → (5) vulnerability analysis → (6) attack simulation → (7) risk analysis. TRIKE is risk-based using DFDs. CVSS produces a numerical severity score (low / medium / high / critical). Best practices include multidisciplinary teams, DFDs, and SDLC integration.
- **Relevance**: Provides the clearest comparison of STRIDE vs. PASTA and introduces CVSS for scoring threat severity — essential for understanding which framework to pick and when.

### OWASP Threat Modeling Cheat Sheet — Frameworks Section

- **Source**: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- **Summary**: Lists STRIDE, PASTA, LINDDUN (privacy-focused threat framework), OCTAVE (risk-based, organisational focus), and VAST (DevOps-oriented, scalable). Notes that STRIDE pairs well with MITRE ATT&CK for deeper analysis. Threats are ranked by likelihood × impact after identification.
- **Relevance**: Introduces LINDDUN as the go-to framework when privacy threats (GDPR, data minimisation) are the primary concern — relevant for any web app handling personal data.

---

## 3. The threat modeling process step-by-step in a web app context

### Martin Fowler — Agile Threat Modelling

- **Source**: https://martinfowler.com/articles/agile-threat-modelling.html
- **Summary**: Describes a three-activity loop suited for development teams: (1) **Explain & Explore** — build a shared low-level data flow diagram showing components, users, data flows, trust boundaries, and assets; (2) **Identify Threats** — apply STRIDE to each data flow systematically, writing one threat per sticky note (e.g. "SQL injection from internet"); (3) **Prioritize & Fix** — translate findings into security acceptance criteria, user stories, or investigation spikes in the backlog. Advocates 15–30 minute focused sessions tied to current sprint work rather than exhaustive one-off workshops.
- **Relevance**: The most practical, developer-friendly process description — maps directly onto how a junior dev would run threat modeling during web app feature development.

### Microsoft SDL — Five-Step Threat Modeling Process

- **Source**: https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling
- **Summary**: Defines five sequential steps: (1) Define security requirements, (2) Create an application diagram, (3) Identify threats, (4) Mitigate threats, (5) Validate that mitigations are in place. Emphasises the process is iterative — embedded in routine development so teams can "progressively refine" their models over time.
- **Relevance**: Provides the canonical step-by-step framing from the organisation that created STRIDE, making it a trustworthy process reference.

### Microsoft Threat Modeling Tool — Getting Started Guide

- **Source**: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started
- **Summary**: Walks through a concrete web app threat modeling session with a developer (Cristina), program manager (Ricardo), and tester (Ashish). Shows how a DFD is built (user → web server → database), how the tool auto-generates STRIDE threats, and how each threat is reviewed, prioritised, mitigated, and tracked. Demonstrates that a tester's scepticism (Ashish finding gaps Ricardo missed) adds value — confirming threat modeling is a team activity, not a solo exercise.
- **Relevance**: Best concrete worked example of threat modeling a web app end-to-end — useful as a mental template for applying the process to your own project.

---

## 4. Outputs and documentation — what a threat model looks like

### OWASP Threat Modeling Cheat Sheet — Outputs Section

- **Source**: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- **Summary**: Documents five canonical outputs: (1) Data Flow Diagrams (DFDs) that map trust boundaries, data flows, processes, and external entities; (2) a ranked threat list scored by likelihood × impact; (3) documented response strategies per threat (mitigate / eliminate / transfer / accept); (4) actionable, testable mitigation requirements referencing OWASP ASVS or MITRE CWE; (5) formal documentation stored accessibly for stakeholders. Validation questions are also listed to confirm the model is complete.
- **Relevance**: The clearest enumeration of what a finished threat model looks like as a set of deliverables — essential for knowing what "done" means.

### Microsoft Threat Modeling Tool — Getting Started Guide (Reports)

- **Source**: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started
- **Summary**: The tool generates a full report summarising: all identified threats, their category (STRIDE), priority, status (Not Started / Needs Investigation / Mitigated / Not Applicable), and mitigation notes. Reports can be exported and shared. Threat models are saved as files that can be stored in source control or shared via OneDrive for team review and sign-off.
- **Relevance**: Shows the concrete format of a threat model report — gives a junior dev a clear picture of what to produce and share.

### OWASP / Attack Surface Analysis Cheat Sheet

- **Source**: https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html
- **Summary**: Describes how to map all points where an attacker could enter a system — covering UI forms, APIs, HTTP headers, files, databases, and runtime arguments. The attack surface map is a companion output to the threat model, and the two are mutually reinforcing: "changes to the Attack Surface should trigger threat modeling, and threat modeling helps you to understand the Attack Surface."
- **Relevance**: Explains the attack surface map as a key sub-output of the threat modeling process — developers working on web apps need to understand this to scope what gets modeled.

---

## 5. Practical tooling and resources for developers

### OWASP Threat Dragon

- **Source**: https://owasp.org/www-project-threat-dragon/
- **Summary**: An open-source web and desktop application for creating threat model diagrams. Features a rule engine that auto-generates threats and mitigations from DFDs, supports multiple frameworks (STRIDE, LINDDUN, CIA, DIE, PLOT4ai), and produces printable reports and JSON threat model files. Runs as a Docker image, desktop installer (Linux/macOS/Windows), or browser-based app. Public demo at `threatdragon.com`.
- **Relevance**: The best free, open-source starting tool for a junior developer — visual, beginner-friendly, and covers STRIDE out of the box.

### Microsoft Threat Modeling Tool

- **Source**: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started
- **Summary**: A free Windows desktop tool designed "with non-security experts in mind." Users draw a DFD using built-in stencils, and the tool auto-generates a STRIDE threat list. Templates exist for generic SDL models and Azure-specific architectures. Threat status, priority, and mitigations can be tracked and exported as a full report.
- **Relevance**: Industry-standard free tool with extensive documentation — the easiest way to run a structured threat modeling session on a new web app without prior security expertise.

### Varonis — Threat Modeling Best Practices

- **Source**: https://www.varonis.com/blog/threat-modeling
- **Summary**: Frames threat modeling in four stages (planning, identifying, prevention/mitigation, validation/remediation) and identifies common mistakes to avoid: treating pen tests or code reviews as substitutes, delaying until the team grows, and skipping threat modeling before major deployments. Notes that framework selection depends on industry, team maturity, resource availability, and risk appetite.
- **Relevance**: Useful for understanding common pitfalls and how to pick the right framework for your team's maturity level.

### Imperva — Practical Tooling Summary

- **Source**: https://www.imperva.com/learn/application-security/threat-modeling/
- **Summary**: Recommends using DFDs to visualise vulnerability points, integrating threat modeling into the SDLC from the start, using multidisciplinary teams (security, dev, architecture, business), and leveraging current threat intelligence alongside automated tooling. CVSS is highlighted as a practical scoring system for communicating threat severity to non-security stakeholders.
- **Relevance**: Provides the broader ecosystem view — useful for understanding where threat modeling sits relative to CVSS scoring, penetration testing, and vulnerability management.

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- https://www.threatmodelingmanifesto.org/
- https://owasp.org/www-community/Threat_Modeling
- https://martinfowler.com/articles/agile-threat-modelling.html
- https://owasp.org/www-project-threat-dragon/
- https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started
- https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
- https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling
- https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html
- https://www.imperva.com/learn/application-security/threat-modeling/
- https://www.varonis.com/blog/threat-modeling
