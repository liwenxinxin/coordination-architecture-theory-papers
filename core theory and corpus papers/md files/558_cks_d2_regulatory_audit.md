# FAI Governance for Regulatory Audit Contexts

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note is D2.63 in the Phase D2 derivation series. It derives from D2.36 (documentation standards for FAI governance records) and D2.34 (cross-organizational governance agreements), extending both to regulated-domain contexts where external regulatory bodies may request audit access to FAI governance records. The note distinguishes internal audit — participating Selves reviewing their own records using the inspect right — from regulatory audit, in which a legally empowered external body requests access to governance records produced during FAI events. It then establishes the key architectural observation that undergirds the entire note: the architecture produces audit-grade records by design, without a special regulatory mode. The FAI governance record, documentation standards, and path retraceability together already produce what a regulator requires. D2.63 formalizes four requirements that translate this architectural readiness into concrete governance specifications for regulated-domain deployments: a regulatory retention policy, regulatory audit access provision, record format for regulatory use, and chain of custody for audit records. It then names the anti-pattern — regulatory audit surprise — and states the operational test.

---

## 1. Position in the derivation sequence

D2.63 is the sixty-third Phase D2 note and occupies position #558 in the continuous derivation series. Its immediate parents are D2.36, which established documentation standards for FAI governance records, and D2.34, which established the cross-organizational governance agreement as the architectural mechanism through which participating Selves formalize their joint governance commitments before FAI events begin.

D2.63 does not introduce new architecture. It applies the governance framework that D2.36 and D2.34 already establish to a specific operational context: FAI events occurring in regulated domains where external regulatory bodies carry legal authority to request audit access to governance records. The application produces four requirements that participating Selves should address in their cross-organizational agreement and FAI configuration before events begin.

---

## 2. Internal audit versus regulatory audit

Two distinct audit relationships touch FAI governance records, and conflating them produces misspecification.

**Internal audit** is the governance function through which participating Selves review their own FAI records. It is exercised through the inspect right (D2.04), which is available to any authorized participant at any time. Internal audit is normal governance operation: a Self's governance actors reading the FAI governance record, verifying that documentation standards were met, checking conflict provenance, confirming that the Locus 2 durable record is complete. No special arrangement is required beyond the access rights the architecture already provides.

**Regulatory audit** is something different. A regulatory body with legal authority — a financial regulator, a healthcare oversight body, a data protection authority, or any other jurisdiction-specific body — requests access to FAI governance records as part of its oversight function. The regulatory body is external to the architecture. It does not hold the inspect right in the architectural sense; its access authority derives from law, not from the governance configuration of the FAI event. The architecture must be able to support this access, but the access mechanism must be arranged outside the substrate itself — in the cross-organizational agreement and in whatever access arrangements that agreement specifies with the regulatory body.

The distinction matters for two reasons. First, the response to internal audit is already specified by the architecture: governance actors use the inspect right. No additional design is required. Second, the response to regulatory audit requires anticipatory governance work: specifying in the cross-organizational agreement how access will be provided, in what format, with what retention period, and under what chain-of-custody assurances — before any events begin. D2.63 formalizes that anticipatory work as four requirements.

---

## 3. The architecture produces audit-grade records by design

The central observation that organizes D2.63 is this: the architecture does not need a special regulatory mode. It produces audit-grade records through its standard documentation requirements.

The FAI governance record (D2.18) captures the full lifecycle of a FAI event: which Selves participated, what aspects each contributed, what conflicts arose, how conflicts were handled, what decisions were made, and what persisted at dissolution. The documentation standards (D2.36) specify that this record must be non-specialist accessible — written so that someone without deep familiarity with the architecture can understand what it contains. The path retraceability commitment (Paper 1, A1.07) ensures that any action in the governance record can be traced back through its contributing inputs. The immutable version history (D2.38) ensures that the record at any point in time is recoverable. The provenance chain (D2.03) connects every governance action to its author and authority source.

These are not regulatory requirements. They are architectural requirements that the governance record satisfies for reasons intrinsic to the CKS pattern. Regulatory audit readiness is a consequence of this architecture, not a supplement to it.

This observation is important because it sets the correct framing for D2.63. The four requirements that follow are not additions to the architecture. They are governance specifications — content that should appear in the cross-organizational agreement and the FAI configuration — that translate the architecture's inherent audit-grade record production into explicit commitments that satisfy regulatory requirements in a specific domain. The architecture provides the capability; the governance specifications direct that capability toward regulatory compliance.

---

## 4. Four requirements for regulated-domain FAI governance

### Requirement 1 — Regulatory retention policy

