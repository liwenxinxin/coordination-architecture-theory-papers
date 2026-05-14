# Horizontal Evolution Inherits Paper 1's Substrate Content Modifiability

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to show that Paper 2's named mechanism of horizontal evolution is a specific variant of substrate content modifiability already committed to in Paper 1, and to identify precisely what is preserved from Paper 1 and what is new in Paper 2.

---

## Abstract

Paper 2 of the CKS theory series introduces *horizontal evolution* as a named mechanism for peer-to-peer improvement propagation within an aspect. When a directed selection event improves one cell's DNA, governance may propagate the improvement to peer cells in the same aspect — cells that share a content-domain and are therefore plausible beneficiaries of the same improvement. This note formalizes the inheritance edge: horizontal evolution is a named variant of Paper 1's substrate content modifiability (the modify right, Claim 3/A0.03) applied iteratively across peer cells with individual governance authorization per peer. The identity-preserving properties — individual attribution, human-selective application, and modify-right as underlying mechanism — are inherited directly from Paper 1. What Paper 2 adds is the named mechanism itself, the aspect as a natural propagation boundary, the improvement-triggered propagation condition, and the peer relevance assessment that precedes each propagation decision. This note also positions horizontal evolution as a variant of directed selection (C1.18), sharing the same Paper 1 foundation and adding only the peer-propagation specifics. The prior-art significance is that peer-propagation of improvements within a coordination scope does not constitute a novel mechanism beyond Paper 1's composition and modification commitments.

---

## 1. The inheritance edge stated

The inheritance relationship is:

> **Horizontal evolution (Paper 2) ⊃ Substrate content evolution (Paper 1)**

The ⊃ symbol here means: every operation that horizontal evolution performs is an instance of a category of operation already present in Paper 1. Paper 2's horizontal evolution does not introduce a mechanism outside Paper 1's scope; it names a specific pattern of applying Paper 1 mechanisms that Paper 1 already enabled.

The Paper 1 side of the edge is the substrate content modification commitment. Paper 1 Claim 3 grants governance the right to modify any substrate content and any orchestration rule at any time. Paper 1's composition requirements (A1.13, requirement E, human-selective composition) require that governance selects which cells and substrates participate in a composition, and governs how improvements to one component affect others. Paper 1's labor allocation framework (A1.12) recognizes that AI-assisted work — including identifying which cells might benefit from an update — is available under governance authorization. Taken together, these commitments already licensed the following operation: take an improvement proven at one cell, identify other cells whose substrate content would benefit from the same improvement, and apply the modify right to each of those cells' substrate content, one by one, under individual governance authorization.

Paper 2 names this pattern. The name is *horizontal evolution*, the scope is the aspect, and the trigger is a successful directed selection event at one peer cell. But the underlying machinery is entirely Paper 1.

---

## 2. What horizontal evolution is

Before formalizing the inheritance, it is necessary to state what horizontal evolution is with enough precision to identify which elements are inherited and which are new.

**The trigger condition.** Horizontal evolution begins with a successful directed selection event at one cell within an aspect. The cell's DNA — its orchestration substrate content — has been improved: a governance-authorized modification has been applied, evaluated, and confirmed as an improvement. This confirmation triggers the question: do any peer cells in the same aspect stand to benefit from the same improvement?

**The propagation scope.** The propagation scope is the aspect. An aspect groups cells that share a content-domain — cells whose DNA covers similar subject matter or similar functional patterns. Because peer cells in the same aspect share a content-domain, an improvement relevant to one cell is plausibly relevant to peers. This plausibility is why the aspect is the natural propagation boundary. Propagation does not extend across aspect boundaries because different aspects cover different content-domains; an improvement optimized for one content-domain does not reliably transfer to another.

**The relevance assessment.** Before governance propagates an improvement to a peer cell, governance must assess whether the improvement is relevant to that peer. This is not a mechanical or automatic step. It requires judgment about whether the peer cell's content-domain is similar enough to the originating cell's content-domain that the same improvement applies. The relevance assessment is new governance work that Paper 1 did not name, though Paper 1's labor allocation framework recognized that AI assistance could support such assessments under governance authorization.

**The propagation event.** Each propagation to a peer cell is a separate directed selection event for that peer cell. Governance authorizes the application, the peer cell's DNA is updated, and the event is recorded in that peer cell's lineage chain with individual attribution: who authorized the propagation, what was propagated, and what original improvement event triggered the propagation. There is no bulk update. If an improvement at cell A is to be propagated to peers B, C, and D, that is three directed selection events — three authorizations, three lineage chain entries, three records — not one operation covering all three.

**The aspect-bounded scope.** Horizontal evolution does not propagate improvements beyond the aspect boundary. This is not a prohibition to be enforced; it is a structural consequence of the mechanism. The trigger is an improvement at a peer in the same aspect, the relevance plausibility rests on shared content-domain, and the shared content-domain is the defining property of aspect membership. An improvement to a cell outside the aspect may be relevant on other grounds, but that relevance is evaluated through a different governance channel — not through horizontal evolution.

