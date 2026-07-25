---
type: literature-note
source_url: https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api
author: OpenAI Help Center
tags: [prompt-engineering, openai-api, llms, ai]
date_consumed: 2026-07-26
---

## Summary

This article explains how to get better results from the OpenAI API by writing clearer, more structured prompts. Its main claim is that model performance improves when instructions are explicit, examples are provided when needed, and output requirements are defined carefully. The guidance is especially relevant for tasks like extraction, classification, code generation, or instruction following.

## Core Concepts

- [[Prompt Engineering]] — crafting instructions that steer model behavior
- [[OpenAI API]] — programmatic interface for calling OpenAI models
- [[Large Language Models]] — models that generate text from prompt input
- [[Few-shot Learning]] — teaching through examples included in the prompt
- [[Zero-shot Prompting]] — asking for a task without examples
- [[Temperature]] — parameter that controls randomness and creativity
- [[Stop Sequences]] — tokens that tell the model when to stop generating
- [[Structured Output]] — formatting responses for reliable parsing

## Key Takeaways

- **Use the latest model**: newer models are usually easier to prompt effectively.
- **Put instructions first**: lead with the task and separate it from context.
- **Be specific**: define goal, length, style, and format clearly.
- **Show examples**: examples improve consistency and reduce ambiguity.
- **Start simple**: try zero-shot before few-shot, then consider fine-tuning.
- **Reduce vagueness**: replace fuzzy wording with precise constraints.
- **State what to do**: positive instructions work better than only listing prohibitions.
- **Use leading words**: hints like "import" can steer code generation patterns.
- **Tune parameters carefully**: [[Temperature]] and model choice affect output behavior.
