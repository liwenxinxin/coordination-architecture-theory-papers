# Instinct-Routing Patterns in the Coordination Knowledge Substrate Pattern: Operational Variants of the Instinct/Reasoning Separation per Cell Goal

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the operational patterns by which cells route processing between consulting the instinct layer (LLM) and processing through the reasoning layer (substrate) per cell goal under rules authored per A2.04.

## Abstract

A separate derivation note (B1.01) formalizes the instinct/reasoning separation as Paper 2's foundational architectural commitment: the LLM as instinct layer, the CKS substrate as reasoning layer, and the two layers as independently-evolving components under unified human governance. Subsequent decomposition notes formalize the instinct layer alone (B2.01), the reasoning layer alone (B2.02), and the architectural test for separation (B2.03). This note formalizes the next decomposition: how the separation manifests operationally per cell through routing patterns. Cells with different goals route processing differently between instinct and reasoning, with routing rules themselves substrate-resident authoritative content authored per A2.04. The note enumerates six illustrative routing patterns — pure-instinct, pure-reasoning, hybrid, conditional, multi-consultation, parallel — and articulates what makes routing-as-architectural-commitment distinctive, what cognitive analog it stands in for, what Paper 1 commitments it inherits, what operational implications follow, and what the commitment does not entail.

## 1. Why instinct-routing patterns need to be formalized as standalone

A separate note (B1.01) defends the foundational commitment: the LLM operates as instinct layer, the substrate operates as reasoning layer, and the two compose into one Self under unified human governance with the layers independently evolving. B2.01 and B2.02 formalize what each layer commits to alone; B2.03 formalizes the architectural test for whether a candidate system instantiates the separation.

What those notes do not specify is how the separation manifests *per cell at execution time*. A Self typically contains many cells with different goals. Some cells perform pattern-matching tasks well-served by the LLM's fast-path responses; some perform deterministic logic well-served by substrate-resident rules; some benefit from LLM consultation followed by substrate-rule validation; some require iterative or multi-perspective LLM input combined under substrate orchestration. The instinct/reasoning separation is what makes these per-cell variations architecturally available. The patterns by which cells exercise that variation — *which* cells consult the LLM, *how* they consult, *what* substrate logic processes the result — are operationally distinct from the foundational separation and require their own formalization.

The remedy is to name **instinct-routing patterns** as a standalone architectural variant with independent operational content. Routing is the operational mechanism by which the separation manifests differently for different cell goals; routing rules are themselves substrate-resident authoritative content per A2.46 Category 4; routing decisions are recorded per A2.40. Naming routing patterns as a class makes the per-cell adaptability of CKS deployments architecturally describable rather than incidental, and prevents the misreading that the instinct/reasoning separation imposes one fixed processing pattern across every cell in a Self.

This note is the fourth of approximately six Phase B2 decomposition notes for B1.01. B2.01 specifies the instinct layer; B2.02 specifies the reasoning layer; B2.03 specifies the architectural test; B2.04 (this note) specifies the routing patterns; B2.05 will specify high-stakes-decision identification for reasoning-pinning; B2.06 will specify verification gates for instinct.

## 2. The architectural commitment, stated precisely

In the CKS pattern, a cell's **routing pattern** specifies, for the cell's execution per the cell goal, whether and how the LLM is consulted, whether and how substrate-resident rules process the result, and how the two combine. Routing patterns are specified by orchestration rules authored per A2.04. The rules are substrate-resident authoritative content per A2.46 Category 4 — that is, the substrate is authoritative on which routing pattern applies to which cell. Routing decisions taken at execution time are recorded in provenance per A2.40 — the substrate carries which pattern executed, what input went to the LLM (if anything), what output came back, what substrate logic processed it.

Six routing patterns are illustrative, not exhaustive. Each is specified at the orchestration-rule layer; each is substrate-resident; each is applied per cell rather than per Self.

