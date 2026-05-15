# FAI Governance for Aspect Restructuring

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

A CKS-governed Self may restructure its aspect organization — creating, merging, splitting, or retiring aspects — before, during, or after a Full Aspect Integration (FAI) event. Each timing has distinct governance implications. Pre-FAI restructuring affects which aspects are available for contribution and may require standing-configuration amendment. During-FAI restructuring is isolated under the lifecycle isolation principle (D2.53): the shared substrate holds pre-restructuring aspect versions, and any cross-scope implication of mid-event restructuring requires explicit governance action. Post-FAI restructuring informed by the evolution feed and post-mortem review is the most productive case — it closes the structural co-adaptation cycle that Paper 2's C1.30 commitment names and Paper 3's FAI mechanism operationalizes. When restructuring is causally downstream of FAI learning, the restructuring governance record should carry provenance linking back to the FAI event and the evolution feed content that informed the decision. The anti-pattern is FAI-oblivious restructuring: reorganizing aspects based solely on internal considerations while ignoring inter-Self learning opportunities the evolution feed provides.

---

## 1. Context and derivation lineage

Paper 2 committed to structural co-adaptation as an architectural property of CKS-governed Selves (C1.30): the architecture supports evolution of organizational structure — the arrangement of cells into aspects, and aspects into a Self — as operational needs change. This commitment was framed at intra-Self scope: a Self's aspect structure can and should change over time in response to operational experience, governance review, and directed selection.

Paper 3 introduced Full Aspect Integration (FAI) as the canonical operation over the shared substrate through which two or more CKS-governed Selves coordinate. FAI events produce three categories of output that each participating Self can ingest into its home substrate: DNA-layer content (orchestration substrates, behavior substrates, schemas, rules), action-layer content (recorded task instances, outputs, lived experience), and conflict carry-through annotations (D1.16) that capture unresolved tensions surfaced during the integration event. These outputs reach the participating Self's home governance through the four-locus evolution-feed mechanism at the FAI hand-off boundary (Paper 3 Claim 4).

D2.55 synthesizes these two cross-paper commitments. The question this note addresses is: when a Self exercises its Paper 2 C1.30 right to restructure its aspects, what governance constraints does Paper 3 FAI impose, and — conversely — what governance opportunities does Paper 3 FAI create? The answer depends on the timing of the restructuring relative to the FAI event lifecycle.

---

## 2. Pre-FAI aspect restructuring: configuration alignment requirement

When a Self restructures its aspects before participating in a FAI event — creating new aspects from existing cells, merging two aspects into one, splitting one aspect into several, or retiring an aspect entirely — the restructuring is governed entirely within the Self's home perimeter. The lifecycle records produced by the restructuring (aspect births, matings, and deaths per Paper 2 Claim 3 / B0.03) are home governance records. No inter-Self coordination is required for the restructuring itself.

The governance implication arises at the configuration layer. A FAI event's sharing scope — Dimension 1 of the configuration (D1.22) — specifies which aspects each participating Self contributes. If the FAI configuration was authored before the restructuring occurred, it may reference aspects by name or type that no longer exist in their prior form, or it may fail to reference new aspects the restructuring created.

Two specific configuration situations arise.

**Ad hoc configuration (single-event).** If the FAI event is being configured freshly after the restructuring, the configuration naturally reflects the post-restructuring aspect structure. No amendment is needed because no prior configuration exists. The governance discipline is that the configuration must be authored against the current aspect structure — the person or process authoring the sharing scope should not import a prior configuration without reviewing it for post-restructuring coherence.

**Standing configuration (D2.21).** If a standing FAI configuration exists — a pre-authorized configuration governing a recurring or expected FAI event — and that configuration references aspects by name or type, aspect restructuring may trigger a standing configuration amendment requirement (D2.21 Requirement 4). The amendment must be executed before the next FAI event under that configuration occurs. Operating a FAI event under a standing configuration that does not reflect the current aspect structure is a governance defect: the configuration commits to contributing aspects that may not exist, or omits aspects that now cover domain territory the configuration intended to share.

