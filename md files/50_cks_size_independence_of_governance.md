# The Size-Independence-of-Governance Property as Standalone Architectural Commitment in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 4 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one architectural property of the CKS linear-cost scaling commitment — the **size-independence-of-governance property** — as a standalone architectural commitment with independent operational content, paired with but distinct from the dimension-axis treatment of the same claim formalized in the companion note on Dimension A (substrate-size cost).

## Abstract

The CKS pattern's linear-cost scaling commitment, defended in §6 of the source paper, decomposes deployment cost across four dimensions: substrate size, rule variety, intervention frequency, and cell execution count. Within that decomposition, the load-bearing claim — the one that distinguishes the CKS cost profile from N-proportional governance patterns — is that governance cost does not grow with substrate size N. The companion note on Dimension A treats this claim from the dimension-axis perspective, asking what cost behavior characterizes the substrate-size dimension. This note treats the same claim from the property-axis perspective, asking what architectural property holds across the governance moments. The two framings differ in emphasis but agree on substance. This note states the size-independence-of-governance property in terms of four operational components, distinguishes it from four adjacent commitments commonly conflated with it (best-case cost-scaling, performance-tuned governance, optimized review patterns, sample-based governance), names eight failure modes that violate the property even when other cost commitments hold, and provides an operational test for whether a deployment's governance cost behavior respects size-independence in the architectural sense. The property is one of the most defensible standalone commitments in the CKS pattern because it forecloses the position that N-proportional governance cost is necessary or unavoidable.

## 1. Why size-independence-of-governance needs to be formalized as standalone

The parent foundational note on linear-cost scaling commits the CKS pattern to a four-dimension cost profile in which governance cost is not size-proportional. The integrating-frame note on the operational treatment of that commitment establishes the four-dimension cost structure — substrate size, rule variety, intervention frequency, cell execution count — and the dimension-axis decomposition treats each axis on its own terms. The Dimension A note, in particular, includes the size-independence guarantee as part of Dimension A's cost behavior. This note formalizes the same claim from a different framing: the size-independence-of-governance property as a standalone architectural commitment, independent of the dimension framing.

Three motivations make the standalone treatment worth its own note.

**Foreclosure value.** Arguments that governance must scale with N typically identify a feature that seems operationally necessary — periodic audits over all substrate, compliance checks applied per element, review cycles proportional to accumulated decisions, schema-migration passes triggered by substrate growth — and treat it as architecturally necessary. Named explicitly, the size-independence property forecloses each such argument: governance cost — the cost paid at the architectural moments of orchestration rule authoring (per the prior derivation note on Moment 1) and direct override (per the prior derivation note on Moment 2) — is independent of N, regardless of what operational features a deployment layers on top.

**Strategic prior-art posture.** Among the dimension-axis specializations of the linear-cost commitment, size-independence-of-governance is the single most consequential prior-art claim, because it is the property that distinguishes CKS from review-everything, full-substrate-audit, per-element-approval, and comprehensive-coverage governance patterns. A vendor publishing a "scalable governance architecture" or "size-aware audit system" is substantially less defensibly novel when the property is publicly formalized as a standalone architectural commitment.

**Connection to the architectural-property qualifier.** A prior derivation note establishes that governance is an architectural property rather than a procedural promise. Size-independence is what makes architectural governance operationally feasible at scale — without it, architectural governance could still be infeasible if its cost grew with N. The two properties together specify what makes governance both architecturally sound and operationally feasible at any substrate size.

## 2. The size-independence-of-governance property, defined precisely

In the CKS pattern, a deployment satisfies the **size-independence-of-governance property** when the governance cost component of total deployment cost — the cost paid at the two architectural governance moments — is independent of substrate size N. The property has four operational components.

**(a) Rule-authoring cost is size-independent.** The cost of authoring an orchestration rule is the same architecturally regardless of whether the substrate is small or large. A rule authored for a deployment with N=1,000 elements costs the same architectural effort as the same rule authored for a deployment with N=1,000,000 elements. Per the companion note on Dimension B, rule-authoring cost grows with R (rule variety and complexity); the size-independence property adds that this cost does not depend on N at the moment the rule is authored.

**(b) Direct-override cost is size-independent.** The cost of exercising an override is the same architecturally regardless of substrate size. An override against a specific piece of substrate content costs the human's evaluation and execution effort at the moment of intervention; the substrate's total size does not affect this cost. Per the companion note on Dimension C, intervention cost grows with F (intervention frequency); the size-independence property adds that this per-intervention cost does not depend on N.

**(c) Aggregate governance cost is size-independent.** Total governance cost — the sum of the rule-authoring and intervention components — does not grow with N. A deployment that scales N by ten-fold while holding R and F constant has the same aggregate governance cost; only deployments that scale R or F see governance cost grow.

**(d) The property holds continuously.** As substrate accumulates over the deployment's lifetime, the size-independence property holds continuously. The deployment does not encounter scaling thresholds beyond which governance cost begins to grow with N. The property is invariant under N growth.

