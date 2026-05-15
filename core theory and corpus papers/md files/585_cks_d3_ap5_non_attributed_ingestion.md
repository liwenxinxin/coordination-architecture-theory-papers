# AP-5: Non-Attributed Ingestion

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Non-Attributed Ingestion is the second Taxonomy Category 3 anti-pattern in the Phase D3 series. It occurs when action-layer records originating from a Full Aspect Integration (FAI) event enter a participating Self's home action layer without provenance identifying their inter-Self origin. The records are present and operative — they will inform action-feedback proposals going forward — but they carry no FAI event reference, no contributing-Self attribution, and no inter-Self origin marker. From the home substrate's perspective, they are indistinguishable from records produced by the Self's own cell operations. This note formalizes the anti-pattern across the seven-element Phase D3 structure: name and category, description, detection criteria, governance commitment violated, consequences, intra-Self analog, and resolution. Three consequences receive extended treatment because of their severity: permanent indistinguishability, proposing-substrate intelligence loss, and the impossibility of exit-relationship analysis after FAI relationship termination.

---

## 1. Anti-Pattern Name and Category

**Name:** Non-Attributed Ingestion

**Designation:** AP-5

**Taxonomy Category:** Category 3 — Evolution Feed Failures

Category 3 anti-patterns are failures in the governance of content that crosses the FAI dissolution boundary into a participating Self's home substrate. The shared substrate dissolves at the close of a FAI event; content from that dissolution propagates to each participating Self's home substrate per governance-configured ingestion at the home perimeter. Category 3 failures corrupt or contaminate this propagation — not by preventing it (that is a Category 2 failure), and not by allowing the wrong content to cross (that is a different Category 3 failure), but by allowing content to arrive without the governance metadata that makes subsequent home substrate operation auditable, differentiable, and reversible. Non-Attributed Ingestion is the Category 3 failure of provenance: the content arrives, but the record of where it came from does not.

---

## 2. Description

At FAI dissolution, action-layer content from the shared substrate enters each participating Self's home action layer under the governance-configured ingestion mechanism specified in D2.10. This ingestion is governed by three requirements: (1) home governance authorization for the ingestion, (2) FAI-origin provenance on all ingested records, and (3) an ingestion record documenting what was ingested. Non-Attributed Ingestion is the failure of Requirement 2.

The failure presents as follows. FAI-origin action-layer records arrive in the home action layer. They are correctly authorized under Requirement 1 — the home governance permitted the ingestion. An ingestion record may even exist under Requirement 3. But the individual records themselves carry no provenance identifying their inter-Self origin. No FAI event reference is attached. No contributing-Self identifier is present. No inter-Self origin marker distinguishes them from records produced by the Self's own cell operations during normal home substrate work.

The consequence of this presentation is immediate and structural: the records enter the home action layer as anonymous content. They look like home-generated records. They are indexed alongside home-generated records. They will be retrieved alongside home-generated records when the proposing substrate (D2.59) operates. Nothing about their presence in the substrate signals that they carry the epistemic signature of inter-Self learning — that they reflect another Self's operational experience, another Self's resolved conflicts, another Self's governance history — rather than the home Self's own operational accumulation.

The failure is architecturally distinct from a related failure in which FAI-origin records are simply not ingested at all. Non-Attributed Ingestion is the worse failure in one respect: the records are present and operative, but governance cannot see what they are. They contribute to home governance proposals without accountability. They compound over time as more FAI events dissolve and more unattributed records accumulate. And, as the consequences section develops, the failure may be permanently irreversible.

---

## 3. Detection Criteria

Non-Attributed Ingestion is detectable through four diagnostic patterns, applied singly or in combination.

**Temporal growth without operational explanation.** The home substrate's action layer grows around the time of FAI event dissolution without corresponding home cell operational activity that would explain the growth. If the home substrate's operational log shows low cell activity during a period in which the action layer expanded, and the expansion coincides with the dissolution of one or more FAI events, the temporal pattern is a primary indicator.

**Provenance field audit.** Action-layer records appear in the home substrate that carry incomplete or missing provenance. Paper 1 A1.07 specifies six provenance metadata fields for all substrate content. Records that fail the "who authored" and "what came before" fields — or that carry generic home-substrate author attributions that do not reflect the actual FAI-event origin — are candidates for Non-Attributed Ingestion classification.

**Post-mortem review indistinguishability.** Post-mortem review (D2.39) cannot distinguish which action-feedback proposals are informed by FAI learning versus home operational experience. If the post-mortem reviewer finds that the action layer contains records that inform proposals in ways inconsistent with the home Self's own operational history — proposing patterns the home Self has not itself encountered, referencing problem classes the home Self has not itself worked through — but those records carry no FAI attribution, the indistinguishability finding is diagnostic.

