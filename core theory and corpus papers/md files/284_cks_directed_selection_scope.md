# Directed Selection Scope: Formalizing the Operating Domain of Directed Selection Across Cell, Aspect, and Self DNA Layers Under Standard Authority Architecture

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The Coordination Knowledge Substrate (CKS) pattern, as extended in Paper 2, commits to three evolution mechanisms operating in productive tension: undirected mutation through instinct evolution, directed selection through DNA evolution, and action-feedback evolution closing the loop from operational experience to governed DNA refinement. Directed selection per B1.14 operates on the DNA layer — the stabilized substrate content within every cell — but the precise scope of that operation requires formalization: which elements at which structural levels are subject to directed selection, and what lies outside that scope. This note formalizes directed selection scope as the architectural delineation of directed selection's operating domain. The scope is comprehensive across all DNA layer content at every structural level (cell, aspect, Self), and that comprehensiveness is not a separate architectural addition but a direct consequence of Paper 1's standard authority architecture (A2.01–A2.04) applying uniformly to all substrate content (A1.08). The note states the scope precisely at each structural level, identifies what is excluded from scope and why, contrasts CKS's comprehensive scope with the limited scope typical in conventional AI directed-modification approaches, presents the biological analog, identifies the inherited Paper 1 commitments that underwrite the scope, and states the operational implications and limits that follow.

## 1. Why directed selection scope needs standalone formalization

B2.61 through B2.66 completed the decomposition of B1.13 mutation — the undirected evolution mechanism through which instinct layer (LLM) changes propagate into the CKS architecture from upstream infrastructure changes. B2.67 opens the decomposition of B1.14 directed selection, the second of the three evolution mechanisms Paper 2 specifies. Six notes decompose B1.14: B2.67 (this note) formalizes the scope of directed selection; B2.68 addresses DNA modification governance; B2.69 addresses DNA version management; B2.70 addresses retroactivity treatment for DNA changes; B2.71 addresses directed selection evolution patterns; and B2.72 addresses directed selection verification. B2.73 through B2.78 and beyond will decompose B1.15 action-feedback evolution.

Directed selection scope is the natural first decomposition note for B1.14 because scope defines the domain within which all subsequent governance, versioning, retroactivity, and verification machinery operates. Before specifying how directed selection is governed or verified, it is necessary to specify what directed selection operates on. The scope question is also where B1.14 makes its most architecturally distinctive claim: directed selection applies to all DNA layer content at all three structural levels. That comprehensiveness is not self-evident; it requires derivation. The derivation runs directly from Paper 1's standard authority architecture — the same authority architecture that governs substrate operations at runtime also governs substrate evolution through directed selection. This note formalizes that derivation.

The strategic prior-art posture of this note is to place on record, at the sixty-seventh position in Phase B2, the precise scope boundary that defines directed selection's operating domain — including both what is within scope and what is deliberately excluded. Both sides of the boundary constitute patentable territory whose prior-art status this series protects.

## 2. The scope stated precisely

Paper 2 specifies that directed selection per B1.14 operates on the DNA layer per B1.06 — the stabilized orchestration and behavior content that defines how a cell behaves — within cells, aspects, and Selves. The scope is the DNA layer content at each structural level.

**Cell DNA scope.** At the cell level, directed selection can operate on the following DNA layer content, each of which was formalized as cell DNA layer specification content in B2.25:

- *Orchestration substrates* — the rules specifying how the cell processes inputs, routes consultation to the instinct layer, and integrates instinct layer outputs into cell behavior. These are the primary authored substrate content in the Paper 1 sense: human-authored rules governing cell-level execution.
- *Behavior substrates* — the rules specifying how the cell behaves for specific input conditions, including decision rules, escalation thresholds, and output formation logic.
- *Harness substrate per B2.30* — the activation rules, carry-strategy configuration specifying which DNA content the cell carries vs. accesses by reference, and expression conditions specifying which DNA content activates for which goals.
- *Schemas* — the input/output schema specifications, data type definitions, and validation rules governing what the cell accepts and produces.
- *Lifecycle policies per B2.25* — the rules governing how the cell handles birth events, the conditions under which cell death is triggered, and mating eligibility configuration.

All of these are substrate content in the sense of A1.08: they reside in the substrate, are governed by the standard authority architecture, and are subject to the inspect, modify, and override rights of A2.01–A2.03. Directed selection over cell DNA is therefore governed by the same authority architecture that governs all cell-level substrate operations.

