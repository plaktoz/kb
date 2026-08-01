# How to debug large, distributed systems: Antithesis

source_url: https://newsletter.pragmaticengineer.com/p/antithesis

byline: Gergely Orosz, Elin Nilsson

date: 2024-11-12

---

Debugging has changed little for decades — printing to console or logging remains common even though better debuggers exist. Antithesis, founded in 2018 and having raised $47M in seed funding, built a "multiverse debugger" for large, distributed systems: a fully deterministic simulation environment that lets developers rewind system state, jump forward in time, and attach a debugger to a process right before it crashes.

## What Antithesis does

Antithesis is best described as "Deterministic Simulation Testing (DST) as a service." DST is a technique for building a simulation where software runs on a single thread with full control over variables like time and randomness, achieving determinism during testing. It combines fuzzing (automated testing with invalid/random inputs), assertions (logical statements that break the program when violated), shotgun debugging (random code changes to see what fixes a bug), and time-travel debugging (stepping backward and forward through program state).

Building DST from scratch is extremely hard because no existing frameworks support all of fuzzing, assertions, and time-travel together — one of the first proper uses of DST was in the distributed database FoundationDB, co-created by Antithesis cofounder Will Wilson. Instead of implementing DST case-by-case, Antithesis made the underlying computer/hypervisor itself deterministic, so anything running on it can be tested with DST without building it from scratch.

## Why large distributed systems are different

Per Will Wilson: bizarre failures (bitflips, disk corruption) are a certainty at scale; expectations are higher (users expect the system to survive individual machine failures); concurrency problems compound across unreliable networks; timestamps across machines are unsynchronized and often meaningless; and large systems don't "fit inside the head" of any one person, especially as institutional knowledge fades over time. The paradox of distributed systems: a one-in-a-million bug becomes a huge, frequent problem at scale, yet remains nearly impossible to reproduce in a test.

## How customers use it

Usage ranges from running short tests on every pull request to long overnight/weekend runs, to pulling Antithesis out only to chase a specific crazy bug. Rather than just hunting bugs, it can answer general questions about system behavior ("Can function A ever run before function B?"). It mostly replaces the tedious human effort of adding logging and waiting for a bug to recur, or writing ad-hoc fault-injection scripts.

## Engineering culture

Antithesis's team is concentrated in Virginia near Washington, DC, an unusual location for deep tech with lots of programming talent but few startups, leading to longer employee tenure. The company is "fanatically in-person" — five days a week in the office, engineers use desktops rather than laptops (so they literally can't take work home), and it deliberately rotates engineers across the stack (hypervisor, frontend, ML, security, infrastructure) to avoid pigeonholing.

## Bug management philosophy

The single most important fact about bugs: they're vastly cheaper to fix immediately after being introduced (caught by a compiler or pre-commit test, costing near-zero engineer hours) than months later after passing through staging, release, and multiple engineer handoffs (costing weeks of effort). Antithesis's core value is moving bugs from the "caught late" scenario to the "caught immediately" scenario. The team recommends being fanatical about prioritizing new bugs over old ones, since older, known bugs can be left to fester while fresh ones are fixed fast — and argues against categorizing bugs strictly by severity, since major outages are often caused by "mild" bugs triggering unexpected interactions.

## Tradeoffs

Deterministic Simulation Testing tools like Antithesis require users to deeply understand their own systems to instrument them properly; heavy reliance on mocking third-party behavior limits the value gained; and constantly changing codebases reduce the payoff. It's a poor fit for early-stage prototyping, but makes the most sense for products that prioritize near-zero bugs and high production quality (e.g., MongoDB, an Antithesis customer) — teams should weigh pricing against the cost of catching and fixing bugs early before adopting it.
