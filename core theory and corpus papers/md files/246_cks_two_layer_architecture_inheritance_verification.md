# Two-Layer Architecture Inheritance Verification: Layer-Scope Application of Operational Tests Within Cell-Level Verification in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a standalone operational variant, the **layer-scope refinement of cell-level inheritance verification** — the application of Paper 1's operational tests at each of the two layers Paper 2 specifies within every cell (DNA and Action), with layer-distinct semantics, ensuring Paper 1's commitments hold for both layers individually rather than only for the cell as a whole.

## Abstract

Paper 2 specifies that within every cell, two architectural layers exist: a **DNA layer** carrying stabilized orchestration substrates and behavior substrates, and an **Action layer** carrying recorded task instances and their outputs. Both layers are substrate content; both are human-governed; but they do different work and evolve through different mechanisms. Paper 1's architectural commitments hold recursively at every level of Paper 2's architecture, including within the cell at layer scope. A separate decomposition note formalizes cell-level inheritance verification as the application of Paper 1's operational tests at cell scope. This note formalizes **two-layer architecture inheritance verification** as the layer-scope refinement of that verification: the same operational tests applied at each layer with layer-distinct semantics, plus cross-layer tests for properties spanning both layers, with the cell's pass condition requiring all layer-scope and cross-layer tests to pass. This is the closing note of the two-layers-within-every-cell decomposition.

## 1. Why two-layer architecture inheritance verification needs to be formalized as standalone

Paper 2 specifies that every cell carries two layers — DNA and Action — each substrate content, each human-governed, each performing distinct work. Earlier decomposition notes formalize each layer as standalone artifact, the separation mechanisms that keep them distinct, and the layer-level governance affordances that apply to each.

What remains underspecified is the operational consequence of Paper 1's inheritance promise at layer scope. Paper 2's continuity-with-Paper 1 commitment makes Paper 1's commitments **recursive** — they hold at the cell, at the aspect, at the Self, and within the cell at the layer level. A separate note formalizes cell-level verification as the application of Paper 1's operational tests at cell scope. But cell-level verification can pass while a layer-scope failure goes unnoticed: a cell may show acceptable inheritance properties in aggregate while one layer alone has gaps. The recursive-inheritance commitment, taken seriously, requires the tests run at layer scope as well, with semantics that reflect what each layer carries.

The remedy is to formalize **two-layer architecture inheritance verification** as a standalone operational variant: the same operational tests that constitute cell-level verification, applied within a cell to each of its two layers separately, with semantics adjusted to the layer's content type, and with cross-layer tests applied where they belong. Without layer-scope verification, the DNA/Action distinction is claimed architecturally but not testable as such; with it, the distinction becomes a verification target whose pass condition is definitive. This is the fifth and closing note of the two-layers-within-every-cell decomposition.

## 2. The verification, defined precisely

A CKS deployment instantiates **two-layer architecture inheritance verification** when, within the cell-level verification structure, the operational tests that apply to the cell are also applied independently at each layer with layer-adjusted semantics, and cross-layer tests are applied at the scope where their target properties live.

Cell-level verification, formalized separately, applies Paper 1's operational test specifications — inspect right, modify right, override right, rule authoring, mediator role, cell-behavior determinism, read determinism, provenance completeness, four accountability questions, source-of-truth-category coverage, conflict coexistence, reproducibility, among others — to the cell as the unit under test. Two-layer architecture inheritance verification refines this structure with three test categories.

**(a) DNA-layer verification semantics.** Tests applied to DNA content (rules, schemas, lifecycle policies, conflict-handling logic):

- Inspect-right: humans can read DNA content directly, without LLM intermediation as a precondition.
- Modify-right: DNA modification proceeds through the directed-selection mechanism Paper 2 names.
- Override-right: DNA-derived decisions can be overridden at any time without justification.
- Rule-authoring: orchestration rules embedded in DNA are human-authored or under human authority before they take effect.
- Cell-behavior-determinism: DNA produces deterministic cell behavior under the substrate-determinism contract.
- Source-of-truth-categories: DNA content fits the "what rules apply" category of the source-of-truth taxonomy.
- Reproducibility: DNA changes follow the retroactivity discipline that preserves prior DNA versions for reconstitution.

**(b) Action-layer verification semantics.** Tests applied to Action content (recorded task instances, outputs, lived experience):

- Inspect-right: humans can read Action content directly.
- Modify-right: Action records are protected against retroactive modification — override of derived decisions and authoring of new records is preferred to overwriting historical record.
- Read-determinism: Action reads return consistent results across read attempts.
- Provenance-completeness: Action records carry the full provenance metadata required by the path-retraceability commitment.
- Four-accountability-questions: Action provides who, what, when, and why for each recorded instance.
- Source-of-truth-categories: Action content fits the "what happened" and "what's the history" categories.
- Reproducibility: Action records replay deterministically under the same orchestration rules.

