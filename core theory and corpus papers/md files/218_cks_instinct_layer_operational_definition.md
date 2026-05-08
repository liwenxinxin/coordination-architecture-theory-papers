# Operational Definition of the Instinct Layer as the LLM in Its Bounded Mediator Role in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, in operational form, the precise meaning of the term **instinct layer** as the source paper uses it, so that the Phase B2 sequence of operational variants decomposing the instinct/reasoning separation can rest on a definition that is architecturally precise rather than metaphorically suggestive.

## Abstract

Paper 2's foundational architectural move is the separation of fast-pattern instinct from deliberate reasoning into independently-evolving layers within one CKS-governed AI Self. The term **instinct layer** is load-bearing: every Paper 2 commitment about mutation, verification gates, routing patterns, and high-stakes pinning depends on what the instinct layer concretely is. The term is also commonly read metaphorically — as a name for "the fast, intuitive part of the AI" — without architectural specification. This note formalizes the instinct layer as Paper 2 uses it: the LLM operating in its bounded mediator role per Paper 1's A1.04, with Properties A–E from A2.18–A2.23 bounding the layer's behavior, providing pattern-matched fast-path responses that the System 1 cognitive analog names but does not architecturally constitute. The note states the operational definition, distinguishes the precise operational reading from the loose metaphorical one, enumerates the inherited Paper 1 commitments that bound the layer, and gives an operational test for whether a system has correctly identified its instinct layer. It is the first of six notes decomposing Paper 2's instinct/reasoning separation.

## 1. Why a precise operational definition needs to be formalized

Paper 2 names the instinct layer in its overview as "the LLM — pattern-matched, fast-path, no-reasoning-needed responses analogous to human System 1 cognition." The naming carries the right architectural intuition: the LLM is one layer, reasoning is the other, the two evolve independently, and humans govern where the boundary sits. But for the Phase B2 sequence of operational-variant notes to decompose the instinct/reasoning separation precisely — across six notes that this one opens — the term "instinct layer" must be available with operational content sharper than its naming sentence on its own provides.

The misreading the precise definition preempts is not the dual-process analogy itself, which Paper 2 endorses as conceptual scaffold. The misreading is the slide from "instinct layer = the fast part of the AI" to "instinct layer = however the LLM happens to be deployed." Under the loose reading, any LLM call is an instinct-layer call, any LLM-mediated decision is an instinct-layer decision, and any LLM that maintains conversational state is the instinct layer maintaining that state. None of these readings is consistent with Paper 1's mediator-role specification, which Paper 2 inherits in full. The instinct layer is not the LLM doing whatever the LLM does. It is the LLM operating in a bounded role with five named properties.

This is also the first note of Phase B2. Phase B1's twenty foundational commitments are now in place; Phase B2 begins their operational decomposition into approximately one hundred and ten variants paralleling Series A's Phase A2 structure. B2.01–B2.06 jointly decompose B1.01 (the instinct/reasoning separation) into six operational variants: this note (operational definition of instinct layer), B2.02 (operational definition of reasoning layer), B2.03 (architectural test for separation), B2.04 (instinct-routing patterns), B2.05 (high-stakes decision identification), and B2.06 (verification gates for instinct). Each subsequent note rests on the precision the first establishes — without the operational definition pinned down here, the architectural test in B2.03 has no reference point, the routing patterns in B2.04 have no destination to route to or away from, and the verification gates in B2.06 have no specified surface to verify against.

## 2. The operational definition

In the CKS pattern as Paper 2 extends it, the **instinct layer** is the LLM operating in its bounded mediator role per A1.04, providing pattern-matched, fast-path, no-reasoning-needed responses to consultation requests issued by cells, with the layer's behavior bounded by Properties A through E specified at A2.18–A2.23.

The operational content of this definition has three components.

**(a) The instinct layer is the LLM.** Specifically, the instinct layer is the AI vendor's language model that the cell consults under A1.04's mediator-role specification. The instinct layer is not "the AI system." It is not "the part of the substrate that handles fast responses." It is not "the inference layer of any AI component." It is the LLM, identified specifically: the parametric model the cell calls when it issues a consultation, whose outputs flow back into cell processing under orchestration rules.

