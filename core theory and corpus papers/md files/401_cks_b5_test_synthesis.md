# Phase B5 Complete Operational Test Synthesis: How the Test Library (B5.02–B5.09) and Temporal Test Suites (B5.10–B5.13) Together Form the Complete Governance Test Architecture for Paper 2 Deployments, With Coverage Map and Prior Art Significance

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to synthesize the complete Phase B5 operational test architecture — the test library (B5.02–B5.09) and temporal test suites (B5.10–B5.13) — into a unified governance testing framework with a coverage map, and to name that synthesis as prior art.

---

## Abstract

Phase B5 of the CKS derivation note series formalizes operational tests for Paper 2 deployments. It consists of two distinct layers: a test library (notes B5.02–B5.09) containing approximately 41 individual tests organized by architectural commitment, and four temporal test suites (notes B5.10–B5.13) that draw from that library and organize tests by when governance runs them. This synthesis note — B5.14, the penultimate Phase B5 note — assembles the two layers into a single complete governance test architecture, presents a coverage map demonstrating that the architecture covers all twenty B1.01–B1.20 Paper 2 commitments, all Phase B3 cross-cutting anti-patterns, all composition pair integrity points, and all four governance lifecycle stages. It describes how the temporal suites connect to the test library, explains how the combined architecture enables governance diagnostics, workflow guidance, compliance demonstration, and governance maturity indication, and situates the architecture in relation to the inherited Series A tests (A5.01–A5.16). The complete test architecture — library, suites, and coverage map together — is itself named as prior art against future claims to novelty in governance testing for Paper 2-style deployments.

---

## 1. The Two-Layer Structure of the Test Architecture

Phase B5 is not a flat list of tests. It has a deliberate two-layer structure that separates what governance tests from when governance runs tests. The separation matters because it allows the test architecture to serve multiple governance purposes simultaneously without requiring governance to run all tests at all times.

**Layer 1 — The test library (B5.02–B5.09).** Eight notes define the test library. Each note in the library specifies a set of tests organized around a specific architectural commitment or cross-cutting concern. The tests in the library are the authoritative specification of what a Paper 2 deployment should be able to demonstrate. The library does not specify when tests run; it defines what passing looks like. A deployment that can pass all library tests on demand satisfies the complete evidentiary standard for Paper 2 governance.

**Layer 2 — The temporal test suites (B5.10–B5.13).** Four notes define temporal suites. Each suite draws a subset of library tests appropriate to a specific governance timing context — initialization, ongoing operation, evolution events, and external compliance demonstration. The suites do not define new tests; they organize library tests by when governance needs them. A deployment that runs each temporal suite at the appropriate frequency demonstrates not just that it can pass tests on demand, but that its governance operates as a living practice across the deployment lifecycle.

The two layers work in concert. The library provides completeness; the suites provide operational rhythm. Together they form an architecture in which governance knows both what to test and when.

---

## 2. The Test Library (B5.02–B5.09)

The test library contains eight notes totaling approximately 41 individual tests. The eight notes divide into two groups: six commitment-specific test notes and two cross-cutting test notes.

### 2.1 Commitment-specific test notes

**B5.02 — Instinct/reasoning separation (B1.01): 6 tests.** These tests verify that a deployment maintains the instinct/reasoning separation as independently-evolvable layers. Tests cover: structural separation of the LLM layer from the substrate-based reasoning layer; independent evolvability of each layer; the absence of reasoning functions inside the LLM layer; corrective signal paths that do not require weight modification; conflict preservation that catches what instinct would silently merge; and governance boundary placement at the instinct/reasoning divide rather than at a capability boundary.

**B5.03 — Three-level structure (B1.02): 5 tests.** These tests verify that the deployment maintains the cell, aspect, and Self levels with relational role membership semantics. Tests cover: cell-level scope and Paper 1 commitment preservation at that scope; aspect-level scope and purpose-defined structural arrangement; Self-level scope as architecturally coherent whole; relational role membership (cells appearing in multiple aspects without structural duplication); and non-strict hierarchy (Self accessing cells directly when purpose requires).

