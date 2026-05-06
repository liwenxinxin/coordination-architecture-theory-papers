# Boundary, Mediator, Cost: The Three Architectural Properties That Make CKS's Labor Allocation Framework Coherent

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a standalone architectural specification, the three already-committed properties — substrate-cell boundary (A1.02), AI-as-substrate-mediator (A1.04), and linear-cost scaling (A1.06) — whose joint operation produces labor-mode coherence in CKS deployments.

## Abstract

The CKS labor allocation framework (A1.12) commits to three modes of coordination work — humans performing it directly (Mode 1), LLMs performing it under human-authored orchestration rules (Mode 2), and stable cells largely automating it under those rules (Mode 3). The framework's coherence — that all three modes produce substrate content of the same architectural kind, governed by the same authority structure, and movable between modes without changing either — rests on three architectural properties operating jointly: the substrate-cell boundary per A1.02, which gives cell-based labor an architectural locus; AI-as-substrate-mediator per A1.04, which bounds LLM operation in Mode 2 and Mode 3; and linear-cost per A1.06, which keeps all three modes operationally feasible at scale. This note formalizes the three-properties specification standalone — articulating each property's contribution, the four operational components of the joint specification, four adjacent coherence patterns commonly conflated with it, ten failure modes, and an operational test.

## 1. Why the three architectural properties need to be formalized as standalone

The parent foundational note A1.12 commits to the labor allocation framework. The integrating-frame note A2.68 enumerated, at the integrating level, three architectural properties whose joint operation produces mode coherence; the sibling notes A2.69, A2.70, and A2.71 formalized the three modes individually. This note formalizes the three architectural properties — substrate-cell boundary per A1.02, AI-as-substrate-mediator per A1.04, and linear-cost per A1.06 — as a unified specification, with particular weight on how the three compose to produce mode coherence that no property alone could produce.

Without precise specification of the three properties' joint contribution, mode coherence appears either as a vague architectural property — claimed but without specific mechanism — or as a deployment-level feature, achievable through consistent interfaces and unified pipelines without architectural commitment. The standalone treatment makes the coherence-producing mechanism specific: three properties, each named, each with its own contribution, composing architecturally. The note does not re-litigate any of the three foundational commitments; each has its own decomposition. It specifies how their joint operation produces mode coherence specifically — a different question from what each property commits to in isolation.

## 2. The substrate-cell boundary's contribution to mode coherence

The substrate-cell boundary per A1.02 commits to architectural separation between substrate (persistent inspectable artifact) and cells (operational units that read from and write to substrate under rules). Its decomposition per A2.08–A2.12 specifies what each layer commits to. The boundary's contribution to mode coherence operates at the architectural-locus level, in four ways.

First, Mode 2 and Mode 3 operate within cells. The boundary specifies cells as the architectural locus for these modes — LLMs in Mode 2 and stable cells in Mode 3 operate within cells, reading substrate per A2.10 and writing to substrate under rules. Without the boundary, "cell" is not an architecturally distinguished object; cell-based labor is operationally indistinguishable from direct labor.

Second, Mode 1 operates with humans crossing the boundary directly per A2.10. The boundary specifies that direct-human-labor crossings are architecturally distinct from cell-mediated crossings — Mode 1 is not "the cell with no LLM," it is the architecturally distinct mode in which humans cross the boundary themselves.

Third, the boundary distinguishes cell-internal state from substrate state per A2.11. Cells do not hold substrate-relevant state outside substrate; this contributes to Mode 2 and Mode 3 coherence by ensuring LLM non-determinism does not propagate via cell-internal state into the substrate that subsequent cell executions read.

Fourth, the boundary forbids cell-to-cell direct channels per A2.12. All inter-cell communication is substrate-mediated, with substrate's representation determinism per Guarantee A governing what cells see — Mode 2 and Mode 3 cells read the same substrate any other reader would see.

