# Operational Tests for Cross-Level Access and Recursive Governance (B1.19/B1.20): Five Deployment-Facing Tests Including Access Rules Completeness, Authority Distribution Correctness, Unauthorized Access Detection, Recursive Commitments Verification, and Entity-Level Compliance, Each With Question, Mechanism, Pass, Fail, and Remediation Signal

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

The Coordination Knowledge Substrate (CKS) architecture for AI Selves under human governance commits to two structural properties that span its three architectural levels — cell, aspect, and Self — and that together determine whether governance is genuinely recursive or only nominally so. The first, formalized as B1.19, is that cross-level access — any interaction in which one structural level reads from or writes to another — is governed by explicitly authored rules resident in the DNA layer, not by implementation convention or implicit permission. The second, formalized as B1.20, is that every entity at every structural level satisfies the Paper 1 commitments at its level-appropriate scope, so that governance does not collapse into deployment-level-only oversight as the architecture scales. This note formalizes five operational tests for verifying these two commitments in a deployed system: the Access Rules Completeness Test (derived from B2.95), the Authority Distribution Test (derived from A2.47 and B2.107), the Unauthorized Access Detection Test (derived from B2.97), the Recursive Commitments Verification Test (derived from B2.110), and the Entity-Level Compliance Test (derived from B2.109). Each test is stated with a test question, test mechanism, pass condition, fail condition, and remediation signal. The composite B1.19/B1.20 result requires all five tests to pass. The primary anti-patterns this battery detects are B3.20 Ungoverned Cross-Level Access, B3.21 Deployment-Level-Only Governance, and B3.26 Authority Ambiguity.

---

## 1. Why Cross-Level Access and Recursive Governance Require Dedicated Operational Tests

A CKS architecture for AI Selves under human governance distributes coordination work across three structural levels — cell, aspect, and Self — and organizes each level's content and governance in the DNA layer and action layer introduced in Paper 2. The levels do not operate in isolation. Cells interact with the aspects they belong to; aspects interact with the Selves they constitute; Selves govern both. These interactions are cross-level access events: a Self reading cell-level action records to inform DNA evolution, an aspect writing coordination directives to cells, a cell reporting upward to its aspect. Cross-level access is architecturally necessary; what B1.19 requires is that it be governed.

Governed cross-level access means that access rules exist as substrate content in the DNA layer, authored per A2.04 authority, covering all required access directions, and carried in provenance records per A2.40. Without authored rules, cross-level access defaults to implementation-layer convention — whatever the runtime happens to permit — which is ungoverned in the CKS sense even if it produces correct behavior under normal conditions.

Recursive governance, formalized as B1.20, is the complementary commitment. A system can have complete cross-level access rules and still fail B1.20 if those rules govern only the deployment level while cells and aspects operate without level-appropriate Paper 1 commitments. The recursive structure requires that the same governance properties — inspect, modify, override; authored orchestration rules; conflict preservation; path retraceability — hold at cell scope, at aspect scope, and at Self scope, not only at the top-level deployment scope. B3.21 Deployment-Level-Only Governance is the anti-pattern that results when the recursion is not maintained.

Testing for B1.19 and B1.20 compliance cannot be accomplished by inspecting any single artifact or layer. The five tests below partition the verification work: Tests 1 through 3 address the access-governance side of B1.19; Tests 4 and 5 address the recursive-compliance side of B1.20. All five must pass for the composite result to hold.

---

## 2. Architectural Position of B1.19 and B1.20

B1.19 and B1.20 are Phase B1 foundational commitments — they are architectural properties of the multi-level CKS structure that every deployment must satisfy, not operational choices that can be deferred. Their decompositions into testable sub-claims occupy B2.94–B2.110 of the Paper 2 derivation record.

