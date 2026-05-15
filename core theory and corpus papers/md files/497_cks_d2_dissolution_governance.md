# Dissolution Event Governance Requirements

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

The shared substrate in the CKS inter-Self coordination architecture is a temporary construction: it is built for a Full Aspect Integration (FAI) event, operates for the duration of that event, and dissolves on the event's completion. Derivation note D1.01 established that dissolution is a governed event — not an automatic cleanup but a coordinated closure subject to the same architectural commitments that governed the substrate's operation. D2.02 formalizes what that governance commitment means operationally. Six requirements must be satisfied for dissolution to be properly governed: three apply at the moment of dissolution and three apply in the period after it. Together they constitute the governed-dissolution criterion. Failure to satisfy any of the six constitutes an anti-pattern — ungoverned dissolution — the inter-Self analog of Paper 2's ungoverned death. Each requirement is formalized below, the satisfaction criterion is stated, the anti-pattern is named, and the inheritance from Paper 2's entity death governance is identified. An operational test enables an observer to verify, for any completed FAI event, whether dissolution was properly governed.

---

## 1. Why dissolution governance requires formalization

The CKS pattern commits to substrate-as-source-of-truth: every governance-relevant event in the substrate's lifetime is recorded as substrate content with provenance. For a substrate that lives for the duration of one FAI event and then dissolves, dissolution is the terminal governance-relevant event. It is the moment at which three things happen simultaneously: the persistence policy (which content survives and in what form) is executed; the hand-off boundary (through which each participating Self receives FAI evolution outputs) is activated; and the shared substrate ceases to operate as the active coordination medium for the event.

Because these three things happen at the same moment, and because each of them has downstream consequences — a durable record that must remain accessible, home substrates that must know what they received, and a provenance chain that must be traceable to its end — dissolution governance cannot be left implicit. An ungoverned dissolution is one in which some or all of these consequences go unrecorded. The shared substrate closes without establishing what it produced, where the content went, and whether the closure itself was authorized. That failure is not a minor gap in bookkeeping; it breaks the accountability architecture the pattern depends on: path retraceability becomes unavailable at precisely the moment when a cross-organizational audit would need to trace events to their conclusion.

D2.02 provides the operational decomposition of D1.01's commitment that dissolution is a governed event. It enumerates the six requirements that governed dissolution satisfies and specifies what each requires.

---

## 2. The three at-dissolution requirements

Three records must be created at the moment of dissolution.

**Requirement 1: Persistence policy execution record.** The persistence policy was authored as substrate content before the FAI event was constructed; it specifies which content, if any, is to be retained after dissolution and where. At dissolution, that policy is executed. The execution must be recorded. The persistence policy execution record documents: which policy was applied (with provenance reference to the authored policy in the substrate), which content was retained (and designated as Locus 2 — the durable record that survives dissolution), which content was dissolved (with no further accessibility commitment), and the governance authorization under which the dissolution proceeded. This record is itself substrate content with provenance. Its existence establishes that the persistence policy was not merely specified but was actually carried out under the authorization that permitted the event to dissolve.

**Requirement 2: Hand-off boundary activation record.** The hand-off boundary is the mechanism through which FAI evolution outputs flow from the shared substrate to each participating Self's home substrate. At dissolution, the hand-off boundary activates. The activation must be recorded. The hand-off boundary activation record documents: which evolution outputs flowed to which home substrate, under which configuration, and with which provenance carry-over depth (the depth at which provenance from the shared substrate is preserved as the outputs enter each home substrate — a governance-configurable dimension of the FAI event's configuration). This record is the dissolution phase's governance artifact for the evolution feed: it establishes, at the perimeter of the shared substrate, that specific outputs traveled to specific destinations under specific configuration. What each participating Self does with those outputs once they cross the home-substrate perimeter is governed by that Self's home governance — Locus 3 governance, outside the scope of the shared substrate's dissolution requirements. The hand-off boundary activation record does not reach into that downstream processing; it documents only that the hand-off happened, what flowed, and under what configuration.

**Requirement 3: Dissolution record.** The dissolution event itself is recorded as the shared substrate's closure record. This is the terminal entry in the shared substrate's provenance chain. Contents of the dissolution record: dissolution timestamp, governance authorization for the closure, confirmation that the persistence policy was executed (referencing the persistence policy execution record from Requirement 1), confirmation that the hand-off boundary was activated (referencing the hand-off boundary activation record from Requirement 2), and reference to the Locus 2 durable record's location, if any retention was specified. After the dissolution record is written, the shared substrate's provenance chain is closed. No further entries are possible. Every event within the shared substrate — from its construction record through its operational history, its conflicts, its governance actions, and now its closure — is traceable to this terminus.

