# Recursive Composition Requirements (A1.13): Nested Validity at Cell, Aspect, and Self Scope

**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** May 12, 2026  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize, as a standalone operational variant, how A1.13 composition requirements apply recursively across the three architectural levels Paper 2 defines: cells composing within aspects, aspects composing within Selves, with nested composition validity verified at each level through the A5.14 composition-requirements-five test.

## Abstract

Paper 2 specifies, through its B1.20 recursive Paper 1 commitments treatment, that Paper 1's composition requirements commitment (A1.13) applies at every architectural level: cell, aspect, and Self. This note formalizes that application as recursive composition requirements — A1.13 at cell scope, A1.13 at aspect scope, and A1.13 at Self scope — with A5.14 serving as the verification mechanism at each scope. The central structural feature is the dual role of aspects: aspects are both composed entities that must satisfy composition requirements within Selves, and composing environments that must enforce composition requirements for their cells. Nested composition validity follows from this structure: a deployment is compositionally valid when each cell is compositionally valid within its aspects, each aspect is compositionally valid within its Selves and enforces composition for its cells, and each Self enforces composition for its aspects. Composition failures propagate: a cell that fails composition within an aspect affects that aspect's composition validity within its Self. This note is the ninth of thirteen notes decomposing B1.20.

---

## 1. Why recursive-composition-requirements-A1.13 requires standalone formalization

Paper 2 introduces three structural levels — cell, aspect, and Self — that Paper 1 does not define. Paper 1's A1.13 specifies that entities participating in composed deployments must satisfy composition requirements; with the introduction of three levels, the question of which composition requirements apply at which level must be answered explicitly. Paper 2's B1.20 recursive Paper 1 commitments treatment provides the answer: all Paper 1 commitments hold at every level, and A1.13's composition requirements are no exception. But the recursive application of A1.13 is more structurally complex than the recursive application of most other Paper 1 commitments, because composition is inherently relational — it describes how entities fit within composing environments — and Paper 2 introduces two distinct composing environments (aspects for cells, Selves for aspects) along with one entity type that occupies both roles simultaneously (aspects).

That dual role is what makes formalizing recursive A1.13 non-trivial. An aspect must simultaneously satisfy composition requirements in the upward direction — within its Self — and enforce them in the downward direction — over its cells. No other entity in the three-level architecture occupies this reflexive position: cells are only composed, Selves are only composing in single-Self deployments. The prior eight notes in the B1.20 decomposition — B2.98 through B2.105, covering cross-lineage mating compatibility, structural evolvability, retraceability, and five per-commitment formalizations — established the recursive application of individual Paper 1 commitments without needing to address nested composition validity. B2.106 addresses it directly.

The strategic purpose of naming recursive composition requirements as a standalone operational variant is defensive prior-art positioning: the nested composition validity structure, the dual role of aspects within it, and the per-level application of A5.14 constitute patentable architectural territory that requires explicit formalization to occupy. An architecture in which composition requirements apply in a nested, level-specific, bidirectional manner — with a verification mechanism applied at each scope — differs from conventional composition architectures in ways that each require naming before they can be claimed as prior art.

---

## 2. The recursive application of A1.13, precisely stated

### A1.13 at cell scope — cells composing within aspects

Four composition requirements apply to a cell for it to be compositionally valid within an aspect.

First, the cell must have a complete birth specification per B2.40. A cell that has not completed its birth specification is not compositionally available: its substrate state, orchestration rules, and DNA-layer content are not settled enough to define composition compatibility. Birth-specification completeness is the precondition for all other composition requirements, because an incomplete specification does not fully define what is being composed.

Second, the cell's content-domain per B1.18 must be compatible with the aspect's content-domain. This semantic requirement, formalized in B2.92, distinguishes CKS recursive A1.13 from interface-only composition: two entities with matching interfaces but incompatible content-domains are not compositionally valid. An aspect operating over clinical-care-delivery content cannot coherently compose a cell whose content-domain is supply-chain logistics without an explicit compatibility specification.

