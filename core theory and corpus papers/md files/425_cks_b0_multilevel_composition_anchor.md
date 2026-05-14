# Multi-Level Composition as Paper 2's Second Architectural Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the architectural commitments introduced in *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance* (Li, April 2026), which extends the Coordination Knowledge Substrate (CKS) pattern from *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to anchor Paper 2's second architectural commitment — the structural-modularity claim — at the level of a single named claim, so that the foundational sub-commitments derived from it in the Series B derivation notes have an explicit parent claim cited as their source.

## Abstract

Paper 2 of the CKS theory series defends six architectural commitments. Its second claim — that a CKS-governed AI Self is architecturally modular by commitment rather than by evolution, at every level of composition — is the structural commitment on which much of the rest of Paper 2 depends. The claim is internally composite: it carries four distinct sub-commitments (three structural levels with distinct governance scopes; level membership as relational functional determination rather than intrinsic type assignment; the DNA/action layer distinction within every cell; expression as governed selection at aspect and Self scope) that the paper defends together as one structural architecture. This note formalizes Claim 2 as a single named architectural commitment, positions it relative to Paper 1's two-level substrate-cell foundation, names the four failure modes the commitment defends against, and maps the foundational sub-commitments (B1.02, B1.03, B1.04, B1.17) and their decompositions as derivations of this parent claim.

## 1. Why this claim needs an anchor

Paper 2 develops six architectural commitments through six claims. The Series B derivation notes decompose those commitments into sub-commitments, operational variants, anti-patterns, composition pairs, operational tests, and boundary cases — but until the Phase B0 anchors, the six claims themselves were not formalized as named architectural commitments at paper-claim level. This left a prior-art gap at the level immediately above the sub-commitments.

Claim 2 is one of the two claims (with Claim 4) where the gap is most consequential. The claim is internally composite — four sub-commitments held together — and the paper develops them as one architecture across §5.2 through §5.4 because each component requires the others to be coherent. This note anchors all four together rather than treating them as independent commitments.

## 2. The claim and its four sub-commitments

In Paper 2, Claim 2 states that a CKS-governed AI Self is architecturally modular *by commitment* rather than *by evolution*, with modularity required at every level of composition rather than treated as an emergent property the architecture must wait for. The claim has four sub-commitments, which the paper develops together and which this note treats as the claim's four components:

1. **Three structural levels with distinct governance scopes.** Cells compose into aspects; aspects compose into Selves. Cell, aspect, and Self are each named architectural levels with distinct governance scopes, purpose statements, and coordination rules.
2. **Relational role membership.** Level is a relational determination made under governance based on the entity's functional role, not an intrinsic type assigned at instantiation and fixed forever. The same underlying CKS artifact can participate as a cell in one arrangement, as part of an aspect in another, or as a component of different aspects simultaneously.
3. **DNA/action layer distinction within every cell.** Two distinguishable substrate layers operate within every cell: the DNA layer carries stabilized orchestration content (the cell's governing architecture); the action layer carries recorded task instances and their outputs (the cell's operating history). Both are substrate content under Paper 1 commitments, with one-way authority running from DNA to action.
4. **Expression as governed selection at aspect and Self scope.** Expression is the mechanism that determines which DNA-layer substrates activate for a given cell goal in a given coordination context. At aspect and Self scope, the higher level's DNA governs which cell-level rules are expressed without modifying the underlying cell DNA. Expression is governed selection by orchestration substrate; it is not implicit, not automatic, and not the same as inheritance or orchestration-rule authoring.

The four sub-commitments compose into one architectural claim because each is required for the others to be coherent. Without three levels, expression has no scope to select rules at. Without relational role membership, the levels become fixed types and the same underlying artifact cannot participate in multiple arrangements. Without DNA/action layering, expression has no substrate content to select over. Without expression, higher-level governance cannot specialize cell behavior without rewriting cell DNA.

## 3. The four sub-commitments in detail

### 3.1 Three structural levels with distinct governance scopes

The cell is the atomic unit from Paper 1 — a CKS artifact with substrates, orchestration rules, and the six architectural commitments Paper 1 defends, all holding at the cell level without modification. An aspect is a coordination arrangement of cells serving a particular purpose, operating over its constituent cells as content domain. The Self is the integrated whole that holds multiple aspects as facets of one CKS-governed intelligence — not a bigger aspect, not a rigid top-of-hierarchy, but the unified composition the multiple aspects compose into.

Each level has a distinct governance scope. Cell-scope governance operates on the cell's own DNA and action content under Paper 1's substrate/LLM division. Aspect-scope governance operates on the orchestration of cells into a purpose-defined arrangement and on the cross-cell coordination rules that arrangement requires. Self-scope governance operates on the composition of aspects into one whole. The same architectural primitives (substrate, orchestration rules, conflict preservation, AI-as-substrate-mediator) hold at each level, but each level applies them to a different scope of coordination content.

