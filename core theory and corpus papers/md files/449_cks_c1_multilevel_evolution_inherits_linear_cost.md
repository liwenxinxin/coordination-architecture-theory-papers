# Multi-Level Evolution Preserves Paper 1's Linear-Cost Commitment

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to show that the multi-level evolution architecture Paper 2 introduces preserves, rather than disrupts, the linear-cost commitment Paper 1 establishes — and to make that preservation precise enough that downstream work can verify it independently.

## Abstract

Paper 1 of the CKS series commits to linear-cost composition: governance costs, onboarding costs, and execution costs scale linearly with entity count rather than with total system size, making CKS viable at enterprise scale without governance becoming a bottleneck as deployments grow. Paper 2 introduces evolution across three structural levels — cell, aspect, and Self — with mutation, directed selection, and action-feedback mechanisms operating at each level, and with vertical evolution propagating improvements upward and horizontal evolution propagating improvements across peers. This note establishes the inheritance edge: Paper 2's multi-level evolution architecture inherits and preserves Paper 1's linear-cost commitment across all three levels. The note shows what is preserved identically (governance cost per entity, onboarding cost, execution cost, storage), what is genuinely new in Paper 2 (multi-level cost accounting, vertical evolution cost structure, aspect- and Self-level governance as separately counted cost units), and explicitly forecloses the adversarial reading that three structural levels necessarily compound governance costs relative to a single-level architecture. An operational test for the inherited property closes the note.

## 1. The two sides of the inheritance edge

### Paper 1's linear-cost commitment (the inherited side)

Paper 1 Claim 6 (A0.06) commits to linear-cost composition along three independent cost dimensions. Governance cost per cell is not size-proportional: a human governing a single cell's directed-selection event does not need to also review the rest of the substrate. Onboarding cost for new readers is not size-proportional: a reviewer joining a CKS deployment reads the content relevant to their role, not the full substrate. Execution cost per cell is task-scope-proportional, not total-system-proportional: a cell reads and writes the substrate content within its task scope, so adding unrelated cells elsewhere in the deployment does not increase any given cell's execution cost. Storage is the one cost that does scale with system size — it grows linearly with content volume, which is the trivial property any persistent representation has.

The asymmetry between storage (size-proportional) and everything else (not size-proportional) is the substantive content of Paper 1's linear-cost claim. It is what makes bottom-up adoption defensible: an organization that starts with a single cell and grows incrementally does not encounter an infrastructure cliff at any point, because governance cost, execution cost, and onboarding cost do not compound as the deployment grows.

### Paper 2's multi-level evolution architecture (the extending side)

Paper 2 introduces three structural levels — cell, aspect, and Self — and commits that the same three evolution mechanisms (instinct evolution, DNA evolution, action-feedback evolution) operate at each level. Cells are the atomic coordination units. Aspects are governed collections of cells with a shared functional scope. A Self is the top-level entity composed of aspects and constituting the enterprise coordination architecture.

Paper 2 also distinguishes two axes of evolution. Horizontal evolution refines content within existing structure: cells refine their DNA, aspects refine their cell composition, Selves refine their aspect arrangement. Vertical evolution reorganizes structure itself: cells can be reassigned across aspects, aspects can split or merge, Selves can gain or lose aspects. Both axes operate at every level through the three mechanisms.

The extension question this note addresses is: does adding two structural levels above the cell — aspect and Self — compound governance costs relative to Paper 1's single-level architecture? The answer is no, and the argument is the content of §§2–4.

## 2. What is preserved: linear-cost identity at each cost dimension

### Governance cost per entity

In Paper 1, governing one directed-selection event at cell scope costs approximately the cost of authoring or approving one orchestration rule change, or of exercising one direct override — the two moments at which Paper 1 locates governance. The level label (cell, aspect, Self) does not change the structure of this cost. Governing one directed-selection event at aspect scope means a human authorizing a change to the aspect's DNA content — the orchestration substrate defining which cells participate in the aspect, under what rules, with what composition. The structure of the governance act is the same: one authorization over one bounded scope of substrate content. It is not the sum of authorizing every cell within the aspect individually.

The cost identity holds because Paper 2 inherits Paper 1's authority-not-labor commitment. Governance in the CKS sense is the right to inspect, modify, and override — not the obligation to review every element. An aspect-level governance event is one event at aspect scope. It does not require reading all cell-level content first. It does not trigger a review cascade over all cells in the aspect. The scope of the governance act is the aspect's own substrate content; what lives inside the aspect at cell scope is separately governed, separately counted, and independently readable.

### Onboarding cost

Paper 1 commits that onboarding cost for a new reader is not size-proportional. A governance practitioner joining an existing CKS deployment reads what their role requires, not the full substrate.

Paper 2 preserves this. A practitioner whose governance scope is aspect-level DNA content reads the aspect's orchestration substrate. They do not need to first read all cell-level DNA within the aspect. A practitioner whose scope is Self-level architecture reads the Self's aspect composition substrates. They do not need to first read every aspect's cell composition, or every cell's task-level DNA. Each level is independently readable because each level's content is separately stored substrate content with its own scope boundary.

