# AP-2: Ungoverned Dissolution

**Derivation Note 578 — Phase D3, Anti-Pattern Formalization**
**Series:** CKS Defensive Publication Series, Phase D3 (Anti-Pattern Formalizations)
**Note number in series:** D3.03

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

A shared substrate constructed for a Full Aspect Integration (FAI) event is a temporary artifact with a governed lifecycle. Dissolution — the close of that lifecycle — is itself a governed event: it must produce a dissolution record, a persistence policy execution record, and a hand-off boundary activation record for each participating Self. When a shared substrate ceases operation without any of these records, the failure is Ungoverned Dissolution (AP-2). This note formalizes AP-2 as the first Lifecycle Governance Failure in the Phase D3 anti-pattern taxonomy, specifying its description, four detection criteria, two violated governance commitments, five consequences, its structural analog at intra-Self scope (Paper 2 B3.11, Ungoverned Death), and its complete resolution path. The note draws a precise boundary between AP-2 and emergency dissolution: emergency dissolution is governed dissolution executed under urgent circumstances; ungoverned dissolution is dissolution without any governed closure act. The difference is categorical, not one of degree.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-2 — Ungoverned Dissolution

**Taxonomy category:** 1 — Lifecycle Governance Failures

**One-sentence statement:** A shared substrate that ceases operation without a dissolution record, a persistence policy execution record, or a hand-off boundary activation record, leaving the closure of the FAI event without any governance documentation.

---

## 2. Description

### 2.1 The governance commitment dissolution carries

Paper 3 Claim 1 establishes the shared substrate as a temporary construction: it is built across the perimeters of participating Selves for the duration of a FAI event and dissolves at that event's close. The temporary character is not incidental; it is an architectural commitment. A shared substrate is not a permanent multi-party repository. It is an event-bounded coordination object, and its dissolution is as much a governed act as its construction.

Governed dissolution produces three records. The **dissolution record** documents what happened at event closure: which participants were present, what content the shared substrate held at dissolution, the date and conditions of closure, and whether dissolution was planned, unplanned, or emergency. The **persistence policy execution record** documents the disposition of Locus 2 content — content that the shared substrate held at a persistence locus with a governance-determined retention or release outcome — confirming whether that content was retained, released, or deleted in accordance with the policy the substrate carried. The **hand-off boundary activation record** documents what content flowed from the shared substrate to each participating Self's home substrate at dissolution, under what ingestion configuration, and through which of Paper 2's evolution mechanisms at each home perimeter.

These three records are not documentation overhead appended to dissolution. They are what makes dissolution a governed event in the CKS sense. Without them, the FAI event ends — through completion, abandonment, or technical failure — but the governance architecture that makes FAI coordination meaningful has not closed. The event ends; the governance does not.

### 2.2 What ungoverned dissolution is — and what it is not

Ungoverned dissolution is the condition in which a shared substrate ceases operation without producing any of the three records named in §2.1. The shared substrate may have dissolved because the FAI event reached its natural completion, because participating Selves abandoned the coordination, or because a technical failure terminated the substrate. The cause of cessation is not what distinguishes ungoverned dissolution. What distinguishes it is the absence of any governed closure act.

This places ungoverned dissolution in a different category from **emergency dissolution**, which D2.02 governs directly. Emergency dissolution occurs when a shared substrate must be closed under urgent circumstances — system failure, unresolvable conflict, withdrawal of a participating Self — and the full dissolution workflow cannot be executed in the normal sequence. D2.02 specifies five requirements for emergency dissolution, and the dissolution record requirement is among them. Emergency dissolution is therefore still governed dissolution: the urgency changes the timeline and the sequence of governance acts, but it does not eliminate the governance requirement. A shared substrate that closes under emergency conditions but still produces the dissolution record, even in compressed or partial form, is not an instance of AP-2.

AP-2 is the condition in which no dissolution record was produced — emergency or otherwise. The distinction matters for remediation: a discovered emergency dissolution record, however spare, provides something to audit. A discovered absence of any dissolution record is the anti-pattern this note addresses.

### 2.3 The three record types as a complete closure set

The three records are individually necessary and jointly sufficient for governed dissolution. A dissolution record without a persistence policy execution record documents closure but leaves Locus 2 content status unknown: governance cannot confirm whether retained content was authorized or whether released content was authorized. A dissolution record and a persistence policy execution record without a hand-off boundary activation record document closure and Locus 2 disposition but provide no basis for auditing what entered participating Selves' home substrates. All three must be present for dissolution to be governed in the sense Claim 1 requires.

---

## 3. Detection Criteria

AP-2 is present when one or more of the following are true:

**Criterion 1 — Missing dissolution record.** The shared substrate no longer exists or is inactive, but no dissolution record can be located through the governance records of any participating Self or of the shared substrate's host environment. The shared substrate's lifecycle ended without documented closure.

