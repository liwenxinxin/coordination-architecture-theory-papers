# Boundary Case: Action-Feedback at Evidence Scale — Governance Implications When the Action Layer Has Accumulated Massive Operational Evidence, Testing Whether Proposing Substrates Can Still Surface Useful Improvement Signals and How Evidence Retention, Staleness, and Scale Affect Action-Feedback Quality

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The action-feedback evolution mechanism commits to closing the loop from recorded action-layer evidence back into governed DNA refinement. This derivation note formalizes the boundary case that arises when a mature deployment has accumulated very large volumes of action-layer operational records — millions or more — and tests whether the action-feedback architecture remains effective at evidence scale. Three architectural boundaries are tested: whether proposing substrates can surface useful improvement signals from very large evidence pools; whether evidence staleness from prior DNA versions contaminates current-version proposals; and whether evidence retention governance remains coherent as the action layer grows without bound. The note introduces the evidence-tiering resolution — dividing action-layer records into active evidence (current DNA-version scope, used by proposing substrates for improvement proposals) and archived evidence (older records, preserved exclusively for A1.07 retraceability) — and establishes that tier boundaries are governed substrate content per A2.04. The note also identifies the paradoxical Evidence Blindness (B3.28) risk that develops through evidence overload rather than absence, and distinguishes the retraceability commitment from the evidence-scoping commitment that governs proposal quality.

---

## 1. Overview

The action-feedback evolution mechanism, as committed in Paper 2 (§7.2, §8), records action-layer operational experience and governs the loop from that experience back into DNA refinement. The mechanism is expected to accumulate evidence: every cell execution under every DNA version contributes to the action layer, and accumulation is architectural, not incidental. Over the lifetime of a mature deployment, the action layer per B2.26 may grow to contain millions or billions of operational records spanning multiple DNA versions — each version reflecting behavioral configurations shaped by prior directed-selection events.

This growth is expected and governed. The architecture commits to the action layer as persistent substrate content, with A1.07 retraceability requiring that records remain accessible for governance audit. What the architecture does not specify — and what this boundary case formalizes — is how proposing substrates per B2.74 should evaluate a very large evidence pool when producing improvement proposals, and how governance should manage the tension between unlimited evidence accumulation (required for retraceability) and evidence scoping (required for proposal quality).

The boundary case tests whether action-feedback evolution degrades as the evidence pool grows very large, or whether the architecture supports evidence governance mechanisms that preserve proposal quality at scale.

---

## 2. Configuration Description

The deployment configuration for this boundary case is a mature system in which cells have operated continuously for an extended period. The Action layer per B2.26 contains very large volumes of operational records — millions or more, spanning multiple DNA versions. Records from prior DNA versions reflect behavioral patterns under orchestration rules and substrate configurations that may have been substantially revised through subsequent directed-selection events.

Proposing substrates per B2.74 are authored substrate content per A2.04 — not autonomous agents but human-governed specifications of how evidence should be evaluated and what proposal criteria apply. Stage 1 governance per B2.75 receives proposals from proposing substrates and exercises authority over whether proposed DNA changes are accepted.

All action-feedback commitments per B1.15 hold in this configuration. The boundary being tested is not whether these commitments apply — they do — but whether proposing substrate architecture and evidence governance can be specified in ways that remain effective at evidence scale.

---

## 3. Architectural Boundaries Tested

Three architectural boundaries are tested by this configuration.

**B2.73 action evidence evaluation at scale.** The source paper commits that action-feedback proposals are produced by proposing substrates evaluating action-layer evidence. At small evidence scales, a proposing substrate that evaluates all available records may produce useful signals without explicit evidence-window design. At very large evidence scales, the same approach degrades: the signal-to-noise ratio of a full-history evaluation worsens as old patterns accumulate weight alongside current ones, and evaluating millions of records makes governance-review timelines impractical. The boundary tests whether proposing substrate specification must include explicit evidence-window design to remain effective, and whether that design requirement is a governance obligation per A2.04.

**Evidence staleness from prior DNA versions.** Each directed-selection event produces a new DNA version whose behavioral configuration may differ substantially from prior versions. Action-layer records accumulated under prior versions record how cells behaved under rules that have since been revised; the patterns they reveal may be irrelevant or actively misleading about current behavior. The A6.02 retroactivity principle means governance authority applies forward from its exercise; it does not retroactively update the evidential meaning of records generated under prior configurations. The boundary tests whether proposing substrates must scope their evidence evaluation to current-DNA-version records in order to produce proposals relevant to current behavior.

**B2.26 action-layer retention governance.** The architecture requires that action-layer records be maintained as persistent substrate content. A1.07 retraceability requires that records remain accessible for compliance audit — the causal path from any current substrate state to its antecedents must be reconstructable from substrate content alone, and old action-layer records form part of that antecedent chain. The boundary tests whether the architecture supports a principled distinction between evidence retention (required for A1.07) and evidence use (governed for proposal quality), and whether this distinction must be made explicit as governed substrate content per A2.04.

---

