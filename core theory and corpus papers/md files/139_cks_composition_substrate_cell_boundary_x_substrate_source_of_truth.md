# Authority on the State Side: The Composition of the Substrate-Cell Boundary and Substrate-as-Source-of-Truth in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the emergent architectural property that arises when two foundational CKS commitments compose: the substrate-cell boundary and the commitment that the substrate is the source of truth. Each commitment has been formalized standalone in this series; the present note formalizes their composition.

## Abstract

Two of the CKS pattern's foundational commitments — the substrate-cell boundary (§2.1, §4.1) and the substrate-as-source-of-truth claim (§11.3, §6.2) — produce, when taken together, an emergent architectural property that neither yields independently: authority for coordination questions lives specifically on the state side of the boundary, in the substrate, and not on the behavior side, in the cells. This note names that property *authority-locus-on-state-side-of-boundary*, states it as four operational components, identifies the architectural decisions the composition forces beyond either commitment alone, names the anti-patterns that specifically violate it (cells holding state that should be substrate-resident, agent memory or LLM context treated as authoritative, hidden cell-internal state operationally affecting coordination, authority duplicated across substrate and cells), and provides an operational test with three sharpening properties.

## 1. Why the composition needs to be formalized as a standalone derivation

The substrate-cell boundary commits to two architectural layers — substrate (state) and cells (behavior). The substrate-as-source-of-truth commitment (§11.3) commits separately to the substrate being authoritative for the coordination questions the system needs to answer: what was decided, by whom, under what authority, with what rationale, and where contradictions remain unresolved.

Each commitment is individually formalized in this series, and each is, on its own, satisfiable in ways that produce architectures the source paper does not endorse. The boundary commitment, taken alone, can be satisfied by a deployment that preserves the layers nominally — substrate exists, cells execute, the layers are named — while authority for coordination state migrates to a third location entirely (a vendor service, a long-lived cache, an external runtime). The source-of-truth commitment, taken alone, can be satisfied by a deployment in which the substrate is treated as authoritative *and* cells also hold authoritative state simultaneously, producing duplicated authority where the two may disagree without architectural recourse.

What excludes both failure modes is the composition: when the boundary is preserved *and* the substrate is the source of truth, authority is forced specifically onto the state side of the boundary, exclusively, with cells operating as processing units that hold no authoritative content of their own. The source paper develops this composition implicitly across §2.1, §3.1, §4.1, and §11.3 — particularly in §2.1's treatment of how the boundary specifically locates authority on substrate — but does not name the resulting property as a standalone feature.

The composition matters because the dominant failure modes in 2024–2026 AI deployments — agent-memory architectures accumulating authoritative state across runs, LLM-context state treated as authoritative across turns, hidden runtime caches affecting downstream coordination — are exactly the failures it forbids. Each can be present in a deployment that nominally satisfies both foundational commitments in isolation; the composition is what supplies the architectural reason none of them is admissible.

## 2. The emergent architectural property, stated precisely

When the substrate-cell boundary and substrate-as-source-of-truth compose, the property that emerges is *authority-locus-on-state-side-of-boundary*. The property has four operational components.

**(a) Cells do not hold authoritative state internally.** A cell executes behavior under orchestration rules; it processes substrate content, applies rules, and produces outputs. Cell-internal state may exist for the duration of execution — working memory, intermediate computations, the LLM's context within a single invocation — but no cell-internal state holds authoritative content for the coordination questions the system needs to answer. The five categories of authoritative state — what was decided, by whom, under what authority, with what rationale, and where contradictions remain — never live in the cell.

**(b) The substrate holds all authoritative state across the five categories, exclusively.** The substrate is the unique location for authoritative content. When the system needs to answer a coordination question, the answer is read from the substrate; when an answer is produced, it is written to the substrate. No second location is treated as authoritative, even if it happens to agree with the substrate at any given moment.

**(c) Cell processing produces authoritative content only through rule-mediated substrate writes.** A cell's outputs are not directly authoritative. They become authoritative when, and only when, an orchestration rule mediates a write of those outputs into the substrate. Pre-write, the cell's output is non-authoritative. Post-write, the substrate content — written under rule mediation, with the cell's identity recorded as writer — is authoritative. The transition occurs at the substrate-write moment.