**(b) The layer provides pattern-matched, fast-path, no-reasoning-needed responses.** *Pattern-matched* names the recognition of patterns by the trained model without explicit reasoning steps. *Fast-path* names single-pass inference rather than iterative deliberation. *No-reasoning-needed* names outputs the model produces through its trained patterns rather than through explicit reasoning chains. These three terms together describe the kind of response the layer produces — the System 1 analog in dual-process cognitive theory — and distinguish it operationally from the explicit, deliberate, human-governed substrate processing that constitutes the reasoning layer.

**(c) The layer's behavior is bounded by Properties A–E.** The five properties from A2.19–A2.23 are inherited in full: Property A (consults but does not direct-write substrate), Property B (writes under orchestration rules when writes are warranted), Property C (does not hold substrate-relevant state outside substrate), Property D (consultation explicit, not ambient), and Property E (outputs recorded with attribution). The properties together are what make the layer specifically a *layer* rather than a *system*. Without them, the LLM expands to fill the architectural space — maintaining state, deciding directly, writing autonomously, operating ambiently — and the separation that Paper 2's foundational move depends on collapses.

The three components are jointly necessary. A deployment that identifies "the LLM" but does not enforce Properties A–E has identified a candidate but not the instinct layer. A deployment that produces fast-path responses through some other mechanism — a rule engine, a cached lookup, a non-LLM classifier — has produced fast-path responses but has not produced instinct-layer outputs in the CKS sense. The precise definition is conjunctive: LLM in bounded mediator role with Properties A–E, producing pattern-matched fast-path outputs.

## 3. What makes the precise operational definition distinctive

Conventional AI architectures — particularly the LLM-only deployments Paper 2 contrasts CKS Selves against — typically conflate the LLM with the system. The LLM *is* the AI; the LLM's outputs *are* the system's decisions; the LLM's training *is* the path by which the system improves. Under this conflation, the question "what is the instinct layer of this system" has no architectural answer, because the system has only one layer. CKS architectures break the conflation by specification: the LLM is not the system; the LLM is one layer of the system, with a name (instinct) and a bounded role (A1.04 plus Properties A–E). The bounded role is what makes the naming architecturally precise rather than merely cognitively suggestive.

Property C in particular — the prohibition on the LLM holding substrate-relevant state outside the substrate — is what most directly prevents the layer from silently re-expanding into the system. An LLM that maintains a long-running session memory of substrate-relevant decisions has begun to constitute a parallel substrate; an LLM whose context window is the only place where authoritative state lives has fully constituted one. Property C forbids both. The instinct layer's outputs flow into cell processing, are recorded with attribution per Property E, and become substrate state through whatever orchestration rules govern the write per Property B. The LLM itself holds no authoritative state about the deployment — it consults, produces, and is done. This is the architectural sense in which "instinct" is precise rather than metaphorical: the cognitive metaphor names the kind of cognition the layer performs; the architectural specification names what the layer is, what it can and cannot do, and where its boundary sits.

## 4. The cognitive analog as conceptual scaffold

Dual-process cognitive theory distinguishes System 1 (fast, automatic, pattern-based, low-effort) from System 2 (slow, deliberate, sequential, effortful). Paper 2 leans on this distinction explicitly: the instinct layer is the System 1 analog, the reasoning layer is the System 2 analog. The mapping is direct in shape — pattern-matched fast-path responses correspond to System 1's signature; explicit deliberate substrate processing corresponds to System 2's. The analog functions as conceptual scaffold readers absorb quickly, communicating the architectural shape without requiring a from-scratch explanation. This is the same role biology mimicry plays elsewhere in Paper 2.

The architectural substance, however, is the LLM-in-bounded-mediator-role specification, not the cognitive analog. The instinct layer is not literally a System 1 process; it does not have the neuropsychological signature of human fast cognition; it is not constrained by the failure modes of human heuristic reasoning. It is an LLM, with the failure modes LLMs have, in a role specification that bounds those failure modes architecturally. The cognitive analog points at the layer; the architectural specification *is* the layer.

