# The Temporal Property of Governance: At-Any-Time Availability of the Three Rights in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 1 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one of the two qualifiers the source paper places on the human-governed commitment's three rights — the **temporal property** — as a standalone architectural commitment, paired with the architectural-property qualifier formalized in a sibling derivation note. Together the two qualifiers exhaust the property-axis decomposition of human-governed.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern's "human-governed" commitment names three rights — to inspect, to modify, and to override substrate content and orchestration rules — and qualifies them with two architectural conditions: that the rights be available as a property of the system's design (the *architectural property*), and that they be available at any time during the substrate's existence (the *temporal property*). A separate note formalizes the architectural property. This note formalizes the temporal property as standalone. The motivation is that the temporal property is the most common point at which deployments add seemingly-reasonable gating that violates the architecture: scheduled review windows, audit cycles, designated change-management periods, and approval-gated checkpoints, each of which converts the temporal commitment from "at any time" to "at certain times." Naming the temporal property as standalone is what makes such conversions visible as architectural compromises rather than as harmless process additions. The note states the commitment in five operational components, distinguishes it from five adjacent commitments commonly conflated with it, situates it relative to the architectural property and the linear-cost commitment, enumerates the failure modes that violate the temporal property specifically, and provides an operational test.

## 1. Why the temporal property needs to be formalized as standalone

The CKS pattern's "human-governed" commitment names three rights — inspect, modify, override — and qualifies them with two architectural conditions. The first condition says the rights must be available as a property of the system's design, not as a procedural promise that depends on a particular deployment, vendor, or workflow; the second says the rights must be available at any time, not only at predetermined checkpoints (§3.3 of the source paper). A sibling derivation note formalizes the first qualifier as the architectural property. This note formalizes the second qualifier as the temporal property.

