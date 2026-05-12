# Provenance Void — The Cross-Cutting Anti-Pattern Where Systematic Absence of A2.40 Provenance Records Makes the Deployment's Operational and Governance History Unretraceable, Violating A1.07 Retraceability and Undermining All Lifecycle, Evolution, and Governance Commitments That Depend on Record Integrity

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026).

## Abstract

Provenance Void is the cross-cutting anti-pattern in which systematic absence of A2.40 provenance records makes a deployment's complete operational and governance history unretraceable. Unlike individual missing records — a single unrecorded birth, a single missing governance decision — Provenance Void is the absence of provenance infrastructure itself: the deployment was never designed to create comprehensive records, or the infrastructure has failed across multiple event categories simultaneously. The anti-pattern manifests in three sub-forms: systematic record absence (no provenance infrastructure was ever established), record degradation (infrastructure existed but records have been lost over time), and selective recording (certain event categories are consistently omitted while others are recorded). Provenance Void violates A1.07 path retraceability, A2.40's six provenance metadata fields, A1.08 substrate-as-source-of-truth, A5.08 provenance-completeness, and every B1.xx lifecycle, evolution, and governance commitment that depends on event records existing. Its emergence conditions include treating provenance as storage overhead, confusing operational logs with A2.40-compliant provenance, and deferring governance record infrastructure as a "future enhancement." Operational consequences span the full governance stack: lifecycle audits cannot run, evolution audits cannot run, action-feedback pathway integrity cannot be verified, compliance demonstration is impossible, and the claim that the deployment is governed per A1.01 cannot be substantiated. Detection runs through comprehensive A5.08 provenance-completeness testing across all event categories and A5.09 four accountability questions applied systematically. Remediation faces a fundamental ceiling: records that were never created cannot be accurately recreated retroactively. Prevention and infrastructure establishment from deployment initialization are the only complete remediation.

---

## 1. Anti-pattern name and cross-cutting character

**Pattern name:** Provenance Void

**Cross-cutting character.** Most B3.xx anti-patterns are localized to a specific commitment or lifecycle stage: cell birth without governance (B3.14) violates the birth commitment; death without archival (B3.18) violates the archival commitment. Provenance Void is not localized. It cuts across every commitment in the architecture that depends on event records existing, which is nearly every operational and governance commitment Paper 2 establishes. A deployment that has no provenance infrastructure does not merely fail one verification; it fails all of them simultaneously. This cross-cutting character is what distinguishes Provenance Void from individual missing records and what makes it worth treating as a named anti-pattern in its own right.

---

## 2. Commitments violated

Provenance Void violates the following commitments:

**A1.07 (path retraceability).** Path retraceability is a structural property of substrate content: any piece of content must be traceable back through its antecedents by reading substrate content alone. Without provenance records carrying the six A2.40 fields — writer attribution, timestamp, antecedent reference, rule reference, rationale, and contradiction relationships — the path runs through information the substrate does not carry. Retraceability does not degrade gracefully; it fails entirely wherever records are absent.

**A2.40 (six provenance metadata fields).** A2.40 specifies the six fields that every governance event record must carry. Provenance Void is the systematic failure to satisfy this commitment: the fields are not present because the records do not exist.

**A1.08 (substrate as source of truth).** Provenance records are substrate content. A deployment whose substrate carries no governance history cannot function as the authoritative record of the deployment's operational state. The substrate, absent its provenance records, is structurally incomplete.

**A5.08 (provenance-completeness test).** A5.08 is the operational test that verifies provenance infrastructure is present and complete across all event categories. Provenance Void produces comprehensive, systematic failures of this test rather than isolated gaps.

**B1.xx lifecycle and governance commitments (collectively).** Every lifecycle commitment that requires events to be recorded — governed birth origination (B1.06), mating with provenance (B1.07), death with archival (B1.08), evolution mechanism governance (B1.09–B1.12), multi-shaped human governance across evolution mechanisms (B1.15) — depends on records existing at the time of the event. Without provenance infrastructure, these commitments cannot be verified after the fact.

