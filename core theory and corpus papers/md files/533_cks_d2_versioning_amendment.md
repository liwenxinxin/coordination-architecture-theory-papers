# FAI Event Versioning and Amendment History

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

D1.22 committed that FAI configuration is substrate content — the six configurable dimensions of the Full Aspect Integration mechanism live in the shared substrate and are subject to the same governance properties as all other substrate content. D2.04 committed that the modify right applies to shared-substrate content and is exercisable by participating governance jointly. D2.38 formalizes the versioning dimension of those two commitments: what happens when governance exercises the modify right to amend FAI configuration during an active event. The note defines the amendment event as a five-field record in the shared substrate, specifies the version history structure for each amendable configuration element, states the three structural properties version histories must satisfy, identifies amendment history analysis across multiple FAI events as a governance intelligence mechanism that feeds into standing configuration improvement, establishes that the FAI configuration version history is the inter-Self analog of Paper 2's DNA version history, and names the invisible amendment as the anti-pattern that violates path retraceability at inter-Self scope. An operational test for conforming implementations is provided.

---

## 1. Derivation position and scope

D2.38 is an operational decomposition of two prior commitments. D1.22 committed that every dimension of the FAI protocol is human-governed and that governance configurations live as substrate content within the shared substrate — inspectable, modifiable, and subject to the same provenance requirements as task content. D2.04 committed that the modify right — one of the three rights that constitute human governance in the CKS pattern — applies to shared-substrate content and is exercisable through joint authority of the participating governance structures.

The question D2.38 addresses is narrower than either parent: when governance actually exercises the modify right to change FAI configuration during an event that is already underway, what does the substrate record? The question matters because FAI events are not always static after construction. Task conditions change. A conflict-handling routing rule that seemed appropriate at construction proves insufficient for the conflicts the event actually generates. A sharing-scope specification that was conservative at initiation can be expanded once governance observes how the shared substrate is being used. A persistence policy can be revised as the significance of the event becomes clearer. The architecture permits these mid-event amendments; D2.38 specifies what governance record they must produce.

---

## 2. The amendment event

When participating governance jointly exercises the modify right to change any element of the FAI configuration during an active event, this produces an **amendment event** in the shared substrate. The amendment event is not a side-effect or a log entry appended by an external system — it is a substrate-content record created by the modify operation itself, carrying the governance properties of all substrate content: provenance, attributability, and subject to the same persistence policy as the event's other content.

Each amendment event carries five fields.

**Field 1 — Amendment ID.** A unique identifier for this amendment within the FAI event's governance record. The amendment ID is scoped to the event; it allows the amendment record to be referenced from other substrate content (for example, from conflict records that triggered the amendment) without ambiguity.

**Field 2 — Amended dimension.** Which element of the FAI configuration was changed. The amendable dimensions include the six named in D1.22 — sharing scope, cardinality, persistence policy, cooperation/competition variant, provenance carry-over depth at the perimeter, and provenance preservation on internalization — as well as any other governance specifications that are substrate content within the event. Naming the amended dimension precisely is what makes the version history navigable: a reader consulting the history knows immediately which configuration axis changed and which did not.

**Field 3 — Prior value.** The configuration value in effect immediately before the amendment. This field is non-optional. Preserving the prior value is what distinguishes a genuine version history from a current-state record: an observer reading Field 3 can reconstruct what governed the event up to the moment of amendment, not merely what governs it afterward. The modify right as CKS specifies it does not delete prior state — it adds a new state, with the prior state preserved as substrate content.

**Field 4 — New value.** The configuration value in effect after the amendment. For the event to proceed coherently after the modify operation, both participating governance structures and the substrate mediators operating within the shared substrate must be able to read the new value as the authoritative current configuration for the amended dimension.

**Field 5 — Amendment authorization.** Which governance authorities jointly authorized this amendment, when authorization occurred, and the governance reasoning that motivated it. This field carries the accountability content that makes the amendment record useful for audit and for organizational learning. The authorization record links the amendment to the human authority that produced it, satisfying the provenance requirements Paper 1 establishes (A1.07) at inter-Self scope. The governance reasoning field is the amendment's equivalent of Paper 1's "rationale" provenance field — it records why the change was made, not merely that it was made.

---

## 3. Version history structure

Each amendable element of the FAI configuration has a **version history** — an ordered sequence of amendment events from the element's initial value at event construction through every subsequent amendment to the current effective value. The version history is substrate content within the shared substrate, subject to the same persistence policy as the event's other Locus 2 content.

Three structural properties are required of every version history.

