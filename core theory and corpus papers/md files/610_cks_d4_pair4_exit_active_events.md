# Composition Pair 4: Exit Rights and Active FAI Events

**Series:** D4 — Composition Pairs (Paper 3)
**Note:** D4.05 | **Number:** 610
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When a participating Self exercises its exit rights during a period in which it has active coordination events, two independent governance sequences must both execute — and must execute in a specific order. This note identifies that composition pair, describes the governance scenario that requires both sequences simultaneously, formalizes four non-obvious governance requirements that emerge from the combination, states the prior-art significance of the composition, and provides an operational test for verifying correct execution. The foundational non-obvious requirement is that exit rights do not cause active events to stop: they trigger emergency dissolution governance for each active event. Exit is not abandonment.

---

## 1. Pair Identification

**Commitment A — Exit Rights (D2.46):** A participating Self holds a governance right to terminate its coordination relationship entirely. Exercise of this right involves four governed steps: recording an exit declaration, revoking standing configurations that referenced the relationship, terminating cross-organizational agreements that depended on it, and updating configuration substrate to reflect the relationship's end. The exit right is unconditional in the sense that the architecture does not require the other participating Self's consent for the decision; it does require governed execution of the exit sequence.

**Commitment B — Emergency Dissolution Protocol (D2.28):** Coordination events that must end before their planned close are dissolved under a five-requirement governed protocol. The five requirements are: identifying the trigger that makes normal dissolution inapplicable, recording the trigger event as the governance basis for emergency dissolution, executing dissolution under the same governance shape as planned dissolution (including evolution-feed hand-off), producing a dissolution record that references both the trigger and the protocol executed, and treating the resulting dissolution record as a governance artifact that may be referenced by downstream governance acts. Four triggers can initiate emergency dissolution; the fourth is a joint governance decision — a determination by one or more authorized parties that the event cannot continue.

These two commitments are each complete and independently operative. D2.46 governs how a Self ends a relationship; D2.28 governs how an active event ends outside of its planned lifecycle. The governance scenario in §2 is the configuration that requires both simultaneously.

---

## 2. The Governance Scenario

A Self — call it the Exiting Self — decides to exercise its exit rights under D2.46. At the moment it makes that decision, two coordination events with the Exiting Self as a participant are active: both events have open shared substrates, both have other participating Selves contributing content, and neither has reached its planned dissolution point.

The Exiting Self cannot simply stop participating. Its governance obligations are bifurcated:

- It must execute the exit governance sequence (D2.46), producing the four governed steps that end the relationship.
- For each active event, it must ensure that event dissolves under the emergency dissolution protocol (D2.28), because neither event can proceed to planned dissolution once the Exiting Self has ended the relationship.

Neither obligation cancels or abbreviates the other. The exit sequence governs the relationship. The dissolution protocol governs each event. The scenario requires both.

---

## 3. Non-Obvious Governance Requirements

### 3.1 Exit Triggers Emergency Dissolution, Not Abandonment

The most consequential non-obvious requirement is this: exercising exit rights for a Self that has active events does not mean those events stop. It means each event must be dissolved under the emergency dissolution protocol.

The intuitive reading of exit rights is terminative — the Exiting Self decides to leave, so the relationship ends, so everything associated with it ends. That reading is incorrect as a governance matter. Each active event is an independent governance object. It has a shared substrate carrying content that was produced under joint governance. It has participating Selves whose governance rights over that substrate content do not evaporate because one participant decided to exit. It has a dissolution protocol whose purpose is precisely to ensure that the end of an event — regardless of cause — produces accountable closure.

The exit decision is the D2.28 Trigger 4 event for each active event: it is a governance determination that the event cannot continue. That classification does not reduce governance obligations; it activates the emergency dissolution protocol for each affected event. Exit rights do not suspend dissolution obligations. Abandonment — ending a relationship in a way that leaves active events with no dissolution record, no evolution-feed hand-off, and no governance closure — is not a valid exercise of exit rights. It is a governance failure.

