---
source_url: https://venturebeat.com/technology/meta-unveils-muse-spark-open-the-new-top-u-s-open-weights-model-and-it-runs-on-two-paired-mac-desktops
author: Carl Franzen
date: 2026-10-15
---

# Meta unveils Muse Spark Open, the new top U.S. open weights model — and it runs on two paired Mac desktops

Chinese labs have become a go-to source for AI models businesses can download, customize and run on their own infrastructure. Alibaba’s Qwen, DeepSeek and Moonshot AI’s Kimi help set the competitive standard for open-weight systems, giving developers alternatives to proprietary models accessed through commercial APIs.

That shift shows up in adoption as well as benchmarks. Hugging Face’s March 2026 assessment says Chinese models accounted for 41% of downloads over the preceding year, surpassing U.S. models. In September, OpenRouter reported that open-weight models handled 60% of token volume from U.S.-originating requests on its platform, with Chinese labs supplying most of its open-model traffic.

Now Meta is releasing Muse Spark Open, an 816-billion-parameter model it calls “the most capable US open-weight model to date.” Announced October 15, the release gives enterprises another U.S.-developed option for running and adapting a large model themselves — and on relatively affordable consumer hardware, no less.

The geographic qualifier matters to the competition between AI labs and to buyers with specific procurement requirements. For enterprise teams choosing on practical grounds, the tests are task completion, reliability, licensing and operating cost. Where a model is developed does not by itself determine where business data is processed: OpenRouter already offers U.S. hosting for Chinese models, including DeepSeek V4 Pro and Kimi K3.

Meta’s published results make Spark Open a contender with specific strengths, rather than an overall open-weight leader. Its model card reports an Artificial Analysis Intelligence Index score of 39, below MiMo-V2.6-Pro’s independently published 46.

Meta’s table puts Spark Open ahead of its listed rivals on the JobBench and MCP-Atlas tool-use tests, but behind Kimi K3 and GLM 5.3 on terminal coding, extended software-engineering tasks and the GDPVal-AA professional-work evaluation. A separate public Artificial Analysis assessment of Spark Open could not be verified at publication.

The announcement does not establish a cost lead: it omits hosted token rates, while Meta’s desktop configuration uses a pair of M5 Ultra Mac Studios with a memory configuration that hasn't publicly shipped yet.

Spark Open’s case rests on what enterprises gain from its particular combination of capabilities, hardware support and commercial terms. U.S. leadership alone does not settle that buying decision.

## A large model with a consumer desktop configuration

According to the Spark Open model card, the model uses a mixture-of-experts design, activating 42 billion of its 816 billion parameters for each token. It supports a context of up to 1 million tokens and accepts text, images, video and audio. Its output is text.

That distinction matters for prospective applications. A developer can use the model to interpret recordings, inspect screenshots or analyze documents alongside written instructions. The release does not make Spark Open an image, audio or video generator.

Meta’s desktop configuration combines two M5 Ultra Mac Studios, each offering up to 512GB of unified memory. In its launch announcement, Meta describes the pair as providing a terabyte of memory and says MLX enables local operation.

The desktop pitch comes with a catch: Apple’s 512GB-memory configuration doesn’t arrive until late October, and its price remains unannounced. Current pricing points to an investment of tens of thousands of dollars. Apple lists a 256GB M5 Ultra workstation with a 1TB SSD at $10,799; four would provide the same combined terabyte of memory for $43,196 before tax and accessories. That provides a reference for the cost of assembling comparable memory capacity today, rather than a confirmed price for Meta’s two-computer setup.

The model card lists at least 700GB of accelerator memory for the NVFP4 version and 2TB for BF16. Activating a smaller share of the model during generation does not reduce those stated memory requirements to those of a standalone 42-billion-parameter model.

Meta describes local demonstrations in which Muse Code, powered by Spark Open, modifies the Ice Cubes Mastodon application and operates DaVinci Resolve to review footage and prepare vertical crops. These are company demonstrations; the announcement supplies no measured token-generation rate or complete hardware cost for the two-computer setup.

Developers can also use familiar serving software. Meta lists SGLang, vLLM, TensorRT-LLM, Transformers, MLX, llama.cpp and Unsloth, with support spanning AMD, Apple, Intel and Nvidia hardware. It points to PyTorch’s TorchTitan for further tuning.

## Strong results on selected tasks, with competition on coding

Meta’s benchmark table places Spark Open ahead of the listed competitors on JobBench and MCP-Atlas. The same table shows GLM 5.3, Kimi K3 and Qwen3.8 ahead on several other measures.

