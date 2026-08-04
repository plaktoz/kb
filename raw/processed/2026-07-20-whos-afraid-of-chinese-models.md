---
source_url: https://stratechery.com/2026/whos-afraid-of-chinese-models/
author: Ben Thompson
date: 2026-07-20
---

# Who's Afraid of Chinese Models?

Thompson argues that panic over Chinese AI models like Kimi K3 and Alibaba's Qwen3.8 Max is largely overblown from an economic standpoint, while identifying one genuinely serious concern.

## Key Arguments

**Open weights aren't truly "free"** — The cost savings Chinese models offer apply only to R&D (a fixed cost). COGS — inference costs — are very real and scale with usage. Token pricing comparisons can be misleading because reasoning-heavy models may use far more tokens per correct answer.

**Intelligence, not tokens, is the commodity** — Tokens aren't fungible across models; the underlying *intelligence* is. Cost per unit of intelligence depends on model footprint, inference efficiency, memory efficiency, serving efficiency, and token efficiency.

**Commodity market dynamics** — In mature commodity markets, the lowest-cost producer wins. Thompson believes frontier labs like Anthropic and OpenAI likely have superior cost structures, and current high prices reflect supply constraints rather than Chinese models being structurally cheaper.

**Why labs panic anyway:**
- Historical anchoring to training-cost-dominated financial models
- Data flywheel advantages from running inference
- Stickiness of developer tools (e.g., Claude Code)
- Anthropic's ideological belief in its own unique trustworthiness

**China's strategy is deliberate** — Xi Jinping's push for open-weights AI aligns with China's strength in physical-world industries like robotics. Thompson frames it as "commoditize your complements."

**Distillation is structural** — Chinese labs benefit from using frontier US models as teachers for reinforcement learning. Meanwhile, US open-weight developers are contractually barred from doing the same, leaving them disadvantaged. Thompson proposes:
1. Codifying AI training data collection as fair use
2. Banning terms-of-service restrictions on distillation for US companies

**The real danger — cybersecurity** — Thompson cites a Hugging Face breach where US model guardrails blocked incident responders, forcing them to use China's GLM 5.2 instead. He calls Trump administration restrictions on using frontier models for cybersecurity "insane," arguing defenders need the best tools available.

## Conclusion

Thompson contends the US should compete through openness and capability — loosening restrictions on frontier model use in cybersecurity and leveling the playing field for domestic open-weight developers — rather than ceding the innovation narrative to China.