A deployment that satisfies all four has governance cost that does not scale with N; a deployment that fails any one has size-dependent governance cost in some respect.

## 3. What the property does NOT claim

Stating precisely what the property does not claim is what keeps the standalone framing from drifting into something stronger than the source paper supports.

**It does not claim that all costs are size-independent.** Storage cost, backup cost, replication cost, and other host-level operational costs may grow with N. The property is specifically about governance cost, not about all deployment costs.

**It does not claim that governance is cheap in absolute terms.** The property is about scaling behavior, not absolute levels. A deployment with high R or F has high absolute governance cost, but this cost does not grow with N. Absolute level is set by deployment design; the scaling property is set by the architecture.

**It does not claim that all operational concerns related to governance are size-independent.** Audit logging, observability dashboards, compliance reporting, and similar operational features may grow with N. These are deployment-layer concerns, not architectural governance moments.

**It does not constrain how N can grow.** The architecture does not specify a maximum N; size-independence holds at any N value the deployment reaches.

**It does not claim that size-independence is automatic.** Deployments can implement governance patterns that violate size-independence (per the failure modes in §6). The architectural commitment is that the architecture *supports* size-independent governance; whether deployments actually implement it is a deployment-design choice.

**It does not foreclose layered N-dependent operational features.** A deployment may implement audit cycles, periodic reviews, or N-scanning compliance checks as deployment-layer concerns. What the property forbids is treating those features as architectural governance moments — that is, conflating an operational feature with the two-moment architectural commitment.

## 4. What the property is NOT

Four adjacent commitments are commonly conflated with the size-independence-of-governance property. Each is a real and reasonable commitment in some other architecture; naming what the property is not is what prevents the misreading.

**Not best-case cost-scaling.** Best-case cost-scaling describes the architecturally best-case scenario for governance cost, with worse cases scaling with N. Size-independence is different: governance cost does not grow with N in *all* cases, not only best ones. Implementations that achieve size-independence only under favorable conditions — small substrates, simple rules, rare interventions — do not satisfy the architectural commitment.

**Not performance-tuned governance.** Performance-tuned governance achieves approximate constant-time behavior through caching, indexing, batching, or similar optimizations applied to an underlying N-scaling design. Size-independence is different: governance cost does not grow with N regardless of whether optimizations are applied. An implementation that achieves apparent size-independence only because performance tuning has flattened the curve at deployment scale may operate within size-independent envelopes today and fail tomorrow when conditions shift. The architectural commitment is that the property holds without requiring optimizations to succeed.

**Not optimized review patterns.** Optimized review patterns reduce governance cost through clever sampling, batching, or prioritization of an N-scanning review workflow. Size-independence is different: governance moments cost their human-effort amounts regardless of substrate size, without requiring review optimizations to remain operationally feasible. Optimized review patterns can be deployed on top of size-independent architecture, but they are deployment-layer features, not the architectural commitment.

**Not sample-based governance.** Sample-based governance reviews a sample of substrate content rather than all of it, achieving lower per-cycle review cost while still treating review cycles as the governance mechanism. Size-independence is different: it is not about reducing the per-cycle cost of an N-dependent review pattern; it is about governance cost being architecturally independent of N from the start.

## 5. Why the property is load-bearing for downstream commitments

The size-independence-of-governance property is load-bearing for several CKS commitments.

**The linear-cost scaling commitment.** The parent foundational note's commitment depends on size-independence specifically — without it, governance would scale with N, and the linear-cost commitment would fail along its most consequential axis.

**The architectural-property qualifier on governance.** Size-independence is what makes architectural governance operationally feasible at scale; without it, architectural governance could be infeasible at large N regardless of how robustly it is committed in principle.

**The non-specialist governance commitment.** The commitment to commodity-tool governance defended in §7.4 of the source paper depends on governance being operationally feasible in environments meeting the three minimal requirements. Size-independence is what makes this feasible: humans using commodity tools can exercise governance over substrates of any size because the per-moment cost does not grow with substrate size.

**Migration safety.** Substrates can be migrated between hosts that meet the three minimal requirements without governance cost growing during or after migration. Size-independence ensures that governance over a migrated substrate costs the same architecturally as governance over an originating substrate of the same R and F.

**Strategic prior-art posture.** The architectural commitment to size-independence forecloses the position that N-proportional governance is necessary. Standalone formalization establishes prior-art territory that downstream parties cannot patent without bumping into the formal commitment.

## 6. Failure modes that violate size-independence

A deployment can produce governance cost that grows with N even when other cost commitments hold. Eight failure modes name the most common ways this happens.

**(a) N-scanning rule authoring.** Rule authoring requires considering all substrate content related to the rule's domain, with authoring cost growing with N. The amortization property holds — the rule cost is paid once — but the per-authoring cost is N-dependent, breaking size-independence on the rule-authoring side.

**(b) Substrate-volume-dependent override evaluation.** Interventions require considering substrate content related to the override target, with per-intervention evaluation cost growing with related-substrate volume. The per-intervention property holds nominally, but the per-intervention cost is N-dependent.