**B5.04 — Lifecycle commitments (B1.09–B1.11): 5 tests.** These tests verify that the three evolution mechanisms are present and in productive tension. Tests cover: instinct evolution as undirected mutation operating on the LLM and infrastructure layers; DNA evolution as directed selection operating on the orchestration substrate; action-feedback evolution as the closing-the-loop mechanism from action layer back to DNA layer; governance authority over each mechanism; and the absence of conflation between mechanism types.

**B5.05 — Evolution commitments (B1.12–B1.16): 5 tests.** These tests verify the multi-level and multi-shaped evolution architecture. Tests cover: multi-level simultaneous evolution across cell, aspect, and Self scopes; horizontal evolution (content-layer change within a scope); vertical evolution (structural reorganization across scopes); multi-shaped human governance across the three mechanisms; and the instinct/reasoning boundary maintained as governed substrate content through evolution events.

**B5.06 — Content-domain commitments (B1.18): 5 tests.** These tests verify distinct governance processes for distinct death types. Tests cover: functional obsolescence governance process; capability supersession governance process (two variants: instinct evolution absorbing a reasoning function; DNA evolution consolidating substrates); archival of dead cells as addressable operational retirement; and governance authority over reactivation.

**B5.07 — Cross-level access and recursive governance (B1.19 and B1.20): 5 tests.** These tests verify the enterprise-brain Self and the six points where CKS architecture exceeds biology's constraints. Tests cover: enterprise-brain Self as architecturally coherent design pattern; substrate-shared topology enabling cross-aspect coordination as a first-class concern; distributed failure risk localization (failures contained at appropriate scope rather than propagating across the Self); structural co-adaptation between organizational structure and Self architecture; and reactivation as an architectural property absent from biological systems.

### 2.2 Cross-cutting test notes

**B5.08 — Composition pair integrity: 5 tests.** These tests verify that adjacent commitment pairs, when composed in a deployment, preserve each commitment's properties through the composition. Tests draw from the Phase B4 composition pair formalizations and cover the integrity of the five most operationally consequential composition pairs: instinct/reasoning separation composed with the three-level structure; lifecycle composed with evolution mechanisms; DNA evolution composed with governance boundary placement; the enterprise-brain pattern composed with Paper 1 cell commitments; and verification substrates composed with instinct integration governance.

**B5.09 — Anti-pattern detection: 5 tests.** These tests directly probe for the cross-cutting anti-patterns formalized in Phase B3. Tests cover: instinct/reasoning conflation (the pattern where reasoning substrate content is allowed to migrate to or be governed by the LLM layer); governance erosion under evolution pressure (the pattern where evolution events weaken rather than preserve the governance boundary); scope collapse (the pattern where cell-level and Self-level commitments are treated as equivalent rather than recursive); lineage discontinuity (the pattern where evolution events break path retraceability); and single-mechanism evolution (the pattern where only one of the three evolution mechanisms is exercised, losing the productive tension that requires all three).

### 2.3 Library total

The eight notes contain approximately 41 individual tests: 6 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = 41. Each test produces a binary pass/fail result accompanied by the evidence basis for that result. The test library is complete in the sense that a deployment passing all 41 tests has demonstrated compliance with every Paper 2 architectural commitment.

---

## 3. The Temporal Test Suites (B5.10–B5.13)

The four temporal suites organize library tests by governance timing. Each suite specifies which library tests to run, when to run them, and what output form is appropriate for that timing context.

**B5.10 — Initialization suite (runs once at deployment creation).** The initialization suite draws from B5.04 (lifecycle configuration), B5.03 (three-level structure), B5.06 (content-domain governance processes), B5.02 (instinct/reasoning separation), B5.07 (cross-level access and recursive governance), B5.05 (evolution configuration), and B5.09 (anti-pattern scan). The suite runs once, at the moment a new deployment is created and before it enters operation. Its purpose is to verify that the deployment is correctly configured before any governance stakes accumulate. The initialization suite is the deployment's entry-conditions test; a deployment that fails initialization tests should not proceed to operation.

