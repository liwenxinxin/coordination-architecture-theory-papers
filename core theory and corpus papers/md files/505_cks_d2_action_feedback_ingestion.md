# Action-Feedback Ingestion Governance at FAI Dissolution

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D1.17 commits that when a Full Aspect Integration (FAI) event dissolves, action-layer content from the shared substrate enters each participating Self's home action layer through the action-feedback locus. This note formalizes the operational governance requirements for that ingestion. Three requirements govern the transition: home governance must authorize every ingestion event, whether through standing configuration or per-event review; all ingested records must carry provenance identifying their FAI origin; and the ingestion event itself must be recorded as home governance content. Once ingested, FAI-origin records enter the Paper 2 action-feedback pipeline without modification — the same proposal, Stage 1 review, Stage 2 human decision, and directed-selection sequence that processes home-generated records. The pipeline is not extended or supplemented for FAI-origin content; FAI origin is metadata on the record, not a routing condition. The note states an anti-pattern — non-attributed ingestion — in which FAI-origin content enters the home action layer without provenance, making inter-Self learning indistinguishable from home-generated content and breaking the governance traceability the three requirements collectively protect.

---

## 1. Derivation context

D2.10 is an operational decomposition of D1.17. D1.17 commits that FAI event outcomes enter each participating Self's home action layer through the action-feedback locus at the FAI hand-off boundary. That commitment names the locus and the direction of flow; it does not specify the governance requirements that make the flow auditable and traceable. D2.10 supplies those requirements.

The broader context is Paper 3's Claim 4: the four-locus evolution-feed mechanism at the FAI hand-off boundary. Claim 4 establishes that when the shared substrate dissolves at the close of an FAI event, content propagates to each participating Self's home substrate through its existing Paper 2 evolution mechanisms, operating at home under home governance. The layer-routing rule within Claim 4 specifies that action-layer content from the FAI event feeds action-feedback evolution operating within home action layers. D2.10 formalizes what governance requires at the moment that routing takes effect — at the point of ingestion through the action-feedback locus.

Three prior commitments constrain D2.10's requirements without being re-derived here. First, Paper 1's commitment to human governance as an authority architecture (the three rights: inspect, modify, override) applies within each Self's home substrate as a property of its design; ingestion into the home action layer is a substrate operation and therefore within that architecture's scope. Second, Paper 1's six metadata fields (A1.07) apply to records held in the substrate; records ingested from an FAI event are substrate records and inherit the metadata requirement. Third, Paper 2's action-feedback pipeline (B1.15) specifies how action-layer content reaches governance for review and decision; D2.10 does not alter the pipeline, it specifies that FAI-origin content enters it.

---

## 2. What is eligible for ingestion

At the FAI hand-off boundary, the following categories of action-layer content are eligible for ingestion into each participating Self's home action layer:

**FAI event operational results.** The outcomes produced during the FAI event — the coordination work performed within the shared substrate. These are action-layer records of what occurred during the event: what was attempted, what was completed, what state the coordination task reached.

**Conflict carry-through annotations.** When the three-tier conflict-handling mechanism (D1.13–D1.16) preserves a conflict at the substrate level rather than resolving it within the FAI event, that preserved conflict boundary carries through to the home substrate as an annotation on the ingested action-layer content. The annotation marks a boundary that home governance must address under home authority during the action-feedback pipeline.

**Governance records of significance.** Summaries of key governance decisions made within the shared substrate during the FAI event: which content was resolved in what direction, what was escalated, how the orchestration-layer handled contested content. These records are not the full shared substrate governance log; they are the summary content that home governance has configured as worth ingesting for home evolution purposes.

Eligibility is governed by each Self's home governance through the hand-off boundary configuration. Paper 3 §8 (Claim 5, configuration as substrate content) applies: the configuration that specifies which categories of FAI-origin content are eligible for ingestion is itself substrate content, authored by home governance, subject to the three rights. Different Selves may configure different eligibility rules for the same FAI event — the asymmetric ingestion property established in Claim 4 applies here. There is no architectural requirement that all Selves take the same content from a shared FAI event.

---

## 3. Three requirements for ingestion governance

