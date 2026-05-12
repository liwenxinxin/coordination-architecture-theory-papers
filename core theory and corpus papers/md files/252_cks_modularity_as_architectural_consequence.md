# Modularity as Architectural Consequence: Formalizing How Paper 2's Structural Modularity Emerges from Four Paper 1 Architectural Commitments

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize, as a standalone operational specification, the precise mechanism by which structural modularity in CKS architectures emerges as the joint consequence of four Paper 1 architectural commitments operating together — rather than as a design pattern introduced by Paper 2 or chosen by an implementer.

This is derivation note B2.35 in the CKS defensive publication series. It opens the five-note B1.08 decomposition (B2.35–B2.39) within Phase B2 of Series B.

## Abstract

Paper 2's "Modularity as continuity with Paper 1" establishes that the structural modularity present in CKS architectures — across cells, aspects, and Selves — is not a Paper 2 addition but an architectural consequence of four commitments Paper 1 already defends: A1.02 (substrate-cell boundary), A1.13 (composition requirements), A1.14 (three adjacencies), and A1.16 (hybrid systems composition with Patterns A/B/C). Together these four commitments produce what this note calls *modularity as architectural consequence*: bounded modular units with specified composability, standard interaction interfaces, and flexible participation modes. All four are required jointly — removing any one leaves the modularity incomplete. This distinguishes CKS modularity from *engineering-choice modularity*, in which components are modular because a designer elected to make them so and in which modularity may erode as the system evolves without architectural enforcement. Architectural consequence modularity is structurally maintained because the commitments hold; it is testable against the architecture. Paper 2's contribution is extending the same four commitments — already operative at the cell level in Paper 1 deployments — to aspects and Selves through B1.20's recursive inheritance. This note formalizes the full specification: the four commitments, their joint operation, the architectural-consequence framing, the Paper 1 inheritance lineage, the operational implications, and the limits.

## 1. Why this specification needs to be formalized as a standalone derivation

Paper 2 commits to structural modularity at every level of composition — cell, aspect, and Self. A reader encountering that commitment faces an immediate question: where does the modularity come from? Two candidate answers present themselves. The first is that Paper 2 introduces a new modularity mechanism, something that does not exist in Paper 1 architectures. The second is that modularity is already present in Paper 1 architectures, and Paper 2 extends it upward by applying the same generating commitments at higher levels. Paper 2 explicitly takes the second position, and B1.08 formalizes it as an architectural commitment. B2.35 opens the decomposition of B1.08 by specifying *precisely* how that generation works.

The specification is prior-art-significant in its own right. A claim that a modular multi-level AI architecture is novel depends on what produces the modularity. If modularity is an engineering choice — made by a designer or platform — it may be novel each time it appears. If modularity is the joint consequence of four architectural commitments that Paper 1 already defends, then any architecture satisfying those four commitments has the same modularity as a structural consequence, and novelty must be located elsewhere. This note formalizes the consequence relationship, making the prior-art scope explicit and checkable.

Positionally, B2.35 is the thirty-fifth note in Phase B2 and opens the five-note B1.08 decomposition. B2.36 through B2.39 operationalize specific downstream implications of the modularity this note specifies. The present note is the foundational statement on which those four depend.

## 2. The architectural specification: four commitments jointly producing modularity

The modularity of cells, aspects, and Selves in CKS architectures is the joint consequence of four Paper 1 commitments. Each contributes one necessary component of complete modular architecture. Together they define what this note calls *modularity as architectural consequence*.

