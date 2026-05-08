# Recursive Paper 1 Commitments at Every Structural Level: A Foundational Architectural Commitment for the Coordination Knowledge Substrate Pattern's Self Architecture

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the architectural recursion by which Paper 1's complete architectural specification holds at every structural level of Paper 2's three-level Self architecture, so that downstream work can derive from, extend, or argue against the recursion claim without ambiguity. This note closes Phase B1 of the Series B derivation effort.

## Abstract

Paper 2 of the CKS theory series introduces a three-level structural architecture — cell, aspect, Self — over which lifecycle operations, evolution mechanisms, and governance commitments operate. Paper 2 also commits, explicitly and load-bearingly, that all Paper 1 architectural commitments hold at every level of that architecture. This note formalizes that recursion claim as Paper 2's twentieth and closing foundational architectural commitment. The recursion is precisely scoped: Paper 1's sixteen foundational commitments — formalized in Series A as A1.01 through A1.16 — hold at the cell level, at the aspect level, and at the Self level, with each commitment retaining its content unchanged but operating at the scope appropriate to the level. Architectural recursion is what is being asserted; implementation flatness is not. Each level retains a level-distinct scope, operational character, and verification semantics; the recursion is a property of the commitments themselves, not of the levels' operational machinery. The recursion is what makes Paper 2 architecturally coherent with Paper 1: without it, Series A's complete derivation chain would not extend to higher levels; with it, Series A's foundational commitments, operational decompositions, anti-pattern formalizations, composition pairs, operational tests, and boundary cases all apply at every level of Paper 2's Self architecture, while Paper 2's distinctive primitives operate alongside the inherited Paper 1 commitments rather than displacing them.

## 1. Why the recursion needs to be formalized as standalone foundational commitment

Paper 2's *Continuity with Paper 1* section commits, in one sentence, that all Paper 1 architectural commitments hold at every level of the three-level structure. The commitment is structurally crucial. It is also easy to read past as a transition between paper sections rather than as the load-bearing architectural property it is.

Three architectural consequences turn on the recursion. First, it is what makes Paper 2 coherent with Paper 1: if Paper 1's commitments held at the cell level only, Paper 2's higher levels would be a different architecture under the same name, and Series A's defensive derivation chain would not extend to them. Second, it is what makes Series A's complete derivation chain operational at every level of Series B's deployments — Series A's foundational commitments, operational decompositions, anti-pattern formalizations, composition pairs, operational tests, and boundary cases were each derived at cell scope; the recursion is what makes them apply at aspect and Self scope without re-derivation. Third, it is what allows Paper 2 to commit to its distinctive primitives — instinct/reasoning separation, DNA/action layers, expression, lifecycle, evolution mechanisms — without redefending Paper 1's foundation. Paper 2 adds to Paper 1's foundation rather than restating it.

The closure positioning matters: B1.20 is the twentieth and final note of Phase B1, after the structural-properties cluster (B1.17–B1.19), the bidirectional-evolution note (B1.16), the evolution-mechanisms cluster (B1.12–B1.15), the lifecycle cluster (B1.09–B1.11), the modularity cluster (B1.06–B1.08), the level-elaborations cluster (B1.03–B1.05), and the foundational pair (B1.01 unifying separation, B1.02 three-level structure). The recursion is what binds all these together as inheriting from Paper 1's foundation, which is why it closes the phase rather than opens it.

## 2. The architectural commitment, precisely stated

In Paper 2's architecture, **Paper 1's complete architectural specification holds recursively at every structural level**. The recursion has three components.

**Component 1 — Same commitments at every level.** Each of Paper 1's sixteen foundational commitments — human-governed (A1.01), the substrate-cell boundary (A1.02), conflict as first-class object (A1.03), AI as substrate mediator (A1.04), tool-agnosticism (A1.05), linear-cost scaling (A1.06), path retraceability (A1.07), substrate as source of truth (A1.08), KO/OIDA inheritance (A1.09), the determinism contract (A1.10), non-specialist governance (A1.11), labor allocation (A1.12), composition requirements (A1.13), the three adjacencies (A1.14), orchestration-layer distinctions (A1.15), hybrid-systems composition (A1.16) — holds at the cell level, at the aspect level, and at the Self level. The same commitment content holds at each level; Paper 2 does not modify the commitments for higher-level operation. Section 5 traces each commitment's level-specific operational meaning.

