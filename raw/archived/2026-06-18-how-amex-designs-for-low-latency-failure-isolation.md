# How Amex Designs for Low-Latency Failure Isolation

source_url: https://techscoop.substack.com/p/how-amex-designs-for-low-latency

---

**By Hey Maria — Jun 18, 2026**

### A deep dive into American Express' cell-based payments architecture, how it reduces blast radius, supports failover, keeps latency predictable, and what platform teams can learn from it.

Payment systems live in one of the least forgiving areas of distributed systems engineering. A delayed transaction is not just a slow API call. It can become an abandoned cart, a stranded customer, a failed merchant sale, a fraud review problem, or a reconciliation issue downstream.

That is why the American Express engineering article on cell-based architecture is important. It is not simply another cloud-native modernization story. It is a case study in how one of the world's major payments ecosystems thinks about failure before failure happens.

The core idea is simple but powerful: do not build one giant platform where every service, database, configuration dependency, and routing path can become part of the same failure domain. Instead, divide the platform into independent cells. Each cell has the services, databases, DNS, observability, and supporting infrastructure needed to process transactions locally. If one cell fails, the failure stays inside that cell. Other cells continue processing.

That sounds obvious until you apply it to payments, where strong consistency, duplicate prevention, partner routing, issuer communication, fraud checks, merchant rules, currency data, and compliance constraints all collide in the same transaction path.

The real lesson from Amex's architecture is this: in mission-critical payments, resiliency is not achieved by adding retries after the fact. Resiliency is achieved by making failure boundaries a first-class architectural primitive.

## What Cell-Based Architecture Means in Payments

A cell is an isolated, independently deployable unit of the system. It contains the microservices, databases, local routing, local observability, and supporting services needed to process a subset of transactions.

In a traditional distributed system, services may be split into microservices but still share central databases, global caches, global configuration services, centralized observability pipelines, and cross-region synchronous dependencies. That can look distributed on a diagram while still behaving like a tightly coupled system during failure.

Cell-based architecture goes further. It asks a stricter question:

**Can this part of the platform continue operating if another cell, region, database cluster, logging system, or downstream dependency is degraded?**

In the Amex design, each cell is a failure domain. It does not span multiple regions. It has local services and local databases. It does not depend on synchronous cross-cell calls during transaction processing. The Global Transaction Router, or GTR, decides where transactions should go and enforces the boundaries between cells.

The important detail is not that there are multiple boxes. The important detail is that the boxes do not depend on one another synchronously in the critical path.

That is the difference between a distributed system and a resilient distributed system.

## Payment Failures Are Business Failures

In most consumer software, a degraded experience may mean a page loads slowly or a user refreshes. In payments, the consequences are immediate.

A card authorization flow has to answer a business-critical question in milliseconds: should this transaction be approved, declined, routed, retried, enriched, or stopped?

The platform must handle high-volume traffic, unpredictable demand spikes, partner-specific routing, fraud checks, issuer connectivity, currency rules, merchant category data, settlement implications, and retry behavior. It must do all of this while keeping latency predictable.

Real payment outages show how fragile the ecosystem can become when a central dependency fails.

In 2018, Visa experienced a major service disruption in Europe caused by the failure of a switch in one of its data centers. Visa later told the UK Parliament that 91% of UK cardholder transactions processed normally during the incident, but 9% failed on the first attempt, with peak disruption periods where average failure rates reached 35%. That is a powerful example of why blast-radius reduction matters. A single infrastructure fault can become visible to merchants and consumers across countries.

Square's 2023 outage offers another lesson. Square said the incident was caused by DNS servers, and noted that without DNS, Square products, internal tools, and services could not communicate. In 2025, Square and Cash App also reported a system-wide disruption tied to a security certificate validation problem that temporarily prevented payment systems from communicating properly with databases.

These are not exotic failures. They are the ordinary enemies of distributed systems: DNS, certificates, routing, configuration, data-center networking, overloaded dependencies, and retries. Cell-based architecture is a way of designing so that ordinary failures do not become total platform failures.

## Principle 1: Reduce Blast Radius Before You Optimize Everything Else

The primary benefit of cell-based architecture is reducing blast radius. If one cell fails, only the traffic assigned to that cell should be affected. The rest of the platform should continue operating.

This is similar to the bulkhead principle in ships: divide the ship into watertight compartments so that damage in one section does not sink the entire vessel.

In payments architecture, blast radius can be defined across several dimensions:

- percentage of total transactions affected
- number of partners or markets affected
- number of card members affected
- number of merchants affected
- number of payment types affected
- operational surface area involved in recovery
- risk of duplicate or inconsistent transactions