Third, the cell must satisfy Paper 1 commitments at cell scope per B2.99. A cell that fails the human-governed commitment, the conflict-preservation commitment, or any other Paper 1 commitment at its own scope is not compositionally valid within an aspect — it would introduce a governance gap or a conflict-handling inconsistency into the aspect's architecture. Composition validity presupposes architectural compliance at the composing entity's own scope.

Fourth, the cell must be distinguishable as a cell per B2.09, which requires a type declaration to be present. Without a type declaration, the composing environment cannot identify the entity as a valid composition participant, and the composition requirement verification cannot be directed at the right scope.

A5.14, the composition-requirements-five test, applied at cell scope verifies all four requirements and determines whether the cell is compositionally valid within its aspect.

### A1.13 at aspect scope — the dual role

Aspects occupy two positions in the composition structure simultaneously, and A1.13 applies in both directions.

As composed entities within Selves, aspects must satisfy composition requirements analogous to those at cell scope: a complete aspect specification per B2.40 (birth requirements at aspect level); content-domain compatibility with the Self's integration scope per B2.92; satisfaction of Paper 1 commitments at aspect scope per B2.100; and distinguishability per B2.09. An aspect that does not satisfy Paper 1 commitments at its own scope — for example, an aspect that does not preserve conflicts arising across its constituent cells — is not compositionally valid within its Self, because it would introduce a first-class commitment failure into the Self's architecture.

As composing environments for their cells, aspects must enforce composition requirements downward. The aspect's coordination rules per B2.16 specify what participation requirements apply to the cells composing into the aspect. The aspect is responsible for verifying that cells it admits satisfy the four cell-scope requirements above. This enforcement responsibility is an architectural commitment, not a deployment option: an aspect that admits cells without verifying composition requirements loses the guarantee that its own composition within a Self is valid, because the Self's composition validity depends in part on whether each aspect properly governs its cells.

A5.14 applied at aspect scope therefore runs in both directions: it verifies the aspect as a composed entity — within its Selves — and as a composing environment — for its cells. Both directions must pass for the aspect to be compositionally valid at its scope. The bidirectional application of A5.14 at aspect scope is architecturally novel relative to the cell and Self applications: it is the only scope at which the test runs in two directions.

### A1.13 at Self scope — the composition apex

Selves enforce composition requirements for their aspects. The Self integration architecture per B2.21 includes aspect composition governance: the mechanisms by which the Self verifies that aspects integrating into it satisfy composition requirements. A Self that admits an aspect without verifying its composition requirements cannot be considered compositionally valid at its scope, because an unverified aspect may fail Paper 1 compliance or content-domain compatibility in ways that undermine the Self's architectural coherence.

The Self is the composition apex in single-Self deployments. There is no higher composing environment within a single-Self deployment that the Self composes into. This does not eliminate A1.13 at Self scope; it means A1.13 at Self scope is entirely a downward-enforcement commitment rather than a bidirectional one. The Self governs composition of its aspects; it does not itself need to satisfy composition requirements within a higher-level entity.

A5.14 applied at Self scope verifies that the Self exercises composition governance over its aspects — that its integration architecture enforces participation requirements and that admitted aspects satisfy composition requirements.

### Nested composition validity

A deployment is compositionally valid when three conditions hold simultaneously. Each cell is compositionally valid within its aspects: the cell satisfies the four cell-scope requirements and A5.14 passes at cell scope. Each aspect is compositionally valid within its Selves and enforces composition for its cells: A5.14 passes in both directions at aspect scope. Each Self enforces composition for its aspects: A5.14 passes at Self scope.

These three conditions nest: the Self's composition validity depends on its aspects' composition validity, which depends in turn on its cells' composition validity. The nesting is not merely definitional; it has operational consequence in the form of failure propagation.

### Failure propagation

