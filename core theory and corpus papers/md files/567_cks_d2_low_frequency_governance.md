# FAI Governance for Low-Frequency and One-Time Events

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D2.71 addressed the governance requirements for organizations conducting Full Aspect Integration (FAI) events at high frequency, where standing configurations amortize governance burden across many events. D2.72 addresses the complementary case: organizations participating in FAI events infrequently — once per year or less — or only once. For these organizations, per-event configuration authoring is the governance mechanism, and the minimum viable governance floor (D2.37) is the practical governance target. This note defines the simplest architecturally valid FAI event — the conjunction of single-aspect contribution (D2.48), minimum configuration (D2.12), full dissolution as the persistence policy, and preserve-tier default for conflict handling — and establishes that floor as the threshold below which no governed FAI event exists. It then presents four practical recommendations for first-event governance: completing the onboarding checklist before the event, partnering with an experienced Self, accepting the preserve-tier default for conflict handling, and committing to a post-mortem after the event. The note closes by framing low-frequency governance as the natural entry point into FAI participation and identifying the anti-pattern of treating infrequency as an exemption from the governance floor.

---

## 1. D2.72 as the Complement to D2.71

D2.71 derived the governance requirements for organizations conducting FAI events at high frequency, where the governance burden per event is low because standing configurations — pre-authored aspect libraries, pre-authorized conflict orchestration rules, established joint-authority arrangements with regular partners — distribute the authoring cost across many events. For those organizations, the governance question is how to maintain and evolve standing infrastructure.

D2.72 addresses the complementary case. An organization that participates in FAI events once per year or less, or that is planning its first FAI event, does not have and cannot be expected to have standing governance infrastructure. Its governance approach must be per-event: the configuration for each event is authored specifically for that event, the joint-authority arrangement is negotiated specifically for that event, and the conflict handling is calibrated to what is achievable without pre-existing orchestration rule libraries.

The distinction matters because the governance design for low-frequency participation is different in character from high-frequency governance, even though the architecture is the same. Low-frequency governance concentrates its investment at each event rather than distributing it across a standing infrastructure. The total governance burden is low because events are rare; the per-event burden is higher than for high-frequency participants, but this is appropriate given that the events themselves are more self-contained.

Both cases share one invariant: the minimum viable governance floor applies regardless of event frequency. Low frequency is not an architectural category that grants exemption from governance requirements. It is an operational context that shapes how governance is exercised, not whether it is exercised.

---

## 2. Per-Event Configuration as the Governance Mechanism

Without standing configurations, a low-frequency participant must author the complete configuration for each FAI event before the event begins. Paper 3 §8 establishes that FAI configuration is substrate content under joint authority of participating Selves' governance; the configuration must be authored under that joint authority before the event commences, regardless of whether either participating Self has pre-existing configuration infrastructure.