**B5.11 — Ongoing suite (runs periodically during operation).** The ongoing suite draws from B5.04, B5.06, B5.05, B5.02, and B5.09. It differs from the initialization suite not only in which tests it includes but in what passing means: the ongoing suite tests for *exercise* of governance mechanisms, not merely *configuration* of them. A deployment that has correctly configured its instinct/reasoning separation but has never actually exercised corrective signal paths has passed initialization but not ongoing. The ongoing suite accumulates evidence that governance is a living practice rather than a one-time setup.

**B5.12 — Evolution event suite (runs event-triggered on each significant evolution event).** The evolution event suite draws from B5.02 (to verify instinct/reasoning separation is preserved through the event), B5.05 (to verify the evolution event matches governed mechanism types), B5.06 (for content-domain composition re-verification when the event affects content scope), and B5.08 (composition pair integrity re-verification). The suite is focused and targeted: it runs only the tests relevant to verifying that a specific evolution event preserved governance commitments. Its result is a per-event evidence record that the evolution was governed.

**B5.13 — Compliance demonstration suite (runs externally-facing when compliance evidence is required).** The compliance demonstration suite draws from all library tests (B5.02–B5.09). It differs from the other suites in its output orientation: rather than producing internal governance signals, it produces external evidence artifacts in forms suitable for audit, regulatory demonstration, or contractual compliance purposes. The same underlying tests run; the evidence artifacts are formatted for external audiences rather than internal governance workflow.

---

## 4. Coverage Map

The coverage map is the centerpiece of this synthesis. It demonstrates that the Phase B5 test architecture provides complete coverage across four coverage dimensions.

### 4.1 Commitment coverage (B1.01–B1.20)

| Commitment | Primary test note | Cross-cutting coverage |
|---|---|---|
| B1.01 — Instinct/reasoning separation | B5.02 | B5.08, B5.09 |
| B1.02 — Three architectural levels | B5.03 | B5.08, B5.09 |
| B1.03 — DNA layer vs. action layer | B5.02, B5.04 | B5.09 |
| B1.04 — Expression as governed selection | B5.02, B5.04 | — |
| B1.05 — Lifecycle primitives at every level | B5.04 | B5.09 |
| B1.06 — Birth as governed origination | B5.04 | — |
| B1.07 — Mating as governable primitive | B5.04, B5.08 | — |
| B1.08 — Death with two distinct types | B5.06 | B5.09 |
| B1.09 — Three evolution mechanisms in productive tension | B5.04 | B5.09 |
| B1.10 — Instinct evolution as undirected mutation | B5.04, B5.05 | B5.09 |
| B1.11 — DNA evolution as directed selection | B5.04, B5.05 | B5.09 |
| B1.12 — Action-feedback evolution | B5.05 | B5.09 |
| B1.13 — Multi-level simultaneous evolution | B5.05 | — |
| B1.14 — Horizontal vs. vertical evolution | B5.05 | — |
| B1.15 — Multi-shaped human governance | B5.05, B5.07 | B5.09 |
| B1.16 — Instinct/reasoning boundary as governed substrate | B5.05, B5.02 | B5.09 |
| B1.17 — Verification substrates | B5.07, B5.08 | — |
| B1.18 — Distinct death-type governance processes | B5.06 | B5.09 |
| B1.19 — Enterprise-brain Self | B5.07 | B5.08 |
| B1.20 — Six points of architectural advantage over biology | B5.07 | — |

Every B1.01–B1.20 commitment is covered by at least one commitment-specific test note and by the cross-cutting anti-pattern detection in B5.09.

### 4.2 Anti-pattern coverage (Phase B3)

| Anti-pattern | Primary detection | Supporting detection |
|---|---|---|
| Instinct/reasoning conflation | B5.09 (direct) | B5.02 (indirect via separation verification) |
| Governance erosion under evolution pressure | B5.09 (direct) | B5.05, B5.12 (evolution event suite) |
| Scope collapse | B5.09 (direct) | B5.03 (indirect via level verification) |
| Lineage discontinuity | B5.09 (direct) | B5.04, B5.12 (evolution event suite) |
| Single-mechanism evolution | B5.09 (direct) | B5.04, B5.11 (ongoing suite exercise verification) |