### 3.2 Relational role membership

Existing modular-software literature commits to intrinsic structural membership: a service belongs to one bounded context; an aggregate to one service; a component to one composite. Claim 2's commitment is the inverse — the same underlying CKS artifact participates as a cell in one arrangement, as part of an aspect in another, or as a component of different aspects simultaneously, depending on what the structure is for. The artifact's identity is the bearer; the role-instance inheres in the bearer per the structural arrangement that calls on it; governance properties propagate per arrangement rather than per unit.

This is the claim's most consequential novel commitment and the one this anchor formalizes as load-bearing prior art. Level in a CKS-governed Self is *not* an intrinsic type assigned at creation and fixed thereafter. Level is a functional determination made under governance based on what the entity does in the relevant coordination context. Governance can redetermine level as function changes — an artifact functioning as a cell can later be reframed as part of an aspect, or as participating in multiple aspects simultaneously, without changing its identity. The structural arrangement determines role membership at the arrangement; the underlying artifact carries identity across arrangements. The commitment synthesizes three closest-adjacent strands — object-capability systems, formal-ontology work on roles and qua-entities, and agent-community work on roles plus deontic governance — within Paper 1's substrate framework at multi-level composition scope; the novelty is the configuration.

### 3.3 DNA/action layer distinction within every cell

Within every cell, two distinguishable substrate layers operate. The DNA layer carries stabilized orchestration content — harness logic, conflict-handling rules, lifecycle policies, schemas — that defines what the cell is governed to do. The action layer carries recorded task instances and their outputs — what actually happened when the DNA met an actual task — that accumulates as the cell's lived experience. Both layers are substrate content under Paper 1's commitments. What distinguishes them is governance semantics: DNA is human-governed at origin and modification, while action is produced by the cell's operation, with one-way authority — DNA constrains and shapes what action can be, and action does not autonomously rewrite DNA.

The architectural shape — governed policy on one side, operational state on the other, one-way authority from policy to state — is recognized in adjacent industry literatures on agent-memory governance (where "memory is governance, not storage" is the formative articulation). Claim 2's specific commitment is that this distinction holds *within every cell* under Paper 1's substrate framework, with the loop closing action evidence back into DNA refinement being a separate, governed evolution mechanism rather than autonomous rewriting.

### 3.4 Expression as governed selection at aspect and Self scope

Expression is the mechanism that determines which DNA-layer substrates activate for a given cell goal in a given coordination context. Each cell carries a harness substrate — itself human-governed, fully inspectable, modifiable, and overridable — that selects which sub-substrates are active for current activity. Cells can carry the full Self's DNA with selective expression (when lineage and reconstitution matter, as in regulated work) or partial slices (when storage and cognitive load matter more), per a per-deployment design choice governed by orchestration substrate.

At aspect and Self scope, expression takes on its higher-level architectural role. The aspect's DNA governs which cell-level rules are expressed in the coordination context the aspect serves; the Self's DNA governs which aspect-level rules are expressed in the integrated whole. This is the mechanism by which aspect-level and Self-level governance specializes the behavior of member cells without modifying their DNA. The orchestration substrate that performs the selection is itself substrate content under Paper 1 commitments.

Three distinctions are load-bearing. Expression is not orchestration-rule authoring: rules are authored once and may be expressed in many contexts. Expression is not inheritance: an inherited rule still requires governed expression to apply in a given context. Expression is not implicit or automatic: rule application is selected by governed substrate content, not by default activation. The architectural novelty of expression is that it makes rule application scope a first-class object of human governance, separate from rule authorship and rule modification.

## 4. Position relative to Paper 1

Paper 1 establishes two architectural levels: substrate and cell. The substrate is the persistent human-governed coordination artifact; the cell is the atomic unit that executes over substrate content under orchestration rules; the governance boundary holds between them. Paper 2 Claim 2 extends this architecture in three distinct ways.

First, the named structural levels increase from two (substrate, cell) to three (cell, aspect, Self), with each new level applying the same substrate/LLM division Paper 1 commits to at cell scope. The increase is not three new levels on top of substrate-cell; it is the cell-scope architecture Paper 1 defends, now composed into two additional named levels (aspect, Self) above it under unified human governance. Second, layering within the cell is made explicit: Paper 1 treats the cell as one unit operating over substrate content; Paper 2 Claim 2 distinguishes DNA and action as two layers within every cell with distinct governance semantics. Third, expression is introduced as a separate governance mechanism: Paper 1 commits to orchestration rules that govern cell-level behavior but does not commit to a mechanism by which higher-level governance selects which rules apply at which scope, and Paper 2 Claim 2 introduces expression as that mechanism.

The relational-roles commitment is the most novel content in this extension. Paper 1 does not distinguish entity type from functional determination. Paper 2 Claim 2 commits that level is a relational functional determination under governance, not an intrinsic type — and this commitment is entirely new in Paper 2.

