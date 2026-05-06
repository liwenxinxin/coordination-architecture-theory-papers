# Predictable Cost Scaling: The Emergent Architectural Property of Composing Linear-Cost Scaling and the Determinism Contract in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the architectural property that emerges when two of the source paper's commitments — linear-cost scaling and the determinism contract — are composed, so that downstream implementers and auditors have a single citable name for the property and a single test by which their system can be checked for it. The composition is treated as a unit because it produces a property — predictable cost scaling — that neither commitment yields alone.

## Abstract

The CKS pattern's commitments interact: many of the architectural properties a CKS-coherent deployment exhibits in operation are produced not by a single commitment in isolation but by two or more commitments composed. This note formalizes one such composition. Linear-cost scaling (the cost commitment defended in §6) and the determinism contract (the reproducibility commitment distributed across §2.1, §3.1, §4.1, §6.2, §8.2, and §11.3, and assembled as a single contract in the prior derivation note) are independently load-bearing. Composed, they produce **predictable cost scaling** — the architectural pattern in which cost is *both* linear in substrate size *and* deterministic in per-operation behavior, with variance bounded to the categories of non-determinism the determinism contract explicitly permits. The note states the four operational components of the composed property, identifies what the composition forces beyond either commitment in isolation, names five anti-patterns that satisfy one commitment while violating the composition, distinguishes the composed property from four neighboring framings it is commonly conflated with, and provides an operational test built around three sharpening properties — per-operation-cost-determinism, linear-scaling, and bounded-variance. The composition is what makes capacity planning, cost-anomaly detection, and performance-regression detection operationally feasible.

## 1. Why the composition pair needs to be formalized as standalone

The source paper's six architectural commitments are individually load-bearing and individually defended. Prior derivation notes have been mounted commitment by commitment. What those notes do not formalize — and what the source paper does not collect under a single name — is the architectural property the two commitments produce *together*.

Naming the composition as standalone is necessary because the property the composition produces is a real operational capability, distinct from either commitment alone, and consequential for the kinds of deployments to which CKS is applied. Capacity-planning-feasible deployments — deployments in which an operator can predict cost growth from substrate growth and per-operation cost from operation type and substrate state — exhibit the property. Variable-cost or super-linear deployments do not, even when they satisfy one of the two commitments.

A1.06 also has a complementary composition pair with tool-agnosticism, formalized as A4.09, *scalable vendor-independence*, which addresses cost predictability across vendors. A4.13 (this note) addresses cost predictability *within* a vendor-and-deployment, by composing linear scaling with operational determinism. Together A4.09 and A4.13 cover how A1.06 composes with the two foundational commitments most directly governing its operational behavior — vendor portability and operational determinism — and close the A1.06 composition cluster within Phase A4. The load-bearing source-paper sections for the present composition are §3 and §6 (cost characteristics), §6.2 (the cost-curve distinction), §3.3 (architectural and temporal qualifiers), and §11.3 (substrate as source of truth).

## 2. The emergent property — four operational components

Predictable cost scaling is the architectural pattern in which a CKS deployment's cost behavior is predictable along both axes A1.06 and A1.10 govern. The property has four operational components.

**(a) Per-operation cost is deterministic for given substrate state.** A substrate operation of a given type, executed against a given substrate state, has a well-defined cost. Two executions of the same operation against the same substrate state yield the same cost up to bounded variance per (c) below. This component derives from the determinism contract's read-determinism and write-determinism guarantees: if substrate reads and substrate-mediated writes are deterministic in *content*, the work performed to produce that content is deterministic in *quantity* as well, modulo allowed non-determinism categories.

**(b) Linear scaling holds across substrate-size variations.** As the substrate grows, system-level cost grows linearly along the substrate-size dimension in the sense the linear-cost commitment defines. Doubling substrate size doubles storage cost and the cost of full-substrate reads; it does not double governance cost, cell-execution cost for task-scoped cells, or LLM cost per execution. This component derives directly from A1.06.

