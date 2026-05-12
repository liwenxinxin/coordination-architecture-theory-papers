# Bidirectional Evolution Integrating Frame: Decomposing B1.16 by Formalizing What Makes CKS Evolution Bidirectional — Horizontal Evolution (Within-Level Peer Influence Across Cells, Aspects, and Selves) and Vertical Evolution (Cross-Level Propagation Both Upward and Downward Through the Three-Level Structure), on Operational Timescales

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The second CKS theory paper (Li, April 2026) establishes bidirectional evolution as a property of the three-level CKS architecture: evolution operates not in a single direction but in two — horizontally within structural levels and vertically across structural levels. This note formalizes the bidirectional evolution integrating frame as the architectural specification that names and bounds both directions. Horizontal evolution is within-level peer influence: improvements to one cell, aspect, or Self inform peer entities at the same structural level through governed propagation. Vertical evolution is cross-level propagation in both directions: upward, as cell-level improvements inform aspect-level evolution and aspect-level improvements inform Self-level evolution; downward, as Self-level changes affect cell behavior through the expression mechanism. Both directions operate on operational timescales — during deployment operation, not only at design time. Neither direction is automatic; both require governance decisions at the origin level and, for vertical propagation, at the destination level as well. The note articulates what makes this frame architecturally distinctive, identifies the inherited Paper 1 commitments it carries, states its operational implications, and specifies its limits. This is derivation note B2.79 in Phase B2 of Series B, opening the five-note decomposition of B1.16 (B2.79–B2.83).

---

## 1. Why the bidirectional evolution integrating frame needs to be formalized

B1.16 establishes that CKS evolution is bidirectional. The Series B decomposition has spent B2.47–B2.72 formalizing the three-level structure and multi-level evolution properties, and B2.73–B2.78 decomposing the three evolution mechanisms (mutation, directed selection, action-feedback). B2.79 opens the B1.16 decomposition by formalizing what *bidirectional* means as an architectural property: that evolution can and does move in two directions — horizontally within structural levels and vertically across structural levels.

Formalizing this frame as a standalone derivation note matters for two related reasons.

The first is architectural precision. Bidirectionality is not a consequence of having three structural levels; many architectures with hierarchical structure permit evolution at only one level or in only one direction. Bidirectionality is a deliberate architectural specification — the claim that the three-level structure supports peer-level influence and cross-level propagation in both upward and downward directions. That specification requires articulation before the specific directions can be decomposed in B2.80 (horizontal evolution) and B2.81 (vertical evolution).

The second is prior-art posture. Conventional AI architectures evolve primarily through model retraining and redeployment: a model improves, a new version is deployed, prior behavior is superseded. Within-level peer influence and cross-level propagation as *architectural properties* are not features of such architectures. Formalizing the bidirectional evolution integrating frame places on record the specific architectural commitment that distinguishes CKS evolution from unidirectional retraining-and-redeployment evolution, in the seventy-ninth position in the Phase B2 derivation chain, before individual directions are treated in detail.

---

## 2. The architectural frame precisely stated

The bidirectional evolution integrating frame specifies that CKS evolution operates along two directional axes within the three-level structure.

**Horizontal evolution** is within-level peer influence. Changes at one entity within a structural level influence peer entities at the same level. Three within-level domains are specified:

At the *cell level*, improvements to one cell's DNA may be applied to peer cells with similar functions. A cell that matures through operational experience — developing tighter orchestration rules, sharper conflict-handling, more efficient action patterns — may be used as a template for peer cells of the same type. Directed selection improvements applied to one cell's DNA may be extended to structurally similar cells. Mating between cells per B1.10 generates peer cells at the cell level, propagating improvements horizontally through lineage.

At the *aspect level*, improvements to one aspect's coordination rules may inform peer aspects serving similar purposes. Aspects that evolve tighter cell-composition rules or more effective purpose-alignment may inform parallel aspects through governed propagation. Directed selection improvements to one aspect's orchestration patterns may be applied to peer aspects with related structures.

At the *Self level*, improvements to one Self's integration architecture — how it holds aspects together, how it manages cross-aspect coordination, how it configures its instinct/reasoning boundary per B2.23 — may inform peer Selves at the same level.

