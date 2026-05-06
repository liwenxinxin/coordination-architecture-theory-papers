# The Linear-Cost Scaling Commitment: Full Operational Treatment of Cost Dimensions and the Size-Independence Guarantee in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the four-dimension cost structure and the size-independence-of-governance guarantee that together carry the source paper's linear-cost scaling commitment (Claim 5; §6, §6.1, §6.2, §6.3), establishing the integrating frame within which subsequent notes specialize each cost dimension and the size-independence property as standalone derivations.

## Abstract

The CKS pattern's fifth commitment is that costs scale in a specific way: governance cost does not grow with substrate size, and the four dimensions along which costs do grow are deployment-controllable rather than emergent from substrate accumulation. This note formalizes that commitment as an integrating frame. It identifies the four cost dimensions the architecture specifies (substrate size N, rule variety R, intervention frequency F, workload W); states the size-independence-of-governance guarantee precisely as the load-bearing claim; distinguishes what the commitment does and does not say (it does not claim absolute cost levels, predictability, or that all four dimensions scale linearly); describes the architectural relationships among the dimensions (independence as commitment, correlation as deployment pattern); enumerates seven failure modes by which an implementation can produce N-coupled cost growth; and provides an operational test for whether a system satisfies the commitment in the architectural sense. Subsequent notes specialize each dimension (A2.30–A2.33) and the size-independence property (A2.34) as standalone derivations; this note is the integrating frame within which those specializations sit.

## 1. Why the cost-scaling commitment needs to be formalized as standalone

The parent foundational note A1.06 commits the CKS pattern to linear-cost scaling as Claim 5 of the source paper. That commitment is the architectural reason a CKS deployment can be operated at substrate sizes that would be infeasible under size-coupled governance designs. The commitment is also the most easily misread of the six pattern commitments: read as a claim about absolute cost levels, it overstates; read as a claim that all costs are constant in substrate size, it overstates differently; read as a single cost property rather than a four-dimension surface, it underspecifies.

Three motivations make the integrating-frame treatment necessary. First, operational planning: a deployment forecasting cost over months and years needs to ask the four-dimension questions independently — how cost responds to substrate accumulation, to rule additions, to intervention patterns, to throughput growth — and the answers diverge in ways the single phrase "linear-cost" obscures. Second, prior-art posture: patentable derivations focused on cost-scaling, governance-cost amortization, or size-independent governance are substantively more defensibly contested when the four-dimension structure is publicly formalized as standalone. Third, operational diagnosis: cost-growth surprises typically trace to a specific dimension that grew unexpectedly, and the integrating frame makes the diagnostic structure explicit instead of leaving it implicit in §6 of the source paper.

## 2. The four cost dimensions

The architecture identifies four dimensions along which cost in a CKS deployment grows. Each is operationally distinct; together they specify the cost surface.

**Dimension A — Substrate size (N).** The total volume of substrate content the deployment maintains, in whatever unit the host environment supports (rows, records, documents, fields, bytes). N grows over a deployment's lifetime as decisions are recorded, conflicts preserved, rules accumulated, and prior content retained for path retraceability. Full operational treatment: A2.30.

**Dimension B — Rule variety (R).** The number of distinct orchestration rules the deployment maintains, weighted by authoring complexity. R grows as deployments author rules to handle new situations, refine existing rules, or extend coverage to new domains. Full operational treatment: A2.31.

**Dimension C — Intervention frequency (F).** The rate at which humans exercise direct override over substrate content or orchestration rules per unit time. Tightly-ruled deployments with comprehensive coverage have low F; loosely-ruled deployments where rules cover less of the situation space have higher F. Full operational treatment: A2.32.

**Workload axis — Cell execution volume (W).** The rate at which cells execute per unit time. W reflects deployment demand — how often the deployment processes inputs, responds to events, or executes scheduled work. Full operational treatment: A2.33.

The four dimensions are architecturally independent: a deployment can occupy any position on each axis without architectural constraint from the others. Total cost is approximately C(N, R, F, W); the architectural commitment is to specific properties of how that function responds to changes in each input. The substantive properties — particularly the response to N — are the subject of §3.

## 3. The size-independence guarantee

The load-bearing claim of A1.06 is that governance cost is independent of substrate size. This is the property that makes the architecture defensible at scale.

**(a) Rule-authoring cost grows with R, not with N.** A rule authored for a substrate of size 1,000 has the same architectural authoring cost as a rule authored for a substrate of size 1,000,000. The work of writing a rule depends on the rule's behavioral content, not on the volume of substrate over which it will be applied. Rule authoring is paid per rule and amortized across all subsequent cell executions to which the rule applies — the property §6.3 of the source paper carries when it commits rule-authoring cost as paid once per rule, not once per element governed.