Per-event configuration authoring covers the same dimensions that standing configurations cover for high-frequency participants. The critical dimensions that the minimum viable governance floor requires (D2.12) are: the sharing scope of the FAI event (what content from each participating Self's home substrate enters the shared substrate), the cardinality of participating Selves, and the persistence policy governing what remains after the event dissolves. At minimum, these three dimensions must be explicitly specified in the configuration before the event begins.

The governance burden of per-event configuration is highest on the first event, when the authoring organization has no prior event configurations to adapt and no accumulated experience with which conflict classes are likely to arise. It decreases with each subsequent event as the organization develops reusable configuration fragments, learns its conflict profile, and establishes relationships with partner Selves. This trajectory from per-event authoring toward standing infrastructure is the natural path of governance maturation for organizations that choose to increase FAI participation frequency.

For organizations that will remain low-frequency participants — one event per year, or events separated by long intervals — per-event authoring remains the appropriate governance mechanism indefinitely. The architecture does not require standing infrastructure; it requires that whatever configuration exists for each event satisfies the governance floor.

---

## 3. The Simplest Valid FAI Event

D2.37 (minimum viable governance) and D2.48 (single-aspect contribution) together define the simplest architecturally valid FAI event. This conjunction is architecturally significant: it establishes the prior-art floor below which no event is a governed FAI event in the Paper 3 sense. Everything below this floor — sub-aspect contribution, unconfigured events, events with no conflict registry — falls outside the architecture.

The simplest valid FAI event has five components:

**One Self contributes one aspect.** D2.48 establishes that single-aspect contribution is the minimum meaningful unit of FAI participation. Below the aspect, contribution is at sub-aspect granularity — individual cells rather than purpose-defined arrangements of cells. Sub-aspect contribution does not constitute FAI because the aspect is the unit of exchange Paper 3 §5 commits to; cells alone surface fragments below purpose-coherence, and the reconstitution of the structural arrangement at the receiving side that §5 requires operates at aspect scope, not cell scope.

**Three critical dimensions are configured (D2.12).** The minimum configuration specifies sharing scope, cardinality, and persistence policy. These three dimensions must be explicitly specified as substrate content under joint authority before the event begins. An event without explicit configuration for these dimensions is not a governed FAI event; configuration omissions are not resolvable by default inference.

**Full dissolution as the persistence policy.** The minimum valid persistence policy is full dissolution: upon the event's conclusion, the shared substrate exits operation and no shared substrate content persists beyond what each participating Self ingests into its home substrate via the four-locus evolution-feed mechanism (Paper 3 §7). Full dissolution is governance-appropriate for a first event because it bounds the scope of what the participants must govern after the event ends. More complex persistence policies — retaining the full shared substrate as a durable inter-organizational record, for example — impose ongoing governance obligations that a first-event participant may not be prepared to meet.

**Full merger as the default.** Paper 3 §5 establishes full merge as the architectural default at inter-Self scope: contributed aspects merge into the shared substrate with conflict preservation as the mechanism for handling incompatibilities. The simplest valid event accepts this default without configuring selective merge variants. Selective merge is one of three configurable pattern variants; choosing it requires governance experience with the conflict classes likely to arise, which a first-event participant typically does not have. Full merger with conflict preservation achieves the coordination purpose of the event while keeping the governance obligation at the floor.

**Preserve-tier default for conflict handling.** The three-tier conflict-handling mechanism (preserve / resolve via orchestration / escalate to humans) operates in ascending order of governance sophistication. At the floor, conflicts are routed primarily to the preserve tier: they surface as first-class substrate state in the shared substrate and carry through as evolution-feed annotations to each participating Self's home substrate via the four-locus mechanism. The preserve tier requires no authored orchestration rules for the conflict classes it handles; it is the tier available to a participant without a pre-existing conflict rule library.

This conjunction of five components defines what constitutes an architecturally valid governed FAI event at minimum scope. An event satisfying all five is Paper 3 compliant at the floor. An event failing any one of the five is not a governed FAI event; it may be some other form of inter-organizational coordination, but it is not FAI under the Paper 3 architecture.

---

## 4. Four Practical Recommendations for First-Event Governance

Four recommendations address the practical governance challenges a first-event or low-frequency participant faces. Each recommendation is architecturally grounded; none introduces obligations beyond the architecture, and none waives floor requirements.

### Recommendation 1: Complete the Onboarding Checklist First (D2.69)

D2.69 derived the onboarding checklist for organizations preparing to participate in FAI events. The checklist verifies governance readiness before the first event begins: it confirms that the organization's home substrate has the structural prerequisites for FAI participation, that the governance authority arrangement the event requires has been established, and that the minimum configuration dimensions can be specified. Even for a one-time event, completing the onboarding checklist before the event is not optional procedure — it is the mechanism by which the organization verifies that the minimum viable governance floor is achievable. An organization that skips the checklist and proceeds directly to the event has no verification that the floor requirements are met.

### Recommendation 2: Partner With an Experienced Self

Pairing with a Self that has prior FAI experience and comprehensive standing configurations substantially reduces the governance burden on the inexperienced participant. The architectural grounding for this recommendation is in the joint-authority structure of FAI configuration: configuration is substrate content under joint authority of participating Selves' governance, which means either participant may propose the configuration for the other to review and authorize.

An experienced Self with pre-existing configuration infrastructure for common FAI scenarios can propose a configuration that the inexperienced Self reviews and authorizes, rather than requiring the inexperienced Self to author the configuration from scratch. The inexperienced Self's governance role shifts from authoring to reviewing: it verifies that the proposed configuration satisfies its own governance interests, confirms that the sharing scope appropriately bounds what content enters the shared substrate from its home substrate, and authorizes the configuration by the same joint-authority mechanism Paper 3 §8 commits to. This is not a delegation of governance authority; it is an exercise of governance authority at the review-and-authorize stage rather than the author stage. The governance authority of the inexperienced Self over the configuration is undiminished.

The experienced Self's pre-authorized orchestration rules, if they exist for the conflict classes the event is likely to surface, are also available as shared substrate content under joint authority. Where both participants agree that those rules are appropriate for the event, they can be incorporated into the shared substrate's orchestration layer without the inexperienced participant needing to author its own rules for the same conflict classes. This is the mechanism by which the partnership reduces the governance burden at the resolve-via-orchestration tier, allowing the inexperienced participant to begin with functioning conflict handling beyond the preserve tier without the authoring investment it would otherwise require.

### Recommendation 3: Accept the Preserve-Tier Default

For first events, routing most conflicts to the preserve tier rather than authoring conflict resolution rules for the resolve-via-orchestration tier is governance-appropriate. The basis for this recommendation is the experience prerequisite for effective orchestration rule authoring.

Authoring orchestration rules for a conflict class requires knowing what the conflict class looks like, how often it arises, what resolution logic is likely to produce acceptable outcomes for both participants, and what the governance boundary conditions are for that resolution logic. This knowledge is accumulated through event experience; a first-event participant does not have it. Conflict rules authored without this knowledge are likely to be underspecified, misspecified for the actual conflict classes that arise, or over-scoped in ways that produce unintended resolution outcomes.

The preserve tier requires none of this knowledge. Conflicts are preserved as first-class substrate state — the divergence is identified, both participants' positions are retained distinct, and provenance is attached. The preserved conflicts carry through as evolution-feed annotations to each participant's home substrate via Paper 3 §7's four-locus mechanism. Within the home substrate, each participating Self determines how to treat the annotated boundary under its own governance: as a place to do further work, as a place to leave the divergence in place, or as a place to escalate. The governance quality of the preserve tier is appropriate for first-event participants: it achieves conflict registration without requiring the orchestration rule authoring that effective conflict resolution demands.

The preserved conflicts also have learning value for future events. The conflict classes that surface during the first event, captured as evolution-feed annotations in the home substrate, are the empirical basis on which the organization can author orchestration rules for subsequent events. Accepting the preserve-tier default on the first event is therefore not a permanent limitation; it is the governance-appropriate starting point that generates the experience needed to improve on the second event.

### Recommendation 4: Commit to the Post-Mortem

D2.39 derived the post-mortem review as a governance mechanism for evaluating FAI event outcomes and informing future configuration. For a first-event or low-frequency participant, the post-mortem is particularly valuable because the event generates experience the organization did not have before it.

The post-mortem examines what the event produced in terms of governance learning: which conflict classes arose, how the preserve-tier handling performed, whether the sharing scope was appropriately calibrated, whether the configuration dimensions were correctly specified, and what the evolution-feed annotations reveal about coordination boundaries the home substrate must address. If the organization anticipates future FAI events — even infrequent ones — the post-mortem directly informs the standing configuration development that would reduce per-event authoring burden on subsequent events. If the event was genuinely one-time, the post-mortem nonetheless closes the event's governance arc: it produces an organizational record of what the event achieved and what its coordination implications are.

Committing to the post-mortem before the event begins — as a planned governance activity rather than an optional retrospective — ensures that the event is designed with reviewability in mind. Configuration choices made in advance of the event can be informed by what the post-mortem will need to evaluate.

---

## 5. Low-Frequency Governance as Entry Point

Low-frequency governance is the natural entry point into FAI participation. The architecture does not require organizations to begin with standing infrastructure; the simplest valid FAI event defined in §3 is achievable without it. Organizations that have not participated in FAI events before can conduct their first event at the floor, accumulate governance experience from that event through the post-mortem and the evolution-feed annotations, and optionally develop standing configurations that reduce per-event authoring burden as participation frequency increases.

The trajectory from first event to standing infrastructure is not architecturally prescribed; it is architecturally supported. An organization may remain a low-frequency participant indefinitely, conducting one event per year with per-event configuration authoring, and this is a fully valid governance posture under the architecture. Standing infrastructure is what high-frequency participation makes economically rational, not what the architecture requires for governance floor compliance.

This entry-point framing has a practical implication for organizations considering whether to participate in FAI at all: the governance investment required for a first event is bounded by the floor. The four recommendations in §4 are calibrated to make that investment achievable for an organization without prior FAI governance experience. The architecture does not impose a minimum governance investment beyond the floor, and the floor is designed to be achievable in commodity tools by non-specialist governance actors (Paper 1 §7.4, extended through Paper 3 §4).

---

## 6. Anti-Pattern: One-Time Event as Governance Exception

The anti-pattern for low-frequency or one-time event governance is treating infrequency as a basis for governance exception: reasoning that because the event is rare or singular, the governance overhead is disproportionate, and therefore the floor requirements need not be met.

This reasoning is incorrect in two respects.

First, the minimum viable governance floor applies regardless of event frequency. The floor is defined by what constitutes an architecturally valid governed FAI event, not by the governance capacity of the participants or the frequency of their participation. An event conducted without the floor requirements met is not an FAI event at a reduced governance level; it is not a governed FAI event. The shared substrate's integrity properties, the conflict preservation commitment, and the joint-authority structure of configuration are not optional overlays on top of a functional coordination event; they are what makes the event an FAI event in the Paper 3 sense.

Second, the governance investment required by the floor for a first event is not disproportionate. §3 defines the simplest valid event explicitly to establish that the floor is achievable without standing infrastructure, with a single aspect contribution, minimum configuration, full dissolution, and preserve-tier default conflict handling. An organization that concludes the floor requirements are disproportionate has likely misread the floor as requiring comprehensive standing infrastructure — the misreading this note is designed to prevent. The four recommendations in §4 are calibrated to make floor compliance achievable for an organization with limited governance experience and no prior FAI participation.

The anti-pattern is particularly consequential because first-event governance failures are not correctable within the event. A first event conducted without conflict registration, without explicit configuration, or without joint-authority structure for the shared substrate produces coordination outputs that lack the architectural properties — addressability, provenance, conflict preservation — that make the outputs usable by each participant's home substrate evolution mechanisms. The learning value the event could have provided is lost; the evolution-feed annotations that should inform future events are absent. The cost of the anti-pattern is paid not in the event itself but in the inability to build on the event's governance record.

---

## 7. Operational Test

For a first FAI event, an observer can verify governance floor compliance by checking whether all of the following are satisfied before the event begins and throughout its operation:

1. **Aspect-level contribution.** Each participating Self is contributing at least one complete aspect — a purpose-defined arrangement of cells — to the shared substrate. No participant is contributing at sub-aspect (cell-only) granularity.

2. **Three critical dimensions configured.** The event configuration, as substrate content under joint authority, explicitly specifies the sharing scope, the cardinality of participating Selves, and the persistence policy. These specifications are readable in the shared substrate before the event commences.

3. **Full dissolution or a more specific persistence policy specified.** The configuration explicitly commits to what happens to the shared substrate at event dissolution. If full dissolution is not specified, a more specific retention policy is explicitly specified and is within the governance capacity of both participants to maintain.

4. **Conflict registry present.** The shared substrate has a conflict registry: a mechanism by which conflicts surfacing during the FAI event are recorded as first-class substrate state, with both participants' positions retained distinct, the divergence point identified, and provenance attached.

5. **Conflict tier routing specified.** The configuration specifies which conflict tier handles which conflict classes. At minimum, a default routing to the preserve tier is specified for conflict classes without explicit orchestration rule coverage.

6. **Joint authority over configuration established.** Both participants can demonstrate that the configuration was authorized under the joint-authority arrangement Paper 3 §8 requires: neither participant's governance authority over the configuration is subordinate to the other's, and both participants have exercised the review-and-authorize step.

7. **Post-mortem committed.** The participants have agreed that a post-mortem will be conducted after the event, and the mechanism for conducting it — who participates, what it reviews, where its outputs are recorded — is specified.

An event that satisfies all seven requirements is at or above the minimum viable governance floor. An event that fails any of the seven is below the floor and is not a governed FAI event in the Paper 3 sense, regardless of how the participants describe it.

---

## 8. Conclusion

D2.72 completes the low-frequency side of the FAI governance frequency spectrum that D2.71 opened on the high-frequency side. Low-frequency and one-time FAI participation is the natural entry point into the architecture: it is achievable without standing infrastructure, at the governance floor, with the simplest valid event composition. The four practical recommendations — completing the onboarding checklist, partnering with an experienced Self, accepting the preserve-tier default, and committing to a post-mortem — are calibrated to make floor compliance achievable for an organization conducting its first event. The anti-pattern of treating infrequency as an exemption from floor requirements produces events that are not governed FAI events and loses the learning value those events could provide. The minimum viable governance floor applies at every event frequency. What changes with frequency is not whether governance applies but how its burden is distributed — per-event for low-frequency participants, across standing infrastructure for high-frequency participants.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance for Low-Frequency and One-Time Events.* May 15, 2026. ORCID: 0009-0004-8065-3235.