All Phase B3 cross-cutting anti-patterns receive both direct detection (B5.09) and indirect detection through the commitment-specific tests that verify the positive commitments whose absence the anti-patterns represent.

### 4.3 Composition pair integrity coverage (Phase B4)

| Composition pair | Primary test note | Temporal suite re-verification |
|---|---|---|
| Instinct/reasoning separation × three-level structure | B5.08 | B5.10 (init), B5.12 (evolution events) |
| Lifecycle × evolution mechanisms | B5.08 | B5.10 (init), B5.11 (ongoing) |
| DNA evolution × governance boundary | B5.08 | B5.10 (init), B5.12 (evolution events) |
| Enterprise-brain × Paper 1 cell commitments | B5.08 | B5.10 (init) |
| Verification substrates × instinct integration governance | B5.08 | B5.10 (init), B5.12 (evolution events) |

All five operationally consequential composition pairs receive integrity verification in B5.08, with temporal re-verification at appropriate lifecycle stages.

### 4.4 Governance lifecycle stage coverage

| Lifecycle stage | Primary suite | Tests included |
|---|---|---|
| Initialization | B5.10 | B5.02, B5.03, B5.04, B5.05, B5.06, B5.07, B5.09 |
| Ongoing operation | B5.11 | B5.02, B5.04, B5.05, B5.06, B5.09 |
| Evolution events | B5.12 | B5.02, B5.05, B5.06 (re-verification), B5.08 |
| Compliance demonstration | B5.13 | B5.02–B5.09 (full library) |

All four governance lifecycle stages receive test coverage. No lifecycle stage is ungoverned; no test suite is ungoverned by a lifecycle stage.

---

## 5. Relationship to Series A Tests (A5.01–A5.16)

Phase B5 extends, not replaces, the Series A operational tests (A5.01–A5.16). The relationship has a specific structure.

Series A tests (A5.01–A5.16) verify the sixteen Paper 1 architectural commitments at cell scope. Because Paper 2 is a recursive extension of Paper 1 — Paper 1 commitments apply at every level of the Paper 2 architecture — Series A tests remain directly applicable to Paper 2 deployments. A Paper 2 deployment must pass Series A tests at cell scope before Phase B5 tests provide meaningful additional evidence.

Each Phase B5 commitment-specific test note (B5.02–B5.07) incorporates the relevant A5 tests for the Paper 1 commitments that the B1 commitments extend, plus Paper 2-specific test questions that cover the extended architectural content. This inheritance structure means each B5 note's tests are supersets of the A5 tests they extend: passing the B5 note's tests implies passing the relevant A5 tests, but not vice versa.

The complete test architecture for a Paper 2 deployment is therefore Series A tests plus Phase B5 tests together. Governance that runs only Phase B5 tests omits the cell-scope Paper 1 verification that underpins the entire architecture. Governance that runs only Series A tests omits the Paper 2-specific verification of the instinct/reasoning separation, multi-level structure, evolution mechanisms, and enterprise-brain coherence that Paper 2 adds.

---

## 6. How the Test Architecture Enables Governance

The Phase B5 test architecture enables governance in four distinct modes.

**Diagnostic framework.** When a governance review reveals a problem in a Paper 2 deployment, the test architecture provides the diagnostic question structure. Which library test fails identifies which governance area needs attention: a failure in B5.02 points to the instinct/reasoning separation; a failure in B5.05 points to the evolution mechanism architecture; a failure in B5.09 points to one of the named cross-cutting anti-patterns. The test architecture transforms a vague governance concern ("something seems wrong") into a specific architectural diagnosis.

**Governance workflow guide.** The temporal suites tell governance when to run which tests. A governance team that follows the temporal suite structure — running B5.10 at initialization, B5.11 periodically, B5.12 on each evolution event, and B5.13 when compliance evidence is needed — operates a complete governance workflow without needing to design that workflow from first principles. The architecture specifies the workflow; governance executes it.

**Compliance demonstration framework.** B5.13 produces external evidence artifacts from the same tests that drive internal governance. A deployment that runs B5.13 regularly has evidence on hand before a compliance request arrives, rather than needing to generate evidence reactively. The compliance demonstration suite is not a separate compliance process; it is the governance process made legible to external audiences.

