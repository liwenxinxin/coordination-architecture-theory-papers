# Three FAI Persistence Loci as Distinct Governance Objects

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note ID:** D1.11 — #476 in the CKS Derivation Note Series
**Parent claim:** Paper 3 Claim 2 (Full Aspect Integration as the canonical operation over the shared substrate)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When a Full Aspect Integration (FAI) event completes and its shared substrate dissolves, the content that existed within that substrate does not converge to a single governed location. It distributes across three structurally distinct persistence loci, each with its own governance mechanism and its own governance authority. This note formalizes the three-locus structure as an architectural sub-commitment of Paper 3 Claim 2: (1) the live shared substrate during the event, jointly governed by all participating Selves under the six Paper 1 commitments; (2) the durable record after dissolution, governed by the jointly authored persistence policy; and (3) each Self's home substrate evolution outputs, governed independently by each Self's own home governance. The note explains why these are three different authorities governing three different objects — not one authority governing three content containers — and why this distinction is what preserves each Self's governance sovereignty when participating in inter-organizational FAI events. It further formalizes that an empty Locus 2 (a persistence policy that retains nothing) is a governed outcome, not an absence of governance.

---

## 1. The sub-commitment stated

Paper 3 Claim 2 establishes Full Aspect Integration (FAI) as the canonical operation over the shared substrate. Among its architectural commitments is a specification of what happens to the content produced by an FAI event — not just while the event is active, but across the full lifecycle from initiation through dissolution and into whatever persists afterward. That specification is the subject of this note.

The sub-commitment is this: **content from a Full Aspect Integration event persists in three distinct loci, each governed by a different mechanism and a different authority.** These are not three labels for the same governed mass of content at different timestamps. They are three structurally distinct governance objects with different perimeters, different authorities holding governance rights over them, and different mechanisms by which those rights are exercised.

This distinction matters architecturally because conflating the three loci leads to one of several governance errors: applying joint authority to content that each Self's home governance should control independently; treating the absence of a durable record as an absence of governance; or assuming that what a Self ingests from an FAI event is somehow constrained by the joint authority of the other participating Selves. Each of these errors produces a system that is either ungoverned where it should be governed or jointly governed where it should be independently governed. The three-locus structure prevents all four failure modes identified at the close of this note.

---

## 2. Locus 1 — The live shared substrate during the event

The first persistence locus is the shared substrate itself while the FAI event is active. This is the live coordination medium: the architectural object through which participating Selves contribute aspects, surface conflicts, record provenance, and make the governance decisions that shape the event's outputs.

**Content.** Locus 1 contains all contributed aspect content — both DNA-layer content (orchestration substrates, behavior substrates, schemas, rules) and action-layer content (recorded task instances, outputs, lived experience). It contains all conflicts registered as first-class objects under Paper 1 Claim 3's conflict-preservation commitment. It contains all provenance records and all governance decisions made during the event, including the persistence policy that will govern the Locus 1 → Locus 2 transition.

**Governance mechanism.** The six Paper 1 commitments apply within the shared substrate's perimeter: substrate-as-coordination-artifact, human-governed, conflict-as-first-class-object, AI-as-substrate-mediator, tool-agnosticism, and linear-cost scaling. The three governance rights — inspect, modify, override — apply to Locus 1 content during operation. These rights are available to the human governance structures of all participating Selves within the shared perimeter.

**Governance authority.** Locus 1 is jointly governed by all participating Selves' governance structures. No single Self's home governance holds unilateral authority over Locus 1 content; the authority is joint across the participating perimeters. This is what makes Locus 1 a genuinely shared coordination medium rather than one participant's substrate to which others have temporary access.

**Lifecycle.** Locus 1 exists only while the FAI event is active. At dissolution — when the event completes — Locus 1 terminates. It does not persist as a live coordination medium after dissolution. What survives dissolution is determined by the Locus 1 → Locus 2 transition governed by the persistence policy, described in Section 4.

---

## 3. Locus 2 — The shared substrate as durable record after dissolution

The second persistence locus is the durable record of the FAI event — the portion of Locus 1 content that is retained after dissolution as an inter-organizational artifact. Locus 2 is what the persistence policy governs.

