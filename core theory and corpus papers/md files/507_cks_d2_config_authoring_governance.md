# FAI Configuration Authoring Governance Protocol

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

It does not introduce new axioms. Its contribution is to formalize the governance protocol through which a Full Aspect Integration (FAI) configuration is authored before shared-substrate construction — a protocol that follows directly from D1.22 (all six configurable FAI dimensions are substrate content) and D1.25 (joint authority governs the configuration substrate). The note states the five-phase authoring protocol, the minimum required configuration content, and the amendment protocol for changes during active FAI events.

## Abstract

A Full Aspect Integration (FAI) event operates over a shared substrate whose governance framework is determined by a configuration that must itself be jointly authored before construction begins. D1.22 established that all six configurable FAI dimensions — sharing scope per participating Self, cardinality, persistence policy, cooperation/competition variant, provenance carry-over depth, and provenance preservation on internalization — are substrate content subject to governance authority. D1.25 established that joint authority across all participating Selves' governance structures governs the configuration substrate. D2.12 formalizes what those two commitments require operationally: a five-phase authoring protocol running from initial proposal through joint authorization to configuration substrate establishment. The protocol enforces a structural asymmetry — the initiating Self drafts but cannot determine; joint authorization is what makes the configuration jointly governed rather than initiator-imposed. The note states the five minimum content elements below which a configuration is incomplete and construction should not proceed, and the amendment protocol by which the configuration may be changed during an active FAI event. An anti-pattern — implicit configuration, in which no authored configuration substrate exists and the event operates on system defaults — is named and diagnosed as a violation of both D1.22 and D1.25.

## 1. Why a governance protocol for configuration authoring is required

A FAI event constructs a shared substrate that spans the governance perimeters of two or more distinct Selves. The shared substrate is a temporary but real governance artifact: it operates under its own governance framework for the duration of the event, carries substrate content crossing perimeter boundaries, and hands off accumulated knowledge at dissolution. The governance framework that shapes the shared substrate's behavior during operation is the FAI configuration — the set of authoritative decisions covering all six configurable dimensions established in D1.22.

The need for a governance protocol arises from two facts in conjunction. First, the configuration is substrate content: it is not a runtime parameter internal to one Self but an explicit, inspectable, modifiable record that participates in the same governance architecture as any other substrate content per D1.22. Second, the configuration governs a shared artifact that crosses governance boundaries: it cannot be determined by any single Self without violating the joint authority commitment of D1.25. A configuration that reflects only the initiating Self's preferences without review, amendment opportunity, and authorization by all participating governance structures is not a jointly governed configuration — it is unilateral imposition dressed as governance.

The five-phase authoring protocol resolves this conjunction. It gives the initiating Self a defined role as the drafter of the starting point, while reserving the authority to determine the configuration for the joint authorization step in which all participating governance structures participate. The protocol is not procedural overhead. It is the mechanism by which the configuration earns its status as jointly governed substrate content.

## 2. The five-phase authoring protocol

The FAI configuration authoring protocol runs five phases before shared-substrate construction proceeds.

**Phase 1 — Initiating governance proposes the configuration.** The governance of the Self that originates the FAI event drafts an initial configuration. The draft addresses all six dimensions from D1.22: sharing scope for each participating Self (what each Self contributes and what it receives), cardinality (all participating Selves named), persistence policy (whether the shared substrate persists beyond immediate operation or dissolves on completion), cooperation/competition variant (the mode under which participating Selves operate within the shared substrate), provenance carry-over depth (how many layers of provenance travel with contributed aspects), and provenance preservation on internalization (how provenance is handled when a participating Self internalizes shared substrate content). The draft is authored as substrate content within the initiating Self's home substrate with governance attribution — the drafting authority is recorded, not anonymous.

The draft is a starting point, not a determination. The initiating Self's governance does not have the authority to finalize the configuration unilaterally; that authority belongs to the joint structure established in Phase 4. What Phase 1 accomplishes is the production of a concrete, complete-across-all-six-dimensions proposal that the other participating governance structures can review substantively rather than beginning from a blank slate.

**Phase 2 — Proposed configuration shared with all participating governance structures.** The proposed configuration is shared with the governance of every other participating Self. This sharing is itself a governed act: the configuration proposal is substrate content that crosses governance boundaries, and the sharing record documents which governance authority transmitted it, to whom, and when. Each participating governance structure receives the complete proposed configuration and has full inspection rights over it. Selective disclosure — sharing some dimensions with some participating Selves but withholding others — violates both the inspectability property of substrate content and the joint authority commitment of D1.25.

**Phase 3 — Negotiation and amendment.** Participating Selves' governance structures may propose amendments to any dimension of the configuration. Each amendment is a governance act with attribution: the amending authority is recorded, the amended dimension is identified, and the prior value and proposed new value are both preserved in the record. Amendments may cycle through multiple rounds. The negotiation continues until all participating governance structures have reached the jointly-configured approval threshold established in D1.25's approval mechanics — the threshold at which the accumulated configuration reflects positions that all participating governance structures have authorized rather than merely observed.

