# Cell-Level Conflict Resolution Under Orchestration Rules as Standalone Architectural Commitment in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 2 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one of the two levels of conflict handling named in the source paper's "conflict-preserving" commitment — **cell-level resolution under orchestration rules** — as a standalone architectural commitment with independent operational content, separable from the substrate-level preservation mechanism with which it composes.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern's "conflict-preserving" commitment names two levels of conflict handling — substrate-level preservation and cell-level resolution under orchestration rules — as jointly necessary for the architectural property the term carries. A separate note formalizes the substrate-level half. This note formalizes the cell-level half as having independent operational content that can be defended, implemented, and tested independently of substrate-level preservation. The motivation is concrete: cell designs must be evaluatable for compliance with resolution requirements, orchestration rules audited for resolution-handling completeness, and cells reused across deployments where the substrate-level preservation regime varies. Cell-level resolution is also the half most often misread as autonomous-agent decision-making, which the architecture forbids at the cell layer. The note states what cell-level resolution requires of cells (response determined by orchestration rules, resolution decision recorded as substrate content, no modification of underlying contradicting content, full provenance, subjection to subsequent resolution), distinguishes the commitment from four adjacent technical patterns commonly conflated with it (autonomous-agent decision-making, configuration-driven selection logic, hardcoded resolution policies, machine-learning-based preference inference), enumerates the failure modes that violate it, and provides an operational test for whether a system implements cell-level resolution separable from substrate-level preservation.

## 1. Why cell-level resolution needs to be formalized as standalone

The CKS pattern's "conflict-preserving" commitment names two levels of handling together: substrate-level preservation, in which contradictions persist as substrate state by default and are never collapsed by automated processes; and cell-level resolution, in which cells executing over substrate content with active contradictions resolve them according to human-authored orchestration rules, recording the resolution decisions as additional substrate content rather than as mutations of the underlying contradicting content (§5.3 of the source paper). A separate derivation note formalizes the substrate-level half. This note formalizes the cell-level half as having independent architectural content.

Three motivating cases make the standalone treatment necessary. First, deployments routinely require cell-level resolution to be evaluatable on its own terms: cell designs reviewed for compliance with the resolution requirements, orchestration rules audited for completeness across the contradictions cells will encounter, and cells reused across deployments where the cell's resolution behavior travels with the cell.

Second, cell-level resolution is the half most often misread as autonomous-agent decision-making. The dominant 2024–2026 pattern in agent infrastructure — agents that "decide what to do" through emergent LLM behavior — looks superficially like cell-level resolution but resolves the architectural relationship between rules, cells, and resolution decisions in a different way. CKS commits cells to rule-governed response, not autonomous decision-making.

Third, derivations of CKS focused on conflict-handling mechanisms — specific resolution algorithms, conflict-detection patterns, escalation flows — are more defensibly contestable as prior art when cell-level resolution is publicly formalized as standalone, because any "conflict resolution innovation" can then be evaluated against the rule-governed-resolution commitment.

## 2. The cell-level resolution commitment, defined precisely

In the CKS pattern, a cell satisfies **cell-level conflict resolution** if and only if all of the following five components hold during the cell's execution.

**(a) The cell's response to contradicting substrate content is determined by orchestration rules.** When the cell encounters contradicting substrate content, the response — whether to resolve to one position, escalate to a human, defer execution, refuse to act, or take any other specified action — is determined by an orchestration rule humans authored at design time (§3.3, §5.3). The cell does not exercise judgment about contradiction handling outside what rules specify. Cells whose mediator role is filled by an LLM (per A1.04) may use the LLM to *execute* the resolution under the rule's constraints, but the *governance* of the response is the rule, not the LLM's judgment outside the rule.

**(b) The resolution decision is recorded as substrate content.** When the rule's specified response is resolution rather than escalation, deferral, or refusal, the cell does not silently proceed under one interpretation while ignoring the other. It produces a substrate write recording its position on the contradiction, the rule under which the position was taken, and the antecedent contradicting content the position addressed (§5.3, §11.3).

**(c) The resolution decision does not modify the underlying contradicting substrate content.** The cell writes its resolution as new substrate content; the original contradicting pieces remain in the substrate, where the substrate-level preservation commitment continues to carry them (per A2.13). The substrate after the resolution carries the contradiction, the resolution decision, and the relationship between them as three distinct elements.

**(d) The resolution decision carries provenance.** The cell's identity, the orchestration rule applied, the timestamp, the antecedent reference, and (where the rule requires) the rationale are recorded as substrate metadata for the resolution decision, on the same terms as any other governed substrate content (§3.1, A1.07; the four-field treatment is the subject of A2.16).

**(e) The resolution decision is itself subject to subsequent resolution.** Because the resolution is substrate content, later cells encountering the same contradicting content may, under their own rules, take different positions — producing further substrate content recording the subsequent decisions. The substrate accumulates resolution history; the architecture does not commit to any single resolution being final.

The five components together define what cell-level resolution requires architecturally. A cell satisfying fewer than five performs resolution in some other useful sense, but is not CKS-coherent on this axis.

