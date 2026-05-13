# Operational Tests for Content-Domain (B1.18): Five Deployment-Facing Tests Including Specification Completeness, Boundary Coherence, Composition Compatibility, Complete Verification, and Evolution-Triggered Re-Verification, Each With Question, Mechanism, Pass, Fail, and Remediation Signal

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Content-domain — the architectural commitment formalized as B1.18 — requires that every entity in a CKS-governed multi-level architecture carry an explicit, governed specification of the scope within which it operates: what inputs it addresses, what purpose it serves, what coordination it governs. Without explicit content-domain, composition is unverifiable, governance gaps accumulate silently, and the Paper 2 commitment that higher levels operate over lower levels *as content domain* becomes architecturally inert. This note formalizes five deployment-facing operational tests for B1.18, drawing on the B1.18 decomposition in B2.89–B2.93. Each test carries a test question, test mechanism, pass condition, fail condition, and remediation signal. Test 1 (Specification Completeness, B2.90) verifies that level-appropriate specification elements are present in the DNA layer. Test 2 (Boundary Coherence, B2.91) verifies internal consistency of boundary rules. Test 3 (Composition Compatibility, B2.92) verifies that content-domain specifications enable semantic composition assessment — cells must address their aspect's coordination purpose, not merely satisfy a technical composition check. Test 4 (Complete Content-Domain Verification, B2.93) runs all four dimensions jointly. Test 5 (Evolution-Triggered Re-Verification) verifies that content-domain changes through directed selection trigger re-verification of all affected compositions. The primary anti-pattern detected by this suite is B3.19 Implicit Content-Domain in any of its three sub-forms; the secondary anti-pattern is B3.04 Undifferentiated Cell.

---

## 1. Background: Why Content-Domain Requires Operational Tests

Paper 2 commits that higher levels in the three-level CKS architecture — cell, aspect, Self — operate over lower levels *as content domain*. An aspect operates over its constituent cells for its coordination purpose. A Self operates over its aspects as the integrated whole. This operating relationship is not merely structural: it is semantic. The aspect's coordination purpose defines the territory within which its cells must operate; the Self's integration scope defines the territory within which its aspects must operate. If that semantic relationship is not explicitly specified and governed, the architecture cannot verify that composition is valid, cannot detect coordination gaps, and cannot assess whether changes to cell or aspect boundaries have disrupted the structure.

Content-domain specifications are DNA-layer content per B1.06. They fall under Category 4 content per A2.46 — orchestration-shaping specifications that govern how entities relate to each other and to their parent structures. As DNA-layer content, they are authored by humans under directed selection per B1.14, governed under the standard human-governed commitment, and subject to A2.40 provenance requirements. Their absence from the DNA layer — whether through omission (Form 1 of B3.19), vagueness that prevents operational classification (Form 2), or presence in documentation rather than in the substrate itself (Form 3) — is the defining failure mode this test suite detects.

The five tests below are applied at deployment time and at re-verification intervals. They are not design-time guidelines; they are operational questions with determinate pass and fail conditions.

---

## 2. Test 1 — Specification Completeness Test (B2.90)

**TEST QUESTION.** Does each entity carry a complete content-domain specification appropriate to its level in the DNA layer?

**TEST MECHANISM.** Apply the B2.90 content-domain specification requirements check. For each entity in the deployment, verify level-appropriate specification elements:

*At cell level:* (a) Input domain schemas are present — the cell's specification defines what types of input it addresses and, where applicable, what types it rejects. (b) Behavioral scope specification is present — the cell's specification defines what coordination tasks it performs within its domain. (c) Out-of-domain handling rules are present — the cell's specification defines how it behaves when presented with inputs outside its domain (reject, escalate, delegate, or other governed response).

*At aspect level:* (a) Purpose statement is present per B2.15 — the aspect's specification names the coordination purpose it serves, stated with sufficient precision to assess whether member cells address it. (b) Coordination scope specification is present — the aspect's specification defines the domain of coordination over which it operates, enabling both cell-to-aspect compatibility assessment and aspect-to-Self integration assessment.

*At Self level:* (a) Integration scope statement is present — the Self's specification defines the domain within which its aspects collectively operate. (b) Aspect collection is specified per B2.21 — the aspects composing the Self are named and their relationship to the integration scope is stated.

For all levels: verify that specifications reside in the DNA layer under B1.06, not in documentation, design-time notes, or external artifacts. Verify that each specification carries A2.40 provenance — author, timestamp, rationale, and version.

**PASS CONDITION.** All level-appropriate specification elements are present in the DNA layer for every entity in the deployment. Each specification carries A2.40 provenance. No specification element is present only in documentation outside the substrate.

**FAIL CONDITION.** Any level-appropriate specification element is absent for any entity. Any content-domain specification resides in documentation rather than in the DNA layer. Any specification lacks A2.40 provenance, making its authority and currency unverifiable.

