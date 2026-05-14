# Instinct/Reasoning Separation Inherits the Substrate/LLM Hybrid

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its contribution is to state precisely what Paper 2's instinct/reasoning separation preserves from Paper 1's substrate/LLM hybrid commitment, what it adds, and why the inheritance relationship is structural rather than merely thematic.

## Abstract

Paper 2 of the CKS theory series commits to a separation of fast-pattern instinct from deliberate reasoning into two independently governed, independently evolving layers within every cell of a CKS-governed AI Self. Paper 1 of the same series commits to a hybrid architecture in which a human-governed substrate holds coordination knowledge and orchestration rules, while an LLM serves as the mediating agent that reads from and writes to the substrate under those rules. This note formalizes the inheritance edge: Paper 2's instinct/reasoning separation is a strict extension of Paper 1's substrate/LLM hybrid. The two-layer architectural principle, the commitment that substrate content governs behavior at each layer, the use of the LLM as mediator, and the requirement of human governance over both layers — all of these are preserved unchanged. What Paper 2 adds is the explicit naming and separation of fast-pattern processing from deliberate processing, the harness substrate as a new architectural object distinct from the coordination substrate, and the commitment to independent evolution of the two layers. Anyone implementing Paper 2's instinct/reasoning separation is necessarily implementing a refinement of Paper 1's hybrid commitment; the converse is not true.

## 1. Series C frame

This note opens Series C of the CKS derivation-note series. Series C comprises thirty notes (C1.01 through C1.30, sequential numbers #430 through #459) whose purpose is to formalize the inheritance edges that connect Paper 2's architectural commitments back to Paper 1's. Each note in Series C covers exactly one such edge.

The notation `Paper 2 commitment ⊃ Paper 1 commitment` denotes strict extension: the Paper 2 commitment satisfies every property the Paper 1 commitment requires AND adds new architectural commitments on top. The relationship is not isomorphism, and not mere thematic continuity. It is structural inheritance: any system instantiating the Paper 2 commitment necessarily instantiates the Paper 1 commitment within it, plus the additions Paper 2 names.

Series C's prior-art purpose is to foreclose adversarial readings that try to separate Paper 2 from Paper 1 — readings in which a party might claim that Paper 2's architectural moves are novel inventions independent of the Paper 1 hybrid, or that Paper 2 could be implemented without Paper 1's substrate-governance machinery. Formalizing the edges as named, dated, public prior-art notes closes that adversarial space. Each edge stands on its own as a derivation; the thirty together form a derivation chain from Paper 1 outward through every Paper 2 commitment.

This note covers the first and foundational edge: Paper 2's instinct/reasoning separation inherits from Paper 1's substrate/LLM hybrid.

## 2. The C1.01 inheritance edge stated

The edge formalized in this note is:

> **Paper 2's instinct/reasoning separation ⊃ Paper 1's substrate/LLM hybrid.**

In long form:

- The **Paper 1 commitment** (inherited side): a two-layer hybrid architecture in which a persistent, human-governed *substrate* holds coordination knowledge and orchestration rules, and the *LLM* serves as the mediating agent that reads from and writes to substrate content under those orchestration rules. The two layers have different governance properties: the substrate layer is the authoritative source of state; the LLM layer is the governed mediating agent. This is the foundational hybrid commitment of CKS, defended as Paper 1's Claim 1.

- The **Paper 2 commitment** (extending side): every cell of a CKS-governed AI Self carries two distinct, independently governed processing layers. The *instinct layer* is fast-pattern processing — LLM inference unsupplemented by deliberate substrate consultation, governed by harness substrates (human-authored specifications that determine when instinct is trusted, where it is routed, and how its outputs are integrated). The *reasoning layer* is deliberate processing — LLM mediation over coordination substrate content under orchestration rules, exactly as Paper 1 specified. The two layers are (i) independently governed by distinct substrate objects, (ii) independently evolving under distinct evolution mechanisms, and (iii) both subject to Paper 1's human-governance commitment.

The structural claim of this note is that the second commitment is a strict extension of the first. Sections 3 and 4 state precisely what is preserved and what is new.

## 3. What is preserved (inherited from Paper 1)

Four properties of the Paper 1 substrate/LLM hybrid carry through unchanged.

**Two-layer architecture principle.** Paper 1 commits to two distinct architectural layers with different governance properties — substrate as authoritative state holder; LLM as governed mediating agent. Paper 2 preserves this exactly: instinct and reasoning are two distinct architectural layers with different governance properties. The principle that a CKS-governed AI system has *two* layers, not one, is inherited without modification. Paper 2 does not collapse the substrate into the LLM, does not collapse instinct into reasoning, and does not introduce a third architectural layer at the same level of abstraction. It instantiates the same two-layer principle at the level of in-cell processing.

**Substrate-governs-behavior principle.** Paper 1 commits that explicit, human-authored substrate content governs cell behavior — orchestration rules determine what the cell does, how the LLM is allowed to operate, and how conflicts are handled. Paper 2's reasoning layer satisfies this directly: it is the layer that reads from coordination substrate under orchestration rules. The instinct layer also satisfies this commitment, but with respect to a different substrate object: the harness substrate. Both layers are governed by explicit substrate content; neither layer escapes substrate governance.

**LLM-as-mediator principle.** Paper 1 commits that the LLM's role is to help the substrate and its users read, write, interpret, and compose substrate content, and to execute cell operations in accordance with orchestration rules. The LLM is the mediating agent; it is not the authoritative state holder, and has no authority to override substrate content or orchestration rules. Paper 2 preserves this at the reasoning layer. At the instinct layer, the LLM is the source of fast-pattern outputs — its weights produce them — but the harness substrate retains authority to route, verify, override, and pin. The LLM does not gain authority by being the source of instinct outputs.

**Human governance at both layers.** Paper 1 commits that humans retain the right to inspect, modify, and override substrate content and orchestration rules at any time. Paper 2 inherits this at both layers: the coordination substrate (governing reasoning) remains human-governed exactly as Paper 1 specified, and the harness substrate (governing instinct) is also human-governed by the same definition. No layer of Paper 2's architecture is outside human governance.

These four preserved properties are why the inheritance is structural and not merely thematic. An implementation of Paper 2's separation that violated any of them would also violate Paper 1's hybrid commitment, because the four properties together are what the hybrid commitment names.

## 4. What is new in Paper 2

Three architectural commitments in Paper 2 are not present in Paper 1 and are added on top of the inherited four.

**Explicit naming and separation of fast-pattern from deliberate processing.** Paper 1 commits to a substrate/LLM hybrid in which the LLM handles high-dimensional reasoning. Paper 1 does not distinguish, within the LLM's role, between fast-pattern responses (where the model's trained dispositions are taken as sufficient and no substrate consultation is required) and deliberate processing (where the model reads from substrate content, applies orchestration rules, and produces a substrate-mediated output). Paper 2 introduces this distinction as architectural commitment. Fast-pattern instinct is named as one layer; deliberate reasoning is named as another. The separation is not optional; it is part of every Paper 2 cell.

