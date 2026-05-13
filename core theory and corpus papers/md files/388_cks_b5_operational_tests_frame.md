# Operational Tests Integrating Frame: Opening Phase B5 of Series B by Formalizing What Operational Tests Are in the CKS Architecture, How They Extend Series A's A5.01–A5.16 Test Suite for Paper 2's Distinctive Architectural Elements, and the Taxonomy of Test Areas for Deployment-Facing Governance Verification

**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** May 13, 2026  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Phase B5 of Series B opens with this integrating frame. The note formalizes what Phase B5 operational tests are — deployment-facing governance verification tests that governance runs against a live instantiation of Paper 2's architecture to confirm that the full architecture is correctly implemented — and distinguishes them from the three prior Series B phases: Phase B2 (which verified that individual Paper 2 commitments were correctly specified in the substrate), Phase B3 (which named anti-patterns for each commitment), and Phase B4 (which identified composition pairs between commitments). The note articulates the relationship between Phase B5 and Series A's A5.01–A5.16 operational test suite: Phase B5 does not duplicate Series A's tests but extends them by adding Paper 2-specific tests for the instinct/reasoning separation, three-level structure, lifecycle primitives, evolution mechanisms, and governance properties. The note specifies the five-component structure that each Phase B5 test note will use — test question, test mechanism, pass condition, fail condition, remediation signal — and provides the full taxonomy of test areas across the fourteen notes that follow (B5.02–B5.15). The prior art significance of formalizing these specific test questions is stated explicitly.

## 1. What Phase B5 operational tests are

An operational test in the CKS derivation series is a deployment-facing verification that governance runs against a live system to answer a specific question about whether that system correctly instantiates a given architectural commitment. Operational tests are not specifications (they do not say how the commitment should be implemented), not anti-patterns (they do not name what violation looks like), and not composition pairs (they do not identify which commitments require each other). They are the question-and-answer apparatus governance needs to confirm, at any point in a deployment's lifecycle, that the architecture is correctly in place.

The distinction is practical and important. A commitment specification (Series B Phase B2) answers: *Has this commitment been correctly decomposed into substrate content, orchestration rules, and operational variants?* An anti-pattern (Phase B3) answers: *What does violation of this commitment look like, so that governance can recognize it?* A composition pair (Phase B4) answers: *Which commitments require co-presence — so that implementing one without the other produces an architecturally incomplete result?* An operational test (Phase B5) answers a fourth and distinct question: *In this live deployment, is this commitment correctly implemented right now?*

The shift from specification to operational verification changes the audience and the mechanism. Phase B2–B4 work is governance design work — work done when architecting and specifying the system. Phase B5 work is governance verification work — work done by governance running checks against a deployed system. The tests are deployment-facing rather than design-facing, and they are organized to support the three stages at which governance typically runs them: deployment initialization (confirming the architecture is correctly established before operation begins), ongoing operation (confirming the architecture remains correctly instantiated over time), and evolution events (confirming that evolution actions have not inadvertently disrupted architectural correctness).

## 2. Distinction from prior Series B phases

The four phases of Series B prior to Phase B5 approached Paper 2's architectural commitments from four complementary angles. Phase B1 established the foundational commitments themselves — the twenty core architectural claims that Paper 2 adds to or extends from Paper 1. Phase B2 decomposed each commitment into its operational variants, asking what the commitment means concretely across implementation configurations. Phase B3 named the anti-patterns — the specific failure modes that arise when a commitment is violated or implemented incorrectly. Phase B4 formalized composition pairs — the thirty-plus commitment pairs that must co-occur for either commitment to be correctly instantiated.

Phase B5 adds the fifth angle: the operational test battery. Where Phase B2 established what correct implementation looks like from the specification side, Phase B5 establishes how governance confirms correct implementation from the verification side. Where Phase B3 named what violations look like, Phase B5 specifies the test questions that detect violations before they become entrenched. Where Phase B4 identified which commitments require each other, Phase B5 provides the tests that confirm pair co-presence in a live deployment.

The four angles are complementary and non-redundant. A governance team that has only Phase B2 knows what to specify but has no battery for verifying that the specification was implemented. A governance team that has only Phase B3 can recognize violations after they appear but has no proactive test regimen for confirming correctness. A governance team that has Phase B2–B4 but not Phase B5 has the full architectural design apparatus but is missing the deployment-verification apparatus. Phase B5 completes the battery.

## 3. Relationship to Series A's A5.01–A5.16 test suite

Series A's Phase A5 established the baseline operational test suite for Paper 1's sixteen architectural commitments: human-governed, substrate-cell boundary, conflict-as-first-class, AI-as-substrate-mediator, tool-agnosticism, linear-cost scaling, path retraceability, substrate-as-source-of-truth, KO/OIDA inheritance, determinism contract, non-specialist governance, labor allocation, composition requirements, three adjacencies, orchestration-layer distinction, and hybrid systems composition. Each of A5.01–A5.16 is a standalone operational test for one of these commitments.

