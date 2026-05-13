# Ongoing Governance Test Suite — The Periodic Test Battery Governance Runs During Normal Deployment Operation to Confirm the Paper 2 Architecture Remains Sound Through Evolution, Entity Population Changes, and Action Layer Evidence Accumulation

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

A CKS deployment that passes initialization testing has demonstrated that its architecture is correctly configured: evolution mechanisms are in place, DNA layers are populated, lifecycle governance is wired, and the instinct/reasoning separation is sound at the moment of launch. But correct configuration at initialization does not guarantee that the architecture continues to operate as designed as the deployment matures. Entity populations change through births, matings, and deaths. DNA specifications evolve through directed selection. Action layer evidence accumulates. LLM versions may be upgraded. Each of these developments provides new surface for architectural degradation if governance is not exercised concurrently. This note formalizes the ongoing governance test suite — the periodic test battery governance runs during normal deployment operation — as a six-stage workflow: entity population health check, DNA specification health check, evolution mechanism exercise verification, instinct/reasoning separation maintenance check, ongoing anti-pattern scan, and review recording with cadence maintenance. The central distinction that makes ongoing testing architecturally distinct from initialization testing is the configuration-versus-exercise distinction: initialization tests ask whether mechanisms are configured; ongoing tests ask whether configured mechanisms have been exercised. A deployment whose mechanisms are configured but never exercised is developing Evolution Stasis (B3.24), and the ongoing test suite is the governance instrument that detects it before it becomes entrenched.

## 1. Why ongoing testing is architecturally distinct from initialization testing

An initialization test suite (B5.10) establishes a baseline: at launch, the deployment's architecture satisfies the commitments the source paper specifies. It answers configuration questions. Are the three architectural levels present? Is the instinct/reasoning separation sound? Are evolution mechanisms wired? Are lifecycle governance procedures in place? Passing initialization means: *the architecture is correctly set up.*

Ongoing testing asks a different question. As time passes and the deployment operates, it asks: *is the architecture continuing to operate as designed?* The two questions are distinct because correct configuration does not entail continued operation. A deployment can be perfectly initialized and then fail to exercise any of its configured mechanisms. Directed selection can be authorized without ever being used. The action-feedback pipeline can be wired without ever generating a proposal. Mutation events can be processed without triggering verification gates. In each case, the mechanism is configured but dormant — and dormancy is itself an architectural signal, not a neutral absence of activity.

The source paper's three evolution mechanisms — instinct evolution, DNA evolution, and action-feedback evolution — are designed to operate in productive tension (§8, Paper 2). When only one mechanism operates, or when none do, the tension collapses. Single-Mechanism Evolution (B3.13) and Evolution Stasis (B3.24) are both failure modes that develop over time, not at initialization. They are detectable only by tests that examine the deployment's operational record across a review period — which is precisely what the ongoing test suite provides.

Three additional developments distinguish the ongoing context from the initialization baseline. First, entity populations change: entities born since initialization need complete birth records; entities that have died need governed retirement records; entities whose functions have shifted significantly may need updated level determinations. Second, DNA specifications evolve: modifications made since initialization need authorization records; content-domain boundaries may have drifted from stated operational territory. Third, action layer evidence accumulates: the proposing substrate should be drawing on this accumulation to generate DNA refinement proposals; failure to do so signals Evidence Blindness (B3.28).

The ongoing test suite is structured as six stages. Stages 1 through 5 perform the substantive architectural checks; Stage 6 records results, documents triggered governance decisions, and schedules the next review.

## 2. Stage 1 — Entity population health check

The entity population health check confirms that the three-level entity structure remains sound and that lifecycle governance has been applied correctly to every entity event since the last review. Four sub-checks compose this stage.

**Sub-check 1a — Entity inventory reconciliation.** The live entity count in the substrate should equal the total entity birth count minus the total entity death count. This arithmetic test is the most efficient ongoing population check available: it does not require inspecting every entity, only the three tallies. A positive discrepancy — more live entities than births-minus-deaths accounts for — signals ungoverned births: entities that came into existence without governance records, violating the lifecycle governance commitment (B2.44). A negative discrepancy — fewer live entities than expected — signals silent deaths: entities retired or removed without governed death records. Either direction triggers lifecycle anti-pattern detection (B3.10, B3.11). When the count balances, the inventory is coherent and per-entity inspection is not required to establish population integrity.

