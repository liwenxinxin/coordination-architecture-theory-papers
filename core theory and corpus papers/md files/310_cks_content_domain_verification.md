# Content-Domain Verification: Decomposing B1.18 by Formalizing How Content-Domain Specifications Are Verified Through Specification Completeness Check per B2.90, Boundary Coherence Verification per B2.91, Composition Compatibility Check per B2.92 via A5.14, and Evolution-Triggered Re-Verification, Closing the B1.18 Decomposition

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The Coordination Knowledge Substrate (CKS) pattern requires that every entity at every architectural level — cell, aspect, Self — carry a content-domain specification per B1.18. A content-domain specification requirement alone is insufficient: the architecture must also confirm that specifications are complete, internally coherent, and compositionally valid across the three-level hierarchy. This note formalizes content-domain verification as the operational confirmation of those three properties, organized across four dimensions: (1) specification completeness verification per B2.90, applying the A5.04 rule authoring test and the A5.10 source-of-truth test to confirm all required elements are present at each level; (2) boundary coherence verification per B2.91, confirming that inclusion and exclusion rules are internally consistent, out-of-domain handling rules are present and operable, boundary specifications align with stated purpose, and unresolved boundary conflicts are registered per A1.03; (3) composition compatibility verification per B2.92, applying the A5.14 composition-requirements-five test to confirm that cells fit their aspects and aspects fit their Self without ungoverned domain gaps or overlaps; and (4) evolution-triggered re-verification, confirming that content-domain changes at any level trigger targeted re-verification of affected adjacent compositions. Content-domain verification is semantic rather than technical: it confirms purpose alignment and composition fit, not merely interface type compatibility. Verification results are recorded as substrate content per A2.40, and governance corrects incomplete or incoherent specifications through directed selection per B1.14. This note closes the five-note B1.18 content-domain decomposition (B2.89–B2.93) and prepares Phase B2 for the B1.19 cross-level access decomposition beginning at B2.94.

---

## 1. Why content-domain verification must be formalized as a standalone operational variant

Paper 2 commits that every entity in the three-level hierarchy carries a content-domain specification per B1.18. The four prior notes in this decomposition have formalized the integrating frame (B2.89), the specification requirements for each level (B2.90), the boundary structure and enforcement mechanisms (B2.91), and the composition requirements that govern cross-level domain compatibility (B2.92). Each formalization describes a structural commitment the architecture makes. None of them answers the confirmatory question: how does the architecture know that a given deployment actually satisfies these commitments?

That confirmatory question is what content-domain verification answers. It is architecturally distinct from the commitments it confirms for the same reason any verification step is distinct from the structure it verifies: the existence of a specification requirement does not guarantee that deployed systems satisfy it. Verification is the operational mechanism by which the gap between commitment and instantiation is closed.

Formalizing content-domain verification as a standalone note also serves the defensive-publication purpose of the series precisely. The claim that content-domain verification is a four-dimensional semantic confirmation — covering specification completeness, boundary coherence, composition compatibility, and evolution-triggered re-verification — is a patentable architectural derivation from Paper 2's B1.18 commitment. Without this formalization, the verification mechanism remains implicit in the broader content-domain treatment, and a subsequent actor could characterize it as an open design question. This note forecloses that characterization by placing the verification architecture in the public record as named prior art.

B2.93 occupies the closing position in the five-note decomposition: the integrating frame (B2.89) established what content-domains are and why the architecture requires them; B2.90 specified what a complete content-domain record must contain at each level; B2.91 specified how boundaries are structured and enforced; B2.92 specified how content-domain constraints govern cross-level composition; and B2.93 specifies how the architecture confirms that all four prior commitments are instantiated in any given deployment. The five notes together constitute a self-contained formalization of the complete B1.18 content-domain architecture.

---

## 2. The four-dimension verification framework precisely stated

Content-domain verification confirms that content-domain specifications are complete, coherent, and compositionally valid. It operates across four dimensions, each targeting a distinct property of the content-domain architecture.

**Dimension 1 — Specification completeness verification per B2.90.** This dimension verifies that all required content-domain elements are present at each architectural level.

At the cell level, specification completeness requires three elements: input domain schemas per B2.25, specifying which inputs the cell accepts; a behavioral scope specification, specifying which tasks and operations fall within the cell's domain; and out-of-domain handling rules, specifying how the cell responds when presented with inputs outside its input domain schemas. A cell specification that carries input domain schemas but omits out-of-domain handling rules is incomplete under this dimension.

