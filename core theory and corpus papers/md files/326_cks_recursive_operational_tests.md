# Recursive Operational Tests — Decomposing B1.20 Recursive Paper 1 Commitments by Formalizing How Series A's Operational Test Suite (A5.01–A5.16) Applies Recursively at Cell Scope, Aspect Scope, and Self Scope, With Level-Appropriate Test Subjects and Enabling Entity-Level Paper 1 Compliance Verification

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The Coordination Knowledge Substrate (CKS) pattern's Series A established sixteen operational tests (A5.01–A5.16) to verify that a deployment satisfies Paper 1's architectural commitments. Paper 2's B1.20 commitment — that CKS architectures apply Paper 1 commitments recursively at cell, aspect, and Self scope — extends these tests beyond deployment-level application. This note formalizes recursive operational tests as the synthesis of how the complete A5.01–A5.16 test suite applies at each structural level with level-appropriate test subjects. The B2.14, B2.19, and B2.24 notes established level-specific inheritance verification frameworks; this note synthesizes the complete test suite picture across all three levels. Running the full test suite at any entity in the architecture — any cell, any aspect, the Self — produces entity-level Paper 1 compliance verification at that scope. The result is a governance architecture auditable at any granularity, with test failures precisely identifying the scope at which governance correction is needed rather than returning a single deployment-level verdict. This is the twelfth of thirteen notes decomposing B1.20, and the penultimate note of Phase B2.

## 1. Why recursive operational tests needs to be formalized as a standalone operational variant

Paper 2's B1.20 commitment establishes that CKS exceeds biology in part through recursive application of Paper 1's architectural commitments at every level of structural composition — cell, aspect, and Self. The B2.14, B2.19, and B2.24 notes each established inheritance verification frameworks at one of these three levels, confirming that the relevant Paper 1 commitments hold at that scope. What those notes do not synthesize individually is the complete picture of how the full Series A operational test suite applies across all three levels jointly. That synthesis is the contribution of this note.

The strategic prior-art motivation is distinct from the three inheritance verification notes. B2.14, B2.19, and B2.24 establish that commitments hold at each level. This note formalizes the test machinery that verifies they hold — and establishes that the machinery is applicable at any entity in the architecture, not only at deployment scope. The combination of recursive commitments and recursive test coverage is what makes entity-level Paper 1 compliance verification a publicly claimed architectural property.

Conventional AI governance architectures test at deployment scope: the deployment either passes or fails the operational test suite as a whole. A multi-entity architecture such as a CKS Self — composed of cells organized into aspects — that only tests at deployment scope cannot distinguish whether a failure originates in a particular cell, a particular aspect, or the Self's integration layer. The recursive test suite eliminates that ambiguity. Each entity can be tested independently; a failing entity is identified precisely; governance correction targets that entity's scope. This is the patentable territory B2.109 forecloses: the extension of an operational test suite from deployment scope to entity scope, with entity-level compliance verification as a claimed output.

As the twelfth of thirteen notes decomposing B1.20, this note occupies the synthesis position in the decomposition sequence. The prior eleven notes (B2.98–B2.108) each formalized one facet of B1.20's architectural advantage and the recursive application of individual Paper 1 commitments. The present note synthesizes how the test suite designed to verify those commitments applies at every scope, completing the verification architecture. The thirteenth and final note, B2.110, will close the B1.20 decomposition by formalizing recursive commitments verification as the architectural outcome the full decomposition sequence produces — and will thereby close Phase B2 entirely.

## 2. The recursive application of the operational test suite, precisely stated

Series A established sixteen operational tests to verify Paper 1's architectural commitments at deployment scope. The recursive application of Paper 1 commitments through B1.20 entails that these tests apply at each structural level, with the test subject at each level being the entity at that level rather than the deployment as a whole.

**Test suite at cell scope (B2.14 framework).** Nine tests apply at cell scope with cells as primary test subjects. The A5.01 INSPECT-RIGHT TEST verifies that the cell's DNA layer and action layer are inspectable by a human with appropriate access, without intermediation or scheduling. The A5.04 RULE-AUTHORING TEST verifies that the cell's DNA layer was authored under human authority per A2.04. The A5.05 MEDIATOR-ROLE TEST verifies that the cell's LLM instinct layer operates within Properties A through E of the AI-as-substrate-mediator commitment (A1.04): reading from substrate as primary source of state, writing only under orchestration rules, holding no substrate-relevant state outside the substrate, exercising no authority over substrate content, and recording all substrate-affecting operations with attribution. The A5.06 CELL-BEHAVIOR-DETERMINISM TEST verifies that cell behavior is deterministic given cell DNA and inputs, satisfying the five-guarantee determinism contract (A1.10). The A5.08 PROVENANCE-COMPLETENESS TEST verifies that action layer records carry the six-field provenance metadata the path-retraceability commitment (A1.07) requires. The A5.09 FOUR-ACCOUNTABILITY-QUESTIONS TEST verifies that who, what, when, and why can be answered for cell operations. The A5.10 SOURCE-OF-TRUTH-FIVE-CATEGORIES TEST verifies that cell DNA is correctly categorized as Category 4 content under A2.46, stored in the substrate rather than in agent memory or external caches. The A5.14 COMPOSITION-REQUIREMENTS-FIVE TEST verifies that the cell satisfies the five composition requirements (A1.13) within its aspect arrangements. The A5.16 REPRODUCIBILITY TEST verifies that cell operations replay deterministically given the same DNA and inputs.