**REMEDIATION SIGNAL.** Failure indicates Implicit Content-Domain B3.19 Form 1 (absent — specification element was never authored) or Form 2 (vague — specification exists but lacks sufficient precision to classify inputs or assess composition). Remediation: author the missing or vague content-domain specifications through directed selection per B1.14, placing them in the DNA layer with A2.40 provenance. Do not treat documentation updates as remediation; the specification must be substrate content.

---

## 3. Test 2 — Boundary Coherence Test (B2.91)

**TEST QUESTION.** Are content-domain boundary rules internally consistent — no contradictions between inclusion and exclusion rules, and boundary rules aligned with the entity's stated purpose?

**TEST MECHANISM.** Apply the B2.91 boundary coherence check. For each entity in the deployment, inspect the DNA layer for boundary rules and verify:

(a) Inclusion rules and exclusion rules do not contradict each other for any input type. An input type that is simultaneously included by one boundary rule and excluded by another creates an unresolvable classification ambiguity. Each candidate input must be classifiable as in-domain or out-of-domain by the boundary rules without contradiction.

(b) Boundary enforcement rules are present and operable. The specification must not merely describe a domain; it must specify the enforcement mechanism — the orchestration rules that cause the entity to act differently on in-domain versus out-of-domain inputs. A description of scope without enforcement rules is a boundary in name only.

(c) Boundary specifications are sufficiently precise to classify any given input as in-domain or out-of-domain without requiring human judgment at classification time. Specifications that leave the classification ambiguous at the boundary — cases where a human must decide whether a given input falls within scope before the entity can process it — do not satisfy this requirement. The entity must carry enough specification to make that determination itself under its orchestration rules.

(d) The A1.03 conflict registry is checked for registered boundary conflicts. If any boundary conflict involving this entity has been registered and not yet resolved, that registered conflict is a boundary coherence failure until addressed.

**PASS CONDITION.** No internal contradictions between inclusion and exclusion rules. Every input type classifiable as in-domain or out-of-domain by inspection of the entity's boundary rules. Boundary enforcement rules are present and operable under the entity's orchestration substrate. No unresolved boundary conflicts registered in the A1.03 registry for this entity.

**FAIL CONDITION.** Contradictory inclusion and exclusion rules for any input type. Input types that cannot be classified without human judgment at classification time. Boundary enforcement rules absent — boundary is descriptive rather than operative. Unresolved boundary conflicts in the A1.03 registry.

**REMEDIATION SIGNAL.** Failure indicates Implicit Content-Domain B3.19 Form 3 (unenforced — boundary exists in specification but is not operative in the substrate) or Form 2 (vague — boundary cannot classify inputs determinately). For contradictions: register in A1.03 conflict registry and resolve through directed selection per B1.14. For absent enforcement rules: author boundary enforcement rules as orchestration substrate content. Do not resolve ambiguity by widening the boundary; widening without purpose alignment produces a different failure at Test 3.

---

## 4. Test 3 — Composition Compatibility Test (B2.92)

**TEST QUESTION.** Do entity content-domain specifications enable composition compatibility assessment, and do entities semantically address their parent's coordination purpose or integration scope?

**TEST MECHANISM.** Apply the B2.92 composition compatibility check, using the A5.14 composition-requirements-five test with explicit semantic dimension. This test is semantic, not merely technical: it is insufficient for schemas to compose or for type constraints to be satisfied. The content-domain of a lower-level entity must address the coordination purpose of its parent entity. Four checks compose this test:

*Cell-to-aspect semantic check.* For each cell within an aspect: does the cell's content-domain address a part of the aspect's stated coordination purpose? A cell is semantically compatible with its aspect if its input domain and behavioral scope speak to work the aspect coordinates. A cell is semantically incompatible if its domain — however well-specified — addresses coordination work that does not contribute to the aspect's purpose. Technical composition compatibility is not sufficient for this check.

*Aspect-to-Self semantic check.* For each aspect within a Self: does the aspect's content-domain address a part of the Self's integration scope? An aspect is semantically compatible with its Self if its coordination scope speaks to a facet of the integrated whole the Self constitutes. An aspect whose coordination scope falls entirely outside the Self's integration scope is semantically incompatible, regardless of whether it is structurally present in the Self.

*Domain gap check.* Are there areas of an aspect's coordination purpose not covered by any member cell? A gap means the aspect commits to coordinating a domain for which no member cell is scoped. Under this condition, the aspect cannot fulfill its coordination purpose; the gap will either be silently ignored or require ad-hoc human intervention not supported by the architecture. Similarly, are there areas of a Self's integration scope not addressed by any member aspect?

