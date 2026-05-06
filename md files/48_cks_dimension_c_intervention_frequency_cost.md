# Dimension C: Intervention-Frequency Cost as Standalone Architectural Treatment in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 4 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one of the four cost dimensions named in the source paper's "linear-cost scaling" commitment — **Dimension C, intervention-frequency cost** — as a standalone architectural treatment with independent operational content, separable from the substrate-size, rule-variety, and workload dimensions with which it composes into the integrated cost-scaling commitment.

## Abstract

The CKS pattern's "linear-cost in storage and composition" commitment (Claim 5; §6 of the source paper) decomposes into four cost dimensions: substrate size (A), rule variety (B), intervention frequency (C), and workload. A separate note formalizes the integrating frame; further notes formalize the other three dimensions. This note formalizes Dimension C — the cost behavior of human-initiated direct overrides per the second governance moment (§3.3) — as having independent operational content. Its load-bearing claim is the **per-intervention cost property**: each override carries a cost paid at the moment of exercise, bounded by the human's evaluation effort and the intervention's scope, not amortized across substrate scope and not amplified by architectural infrastructure. The note states what Dimension C measures, specifies the cost behavior the architecture commits to, articulates the R/F tradeoff through which Dimensions B and C interact at deployment design, distinguishes Dimension C from four adjacent cost patterns commonly conflated with it, enumerates eight failure modes that violate the per-intervention property, and provides an operational test for whether a deployment is CKS-coherent on the intervention-frequency dimension.

## 1. Why Dimension C needs to be formalized as standalone

The parent foundational note on linear-cost scaling commits the CKS pattern to a cost contract whose substantive claim is asymmetric: of the costs a CKS system incurs, only storage and full-substrate read scale with substrate size, while governance, cell execution, LLM cost per execution, conflict handling, and onboarding costs do not. The integrating-frame note for the operational decomposition resolves the contract into four cost dimensions, three of which (A, B, C) carry architectural commitments and one of which (workload) is acknowledged as orthogonal. Dimension-specific standalone treatments formalize substrate size and rule variety. This note formalizes the third dimension — **intervention frequency**, denoted F — as standalone.

Dimension C is paired with Dimension B on the governance-cost axis. B is **design-time governance cost** (rule authoring, paid once per rule and amortized across cell executions); C is **intervention-time governance cost** (direct override, paid once per exercise and not amortized). Together they exhaust the architecture's commitment to where governance cost is paid — at design time and at intervention time, neither continuously nor per substrate element. Dimension B's standalone treatment articulates the design-time half; this note articulates the intervention-time half.

Architecturally, Dimension C specifies the cost-behavior content of the second governance moment treated by the deep-dive note on direct override and the standalone note on the override right. Those notes treat the moment and the right; this note treats their cost properties. The pairing is what makes the override commitment operationally exercisable at scale — a right whose exercise carries architectural overhead is operationally compromised at scale, however formally it is preserved. Without a precise specification of what cost behavior the architecture commits to on this dimension, deployments cannot plan governance patterns coherently, and downstream implementations cannot defensibly claim CKS-coherence on the intervention-cost axis. Formalizing the per-intervention property publicly also forecloses architectures where intervention cost grows with substrate scope or cumulative intervention history, narrowing the patentable territory around intervention-management and override-tracking infrastructure.

## 2. What Dimension C measures

Dimension C measures the rate F at which humans exercise direct override over substrate state per unit time. The measurement has three operational components.

**(a) Intervention rate.** The number of overrides exercised per unit time — per day, per week, or per month. F is a rate, not a cumulative count. Cumulative interventions over a deployment's lifetime grow without bound; the architecturally relevant quantity is the rate over a defined window, since per-period cost is what determines whether the deployment's intervention pattern is sustainable.

**(b) Intervention scope distribution.** Different interventions have different scopes: a single-element substrate edit, a multi-element correction, an orchestration-rule modification, or a complex multi-step intervention spanning several substrate regions. Scope affects per-intervention cost; F as a rate is approximately the average over the scope distribution the deployment exhibits.

**(c) Intervention authority distribution.** Different humans with override authority may exercise it at different rates, with different scopes, in different substrate domains. Aggregate F is the sum of per-human intervention rates across the deployment's authority structure. The architectural commitment to per-intervention cost is independent of distribution; the operational characteristics of the resulting F are not.

F grows in three patterns deployments commonly exhibit: increased deployment activity, rule-coverage degradation as substrate domains evolve, and new situation classes when deployments expand into substrate domains rules do not yet cover. These are deployment dynamics the architecture supports without prescribing; none is itself an architectural commitment.

## 3. The cost behavior committed to

The architectural commitment on Dimension C — the load-bearing claim of this note — has four components.

**(a) Cost is paid per intervention at the moment of exercise.** Each intervention costs the human's effort to evaluate the situation, decide on the override action, and execute it on substrate state. The cost is paid once per intervention; subsequent interventions cost their own human-effort independently. This is the cost-behavior counterpart of the architectural commitment to direct override as the second governance moment.

