# Disambiguating "Action-Feedback" Across the Trilogy

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate the precise meanings of "action-feedback" as that term and its derivatives are used across the trilogy, so that downstream work can adopt or argue against specific usages without conflating distinct architectural concepts.

## Abstract

The term "action-feedback" and its derivatives — "action layer," "action-feedback mechanism," "action-feedback locus," "action-feedback ingestion" — appear across all three papers in the CKS trilogy with related but distinct meanings. They refer to: the action layer as a substrate repository of operational records (all three papers); the action-feedback mechanism as a complete processing pipeline from stored records to governance proposals (Paper 2); the action-feedback locus as the entry point through which inter-Self event outcomes reach the home action layer at dissolution (Paper 3); and the ingestion governance requirements that apply at that entry point (Paper 3). The critical disambiguation is between locus and mechanism. The locus is a delivery pathway; the mechanism is what processes the delivered content. They are sequential, not competing. Paper 3 does not replace or modify Paper 2's action-feedback mechanism; it adds a governed entry point through which a new category of content — outcomes from inter-Self coordination events — reaches the action layer from which the existing mechanism continues to operate unchanged. This note states the four scope-specific meanings, names the critical disambiguation, identifies the action layer as the stable architectural object across all three papers, and identifies ingestion governance as the genuinely new Paper 3 addition.

## 1. Why this disambiguation is needed

The word "action" compounds with "feedback" across the trilogy in four distinct constructions: the action layer itself, the action-feedback mechanism, the action-feedback locus, and action-feedback ingestion. All four are architecturally coherent. All four are related. They operate at different scopes and name different things, however, and conflating them produces two damaging misreadings.

The first misreading treats the action-feedback locus (Paper 3) as a replacement for or elaboration of the action-feedback mechanism (Paper 2). Under this reading, Paper 3 redesigns the mechanism — changes how operational records become governance proposals, or adds new processing steps to the pipeline. This misreading obscures that Paper 3's contribution at the action-feedback level is narrowly scoped to the entry point: where a new category of content comes from at the inter-Self boundary, and what governance requirements apply when that content crosses into the home action layer. The mechanism itself is inherited unchanged.

The second misreading treats the action layer as scope-specific — as if Paper 2's action layer and Paper 3's action layer name different objects with different properties. Under this reading, Paper 3 introduces a new kind of action layer for inter-Self contexts. This misreading obscures that the action layer is the same architectural object throughout the trilogy: the substrate repository of operational records within every cell, operating under the same governance commitments at every scope. What changes is the source of content that can enter the layer, not the layer's definition or governance.

Naming the four constructions precisely and stating the relationships among them forecloses both misreadings.

## 2. The action layer: stable substrate across all three papers

The action layer is one of two named substrate layers within every cell. Paper 2 (Li, 2026b) names and formalizes it as the repository of the cell's operational records — the accumulated execution history of what the cell has done, stored as substrate content under the same governance commitments that apply to all substrate content. The companion DNA layer carries behavioral specifications; the action layer carries operational history.

Paper 1 (Li, 2026a) does not use the term "action layer" but establishes the substrate structure from which Paper 2 derives it. Paper 1's substrate is a persistent, human-governed coordination medium at cell scope; all authoritative state lives in it; LLM operations over it produce governance-relevant outputs. The action layer is Paper 2's formalization of the substrate at the operational-records dimension within a cell.

Paper 3 (Li, 2026c) does not redefine the action layer. When a participating deployment contributes an aspect to the shared substrate at an inter-Self coordination event, the aspect's action-layer content is part of what exchanges across the shared substrate. When the event dissolves and content propagates back to each participating deployment's home substrate, the action layer that receives FAI-origin content is the same layer Paper 2 defines: the substrate repository of operational records, governed by human authority over what enters it, accessible to LLM reads under orchestration rules.

