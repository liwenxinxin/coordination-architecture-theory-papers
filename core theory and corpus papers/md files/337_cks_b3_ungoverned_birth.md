# Ungoverned Birth: The Anti-Pattern Arising When Entities Are Created Without Human Governance Authorization, Incompletely Specified, or Without Birth Records

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Birth in the Coordination Knowledge Substrate pattern is the governed lifecycle starting event: a human governance decision authorizes entity creation, a birth specification meeting the requirements established in B2.40 is completed, and a birth record anchoring the entity's lineage is created per A2.40. The Ungoverned Birth anti-pattern names the failure mode where one or more of these requirements is absent when an entity enters operational status. Three sub-forms are identified: the auto-created entity, in which entity creation occurs through automated processes without human governance authorization; the incomplete-birth entity, in which a governance decision was made but the birth specification is missing required elements; and the unrecorded birth, in which governance decision and specification exist but the birth event was not recorded. Each sub-form violates B1.09 birth as human-governed origination through a distinct mechanism, but all three produce the same structural consequence: an entity whose existence lacks the governed starting point that all downstream operations require. The note formalizes the anti-pattern, traces its three emergence pathways, identifies the operational consequences for governance integrity, specifies detection through birth verification per B2.44 and birth record audit per A2.40, and specifies remediation through retroactive governance authorization and specification completion — while noting that retroactive governance is a lesser substitute for proper governance at the moment of creation.

---

## 1. The commitment violated

Birth in CKS names the governed lifecycle starting event. The source paper (Li, April 2026) commits at §6.2 that a cell, aspect, or Self comes into existence when humans authorize its creation under their governance authority. Labor — the origination of the entity's substrate content — may be performed by humans directly, by LLMs operating under human direction, or by both under whatever orchestration rules humans have authored. What the architecture requires is that authorization be a human act performed prior to and distinct from the labor of creating the entity's specification.

B1.09 formalizes birth as human-governed origination. Its decomposition in B2.40–B2.44 specifies four requirements that every birth event must satisfy: a complete birth specification per B2.40 (including DNA-layer content, type declaration, and all required fields); a governance authorization that is distinct from and prior to entity creation per B2.41; a lineage anchor establishing the entity's position in the deployment's genealogy per B2.43; and the capacity to pass birth verification per B2.44 if run. These four requirements are not administrative overhead. They are the structural preconditions for every subsequent operation the architecture commits to. An entity that lacks any of them lacks the governed starting point that makes downstream evolution, compliance demonstration, and governance affordance exercise possible.

The Ungoverned Birth anti-pattern names the failure mode where one or more of the four requirements is absent at the moment the entity enters operational status.

---

## 2. Three recognizable forms

Ungoverned Birth appears in three sub-forms. Each violates B1.09 through a distinct mechanism. All three produce architecturally illegitimate entities — entities that exist in the deployment but whose existence lacks a proper governed anchor.

**Form 1 — Auto-created entity.** An entity is created through automated processes without a human governance decision authorizing its creation. The characteristic pattern: LLM labor generates a cell specification, and entity creation proceeds directly from that specification without a human governance act intervening. The automation may be sophisticated — the LLM may draft a complete, internally coherent specification — but the governance-vs-labor distinction per B2.41 is violated. Labor (specification drafting) has collapsed into authority (creation authorization); the governance decision was never made as a distinct human act.

Recognition signals: birth records per A2.40 lack a human authority record. The B2.41 distinction between governance and labor is absent from the creation record; there is no evidence that a human authorized the entity's existence separately from a human or LLM producing its content. The entity exists in the deployment and may operate correctly, but its creation was not authorized by a human governance act. All downstream operations on this entity rest on a governance foundation that was never established.

**Form 2 — Incomplete-birth entity.** An entity was created with a governance decision — a human authorized its existence — but the birth specification is missing required elements per B2.40. Missing DNA-layer content, a missing type declaration, or missing birth record fields are the characteristic gaps. The governance act occurred; the specification did not meet its requirements.

Recognition signals: birth verification per B2.44 would fail if run. The entity operates but level-specific inheritance verification fails for the affected fields. Composition requirements per A1.13 are not satisfied because the birth specification was incomplete. The governance decision exists in the record, but the entity was allowed to proceed to operational status before the specification was verified.

This sub-form is distinct from Form 1 in that the governance act occurred; it is distinct from a properly governed entity in that the specification requirements were not satisfied before the entity became operational. The governing commitment does not merely require a human authorization decision; it requires that the authorization proceed on the basis of a complete and verified specification. Authorizing an incomplete specification is a lesser form of Ungoverned Birth, but it is Ungoverned Birth in the specification sense: the entity did not receive the full specification to which its governed existence entitles it.

