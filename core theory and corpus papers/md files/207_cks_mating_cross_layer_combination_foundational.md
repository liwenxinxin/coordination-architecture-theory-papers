# Mating as Cross-Layer Combination: A Foundational Commitment Establishing the Lifecycle Operation That Combines Parental Content Across DNA and Action Layers Through Three Orchestration-Governed Patterns

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one of the lifecycle primitives Paper 2 commits to — **mating** — as a standalone foundational architectural commitment defining a cross-layer combination operation over DNA-layer and action-layer parental content, configured per mating event by orchestration substrate through three architecturally specified patterns: Union, Selective merge, and Lineage-preserved union.

## Abstract

Paper 2 commits to three lifecycle primitives — birth, mating, and death — applying uniformly at every level of structural composition (cell, aspect, Self) under unified human governance. A separate note (B1.09) formalizes birth as governed origination from specification. This note formalizes mating as the lifecycle operation that combines parental content across both the DNA layer and the action layer of two or more parental cells, aspects, or Selves, configured per mating event by orchestration substrate authored under human authority, with three architecturally specified patterns available: Union, Selective merge, and Lineage-preserved union. Mating's distinctive architectural work, beyond the three patterns, is collapsing what biology distributes across separate genetic, epigenetic, and cultural inheritance channels into one governable primitive. This note states the commitment, distinguishes it from adjacent operations, enumerates the inherited Paper 1 commitments the patterns rest on, articulates operational implications and limits, and provides an operational test.

## 1. Why mating-as-cross-layer-combination needs to be formalized as standalone

Paper 2 introduces three lifecycle primitives at every level of structural composition: birth, mating, and death. Birth has been formalized as standalone in B1.09 — origination from specification under human governance, governance-not-labor, applicable uniformly at cell, aspect, and Self scopes. Death will be formalized in B1.11. This note formalizes the middle primitive: mating.

Standalone treatment is necessary for four reasons. First, mating is operationally distinct from both birth and death: birth originates from specification with no parents, mating combines content from existing parents, death retires existing entities. Second, mating is the only lifecycle primitive that combines content across both layers within a cell — per B1.06, every cell has a DNA layer (stabilized orchestration substrates and behavior substrates) and an action layer (recorded task instances and outputs). Third, three architectural patterns are available, each serving distinct operational purposes — Union maximizes information preservation including conflict preservation per A1.03; Selective merge enables curated combination with labor allocable per A1.12; Lineage-preserved union maximizes provenance for audit and lineage reconstruction per A1.07. Fourth, mating in CKS collapses what biology treats as separate inheritance channels — genetic, epigenetic, and cultural — into one governable primitive.

The standalone treatment is the tenth Phase B1 note, second in the lifecycle cluster, and load-bearing for the evolution mechanisms that follow. Without mating's flexible inheritance, evolution mechanisms (B1.12–B1.15) would have only de novo birth as origination; succession across generations carrying parental content forward depends on mating as primitive.

## 2. The architectural commitment, precisely stated

In the CKS pattern, a cell, aspect, or Self performs **mating** when it combines parental content across both the DNA layer and the action layer of two or more parental cells, aspects, or Selves into a new offspring, with the specific combination configured per mating event by orchestration substrate authored under human authority. Three architecturally specified patterns are available; pattern selection is per mating event.

**Union.** The offspring's substrate carries everything from both parental DNA layers and both parental action layers. When parental DNA layers conflict — for example, when two parents specify different orchestration rules for the same situation — both rules are preserved in the offspring as first-class substrate state per A1.03 conflict-as-first-class, with the conflict registered as substrate content per A2.45. When parental action layers conflict, both records are preserved with the conflict registered. The offspring's cell-level orchestration rules govern how the cell handles the preserved conflicts at execution; resolution is by human-authored meta-rule, not automatic merge.

**Selective merge.** Humans, or LLMs operating under human direction, pre-curate which content from each parent crosses the boundary into the offspring. The labor of curation is allocable per A1.12 — humans directly, LLMs under human direction identifying candidates with humans approving, or stable cells executing curation under orchestration rules. Authority over the curation rules is human per A1.01; the rules are substrate content authored per A2.04.

