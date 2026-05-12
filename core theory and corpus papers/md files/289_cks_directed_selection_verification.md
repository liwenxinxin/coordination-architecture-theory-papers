# Directed Selection Verification — Decomposing B1.14 Directed Selection (DNA Evolution) Under Standard Authority Architecture by Formalizing How Directed Selection Events Are Verified Through Governance Authorization Check, DNA Change Correctness Verification, Retroactivity Compliance, and Behavioral Outcome Verification Using Series A Operational Tests, Closing the B1.14 Decomposition

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Directed selection in the Coordination Knowledge Substrate (CKS) pattern produces DNA changes — modifications to the stabilized orchestration substrate that governs cell-level behavior. Paper 2 specifies that directed selection operates under a standard authority architecture: humans define goals, humans or LLMs under human direction draft changes, and humans hold authority over acceptance decisions. What Paper 2 also specifies, but does not collect under a single operational description, is the post-modification verification gate that confirms a directed selection event satisfied its architectural commitments. This note names and formalizes that gate as *directed selection verification*. The verification operates across four dimensions: governance authorization verification (A5.04 rule authoring test); DNA change correctness verification (A5.10 source-of-truth test); retroactivity compliance verification (A6.02 retroactivity treatment per B2.70); and behavioral outcome verification (A5.06 cell-behavior-determinism test, A5.16 reproducibility test). Supplementary verification (A5.08 provenance-completeness, A5.09 four-accountability-questions) supports the primary four. Verification intensity scales with the modification pattern per B2.71 — structural redesign warrants comprehensive verification; incremental improvement warrants lighter, targeted verification. Cross-level verification confirms that DNA changes at Self or aspect scope do not unexpectedly affect cell behavior through expression. This note is B2.72 in Phase B2 of the derivation note series; it closes the six-note B1.14 decomposition (B2.67–B2.72) and positions Phase B2 to continue with B2.73 beginning the B1.15 action-feedback decomposition.

---

## 1. Why directed-selection-verification requires formalization as a standalone operational variant

Directed selection, as B1.14 specifies and B2.67–B2.71 decompose, is a governed, purposeful modification of DNA content under human authority. B2.67 established what DNA scope a directed selection event may reach. B2.68 established the governance machinery by which modification authority is exercised. B2.69 established how DNA versions are managed and preserved through modification events. B2.70 established the retroactivity treatment: new DNA governs forward from its modification timestamp; prior DNA versions govern prior records; retroactive rewriting is prohibited. B2.71 established the evolution patterns — incremental improvement, structural redesign, and multi-level coordination — that characterize different directed selection events.

Each of those prior notes addresses an architectural property that must hold *before or during* a directed selection event. What none of them addresses directly is the structured confirmation that a directed selection event *actually satisfied* those properties after the fact. That confirmation is directed selection verification.

The need for a distinct formalization is architectural, not procedural. A directed selection event modifies the DNA governing cell-level behavior across an operational system. The modification carries three independent sources of potential failure. The governance machinery may not have been correctly executed: the modification may lack proper authorization, may have been authored outside the delegated authority scope, or may lack the provenance record that A2.40 requires. The DNA change may not accurately reflect governance intent: unintended elements may have been added, elements may have been omitted, or the new DNA content may not correctly occupy Category 4 of the A5.10 source-of-truth five categories. The new DNA may not produce the behavioral properties the architecture requires: cell behavior under new DNA may be non-deterministic, or it may not replay reproducibly, violating A1.10 and the commitments A5.06 and A5.16 operationalize. A directed selection event that completes without verification has no structured confirmation that any of these three sources of failure is absent.

The strategic prior-art posture behind formalizing directed-selection-verification as a standalone named operational variant is the same as the prior five B1.14 decomposition notes: each patentable sub-claim in the directed-selection territory becomes occupied prior art before any party can claim it as novel. The four-dimension verification gate, the Series A test application sequence, the intensity-scaling relationship with B2.71 patterns, and the cross-level verification commitment together constitute a territory that is more granular than the general directed-selection commitment B1.14 carries. Naming them explicitly closes the patentable claim space at this level of specificity.

---

## 2. The four-dimension post-modification gate

Directed selection verification applies four dimensions of confirmation after a directed selection event completes. The dimensions are independent: each targets a different potential failure mode, and failure in any one dimension constitutes an incomplete verification regardless of the others' results.

