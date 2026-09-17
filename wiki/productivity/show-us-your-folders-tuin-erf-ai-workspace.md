---
type: literature-note
source_url: https://every.to/context-window/show-us-your-folders
author: Katie Parrott
tags: [ai-workspace, folder-organization, ai-agents, knowledge-management]
date_consumed: 2026-09-17
---

## Summary

Every launched "Show Us Your Folders," a recurring series where team members share their AI workspace setups. The pilot featured [[Kieran Klaassen]] (GM of [[Cora]]), who built a two-part personal system: Tuin (personal storage) and Erf (task dispatcher), grounded in the principle of building around how you already work rather than adopting someone else's template. The newsletter also highlights Anthropic merging Claude Chat and Cowork, and [[Dan Shipper]]'s proposal to "distribute the frontier" of AI to everyday users.

## Core Concepts

- **Tuin / Erf Split**: Klaassen's personal AI workspace divides into Tuin ("garden" in Dutch) for goals, notes, tasks, and memory, and Erf ("yard") as a coordinator that routes tasks to the right agent folder — separating *storage* from *dispatch*.
- **[[Folder-as-Agent Pattern]]**: Extends the same principle from Klaassen's engineering practice — one folder per job, with all required context inside it, so the agent knows exactly what it owns.
- **Temporal Memory Tiers**: Memory in Tuin is organized by time scale (daily, weekly, monthly, yearly), enabling context that is both fresh and durable.
- **[[Compound Engineering]]**: The `/ce-doc-review` command can audit an AI workspace by mapping what each folder owns and surfacing conflicts — recommended before making any structural changes.
- **Distributing the Frontier**: [[Dan Shipper]]'s proposal that AI safety and capability benefits should reach ordinary users independently, not just through institutions. [[Anthropic]]'s Project Glasswing and [[OpenAI]]'s Daybreak are institutional steps, but neither currently reaches everyday users on their own.
- **Anthropic App Consolidation**: Anthropic merged Claude Chat and Cowork into a single app, continuing the industry trend toward a unified knowledge-work interface.

## Key Takeaways

- **Two-folder principle**: Separate storage (Tuin) from dispatch (Erf) to keep context clean.
- **One folder per job**: Each agent folder contains everything it needs; no shared context drift.
- **Build for yourself**: Design workspace systems around your existing habits, not external templates.
- **Temporal memory tiers**: Organize memory by daily / weekly / monthly / yearly time scales.
- **Audit before restructuring**: Use `/ce-doc-review` to map ownership and find conflicts first.
- **AI writing risk-taking**: Mike Taylor argues good AI writing still requires the same honesty and risk-taking as any authentic writing — the model doesn't lower that bar.
- **Frontier distribution gap**: Glasswing and Daybreak are institutional; a personal antivirus-style defensive AI for ordinary users remains unbuilt.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: The Tuin/Erf split operationalizes this at the workspace level — storage and dispatch are kept orthogonal so neither bleeds into the other's domain, reducing ambiguity about where any piece of context lives.
- **[[Conway's Law]]** (applied to personal systems): Klaassen's workspace structure mirrors the structure of the work itself — temporal tiers, per-job folders, a routing layer — so the system's shape reinforces the work's natural boundaries rather than fighting them.

## 🃏 Review Questions

**Q1**: What is the core organizational principle behind Kieran Klaassen's Tuin/Erf workspace?
**A**: Separate storage from dispatch — Tuin holds all personal memory and goals, while Erf routes tasks to the correct agent folder, keeping the two concerns cleanly isolated.

**Q2**: How does the `/ce-doc-review` audit workflow work, and why does it matter?
**A**: It asks the agent to map what each folder owns and identify conflicts before touching anything, with the instruction "Do not move, rename, or delete anything until I approve" — preventing destructive restructuring based on incomplete information.

**Q3**: What does Dan Shipper mean by "distributing the frontier," and why is it still unresolved?
**A**: He proposes an antivirus-style defensive AI tool that ordinary users can run independently, not just rely on institutional players; while Anthropic's Project Glasswing and OpenAI's Daybreak move in this direction, neither yet reaches everyday users without institutional mediation.
