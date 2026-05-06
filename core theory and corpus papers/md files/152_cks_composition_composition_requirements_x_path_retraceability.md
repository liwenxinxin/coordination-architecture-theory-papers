# Retraceability Preservation Across Composition: The Emergent Architectural Property of Composing CKS's Composition Requirements with Path Retraceability

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the emergent architectural property that arises when two foundational commitments of the CKS pattern — composition requirements (A1.13) and path retraceability (A1.07) — are composed: the property of *retraceability preservation across composition*, which operationalizes A1.13's per-substrate retraceability-preservation requirement through A1.07's specific provenance and accountability machinery, applied uniformly at every composition partner.

## Abstract

CKS deployments at scale typically involve multiple substrates composed within a single organizational governance domain. Two foundational commitments of the CKS pattern bear directly on whether such compositions remain auditable: composition requirements (A1.13), which names per-substrate retraceability preservation as one of five constraints multi-substrate composition must satisfy, and path retraceability (A1.07), which specifies what retraceability requires of substrate content at single-substrate scope. Neither alone tells a deployment what multi-substrate retraceability requires. The composition is the operational form: A1.07's six provenance fields and four accountability questions hold at every composition partner, cross-substrate operations preserve provenance at each side, and A1.07's substrate-only-paths property holds at every partner. This note states the emergent property as four operational components, identifies what the composition forces beyond either commitment alone, names five anti-patterns that specifically violate the composition, and supplies an operational test with three sharpening properties. The note is the third in the A1.13 composition cluster, following the formalizations of mediator preservation and governance preservation across composition.

## 1. Why this composition pair needs to be formalized as standalone