No dimension of the configuration may remain in substantive dispute when the protocol advances to Phase 4. A configuration with unresolved disagreements on any of the six dimensions is not ready for joint authorization; advancing to Phase 4 over unresolved disagreement produces a configuration whose joint authorization is nominal rather than real.

**Phase 4 — Joint authorization.** All participating governance structures formally authorize the final configuration per the approval mechanics from D1.25. The joint authorization record documents: which governance authorities participated, in what capacity, when each authorization was recorded, and the complete final configuration as of the authorization moment. This record is substrate content in the jointly-authorized configuration substrate. The authorization is not a signature applied externally to the configuration; it is the act that constitutes the configuration as jointly governed substrate content. A configuration that has been negotiated but not formally authorized has not completed Phase 4.

**Phase 5 — Configuration substrate established.** The jointly-authorized configuration becomes the shared substrate's initial governance framework. It is carried forward into the shared substrate at construction per the construction mechanics formalized in D2.01. From the moment of construction, the shared substrate operates under this configuration: the sharing scope, persistence policy, conflict-handling routing rules, and all other dimensions take effect. The configuration substrate is not a separate artifact held outside the shared substrate; it is substrate content within it, inspectable and — subject to the amendment protocol in §4 — modifiable under joint authority during operation.

## 3. Minimum required configuration content

Not every configuration detail need be specified before construction, but five elements constitute the governance floor below which a configuration is incomplete and construction should not proceed. A FAI event with an incomplete configuration lacks the governance infrastructure to operate as a compliant shared substrate.

The five minimum elements are:

**(a) Cardinality and participating Selves identified.** The configuration must name every Self participating in the FAI event and specify the total cardinality. A configuration that leaves cardinality open — "to be determined at runtime" — cannot support joint authorization because the set of authorizing parties is itself undefined. A configuration that names some participating Selves but not others creates a two-tier structure in which unnamed Selves have no governance standing in the configuration that governs their participation.

**(b) Sharing scope for each participating Self.** The configuration must specify what each named Self contributes and what each receives. Sharing scope is the dimension that directly governs what crosses governance perimeters during the FAI event. A configuration that leaves sharing scope unspecified allows arbitrary content exchange without governance constraint, violating D1.22's commitment that sharing scope is substrate content subject to governance authority.

**(c) Persistence policy.** The configuration must specify the persistence policy for the shared substrate — even if the policy is full dissolution at event completion. "Full dissolution" is a valid and complete persistence policy. What is not valid is the absence of any persistence policy, because persistence policy governs how and whether accumulated substrate content survives the event and enters the four-locus evolution feed formalized in D1.17–D1.21. Without a persistence policy, the fate of accumulated content is undetermined, not governed.

**(d) At least basic conflict-handling routing rules.** The configuration must specify at minimum how conflicts arising within the shared substrate are routed — which tier of the three-tier conflict-handling mechanism from D1.13–D1.16 applies as the first-line response. This does not require exhaustive conflict-class definitions, but it requires that the shared substrate not operate with no routing rules at all. A shared substrate with no conflict-handling routing rules cannot resolve, preserve, or escalate conflicts in a governed manner; it can only accumulate them invisibly.

**(e) Hand-off boundary configuration.** The configuration must specify how the hand-off at FAI dissolution is structured — which content is pushed to which participating Selves' home substrates, under what provenance attribution. Hand-off boundary configuration connects the shared substrate's lifecycle to the evolution-feed commitments of D1.17 and must be present before construction so that dissolution can be executed under the same governance framework that governed operation.

A configuration satisfying all five elements may be minimal but is governance-complete in the sense that the shared substrate can operate, handle conflicts, and dissolve in a governed manner. A configuration missing any one of the five cannot make that claim.

## 4. Configuration amendment during active FAI events

The configuration governs the shared substrate throughout the FAI event's lifecycle, not only at the moment of construction. Circumstances may arise during operation that make amendment of the configuration appropriate: a participating Self may need to adjust its sharing scope, cardinality may change if a new Self joins or a participating Self withdraws, or the conflict-handling routing rules may need refinement based on conflict patterns observed during operation.

Amendments during active FAI events are permitted but require the same joint authorization protocol that governs initial configuration. Specifically, Phases 3 and 4 of the authoring protocol apply to mid-event amendments without exception:

The governance structure seeking the amendment proposes the specific change with attribution, identifying which dimension is being amended and the rationale. All participating governance structures receive the proposed amendment and have the opportunity to review and respond — the same inspection right that applied to the initial configuration applies to amendments. Negotiation proceeds until the jointly-configured approval threshold is reached. Joint authorization of the amendment is recorded as substrate content with the same documentation requirements as the initial authorization: which governance authorities participated, when, and the specific change authorized.

The effect is that the governance framework of an active shared substrate cannot be changed by any single participating Self unilaterally, regardless of the change's apparent reasonableness. A unilateral mid-event configuration change by one Self is not an amendment — it is a governance violation. It bypasses the joint authority structure that the initial configuration established and that D1.25 requires throughout the event's lifecycle.