**(c) Cross-layer verification semantics.** Tests for properties that span both layers:

- Conflict-coexistence: conflicts at either layer — rule contradictions in DNA, recorded instance contradictions in Action — are registered as first-class substrate state, respecting Paper 1's conflict-preservation commitment.
- Mediator-role: LLM consultation respects the AI-as-substrate-mediator properties across both layers' involvement in cell operation.

The verification is governed under the broader human-governed authority architecture, and verification events are recorded under the path-retraceability commitment. Layer-scope verification operates *within* cell-level verification: both layers' tests, together with the cross-layer tests, must pass for the cell-level verification to pass in full.

## 3. What makes two-layer architecture inheritance verification distinctive

Conventional AI architectures often verify component-level properties without intra-component layer scope. Models are tested against benchmarks; runtimes against contracts; vector stores for retrieval relevance — verification operates at component granularity, not within it. This is appropriate where the component is the smallest architecturally distinct unit.

The CKS cell is not such a unit. Paper 2's two-layer specification names DNA and Action as architecturally distinct content types within the cell, with distinct work, distinct evolution mechanisms, and distinct governance shapes. The distinction is architectural, not merely organizational. Verifying it requires layer-scope test application.

The layer scope is what makes Paper 2's two-layer specification operationally demonstrable rather than only architecturally claimed. Without it, a deployment can satisfy cell-level tests by averaging out layer-specific failures, and the DNA/Action distinction becomes a labeling convention. With it, the distinction is a verification target — DNA and Action each pass or fail their applicable tests independently, and the cell's pass condition is the conjunction.

## 4. Inherited Paper 1 commitments at layer scope

The recursive-inheritance commitment makes Paper 1's commitments hold at every level of Paper 2's architecture, including the intra-cell layer level. Each commitment carries a layer-distinct operational meaning where the layer scope is informative.

**Substrate-based** is satisfied by construction at layer scope, since both layers are substrate content. **Human-governed** requires each layer to independently satisfy the inspect, modify, and override rights against layer-distinct content; the DNA layer additionally carries the orchestration-rule-authoring constraint, and the Action layer carries the record-protection constraint that prefers override and new authoring to retroactive overwriting. **Conflict-preserving** holds only when conflicts at every layer where they arise are registered as first-class substrate state. **AI-as-substrate-mediator** requires LLM consultation to respect the mediator properties across both layers' involvement in cell operation. **Tool-agnostic** requires both layers to be representable in any environment satisfying the three minimal requirements. **Linear-cost** holds at layer scope as it holds at cell scope.

Three commitments take specifically layer-distinct operational meaning. The **path-retraceability** commitment specifically operates on the Action layer, since Action records the lived task instances whose retraceability is being claimed. The **determinism** commitment applies to cell behavior given DNA, since DNA is what determines cell behavior under the determinism contract. The **source-of-truth-category** commitment maps differently across layers: "what happened" and "what's the history" map to Action; "what rules apply" maps to DNA.

## 5. Layer-distinct test semantics

The *test specifications* are the same across layers — drawn from one suite — but the *artifacts under test* differ in their content type and the test interpretations differ accordingly.

The inspect-right test at DNA scope inspects rules, schemas, and lifecycle policies; at Action scope it inspects recorded instances and outputs. The source-of-truth-categories test at DNA scope verifies "what rules apply" coverage; at Action scope it verifies "what happened" and "what's the history." The reproducibility test at DNA scope verifies retroactivity preservation across DNA versions; at Action scope it verifies replay determinism across Action records. Same test specifications, layer-distinct architectural artifacts under test.

There are not two separate verification frameworks for DNA and Action; there is one framework — the operational tests defined at cell scope — applied with layer-distinct interpretations. Paper 2's recursive-inheritance commitment is honored at intra-cell layer level via this single mechanism, without adding new tests beyond what Paper 1 already commits to.

## 6. Operational implications

**Per-cell-type configuration.** Different cell types carry different DNA shapes and accumulate different Action profiles; deployments configure layer-scope verification per cell type. Configuration parameters are themselves substrate state under the human-governed authority architecture.

**Verification at cell birth.** Both layers are verified at cell creation: DNA against its declared schema; Action as properly empty or properly initialized. A cell whose layers fail birth-time verification does not enter active substrate state.

**Verification at DNA modification.** When DNA is modified through the directed-selection mechanism, DNA-layer verification runs after the modification, and cross-layer tests rerun. The retroactivity discipline that preserves prior DNA versions is itself verified by the reproducibility test at DNA scope.

