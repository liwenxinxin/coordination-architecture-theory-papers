# Modularity Verification: Formalizing How Modularity Properties Are Operationally Verified Through the A5.14 Composition-Requirements-Five Test and A5.15 Pattern-Mapping Test as Primary Mechanisms at Every Structural Level

**Note ID:** B2.39
**Series:** B — Paper 2 Derivation
**Phase:** B2 — Operational Variants and Decompositions
**Parent note:** B1.08 (Modularity from Architectural Commitment)
**Position in decomposition:** Fifth and closing note of the B1.08 decomposition
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

B1.08 establishes modularity as an architectural commitment in CKS deployments — modular by design from the start, at every level of composition, rather than modular by evolution or by measurement after the fact. Four notes preceding this one decomposed the B1.08 commitment from four angles: B2.35 as architectural consequence of four inherited Paper 1 properties, B2.36 as source of composition configurability, B2.37 as enabler of vertical evolution, and B2.38 as the foundation for cross-partner compositions. This note closes the B1.08 decomposition by formalizing the fifth and operationally essential angle: modularity verification — how the modularity commitment is tested rather than merely asserted. The primary verification mechanisms are two Series A composition-focused tests. The A5.14 composition-requirements-five test verifies that all five A1.13 composition requirements are satisfied for every composition in the deployment — at cell-to-aspect scope, aspect-to-Self scope, and cross-partner scope. The A5.15 pattern-mapping test verifies that each composition in the deployment maps to Pattern A, B, or C per A2.92–A2.94 with the applicable sharpening properties per A4.27–A4.29. Both tests operate within the broader level-specific inheritance verification suites per B2.14 (cell level), B2.19 (aspect level), and B2.24 (Self level), serving as the modularity-specific component of those suites. The architectural significance of naming these tests explicitly is that they convert modularity from a claimed property into a demonstrable one: A5.14 and A5.15 failures reveal non-modular coupling and implicit composition that would otherwise remain hidden. This note formalizes the verification mechanism, its failure modes, its temporal triggers, its limits, and its relationship to the broader inheritance verification framework, completing the B1.08 decomposition.

---

## 1. Why modularity verification needs to be formalized as a standalone operational variant

B1.08 states a strong architectural commitment: modularity in CKS deployments is required at instantiation time, not hoped for or measured after the fact. B2.35 through B2.38 developed four consequences of that commitment — modularity as architectural consequence of four Paper 1 properties, as source of composition configurability, as enabler of vertical evolution, and as the structural basis for cross-partner compositions. Each of those notes describes what modularity makes possible. None of them addresses a question that any serious deployment must answer: how does a deployment operator confirm that the modularity commitment is actually holding?

This question is not answered by the architectural commitment itself. Commitment establishes what must be true; verification establishes whether it is true and reveals when it has been violated. In conventional AI architectures, modularity is most commonly asserted at design time — components are declared modular because they were designed to be modular. That declaration is not testable without explicit architectural tests. Design-time intent and runtime state can diverge silently, and without tests that detect divergence, the modularity claim remains credible only for as long as the deployment's history is short and its structure is simple.

CKS deployments do not rely on asserted modularity. Series A Phase A5 provides explicit operational tests that apply to composition-level properties; two of those tests — A5.14 and A5.15 — are the primary mechanisms for verifying that modularity holds at every composition in the deployment. Naming these tests explicitly as the modularity verification mechanism is the defensive-publication contribution of B2.39: formalizing, in derivation form, the prior-art position that modularity in a CKS deployment is testable through specific composition-focused tests, not merely asserted through design intent.

B2.39 occupies the closing position of the B1.08 decomposition because verification is architecturally downstream of commitment. B2.35 establishes what modularity is built from; B2.36 through B2.38 establish what it enables; B2.39 establishes how it is confirmed. Without the verification mechanism, the B1.08 commitment is incomplete as an operational architectural specification.

---

## 2. The verification mechanism precisely stated

