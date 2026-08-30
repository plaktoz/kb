---
source_url: https://the-decoder.com/openais-first-custom-chip-jalapeno-reportedly-beats-nvidias-blackwell-and-rubin-in-inference-benchmarks/
author: Matthias Bastian
date: 2026-08-25
---

# OpenAI's first custom chip "Jalapeño" reportedly beats Nvidia's Blackwell and Rubin in inference benchmarks

OpenAI showed off the first benchmarks for its in-house inference chip at the Hot Chips conference. "Jalapeño" reportedly outperforms both Nvidia's Blackwell and Rubin in throughput per watt and token latency.

The chip handles inference only, meaning it runs AI models but doesn't train them. Jalapeño isn't tuned to OpenAI's own models either. It's a general-purpose LLM inference accelerator.

OpenAI claims Jalapeño delivers 1.5x to 1.9x more AI work per watt at peak throughput across all three tested models, with 1.7x to 3.6x lower end-to-end latency than the best commercially available systems. For interactive workloads, the company says performance is 2.1x to 4.1x higher.

The results come from tests using SemiAnalysis's public InferenceX benchmark. OpenAI provided the numbers. SemiAnalysis verified some runs on-site in the lab. The models tested were GPT-OSS 120B, Deepseek R1 670B, and Kimi K2.5 1T. On GPT-OSS, Jalapeño hit about 1,400 tokens per second per user. On Deepseek R1, it topped 700 tokens per second on a single concurrent request.

At matched decoding speed, Jalapeño achieves 54x to 104x the token throughput per kilowatt compared to the best available accelerator, depending on the model.

Jalapeño posted these numbers without using techniques like multi-token prediction or speculative decoding, while some of the comparison systems did rely on those optimizations, so there's still room to improve.

In its headline performance-per-watt comparison, "Jalapeño smokes every other chip," SemiAnalysis writes. SemiAnalysis CEO Dylan Patel added, "Usually first generation chips aren't competitive, but OpenAI is beating Nvidia Blackwell and even Rubin."

SemiAnalysis points out that the fairer comparison isn't Blackwell but Nvidia's newer Vera Rubin platform, since both use HBM4 memory. Even here, Jalapeño squeezes out more output tokens per megawatt than Vera Rubin, even though Nvidia's accelerator uses the multi-token prediction optimization that Jalapeño hasn't adopted yet. On total cost of ownership per token, the two come out roughly even.

There are caveats, though. Nvidia and AMD have already published results with larger models like Deepseek V4 Pro and Kimi K3 that haven't been tested on Jalapeño yet. And while Rubin systems are already shipping to customers, Jalapeño reportedly hasn't moved beyond engineering samples.

## OpenAI built the chip in nine months, partly using its own models

OpenAI developed Jalapeño with Broadcom. Design work kicked off in mid-2024, and the final design went to fabrication in November 2025. The full cycle took about 16 months, but OpenAI says only nine months passed between the first chip design and the finished blueprint heading to the factory. The company used its own AI models during development, according to OpenAI. Older model generations helped with chip design, while newer ones sped up programming and optimization.

SemiAnalysis sees this as a sign that Nvidia's much-discussed "CUDA moat" may not hold anymore. "The CUDA moat is potentially dead given how fast OpenAI can bring up new models on their silicon," the firm wrote.

OpenAI CFO Sarah Friar says the chip fits into a broader compute strategy where data centers, chips, models, the developer platform, products, and devices all work as one integrated system. She claims Jalapeño complements OpenAI's existing partnerships with Nvidia, AMD, AWS, Cerebras, CoreWeave, and others rather than replacing them.

OpenAI has deep ties with several of these companies. Nvidia, AMD, and AWS are all investors or compute partners, with Nvidia being one of the largest. Each of them is also building its own AI chips, which makes the relationship both cooperative and competitive. That said, all of these companies keep saying the world can't have enough compute, a claim that conveniently supports their own business models.
