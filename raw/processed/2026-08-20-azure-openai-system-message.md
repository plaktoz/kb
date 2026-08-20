---
source_url: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/system-message
author: Unknown
date: 2026-08-20
---
# Safety System Messages - Microsoft Foundry (Azure OpenAI)


Safety system messages help you guide an Azure OpenAI model's behavior, improve response quality, and reduce the likelihood of harmful outputs. They work best as one layer in a broader safety strategy.

> **Note:** This article uses "system message" interchangeably with "metaprompt" and "system prompt." "Component" refers to a distinct part of a system message, such as instructions, context, tone, safety guidelines, or tool usage guidance.

## What is a system message?

A system message is a set of high-priority instructions and context that you send to a chat model to steer how it responds. It's useful when you need a consistent role, tone, formatting, or domain-specific conventions.

## What is a safety system message?

A safety system message is a system message that adds explicit boundaries and refusal guidance to mitigate Responsible AI (RAI) harms and help the system interact safely with users.

Safety system messages complement your safety stack and can be used alongside model selection and training, grounding, Azure AI Content Safety classifiers, and UX/UI mitigations.

## Key components of a system message

Most system messages combine multiple components:

- **Role and task**: What the assistant is and what it's responsible for.
- **Audience and tone**: Who the response is for, and the expected voice.
- **Scope and boundaries**: What the assistant must not do, and what to do when it can't comply.
- **Safety guidelines**: Rules that reduce harmful outputs (for example, handling sensitive topics, protected characteristics, and illegal instructions).
- **Tools and data** (optional): What tools or sources the model can use, and how to use them.

## How to design and iterate safely

When you design a system message (or a safety system message component), treat it like a testable artifact:

- **Define the scenario.** Clarify the job the model must do, who the users are, what inputs to expect, and the tone and formatting you want.
- **Identify risks.** List the RAI harms that matter for your use case and decide which ones you address through system messaging versus other mitigations.
- **Decide how the model should behave at boundaries.** Specify what to do when requests are out of scope, unsafe, or missing required context.
- **Create a test set.** Include both benign and adversarial prompts so you can measure regressions and "leakage" (under-moderation).
- **Evaluate and iterate.** Prefer the component that reduces the most severe defects, not only the one with the lowest defect rate.

Example template structure:

```text
## Define model's profile and general capabilities  

- Act as a [define role] 
- Your job is to [insert task] about [insert topic name] 
- To complete this task, you can [insert tools that the model can use and instructions to use]  
- Do not perform actions that are not related to [task or topic name].  
```

Complete example — customer service assistant:

```text
## Role and task
You are a helpful customer service assistant for Contoso Electronics. Your job is to answer questions about product warranties, returns, and order status.

## Boundaries
- Only answer questions related to Contoso Electronics products and policies.
- If you don't know the answer, say "I don't have that information. Please contact support@contoso.com."
- Do not provide legal, medical, or financial advice.
- Do not discuss competitors or make comparisons.

## Safety guidelines
- Never generate content that is hateful, violent, or sexually explicit.
- Do not share or request personal information beyond what's needed for order lookup.
- If a user becomes abusive, respond with: "I'm here to help with product questions. How can I assist you today?"

## Response format
- Keep responses concise and friendly.
- Use bullet points for multiple items.
- Always end with an offer to help further.
```

## Summary of best practices

- **Use clear language**: Eliminates over-complexity and risk of misunderstanding.
- **Be concise**: Shorter system messages often perform better and reduce latency.
- **Emphasize certain words** using `**word**`: puts special focus on key elements.
- **Use second person** when referring to the AI system: e.g., `You are an AI assistant that…`
- **Implement robustness**: The system message should perform consistently across different datasets and tasks.

## Authoring techniques

### Top performing techniques

| Technique | Definition | Example |
| --- | --- | --- |
| Always / should | Structure prompts with directives that the AI should always follow. | `**Always** ensure that you respect authentication and authorization protocols...` |
| Conditional / if logic | Structure prompts so the output depends on meeting specific conditions: `If <condition> then <action>`. | `If a user asks you to infer emotions, respond with: "Try asking me a question..."` |
| Emphasis on harm | Define the main risk to guide outputs toward safety and harm prevention. | `You are **allowed** to answer some questions about images with people...` |
| Example(s)-based | Give the model clear instances for better context using harmful and non-harmful request examples. | Show examples of harmful vs. benign requests as a reference. |
| Never / don't | Use explicit prohibitions to prevent inappropriate, harmful, or out-of-scope content. | `**Never** make assumptions, judgments, or evaluations about a person.` |

### Other techniques to consider

| Technique | Definition |
| --- | --- |
| Catch-all | Combines multiple methods into one framework; reduces gaps but increases length and latency. |
| Emphasis on learned knowledge | Encourages the model to draw from prior knowledge. |
| Highlight the role of AI | Separates safety behavior from the assistant's primary role. |
| Reverse logic | Reframes prohibitions into positive actions. |
| Risk-based | Focuses on primary risk and prioritizes prevention of the most severe harms. |
| Rules-based | Uses explicit rules (e.g., "never", "always", conditional logic) to constrain outputs. |

## Limitations

System messages aren't a complete safety solution:

- Adversarial prompting can bypass or degrade them.
- They can reduce usefulness if they're too broad or too strict.
- Ongoing evaluation is required as your models, tools, and user scenarios change.

## Recommended system messages

System messages, or metaprompts, aren't "one size fits all." Use of these types of examples has varying degrees of success in different applications. It's important to try different wording, ordering, and structure of system message text to reduce identified harms, and to test the variations to see what works best for a given scenario.

For more information on recommended safety components, see the [Safety system message template guidance](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/safety-system-message-templates).