This distinction matters for downstream notes. The architectural test in B2.03 — whether humans can correct AI behavior without modifying model weights or context — is a test against the architectural specification, not against the cognitive analog. The verification gates in B2.06 verify properties of the LLM-in-bounded-role, not properties of System 1 cognition as such. The mutation mechanism in B1.13 evolves the LLM through vendor model updates and infrastructure shifts, not through any process with a cognitive-analog reading. Throughout, the analog remains conceptual scaffold; the architectural substance carries the operational weight.

## 5. Inherited Paper 1 commitments operationally specifying the instinct layer

The instinct layer is operationally specified by inherited Paper 1 commitments. The inheritance is direct: Paper 2's hybrid commitment preserves Paper 1's mediator-role architecture in full, and the instinct layer is precisely the LLM in that mediator role, named under its Paper 2 architectural function.

**A1.04 (AI-as-substrate-mediator)** is the operational definition of the instinct layer. A system has identified its instinct layer when it has identified the LLM that cells consult under A1.04's specification.

**A2.18 (the integrating frame)** names what the LLM does in CKS architectures as a coherent role rather than as a collection of capabilities. **A2.19 (Property A: consults but does not direct-write)** routes the layer's outputs to substrate through cell processing rather than directly. **A2.20 (Property B: writes under orchestration rules)** keeps the write path human-governed even when the proximate cause is an LLM-produced output. **A2.21 (Property C: does not hold substrate-relevant state outside substrate)** prevents the layer from constituting a parallel authoritative store. **A2.22 (Property D: consultation explicit, not ambient)** makes instinct-layer consultations recordable, attributable, and bounded in scope. **A2.23 (Property E: outputs recorded with attribution)** makes the layer's contribution to substrate state retraceable per Paper 1's path-retraceability commitment.

**A2.62 (allowed non-determinism categories)** bounds the layer's behavioral non-determinism within named categories. The instinct layer is not deterministic in the strict sense; it is *bounded non-deterministic*, with the boundedness itself an architectural property rather than a deployment-by-deployment exception.

The eight commitments together operationally specify the instinct layer. The specification is fully inherited; this note does not extend Paper 1, only formalizes how Paper 1's mediator role becomes Paper 2's instinct layer under the new naming.

## 6. Operational implications

Several implications follow directly from the operational definition.

**Deployments identify the instinct layer concretely.** A deployment instantiating the CKS pattern in Paper 2's extended form must point, when asked, to the specific LLM that constitutes its instinct layer — vendor, model, version, deployment endpoint, or equivalent identifier. "The instinct layer" is not a place in the architecture diagram; it is a specific component whose behavior is bounded by Properties A–E. The layer is testable through A5.05 (the mediator-role test, in Series A), since the instinct layer is the LLM in the mediator role under its Paper 2 naming.

**Mutation evolution per B1.13 affects this layer specifically.** Of Paper 2's three evolution mechanisms (mutation, directed selection, action-feedback), mutation operates on the instinct layer — through LLM model updates, vendor changes, and substrate-platform infrastructure shifts. Directed selection (B1.14) and action-feedback (B1.15) operate on the DNA layer of cells, which is reasoning-layer content. Mutation is the instinct layer's evolution mechanism specifically, and its undirected character is bounded by the verification, routing, and high-stakes pinning that B2.06, B2.04, and B2.05 will formalize.

**The instinct layer cannot become authoritative for deployment state.** Property C protection is architectural, not procedural. A deployment cannot satisfy the operational definition while also relying on the LLM's context window or session memory as the authoritative location for any substrate-relevant state. If state lives in the LLM, it does not live in the substrate; if it does not live in the substrate, the reasoning layer cannot reason over it under human governance; if the reasoning layer cannot reason over it, the separation has collapsed.

