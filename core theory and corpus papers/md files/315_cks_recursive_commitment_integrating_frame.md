# Recursive Commitment Integrating Frame: The Same Governance Architecture Applies at Cell Scope, Aspect Scope, and Self Scope

**A derivation note from the Coordination Knowledge Substrate (CKS) pattern — Series B, Phase B2, Note B2.98**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the precise meaning of recursive commitment as that concept is used in the source paper, so that downstream work can adopt or argue against the concept without ambiguity.

## Abstract

Paper 2 (Li, April 2026) specifies, through its foundational architectural commitment B1.20, that Paper 1's governance commitments apply recursively at cell scope, aspect scope, and Self scope. This note formalizes what that recursive application means as an architectural specification. A commitment is recursive, in this context, when it applies at each structural level with that level's scope — the same commitment, at different scopes, rather than a deployment-level commitment that governs only the outermost shell. What changes per level is scope: cell scope covers the cell's operational territory; aspect scope covers the aspect's coordination domain; Self scope covers the Self's integration span. What does not change is the principle: A1.01 governance, A1.07 retraceability, A1.08 substrate-as-source-of-truth, A1.10 determinism, A1.12 labor allocation, A1.13 composition requirements, A2.01–A2.04 governance affordances, A2.40 provenance, and A2.46 authoritative content each apply at all three levels. The architectural significance of recursive application is that every entity at every structural level operates under Paper 1 governance — not just the deployment as a whole. Without recursive application, cells and aspects could operate entirely outside Paper 1 governance while the deployment was nominally governed only at the top level. Recursive application makes CKS a coherently governed architecture rather than a governed shell around ungoverned components. This note opens the thirteen-note B1.20 decomposition (B2.98–B2.110), the final Phase B2 decomposition.

---

## 1. Why the recursive-commitment-integrating-frame needs to be formalized as a standalone operational variant

Phase B2 of Series B has decomposed each of Paper 2's twenty foundational architectural commitments (B1.01–B1.20) into the operational variants that make the commitment precise enough for downstream adoption, extension, and argument. The B1.20 decomposition is the final decomposition in Phase B2, and B2.98 is its opening note.

B1.20 establishes that Paper 1's governance commitments apply recursively at cell scope, aspect scope, and Self scope. That claim is architecturally load-bearing in a distinctive way: it is not a claim about any single commitment in isolation but about the structural relationship between the three-level architecture (B1.02) and the full set of Paper 1 commitments. Every subsequent note — B2.99 through B2.110 — depends on the recursive-commitment frame being precisely specified first. Without it, per-commitment recursive treatments risk equivocation: does "A1.01 applies at cell level" mean the same governance principle applies at cell scope, or does it mean a cell-specific mechanism is added on top of the Paper 1 commitment?

The recursive-commitment-integrating-frame formalizes that recursive means: the same governance principles, applied at different scopes, at each structural level. This is the integrating frame because it holds the thirteen-note decomposition together. The per-commitment applications (B2.99–B2.108) are specifications of this frame for individual commitments; B2.109 presents recursive operational tests; B2.110 closes the decomposition and completes Phase B2.

By formalizing recursive-commitment-as-architectural-specification as a named, dated, attributed concept, this note establishes public prior art that any subsequent claim to recursive governance in multi-level AI architectures must navigate.

---

## 2. The architectural frame precisely stated

**The recursive definition.** A commitment is recursive when it applies at each structural level with that level's scope. This is a specific definition, not an informal use of the word recursive. The recursion is not procedural (a function calling itself) but structural: the same governance principle is instantiated at each level, with the level supplying the scope of instantiation. Three levels produce three instantiations; one principle governs all three.

**What changes per level: scope.** At cell scope, a commitment applies to the cell's operational territory — the specific coordination task or domain for which the cell was instantiated. At aspect scope, the same commitment applies to the aspect's coordination domain — the purpose-defined arrangement of cells that constitutes the aspect. At Self scope, the commitment applies to the Self's integration span — the full enterprise scope across all aspects. Scope is not a fixed magnitude but a level-determined boundary. The cell's scope is narrower than the aspect's scope; the aspect's scope is narrower than the Self's scope. Recursive application does not require identical scope — it requires that the principle be applied at whatever scope is level-appropriate.

**What does not change: the principle.** A1.01 governance is A1.01 governance whether the level is cell, aspect, or Self. The commitment that humans hold authority — the rights to inspect, modify, and override substrate content and orchestration rules at any time — does not change based on which level holds it. A1.08's commitment that the substrate is the source of truth does not become a different commitment at aspect level; it becomes the same commitment applied to the aspect's substrate. A1.07 retraceability is retraceability at every level. Principle invariance under scope change is the defining characteristic of recursive application.