## 5. Failure modes the claim defends against

Naming the failure modes makes the claim's content checkable. Claim 2 defends against four:

**Fixed-type architectures.** Architectures in which cell, aspect, and Self are intrinsic types assigned at instantiation and fixed thereafter — an artifact is created as a cell and remains a cell; level membership is not redeterminable under governance. This violates the relational-roles sub-commitment (§3.2) and precludes the same artifact participating in multiple arrangements simultaneously.

**Flat architectures.** Architectures in which all entities are cells with no aspect-level coordination layer and no Self-level integration layer. This violates the three-levels sub-commitment (§3.1) by forcing all coordination content into cell-scope substrates regardless of whether it operates on cells, on coordination arrangements of cells, or on integration of those arrangements.

**Single-layer cells.** Architectures in which a cell carries only one substrate layer — either policy/DNA content or operational/action content but not both as distinct governed objects. This violates the DNA/action sub-commitment (§3.3) and collapses the one-way authority Claim 2 commits to.

**Implicit expression.** Architectures in which rules apply by default whenever they exist, without a governed selection mechanism determining which rules apply at which scope. This violates the expression sub-commitment (§3.4) and makes rule application scope an implicit property of rule existence rather than a first-class object of human governance.

A system that fails any one of the four is not architecturally modular in the Claim 2 sense.

## 6. Mapping to derived sub-commitments

The Series B derivation notes formalize Claim 2's content at sub-commitment granularity. The mapping from this anchor to the derivations is:

**Foundational sub-commitments (Phase B1).** B1.02 formalizes the three structural levels with distinct governance scopes (§3.1). B1.03 formalizes the DNA/action layer distinction within every cell with one-way authority (§3.3). B1.04 formalizes expression as governed selection at aspect and Self scope, including the harness substrate and per-deployment expression configuration (§3.4). B1.17 formalizes relational role membership as functional determination under governance rather than intrinsic type assignment (§3.2).

**Operational decompositions (Phase B2).** Each foundational sub-commitment decomposes into operational variants (B2.11 through B2.30 in the master plan's enumeration), covering per-level governance scopes and recursive applicability of Paper 1 commitments (B1.02 children); layer-specific governance semantics and action-as-substrate-content (B1.03 children); harness substrate, partial-DNA expression, full-DNA-with-selective-expression, and expression-of-expression governance (B1.04 children); multi-arrangement participation, governance-driven level reframing, and bearer-identity preservation (B1.17 children).

**Anti-pattern formalizations (Phase B3).** B3.18 formalizes the Intrinsic Type Assignment anti-pattern — the fixed-type failure mode named in §5. B3.29 formalizes the Cross-Level Confusion anti-pattern — governance content from one level applied at another level without governed expression.

Each derived note cites this anchor as its parent claim.

## 7. Operational test

A system instantiates Claim 2's commitment if and only if all of the following are true:

1. **Three named levels with distinct scopes.** An observer can independently identify three architectural levels — cell, aspect, Self — and name a distinct governance scope, purpose statement, and coordination-rule set for each.

2. **Relational level membership.** Level membership is determinable from the entity's functional role in the relevant coordination arrangement, not from a fixed type assigned at creation. At least one underlying artifact participates in multiple structural arrangements simultaneously without identity change, and governance supports level redetermination as function changes.

3. **DNA/action distinction within every cell.** Every cell carries two distinguishable substrate layers — DNA and action — with distinct governance semantics. An observer can read DNA content separately from action content; modifications to action do not autonomously modify DNA; the loop from action evidence to DNA refinement is governed.

4. **Expression as governed selection at aspect and Self scope.** Aspect-level and Self-level governance specializes member behavior through a governed expression mechanism that selects which lower-level substrates activate in the coordination context, not by modifying the lower-level DNA. The orchestration substrate performing the selection is inspectable and modifiable, and rules do not apply implicitly by default.

A system that fails any of (1) through (4) is not architecturally modular in the Claim 2 sense, regardless of whether it is modular in some other sense.

## 8. Conclusion

Claim 2 of Paper 2 is the structural commitment on which Paper 2's later claims depend. It is internally composite — three structural levels with distinct governance scopes; relational role membership rather than intrinsic type assignment; the DNA/action layer distinction within every cell; expression as governed selection at aspect and Self scope — and the four sub-commitments are defended together because each requires the others to be coherent. The relational-roles commitment is the most consequential novel content and is entirely new in Paper 2: level is a functional determination under governance, not an intrinsic type assignment.

Subsequent work that adopts Paper 2's multi-level composition pattern, extends it, composes it with adjacent patterns, or argues against it should treat the four sub-commitments as the claim's content held together. Subsequent work that treats them as independent commitments, or that omits any one of them, is treating a different claim, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Multi-Level Composition as Paper 2's Second Architectural Claim.* May 14, 2026. ORCID: 0009-0004-8065-3235.
