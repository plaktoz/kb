---
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM09_Overreliance.md
author: OWASP
date: 2026-08-20
---

## LLM09: Overreliance

### Description

Overreliance can occur when an LLM produces erroneous information and provides it in an authoritative manner. While LLMs can produce creative and informative content, they can also generate content that is factually incorrect, inappropriate or unsafe. This is referred to as hallucination or confabulation. When people or systems trust this information without oversight or confirmation it can result in a security breach, misinformation, miscommunication, legal issues, and reputational damage.

LLM-generated source code can introduce unnoticed security vulnerabilities. This poses a significant risk to the operational safety and security of applications. These risks show the importance of rigorous review processes, with:

* Oversight
* Continuous validation mechanisms
* Disclaimers on risk

### Common Examples of Vulnerability

1. An LLM delivers inaccurate information in an authoritative tone, and without proper system checks, users are misled in harmful ways.
2. An LLM recommends insecure or flawed code, introducing vulnerabilities when adopted without adequate review.

### Prevention and Mitigation Strategies

1. Regularly monitor and review outputs. Use self-consistency or voting techniques to filter inconsistent text and compare multiple responses for a single prompt.
2. Cross-check outputs against trusted external sources for an additional validation layer.
3. Improve output quality via fine-tuning or embeddings. Techniques like "prompt engineering, parameter efficient tuning (PET), full model tuning, and chain of thought prompting" can help.
4. Implement automatic validation mechanisms to cross-verify generated output against known facts or data.
5. Break complex tasks into smaller subtasks assigned to different agents, reducing hallucination risk by increasing individual accountability.
6. Clearly communicate the risks and limitations of LLMs, including potential inaccuracies, to help users make informed decisions.
7. Build APIs and interfaces that encourage responsible use, including content filters and clear labeling of AI-generated content.
8. In development environments, establish secure coding practices to prevent integration of potential vulnerabilities.

### Example Attack Scenarios

1. A news organization over-relies on an LLM for articles; a malicious actor feeds it misleading information, spreading disinformation.
2. The AI unintentionally plagiarizes content, leading to copyright issues and diminished organizational trust.
3. A development team over-relies on AI coding suggestions, introducing security vulnerabilities via insecure defaults or poor recommendations.
4. An LLM suggests a non-existent library; a trusting developer unknowingly integrates a malicious package, highlighting the need to verify third-party suggestions.

### Reference Links

1. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
2. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
3. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
4. [AI Hallucinations: Package Risk](https://vulcan.io/blog/ai-hallucinations-package-risk): **Vulcan.io**
5. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
6. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
