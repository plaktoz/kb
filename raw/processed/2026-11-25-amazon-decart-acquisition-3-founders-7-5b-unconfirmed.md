---
source_url: https://shattered.io/decart-amazon-three-founders-chip-portability-7-5-billion-unconfirmed-nov-25/
author: Marcus Bell
date: 2026-11-25
---

# Amazon Decart Acquisition: 3 Founders, $7.5B Unconfirmed

Amazon announced on November 23, 2026 that it signed an agreement to purchase the proprietary technology behind Decart Optimization Stack, known as DOS. The software helps AI systems run faster and move between chips from Nvidia, Amazon and Google. Three people Amazon identifies as Decart co-founders come with it, along with Decart’s AI researchers and engineers. That makes the Amazon Decart acquisition less a software purchase than a bet on a small group of people who know how to squeeze more work out of silicon.

The headline number is the part nobody can pin down. Secondary reports attribute a figure of about $7.5 billion to Bloomberg, but Amazon’s own announcement names no price. We covered the first-day facts in our earlier report on Amazon buying Decart’s AI chip software. This piece takes a different angle. It asks what the deal says about where AI value is moving, why a chip-portability layer commands attention, and which claims about the transaction are still unproven.

Reuters called the deal Amazon’s latest AI talent grab. That framing matters, because it places the Decart Optimization Stack inside a pattern in which large technology companies buy small teams to lock down scarce engineering skills. Whether you read it as a product deal or a hiring deal changes how you judge the reported price, the risk to rivals and the odds that customers see any benefit.


## What Amazon Confirmed on November 23

Start with what sits on the record. Amazon said it signed an agreement to buy the proprietary technology behind Decart Optimization Stack. It also said it will bring Dean Leitersdorf, Moshe Shalev and Orian Leitersdorf to Amazon. Amazon identifies all three as Decart AI co-founders. Dean Leitersdorf serves as Decart’s chief executive. The researchers and engineers who built the stack move over with them.

Amazon framed the purpose in operational terms. According to the company, the technology is meant to help optimize inference and custom-silicon performance, so customers can train and run AI models faster and at lower cost. Peter DeSantis, Amazon’s senior vice president of foundational AI models, custom silicon and quantum computing, put the thesis in one line. He said every leap forward in AI starts with getting more out of every chip.

That sentence is the strategic core of the announcement. It does not promise a new model, a new chatbot or a new consumer product. It promises efficiency, which is the lever that cloud providers pull when demand for compute outruns supply. Amazon sells compute, so any software that raises output per chip raises the value of every chip it already owns or plans to build.

The confirmed scope is also narrower than some headlines suggest. Amazon bought technology and people. The announcement does not say Amazon bought all of Decart, and it does not say Decart’s AI models are part of the package. Readers should treat both of those claims as open until Amazon or Decart says otherwise.

## The $7.5 Billion Figure: Reported, Not Confirmed

The $7.5 billion number travels fast because it is large and easy to repeat. Its footing is weaker than its reach. Secondary reports attribute the figure to Bloomberg, which cited a person familiar with the matter. Reuters and Amazon’s announcement, in the material available at the time of writing, do not confirm a price. GeekWire’s headline carries the same hedge by calling it a reported $7.5 billion.

One more data point gives the number context. Reuters, citing PitchBook data, said the reported price sits well above Decart’s most recent valuation of nearly $4 billion. If the reported figure holds, Amazon would pay a steep premium over the last private mark. Premiums of that size usually reflect one of three things. The buyer may see strategic scarcity, the buyer may be paying for retention of key people, or the structure may include payments that depend on future milestones.

We cannot say which of those applies, because no outlet has published deal terms. That gap is why this article avoids treating $7.5 billion as a settled price. Deals structured around technology plus hires often carry retention packages, and a headline value can bundle several moving parts. Until Amazon discloses terms or a regulatory filing surfaces, the number stays a report.

For anyone writing about the deal, the safe wording is simple. Say Bloomberg reported about $7.5 billion, say Amazon did not disclose a price, and say the prior valuation of nearly $4 billion comes from PitchBook data cited by Reuters. Each clause names its owner. None of them asks the reader to take a number on faith.

## What Decart Optimization Stack Does