**(c) Cost variance is bounded to allowed non-determinism categories.** The determinism contract permits specific categories of non-determinism — most consequentially, LLM consultation cost variance from temperature and sampling, and timing variance that does not affect substrate-write content. Cost variance attributable to these categories is allowed and bounded; cost variance attributable to anything outside these categories indicates a composition failure. The composition does not require zero variance; it requires variance attributable to declared sources only.

**(d) Capacity planning is operationally feasible with bounded uncertainty.** The composition of (a), (b), and (c) makes capacity planning a tractable operational activity. From a forecast of substrate-size growth and a characterization of per-operation cost as a function of operation type and substrate state, an operator can forecast cost growth with uncertainty bounded by (c). This component is the operational consequence of the first three; it is the property that distinguishes CKS deployments operationally from variable-cost or super-linear systems for the planning purposes deployments most often face.

The four components are not redundant. (a) and (b) together specify the deterministic-and-linear shape; (c) specifies the variance envelope; (d) names the operational consequence. A deployment satisfying (a) and (b) but not (c) — variance present but unbounded or unattributed — fails the composition. A deployment satisfying (a), (b), and (c) but not actually used for capacity planning still exhibits the architectural property; (d) is the capability the composition affords, not a use it requires.

## 3. What the composition forces beyond either commitment alone

The composition is meaningful precisely because each commitment alone is satisfiable in ways that fail the composition.

**A1.06 alone is satisfiable by linear-scaling-with-variable-cost.** A system can satisfy linear-cost scaling — total cost grows linearly with substrate size, governance cost is not size-proportional, no superlinear regimes — while admitting per-operation cost variability across executions. Same operation against same substrate state may cost differently across runs because of caching that misses unpredictably, race conditions in concurrent reads, background-process interference, or vendor-side variability the deployment does not control. Aggregate cost still scales linearly; per-operation cost is unpredictable. A1.06 is satisfied; the composition is not.

**A1.10 alone is satisfiable by deterministic-with-super-linear-scaling.** A system can satisfy the determinism contract — every read is deterministic, every write is addressable, conflicts are preserved, the substrate is the source of truth — while admitting operations whose cost scales super-linearly with substrate size. A graph-traversal operation that visits all substrate content on every execution is deterministic (same state → same answer → same traversal → same cost) but super-linear. A1.10 is satisfied; the composition is not.

**The composition forces both.** Per-operation cost must be deterministic in the sense (a) names *and* aggregate cost must scale linearly in the sense (b) names *and* variance must be bounded in the sense (c) names. The forcing is asymmetric: the composition does not require zero variance, but it requires that whatever variance exists is attributable to allowed non-determinism categories and bounded within them. LLM consultation cost varies; the architecture acknowledges and bounds the variance per the bounded-non-determinism-within-the-mediator commitment. Timing variance from infrastructure scheduling exists; it is bounded because it does not affect substrate-write content. What the composition rules out is unbounded or unattributable variance — the kind that prevents capacity planning even when its expected value scales linearly.

## 4. Anti-patterns specific to the composition

Five anti-patterns recur in deployments that satisfy one of the two source commitments while failing the composition.

**Variable-cost operations.** Same operation against same substrate state produces materially different costs across executions, attributable to caching effects, concurrency, or hidden state rather than to any allowed non-determinism category. Violates component (a). The deployment may scale linearly in aggregate while remaining unpredictable per-operation.

**Super-linear cost spikes from non-determinism.** Occasional spikes in operation cost — order-of-magnitude departures from baseline — attributable to non-deterministic factors such as cache misses on hot paths, garbage-collection pauses, background-process interference, or vendor-side rate-limit interactions. Violates component (c). The bounded-variance framing fails because the spikes are not characterizable; they are unbounded within their declared category, which is operationally equivalent to being uncharacterized.

