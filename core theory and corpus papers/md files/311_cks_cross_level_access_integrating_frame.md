# Cross-Level Access Integrating Frame: Decomposing B1.19 by Formalizing the Governed Mechanism Enabling Entities at One Structural Level to Interact With Entities at Another Level While Preserving Level Distinctions

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

It is the ninety-fourth note in Phase B2 of Series B, opening the four-note B1.19 cross-level access decomposition (B2.94–B2.97). It does not introduce commitments outside Paper 2 or the inherited Paper 1 specification. Its contribution is to formalize cross-level access as the architectural integrating frame — the governed mechanism by which entities at one structural level interact with entities at another structural level while preserving level distinctions — so that subsequent decomposition notes (B2.95: cross-level access governance; B2.96: cross-level access patterns; B2.97: cross-level access verification) can reference a stable prior-art anchor.

## Abstract

Paper 2's three-level structure (cell, aspect, Self) per B1.02 requires that entities at different levels be able to interact. Without governed inter-level interaction, the three levels would be structurally isolated: cells could not receive coordination from aspects, aspects could not be governed by Selves, Selves could not exercise governance over operational behavior. This note formalizes cross-level access as the architectural integrating frame that makes the three-level structure coherent rather than three isolated layers. Cross-level access is defined as the governed mechanism by which an entity at one structural level interacts with an entity at another structural level. Access operates in two directions — downward (higher-level governing lower-level) and upward (lower-level reporting to higher-level) — and is configured through the Self integration architecture per B2.21. Authority distribution per A2.47 specifies who holds cross-level access authority at each level; access without authority is a governance violation. Crucially, cross-level access does not collapse levels: a cell receiving downward access from an aspect remains a cell; an aspect contributing upward to Self integration remains an aspect. The levels remain distinct; the access is the governed channel between them. The expression mechanism per B2.30 is one specific form of downward cross-level access — Self DNA affecting cell behavior — and is treated here as the architecturally developed canonical instance of the frame in operation.

## 1. Why the cross-level access integrating frame needs to be formalized as a standalone derivation

Phase B2 decomposes each B1 foundational commitment into operational variants that expose patentable architectural territory. Notes B2.89–B2.93 completed the B1.18 content-domain decomposition. B2.94 opens the B1.19 decomposition, which runs four notes: B2.94 (this note, the integrating frame), B2.95 (cross-level access governance), B2.96 (cross-level access patterns), and B2.97 (cross-level access verification). After B2.97, Phase B2 continues with B2.98–B2.110 decomposing B1.20's recursive Paper 1 commitments.

Cross-level access is architecturally load-bearing in a specific way that makes it worth formalizing before its operational decompositions. It is not merely a feature of the three-level structure — it is what makes the three-level structure function as one coherent whole rather than as three independent systems. The three levels are the structural fact; cross-level access is the mechanism that makes those levels functional together. This note formalizes that architectural role precisely, establishing the integrating frame that the three subsequent decomposition notes can treat as given.

The strategic prior-art posture follows the Series B pattern throughout: naming the frame explicitly, with precise architectural content, in advance of any downstream claim that the mechanism is novel. The cross-level access integrating frame is not a product or implementation; it is an architectural specification of governed inter-level interaction with direction, authority, and level-distinction constraints. Placing it in the prior-art chain at this position closes territory across any architecture that uses governed hierarchical access patterns without attributing the frame.

## 2. The architectural frame precisely stated

**Definition.** Cross-level access is the governed mechanism by which an entity at one structural level interacts with an entity at another structural level within the three-level CKS structure per B1.02.

The definition has four load-bearing components. First, it is a *mechanism* — a specified architectural channel, not ad hoc inter-level communication. Second, it is *governed* — access rules are authored, access authority is distributed, and access events are subject to the governance commitments inherited from A1.01. Third, it operates *between structural levels* as defined by the three-level structure per B1.02: cell, aspect, Self. Fourth, it is an *interaction* — cross-level access enables an entity to act on, report to, or be acted on by an entity at another level, without that entity becoming a member of the other level.

