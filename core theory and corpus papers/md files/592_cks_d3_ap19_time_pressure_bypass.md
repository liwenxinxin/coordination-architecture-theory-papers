# AP-19: Time-Pressure Governance Bypass

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** D3 — Phase D3 Anti-Pattern Catalog (Paper 3 Derivation)
**Note number:** #592 (D3.17 — Taxonomy Category 4, Configuration Failures — closing note)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes AP-19 (Time-Pressure Governance Bypass), the fifth and final anti-pattern in Taxonomy Category 4 (Configuration Failures) of the Phase D3 catalog. AP-19 describes a failure mode in which governance practitioners invoke urgency as a justification for skipping Full Aspect Integration (FAI) governance requirements — proceeding without authored configuration, pre-construction authorization, or conflict registration because a compressed timeline makes those steps feel impractical. The note establishes that the human-governed authority commitment (Paper 1 Claim 3) does not contain an urgency exception: the three rights — to inspect, to modify, and to override — apply at all times and are not suspended by time pressure. The architecture's response to urgency is pre-authorization infrastructure, not governance suspension. The note further establishes that the primary long-term risk of AP-19 is normalization: organizations that accept urgency as a bypass justification train governance practitioners to treat governance as optional when inconvenient, a cultural erosion that is more damaging than any individual event's governance deficit. The resolution is explicit: urgency produced by the absence of pre-authorization infrastructure is a governance preparation failure, and the correct response is to delay the event until infrastructure is ready.

---

## 1. Anti-Pattern Name and Category

**Anti-pattern:** AP-19 — Time-Pressure Governance Bypass
**Category:** Taxonomy Category 4 — Configuration Failures
**Position:** Fifth and final Category 4 anti-pattern; closes Category 4 in the D3 catalog.
**Relationship to prior Category 4 anti-patterns:** AP-15 through AP-18 document failures of authored configuration content — absent configuration (AP-15), misconfigured scope (AP-16), authority boundary erosion (AP-17), and standing configuration misuse (AP-18). AP-19 documents a distinct failure mode: the rationale used to justify skipping configuration authoring altogether. Where AP-15 describes what is missing, AP-19 describes why practitioners believe they are permitted to omit it.

---

## 2. Description

A Full Aspect Integration (FAI) event must occur on a compressed timeline. Rather than relying on pre-authorization mechanisms — standing configurations, pre-authorized orchestration rules, standing cross-organizational agreements — to enable rapid compliant participation, governance practitioners rationalize skipping governance requirements because of urgency. The event proceeds with implicit configuration (the failure mode of AP-15/AP-6), without pre-construction authorization, or without conflict registration — justified by the claim that there was insufficient time to meet governance requirements. The urgency argument becomes the operative basis for suspending governance commitments.

The formal structure of AP-19 is a rationalization, not merely an oversight. In AP-15, practitioners fail to author configuration; the gap may be inadvertent. In AP-19, practitioners make an explicit judgment that urgency excuses the gap. This distinction matters architecturally: the rationalization imports a claim about the governance architecture — that urgency creates an exception — that the architecture does not support. Governance practitioners who invoke AP-19 have an incorrect understanding of Paper 1 Claim 3.

The urgency invoked in AP-19 may arise from two sources, which must be distinguished because their diagnoses and resolutions differ:

**External urgency:** A genuine time constraint imposed by an external event — a partner organization's deadline, a regulatory window, an operational emergency. External urgency is real pressure on the timeline. The correct response is to use pre-authorization infrastructure that was established before the event arose, enabling rapid compliant participation without per-event governance work.

**Infrastructure-gap urgency:** A time constraint that arises because the pre-authorization infrastructure necessary for rapid compliant participation does not exist. The organization has not authored standing configurations, has not pre-authorized orchestration rules, and has not established cross-organizational governance agreements. When a time-sensitive event arrives, there is no compliant fast path available. The urgency is not external; it is a consequence of governance preparation failure. This category of urgency is not a justification for bypass; it is a diagnostic signal that investment in pre-authorization infrastructure is required.

Both categories produce the same observable behavior — governance requirements are skipped under urgency justification — but they represent distinct organizational situations. The resolution section below addresses each.

---

## 3. Detection Criteria

The following conditions, individually or in combination, indicate that AP-19 may be present:

- FAI governance records are sparse or absent for an event that was explicitly time-sensitive, with no pre-authorization reference explaining how the rapid timeline was accommodated compliantly.
- Governance records contain urgency justifications ("insufficient time for full authorization," "emergency circumstances," "expedited review required") rather than references to pre-existing standing configurations or pre-authorized orchestration rules that enabled rapid participation.
- The event lacks the pre-authorization infrastructure — standing configuration, pre-authorized rules, standing cross-organizational agreements — that would have enabled rapid compliant participation. The absence of infrastructure explains why bypass was chosen.
- A pattern of urgency-justified governance gaps across multiple events, suggesting practitioners have learned that urgency is an accepted justification for bypassing governance. This pattern-level signal is the most serious detection criterion: it is not the sign of individual failures but of organizational normalization.
- Urgency justifications that reference the timeline of an event without referencing any effort to establish pre-authorization infrastructure as a forward-looking corrective. An organization that bypasses governance under urgency and then invests in pre-authorization infrastructure has committed an AP-19 instance but is moving toward resolution. An organization that bypasses governance under urgency without corrective investment is normalizing the pattern.