---

## 3. Recognizable form

Provenance Void manifests in three sub-forms, each with distinct recognition signals.

### Form 1 — Systematic record absence

The most complete sub-form: provenance infrastructure per A2.40 was never established. No lifecycle events — births, matings, deaths — are recorded. No evolution events — DNA modifications, mutation integrations, action-feedback approvals — are recorded. No governance events — overrides, authority decisions, verification outcomes — are recorded. The deployment may have been in operation for months or years; the substrate carries its current state but no history of how it reached that state.

Recognition signals for Form 1 are comprehensive. The A5.08 provenance-completeness test fails across every event category without exception. Lineage chains per B2.43 are entirely absent: no entity in the deployment has a birth record, so no chain can begin. Compliance auditors find no governance history to review. The A5.09 four accountability questions — who authorized this, what rule governed it, what was the antecedent, when did it occur — cannot be answered for any event in the deployment's history.

### Form 2 — Record degradation

Infrastructure existed at deployment initialization but records have been degraded over time. Old records were deleted to save storage. Records were overwritten without versioning when entities were updated. Records were corrupted through migration or platform changes. The deployment's history is retraceable for some periods and void for others.

Recognition signals for Form 2 are temporal. Older entities have some records, but recent events are unrecorded; or recent records exist, but the deployment's early history was purged. The A5.08 test produces partial results: it passes for some time windows and fails for others. Lineage chains per B2.43 have gaps — an entity's record sequence has breaks where events occurred but were not preserved or were subsequently lost. The governance claim "this deployment has been governed throughout its operation" cannot be substantiated because the record of portions of that operation no longer exists.

### Form 3 — Selective recording

Provenance records are created only for certain event categories while others are systematically omitted. Governance decisions are recorded but operational events are not, so the authorizations exist but the events they authorized have no record. Or operational events are recorded but governance authorizations are not, so actions are traced but authority cannot be established. Or action-feedback proposals per the action-feedback evolution pathway are recorded but Stage 2 approval events are not, making pathway integrity verification impossible.

Recognition signals for Form 3 are categorical. The A5.08 test passes for some event categories but fails for others in a consistent, reproducible pattern — not random gaps but systematic omissions. The A5.09 four accountability questions can be answered for some event types but not others. This sub-form is often produced by deliberate design decisions: the system was built to record what implementers thought mattered, without recognizing that A2.40 requires comprehensive coverage across all governance event categories.

---

## 4. What distinguishes Provenance Void from individual missing records

Individual missing records — an unrecorded birth in B3.14's territory, a single missing governance authorization — are gaps in an otherwise functional provenance infrastructure. The substrate has a record-creation architecture; particular events were missed within it. Remediation is targeted: identify the missing events, create records for those that can be reconstructed, document the gap for those that cannot.

Provenance Void is categorically different. The absence is not a gap in infrastructure; it is the absence of infrastructure. The deployment was never designed to create comprehensive provenance records, or the infrastructure has failed systematically. The A5.08 test does not identify isolated missing records; it reveals that the record-creation architecture itself is absent or broken. This distinction matters for both detection and remediation: individual missing records call for gap-filling; Provenance Void calls for infrastructure establishment.

---

## 5. Emergence conditions

Three conditions, alone or in combination, produce Provenance Void in practice.

**Storage cost concern.** Provenance records are treated as storage overhead rather than as substrate content. The decision to not create them — or to delete them after some retention period — is framed as a storage optimization. What this framing misses is that provenance records are not optional logging; they are the substrate's governance history, and A1.08 makes the substrate the authoritative record of the deployment's state. Deleting provenance records to save storage is architecturally equivalent to deleting substrate content to save storage: it destroys the source of truth the architecture depends on.

