# Phase D3 Overview and FAI Anti-Pattern Taxonomy

**Derivation Note D3.01 — #576 in the CKS Derivation Series**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Phase D3 is the anti-pattern formalization phase of the Series D derivation corpus. Its purpose is to give each FAI governance failure mode — named in passing across the Phase D2 operational-variants corpus — standalone prior-art depth as a dedicated derivation note. This note, D3.01, serves as the Phase D3 overview and taxonomy introduction. It states the relationship between Phase D2 and Phase D3, presents the complete twenty-seven anti-pattern taxonomy organized in seven categories (Lifecycle Governance Failures, Conflict Handling Failures, Evolution Feed Failures, Configuration Failures, Perimeter and Content Failures, Governance Quality Failures, and Population-Scope Failures), specifies the consistent seven-element structure that each subsequent note (D3.02–D3.30) follows, and states Phase D3's scope and closure. The taxonomy expands the twelve core anti-patterns named in D2.19 to twenty-seven by consolidating all failure modes identified across the full Phase D2 corpus.

---

## 1. The relationship between Phase D2 and Phase D3

Phase D2 is the operational-variants phase of Series D. Across approximately eighty notes (D2.01–D2.80), Phase D2 decomposes each of Paper 3's foundational sub-commitments into operational variants: the specific conditions under which each commitment holds, the configurations it permits, the boundaries it enforces, and the governance behaviors it requires. As a byproduct of this operational decomposition, Phase D2 names governance failure modes — conditions under which a deployed system violates a commitment without the violation being immediately visible in governance records.

Phase D2's naming of failure modes is functional for the purpose of each individual D2 note — the anti-pattern is named to sharpen the contrast with the commitment being decomposed — but it is not designed to serve as a standalone governance reference. A practitioner identifying a potential failure mode in a deployed system needs more than a name and a contrast statement. They need detection criteria, consequence analysis, identification of the specific governance commitment being violated, the intra-Self analog from Paper 2's Series B where one exists, and resolution guidance that specifies what correct governance looks like.

Phase D3 provides this. For each of the twenty-seven failure modes named across Phase D2, Phase D3 produces a dedicated note with those five additional analytical layers. The note also serves as a prior-art record: an independently-dated, specifically-titled derivation document that anchors each failure mode in the CKS governance architecture with a precision that passing D2 references cannot provide.

The relationship is additive and non-redundant. D2 notes remain the source authority for each failure mode's definition within the context of the commitment being decomposed. D3 notes do not redefine or revise D2 definitions; they elevate each failure mode to the depth required for independent reference.

---

## 2. Taxonomy expansion: from twelve to twenty-seven

D2.19 introduced a preliminary anti-pattern taxonomy covering twelve governance failure modes identified as of that note's position in the Phase D2 sequence. That twelve-pattern taxonomy was explicitly marked as preliminary — covering the failure modes visible at D2.19's position in the corpus, not the full set that Phase D2 would eventually name.

The complete Phase D3 taxonomy contains twenty-seven anti-patterns, consolidated from the full Phase D2 corpus. The fifteen additional failure modes (AP-13 through AP-27) were named in D2 notes published after D2.19, as Phase D2's decomposition extended into conflict handling, evolution feed, configuration, perimeter, governance quality, and population-scope sub-commitments. D3.01 is the first note in the corpus to present all twenty-seven in one authoritative list.

The expansion is consolidation, not invention. Every anti-pattern in the twenty-seven-pattern taxonomy was already named in a Phase D2 note. Phase D3 adds depth and standalone reference status; it does not add new failure modes beyond what Phase D2 identified.

---

## 3. The complete FAI anti-pattern taxonomy

### Category 1 — Lifecycle Governance Failures

Failure modes in which a shared substrate's construction, operation, or dissolution is not governed under the commitments Paper 3 establishes for the FAI lifecycle.

| Code | Anti-Pattern Name | Phase D2 Source |
|------|-------------------|-----------------|
| AP-1 | Ungoverned Construction | D2.01 |
| AP-2 | Ungoverned Dissolution | D2.02 |
| AP-13 | Silent Offboarding | D2.70 |

