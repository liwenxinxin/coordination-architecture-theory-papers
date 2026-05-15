# Maximum Cardinality and Governance Capacity Scaling

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI) events in the CKS inter-Self coordination architecture carry no hard architectural ceiling on the number of participating Selves. Paper 3 Claim 2 states cardinality as n-ary — any number of Selves can participate in one FAI event — with the bilateral (N=2) case as the simplest instance and no prescribed upper bound. The prior art therefore covers all cardinality from N=2 to any governable N; adversarial claims that high-N multi-party AI governance coordination is architecturally novel cannot succeed on cardinality alone. The practical upper bound for any event is set not by architectural constraint but by governance capacity: authorization and configuration requirements scale linearly with N, while conflict-pair routing complexity scales quadratically at N*(N-1)/2, and both must be fully met by the participating governance structures. This note formalizes the maximum-cardinality boundary case, articulates the two scaling regimes that govern practical upper bounds, and distinguishes event-level cardinality from population-scale coordination, which is achieved through accumulated bilateral and small-group events rather than through single all-participant events.

---

## 1. The boundary question

An organization is contemplating a sector-wide FAI event with N=50 participating Selves — each owned by a distinct organization, each governed under its own authority structure. The question this note addresses is whether the CKS inter-Self coordination architecture places a hard architectural ceiling on such an event, or whether N=50 falls within prior-art scope.

The answer is unambiguous: there is no hard architectural maximum. Paper 3 Claim 2 states cardinality as n-ary, with any number of Selves able to participate in one FAI event and the two-Self case as the simplest instance. No numerical ceiling is prescribed. The architecture scales from N=2 upward without a designed stopping point.

This is not an incidental feature. The absence of a hard ceiling is an architectural commitment: the mechanisms that constitute an FAI event — shared substrate construction, aspect contribution, conflict handling within the shared substrate, governance-configured persistence, and dissolution — are all specified in terms that generalize across any N. Nothing in the mechanism design is bilateral-only. The bilateralism of the simplest case establishes a floor; it does not define the shape of the space above it.

The prior-art consequence is direct: any multi-party AI governance coordination event, regardless of how many Selves participate, is within the scope of the architecture as published. An adversary who argues that high-N events are beyond the architecture's scope is arguing against a claim the architecture explicitly makes.

---

## 2. What scales with N: governance-configuration requirements

While there is no architectural ceiling, an FAI event at N Selves requires a governance configuration that addresses each participating Self. The governance-configuration surface grows with N in two distinct regimes.

