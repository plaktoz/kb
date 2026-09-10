---
source_url: https://every.to/working-overtime/i-vibe-coded-a-security-risk
author: Katie Parrott
date: 2026-08-10
---

# I Vibe Coded a Security Risk

Parrott, a self-described "baby vibe coder," built an app called Tastemaker — a writing style guide tool — then added an MCP (AI agent connector) without proper security review. A later audit revealed "a public registration route" that was openly accessible when it shouldn't have been. No data was confirmed stolen, but the feature was taken down immediately.

She traces the failure to two cognitive traps:

1. **Illusion of explanatory depth** — because the AI's explanation *sounded* coherent, she assumed she understood the underlying work
2. **Confirmation bias in testing** — she verified the happy path (it connected!) but never asked whether *unauthorized* users could also connect

Her key takeaway: "If AI built the thing, don't let the same system's reassurance be the only evidence that it's ready." She now advocates for human expert review and deliberate friction before deploying AI-generated features.

The broader point is about **task crossover** — AI enabling non-specialists to do specialist work fast enough to outrun their own judgment.