---

## 3. Substrate content evolution identity preserved

Four properties of Paper 1's substrate content evolution are fully preserved in horizontal evolution.

**Individual attribution per peer.** The modify right in Paper 1 is not a bulk-update license. It applies cell by cell, requiring governance authorization for each cell's substrate content. Horizontal evolution inherits this property directly: each propagation event is a separate governance act for each peer cell. An observer examining the lineage chains of cells B, C, and D after horizontal evolution from cell A would find three separate records, not one shared record pointing to a batch operation. The reason this property is load-bearing — the reason it makes horizontal evolution an *inheritor* rather than a *novelty* — is that Paper 1's modify right was always applicable to multiple cells in sequence. Nothing about applying the modify right to ten cells one after another required a new mechanism. Horizontal evolution is that sequence, named and bounded by the aspect scope.

**Human-selective application.** Paper 1's human-selective composition requirement (A1.13, requirement E) means governance decides which cells and substrates participate in a composition and how improvements to one component affect others. This maps directly onto horizontal evolution: governance decides which peer cells receive the propagated improvement and which do not. Not all peers in the aspect automatically receive the improvement. Governance may decide that peer cell B benefits from the improvement, peer cell C does not (because the relevance assessment concluded the content-domains are too different), and peer cell D should receive a modified version of the improvement rather than the original. Each of these is a human decision, not an automatic propagation. The human-selective property is preserved in full.

**Individual attribution in lineage chains.** Paper 1's accountability vocabulary requires that governance-authorized modifications are attributed — who authorized the change, what was changed, and traceable to what decision. Horizontal evolution inherits this exactly. Each propagation event in each peer's lineage chain carries individual attribution: the governance actor who authorized the propagation to that specific peer, the content of what was propagated, and a reference to the originating improvement event that triggered the propagation. The lineage chain is the accountability record, and it is per-cell, not per-propagation-wave.

**Modify right as underlying mechanism.** The mechanical operation that horizontal evolution performs is a substrate content modification to the peer cell's DNA. This is precisely the modify right from Paper 1. There is no new operation at the infrastructure level. The governance layer is richer — it now includes the aspect scope, the relevance assessment, and the improvement-triggered propagation condition — but the operation applied to each peer cell's substrate is the same modify right that Paper 1 established.

---

## 4. What is new in Paper 2

Paper 1 did not name horizontal evolution. Four elements are genuinely new in Paper 2.

**The named mechanism.** Paper 1 had the modify right applicable to multiple cells. Paper 2 names peer-propagation of improvements within an aspect as a distinct evolution mechanism with a specific shape: triggered by a successful directed selection event, bounded by the aspect, proceeding peer by peer under governance authorization. The name is not merely taxonomic; it creates a referenceable mechanism that governance can deliberately invoke when applicable conditions arise.

**The aspect as propagation boundary.** Paper 2 establishes that the aspect's shared content-domain is the structural reason improvement propagation is bounded at the aspect level. Paper 1 did not introduce aspects as an architectural level; aspects are introduced in Paper 2's three-level architecture (cell, aspect, Self). The aspect-bounded propagation scope therefore depends on architectural structure that did not exist in Paper 1. This is a structural new element, not merely a naming choice.

**The improvement-triggered propagation condition.** Horizontal evolution is specifically triggered by a successful directed selection event at one cell. The trigger condition — that a proven improvement at one peer prompts governance to consider propagation to peers — is new governance logic in Paper 2. Paper 1 did not specify when the modify right should be considered for application to multiple cells; that was entirely a governance judgment without architectural specification. Paper 2 names one specific condition under which that judgment should arise.

**The peer relevance assessment.** Before each propagation event, governance must assess whether the improvement is relevant to the candidate peer cell. This relevance assessment — does this improvement apply to a peer with a similar but not identical content-domain? — is new governance work identified as part of the horizontal evolution mechanism. Paper 1's labor allocation framework supported AI-assisted identification work under governance authorization, but did not name relevance assessment as a specific step in any named mechanism.

---

## 5. Relationship to C1.18 (directed selection)

Derivation note C1.18 formalizes the inheritance edge between Paper 2's directed selection and Paper 1's substrate content modifiability. Horizontal evolution is a variant of directed selection — not a separate mechanism — and C1.21 shares the same Paper 1 foundation as C1.18.

The shared foundation is the modify right (Paper 1 Claim 3/A0.03): governance-authorized modification of substrate content, with individual attribution, applied to one cell's DNA. Directed selection (C1.18) names the pattern of applying this right to improve a single cell's DNA through a governed selection process. Horizontal evolution (C1.21) names the pattern of applying this right to multiple peer cells' DNA after a successful directed selection event at one peer, with the aspect as propagation boundary.