The key insight is that blast radius is not only a technical metric. It is a business metric.

A 100% outage is a crisis. A 5% cell-specific degradation is still serious, but it is diagnosable, containable, and recoverable. It gives operators options.

This is why Amex's cell design allows a cell to be taken out of rotation manually or automatically. A bad cell does not need to be fixed in-place while still serving critical traffic. The router can drain it, shift traffic away, and later validate it under partial load before full recovery.

This is a major operational advantage. Instead of asking "How do we repair the plane while flying it?" the architecture asks "How do we route around the damaged engine while keeping the plane airborne?"

## Principle 2: Keep Data Local Unless There Is a Strong Reason Not To

Payments need data. Some of that data is static or semi-static: currency rates, merchant category codes, product rules, market configuration, partner metadata, and routing tables. Other data is dynamic and transaction-specific.

Amex handles these differently.

For static and semi-static data, the platform replicates reference data into each cell ahead of time. That means transaction processing does not have to pause for a synchronous lookup to a central system of record. This avoids cache-miss latency and keeps the critical path local.

This is one of the most important patterns in low-latency systems: move work out of the critical path before the user request arrives.

For dynamic data, the answer is not "replicate everything everywhere instantly." That is expensive, slow, and often impossible when strict consistency is needed. Instead, Amex uses deterministic routing. The Global Transaction Router sends the transaction to the cell where the required dynamic state is already authoritative or available.

That is a deeper lesson for platform teams: locality is not only about where services run. It is about where the correct state lives.

A payment system cannot simply spray requests randomly across cells if the transaction requires strongly consistent state. The router must understand enough about the transaction to make a safe routing decision, without becoming the owner of the payment business logic itself.

That balance is subtle. The router needs just enough protocol awareness to route correctly. But it must not become a giant payment-processing brain at the edge, because then the router itself becomes too complex and too risky.

## Principle 3: The Router Becomes the Control Point, But Must Stay Thin

The Global Transaction Router is the heart of the architecture. It manages connectivity, routing, failover, traffic shaping, and cell selection.

But the most important design choice is what it does not do.

It does not own full payment processing logic. It does not become a dependency-heavy orchestration system. It does not call every downstream service to make a decision. It sits at the edge, understands enough of the transaction to route it, and keeps the critical path thin.

This matters because edge systems amplify failure. If the router depends on too many systems, then every one of those dependencies becomes a possible payments outage.

That is why Amex describes minimal dependencies at the edge. If logging fails, the router should not block transaction processing. If configuration service access is temporarily unavailable, the router should continue with the last known good configuration. Logs, metrics, and configuration updates are important, but they should not be allowed to stop payment authorization.

This is closely related to the concept of static stability: the data plane should keep doing useful work even if the control plane is impaired. In payments, this is not a nice-to-have. It is the difference between degraded operations and a full outage.

## Principle 4: Do Not Let Cells Talk to Each Other Freely

One of the most dangerous failure modes in microservice platforms is dependency creep.

At first, every service is cleanly isolated. Then one team needs a "temporary" cross-cell call. Another team adds a shared service. A third team introduces a central cache. A fourth team depends on a global observability or configuration API. Eventually, a platform that looks cell-based becomes a distributed monolith.

Amex avoids this by enforcing ingress and egress through the Global Transaction Router. Transactions enter a cell through the router. If rerouting is needed, the transaction goes back through the router. Cells do not casually talk to each other.

This may create duplicated services. It may feel inefficient compared with a shared implementation. But duplication is sometimes the cost of true resilience.

For platform teams, this is one of the hardest cultural lessons. Engineers are trained to remove duplication. But in high-availability systems, the wrong kind of reuse can create the wrong kind of coupling.

Shared code is usually fine. Shared runtime dependencies are risky. Shared databases across cells are dangerous. Synchronous shared services in the transaction path can defeat the entire point of cell-based architecture.

## Principle 5: Restart Failed Transactions, But Respect the Point of No Return

One of the most interesting parts of the Amex design is how it handles in-flight failures.

If a downstream service inside a cell begins to fail, an orchestrator detects the failure, halts processing, and sends the transaction back to the Global Transaction Router. The router can then restart processing in another healthy cell.

The word "restart" matters.

Amex does not attempt to resume partially processed transactions across cells. Resuming would require shared state, cross-cell coordination, and complex consistency guarantees. Instead, the transaction restarts with the original transaction data.

This works only because the system respects a "point of no return." Before a transaction is sent to an external system such as an issuer, it can be safely rerouted and restarted. After that point, rerouting could create duplicates or inconsistent downstream effects.