**Why cross-level access is necessary.** Without cross-level access, the three-level structure would be three structurally isolated layers unable to function together. Cells would execute without receiving coordination input from aspects; aspects would operate without Self-level governance; Selves would hold governance authority in name but lack a governed channel through which to exercise it over operational behavior. Cross-level access is not an optional extension of the three-level structure — it is what makes the three levels function as one governed whole.

**Two access directions.** Cross-level access operates in two directions, each governed distinctly.

*Downward access* is higher-level entities accessing lower-level entities. Three downward access forms are specified. Self-to-aspect downward: the Self exercises governance authority over aspect configuration through the integration architecture per B2.21. Self-to-cell downward: Self DNA affects cell behavior through the expression mechanism per B2.30 — this is the architecturally most developed instance of downward cross-level access in Paper 2's core theory. Aspect-to-cell downward: the aspect exercises coordination authority over its constituent cells through coordination rules per B2.16, operating over those cells as its content domain.

*Upward access* is lower-level entities accessing higher-level entities. Two upward access forms are specified. Cell-to-aspect upward: cells report operational results to aspects, contributing to aspect-level coordination outcomes across the cells the aspect holds. Aspect-to-Self upward: aspects contribute to Self integration, informing Self-level operational decisions and providing the material from which the integrated whole exercises its governance.

**Configuration per B2.21.** Cross-level access patterns are substrate-resident configuration, not hardwired architectural defaults. What cross-level access is permitted — which entities have access to which other entities at which scope — is specified in the Self integration architecture per B2.21 and authored per A2.04 as substrate content under Paper 1's governance commitments. This makes cross-level access configuration itself human-governed, inspectable, modifiable, and overridable per A1.01.

**Authority distribution per A2.47.** Cross-level access authority is distributed per A2.47's Category 5 authority distribution. Not every entity at every level holds cross-level access authority to all other levels; the authority distribution specifies who at each level has authority to access entities at other levels and under what conditions. Cross-level access without authority is a governance violation in the CKS sense — an architectural constraint, not merely a policy preference. Cross-partner cross-level access, where access crosses partner governance boundaries, requires cross-partner authority per A2.47.

**Level-distinction preservation.** Cross-level access does not collapse levels into one. A cell that receives downward access from an aspect remains a cell; it does not become an aspect. An aspect that contributes upward to Self integration remains an aspect; it does not become a Self. The levels remain structurally distinct per B1.02; the access is governed interaction between distinct levels, not a merger of levels.

## 3. What makes the cross-level access integrating frame architecturally distinctive

The contrast with conventional multi-component AI architectures is direct. In typical architectures with multiple components — LLM agents calling other agents, orchestration layers delegating to sub-agents, multi-step pipelines — cross-component communication is architecturally implicit. Components call each other through APIs or message-passing without any specified access governance: no access direction specification, no authority distribution, no level-distinction constraint, no substrate-resident configuration of what access is permitted. Such architectures may have implicit hierarchical relationships (orchestrator over worker), but the architectural specification of those relationships is absent or treated as a deployment-time engineering concern rather than a first-class architectural commitment.

CKS cross-level access is architecturally explicit across four dimensions that conventional architectures treat implicitly: (1) access direction is specified — downward and upward, with named forms at each direction; (2) authority distribution is specified per A2.47, naming who holds access authority at each level; (3) configuration is substrate-resident, authored per A2.04 and held as governed substrate content per B2.21; and (4) level-distinction preservation is a first-class architectural constraint, not a consequence of deployment-time practice.

The explicit access governance is what preserves the three-level structure as architecturally coherent while enabling the inter-level interactions the structure requires. An architecture that names three levels but leaves inter-level communication unspecified has named three levels; it has not committed to cross-level access governance, and the three-level structure is therefore nominal rather than architectural.

## 4. The biological analog as conceptual scaffold

Cross-level access parallels intercellular signaling within biological organismal hierarchy. In an organism, cells receive signals from tissues (downward access — the tissue-level coordination pattern affects cell behavior without cells becoming tissues) and report status to tissues (upward access — cell-level metabolic state informs tissue-level coordination without cells acquiring tissue-level governance authority). The hierarchical signaling enables coherent organismal function while maintaining cellular and tissue identity as distinct levels.