Phase B5 does not duplicate or replace A5.01–A5.16. All Paper 1 commitments remain in effect at every level of Paper 2's architecture — the instinct/reasoning separation operates on top of Paper 1's substrate, not instead of it, and every cell in a Paper 2 deployment is still a Paper 1 cell subject to Paper 1's full commitment set. The A5 tests therefore apply to every Paper 2 deployment as baseline.

What Phase B5 adds are the tests for Paper 2's distinctive architectural elements — the elements that Paper 2 introduces and that A5.01–A5.16 do not cover. These are organized into six clusters:

**Instinct/reasoning separation tests (B5.02).** Paper 2's foundational architectural move is the separation of the LLM's fast-path pattern-matching layer from the CKS substrate's deliberate reasoning layer as independently-evolving components of one Self. The test questions confirm that the separation is architecturally in place — not merely conceptually intended — with the reasoning layer capable of routing around bad instinct, conflict preservation catching what instinct silently merged, and the governance boundary between instinct and reasoning explicitly materialized in substrate content rather than informally understood.

**Three-level structure tests (B5.03).** Paper 2 introduces three architectural levels — cell, aspect, Self — with relational role membership (the same underlying artifact can participate in multiple aspects simultaneously). The tests confirm that the three levels are correctly instantiated, that structural roles are relational and purpose-defined rather than intrinsic, and that the recursive-levels principle holds (Paper 1's commitments apply at cell, aspect, and Self scope without modification).

**Lifecycle tests (B5.04).** Paper 2 formalizes three lifecycle primitives — birth, mating, death — at every level. The tests confirm that each lifecycle operation is human-governed in the Paper 1 sense (authority, not labor), that mating is implemented through one of the three governable patterns (union, selective merge, lineage-preserved union), and that death is distinguished by type (functional obsolescence vs. lineage supersession) with governance processes appropriate to each type.

**Evolution mechanism tests (B5.05).** Paper 2 introduces three evolution mechanisms in productive tension — instinct evolution (undirected mutation at the LLM and infrastructure layer), DNA evolution (directed selection through human-governed orchestration substrate updates), and action-feedback evolution (lived experience closing the loop from action layer back to DNA layer). The tests confirm that each mechanism is correctly instantiated, that their productive tension is architecturally maintained rather than collapsed into one of the three, and that multi-level, horizontal, and vertical evolution are all available.

**Content-domain and roles tests (B5.06).** Paper 2 extends Paper 1's governance architecture to cover verification substrates, the instinct/reasoning boundary as governed substrate content, and governance shapes across all three evolution mechanisms. The tests confirm that these governance properties are correctly instantiated.

**Cross-level access and recursive governance tests (B5.07).** Paper 2's three-level structure permits non-hierarchical access patterns (the Self can access cells directly when purpose requires) and mandates that Paper 1's governance commitments hold recursively at every level. The tests confirm correct implementation of cross-level access and recursive governance.

## 4. Operational test structure

Each Phase B5 test note formalizes its tests in a five-component structure. This structure is the same across all notes in the phase, which makes the test battery executable as a consistent regimen regardless of which governance participant runs it.

**Test question.** What specific architectural property is being confirmed? The test question names the commitment and the specific dimension of that commitment being probed. A well-formed test question is answerable with observable substrate state — it does not depend on intent, documentation, or verbal assertion.

**Test mechanism.** How is the test administered? The mechanism specifies what governance looks at, what substrate content is examined, what comparison is made, and what questions are asked of the deployment's human governance participants. Mechanisms are tool-agnostic — they specify what to examine, not which software to use for examination, consistent with Paper 1's tool-agnosticism commitment.

**Pass condition.** What does passing look like? The pass condition states the specific observable state that constitutes correct instantiation. Pass conditions are binary where architectural correctness is binary (the commitment is either in place or not) and graduated where the commitment admits of degrees (for example, the proportion of evolution actions that go through verified governance pathways).

**Fail condition.** What does failing look like? The fail condition states the specific observable state that constitutes incorrect instantiation or architectural incompleteness. Fail conditions are specific enough that governance can recognize them without ambiguity.

**Remediation signal.** What does failure indicate about which governance correction is needed? The remediation signal maps the specific failure to the specific Phase B2 operational variant, Phase B3 anti-pattern, or Phase B4 composition pair that the failure reveals. This mapping makes the test battery actionable — a failed test does not just identify a problem but points to the prior-phase documentation that specifies the correction.

This five-component structure is itself prior art for this series. Formalizing operational tests for an AI coordination architecture in this specific structure — with remediation signals mapped to anti-pattern and composition-pair documentation — is a design pattern that the derivation series establishes publicly here.

## 5. Test taxonomy and Phase B5 sequence

Phase B5 spans fourteen notes beyond this integrating frame (B5.02–B5.15), organized by the following taxonomy:

**Commitment-specific tests (B5.02–B5.07).** Six notes, each covering one cluster of Paper 2-specific commitments: instinct/reasoning separation (B5.02, parent: B1.01); three-level structure (B5.03, parent: B1.02); lifecycle primitives — birth, mating, death at all three levels (B5.04, parents: B1.05–B1.08); evolution mechanisms — instinct, DNA, action-feedback, multi-level, horizontal/vertical (B5.05, parents: B1.09–B1.16); content-domain governance — verification substrates, boundary as governed content, multi-shaped governance (B5.06, parents: B1.17–B1.18); cross-level access and recursive governance (B5.07, parents: B1.19–B1.20). Each note provides the five-component test structure for all commitments in its cluster.

**Composition pair integrity tests (B5.08).** One note covering the tests that confirm Phase B4's composition pairs are correctly co-present in a live deployment. Where Phase B4 identified which pairs of commitments must co-occur, B5.08 provides the tests that confirm co-occurrence is actually instantiated.

**Anti-pattern detection tests (B5.09).** One note covering the tests that detect specific Phase B3 anti-patterns. Where Phase B3 named what violations look like, B5.09 provides the detection tests that governance runs proactively rather than waiting for failures to surface.

**Temporal test suites (B5.10–B5.13).** Four notes organizing tests by deployment lifecycle stage rather than by commitment. B5.10 covers the deployment initialization test suite — the tests governance runs before declaring a deployment ready for operation. B5.11 covers the ongoing governance test suite — the tests governance runs on a recurring basis to confirm continued architectural correctness. B5.12 covers the evolution event test suite — the tests governance runs when any of the three evolution mechanisms produces a change, to confirm the change has not disrupted architectural properties. B5.13 covers the compliance demonstration test suite — the organized presentation of test evidence for external parties who need to verify that a deployment correctly instantiates the CKS architecture.

**Synthesis (B5.14–B5.15).** Two closing notes. B5.14 provides the complete operational test synthesis — the full Phase B5 battery assembled as a unified document that governance can use as a master checklist. B5.15 provides Phase B5 closure and the opening frame for Phase B6 (boundary cases).

The twenty individual commitment-specific test notes enumerated in the master plan (B5.01–B5.20) map to this taxonomy as follows: B5.02–B5.07 cover the commitment-specific cluster tests; B5.08–B5.09 cover composition and anti-pattern detection; B5.10–B5.13 cover temporal suites; B5.14–B5.15 cover synthesis and closure. The fourteen notes in the prompt-specified sequence and the master plan's enumeration of twenty individual-commitment tests are complementary representations of the same test territory, with the cluster-based approach used here grouping related commitments for architectural coherence.

## 6. Prior art significance

Formalizing the specific operational tests for Paper 2's architecture is itself prior art, independent of the prior art established in the source paper and in Series B's earlier phases. Three prior art claims follow from this note:

**The five-component test structure as prior art.** The formalization of operational tests for a CKS deployment in the specific five-component structure — test question, test mechanism, pass condition, fail condition, remediation signal — is a design pattern established publicly here. Any party who subsequently proposes "discovering" that governance should verify CKS deployments by asking specific questions in this structure cannot claim novelty for the structure itself.

**The six-cluster taxonomy as prior art.** Organizing Paper 2's operational tests into the six clusters named above — instinct/reasoning, three-level structure, lifecycle, evolution mechanisms, content-domain governance, cross-level access and recursive governance — is a specific taxonomic decision established publicly here. Any party who subsequently proposes this or a closely related taxonomy as novel is building on publicly-prior terrain.

**The temporal test suite organization as prior art.** Organizing governance verification tests by deployment lifecycle stage — initialization, ongoing operation, evolution events, compliance demonstration — is a specific organizational decision established publicly here. Any party who subsequently proposes that AI governance verification should be organized this way cannot claim that organizational framing as a novel contribution.

The prior art significance of operational test formalization is general across architectures: the first party to publicly specify the questions that governance should ask about a given architecture, and to specify what answers constitute passing and what answers constitute failing, closes the space for subsequent parties to claim those questions as novel. Phase B5 makes that closure explicit for Paper 2's architecture.

## 7. Conclusion

Phase B5 provides the operational test battery that governance runs against live deployments of Paper 2's CKS architecture. It extends Series A's A5.01–A5.16 baseline test suite with tests specific to Paper 2's distinctive architectural elements — the instinct/reasoning separation, three-level structure, lifecycle primitives, evolution mechanisms, and governance properties. It organizes those tests in the five-component structure (test question, mechanism, pass condition, fail condition, remediation signal) that makes the battery executable and actionable. And it organizes the tests temporally (initialization, ongoing, evolution, compliance) so that governance can run the appropriate subset at each stage of a deployment's lifecycle.

The fourteen notes that follow this integrating frame (B5.02–B5.15) deliver the tests. This note establishes what the tests are for, how they relate to prior phases of Series B and to Series A, the structure they use, and the taxonomy they organize. Together, B5.01–B5.15 complete the test layer of Series B's six-phase derivation of Paper 2's architectural commitments.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Operational Tests Integrating Frame: Opening Phase B5 of Series B by Formalizing What Operational Tests Are in the CKS Architecture, How They Extend Series A's A5.01–A5.16 Test Suite for Paper 2's Distinctive Architectural Elements, and the Taxonomy of Test Areas for Deployment-Facing Governance Verification.* May 13, 2026. ORCID: 0009-0004-8065-3235. Note B5.01 in the CKS Derivation Notes series.