**Pure-instinct routing.** The cell consults the LLM and processes the result minimally through substrate logic. Substrate processing is limited to receiving the LLM output and writing it to substrate per A2.19 Property A — the LLM consults; the substrate writes. Appropriate when the cell goal is well-served by pattern-matching and the LLM's fast-path response carries the work. Risk noted in §7: pure-instinct routing without substrate-rule processing of the output risks failing the architectural test per B2.03, since corrections to cell behavior would require modifying the LLM rather than modifying substrate-resident logic.

**Pure-reasoning routing.** The cell processes only through substrate-resident logic without consulting the LLM. Substrate-resident rules per A2.04 specify the cell behavior fully. Appropriate when the cell goal is well-served by deterministic substrate logic and pattern-matching is not required.

**Hybrid routing.** The cell consults the LLM and processes the LLM output through substrate-resident rules per A2.20 Property B. Appropriate for goals that benefit from instinct pattern-matching followed by reasoning-layer validation, conflict checking, transformation, or cross-checking against substrate-resident decisions. The LLM is the candidate; the substrate is the gate.

**Conditional routing.** The orchestration rule specifies conditional logic determining which routing pattern applies based on input characteristics — pure-instinct for one input class, hybrid for another, pure-reasoning for a third. The conditional logic itself is substrate-resident authoritative content per A2.46 Category 4. Appropriate when different input categories warrant different processing approaches within a single cell's scope.

**Multi-consultation routing.** The cell consults the LLM multiple times, potentially with different prompts, and substrate logic processes the multiple outputs. Substrate rules orchestrate the consultations and combine their outputs. Appropriate when iterative or multi-perspective LLM input is useful.

**Parallel routing.** The cell consults the LLM concurrently with substrate-resident processing along an independent path; substrate rules combine the results. Appropriate for goals where redundant processing increases reliability, where instinct and reasoning are expected to converge most of the time, and where divergence is itself an output the substrate uses to flag the case.

The enumeration is explicitly illustrative. Deployments may author additional patterns per A2.04 specifying novel routing logic. The architectural commitment is that *whatever* pattern a cell uses, the pattern is rule-specified, substrate-resident, and recorded — not that the six named patterns exhaust the design space.

## 3. What makes instinct-routing patterns architecturally distinctive

Conventional AI architectures typically commit to a single routing pattern for every cell or processing unit: every component invokes the model in the same way, with the same harness substrate, under the same conditions. Where the instinct/reasoning split is attempted at all, it is typically uniform — every component uses the LLM the same way, and per-cell adaptability is left to the application layer rather than the architecture.

CKS deployments commit to the opposite: routing patterns vary per cell purpose under orchestration-rule governance. Different cells in the same Self may use different routing patterns; the same cell may use different patterns under different input conditions through conditional routing; the routing rules themselves are substrate-resident authoritative content humans inspect, modify, and override per the inherited A1.01 authority architecture. The configurability under governance is what makes CKS deployments operationally adaptable to varied requirements without modifying the instinct or reasoning layers themselves. A Self with many cells can carry pattern-matching cells under pure-instinct routing alongside compliance-bearing cells under hybrid or pure-reasoning routing, with the routing rules — not the LLM, not the substrate platform, not the cell scaffolding — carrying the variation.

Routing is therefore not a runtime engineering choice that emerges from how each cell happens to be implemented; it is a substrate-resident architectural commitment under rule governance.

## 4. The cognitive analog as conceptual scaffold

Routing patterns parallel the human cognitive phenomenon of mode-of-engagement selection. Different tasks engage different cognitive modes: some are predominantly System 1 pattern-recognition (similar in shape to pure-instinct routing), some are predominantly System 2 deliberation (similar to pure-reasoning routing), most combine the two (similar to hybrid routing). The analog functions as conceptual scaffold readers absorb quickly because the parallels are intuitive. The architectural substance is the commitment to rule-specified routing under governance. Paper 2 §4 makes the same move at the foundational level — System 1/System 2 framing as scaffold, architectural separation as commitment — and B2.04 makes it again at the operational level: cognitive mode selection as scaffold, rule-specified routing as commitment. The architectural argument would hold with the cognitive scaffold replaced; the scaffold earns its place on warrant, not on theoretical load-bearing.

