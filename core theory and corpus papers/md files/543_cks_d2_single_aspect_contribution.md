# FAI Governance for Single-Aspect Contribution

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series note:** #543 — Phase D2, Note D2.48

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D2.48 derives from D1.06 (the aspect as the exchange unit in Full Aspect Integration) and D2.37 (the minimum viable governance floor for a FAI event). It establishes single-aspect contribution — where one participating Self contributes exactly one aspect to the shared substrate during a FAI event — as the minimum valid FAI participation unit. The note argues that single-aspect contribution is architecturally valid because the aspect, not the cell and not the full Self, is the exchange unit; contributing one aspect satisfies all of the commitments the architecture imposes on contributing Selves. It further establishes that no governance requirement is relaxed for single-aspect contribution: all seven minimum viable governance floor requirements apply unchanged. Three cases where single-aspect contribution is appropriate are identified — targeted coordination, first-time participation as a trust-calibration step, and deployment by a Self whose governance architecture comprises exactly one aspect. The note closes by positioning single-aspect contribution as the scalability minimum that anchors the architecture's range — from one aspect contributed by one Self in one event to all aspects contributed by all participating Selves across many events — and by formalizing sub-aspect (cell-level) contribution as the anti-pattern that violates the exchange-unit commitment regardless of how many cells are offered.

---

## 1. Derivation context