The persistence policy (D1.04) governs what remains after an FAI event dissolves, where it persists, and for how long. This is governance content (D1.22 Dimension 3), meaning governance sets it. For unregulated domains, governance may set the retention period according to operational judgment. For regulated domains, governance must set the retention period to satisfy regulatory minimums — the periods specified by the applicable regulatory framework for records of the type the FAI event produces.

The practical specification: the cross-organizational agreement (D2.34, Component 1, mutual governance standards) should name the regulatory retention period applicable to the domain and specify that the persistence policy for FAI events in that domain meets or exceeds that period. This ensures that the records a regulator may request are available when requested, regardless of when the request arrives relative to the event.

Retention period specification in the cross-organizational agreement before events begin is the correct moment for this decision. Specifying it retroactively — after a regulatory audit request arrives — may be too late if records have already been purged under a shorter default retention period.

### Requirement 2 — Regulatory audit access provision

The cross-organizational agreement must specify how a regulatory body is granted access to FAI governance records when it exercises its legal authority to request them. Two structural approaches are available:

**Direct access.** Each participating Self provides its own governance records to the regulatory body under the regulator's legal authority. The regulatory body reviews each Self's records separately. This approach preserves each Self's governance independence: each Self manages its own records production and regulatory relationship. It is straightforward where the regulatory body's authority runs against each Self individually and where the regulatory relationship between each Self and the regulator is already established.

**Joint access provision.** The participating Selves jointly provide the shared-substrate governance records to the regulatory body through a jointly authorized access arrangement — for example, a designated contact or a jointly authorized production mechanism specified in the cross-organizational agreement. This approach is appropriate where the regulatory body's inquiry runs to the shared-substrate event as a unit, where the records of interest are the shared records rather than each Self's home records, or where the regulatory body's authority spans the joint activity rather than each Self individually.

The cross-organizational agreement should specify which approach applies, the contact or mechanism through which access is provided, and the triggering conditions (for example, receipt of a legally authorized audit request). Leaving this unspecified means that when a regulatory body makes a request, the participating Selves must negotiate both the substantive and procedural response under time pressure, with governance mechanisms that were not designed for that scenario.

### Requirement 3 — Record format for regulatory use

Documentation standards (D2.36, Standard 1) require non-specialist accessibility: governance records must be interpretable by humans who are not specialists in the CKS architecture. For regulatory audit, non-specialist accessibility has a specific instantiation: the records must be interpretable by regulatory reviewers who are familiar with the regulatory framework applicable to the domain but who may have no familiarity with the CKS pattern, FAI events, the shared substrate, or the governance mechanisms that produced the records.

This does not require a separate record format. It requires that the Locus 2 durable record produced under D2.36 be designed with regulatory reviewers in mind. Specifically:

- The governance record's structure should be documented: what each section records, what abbreviations or terms mean, how the record maps to the sequence of events in the FAI lifecycle.
- Governance decisions should be explained in plain terms sufficient for a reviewer who understands the regulatory domain but not the architecture.
- Cross-references within the record should be navigable: a reviewer should be able to move from a conflict record to its resolution to its provenance without specialized tools.

The governance instrument for this requirement is the Locus 2 durable record, which the FAI configuration and cross-organizational agreement specify. The cross-organizational agreement should include guidance or a template for how Locus 2 records are prepared when the domain is regulated.

### Requirement 4 — Chain of custody for audit records

When governance records are produced for regulatory review, the regulatory body must be able to verify that the records are authentic — that they represent the actual governance record of the FAI event and have not been modified after the event. This is the chain-of-custody requirement.

The architecture provides the chain of custody through two mechanisms:

The **immutable version history** (D2.38) records every state of the governance record from initial creation forward, with timestamps and author attribution. A reviewer can verify that the record produced for regulatory review matches the record at any prior point in the version history, establishing that no post-hoc modification has occurred.

The **provenance chain** (D2.03) links every governance action to its author, its authority source, and the substrate state it operated on. The provenance chain establishes not only what the record says but how it came to say it, tracing each entry back to the governance actions that produced it.

For regulatory audit purposes, the cross-organizational agreement should specify how these mechanisms are presented to the regulatory body — for example, by producing the version history alongside the current record, or by providing the provenance chain in a format that regulatory tools can process. The goal is to give the regulatory body the evidence it needs to verify authenticity without requiring specialized access to the substrate.

---

## 5. Regulatory audit as governance quality signal

The ability to produce audit-grade FAI governance records for regulatory review — records that satisfy all four requirements — is a governance quality indicator. It signals that:

