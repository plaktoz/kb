---
source_url: https://valueaddvc.com/pulse/meta-muse-spark-open-816b-parameter-model-2026
author: Value Add VC
date: 2026-10-15
---

# Meta Ships An 816B-Parameter Open Model For Macs

Meta released Muse Spark Open, an 816-billion-parameter open-weight model with a 1-million-token context window built to run locally on Apple's new Mac Studio with the M5 Ultra chip.

## The Rundown

Meta is shipping its most capable open-weight model yet instead of keeping it behind an API, a notably different posture than the closed Muse Wonder release just three days earlier.

Requiring roughly 1TB of RAM to run locally means this targets well-funded labs clustering multiple Mac Studios, not solo developers on a laptop.

Pairing the release with Apple's new M5 Ultra chip gives Apple a flagship AI workload to sell into, even though Apple had no public role in training the model.

Open-weight releases this large pressure Meta's own prior flagship, Llama, and rivals like Mistral and DeepSeek competing for the same developer mindshare.

## The VC Read

Watch the hardware math, not just the model card: a single Mac Studio M5 Ultra tops out around $9,500 for 256GB, and Meta's own minimum spec calls for roughly 1TB of RAM, meaning a real deployment needs multiple clustered units, pushing total hardware cost well past $20,000. That's a specific, checkable number that tells you this release targets funded AI teams and enterprise labs, not the open-source hobbyist audience Meta's framing implies.

## Analysis

Meta released Muse Spark Open on Thursday, an open-weight AI model the company calls the most capable openly available model built in the United States, with 816 billion parameters, a 1-million-token context window, and native multimodal support for complex coding and agentic work, according to TechCrunch. The model is designed to run locally on Apple hardware, specifically a Mac Studio equipped with Apple's new M5 Ultra chip, and is available now through several API platforms for developers who don't want to self-host it.

## From a closed frontier model to an open one, in three days

The release caps a fast pivot inside Meta's Superintelligence Labs, led by Alexandr Wang. Muse Spark first launched in April 2026 as the unit's debut model, closed and API-only, aimed at powering Meta's own products. Meta followed with Muse Wonder on Oct. 12, its first genuine frontier-class model, which Pulse covered as the lab's long-delayed answer to OpenAI and Anthropic. Shipping an open-weight variant of Spark just three days after Wonder's closed debut suggests Meta is running a dual-track strategy: compete at the closed frontier against GPT and Claude, while using open weights to win back developer mindshare that drifted to Meta's own earlier Llama models, DeepSeek and Mistral as those projects matured faster than Meta's follow-ups.

Meta says Muse Spark Open outperforms other popular open-weight models on its own evaluation suite, released Thursday, and has already paired internally with Muse Code, its AI coding terminal, to ship a real Mastodon-client update, bug fixes, new features and a full build, Meta says. It's also been demonstrated inside DaVinci Resolve for reviewing and cropping video footage, pointing toward creative and developer tooling as the near-term use case Meta is pitching, rather than consumer chat.

The catch is hardware. Meta's own guidance says running the model locally requires at least 1 terabyte of RAM, with the best performance on a Mac Studio configured with the M5 Ultra chip, a system that, at over $10,000 for a 256GB configuration, is well short of the 1TB floor on its own. Apple's answer, per Apple's own announcement, is to cluster multiple Mac Studio units over Thunderbolt 5 with RDMA support, pooling memory across machines; a four-unit cluster delivers up to 3x faster distributed inference than one machine alone, Apple says. That math puts a real deployment well north of $20,000 in hardware before any cloud alternative is considered, a meaningfully different audience than the "run it on your laptop" framing the open-weight label implies.

For AI infrastructure investors, the more interesting signal than the model itself is Apple's posture: nothing in Meta's announcement describes a formal commercial partnership, and Apple hasn't said anything officially about Muse Spark Open, but the model was explicitly engineered around Apple's newest silicon. If that relationship deepens, it would mark a notable thaw between two companies that have mostly kept their AI roadmaps separate, Apple leaning on its own on-device models and reported outside deals, Meta building out Muse independently. Whether that's a one-off compatibility choice or the start of something more formal is the thing to watch heading into Apple's next developer cycle.

Reported by TechCrunch · Analysis by Value Add Pulse.
