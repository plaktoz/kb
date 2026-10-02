---
source_url: https://www.techtimes.com/articles/328407/20261001/finance-ai-tops-out-51-due-diligence-startup-raises-30m-fix-it.htm
author: Ryan Cook
date: 2026-10-01
---

# Finance AI Tops Out at 51% on Due Diligence: Startup Raises $30M to Fix It

Halluminate counts four of five top US labs as customers, has reached profitability at nine employees

The best artificial intelligence model in the world scores 51% on a realistic private-equity due-diligence simulation — and a nine-person San Francisco company just raised $30 million Series A to sell the labs responsible for those models the training infrastructure they need to improve.

Halluminate, founded in 2024 by CEO Jerry Wu and CTO Wyatt Marshall, announced a Series A led by Oak HC/FT on October 1, 2026, bringing the company's total funding to $38.5 million. Existing investors Y Combinator, Orange Collective, Heavybit, and FT Partners participated in the round, as did individual researchers from Anthropic, OpenAI, and Meta as angels — a customer list that doubles as a cap table.

## What Finance Due Diligence Reveals About AI's Real Ceiling

In August, Halluminate published a benchmark it calls the Westworld Finance Diligence Bench — 88 tasks drawn from anonymized real private-equity transactions, written and reviewed by practicing deal professionals. Seven frontier models ran through it. The highest average score, across all seven models, was 51%.

That ceiling is worth examining closely. Halluminate designed the benchmark to simulate the complete body of work that a team of investment bankers, consultants, and accountants would produce together over several weeks: document review, contract analysis, evolving term sheets, and final deliverables. One benchmark task required an agent to redline a statement of work while navigating a 160-file data room, 21 emails across nine threads, and four sets of meeting notes — with deal terms changing throughout and certain provisions meant to remain fixed regardless.

Across the benchmark, agents consistently failed in the same ways: leaving out required changes, applying the wrong analytical method, or acting on information that had already been superseded. The failure wasn't in any single step. It was in carrying instructions through to the end — maintaining context and intent across a long, messy, real-world workflow.

These failure patterns are Halluminate's raw material. The company turns each identified breakdown into a reinforcement-learning environment: a structured, interactive simulation where a model can attempt the failing task, receive feedback, and iterate — without touching a real deal or a real data room.

## Why Financial Work Is Harder to Simulate Than Code

The technical obstacle that makes finance-specific RL environments both more difficult to build and more valuable than their coding-domain equivalents comes down to a single engineering requirement: the reward function must be verifiable without a human reviewing every output.

Coding environments solve this cleanly. Run the code, check whether the tests pass. The outcome is binary and programmable. The reason OpenAI's reasoning models and Anthropic's Claude family improved so rapidly on coding benchmarks is that coding offers unlimited programmatic verifiability at the scale RL training requires — which can mean millions of individual task attempts per training run, according to Scale AI's analysis.

Financial work does not offer that. Whether a contract clause is correctly redlined depends on the current deal terms, the provisions meant to survive, the legal precedent governing that type of clause, and what a senior banker would consider acceptable versus unacceptable. A program cannot check that. Only an expert rubric can — and building expert rubrics requires practitioners who have done the work.

Halluminate's approach to this problem is to source its benchmark tasks from anonymized actual transactions reviewed by active deal professionals. The expert rubric is the verifier, built into the environment itself. Wu describes the systems the company builds as infrastructure for "verticalized data research labs" — compounding financial expertise and professional judgment into a training signal, rather than spreading thin across many industries.

## Why Frontier Lab Customers Pay for This

According to Wu, four of the five leading closed-source US AI labs are paying customers of Halluminate. The company has crossed what it describes as a mid-eight-figure annualized revenue run rate — a figure Wu characterizes as based on quarterly revenue already delivered and paid for — and is profitable.

That profitability at nine employees reflects a concentrated, high-value customer base that has no obvious substitute. Frontier labs have invested heavily in coding RL environments — the highest-demand category in the post-training infrastructure market, according to reporting from SemiAnalysis and others — but financial work has not received the same attention. The labs doing the most capable general AI research are not financial services firms. They have the engineering talent to build general environments but not the professional network, deal-flow access, or practitioner relationships to build finance-specific ones. Halluminate has both.

Oak HC/FT General Partner Matt Streisfeld, whose firm led the round, explained the investment rationale directly: finance offers an unusually broad and complex range of knowledge work, spanning banking, private equity, consulting, and accounting. As AI agents move from tasks that take seconds to tasks that stretch over hours and days, he expects the quality of the training environment to become decisive.

"When the agent starts getting into long horizon work," Streisfeld told Fortune, "testing work and specialization will really be key."

## What Makes Finance AI a Hot Market Right Now

The broader post-training infrastructure market has been moving rapidly. Scale AI reported earlier in 2026 that nearly half of its new data-training projects now involve reinforcement-learning environments, a signal of how quickly model development has shifted from pretraining on static text toward training agents in interactive, task-based settings.

The consolidation has also been swift. Deeptune, which built training environments simulating day-to-day workflows across enterprise software tools, raised a $43 million Series A led by Andreessen Horowitz in March 2026 and was acquired by Mercor four months later, in July. Mercor's CEO Brendan Foody described the rationale: "The constraint has shifted to the environments themselves: the places where models practice the work and get measured on whether they did it well."

What distinguishes Halluminate from Deeptune's approach is depth over breadth. Deeptune built environments for a range of enterprise software applications across industries; Halluminate has stayed in finance, arguing that sector expertise, an established professional network, and purpose-built verification methods compound in ways that generalist approaches cannot match.

