# Composition Pair 9: Regulatory Audit and Documentation Standards

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Two commitments apply simultaneously whenever a Full Aspect Integration (FAI) event occurs in a regulated domain: Regulatory Audit Context Governance (D2.63), which imposes four requirements where external bodies may request audit access to governance records, and Documentation Standards (D2.36), which imposes four standards — format accessibility, attribution completeness, mutual accessibility, and retention period — on all FAI governance records. This note formalizes three non-obvious governance requirements that arise from their composition: a dual-floor architecture requiring the more demanding requirement to govern each overlapping dimension; a pre-specification obligation requiring the cross-organizational agreement to identify where regulatory requirements exceed documentation standards before events begin; and an explicit-resolution obligation when Standard 3 (mutual accessibility) conflicts with regulatory confidentiality restrictions. Each requirement is stated, its non-obviousness explained, and a three-part operational test provided.

---

## 1. Pair Identification

**Commitment A — Regulatory Audit Context Governance (D2.36)** specifies four requirements that apply when FAI governance records may be subject to review by external regulatory bodies: (1) retention minimums meeting applicable regulatory schedules, (2) record completeness sufficient to support a third-party audit without supplementation, (3) format accessibility for regulatory reviewers who may not be members of any participating organization, and (4) chain-of-custody documentation demonstrating that records have not been modified after the FAI event they document.

**Commitment B — Documentation Standards (D2.36)** specifies four standards that apply to all FAI governance records regardless of domain: (1) format accessibility for non-specialist readers, (2) attribution completeness covering the full provenance of each governance record, (3) mutual accessibility ensuring all participating Selves can read all governance records, and (4) a specified retention period that survives any individual organization's record-management policies.

Both commitments are live simultaneously for any FAI event occurring in a regulated domain — healthcare, finance, critical infrastructure, or any domain where an external body holds statutory authority to examine coordination records.

---

## 2. The Governance Scenario

An FAI event occurs among organizations operating in a regulated domain. The event produces governance records: the shared substrate content documenting the FAI exchange, any conflicts preserved for resolution, and the disposition of those conflicts. These records must satisfy D2.36's four documentation standards because they are FAI governance records — the universal floor applies. They must also satisfy D2.63's four regulatory audit requirements because the domain makes external audit access a live possibility.

The governance team does not face a choice between the two commitments. Both apply. The question the composition pair forces is not which commitment to prioritize but how to satisfy both simultaneously and, where they overlap on a dimension, which requirement to meet when they diverge.

This scenario is not exotic. Regulated domains are the primary deployment context for consequential inter-organizational coordination. Healthcare interoperability, financial services clearance, and supply-chain compliance all routinely require organizations to coordinate while operating under statutory governance obligations. Any architecture for inter-Self coordination in these domains must account for the composition, and the consequences of failing to do so become visible at audit time — typically the worst possible moment.

---

## 3. Non-Obvious Governance Requirements

### Requirement 1 — Dual Floor: Meet the Higher of the Two Requirements on Each Dimension

The first non-obvious requirement is structural. Documentation standards are a universal floor: they apply to every FAI event in every domain. Regulatory audit requirements are a domain-specific overlay: they apply only in regulated domains, but when they apply, they may exceed the universal floor on specific dimensions.

The composition does not produce a simple additive requirement — "satisfy both lists." It produces a **dual floor** in which, on every dimension where the two commitments overlap, the more demanding requirement governs. Three overlapping dimensions require explicit comparison:

**Retention.** Documentation Standard 4 requires that a retention period be specified. Regulatory Requirement 1 specifies retention minimums keyed to applicable regulatory schedules. The more demanding minimum governs. If the regulatory schedule requires seven years and the cross-organizational agreement specified three, the agreement's specification is insufficient — the regulatory floor supersedes it. The governance team must identify the applicable regulatory minimum and confirm that the documentation-standard retention period meets or exceeds it.

