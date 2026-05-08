# Cell-to-Cell Relationships Within Aspects in the Coordination Knowledge Substrate Pattern: Aspect-Mediated Coordination Preserving Modular Cell Boundaries

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a standalone operational variant, **cell-to-cell relationships within aspects** — how cells participating in the same aspect relate through aspect-mediated coordination over substrate pathways, preserving cell modular boundaries per A1.02 while enabling aspect-level integration via coordination rules per B1.04 and composition patterns A/B/C per A2.92–A2.94. This is the third decomposition of B1.03 (cell as atomic unit), following B2.11 and B2.12; B2.14 closes the decomposition with cell-level inheritance verification.

## Abstract

Paper 2's three-level architecture (cell, aspect, Self) establishes the cell as the atomic unit and the aspect as the coordination arrangement for cells serving a particular purpose. Two prior notes decompose B1.03 by formalizing the cell's external interfaces (B2.11) and internal architecture (B2.12). This note formalizes the third dimension: how cells relate to each other when they share an aspect. The architecturally distinctive commitment is that cells in CKS do not directly couple — they relate through aspect-mediated coordination over substrate pathways. Aspect coordination rules per B1.04 specify how constituent cells interact; substrate writes per A2.20 and reads per A1.08 carry the information; composition patterns A/B/C per A2.92–A2.94 govern the form of the relationship; and substrate-resident coordination rules per A2.46 keep it governable. The note states the relationships precisely, distinguishes the architecture from conventional direct component-to-component coupling, identifies inherited Paper 1 commitments, articulates operational implications, and provides an operational test.

## 1. Why cell-to-cell relationships within aspects need to be formalized as standalone

Paper 2's "Three levels of structure" introduces aspects as coordination arrangements of cells serving a particular purpose: an aspect "asks pattern questions across its constituent cells for its purpose," operating over those cells as content domain. Aspects exist because cells need to relate to each other for purposes that no single cell serves alone. But the form of that relationship is not self-evident, and three failure modes are reachable without a precise formalization.

First, "cells coordinate within an aspect" admits readings in which cells call each other directly, share state directly, or take direct dependencies on each other's implementations — readings that would dissolve the modular cell boundary B2.11 establishes externally and B2.12 fixes from the cell's interior. Second, the substrate's role as the architectural medium for inter-cell information flow can become invisible when relationships are described abstractly rather than mechanically. Third, aspect-level coordination rules can collapse into implementation detail rather than being recognized as substrate-resident authoritative content per A2.46, governable per A2.04.

The note is the thirteenth in Phase B2 and the third of four decomposing B1.03: B2.11 fixed the cell's external interface, B2.12 fixed its internal architecture, B2.13 fixes how cells relate to each other when they share an aspect, and B2.14 will close the decomposition with cell-level inheritance verification.

## 2. The architectural relationships precisely stated

Cells participating in the same aspect relate to each other through **aspect-mediated coordination** over substrate pathways. The relationship has four operational components.

**(a) Aspect coordination rules per B1.04.** The aspect is the architectural locus of cell-to-cell coordination. An aspect carries coordination rules that specify how its constituent cells interact for the aspect's purpose: which cells contribute to which pattern questions, which cell outputs are consulted by which other cells, in what order, under what conditions, with what conflict-handling discipline. The coordination rules are aspect-level content — they specify behavior across cells, not within any one cell.

**(b) Substrate pathways for information flow.** Cells do not directly call each other or share in-memory state. A cell writes to substrate per A2.20 (Property B with orchestration rules); other cells in the same aspect read from substrate per A1.08. The substrate is the architectural medium for cell-to-cell information flow. The flow is asynchronous in form — a producing cell writes when its work yields substrate-bound output; a consuming cell reads when its own work requires substrate input — and is governed by the aspect's coordination rules, not by direct synchronous coupling.

**(c) Composition patterns A/B/C per A2.92–A2.94.** The form a cell-to-cell relationship takes within an aspect is one (or a composition) of three patterns inherited from A1.16 and operationalized at A2.92–A2.94. Pattern A (consultation) is when one cell consults another cell's substrate output as part of the aspect's purpose-coordination. Pattern B (derived view) is when the aspect derives a unified view from multiple cells' substrate content. Pattern C (separate concerns) is when cells in the same aspect operate on substantively separate concerns and the aspect integrates their outputs without requiring the cells to consult each other. Pattern selection is per aspect coordination rule and follows aspect purpose.

**(d) Substrate-resident, governable coordination.** Aspect coordination rules and the patterns they encode are substrate content per A2.46, authoritative under the human-governed commitment. Humans author them per A2.04. Consultation events, derived-view computations, and integration steps are recorded per A2.40 with provenance — what cell consulted what other cell through which aspect rule, which derived view drew from which contributing cells, which integration combined which separate concerns. Cell-to-cell coordination is therefore inspectable, modifiable, and overridable through the same authority architecture that grounds substrate content generally.

