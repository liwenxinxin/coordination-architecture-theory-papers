# FAI Governance for High-Frequency Events

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

It does not introduce new axioms. Its contribution is to derive the governance infrastructure required when FAI events occur at high frequency — daily or weekly cadence with recurring partners — and to identify the four infrastructure elements that allow governance integrity to be maintained at that scale.

## Abstract

FAI governance at low frequency is largely served by per-event configuration authoring, full post-mortem review, and manual governance labor. At high frequency — daily or weekly events with regular partners — this per-event governance posture becomes operationally unsustainable. This note formalizes the four infrastructure elements required to sustain FAI governance at high frequency: comprehensive standing configurations covering all six FAI dimensions per partner, automated governance labor executing under pre-authorized standing configurations, sampled post-mortem review with automated health monitoring between samples, and escalation capacity planning calibrated to event volume. The note further states the governance integrity non-negotiables that hold at any frequency regardless of infrastructure automation, identifies the governance health dashboard as the primary tool for detecting frequency-driven governance decay, and provides an operational test for verifying that a high-frequency FAI participant has the required infrastructure in place.

## 1. The scaling problem: governance infrastructure at high frequency

FAI governance architecture is designed around a set of governance operations that must occur at every event: shared substrate construction (with a construction record), conflict registration and handling during the event, dissolution (with a dissolution record), and evolution feed activation at dissolution. These are not optional steps — they constitute the minimum viable governance floor that every FAI event must meet (D2.37). At low frequency, each of these operations can be performed manually by the relevant governance parties without creating unsustainable labor demand.

At high frequency — daily events, or multiple events per week with the same recurring partners — per-event manual governance labor becomes a binding constraint. If an organization runs FAI events with a given partner daily, requiring fresh per-event configuration authoring, manual conflict registry maintenance throughout each event, manually generated dissolution records, and full post-mortem review after each event will either consume governance capacity entirely or be quietly abandoned. The second outcome is the more dangerous one: governance obligations appear to be met while governance quality silently declines.

This note derives the governance infrastructure required to prevent that outcome. The derivation proceeds from three parent notes. D2.21 (standing configurations) establishes that governance configurations covering recurring event patterns can be authored once, jointly approved, and applied at each subsequent event in lieu of per-event authoring. D2.37 (minimum viable governance) establishes the governance floor that every FAI event must meet regardless of frequency or automation. D2.41 (time-sensitive governance) establishes the principle that governance can be pre-authorized for operational contexts that do not permit deliberative review at event time — a principle that extends directly to high-frequency contexts where deliberative per-event review is impractical by volume rather than by time pressure.

The governance challenge at high frequency is therefore not a new problem but a scaling condition on existing governance architecture. The infrastructure elements derived below are what the existing architecture requires when that scaling condition applies.

## 2. Infrastructure element 1: comprehensive standing configurations

Standing configurations (D2.21) are the foundational infrastructure element for high-frequency FAI governance. A standing configuration is a governance artifact — itself substrate content under joint authority — that specifies the governance parameters for FAI events with a given partner without requiring those parameters to be authored at each event. At high frequency, standing configurations must be comprehensive: they must cover all six FAI dimensions (aspects contributed by each party, depth of provenance carry-over at the perimeter, persistence policy after dissolution, conflict-handling tier selection, escalation-path configuration, evolution feed ingestion parameters) rather than covering only selected dimensions with per-event supplementation.

The comprehensive coverage requirement follows from the operational context. At high frequency, there is no practical mechanism for per-event supplementation of a partially-specified standing configuration: the event cadence does not permit the deliberative authoring and joint approval that supplementation would require. If the standing configuration does not cover a dimension, that dimension is ungoverned at high frequency. Comprehensive coverage is therefore not a preference but a structural requirement.

Two properties of standing configurations are particularly important at high frequency. First, standing configurations carry governance authority, not merely operational preference. When automation fires at event start to generate a construction record, it does so because the standing configuration authorizes that action. The authority was exercised when the standing configuration was jointly authored and approved; the automation executes that pre-authorized decision. The non-delegation principle (D2.43) holds throughout: governance authority is not delegated to the automation; it was exercised in advance by the governance parties who hold that authority.

Second, high-frequency events generate governance intelligence — through post-mortems (D2.39), through the governance health dashboard (D2.35), through escalation patterns — faster than low-frequency events do. Standing configurations should accordingly be reviewed more frequently at high cadence than the nominal annual-or-as-needed review cadence appropriate for low-frequency participation. The standing configuration review cadence is itself a governance parameter that belongs in the standing configuration.

## 3. Infrastructure element 2: automated governance labor