Without the substrate-cell boundary, Mode 2 and Mode 3 have no architectural locus; cells are operationally ambiguous; Mode 1 becomes operationally indistinguishable from cell-based modes. The boundary removes the architectural-locus barrier.

## 3. AI-as-substrate-mediator's contribution to mode coherence

AI-as-substrate-mediator per A1.04 commits to the LLM operating as substrate mediator with five properties per A2.19–A2.23. Its contribution to mode coherence operates at the LLM-bounding level, with each property contributing distinctly.

Property A per A2.19 — LLM reads substrate as primary source — ensures Mode 2 and Mode 3 LLM reads are deterministic per Guarantee A: the LLM operates on the same content any other reader would see at the same substrate state. Without it, the LLM might read from a private cache or model-internal memory, breaking substrate-as-source-of-truth for cell-based modes.

Property B per A2.20 — LLM writes under orchestration rules — ensures Mode 2 and Mode 3 writes are rule-conformant per Guarantee B. The rule-governance is what distinguishes these modes from autonomous AI patterns: the LLM writes substrate content only as the cell's authored output under human-authored rules, never as autonomous-agent output bypassing the rule layer.

Property C per A2.21 — LLM does not hold substrate-relevant state outside substrate — ensures LLM non-determinism does not accumulate across cell executions in ways that propagate to substrate. Each cell execution is bounded; what crosses to substrate is the rule-governed output, not the LLM's accumulated state.

Property D per A2.22 — LLM does not exercise authority over substrate content — ensures authority over Mode 2 and Mode 3 substrate content remains with humans per A1.01. The labor-vs-authority distinction per A2.73 holds across all three modes because Property D holds in Mode 2 and Mode 3, and Mode 1 holds authority directly. Without Property D, Mode 2 and Mode 3 silently transfer authority to the LLM, making the framework's central commitment — that authority is mode-independent — false in operation even where claimed in architecture.

Property E per A2.23 — LLM outputs that affect substrate state are recorded with attribution — ensures Mode 2 and Mode 3 writes carry cell-with-rule attribution per A2.37, making the modes operationally distinguishable at the substrate-content level.

Without AI-as-substrate-mediator, Mode 2 and Mode 3 are architecturally unspecified — autonomous AI patterns, terminal-producer patterns, and rule-bounded patterns are indistinguishable. The mediator commitment removes the LLM-bounding barrier.

## 4. Linear-cost's contribution to mode coherence

Linear-cost per A1.06 commits to the cost contract per A2.29–A2.34, which specifies what scales with substrate size (storage; full-substrate-read) and what does not (cell execution cost is task-scope-proportional per A2.32; governance cost is not size-proportional per A2.33). Its contribution to mode coherence operates at the cost-properties level.

Mode 1 cost scales with intervention frequency, a deployment choice, not with substrate size: non-specialists per A1.11 can govern substrates of any size in Mode 1 because governance cost is not size-proportional and the inspect/modify/override rights are exercised at moments of choice. Mode 2 cost scales with cell execution count — task-scope-proportional per A2.32 — and rule variety per A2.31, not with substrate size, because each cell execution reads only the cell-scoped subset of substrate the rules name. Mode 3 cost scales with rule variety per A2.31, not with substrate size; the cost benefit of Mode 3 is specifically that human labor is released by automation while governance cost remains bounded by intervention frequency.

Cost properties compose across modes: a deployment using all three modes simultaneously faces cost dynamics that remain bounded by the contract, because each mode's cost is bounded individually and the modes share substrate as their interface.

Without linear-cost, all three modes face cost amplification at scale that undermines feasibility: Mode 1 governance scales prohibitively as substrate grows; Mode 2 LLM operation faces cost amplification as cells expand the substrate they read; Mode 3 stable-cell governance does not produce the cost benefits that motivate its use. The cost contract removes the cost-amplification barrier.

## 5. The four operational components of the joint specification

