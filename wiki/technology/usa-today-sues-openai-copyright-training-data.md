---
type: literature-note
source_url: https://www.unite.ai/usa-today-sues-openai-over-copyrighted-news-content-in-ai-training/
author: Sophie Denar
tags: [openai, copyright-lawsuit, ai-training-data, journalism]
date_consumed: 2026-10-10
---

## Summary

USA TODAY Co. and 19 affiliated newspapers sued OpenAI in the Southern District of New York on October 8, 2026, alleging GPT models were trained on hundreds of thousands of their copyrighted articles without authorization and that OpenAI stripped copyright management information before ingesting the content. The suit, seeking over $250 million and joining the consolidated OpenAI copyright litigation in the same court, cites specific dataset figures (WebText, C4) and internal admissions from OpenAI and Microsoft executives that the models memorize and can regurgitate training text.

## Core Concepts

- **[[USA Today Co. v. OpenAI Foundation]]**: Copyright lawsuit filed October 8, 2026 by USA TODAY Co. (formerly Gannett) covering 19 publications including USA TODAY, the Detroit Free Press, and The Arizona Republic, against [[OpenAI]]'s corporate entities.
- **[[Copyright Management Information]] stripping**: The complaint alleges OpenAI used programs to remove ownership/rights data attached to published works before training, exposing it to statutory damages up to $25,000 per violation on top of up to $150,000 per willful infringement.
- **Training corpus evidence**: The complaint cites 160,000+ entries from the plaintiffs' domains in [[WebText]] (used for GPT-2), 83,266 from usatoday.com alone, and 122 million+ tokens from the plaintiffs' domains in [[C4]], the filtered Common Crawl subset used in GPT-3's training mix.
- **Project Taxi / Project Mango**: Alleged Microsoft–OpenAI data-sharing initiatives, where Microsoft supplied OpenAI its Bing Index and ran a dedicated crawler on OpenAI's behalf, both referenced in overlapping copyright litigation including [[NYT v. OpenAI]].
- **GPT output substitution**: The complaint reproduces GPT-5.6 outputs it says paraphrase and structurally mirror original articles, arguing OpenAI post-trained models to summarize rather than link to articles — echoing an OpenAI Head of ChatGPT quote that there's "no good reason to click" through once an answer is given.
- **Internal admissions**: Quotes from OpenAI co-founder [[Greg Brockman]] and a VP of Research ("We train our networks to memorize the training data — that's their objective") are used to argue OpenAI understood its models retained and could reproduce copyrighted text.

## Key Takeaways

- **Damages sought**: Over $250 million, with statutory caps of $150,000 per willful infringement and $25,000 per CMI violation.
- **Scale alleged**: 160,000+ WebText entries and 122M+ C4 tokens from the plaintiffs' 19 publications.
- **Models named**: GPT-1 through GPT-6.1 and GPT-OSS, across Instant, Thinking, mini, nano, and Pro variants.
- **Related litigation**: Filed as related to the consolidated OpenAI copyright cases already pending in SDNY.
- **Selective filtering alleged**: OpenAI's output filters reportedly only suppressed content from entities that had already sued, called an "accidental cover-up" internally.
- **Business context**: Complaint cites OpenAI's October 2025 recapitalization (~$130B value) and 900M+ weekly ChatGPT users as of March 2026.

## 🧠 First Principles & Mental Models

- **[[Externalities]]**: As in the parallel NYT v. OpenAI case, the complaint alleges OpenAI captured the value of publisher journalism (training data, substitutive summaries) while pushing the cost — lost traffic and subscription revenue — onto the newspapers that produced it.

## 🃏 Review Questions

**Q1**: What is the central allegation in USA Today Co.'s lawsuit against OpenAI?
**A**: That OpenAI trained its GPT models on hundreds of thousands of the plaintiffs' copyrighted articles without authorization, stripped copyright management information, and that its outputs now substitute for the original journalism.

**Q2**: What specific dataset evidence does the complaint cite to show scale of alleged copying?
**A**: It cites 160,000+ entries from the plaintiffs' domains in the WebText corpus used for GPT-2 (83,266 from usatoday.com alone) and more than 122 million tokens from the plaintiffs' domains in the C4 dataset used in GPT-3's training mix.

**Q3**: Why does the complaint argue OpenAI's summarization behavior harms publishers commercially?
**A**: It alleges OpenAI post-trained models to produce substitute summaries instead of linking out, quoting OpenAI's own Head of ChatGPT that users have "no good reason to click" through, which removes readers' incentive to visit or subscribe to the original sources.