The relationship between C1.18 and C1.21 is therefore:

> Horizontal evolution = directed selection + peer-propagation trigger + aspect-bounded scope + relevance assessment per peer

All three components added to directed selection are new in Paper 2. None of them change the modify-right foundation. Together, C1.18 and C1.21 cover the full directed-selection inheritance territory from Paper 1 to Paper 2: C1.18 covers the single-cell application and C1.21 covers the multi-peer aspect-bounded extension of the same underlying operation.

This framing matters because it forecloses a reading of horizontal evolution as architecturally discontinuous with directed selection. An architecture that already supports directed selection at the cell level supports horizontal evolution as a coordination policy layered on top of that same mechanism — not as a new mechanism requiring independent architectural justification.

---

## 6. Prior-art significance

The inheritance edge formalized in this note forecloses three categories of adversarial claims.

**Claim category (a): peer-propagation of improvements within a coordination scope is novel relative to Paper 1.** The inheritance edge shows it is not. Paper 1's modify right, applied iteratively to peer cells with individual governance authorization, is peer-propagation. What Paper 2 adds is the name, the trigger condition, and the aspect-bounded scope — none of which introduce a mechanism outside Paper 1's operational territory.

**Claim category (b): aspect-bounded improvement propagation is novel.** The aspect-bounded scope is new in Paper 2 as a structural element, because aspects are introduced in Paper 2. But the claim that *bounding propagation to a coordination scope* is novel is foreclosed by Paper 1's composition requirements, which already required governance to decide which cells participate in a composition and how improvements propagate. The aspect provides a named scope for that decision; it does not introduce the decision itself.

**Claim category (c): the named mechanism "horizontal evolution" covers territory not already in Paper 1's composition and modification commitments.** The name is new. The territory is not. Every operation within horizontal evolution is either the modify right applied to a peer cell (Paper 1 Claim 3) or a governance judgment about relevance and selection (Paper 1's human-selective composition requirement and authority architecture). The name organizes territory already present in Paper 1; it does not expand it.

---

## 7. Operational test

For any claimed horizontal evolution event, an observer can apply the following test to verify that the event instantiates the inherited properties rather than introducing a novel bulk-update mechanism.

1. **Separate lineage chain records.** Does each peer cell that received the propagated improvement have a separate, individually attributed record in its own lineage chain? If horizontal evolution was applied to N peers, there must be N separate records — not one shared record or one batch entry covering all peers. A single record covering multiple peers fails this test and indicates a bulk-update operation outside the Paper 1 modify-right pattern.

2. **Individual governance authorization per peer.** For each peer cell that received the improvement, is there a separate governance authorization — a specific act of approval by a human with appropriate authority — covering that peer's modification? The authorizations may have occurred in close sequence and may have been assisted by AI relevance assessments, but each must be individually traceable to a human governance decision.

3. **Traceability to the originating improvement event.** Does each peer's lineage chain entry identify the originating improvement event — the directed selection event at the source cell — that triggered the propagation? This traceability is what distinguishes horizontal evolution from an independently motivated modification to each peer cell. Without it, the propagation is indistinguishable from N separate modifications made for N independent reasons.

4. **Aspect-bounded scope.** Did no propagation cross the aspect boundary? Peer cells that received the improvement should all be members of the same aspect as the originating cell. Propagation to cells in a different aspect would indicate a different mechanism or a governance judgment that is not horizontal evolution in the Paper 2 sense.

5. **Non-automatic application.** Is there evidence that governance assessed relevance for each peer and made a selective decision? If all peers in the aspect automatically received the improvement without individual relevance assessment, that is an automatic propagation mechanism, not governed horizontal evolution. At minimum, a record should exist showing which peers were assessed, which were selected for propagation, and on what grounds peers (if any) were excluded.

A claimed horizontal evolution event that passes all five checks instantiates the inherited properties and the new Paper 2 elements as formalized in this note.

---

## 8. Conclusion

Horizontal evolution in Paper 2 is a named variant of Paper 1's substrate content modifiability — the modify right applied iteratively across peer cells in the same aspect, with individual governance authorization per peer, triggered by a successful directed selection event at one cell. The four properties that make it an inheritor rather than a novelty are: individual attribution per peer, human-selective application, per-cell lineage chain attribution, and the modify right as the underlying mechanism. What Paper 2 adds are the name, the aspect as propagation boundary, the improvement-triggered propagation condition, and the peer relevance assessment that precedes each propagation decision. Horizontal evolution stands in the same inheritance relationship to Paper 1 as directed selection (C1.18), sharing the same modify-right foundation and extending it with peer-propagation logic bounded by the aspect scope.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Horizontal Evolution Inherits Paper 1's Substrate Content Modifiability.* May 14, 2026. ORCID: 0009-0004-8065-3235.