The three-level architecture adds depth to the content hierarchy without adding a mandatory vertical read requirement. Readability at any level is independent of what lives below or above that level — this is the structural feature that makes onboarding cost at aspect scope approximately equal to onboarding cost at cell scope, holding the Paper 1 commitment at each new level Paper 2 introduces.

### Execution cost

Paper 1 commits that cell execution cost is task-scope-proportional, not total-system-proportional. A cell executes over the substrate content within its task scope. Adding other cells elsewhere in the deployment does not affect any given cell's execution cost.

Paper 2 preserves this. Aspect-level governance events — governed changes to the aspect's orchestration substrate — do not add execution overhead to all cells within the aspect. A cell continues to execute over its task-scoped substrate content. The aspect-level layer and the Self-level layer are separate substrate scopes. Operations at those scopes affect those scopes' content; they do not cause cells to execute over larger inputs. Adding more aspects or more Selves to a deployment does not increase any given cell's execution cost.

### Storage

Paper 1 identifies storage as the one cost that does scale linearly with system size. Paper 2 inherits this: adding multi-level evolution records — aspect lineage chains, Self DNA version history, vertical evolution propagation records — adds storage proportional to the number of such records. This is the same trivial linear-cost property at larger scope. It is not a new cost structure; it is the same cost structure applied to a larger total entity count.

## 3. What is new in Paper 2: the multi-level extensions

### Multi-level cost accounting

Paper 1 had one governance scope: cell. Paper 2 has three: cell, aspect, Self. The linear-cost commitment must now be verified at each level independently. This verification obligation is new.

"Proving linear-cost at aspect scope" means concretely showing three things. First, that governing one aspect-level directed-selection event does not require reading all constituent cell DNA first — the governance act is bounded at aspect scope. Second, that onboarding a new governance practitioner to aspect-level content does not require first reading all cell-level content — each level is independently readable. Third, that aspect-level execution (governed changes to aspect orchestration substrates) does not add per-cell overhead to all cells within the aspect — the execution boundary holds at the level of the event.

The same three-part verification applies at Self scope: one Self-level event does not require reading all aspect-level content; onboarding to Self-level content does not require reading all aspect-level or cell-level content; Self-level changes do not add per-aspect or per-cell execution overhead. The form of the proof obligation is inherited from Paper 1; the number of levels to which it applies is new.

### Vertical evolution cost structure

Paper 2 introduces vertical evolution — the propagation of improvements from cell scope upward to aspect or Self architecture. This is new machinery that Paper 1 has no equivalent for, and it requires a cost characterization Paper 1 did not need to provide.

The cost structure of a vertical evolution event is: one directed-selection event at cell scope (the originating improvement), followed by one governance determination at aspect scope (whether the improvement warrants aspect-level propagation), followed optionally by one governance determination at Self scope (whether aspect-level propagation warrants Self-level update). Each step in this chain is one governance event at its level. The chain costs approximately the number of levels it touches in single-level governance events — it does not compound multiplicatively. A vertical evolution event touching cell, aspect, and Self costs approximately three single-level governance events, not the product of those levels.

This cost structure holds because each step is a separate, discretely governed authorization at its level's scope, not an automatic cascade or a review-all-members obligation at each level passed through.

### Aspect-level and Self-level governance as separately counted cost units

Paper 1 counted governance events at cell scope. Paper 2 adds two new classes of governance event — aspect-level events and Self-level events — and commits that these are independently counted units, not multiplicative overhead applied to all their member entities.

An aspect-level directed-selection event is counted as one governance event. It is not counted as one event per cell in the aspect, and it does not trigger a re-governance pass over the aspect's member cells. A Self-level event is counted as one governance event. It is not counted as one event per aspect in the Self, and it does not trigger aspect-level or cell-level re-governance.

This independence of counting is what makes the linear-cost property hold at enterprise scale: as the number of cells, aspects, and Selves grows, total governance cost grows approximately linearly with total event count rather than with the product of entity counts across levels.

## 4. Foreclosing the adversarial reading

The most direct challenge to the inheritance claim in this note is the following: Paper 2's three-level architecture means every improvement requires governance at three levels — cell, aspect, and Self — so governance costs triple relative to Paper 1's single-level architecture. This reading is incorrect for a reason that is architectural rather than empirical.

Vertical evolution is optional. Most directed-selection events in a Paper 2 deployment occur at cell scope only. A cell's orchestration substrate is updated; the improvement is local to that cell; no propagation to aspect or Self scope is warranted or triggered. The improvement costs one governance event, exactly as in Paper 1. Vertical propagation to aspect scope occurs when a human governance determination concludes that the improvement is relevant to the aspect's orchestration structure — for example, that a workflow pattern refined in one cell should be adopted by the aspect's coordination rules. That determination is itself a governance event at aspect scope. It is not an automatic overhead. It is a decision, made when the facts warrant it, that the improvement merits wider structural expression.