A system that instantiates only some of (a)–(d) — for example, aspect coordination rules without substrate pathways, or substrate pathways without governable coordination rules — does not implement the commitment as the architecture states it.

## 3. What aspect-mediated cell-to-cell coordination is NOT

The standalone treatment is precise about what cell-to-cell relationships within aspects are. Stating what they are not is what keeps the framing from drifting into commitments the source paper does not support.

**Not direct cell-to-cell coupling.** Conventional architectures often couple components directly — components call each other directly, share state through shared mutable objects, take compile-time or runtime dependencies on each other's interfaces beyond a substrate boundary. CKS cells do not. They relate through the aspect and through the substrate; the aspect and the substrate together are the medium.

**Not a violation of A1.02 between cells.** The substrate-cell boundary inherited from Paper 1 holds between cells, not only between substrate and the cell that owns it. A cell does not modify another cell's internals — its DNA-layer substrates, its action-layer recordings, its harness substrate, or its expression state. What one cell writes for another is substrate content per A2.20, governed by orchestration rules; the consuming cell reads substrate content per A1.08; neither cell reaches across the boundary into the other's interior.

**Not a violation of the three adjacencies.** A1.14 specifies three architectural adjacencies for cells: cell↔substrate, cell↔mediator, and cell↔human. Direct cell↔cell adjacency is not among them. Cell-to-cell relationships are mediated through cell↔substrate adjacency on each side, with the aspect coordination rule that ties them together itself substrate content read by both cells' executions.

**Not a dissolution of cell modular boundaries.** B2.11 establishes the cell as a modular unit at its external interface and B2.12 establishes the boundary internally; neither is weakened when the cell participates in an aspect. Aspect-level integration does not turn the cell into a non-modular subroutine of a larger composite.

**Not a prescription of specific patterns.** The architecture does not commit to any one of patterns A, B, or C as canonical. Pattern selection is a deployment decision driven by aspect purpose; mixed compositions within a single aspect are permissible.

**Not exhaustive of all cell relationships.** Cells may also relate cross-aspect (per B1.19 cross-level access), or to the Self level when purpose requires. This note formalizes the within-aspect case specifically.

## 4. Biological analog

The analog within Paper 2's biology mimicry is cell-to-cell signaling in tissues. Biological cells in the same tissue relate through chemical signals (paracrine, juxtacrine, gap-junction transfer) mediated by the tissue's structural and chemical context. The communication is constrained by the tissue's architectural rules; cells in different tissue contexts have different relationships even when they are the same cell type.

CKS exceeds biology on two axes. First, biological cells have direct mechanisms (gap junctions, direct membrane contact) that move material across cell boundaries without going through the surrounding medium; CKS cells do not — the substrate is always the medium for inter-cell information flow within an aspect. Second, biological tissue coordination rules evolved over deep time and are not directly inspectable, modifiable, or overridable by the organism; CKS aspect coordination rules are substrate-resident content authored by humans, fully inspectable and modifiable under the human-governed commitment. The biology is conceptual scaffold; the architectural substance is aspect-mediated, substrate-resident, governable coordination.

## 5. Inherited Paper 1 commitments

Cell-to-cell relationships within aspects are not a new commitment requiring fresh defense. They inherit as follows.

A1.02 (substrate-cell boundary) holds between cells, not only between substrate and a single cell. A1.13 (composition requirements) constrains how cells compose, including within aspects. A1.14 (three adjacencies) restricts architectural adjacency to cell↔substrate, cell↔mediator, and cell↔human, ruling out direct cell↔cell channels. A1.16 (hybrid composition patterns) is the parent of patterns A/B/C; their operational forms (A2.92, A2.93, A2.94) apply per aspect purpose. A2.04 governs the authoring of aspect coordination rules; A2.46 (Category 4) names them as authoritative substrate-resident content; A2.40 records consultation, derivation, and integration events with provenance; A1.07 (path retraceability) extends across the recorded coordination chain so that a coordinated outcome can be reconstructed from the substrate's record.

Series B inheritance is also direct. B1.04 establishes the aspect as a coordination arrangement; this note formalizes the cell-side relational properties B1.04 governs from the aspect side. B2.11 and B2.12 supply the modular-cell foundation that aspect-mediated coordination preserves. B1.16 (vertical evolution) modifies cell-to-cell relationships through aspect restructuring without modifying cell internals. B1.17 (multiple-aspect participation) means the same cell may have different relationships across different aspects. B1.18 (higher level as content domain) is the broader category in which cell-to-cell relationships within aspects sit.

## 6. Operational implications

Six implications follow from formalizing cell-to-cell relationships within aspects as the architecture commits to.

**Configuration through aspect rules.** Deployments configure cell-to-cell coordination by authoring aspect-level coordination rules per A2.04. The rules name which cells participate, what pattern (A, B, C, or a composition) governs their relationships, what conflict-handling applies, and what provenance is recorded. Configuration is substrate-level work, not infrastructure-level work.