The three-properties specification's content is the joint operation of the three properties; that joint operation has four operational components.

**(a) Each property's contribution is operationally distinct** per sections 2–4. The contributions operate at different architectural layers — substrate-content, cell-execution, cost-properties — and address different dimensions of the framework's operational requirements.

**(b) The three properties compose architecturally.** No property alone produces mode coherence. Substrate-cell boundary alone specifies architectural locus but does not bound LLM operation or cost; AI-as-substrate-mediator alone bounds LLM operation but does not provide locus or bound cost; linear-cost alone bounds cost but does not provide locus or bound LLM operation. The three together produce the operational coherence the framework requires; the composition is architectural, not feature-additive.

**(c) Each property is necessary.** Removing substrate-cell boundary produces architectures where Mode 2 and Mode 3 lack locus. Removing AI-as-substrate-mediator produces architectures where LLM operation is unspecified. Removing linear-cost produces architectures where cost dynamics undermine mode operational feasibility. Each property removes a different barrier; all three are needed.

**(d) The specification operates at the architectural-pattern level.** The three properties are architectural commitments, not deployment-level features. Deployment-level features — consistent UIs across modes, unified pipelines, standardized monitoring — may operationally enhance coherence but do not substitute for the architectural commitments. A deployment may be more or less operationally polished depending on its features; the architectural mode coherence is produced by the three properties, regardless.

A system that satisfies all four components has the joint specification in the architectural sense.

## 6. What the specification does NOT claim

The specification does not claim the three properties are *sufficient* for the entire labor allocation framework. Mode coherence is one architectural concern; the framework also requires the labor-vs-authority distinction per A2.73 and mode progression dynamics per A2.74. The three properties produce mode coherence specifically; other elements produce other framework properties.

It does not specify deployment-level coherence features. Deployments may have specific features — consistent interfaces, unified observability — that complement the architectural properties without substituting for them.

It does not claim the three properties are mutually independent. They are operationally entangled: the boundary depends on cells being architecturally specified, which AI-as-substrate-mediator partially specifies for LLM cells; linear-cost depends on the boundary's structure to bound cell execution cost. Their entanglement is a feature, not a limitation.

It does not foreclose other commitments from contributing. The determinism contract per A1.10 contributes through Guarantees A and B; path retraceability per A1.07 through writer-attribution; substrate-as-source-of-truth per A1.08 through the single-substrate property the modes share. The three properties named here are load-bearing for mode coherence specifically; other contributions are additional.

It does not require all three properties to operate at the same operational layer (the boundary at substrate-content, the mediator at cell-execution, the cost contract at cost-properties), and it does not specify how the properties are operationally implemented. The architectural commitment is to the properties being operationally satisfied per their own decompositions, not to specific implementation mechanisms.

## 7. What the specification is NOT

Four adjacent coherence patterns are commonly conflated with the three-properties specification.

**Not architectural consistency.** Architectural consistency is the property that all parts of an architecture follow the same patterns. The specification is different: it commits to three particular architectural commitments. A consistently-designed autonomous-AI architecture has consistency without mediator bounding; a system may satisfy the specification with apparent inconsistency at the implementation level, because the specification operates at the pattern level above implementation.

**Not operational uniformity.** Operational uniformity is the property that operations look or behave similarly across contexts. The three modes may have very different operational characteristics — Mode 1 is direct human labor with whatever interface the human chooses; Mode 2 is LLM-under-rule with cell execution dynamics; Mode 3 is automated stable-cell with intervention-on-exception dynamics — while satisfying the architectural specification.

**Not infrastructure standardization.** Infrastructure standardization is the operational practice of using common infrastructure across deployments. The specification operates at the architectural-pattern level; implementations may use various infrastructure choices while satisfying it, because the architecture is technology-agnostic per A1.05.