**(b) Direct-override cost grows with F, not with N.** Per-intervention cost is independent of substrate size; total intervention cost over a time period is F times the per-intervention cost. Substrate size enters per-intervention cost only through whatever bounded scope the intervention specifically touches, not through the full size of the substrate the intervention sits within.

**(c) Workload cost grows with W and per-cell scope, not with full N.** A cell's execution cost depends on its computational complexity, the substrate scope it reads and writes, and the LLM calls it makes — but the bounded-scope commitment of A2.09 means this cost does not grow with full substrate size. A cell operating on a bounded slice has cost bounded by that slice, regardless of how much other substrate exists.

**(d) Total governance cost is bounded by R and F, not by N.** Because rule-authoring cost is governed by R, direct-override cost by F, and N enters neither, total governance cost is bounded by deployment-design parameters rather than by substrate-size growth which the deployment cannot architecturally bound. Full standalone treatment: A2.34.

The architectural significance is structural. Substrate size grows as deployments operate; deployments cannot bound N below a threshold without sacrificing the substrate's role as source of truth. What deployments can bound is R and F — both deployment-design choices. A commitment that governance cost depends only on the bounded-controllable dimensions is what makes the architecture defensible at scales where N is unbounded.

## 4. What the cost-scaling commitment does NOT claim

The commitment is precise, and stating what it does not claim is what keeps the integrating frame from being read as something stronger than the source paper supports.

**It does not claim absolute cost advantage.** The architecture does not commit to CKS deployments being cheaper in absolute terms than non-CKS alternatives. A CKS deployment with high R, F, and W may have substantial absolute cost; what the architecture commits to is the scaling behavior — that doubling N does not double the cost — not the absolute level.

**It does not claim cost is constant in N.** The architectural commitment is to the governance component being independent of N. Workload cost may have small dependencies on N if cells need to scan portions of substrate during execution, but A2.09's bounded-scope commitment keeps such dependencies bounded by the cell's scope, not by full substrate size. Storage cost is N-proportional in any honest accounting; the commitment is about active operational costs, not storage.

**It does not claim all four dimensions scale linearly.** The "linear-cost" framing is shorthand for the size-independence-of-governance property, not for linear scaling on every axis. R may grow in step changes, F may spike under operational stress, W may grow as deployment demand grows. The architecture does not constrain how each dimension grows; it commits to the relationship of each dimension to N (no coupling) and the architectural independence of the four dimensions from each other.

**It does not claim cost is predictable for any specific deployment.** Predictability depends on deployment design, governance pattern, and workload characteristics. The architectural commitment is to the relationships among dimensions, not to specific cost levels.

**It does not claim workload is bounded.** Workload can grow without bound as deployment demand grows; the commitment is to workload being independent of N, not to workload itself being bounded.

## 5. The architectural relationships among dimensions

The four dimensions are architecturally independent — each can vary without the others varying — but they may correlate in deployment practice. The integrating-frame treatment names the architectural commitment to independence, while observing that correlations are deployment-design properties rather than architectural ones.

**N and R may correlate.** As substrate size grows, deployments may author additional rules to handle the wider variety of situations a larger substrate represents. The architecture does not require this: some deployments hold R nearly constant as N grows over years. R growth, when it occurs, is the deployment's design choice, not architecturally forced by N growth.

**N and F may correlate.** As substrate size grows, the absolute number of interventions per unit time may grow if the rate per substrate unit stays constant. But F depends on intervention triggers and rule coverage, not on substrate size directly. Tightly-ruled deployments hold F nearly constant as N grows.

**R and F may inversely correlate.** Tighter rule coverage (high R, well-designed) reduces intervention need; looser coverage increases it. This is a deployment-design tradeoff: invest in rule authoring once to reduce intervention frequency thereafter, or keep authoring minimal and accept higher intervention frequency.

**W and N are architecturally independent.** Workload reflects demand; substrate size reflects accumulated content. A deployment can have small substrate and high workload (frequent processing of small state) or large substrate and low workload (occasional processing of large accumulated state). Neither configuration is architecturally favored.

**W and R may correlate.** More cell variety may produce more cell executions; but cell variety and cell execution rate are distinct, and the architecture supports decoupling them.

The architectural commitments — particularly the size-independence of governance — hold whether or not these correlations occur in any specific deployment.

## 6. Failure modes that violate the cost-scaling commitment

A system can violate the linear-cost scaling commitment in several distinct ways. Each anti-pattern names a way an implementation can produce cost scaling that couples to N when the architecture commits to independence.