**Criterion 2 — Untraced FAI-origin content.** Content appears in one or more participating Selves' home substrates attributed to a specific FAI event, but no hand-off boundary activation record documents the flow from that event's shared substrate to the home substrate. The home-substrate content is the symptom; its presence without a corresponding hand-off record is the detection signal. This criterion is the most common route by which AP-2 surfaces: governance discovers the anti-pattern not at dissolution but later, when FAI-origin content in a home substrate cannot be traced to a governed hand-off.

**Criterion 3 — Missing persistence policy execution record.** The persistence policy for the shared substrate cannot be located, or the policy exists but no execution record documents what Locus 2 content was actually retained or released at dissolution. The disposition of Locus 2 content is unknown: governance cannot determine whether retained content was authorized by the policy or whether released content was authorized by the policy.

**Criterion 4 — No joint dissolution agreement on record.** Governance of the participating Selves cannot produce documentation of what was jointly agreed to happen at dissolution — which content would flow to which Selves, under what ingestion configuration, under what persistence policy. Participating Selves' governance records are individually silent on the event's closure terms.

---

## 4. Governance Commitment Violated

**Primary violation — Paper 3 Claim 1 (dissolution as governed event, per D1.01 temporary construction).** Claim 1 establishes the shared substrate as a temporary construction with a governed lifecycle. The temporary character entails that dissolution is itself a governed act, not merely an outcome that happens when coordination ends. A shared substrate that ceases operation without producing the three governance records violates the foundational property Claim 1 commits to: that the shared substrate's lifecycle, end-to-end, is under human governance. Dissolution without records is dissolution outside human governance.

**Secondary violation — Paper 1 A1.07 (path retraceability).** A1.07 commits the CKS architecture to path retraceability: any output or content the substrate produces must be traceable, step by step, to the governance acts that authorized it. FAI-origin content in a participating Self's home substrate is an output of the FAI event and of the dissolution hand-off. When no hand-off boundary activation record exists, the path from the FAI event to the home-substrate content is broken. The content exists; the governance path that authorized its entry into the home substrate does not. A1.07 is violated whenever FAI-origin content enters a home substrate through an ungoverned dissolution.

**Operational reference — D2.02 (dissolution event governance requirements, six requirements).** D2.02 specifies three at-dissolution requirements and three post-dissolution requirements that together constitute governed dissolution. AP-2 is, operationally, the failure mode in which the at-dissolution requirements were not executed.

---

## 5. Consequences

**Consequence 1 — Broken provenance chain on FAI-origin content.** Content that entered a home substrate through an ungoverned dissolution carries a broken provenance chain. The content exists in the home substrate; the governance act that authorized its entry does not. This is a provenance break of the type described at D2.67 (break type 2): content present in the substrate without a traceable authorization path.

**Consequence 2 — Unauthorized evolution feed entry.** The four-locus evolution feed mechanism at the FAI hand-off boundary (Paper 3 Claim 4) requires that content propagating from a dissolving shared substrate to each participating Self's home substrate does so under governance-configured ingestion at the home perimeter. An ungoverned dissolution bypasses this configuration: content enters the evolution feed without a governing ingestion decision having been made and recorded. The evolution feed has been activated without authorization.

**Consequence 3 — Unresolvable post-dissolution disputes.** D2.45 addresses disputes that arise after an FAI event closes — disputes about what was agreed, what content was supposed to flow to which Self, and under what terms. The dissolution record is the primary artifact against which such disputes are resolved. When no dissolution record exists, post-dissolution disputes cannot be resolved by reference to governance documentation. Participating Selves may have divergent recollections of closure terms, with no authoritative record to adjudicate between them.

**Consequence 4 — Unknown Locus 2 content status.** Locus 2 content — content held at the persistence locus with a governance-determined disposition outcome — may have been retained in the shared substrate's host environment, released to one or more Selves, or deleted. Without a persistence policy execution record, the disposition is unknown. Content may have been inappropriately retained (creating an ongoing privacy or governance exposure) or inappropriately lost (destroying content that should have survived dissolution). Neither can be diagnosed without the record.

**Consequence 5 — Regulatory audit failure.** D2.63 addresses regulatory and compliance audits of FAI event histories. An ungoverned dissolution leaves a gap in the governance record that a regulatory audit cannot bridge. The audit can establish that the shared substrate existed and that FAI activity occurred; it cannot establish what happened at event closure or whether dissolution was authorized and compliant. The gap is not a documentation deficiency that supplemental records can remedy: the at-dissolution acts either occurred and were recorded or they did not occur.

---

## 6. Intra-Self Analog

AP-2 is structurally identical, at inter-Self scope, to **Paper 2 B3.11 (Ungoverned Death)**: an entity that ceases operation within a home substrate without a death record or governance-authorized closure act.