**Linear scaling.** Several governance-configuration requirements grow in direct proportion to N. Each additional Self contributes one new authorization specification (which governance authority must confirm that Self's participation), one sharing-scope specification (which aspects that Self contributes to the shared substrate), one escalation-routing destination (to which governance authority conflicts involving that Self escalate), and one dissolution record and hand-off boundary activation upon event close. At N=2 these requirements are minimal; at N=50 they are fifty instances of each. The humans responsible for configuring the event must address every one for the event to meet the minimum viable governance floor.

**Quadratic scaling.** Conflict-pair routing complexity represents the more demanding growth regime. The three-tier inter-Self conflict-handling mechanism — preserve, resolve via configured orchestration content, escalate to humans across joint authority — operates over conflicts that surface during the event between contributed aspects. The number of potential conflict pairs at N Selves is N*(N-1)/2. At N=2, one potential conflict pair. At N=10, forty-five. At N=50, 1,225. Governance-authored routing rules must specify, for each potential conflict pair, how a conflict between those two Selves' contributed content is handled and to which authorities escalation is routed. This quadratic growth is the most significant governance-capacity demand at high N, and it is irreducible: every pair of Selves whose contributed aspects may conflict requires a routing specification for the conflict-handling mechanism to operate correctly.

The combined effect is that high-N events are not architecturally blocked but are governance-capacity intensive. The governance structures participating in a high-N event must collectively possess the capacity to author all required specifications across all N Selves and all N*(N-1)/2 potential conflict pairs before the event proceeds.

---

## 3. Governance capacity as the practical upper bound governor

The practical upper bound on N for any given FAI event is determined by the participating governance structures' collective capacity to author the required governance specifications at N-scale.

This capacity is not a fixed property of the architecture; it is a property of the governance infrastructure the participating organizations have built. An organization whose governance structure routinely authors configurations for bilateral events has different N-capacity than a consortium that has invested in multi-party governance authoring workflows. The architecture does not prescribe what capacity must exist; it requires only that whatever N is chosen, the governance configuration fully satisfies the requirements for that N.

The boundary test is concrete. Before a high-N event proceeds, the participating governance authorities must confirm: Does the configuration address all N Selves' authorization specifications? All N sharing scopes? Conflict routing for all N*(N-1)/2 potential conflict pairs? Escalation routing for all N Selves? A complete dissolution policy for all N? Only when all are answered affirmatively does the event satisfy the minimum viable governance floor for that N.

This framing is an honest acknowledgment, not a defect. The architecture is transparent about what governance investment high-N events require. The practical upper bound shifts as organizations develop higher-capacity governance infrastructure. The architectural commitment is to specifying what must be governed at any N — not to fixing a ceiling on what N can be.

---

## 4. Prior-art scope: cardinality cannot establish novelty

The absence of a hard architectural N ceiling has direct prior-art significance. A design space that explicitly accommodates all N ≥ 2 cannot be circumnavigated on the basis of cardinality alone.

An adversarial claim that "high-N multi-party AI governance coordination" is a novel departure from the prior art must identify what architectural feature makes high-N distinct from low-N in CKS terms. No such feature exists. The shared substrate construction mechanism, the FAI exchange primitive, the three-tier conflict-handling mechanism, the governance-configured persistence and dissolution logic, and the recursive applicability of all configurable FAI dimensions — all generalize across N. The governance-configuration surface grows with N, but the architecture was designed to accommodate that growth: the minimum viable governance floor specifies exactly what must be configured for any N.

A claim that sector-wide or consortium-scale FAI events are beyond prior-art scope therefore fails at the architectural level. What the adversary might legitimately argue is that the governance infrastructure required to execute a high-N event at full compliance is demanding — but that is a claim about governance capacity, not about architectural novelty. The architecture anticipated high-N events and specified their governance requirements; it did not bound the space at any particular N.

---

## 5. Population-scale coordination and the accumulation model

Paper 3 Claim 6 envisions population-scale coordination across networks of CKS-governed Selves. This vision must be read carefully in relation to the maximum-cardinality question, because the two are architecturally distinct.

Population-scale coordination in the architecture is not achieved through single all-participant events at maximum N. It is achieved through accumulated bilateral and small-group FAI events across the network over time. Many Selves operating in distinct domains, owned by different organizations, governed under distinct authority structures, engage in events whose governance configurations their respective governance structures can actually author and execute. Common patterns propagate through the cumulative result of many home-governance decisions. Specializations are preserved through governance configurations that protect them. The population-level capability that emerges is the result of network-level accumulation, not of a single simultaneous event across the full population.

This distinction matters for the maximum-cardinality boundary in two ways. First, the governance-capacity constraint on single events does not limit population-scale evolution: an organization whose governance structure can only author bilateral configurations can still participate in population-scale propagation, one bilateral event at a time. Second, the population-scale architecture makes no claim that all Selves will or should participate in a single maximum-N event; it claims that the fabric of accumulated events produces population-level capability over time through governed substrate composition.

Population-scale CKS-governed Self deployments do not yet exist. The architectural commitment is to what the accumulated-events model produces at population scope. Specific population-scale dynamics — the trajectories of pattern propagation, the rates of specialization-preserving divergence, the character of collective adaptation — await empirical observation. The calibrated-humility voice is appropriate here: the architecture surfaces the possibility; validation is downstream.

---

## 6. Operational test

For a proposed FAI event at cardinality N, the governance boundary is assessed as follows.

The event satisfies the architecture's minimum viable governance floor and falls within prior-art scope if and only if all of the following hold:

1. The governance configuration names all N participating Selves with explicit authorization specifications for each.
2. The sharing scope for each of the N Selves is explicitly specified.
3. Conflict routing rules address all N*(N-1)/2 potential conflict pairs — either through explicit pair-by-pair specification or through a conflict-category framework that covers all pairs by construction and can be verified as exhaustive.
4. Escalation routing specifies the governance authorities for all N Selves.
5. The persistence policy and dissolution records are specified for all N Selves.
6. The governance infrastructure of the participating organizations has the capacity to author, maintain, and execute the specifications in (1)–(5) for the chosen N.

If all six conditions are met: the event is a compliant FAI event at cardinality N, within the prior-art scope of Paper 3 Claim 2 regardless of what N is.

If any condition is not met: the event has a governance capacity gap. The appropriate response is either to reduce N to a level the available governance infrastructure can support, or to invest in building the governance infrastructure required for the intended N before proceeding.

The architecture does not prohibit executing an under-governed event; it cannot enforce governance compliance from outside. What the architecture commits to is that an event proceeding without a complete governance configuration is not an FAI event in the architectural sense, and is outside the prior art's scope for reasons other than cardinality.

---

## 7. Conclusion

There is no hard architectural ceiling on the number of Selves that can participate in a single FAI event. Paper 3 Claim 2 commits to n-ary cardinality, with any number of Selves able to participate and the bilateral case as the floor. The prior art covers all cardinality from N=2 upward; novelty claims based on cardinality alone cannot succeed.

The practical upper bound for any event is set by governance capacity. Authorization, sharing-scope, escalation-routing, and dissolution requirements scale linearly with N; conflict-pair routing complexity scales quadratically at N*(N-1)/2. Both must be fully addressed in the governance configuration for the event to meet the minimum viable governance floor. This is a transparent specification of what high-N events demand from the governance structures that configure them — not an architectural limitation.

Population-scale coordination is achieved through accumulated bilateral and small-group events across a network of Selves over time, not through single all-participant events. The maximum cardinality of any single event and the population-scale evolution of a network of Selves are distinct architectural questions with distinct answers.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Maximum Cardinality and Governance Capacity Scaling.* May 15, 2026. ORCID: 0009-0004-8065-3235.