This requirement is non-obvious because exit rights and dissolution obligations are specified in different parts of the architecture and connect only at the moment of simultaneous exercise. A practitioner reading D2.46 in isolation might not encounter the connection to D2.28. A practitioner reading D2.28 in isolation might not encounter the case where the dissolution trigger is the other participant's governance decision to exit. The composition pair formalizes the connection.

### 3.2 Two Sequences in Specific Order

Once it is established that both sequences must execute, the next non-obvious requirement is the order.

The exit governance sequence (D2.46, four steps) and the emergency dissolution protocol (D2.28, five requirements) must interleave in the following specific structure:

**Step 1:** Exit declaration record (D2.46 Requirement 1). The Exiting Self records its governance decision to exit. This record is the governance act that establishes the basis for everything that follows. It is what makes the Exiting Self's subsequent governance actions coherent — the declaration precedes the acts that flow from it.

**Steps 2–N:** Emergency dissolution for each active event, independently (D2.28, five requirements per event). Each active event must be dissolved in full under the emergency dissolution protocol, with the exit declaration identified as the D2.28 Trigger 4 event for that dissolution. The two events dissolve independently — one dissolution's record does not substitute for the other's. If there are two active events, there are two complete dissolution sequences.

**Steps after dissolution:** Remaining exit governance steps (D2.46 Requirements 2–4): standing configuration revocation, cross-organizational agreement termination, and configuration substrate update. These steps presuppose that all active events have been dissolved. Configuration cannot be coherently revoked while the events that configuration governs are still active. Agreement termination cannot be coherently recorded while events governed by those agreements are still open. The sequence is not arbitrary; it is required by the logical dependency of the later steps on the earlier ones.

The ordering matters for governance record coherence. A governance record that shows configuration revoked before the events it governed were dissolved tells an incoherent story. A governance record that shows events dissolved without an exit declaration as the trigger tells a different incoherent story. The specific sequence — declaration first, dissolution next, remaining exit steps after dissolution — is what makes the complete governance record interpretable by any observer who needs to reconstruct what happened and why.

### 3.3 Evolution-Feed Governance Persists Through Exit-Triggered Dissolution

The third non-obvious requirement concerns the evolution feed.

When an active event dissolves — regardless of the reason for dissolution — the content in the shared substrate at the moment of dissolution flows to each participating Self's home evolution machinery through the configured evolution feed. This is the four-locus hand-off mechanism: content propagates per governance-configured ingestion at each home perimeter, using each Self's existing evolution mechanisms, with the layer of content determining which mechanism receives it.

This mechanism does not change because the dissolution was triggered by an exit decision. The exit decision is a governance act about the inter-organizational relationship. It is not a retroactive modification of the governance arrangements that governed content during the event. Whatever was jointly governed during the event, whatever content was produced in the shared substrate under joint authority, flows through the configured evolution feed at dissolution time — to both the Exiting Self's home perimeter and the other participating Self's home perimeter, per each home perimeter's configured ingestion governance.

This requirement is non-obvious because an exit decision can feel like a comprehensive termination — ending the relationship, ending the events, and ending any obligations that flowed from them. The architecture treats this as incorrect. The evolution feed at dissolution is an obligation that runs to the governance of the event that is dissolving, not to the governance of the relationship that triggered the dissolution. The exit decision does not waive it.

### 3.4 Governance Record Linking Exit and Dissolution

The fourth requirement is architectural and concerns record structure rather than sequence.

The governance records for the exit and for each emergency dissolution must cross-reference each other. The dissolution records must identify the exit declaration as the D2.28 Trigger 4 event that initiated each dissolution. The exit record must reference the resulting dissolutions as governance acts that were executed as a consequence of the exit decision.