The two qualifiers are independent. A system can satisfy the architectural property — the rights exist in the system's design rather than as a procedural promise — and still fail the temporal property if the architectural design itself imposes time gates (a system designed to grant the three rights only during scheduled review windows). A system can satisfy the temporal property — the rights are nominally always available — and still fail the architectural property if the always-available access depends on a workflow commitment rather than on the system's design (read access continuously provided by an operations team's promise, not by the architecture). Both failure patterns produce CKS-non-coherent systems on the human-governed axis, so each qualifier needs standalone formalization.

A second motivation is more practical. The temporal property is the most common point at which deployments add seemingly-reasonable gating that violates the architecture. Scheduled review windows, audit cycles, designated change-management periods, and approval-gated checkpoints are widespread in organizational governance; each of them, applied to architectural governance, converts the temporal property from "at any time" to "at certain times," which the architecture does not commit to. Naming the temporal property as standalone is what makes these conversions visible as architectural compromises rather than as harmless process additions.

## 2. The temporal property, defined precisely

In the CKS pattern, a substrate's human-governed commitment satisfies the **temporal property** if and only if the three rights — inspect, modify, override — are available to authorized humans at any moment they choose, during the substrate's existence, without architectural gating on time, schedule, checkpoint, window, condition, or designation. The commitment has five operational components.

**(a) Continuous availability during the substrate's existence.** From the moment the substrate is created to the moment it is decommissioned, the three rights are exercisable. There are no intervals during the substrate's life when governance is architecturally unavailable.

**(b) Exercise at the human's chosen moment.** The human, not a process, chooses when to exercise governance. This is the at-any-time content of the commitment: the architecture does not impose its own timing on when governance can be exercised.

**(c) No qualifying conditions.** The architecture does not commit governance availability to any condition — incident declaration, scheduled review, batched intervention, designated change window, organizational alignment, or other qualifying state. The commitment is unconditional within the architecture's scope.

**(d) Survival across substrate evolution.** As the substrate grows, ages, accumulates content, and accumulates change history, the three rights remain available across all of it. There is no temporal threshold past which substrate content becomes architecturally beyond governance reach.

**(e) Present-moment exercise.** A human exercising the inspect right reads substrate content as it is now; a human exercising the modify right writes substrate content effective now; a human exercising the override right intervenes in substrate state now. Past states may be inspectable through provenance metadata (§3.1 of the source paper); future states are determined by present writes; the architectural commitment is to the present moment as the moment of governance exercise.

The five components together define what makes governance temporally available in the architectural sense. Failing any one, even with the other four robustly satisfied, fails the temporal property.

A scoping point belongs here. The temporal property does not require humans to be available at all times; it requires the architecture to be available whenever the human chooses. A deployment may have governance roles exercised infrequently, by humans themselves only available during business hours; the temporal property is preserved as long as the architecture does not force this — as long as the same human exercising governance at 3 AM Sunday has the same rights as the same human exercising governance at 10 AM Tuesday.

## 3. What the temporal property is NOT

Five adjacent commitments are commonly conflated with the temporal property. Each is a real and reasonable commitment in some other architecture; naming what the temporal property is not is what prevents the misreading.

**Not high availability.** High availability in operational systems names a commitment to system uptime — typically expressed as percentages (99.9%, 99.99%) or as outage budgets. High availability addresses what fraction of clock time the system is operational; the temporal property addresses when governance is exercisable during the system's operational time. A system with 99% uptime can satisfy the temporal property during the 99% of clock time it is operational, provided governance is exercisable continuously during that operational time. A system with 100% uptime that gates governance on scheduled review windows fails the temporal property despite having no operational outages.

**Not 24/7 operations.** 24/7 operations names a commitment that human operators are continuously available to operate the system. The temporal property does not require 24/7 human operators; it requires that whichever humans hold governance authority can exercise that authority whenever they choose, whether that is during business hours, at 3 AM, or after a long absence. A deployment with business-hours-only operations can satisfy the temporal property if governance during those hours is at the operator's discretion, not at a process's discretion.

**Not real-time access.** Real-time access typically means access with low latency — sub-second response, immediate feedback, synchronous interaction. The temporal property does not require specific latency characteristics; it requires architectural availability. A substrate hosted in a system with multi-second query latency can satisfy the temporal property if the latency is operational rather than gating, and if the human's choice of when to query is unconstrained by architectural scheduling.

**Not on-demand provisioning.** On-demand provisioning in cloud and infrastructure systems means resources can be requested and allocated as needed. The temporal property does not require provisioning patterns; it requires that whatever resources the substrate has, the three rights are exercisable on them whenever the human chooses. A system with rich on-demand provisioning can fail the temporal property if the architectural governance over the provisioned substrate is scheduled rather than at-any-time.

**Not pre-scheduled review cycles.** Many governance frameworks impose review cycles — quarterly governance reviews, monthly audits, weekly steering meetings. These cycles are reasonable in their context; what they cannot do is constitute the architectural temporal property. Pre-scheduled review cycles define when reviews happen; the temporal property requires that governance is exercisable when the human chooses, which is compatible with cycles being one occasion among many but not compatible with cycles being the only occasion.

The five adjacent commitments can coexist with the temporal property. What the temporal property requires is that none of them substitute for it.

## 4. Relation to the architectural property

The architectural property and the temporal property work together to make governance defensible against a specific failure mode: the conversion of architectural governance into process-gated governance through scheduling. A system can satisfy the architectural property — the rights exist in the architecture rather than in process — and still fail the temporal property if the architecture itself imposes timing constraints. The architectural property addresses *what kind of guarantee* governance is; the temporal property addresses *when the guarantee holds*.

The two properties are particularly tightly coupled around scheduled-window patterns. A scheduled review window can be defended as architectural ("this system is designed to support reviews at these intervals") while still violating the temporal property ("governance is only available at these intervals"). The architectural property by itself does not prevent this; the temporal property is what does. The pair-axis decomposition — architectural property paired with temporal property — is what makes the full content of A1.01's qualifiers on the three rights defensible against this failure pattern.

A system that satisfies both qualifiers is one where governance is architectural and continuously available; a system that satisfies one but not the other has a partial commitment that fails under specific conditions.

## 5. Relation to the linear-cost commitment

The source paper's linear-cost commitment (Claim 5) names governance cost as paid at two moments — rule authoring and direct override — each growing with its own cost dimension (rule variety and intervention frequency) (§6.3). The cost model assumes governance is exercised when the deployment chooses, not when the architecture forces. Scheduled-batch governance — governance gated on review windows or audit cycles — introduces a third cost dimension the architecture does not commit to: the cost of batching, scheduling, and managing the windows themselves.

The temporal property forecloses this third cost dimension. If governance is exercisable at any time, then governance cost grows only with rule variety and intervention frequency, and not with the additional process overhead of batching governance into scheduled occasions. Deployments may add scheduled governance occasions on top — for example, a quarterly review where multiple governance actions are bundled — but these are deployment additions, not architectural requirements.

The temporal property is what makes the cost model defensible against the misreading that scheduled governance is what makes governance affordable at scale. The architecture's claim runs the opposite direction: at-any-time governance is what makes governance cost not size-proportional, because scheduled governance introduces process cost that the architectural at-any-time commitment avoids.

## 6. Failure modes that violate the temporal property

A system can fail the temporal property specifically, even when it satisfies the architectural property and the broader human-governed commitments in some other respect. Six failure modes name the most common ways this happens.

**(a) Scheduled-window governance.** When governance is exercisable only during designated review windows, change-management periods, or audit cycles, the at-the-human's-chosen-moment component is violated. The window may be wide; what the commitment forbids is the architectural existence of the window as a precondition.

**(b) Condition-gated governance.** When governance is exercisable only when specific conditions hold — incident declared, organizational state aligned, designated personnel present, qualifying circumstances met — the no-qualifying-conditions component is violated. The condition may be reasonable; what the commitment forbids is its architectural status as a gate.

**(c) Retrospective-only governance.** When governance can only be exercised after-the-fact, against substrate states that are already historical, and not against current substrate state, the present-moment component is violated. Retrospective review is a useful adjacent activity; what the commitment forbids is the architectural denial of present-moment governance.

**(d) Prospective-only governance.** When governance can only be exercised pre-deployment or pre-execution, before substrate content takes effect, and not against substrate state once it is operational, the continuous-availability component is violated. Pre-deployment review is a useful adjacent activity; what the commitment forbids is the architectural restriction of governance to pre-deployment moments.

**(e) Aging substrate beyond governance reach.** When substrate content past a certain age is architecturally beyond the governance commitments — not modifiable, not overridable — the survival-across-substrate-evolution component is violated. Archive policies are useful; what they cannot do is convert old substrate content into architecturally ungoverned content.

**(f) Session-scoped governance.** When the three rights are only available during designated sessions (workshop sessions, review sessions, change sessions) and unavailable outside them, the at-any-time content of the commitment is violated. Sessions may be useful organizational tools; the architecture does not commit to governance being session-scoped.

A system that exhibits any of (a)–(f) does not implement the temporal property in the architectural sense, and naming the failure precisely is what allows downstream remediation.

## 7. Operational test

A system implements the temporal property if and only if all of the following are true at all times during the substrate's existence:

1. The three rights (inspect, modify, override) are exercisable by authorized humans at any moment they choose, during the substrate's operational time, without architectural gating on schedule, window, cycle, or session.
2. The architecture imposes no qualifying conditions on governance exercise — no incident declaration, no organizational state requirement, no designated-personnel constraint, no special-circumstance flag.
3. The rights are available across the full lifecycle of substrate content, from creation to decommission, with no architectural threshold past which content becomes beyond governance reach.
4. The rights are exercisable in the present moment against current substrate state, not only retrospectively against historical state or prospectively against future state.
5. Operational events that temporarily affect substrate availability (planned maintenance, backup windows, vendor outages) do not constitute architectural temporal gating; the temporal property is satisfied if the architecture commits to at-any-time governance during operational time, even if operational time is not 100%.

A system that fails any of (1)–(5) does not implement the temporal property in the architectural sense, even if it supports governance in some other temporal pattern. Such a system may be useful — and may be appropriate for deployments that genuinely need scheduled governance — but is not CKS-coherent on the temporal axis.

## 8. Why naming the temporal property as standalone matters

Implementations that gate governance on schedule produce systems where humans needing to exercise authority must wait for the architecture's timing, with consequences for both responsiveness (governance delayed when situations require it) and cost (the scheduling apparatus itself is expensive to maintain). Implementations that gate governance on conditions produce systems where the qualifying condition itself becomes a contested object — when is an incident really an incident, when are circumstances really qualifying — which the architecture is not designed to adjudicate. In each case governance becomes something the architecture itself can defer, deny, or condition, rather than something that remains continuously available as a property the architecture commits to.

Implementations that conflate the temporal property with high availability, real-time access, or on-demand provisioning produce a different misframing: governance treated as an infrastructure problem ("we need better uptime to support governance") rather than as an architectural commitment ("we need at-any-time governance availability as a property of the architecture, regardless of infrastructure characteristics"). Better uptime is generally desirable, but it is not what the temporal property commits to. The architectural commitment holds independently of how robust the infrastructure underneath is, and is violated independently of how robust that infrastructure is.

Naming the temporal property as standalone — paired with the sibling note's treatment of the architectural property — exhausts the property-axis decomposition of A1.01's qualifiers on the three rights. The two notes together formalize the full content of "as a property of the system's design" and "at any time" as architectural commitments, with each commitment defending against different failure modes. With both notes in place, the property-axis decomposition of human-governed is locked down: governance must be architectural (not procedural) and temporally unconstrained (not scheduled), and any system claiming architectural human governance must satisfy both.

Subsequent work that adopts, extends, composes with, or argues against the CKS human-governed commitment should treat the temporal property in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Temporal Property of Governance: At-Any-Time Availability of the Three Rights in the Coordination Knowledge Substrate Pattern.* 1 May 2026. ORCID: 0009-0004-8065-3235.
