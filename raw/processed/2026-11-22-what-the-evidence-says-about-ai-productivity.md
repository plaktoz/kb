---
source_url: https://medium.com/@milesk_33/what-the-evidence-says-about-ai-productivity-cfcfff9bb38f
author: milesk_33
date: 2026-11-22
---

# What the Evidence Says About AI Productivity

In early 2025, a group of experienced open-source developers predicted AI tools would make them 24% faster. METR measured them on 246 real tasks in their own repositories and found they took 19% longer with AI. After the study, the same developers still believed AI had sped them up by 20%.

That result became the most quoted number in the AI productivity debate, and it's already out of date. Twenty months later, Stack Overflow's 2026 survey finds 62% of developers view AI favorably at work, rising to 71% among daily users. Microsoft's own telemetry shows engineers merging more code with coding agents. Meanwhile, nearly 9 in 10 executives in a large 2026 survey say AI hasn't changed their company's productivity yet.

I ship AI products for a living, so I care less about who wins this argument than about what to put on the dashboard. I spent the last few weeks reading the 2025 and 2026 research, surveys, company filings, and the forum threads where practitioners argue about all of it. The evidence turns out to be more consistent than the debate suggests, once you notice what each study is actually measuring.

## Why the studies seem to disagree

Most of the contradiction disappears when you sort the evidence by level. Studies of a single task find large gains. Studies of whole companies and labor markets find small or no effects so far. Self-reports run highest of all.

None of these levels is the "real" answer. Each one answers a different question, and the gaps between them are where the interesting work is.

## Developers: Real speed, real review costs

The developer evidence has moved quickly. METR's February 2026 follow-up with 57 developers and more than 800 tasks now points toward a speed-up: about 18% less task time for returning developers and 4% less for new ones. Both confidence intervals still cross zero, and METR calls the data unreliable for an unusual reason: a growing share of developers refused to work on tasks without AI at all. A separate METR survey from May 2026 found technical workers self-reporting a median 3x speed change, and METR itself warns that people have overestimated AI's effect on their time before.

The strongest new measured evidence comes from Microsoft. A July 2026 study of its rollout of Claude Code and GitHub Copilot CLI, covering tens of thousands of engineers, found adopters merged 24% more pull requests than they would have otherwise. Engineers using the tools five or more days a week saw a 50% lift. Earlier field experiments across Microsoft, Accenture, and a Fortune 100 firm found 26% more completed tasks, with most of the gain going to newer developers: 27% to 39% for juniors and 8% to 13% for seniors.

Throughput is half the picture, though. Engineering-analytics data from 2026 shows the cost side:

An open-source study presented at MSR 2026 adds a time dimension. Repositories that adopted coding agents saw commits rise 36%, but projects already using AI editors saw early gains fade by six months, while code complexity rose 39%. These are vendor and observational numbers with real caveats, and they point the same way: AI moves the bottleneck from writing code to reviewing and trusting it.

Developers say the same thing in their own words. The 2026 Stack Overflow survey finds 48% trust AI output when they can easily validate it, and only 16% trust it for most tasks short of important decisions. If you're adopting agents on your team, the workflow and review practices matter as much as the tool.

## Knowledge workers: Big gains inside the frontier

Outside software, the best field evidence tells a similar story with a sharper edge. In a study of 5,179 customer support agents, an AI assistant raised issues resolved per hour by 14% on average and by 34% for novices, with minimal effect on the most experienced agents.

A field experiment with 758 BCG consultants found what the authors called a "jagged technological frontier." On tasks inside AI's capability, consultants completed 12.2% more tasks, 25.1% faster, at over 40% higher quality. On a task deliberately designed to fall outside it, consultants using AI were 19 percentage points less likely to reach the correct answer. The same tool that lifted performance on one kind of task lowered it on another.

Self-reported time savings are real and modest at scale. The UK government's trial of Microsoft 365 Copilot with 20,000 civil servants reported 26 minutes saved per day, self-reported and without a control group. HMRC's randomized arm found 2% to 3% of the working week. Across the whole US workforce, the St. Louis Fed's tracker puts time saved with generative AI at 2.17% of all work hours in Q2 2026, up from 1.81% a year earlier.

There's a cost on the receiving end too. A Stanford and BetterUp survey of 1,150 workers, published in Harvard Business Review, found 40% had received "workslop" in the past month: AI-generated work that looks polished but doesn't move the task forward. Each instance took about two hours to deal with. Teams that want AI output to be trustworthy by default need guardrails and review norms designed in.

## Companies and the economy: The gains haven't added up yet

At the firm level, the numbers drop sharply. A February 2026 NBER survey of nearly 6,000 executives in the US, UK, Germany, and Australia found 69% of firms actively use AI, and about 9 in 10 executives report no impact on employment or productivity over the past three years. They expect a 1.4% productivity gain over the next three.