**Dimension 1 — Governance authorization verification.** The A5.04 rule authoring test is applied to the directed selection event itself. The test asks whether the DNA change was authored by a human holding A2.47 authority for the specific DNA scope modified, whether the authorization record per A2.40 is present and complete, and whether the authorization was exercised per the governance machinery A2.04 specifies. Governance authorization verification is not a check that the DNA change is correct in content; it is a check that the decision to make the change was legitimate. A DNA change that is technically correct but unauthorized does not satisfy this dimension.

The A2.40 provenance requirement is central here. Every directed selection event must leave an authorization record that names who authorized the change, under what authority scope, at what timestamp, and with what rationale. Governance authorization verification confirms that record exists, that it references the correct authority scope, and that the authoring human was within their A2.47 delegation for the DNA modified. Without this dimension, the directed selection event has no governance chain that can be inspected retrospectively.

**Dimension 2 — DNA change correctness verification.** This dimension confirms that the DNA change was applied as intended: the new DNA content matches the authorized specification; no unintended elements were added; no intended elements were omitted. The A5.10 source-of-truth five-categories test is applied to confirm that new DNA content correctly occupies Category 4 — what rules apply — without improperly mixing in elements from other categories. A DNA change that passes governance authorization but introduces unintended orchestration rules fails this dimension.

DNA change correctness verification is a structural confirmation, not a behavioral one. It confirms the modification artifact is what governance authorized, not yet whether that artifact produces the right behavior. The distinction matters because a structurally correct DNA change may still produce behavioral anomalies, which the fourth dimension addresses separately.

**Dimension 3 — Retroactivity compliance verification.** B2.70 established the retroactivity rule: new DNA governs forward from its modification timestamp; the prior DNA version is preserved in version history per B2.69; Action records that were governed by the prior DNA version correctly reference that version in the A2.40 provenance field 4; no retroactive rewriting of prior Action records occurs under new DNA. The A6.02 retroactivity treatment is applied to confirm this temporal governance boundary is correct.

Retroactivity compliance verification checks three things: that the modification timestamp is recorded and the new DNA applies only forward from it; that the prior DNA version is preserved in version history and accessible for audit; and that the A2.40 provenance linkages in existing Action records still reference the correct DNA version for their governing period. A directed selection event that inadvertently overwrites prior DNA versions, or that causes existing Action records to appear governed by DNA that was not in effect when they were recorded, fails this dimension.

**Dimension 4 — Behavioral outcome verification.** The A5.06 cell-behavior-determinism test and A5.16 reproducibility test are applied to confirm that new DNA produces architecturally sound behavior. A5.06 verifies that cell behavior under the new DNA satisfies A1.10's determinism requirement: two cells executing under the same new DNA over the same substrate state produce equivalent substrate-write outcomes, judged at the substrate-write layer. A5.16 verifies that DNA-governed behavior replays deterministically — that a behavior sequence governed by the new DNA, replayed from the same substrate state and the same orchestration rules, produces the same outcome.

Behavioral outcome verification confirms architectural properties, not improvement quality. It does not assess whether the new DNA produces better outcomes than the prior DNA; it assesses whether the new DNA governs behavior that the architecture can rely on. A directed selection event that passes governance authorization, DNA change correctness, and retroactivity compliance but produces non-deterministic or non-reproducible behavior fails this dimension and is incomplete as an architectural event.

---

## 3. Supplementary verification

Two additional Series A tests support the primary four dimensions without constituting independent dimensions.

The A5.08 provenance-completeness test verifies that the modification event itself — the directed selection event as a recorded event in the substrate — carries complete A2.40 provenance. This goes beyond the authorization record confirmed in Dimension 1: it confirms that the full provenance chain for the modification event is present, including the substrates modified, the actor performing the modification, the timestamp, and the rationale. Provenance completeness is what makes the directed selection event auditable as a historical record, independently of whether the new DNA is operationally sound.

The A5.09 four-accountability-questions test verifies that the directed selection event can be fully accounted for: who authorized it, what was changed, when it took effect, and why governance authorized it. The four-accountability-questions test is a completeness check across the provenance and authorization record together. It is not a new check for any single dimension; it is a cross-dimension confirmation that no accountability gap exists after the four primary dimensions are confirmed.

---

## 4. Cross-level verification

The three-level architecture (cell, aspect, Self) means that a directed selection event at one level may affect behavior at another level through expression. A DNA change at Self level — modifying orchestration rules that govern the Self's overall operational posture — may propagate through expression to affect cell-level behavior in ways that were not anticipated when the change was authored. The B1.20 recursive-inheritance commitment means the same DNA layer and expression mechanisms operate at every level; cross-level effects are an architectural possibility, not an edge case.

