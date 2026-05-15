# Phase D5 Overview and Test Expansion Framework

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

Phase D2 note D2.24 produced a twenty-test operational test suite for Paper 3's governance commitments, covering the core lifecycle and governance requirements for inter-Self coordination under a shared substrate. Phase D3 subsequently formalized 27 anti-patterns — failure modes not covered by D2.24's single-commitment structural tests. Phase D4 established 26 composition pairs — joint governance requirements that arise when two commitments are held simultaneously, also not covered by D2.24's baseline. Phase D5 closes this coverage gap by systematically adding tests for what Phases D3 and D4 established, plus governance quality and learning governance properties. The result is a 55-test comprehensive operational library organized into six layers: D2.24's original twenty tests plus five expansion categories — Tests 21–30 (composition pair tests), Tests 31–40 (anti-pattern detection tests), Tests 41–45 (governance quality tests), Tests 46–50 (evolution learning tests), and Tests 51–55 (population-scope tests in the calibrated-humility register). All 55 tests follow the binary format D2.24 established: YES/NO questions answerable from governance records alone, without implementation knowledge. This note introduces Phase D5, states what D2.24 established and why expansion is needed, describes the five expansion categories with their test number ranges, states the expanded test library format, and describes the note structure for the D5.02–D5.14 notes that follow.

## 1. What D2.24 established and why expansion is needed

Note D2.24 produced the first operational test suite for Paper 3's governance commitments. The twenty baseline tests were structured as binary questions — answerable YES or NO from governance records alone, without consulting implementation code or requiring specialist technical knowledge — and covered the core lifecycle and governance requirements that Paper 3's six claims produce at the inter-Self scope.

The twenty baseline tests addressed eight governance requirement areas: shared substrate construction records (Tests 1–3), dissolution records (Tests 4–5), configuration completeness (Tests 6–8), exchange bounding (Tests 9–11), conflict registry (Tests 12–14), escalation routing (Tests 15–16), evolution feed mechanics (Tests 17–18), and path retraceability across perimeters (Tests 19–20). Together, these tests provided a practitioner with the means to determine whether a deployment satisfies Paper 3's core structural requirements by reading governance records alone.

What D2.24 was not designed to cover is what Phases D3 and D4 subsequently established. Phase D3 formalized 27 anti-patterns — specific failure modes in which governance structure is nominally present but a particular pathological pattern undermines the commitment the structure is meant to satisfy. None of D2.24's twenty tests specifically detect anti-pattern presence. They verify compliant structure; they do not ask whether the signature of a known failure mode appears in the records alongside that structure.

Phase D4 established 26 composition pairs — joint governance requirements that arise when two named commitments are held simultaneously. Composition pair notes formalized that two commitments held together produce obligations that neither generates alone. None of D2.24's twenty tests covers two-commitment governance satisfaction simultaneously; each baseline test examines one commitment in isolation.

Phase D5 closes this coverage gap. The result — D2.24's twenty baseline tests plus Phase D5's thirty-five additions — is a 55-test library that enables complete compliance verification for Paper 3's governance commitments: structural verification, anti-pattern detection, composition pair joint verification, governance quality assessment, evolution learning depth, and population-scope governance where applicable.

## 2. The binary format: consistency across all 55 tests

The defining format property of the test library is binary: every test is a YES/NO question answerable from governance records alone, without consulting implementation code, deployment logs, or specialist technical knowledge. This is the format D2.24 established for its twenty baseline tests. All 55 tests in the expanded library maintain this format exactly.

The binary format has a specific practical consequence: a governance practitioner who can read the governance records — the shared substrate, configuration documents, conflict registry, escalation routing specification, evolution feed records — can apply every test in the library without implementation access and without specialized architectural expertise. No test requires interpreting code. No test requires knowing what a particular deployment engine does internally.

This connects to Paper 1's non-specialist governance commitment, which holds at inter-Self scope by inheritance from Paper 3's shared substrate carrying all six Paper 1 commitments within scope. The governance record structures that Paper 3's commitments require must be readable and actionable by governance practitioners, not only by system architects. A test library that required specialist technical knowledge to apply would contradict this property at the test-suite layer. The binary format, consistently applied across all 55 tests, preserves it.

Each test in the expanded library specifies four elements: (1) the test number and name; (2) what records to examine; (3) the binary question the test asks; and (4) what a YES answer indicates and what a NO answer indicates. The pass/fail semantics are explicit for every test: YES means the governance records satisfy the requirement; NO means a specific, nameable gap that a practitioner can act on.

## 3. Expansion Category 1 — Composition pair tests (Tests 21–30)