**Format.** Documentation Standard 1 requires format accessibility for non-specialists. Regulatory Requirement 3 requires format accessibility for regulatory reviewers, who may have specific format expectations — particular file types, structured metadata fields, or presentation conventions that differ from what general non-specialist accessibility requires. Both requirements apply. Where regulatory reviewer accessibility imposes additional format specifications beyond general non-specialist accessibility, those additional specifications govern. Meeting only the documentation standard floor on format is insufficient if regulatory format requirements are more demanding.

**Attribution.** Documentation Standard 2 requires complete provenance — a record of who produced which governance content and when. Regulatory Requirement 4 requires chain-of-custody documentation demonstrating non-modification after the event. Chain of custody is an additional attribution requirement that Standard 2 alone does not supply: provenance records the origin of content; chain of custody demonstrates the content has not changed since that origin. An attribution record meeting Standard 2 but not Regulatory Requirement 4 satisfies the universal floor but fails the regulatory overlay.

The dual-floor architecture is non-obvious because practitioners who are familiar with documentation standards and with regulatory requirements may treat them as separate checklists to complete independently. The composition pair establishes that they are not independent where they overlap on a dimension: the higher floor governs, and governance must explicitly compare the two on each overlapping dimension rather than verifying each list in isolation.

### Requirement 2 — Pre-Specification: The Cross-Organizational Agreement Must Identify Where Regulatory Exceeds Documentation Before Events Begin

The second non-obvious requirement is temporal. The cross-organizational agreement — the governance document that specifies how participating organizations will conduct FAI events and what obligations they accept — must explicitly identify the dimensions on which regulatory requirements exceed documentation standards. This identification must be present in the agreement before any FAI event in the domain begins.

The non-obviousness is that practitioners may not know in advance which dimensions are affected. The regulatory audit requirements for healthcare differ from those for financial services; the specific retention schedules, format conventions, and chain-of-custody specifications vary by jurisdiction and regulatory body. Without a systematic comparison embedded in the agreement, governance practitioners may not discover that the universal floor is insufficient on a given dimension until an audit request arrives.

Discovering this gap at audit time is the regulatory version of a general anti-pattern: governance gaps are cheapest to close at agreement drafting time, when the participating organizations can consult regulatory counsel, align their record-keeping systems, and specify compliant procedures before any event takes place. At audit time, the gap is expensive in two senses: remediation may require reconstructing records that no longer exist in compliant form, and the gap itself may constitute a regulatory violation independent of the underlying coordination records.

The pre-specification obligation means the agreement must contain a section — or a referenced annex — that maps each applicable regulatory requirement to the documentation standard it affects, identifies whether it exceeds the documentation floor on that dimension, and specifies which requirement the governance procedures will implement. Practitioners cannot defer this comparison to post-event verification.

### Requirement 3 — Standard 3 / Regulatory Confidentiality: Explicit Resolution Required

The third non-obvious requirement addresses a genuine conflict between two requirements that apply simultaneously. Documentation Standard 3 requires that governance records be mutually accessible to all participating Selves: every organization that participated in an FAI event must be able to read the governance records that document it. This mutual accessibility requirement is the inter-organizational analog of the within-organization transparency that substrate-based governance depends on.

Some regulated domains impose confidentiality requirements that restrict who may access certain categories of governance records. A healthcare regulator may restrict access to records containing patient identifiers to designated roles within each organization. A financial regulator may restrict access to records touching on non-public trading information. These restrictions are not optional: they are statutory obligations that cannot be waived by cross-organizational agreement.

When a regulatory confidentiality requirement restricts access to a governance record that Standard 3 requires to be mutually accessible to all participating Selves, the two requirements conflict. Neither can be silently sacrificed. Silencing Standard 3 — restricting mutual accessibility without acknowledgment — violates the dual-floor requirement by treating a documentation standard as optional. Silencing the regulatory confidentiality requirement — providing unrestricted access to records the regulation restricts — violates the regulatory audit requirement and may constitute a regulatory violation in its own right.