**(b) Per-intervention cost is bounded by the intervention's scope and the human's evaluation effort, not by substrate size.** An override exercised against a substrate of size N=1,000,000 costs the same human effort as an override of identical scope against a substrate of size N=1,000. Cost depends on what the human must evaluate to make the specific intervention, not on the substrate's total size. This is Dimension C's inheritance of the size-independence guarantee from Dimension A; the size-independence-of-governance property as a whole receives its own standalone treatment in a sibling note.

**(c) Cost is not amortized across substrate scope.** Unlike rule cost on Dimension B, which is paid once per rule and applied across every subsequent cell execution under that rule, intervention cost is paid per exercise. Each override is a discrete human-effort cost; there is no equivalent to rule amortization on Dimension C. A deployment cannot reduce its per-period intervention cost by accumulating interventions; the only architectural lever is F itself.

**(d) Aggregate intervention cost grows linearly with F.** A deployment with F=10 per week has roughly ten times the per-week intervention cost of a deployment with F=1, assuming similar scope distributions. Linearity is the integration of (a)–(c): if cost is paid per intervention, bounded by per-intervention scope, and not amortized, then aggregate cost over a period is the per-period count multiplied by the per-intervention scope-bounded cost. The 100th intervention in a period costs the same as the 1st, modulo scope differences.

The four components together specify the cost-curve shape the architecture commits to on Dimension C. None of them is a claim about absolute cost levels.

## 4. The R/F tradeoff

Dimensions B and C are independent architectural axes — a deployment may exhibit any combination of rule variety R and intervention rate F — but they correlate inversely through deployment design. Tighter, well-designed rule coverage reduces intervention need because rules handle more of the situation space cells encounter; looser rule coverage increases intervention need because humans intervene more often to handle situations rules do not address. The deployment chooses where to place itself on this tradeoff.

Three operational considerations shape the choice. **Authoring-versus-intervention cost balance:** authoring more rules costs more on Dimension B; needing fewer interventions saves cost on Dimension C. Deployments with scarce override-authority humans favor more comprehensive rules; deployments with scarce rule-authoring expertise favor fewer rules and more direct override. **Domain stability:** stable, recurring-situation domains favor higher R and lower F because rules amortize across many subsequent cell executions; volatile, non-recurring-situation domains favor lower R and higher F because authoring rules in advance is less effective. **Authority structure:** broadly-distributed override authority absorbs aggregate F across many humans without bottlenecking, while concentrated authority may experience F as a bottleneck even at moderate aggregate F.

The architecture supports any (R, F) combination; the deployment designs its position on the tradeoff. This note takes no position on which combinations are preferable. The architectural commitment is to the cost-curve shape on each dimension, not to any specific (R, F) point.

## 5. Limitations and adjacent patterns

The commitment is not that intervention is cheap in absolute terms — a high-stakes override may take hours of evaluation, and the architectural commitment is to cost behavior rather than absolute levels. It does not constrain how F grows; F is a deployment design parameter, and the architecture specifies no minimum, maximum, or target. It does not claim all interventions are equally costly; per-intervention cost is bounded by scope, not equalized across scopes. And it does not claim intervention timing is predictable — timing depends on situations rules do not address, may cluster temporally, and may exhibit bursty patterns; F as a rate averages across the period the deployment uses.

Four adjacent cost patterns are commonly conflated with Dimension C.

**Not incident-response cost.** Incident response involves emergency procedures, on-call rotations, and incident-management tooling — overhead paid per incident regardless of whether an override is involved. Dimension C is about the normal exercise of override authority per the second governance moment, regardless of whether the override responds to an incident or to ordinary operational drift. A deployment that treats every override as an incident has converted per-intervention cost into per-incident cost.

**Not audit-cycle cost.** Some implementations conduct periodic audits in which interventions are batched, with audit-cycle costs paid per cycle. Audit cycles are operational concerns, not architectural governance moments. Dimension C measures the rate of overrides exercised at the moment they are needed, not the rate of audit cycles.

**Not escalation-process cost.** Some deployments run overrides through approval chains. Escalation-process costs grow with chain length and chain-management overhead. The architectural treatment of the override right rules out escalation as architectural precondition; deployments may add escalation as deployment-layer process, but the architectural cost commitment is per-intervention without escalation overhead.

**Not manual-review-queue cost.** Some implementations queue proposed interventions for batch review, with queue-management costs paid separately from per-intervention costs. The architectural commitment to direct override is exercise at the time the human chooses, not after queue processing.

## 6. Failure modes that violate the per-intervention cost property

Eight failure modes name common ways an implementation produces intervention-cost behavior that scales beyond per-intervention. None looks pathological at the local level; each is a small drift toward governance sophistication, audit rigor, or compliance overhead that adds up to a violated cost commitment.

**(a) Intervention cost growing with substrate scope.** The implementation requires interventions to consider all substrate content related to the override target — entities the changed entity references, decisions affected by the changed decision, rules cross-referencing the changed rule. Per-intervention cost grows with related-content volume and becomes effectively size-dependent.

**(b) Justification-required overrides.** The implementation requires a written rationale committed to substrate as a precondition of the override taking effect. Justification cost is paid per intervention beyond the human's evaluation effort. The override-right standalone note treats this as a violation of the right; it is also a violation of Dimension C.