**Immutability.** Prior versions cannot be deleted or modified; only new versions can be appended. This is the property that distinguishes a version history from a current-state record. The current-state record tells an observer what the configuration is now. The version history tells an observer what it was at any specific moment during the event — which is the question an auditor asks when investigating whether a decision made at hour three of an event was made under the configuration that was in place at hour three, or under an amended configuration that came into force at hour four. A mutable version history cannot answer that question reliably; an immutable one can.

The immutability requirement is inherited from two prior commitments. Paper 2's DNA version history records all governance-authorized changes to DNA-layer content, with prior versions preserved as archived substrate content. Paper 1's path retraceability commitment (A1.07) requires that the substrate carry enough attribution and antecedent information to allow an observer to reconstruct the causal path of any governed decision. Applying path retraceability to the FAI configuration substrate yields immutable version history as a consequence: if prior versions can be deleted, the causal path through configuration state cannot be reconstructed.

**Attribution.** Each version in the history carries full authorization and provenance records — who authorized it, when, under what governance reasoning, and which governance authorities participated. Attribution is what makes the version history an accountability record rather than merely a change log. A change log records what changed; an attributed version history records what changed, who decided it should change, and why.

**Navigability.** An observer can read the version history to understand how the configuration evolved from its initial value to its current value and why each change occurred. Navigability is partly a structural requirement (the history is ordered and complete, with no gaps) and partly a content requirement (the governance reasoning field in each amendment record is populated with enough substance to support retrospective understanding, not merely ritual entries). A version history that is immutable and attributed but opaque — containing amendment records with empty reasoning fields and unidentifiable authorization entries — satisfies the letter of the first two properties while failing the intent of the third.

---

## 4. Amendment history as governance record

The amendment history for an FAI event is part of the Phase 2 governance record (D2.18). As Locus 2 content — content that persists in the shared substrate after the event dissolves, or is transferred to a participating Self's home substrate at dissolution — the amendment history is subject to the persistence policy configured for the event.

For high-stakes FAI events, retaining the full amendment history as Locus 2 content is appropriate. The amendment history documents not only what the participating Selves agreed to do but how their governance adjusted mid-event — which is often where the most significant inter-organizational learning occurs. An event that began with conservative sharing scope and expanded it twice, under joint authorization, tells a different organizational story than an event that operated under its initial configuration throughout. Both stories are important, and both are recoverable only if the amendment history is retained.

The persistence policy for the amendment history is itself a governance decision, configurable per event. Governance may specify that amendment records are retained indefinitely at both participating Selves' home substrates, retained for a fixed period, or retained only for events above a complexity or stakes threshold. Whatever the retention policy, its application to amendment history records is identical to its application to other Locus 2 content — there is no separate retention architecture for governance records.

---

## 5. Amendment history as governance intelligence

Beyond its role in any single event's record, the amendment history is a source of governance intelligence when analyzed across multiple FAI events between the same Selves. The pattern of amendments across events reveals how well the initial configurations — authored under the standing configuration (D2.21) — actually serve the events they govern.

**Frequently amended dimensions indicate miscalibrated initial configurations.** If the conflict-handling routing dimension is amended in seven of ten FAI events between the same two Selves, that pattern is evidence that the standing configuration's initial value for that dimension is systematically wrong for the task class those events serve. The amendment history makes this visible in a way that reviewing final configurations cannot: looking only at end-state configurations, all ten events might appear to have used identical routing specifications; looking at amendment histories, the recurrent mid-event correction becomes apparent.

**Rarely amended dimensions indicate stable initial values.** Dimensions that are almost never amended across a population of FAI events between the same Selves are well-calibrated in the standing configuration. Governance practitioners can treat these dimensions as stable defaults and concentrate calibration attention on the frequently amended ones.

**Amendment triggers reveal pre-authoring opportunities.** When an amendment record's governance reasoning field cites a specific conflict class — "amended conflict-handling routing after conflict class C4 generated three unresolved escalations in the first two hours" — that trigger is evidence that the pre-authored orchestration rules (D2.15) should be enhanced to handle that conflict class without requiring mid-event governance intervention. The amendment history converts lived operational experience into specification input for rule improvement.

This intelligence mechanism is the inter-Self analog of action-feedback evolution in Paper 2. In Paper 2, action-layer accumulation provides evidence that feeds into governed DNA refinement — lived operational experience shaping what is later stabilized as orchestration substrate. At inter-Self scope, amendment history accumulation provides evidence that feeds into standing configuration refinement — lived inter-organizational governance experience shaping what the initial configuration offers in future events. The governing principle is the same: operational records carry learning that initial design cannot anticipate, and the architecture is designed so that learning is recoverable rather than ephemeral.

---

## 6. Inheritance from Paper 2's DNA version history

