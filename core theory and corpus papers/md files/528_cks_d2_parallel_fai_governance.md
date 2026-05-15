# Managing Parallel FAI Events at Governance Scale

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

A CKS-governed Self participating in the population-scale FAI network may have multiple FAI events active simultaneously — with different partner Selves, covering different domains, at different lifecycle phases. This note formalizes the governance requirements for managing parallel FAI events as an operational decomposition of D1.26 (joint authority at population scope) and D1.22 (configuration as substrate content). The note establishes three core properties: (1) architectural isolation between parallel events at the shared-substrate level, which is what makes parallel participation safe; (2) governance portfolio management, comprising a portfolio record, attention triage, and a home-governance-authored capacity threshold; and (3) isolation verification for the special case of parallel events involving overlapping partner Selves. It names the anti-pattern governance overextension, identifies its connection to the emergency-dissolution trigger established in D2.28, and provides an operational test for a Self carrying three concurrent active FAI events.

## 1. The parallel-event governance problem

D1.26 establishes joint authority at population scope — the architectural commitment that population-level dynamics across a FAI network are governable through the same substrate-mediated mechanism as individual FAI events, with each event operating under joint authority across the participating Selves' governance perimeters. D1.22 establishes that every configurable dimension of an FAI event is itself substrate content, including the dimensions that govern how a Self participates in the network. Together these two parents create the parallel-event governance problem: at population scope, a Self is not just a participant in one event but a potential concurrent participant in many, and the governance obligations that joint authority entails — conflict registry monitoring, exchange-bounding verification, escalation response, configuration amendment authorization — multiply with participation count.

Nothing in the architecture prevents a Self from accepting participation in an unbounded number of concurrent FAI events. The shared-substrate architecture scales horizontally: each new event constructs its own shared substrate, draws its own governance perimeter, and operates under its own joint authority. The architecture does not experience congestion in this horizontal sense. Governance, however, is not horizontal: it is exercised by the humans who constitute home governance, and those humans have finite attention. The parallel-event governance problem is therefore a human-capacity problem, not an architectural-capacity problem. D2.33 formalizes how governance should be structured — through explicit records, deliberate attention allocation, and authored capacity limits — to remain adequate across the full portfolio of active events.

## 2. Derivation from D1.26 and D1.22

D2.33 is an operational decomposition of two parents. From D1.26 it inherits the joint-authority framing: governance over each active FAI event is not unilateral but joint, spanning the governance perimeters of all participating Selves. This means that governance obligations are not optional — an active event has governance demands that home governance committed to when the event was initiated, and those demands persist until the event dissolves. From D1.22 it inherits the substrate-content framing: the configuration of how a Self participates in the network is itself substrate content, subject to the full six Paper 1 commitments — including human governance, inspectability, and path retraceability. This means that governance's determination of how many parallel events it can handle, and the rules for managing the resulting portfolio, are not informal policies held in human heads; they are authored governance content in the home substrate, auditable and revisable under normal governance mechanisms.

The operational decomposition at D2.33 works on the question that these two parents leave open: given that a Self may be participating in several active FAI events simultaneously, how should governance be organized at the portfolio level — not just within each individual event — to preserve the joint-authority commitment that each event requires?

## 3. Architectural isolation between parallel events

Each FAI event constructs a distinct shared substrate. The shared substrate for Event 1 is one object; the shared substrate for Event 2 is another. These are separate substrate instances with separate governance perimeters, separate joint authority configurations, separate conflict registries, and separate orchestration rules. There is no architectural connection between them. Content written into Event 1's shared substrate is not readable from Event 2's shared substrate; conflict escalations in Event 1 do not reach Event 2's joint authority; an emergency dissolution of Event 1 does not touch Event 2.

This architectural isolation is not incidental. It is the property that makes parallel participation safe. Because each event is structurally independent, a governance failure in one event — or the full emergency dissolution sequence — is contained within that event's governance perimeter. The other active events continue operating under their own joint authority structures without automatic disturbance.

The isolation does not, however, prevent all inter-event influence. Within the participating Self's home substrate, records from parallel events are kept distinct through FAI event ID provenance (established in D2.03): each event's contribution records, conflict registry entries, and evolution feed outputs are attributed to their specific event. After an event dissolves, its outputs may be ingested into the home substrate through the four-locus evolution-feed mechanism (D1.17–D1.21). Those ingested outputs then become part of the home substrate's accumulated content, available to inform subsequent events — including events that begin after the first has closed. This pathway through the home substrate is the only legitimate channel by which one event's outputs can influence another, and it operates only at event boundaries, not during concurrent live events. Cross-event influence during concurrent active participation can only occur if home governance deliberately carries content across, which requires home-governance action and leaves a trace in the home substrate's provenance record.

The isolation-is-architectural-safety principle has a practical governance implication: governance should not compensate for the safety that isolation provides by treating parallel events as if they were internally connected. Each event's governance attention should be directed at the demands of that event, not at managing dependencies between events that the architecture ensures do not exist at the shared-substrate level.

