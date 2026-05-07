# Five Requirements at Every Partner: A Standalone Operational Test for Composition Coherence in Multi-Substrate CKS Deployments

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the composite operational test that verifies the five composition requirements named in A2.76–A2.80 (within A1.13) at every composition partner participating in a multi-substrate CKS deployment, and across every boundary between partners.

## Abstract

The CKS source paper defends six architectural commitments at the single-substrate scope. A prior derivation note (A1.13) formalized the constraint set those commitments project onto multi-substrate composition; a second tier of derivation notes (A2.76–A2.80) decomposed A1.13 into five operationally distinct Requirements — per-substrate human governance preservation, per-substrate retraceability preservation, per-substrate determinism preservation, AI-as-mediator at every layer, and human-selective composition. The present note formalizes the composite operational test that ties the five Requirements together at deployment scale: for every composition partner, all five Requirements must hold, and at every cross-partner boundary, the first four must be preserved. The test delegates Requirement-specific verification to prior Phase A5 tests (A5.01–A5.10) rather than duplicating them; its proper scope is composition-level coherence — per-partner satisfaction *plus* cross-partner preservation — which the per-substrate tests do not by themselves establish. The note states what the test verifies, specifies the procedure as eight operational steps, defines pass and fail with location identification, names the composition-specific anti-patterns the test detects, identifies the integration points at which it should run, and bounds its scope against three adjacent verifications it deliberately does not perform.

## 1. Why the composition-requirements-five test needs to be formalized as standalone

A2.76–A2.80 decomposed A1.13 into five Requirements, each with its own architectural content. Verifying any one Requirement at any individual substrate exercises one or more of the per-substrate tests A5.01–A5.10 supplies. Verifying that all five hold *across the composition* — at every partner, plus at every boundary between partners — is a different job. Composition-level failure modes — asymmetric satisfaction across partners, cross-boundary requirement loss, vendor-determined partner selection — are invisible to any test that examines one substrate at a time.

Formalizing the composite test as standalone allows downstream implementers and reviewers to evaluate composition coherence through one named procedure rather than through ad-hoc reassembly of the per-Requirement tests. The standalone test specifies which prior tests run, against which partners, with what cross-partner verification, and with what aggregate pass/fail criteria. A composition that passes A5.14 has demonstrated, in one cited procedure, that it satisfies all five composition Requirements at every participating partner and preserves the boundary-spanning Requirements across cross-partner boundaries. A composition that fails has identified where the failure sits — by Requirement, by partner, by boundary.

The strategic posture follows. The source paper §4.5 frames hybrid composition as architecturally significant but defers composition mechanisms to future work (§13.3). A1.13 and A2.76–A2.80 close the constraint side of the design space without occupying the mechanism side. A5.14 closes the verification side: any future composition mechanism, by the author or others, must demonstrate satisfaction of this test (or argue against it by name) to remain in continuity with the CKS pattern.

A5.14 opens the composition-tests cluster of Phase A5 — A5.14, A5.15 (hybrid pattern mapping per A1.16), A5.16 (reproducibility per A4.06) — and follows three earlier clusters supplying the per-substrate tests A5.14 delegates to: four-governance-rights (A5.01–A5.04), AI-mediation-and-substrate-state (A5.05–A5.10), and substrate-operational-properties (A5.11–A5.13).

## 2. The architectural commitment under test

A5.14 verifies satisfaction of the five composition Requirements that A2.76–A2.80 decompose from A1.13:

- **Requirement A — per-substrate human governance preservation** (A2.76). Every composition partner remains human-governed: humans retain inspect, modify, and override authority over substrate content and orchestration rules at any time, with no operation, vendor, or runtime layer in principle preventing those rights.

- **Requirement B — per-substrate retraceability preservation** (A2.77). Every partner preserves path retraceability: any decision visible at or originating from the partner can be traced to the substrate elements, orchestration rules, content, and rationale that produced it.

- **Requirement C — per-substrate determinism preservation** (A2.78). Every partner satisfies the determinism guarantees the source paper §4.1 and §11.3 commit the substrate side of the governance boundary to: substrate state, once written under appropriate authority, is what the substrate carries until written again under appropriate authority.

- **Requirement D — AI-as-mediator at every layer** (A2.79). The LLM operates as substrate mediator at every layer of the composition — at each underlying substrate, at any intermediate composed view, at the cell aggregating partners, and at any cross-partner operation. No layer operates the LLM as autonomous agent (A3.11), terminal producer (A3.12), or substrate-authority source (A3.13).

- **Requirement E — human-selective composition** (A2.80). Which partners participate, under which composition pattern, with what cross-partner relationships is determined by human-authored substrate-resident rule (per A2.04), not by vendor recommendation, framework default, or LLM-proposed assemblage.

Each Requirement is per-substrate — the commitment holds at each partner individually, not aggregately. Requirements A through D additionally apply at composition boundaries, where state, conflicts, provenance, or control crosses between partners. The compound nature — per-partner satisfaction plus boundary preservation — is what makes a composite test necessary.

## 3. The test procedure

