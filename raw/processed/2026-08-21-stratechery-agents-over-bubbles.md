---
source_url: https://stratechery.com/2026/agents-over-bubbles
author: Ben Thompson
date: Unknown
---

# Agents Over Bubbles

Ben Thompson argues that despite long being sympathetic to the idea that AI spending is a bubble, the rise of agents has changed his mind. He traces three LLM inflection points: ChatGPT (Nov 2022), which was useful but prone to hallucination; OpenAI's o1 (Sept 2024), which reasoned over its answers before responding, making them more reliable; and Anthropic's Opus 4.5 combined with the Claude Code "harness" (late 2025), which let an agent direct a model, verify its own output, and retry until a task is actually done — without the user needing to stay in the loop.

Each paradigm increased compute demand: the first needed heavy training compute but efficient inference; the second required far more inference compute because reasoning consumes many extra tokens; the third requires even more, because agents make multiple calls to reasoning models and need their own compute for tool use. Thompson argues this is why every hyperscaler says demand for compute exceeds supply, and why massive capex is being justified as necessity rather than speculation.

Critically, agents also reshape where profit accrues in the AI value chain. Because effective agents require tight integration between model and "harness," Thompson argues profit will flow to the integrated players — chiefly Anthropic and OpenAI — rather than being commoditized away, as some critics (like Asymco's Horace Dediu, writing about Apple's strategy) have argued. As evidence, he points to Microsoft's own pivot: despite once championing a model-agnostic, commodity-model strategy, Microsoft's new Copilot Cowork product (a rival to Claude Cowork) is not model-agnostic, an implicit admission that a compelling agentic product requires an integrated model-and-harness stack.

Thompson also argues agents will let organizations replace "hard-to-manage-and-motivate human cogs" with agents that work tirelessly, meaning AI-driven layoffs will be about more than correcting pandemic-era overhiring — companies will rightsize toward much smaller workforces built around agents, and competitors who don't will be outcompeted by smaller, AI-native rivals.