**Content.** Locus 2 is a subset of Locus 1. Its content ranges across a spectrum: at one extreme, nothing is retained (Locus 2 carries zero content); at the other extreme, the full shared substrate is retained as an auditable record of everything that occurred during the event. Between these poles, any selective policy is architecturally permissible — retaining, for instance, only conflict records and their resolutions, or only the governance decisions, or only the provenance map.

**Governance mechanism.** The persistence policy governs Locus 2. The persistence policy is itself substrate content — authored as jointly governed content during the event (Locus 1), and therefore carrying the same governance properties as any other Locus 1 content. The persistence policy specifies what of Locus 1 is retained after dissolution and under what terms. Because the policy is authored under joint authority during the event, the resulting Locus 2 is a jointly governed artifact even after the live shared substrate dissolves.

**Governance authority.** Locus 2 is governed by the joint authority of participating Selves' governance structures, as embodied in the persistence policy. The policy was authored under that joint authority; its execution at dissolution is the exercise of that authority over the surviving record.

**The empty case.** A persistence policy that specifies "retain nothing" produces a Locus 2 with zero content. This is an important boundary case: zero content is not the same as zero governance. The decision to retain nothing was made under the joint authority of participating Selves' governance structures, recorded in the persistence policy as substrate content during the event, and executed at dissolution as a positive governance outcome. The absence of a durable record is itself a governed result. A system in which no persistence decision was made and nothing was retained would be missing governance; a system in which the governance decision was made and the outcome was "retain nothing" is fully governed, with an empty Locus 2.

---

## 4. The Locus 1 → Locus 2 transition (dissolution)

At dissolution, the live shared substrate of Locus 1 terminates as a coordination medium. The persistence policy — authored as Locus 1 content during the event — specifies which portions of Locus 1 survive into Locus 2. Everything not retained by the persistence policy ceases to exist as a governed object when Locus 1 dissolves.

The transition is governed: the persistence policy was authored under joint authority and is itself inspectable, modifiable, and overridable substrate content. The transition is not automatic, opaque, or implementation-determined. It executes according to a human-authored policy that was made available for governance before dissolution.

Several consequences follow. First, the timing of the persistence policy's authorship matters architecturally: it must be authored during the event (as Locus 1 content under joint authority), not after dissolution (when joint authority over Locus 1 has already terminated). A persistence policy authored post-hoc, outside the shared substrate's governance perimeter, is not subject to joint authority and therefore does not satisfy the sub-commitment. Second, the persistence policy's scope covers whatever dimensions the participating Selves' governance structures choose to configure; no fixed set of retained elements is architecturally mandated. Third, once Locus 1 dissolves and the persistence policy has executed, the resulting Locus 2 is the inter-organizational record; the live coordination medium is gone.

---

## 5. Locus 3 — Each Self's home substrate evolution outputs

The third persistence locus is what each participating Self ingests into its home substrate from the FAI event. This is the evolution-feed pathway described in Paper 3 Claim 4: at the FAI hand-off boundary, Locus 1 content designated as evolution feed flows into each Self's home substrate under each Self's home governance.

**Content.** Locus 3 content is governance-configured by each participating Self independently. Self A's home governance determines what Self A ingests from the FAI event's outputs; Self B's home governance determines what Self B ingests. The same FAI event can produce asymmetric Locus 3 content across participating Selves: one Self may ingest the full evolution feed; another may ingest only selected portions; a third may ingest nothing. No architectural requirement of symmetric absorption exists.

The layer-routing rule from Paper 3 Claim 4 governs what the ingested content reaches: DNA-layer content feeds DNA evolution at each home perimeter; action-layer content feeds action-feedback evolution; instinct evolution takes no FAI input by architectural commitment, because LLM weights and instinct-layer content do not cross the inter-Self boundary per the FAI exchange-bounding commitment.

**Governance mechanism.** Each Self's home governance mechanisms govern Locus 3 independently. These are Paper 2's governance structures operating at home perimeter: the per-mechanism governance shapes (verification-substrate machinery for instinct integration, authority architecture for DNA evolution, proposal-and-acceptance machinery for action-feedback), with the FAI-derived content arriving as an additional input source rather than as a replacement for or modification of those existing mechanisms.

