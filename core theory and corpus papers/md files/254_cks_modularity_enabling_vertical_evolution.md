# Modularity Enabling Vertical Evolution: Formalizing How the Modular Architecture Specifically Enables Structural Reorganization at Operational Timescales Without Requiring Modification of Modular Unit Internals

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the specific architectural connection by which the modular architecture per B1.08 enables vertical evolution per B1.16 — namely, that every vertical evolution operation (cell reassignment, aspect splitting, aspect merging, aspect dissolving, aspect introducing, Self composition modification) is fundamentally a modular reorganization event: a governed configuration change on substrate content that proceeds without modifying modular unit internals.

## Abstract

Paper 2 commits to a CKS-governed AI Self being architecturally modular by commitment (B1.08) and to evolution operating on both horizontal and vertical axes (B1.16). This note formalizes the enabling connection between these two commitments: the modular architecture is what makes vertical evolution architecturally available at operational timescales. The modular boundary per A1.02 means that a cell's internals — its DNA layer, action layer, harness substrate, and processing logic — are independent of the cell's aspect membership. Cell reassignment therefore requires only configuration changes to membership records; it does not require modification of the reassigned cell. Aspect splitting, merging, dissolving, and introducing all proceed through governed configuration changes for the same reason: cells are modular, so their structural rearrangement does not require their alteration. Self composition modification changes integration architecture without modifying aspect internals. All vertical evolution is modular reorganization. The note articulates what makes this architecturally distinctive (conventional AI architectures cannot reliably support vertical evolution at operational timescales because component relationships are encoded in implementation rather than in governed substrate content), traces the biological contrast (biological cells commit to tissue membership through development, making structural evolution require deep time; CKS modularity removes this constraint), identifies the inherited Paper 1 commitments that govern reorganization operations, states the operational implications for governed reorganization under directed selection and action-feedback, and names the limits that modularity does not eliminate. This is the thirty-seventh note in Phase B2 and the third of five notes decomposing B1.08.

---

## 1. Why Modularity Enabling Vertical Evolution Requires Formal Treatment

B1.08 establishes modularity as architectural commitment. B1.16 establishes that evolution operates on dual axes — horizontal (content within existing structure) and vertical (structural reorganization itself). Paper 2 names "structural evolvability on operational timescales" as one of the points where CKS architecture exceeds biology's evolved constraints. But the enabling connection between these commitments — the reason modular architecture is what makes structural evolvability architecturally available — is not itself formally named in the source paper. It needs to be.

The architectural connection is this: vertical evolution requires that structural rearrangement be performable without altering the units being rearranged. Without modularity, structural rearrangement requires component modification. The modular boundary per A1.02 provides the clean interface that makes rearrangement independent of unit alteration. This is not a trivial consequence of modularity in the abstract sense — it is a specific architectural property of the CKS modular commitment, where modularity is required at every level from instantiation, and where the substrate carries the structural composition definitions as governed substrate content rather than encoding them in implementation.