---

## 3. The three post-dissolution requirements

Three ongoing conditions must hold after dissolution.

**Requirement 4: Locus 2 record accessibility.** If the persistence policy specified any retention, the durable record (Locus 2) must be accessible after dissolution. Accessibility here carries specific meaning: the Locus 2 record must satisfy Paper 1's six provenance metadata fields (A1.07 path retraceability) and must remain inspectable under the three governance rights — the right to inspect, the right to modify, and the right to override — exercisable by the participating Selves' governance at any time during the Locus 2 record's existence. The Locus 2 record is not simply a file placed in cold storage. It is a governed substrate record with ongoing accessibility obligations. Whether those obligations are fulfilled by a shared access arrangement between the participating Selves, by a designated custodian organization, or by some other governance-configured mechanism is a deployment decision; the architectural requirement is that the three rights remain available and the six provenance fields remain populated. A Locus 2 record that becomes inaccessible, whose provenance fields become incomplete, or over which the governance rights become unavailable, constitutes an ongoing post-dissolution governance failure — not a one-time failure at the moment of dissolution.

**Requirement 5: Home substrate ingestion records.** Each participating Self must have records in its home substrate of what it received at the hand-off boundary. These records are governed by each Self's home governance — Locus 3 governance — not by the shared substrate's dissolution governance. The distinction matters: Requirement 2 (hand-off boundary activation record) is the shared substrate's record of what flowed at the perimeter; Requirement 5 is each Self's record of what it received and how it processed those inputs. Both must exist, but they sit in different governance perimeters. The shared substrate's dissolution governance establishes only that the hand-off happened under proper configuration (Requirement 2); that each Self maintains its own ingestion records under its own governance is a separate architectural commitment, one that operates at the home-substrate scope and is not contingent on the shared substrate's dissolution having been properly governed.

**Requirement 6: Lineage chain terminus.** The shared substrate's provenance chain is closed at dissolution by the dissolution record (Requirement 3). Requirement 6 completes the cross-perimeter accountability picture: participating Selves' home substrate evolution records that incorporate FAI-derived content must carry cross-references back to the shared substrate's lineage terminus. These cross-references are the mechanism that enables full provenance tracing across the inter-Self boundary. Given a Locus 3 evolution record in either participating Self's home substrate, an auditor can follow the cross-reference back to the shared substrate's lineage terminus, and from there trace forward through the dissolution record to the persistence policy execution record and the hand-off boundary activation record — or backward through the shared substrate's operational history to its construction record. The lineage chain terminus is the anchor point that makes this traversal possible. Without it, the cross-organizational provenance chain is broken: the home substrate's evolution records exist, the shared substrate's operational records exist, but they are not linked.

---

## 4. The satisfaction criterion

Dissolution is properly governed if and only if all six requirements are satisfied:

**(a)** The persistence policy execution record exists, documents which policy was applied, and carries governance authorization for the dissolution.

**(b)** The hand-off boundary activation record exists, documents what flowed to each home substrate, and records the configuration and provenance carry-over depth under which the flow occurred.

**(c)** The dissolution record exists as the terminal entry in the shared substrate's provenance chain, with timestamp, governance authorization, and cross-references to (a) and (b).

**(d)** If the persistence policy specified retention, the Locus 2 durable record is accessible post-dissolution, satisfies Paper 1's six provenance metadata fields, and remains subject to the three governance rights.

**(e)** Each participating Self's home substrate carries ingestion records under that Self's home governance.

**(f)** Participating Selves' home substrate evolution records carry cross-references back to the shared substrate's lineage chain terminus.

A dissolution that satisfies (a)–(f) is fully governed. A dissolution that satisfies (a)–(c) but fails (d)–(f) has properly closed the shared substrate but left post-dissolution governance obligations unmet. A dissolution that fails any of (a)–(c) is ungoverned at the moment of closure.

---

## 5. Anti-pattern: ungoverned dissolution

