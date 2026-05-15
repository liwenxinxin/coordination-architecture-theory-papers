# FAI and the Vertical Evolution Mechanism

**Series:** CKS Derivation Notes — Phase D2, Note D2.57 (#552)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 2 established vertical evolution as the mechanism through which operational insights at the cell level propagate upward through aspects to the Self level, informing governance improvement at each tier. That mechanism operated within one Self's home perimeter, informed solely by one Self's internal operational experience. This note formalizes the relationship between Paper 3's Full Aspect Integration (FAI) events and the Paper 2 vertical evolution mechanism. FAI outputs — action-layer records ingested at the home perimeter following FAI dissolution — enter the vertical evolution pathway as action-layer content, where the existing mechanism processes them without modification. This creates a scope extension: vertical evolution becomes informed by inter-Self coordination experience, not only by one Self's internal experience. The note formalizes three vertical propagation scenarios corresponding to where FAI-origin records land in the home action layer (cell-level, aspect-level, direct Self-level), states FAI's role as a vertical evolution amplifier, specifies the provenance requirements that apply through every tier of vertical propagation, and names the anti-pattern in which FAI-origin provenance is removed from propagating proposals — breaking the accountability chain for inter-Self learning that has reached Self-level governance.

---

## 1. Position and derivation basis

D2.57 is a cross-paper operational synthesis note. Its two parent commitments sit in different papers.

The first parent is Paper 2's vertical evolution mechanism (C1.22 / §7.4). Paper 2 established that evolution in a CKS Self operates on two axes. Horizontal evolution refines content within existing structure — DNA, action, and instinct evolving within the current cell, aspect, and Self composition. Vertical evolution reorganizes structure itself — composition relationships between levels change through governed reorganization decisions. Both axes operate through Paper 2's three evolution mechanisms. Vertical evolution propagates insights upward: cell-level proposals aggregate into aspect-level proposals; aspect-level proposals aggregate into Self-level proposals; directed selection at the Self level then acts on whatever reached it from below. The structural arrangement is itself substrate content humans govern, so vertical evolution is a substrate-edit operation at every tier. Before FAI enters the picture, what informs this pathway is limited to one Self's accumulated operational experience.

The second parent is Paper 3's FAI action-feedback ingestion as established in D2.10. When a FAI event dissolves, each participating Self's home perimeter receives FAI-derived content through governance-configured ingestion. The layer-routing rule determines what reaches which evolution mechanism: action-layer content reaches action-feedback evolution operating within home action layers; DNA-layer content reaches DNA evolution; instinct evolution takes no FAI input. These FAI-origin records, once in the home action layer, are substrate content — specifically, action-layer content — that the home action-feedback mechanism processes identically to home-generated records. No architectural modification is required; FAI outputs are inputs to an existing mechanism.

D2.57 formalizes what follows from combining these two parent commitments: FAI-origin action-layer records participate in the vertical evolution pathway by the same path that any action-layer content participates. The amplification is structural, not designed. It is a consequence of the ingestion architecture, not an extension added for this purpose.

---

## 2. How FAI outputs enter the vertical evolution pathway

The pathway from FAI event to vertical evolution proceeds through several steps, each of which is already established in the prior derivation record.

At FAI dissolution, the shared substrate closes. Each participating Self's home governance determines what to ingest. Action-layer content from the event — recorded coordination work, executed task instances, conflict-carry-through annotations from FAI conflict handling, and FAI event summaries — enters the home action layer as FAI-origin records. These records carry their FAI-origin provenance under the governance-configured provenance carry-over depth the home authority specified. The records are now action-layer content inside the home substrate.

From this point, Paper 2's action-feedback evolution mechanism treats them as it treats any action-layer content. Proposing substrates evaluate action-layer records and generate improvement proposals when the evidence supports them. Proposals travel upward through the vertical hierarchy: cell-level proposals aggregate into aspect-level proposals; aspect-level proposals aggregate into Self-level proposals. At each tier, governance evaluates and acts on what arrives. Directed selection events at the Self level may follow from proposals whose originating evidence included FAI-origin records.

The critical architectural point is that no step in this pathway is FAI-specific. The action-feedback mechanism does not distinguish FAI-origin records from home-origin records during proposal generation. The vertical propagation pathway does not distinguish FAI-informed proposals from home-informed proposals during aggregation. What is FAI-specific is only the provenance the records carry — their FAI-origin attribution, the FAI event identifier, and the inter-Self coordination context. That provenance travels with the records and with the proposals they generate; it does not modify the mechanism through which those proposals travel.

---

## 3. Three vertical propagation scenarios

Where FAI-origin records land in the home action layer determines which scenario applies. The scenario is not a design choice made at FAI time; it follows from which aspects participated in the FAI event and how their action layers are structured within the home substrate.

**Scenario 1 — Cell-level FAI insights propagate upward.** FAI-origin records land in individual cells' action layers within the aspects that contributed to the FAI event. Cell-level proposing substrates evaluate these records and generate cell-level improvement proposals. Cell proposals aggregate into aspect-level proposals in the normal way. Aspect proposals aggregate into Self-level proposals in the normal way. FAI learning that originated at the cell level of a coordination task reaches Self-level governance through the full vertical propagation chain: cell → aspect → Self. This is the longest path, passing through every tier. It is also the most common scenario, because most FAI coordination work executes at the cell level within the contributing aspects.

**Scenario 2 — Aspect-level FAI insights propagate upward.** FAI-origin records land at the aspect action layer rather than at individual cell action layers. This occurs when what the FAI event produces is aspect-scoped: conflict carry-through annotations that characterize the boundary between two aspects' coordination approaches, FAI event summaries that capture inter-aspect dynamics, or records whose content addresses how an entire aspect's contribution related to the other Self's contribution. Aspect-level proposing substrates evaluate these records and generate aspect-level proposals directly. These proposals propagate to the Self level through standard vertical evolution without needing to aggregate upward from cells first. The path is shorter — aspect → Self — but the mechanism is identical.

**Scenario 3 — Direct Self-level FAI insights.** FAI conflict patterns that reveal Self-level integration issues enter the Self-level action layer directly as FAI-origin records. This occurs when the FAI event produces evidence about how the participating Self's governance structure as a whole relates to the other Self's governance structure — evidence that is not reducible to any single aspect or cell but characterizes the Self as a unit. These records do not need to propagate through the vertical hierarchy; they enter the highest governance tier directly as action-layer content at Self scope. Self-level directed selection events may follow without the upward aggregation steps that Scenarios 1 and 2 require.

All three scenarios use the same underlying vertical propagation mechanism. What varies is the entry point: Scenario 1 enters at cell level and traverses the full hierarchy; Scenario 2 enters at aspect level and traverses one tier; Scenario 3 enters at Self level and does not traverse upward at all. The scenario is determined by the structure of the FAI event and the home action layer, not by any FAI-specific routing decision.

---

## 4. FAI as vertical evolution amplifier

The scope extension that FAI creates for vertical evolution is the central architectural contribution this note formalizes.

Before FAI, vertical evolution within a Self was informed by that Self's internal operational experience. The cell-level records that generated proposals, the aspect-level records that generated proposals, the Self-level records that generated proposals — all originated within the home perimeter, from tasks the home cells executed, conflicts the home conflict-handling infrastructure resolved, and coordination patterns the home orchestration rules produced. The vertical pathway was rich, but its source was bounded: one Self's history.

After FAI, vertical evolution is informed by inter-Self coordination experience. FAI-origin action-layer records enter the home vertical pathway carrying evidence about how the home Self's coordination approaches interacted with another Self's coordination approaches under joint governance. This is a category of evidence the home Self cannot generate internally. No internal task produces records about how the home Self's conflict-handling compares to a peer Self's conflict-handling under a shared substrate. No internal cell execution produces records about how the home Self's aspect contribution was received, integrated, and processed by another governance structure. FAI events are the only source of this class of evidence.

The amplification is available without architectural changes to the vertical evolution mechanism. FAI outputs are action-layer content. The existing mechanism processes action-layer content. No new mechanism is required; no modification to the vertical propagation pathway is required. The amplification is a structural consequence of the ingestion architecture: because FAI outputs enter the action layer, and because the action layer feeds the vertical evolution pathway, FAI learning reaches Self-level governance through the same channel that all action-layer learning uses.

This is the inter-Self scope extension of Paper 2's vertical evolution mechanism. A Self operating in isolation evolves on the basis of its own operational history. A Self participating in FAI events evolves on the basis of its own operational history plus its inter-Self coordination history. The second category of evidence extends the scope of what vertical evolution can act on, and the extension compounds over time as FAI events accumulate.

---

## 5. Provenance in vertical propagation

FAI-origin records that propagate upward through vertical evolution carry their FAI-origin provenance through each tier. The six provenance metadata fields established in Paper 1 (A1.07) — writer attribution, timestamp, antecedent reference, rule reference, rationale where required, and contradiction relationship where applicable — must be present on FAI-origin records as they enter the home action layer, and must be preserved as those records generate proposals that move upward through the vertical hierarchy.

The accountability requirement is directional. At the moment a Self-level directed selection event occurs — a governance decision about how the Self operates, informed partly by proposals that originated in FAI-origin action-layer records — the governance chain must be traceable in the following direction: from the Self-level event backward to the proposals that informed it, from those proposals backward to the aspect-level aggregation that produced them, from that aggregation backward to the cell-level or aspect-level action-layer records that generated the original proposals, and from those records backward to the FAI event that produced them. An observer following this chain should be able to reach the FAI event source: the participating Self whose coordination work generated the evidence, the specific FAI event identifier, and the inter-Self coordination context that made the record relevant.

This full vertical provenance chain is the accountability trail for inter-Self learning that has reached Self-level governance. Its presence is what makes the governance decision auditable: not merely auditable as a decision with substrate evidence, but auditable as a decision whose inter-Self learning origin is identifiable. The governance authority that approved the directed selection event at the Self level can, if queried, demonstrate that the proposal it acted on was informed by FAI experience from a specific inter-Self event under specific joint governance.

Provenance preservation at each tier is a substrate content requirement, not a process reminder. Every proposal generated from FAI-origin records must carry an antecedent reference to those records. Every aggregated aspect-level proposal must carry antecedent references to the cell-level proposals it aggregated. Every Self-level proposal must carry antecedent references to the aspect-level proposals that informed it. The six fields travel with the content through the vertical hierarchy because provenance is a property of substrate content, and the substrate content at every tier is what the chain is made of.

---

## 6. Anti-pattern: Vertical propagation break

The anti-pattern in this domain is the vertical propagation break: FAI-origin action-layer records trigger cell-level or aspect-level proposals, but the FAI-origin provenance is stripped from those proposals before they propagate upward through the vertical hierarchy.

A vertical propagation break produces proposals that reach higher-tier governance carrying the evolutionary signal from FAI experience — the content improvement, the conflict resolution, the schema refinement — but not the FAI origin of that signal. Higher-tier governance receives proposals informed by inter-Self learning but cannot trace the inter-Self origin. The directed selection events that follow are informed by FAI experience that is, from the governance record's perspective, invisible: the proposals look like home-generated proposals because their provenance no longer identifies the FAI event that produced their evidentiary basis.

This breaks the accountability chain in a specific way. The problem is not that the proposals are wrong or that the resulting directed selection events produce bad outcomes. The proposals may be excellent and the outcomes may be improvements. The problem is that the governance authority approving the Self-level change cannot account for the full provenance of what it is approving. If the FAI event's inter-Self coordination context is relevant to evaluating the proposal — if, for example, the evidence comes from an FAI event with a particular conflict-handling history, or from a contributing Self whose governance structure differs materially from the home Self's — that context is lost when provenance is stripped. The governance decision proceeds without the information it would need to evaluate the proposal's inter-Self origin.

The operational test for the vertical propagation break is straightforward: for any Self-level directed selection event that is claimed to have been informed by FAI evolution, can an observer trace the full vertical provenance chain from the Self-level event backward through the aggregation tiers to a specific FAI-origin action-layer record in the home substrate, and from that record to the specific FAI event that produced it? If yes, the vertical provenance chain is intact. If the chain terminates — if a proposal exists whose antecedent references do not reach an action-layer record with FAI-origin attribution, or if the FAI-origin attribution identifies no specific FAI event — the vertical propagation break has occurred at that point in the chain.

---

## 7. Operational test

A deployment instantiates the D2.57 specification for FAI-informed vertical evolution if and only if all of the following are true for any FAI-origin record that enters the home action layer following a FAI dissolution event:

First, the record carries the six provenance metadata fields from Paper 1 A1.07, with the FAI event identifier present as part of the writer attribution or antecedent reference fields, and with the provenance depth matching the governance-configured carry-over depth that home authority specified at ingestion.

Second, when proposing substrates evaluate the record and generate improvement proposals, those proposals carry antecedent references to the FAI-origin record. The proposals do not strip or summarize away the FAI-origin attribution in the antecedent reference field.

Third, as proposals propagate upward through the vertical hierarchy — from cell level to aspect level, from aspect level to Self level — each aggregation step preserves the antecedent references of the contributing proposals. An aggregated aspect-level proposal can be traced back to the cell-level proposals it aggregated; a Self-level proposal can be traced back to the aspect-level proposals it aggregated.

Fourth, for any Self-level directed selection event informed by FAI evolution, an observer can follow the vertical provenance chain from the Self-level event backward through every aggregation tier to a specific FAI-origin action-layer record in the home substrate, and from that record to the specific FAI event identifier that produced it. The chain does not terminate before reaching the FAI event source.

A deployment in which FAI-origin provenance is present on ingested records but absent on proposals generated from those records fails the second condition. A deployment in which proposals carry FAI-origin antecedent references but aggregation steps consolidate those references into summary references that no longer identify individual FAI-origin records fails the third condition. A deployment in which Self-level directed selection events reference Self-level proposals whose backward chain terminates before reaching a FAI-origin record fails the fourth condition. Each failure is a vertical propagation break at a different tier of the hierarchy.

---

## Summary

D2.57 establishes the following:

FAI-origin action-layer records enter the vertical evolution pathway at the tier corresponding to where they land in the home action layer (cell-level, aspect-level, or Self-level), and are processed by the existing vertical propagation mechanism without modification. Three scenarios follow from entry-point position: cell-level entry traverses the full hierarchy; aspect-level entry traverses one tier; direct Self-level entry requires no upward traversal. All three scenarios use the same mechanism.

FAI extends the scope of what informs vertical evolution from one Self's internal operational experience to inter-Self coordination experience. This amplification is a structural consequence of action-layer ingestion architecture; no modifications to the vertical evolution mechanism are required or implied.

The six provenance metadata fields established in Paper 1 must travel intact through every tier of vertical propagation for any FAI-origin record entering the pathway. An observer must be able to trace the full vertical provenance chain from any Self-level directed selection event back to the FAI event source that produced the originating evidence.

Removing FAI-origin provenance from proposals before they propagate upward through the vertical hierarchy — the vertical propagation break — is the named anti-pattern. It produces governance decisions informed by inter-Self learning whose inter-Self origin cannot be accounted for within the governance record.