**Recursive application examples.** Three commitments illustrate the frame. A1.01 governance: humans govern cell-level behavior through cell DNA, aspect-level coordination through aspect DNA, and Self-level integration through Self DNA — human authority applies at each level's scope, not only at Self scope. A1.08 substrate-as-source-of-truth: cell substrate, aspect substrate, and Self substrate each hold authoritative state for their level's operations — the commitment is level-instantiated, not a single centralized truth. A1.07 retraceability: cell operations are retraceable through cell lineage, aspect operations through aspect lineage, Self operations through Self lineage — retraceability is instantiated at each level, not delegated upward.

**Why recursive application is architecturally significant.** Without recursive application, Paper 1 commitments would apply only at deployment level: the deployment as a whole is governed, but the individual cells and aspects that compose it operate without their own level-appropriate governance. Cells could generate outputs, make routing decisions, and record state outside the A1.08 substrate-as-source-of-truth commitment. Aspects could coordinate without the A1.01 authority structure applying to their coordination substrate. The deployment would be a governed shell containing ungoverned components. Recursive application closes this gap: every entity at every level operates under Paper 1 governance at its level-appropriate scope.

**Recursion does not collapse levels.** The three-level structure (B1.02) maintains distinct scopes — cell scope, aspect scope, and Self scope are not interchangeable. Recursive application does not mean that governance at cell level is the same as governance at Self level; it means the same governance *principle* applies at different *scopes*. A cell's substrate and a Self's substrate are not the same substrate. A cell's orchestration rules and a Self's orchestration rules are not the same rules. The recursion preserves level distinctions while extending principles across them.

---

## 3. What makes recursive-commitment-integrating-frame architecturally distinctive

The conventional approach to governance in multi-component AI architectures is top-level governance: the deployment is governed, but individual models and services operate without their own level-appropriate governance framework. Components are governed only insofar as they are components of a governed deployment.

CKS recursive commitment is architecturally different. The difference is not a matter of degree (more logging, more oversight) but of structural location: governance is a property of every entity at every structural level, not only of the deployment as a whole. Each cell, each aspect, and the Self each carry their own instantiation of Paper 1 governance commitments at their level-appropriate scope.

This difference produces entity-level compliance demonstration. In a top-level-only governance architecture, compliance is deployment-level; there is no architectural basis for per-component compliance demonstration because the components do not carry governance commitments at their own scope. In a recursive-commitment architecture, compliance can be demonstrated at cell level, aspect level, and Self level independently — a cell's A1.08 compliance can be assessed from the cell's own substrate and lineage records without auditing the full deployment. Entity-level audit capability is the architectural consequence of governance being a property of entities rather than of deployments.

---

## 4. The biological analog as conceptual scaffold

The biological analog for recursive commitment is regulatory architecture at multiple organizational levels. In biological systems, cells, tissues, and organs each have their own regulatory mechanisms — yet the same fundamental biological principles (DNA-based operation, membrane integrity, metabolic governance) govern at all levels. Biology does not govern only at the organism level while leaving cells to operate without regulatory mechanisms. The regulatory architecture is instantiated at each organizational level with that level's scope.

CKS recursive commitment is the governed architectural analog: the same governance principles (Paper 1 commitments) apply at each structural level (cell, aspect, Self) with that level's scope. The biological analog functions as conceptual scaffold — a way to render the recursive architecture intuitive — but the architectural substance is the same governance principles at each structural scope, not an attempt to map biological mechanisms onto software systems. Paper 1 commitments are foundational at cell scope; the three-level architecture (B1.02) composes those commitments at higher scopes through recursive application.

---

## 5. The inherited Paper 1 commitments that apply recursively

B1.20's claim is that all Paper 1 commitments apply recursively. This note catalogs the full scope of that claim; per-commitment treatments follow in B2.99–B2.108.

**A1.01 — Human-governed: authority not labor.** Human authority (inspect, modify, override) over substrate content and orchestration rules applies at cell scope, aspect scope, and Self scope. Authority is level-instantiated, not a deployment-level wrapper.

**A1.07 — Path retraceability.** The provenance metadata requirement applies at each level. Each level maintains its own lineage record.

**A1.08 — Substrate as source of truth.** Authoritative state lives in the substrate at each level. Cell substrate, aspect substrate, and Self substrate each hold authoritative state for their level's operations.

**A1.10 — The determinism contract.** The determinism guarantees apply at each level with level-appropriate scope.

**A1.12 — Labor allocation: three modes.** Direct human labor, LLM-under-rule labor, and stable-cell labor apply at each level, with the level's coordination domain as the relevant scope.

