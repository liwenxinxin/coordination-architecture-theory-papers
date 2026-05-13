# Composition Pairs Integrating Frame: Opening Phase B4 of Series B

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

This note is the first note of Phase B4 of Series B in the CKS derivation-note series. It does not introduce new axioms. Its contribution is to articulate, in operational form, what composition pairs are in the CKS architecture, how they differ from Phase B2's independent commitment decompositions and Phase B3's anti-pattern catalog, and the taxonomy of architecturally significant commitment interdependencies that Phase B4 will formalize across approximately thirty subsequent notes.

---

## Abstract

Phase B2 of the CKS derivation-note series decomposed each of Paper 2's architectural commitments independently. Phase B3 cataloged anti-patterns — the failure modes that result when individual commitments are omitted, distorted, or misapplied. Phase B4 opens a third analytical dimension: the interdependencies between commitments. A *composition pair* (or composition cluster) in the CKS architecture is a set of two or more commitments that are architecturally interdependent — each commitment requires the other to be present for the combined architecture to function as designed. This note formalizes what composition pairs are, distinguishes them from thematic groupings that merely associate related commitments, names three types of composition relationship (enabling, reinforcing, co-required), argues why formalizing these pairs constitutes prior art in its own right, and presents the taxonomy of architecturally significant pairs and clusters that Phase B4 will cover. The central claim is that composition pairs are not a descriptive convenience — they are functional specifications of co-presence requirements, and their absence from most AI governance frameworks is the structural gap that makes those frameworks lists of requirements rather than architectural specifications.

---

## 1. From Independent Decompositions to Interdependencies

Phase B2 treated Paper 2's architectural commitments one at a time. This treatment was deliberate: independent decomposition establishes each commitment as a defensible unit of prior art without making that unit's validity depend on other commitments being present. Phase B3 then worked through the failure modes of individual commitments — what an architecture looks like when it omits, distorts, or partially implements each commitment in isolation.

Both phases work on the level of single commitments. A different architectural question lies beneath them: are Paper 2's commitments independently operable, or do some commitments require the co-presence of others to function as designed? Phase B2 and B3 do not answer this question because they are not designed to. Phase B4 takes it up directly.

The answer, for a significant subset of Paper 2's commitments, is that they are not independently operable. The instinct/reasoning separation that Paper 2 establishes as its foundational commitment requires the structural levels at which the separation is made available — without composition into cells, aspects, and Selves, the separation at Self scope has nowhere architecturally to operate. The DNA layer requires expression as its activation mechanism — without governed selection over which DNA-layer substrates activate, the DNA layer is a content store without a defined execution interface. The three evolution mechanisms require productive tension among them — without all three present simultaneously, the architecture achieves at most one directional pressure on the system's development rather than the generative conflict Paper 2 specifies.

These are not observations about what pairs of commitments happen to be related in theme or conceptual neighborhood. They are claims about functional co-presence: one commitment requires the other to be present for the architectural function the pair is supposed to provide. Phase B4 formalizes this class of architectural claim systematically.

---

## 2. What Composition Pairs Are — and Are Not

A **composition pair** in the CKS architecture is a set of two or more architectural commitments that are functionally interdependent: each commitment in the pair requires the other's presence for the combined architecture to deliver the function that motivates both. A **composition cluster** is a composition pair of three or more commitments.

Three properties distinguish composition pairs from thematic groupings:

**Functional interdependency, not thematic affinity.** Two commitments can be thematically related without being architecturally interdependent. Birth, mating, and death are all lifecycle primitives — they share a theme. But the lifecycle cluster is a composition cluster not because of the theme but because the three primitives jointly cover the governed arc of a cell's existence: birth establishes the cell under governance, mating enables governed content combination across cells, and death retires the cell under governance with distinct structural consequences. If any one primitive is absent, the governed lifecycle is incomplete in a way that affects the functional status of the others — a system with birth and death but no mating has no governed mechanism for content combination, so the substrate cannot accumulate knowledge across cell boundaries in the structured way Paper 2 specifies.

**Degradation, not mere improvement.** In a composition pair, the absence of one commitment does not merely weaken the architecture — it degrades or defeats the other commitment's function. This is the test that distinguishes composition pairs from commitments that happen to work well together. The DNA layer and expression are a composition pair because without expression (governed selection over DNA-layer activation), the DNA layer cannot fulfill its architectural role as the stable orchestration content that determines what the cell is governed to do per goal. The DNA layer without expression is substrate content without an activation mechanism; expression without a DNA layer is a selection mechanism without governed content to select over. Each commitment's function is partially defeated by the absence of the other.