**Not deployment-pattern unification.** Deployment-pattern unification is the practice of using common deployment patterns across services. Deployments may have varied operational patterns — different release cadences, different monitoring conventions — while satisfying the architectural specification.

## 8. Why the specification is load-bearing for downstream commitments

The specification is load-bearing for several commitments downstream of A1.12. The integrating labor-allocation framework per A1.12 and A2.68 depends on it: without the three properties composing, mode coherence is aspirational rather than architecturally produced, and the framework collapses into three disconnected modes that share a name but not an architecture. The three modes individually per A2.69, A2.70, and A2.71 each depend on the three properties operating: Mode 1 depends on the boundary's distinction of direct-human-labor crossings; Mode 2 and Mode 3 depend on all three properties operating together to make cell-based labor architecturally coherent.

The labor-vs-authority distinction per A2.73 depends on architectural mode coherence: authority is independent of labor mode because the three properties preserve authority across all modes — Property D within the mediator commitment preserves it in Mode 2 and Mode 3, and Mode 1 preserves it by definition. The mode progression dynamics per A2.74 depend on the three properties holding across mode transitions: moving work between modes does not require new architectural commitments because the three properties already operate; what changes is the writer attribution per Property E.

The non-specialist governance commitment per A1.11 depends on the specification: substrate-cell boundary provides the inspect locus; AI-as-substrate-mediator ensures LLM writes are rule-conformant for governance review; linear-cost ensures governance accessibility scales with substrate size rather than collapsing under it.

## 9. Failure modes that miss one or more of the three properties

**(a) Missing substrate-cell boundary.** The implementation lacks architectural separation between substrate and cells; cells hold substrate-relevant state outside substrate or substrate executes cell-like behavior. Mode 2 and Mode 3 lack architectural locus; cell-based labor is indistinguishable from direct labor.

**(b) Missing AI-as-substrate-mediator.** The implementation permits LLMs to operate without the five mediator properties — autonomous AI, terminal-producer, or authority-bearer patterns. Mode 2 and Mode 3 are architecturally unspecified; what the deployment calls "Mode 2" may be any of several roles depending on which property is missing.

**(c) Missing linear-cost.** The implementation has cost dynamics that scale super-linearly with substrate size for one or more modes. The framework's offer that work can be allocated freely across modes is hollow because some modes become unaffordable as substrate grows.

**(d) Missing two or three properties.** Implementations missing multiple properties produce architectures with multiple barriers to mode coherence. The pathology is multiplicative: missing both boundary and mediator, for example, produces an architecture with neither cell locus nor LLM bounding, where the modes are not even nominally distinguishable.

**(e) Treating the properties as feature-additive.** The implementation adds the three as separate features that compose feature-additively. The architectural composition per component (b) of section 5 is broken; each property is treated as an independent enhancement rather than as a commitment whose joint operation with the others is what produces the coherence.

**(f) Treating the properties as deployment options.** The implementation makes the three properties configurable through deployment options — the boundary turned off in some deployments, the mediator commitment relaxed for "agent-mode" cells, the cost contract waived for "high-throughput" workloads. Mode coherence becomes conditional rather than guaranteed.

**(g) Operationally simulating coherence without architectural commitments.** The implementation provides consistent interfaces or unified pipelines that operationally suggest mode coherence, but the architectural properties are not present beneath the interfaces. The coherence depends on deployment-level features that may be removed, degraded, or undermined by changes leaving the interfaces intact.

**(h) Substrate-cell boundary without cell architectural specification.** The implementation has a "boundary" but cells are not architecturally specified per A1.02's decomposition. The boundary is nominal; the cell layer's commitments per A2.08–A2.12 are absent.

**(i) AI-as-substrate-mediator with hidden authority delegation.** The implementation claims the mediator commitment but operationally permits LLMs to "interpret" rules, "extend" them for novel cases, or "exercise judgment" about edge cases beyond rule scope. Property D fails operationally; authority over Mode 2 and Mode 3 substrate content silently transfers from humans to the LLM under cover of rule-conformance language.

