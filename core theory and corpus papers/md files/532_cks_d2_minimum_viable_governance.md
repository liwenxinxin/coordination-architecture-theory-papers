# FAI Minimum Viable Governance

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series note:** #532, Phase D2.37

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D2.18 established seventeen record categories constituting a complete FAI governance record. This note derives the minimum viable governance floor — the seven requirements that cannot be reduced without ceasing to implement Paper 3's architecture. Six requirements produce records or artifacts; the seventh is an availability commitment that must hold throughout the event and cannot be satisfied after the fact by any record. The floor has dual prior-art significance: it forecloses claims that the architecture imposes prohibitive governance overhead (the floor shows minimal governance is achievable with standing configurations and pre-authorized rules) and simultaneously forecloses claims that any inter-Self exchange mechanism is a compliant FAI event (the floor shows specific, verifiable requirements must be satisfied — most contemporary exchange mechanisms fail multiple floor requirements simultaneously). The floor concept at inter-Self scope derives from Paper 2's B6.01 minimum governance boundary case at intra-Self scope, closing the intra-to-inter-Self prior-art chain on this concept.

---

## 1. Deriving the Floor

D2.18 established seventeen record categories for a complete FAI governance record, covering construction, dissolution, configuration, conflict handling, exchange bounding, contribution attribution, three rights confirmation, and supplementary audit and retention categories. That enumeration covers what full governance documentation looks like for an FAI event. It does not specify which subset is irreducible — which requirements, if absent, cause an event to stop instantiating Paper 3's architecture and become instead an unstructured inter-Self data exchange.

D2.37 derives that floor. The derivation method is elimination: for each Paper 3 commitment bearing on FAI events, identify the minimal artifact or property that must be demonstrable for that commitment to be operative. The result is seven floor requirements. Below any one of them, the architecture's commitments are stated but unverifiable. Above all seven, additional governance enriches the record without affecting compliance status.

Six of the seven floor requirements produce artifacts: an authored configuration, a construction record, a conflict registry, a dissolution record, contribution attribution attached to all shared-substrate content, and verifiable exchange bounding. The seventh floor requirement produces no artifact at all. It is an availability commitment: throughout the FAI event, all participating governance must be able to exercise the inspect right over shared-substrate content. No record produced after the event can satisfy this requirement retroactively. If inspect-right availability was absent during the event, the requirement is violated from the moment of inaccessibility, regardless of what documentation exists.

---

## 2. The Seven Floor Requirements

**Floor Requirement 1 — Authored Configuration.** A FAI event must have an authored configuration specifying at minimum the sharing scope, the persistence policy, and the basic conflict-handling routing (D2.12 minimum required content). These three dimensions must be governed content — not unreviewed system defaults or implied arrangements. Elaborate specification of all six configuration dimensions is above the floor; a standing configuration satisfies the requirement if it is current and jointly authorized by the participating governance. The rationale: Paper 3's Claim 5 commits to configuration as substrate content under joint authority. An FAI event that proceeds without authored governance of these three dimensions is operating on unspecified configuration, not on governed configuration. The configuration need not be lengthy; it must be real.

**Floor Requirement 2 — Construction Record.** The construction event must produce a record identifying the governing authorization reference and the participating Selves (D2.01). The record may be brief. What it cannot be is absent: if no construction record exists, the event's authorization basis is unverifiable, and the perimeter-spanning property (D1.02) is undemonstrable. A construction event that leaves no record is not an auditable governed act in Paper 3's sense; it is an undifferentiated system interaction whose participants, scope, and authorization are untraced.

**Floor Requirement 3 — Conflict Registry.** For every conflict detected during the FAI event, an entry must exist with both sides preserved and with attribution identifying the contributing Selves (D2.13). The registry may employ the preserve tier exclusively — the lowest-overhead resolution path — but cannot be empty when conflicts were detected. The rationale: Paper 3's Claim 3 commits to conflicts as first-class addressable substrate state. An empty conflict registry in the presence of detected conflicts is not a light implementation of that commitment; it is the erasure of the commitment. Full preservation without resolution is operationally minimal and fully compliant at the floor.

**Floor Requirement 4 — Exchange Bounding.** Exchange bounding must be verifiable (D2.16 Check 1). The floor does not require a formal per-event bounding verification report; it requires that content in the shared substrate during the event is classifiable as DNA-layer or action-layer content. LLM weights and instinct-layer content must not have entered the shared substrate. The rationale: Paper 2's instinct/reasoning separation extends through FAI per Paper 3's exchange-bounding commitment. If the separation cannot be demonstrated — because content is unclassified or unattributed by layer — the commitment is operationally absent. Content classification at authoring time with spot-checks satisfies the floor; a formal verification pass becomes relevant only when above-floor governance options are elected.