The governance action required when pre-FAI restructuring precedes a standing configuration is: review the standing configuration's sharing scope dimension against the post-restructuring aspect inventory; execute an amendment if any referenced aspect was created, renamed, merged, split, or retired; obtain whatever human authorization the standing-configuration amendment process requires; and record the amendment with a reference to the restructuring records that motivated it.

---

## 3. During-FAI aspect restructuring: lifecycle isolation applies

Home governance continues independently during an active FAI event (D2.23). A participating Self's governance authority over its home perimeter is not suspended or transferred by participation in FAI. A Self that needs to restructure an aspect while a FAI event is live may do so.

The lifecycle isolation principle (D2.53) governs what happens at the boundary between the live FAI event and the home-side restructuring. The shared substrate contains the versions of aspects as contributed at configuration time — the point at which the contributing Self surfaced the aspect's cells, DNA-layer content, and action-layer content into the shared substrate. A home-side restructuring that occurs after that contribution point does not automatically update the shared substrate. The FAI event continues operating on the pre-restructuring aspect versions.

This isolation is architecturally correct. The shared substrate is a temporarily constructed coordination medium with its own governance perimeter spanning the participating Selves; it is not a live mirror of each Self's current home-perimeter state. Allowing home-side changes to propagate into the shared substrate mid-event would make the shared substrate's content indeterminate — the participating Selves and the orchestration layer could not rely on aspect content remaining stable while integration work is in progress.

Three governance-relevant cases arise when during-FAI restructuring involves an aspect that is also being contributed to the shared substrate.

**Case 1 — The restructured aspect is not among the contributed aspects.** No governance action is required at the inter-Self scope. The shared substrate is unaffected. Home governance records the restructuring normally.

**Case 2 — The restructured aspect overlaps with contributed content, but the restructuring does not materially alter the contribution's representational validity.** For example, an aspect is reorganized internally (cells reassigned) but the aspect-level domain coverage and DNA-layer content in the shared substrate remain accurate. Home governance documents the restructuring and notes in the home record that the shared-substrate contribution predates the reorganization. No withdrawal or amendment is triggered unless human governance judgment determines the change is material.

**Case 3 — The restructuring materially affects a contributed aspect.** For example, two aspects are merged mid-event, one of which is among the contributed aspects; or an aspect being contributed is split, producing new aspects with different domain scopes. In this case, the pre-restructuring version of the aspect remains in the shared substrate under lifecycle isolation, but that version no longer accurately represents the Self's current organizational structure. Home governance must choose among three options: (a) withdraw the affected contribution (D2.27), which removes the aspect's content from the shared substrate and records the withdrawal; (b) execute a configuration amendment (D2.38) to update what the Self is contributing, which may require re-contribution under the new aspect structure; or (c) continue with the pre-restructuring version in the shared substrate, explicitly documenting the governance decision that the contribution remains valid for the purposes of the FAI event despite the home-side restructuring.

Option (c) is not a default — it requires an affirmative governance decision that the pre-restructuring contribution is adequate. Implicit continuation without governance review is the failure mode this case analysis is designed to prevent.

---

## 4. Post-FAI aspect restructuring: closing the structural co-adaptation cycle

Post-FAI aspect restructuring informed by the FAI evolution feed is the most governance-rich case, and the one that directly operationalizes Paper 2 C1.30's structural co-adaptation commitment through Paper 3's inter-Self coordination machinery.

FAI events produce governance intelligence that extends beyond the immediate coordination outputs. Three specific post-FAI outputs are relevant to aspect restructuring decisions.