## 5. Inherited Paper 1 commitments

Routing patterns inherit Paper 1 commitments without modification. The A1.04 mediator role bounds all patterns: even pure-instinct routing preserves Properties A through E, with the LLM consulting but not directing writes (Property A) and substrate orchestration governing LLM output processing where rules so specify (Property B). A routing pattern that grants the LLM substrate-write authority outside the mediator role is not a CKS routing pattern, regardless of how it is named.

The A2.04 rule-authoring authority architecture is the foundation: routing rules are authored under human authority, with labor allocable to humans directly or to LLMs operating under human direction. A2.20 Property B is invoked explicitly by hybrid, multi-consultation, and parallel routing — substrate rules govern *what happens to* LLM outputs, not just *whether* the LLM is consulted. A2.46 Category 4 makes routing rules substrate-resident authoritative content; vendor middleware that overrides them outside the human-governed authority architecture is incompatible with the commitment. A2.40 records routing decisions in the six-field provenance metadata, which is what makes routing auditable per A1.07 retraceability. The A1.10 determinism contract holds: given the same inputs and the same routing rule, cell behavior is deterministic at the substrate-state level the contract commits to, with LLM-side non-determinism bounded by Property B substrate rules where they apply. And when a cell consults the LLM as adjacent component, the consultation can follow the A4.27 Pattern A operationalization — substrate-prepared prompt in, structured output out, substrate-rule processing of the result.

The inherited commitments are not new architectural content; they are what routing patterns already operate within once the foundational separation is in place.

## 6. Operational implications

Six implications follow directly from the formalization.

Routing is configured per cell purpose during the birth lifecycle primitive per B1.09 — the pattern is part of the orchestration rule the cell carries from origination, authored explicitly or selected from a catalog of substrate-resident patterns the deployment maintains. Routing patterns are evolvable per directed selection per B1.14: humans modify routing rules to optimize cell behavior — narrowing pure-instinct to hybrid where post-hoc inspection reveals errors instinct silently produced, broadening hybrid to pure-instinct where substrate-rule processing has become rote, introducing conditional routing where input variation warrants it. Routing patterns are testable through the A5.16 reproducibility test — given recorded inputs and a recorded routing rule, replay produces the recorded outputs at substrate-state level. Routing is one of three mutation governance instruments per B1.13 alongside verification and pinning: when upstream LLM upgrades change instinct behavior, routing rules can redirect specific cell goals from pure-instinct to hybrid or pure-reasoning during the integration period and back as verification evidence accumulates, which is also how deployments operationalize partial adoption of new instinct capability across cells. Routing patterns interact with verification gates per B2.06 (a verification regime appropriate for pure-instinct may be inadequate for hybrid) and with high-stakes-decision identification per B2.05 (high-stakes decisions typically use pure-reasoning or hybrid-with-pinning rather than pure-instinct). And because routing decisions are recorded in provenance per A2.40, an auditor exercising the inspect right can reconstruct, for any past cell execution, which pattern applied and what processing occurred — which is what makes routing patterns architecturally accountable rather than only operationally specified.

## 7. What the commitment does not entail

Six limits keep the standalone framing from drifting beyond what Paper 2 supports.

Routing patterns do not bypass governance — all patterns operate under A2.04 rule specification within the human authority architecture inherited from A1.01, and routing is not a side channel through which deployments can grant the LLM authority outside the mediator role. Routing patterns do not violate Properties A–E — even pure-instinct routing preserves A2.19 Property A, with the LLM consulting and the substrate writing; a routing rule that grants the LLM direct substrate-write authority is not a CKS routing pattern.