**Vertical evolution** is cross-level propagation in two directions:

*Upward vertical evolution* moves from lower levels to higher levels. Cell-level evolution propagates to the aspect level: improvements to cell DNA may warrant evolution of the aspect-level coordination rules that govern those cells (per B2.16); cell behavioral improvements inform aspect purpose alignment. Aspect-level evolution propagates to the Self level: improvements to aspect-level orchestration may warrant evolution of the Self-level integration architecture (per B2.21); aspect improvements inform how the Self holds its aspects as a coherent whole.

*Downward vertical evolution* moves from higher levels to lower levels. Self-level evolution affects cell behavior: Self-level DNA changes — including integration architecture changes, instinct/reasoning boundary configuration per B2.23, and cross-aspect coordination rules — affect cell operation through the expression mechanism per B2.30. The expression mechanism is the downward channel: which DNA-layer substrates activate for a given cell goal is governed by the harness substrate, itself governed content. When Self-level DNA changes, the expression configuration changes, and cell behavior changes accordingly without requiring cell-level DNA modification. Aspect-level coordination rule changes affect cell participation patterns — which cells are active in which arrangements — producing behavioral changes at cell level driven by aspect-level evolution.

**Operational timescales.** Both directions operate on operational timescales — during deployment operation, not only at design time. This is architecturally significant. It means deployed CKS architectures evolve while in service: cells improve through operational experience during deployment; aspects restructure in response to operational patterns; Selves integrate new capabilities while serving users. The architecture is not a static artifact deployed once and replaced periodically; it is an evolving structure that changes direction under governance during operation.

**Governance required.** Neither direction is automatic. Horizontal propagation — applying improvements from one cell, aspect, or Self to peers — requires governance decisions to authorize the propagation. An improvement demonstrated in one cell does not automatically transfer to peer cells; humans holding authority over the peer cells must authorize the transfer. Vertical propagation — upward from cell improvements to aspect evolution, or downward from Self-level DNA changes to cell behavior — requires governance decisions at both origin and destination levels. When vertical evolution changes authority distribution, the A6.06 authority distribution change boundary applies, requiring boundary-level governance handling.

---

## 3. What makes this frame architecturally distinctive

The bidirectional evolution integrating frame is distinctive against conventional AI evolution architectures on three axes.

**Directionality as architectural specification.** Conventional AI architectures typically evolve through model retraining and redeployment. The trajectory is effectively unidirectional: models improve through upstream retraining, improved versions are deployed, prior behavior is superseded. There is no within-level peer influence specified as an architectural property — one deployed model does not influence a peer deployed model through the architecture — and no cross-level propagation architecture, because the unidirectional architecture typically has one functional level rather than three. CKS bidirectional evolution is architecturally specified: the architecture commits to both within-level peer influence and cross-level propagation as properties of how the three-level structure evolves.

**Coherent whole-architecture evolution.** Bidirectionality is what enables CKS to evolve as a coherent architectural whole rather than as isolated components improving independently. Without horizontal evolution, cell improvements would not propagate to peer cells; the architecture would accumulate divergence rather than coherence. Without vertical evolution, cell improvements would not inform aspect and Self architecture, and Self-level changes would not propagate to cell behavior; the levels would drift into incoherence. Horizontal evolution enables organizational learning — improvements demonstrated at one cell spread to similar cells through governed propagation. Vertical evolution enables architectural coherence — improvement signals move upward through levels, and architectural configuration signals move downward through expression.

**A property of how mechanisms operate, not a fourth mechanism.** Bidirectional evolution is not an independent mechanism alongside mutation, directed selection, and action-feedback. All three mechanisms can produce bidirectional evolution. Mutation-like instinct evolution that sharpens a cell's capability may warrant horizontal propagation to peer cells and vertical propagation to aspect-level coordination rules. Directed selection improvements to one cell's DNA may be applied horizontally to peer cells. Action-feedback loop improvements may propagate vertically from the cell level to the aspect level. Bidirectionality is the property that characterizes how these mechanisms operate within the three-level structure.

---

## 4. The biological analog as conceptual scaffold

