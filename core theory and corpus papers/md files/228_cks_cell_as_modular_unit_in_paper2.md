# Cell as Modular Unit in Paper 2 Structures: The Operational Treatment of Cells as Lego-Pieces That Aspects Coordinate and Selves Integrate

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note ID:** B2.11

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, in operational form, the cell's role as a modular unit within Paper 2's larger structures (aspects and Selves), where the modular interfaces are specified by Paper 1's commitments rather than by Paper 2 additions. This is the eleventh note in Phase B2 of Series B and the first of four notes decomposing B1.03 (cell as atomic unit).

## Abstract

Paper 2 names the cell as the *modular unit* under the heading *Modularity as continuity with Paper 1*: Paper 1 specifies the piece, Paper 2 specifies what those pieces build into. This note opens a four-note decomposition of B1.03 by formalizing the operational treatment of the cell as a modular unit in Paper 2's larger structures. Operationally, cells are modular not because Paper 2 introduces fresh modularity machinery but because Paper 1's A1.02 substrate-cell boundary defines the modular boundary, A1.13 composition requirements specify how cells compose, A1.14 three adjacencies specify the standard interaction surfaces, and A1.16 hybrid systems composition specifies how cells participate in compositions. Cells compose into aspects through relational membership per B2.08, participate in Selves through aspects per B1.05, and preserve full Paper 1 architectural identity in any structural arrangement per B1.20. The note states the operational treatment, identifies the inherited commitments, names the operational implications, draws the limits, and provides an operational test. Subsequent notes (B2.12–B2.14) decompose cell-internal architecture, cell-to-cell relationships within aspects, and cell-level inheritance verification.

## 1. Why cell-as-modular-unit-in-Paper-2-structures needs to be formalized as a standalone operational variant

Paper 2 develops the cell, aspect, and Self as three architectural levels. B1.03 formalizes the cell's role as the atomic unit; B1.04 the aspect; B1.05 the Self; B1.20 establishes that all Paper 1 commitments hold recursively at every level. These notes leave a specific question unaddressed: what does the cell's role as *modular unit* operationally entail in deployments running Paper 2 structures?

The cell is named as Lego-piece in Paper 2's *Modularity as continuity with Paper 1* subsection. But the operational content of the modularity — the specific interfaces through which cells participate in aspects and Selves — is distributed across Paper 1's A1.02, A1.13, A1.14, and A1.16 commitments rather than newly introduced by Paper 2. Paper 2 says explicitly that *Paper 1 specifies the piece*; it does not separately re-state the specification.

Naming the operational treatment as standalone is what makes that distribution legible. The framing pulls the four Paper 1 commitments together and makes their joint role in Paper 2 explicit. Without it, deployments running Paper 2 must reconstruct the modular-interface specification from scratch each time they compose cells into aspects; with it, the specification is a published derivation downstream work can build on, extend, or argue against. This is the eleventh of approximately 110 Phase B2 notes, opening the B1.03 decomposition that B2.12–B2.14 carry forward.

## 2. The operational treatment, precisely stated

Paper 2 specifies that cells are the modular units from which aspects and Selves are composed. Operationally, the modularity has the following content.