**Lineage-preserved union.** The offspring's substrate carries everything from both parental DNA and action layers as in Union, with one architectural addition: every element of the offspring's substrate carries a pointer back to the parental cell from which it derived. Provenance is traceable from any offspring substrate element to its original parental source per A1.07. The lineage pointers are themselves substrate content in the offspring.

Pattern selection is per mating event, configured by orchestration substrate authored per A2.04 — regulated-work mating may default to Lineage-preserved union, high-curation mating to Selective merge, conflict-preserving research mating to Union. The mating event is recorded with provenance per A2.40: what mated, when, under what pattern, with what offspring identifier. The offspring is itself a cell, aspect, or Self with full inheritance of Paper 1 commitments per B1.03/B1.04/B1.05, governed from the moment of mating. Mating is distinct from birth (B1.09): birth originates from specification with no parents; mating combines content from existing parents. Both origination patterns are available; deployments choose between them per origination event.

## 3. What makes mating-as-cross-layer-combination architecturally distinctive

Conventional AI systems lack a coherent architectural inheritance/combination operation between AI components. Three adjacent design objects illustrate the gap.

Machine-learning ensemble fusion (bagging, boosting, stacking, mixture-of-experts) combines the *outputs* of multiple models through voting, averaging, or gating. It does not combine architectural structure; constituent models retain their separate parameters. CKS mating, by contrast, combines architectural content (DNA-layer orchestration logic and action-layer recorded experience) into a single offspring whose architectural structure is itself the combination of its parents'.

Model merging in the LLM weight-space sense (TIES-merging, DARE, SLERP-style interpolation, task-vector arithmetic) combines parameters of multiple fine-tuned models into a single merged model. These operate inside the model on weights; the resulting merged model carries no architectural commitments forward, no provenance of which weight came from which parent, no substrate-level conflict representation. CKS mating operates outside the model on substrate content and carries Paper 1's commitments forward at the offspring level by construction.

Software lifecycle merge logic and agent frameworks (Git two-parent merges, schema migrations, software product-line feature derivation; AutoGen, LangGraph, OpenAI Agent Builder, the Claude Agent SDK) have merge or instantiation operations but no first-class architectural inheritance primitive. Git merge conflicts are transient — required to be resolved before the merge completes — whereas Union's commitment is the inverse: merge conflicts become persistent first-class substrate state. Agent frameworks have configuration-driven instantiation but no two-parent combination primitive at all.

CKS mating is distinctive in three respects. First, **cross-layer architectural combination**: both DNA layer and action layer are combined per mating event, made possible architecturally by the two-layer-within-cell distinction (B1.06). Second, **three-pattern flexibility under orchestration governance**: Union, Selective merge, Lineage-preserved union — each architecturally specified, each selected per event by human-authored orchestration. Conventional combination operations are typically uni-modal; CKS mating commits to multi-pattern flexibility. Third, **unification of biology's separate inheritance channels into one primitive**, developed in §4.

## 4. The biological analog and where CKS exceeds biology

Biology's closest architectural analog is multi-channel inheritance, treated by the Extended Evolutionary Synthesis as causally entangled channels of one inheritance architecture: genetic inheritance via DNA replication (high-fidelity), epigenetic inheritance via methylation patterns and histone modification (intermediate-fidelity), and cultural inheritance via teaching and learned behavior (low-fidelity but high-flexibility). Each channel evolved as a separate transmission mechanism because no single biological mechanism could handle all three — DNA replication does not transmit acquired methylation patterns or learned behaviors; methylation does not transmit teaching; teaching does not transmit genome.

CKS exceeds biology at this exact point. The architecture specifies a unified mating primitive that handles all three through configurable cross-layer combination of DNA-layer and action-layer content. The DNA layer carries stabilized orchestration logic — the architectural-pattern analog of biological genome. The action layer carries recorded experience — the analog of epigenetic memory and learned behavior combined. The three patterns become governance-configured combinations of which biology's distinctions are special cases: a Union over DNA layers approximates genetic recombination at high fidelity; a Selective merge over action layers approximates curated cultural transmission; a Lineage-preserved union approximates a richer-than-biology provenance contract. CKS does not commit to genetic-style high-fidelity copying or cultural-style low-fidelity imitation as separate mechanisms but to one configurable combination primitive tunable to whichever fidelity profile the offspring's goal requires.