The procedure is composite: per-Requirement verification is delegated to prior Phase A5 tests, and the test's specific work is the composition-level aggregation, the cross-partner boundary checks, and the Requirement E substrate-resident-rule check that no prior test by itself performs.

**Step 1 — Identify all composition partners.** Enumerate every substrate that participates in the composition. Within-cell partners (multiple substrates aggregated by one cell) and cross-cell partners (substrates whose state is read or written across cell boundaries) both count, per A1.13 §1's scope.

**Step 2 — Verify Requirement A at each partner.** Run the four-governance-rights tests A5.01 (inspect), A5.02 (modify), A5.03 (override), and A5.04 (orchestration-rule authoring as governance). Pass at all four constitutes a pass on Requirement A at that partner.

**Step 3 — Verify Requirement B at each partner.** Run the provenance-completeness test A5.08 and the four-accountability-questions test A5.09. Pass at both constitutes a pass on Requirement B.

**Step 4 — Verify Requirement C at each partner.** Run the cell-behavior-determinism test A5.06 and the read-determinism test A5.07. Pass at both constitutes a pass on Requirement C.

**Step 5 — Verify Requirement D at each partner.** Run the mediator-role test A5.05. Pass on the five mediator properties — with no autonomous-agent (A3.11), terminal-producer (A3.12), or substrate-authority (A3.13) anti-pattern present — constitutes a pass on Requirement D.

**Step 6 — Verify Requirement E for the composition.** For each partner, verify that the partner is included through a human-authored substrate-resident orchestration rule (per A2.04). The rule by which the partner is included is itself substrate content under the broader human-governed authority architecture verified at Step 2. Compositions in which partner inclusion derives from vendor recommendation, framework default, or LLM proposal that bypassed substrate-resident rule authoring fail Requirement E regardless of how Steps 2–5 turn out.

**Step 7 — Verify cross-partner preservation.** For each composition boundary — any location where state, conflicts, provenance, or control crosses between two partners — verify that Requirements A through D are preserved by composition behavior, not dependent on extra-substrate enforcement: (a) no partner exercises authority over another partner's content outside human-authored authorization; (b) provenance traces cross the boundary cleanly, with cross-partner decisions retraceable to the contributing partners; (c) determinism guarantees do not weaken at the boundary; (d) the LLM remains mediator at every layer including composed views and cross-partner aggregations.

**Step 8 — Aggregate.** The composition passes A5.14 if and only if every partner passes Requirements A through E at Steps 2–6 *and* every cross-partner boundary preserves Requirements A through D at Step 7. Any single failure — at any partner on any Requirement, or at any boundary — fails the composite test.

## 4. What the test outputs

The output is a structured pass/fail with location identification.

**Pass.** Every composition partner passes the per-partner tests for Requirements A, B, C, and D, every partner is included via substrate-resident rule per Requirement E, and every cross-partner boundary preserves Requirements A through D. The composition is CKS-coherent on the five-composition-requirements axis.

**Fail with location.** Any Requirement fails at any partner, or any Requirement fails at any cross-partner boundary. The output identifies which Requirement (A through E), at which partner or boundary, with delegation to whichever sub-test (A5.01 through A5.10) returned the failure. Composition tests reporting only aggregate pass/fail cannot drive remediation; A5.14 commits to per-partner-per-Requirement-per-boundary reporting so that compositions which fail produce actionable information.

## 5. What anti-patterns the test specifically detects

A5.14 detects several composition-specific anti-patterns that the per-partner tests in isolation cannot.

**Asymmetric governance across composition.** Requirement A passes at some partners and fails at others; the composition is asymmetrically governed and carries human-governance pockets rather than being human-governed.

**Asymmetric retraceability.** Some partners have full provenance and others do not; decisions that span partners cannot be traced through the composition because the composite trace has gaps wherever a non-retraceable partner participated.

**Asymmetric determinism.** Some partners satisfy determinism guarantees and others do not; the composition's deterministic behavior is bounded by the weakest partner.

**Non-mediator AI in some partners.** Requirement D passes at some partners but fails at others — perhaps because some partners are managed under the CKS pattern and others under an autonomous-agent (A3.11), terminal-producer (A3.12), or substrate-authority (A3.13) framework. The composition operates the LLM in different roles at different partners, which the architecture does not support.

**Vendor-determined or framework-default composition.** Composition-partner selection is dictated by vendor recommendation, framework default, or LLM-proposed assemblage that bypassed substrate-resident rule authoring. Requirement E fails: the composition is vendor-selective with human acceptance, not human-selective in the architectural sense. Step 6 detects this directly, in concert with the broader composition anti-pattern set A2.95 catalogues.

**Cross-partner-requirement-loss.** Requirements A through D hold at every individual partner but break at cross-partner boundaries: provenance that exists per-partner does not cross boundaries; conflicts preserved per-partner are masked in composed views; deterministic state per-partner becomes non-deterministic in aggregate. The composition has the *appearance* of CKS-coherence at every partner with the *reality* of incoherence at the composition layer. Step 7 specifically targets this pattern.

