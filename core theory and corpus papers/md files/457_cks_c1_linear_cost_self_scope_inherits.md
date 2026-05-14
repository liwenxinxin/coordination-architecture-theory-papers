# Linear-Cost at Self Scope Inherits Paper 1's Extension Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** CKS Derivation Notes — Series C (Cross-Derivation), Note C1.28 (#457)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to establish, as named public prior art, that Paper 2's linear-cost commitment at Self scope is an extension of Paper 1's linear-cost extension claim (A0.06), not an independent invention.

## Abstract

Paper 1's sixth architectural commitment (A0.06) establishes a linear-cost extension claim: governance costs, onboarding costs, and execution costs scale linearly with cell count rather than with total system size. Adding the Nth cell costs approximately the same as adding the first cell. Paper 2's enterprise brain Self pattern (Claim 6a, B0.06) requires that this commitment hold not only at cell scope but at every level of a three-tier structural hierarchy: cell, aspect, and Self. This note formalizes that inheritance edge — linear-cost at Self scope ⊃ Paper 1 Claim 6 (A0.06) — names what is preserved from Paper 1 and what is new in Paper 2, distinguishes this structural inheritance from the parallel evolutionary inheritance established in C1.20, and states the three adversarial claims the prior-art position forecloses.

## 1. The inheritance edge stated

The inheritance relationship this note formalizes is:

> **Paper 2 linear-cost at Self scope ⊃ Paper 1 Claim 6 (A0.06)**

Reading left to right: Paper 2's commitment that governance costs remain per-entity proportional across the cell/aspect/Self structural hierarchy *extends* — and does not supersede, contradict, or replace — Paper 1's commitment that governance costs scale linearly with cell count rather than with total system size.

The ⊃ symbol denotes strict extension: Paper 1's linear-cost identity is preserved intact at the cell level within Paper 2. The extension adds a requirement that the identity hold at two additional structural levels — aspect and Self — that Paper 1's single-cell scope did not define.

Paper 2 makes this inheritance explicit. At §9.6, the paper states that "Paper 1 §6's linear-cost composition is the load-bearing inheritance for the wholeness commitment's tractability — composition stays linear in cost as the unit propagates from cells through aspects and Selves to the enterprise brain." The extension is acknowledged, not merely implied.

## 2. What Paper 1's linear-cost claim establishes

Paper 1 Claim 6 (A0.06) makes a cost-model commitment with three sub-claims.

The first sub-claim is about governance cost: adding a cell to a CKS deployment does not require governance practitioners to re-examine or re-govern cells already present. The cost of governing cell N is approximately independent of whether the deployment contains one cell or one thousand. This is not a claim about coordination intelligence growing linearly; it is a claim about the infrastructure of governance not exhibiting the superlinear scaling costs characteristic of parametric memory updates, re-embedding operations, or multi-agent coordination overhead.

The second sub-claim is about onboarding cost: a practitioner reading a cell's substrate content does not need to read the substrate content of other cells to understand how that cell is governed or how it behaves. Cells are governed locally with respect to comprehension. The per-cell onboarding cost is approximately constant.

The third sub-claim, the one exception, is about storage: storage scales linearly with substrate size. Adding a cell adds storage proportional to that cell's content. This scaling is accepted as necessary and distinguished from the governance and onboarding costs that are held constant.

Paper 1 presents this as an *extension claim* within the core theory: a projection of what the modular substrate-cell separation implies at larger scale. The claim is architecturally derived — it follows from the governance boundary's design — rather than independently demonstrated at scale. Paper 1 inherits the empirical base from Knowledge Objects (Zahn & Chana 2026) and extends it with richer governance semantics on two axes. Claim 6's extension framing is what makes it defensible as extension rather than new theory: the same architecture, yielding the same cost profile, as cell count grows.

## 3. What linear-cost at Self scope requires

Paper 2's enterprise brain Self pattern introduces a three-tier structural hierarchy: cells compose into aspects, aspects compose into a Self, and the Self is the unit that constitutes the enterprise brain. This hierarchy creates three structural levels at which the linear-cost commitment must hold independently.

**At cell scope.** Paper 1's linear-cost commitment is inherited without modification. Adding a cell to any aspect costs approximately the same as adding the first cell. Governance cost per cell remains approximately independent of total cell count in the aspect or deployment. This is the foundation; Paper 2 does not weaken it.

**At aspect scope.** Paper 2 requires that adding an aspect to a Self costs approximately the same as adding the first aspect. Governance cost per aspect must remain approximately independent of how many aspects the Self already contains. This requirement does not follow automatically from cell-scope linear-cost: if aspects required governance practitioners to read and integrate all other aspects' DNA content to govern a new one, aspect-level governance would compound even while cell-level governance remained linear. The architecture forecloses this by requiring that Self-level DNA contain the integration architecture at the appropriate abstraction level, not the content of every cell within every aspect.

