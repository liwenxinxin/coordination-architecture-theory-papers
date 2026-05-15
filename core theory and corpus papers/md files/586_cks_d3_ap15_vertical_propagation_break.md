# AP-15: Vertical Propagation Break

**Derivation Note D3.11 — CKS Series D, Phase D3 (Anti-Pattern Formalizations)**
**Note #586 in the CKS Derivation Note Series**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

AP-15 names a failure mode in the vertical evolution hierarchy established by Paper 2: FAI-origin provenance is stripped from improvement proposals at some point during their upward propagation through the cell, aspect, and Self governance tiers, leaving Self-level governance unable to identify which proposals were informed by inter-Self learning. The break may occur at the cell-to-aspect transition, at the aspect-to-Self transition, or may never have been established at the originating cell level in the first place. Regardless of where in the chain the break occurs, the result is a governance information asymmetry: lower tiers retain awareness of the inter-Self origin; the highest-authority tier — Self-level governance — does not. This asymmetry violates Paper 1's path-retraceability commitment (A1.07) and Paper 2's vertical evolution provenance requirement (C1.21), and it undermines the integration architecture decisions that Self-level governance is responsible for making. The resolution is to configure the proposing substrate to carry FAI-origin attribution through every tier transition, so that proposals arriving at Self-level governance bear a complete, unbroken provenance chain traceable to their FAI-event source.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-15: Vertical Propagation Break

**Category:** Taxonomy Category 3 — Evolution Feed Failures. This category covers failure modes in which FAI-derived content enters a Self's home evolution machinery but the traceability or attribution requirements of that machinery are not satisfied. The Vertical Propagation Break is the third of four Category 3 anti-patterns (following AP-13 and AP-14). It is distinct from its neighbors in that it does not concern whether FAI-derived content enters the evolution feed at all, but whether the provenance annotation that identifies that content as FAI-derived survives the upward journey through the vertical hierarchy to the tier where governance decisions are made.

---

## 2. Description

Paper 2's vertical evolution hierarchy defines a three-tier propagation path for improvement proposals: cell-level action-feedback processes generate proposals grounded in operational action-layer records; aspect-level governance aggregates cell-level proposals and considers their cumulative implications; Self-level governance receives the aggregated stream and makes integration architecture decisions — decisions about how the Self's overall structure, its aspect configuration, and its governance rules should evolve. Each tier relies on what the tier below it sends upward.

When a Full Aspect Integration (FAI) event concludes and its outputs enter a participating Self's home evolution machinery, some of those outputs become action-layer records — substrate entries that capture what occurred during the inter-Self interaction. These FAI-origin records are then eligible to inform the same cell-level action-feedback processes that normally consume internally-generated action records. A cell may generate a directed-selection proposal on the basis of a FAI-origin action-layer record, just as it would on the basis of any other record. The structural mechanism is unchanged. What changes is the epistemic significance of the proposal: it is now an improvement signal that derives from inter-Self learning, not from the Self's home operational experience alone.

The Vertical Propagation Break occurs when FAI-origin provenance — the annotation identifying a proposal as having been informed by a FAI-origin action-layer record — is lost at some tier in the propagation chain. Three specific failure modes instantiate this anti-pattern:

**Form 1 — Never established.** The originating cell generates a proposal from FAI-origin action-layer records but does not mark the proposal as FAI-origin. The provenance is not stripped during propagation; it was never present to begin with. Every tier above the cell receives a proposal that is, from a provenance perspective, indistinguishable from one generated against home operational records.

**Form 2 — Stripped at cell-to-aspect transition.** The originating cell does carry FAI-origin provenance in its proposal. The aspect-level aggregation process, however, does not preserve this field when consolidating proposals from multiple cells. The aspect produces a consolidated proposal set that has lost the source-level attribution.

