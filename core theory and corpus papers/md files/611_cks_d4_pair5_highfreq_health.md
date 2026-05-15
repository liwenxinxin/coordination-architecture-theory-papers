# Composition Pair 5: High-Frequency Events and Governance Health Monitoring

**Derivation Note D4.06 — Series D, Phase D4 (Composition Pairs)**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Two governance commitments introduced in the CKS Paper 3 theory — high-frequency event governance infrastructure (D2.71) and the six-indicator governance health monitoring framework (D2.35) — interact in ways that produce three non-obvious architectural requirements when they are applied together. Frequency-adjusted health thresholds are the core non-obvious requirement: health indicators specified as absolute counts produce misleading signals at high event frequency, and the composition requires threshold calibration as frequency-relative ratios. Automated between-review monitoring is the second non-obvious requirement: D2.71's sampled post-mortem review creates gaps between reviews that, at high frequency, span many events, and D2.35's indicators must be monitored continuously in automated form to fill those gaps. Cadence scaling is the third non-obvious requirement: the AP-19 frequency-driven governance decay anti-pattern means governance quality can degrade faster at high frequency than at low frequency, and the monitoring cadence must be calibrated to event frequency rather than held at a fixed schedule. None of these requirements is derivable from either commitment read in isolation; all three emerge from the composition. This note formalizes the three requirements, identifies their prior-art significance for governance systems combining high-frequency and health-monitoring commitments, and provides an operational test for verifying each requirement in a deployed system.

---

## 1. Pair Identification

**Commitment A — High-Frequency Event Governance (D2.71).** This commitment specifies the governance infrastructure required for organizations that conduct Full Aspect Integration (FAI) events at daily or weekly frequency. The infrastructure has three components: sampled post-mortem review, in which every N events (not every event) receives a governance review for quality assessment; automated governance labor, in which governance tasks that would not scale to every event at high frequency are partially automated under human authority; and frequency-aware conflict-handling capacity, in which the organization's conflict registry and escalation pathway are designed to handle simultaneous or rapidly successive events rather than sequential events with ample clearance time between them. D2.71 addresses the operational shape of governance at high frequency; it does not specify what governance quality looks like or how to detect its degradation.

**Commitment B — Governance Health Monitoring (D2.35).** This commitment specifies six health indicators — H1 through H6 — for assessing FAI governance quality. H1 measures conflict registry completeness: what fraction of FAI events have complete, well-formed conflict registry entries. H2 measures escalation pathway integrity: whether the pathways for escalating conflicts to human authority are intact and exercisable. H3 measures escalation response rate: how promptly governance authority responds to escalated conflicts. H4 measures substrate audit coverage: what fraction of substrate content is covered by current audit records. H5 measures configuration governance currency: whether the governance configurations for FAI parameters are current and within authorized bounds. H6 measures evolution-feed traceability: whether the hand-off from FAI events to each Self's home-perimeter evolution machinery is traceable. D2.35 specifies what to measure; it does not specify how measurement scales with event frequency.

The composition pair is therefore: an organization using both D2.71 and D2.35 simultaneously — conducting FAI events at high frequency while maintaining governance health monitoring over those events.

---

## 2. The Governance Scenario

An organization conducts FAI events at daily frequency — fifty to a hundred events per week, depending on coordination volume. It has adopted D2.35's six health indicators as its governance quality monitoring framework and D2.71's high-frequency governance infrastructure as its operational model. A governance officer reviews the weekly health indicator report.

The report shows that H1 (conflict registry completeness) has flagged seven unresolved conflicts over the past week, which is above the threshold of five that was set when the organization first adopted D2.35 at lower event frequency. The officer escalates to a governance review. The review finds that governance quality has not degraded — seven unresolved conflicts in a week of eighty events represents a 91% registry completeness rate, which is strong performance. The threshold of five was calibrated for a period when the organization ran ten events per week; seven unresolved conflicts in ten events would have been alarming (30% incomplete), but seven in eighty is not.

The scenario surfaces the core problem: health indicator thresholds that were correctly calibrated for one event frequency produce misleading signals at another. The composition of D2.71 and D2.35 requires explicit, frequency-adjusted threshold calibration that neither commitment specifies on its own.

A second scenario: between sampled post-mortem reviews — every N=20 events — governance quality degrades in a way that the next scheduled review would detect, but not before ten events have been conducted under degraded governance. At high frequency, ten events may occur in two days. A governance failure that would have been detected within a few days at low frequency goes undetected for the equivalent of two weeks of low-frequency governance before the next scheduled review. The combination of D2.71's sampled review and D2.35's six indicators requires automated monitoring between reviews to close this gap.