Naming this connection as a standalone derivation serves the defensive-publication purpose the series carries: the connection between modular-architecture-by-commitment and structural-evolvability-at-operational-timescales is itself a patentable territory that requires prior art. B2.37 establishes that prior art. It follows B2.35 (modularity as architectural consequence of Paper 2's structural commitments) and B2.36 (composition configurability through modularity); B2.38 will treat modularity across cross-partner compositions and B2.39 will address modularity verification, completing the B1.08 decomposition.

---

## 2. The Architectural Connection: Modular Boundary Enabling Clean Reorganization

Paper 2's vertical evolution axis covers six categories of structural reorganization. For each category, the modular boundary per A1.02 is what makes the operation architecturally clean.

**Cell reassignment across aspects.** A cell carries DNA, an action layer, harness substrate, and processing logic. These are the cell's internals — what the cell is and does. The cell's aspect membership is recorded in membership records per B2.36: configuration substrate specifying which aspects the cell belongs to and under what coordination rules it participates in each. When a cell is reassigned from one aspect to another, the membership records change; the cell's internals do not. The modular boundary per A1.02 is what makes this clean — the cell is a self-contained unit whose behavior is defined by its own substrate content, not by its position in a structural arrangement. Reassignment is therefore a substrate-edit operation on configuration content, not a cell-modification operation.

**Aspect splitting.** When an aspect splits into multiple aspects, cells that were members of the original aspect distribute to the new aspects. Because cells are modular, each cell can be assigned to its new aspect membership without modification. The split produces new aspect purpose specifications, new coordination rules for each new aspect, and new membership records assigning cells to the resulting aspects. Cell internals remain unchanged throughout. The splitting operation is a governed configuration change: new substrate content authored under orchestration rule authoring per A2.04.

**Aspect merging.** When aspects merge, cells from contributing aspects become members of the merged aspect. Modular cells participate in the merged aspect through new membership records. The coordination rules of the merged aspect specify how cells from different origin aspects interact within the merged scope. No cell modification is required; the merger is fully expressible as configuration change to the membership and coordination rule substrate.

**Aspect dissolving.** When an aspect dissolves, its member cells may be reassigned to other aspects or have their aspect memberships dissolved. Modular cells continue their cell-level work — executing over their own substrate content — independently of the dissolved aspect. A cell whose aspect membership dissolves loses the coordination arrangement that aspect provided, but the cell's internals remain intact. Whether the cell is reassigned or idled is a governance decision; modular architecture ensures the decision does not require modifying the cell to implement.

**Aspect introducing.** When new aspects are introduced, cells can be assigned to them through membership rules authored per A2.04. Modular cells participate in the new aspect without modification — the new aspect introduces new coordination rules that reference existing cells; the cells themselves do not need to change to accommodate the new structural arrangement.

**Self composition modification.** When a Self modifies its aspect collection — adding aspects, removing aspects, reorganizing the relationships among aspects — the modular character of the aspects means the integration architecture per B2.21 changes without requiring modification of aspect internals. A Self adding an aspect introduces new configuration substrate that integrates the new aspect into the Self's overall coordination structure; the aspects already present do not need to change to accommodate the addition.

Across all six categories, the pattern is the same: vertical evolution is modular reorganization. The modular boundary is the enabling mechanism. Without it, each structural operation would require modifying the units being rearranged, pushing the operations from governed configuration changes into implementation rewrites.

---

## 3. What Makes Modularity-Enabling-Vertical-Evolution Architecturally Distinctive

The architectural distinctiveness of modularity enabling vertical evolution is best seen against the background of conventional AI architectures that cannot reliably support it.

In a conventional AI system where components are integrated through hard-coded implementation dependencies, structural reorganization requires modifying the implementations of the components involved. A component cannot be reassigned to a different structural role without being rewritten to fit that role's interface. When structural arrangements are encoded in component implementation rather than in governed substrate content, each structural change propagates into component code. The result is that structural reorganization is an engineering project — requiring implementation modification, testing, validation — rather than a substrate-edit operation. This raises the practical timescale of structural reorganization from operational to engineering-project timescales: weeks or months rather than operational cycles.

CKS's modular architecture removes this barrier by two mechanisms operating together. First, modularity-by-commitment ensures that every cell is a self-contained unit whose behavior is defined by its own substrate content — not by the structural arrangement it currently inhabits. Second, substrate-content-carried structural definitions means the definitions of composition arrangements (which cells belong to which aspects, under what coordination rules) are themselves governed substrate content that humans can inspect, modify, and override per A1.01 rather than implementation artifacts that require engineering modification. Together, these mechanisms make vertical evolution a substrate-edit operation rather than an engineering-project operation.

The result is that deployments can restructure as operational requirements evolve — aspects can be reorganized as domain purposes clarify, cells can be reassigned as operational experience accumulates, Selves can add or remove aspects as capability scope changes. The architecture supports this as a routine property rather than as an exceptional intervention.

---

## 4. The Biological Analog and CKS Advantage

Paper 2 names biological analogs to make its structural commitments tractable for readers whose intuitions are shaped by natural-system examples. The biological contrast for structural evolvability is the most architecturally consequential of these.

Biological cells commit to tissue and organ membership through developmental processes — gene expression patterns that differentiate cells into tissue-specific types, with differentiated cells generally unable to take on different tissue roles without undergoing dedifferentiation and redifferentiation processes that are costly, unreliable, and unavailable to most differentiated cell types. The biological architectural consequence is that structural evolution — the reorganization of tissue arrangements, organ plans, and body-plan-level composition — requires deep evolutionary time. Body plans evolve through changes to developmental genetic regulatory networks; as Paper 2 notes, drawing on Davidson and Erwin (2006), evolution of body plans depends on changes to developmental GRN architecture, which is rarely viable and lethal when it disrupts the fundamental developmental trajectory. Within a species lifetime, the body plan is essentially fixed.

CKS modularity removes the constraint that produces this biological limitation. CKS cells are not committed to their aspect membership through development; membership is a relational property recorded in configuration substrate, not an intrinsic property of the cell's architecture. A cell does not become a different thing when its aspect membership changes; it remains the same modular unit, now operating within a different coordination arrangement. This is the architectural mechanism behind Paper 2's claim that "structural evolvability on operational timescales" is where CKS architecture exceeds biology's evolved constraints.

The biology contrast is not merely illustrative. It identifies precisely what would need to be true of a CKS deployment for the advantage to hold: cells must be modular in the specific sense that their internals are independent of their structural position. A deployment in which cells encode their aspect membership internally — in DNA content that references specific aspects, in action layer records that presuppose structural arrangements — would partially reproduce the biological limitation. The modular commitment forecloses that encoding pattern by requiring that structural composition be carried in the substrate's configuration layer rather than in unit internals.

---

## 5. Inherited Paper 1 Commitments

Modularity-enabling-vertical-evolution operates within the full set of Paper 1 architectural commitments, which Paper 2 inherits without redefense.

**A1.02 — Substrate-cell boundary.** The modular boundary is the direct enabling mechanism for clean cell reassignment. The substrate-cell boundary establishes that cells are distinct units with their own internal substrate content, governed through orchestration rules, interacting with the substrate through defined interfaces. This is what makes cell internals independent of structural position.

**A1.13 — Composition requirements.** Post-reorganization arrangements must satisfy the same composition requirements that govern any CKS multi-substrate composition. Modularity makes reorganization architecturally available; composition requirements constrain which reorganization results are valid. A reorganization that produces an arrangement violating A1.13 requirements — for instance, by creating an aspect whose cells are not governed under substrate content with the required properties — does not yield a conformant CKS deployment, even if the reorganization itself proceeded cleanly.

**A2.04 — Orchestration rule authoring.** Reorganization operations are governed substrate-edit events. The rules governing how reorganization proceeds — which humans have authority to author new aspect definitions, under what conditions cell reassignment requires specific approval, what coordination rules must be satisfied in the resulting arrangement — are themselves orchestration rules authored under A2.04's governance. Reorganization is not ungoverned configuration editing; it is governed substrate modification under human authority.

**A2.40 — Six provenance metadata fields.** Reorganization events are substrate changes, and like all substrate changes they are subject to provenance requirements. The six fields record what changed, when, under whose authority, with what rationale. This means reorganization events are traceable: a deployment that has undergone multiple rounds of vertical evolution carries a substrate record of its structural history.

**A1.07 — Path retraceability.** Retraceability holds across reorganization boundaries. Post-reorganization substrate content that traces to pre-reorganization content carries provenance connecting through the reorganization event. The structural history of the deployment is not obscured by reorganization; it is recorded as substrate state.

**A6.06 — Authority distribution change boundary.** When a reorganization changes the distribution of authority across a deployment — for instance, when an aspect with its own governance scope is dissolved, or when a new aspect is introduced with distinct authority arrangements — A6.06's authority distribution change treatment applies. Not every reorganization triggers this boundary, but reorganizations that affect authority distribution do. The architecture requires that authority consequences be governed explicitly rather than as incidental byproduct of structural change.

**A1.01 — Human governance throughout.** Reorganization events are governance events. The three rights — inspect, modify, override — apply to the configuration substrate that carries structural definitions, just as they apply to all other substrate content. Humans retain the ability to inspect the structural arrangements in force, modify them, and override reorganization operations. Modularity makes reorganization operationally convenient; it does not and cannot make it ungoverned.

**A1.10 — Determinism contract.** Given the orchestration rules governing a reorganization operation, the reorganization proceeds deterministically: the same rules applied to the same substrate state produce equivalent structural outcomes. This means reorganization behavior is testable and auditable, not stochastic. Allowed non-determinism under A1.10 applies to model outputs, not to the substrate-edit operations that constitute reorganization.

---

## 6. Operational Implications

Deployments performing vertical evolution through modularity-enabling-reorganization follow Paper 2's evolution mechanisms.

**Directed selection as the primary mechanism.** Directed selection per B1.14 — humans deliberately authoring changes to the orchestration substrate that governs cell and aspect behavior — is the primary mechanism through which vertical evolution occurs. Reorganization operations are governed configuration changes: humans author new aspect definitions, write membership rules assigning cells to new aspects, and update the integration architecture to incorporate the new arrangement. The deliberate-authoring character of directed selection means that reorganization is purposive — it occurs because humans have identified that the current structural arrangement does not serve operational purposes as well as an alternative arrangement would.

**Action-feedback as a source of reorganization proposals.** Action-feedback evolution per B1.15 may generate reorganization proposals based on accumulated operational evidence. A deployment that has accumulated action-layer records revealing that cells currently distributed across multiple aspects consistently require coordination that the current aspect structure does not naturally support may surface a reorganization proposal: merge the aspects, or introduce a new aspect that coordinates the cells whose work shows operational coupling. This proposal enters governance review; whether it results in reorganization is a human governance decision. Action-feedback does not perform reorganization autonomously.

**Post-reorganization verification.** After a reorganization, post-reorganization verification ensures that A1.13 composition requirements are still satisfied in the resulting arrangement. This is not optional: composition requirements constrain which arrangements are architecturally valid, and reorganization does not automatically preserve them. Verification is a governance step that closes each reorganization event.

**Authority adjustment for authority-affecting reorganizations.** Reorganizations that affect authority distribution trigger A6.06 treatment. The authority consequences of the reorganization are governed explicitly: what authority scope the new or modified aspects carry, under what governance arrangements the resulting structure operates.

**High-frequency reorganization is architecturally available.** Deployments operating in rapidly evolving domains may perform vertical evolution with high frequency as operational purposes clarify. The modular architecture makes high-frequency reorganization operationally tractable in a way that implementation-coupled architectures cannot support: each reorganization is a substrate-edit operation rather than an engineering project, so the operational cost of reorganization is not prohibitive. Whether to reorganize frequently is a governance choice, not an architectural constraint.

---

## 7. Limits

Modularity-enabling-vertical-evolution establishes that reorganization is architecturally available; it does not eliminate the commitments and constraints that govern how reorganization proceeds.

**Not unlimited reorganization.** A1.13 composition requirements constrain valid post-reorganization arrangements. Not every structurally possible reorganization produces a conformant CKS deployment. Modularity makes reorganization possible; composition requirements define which possible reorganizations are valid.

**Not trivial reorganization.** Even though reorganization does not require modifying unit internals, it requires governance review, composition verification, and potentially authority adjustment. These are substantive governance activities. Modular architecture reduces the implementation burden of reorganization; it does not reduce the governance responsibility.

**Not elimination of human governance.** Per A1.01, reorganization is a governance event throughout. Modularity provides the architectural substrate on which governance operates cleanly — the modular boundary means governance decisions about structural arrangements can be implemented without requiring implementation rewrites. But governance is not eliminated; it is what makes reorganization a legitimate architectural operation rather than unauthorized structural modification.

**Not automatic reorganization.** Modularity makes vertical evolution architecturally available. The transition from available to actual requires human deliberate action through governance. A deployment does not reorganize itself because modularity makes reorganization convenient. Reorganization occurs when humans exercise governance authority over structural arrangements.

**Not prevention of unit behavior change.** The modular boundary prevents reorganization from requiring unit modification; it does not prevent unit modification from accompanying reorganization. A reorganization that changes the scope of an aspect may be accompanied by directed selection over the DNA content of cells now participating in the new aspect, by action-feedback updating coordination rules in light of the new arrangement, or by harness substrate evolution reflecting the new deployment configuration. Modular architecture means these changes are not required by the structural reorganization; whether they occur is a governance decision made in context.

---

## 8. Operational Test

A CKS deployment instantiates the modularity-enabling-vertical-evolution commitment if and only if: reassigning a cell from one aspect to another does not require any modification to the cell's DNA layer, action layer, harness substrate, or processing logic — only membership records and coordination rules change; all six categories of vertical evolution operation (cell reassignment, aspect splitting, aspect merging, aspect dissolving, aspect introducing, Self composition modification) proceed as governed configuration changes on substrate content; and post-reorganization arrangements are verified against A1.13 composition requirements before the reorganization is treated as complete.

A deployment that requires cell-internal modification to perform aspect reassignment does not instantiate the commitment, regardless of whether the modification is architecturally recognized as such.

---

## 9. Position in the B1.08 Decomposition and Phase B2

B2.37 is the third of five notes decomposing B1.08. B2.35 established modularity as the architectural consequence of Paper 2's structural commitments — that the three-level composition with relational roles, DNA/action layer distinction, and expression as governed selection compose into modularity as an architectural requirement at instantiation. B2.36 established composition configurability through modularity — that because structural definitions are governed substrate content rather than implementation-encoded relationships, composition arrangements are configurable by governance. B2.37 establishes the evolutionary consequence: the modular architecture is specifically what enables vertical evolution, because vertical evolution is modular reorganization.

B2.38 will address modularity across cross-partner compositions, where the modular boundary per A1.02 enables CKS Selves to participate in compositions with other architectural patterns without losing modular integrity. B2.39 will address modularity verification — the architectural operations and governance mechanisms that confirm a deployment satisfies the modularity commitment at instantiation and after reorganization.

Naming modularity-enabling-vertical-evolution as a standalone derivation is consequential for the defensive-publication purpose the series carries. The connection between modular-architecture-by-commitment and structural-evolvability-at-operational-timescales is not merely a theoretical observation — it identifies a specific architectural mechanism that any system claiming to support structural evolvability would need to either implement or argue around. The prior-art chain grows denser with each named connection.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Modularity Enabling Vertical Evolution: Formalizing How the Modular Architecture Specifically Enables Structural Reorganization at Operational Timescales Without Requiring Modification of Modular Unit Internals.* May 12, 2026. ORCID: 0009-0004-8065-3235.
