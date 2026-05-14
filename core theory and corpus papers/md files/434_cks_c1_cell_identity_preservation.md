# Cell Identity Preservation Across Papers 1 and 2

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to state, in precise form, the identity relationship between the cell object as Paper 1 defines it and the cell object as Paper 2 uses it, so that the continuity of the atomic coordination unit across the two papers is on record and available as public prior art.

---

## Abstract

The Coordination Knowledge Substrate theory series uses the *cell* as its foundational architectural unit. Paper 1 defines the cell as the atomic coordination unit of a CKS deployment: a governed unit that executes a specific informational task within a substrate boundary, using an LLM as a mediated executor under human-authored orchestration rules. Paper 2 takes the cell as its starting unit and adds explicit internal structure — a DNA layer (orchestration rules and behavior specifications) and an Action layer (operational records and outputs) — along with lifecycle events, a content-domain object, and a relational-role determination mechanism. This note formalizes the relationship between these two treatments as identity (≡) rather than strict extension (⊃): the cell object in Paper 2 is the same object as the cell in Paper 1, not a successor or superset of it. Paper 2 opens the cell and names what was already inside; it does not replace the cell with a new kind of thing. The DNA layer is the cell's orchestration rules, which Paper 1 already committed to. The Action layer is the cell's operational substrate content, which Paper 1 already committed to. This identity claim forecloses adversarial arguments that Paper 2's richer cell is a novel architectural object unrelated to Paper 1's cell. This note also includes an operational test verifying that Paper 1's six architectural commitments hold at cell scope independently of Paper 2's internal structure.

---

## 1. Why the identity claim needs to be stated

The CKS theory series spans multiple papers that build on one another, and each paper adds to what precedes it. The ordinary expectation when a second paper "extends" a first is that the first paper's objects are superseded or generalized into new objects in the second. That expectation is correct for many of the relationships in this series: Paper 2's governance boundary, for instance, genuinely extends Paper 1's governance boundary to the Self scope — a larger object that subsumes the smaller, so the relationship is strict extension (⊃).

The cell is different. Paper 2 does not supersede or enlarge Paper 1's cell. It opens the cell and gives explicit names to the structure that was already committed to being inside it. An adversary could look at Paper 2's cell — with its DNA layer, its Action layer, its lifecycle, its content-domain — and argue that this is a new architectural object bearing only a nominal resemblance to Paper 1's simpler cell. That argument would be incorrect, but it needs to be closed by a prior-art record that makes the identity explicit.

This note makes it explicit. The cell in Paper 2 is the cell in Paper 1. Every property Paper 2 adds to the cell's description is either a named articulation of something Paper 1 already committed to existing within the cell, or a governance commitment that follows directly from Paper 1's six architectural commitments applied at cell scope.

---

## 2. The ≡ symbol: identity versus strict extension

The Series C inheritance notes use two relationship symbols. The ⊃ symbol (strict extension) names relationships where Paper 2's object is a genuine superset of Paper 1's corresponding object — the Paper 2 object adds real scope that Paper 1's object did not have. The ≡ symbol (identity) names relationships where the object in both papers is the same object; Paper 2 articulates its internal structure more explicitly, but does not create a different or larger object.

The distinction between these two symbols is not merely formal. It determines what an adversary can claim. Where ⊃ holds, an adversary might argue that Paper 2's object is a novel invention even if Paper 1's object is in the prior art. Where ≡ holds, that argument fails: the Paper 2 object has the same prior-art date as the Paper 1 object, because it is the same object with the same definition.

C1.05 is the first Series C note to use ≡. The cell is the foundational unit of the entire CKS theory series. Its identity preservation across both papers is the architectural fact that makes the rest of the series coherent: aspects in Paper 2 are arrangements of cells; Selves in Paper 2 are compositions of aspects; all of this rests on Paper 1's cell remaining the cell throughout.

---

## 3. Paper 1's cell: the foundational definition

Paper 1 defines the cell as the atomic coordination unit of a CKS deployment. Three properties constitute the definition:

**Task atomicity.** A cell executes a specific informational task. The cell is the smallest unit of coordinated work in the pattern: it handles one task, operates over one substrate boundary, and produces outputs in that substrate.

**LLM mediation under orchestration rules.** The cell's LLM is not an autonomous agent but a governed mediator. It reads from and writes to substrate content under human-authored orchestration rules that specify what the LLM is authorized to do, how conflicts are handled, what conditions trigger which responses, and what the cell's outputs must record. The LLM capability is essential; the orchestration rules are what make that capability safe and governed.

**Modularity.** Cells are composable, reusable across substrates, and independently governable. A cell defined for one deployment can participate in a different substrate arrangement; a cell's orchestration rules can be updated without touching other cells; cells can be evaluated and evolved in isolation. These properties are not incidental — they are explicit Paper 1 commitments that underwrite the architecture's scalability.