**Pre/post dissolution comparison.** Comparison of the action layer before and after FAI event dissolution shows new content without home operational record origins. This is the most direct detection method when the comparison can be made: if the delta between pre-dissolution and post-dissolution action-layer content cannot be explained by home cell operations occurring in the intervening period, and the unexplained delta coincides with dissolution, Non-Attributed Ingestion is the presumptive diagnosis.

A system with robust ingestion governance will produce a clean negative on all four criteria: action-layer growth at dissolution will be explained by FAI-origin records carrying explicit FAI attribution, and post-mortem review will be able to distinguish FAI-informed from home-operational proposals by inspecting provenance fields.

---

## 4. Governance Commitment Violated

Non-Attributed Ingestion violates two governance commitments, one primary and one secondary, with an operational reference to the three ingestion governance requirements.

**Primary violation: Paper 1 A1.07 — Path Retraceability.** Paper 1 A1.07 requires that all substrate content carry six provenance metadata fields, including fields that identify who authored the content and what content preceded it in the substrate's history. FAI-origin records in the home action layer without FAI attribution fail the "who authored" field — the real author of the content is the contributing Self operating within the FAI event, not the home Self's cells — and fail the "what came before" field — the content's immediate predecessor is the FAI event record in the shared substrate, not any home-substrate antecedent. A1.07 is a commitment about all substrate content without exception. The inter-Self scope of Paper 3 does not relax the commitment; it extends it. Records that cross the perimeter from a dissolved shared substrate are substrate content in the home substrate from the moment of ingestion. They fall under A1.07 from that moment. Non-Attributed Ingestion violates A1.07 from the moment of ingestion, without recovery unless attribution is subsequently reconstructed.

**Secondary violation: Paper 3 Claim 4 Action-Feedback Locus (D1.17).** Claim 4 specifies that action-layer content from a FAI event enters the home action layer — this is the action-feedback locus. The locus is not merely a routing commitment; it carries an accountability requirement. Content crossing into the home action layer through the action-feedback locus does so under home governance authority, and that authority requires that the crossing be legible: the home governance must be able to see what crossed and from where. Non-Attributed Ingestion completes the routing (content enters the home action layer) while defeating the accountability requirement (the crossing is not legible as FAI-origin). The locus is satisfied in form but violated in substance.

**Operational reference: D2.10 Requirement 2.** D2.10 specifies three ingestion governance requirements. Requirement 2 — FAI-origin provenance on all ingested records — is directly and completely violated by Non-Attributed Ingestion. The other two requirements (home governance authorization and an ingestion record) may be satisfied; Requirement 2 alone is the minimal site of the violation.

---

## 5. Consequences

Non-Attributed Ingestion produces five distinct consequences. Three — permanent indistinguishability, proposing-substrate intelligence loss, and exit-relationship analysis failure — receive extended treatment because of their severity or irreversibility.

### 5.1 Permanent Indistinguishability

Once FAI-origin records enter the home action layer without attribution, the default consequence is permanent indistinguishability: those records cannot be reliably separated from home-generated records by any subsequent operation on the home substrate alone.

The severity of this consequence depends on what external provenance sources remain available after the fact. If the FAI event's shared substrate was retained under a full-retention persistence policy (Paper 3 §8), it may be possible to cross-reference the home action layer's unattributed growth against the shared substrate's action-layer content and reconstruct attribution retroactively. If the contributing Self's records are available and cooperative, that source provides a second avenue of attribution reconstruction. These recovery paths are the basis for the remediation procedure in §7 below.

However, many realistic deployments do not produce these conditions. FAI persistence policy may specify minimal retention — the shared substrate dissolves and no durable record is retained beyond what each home perimeter ingested. Contributing Selves may be unwilling or unable to share their records. In these conditions, attribution reconstruction is impossible. The home action layer contains content whose inter-Self origin will never be established. Every action-feedback proposal informed by that content will be informed by inter-Self learning that the home governance cannot see, and this will remain true for as long as those records remain in the home substrate.

This is what distinguishes Non-Attributed Ingestion from most other Phase D3 anti-patterns. The majority of anti-patterns in this series have defined remediation procedures that, if executed, restore governance compliance. Non-Attributed Ingestion may not. If the external provenance sources do not exist, the remediation procedure fails and the governance gap is permanent. Governance documentation (§7) of this permanent gap is the only remaining option. This severity should calibrate the implementation priority of Requirement 2: the cost of failing to attach provenance at ingestion time can be the permanent loss of home substrate auditability for an indeterminate class of content.

### 5.2 Proposing-Substrate Intelligence Loss

