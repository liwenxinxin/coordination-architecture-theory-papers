# DNA Layer Operational Specification: Decomposing the Two-Layer Cell Architecture by Formalizing the DNA Layer as Substrate-Resident Stabilized Behavioral Specification

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 8 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one operational variant of the two-layer cell architecture from the source paper — the **DNA layer's operational specification** — as having independent operational content separable from the action layer with which it composes.

## Abstract

Paper 2 commits every cell to a two-layer internal architecture: a DNA layer that holds the cell's stabilized behavioral specification, and an action layer that records the cell's actual task instances and their outputs. The two-layer commitment is load-bearing for Paper 2's lifecycle and evolution machinery — mating combines layers, expression activates DNA elements, evolution refactors DNA, action-feedback closes a loop from action layer back into DNA refinement. This note formalizes the DNA layer specifically: what it carries operationally (orchestration substrates, behavior substrates, harness logic, schemas, lifecycle policies), where it sits relative to the substrate-cell boundary, what governance affordances apply, what evolution mechanisms operate on it, what it is not, and what test a system must pass to instantiate it. The note opens a five-note decomposition of the two-layer commitment.

## 1. Why the DNA layer needs to be formalized as standalone

Paper 2 commits every cell to a two-layer architecture: every cell has a DNA layer and an action layer, both substrate content, both human-governed, but doing different work and evolving through different mechanisms. The joint commitment is correct as far as it goes, and this note does not contradict it. But the joint framing leaves a class of cases architecturally underspecified.

Several of Paper 2's central machineries operate on the DNA layer specifically rather than on the cell as a whole. Mating combines DNA in the genetic sense and action in the epigenetic and cultural sense — different operations. Directed selection refactors DNA without touching action history. Verification substrates verify behavior compatibility against the DNA's specification, not against accumulated action records. Pinning of high-stakes decisions targets the DNA's substrate-resident rule content, not the cell's instinct-pattern outputs. If the DNA layer is treated only as one half of a composite property, each machinery has to re-specify what content it operates on, and the architectural object that all of them share has no standalone vocabulary.

The remedy is to name the DNA layer as a standalone architectural object with independent operational content. Once named, it becomes the consistent target for evolution, verification, pinning, birth-time configuration, and mating's genetic-mode combination. Naming it explicitly prevents the slide where DNA-layer content becomes scattered across implementation artifacts (configuration, code, weights, middleware) without unified architectural treatment.

## 2. The DNA layer, defined precisely

In the CKS pattern as extended by Paper 2, the **DNA layer** of a cell is the substrate-resident content holding the cell's stabilized behavioral specification — the stable specification of what the cell does, distinct from any record of what the cell has done. The DNA layer has five operational content categories.

**(a) Orchestration substrates.** Rules specifying how the cell processes inputs, how it routes consultation to the instinct layer when consultation is permitted, how it integrates instinct outputs with substrate-resident processing, and how conflicts encountered during processing are handled per the conflict-preservation commitment.

**(b) Behavior substrates.** Rules specifying how the cell behaves for specific input conditions — what outputs are produced, what conflict-handling applies for which scenarios, what defaults govern when input conditions are underspecified. Behavior substrates carry the conditional content that gives the cell its stable behavioral character.

**(c) Harness logic.** Rules per Paper 2's expression mechanism that determine which DNA elements activate for which inputs and which cell goals. The harness substrate is itself DNA-layer content — the specification of expression sits in the same authoritative substrate as the content being expressed.

**(d) Schemas.** Input and output schemas, data type specifications, and validation rules that govern what the cell accepts and produces. Schemas are part of the DNA layer because they are stabilized behavioral specification — they specify how the cell behaves with respect to data shape, not data values.

**(e) Lifecycle policies.** Rules specifying how the cell handles birth events (initial DNA configuration), death conditions, mating eligibility, and other lifecycle-stage transitions. Lifecycle policies are DNA-layer content because they specify behavioral character with respect to the cell's life stages, not because they record stage events that occurred.

These five categories together are the cell's stable behavioral specification, held as one named substrate-resident unit for governance purposes.

The DNA layer is **substrate-resident** per the substrate-cell boundary commitment: all DNA content sits on the substrate side, not in LLM parametric memory, not in adjacent agent-framework runtime, not in vendor-managed platform layers. It is **authored by humans** in the rule-authoring sense (LLM-drafted rules subject to human authority before they take effect being admissible). It is **inspectable, modifiable, and overridable** under the three rights from Paper 1's human-governed commitment. It is **stable**: it specifies the cell's behavioral character that persists across operations, evolving only through the mechanisms named in §4, not drifting silently with each task instance. It is **distinct from the action layer** that pairs with it: the DNA layer holds *specification*, the action layer holds *history*. This split is what allows the two layers to evolve through different mechanisms and to be combined differently in mating.