## 4. Governance Implications

The governance implications of this boundary case organize around three design decisions that proposing substrate authors per A2.04 must address for action-feedback to remain effective at evidence scale.

**Evidence-window specification in proposing substrate authorship.** At evidence scale, proposing substrate specification must include explicit evidence-window design rather than implicitly evaluating all available records. Two evidence-window strategies are available to authors.

*Recency-weighted evidence* assigns greater evaluative weight to recent records than to old records, reflecting that recent behavior is more predictive of current behavior than behavior recorded under long-superseded configurations. Recency weighting does not exclude old records from evaluation; it attenuates their contribution relative to recent records. The weighting function is itself governed substrate content — authors specify the decay rate, the time horizon, and the weighting formula as part of the proposing substrate's specification under A2.04.

*DNA-version-scoped evidence* evaluates only records generated under the current DNA version, defined as records accumulated since the last directed-selection event. This is a harder scope boundary: it excludes pre-directed-selection records entirely from improvement proposal evaluation. DNA-version-scoping is appropriate when directed-selection events represent substantial behavioral reorganization and when pre-revision records are structurally non-comparable to current patterns. Both strategies are authoring decisions per A2.04; governance determines which applies in a given deployment.

**Evidence tiering as the resolution of the A1.07–proposal-quality tension.** The tension between A1.07 retraceability and action-feedback proposal quality is resolved through a two-tier evidence structure within the action layer.

*Active evidence* consists of records within the current evidence window as defined by the proposing substrate specification in effect. Active evidence is what proposing substrates evaluate when generating improvement proposals. Its boundaries are governed per A2.04 and are themselves substrate content — the specification of what counts as active evidence is authored, versioned, and subject to the three governance rights (inspect, modify, override) at all times.

*Archived evidence* consists of records outside the current evidence window — older records from prior DNA versions or beyond the recency-weighting horizon. Archived evidence is preserved in the action layer as required by A1.07: it remains accessible to compliance audit and governance review, and supports reconstructing the causal history of current substrate state from its antecedents. Archived evidence is not used by proposing substrates for improvement proposals.

The key architectural observation is that the two tiers satisfy different commitments through different access patterns over the same underlying substrate. A1.07 retraceability requires that archived evidence be accessible; it does not require that it be included in action-feedback evaluation. Action-feedback quality requires that proposing substrates evaluate evidence relevant to current behavior; it does not require that irrelevant records be purged. Evidence tiering satisfies both requirements without sacrifice to either.

**Governance of tier boundaries.** Evidence tier boundaries are governed substrate content, not fixed architectural constants. The boundary between active and archived evidence — defined by evidence-window specification, DNA-version scope, or recency-weighting horizon — is authored per A2.04, subject to revision as the deployment matures, and auditable as part of the governance trace. Governance decides when to update tier boundaries following directed-selection events, how to handle records at the boundary margin, and whether tier-boundary revisions require Stage 1 governance review per B2.75 before taking effect.

**Pattern detection at scale.** Within the active evidence pool, proposing substrates at evidence scale must use pattern-detection approaches that account for the statistical characteristics of large evidence pools. A pattern appearing in ten records may warrant a proposal at small evidence scale; the same pattern appearing in ten records out of a million may lie within normal operational variance. Proposing substrate specification per A2.04 should include statistical significance thresholds appropriate to active evidence pool size — thresholds that are themselves governed substrate content, revisable as the pool grows or as governance develops experience with the deployment's variance characteristics.

---

## 5. Boundary Tests

Four tests establish whether the action-feedback architecture is functioning appropriately at evidence scale.

**(a) Proposing substrates specify evidence windows.** A proposing substrate per B2.74 should contain explicit evidence-window specifications — either recency-weighting parameters, DNA-version scope boundaries, or both — authored per A2.04. A proposing substrate that implicitly evaluates all available action-layer records without evidence-window specification is not designed for evidence-scale operation and will produce proposals of degrading quality as evidence accumulates.

**(b) Stage 1 governance receives actionable proposals.** Stage 1 governance per B2.75 should receive improvement proposals that reflect current behavioral patterns under the current DNA version, not proposals generated from patterns in records from superseded configurations. A governance body receiving proposals it cannot trace to current active evidence, or proposals driven by ancient behavioral patterns no longer relevant to the deployment, cannot exercise meaningful authority over the action-feedback loop.

**(c) Evidence retention tiers are governed per A2.04.** The tier boundary between active and archived evidence should exist as authored substrate content — versioned and attributable. An action layer in which all records are implicitly treated as equally available for proposal evaluation, with no governed distinction between active and archived evidence, is operating without evidence-tier governance and is exposed to the evidence-overload stress point described in §6.

**(d) A1.07 retraceability compliance access remains functional.** Compliance audit operations that require reconstructing causal paths through old action-layer records should be able to access archived evidence without disruption. Evidence tiering must not be implemented as evidence purging: archived evidence must remain accessible, even while excluded from active-evidence evaluation pools. An action layer that satisfies proposal quality by purging old records rather than by tiering them fails A1.07 retraceability.

