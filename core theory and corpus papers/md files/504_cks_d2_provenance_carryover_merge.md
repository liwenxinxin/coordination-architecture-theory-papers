# Provenance-Carry-Over Merge Operational Requirements

**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** May 15, 2026  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Provenance-carry-over merge is the third and most audit-intensive of the three Full Aspect Integration (FAI) pattern variants. It performs full merge of contributed aspects in the shared substrate and additionally establishes explicit cross-Self provenance references — navigable reference chains from each piece of shared-substrate content back into the contributing Self's home governance records, at a depth jointly authorized before the FAI event begins. This note formalizes what establishing those references operationally requires: three distinct requirements (provenance depth authorization, reference construction at contribution, and cross-reference record in the shared substrate) whose satisfaction jointly produces bidirectional traceability between shared-substrate content and contributing Selves' home governance. The note also defines the cross-Self reference level structure (Levels 1, 2, 3+), states when this pattern is appropriate relative to the other two variants, and identifies the shallow-reference merge anti-pattern — configurations that satisfy the form of provenance-carry-over without enabling genuine navigation to home governance records.

---

## 1. Position in the Derivation Series

This is derivation note D2.09 in Phase D2 of the Series D derivation from Paper 3. It stands in the same relation to D1.09 that the other D2 notes stand to their D1 parents: D1.09 committed that the three FAI pattern variants exist and named the third variant as provenance-carry-over merge — full merge of contributed aspects plus explicit cross-Self provenance references. D2.09 operationalizes what "explicit cross-Self provenance references" requires in practice.

