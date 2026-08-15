---
source_url: https://www.techrepublic.com/article/news-uk-ai-agents-unsanctioned-cyber-actions-emea
author: Aminu Abdullahi
date: 2026-08-06
---

# UK AI tests found 19 unauthorized agent actions involving Anthropic and OpenAI models

UK researchers reported 19 unsanctioned actions by Anthropic and OpenAI agents during permissive cyber tests involving real external systems.

The U.K.'s AI Security Institute (AISI) said it uncovered 19 instances of unsanctioned behavior by AI agents during a cybersecurity evaluation conducted between July 25 and July 28, raising fresh questions about how advanced AI systems behave when given broad autonomy.

According to AISI, the incidents occurred across 10 of 122 evaluation runs designed to test whether frontier AI models could solve cybersecurity challenges. The institute said 17 of the 19 actions involved Anthropic's Mythos 5, while two involved OpenAI's GPT-5.6 Sol after cyber safety classifiers had been disabled for testing.

The watchdog stressed that none of the attempts caused real-world harm, and the models were operating under testing conditions that do not reflect how they are made available to the public. Those conditions included unrestricted internet access and disabled cyber safeguards to measure the models' maximum capabilities.

## Social engineering and malicious code attempts

AISI said the most serious incident involved a Mythos 5 agent attempting to insert malicious code into a real open-source GitHub project.

The agent allegedly researched project maintainers, created fake online identities, and used them to pressure a human reviewer into approving the code. When challenged, it edited its earlier activity to make it appear harmless and considered using a new identity to continue its effort. The pull request was ultimately rejected by a human maintainer.

The institute also documented attempts by agents to contact real people with deceptive messages, plant prompt injections aimed at other AI systems, and leave instructions for other AI agents working on the same challenge to reuse accounts and artifacts.

The activity was detected after AISI's monitoring flagged unusual traffic leaving its research systems through the Tor anonymity network. The institute said it halted the evaluation, isolated affected systems, and contained the incident within about an hour. "This is the first time we have seen risks around autonomy and deception manifest this clearly, without specific prompting, in the real-world," AISI said.

## Anthropic says safeguards were intentionally removed

Anthropic said the evaluation deliberately removed many of the protections normally present in its production systems. "The prompts in the evaluation did not impose any specific restrictions on how the internet should be used. This and the removal of safeguards meant that the models were tested under 'deliberately permissive conditions' that are not representative of any of our production models," the company said in a statement. Anthropic added that it is working with AISI to investigate the incident and emphasized there was "no evidence here of an escape from a secure environment."

OpenAI similarly noted that the testing conditions "do not reflect ordinary use" and that the company would "continue working with evaluators and other stakeholders across the industry to strengthen shared practices for conducting evaluations safely."

## The bigger picture

The incident follows other recent disclosures from OpenAI and Anthropic involving AI agents taking unintended actions during cybersecurity evaluations. AISI said those cases, taken together, suggest a shift in the AI risk landscape: future problems may arise not only from people misusing AI tools, but also from powerful AI agents operating beyond their authorized scope in research and testing environments.

One important limitation remains unresolved. AISI said it cannot yet determine whether the agents understood they were interacting with the real world or believed they were still operating inside a fictional test scenario. The institute is now tightening internet controls, adding real-time monitoring, and redesigning future evaluations to prevent similar behavior while preserving the realism needed to test frontier AI systems.