Decart Optimization Stack sits between an AI model and the hardware that runs it. Amazon describes it as software that helps AI systems run faster and switch among chips from Nvidia, Amazon and Google. Reports describe the same job from the developer side. The stack tunes a model for a given accelerator, helps move a workload from one chip family to another and improves how efficiently the hardware gets used.

Think of it as translation plus tuning. A model written and tested on one kind of chip does not automatically run well on another. Engineers spend weeks rewriting low-level code, adjusting memory use and testing speed. A layer that automates part of that work shortens the path from a trained model to a cheap, fast deployment. That is the practical meaning of Amazon’s phrase about running models at lower cost.

## Inference is the cost center

Amazon named inference in its stated goal, and the choice makes sense. Training a model happens once per version. Serving it happens every time a user sends a prompt. As products reach more users, serving cost becomes the line item that finance teams watch. A few percentage points of efficiency, applied across a very large fleet of chips, can matter more than a flashy model launch. We have no verified figure for how much DOS improves efficiency, so this article does not offer one.

## Custom silicon needs software to compete

Amazon also named custom-silicon performance. Custom chips only win customers when the software around them feels as easy as the incumbent option. A chip that costs less but takes months to port a model onto rarely wins a procurement fight. Optimization software narrows that gap, which explains why Amazon wants it in-house rather than renting it.

## Why Chip Portability Is Worth Paying For

The ability to switch among chips is the feature that makes the Amazon Decart acquisition strategically interesting. Buyers of AI compute face supply limits, price swings and vendor dependence. A model locked to one chip family inherits all three problems. A model that can move between Nvidia, Amazon and Google hardware gives its owner leverage in every contract negotiation.

Portability changes bargaining power in two directions. Customers gain options, and the cloud provider that owns the portability layer gains a way to steer workloads toward its own silicon. Amazon plainly wants the second outcome. If DOS makes it easy to run a model on Trainium, more customers will try Trainium. If DOS also keeps working on other vendors’ chips, customers keep trusting the tool, and Amazon keeps the relationship.

That tension is worth watching. A neutral tool is more attractive to customers than a tool that favors its owner. Amazon has not said whether DOS will keep supporting rival chips at full strength after the deal closes. Its announcement describes the stack as helping systems switch among Nvidia, Amazon and Google chips, but that is a description of the current product, not a commitment about the roadmap.

The cloud market has already shown how much money rides on inference economics. Our report on AWS Lambda gaining GPU support at the EC2 price plus a 9.75% fee shows Amazon packaging accelerator access into easier, pay-as-you-go products. A strong optimization layer fits that direction, because it lowers the skill needed to get good performance from the hardware underneath.

## Trainium, Inferentia and the Annapurna Labs Connection

Amazon built Trainium for training and Inferentia for inference. GeekWire reported that the technology is expected to support both chip families, and that the transaction runs through Annapurna Labs, Amazon’s chip organization. Amazon also said Decart has worked with it since 2025 to deliver strong performance on Trainium. That history matters. Amazon did not buy a stranger. It bought a team it already knew.

A prior working relationship lowers integration risk in one way and raises a different question in another. Integration risk falls because engineers on both sides already share code paths, test setups and performance targets. The new question is why a close partner needed to be owned. Partnerships can end, change terms or serve competitors. Ownership removes that uncertainty, and it keeps the team’s next breakthrough from landing on a rival’s chips first.

TechCrunch’s headline ties the deal to Amazon preparing to sell Trainium chips. The wording points to a commercial shift. Selling chips, as opposed to renting them inside AWS, would put Amazon in front of buyers who expect a mature software path. Optimization tooling is the kind of asset that makes that pitch credible. We have not seen Amazon confirm a chip-sales program in the material reviewed here, so treat that link as TechCrunch’s framing.

## The Three Founders and the Talent Grab Pattern

Reuters described the deal as Amazon’s latest AI talent grab, and the founders’ inclusion shows why. Amazon is not licensing the code and leaving the authors behind. It is hiring the people who wrote it. In fast-moving AI infrastructure, code ages quickly and the knowledge in people’s heads ages slowly. A team that understands why a kernel runs fast on one chip is worth more than a snapshot of that kernel.

The structure also protects the buyer against a common failure. Acquired software often decays once its authors leave. By bringing Dean Leitersdorf, Moshe Shalev and Orian Leitersdorf aboard, along with Decart’s researchers and engineers, Amazon keeps the maintainers close to the product. For a tool that has to track every new chip generation, maintenance is the whole game.

