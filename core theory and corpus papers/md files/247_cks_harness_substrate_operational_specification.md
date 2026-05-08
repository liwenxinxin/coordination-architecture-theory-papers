# The Harness Substrate as Substrate-Resident Expression Determination Component in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the **harness substrate operational specification** as a standalone derivation: the harness substrate as substrate-resident architectural component within cell internals that determines DNA-layer activation per cell goal under human governance, with the operational content, governance posture, and inherited Paper 1 commitments made explicit so that subsequent decompositions of expression patterns, carry-strategies, and expression evolution can build on a fixed reference.

## Abstract

Paper 2 commits, within Claim 2, to expression as governed selection over which DNA-layer substrates activate per cell goal, and names the **harness substrate** as the cell-internal mechanism that performs that selection. The commitment is load-bearing: multi-aspect cell participation, carry-strategy variation across deployments, action-feedback refinement of expression rules, and the architectural realization of high-stakes pinning all run through the harness substrate. This note formalizes the harness substrate's operational specification as a standalone architectural component — what it holds, where it sits, what governs it, what it is distinct from, and what inherited Paper 1 commitments determine its behavior. It articulates the biological analog (cellular regulation of gene expression) and where CKS exceeds biology, enumerates inherited commitments, operational implications, and limits, and provides a one-sentence architectural specification.

## 1. Why the harness substrate operational specification needs to be formalized as standalone

Paper 2 names the harness substrate within the *Expression* subsection of *Three levels of structure*: every cell carries a harness substrate that is itself human-governed, fully inspectable, modifiable, and overridable, and that selects which sub-substrates are active for current activity. Several downstream commitments — carry-strategy choice between full DNA with selective expression and partial slice, per-aspect expression in multi-aspect cell participation, expression evolution under directed selection and action-feedback, and the architectural realization of high-stakes pinning — depend on what the harness substrate operationally consists of, where it sits relative to the DNA and action layers, what governs its content, and how it inherits Paper 1's commitments. Without an explicit operational specification, those downstream commitments are reachable only by reading several Paper 2 sections together and reconstructing the harness substrate's role by inference.

The remedy is to formalize the harness substrate as a substrate-resident architectural component with explicit operational content, distinct from the DNA layer it operates over and the action layer it does not produce. The strategic posture is defensive publication of public prior art: the more explicitly the harness substrate's operational content is recorded as derived from Paper 2, the smaller the territory in which any party could later claim novel invention of an expression-determination layer, an activation-rule layer, a per-deployment carry-strategy mechanism, or a per-aspect expression-rule mechanism without bumping into this prior-art chain.

This is the thirtieth note in Phase B2 and opens the five-note decomposition of B1.07 (expression mechanism). Subsequent notes formalize DNA activation patterns (B2.31), carry-strategy operational specification (B2.32), expression evolution operational treatment (B2.33), and expression mechanism inheritance verification (B2.34). The Phase B2 sequence then continues to B1.08 (modularity from architectural commitment) at B2.35.

## 2. The architectural specification, precisely stated

In the CKS pattern as extended by Paper 2, the **harness substrate** is the substrate-resident architectural component within cell internals that determines which DNA-layer substrates activate for which inputs, contexts, and aspects under human governance. Operationally, the harness substrate carries five categories of content:

**(a) Activation rules.** Rules, authored as orchestration content under A2.04, specifying conditions under which DNA-layer elements activate. Rules can specify activation by input characteristics, by context, by aspect membership, or by combinations of these.

**(b) Carry-strategy configuration.** Specification of whether the cell carries the full Self's DNA with selective expression, or carries a partial slice — the per-deployment design choice Paper 2 commits to. The harness substrate is what implements the chosen carry-strategy at the activation determination layer; the carry-strategy itself is decomposed in B2.32.

**(c) Expression conditions.** Substrate-resident specifications of when expression occurs — whether evaluated on each input, re-evaluated when context changes, refreshed at deployment-phase transitions, or held stable across some scope — and how activation state is maintained between evaluations.

**(d) Input-to-expression mapping.** The mapping from cell inputs to activation decisions, itself substrate-resident content rather than implicit in the cell's processing logic. What inputs lead to what activation choices is inspectable, modifiable, and overridable as substrate state.

**(e) Context-aware expression specifications.** Rules that condition activation on the cell's current context — which aspect the cell is participating in, what time, what deployment phase, what upstream cell signaled the request, what authority is currently in effect. Context-aware expression supports a single cell having different active behavior in different aspect contexts per B1.17.

