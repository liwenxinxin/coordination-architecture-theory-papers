# FAI Event Scope Boundaries

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series note:** D2.42 — #537 in the CKS derivation-note series

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 of the CKS theory series makes specific architectural commitments about what happens inside a temporarily constructed, perimeter-spanning, governance-configured shared substrate during a Full Aspect Integration (FAI) event. Those commitments are precise because they are scoped. This note formalizes that scope: four conditions that must all hold for an activity to fall inside a governed FAI event, four categories of activities that fall outside it, the defensive prior-art function the scope boundary performs, and an operational test that any observer can apply to a claimed FAI event. The scope boundary forecloses two adversarial positions — over-inclusion (treating any inter-AI coordination as a FAI event) and under-inclusion (treating Paper 3's governance commitments as inapplicable because an exchange does not look formal enough) — and preserves the architecture's claim-precision for downstream work.

---

## 1. D2.42 as operational scope definition deriving from D0.01 and D1.05

D0.01 committed to the shared substrate as the architectural object of inter-Self coordination. That note anchored Paper 3's first claim: a temporarily constructed, perimeter-spanning, governance-configured-persistence shared substrate carrying all six Paper 1 commitments within scope, with the configuration of the perimeter-spanning itself substrate content under joint human authority. D1.05 named the architectural foil: opaque agent-to-agent communication — message-passing, tool-call coordination, and shared-memory access between AI Selves outside any CKS substrate.

D0.01 established what the architecture commits to. D1.05 named what it contrasts against. D2.42 establishes where the governance commitment begins and ends. It does so by formalizing the scope of a governed FAI event in both directions: what must be present for Paper 3's architecture to apply, and what falls outside that architecture even when it produces coordination between AI Selves.

The scope definition is operational. It does not describe an ideal or a target — it states the conditions that define a governed FAI event as that term is used throughout the D2 sub-series and the source papers.

---

## 2. Four conditions for inside-scope activity

An activity falls within the scope of a governed FAI event if and only if all four of the following conditions hold simultaneously.

**Condition 1 — Two or more CKS-governed Selves through a shared substrate meeting D2.37's minimum viable governance floor.** The activity must involve at least two Selves, each operating under its own home governance perimeter and each carrying the CKS substrate architecture Paper 2 specifies. The exchange must occur through a shared substrate — a substrate that spans the home perimeters of the participating Selves and that satisfies the minimum viable governance floor established in D2.37. Single-Self operations, and multi-Self exchanges that do not involve a shared substrate satisfying D2.37, are not inside scope regardless of how productive they are.

**Condition 2 — The shared substrate carries all six Paper 1 commitments within its scope.** The exchange medium must itself instantiate the six Paper 1 architectural commitments: substrate-as-coordination-artifact, human-governed, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, and linear-cost scaling. These commitments travel with the shared substrate by inheritance. An exchange medium that satisfies some Paper 1 commitments but not others does not constitute a governed FAI event's exchange medium. The governance properties of the shared substrate are not configurable down to zero — they are the definitional floor.

**Condition 3 — The participating Selves have jointly authorized a configuration for the exchange.** The exchange must be operating under a governance-configured set of parameters that both participating Selves' human authority structures have authorized. This is the joint-authority requirement: neither Self unilaterally configures the shared substrate; both home governance structures have authorized the configuration. The authorization is itself substrate content, making it inspectable and auditable. An exchange that occurs without mutual governance authorization — even through a technically compliant shared substrate — does not meet this condition.

**Condition 4 — The exchange is bounded to DNA-layer and action-layer content.** The exchange may carry DNA-layer content (orchestration substrates, behavior substrates, schemas, rules) and action-layer content (recorded task instances, outputs, lived experience) through the shared substrate. It may not carry instinct-layer content — LLM weights and instinct-layer parameters do not cross the inter-Self perimeter through a FAI event. This bounding is architectural commitment, not configuration: it holds regardless of what the governance configuration otherwise specifies for the event. An exchange that transmits or is designed to transmit instinct-layer content is not a governed FAI event.

All four conditions must hold. If any one fails, the activity does not fall within Paper 3's governed FAI architecture, regardless of whether it involves AI Selves, coordination intent, or a substrate-like medium.

Activities that are inside scope, given all four conditions, include: aspect contribution to the shared substrate during an event; conflict handling within the shared substrate through the three-tier mechanism; evolution feed outputs processed at dissolution and routed to home evolution machinery; and governed pattern propagation through chained FAI events where the output of one event becomes the input configuration basis for a subsequent event.

---

## 3. Four categories of outside-scope activities

Activities that do not meet all four inside-scope conditions fall into one of four categories. The categories are mutually exclusive as defined; any activity that fails to be an inside-scope FAI event falls into exactly one of these categories.

**Category 1 — Pre-FAI coordination.** Organizational discussions, relationship-building between teams, and governance negotiations that precede constructing a shared substrate fall outside the scope of any FAI event. This includes drafting the cross-organizational governance agreement that enables FAI and authoring the standing configuration that governs an ongoing FAI relationship. These activities occur through normal organizational channels — communications, documents, meetings — that are not themselves CKS substrates configured for inter-Self exchange. They inform and enable FAI events; they are not FAI events. The FAI governance commitment begins at shared-substrate construction, not at the moment two organizations begin discussing whether to coordinate.

The distinction is not arbitrary. Pre-FAI coordination is governed, if at all, by whatever governance frameworks the participating organizations choose to apply to their internal and inter-organizational communications. Those frameworks may be rigorous or minimal; they may or may not involve CKS substrates at the home level. None of this bears on whether the eventual shared-substrate exchange is a governed FAI event. The two regimes are separate.

**Category 2 — Post-FAI coordination.** Organizational discussions and follow-up activities after a FAI event dissolves are outside scope. After dissolution, the shared substrate either has been discarded (retention at zero) or persists as an auditable record per the governance-configured persistence policy. Either way, the FAI event is over. What happens next within each participating Self's home governance — decisions about which evolution outputs to accept, how to use absorbed DNA-layer content, whether to propose a subsequent FAI event — is home-perimeter governance, not part of the dissolved event. Governance decisions about FAI evolution outputs are home-governance activities subject to each Self's own authority structure.

**Category 3 — Non-CKS inter-Self coordination.** Coordination activities between AI Selves that do not use a shared CKS substrate fall outside the scope of Paper 3's governed FAI architecture. This is the foil category named in D1.05. Message-passing between AI Selves, tool-call coordination in which one Self issues function calls that another executes, and shared-memory access in which multiple Selves read and write to a common memory object are coordination mechanisms that may produce useful outcomes. They are not governed FAI events. Paper 3's architectural commitments do not apply to them. The six Paper 1 commitments are not inherited by them. The conflict-handling tier does not operate within them. The governance-configured exchange conditions do not bind them.

This category is the most consequential for defensive publication purposes. A party claiming that Paper 3's architecture is anticipated by prior-art systems using message-passing, tool-call coordination, or shared-memory between AI agents is claiming that Category 3 coordination constitutes FAI. It does not. The absence of a shared substrate satisfying Condition 1 and Condition 2 is dispositive. The scope boundary here is not a narrow technical distinction — it reflects the architecture's central design decision, inherited from Papers 1 and 2, that coordination knowledge belongs in a persistent governed substrate outside the LLM, not in ephemeral runtime communication channels between agents.

**Category 4 — Cross-Self influence without FAI.** If one Self observes another Self's publicly available outputs — published substrates, released artifacts, documented patterns — and uses those observations to inform home governance decisions, no FAI event has occurred. No shared substrate spans the perimeters; no joint authorization governs the exchange; no governance-configured exchange bounded to DNA-layer and action-layer content is taking place. The observing Self is simply conducting research and feeding it into its own home governance processes. This is legitimate and valuable activity. It is not a governed FAI event, and Paper 3's architecture does not govern it. Treating cross-Self observation as a FAI event would extend Paper 3's governance commitments to any instance of learning from publicly available work, which is not what those commitments mean.

---

## 4. The scope boundary as prior art: forecloses over-inclusion and under-inclusion

The scope boundary performs defensive prior-art work in two directions.

**Over-inclusion foreclosed.** An over-inclusion claim holds that any inter-AI coordination constitutes a FAI event, and therefore that Paper 3's architecture is anticipated by — or equivalently, that Paper 3's claims cover — all inter-AI coordination mechanisms. The scope boundary forecloses this by specifying the four conditions that must hold. Category 3 coordination explicitly places the most common alternative coordination mechanisms outside scope. Message-passing, tool-call coordination, and shared-memory access between AI Selves are named and explicitly classified as non-FAI activities. A party attempting to claim that Paper 3 covers these mechanisms, or that these mechanisms anticipated Paper 3, faces this explicit categorization as prior art.

**Under-inclusion foreclosed.** An under-inclusion claim holds that Paper 3's architecture is so narrow in its scope — requiring a formally constructed perimeter-spanning substrate, joint authorization, and multi-organizational governance agreements — that it applies only in exotic or impractical configurations, and therefore that the architecture's claims do not protect anything practically valuable. The scope boundary forecloses this by specifying that any two CKS-governed Selves exchanging content through a shared substrate satisfying D2.37's minimum viable governance floor constitutes a governed FAI event. The floor is minimal by design: D2.37 deliberately sets a low enough bar that practical deployments qualify. The four inside-scope conditions do not require large organizations, complex governance bureaucracies, or formally negotiated treaties. They require a shared substrate that carries Paper 1's commitments, joint authorization of the exchange configuration, and bounded content exchange. These are achievable in small and simple deployments.

Both directions of foreclosure depend on the scope boundary being stated explicitly and dated. A scope boundary that is only implicit in Paper 3's architecture — visible to a careful reader but never directly stated — is weaker prior art than one that is named, formally stated with conditions and categories, and published with a date.

---

## 5. The scope boundary protects architectural precision

Paper 3's architecture makes commitments that hold within the shared substrate's scope. The six Paper 1 commitments hold within scope by inheritance. Conflict handling operates within the shared substrate through the three-tier mechanism. Evolution feeds are routed by the layer-routing rule at each home perimeter on dissolution. Configuration is substrate content under joint human authority. These commitments are precise because they are scoped — they apply to an identified architectural object (the shared substrate) during an identified temporal interval (from shared-substrate construction to dissolution) with identified parties (two or more CKS-governed Selves operating under jointly authorized configurations).

If the scope is ambiguous, the commitments lose their precision in two ways. First, a party could claim that the commitments apply to non-CKS coordination mechanisms (Category 3), which would require defending those mechanisms' equivalence to the shared substrate — an argument that misrepresents the architecture. Second, a party could claim that the commitments do not apply to a given shared-substrate exchange because the exchange does not look sufficiently formal, which would require defining formality — a question the architecture's four explicit conditions already answer.

The scope boundary resolves both imprecisions. Downstream work that extends, composes, or argues against Paper 3's architecture should use "governed FAI event" to refer to activities meeting all four inside-scope conditions and should not apply Paper 3's commitments to activities falling in any of the four outside-scope categories. Using the scope precisely is what makes the architecture's claims defensible rather than vague.

---

## 6. Anti-pattern: scope confusion

**Scope confusion** occurs when the boundary between inside-scope and outside-scope activities is not maintained, in either direction.

**Over-inclusion form:** Treating informal inter-organizational coordination (Category 1 or Category 4) or non-CKS agent coordination (Category 3) as governed FAI events. The practical consequence of this form is that Paper 3's governance commitments are asserted to apply where the shared substrate does not exist and its conditions are not met. This produces false accountability claims (the conflict-handling tier is asserted to be operating when it is not), false provenance claims (instinct/reasoning separation is asserted to be respected when it is not), and false governance claims (joint human authorization is asserted when no shared substrate carrying that authorization exists). Over-inclusion form inflates the apparent reach of the architecture while undermining the commitments that give the architecture its value.

**Under-inclusion form:** Refusing to recognize a compliant shared-substrate exchange as a governed FAI event because of the exchange's apparent scale or simplicity. If two small CKS-governed Selves exchange aspects through a minimal shared substrate satisfying D2.37's floor under jointly authorized configuration bounded to DNA-layer and action-layer content, the activity is a governed FAI event regardless of whether it involves large organizations, complex governance structures, or lengthy duration. Under-inclusion form treats the architecture as applying only to a class of large and formal exchanges that do not need to be named explicitly by the architecture — which undermines the architecture's minimum viable governance floor commitment and creates false distinctions within the class of governed FAI events.

Both forms of scope confusion damage the architecture's defensive publication value. The note establishes this anti-pattern explicitly so that downstream work can identify and correct it.

---

## 7. Operational test

For any activity claimed to be a governed FAI event, an independent observer can apply the following test. The activity is a governed FAI event if and only if all four questions can be answered affirmatively:

1. **Shared substrate and Self qualification:** Can the observer identify a shared substrate spanning the home perimeters of two or more CKS-governed Selves, and does that shared substrate satisfy D2.37's minimum viable governance floor?

2. **Six Paper 1 commitments within scope:** Does the identified shared substrate carry all six Paper 1 commitments — substrate-as-coordination-artifact, human-governed, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, and linear-cost scaling — within its scope by inheritance?

3. **Joint authorization:** Can the observer identify the governance-configured exchange parameters, and can the observer verify that both (all) participating Selves' human authority structures jointly authorized those parameters as substrate content?

4. **Exchange bounding:** Is the exchange bounded to DNA-layer and action-layer content, with instinct-layer content not crossing the inter-Self perimeter through this exchange?

If any of the four questions cannot be answered affirmatively — or if the activity falls cleanly into one of the four outside-scope categories (pre-FAI coordination, post-FAI coordination, non-CKS inter-Self coordination, or cross-Self observation without a shared substrate) — the activity is not a governed FAI event, and Paper 3's governance commitments do not apply to it.

The test is observer-applicable without access to proprietary system internals. Condition 1 requires identifying a shared substrate — a structural feature. Condition 2 requires verifying Paper 1 commitment inheritance — which, because those commitments are architectural properties of the shared substrate, follows from the substrate's design. Condition 3 requires identifying the jointly authorized configuration — which is substrate content, therefore inspectable per Paper 1's human-governed commitment. Condition 4 requires verifying exchange bounding — a claim the exchange mechanism either makes architecturally or does not.

---

## 8. Conclusion

D2.42 establishes the operational scope of Paper 3's governed FAI architecture: four conditions that must all hold for an activity to fall inside a governed FAI event, and four categories that classify activities falling outside it. The scope boundary derives from D0.01 (shared substrate as architectural object of inter-Self coordination) and D1.05 (opaque agent-to-agent communication as named foil), and formalizes the boundary that those two notes implicitly require.

The scope boundary performs defensive prior-art work in two directions: it forecloses over-inclusion by placing message-passing, tool-call coordination, and shared-memory access in Category 3 (non-FAI coordination), and it forecloses under-inclusion by establishing that any exchange meeting all four inside-scope conditions constitutes a governed FAI event regardless of scale or organizational complexity. The boundary protects architectural precision by maintaining the scope of Paper 3's specific commitments — the six Paper 1 commitments within scope, the three-tier conflict-handling mechanism, the layer-routing rule on dissolution, and the joint-authorization requirement — against both inflation and deflation.

Subsequent work that adopts, extends, or argues against Paper 3's architecture should use "governed FAI event" as defined here. Work that uses the term to cover Category 3 coordination, or that refuses to apply the term to compliant shared-substrate exchanges meeting all four conditions, is working with a different concept — and the difference should be named.

---

## Source papers

- Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.
- Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.
- Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Event Scope Boundaries.* May 15, 2026. ORCID: 0009-0004-8065-3235. CKS Derivation Note D2.42 (#537). CC BY 4.0.
