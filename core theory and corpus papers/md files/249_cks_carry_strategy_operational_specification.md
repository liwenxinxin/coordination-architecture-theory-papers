# Carry-Strategy Operational Specification: The Per-Deployment Design Choice Between Full Self DNA with Selective Expression and Partial Slice in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the **carry-strategy** — the per-deployment design choice by which each cell determines what DNA-layer content it holds — as a standalone operational specification, separable from but composing with the harness substrate's selection logic (B2.30) and the activation patterns that operate over it (B2.31).

## Abstract

Paper 2 introduces the expression mechanism (B1.07) by which DNA-layer content activates for a given cell goal, and notes that cells "can carry the full Self's DNA with selective expression... or partial slices" depending on deployment characteristics. The phrase carries more architectural weight than its compactness suggests: it names a per-deployment design choice — about *what each cell carries*, not only *what activates* — that operates at a layer below the harness substrate's selection logic and above the DNA layer's content. Naming this layer precisely allows downstream deployments to reason about the choice deliberately: as a governable architectural commitment, recorded as substrate-resident authoritative content per A2.46, authored per A2.04, configured at cell birth per B1.09, and evolvable through directed selection per B1.14. This note formalizes the carry-strategy as such a standalone specification: it states the two principal strategies — full Self DNA with selective expression and partial slice — names the hybrid composition that combines them, identifies trade-offs, locates the choice in the inherited Paper 1 commitments, and gives an operational test. The note is the third of five decomposing B1.07, following B2.30 and B2.31.

## 1. Why carry-strategy needs to be formalized as standalone

Paper 2's expression mechanism (B1.07) names two layers operating together: a harness substrate per cell that selects which DNA-layer content is active for current activity (formalized in B2.30), and the activation patterns that the harness applies across that content (formalized in B2.31). A third architectural choice sits beneath both and is easy to leave implicit: *what DNA content does each cell hold in the first place.* The harness can only select among what the cell carries, and the activation patterns can only operate over what the harness has visibility into. The carrying is logically prior, and the choice about what to carry is a deployment-design decision with operational consequences that B2.30 and B2.31 do not exhaust.

In conventional AI architectures the question rarely surfaces explicitly. Components hold whatever knowledge or rule content they were built with; the boundary is set implicitly by implementation packaging. When the question does surface — as in retrieval-augmented systems where "what does this agent see" is a runtime decision over an external corpus — it is treated as an indexing or retrieval-policy concern, not as an architectural commitment about the component itself. Paper 2's expression mechanism makes the choice architecturally visible, and the source paper's phrase about a per-deployment design choice governed by orchestration substrate is a direct invitation to treat it as such.

The remedy is to name the carry-strategy as a standalone operational specification. A deployment that has decided which strategy each cell type uses, recorded that decision as substrate-resident content, and configured cells accordingly at birth has made an architectural commitment with downstream consequences for governance, modularity, evolution, and cost. Naming this commitment explicitly is what makes those consequences traceable, and what places the carrying decision on the same architectural footing as the selecting decision (B2.30) and the activation decision (B2.31).

## 2. The carry-strategy, defined precisely

In the CKS pattern, the **carry-strategy** for a cell is the architectural specification of what DNA-layer content the cell holds, distinct from the architectural specification of what the cell's harness selects to activate at any given moment. Two principal strategies are named in Paper 2; a third strategy class composes them.

**Full Self DNA with selective expression.** The cell carries the full DNA-layer content of the Self to which it belongs. The harness substrate (B2.30) determines which subset of that content is active for any given task; the activation patterns (B2.31) operate over the full carried set. The strategy is the direct architectural analog of biological cells carrying the full genome and expressing tissue-specific subsets — Paper 2 names this analog and goes on to make the carry/express distinction architecturally explicit in a way biology cannot, because biology has no delivery mechanism for partial genomes.

**Partial slice.** The cell carries only the DNA-layer content relevant to its specific informational task. The harness substrate operates over a smaller carried set, with simpler selection logic because the slice is already scoped. The strategy resembles engineering-analog modular components, where each component holds only the rules and schemas its narrow purpose requires.

