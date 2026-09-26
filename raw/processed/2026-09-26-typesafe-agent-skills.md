---
source_url: https://github.com/typesafe-ai/skills
author: Unknown
date: 2026-09-26
---

# TypeSafe Agent Skills

Agent skills for building with TypeSafe — providing "typed decisions and probabilities from System One models."

## Installation

### Claude Code Plugin

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

### Other Agents (via skills.sh)

```bash
npx skills add typesafe-ai/skills --skill typesafe-ai
```

Select your agent when prompted. Default install is project-local; append `-g` for global scope.

## Usage

Prompt your agent with natural language, for example:

> "Use TypeSafe to route incoming support tickets by department, with human review for uncertain decisions."

In Claude Code, invoke directly with `/typesafe:typesafe-ai`.

## Skill List

| Skill | Purpose |
|-------|---------|
| `typesafe-ai` | Design TypeSafe workflows, locate current docs/cookbooks, and compose typed judgments in code |

## Additional Resources

- SKILL.md: `https://raw.githubusercontent.com/typesafe-ai/skills/main/skills/typesafe-ai/SKILL.md`
- Installation guide: `https://docs.typesafe.ai/agent-skill#installation`

**License:** MIT
