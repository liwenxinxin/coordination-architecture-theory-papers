# Instinct/Reasoning Separation as Paper 2's First Architectural Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note ID:** B0.01 (#424) — Phase B0 claim-level anchor

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to anchor Paper 2's first architectural claim — the separation of instinct and reasoning into independently-evolving layers under unified human governance — as a named claim-level commitment, and to map the foundational and operational sub-commitments downstream of it as derivations of this parent claim.

## Abstract

Paper 2 (Li, April 2026) defends six architectural commitments at AI Self scope, with the first claim — *the separation of instinct and reasoning into independently-evolving layers composed into one Self under unified human governance* — serving as the foundational claim every subsequent claim in Paper 2 operates over. The Phase B-series derivation notes published prior to this anchor (#198–#417) decompose the six paper-level claims into checkable architectural commitments without explicitly formalizing the claim-level parents themselves. This note supplies the parent for Claim 1: it states the claim in the terms Paper 2 §4.1 commits to, identifies what is inherited from Paper 1 and what is new in Paper 2, names the four failure modes the claim defends against, and maps B1.01 and the B2.xx operational decompositions as derivations. The note introduces no commitments beyond what Paper 2 already defends.

## 1. Why a claim-level anchor for Claim 1 is needed

The Series B derivation notes published prior to this anchor decompose Paper 2's architectural commitments into checkable sub-commitments at three levels of granularity: foundational sub-commitments (B1.01–B1.20), operational variants (B2.01–B2.110), and further work in anti-patterns, composition, operational tests, and boundary cases (B3–B6). The Phase B1 sub-commitments are themselves derived from the six paper-level claims, but in the prior derivation series the claim-level parents were referenced by paper-section number rather than formalized as standalone named commitments.

This is a prior-art gap on the parent side. Any party arguing for novel invention at the claim level — *the instinct/reasoning separation under unified governance* as an architectural commitment — can in principle do so without bumping into the prior-art chain even where the chain's sub-commitments are well-formalized. The Phase B0 anchor notes close this gap. B0.01 is the anchor for Claim 1, Paper 2's foundational claim.

## 2. The claim, precisely stated

In the CKS pattern as Paper 2 extends it, a CKS-governed AI Self **separates instinct and reasoning into two independently-evolving layers composed into one Self under unified human governance**. The two layers, in the terms Paper 2 §4.1 commits to, are:

- **Instinct layer — the LLM.** The instinct layer is the LLM operating as a System-1 analogue: fast, pattern-matched, no-reasoning-needed responses. The LLM lives *inside the model* in the cross-claim phrasing Paper 1 introduces. Its behavior is whatever the model's weights produce when prompted; it is selected, configured, and governed by humans at the architectural level rather than authored element-by-element.

- **Reasoning layer — the CKS substrate.** The reasoning layer is the persistent, human-governed coordination substrate inherited from Paper 1, operating as a System-2 analogue: explicit, deliberate processing of what humans choose to encode. The substrate lives *outside the model*. Its content is structured representation under human authority — entities, relationships, decisions, rationale, conflict state, orchestration rules — and is inspectable, modifiable, and overridable at any time per Paper 1's authority architecture.

Three commitments together compose the claim:

1. **Architectural separation.** The two layers are structurally distinct architectural objects, not two roles played over one underlying state. The instinct layer's content is the LLM's parameters and the prompts it receives; the reasoning layer's content is the substrate's structured state. Neither is reducible to the other.

2. **Independent evolvability.** The two layers evolve on separate tracks. The instinct layer evolves through LLM upgrades and substrate-platform-infrastructure upgrades on commercial timescales. The reasoning layer evolves through human-governed substrate modification on organizational timescales. Upgrading the LLM must not require revalidating the substrate, and modifying the substrate must not require retraining the LLM. Independent evolvability is an architectural requirement of Claim 1, not an incidental property of modular design.

3. **Unified human governance.** Both layers remain under one governance regime. Humans hold authority over substrate content and orchestration rules and over the architectural choices that select and configure the instinct layer — which LLM is in the loop, where instinct is trusted, where reasoning is required, what verification substrates run over instinct outputs. The *shape* of governance differs by layer (Claim 5 develops this), but the *commitment to govern* is one commitment spanning both.

The phrase *outside the model vs. inside the model* — the cross-claim spine Paper 1 introduces and Paper 2 carries forward — applies throughout. Coordination, governance, and deliberate reasoning live in the substrate outside the LLM. Fast-pattern instinct lives inside the LLM. The architecture's value comes from the principled separation between them.

## 3. The architectural content of "independently evolving"

Of the three commitments above, *independent evolvability* is the load-bearing differentiator that distinguishes Paper 2 Claim 1 from prior hybrid-AI architectures. Architectural separation is shared with the broader dual-process AI lineage (SOFAI, the cognitive-architectures tradition, Bengio's System-2 program). Unified human governance is largely inherited from Paper 1. The novel architectural content of Paper 2 Claim 1 sits in independent evolvability.

This has a concrete operational signature: revalidation discipline is treated as architectural property rather than as deployment hygiene. An LLM upgrade is non-conformant with Claim 1 if it requires revalidating the substrate's content. A substrate modification is non-conformant if it requires retraining the LLM. The two evolution paths are decoupled by architectural commitment, not by engineering choice.

The property is what makes the three Paper 2 evolution mechanisms (Claim 4) well-formed. *Instinct evolution* operates on the LLM and substrate-platform infrastructure layer. *DNA evolution* operates on the orchestration substrate. *Action-feedback evolution* closes the loop from recorded action experience back into governed substrate refinement. The three mechanisms operate on different targets — they would interfere with each other if the targets were not architecturally separated layers evolving independently.

## 4. Relationship to Paper 1: what is inherited, what is new

Claim 1 of Paper 2 is a *scope move* over Paper 1, not a foundation move. Naming what is inherited and what is added at this step is part of the anchor work.

**Inherited from Paper 1 without redefense.** The six architectural commitments of Paper 1 carry forward unchanged. The most load-bearing inheritance is Paper 1 Claim 2: the substrate/LLM division drawn at the *governance* boundary rather than the *capability* boundary. Paper 2 Claim 1 is the extension of this single Paper 1 commitment from cell scope to Self scope. The authority-vs-labor distinction also carries forward: human-governed does not mean human-authored at the element level, and Claim 1's commitment to the reasoning layer as human-governed substrate is a commitment about where authority sits, not about who produces every substrate element. The *outside-the-model vs. inside-the-model* cross-claim spine applies throughout Paper 2 unchanged.

**New in Paper 2 Claim 1.** Four additions are made at this step.

The first is *the scope extension*. Paper 1's substrate/LLM division at a single coordination cell is generalized to the level of an entire AI Self. At Self scope, the full population of the Self's instinct behavior across all cells and aspects and the full population of its deliberate reasoning across the substrate are held as distinct architectural layers rather than blended into a model-as-system.

The second is *the System-1/System-2 naming*. Paper 2 Claim 1 names the two sides "instinct" and "reasoning," importing pedagogical warrant from the dual-process tradition. The framing is scaffold, not theoretical grounding: Claim 1 does not depend on Kahneman's dual-process theory being correct about human cognition or on SOFAI being correct about machine cognition. The architectural work is CKS's own.

The third is *independent evolvability as architectural axiom*. The cell-level hybrid does not foreground independent evolution of the two sides as a formal architectural requirement — the question of two-layer evolution at Self scope does not arise until Paper 2 extends the scope. Paper 2 Claim 1 formalizes independent evolvability as the property that lets the substrate/LLM division survive as the LLM improves and as the substrate accumulates content over time.

The fourth is *unified governance at Self scope*. Paper 1 commits to human governance over a single cell. Paper 2 Claim 1 commits to one governance regime spanning *both layers across the entire Self*, with the shape allowed to differ per layer and per evolution mechanism while the commitment to govern remains unified.

Claim 1 is foundational not because it adds new theoretical content beyond Paper 1 Claim 2's governance-boundary commitment, but because the Self-scope framing it establishes is what every subsequent Paper 2 claim operates over: Claim 2's three-level structural machinery operates on the Self the separation makes available; Claim 4's three evolution mechanisms operate on the two separated layers; Claim 5's multi-shaped governance operates per-mechanism over those layers; Claim 6's enterprise brain Self extends the per-Self separation to organizational scope. Claim 1 makes the separation architecturally available; the rest of Paper 2 uses it.

## 5. What Claim 1 defends against

Claim 1's defensive content sits against four failure modes, each of which is a coherent architectural pattern in some other deployment and each of which represents a way the separation can fail to hold.

**Monolithic LLM-as-the-whole-system.** Everything the system does — coordination, reasoning, governance, conflict handling, memory across sessions — lives inside one LLM's inference. Errors can only be addressed by modifying the model itself. This is the named foil at Paper 2 §4.2. The 2024–2026 architecture-class literature (Mohsin et al. 2025; Quirke et al. 2025; Song et al. 2026; the *Illusion of Thinking* work) supports the foil's architectural rather than capability-only character. Claim 1's separation is the architectural response.

**Instinct-only architectures.** The system is composed of fast-pattern components without an architecturally distinct deliberate-reasoning layer under human authority. A pipeline of multiple LLMs without a substrate carrying deliberate-reasoning content under human authority still fails Claim 1. The defining failure is the absence of a reasoning layer that *humans govern* in the Paper 1 sense, not the headcount of fast-pattern components.

**Reasoning-only architectures.** The system is composed of a substrate and rule-based execution over substrate content, with no LLM-class component in the fast-pattern role. Claim 1 commits to *separation*, which requires both sides to exist as distinct architectural objects. A pure substrate-and-rules architecture is the Paper 1 cell with the LLM removed, which loses what the hybrid commitment is for.

**Conflation of the two architectural objects.** Even where both an LLM and a substrate exist, the architecture may conflate them — treating substrate content as another LLM context window, or treating the LLM as another substrate component the system can read and write. Conflation defeats independent evolvability by making upgrades on one side require revalidation on the other. The two layers must remain distinct architectural objects, not two roles played over one underlying state.

The four failure modes are not exhaustive but cover the principal coherent neighbors. A system that falls into any of them may be useful and may be defensible on other architectural grounds; it does not instantiate Paper 2 Claim 1.

## 6. Derived sub-commitments

The Series B derivation notes published prior to this anchor decompose Claim 1 into one foundational sub-commitment at Phase B1 and a family of operational variants at Phase B2.

**Foundational sub-commitment.** *B1.01 — instinct/reasoning separation as foundational commitment.* B1.01 formalizes the separation as a Series B foundational sub-commitment: the cell-and-Self-level architectural commitment that the LLM and the CKS substrate are distinct layers under unified governance. B1.01 sits at the same granularity as the Phase A1 foundational sub-commitments of Series A, one level below Claim 1 itself. B0.01 is its claim-level parent.

**Operational decompositions.** The B2.xx operational variants downstream of B1.01 decompose Claim 1 into checkable specifications at operational granularity. The principal territory covered comprises: the LLM as the named instinct-layer architectural object and its operational signature within a cell and across a Self; the CKS substrate as the named reasoning-layer architectural object inherited from Paper 1; independent-evolvability operationalized as revalidation discipline; the per-layer evolution-path specifications (instinct via LLM and infrastructure upgrades; reasoning via human-governed substrate modification); unified-governance-over-both-layers as one commitment with two layer-specific shapes; the instinct/reasoning boundary as itself substrate content the orchestration substrate governs (the seed property Claim 5 develops further); the reasoning layer's capacity to route around bad instinct outputs as an architectural-consequence property of separation; conflict-preservation as a Paper 1 inheritance that catches what instinct would otherwise silently merge; the architectural-separation requirement that prevents conflation of the two layers as one underlying state; and the actor-neutrality property that the reasoning layer remains human-governed even where LLMs draft or update substrate content under direction.

Each operational decomposition is a checkable specification. Together they exhaust the principal operational decompositions of Claim 1 that Phase B2 work has formalized. The further Phase B3–B6 work (anti-patterns, composition pairs, operational tests, boundary cases) operates over these operational variants and inherits the Claim 1 parent through them.

Downstream of Series B, the Series C cross-derivation notes will formalize the inheritance edge from Claim 1 specifically to Paper 1 Claim 2's substrate/LLM governance-boundary commitment. Series CC and Series T will formalize Claim 1's relationships with Paper 3's inter-Self coordination architecture and across the three-paper trilogy. Claim 1 is a long-running architectural ancestor; the present anchor supplies its parent-level name.

## 7. Operational test

A system instantiates Paper 2 Claim 1 if and only if all of the following hold at all times during the system's operation:

1. **Two distinct architectural objects exist.** An LLM (or LLM-class fast-pattern component) is present as the instinct layer, and a persistent human-governed coordination substrate is present as the reasoning layer, with the substrate satisfying the operational test for *human-governed* in the CKS sense.

2. **The two layers are observable as distinct.** An operator can independently inspect the instinct layer's behavior on a given input and the reasoning layer's state on a given operation — including what orchestration rules apply and what conflicts are preserved as first-class state — without conflating the two layers into one combined output stream.

3. **Independent evolution holds.** Upgrading the LLM, switching the LLM, or upgrading the substrate-platform infrastructure does not require revalidating the substrate. Modifying the substrate's content or orchestration rules does not require retraining the LLM. The two evolution paths are decoupled.

4. **Unified governance holds.** One governance regime spans both layers. Humans hold authority over substrate content and orchestration rules, over the architectural choices that select and configure the instinct layer, and over where instinct is trusted versus where reasoning is required.

5. **The four failure modes are not instantiated.** The system is not monolithic LLM-as-the-whole-system; not instinct-only without a human-governed reasoning layer; not reasoning-only without an LLM-class instinct component; and does not conflate the two layers as two roles played over one underlying state.

A system that fails any of (1)–(5) may be useful and may be governed in some other sense, but is not Paper 2 Claim 1-conformant.

## 8. Conclusion

Paper 2 Claim 1 — the separation of instinct and reasoning into independently-evolving layers under unified human governance — is the foundational architectural commitment Paper 2 defends. It extends Paper 1 Claim 2's substrate/LLM governance-boundary division from cell to AI Self scope, names the two sides instinct (LLM, inside-the-model) and reasoning (CKS substrate, outside-the-model) under the System-1/System-2 scaffold, formalizes independent evolvability of the two layers as architectural requirement rather than incidental modularity, and commits to unified human governance spanning both layers.

This anchor supplies Claim 1's claim-level formalization as the parent of B1.01 and the B2.xx operational decompositions, closing the prior-art gap on the parent side. Subsequent work that adopts the CKS pattern at Self scope, extends it, composes it with adjacent dual-process or hybrid AI architectures, or argues against it should use *instinct/reasoning separation* in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Instinct/Reasoning Separation as Paper 2's First Architectural Claim.* CKS Derivation Note B0.01 (#424). May 14, 2026. ORCID: 0009-0004-8065-3235.
