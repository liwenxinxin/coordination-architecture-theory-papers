# P3↔P1 Path Retraceability Inheritance

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize a specific inheritance edge: Paper 3's cross-organizational authorization chain is a direct extension of Paper 1's six-field path retraceability commitment to the inter-Self scope, where additional governance authority links are required by organizational boundary crossings, not by novel architecture.

## Abstract

Paper 1 (A1.07) establishes path retraceability as a structural commitment of every CKS substrate: each piece of substrate content carries six provenance metadata fields sufficient to reconstruct, from substrate content alone, the complete chain of governance decisions that authorized it. At intra-Self scope — within a single governance authority — this yields a single-authority provenance chain. Paper 3 extends the inter-Self coordination architecture across organizational boundaries, and with that extension the provenance chain must cross governance perimeters. This note formalizes the inheritance relationship: Paper 3's four-link cross-organizational authorization chain is what Paper 1's single-authority chain becomes when content crosses organizational boundaries. The additional links are not architectural novelty; they are a structural consequence of the boundary crossings themselves. Every additional link marks a moment at which governance authority changes hands, and the accountability principle — every substrate content traceable to authorizing governance decisions — is preserved at each transition. The six provenance metadata fields established by Paper 1 apply without modification to shared-substrate content; what Paper 3 adds is the cross-perimeter reference capability that allows those fields to be navigated across the contributing Self's governance perimeter boundary. The four-link chain is the prior-art basis for the inter-organizational path retraceability property.

## 1. The source commitment: Paper 1's six-field path retraceability (A1.07)

Paper 1's traceability commitment (§3.1, A1.07) establishes that every piece of substrate content must carry provenance sufficient to reconstruct its governance lineage from the content itself, without consulting external logs, agent memory, or human recollection. The commitment imports two named vocabularies: path retraceability (Rajabi & Kafaie, 2022), which is a structural property of the substrate, and the accountability plan / accountability trace pair (Naja et al., 2021), which is the contract layer specifying what the trace must capture. Together, the two vocabularies require the substrate to carry the following six provenance fields for each piece of content:

1. **Writer attribution** — who or what authored this content (a human acting under preserved authority, or an AI acting under a named orchestration rule in a named cell execution).
2. **Timestamp** — when the content was written, making the provenance path orderable over time.
3. **Antecedent reference** — what prior substrate content the writer drew on, so each step in the path is itself a substrate read.
4. **Rule reference** — the orchestration rule under which the content was written, where cell-mediated.
5. **Rationale** — the reason the writer wrote what they wrote, where the accountability plan requires it.
6. **Contradiction relationship** — the explicit relationship to contradicting substrate content, where applicable.

At intra-Self scope, these six fields create a complete, navigable provenance chain from any substrate content back through the governance decisions that authorized it. The chain terminates at human-authored governance authority: the orchestration rules are human-authored, and the human's exercise of override authority is itself a substrate-recordable fact. This is what the accountability plan specifies; the accountability trace (the substrate content as accumulated) either carries the chain or fails the plan.

The provenance chain at intra-Self scope passes through a single governance authority. A reader tracing any substrate content backwards reaches, at each step, the same governance perimeter's decisions. The principle — every substrate content traceable to authorizing governance decisions — is satisfied by one-authority traversal.

## 2. The extension requirement: what changes when content crosses an organizational boundary

Paper 3 introduces the shared substrate as the architectural object of inter-Self coordination (§4). The shared substrate inherits all six Paper 1 commitments, including path retraceability. But applying path retraceability at inter-Self scope introduces a structural requirement that does not arise at intra-Self scope: content may originate inside one governance perimeter and be authorized for contribution by that governance authority, then enter a shared substrate governed jointly by multiple governance authorities, then be authorized for absorption back into a home governance perimeter by yet another governance authority.

At each of these transitions, governance authority changes hands. The provenance chain must record each transition, because the chain's purpose is to trace every governance outcome to the authorizing governance decisions — and at inter-Self scope, the authorizing decisions are distributed across governance boundaries.

This is the structural reason the provenance chain is longer at inter-Self scope. The additional links are not introduced by architectural novelty; they are introduced by the boundary crossings themselves. If content never crossed an organizational boundary, the single-authority chain would suffice. When content does cross organizational boundaries — which is the defining operation at inter-Self scope — the chain must extend to cover each authority transition. The extension is logically required, not architecturally invented.

## 3. The four-link cross-organizational authorization chain

Paper 3's inter-Self path retraceability requirement traces through four governance authority links rather than one. The four links are:

**Link 1: Home governance authorization of contribution.** Before a Self contributes aspects to the shared substrate through a Full Aspect Integration (FAI) event, the contributing Self's own governance authority must authorize the contribution. This link records: under what home governance authorization did this content leave the contributing Self's perimeter? Without this link, the provenance chain has a gap at the point where content first crossed the organizational boundary.

**Link 2: Joint FAI event authorization.** The FAI event itself — the operation that places contributed content into the shared substrate — is governed jointly by the governance structures of the participating Selves (§5 of Paper 3). This link records: under what jointly-authorized governance event did this content enter the shared substrate? The joint authorization is the governance act that constitutes the inter-Self exchange, and it is itself substrate-recordable per the six provenance fields.

**Link 3: Shared-substrate governance of content.** Once content resides in the shared substrate, it is subject to the shared substrate's governance — jointly held by the participating Selves. This link records: what governance decisions within the shared substrate's scope authorized the content as it stands within the shared substrate? This is the intra-substrate link, directly analogous to the single authority link at Paper 1's scope, but operating under joint governance authority.