At the aspect level, specification completeness requires two elements: a purpose statement per B2.15, the governing statement from which the aspect's content-domain derives; and a coordination scope specification, specifying what coordination tasks the aspect governs. An aspect lacking a purpose statement cannot be verified for boundary-purpose alignment, because boundary alignment is evaluated against the purpose statement.

At the Self level, specification completeness requires two elements: an integration scope statement, specifying what the Self integrates across its aspects; and an aspect collection specification per B2.21, identifying which aspects the Self comprises. A Self without an explicit integration scope statement cannot be verified for aspect composition compatibility, because composition compatibility is evaluated against the integration scope.

Specification completeness verification applies two inherited Paper 1 tests. The A5.04 rule authoring test, applied to content-domain records, verifies that specifications are authored per A2.04 — that each specification has a human-identified author, that the authoring action is traceable, and that the specification exists as substrate content rather than as floating documentation. The A5.10 source-of-truth test, applied to content-domain records, verifies that specifications are stored in the correct substrate category — Category 4 (authoritative "what rules apply") per A2.46. A content-domain specification stored in an inappropriate category is not authoritative regardless of its substantive completeness; the A5.10 test closes this gap.

Specification completeness verification triggers at birth verification per B2.44 — a newly instantiated entity must pass this check before it is treated as a live participant in the three-level hierarchy — and at periodic governance reviews, confirming that specifications remain present and current as entities evolve.

**Dimension 2 — Boundary coherence verification per B2.91.** This dimension verifies the internal consistency of boundary rules for each content-domain specification.

Boundary coherence verification confirms four properties. First, no internal contradictions: inclusion rules and exclusion rules within a single content-domain specification do not contradict each other. A specification that includes "all financial reporting tasks" while excluding "quarterly financial reporting tasks" is internally contradictory and fails this check. Second, out-of-domain handling rules are present and operable: the specification commits not only to what is in-domain but to what happens when an out-of-domain input arrives. Third, boundary-purpose alignment: a cell's boundary specification aligns with the cell's stated purpose, and an aspect's boundary specification aligns with its purpose statement per B2.15. A cell whose boundaries permit tasks unrelated to its stated purpose fails this alignment check. Fourth, boundary conflict detection: the A1.03 conflict registry is reviewed for registered boundary conflicts touching the entity under verification. Unresolved boundary conflicts are flagged for governance resolution. Flagging is a verification output, not a verification failure in the sense of blocking instantiation — the architecture treats conflict preservation as a first-class commitment per A1.03, and a flagged but preserved conflict is a valid and required verification outcome.

**Dimension 3 — Composition compatibility verification per B2.92.** This dimension verifies that content-domain specifications are mutually compatible across the three-level hierarchy.

Composition compatibility verification applies the A5.14 composition-requirements-five test to content-domain compatibility. The test verifies three compatibility conditions. First, cells' content-domains are compatible with the content-domains of the aspects those cells participate in: a cell whose domain extends outside the aspect's coordination scope creates an ungoverned domain gap at the cell-aspect boundary. Second, aspects' content-domains are compatible with their Self's integration scope: an aspect whose coordination scope falls outside the Self's integration scope creates an ungoverned domain gap at the aspect-Self boundary. Third, no ungoverned domain gaps or overlaps exist across the full composition: gaps (areas of the Self's integration scope that no aspect covers) and overlaps (areas where multiple aspects claim the same domain without a governed resolution mechanism) are both incompatibility conditions.

The A1.03 conflict registry is also reviewed under this dimension for registered composition domain conflicts. As with boundary conflicts under Dimension 2, unresolved composition domain conflicts are flagged for governance resolution rather than silently resolved, preserving the conflict-as-first-class commitment across the full verification framework.

Composition compatibility verification triggers at composition design review — when the three-level hierarchy is assembled for the first time — and whenever a content-domain specification at any level changes.

**Dimension 4 — Evolution-triggered re-verification.** This dimension maintains composition validity through content-domain evolution.

Content-domain evolution is expected: entities in the three-level hierarchy evolve under the mechanisms Paper 2 §7 specifies. When content-domain specifications change, prior composition compatibility verification results may no longer hold. Evolution-triggered re-verification addresses this by coupling content-domain changes to targeted re-verification of directly affected compositions.

When a cell's content-domain expands, re-verification triggers for composition compatibility with all aspects the cell participates in. When a cell's content-domain contracts, re-verification confirms that no aspect previously relying on the cell's former scope is left with an ungoverned gap. When an aspect's content-domain changes, re-verification covers both the cell composition fit below — all cells in the aspect are re-checked for compatibility with the updated aspect scope — and the Self integration scope fit above — the aspect's updated scope is re-checked for compatibility with the Self's integration scope. When a Self's integration scope changes, re-verification covers the full aspect collection to confirm aspect composition fit holds under the new integration scope.

