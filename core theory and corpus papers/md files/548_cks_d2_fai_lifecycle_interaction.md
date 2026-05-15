# FAI and Intra-Self Lifecycle Interaction

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When a Full Aspect Integration (FAI) event is active, the participating Selves' home substrates continue to operate under their own governance, including lifecycle events — birth of new cells or aspects, mating operations that alter DNA-layer content, and death of constituent cells or aspects. This note formalizes the governance implications of that concurrency. The core principle is lifecycle isolation: home lifecycle events do not automatically propagate into the shared substrate. The shared substrate holds the versions of contributed aspects as they existed at contribution time; subsequent home changes occur in a separate governance scope and reconnect with the FAI record only through explicit governance action — configuration amendment or withdrawal — or at dissolution via the evolution feed. The note covers each lifecycle case in turn, states the lifecycle isolation principle, derives it from D1.03's additive perimeter commitment, identifies the automatic lifecycle propagation anti-pattern, and provides an operational test. This is note D2.53 in the CKS derivation series, note #548 overall.

---

## 1. Position and scope

D2.53 is a cross-paper operational synthesis. Its two source commitments are Paper 3's FAI architecture — specifically the shared substrate's construction-time configuration (D1.22, Dimension 1: sharing scope) and the no-pause principle that home governance continues during an active FAI event (D2.23) — and Paper 2's lifecycle architecture, which specifies birth, mating, and death as the three lifecycle primitives operating at every level of the cell-aspect-Self hierarchy (B0.03, B1.05–B1.07).

The synthesis occasion is this: Paper 3 specifies that the shared substrate is constructed at a particular moment with a particular configuration, holds content contributed from aspects in existence at that time, and dissolves on completion. Paper 2 specifies that a Self's home substrate is a living governance object in which birth, mating, and death continue on their own schedules independently of any inter-Self operation. These two commitments coexist for the full duration of any active FAI event. D2.53 formalizes what that coexistence means for governance.

The note derives from D1.03, which establishes that the inter-Self governance perimeter is additive: participating in a FAI event does not pause, suspend, or supersede home governance. D1.03's additive perimeter means that home governance and inter-Self governance run concurrently, each within its own scope, without automatic mutual influence. D2.53 makes this abstract commitment operationally concrete at the lifecycle level.

---

## 2. Birth during a FAI event

The first lifecycle case is birth: a new cell or aspect comes into existence within a participating Self's home substrate while a FAI event is active.

The governance implication is direct. The FAI event's sharing scope — the set of aspects contributed from that Self to the shared substrate — was established at construction time (D2.01) by the configuration that governed FAI construction. That configuration enumerated the aspects then in existence. A newly born entity is outside that enumeration. It is not part of the FAI event's shared substrate unless governance explicitly amends the configuration to include it (D2.38 configuration amendment). The birth does not automatically expand the sharing scope.

This is not a technical oversight in the architecture; it is a governance property. If births automatically expanded the sharing scope, the scope of joint governance between participating Selves could change without any explicit governance act by any party. A home governance event in one Self's perimeter would modify the joint governance substrate without the other participating Selves' governance having authorized the modification. The lifecycle isolation principle prevents this by treating the birth record as home governance content — recorded in the home substrate per B1.05, governed within the home perimeter — and treating the FAI configuration as a separate governance object that requires explicit amendment to reflect any new entity.

The birth record and the FAI event record are concurrent but independent governance events. An auditor reviewing both records would find them in separate governance scopes with no automatic linkage. If the Self's governance later decides that the new entity should participate in the active FAI event, that decision produces an explicit configuration amendment record (D2.38) that creates the linkage with a human-authorized timestamp and rationale. The linkage is a governance act, not an automatic system behavior.

---

## 3. Mating during a FAI event

The second lifecycle case is mating: an intra-Self mating operation (B1.06) occurs within a participating Self's home substrate while a FAI event is active. Paper 2's mating primitive combines two or more aspects to produce offspring aspects in the home substrate, potentially modifying the DNA-layer content of the resulting aspects.

Two governance implications follow, corresponding to two sub-cases.

The first sub-case is that the mating produces new offspring aspects not previously part of the FAI event's sharing scope. The new aspects are home governance entities, and the same governance analysis as birth applies: they are not automatically included in the FAI event's sharing scope. If the Self's governance intends to contribute the offspring aspects to the active FAI event, a configuration amendment (D2.38) is required. The mating record in the home substrate and the FAI event record remain in separate governance scopes unless that amendment is executed.