Reports say Decart started in 2023 in Israel. If so, the company went from founding to a reported multibillion-dollar outcome in about three years. That speed shows how much the market pays for people who sit at the hardware and software boundary. Skills in this area are rare, and every large buyer of AI chips competes for them.

The talent angle also explains the open questions about scope. Buyers who want people often leave the rest of the company behind, which can mean the remaining business shrinks or pivots. Amazon has not said what happens to Decart’s other activities. That silence is a reason to hold back on any claim that the deal covers the whole company.

## Market Impact: Nvidia, Google and Cloud Rivals

No stock-price move tied to the announcement appears in our verified material, so this section deals in direction rather than percentages. The most direct effect lands on chip vendors whose silicon DOS supports. A tool that eases switching among Nvidia, Amazon and Google chips reduces the stickiness any one vendor enjoys. Nvidia’s strength has long rested on software familiarity as much as hardware speed, and anything that weakens that familiarity helps challengers.

Cloud rivals face a different problem. If Amazon turns DOS into a built-in feature of AWS, customers get a faster path to cheaper inference without leaving the platform. Rivals must then match the capability, buy their own, or accept a gap. Buying becomes harder as targets shrink. Few independent teams specialize in this layer, and Amazon just removed one from the market.

Spending data shows why the layer matters. Dell lifted its annual forecast as its AI backlog reached $132.3 billion, which we detailed in our report on Dell’s $202 billion outlook. When customers commit that much money to AI hardware, a few points of extra efficiency turn into real savings. Software that raises utilization competes for the same budget line as the hardware itself.

Smaller chip designers should pay attention too. Startups that build alternative accelerators depend on software stacks to make their hardware usable. Our coverage of Axelera’s reported $400 million funding talks and of Marlowe’s $277 million seed round shows investors still back Nvidia alternatives. Each of those companies must solve the same software problem, and Amazon just paid to solve it for itself.

## Confirmed, Reported and Unconfirmed: A Status Table

The table below separates what Amazon has said from what outlets report and from what remains unverified. It uses only the announcement and the attributed reports described above.

Two rows carry the most risk for readers. The price and the scope both appear in casual summaries as if they were settled, and neither is. Writers who copy a headline figure without its attribution turn a report into a fact, and that is how weak numbers harden into accepted history.

## Competitive Comparison: Who Controls the Software Layer

The deal reflects a broader contest over who owns the layer between models and chips. Chip makers want developers tied to their tools. Cloud providers want customers tied to their platforms. Independent tooling companies want to stay neutral and sell to everyone. Amazon just moved one of the neutral players into its own camp.

The outlets covering the story frame it in slightly different ways, and the differences show which angle each cares about. The table compares those framings using each outlet’s own headline.

Read together, the framings show a consistent core. Everyone agrees Amazon gets technology and a team. They split on emphasis. Amazon talks about customer benefit, TechCrunch about chip sales, Reuters about talent. The Next Web and Silicon Republic both lead with the pairing of technology and people, which matches what Amazon confirmed.

## Historical Context: Software Decides Which Chips Win

Hardware contests rarely end on raw speed. They end on which platform developers find easiest to build on. Nvidia’s lead in AI accelerators grew alongside a software ecosystem that engineers learned early and kept using. Rivals that shipped capable chips without equal tooling often struggled to win large customers, because the cost of rewriting code outweighed the savings on hardware.

Amazon learned a version of this lesson with its own silicon. Building Trainium and Inferentia solved the hardware half. The software half needs constant work as models change shape and new chip generations arrive. The 2025 collaboration with Decart, which Amazon described as aimed at strong Trainium performance, was an early sign that Amazon saw the gap and wanted outside help closing it.

The acquisition path also echoes earlier cycles in which dominant firms bought the specialists who stood between their products and wider adoption. The pattern repeats because the logic is stable. When one narrow skill gates a large market, the largest participant eventually buys it rather than rents it.

Financing history adds another layer. Frontier AI labs now raise enormous sums, and a growing share of that money goes to compute. Our analysis of Anthropic’s $93.5 billion IPO and how AI labs pay for compute explains why. When compute eats that much capital, tools that stretch each chip further stop being a nice extra and start being a core cost-control measure.

## What Developers and Customers Should Watch