Phase D4 established 26 composition pairs for Paper 3. Composition pair notes formalized that holding two commitments simultaneously produces requirements neither commitment generates alone — the pair creates a joint governance obligation that a practitioner examining each commitment independently would not detect.

D2.24's twenty baseline tests examine each commitment individually. Tests 21–30 add joint verification capability. Each composition pair test examines governance records for evidence that two commitments are satisfied in a way that is mutually consistent — not merely that each is satisfied in isolation.

Representative composition pairs in this range include: shared substrate construction records that also satisfy exchange bounding requirements (Claim 1 × Claim 2 joint governance); conflict registry entries that carry the layer-routing attribution required by the four-locus evolution feed (Claim 3 × Claim 4 joint governance); and configuration documentation that establishes both the persistence loci required by FAI and the recursive applicability structure required by Claim 5 (Claim 1 × Claim 5 joint governance). Each test produces a YES/NO answer about whether the joint obligation is satisfied in the governance records, not whether each individual commitment is satisfied.

## 4. Expansion Category 2 — Anti-pattern detection tests (Tests 31–40)

Phase D3 formalized 27 anti-patterns for Paper 3 — specific failure modes organized by the claim they violate. Anti-pattern categories include opaque inter-Self communication (Claim 1 violations), shallow merge and federation-only patterns (Claim 2 violations), silent conflict resolution at the inter-Self perimeter (Claim 3 violations), ungoverned evolution feed (Claim 4 violations), fixed configuration and meta-governance escape (Claim 5 violations), and emergent-coordination-replaces-substrate patterns (Claim 6 violations).

D2.24's twenty baseline tests verify that compliant governance structure is present. They do not ask whether a known failure mode's signature is simultaneously present in the records. A deployment can pass all twenty baseline tests and still exhibit the anti-pattern of opaque inter-Self communication if its substrate construction records satisfy formal requirements but conceal the information that practitioners need for governance oversight. Tests 31–40 add this detection capability.

Anti-pattern detection tests are structurally different from compliance verification tests. A compliance test asks: does the governance record contain the required structural element? An anti-pattern detection test asks: does the governance record show the characteristic absence, distortion, or substitution that identifies a known failure mode? Both question types are answerable YES or NO from governance records alone. The difference is in what a NO answer identifies: in a compliance test, NO identifies a missing element; in an anti-pattern detection test, NO identifies the presence of a specific named failure mode that Phase D3 established and named.

## 5. Expansion Category 3 — Governance quality tests (Tests 41–45)

D2.24's baseline tests verify governance structure: are the required records present, do they contain the required elements, do they satisfy the architectural requirements Paper 3's commitments impose. Tests 41–45 add governance quality assessment — a distinct dimension that structural tests do not cover.

The three quality dimensions these tests address are: determinism contract satisfaction, documentation standard compliance, and non-specialist accessibility. Determinism contract satisfaction asks whether the governance records demonstrate that the shared substrate's coordination state is deterministic in the sense Paper 1's determinism commitment requires at inter-Self scope — that two practitioners reading the same governance records at the same moment would reach the same answers to governance questions. Documentation standard compliance asks whether the governance records meet the standard that makes them actionable: are terms defined where they are introduced, are record structures consistent across events, are governance decisions traceable to the authorizations that permitted them. Non-specialist accessibility asks whether the governance records are structured so that a practitioner without specialist technical expertise in the underlying architecture can read, understand, and act on them.

Governance quality tests are not pass/fail on structural completeness. They are pass/fail on usability and fidelity properties that structural completeness alone does not guarantee. A governance record can be structurally complete — containing every element the baseline tests require — while failing governance quality tests because its content is not deterministic, its documentation is inconsistent, or its language is inaccessible to non-specialist practitioners. Tests 41–45 surface this failure mode.

## 6. Expansion Category 4 — Evolution learning tests (Tests 46–50)

D2.24's evolution feed tests (Tests 17–18) cover the basic mechanics of the four-locus evolution feed: are evolution feed records present at FAI dissolution, do they carry the layer-routing attribution the four-locus mechanism requires, is the three-case routing rule (DNA-layer content to DNA evolution, action-layer content to action-feedback evolution, instinct evolution receiving no FAI input by architectural commitment) reflected in the records. These tests verify that the feed exists and is attributed correctly.