**Conflict carry-through annotations (D1.16).** Conflicts surfaced during the FAI event that were preserved as first-class substrate state rather than resolved. These annotations record where the participating Selves' contributed content was in tension — overlapping domain coverage, contradictory orchestration rules, inconsistent action-layer records. When a Self reviews these annotations during post-mortem review (D2.39), they may reveal structural issues: aspect boundaries that are too broad (generating unnecessary conflicts with other Selves' corresponding aspects), aspect boundaries that are too narrow (failing to surface relevant cells during contribution), or domain territory that is not covered by any current aspect.

**Action-feedback ingestion (D2.10).** Action-layer content ingested from the evolution feed may reveal that the Self's current aspect structure does not reflect the actual distribution of work. If action-layer records show sustained activity at the boundary between two aspects — tasks that draw on cells from both — the post-mortem review may identify the aspect boundary as artificially imposed rather than domain-natural. Merging the two aspects, or restructuring their boundary, would produce a better contribution in future FAI events.

**Post-mortem review recommendations (D2.39).** The formal post-mortem review conducted after FAI dissolution may directly recommend aspect restructuring as a governance improvement action. These recommendations are governance proposals, not automatic directives — home governance authority determines whether to accept, modify, or decline them. When accepted, they become restructuring decisions subject to the full lifecycle record requirements.

The structural co-adaptation cycle that D2.55 formalizes runs as follows:

> FAI events → evolution feed (conflict annotations, action-layer content, DNA-layer content) → home action-feedback ingestion and post-mortem review → governance improvement proposals (which may include aspect restructuring) → directed selection executed as home lifecycle operations (aspect births, matings, deaths) → improved aspect structure → better future FAI contributions → repeat.

This cycle is the operational expression of Paper 2 C1.30 at inter-Self scope. C1.30 committed that the architecture supports organizational structure evolution. Paper 3 FAI provides the external signal source — other Selves' contributed content, surfaced conflicts, cross-Self action-layer comparison — that makes the evolution directional rather than merely permissible. Without FAI, structural co-adaptation responds only to internal signals. With FAI, it responds to inter-Self learning, and the Self's aspect structure can converge toward better alignment with the coordination domain it operates in.

---

## 5. FAI-informed restructuring records: the provenance requirement

When aspect restructuring is causally downstream of FAI learning — when the decision to restructure was informed by evolution-feed outputs, conflict annotations, or post-mortem recommendations from a specific FAI event — the restructuring governance record should carry provenance linking back to that causal chain.

Concretely: the aspect birth record for a newly created aspect, the aspect death record for a retired aspect, or the mating record for a merged or restructured aspect should reference (a) the FAI event identifier whose outputs informed the decision, (b) the specific evolution-feed content or conflict annotation that triggered the governance review, and (c) the post-mortem recommendation or governance improvement proposal through which the restructuring decision was formally authorized.

This provenance requirement serves three governance functions.

**Traceability.** An observer reviewing the Self's governance history can trace the path from inter-Self coordination event to intra-Self structural change. This is the inter-Self learning provenance chain: contributing Self's content → FAI event → shared substrate → evolution feed → receiving Self's post-mortem review → restructuring decision → new aspect structure. Without the provenance link in the restructuring record, the chain is present in the substrate but not traceable without forensic reconstruction.

**Accountability.** If a restructuring decision is later found to have degraded the Self's coordination quality — the new aspect structure produces worse contributions in subsequent FAI events — the governance record allows the decision-making path to be reviewed. What FAI signal prompted the restructuring? Was the post-mortem recommendation sound? Was the governance authorization appropriate? Provenance-bearing records make this review possible; provenance-free records do not.

**Collective learning signal.** When multiple Selves in a coordination network restructure aspects in response to the same FAI event's signals, the pattern of restructurings is itself a collective governance signal — evidence that the FAI event surfaced genuine structural issues across participants. This population-level signal (Paper 3 Claim 6) is only legible if individual restructuring records carry FAI event provenance. Without it, the pattern cannot be traced.

The provenance requirement does not impose a labor burden disproportionate to its governance value. Aspect restructuring is an infrequent, deliberate governance action; adding a reference to the FAI event and the specific evolution-feed content that informed the decision requires a small number of additional fields in the restructuring record. The governance discipline is that this linking should be performed at the time of restructuring, when the causal chain is fresh, rather than reconstructed after the fact.