The action layer's governance relationship is unchanged across the trilogy. Human authority governs what enters it. The LLM mediates reads from it to produce governance-relevant outputs. No aspect of that relationship is modified at inter-Self scope. The only thing that changes is the source of content that can enter the layer: at Paper 2 scope, content originates from the home deployment's own operational records; at Paper 3 scope, content may also originate from inter-Self coordination events, subject to the ingestion governance requirements Paper 3 introduces.

## 3. The action-feedback mechanism: Paper 2's complete processing pipeline

Paper 2 formalizes the action-feedback mechanism as one of three evolution mechanisms operating within a deployment's home perimeter. The mechanism runs a complete pipeline. The proposing substrate reads the action layer and generates improvement proposals from the operational evidence it finds there. Those proposals flow to home governance for review. If a proposal is authorized, a directed selection event incorporates the authorized improvement into the home deployment's behavioral specifications. The complete pipeline is: action-layer content → LLM-mediated reads by the proposing substrate → improvement proposals → governance review → directed selection if authorized.

The governance shape for this mechanism is proposal-and-acceptance machinery: the LLM proposes; humans authorize or decline. No proposal reaches the DNA layer or modifies the deployment's operational configuration without human authorization. This authority structure is established in Paper 2 and derives directly from Paper 1's authority-versus-labor distinction applied at the evolution level.

Paper 3 does not modify this mechanism. The action-feedback mechanism operates at intra-Self scope under home governance authority, and its operation is unchanged at Paper 3 scope. After dissolution of an inter-Self coordination event, after FAI-origin content has entered the action layer through the action-feedback locus under ingestion governance, the proposing substrate reads the action layer — including whatever FAI-origin content has been ingested — and generates improvement proposals exactly as Paper 2 specifies. The mechanism receives new input content; it does not receive new operational logic.

## 4. The action-feedback locus: Paper 3's governed entry point

Paper 3 introduces the four-locus evolution-feed mechanism at the dissolution boundary of inter-Self coordination events. The four loci are the entry points through which event outcomes enter each participating deployment's home evolution machinery when the event dissolves and the shared substrate closes. The action-feedback locus is the first of the four: the entry point through which event outcomes enter the home action layer.

The locus is not the mechanism. The locus is the delivery pathway — the governed channel through which FAI-origin content arrives at the action layer. The mechanism is what happens after content arrives: the proposing substrate reads the action layer, including any FAI-origin content that has entered through the locus, and generates proposals for home governance.

The relationship between locus and mechanism is sequential. The locus operates at the dissolution boundary, at the moment when the shared substrate closes and content propagates to home substrates. The mechanism operates within the home perimeter, after dissolution, on the content the action layer holds. An implementation that treats the locus as a redesign of the mechanism would look for the action-feedback processing pipeline at the inter-Self boundary — inside the shared substrate, during the event, as part of the coordination itself. Neither paper commits to that. The mechanism's location and governance are fixed at home; the locus governs how FAI-origin content reaches the mechanism's input.

This disambiguation matters most when reading Paper 3's four-locus architecture. The four loci are entry points, not mechanisms. Each locus routes FAI-origin content from the dissolving shared substrate to the appropriate home evolution mechanism. The action-feedback locus routes to Paper 2's action-feedback mechanism. The DNA evolution locus routes to Paper 2's directed selection mechanism operating on home DNA. Instinct evolution takes no FAI input by architectural commitment — the instinct layer does not exchange across inter-Self coordination events. The layer-routing rule is: the content's layer determines which home evolution mechanism receives it. That rule operates at the locus level, before the mechanisms run.

## 5. Ingestion governance: the genuinely new Paper 3 requirement

Paper 3 introduces ingestion governance as the governance requirements that apply when FAI-origin content enters the home action layer through the action-feedback locus. Paper 2's action-feedback mechanism is inherited unchanged; the ingestion governance requirements for the locus are not.