**Hybrid carry-strategies.** A deployment is not architecturally constrained to apply a single strategy uniformly. Cells of one type may use full carry while cells of another type use partial slice, with the choice recorded per cell type rather than per deployment. The composing rule is "one strategy per cell or cell type, recorded as substrate-resident specification," not "one strategy per Self." Hybrid strategies are operationally legitimate; they are not a deviation from the architectural commitment but an instance of it.

The strategy choice has four further architectural properties. It is **substrate-resident** — the strategy applied to a given cell is itself substrate content of the kind named in A2.46, not held in LLM weights or implicit in runtime. It is **authored** — chosen by humans through orchestration-rule authoring per A2.04, with authoring labor allocable across humans and LLMs under human direction but authority remaining human. It is **configured at cell birth** — a required field in the birth specification per B1.09, materialized at instantiation rather than deferred. It is **evolvable** — directed selection per B1.14 is the mechanism for migrating cells from one strategy to another; vertical evolution per B1.16 is the mechanism for revising the strategy distribution at deployment scale.

## 3. What makes carry-strategy architecturally distinctive

Conventional AI architectures often treat the question of what knowledge or rule content a component holds as an implicit packaging decision — the component has the content it was built with, and the boundary is set by where the implementer drew the package boundary. Adjacent design objects sometimes make some version of the question explicit, but typically as a retrieval-policy or indexing concern at runtime, not as an architectural commitment about the component itself.

The CKS treatment differs in three respects. First, **the choice is explicit**: carry-strategy is a named architectural property; a deployment can answer "what carry-strategy do my cells use?" by reading substrate content. Second, **the choice is governable**: because the strategy is substrate-resident authoritative content per A2.46 and authored per A2.04, it is subject to the three rights — inspect, modify, override — that the human-governed commitment names. Third, **the choice supports both biological-analog and engineering-analog modeling**: deployments inclined toward biological framing adopt full Self DNA; those inclined toward engineering-analog modular components adopt partial slice; those finding both useful adopt hybrid strategies. The architectural support is for the choice itself, not for one framing of it.

These three properties together are what makes "we use full carry for cells of type X and partial slice for cells of type Y" a complete architectural statement under CKS, rather than a fragment that needs further unpacking to be operationally meaningful.

## 4. The biological analog and where CKS offers a choice

Paper 2 explicitly engages biology as conceptual scaffold. The full-Self-DNA strategy parallels the biological case directly: each cell of a multicellular organism carries the full genome, and tissue differentiation operates by selective expression rather than by selective carrying. The harness substrate is the architectural analog of the regulatory machinery that drives expression; the activation patterns are the architectural analog of how that machinery's outputs vary with cellular context.

The partial-slice strategy is where CKS exceeds the biological analog. Biology forces full carrying as a structural constraint because no delivery mechanism for partial genomes exists. CKS has no equivalent constraint — content can be apportioned per cell at birth because the substrate is structured artifact. The architectural choice between strategies is therefore a degree of freedom CKS holds that biology does not, as Paper 2 names explicitly.

The analog functions as conceptual scaffold rather than architectural import. The architectural substance is the governable carry-strategy choice; biological framing and engineering-analog framing of partial-slice cells as bounded modular components are alternative communication framings. Neither is privileged; the architectural commitment is the choice itself.

## 5. Inherited Paper 1 commitments

The carry-strategy specification operates within commitments inherited from Paper 1 and reinforced in Paper 2. **A1.05 tool-agnosticism** holds: the strategy is a substrate-content specification realizable in any host environment meeting the three minimal requirements — persistent structured state, human read/write access, LLM access to substrate content. **A1.06 linear-cost scaling** holds: full carry imposes higher per-cell storage and richer harness rules, partial slice imposes the inverse, but both are bounded by deployment-level design parameters rather than by substrate-content size in a way that would violate the cost contract. **A1.13 composition requirements** are satisfied by both strategies; a multi-substrate composition can include cells with full carry and cells with partial slice within the same composed system without special accommodation. **A1.16 hybrid composition** holds: both strategies operate with the three hybrid composition patterns. **A2.04 rule authoring** is the layer at which the strategy is chosen. **A2.46 Category 4** is the kind of authoritative content the strategy in force constitutes. **A2.40 provenance** applies to strategy choices and migrations as it applies to any other substrate-resident decision.

## 6. Operational implications

