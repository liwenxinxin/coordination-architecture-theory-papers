# FAI Event Governance Record

**Series:** Coordination Knowledge Substrate — Derivation Note Series D, Phase D2, Note D2.18  
**Note number:** 513  
**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** May 15, 2025  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

A Full Aspect Integration (FAI) event produces governance records across its complete lifecycle. D2.01 through D2.17 established the individual record types — construction records, contribution records, conflict registry records, escalation records, dissolution records, and home substrate records, among others. This note synthesizes those record types into a single audit package: the complete FAI event governance record. The package is organized into four phases — pre-construction, construction and operation, dissolution and hand-off, and home substrate — containing seventeen record categories in total, labeled (a) through (q). A FAI event is auditable end-to-end if and only if all seventeen categories are present. A missing category indicates a governance gap at the corresponding phase. The note further identifies six questions an auditor should be able to answer from the records alone and provides an operational test: given any FAI event, can an auditor locate all seventeen categories and answer all six questions without leaving the record set?

---

## 1. D2.18 as synthesis

D2.01 through D2.17 each established a specific record type required by the FAI architecture. D2.01 and D2.02 established the construction and dissolution records. D2.06 established contribution records — the per-Self, per-aspect records that document what each participating Self brought to the shared substrate. D2.10 and D2.11 established the action-feedback ingestion and DNA absorption records that document how FAI-origin content enters each Self's home evolution machinery after dissolution. D2.12 established configuration proposal and amendment records. D2.13 established the conflict registry — the record of every detected inter-Self conflict with both sides documented, tier assignment, and resolution outcome. D2.14 established escalation records. D2.15 established coverage gap assessment records and orchestration rule firing records. D2.16 established exchange bounding verification. D2.17 established home perimeter integrity verification.

Each of these record types was derived from the architectural commitments that generated it. None of them was arbitrary. Taken individually, each answers a specific governance question about a specific phase of FAI operation. Taken together, they constitute something more than a list: a complete governance record that makes a FAI event auditable from its initial configuration through the home substrate changes its dissolution produces.

D2.18 is not a new architectural commitment. Its contribution is consolidation: it names the complete set, organizes it by phase, identifies the six questions the complete set must answer, and states the operational test that determines whether any given FAI event has a complete record or a governance gap.

---

## 2. The four phases of the FAI event governance record

### Phase 1 — Pre-construction records

Three record categories are required before a FAI event's shared substrate is constructed.

**(a) Configuration proposal and amendment records.** The event's configuration — which aspects each participating Self contributes, the depth of provenance carry-over at each Self's perimeter, the persistence policy after dissolution, the cooperation or competition variant, and any other configurable dimension — must be documented as it was proposed, as it was amended, and as it was finally agreed. Who proposed the configuration, what amendments were made, and what the final agreed configuration was must all be present. These records establish that the event's governing parameters were explicit and agreed before construction began.

**(b) Joint authorization records.** The governance authorities of each participating Self must have authorized the event before its shared substrate was constructed. The joint authorization record documents which governance authorities authorized, acting under which home authority structures, and when authorization was given. Joint authorization is the mechanism by which the event is brought under human governance from both sides of the inter-Self perimeter.

**(c) Coverage gap assessment.** Before construction, governance must have assessed which conflict classes have authored resolution rules and which do not. The coverage gap assessment documents that assessment. Its purpose is not to require that all conflict classes be covered before construction — the architecture permits gaps in coverage, handled through the preserve tier — but to ensure that the governance authorities entered the event with explicit awareness of which conflict classes had authored orchestration and which would require either preservation or escalation if surfaced.

### Phase 2 — Construction and operation records

Eight record categories document the event's active lifecycle from shared substrate construction through any operational amendments.

**(d) Construction record.** The construction event itself must be recorded: the event's full provenance, the timestamp of construction, and a reference to the initial configuration that governed construction. The construction record is the event's birth record — the point at which it becomes an auditable object.

**(e) Contribution records — home substrate perspective.** For each participating Self, and for each aspect that Self contributed to the shared substrate, a contribution record is required from the contributing Self's home substrate perspective. This record documents what was contributed, from which home substrate it originated, and under which home governance authority the contribution was authorized.

**(f) Contribution records — shared substrate perspective.** The same contribution events must also be documented from the shared substrate's perspective — recording the contributed aspect content as it arrived and was integrated into the shared substrate. The two-perspective structure preserves cross-perimeter traceability: the home substrate record and the shared substrate record together establish that what arrived in the shared substrate is what the home substrate authorized to be contributed.

**(g) Conflict registry.** Every conflict detected during the event's operation must be registered. The conflict registry is a running record of detected inter-Self conflicts, with both sides of each conflict documented, attribution assigned, the tier to which each conflict was assigned (preserve, resolve via orchestration, or escalate), the resolution status, and the outcome record for resolved conflicts. No detected conflict may be absent from the registry. The registry is the primary record establishing that inter-Self conflict handling operated through the three-tier mechanism rather than through opaque resolution outside the shared substrate.