**AP-1 (Ungoverned Construction):** A shared substrate is constructed for an FAI event without a governance record establishing which Selves participate, what aspects each contributes, what the persistence policy is, and under whose authority the event operates. The construction happens, but not as substrate content under human-governed authority.

**AP-2 (Ungoverned Dissolution):** A shared substrate dissolves — either at event completion or through abandonment — without a governance record establishing what was preserved, where evolution outputs were routed, and what auditable record (if any) was retained. The dissolution happens, but not as a governed transition.

**AP-13 (Silent Offboarding):** A participating Self is removed from an ongoing or future FAI configuration without the removal being recorded as substrate content under the authority of all affected Selves' governance structures.

---

### Category 2 — Conflict Handling Failures

Failure modes in which inter-Self conflicts arising during an FAI event are not handled through Paper 3's three-tier mechanism (preserve / resolve via orchestration / escalate to humans).

| Code | Anti-Pattern Name | Phase D2 Source |
|------|-------------------|-----------------|
| AP-3 | Silent Conflict Collapse | D2.07 |
| AP-11 | Unresponsive Escalation | D2.14 |
| AP-12 | Informal Resolution Rules | D2.15 |
| AP-14 | Competitive Intelligence Misrouting | D2.65 |

**AP-3 (Silent Conflict Collapse):** A conflict between aspects contributed by different Selves is resolved inside the shared substrate by AI mediation, without the conflict being preserved as first-class state and without the resolution being recorded as a governed outcome. The conflict disappears rather than being handled.

**AP-11 (Unresponsive Escalation):** A conflict reaches the escalation tier — it cannot be preserved or resolved by orchestration — but the humans holding governance authority over the relevant Selves do not respond within any governance-configured window, and the conflict is abandoned rather than held pending resolution.

**AP-12 (Informal Resolution Rules):** Orchestration rules governing conflict resolution within the shared substrate are communicated informally rather than existing as human-authored substrate content subject to the inspect and modify rights. Resolution behavior is not inspectable from the substrate.

**AP-14 (Competitive Intelligence Misrouting):** Content from one Self's contributed aspects — specifically content that carries competitive sensitivity — is routed to another Self's evolution feed through the FAI event without the governance configuration authorizing that routing.

---

### Category 3 — Evolution Feed Failures

Failure modes in which the connection between FAI events and participating Selves' home evolution mechanisms operates outside the governance commitments Paper 3 establishes for the four-locus evolution feed.

| Code | Anti-Pattern Name | Phase D2 Source |
|------|-------------------|-----------------|
| AP-4 | Automatic DNA Absorption | D2.11 |
| AP-5 | Non-Attributed Ingestion | D2.10 |
| AP-15 | Vertical Propagation Break | D2.57 |
| AP-16 | Unconfigured Proposing Substrate | D2.59 |

**AP-4 (Automatic DNA Absorption):** Orchestration patterns, schemas, or rules from another Self's contributed aspects are absorbed into the receiving Self's DNA layer without home governance authorizing the absorption. The DNA changes, but not through directed selection under human authority.

**AP-5 (Non-Attributed Ingestion):** Evolution outputs ingested from an FAI event into a home substrate lose provenance attribution — the record that the content originated from a specific FAI event, from a specific contributing Self. The ingested content cannot be traced to its inter-Self origin.

**AP-15 (Vertical Propagation Break):** Evolution outputs from an FAI event that should propagate across the receiving Self's aspect hierarchy — because they update DNA content that structures multiple aspects — propagate only to the aspect directly involved in the FAI event, not to dependent aspects.

**AP-16 (Unconfigured Proposing Substrate):** A Self proposes content for absorption into another Self's home substrate through an FAI evolution output without the proposing substrate configuration being established as substrate content under both Selves' governance authority.

---

### Category 4 — Configuration Failures

Failure modes in which the configurable dimensions of FAI protocol operation are not managed as human-governed substrate content under the commitments Paper 3 establishes for configuration governance.