*Domain overlap check.* Do any peer cells within the same aspect have overlapping content-domains? Overlap between peer cells creates coordination ambiguity: when an input falls within both cells' domains, the aspect has no governed basis for routing it. Overlap does not automatically fail the test — legitimate shared-domain cells exist — but unresolved overlap without an explicit routing rule in the aspect's orchestration substrate is a coherence failure.

Check the A1.03 conflict registry for registered composition domain conflicts involving any entity in scope.

**PASS CONDITION.** Every cell semantically addresses its aspect's coordination purpose. Every aspect semantically addresses its Self's integration scope. No ungoverned domain gaps in aspects or Self. Domain overlaps, if present, are covered by explicit routing rules in the orchestration substrate. The A1.03 registry is clear of unresolved composition domain conflicts, or conflicts are actively being addressed under directed selection.

**FAIL CONDITION.** Cells whose content-domains do not address their aspect's coordination purpose. Aspects whose content-domains do not address their Self's integration scope. Ungoverned domain gaps — areas of coordination purpose or integration scope not addressed by any lower-level entity. Unresolved domain overlaps lacking routing rules. Unaddressed composition domain conflicts in the A1.03 registry.

**REMEDIATION SIGNAL.** Failure indicates Implicit Content-Domain B3.19 causing composition incompatibility — either the entities' specifications are absent or vague enough that this semantic check cannot be performed, or the check reveals a real semantic mismatch. If the aspect's purpose statement is too vague to assess cell compatibility, this also indicates B3.05 Purposeless Aspect, which must be remediated before the composition check can proceed. Remediation path: author or sharpen content-domain specifications through directed selection per B1.14, addressing purpose alignment at every level; register domain conflicts in A1.03 and resolve under directed selection.

---

## 5. Test 4 — Complete Content-Domain Verification Test (B2.93)

**TEST QUESTION.** Does the complete four-dimension B2.93 content-domain verification pass across all entities in the deployment?

**TEST MECHANISM.** Apply the B2.93 complete content-domain verification. This test runs all four dimensions jointly and requires all four to pass:

*Dimension 1 — Specification completeness.* Apply the A5.04 rule authoring test to content-domain specifications: are specifications authored under the correct authority, present in the DNA layer, and verifiable as human-governed substrate content? Apply the A5.10 source-of-truth test to content-domain records: does the substrate hold the authoritative version of each specification, with no shadow versions in documentation or in LLM context?

*Dimension 2 — Boundary coherence.* Apply Test 2 (§3 above) across all entities. Any boundary coherence failure in any entity fails this dimension.

*Dimension 3 — Composition compatibility.* Apply Test 3 (§4 above) across all compositions. Any semantic incompatibility, domain gap, or unresolved overlap fails this dimension.

*Dimension 4 — Evolution-triggered re-verification status.* Have any content-domain specifications changed since the most recent full verification? If so, was B2.93 re-verification triggered, conducted, and completed for all affected compositions? Re-verification results must be recorded per A2.40. If changes occurred without triggering re-verification, or if re-verification was triggered but not completed, this dimension fails.

The complete test passes only when all four dimensions pass simultaneously. A partial pass — three dimensions passing and one failing — is a full test failure. The failing dimension identifies the specific content-domain governance area requiring attention.

**PASS CONDITION.** All four dimensions pass. Specification completeness: content-domain specifications are substrate content under A5.04 and A5.10, authored and governed correctly. Boundary coherence: all boundary rules are internally consistent and enforced per Test 2. Composition compatibility: all semantic compatibility requirements met per Test 3. Re-verification status: all post-change re-verifications were triggered, completed, and recorded.

**FAIL CONDITION.** Any single dimension fails. The failing dimension is recorded as the specific content-domain governance deficiency. Multiple-dimension failures are each recorded separately.

**REMEDIATION SIGNAL.** The failing dimension points directly to the remediation target. Dimension 1 failure: content-domain specifications are missing from the substrate or not governed correctly — apply A5.04 and A5.10 remediation. Dimension 2 failure: boundary incoherence per Test 2 remediation signals. Dimension 3 failure: semantic compatibility failure per Test 3 remediation signals. Dimension 4 failure: re-verification workflow not operating — see Test 5 (§6 below).

---

## 6. Test 5 — Evolution-Triggered Re-Verification Test

**TEST QUESTION.** When content-domain specifications change through directed selection, is re-verification triggered and completed for all affected compositions?

**TEST MECHANISM.** Inspect the DNA modification records per A2.40 for all content-domain specification changes since the last verified baseline. For each such change, verify three properties:

(a) Composition compatibility re-verification was conducted per B2.93 after the change. Re-verification must cover every composition relationship that could be affected by the changed specification: if a cell's content-domain changed, the cell-to-aspect semantic check must be re-run for every aspect that contains the cell; if an aspect's coordination scope changed, the aspect-to-Self semantic check must be re-run for every Self that contains the aspect.