**Governance maturity indicator.** The frequency and completeness with which a deployment runs the temporal suites is itself an indicator of governance culture maturity. A deployment that runs only the initialization suite and never re-runs subsequent suites has configured governance without sustaining it. A deployment that runs all four suites at appropriate frequencies, accumulates the exercise evidence the ongoing suite requires, and maintains per-event records from the evolution event suite demonstrates that governance is an organizational practice, not a one-time configuration act. The test architecture makes the difference between initial configuration and mature governance culture operationally measurable.

---

## 7. Prior Art Significance

The complete Phase B5 operational test architecture — the test library, the temporal suites, and the coverage map — is itself significant prior art against future claims to novelty in governance testing for Paper 2-style deployments.

**The 41-test library as prior art.** The test library formalizes the specific questions CKS governance should ask of a Paper 2 deployment. Any future proposal that defines a set of tests for instinct/reasoning separation, three-level structure, evolution mechanism governance, content-domain commitment, cross-level access, composition pair integrity, or anti-pattern detection is working within territory the B5 test library already occupies. The library establishes publicly, with attribution and date, what the governance testing questions are.

**The temporal suite organization as prior art.** The organization of governance tests into initialization, ongoing, evolution-event, and compliance-demonstration timing categories formalizes when governance should run tests in a Paper 2 deployment. Any future proposal that "discovers" governance should run certain tests at deployment creation, periodically during operation, on evolution events, or for compliance demonstration is working within a timing structure the Phase B5 suites already define. The four-category temporal organization is prior art against novelty claims at the level of governance workflow design.

**The coverage map as prior art.** The coverage map formalizes what "complete testing" means for a Paper 2 deployment: coverage of all B1.01–B1.20 commitments, all Phase B3 anti-patterns, all Phase B4 composition pair integrity points, and all four governance lifecycle stages. Any future standard, framework, or certification scheme for Paper 2-style deployment governance that defines completeness criteria is working within a completeness definition the Phase B5 coverage map already establishes.

Together, the test library, the temporal suite organization, and the coverage map define the complete prior art for Paper 2 deployment governance testing. Phase B5 as a whole — with this synthesis as its organizing capstone — is the published record that that prior art exists under Wenxin Li's authorship as of its Zenodo deposit date.

---

## 8. Sources

**Primary source:**
Li, Wenxin. "The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance." April 2026.

**Foundational source:**
Li, Wenxin. "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems." April 2026.

**Series context — preceding Phase B5 notes:**
Li, Wenxin. CKS Derivation Note B5.02: Operational Test — Instinct/Reasoning Separation. 2026.
Li, Wenxin. CKS Derivation Note B5.03: Operational Test — Three-Level Structure. 2026.
Li, Wenxin. CKS Derivation Note B5.04: Operational Test — Lifecycle Commitments. 2026.
Li, Wenxin. CKS Derivation Note B5.05: Operational Test — Evolution Commitments. 2026.
Li, Wenxin. CKS Derivation Note B5.06: Operational Test — Content-Domain Commitments. 2026.
Li, Wenxin. CKS Derivation Note B5.07: Operational Test — Cross-Level Access and Recursive Governance. 2026.
Li, Wenxin. CKS Derivation Note B5.08: Operational Test — Composition Pair Integrity. 2026.
Li, Wenxin. CKS Derivation Note B5.09: Operational Test — Anti-Pattern Detection. 2026.
Li, Wenxin. CKS Derivation Note B5.10: Initialization Test Suite. 2026.
Li, Wenxin. CKS Derivation Note B5.11: Ongoing Operation Test Suite. 2026.
Li, Wenxin. CKS Derivation Note B5.12: Evolution Event Test Suite. 2026.
Li, Wenxin. CKS Derivation Note B5.13: Compliance Demonstration Test Suite. 2026.

**Stylistic template:**
Li, Wenxin. CKS Derivation Note A1.01: "Authority, Not Labor: A Precise Definition of 'Human-Governed' in the Coordination Knowledge Substrate Pattern." April 2026.