**(d) The boundary's directional property locates authority on the state side architecturally.** The boundary is not symmetric. State flows from substrate to cells as input; the cell processes the input and produces output; the output flows back to substrate through rule-mediated writes. Authority does not cross the boundary; it sits on the substrate side. The boundary, read directionally, says: state → substrate (held with authority); behavior → cells (executed without authority).

The four components are jointly sufficient and individually necessary. A deployment that exhibits all four satisfies the composition; a deployment that fails any one of them fails the composition.

## 3. What the composition forces beyond either commitment in isolation

The composition forces architectural decisions neither commitment in isolation forces. Each pattern below is admissible under one of the foundational commitments alone but ruled out by their composition.

*Boundary preservation alone is insufficient.* A deployment may preserve the layers nominally while authority migrates to a third location — a vendor-managed cache, an in-memory runtime store, an external "session" service. The layers are intact; authority has left the substrate without entering the cells. The composition forecloses this: authority must be on the substrate side, not in adjacent infrastructure.

*Substrate authority alone is insufficient if cells are also authoritative.* A deployment may treat the substrate as authoritative and *also* hold authoritative state in cells — typically as a performance optimization or as an emergent consequence of agent-memory designs. The composition rules this out: cells must hold no authoritative content.

*Cell-internal authoritative state of any kind must not exist.* The prohibition is general. It applies to agent memory persisting across runs, to LLM context windows persisting across turns, to instance variables in long-running cell processes, to runtime caches that downstream operations consult. Whether the storage is named "memory," "context," or "cache," and whether it persists for milliseconds or for the lifetime of the cell, the composition forbids it from holding authoritative content.

*Cell processing produces authoritative content only through rule-mediated substrate writes.* The composition forces the route by which cell output becomes authoritative. Cell output consumed directly by another cell as authoritative input — without an intermediating substrate write — has bypassed the architectural mechanism that confers authority.

*The boundary is asymmetric for authority.* A reading that treats the boundary as a symmetric separation — two layers, either of which may carry authority — is not what the composition supports. The composition makes the asymmetry explicit and architecturally enforceable rather than leaving it implicit in the source paper's prose.

## 4. Anti-patterns that specifically violate the composition

Several anti-patterns formalized elsewhere in this series violate the composition specifically. Naming each makes the composition operationally diagnosable.

**Cell-as-substrate.** The canonical composition violation: cells hold state that should be substrate-resident. Both foundational commitments may be partially satisfied — the layers exist by name; the substrate carries some authoritative content — yet cells also hold authoritative content, breaking the exclusive-locus requirement. This is the failure mode §2.1 and §11.3 point to when warning against treating execution context as substrate.

**Hidden state in cells.** The generalized composition violation: cell-internal state — local variables persisting across executions, runtime caches, session state, instance data — operationally affects coordination, even when not labeled "authoritative." If a cell's prior internal state changes the outcome of a subsequent coordination question, the cell has exercised authority regardless of how the state is labeled.

**Agent memory as source of truth.** A specific instantiation: agent-memory architectures that accumulate state across cell invocations and treat that state as authoritative for downstream decisions. Agent memory is on the cell side of the boundary. A store holding non-authoritative working state is admissible; one holding authoritative coordination content is not.

**LLM context as source of truth.** A second specific instantiation: the LLM's context window during invocations, treated as authoritative for what was decided, what is current, what conflicts exist. The context window is on the cell side; the composition forbids authoritative content there, even when authority is exercised only ephemerally within a single invocation.

**Authority duplication.** A composition violation common in performance-motivated designs: substrate is authoritative *and* cells also hold the same content as authoritative — typically as cached copies that downstream operations read from. The composition forbids duplication. If cells cache substrate content, the cache must be a non-authoritative derived view, reconciled to substrate on disagreement, never a second authoritative copy.

**Cell-direct-authoritative-output.** A composition violation common in pipelines that chain cells: cell A's output is consumed directly by cell B as authoritative input, without a rule-mediated substrate write between. Authority is conferred at the cell-output layer rather than the substrate-write layer.

**Cell-internal cache as authoritative.** A composition violation hiding as performance optimization: cells cache substrate content internally, and downstream operations consult the cache rather than re-reading the substrate. Even with periodic invalidation, the cache operationally functions as authoritative state on the cell side as long as downstream operations read from it as the source.

## 5. What the composition forces operationally — and what it does not

The composition translates into deployment-level decisions, and stating the admissible patterns alongside the forbidden ones prevents over-reading the prohibition.