---

## 6. Anti-pattern: FAI-oblivious restructuring

The anti-pattern D2.55 names is aspect restructuring that ignores the FAI evolution feed and post-mortem findings — a Self that restructures its aspects based exclusively on internal considerations while the evolution feed from recent FAI events sits unreviewd.

FAI-oblivious restructuring is not a violation of intra-Self governance correctness. The Self may apply its home lifecycle primitives correctly, authorize the restructuring appropriately, and maintain accurate internal records. The defect is at the inter-Self learning scope: the Self is treating FAI as a coordination transaction that produces immediate outputs (merged substrate content, resolved conflicts) while discarding the governance intelligence the evolution feed carries.

The practical consequence is that the Self's aspect structure drifts toward internal coherence while losing alignment with the coordination domain. Aspects optimized for internal efficiency may produce poor FAI contributions — overlapping heavily with other Selves' aspects in some domains, leaving coordination gaps in others, generating conflicts that the Self's current structure was not designed to handle. The FAI events that could have informed corrective restructuring were processed for their immediate outputs only.

The pattern is especially visible when a Self participates in repeated FAI events with the same partner Selves and the same categories of conflicts recur across events. Recurring conflicts that are never addressed by structural review are a signal of FAI-oblivious governance — the Self is contributing the same structural misalignment event after event, generating the same conflict preserve-or-resolve decisions, without using the conflict pattern as a signal to review whether aspect restructuring would address the root cause.

The correction is not a process requirement that every FAI post-mortem must produce a restructuring recommendation. Most FAI events will not reveal structural deficiencies; post-mortem review may find no restructuring opportunities. The anti-pattern is the absence of the review, not the absence of a restructuring result. A Self that conducts genuine post-mortem review and concludes that no aspect restructuring is warranted is not exhibiting the anti-pattern.

---

## 7. Operational test

For a Self that restructured one or more aspects after a FAI event, the following questions test whether the governance requirements this note formalizes were met.

1. **Provenance in restructuring records.** Can an observer locate, in the restructuring governance records (aspect birth, death, or mating records produced by the restructuring), an explicit reference to a specific FAI event and to the evolution-feed content or conflict annotation that informed the restructuring decision? If the records are present but contain no FAI provenance, the inter-Self learning provenance chain is broken.

2. **Post-mortem pathway.** Is there a post-mortem review record (D2.39) for the FAI event that the restructuring records reference, and does that record include a governance improvement proposal recommending or suggesting the restructuring? If the restructuring records cite a FAI event but no post-mortem record exists, the causal chain runs from FAI event directly to restructuring without the governance review intermediate — which collapses the deliberation step the cycle requires.

3. **Conflict annotation linkage.** If the restructuring was prompted by recurring conflicts surfaced in the FAI event, can the observer locate the conflict carry-through annotations (D1.16) from the shared substrate, trace them through the evolution feed to the home substrate, and then forward to the post-mortem review that identified them as restructuring drivers? This is the full traceable chain: shared substrate conflict → home evolution feed → post-mortem review → restructuring record.

4. **Configuration coherence.** Following the restructuring, was the FAI standing configuration (if one exists) reviewed and, where necessary, amended to reflect the new aspect structure? Is there an amendment record that references both the restructuring records and the prior standing configuration?

A Self whose governance records support affirmative answers to all four questions has instantiated the structural co-adaptation cycle D2.55 formalizes. A Self whose records support (1) through (3) but not (4) has performed the intra-Self governance correctly but left the inter-Self configuration in a potentially inconsistent state. A Self whose records fail (1) and (2) has restructured its aspects in a manner that is internally valid but opaque to inter-Self learning review.

---

## Source papers

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance for Aspect Restructuring.* May 15, 2026. ORCID: 0009-0004-8065-3235.