**Aspect DNA scope.** At the aspect level, directed selection can operate on the aspect coordination rules formalized in B2.16:

- *Membership rules* — which cells participate as aspect members, including join and leave conditions.
- *Invocation rules* — how the aspect invokes constituent cells, including sequencing, parallelism, and conditional invocation logic.
- *Output-integration rules* — how cell outputs combine to produce aspect-level outputs.
- *Conflict-handling rules* — how conflicts among cell outputs or cell-level substrate states are handled at the aspect level.
- *Purpose-alignment rules* — the rules specifying how cell-level activity aligns with the aspect's defined purpose.
- *Lifecycle rules* — aspect-level birth, mating, and death governance.

These coordination rules constitute the aspect's DNA layer: the stabilized, substrate-resident rules that define the aspect's behavioral architecture rather than its individual cell operations. They are subject to directed selection in exactly the same sense as cell DNA content, because they are substrate content under the same authority architecture.

**Self DNA scope.** At the Self level, directed selection can operate on:

- *Integration architecture per B2.21* — the rules governing how aspects coexist within the Self, how Self-level operations coordinate across aspects, and how cross-level access between the Self and individual cells is configured when purpose requires direct access per B2.17.
- *Instinct/reasoning configuration per B2.23* — the configuration specifying which LLM instances serve the instinct layer, the separation configuration rules governing where instinct layer outputs are trusted vs. routed through reasoning-layer verification, high-stakes identification rules specifying which decisions are architecturally pinned to the reasoning layer regardless of instinct layer capability, verification configuration governing how instinct layer outputs are checked, and mutation governance rules specifying how instinct layer changes are integrated.

Self-level DNA scope is operationally significant in a way that warrants emphasis. The integration architecture and instinct/reasoning configuration are the highest-level DNA elements in the CKS structure: they shape the entire Self's operational character. Directed selection operating at Self level means that these highest-level configuration elements are governable and modifiable through the standard authority architecture — they are not fixed at deployment time and immutable thereafter.

**Scope exclusions.** Two domains are explicitly outside directed selection scope.

The *action layer per B2.26* is not direct directed selection scope. The action layer accumulates recorded task instances, execution traces, and outputs through routine cell operation. Action layer content grows through cell execution, not through directed modification under selection criteria. The pathway from action layer content into DNA layer content is action-feedback evolution per B1.15 — a governed, human-mediated loop in which accumulated action evidence informs proposed DNA changes that are then authorized through the standard authority architecture. Direct directed selection over the action layer would bypass that loop and the governed proposal-and-acceptance machinery it provides; action-feedback is the correct mechanism for action-to-DNA transitions.

The *instinct layer (LLM)* is not directed selection scope. LLM changes propagate through mutation per B1.13 — undirected changes arriving through upstream infrastructure upgrades, integrated through verification substrates. Directed modification of LLM weights is not part of the CKS architecture at all; that would be model fine-tuning, which is a different operation on a different layer. Within CKS, the instinct layer is treated as a governed input whose changes arrive undirected and are managed at the integration boundary, not as a substrate layer subject to directed selection.

## 3. What makes directed selection scope architecturally distinctive

Conventional AI architectures that include any form of directed modification — model fine-tuning, retrieval-augmented generation index updates, prompt library curation — typically have limited and layer-specific modification scope. Fine-tuning operates on model weights. RAG index updates operate on retrieval content. Prompt library curation operates on static prompt templates. None of these approaches provides directed-modification scope across all levels of a structured architecture simultaneously, and none operates under a unified authority architecture that makes the modification criteria themselves governable substrate content.

CKS directed selection scope is comprehensive in two senses. First, it covers all DNA layer content: every category of substrate-resident rule at every structural level is subject to directed selection. There is no carve-out for "configuration that cannot be changed" or "parameters that require specialized tooling." Second, it applies consistently at all three structural levels — cell, aspect, and Self — under the same authority architecture. A deployment can address behavioral issues at cell level, coordination issues at aspect level, and architectural issues at Self level all through the same directed selection mechanism governed by the same authority structure.

This comprehensiveness is not a separate architectural design decision added on top of Paper 1. It is a direct consequence of A1.08 (substrate-as-source-of-truth) and A2.01–A2.04 (governance affordances: inspect, modify, override, author). Because all DNA layer content is substrate content under A1.08, and because A2.01–A2.03 apply to all substrate content, the authority architecture that governs substrate operations at runtime also applies to substrate evolution through directed selection. Comprehensive directed selection scope follows necessarily from the foundational commitments Paper 1 establishes. Paper 2 is explicit: directed selection is "governed through the standard authority architecture from Paper 1" (§8).