**Form 3 — Stripped at aspect-to-Self transition.** FAI-origin provenance survives the cell-to-aspect transition but is dropped when the aspect passes proposals upward to Self-level governance. This may occur because the Self-level receiving format does not include a FAI-origin field, because the tier-to-tier transfer logic does not copy the field, or because a summarization step that reduces proposal volume also reduces provenance specificity.

In all three forms, the observable result at Self level is the same: improvement proposals arrive without FAI-origin attribution. Self-level governance cannot determine, from the proposal stream itself, which proposals were informed by inter-Self learning.

---

## 3. Detection Criteria

Detection proceeds by backward tracing from Self-level governance through the vertical hierarchy:

- Improvement proposals present at Self-level governance that, when traced downward through the tier hierarchy, eventually reference cell-level action-layer records bearing FAI-origin markers — but lose FAI-origin attribution before reaching Self level. The presence of FAI-origin records at the bottom of the chain, combined with the absence of FAI-origin attribution at the top, localizes the break to one of the two tier transitions.

- Cell or aspect-level directed-selection events that reference FAI-origin action-layer records in their evidentiary basis, where the resulting proposals or DNA changes propagating upward do not carry corresponding FAI-origin attribution fields.

- Self-level governance that cannot distinguish, from the proposal stream, which directed-selection proposals were informed by inter-Self learning versus home operational experience alone. When this inability is confirmed — not merely suspected — it is the direct observable signature of the anti-pattern, regardless of which tier transition caused the break.

- Aspect-level aggregation outputs that consolidate proposals from cells known to have processed FAI-origin records, where the aggregated output contains no FAI-origin annotation. This targets Form 2 specifically.

---

## 4. Governance Commitment Violated

**Primary — Paper 1 A1.07 (Path retraceability).** The six provenance fields that A1.07 requires to be maintained must survive the vertical propagation chain. A proposal that carries a FAI-origin action-layer record as its evidentiary basis but does not carry FAI-origin provenance attribution has broken the path-retraceability commitment at the tier where the attribution was lost. The commitment is not satisfied by provenance maintenance at lower tiers alone; it requires that the chain remain unbroken from the action-layer source through to the governance tier that acts on the proposal.

**Secondary — Paper 2 vertical evolution governance (C1.21).** Proposals must carry their evidentiary chain as they propagate upward through tiers. The requirement exists because the governance value of a proposal depends on knowing its evidential basis. Stripping provenance at any tier-to-tier transition violates the traceability requirement at that transition, regardless of how complete the provenance was at the tier below.

**Operational reference — D2.57 (FAI and vertical evolution).** The vertical provenance chain is an accountability requirement. The chain must be complete from Self level back to the FAI event source. D2.57 establishes that FAI-origin provenance is not an optional annotation; it is a required field in any proposal that traces to a FAI-origin record.

---

## 5. Consequences

**Self-level governance makes integration architecture decisions without inter-Self context.** D2.56 establishes that Self-level governance is responsible for integration architecture decisions — decisions about how the Self's overall structure and governance rules should evolve. When the proposal stream that informs these decisions does not identify FAI-origin proposals as such, governance operates without knowing how much of the incoming improvement signal derives from what another Self has learned versus what this Self has learned on its own. The governance decisions may therefore fail to adequately weigh inter-Self context: the appropriate weight to give a proposal may differ depending on whether it reflects local operational evidence or evidence acquired across a perimeter boundary.

**Post-mortem review cannot assess inter-Self learning contribution.** D2.39 requires that post-mortem review can assess the sources of home governance improvement. When FAI-origin provenance is lost during upward propagation, the post-mortem cannot determine how much of an architectural improvement derived from inter-Self learning versus internal evolution. This gap is cumulative: the longer the anti-pattern persists, the less accountable the governance improvement record becomes.