**Link 4: Home governance absorption authorization.** When evolution outputs from the FAI event are ingested into a participating Self's home substrate, the receiving Self's governance authority must authorize the absorption. This link records: under what home governance authorization did this content enter the receiving Self's home substrate? Without this link, the provenance chain has a gap at the re-entry point.

The four links together form a complete provenance chain across the inter-Self governance boundary. A reader tracing any shared-substrate content can reach, at each step, the governance decisions that authorized the content's status at that step. The chain does not skip any authority transition; every point at which governance authority changes hands is recorded.

## 4. What is preserved and what is extended

**What is preserved.** The six provenance metadata fields are unchanged. Paper 3 does not introduce new field types; the same six fields — writer attribution, timestamp, antecedent reference, rule reference, rationale, and contradiction relationship — apply to shared-substrate content exactly as they apply to intra-Self substrate content. The accountability principle is unchanged: every substrate content must be traceable to the authorizing governance decisions. The structural requirement that the path exist as addressable substrate content, not as an external log, is unchanged. The requirement that the path be reconstructable from substrate content alone, without consulting human recollection or external records, is unchanged.

**What is extended.** The cross-perimeter reference capability of the six fields is extended. At intra-Self scope, the antecedent reference field (field 3) points to prior substrate content within the same governance perimeter. At inter-Self scope, shared-substrate content contributed by a participating Self carries cross-perimeter references — the antecedent content from which it derives may reside within the contributing Self's home substrate, across the governance perimeter boundary. Paper 3's configuration substrate (Claim 5, §8) specifies the governance-configurable depth of this cross-perimeter provenance carryover: how far into the contributing Self's home provenance chain the shared substrate carries. This governance-configurable depth is an extension of the antecedent reference field's reach, not a new field type. The field is the same; the reference it can carry now spans organizational boundaries.

The number of governance authority links the chain must traverse is also extended. At intra-Self scope, the chain traverses one authority's decisions. At inter-Self scope, the chain traverses four. The extension is monotone: a four-link chain satisfies a single-link requirement wherever single-link traversal is sufficient. The inter-Self chain is strictly more complete, not architecturally different.

## 5. The prior-art inheritance claim

Paper 3's cross-organizational path retraceability — including the four-link authorization chain and the cross-perimeter provenance reference capability — is a direct extension of Paper 1's A1.07 commitment to the inter-organizational governance context. The inheritance is structural, not analogical. The four-link chain is what the single-authority chain must become when applied to a context where content crosses two organizational boundaries (the contributing boundary and the absorbing boundary), with a joint governance event in between. The chain length is determined by counting the governance authority transitions; the chain's purpose and structure are unchanged.

The prior-art claim covers the following: any implementation that (a) carries the six provenance metadata fields on shared-substrate content, (b) records home governance authorization of contribution as a substrate-verifiable fact, (c) records the joint FAI event authorization as a substrate-verifiable fact, (d) records shared-substrate governance decisions as substrate content subject to the same six fields, and (e) records home governance absorption authorization as a substrate-verifiable fact — is implementing Paper 1's path retraceability at inter-Self scope, not a novel provenance architecture. The four links are the Paper 1 accountability plan applied to the inter-Self governance context.

The key operational consequence is this: the four-link chain is what makes it possible to prove, from substrate content alone, that every governance outcome involving inter-Self coordination traces to human governance decisions at every authority transition. At intra-Self scope, Paper 1's single-authority chain provides this proof. At inter-Self scope, the four-link chain extends the same proof to the multi-authority case. Without the four-link chain, a gap exists at each authority transition; with it, the proof is complete across the full inter-organizational scope.

## Operational test

A shared-substrate implementation satisfies the P3↔P1 path retraceability inheritance if and only if, for any piece of shared-substrate content, a reader can reconstruct — from substrate content alone, without external records — answers to all of the following questions: (1) Under what home governance authorization did the contributing Self place this content in the shared substrate? (2) Under what joint governance authorization did the FAI event occur that introduced this content? (3) What governance decisions within the shared substrate's scope cover this content as it stands? (4) Under what home governance authorization was any evolution output derived from this content absorbed into a receiving Self's home substrate? If any of these questions cannot be answered from substrate content alone, the four-link chain is incomplete and the path retraceability commitment is not satisfied at inter-Self scope.

## Sources

- Li, Wenxin. *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. [§3.1 (A1.07 path retraceability and accountability vocabulary); §5.2 (OIDA differentiation)]
- Li, Wenxin. *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. [§4 (Claim 1, shared substrate); §5 (Claim 2, FAI); §8 (Claim 5, configuration substrate and cross-perimeter provenance depth)]
- Li, Wenxin. *The Instinct/Reasoning Separation Outside the Model.* April 2026.
- Rajabi, E. & Kafaie, S. (2022). Data Provenance and Trustworthiness. *Sensors*, 22(10), 3950. [path retraceability vocabulary, as cited in Paper 1 §3.1]
- Naja, I. et al. (2021). A Semantic Framework for Ethical AI Systems. [accountability plan / accountability trace vocabulary, as cited in Paper 1 §3.1]
- Li, Wenxin. *Path Retraceability and the Accountability Vocabulary: What CKS Substrates Must Carry to Remain Auditable.* April 2026. [derivation note formalizing the two-vocabulary relationship at intra-Self scope]
