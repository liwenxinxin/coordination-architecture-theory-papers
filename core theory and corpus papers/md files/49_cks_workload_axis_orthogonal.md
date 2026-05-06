# Workload Cost as Architecturally Orthogonal to Governance: Per-Cell-Execution Cost as the Fourth Cost Axis in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the workload axis as the fourth cost axis in the CKS linear-cost-scaling decomposition, with particular weight on the architectural orthogonality of workload cost to the three governance cost dimensions, so that downstream work can adopt or argue against the orthogonality claim without ambiguity.

## Abstract

The CKS linear-cost-scaling commitment (Claim 5, §6 of the source paper) decomposes into four independent cost axes: substrate size (Dimension A), rule variety (Dimension B), intervention frequency (Dimension C), and workload — the rate of cell executions and the per-execution cost incurred at that rate. Sibling derivation notes formalize the three governance dimensions as standalone architectural commitments. This note formalizes the workload axis as standalone, with particular weight on the architectural orthogonality of workload cost to the three governance dimensions: workload can grow without forcing governance growth, governance can grow without forcing workload growth, and the four axes are mutually independent. The note specifies what the workload axis measures, states the four-component orthogonality property, distinguishes workload cost from three adjacent cost patterns commonly conflated with it (per-element processing, per-rule execution overhead, full-substrate scanning), enumerates failure modes that violate the orthogonality property, and provides an operational test for whether a deployment's workload-cost behavior is CKS-coherent.

## 1. Why the workload axis needs standalone formalization

The CKS pattern's linear-cost commitment is defended in the source paper as Claim 5 (§6) and decomposed in the parent foundational note A1.06. The integrating-frame note A2.29 established that the decomposition has four cost axes, three of which carry governance cost (Dimensions A, B, C) and one of which carries workload cost. Sibling notes A2.30, A2.31, and A2.32 formalize the three governance dimensions. This note formalizes the fourth axis.

The motivating cases are deployments that need to assess how their costs respond to changes in deployment activity. Workload volume varies with deployment demand: more inputs to process, more events to respond to, more scheduled work to execute. The question of how this volume translates into operational cost — and how that cost responds independently of governance pattern choices — has no single locus in the source paper, because the workload axis is named explicitly only as the orthogonal quantity the linear-cost claim is *not* about (§6.1). The architectural commitments around workload cost are real and load-bearing, but they are stated in distributed form across §6, §6.3, §2.3, and §4.2. Without a standalone specification of the workload axis, deployments cannot reason about workload-versus-governance cost separately, and downstream implementations cannot defensibly claim CKS-coherence on the workload-cost axis.

A second motivation is the prior-art posture. The orthogonality property — workload and governance varying independently — forecloses architectures that couple workload and governance costs, and any "workload cost innovation" downstream can be evaluated against the specific architectural commitments to orthogonality and bounded per-cell cost.

A third motivation is the connection to the labor allocation framework formalized in A1.12. That framework names three modes (direct human, LLM under rule, stable-cell automation), each with different per-task cost characteristics. The workload axis is where these per-task costs aggregate at the deployment level as the execution rate grows.

## 2. What the workload axis measures

The workload axis measures the cost of cell execution in the deployment. The measurement has three operational components.

**Cell execution rate.** The number of cell executions per unit time. This rate grows with deployment demand: more inputs to process, more events to handle, more scheduled work to execute. The architecture commits to no specific level of execution rate.

**Per-cell-execution cost.** The cost of executing a single cell once. Per-cell-execution cost depends on three properties of the cell: its scope, per A2.09's bounded-scope commitment; its labor mode, per A1.12 (direct human in Mode 1, LLM under rule in Mode 2, stable-cell automation in Mode 3); and its specific computational characteristics — LLM token cost for Mode 2, code execution cost for Mode 3, human time for Mode 1. The architectural commitment is that per-cell-execution cost is bounded by cell scope, not by total substrate size.

**Cell-type distribution.** Different cell types in the deployment have different per-execution costs. Total workload cost is the sum across cell types of the execution rate of that type multiplied by its per-execution cost. The aggregate is what scales with deployment activity.

Workload grows in three patterns: demand growth, in which deployment demand drives execution rate up uniformly across cell types; cell-type expansion, in which the deployment adds new cell types to handle new situations; and cell complexity changes, in which existing cells become more sophisticated, with per-execution cost growing without execution rate changing. The architecture supports all three growth patterns. The commitment is to orthogonality with the three governance dimensions, not to specific workload behavior.

## 3. The orthogonality property

The architectural commitment is that the workload axis is orthogonal to Dimensions A, B, and C — meaning the four cost axes can vary independently. The orthogonality has four operational components.