**Sampling at Action accumulation.** Action accumulates continuously; complete verification of every Action record at every step is operationally expensive. Deployments may sample Action records for ongoing verification with periodic full verification runs, provided the sampling regime is itself substrate state under human governance.

**Verification at action-feedback evolution.** When the action-feedback-evolution mechanism proposes DNA changes from Action evidence, four properties are verified: the DNA change is correctly applied; the Action evidence base is preserved; the new DNA produces expected behavior; layer separation is maintained. Action-feedback evolution is the only mechanism that crosses the layer boundary, and the verification structure recognizes its cross-layer character explicitly.

**Failure handling under governance.** Verification failures trigger governance under the broader authority architecture: an override corrects the immediate failure; a rule-authoring change addresses structural causes.

**High-stakes deployment relevance.** When a deployment handles high-stakes decisions, both DNA correctness (for behavioral pinning) and Action retraceability (for audit) become operationally critical. Two-layer verification is what demonstrates both architectural properties hold. When authority is distributed across organizational partners, layer-scope verification follows the authority distribution.

## 7. Limits

**It does not replace cell-level verification.** Layer-scope verification refines cell-level verification at finer scope, embedded within the cell-level structure; it does not substitute for it.

**It does not eliminate verification at other levels.** Aspect-level and Self-level verification each run independently at their scopes. Layer-scope verification within the cell is one slice of the broader recursive-inheritance requirement.

**It does not prescribe specific test parameters.** Sampling rates, coverage thresholds, retroactivity windows, and replay criteria are deployment configuration, not architectural commitments. The verification names what is verified and at what scope, not how parametrically.

**It does not guarantee behavioral correctness.** The tests verify architectural properties — inspectability, modifiability, override authority, retraceability, determinism, conflict preservation, source-of-truth-category coverage. They do not verify that the cell's outputs are correct in the domain sense.

**It is not a single test.** Layer-scope verification is the application of the full operational test suite at layer scope, with cross-layer tests at cross-layer scope. Reading two-layer verification as one new test added to the suite misreads its structure.

**It does not eliminate verification gates for instinct.** Instinct evolution operates through a separate verification mechanism — the verification-gate framework that evaluates LLM behavior under controlled conditions during instinct integration. That mechanism addresses the LLM, not the substrate's two layers.

## 8. Operational test

A deployment instantiates two-layer architecture inheritance verification if and only if all of the following are true at the time the verification structure is exercised:

1. The cell-level verification structure applies the operational test suite to the cell as the unit under test.
2. Each test that has layer-distinct artifact applicability is also applied at DNA scope, with DNA content as the artifact and the layer-distinct semantics named in §2(a).
3. Each test that has layer-distinct artifact applicability is also applied at Action scope, with Action content as the artifact and the layer-distinct semantics named in §2(b).
4. Tests that verify cross-layer properties — conflict coexistence across layers, mediator role across layers — are applied at the cross-layer scope explicitly, as named in §2(c).
5. The cell-level verification's pass condition requires all DNA-scope, all Action-scope, and all cross-layer tests to pass; layer-scope failures are not averaged into aggregate pass.
6. The verification is governed under the broader human-governed authority architecture, and verification events are recorded under the path-retraceability commitment.
7. Configuration parameters that operationalize the verification — sampling rates, test scopes, retroactivity windows, replay criteria — are themselves substrate content under the same authority architecture.

A deployment that fails any of (1)–(7) does not instantiate two-layer architecture inheritance verification, regardless of how robustly it instantiates cell-level verification in aggregate.

## 9. Conclusion

Two-layer architecture inheritance verification is the layer-scope refinement of cell-level verification. The operational tests that constitute cell-level verification are applied independently at each of the cell's two layers, with layer-distinct semantics that reflect the layer's content type, and with cross-layer tests for properties spanning both layers. All layer-scope and cross-layer tests must pass for the cell-level verification to pass in full. Without this structure, Paper 2's two-layer specification holds as architectural claim but not as operationally demonstrable property.

This note closes the two-layers-within-every-cell decomposition. The four earlier notes formalized the DNA layer, the Action layer, the separation mechanisms, and the layer-level governance affordances. This note formalizes the verification structure that demonstrates the inheritance. Subsequent decomposition notes turn to the **expression mechanism** — the harness substrate that selects which DNA-layer substrates activate for a given cell goal — and develop that mechanism as standalone with its own decomposition.

Subsequent work that implements, extends, or argues against the CKS two-layer architecture should use "two-layer architecture inheritance verification" in the sense formalized here. Subsequent work using the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Two-Layer Architecture Inheritance Verification: Layer-Scope Application of Operational Tests Within Cell-Level Verification in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