| Evaluation | Muse Spark Open (xhigh) | GLM 5.3 (max) | Kimi K3 (max) | Qwen3.8-2.4T-A95B (xhigh) |
|---|---|---|---|---|
| JobBench | 61.8 | 61.4 | 54.3 | 52.7 |
| MCP-Atlas | 89.2 | 84.2 | 82.3 | 84.5 |
| GDPVal-AA v2 | 1,401 | 1,653 | 1,537 | 1,613 |
| Terminal-Bench 2.1 | 76.4 | 83.9 | 85.0 | 82.0 |
| DeepSWE 1.1 | 60 | 67 | 68 | 57 |
| Artificial Analysis Intelligence Index | 39 | 45 | 44 | 40 |

These figures come from Meta’s materials, using the reasoning settings shown above. DeepSWE figures use each model’s preferred or best-available harness, so the surrounding agent software is part of the comparison.

Meta reports the Intelligence Index score of 39 in its model card. At publication, VentureBeat could not verify a separate public assessment of Spark Open from Artificial Analysis; the score should therefore remain attributed to Meta’s table. Artificial Analysis’s evaluations of the hosted Spark and Wonder models concern separate releases.

Spark Open also leads the listed models on HLE-Diamond without tools, scoring 26.1 against Kimi K3’s 22.2 and Qwen3.8’s 17.3. On visual evaluations with tools, it records 50 on ZeroBench against Kimi K3’s 41, and 73.6 on SimpleVQA against 71.9.

The U.S. qualification in Meta’s headline claim matters. Its table lists Intelligence Index scores of 26 for Inkling and 23 for Nemotron 3 Ultra, below Spark Open’s 39. Several other open-weight competitors nevertheless score higher. These results support a competitive U.S. release, with task-specific advantages; they do not establish a universal performance lead.

That U.S. distinction helps explain the enthusiasm of Interconnects author Nathan Lambert. “I waited so long for US open weight models to be relevant again,” he wrote on X. “Still more work to do!”

Independent listings from Artificial Analysis put that geographic distinction in sharper focus. The evaluator lists Xiaomi’s MiMo-V2.6-Pro at 46, GLM-5.3 at 45 and Kimi K3 at 44. It also lists GLM-5.3-Flash at 42, while Qwen3.8 2.4T A95B and Qwen3.8-Flash-Next each score 40. All six published scores exceed the 39 Meta reports for Spark Open.

Those comparisons remain provisional for Meta’s released checkpoint until its result can be independently confirmed. They nevertheless show why leadership among U.S.-developed open-weight models is a narrower claim than leadership across downloadable models worldwide. Spark Open adds another U.S. option for enterprise teams, while the higher published scores of several Chinese releases remain part of the competitive picture.

## Free commercial use has a specific exception

The Muse Model License grants rights to run, modify, fine-tune, distill and redistribute the software, subject to its conditions and usage policy.

Its revenue provision targets businesses providing models as a service. When the licensee and its affiliates generate more than $20 million in aggregate gross revenue during any consecutive 12 months, the license requires notification to Meta and a separate written agreement before offering Spark Open or its derivatives within that model-serving business.

The revenue measure covers the licensee and its affiliates, rather than only revenue attributable to Spark Open. But the provision explicitly exempts internal deployment, research, commercial activities outside model serving, and use inside a company’s own product when that product is not itself a model-as-a-service offering.

For an enterprise developing an internal assistant or incorporating AI features into an application, that exemption is material. The $20 million figure is not a general ceiling on free commercial deployment.

Other obligations still apply. Products must carry the attribution “Built with Muse Spark Open” in a permitted location, which can include documentation, a website or settings. The license also defines derivatives broadly enough to encompass models improved using Spark Open’s outputs. Meta states that it claims no ownership of generated outputs.

The appropriate description is therefore an open-weight release under a custom license. Downloadable access does not remove the license’s commercial conditions or usage restrictions.

## An unusually detailed download gate, with precedents

Spark Open’s Hugging Face access notice asks applicants for their “full legal name,” “date of birth,” and “full organization name with all corporate identifiers.”

It instructs them to avoid acronyms and special characters, says the submitted form cannot be edited, and warns that failing to follow the instructions could affect access to this and other models on Hugging Face. The notice says the information falls under Meta’s privacy policy.

That is an unusually detailed request compared with Hugging Face’s default access gate. The platform’s documentation describes a default process in which users share their username and email address with a model’s authors. Publishers can add fields and customize the notice; the birth-date request is not a universal requirement for downloading models from Hugging Face.

The wording nevertheless has clear precedents. The Hugging Face pages for Meta’s Llama 4 Scout, Meta-SecAlign-8B and OMol25 display the same instructions.

A release outside Meta, Trillion Labs’ Tri-21B, also displays the same notice, referring to Trillion Labs’ privacy policy.