**Primary verification mechanisms.** Two Series A composition-focused tests are the primary mechanisms for modularity verification in CKS deployments.

**A5.14 — Composition-requirements-five test at modularity scope.** The A5.14 test verifies that all five composition requirements per A1.13 are satisfied for every composition in the deployment. The five requirements are: Requirement 1, substrate-authoritative content — each composition operates over substrate content that carries the substrate-as-source-of-truth commitment per A1.08; Requirement 2, conflict as first-class per A1.03 — conflict states are preserved across the composition boundary, not resolved or discarded at the junction; Requirement 3, governance affordances per A2.01–A2.04 — the composition supports human inspection, modification, and override rights at the composed scope; Requirement 4, determinism per A1.10 — the composition satisfies the determinism contract, with same substrate state producing equivalent behavior; Requirement 5, retraceability per A1.07 — the path through the composition is traceable with the required provenance metadata. The A5.14 test runs at cell-to-aspect composition, at aspect-to-Self composition, and at cross-partner compositions. All five requirements must be satisfied for each composition; partial satisfaction is not conformant. A5.14 failure at any composition indicates that composition requirements have been violated at that junction — which means the composition is not architecturally modular in the CKS sense, regardless of what design intent specified.

**A5.15 — Pattern-mapping test at modularity scope.** The A5.15 test verifies that each composition in the deployment maps to one of Pattern A, B, or C per A2.92–A2.94. Pattern A, B, and C are the three recognized composition patterns in CKS architecture; every compliant composition instantiates one of them. The test applies the sharpening properties per A4.27, A4.28, A4.29 for the applicable pattern, confirming that the composition is a legitimate instance of its claimed pattern. Pattern mapping must be established and documented for every composition in the deployment; an undocumented or pattern-unassigned composition is not conformant. A5.15 failure indicates that the composition pattern has not been established — which means the composition is implicit, outside the governed architecture, and therefore not modular in the CKS sense.

**Supplementary tests contributing to modularity verification.** Three additional Series A tests contribute to modularity verification without serving as primary mechanisms. A5.01 (inspect right) verifies that A1.02 modular boundaries are inspectable — that the boundary between substrate and cell is operationally accessible to human inspection at every level where it holds. A5.11 (tool-agnosticism-migration) verifies that modular units maintain their interfaces through technology migration — that the tool-agnosticism commitment per A1.05 holds across the composition boundary when the deployment's tools change. A5.16 (reproducibility) verifies that compositions replay deterministically — that the determinism contract per A1.10 holds for composed execution, not only for individual cell execution.

**Cross-partner modularity verification.** For cross-partner compositions per B2.38, the A5.14 and A5.15 tests run across partner boundaries. A5.14 must confirm that all five composition requirements hold for the cross-partner junction specifically — with particular attention to Requirement 1 (substrate-authoritative content), since cross-partner compositions involve distinct substrates each carrying their own source-of-truth commitments, and to Requirement 3 (governance affordances), since cross-partner governance authority must be established before cross-partner operations can be governed. A2.47 authority distribution must be established for cross-partner tests to proceed: without cross-partner authority distribution, the governance affordance requirement of A5.14 cannot be evaluated, and A5.14 cannot be run in a governed way. This makes A2.47 establishment a prerequisite for cross-partner A5.14 and A5.15 tests, not an optional precondition.

**Temporal triggers.** Modularity verification is not a one-time event at deployment initialization. Three temporal triggers ensure verification is maintained across the deployment lifecycle. At composition creation per B1.09 birth, A5.14 and A5.15 run to confirm the new composition is modular from its first operational moment. At composition modification per B1.16 vertical evolution, A5.14 and A5.15 run to confirm that structural reorganization preserves modularity — vertical evolution changes composition relationships, and each change requires fresh verification that the post-evolution composition still satisfies requirements and maps to a pattern. At cross-partner composition establishment per A2.47, A5.14 and A5.15 run after authority distribution is confirmed and before cross-partner operations proceed. Together, these three triggers maintain modularity assurance as the deployment evolves rather than only at a single baseline point.