Tests 46–50 add governance depth to the evolution learning dimension. Trust calibration records ask whether governance records document how trust assessments of participating governance structures are updated following FAI events — whether the governance learning from each event is captured in a form that can inform subsequent FAI event governance decisions. Post-mortem improvement record quality asks whether governance records for FAI events that produced evolution-relevant outcomes document the causal structure in enough depth to be actionable for governance improvement: what produced the outcome, what rule or configuration produced it, and what governance response is indicated. DNA absorption governance depth asks whether the governance records for DNA-layer evolution feed items document the full authorization chain from FAI event identification through layer routing to DNA incorporation — so that the ancestry of any DNA change is retraceable through governance records alone.

These are governance depth tests, not structural presence tests. A governance record that mechanically logs evolution feed items at dissolution satisfies D2.24's Tests 17–18. A governance record that additionally documents trust calibration, causal structure in post-mortems, and DNA absorption authorization chains satisfies Tests 46–50.

## 7. Expansion Category 5 — Population-scope tests in the calibrated-humility register (Tests 51–55)

Tests 51–55 are in the calibrated-humility register, and this placement requires explicit statement.

Paper 3's Claim 6 articulates population-scale collective evolution as the architectural object its preceding five claims compose into at population register when accumulated FAI events across many governance-compliant Selves operate under joint authority across population-level governance perimeters. Claim 6 is rendered with calibrated humility: population-scale deployments do not yet exist; the architectural commitment is to what the preceding five claims produce at population scope through composition, with specific population-scale dynamics awaiting empirical observation.

Tests 51–55 inherit this calibration. They test governance properties that the architecture supports and that Paper 3's Claim 6 requires at population register — but not governance properties that are architecturally required in the same way as Tests 1–20's Claims 1–5 compliance tests. The three population-scope dimensions these tests address are: participation configuration completeness (whether governance records specify participating Self identities, perimeter authorities, approval mechanics, and joint authority structure for population-scope coordination events); governance capacity ceiling specification (whether governance records document the governance authority limits and load boundaries at population scope, such that practitioners can assess whether a proposed population-scope event is within governed capacity); and trust calibration record currency (whether trust calibration records for population-scope governance reflect the current state of participating governance structures, such that a practitioner can assess the trust basis for a proposed population-scope event from governance records alone).

A practitioner applying Tests 51–55 to a deployment that does not yet operate at population scope should record the tests as Not Applicable rather than as failures. The calibrated-humility register marks these tests as appropriate to population-scope deployments, not as required elements of single-pair or small-n inter-Self deployments. This distinction is architecturally significant: it means a deployment can pass all 50 non-population-scope tests (Tests 1–50) and achieve full compliance verification for Claims 1–5 governance without addressing Tests 51–55.

## 8. The expanded test library format

Each test in the expanded library follows the format D2.24 established for its baseline tests. Every test specifies:

1. **Test number and name.** A sequential number (1–55) and a short descriptive name that identifies what governance requirement the test addresses.
2. **Records to examine.** A specification of which governance records the practitioner should read in order to apply the test — shared substrate records, configuration documents, conflict registry, escalation routing specification, evolution feed records, or population-scope governance documents, as the test requires.
3. **The binary question.** The YES/NO question the test asks, stated in terms that a practitioner can answer by reading the specified records without implementation knowledge.
4. **Pass and fail interpretation.** What a YES answer indicates (which requirement is satisfied, or which anti-pattern is absent) and what a NO answer indicates (which specific gap or failure mode the practitioner has identified and should act on).

The format is identical across all 55 tests. A practitioner can apply any test in the library without reading the other tests; each test is self-contained.

## 9. Phase D5 note structure

D5.01 (this note) introduces the framework. D5.02 through D5.14 cover the five expansion categories and their full sets of tests. D5.15 closes Phase D5 with a summary of the complete 55-test library and its structural relationship to Paper 3's governance commitments.

Each note in D5.02–D5.14 covers one expansion category, stating each test in full form. The tests are designed to be usable by governance practitioners reading from this note series without prior knowledge of Phase D3 anti-pattern formalization or Phase D4 composition pair content. The only precondition for applying the tests is access to the governance records that Paper 3's commitments require a compliant deployment to maintain.

The 55-test library Phase D5 produces closes the coverage gap that Phases D3 and D4 opened by establishing content beyond D2.24's design scope. D2.24's twenty baseline tests provided complete operational coverage for Paper 3's core structural governance requirements. Phase D5 extends that coverage to the full set of compliance verification needs that Paper 3's governance commitments generate: structural verification, anti-pattern detection, joint commitment verification, governance quality assessment, learning governance depth, and population-scope governance where applicable. Together, the six layers constitute a comprehensive operational library for practitioners responsible for verifying compliance with Paper 3's governance commitments from governance records alone.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Phase D5 Overview and Test Expansion Framework.* May 15, 2026. ORCID: 0009-0004-8065-3235.
