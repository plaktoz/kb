---
source_url: https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/
author: Lilian Weng
date: 2023-10-25
---

# Adversarial Attacks on LLMs

This article examines how adversarial attacks and jailbreak prompts can trigger large language models to produce undesired outputs. Unlike image-based adversarial attacks that operate in continuous pixel space, text attacks face a harder problem: inputs are discrete tokens, so there is no direct gradient signal to exploit. Optimization must work around the non-differentiable token selection step.

## Threat Model

Attacks are assumed to occur at inference time only, with fixed model weights. Two primary access levels:

- **White-box:** Attacker has full access to model architecture, weights, and gradients
- **Black-box:** Attacker only has API access — can observe inputs and outputs but not internals

Tasks covered include both classification (sentiment, toxicity detection) and text generation (instruction following, dialogue).

## Five Attack Types

### 1. Token Manipulation (Black-Box)

Synonym replacement and character-level perturbations to flip model predictions while preserving human readability.

Key methods:
- **TextFooler** — Greedy search over synonym replacements ranked by semantic similarity
- **BERT-Attack** — Uses BERT masked language modeling to generate contextually appropriate replacements

These attacks reveal that classifiers are brittle to surface-form changes that preserve meaning for humans.

### 2. Gradient-Based Attacks (White-Box)

Methods that exploit gradient information to find adversarial token sequences:

- **GBDA (Gumbel-Softmax Discrete Attack)** — Uses Gumbel-softmax relaxation to make discrete token selection differentiable
- **HotFlip** — Approximates token substitution gradient using first-order Taylor expansion
- **Universal Adversarial Triggers** — Finds a fixed prefix/suffix that causes target behavior across many inputs
- **GCG (Greedy Coordinate Gradient)** — Efficient greedy search using gradient to rank candidate token substitutions at each position; highly effective at generating jailbreak suffixes

### 3. Jailbreak Prompting (Black-Box Heuristic)

Human-crafted prompts that exploit systematic weaknesses in safety training:

**Competing objectives:** Safety training conflicts with helpfulness training. Prompts that frame harmful requests as "helpful" can exploit this tension.

**Mismatched generalization:** Safety fine-tuning is applied narrowly, but the base model's capabilities generalize broadly. Prompts can access capabilities that exist in the base model but weren't covered by safety training.

Common techniques: role-play personas, hypothetical framing, code simulation, multi-step escalation.

### 4. Human Red-Teaming

Tool-assisted adversarial generation where human annotators are given structured support (model-suggested variations, scoring feedback) to efficiently find failure modes.

More targeted than automated methods for finding nuanced, contextually sensitive failure cases.

### 5. Model Red-Teaming

Training a separate "red-teamer" LLM to generate attack prompts against a target model:

- **Perez et al.** — Fine-tune a red-teamer via reinforcement learning to maximize target model policy violations
- **FLIRT (Few-shot LLM Red-Teaming)** — Few-shot prompting to steer a base LLM toward generating jailbreaks
- **Casper et al.** — Elicitation-based approach discovering unexpected model capabilities

## Mitigations

Each mitigation involves tradeoffs between robustness and general model performance:

| Mitigation | Mechanism | Tradeoff |
|---|---|---|
| Adversarial training | Include adversarial examples in training | Can reduce helpfulness if overdone |
| Perplexity filtering | Reject inputs with anomalously high perplexity | May block legitimate complex queries |
| Paraphrasing | Rewrite inputs before processing | Adds latency; may lose meaning |
| Retokenization | Randomize tokenization to break token-specific attacks | Changes model behavior unpredictably |
| Self-reminder prompting | Include explicit safety reminders in context | Limited effectiveness against sophisticated attacks |

No mitigation is fully robust. Defense-in-depth combining multiple approaches is recommended for production systems.