**(a) Per-element governance.** A governance action — review, approval, validation — is required per piece of substrate content. Governance cost grows with N, breaking the size-independence guarantee directly. This is the most common failure mode and the one §3.3 of the source paper most directly preempts.

**(b) Substrate-size-dependent rule application.** Rules apply per element across the entire substrate during cell execution, with the cell's per-execution cost growing with N. This violates A2.09's bounded-scope commitment, which the cost commitment depends on.

**(c) Rule re-validation per cell execution.** Each cell execution re-validates orchestration rules against substrate state, with validation cost growing with N. The amortization property of rule authoring is broken; rule cost is re-paid per execution and grows with N indirectly.

**(d) Intervention-cost amplification by N.** Interventions are required to consider all substrate content, with per-intervention cost growing with N. The override right's at-the-time-of-choosing component is operationally compromised because intervention cost becomes prohibitive at scale, even when the right is nominally preserved.

**(e) Schema-migration costs scaling with N.** Substrate schema changes are propagated to all existing substrate content as ongoing rather than one-time governance, with migration cost growing with N. A one-time migration cost may be acceptable; treating schema change as ongoing N-scanning work violates the commitment.

**(f) Audit costs scaling with N.** Audits are required to scan all substrate content. The architectural commitment to path-retraceability does not require N-scanning audits; if a deployment treats N-scanning audit cost as architectural, the commitment is violated.

**(g) Authority-revocation costs scaling with N.** Authority changes — revoking modify rights, transferring override authority — are propagated through all substrate content. The architectural commitment to authority being a property of the architecture rather than a per-element annotation does not require this propagation; if a deployment requires it, the commitment is violated.

A system exhibiting any of (a)–(g) does not satisfy the architectural cost commitment, even if absolute cost is acceptable for current scale. Failure modes are diagnosed by their N-coupling, not by their current cost magnitude.

## 7. Operational test

A CKS deployment respects the linear-cost scaling commitment if and only if all of the following are true.

1. Governance cost — the sum of rule-authoring cost and direct-override cost — does not grow with substrate size N. Doubling N does not double governance cost.
2. Rule-authoring cost grows with R (rule variety and complexity), not with N.
3. Direct-override cost grows with F (intervention frequency), not with N.
4. Workload cost grows with W (cell execution volume) and may depend on per-cell scope, but does not grow with full substrate size beyond the bounded scope per A2.09.
5. The four cost dimensions are architecturally independent: growth in one does not architecturally force growth in any of the others, even when deployment patterns exhibit correlations among them.

A deployment that fails any of (1)–(5) does not satisfy the linear-cost scaling commitment in the architectural sense, even if its absolute cost is acceptable at current scale. A system that fails (1) at small scale will fail it more visibly at large scale, but the architectural failure is present from the moment of construction, not from the moment its consequences become operationally painful.

## 8. Why the integrating frame matters

Implementations under pressure to deliver governance, audit, or compliance features consistently drift toward features that scale with N. The drift is steady because N-scanning features are technically straightforward — familiar from database, ETL, and analytics systems where N-scanning is the normal way of doing business — and because each individual N-scanning feature appears modest in isolation. The architectural commitment to size-independence is what each such feature erodes, but the erosion happens one feature at a time, often without anyone observing the trajectory.

Implementations that drift away from the linear-cost commitment produce systems that work at small substrate sizes but become operationally infeasible as substrate accumulates. The downstream consequences manifest as scaling crises: review backlogs that grow faster than reviewers can work through them, audit costs that become prohibitive, intervention costs that prevent humans from exercising override authority at scale, schema-change paralysis. Each crisis traces back to a cost dimension that was allowed to scale with N when the architecture committed to independence; the crises are typically diagnosed only when N is already too large for any of the available remediations to be cheap.

Naming the four-dimension cost structure and the size-independence guarantee as a standalone integrating frame gives downstream implementers a precise specification of what cost-scaling CKS commits to. Each failure mode is detectable by structure rather than by symptom; each cost dimension is independently characterizable; each architectural relationship is independently testable. Subsequent notes A2.30–A2.34 specialize each dimension and the size-independence property as standalone derivations; together with this integrating frame, they give the full operational decomposition of A1.06's commitment. Subsequent work that adopts the CKS cost-scaling commitment, extends it, composes it with adjacent patterns, or argues against it should use the four-dimension cost structure and the size-independence-of-governance guarantee in the sense formalized here. Subsequent work that uses a different cost model is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Linear-Cost Scaling Commitment: Full Operational Treatment of Cost Dimensions and the Size-Independence Guarantee in the Coordination Knowledge Substrate Pattern.* May 4, 2026. ORCID: 0009-0004-8065-3235.