**Sub-check 1b — New entity verification.** For any entities born since the last review, governance confirms that complete birth records exist per the birth governance commitment (B2.44): authorized origination decision, level determination at birth, initial DNA specification populated, governance record with provenance. An entity present in the substrate without a birth record is an ungoverned birth regardless of whether the inventory count balances — birth records and count reconciliation are independent checks.

**Sub-check 1c — Level determination currency.** Any entity whose function has changed significantly since its last level determination review is a candidate for the evolution-triggered role change assessment (B2.87). The three architectural levels — cell, aspect, and Self — are not permanent assignments; they reflect current functional role. An entity whose operational scope has grown to encompass coordinating multiple cells should be assessed for level promotion; an entity whose scope has narrowed should be assessed for level demotion. Stale level determinations produce structural incoherence in the three-level architecture even when the entity count is correct.

**Sub-check 1d — Three-level structure integrity.** All three architectural levels must remain instantiated. A deployment in which one level has been entirely emptied — through deaths, restructuring, or failure to instantiate new entities at a vacated level — no longer satisfies the three-level structural commitment (B2.03). The Intrinsic Type Assignment anti-pattern (B3.18) is the relevant signal when level determinations appear to have been assigned by convenience rather than by genuine functional assessment.

Stage 1 signal summary: lifecycle anti-patterns (B3.10, B3.11) if count discrepancy; Intrinsic Type Assignment (B3.18) if level determinations are stale or structurally unsound.

## 3. Stage 2 — DNA specification health check

The DNA specification health check confirms that the DNA layer remains coherent, that all modifications since the last review were authorized and recorded, and that the deployment's operational territory remains governed by current specifications.

**Sub-check 2a — Directed selection governance audit.** All DNA modifications made since the last review must have authorization records, governance decision records, and retroactivity-compliance documentation per the directed selection governance commitment (B2.72). Retroactivity compliance means that if a DNA modification changes the standing instruction under which prior actions were taken, the modification's governance record acknowledges this scope. The audit covers the full review period: modifications without records, regardless of apparent intent, constitute Ungoverned DNA Modification (B3.15).

**Sub-check 2b — DNA coherence spot-check.** A random sample of entities is selected and their DNA specifications examined for internal contradiction: conflicting orchestration rules, schema incompatibilities between aspects sharing a cell, or specification content that contradicts the entity's stated operational domain. The spot-check does not inspect every entity's DNA at every review; it provides early detection sensitivity for Specification Integrity Collapse (B3.30), which characteristically develops through incremental contradictions that individually appear minor. Sample size should scale with entity population size and elapsed time since last review.

**Sub-check 2c — Content-domain currency.** Each entity's DNA layer specifies the operational territory within which the entity's action layer evidence is meaningful. If action layer evidence shows systematic processing outside the stated domain — tasks executed that fall outside the entity's specified content domain — the entity's content-domain specification has drifted from operational reality (B2.91). Governance decides whether to expand the stated domain to match actual practice, constrain actual practice to match the stated domain, or create a new entity for the out-of-domain processing.

**Sub-check 2d — Conflict registry review.** Any conflicts recorded in the A1.03 conflict registry that remain unresolved from prior reviews require directed selection attention. Aging unresolved conflicts are a signal that the directed selection mechanism is configured but not being applied to its highest-value targets. Resolution decisions belong to governance authority, not to the ongoing test suite itself — but the test suite surfaces the outstanding resolution obligations.

Stage 2 signal summary: Specification Integrity Collapse (B3.30) if coherence failures detected; Ungoverned DNA Modification (B3.15) if modifications lack governance records.

## 4. Stage 3 — Evolution mechanism exercise verification

Stage 3 is the stage most distinctive to the ongoing test suite. Where initialization tests asked whether evolution mechanisms are configured, ongoing tests ask whether configured mechanisms have been exercised since the last review. The productive tension among the three mechanisms (§8, Paper 2) requires all three to remain active; dominance of one mechanism, or dormancy across all, signals architectural degradation.

