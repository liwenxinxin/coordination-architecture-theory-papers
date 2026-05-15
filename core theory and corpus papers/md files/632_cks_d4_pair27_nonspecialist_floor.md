# Final Additional Composition Pair: Non-Specialist Governance and Minimum Viable Governance Floor

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes the composition of two Paper 3 derivation commitments: the non-specialist governance principle (D2.75), which holds that operational governance practitioners without specialist AI technical expertise can govern Full Aspect Integration (FAI) events, with governance authority remaining with non-specialists even when specialists assist with labor; and the minimum viable governance floor (D2.37), which specifies seven irreducible requirements constituting the minimum for a compliant FAI event. Considered separately, each commitment is tractable. The non-specialist governance principle names who governs; the governance floor names what they must produce. Composed, they generate three non-obvious requirements that neither commitment produces alone. First, the floor functions as the operational test for non-specialist accessibility: if non-specialist practitioners can meet all seven floor requirements, the architecture has kept its accessibility commitment; if any requirement is uninterpretable without specialist expertise, the floor itself has an accessibility defect that must be corrected at the specification level. Second, the authority-labor distinction must be applied per floor requirement: every requirement carries an authority dimension that governance must personally decide or authorize, and a labor dimension that specialists may assist with, and governance practitioners need this decomposition made explicit for each requirement to understand what they must personally do. Third, the floor specification itself must satisfy the non-specialist readability standard: a floor written in technical language cannot be self-checked by the practitioners it governs, closing the gap between meeting the floor and being able to verify that one has met it. Any governance framework positioning itself as an "AI governance floor standard for non-specialist practitioners" must address these three properties.

---

## 1. Why this composition needs to be named

Paper 3's non-specialist governance principle (D2.75) is a commitment about who holds authority over FAI events. The governance practitioners conducting an FAI event need not possess specialist knowledge of AI architecture, substrate schema design, or orchestration rule mechanics. Authority is theirs by construction; what specialists contribute is labor under governance direction, not authority over governance outcomes.

Paper 3's minimum viable governance floor (D2.37) is a commitment about what a compliant FAI event must produce. Seven requirements are irreducible: governance cannot hold a compliant FAI event without all seven, and no requirement can be collapsed into another without losing a structurally necessary governance property.

The two commitments are often discussed in sequence — practitioners learn the floor requirements, then learn that they can be met without specialist expertise — but the sequence conceals a deeper relationship. The non-specialist governance principle and the governance floor are not simply two things that happen to coexist in the same architecture. Composed, they constrain each other in ways that produce requirements neither commitment generates on its own. This note formalizes three such requirements.

---

## 2. The pair

**Commitment A — Non-Specialist Governance Principle (D2.75).** Governance practitioners without specialist AI technical expertise can govern FAI events. The governance authority that Paper 3 assigns to humans across the inter-Self perimeter — authority to configure the FAI event, to authorize the aspects each Self contributes, to decide how conflicts are handled, to specify the persistence policy — is exercisable by practitioners who do not possess specialist expertise. Specialists may assist with the labor of execution: authoring technically complex orchestration rules, constructing the shared substrate, implementing governance decisions in the substrate. They do not thereby hold governance authority. The non-specialist governance principle holds that governance authority is accessible to non-specialists by architectural design, not by exception or workaround.

**Commitment B — Minimum Viable Governance Floor (D2.37).** Seven requirements are irreducible for a compliant FAI event. An event missing any one of the seven is not a compliant FAI event in the CKS sense, regardless of how otherwise well-executed it is. The floor is a minimum: meeting it does not exhaust what good governance can produce, but every floor requirement is genuinely necessary rather than aspirational.

---

## 3. The governance scenario

An organization's governance practitioners — non-specialists in the D2.75 sense — are conducting their first FAI events. They hold governance authority over the events. They have access to specialist staff who can assist with technical execution. They need to ensure that their events meet the governance floor (Commitment B), and they need to be able to do this without acquiring specialist expertise (Commitment A). Both commitments apply simultaneously: the floor must be met, and it must be meetable by the people who are actually conducting governance.

This scenario is the standard case rather than the edge case. Governance of AI coordination systems in most organizations will be conducted by practitioners whose expertise is in the domain the system serves — legal, operational, clinical, financial — not in AI architecture. The composition question is therefore a practical governance design question: what does an architecture that commits to both floor compliance and non-specialist accessibility require of itself?

---

## 4. Non-obvious requirements from the composition

### Requirement 1 — The floor is the operational test for non-specialist accessibility

Considered alone, the non-specialist governance principle is a claim about accessibility: governance is exercisable by non-specialists. Considered alone, the governance floor is a compliance standard: these seven things must be present. Composed, the floor becomes more than a compliance standard — it becomes the test through which the non-specialist governance commitment is verified or falsified.

The logic runs in both directions. If non-specialist practitioners can meet all seven floor requirements, then the non-specialist governance principle is operational: the architecture has delivered accessibility for this class of governance event. If any floor requirement cannot be met by non-specialist practitioners — because interpreting the requirement, verifying whether it is satisfied, or making the governance decision it calls for requires specialist expertise — then the architecture has a non-specialist accessibility failure at that requirement, regardless of how accessible the other six requirements are.

This bidirectionality is what the composition produces. A governance floor that is genuinely meetable by non-specialists is an accessibility guarantee — practitioners can use the floor as a checklist that, when satisfied, gives them confident self-certification of compliance. A governance floor that contains even one requirement opaque to non-specialists breaks the accessibility promise at that requirement. The composition therefore requires that every floor requirement be specified in terms non-specialists can interpret and evaluate, or the floor itself must be respecified. The floor is not just what governance must produce; it is the architectural measure of whether the accessibility commitment holds in practice.

