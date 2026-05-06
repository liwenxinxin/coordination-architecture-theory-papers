# Mode 3 — Stable-Cell Automation: A Standalone Treatment of the Third Labor Mode in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize Mode 3 — stable-cell automation — as a standalone architectural specification within the labor allocation framework, sufficient to be defended, implemented, and tested independently of the other two modes and the broader framework specifications.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern's labor allocation framework names three modes by which coordination work can be performed: direct human labor, LLM labor under orchestration rules, and stable-cell automation. The third is what the second becomes when the orchestration rule has reached operational stability — refined and validated to the point that humans review at the rule level rather than at the per-execution level. This note formalizes Mode 3 as a standalone architectural specification, defined by four operational components: a rule-stability property, reduced per-execution human attention, preserved at-any-time governance, and stable-cell writer attribution. Mode 3 uses the same architectural mechanisms as Mode 2 — cells, orchestration rules, and the five mediator properties — with operational stability adding reduced-attention properties; the architectural distinction is at the operational-stability level, not at the architectural-mechanism level. Mode 3 is automation under sustained human authority, not autonomy: the temporal property of governance commits to humans retaining inspect, modify, and override rights at any time, including override with no architectural justification precondition. The note specifies the four components, distinguishes Mode 3 from four adjacent labor patterns commonly conflated with it, names the failure modes that violate it by either compromising at-any-time governance or treating it as architecturally autonomous, and provides an operational test for the specification.

## 1. Why Mode 3 needs to be formalized as standalone

The parent foundational note A1.12 commits to the labor allocation framework. The integrating-frame note A2.68 named Mode 3 at the integrating level. A2.69 and A2.70 formalized Mode 1 and Mode 2 as standalone treatments. This note formalizes Mode 3 — stable-cell automation — as having independent architectural content, with particular weight on the operational-stability property that distinguishes Mode 3 from Mode 2 while preserving the at-any-time governance commitment per A2.07.

The motivating cases are deployments where coordination work has reached operational stability under specific orchestration rules: established decision-support cells where the rule has been refined and validated over many executions; well-defined extraction cells operating on repetitive content; routine summarization cells where the rule produces consistent rule-conformant output. Each requires automation under sustained human authority, with reduced per-execution attention.

A second motivation is the prior-art posture. Mode 3 forecloses architectures that present rule-stable AI operation as autonomous AI. Derivations focused on stable-cell architectures, automated AI workflows, or rule-stable AI systems are substantially more defensibly contested when Mode 3 is publicly formalized as standalone with the governance-preservation commitment per A2.07 specified.

A third motivation is the connection to A1.04 (AI-as-substrate-mediator) and A2.07 (temporal property of governance). Mode 3 is what those commitments produce when rule stability allows reduced per-execution attention: the mediator properties hold at every execution; the temporal property holds across the entire rule lifecycle; the architectural commitments are unchanged from Mode 2; the operational pattern is the only difference.

## 2. The Mode 3 commitment, defined precisely

A system supports Mode 3 if and only if it operationalizes the following four components.

**(a) Rule-stability property.** Mode 3 cells operate under orchestration rules per A2.04 that have reached operational stability — rules refined and validated to the point that they consistently produce rule-conformant outputs across the situations the deployment encounters. Stability is an operational property of the rule, not a separate architectural element; the rule itself is substrate content per A2.46, governed under the same human authority that governs all other substrate content. What "stable" means in any particular deployment — observed rule-conformance over many executions, validation against expected outcomes, or other deployment-specific signals — is a deployment judgment; the architectural commitment is to the operational pattern, not to specific stability criteria.

**(b) Reduced per-execution human attention.** Mode 3 operates with humans reviewing at coarser granularity than Mode 2 — typically per-rule, when rules need updating, rather than per-execution. Reduced attention is operationally feasible because rule stability makes per-execution review unnecessary; the operational benefit scales with rule stability. Reduced attention is the operational consequence of (a); a deployment may, by choice, continue per-execution review of cells operating under stable rules without violating the architecture, but it is not architecturally required to do so.