**The harness substrate as a new architectural object.** Paper 1 names one kind of substrate object — coordination substrate that holds entities, relationships, decisions, rationale, and conflicts, together with orchestration rules that govern cell behavior. Paper 2 introduces a second kind of substrate object: the *harness substrate*. The harness substrate is human-authored content that governs the instinct layer specifically — it specifies which fast-pattern outputs are routed to verification, which are accepted directly, which are pinned to the reasoning layer, and how the instinct-reasoning boundary itself is positioned. This is a distinct architectural object: it is not coordination substrate (it does not hold coordination knowledge of the kind Paper 1 specified), and it is not orchestration rules in Paper 1's sense (it governs the instinct layer rather than cell-level execution over coordination content). It is a Paper 2 invention that has no Paper 1 ancestor at the object level, even though it inherits the substrate-governs-behavior principle from Paper 1 at the principle level.

**Independent evolution of the two layers.** Paper 1 does not commit to any particular evolution mechanism for the substrate-LLM hybrid. The substrate can grow, orchestration rules can be revised, the LLM can be replaced — but Paper 1 makes no architectural commitment to how these changes interact. Paper 2 makes a strong commitment here: the two layers evolve through different mechanisms operating on different objects. Instinct evolution is *mutation*, affecting the LLM's fast-pattern capability through upgrades and substrate-platform sharpening. DNA evolution and action-feedback evolution are *directed selection*, affecting the coordination substrate, harness substrate, and orchestration rules through governed authoring and refinement. The two evolution paths do not cross-interfere by default; an instinct upgrade does not silently modify reasoning behavior, and a DNA revision does not require an instinct upgrade. The independence is itself an architectural commitment, governed by the same human-governance commitment that holds the layers themselves.

These three additions are what make Paper 2 a strict extension rather than a restatement. They define new architectural objects (harness substrate), new architectural distinctions (instinct vs reasoning as named layers), and new architectural dynamics (independent evolution of the two layers under three distinct mechanisms in productive tension).

## 5. Why the inheritance is structural

A system implementing Paper 2's instinct/reasoning separation must have: a fast-pattern processing layer, a deliberate processing layer, harness substrate governing the first, coordination substrate governing the second, the LLM mediating both, and humans holding inspect-modify-override authority over both substrate objects. Any such system automatically satisfies Paper 1's hybrid commitment — the Paper 1 commitment is contained within the Paper 2 commitment by construction.

