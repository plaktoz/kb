---
type: literature-note
source_url: https://www.youtube.com/watch?v=5DtjQrROUzY
author: Maddy Zhang
tags: [llm, tokens, context-window, ai-agents, mcp, rag, fine-tuning, context-engineering, reasoning-models, multimodal-ai, mixture-of-experts]
date_consumed: 2026-08-02
---

## Summary

Maddy Zhang (ex-Google, Amazon, IBM, Microsoft) walks through the 10 foundational AI concepts every software engineer needs to understand in 2026 — from the basic mechanics of [[LLM|large language models]] and tokens to [[AI Agents]], [[MCP]], [[RAG]], [[Fine-Tuning]], [[Context Engineering]], [[Reasoning Models]], [[Multimodal AI]], and [[Mixture of Experts]].

## Core Concepts

- **[[LLM]] (Large Language Model)**: Neural network trained on massive text data to predict the next token in a sequence. At scale, this yields reasoning, code generation, and summarization. Examples: ChatGPT, Claude, Gemini. Understanding LLMs in 2026 is table stakes — equivalent to knowing what an API is in 2010.
- **[[Token|Tokens]] & [[Context Window]]**: LLMs break text into sub-word units called tokens. Every model has a context window — the maximum tokens it can process at once (the model's short-term memory). Early GPT had 4K tokens; modern models exceed 1M. A larger window allows the model to see more conversation, code, or documents simultaneously. Context window exhaustion causes the AI to "forget" earlier parts of a conversation.
- **[[AI Agents]]**: AI systems that can reason, plan, and act autonomously in a loop — perceive → reason → act → observe → repeat — until a goal is complete. A chatbot answers "how to book a flight"; an agent goes and books it. Example: Open Claw (Peter Steinberger), which went viral (60K GitHub stars in 72h) and was acquired by OpenAI.
- **[[MCP]] (Model Context Protocol)**: Open protocol that standardizes how AI models connect to external tools, databases, and services. Analogous to USB for AI — eliminates bespoke integrations. Donated by [[Anthropic]] to the AI Agentic Foundation (Linux Foundation). Rapidly becoming the standard for agent-to-tool connectivity.
- **[[RAG]] (Retrieval-Augmented Generation)**: Adds a retrieval step before generation — relevant documents from a [[Vector Database]] are injected into the LLM's prompt, grounding responses in private or recent data the model wasn't trained on. Solves hallucination for organizational knowledge bases. Vector databases store text as embeddings (semantic numerical representations), enabling similarity search rather than keyword matching.
- **[[Fine-Tuning]]**: Taking a pre-trained model and training it further on a smaller, domain-specific dataset to change *how it behaves* — tone, style, format, specialized vocabulary. Distinct from RAG: use RAG to give the model specific *facts*; use fine-tuning to change the model's *behavior*. Both can be combined.
- **[[Context Engineering]]**: Goes beyond prompt engineering — designing the entire information environment around the model: what RAG documents to retrieve, what conversation history to include, what tools to expose via MCP, and how to prioritize content within the context window. The quality of an LLM's output is directly tied to the quality of the context it receives. Engineers who master this are among the most sought-after in 2026.
- **[[Reasoning Models]]**: LLMs trained to generate an internal chain-of-thought before answering. They pause, decompose problems, consider approaches, and verify logic before producing a final output. Trained via reinforcement learning on verifiable problems (math, code). Examples: OpenAI o-series, [[DeepSeek]]. Essential for agentic tasks requiring multi-step planning rather than pattern-matching.
- **[[Multimodal AI]]**: Models that process and generate across multiple data modalities — text, images, audio, video. Real-world impact includes whiteboard analysis, voice memo transcription, image generation, and medical scan interpretation alongside clinical notes. Cross-modal training also deepens model understanding of shared concepts.
- **[[Mixture of Experts]] (MoE)**: Architectural pattern dating to 1991 that divides a model into specialized sub-networks ("experts") with a router activating only the most relevant experts per query. Result: intelligence of a 100B+ parameter model at the compute cost of a much smaller one. Core reason AI models have scaled so rapidly without proportional cost increases.

## Key Takeaways

- **RAG vs. Fine-Tuning decision rule**: RAG for grounding in new facts; fine-tuning for changing model behavior/style. Combinable.
- **Context engineering is the highest-leverage skill**: Two engineers using the same model can get radically different results depending on how they structure context.
- **Reasoning models need time**: They're slower than standard LLMs but significantly better on complex multi-step problems — use them when planning matters.
- **MoE explains why AI got cheap fast**: Sparse activation means you pay for a fraction of the model on each query while retaining full-model intelligence.
- **Agentic loop architecture**: Agents aren't magic — they're a structured perceive → reason → act → observe loop that runs until a stopping condition.

## Related Notes

- [[what-is-retrieval-augmented-generation-rag]]
- [[a-guide-to-context-engineering-for-llms]]
- [[the-new-rules-of-context-engineering-for-claude-5]]
- [[ai-agents-fundamentals]]
- [[what-is-mcp-integrate-ai-agents-with-databases-apis]]
- [[mcp-vs-a2a-vs-acp-agent-communication-protocols]]
- [[building-effective-ai-agents-anthropic]]

## First Principles & Mental Models

- **[[Scalable Sparsity]]**: MoE demonstrates that intelligence and computational cost can be decoupled — routing activates capability on demand rather than loading the full network every time, the same principle behind microservices and lazy loading in software.
- **[[Context as Working Memory]]**: The context window is a precise technical implementation of working memory theory from cognitive psychology — it has a hard capacity, and what you put inside it directly determines output quality.