---

## 3. What makes modularity verification architecturally distinctive

The conventional AI architecture posture for modularity is design-time declaration. Components are designed modularly and declared to be modular; the modularity claim is part of the architecture documentation. This posture is not wrong — modular design is better than non-modular design — but it is incomplete as an operational commitment because it provides no mechanism for detecting when the modularity claim has been violated. Non-modular coupling introduced by operational evolution, by emergent composition behavior, or by cross-component side effects remains invisible under design-time declaration until a failure event reveals it.

The CKS posture is categorically different. A5.14 and A5.15 are explicit architectural tests. They do not ask whether the components were designed modularly; they test whether the composition requirements and composition patterns that constitute modularity in the CKS sense are currently satisfied. A5.14 failure is an operational finding — composition requirements violated — not a retroactive design critique. A5.15 failure is an operational finding — composition pattern not established — not a design documentation gap. Both failures are detectable before they produce downstream coordination failures, which is the operational value of explicit testing over design-time assertion.

The architectural distinctiveness is not that CKS has tests while other architectures do not. Software testing is universal. The distinctiveness is that A5.14 and A5.15 are tests for specific architectural properties — composition requirements and composition patterns — that are precisely defined in the CKS framework and that jointly constitute the modularity commitment under B1.08. Without precise composition requirements (A1.13) and precise composition patterns (A2.92–A2.94), there is nothing for A5.14 and A5.15 to test against. The testability of modularity in CKS deployments is downstream of the precision of the compositional specification, which is what makes it genuinely architectural rather than merely procedural.

---

## 4. Inherited Paper 1 commitments

A5.14 and A5.15 inherit directly from Series A Phase A5. A1.13 composition requirements are the foundational specification that A5.14 tests against; without A1.13's five-requirement structure, A5.14 has no content. A1.16 hybrid systems composition is the foundational specification that A5.15 tests against at the pattern level; the three composition patterns per A2.92–A2.94 are downstream of A1.16's compositional commitments.

B1.20 recursive Paper 1 commitments establishes that all six Paper 1 architectural commitments apply at every level of the three-level CKS structure — cell, aspect, Self. This recursive application is what makes A5.14 and A5.15 run at every composition scope rather than only at the scope Paper 1 addresses directly. Without B1.20's recursion, modularity verification would apply at cell scope but not at aspect-to-Self or cross-partner scope. B1.20 is the load-bearing inheritance that gives the temporal triggers their full scope.

A2.47 authority distribution is the prerequisite for cross-partner A5.14 and A5.15 tests, as noted above. A2.47 is inherited from Series A and carried forward through B2.38 cross-partner compositions; B2.39 inherits A2.47's role as cross-partner authority prerequisite directly.

A1.01 human-governed governance applies throughout the verification process. Verification runs, failure findings, and governance review actions are all substrate content under A1.01. Human authority to inspect, modify, and override applies to verification results as well as to the compositions being verified. Test failures trigger governance review because governance authority — per A1.01 — covers the architectural state the tests report on.

---

## 5. Modularity failure modes

Two primary failure modes correspond directly to the two primary tests.

**A5.14 failure: composition requirements violated.** When A5.14 fails for a given composition, one or more of the five A1.13 requirements is not satisfied at that junction. The architectural significance is that non-modular coupling has crept into the composition. Non-modular coupling in the CKS sense is not merely tight coupling in the software-engineering sense; it is the violation of a specific structural property — the substrate-authoritative, conflict-preserving, governance-affordant, deterministic, retraced composition that A1.13 specifies. A5.14 failure localizes the violation: the failure finding identifies which requirement is unsatisfied at which composition scope, providing the governance review with a specific remediation target. Without A5.14, non-modular coupling of this kind is invisible until it produces a coordination failure — a governance affordance that cannot be exercised, a conflict that was discarded at a composition boundary, a determinism guarantee that fails at composed scope.