## 4. Governance attention allocation across parallel events

Each active FAI event generates ongoing governance obligations. At minimum, these are: monitoring the conflict registry for new conflicts and escalations; verifying exchange bounding at configured intervals; responding to escalations within configured response timelines; and authorizing configuration amendments when required. Standing configuration (D2.21) and pre-authorized orchestration rules (D2.15) reduce the per-event attention load by automating routine cases — but they do not eliminate the monitoring obligation, and they do not eliminate the escalation-response obligation when configured orchestration rules reach their limit and surface a conflict to human authority.

When multiple events are active simultaneously, these obligations run in parallel. An escalation in Event 2 does not pause because governance is currently engaged with a conflict in Event 1. Response timelines configured under D2.14 run continuously regardless of what else is active. Exchange-bounding verification windows open and close on each event's own schedule. The governance attention demand of a portfolio of parallel events is approximately the sum of the individual demands of each event, less whatever reduction standing configuration provides, but with the added complexity that demands from different events may arrive simultaneously rather than sequentially.

This additive and asynchronous character of the attention demand is what makes governance capacity the operative limit on parallel participation. The architecture supports any number of concurrent events; governance does not.

## 5. Governance portfolio management

The set of a Self's active FAI events constitutes a governance portfolio. Managing the portfolio effectively requires three operational structures authored as home-substrate governance content.

**Portfolio record.** The home substrate should carry a portfolio record: a maintained record of all currently active FAI events, their lifecycle phase, their partner Selves, the domain or aspect scope of each event, and any pending governance actions within each event. The portfolio record is not a summary for convenience; it is authoritative governance content. It is the substrate artifact that makes the portfolio visible to human governance at any moment — fulfilling the inspect right that CKS's human-governed commitment requires (per the authority/labor distinction from Paper 1 §3.3). An observer who has access to the home substrate should be able to determine, from the portfolio record alone, which FAI events are active, at what phase, and what governance actions they are waiting on.

**Attention triage.** When multiple active events simultaneously present governance demands — two escalations arriving on the same day, an exchange-bounding verification window opening while a conflict-registry review is pending — governance must triage. Triage prioritizes governance actions based on urgency (configured response timelines under D2.14 establish the urgency hierarchy for escalations) and strategic importance (relative significance of the event's domain to the participating Self's operational continuity). Triage rules should themselves be authored as governance content — either within the portfolio record or within the network participation configuration (D2.31) — so that the prioritization logic is explicit and does not depend on ad hoc human judgment under time pressure. A triage rule that is only in human heads is a governance rule that cannot be inspected, audited, or revised through normal substrate governance.

**Capacity threshold.** Home governance should establish a maximum parallel participation threshold: the maximum number of FAI events it can govern effectively and simultaneously. This threshold is home governance content — part of the network participation configuration authored under D2.31. The architecture does not prescribe the value of the threshold; that determination belongs entirely to home governance based on its actual staffing, attention bandwidth, and the governance demands of the event types it typically participates in. What the architecture requires is that the threshold be authored explicitly as substrate content, not held as an informal upper limit that no one has recorded.

The capacity threshold must be set conservatively. Governance attention demands are not perfectly predictable: an event that appeared low-demand at initiation may surface a conflict requiring escalation precisely when another event is also escalating. The threshold should incorporate buffer against simultaneous-demand spikes. A threshold set at governance's observed maximum capacity, with no buffer, is a threshold that will be exceeded under normal variance.

The threshold also requires periodic review. As standing configuration and pre-authorized orchestration rules mature — as home governance accumulates experience with the typical attention patterns of FAI events — the threshold may appropriately increase. As governance staffing changes or the complexity of participated events increases, the threshold may need to decrease. Because the threshold is authored governance content, this review and revision is a standard governance action.

## 6. Isolation verification for overlapping partner sets

The general isolation property in §3 holds for all parallel events. But a specific case requires explicit verification: parallel events with overlapping partner Selves. When Self A participates in Event 1 with Self B and simultaneously in Event 2 also with Self B, the architectural isolation between the shared substrates of Event 1 and Event 2 remains intact. The two events still have separate shared substrates, separate joint authorities, and separate governance perimeters. Neither shared substrate can read from the other.

However, governance should explicitly verify this isolation when overlapping partner sets occur, for two reasons. First, the overlapping-partner case creates a surface where inadvertent cross-event influence is most plausible — humans governing both events may unconsciously carry information from one event's governance decisions into the other. Second, overlapping partners may create strategic complexity: what Self A learns about Self B's coordination posture in Event 1 could, in principle, inform how Self A configures participation in Event 2. Whether such cross-event influence is appropriate depends on governance's determination of each event's purpose and scope; it cannot be resolved architecturally.

The isolation verification requirement for overlapping partner sets amounts to an explicit governance check: is any content from Event 1's shared substrate appearing in Event 2's shared substrate, or vice versa, through any path other than the home-substrate evolution-feed pathway? If the answer is yes, cross-event substrate contamination has occurred, and the architectural isolation has been violated. Home governance must identify how the contamination occurred and restore isolation before the affected events proceed.