**(c) Preserved at-any-time governance per A2.07.** Mode 3 preserves the temporal property of governance: humans retain the three rights per A2.01–A2.03 at any time, including override per A2.03 with no architectural justification precondition. Reduced operational attention does not reduce architectural authority; humans can intervene at any moment regardless of the cell's operational stability. This component is what makes Mode 3 automation rather than autonomy — the architectural authority structure is identical to Mode 2's; only the operational attention pattern differs.

**(d) Stable-cell writer attribution per A2.37.** Mode 3 writes carry attribution identifying the cell, the orchestration rule under which the cell operated, and operationally indicating the rule's stability status — distinguishing Mode 3 attribution from Mode 2 attribution operationally. Architecturally, both modes have cell-with-rule attribution at the substrate level; the stability property is operational metadata over that architectural attribution. Attribution as Mode 3 makes the labor mode itself an inspectable property of substrate content, supporting per-content judgment about reading, override, or rule revision.

The four components together define Mode 3. A system whose stable-cell labor is rule-governed per A2.04, attended to at coarser granularity than Mode 2, governable at any time per A2.07, and attributable to stable-cell writers instantiates Mode 3 in the architectural sense.

## 3. What Mode 3 does NOT claim

The specification is precise about what Mode 3 *is*. It is equally important to state what it does not claim, because each of the following is a real and reasonable commitment in some other architecture, and conflating any with Mode 3 produces a misreading.

**Not autonomy.** Mode 3 is automation under sustained human authority — the five mediator properties per A2.19–A2.23 hold; the temporal property per A2.07 holds; the human-governed commitment per A1.01 holds. Reduced per-execution attention is operational; authority is architectural.

**Not a prescription about when to move work to Mode 3.** Mode progression dynamics per A2.74 are deployment choices; the architectural commitment is to Mode 3 being operationally feasible, not to specific timing for transitions. A deployment may operate entirely in Mode 1, never reach Mode 2, and leave Mode 3 unused without failing the framework.

**Not a constraint on human attention.** Humans may exercise inspect, modify, or override per A2.01–A2.03 over Mode 3 substrate content at any time. Reduced per-execution attention is the operational benefit of Mode 3, not a restriction on what humans may do.

**Not error-immunity.** Mode 3 operates with allowed LLM non-determinism per A2.62 category (a); rule stability bounds the variation per Guarantee B per A2.58, but specific outputs may still vary within rule-allowed bounds. Mode 3 is not error-free; it is rule-conformant.

**Not mandatory adoption for stable-rule cells.** A deployment may continue Mode 2 operation, with per-execution review, for cells with stable rules if specific operational concerns warrant continued attention. The architectural commitment is to Mode 3 being available, not to its automatic adoption.

**Not a prescription about stability criteria.** What constitutes "stable" is a deployment judgment based on observed rule-conformance, validation against expected outcomes, or other deployment-specific signals. The architectural commitment is to the operational pattern, not to any specific measurement methodology.

## 4. What Mode 3 is NOT

Four adjacent labor patterns are commonly conflated with Mode 3; distinguishing them sharpens the standalone treatment.

**Not autonomous AI systems.** Autonomous AI systems are LLM-based systems where the LLM operates with broad autonomy — making decisions, writing to systems, and executing actions without architectural rule-governance and without sustained human authority. Mode 3 is different: the cell operates under orchestration rules per A2.04; the LLM does not exercise authority per A2.22 (Property D); humans retain governance authority at all times per A2.07. Reduced per-execution attention is operational; the architectural commitments are unchanged from Mode 2.

**Not automated pipelines.** Automated pipelines are operational patterns where work flows through pre-defined steps without human attention, typically without rule-governance as the architecture commits to it. Mode 3 cells operate under orchestration rules per A2.04, with humans authoring and refining rules per the authorship roles A2.66 articulates. Pipeline automation that does not have rule-governance is autonomous operation outside the architecture, not Mode 3.

**Not scheduled batch processing.** Scheduled batch processing runs at scheduled times under pre-defined logic. Mode 3 cells execute in response to triggering conditions per A2.10's boundary crossings, not on schedules; the operational stability is in the rule's behavior, not in the scheduling. Scheduled processing without rule-governance is not Mode 3, regardless of how stable the schedule is.