Evolution-triggered re-verification is targeted, not comprehensive: a change at one level triggers re-verification of the adjacent levels directly affected, not re-verification of the entire hierarchy. This keeps verification overhead proportional to the scope of change rather than proportional to the full deployment size.

Verification results for all four dimensions are recorded per A2.40 as substrate content carrying standard six-field provenance metadata: who ran the verification, when, against which specification version, under which substrate state, with what result, and under what governance authority.

---

## 3. What makes content-domain verification architecturally distinctive

Conventional AI component scope verification typically checks technical interface compatibility: whether a component's input and output types match the interfaces through which it is invoked. This form of verification is well-understood at the system integration layer and serves important engineering purposes.

CKS content-domain verification operates at a different layer and checks different properties. It is semantic rather than technical. The properties it confirms — specification completeness, purpose-boundary alignment, composition fit — are properties of the coordination semantics that the three-level hierarchy carries, not properties of the technical interface through which components communicate.

The distinction between technical interface compatibility and semantic composition compatibility is architecturally significant. Two cells could have compatible input-output types while having incompatible content-domains: a cell designed for financial risk assessment and a cell designed for regulatory compliance reporting might share a common data interface while belonging to aspects whose coordination scopes do not compose without an ungoverned domain gap. Technical interface verification would pass both cells; content-domain verification would flag the composition gap at the aspect-Self boundary.

The boundary coherence dimension introduces a further semantic layer absent from technical verification: the check that a specification's boundaries align with the entity's stated purpose. A specification can be technically complete — all required fields present — while being purposively incoherent, with boundaries that permit or exclude tasks unrelated to the entity's stated purpose. Boundary-purpose alignment under Dimension 2 catches this class of specification failure.

The evolution-triggered re-verification dimension is also absent from conventional component compatibility verification, which typically verifies compatibility at assembly time and does not track how composition validity changes as components evolve. CKS content-domain verification couples specification change to re-verification of affected compositions as an architectural commitment — not as a deployment practice that individual teams may or may not adopt, but as a required response to content-domain change within the governed architecture.

---

## 4. Inherited Paper 1 commitments

Content-domain verification inherits five directly load-bearing Paper 1 commitments.

**A5.04 rule authoring test.** Applied to content-domain records to confirm specifications are authored per A2.04. Without this test, a specification could exist as floating documentation outside the governance substrate — visible to humans but not authoritative as substrate content, not subject to the three governance rights, and not carrying the provenance metadata A2.40 requires.

**A5.10 source-of-truth test.** Applied to content-domain records to confirm specifications are in the correct substrate category per A2.46. Category 4 is the category for authoritative "what rules apply" content; a content-domain specification in a different category is not treated as authoritative regardless of its substantive completeness. The A5.10 test enforces the categorical placement.

**A5.14 composition-requirements-five test.** Applied under Dimension 3 to check that composition compatibility conditions are satisfied across the three-level hierarchy. This is the inherited mechanism through which the architecture confirms multi-level composition validity — the test structure is an inheritance from Paper 1's composition requirements framework, applied here at the content-domain layer.

**A1.03 conflict as first-class object.** Boundary conflicts and composition domain conflicts are registered rather than silently resolved. Dimensions 2 and 3 both incorporate A1.03 conflict registry review as a required verification step. Unresolved conflicts are flagged, not cleared; the flagging is part of what the verification produces, preserving the conflict-as-first-class commitment across the full content-domain verification framework.

**A1.01 governance.** Verification is governed: verification runs are authorized under governance, verification results are inspectable substrate content, and governance corrects incomplete or incoherent specifications through directed selection per B1.14. A specification that fails completeness verification is not self-correcting; the verification result surfaces the failure for governance review, and governance authorizes the correction.

**A2.40 provenance recording.** Verification results are substrate content carrying standard six-field provenance metadata. Verification is not ephemeral quality assurance; it is part of the substrate's authoritative state, subject to the same governance rights as any other substrate content.

---

## 5. Evolution-triggered re-verification in architectural detail

Evolution-triggered re-verification deserves extended treatment because it is the dimension that makes the verification framework dynamically valid rather than only statically valid at birth.