**A1.02 — Substrate-cell boundary as modular boundary.** The substrate-cell boundary per A1.02 is not merely a governance partition; it is a modular boundary. It specifies what is inside each modular unit (the cell's substrate content and orchestration rules) and what is outside (the shared substrate layer and adjacent cells). Every modular unit — whether a cell, an aspect, or a Self — has a substrate-resident boundary that defines its modular identity: what it owns, what it exposes, and what it does not expose. Without a defined boundary, there is no modular unit, only an undifferentiated mass of substrate state.

**A1.13 — Composition requirements as composability specification.** A1.13 specifies the five requirements that must be satisfied for two or more substrate-governed units to compose validly: per-substrate human governance preservation, conflict preservation across boundaries, and the three further requirements governing how units join. These requirements are not optional guidance; they are the conditions under which the composed unit retains Paper 1's properties. They constitute the composability specification for modular CKS units. Without a composability specification, bounded units cannot be reliably combined — they are bounded but not composable.

**A1.14 — Three adjacencies as standard interaction interfaces.** A1.14 specifies three canonical interaction surfaces: cell↔substrate, cell↔substrate-mediator, and cell↔human. These three adjacencies are the "connector standard" for CKS modular units. Any cell (and, by extension, any aspect or Self) interacts with adjacent components through one of these three specified surfaces. The adjacencies are what make modular units interchangeable at the interface level — a cell composed into one aspect interacts with its substrate through the same surface specification as a cell composed into a different aspect. Without standard interfaces, modular units cannot be combined and recombined reliably; each composition would require bespoke interface negotiation.

**A1.16 — Hybrid systems composition with Patterns A/B/C as flexible composition modes.** A1.16 specifies how modular components participate in larger compositions through three patterns: Pattern A (the component as consultant to a primary composition), Pattern B (the component as content-domain provider within a composition), and Pattern C (the component as a separate concern in parallel composition). These three patterns specify the *modes* of modular participation — the range of structural roles a modular unit can occupy in relation to a larger arrangement. Without flexible participation modes, bounded and composable modular units with standard interfaces would still be restricted to a single compositional relationship, limiting their reuse across structures.

**The joint consequence.** The four commitments together define a complete modular architecture: bounded (A1.02), composable (A1.13), interfaced (A1.14), and modal (A1.16). The modularity is not added by a fifth commitment; it is what the four commitments jointly produce when they hold together. Paper 2's structural modularity — cells composing into aspects, aspects composing into Selves, with relational role membership per B1.17 — is the expression of this joint consequence at multiple levels.

## 3. What makes modularity-as-architectural-consequence architecturally distinctive

The distinction between modularity as architectural consequence and modularity as engineering choice is not a matter of degree; it is a structural difference with operational consequences.

In engineering-choice modularity, components are modular because a designer decided to make them modular at a point in time. The decision produces modular components at that moment. But the modularity is not maintained by the architecture; it is maintained by continuing discipline. As the system evolves — as new components are added, as interfaces accumulate ad hoc modifications, as composition patterns multiply — the modularity erodes unless each subsequent design decision re-elects it. Engineering-choice modularity is fragile in exactly this sense: there is no architectural mechanism that re-establishes it when a decision breaks it.

In architectural-consequence modularity, the modularity is not a decision made at a point in time; it is a structural property that holds as long as the four commitments hold. If the commitments are satisfied — boundaries defined per A1.02, composition requirements met per A1.13, adjacencies respected per A1.14, participation patterns followed per A1.16 — the modularity is present. If the commitments are violated, the modularity degrades. This is testable: a deployment can be checked against the four commitments, and the presence or absence of modularity follows from that check. Engineering-choice modularity has no equivalent test.

The testability has a further consequence: architectural consequence modularity supports what A5.14 formalizes as the composition requirements test. The test is possible precisely because the modularity is specified as a consequence of identifiable commitments that are themselves checkable. Engineering-choice modularity, lacking that commitment structure, resists analogous testing.

## 4. The joint operation of the four commitments: completeness and the incompleteness condition

The four commitments are jointly sufficient for complete modular architecture. They are also individually necessary: removing any one leaves the modularity incomplete in a specific and architecturally significant way.

A1.02 without A1.13 produces bounded units that cannot be reliably composed. Each unit has a defined boundary, but there is no specification of the conditions under which units compose validly. Ad hoc composition may work in specific instances but does not carry guarantees.

A1.13 without A1.02 produces composability requirements that lack a clear boundary to compose across. The requirements specify how units join, but without a boundary specification, it is not clear what counts as a unit and what counts as its outside.

A1.14 without A1.16 produces standard interfaces without flexible participation modes. Units can interact through specified surfaces, but the range of structural roles they can occupy in larger compositions is not specified. Each composition would need to define participation roles independently.

A1.16 without A1.14 produces flexible participation modes without standard interfaces. Units can occupy different structural roles in different compositions, but the interaction surfaces through which they do so are not standardized, requiring bespoke interface specification at each composition.

The incompleteness in each case is not a minor gap; it is the absence of one of the four components that jointly define complete modular architecture. All four are required. This is what makes the modularity a *joint* consequence rather than the output of any subset.

## 5. Inherited Paper 1 commitments and the Paper 2 extension

All four commitments are Paper 1 commitments. A1.02, A1.13, A1.14, and A1.16 are specified in Paper 1 and defended there at the cell level. Paper 1 deployments already have modular cells as a consequence of these four commitments operating at cell scope. This is architecturally significant: the modularity is not a feature that Paper 2 introduces; it is a property already present in every Paper 1 deployment.

The operational decompositions of these four commitments in Series A (A2.08–A2.12 for the substrate-cell boundary; A2.75–A2.80 for composition requirements; A2.81–A2.85 for adjacencies; A2.91–A2.95 for hybrid composition; A4.14–A4.30 for composition pairs; A5.14 for the composition requirements test) are all load-bearing references for the modularity this note formalizes. The modular architecture is specified through those decompositions; B2.35 specifies that the same architecture, operating at the cell level in Paper 1, extends to aspects and Selves in Paper 2.

Paper 2's contribution to modularity is the extension per B1.20's recursive inheritance: the same four commitments that produce cell-level modularity in Paper 1 operate at the aspect level and the Self level in Paper 2, producing modularity at all three levels. The extension is possible precisely because the four commitments are architectural commitments — they apply wherever CKS structure holds, not only at the cell level. B2.11 operationalizes modularity at cell scope within Paper 2 structures; B2.35 specifies the foundational mechanism from which B2.11 and the aspect-level and Self-level equivalents all derive.

## 6. Operational implications

Several operational properties follow directly from modularity as architectural consequence.

**Modularity is present without additional configuration.** A deployment satisfying the four commitments inherits modular cells, modular aspects, and a modular Self without further design work directed at modularity. The modularity is a consequence of commitments already required by the pattern. A deployment that independently pursues modularity as an engineering goal achieves the same structural property by a different route; CKS deployments do not need to pursue it as a separate goal.

**Reassignment per B1.17 is supported by modular interfaces.** The relational structural roles commitment per B1.17 — through which the same underlying substrate artifact can participate as a cell in one aspect and as a component in a different aspect simultaneously — depends on the standardized interfaces A1.14 provides. The interfaces are what make reassignment structurally safe: the artifact's interaction surface with the substrate, with the substrate mediator, and with human governance does not change when the artifact moves across compositional arrangements. B2.35 is the foundational specification for why reassignment works without bespoke re-engineering.

**Vertical evolution per B1.16 operates through modular restructuring.** The vertical evolution axis — in which structural relationships between cells, aspects, and Selves change over time — presupposes modular units that can be detached, repositioned, and recomposed. The modular architecture specified here is what makes vertical restructuring possible without requiring that every restructuring event be bespoke. B2.37 develops this implication in detail; B2.35 provides its foundation.

**Tool-agnosticism per A1.05 is supported.** Modular units can migrate to different substrate technologies while maintaining their modular interfaces, because the interfaces are specified by the four architectural commitments, not by specific implementation technology. A cell that satisfies A1.14's three adjacencies in one substrate implementation satisfies them in another. The modularity is substrate-technology-independent in this sense.

## 7. Limits of the specification

Modularity as architectural consequence does not imply unlimited composability or uniformity. The following limits hold.

**Not all compositions are valid.** A1.13's five composition requirements must be satisfied for any given composition. Modularity establishes that units are composable in principle; it does not guarantee that any specific composition is valid. The composition requirements test per A5.14 is required to confirm validity.

**Modular units are not interchangeable in their content.** Each cell has a specific informational task; each aspect has a specific purpose; each Self has a specific identity. Modularity is a property of interfaces and structural participation, not of internal content. Two modular units that share the same interaction surfaces may carry entirely different content and may not be substitutable for each other in a given composition.

**Modularity does not eliminate governance at any level.** Cell-level governance, aspect-level governance, and Self-level governance each hold within their respective scopes. Modularity makes units composable across governance scopes; it does not collapse those scopes into one. Human authority over substrate content and orchestration rules operates at each level independently.

**Modularity does not prescribe specific implementations.** A1.05 tool-agnosticism holds throughout. The modular architecture is realizable across different substrate technologies; the four commitments do not mandate specific tools, storage formats, or runtime infrastructure. The modularity is a property of the commitment structure, not of its implementation.

**Level distinctions are not eliminated.** Per B2.07, cells, aspects, and Selves have distinct scopes — cell scope is the informational task scope Paper 1 defends; aspect scope is the coordination arrangement scope; Self scope is the integrated whole. Modularity is a property of the architectural structure; it does not make the three scopes equivalent or interchangeable.

**Modularity is not uniformity.** Modular units may have highly varied internal specifications, orchestration rules, content types, and governance configurations while sharing the modular interfaces the four commitments specify. Modularity is a property of the interfaces and structural participation modes, not of internal consistency across units.

## 8. Operational test

A CKS architecture instantiates modularity as architectural consequence if and only if: (1) every substrate-governed unit — cell, aspect, and Self — has a boundary defined by A1.02 specifying its interior and exterior; (2) compositions of those units satisfy the five A1.13 composition requirements; (3) all interactions between units and adjacent components occur through one of the three A1.14 adjacencies; and (4) every unit's participation in a larger composition follows one of the three A1.16 hybrid composition patterns. When all four conditions hold at every level at which the architecture operates, the modularity is present as architectural consequence. When any one fails, the modularity is incomplete in the specific way that commitment's absence produces.

## 9. Conclusion: why standalone formalization matters and the decomposition sequence

The prior-art consequence of treating modularity as architectural consequence rather than engineering choice is specific. An architecture whose modularity is the consequence of four identifiable commitments inherited from Paper 1 cannot be claimed as novel modularity by a later party — the modular architecture is present wherever the four commitments are satisfied, and that presence predates any such later claim. The standalone formalization makes the consequence relationship explicit, citable, and checkable.

Within the derivation sequence, B2.35 establishes the foundational specification on which B2.36 (composition configurability through modularity), B2.37 (modularity enabling vertical evolution per B1.16), B2.38 (modularity across cross-partner compositions), and B2.39 (modularity verification) each depend. B2.36 through B2.39 are operationalizations of specific downstream capabilities that the modular architecture produces; they inherit the specification this note establishes. After B2.39 completes the B1.08 decomposition, Phase B2 continues with the B1.09 birth decomposition at B2.40–B2.44.

The formalization is also the anchor for cross-series references: B2.11's operationalization of cell-level modularity within Paper 2 structures, B1.16's bidirectional evolution commitment, B1.17's relational structural roles commitment, and the composition decomposition notes at A2.91–A2.95 and A4.27–A4.29 all depend on the modularity being architecturally specified rather than assumed. B2.35 provides that specification.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Modularity as Architectural Consequence: Formalizing How Paper 2's Structural Modularity Emerges from Four Paper 1 Architectural Commitments.* May 12, 2026. ORCID: 0009-0004-8065-3235. [Derivation note B2.35, CKS series.]