The FAI configuration version history is the inter-Self analog of Paper 2's DNA version history. In Paper 2, DNA-layer content — stabilized orchestration substrates and policy substrate within a Self — is subject to directed-selection governance: changes to DNA content are authorized by human governance, with prior versions preserved as archived substrate content. The DNA version history records all directed-selection events from a cell's birth through all subsequent governance-authorized DNA changes, with full attribution at each step.

The FAI configuration version history inherits all three structural commitments of the DNA version history: immutable prior versions, full attribution, navigable history from initial value to current value. The structural difference is scope: the DNA version history operates within a single Self's home perimeter, under that Self's governance alone. The FAI configuration version history operates within the shared substrate, under the joint authority of all participating governance structures.

The inheritance is by direct application of Paper 2's DNA-versioning pattern to a new substrate scope, not by analogy. Because the FAI configuration is substrate content (D1.22), and because Paper 2 establishes how substrate content evolves under governance authorization, the version history structure follows immediately from applying Paper 2's DNA evolution commitment to the configuration substrate at inter-Self scope.

---

## 7. Anti-pattern: invisible amendment

The anti-pattern that D2.38 is defined against is the **invisible amendment**: a FAI configuration element that changes during an active event without producing an amendment record in the shared substrate.

The invisible amendment produces a specific and consequential failure: the substrate's stated configuration diverges from the configuration actually in effect at the moment of divergence. An observer reading the substrate at any point after the invisible amendment will see a configuration record that does not match what governed the event from that moment forward. More consequentially, an observer attempting retrospective reconstruction — asking what configuration was in effect when a specific decision was made, or when a specific conflict was handled — cannot answer that question from the substrate alone.

This is a path retraceability violation. Paper 1 (A1.07) requires that substrate content carry enough attribution and antecedent information to allow reconstruction of the causal path of any governed decision. The FAI configuration is part of what governs every decision made within the shared substrate during an event. If the configuration record is inaccurate — because an amendment occurred without being recorded — the substrate cannot support path retraceability for decisions made after the invisible amendment.

The violation applies at inter-Self scope with additional significance because the participating Selves' home substrates may each carry a record of the event that references the shared substrate's configuration. If the shared substrate's configuration record is inaccurate, both Selves' event records inherit that inaccuracy. Correcting an invisible amendment after the fact requires amending governance records across organizational boundaries — a considerably more costly operation than capturing the amendment record at the moment of change.

The operational discipline that prevents invisible amendments is simple: the modify right, when exercised over FAI configuration content, automatically produces an amendment record as part of the modification operation. This is not a separate recording step; it is the same operation. Governance configurations that decompose "modify configuration element" and "record modification" into separable steps create the conditions under which invisible amendments occur.

---

## 8. Operational test

A FAI event implementation satisfies the D2.38 versioning commitment if and only if the following are true for any event in which at least one configuration amendment occurred:

1. An observer with inspect rights over the shared substrate can locate, for each amended configuration element, an amendment record containing all five fields: amendment ID, amended dimension, prior value, new value, and amendment authorization.

2. The prior value field is populated with the value that was in effect immediately before the amendment — the observer can verify this by reading the immediately preceding version in that element's version history and confirming that the prior value field matches.

3. The observer can navigate the complete version history for each amended dimension, from the initial value recorded at event construction through every subsequent amendment to the value in effect at the moment of inspection, with no gaps in the sequence.

4. No version in the history has been deleted or modified after its creation — the history is append-only, and the observer can confirm this through the substrate's standard provenance mechanisms.

5. For events for which amendment history has been retained as Locus 2 content per the event's persistence policy, the amendment records remain accessible after event dissolution.

A system that fails criterion 1 produces invisible amendments. A system that fails criterion 2 records that something changed but not what it changed from — the history is present but insufficient for retrospective reconstruction. A system that fails criterion 3 has gaps in the version history — some configuration evolution is not recorded. A system that fails criterion 4 maintains a mutable history — the record is not a reliable audit trail. A system that fails criterion 5 applies the persistence policy selectively to task content but not to governance records — which is itself a governance record failure.

---

## 9. Conclusion

D2.38 formalizes what governance exercises of the modify right over FAI configuration produce: amendment events with five-field records, composing into version histories that are immutable, attributed, and navigable. The version history for each amendable configuration element is the substrate artifact that makes path retraceability at inter-Self scope achievable: it allows an observer to reconstruct what configuration governed any moment of an active event, not merely what configuration governs it now. Across multiple events, amendment histories are governance intelligence — the accumulated signal from which initial configuration calibration can be improved and pre-authored orchestration rules can be enhanced. The invisible amendment, the anti-pattern that severs this intelligence chain, is a path retraceability violation at inter-Self scope inherited from the same commitment Paper 1 establishes at cell scope and Paper 2 extends to DNA evolution within a Self. D2.38 applies it to the one remaining substrate scope the trilogy establishes: the shared substrate that spans organizational boundaries.
