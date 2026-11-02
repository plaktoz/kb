---
source_url: https://www.techedt.com/google-joins-openai-and-anthropic-in-adopting-new-ai-scraping-controls
author: Joby Jean
date: 2026-10-31
---

# Google joins OpenAI and Anthropic in adopting new AI scraping controls

Google, OpenAI, Anthropic and Microsoft back a shared robots.txt standard giving publishers greater control over AI training crawlers.

Google has joined OpenAI, Anthropic and Microsoft in committing to a new standard that gives website publishers greater control over how their content is collected for generative artificial intelligence (AI) training.

The companies have agreed to support a proposed robots.txt directive currently under consideration by the Internet Engineering Task Force (IETF), an organisation that develops internet standards. Kevin Kelley, an Anthropic technical lead for standards, wrote the proposal, which aims to establish a common way for publishers to communicate their preferences to AI companies.

The move addresses growing concerns among website owners about how their articles, images and other online materials are collected and used to develop AI models. Under the proposed system, publishers can use a shared instruction rather than creating separate restrictions for individual AI providers.

## New robots.txt directive aims to simplify AI scraping restrictions

Website owners have traditionally relied on the robots.txt file to tell automated crawlers what they can access. However, controlling AI-related scraping has become more complicated as different companies operate their own web crawlers, each with separate identification names and rules.

For example, publishers who want to prevent several AI companies from collecting their content must identify the relevant crawlers individually and add specific instructions for each one. This process can become time-consuming, particularly for websites that want to manage access across multiple AI providers.

Kelley’s proposal aims to address this problem by introducing a common user-agent directive specifically for AI training. Instead of maintaining separate restrictions for every company, publishers can use a single section in their robots.txt files to communicate whether automated systems may collect their material for AI training.

The proposed system also gives publishers more flexibility over which parts of their websites can be accessed. Website operators can use the directive to block AI training crawlers across their content while allowing access to selected pages or sections. For example, a publisher could permit the collection of materials from a press kit while restricting access to its original news articles.

OpenAI and Google have both highlighted the potential benefits of a shared approach, particularly as the number of AI companies collecting publicly available online information continues to grow. A common standard could make it easier for website operators to communicate their preferences without understanding the individual requirements of every AI provider.

## Publishers can restrict AI training without blocking search indexing

The proposed directive is designed specifically to control the collection of website content for AI training. It does not automatically prevent all forms of crawling or stop a website’s pages from appearing in search engine results.

This distinction is important because website owners may want their content to remain discoverable through traditional search engines while preventing AI companies from using the same material to train their models. The new instructions aim to separate these activities rather than treat all automated website access the same way.

Google, for example, will interpret the directive as a restriction applying to its Google-Extended user agent. This crawler collects website content that may be used to improve and train Google’s Gemini AI models. Blocking this specific user agent through the new instruction will not automatically remove a website from Google’s search index.

The approach gives publishers a more targeted way to manage how their online material is used. They can keep information available to people through search engines while expressing a separate preference about whether AI training systems should collect it.

However, the proposal also has an important limitation. The new directive cannot reverse scraping activities that have already taken place. If an AI company previously accessed and collected content from a website, adding the new instruction will not remove that material from its existing datasets or automatically affect models already trained on it.

Instead, the standard is intended to prevent future collection by participating companies. Its effectiveness will therefore depend on AI providers implementing the directive and respecting the instructions published by website owners.

This means publishers may gain greater control over future data collection. Still, the change will not fully address concerns about how previously collected online content has been used to develop generative AI systems.

## Major AI companies set different implementation timelines

Anthropic has already begun supporting the proposed directive, making it the first participating company to introduce compatibility with the new standard.

Other companies have announced plans to follow, although their implementation schedules differ. OpenAI has committed to introducing support in the coming months, while Google expects to adopt the directive in early 2027.

Microsoft has also confirmed its participation, with support scheduled to begin on 1 February 2027. These commitments indicate growing cooperation among major technology companies around establishing a more consistent approach to website scraping for AI development.

Google, OpenAI, Anthropic, and Microsoft are significant participants because their services and AI models rely on large amounts of information collected from online sources. A shared standard could make it easier for publishers to communicate their preferences across several major AI platforms without repeatedly updating their website configurations.

However, the proposal’s success will depend on how widely it is adopted beyond the companies that have already announced their support. Smaller AI developers and other organisations that collect online content would also need to recognise and respect the directive for publishers to benefit from a more consistent system.

The proposal remains part of the IETF’s standards process, and its wider adoption will be an important factor in determining how effectively it changes the relationship between website publishers and AI developers.

For website owners, the initiative represents a step towards greater transparency and control over the use of their online material. While it cannot address past scraping, the shared directive could offer a simpler way to set boundaries on how publicly accessible content is used in future AI training.