**Outputs flow through cell processing, not directly to substrate.** Property A makes the cell — reasoning-layer-resident processing logic — the integration point between instinct outputs and substrate state. The instinct layer produces an output; the cell processes the output under orchestration rules; the substrate receives whatever write the cell's processing produces. This three-step path is what every instinct-layer contribution to substrate state traverses; it is not optional. Per A2.62 and Property E, the layer's behavioral non-determinism is bounded in kind and recorded in instance.

## 7. Limits

Stating what the operational definition does not extend to is what keeps the standalone treatment from drifting into something stronger than the source paper supports.

**Substrate, cell processing, and orchestration rules are not part of the instinct layer.** The substrate is the reasoning layer per B2.02. The cell's processing logic — orchestration rule application, conflict handling, write decisions — is reasoning-layer work that mediates instinct-layer outputs; the instinct layer ends at the LLM's output and cell processing begins after. Orchestration rules are substrate-resident, human-authored content; they govern instinct-layer consultation and output handling but are not themselves part of the instinct layer.

**The instinct layer is not optional.** Paper 2 is explicit on this point: the LLM instinct layer is essential at every scope, and Paper 2 is not a replacement for LLM-based AI. The operational definition makes the essentiality precise — what the LLM is in CKS architecture, not whether the LLM is present at all.

**The instinct layer does not process state.** It processes consultation inputs and produces outputs. State processing — reading substrate, writing substrate, resolving conflicts, applying rules — is reasoning-layer work.

**The definition does not prescribe specific LLM vendors or models.** A1.05 tool-agnosticism holds. Any LLM that satisfies Properties A–E in the deployment's mediator-role configuration constitutes the instinct layer for that deployment. The operational definition specifies the role, not the occupant.

## 8. Operational test

A system has correctly identified its instinct layer if and only if all of the following are true:

1. The layer is concretely identifiable as the LLM (vendor model, version, endpoint, or equivalent specifier) that cells consult under A1.04's mediator-role specification.
2. The layer's outputs do not directly write substrate; outputs flow to substrate through cell processing under orchestration rules (Property A; A2.19).
3. When writes attributable to layer outputs do occur, they occur under orchestration rules that humans author and govern (Property B; A2.20).
4. The layer holds no substrate-relevant state outside substrate; the LLM's context window, session memory, or any other LLM-resident store is not the authoritative location for any deployment state (Property C; A2.21).
5. The layer is consulted explicitly by cells, not ambiently as an always-on observer (Property D; A2.22).
6. The layer's outputs are recorded with attribution sufficient to retrace which model produced what output on what input under what consultation (Property E; A2.23).
7. The layer's behavioral non-determinism falls within the categories A2.62 allows, and the non-deterministic outputs are recorded as in (6).

A system that fails any of (1)–(7) has not identified an instinct layer in the CKS sense, regardless of how prominently an LLM features in its architecture.

## 9. Conclusion

The operational definition transforms a cognitive metaphor into an architectural specification. The metaphor — System 1 cognition, fast and pattern-based — communicates the layer's shape quickly. The specification — the LLM in its bounded mediator role per A1.04 with Properties A–E from A2.18–A2.23 — gives the layer its operational content, its testable boundary, and its inheritance from Paper 1.

Naming the instinct layer as standalone operational variant is what makes the rest of Phase B2's work on B1.01 possible. B2.02 will articulate the reasoning-layer counterpart with parallel precision. B2.03 will give the architectural test for the separation as a whole — whether humans can correct AI behavior without modifying model weights or context — and that test rests on identifying both layers correctly. B2.04 will formalize routing patterns that direct cell consultation toward instinct or reasoning depending on stakes and substrate state. B2.05 will identify the high-stakes decision class that orchestration rules pin to reasoning regardless of how capable the instinct layer becomes. B2.06 will specify the verification gates through which instinct-layer outputs are checked when the deployment's risk profile warrants verification. Each subsequent note assumes the precision this one establishes.

Subsequent work that adopts, extends, or argues against the instinct/reasoning separation in CKS-governed AI Selves should use "instinct layer" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Operational Definition of the Instinct Layer as the LLM in Its Bounded Mediator Role in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
