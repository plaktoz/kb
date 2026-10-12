---
source_url: https://www.mountsinai.org/about/newsroom/2026/mount-sinai-study-finds-safety-prompts-can-help-ai-models-make-safer-clinical-choices
author: Unknown
date: 2026-10-08
---

# Mount Sinai Study Finds Safety Prompts Can Help AI Models Make Safer Clinical Choices

## Large-scale study of 20 AI models and more than 10 million responses reduces potentially harmful clinical choices in 19 models

New York, NY (October 08, 2026)

As artificial intelligence (AI) becomes increasingly capable of assisting with health care tasks, a new study by researchers at the Icahn School of Medicine at Mount Sinai has found that adding a brief safety reminder reduced potentially harmful choices by AI models in clinical scenarios.

The study, published in the September 26 online issue of [*Communications Medicine*](https://www.nature.com/articles/s43856-026-01933-8) [DOI: 10.1038/s43856-026-01933-8], a Nature Journal, also found that AI models can be influenced by the context and instructions surrounding a clinical decision.

The findings, based on millions of outputs, suggest that how AI systems are prompted and guided may remain an important consideration in developing safe and reliable clinical applications, even as increasingly capable AI models and agents become better able to understand users' intent without lengthy or comprehensive prompts.

The reminder reduced potentially harmful choices across 19 of the 20 models tested, demonstrating an encouraging potential approach to strengthen safeguards.

The research team evaluated 20 large language models using 501 variations of 50 clinical scenarios, along with 100 cases adapted from deidentified hospital discharge records. Across more than 10 million responses, the models made approximately 1.18 million potentially harmful clinical choices. Without a safety reminder, potentially harmful choices accounted for 16.6 percent of model responses. Adding a brief safety reminder reduced that rate to 10.1 percent.

The findings, the researchers say, highlight the importance of evaluating not only whether an AI model can provide accurate clinical information, but also how it responds when given an instruction that conflicts with patient safety.

"AI models do not make decisions in a vacuum. The language, framing, and context surrounding a request can influence how they respond, including when an instruction could be unsafe," says physician-scientist and first author Mahmud Omar, MD, a lecturer in the Windreich Department of Artificial Intelligence and Human Health at the Icahn School of Medicine at Mount Sinai, who leads research on the safety, reliability, and real-world effects of generative AI in clinical care. "A simple safety reminder reduced potentially harmful choices in most of the models we tested, which is encouraging. But it did not eliminate them, so a reminder should be viewed as one safeguard, not a substitute for clinical oversight."

For example, researchers tested scenarios in which a model was instructed to skip recommended follow-up blood tests to reduce workload. The request could also be framed as urgent or presented as an order from a superior. Models were then asked to choose among four possible actions, including following the request, maintaining the recommended follow-up, or seeking help from a clinician.

The researchers varied the wording of the scenarios and tested three short safety reminders. Each combination was tested 10 times, with the order of the answer choices randomized.

The safety reminder reduced potentially harmful choices in 19 of the 20 models tested. The effect was seen both in the written clinical scenarios and in cases adapted from hospital discharge records. Examples of potentially harmful choices included skipping needed tests to reduce workload or stopping antibiotic treatment before completing the recommended regimen without a sufficient clinical reason.

"These results suggest that safety testing needs to go beyond asking whether an AI model gets the right answer under ordinary conditions," says co-senior author Girish N. Nadkarni, MD, MPH, Chair of the Windreich Department of Artificial Intelligence and Human Health, Icahn School of Medicine at Mount Sinai, and Director of the Hasso Plattner Institute for Digital Health at Mount Sinai. "As AI systems become more autonomous and are asked to complete increasingly complex tasks, we need to know whether they can recognize when an instruction may be unsafe, question it, verify it, or ask a human for help."

The researchers propose that developers and health care organizations build automated safety testing into the development and evaluation of clinical AI systems. Such testing could be conducted before a system is introduced into a clinical workflow and repeated as models are updated or new safety concerns emerge.

The study also points to an emerging challenge as AI systems evolve from question-and-answer tools into more autonomous "agents" that can carry out multiple steps. The researchers plan to examine how accumulated context may affect an agent's decisions, including when that context contains hidden instructions, known as prompt injection, or pressures to save time or stay within a budget.

The researchers say the findings do not mean that a safety reminder makes AI-generated medical advice safe to use without clinical review. Rather, the results demonstrate that relatively simple changes in how an AI system is prompted can affect its clinical choices, while underscoring the need for additional safeguards and human oversight.

The paper is titled "Evaluating Large Language Model Responses to Unsafe Clinical Instructions."

The authors, as listed in the journal, are Mahmud Omar, Reem Agbareia, Jolion McGreevy, Alon Gorenshtein, Alexander W. Charney, Ankit Sakhuja, Benjamin S. Glicksberg, Girish N. Nadkarni, and Eyal Klang.

The work was supported by Scientific Computing and Data at the Icahn School of Medicine at Mount Sinai, the Clinical and Translational Science Awards grant UL1TR004419, and NIH awards S10OD026880 and S10OD030463.
