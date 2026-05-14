# Instinct/Reasoning Boundary Inherits Paper 1's Within-Cell Governance Boundary

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** C — Cross-Derivation Notes (Paper 1 ↔ Paper 2)
**Note ID:** C1.25 (#454 in continuous series)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series.

---

## Abstract

Paper 2 of the CKS theory series introduces the instinct/reasoning boundary: a specification, within a cell, of which inputs and operations are handled by the fast-pattern instinct layer and which are handled by the deliberate reasoning layer. This note formalizes the inheritance edge C1.25: the instinct/reasoning boundary inherits Paper 1's governance boundary concept, instantiated at within-cell scope rather than at the external cell-substrate perimeter. What is preserved across the inheritance is the two-sided architectural structure, the principle that human governance applies on both sides via substrate content, the placement of the boundary itself as governed substrate content, and the commitment that the LLM mediates on the deliberate-processing side. What is new in Paper 2 is the within-cell location of the boundary (internal rather than external), the treatment of the boundary as an explicitly authored governance object, the capacity for per-entity boundary variability under multi-shaped governance, and the consequent property that the boundary is an evolution target — modifiable through directed selection as an entity's operational profile changes. The note distinguishes C1.25 from C1.04, which covered the external governance perimeter; positions both as distinct instantiation angles on the same Paper 1 boundary concept; provides an operational test; and states the prior-art significance.

---

## 1. The Inheritance Edge Stated

Paper 1 of the CKS theory series defends a governance boundary between the substrate layer and the LLM execution layer at cell scope. On the substrate side: human-governed, persistent, authoritative content subject to the three rights of inspection, modification, and override. On the LLM execution side: AI-mediated processing operating under orchestration rules, holding no shadow state that competes with the substrate's authority. The boundary is not a capability boundary — it does not say which tasks the LLM is good at. It is a governance boundary: it specifies where human authority directly applies and where the LLM mediates under human-authored rules.

Paper 2 introduces the instinct/reasoning boundary within a cell. This boundary specifies, for each entity, which inputs and operations are handled by the instinct layer (fast-pattern, LLM-based, harness-substrate-governed) and which are handled by the reasoning layer (deliberate, substrate-mediated, operating under orchestration rules). The boundary is not implicit in the cell's architecture. It is an explicitly authored governance object: substrate content that specifies where, for this entity, instinct handling ends and reasoning handling begins.

C1.25 formalizes the inheritance relationship: Paper 2's instinct/reasoning boundary ⊃ Paper 1's governance boundary, instantiated at within-cell scope. The instinct/reasoning boundary is a second, internal instantiation of the same boundary concept Paper 1 establishes at the cell's external perimeter. What the boundary separates, how it governs both sides, what it is made of, and how the LLM is positioned on the mediation side — all of these carry the Paper 1 governance boundary identity forward. What is new is that the boundary is now internal to the cell, explicitly authored, variable per entity, and modifiable through governance over the cell's lifetime.

---

## 2. What the Instinct/Reasoning Boundary Inherits

Four properties identify the governance boundary concept that Paper 1 establishes and that C1.25 shows Paper 2 inherits.

**Two-sided architecture.** Paper 1's governance boundary creates exactly two sides: the substrate side, where human governance applies directly, and the LLM execution side, where the LLM mediates under orchestration rules. The instinct/reasoning boundary within a cell creates the same two-sided structure. The instinct layer sits on the governed side: its behavior is determined by harness substrates that are human-authored orchestration content. The reasoning layer sits on the mediated side: it uses the LLM to process what humans have encoded in the coordination substrate, operating under orchestration rules that govern what the LLM can read, write, and infer. The structural logic — governed side, mediated side, boundary between them — is preserved without modification.

**Human governance applies on both sides.** A potential misreading of the two-sided structure is that governance applies on one side and automation applies on the other. Paper 1 rules this out: the LLM execution side is not ungoverned; it is governed through orchestration rules that are human-authored substrate content. The instinct/reasoning boundary preserves this property. The instinct layer is governed through harness substrates — substrate content that specifies which patterns the instinct layer handles and under what conditions. The reasoning layer is governed through coordination substrates and orchestration rules. Human governance, as the authority to inspect, modify, and override substrate content and orchestration rules on both sides, holds throughout. Paper 2 Claim 5's multi-shaped governance is precisely the statement that governance holds differently across mechanisms, not that it holds only on one side.

**The boundary is itself substrate content.** In Paper 1, the governance boundary is implicit in the hybrid architecture: it is a structural consequence of the substrate/LLM division of labor, not a named, authored artifact. But the principle that the governance boundary is itself governed — that the rules determining where the boundary operates are human-authored orchestration content — is present in Paper 1. The instinct/reasoning boundary in Paper 2 inherits this principle and makes it explicit. The boundary specification is authored substrate content: it is subject to the three rights (inspect, modify, override), it is independently addressable, and it is modifiable without modifying the LLM's weights. The boundary's position within the cell is a governance decision, recorded as a governance artifact. This authored-boundary-as-substrate-content property is what makes the instinct/reasoning boundary a second instantiation of Paper 1's governance boundary concept rather than a merely structural analogy to it.

**The LLM mediates on the deliberate-processing side.** Paper 1's foundational commitment — substrate handles coordination and governance, LLM handles high-dimensional reasoning, division at the governance boundary rather than the capability boundary — carries directly into the reasoning layer's architecture. On the reasoning side of the instinct/reasoning boundary, the LLM reads from the coordination substrate, processes under orchestration rules, and writes under governance constraints. The LLM holds no shadow state that competes with the substrate's authority. This is Paper 1's AI-as-substrate-mediator commitment, applied to the within-cell reasoning layer without modification.

---

## 3. What Is New in Paper 2

Four properties are new to the instinct/reasoning boundary and are not inherited from Paper 1's governance boundary.

**Within-cell location.** Paper 1's governance boundary is external to the cell's internal processing — it demarcates the cell as a unit from the substrate and LLM layers at the perimeter level. The instinct/reasoning boundary is internal to the cell: it operates within the cell's execution, specifying which branch of internal processing each input and operation takes. This within-cell location is what makes C1.25 a distinct note from C1.04. C1.04 covered the external governance perimeter — how Paper 2's nested three-level boundary structure (cell, aspect, Self) inherits Paper 1's external perimeter concept. C1.25 covers the internal cell boundary — how Paper 2's within-cell instinct/reasoning specification instantiates the same Paper 1 boundary concept at a different structural location. The two notes cover different instantiation angles on the same inherited concept; neither subsumes the other.

**Explicitly authored boundary specification.** In Paper 1, the governance boundary is architecturally given: a system either implements the substrate/LLM division or it does not, and the boundary's position is fixed by the architecture's structure rather than by an authored content item. Paper 2 makes the instinct/reasoning boundary an explicit authored governance object. For each entity, the specification is a substrate content item that states: these input types and operations are instinct-handled; these input types and operations are reasoning-handled; these conditions trigger escalation from instinct to reasoning. The specification is not system-defaulted or vendor-determined. It is authored, named, and addressable as substrate content. An observer with inspection rights can find the specification, read it, verify that it was human-authored (or authored by an LLM under human direction), and confirm that it is independently modifiable per the three rights.

**Per-entity boundary variability.** Paper 1's governance boundary is uniform across cells: every cell instantiates the same substrate/LLM division at the same structural location. The instinct/reasoning boundary within a cell can vary across entities. One entity's boundary specification may route all pattern-matching operations to instinct and escalate only novel exception cases to reasoning. Another entity's boundary specification may pin high-stakes decisions architecturally to reasoning regardless of how capable its instinct layer becomes, ensuring that governance explicitly covers the decision path on safety-critical operations. This per-entity variability is what Paper 2 calls multi-shaped governance. Different operational profiles warrant different boundary positions. The authored-specification property is what makes the variability governable: the boundary's position is not an emergent property of the LLM's capability profile; it is a governance decision recorded as substrate content.

**Boundary as evolution target.** Because the instinct/reasoning boundary is substrate content, it is subject to directed selection — one of Paper 2's three evolution mechanisms. Governance can shift where the boundary falls for an entity over time. As instinct capability sharpens through instinct evolution (LLM and infrastructure upgrades), governance can decide to collapse previously-reasoned decisions to instinct, provided verification confirms the collapse is safe. As an entity's operational scope changes, governance can expand the reasoning layer's domain for categories of decision that newly warrant deliberate processing. As reliability evidence accumulates, governance can relax or tighten escalation conditions. None of this requires modifying the LLM's weights. It requires modifying the boundary specification as substrate content, under the same authority architecture that governs all other substrate content changes. The boundary evolves as a governed artifact, not as a system-determined emergent property. This evolution-target property has no parallel in Paper 1, where the external governance boundary is fixed by the architecture's structural commitments rather than by an authored specification that governance can update.

---

## 4. Positioning Relative to C1.04

C1.04 and C1.25 are both Series C notes formalizing inheritance from Paper 1's governance boundary concept. They cover different instantiation angles and are complementary rather than redundant.

C1.04 established that Paper 2's governance perimeter — the nested three-level boundary structure across cell, aspect, and Self — inherits Paper 1's external governance boundary. The governance perimeter is the boundary that demarcates each structural unit (cell, aspect, Self) from the coordination substrate and the wider architecture: the same external perimeter concept Paper 1 defends at cell scope, extended to operate at three nested scopes in Paper 2.

C1.25 establishes that Paper 2's instinct/reasoning boundary — the within-cell specification of where fast-pattern handling ends and deliberate processing begins — inherits Paper 1's governance boundary concept at a different instantiation level. The instinct/reasoning boundary is not the cell's external perimeter; it is a boundary that operates inside the cell, between two layers of the cell's own internal processing.

Together, C1.04 and C1.25 show that the Paper 1 governance boundary concept instantiates in Paper 2 at two distinct structural locations: at the external perimeter of each structural unit (C1.04) and at the internal processing boundary within each cell (C1.25). Both locations carry the same two-sided architecture, the same human-governance-on-both-sides principle, the same boundary-as-substrate-content property, and the same LLM-mediates-on-the-deliberate-side commitment. The two notes together establish that Paper 1's governance boundary concept is not a single-instantiation architectural feature; it is a design principle that operates at multiple structural locations throughout Paper 2's architecture.

---

## 5. Operational Test

For any CKS cell, the instinct/reasoning boundary inherits Paper 1's governance boundary if and only if the following conditions hold:

**Locatability.** An observer with inspection rights can find, within the cell's substrate content, a named boundary specification that states which input types and operations are instinct-handled and which are reasoning-handled. The specification is not embedded in the LLM's weights, inferred from operational behavior, or reconstructed from system configuration files outside the substrate. It is a substrate content item with a defined location, accessible under the inspect right.

**Human-authorship verifiability.** The observer can verify that the boundary specification was authored by a human or by an LLM operating under human direction with human approval of the specification's content. The specification was not system-defaulted or vendor-assigned as a non-overridable initialization parameter. Evidence of human authorship or human-directed authorship is traceable in the substrate's provenance.

**Independent modifiability.** The observer can confirm that the boundary specification is modifiable, under the modify right, without requiring modification of the LLM's weights, the underlying infrastructure, or any component outside the substrate. A change to the boundary specification — moving a category of operation from instinct-handled to reasoning-handled, or relaxing an escalation condition — is a substrate edit operation under the authority architecture Paper 1 establishes.

**Two-sided governance.** The observer can confirm that both the instinct layer and the reasoning layer operate under substrate content that is human-governed in Paper 1's sense: the three rights (inspect, modify, override) apply to harness substrates governing the instinct layer and to coordination substrates and orchestration rules governing the reasoning layer.

A cell that satisfies all four conditions instantiates the within-cell governance boundary that C1.25 formalizes. A cell whose instinct/reasoning handling is determined by the LLM's internal capability profile alone, without an independently locatable, human-authored, and independently modifiable boundary specification in substrate content, does not instantiate the commitment — even if it happens to route some operations differently from others.

---

## 6. Prior-Art Significance

C1.25 forecloses three categories of adversarial claim.

**Claim category (a): An explicit within-cell architectural boundary separating fast-pattern from deliberate processing is novel relative to Paper 1's governance boundary.** This claim fails because the within-cell instinct/reasoning boundary is a direct instantiation of Paper 1's governance boundary concept at a different structural location. The two-sided structure, the human-governance-on-both-sides principle, the boundary-as-substrate-content property, and the LLM-mediates-on-the-deliberate-side commitment all carry forward from Paper 1 without modification. The within-cell location is new; the governance boundary concept it instantiates is not.

**Claim category (b): Making the governance boundary a variable, explicitly authored substrate content specification is novel relative to Paper 1.** This claim fails because Paper 1 establishes that the boundary is itself governed: orchestration rules governing LLM behavior are human-authored substrate content, and the authority to modify those rules is part of what Paper 1's human-governed commitment names. Paper 2's authored boundary specification is the explicit, per-entity instantiation of this implicit principle. Making the principle explicit and per-entity-variable extends Paper 1's commitment; it does not introduce a new commitment independent of it.

**Claim category (c): Per-entity boundary variability — different cells having different instinct/reasoning boundaries — is novel relative to Paper 1's governance boundary commitment.** This claim fails because Paper 1's authority-not-labor principle commits to human governance as an authority architecture over substrate content and orchestration rules, not as a fixed structural configuration. The multi-shaped governance that Paper 2 Claim 5 names — governance holding different shapes across entities and evolution mechanisms — is the natural extension of Paper 1's authority architecture to the per-entity authored boundary specification. The per-entity variability is enabled by Paper 1's substrate-content commitment; it is not independent of it.

---

## 7. Conclusion

The instinct/reasoning boundary within a CKS cell is a within-cell instantiation of Paper 1's governance boundary concept. It preserves the two-sided architecture, the human-governance-on-both-sides principle, the boundary-as-substrate-content property, and the LLM-mediates-on-the-deliberate-side commitment that Paper 1 establishes at the cell's external perimeter. It adds within-cell location, explicitly authored boundary specification, per-entity variability under multi-shaped governance, and the evolution-target property that follows from the boundary being authored substrate content. C1.25 and C1.04 together establish that Paper 1's governance boundary concept instantiates at two distinct structural locations in Paper 2's architecture — the external perimeter of each structural unit and the internal processing boundary within each cell — and that both instantiations carry the full inheritance load of Paper 1's governance boundary commitments without requiring independent theoretical defense.

---

*End of C1.25 (#454).*
