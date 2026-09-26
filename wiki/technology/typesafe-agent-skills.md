---
type: literature-note
source_url: https://github.com/typesafe-ai/skills
author: Unknown
tags: [jev, claude-code, agent-skills, developer-tools]
date_consumed: 2026-09-26
---

## Summary

TypeSafe's agent skills repository provides reusable, installable knowledge modules that teach AI agents (including [[Claude Code]]) how to use the [[Jev]] / [[TypeSafe AI]] API via natural language prompting. Once installed, the skill enables an agent to design TypeSafe workflows, look up current docs and cookbooks, and generate typed judgment code without the developer manually specifying the API.

## Core Concepts

- **[[Agent Skill]]** — a portable knowledge module installable into AI coding agents that teaches the agent a specific API or capability
- **`typesafe-ai` skill** — the core skill; enables "design TypeSafe workflows, find current docs and cookbooks, and compose typed judgments in code"
- **Claude Code plugin** — installed via `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`; invoked with `/typesafe:typesafe-ai`
- **`skills.sh` / npx install** — `npx skills add typesafe-ai/skills --skill typesafe-ai` for non-Claude agents; `-g` flag for global scope
- **Natural language invocation** — prompt the agent: *"Use TypeSafe to route incoming support tickets by department, with human review for uncertain decisions"*

## Key Takeaways

- **What it does**: lets AI agents author TypeSafe/Jev code from natural language descriptions
- **Claude Code install**: `claude plugin marketplace add typesafe-ai/skills` → `claude plugin install typesafe@typesafe-ai`
- **Invocation**: `/typesafe:typesafe-ai` in Claude Code
- **Scope**: project-local by default; add `-g` for global install
- **Reference**: SKILL.md at `github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md`

## 🃏 Review Questions

**Q1**: What problem do agent skills solve for developers using Jev?
**A**: They allow developers to describe what they want in natural language (e.g. "route support tickets by department") and have an AI agent generate the correct TypeSafe workflow code, instead of manually reading API docs.

**Q2**: How do you install the TypeSafe skill in Claude Code vs other agents?
**A**: Claude Code: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`. Other agents: `npx skills add typesafe-ai/skills --skill typesafe-ai`.

**Q3**: What is the scope difference between default and `-g` installs?
**A**: Default install is project-local (only available in the current project); `-g` flag installs globally so the skill is available across all projects on the machine.
