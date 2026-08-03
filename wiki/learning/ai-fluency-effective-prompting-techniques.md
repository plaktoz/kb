---
type: literature-note
source_url: https://www.youtube.com/watch?v=2YCaBqP8muw
author: Anthropic (with Prof. Rick Dakan & Prof. Joseph Feller)
tags: [prompting, prompt-engineering, ai-fluency, claude, llms, description-competency]
date_consumed: 2026-08-03
---

## Summary

Lesson 7 of Anthropic's AI Fluency: Framework & Foundations course. Prompting is the practical application of the "description competency" — clearly communicating what you want, how you want it, and how to interact with an AI throughout the task. Six foundational tips consistently improve results across AI systems, and the meta-technique of asking the AI to improve your prompt is presented as a "secret weapon."

## Core Concepts

- [[Prompt Engineering]] — designing effective instructions for AI systems
- [[Few-shot Prompting]] — providing examples the AI should emulate (n-shot where n = number of examples)
- [[Chain of Thought Prompting]] — decomposing complex tasks into ordered steps
- [[Description Competency]] — the AI fluency skill of communicating intent clearly to an AI assistant
- [[Context Window]] — the limited memory space an AI can attend to; affects how much background info is useful

## Six Foundational Prompting Tips

1. **Give context** — specify what you want, why you want it, who you are, and how you'll use the output. Vague prompts leave the AI guessing about depth, geography, expertise level, etc.

2. **Show examples (few-shot)** — provide samples of your desired output style when it's easier to show than describe. Cover diverse cases so the AI grasps the full pattern.

3. **Specify output constraints** — define format, length, coding language, design choices, or any other production requirement upfront to avoid reformatting later.

4. **Break complex tasks into steps** — list the process you want followed (chain of thought). More useful when execution requires domain knowledge or when there is high variance in how a task could be done well.

5. **Ask the AI to think first** — explicitly prompt the AI to reason through the problem before answering. Reasoning models do this by default; for others, add "think through this carefully before responding." Thinking *before* acting improves quality more than explaining afterward.

6. **Define role, style, or tone** — specify expertise level, persona, or communication style. Useful for audience-targeted explanations (e.g., "science teacher explaining to a 10-year-old") and for structured feedback (e.g., "as a UX expert, review this wireframe").

## Bonus: Ask the AI to Improve Your Prompt

When unsure how to phrase a request, describe the situation to the AI and ask it to craft or improve the prompt for you. Performance varies across models, so experimentation is encouraged.

## Iterative Mindset

- First attempts rarely yield perfect output — iteration is expected and productive.
- Tactics for refinement: add specificity, provide examples, break into steps, request variations, check confidence, reset the conversation.
- Prompting best practices evolve as models improve; some specific techniques become unnecessary as AI capabilities advance.

## Common Mistakes to Avoid

- Assuming the AI can infer unstated context.
- Overloading one prompt with multiple unrelated tasks.
- Being vague about what success looks like.
- Not giving feedback on previous responses.

## Related Notes

- [[best-practices-for-prompt-engineering-with-the-openai-api]]
- [[agentic-ai-workflow-prompt-engineering-ibm]]
- [[ai-fluency-discernment-product-process-performance]]