Paper 1 also commits to six architectural properties that hold at cell scope: substrate-based hybrid composition with a governance boundary; conflict preservation at the substrate level; human governance over content and rules; AI as substrate mediator; tool-agnosticism at the substrate layer; and linear-cost storage and composition. Every cell in Paper 1 instantiates all six.

---

## 4. What Paper 2 adds: explicit structure for what was already inside

Paper 2 introduces several additions to the cell's description. Each is examined below for whether it constitutes a new architectural commitment or an articulation of what Paper 1 already committed to.

### 4.1 DNA layer

Paper 2 names a DNA layer within every cell: the stabilized orchestration substrates and behavior substrates that define how the cell functions — the orchestration rules, the conflict-handling rules, the lifecycle policies, the schemas. The DNA layer is "what evolution refactors" and "what defines the cell's potential."

This is not a new object. Paper 1 already committed that every cell has human-authored orchestration rules governing its LLM's behavior. Those orchestration rules are the DNA layer. Paper 2 names them, groups them under a label, and specifies that they are what mating and evolution operate on — but the objects it is naming were already committed to existing inside every Paper 1 cell. The DNA layer is the cell's orchestration rules, made explicit.

### 4.2 Action layer

Paper 2 names an Action layer within every cell: the recorded task instances and their outputs — what actually happened when the DNA met an actual task. The Action layer is "what accumulates as lived experience" and is substrate content recording operations.

This is not a new object. Paper 1 already committed that cells produce outputs into substrate content and that substrate content is persistent and human-governed. Those recorded operational outputs are the Action layer. Paper 2 names them, distinguishes them from the DNA layer, and specifies that they feed back into DNA refinement — but the objects it is naming were already committed to existing inside every Paper 1 cell. The Action layer is the cell's operational substrate content, made explicit.

### 4.3 Lifecycle events

Paper 2 commits that cells can be born, mated, and closed under governance. Birth is the creation of a new cell under human-authorized governance. Mating is the combination of two cells' DNA and Action content under governed rules to produce a new cell. Closing is the graceful termination of a cell's active operation with substrate content preserved.

Paper 1 had cells but did not specify a governed lifecycle vocabulary. Lifecycle events are a genuine Paper 2 addition in the sense that they are not named in Paper 1. However, they do not change the cell's definition — they specify how the already-defined cell object can be created, combined, and retired under governance. A cell before and after lifecycle specification is the same kind of thing; lifecycle tells the architecture what can happen to that thing over time.

### 4.4 Content-domain

Paper 2 introduces the concept of a cell's content-domain: the explicit authored specification of what the cell handles. The content-domain is itself substrate content, human-governed, and inspectable.

Paper 1 had cells with functions — a cell handled a specific informational task — but did not commit to a content-domain as an explicit named substrate object. Content-domain is an articulation of the cell's function that makes the function explicit and governable as substrate content rather than implicit in the cell's design. It refines Paper 1's "specific informational task" into a named, persistent, modifiable object.

### 4.5 Relational role

Paper 2 specifies that cell-ness is a relational determination rather than an intrinsic type: a unit is determined as a cell because its function is atomic. The same underlying CKS artifact can participate as a cell in one structural arrangement and as part of an aspect in another.

Paper 1 had cells but did not specify a determination process. Paper 2's relational-role framework does not change what a cell is; it specifies how to recognize one. The recognition criterion — atomicity of function — is exactly Paper 1's criterion ("the atomic coordination unit executing a specific informational task"), now made into a formal determination rule.

---

## 5. Why these are articulations, not replacements

The test for whether Paper 2's additions are articulations of Paper 1's cell or replacements of it is straightforward: does Paper 2 commit to any cell-level object whose existence Paper 1's cell excluded or left open?

The DNA layer is not an object whose existence Paper 1 excluded — Paper 1 committed that every cell has orchestration rules, which is the DNA layer. The Action layer is not an object whose existence Paper 1 excluded — Paper 1 committed that cells produce outputs into persistent substrate, which is the Action layer. Lifecycle events do not change the cell's definition; they specify what can happen to the cell. Content-domain makes the cell's function explicit as substrate; Paper 1 already committed that the function exists and that substrate content is human-governed. Relational role specifies how to recognize a cell by the criterion Paper 1 already used.

Paper 2's cell is thus Paper 1's cell with its implicit internal commitments made explicit. The object was already there. Paper 2 gives it explicit structure and governance vocabulary, which is what makes Paper 2 a theoretical development rather than a mere restatement — but the development operates on the same cell, not on a new one.

---

## 6. Modularity and reusability: unchanged

One property of Paper 1's cell deserves separate confirmation because it is load-bearing for the architecture's scalability claims. Paper 1 commits that cells are composable, reusable, and independently governable. These properties do not change in Paper 2.