**Floor Requirement 5 — Dissolution Record.** The dissolution event must produce a record confirming that dissolution occurred and specifying the disposition of shared-substrate content (D2.02). The record may be brief. The floor requires that dissolution was a governed act — not an implicit timeout or silent connection close. The rationale: Paper 3's shared substrate is temporary by architectural commitment (D1.01). If no dissolution record exists, the temporary-construction commitment is not demonstrable as a governed event; the architecture collapses to a data exchange of indeterminate duration with unspecified content disposition.

**Floor Requirement 6 — Contribution Attribution.** All content in the shared substrate must be attributable to a contributing Self and aspect. No unattributed content. Attribution may be minimal — FAI event ID plus contributing Self ID plus aspect ID — but must exist for all content. The rationale: Paper 3's perimeter-spanning property (D1.02) entails that content crossing Self perimeters carries provenance from its origin. Content that cannot be attributed to a contributing Self has no demonstrable provenance; the perimeter-spanning property is unverifiable for that content. Richer provenance chains are above-floor enhancements.

**Floor Requirement 7 — Three Rights Availability.** Throughout the FAI event, all participating governance must be able to exercise the inspect right over shared-substrate content. Modify and override rights must be exercisable by joint governance. This requirement is not satisfied by a record; it is an availability commitment that must hold continuously during the event. If shared-substrate content is inaccessible to any participating governance — whether through access restriction, system design, or operational failure — the inspect right is violated from the moment of inaccessibility. No after-the-fact documentation repairs the violation. The rationale: Paper 1's human-governed commitment extends into the shared substrate by Paper 3's Claim 1 inheritance. Human-governed means the three rights are available at all times, not available in principle at scheduled checkpoints. An FAI event in which shared-substrate content was inaccessible to participating governance for any portion of its duration is not architecturally compliant for that portion.

---

## 3. What Can Be Streamlined Above the Floor

The seven floor requirements define the compliance boundary. Nothing below the floor is a compliant FAI event. Everything above the floor is a design choice that may reduce per-event governance overhead without touching compliance status.

Several significant streamlining paths operate above the floor.

*Per-event configuration authoring → standing configuration.* The floor requires an authored configuration. It does not require that configuration be authored fresh for each event. A standing configuration that is current, jointly authorized, and available to all participating governance satisfies Floor Requirement 1 across all events it governs. This eliminates per-event configuration authoring for stable deployment relationships.

*Per-conflict governance review → pre-authorized orchestration rules.* The floor requires a conflict registry with both sides preserved (Floor Requirement 3). It does not require real-time human review of each conflict. Pre-authorized orchestration rules specifying conflict routing (D2.15) satisfy the floor requirement with minimal per-conflict human involvement. Conflicts accumulate in the registry under pre-authorized rules; human review occurs on a governance-configured schedule above the floor.

*Per-event escalation routing → cross-organizational agreement.* The floor requires a dissolution record and a conflict registry. It does not require that escalation paths be decided event-by-event. A pre-specified cross-organizational escalation agreement (D2.34) satisfies the routing requirement for all covered events without per-event decision overhead.

*Formal exchange bounding verification → content classification spot-checks.* The floor requires verifiable exchange bounding (Floor Requirement 4). A formal per-event bounding verification report is above the floor. Classifying content by layer at authoring time, with spot-checks at event boundaries, satisfies Floor Requirement 4 at substantially reduced overhead.

*Provenance depth → minimal attribution.* The floor requires attribution for all content (Floor Requirement 6). Minimal attribution — FAI event ID plus contributing Self ID plus aspect ID — satisfies the floor. Richer provenance chains tracking cell-level lineage and version history are above-floor governance choices available to deployments where that granularity is warranted.

The practical consequence is that a low-stakes, high-frequency deployment can operate at the compliance floor — standing configurations, pre-authorized conflict routing, minimal attribution, content classification by layer — while a high-stakes, audit-intensive deployment enriches governance at each dimension above the floor. Both are compliant. The architecture scales in governance depth without a compliance discontinuity.

---

## 4. Dual Prior-Art Significance

Establishing the governance floor has two distinct prior-art functions, and both are necessary for the derivation series.

The first function is to foreclose the prohibitive-overhead objection. An adversarial reader might argue that Paper 3's architecture imposes governance overhead that is disproportionate to the value of low-stakes inter-Self events — that record-keeping and rights-availability requirements make compliant FAI events practically achievable only in high-investment deployments. The floor answers this directly: a minimally compliant FAI event requires authored governance content in seven specific forms, several of which can be reduced to brief records and all of which can be supported by standing configurations and pre-authorized rules. The overhead objection applies against above-floor governance enrichment choices, not against the architecture itself.

The second function is to foreclose the any-exchange-is-FAI claim. An adversarial reader might argue that an existing inter-Self exchange mechanism — a shared API endpoint, a message-passing protocol, a federated query interface — already constitutes a compliant FAI event, and that Paper 3 adds nothing not already present. The floor answers this directly: if any of the seven floor requirements is absent, the event is not a Paper 3 compliant FAI event, regardless of what content moves between the parties. Most existing exchange mechanisms fail Floor Requirements 1, 2, 3, 5, 6, and 7 simultaneously: no authored configuration specifying conflict-handling routing, no construction record identifying authorization, no conflict registry, no dissolution record governing content disposition, no content attribution by contributing Self and aspect, and no verified availability of the three governance rights throughout the exchange.