**A5.15 failure: composition pattern not established.** When A5.15 fails for a given composition, the composition does not map to Pattern A, B, or C per A2.92–A2.94. The architectural significance is that an implicit composition exists outside the governed architecture. Implicit compositions are not merely undocumented compositions; they are compositions whose behavior is not governed by the pattern-specific constraints that A2.92–A2.94 establish, including the sharpening properties per A4.27–A4.29. An A5.15 failure does not mean the composition is non-functional; it means the composition operates outside the architectural framework that the B1.08 commitment requires. Without A5.15, implicit compositions can accumulate silently, gradually replacing the governed architecture with an ungoverned one.

Both failure modes have architectural significance in the B1.08 context because both represent violations of the modularity commitment specifically — not performance failures, not behavioral failures, but structural failures that undermine the architecture's ability to support composition configurability per B2.36, vertical evolution per B2.37, and cross-partner compositions per B2.38.

---

## 6. Operational implications

CKS deployments run A5.14 and A5.15 at the three temporal triggers established in §2: composition creation, composition modification, and cross-partner establishment. These runs are governed operations — their results are substrate content under A1.01, subject to human inspection, modification, and override.

Test failures trigger governance review. The governance review addresses the architectural question the failure identifies: which composition requirement is violated (A5.14 failure), or which composition pattern needs to be established (A5.15 failure). Governance review may result in composition remediation, in modification of the affected orchestration rules, or in a recorded governance decision that the deployment accepts a specific deviation from the A5.14 or A5.15 standard with documented rationale. All of these outcomes are substrate content under A1.01.

Modularity verification results inform deployment confidence in structural stability. A deployment in which all compositions have passed A5.14 and A5.15 at their most recent trigger points has demonstrable modularity assurance — not a claim, but a verifiable record. This is what makes B1.08's commitment to modularity-from-the-start operationally meaningful rather than architecturally aspirational: the record exists and is substrate content.

Cross-partner verification is required before cross-partner operations proceed. This sequencing is not optional; A2.47 authority distribution precedes the tests, and the tests precede cross-partner operations. The sequencing is the governance-first posture of B2.38 expressed at the verification layer: cross-partner operations under CKS governance are governed operations, and governance over them requires the verification that A5.14 and A5.15 provide.

The modularity-specific A5.14 and A5.15 tests integrate with the broader inheritance verification suites. B2.14 cell-level inheritance verification, B2.19 aspect-level inheritance verification, and B2.24 Self-level inheritance verification each verify that the full set of inherited Paper 1 commitments holds at their respective scopes. A5.14 and A5.15 are the modularity-specific components of those suites — the tests that verify the composition-level properties specifically. Running A5.14 and A5.15 does not replace the broader verification suites; it contributes the modularity-focused component to them.

---

## 7. Limits

**Modularity verification does not guarantee behavioral correctness.** A5.14 and A5.15 verify architectural properties of compositions — that composition requirements are satisfied and that compositions map to governed patterns. They do not verify that the substrate content within the compositions is correct, that the orchestration rules produce intended behaviors, or that the deployment achieves its organizational objectives. A deployment can pass both tests and still have incorrect content, misconfigured rules, or ineffective coordination.

**A5.14 and A5.15 are not the only modularity-relevant tests.** Supplementary tests A5.01 (inspect right), A5.11 (tool-agnosticism-migration), and A5.16 (reproducibility) each contribute to the modularity assurance picture. A full modularity verification suite runs all five tests, not only the two primary ones.

**Modularity verification does not prescribe specific test parameters.** The A5.14 and A5.15 tests are architectural specifications for what to test; they do not specify tooling, testing frequency beyond the three temporal triggers, or the format of test records. These are deployment design choices within the constraints the tests establish.

**Modularity verification does not replace cross-partner governance agreements.** A5.14 and A5.15 verify architectural properties of cross-partner compositions; they verify that composition requirements hold across the partner boundary and that the composition maps to a governed pattern. They do not verify that partner governance agreements are appropriately scoped, that partner authority assignments are substantively correct, or that cross-partner coordination arrangements serve the intended organizational purposes. Governance agreements are the human-governed substrate content that frames cross-partner compositions; the tests verify the architectural properties of the compositions, not the correctness of the agreements themselves.