At high frequency, the four core governance labor operations — construction record generation at event start, conflict registry maintenance during the event, dissolution record generation at event end, and evolution feed activation at dissolution — must be substantially automated. The alternative is unsustainable labor demand on governance parties who may themselves be operating under resource constraints.

The architecture governing this automation requires precision. The distinction between governance labor and governance authority (D2.43 extending Paper 1 §3.3) is the load-bearing structure. Automated governance labor means automating the execution of governance decisions that have already been made and authorized. It does not mean automating the making of governance decisions. The difference between these two postures is the difference between an automation that generates a construction record because the standing configuration authorizes construction records for this partner in this event class, and an automation that decides whether this event should occur at all or how conflicts during it should be resolved.

Concretely: automated construction record generation at event start is governance labor automation. The governance decision — that FAI events with this partner produce construction records with these fields — was made when the standing configuration was authored. The automation executes that decision at each event start without requiring the governance parties to re-make it. The authority is in the standing configuration; the labor is automated. The same logic applies to automated conflict registry maintenance (the governance decision to register conflicts was made in the standing configuration; automation executes it), automated dissolution records (governed by the standing configuration's dissolution parameters), and automated evolution feed activation (governed by the standing configuration's ingestion-policy specification).

What cannot be automated under this architecture is governance authority itself. Conflict escalation decisions — where a conflict cannot be resolved by the configured orchestration tier and must be referred to the governance parties under joint authority — cannot be automated. Joint authority decisions over configuration changes cannot be automated. Post-mortem findings that require standing configuration revision require human governance action. The automation handles the execution layer; the authority layer remains with the governance parties.

This is not a limitation of high-frequency governance; it is its structural definition. An organization that routes authority decisions to automated systems has not achieved efficient high-frequency governance — it has abandoned the governance architecture entirely.

## 4. Infrastructure element 3: sampled post-mortem review

D2.39 establishes post-mortem review as the mechanism through which governance intelligence accumulates after FAI events: what conflicts arose, how they were handled, what escalations occurred, what standing configuration parameters should be revisited. At low frequency, full post-mortem review after every event is practical and appropriate. At high frequency, it is not.

The practical governance solution is a sampled review cadence: full post-mortem review after every N events, with automated governance health monitoring (D2.35) between full reviews to identify warning indicators that require immediate attention before the next scheduled review.

Several design parameters require governance attention. The sampling rate N is not an arbitrary convenience setting. It is a governance decision that should be calibrated to the governance complexity of the events being run: events with high conflict rates, novel conflict classes, or participation by partners whose aspects are evolving rapidly warrant more frequent review than events with stable conflict patterns and mature standing configurations. The sampling rate belongs in the standing configuration and is subject to the same joint-authority authorship requirement as all other governance parameters.

Between full post-mortems, automated governance health monitoring serves as the detection layer for conditions that cannot wait for the next scheduled review. The governance health dashboard (D2.35) tracks indicators including: conflict registration rates (are conflicts being registered at expected rates?), escalation volumes (are escalations accumulating at a rate governance capacity can respond to?), resolution rates (are conflicts being resolved within configured timelines?), and standing configuration coverage gaps (are events generating conflict classes the standing configuration does not address?). An indicator that might be addressed in a subsequent event at low frequency requires immediate attention at high frequency, because the next event follows quickly and an unaddressed condition will compound.

The sampled post-mortem is a practical accommodation — not a compromise of governance integrity. The minimum viable governance floor (D2.37) is met at every event through the standing configuration and automated governance labor. The post-mortem cadence governs the reflection and learning loop, not the per-event governance floor. Reducing the post-mortem cadence reduces the rate of governance learning; it does not reduce the per-event governance minimum.

## 5. Infrastructure element 4: escalation capacity planning

Escalation capacity is a finite resource. At low frequency, the number of escalations per time period is bounded by the event cadence. At high frequency, escalations can accumulate faster than governance parties can respond to them, particularly during periods of standing configuration misalignment with actual event complexity.

Governance must therefore plan escalation capacity explicitly. The planning involves three steps. First, estimating escalation volume: for events at the planned cadence, what is the expected escalation rate per event given the partner's conflict history and the standing configuration's conflict-handling tier specification? Second, estimating governance response capacity: how many escalations per time period can the governance parties to this standing configuration respond to within the configured escalation response timeline (D2.14)? Third, identifying the constraint: if projected escalation volume exceeds response capacity, either event frequency must be reduced or escalation response capacity must be expanded.

Ignoring the capacity constraint does not make it disappear. Escalations that exceed governance response capacity accumulate as unresponded escalations, which means exchange bounding (D2.16) cannot be verified for the events that generated them, which means the minimum viable governance floor is no longer being met. The governance architecture degrades not because of a discrete decision to abandon governance but because of a continuous mismatch between demand and capacity that was not planned for.