The optionality is the load-bearing feature. Three-level architecture does not mean three-level governance for every event; it means governance events can occur at three scopes, each independently, each only when warranted. The architecture provides the capacity for vertical propagation without imposing it as overhead. An architecture that automatically propagated every cell-level event to all parent levels would compound costs multiplicatively and would fail the linear-cost commitment. Paper 2's architecture does not do this; governance determination gates every propagation step.

The same logic applies to horizontal evolution. Propagating an improvement from one cell across peer cells within an aspect requires a governance determination that the peer adoption is warranted. It is not automatic. The cost is proportional to the number of cells that adopt the improvement, each counted as a separate governance event at that cell's scope, not as a single governance event that multiplies across all peers.

## 5. Prior-art significance

This note forecloses three categories of adversarial claim.

The first is that multi-level governance architectures necessarily compound governance costs relative to single-level architectures. The CKS three-level architecture contradicts this: the same per-entity cost structure that holds at cell scope holds at aspect and Self scope, because the governance act at each level is bounded to that level's scope and does not cascade to member entities automatically.

The second is that three-level evolution — with mutation, directed selection, and action-feedback operating at cell, aspect, and Self — introduces cost structures that are novel relative to Paper 1's linear-cost commitment and therefore not covered by it. The structures are novel in that Paper 1 did not describe them, but the cost properties they exhibit are inherited rather than novel: the same authority-not-labor architecture that makes cell-level governance linear-cost makes aspect-level and Self-level governance linear-cost, because the governance act in each case is an authority exercise at a bounded scope, not a labor obligation over all members.

The third is that vertical evolution across levels necessarily creates multiplicative governance overhead. The optionality argument in §4 forecloses this: vertical propagation is a governance determination, not an automatic mechanical consequence of the three-level structure. Systems that implement three-level evolution with automatic propagation at every level would compound costs; CKS with its governed-determination model does not.

## 6. Operational test

The following test verifies that a given Paper 2 deployment preserves Paper 1's linear-cost commitment across all three levels.

Consider a deployment with N cells organized into M aspects under one Self. The test asks whether governance cost per entity remains approximately constant as N increases, as M increases, and as the number of Selves increases — independently verifying the linear-cost property at each level.

**Cell-scope test (N increases).** Add cells to an existing aspect. Verify that (a) governance cost per cell does not increase as N grows; (b) onboarding a new governance practitioner for one cell's content does not require reading other cells' content; (c) adding a cell does not increase execution cost for existing cells whose task scope does not intersect the new cell's scope. A deployment that passes this test satisfies the Paper 1 linear-cost commitment at cell scope.

**Aspect-scope test (M increases).** Add aspects under the existing Self. Verify that (a) governance cost per aspect does not increase as M grows — a new aspect-level directed-selection event costs approximately the same as the first aspect-level event; (b) onboarding a new governance practitioner for one aspect's content does not require reading other aspects' content; (c) adding an aspect does not increase execution cost for cells in existing aspects whose task scope does not intersect the new aspect. A deployment that passes this test satisfies the linear-cost commitment at aspect scope.

**Self-scope test (number of Selves increases).** Add Selves. Verify that (a) governance cost per Self does not increase as the number of Selves grows; (b) onboarding a new governance practitioner for one Self's architecture does not require reading other Selves' architecture; (c) adding a Self does not increase execution cost for aspects or cells within existing Selves. A deployment that passes this test satisfies the linear-cost commitment at Self scope.

**Vertical evolution test.** For a given vertical evolution event — a cell-level improvement propagated to aspect scope — verify that (a) the total cost of the event is approximately the sum of one cell-scope governance event plus one aspect-scope governance event; (b) the aspect-scope governance event does not require re-governing all cells in the aspect; (c) if Self-scope propagation is not determined to be warranted, no Self-scope governance event is incurred. A deployment in which vertical evolution events consistently cost the sum of the levels they touch, rather than a multiple of the total entity count below those levels, passes the vertical evolution cost test.

**Failure modes to look for.** Governance procedures that require per-member review at each level when an event at the parent level occurs violate the cell-scope and aspect-scope tests. Onboarding procedures that require reading all child-scope content before operating at parent scope violate the onboarding test. Vertical evolution implementations that automatically propagate every cell-level event to parent scopes without a governance determination violate the vertical evolution test. Any of these failures constitutes a departure from the inherited linear-cost commitment, even if the system otherwise inherits CKS architecture at the schema or substrate level.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Paper 1). April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *CKS Selves: Multi-Level Composition, Lifecycle, and Governed Evolution in the Coordination Knowledge Substrate* (Paper 2). April 2026. ORCID: 0009-0004-8065-3235.

## Companion derivation notes

Li, W. (2026). *Linear-Cost Scaling: What Grows Linearly in CKS, What Doesn't, and Why.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Multi-Level Evolution Preserves Paper 1's Linear-Cost Commitment.* May 14, 2026. ORCID: 0009-0004-8065-3235.