### Requirement 2 — Authority and labor must be decomposed per floor requirement

The authority-labor distinction — that governance authority is non-delegable while governance labor is allocable to specialists — is established at Paper 1 and applies throughout Paper 3. What the composition adds is that this distinction must be applied at the level of each individual floor requirement, not at the level of governance as a whole.

Governance practitioners navigating their first FAI events face a concrete practical problem: for each of the seven floor requirements, what do they personally need to decide or authorize, and what can specialists execute on their behalf? The non-specialist governance principle says that governance authority is theirs; the floor says that seven requirements must be met. Neither commitment, taken alone, gives practitioners a map from the seven requirements to the specific decisions they must personally make.

The composition produces that map. For each floor requirement, there is an authority dimension — the governance decision or authorization that cannot be delegated because it belongs to governance's non-delegable authority under Paper 1 — and a labor dimension — the technical execution, complex rule authoring, or substrate construction that specialists can assist with. Authority over each requirement must be exercised by governance; labor for each requirement can be allocated. Practitioners who understand only the floor requirements without the authority-labor decomposition per requirement will either over-delegate (delegating governance decisions to specialists) or under-delegate (performing specialist labor themselves when governance authority is already satisfied). The composition's practical product is a governance tool: a per-requirement decomposition that maps each floor requirement to what governance must personally decide and what specialists can help execute.

### Requirement 3 — Floor specification language must satisfy the non-specialist standard

The non-specialist governance principle, combined with Paper 1's governance records standard, requires that governance records be readable without specialist expertise. This readability requirement applies not only to governance records produced during an event but to the floor specification itself — the statement of what each floor requirement means and how governance knows whether it has been met.

A floor requirement specified in technical language is a floor requirement that governance cannot self-check. If the specification of a requirement reads: "authored orchestration rules implementing the three-tier conflict-handling mechanism with preserve as substrate-level state default and resolve tier operating through inspectable rules," a non-specialist practitioner cannot readily determine whether their event satisfies it. The same requirement in non-specialist-accessible language might read: "a written set of jointly-agreed rules specifying how disagreements between the contributing parties' materials will be handled, including which disagreements will be left open, which will be resolved during the event, and which will be referred to both organizations' governance for a decision." Both statements name the same architectural requirement; only the second is self-checkable by its intended users.

The composition requires that each floor requirement be specified in terms meeting the same readability standard as the governance records the floor produces. This is not a dumbing-down of technical content; it is an accessibility specification for the compliance instrument itself. A floor whose requirements are inaccessible to the practitioners it governs is not a non-specialist-accessible floor, regardless of the accessibility of the underlying architecture.

---

## 5. Prior-art significance

The three requirements this composition produces define a non-trivial prior-art space. Any architecture advancing a governance floor standard for non-specialist practitioners must address all three:

- The bidirectionality property — floor as operational test for accessibility, with floor requirements that are opaque to non-specialists constituting accessibility failures requiring respecification — must be addressed, not just the floor's compliance function.
- The per-requirement authority-labor decomposition must be addressed as a practical governance instrument, not merely the general authority-labor distinction at the level of governance as a whole.
- The accessible floor specification requirement must be addressed for the floor itself as a compliance document, not just for governance records produced under the floor.

These three properties, in their specific combination and mutual constraint, are what the composition of D2.75 and D2.37 formalizes. Prior art in AI governance compliance floors and non-specialist governance frameworks does not occupy this combination.

---

## 6. Operational test

For a non-specialist governance practitioner reviewing the governance floor requirements for their upcoming FAI events, the composition is satisfied if and only if all of the following hold:

1. **Floor specification accessibility.** Each of the seven floor requirements is stated in language the practitioner can interpret without specialist expertise — meaning they can read each requirement and form a judgment about whether it is satisfied by examining governance records, without needing a specialist to translate or interpret.

2. **Per-requirement authority-labor decomposition.** For each floor requirement, the practitioner can identify: (a) the specific governance decision or authorization that belongs to them personally and cannot be delegated, and (b) the technical or complex execution steps that specialists can assist with while governance authority remains with the practitioner.

3. **Self-certification from governance records alone.** The practitioner can verify that all seven floor requirements are met by reviewing governance records they can read and evaluate, without specialist assistance. Their review produces a defensible compliance judgment — not certainty that the underlying technical implementation is correct, but confirmation that governance has authorized and recorded what the floor requires governance to authorize and record.

A governance floor that fails any of (1)–(3) has an accessibility defect at the failing requirement. The defect must be addressed at the specification level — by respecifying the requirement in non-specialist-accessible language and providing the authority-labor decomposition for that requirement — rather than by training governance practitioners in specialist skills.

---

## 7. Conclusion

The non-specialist governance principle and the minimum viable governance floor are not merely two commitments that coexist in the same architecture. Composed, they produce a requirement that the floor function as the operational test for the accessibility commitment; a requirement that governance practitioners receive a per-requirement map of what they must personally decide versus what specialists can execute; and a requirement that the floor specification itself be written in language its intended users can read and self-check. These three properties, in combination, define what a genuine non-specialist-accessible governance floor standard for FAI events must provide.

Subsequent work positioning itself as an AI governance floor standard for non-specialist practitioners should address all three. Work that provides a governance floor without the bidirectionality property is a compliance standard without an accessibility test. Work that provides the authority-labor distinction at the level of governance as a whole, without decomposing it per floor requirement, is an abstract principle without a practical governance instrument. Work that specifies floor requirements in technical language is a floor non-specialists cannot self-check. All three defects are, by the composition formalized here, accessibility failures under the non-specialist governance commitment.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Final Additional Composition Pair: Non-Specialist Governance and Minimum Viable Governance Floor.* May 15, 2026. ORCID: 0009-0004-8065-3235.