The composition pair requires that this conflict be **explicitly resolved** in the cross-organizational agreement. The resolution cannot be implicit, informal, or deferred to case-by-case judgment when a specific record is created. One defensible resolution form is **scoped access**: governance records subject to regulatory confidentiality are accessible to all participating Selves in the sense that each Self has a designated role or designated personnel with access, but access within each Self is restricted to those designated roles. This preserves the inter-organizational dimension of Standard 3 — every participating Self can access the records — while satisfying the intra-organizational restriction the regulatory requirement imposes.

The authored resolution must appear in the cross-organizational agreement and must identify which categories of governance records are subject to regulatory confidentiality, what access scope applies to each category, and how the scoped-access specification satisfies both Standard 3 and the applicable regulatory requirement. A resolution that is not authored and not present in the agreement does not satisfy either requirement.

---

## 4. Prior-Art Significance

The three governance requirements above define what "governed AI coordination meeting regulatory compliance standards" architecturally requires, at the level of specificity needed to distinguish compliant implementations from implementations that satisfy each commitment in isolation but fail the composition.

The first prior-art claim is the **dual-floor architecture** itself: the principle that where a universal documentation standard and a domain-specific regulatory requirement overlap on a dimension, the more demanding requirement governs, and governance must explicitly compare the two floors rather than verifying each independently. This comparison is an architectural obligation, not a deployment judgment.

The second prior-art claim is the **pre-specification requirement**: that the cross-organizational agreement must contain the floor-comparison analysis before FAI events in the regulated domain begin. A governance architecture in which this comparison is deferred to post-event or audit-time verification does not satisfy the composition pair's requirements, regardless of whether the comparison is eventually performed.

The third prior-art claim is the **scoped-access resolution form** for Standard 3 / regulatory confidentiality conflicts: inter-organizational accessibility satisfied at the Self level, with intra-organizational access restricted to designated roles within each Self, as the canonical resolution for this class of conflict. A governance architecture that relies on implicit case-by-case judgment rather than an authored scoped-access specification does not satisfy the explicit-resolution requirement.

These claims are precise enough to distinguish compliant governance from non-compliant governance in operational deployments, making them suitable prior-art anchors against subsequent attempts to claim novelty for each element individually or for their combination.

---

## 5. Operational Test

For a FAI event that has occurred in a regulated domain, an independent observer can apply the following three-part test to determine whether the composition pair is satisfied:

**(a) Agreement pre-specification.** Does the cross-organizational agreement — in force before the FAI event took place — contain an explicit identification of the dimensions on which the applicable regulatory requirements exceed the four documentation standards? Specifically: does it identify the applicable regulatory retention minimum and confirm it exceeds or equals the documentation-standard retention period? Does it identify any regulatory format specifications that exceed general non-specialist accessibility and specify that those specifications govern? Does it identify the chain-of-custody requirement and specify how it is satisfied as an additional attribution requirement beyond Standard 2?

**(b) Higher-floor satisfaction.** For the FAI event's governance records, does each record satisfy the higher of the two applicable floors on each overlapping dimension? Is the retention period consistent with the regulatory minimum rather than only the documentation-standard specification? Is the format consistent with regulatory reviewer accessibility requirements where those exceed non-specialist accessibility? Does the attribution record include chain-of-custody documentation in addition to provenance?

**(c) Explicit Standard 3 / confidentiality resolution.** If any governance records are subject to regulatory confidentiality restrictions, does the cross-organizational agreement contain an explicit scoped-access specification for that category of record? Does the specification identify which participating Selves have designated access, identify the roles within each Self to whom access is restricted, and state how the specification satisfies both Standard 3 and the applicable regulatory requirement?

A governance implementation that passes all three parts of this test satisfies the composition pair's requirements. A governance implementation that passes each commitment's checklist independently — satisfying D2.36's four standards and D2.63's four requirements as separate lists without applying the dual-floor architecture, the pre-specification obligation, or the explicit-resolution requirement — does not satisfy the composition pair, because it has treated the commitments as independent when they are not.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Composition Pair 9: Regulatory Audit and Documentation Standards.* May 15, 2026. ORCID: 0009-0004-8065-3235.