A1.13 (composition requirements) names *per-substrate retraceability preservation* as one of five requirements any multi-substrate composition must satisfy: every substrate participating in the composition must remain path-retraceable, and the path produced by the composition must be traversable end-to-end. The requirement has its own decomposition (Requirement B in the source paper's composition-requirements treatment, formalized in this series as A2.77). What A1.13 does not do is specify the operational content of retraceability; it is a constraint set on what compositions must preserve, silent on what preservation requires of substrate content.

A1.07 (path retraceability) supplies the operational content. Every piece of substrate content carries six provenance fields (formalized as A2.40 — writer attribution, timestamp, antecedent reference where antecedents exist, orchestration rule reference for cell-mediated writes, rationale where the accountability plan calls for it, and conflict relationship reference for content participating in conflicts); the four accountability questions (formalized as A2.36–A2.39 — what was decided, by whom, under what authority, with what rationale) are answerable from substrate content alone; and the retraceable path runs through substrate content rather than through external logs, agent memory, or human recollection (formalized as A2.41 — substrate-only paths). What A1.07 does not do is specify how retraceability extends across substrate boundaries when multiple substrates are composed.

The composition of the two commitments is the operational form. A1.13's per-substrate retraceability requirement (A2.77) is satisfied if and only if A1.07's machinery — the six fields, the four questions, the substrate-only path — holds at every composition partner, with cross-substrate operations preserving provenance at each side. The composition produces an architectural property neither commitment supplies independently: retraceability preserved uniformly across composition rather than fully at primary substrates and partially at secondary ones.

The motivating cases are concrete. A regulated deployment with a coordination substrate at its center, an audit substrate the compliance function operates, and a derived-projection substrate the reporting function consumes is, by composition, a multi-substrate system. An auditor reconstructing a contested decision must traverse from the audit substrate's record back to the coordination substrate's content, and the traversal must remain on substrate rails throughout. If the coordination substrate's writes lack antecedent references, the path breaks at the moment it crosses into that substrate; if both substrates record provenance but the cross-substrate operation that copied content between them did not preserve antecedent references at the boundary, the path breaks at the boundary itself. The composition pair has independent prior-art status because "auditable multi-substrate AI" is increasingly used in commercial systems to describe deployments that may not preserve provenance uniformly across composition.

This note is the third in the A1.13 composition cluster. A4.14 (A1.13 × A1.04) formalizes mediator preservation per A2.79; A4.15 (A1.13 × A1.01) formalizes governance preservation per A2.76; the present note formalizes retraceability preservation per A2.77. Subsequent cluster notes will cover A2.78 determinism preservation (A4.17, A1.13 × A1.10) and A2.80 human-selective composition (A4.18, A1.13 × A1.16). The cluster operationalizes A1.13's five composition requirements one at a time.

## 2. The emergent architectural property — four operational components

The emergent architectural property of A1.13 × A1.07 is *retraceability preservation across composition*. The property has four operational components, taken jointly.

**(a) Per-substrate provenance completeness.** Every piece of substrate content at every composition partner carries the six A2.40 fields — writer, timestamp, antecedent reference, orchestration rule reference, rationale where the plan requires it, and conflict relationship reference. The fields are recorded at every composition partner, not only at primary substrates. A composition partner that records writer attribution and timestamp but omits orchestration-rule references for cell-mediated writes, or records antecedent references for some operations and not others, fails the property at that partner.

**(b) Four-questions answerability at each partner.** The four accountability questions per A2.36–A2.39 — what was decided, by whom, under what authority, with what rationale — are answerable at every composition partner from that partner's substrate content alone. The composed system's auditability is not produced by aggregating partial answers across partners; it is produced by each partner being independently answerable to all four questions for the substrate content it carries, and by the composition preserving the cross-references that let an auditor traverse from one partner to another.

**(c) Cross-substrate provenance preservation.** Operations that cross substrate boundaries — content read from one substrate into another, content written from one substrate to another, conflicts referencing content held in another substrate — preserve provenance at each side of the boundary. The receiving substrate records the antecedent reference back to the originating substrate's content; the originating substrate records the consultation where the orchestration rule requires it. Cross-substrate operations are first-class composition events with first-class provenance, not opaque transitions between locally-retraceable regions.

**(d) Substrate-only paths at each partner.** A1.07's substrate-only-paths property (A2.41) holds at every composition partner. The retraceable path at each partner runs through that partner's substrate content alone, without recourse to external logs, vendor consoles, agent session memory, or LLM internal state. A composition partner whose path runs through a vendor's audit infrastructure satisfies that vendor's audit framework; it does not satisfy A2.41 at that partner, and the composition fails there regardless of how robustly other partners satisfy it.

The four components are jointly necessary and individually insufficient. A composition that satisfies (a), (b), and (d) but loses provenance at cross-substrate boundaries fails the property at the boundaries. A composition that satisfies (a)–(c) but lets one partner's path run through vendor logs fails (d) at that partner. The architectural property is the conjunction across composition, not the disjunction.

## 3. What the composition forces beyond either commitment alone

Four architectural decisions follow from the composition that do not follow from either commitment alone.

*A2.77 architecturally specified through A2.40 fields, uniformly.* A1.13 alone leaves A2.77 as constraint vocabulary — "per-substrate retraceability must be preserved" — without specifying what retraceability is. The composition specifies that A2.40's six fields, A2.36–A2.39's four questions, and A2.41's substrate-only-paths property *are* what retraceability is, by transitivity through A1.07. A composition partner that satisfies A2.77 with a different field set or a different answerability standard is not satisfying A2.77 in the CKS sense; the field set and the answerability standard are A1.07's, made architectural across composition by A1.13.

*Cross-substrate provenance preservation as a first-class composition concern.* Neither commitment alone addresses what happens at the moment content crosses a substrate boundary. A1.07 specifies provenance at writes within a substrate; A1.13 specifies that retraceability must be preserved at every participating substrate. The composition specifies the boundary itself: every cross-substrate operation creates an antecedent edge that must be recorded explicitly, and the edge must be addressable from both ends. The boundary is not a no-op; it is a substrate-resident object with its own provenance.

*Vendor-managed audit logs map to A2.40 architecturally, not as substitution.* Composition partners that operate inside vendor-managed audit infrastructure can participate in a CKS-coherent composition only when the vendor's audit log content maps onto A2.40's six fields at the architectural level — not when the deployment treats the vendor's framework as a parallel audit system substituting for substrate-resident provenance. A vendor framework that records actor, action, and timestamp but lacks orchestration-rule references or antecedent references is internally coherent and CKS-incoherent at the same time; the deployment must either supplement it with substrate-resident A2.40 fields or accept that the partner does not participate in retraceability preservation across composition.

*Primary/secondary asymmetry prohibited.* A common deployment pattern grants primary substrates full provenance fidelity while accepting partial provenance at secondary substrates — those that downstream consumers query but that are not themselves audited as primary records. The composition forbids this pattern. A1.13's per-substrate framing is uniform across participating substrates; A1.07 applies at each substrate. The composition does not admit a "primary preserves, secondary best-effort" stance; the property holds uniformly or fails.

## 4. What the composition is NOT

Four adjacent commitments are commonly conflated with retraceability preservation across composition, and naming what the composition is not preempts the misreadings.

*Not A1.13 alone (the requirement without the specification).* A composition that names A2.77 in deployment documentation but does not record A2.40 fields at each substrate has satisfied the constraint vocabulary without the operational content. The constraint without the specification is unfalsifiable; the composition makes it falsifiable.

*Not A1.07 alone (single-substrate retraceability).* A deployment with a single substrate is satisfying A1.07 without invoking the composition. Retraceability preservation across composition is operationally distinct only when more than one substrate participates; the property does not exist at single-substrate scope.

*Not best-effort provenance.* The property is uniform across composition partners. A deployment cannot claim to preserve provenance "where convenient," "for primary writes," or "for the partners under audit this quarter." Either the four operational components hold at every partner at all times during the composition's existence, or the property does not hold.

*Not retraceability over content the substrate does not carry.* The substrate-only-paths component (d) bounds the property's scope. The composition does not extend retraceability into LLM internal reasoning, parametric memory, agent session state, or external systems whose content the substrate does not address. The path runs through substrate content; what the substrate does not carry is outside the property's reach by design.

## 5. Anti-patterns specifically violating the composition

Five anti-patterns instantiate composition violations.

*Asymmetric provenance across composition.* Primary substrates record full A2.40 provenance; secondary substrates record subsets — writer and timestamp without orchestration-rule references, or rule references without antecedent references. The composition is asymmetric across partners; component (a) fails at the partners with subset provenance.

*Cross-substrate provenance loss.* Content flows from substrate A to substrate B through an orchestration rule that authorizes the cross-substrate operation, and B records the content as a write but does not record the antecedent reference back to A. The composed view loses the path at the boundary; downstream audit queries that begin at B's content cannot traverse to A's source content. Component (c) fails at the boundary.

*Vendor-managed audit logs not mapping to A2.40.* A composition partner uses a vendor's audit infrastructure that records a different field set — actor, action, timestamp, policy decision — without A2.40's orchestration-rule references, rationale fields, or conflict relationship references. The vendor's framework is internally coherent; component (a) fails at that partner because the recorded fields are not A2.40, and component (d) fails because the path runs through vendor infrastructure.

*A3.19 (non-addressable writes) compounded across composition.* Any composition partner that writes to non-addressable storage — append-only logs without record IDs, embedded blobs without addressable structure, vendor-opaque queues — breaks retraceability at that partner because the write cannot be referenced as an antecedent for subsequent writes. In multi-substrate composition the failure compounds: any partner with non-addressable writes is a partner the composed path cannot traverse into or through. The composition fails at every partner whose path needs to cross the offending partner.

*A3.17 (external tool state authoritative) compounded across composition.* Any composition partner whose authoritative state lives in an external tool — a SaaS console's internal state, a workflow engine's queue, a fine-tuned model's parametric memory — loses substrate-only-paths at that partner. The retraceable path leaves substrate rails at the moment it enters the external tool's authority. The composition fails because the path runs through state the substrate does not own; component (d) fails at the affected partner, and any cross-substrate operation that touches the affected partner inherits the failure.

The five anti-patterns share a common structural feature: each makes the composed retraceable path discontinuous at exactly one composition partner or at one cross-substrate boundary, and the discontinuity is what the composition forbids. Naming the anti-patterns precisely is what allows downstream remediation; the failure is local, but the property fails globally.

## 6. Operational test

A multi-substrate composition satisfies retraceability preservation across composition if and only if all of the following are true at every composition partner at all times during the composition's existence:

1. **Per-substrate provenance completeness.** Every piece of substrate content at every composition partner carries the six A2.40 fields — writer attribution, timestamp, antecedent reference (where antecedents exist), orchestration rule reference (for cell-mediated writes), rationale (where the accountability plan calls for it), and conflict relationship reference (for content participating in conflicts).

2. **Cross-substrate provenance preservation.** Every cross-substrate operation — content read from one substrate into another, content written from one substrate to another — preserves provenance at each side: the receiving substrate records an antecedent reference back to the originating substrate's content, and the originating substrate records the consultation where the orchestration rule that authorized the operation requires it.

3. **Four-questions answerability at each partner.** The four accountability questions per A2.36–A2.39 — what was decided, by whom, under what authority, with what rationale — are answerable at every composition partner from that partner's substrate content alone, without recourse to external logs, vendor metadata, LLM session state, or human recollection.

A composition that fails any of (1)–(3) at any composition partner, or at any cross-substrate boundary, does not satisfy retraceability preservation across composition, even when other partners robustly satisfy the property locally. The property is a conjunction across the composition, not an aggregate.

Stated as one sentence: *a multi-substrate composition preserves retraceability across composition if and only if A1.07's six provenance fields and four accountability questions hold at every composition partner, and cross-substrate operations preserve provenance at each side.*

## 7. Why naming this composition as standalone matters

Three load-bearing consequences follow from naming this composition as a standalone architectural property.

First, it operationalizes A2.77 (Requirement B of A1.13) precisely. Without the composition, A2.77 is constraint vocabulary downstream implementations can claim to satisfy without falsification; with it, A2.77 is the conjunction of A1.07's six fields, four questions, and substrate-only paths applied uniformly across composition partners, plus the cross-substrate preservation requirement. Implementations claiming A1.13-coherence have a precise specification to test against, and the test is the operational test in §6.

Second, it makes A4.06 (reproducibility) holdable at composition scale. A4.06 formalizes reproducibility as the conjunction of A1.07 and A1.10 (the determinism contract): a substrate state can be reconstructed by replaying recorded operations from recorded antecedents under recorded rules. Replay across composition partners requires retraceability at each partner; without the present composition, A4.06 holds only at single-substrate scope.

Third, it supports A4.04 (AI-mediated retraceability) at composition scale. A4.04 specifies that AI mediator consultations are recorded as substrate provenance — the cell, the rule, the consultation, the substrate content read or written. The present composition extends this requirement across multi-substrate deployments: when a mediator consults or writes across more than one substrate, each consultation is recorded as substrate provenance at every relevant partner under the cross-substrate provenance preservation component. A4.04 and A4.16 cover different scope dimensions — the mediator's consultations and the substrate boundaries — and together they cover the multi-substrate, AI-mediated case.

The composition layer is independently citable, independently testable, and independently extendable. Subsequent work that adopts the CKS pattern, extends it, or composes it with adjacent multi-substrate audit frameworks should use "retraceability preservation across composition" in the sense formalized here, and should test deployments against the operational test in §6. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Retraceability Preservation Across Composition: The Emergent Architectural Property of Composing CKS's Composition Requirements with Path Retraceability.* May 6, 2026. ORCID: 0009-0004-8065-3235.