A second axis on which CKS exceeds biology is **cross-lineage mating compatibility**. Biology's general case in canonical multicellular eukaryotes is reproductive isolation; the narrowing-contrast cases (horizontal gene transfer in prokaryotes, symbiogenesis as rare and transformative events, hybridization rate-limited and lineage-biased) narrow but do not invalidate the contrast. CKS commits to governance-configured cross-lineage combinations across all cell types as architectural commitment, not as exception.

A bound on the term: CKS mating is the broader combination primitive of which sexual-reproduction-style two-parent inheritance is one governance-configured pattern. The architecture does not commit to gametes, fertilization, meiosis, or two-parent-only configurations; whether a mating instance is two-parent biological-style, multi-parent, or self-derived from variants of one parent is configured by orchestration substrate. The biological analog functions as conceptual scaffold; the architectural substance is governable combination across two-layer architecture.

## 5. Inherited Paper 1 commitments

Mating inherits from Paper 1 without redefense. Six inheritances are load-bearing.

**A1.01 (human-governed)** is foundational at every layer of mating. The decision to mate, the choice of pattern, the rules determining which pattern applies, and the curation rules in Selective merge are all under human authority. Labor is allocable per A1.12; authority is not.

**A1.03 (conflict-as-first-class)** is foundational for Union. Union's commitment to preserving merge-time conflicts as first-class substrate state in the offspring is a direct extension of A1.03. Without A1.03, Union would either silently merge conflicting parental content (losing information) or refuse to mate (losing flexibility); with A1.03, Union preserves the conflicts as substrate content the offspring's cell-level orchestration rules govern at execution.

**A1.07 (path retraceability)** is foundational for Lineage-preserved union. The lineage pointers are an extension of A1.07's six-field provenance commitment. The mating event itself is recorded per A2.40 — what mated, when, under what pattern, by whose authority, against which substrate state, with what offspring identifier.

**A1.10 (determinism contract)** holds for mating operations. Given a fixed mating specification (parents, pattern, curation rules) and fixed parental substrate content at the moment of mating, the resulting offspring substrate is determined. Mating is not a stochastic process at the architectural level.

**A1.12 (labor allocation)** enables Selective merge. The curation labor is allocable across the three modes A1.12 specifies — humans directly, LLMs under human direction, stable cells under orchestration rules. Selective merge with LLM-mediated pre-curation under human review is exactly the deployment pattern A1.12 commits the architecture to supporting.

**A2.04 (orchestration rule authoring)** underwrites pattern selection. The rules determining which mating pattern applies under what circumstances are themselves substrate content authored by humans. Pattern selection is a design-time authoring decision that takes effect through substrate, not a runtime LLM decision.

These inheritances are not new commitments; they are Paper 1 commitments operating at the offspring level and at the mating event itself.

## 6. Operational implications

Five implications follow.

**Deployments configure mating governance per their needs.** Which patterns apply under which circumstances, who can authorize a mating event, what review processes precede a mating commit, what curation labor is allocated — all are deployment decisions configured through substrate.

**Offspring inherits Paper 1 commitments at the appropriate level.** Cell mating produces an offspring cell governed at cell scope per B1.03; aspect mating produces an offspring aspect at aspect scope per B1.04; Self mating produces an offspring Self at Self scope per B1.05.

**Cross-lineage mating is supported architecturally.** Biology's species barriers do not have an architectural analog in CKS. Two cells from different lineages can be mated through specification when orchestration substrate authorizes the combination — combining a regulatory cell's DNA with a customer cell's action history, mating an internal-process aspect with an external-coordination aspect, restructuring Selves through inter-lineage combinations under human authority.

**Mating events constitute lineage continuation points.** Subsequent operations on the offspring can reference parental lineages through Lineage-preserved union's pointers, through Union's preserved provenance metadata, or through the mating event's A2.40 record. Lineages remain reconstructible.

**Mating at each level has level-distinct semantics.** Cell mating combines the content of two cells — orchestration rules, schemas, recorded task instances, conflict-handling logic. Aspect mating combines the coordination structures of two aspects — which cells participate, how they interact, the aspect-level orchestration that ties them together. Self mating combines the integrated whole structures of two Selves. The three patterns apply at every level with level-distinct content.

## 7. Limits

Six limits keep the framing from drifting beyond what the source paper supports.

**Mating does not happen without orchestration governance.** Pattern selection is human-authored per A2.04. A mating event without authorized orchestration substrate specifying which pattern applies is not architecturally well-formed.