This is where idempotency becomes essential. For payment types where retries and reroutes can happen, each transaction needs a stable unique identifier. Downstream systems can use that identifier to detect and suppress duplicates.

Stripe's public API documentation provides a well-known example of this principle: idempotency keys allow clients to safely retry mutating requests without accidentally creating a second object or performing an operation twice. The same concept becomes even more important in payment networks, where retries are unavoidable but duplicate charges are unacceptable.

The practical lesson is clear: you cannot build safe failover unless you design transaction identity first.

## Cell-Based Architecture Is Also a Deployment Strategy

The article frames cells as a resiliency architecture, but the related Amex migration story shows another advantage: cells make migration safer.

Amex used the Global Transaction Router to migrate payment traffic gradually. It introduced the router into the transaction path, used shadow traffic to validate the new payment processing platform, then applied canary routing by moving small percentages of live traffic to the new system. It started with small percentages, monitored health, and rolled back when needed.

This is a major insight for platform engineers: the same architecture that helps you survive incidents also helps you ship change safely.

A cell-based platform allows teams to:

- deploy to one cell before all cells
- compare cell-level performance
- run canaries by market, partner, or payment type
- drain cells for maintenance
- validate recovering cells under partial load
- roll back traffic without rolling back code everywhere
- isolate bad deploys to a smaller user or transaction population

This turns migration from a big-bang event into a routing decision.

For payments, that matters because modernization is dangerous. Legacy systems often contain decades of edge cases. Rebuilding everything before moving traffic is slow and risky. Moving everything at once is also risky. A router-controlled migration path creates a middle ground: prove the new system with real traffic, but only within controlled boundaries.

## Observability Must Be Local First, Global Second

A common mistake in distributed platforms is making observability centralized too early.

Global dashboards are useful for executives, incident commanders, and fleet-wide analysis. But if every service must synchronously publish logs, metrics, or traces to a central platform during the transaction path, observability can become a dependency.

Amex avoids this by publishing logs, metrics, and traces to observability components localized within each cell first. Global aggregation still exists, but it happens asynchronously.

This means an observability failure does not take down payment processing. It only reduces visibility in the affected scope.

The deeper lesson: observability should help you survive incidents, not participate in causing them.

Local-first observability also improves incident response. If Cell B is unhealthy, engineers should be able to inspect Cell B without depending entirely on a global telemetry path that may itself be delayed, overloaded, or unavailable.

## Additional Insight: The Hard Part Is Not Creating Cells. It Is Keeping Them Independent.

Many engineering teams can draw a cell-based architecture diagram. Few can keep it true over years of product growth.

The difficult questions are operational:

- Can each cell be deployed independently?
- Can each cell process transactions if the global config service is unavailable?
- Can a cell lose logging without losing payment processing?
- Can a cell be drained without asking every downstream team for coordination?
- Can a bad deploy be stopped at one cell?
- Can dynamic state be routed deterministically?
- Can a transaction be retried safely without duplicate side effects?
- Can the platform prove through testing that a cell failure does not cascade?

Without these answers, "cell-based architecture" becomes branding. With these answers, it becomes a resilience strategy.

## What Tech Leaders Should Take Away

The American Express architecture is valuable because it shows what mature resiliency looks like in a high-stakes domain.

For CTOs, it shows that cloud-native modernization should not simply mean moving services to Kubernetes or splitting a monolith into microservices. The deeper goal is to define and enforce failure boundaries.

For SREs, it reinforces that availability is designed through locality, dependency control, load isolation, failover testing, and rollback paths — not only through dashboards and alerts.

For platform engineers, it shows why routing infrastructure can become one of the most strategic parts of the platform. The router is not just a load balancer. It is the enforcement point for resiliency, migration, failover, canarying, and operational control.

For payment engineers, it highlights a crucial principle: transaction identity, idempotency, and point-of-no-return design must be built into the architecture before failover becomes safe.

## Resiliency Is a Boundary Problem

The most important idea in cell-based architecture is not the cell. It is the boundary.

- Where does failure stop?
- Where does state live?
- Where can traffic be rerouted?
- Which dependencies are allowed in the critical path?
- Which systems can degrade without stopping payments?
- Which transactions can be restarted, and which have crossed the point of no return?

American Express' payments architecture answers these questions through independent cells, deterministic routing, local data, asynchronous replication, strict ingress and egress enforcement, idempotent transaction handling, and minimal dependencies at the edge.

That is the real lesson for the broader tech industry. Resilient systems are not built by assuming everything will work. They are built by deciding, in advance, exactly how much is allowed to break.