## 7. Anti-pattern: governance overextension

Governance overextension is the anti-pattern of participating in more simultaneous FAI events than home governance can effectively monitor and respond to. The failure mode has a specific progression: as parallel participation count increases past the effective capacity threshold, governance attention is spread thin; escalation response times lengthen toward and then past configured deadlines; conflict-registry monitoring becomes irregular; exchange-bounding verification is delayed. At the extreme, governance is no longer providing the minimum attention required for at least one active event to operate within the joint-authority commitments that event requires.

This condition is D2.28 Trigger 1: governance capacity failure. When an active FAI event loses adequate governance coverage because home governance's attention has been depleted by parallel obligations, the conditions for emergency dissolution of that event are present. Emergency dissolution is architecturally correct but operationally costly: it terminates an event that may be mid-lifecycle, may have produced content the participating Selves were counting on, and may damage the governance relationship with the partner Self.

The connection between governance overextension and D2.28 Trigger 1 establishes the direction of the conservative bias for the capacity threshold. Because the failure mode that follows threshold violation leads to emergency dissolution — not to a graceful slow-down — the threshold must be set to allow home governance to reduce participation before reaching the trigger, not at it. A Self that accepts a new event when already at its capacity threshold has no buffer between its current state and the trigger condition. A Self that maintains the threshold at a conservatively low value retains the ability to respond to unexpected governance demand increases by pausing the consideration of new events before any active event is endangered.

The practical implementation of this conservative posture: when a new FAI event initiation is proposed and the Self's current portfolio is at or approaching the capacity threshold, home governance should decline the new participation or defer it — not force it through on the assumption that governance will manage. Declining new participation when at capacity is not a governance failure; it is the governance discipline that keeps the existing portfolio governable.

## 8. Operational test

For a Self with three parallel active FAI events, a governance observer should be able to verify all three of the following properties:

1. **Shared-substrate isolation.** Each of the three active events has a distinct shared substrate. The observer can identify three separate substrate instances, each with its own joint authority configuration, conflict registry, and governance perimeter. No content written into one event's shared substrate appears in another event's shared substrate except through the explicit home-substrate evolution-feed pathway after an event that has completed. For any pair of events with overlapping partner Selves, the observer can confirm that the shared substrates are architecturally separate and that no cross-event contamination has occurred.

2. **Portfolio record in the home substrate.** The home substrate carries a portfolio record identifying all three active events by their FAI event IDs, their current lifecycle phases, their partner Selves, their domains or aspect scopes, and any pending governance actions (outstanding escalations, pending exchange-bounding verifications, pending configuration amendment authorizations). A human with appropriate access can read this record directly from the home substrate without requiring access to any of the three shared substrates. The record is current as of the last governance update.

3. **Governance capacity threshold specification.** The home substrate's network participation configuration (or an explicitly referenced governance content artifact within it) carries a documented capacity threshold specifying the maximum number of parallel FAI events home governance will accept simultaneously. The threshold is authored as governance content — not a verbal policy — so it is readable, auditable, and revisionable through normal governance mechanisms. The threshold value includes the reasoning basis (staffing level, typical governance demand per event type, buffer margin against simultaneous-demand spikes) or carries a reference to the governance record where that reasoning appears. With three active events, the portfolio is within the threshold, and the observer can verify this directly.

A Self that fails any of (1)–(3) may be participating in multiple FAI events, but it is not doing so under the governance structure D2.33 formalizes.

## 9. Conclusion

D2.33 formalizes what parallel FAI participation requires from governance. Three properties together constitute adequate governance at portfolio scope. Architectural isolation between parallel events — guaranteed by the separate-shared-substrate construction of each event — is what makes parallel participation safe: governance failures do not automatically propagate across events. Governance portfolio management — portfolio record, attention triage, and conservatively authored capacity threshold, all as home-substrate governance content — is what makes parallel participation auditable and governable. Isolation verification for overlapping partner sets is what ensures that the architectural isolation property is not inadvertently violated in the case where the same partner Self appears in multiple concurrent events.

The capacity threshold is the operational center of gravity for D2.33. It is the authored governance commitment that determines whether a Self can accept new FAI participation without putting its existing portfolio at risk. Setting it conservatively — with buffer against the simultaneous governance demand spikes that normal variation produces — is what keeps active events clear of the D2.28 Trigger 1 boundary. The threshold is not prescribed by the architecture; it is home governance's determination. But its existence as explicit substrate content, rather than as informal practice, is what the architecture requires.

Subsequent work formalizing specific governance workflows for portfolio-level monitoring (D2.34 and beyond) and the D3.xx anti-pattern series for Paper 3's overextension failure mode will build on the three properties D2.33 establishes here.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Managing Parallel FAI Events at Governance Scale.* May 15, 2026. ORCID: 0009-0004-8065-3235.
