---
type: literature-note
source_url: https://www.nunodonato.com/blog/my-productivity-system-in-2026/
author: Nuno Donato
tags: [gtd, ai-agents, personal-productivity, automation]
date_consumed: 2026-09-28
---

## Summary

A long-time [[Getting Things Done]] (GTD) practitioner describes a 2026 update to his personal productivity system, built around [[Goose]], an open-source AI agent harness, with read-only calendar access and a dedicated agent email mailbox. Three custom skills — GTD list management, an end-of-day brain-dump processor, and a start-of-day briefing generator — automate the busywork around his existing GTD lists rather than replacing the methodology itself. He closes by tying the design to David Allen's principle that systems should support low-energy moments and to the idea of achieving simplicity through subtraction.

## Core Concepts

- **[[Getting Things Done]]**: The author's baseline methodology, which he tightens during hectic periods and relaxes during calmer ones rather than following rigidly at all times.
- **[[Goose]]**: An open-source AI agent harness used for personal (non-work, non-coding) tasks, configured with read-only calendar access and a dedicated agent email mailbox.
- **End-of-Day Brain Dump**: A free-form nightly capture that the agent cross-references against GTD data — adding tasks, checking off completed items, flagging emails, and pre-researching info needed for upcoming commitments.
- **Start-of-Day Briefing**: An agent skill that reviews the prior night's dump, calendar, reminders, and emails to generate a daily priorities briefing with suggested actions.
- **[[David Allen]]**: Creator of GTD, cited for the principle that productivity systems should be designed to support a person's low-energy moments, not just their peak performance.
- **Local-First AI Tooling**: The system is built to work independently of cloud services, including with a local AI model, keeping personal task data outside third-party clouds.

## Key Takeaways

- **Markdown-Based Lists**: The GTD skill manages simple markdown task/project lists, moving items between them as needed.
- **Proactive Research**: The end-of-day skill researches information (e.g., phone numbers) ahead of tasks that need it.
- **Read-Only Calendar Scope**: Agent has read-only access across personal, kids', and work calendars — no write permissions.
- **Dedicated Agent Mailbox**: A separate email address lets the author forward information to, and receive messages from, the agent.
- **Methodology Over Tooling**: GTD stays the constant; the AI agent only automates the mechanical overhead around it.
- **Cloud Independence**: The whole setup also runs against a local AI model, with no dependency on cloud services.

## 🧠 First Principles & Mental Models

- **[[Chesterton's Fence]]**: Rather than discarding GTD for something AI-native, the author keeps the proven methodology in place and only automates the friction around it — changing implementation, not the underlying system that already works.

## 🃏 Review Questions

**Q1**: What is the core idea behind the author's 2026 productivity system update?
**A**: Keep GTD as the underlying methodology, but use an AI agent (Goose) with calendar and email access to automate the mechanical overhead — end-of-day processing and start-of-day briefings — around it.

**Q2**: How does the end-of-day skill work?
**A**: It takes a free-form brain dump and cross-references it with GTD data, adding new tasks, checking off completed ones, flagging emails, and proactively researching information needed for upcoming tasks.

**Q3**: What broader productivity principle does the author invoke to justify the design?
**A**: David Allen's idea that systems should be designed to support low-energy moments, combined with achieving simplicity through subtraction — summarized as "KISS always prevails."