**Governance authority.** This is where Locus 3 is structurally distinct from Loci 1 and 2. Locus 3 is not jointly governed. Each Self's home governance holds independent authority over what that Self ingests. The joint authority of the participating Selves — which governs Locus 1 during the event and Locus 2 through the persistence policy — does not extend into any Self's home substrate. What Self A does with FAI evolution outputs in its home substrate is a home governance decision. Self B cannot determine or constrain Self A's ingestion decisions; Self A cannot determine or constrain Self B's.

---

## 6. Why Locus 3 is not jointly governed: governance sovereignty

The independence of Locus 3 governance is not an oversight in the architecture. It is the architectural property that makes inter-organizational FAI participation safe for each Self.

If the joint authority of the FAI event extended into each participating Self's home substrate — if the other Selves could determine or constrain what a Self ingests — then participation in an FAI event would require each Self to surrender some portion of its home governance sovereignty. The scope of that surrender would expand with each FAI event participated in. Over many events, a Self's home governance would increasingly reflect the accumulated governance decisions of other Selves rather than its own home authority.

The three-locus structure prevents this. The joint authority of the FAI event terminates at dissolution. It governs Locus 1 during the event and Locus 2 as the durable record. It does not govern Locus 3. What each Self absorbs from the event is governed entirely by that Self's home governance, which remained sovereign throughout the event and continues sovereign afterward.

This is the architectural basis for inter-organizational FAI as a coordination mechanism that does not require trust in the sense of delegation: participating Selves do not delegate home governance authority to the joint authority of the event. They bring their home governance into a shared coordination medium for the duration of the event, operate within it under joint authority, and then retrieve the outputs into their home substrates under their own governance. The shared coordination medium is temporary and bounded; home governance is permanent and sovereign.

The practical implication is that each Self retains full control over the effect an FAI event has on its home substrate. The event may have produced coordination outputs, resolved conflicts, and surfaced evolution-feed content — but whether and how each Self incorporates those outputs into its home substrate is not determined by the event, by the other participating Selves, or by the joint authority that governed the shared substrate. It is determined by each Self's own governance, applied at its own home perimeter.

---

## 7. The three governance mechanisms distinguished

For precision, the three governance mechanisms are stated side by side:

**Locus 1 — Live shared substrate during the event.** Governance mechanism: joint authority of all participating Selves' governance structures, with the six Paper 1 commitments applying within the shared substrate perimeter. Rights: the three governance rights (inspect, modify, override) held by the participating Selves' governance structures, exercisable at any time during the event. Scope: all contributed content, all conflicts, all provenance, all governance decisions including the persistence policy.

**Locus 2 — Durable record after dissolution.** Governance mechanism: the persistence policy, authored as Locus 1 content under joint authority. Rights: those specified in the persistence policy for the surviving record; the joint authority that authored the policy determined the scope and terms of the surviving record's governance. Scope: whatever content the persistence policy specifies as retained, including the empty set.

**Locus 3 — Each Self's home substrate evolution outputs.** Governance mechanism: each Self's independent home governance, applied at each home perimeter under Paper 2's per-mechanism governance shapes. Rights: held by each Self's human governance independently, not subject to any constraint from the other participating Selves' governance or from the joint authority of the event. Scope: whatever each Self's home governance authorizes for ingestion from the FAI evolution feed.

These are not the same authority governing three different containers. They are three different authorities — joint event authority, persistence-policy-bounded joint authority, and independent home authority per Self — governing three different objects.

---

## 8. Four failure modes this sub-commitment defends against

**Failure mode 1 — Treating all three loci as one governance object.** An implementation that governs Locus 1, Locus 2, and Locus 3 through a single undifferentiated governance mechanism has collapsed three distinct governance objects into one. The consequences depend on which authority is applied uniformly: if joint authority governs Locus 3, each Self's home governance sovereignty is violated; if home governance governs Locus 1, the shared substrate loses its inter-organizational governance coherence; if no governance applies uniformly, the evolution-feed pathway is ungoverned at some point in the lifecycle.