## 3. What the DNA layer is NOT

Stating precisely what the DNA layer is not is what keeps the standalone framing from drifting into something stronger than the source paper supports.

**Not action-layer content.** The DNA layer holds behavioral specification, not records of task instances. Recorded task inputs, recorded task outputs, recorded conflict-handling outcomes, and accumulated lived experience belong in the action layer.

**Not execution state or runtime data.** The DNA layer is specification, not the runtime state of an executing operation. A cell's current step, current intermediate values, current LLM consultation in flight, and the application-layer data flowing through the cell during operation are not DNA-layer content. Such content sits at the action layer when recorded, or in transient operation state when not yet recorded; either way, it is not specification.

**Not implementation-prescribing.** The DNA layer specifies the cell's behavioral character; it does not prescribe specific implementation technologies. Tool-agnosticism from Paper 1 holds — the DNA layer can be expressed in any persistent structured representation the host environment supports. Specific rule-engine products, behavior-tree frameworks, or AI-platform features may all be admissible carriers; none is architecturally privileged.

**Not static across the deployment lifecycle.** The DNA layer is stable in the operational sense — it specifies behavior that persists across operations — but it is not frozen. It evolves through the governed mechanisms named in §4. "Stable" here distinguishes specification from operation-by-operation drift, not from governed change over time.

**Not cell-specific globally.** Different cells have different DNA. The DNA layer is a per-cell architectural object; the Self-level question of how DNA composes across cells is the subject of Paper 2's lifecycle and expression machinery, not of the per-cell specification given here.

**Not the harness substrate as a separate concept.** The harness logic that determines DNA expression is itself DNA-layer content, not a separate substrate alongside the DNA layer. The expression mechanism pairs with the DNA layer; the harness substrate that implements expression sits inside the DNA layer as one of its content categories.

## 4. The DNA layer's evolution mechanisms

The DNA layer is stable but not frozen. Two evolution mechanisms operate on it, both human-governed.

**Directed selection.** Humans deliberately modify the DNA layer based on improvement goals — adding a new behavior substrate, refining an orchestration rule, tightening a schema, adjusting a lifecycle policy. Directed selection is governed through Paper 1's standard authority architecture: rule authoring at design time, override at intervention time. Its trajectory is predictable and its outcome is evaluable by intent and outcome together.

**Action-feedback evolution.** Humans modify the DNA layer based on proposals derived from accumulated action-layer evidence. The mechanism is human-mediated rather than automatic: substrates may propose DNA changes from action-evidence patterns, but the proposals are reviewed by humans before integration. This closes the loop from action layer back to DNA layer while preventing the action layer from silently drifting the DNA over time.

A third evolution mechanism — undirected mutation — operates on the instinct layer (the LLM and supporting infrastructure) external to the cell, not on the DNA layer. Naming the DNA layer's evolution mechanisms specifically distinguishes them from instinct mutation and clarifies which evolution machinery touches DNA content.

DNA-layer changes follow Paper 1's rule-retroactivity treatment: historical DNA versions are preserved, with new DNA applying forward from the change point. DNA-layer events are recorded with the substrate's standard provenance metadata — what content existed, what changed, when, by whom, under what rule — so that DNA history is itself inspectable.

## 5. What makes the DNA layer architecturally distinctive

Conventional AI architectures often have implicit behavioral specification. A cell-equivalent component's processing logic sits in configuration files, source code, trained model weights, or runtime middleware — present in the system but not present as named, located, governable substrate content. Behavior changes happen by editing configuration, deploying new code, retraining, or reconfiguring middleware. The behavior is real, but the *specification of the behavior as a substrate-resident architectural object* is absent.

The CKS DNA layer makes the cell's stable behavioral specification explicit substrate-resident content — named, located, governable. This is consequential at the architectural layer. Because DNA is substrate content with standard provenance, any change to behavioral specification leaves a record — there is no equivalent of an undocumented configuration drift or an opaque retraining update. Because DNA is inspectable, the cell's behavioral character is verifiable by reading the DNA layer directly, not by depending on the LLM's self-reports. Because DNA changes go through directed selection or human-mediated action-feedback, the cell's behavior cannot evolve outside human authority.

The biological analog is direct. Biological DNA holds stable specification for cell behavior; the CKS DNA layer parallels it. Where CKS exceeds biology is in the directed-selection mechanism alongside undirected variation, and in human governance over the specification rather than evolutionary process operating without authority. The analog provides scaffold; the architectural substance is governable substrate-resident specification.