Cross-level verification confirms that DNA changes at one level do not produce unexpected behavioral effects at lower levels. For a directed selection event at Self scope, cross-level verification applies the A5.06 and A5.16 tests to cell-level behavior under the modified DNA, not only to the cells that directly implement the modified orchestration rules but to cells whose behavior is shaped by expression of the modified DNA. For a directed selection event at aspect scope, cross-level verification applies the same tests to constituent cells. For a directed selection event at cell scope, cross-level verification is not triggered upward — cell-level DNA changes do not propagate upward to affect aspect or Self behavior.

Cross-level verification does not require that the A5.04, A5.10, and A6.02 checks be re-run at every lower level. Those dimensions are scoped to the modification event itself, which occurs at a specific level. Cross-level verification is specifically behavioral: it applies A5.06 and A5.16 to confirm that the behavioral properties the architecture requires are not disrupted at levels the modification did not directly target.

---

## 5. What makes directed-selection-verification architecturally distinctive

The contrast with conventional AI post-modification evaluation illuminates what is architecturally distinctive about CKS directed-selection-verification.

In conventional AI development, directed evolution of model behavior — fine-tuning, reinforcement learning from human feedback, prompt engineering deployed at scale — is followed by evaluation. That evaluation is typically performance-level: accuracy metrics, benchmark scores, human preference ratings, or qualitative assessments by subject-matter reviewers. The evaluation asks whether the modified model performs better on the target task. It does not ask whether the modification was authorized, whether the modification artifact correctly reflects an authorization record, whether the modification respects a temporal governance boundary, or whether the modified behavior satisfies reproducibility at a substrate level. These questions are not asked because the conventional architecture has no substrate layer at which they could be answered.

CKS directed-selection-verification is architecture-level, not performance-level. It does not ask whether the new DNA produces better outcomes than the prior DNA — that is a separate governance judgment. It asks whether the directed selection event satisfies the architectural commitments the CKS pattern makes about governance authorization, modification correctness, temporal boundary compliance, and behavioral determinism. The four dimensions together constitute a structured gate that confirms the directed selection event is a valid architectural event, independently of whether it constitutes a wise operational decision.

The three-property confirmation in one framework — governance authorization AND behavioral correctness AND retroactivity compliance — is distinctive because each property corresponds to a different layer of the architecture. Governance authorization addresses the human authority layer (who had the right to make this change and whether they exercised it correctly). Behavioral correctness addresses the execution layer (whether the new DNA governs behavior the architecture can rely on). Retroactivity compliance addresses the temporal provenance layer (whether the modification event correctly respects the historical record). No single Series A test addresses all three; the four-dimension gate is the integration point where they are applied together.

---

## 6. Inherited Paper 1 commitments

Directed-selection-verification inherits, without modification, the following Series A commitments:

**A1.01 (human-governed)** — verification is itself subject to the governance commitment: the verification tests, the verification records, and the authority to determine that verification is complete all operate under A1.01's requirement that humans retain the right to inspect, modify, and override at any time.

**A2.04 (governance authorization)** — Dimension 1 applies A5.04 to confirm compliance with A2.04's authorization requirement.

**A2.40 (provenance)** — Dimensions 1 and 3 both check A2.40 provenance fields; A5.08 supplementary verification confirms provenance completeness for the modification event as a whole.

**A2.47 (authority delegation)** — Dimension 1 confirms the authoring human held A2.47 authority for the specific DNA scope modified.

**A5.04 (rule authoring test)** — Dimension 1 primary test.

**A5.06 (cell-behavior-determinism test)** — Dimension 4 primary test; also applied in cross-level verification.

**A5.08 (provenance-completeness test)** — Supplementary verification.

**A5.09 (four-accountability-questions test)** — Supplementary verification.

**A5.10 (source-of-truth five-categories test)** — Dimension 2 primary test.

**A5.16 (reproducibility test)** — Dimension 4 primary test; also applied in cross-level verification.

**A6.02 (retroactivity treatment)** — Dimension 3 primary check.

These commitments are inherited references: directed-selection-verification does not modify, extend, or qualify any of them. The verification gate is an application of these commitments to the specific post-modification context that directed selection events create.

---

## 7. Verification intensity scaled to modification pattern

B2.71 established three directed selection patterns: incremental improvement, structural redesign, and multi-level coordination. Directed-selection-verification scales its intensity to the pattern, because different patterns carry different scope of risk and different reach of potential effects.