**Primary-strict-secondary-loose patterns.** The deployment commits its "primary" substrate to the full Requirement set but treats "secondary" composition partners as loosely-governed adjacencies. Requirements A through E apply per-substrate, and the per-substrate structure does not distinguish primary from secondary partners.

## 6. How the test integrates with deployment verification

Five integration points name when A5.14 should run during a deployment's lifecycle.

*Initial deployment validation.* Before a CKS deployment with multi-substrate composition is activated, A5.14 runs against every composition partner identified in the deployment's design. Activation proceeds only after a clean pass.

*Composition partner addition.* When a new partner joins, A5.14 runs to verify that the addition does not break composition coherence — exercising the new partner against Requirements A through E and verifying that all cross-partner boundaries the new partner introduces preserve Requirements A through D.

*Composition partner removal.* When a partner is removed, A5.14 runs to verify that the remaining partners still satisfy the Requirements and that no boundary preservation depended on the removed partner's behavior. Removal does not trivially preserve coherence; the remaining composition is a different composition, and verification on the new structure is needed.

*Composition pattern change.* When the hybrid composition pattern of a partner changes (per A1.16: input-to-cell, derived-view, separate-concern), A5.14 runs against the new configuration. A partner's role affects which Requirements apply at which boundaries; pattern change requires re-verification.

*Vendor migration.* When a vendor change occurs at any layer (per A4.10), A5.14 runs at the post-migration configuration. Vendor migration may alter the realization of Requirements A through D — particularly Requirement A's no-vendor-prevention component and Requirement D's no-autonomous-agent component — and the composite test verifies that migration preserves the requirements rather than silently degrading them.

These five points are not exhaustive, but they are the architectural events at which the composition's structure changes and at which composition-coherence verification is required.

## 7. Limits of the test

A5.14 is not a complete deployment-verification test. Three scoping limits name what it does not do.

*A5.14 does not verify A1.16 hybrid composition patterns in isolation.* Whether each adjacent component is correctly positioned in Pattern A, B, or C is a separate verification, formalized at A5.15. A composition can pass A5.14 (Requirements satisfied per-partner with cross-boundary preservation) and still fail A5.15 (a partner positioned in the wrong pattern for its actual role); the converse also holds.

*A5.14 does not verify A4.06 reproducibility.* Whether a CKS deployment's outputs are reproducible across runs, vendors, infrastructure changes, and over time is a separate property formalized at A5.16. A composition can pass A5.14 and fail A5.16 if its determinism guarantees per-partner do not aggregate to reproducibility under specific environmental variations.

*A5.14 does not verify operational suitability or business appropriateness.* Whether a given composition is the right composition for the deployment's actual use case — whether its partners are well-chosen, its boundaries appropriately drawn, its complexity justified by business outcome — sits outside the architecture's scope. A5.14 verifies that the composition satisfies the architectural commitments; it does not verify that the composition is wise, efficient, or fit for purpose.

These limits are deliberate. A5.14's narrow scope is what makes it useful; a test that tried to verify everything at once would lose the precision that lets it identify location-specific failures.

## 8. Operational test (one-sentence form)

A multi-substrate CKS composition satisfies the composition-requirements-five test (A5.14) if and only if (a) at every composition partner, Requirements A through E hold — Requirement A by passing A5.01–A5.04, Requirement B by passing A5.08–A5.09, Requirement C by passing A5.06–A5.07, Requirement D by passing A5.05, Requirement E by partner inclusion via human-authored substrate-resident rule per A2.04 — and (b) at every cross-partner boundary, Requirements A through D are preserved by composition behavior rather than dependent on extra-substrate enforcement. A composition that fails any clause of (a) or (b) at any partner or boundary is not CKS-coherent on the five-composition-requirements axis, regardless of which other architectural properties it may satisfy.

## 9. Conclusion

Treating the composition requirements as five independently named operational statements (A2.76–A2.80) makes per-Requirement verification possible at any single substrate. Treating their joint satisfaction across a composition as its own architectural object — and naming the composite test that verifies it — is what makes deployment-scale CKS-coherence verifiable rather than only assertable.

The composite-delegation framing matters. A5.14 does not duplicate the per-substrate Phase A5 tests; it sequences them. The work the composite test performs that the per-substrate tests do not is the cross-partner preservation check (Step 7) and the substrate-resident-rule check for Requirement E (Step 6) — the composition-specific verifications that no individual Requirement test by itself can perform.

A5.14 opens the composition-tests cluster of Phase A5. A5.15 follows with hybrid composition pattern mapping (A1.16); A5.16 closes Phase A5 with reproducibility (A4.06). Together A5.14–A5.16 verify that a CKS deployment composes coherently along the three composition axes the source paper supports — requirements satisfaction, pattern correctness, and reproducibility. Phase A6 boundary-cases work picks up afterward, formalizing edge scenarios that the composition tests bound rather than resolve.

Subsequent work that implements, extends, or argues against the CKS composition commitments should use the composition-requirements-five test in the sense formalized here. Subsequent work that uses a different test is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Five Requirements at Every Partner: A Standalone Operational Test for Composition Coherence in Multi-Substrate CKS Deployments.* May 7, 2026. ORCID: 0009-0004-8065-3235.