**(c) Approval-gated overrides.** Each intervention flows through an approval chain before taking effect. Per-intervention cost grows with chain length and chain-management overhead, exceeding the human-effort bound the architecture commits to.

**(d) Audit-cycle batching of overrides.** Interventions are batched into audit cycles with per-cycle overhead (cycle scheduling, batch preparation, cross-batch coordination), making intervention cost effectively higher than the per-intervention bound.

**(e) Override scope amplification by infrastructure.** The infrastructure expands override scope automatically — overrides propagate to related substrate content, trigger downstream re-evaluations, cascade across cells reading affected substrate regions. Per-intervention cost grows with the amplification, not with the human's intent.

**(f) Override-tracking systems with per-override overhead.** Tracking infrastructure (logging, notification fan-out, audit-trail synthesis) imposes per-override overhead beyond the architectural provenance commitment, conflating tracking cost with intervention cost.

**(g) Escalation overhead per intervention.** Every intervention flows through escalation procedures as architectural precondition. This is the failure-mode form of the not-escalation-process distinction in §5; it is named separately because compliance-heavy deployments drift into it under the appearance of good practice.

**(h) Re-evaluation costs propagating from interventions.** After an intervention, the implementation re-evaluates rules, re-runs cells, or re-validates substrate state. Re-evaluation cost is paid per intervention, growing intervention cost beyond the human's evaluation and execution effort.

A system exhibiting any of (a)–(h) does not respect Dimension C's per-intervention cost property in the architectural sense, even when its absolute intervention cost is operationally acceptable.

## 7. Operational test

A deployment respects Dimension C's per-intervention cost property if and only if all of the following are true at all times during the substrate's existence.

1. Intervention cost is paid per intervention at the moment of exercise per the second governance moment, not amortized across substrate scope and not batched into cycles.
2. Per-intervention cost is bounded by the intervention's scope and the human's evaluation and execution effort, not by substrate size or by the volume of related substrate content.
3. Intervention cost is not amplified by architectural infrastructure beyond the human's evaluation and execution effort — no architectural justification, approval, escalation, queue, or re-evaluation overhead is paid as precondition of the override taking effect.
4. Aggregate intervention cost over a period grows linearly with F, not super-linearly.
5. Intervention cost is independent of cumulative intervention history — the 100th intervention costs the same human-effort as the 1st, modulo scope differences.

A deployment that fails any of (1)–(5) is not CKS-coherent on the intervention-frequency dimension, even if the modify and override rights are nominally satisfied and the absolute intervention cost is operationally acceptable. Such a deployment may be useful for other purposes; on Dimension C it has moved into a different architectural region, and downstream work that relies on its cost guarantees should be scoped accordingly.

## 8. Conclusion

Implementations under pressure to add governance sophistication, audit rigor, or compliance overhead consistently drift toward intervention costs that grow beyond per-intervention. The drift is steady because each addition — justification, approval, audit, tracking, escalation, re-evaluation — feels like good practice, and the per-intervention commitment seems abstract relative to the concrete value each addition appears to provide. The cumulative drift produces systems where intervention becomes operationally expensive: humans who hold override authority cannot exercise it freely because each exercise carries substantial overhead, and the architectural commitment to direct override becomes nominal even when the authority is technically present. The two-moment governance structure collapses into a hybrid where intervention has accreted the cost characteristics of design-time activity, and the architecture's claim to non-size-proportional governance fails on the intervention-time half.

Naming Dimension C as a standalone architectural commitment makes load-bearing connections explicit. Direct override as the second governance moment depends on per-intervention cost — the moment is operationally exercisable only because cost is paid at exercise time, bounded by human-effort, and not amplified by infrastructure. The override right's no-justification and at-the-time-of-choosing components depend on the same property. The two-moment governance structure depends on Dimension C's per-intervention behavior remaining cost-distinct from Dimension B's amortized rule cost. The labor allocation framework's per-task costs on Modes 2 (LLM-under-rule) and 3 (stable-cell automation) depend on direct override remaining a cost-additive overlay rather than a replacement, since the architecture supports human intervention in any mode when rules misfire. None of these dependencies survives if intervention cost is not held to the per-intervention bound.

Subsequent notes in the linear-cost-scaling decomposition specialize the workload axis as architecturally orthogonal and the size-independence-of-governance property as standalone; together with the notes on Dimensions A and B, they give the full operational decomposition of the linear-cost-scaling commitment. Subsequent work that adopts, extends, or argues against the CKS commitment on intervention-frequency cost should use Dimension C in the sense formalized here. Subsequent work that uses the term differently — most often by identifying intervention cost with incident-response or audit-cycle overhead, while leaving per-intervention boundedness and size-independence unconstrained — is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion derivation notes

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Linear-Cost Scaling: What Grows Linearly in CKS, What Doesn't, and Why.* 25 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Dimension C: Intervention-Frequency Cost as Standalone Architectural Treatment in the Coordination Knowledge Substrate Pattern.* 4 May 2026. ORCID: 0009-0004-8065-3235.