The structural identity is precise. In both cases: a governed lifecycle ends without the governance records that close it; content that was produced by the entity persists in the system without a traceable authorization path; downstream governance cannot reconstruct what happened at closure; and the absence of records is the anti-pattern rather than the fact of cessation. Whether the ceasing entity is an intra-Self record-entity (B3.11) or an inter-Self shared substrate (AP-2), the architecture's response is the same — dissolution is a governed event, and a governed event that produces no governance records has not been governed.

The scope difference is consequential for remediation: an ungoverned death within a single Self's home substrate affects that Self's internal governance; ungoverned dissolution of a shared substrate affects the governance of every participating Self and the integrity of content in every participating Self's home substrate that bears FAI-origin attribution. AP-2 therefore has a wider governance surface and, correspondingly, a more complex remediation path.

---

## 7. Resolution

### 7.1 Prevention: D2.02's six dissolution governance requirements

AP-2 is prevented in its entirety by executing D2.02's six dissolution governance requirements. Three requirements apply at dissolution: (1) the dissolution record must be produced, documenting participants, content at dissolution, date, and conditions of closure; (2) the persistence policy must be executed and the execution recorded; (3) the hand-off boundary activation record must be produced for each participating Self, documenting what content flowed to which home substrate under what ingestion configuration. Three requirements apply post-dissolution: (4) the dissolution record must be stored in at least one participating Self's home substrate; (5) each participating Self's governance must acknowledge receipt of the hand-off record for their home substrate; (6) any disputes about dissolution terms must be directed to the dissolution record as the authoritative reference.

For emergency dissolution specifically, D2.02's emergency dissolution variant (D2.28) relaxes the sequence and timeline of these requirements but does not eliminate them. The dissolution record requirement survives in all emergency conditions. AP-2 is present whenever the dissolution record is absent; D2.28 compliance prevents AP-2 even under emergency circumstances.

### 7.2 Remediation: discovered ungoverned dissolution

When AP-2 is discovered after the fact — typically through Criterion 2, the detection of FAI-origin content in a home substrate without a corresponding hand-off record — remediation proceeds in the following steps.

**Step 1 — Investigate FAI-origin content across participating Selves.** Governance of each participating Self audits its home substrate for content bearing FAI-origin attribution to the event in question. The audit establishes what content entered, through which evolution mechanisms, and at what time, to the extent the home substrate's own records permit reconstruction.

**Step 2 — Produce a retrospective dissolution record.** Governance produces a retrospective dissolution record documenting what is known about the event's closure and explicitly marking what cannot be reconstructed. The retrospective record does not remediate the governance gap — the at-dissolution acts did not occur and cannot be retroactively executed — but it establishes the current known state and provides a reference point for subsequent governance decisions. The retrospective record must itself be treated as a governance artifact: authored by identified human governance actors, dated, and stored in each participating Self's home substrate.

**Step 3 — Treat the gap as a process dispute under D2.45.** The ungoverned dissolution creates a process dispute: participating Selves' governance cannot agree on what was authorized at closure because no closure record exists. D2.45's process dispute framework applies. The retrospective dissolution record produced in Step 2 becomes the dispute's primary reference artifact. The investigation record documents what the dispute was, what was reconstructed, and what decisions were made under governance uncertainty.

**Step 4 — Evaluate and potentially revoke FAI-origin absorptions.** DNA absorptions that entered a participating Self's home substrate through an ungoverned dissolution lack the authorization chain that makes them legitimate under Paper 3 Claim 1 and Paper 1 A1.07. Each participating Self's governance must evaluate whether absorptions of this type should remain in the home substrate or be revoked. The evaluation considers what is known about the dissolution — including the retrospective record from Step 2 — and produces a governance decision, recorded as substrate content, for each absorption under review. Absorptions without governed dissolution provenance are structurally unauthorized; the remediation decision determines whether authorization can be retrospectively established or whether revocation is required.

**Step 5 — Review persistence policy status.** If the persistence policy cannot be located (Criterion 3), governance must determine whether Locus 2 content was retained in the host environment, lost, or released. If retained content is found without policy authorization, governance must make a retention or deletion decision and record it. If content that should have been retained is found to have been lost, the loss is documented as an irrecoverable governance gap.

### 7.3 Scope note: what remediation does not accomplish

Retrospective records do not retroactively govern the dissolution. The at-dissolution governance acts — producing the three required records at the moment of closure — cannot be performed after the fact. What remediation accomplishes is: establishing the current known state, creating a governance record of the discovery and investigation, enabling downstream governance decisions (including absorption revocation) on a documented basis, and preventing the ungoverned dissolution from propagating further governance damage through unexamined FAI-origin content. The best outcome of remediation is a documented and bounded gap. The goal of prevention, through D2.02 compliance, is that no such gap arises.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-2: Ungoverned Dissolution.* Derivation Note 578, CKS Defensive Publication Series, Phase D3. May 15, 2026. ORCID: 0009-0004-8065-3235.