The converse does not hold. A Paper 1 implementation may treat all LLM output uniformly without distinguishing fast-pattern from deliberate processing, may have no harness substrate (because all governance flows through orchestration rules over coordination substrate), and may have no independent-evolution commitment. A Paper 1 system can be perfectly correct without naming or separating the two processing layers Paper 2 names. This asymmetry is the definition of strict extension.

## 6. Prior-art significance

The inheritance edge formalized in this note serves a specific prior-art function in the CKS derivation series.

An adversarial reading might attempt to separate Paper 2 from Paper 1 in one of three ways: (i) claiming that the instinct/reasoning separation is a novel architectural invention with no Paper 1 ancestor; (ii) claiming that the harness substrate is a separable invention that does not require the Paper 1 substrate machinery to function; (iii) claiming that the two-layer-independent-evolution dynamic stands without the Paper 1 hybrid foundation.

Formalizing the edge forecloses these readings. The separation cannot be claimed as novel relative to the hybrid because it is a strict extension of that hybrid — the two-layer principle, the substrate-governs-behavior principle, the LLM-as-mediator principle, and human-governance at both layers all come from Paper 1. The harness substrate cannot be claimed as separable from Paper 1's substrate-governance machinery because it inherits the substrate-governs-behavior principle and the human-governance commitment that define what *substrate* means in CKS. Independent evolution cannot be claimed as standalone because it operates over the two layers Paper 1 named (as substrate and LLM) and Paper 2 refined (as reasoning layer and instinct layer).

The publication of this note establishes that as of its date, the inheritance edge `Paper 2 instinct/reasoning ⊃ Paper 1 substrate/LLM` is public prior art under Wenxin Li's name. Subsequent claims that the Paper 2 separation is novel, that the harness substrate is freestanding, or that independent evolution is a Paper-2-only contribution encounter this prior-art chain.

## 7. Operational test

A given cell deployment instantiates the C1.01 inheritance edge if and only if an observer can verify all of the following:

1. The cell exhibits two distinct processing layers: a fast-pattern layer that produces outputs without consulting coordination substrate at decision time, and a deliberate layer that reads from coordination substrate and applies orchestration rules during processing.

2. The observer can identify the harness substrate that governs the fast-pattern layer — a named, inspectable artifact containing human-authored content that specifies when fast-pattern outputs are accepted, when they are verified, and when they are pinned to the deliberate layer regardless of fast-pattern capability.

3. The observer can identify the coordination substrate and orchestration rules that govern the deliberate layer — named, inspectable artifacts holding coordination content and the rules that determine deliberate-layer behavior.

4. The two substrate objects are distinct artifacts — modifying the harness substrate does not directly modify coordination substrate content, and modifying coordination substrate or orchestration rules does not directly modify the harness substrate. Both kinds of modification take effect through human authority, not through cross-layer side effects.

5. Both substrate objects are human-governed in the sense of the CKS definition: humans with appropriate access retain inspect, modify, and override rights over both at all times, with no LLM operation, vendor policy, or runtime intermediation able to prevent those rights in principle.

6. The observer can trace, for any cell behavior produced under deployment, which layer produced it (fast-pattern or deliberate) and which substrate governs that layer (harness substrate for fast-pattern; coordination substrate plus orchestration rules for deliberate).

A deployment passing all six checks instantiates Paper 2's instinct/reasoning separation, and by the inheritance edge formalized here, also instantiates Paper 1's substrate/LLM hybrid commitment within it. A deployment failing any of the six does not instantiate the C1.01 commitment — it may instantiate some other architecture, but not the one this inheritance edge names.

## 8. Conclusion

The first and foundational inheritance edge of Series C is `Paper 2 instinct/reasoning separation ⊃ Paper 1 substrate/LLM hybrid`. Paper 2 preserves the two-layer architecture principle, the substrate-governs-behavior principle, the LLM-as-mediator principle, and the human-governance commitment from Paper 1. It adds the explicit naming and separation of fast-pattern instinct from deliberate reasoning, the harness substrate as a new architectural object governing the instinct layer, and the commitment that the two layers evolve independently through distinct mechanisms.

The inheritance is structural: any implementation of the Paper 2 separation contains an implementation of the Paper 1 hybrid within it; the converse does not hold. Subsequent work that adopts, extends, or argues against Paper 2's instinct/reasoning separation should treat the inheritance from Paper 1's hybrid commitment as part of what is being adopted, extended, or argued against. Work that attempts to separate the two is using a different architecture, and the difference should be named.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Instinct/Reasoning Separation Inherits the Substrate/LLM Hybrid.* May 14, 2026. ORCID: 0009-0004-8065-3235.