D2.59 specifies the proposing substrate — the substrate-layer mechanism that generates action-feedback proposals from home action-layer content. The proposing substrate can be configured in multiple ways (D2.59 Configs A, B, and C) with respect to FAI-origin records. These configurations include generating comparative proposals that place FAI-origin experience alongside home-operational experience, flagging inter-Self-origin proposals for differential governance review, and applying FAI-origin-specific processing that leverages the fact that the record reflects another Self's perspective rather than the home Self's own.

All of these configurations presuppose that FAI-origin records are identifiable as FAI-origin at the time of proposal generation. The proposing substrate must be able to ask, for any given action-layer record: is this record FAI-origin or home-origin? Without a reliable answer to this question, the differentiated configurations cannot operate. The proposing substrate falls back to undifferentiated processing — treating all action-layer records as equivalent regardless of their actual origin.

This is not merely an audit failure. It is a live, ongoing loss of governance intelligence. The differentiated proposing-substrate configurations represent a capability that the architecture is designed to provide: the ability to leverage inter-Self learning in a governed, traceable, and auditable way that is distinguishable from home-operational learning. Non-Attributed Ingestion permanently disables this capability for the unattributed records. The home governance cannot configure differentiated proposal processing for content it cannot identify. The inter-Self learning is present in the substrate, contributing to proposals, but invisible to the governance that would otherwise govern its contribution.

The loss compounds over time. As more FAI events dissolve and more unattributed records accumulate, the proportion of the action layer that is opaque to differentiated proposal processing grows. The proposing substrate operates increasingly over a mixture it cannot decompose. This is a governance intelligence degradation that, like the indistinguishability problem, is not recoverable without external provenance sources.

### 5.3 Exit-Relationship Analysis Failure

When a Self exits a FAI relationship (D2.46), a governance question of practical significance arises: what home substrate content — particularly in the action layer — was shaped by that relationship? The answer to this question matters for at least three reasons.

First, it identifies the ongoing influence of a now-terminated relationship on home governance proposals. Even after the relationship ends, action-layer records from it continue to generate proposals. Understanding which records those are allows home governance to evaluate whether the relationship's influence is appropriate to carry forward, whether any records should be reviewed or retired, and whether the proposals generated from FAI-origin records should receive different weighting or scrutiny after relationship termination.

Second, it supports accountability documentation for the terminated relationship. A Self's governance record for a FAI relationship should include not only what was shared and received during the relationship but also what accumulated in the home substrate as a result. This is the home-side record of the relationship's impact. Without it, the governance record is incomplete.

Third, it enables clean boundary drawing for future relationships. If a Self enters a new FAI relationship after exiting a prior one, the home governance may need to know what the current action layer owes to prior inter-Self learning versus home operational experience, so that it can govern the new relationship's ingestion with accurate knowledge of the substrate's composition.

Non-Attributed Ingestion makes this exit analysis impossible. There is no marker in the home action layer identifying which records came from the terminated relationship. Post-exit, the action layer is a mixture of home-generated and FAI-origin content that cannot be decomposed by any substrate-internal operation. The governance record for the terminated relationship is permanently incomplete in this dimension. The ongoing influence of the terminated relationship on home governance proposals is present but invisible. This failure persists indefinitely: the home action layer carries the influence of terminated relationships forward, without attribution, for as long as those records remain operative.

### 5.4 Path Retraceability Break

The path retraceability failure produced by Non-Attributed Ingestion is classified as a D2.67 break type 3: FAI-origin home substrate content lacks the provenance link back to the FAI event. Unlike a break type 1 (no provenance at all) or break type 2 (provenance chain interrupted mid-sequence), a type 3 break is specifically the failure of the inter-Self provenance link — the link that would connect a home substrate record back through the dissolution boundary to the FAI event record in the shared substrate. This link is what makes inter-Self learning traceable at the home governance level. Its absence is the defining structural feature of Non-Attributed Ingestion.

### 5.5 Regulatory and Audit Incapacity

Regulatory audit (D2.63) requires the ability to establish what proportion of home governance proposals derive from inter-Self learning. This capability presupposes that inter-Self-origin records are identifiable in the home action layer. Non-Attributed Ingestion defeats this presupposition. The audit cannot establish the FAI-origin proportion because the home substrate does not contain the information needed to compute it. If regulatory requirements include documentation of inter-Self learning inputs to governance proposals, Non-Attributed Ingestion produces a compliance gap that cannot be remediated by any audit procedure operating on the home substrate alone.

---

## 6. Intra-Self Analog

Non-Attributed Ingestion at inter-Self scope is the exact inter-Self analog of unattributed action-layer content at intra-Self scope. Paper 1 A1.07 requires six provenance metadata fields on all substrate content. That requirement does not distinguish between content produced by home cell operations and content produced by inter-Self exchange. It applies to all substrate content without scope qualification. The inter-Self extension in Paper 3 does not modify A1.07; it extends the substrate to which A1.07 applies.