**Component 2 — Level-distinct scope.** Each commitment operates at the scope appropriate to the level at which it is invoked. Human-governed (A1.01) at the cell level governs cells, at the aspect level governs aspects, at the Self level governs the Self. Path retraceability (A1.07) at the cell level traces cell operations, at the aspect level traces aspect operations, at the Self level traces Self operations. Composition requirements (A1.13) apply to compositions internal to the level at which they hold — cell-internal substrate composition, aspect-internal cell composition, Self-internal aspect composition. The commitment content is invariant; the operational scope is level-distinct.

**Component 3 — Architectural, not implementational.** The recursion is a property of the commitments themselves, not a flattening of operational machinery across levels. Each level retains a level-distinct verification regime, governance configuration, and operational character per B1.03 (cell as atomic unit), B1.04 (aspect as coordination arrangement), and B1.05 (Self as integrated whole). What recurses is *the architectural commitments to which the level is subject*; what does not recurse is the level's specific machinery. This distinction is what keeps the recursion claim load-bearing without overclaiming a structural identity the levels do not have.

## 3. What makes the recursion architecturally distinctive

Conventional AI architectures with hierarchical structures typically commit to *level-distinct properties* rather than level-recursive commitments. An orchestrator has orchestrator-specific properties (workflow definition, dependency management, retry semantics); a tool has tool-specific properties (idempotence, side-effect declaration, cost characteristics); a control plane has control-plane-specific properties (admission, scheduling, eviction). The architectural specification fragments across levels, with each level's properties stated separately and the relationships between them articulated by integration contracts rather than by recursive commitments.

CKS commits differently. The architectural specification is the same at every level — Paper 1's sixteen commitments hold uniformly at cell, aspect, and Self — and the levels differ in operational scope rather than in architectural specification. This is unusual and consequential. It means the architectural specification does not fragment across the structural framework; one specification governs all three levels. It means downstream derivation work — operational tests, anti-pattern detectors, composition rules — does not have to be replicated three times for three levels but applies at each level by the same definition. And it means defensive prior-art coverage extends with the architecture: a derivation chain written at one level applies at every level by the same recursion that makes the commitments hold there.

## 4. The biological analog

The closest contrast outside CKS is biology, which has *partial* architectural recursion. Cells respire; organs respire as collective metabolic regimes of their constituent cells; organisms respire as integrated cardiopulmonary systems of their constituent organs. Recursion is real, but partial and emergent: each level acquires properties the lower levels do not have (cells do not have hearts; organs do not have nervous systems coordinating them; only organisms have integrated respiratory regulation), and the recursion of any one property operates over a narrow band of the levels rather than across all of them with the same content.

CKS exceeds biology along this axis. The architectural recursion of Paper 1's commitments at every level of Paper 2's structure is *full* — the same sixteen commitments hold at all three levels with content-invariant specification — and it is *architectural* rather than evolved, available at instantiation rather than as a property the architecture has to wait for. The biological scaffold is what makes the recursion immediately legible to readers; the architectural substance is the full recursion across the three levels. As elsewhere in the CKS theory series, biology supplies the framing, and the architectural commitment is CKS's own.

## 5. Inherited Paper 1 commitments operating recursively at each level

Each of A1.01–A1.16 has a level-distinct operational meaning at each level.

**A1.01 — Human-governed.** The three rights — inspect, modify, override at any time — hold over substrate content and orchestration rules at every level: humans govern cells, aspects, and Selves at the corresponding scope.

**A1.02 — Substrate-cell boundary.** The two-layer architectural separation between persistent state and bounded execution holds at every level, with the appropriate boundary objects at cell, aspect, and Self scope.

**A1.03 — Conflict as first-class object.** Two-level conflict handling — substrate-level preservation, resolution under orchestration rules — holds at every level. Cell-internal conflicts in cell substrate, aspect-internal cross-cell conflicts in aspect substrate, Self-internal cross-aspect conflicts in Self substrate; each resolved by the orchestration rules of its level.

**A1.04 — AI as substrate mediator.** The five-property mediator role applies at every level. LLMs operate over cell, aspect, and Self substrate as mediators governed by the orchestration rules of the corresponding level.

**A1.05 — Tool-agnosticism.** The three minimal requirements — persistent state, human read/write access, LLM access to substrate content — hold at every level; each level can be instantiated in commodity tools satisfying the requirements.