**Test suite at aspect scope (B2.19 framework).** The same tests apply at aspect scope with aspects as primary test subjects. The A5.01, A5.04, A5.08, A5.09, A5.10, and A5.16 tests apply in direct analogy to their cell-scope forms, with the aspect's substrate — its coordination arrangement and governing orchestration content — as the test subject. The A5.14 test takes a distinctive form at aspect scope: an aspect must satisfy composition requirements both upward within its Self and downward over its constituent cells. This bidirectionality makes A5.14 at aspect scope the only level at which both directions are simultaneously operative. The A5.05 MEDIATOR-ROLE TEST at aspect scope applies to the coordination substrate role — the aspect's substrate mediates coordination among cells within it and must satisfy the mediator commitment in that capacity, though this application is less direct than at cell scope or Self scope.

**Test suite at Self scope (B2.24 framework).** The same tests apply at Self scope with the Self as primary test subject. The A5.01, A5.04, A5.08, A5.09, A5.10, A5.14, and A5.16 tests apply in direct analogy to their cell-scope forms, with the Self's integration substrate as the subject. The A5.05 MEDIATOR-ROLE TEST takes its most architecturally significant form at Self scope: the test subject is the instinct/reasoning configuration the B2.23 framework establishes — the committed allocation of decisions between the LLM instinct layer and the reasoning substrate. The test verifies that this configuration satisfies Properties A through E not only at individual cell scope but at the level of the Self's integrated instinct/reasoning architecture. A5.05 is therefore primarily applicable at cell scope and Self scope, with aspect scope as the intermediate application.

## 3. What makes recursive operational tests architecturally distinctive

In a deployment-level test suite, a single pass/fail verdict per test is produced for the deployment as a whole. A provenance failure tells a governance reviewer that the deployment does not meet provenance requirements — but not which of hundreds of cells or dozens of aspects is the source. Locating the failure requires additional investigation beyond what the test suite produces.

Recursive operational tests change this. A provenance failure at cell scope locates the failure at that cell. A failure at aspect scope that passes at all constituent cell scopes locates the failure at the aspect's coordination layer specifically. A Self-scope failure that passes at all aspect scopes locates it at Self-level integration. The test architecture is a precision governance instrument: it identifies not only that a commitment is violated but at what granularity correction is needed.