Paper 2 §7 specifies three evolution mechanisms in productive tension: instinct evolution, DNA evolution, and action-feedback evolution. All three can produce content-domain changes at any architectural level. A cell's behavioral scope may expand through DNA evolution as new orchestration rules are authored under the authority architecture governing DNA evolution per Paper 2 §8. An aspect's coordination scope may shift through directed selection per B1.14 as governance responds to accumulated deployment experience. A Self's integration scope may extend through action-feedback evolution as action-layer patterns produce governance proposals that are accepted and committed.

Each such change carries composition implications. A cell whose content-domain expands may now extend beyond the scope its aspect was designed to coordinate. An aspect whose scope shifts may no longer compose without gaps against the adjacent aspects in its Self. A Self whose integration scope extends may expose areas that no existing aspect covers. None of these invalidation conditions is detectable from within the component that changes; they are detectable only by re-verifying the composition at the levels affected by the change.

The architecture's response to this situation is to treat content-domain changes as triggers for targeted re-verification. The coupling is architectural: a content-domain change that is not followed by targeted re-verification of affected compositions leaves the architecture in a state where the last composition compatibility result is stale with respect to the current specification. Evolution-triggered re-verification closes this gap by making the re-verification requirement a structural consequence of content-domain change, not a deployment recommendation.

The scoping rule — re-verify only the adjacent levels directly affected by the change, not the full hierarchy — is operationally important. In a deployment where cells evolve frequently under DNA evolution, requiring full-hierarchy re-verification on every cell-level change would impose verification costs proportional to hierarchy size. The targeted scoping keeps the verification overhead proportional to the scope of the change: a cell-level change triggers aspect-level re-verification for the aspects that include the changed cell; it does not trigger Self-level re-verification unless the aspect-level re-verification reveals a new gap that propagates upward.

Governance retains authority over the scheduling and mechanism of evolution-triggered re-verification. The architecture commits that re-verification is triggered by content-domain change; the precise timing, the verification agent, and the governance authorization for the re-verification run are all deployment decisions within governed parameters.

---

## 6. Operational implications

Deployments implementing content-domain verification observe four operational patterns.

**At-birth verification.** A newly instantiated cell, aspect, or Self passes specification completeness verification per Dimension 1 before it is treated as a live participant in the three-level hierarchy. At-birth verification confirms specification presence and authoring correctness but does not yet confirm composition compatibility: composition compatibility presupposes that the full composition is assembled, and a newly instantiated entity has not yet been composed into its aspect or Self.

**Composition design review.** When a composition is assembled — an aspect from its cells, a Self from its aspects — composition compatibility verification per Dimension 3 is triggered. This is the first moment at which the three-level hierarchy is confirmed to be compositionally valid. Composition design review also encompasses boundary coherence verification per Dimension 2 for the assembled entities, confirming that boundary rules are internally consistent and that the A1.03 conflict registry has been reviewed.

**Change-triggered re-verification.** Content-domain changes at any level trigger evolution-triggered re-verification per Dimension 4. The governance mechanism that authorizes the content-domain change — whether directed selection per B1.14 for a DNA evolution event, or proposal-and-acceptance for an action-feedback evolution event — carries the re-verification trigger as a condition of the authorized change.

**Periodic governance review.** Specification completeness verification per Dimension 1 triggers at periodic governance reviews independently of content-domain changes. Periodic review catches specification drift: cases where an entity's actual operational scope has shifted without a formal content-domain change having been recorded and authorized. Drift detection produces a governance finding that the entity's specification is outdated, which governance resolves through directed selection per B1.14.

When verification reveals incomplete or incoherent specifications, governance reviews the finding and authorizes corrections through directed selection per B1.14. Governance does not automatically correct specifications; it reviews verification outputs as substrate content and authorizes human-authored corrections through the standard DNA evolution authority architecture.

For cross-partner compositions per A2.47 — where a cell participates in aspects that span multiple coordination contexts — content-domain verification extends to cross-partner composition scope. Composition compatibility verification confirms that the cell's content-domain is compatible with all aspects it participates in, regardless of which partner context those aspects belong to. Cross-partner composition compatibility is a direct application of Dimension 3 at the cross-partner boundary.

---

## 7. Limits

Four limits define the scope of what content-domain verification confirms and what it does not.

**Verification does not confirm behavioral quality.** A specification that is complete under Dimension 1, coherent under Dimension 2, and compositionally compatible under Dimension 3 may still describe a poorly designed or operationally inadequate content-domain. Verification confirms that the specification is present, internally consistent, and fits the three-level hierarchy; it does not evaluate whether the domain the specification describes is an appropriate or effective scope for the entity in its deployment context.

