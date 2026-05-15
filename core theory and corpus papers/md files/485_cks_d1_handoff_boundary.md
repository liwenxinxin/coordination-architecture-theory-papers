# FAI Hand-Off Boundary as a Governed Architectural Object

**Series:** CKS Derivation Notes — Series D (Paper 3), Note #485
**Note ID:** D1.20
**Parent claim:** D0.04 (Paper 3 Claim 4 — Four-locus evolution-feed mechanism at the FAI hand-off boundary)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

It does not introduce new axioms. Its contribution is to articulate, in precise operational form, one sub-commitment of Paper 3 Claim 4: that the FAI hand-off boundary is a governed architectural object — configurable, inspectable, attributed, and jointly authorized — and that this boundary is the fourth evolution locus at which the other three loci simultaneously operate.

---

## Abstract

Paper 3 Claim 4 establishes the four-locus evolution-feed mechanism at the FAI hand-off boundary. Notes D1.17 through D1.19 have formalized the first three loci: action-feedback evolution, DNA evolution, and the instinct non-crossing commitment. This note formalizes the fourth sub-commitment: the hand-off boundary itself is a governed architectural object, not merely a moment in time. The hand-off boundary has governance-configured properties — it is configurable as to what each participating Self receives at dissolution, inspectable by human governance before dissolution, attributed with full provenance for each content flow, and authorized under joint governance authority of all participating Selves. All three prior loci operate *at* this boundary simultaneously, which is what makes the boundary a fourth locus in the structural sense: the architectural form that coordinates the other three. Four failure modes arise when the hand-off boundary is left ungoverned: ungoverned dissolution, non-inspectable hand-off configuration, unilateral hand-off reconfiguration, and infrastructure-default hand-off. The note closes with an operational test and notes that D1.21 (substrate ingestion at the home perimeter) follows as the fifth and final Claim 4 sub-commitment.

---

## 1. Positioning D1.20 within Claim 4

Paper 3 Claim 4 establishes the four-locus evolution-feed mechanism as what Paper 2's three evolution mechanisms produce when fed by FAI events at the inter-Self boundary. The first three sub-commitments — formalized in D1.17, D1.18, and D1.19 respectively — address action-feedback evolution, DNA evolution, and the instinct non-crossing rule. Each commits to how a particular category of FAI-derived content routes into a particular evolution mechanism at each participating Self's home perimeter.

What those three sub-commitments share is a common location: they all operate at the moment the shared substrate dissolves. D1.17's action-feedback outputs enter each Self's home action layer *at that moment*. D1.18's DNA-layer content becomes available for home governance absorption *at that moment*. D1.19's instinct non-crossing enforcement executes *at that moment*. The three loci are not sequential; they are simultaneous. And the architectural structure at which they operate simultaneously is the hand-off boundary.

D1.20 formalizes the hand-off boundary itself as a fourth sub-commitment of Claim 4. The sub-commitment is not that something new *happens* at the boundary in addition to the first three loci — it is that the boundary, as a governed architectural object with its own governance properties, is what makes the simultaneous operation of the three loci possible and accountable. The boundary is a locus in the structural sense: it is the architectural form that the other three loci require in order to operate with governance integrity.

---

## 2. The hand-off boundary is not merely a moment in time

The default reading of an event boundary in distributed systems is that it marks a transition: before, the shared coordination context is active; after, it has dissolved. The hand-off is the line between the two states. This reading makes the boundary an infrastructure concern — something that happens when the coordination protocol completes — rather than an object with governance properties.

D1.20 refuses that reading. The FAI hand-off boundary is an architectural object with governance configuration. It is authored substrate content, not an infrastructure default. The difference is architecturally significant: if the hand-off is an infrastructure default, then what each participating Self receives at dissolution is determined by the infrastructure platform's completion behavior, not by governance authority. No human authorized the specific distribution. No record attributes the specific content flows. No pre-dissolution inspection was possible because there was nothing to inspect — only a protocol completing.