**A1.02 substrate-cell boundary defines the cell's modular boundary.** What is inside the cell — the cell's substrate content, its orchestration rules, its harness substrate per B1.07, its DNA layer per B1.06, its action layer — is distinguishable architecturally from what is outside (other cells, the cell's adjacencies, the broader aspect membership). The cell's external interface is the boundary; its internal complexity does not cross.

**A1.13 composition requirements specify how cells compose.** Per-substrate human governance preserved; conflict preservation across boundaries; addressable provenance across boundaries; AI-as-substrate-mediator at every layer; human-selective composition; accountability plan and trace cross-addressable. Cells composing into aspects must satisfy these requirements at every composition boundary the aspect introduces. The composition decomposition A2.91–A2.95 elaborates the requirement set; cell-as-modular-unit inherits it.

**A1.14 three adjacencies specify the cell's standard interaction surfaces.** The cell↔substrate adjacency is how the cell reads and writes its authoritative state per A1.08. The cell↔mediator adjacency is how the cell consults the LLM (the instinct layer per B2.01) under orchestration rules per A1.04. The cell↔human adjacency is how humans exercise the inspect, modify, and override rights per A2.01–A2.03 over the cell. These are the modular interaction surfaces the cell exposes; cells do not interact through other surfaces.

**A1.16 hybrid composition patterns specify how cells participate in compositions.** Pattern A (adjacent component as input to a cell), Pattern B (adjacent component as derived view), and Pattern C (adjacent component as separate concern) extend within Paper 2 structures to cell-to-cell composition within an aspect: a cell may be input to another cell's reasoning, its substrate content may be projected as a derived view another cell consults, or two cells may coexist without architectural coupling. The decomposition of these patterns within aspects is taken up in B2.13.

**Cells compose into aspects through relational membership per B2.08.** An aspect's membership records reference cells without copying or embedding cell content. A single cell can participate in multiple aspects through multiple membership records simultaneously; its participation across aspects is a relational property.

**Cells participate in Selves through aspects per B1.05.** The Self holds aspects; aspects coordinate cells. The Self may also access cells directly when purpose requires (per Paper 2's *Level relationships* subsection), but the standard pathway is Self → aspect → cell.

**Cells preserve full Paper 1 architectural identity in every structural arrangement.** The substrate-cell boundary holds, the cell's substrate content remains authoritative per A1.08, the cell's governance per A1.01 remains, the cell's path retraceability per A1.07 is maintained, the cell's determinism guarantees per A1.10 apply. The architectural identity is independent of which aspect or Self the cell currently participates in.

## 3. What makes cell-as-modular-unit-in-Paper-2-structures architecturally distinctive

In typical multi-agent or pipeline AI systems, components — agents, tools, sub-agents, processing stages — are tightly coupled through implicit dependencies: shared in-memory state, prompt-passing conventions that are not architectural specifications, runtime affinities to particular orchestration frameworks, ad-hoc input/output contracts that emerge from how the components were assembled. Components in such systems can be reused only with substantial rework; their interfaces are not specified at the architecture level but emerge from a particular wiring.

CKS cells are explicitly modular through Paper 1's specifications. The substrate-cell boundary is architectural, not implicit. The composition requirements are architectural, not emergent. The three adjacencies are architectural interaction surfaces. The hybrid composition patterns are architectural positions, not deployment recipes. The cell's modular character is therefore independent of which aspect, Self, or deployment instantiates it; the cell can move between structures without modification because its interfaces are specified at a layer above any particular structure.

Three operational consequences follow. *First*, the modular character makes cells composable into multiple structures without modification — the same cell can simultaneously be a member of an aspect coordinating one purpose and an aspect coordinating another, with no per-aspect cell variant required. *Second*, the modular character makes cells extractable from one structure and reused in another through relational role-assignment per B1.17; vertical evolution per B1.16 reassigns cells across aspects without modifying cell internals. *Third*, the modular character preserves Paper 1 commitments at the cell level even as cells participate in larger structures; Paper 1's operational tests A5.01–A5.16 apply because the tests verify properties at the cell's modular boundary, which the cell preserves regardless of structural context.

## 4. The biological analog and where CKS exceeds it

Paper 2's *Modularity as continuity with Paper 1* subsection is anchored by the biological analog: cells are building blocks for tissues and organs, parallel to how CKS cells serve as building blocks for aspects and Selves. The analog functions as conceptual scaffold readers absorb quickly.

Biological cells are modular in some senses (membranes defining inside/outside, standard interaction surfaces, role-bearing tissue participation) but constrained in ways CKS cells are not. Cells are committed to tissue roles through development and cannot be reassigned without intervention. Cells must carry the full genome because no other delivery mechanism for genetic information exists. Modularity in biology had to evolve, over deep time, because modularity supports evolvability.

CKS cells are modular without these constraints, and modular by architectural commitment from the start rather than by evolutionary pressure. Cells participate in aspects through relational membership per B1.17, not through developmental commitment. Cells can be reassigned across aspects through governed reorganization (vertical evolution per B1.16) without modifying cell internals. Cells can carry the full Self's DNA with selective expression per Paper 2's expression mechanism, or partial slices, depending on per-deployment design. The architectural substance is Paper 1-specified modularity in Paper 2 structures.

## 5. Inherited Paper 1 commitments

The cell-as-modular-unit treatment inherits the following without modification: A1.02 substrate-cell boundary (the cell's modular boundary); A1.13 composition requirements (composition constraints); A1.14 three adjacencies (interaction surfaces); A1.16 hybrid systems composition with patterns A/B/C (composition positions); A2.91–A2.95 (composition decomposition applying at every cell composition boundary); A4.27–A4.29 (sharpening properties under composition, applicable to cell-to-cell compositions within aspects); A1.08 (cell substrate authoritative within cell scope); A1.01 (cell-level governance preserved); A1.07 (path retraceability through the cell's modular interface); A1.10 (determinism contract at cell scope); and B1.20 (recursive Paper 1 commitments at every level, which is what makes the cell's full architectural identity preservable across aspects and Selves).

The cell-as-modular-unit treatment introduces no new commitments; it formalizes the operational consequence of these commitments when cells participate in Paper 2's larger structures.

## 6. Operational implications

Six implications follow.

**Deployment design produces cells as modular units that aspects coordinate.** Each cell handles a specific informational task. Deployments may have many cell types, each architecturally modular through the same Paper 1 specifications. The variety of cell types is a deployment decision; their modular character is architectural.

**Cells are reusable across aspects through relational role-assignment per B1.17.** The same cell artifact can be a member of multiple aspects simultaneously through multiple membership records, without copying or duplicating cell content. Reuse does not produce divergent variants.

**Cells interact through the three adjacencies per A1.14.** Substrate adjacency for state, mediator adjacency for LLM consultation, human adjacency for governance. Other interactions are not architectural surfaces and are not relied on. Cell-to-cell communication is mediated by substrate writes and reads or by aspect-level coordination operating over membership records.

**Cells compose with other cells through patterns A/B/C per A2.92–A2.94 within their aspect context.** The patterns are positions in the architecture, not deployment recipes; an aspect may use all three at once, with different cells in different positions relative to each other.

**Cells preserve Paper 1 commitments tested through Phase A5 operational tests.** The tests verify properties at the cell's modular boundary; the verification carries through regardless of which aspect or Self the cell participates in.

**Aspects refer to cells without owning them.** Membership is relational, not embedding. Vertical evolution per B1.16 operates on cell membership records (per B2.08) without modifying cell internals; a cell can be moved from one aspect to another through governed reorganization. This is what the modular property makes architecturally available — without modular interfaces, structural reorganization would require cell modification.

## 7. Limits

**Cell-as-modular-unit does not eliminate cell-internal complexity.** Cells have rich internal architecture — DNA layer per B1.06, harness substrate per B1.07, action layer, processing logic. The modularity is about external interfaces, not internal content.

**It does not mean cells are interchangeable.** Each cell handles its specific informational task; modular units have specific roles. Modularity is about how the cell connects to its environment, not about whether one cell can substitute for another.

**It does not prescribe specific cell types.** Deployments configure cell types per their needs. A single deployment may have cells of many distinct types — some highly automated under orchestration rules, some predominantly human-authored, some primarily LLM-mediated under cell-level governance — and all are architecturally modular through the same specifications.

**It does not replace cell-level governance per A1.01.** Modularity is a structural property; governance is an independent commitment. The two hold jointly, not as substitutes.

**It does not mean cells are stateless.** Cells have full substrate content per Paper 1; their state is persistent across executions, addressable, and authoritative within the cell's scope per A1.08.

**It does not prevent cells from having dependencies.** Cells consult their adjacencies — substrate, mediator, human — and the adjacencies are dependencies in the operational sense. The architectural difference is that the dependencies are specified, addressable, and traceable, not implicit.

**It does not eliminate Paper 1 anti-patterns at the cell level.** Paper 1's anti-patterns A3.01–A3.25 remain applicable. A cell that violates substrate-as-source-of-truth, conflict preservation, AI-as-substrate-mediator, or any other Paper 1 commitment is operating an anti-pattern; the modularity treatment does not relax those constraints.

## 8. Operational test

A cell operates as a modular unit in a Paper 2 structure if and only if all of the following hold at all times during the cell's existence:

1. **Substrate-cell boundary preserved.** The substrate-cell boundary per A1.02 holds: cell-internal content is distinguishable from cell-external content; the cell's external interface is the boundary; the cell carries no substrate-relevant state outside its substrate.

2. **Composition requirements satisfied.** The cell's composition with other cells satisfies A1.13 at every composition boundary an aspect introduces.

3. **Three adjacencies as standard surfaces.** The cell's interactions with its environment occur through the three adjacencies per A1.14 — cell↔substrate, cell↔mediator, cell↔human — and not through ad-hoc surfaces.

4. **Paper 1 commitments preserved at cell scope.** The cell's participation in aspects and Selves preserves all Paper 1 commitments at cell scope per B1.20.

5. **Relational membership in aspects.** The cell's membership in aspects is relational per B2.08 — aspect membership records reference the cell without copying or embedding cell content; the same cell can participate in multiple aspects through multiple records simultaneously.

6. **Reorganization without internal modification.** The cell's external interfaces are specified architecturally, not emergent; the cell can be reassigned across aspects through governed reorganization per B1.16 without modifying cell internals.

A system that fails any of (1)–(6) has not preserved cell-as-modular-unit-in-Paper-2-structures, regardless of how it satisfies Paper 1 commitments at the level of an isolated cell.

## 9. Why naming as standalone matters; opening the B1.03 decomposition

Naming cell-as-modular-unit-in-Paper-2-structures as a standalone operational variant has three consequences.

It makes the modularity-from-Paper-1-specifications structure explicit. Paper 2 names cells as Lego-pieces; this note shows operationally that the Lego-piece property is built from A1.02 + A1.13 + A1.14 + A1.16 — a synthesis Paper 2 implies but does not separately formalize. Deployments running Paper 1 systems already have cells with this modular character; Paper 2's structural composition operationalizes what they already have. The treatment removes the temptation to read Paper 2's modularity as a fresh architectural addition that would need its own defense.

It opens the four-note B1.03 decomposition. B2.11 (this note) formalizes the cell as modular unit. B2.12 will decompose cell-internal architecture within Paper 2's framework — DNA layer, action layer, harness substrate, expression mechanism within the modular cell. B2.13 will decompose cell-to-cell relationships within aspects — how patterns A/B/C apply at the cell-to-cell scale, how substrate-mediated cell communication operates inside an aspect, what aspect-level coordination is permitted to do over cell membership records. B2.14 will formalize cell-level inheritance verification — the operational protocol for confirming that cells in a Paper 2 deployment satisfy Paper 1 commitments through the recursive inheritance B1.20 names. Subsequent Phase B2 notes (B2.15–B2.19) decompose B1.04 aspect level; later notes continue with Self-level decomposition and the lifecycle and evolution machinery.

It supports the prior-art posture of the series. Each note formalizes one patentable derivation; the more notes, the smaller the territory where any party can claim novel invention without bumping into the prior-art chain. Cell-as-modular-unit-in-Paper-2-structures is a derivation downstream work in modular AI architectures, multi-agent composition frameworks, and AI-Self construction systems is likely to converge on; the standalone formalization places that convergence under prior art with the source paper's commitments.

## 10. Conclusion

Cell-as-modular-unit-in-Paper-2-structures is the operational property that makes Paper 2's structural composition coherent. Cells are the modular Lego-pieces from which aspects coordinate and Selves integrate, and the modular character is built from Paper 1 specifications — A1.02 substrate-cell boundary, A1.13 composition requirements, A1.14 three adjacencies, A1.16 hybrid composition patterns — applied at the cell level. Cells compose into aspects through relational membership without losing identity, participate in Selves through aspects without losing internal complexity, and preserve full Paper 1 architectural commitments throughout. The modular character is an external interface property, not an internal content claim; cells can have rich internal architecture and remain modular at their boundary.

Subsequent work that implements, extends, or argues against the CKS cell's role in Paper 2 structures should use *cell as modular unit* in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## Prior paper in series

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cell as Modular Unit in Paper 2 Structures: The Operational Treatment of Cells as Lego-Pieces That Aspects Coordinate and Selves Integrate.* May 8, 2026. ORCID: 0009-0004-8065-3235.