D2.48 sits at the intersection of two prior commitments in the series. The first is D1.06's commitment that the aspect is the exchange unit in FAI. When a participating Self contributes content to the shared substrate during a FAI event, the contribution is bounded at the aspect level: the Self surfaces the constituent cells, DNA-layer content (orchestration rules, content-domain specification, and coordination rules for the contributed aspect's cells), and action-layer content (operational records from the contributed aspect's cells) for each aspect it contributes. The commitment at D1.06 is architectural: the aspect is not a convenient grouping unit chosen at deployment time, but the defined boundary at which governed coordination content travels across the inter-Self perimeter. Below-aspect granularity strips the governance structure that makes the exchange architecturally coherent; above-aspect granularity (the whole Self) either absorbs a Self's identity or is a different kind of operation than coordination through a shared substrate.

The second commitment is D2.37's minimum viable governance floor, which specifies the seven requirements that every FAI event must satisfy regardless of its scope, cardinality, or the content of its configuration: a construction record, a dissolution record, a contribution record for each participating Self's contributed content, a FAI configuration covering all six governance dimensions, a conflict registry operating across the shared substrate, the full set of Paper 1 commitments within the shared substrate, and human-authored authority over the configuration substrate itself. D2.37 establishes these seven requirements as a floor — they cannot be waived, relaxed, or deferred in a compliant FAI event.

D2.48 derives the boundary case: a FAI event in which one participating Self contributes exactly one aspect. The derivation serves two purposes. First, it confirms that the architecture is coherent at the minimum contribution scale, which matters for prior-art coverage: any implementation in which a Self contributes one or more aspects to a shared substrate in a governance-configured FAI event is within the architecture's scope. Second, it closes the specification of what counts as FAI participation, by naming the minimum valid unit (one aspect) and explicitly excluding the sub-aspect approach (individual cells without aspect governance context) as an anti-pattern.

---

## 2. Why single-aspect contribution is architecturally valid

The aspect-as-exchange-unit commitment (D1.06) implies the minimum valid exchange is one aspect. This is not a corner case that needs special treatment; it is the direct consequence of what the commitment means. If the aspect is the exchange unit, then the minimum number of exchange units a contributing Self can offer is one.

A Self contributing one aspect to the shared substrate during a FAI event contributes a fully structured governance unit. The aspect's DNA-layer content travels with it: the orchestration rules that govern the contributed aspect's cells, the content-domain specification that bounds what the aspect operates over, and the coordination rules that govern how the aspect's cells relate to one another. The aspect's action-layer content also travels: the operational records accumulated by the aspect's cells, representing the lived governance experience the contributing Self is surfacing for shared coordination. All six Paper 1 commitments — human-governed substrate, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, provenance, and linear-cost scaling — hold within the shared substrate as soon as one aspect's content enters it, because those commitments are properties of the shared substrate's architecture, not properties that scale with the number of aspects contributed.

The single-aspect case does not relax these commitments. A conflict arising between the contributed aspect's content and a receiving Self's contributed content is first-class substrate state by Paper 1 inheritance, regardless of how many aspects were contributed by each side. The provenance metadata traveling with the contributed aspect's cells retains its structure regardless of whether ten other aspects traveled alongside it. Human authority over the shared substrate's configuration and content applies from the moment the shared substrate is constructed, not from the moment some contribution threshold is crossed.

The other aspects in the contributing Self's home architecture remain within the home governance perimeter. They are not contributed, they are not visible to the shared substrate's participants, and no governance obligation arises with respect to them from the FAI event. The contribution record (D2.06) documents what was contributed; the fact that the contributing Self has additional aspects beyond the one contributed is outside the shared substrate's governance scope.

---

## 3. Governance requirements unchanged for single-aspect contribution

Every minimum viable governance floor requirement (D2.37) applies to a single-aspect FAI event without modification.

The **construction record** exists for the event as a whole. It records when the shared substrate was constructed, who the participating Selves are, and under whose authority the construction was authorized. None of these fields change because the contribution scope is one aspect rather than many.

The **dissolution record** exists for the event as a whole. It records when the shared substrate is dissolved and what becomes of the content it carried. The dissolution governance obligation does not diminish because the substrate held one aspect's content rather than many.

The **contribution record** exists for each contributing Self. For a Self contributing one aspect, the contribution record documents that aspect: its DNA-layer content, its action-layer content, and the scope commitment that this aspect — and no others from that Self's home architecture — was contributed. The contribution record is complete with one entry; it is not deficient because there is only one entry.

The **FAI configuration** specifies all six governance dimensions regardless of contribution scope. The configuration still names which aspects are contributed by which Selves (the answer for the single-aspect contributor is "one aspect"), how the full-merge default is applied or overridden, how conflicts are handled, what the dissolution terms are, what authority each participating Self retains over the shared substrate during the event, and what provenance carries. None of these dimensions is vacated by small contribution scope.

The **conflict registry** operates over whatever content is in the shared substrate. A conflict arising from one contributed aspect merging with another Self's contributed content is a conflict as fully as any other. The registry's obligation to record and preserve conflicts as first-class substrate state is not scope-dependent.

The **Paper 1 commitments** within the shared substrate hold from the moment the shared substrate is constructed. The substrate is human-governed because the configuration was authored under human authority and the override rights are preserved; that property does not require a minimum content volume.

The **human-authored authority** over the configuration substrate (D2.37's seventh requirement) applies to the governance configuration of this event. The humans holding authority over the shared substrate during a single-aspect event hold the same architectural rights as the humans holding authority during a many-aspect event.

The practical consequence is that there is no governance discount for small contribution scope. A compliant single-aspect FAI event is as demanding to document, configure, and dissolve as a compliant many-aspect event. The architecture does not offer a simplified pathway for minimal participation. What changes is not the governance structure but only the content volume — one aspect's DNA and action layers rather than many.

---

## 4. Three cases where single-aspect contribution is appropriate

Three deployment circumstances make single-aspect contribution the correct choice. These are not the only circumstances that could arise, but they are the archetypal cases the architecture accommodates.

**Case 1 — Targeted coordination.** A FAI event may be organized around a specific, bounded coordination problem that corresponds to one operational domain — an aspect. Contributing all aspects would expose governance architecture for other operational domains that have no bearing on the event's purpose. Where the coordination objective is narrow and aspect-bounded, single-aspect contribution is the architecturally appropriate scope. It surfaces exactly the content relevant to the shared objective and withholds the rest. The home governance perimeter of the contributing Self does the boundary-maintenance work: other aspects are simply never surfaced to the shared substrate.

**Case 2 — First-time participation as a trust-calibration step.** D2.29 established trust calibration as a governable mechanism within the FAI architecture: the scope of content shared during a FAI event can be calibrated to the current state of inter-organizational trust, and trust evidence accumulates as a function of FAI event history. Single-aspect contribution is the natural entry point for a Self conducting its first FAI event with a new partner. By contributing one aspect, the participating Self creates a construction record, a contribution record, and a conflict registry — all of which become trust evidence that subsequent events can build on. The graduated adoption path this enables is significant: organizations new to inter-Self coordination can participate minimally, accumulate documented governance history, and expand contribution scope as the trust evidence base grows. Nothing in the architecture requires this graduated path; everything in the architecture supports it.

**Case 3 — Single-aspect governance architecture.** A Self whose governance architecture comprises exactly one aspect contributes its entire governance architecture by contributing that one aspect. This is not a minimal contribution in the sense of withholding; it is the maximum contribution available given the Self's structure. The single-aspect case in Case 3 is indistinguishable from the structural perspective of the shared substrate: it sees one contributed aspect with its full DNA and action layers, with contribution records documenting the scope, regardless of whether the contributing Self chose to limit its contribution (Case 1 and Case 2) or contributed its entire governance structure (Case 3). The architecture handles all three cases under the same commitments.

---

## 5. Single-aspect contribution as the scalability minimum

The architecture's claim to scope coverage depends on establishing that the same commitments operate at every contribution scale. D2.48 establishes the floor. The scalability range runs from the minimum — one aspect contributed by one Self in one event — to the maximum — all aspects contributed by all participating Selves across many events in a sustained coordination relationship. Within that range, every intermediate configuration (some aspects from some Selves in some events) inherits the same governance architecture.

This has a prior-art consequence. Because the architecture is defined at the aspect level and because D2.48 confirms it is coherent at the one-aspect floor, any implementation that contributes one or more aspects to a shared substrate in a governance-configured FAI event is within the architecture's scope. The contribution does not need to be large, sustained, or multi-aspect to be within the architecture's prior-art perimeter. The floor is one aspect. The ceiling is all aspects of all participating Selves.

The scalability argument also runs in the other direction. Because single-aspect contribution does not relax any governance requirement, expanding contribution scope from one aspect to many does not require a governance transition. The governance architecture already in place for a single-aspect event — the construction record, the contribution records, the FAI configuration, the conflict registry, the dissolution record — is the same architecture that governs a many-aspect event. Scale changes content volume; it does not change governance structure.

---

## 6. The anti-pattern: sub-aspect (cell-level) contribution

The anti-pattern to single-aspect contribution is sub-aspect contribution: a Self contributing individual cells to the shared substrate rather than aspects, on the premise that cells are a simpler or more granular form of exchange.

Sub-aspect contribution violates D1.06's commitment that the aspect is the exchange unit. A cell contributed without its aspect's governance envelope — without the orchestration rules, content-domain specification, and coordination rules that the aspect provides — is a fragment below purpose-coherence. The cell carries its own provenance metadata, but it does not carry the governance context that makes the exchange interpretable within the shared substrate. The receiving Self and the shared substrate's governance configuration cannot determine from the cell alone what operational domain it belongs to, what rules govern its behavior, or how it relates to the other cells in the contributing Self's aspect.

The practical consequence is that sub-aspect contribution degrades the shared substrate's governance properties. Conflicts arising from cell-level content are harder to attribute to a governed source. The contribution record cannot be written coherently because the unit of contribution does not correspond to the architecture's defined exchange unit. The FAI configuration's content-domain specification — which is written at the aspect level — cannot be applied to individual cells contributed outside their aspect structure.

The anti-pattern may appear superficially attractive because it seems to reduce contribution scope further than single-aspect contribution. It does not. Single-aspect contribution is not "one aspect selected from a range of possible contribution granularities"; it is the minimum contribution that satisfies the architecture's commitments. Sub-aspect contribution is not a further reduction; it is a violation of the exchange-unit commitment. There is no version of cell-level exchange that constitutes a compliant FAI event, regardless of how many cells are offered or how carefully they are selected. The architecture explicitly requires aspect-level exchange, and that requirement does not scale down.

---

## 7. Operational test

The following test applies to a FAI event in which one participating Self (Self A) contributed exactly one aspect (Aspect X) to the shared substrate. An observer can confirm the event is a compliant single-aspect FAI event if and only if all of the following are true:

1. **Construction record exists.** A record documenting the shared substrate's construction is present, naming the participating Selves, the construction authority, and the construction date.

2. **Contribution record exists for Aspect X.** A record documents that Self A contributed Aspect X, including the DNA-layer content (orchestration rules, content-domain specification, coordination rules for Aspect X's cells) and the action-layer content (operational records from Aspect X's cells).

3. **Contribution scope is bounded at the aspect level.** The contribution record confirms that Aspect X — not individual cells from Aspect X, and not any other aspect from Self A's home architecture — was the contributed unit. Self A's other aspects are absent from the shared substrate.

4. **FAI configuration covers all six dimensions.** The governance configuration for the event specifies: which aspects each Self contributed (one aspect from Self A), how the merge default is applied or overridden, how conflicts are handled, what the dissolution terms are, what authority each Self retains during the event, and what provenance carries.

5. **Conflict registry is operational.** Any conflicts arising from the merge of Aspect X's content with other contributed content are recorded as first-class substrate state. The absence of conflicts is permissible; the absence of a conflict registry is not.

6. **All six Paper 1 commitments hold within the shared substrate.** The shared substrate is human-governed (the three rights — inspect, modify, override — are preserved for the participating humans), conflict-preserving, AI-mediated, tool-agnostic, provenance-carrying, and constructed at linear cost.

7. **Dissolution record exists or is committed.** A dissolution record documenting the event's closure terms exists or is specified in the FAI configuration as a future obligation.

A FAI event that satisfies all seven requirements is a compliant single-aspect FAI event. A FAI event that contributes cells rather than Aspect X fails requirement 3 regardless of how many cells are contributed; cell-level contribution is not a compliant lower-scope variant of single-aspect contribution.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance for Single-Aspect Contribution.* May 15, 2026. Series note #543 (Phase D2, Note D2.48). ORCID: 0009-0004-8065-3235.