CKS cross-level access is the governed architectural analog of this signaling structure. The analog is useful as conceptual scaffold — it locates the architectural pattern within a familiar organizational logic — but the architectural substance is not the biology. The architectural substance is: governed directed inter-level interaction, with access direction specified, authority distributed, configuration substrate-resident, and level distinctions preserved by architectural constraint rather than by biological development.

The biological analog breaks in one important place where CKS exceeds biology: biological intercellular signaling is not authored, inspectable, or overridable by a governing human. CKS cross-level access is all three. The harness substrate per B2.30 through which expression (one form of downward cross-level access) operates is itself human-governed, fully inspectable, modifiable, and overridable per A1.01. The biological analog's value is conceptual scaffolding; the operational specification is architectural.

## 5. Inherited Paper 1 commitments

Cross-level access inherits the full Paper 1 commitment set as that set applies to the access mechanism.

*A1.01 (human-governed).* Cross-level access governance is itself human-governed: the access configuration per B2.21 is substrate content subject to A1.01's three rights (inspect, modify, override). Cross-level access patterns are not hardwired architecture; they are authored substrate content that humans can inspect, modify, and override at any time.

*A2.47 (Category 5 authority distribution).* Cross-level access authority is distributed at Category 5: who has authority to access entities at other levels, at what scope, and under what conditions. The authority distribution is itself substrate content under Paper 1's governance commitments.

*A2.04 (rule authoring).* Access rules — specifying what cross-level access is permitted, in which direction, at what scope, by which entities — are authored per A2.04 as human-authored governance content. The authority-not-labor distinction from A1.01 holds here: humans hold authority over access rule content; LLMs may draft access rules under human direction without those rules taking effect outside human authority.

*A2.40 (provenance).* Cross-level access events are operational records subject to provenance tracking per A2.40. When a Self exercises authority over aspect configuration, when an aspect reports to Self integration, when Self DNA is expressed at the cell level through expression per B2.30 — these are recordable events with provenance metadata, not invisible operations.

*B2.21 (Self integration architecture).* Cross-level access is configured through the Self integration architecture per B2.21. The integration architecture is the substrate-resident home for cross-level access configuration, specifying which access patterns are enabled and at what scope for a given deployment.

*B2.30 (expression mechanism).* The expression mechanism per B2.30 is one specific, architecturally developed form of downward cross-level access: Self DNA affecting cell behavior through the harness substrate. B2.30 is not the whole of cross-level access; it is the canonical downward form through which Paper 2's core theory develops the access pattern most thoroughly, and it serves as the load-bearing concrete example of the frame in operation.

## 6. Operational implications

*Configure access per B2.21.* Deployments configure cross-level access patterns through the Self integration architecture per B2.21. Configuration specifies which cross-level access forms are active, what access scope applies at each direction, and what authority is required to exercise access. Access configuration is authored per A2.04 and held as substrate content, not as hardwired deployment logic.

*Authority verification.* Cross-level access events are subject to authority verification per A2.47. Only entities with specified cross-level access authority can initiate or receive cross-level access at a given direction and scope. Verification is an architectural requirement: the access configuration itself specifies the authority requirements, and access without meeting those requirements is a governance violation.

*Operational records.* Cross-level access events are operational records per A2.40. The governance record therefore includes cross-level interaction events alongside within-level operational events. This enables governance and provenance review of how levels have interacted across a deployment's operational history — including which entities exercised downward access, what upward reports were generated, and when expression per B2.30 activated.

*Vertical evolution uses configured cross-level access paths.* Vertical evolution per B1.16 — propagating improvements upward and downward through the three-level structure — operates through the configured cross-level access paths. Upward propagation (cell improvements informing aspect evolution, aspect improvements informing Self evolution) uses the upward access forms; downward propagation (Self-level governance changes affecting aspect and cell configuration) uses the downward access forms. The cross-level access integrating frame is therefore the operational substrate for vertical evolution, not merely a static access specification.