**Workload–substrate-size orthogonality.** Workload can grow without substrate size growing; substrate size can grow without workload growing. A deployment can have small substrate with high cell-execution rate (frequent processing of compact state) or large substrate with low cell-execution rate (occasional processing of large state). The architectural foundation is A2.09's bounded-scope commitment: cells operating within bounded scope have per-execution cost bounded by scope, not by total substrate size. This is what makes workload independence from Dimension A operationally realizable.

**Workload–rule-variety orthogonality.** Workload can grow without rule variety growing; rule variety can grow without workload growing. A deployment can run many cell executions under a small rule set, or few cell executions under a large rule set. Per A2.31's amortization property, rule cost is paid at design time and amortizes across every cell execution thereafter; workload growth does not force rule growth, and rule growth does not force workload growth.

**Workload–intervention-frequency orthogonality.** Workload can grow without intervention frequency growing; intervention frequency can grow without workload growing. A deployment can run many cell executions with rare interventions (a well-ruled, high-throughput configuration) or few cell executions with frequent interventions (a loosely-ruled, low-throughput configuration). The architectural commitment is that intervention rate is a deployment design choice independent of cell-execution rate.

**Workload–aggregate-governance orthogonality.** The aggregate of governance cost (Dimensions A, B, and C taken together) varies independently of workload cost. A deployment with minimal governance and heavy workload has high workload cost and low governance cost; a deployment with rich governance and minimal workload has the opposite profile; deployments at any combination of the four axes are architecturally coherent. The commitment is that the four cost axes are mutually independent dimensions of the cost surface, not points on a single coupled curve.

Implementations that preserve these orthogonalities have flexibility to scale any axis without forcing changes in others; implementations that violate them produce coupling that constrains the deployment's operational choices and breaks cost-axis independence.

## 4. What the workload axis does not claim

The orthogonality commitment is precise about what the workload axis *is*. It is equally important to state what it is not, both as scope-limits on the claim itself and as distinctions from adjacent cost patterns commonly conflated with workload cost.

**Scope limits on the claim.** The workload axis does not claim that workload cost is bounded in absolute terms; workload can grow without bound as deployment demand grows. It does not claim that all cells have similar per-execution cost or that cost is predictable; cells vary widely depending on scope, labor mode, and computational characteristics, and per-execution cost may vary with inputs, runtime conditions, or LLM non-determinism. It does not constrain how the execution rate grows; deployments choose how to scale workload, and the architecture specifies no target. It does not claim that workload cost is cheap in absolute terms. It does not claim that workload is independent of substrate content's complexity or distribution; cells operate on substrate content, and content's nature affects what cells must do. The commitment is to architectural independence from governance cost dimensions, not to absolute workload behavior.

**Not per-element processing cost.** Per-element processing has cost that grows with substrate size — for each substrate element, perform processing. The workload axis depends on cell execution rate, with per-cell cost bounded by cell scope per A2.09. Per-element processing within unbounded scope is a violation of A2.09 and produces cost that scales with substrate size, not with workload as defined here.

**Not per-rule overhead in execution.** Some implementations pay per-rule overhead at every cell execution, with per-execution cost growing with rule variety per execution. Per A2.31's amortization property, rule cost is paid at design time, not per execution; per-rule overhead at execution time violates the amortization. Workload cost is the cost of executing a cell within its bounded scope under whatever rules govern it, with the rules having been authored at design time and amortized across all subsequent executions.

**Not full-substrate scanning costs.** Some patterns have cells that scan the entire substrate as part of execution, with per-execution cost growing with substrate size. This violates A2.09's bounded-scope commitment and Dimension A's size-independence guarantee. Cells operating in CKS-coherent way have bounded scope, and per-execution cost is bounded by scope rather than by total substrate size.

## 5. Why the workload axis is load-bearing for downstream commitments

The workload axis carries several CKS commitments. The bounded-scope commitment for cells (A2.09) depends on per-cell-execution cost being bounded by cell scope rather than by total substrate size; the workload axis is where this bounded cost accumulates at the deployment level, and the orthogonality property depends on cells respecting bounded scope.

The labor allocation framework (A1.12) names three modes with different per-task cost characteristics. The workload axis aggregates these per-task costs across cell executions; the framework's economic value depends on per-task costs being bounded and the modes being amortized at design time (Modes 2 and 3) or appropriately costly per execution (Mode 1).

The size-independence guarantee on Dimension A (A2.30) depends on cells respecting bounded scope. If cells operated over unbounded scope, workload cost would scale with substrate size indirectly — through per-execution scans of growing state — breaking Dimension A's guarantee. The workload axis is what carries Dimension A's commitment at the operational layer.

The cross-claim spine articulated in A1.06 commits to the four cost axes being independent. The workload axis's orthogonality with the three governance dimensions is what makes this independence operational at runtime, and it is also what keeps governance architectural rather than procedural per A2.06: workload changes do not force governance procedure changes, and governance is exercised at the two non-size-proportional moments (rule authoring, direct override) that the human-governed commitment names.