The second sub-case is more architecturally significant. If the mating modifies the DNA-layer content of an aspect that is currently being contributed to the FAI event — an aspect whose content is already present in the shared substrate — the lifecycle isolation principle applies with version-fixing force. The shared substrate holds the version of that aspect's DNA-layer content as it existed at contribution time. The post-mating version exists in the home substrate. These are two distinct versions in two distinct governance scopes. The shared substrate does not automatically update to reflect the post-mating DNA.

This version-fixing property is what prevents a category of race condition between home lifecycle events and FAI operations. If the shared substrate automatically reflected every home DNA modification in real time, the content of the shared substrate would be a moving target — jointly visible to all participating Selves, but unilaterally modifiable by any one Self's home mating operation without joint governance authorization. The lifecycle isolation principle closes this vulnerability by holding the shared substrate to its contribution-time snapshot. The home substrate and the shared substrate diverge in their representations of the aspect's DNA after the mating, and the two trajectories reconnect only at dissolution, when the evolution feed (D1.17–D1.21) carries FAI-derived content back to home substrates through governance-configured ingestion.

---

## 4. Death during a FAI event

The third lifecycle case has three sub-cases, distinguished by whether the dying entity is participating in the FAI event and at what structural level the death occurs.

**Case 1 — death of a non-contributed entity.** An aspect or cell that is not part of the FAI event's sharing scope dies during the event. The governance analysis is straightforward: the death is a home governance event entirely within the home perimeter. The FAI event record has no reference to the dying entity, and the death record has no reference to the FAI event. The two records are parallel, independent governance entries.

**Case 2 — death of a constituent cell within a contributed aspect.** A cell within an aspect currently contributing content to the FAI event dies during the event. The cell's pre-death content was already present in the shared substrate as part of the contributed aspect. That content is not automatically removed from, modified in, or flagged within the shared substrate by the home death event. The home death record (B1.07) is recorded in the home substrate; the FAI contribution record in the shared substrate reflects the pre-death state of the contributed aspect; the two records coexist in separate governance scopes without automatic linkage.

This is the correct behavior for the same governance reason that applies across all lifecycle cases: the shared substrate is a governed snapshot, not a live mirror of home substrate state. Automatic removal of contributed content from the shared substrate upon a home death event would make joint governance content subject to unilateral home governance actions, without explicit authorization from the full set of participating Selves.

**Case 3 — governance-relevant death of a key contributing entity.** In some circumstances, the death of a structurally important aspect that is being contributed to the FAI event may be significant enough that the contributing Self's governance judges the contribution's validity to be affected. For example, if the contribution's purpose depends on the continued existence of the entity whose content is being contributed, governance may determine that the FAI event should be amended or the contribution withdrawn.

This case does not change the lifecycle isolation principle — the death is still a home governance event and does not automatically modify the shared substrate. What changes is that the governing humans of the contributing Self, upon observing the home death event and evaluating its implications, may execute a configuration amendment (D2.38) or a withdrawal from the FAI event (D2.27). These are explicit governance acts, each producing its own governance record, each requiring human authorization. The path from home death to FAI modification runs through governance judgment and explicit action, not through automatic propagation.

---

## 5. The lifecycle isolation principle

The three lifecycle cases share a common governance logic, which this note formalizes as the lifecycle isolation principle:

**Home lifecycle events are isolated from FAI operations. Each is governed within its own scope. Cross-scope implications — a home lifecycle event affecting FAI validity or FAI content — require explicit governance action (configuration amendment or withdrawal), not automatic propagation.**

The principle has three operational components. First, the shared substrate holds contribution-time versions of contributed content; subsequent home evolution of that content — through mating, cell death, or any other lifecycle mechanism — does not automatically update the shared substrate's representation. Second, home lifecycle events that produce new entities (births, mating offspring) do not automatically expand the sharing scope of an active FAI event; new entities are outside the joint governance perimeter unless explicitly included by amendment. Third, home lifecycle records and FAI event records occupy separate governance scopes; an auditor reviewing both records should find no automatic linkage between them unless an explicit governance act — with its own record, authorization, and timestamp — created the linkage.

The lifecycle isolation principle is what makes concurrent home and inter-Self governance coherent. If home lifecycle events automatically propagated into the shared substrate, the shared substrate's content would be unilaterally mutable by any participating Self's home governance operations, and the joint governance perimeter would be porous. The isolation principle is the architectural property that keeps the joint governance perimeter clean: modifications to the shared substrate require joint governance authorization, while modifications to the home substrate remain within the home governance scope.