Naming the carry-strategy as standalone has six consequences. **Configuration is per cell type at design time** — the deployment chooses which cell types use which strategies and records the choice as substrate content. **Configuration is materialized at cell birth** per B1.09 as a required field; cells are not born without a strategy. **Evolution proceeds through directed selection** per B1.14, with provenance recorded per A1.07 and A2.40, as a deployment's understanding of cell purposes matures. **Vertical evolution may revise strategy distribution at scale** per B1.16. **High-stakes deployments may favor full carry** — where lineage and reconstitution matter, full Self DNA supports richer context-aware expression of pinning rules and finer-grained traceability. **Cross-partner strategy follows authority distribution** per A2.47 — each authority partition carries its own strategy choice, and cells with different strategies coexist within the same Self under unified governance.

These implications follow from treating the carry-strategy as having independent operational content.

## 7. What the carry-strategy is NOT

Treating the carry-strategy as a standalone specification can drift into something stronger than the source paper supports if the limits are not stated.

**Not a prescription of implementation.** Tool-agnosticism per A1.05 holds; the strategy specifies what content the cell carries at the substrate level, not how that content is physically stored, indexed, retrieved, or replicated.

**Not a substitute for the harness substrate.** Both strategies are realized through a harness substrate per B2.30. Partial-slice cells still have a harness — it operates over a smaller carried set with simpler rules, but it is not absent.

**Not a modification of the DNA layer's content.** DNA content per B2.25 is *what* the cell carries; carry-strategy is *how much*. The strategy does not alter the content that exists in the Self's DNA layer at large.

**Not static.** The strategy is evolvable through directed selection per B1.14 and vertical evolution per B1.16; treating it as immutable is more rigid than the architecture requires.

**Not preventing multi-aspect cell participation.** A cell that participates in multiple aspects per B1.17 may use either strategy; full-carry cells reassign with full DNA available, while partial-slice cells may need slice adjustments through directed selection at reassignment time.

**Not bypassing governance.** The strategy choice is itself a governable decision; the three rights apply to it as they apply to any other substrate-resident authoritative content.

**Not exhaustive.** Additional strategies may be authored as deployments' needs require; the architecture does not constrain the set to two.

**Not eliminating cell-level governance.** Choosing a carry-strategy does not preempt subsequent governance of the cell's behavior, its DNA content, or its activation patterns.

## 8. Operational test

A deployment has made its carry-strategy explicit in the CKS sense if and only if all of the following are true at all times during the substrate's existence.

1. For each cell or cell type in the deployment, the carry-strategy in force is recorded as substrate-resident content readable through the inspect right within authorized scope.
2. The recorded strategy is one of: full Self DNA with selective expression, partial slice, or a named hybrid composing them.
3. The cell birth specification per B1.09 includes the strategy as a materialized field; cells are not born without a strategy.
4. The strategy is authored by humans or by LLMs operating under human direction per A2.04, and the authoring is subject to the three rights (inspect, modify, override).
5. Strategy migrations are exercised through directed selection per B1.14, with provenance recorded per A1.07 and A2.40.
6. Where cells of different strategies coexist within the same Self, the boundary is described by substrate-resident specification, not by implementation accident.

A deployment that fails any of (1)–(6) has not made its carry-strategy architecturally explicit, even if it has chosen a strategy in some operational sense, and downstream work that relies on its expression mechanism's properties should be scoped accordingly.

## 9. Why naming as standalone matters

The expression mechanism (B1.07) is being decomposed across this Phase B2 sequence into five operational specifications: B2.30 (harness substrate) names what the cell uses to select active content; B2.31 (activation patterns) names how the harness selects; this note names what the harness has to select among in the first place; B2.33 (expression evolution) and B2.34 (inheritance verification) close the decomposition.

The third position in this sequence is load-bearing in a specific way. Without it, the harness specification and the activation-patterns specification together describe what happens with content the cell already has, but leave the question of what content the cell has at all to implicit choice. Naming the carry-strategy as standalone is what makes the expression mechanism architecturally complete on the *carrying* axis as well as on the *selecting* and *activating* axes.

Subsequent work that adopts the CKS expression mechanism, extends it, composes it with adjacent patterns, or argues against it should use "carry-strategy" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Carry-Strategy Operational Specification: The Per-Deployment Design Choice Between Full Self DNA with Selective Expression and Partial Slice in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