Entity-level compliance is also independently verifiable. An aspect under governance review can be tested in isolation; a newly born cell (per B2.44's birth verification framework) can be tested at cell scope before integration; the Self can be periodically tested without retesting all constituent cells and aspects. The test suite scales downward to the entity, not only upward to the deployment.

No standard AI governance framework formalizes entity-level compliance verification in this sense. Conventional AI architectures do not expose their internal structural composition as independently testable entities; tests apply to the system as a whole. CKS's three-level architecture, with entities that carry their own DNA layers and action layers under human-governed authority, is the architectural precondition for recursive test application. The test suite extension follows from the architectural commitment.

## 4. The biological analog as conceptual scaffold

Medicine applies diagnostic tests at multiple organizational levels: cellular assays (metabolic function, DNA integrity, membrane permeability), tissue tests (histological analysis, biopsy), organ tests (functional assessments of individual organs), and organism-level diagnostics. It does not confine itself to organism-level diagnosis when cellular-level pathology is the likely source. A liver function test isolates hepatic pathology from systemic signals; a biopsy isolates tissue pathology from organ-level function.

CKS recursive operational tests are the governed architectural analog. The three structural levels — cell, aspect, Self — parallel the nested levels of biological organization. Each level has an applicable test suite with level-appropriate subjects; entity-level failures are locatable at the appropriate level of organization.

The analog is pedagogical scaffold, not theoretical grounding. CKS recursive tests have one architectural advantage the biological analog lacks: they can be run on demand, at any time, on any entity, by any human with the inspect right. Biological diagnostics require specialist ordering and physical access. CKS tests are substrate operations — reads and provenance checks over content the substrate already carries — and impose no additional burden on the entities being tested. The governed architectural analog exceeds the biological one on testability as it exceeds it on reversibility, directed evolution, and modularity (B2.97, B2.95, B2.96).

## 5. Inherited Paper 1 commitments and the enabling B1.20 claim

The full A5.01–A5.16 test suite is the inherited set of commitments being made recursive by B1.20. Each test verifies one of Paper 1's six architectural commitments; recursive application extends each test's scope from deployment to entity.

B2.14 established the cell-level inheritance verification framework: Paper 1 commitments hold at cell scope, and the test suite therefore applies at cell scope with cells as test subjects. B2.19 established the parallel framework at aspect scope. B2.24 established it at Self scope. These three notes are directly load-bearing: without the inheritance verification frameworks they establish, the claim that tests apply at each scope would be ungrounded.

B1.20 is the enabling claim that licenses the synthesis. Its commitment that CKS architectures apply Paper 1 commitments recursively at every structural level is the architectural property from which recursive test applicability follows directly. A test suite verifies commitments; if commitments hold at every level, the test suite applies at every level. B2.109 formalizes that derivation. The recursive application is neither arbitrary extension nor scope inflation — it follows from what the tests are: verification instruments for architectural commitments that hold at entity scope.

## 6. Operational implications

**Birth verification runs tests at entity scope.** When a new cell is born, the B2.44 birth verification framework can run the relevant A5 tests at cell scope before integration. The cell enters the deployment with a compliance record, not merely an origination record.

**Governance reviews target the appropriate scope.** A reviewer concerned with an aspect's behavior can run the test suite at aspect scope without deployment-wide retesting. Governance effort is directed at the scope where governance concern exists.

**Entity-level results feed deployment-level compliance views.** The deployment-level compliance picture is an aggregation of entity-level test results. A deployment-level failure is traceable to the entity-level failure that produces it. Governance information flows upward from entity scope rather than being generated anew at deployment scope.

**Test failure is precisely located.** A cell failing A5.06 (cell-behavior-determinism) requires cell-scope correction; no aspect-level or Self-level intervention is required unless the failure has propagated. An aspect failing A5.14 while all constituent cells pass localizes the failure to the aspect's own coordination substrate. Selective testing is efficient: scope-appropriate tests run in response to scope-appropriate governance signals.

## 7. Limits

**Not all tests apply identically across levels.** A5.05 (MEDIATOR-ROLE) is primarily applicable at cell scope and Self scope; at aspect scope it applies to the coordination substrate role in a less direct form. A5.02 and A5.03 (tool-agnosticism) apply primarily at cell scope where LLM and tool infrastructure are directly relevant. Tests A5.07, A5.11, A5.12, A5.13, A5.15 apply in specific deployment contexts.

**The test suite verifies commitments; it does not constitute them.** Passing the test suite is evidence of commitment satisfaction, not its source. A deployment satisfies Paper 1 commitments because of its architectural properties; the tests confirm that those properties hold.

**Test coverage depends on configuration.** The recursive test suite is a framework. Whether tests are run at each entity scope, with what frequency, and by whom is a governance decision. The architecture makes entity-level compliance verification possible; deployment configures whether it occurs.

**Test failures require governance correction at the appropriate scope.** Precision in locating failures is only as useful as the governance response it enables. The test suite identifies failure location; it does not perform corrections.

## 8. One-sentence test

A CKS deployment instantiates recursive operational tests if and only if the complete A5.01–A5.16 test suite can be applied independently to any cell, any aspect, and the Self — with each application producing entity-level Paper 1 compliance verification at that scope, test failures identifying precisely the scope at which governance correction is needed, and entity-level results aggregable to deployment-level compliance views.

## 9. Why naming as standalone matters; penultimate Phase B2 note

Naming recursive operational tests as a standalone operational variant establishes publicly that entity-level Paper 1 compliance verification is a claimed architectural property of CKS deployments operating under B1.20. Without this formalization, the entity-level compliance capability exists as an implication of B1.20 and the B2.14/B2.19/B2.24 frameworks but is not directly citable as prior art. The naming eliminates the territory where a subsequent party could claim novelty in applying an operational test suite at entity scope within a multi-level governed AI architecture.

The prior-art posture is precisely targeted. The combination of recursive architectural commitments (B1.20), level-specific inheritance verification frameworks (B2.14, B2.19, B2.24), and entity-level test application (this note) is the patentable territory being foreclosed. Each element individually is established in the prior note series; the synthesis establishing their joint implication — recursive test applicability — is the novel contribution of B2.109.

The thirteenth and final note, B2.110 (recursive commitments verification), will close the B1.20 decomposition by formalizing how deployment-level Paper 1 compliance is assembled from entity-level test results — completing the governance accountability picture this note's entity-level test framework makes possible, and closing Phase B2 in its entirety.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Recursive Operational Tests — Decomposing B1.20 Recursive Paper 1 Commitments by Formalizing How Series A's Operational Test Suite (A5.01–A5.16) Applies Recursively at Cell Scope, Aspect Scope, and Self Scope, With Level-Appropriate Test Subjects and Enabling Entity-Level Paper 1 Compliance Verification.* May 12, 2026. ORCID: 0009-0004-8065-3235.