## 6. Inherited Paper 1 commitments

The DNA layer inherits Paper 1's foundational commitments wholesale: the substrate-cell boundary places DNA inside the cell on the substrate side; the substrate-as-source-of-truth status applies to DNA directly, making it authoritative for "what rules apply" to the cell; rule authoring grounds DNA content in human authorship (with LLM-drafted DNA subject to human authority being admissible); the standard six-field provenance metadata records DNA changes; the inspect, modify, and override rights apply to DNA with no architectural gating compromising any of the three; path retraceability preserves DNA history as substrate content; the rule-retroactivity treatment governs how DNA changes propagate (forward from the change point, with historical versions preserved); and the determinism contract holds — given a specific DNA configuration and a specific input, the cell's specified behavior is deterministic, with allowed non-determinism sitting at the LLM-consultation layer rather than at the DNA layer. These inherited commitments make the DNA-layer specification recursive on Paper 1: every Paper 1 substrate property holds for DNA content as a special case.

## 7. Operational implications

Several operational implications follow directly from naming the DNA layer as standalone. Cells configure their DNA per their intended purpose at birth; deployments may carry many DNA configurations simultaneously across their cell populations. DNA content is testable through direct inspection and through replay of operations against specific DNA versions. DNA is the pinning target for high-stakes decisions: when pinning is applied, the cell processes through DNA-specified rules rather than through instinct-pattern outputs alone. DNA is the verification baseline: when verification gates run during instinct-layer changes (LLM upgrades, infrastructure migrations), they verify that cell behavior remains compatible with the DNA's specification. When a deployment has cross-partner authority structures, specific DNA elements may need cross-partner authority for modification. Action-feedback proposals for DNA changes are themselves substrate content under inspection, with human review exercised under the standard three rights.

These implications follow from treating the DNA layer as having independent operational content under the inherited Paper 1 governance architecture.

## 8. Operational test

A system instantiates the DNA layer specifically if and only if all of the following are true at all times during the cell's existence:

1. The cell's stabilized behavioral specification — orchestration substrates, behavior substrates, harness logic, schemas, and lifecycle policies — exists as named, located, substrate-resident content within the cell, on the substrate side of the substrate-cell boundary.
2. A human with appropriate access can read the DNA content directly, in inspectable form, without LLM intermediation as a precondition.
3. A human with appropriate access can modify the DNA content, with the change taking effect as substrate state and recorded with the standard provenance metadata.
4. The DNA layer is distinguishable from the action layer in the system's representation: specification content and history content are not commingled in a way that prevents either from being addressed independently.
5. DNA changes are propagated under rule-retroactivity treatment: historical DNA versions are preserved, and new DNA applies forward from the change point.
6. The cell's behavior, given a specific DNA configuration and a specific input, is deterministic in the sense Paper 1 commits to; allowed non-determinism sits at the LLM-consultation layer when consultation is permitted, not at the DNA layer.
7. No LLM operation, vendor policy, or runtime middleware can in principle prevent (1)–(6) for authorized humans.

A system that fails any of (1)–(7) does not implement the DNA layer specifically, even if it satisfies other Paper 2 commitments in some form. Such a system is not Paper-2-coherent on the DNA-layer axis, and downstream work that relies on its DNA-layer guarantees should be scoped accordingly.

## 9. Conclusion

Treating the two-layer cell architecture as a single composite property makes the DNA layer's role in evolution, verification, pinning, and mating's genetic-mode combination difficult to describe architecturally and tempts implementers to scatter behavioral specification across diverse runtime artifacts (configuration, code, weights, middleware) without a unified treatment. Naming the DNA layer as standalone architectural object — substrate-resident, named, located, governable — gives downstream implementers a precise specification of what their cell's behavioral content must satisfy, independent of how the action layer that pairs with it is handled.

The note opens a five-note decomposition of the two-layer commitment. The action layer is formalized in the next note. The note after that formalizes the operational mechanisms by which the two layers remain separable in practice. The fourth note formalizes the layer-level governance affordances. The fifth note verifies that the two-layer architecture inherits all of Paper 1's substrate commitments. Subsequent Phase B2 notes then turn to the expression mechanism.

Subsequent work that implements, extends, or argues against the CKS DNA layer commitment should use "the DNA layer" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *DNA Layer Operational Specification: Decomposing the Two-Layer Cell Architecture by Formalizing the DNA Layer as Substrate-Resident Stabilized Behavioral Specification.* 8 May 2026. ORCID: 0009-0004-8065-3235.