**A1.13 — Composition requirements.** No new primitives are required for each level; levels compose from existing primitives. Cells satisfy composition requirements within aspects; aspects satisfy composition requirements within Selves.

**A2.01–A2.04 — Governance affordances.** The four governance affordances apply at each structural level with level-appropriate scope.

**A2.40 — Provenance.** Cell lineage, aspect lineage, and Self lineage each satisfy the provenance commitment for their level's operations.

**A2.46 — Authoritative content.** Cell substrate content, aspect substrate content, and Self substrate content each satisfy the authoritative-content commitment for their level.

The catalog matters for the prior-art record. The claim is not that governance applies recursively in some general sense but that each named Paper 1 commitment applies at each named structural level. That specificity is what makes the recursive frame a precise architectural specification rather than an informal aspiration.

---

## 6. Operational implications

**Apply Paper 1 at each entity level, not only at deployment level.** A deployment satisfying B1.20's recursive commitment applies Paper 1 commitments at cell scope, aspect scope, and Self scope — not only at the deployment level. A deployment that applies Paper 1 commitments only at the top level while leaving cells and aspects without level-appropriate governance satisfies the form of Paper 2's architecture without satisfying the recursive commitment.

**Entity-level compliance demonstrations are possible.** Because governance is a property of entities rather than only of deployments, compliance can be demonstrated at cell level, aspect level, and Self level independently. A cell's substrate can be audited against A1.08's authoritative-state categories using the cell's own substrate and lineage records, without auditing the full deployment. An aspect's DNA can be audited against A1.01's authority structure. These are direct entity-level compliance assessments, not proxies for deployment-level compliance.

**Every component is independently auditable.** Entity-level audit capability follows from recursive commitment without additional architectural mechanisms. The same audit methods that apply to a single-cell Paper 1 deployment apply to each cell in a Paper 2 deployment — the cell's own substrate and lineage records are the audit target.

---

## 7. Limits of recursive-commitment-integrating-frame

**Not identical application.** Recursive application does not mean that every commitment is applied identically at every level. Scope differences can produce differences in instantiation. A1.12's labor allocation framework applies at each level, but the specific allocation pattern at Self scope may differ from the pattern at cell scope because the coordination tasks differ. The recursion is principle-preserving, not form-preserving. Level-appropriate variations within the same principle are expected and permitted.

**Not three separate governance systems.** Recursive application does not create three independent governance systems that happen to share the same principles. It is one governance architecture applied at three nested scopes. Cell scope is contained within aspect scope; aspect scope within Self scope. Governance at one level interacts with governance at adjacent levels through composition relationships (B1.02).

**B1.20 is the Paper 2 claim; per-commitment applications are formalized in B2.99–B2.108.** B2.99 formalizes cell-level Paper 1 commitments; B2.100 aspect-level; B2.101 Self-level; B2.102–B2.108 per-commitment recursive applications; B2.109 recursive operational tests; B2.110 closes the decomposition and completes Phase B2. This note does not propose recursive governance products, multi-level compliance frameworks, or entity-level audit tools — the formalization is of the architectural specification.

---

## 8. One-sentence test

A three-level CKS deployment satisfies the recursive-commitment frame if and only if each Paper 1 commitment can be assessed at cell scope, at aspect scope, and at Self scope independently — using each level's own substrate and lineage records — without requiring access to a higher-level substrate to establish compliance.

---

## 9. Why naming the recursive-commitment-integrating-frame as a standalone concept matters

The recursive-commitment-integrating-frame is not a consequence that follows automatically from combining B1.02's three-level structure with Paper 1's commitment list. It is a specific architectural decision: to extend governance principles downward through all structural levels rather than to govern only at the top. A three-level architecture could have been specified with governance only at Self scope and operational freedom at cell and aspect scope. B1.20's claim that Paper 1 commitments apply recursively is the specification that rejects that alternative, and the recursive-commitment-integrating-frame is the architectural form that claim takes.

By naming the frame as a standalone concept, this note establishes that the recursive extension of governance principles through structural levels is a design choice with a specific architectural form, not an informal property. Downstream work that adopts the frame inherits its precision; downstream work that departs from it can name the departure against a defined standard.

This note opens the B1.20 decomposition (B2.98–B2.110) — the thirteen notes that together constitute the complete recursive Paper 1 commitments treatment for Paper 2's three-level architecture, and the final Phase B2 decomposition. The recursive-commitment-integrating-frame is the architectural foundation on which the remaining twelve notes stand.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). Recursive Commitment Integrating Frame: The Same Governance Architecture Applies at Cell Scope, Aspect Scope, and Self Scope. Series B, Phase B2, Note B2.98. May 12, 2026. ORCID: 0009-0004-8065-3235.