**What the composition forces.** Cells read the substrate when they need authoritative state. Cell outputs that affect coordination flow to the substrate through rule-mediated writes; the substrate write is the moment authority is conferred. Authority for the five source-of-truth categories is substrate-resident exclusively. The boundary is preserved with authority specifically located on the state side; symmetric or unspecified handling of authority across the boundary is not admissible.

**What the composition does not forbid.** Cell-internal state that is *ephemeral and non-authoritative* is admissible: cells may use working memory, intermediate computations, and per-invocation context as part of their processing, provided these neither persist in a way that affects later coordination nor produce authoritative effects outside the substrate-write path. Derived views, indexes, projections, and caches outside the substrate are admissible provided they are treated as non-authoritative — derived from substrate, reconciled to it on disagreement, never read as the source of authoritative answers.

The distinction between cell-internal state in general and cell-internal *authoritative* state carries the operational weight.

## 6. Operational test

A deployment satisfies the substrate-cell-boundary × substrate-as-source-of-truth composition if and only if all of the following are true at all times during the deployment's existence.

1. **Cells hold no authoritative state internally.** No cell-internal location — agent memory, LLM context, runtime cache, instance state — holds authoritative content for any of the five source-of-truth categories.

2. **The substrate holds all authoritative state, exclusively.** Every coordination question is answered from substrate content, and only from substrate content.

3. **Cell processing produces authoritative content only through rule-mediated substrate writes.** No path produces authoritative coordination state without flowing through a rule-mediated write into the substrate. Cell outputs that bypass this path are non-authoritative regardless of subsequent use.

4. **The boundary's directional property is preserved.** The architecture treats the substrate side as authoritative and the cell side as processing; no operational pattern treats authority as living on either side at architectural discretion.

Three sharpening properties make the test operationally inspectable in deployment review.

*Cell-state-authority-absence test.* Examine each cell's internal state across executions; verify that no cell-internal location holds content downstream coordination would read as authoritative. Presence of such content indicates composition failure.

*Substrate-authority-locus test.* Examine where coordination questions are answered from in the deployment's runtime paths. Answers produced from cell-side state rather than substrate reads indicate composition failure, even when the cell-side state happens to agree with the substrate.

*Boundary-directionality test.* Examine the deployment's architectural specification for symmetric or unspecified handling of authority across the boundary. Architectures that leave authority's side unspecified, or that allow authority on either side as a configuration choice, indicate composition failure.

Stated as a single sentence: a deployment satisfies the composition if it preserves the substrate-cell boundary with cells executing behavior on the behavior side and substrate holding state on the state side, holds authoritative content for all five source-of-truth categories exclusively in the substrate (no authoritative agent memory, no authoritative context-window state, no authoritative hidden cell-internal state), and produces authoritative content only through rule-mediated substrate writes — at which point the LLM mediator on the cell side is, by the composition, architecturally prevented from exercising authority, and the boundary's directional property of state→authority and behavior→processing holds at all times.

## 7. Why naming the composition standalone matters

The composition is the architectural answer to "where does coordination authority live?" in CKS systems. The substrate-cell boundary names the two layers; the source-of-truth commitment names the substrate as authoritative; the composition locates authority specifically on the state side and forbids it from migrating to the behavior side. Without the composition stated as its own property, the boundary's directional character is implicit in the source paper's language but not architecturally enforceable as a single inspectable feature.

The composition is the diagnostic for the cluster of authoritative-state-in-cells failures that dominate operational AI deployments. Agent-memory architectures, LLM-context-as-source-of-truth designs, and hidden cell-internal state all violate it by placing authority on the cell side; each can be present in a system that nominally satisfies both foundational commitments in isolation. The composition further supports the AI-as-substrate-mediator commitment architecturally: the LLM operates within cells on the behavior side; the composition forces authority onto the state side; the LLM, accordingly, cannot exercise authority over coordination state — it can only mediate substrate content under orchestration rules. The mediator's no-authority property becomes architecturally enforceable rather than procedurally promised.

Naming the composition as its own architectural property gives downstream readers — implementers, auditors, reviewers, and any party deriving from or extending CKS — a precise specification of where authority lives, what configurations are admissible, and what configurations specifically violate the architecture. Implementations satisfying either commitment individually but failing the composition produce systems where authority migrates to the cell side; the composition forbids each such configuration and gives reviewers a single property to test for. This note is the standalone formalization of that property.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Authority on the State Side: The Composition of the Substrate-Cell Boundary and Substrate-as-Source-of-Truth in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