A cell failing composition within an aspect — for example, a cell whose content-domain is incompatible with the aspect's content-domain, or a cell that fails Paper 1 compliance at cell scope — does not merely make that cell invalid. It introduces a composition defect into the aspect itself. Because the aspect's composition validity within its Self depends in part on the aspect's governance of its cells' composition, a cell that the aspect has admitted without verifying composition requirements creates a defect at the aspect's scope. That aspect-scope defect propagates: if the aspect is compositionally invalid within its Self, the Self's composition validity is affected.

This propagation is the architectural justification for enforcing composition requirements at each level rather than only at the level where the defect first appears. Composition failures cannot be localized to the level where they originate; they must be addressed at that level to prevent higher-level effects. Governance processes must therefore be capable of tracing defects from where they originate to where they propagate.

### What is constant and what differs across levels

Across all three levels, two things are constant. The composition-requirements principle — that entities must be compositionally valid at their level scope — holds at cell, aspect, and Self scope without modification. And A5.14 is the verification mechanism at each scope; the same test applies to cell composition within aspects, aspect composition within Selves, and Self governance of aspects.

What differs across levels is what composition validity means concretely. At cell scope, composition validity is about fitting within an aspect's coordination environment: birth completeness, content-domain semantic compatibility, Paper 1 compliance, and type identity. At aspect scope, composition validity is bidirectional: fitting within the Self's integration scope and governing cell composition. At Self scope, composition validity is entirely about governing aspect composition — the Self has no higher composing environment to fit within.

---

## 3. What makes recursive A1.13 architecturally distinctive

The contrast with conventional AI architectural composition is direct. In systems where components compose when their interfaces match — API compatibility, message schema alignment, protocol adherence — composition validity is a structural and syntactic property. If input and output types are compatible, the components compose. There is no per-level composition requirement, no semantic content-domain compatibility test, and no recursive enforcement of composition governance at intermediate levels.

Recursive A1.13 creates a different architecture. Composition validity is not merely structural; it is semantic — content-domain compatibility per B2.92 — and governance-based — Paper 1 commitments at cell scope per B2.99 and at aspect scope per B2.100. Two cells with matching interface definitions but incompatible content-domains are not compositionally valid in the CKS sense. A cell whose orchestration rules do not preserve conflicts is not compositionally valid, regardless of whether its interface integrates cleanly with the aspect's API.

The dual role of aspects is the most architecturally distinctive single feature of recursive A1.13. No conventional AI architecture defines an intermediate-level entity that must simultaneously satisfy composition requirements from above and enforce them below. That dual role is what makes nested composition validity coherent: aspects are the layer at which upward compatibility and downward governance meet. Removing the dual role would require either collapsing composition governance entirely to the Self or distributing it entirely to cells, both of which lose the per-level composition guarantees that A5.14 verifies at each scope.

The nested composition validity structure also means that composition validity is sensitive to changes at any level. A change to a cell's DNA that affects its content-domain may invalidate that cell's composition within its aspects. A change to an aspect's coordination rules that affects its content-domain scope may invalidate that aspect's composition within its Self. This change-sensitivity is not a weakness of the architecture; it is the predictable consequence of maintaining semantic and governance-based composition validity rather than interface-only validity, and it is what makes composition validity a genuine architectural guarantee rather than an initial-deployment assertion.

---

## 4. The biological analog

Biological compositional organization provides a useful conceptual scaffold for nested composition validity. Cells must satisfy cell-tissue compatibility requirements to be admitted into a tissue. Tissues must satisfy tissue-organ compatibility requirements to function within an organ. Each level has its own compatibility requirements; meeting requirements at one level does not automatically guarantee requirements at another level. A cell that integrates into one tissue does not automatically integrate into a different tissue operating under different compatibility requirements, even within the same organism.

The biological analog is structurally apt but architecturally bounded. Biology's composition compatibility is implicit — encoded in molecular recognition, adhesion molecules, and developmental signaling pathways — rather than explicit substrate content subject to governance. The composition requirements are not directly inspectable or modifiable by an external authority; they evolve over geological timescales through selection pressure rather than through deliberate governance decisions.