---

## 4. Governance Commitment Violated

**Primary commitment violated:** Paper 1 Claim 3 — human-governed authority.

Paper 1's human-governed commitment names three rights that humans retain over substrate content and orchestration rules: the right to inspect, the right to modify, and the right to override. These rights are architectural: they must be available as a property of the system's design, not as a procedural promise. They are also temporal: they must be available at any time during the substrate's existence, not only at predetermined checkpoints.

The temporal scope of the commitment is the load-bearing property for AP-19. The human-governed commitment does not contain an urgency exception. It does not state that the three rights apply "except when time pressure makes them impractical." It does not recognize urgency as a condition that suspends governance requirements. A governance practitioner who proceeds through an FAI event without authored configuration because urgency made configuration authoring feel impractical has not satisfied the commitment; the practitioner has bypassed it while believing the bypass is architecturally permitted.

This is the sharpest statement this note offers: urgency does not suspend the human-governed authority commitment. The architecture is silent on urgency as a governance exception because it accommodates urgency through a different mechanism entirely — pre-authorization, not suspension.

**Secondary commitment violated:** Paper 3 Claim 5 — configuration as substrate content.

Paper 3 Claim 5 commits to FAI configuration on the same architectural plane as other substrate content: authored, versioned, inspectable, subject to the three rights. Urgency does not exempt configuration from this requirement. If there is no time to author configuration for a specific event, the correct response is to use a standing configuration authored before the event. If no standing configuration exists, the governance infrastructure is not ready for urgent events — which is a preparation failure, not a justification for proceeding without configuration.

**Operational reference:** D2.41 (time-sensitive governance). The derivation note D2.41 establishes the architectural accommodation of time pressure: governance work is moved forward in time through pre-authorization, not removed from the critical path through bypass. D2.41 is the positive specification of which AP-19 is the negative violation.

---

## 5. Consequences

**Immediate consequence:** Every governance decision in the event that proceeded under urgency bypass carries the same deficits as AP-15 (implicit configuration). There is no authored configuration foundation. The scope is ambiguous. Boundary authority is undocumented. Conflicts are not registered or preserved. The event's governance record cannot support path retraceability. These are the same harms AP-15 produces; AP-19 adds a justification layer but does not reduce the damage.

**The normalization consequence — the primary long-term risk:** A single urgency bypass is a governance failure localized to one event. A pattern of accepted urgency bypasses is a governance architecture failure. The critical mechanism is social: if an urgency bypass is accepted — if governance practitioners observe that urgency justification was raised, the event proceeded, and no corrective consequence followed — they update their understanding of the governance architecture. They learn that urgency creates an exception. The bar for invoking urgency as justification then lowers over time. The first bypass requires a genuine emergency. The second requires a significant time constraint. By the fifth, urgency is invoked for any event where governance requirements feel burdensome. Governance quality degrades not through a single failure but through accumulated normalization of an exception that the architecture does not recognize.

The normalization dynamic is self-amplifying in a specific way: each accepted bypass makes the next bypass easier to rationalize, because practitioners can point to precedent. Organizations that have experienced multiple urgency bypasses without corrective response develop an informal governance norm — "we move fast when we have to" — that directly conflicts with the architecture's commitment. Reversing this norm requires active organizational effort; it does not correct itself.

**The organizational culture consequence:** Organizations that normalize urgency bypasses communicate to governance practitioners that governance is optional when inconvenient. This message is not necessarily explicit; it is embedded in what is accepted without consequence. A governance practitioner who sees urgency bypass tolerated learns that governance is a fair-weather commitment — maintained when timelines are comfortable, suspended when they are not. This understanding undermines governance commitment throughout the organization, not only in time-sensitive contexts. The cultural damage extends beyond FAI events to every context where governance requirements feel burdensome. The organizational culture consequence is the most damaging long-term consequence of AP-19 because it is not bounded to the specific failure mode: it generalizes the lesson that governance is negotiable.

---

## 6. Intra-Self Analog

Paper 1's commitment to human-governed authority applies at intra-Self scope as well as at inter-Self scope. AP-19 does not arise exclusively in FAI coordination between multiple organizational Selves; it arises wherever governance requirements exist and time pressure provides a rationalization for bypassing them.

At intra-Self scope, the analog is a governance practitioner who skips orchestration rule authoring because a cell needs to execute quickly. The practitioner proceeds with an implicit rule — one that has not been authored, versioned, or authorized — because there was no time to author one explicitly. The bypass is the same anti-pattern at a different scope: urgency is invoked to justify skipping a governance requirement that the architecture does not suspend under urgency.