(b) All affected compositions were re-assessed. A change to one entity's content-domain can propagate through multiple composition relationships. The re-verification scope must be calculated conservatively: if the full propagation scope is uncertain, err toward broader re-assessment.

(c) Re-verification results were recorded per A2.40 — each re-verification result carries the verifying author, timestamp, scope of entities re-assessed, outcome, and reference to the triggering change record. An undocumented re-verification is architecturally equivalent to a missing re-verification: there is no substrate record establishing that composition validity was confirmed.

**PASS CONDITION.** Every content-domain change in the A2.40 modification records is paired with a triggered re-verification record. Re-verifications cover all affected compositions, not only the directly modified entity. Re-verification results are recorded per A2.40 with full provenance. All re-verifications that were triggered were also completed; no re-verification was initiated and then abandoned without a recorded outcome.

**FAIL CONDITION.** Any content-domain change appears in A2.40 modification records without a corresponding triggered re-verification. Re-verifications that cover only the directly modified entity but not downstream compositions. Re-verification results that lack A2.40 provenance. Re-verifications triggered but not completed.

**REMEDIATION SIGNAL.** The failure mode is silent composition validity degradation: the architecture continues to operate without error, but the semantic relationship between cells and their aspects, or between aspects and their Self, may have become incoherent through accumulated unevaluated changes. This failure is particularly hazardous because it produces no runtime signal — the substrate carries specifications that were once valid but may no longer be. Remediation: establish a governance workflow that triggers B2.93 re-verification as a required step in every directed selection event that touches content-domain specifications. The trigger must be architectural, not procedural — it must be embedded in the orchestration substrate governing directed selection, not in a checklist outside the substrate.

---

## 7. Composite Result and Anti-Pattern Summary

**Composite content-domain test result.** All five tests must pass for B1.18 to be operationally satisfied. Passing four of five is not a partial pass; it is a failure in a specific governance dimension. The composite result is binary: the content-domain commitment is either operationally instantiated or it is not.

**Primary anti-pattern: B3.19 Implicit Content-Domain.** This anti-pattern is detected by Tests 1, 2, and 3, and can prevent Test 4 from being executable at all. It takes three sub-forms: Form 1 (absent — no content-domain specification exists for the entity; Test 1 fails immediately); Form 2 (vague — a specification exists but is insufficiently precise to classify inputs or assess composition; Test 2 or Test 3 fails when the specification cannot support determinate answers); Form 3 (unenforced — a specification exists and is precise on paper but is not operative in the entity's orchestration substrate, existing only in documentation; Test 1 or Test 2 fails when the specification is not substrate content). Any form of B3.19 is sufficient to make the full five-test suite fail.

**Secondary anti-pattern: B3.04 Undifferentiated Cell.** This anti-pattern is detected by Test 3. An undifferentiated cell lacks a distinct content-domain relative to its peers in the same aspect. Its domain either fully overlaps with one or more peer cells (producing the domain overlap condition in Test 3) or extends so broadly as to functionally subsume the aspect itself (producing a cell-to-aspect semantic compatibility failure in a different direction — the cell is not addressing a part of the aspect's purpose; it is attempting to address all of it). B3.04 can also prevent Test 2 from finding a determinate boundary, since an undifferentiated cell cannot coherently specify what is out-of-domain for it.

**Adjacent anti-pattern for Test 3: B3.05 Purposeless Aspect.** An aspect that lacks a sufficiently precise purpose statement cannot support the cell-to-aspect semantic check in Test 3, because there is no stated coordination purpose against which to assess cell compatibility. When Test 3 cannot be performed because the aspect's purpose is too vague, B3.05 is the proximate cause. Remediation must address B3.05 before B3.19's Test 3 implications can be evaluated.

---

## 8. Source Paper and Series Citations

**Source paper.** "The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance" (Li, April 2026). The three-level architecture (§5.2), the commitment that higher levels operate over lower levels as content domain (§5.2), DNA-layer content structure (§5.3), and directed selection as the evolution mechanism for governed DNA-layer content (§7.2) are the source commitments this note operationalizes.

**Paper 1.** "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). The human-governed commitment (§2.3), conflict preservation as first-class object (§3), provenance requirements (§3.1), and DNA-layer as substrate content under human authority (§4.1) are all inherited by B1.18 operational tests without redefense.

**Series.** This note is derivation note B5.06 in the CKS derivation-note series. It is the sixth note in Phase B5 (operational tests as standalone) and formalizes operational tests for the B1.18 content-domain commitment. Related series notes include B2.89–B2.93 (B1.18 decomposition), B3.19 (Implicit Content-Domain anti-pattern formalization), B3.04 (Undifferentiated Cell anti-pattern formalization), and B3.05 (Purposeless Aspect anti-pattern formalization).