The ingestion governance requirements for action-feedback content include three components. First, provenance requirements: FAI-origin content entering the home action layer carries provenance identifying its inter-Self source, the coordination event in which it originated, and any conflict annotations it carries from the shared substrate's conflict-handling during the event. This provenance is substrate content in the home action layer alongside the ingested records; it is not discarded at the perimeter boundary. Second, authorization requirements: home governance authorizes the ingestion of FAI-origin content through the locus. Ingestion does not occur by default. The configuration of what each home perimeter accepts from a given event is itself substrate content under home governance authority, configured before the event begins or updated by home governance during the event. Third, ingestion record requirements: the ingestion event itself is recorded as substrate content with appropriate metadata — what was ingested, from which event, under which authorization, at what time.

These requirements are new at Paper 3 scope because the intra-Self action-feedback mechanism in Paper 2 does not face the problem they address. In Paper 2, all content entering the action layer originates from the home deployment's own operational records, within the home governance perimeter. Cross-perimeter provenance, inter-Self authorization, and ingestion records are not at issue. Paper 3 adds them because FAI-origin content crosses home governance perimeters, and the trilogy's governance commitments — human authority over what enters the substrate; provenance as a first-class property of substrate content — apply specifically and necessarily at that crossing point.

## 6. Prior-art closure and operational test

The four constructions together constitute the complete action-feedback concept as it appears across the trilogy. Each construction covers a distinct aspect of the same underlying architectural pattern: the action layer as storage, the action-feedback mechanism as the processing pipeline that reads from that storage, the action-feedback locus as the inter-Self delivery pathway to that storage, and ingestion governance as the requirements for governed delivery. A system that implements any of these four constructions is instantiating the CKS action-feedback concept at the appropriate scope. This note's prior-art coverage forecloses adversarial claims of novelty for any of the four, whether presented individually or as a combined architecture.

A system instantiates the complete CKS action-feedback concept at Paper 3 scope if and only if all of the following hold:

1. The action layer is a substrate repository of operational records within every cell, governed by human authority over what enters it, accessible to LLM reads under orchestration rules. The layer's definition and governance are not modified at inter-Self scope.
2. The action-feedback mechanism operates at home perimeter: the proposing substrate reads the action layer and generates improvement proposals for home governance to authorize or decline; no proposal modifies the deployment's operation without governance authorization.
3. The action-feedback locus is the entry point through which inter-Self event outcomes reach the home action layer at dissolution; it is a delivery pathway and not the mechanism; it precedes the mechanism in the processing sequence.
4. FAI-origin content entering through the action-feedback locus carries provenance identifying its inter-Self source; home governance explicitly authorizes the ingestion; the ingestion event is recorded as substrate content.
5. No content originating from an inter-Self coordination event may be committed to the home action layer through the action-feedback locus without home governance authorization; that authorization is a human-held right, not an architectural default.

A system that satisfies (1) and (2) but not (3) implements the Paper 2 action-feedback mechanism without the Paper 3 inter-Self extension. A system that satisfies (3) but not (4) implements the locus without the ingestion governance requirements Paper 3 adds. A system that conflates (3) with (2) — treating the locus as if it were the mechanism, or locating the mechanism at the inter-Self boundary rather than at home — has misread the architecture at the critical disambiguation point this note addresses.

## 7. Conclusion

"Action-feedback" in the CKS trilogy names four distinct but related architectural constructions. The action layer is the stable substrate repository of operational records at every scope. The action-feedback mechanism is Paper 2's complete processing pipeline from action-layer content to governance proposals under home authority. The action-feedback locus is Paper 3's governed entry point through which inter-Self event outcomes reach the action layer at dissolution. Ingestion governance is Paper 3's requirement set for that entry: provenance, authorization, and ingestion record. The locus delivers; the mechanism processes. They are sequential, not competing. Paper 3 does not redesign Paper 2's mechanism; it adds a governed entry point through which a new category of content can reach the layer from which the existing mechanism continues to operate.

Subsequent work that adopts, extends, or argues against these concepts should use the four-way distinction formalized here. Work that uses "action-feedback" without specifying which construction is under discussion risks conflating the delivery pathway with the processing pipeline — the central disambiguation this note addresses.

---

## Source papers

Li, W. (2026a). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Disambiguating "Action-Feedback" Across the Trilogy.* May 15, 2026. ORCID: 0009-0004-8065-3235.