**Form 3 — Unrecorded birth.** An entity was created with both a governance decision and a complete birth specification, but the birth event was not recorded per A2.40. The lineage anchor per B2.43 is absent. The entity exists and operates; it passes birth verification on its specification content; but its origin has no record in the substrate.

Recognition signals: the entity exists in the deployment but has no birth record. B2.43 lineage establishment is absent. Path retraceability per A1.07 fails at entity scope — there is no lineage chain starting point. The compliance demonstration that later operations will require is impossible for this entity, because its origin has no substrate record from which compliance can be traced.

This sub-form is the most insidious of the three. The governance decision occurred; the specification is complete; the entity operates correctly. The missing element is the record. It may be rationalized as an administrative omission, but its architectural consequence is not administrative: without a birth record, the entity's operational history accumulates on a lineage chain that has no governed starting point, and every subsequent event in that chain is retraceable only forward from the first recorded operation, not backward to an authorized origin.

---

## 3. Emergence conditions

Three emergence conditions characterize the operational environments where Ungoverned Birth reliably appears.

**Automation shortcut.** Automated workflows create entities to fill operational gaps without triggering governance processes. The characteristic failure pattern is operational: the system needed a new cell; the LLM created one. The automation may be driven by a reasonable operational logic — a detected gap, an unhandled case, a scale requirement — but the governance process that B1.09 requires was not part of the automation's design. Automated entity creation is not inherently problematic in the CKS architecture; what is problematic is automated entity creation that does not route through a human governance act before the entity becomes operational.

**Governance process skip.** Governance processes are treated as overhead that can be deferred. Architects skip birth governance during rapid development, intending to add governance retroactively. The characteristic rationalization: the system is moving fast; governance can be added later; the entity works correctly, so the formality can follow. This rationalization is architecturally unsound not because governance documentation lacks value in its own right, but because the governance act that B1.09 requires is not a documentation act — it is an authorization act. Retroactive documentation of a decision that was never made is not the equivalent of the decision.

**Tooling failure.** Entity creation tooling does not enforce birth record creation per A2.40. The tooling may have been designed without governance enforcement; the enforcement may have been removed for convenience; the tooling may have been adopted from an adjacent system that does not share CKS commitments. Whatever the cause, the tooling allows entity creation to complete without requiring governance authorization as a precondition. When tooling does not enforce governance, governance occurs inconsistently, and its omission is invisible until audit.

---

## 4. Operational consequences

Ungoverned Birth produces four categories of operational consequence, each compounding the severity of the others.

**Governance anchor absent.** Entities without governance authorization are architecturally illegitimate in the CKS sense. Governance affordances per A2.01–A2.04 — the rights to inspect, modify, and override — cannot be meaningfully exercised on entities without governance provenance, because the substrate has no authoritative starting point for those rights. Inspecting, modifying, or overriding an auto-created entity is not governance over the entity's existence; it is governance over operational content that should not exist without a governance foundation. The right can be exercised mechanically; what it cannot do is retroactively constitute the governance that was absent at creation.

**Lineage chain broken.** Without a birth record, an entity's operational history has no retraceable starting point per A1.07. Action-feedback evolution per B1.15 accumulates operational evidence — task instances, outputs, feedback — without a governed anchor. The evidence is real; the lineage from which it descends is not governed. Any audit of the entity's evolution will trace backward through a chain of operational events and arrive not at a birth record but at the first recorded operation following an undocumented creation. That is not a lineage chain; it is an operational log with an unverified origin.

**Compliance impossible.** Entities without proper birth records cannot demonstrate Paper 1 compliance at their structural level. Level-specific inheritance verification requires a complete specification at creation; entities missing that specification cannot retroactively satisfy requirements that were to be met at birth. Audit finds entities with no governance history, no verifiable birth specification, or no lineage anchor — and any compliance claim for those entities is an assertion without a traceable basis.

**Trust contamination.** If any entity in the deployment was auto-created without governance authorization, the deployment's governance integrity is in question across all entities. Auditors cannot verify which entities were and were not properly governed without examining every entity's birth record individually. A deployment that contains even one Ungoverned Birth entity has a governance integrity gap whose full scope cannot be assessed without comprehensive audit. The contamination is not limited to the affected entity; it extends to the deployment's overall claim to governance integrity.

---

## 5. Detection

Four detection mechanisms allow Ungoverned Birth to be identified once suspected or as a precautionary audit.