---

## 6. Stress Points

Two stress points threaten the action-feedback architecture under evidence-scale conditions.

**Evidence noise overwhelming signal — paradoxical Evidence Blindness (B3.28).** The canonical form of Evidence Blindness is a cell or aspect operating without sufficient action-layer records to generate meaningful proposals — evidence absence producing a blind improvement loop. This boundary case reveals a paradoxical form: Evidence Blindness (B3.28) can develop through evidence overload rather than absence. When proposing substrates evaluate the full action layer without evidence-window specification, records from prior DNA versions outnumber records from the current DNA version, because the deployment has been accumulating records longer than the current DNA version has been in effect. The behavioral patterns that appear most prominent in a full-history evaluation are therefore likely to be patterns from superseded configurations — patterns reflecting how cells behaved before governance intervened to improve them. These old patterns generate improvement proposals that, if accepted, would partially revert prior directed-selection improvements. Governance receiving and recognizing these proposals as spurious incurs overhead; governance accepting them produces behavioral regression. In either case, the signal that action-feedback is supposed to surface — evidence of patterns worth improving in the current configuration — is invisible beneath the noise of superseded evidence. More evidence, without evidence-window governance, produces worse proposals: the paradox of overload producing the same blindness as absence.

**Evidence governance debt.** If evidence tier governance is never established — if governance never authors evidence-window specifications per A2.04, never designates tier boundaries, and never specifies statistical significance thresholds for pattern detection — the action layer grows without bound and the proposing substrate specification gap widens with each new DNA version. Evidence governance debt accumulates in the same way technical debt accumulates: it does not produce immediate failure but degrades action-feedback effectiveness incrementally and compounds over time. A deployment that has operated for several years without evidence-tier governance has an action layer in which current-version records are a small minority of all records, directed-selection history has produced multiple DNA versions contributing undifferentiated records to the evaluation pool, and proposing substrates have no principled basis for distinguishing current from superseded behavioral evidence. Recovering from evidence governance debt requires retroactive tier-boundary authorship — deciding, for each prior directed-selection event, where the tier boundary should have been placed — whose cost grows with accumulated debt.

---

## 7. Architectural Limits

The action-feedback architecture at evidence scale imposes four limits that governance must accept as fixed constraints.

The architecture requires action-layer records per B2.26 for retraceability per A1.07. This means the architecture does not support evidence purging as a response to evidence scale; records required for compliance audit cannot be deleted even when outside the active evidence window. Evidence tiering is the only permissible architectural response to evidence scale that does not compromise retraceability.

The architecture does not specify maximum action-layer size or retention policies. Governance determines appropriate evidence tiering and retention — including whether archived evidence may be moved to cold storage for access-time management while remaining accessible per A1.07 — but these are governance decisions, not architectural constants. The boundary case formalizes the governance implications without resolving them to defaults.

The architecture requires that proposing substrates be authored substrate content per A2.04. Evidence-window specifications must be authored by humans exercising governance rights, not generated autonomously by cells or LLMs without governance authority over the specification. A proposing substrate that autonomously adjusts its own evidence window in response to evidence accumulation, without human authorship of the adjustment specification, violates the A2.04 authorship commitment.

The architecture does not specify what counts as "current" for evidence-window purposes. Whether "current" means post-last-directed-selection, a rolling time window, a record-count threshold, or a behavioral-change-magnitude criterion is a governance decision. The architecture commits to the evidence-tier structure and the A2.04 authorship requirement; it leaves the operational definition of currency to governance.

---

## 8. Conclusion

The action-feedback boundary case at evidence scale reveals that accumulation — which the architecture expects and the action layer commits to — becomes an architectural challenge when ungoverned at the evidence-evaluation layer. The action-feedback mechanism is designed to surface improvement signals from operational experience; at evidence scale, it can just as easily surface noise from superseded experience if proposing substrates lack evidence-window specification. The resolution is architectural but not automatic: evidence tiering, governed per A2.04, provides the structure within which action-feedback proposal quality is maintained across a deployment's operational lifetime. The paradoxical form of Evidence Blindness (B3.28) — blindness through overload rather than absence — is the stress point that evidence-tier governance specifically prevents.

The retraceability commitment per A1.07 and the action-feedback quality commitment per B1.15 are not in conflict; they satisfy different requirements through different access patterns over the same action layer. Governance is the architectural actor that maintains both: authoring evidence-window specifications that focus proposing substrates on current behavioral patterns, while preserving the full record for compliance and accountability purposes. Evidence governance debt is the consequence of not performing that authoring function as the deployment matures.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Boundary Case: Action-Feedback at Evidence Scale — Governance Implications When the Action Layer Has Accumulated Massive Operational Evidence, Testing Whether Proposing Substrates Can Still Surface Useful Improvement Signals and How Evidence Retention, Staleness, and Scale Affect Action-Feedback Quality.* CKS Derivation Notes, B6.11. May 13, 2026. ORCID: 0009-0004-8065-3235.
