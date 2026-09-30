---
source_url: https://x.ai/news/team-bots
author: xAI
date: 2026-09-28
---

# Team Bots: AI coworkers that learn from your team

Today we're launching Team Bots, Grok Bots that work and learn alongside your team. Give one access to the files, apps, and expertise it needs, then share it so everyone can work from the same context.

At SpaceXAI, Team Bots brief account teams each morning, coordinate engineering projects, and answer data questions across the company. Here's how they work, how we use them, and how to build one for your own workflow.

## Team Bots bring context, tools, and memory together

You build a Team Bot around a role or workflow your team shares. Everyone gets access to the same Bot and its expertise, while still being able to work with it individually.

Every Team Bot brings together four things that help it do its job:

- **Context** gives it the relevant files, instructions, and skills, from brand guides to internal documentation.
- **Plugins** let it work in applications such as Salesforce, Notion, and GitHub. They can be connected by each person or configured for the whole team.
- **Credentials** let it securely access third-party APIs that do not have a plugin.
- **Memories** help it retain what it learns and improve at its role over time.

Although the Bot is shared, each person's conversations with it remain private. The Bot keeps separate context and memories for each user while drawing on the skills shared across the team.

Teams can also collaborate with a Team Bot in Slack. Each Team Bot has its own handle, so you can invite it to a channel where everyone can ask questions, contribute context, and see its responses.

## Team Bots take on work across SpaceXAI

At SpaceXAI, we're using Team Bots in some of our most context-heavy workflows. Here are four examples from Sales and Customer Success, Product and Engineering, Marketing, and Data Analytics.

### Sales and Customer Success

At SpaceXAI, every major sales account has a dedicated Team Bot. Each Bot is shared by the account executive, customer success manager, solutions architect, and sales leader.

Every night, the Bot reviews company news, recent Gong calls, Notion docs, and relevant Slack threads. Each morning, it posts a briefing in the account's Slack channel with what changed and what each person should do next, including drafts tailored to their role.

Throughout the day, account teams use the Bot in Slack to assess strategy, check its thinking against account data, and plan next steps. The Bot remembers the decisions teams make and builds rich context over time. As people rotate on and off the account, it becomes the system of record and can quickly bring new team members up to speed.

Harper, an insurance company serving small businesses, built a Team Bot to identify customers with lapsed policies and help them reinstate their coverage, reducing manual work for its team and recovering substantial savings for customers. Harper CEO Dakotah Rice said the team built the bot in 24 hours to automate a process that previously required manually checking every customer through three platforms, saving customers over $120,000 from hundreds of policies.

### Product and Engineering

The Engineering Team Bot works from a project's Slack channel and connects to Notion, Linear, Hex, Datadog, and Cursor. It follows product decisions, triages bug reports, creates tickets, and launches Cloud Agents to handle well-defined fixes.

SpaceXAI taught the Bot its shipping process through skills — how to handle PR reviews, when to ask the team for help, and what evidence a change needs before it is complete. It coordinates work across tools and agents, then reports progress and blockers in Slack. SpaceXAI used this setup while building Team Bots itself: the Bot steered a Cursor Project that orchestrated hundreds of Cloud Agents, helping a five-person team ship more than 100 PRs a day and launch Team Bots in a few weeks.

### Marketing

Large marketing teams spend considerable time keeping their brand, messaging, and voice consistent. SpaceXAI built Marketing Bot to make that work easier, giving it access to brand guidelines, blog posts, and social copy. Whenever someone shares a draft for approval in Slack, it reviews the work against voice and latest messaging, letting regional teams get feedback without waiting for an approval cycle at HQ.

For website and SEO changes, Marketing Bot carries the work from review to launch, posting a preview link in Slack for final sign-off once a content update passes review.

### Data Analytics

The data analytics team built Data Bot so anyone at SpaceXAI can get answers without waiting for an analyst or setting up warehouse access. Data Bot uses shared, read-only credentials to query approved tables in Databricks, and also connects to Datadog, Hex, and Statsig to investigate questions and present results.

The team gave Data Bot its existing library of skills for working with more than 45,000 tables, including instructions for finding the right data, analyzing feature usage for fraud, following chart standards, and safely updating company-wide dashboards. Data Bot also remembers corrections to its queries, so what it learns from one person improves the answers it gives everyone.

## Get started with Team Bots

Team Bots is available today in public beta on Teams and Enterprise plans, with pre-built Team Bots available for sales, product management, marketing, and data analytics.