## 4. The biological analog

In selective breeding — the historical origin of the directed selection concept — breeders can select for any trait that has a genetic basis. Scope is not limited to specific gene loci or specific phenotypic domains. If a trait varies and if variation is heritable, selective breeding can operate on it. Scope is comprehensive relative to the genetic architecture of the organism.

CKS directed selection scope is the architectural analog. Every element of DNA layer content is "heritable" in the relevant sense — it resides in the substrate, is carried forward through cell lifecycle operations, and is subject to modification under selection criteria. Therefore directed selection can operate on any DNA layer content element at any structural level. The comprehensive scope of CKS directed selection mirrors the comprehensive scope of selective breeding within the genetic layer.

CKS exceeds the biological analog in one important respect: the biological analog applies within one level of biological organization, while CKS directed selection scope applies consistently at three structural levels (cell, aspect, Self). This is one of the points where CKS exceeds biology per B1.20: biology has hierarchical levels of organization but does not have a unified directed-selection mechanism operating across all levels simultaneously under one governance authority.

The biological analog serves as a conceptual scaffold. The architectural substance is the comprehensive DNA layer scope under standard authority architecture, derived directly from Paper 1's foundational commitments.

## 5. Inherited Paper 1 commitments

Directed selection scope is underwritten by several Paper 1 architectural commitments that B2.67 inherits directly.

**A1.08 (substrate-as-source-of-truth)** establishes that substrate content — including all categories of authoritative state the architecture defines — resides in the substrate rather than in agent memory, LLM context, or untracked operational state. DNA layer content is substrate content under A1.08; this is what makes it addressable, inspectable, and modifiable through the standard authority architecture. Directed selection over DNA content is possible precisely because that content is substrate-resident rather than implicit.

**A2.46 (Category 4 content)** establishes that DNA layer content — "what rules apply" — is authoritative content whose governance is architecturally specified. Directed selection modifies the most directly authoritative category of substrate content: the rules that govern cell, aspect, and Self behavior. A2.46's Category 4 designation is what makes the modification of this content a governed act rather than an incidental operational change.

**A2.04 (rule authoring)** establishes that orchestration rules — the primary DNA layer content — must be authored by humans. Directed selection over DNA content is an instance of rule authoring in the A2.04 sense: humans (or LLMs operating under human direction with humans holding authority over the acceptance decision) deliberately modify substrate-resident rules under governance-defined selection criteria.

**A2.01–A2.03 (governance affordances: inspect, modify, override)** establish that all substrate content is subject to human inspection, modification, and override at any time. Directed selection is the systematic exercise of the modify right under governance-defined selection criteria. The modify right established in A2.02 is what makes directed selection an architectural commitment rather than a deployment option.

**B1.20 (recursive at every level)** establishes that Paper 1's architectural commitments apply at cell level, aspect level, and Self level consistently. Because A1.08, A2.01–A2.03, A2.04, and A2.46 apply at every level per B1.20, directed selection scope is comprehensive across all levels as a logical consequence.

## 6. Operational implications

Several operational implications follow from the formalized scope.

**Any behavioral issue addressable through directed selection.** Comprehensive DNA layer scope means that any behavioral issue whose source can be traced to DNA layer content — misconfigured orchestration rules, overly permissive behavior substrates, inadequate conflict-handling logic, misaligned lifecycle policies — is addressable through directed selection. Deployments do not face architectural constraints on which aspects of behavior are subject to directed improvement.

**Self-level scope is operationally significant.** The ability to apply directed selection to Self-level integration architecture and instinct/reasoning configuration means that the highest-level behavioral characteristics of a deployment — how aspects coordinate, where instinct layer outputs are trusted, which decisions are pinned to reasoning-layer verification — are governable and improvable through the same directed selection mechanism as cell-level behavior rules. Self-level directed selection enables architectural refinement of the deployment as a whole.

**Governance intensity may vary across scope elements.** Comprehensive scope does not mean undifferentiated governance. Deployments may appropriately apply different governance intensities to different DNA scope elements: Self-level instinct/reasoning configuration changes may require more extensive review, broader authority, and more rigorous verification than individual cell-level behavior rule changes. The standard authority architecture permits this differentiation — the orchestration rules governing which changes require which authorization levels are themselves DNA layer content subject to directed selection.

