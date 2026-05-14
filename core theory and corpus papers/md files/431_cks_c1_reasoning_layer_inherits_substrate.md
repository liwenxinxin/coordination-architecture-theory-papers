# Reasoning Layer Coordination Substrate Inherits Paper 1's Substrate

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series.

## Abstract

Paper 2 of the CKS theory series introduces an instinct/reasoning separation within every cell of a CKS-governed AI Self: instinct lives inside the LLM, reasoning lives in a coordination substrate outside the LLM. Paper 2 names this configuration explicitly as "a persistent human-governed coordination substrate in Paper 1's specific sense" (§4.3). This note formalizes the consequence: the reasoning layer coordination substrate inside every Paper 2 cell *is* the Paper 1 substrate, scoped to cell-reasoning context, with all six Paper 1 architectural commitments traveling with it unchanged. The inheritance is strict (⊃) rather than approximate: Paper 2 adds cell-scope explicit naming, coexistence with a second substrate (the harness substrate, governing the instinct layer), and participation in Paper 2's lifecycle and evolution mechanisms, but these are additions to the inherited commitments rather than substitutions for them. Anyone implementing a Paper 2 reasoning layer is therefore implementing a Paper 1 substrate at cell-reasoning scope. This forecloses two adversarial readings: that Paper 2's coordination substrate is a new invention unrelated to Paper 1's substrate, and that it is free of Paper 1's governance commitments. Note C1.01 formalized the broader inheritance of the full instinct/reasoning separation from Paper 1's hybrid architecture; this note narrows to the substrate object directly, tracing it to its Paper 1 parent and stating the operational test under which the inheritance can be verified.

## 1. Why this inheritance edge needs to be formalized