The harness substrate is **substrate-resident** per A1.08 — its content lives on the substrate side of the A1.02 boundary, not inside the LLM and not in cell-internal processing memory. It is **authoritative content** per A2.46 Category 4 — what activates which DNA element under which conditions is governable substrate state, not an emergent property of inference. It is **authored** under A2.04, with humans holding authority over rule content while the labor of drafting may be allocated to LLMs operating under that authority. It is **inspectable** per A2.01, **modifiable** per A2.02, and **overridable** per A2.03 with no architectural justification gate. Operations on the harness substrate are recorded with A2.40's six provenance metadata fields.

The harness substrate **evolves** through Paper 2's evolution mechanisms. Directed selection per B1.14 is the primary path: humans modify harness rules to refine expression behavior, with intent and outcome evaluated together. The harness substrate may also evolve through action-feedback per B1.15: substrates that propose harness modifications can examine action-layer evidence for refinement opportunities, with human mediation governing whether proposals take effect. Both produce governance events with A2.40 provenance.

## 3. What makes the specification architecturally distinctive

Conventional AI components that select among behaviors typically have **implicit activation logic** — the component's processing determines what it does without architectural specification of activation determination as governable substrate content. A model that selects different responses for different inputs encodes the selection in its parameters; a chain of prompts that branches across contexts encodes the branching in code; a feature-flag layer over a model encodes flag configurations in deployment files. None of these are wrong as engineering practice. What they share is that activation determination is not a named, located, governable substrate component with the three rights from Paper 1 attached.

The harness substrate operational specification makes activation determination an **explicit substrate-resident component** with three architectural consequences. First, expression behavior is **traceable**: an activation decision can be retraced to the harness rule that produced it under A1.07's path retraceability commitment, with the rule's authorship and version history available under A2.01. Second, expression is **explainable through harness inspection**: the question "why did this cell activate DNA element X for this input?" is answered by reading the harness rules, not by reconstructing the cell's runtime trajectory. Third, expression **evolves through governed mechanisms**: changes to expression behavior are changes to harness substrate content, recorded as governance events, not adjustments hidden in code or model parameters.

The architectural treatment also supports a property Paper 2 commits to that is otherwise difficult to realize: **multi-aspect cell participation** per B1.17. The same cell can participate in multiple aspects with different active expression in each, by virtue of harness rules conditioning on aspect context. Without an explicit harness substrate, the only way to give one cell different active behavior in different aspects is to duplicate the cell, embed the differentiation in the cell's processing logic (which makes it implicit), or drive the differentiation from outside the cell (which violates the cell-internal architecture per B2.12). The harness substrate makes the relational property at expression scope architecturally available rather than reconstructed.

## 4. The biological analog, and where CKS exceeds it

The biological analog is direct. Biological cells do not express every gene every moment; they have regulatory mechanisms — transcription factors, chromatin states, signaling cascades — that determine which genes activate in which contexts. The work of Davidson and Levine on gene regulatory networks treats the genome as a static catalog and the regulatory state as what differs across cell types and developmental stages. In CKS, the DNA layer is the static catalog and the harness substrate is the regulatory state.

CKS exceeds biology at three points. Biological regulatory mechanisms emerged through evolution under fitness pressure and are not configurable on operational timescales; CKS harness substrates are configured by humans at cell birth per the cell's purpose and modified through directed selection. Biological regulatory state is not subject to inspect/modify/override authority by the organism's owners; CKS harness substrates are subject to those rights at all times. And biology has no separation between regulatory state and the genome it regulates beyond the molecular distinction; CKS treats the harness substrate and the DNA layer as architecturally distinct substrate components with separate governance semantics, separate evolution mechanisms, and separate provenance. The biological analog functions as conceptual scaffold readers absorb quickly because the parallel between *catalog plus regulator* and *DNA layer plus harness substrate* is intuitive. The architectural substance — governable substrate-resident expression determination under human authority — is CKS's own.

## 5. Inherited Paper 1 commitments

The harness substrate inherits Paper 1's commitments at full scope. It sits inside the substrate-cell boundary per A1.02, on the substrate side. It is substrate-resident per A1.08, with its content as part of the substrate's source-of-truth role. It is authoritative content per A2.46 Category 4 for activation determination. It is authored under A2.04, with humans holding authority while drafting labor may be allocated. Operations are recorded with A2.40's six provenance metadata fields. The three rights from A1.01 apply in their decomposed forms (A2.01 inspect, A2.02 modify, A2.03 override). Path retraceability per A1.07 covers harness rules and their changes. Where harness rule changes apply retroactively to interpretation of past activations, A6.02's retroactivity treatment carries through. The determinism contract per A1.10 holds at the harness substrate's scope: given fixed inputs and fixed harness rules, the activation decisions the harness substrate produces are deterministic; non-determinism enters only at the points the determinism contract permits it (LLM inference under A1.04 within the bounds A2.20 sets).

## 6. Operational implications