| Code | Anti-Pattern Name | Phase D2 Source |
|------|-------------------|-----------------|
| AP-6 | Implicit Configuration | D2.12 |
| AP-9 | Pseudo-Selective Merge | D2.08 |
| AP-17 | N-Blind Configuration | D2.22 |
| AP-18 | Forgotten Standing Configuration | D2.21 |
| AP-19 | Time-Pressure Governance Bypass | D2.41 |

**AP-6 (Implicit Configuration):** One or more configurable FAI dimensions — which aspects are contributed, what the persistence policy is, what the conflict-handling tier sequence is — operates by runtime default rather than by human-authored substrate content. The configuration exists implicitly in system behavior, not explicitly in the substrate.

**AP-9 (Pseudo-Selective Merge):** A merge is recorded as selective — only certain aspect content integrated into the shared substrate — but the selection is performed by AI mediation without the selection criteria existing as human-authored substrate content. The merge appears governed but is not.

**AP-17 (N-Blind Configuration):** A FAI configuration is authored for two-Self participation and extended to three or more Selves without the n-ary cardinality change being governed — without the additional Selves' participation, their aspect contributions, and the conflict-handling implications of the larger participant set being explicitly configured.

**AP-18 (Forgotten Standing Configuration):** A standing FAI configuration — one established for recurring events between the same Selves — remains active after the conditions that warranted it have changed, because no governance review mechanism for standing configurations exists in the substrate.

**AP-19 (Time-Pressure Governance Bypass):** Operational urgency is used to justify conducting an FAI event without completing the governance record that Paper 3 requires — persisting the construction record, the participation configuration, or the persistence policy — on the assumption that the record will be completed retrospectively.

---

### Category 5 — Perimeter and Content Failures

Failure modes in which the boundary between a Self's home governance perimeter and the shared substrate is violated, or in which content within the shared substrate exceeds or misrepresents what the exchange commitment authorizes.

| Code | Anti-Pattern Name | Phase D2 Source |
|------|-------------------|-----------------|
| AP-7 | Home Perimeter Erosion | D2.17 |
| AP-8 | Exchange Bounding Violation | D2.16 |
| AP-10 | Shallow-Reference Merge | D2.09 |
| AP-20 | FAI-Oblivious Restructuring | D2.55 |

**AP-7 (Home Perimeter Erosion):** Content from the shared substrate flows back into a participating Self's home substrate through a path outside the governed evolution feed — bypassing the home governance authority that Paper 3 requires to authorize ingestion.

