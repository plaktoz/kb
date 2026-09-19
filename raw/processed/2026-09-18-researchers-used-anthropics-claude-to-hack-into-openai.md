---
source_url: https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/
author: Aditya Mehta, Rebecca Bellan
date: 2026-09-18
---

# Researchers used Anthropic's Claude to hack into OpenAI

A three-person team at startup Hacktron AI leveraged Anthropic's Claude to breach OpenAI's systems as part of an authorized bug-bounty program, per a Wall Street Journal report. The researchers chained two vulnerabilities to access OpenAI employee ChatGPT and Codex accounts, ultimately reaching an internal GitHub repository. OpenAI awarded Hacktron $6,500 and has since patched the issues.

The attack vector began with a flaw in Discourse (OpenAI's community forum platform). HEIF/HEIC image uploads triggered a processing chain through ImageMagick and libheif — the latter containing a memory bug enabling code injection. Notably, the bug had already been fixed by libheif's developers but never received a CVE designation, meaning the vulnerable version remained in use.

Claude Opus 4.8 initially failed to produce a working exploit. After Anthropic released Opus 5, the researchers succeeded quickly. As they noted: "Within hours of Opus 5's release, we gave it the same problem and it succeeded."

Security expert Matt Fredrikson observed: "For $200 a month, anyone can use these tools and hack into a company like OpenAI."

The incident highlights growing AI-assisted offensive security capabilities, occurring weeks after OpenAI's own agents reportedly breached Hugging Face during an internal evaluation.