**Cross-partner scope per A2.47.** When directed selection operates on DNA content that affects cross-partner components — aspects or cells whose orchestration rules govern interactions with other parties — the cross-partner governance requirements per A2.47 apply. Directed selection scope at aspect or Self level may implicate cross-partner coordination, and the authority architecture must be configured to handle cross-partner authorization for such changes.

## 7. Limits

Comprehensive directed selection scope has important limits that must be named alongside the scope itself.

**Scope does not include the action layer.** Action layer content accumulates through cell execution; direct modification of action layer content through directed selection would bypass the governed action-feedback loop that B1.15 establishes. The action-to-DNA pathway runs through action-feedback evolution per B1.15, not through directed selection.

**Scope does not include the instinct layer.** LLM changes arrive through mutation per B1.13; they are not within directed selection scope. The instinct layer is governed at the integration boundary through verification substrates, not through directed modification of the LLM itself.

**Scope does not guarantee quality of directed selection changes.** Comprehensive scope means that directed selection can operate on any DNA content element. It does not mean that every directed selection change produces behavioral improvement. Quality depends on the human authoring: on the accuracy of the selection criteria, the precision of the rule modifications, and the appropriateness of the changes relative to the deployment's purpose. Scope is a necessary condition for directed improvement, not a sufficient one.

**Scope does not mean unlimited changes.** A6.02 retroactivity requirements and A1.13 composition requirements constrain how directed selection changes take effect within an existing deployment. Changes to DNA content may have retroactive effects on prior actions or on composed substrates, and those effects must be managed under the governance architecture rather than ignored. Scope is comprehensive; the governance of scope-within-scope changes is architecturally constrained.

**Scope is comprehensive but governed.** The comprehensiveness of directed selection scope and the governance of directed selection are not in tension — they are jointly underwritten by the same Paper 1 authority architecture. Scope is comprehensive because A1.08 and A2.01–A2.03 apply to all substrate content. Governance is rigorous because A2.04 and A2.46 apply to rule authoring and authoritative content modification. Comprehensiveness without governance would be arbitrary modification; governance without comprehensive scope would leave behavioral domains outside the reach of directed improvement. The standard authority architecture provides both.

## 8. Operational test

A CKS deployment instantiates B1.14 directed selection scope as formalized in this note if and only if: every element of DNA layer content at every structural level (cell orchestration substrates, behavior substrates, harness substrate, schemas, lifecycle policies; aspect coordination rules; Self integration architecture and instinct/reasoning configuration) is subject to the inspect, modify, and override rights of A2.01–A2.03 under the standard authority architecture; and neither action layer content nor instinct layer (LLM) content is subject to direct directed selection (action layer changes running through action-feedback per B1.15; instinct layer changes arriving through mutation per B1.13).

## 9. Why naming directed selection scope as standalone matters

B2.67 opens the B1.14 directed selection decomposition at the scope question because scope is the prior question on which all subsequent decomposition notes depend. B2.68 (DNA modification governance) specifies the authority architecture for making changes within the scope B2.67 defines. B2.69 (DNA version management) specifies how versions of DNA content within scope are tracked. B2.70 (retroactivity treatment) addresses how scope-reaching changes interact with prior deployment state. B2.71 (directed selection evolution patterns) formalizes recurring patterns of how directed selection operates within scope. B2.72 (directed selection verification) specifies the verification machinery applied to scope-reaching changes. Each of these six notes presupposes that scope is settled; B2.67 settles it.

Naming directed selection scope as a standalone derivation note also serves the prior-art function of this series. The claim that directed selection scope is comprehensive across all DNA layer content at all three structural levels — cell, aspect, and Self — and that this comprehensiveness follows necessarily from Paper 1's standard authority architecture rather than from a separate architectural design decision, is itself a patentable derivation. Placing this claim on record with precision, traceable to the Paper 2 source text's "governed through the standard authority architecture from Paper 1" and to the Paper 1 source text's A1.08 and A2.01–A2.04 commitments, establishes prior art for the complete scope architecture.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Directed Selection Scope: Formalizing the Operating Domain of Directed Selection Across Cell, Aspect, and Self DNA Layers Under Standard Authority Architecture.* May 12, 2026. ORCID: 0009-0004-8065-3235.