**B2.44 birth verification.** Run birth verification for every entity in the deployment. Entities failing verification have Ungoverned Birth in one or more of its forms. Birth verification checks specification completeness against requirements established in B2.40; entities with missing DNA-layer content, missing type declarations, or missing required fields will fail. This mechanism detects Form 2 (incomplete-birth entities) most directly and can detect Form 1 (auto-created entities) where the auto-creation produced an incomplete specification.

**A2.40 birth record audit.** For every entity, ask: does a birth record exist in the substrate, and does that record include a human authority record? Entities with no birth record have Ungoverned Birth in Form 3 (unrecorded birth). Entities with a birth record lacking a human authority record have Ungoverned Birth in Form 1 (auto-created without governance authorization). This audit is the primary detection mechanism for Forms 1 and 3.

**B2.43 lineage anchor check.** Does every entity have a lineage starting point? An entity without a birth record has no lineage anchor per B2.43, regardless of how complete its operational history is. This check is equivalent to the birth record audit for Form 3, but framed from the lineage perspective: the question is whether path retraceability per A1.07 is satisfied at entity scope.

**B2.41 governance-labor distinction audit.** For entities with birth records, ask: was governance authorization separate from and prior to entity creation? A birth record that reflects specification creation without a distinct prior authorization act indicates that labor and governance were conflated — that the entity's specification was drafted and the entity was created without a human governance act intervening. This audit is the deepest check for Form 1, applicable when a birth record exists but its content does not distinguish governance from labor.

---

## 6. Remediation

Remediation differs by sub-form. For all three, retroactive governance is possible; for none of the three is it fully equivalent to proper governance at creation.

**For auto-created entities (Form 1).** Authorized humans must review and explicitly authorize the existence of each auto-created entity. This authorization should not be treated as a rubber stamp on existing operational entities; it is the governance act that should have occurred at creation. Following authorization, proper birth specifications per B2.40 should be authored through directed selection per the applicable mechanism. Birth records per A2.40 should be created with retroactive timestamps and explicit human governance authorization recorded, noting that the authorization is retroactive.

**For incomplete-birth entities (Form 2).** Missing specification elements should be completed through directed selection — human review and authored completion of the missing DNA-layer content, type declaration, or required fields. Birth verification per B2.44 should be run following completion to confirm the specification now satisfies requirements. The governance decision record should be updated to reflect that specification completion was reviewed and authorized.

**For unrecorded births (Form 3).** Birth records should be created retroactively. Because the governance decision and specification exist, this sub-form is the most straightforward to remediate procedurally — the record is the missing element, and it can be created from available evidence. What cannot be reconstructed is the contemporaneous governance act: a retroactive record accurately reflects what occurred, but cannot substitute for the record that should have been created at the time of the governance decision. The retroactive record should note that it is retroactive, with appropriate governance review of the decision to accept the entity's existence under retroactive documentation.

**Prevention as the preferred approach.** In all three cases, retroactive governance is a degraded substitute for the governance B1.09 requires. The governance decision at creation is what B1.09 commits to; retroactive authorization is a remediation, not an equivalent. Prevention — tooling that enforces birth record creation per A2.40, governance processes that treat birth authorization as a precondition for entity creation per B2.41, and birth verification per B2.44 as a gate before operational deployment — is the preferred approach. Where prevention failed, remediation restores the minimum viable governance posture. Where prevention is available going forward, it must be implemented before the next entity is created.

---

## 7. Conclusion

Ungoverned Birth violates B1.09 birth as human-governed origination by allowing entities to enter operational status without the governed starting point the architecture requires. The three sub-forms — auto-created entity, incomplete-birth entity, and unrecorded birth — each violate the commitment through a distinct mechanism, but all three produce the same structural consequence: an entity whose downstream operations have no legitimate governance anchor. The consequence is not limited to the affected entity. It contaminates the deployment's overall governance integrity, breaks the lineage chains on which retraceability depends, and makes compliance demonstration impossible for the affected entities.

The anti-pattern is recognizable, detectable through the birth verification and birth record audit mechanisms the architecture provides, and remediable through retroactive governance — though retroactive governance is a lesser substitute for the governance act that should have occurred at creation. Deployments committed to CKS governance integrity must treat birth authorization as a precondition for entity creation, not a documentation task to be completed after the fact.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

---

## How to cite this note

Li, W. (2026). *Ungoverned Birth: The Anti-Pattern Arising When Entities Are Created Without Human Governance Authorization, Incompletely Specified, or Without Birth Records.* May 12, 2026. ORCID: 0009-0004-8065-3235.