The architecture's answer at intra-Self scope is identical to its answer at inter-Self scope: pre-authorization. If a cell type is expected to execute under time pressure, the orchestration rules for that cell type should be authored before the pressure arrives. Standing orchestration rules enable rapid compliant execution without per-event rule authoring. The urgency bypass is never the correct path; the correct path is standing infrastructure established before urgency arises.

The intra-Self analog establishes a broader principle: AP-19 is not a failure mode specific to cross-organizational FAI coordination. It is a failure mode that can appear at any scope where the human-governed commitment applies and time pressure provides an available rationalization. Category 4's closing anti-pattern is, in this sense, a universal configuration failure pattern — the one that uses urgency to license all other configuration failures.

---

## 7. Resolution

The resolution to AP-19 is fully specified by D2.41 (time-sensitive governance) and the pre-authorization infrastructure it establishes. Three mechanisms are available:

**Standing configurations (D2.21).** A standing configuration is an authored, authorized configuration that applies across a class of events without per-event authoring. Organizations that anticipate time-sensitive FAI events should establish standing configurations for the event types they expect to face. When urgency arrives, the standing configuration enables rapid compliant participation: configuration authoring has already occurred, authorization has already been granted, the substrate content foundation is already in place. The urgency is absorbed by the standing configuration, not by governance bypass.

**Pre-authorized orchestration rules (D2.15 standing scope).** For organizations that participate in recurring FAI coordination, pre-authorized orchestration rules eliminate real-time conflict governance overhead. Rules that apply across a standing coordination relationship are authored and authorized before any specific event. When time-sensitive events occur within that relationship, the governance infrastructure is ready. There is no per-event governance work to skip.

**Pre-construction authorization.** Where a specific event type is anticipated, authorization work can be completed before the event begins. Pre-construction authorization does not require knowing the event's specific parameters; it requires knowing enough about the event type to authorize a class of configurations in advance. This is the forward-in-time movement D2.41 specifies: governance work is moved earlier, not removed.

**When pre-authorization infrastructure does not exist:** The most important resolution point concerns the case where urgency arises precisely because no pre-authorization infrastructure is in place. The event is time-sensitive. No standing configuration exists. No pre-authorized rules apply. There is no compliant fast path. What is the correct response?

The correct response is to delay the event until the infrastructure is in place. This is the answer the architecture requires, and it is the answer that practitioners find most difficult to accept.

The difficulty is real but does not alter the architecture. Urgency created by inadequate governance infrastructure preparation is not a justification for bypassing governance — it is a signal that pre-authorization infrastructure investment is required. An organization that accepts urgency bypass in this situation is choosing to proceed with governance debt rather than to invest in governance infrastructure. That choice produces the immediate governance deficits of AP-15 and the normalization consequences described in §5. An organization that delays the event instead accepts a short-term coordination cost in exchange for preserving the governance commitment and generating the organizational signal that pre-authorization infrastructure must be built.

The delay response is also the diagnostic response: it makes the infrastructure gap visible as a consequence with organizational weight. A bypass that is accepted makes the infrastructure gap invisible — the event succeeded, and no one is accountable for the absence of infrastructure. A delay that forces investment makes the gap visible and produces the investment that prevents the same situation from recurring.

Building pre-authorization infrastructure is not a one-time cost. It is an ongoing governance investment — maintaining standing configurations as coordination relationships evolve, updating pre-authorized rules as scope changes, establishing new cross-organizational agreements as new FAI relationships form. Organizations that treat pre-authorization infrastructure as a permanent governance priority will face fewer situations in which urgency creates pressure toward bypass. Organizations that defer infrastructure investment will face that pressure repeatedly, and each bypass makes the next one easier to accept.

---

## Closing Note: Category 4 in Context

AP-19 closes Taxonomy Category 4 (Configuration Failures). The five Category 4 anti-patterns together document the full space of configuration-related governance failures in FAI coordination:

- **AP-15** — Absent configuration: the event proceeds with no authored configuration.
- **AP-16** — Misconfigured scope: configuration is present but incorrectly specifies the coordination boundary.
- **AP-17** — Authority boundary erosion: configuration is present but does not maintain separation between home authority and shared authority.
- **AP-18** — Standing configuration misuse: a standing configuration is applied to an event outside its authorized scope.
- **AP-19** — Time-pressure governance bypass: configuration is absent because urgency was accepted as a justification for skipping configuration authoring.

AP-19 is the rationalization that licenses the other four. An organization that accepts urgency bypass as a governance exception may proceed with absent configuration (AP-15), may fail to scope it correctly under time pressure (AP-16), may blur authority boundaries when moving quickly (AP-17), or may over-extend a standing configuration rather than delaying for proper authorization (AP-18). Closing Category 4 with the rationalization pattern is architecturally accurate: urgency bypass is not one more configuration failure alongside the others — it is the justification structure that makes practitioners believe any configuration failure is acceptable.

The architecture's answer to that justification structure is direct. The human-governed authority commitment does not contain an urgency exception. It never has.