---

## 3. Non-Obvious Governance Requirements

### Requirement 1 — Frequency-Adjusted Health Thresholds

Health indicator thresholds must be specified as frequency-relative ratios rather than absolute counts. This requirement is not apparent from either D2.71 or D2.35 read in isolation.

D2.35 specifies six health indicators and the concept of a threshold per indicator. It does not specify how thresholds should be calibrated or whether the calibration should vary with event frequency. A practitioner implementing D2.35 without awareness of D2.71 might naturally specify H1's threshold as an absolute count — "flag for review if more than five conflicts are unresolved at end of week" — which is a reasonable choice in a low-frequency context.

D2.71 specifies that high-frequency governance infrastructure differs from low-frequency governance infrastructure in operational shape — sampled review rather than every-event review, automated labor, parallelism-aware conflict handling. It does not address how health monitoring thresholds interact with frequency.

The composition makes the frequency-threshold interaction unavoidable. At high frequency:

- **H1 (conflict registry completeness)** must be measured as the percentage of events with complete conflict registry entries, not as a count of incomplete entries. An organization running five events per week and an organization running one hundred events per week may both have strong governance quality while generating very different absolute counts of incomplete entries.

- **H3 (escalation response rate)** must account for simultaneous escalations. At low frequency, escalations arrive sequentially with time between them; the threshold can be specified as a maximum response time for the next escalation. At high frequency, multiple escalations may arrive within the same governance window; the threshold must be specified as a rate — escalations resolved per unit time, or percentage of escalations resolved within a time window — rather than as a simple sequential response time.

- **H4 (substrate audit coverage)** must be measured relative to the number of events in the audit window. At high frequency, the substrate grows substantially between audit cycles; coverage measured as a percentage of events audited is a more stable indicator than coverage measured as a count of audited entries.

The general principle: any health indicator that accumulates with event count must be expressed as a rate or percentage rather than an absolute value. The composition of D2.71 and D2.35 requires that every indicator in the H1–H6 set be evaluated for frequency-sensitivity and re-specified in ratio form where sensitivity is present.

### Requirement 2 — Automated Health Monitoring Between Sampled Reviews

The combination of D2.71's sampled post-mortem review and D2.35's six health indicators produces a structural gap: between sampled reviews, the six indicators are unmonitored unless an additional automated monitoring layer operates.

D2.71 specifies sampled review (every N events) as the governance review cadence for high-frequency operations, on the grounds that a full governance review of every event does not scale to high frequency. D2.35 specifies six health indicators as the measurement framework for governance quality. Read separately, the natural implementation is: apply the six indicators at each sampled review. Read together, this natural implementation is insufficient.

At high frequency, the gap between sampled reviews spans many events. If N=20 and the organization runs ten events per day, the gap between reviews is two days. Governance quality can degrade within a two-day span — conflict registry discipline can slip, escalation pathways can become congested, configuration governance can drift — and the degradation will not be detected until the next scheduled review, two days later, after potentially twenty more events have been conducted under degraded governance.

The composition requires a two-layer monitoring architecture:

**Layer 1 — Automated between-review monitoring.** Automated proxies for each of the six health indicators operate continuously between sampled reviews. These proxies need not replicate the full depth of a sampled review — they can be lightweight automated checks on structural properties of substrate content (Is the conflict registry entry complete for each completed event? Has the escalation pathway been exercised within its defined response window? Is the substrate audit current?). The proxies generate continuous signals rather than periodic assessments.

**Layer 2 — Sampled post-mortem review.** Every N events, a full governance review assesses quality in depth — reviewing the substance of how conflicts were resolved, whether evolution-feed hand-offs were correctly executed, whether governance configurations remain within authorized bounds. The depth of a sampled review cannot be automated without losing the governance quality that makes the review meaningful; this layer remains human-governed at its core.

The automated layer triggers an unscheduled review when any indicator proxy exceeds its threshold between scheduled reviews. The unscheduled review protocol is itself governance content — it specifies what triggers it, who conducts it, what actions it can authorize, and how its outcomes are recorded. Neither D2.71 nor D2.35 alone specifies this two-layer architecture with unscheduled review triggering; the architecture is a non-obvious product of their combination.

### Requirement 3 — Health Indicator Degradation Detection Rate

The AP-19 frequency-driven governance decay anti-pattern identifies a systematic failure mode: governance quality degrades faster at high event frequency than at low frequency because shortcuts accumulate faster, discipline erodes faster, and coordination volume amplifies small quality deficits into large governance failures. This anti-pattern means that the time available to detect a degradation before it compounds is shorter at high frequency.