At intra-Self scope, the failure is an action-layer record that lacks proper provenance — no author identification, no predecessor link. This fails A1.07 at home scope. The remediation is the same structural move as at inter-Self scope: reconstruct provenance where possible, document the gap where not.

At inter-Self scope, the failure is an action-layer record that lacks FAI-origin provenance specifically. This fails A1.07 at home scope for the same structural reason: the "who authored" and "what came before" fields are wrong or absent. The added dimension at inter-Self scope is that the gap cannot always be remediated from within the home substrate — the information needed to fill the gap is held outside the home perimeter, in a dissolved shared substrate or a contributing Self's records. This makes the inter-Self version potentially more severe than the intra-Self version, where the authoring context is always held within the home perimeter and reconstruction is more often feasible.

The two scopes share the same preventive architecture: provenance must be attached at the time of content production or ingestion, not reconstructed after the fact. At intra-Self scope, this means cell operations attach provenance to records they produce. At inter-Self scope, this means ingestion mechanisms attach FAI-origin provenance to records at the moment of crossing the dissolution boundary into the home action layer. The earlier in the process provenance is attached, the lower the risk of Non-Attributed Ingestion.

---

## 7. Resolution

**Prevention.** D2.10's three ingestion governance requirements are the complete prevention of Non-Attributed Ingestion:

1. Home governance authorization for ingestion — establishes that the crossing is governed.
2. FAI-origin provenance on all ingested records — directly prevents Non-Attributed Ingestion by requiring the attribution that this anti-pattern's description identifies as absent.
3. An ingestion record documenting what was ingested — provides a secondary accountability layer and a remediation resource if Requirement 2 fails for a subset of records.

Implementation of Requirement 2 requires that the ingestion mechanism — the technical process by which records cross from the dissolving shared substrate into the home action layer — attach FAI-origin provenance at the moment of crossing. This is an architectural requirement, not a post-hoc review requirement. Provenance attached after ingestion is better than no provenance, but it introduces a window during which records are in the home action layer without attribution and during which proposals could be generated from unattributed content. The safest implementation attaches provenance as part of the ingestion operation itself, so that no record enters the home action layer without attribution.

The minimum FAI-origin provenance fields required to satisfy Requirement 2 are: (a) the FAI event identifier, (b) the contributing Self identifier, and (c) the inter-Self origin marker distinguishing the record from home-generated content. These three fields, when present on every ingested record, satisfy the "who authored" and "what came before" requirements of A1.07 at inter-Self scope and enable all downstream governance operations — differentiated proposal processing, post-mortem review, exit-relationship analysis, regulatory audit — that depend on FAI-origin identifiability.

**Remediation of discovered non-attributed ingestion.** When Non-Attributed Ingestion is discovered after the fact, the remediation procedure operates in three steps, in order of preference:

*Step 1 — Temporal analysis and candidate identification.* Identify records in the home action layer that are candidates for FAI-origin classification based on temporal analysis: records whose presence in the action layer correlates with FAI event dissolution periods and for which no home operational record provides an origin explanation.

*Step 2 — Attribution reconstruction from external sources.* If FAI event records exist — either in a retained shared substrate (Locus 2 content) or in a contributing Self's records — cross-reference the candidate records against those external sources and retroactively attach FAI-origin provenance where a match can be established. Retroactive attribution is governance-quality attribution: it should document the reconstruction method, the confidence level, and the external sources used, so that subsequent reviewers understand the provenance history of the record including the gap and its reconstruction.

*Step 3 — Gap documentation where reconstruction fails.* If attribution cannot be reconstructed — external sources do not exist, the contributing Self is unavailable, or the temporal correlation is insufficient to establish a match — document the non-attribution gap as a governance record. The documentation should specify: the time period affected, the FAI events that dissolved during that period, the estimated volume of unattributed records, and the audit implications (that proposals generated from these records have an unknown inter-Self contribution that cannot be quantified). This documentation does not remediate the A1.07 violation in a technical sense — the records still lack attribution — but it records the governance quality finding in a way that satisfies the accountability requirement to the extent possible.

Governance documentation under Step 3 should be treated as a quality finding requiring review at the home governance level. Depending on the home Self's governance configuration, findings of this severity may warrant escalation to human authority, adjustment of the proposing-substrate configuration to flag affected records, or operational procedures that reduce reliance on unattributed action-layer content for high-stakes governance proposals.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-5: Non-Attributed Ingestion.* May 15, 2026. ORCID: 0009-0004-8065-3235.