**AP-8 (Exchange Bounding Violation):** Instinct-layer content or LLM-weight information is introduced into the shared substrate during an FAI event, violating the Paper 3 commitment that exchange is bounded to substrate content (DNA-layer and action-layer content from Paper 2's reasoning layer).

**AP-10 (Shallow-Reference Merge):** Aspects are merged into the shared substrate at the reference level — identifiers or pointers to content held in a participating Self's home substrate — rather than at the content level. The shared substrate carries apparent integration without carrying the actual content the governance commitments operate over.

**AP-20 (FAI-Oblivious Restructuring):** A participating Self restructures its home substrate — reorganizing aspects, renaming cells, changing DNA content — during or after an FAI event without accounting for the shared substrate's dependency on the pre-restructuring home substrate state. The shared substrate and the home substrate fall out of consistency without the inconsistency being recorded as a conflict.

---

### Category 6 — Governance Quality Failures

Failure modes in which the governance record for FAI events exists formally but does not satisfy the substantive governance properties that Paper 3's commitments require.

| Code | Anti-Pattern Name | Phase D2 Source |
|------|-------------------|-----------------|
| AP-21 | Governance Theater | D2.36 |
| AP-22 | Black Box Shared Substrate | D2.66 |
| AP-23 | Authorization Chain Gap | D2.67 |
| AP-24 | Automated Governance | D2.43 |

**AP-21 (Governance Theater):** A governance record for an FAI event exists and is structurally complete but was produced to satisfy a compliance requirement rather than to exercise genuine governance authority. The record cannot be used to reconstruct what was governed, by whom, and under what authority.

**AP-22 (Black Box Shared Substrate):** The shared substrate's content is not inspectable by the humans holding governance authority over participating Selves — either because the substrate is stored in a format requiring specialized tooling not held by governance-authority holders, or because access controls prevent inspection by those with governance rights.

**AP-23 (Authorization Chain Gap):** The human authority that governs a participating Self has not explicitly delegated FAI participation authority to the operators who conducted the event. The event was conducted by individuals with operational access but without a traceable authorization chain extending to the Self's governance authority.

**AP-24 (Automated Governance):** Governance records for FAI events are generated by automated processes — AI-drafted and auto-committed without human authority review — rather than being human-authored substrate content. The form of governance is present; the authority-based property is not.

---

### Category 7 — Population-Scope Failures

Failure modes that arise specifically at the population scale of Paper 3's Claim 6 — where many Selves coordinate across a shared governance ecology — and that are not fully visible at two-Self FAI scope.

| Code | Anti-Pattern Name | Phase D2 Source |
|------|-------------------|-----------------|
| AP-25 | Topology Lock-In | D2.61 |
| AP-26 | Participation Mode Gaming | D2.62 |
| AP-27 | Forced Propagation | D2.32 |

**AP-25 (Topology Lock-In):** A population-scale coordination topology — which Selves participate in FAI with which others, under what standing configurations — becomes fixed through accumulated event history rather than through explicit governance configuration, so that governance authority over topology is lost without any single event recording the loss.

**AP-26 (Participation Mode Gaming):** A Self adjusts which aspects it contributes to FAI events based on what it expects other Selves to contribute — optimizing its own evolution-feed outcomes at population scale rather than contributing aspects governed by home authority's genuine assessment of what exchange serves the shared substrate's purpose.

**AP-27 (Forced Propagation):** An evolution output from an FAI event is propagated into a participating Self's home substrate by an external governance actor — another Self, an orchestration layer, or a population-level coordination mechanism — without the receiving Self's home governance authority authorizing the ingestion.

---

## 4. Note structure for D3.02–D3.30

Each subsequent Phase D3 note addresses one anti-pattern following a consistent seven-element structure. The structure is identical across all twenty-seven notes; practitioners can locate the same information in the same position regardless of which anti-pattern they are consulting.

**Element 1 — Anti-pattern name and category.** The anti-pattern's canonical name, its taxonomy code (AP-1 through AP-27), and its category among the seven taxonomy categories. Cross-reference to the Phase D2 source note in which the anti-pattern was first named.

**Element 2 — Description.** What the anti-pattern is: the governance condition it describes, how it arises, and what makes it a failure mode rather than a governed configuration choice. This section provides the precision that passing D2 references do not.

**Element 3 — Detection criteria.** How to identify the anti-pattern in governance records of a deployed system. Detection criteria are stated as observable conditions in substrate content, governance records, or system behavior — not as subjective assessments. The aim is that a practitioner with access to the substrate and its governance records can apply the criteria without specialized judgment beyond familiarity with the CKS architecture.

**Element 4 — Governance commitment violated.** The specific Paper 3 commitment the anti-pattern violates, with reference to the relevant claim and section. Where the violated commitment inherits from Paper 1 or Paper 2, the inheritance chain is identified. This section anchors the anti-pattern in the CKS theory rather than treating it as a standalone empirical observation.

**Element 5 — Consequences.** What governance failures result from the anti-pattern's presence: which properties are lost (inspectability, authority traceability, conflict-first-class status, etc.), what downstream harms become possible, and how the failure mode can compound with others if unaddressed.

**Element 6 — Intra-Self analog.** Where the anti-pattern has a corresponding intra-Self failure mode identified in Series B (Paper 2's derivation corpus), that analog is named and the relationship stated. Some Phase D3 anti-patterns are direct extensions of Series B anti-patterns to the inter-Self scope; others are specific to the inter-Self context and have no direct Series B analog. Both cases are explicitly noted.

**Element 7 — Resolution.** What correct governance looks like in place of the anti-pattern: the substrate content that should exist, the authority structure it should reflect, and the governance behavior that the commitment requires. Resolution guidance is prescriptive and stated in terms the CKS architecture defines, not as general governance advice.

---

## 5. Phase D3 scope

**D3.01 (this note)** is the Phase D3 overview and taxonomy introduction. It does not analyze any individual anti-pattern at full depth; its role is to establish the taxonomy, the note structure, and the relationship between Phase D2 and Phase D3 before the per-anti-pattern notes begin.

**D3.02–D3.08** cover Category 1 (Lifecycle Governance Failures) and Category 2 (Conflict Handling Failures): the seven anti-patterns AP-1 through AP-3 and AP-11, AP-12, AP-14 in standalone note form.

**D3.09–D3.15** cover Category 3 (Evolution Feed Failures) and Category 4 (Configuration Failures): the nine anti-patterns AP-4, AP-5, AP-15, AP-16 and AP-6, AP-9, AP-17, AP-18, AP-19.

**D3.16–D3.22** cover Category 5 (Perimeter and Content Failures) and Category 6 (Governance Quality Failures): the eight anti-patterns AP-7, AP-8, AP-10, AP-20 and AP-21, AP-22, AP-23, AP-24.

**D3.23–D3.25** cover Category 7 (Population-Scope Failures): the three anti-patterns AP-25, AP-26, AP-27.

**D3.26–D3.28** address anti-patterns that appear in multiple categories or that interact across categories in ways that single-category treatment obscures — cross-cutting failure modes whose full analysis requires reference to more than one commitment cluster.

**D3.29** is a cross-category analysis: how anti-patterns combine in practice, which pairings produce compounding failures, and what early-detection posture can prevent the most consequential combinations.

**D3.30** closes Phase D3 with a summary of the prior-art coverage the full phase provides and the transition to Phase D4 (composition pairs).

---

## 6. Why the consistent structure matters

The seven-element structure is not a stylistic convention. It serves the specific epistemic purpose of making Phase D3 useful as a governance reference independent of the derivation context in which it was produced.

A practitioner who has identified a suspected governance failure in a deployed system needs to answer three questions in sequence: Is this actually the anti-pattern I think it is (detection criteria)? What commitment does it violate (governance commitment, with paper reference)? What do I do about it (resolution)? The seven-element structure ensures those three questions have consistent, locatable answers in every Phase D3 note.

The intra-Self analog element serves a different purpose: it connects Phase D3 to the Series B corpus, allowing practitioners familiar with intra-Self governance failure modes to locate the inter-Self analogs without surveying the full Phase D3 corpus. Where Series B has characterized a failure mode in detail, Phase D3 inherits that characterization and identifies what changes at the inter-Self scope.

The consequences element serves the prior-art function directly: by specifying which governance properties a given anti-pattern destroys, Phase D3 provides the analytical basis for establishing that a given pattern of system behavior constitutes a governance failure under the CKS commitments, not merely a suboptimal configuration choice. This distinction is what prior-art documentation for defensive publication requires.

---

## 7. Relation to prior series

Phase D3 is the fourth formalized anti-pattern corpus in the CKS derivation series, following Phase A3 (Paper 1 anti-patterns), Phase B3 (Paper 2 intra-Self anti-patterns), and the anti-pattern content embedded in Phase A6 and B6 boundary-case notes. Phase D3 does not supersede those earlier corpora; it operates at the inter-Self scope that Papers 1 and 2's corpora do not cover.

Where Phase D3 anti-patterns inherit from Phase A3 or Phase B3 patterns — because Paper 3's inter-Self commitments inherit from Paper 1's cell-scope and Paper 2's intra-Self-scope commitments — the inheritance chain is identified in each note's governance commitment element. The inheritance tracking is what allows Phase D3 to avoid re-establishing prior-art for properties that earlier phases already cover: Phase D3 notes what is genuinely new at inter-Self scope and what is application of prior commitments at a larger scope.

The complete Series D corpus — Phases D0 through D6, plus Series CC cross-derivation and Series T trilogy-scope notes — produces the inter-Self and population-scope prior-art record that Papers 1 and 2's derivation series produced for their respective scopes.

---

## How to cite this note

Li, W. (2026). *Phase D3 Overview and FAI Anti-Pattern Taxonomy* (CKS Derivation Note D3.01, #576). May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
