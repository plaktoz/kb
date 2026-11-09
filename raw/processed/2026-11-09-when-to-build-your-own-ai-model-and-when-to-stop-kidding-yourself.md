---
source_url: https://www.forbes.com/councils/forbestechcouncil/2026/11/09/when-to-build-your-own-ai-model-and-when-to-stop-kidding-yourself
author: Eilon Reshef
date: 2026-11-09
---

# When To Build Your Own AI Model (And When To Stop Kidding Yourself)

We were running our own models at Gong long before ChatGPT became a household name. This was the era of transformer-based language models, the state of the art for natural language understanding before LLMs. We'd take these prebuilt foundation models, train them further on our domain and data and then deploy them for very targeted jobs.

We called it fine-tuning. Academics called it transfer learning. Most people just called it a lot of work.

I tell you this because it's important context for what comes next: the hype around post-trained small language models (SLMs) and their very real practical potential.

## What We're Actually Talking About

First, an important distinction: This isn't about training a foundation model from scratch. For most product companies, that would be economic malpractice. It's about taking an existing model and making it much better at a specific job through supervised fine-tuning, preference optimization, reinforcement learning, distillation or some combination of them.

Fine-tuning is one form of post-training. I'll use the broader term when that distinction matters.

Most major AI providers offer a lineup of models that sits roughly on a diagonal: cheap and fast at one end, more capable and expensive at the other. The names differ, but the trade-offs don't.

The promise of post-training is that it lets you move above this line for a specific task. You can get higher quality than an off-the-shelf model at the same inference cost or comparable task quality at a lower cost.

That doesn't mean the smaller model is smarter overall, but that specialization can make it better at the specific job you need it to do. The real question is when that advantage holds and what it costs.

## Killing The 'Moat' Story

Before we go further, I want to address something I keep hearing in investor conversations and startup pitches: "We fine-tune our own models, so we have a proprietary moat." The reality is, no, you don't.

Fine-tuning is an engineering decision. It's neither magic nor a competitive advantage on its own. Saying "we do post-training" to investors is about as distinctive as saying "we use a database."

What's defensible is what compounds around the model: proprietary data, feedback loops, rigorous evaluation and the application layer, or harness, that connects the model to context, tools, workflows and systems of record.

The learning system that fine-tuning or a generic agent framework creates is the true competitive moat, refined and improved by real-world use. It captures how work gets done, raises switching costs and makes the underlying model replaceable. Pitch the model work itself as the advantage, and the story eventually falls apart with investors or customers who look closely.

## The Real Decision Framework

Knowing when to fine-tune is hard. The decision comes down to four things: scale, task specificity, prompting as the baseline and negotiation leverage.

Scale is the biggest factor. Post-training carries meaningful upfront costs. At millions of inference calls a month, the economics can work. At thousands, they usually don't—especially once ongoing maintenance is included.

Task specificity is the next filter. Fine-tuning works best on narrow, repeatable tasks with a high quality bar. Think tagging customer conversations, emails and calls against a defined taxonomy, where the model must understand the domain and return the exact format the system expects.

Prompting as the baseline means pushing prompt engineering as far as possible before committing to post-training. Strong system prompts, few-shot examples, the right context and strict output specs will go a long way. It's also no longer entirely manual. Automatic optimizers can generate and test variations, raising the baseline before you change a single model weight.

Too many teams skip this work and go straight to fine-tuning because it feels more "real." Don't do that. Exhaust the prompting path first.

Negotiation leverage comes with scale. If you're big enough to consider fine-tuning, you're probably big enough to push vendors on price, volume discounts or dedicated capacity. "Should we fine-tune?" may not be the right question. You should probably be asking, "Should we renegotiate our API contract?"

One prerequisite underlies all of this: evaluation. Build a representative gold set with human-approved answers, hold back some for testing and run every prompt revision, model upgrade and fine-tune through the same pipeline. Keep adding production failures and edge cases. Without strong evals, you can't tell real product improvement from an overfit demo.

## The Ongoing Cost: Operations

Once the math works, scale is achieved and prompting is exhausted, be sure to understand the operational cost of post-training before committing:

1. The model has to run somewhere. Self-hosted or managed, it's still more work than calling a frontier API. You now own uptime, scaling, monitoring, hardware, utilization and capacity planning.

2. Models age. A fine-tuned model reflects a snapshot in time. Months later, the base model has improved, data has shifted and new edge cases have appeared.

Post-training isn't a one-time project. You need to collect new data, rerun evaluations, track drift and retrain as new failure modes emerge. That takes ongoing staffing and investment.

The overlooked cost of SLMs is keeping them competitive.

## Beyond Cost: Other Reasons To Fine-Tune

Cost and quality aren't everything. Latency, control and privacy can also justify fine-tuning. Know what you're optimizing for before you make the investment.

The decision shouldn't come down to cost alone. Be clear about what you're optimizing for: speed, control, privacy, quality or some combination of them.

## Practical Takeaways

Post-training and SLMs are real, powerful tools, but they work best as engineering and business decisions, not marketing stories. The winners usually have scale, strong evaluations, good data and the discipline to keep maintaining the system.

We use both approaches. Some products depend on fine-tuned models, while others are better served by riding frontier improvements. The point is to let the trade-offs decide.

The practical rule is simple: Start broad, measure everything and specialize only when the task is stable and the economics justify it.