Escalation capacity planning is itself a governance responsibility, not an operational one. The standing configuration should record the estimated escalation volume, the confirmed governance response capacity, and the cadence at which this capacity planning will be revisited.

## 6. Governance integrity non-negotiables at any frequency

The four infrastructure elements above describe what high-frequency governance requires in addition to baseline governance architecture. The following items are not relaxed by high-frequency operation — they hold at every event regardless of cadence, automation level, or operational pressure.

Every event meets the minimum viable governance floor (D2.37). Automation handles the governance labor; the standing configuration carries the governance authority; the floor is met at every event. An event that does not meet the floor is a governance failure regardless of how many events preceded it that did.

Every conflict is registered (D2.13). Automated conflict registry maintenance ensures this at high frequency. An unregistered conflict cannot be handled, escalated, or reported; automated registration is the mechanism that prevents conflicts from falling through the governance record at high event cadence.

Every escalation receives a response within the configured timeline (D2.14). This is the primary constraint that escalation capacity planning (§5) is designed to protect. If response capacity is insufficient for the event cadence, the cadence must be reduced. The escalation response obligation is not a target; it is a binding commitment under the governance architecture.

Exchange bounding holds (D2.16). At high frequency, every-event verification of exchange bounding is impractical. Verification is instead performed through periodic sampling — sampled post-mortems and health dashboard monitoring — calibrated to detect exchange bounding violations with sufficient reliability for the governance context. The obligation does not disappear; the verification mechanism adapts.

## 7. Governance health at high frequency and the anti-pattern of frequency-driven decay

The governance health dashboard (D2.35) is the primary instrument for detecting governance quality at high frequency. At low frequency, post-mortem review and direct governance party observation provide sufficient visibility into governance health. At high frequency, the volume of events makes direct observation impractical; health must be tracked through aggregate indicators.

The dashboard indicators most relevant for high-frequency governance are: conflict registration completeness (are all events producing complete conflict records?), escalation response timeliness (are escalations being responded to within configured timelines?), standing configuration coverage stability (is the proportion of events generating unconfigured conflict classes increasing?), and post-mortem finding velocity (are post-mortem findings producing standing configuration updates at a rate that keeps the configuration current?).

Collectively these indicators detect the primary governance risk at high frequency: frequency-driven governance decay. This anti-pattern arises when an organization increases FAI event frequency without proportionally increasing governance infrastructure. The events run faster; the governance infrastructure — standing configurations not reviewed at appropriate frequency, post-mortems sampled too coarsely, escalation capacity not expanded to match volume, health dashboard not monitored — fails to scale with the event cadence. The degradation is characteristically invisible within any single event. Each individual event may appear to be meeting its governance obligations. The decay is visible only as a pattern: conflict registration rates declining, escalation response timelines lengthening, standing configurations drifting from the actual governance needs of the events they govern, post-mortem findings accumulating without producing configuration updates.

The anti-pattern's invisibility at the event level is precisely why the health dashboard matters at high frequency. An observer looking at any single event in a decaying high-frequency program may conclude that governance is functioning; the dashboard, tracking trends across many events, reveals the pattern.

## 8. Operational test

A high-frequency FAI participant has the required governance infrastructure in place if and only if an independent observer can verify all of the following:

1. A comprehensive standing configuration exists for each regular partner, covering all six FAI dimensions, with evidence of joint authority authorship and approval. The standing configuration records its own review cadence and documents the last review.

2. Automated governance labor is operational: construction records are generated at each event start, conflict registry is maintained during each event, dissolution records are generated at each event end, and evolution feeds are activated at each dissolution — all without per-event manual authoring, and all traceable to authorization in the standing configuration.

3. A sampled post-mortem cadence is specified in the standing configuration and is being followed. The sampling rate is calibrated to the governance complexity of the events. Automated health monitoring is operational between full post-mortems, with documented thresholds for indicators requiring immediate attention.

4. Escalation capacity has been estimated, compared to escalation volume, and found sufficient — or, where insufficient, the event cadence has been reduced or response capacity expanded to restore sufficiency. This planning is documented in the standing configuration.

5. The minimum viable governance floor (D2.37) is verifiably met at every event: every conflict is registered, every escalation receives a response within the configured timeline, and exchange bounding is verified through the sampling mechanism at the configured rate.

6. The governance health dashboard shows no sustained trends indicating frequency-driven decay: conflict registration completeness, escalation response timeliness, standing configuration coverage stability, and post-mortem finding velocity are all within the ranges the governance parties have established as acceptable.

A high-frequency FAI participant that fails any of (1)–(6) has a governance infrastructure gap that, if unaddressed, will produce cumulative governance degradation across subsequent events.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance for High-Frequency Events.* May 15, 2026. ORCID: 0009-0004-8065-3235.