## 6. Failure modes that violate workload orthogonality

Eight anti-patterns illustrate how an implementation can produce workload cost coupled with one or more governance dimensions.

(a) **Workload-driven substrate-size coupling.** Cells whose per-execution cost grows with cumulative substrate size, typically through per-execution scans of growing state. Substrate growing as workload writes content is normal; per-execution cost growing with the cumulative substrate is the failure mode and breaks workload–N orthogonality.

(b) **Workload-driven rule-variety coupling.** The architecture forces new rule authoring as workload patterns change, with rule variety growing as a function of workload. Adding rules to handle new situations remains a deployment design choice; the failure mode is when the architecture forces additions per workload pattern, removing that choice.

(c) **Workload-driven intervention-frequency coupling.** The architecture requires interventions per workload threshold (for example, one intervention per N cell executions), causing intervention frequency to grow with workload. Intervention frequency may correlate with deployment activity in practice; the failure mode is the architecture enforcing the coupling rather than letting deployments manage rule-variety/intervention-frequency tradeoffs independently.

(d) **Per-execution rule overhead.** Cells pay per-rule overhead at execution time, with per-cell cost growing with rule variety per execution. This is Dimension B amortization failure (per A2.31), but it manifests as workload cost growing with rule variety, violating workload–rule-variety orthogonality.

(e) **Per-execution governance overhead.** Cells pay per-execution governance cost — justification, approval gates, audit log generation — for each execution, with per-cell cost growing with governance pattern complexity. This violates workload orthogonality with the aggregate governance dimensions and is among the most common drift patterns in compliance-oriented deployments, where governance features are implemented as runtime gates rather than as authority-architecture properties.

(f) **Per-execution intervention cost.** Cells pay per-execution cost related to historical intervention frequency, with workload cost growing with cumulative intervention count. This violates workload–intervention-frequency orthogonality and Dimension C's per-intervention cost property simultaneously.

(g) **Workload-driven authority changes.** The architecture requires authority structure changes as workload scales (for example, more humans needed for governance as execution rate grows). Distributing authority across humans is a deployment choice; the failure mode is the architecture forcing authority scaling with workload.

(h) **Cross-cell coordination scaling with workload.** Cells coordinate through substrate per A2.12 (no direct channels between cells). Per-cell coordination is architecturally fine; the failure mode is when coordination cost grows with cumulative cell interactions across the deployment, exceeding the per-cell scope budget that A2.09 commits to.

A deployment that exhibits any of (a)–(h) does not preserve the workload axis's orthogonality property in the architectural sense, even if its absolute costs are acceptable.

## 7. Operational test, and why naming the axis as standalone matters

A deployment respects the workload axis's orthogonality property if and only if all of the following are true at all times during the substrate's existence.

1. Per-cell-execution cost is bounded by the cell's scope per A2.09, not by total substrate size or by cumulative workload history.

2. Workload growth does not architecturally force growth in rule variety, intervention frequency, or substrate size; the deployment retains design choice on each governance dimension independent of workload.

3. Governance pattern changes do not architecturally force growth in workload; the deployment retains operational choice on workload independent of governance.

4. Per-cell-execution cost includes only the cell's own execution work — computation, LLM operations, human labor under the cell's labor mode — and does not include per-rule overhead at execution time, per-element scanning beyond cell scope, or per-intervention processing.

5. The four cost axes (substrate size, rule variety, intervention frequency, workload) are independent in the deployment's actual cost behavior; varying one does not architecturally couple to varying others.

A deployment that fails any of (1)–(5) does not respect the workload axis's orthogonality property in the architectural sense. It may be a useful deployment, and it may be cost-effective in some absolute sense, but it has moved into a different architectural region on the workload-cost axis.

Implementations under pressure to simplify cost modeling, optimize for specific deployment patterns, or add governance-compliance features consistently drift toward coupling workload cost with governance dimensions. Coupled patterns appear architecturally simpler, and modern operational systems often default to coupled cost models — particularly in compliance-oriented contexts where governance is implemented as runtime gates rather than as authority architecture. The drift produces systems where deployment-design choices on one axis constrain choices on others: a deployment cannot scale workload without simultaneously expanding governance, or cannot reduce intervention frequency without simultaneously reducing workload.

Naming the workload axis as a standalone architectural commitment gives downstream implementers a precise specification of what cost behavior CKS commits to on this axis. With this note complete, the four cost axes are fully formalized as standalone dimensions in the linear-cost-scaling decomposition; the subsequent note specializes the size-independence-of-governance property as a standalone architectural commitment, completing the decomposition.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Workload Cost as Architecturally Orthogonal to Governance: Per-Cell-Execution Cost as the Fourth Cost Axis in CKS.* May 4, 2026. ORCID: 0009-0004-8065-3235.