**Not "set-and-forget" automation.** "Set-and-forget" automation is an operational pattern in which humans configure systems once and do not return attention. A2.07's temporal property of governance commits to humans retaining authority at any time. "Set-and-forget" suggests authority is relinquished after configuration; Mode 3 commits to authority preservation at all times — even though operational attention may be reduced.

## 5. Why Mode 3 is load-bearing for downstream commitments

Mode 3 is load-bearing for several CKS commitments that the labor allocation framework supports.

It is load-bearing for the integrating labor-allocation framework per A1.12 and A2.68. Without Mode 3, the framework would lack the operationally-stable automated labor mode that distinguishes it from any two-mode allocation.

It is load-bearing for the mode progression dynamics per A2.74. Mode 3 is the operational-stability target of Mode 2 → Mode 3 progression; without it specified, the progression dynamics would be incomplete and the architectural commitment to bidirectional progression — Mode 3 → Mode 2 reversal when rules need refinement — would have no defined endpoint.

It is load-bearing for the temporal property of governance per A2.07. Mode 3 is the labor mode where the at-any-time commitment is most operationally consequential — humans retain authority over operationally stable cells despite reduced per-execution attention. Without Mode 3, A2.07's commitment would be primarily relevant to Mode 1 (where reduced attention is not the issue) and Mode 2 (where per-execution attention is typical); Mode 3 is where the at-any-time commitment does the most work.

It is load-bearing for the cost analysis per A1.06 and §6.3. Mode 3 is the labor mode with the most consequential cost benefits — human labor is released by automation while governance cost remains bounded by intervention frequency per A2.33. The linear-cost claim's defensibility under the "but humans must review everything" critique depends on Mode 3 being a coherent architectural commitment.

It is load-bearing for the non-specialist governance commitment per A1.11. Non-specialists govern Mode 3 substrate content the same way they govern Mode 1 and Mode 2 content. Mode 3's reduced per-execution attention is operational; non-specialist governance authority is architectural per A1.01.

## 6. Failure modes that violate Mode 3

Each anti-pattern names a way an implementation can fail Mode 3 by compromising at-any-time governance, treating Mode 3 as autonomous, or violating the underlying mediator commitments.

**(a) Autonomous-Mode-3 patterns.** The implementation treats Mode 3 cells as autonomous — humans cannot exercise the three rights per A2.01–A2.03 over Mode 3 substrate content without going through specialized override workflows. The temporal property per A2.07 fails; Mode 3 becomes autonomy rather than automation under authority.

**(b) Justification-required-for-Mode-3-override.** The implementation requires humans to provide architectural justifications for overriding Mode 3 content — for example, requiring specification of why the cell's output should be overridden, or rule-update proposals as preconditions for override. The no-justification-as-precondition commitment per A2.03 fails specifically for Mode 3; Mode 3 acquires architectural override-friction Mode 1 and Mode 2 content do not have.

**(c) Scheduled-review-only governance.** The implementation restricts human governance over Mode 3 cells to scheduled review windows — quarterly rule reviews, periodic stability audits, designated revision cycles. The at-any-time commitment per A2.07 fails; the at-any-time guarantee is replaced by an at-scheduled-times guarantee that is a different commitment.

**(d) Mode-3-only attention degradation.** The implementation operationally degrades inspection access for Mode 3 cells — outputs are summarized rather than readable, content is archived to slower-access storage, attribution is hidden under "automated" labels that do not surface the rule and cell information. The inspect right per A2.01 is operationally compromised for Mode 3 even where it is not architecturally denied.

**(e) Rule-stability promotion without human authorization.** The implementation automatically promotes Mode 2 cells to Mode 3 based on rule-conformance metrics, without human authorization for the mode transition. The architectural commitment to mode-transition being a deployment choice per A2.74 is broken; Mode 3 adoption becomes a runtime-determined property rather than a governance decision.

**(f) Mode 3 attribution conflation.** The implementation does not distinguish Mode 3 attribution from Mode 2 attribution at the operational level. The mode distinction is lost operationally; per-content judgment about whether to revisit at the rule level or the execution level cannot be made because the labor mode is not inspectable.