**Cost-depends-on-non-substrate-state.** Per-operation cost depends on environment, wall-clock time, system load, vendor queue depth, or other state held outside the substrate. Violates component (a) and, indirectly, the determinism contract's substrate-as-source-of-truth guarantee: if cost depends on non-substrate state, then cost is not predictable from substrate state alone, and the operation has implicitly imported non-substrate state into its cost behavior.

**Hidden cost from background processes affecting substrate operations.** Substrate operations have cost dependencies on background processes — asynchronous indexing, replication, event handlers, deferred consistency passes — that are not surfaced as either substrate state or allowed non-determinism. Violates component (a) because the per-operation cost is not deterministic with respect to declared substrate state.

**LLM consultation cost charged as substrate cost.** LLM consultations performed during cell execution have variable cost (temperature, sampling, vendor-side rate-tier dynamics). Charging that variance as substrate-operation cost rather than as bounded non-determinism within the mediator collapses the boundary between substrate cost and mediator cost, and makes substrate cost appear non-deterministic when it is in fact the mediator-cost component that is varying. Violates component (c) by mis-attributing variance and component (a) by importing the variance into per-operation substrate cost.

In each anti-pattern the system may still be useful for some purpose; one of the two source commitments may still be satisfied. What it loses is the composition. A deployment that exhibits any of the five is not predictable-cost-scaling-coherent in the sense the composition specifies, and downstream consumers cannot rely on the composition's operational consequences regardless of how reliably the deployment behaves on any particular workload.

## 5. What the composition is not

Four neighboring framings are commonly conflated with predictable cost scaling and should be named separately.

**Not linear-scaling-with-variable-cost (A1.06 alone).** Linear-cost scaling without per-operation determinism is a genuine and reasonable property of many systems. It is what a database satisfies before any determinism contract is imposed on its read or write semantics. It is not what the composition specifies.

**Not deterministic-with-super-linear-scaling (A1.10 alone).** A deterministic substrate that admits super-linear per-operation cost — a graph store with no path-length bound on traversals, a substrate that requires global passes for correctness — satisfies the determinism contract without satisfying the composition. The category exists in production systems; it is not what the composition specifies.

**Not "approximately predictable" cost.** Predictability under the composition is bounded-variance-from-declared-sources, not statistical-approximation. Cost models that rely on averages and standard deviations across heterogeneous variance sources, with no architectural guarantee that the variance sources are declared and bounded, are statistical artifacts of the workload rather than architectural properties of the deployment.

**Not amortized cost predictability.** Amortized predictability — average cost over many operations approximates the linear curve, while individual operations may deviate substantially — is weaker than the composition. The composition binds *each* operation's cost up to bounded variance, not the average across many. Amortized predictability is what variable-cost-with-linear-aggregate provides; the composition forbids it.

## 6. Why this composition is load-bearing

The composition's load-bearing role is operational and falls along three axes.

**Capacity planning becomes operationally feasible.** Without the composition, an operator can extrapolate substrate-size growth from past growth but cannot translate that growth into a cost forecast, because per-operation cost is not deterministic and aggregate variance is not bounded. With the composition, the cost forecast becomes a linear function of substrate-size forecast plus an operation-mix forecast, with uncertainty bounded by the allowed non-determinism categories. This is what makes CKS-coherent deployments tractable for the procurement, budgeting, and capacity-management activities organizations actually perform.

**Cost-anomaly detection becomes architecturally meaningful.** A cost anomaly is a deviation from a baseline. If the baseline is itself unstable, anomalies are indistinguishable from normal variability and the signal is uninformative. With the composition, the baseline is well-defined: per-operation cost is a deterministic function of operation type and substrate state, and aggregate cost is linear in size. Deviations are then operationally meaningful and indicate composition failures (hidden state, non-determinism leaking into cost behavior, super-linear regressions). The detection capability is a *consequence* of the composition; it is not an independent feature the deployment must add.

