# Generative AI & LLM Foundations: How It Works

**Source:** [Lesson 3A: What is Generative AI? (Deep Dive) — AI Fluency: Framework & Foundations](https://www.youtube.com/watch?v=RyvXxApfHkk)
**Author:** Anthropic (Drew Bent, Prof. Rick Dakan, Prof. Joseph Feller)

---

## What is Generative AI

Generative AI refers to AI systems that **create new content** rather than just analyzing or categorizing existing data. Traditional AI might classify emails as spam; generative AI can write a new email entirely. This distinction marks a fundamental shift in AI capabilities.

**Large Language Models (LLMs)** — such as Claude — are the dominant form of generative AI. They are:
- Trained to predict and generate human language
- "Large" because they contain **billions of parameters** (mathematical values that shape how the model processes information, analogous to synaptic weights in the brain)

---

## Three Key Developments That Made Modern LLMs Possible

1. **Algorithmic & architectural breakthroughs** — The [[transformer architecture]] (2017) was a pivotal innovation. It excels at processing text sequences while maintaining long-range relationships between words, enabling contextual language understanding at scale.

2. **Explosion of digital data** — LLMs train on vast, diverse corpora: websites, code repositories, books, and more. This breadth lets models develop nuanced understanding of both language and knowledge domains.

3. **Massive increases in compute** — Specialized hardware (GPUs, TPUs) and distributed computing clusters made training on these enormous datasets feasible. Progress that would have been impossible a few years prior became routine.

---

## Scaling Laws & Emergent Capabilities

Combining the three factors above revealed **scaling laws**: empirical findings showing that as models grow larger and train on more data with more compute, performance improves in predictable ways.

More surprising: entirely **new capabilities emerge** at scale — abilities no one explicitly programmed, such as:
- Reasoning step-by-step through problems
- Adapting to new tasks with minimal instruction (few-shot generalization)

These emergent behaviors sometimes surprised even the researchers building the models.

---

## How LLMs Are Trained

### Pre-training
The model is shown billions of text examples and trained to **predict the next token**. Through many iterations it builds a compressed map of language patterns and world knowledge — not storing facts like a database, but learning statistical relationships.

### Fine-tuning
After pre-training, models undergo additional training to:
- Follow instructions and give helpful responses
- Avoid generating harmful content
- Use **reinforcement learning from human feedback (RLHF)** — rewards and penalties shape behavior toward being helpful, honest, and harmless

---

## How LLMs Work in Practice

- **Prompts as continuations** — When you send a prompt, the model generates text that statistically follows from it. It is not retrieving a stored answer; it is producing novel text.
- **Context window** — The model's working memory. It holds your prompts, AI responses, and any shared documents. Once the limit is exceeded, information outside the window is inaccessible without tools like web search.

---

## Three Characteristics of Modern Generative AI

| Characteristic | Description |
|---|---|
| Vast training data | Enables learning complex, nuanced language and knowledge patterns |
| In-context learning | Adapts to new tasks from instructions or examples in the prompt alone — no retraining needed |
| Emergent capabilities | Abilities that arise from scale and were not explicitly programmed |

---

## Related Notes
- [[llm-capabilities-and-limitations]]
- [[what-is-retrieval-augmented-generation-rag]]
- [[a-guide-to-context-engineering-for-llms]]
- [[llm-powered-autonomous-agents-lilian-weng]]
- [[ai-capability-stack-tools-mcp-skills-evolution]]