**Sub-check 3a — Mutation event exercise.** Have any LLM version changes or infrastructure upgrades occurred since the last review? If so, were they processed through full mutation governance, including verification substrates determining which prior reasoning can be retired, retained as fallback, or retained as active verification on safety-critical paths (B2.66)? A mutation event processed without verification gate exercise constitutes Ungoverned Mutation (B3.14). A deployment that has experienced LLM upgrades without mutation governance records has let instinct evolution proceed outside its governance shape.

**Sub-check 3b — Directed selection event exercise.** Have any DNA improvements been made through the authorized directed selection governance process (B2.72) since the last review? If the DNA layer has remained entirely static across the review period in a mature deployment, directed selection is configured but dormant — a contribution to Evolution Stasis (B3.24). Governance should assess whether dormancy is appropriate to the review period's circumstances or whether it signals that the directed selection process is not functioning as intended.

**Sub-check 3c — Action-feedback cycle exercise.** For mature deployments, at least one complete action-feedback pipeline execution should have occurred since the last review: action layer evidence accumulated, evidence processed by the proposing substrate, at least one proposal generated for governance consideration (B2.76). The test does not require that proposals have been accepted — rejection under governance is a legitimate outcome. It requires that the pipeline has executed, closing the loop from accumulated evidence back to governed DNA consideration. A pipeline that never generates proposals, despite growing action layer evidence, signals Evidence Blindness (B3.28).

**Sub-check 3d — Bidirectional evolution scope.** Have any horizontal evolution events (peer propagation of DNA improvements across entities at the same level) or vertical evolution events (propagation up or down the three-level hierarchy) occurred since the last review (B2.79, B2.80)? Single-mechanism evolution — where only one of the three mechanisms is active across the review period — is the signal for Single-Mechanism Evolution (B3.13), which represents loss of the productive tension the source paper's architecture requires.

Stage 3 signal summary: Evolution Stasis (B3.24) if no mechanism activity detected across the review period; Single-Mechanism Evolution (B3.13) if only one mechanism has been active; Evidence Blindness (B3.28) if action-feedback pipeline has not generated proposals despite accumulated action layer evidence; Ungoverned Mutation (B3.14) if mutation events were not processed through verification gates.

## 5. Stage 4 — Instinct/reasoning separation maintenance check

The instinct/reasoning separation is the architectural commitment that makes CKS inference deterministic and its governance meaningful: instinct layer handles what it handles reliably, and reasoning layer handles what requires substrate-mediated deliberation. Evolution can erode this separation if not actively maintained.

**Sub-check 4a — Reproducibility spot-check on evolved cells.** Any cells whose DNA has been modified through directed selection since the last review are candidates for the reproducibility check (A5.16): given the same substrate state and orchestration rules, does the cell produce equivalent outputs? DNA evolution that introduces non-determinism into cells previously deterministic violates the determinism contract (B2.12) and signals Instinct-Reasoning Collapse (B3.02). The spot-check need not cover all cells at every review — cells that have not evolved since the last check are not candidates. It covers cells that have evolved.

**Sub-check 4b — Verification gate freshness.** For any mutation events that occurred since the last review, confirm that verification gates were exercised at the time of the mutation event per the mutation governance commitment (B2.06). Verification gate records should exist in the substrate; their absence signals that instinct evolution was processed without the governance shape designed for it. Retroactive verification gate application is not equivalent to contemporaneous application — the governance record should reflect the verification gate's role in the integration decision, not a post-hoc check appended later.

**Sub-check 4c — High-stakes pinning currency.** Operational experience since initialization may have identified decision classes that warrant pinning — explicit substrate decisions that the reasoning layer must use rather than re-derive on each execution (B2.05). Any high-stakes decision patterns that have emerged in the action layer since the last review and that lack pinning records should be assessed for whether pinning is appropriate. Unpinned high-stakes decisions are not necessarily a violation, but they are a governance attention signal: the ongoing test surfaces them for human assessment.

Stage 4 signal summary: Instinct-Reasoning Collapse (B3.02) if separation has degraded through evolution; Ungoverned Mutation (B3.14) if mutation events bypassed verification gates.

## 6. Stage 5 — Ongoing anti-pattern scan

Four anti-patterns develop characteristically over time rather than at initialization. The ongoing anti-pattern scan examines the deployment's record for their signatures.