---

## 6. Inheritance from D1.03

The lifecycle isolation principle is the operational expression of D1.03's additive perimeter commitment. D1.03 establishes that the inter-Self governance perimeter is additive: participating in a FAI event does not supersede, replace, or pause home governance. Home governance and inter-Self governance coexist as independent governance objects, each operating within its own scope.

D2.53 makes D1.03's additive commitment specific at the lifecycle level. The "coexistence" D1.03 names is not merely a scheduling property (both governance systems are running simultaneously); it is a governance boundary property (events in one scope do not automatically produce effects in the other scope). The lifecycle cases in §§2–4 are the operational instances of that boundary property. Birth in the home perimeter does not automatically appear in the inter-Self perimeter. Mating-driven DNA modification in the home perimeter does not automatically update the inter-Self snapshot. Death in the home perimeter does not automatically remove content from the inter-Self scope.

The inheritance runs in one direction: D2.53 follows from D1.03's additive commitment. The reverse is not true — D1.03 does not follow from lifecycle isolation specifically; it is a broader commitment about all home governance operations, of which lifecycle operations are one category. D2.53 is the lifecycle-specific derivation within the broader additive perimeter family.

---

## 7. Anti-pattern: automatic lifecycle propagation

The failure mode this note closes is automatic lifecycle propagation: a FAI implementation in which home lifecycle events automatically update shared-substrate content.

The pattern takes several forms, all of which violate lifecycle isolation. A cell death that automatically removes the cell's contributed content from the shared substrate is one form. A birth that automatically adds the new entity to the active FAI event's sharing scope is another. A mating event that automatically updates the DNA-layer content in the shared substrate to reflect the post-mating version is a third. In each case, a home governance event in one Self's perimeter produces an effect in the joint governance scope without explicit authorization from any party — including the contributing Self's own governance, which may not have evaluated the lifecycle event for FAI implications.

The governance harm is structural. Automatic lifecycle propagation makes the shared substrate's content a function of each participating Self's ongoing home lifecycle operations rather than a function of explicit governance decisions about what content to contribute and when. This removes the joint governance perimeter's integrity: the other participating Selves, and any auditor reviewing the shared substrate, cannot determine whether the content in the shared substrate reflects a governed contribution decision or an automatic mirror of some home lifecycle event. The version-fixing property — that the shared substrate holds contribution-time snapshots — is what separates governed contribution from automatic mirroring, and automatic lifecycle propagation destroys it.

The practical governance repair for any system exhibiting this anti-pattern is to restore explicit governance gates at the lifecycle-to-FAI boundary: births, matings, and deaths in the home substrate are recorded in the home substrate; cross-scope implications of those events are evaluated by the governing humans of the contributing Self; and if a cross-scope action is warranted, it is executed as an explicit configuration amendment or withdrawal with its own governance record.

---

## 8. Operational test

For a FAI event during which a home lifecycle event occurred — whether a birth, a mating, or a death within a participating Self's home substrate — the following questions constitute the operational test for the lifecycle isolation principle:

Can an auditor reviewing both the home governance record and the FAI event record verify that the lifecycle event record is in the home governance scope and the FAI event record is in the inter-Self governance scope, with no automatic linkage between them? If a cross-scope implication was identified and acted upon, is there a discrete configuration amendment or withdrawal record — with its own governance authorization and timestamp — that constitutes the explicit governance act connecting the two scopes? Can an auditor confirm that the version of contributed content in the shared substrate reflects the contribution-time snapshot rather than a post-lifecycle-event update? And can an auditor verify that no home lifecycle event (birth, mating-produced entity, cell death) automatically modified the sharing scope, the contributed content, or any other dimension of the active FAI event without an explicit governance act?

A FAI implementation that passes all four verification questions instantiates the lifecycle isolation principle. One that fails any of them — including by exhibiting automatic linkage, automatic scope expansion, or automatic content update triggered by a home lifecycle event — exhibits the automatic lifecycle propagation anti-pattern, which violates the lifecycle isolation principle and the D1.03 additive perimeter commitment from which it derives.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI and Intra-Self Lifecycle Interaction.* May 15, 2026. ORCID: 0009-0004-8065-3235. CKS Derivation Note D2.53 (#548).
