# Anti-Pattern: Workflow-Approval-Gated Governance — A Standalone Formalization of the Failure Mode Where Human Governance Rights Require Workflow Approval Before Exercise in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as standalone prior art, a specific architectural failure mode — *workflow-approval-gated governance* — that violates the source paper's foundational commitment to human-governed substrate (§3.1, §3.3, §6.3) by conditioning the exercise of inspect, modify, and override rights on workflow approver consent.

## Abstract

The CKS pattern names "human-governed" as a foundational architectural commitment, with two qualifying properties: governance must be *architectural* (a property of the design, not a procedural promise) and *temporal* (the rights must be exercisable at any time, not only at scheduled checkpoints). This note formalizes a failure mode in which both qualifying properties are simultaneously compromised: deployments where the three rights (inspect, modify, override) require workflow approval before they take effect, where approver consent operates as the authority-granting mechanism, where justification must be supplied to obtain approval, and where multi-stage approval chains gate the canonical governance moments. The anti-pattern violates the architectural property, violates the temporal property, and additionally and uniquely compromises the override right's no-justification-required property. The note specifies four operational components, identifies the CKS commitments violated, traces the failure mode, states the architectural correction, distinguishes the anti-pattern from four adjacent legitimate practices, and provides an operational test. Together with the sibling notes on vendor-revocable governance and scheduled-review-window governance, this note closes the foundational governance anti-patterns at the human-governed commitment.

## 1. Why standalone formalization is needed

The human-governed commitment is the architectural anchor of the CKS pattern (source paper §3.1, §6.3): every other commitment in the design depends on what governance means and how it is preserved. The source paper qualifies the commitment along two dimensions (§3.3): governance must be architectural (a property of the design, not a procedural or vendor-dependent promise) and temporal (exercisable at any time, not only at scheduled checkpoints). Each qualifier names a failure surface; the sibling anti-pattern notes on vendor-revocable governance and scheduled-review-window governance formalize the failure modes that violate one qualifier each.

This note formalizes the failure mode that violates both qualifiers simultaneously and additionally compromises a property uniquely characteristic of the override right. Deployments operating under regulated or compliance-oriented governance frameworks consistently default to approval-workflow systems for governance activities, and the resulting configurations look responsibly designed by the standards of those frameworks while quietly failing the foundational CKS commitment. Naming the failure mode as a standalone anti-pattern, with operational components and a published correction, is what allows downstream work to recognize it before reproducing it.

The override-specific motivation is the third reason for standalone formalization. The CKS pattern commits to override being exercisable without justification (source paper §3.3); workflow approval typically requires justification for approval to be granted. Standalone formalization makes visible that ordinary approval-workflow integration fundamentally compromises the override right's architectural design.

## 2. The anti-pattern, defined as four operational components

A deployment exhibits *workflow-approval-gated governance* if any of the following operational components are present in its architecture. A deployment exhibiting all four exhibits the anti-pattern fully.

**(a) Workflow-approval as precondition for rights exercise.** The architecture requires workflow approval as a precondition for any of the three rights to take effect. The user submits a request; the request enters a workflow; only after the workflow completes — with approver consent — does the right operationally exercise. Substrate interfaces that would otherwise carry rights exercise are mediated by the workflow system; rights do not exist for the user to exercise directly.

**(b) Approver consent as authority-granting.** The workflow approvers' consent operates as the authority-granting mechanism. The rights remain architecturally named in the system's design, but their exercise depends on approver consent. The architectural commitment that authority is held by humans named in the substrate-resident authority structure becomes operationally a commitment that authority is held by the *workflow approvers* — whose consent is required regardless. The locus of authority migrates from the substrate's authority structure to the approval chain.

**(c) Justification-requirement for override exercise.** The workflow approval process requires justification to be granted: the human invoking override must provide reasons, which approvers evaluate before granting consent. This component specifically and directly compromises the override right's no-justification-required property. The architectural design — override exercisable on the human's authority alone, without explanation — fails operationally because justification is required to obtain the approval that the workflow has interposed between the user and the right.

**(d) Multi-stage approval chains gating governance moments.** Approval workflows typically include multiple stages: initial review, compliance check, manager approval, executive approval. Each gates the governance moment. Rule authoring, which the source paper names as the canonical design-time governance moment (§3.3), becomes a multi-stage workflow rather than an immediate exercise of authority.

The four components together define the anti-pattern architecturally: (a) is the gating mechanism, (b) is the authority migration, (c) is the violation specific to override, (d) is the temporal and procedural dilution of the canonical governance moments.

## 3. Which CKS commitments are violated