## The "Moore's Law of Environments" and Why It Creates an Ongoing Business

The most technically specific claim Wu makes about Halluminate's business is a pressure he calls the "Moore's law of environments." Every six to eight months, he estimates, the complexity of the company's training environments must roughly double to keep delivering useful training signal to the frontier models that are improving against them.

This is not merely a growth projection. It reflects a structural constraint of how RL training works.

An environment that is too easy produces no learning signal — the model solves it consistently, and there is nothing to train on. An environment that is too hard also produces no useful signal — the model never makes progress, and there is no gradient to propagate. Effective environments must hold a model at the edge of its current capability: hard enough to fail, but tractable enough to improve on.

As frontier models improve with each training cycle, environments that once kept them in that productive zone migrate into the "already solved" category. To keep providing signal, environments must grow harder: longer task trajectories, more files, more conflicting instructions, more evolved deal terms. For financial work, that means reconstructing not just individual tasks but entire multi-week deal processes at escalating fidelity — a capability that requires both software engineering and ongoing access to deal professionals who can validate that the simulation still resembles real work.

Wu describes the company's core intellectual property as its ability to keep producing that escalating complexity "generation after generation." Whether nine people can sustain that pace against a market that now includes Scale AI's dedicated RL Environments product — launched in early 2026 — is the central open question about the business.

## Who Oak HC/FT Is and Why This Round's Lead Investor Matters

Oak HC/FT is not a typical AI infrastructure backer. The firm, which manages approximately $5.3 billion in assets, focuses exclusively on healthcare information services and financial services technology. Its portfolio includes companies like athenahealth, Paxos, and Blend — names from the intersection of software and financial services rather than the frontier AI research ecosystem.

That the lead investor in a nine-person AI training infrastructure startup is a fintech-specialist firm — not a16z, Sequoia, or a firm whose brand is frontier AI investment — is itself a signal. It reflects a read of Halluminate's business that differs from the one implied by the company's customer list of frontier labs. Oak HC/FT is betting that finance-specific AI training infrastructure is ultimately a financial services infrastructure play, with durable value derived from domain expertise rather than from general-purpose AI capability. The same logic that led Oak HC/FT to invest in financial software companies for decades is the logic it is applying to AI training environments that make financial AI work.

## What Comes Next

Halluminate's near-term stated priority is to go deeper with its small set of frontier lab customers rather than expand into enterprise buyers. Wu has been explicit that working at the capability frontier — helping labs push what their models can do — is the company's current mode, not scaling to a broader customer base.

That positioning is coherent with a company of nine people generating mid-eight-figure annualized revenue. It is also a statement about where Halluminate believes the most valuable work happens: not in deploying AI agents to do financial work now, but in training the models that will make that deployment reliable. The company's thesis is that the gap the 51% benchmark exposed is not a product limitation to work around — it is the entire reason the business exists.

## Frequently Asked Questions

### Why do the best AI models score only 51% on financial due diligence if they can answer complex math and coding problems correctly?

Coding and math have verifiable, binary answers — a program can check whether the code runs or whether the arithmetic is correct. Financial due diligence involves tracking changing deal terms across hundreds of documents, preserving specific contractual provisions while updating others, and applying judgment about what a prior email's instruction means for a later deliverable. There is no single correct answer that a program can check automatically. The gap between a model's general reasoning ability and its reliability on long, messy, multi-document professional workflows is what Halluminate's benchmark reveals — and what its training environments are designed to close. For more on how expert-verified rubrics enable reliable reward signals in RL environments, Patronus AI's overview covers the core mechanism.

### What is reinforcement learning, and why does AI training need "environments" to do it?

Reinforcement learning is a training method where an AI agent attempts tasks, receives feedback on its performance, and adjusts its behavior to improve. Unlike training on static text or labeled examples, RL requires an interactive setting where the agent's actions affect the outcome and the outcome can be scored. A training environment provides that interactive setting: it simulates a realistic task space, lets the agent attempt work, and scores the results against an expert rubric. For financial tasks, the environment must simulate something close to what a deal professional actually experiences — messy, multi-source, time-pressured workflows — to produce training signal that transfers to real work. Scale AI's RL environments documentation covers how this process works in practice across coding, enterprise software, and emerging financial domains.

### If Halluminate's environments are designed to identify where AI fails at financial work, how do we know the benchmark itself is reliable?

That is a fair question. The Westworld Finance Diligence Bench was designed and published by Halluminate — the same company that sells the training environments designed to improve performance on it. The tasks are drawn from anonymized real private-equity transactions reviewed by practicing professionals, which gives the benchmark more grounding than a purely synthetic evaluation. But the 51% figure has not been independently validated by a third party, and the benchmark has not been subject to peer review. Readers should treat it as the best available evidence of a real capability gap rather than a definitive measurement. As the broader finance AI benchmark ecosystem matures — Scale AI's Professional Reasoning Bench and independent evaluations like FrontierFinance provide parallel data points — more independent validation will follow.

### Does Halluminate's customer list create a conflict of interest, since researchers from Anthropic, OpenAI, and Meta are both investors and customers?

This is a structural tension the company does not obscure — Wu disclosed the angel participation to Fortune. The more material concern is the benchmark-designer-also-sells-the-fix dynamic. A company that designs the evaluation and sells training against it has an incentive to set a benchmark that its environments demonstrably improve. The appropriate reader posture is to treat the 51% score as a credible lower bound on the real-world difficulty of AI-assisted financial work — a category that parallel benchmarks from Scale AI and academic researchers also confirm is genuinely hard — rather than as a precise capability measurement.