### Requirement 1 — Home governance authorization

The ingestion of FAI-origin content into the home action layer must be authorized by home governance. This requirement admits two valid forms.

*Standing configuration.* Home governance authors a standing rule: all FAI outcomes meeting the eligibility configuration are ingested at dissolution. This is the common operational form. It does not require per-event review; the review occurred when governance authored the standing rule. Under standing configuration, ingestion at each FAI dissolution is automatic in execution but governed in origin — the standing rule is substrate content authored by humans, subject to the inspect, modify, and override rights at any time.

*Per-event authorization.* At dissolution, home governance reviews the specific content available for ingestion and authorizes what is taken. This form is appropriate where the FAI event involved unusual content, where the participating Selves were unfamiliar, or where governance policy requires review before each inter-Self absorption.

Both forms satisfy Requirement 1. What neither form permits is ingestion that bypasses governance authorization entirely — content flowing into the home action layer without either a standing rule that covers it or a per-event authorization decision. The requirement is that authorization in some form exists and is traceable.

The authorization record is home governance content. For standing configuration, the record is the standing rule itself and the governance decision that authored it. For per-event authorization, the record is the decision artifact produced at dissolution. Either way, the authorization can be retrieved by any party with inspect rights on the home substrate.

### Requirement 2 — FAI-origin provenance on ingested records

All FAI-origin content ingested into the home action layer must carry provenance identifying its FAI origin. This provenance is part of the record's metadata — specifically the six fields established in Paper 1 (A1.07) and applied to records held in the substrate. Applied to FAI-origin ingested records, the relevant provenance fields identify: which FAI event produced the content, which contributing Self or Selves were the source, and what governance context surrounded the content within the shared substrate.

This requirement is not a best practice; it is the structural basis for the traceability of inter-Self learning. Without FAI-origin provenance, ingested records are indistinguishable in the home action layer from home-generated records. Home governance cannot trace which action-layer content derives from inter-Self coordination and which derives from the Self's own home operations. The action-feedback pipeline processes content without knowing which learning is home-origin and which is FAI-origin. Over time, the home substrate accumulates action-layer content whose genealogy is opaque.

The provenance requirement does not require that FAI-origin records be processed differently from home-generated records — the pipeline is unchanged, as §4 specifies. It requires that the records carry enough metadata to permit governance to exercise its inspect right meaningfully: to trace a record's origin to the FAI event that produced it, the Self that contributed it, and the governance context that governed it within the shared substrate.

### Requirement 3 — Ingestion record

The ingestion event itself is recorded as home governance content. This record captures: what content was ingested, from which FAI event, at what time, under what authorization form (standing rule identifier or per-event decision reference). The ingestion record is the home substrate's own governance artifact for the FAI-to-home transition.

The ingestion record is distinct from the provenance metadata on individual ingested records (Requirement 2). Requirement 2 governs each record individually — each carries its own FAI-origin provenance. Requirement 3 governs the ingestion event as a whole — a single record captures the transition at the event level. Together they provide two inspection paths: an observer can locate the ingestion record to understand what arrived from a given FAI event at a given time, and can inspect any individual ingested record to find its specific FAI-origin provenance.

The ingestion record is substrate content subject to the three rights. It is not an audit log held in infrastructure outside the substrate; it is a governance artifact held within the home substrate under the same authority architecture that governs all home substrate content.

---

## 4. Post-ingestion: the unchanged Paper 2 action-feedback pipeline

Once ingested through the action-feedback locus, FAI-origin action-layer records enter the home action-feedback pipeline exactly as any other action-layer content enters it. The pipeline is not modified, extended, or supplemented for FAI-origin records.

The Paper 2 action-feedback pipeline (B1.15) operates as follows within the home substrate:

The proposing substrate — the AI system operating within the Self under the home substrate's governance — evaluates the action layer. The action layer now contains both home-generated records and FAI-origin records, each carrying appropriate provenance metadata. The proposing substrate generates proposals based on this combined action layer.

Proposals proceed to Stage 1 governance review, where orchestration-layer mechanisms evaluate them against home governance rules. Stage 1 review does not apply a different pathway to proposals informed by FAI-origin records versus proposals informed by home-generated records. The FAI origin of input records is visible through their provenance metadata, but the review process is the same process.