**A1.06 — Linear-cost scaling.** Governance, cell, and LLM cost are not size-proportional at any level; cell-level linear cost extends to aspect-level linear cost in cell count and Self-level linear cost in aspect count.

**A1.07 — Path retraceability.** The six-field provenance metadata applies to operations at every level. Cell, aspect, and Self operations all record writer, timestamp, rationale, provenance, version, and authority scope.

**A1.08 — Substrate as source of truth.** The five categories of authoritative state — and the boundary against agent-internal memory — hold at every level. No level relies on agent memory for state that needs to persist between executions.

**A1.09 — KO/OIDA inheritance.** The two-axis extension structure (governance, multi-human) holds at every level; multi-human governance configurations apply at cell, aspect, and Self scope concurrently and in compatible shapes.

**A1.10 — The determinism contract.** The five guarantees and allowed non-determinism patterns hold at every level. Cell, aspect, and Self determinism all operate under the same contract.

**A1.11 — Non-specialist governance.** Governance accessibility decoupled from authorship expertise holds at every level; non-specialists can exercise the three rights at cell, aspect, and Self scope without specialist training.

**A1.12 — Labor allocation.** The three modes (direct human, LLM-under-rule, stable cell) apply at every level; aspect-level and Self-level labor are allocable across the three modes as cell-level labor is.

**A1.13 — Composition requirements.** The five constraints any multi-substrate composition must satisfy apply to compositions internal to each level — cell-internal substrate compositions, aspect-internal cell compositions, and Self-internal aspect compositions all satisfy the same five constraints.

**A1.14 — The three adjacencies.** The architectural distinctions from RAG, parametric memory, and external structured memory hold at every level; none of the three adjacencies converges with CKS at higher levels.

**A1.15 — Orchestration-layer distinctions.** The three-layer architectural model (CKS not workflow engine, agent framework, control plane) holds at every level; aspect orchestration and Self orchestration are also distinct from those three adjacent layers.

**A1.16 — Hybrid-systems composition.** The three composition patterns (input, derived view, separate concern) apply at every level for compositions with adjacent AI components. The instinct/reasoning separation per B1.01 is the Self-scope hybrid composition; cell-scope and aspect-scope hybrid compositions also follow A1.16's three patterns.

## 6. Operational implications

Several implications follow directly from the recursion.

**Series A applies at every level of Paper 2 deployments.** Phase A1's foundational commitments hold at every level by the recursion this note formalizes; Phase A2's operational decompositions extend by the same recursion; Phase A3's anti-pattern formalizations are detectable at every level under the same architectural definitions; Phase A4's composition pairs operate at every level; Phase A5's operational tests run at every level; Phase A6's boundary cases apply at every level. Series A's complete derivation chain is operational across Paper 2 deployments at all three levels.

**Verification is three-leveled.** Verification of inspect, modify, and override rights, of orchestration-rule authoring, and of the rest of A1.01–A1.16 must run at the cell level, at the aspect level, and at the Self level. A deployment that verifies cell-level inspect right but not aspect-level or Self-level inspect right has not verified the recursion, even if cell-level results are robust. Anti-patterns Paper 1 names at cell scope — substrate writes outside cell scope, LLM-internal coordination state, vendor-revocable substrate access, scheduled-window inspection, opaque rule embedding — have aspect-level and Self-level analogues detectable under the same definitions, with the appropriate level-scope object substituted.

**Series B builds on Series A recursively.** Series B does not need to re-derive Paper 1 properties for higher levels. Series B's distinctive content — instinct/reasoning separation, three-level structure, DNA/action layers, expression, lifecycle, evolution mechanisms, bidirectional evolution, structural properties — operates over the inherited Paper 1 foundation. Each Series B note can reference Paper 1 commitments at the level appropriate to its scope without restating Paper 1's derivation.

**Deployments operationalize the recursion through three-level governance.** A Paper 2 deployment configures human-governed authority at cell, aspect, and Self levels concurrently; runs path-retraceability machinery at each level; applies anti-pattern detection at each level; and verifies the determinism contract at each level. The recursion is not an abstract architectural property; it is what governs how the deployment is configured and verified.

## 7. Limits

The recursion claim is precisely scoped, and stating its limits is what keeps the claim load-bearing without overclaiming.