Labor market data is similarly quiet on the headline measures. Danish researchers linking adoption surveys to administrative records found precise null effects on earnings and recorded hours, ruling out effects larger than 2% two years after ChatGPT. The one place a clear signal shows up is entry-level hiring: Stanford's "Canaries in the Coal Mine" paper, updated in August 2026, finds employment of 22-to-25-year-olds in AI-exposed jobs is 19% below the trend of less-exposed peers. The authors call it descriptive and early.

Why would individual gains fail to show up in company results? Economists have a name for this from the computer era, the productivity paradox, and the usual explanation is that new tools pay off only after organizations redesign the work around them. The 2026 data supports that reading. Microsoft's Work Trend Index attributes 67% of reported AI impact to organizational factors and 32% to individual mindset. BCG's 2026 Applied AI Index finds only 7.5% of firms qualify as "future-built," up from 5% a year earlier, and those firms report 2.4x the revenue growth of laggards.

Redesigning work around AI usually means moving from individual prompting to structured, multi-step workflows with clear handoffs and checks.

## AI-powered products: The case study everyone cites

Klarna is the example on every slide, usually told as a reversal. The filings tell a more nuanced story. In February 2024, Klarna said its AI assistant handled two-thirds of customer service chats in its first month, the work of about 700 agents. In May 2025, its CEO told Bloomberg that cost had been "a too predominant evaluation factor," resulting in "lower quality," and Klarna began piloting remote human agents. Then its 2025 annual report showed the assistant handling 80% of chats, doing the work of more than 850 agents, saving about $59 million, with Klarna reporting no drop in customer satisfaction.

The accurate summary is a hybrid model. AI handles routine volume; humans stay available for the cases that need them. Customers want exactly that arrangement: in a 2026 Gartner survey of 3,566 customers, 50% said generative AI made interactions easier, and 87% said companies using it must still offer a way to reach a human.

The stakes for getting product answers right are also clear. A Canadian tribunal held Air Canada liable for refund information its chatbot invented, rejecting the argument that the chatbot was a separate entity. And Gartner predicts over 40% of agentic AI projects will be canceled by the end of 2027 over cost, unclear value, or weak risk controls.

A support product's usefulness depends heavily on how well it's grounded in the company's own policies and data, which is the problem retrieval systems solve.

## What practitioners are arguing about

The 2026 forum debates have shifted. Few high-engagement threads still claim AI coding is useless, and plenty of experienced engineers describe real gains, including a Hacker News thread from a 60-year-old developer about Claude Code reigniting their passion that drew more than 1,000 points. The arguments have moved downstream:

- **Verification is the new bottleneck:** An "Ask HN" on AI-assisted coding at work collected over 600 replies describing gains on scripts and cleanup and extra work in production code. Addy Osmani calls the result "comprehension debt", and Simon Willison writes that the work shifts to testing, design, and review.
- **Parallel agents have a ceiling:** In a thread on running coding agents in parallel, many found validation and merge conflicts kept the useful number of simultaneous agents to two or three.
- **Maintainers absorb the volume:** Open-source maintainers describe a flood of low-effort AI contributions that shifts cost onto reviewers.
- **The junior pipeline worries people:** Threads debate whether AI is eroding how juniors learn, while others argue interest rates and remote work explain weak entry-level hiring better than AI does.
- **Measurement is getting gamed:** Reporting on token counts appearing in performance reviews drew sharp criticism, since usage volume says little about output.

Most of these accounts are anecdotes, and they line up closely with the measured data above.

## What the teams seeing gains do differently

Put the evidence together, and a few patterns hold across levels.

1. **They measure outcomes and keep self-reports in their place:** People consistently feel more productive than the clock shows. Track merged and shipped work, lead time, and customer outcomes, and use surveys for experience and sentiment.
2. **They track quality next to speed:** Throughput gains arrive with more bugs, incidents, and review load. Put rework, incident rate, and review time on the same dashboard as velocity, so you see both sides at once.
3. **They invest in verification:** Charity Majors argues that trust has to move from line-by-line review to tests, evals, and telemetry. That shift is what lets review keep up with generation.
4. **They know where the frontier is:** Gains concentrate on well-defined tasks and among newer workers, and performance drops on tasks outside the model's strength. Map which work belongs where before mandating usage.
5. **They redesign the workflow:** Organizational factors account for most reported impact. Individual adoption without process change tends to show up as personal time savings that never reach the company's numbers.

## The honest answer

Does AI make us more productive? At the task level, the evidence says yes, often substantially, especially for less experienced people and well-defined work. At the company level, the evidence says not yet for most firms, with a small and growing group pulling ahead. Both findings can be true at once, and the distance between them is mostly organizational.

That's good news for anyone building with these tools, because the part that separates the leaders is the part you control: how you measure, how you verify, and how you change the work around the model. The productivity is there to be captured. The evidence just says it takes more than a license to capture it.