**Observability misunderstanding.** Provenance is confused with application logging. The deployment has operational logs — events, errors, timing information — and those logs satisfy operational observability requirements. The implicit conclusion is that provenance requirements are also satisfied. They are not. Application logs record what happened in a form useful for debugging and performance monitoring. A2.40's six provenance fields require writer attribution, timestamp, antecedent reference, rule reference, rationale, and contradiction relationships in a form that supports governance reconstruction. An application log that records "cell execution completed at 14:32:07" does not record which human authorized the orchestration rule under which the cell executed, what substrate content the cell read as input, or what the rationale for the rule's specific configuration was. The two record types are not interchangeable, and deployments that have only the first kind are in a state of Provenance Void with respect to governance history regardless of how comprehensive their operational logs are.

**Governance architecture incomplete.** Provenance record creation was not built into the deployment's operational architecture. It was treated as a "future enhancement" during initial deployment — something to add later, once core functionality was working. In practice, the enhancement is never added: the deployment is operating, it appears to be working, and the cost and disruption of retrofitting a record-creation architecture across all event categories is high. Provenance Void becomes the deployment's permanent state.

---

## 6. Operational consequences

The consequences of Provenance Void span the full architecture of Paper 2's governance commitments.

**Retraceability failure.** A1.07 path retraceability cannot function without provenance records. The substrate carries its current state but not the path that produced it. Any piece of current substrate content that was produced by a governed process cannot be traced back to the authority under which it was created. Compliance demonstration at any level — to internal governance bodies, to external auditors, to regulators — is impossible.

**Lifecycle audit impossible.** The lifecycle verification commitments — governing birth origination, mating provenance, and death archival — require that the events they verify are recorded. Without records, verification cannot run. An auditor cannot confirm that a cell was born under governed origination, that its parents were correctly recorded at mating, or that its retirement followed the appropriate death-type governance process, because no records of those events exist to verify against.

**Evolution audit impossible.** The evolution governance commitments — verification substrates governing instinct integration, authority architecture governing DNA evolution, human-mediated approval governing action-feedback cycles — produce governance events that must be recorded to be auditable. Without records of which DNA modifications were authorized under which governance process, the claim that DNA evolution is governed by human authority cannot be substantiated. Without records of which instinct integration proposals were reviewed through which verification substrates, the claim that instinct evolution is governed cannot be substantiated. The governance happened, or it did not; without records, the two cases are indistinguishable.

**Action-feedback pathway broken.** The action-feedback evolution pathway depends on complete provenance at every step: action patterns recorded in the action layer, proposals generated and recorded, Stage 2 approval recorded, DNA modification made and recorded. Without provenance at each step, pathway integrity verification per the action-feedback governance commitments fails. The pathway may have been followed; without records, the pathway's integrity cannot be confirmed.

**Compliance impossible.** Any compliance regime that requires governance history finds nothing to audit. The deployment cannot demonstrate that governance occurred, that authority was followed, or that the commitments the architecture makes were honored. This consequence is distinct from governance not having occurred: a deployment may have been carefully governed throughout its operation, with every decision taken under proper authority. Provenance Void means the evidence of that governance is absent, making the governance indistinguishable from its absence.

**Governance integrity claim invalid.** The foundational claim that a deployment is governed per A1.01's authority-not-labor definition requires that governance events are recorded. Without records showing that humans exercised inspect, modify, and override rights at the appropriate moments — and that those exercises are preserved as substrate content — the claim cannot be substantiated. Provenance Void is not merely a documentation failure; it is an architecturally significant condition that makes the deployment's governance claim unverifiable.

---

## 7. Detection

Two detection mechanisms are primary.