**(h) Orchestration rule firing records.** For every conflict assigned to the resolve tier, the record of which authored orchestration rule fired, what it resolved, and what outcome it produced must be present. These records establish that tier-2 resolution was rule-governed and inspectable, not ad hoc.

**(i) Escalation records.** For every conflict escalated to human governance authorities across the joint authority structure, the escalation record must document what was escalated, to whom it was escalated, when the escalation occurred, and what governance response was produced. Escalation records establish that the third tier of inter-Self conflict handling operated through human authority rather than through automated resolution outside governance.

**(j) Exchange bounding verification record.** A record confirming that exchange bounding was verified throughout the event's operation must be present. Exchange bounding is the architectural commitment that the exchange is bounded to substrate content — that instinct-layer content and model weights do not exchange across the shared substrate. The verification record documents that bounding was confirmed and what the confirmation produced.

**(k) Configuration amendments during operation.** Any amendments to the event's configuration made after construction and during operation must be recorded in the same form as the pre-construction configuration records: who proposed the amendment, what the amendment changed, what authorization it received, and when it took effect. An event with no operational amendments still satisfies this requirement — the record is simply empty for this category.

### Phase 3 — Dissolution and hand-off records

Three record categories document the event's closing lifecycle.

**(l) Dissolution record.** The dissolution event must be recorded: the authorization under which dissolution proceeded, the timestamp of dissolution, and a reference to the persistence policy that governed what would be retained and what would dissolve. The dissolution record is the event's death record — the point at which the shared substrate exits operation.

**(m) Persistence policy execution record.** The persistence policy governs what remains after dissolution: at one extreme, only the evolution outputs each participating Self ingests into its home substrate; at the other extreme, the full shared substrate retained as durable inter-organizational record. The persistence policy execution record documents which option was in effect and what was retained at Locus 2 — the shared substrate as durable record — versus what dissolved. This record establishes that the persistence policy was executed as configured and not selectively applied.

**(n) Hand-off boundary activation record.** Content flowing from the dissolving shared substrate to each participating Self's home substrate crosses each Self's home perimeter through the hand-off boundary. The hand-off boundary activation record documents what content flowed to which home substrate and when the flow occurred. For each participating Self, the record must be present. Together, the hand-off boundary activation records establish the complete accounting of what left the shared substrate and where it went.

### Phase 4 — Home substrate records

Three record categories document what happened within each participating Self's home substrate as a result of the FAI event.

**(o) Action-feedback ingestion records.** FAI-origin action-layer content — recorded task instances, outputs, lived experience from the event — that each participating Self ingested into its home action layer must be documented. The action-feedback ingestion record covers what FAI-origin content was ingested, through which governance-authorized pathway it entered the home action layer, and what home governance authorization covered the ingestion. Action-layer content from a FAI event is, from each Self's home perspective, a class of lived experience; the ingestion record establishes that this lived experience entered the home evolution machinery through authorized channels.

**(p) DNA absorption records.** Where a participating Self's governance authorized absorption of DNA-layer content from the FAI event — orchestration patterns, schemas, rules, or other DNA-layer material from another Self's contributed aspects — each such directed selection event must be documented. The DNA absorption record covers what was absorbed, what home governance authorization covered the absorption, and any provenance from the source Self that traveled with the absorbed content. Where no DNA absorption occurred, this record is empty for that Self; a FAI event may produce action-layer ingestion without DNA absorption.

**(q) Home perimeter integrity verification.** For each participating Self, a record confirming that the Self's home substrate underwent no unintended changes during or after the FAI event must be present. The home perimeter integrity verification establishes that the only changes to each Self's home substrate were those that occurred through the authorized ingestion and absorption pathways documented in records (o) and (p). This record closes the audit: it confirms that the inter-Self exchange was bounded and that home substrate governance remained intact throughout.

---

## 3. The complete record as an audit package

The seventeen record categories constitute an audit package. An auditor reviewing a FAI event should be able to obtain all records across the four phases and answer six questions from the records alone — without external investigation, without interviewing participants, and without reconstructing what happened from indirect evidence.

**Question 1:** Was the FAI event properly configured and jointly authorized before construction? The answer is traceable to records (a), (b), and (c): the configuration that governed the event was proposed and agreed before construction; the governance authorities of each participating Self authorized the event; and the coverage gap assessment established which conflict classes had authored rules and which did not.

**Question 2:** Was every conflict detected, registered, and handled through the three-tier mechanism? The answer is traceable to records (g), (h), and (i): every detected conflict appears in the conflict registry with its tier assignment and outcome; every tier-2 resolution has an orchestration rule firing record; every tier-3 escalation has a governance response record.

**Question 3:** Was exchange bounding maintained throughout? The answer is traceable to record (j): the exchange bounding verification record documents that bounding was confirmed and what the confirmation produced.

**Question 4:** Did dissolution proceed per the persistence policy? The answer is traceable to records (l), (m), and (n): the dissolution event was authorized and recorded; the persistence policy was executed as configured; and the hand-off boundary activation records account for all content that left the shared substrate.