**Pattern variation by aspect purpose.** Different aspects of the same Self may use different patterns. An aspect that asks "what does our overall risk position look like across these cells?" tends to use Pattern B; an aspect that asks "should this cell's recommendation defer to that cell's recommendation under conditions C?" tends to use Pattern A or a Pattern A/B composition.

**Asynchrony as the default form of information flow.** Substrate pathways are asynchronous: a producing cell writes when its work produces substrate-bound output, and a consuming cell reads when its own work requires it. Some deployments may use orchestration tooling that makes the flow appear synchronous from outside the substrate; the substrate-mediated form is what the architecture commits to.

**Vertical evolution through aspect restructuring.** Per B1.16, vertical evolution restructures cells' relationships across aspects — reassigning a cell, splitting an aspect, merging two, dissolving one, introducing a new one — without modifying any participating cell's internals. The cell-to-cell relationships change because the aspect coordination rules change; the cells themselves do not.

**Relationship variation across aspects.** Per B1.17, the same cell may participate in multiple aspects, and its relationships within each aspect are governed by that aspect's coordination rules. The same pair of cells may consult each other in one aspect and contribute to a derived view in another; the relationships are aspect-relative, not cell-pair-intrinsic.

**Cross-partner coordination follows existing discipline.** Where cell-to-cell coordination spans multi-author authoring contexts (per A2.47), the multi-author rule-authoring conflict treatment (A6.12) applies. The standalone framing here preserves the existing discipline.

Cell-to-cell coordination is testable through inspection and replay: the reproducibility test (A5.16) verifies that a coordinated outcome reproduces from the recorded substrate inputs and aspect coordination rules — the same cell outputs, read in the order the aspect rule specifies, under the same coordination pattern, produce the same coordinated result.

## 7. Limits

Section 3 names what cell-to-cell relationships within aspects are not at the architectural level. Two further limits keep the operational scope precise. The framing **does not operate without governance**: aspect coordination rules are substrate-resident authoritative content per A2.46, authored by humans per A2.04; a system that runs cell-to-cell coordination through arrangements that escape the human-governed authority architecture does not instantiate the commitment. The framing **does not replace cell-level work**: cells continue cell-level processing under their own orchestration rules; aspect coordination operates over what cells produce, not in place of it.

## 8. Operational test

A system implements cell-to-cell relationships within aspects as the architecture commits to if and only if all of the following are true at all times during the substrate's existence:

1. Cells participating in the same aspect relate to each other through substrate-mediated information flow — producing cells write to substrate per A2.20; consuming cells read from substrate per A1.08; no direct in-memory or runtime cell-to-cell channel is required for the relationship to function.
2. The aspect carries coordination rules, substrate-resident per A2.46, that specify which cells participate, in what relational pattern (A/B/C or composition), with what conflict-handling, and what provenance is recorded.
3. The aspect coordination rules are authored by humans per A2.04 and are inspectable, modifiable, and overridable under the human-governed commitment.
4. Coordination events are recorded per A2.40 with provenance sufficient to reconstruct what cell consulted what other cell through which aspect rule, or which cells contributed to which derived view, or which separate-concerns outputs were integrated.
5. Cell-to-cell coordination preserves A1.02 — cells do not modify each other's internals — and preserves modular cell boundaries per B2.11; participation in an aspect does not weaken either property.

A system that fails any of (1)–(5) does not implement cell-to-cell relationships within aspects as the architecture commits to. Such a system may instantiate some other coordination pattern; downstream work that relies on its coordination guarantees should be scoped accordingly.

## 9. Why naming this as standalone matters

Naming cell-to-cell relationships within aspects as a standalone operational variant matters for three reasons.

First, it is the third of four decompositions of B1.03. B2.11 fixed the cell's external interface; B2.12 fixed its internal architecture; B2.13 fixes how cells relate when they share an aspect; B2.14 will close the decomposition with cell-level inheritance verification. The four notes together exhaust B1.03's operational content along the dimensions Phase B2 needs to make explicit.

Second, the standalone framing makes the boundary between cell-level and aspect-level architectural work observable. Cell-level work (processing under cell orchestration rules) is what cells do; aspect-level work (coordination across cells for an aspect's purpose) is what aspects do; cell-to-cell relationships within aspects is the operational interface between the two. Without naming it explicitly, it tends to disappear into one or the other, with downstream consequences for how implementations are described and assessed.

Third, the standalone framing prepares Phase B2's progression. Subsequent notes B2.15–B2.19 will decompose B1.04 from the aspect side. Cell-to-cell relationships within aspects, fixed here, is what those decompositions can take as given when they reason from the aspect side toward the cells the aspect coordinates.

Subsequent work that adopts, extends, or argues against the CKS aspect-mediated coordination commitment should use "cell-to-cell relationships within aspects" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cell-to-Cell Relationships Within Aspects in the Coordination Knowledge Substrate Pattern: Aspect-Mediated Coordination Preserving Modular Cell Boundaries.* May 8, 2026. ORCID: 0009-0004-8065-3235.