**(j) Linear-cost in name only.** The implementation claims linear-cost but specific operational paths produce super-linear cost dynamics for one or more modes — full-substrate context windows passed to every Mode 2 cell execution, governance review processes that scan all substrate on every change, Mode 3 monitoring whose cost grows with substrate size. The contract is nominally present but operationally violated for the specific allocations that matter most.

## 10. Operational test

A system instantiates the three-properties specification if and only if all of the following are true at all times during the substrate's existence.

1. **Substrate-cell boundary per A1.02 is operationally satisfied.** The architectural separation per A2.08–A2.12 holds; cells are architecturally distinct from substrate; the boundary is operationally crossed only through A2.10's atomic commits; cell-internal state is operationally distinct from substrate state per A2.11; cell-to-cell communication is substrate-mediated per A2.12.

2. **AI-as-substrate-mediator per A1.04 is operationally satisfied.** The five mediator properties per A2.19–A2.23 hold for all LLM operation in Mode 2 and Mode 3: LLMs read substrate as primary source, write under orchestration rules, do not hold substrate-relevant state outside substrate, do not exercise authority over substrate content, and produce outputs recorded with cell-with-rule attribution.

3. **Linear-cost per A1.06 is operationally satisfied.** The cost contract per A2.29–A2.34 bounds cost dynamics for all three modes; cell execution cost is task-scope-proportional per A2.32; governance cost is not size-proportional per A2.33.

4. **The three properties compose architecturally to produce mode coherence** per component (b) of section 5. The composition is not feature-additive.

5. **Each of the three properties is necessary for mode coherence** per component (c) of section 5. Removing any one would produce an identifiable barrier — the architectural-locus barrier, the LLM-bounding barrier, or the cost-amplification barrier — that the deployment can describe.

6. **The specification operates at the architectural-pattern level** per component (d) of section 5. Deployment-level features may complement the properties but do not substitute for them.

A system that fails any of (1)–(6) does not instantiate the three-properties specification in the architectural sense, even if its operational interfaces appear coherent across modes.

## 11. Why naming the specification as standalone matters

Implementations under pressure to deliver flexible labor-allocation capabilities consistently drift toward operational-coherence patterns that do not produce architectural coherence. The drift is steady because operational features — consistent interfaces, unified pipelines, standardized monitoring — are commercially familiar and rhetorically accessible: audiences understand "consistent experience" more easily than "three architectural properties composing to produce mode coherence." The drift is also concealable, because operational features can produce, for a time, behavior indistinguishable from what the architectural specification would produce.

Implementations that drift away from the specification produce systems where mode coherence is operationally claimed but architecturally absent. The downstream consequences manifest as mode-incoherence under stress, labor-allocation failures at scale, authority-leakage when the mediator commitment is not architecturally enforced, and framework-incompleteness when the architectural support for mode coherence collapses.

Naming the three-properties specification as a standalone architectural commitment gives downstream readers a precise specification of what produces mode coherence architecturally, and what fails to produce it even when the operational appearance is similar. The subsequent notes A2.73 and A2.74 specialize the labor-vs-authority distinction and mode progression dynamics; together with this specification, they will close the decomposition of A1.12.

## Source paper

Li, Wenxin. *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. Sections referenced: §2.1 (substrate as inspectable artifact), §2.3 (labor-vs-authority; the three modes and the architectural properties making them coherent), §4.1 (cells as operational units), §4.2 (LLM as substrate mediator), §6.1 (linear-cost scaling and the cost properties of the labor modes).

## Self-citation

Li, Wenxin. *Boundary, Mediator, Cost: The Three Architectural Properties That Make CKS's Labor Allocation Framework Coherent.* Derivation note A2.72 in the CKS derivation series. May 5, 2026. Licensed CC BY 4.0. ORCID: 0009-0004-8065-3235.