**At Self scope.** Adding a Self to a deployment costs approximately the same as adding the first Self. Governance cost per Self must remain approximately independent of how many Selves exist in the deployment. This is the outermost requirement, applying to multi-Self configurations that remain within Paper 2's scope.

The three requirements together constitute linear-cost at Self scope: per-entity cost approximately constant at all three structural levels as the number of entities at each level grows.

## 4. The distinction from C1.20

Note C1.20 established a closely related but distinct inheritance edge: **Paper 2 multi-level evolution ⊃ Paper 1 linear-cost (evolutionary dimension)**. That note covered the *evolutionary* application of linear-cost: the three evolution mechanisms (instinct evolution, DNA evolution, action-feedback evolution) operating across the three structural levels do not compound governance costs as cells, aspects, and Selves evolve. The cost of governing an evolution event — a mutation, a directed selection, an action-feedback update — remains approximately proportional to the entity being evolved, not to the total population of entities being evolved alongside it.

C1.28 covers the *structural* application of linear-cost: the costs of *adding* entities to the hierarchy — adding cells to aspects, adding aspects to Selves, adding Selves to a deployment — do not compound governance costs as the structural population grows. The cost of governing a new entity's presence is approximately proportional to that entity alone.

Both notes inherit from Paper 1 Claim 6 (A0.06), but through different channels:

- **C1.20's channel:** linear-cost under change — cost of *evolving* entities at any level
- **C1.28's channel:** linear-cost under growth — cost of *adding* entities at any level

The distinction matters for the prior-art coverage the series provides. An adversarial architecture that preserves evolutionary linear-cost but compounds structural linear-cost — one where adding a new aspect requires re-governance of all existing aspects — would satisfy C1.20's inheritance but not C1.28's. The two notes together close that gap.

## 5. What is preserved from Paper 1

Three elements of Paper 1's linear-cost identity are preserved without modification at Self scope.

**Governance cost per entity approximately constant.** The governance cost of a cell at cell scope, an aspect at aspect scope, and a Self at Self scope is approximately independent of the total number of entities at each respective level. This is the core cost-model commitment, carried upward from cell scope to the full hierarchy.

**Onboarding cost locally bounded.** A governance practitioner reading Self-level DNA does not need to read all aspect-level DNA or all cell-level DNA to understand the integration architecture the Self governs. Per-unit comprehensibility — the property that governance does not require full-substrate reading at the level being governed — extends from cells through aspects to the Self level. The one exception from Paper 1 (full-substrate read scales with substrate size) is preserved as an exception at Self scope as well: a practitioner who needs to read every cell's content across the enterprise brain faces a read cost proportional to the total substrate volume, but this is an optional deep-dive cost, not a mandatory governance cost.

**Storage scales linearly; this is the accepted exception.** Self-level DNA and action-layer records add linearly to storage per entity added, just as cell-level substrate content does at Paper 1's scope. The one scaling exception Paper 1 named is preserved intact.

## 6. What is new in Paper 2

Three elements of Paper 2's linear-cost commitment are genuine additions that Paper 1's single-cell scope did not contain.

**Multi-level cost accounting at Self scope.** Paper 1 performed cost accounting at cell scope: cells are the units, and governance cost per cell is the relevant quantity. Paper 2 extends the cost accounting to three scopes simultaneously. Governance cost must be analyzed per-cell (inherited), per-aspect (new), and per-Self (new). The enterprise brain pattern requires this multi-level accounting because a practitioner governing an aspect must know that doing so does not implicitly require re-governing all cells in other aspects, and a practitioner governing a Self must know that doing so does not implicitly require re-governing all aspects.

**Aspect as an independent cost unit.** Paper 2 introduces the aspect as a structural unit between cell and Self, and requires that the linear-cost commitment hold *at the aspect level* as a cost unit in its own right. An aspect is not merely a named collection of cells for organizational purposes; it is an entity with its own DNA and action layers, its own governance surface, and its own per-unit governance cost. This aspect-as-cost-unit framing is new. Paper 1 had no intermediate level between the cell and the deployment, and therefore had no requirement to establish that the intermediate level's governance cost was linear in aspect count.

**Enterprise viability as an explicit conditional argument.** Paper 2 explicitly connects linear-cost at Self scope to the *viability* of the enterprise brain pattern at enterprise scale. The argument structure is: enterprise brain pattern is viable at enterprise scope *if and only if* governance costs do not compound as cell count, aspect count, and Self count grow; linear-cost at Self scope is the architectural commitment that makes the enterprise brain tractable rather than prohibitively expensive to govern. This explicit conditional — the architecture is designed for enterprise scale precisely because governance costs remain per-entity proportional — strengthens the prior-art position because the paper itself binds the structural architecture to the cost property. An adversarial claim that enterprise-scale AI governance architectures face compounding costs cannot avoid Paper 2's explicit commitment to the contrary.

