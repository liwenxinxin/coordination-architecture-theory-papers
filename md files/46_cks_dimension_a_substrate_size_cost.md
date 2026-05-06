# Dimension A: Substrate-Size Cost and the Size-Independence Guarantee in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize Dimension A — substrate size as a cost dimension — as having independent operational content within the linear-cost scaling commitment, with particular weight on the size-independence guarantee on governance cost that distinguishes Dimension A from adjacent patterns commonly conflated with it.

## Abstract

The CKS pattern's linear-cost commitment (Claim 4, §6 of the source paper) makes claims along three architecturally independent cost dimensions — substrate size, rule variety, and intervention frequency — with cell-execution workload sitting orthogonal to all three. This note formalizes the first, Dimension A (substrate size), as a standalone treatment. The architectural commitment on this dimension is asymmetric: storage cost grows with substrate size N, backup and replication costs grow with N, but *governance cost* does not. The size-independence guarantee on governance cost is the load-bearing claim that makes the architecture defensible at scale; it forecloses the alternative — N-proportional governance cost — that adjacent architectures, audit systems, and per-element review workflows exhibit as their headline scaling property. The note specifies what Dimension A measures, how substrate size grows, the four operational components of the guarantee, what the commitment does and does not claim, four adjacent cost patterns to distinguish from it, eight failure modes that violate it, and an operational test for CKS-coherence on this dimension.

## 1. Why Dimension A needs to be formalized as standalone

The parent foundational note on linear-cost scaling commits the CKS pattern to a cost contract organized around three independent dimensions plus the workload axis, and the integrating-frame note on operational variants establishes the full four-dimension structure as a single architectural commitment. This note formalizes the first of those dimensions — Dimension A, substrate size — as having independent operational content that can be specified, defended, and tested separately from the others, while still composing with them into the integrated commitment.

Three motivations make the standalone treatment worth its space. The first is *operational*. Substrate size grows monotonically over time as the deployment accumulates decisions, conflicts, rules, and rationale; the architectural question is what this growth does to operating cost. Without a precise specification, deployments cannot plan for scale, and implementations cannot defensibly claim CKS-coherence on the cost axis as substrates grow.

The second is *strategic*. The size-independence guarantee on governance cost is among the most consequential prior-art claims in the cost-scaling decomposition, because it forecloses the alternative in which N-proportional governance cost is treated as necessary or unavoidable. Adjacent architectures — review-everything patterns, full-substrate audit systems, per-element approval workflows — have governance cost that scales with N as their headline property. Naming the guarantee as a standalone commitment establishes the prior-art line against any of these designs being claimed as novel.

The third is *diagnostic*. When a deployment reports that costs grow as the substrate grows, the diagnosis is rarely that the substrate is too large; it is almost always that some specific feature was added that allows N to drive cost — an N-scanning audit, a full-substrate validation, a permission-propagation pattern, a conflict-detection mechanism that scans rather than queries provenance metadata. The standalone treatment names which feature, against which architectural commitment.

## 2. What Dimension A measures and how it grows

Dimension A measures the volume of substrate content the deployment maintains: entities, relationships, decisions, rationale, conflicts (per A1.03's preserved-conflict commitment), orchestration rules, provenance metadata (per A1.07's six-field requirement), and any other content the substrate carries. The measurement units depend on the host environment's structure — rows, records, documents, fields, bytes — but the dimension is invariant under unit choice; the architectural commitment is about scaling with content volume regardless of how volume is counted.

Substrate size grows in three distinct patterns deployments commonly exhibit, and naming them precisely is what makes the guarantee in §3 testable.

