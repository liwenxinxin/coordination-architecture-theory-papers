# AP-25: Topology Lock-In

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes AP-25: Topology Lock-In, the first of three Category 7 (Population-Scope Failures) anti-patterns in the Phase D3 series. Topology lock-in names the condition in which a governance arrangement — a standing configuration, cross-organizational agreement, or informal commitment — prevents a participating Self from exercising its exit rights or adjusting its network participation configuration. When this condition holds, a Self's network topology is determined by its governance obligations rather than by its current governance intent, and the distributed-governance property of the population-scale FAI network is compromised. The note operates in the calibrated-humility register throughout: topology lock-in is a possibility the architecture is designed to prevent, not an inevitable feature of population-scale FAI deployments. The prevention is architectural — exit rights are inalienable under governance sovereignty commitments, and any governance arrangement provision that forecloses them is invalid by construction.

---

## Opening Category 7

Anti-patterns AP-25 through AP-27 form Taxonomy Category 7: Population-Scope Failures. Category 7 addresses failure modes that arise specifically at the network scale that Paper 3's Claim 6 projects — the dynamics that emerge when FAI events accumulate across a population of CKS-governed Selves operating across diverse domains, distinct organizations, and distinct governance authority structures. The failure modes in this category cannot be observed within a single Self or a single bilateral FAI event; they arise from the aggregation of governance arrangements and network participation decisions across many Selves over time.

All three Category 7 anti-patterns are in the calibrated-humility register. Claim 6 itself holds the calibrated-humility voice anchor: population-scale CKS-governed Self deployments do not yet exist, and the architectural commitment is to what the inheritance produces at population scope, with specific population-scale dynamics awaiting empirical observation. Category 7 carries the same voice — the three anti-patterns surface possibilities that governance must be built to prevent, not pathologies that are inevitable once network scale is reached. The architecture's prevention commitments are the substance of each note.

AP-25 opens the category with the most structurally fundamental of the three: the governance arrangement that prevents a Self from leaving.

---

## 1. Anti-Pattern Name and Category

**AP-25: Topology Lock-In**
**Category 7 — Population-Scope Failures (Calibrated-Humility Register)**

---

## 2. Description

A governance arrangement — a standing configuration, a cross-organizational agreement, or an informal commitment that has acquired binding force — prevents a participating Self from exercising its exit rights or from adjusting its network participation configuration. In the condition AP-25 names, the Self cannot change which FAI relationships it maintains, cannot reduce its participation volume, and cannot exit a relationship without breaching governance obligations it has accepted.

The result is that the Self's network topology is determined by its governance obligations rather than by its current governance intent. What should be a continuously governable dimension of the Self's coordination strategy has become fixed by prior commitments the Self cannot unilaterally revise or terminate.

At population scale, this condition compounds. If multiple Selves in the FAI network find their topologies locked by standing arrangements, the population-level network topology reflects accumulated prior commitments rather than the distributed, contemporaneous governance decisions of its participating Selves. The distributed-governance property of the FAI network — one of the architectural features Claim 6's extension commits to — is not present when topology is institutionally determined rather than governance-determined.

The mechanisms through which topology lock-in arises are governance-layer, not architectural. The architecture does not produce lock-in; governance arrangements that contain lock-in provisions produce it. This distinction is the reason AP-25 operates in the calibrated-humility register: the architecture is designed to prevent lock-in, and whether it occurs in any specific deployment depends on whether the governance practitioners who author standing configurations and cross-organizational agreements honor the exit-rights requirements the architecture specifies.

---

## 3. Detection Criteria

Three observable conditions indicate topology lock-in may be present:

**Standing configurations without unilateral revocation rights.** A standing configuration governs how a Self participates in one or more ongoing FAI relationships — which aspects it contributes, at what cardinality, under what persistence policy. If the standing configuration contains provisions that prevent the Self from revoking or modifying the configuration unilaterally with appropriate notice, the amendment-protocol requirement is absent or restricted. The Self's participation is governed by a configuration it cannot exit.

**Cross-organizational agreements without workable termination governance.** A cross-organizational agreement coordinates participation across distinct governance perimeters. If the agreement's termination governance — the provisions that specify how either party may end the agreement — is absent, or if the specified termination process is practically impossible to execute (prohibitive notice periods, requirement for unanimous consent among many parties, financial penalties disproportionate to exit, termination conditioned on successor-party designation), the agreement has become a lock-in vehicle. The formal right to exit may nominally exist; the practical ability to exercise it does not.

**Governance practitioners reporting inability to exit.** When the humans who govern a Self report that they wish to exit or substantially modify a FAI relationship but cannot do so because of existing agreement provisions, topology lock-in is operationally present regardless of the formal structure of the arrangements. This is the practitioner-facing signal that the governance commitment has been compromised in practice.

---

## 4. Governance Commitment Violated

**Primary violation — exit rights governance.** The exit right is an expression of home governance sovereignty. A Self's governance authority over its own coordination posture includes the authority to decide which FAI relationships to enter, which to maintain, and which to terminate. A governance arrangement that prevents the exercise of this authority violates home governance sovereignty directly. The exit right is not a convenience feature; it is the enforcement mechanism for home governance authority over network participation. When it is foreclosed by a governance arrangement, the governance arrangement has appropriated an authority that belongs, architecturally, to the home governance perimeter.