Proposals that clear Stage 1 proceed to Stage 2 human governance decision. Humans holding authority in the home governance structure review and decide on proposals. They may recognize FAI-origin records in a proposal's basis through their provenance metadata and factor that origin into their decision. Or they may treat FAI-origin records as equivalent to home-generated records for decision purposes. Either is valid; the decision authority rests with home governance.

Approved proposals are implemented through directed selection — the Paper 2 mechanism for updating the home action layer under governance authorization.

The proposing substrate may be configured to surface FAI-origin provenance in its proposals — drawing attention to the fact that a proposal draws on inter-Self learning rather than home-generated content. This is a valid configuration. It is not architecturally required. The pipeline supports it because the provenance metadata is present on each ingested record; whether to surface it prominently is a governance configuration decision within the home substrate.

The prior-art claim is precise: no new action-feedback mechanism is introduced at the inter-Self boundary. FAI-origin content enters home action-feedback evolution through the same governance-authorized pipeline that processes all action-layer content. The existence of a shared FAI event upstream does not add a new pipeline step, a new review tier, or a new approval layer within the home substrate.

---

## 5. Anti-pattern: non-attributed ingestion

**Non-attributed ingestion** is the failure mode in which FAI-origin content enters the home action layer without provenance identifying its FAI origin, making it indistinguishable from home-generated content.

Non-attributed ingestion may occur in several ways: the provenance metadata fields are not populated at ingestion; the ingestion mechanism strips provenance before writing records to the home action layer; the FAI event produces content that is merged directly into home action-layer records without a distinct ingestion step. In each case, the result is the same — records that originated in inter-Self coordination are present in the home action layer but cannot be identified as such.

The governance damage from non-attributed ingestion is not primarily operational in the short run. The action-feedback pipeline functions; proposals are generated; humans make decisions. The damage is to the substrate's traceability over time. Home governance cannot distinguish which of the Self's action-layer evolution derives from home operations and which derives from FAI events with other Selves. The three rights — inspect, modify, override — can be exercised on individual records, but governance cannot exercise meaningful oversight of the inter-Self learning trajectory because the inter-Self origin is gone.

Non-attributed ingestion also breaks Requirement 3. If ingested records carry no FAI-origin provenance, the ingestion record required by Requirement 3 cannot accurately represent what was ingested or where it came from. The two requirements are architecturally coupled: Requirement 3's event-level ingestion record is only meaningful if Requirement 2's per-record provenance is accurate.

The anti-pattern is not about whether FAI-origin records are processed differently from home-generated records — they are not, per §4. It is specifically about whether governance can tell, after the fact, which records came from FAI events. That traceability is the property at stake.

---

## 6. Operational test

An implementation satisfies D2.10's governance requirements if and only if all of the following are true for each FAI dissolution event in which the Self participated:

**Authorization traceability.** An observer with inspect rights on the home substrate can locate an authorization record — either a standing configuration rule that covers the ingestion or a per-event authorization decision — for the ingestion of FAI-origin content from this event. The authorization record was authored by home governance and is subject to the three rights.

**Per-record provenance.** Each FAI-origin record present in the home action layer carries provenance metadata identifying its FAI event of origin, the contributing Self or Selves, and the governance context within the shared substrate. An observer can retrieve this provenance from the record without reference to external records.

**Ingestion record.** An observer can locate an ingestion record within the home substrate — separate from individual record provenance — that captures what was ingested from this FAI event, at what time, and under what authorization. This record is home governance content subject to the three rights.

**Standard pipeline.** An observer can confirm that FAI-origin action-layer records entered the home action-feedback pipeline through the same proposal, Stage 1 review, Stage 2 human decision, and directed-selection sequence used for home-generated records. No separate pipeline or supplementary review tier was introduced for FAI-origin content.

A system that fails any of these conditions does not satisfy D2.10, regardless of whether it satisfies D1.17's structural commitment to the action-feedback locus. D1.17 establishes that the locus exists; D2.10 establishes the governance requirements that make the locus's operation traceable.
