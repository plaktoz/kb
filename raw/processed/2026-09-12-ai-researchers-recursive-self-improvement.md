# AI Researchers Debate How Close We Are to Recursive Self-Improvement

source_url: https://www.dwarkesh.com/p/john-beren-charlie
author: Dwarkesh Patel
date: 2026-09-11
publication: Dwarkesh Podcast

---

## Overview

Dwarkesh Patel convenes a discussion with three AI researchers: **Beren Millidge** (CTO, Zyphra), **John Schulman** (Chief Scientist, Thinking Machines; ex-OpenAI co-founder), and **Charlie O'Neill** (Head of Model Training, Baseten) to explore the frontier of AI development and recursive self-improvement (RSI).

---

## Key Themes & Takeaways

### Why 2036 Might Not Be "Superintelligence World"

The researchers brainstorm technical failure modes. Millidge raises a Moravec's-paradox-style concern: AI may excel at benchmarks while a persistent sim-to-real gap blocks real-world impact. Schulman notes the recurring cycle where new models initially impress, then feel limited after regular use.

O'Neill highlights architectural discontinuities—like the shift from pre-training scaling to RL—arguing that if another such leap is required, current methods may not discover it autonomously.

### What Drives Chinese Lab Progress

Schulman points to **distillation** as the primary force countering centralization. He notes Chinese developers likely leverage proxy/router services collecting real user prompts—creating ideal distillation datasets. Millidge adds that Chinese labs can simply purchase the same pre-training data as Western labs.

O'Neill raises a pointed observation: GLM-5.3 and Kimi K3 arguably outperform Anthropic's Sonnet 5 and Opus 5, despite the latter having access to logit distillation from a larger frontier model—suggesting **real-world deployment data may matter more than internal RL environments**.

Schulman offers an alternative hypothesis: large models generalize better from narrow verifiable tasks to realistic settings; distillation without a realistic prompt distribution fails to capture this.

### Training Automated AI Researchers

The group discusses how future AI R&D automation will likely develop through:
- Human feedback to absorb researcher intuition/"taste"
- Multi-step research project environments
- Iterative patching of weaknesses observed during deployment

O'Neill suggests labs will stay near the training frontier, converting recent discoveries into environments rather than rolling back to earlier paradigms—essentially "continual learning within the lab."

### Will Long-Horizon RL Yield AGI?

O'Neill describes labs' apparent strategy: scale RLVR across diverse environments (coding → finance → legal → general work tasks), producing capable agents for economic deployment. The question is whether sim-to-real transfer is sufficient for highly complex, long-horizon real-world tasks.

A key distinction emerges between:
- **Cumulative tasks** (like RSI itself—each discovery is permanently added to the stack)
- **Non-stationary tasks** (like legal work—requiring continuous adaptation to shifting contexts/relationships)

> "It's so unfortunate that RSI happened to be easier than being a paralegal."
> — Dwarkesh Patel

### The Sim-to-Real Gap

Schulman identifies model weaknesses beyond sample efficiency: lower diversity of thought, poor long-horizon judgment, and underdeveloped "taste"—knowing what will work well over the long run of a project.

The group debates whether continual learning is primarily a **capacity problem** or a **technique problem**. Consensus leans toward technique: catastrophic forgetting and plasticity loss prevent indefinite iterative training on the same base model, which is why labs periodically retrain from scratch.

### How Much Progress Comes From Data?

Patel references research (with Princeton student Jerry Han) suggesting pre-training data improvements account for roughly a **12x compute efficiency gain**, versus ~3.7x from architectural improvements—though both figures are small-scale.

Millidge argues this framing may be misleading: architectural improvements unlock qualitatively new regimes (e.g., long-context capabilities) that then make certain data usable. The gains aren't simply multiplicative.

O'Neill notes that at the capability frontier, the world itself may not be generating enough novel signal: "How many new maths problems are being solved that are just beyond the reach of current models?"

### Why RL Is Working Better Than Expected

Millidge attributes RL's outsized impact to:
1. **Mid-training** doing heavy lifting (~80% of capability gains before RL begins)
2. RL providing extremely **high signal-to-noise** bits—unlike SFT, which forces matching exact reasoning tokens

O'Neill emphasizes **horizon generalization**: models trained on RL learn to sustain effort across longer tasks and transfer that persistence to new domains, even without transferring domain-specific reasoning. He cites a paper showing the rate at which models handle longer tasks is doubling roughly every three months.

### Move 37 and Entropy Collapse

The researchers examine the tension between RL causing **entropy collapse** (concentrating probability on known solutions) versus producing genuinely novel strategies analogous to AlphaGo's famous Move 37.

---

## Bottom Line

The researchers broadly agree that recursive self-improvement is not obviously blocked by fundamental technical barriers, but the path is nonlinear. The most likely friction points are:
- Specifying the right objectives (which Schulman calls the "last job for humans")
- Sim-to-real transfer for long-horizon, socially embedded tasks
- Sample efficiency for weight updates from real-world deployment
- The difficulty of discovering new training paradigms within existing ones

As Schulman puts it: "We're nowhere near the ceiling" of how well AI can conduct research—but getting there requires solving objective specification, not just scaling compute.
