# FAI Governance for Time-Sensitive Coordination

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026). It does not introduce new axioms. Its contribution is to articulate, in operational form, how the architecture meets governance requirements when Full Aspect Integration (FAI) events must operate on compressed timelines — deriving this articulation from D1.22 (configuration as substrate content) and D2.37 (FAI minimum viable governance floor).

---

## Abstract

Not all FAI events can afford extended per-event configuration authoring and joint authorization cycles. Some coordination tasks are time-sensitive. This note derives how the architecture accommodates time pressure without compromising the minimum viable governance floor established in D2.37. The derivation turns on a single analytical move: pre-authorization shifts governance work forward in time rather than off the critical path. Three pre-authorization mechanisms — standing configurations (D2.21), comprehensive orchestration rules (D2.15), and pre-specified escalation routing (D2.14) — collectively enable a time-sensitive FAI event to proceed under fully authorized governance whose work was completed before the event began. The minimum viable governance floor is non-negotiable under time pressure; what pre-authorization changes is when the floor's requirements are satisfied, not whether they must be satisfied. The note identifies the time-pressure governance bypass as an anti-pattern adversarial to Paper 3's commitments, formalizes the governance quality and time pressure relationship, and provides an operational test for verifying compliant rapid FAI events.

---

## 1. D2.41 as operational decomposition of D1.22 and D2.37

D1.22 establishes configuration as substrate content: every governance dimension of an FAI event — which aspects each Self contributes, the conflict-handling tier logic, the escalation routing, the persistence policy, the joint authorization structure — is authored and held as substrate content under the participating Selves' governance. Configuration is not metadata about the event; it is first-class substrate content with the same inspectability, modifiability, and authority properties as all other substrate content in the CKS architecture.

D2.37 establishes the minimum viable governance floor for FAI events: a set of requirements that must be satisfied for a FAI event to count as a governed event under the architecture. The floor includes an authored configuration, a construction record, conflict registration as first-class objects, a dissolution record, and contribution attribution for all content. D2.37 establishes that this floor is invariant — it is the floor below which an FAI event is ungoverned, regardless of the operational context that produced it.

D2.41 addresses the intersection of these two commitments under time pressure. Time-sensitive coordination tasks create pressure to abbreviate or bypass the governance work that D1.22 and D2.37 jointly require. D2.41 formalizes what the architecture produces when these commitments are applied to the time-pressure dimension: the governance work required by the floor can be completed before the event begins, and once completed in advance, the event can proceed rapidly without compromising the floor. The derivation is from the architecture's existing commitments; D2.41 introduces no new architectural axioms.

---

## 2. The pre-authorization move: governance forward in time, not off the critical path

The central analytical move of D2.41 is a precise characterization of pre-authorization. Pre-authorization is not a relaxation of governance requirements. It is the structural possibility — inherent in D1.22's configuration-as-substrate-content commitment — of completing governance work before an event occurs rather than during it.

When a standing configuration is established, joint authorization happens at establishment time. The configuration substrate is authored, reviewed, and authorized under the participating Selves' governance before any specific time-sensitive event arises. When a time-sensitive event within the standing configuration's scope subsequently occurs, the governance is already done. The event proceeds under pre-authorized governance — not under bypassed governance.

This distinction is architecturally load-bearing. A time-sensitive FAI event that proceeds under a standing configuration is a governed event: its configuration exists as substrate content, its joint authorization is on record, its conflict-handling logic is pre-specified, and all floor requirements can be met. A time-sensitive FAI event that proceeds without pre-authorization — where the standing configuration does not exist and per-event governance is skipped under time pressure — is an ungoverned event regardless of how the participants characterize it.

Pre-authorization moves governance work earlier. It does not eliminate governance. Every requirement the minimum viable governance floor imposes remains in effect; pre-authorization is one means by which those requirements can be satisfied.

---

## 3. Three pre-authorization mechanisms

The architecture provides three distinct pre-authorization mechanisms. A well-prepared Self deploys all three. Each addresses a different aspect of the governance work that time pressure might otherwise compress.

**Mechanism 1 — Standing configurations (D2.21).** A standing configuration is a configuration substrate that pre-authorizes an FAI event class rather than a single event. It specifies all six FAI governance dimensions for the class of events it covers: which aspects each participating Self contributes, the depth of provenance carry-over, the conflict-handling tier logic, the escalation routing, the persistence policy, and the joint authorization structure. Joint authorization over the standing configuration is obtained from all participating Selves' governance at the time the standing configuration is established.

When a time-sensitive event arises that falls within the standing configuration's scope, no per-event configuration authoring is required. The event uses the pre-authorized configuration directly. The authored configuration requirement of the minimum viable governance floor is satisfied by the standing configuration. The labor of configuration authoring and joint authorization has been performed; it has simply been performed in advance.