**Modularity verification does not eliminate the need for level-specific inheritance verification.** B2.14, B2.19, and B2.24 verify the full suite of inherited Paper 1 commitments at their respective structural levels. A5.14 and A5.15 are components of those suites, not replacements for them. A deployment that runs A5.14 and A5.15 without running the broader level-specific inheritance verification suites has verified modularity-specific properties without verifying the other inherited commitments those suites cover.

---

## 8. Operational test

A CKS deployment instantiates the B1.08 modularity commitment with full operational verification — rather than merely asserting it architecturally — if and only if all of the following are true:

For every composition in the deployment (cell-to-aspect, aspect-to-Self, and cross-partner): (1) the A5.14 composition-requirements-five test has been run at the most recent applicable temporal trigger and all five A1.13 requirements were satisfied; (2) the A5.15 pattern-mapping test has been run at the most recent applicable temporal trigger and the composition maps to Pattern A, B, or C per A2.92–A2.94 with the applicable sharpening properties per A4.27–A4.29; (3) for cross-partner compositions, A2.47 authority distribution was confirmed before the A5.14 and A5.15 tests were run; (4) test results are substrate content under A1.01, subject to human inspection; and (5) A5.14 or A5.15 failures have either been remediated or have been addressed by a recorded governance decision.

A deployment that satisfies these five conditions has demonstrable modularity assurance. A deployment that satisfies only the design-time architectural commitment of B1.08 without the operational verification this test specifies has asserted modularity, not demonstrated it.

---

## 9. Conclusion: closing the B1.08 decomposition

B2.35 through B2.39 constitute the complete decomposition of B1.08's modularity-from-architectural-commitment claim across five operational angles. B2.35 established that modularity in CKS deployments is the architectural consequence of four inherited Paper 1 properties — it does not need to be separately engineered because it follows from commitments already required. B2.36 established that composition configurability — the ability to vary composition configurations within governed constraints — is made possible by the modularity B1.08 requires. B2.37 established that vertical evolution — structural reorganization of the deployment — is safe under B1.08 because modularity guarantees that composition reorganization does not violate inherited commitments at newly formed boundaries. B2.38 established that cross-partner compositions extend B1.08's modularity commitment across organizational boundaries rather than treating partner-boundary compositions as outside the governed architecture.

B2.39 closes the decomposition by formalizing what is operationally necessary to hold all four prior notes together: the verification mechanism. Without A5.14 and A5.15, the configurability of B2.36 is not testably maintained, the safety of B2.37's vertical evolution is not verifiable, and the boundary integrity of B2.38's cross-partner compositions is not confirmed. With A5.14 and A5.15 running at the three temporal triggers, across all composition scopes, with results as substrate content under A1.01 governance, the B1.08 commitment becomes operationally complete — not an architectural aspiration but a verifiable, governable, deployment-lifecycle property.

The naming of A5.14 and A5.15 as the primary modularity verification mechanisms is the prior-art contribution this note formalizes. Any subsequent claim to a novel mechanism for verifying modularity in multi-level AI substrate architectures through composition-requirement-five tests and pattern-mapping tests applied at composition creation, modification, and cross-partner establishment, within a broader inheritance verification framework, must contend with this derivation and its position in the B1.08 decomposition chain.

Phase B2 continues with B2.40 beginning the B1.09 birth decomposition, applying the five-note decomposition methodology to the governed origination of cells, aspects, and Selves as the next structural lifecycle commitment Paper 2 specifies.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Modularity Verification: Formalizing How Modularity Properties Are Operationally Verified Through the A5.14 Composition-Requirements-Five Test and A5.15 Pattern-Mapping Test as Primary Mechanisms at Every Structural Level.* Note B2.39 in the CKS Derivation Note Series. May 12, 2026. ORCID: 0009-0004-8065-3235.