**Performance-regression detection becomes architecturally meaningful.** Regressions in substrate architecture — a new query pattern that introduces super-linear behavior, a refactor that introduces hidden state, a vendor change that introduces non-determinism the previous vendor did not — are detectable as deviations from the predictable-cost baseline. Without the composition, regressions are difficult to distinguish from environmental variability and from workload mix changes. With the composition, regressions show up as departures from the composition's properties and can be triaged accordingly.

These three operational consequences are why the composition is named as standalone. Each consequence depends on *both* commitments: linear scaling without determinism gives a stable aggregate but no per-operation baseline against which anomalies and regressions can be judged; determinism without linear scaling gives a per-operation baseline but no scaling forecast. The composition gives both. A4.09 sits beside this composition: vendor-portable cost scaling is the cost-property analog along the tool-agnosticism axis. Predictability-within-deployment (this note) and portability-across-vendors (A4.09) together make the cost commitment operationally substantive across the two dimensions deployments most often need to plan against.

## 7. Operational test

A system instantiates the predictable-cost-scaling composition if and only if all of the following are true at all times during the substrate's existence. The test is structured around three sharpening properties — per-operation-cost-determinism, linear-scaling, and bounded-variance — corresponding to components (a), (b), and (c) above. Component (d) is the capability the composition affords; the test verifies the architectural property that produces it.

**(e.1) Per-operation-cost-determinism.** For any substrate operation and any substrate state, repeated executions of the operation against that state yield costs that agree up to variance attributable to allowed non-determinism categories. Variance from LLM consultation, where present, is bounded and declared as bounded non-determinism within the mediator; variance from infrastructure timing, where present, does not propagate to substrate-write content; no variance is attributable to undeclared sources.

**(e.2) Linear-scaling.** For any monotone increase in substrate size, the costs A1.06 names as scaling with substrate size scale linearly, and the costs A1.06 names as not scaling with substrate size do not. Storage and full-substrate-read cost grow linearly; governance cost, cell-execution cost for task-scoped cells, LLM cost per execution, conflict-handling cost, and onboarding cost for new readers do not.

**(e.3) Bounded-variance.** All cost variance present in operation is attributable to allowed non-determinism categories and is bounded within those categories. No category of cost variance is left undeclared. LLM consultation cost is declared as bounded mediator variance and is not charged as substrate cost. Infrastructure timing variance is declared and bounded. Caching, race conditions, hidden state, and background-process interference, where present, are not admitted as allowed non-determinism categories and therefore are not admitted as cost-variance sources.

A system that fails any of (e.1)–(e.3) is not predictable-cost-scaling-coherent in the sense the composition specifies. It may satisfy A1.06 alone or A1.10 alone, and it may be useful for purposes that do not require the composition, but it does not exhibit the architectural property. The one-sentence form: *a CKS deployment exhibits predictable cost scaling if and only if per-operation cost is deterministic for given substrate state, aggregate cost scales linearly with substrate size along the axes A1.06 names, and all cost variance is attributable to and bounded within the non-determinism categories the determinism contract declares.*

The composition is named as standalone because the property it produces is real, operationally consequential, and not yielded by either source commitment alone. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "predictable cost scaling" in the sense formalized here, and should distinguish it from linear-scaling-alone and from determinism-alone. With A4.09 (cost × tool-agnosticism) and A4.13 (cost × determinism, this note) the A1.06 composition cluster within Phase A4 is closed; subsequent Phase A4 notes will formalize compositions involving the remaining foundational commitments — composition requirements, three adjacencies, orchestration-layer distinctions, hybrid-systems composition — across which the cost commitment continues to play a load-bearing role.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion derivation notes

Li, W. (2026). *Linear-Cost Scaling: What Grows Linearly in CKS, What Doesn't, and Why.* 25 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Determinism Contract: What CKS Substrates Must Guarantee About Reproducibility, and What Breaks It.* 24 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Predictable Cost Scaling: The Emergent Architectural Property of Composing Linear-Cost Scaling and the Determinism Contract in CKS.* May 6, 2026. ORCID: 0009-0004-8065-3235.