**Governance Theater** develops when governance records are created retroactively or formulaically, producing provenance records that satisfy the formal requirement but do not reflect genuine governance exercise. The operational signature is provenance timing: governance records created contemporaneously with governed events have distinct provenance timestamps and decision-content density compared to records created in bulk after the fact. The ongoing scan examines governance record density distribution across the review period — clustering in time (many records created in a short window, widely separated from the events they purport to govern) is the primary signal.

**Evidence Blindness** develops when action layer evidence accumulates without driving proposing substrate activity. The operational signature is the ratio of action layer growth to proposal generation: a deployment whose action layer has grown substantially since the last review but whose proposing substrate has generated no proposals has decoupled evidence accumulation from evolution — precisely the failure mode the action-feedback mechanism exists to prevent. Action layer volume and proposal record volume are both substrate-observable quantities.

**Specification Integrity Collapse** develops through incremental DNA contradictions that individually pass governance review. The operational signature is DNA volume growth outpacing coherence governance: as specifications accumulate refinements, the surface area for internal contradiction grows. The spot-check in Stage 2 provides early detection; the ongoing scan monitors the trend. Governance cadence should increase when DNA volume growth accelerates.

**Authority Ambiguity** develops when governance acts are taken by parties whose authority is not clearly established under the A2.47 authority distribution. The ongoing scan reviews governance records from the review period for acts taken outside established authority scope — not to invalidate prior decisions retrospectively, but to identify authority gaps that need explicit resolution before they produce genuine conflicts. Any governance act that could not be unambiguously attributed to an established authority scope at the time it was taken belongs in the conflict registry pending authority clarification.

## 7. Stage 6 — Review recording and governance cadence

The ongoing governance review concludes with recording and scheduling.

**Recording (B2.40).** The results of all five substantive stages are recorded in the substrate as governance review content: which checks were run, what was found, which signals were triggered, and which governance decisions were made or initiated as a result. The review record itself is substrate content with provenance — the review record's timestamp, the reviewer, and the scope covered are all recorded fields. A governance review that is not recorded has occurred but has not been governed.

**Governance decisions triggered by review findings.** Any signals raised in Stages 1 through 5 that require governance response — lifecycle anti-pattern remediation, DNA modification retroactivity resolution, Evolution Stasis response, verification gate backfill, authority ambiguity resolution — are recorded as open governance obligations with attribution and target resolution date. The ongoing test suite surfaces obligations; it does not resolve them. Resolution belongs to the governance processes the source paper specifies for each mechanism.

**Next review scheduling (governance cadence maintenance).** The most important output of any governance review is the scheduling of the next one. Cadence should be calibrated to deployment activity: a deployment processing frequent mutation events, active directed selection, and high action layer growth rate requires more frequent reviews than a stable deployment in a steady operational period. The unconditional minimum is one review at every significant evolution event or event batch — a mutation event, a directed selection cycle, a major lifecycle event (multiple births, a mating, a death). A deployment that completes a significant evolution event without scheduling the next governance review has let cadence drift. Cadence drift is itself the early-stage signature of Evolution Stasis: governance that does not keep pace with evolution cannot detect when evolution stops.

## 8. Conclusion

The ongoing governance test suite and the initialization test suite address the same architecture but from different vantage points. Initialization testing establishes that the architecture is correctly configured at launch. Ongoing testing confirms that the architecture continues to operate as designed as the deployment matures. The distinction is the configuration-versus-exercise distinction: mechanisms can be configured without being exercised, and the gap between configuration and exercise is where Evolution Stasis, Single-Mechanism Evolution, and Evidence Blindness develop.

The six-stage structure of the ongoing test suite reflects the six surfaces on which architectural degradation manifests over time: entity population integrity (Stage 1), DNA specification coherence (Stage 2), evolution mechanism exercise (Stage 3), instinct/reasoning separation maintenance (Stage 4), time-developing anti-pattern detection (Stage 5), and governance cadence maintenance (Stage 6). A deployment that runs the ongoing test suite at appropriate intervals and responds to its signals is a deployment that governs its own architectural health — which is the operational expression of the human-governed commitment the source paper places at the center of the CKS pattern.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Ongoing Governance Test Suite — The Periodic Test Battery Governance Runs During Normal Deployment Operation to Confirm the Paper 2 Architecture Remains Sound Through Evolution, Entity Population Changes, and Action Layer Evidence Accumulation.* May 13, 2026. ORCID: 0009-0004-8065-3235.