For engineers who run AI workloads on AWS, the practical question is when DOS shows up in a form they can use. Amazon has not published a delivery date, a pricing model or an integration plan in the material reviewed. The announcement describes intent, so customers should wait for documentation before changing any procurement plan.

Teams that use Decart’s tooling today face a more urgent set of questions. Will existing agreements continue, will support for non-Amazon chips stay at its current level, and will the stack remain available to customers who do not use AWS? None of those answers appears in the confirmed facts. Anyone who depends on the software should ask their account contact directly and get answers in writing.

Buyers weighing Trainium against Nvidia hardware should also keep their expectations grounded. Better tooling lowers the switching cost, but it does not erase it. Real workloads vary, and published claims about speedups need testing on your own models. Run a pilot, measure cost per request and compare against your current setup before committing.

## Five Predictions for the Decart Deal

These are analyst-style judgments, not reported facts. Each rests on the confirmed details above and on how similar deals have tended to play out.

Amazon will fold DOS into AWS tooling. The stated goal is faster, cheaper training and inference for customers, and the cleanest delivery route is a built-in feature of the platform.

Neutrality will become a talking point. Customers will press Amazon on whether DOS keeps working well on Nvidia and Google chips. Expect Amazon to answer with reassurance, and expect skeptics to test it.

Rivals will buy or build comparable layers. Cloud providers and chip designers that lack an equivalent will look at the few remaining independent teams in this space.

Price details will surface through filings or leaks. A reported figure this large rarely stays vague forever, and the gap between Bloomberg’s number and Amazon’s silence will draw more reporting.

Talent deals will keep structuring around technology plus people. The pairing protects the buyer from knowledge loss and gives founders a clean exit, so other large firms will copy it.

The weakest of the five is the second, because it depends on a corporate choice Amazon has not yet made. The strongest is the first, since it follows directly from the purpose Amazon stated in its own announcement.

## The Takeaway on the Amazon Decart Acquisition

The Amazon Decart acquisition confirms one thing and leaves several things open. Amazon has the technology behind Decart Optimization Stack, and it has the three founders plus Decart’s researchers and engineers. The reported $7.5 billion price, the scope of the purchase and the fate of Decart’s models all lack confirmation from Amazon.

The strategic logic holds up without the price. AI demand keeps stretching chip supply, and software that squeezes more output from each chip improves the economics of every data center that adopts it. Amazon chose to own that capability instead of renting it, and it chose to hire the people who built it. Watch for deal terms, a product timeline and any statement on support for rival chips. Those three items will show whether this deal opens the AI chip market or tilts it toward AWS.

## Frequently Asked Questions

## What did Amazon announce about Decart?

On November 23, 2026, Amazon announced an agreement to purchase the proprietary technology behind Decart Optimization Stack. It will also bring Decart’s three named co-founders, along with its AI researchers and engineers, to Amazon.

## How much is Amazon paying for Decart’s technology?

Amazon has not disclosed a price. Secondary reports attribute a figure of about $7.5 billion to Bloomberg, which cited a person familiar with the matter. Treat that number as reported and unconfirmed.

## What is Decart Optimization Stack?

It is software built to help AI systems run faster and switch among chips from Nvidia, Amazon and Google. Amazon says it should improve inference and custom-silicon performance, so customers can train and run models faster and at lower cost.

## Is Amazon buying all of Decart?

That is not confirmed. Amazon’s announcement covers the proprietary technology behind the stack and the named founders and team. It does not say the deal includes Decart’s entire business or its AI models.

## Who are the Decart founders joining Amazon?

Amazon named Dean Leitersdorf, Moshe Shalev and Orian Leitersdorf as Decart AI co-founders joining the company. Dean Leitersdorf is Decart’s chief executive.

## How does this connect to Trainium and Inferentia?

GeekWire reported that the technology is expected to support Amazon’s Trainium training chips and Inferentia inference chips, with the transaction running through Annapurna Labs. Amazon also said Decart has worked with it since 2025 on strong Trainium performance.

## Will DOS still work with Nvidia and Google chips?

Amazon has not said. The current product helps systems switch among Nvidia, Amazon and Google chips, but the announcement makes no commitment about future support. Customers who rely on multi-vendor setups should ask Amazon for written answers.

## Why do reports call this an AI talent grab?

Reuters used that phrase because Amazon is hiring the founders, researchers and engineers along with buying the technology. Large technology companies increasingly buy small AI teams to secure scarce engineering skills.