The scope discipline of standing configurations is part of their governance function. A standing configuration must accurately specify the class of events it covers; events outside its scope cannot use it without expanding the authorization to cover the new scope. Scope creep — using a standing configuration for events it was not authorized to cover — is a governance violation distinct from bypass but similarly adversarial to the floor.

**Mechanism 2 — Comprehensive orchestration rules (D2.15).** Pre-authored conflict resolution rules that cover the full anticipated range of conflict classes for the event type eliminate the need for real-time governance review of individual conflicts. Under D2.37, conflicts must be registered as first-class objects; they cannot be skipped under time pressure. Comprehensive orchestration rules satisfy this requirement at speed: conflicts are registered as first-class objects and resolved through pre-authored tier logic, with no per-conflict governance negotiation required during the event.

The comprehensiveness criterion is exacting. Rules cover the range of conflict classes only if unanticipated conflict classes are handled by a default carry-through rule — preserving the conflict as first-class substrate state for post-event governance — rather than by improvised resolution or silent suppression. A carry-through default is itself a pre-authored rule; it satisfies the conflict registration requirement while deferring resolution to a timeline that permits deliberate governance review.

**Mechanism 3 — Pre-specified escalation routing (D2.14).** Standing cross-organizational agreement pre-specifies which governance authorities receive escalations of which class, the response protocol, and the timing expectations. When escalation routing is pre-specified, a time-sensitive event can escalate without per-event routing setup. The escalation reaches the appropriate authority through a pre-authorized channel rather than through a routing negotiation that would consume the time the event does not have.

Pre-specified escalation routing is governance infrastructure that operates at the inter-organizational relationship layer rather than the per-event layer. It is established through cross-organizational agreement (D2.34) and maintained as standing substrate content. Like standing configurations and comprehensive orchestration rules, it represents governance work completed in advance so that rapid events can proceed on pre-authorized rails.

---

## 4. What cannot be compressed: the non-negotiable floor

The minimum viable governance floor from D2.37 is invariant under time pressure. Each floor requirement admits pre-authorization as the mechanism for satisfying it rapidly — but pre-authorization satisfies the requirement, it does not waive it. The floor cannot be negotiated down by urgency.

The five floor requirements and their time-sensitive satisfaction paths are as follows.

**Authored configuration must exist.** A standing configuration satisfies this requirement for events within its scope. If no standing configuration exists and no per-event configuration has been authored, this requirement is unsatisfied, and the event is ungoverned.

**A construction record must be produced.** Construction records can be automated: the event initiation can trigger automated record generation that captures the standing configuration reference, the event class designation, the participating Selves, and the initiation timestamp. Automated record generation satisfies the requirement provided the record exists and is held as substrate content. The automation is labor allocation; the record's existence is non-negotiable.

**Conflicts must be registered as first-class objects.** This requirement admits no compression. Every conflict arising during the event must be registered as a first-class substrate object. Time pressure does not authorize conflict suppression, conflict averaging, or silent resolution outside the pre-authored tier logic. If a conflict arises that the pre-authored orchestration rules do not cover, the carry-through default applies: the conflict is preserved as first-class substrate state, flagged for post-event governance review.

**A dissolution record must be produced.** Like construction records, dissolution records can be automated. The event closure triggers automated record generation capturing the event outcome, the content that propagated to each participating Self's home substrate, and the timestamp. The automation is labor allocation; the record is non-negotiable.

**Contribution attribution must exist for all content.** Attribution is tracked through the substrate structure — content contributed by each participating Self carries provenance through the aspect-granularity contribution structure D1.22 specifies. Pre-authorization does not affect this requirement; attribution is an inherent property of the substrate's content structure, not a per-event labor task.

A time-sensitive FAI event in which all five requirements are satisfied through pre-authorization mechanisms is a compliant governed event. A time-sensitive FAI event in which any requirement is absent is a non-compliant ungoverned event. The floor's status as a floor means there is no partial compliance: each requirement is satisfied or it is not.

---

## 5. Governance quality and time pressure

The relationship between governance quality and time pressure is structural rather than incidental. How quickly a Self can participate in governed FAI events depends on how much governance infrastructure the Self has pre-authorized. Time pressure does not change governance requirements; it reveals the governance preparation state of the participating Selves.

**Well-prepared governance.** A Self with comprehensive standing configurations covering its anticipated FAI event classes, pre-authored orchestration rules covering the full anticipated conflict range with carry-through defaults, and pre-specified escalation routing for the relevant cross-organizational relationships can participate in time-sensitive FAI events with minimal per-event overhead. The per-event governance labor is small: confirm the event falls within the standing configuration's scope, initiate automated record generation, execute. The governance is thorough; the per-event burden is low because the governance work was done earlier.