The anti-pattern violates a broader set of commitments than the sibling A1.01 anti-patterns. The violations sort into three tiers.

**Tier 1 — Direct foundational violations.**

*Human-governed (source paper §3.1, §3.3) is violated across both qualifying properties.* The architectural property fails because governance becomes a feature of the workflow system rather than a property of the substrate's design — rights exist only as workflow-mediated requests, not as architectural affordances. The temporal property fails because rights are not exercisable at any time; they are exercisable only after workflow completion, which is process-determined timing rather than human-determined. The two qualifiers fail simultaneously, not independently.

*The override right's no-justification-required property is directly violated.* The CKS pattern commits to override being exercisable without the human providing justification (source paper §3.3); workflow approval typically conditions consent on justification. Override's distinctive property — exercisable on the human's authority alone — is uniquely vulnerable to workflow-approval-gating; the inspect and modify rights do not depend on a no-justification-required property in the same load-bearing way. This violation is what distinguishes this note's anti-pattern from the two siblings, which do not specifically compromise override's distinctive property.

**Tier 2 — Operationally compromised commitments.**

The three rights individually become conditional on workflow approval; they exist architecturally but are exercisable only with approver consent. The canonical governance moment of orchestration rule authoring at design time becomes a multi-stage workflow rather than the immediate exercise the source paper names. The substrate-resident authority structure fails operationally as the source-of-truth for *who has what authority*, because authority is exercised through the workflow approver chain — which may or may not coincide with the substrate's specified authority.

**Tier 3 — Extended violation.**

The composition requirement that per-substrate human governance be preserved across compositions is extended-violated. Governance preservation is conditional on workflow approver consent rather than architecturally guaranteed; substrate composition into multi-substrate deployments inherits this conditionality. The requirement that each composed substrate retain its own human-governed property fails not only at the deployment in question but at every substrate that composes with it under the same workflow approval regime.

## 4. The failure mode

Workflow-approval-gated governance produces deployments where the three rights are operationally exercised through approval workflows rather than directly. The downstream consequences are operationally specific.

*Rights become privileges granted by workflow.* The architectural commitment that humans hold authority becomes operationally a commitment that humans must persuade approvers to grant the privilege of exercising the right. Persuading-to-obtain-privilege depends on approver judgment; holding the right depends on the substrate's authority structure. The two are fundamentally different.

*Override decisions cannot be made urgently.* Override is architecturally designed for urgent intervention — when orchestration rules produce harmful outcomes, when substrate content needs immediate correction. Workflow processing introduces delay: stages must complete, approvers must be reached, consent must be gathered. The workflow delay may render override operationally unavailable when most needed.

*Justification-to-approvers dilutes authority.* Override is designed to be exercisable without justification because requiring justification places the burden of persuasion on the rights-holder and locates the evaluation of that persuasion outside the rights-holder's authority. When workflow approval requires justification, the human's authority is not what determines whether the right exercises — the approvers' evaluation of the justification is.

*Workflow approvers become de facto authority-holders.* Even if substrate-resident authority structure specifies that the human exercising rights holds authority, the approvers' consent is operationally required. Authority migrates from the substrate authority structure to the workflow approval chain; the substrate's specification becomes documentary rather than operative.

*Coordination work is blocked by approval delays.* Substrate operations that depend on rights exercise — modifications to authority structure, override of harmful rule outcomes, inspection during incident response — are blocked while approval is in progress. Approver veto effectively forecloses rights exercise; recovery from workflow failures (approver unavailability, escalation cycles, system errors) translates directly into rights-exercise failures, because the architectural commitment to exercisable rights has been delegated to the workflow's reliability.

## 5. The architectural correction

The architectural correction operates through three foundational moves and three operational practices.

**Direct rights exercisability.** The three rights must be exercisable directly through architectural mechanisms that do not gate exercise on workflow approver consent. The deployment must provide substrate interfaces where humans named in the substrate-resident authority structure can exercise inspect, modify, and override directly; the interfaces operate immediately on rights exercise.

**No-justification-required override.** The override right must be exercisable without the human providing justification before the override takes effect. Logging, audit, and post-exercise documentation are admissible (and often desirable); they may not be conditions of exercise. The distinction between gate-on-justification and document-after-exercise is the architectural correction.

**Architectural property of governance preserved.** Governance must be a property of the deployment's architecture, not a feature of the workflow system that operates over the deployment. The substrate interfaces, the authority structure, and the rights-exercise mechanisms are properties of the substrate's design — not features that depend on a workflow system to be present and operational.

A correctly architected deployment additionally:

*Maintains workflow approval as collaborative complement, not gating substitute.* Workflow approval may operate as collaborative review for proposals, policy updates, or stakeholder deliberation. The architectural commitment is that approval *complements* rather than *gates*: review may be sought, but rights remain exercisable independently of whether review has been requested or completed.

*Specifies operational paths for urgent rights exercise.* The deployment includes mechanisms by which humans can exercise the three rights immediately when needed without entering workflow approval. Routine deliberative paths and urgent direct paths may both be present; the architecture requires that the direct path be available, not that it be the only path.

*Maintains substrate-resident authority structure.* The authority structure for *who has what authority* remains the substrate's, not the workflow's. Approver lists, approval hierarchies, and consent chains may operate as additional operational practices but cannot substitute for the substrate-resident authority specification.

## 6. What workflow-approval-gated governance is NOT

The anti-pattern is operationally distinct from four adjacent legitimate practices commonly conflated with it.

*Not collaborative review processes that complement rights exercise.* Peer review of proposals, team review of significant changes, and advisory review of new orchestration rules are legitimate when they complement rather than gate rights exercise. The anti-pattern arises specifically when collaborative review becomes a precondition for rights to take effect; deployments where review operates over proposals while individual rights remain directly exercisable satisfy the architecture.

*Not documentation requirements that operate post-exercise.* Some deployments require documentation of rights exercise after the right has been exercised — for audit, record-keeping, or compliance reporting. Post-exercise documentation does not gate the right; it documents what has occurred. Gating documentation that conditions exercise is the anti-pattern.

*Not advisory review without gating.* Advisory review processes in which humans receive feedback before exercising rights are legitimate when the feedback is informational rather than gating. The human may consider advisory feedback but is architecturally entitled to exercise rights regardless of it.

*Not multi-author coordination through proposal patterns.* Multi-author coordination — where one author proposes a change and others review before acceptance — is legitimate when each author retains architectural rights to exercise inspect, modify, and override. Multiple humans may collaborate while each retains direct exercisability. Workflow approval gating, by contrast, makes rights conditional on approver consent regardless of who proposed the change.

## 7. Operational test

A deployment exhibits workflow-approval-gated governance if any of the following hold at any time during its existence:

(a) The three rights require workflow approval before taking effect; humans cannot exercise rights directly without obtaining approver consent.

(b) The override right requires justification to approvers; the no-justification-required property is operationally compromised.

(c) Workflow approver consent is operationally required to make rights take effect, even though the substrate-resident authority structure specifies the human as authority-holder.

(d) Rights exercise is delayed by workflow processing time; urgent rights exercise is blocked by workflow throughput.

Three sharpening properties operationalize the test for review.

**Gating-versus-collaborative test.** Attempt rights exercise without entering the workflow. If the right exercises, the workflow is collaborative; if not, the workflow is gating.

**Justification-required test.** Attempt override without providing justification. If approval is denied, deferred, or treated as incomplete for lack of justification, the no-justification-required property is violated.

**Authority-locus test.** Examine whether approval is required even when the substrate-resident authority structure specifies the user as authority-holder. If yes, authority has migrated from the substrate to the workflow.

A deployment that fails any of (a)–(d) and any of the three sharpening properties exhibits the anti-pattern. The correction in §5 specifies the operational changes required.

The one-sentence test: *if a deployment's three rights require workflow approval before taking effect, and the override right specifically requires justification to approvers as a condition for approval, the deployment exhibits workflow-approval-gated governance — and the architectural commitment to human-governed fails at the architectural property, at the temporal property, and at the override right's no-justification-required property simultaneously.*

## Conclusion

Workflow-approval-gated governance is the canonical drift mode in compliance-oriented and regulated AI deployments because compliance frameworks routinely require approval workflows for significant decisions. The drift is largely invisible to the audiences that adopt these frameworks: "we have approval workflows for AI decisions" reads as responsible AI governance, while quietly compromising the architectural commitment that anchors the CKS pattern. The downstream consequences manifest as authority migration to the approval chain, override blocking through delays, justification-requirement violations of override's distinctive property, and source-of-truth migration from the substrate to workflow approvers.

Together with the sibling notes on vendor-revocable governance (which violates the architectural property through vendor revocability) and scheduled-review-window governance (which violates the temporal property through scheduled windows), this note closes the foundational governance anti-patterns at the human-governed commitment. The siblings cover the failure modes that violate one qualifier each; this note covers the failure mode that violates both qualifiers simultaneously and additionally compromises the override right's no-justification-required property. Subsequent notes formalize anti-patterns at additional foundational commitments.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Anti-Pattern: Workflow-Approval-Gated Governance — A Standalone Formalization of the Failure Mode Where Human Governance Rights Require Workflow Approval Before Exercise in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