B1.19 decomposes via B2.94–B2.97. B2.94 establishes that cross-level access is an architectural necessity arising from the three-level structure. B2.95 specifies that access rules for all required access directions — Self-to-aspect, aspect-to-cell, Self-to-cell through expression, cell-to-aspect reporting, and aspect-to-Self reporting — must be authored and substrate-resident. B2.96 connects access-rule authoring to the A2.04 authority framework. B2.97 formalizes the unauthorized-access detection requirement: any access event outside the A2.47 authority distribution is a compliance failure, not merely an anomaly.

B1.20 decomposes via B2.98–B2.110. B2.98–B2.106 establish the three-level recursive commitment structure, specifying what Paper 1 compliance looks like at cell scope (B2.14 frameworks), aspect scope (B2.19 frameworks), and Self scope (B2.24 frameworks). B2.107 formalizes the recursive authority architecture, establishing that authority distribution is level-differentiated — not all actors have all authority at all levels — and that cross-level access authority is a distinct configuration within A2.47. B2.108 specifies the conflict registry requirement at each level. B2.109 introduces recursive operational tests: the Paper 1 test suites (A5.01–A5.16) apply at each structural scope. B2.110 provides the comprehensive eight-step recursive commitments verification sequence.

---

## 3. Test 1 — Access Rules Completeness Test

**Derived from:** B2.95

**TEST QUESTION:** Are cross-level access rules per B2.95 authored, complete, and substrate-resident for all required access directions?

**TEST MECHANISM:** Inspect the Self integration architecture per B2.21 for cross-level access configuration. Verify that downward access rules are present covering: Self-to-aspect governance interactions, aspect-to-cell coordination interactions, and Self-to-cell interactions through expression per B2.30. Verify that upward access rules are present covering: cell-to-aspect reporting and aspect-to-Self reporting. For each access direction, verify that the governing rule is authored per A2.04 authority and resident in the DNA layer per B1.06. Apply the A5.04 rule authoring test to access rules as a rule category.

**PASS CONDITION:** A complete set of access rules covering all required access directions is present in the DNA layer. Every access rule carries A2.40 provenance including writer, timestamp, rationale, and authority reference. The A5.04 rule authoring test passes for all access rules.

**FAIL CONDITION:** Access rules are absent for one or more required access directions. Cross-level interactions are occurring through implementation channels or runtime conventions without corresponding governance rules in the DNA layer. The A5.04 rule authoring test fails when applied to access rules.

**REMEDIATION SIGNAL:** B3.20 Ungoverned Cross-Level Access, Form 3 (access-rule-absent design). The remediation is not to document existing runtime conventions but to author access rules per B2.95 through directed selection per B1.14, placing them in the DNA layer with proper A2.40 provenance. Each required access direction requires its own authored rule; omnibus permissions that cover all access implicitly do not satisfy B2.95.

---

## 4. Test 2 — Authority Distribution Test

**Derived from:** A2.47 and B2.107

**TEST QUESTION:** Is cross-level access authority per A2.47 correctly distributed at each level scope, and does it derive from B1.20's recursive authority architecture per B2.107?

**TEST MECHANISM:** Inspect the A2.47 authority distribution specification for level-differentiated content. Verify that the specification names: who holds cell-level A2.01–A2.04 authority for each cell; who holds aspect-level authority for each aspect; who holds Self-level authority; and who holds cross-level access authority per B2.95 at each access direction. Verify that level-specific authority is distinct — actors appropriate to cell-scope governance are not automatically granted Self-scope authority, and the reverse. If authority has changed since initial deployment, verify A6.06 compliance for the transition.

**PASS CONDITION:** A2.47 specifies level-differentiated authority covering all three structural scopes. Cross-level access authority is configured per B2.95 for each access direction. No actor holds blanket authority across all levels without explicit scope specification. Authority differentiations are consistent with B2.107's recursive authority architecture.

**FAIL CONDITION:** A2.47 is absent or specifies uniform authority — all actors effectively hold all authority at all levels, or cross-level access authority is unspecified. No level-appropriate authority differentiation can be identified. Anyone can access any level without a governing authority basis.