**A5.08 provenance-completeness test, applied comprehensively.** The key word is "comprehensively." A5.08 run against a sample of recent events, or run against only the event categories an implementer believes are recorded, will not detect Provenance Void reliably. The test must be run across all event categories — lifecycle events (births, matings, deaths at every level), evolution events (instinct integration records, DNA modification authorization records, action-feedback approval records), and governance events (override records, authority decisions, verification outcomes). Systematic failures across multiple categories, or complete failures within any category, indicate Provenance Void rather than individual missing records.

**A5.09 four accountability questions, applied by event type.** The four accountability questions — who authorized this event, under what rule, on the basis of what antecedent substrate content, and when — should be applied not only to individual events but across event types. If the questions can be answered for governance events but not for operational events, or vice versa, the pattern points to Form 3 selective recording. If the questions cannot be answered for any event type, the pattern points to Form 1 systematic record absence. If the questions can be answered for events in one time period but not another, the pattern points to Form 2 record degradation.

**Lineage chain completeness per B2.43.** Every entity in the deployment should have a birth record and a subsequent chain of event records covering the entity's operational history. Absence of birth records across entities — not isolated missing records but systematic absence — confirms Form 1. Chains with temporal breaks confirm Form 2.

---

## 8. Remediation

Remediation must acknowledge a fundamental ceiling.

**Infrastructure establishment.** For a deployment in Form 1 systematic record absence or Form 3 selective recording, the primary remediation is to establish provenance record creation infrastructure per A2.40 through directed selection per DNA evolution governance. This means building record creation requirements into the deployment's operational workflows — not as an optional logging step but as a required substrate write — for every event category A2.40 covers. The infrastructure must be governed under the same authority architecture that governs other substrate modifications.

**Retroactive reconstruction.** For events that can be reconstructed from other sources — application logs, external system records, human recollection — provenance records should be created retroactively, with their current-date creation explicitly noted in their own provenance fields. A retroactively created record is better than no record, provided its retroactive origin is itself recorded.

**Gap documentation.** For events that cannot be reconstructed, records should be created documenting the provenance gap with current-date acknowledgment: the event category, the time period, the reason records do not exist, and the date the gap was identified and documented. Gap documentation does not recreate the missing history, but it makes the gap itself part of the substrate's governance record.

**The partial-remediation ceiling.** Provenance Void cannot be fully remediated retroactively. Records that were never created cannot be recreated accurately. Retroactive records carry inherent uncertainty about whether they accurately reflect what occurred. Gap documentation acknowledges absence without filling it. The deployment will carry the governance record deficit of its Provenance Void period permanently — the history before infrastructure establishment will remain less traceable than the history after it.

This ceiling is why prevention is the only complete remediation. Provenance infrastructure must be established at deployment initialization, built into the operational workflows before any governance events occur that need to be recorded. Every day a deployment operates without provenance infrastructure is a day of governance history that cannot be fully recovered.

---

## 9. Why the anti-pattern recurs

Provenance Void recurs because its cost is invisible until a governance event requires history that does not exist. A deployment without provenance infrastructure operates normally in day-to-day use: cells execute, DNA evolves, lifecycle events occur. The absence of records does not disrupt operations. The cost materializes at compliance review, at audit, at the moment a governance decision requires justification, or at the moment a failure requires investigation. At that moment, the deployment is in a state where the cost of Provenance Void — inability to demonstrate governance, inability to trace decisions, inability to verify lifecycle and evolution compliance — is fully realized and cannot be remediated without accepting the partial-remediation ceiling.

Naming Provenance Void as a cross-cutting anti-pattern makes the cost legible before it materializes. The three sub-forms, the three emergence conditions, and the detection mechanisms together give deployment designers and operators a vocabulary for identifying when their deployment is at risk of entering or already occupying the anti-pattern, before the governance event that makes the void consequential.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Provenance Void — The Cross-Cutting Anti-Pattern Where Systematic Absence of A2.40 Provenance Records Makes the Deployment's Operational and Governance History Unretraceable.* May 12, 2026. ORCID: 0009-0004-8065-3235.