Each amendment is recorded as a versioned entry in the configuration substrate. The configuration substrate is therefore not a single static record but a governed log of: the initial configuration with its Phase 4 joint authorization, followed by any amendments each with their own joint authorization records. An observer inspecting the configuration substrate at any point during the FAI event can read the complete governance history of the shared substrate's governance framework.

## 5. Anti-pattern: implicit configuration

The implicit configuration anti-pattern is the failure mode in which a FAI event proceeds without an authored configuration substrate — the shared substrate is constructed and operated using system defaults for all six configurable dimensions, without any governance authority having explicitly authored, negotiated, or jointly authorized the configuration.

Implicit configuration violates D1.22 in the most direct way possible: the six configurable dimensions are substrate content by D1.22's commitment, and substrate content requires explicit authoring under governance authority. System defaults are not authored configuration; they are the absence of governance decision expressed as operational behavior. A FAI event running on system defaults is not operating under a lightly governed configuration — it is operating under no configuration that any governance authority has owned.

Implicit configuration also violates D1.25 by eliminating the joint authority structure entirely. There is no proposal to review, no amendment opportunity, no joint authorization record. No participating governance structure has exercised authority over the configuration; the event's governance framework was determined by whoever last set the system defaults.

The practical consequences include: sharing scope that may not reflect any participating Self's actual governance preferences; persistence policy that defaults to whatever the system does rather than what any governance authority chose; conflict-handling routing that reflects a generic design rather than the specific character of the participating Selves' relationship; and a hand-off at dissolution that is undocumented in the configuration substrate, making it ungoverned in the D1.17 sense.

Implicit configuration is most likely to occur when FAI events are treated as lightweight technical operations rather than governed inter-Self coordination events, or when the five-phase authoring protocol is seen as overhead that can be deferred until the shared substrate is already operating. Both framings misidentify where the governance work is: the configuration authoring protocol is not overhead appended to a technical operation; it is the governance act that constitutes the shared substrate as a jointly governed artifact rather than a shared technical resource.

## 6. Operational test

For any claimed FAI event, a compliance observer applies the following test to determine whether D2.12 has been satisfied. The test has three parts.

**Part 1 — Configuration substrate completeness.** Can the observer locate, within the shared substrate, a complete configuration substrate that specifies all six dimensions from D1.22 — sharing scope for each participating Self, cardinality, persistence policy, cooperation/competition variant, provenance carry-over depth, and provenance preservation on internalization? If any dimension is absent, or if any dimension's content is "system default" or equivalent rather than an explicitly authored value, the configuration substrate is incomplete and the test fails.

**Part 2 — Joint authorization record.** Does the configuration substrate contain a joint authorization record from Phase 4 that documents: (a) the identity of each participating governance authority that authorized, (b) the time of each authorization, and (c) the complete final configuration as of the authorization moment? If any participating governance authority is absent from the authorization record, or if the authorization record exists but post-dates construction (meaning construction proceeded before joint authorization was complete), the test fails.

**Part 3 — Amendment records for any mid-event changes.** If the configuration substrate has been modified since initial construction, does each modification appear as a versioned amendment entry with its own joint authorization record, satisfying the same documentation requirements as the initial authorization? An amendment without a corresponding joint authorization record is a unilateral change; the test fails.

A FAI event passes the operational test if and only if all three parts are satisfied: the configuration substrate is complete across all six dimensions with no dimension relying on system defaults, the joint authorization record includes all participating governance authorities and predates construction, and every post-construction modification appears as a jointly authorized amendment.

## 7. Conclusion

D2.12 formalizes the governance protocol through which a FAI configuration is authored before shared-substrate construction and maintained throughout the event's lifecycle. The five-phase protocol — proposal by the initiating governance, sharing with all participating governance structures, negotiation and amendment, joint authorization, configuration substrate establishment — is the operational consequence of D1.22 and D1.25 in conjunction: configuration as substrate content requiring governance authorship, and joint authority requiring participation by all governance structures rather than determination by one.

The structural asymmetry at the protocol's core — initiating governance proposes, joint governance authorizes — is not a procedural nicety. It is what distinguishes a jointly governed configuration from an initiator-imposed one. A FAI event whose configuration was drafted and finalized by a single Self, then handed to other participating Selves as a fait accompli, is not operating under a jointly governed configuration regardless of how complete the configuration's coverage of the six dimensions may be.

The minimum required configuration content establishes the governance floor: the five elements without which the shared substrate cannot operate, handle conflicts, and dissolve in a governed manner. Construction below this floor does not merely create a lightly governed shared substrate; it creates a shared substrate without the governance infrastructure the CKS architecture requires.

The amendment protocol preserves governance integrity across the full FAI event lifecycle. The same joint authorization that constitutes the initial configuration as jointly governed applies to every subsequent change. The configuration substrate is therefore a governed record of governance decisions, not a static initialization artifact that recedes into the background once construction is complete.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235. [Paper 3 in the CKS theory series.]

## How to cite this note

Li, W. (2026). *FAI Configuration Authoring Governance Protocol.* May 15, 2026. ORCID: 0009-0004-8065-3235. Derivation note D2.12 in the CKS defensive-publication series, note #507.