**Failure mode 2 — Home governance over the shared substrate.** An implementation in which one participating Self's home governance holds unilateral authority over Locus 1 content is not a shared substrate — it is one Self's substrate to which others have been granted access. The architectural property of joint authority within the shared perimeter does not exist in such an implementation. Conflicts, provenance records, and governance decisions within what purports to be a shared substrate may be modified or overridden by one Self without the other Selves' governance authority applying. This is a Locus 1 governance failure with downstream consequences for the integrity of Locus 2 (whose persistence policy was authored under corrupted joint authority) and potentially for Locus 3 (whose evolution feed originates from a Locus 1 that was not genuinely jointly governed).

**Failure mode 3 — Joint authority over what each Self ingests.** An implementation in which the joint authority of the FAI event, or any participating Self's governance, constrains what another Self ingests into its home substrate has extended the event's governance beyond its proper perimeter. Locus 3 is not within the shared substrate's perimeter. The joint authority terminates at dissolution. Post-dissolution constraints on what a Self absorbs from the evolution feed — whether imposed by technical architecture, by governance agreement terms, or by the persistence policy — constitute a claim of joint authority over Locus 3 that this sub-commitment rules out. Each Self's home governance is sovereign over its home substrate, including the evolution-feed ingestion decisions made at the home perimeter.

**Failure mode 4 — Treating an empty Locus 2 as absent governance.** An implementation that infers, from the absence of a durable record, that no governance decision was made about persistence has misread the architecture. The persistence policy governs the Locus 1 → Locus 2 transition. A persistence policy specifying "retain nothing" is a governance decision that produces a zero-content Locus 2. An implementation that does not track, record, or make inspectable the persistence policy's specification — relying instead on the absence of a durable record as implicit evidence of the policy — has made the governance decision uninspectable. The three governance rights (inspect, modify, override) apply to the persistence policy itself as Locus 1 content. An uninspectable persistence policy violates the six Paper 1 commitments within the shared substrate perimeter.

---

## 9. Operational test

After a Full Aspect Integration event has completed and the shared substrate has dissolved, an authorized observer should be able to conduct the following independent verification:

**For Locus 2:** Locate the persistence policy that was authored as substrate content during the event. Read the policy's specification of what was to be retained. Verify that the durable record (if any) matches the policy's specification. If the policy specified "retain nothing," verify that no durable record exists and that the policy's own record is available for inspection. The persistence policy must be findable and readable independently of the event's participants' representations about what was retained.

**For Locus 3:** For each participating Self, locate the records of the home governance decision about what evolution-feed content was ingested from the event. These records exist within each Self's home substrate governance records — not in the shared substrate or in any jointly maintained artifact. For Self A, the observer consults Self A's home governance records. For Self B, the observer consults Self B's home governance records. The ingestion decisions are independent; the records are independent; neither Self's ingestion decision should be derivable from the other Self's governance records.

If the observer can independently locate and verify Locus 2 through the persistence policy, and can independently locate and verify Locus 3 ingestion decisions in each Self's home governance records without cross-referencing the other Selves' records, the implementation satisfies the three-locus sub-commitment. If either verification fails — because the persistence policy is not independently findable, because the durable record does not match the policy, because one Self's Locus 3 content appears to be constrained by another Self's governance records, or because the evolution-feed ingestion decisions cannot be found in the home governance records — the implementation has not instantiated the three-locus governance structure.

This test is an independence test: each locus should be verifiable through its own governance mechanism, through its own governance authority's records, without requiring access to either of the other loci's governance records to confirm what was decided. Independence of verification tracks independence of governance.

---

## 10. Summary

Full Aspect Integration produces three persistence loci that are distinct governance objects, not three containers managed by the same governance authority:

- **Locus 1** (live shared substrate during the event) is jointly governed by all participating Selves under the six Paper 1 commitments, and terminates at dissolution.
- **Locus 2** (durable record after dissolution) is governed by the jointly authored persistence policy, ranges from nothing retained to the full substrate retained, and is a governed outcome even when its content is the empty set.
- **Locus 3** (each Self's home substrate evolution outputs) is governed independently by each Self's home governance, is asymmetric across participating Selves by design, and is not subject to the joint authority of the event or the governance of any other participating Self.

The joint authority of the FAI event governs Loci 1 and 2. Each Self's independent home authority governs its own Locus 3. This distribution of authority is what makes inter-organizational coordination through FAI compatible with governance sovereignty: each Self participates in the shared coordination medium without surrendering authority over what it takes home from it.