**Unprepared governance.** A Self without pre-authorization infrastructure — no standing configurations for the event class, no pre-authored orchestration rules, no pre-specified escalation routing — cannot participate in a time-sensitive FAI event without one of two outcomes: either the event is delayed until governance infrastructure is established, or the event proceeds as an ungoverned event. The architecture prescribes the former. Time pressure that reveals unprepared governance is a signal that governance infrastructure investment is needed, not a justification for ungoverned events.

**Governance infrastructure as a preparation investment.** The pre-authorization mechanisms are not emergency equipment assembled when urgent events arise. They are standing infrastructure assembled deliberately, at a time when governance cycles are available, so that urgent events when they arise have pre-authorized governance rails to operate on. The preparation investment is paid once per event class; it amortizes across all subsequent events of that class. A Self that invests consistently in standing configurations and comprehensive orchestration rules over time builds the capacity to handle time-sensitive coordination as governed events without per-event overhead.

---

## 6. Anti-pattern: time-pressure governance bypass

The time-pressure governance bypass is the pattern of proceeding with a FAI event under time pressure by skipping governance requirements, rationalizing the bypass with urgency. It is the inter-Self analog of the urgency rationalization that Paper 1 guards against in cell governance: the structural argument that exceptional circumstances justify departing from the governance commitments the architecture is built on.

The bypass anti-pattern takes several surface forms. In each, the governance failure is the same: the floor requirement is absent, and urgency is offered as the reason the requirement can be absent.

The most direct form is explicit omission: the event proceeds without an authored configuration, or without conflict registration, or without a construction record, because there is no time to produce them. The rationalization is: "this is an exception; the urgency is real; governance can be reconstructed after the fact." Post-event reconstruction does not satisfy the floor. Reconstruction is not the same as the record that would have been produced if governance had been operating; it is a retrospective artifact that cannot carry the properties the floor requires.

A less direct form is scope extension: a standing configuration that was authorized for one event class is applied to an event outside its scope, rationalizing that the standing configuration is close enough. This form preserves the appearance of pre-authorization while violating the joint authorization requirement. The standing configuration authorizes the event class it was authorized to cover; it does not authorize event classes that were not included in the joint authorization.

A third form is conflict suppression under time pressure: conflicts that arise during the event are resolved silently or averaged rather than registered as first-class objects, rationalizing that registration overhead is too slow. This form violates the conflict registration requirement of the floor even when every other requirement is satisfied.

The architecture's answer to all three forms is the same: build pre-authorization infrastructure for the urgency case; do not bypass governance when urgency arrives. A Self that consistently encounters time-pressure governance bypass situations has a governance preparation problem, not a governance floor problem. The floor is not the obstacle; inadequate pre-authorization infrastructure is.

---

## 7. Operational test

For a time-sensitive FAI event that completed rapidly, an observer can verify compliant governance and identify the pre-authorization mechanisms that enabled it by examining the following:

1. Does an authored configuration exist as substrate content? If the event used a standing configuration, is the event within the standing configuration's explicitly authorized scope? — *Verifies: authored configuration requirement; tests standing configuration scope discipline.*

2. Does a construction record exist, produced at or near event initiation, capturing the configuration reference, participating Selves, and initiation timestamp? — *Verifies: construction record requirement; tests automated record generation.*

3. Are all conflicts that arose during the event registered as first-class substrate objects? Are conflicts that fell outside the pre-authored orchestration rules' coverage present as carry-through objects flagged for post-event review? — *Verifies: conflict registration requirement; tests comprehensiveness of orchestration rules.*

4. Does a dissolution record exist, capturing the event outcome, content propagated to each home substrate, and dissolution timestamp? — *Verifies: dissolution record requirement; tests automated record generation at closure.*

5. Does every element of substrate content carry contribution attribution traceable to the contributing Self? — *Verifies: contribution attribution requirement.*

6. Were all conflicts resolved through pre-authored tier logic or carry-through default, with no improvised resolution or silent suppression? — *Verifies: comprehensive orchestration rules (Mechanism 2) operated correctly.*

7. If escalation occurred, did it reach the appropriate governance authority through a pre-specified channel, with no per-event routing negotiation? — *Verifies: pre-specified escalation routing (Mechanism 3) operated correctly.*

An event that satisfies all seven checks is a compliant governed time-sensitive FAI event. An event that fails any check is non-compliant. Failures at checks 1–5 are floor violations. Failures at checks 6–7 are pre-authorization infrastructure failures that, depending on how they were handled, may also produce floor violations.

Where an event satisfies all checks and the pre-authorization mechanisms are identified, the appropriate observation is: this event was compliant because governance was pre-authorized, not because governance was bypassed. The speed of compliance is a property of the pre-authorization infrastructure, not evidence that governance requirements were relaxed.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

---

## How to cite this note

Li, W. (2026). *FAI Governance for Time-Sensitive Coordination.* May 15, 2026. ORCID: 0009-0004-8065-3235.