## 3. What cell-level resolution does NOT require

Stating precisely what the commitment does not require is what keeps the standalone framing from drifting into something stronger than the source paper supports.

**It does not require resolution.** Orchestration rules may specify non-resolution responses — escalation, deferral, refusal under specified conditions. Each is fully CKS-coherent. What the commitment requires is that the response is rule-governed, not that it is resolution.

**It does not require any specific resolution algorithm.** Rules may specify resolution by recency, writer authority, external lookup, LLM judgment under constraints, voting, or any other mechanism the rule's authors chose. The commitment is to rule-governance, not algorithm specification.

**It does not require LLM mediation.** Deterministic cells running under rules can perform cell-level resolution; cells with LLM mediators can also perform it. The commitment is independent of whether an LLM is involved.

**It does not require full visibility into all related contradictions.** The cell encounters contradictions within its bounded scope (per A2.09); it resolves under rules within that scope. Contradictions outside the cell's scope are handled by other cells or by humans.

**It does not require resolutions to be consistent across cells.** Different cells with different rules may resolve the same substrate-level contradiction differently. This is permitted, and itself produces substrate state humans can inspect and govern. The architecture commits to each resolution being rule-governed and traceable, not to global consistency.

**It does not require resolutions to be permanent.** Resolution decisions are substrate content subject to the three rights named in A1.01; humans with override authority can modify or reverse them, and subsequent cells under different rules can produce different resolutions of the same contradiction.

## 4. What cell-level resolution is NOT

Four adjacent technical patterns are commonly conflated with cell-level resolution. Each is reasonable in some other architectural context; in CKS, each violates a load-bearing commitment.

**Not autonomous-agent decision-making.** This is by far the most consequential conflation in current AI infrastructure. Autonomous agents in the dominant 2024–2026 idiom respond to inputs through emergent behavior driven by goals, plans, and reasoning that are not fully traceable to specific rules: the agent "decides what to do" about contradictions encountered during execution, with the deciding authority sitting in the agent's reasoning rather than in a substrate-resident artifact. The CKS cell does not operate this way. Its responses to contradictions are determined by orchestration rules humans authored at design time; the rule is the deciding authority, the cell applies the rule. An LLM mediator inside the cell may execute the application — reading the rule, reading the contradicting content, producing the resolution text under the rule's constraints — but the LLM is not the decider; it is the executor of a decision the rule already specifies. Implementations that grant emergent LLM behavior the role of deciding what to do about contradictions, even when the behavior produces reasonable results, have located the deciding authority outside the substrate, where it cannot be inspected, modified, or overridden through the rights A1.01 commits to. The mismatch is not about whether the LLM is involved or whether reasoning happens; it is about where the authority for the response sits.

**Not configuration-driven selection logic.** Configuration-driven systems often resolve contradictions through deployment configurations that determine which version wins (priority rules, source rankings, freshness thresholds). These configurations may be human-authored, but the commitment in CKS is different: orchestration rules are *substrate content* (per §2.1, §2.3 and A2.04), governable on the same terms as other substrate content. A configuration file held outside the substrate as a deployment parameter is not an orchestration rule in the architectural sense.

**Not hardcoded resolution policies.** Some implementations encode resolution policies directly in cell code — always prefer newer, always prefer human-authored, always escalate. Hardcoded policies violate the rule-as-substrate-content commitment: the policy is in code, not in substrate, and is not governable through the inspect/modify/override rights or part of the path-retraceability vocabulary. Cell code may implement resolution mechanics; the policy that determines which mechanics apply must live in substrate-resident orchestration rules.

**Not machine-learning-based preference inference.** Some implementations train ML models to predict resolution preferences from past resolution patterns. The learned model is a parametric representation of inferred preferences, not a human-authored governable rule. ML models can be used as adjacent components within cells (per A1.16), but the cell's resolution behavior must be governed by orchestration rules in the substrate, not by the model's inferred preferences.

## 5. Why cell-level resolution is load-bearing for downstream commitments

Cell-level resolution is load-bearing for five other CKS commitments.

**Two-level coupling (A2.15, planned).** The two-level handling pattern requires both halves. If cell-level resolution is silently applied — without rule governance, without provenance — the coupling collapses into a one-level architecture in which the cell becomes the resolution authority, a configuration the architecture does not permit.

**Path retraceability (A1.07).** When cells resolve contradictions under rules with full provenance, the resolution decisions become traceable substrate content with antecedent references to the contradictions resolved. Without this, the trace is broken at exactly the points where coordination consequence accumulates.

**Human-governed (A1.01).** Cell-level resolution operationalizes human governance at the execution layer: cells respond under rules humans authored, and humans retain override authority over both the rules and the resolution decisions. Silent or autonomous cell behavior bypasses this governance regardless of how robustly the substrate is governed elsewhere.

**Source-of-truth (A1.08).** Resolution decisions are part of the substrate's authoritative state — what was decided about each contradiction, by which cell, under which rule, is queryable substrate content. Without recording these decisions, the substrate's source-of-truth property fails for coordination questions involving contradictions.