**Incremental improvement pattern** — a targeted DNA change within an established DNA structure, modifying specific orchestration rules without altering the structure's organization. Verification at this pattern applies all four dimensions, but the behavioral outcome dimension (A5.06, A5.16) may be scoped narrowly to the specific cells and behaviors the modified rules govern. Cross-level verification is triggered only if the modified rules participate in expression that affects higher-level DNA. The governance authorization and retroactivity dimensions are applied at full intensity regardless of pattern, because those dimensions are not scope-dependent: an incremental improvement is as subject to the governance authorization requirement as a structural redesign.

**Structural redesign pattern** — a DNA change that reorganizes the structure, adds or removes major orchestration rule categories, or alters the coordination logic across multiple cell behaviors. Verification at this pattern applies all four dimensions at full intensity and always triggers cross-level verification. The behavioral outcome dimension (A5.06, A5.16) is applied comprehensively, covering all cells and behaviors that may have been affected. A5.08 provenance-completeness and A5.09 four-accountability-questions supplementary checks are applied with additional rigor, because structural redesign produces larger provenance records and more complex authorization chains.

**Multi-level coordination pattern** — a directed selection event that spans multiple levels simultaneously. Verification at this pattern applies all four dimensions at the level of each participating modification, and cross-level verification is applied at every boundary between participating levels. The retroactivity dimension is applied at each level, because multi-level coordination may produce multiple modification timestamps that must all correctly bound the forward-only application rule.

The calibration principle is that verification intensity should be proportional to the scope of potential architectural disruption the modification pattern carries, not to the administrative complexity of the modification itself. A structurally simple incremental improvement that touches a high-frequency cell behavior may warrant more intensive behavioral outcome verification than a structurally complex structural redesign that affects a low-frequency coordination path.

---

## 8. Operational implications

Deployments implementing directed-selection-verification face several operational implications that follow from the architecture.

**Verification runs after each directed selection event, not periodically.** Because a directed selection event modifies the DNA governing cell-level behavior, the window between modification and verification is a period in which the deployment is operating under DNA whose architectural properties are unconfirmed. Running verification after each event rather than periodically closes that window.

**Verification results inform whether directed selection achieved its governance objectives.** Behavioral outcome verification (Dimension 4) confirms determinism and reproducibility, not improvement quality. Governance's judgment about whether the directed selection event achieved its intended improvement is a separate question, informed by operational evidence accumulated in the Action layer. The verification gate confirms architectural soundness; operational improvement assessment is a governance activity that follows from accumulated action evidence and may itself inform further directed selection.

**Failed verification may trigger rollback per B2.69 or further directed selection.** If any dimension fails, the directed selection event is not complete as an architectural event. The B2.69 version management commitment means the prior DNA version is preserved and accessible. Rollback to the prior version restores the deployment to a state whose architectural properties were previously confirmed. Alternatively, the failure may indicate that the modification was correctly authorized and structurally correct but produced unexpected behavioral effects, in which case further directed selection targeting those behavioral effects may be the appropriate response.

**Verification results are recorded per A2.40.** The outcome of directed-selection-verification — which dimensions were applied, which passed, which failed, and what corrective action was taken — is itself a substrate event that requires provenance per A2.40. This record is what allows governance to review the verification history for a given DNA scope and to identify patterns of verification failure that may indicate systematic issues in the directed selection process.

**Cross-level verification ensures system-wide consistency.** A deployment that runs verification only at the level of the modification event without cross-level behavioral checks may miss behavioral disruptions at lower levels that propagate from the modification through expression. Cross-level verification is the mechanism by which the three-level architecture's expression dynamics are confirmed to remain consistent after a directed selection event.

---

## 9. Limits of directed-selection-verification

Four limits bound what directed-selection-verification can and cannot do.

**Verification does not guarantee improvement quality.** The four-dimension gate confirms governance authorization, modification correctness, retroactivity compliance, and behavioral determinism. It does not confirm that the new DNA produces better governance outcomes than the prior DNA. Improvement quality is a governance judgment that depends on operational evidence — accumulated Action records, outcome measures, and the governance decision-makers' assessment — not on verification. A directed selection event can pass all four verification dimensions and still represent a poor governance choice.

**Verification does not prevent problematic DNA changes.** The verification gate is a post-modification confirmation. It does not operate as a pre-modification barrier that prevents problematic DNA changes from being applied. A DNA change that passes governance authorization (because the authoring human held valid authority) but produces poor behavioral outcomes will not be prevented by the verification gate; it will be detected through behavioral outcome verification (Dimension 4) after the modification is applied. The appropriate architectural response to detected behavioral failure is rollback per B2.69 or further directed selection, not a redesign of the verification gate to function as a pre-modification barrier.