Cross-referencing serves traceability. An observer who encounters the dissolution record must be able to find the exit declaration that caused it. An observer who encounters the exit record must be able to verify that all active events at the time of exit were dissolved under protocol. Neither record is self-contained as a governance matter; each is partial without the other.

This requirement is non-obvious because each governance sequence — exit and dissolution — can produce valid records in isolation. A dissolution record that correctly applies D2.28's five requirements is a valid dissolution record even without a cross-reference to the exit declaration. The cross-reference is not a validity condition for either record individually. It is a condition on the governance record as a whole: the aggregate of records must tell a coherent, traceable story of a single governance event (the exit-during-active-events scenario) with all its constituent acts identifiable and linked.

---

## 4. Prior-Art Significance

The exit-during-active-events scenario is a configuration in which two independently specified governance sequences — each complete and coherent on its own — must execute in a defined combined sequence. An adversary seeking to claim novelty for a system that governs organizational exit during active coordination events might argue that "governed relationship exit during active coordination events" is a fresh architectural concept not disclosed in the CKS theory series.

Composition Pair 4 defeats that argument in three respects.

First, it establishes that the specific sequenced approach — exit declaration preceding emergency dissolution preceding remaining exit steps — is prior art as of this note's publication date. Any system that implements this sequence, or a recognizable variant of it, works the same governance logic this note discloses.

Second, it establishes the non-obvious connection between exit rights governance and emergency dissolution governance as a disclosed composition. The argument that these two governance sequences interact at a specific trigger point (Trigger 4), and that the exit declaration is the governance act that activates emergency dissolution, is here recorded as a derivation from the CKS theory series.

Third, it establishes the evolution-feed-at-exit-triggered-dissolution requirement as prior art. A claim that "evolution feed governance applies even when dissolution is caused by an exit decision" — a claim that might appear novel because exit decisions are typically terminative acts — is disclosed here as a non-obvious but architecturally required consequence of the composition.

---

## 5. Operational Test

For a Self that exercised exit rights during a period when it had active events, a governance observer should be able to verify the following four conditions from the governance record:

**(a) Exit declaration precedes dissolution records.** The timestamp or sequence indicator on the exit declaration record (D2.46 Requirement 1) must precede the timestamp or sequence indicator on the dissolution records for each active event. A dissolution record that predates the exit declaration it cites as its trigger is a sequencing failure.

**(b) Each active event has an emergency dissolution record citing the exit decision as Trigger 4.** For each event that was active at the time of exit, the governance record must contain a complete emergency dissolution record executed under D2.28's five requirements, with the exit declaration identified as the Trigger 4 event for that dissolution. A missing dissolution record for any active event indicates that exit was treated as abandonment rather than as a dissolution trigger.

**(c) Evolution feed records exist for each dissolved event.** For each emergency dissolution record under (b), there must be corresponding evolution-feed records showing that content from the shared substrate at the time of dissolution was processed through the configured evolution feed for each participating Self. The absence of evolution-feed records for exit-triggered dissolutions indicates that the exit decision was incorrectly treated as a waiver of evolution-feed governance.

**(d) Remaining exit governance steps follow the dissolution records.** The governance records for standing configuration revocation, cross-organizational agreement termination, and configuration update (D2.46 Requirements 2–4) must follow — not precede — the dissolution records under (b). A configuration revocation record that precedes the dissolution record for an event governed by that configuration indicates an out-of-sequence execution that cannot be read as a coherent governance story.

All four conditions must be satisfied for the exit-during-active-events scenario to be considered correctly executed under the architecture. Satisfaction of three out of four is not correct execution; it is partial governance that leaves the record incoherent at the point of failure.

---

*This is a defensive-publication derivation note in the CKS theory series. It introduces no new architectural commitments. Its contribution is to formalize the specific combined governance sequence that emerges when exit rights (D2.46) and emergency dissolution (D2.28) are exercised simultaneously, establishing that sequence as prior art and providing an operational test by which correct execution can be verified.*