**Question 5:** Did each participating Self's home perimeter remain intact? The answer is traceable to record (q): the home perimeter integrity verification for each Self confirms that no unintended changes occurred to each Self's home substrate.

**Question 6:** Did each Self's home evolution — ingestion and absorption — proceed with governance authorization? The answer is traceable to records (o) and (p): the action-feedback ingestion records and DNA absorption records document every pathway by which FAI-origin content entered each home substrate, along with the governance authorization that covered each pathway.

---

## 4. The minimum complete record

A FAI event is auditable if and only if all seventeen record categories are present. The minimum complete record is not a subset of the seventeen categories; it is all seventeen. The architecture does not permit an auditor to infer missing records from present ones — a missing escalation record does not mean no escalations occurred; it means the governance record does not establish that escalation handling operated correctly. A missing home perimeter integrity verification does not mean home perimeters remained intact; it means the record does not establish that they did.

A FAI event with fewer than seventeen record categories has a governance gap. The location of the gap — which phase, which category — identifies where governance failed. A gap in Phase 1 means the event operated without a documented pre-construction governance posture. A gap in Phase 2 means some aspect of the event's active operation was ungoverned or undocumented. A gap in Phase 3 means dissolution accountability is incomplete. A gap in Phase 4 means the home substrate effects of the event are not established in the record.

The record categories also map to specific prior derivation notes, so a governance gap in any category can be traced to the specific architectural commitment that the missing record was meant to satisfy. A missing conflict registry traces to D2.13; a missing home perimeter integrity verification traces to D2.17; a missing DNA absorption record traces to D2.11. This traceability is not incidental — it is what makes the audit package a derivation-grounded governance structure rather than a checklist.

---

## 5. Inheritance from Paper 2's entity lifecycle governance record

The four-phase, seventeen-category FAI event governance record is the inter-Self analog of the entity lifecycle governance record Paper 2 establishes for single-entity governance history. Paper 2's entity lifecycle produces a complete governance record: the birth record documenting the entity's construction; the directed selection records documenting every instance in which the entity's DNA layer was deliberately evolved; the mating records documenting inter-entity coordination events under home governance; and the death record documenting dissolution and the persistence policy its dissolution followed.

The structural parallel is exact. FAI pre-construction records correspond to the governance posture that precedes a Paper 2 mating event — configuration and joint authorization are the inter-Self analog of the within-Self authorization that precedes directed selection. FAI construction and operation records correspond to the Paper 2 mating record itself — the active event, with its conflicts, its orchestration, and its escalations all documented. FAI dissolution and hand-off records correspond to the Paper 2 death record — the event ends, persistence is governed, and what flows out is accounted for. FAI home substrate records are the inter-Self extension of what Paper 2's directed selection records capture at within-Self scope — the evolution feed from one event entering the governance record of each participating Self's ongoing lifecycle.

This inheritance is architecturally significant because it closes the adversarial gap for FAI governance record requirements. If an auditor or regulator requires that an entity's lifecycle governance record be complete — as Paper 2's structure establishes — the same requirement extends to FAI events by the structural parallel. A FAI event is a mating event at inter-Self scope, and the same completeness requirement that applies to within-Self mating records applies to inter-Self FAI records. The seventeen-category package is not a new burden; it is the application of Paper 2's completeness requirement at the scope Paper 3 introduces.

---

## 6. Operational test

For any FAI event, the governance record is complete if and only if an auditor can:

1. Locate all seventeen record categories — (a) through (q) — in the records produced by the event.
2. Answer all six audit questions — configuration and authorization; conflict handling; exchange bounding; dissolution; home perimeter integrity; home evolution authorization — from those records alone, without external investigation.

A FAI event that passes both conditions is auditable end-to-end. A FAI event that fails either condition has a governance gap. Condition 1 determines whether the record exists; Condition 2 determines whether the record is sufficient to establish what governance requires. A record that exists but does not answer its corresponding audit question satisfies Condition 1 but fails Condition 2 — the record is present but not complete enough to serve its governance function.

The operational test can be applied prospectively — when designing a FAI event's governance configuration, checking whether the planned record structure will produce all seventeen categories and support all six questions — and retrospectively, when auditing a completed event's governance record. Both directions of application are valid uses of the test.

---

## 7. Conclusion

D2.18 synthesizes the record types established in D2.01 through D2.17 into a single unified governance record for FAI events. The complete record spans four phases — pre-construction, construction and operation, dissolution and hand-off, and home substrate — and contains seventeen required categories. All seventeen are required; a missing category is a governance gap, not an acceptable abbreviation. An auditor holding the complete record should be able to answer six questions about the event from the records alone. The FAI event governance record inherits its completeness requirement from Paper 2's entity lifecycle governance record, extending that requirement to inter-Self scope through the structural parallel between FAI events and Paper 2 mating events.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Event Governance Record.* Derivation Note D2.18 (#513), CKS Derivation Note Series. May 15, 2026. ORCID: 0009-0004-8065-3235.