**(c) Per-cycle audit treated as governance.** The deployment conducts periodic audits with audit cost growing with N, and treats audit cycles as architectural governance moments rather than operational features. The two-moment governance structure becomes a three-moment structure with the third moment being N-scaling.

**(d) Schema-migration costs treated as governance.** When substrate schema evolves, the deployment treats schema migration as architectural governance with cost growing with N. Schema migration is a one-time operational event; treating it as ongoing architectural governance violates size-independence.

**(e) Comprehensive-coverage rules.** The deployment authors orchestration rules that aim to cover all substrate elements comprehensively, with rule complexity growing with N. The per-rule cost grows because the rule must address the full substrate volume; size-independence on the rule-authoring side is broken.

**(f) Cumulative-state intervention.** Interventions consider cumulative substrate history — all past decisions, conflicts, rules — with per-intervention cost growing with the cumulative history (which itself grows with N). The per-intervention property holds, but the per-intervention cost is N-dependent through cumulative history.

**(g) Authority-revocation propagation costs.** When authority changes — revoking a human's authority, transferring override authority — the implementation propagates changes through all substrate content, with propagation cost growing with N. The authority change is treated as architectural governance with N-scaling cost.

**(h) Compliance frameworks applied per-element.** The deployment applies compliance checks to each substrate element with compliance cost growing with N. Compliance can be a deployment-layer concern; treating per-element compliance as architectural governance violates size-independence.

A deployment that exhibits any of (a)–(h) does not respect the size-independence-of-governance property in the architectural sense, and naming the failure precisely is what allows downstream remediation.

## 7. Operational test

A deployment respects the size-independence-of-governance property if and only if all of the following are true at all times during the substrate's existence:

1. Rule-authoring cost is size-independent: a rule of the same complexity costs the same architectural authoring effort regardless of substrate size at the time of authoring.
2. Direct-override cost is size-independent: an intervention of the same scope costs the same architectural intervention effort regardless of substrate size at the time of intervention.
3. Aggregate governance cost (the sum of the rule-authoring and intervention components) does not grow with N. Doubling N while holding R and F constant does not increase governance cost.
4. The property holds continuously over the deployment's lifetime. The deployment does not encounter scaling thresholds beyond which governance cost begins to grow with N.
5. Operational features that grow with N — audit logging, backup, monitoring, observability — are kept architecturally separate from the two governance moments. The deployment may have N-dependent operational costs, but these do not contribute to architectural governance cost.

A deployment that fails any of (1)–(5) does not respect the size-independence-of-governance property in the architectural sense, even if its absolute governance cost is acceptable for its current scale. Such a deployment is not CKS-coherent on the size-independence axis, and downstream work that relies on its governance scaling guarantees should be scoped accordingly.

## 8. The relationship between this note and the Dimension A note

This note and the companion Dimension A note treat the same architectural claim from different framings, and the framing distinction matters for how each is read.

The Dimension A note frames the claim from the dimension-axis perspective: what is Dimension A's cost behavior? Its answer is that governance cost on Dimension A is zero — governance is independent of N — while operational cost on Dimension A may grow with N (storage, backup, replication) but is not architectural governance cost. The note is organized around the substrate-size dimension and how cost behaves on it.

This note frames the claim from the property-axis perspective: what is the architectural property of governance with respect to substrate size? Its answer is the four-component size-independence property defined in §2. The note is organized around the property as a standalone architectural commitment.

The two notes share content — both establish that rule-authoring and intervention cost do not grow with N — but organize that content differently. Readers interested in dimension-axis cost analysis read the Dimension A note; readers interested in the property-axis architectural commitment read this one. Together they exhaust the size-independence treatment within the linear-cost scaling decomposition.

## 9. Conclusion

Implementations under pressure to add governance features, audit rigor, or compliance overhead consistently drift toward governance patterns that scale with N. The drift is steady because N-scaling features are technically straightforward, architecturally familiar from database and analytics systems, and easy to justify as good practice. The architectural commitment to size-independence is what each N-scaling feature erodes when added as architectural rather than operational concern.

Implementations that drift away from size-independence produce systems that work at small substrate sizes and become operationally infeasible as substrate accumulates. Governance becomes a scaling crisis: rule authoring takes longer as substrate grows; interventions become slower because more substrate must be considered; compliance frameworks become bottlenecks. Each crisis traces back to governance cost that was allowed to scale with N when the architecture committed to size-independence.

Naming the size-independence-of-governance property as a standalone architectural commitment gives downstream implementers a precise specification of what the commitment requires, and gives the prior-art record an explicit foreclosure of the position that N-proportional governance is necessary.

Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "size-independence of governance" in the sense formalized here. Subsequent work that uses the term differently — most often by identifying the property with performance-tuned scaling, sample-based review, or best-case cost behavior — is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Size-Independence-of-Governance Property as Standalone Architectural Commitment in the Coordination Knowledge Substrate Pattern.* 4 May 2026. ORCID: 0009-0004-8065-3235.