Paper 2's foundational move — the instinct/reasoning separation — rests on a specific reading of where the reasoning layer lives architecturally: not inside the LLM's weights, not in engineered configuration held fixed during operation, but in a persistent human-governed coordination substrate. Paper 2 §4.3 states the System-2-analogue layer "lives in a persistent human-governed coordination substrate in Paper 1's specific sense." §4.4 makes the same identification load-bearing for differentiation from the dual-process AI literature Paper 2 surveys (SOFAI, Bengio's System-2 Deep Learning program, *Reasoning on a Spectrum*, D-Mem, the cognitive-architectures tradition): "Only if it lives in a human-governed coordination substrate — persistent, inspectable, modifiable, overridable, cross-session-addressable — can humans maintain architectural authority over the reasoning layer during operation."

The phrase "in Paper 1's specific sense" is the link. Without it, *coordination substrate* could be read as a fresh Paper 2 term naming a new object whose properties Paper 2 would have to defend from scratch. With it, the coordination substrate is the Paper 1 substrate carrying Paper 1's six architectural commitments. This note states the consequence operationally, so downstream work and adversarial readings cannot detach the coordination substrate from its Paper 1 parent.

## 2. The inheritance edge — precise statement

The inheritance edge formalized here is:

> The reasoning layer coordination substrate within every Paper 2 cell *is* the Paper 1 substrate, scoped to cell-reasoning context. All six Paper 1 architectural commitments apply to it unchanged.

Three clauses of this statement carry distinct work.

**"Is the Paper 1 substrate"** — identity, not analogy. The coordination substrate is the same architectural object Paper 1 defines, named in Paper 2 with a more specific qualifier (*coordination*) to distinguish it from the second substrate Paper 2 introduces in the same cell — the harness substrate, which governs instinct expression, verification, and integration into reasoning outputs. The qualifier names the layer the substrate serves; it does not name a different kind of substrate.

**"Scoped to cell-reasoning context"** — the only modification Paper 2 makes. In Paper 1, the substrate is the cell's substrate object; there is no other substrate within the cell. In Paper 2, the same substrate object is now identified as the substrate of the reasoning layer specifically, coexisting with the harness substrate that serves the instinct layer. The scope-narrowing is architecturally consequential but does not weaken or replace any commitment Paper 1 places on the substrate. The Paper 1 substrate at cell-reasoning scope is still the Paper 1 substrate.

**"All six Paper 1 architectural commitments apply unchanged"** — the strict-inheritance (⊃) clause. Each of Paper 1's six commitments applies to the reasoning layer coordination substrate as Paper 1 defends them at cell scope. None is weakened, replaced, or made conditional on Paper 2 machinery. Path retraceability, the §3.1 traceability commitment Paper 1 imports from prior work, travels with the substrate as well. Section 3 traces each through.

## 3. What is preserved — the six commitments at cell-reasoning scope

Each Paper 1 commitment makes specific demands of substrate content and substrate access; each carries through unchanged.

**Hybrid architecture with governance boundary (Claim 1).** The division between LLM and substrate at the governance boundary holds. The coordination substrate carries what humans encode explicitly — entities, rules, decisions, rationale, conflicts — and the LLM handles high-dimensional reasoning humans cannot or should not encode. The division Paper 1 draws at cell scope holds at reasoning-layer scope.

**Conflict preservation (Claim 2; Claim 3 reframed).** Contradictions surfaced during reasoning-layer operation are persisted in the coordination substrate as first-class addressable objects with their own identity and provenance, preserved by default rather than auto-resolved. Cell-level handling of preserved conflicts follows human-authored orchestration rules. The two-level conflict-handling structure applies to the coordination substrate as it applies to any Paper 1 substrate.

**Human-governed authority.** The three rights — inspect, modify, override — apply to the coordination substrate's content and to the orchestration rules that govern the reasoning layer's cell-level behavior. Humans retain these rights at any time, with no architectural gating. The authority architecture Paper 1 commits to — authority not labor, available not mandatory, architectural not procedural — transfers intact. Governance cost is paid at the two moments Paper 1 names (rule authoring; direct override), neither of which scales with substrate content size.

**AI-as-substrate-mediator (Claim 3, reframed).** The LLM operates as mediator over the coordination substrate, reading from it as its primary state source and writing to it under orchestration rules. The coordination substrate is the source of truth for the reasoning layer; the LLM does not hold reasoning-layer state in its context as authoritative. The LLM cannot resolve substrate conflicts outside what orchestration rules authorize, cannot override the substrate's default conflict-preservation behavior, and cannot alter orchestration rules without human authority.

**Tool-agnosticism (Claim 5).** The coordination substrate can be instantiated in any environment meeting the three minimal host requirements: persistent structured state, human read/write access, and LLM access to substrate content. No specialized runtime is required. The property follows from the substrate object's identity, not from cell-level structure around it.

**Linear-cost composition (Claim 4/6).** Expanding the coordination substrate's content grows storage linearly. Composition is human-governed and selective. The cost model is infrastructure scaling, not coordination-intelligence scaling. Paper 2's lifecycle and evolution mechanisms act on the substrate but do not alter its cost-scaling profile.

**Path retraceability (§3.1).** The provenance commitments Paper 1 §3.1 imports — writer attribution, timestamp, antecedent reference, rule reference, rationale where required, contradiction-relationship references where applicable — apply to coordination substrate content unchanged. Any decision recorded in the reasoning layer's coordination substrate must be reconstructable from substrate content alone. The accountability-plan / accountability-trace contract travels with the substrate: schema and orchestration rules constitute the plan; substrate content as it accumulates constitutes the trace.

The six commitments specify what a Paper 1 substrate must be; the reasoning layer coordination substrate satisfies them all.

## 4. What is new in Paper 2 — additions, not replacements

Paper 2 adds structure around the coordination substrate. None of the additions replace or weaken the inherited commitments.

**Cell-scope explicit naming.** Paper 2's coordination substrate is named specifically as the substrate of the reasoning layer within the cell, distinguishing it from the harness substrate. A Paper 2 cell has two substrate objects where a Paper 1 cell had one, but the qualifier identifies scope, not substance.

**Coexistence with the harness substrate within the cell boundary.** Within every Paper 2 cell, the coordination substrate and the harness substrate are distinct governed objects sharing the cell boundary. Both are substrate content under Paper 1 commitments; they serve different layers. The coordination substrate holds what the reasoning layer reads and writes; the harness substrate holds what governs the instinct layer's expression, verification, and integration. The coordination substrate's identity as a Paper 1 substrate is not modified by the presence of the second substrate; it is simply no longer the only substrate in the cell.

**Participation in Paper 2 lifecycle and evolution mechanisms.** The coordination substrate participates in Paper 2's three evolution mechanisms (instinct evolution, DNA evolution, action-feedback evolution) and in the lifecycle primitives (birth, mating, death). Its content feeds the action layer; directed-selection events under DNA evolution modify its specifications; action-feedback proposals target it for refinement. These mechanisms operate on the substrate but do not replace the Paper 1 commitments it carries. Mating produces a new coordination substrate that is itself a Paper 1 substrate. DNA evolution updates orchestration content under the human-governed authority architecture. Action-feedback proposals are substrate-recordable and human-mediated before they take effect. The evolution machinery operates within the inherited commitments, not over them.

## 5. Relationship to C1.01

C1.01 formalized the inheritance of the full instinct/reasoning separation from Paper 1's hybrid architecture (Claim 1) — the architectural move under which the reasoning layer exists outside the LLM and the instinct layer remains inside it, with the division drawn at the governance boundary at Self scope rather than only at cell scope. C1.01 covered the separation as a whole: instinct side, reasoning side, and the boundary between them.

This note (C1.02) narrows to one side of that separation: the reasoning layer's substrate object specifically, traced as identity to the Paper 1 substrate. C1.01 says the instinct/reasoning separation inherits from the hybrid commitment; C1.02 says the substrate object inside the reasoning layer of every Paper 2 cell *is* the Paper 1 substrate at cell-reasoning scope. Subsequent Series C notes will trace remaining inheritance edges — the instinct-layer side via the harness substrate, lifecycle primitives, evolution mechanisms, per-mechanism governance shape, enterprise-brain scope — one at a time. C1.02 supplies the object-level argument that complements C1.01's architecture-move-level argument.

## 6. Prior-art significance — two adversarial claims foreclosed

By formalizing the coordination substrate as the Paper 1 substrate at cell-reasoning scope, this note forecloses two adversarial readings.

**The first foreclosed reading: novel-object claim.** Without this identification, an adversary could argue that Paper 2's coordination substrate is a new object — a Paper 2 invention named with a Paper 2 term — and that prior-art coverage of the Paper 1 substrate does not extend to it. The note forecloses this reading: Paper 2's coordination substrate is the Paper 1 substrate. The naming distinction is scope; the object is unchanged. Implementing a Paper 2 reasoning layer means implementing a Paper 1 substrate at cell-reasoning scope, and prior art covering the Paper 1 substrate covers it.

**The second foreclosed reading: stripped-governance claim.** An adversary could argue that even if the coordination substrate inherits the name *substrate* from Paper 1, it does not inherit Paper 1's specific governance commitments — that one could implement a coordination substrate stripped of conflict preservation, human-governed authority, AI-as-substrate-mediator, tool-agnosticism, linear-cost composition, or path retraceability, and still satisfy what Paper 2 requires. The note forecloses this reading: all six commitments are required of the coordination substrate as a condition of identity. A "coordination substrate" lacking any of the six is not a Paper 2 coordination substrate in Paper 1's specific sense.

The two foreclosures together establish that the inheritance edge is strict (⊃), not approximate. Paper 2's reasoning layer is Paper 1 at cell-reasoning scope plus Paper 2 additions; it is not Paper 1 with selective inheritance, nor a parallel-rather-than-derivational object.

## 7. Operational test

A reasoning layer in a Paper 2 cell instantiates the inheritance edge formalized here if and only if all of the following hold for its coordination substrate, verifiable independently of the harness substrate that coexists in the same cell:

1. The substrate is human-governed in Paper 1's specific sense — humans retain the rights to inspect, modify, and override its content and the orchestration rules that govern reasoning-layer cell-level behavior, at any time, with no architectural gating by LLM, vendor, or runtime middleware.
2. Conflicts encountered during reasoning-layer operation are preserved as first-class addressable substrate objects with their own identity and provenance, with cell-level conflict handling following human-authored orchestration rules.
3. The LLM mediating the reasoning layer reads from and writes to the coordination substrate under orchestration rules, does not hold reasoning-layer state as authoritative in its context, and cannot resolve conflicts or alter orchestration rules outside human authority.
4. The substrate is instantiable in any environment meeting Paper 1's three minimal host requirements (persistent structured state, human read/write access, LLM access to substrate content); no specialized runtime is required.
5. Expanding the coordination substrate's content grows storage linearly; composition is human-governed and selective.
6. Every piece of coordination substrate content carries the provenance fields path retraceability requires — writer attribution, timestamp, antecedent reference, rule reference where applicable, rationale where the plan requires it, contradiction-relationship references where applicable — and any decision recorded in the reasoning layer can be reconstructed from substrate content alone.

A reasoning layer that fails any of (1)–(6) may be a useful reasoning layer, but it does not instantiate Paper 2's coordination substrate in Paper 1's specific sense. The coordination substrate's identity as a Paper 1 substrate is what the six tests check.

The test is statable for the coordination substrate alone, without reference to the harness substrate. The harness substrate is a parallel object subject to its own inheritance edge, formalized separately.

## 8. Conclusion

The reasoning layer coordination substrate within every Paper 2 cell is the Paper 1 substrate at cell-reasoning scope. All six Paper 1 architectural commitments apply unchanged; path retraceability and the accountability-plan / accountability-trace contract travel with it as well. Paper 2 adds explicit cell-scope naming, coexistence with the harness substrate, and participation in Paper 2's lifecycle and evolution mechanisms, but these additions sit on top of the inherited commitments rather than modifying them. The inheritance is strict (⊃): implementing a Paper 2 reasoning layer is implementing a Paper 1 substrate at cell-reasoning scope.

The prior-art consequence is that two adversarial readings — that Paper 2's coordination substrate is a new object, and that it does not carry Paper 1's governance commitments — are both foreclosed by Paper 2's own §4.3–§4.4 text and by the operational test in §7. Subsequent work using the term *coordination substrate* in a different sense is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Reasoning Layer Coordination Substrate Inherits Paper 1's Substrate.* May 14, 2026. ORCID: 0009-0004-8065-3235.