*Cross-partner cross-level access.* When cross-level access crosses partner governance boundaries — entities in one partner's governance perimeter accessing entities in another partner's perimeter — cross-partner authority per A2.47 is required. The cross-partner shape is a boundary case of the cross-level access frame, not a separate access mechanism, and the same direction, configuration, and level-distinction constraints apply.

## 7. Limits of cross-level access

Stating the limits of the frame is as important as stating the frame, because cross-level access is architecturally significant and several misreadings are natural.

*Cross-level access does not collapse levels.* This is the central limit. Downward access by a Self over an aspect is governed interaction between distinct levels; it is not the Self absorbing the aspect or the aspect becoming a part of the Self beyond its already-integral relationship. Upward reporting by a cell to an aspect is governed interaction between distinct levels; it is not the cell acquiring aspect-level governance authority. Levels remain structurally distinct per B1.02 before and after cross-level access events.

*Downward access is not arbitrary override.* Downward cross-level access is governed and scoped. A Self does not hold unrestricted authority to override any cell-level operation simply by virtue of being at a higher level. Access is governed by the configuration per B2.21 and constrained by the authority distribution per A2.47. Downward access through expression per B2.30 is governed — the harness substrate is the channel, and the expression mechanism specifies what DNA-layer substrates activate, not a blank override authority over any cell operation.

*Upward access is reporting, not escalation.* Upward cross-level access — cells reporting to aspects, aspects contributing to Self integration — is governed reporting and contribution. It is not the escalation of lower-level governance authority upward. A cell contributing to aspect coordination outcomes does not acquire aspect-level governance authority by virtue of that contribution. An aspect informing Self-level operational decisions does not acquire Self-level authority over other aspects through that reporting.

*Cross-level access is not authority delegation.* Authority delegation is a distinct architectural primitive: it involves transferring governance authority from one entity to another. Cross-level access is governed interaction between entities that retain their respective level identities and authority scopes. An aspect exercising downward access over a cell has not delegated its authority to the cell; it has interacted with the cell through the governed access channel, with the cell's own authority scope unchanged.

*Cross-level access does not make cells equivalent to aspects through access alone.* A cell that participates in extensive cross-level access — receiving downward access from aspects and Selves, reporting upward to aspects — remains a cell with cell-level scope per B2.11. Cross-level access changes what interactions a cell participates in; it does not change the cell's structural level or its level-appropriate architectural scope.

## 8. One-sentence architectural test

A CKS deployment instantiates the cross-level access integrating frame if and only if it specifies, for each structural level in its three-level structure, the governed directions by which entities at that level may interact with entities at other levels, the authority required to initiate or receive such interaction, and the substrate-resident configuration that defines what access is permitted — such that entities at each level remain structurally distinct from entities at other levels following any cross-level access event.

## 9. Why naming this frame as standalone matters: opening the B1.19 decomposition

Phase B2 operates by decomposing each B1 foundational commitment into the operational architecture that commitment implies. The B1.19 decomposition (B2.94–B2.97) follows this pattern: before naming the access governance mechanisms (B2.95), the access patterns (B2.96), and the access verification procedures (B2.97), B2.94 names what cross-level access *is* architecturally — the integrating frame from which those decompositions proceed.

The prior-art value of naming the frame explicitly is that downstream work claiming novelty in governed hierarchical access, multi-level entity interaction, or directed inter-level communication in AI systems architectures encounters B2.94 as a prior specification: cross-level access as a governed mechanism with specified directions, authority distribution, substrate-resident configuration, and level-distinction preservation — published in advance under the author's name. The more precisely the frame is stated, the smaller the territory available for downstream claims that do not attribute or distinguish from it.

B2.95 through B2.97 will develop the governance, patterns, and verification decompositions that the frame established here enables. B2.98–B2.110 will then complete Phase B2 by decomposing B1.20's recursive Paper 1 commitments. B2.94 opens that sequence by placing the cross-level access integrating frame in the prior-art chain at a position that can carry the subsequent three-note decomposition on a stable architectural foundation.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cross-Level Access Integrating Frame: Decomposing B1.19 by Formalizing the Governed Mechanism Enabling Entities at One Structural Level to Interact With Entities at Another Level While Preserving Level Distinctions.* May 12, 2026. ORCID: 0009-0004-8065-3235.