The pattern enumeration is not exhaustive — pure-instinct, pure-reasoning, hybrid, conditional, multi-consultation, and parallel are illustrative, with deployments authoring additional patterns per A2.04 as their goals require. Routing per cell is not fixed — vertical evolution per B1.16 may modify a cell's routing pattern through DNA evolution per B1.14, since routing rules are themselves DNA-layer content under governance.

Routing patterns do not eliminate the instinct/reasoning separation. Pure-instinct routing does not collapse the layers; it specifies that this cell's processing engages the instinct layer fully and the reasoning layer minimally. The two layers remain architecturally separate; what varies per cell is which layer carries which work. A Self with all cells under pure-instinct routing would still hold the layers separable architecturally — and would also be a Self in which the architectural test per B2.03 should be applied with extra care, since substrate-rule processing of LLM outputs is what makes corrections-without-LLM-modification practically available.

Finally, routing patterns do not specify which LLM is consulted. That is mutation governance per B1.13 territory. Routing specifies *whether* and *how* the LLM is consulted; mutation governance specifies *which* LLM. The two operate over different commitments and compose under unified human governance per Paper 2 Claim 5.

## 8. Operational test

A Self instantiates the instinct-routing-patterns commitment if and only if all of the following are true at all times during the Self's existence:

1. For every cell, an orchestration rule authored per A2.04 specifies the cell's routing pattern.
2. The routing rule is substrate-resident authoritative content per A2.46 Category 4; no vendor middleware can in principle override it outside the human-governed authority architecture.
3. Every cell execution records, in provenance per A2.40, which pattern applied, what input went to the LLM (if any), what output came back, and what substrate-rule processing occurred.
4. Different cells in the Self may carry different routing patterns; the architecture does not require uniformity.
5. The routing rule is humanly inspectable, modifiable, and overridable per the inherited A1.01 authority architecture, with changes evolving through the directed-selection mechanism per B1.14.

A system that fails any of (1)–(5) does not implement instinct-routing patterns specifically, even if it implements the foundational instinct/reasoning separation in some other respect. Such a system may carry the separation at the foundational level, but is not CKS-coherent on the routing axis.

## 9. Why naming as standalone matters

A reader who treats the instinct/reasoning separation per B1.01 as the only architectural commitment at this layer can read CKS deployments as committing to one fixed processing pattern across every cell in a Self — every cell consults the LLM the same way, every cell processes results the same way, the per-cell adaptability is application-layer engineering rather than architectural property. This misreads the per-cell adaptability that makes CKS deployments operationally usable across varied requirements.

Naming instinct-routing patterns as a standalone operational variant gives downstream implementers a precise specification of what their per-cell processing variation must satisfy: rule-specified, substrate-resident, recorded, evolvable under governance. It makes the configurability under governance describable as architectural commitment rather than as application-layer convenience. And it preserves the foundational framing of B1.01 by clarifying that what varies per cell is *which* layer carries *which* work, not whether the layers exist as separate architectural components.

This is the fourth of approximately six Phase B2 decomposition notes for B1.01. B2.01 specifies the instinct layer alone; B2.02 specifies the reasoning layer alone; B2.03 specifies the architectural test for separation. B2.04 (this note) specifies the patterns by which cells route between them. B2.05 will specify high-stakes-decision identification for reasoning-pinning — which decisions architecture-pin to the reasoning layer regardless of how capable instinct becomes. B2.06 will specify verification gates for instinct — the substrate-resident gates through which LLM output passes when verification is required. Subsequent Phase B2 notes decompose B1.02 through B1.20 in the same operational-variant-as-architectural-decomposition shape.

Subsequent work that adopts CKS routing patterns, extends them with additional patterns, composes them with adjacent patterns, or argues against them should use "routing patterns" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Instinct-Routing Patterns in the Coordination Knowledge Substrate Pattern: Operational Variants of the Instinct/Reasoning Separation per Cell Goal.* May 7, 2026. ORCID: 0009-0004-8065-3235.