**Behavioral outcome verification tests determinism and reproducibility, not behavioral quality.** A5.06 and A5.16 confirm that cell behavior under new DNA is architecturally sound in the sense the CKS pattern requires: deterministic, reproducible, and consistent with A1.10. They do not assess whether the behavior is appropriate for the governance domain, whether it reflects sound clinical judgment, or whether it produces good operational outcomes. Behavioral quality is a domain-specific assessment that lies outside what the Series A operational tests address.

**Verification is not a single test but an application of multiple Series A tests at appropriate scope.** The four-dimension gate is a structured sequence of Series A test applications, each targeting a different architectural property. No single test constitutes the verification gate alone; the gate requires all four dimensions to be confirmed. A deployment that runs A5.06 alone and calls the result "directed selection verification" is missing three dimensions and has not verified the directed selection event in the sense this note formalizes.

---

## 10. The architectural verification stated as a test

A directed selection event satisfies directed-selection-verification if and only if all of the following hold after the modification is applied:

1. The A5.04 rule authoring test confirms the change was authored by a human holding A2.47 authority for the modified DNA scope, and the A2.40 authorization record is present and complete.
2. The A5.10 source-of-truth five-categories test confirms the new DNA content correctly occupies Category 4 and the change matches the authorized specification without unintended additions or omissions.
3. The A6.02 retroactivity treatment confirms the new DNA applies forward from its modification timestamp, the prior version is preserved per B2.69, and A2.40 provenance field 4 in existing Action records references the correct DNA version for their governing period.
4. The A5.06 cell-behavior-determinism test and A5.16 reproducibility test confirm cell behavior under the new DNA satisfies A1.10 determinism and replays deterministically.
5. A5.08 and A5.09 supplementary checks confirm provenance completeness and four-accountability-question accountability for the modification event.
6. Cross-level verification confirms no unexpected behavioral effects at levels not directly targeted by the modification.

Any directed selection event that does not satisfy all six conditions is architecturally incomplete and requires rollback per B2.69 or further directed selection before it can be treated as a resolved modification.

---

## 11. Naming, decomposition closure, and the progression to B2.73

Naming directed-selection-verification as a distinct operational variant matters for the same reasons that naming each of the six B1.14 decomposition notes mattered. Directed selection verification is not implicit in B1.14's directed-selection commitment; it is a specific operational shape that post-modification confirmation takes when directed selection is implemented within the CKS architecture. Without a named and formalized verification gate, the territory between "directed selection event completed" and "directed selection event architecturally confirmed" is unoccupied prior art, available for any party to claim as novel. With B2.72, that territory is occupied.

The six-note B1.14 decomposition is now complete. B2.67 established directed selection scope: which DNA may be modified, by whom, under what delegation, and what DNA scope means across levels. B2.68 established DNA modification governance: the authority architecture under which directed selection events are initiated, proposed, authorized, and rejected. B2.69 established DNA version management: how version records are created, preserved, and referenced so that the temporal structure of DNA modifications is auditable. B2.70 established retroactivity treatment: the forward-only application rule and the prohibition on retroactive rewriting of prior Action records. B2.71 established directed selection evolution patterns: the three patterns (incremental improvement, structural redesign, multi-level coordination) characterizing different directed selection events and their governance implications. B2.72 (this note) established directed selection verification: the four-dimension post-modification gate that confirms governance authorization, DNA change correctness, retroactivity compliance, and behavioral soundness.

The decomposition cycle for directed selection is complete: scope → governance → versioning → retroactivity → patterns → verification. Each note covers a distinct architectural property that directed selection must satisfy; together, the six notes formalize the full operational architecture of directed selection events within CKS.

Phase B2 continues with B2.73, which begins the B1.15 action-feedback decomposition. Action-feedback evolution, as Paper 2 specifies, closes the loop from accumulated Action-layer evidence back into governed DNA refinement. The B1.15 decomposition will develop the sub-components of that loop — how action evidence is accumulated, how it informs DNA change proposals, how proposals are authorized, and how the feedback mechanism interacts with the directed-selection governance machinery B2.67–B2.72 has now fully formalized — as the same operational-variant-as-architectural-decomposition logic that has governed all of Phase B2.

---

*This note is B2.72 in the Phase B2 derivation series. It is the seventy-second Phase B2 note and the sixth and closing note of the B1.14 directed-selection decomposition (B2.67–B2.72). The prior notes in this decomposition are: B2.67 (directed selection scope), B2.68 (DNA modification governance), B2.69 (DNA version management), B2.70 (retroactivity treatment), and B2.71 (directed selection evolution patterns). The subsequent note, B2.73, begins the B1.15 action-feedback decomposition.*