**Decision accumulation.** As the deployment makes coordination decisions over time, the substrate accumulates the decision records — who decided, when, under what authority, with what rationale (per A1.07's path-retraceability commitment). Decision accumulation is monotonic absent human-authored deletion: substrate size grows over the deployment's lifetime, with the rate proportional to coordination activity.

**Conflict accumulation.** As the deployment encounters contradictions in substrate content (per A1.03's two-level conflict-handling commitment), the substrate accumulates the contradicting pieces and the resolution decisions about them, both held as first-class addressable substrate content. Conflict accumulation grows with deployment activity in domains where contradictions are common.

**Rule and rationale accumulation.** As the deployment authors orchestration rules (per A2.04 — rule authoring as a governance moment) and captures rationale alongside substrate content, the substrate accumulates rule text and rationale text. This contributes to N growth even when decisions and conflicts are sparse.

The architectural commitment is that all three patterns produce N growth without producing growth in governance cost, so long as rule variety and intervention frequency (Dimensions B and C, treated as standalone in A2.31 and A2.32) do not also grow. This is what makes the guarantee size-specific: a substrate growing along Dimension A alone has constant governance cost.

## 3. The size-independence guarantee on governance cost

The architectural commitment on Dimension A is governance-specific: governance cost — the cost paid at the two governance moments, rule authoring (per A2.04) and direct override (per A2.05) — does not grow with N. The guarantee has four operational components, each testable independently and all four of which must hold for a deployment to satisfy it.

**(a) Rule-authoring cost is paid per rule, not per substrate element.** A rule authored against a substrate of N=1,000 has the same architectural cost as the same rule authored against N=1,000,000. The rule's cost depends on its complexity and the human's authoring effort, not on how much content it will eventually govern; the amortization runs from the rule across the substrate, not back the other way.

**(b) Direct-override cost is paid per intervention, not per substrate element.** An override exercised against a specific element costs the human's intervention effort regardless of how many other elements exist. The intervention cost depends on what the human is changing, not on what surrounds it.

**(c) Governance does not require N-scanning.** The architectural governance moments do not require humans to process substrate content proportional to N. Rule authoring considers the rule's domain (typically a small fraction of the substrate); direct override considers the intervention's scope (typically a single element or a small bounded set). Neither moment produces substrate-traversal cost as a function of governance activity.

**(d) Governance is amortized across substrate content.** Rules authored for a domain apply to all substrate content in that domain, regardless of size; override authority exercised at a moment applies to the substrate state at that moment, regardless of size. The amortization runs from the (small) governance moment across the (potentially large) substrate the moment governs.

The four components together define the guarantee. A deployment satisfying all four has governance cost that does not grow with N; failing any one produces size-dependent governance cost in some respect. A2.34 treats the size-independence-of-governance property from the property axis as a standalone commitment; this note treats it from the dimension axis as the load-bearing operational content of Dimension A's cost behavior. The two are cross-readable but not redundant.

## 4. What the Dimension A commitment does NOT claim

The standalone treatment is not maximalist, and stating precisely what the architecture does not claim is what keeps the guarantee defensible against overstatement.

**(a) It does not claim that storage cost is independent of N.** The host environment must store substrate content, and storage cost typically grows with content volume. This is a host-level operational concern; deployments choosing storage-intensive hosts pay storage costs proportional to N as a deployment trade-off, not as an architectural failure.

**(b) It does not claim that backup, replication, or distribution costs are independent of N.** A deployment that backs up substrate content or replicates across regions pays costs proportional to N. These are deployment choices the architecture does not promise to make size-independent.

**(c) It does not claim that cell-execution cost is independent of N.** Cells operate within bounded scope (per A2.09), so per-cell cost depends on cell scope rather than N directly; small N-dependencies within bounded scope do not violate the architectural commitment as long as cells remain bounded.

**(d) It does not claim that the absolute level of governance cost is low.** The guarantee is about scaling behavior, not absolute levels. A deployment with high rule variety or intervention frequency has high absolute governance cost; the guarantee is that this cost does not grow with N.

**(e) It does not claim that N can grow without operational consequence.** Larger substrates may take longer to back up, migrate, load, or validate on schema change. These are operational concerns; they are not violations of the architectural commitment to size-independence of governance.

## 5. What Dimension A is NOT

Four adjacent cost patterns are commonly conflated with Dimension A's architectural commitment. Each is a real concern in some deployments; naming what each is and what makes it distinct is what prevents the slide.

**Not N-scanning operations as governance.** Audits that examine all substrate content, validations that check every element, compliance reviews that read the entire substrate — some implementations treat these as governance. The architectural governance moments (rule authoring, direct override) do not require N-scanning; these may be deployment-level audit or validation activities, but treating an N-scanning audit as governance imports its size-dependency into the governance layer.

**Not full-substrate audits.** Audit systems that scan substrate content for compliance, integrity, or quality issues are deployment concerns, not architectural governance. Path-retraceability (per A1.07) does not require N-scanning audits; it operates through provenance metadata queryable per element.

**Not schema-migration cost.** When orchestration rules evolve and substrate schemas change, deployments may need to apply schema changes to existing content. Migration cost depends on N for one-time migrations, but the architectural commitment is about ongoing governance cost; occasional N-dependent migrations do not violate the guarantee.

**Not backup-and-recovery cost.** Backup, recovery, replication, and disaster recovery have N-dependent costs by nature. Dimension A's commitment is about governance cost; deployments pay N-dependent operational costs without compromising the architectural commitment, provided those costs stay at the operational layer.

## 6. Failure modes that violate the size-independence guarantee

A deployment can fail the guarantee specifically, even when its overall cost profile is acceptable at current scale. Eight failure modes name the most common ways this happens.

**(a) Per-element governance reviews.** The deployment requires human governance review for each piece of substrate content; governance cost grows linearly with N, breaking the per-rule and per-intervention amortization the guarantee depends on.

**(b) Substrate-wide rule re-evaluation.** The deployment re-evaluates orchestration rules against all substrate content periodically; rule authoring becomes effectively per-element in cost behavior even though each rule was authored once.

**(c) Override-with-N-context.** The deployment requires override decisions to consider all substrate content related to the target, with relevance determined by scanning N; intervention cost grows with N even when the override targets a single element.

**(d) Audit-as-governance.** The deployment treats periodic audits as the governance mechanism; governance becomes N-dependent because the deployment has structurally conflated audit (operational) with governance (architectural).

**(e) Schema-validation-on-write scaling with N.** The deployment validates each write against substrate-wide schema constraints, with validation cost growing with N if validation requires scanning related content; placement in the write path makes governance cost N-dependent in practice.

**(f) Conflict-detection scaling with N.** The deployment detects contradictions through full-substrate scans rather than through provenance-relationship metadata (per A2.16's provenance requirement for first-class conflicts); detection cost grows with N, and detection is treated as a governance precondition.

**(g) Permission-propagation scaling with N.** The deployment requires permission changes to be propagated through all affected substrate content, with propagation cost growing with N; authority changes — what should be a per-rule operation — become operationally expensive at scale.

**(h) Indexing operations treated as governance.** The deployment maintains indexes over all substrate content for governance purposes, with index-maintenance cost growing with N; indexes are operational, and treating them as governance imports their N-dependency into the architectural layer.

A system exhibiting any of (a)–(h) fails the size-independence guarantee on Dimension A, even if absolute governance cost remains acceptable at current scale.

## 7. Operational test

A deployment respects the size-independence guarantee on Dimension A if and only if all of the following are true at all times during the substrate's existence:

1. Rule-authoring cost is paid per rule, not per substrate element. Authoring a rule against a larger substrate does not cost more than authoring the same rule against a smaller substrate.
2. Direct-override cost is paid per intervention, not per substrate element. Exercising override against a piece of substrate content does not cost more when the substrate as a whole is larger.
3. Governance does not require N-scanning. The deployment's governance moments operate within their declared scope (the rule's domain, the intervention's target) without needing to consider the substrate as a whole.
4. Governance is amortized across substrate content. Rules and overrides apply to relevant substrate content regardless of how much content exists in total.
5. Operational concerns whose costs are N-dependent (backup, audit, migration, indexing) are kept separate from governance moments architecturally. The deployment may have N-dependent operational costs without those costs being architecturally part of governance.

A deployment that fails any of (1)–(5) does not satisfy the guarantee, even if its absolute governance cost remains acceptable for its current scale. Such a deployment may be CKS-coherent on other axes — the human-governed commitment, the substrate-cell boundary, the conflict-preservation commitment — without being CKS-coherent on Dimension A's cost behavior; downstream work relying on the guarantee should be scoped accordingly.

## 8. Why naming Dimension A as standalone matters

Implementations under pressure to deliver compliance, audit, or quality-assurance features drift consistently toward designs that scale governance cost with N. The drift is steady because N-scanning features are technically straightforward and architecturally familiar from database systems; each such feature, added as an architectural rather than operational concern, erodes the size-independence guarantee in some specific respect, in a direction that compounds. Implementations drifting away from the guarantee work at small substrate sizes but become operationally infeasible as substrate accumulates: governance backlogs grow faster than humans can clear them; audit cycles exceed the cycle period; permission changes paralyze the deployment. Each crisis traces back to governance cost allowed to scale with N when the architecture committed to size-independence.

Naming the size-independence guarantee as a standalone commitment — with the four components in §3, limitations in §4, distinctions in §5, failure modes in §6, and test in §7 — gives downstream implementers a precise specification of what cost behavior the CKS pattern commits to on this dimension. Subsequent work that adopts, extends, composes, or argues against the CKS pattern should use the guarantee in the sense formalized here. Work that uses the term differently — most often by treating periodic audits or per-element review as compatible — is using a different concept, and the difference should be named.

Subsequent notes formalize the other dimensions and the property-axis treatment: A2.31 (Dimension B, rule variety), A2.32 (Dimension C, intervention frequency), A2.33 (the workload axis as architecturally orthogonal), and A2.34 (size-independence as a property). With the integrating-frame note A2.29, these complete the operational decomposition of A1.06's linear-cost commitment.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion derivation notes

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Linear-Cost Scaling: What Grows Linearly in CKS, What Doesn't, and Why.* 25 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Dimension A: Substrate-Size Cost and the Size-Independence Guarantee in the Coordination Knowledge Substrate Pattern.* May 4, 2026. ORCID: 0009-0004-8065-3235.