Recursive A1.13 is the governed architectural analog. The composition requirements at each level are explicit substrate content: birth specifications are human-authored documents, content-domain definitions are governed substrate records, Paper 1 compliance properties are verifiable structural conditions. The governing authority holds the right to inspect, modify, and override composition requirements at any time. And A5.14 provides a deterministic verification test at each scope that biology does not have: explicit composition verification rather than implicit compatibility through developmental processes.

The biological analog thus provides the conceptual shape — nested composition requirements at cell, tissue/aspect, and organ/Self scope — while the CKS architecture provides the governed, explicit, verifiable implementation of that shape. The analog is scaffolding, not specification. CKS recursive A1.13's composition requirements are derived from architectural commitments made in Papers 1 and 2, not from any commitment to biological fidelity.

---

## 5. Inherited Paper 1 commitments

Recursive A1.13 inherits and operationalizes five directly load-bearing Paper 1 references.

**A1.13** is the commitment being formalized recursively. Paper 1's composition requirements — that entities participating in composed deployments must satisfy specific requirements — are not modified by Paper 2; they are extended across the three levels Paper 2 introduces. Recursive A1.13 names the per-level extension explicitly, but the underlying commitment is unchanged.

**A5.14**, the composition-requirements-five test, is the verification mechanism at each scope. The same five-point test applies at cell scope, at aspect scope in both directions, and at Self scope. The test is not modified at different levels; its application is directed to the relevant composition relationship at that scope.

**B2.40** birth specification requirements establish that complete specification at birth is a composition requirement at every level. A cell without a complete birth specification is not compositionally valid. An aspect without a complete aspect specification is not compositionally valid. The birth-time composition requirement is the point at which composition validity is first established, and re-verification is triggered whenever changes equivalent in scope to birth-specification changes occur.

**B2.92** content-domain and composition formalizes semantic compatibility as a composition requirement. Content-domain compatibility is not reducible to interface matching; it is a semantic property of the substrate content the cell or aspect carries. This makes A1.13's composition requirements richer than structural composition validity alone and is what distinguishes CKS recursive A1.13 from conventional interface-based composition validation.

**B2.09** distinguishability — the requirement for type declarations to be present — is the minimal structural composition requirement beneath the semantic requirements. Without a type declaration, a composing environment cannot identify whether the entity is a valid composition participant at the right scope. Type declarations are not the whole of composition validity; they are the syntactic floor below which composition verification cannot meaningfully proceed.

---

## 6. Operational implications

**Verify at birth.** Per B2.44, deployments verify composition validity when cells, aspects, or Selves are first established. Birth-time composition verification is the point at which the nested composition validity structure is first instantiated for each entity at each level. An entity that does not satisfy composition requirements at birth cannot be admitted to the deployment's composition structure.

**Re-verify on changes.** A change to a cell's content-domain, a modification to a cell's orchestration rules that affects Paper 1 compliance, or an update to an aspect's coordination rules may affect composition validity at that level and potentially at higher levels. Composition validity maintenance is therefore an ongoing governance activity, not a one-time verification. Governance processes must track which changes can affect composition and trigger re-verification when they do.

**Propagate-aware governance.** Because a cell failing composition within an aspect can affect that aspect's composition validity within its Self, governance processes that operate only at the level where a defect originates are insufficient. When a cell-scope composition failure is identified, the affected aspect's composition validity within its Self must be re-assessed. Propagation-aware governance means that composition defect handling protocols specify the upward-propagation implications of each defect type.

**Dual-role governance for aspects.** An aspect's governance authorities must manage both the aspect's compliance with Self integration requirements — upward — and the aspect's enforcement of composition requirements for its cells — downward. These two governance activities involve different substrate content, different verification moments, and potentially different authority-holders within the aspect's governance structure. Both are required for the aspect to be compositionally valid at its scope.