D2.35 specifies six health indicators but does not specify how frequently they should be assessed. D2.71 specifies sampled post-mortem review but, as noted in Requirement 2, creates monitoring gaps between reviews.

The composition produces a degradation detection rate requirement: the monitoring cadence must scale with event frequency so that the expected time to detect a degradation does not grow as event frequency increases.

More precisely: if degradation of indicator H1 would typically become detectable within twenty events of its onset, then the monitoring cadence must be no coarser than twenty events regardless of calendar time. At a frequency of one event per week, twenty events correspond to five months — a monthly health review easily meets the cadence requirement. At a frequency of ten events per day, twenty events correspond to two days — a monthly health review does not meet the cadence requirement, because degradation can compound over twenty-five times as many events before detection.

The cadence scaling requirement is operationally distinct from the threshold adjustment requirement (Requirement 1) and the automated monitoring architecture (Requirement 2). An organization could implement frequency-adjusted thresholds and automated monitoring but apply monitoring at fixed calendar intervals regardless of event frequency; such an organization satisfies Requirements 1 and 2 but not Requirement 3. The cadence itself must be a function of event frequency, not a fixed governance schedule.

---

## 4. Prior-Art Significance

This composition pair establishes prior art for the architectural category "governance health monitoring for high-frequency AI coordination events."

The specific frequency-adjusted architecture — adjusted thresholds, automated between-review monitoring with unscheduled review triggering, cadence scaling as a function of event frequency — is not derivable from either D2.71 or D2.35 read in isolation, nor from generic quality management literature applied to AI systems, nor from AI monitoring literature that addresses individual model outputs rather than coordination governance. The composition pair formalizes the specific requirements that emerge when a high-frequency event regime and a health indicator framework are combined under human governance.

Any subsequent governance system that applies health monitoring to high-frequency AI coordination events must address the three requirements this composition pair identifies. A system that applies D2.35's six indicators with absolute-count thresholds to a high-frequency regime has failed to satisfy the frequency-adjusted threshold requirement. A system that applies sampled review without automated between-review monitoring has created a governance gap that is benign at low frequency but structurally hazardous at high frequency. A system that applies health monitoring at fixed calendar intervals regardless of event frequency has miscalibrated its degradation detection capacity.

The prior-art record established here forecloses independent claims on the specific architecture combining these three properties — frequency-adjusted ratios, automated continuous monitoring between sampled reviews, and cadence scaling — for governance systems operating at high frequency over AI coordination events.

---

## 5. Operational Test

For a high-frequency FAI participant with governance health monitoring, an observer can verify the composition pair's requirements with four checks:

**(a) Frequency-adjusted thresholds.** Is each of the six health indicators specified with a threshold expressed as a rate or percentage (e.g., percentage of events with complete conflict registry entries) rather than as an absolute count (e.g., five or fewer incomplete entries per week)? Are indicators that accumulate with event count — H1, H3, H4 at minimum — expressed in ratio form? A system that specifies any health indicator threshold as an absolute count in a high-frequency context has not satisfied Requirement 1.

**(b) Automated between-review monitoring.** Does automated monitoring of the six health indicators (or their automated proxies) operate between sampled post-mortem reviews? Can an observer identify the automated monitoring layer as a distinct component of the governance infrastructure? A system in which the six indicators are assessed only at scheduled sampled reviews, with no monitoring between reviews, has not satisfied Requirement 2.

**(c) Unscheduled review protocol.** Does a governance document or substrate entry specify the conditions under which automated monitoring triggers an unscheduled review, who conducts it, what actions it can authorize, and how outcomes are recorded? A system in which automated monitoring generates signals but no unscheduled review protocol exists to respond to threshold exceedances has not satisfied Requirement 2's triggering component.

**(d) Cadence scaling with event frequency.** Is the monitoring cadence specified as a function of event frequency (e.g., every N events, or every T days where T is calibrated to event frequency) rather than as a fixed calendar interval? If the organization's event frequency increases significantly, does the monitoring cadence adjust accordingly, or does it remain fixed? A system in which monitoring cadence is decoupled from event frequency has not satisfied Requirement 3.

A governance system that passes all four checks satisfies the composition requirements this pair establishes. A system that passes the checks from D2.71 and D2.35 individually but fails any of the four checks above has governance infrastructure appropriate to each commitment separately but not to their combination.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Composition Pair 5: High-Frequency Events and Governance Health Monitoring.* Derivation Note D4.06, CKS Derivation Note Series. May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