Paper 2 uses biological evolution as a conceptual scaffold throughout. Two biological analogs are relevant for bidirectional evolution specifically.

*Ecological co-evolution* is the horizontal analog: species at the same ecological level influence each other's evolution — predator-prey dynamics, competitive interactions, mutualistic relationships produce correlated evolutionary change across peers at the same level. The horizontal direction in CKS bidirectional evolution is the architectural analog: entities at the same structural level influence each other's evolution through governed propagation of improvements.

*Developmental biology* provides the vertical analog: cell differentiation affects organ development, which affects organism structure — changes at lower levels propagate upward and body plan constraints propagate downward. The developmental hierarchy is unidirectional in most biological contexts (genetic information flows from genome to phenotype through development). CKS vertical evolution specifies both upward and downward propagation, with the downward path using the expression mechanism rather than developmental programs, and all propagation governed through human authority rather than genetic determination.

The analogs function as conceptual scaffolding — they provide intuitive orientation. The architectural substance is governed horizontal and vertical evolution within the CKS three-level structure, not biological mimicry.

---

## 5. Inherited Paper 1 commitments

Bidirectional evolution carries the full set of Paper 1 commitments, inherited directly.

**A1.01 human governance.** All bidirectional evolution is governed. Horizontal evolution changes are governed at the level where they occur — governed decisions to propagate improvements to peer entities. Vertical evolution changes require governance at both the origin level and the destination level. The A1.01 commitment that humans retain the right to inspect, modify, and override substrate content and orchestration rules applies throughout both directions.

**A6.06 authority distribution change.** When vertical evolution changes authority distribution — when Self-level DNA changes affect which humans hold authority over which substrates, or when aspect-level changes redistribute cell-level authority — the A6.06 boundary applies. Authority distribution changes through vertical evolution require boundary-level governance handling, not only origin- and destination-level governance.

**A1.13 composition requirements.** Bidirectional evolution must preserve composition validity. Horizontal propagation of improvements to peer cells or peer aspects must maintain the composition properties the architecture requires. Vertical propagation must maintain the three-level composition structure. Evolution that would break composition validity requires governance resolution before propagation proceeds.

**A1.07 retraceability.** Bidirectional evolution paths are retraceable. An improvement propagated horizontally from one cell to peer cells must be traceable: which origin cell, which governance decision authorized the propagation, which destination cells were affected, what the change was. An improvement propagated vertically — upward from cell to aspect, downward from Self through expression to cell behavior — must be traceable through the levels it crossed.

**A2.40 provenance.** Bidirectional evolution events are recorded. The provenance of every evolutionary change includes its direction (horizontal or vertical), its origin, its path, and the governance authorization that permitted propagation.

---

## 6. Operational implications

Deployments that instantiate CKS architecture with bidirectional evolution as a specified property carry several operational implications.

Horizontal evolution enables *organizational learning* as an architectural property. When a cell improves through operational experience, the improvement is not trapped in that cell's history — it is available for governed propagation to peer cells with similar functions. An organization deploying a CKS architecture can recognize that cell improvements are potential learning events for the wider cell population, and governance decisions can transfer improvements efficiently rather than allowing parallel cells to improve independently through separate experience accumulation.

Vertical evolution enables *architectural coherence* as an operational outcome. Cell improvements propagate upward to aspect and Self levels, keeping higher-level architecture aligned with lower-level operational realities. Self-level changes propagate downward through expression, keeping cell behavior consistent with updated Self-level architecture. The coherence is not automatic — it requires governance decisions at each level — but the architecture specifies propagation as available and defines the path.

Operational timescale bidirectionality means deployments must *actively manage ongoing evolution* rather than treating the deployed architecture as fixed between redeployment events. Governance machinery for evolution management — authority architecture for horizontal propagation decisions, expression configuration for downward vertical propagation, boundary handling for A6.06 cases — is operational machinery, not only design-time machinery.

When vertical evolution changes authority distribution, A6.06 boundary handling is operational work. Deployments must identify when proposed vertical evolution crosses the authority distribution boundary and must route those cases to appropriate boundary-level governance before propagation proceeds.

---

## 7. Limits

The bidirectional evolution integrating frame does not guarantee automatic bidirectionality, and several limits apply precisely.