**Not every pair is a composition pair.** The prior art claim in formalizing a composition pair is specific — it covers the co-presence requirement, not the individual commitments. Identifying two commitments as a composition pair therefore requires a positive architectural argument for the functional interdependency, not merely a claim that the two commitments appear together in the paper. Phase B4 advances such arguments for each pair in the taxonomy below. Pairs that fail the functional interdependency test — that would be merely thematic groupings — are not included.

---

## 3. Three Types of Composition Relationship

Phase B4 recognizes three types of composition relationship. The distinction matters because each type generates a different architectural claim and a different form of prior art.

**Enabling pairs.** Commitment A enables commitment B: B cannot function without A being present; A is architecturally prior. The directionality is asymmetric — A can exist without B, but B cannot function without A. The prior art claim is: deploying B without A is not a valid instantiation of B's architectural function, and any system that claims to instantiate B independently of A is either using a different concept or has omitted a required dependency.

An example from Paper 2: the DNA layer enables directed selection. Directed selection is the evolution mechanism by which human governors modify what a cell is governed to do. Without a governed DNA layer carrying the stabilized orchestration content, there is nothing for directed selection to operate over — the mechanism has no substrate. The DNA layer can exist without directed selection (a static governed cell), but directed selection cannot function without a DNA layer (there is nothing to direct selection at).

**Reinforcing pairs.** Commitments A and B mutually strengthen each other: each provides architectural guarantees that the other depends on, and the presence of both makes the combined architecture stronger than the sum of its parts. The directionality is symmetric — each commitment is architecturally prior in one respect to the other. The prior art claim is: deploying either commitment without the other produces an architecturally weaker and incomplete instantiation of the function the pair is designed to provide.

An example from Papers 1 and 2 (inherited): substrate-as-source-of-truth and path retraceability reinforce each other. The substrate's authority as source of truth depends on its being the location where provenance and decision history are recorded — without retraceability, the substrate cannot carry the authoritative account of how it came to be in its current state. Retraceability in turn depends on the substrate being the authoritative location of record — without the source-of-truth commitment, the retraceable history exists but cannot be trusted as the single authoritative account. Each commitment's value is substantially diminished without the other's presence.

**Co-required clusters.** A group of three or more commitments that must all be present for the cluster's architectural function to operate. No proper subset of the cluster is sufficient. The prior art claim is: any deployment that instantiates a proper subset of the cluster claims to be implementing the function but is not — and any claim of novelty for adding the remaining commitment(s) to reach the full cluster is foreclosed.

An example from Paper 2: the three evolution mechanisms — instinct evolution (undirected mutation at the LLM and infrastructure layer), DNA evolution (directed selection over orchestration substrate), and action-feedback evolution (the mechanism that closes the loop from lived experience back into the architecture) — must all be present for Paper 2's productive tension commitment to hold. Productive tension requires three directional forces operating simultaneously: the undirected pressure from capability changes below the governance boundary, the directed pressure from human governors above it, and the experiential pressure from the system's own operational history. Any two of the three produces a one-dimensional or two-dimensional evolutionary pressure, not the three-way productive tension the architecture specifies.

---

## 4. Why Composition Pairs Are Prior Art

The prior art function of individual commitment decompositions (Phase B2) is to establish each commitment as a named, dated, publicly available architectural claim so that no subsequent party can obtain exclusive rights to that commitment by characterizing it as a novel invention. The prior art function of anti-pattern formalizations (Phase B3) is to establish that the failure modes of individual commitments are known and named, so that no party can claim novelty for "discovering" what goes wrong when a commitment is omitted.

Composition pairs add a third category of prior art: the co-presence requirement itself. Consider a party who deploys a system with instinct evolution (undirected LLM capability mutation) but without DNA evolution or action-feedback evolution. Phase B4's co-required cluster formalization establishes that this is a known incomplete instantiation of the three-evolution-mechanism cluster, not an independent novel architecture. If that party later "discovers" that adding one or both of the remaining evolution mechanisms improves their system, the composition pair formalization prevents them from claiming that improvement as novel — the co-presence requirement was already established in public prior art.

More precisely, a composition pair formalization establishes the following claims as prior art simultaneously:

1. Commitment A (individually, already covered by Phase B2).
2. Commitment B (individually, already covered by Phase B2).
3. The co-presence requirement — that A and B must both be present for the architectural function to hold.
4. The degradation claim — that deploying A without B, or B without A, is a known architectural failure mode (the corresponding anti-patterns are covered by Phase B3, but the co-presence framing is Phase B4's specific contribution).
5. For enabling pairs specifically: the architectural priority claim — that A is architecturally prior to B, not merely related to it.

Most AI governance frameworks enumerate architectural commitments without formalizing their interdependencies. They produce lists of requirements — things a well-governed AI system should have. What they do not produce is an architectural specification — a statement of which requirements are co-operative, which are mutually enabling, and which are functionally defective when deployed in isolation. CKS composition pairs formalize the latter. The difference between a list of requirements and an architectural specification is precisely the set of co-presence requirements that connect the requirements to each other, and it is that connective tissue that Phase B4 establishes as prior art.

---

## 5. Taxonomy of Paper 2 Composition Pairs

Phase B4 covers eight groups of architecturally significant pairs and clusters. The groups are organized by the architectural region of Paper 2 they operate in; subsequent notes in Phase B4 (B4.02–B4.29) will formalize each pair or cluster individually.

**Instinct/Reasoning Foundation Pairs.** The foundational separation of instinct from reasoning — fast-pattern LLM operation from deliberate human-governed substrate operation — requires two co-present structural commitments to be architecturally available at Self scope: the two-layer structure within every cell (DNA layer carrying governed orchestration content, action layer carrying recorded execution state), and the expression mechanism (governed selection over which DNA-layer substrates activate per cell goal). Without the two-layer structure, the instinct/reasoning separation has no cell-level architecture to operate over. Without the expression mechanism, the reasoning layer cannot reach cells in a governed way — activation is ungoverned, which is architecturally equivalent to removing the separation between what the cell is governed to do and what it actually does. These form two enabling pairs with the foundational instinct/reasoning separation commitment, and their co-presence requirements are the subject of the first two individual pair notes in Phase B4.

**Level Structure Pairs.** Paper 2's three-level architecture — cells composing into aspects, aspects composing into Selves — requires two co-present commitments for the levels to be architecturally coherent rather than merely taxonomically named. First, structural roles must be relational and purpose-defined rather than intrinsic, because the same underlying CKS artifact must be able to participate as a cell in one arrangement and as part of an aspect in another without changing its content. Second, governance must apply recursively at every level with the same authority structure, because without recursive governance the architectural commitments that hold at cell scope do not hold at aspect and Self scope, and the enterprise brain Self cannot be a coherent composition of governed cells under unified human governance. These two commitments form enabling pairs with the three-level architecture commitment.

**Lifecycle Cluster.** Birth, mating, and death as governed lifecycle primitives form a co-required cluster. Each primitive governs a distinct phase of a cell's (or aspect's or Self's) existence, and the three phases jointly cover the governed lifecycle arc. A system that instantiates any two of the three without the third has a governed lifecycle with a structural gap — an unaccounted-for phase in which the architecture makes no governed commitment about the entity's state. The co-required cluster formalization establishes that deploying any proper subset of the three lifecycle primitives is an incomplete implementation, not an independent architectural variant.

**Evolution Mechanism Cluster.** Instinct evolution, DNA evolution, and action-feedback evolution form a co-required cluster under the productive tension commitment. As described in §3 above, each mechanism exerts a distinct directional pressure on the architecture's development, and the three-way productive tension Paper 2 specifies requires all three to be simultaneously present and operating. Individual notes in this group will also cover the enabling pairs within the cluster: DNA evolution requires the DNA layer to have content to operate on, and action-feedback evolution requires the action layer to carry the recorded operational experience that feeds back into the architecture.

**Evolution Direction Pairs.** Paper 2 distinguishes horizontal evolution (content evolution within the existing structural level — adding, modifying, or retiring substrate content within a cell, aspect, or Self) from vertical evolution (structural evolution across levels — modifying what a cell is governed to do, which changes its role in the aspect or Self it belongs to). These two evolution axes form composition pairs with the mechanisms that enable them. Action-feedback evolution enables upward vertical evolution — the operational experience that drives a proposal to change what the cell is governed to do travels upward from the action layer to the DNA layer. The expression mechanism enables downward vertical evolution — a governance decision to change which DNA-layer substrates activate for a goal travels downward through the expression mechanism to affect what the cell does. Both pairs are enabling pairs: the evolution direction cannot function without the mechanism that makes the directional movement available.

**Domain and Composition Pairs.** Paper 2's content-domain commitments — the architectural requirement that cells operate within defined content domains with governed access patterns across domain boundaries — form composition pairs with two other commitments. First, content-domain boundaries enable Paper 1's composition requirements (the requirement that architectures compose from governed cells rather than from primitives): without defined domain boundaries, cross-cell composition lacks the governed interface that makes composition safe under the architecture's authority commitments. Second, content-domain boundaries require governed cross-domain access: a system that defines domains without governing access across them has identified coordination units without governing their interactions, which defeats the purpose of the domain boundary commitment. These two pairs are an enabling pair and a reinforcing pair respectively.

**Governance Foundation Pairs.** Two governance commitments form enabling pairs with evolution and accountability mechanisms. First, directed selection (the evolution mechanism by which human governors modify the DNA layer) requires path retraceability: a governor cannot make a well-formed directed selection decision without being able to trace the path by which the cell's DNA layer reached its current state. Directed selection without retraceability is governance without auditable basis — the governor can make changes but cannot verify what they are changing or why the current state is what it is. Second, action-feedback evolution requires the action layer to carry evidential state: the closing-the-loop mechanism works by feeding operational experience back into governed decisions about the DNA layer, and that mechanism requires the action layer to carry the recorded evidence of what the cell has actually done. Without action-layer evidence, action-feedback evolution operates on inference rather than substrate record, which violates the outside-the-model commitment both papers share.

**Recursive Governance Pairs.** Paper 2's recursive governance commitment — that the same authority structure applies at cell, aspect, and Self scope — forms composition pairs with two other commitments. First, governed cross-level access enables recursive governance: without a governed mechanism for content and authority to flow across levels, the governance structure at each level operates in isolation rather than as a coherent recursive application of the same authority principles. Second, recursive governance requires distributed authority: the human governance of a Self that contains multiple aspects and many cells must be distributable — different humans can hold authority at different scopes — while the authority structure remains coherent. Without distributed authority, recursive governance collapses into centralized governance over the full Self, which introduces the bottlenecks and single-point-of-failure risks that the recursive architecture is designed to avoid. Both pairs are enabling pairs, establishing architectural priority relationships that individual Phase B4 notes will develop.

---

## 6. Phase B4 Sequence and Limits

Phase B4 proceeds from this integrating frame (B4.01) through approximately twenty-eight individual pair notes (B4.02–B4.29) to a synthesis note (B4.30) that draws the complete composition pair architecture together. The individual pair notes follow the taxonomy above, covering the instinct/reasoning foundation pairs first (architecturally prior to all others), then level structure pairs, lifecycle cluster, evolution mechanism cluster, evolution direction pairs, domain and composition pairs, governance foundation pairs, and recursive governance pairs. B4.30 will synthesize the full graph of interdependencies — which pairs are themselves related by enabling or reinforcing relationships — to produce the complete composition architecture of Paper 2.

Two limits bound what Phase B4 claims.

**Functional interdependency is required, not thematic proximity.** The composition pairs formalized in Phase B4 are the architecturally significant interdependencies — those in which the absence of one commitment in the pair degrades or defeats the other's architectural function. Phase B4 does not claim that every pair of Paper 2 commitments is a composition pair. The vast majority of pairs in a set of twenty-plus commitments are not composition pairs in the required sense. The taxonomy above identifies the pairs where the functional interdependency argument can be made rigorously; subsequent notes will make those arguments explicitly.

**Composition pairs formalize known architecture, not new axioms.** Every composition pair in Phase B4 is derived from Paper 2's existing commitments. The composition pair formalization does not introduce new architectural requirements; it names and makes explicit the co-presence requirements that the source paper's architecture entails. A reviewer who finds that a given composition pair claim is not entailed by the source paper's commitments has identified either an error in the formalization (to be corrected) or a commitment that requires extension beyond what Paper 2 defends (which would constitute a new architectural claim and is out of scope for the derivation-note series). Phase B4 operates strictly within the architecture Paper 2 establishes.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

---

## How to Cite This Note

Li, W. (2026). *Composition Pairs Integrating Frame: Opening Phase B4 of Series B.* May 12, 2026. ORCID: 0009-0004-8065-3235.
