# Composition Pair 6: Population-Scope Participation and Governance Capacity

**Series D — Phase D4 Composition Pairs, Note D4.07 (Note #612)**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes the composition of two Paper 3 operational commitments: Population-Scope FAI Participation Governance (D2.31, Claim 6 territory) and Governance Capacity Management (D2.33). When applied independently, these commitments address separate concerns — how broadly a Self participates in the population-scale FAI network, and how many simultaneous FAI events a Self can govern. When composed, they reveal a non-obvious architectural requirement: governance capacity is not merely a constraint that limits participation volume after the fact. It is a required input that must shape the participation configuration before invitations arrive. This note formalizes three requirements the composition produces, establishes prior-art significance with calibrated-humility register appropriate to Claim 6 territory, and provides an operational test.

---

## 1. Pair Identification

**Commitment A — Population-Scope FAI Participation Governance (D2.31, Claim 6 territory).** A Self participating in the population-scale FAI network configures its network role across five governance dimensions: (A) the sharing scope for outbound contributions, (B) the cardinality preferences for events it initiates or joins, (C) the partner preference parameters that determine whose invitations the Self will accept, (D) the network role parameters specifying whether the Self acts as initiator, responder, or both, and (E) the review cadence at which the participation configuration itself is reassessed. These dimensions are substrate content authored under the Self's governance; they are the configurable surface through which a Self shapes its exposure to population-scale coordination. Because Claim 6 carries the calibrated-humility register appropriate to the trilogy-completion scope — population-scale collective evolution through accumulated FAI events is an architectural extension claim rather than a well-verified empirical finding — D2.31 inherits that register: the participation configuration governs a pattern with strong architectural motivation and biology-resonant precedent, while remaining appropriately humble about its empirical behavior at scale.

**Commitment B — Governance Capacity Management (D2.33).** A Self's governance capacity is the maximum number of simultaneous FAI events its practitioners can actively govern. Governance capacity is not an arbitrary soft limit; it is a real constraint determined by practitioner count, standing governance infrastructure maturity, and the depth of review each event requires. D2.33 requires that a Self maintain an explicit, current assessment of its governance capacity ceiling and that this ceiling be authored as substrate content — a named, auditable governance object rather than an informal awareness of how busy practitioners currently are.

**The composition.** A Self configuring its D2.31 participation dimensions is simultaneously subject to its D2.33 capacity ceiling. The participation configuration determines the invitation volume the Self will receive; the capacity ceiling determines what it can govern. Unless the two commitments are composed — authored together, reviewed together, and kept synchronized — a Self can create an architecturally coherent participation configuration that is nonetheless ungovernable at the volume it generates.

---

## 2. The Governance Scenario

A Self has operated with modest population-scale participation for several months. Its practitioners have matured its standing governance infrastructure and have begun accepting more FAI invitations. The governance team decides to expand participation: they revise the partner preference parameters (Dimension C) to accept a broader class of initiators, and they revise the network role parameters (Dimension D) to shift from responder-only to initiator-eligible. The revised participation configuration is authored as substrate content and reviewed by governance.

Nothing in this scenario is architecturally incorrect — if the two commitments are treated independently. The participation configuration is properly substrate-content, properly reviewed, properly versioned. The governance capacity assessment is maintained separately as an internal governance awareness: practitioners know roughly how many events they can handle, and they have a sense that the expanded configuration will stay within that range.

The failure mode emerges over the following weeks. The expanded configuration generates more invitations than the informal capacity estimate anticipated. Practitioners begin governing events at partial depth — lighter review, faster approval, less conflict-handling rigor — because the volume exceeds what the capacity can support at full governance depth. No governance record captures this degradation. The participation configuration and the capacity ceiling were never explicitly related, so no governance artifact flags the misalignment.

The scenario makes the problem concrete: treating D2.31 and D2.33 as independent commitments — each properly implemented in isolation — is insufficient. Their composition requires that capacity be an explicit, referenced input to the participation configuration, not a separate concern managed informally alongside it.

---

## 3. Non-Obvious Governance Requirements from the Combination

**Requirement 1 — Governance capacity is an input to participation configuration, not just an output constraint.**

The intuitive framing treats D2.33 as a downstream constraint: the participation configuration generates invitation volume; governance capacity caps what can be processed. In this framing, capacity management operates on whatever the participation configuration produces and flags overload after the fact.

The composition reveals that this framing is architecturally insufficient. The participation configuration's partner preference parameters (Dimension C) and network role parameters (Dimension D) are the primary levers that determine invitation volume. If those levers are set without reference to the governance capacity ceiling, the configuration can generate a volume that exceeds capacity before any downstream capacity management can intervene. The correction is not to add a capacity-check step after the configuration is authored; it is to author the configuration with the capacity ceiling as an explicit input. Specifically: Dimensions C and D must be scoped such that their expected invitation generation — at the configured partner breadth and role posture — remains within the governance capacity ceiling at the time of authoring. Capacity is consulted before the participation configuration is finalized, not applied after it generates load.

**Requirement 2 — The capacity ceiling must be authored as a referenced governance object within the participation configuration.**

It is not sufficient for practitioners to know the capacity ceiling as an internal governance awareness and to author a participation configuration that they believe respects it. The ceiling must be authored as a named, substrate-level governance object, and the participation configuration must explicitly reference it. This requirement follows from the substrate-content commitment at Paper 3's scope: governance objects that are merely informal are not substrate content, are not inspectable by a governance observer, and are not subject to the three rights (inspect, modify, override) that make substrate-based governance meaningful.

The practical consequence is that the participation configuration must specify, in substrate-legible form: (a) the governance capacity ceiling value it was authored against, and (b) the handling rule for invitations received when at capacity — whether additional invitations are queued, declined, or escalated to governance for prioritization. Without this specification, the participation configuration is an incomplete governance document: it specifies who the Self will engage with but not what governance commits to doing when engagement exceeds what it can govern.

**Requirement 3 — The participation configuration review cadence must be synchronized with governance capacity assessments.**

Governance capacity is not static. As a Self's practitioner population grows, as standing governance infrastructure matures, and as event review templates become routine, the capacity ceiling rises. Conversely, if practitioner turnover reduces governance bandwidth, the ceiling may fall. Neither direction is captured by a one-time co-authoring of capacity and participation configuration.

D2.31's review cadence (Dimension E) must therefore be synchronized with D2.33's capacity assessment cadence. The mechanism is straightforward: each scheduled review of the participation configuration includes a current governance capacity assessment as a required input. If the capacity ceiling has risen since the last review, the participation scope can be expanded. If the ceiling has fallen, the participation scope may need to contract. This synchronization ensures that participation scope evolution — the organic process by which a Self becomes more or less engaged in population-scale coordination over time — happens through governed review rather than through accumulated informal adjustments that leave no governance record.

---

## 4. Prior-Art Significance

With calibrated-humility register appropriate to the Claim 6 territory that D2.31 inherits: the composition pair establishes, at the architectural-pattern level, that participation configuration and governance capacity management are not independent governance functions in a population-scale AI coordination network. They are coupled functions that must be co-authored and co-reviewed as substrate content.

The specific prior-art contribution is the directionality: capacity as an *input* to participation configuration, rather than a *constraint on its outputs*. A practitioner implementing "scalable AI governance coordination" without reference to this composition might author participation configuration and capacity management as parallel, non-referencing governance documents. The composition shows that such an architecture creates an unconstrained invitation funnel: the Self's participation posture can generate ungovernable coordination volume without any governance artifact capturing the misalignment.

The three-part structure — capacity-as-input, ceiling-as-authored-object, cadence-synchronization — constitutes prior art for any coordination architecture that claims to support population-scale AI participation governance with human authority at population-level governance perimeters. The architectural commitment does not make empirical claims about how participation scales or how governance capacity evolves in practice; those questions belong to the extension-claim register. The commitment is that the coupling must be governed through explicit, auditable substrate content rather than through informal practitioner awareness, however accurate that awareness may be at any given moment.

---

## 5. Operational Test

For a Self with an authored population-scope participation configuration (D2.31) and an authored governance capacity management commitment (D2.33), an independent governance observer can verify the composition is satisfied if and only if all three of the following hold:

**(a) The participation configuration explicitly references a governance capacity ceiling.** The participation configuration substrate content names a specific governance capacity ceiling value (or references a named substrate object that holds it) against which Dimensions C and D were scoped. An observer can read the participation configuration and identify the capacity ceiling it was authored against without consulting external documentation or practitioner testimony.

**(b) The configuration specifies the handling rule for at-capacity invitations.** The participation configuration substrate content specifies what governance commits to doing when the Self receives invitations while at its capacity ceiling: queue with defined priority rules, decline with a defined response, or escalate to governance for prioritization. The specification is substrate content, not procedural policy held in practitioner memory.

**(c) The participation configuration review cadence and the governance capacity assessment cadence are synchronized.** The participation configuration's authored review schedule (Dimension E) aligns with the cadence at which governance capacity is assessed. Each scheduled participation configuration review has a current capacity assessment as a documented input. An observer can verify, from the review history, that participation scope changes were preceded by, or co-authored with, current capacity assessments.

A system in which one or more of these three conditions is absent has not satisfied the composition. Specifically: a system satisfying only (a) has named the ceiling but not committed to at-capacity handling; a system satisfying only (a) and (b) has authored a complete point-in-time configuration but will drift out of alignment as capacity evolves; a system satisfying all three has implemented the composition as an ongoing governed relationship between the two commitments.

---

*This is a defensive publication. Its purpose is to establish prior art for the governance architecture formalized above. No patent is sought.*