**Governance decisions required; propagation is not automatic.** A cell that improves does not automatically propagate its improvement to peer cells; a Self-level DNA change does not automatically reconfigure cell behavior through expression. All propagation requires governance decisions. Whether improvements propagate horizontally, and in which direction vertical evolution is authorized to flow, are governance decisions made by humans holding authority over the relevant substrates. The frame specifies that propagation is *architecturally available*, not that it occurs automatically.

**Not a fourth mechanism.** Bidirectional evolution does not add a mechanism to the three (mutation, directed selection, action-feedback). Each mechanism can produce bidirectional evolution events, but the directionality property is not itself a mechanism. Deployments should not expect a discrete bidirectionality mechanism alongside the three; they should expect that governance decisions about the three mechanisms will often require considering horizontal and vertical propagation paths.

**Operational timescale governance still applies.** The fact that bidirectional evolution operates on operational timescales does not modify governance requirements. Evolution that occurs during deployment operation is still fully governed per A1.01. Operational timescale evolution is not lower-governance or self-authorizing.

**Governance quality determines architectural coherence.** The frame specifies that bidirectionality is available. Whether the architecture actually evolves as a coherent whole depends on governance quality: whether horizontal propagation decisions are made when they would produce coherence, whether vertical propagation decisions are made when they would produce alignment, and whether A6.06 boundary cases are handled correctly. The architecture provides the structure; governance decisions provide the coherence.

**Composition validity constrains propagation.** Not every improvement at one cell is composable into peer cells, and not every cell-level improvement warrants aspect-level evolution. A1.13 composition requirements constrain which propagation paths are valid. Governance decisions about horizontal and vertical propagation must include composition validity checks.

---

## 8. One-sentence architectural test

A CKS architecture instantiates the bidirectional evolution integrating frame if and only if the following is true: governed evolution changes at any structural level can propagate both horizontally to peer entities at the same level and vertically to entities at other levels in both upward and downward directions, on operational timescales, with A6.06 boundary handling when authority distribution is affected.

---

## 9. Why naming this frame as standalone matters; opening the B1.16 decomposition

Naming the bidirectional evolution integrating frame as a standalone derivation note establishes the architectural frame before its components are decomposed. B2.80 (horizontal evolution specification) formalizes cell-to-cell, aspect-to-aspect, and Self-to-Self peer influence in detail. B2.81 (vertical evolution specification) formalizes the upward and downward propagation paths, including the expression mechanism's role in the downward path. B2.82 (operational timescale treatment) formalizes what operational timescale evolution means for deployment governance. B2.83 (bidirectional evolution verification) formalizes how bidirectional evolution is verified against the architectural commitments. The five-note B1.16 decomposition (B2.79–B2.83) maps a complete territory: the integrating frame, the two component directions, the timescale treatment, and the verification standard.

After B2.83, the Phase B2 decomposition continues with B1.17 relational roles (B2.84–B2.88 and beyond), completing the systematic decomposition of Paper 2's architectural commitments into operational derivations.

The strategic function of formalizing the frame at B2.79 is prior-art establishment at the level of the integrating concept. The individual directions (horizontal, vertical) and the timescale treatment are each separately patentable; but the integrating frame — that bidirectionality is the architectural property specifying that CKS evolution can move in two directions within the three-level structure — is the upstream commitment from which the component derivations follow. Establishing this frame in public prior art before decomposing it closes the territory where any party could independently claim the architectural specification of bidirectional evolution in a three-level governed AI coordination substrate.

---

*Derivation note B2.79 in Phase B2 of Series B. Derives from B1.16 (bidirectional evolution), B1.02 (three-level structure), B1.13–B1.15 (three evolution mechanisms). Cross-references: B2.07 (level-distinct scope), B2.30 (expression mechanism), A6.06 (authority distribution change), A1.01 (human-governed), A1.13 (composition requirements), A1.07 (retraceability), A2.40 (provenance). Opens B1.16 decomposition: B2.79 (integrating frame), B2.80 (horizontal evolution), B2.81 (vertical evolution), B2.82 (operational timescale treatment), B2.83 (bidirectional evolution verification).*