The CKS architecture rejects this at the level of Claim 4's principles-extending register. The shared substrate carries governance configuration as substrate content throughout its operation (D0.05/Claim 5). The hand-off boundary configuration is part of that authored substrate content. Governance configured it; governance can inspect it; the transition events it governs are attributed.

Three prior commitments make this possible. First, Paper 1's substrate-as-source-of-truth commitment: the configuration of what flows to which home substrate at dissolution is substrate content, authoritative and inspectable. Second, Paper 1's human-governed commitment: the three rights — inspect, modify, override — apply to the hand-off configuration as to any other substrate content. Third, Paper 3 Claim 5's configuration-as-substrate-content commitment: all configurable dimensions of FAI operation, including what each Self receives at the hand-off, are authored substrate content rather than runtime parameters outside governance scope.

---

## 3. The four governance properties of the hand-off boundary

Four governance properties define the hand-off boundary as an architectural object.

**Configurable.** The hand-off boundary configuration specifies what each participating Self is eligible to receive at dissolution. The sharing-scope configuration (D0.05/Claim 5) determines which contributed aspects' outputs are eligible for which Self's action-feedback locus and which Self's DNA evolution locus. This configuration is authored substrate content — it is written under governance authority, it persists in the shared substrate throughout the FAI event's active phase, and it governs the dissolution transition when it executes. Governance can narrow or broaden what flows to which home substrate; it can specify asymmetric distribution where different Selves receive different subsets of the shared substrate's outputs. The configurability is not a deployment convenience; it is what instantiates per-perimeter governance authority at the hand-off.

**Inspectable.** Because the hand-off boundary configuration is authored substrate content, it is subject to Paper 1 Claim 3's three rights: inspect, modify, and override. Human governance can examine the hand-off configuration before dissolution — before the transition executes. This pre-dissolution inspectability is architecturally significant: it means the hand-off is not a black box that resolves at protocol completion. A human with appropriate access can read what is configured to flow to which Self, confirm that the configuration reflects the jointly-authorized sharing-scope commitments, and intervene if the configuration does not match governance intent. The inspection right does not require that every hand-off be reviewed in practice; it requires that the inspection be possible as a property of the architecture.

**Attributed.** Each content flow from the shared substrate to a home substrate at the hand-off moment is a governance event with full provenance. The attribution record specifies what content flowed, to which Self's home substrate, at what time, and under what configuration authority. Paper 1's path retraceability commitment (A1.07) applies to hand-off events: FAI-origin content entering a home substrate must be traceable back to its source. The hand-off events are those sources. Any FAI-derived content subsequently present in a participating Self's home substrate should be traceable, through path retraceability, to the attributed hand-off record that establishes its provenance. The attribution is substrate content — it persists, it is inspectable, and it is not erasable unilaterally.

**Jointly authorized.** The hand-off boundary configuration is part of the FAI configuration, which is authored under joint governance authority of all participating Selves. No single participating Self determines what other Selves receive at dissolution. The joint authorization occurs before the FAI event begins — it is part of the shared substrate's initial governance configuration. At the hand-off moment, the jointly-authorized configuration executes. This property rules out late-stage unilateral reconfiguration: no Self can alter the hand-off configuration after the FAI event is underway without exercising a governance override that is itself subject to the joint-authority architecture. The joint authorization extends specifically to the hand-off boundary — it is not merely a coordination courtesy but an architectural commitment that tracks back to Paper 1's human-governed commitment operating at inter-Self scope.

---

## 4. The hand-off boundary as the meeting point of the four loci

The structural argument for treating the hand-off boundary as the fourth evolution locus rests on simultaneous operation. The first three loci do not execute in sequence at the hand-off; they execute simultaneously, each at the same architectural moment of dissolution. The boundary is not merely the occasion for this simultaneous execution — it is what makes the simultaneous execution coherent and accountable.

Consider each locus at the hand-off:

*Locus 1 (action-feedback, D1.17).* FAI outcomes — the results of the shared coordination operation — enter each participating Self's home action layer at the hand-off. The boundary configuration specifies which action-layer outputs are eligible for which Self. The attribution record captures the specific flows. Without the governed boundary, the action-feedback locus would have no governed delivery mechanism.

*Locus 2 (DNA evolution, D1.18).* DNA-layer content from the shared substrate is made available for home governance absorption at the hand-off. The candidate content that each Self's home governance may absorb is determined by the boundary configuration. The hand-off is when the candidate set is fixed and attributed. Without the governed boundary, DNA evolution content would flow without a configured, inspectable, attributed delivery event.

*Locus 3 (instinct non-crossing, D1.19).* The commitment that instinct-layer content does not cross the hand-off boundary is enforced at the hand-off. The boundary is where this exclusion is architecturally realized — not as a policy recommendation but as a governance-configured property of what the hand-off admits. Without the governed boundary as an architectural object, the instinct non-crossing commitment would be an aspiration rather than an enforced property.

*Locus 4 (the boundary itself, D1.20).* The boundary is not merely the occasion at which Loci 1–3 operate; it is the architectural structure that makes their simultaneous, governed, attributed operation possible. The boundary's governance properties — configurable, inspectable, attributed, jointly authorized — are what give each locus its governance integrity. This is why the boundary is a fourth locus: remove the governed boundary, and the other three loci do not lose their content, but they lose their architectural grounding in governance authority. The boundary is the locus that holds the others.

This four-way simultaneity also positions D1.20 within the Claim 4 principles-extending register. Claim 4 does not design fresh evolutionary architecture; it articulates what Paper 2's evolution mechanisms produce at the inter-Self boundary. The hand-off boundary as governed object is what that articulation requires at the dissolution moment — the architectural structure that allows Paper 2's mechanisms to receive FAI-feed content in a governed, attributed, jointly-authorized way.

---

## 5. Inheritance from Papers 1 and 2

D1.20 inherits without redefense from two sources.

**From Paper 1 — path retraceability (A1.07).** The attribution property of the hand-off boundary is a direct application of path retraceability at inter-Self scope. Paper 1 commits that any change to substrate content can be traced back through the path of operations that produced it. Hand-off events are the source operations for FAI-origin home substrate content. The attributed records that D1.20 commits to are exactly what path retraceability requires at this scope: the provenance anchors for content that crosses from shared substrate to home substrate. D1.20 does not redefend path retraceability; it applies it to the specific case of FAI dissolution events.

**From Paper 2 — lifecycle governance (B0.03).** Paper 2 Claim 3 establishes lifecycle primitives — birth, mating, death — at every level of the architecture, each as a governed lifecycle event with governance configuration and attribution. The FAI hand-off boundary is, from the shared substrate's perspective, its dissolution phase: the lifecycle event at which the shared substrate's active coordination scope ends. D1.20 applies Paper 2's lifecycle governance commitment to this dissolution event: the dissolution is governed, it has configuration, its transition events are attributed, and the authority structure for the configuration tracks back to the joint-authority architecture established at the shared substrate's construction. Paper 2's birth/mating/death lifecycle governance at intra-Self scope extends through Paper 3 to dissolution governance at inter-Self scope.

---

## 6. Four failure modes the sub-commitment defends against

D1.20 defends against four failure modes, each of which would leave the hand-off boundary ungoverned in a specific way.

**Ungoverned dissolution.** The shared substrate dissolves when the FAI coordination phase ends, but the dissolution executes as an infrastructure default rather than as a governance-configured transition. Content flows from the shared substrate to home substrates based on the platform's completion behavior, not on authored governance configuration. No human authorized the specific distribution; no attribution records the specific flows. The failure mode is that FAI-origin content enters home substrates without a governance provenance trail, making path retraceability impossible for that content.