- The participating Selves' governance is disciplined enough to specify regulatory requirements in advance, before events begin.
- The FAI configuration produces records that meet the documentation standards required for external review.
- The cross-organizational agreement anticipates scenarios beyond the Selves' own governance needs.
- The governance infrastructure can support the access, format, and chain-of-custody demands of external legal review.

Organizations that pass regulatory FAI audits demonstrate governance quality at a level that general governance trust calibration (D2.29) may not capture. Internal governance review and partner audits can verify that documentation standards are met; regulatory audit verifies that those standards satisfy an externally imposed legal threshold. Successfully passing a regulatory FAI audit is a credentialing event: it constitutes evidence of governance quality that did not exist before the audit was conducted. This evidence is relevant to governance trust calibration with future partners in the same or similar regulated domains.

The governance quality signal is also prospective: an organization that has configured its FAI governance to anticipate regulatory audit requirements — even before any audit occurs — demonstrates governance discipline that informs partnership decisions. The cross-organizational agreement that addresses all four requirements is itself evidence of governance quality, independent of whether a regulatory audit ever materializes.

---

## 6. Anti-pattern: regulatory audit surprise

The anti-pattern is FAI governance records that satisfy the architecture's internal documentation standards but fail regulatory audit because retention periods, format requirements, or chain-of-custody provisions were not anticipated in advance.

Regulatory audit surprise has a characteristic structure. The governance records are complete and internally consistent — they would pass any internal review using the inspect right. But when a regulatory body requests access, some combination of the following has not been addressed:

- Records have been purged because the persistence policy used a default retention period shorter than the regulatory minimum.
- The records are not accessible to the regulatory body under any arrangement specified in the cross-organizational agreement, because no such arrangement was specified.
- The records are intelligible to CKS-architecture participants but opaque to regulatory reviewers, because documentation was written for an internal audience.
- Chain-of-custody verification is not possible because the version history or provenance chain was not preserved in a form that can be presented to the regulatory body.

Each of these failures is preventable through the four requirements specified in §4, provided those requirements are addressed in the cross-organizational agreement before events begin. Each is difficult to remediate retroactively: records that have been purged cannot be recovered; access arrangements that were not established in advance must be negotiated under regulatory time pressure; records that were not written for external audiences must be re-documented from memory or from incomplete internal artifacts; version histories that were not preserved cannot be reconstructed.

The correct governance posture is to treat regulated-domain FAI events as events that will be subject to regulatory audit — whether or not any audit actually occurs. The cross-organizational agreement should address all four requirements in its mutual governance standards (D2.34, Component 1) before the first event begins.

---

## 7. Operational test

For a FAI event in a regulated domain, an observer can apply the following test to verify that D2.63's requirements were satisfied:

1. **Regulatory retention policy:** Is the persistence policy for this domain's FAI events specified in the cross-organizational agreement? Does that policy specify a retention period that meets or exceeds the regulatory minimum applicable to this domain?

2. **Regulatory audit access provision:** Does the cross-organizational agreement specify how a regulatory body will be granted access to FAI governance records? Does it name a structural approach (direct access or joint access provision) and the mechanism through which access is provided?

3. **Record format for regulatory use:** Does the FAI configuration and cross-organizational agreement specify that Locus 2 durable records are prepared with a regulatory-reviewer audience in mind? Do the records produced contain the structural documentation, plain-language explanations, and navigable cross-references that a regulatory reviewer would need?

4. **Chain of custody:** Does the cross-organizational agreement specify how the version history and provenance chain are presented to a regulatory body? Are the mechanisms that establish record authenticity preserved in a form that can be produced under regulatory request?

A FAI governance configuration for a regulated domain that satisfies all four tests has addressed D2.63's requirements. A configuration that fails any test is exposed to regulatory audit surprise and should be remediated before events begin.

---

## 8. Summary

D2.63 derives from D2.36 (documentation standards) and D2.34 (cross-organizational governance agreements) to formalize the governance requirements for FAI events in regulated domains where external regulatory bodies may request audit access. The architectural foundation is the observation that the CKS governance record is audit-grade by design: documentation standards, path retraceability, version history, and provenance chain together produce records that a regulator can review without any special regulatory mode. The four requirements — regulatory retention policy, audit access provision, record format for regulatory use, and chain of custody — are governance specifications that translate this architectural readiness into explicit cross-organizational agreement content, addressing the specific conditions regulatory audit imposes. The anti-pattern is regulatory audit surprise: failure arising not from architectural inadequacy but from failure to anticipate regulatory requirements before events begin. Regulatory audit capability, when established in advance, is a governance quality signal that calibrates governance trust at a level internal audit alone cannot produce.

---

## Source papers

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance for Regulatory Audit Contexts.* May 15, 2026. ORCID: 0009-0004-8065-3235.