**Mating does not eliminate parental cells, aspects, or Selves automatically.** Death is a separate operation per B1.11. Whether parents persist or are retired (and through which death type — functional obsolescence or lineage supersession) is governed independently.

**Mating does not auto-resolve conflicts.** Union's commitment is to preserve merge-time conflicts as first-class substrate state per A1.03. Resolution is by human-authored meta-rule, by deferral, or by cell-level orchestration governing how the offspring handles preserved conflicts at execution. Auto-resolution would violate the architectural commitment.

**Mating does not replace de novo birth (B1.09).** Both origination patterns are available; deployments choose between them per origination event.

**Mating does not bypass Paper 1 commitments at the offspring level.** Offspring is a governed entity from the moment of mating; the six Paper 1 commitments hold at offspring scope by construction. Deployments cannot mate into an ungoverned offspring.

**The three patterns are not exhaustive.** Union, Selective merge, and Lineage-preserved union are the architecturally specified patterns. Additional patterns may be authored per A2.04 if deployment requires them — for example, a hybrid pattern that performs Selective merge on the DNA layer while applying Union to the action layer. The architectural specification commits to the three patterns; it does not preclude further patterns under the same governance envelope.

## 8. Operational test

A system instantiates the CKS mating-as-cross-layer-combination commitment if and only if all of the following are true.

1. Mating combines parental content across both the DNA layer and the action layer of the parents per B1.06.
2. The combination pattern is configurable per mating event through orchestration substrate authored under human authority per A2.04.
3. At minimum, the three architecturally specified patterns are available: Union (preserving content from both parents and registering merge-time conflicts as first-class substrate state per A1.03 and A2.45), Selective merge (with curation labor allocable per A1.12 and curation rules under human authority per A1.01), and Lineage-preserved union (with provenance pointers from offspring substrate elements back to parental sources per A1.07).
4. Each mating event is itself recorded with provenance per A2.40.
5. The offspring is a cell, aspect, or Self with full Paper 1 commitments inherited per B1.03/B1.04/B1.05 at the level of the mating event.

A system that fails any of (1)–(5) may be a useful system, and may have related operations such as ensemble fusion, model merging, software merge logic, or configuration-driven instantiation, but is not implementing CKS mating in the sense formalized here.

## 9. Conclusion

Mating is the second of three lifecycle primitives. Birth (B1.09) has been formalized as origination from specification under human governance. Mating is cross-layer combination of parental content across DNA and action layers through three orchestration-governed patterns. Death (B1.11) will be formalized as governed retirement with two distinct architectural results. Together the three constitute the lifecycle cluster within Phase B1.

Subsequent Phase B1 notes will elaborate the three evolution mechanisms (B1.12–B1.15: instinct evolution, DNA evolution, action-feedback evolution), bidirectional evolution along horizontal and vertical axes (B1.16), and structural properties under which the lifecycle and evolution machinery composes (B1.17–B1.20). Mating's distinctive role within this progression is enabling flexible inheritance across generations: without it the architecture would be limited to de novo birth as origination, and content carried forward across generations would have no governable combination primitive to flow through. Evolution mechanisms operate on a substrate where birth originates, mating combines, and death retires; mating is the primitive that makes succession-with-content-carryforward architecturally available.

The three patterns matter individually as well as collectively. Union makes Paper 1's conflict-preservation commitment architecturally available across mating events. Selective merge makes Paper 1's labor-allocation framework architecturally available at the moment of inheritance. Lineage-preserved union makes Paper 1's path-retraceability commitment architecturally available across generational succession. Each pattern is an extension of a Paper 1 commitment; no pattern introduces a new axiom; all three rest on the inheritances articulated in §5.

Subsequent work that adopts the CKS pattern, builds on Paper 2's lifecycle machinery, or extends the architecture into new operational primitives should use "mating" in the sense formalized here — cross-layer combination across DNA and action layers, with three orchestration-governed patterns serving distinct operational purposes, governed by humans throughout. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## Predecessor paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Mating as Cross-Layer Combination: A Foundational Commitment Establishing the Lifecycle Operation That Combines Parental Content Across DNA and Action Layers Through Three Orchestration-Governed Patterns.* May 7, 2026. ORCID: 0009-0004-8065-3235.