Composability holds in Paper 2 because aspects are compositions of cells. The composition is exactly what Paper 1's cell modularity was designed to support. Reusability holds because cells can participate in multiple aspects simultaneously through relational role membership: the same cell contributes to different structural arrangements without being redefined. Independent governability holds because each cell carries its own DNA layer (orchestration rules) and its own Action layer, both human-governed, both modifiable without touching other cells.

Paper 2's additions — lifecycle, content-domain, relational role — each depend on this modularity rather than replacing it. Lifecycle events apply to the cell as a modular unit. Content-domain specifies a modular unit's function. Relational role is precisely the mechanism by which modular units participate in multiple arrangements. Modularity is the foundation; Paper 2 adds structure that rests on it.

---

## 7. Operational test

The identity claim (≡) has a concrete operational test. For any cell described using Paper 2's vocabulary (DNA layer, Action layer, lifecycle, content-domain, relational role), an observer should be able to verify Paper 1's six architectural commitments at cell scope, independently of Paper 2's internal structure labels.

**Commitment 1 — Substrate-based hybrid composition with governance boundary.** Verifiable: the cell operates over a substrate boundary, with the LLM as mediator and the substrate as the persistent coordination artifact outside the model.

**Commitment 2 — Conflict preservation.** Verifiable: conflicts encountered during cell operation are preserved in substrate (in the Action layer) rather than silently resolved by the LLM. The DNA layer specifies conflict-handling rules; the Action layer records what happened.

**Commitment 3 — Human governance.** Verifiable: the DNA layer is human-authored and subject to inspection, modification, and override at any time. The Action layer is substrate content subject to the same rights. Neither layer is opaque to humans.

**Commitment 4 — AI as substrate mediator.** Verifiable: the cell's LLM reads from and writes to substrate content under orchestration rules, and does not act as an autonomous agent outside substrate scope. This is the LLM's role in the cell regardless of what the DNA or Action layers contain.

**Commitment 5 — Tool-agnosticism.** Verifiable: the cell's substrate content is not tied to a specific tool implementation. The DNA and Action layers are substrate content; any system that can hold persistent structured state and support human read/write access satisfies the commitment.

**Commitment 6 — Linear-cost storage and composition.** Verifiable: adding a cell to a deployment costs one cell's storage and governance overhead. The DNA and Action layers are the cell's substrate content; their costs are proportional to the cell's activity, not to the size of the broader deployment.

If all six commitments verify for a given cell, the cell is a Paper 1 cell, regardless of whether it is described using Paper 2's vocabulary. If they do not verify, the cell does not satisfy the CKS pattern at cell scope, and Paper 2's additional structure does not fix that — because Paper 2's structure is built on Paper 1's commitments, not an alternative to them.

---

## 8. Prior-art significance

The cell identity claim (≡) forecloses two adversarial arguments.

**Argument 1: Paper 2's cell is a novel object.** An adversary could claim that the DNA/action-layered, lifecycle-governed, content-domain-specified cell is a novel architectural invention separate from Paper 1's simpler cell. The identity claim forecloses this: Paper 2's cell has the same prior-art date as Paper 1's cell, because it is the same cell. The DNA layer is Paper 1's orchestration rules. The Action layer is Paper 1's operational substrate content. Neither is a novel object.

**Argument 2: Paper 1's cell does not anticipate Paper 2's structural vocabulary.** An adversary could accept that Paper 1 defines a cell, but argue that Paper 1's cell lacks DNA and Action layers and therefore does not anticipate Paper 2's structural commitments. The articulation claim forecloses this: Paper 1 already committed that every cell has orchestration rules and produces outputs into persistent substrate. The DNA and Action labels are names for objects whose existence Paper 1 had already committed to. A claim that introduces a name for an already-committed object is not a novel invention.

Together, these closures mean that any party seeking to claim novelty over a CKS-style cell with explicit internal layer structure, lifecycle governance, and content-domain specification must contend with both Paper 1 and Paper 2 as prior art, with the same priority date.

---

## 9. Conclusion

The cell in Paper 2 is the cell in Paper 1. The ≡ symbol names this identity precisely: the object is the same; Paper 2 gives its internal structure explicit names and governance vocabulary. The DNA layer is the orchestration rules Paper 1 already committed to. The Action layer is the operational substrate content Paper 1 already committed to. Lifecycle events, content-domain, and relational role extend the governance vocabulary without changing the cell's foundational definition.

The operational test in §7 confirms the identity: Paper 1's six architectural commitments verify at cell scope independently of Paper 2's internal structure labels. A cell that satisfies Paper 2's structural description satisfies Paper 1's commitments, and vice versa.

Subsequent work in the CKS theory series should treat the cell as a single continuous object across both papers. Extensions at higher scopes — aspects, Selves, inter-Self coordination — all rest on this cell. Its identity preservation is the architectural foundation the rest of the series builds on.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* [Paper 1]. April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance* [Paper 2]. April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cell Identity Preservation Across Papers 1 and 2.* May 14, 2026. ORCID: 0009-0004-8065-3235.