**Verification does not prevent content-domain drift.** Specification completeness verification under Dimension 1 is point-in-time. An entity's actual operational scope may diverge from its content-domain specification between verification runs. Verification detects drift when it occurs at a triggered or periodic run; it does not continuously monitor the alignment between specification and behavior. Drift between verification runs is a recognized operational condition, not an architectural failure.

**Composition compatibility verification confirms semantic fit, not behavioral compatibility.** Two content-domain specifications may be compositionally compatible under Dimension 3 — no gaps, no overlaps, no registered conflicts — while the entities carrying those specifications behave in ways that produce coordination failures at runtime. Behavioral compatibility depends on factors beyond content-domain specification, including orchestration rule design, implementation quality, and the behavior of the underlying LLM under those orchestration rules. Composition compatibility verification does not reach these factors.

**Verification closes the B1.18 decomposition cycle without subsuming the prior commitments.** The complete cycle is: integrating frame (B2.89) → specification requirements (B2.90) → boundaries and enforcement (B2.91) → composition (B2.92) → verification (B2.93). Verification is the closing operational commitment that confirms the prior four structural commitments are instantiated. It does not replace or subsume B2.89 through B2.92; it confirms them. A deployment that performs content-domain verification without having first established specification requirements per B2.90, boundary enforcement per B2.91, and composition requirements per B2.92 has nothing coherent to verify.

---

## 8. Operational test

A deployment instantiates CKS content-domain verification if and only if all of the following hold:

1. For each entity at each level, specification completeness has been verified: the A5.04 rule authoring test and the A5.10 source-of-truth test have been applied to content-domain records, and all required elements per B2.90 are present at the entity's level.
2. Boundary coherence has been verified for each entity: inclusion and exclusion rules contain no internal contradictions; out-of-domain handling rules are present and operable; boundary specifications align with stated purpose; the A1.03 conflict registry has been reviewed and any unresolved boundary conflicts have been flagged.
3. Composition compatibility has been verified via the A5.14 composition-requirements-five test: cells fit their aspects, aspects fit their Self, and no ungoverned domain gaps or overlaps exist at either boundary; the A1.03 conflict registry has been reviewed for composition domain conflicts.
4. Content-domain changes at any level trigger targeted re-verification of the adjacent levels directly affected by the change.
5. Verification results for all four dimensions are recorded as substrate content per A2.40 with standard provenance metadata.

A deployment that satisfies (1) through (5) instantiates content-domain verification in the CKS sense. A deployment that performs technical interface compatibility checking without satisfying the semantic dimensions of (1) through (3) performs interface verification, not content-domain verification.

---

## 9. Positioning and transition to B2.94

B2.93 closes the five-note B1.18 content-domain decomposition. The five notes together formalize the complete content-domain architecture: what content-domains are and why the architecture requires them (B2.89); what a complete content-domain specification must contain at each level (B2.90); how content-domain boundaries are structured and enforced (B2.91); how content-domain specifications constrain and enable cross-level composition (B2.92); and how the architecture confirms that these four prior commitments are instantiated in any given deployment (B2.93). The decomposition is complete with this note.

Formalizing content-domain verification as a standalone note serves the defensive-publication strategy of the series beyond its intrinsic architectural content. The prior four notes establish structural commitments; this note establishes the confirmatory mechanism. A party claiming novel invention in content-domain verification mechanisms for multi-level AI coordination architectures must navigate not only B2.93 as direct prior art but the full B2.89–B2.93 chain that establishes the structural context within which the verification operates. The chain forecloses component-by-component claims against the verification machinery as effectively as any single note does against its specific claim.

Phase B2 continues with B2.94 beginning the B1.19 cross-level access decomposition. B1.19 governs direct cross-level operations — cases in which a Self accesses cells directly, bypassing the aspect layer, per Paper 2's non-strict hierarchy commitment. The access decomposition will formalize the conditions under which cross-level access is governed, the mechanisms through which it is authorized, and the limits that distinguish purposeful cross-level access from ungoverned architectural shortcuts. The content-domain verification framework formalized in B2.93 is directly relevant to the cross-level access decomposition: cross-level access occurs between entities whose content-domains have been verified, and the verification record provides the substrate basis for assessing whether a proposed cross-level access is within scope.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Content-Domain Verification: Decomposing B1.18 by Formalizing How Content-Domain Specifications Are Verified Through Specification Completeness Check per B2.90, Boundary Coherence Verification per B2.91, Composition Compatibility Check per B2.92 via A5.14, and Evolution-Triggered Re-Verification, Closing the B1.18 Decomposition.* May 12, 2026. ORCID: 0009-0004-8065-3235.