**REMEDIATION SIGNAL:** B3.26 Authority Ambiguity. The remediation is to configure A2.47 with level-differentiated authority per the B1.20 recursive authority structure, specifying authority at cell, aspect, and Self scope separately, and designating cross-level access authority as a distinct configuration category within A2.47.

---

## 5. Test 3 — Unauthorized Access Detection Test

**Derived from:** B2.97

**TEST QUESTION:** Are there any cross-level access events outside the A2.47 authority distribution?

**TEST MECHANISM:** Examine all cross-level access event records per A2.40 for the deployment period under review. For each access event: verify the accessing entity holds A2.47 authority for that access direction and structural scope; flag any event where authority basis cannot be established. Apply the A5.09 four accountability questions to each flagged event: Who accessed (is this entity authorized for this access direction)? What was accessed (is the target within the entity's authority scope)? When did the access occur (is this within an authority period)? Why was the access made (does a governing rule per B2.95 cover this event)?

**PASS CONDITION:** All cross-level access events in the review period are within the A2.47 authority distribution. No events are found where the accessing entity lacks authority for the direction and scope of access. The A5.09 four accountability questions can be answered for every access event — the "under what authority?" question produces a specific A2.47 reference and B2.95 rule reference for each event.

**FAIL CONDITION:** Access events are found where the accessing entity's authority for that direction and scope cannot be established. The A5.09 "under what authority?" question cannot be answered for one or more events — the event is traceable to a writer and timestamp but not to a governing rule or authority basis.

**REMEDIATION SIGNAL:** B3.20 Ungoverned Cross-Level Access, Form 1 (access without authorization). For identified unauthorized events: retroactively authorize through A2.47 if the access was substantively appropriate and the omission was an oversight; revoke if the access was not appropriate. Going forward: strengthen access governance by auditing authority distribution against access records at regular intervals; treat the gap between A2.47 authority and actual access events as a standing compliance risk requiring periodic review.

---

## 6. Test 4 — Recursive Commitments Verification Test

**Derived from:** B2.110

**TEST QUESTION:** Do all entities at all structural levels satisfy Paper 1 commitments at their level-appropriate scope per B1.20?

**TEST MECHANISM:** Execute the B2.110 eight-step recursive verification sequence in order:

**Step 1 — Entity inventory.** Enumerate all cells, aspects, and Selves in the deployment. Confirm the inventory is complete and that no structural entities are outside the governance record.

**Step 2 — Cell-level verification.** For each cell, apply the B2.14 verification frameworks: confirm the cell has a substrate with A2.40 provenance; confirm cell-level orchestration rules authored per A2.04; confirm conflict records preserved per the Paper 1 first-class conflict commitment; confirm the cell's substrate is the source of truth for its coordination state.

**Step 3 — Aspect-level verification.** For each aspect, apply the B2.19 verification frameworks: confirm the aspect has a substrate carrying the coordination state of its constituent cells; confirm aspect-level orchestration rules; confirm aspect-level conflict preservation; confirm aspect-level source-of-truth status.

**Step 4 — Self-level verification.** For each Self, apply the B2.24 verification frameworks: confirm Self-level substrate and DNA layer completeness; confirm Self-level orchestration rules; confirm Self-level conflict preservation and registry; confirm Self-level source-of-truth.

**Step 5 — Cross-level consistency.** Apply A5.14 composition requirements to verify consistency across levels: the cell-level substrates, aspect-level substrates, and Self-level substrate are compositionally coherent and do not contradict each other on facts each is authoritative for.

**Step 6 — Conflict registry review.** Inspect the conflict registry per B2.108 at each level. Verify that registered conflicts are addressed or explicitly preserved as open; verify that no unregistered conflicts exist that should have been captured.

**Step 7 — Provenance chain verification.** Apply the A5.08 provenance completeness test at each structural level. Verify that provenance chains at cell, aspect, and Self scope are complete and navigable — every piece of substrate content can be traced to its origin, authority basis, and modification history.

**Step 8 — Record verification results.** Record the verification results for all entities at all levels per A2.40, creating an auditable compliance record with writer, timestamp, and references to the governance frameworks applied.

**PASS CONDITION:** All entities at all three structural levels pass their level-appropriate Paper 1 commitments verification in Steps 2–4. Cross-level consistency per Step 5 holds. The conflict registry per Step 6 is clear of unresolved conflicts or contains only explicitly preserved open conflicts. Provenance chains per Step 7 are complete at all three scopes. Verification results per Step 8 are recorded.

**FAIL CONDITION:** Any entity at any structural level fails its level-appropriate verification in Steps 2–4. Cross-level consistency in Step 5 reveals contradictions without governance basis. The conflict registry in Step 6 contains unresolved or unregistered conflicts. Provenance chains in Step 7 are incomplete at any scope. Verification results cannot be recorded because governance records are themselves incomplete.

**REMEDIATION SIGNAL:** If cell-level and aspect-level verification consistently fail while Self-level verification passes, the primary anti-pattern is B3.21 Deployment-Level-Only Governance — governance has concentrated at the deployment level and left lower levels without level-appropriate Paper 1 compliance. For individual entity failures that do not follow this pattern, apply the anti-pattern per the failing dimension: provenance gaps signal B3.20 variants; conflict registry failures signal the conflict-first-class anti-pattern at the relevant scope; orchestration rule absences signal the rule authoring anti-pattern at the relevant scope.

---

## 7. Test 5 — Entity-Level Compliance Test

**Derived from:** B2.109

**TEST QUESTION:** Do entity-level operational tests per B2.109 pass at cell, aspect, and Self scope?

**TEST MECHANISM:** Execute the full A5.01–A5.16 Paper 1 operational test suite at each of the three structural scopes. Running the suite at cell scope means applying each test to each cell's substrate and governance structure using the B2.14 cell-level frameworks as the scope definition. Running at aspect scope means applying each test to each aspect's substrate and governance structure using the B2.19 aspect-level frameworks. Running at Self scope means applying each test to the Self's full DNA and action layer structure using the B2.24 frameworks.

Key tests within the suite that carry distinct weight across levels:

**A5.04 (rule authoring test):** at cell scope, verify that cell-level orchestration rules are authored; at aspect scope, verify aspect-level orchestration rules; at Self scope, verify DNA layer completeness per B1.06.

**A5.08 (provenance completeness):** at each scope, verify that substrate content carries complete A2.40 provenance. The failure mode at lower scopes is often that provenance discipline applied at Self scope is not replicated at cell and aspect scope.

**A5.09 (four accountability questions):** at each scope, verify that the four questions — who, what, when, why — can be answered for governance events. Cross-level access events tested in Test 3 are a subset of the events A5.09 applies to here.

**A5.14 (composition requirements):** at each scope, verify that composition requirements hold within that scope's internal structure, not only at the boundary where scopes meet.

**A5.16 (reproducibility):** at each scope, verify that the substrate's governance state can be reconstructed from its provenance record — this is the scope-appropriate application of the determinism contract.

**PASS CONDITION:** All A5.01–A5.16 tests pass at all three structural scopes — cell, aspect, and Self. No test that passes at Self scope fails at cell or aspect scope because of scope contraction.

**FAIL CONDITION:** Tests fail at any structural scope. Cell-scope tests fail, indicating cells are not independently governed and are relying on aspect- or Self-level governance to supply compliance properties they should carry themselves. Aspect-scope tests fail. Self-scope tests pass but lower-scope tests fail — the characteristic signature of B3.21 Deployment-Level-Only Governance.

**REMEDIATION SIGNAL:** If non-Self-scope tests systematically fail while Self-scope tests pass, the primary anti-pattern is B3.21 Deployment-Level-Only Governance. The remediation is to extend governance structure downward: author cell-level and aspect-level orchestration rules, establish provenance discipline at those scopes, configure level-appropriate authority distribution per B2.107, and re-run the test suite. For individual test failures that do not follow this pattern, apply the anti-pattern per the failing test: A5.04 failure at any scope signals rule authoring absence at that scope; A5.08 failure signals provenance incompleteness; A5.09 failure signals accountability gaps; A5.14 failure signals composition requirement violations.

---

## 8. Composite B1.19/B1.20 Test Result and Anti-Pattern Summary

The composite operational result for B1.19 and B1.20 requires all five tests to pass. No partial pass is architecturally coherent: Tests 1 through 3 together cover the access-governance dimension of B1.19, and a gap in any one creates an ungoverned access vector that the passing tests cannot compensate for. Tests 4 and 5 together cover the recursive-compliance dimension of B1.20, and a gap in either leaves the recursion incomplete.

The three primary anti-patterns this battery detects are:

**B3.20 Ungoverned Cross-Level Access** is detected by Test 1 (access rules absent or incomplete) and Test 3 (access events outside authority distribution). Form 3 of this anti-pattern — access-rule-absent design — is the more fundamental failure and is detected first by Test 1; Form 1 — access without authorization — may exist independently of Form 3 if rules are present but not enforced.

**B3.21 Deployment-Level-Only Governance** is detected by Tests 4 and 5 in combination. The diagnostic signature is Self-scope tests passing while cell-scope and aspect-scope tests fail. This anti-pattern is structurally invisible when governance is assessed only at the deployment level, which is why Tests 4 and 5 explicitly descend to cell and aspect scope rather than relying on Self-level audit alone.

**B3.26 Authority Ambiguity** is detected by Test 2. The anti-pattern arises when A2.47 does not differentiate authority by structural scope — either because the specification is absent or because it grants uniform authority across all levels. Authority Ambiguity is a prerequisite condition for Ungoverned Cross-Level Access: if authority distribution is undifferentiated, any access rule that references authority is effectively vacuous.

The tests follow a logical dependency sequence. Test 2 (authority distribution) provides the reference against which Test 3 (unauthorized access) evaluates events; running Test 3 before Test 2 has passed yields indeterminate results. Test 1 (access rules completeness) must pass before Tests 4 and 5 have their full operational grounding, because the recursive commitments verification in Test 4 and the entity-level compliance in Test 5 both presuppose that cross-level access governance is in place. In practice, the tests can be run in any order for diagnostic purposes, but a deployment should be brought to Test 1 and Test 2 compliance before relying on Test 3 results as definitive, and Tests 4 and 5 are most informative after Tests 1 through 3 have been addressed.

---

## 9. Conclusion

B1.19 and B1.20 are among the more demanding of the Paper 2 foundational commitments because they span all three structural levels simultaneously and require governance properties that are genuinely recursive rather than nominally so. The five tests formalized here provide the deployment-facing verification structure that makes compliance with these commitments checkable rather than asserted.

Tests 1 through 3 operationalize the B1.19 requirement that cross-level access be governed by authored rules resident in the DNA layer and that access events stay within an explicitly configured authority distribution. Test 4's eight-step recursive sequence sweeps all entities at all levels, making it the most comprehensive single test in the battery: it is the test that would detect a deployment where Self-level governance was carefully constructed while cell-level and aspect-level governance were never established. Test 5's three-scope application of the Paper 1 test suite closes the loop: it verifies that the Paper 1 operational commitments hold not just at the top but through the full structural depth of the deployment.

A deployment that passes all five tests has established that its cross-level architecture is governed — that access rules exist and cover the required directions, that authority is appropriately distributed across levels, that access events fall within that authority, that every entity at every level satisfies Paper 1 commitments at its scope, and that the Paper 1 operational test battery passes at cell, aspect, and Self scope. That is the condition the B1.20 recursive governance commitment names. The five tests make it verifiable.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Operational Tests for Cross-Level Access and Recursive Governance (B1.19/B1.20): Five Deployment-Facing Tests Including Access Rules Completeness, Authority Distribution Correctness, Unauthorized Access Detection, Recursive Commitments Verification, and Entity-Level Compliance, Each With Question, Mechanism, Pass, Fail, and Remediation Signal.* May 13, 2026. ORCID: 0009-0004-8065-3235.