**Cross-partner composition.** Cross-partner composition per A2.47 extends nested composition validity into multi-partner deployments. When cells from different partners compose within a shared aspect, cross-partner composition validity verification is required — the content-domain compatibility and Paper 1 compliance of cross-partner cells must be verified against the aspect's composition requirements, not merely against each partner's own internal standards. The same four cell-scope requirements apply; the governance coordination spans partner boundaries.

---

## 7. Limits

Recursive A1.13 does not prescribe specific composition requirements beyond those established in Paper 1 and formalized in Paper 2's treatment of birth specifications, content-domain compatibility, Paper 1 compliance, and type declarations. Deployments configure specific composition rules within those requirements. The architecture commits to the requirement structure — that entities must be compositionally valid at their level scope — not to specific rule content that varies across deployments.

Composition validity does not guarantee behavioral quality. A cell that is compositionally valid — complete birth specification, compatible content-domain, Paper 1 compliant, type-declared — may still produce poor behavioral outcomes. Composition validity verifies structural and governance compatibility; it does not verify that the cell performs well at its designated task. A5.14 is a compatibility and compliance test, not a performance test.

Recursive A1.13 does not create infinite regress. There are exactly three levels — cell, aspect, Self — and the recursion bottoms at cell scope (only composed, no lower composing environment to enforce requirements over) and tops at Self scope (only composing in single-Self deployments, no higher composing environment to satisfy requirements within). No fourth level requires composition requirements to be formalized.

Composition requirements at each level are independent but related. A cell that is compositionally valid within one aspect is not automatically compositionally valid within a different aspect. Content-domain compatibility is assessed relative to the specific aspect's content-domain, not in the abstract. A cell compatible with clinical-care-delivery content may not be compatible with regulatory-and-quality-reporting content, even within the same Self. This independence is architecturally important: it prevents a global composition-validity determination from substituting for the per-level, per-relationship verification that A5.14 requires.

---

## 8. Operational test

A deployment satisfies recursive composition requirements (A1.13) if and only if: every cell admitted to every aspect has a complete birth specification, a content-domain compatible with that aspect's content-domain, Paper 1 commitments satisfied at cell scope, and a type declaration present; every aspect enforces these four requirements for its cells and itself satisfies analogous requirements within its Selves; every Self enforces composition requirements for its aspects through its integration architecture; and A5.14 passes at each scope — cell, aspect, and Self — with aspect scope verified in both directions, upward within Selves and downward over cells.

---

## 9. Conclusion: naming nested composition validity as a standalone commitment

Formalizing recursive A1.13 as a standalone note serves the defensive publication purpose of the series because nested composition validity is not a self-evident consequence of Paper 2's three-level architecture. That cells, aspects, and Selves exist does not automatically establish which composition requirements apply at which level, what it means for an aspect to satisfy composition requirements in two directions simultaneously, how A5.14 applies at each scope, or how composition failures propagate across levels. These are independent architectural derivations that must be named explicitly to constitute prior art.

B2.106 is the ninth of thirteen notes decomposing B1.20. The next four notes address recursive authority architecture A2.01–A2.04 (B2.107), recursive conflict-as-first-class A1.03 (B2.108), recursive operational tests (B2.109), and recursive commitments verification closing Phase B2 (B2.110). Together, the thirteen notes establish that every major Paper 1 commitment, when extended to Paper 2's three-level architecture through B1.20, produces structurally distinct recursive variants that warrant independent formalization. Recursive A1.13 is the variant where the extension is most structurally complex — the dual role of aspects and the nested composition validity it creates are not present in any Paper 1 commitment or in Paper 2's other recursive applications — and its formalization as a standalone operational variant is therefore not redundant with adjacent notes in the series.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Recursive Composition Requirements (A1.13): Nested Validity at Cell, Aspect, and Self Scope.* May 12, 2026. ORCID: 0009-0004-8065-3235.