Ungoverned dissolution is the inter-Self analog of Paper 2's ungoverned death (B3.11 in the Series B derivation notes). Paper 2 identifies ungoverned death as the failure mode in which a cell or aspect is retired, archived, or deleted without the governance records that would permit retrospective audit of the retirement decision. Ungoverned dissolution is the same failure at the inter-Self perimeter: the shared substrate closes, but one or more of the conditions for governed closure are unmet.

Three variants of ungoverned dissolution are architecturally distinct:

**Silent closure.** The shared substrate ceases to operate without a dissolution record. No governance authorization is recorded, no confirmation of persistence policy execution exists, and no hand-off boundary activation record is created. The substrate content that was present simply stops being accessible, with no documented basis for what happened to it. This is the most complete form of ungoverned dissolution.

**Partial execution.** The dissolution record is created, but the persistence policy execution and hand-off boundary activation are not properly recorded. The shared substrate has a documented closure but no traceability to what was retained, what was dissolved, or what flowed to each home substrate. An auditor can establish that the substrate closed; they cannot establish what it produced.

**Policy violation.** The dissolution record is created and the execution records exist, but content that the persistence policy did not authorize to persist has persisted — either in Locus 2 beyond policy scope, or flowing through the hand-off boundary under a configuration that was not authorized. The governance records exist but do not accurately reflect what actually occurred.

All three variants break the accountability architecture at the inter-Self perimeter. They leave the participating Selves with evolution outputs in their home substrates whose provenance chain terminates in unresolvable ambiguity rather than in a documented, authorized closure. The defensive-publication priority for this anti-pattern is high: ungoverned dissolution is the most natural failure mode of a temporary shared substrate, because temporary structures create pressure to treat closure as cleanup rather than governance.

---

## 6. Inheritance from Paper 2

D2.02 inherits two structures from Paper 2 without redefense.

**Entity death governance (B1.07 / B0.03).** Paper 2 commits that entity death — at cell, aspect, or Self level — is a governed retirement decision, not an autonomous outcome of system dynamics. The governed death record documents the retirement decision, its authorization, and the archival state of the retired entity. D2.02 applies the same structure at the inter-Self perimeter: the shared substrate's dissolution is a governed closure decision with a documented record (Requirements 1, 2, and 3) and a specified archival state (Requirement 4). The dissolution record is the inter-Self analog of the entity death record — the substrate-content artifact that closes the lifecycle of the governed structure and establishes the basis for retrospective accountability.

**Archival reactivatability (B2.54).** Paper 2 commits that archived cells remain substrate-addressable after retirement — death in the lineage-supersession case is operational retirement, not deletion of state. Locus 2 record accessibility (Requirement 4) is the inter-Self analog: if content is retained at dissolution, it remains governed and accessible. The specific mechanism differs at the inter-Self scope (the durable record is a governed substrate artifact under joint authority rather than an archived cell under single-Self governance), but the architectural commitment — that retention creates ongoing accessibility obligations rather than producing a file that sits unaddressed — carries over directly.

---

## 7. Operational test

For a completed FAI event, an observer can verify that dissolution was properly governed by asking six questions — one per requirement:

1. Does a persistence policy execution record exist for this event? Does it identify which policy was applied, which content was retained (Locus 2), which was dissolved, and under what governance authorization?

2. Does a hand-off boundary activation record exist? Does it document which evolution outputs flowed to which home substrate, the configuration under which they flowed, and the provenance carry-over depth?

3. Does a dissolution record exist as the terminal entry in the shared substrate's provenance chain? Does it carry a dissolution timestamp, governance authorization, and cross-references to the execution records from (1) and (2)?

4. If the persistence policy specified retention: is the Locus 2 durable record currently accessible? Does it carry Paper 1's six provenance metadata fields (attribution, event scope, governance authorization, conflict notes, decision rationale, modification history)? Can the three governance rights be exercised over it?

5. Does each participating Self's home substrate carry ingestion records for what it received at the hand-off boundary from this event?

6. Do the home substrate evolution records that incorporated FAI outputs from this event carry cross-references back to the shared substrate's lineage chain terminus?

A completed FAI event satisfying all six questions is fully governed at dissolution. An event failing any question has a specific, identifiable governance gap. The test is executable without access to the shared substrate itself — only to the dissolution records, the Locus 2 durable record (if any), and the participating Selves' home substrate records. This is by design: the dissolution governance architecture is auditable from the outside, without requiring the auditor to reconstruct the shared substrate's operational state.

---

## Source papers

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Dissolution Event Governance Requirements.* May 14, 2026. ORCID: 0009-0004-8065-3235.
