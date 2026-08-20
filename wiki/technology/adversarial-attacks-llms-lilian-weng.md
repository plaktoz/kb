---
type: literature-note
source_url: https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/
author: Lilian Weng
tags: [adversarial-attacks, llm-safety, jailbreak, red-teaming]
date_consumed: 2026-08-20
---

## Summary
Adversarial attacks on LLMs exploit the discrete token input space to trigger undesired outputs, ranging from misclassification to jailbroken instruction-following. Unlike image attacks, text attacks cannot use direct gradient descent on inputs — they must approximate or bypass the non-differentiable token selection step. No single mitigation is fully robust; production defenses require layered approaches.

## Core Concepts
- **Threat model**: attacks happen at [[inference]] time with fixed weights; access is either [[white-box]] (full architecture + gradients) or [[black-box]] (API only)
- **[[Token Manipulation]]**: synonym swaps and character perturbations (TextFooler, BERT-Attack) fool classifiers while preserving human readability
- **[[Gradient-Based Attacks]]**: GCG and HotFlip use gradient information to find adversarial token sequences; [[Universal Adversarial Triggers]] find fixed prefixes that generalize across inputs
- **[[Jailbreak Prompting]]**: exploits tension between safety and helpfulness training ("competing objectives") and gaps in safety fine-tuning coverage ("mismatched generalization")
- **[[Red-Teaming]]**: either human-assisted (structured annotation tools) or model-based (a separate LLM trained via RL to generate attacks against a target)
- **Mitigations**: adversarial training, perplexity filtering, paraphrasing, retokenization, self-reminder prompting — each with [[robustness vs. performance]] tradeoffs

## Key Takeaways
- **Discrete barrier**: text attacks are harder than image attacks because tokens are non-differentiable
- **GCG is most effective**: greedy coordinate gradient search produces highly transferable jailbreak suffixes
- **Competing objectives**: safety vs. helpfulness tension is a structural attack surface, not a patch-able bug
- **Mismatched generalization**: base model capabilities extend further than safety training coverage
- **Black-box sufficiency**: many powerful attacks (jailbreaks, model red-teaming) require no internal access
- **Defense-in-depth**: no single mitigation stops all attacks; layer multiple controls in production
- **Perplexity filter caveat**: blocks some attacks but can reject legitimate complex queries
- **Human red-teaming advantage**: finds nuanced, contextually sensitive failures that automated methods miss

## 🧠 First Principles & Mental Models
- **Competing objectives**: any system trained with conflicting loss signals has an attack surface at the conflict boundary — an attacker who frames a request to satisfy the dominant objective can suppress the safety objective
- **Mismatched generalization**: safety fine-tuning is a narrow overlay on a broad base; the base model's capability surface is larger than the safety surface, leaving gaps an attacker can route through

## 🃏 Review Questions

**Q1**: Why can't text adversarial attacks use the same gradient descent approach as image attacks?
**A**: Text inputs are discrete tokens; there is no continuous pixel space to perturb. Gradient signals exist for the model's internal representations but not for the input tokens themselves, so methods must approximate (Gumbel-softmax, Taylor expansion) or avoid gradients entirely.

**Q2**: What is the "mismatched generalization" jailbreak mechanism?
**A**: Safety fine-tuning covers only a subset of the base model's capabilities. Because the base model generalizes broadly, prompts can access capabilities that exist in the model but were never included in safety training, effectively bypassing the safety layer.

**Q3**: Why is defense-in-depth recommended over any single mitigation?
**A**: Each mitigation (perplexity filtering, paraphrasing, adversarial training, etc.) blocks a different attack vector but degrades performance or fails against other vectors. Combining multiple controls raises the cost of a successful attack without any single control being the point of failure.