**Secondary violation — Paper 1 Claim 3 (human-governed authority).** Paper 1's human-governed commitment specifies that humans retain three rights at all times: the right to inspect, the right to modify, and the right to override. These rights apply to substrate content and to orchestration rules. The override right is the architectural expression of the authority to change course — to exit a relationship that governance no longer finds appropriate is an instance of the override right at network-participation scope. If governance cannot exercise the override right to exit a relationship, the structural-authority property that Paper 1 Claim 3 commits to is compromised at the network-topology dimension. Paper 3 extends Paper 1's commitments to inter-Self scope without replacing them; topology lock-in is therefore a Paper 1 Claim 3 violation extended to the population-scope failure register.

**Operational reference.** The exit rights governance sub-commitment (D2.46) names forced lock-in explicitly as the anti-pattern it is designed to prevent. AP-25 formalizes the same failure mode at the anti-pattern register, with detection criteria and resolution that extend the operational content of D2.46.

---

## 5. Consequences (Calibrated-Humility Register)

The following consequences are projected from the architecture's commitments. They describe what topology lock-in would produce if it occurred, not what it necessarily produces in any specific deployment.

**Governance cannot adapt topology to current needs.** A Self's governance needs change over time. FAI relationships that were valuable when entered may become less valuable, may conflict with current governance priorities, or may have served their purpose and no longer warrant the resource commitment they require. When topology is locked, governance cannot adapt the Self's network participation to reflect these changes. The locked-in relationships continue to consume governance attention and substrate resources regardless of whether they continue to serve governance purposes.

**Portfolio management is impaired.** The FAI portfolio — the set of relationships a Self maintains and the governance resources allocated to each — is a governance object under home governance authority. Portfolio management, which involves adding relationships that serve current needs and terminating relationships that do not, requires exit rights as a precondition. When exit rights are foreclosed, portfolio management reduces to the capacity to add new relationships without being able to remove existing ones. The portfolio grows but cannot be pruned, and the allocation of governance resources across relationships cannot be freely revised.

**Network topology becomes institutionally determined.** At population scale, the distributed-governance property of the FAI network requires that each participating Self's network topology reflects its current governance decisions. If many Selves have locked topologies, the population-level network topology reflects accumulated historical governance arrangements rather than the distributed present-tense governance of its participants. The network's evolution mechanism — accumulated FAI events under each Self's home governance authority — cannot operate at full effectiveness when the topology over which FAI events occur is institutionally fixed rather than governance-determined.

---

## 6. Intra-Self Analog

There is no exact intra-Self analog for AP-25. Topology lock-in is specific to the inter-Self relationship governance that Paper 3 introduces. The architecture of a single Self — governed under Papers 1 and 2 — does not include FAI relationships with other Selves; the exit-rights question at inter-Self scope simply does not arise within a single Self's governance perimeter.

The nearest intra-Self parallel would be a Self that cannot restructure its internal aspect arrangement because of binding obligations — a Self locked into a particular cell configuration or role structure by commitments it cannot revise. This parallel exists in a logical sense: both cases involve a governance arrangement that prevents a governance authority from exercising authority it should hold. But the parallel is weak because the mechanism is different and the population-scale consequence is absent. Intra-Self aspect restructuring is a home governance matter that does not propagate consequences across the network.

AP-25 is primarily a population-scope governance failure mode. Its significance is specific to the inter-Self coordination layer that Paper 3 introduces, and its consequences acquire their full weight only at population scale.

---

## 7. Resolution

The prevention is architectural, and the architecture's commitment is already in place. Exit rights governance commits to every governance arrangement preserving exit rights as a condition of its architectural validity. Any governance arrangement provision that prevents a Self from exercising its exit rights is invalid under the architecture's governance sovereignty commitments. This is not a procedural recommendation; it is an architectural prior-art claim. Lock-in provisions are outside the scope of permissible governance arrangements by construction.

The operational implementation of this commitment runs through two governance-arrangement types:

**For cross-organizational agreements,** two components must be present and must be non-vacuous. The termination governance component must specify a feasible termination process — one that either party can execute with appropriate notice, without requirements for successor-party designation, without unanimity requirements that could be blocked by any single other party, and without financial or procedural penalties that would make exit practically impossible despite being nominally available. The amendment protocol component must preserve each Self's ability to revoke its participation in standing configurations that operate under the agreement; an amendment protocol that requires bilateral or multilateral consent to any change that reduces a Self's participation is a lock-in mechanism in amendment-protocol form.

**For standing configurations,** the amendment protocol requirement must allow unilateral revocation by either party with appropriate notice. The notice period may be specified and may be substantial where operational continuity warrants it; the requirement is that the revocation right itself is unilateral and unconditional, not that exit is instantaneous. A standing configuration that can only be terminated by mutual agreement is a lock-in vehicle, because the other party's consent becomes a veto over the revocating Self's exit.

The governance practitioners who author standing configurations and cross-organizational agreements bear the implementation responsibility. The architecture specifies that exit rights must be preserved; governance practitioners implement this specification by ensuring that the arrangements they author contain the required termination and amendment provisions and do not contain lock-in provisions.

Where topology lock-in has already occurred — where a Self finds itself party to arrangements that do not satisfy these requirements — the remediation path runs through the same governance-layer mechanisms. The architecture cannot unilaterally dissolve a governance arrangement that external parties have accepted; but it can supply the standard against which practitioners evaluate their existing arrangements and the vocabulary for governance practitioners to surface the problem, escalate it under Paper 3's three-tier conflict-handling mechanism (D1.13–D1.16), and negotiate arrangements toward architecturally valid forms.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-25: Topology Lock-In.* May 15, 2026. ORCID: 0009-0004-8065-3235.