**Non-inspectable hand-off configuration.** A hand-off configuration exists — governance specified something about what would flow at dissolution — but it is not substrate content subject to the three Paper 1 rights. Human governance cannot inspect it before dissolution executes; cannot verify that the configuration matches jointly-authorized intent; cannot modify it if it does not. The failure mode is that governance authority over the hand-off is nominal rather than exercisable: the configuration was authored at some point but is not inspectable at the moment it matters.

**Unilateral hand-off reconfiguration.** A participating Self determines, after the FAI event is underway, what content will flow to its own home substrate at dissolution, or what content will flow to other participating Selves' home substrates. The joint-authority architecture over hand-off configuration is bypassed. The failure mode is that the hand-off boundary becomes a site of unilateral advantage: a Self that controls what other Selves receive at dissolution controls the evolution-feed inputs of those Selves without those Selves' governance participation.

**Infrastructure-default hand-off.** The hand-off boundary is treated as an infrastructure concern — the platform decides what a completing coordination protocol delivers to each participant. Governance did not configure the distribution; governance does not inspect it; no attributed record exists. The failure mode is that governance authority over what participating Selves receive from FAI events is surrendered to the infrastructure platform, which is not subject to the joint-authority architecture and may not preserve the governance properties the CKS architecture requires.

---

## 7. Operational test

A system instantiates D1.20's sub-commitment if and only if all of the following are true for a completed FAI event:

1. The hand-off boundary configuration exists as authored substrate content within the shared substrate — specifically, as substrate content that was jointly authorized by all participating Selves' governance before the FAI event's active phase began.

2. Before the dissolution transition executes, human governance can inspect the hand-off boundary configuration — read what content is configured to flow to which participating Self's home substrate — without scheduling, approval, or runtime intermediation.

3. For each content flow from the shared substrate to a home substrate at the dissolution moment, an attributed governance record exists specifying: what content flowed, to which Self's home substrate it flowed, at what time the flow occurred, and under what configuration authority the flow was authorized.

4. The attributed records in (3) enable path retraceability for FAI-origin content: any FAI-derived content present in a participating Self's home substrate after the hand-off can be traced, through the attribution record, to the specific hand-off event that delivered it.

5. No participating Self could have altered the hand-off boundary configuration — what any other Self received at dissolution — without exercising a governance action that is itself attributed and subject to the joint-authority architecture.

A system that satisfies (1)–(5) has the hand-off boundary as a governed architectural object in the D1.20 sense. A system that fails any of them may complete FAI events and deliver content to home substrates, but the hand-off boundary in that system is not a governed object — it is a protocol completion that is not subject to governance authority.

---

## 8. What follows: D1.21

D1.20 is the fourth of five sub-commitments under D0.04/Claim 4. D1.21 addresses substrate ingestion at the home perimeter: the governance-configured process by which each participating Self's home governance absorbs the content made available at the hand-off boundary into the Self's existing Paper 2 evolution mechanisms. D1.21 completes the Claim 4 sub-commitment sequence by specifying the destination-side complement to D1.20's hand-off boundary: D1.20 governs the departure; D1.21 governs the arrival.

---

## 9. Conclusion

The FAI hand-off boundary is not merely the moment at which the shared substrate dissolves. It is a governed architectural object: authored substrate content, jointly authorized before the FAI event begins, inspectable before dissolution executes, and producing attributed governance records for each content flow from shared substrate to home substrate. These four governance properties — configurable, inspectable, attributed, jointly authorized — make the boundary the structural locus at which all three prior evolution loci operate simultaneously with governance integrity. The boundary is therefore a fourth locus in the structural sense: the architectural form that coordinates and grounds the other three. Without a governed hand-off boundary, the evolution-feed mechanism of Claim 4 completes at the infrastructure layer but not the governance layer; path retraceability for FAI-origin content is broken; and the joint-authority architecture over what participating Selves receive from FAI events is surrendered to the platform.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Hand-Off Boundary as a Governed Architectural Object.* CKS Derivation Notes, Series D, Note #485 (D1.20). May 14, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