Those examples establish precedent for the published request, although they do not establish how each publisher verifies the submitted information. For enterprise evaluators, the immediate distinction is between being allowed to operate downloaded weights and the personal information requested to obtain them from a particular repository.

## Hosted access varies by provider

Meta’s announcement names Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter and Together AI as API access routes. It lists Amazon SageMaker AI, Google Cloud Model Garden, Hugging Face and Microsoft Foundry Models for obtaining weights.

Enterprises should distinguish those listings from identical support across every service. Meta’s deployment documentation says Groq access requires approval for an organization and describes a 131,072-token context limit on GroqCloud. It lists a 1,048,576-token context for Fireworks. The host can therefore constrain the model’s advertised capacity.

Together AI lists Spark Open API pricing at $1.25 per million input tokens, $0.15 per million cached input tokens and $4.25 per million output tokens. That means, over API, it is

| Model | Input ($/1M) | Output ($/1M) | Total ($/1M) | Source |
|---|---|---|---|---|
| Muse Spark 1.2 / 1.3 Contributor | $0.10 | $0.20 | $0.30 | Meta |
| MiMo-V2.6-Flash | $0.14 | $0.28 | $0.42 | Xiaomi |
| GPT-6 Luna | $0.10 | $0.50 | $0.60 | OpenAI |
| DeepSeek-V4.1-Flash — off-peak | $0.15 | $0.60 | $0.75 | DeepSeek |
| MiMo-V2.6-Pro | $0.435 | $0.87 | $1.305 | Xiaomi |
| MiniMax-M3 | $0.30 | $1.20 | $1.50 | MiniMax |
| LongCat-2.0 — limited-time promo | $0.30 | $1.20 | $1.50 | LongCat |
| DeepSeek-V4.1-Flash — peak hours | $0.30 | $1.20 | $1.50 | DeepSeek |
| DeepSeek-V4-Pro — off-peak | $0.66 | $1.98 | $2.64 | DeepSeek |
| LongCat-2.0 — standard | $0.75 | $2.95 | $3.70 | LongCat |
| Gemini 3.8 Flash — through Dec. 31, 2026 | $0.75 | $3.75 | $4.50 | Google |
| DeepSeek-V4-Pro — peak hours | $1.32 | $3.96 | $5.28 | DeepSeek |
| Muse Spark 1.1 / 1.2 / 1.3 | $1.25 | $4.25 | $5.50 | Meta |
| Muse Spark Open — Together AI serverless | $1.25 | $4.25 | $5.50 | Together AI |
| GLM-5.3 | $1.40 | $4.40 | $5.80 | Z.AI |
| Grok 4.7 — ≤200K prompt tokens | $2.00 | $6.00 | $8.00 | xAI |
| Qwen3.8-Max | $2.00 | $6.00 | $8.00 | QwenCloud |
| Gemini 3.8 Flash — starting Jan. 1, 2027 | $1.50 | $7.50 | $9.00 | Google |
| GPT-6 Sol | $2.00 | $10.00 | $12.00 | OpenAI |
| Claude Sonnet 5.5 | $2.00 | $10.00 | $12.00 | Anthropic |
| Gemini 4 Argon — introductory pricing | $2.00 | $10.00 | $12.00 | Google |
| Grok 4.7 — >200K prompt tokens | $4.00 | $12.00 | $16.00 | xAI |
| Grok 4.7 Fast (Cursor) — ≤256K input | $4.00 | $12.00 | $16.00 | Cursor |
| GPT-5.4 | $2.50 | $15.00 | $17.50 | OpenAI |
| Kimi K3 | $3.00 | $15.00 | $18.00 | Moonshot AI |
| Claude Opus 5.5 | $4.00 | $20.00 | $24.00 | Anthropic |
| Grok 4.7 Fast (Cursor) — >256K input, up to 500K | $6.00 | $18.00 | $24.00 | Cursor |
| Gemini 4 Argon — post-introductory pricing | $4.00 | $20.00 | $24.00 | Google |
| Muse Wonder 1.0 | $4.00 | $20.00 | $24.00 | Meta |
| Sakana Fugu Ultra (≤272K) | $5.00 | $30.00 | $35.00 | Sakana AI |
| Claude Opus 5.5 — Fast mode | $8.00 | $40.00 | $48.00 | Anthropic |
| Claude Fable 5 / Claude Mythos 5 | $10.00 | $50.00 | $60.00 | Anthropic |
| Claude Fable 5.1 / Claude Mythos 5.1 | $10.00 | $50.00 | $60.00 | Anthropic |
| GPT-6 Astra — Standard mode | $10.00 | $50.00 | $60.00 | OpenAI |
| GPT-6 Astra — Fast mode | $20.00 | $100.00 | $120.00 | OpenAI |