**Per-cell-purpose configuration at birth.** Deployments configure the harness substrate per cell purpose at cell birth, in the same governance posture as DNA-layer content. A cell created to handle one purpose receives harness rules tailored to that purpose; a cell created to participate in several aspects receives harness rules that condition on aspect context.

**Testability through inspection and replay.** Harness content is testable: a harness rule can be inspected directly, modified in a test substrate, and replayed against historical inputs to evaluate whether the modified rule would produce different activation decisions. The replay property follows from the determinism contract.

**Evolution through Paper 2 mechanisms.** Harness rules evolve through directed selection per B1.14 (human-deliberate modification with intent and outcome evaluated together) and may evolve through action-feedback per B1.15 (human-mediated proposal-and-approval informed by action-layer evidence). Both produce governance events with provenance.

**Multi-aspect support and high-stakes pinning.** Different active expression for the same cell in different aspect contexts is realized through context-aware expression rules conditioning on aspect membership; this operationalizes the relational property Paper 2 names at expression scope. When a deployment commits to architectural pinning of high-stakes decisions to the reasoning layer per B1.13, harness rules are part of how that pinning is operationally realized — they can require that for high-stakes inputs, cell processing route to DNA-specified behavior rather than instinct-routed behavior.

**Cross-partner authority and many-configuration deployments.** Where cells operate under cross-partner authority arrangements per A2.47, authority over harness rules follows the same authority distribution as authority over other orchestration content. Deployments typically run many cell types in parallel, each with its own harness configuration appropriate to its purpose; harness configurations are not globally uniform, and the architecture does not require them to be. Changes to any harness configuration are governance events recorded with provenance.

## 7. Limits

**Not DNA content.** The harness substrate does not contain the DNA-layer specifications themselves. DNA content is the catalog of behaviors per B2.25; harness content is the regulatory layer that selects from the catalog.

**Not action records.** The harness substrate does not contain action-layer records of what occurred when DNA met an actual task. Action content is per B2.26; harness content is what determines which DNA activates, not what happened after activation.

**Not processing logic.** The harness substrate is not the cell-internal processing logic that operates on activated DNA per A2.20. Processing operates on the DNA the harness substrate has determined to activate; the harness substrate is upstream of processing, not equivalent to it.

**Not implementation-prescribing.** The specification commits to operational content and governance posture, not to specific implementation technologies. A1.05 tool-agnosticism holds: any environment satisfying persistent structured state, human read/write access, and LLM access to substrate content can host harness substrate content.

**Not globally cell-uniform; not a meta-governance layer.** Different cells have different harness substrates; the specification commits each cell to having a harness substrate of the kind described, not to any global uniformity. The harness substrate is governed substrate content, not a meta-governance layer overriding cell-level commitments — cell-level governance applies to harness content as it does to other substrate content.

**Not the same as routing per B2.04.** B2.04's routing is the layer between instinct and reasoning that determines which layer handles a given input. The harness substrate operates within the reasoning layer, determining which DNA-layer elements activate once the input is in the reasoning layer's scope. Routing precedes harness; harness operates after routing has selected the reasoning path.

**Not a bypass of the substrate-cell boundary.** The harness substrate sits inside the A1.02 boundary on the substrate side. Harness operations may consult LLM capability per A1.04 only within the bounds A2.20 Property B sets — LLM-drafted rule content under human authority is admissible, LLM-committed rule content outside human authority is not.

## 8. Operational test

A system implements the harness substrate operational specification if and only if every cell has a substrate-resident component, located on the substrate side of the cell boundary, holding activation rules, carry-strategy configuration, expression conditions, input-to-expression mapping, and context-aware expression specifications, all subject to human authority for inspection, modification, and override at any time during the substrate's existence, with operations recorded under the path-retraceability and provenance commitments inherited from Paper 1, and with the determination of which DNA-layer elements activate for any input being a function of harness substrate content rather than of cell-internal processing logic, model parameters, or deployment-time hidden state.

A system that fails this test for any cell does not implement the harness substrate operational specification for that cell. Such a system may be useful and may govern other things in other ways; it is not implementing the architectural component Paper 2 commits to.

## 9. Why naming the specification as standalone matters

Naming the harness substrate's operational content explicitly is what lets subsequent Paper 2 derivations build on a fixed reference rather than reconstruct the harness substrate's role at each step. With the specification in place, B2.31 can decompose DNA activation patterns over the harness substrate this note specifies, B2.32 can decompose carry-strategy as a configuration choice the harness substrate implements, B2.33 can treat expression evolution as evolution of the harness substrate's content under Paper 2's evolution mechanisms, and B2.34 can verify that expression mechanism inheritance from Paper 1's commitments holds at the operational level the four prior notes establish. Phase B2 then continues to B1.08 modularity decomposition at B2.35.

Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "harness substrate" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Harness Substrate as Substrate-Resident Expression Determination Component in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