**Conflict-as-first-class (A1.03).** The parent commitment requires that contradictions be first-class objects whose handling is itself first-class. Cell-level resolution makes the handling visible: each resolution decision is substrate content, addressable, traceable, and itself governable. Without it, contradictions are first-class but their handling is not.

## 6. Failure modes that violate cell-level resolution

A system can fail cell-level resolution specifically, even when substrate-level preservation is robustly in place. Seven failure modes name the most common ways this happens.

**(a) Silent resolution by LLM judgment.** When an LLM mediator within a cell encounters contradicting substrate content and proceeds with one interpretation through emergent judgment — without an orchestration rule specifying the response, without recording the decision as substrate content — the cell has resolved silently. This is the most subtle failure mode in CKS implementations: the substrate's preservation may remain entirely correct while cells silently resolve, producing an architecture compliant on the substrate side and failing on the response side.

**(b) Hardcoded resolution policies.** When cells handle contradictions through policies encoded in cell code rather than in orchestration rules, the resolution sits outside the architecture's authority structure and is not governable through the rights applied to substrate content.

**(c) Configuration-driven resolution.** When cells handle contradictions through deployment configurations rather than substrate-resident orchestration rules, the configuration is not subject to the architectural rights and lacks provenance metadata. The mechanism may be human-controlled at deployment time; it is not architectural governance.

**(d) Resolution without provenance recording.** When cells resolve contradictions according to orchestration rules but fail to record the decision with full provenance — writer, rule reference, timestamp, antecedent reference, rationale where required — the resolution becomes invisible to downstream retraceability. The cell may have followed the rule; the trace through the resolution is broken.

**(e) Resolution by overwrite.** When cells resolve contradictions by modifying the underlying contradicting substrate content — deleting the rejected piece, marking it superseded in a way that hides it from substrate readers — the substrate-level preservation commitment treated in A2.13 is violated. The cell has crossed from cell-level resolution into substrate-level modification.

**(f) Resolution treated as final.** When the architecture treats a cell's resolution as definitive — preventing subsequent cells from revisiting the contradiction under their own rules, or preventing humans with override authority from reversing it — the commitment to resolutions being substrate content (and thus subject to the three rights) is violated.

**(g) Resolution by ML-based preference inference.** When cells resolve contradictions through ML models that predict preferred resolutions from training data, the resolution is governed by the model's inferred preferences rather than by orchestration rules. The model may be useful as an adjacent component; it cannot be the resolution authority because its inferred preferences are not substrate-resident, human-authored rules.

A system exhibiting any of (a)–(g) does not implement cell-level resolution as the source paper commits to it, and naming the failure precisely is what allows downstream remediation.

## 7. Operational test

A cell satisfies cell-level conflict resolution if and only if all of the following are true at all times during the cell's execution:

1. The cell's response to contradicting substrate content is determined by an orchestration rule that humans authored and that lives as substrate content.
2. When the rule's specified response is resolution, the resolution decision is recorded as substrate content with full provenance (writer, rule reference, timestamp, antecedent reference, rationale where applicable).
3. The resolution decision does not modify the underlying contradicting substrate content; the substrate continues to carry the contradiction per A2.13.
4. The cell does not exercise judgment about contradiction handling outside what orchestration rules specify; if the rule does not address the contradiction directly, the cell's response is whatever the rule's default specifies, which may be escalation, deferral, or refusal.
5. Resolution decisions are themselves substrate content subject to the three rights — humans can inspect, modify, override — and subject to subsequent resolution by other cells under their own rules.

A cell that fails any of (1)–(5) does not satisfy cell-level resolution in the architectural sense, even when the failure happens through reasonable-seeming mechanisms.

## 8. Conclusion

Implementations under pressure to provide "smart" or "autonomous" cell behavior consistently drift toward LLM-judgment-driven resolution, because LLM judgment is flexible, low-friction, and aligned with the dominant agent-framework patterns of current AI infrastructure. The cell-level resolution commitment requires architectural discipline against this drift: cells respond under rules, and the rules — not the LLM — are the authority. The LLM may execute the rule's application; it does not replace the rule.

The drift produces a particularly subtle failure mode. A substrate may preserve contradictions correctly, satisfying every component of the substrate-level commitment formalized in A2.13; but if cells silently resolve them in ways that bypass the rule layer and skip provenance recording, the contradictions are preserved in state while the system's responses to them are ungoverned. The architecture appears to satisfy conflict-as-first-class at the substrate level while failing at the response level where cells actually operate. Naming cell-level resolution as standalone — with the components and distinctions specified above — is what allows that failure mode to be named and remediated.

Together with A2.13, this note decomposes the joint conflict-handling commitment into independently testable architectural content. Subsequent work that adopts, extends, composes, or argues against cell-level resolution should use the term in the sense formalized here; subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cell-Level Conflict Resolution Under Orchestration Rules as Standalone Architectural Commitment in the Coordination Knowledge Substrate Pattern.* 2 May 2026. ORCID: 0009-0004-8065-3235.