Its launch post confirms those rates for serverless access with a 1-million-token context window. Those are Together’s published rates; they do not establish uniform pricing across Meta’s launch partners.

For self-hosted deployments, the license fee is only one component of cost. Hardware, serving capacity and operational support remain part of the buying decision.

## Wonder raises performance, while Full has narrower access

Spark Open arrives amid a broader expansion of Meta’s developer offerings.

On October 12, Meta introduced Muse Wonder and Muse Wonder Full for software engineering and professional tasks involving subjects such as legal documents, finance and health. Meta’s research blog describes stronger underlying models and capabilities intended to retain useful context and sustain work through obstacles.

Independent testing provides evidence of progress. Artificial Analysis reports Intelligence Index v4.3 scores of 52 for Wonder and 56 for Full at maximum reasoning effort, compared with 48 for Spark 1.3 at maximum effort.

On its coding-agent index, Full running in Muse Code scores 68, alongside Claude Code with Sonnet 5.5 at 68 and above the listed Opus 5.5 configuration at 66; Wonder scores 63. These are results for model-and-agent combinations.

The evaluator also reports a GDPval-AA v2.1 score of 1,857 Elo for Full, within the confidence intervals of Opus 5.5 at 1,866 and Sonnet 5.5 at 1,838. That places the systems close together on this professional-work evaluation.

Access and cost qualify those results. Meta’s pricing documentation sets Wonder at $4 per million input tokens, $0.20 for cached input and $20 for output. Meta’s Wonder product page lists a 1-million-token context for both versions, but Full has no published token price: it is available through Muse Code’s $50 monthly Power Usage or $200 Maximum Usage subscriptions.

According to Meta’s subscription rules, those subscriptions apply to Muse Code rather than arbitrary API keys. Usage limits remain, and separate keys incur pay-as-you-go charges.

Subscriptions also default to Contributor mode, allowing Meta to use submitted content for model training in exchange for greater usage. Users can disable that setting, and both Wonder models remain available on eligible plans in either mode. That setting deserves attention before a team submits proprietary code or documents.

Performance gains also carry a higher measured operating cost. Artificial Analysis estimates $4.52 per Intelligence Index task for Wonder, compared with $1.60 for Spark 1.3, $1.99 for Gemini 4 Argon and $0.72 for GPT-6.1 Sol in the tested configurations. Those benchmark costs do not predict every production workload, but they show why token prices alone cannot settle a model comparison.

## Glimmer and Spark mark different stages of the same expansion

Meta introduced the original Muse Spark on April 8, describing it as the first model from its rebuilt Superintelligence Labs organization. Initial access came through Meta AI’s website and application, with an API preview restricted to selected users.

The launch emphasized multimodal reasoning and tool use. Meta also acknowledged remaining gaps in coding and tasks requiring sustained execution—areas that feature prominently in its subsequent releases.

The later hosted Spark models remain less expensive than Wonder. Meta’s current rates list Spark 1.1, 1.2 and 1.3 at $1.25 per million input tokens and $4.25 for output in Standard mode. Contributor variants of 1.2 and 1.3 cost $0.10 and $0.20 respectively, with permission to use customer content for training. Those rates describe the hosted Spark versions, not Spark Open.

Muse Glimmer, released August 10, serves a different deployment need. It is a 30-billion-parameter model under Apache 2.0, designed for local agents that use tools, interpret images and recover from failed steps.

Meta says its compressed language-model weights occupy less than 20GB, allowing the broader setup to operate within 24GB or 32GB memory configurations. That is a substantially smaller hardware requirement than Spark Open’s. For hosted use, Together AI lists Glimmer at $0.35 per million input tokens and $1.50 for output.

## The Llama precedent, with a more varied commercial strategy

Meta’s downloadable-model history predates Muse. The company released the original LLaMA in February 2023 in sizes reaching 65 billion parameters, initially using a research-focused, noncommercial license.

Llama 2 followed in July 2023, expanding availability to commercial applications. In July 2024, Meta released Llama 3.1’s 405-billion-parameter model alongside smaller versions.

The April 2025 Llama 4 release introduced the downloadable Scout and Maverick models, combining native multimodal processing with mixture-of-experts designs. Those architectural ideas also appear in Spark Open.

Taken together, Meta’s 2026 releases suggest a more segmented commercial strategy. Glimmer offers a comparatively compact download under Apache 2.0. Spark Open offers a much larger download with custom commercial conditions. Hosted Spark provides lower token prices, while Wonder and Full target more demanding work through APIs and subscriptions.

For enterprise buyers, the practical choice now spans capability, deployment control, licensing, data use and operating cost. Spark Open adds a substantial new option for teams prepared to run or customize their own infrastructure. Whether that option pays off depends on its performance on their actual tasks—and on what it costs to complete them.
