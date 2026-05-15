# Additional Composition Pair: Governance Health Indicators and Post-Mortem Review

**Series D — Defensive Publication Derivation Note D4.26 (#631)**
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Two operational commitments in the CKS governance architecture — Governance Health Indicators (D2.35) and Post-Mortem Governance Review (D2.39) — are typically described and implemented in isolation. Governance Health Indicators provide six continuous signals (H1–H6) for assessing governance quality in real time and between Full Aspect Integration (FAI) events. Post-Mortem Governance Review provides structured retrospective assessment after FAI event completion, producing improvement records and feeding those improvements back into governance architecture. When both commitments operate simultaneously, three governance requirements emerge that are not apparent from either commitment individually: a forward-to-backward temporal connection that validates indicator accuracy against governance reality; a calibration feedback loop that keeps health indicators accurate as governance patterns evolve; and a warning-triggered post-mortem scheduling requirement that converts sustained indicator warnings into governance action. This note identifies and formalizes those three requirements as prior art.

---

## 1. Pair Identification

**Commitment A — Governance Health Indicators (D2.35):** Six continuous signals, designated H1 through H6, that provide real-time and between-event assessment of FAI governance quality. Each signal monitors a distinct dimension of governance health. Indicators can show green (within normal range), yellow (approaching threshold), or red (threshold exceeded, warning active). The indicators operate continuously across the full governance cycle — before, during, and after FAI events — and are designed to surface potential governance quality problems early enough for intervention.

**Commitment B — Post-Mortem Governance Review (D2.39):** Structured retrospective review conducted after FAI event completion. The review examines what actually happened during governance execution, produces a governance improvement record, and feeds identified improvements back into governance architecture — updating configuration content, orchestration rules, or governance practice. Post-mortem review is episodic rather than continuous: it activates at defined trigger points (typically after event completion) and produces discrete outputs rather than running signals.

These two commitments address governance quality monitoring at different temporal registers: health indicators provide continuous forward-looking signals; post-mortems provide episodic backward-looking validation. Organizations that implement both simultaneously encounter governance requirements that neither commitment alone generates.

---

## 2. The Governance Scenario Requiring Both Simultaneously

An organization has deployed both commitments. Governance health indicators run continuously across all active governance perimeters, surfacing H1–H6 signals for each FAI event in progress and between events. Post-mortem reviews are scheduled and conducted after each event's governance cycle closes, producing improvement records that feed back into architecture.

In this deployment, both commitments are in effect at the same time. During an FAI event, health indicators are producing signals — some green, some yellow, perhaps some red. After the event completes, a post-mortem reviews what governance quality actually was. The post-mortem team can now look backward at what the health indicators showed during the event and compare that to what the post-mortem reveals about actual governance quality.

This comparison is not incidental. It is structurally required by the composition. Once both commitments are present, the question of whether the health indicators correctly signaled what the post-mortem reveals becomes a first-class governance question. The governance requirements that follow are not optional enhancements — they are what coherent simultaneous operation of the two commitments demands.

---

## 3. Non-Obvious Governance Requirements from the Combination

### Requirement 1 — Forward-to-Backward Temporal Connection

Health indicators are forward-looking: they alert governance practitioners to potential problems during and between events, before those problems have been fully realized or fully understood. Post-mortems are backward-looking: they assess what governance quality actually was, after enough time has passed for the event to complete and its governance record to be reviewed.

These two temporal orientations are not naturally connected. An organization can run health indicators that never inform post-mortem analysis, and conduct post-mortems that never evaluate health indicator accuracy. When both commitments operate in isolation, the forward signals and the backward findings accumulate in separate governance records with no structural link between them.

The composition requires closing this loop. Post-mortem records must explicitly evaluate whether the health indicators correctly predicted the governance quality the post-mortem reveals. If indicators showed green throughout an event and the post-mortem reveals significant governance problems, a calibration gap exists: the forward signals failed to detect something real. If indicators showed sustained red and the post-mortem reveals no problems, a false-positive calibration gap exists: the forward signals produced false alarms that, if acted upon, would have consumed governance attention unnecessarily.

Without this connection, health indicators are signals of unknown accuracy. Practitioners using them cannot know whether to trust a green reading, how seriously to treat a yellow reading, or whether a red reading indicates a real problem or instrument error. The forward-to-backward connection is what converts health indicators from signals into calibrated instruments. The post-mortem is the only moment at which the actual governance quality of a completed event is systematically assessed; it is therefore the only moment at which health indicator accuracy can be validated against governance reality.

### Requirement 2 — Calibration Feedback Loop from Post-Mortem to Health Indicators

Even if post-mortem records include explicit evaluation of health indicator signals, a second requirement follows: the findings of that evaluation must feed back into the health indicator specifications themselves.

Health indicators defined at system initialization reflect the governance patterns and failure modes that were understood at that time. Governance patterns evolve. New FAI configurations introduce coordination dimensions that the original indicator set did not anticipate. Governance failures occur in forms that the original six signals were not designed to detect. An indicator set that is never updated against post-mortem findings becomes less accurate over time — not because anything in the indicator design fails, but because governance reality has moved while the indicators have stayed fixed.

The calibration feedback loop operates as follows. After each post-mortem, governance practitioners review whether any governance quality problem identified in the post-mortem was signaled in advance by any health indicator. If the post-mortem identifies a problem that no indicator flagged, that problem represents a coverage gap in the indicator set. If a specific H-signal consistently fails to distinguish between events where a particular problem appears and events where it does not, that signal requires recalibration — its threshold, its measurement definition, or its scope may need revision.

This feedback loop is a quality-assurance mechanism for the monitoring system itself. It is the mechanism by which a governance organization learns whether its monitoring infrastructure is tracking the dimensions of governance quality that actually matter. Without the feedback loop, an organization has no systematic method for distinguishing between "our health indicators show green because governance quality is good" and "our health indicators show green because we are not measuring the dimensions on which governance quality is failing." The calibration feedback loop is what makes the difference between those two states knowable.

### Requirement 3 — Warning-Triggered Post-Mortem Scheduling

The third requirement follows from what health indicators are for. Health indicators are an early-warning system: they exist to surface potential governance problems while intervention is still possible. A warning signal — a health indicator in the red zone, or a pattern of sustained yellow readings across multiple indicators — is governance-actionable information. It means the monitoring system has detected something that warrants investigation.

If warning signals are observed but generate no governance response, the monitoring system has failed its purpose. Worse: if a sustained warning is observed, no post-mortem is triggered, and a subsequent scheduled post-mortem later reveals that the warning correctly signaled a real governance problem that was allowed to persist, the governance failure is compounded. The organization had warning, did not act, and can trace the failure of action directly to the absence of a warning-response protocol.

The composition requirement is structural: health indicator threshold specifications must include a post-mortem trigger criterion. When an indicator crosses its warning threshold and remains in the warning zone for a defined duration, an unscheduled post-mortem review is triggered. The trigger criterion belongs in the threshold specification — not as a separate procedural document, not as an informal escalation practice — because the threshold specification is what governs indicator-driven governance action. A threshold specification that defines when an indicator is in warning mode but does not specify what governance action follows is incomplete.

This requirement makes the monitoring system actionable rather than observational. Health indicators without a warning-triggered response mechanism are governance theater at the monitoring level: the infrastructure of monitoring is present, but the connection between monitoring and action is absent. The connection is what the threshold-level post-mortem trigger criterion provides.

---

## 4. Prior-Art Significance

The three requirements formalized above — forward-to-backward temporal connection, calibration feedback loop, and warning-triggered post-mortem scheduling — are specific governance properties of the composition of D2.35 and D2.39. They are not present in either commitment individually, and they are not derivable from general descriptions of "governance monitoring" or "periodic governance review" without specifying both commitments simultaneously.

Prior art significance follows in three directions. First, any governance monitoring architecture that combines continuous health indicators with episodic post-mortem review must address these three requirements. A system that provides health indicators without post-mortem-based calibration feedback, or that provides post-mortem review without explicit evaluation of health indicator accuracy, or that provides health indicator warnings without a post-mortem trigger criterion, fails to instantiate the composition in its complete form. The requirements function as completeness conditions for the composition.

Second, the calibration feedback loop establishes that health indicators are not static governance artifacts. They are components of a living governance monitoring system that is itself subject to governance. This is a non-obvious design implication: the governance monitoring system must be designed with the expectation that indicator specifications will be revised over time, and the revision process must be driven by structured post-mortem evidence rather than informal practitioner judgment. Governance quality monitoring has an improvement cycle that mirrors the improvement cycle post-mortems create for governance architecture more broadly.

Third, the warning-triggered post-mortem scheduling requirement establishes a formal connection between the monitoring layer and the review layer of governance architecture. These layers are commonly designed as parallel but independent governance mechanisms. The composition requires them to be coupled: the monitoring layer must be able to schedule the review layer, and the review layer must feed back into the monitoring layer's calibration. The bidirectional coupling is what distinguishes a composed governance monitoring system from two governance mechanisms operating in parallel.

---

## 5. Operational Test

For a governance monitoring system implementing both Governance Health Indicators (D2.35) and Post-Mortem Governance Review (D2.39) simultaneously, an independent observer can assess whether the composition is fully instantiated by verifying the following:

**(a) Post-mortem records include explicit validation of health indicator signals.** Each post-mortem record contains a section that identifies the health indicator signals that were active during the reviewed event and evaluates whether those signals accurately predicted the governance quality the post-mortem found. Records that review governance outcomes without referencing indicator signals, or that reference indicator signals without evaluating their predictive accuracy, do not satisfy this criterion.

**(b) Health indicator calibration records reference post-mortem findings.** The specification records for H1–H6 — which define what each indicator measures, what constitutes a warning threshold, and what revision history the indicator carries — reference specific post-mortem findings as the basis for any threshold or scope revisions. Indicator specifications that have never been revised, or that carry revisions without documented post-mortem evidence, indicate that the calibration feedback loop is absent.

**(c) Health indicator threshold specifications include a post-mortem trigger criterion.** The threshold specification for each indicator — or for the indicator set as a system — includes an explicit criterion specifying that sustained warning signals trigger an unscheduled post-mortem review. Threshold specifications that define warning levels without specifying the governance action those warning levels mandate do not satisfy this criterion.

A governance monitoring system that passes all three checks has instantiated the composition. A system that fails any check has a partial instantiation in which the two commitments operate but do not compose. The gap between partial and full instantiation is not cosmetic: each failed check corresponds to a governance failure mode — uncalibrated signals, a degrading monitoring system, or warnings that do not produce governance action — that the composition is designed to prevent.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Additional Composition Pair: Governance Health Indicators and Post-Mortem Review.* Defensive Publication Derivation Note D4.26 (#631), May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