The dual foreclosure is the note's primary prior-art value. The floor concept does not appear in the prior literature at inter-Self scope at this level of specificity. Its absence from the prior literature is precisely what allows advocates of existing exchange mechanisms to claim architectural equivalence and advocates of light implementations to claim compliance without satisfying Paper 3's commitments. The floor makes both claims testable and, for most contemporary mechanisms and light implementations, falsifiable.

---

## 5. Relationship to Paper 2 B6.01

The minimum viable governance concept for FAI events inherits from Paper 2's B6.01 boundary case, which establishes the governance floor for intra-Self operations. B6.01 asks: at minimum, what governance commitments must be operative for a given intra-Self operation to instantiate Paper 2's architecture? The answer at intra-Self scope has the same structural shape as the answer at inter-Self scope: an authored configuration (or standing equivalent), a lifecycle record establishing the operation's governed origin, conflict handling that satisfies Paper 1's preservation commitment, and continuous availability of the three governance rights throughout the operation.

D2.37 extends this floor concept to inter-Self scope. The extension introduces two requirements not present at intra-Self scope.

The first addition is exchange bounding verification (Floor Requirement 4). At intra-Self scope, the instinct/reasoning separation is an internal architectural property of a Self's own substrate; verifying it does not require examining content at a perimeter. At inter-Self scope, content crosses from one Self's home substrate into a shared substrate whose governance perimeter spans multiple Selves. The instinct/reasoning separation must hold at that crossing, and its hold must be verifiable. This is a fresh requirement at inter-Self scope with no intra-Self analog.

The second addition is a construction record identifying participating Selves and governing authorization (Floor Requirement 2). At intra-Self scope, operations occur within a single governance perimeter; the question of which parties are present and what authorizes their participation is answered by the Self's own governance structure. At inter-Self scope, the perimeter-spanning property (D1.02) means that multiple distinct governance structures are present, and the basis on which they cooperate must be traceable. A construction record satisfies that traceability requirement.

The inheritance is genuine: B6.01 established the minimum governance concept at intra-Self scope. D2.37 inherits the concept and extends it to inter-Self scope with the additions Paper 3's fresh architectural commitments require. The floor concept is therefore not a novel invention at inter-Self scope — it is the appropriate extension of an established architectural principle, arriving at the inter-Self boundary with the same function (distinguishing compliant from non-compliant operations) and the same structure (a small set of irreducible requirements, with everything above the floor streamlinable through standing configurations and pre-authorized rules).

This inheritance closes the intra-to-inter-Self prior-art chain on the minimum governance concept: intra-Self scope established at B6.01; inter-Self scope established at D2.37.

---

## 6. Operational Test

For a minimal FAI event operating at the governance floor — with a standing configuration, pre-authorized conflict routing, minimal attribution, and no formal bounding verification report — an observer can verify compliance as follows:

1. Does an authored configuration govern this event, specifying sharing scope, persistence policy, and conflict-handling routing? If a standing configuration is in use, is it current and jointly authorized by all participating governance? *(Floor Requirement 1.)*

2. Does a construction record exist identifying the governing authorization reference and the participating Selves for this specific event? *(Floor Requirement 2.)*

3. For each conflict detected during the event, does the conflict registry contain an entry preserving both contributing sides with attribution? If no conflicts were detected, is this verifiable from event records? *(Floor Requirement 3.)*

4. Is the content in the shared substrate classifiable as DNA-layer or action-layer content? Is there evidence — through content labeling, authoring-time classification, or spot-check — that LLM weights and instinct-layer content did not enter the shared substrate? *(Floor Requirement 4.)*

5. Does a dissolution record exist confirming that dissolution occurred as a governed act, with the disposition of shared-substrate content specified? *(Floor Requirement 5.)*

6. Is all content in the shared substrate attributable to a contributing Self and aspect at minimum? Are there any content items that cannot be attributed? *(Floor Requirement 6.)*

7. Throughout the event, was shared-substrate content accessible to all participating governance for inspection? Were modify and override rights exercisable by joint governance at all times during the event? This check cannot be satisfied retroactively by documentation; it requires either continuous-availability architecture or event-time confirmation. *(Floor Requirement 7.)*

A minimal FAI event that satisfies all seven checks is architecturally compliant under Paper 3, regardless of which above-floor governance enrichments were not exercised. An event that fails any single check is not architecturally compliant, regardless of how elaborate its other governance documentation may be. The asymmetry is intentional: compliance requires all seven; non-compliance requires only one absent.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *FAI Minimum Viable Governance.* May 15, 2026. Series note #532, Phase D2.37. ORCID: 0009-0004-8065-3235.