The prior two FAI pattern variants have already received their D2 operational treatments. Selective merge (the second variant) was addressed in D2.08; full merge (the architectural default, D1's first variant) was addressed in D2.07. D2.09 presupposes the full merge machinery established in D2.07 and builds on it. Everything full merge does — combining all contributed aspect content, registering conflicts as first-class substrate state, recording contribution records (D2.06 element 4) — provenance-carry-over merge also does. The question D2.09 answers is what the additional provenance commitment requires beyond the full merge commitment.

---

## 2. What Provenance-Carry-Over Merge Adds to Full Merge

Full merge, as formalized in D2.07, combines all content from all contributing Selves' contributed aspects into the shared substrate. The contribution record for each aspect (D2.06 element 4) captures what was contributed, by whom, and when. This record supports a forward lookup: given a piece of content in the shared substrate, a reader can identify which contributing Self provided it by consulting the contribution record. This is meaningful provenance — but it is limited provenance. The contribution record lives in the shared substrate. It does not, by itself, provide a navigable path into the contributing Self's home governance records — the aspects within that Self's home substrate, the governance rules that produced them, the lineage of how that aspect came to carry the content it does.

Provenance-carry-over merge adds that navigable path. For every piece of content contributed to the shared substrate, it establishes explicit cross-Self provenance references: references that a reader can follow from the shared substrate into the contributing Self's home governance records, to the depth the jointly-authorized configuration specifies. The result is not merely a record of who contributed what; it is a reference structure that enables actual navigation from the shared substrate into the home governance records of each contributor, and from those home records back to the specific FAI event where the contribution occurred.

This additional navigability is the defining property of the pattern and is what distinguishes it from full merge. The operational question is what must happen — in three distinct requirements — for that navigation to be possible.

---

## 3. The Cross-Self Provenance Reference Structure

Cross-Self provenance references are organized in levels. The levels map the depth of the navigation path from shared-substrate content back through the contributing Self's home governance. Three levels are distinguished; beyond Level 2, the pattern generalizes to any governance-configured depth.

**Level 1 — Contribution record pointer.** The Level-1 reference for a piece of content contributed by Self A points to the contribution record for that content in the shared substrate (D2.06 element 4). This reference is always present — it is also present in full merge. What makes a provenance-carry-over configuration different from full merge at Level 1 is that the Level-1 reference is explicitly structured as the first link in a navigable chain, not merely a record of attribution. The chain must be continuable; the Level-1 reference alone does not discharge the provenance-carry-over commitment.

**Level 2 — Home-substrate aspect pointer.** The Level-2 reference points to the contributing aspect within Self A's home substrate — specifically, to that aspect's governance records as they exist within Self A's home perimeter. The governance records at this level include the aspect's DNA-layer specification, the orchestration rules governing it, and any harness substrate content that describes its role and behavior within Self A. Following the Level-2 reference allows an observer to verify that the content contributed to the shared substrate originated from a governed aspect within Self A's home governance architecture, and to inspect that aspect's current governed form.

**Level 3+ — Home-substrate lineage chain.** References at Level 3 and beyond trace further into Self A's home governance records. Level 3 references typically point to the aspect's lineage chain: prior versions, parent aspects (if the aspect was produced through intra-Self combination operations), and the DNA version history that records how the aspect's governing specification evolved. At greater depths, references can trace back to the aspect's birth record — the earliest version of the aspect in Self A's home substrate. The authorized carry-over depth, configured as part of the FAI event configuration (D1.22 Dimension 5) and jointly authorized before the event (D1.25), determines how far the reference chain extends.

The depth continuum spans from a minimal configuration — Level 1 only, equivalent to full merge's attribution record — up to a maximal configuration in which the full lineage chain back to the aspect's birth is navigable from the shared substrate. Configurations that include only Level-1 references are the shallow-reference anti-pattern addressed in §7; genuine provenance-carry-over requires at least Level-2 navigability.

---

## 4. Three Requirements for Establishing Cross-Self Provenance References

The cross-Self reference structure described in §3 does not appear automatically as a consequence of performing a full merge. It requires three operationally distinct requirements to be satisfied in sequence.

### Requirement 1 — Provenance Depth Authorization

Before the FAI event begins, the jointly-configured governance of the participating Selves must authorize the provenance carry-over depth. This authorization is part of the FAI event configuration, governed by D1.22 Dimension 5 (configurable dimensions of FAI events) and jointly authorized under D1.25 (joint authority requirements for FAI event configuration). The depth specification names how many levels of the reference chain each contributing Self is required to provide and the shared substrate is required to record.

The depth authorization is substantive governance work, not a formality. It requires the participating Selves' governance authorities to agree on how far each Self's home governance records will be exposed to the shared substrate's reference structure. A Self that contributes content to the shared substrate, under a deep provenance configuration, is committing to making its aspect's lineage chain navigable to the authorized depth by any party with access to the shared substrate. The governance authorities of each participating Self must authorize this exposure before the event begins. The depth specification, once jointly authorized, is itself authored substrate content within the FAI event configuration — subject to the three rights (inspect, modify, override) under joint governance authority.

### Requirement 2 — Reference Construction at Contribution

When a participating Self contributes an aspect to the shared substrate (the contribution operation formalized in D2.06), the provenance references must be constructed at contribution time. The contributing Self's governance provides the reference chain entries up to the authorized depth. These entries travel with the contributed content: they are substrate content contributed to the shared substrate alongside the aspect's DNA-layer and action-layer content.

Reference construction at contribution time is an operational requirement on the contributing Self's governance machinery, not on the shared substrate's orchestration. The shared substrate cannot construct Level-2 and Level-3+ references on its own — it does not have access to the contributing Self's home governance records. The contributing Self must provide those references at the moment of contribution. If a contributing Self fails to provide references at the authorized depth — providing Level-1 only when Level-2 was authorized — the contribution is incomplete under the provenance-carry-over configuration, and the FAI event's governance machinery must surface this as a conflict or deficiency.

### Requirement 3 — Cross-Reference Record in the Shared Substrate

The shared substrate records the cross-Self provenance references as substrate content, with their own provenance metadata: which contributing Self provided the reference chain, at what time during the FAI event, under which jointly-authorized depth specification. The cross-reference records are not metadata appended to the contributed content — they are first-class substrate content, subject to the same three rights (inspect, modify, override) as any other substrate content.

Making the cross-reference records first-class substrate content has three operational consequences. First, the references are inspectable: any party with governance access to the shared substrate can examine the reference chain for any contributed content and assess whether it actually navigates to the contributing Self's home governance records at the authorized depth. Second, the references are modifiable: if a reference chain is found to be broken or incorrect, it can be corrected under governance authority without disturbing the contributed content itself. Third, the references are overridable: governance authorities can override a reference if it is determined to be misleading or structurally incorrect, replacing it with a corrected reference. These properties are what make the provenance-carry-over pattern substantively auditable rather than merely formally compliant.

---

## 5. Bidirectional Traceability as the Result

When all three requirements are satisfied, the provenance-carry-over merge produces bidirectional traceability between shared-substrate content and the contributing Selves' home governance records.

**Forward direction.** From any piece of content in the shared substrate, an observer can follow the cross-Self provenance reference chain forward — starting from the Level-1 contribution record, proceeding to the Level-2 home-substrate aspect record within the contributing Self's home perimeter, and continuing to Level 3+ lineage records at the authorized depth. The forward traversal ends at whatever depth the jointly-authorized configuration specifies. At maximum depth, the forward traversal terminates at the aspect's birth record in the contributing Self's home substrate.

**Backward direction.** From the contributing Self's home governance records, an observer can follow references backward — from the aspect's governance records within the home perimeter, to the specific FAI event contribution record in the shared substrate, confirming that this specific governed aspect contributed this specific content to this specific FAI event. The backward direction is what enables each participating Self's governance to audit the specific FAI events in which its aspects participated, without requiring that a complete copy of the shared substrate be retained within the home perimeter.

The two directions together constitute bidirectional traceability. Full merge provides one direction of traceability: from shared-substrate content to the contributing Self's identity (via the contribution record). Provenance-carry-over provides both directions and extends the forward direction to navigate into the contributing Self's home governance records at the authorized depth. It is this bidirectionality, and the home-record navigability of the forward direction, that distinguishes the pattern from full merge as an auditability mechanism.

---

## 6. When to Use Provenance-Carry-Over Merge

Provenance-carry-over merge is the most operationally demanding of the three FAI pattern variants. It requires joint governance agreement on depth before the event, reference construction work by each contributing Self at contribution time, and maintenance of first-class cross-reference records in the shared substrate. This overhead is appropriate in specific circumstances; in other circumstances, full merge or selective merge provides sufficient governance coverage at lower operational cost.

Provenance-carry-over merge is appropriate when one or more of the following conditions holds:

The participating Selves, or any external governance authority with oversight of the FAI event, require the ability to independently verify the origin and governance lineage of content in the shared substrate. Independent verification requires navigable references into each contributing Self's home governance records; attribution alone (as provided by full merge) does not enable it.

The FAI event involves contributions that will be ingested by receiving Selves into their own home substrates (through the evolution-feed mechanism), and those receiving Selves need to verify the governance pedigree of content before ingestion. The Level-2 and Level-3+ references provide the governance pedigree chain that an ingesting Self's governance rules can evaluate.

The FAI event involves contributions across Selves operating in different regulatory or organizational governance contexts, where each Self's governance authority requires that the other Selves' contributed content carry a verifiable trail back to governed sources.

Full merge is the appropriate default for events where contribution attribution suffices and home-record navigability is not required. Selective merge is appropriate when the participating Selves need to limit which aspects are combined, rather than needing to trace the governance lineage of contributed aspects. The choice among the three variants is itself governance-configured and jointly authorized as part of the FAI event configuration.

---

## 7. Anti-Pattern: Shallow-Reference Merge

The shallow-reference merge is the characteristic failure mode of provenance-carry-over merge configurations. A shallow-reference merge uses the provenance-carry-over configuration — the FAI event is designated as a provenance-carry-over event with an authorized depth — but the references actually provided are only Level-1: they point to the contribution record within the shared substrate and do not navigate into the contributing Self's home governance records.

The anti-pattern is detectable. A shallow-reference merge satisfies the formal requirement that cross-Self provenance references exist (they do — the Level-1 contribution record pointer is present), but it does not enable the forward navigation that constitutes the pattern's substantive commitment. An observer attempting to follow the reference chain from shared-substrate content into the contributing Self's home governance records will find that the chain terminates at the contribution record in the shared substrate — the same termination point available in full merge. The provenance-carry-over configuration label is present; the provenance-carry-over capability is absent.

The anti-pattern typically arises from two sources. The first is implementation gap: the contributing Self's governance machinery constructs Level-1 references by default (as in full merge) and the additional reference construction work required by Requirement 2 was not completed. The second is intentional circumvention: a contributing Self participates in a provenance-carry-over configuration but provides only Level-1 references, satisfying the form of the commitment without exposing its home governance records to Level-2 navigation. Both sources produce the same result: a configuration that represents itself as providing bidirectional traceability but does not.

The three-rights property of the cross-reference records (Requirement 3) provides the governance mechanism for detecting this anti-pattern: the cross-reference records are inspectable by any party with governance access, and an inspection that finds only Level-1 references under a greater-depth authorization is a detectable non-conformance.

---

## 8. Operational Test

A provenance-carry-over merge satisfies its operational requirements if and only if all of the following are true:

**Test 1 (Depth Authorization).** Before the FAI event began, the jointly-configured governance produced a jointly-authorized depth specification naming the authorized number of cross-Self reference levels. This specification exists as authored substrate content within the FAI event configuration, with provenance showing it was jointly authorized by the governance authorities of all participating Selves.

**Test 2 (Reference Construction).** For every piece of content in the shared substrate contributed by each participating Self, a reference chain exists at the authorized depth. Following the chain from Level 1 produces a navigable pointer to a contribution record in the shared substrate. Following the chain to Level 2 produces a navigable pointer to the contributing aspect's governance records within the contributing Self's home perimeter. At each additional authorized level, the chain produces a navigable pointer to the next level of home governance records.

**Test 3 (Cross-Reference Record Integrity).** The cross-Self provenance references are recorded as first-class substrate content with their own provenance metadata identifying the contributing Self that provided them, the time of provision, and the depth authorization under which they were constructed. The references are subject to the three rights — inspect, modify, override — under the shared substrate's governance.

**Test 4 (Bidirectional Navigation).** An observer with governance access to the shared substrate can navigate forward from any piece of shared-substrate content to the contributing Self's home governance records at the authorized depth. An observer with governance access to a contributing Self's home governance records can navigate backward from those records to the specific FAI event's contribution record in the shared substrate.

A configuration that passes Tests 1 through 4 is a properly conducted provenance-carry-over merge. A configuration that claims provenance-carry-over status but fails Test 2 or Test 4 — because only Level-1 references are present — is the shallow-reference merge anti-pattern identified in §7.

---

*This note is derivation note #504 in the CKS derivation series (Series D, Phase D2, position D2.09). It formalizes operational requirements derived from Paper 3 of the CKS theory series and is intended for defensive publication as public prior art. It introduces no new axioms beyond what Paper 3 commits to.*