**(g) Mode 3 with mediator-property violations.** The implementation operates Mode 3 cells where the mediator properties per A2.19–A2.23 do not hold consistently — the LLM holds state across executions, exercises authority over substrate, or operates outside cell-mediation. Mode 3's architectural coherence with Mode 2 fails; reduced per-execution attention then operates over an architecture that is not the architecture Mode 3 specifies.

**(h) Mode 3 with rule-bypass mechanisms.** The implementation provides Mode 3 capability through rule-bypass mechanisms — "exception" pathways that allow LLM operation without rule-conformance for specific cases, "fallback" handlers that bypass rules under runtime conditions. Rule-stability is operationally violated; Mode 3 is offered as a label over a labor pattern in which rule-conformance is not actually a property of the cell's operation.

**(i) Mode 3 as architectural endpoint.** The implementation treats Mode 3 as a one-way destination — once a cell is in Mode 3, it cannot return to Mode 2 for refinement. The bidirectional progression per A2.74 fails; rules that have reached stability and then need revision cannot be revised under per-execution attention because the cell's mode does not permit it.

**(j) Mode-3-cost-amplification.** The implementation requires human attention to scale with Mode 3 substrate size — humans must review Mode 3 cell executions at sufficient scale that the operational benefit is consumed by the review labor. The architectural commitment to linear-cost per A1.06 fails specifically for Mode 3; the cost benefits Mode 3 was supposed to deliver are eroded by per-execution review the architecture does not require.

## 7. Operational test

A system supports Mode 3 if and only if all of the following are true at all times during the substrate's existence.

1. Mode 3 operates under orchestration rules per A2.04 with operational stability properties per component (a) of section 2.
2. Mode 3 operates with reduced per-execution human attention per component (b) of section 2; humans review at coarser granularity than Mode 2.
3. Mode 3 preserves at-any-time governance per A2.07 per component (c) of section 2; humans can exercise the three rights per A2.01–A2.03 at any moment without architectural preconditions.
4. Mode 3 writes carry stable-cell writer attribution per A2.37 per component (d) of section 2, distinguishable operationally from Mode 1 and Mode 2 attribution.
5. Mode 3 satisfies all five mediator properties per A2.19–A2.23 — the architectural mechanisms are the same as Mode 2.
6. Mode 3 cells can transition back to Mode 2 (or Mode 1) through human intervention; mode progression dynamics per A2.74 are bidirectional.

A system that fails any of (1)–(6) does not support Mode 3 in the architectural sense, even if cells appear to operate with reduced human attention operationally.

## 8. Why naming Mode 3 as standalone matters

Implementations under pressure to deliver "AI automation" or "agentic AI" capabilities consistently drift toward autonomous-AI patterns that violate Mode 3's at-any-time governance commitment. The drift is steady because autonomous-AI patterns are commercially attractive — audiences understand "AI that runs itself" more easily than "AI under sustained human authority with reduced per-execution attention" — and operationally simpler in the short term, since autonomy avoids the architectural commitment to A2.07's at-any-time governance.

Implementations that drift away from Mode 3 produce systems where stable-cell automation is treated as autonomy. The downstream consequences manifest as governance failures (A2.07's temporal property fails — humans cannot exercise authority at any time over Mode 3 cells), override-commitment failures (A2.03's no-justification-as-precondition fails specifically for stable-cell content), framework-incompleteness (the three-mode framework collapses to two modes plus autonomous AI), and mode-progression failures (A2.74's bidirectional progression cannot operate because Mode 3 is treated as architectural endpoint).

Naming Mode 3 as a standalone architectural specification — with the four operational components in §2, the limitations in §3, the four adjacent-pattern distinctions in §4, the load-bearing connections in §5, the ten failure modes in §6, and the operational test in §7 — gives downstream readers a precise specification of what stable-cell automation architecturally requires. Together with A2.72, A2.73, and A2.74, which specialize the three architectural properties, the labor-vs-authority distinction, and mode progression dynamics, this Mode 3 specification closes the decomposition of A1.12.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Mode 3 — Stable-Cell Automation: A Standalone Treatment of the Third Labor Mode in CKS.* Derivation Note. May 5, 2026. ORCID: 0009-0004-8065-3235.