**Levels are not identical.** The recursion is a property of the commitments, not of the levels. Each level retains its level-distinct scope (cell handles a specific informational task; aspect groups cells for a purpose-defined mode of engagement; Self holds multiple aspects as facets of one whole), level-distinct operational character per B1.03–B1.05, and level-distinct verification semantics per the level-appropriate scope object in each operational test. Recursion of commitments does not flatten levels operationally.

**The recursion does not reduce Paper 2 to Paper 1.** Paper 2 adds architectural commitments not present in Paper 1: the unifying instinct/reasoning separation (B1.01), three-level structure (B1.02), two layers within every cell (B1.06–B1.08), expression (B1.07), lifecycle machinery (B1.09–B1.11), three evolution mechanisms (B1.12–B1.15), bidirectional evolution (B1.16), and structural properties (B1.17–B1.19). The recursion is about Paper 1 *inheritance*; Paper 2's distinctive content is *additional*, not derivable from Paper 1 by recursion alone.

**The recursion is architectural, not implementational.** Each commitment holds at each level with the same architectural content but with level-distinct implementation details. The level-specific implementation work is real and not eliminated by the recursion; what the recursion eliminates is having to redefend the architectural commitment at each level.

**The recursion is one-directional.** Paper 2 inherits from Paper 1; Paper 1 does not depend on Paper 2. Paper 1 stands as an architectural specification at cell scope; Paper 2 extends to higher scopes and inherits Paper 1's specification along the way. The cross-derivation work in Series C formalizes specific inheritance edges; the recursion this note formalizes is the umbrella inheritance under which those edges operate.

**The recursion is finite.** Paper 2 specifies three levels — cell, aspect, Self — and the recursion of commitments operates across these three. Additional levels are not specified by Paper 2. Structural arrangements are themselves evolvable per B1.16, so future architectural extensions could introduce additional levels; until then, the recursion is finite at three.

## 8. Operational test

A system instantiates the recursive Paper 1 commitments at every structural level if and only if all of the following are true at all times during the Self's existence:

1. Each of Paper 1's sixteen foundational commitments (A1.01–A1.16) holds at the cell level, in the form Paper 1 specifies.
2. Each of those sixteen commitments holds at the aspect level, with aspect-distinct scope.
3. Each of those sixteen commitments holds at the Self level, with Self-distinct scope.
4. The commitments' content does not change across levels; only the operational scope changes.
5. Each level retains its level-distinct operational character per B1.03 (cell), B1.04 (aspect), and B1.05 (Self).
6. No higher-level commitment depends on the architectural specification differing at higher levels; no higher-level operation is exempt from the commitments that hold at lower levels.

A system that fails any of (1)–(6) does not instantiate the recursion this note formalizes, even if it satisfies the level-specific commitments individually. Such a system is not CKS-coherent on the recursion axis.

## 9. Conclusion

Recursive Paper 1 commitments at every structural level is what makes Paper 2 architecturally coherent with Paper 1, what makes Series A's complete derivation chain operational across Series B deployments, and what makes Paper 2's distinctive primitives additions to Paper 1's foundation rather than displacements of it. The recursion is full (all sixteen Paper 1 commitments at all three Paper 2 levels), architectural (the commitments themselves recurse, not the levels' operational machinery), and one-directional (Paper 2 inherits from Paper 1, not vice versa).

Naming the recursion as standalone foundational commitment closes Phase B1. Phase B1's twenty foundational commitment notes — B1.01 unifying instinct/reasoning separation, B1.02 three-level structure, B1.03–B1.05 cell, aspect, and Self level elaborations, B1.06–B1.08 intra-cell primitives, B1.09–B1.11 lifecycle machinery, B1.12–B1.15 evolution mechanisms, B1.16 bidirectional evolution, B1.17–B1.19 structural properties, and B1.20 (this note) recursive Paper 1 commitments — establish the architectural foundation of Paper 2. Subsequent Series B work proceeds to Phase B2's operational variants and decompositions, paralleling Series A's Phase A2 structure, with the recursion this note formalizes as the inheritance frame under which those decompositions extend.

Subsequent work that adopts Paper 2's three-level structure, derives from it, extends it, or argues against it should use the recursion in the sense formalized here. Subsequent work that uses recursion differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Recursive Paper 1 Commitments at Every Structural Level: A Foundational Architectural Commitment for the Coordination Knowledge Substrate Pattern's Self Architecture.* May 7, 2026. ORCID: 0009-0004-8065-3235.