## 7. Operational test

For a Self with M aspects and N total cells distributed across those aspects, three independent test conditions verify linear-cost at Self scope.

**Test condition 1 — Per-aspect governance cost as M grows.** Double the number of aspects from M to 2M by adding M new aspects to the Self. Measure the governance cost per aspect before and after. If the cost per aspect remains approximately constant — neither doubling nor growing super-linearly with aspect count — the linear-cost commitment holds at aspect scope for this deployment. The test is independent of N: adding aspects without changing cell count should not affect per-aspect governance cost.

**Test condition 2 — Per-cell governance cost as N grows.** Double the number of cells from N to 2N by adding N new cells distributed across the aspects. Measure governance cost per cell before and after. If the cost per cell remains approximately constant, the linear-cost commitment holds at cell scope for this deployment, inheriting Paper 1's requirement. The test is independent of M: adding cells without changing aspect count should not affect per-cell governance cost.

**Test condition 3 — Per-Self governance cost as Self count grows.** Add a second Self to the deployment (where Paper 2's scope permits multi-Self configurations). Measure governance cost per Self. If the cost per Self is approximately the same as for the first Self, the linear-cost commitment holds at Self scope. This test is independent of M and N: adding a new Self should not require re-governance of the existing Self's aspects or cells.

A deployment satisfies linear-cost at Self scope if all three test conditions are met independently. Failure on condition 1 alone — where per-aspect cost compounds but per-cell cost remains constant — represents an aspect-scope violation of the inherited commitment. That violation pattern is what the enterprise brain architecture's structural design must preclude: Self-level DNA containing the integration architecture at appropriate abstraction, aspect-level DNA governing aspect-local behavior without requiring cross-aspect reads, and cell-level DNA remaining locally scoped.

## 8. Prior-art significance

Three adversarial claims are foreclosed by the inheritance edge this note formalizes.

**Adversarial claim (a): Enterprise-scale AI governance architectures with integration layers can be governed without compounding costs — and this is a novel finding not present in prior art.** Paper 2's explicit commitment that the enterprise brain Self remains governable at enterprise scale because governance costs are per-entity proportional, combined with Paper 1's foundational cell-scope linear-cost commitment, establishes this property as prior art in the CKS theory series. Any patent or claim asserting novelty of non-compounding governance cost in multi-level AI architectures with an integration coordination layer must contend with this publication chain.

**Adversarial claim (b): The three-level hierarchy (cell/aspect/Self) necessarily requires super-linear governance cost relative to flat architectures.** Paper 2 commits explicitly to the contrary: adding an intermediate level (aspect) between cell and Self does not create multiplicative governance overhead. The aspect level governs locally, the Self level governs the integration architecture at the appropriate abstraction, and per-entity cost remains approximately constant at each level independently. An adversarial claim that three-level governance is inherently more expensive than one-level governance in proportion to the number of levels cannot be novel relative to Paper 2.

**Adversarial claim (c): Adding coordination layers between cells and the integration unit creates multiplicative governance overhead.** The aspect is precisely a coordination layer between cells and the Self (integration unit), and Paper 2's linear-cost commitment at Self scope explicitly asserts that this layer does not create multiplicative overhead. The prior-art position is that aspects can be added, governed, and scaled without compounding the governance cost of existing aspects or cells. An adversarial claim asserting that coordination intermediation layers are architecturally novel in preserving linear governance cost must contend with this paper's explicit commitment to the same property.

## 9. Summary

Paper 2's linear-cost at Self scope extends Paper 1 Claim 6 (A0.06) through a structural channel. Paper 1 established that governance costs scale linearly with cell count; Paper 2 extends that commitment to all three structural levels of the cell/aspect/Self hierarchy. The extension is genuine: Paper 2 introduces the aspect as an independent cost unit, performs multi-level cost accounting at cell/aspect/Self scope simultaneously, and explicitly frames the enterprise brain pattern's viability as conditional on linear-cost holding at all three levels. Paper 1's linear-cost identity — per-entity governance cost approximately constant, per-unit onboarding cost locally bounded, storage as the accepted scaling exception — is preserved intact at each level. The operational test at §7 provides three independent conditions for verifying the commitment in a live deployment. The prior-art significance at §8 forecloses three adversarial claims about compounding governance cost in multi-level AI governance architectures.

---

*Note C1.28 in the CKS Derivation Note Series (Series C: Paper 1 ↔ Paper 2 Cross-Derivation). Preceding note: C1.27 — Paper 2 substrate-shared topology ⊃ Paper 1 substrate as primary artifact. Following notes: C1.29 — Paper 2 distributed failure risk ⊃ Paper 1 substrate-cell boundary; C1.30 — Paper 2 structural co-adaptation ⊃ Paper 1 tool-agnosticism + non-specialist governance.*