**FAI relationship exit assessment is impaired.** D2.46 establishes that a Self exiting a FAI relationship should be able to assess how deeply that relationship's learning has propagated into its governance architecture. If vertical propagation break has been occurring throughout the relationship, this assessment is impossible: the Self cannot trace which of its current governance rules and DNA content evolved in response to inter-Self learning, because the proposals that drove those changes carried no FAI-origin attribution at the tier where governance acted on them.

**Regulatory audit cannot fully account for improvement sources.** D2.63 requires that regulatory audit can trace the sources of governance improvement. Vertical propagation break creates an audit gap at the tier where attribution was stripped. The audit may confirm that proposals were received and acted upon, but cannot confirm what sources informed those proposals.

---

## 6. Intra-Self Analog

Paper 2's vertical evolution requirement — that proposals carry their evidentiary basis as they propagate upward through tiers — is already an intra-Self requirement. A proposal that reaches Self-level governance without a traceable connection to its originating action-layer evidence violates this requirement at purely intra-Self scope, without any inter-Self dimension involved. The anti-pattern documented here is the extension of this same requirement to the inter-Self scope.

The extension introduces one additional dimension: the evidence in question is not merely the action-layer record but the identity of that record as FAI-origin — as having crossed from another Self's operational context into this Self's action layer at FAI dissolution. Intra-Self vertical traceability requires carrying the action-layer record citation upward. Inter-Self vertical traceability requires carrying that citation plus the FAI-origin attribution that identifies the record's organizational provenance.

The four-link cross-organizational authorization chain established by D2.67 defines the full traceability requirement at inter-Self scope. Vertical propagation break is a failure to maintain any link in that chain above the cell tier. The intra-Self analog is a failure to maintain the chain within the home vertical hierarchy; the inter-Self version is the same failure at a scope that now includes an inter-Self source.

---

## 7. Resolution

D2.57 establishes the vertical provenance chain requirement: FAI-origin provenance must be maintained through each tier of vertical propagation. The practical resolution requires that the vertical evolution process be configured to carry FAI-origin attribution through tier transitions, rather than treating such attribution as an optional annotation that may or may not survive aggregation or summarization steps.

Three configuration requirements follow from D2.57, one at each tier:

**At cell level.** Cell-level action-feedback processes that generate proposals from action-layer records must check whether those records bear FAI-origin markers and, if so, include FAI-origin provenance in the resulting proposals. This is the point where Forms 1 and 2 originate; if FAI-origin attribution is not established at the cell level, no downstream configuration can recover it.

**At aspect level.** Aspect-level aggregation of cell-level proposals must preserve FAI-origin markers through consolidation. When an aspect produces an aggregated proposal set, FAI-origin attribution from contributing cell-level proposals must be carried forward — either per-proposal or, at minimum, as an aspect-level flag indicating that some proposals in the set derive from FAI-origin records.

**At Self level.** The format in which proposals arrive at Self-level governance must include a FAI-origin field, and the tier-to-tier transfer logic from aspect to Self must populate it. Self-level governance receives proposals with complete provenance chains traceable to FAI event sources.

The practical implementation is D2.59 Config A: a proposing substrate configuration that explicitly tracks and surfaces FAI-origin proposals at every tier. Config A is distinguished from the default proposing substrate configuration (Config B) by the addition of FAI-origin attribution fields that are populated at cell level and preserved through tier transitions. Under Config A, the proposing substrate is configured to treat FAI-origin attribution as a first-class provenance field rather than as a derived annotation that can be dropped when proposal volume is reduced or format is changed.

Config A is the governing configuration in any deployment where a Self participates in FAI events. Its absence — operating under a configuration that does not track FAI-origin attribution — is the structural precondition for the Vertical Propagation Break. Detection of the anti-pattern is therefore also a signal that Config A has not been established, and the remediation is to configure the proposing substrate accordingly before the next vertical evolution cycle processes FAI-origin action-layer records.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-15: Vertical Propagation Break. CKS Derivation Note D3.11 (#586).* May 15, 2026. ORCID: 0009-0004-8065-3235.
