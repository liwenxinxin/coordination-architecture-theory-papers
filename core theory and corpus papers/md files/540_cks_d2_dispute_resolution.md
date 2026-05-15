# FAI Event Dispute Resolution

**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** May 15, 2026  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI) events involve two or more participating Selves contributing aspects to a shared substrate under jointly configured governance. When disputes arise during or after an FAI event, they fall into two structurally distinct categories: content conflicts, which are disagreements about what content in the shared substrate is authoritative, and governance process disputes, which are disagreements about whether the governance process itself was correctly followed. The three-tier conflict-handling mechanism (preserve / resolve via orchestration / escalate to humans) addresses content conflicts within the substrate. This note formalizes five types of governance process disputes that are categorically distinct from content conflicts, three escalation levels through which process disputes are resolved (direct governance dialogue, cross-organizational agreement invocation, and external governance), and the architectural property that makes process disputes resolvable: because governance activities must be recorded as substrate content, governance records are the dispute evidence base. When records are complete, process disputes are resolvable through record review. When records are missing, process disputes are permanently unresolvable — the anti-pattern this note names as unrecorded process. The operational test: for any governance process dispute, can an observer determine from governance records alone whether the disputed claim is supported or denied?

---

## 1. Why the distinction must be established first

An FAI event involving multiple participating Selves operates under a shared governance arrangement: jointly configured orchestration rules, joint modification rights, and cross-organizational governance agreements that specify authority and escalation paths. Over the course of an FAI event, or after it concludes, disputes can arise. These disputes are not homogeneous. Without first distinguishing their category, the wrong resolution mechanism will be applied, and applying the wrong mechanism wastes governance effort while leaving the actual dispute unaddressed.

The three-tier conflict-handling mechanism (D0.03 / Claim 3 of the source paper) is designed for one specific category: content conflicts within the shared substrate. A content conflict is a disagreement about what content is authoritative — for example, two participating Selves have contributed aspects with contradictory knowledge claims about the same entity, and both versions persist in the shared substrate. The mechanism's three tiers — preserve the conflict as first-class substrate state, resolve via configured orchestration rules within the substrate, or escalate to the joint-governance arrangement of participating Selves — address content-level disagreements using substrate-level mechanisms. The conflict itself is a substrate state; the resolution operates through substrate content under joint authority.

Governance process disputes are categorically different. A governance process dispute is not a disagreement about the content of the substrate. It is a disagreement about whether the governance process that was supposed to govern the event was actually followed. The substrate content is not in question; what is in question is the procedural history of the event. Applying the three-tier content-conflict mechanism to a governance process dispute misroutes the dispute, because the three-tier mechanism resolves what content is authoritative — it cannot resolve whether an authorization procedure was followed correctly.

D2.45 addresses governance process disputes. D2.45 is the operational decomposition of two prior commitments: D1.15 (the escalate-to-humans tier, which commits to surfacing unresolvable governance questions to the joint-governance arrangement of participating Selves' home governance structures) and D2.34 (the cross-organizational governance agreement, which specifies the authority structures and escalation framework governing the cross-organizational relationship). Together, D1.15 and D2.34 create the institutional scaffold within which governance process disputes are resolved. D2.45 specifies the five types of disputes that require this scaffold, the three levels at which resolution proceeds, and the evidence base — governance records — that makes resolution possible.

---

## 2. Five types of governance process disputes

Five types of governance process disputes can arise in connection with FAI events. Each concerns a distinct governance requirement; each is resolvable through a distinct class of governance record.

**Type 1 — Authorization dispute.** One participating Self's governance claims that the FAI configuration was not properly jointly authorized. The disputed claim is procedural: that the approval mechanics jointly configured for this event class were not satisfied before the configuration took effect. Example: Self A's governance claims that Self B authorized the FAI configuration without allowing the agreed-upon review period, violating the jointly configured approval mechanics (D1.25/D2.12). Resolution requires the authorization records from the configuration phase.

**Type 2 — Amendment dispute.** Participating governance disagrees about whether a configuration amendment made during the event was properly authorized under the joint modify right (D2.04). Example: Self A claims that Self B amended the persistence policy during the event without requiring joint authorization, exercising a modify right that belongs to both Selves jointly. Resolution requires the amendment records and the orchestration rule specifying the joint modification requirement.

**Type 3 — Home perimeter violation claim.** One participating Self's governance claims that its home perimeter was violated: that content from one FAI event reached a subsequent FAI event or a home substrate without the appropriate provenance records authorizing that transfer (D2.17). Example: Self A claims that knowledge content contributed to FAI Event 1 appeared in Self B's contribution to FAI Event 2 without the required provenance carry-over records. Resolution requires the provenance records from both events.

**Type 4 — Withdrawal dispute.** Participating governance disagrees about whether a withdrawal from the shared substrate during the event was properly governed (D2.27). Example: Self A claims that Self B's aspects disappeared from the shared substrate without a withdrawal record — that the content left the substrate without following the governance-specified withdrawal procedure. Resolution requires the withdrawal records and the substrate state at the relevant timestamps.

**Type 5 — Documentation dispute.** Participating governance disagrees about whether the governance records produced during the event meet the documentation standards (D2.36). Example: Self A claims that Self B's contribution records are incomplete — that the records do not contain the information required by the documentation standards to which both Selves committed in the cross-organizational governance agreement. Resolution requires the records themselves and the documentation standards specification.

Each of these five types concerns a different governance requirement; none concerns the content of the substrate in the sense that the three-tier mechanism addresses. All five require examining governance records. This is the architectural property that connects the dispute taxonomy to the resolution mechanism.

---

## 3. Three resolution escalation levels

Governance process disputes are resolved through a three-level escalation structure. The levels are ordered by scope: direct governance dialogue at Level 1, cross-organizational agreement invocation at Level 2, and external governance at Level 3. Escalation proceeds to the next level only when the current level is insufficient.

**Level 1 — Direct governance dialogue.** The governance practitioners of the participating Selves review the relevant governance records together. This review uses the inspect right (D2.04), which each participating Self holds over the shared substrate's governance records. Most governance process disputes are resolvable at Level 1 because the governance records either confirm or deny the disputed claim. If the authorization record exists and is complete, the authorization dispute is resolved: the claim is denied. If the amendment record is absent where one was required, the amendment dispute is resolved: the claim is supported. Direct governance dialogue is the appropriate first step because it is low-cost and because the records are the authoritative source — adding procedural overhead above the records before consulting the records is wasteful.

**Level 2 — Cross-organizational agreement invocation.** If direct governance dialogue is insufficient — because the records are ambiguous, because the parties cannot agree on what the records establish, or because the dispute involves an interpretation question about the governance requirements themselves — the cross-organizational governance agreement (D2.34) provides the dispute resolution framework. The agreement's escalation governance framework (Component 2 of D2.34) specifies which organizational representatives handle process disputes, what authority they hold, and what findings they can produce. Level 2 invokes the institutional machinery the participating Selves agreed to when they entered the cross-organizational governance relationship.

**Level 3 — External governance.** If the dispute cannot be resolved under the cross-organizational agreement — because the parties cannot agree on the agreement's application, because the dispute goes to the agreement's foundational terms, or because the trust relationship between the participating organizations has degraded — the organizations may engage an external governance body: a trusted third-party assessor with access to the governance records. The external body exercises the inspect right at cross-organizational scope under authority granted by the cross-organizational governance agreement. It reviews the governance records and produces a governance finding: the disputed claim is either supported (the records show the governance requirement was not met) or denied (the records show it was met).

Level 3 is the architectural feature that makes the governance architecture viable for high-stakes cross-organizational coordination. Participating organizations can commit to an FAI governance arrangement knowing that if the internal governance relationship fails — if direct dialogue and agreement-level escalation are both insufficient — there is a credible, record-grounded external path. The external body does not substitute for the governance architecture; it completes it. The external body works with the same evidence base as the internal levels: governance records.

---

## 4. Governance records as the dispute evidence base

The architecture of D2.45 rests on a single enabling property: governance activities are recorded as substrate content. The governance record for an FAI event — including the authorization records, modification records, provenance records, withdrawal records, and documentation records — is itself substrate content within the shared substrate. This is not incidental. It is the architectural commitment that makes governance process disputes resolvable at all.

A governance process dispute claims that a governance requirement was not met. The records either confirm or deny this claim. If the authorization procedure was followed, the authorization record exists. If the persistence policy amendment was jointly authorized, the amendment record reflects that authorization. If a withdrawal was governance-compliant, the withdrawal record is present. In each case, the dispute claim is testable against the record: the record's presence and content either satisfy the governance requirement or they do not.

This record-grounding has two architectural implications. First, it makes governance process disputes binary: a process dispute is not a matter of judgment about competing reasonable positions; it is a factual question about whether a record exists with the required content. The record either satisfies the governance requirement or it does not. Second, it links the viability of dispute resolution directly to documentation completeness. A governance process dispute is resolvable when the records are complete; it is permanently unresolvable when the records are missing.

The twenty test suite (D2.24) and the complete governance record (D2.18) together constitute the evidence base for dispute resolution. These are not auxiliary artifacts — they are the dispute resolution mechanism's substrate.

---

## 5. Anti-pattern: unrecorded process

The anti-pattern that D2.45 warns against is **unrecorded process**: governance process activities that were carried out but not recorded, leaving no evidence in the substrate. Unrecorded process is the structural failure mode that renders governance process disputes permanently unresolvable.

When a governance process activity is unrecorded, the dispute is not merely difficult to resolve — it is impossible to resolve through the evidence-based mechanism D2.45 specifies. At Level 1, the records do not confirm or deny the claim; the dispute cannot be closed. At Level 2, the cross-organizational agreement's escalation mechanism cannot produce a finding because there is no evidence to review. At Level 3, the external governance body faces the same absence: it can review only what the substrate contains.

Unrecorded process thus defeats the dispute resolution architecture entirely. This is the deep reason why the documentation standards commitment (D2.36) is a prerequisite to viable dispute resolution: documentation requirements are not overhead — they are the precondition for the dispute resolution mechanism to function. Participating Selves that commit to an FAI governance arrangement and then fail to record their governance activities do not merely create audit gaps; they create disputes that cannot be resolved by any governance mechanism within the architecture.

The anti-pattern also has an asymmetric cost structure. The cost of recording governance activities is paid at the time of the activity and is low relative to the cost of an unresolvable dispute. An unresolvable dispute at Level 3 — one that reaches an external governance body only to produce no finding because the records are absent — is disproportionately expensive. Documentation discipline is the low-cost prevention mechanism for the high-cost failure mode.

---

## 6. Operational test

A governance process dispute is properly resolvable under the D2.45 architecture if and only if all of the following hold:

1. The dispute is correctly classified as a governance process dispute — not a content conflict to be addressed by the three-tier content-conflict mechanism (D0.03).
2. The relevant governance records — authorization records, modification records, provenance records, withdrawal records, or documentation records — are present in the shared substrate as substrate content.
3. An observer with access to the governance records can determine, from the records alone, whether the disputed claim is supported (the records show the governance requirement was not met) or denied (the records show the governance requirement was met).
4. If direct governance dialogue (Level 1) is insufficient, the cross-organizational governance agreement (D2.34) specifies an escalation path with authority-holding representatives and a framework for producing governance findings.
5. If the cross-organizational agreement level (Level 2) is insufficient, the agreement enables engagement of an external governance body with inspect-right access to the governance records.

A governance arrangement that fails condition (2) instantiates the anti-pattern: unrecorded process. A governance arrangement that fails condition (3) — records are present but do not contain enough information for the claim to be testable — fails the documentation standards (D2.36) and is effectively equivalent to the unrecorded-process anti-pattern for purposes of dispute resolution. A governance arrangement that fails condition (4) or (5) has an incomplete cross-organizational governance agreement (D2.34), leaving the dispute unresolvable above Level 1.

---

## 7. Conclusion

Governance process disputes and content conflicts are two categorically distinct dispute types arising from FAI events. Content conflicts — disagreements about what content in the shared substrate is authoritative — are addressed by the three-tier conflict-handling mechanism operating within the substrate. Governance process disputes — disagreements about whether the governance process was correctly followed — are addressed by a three-level escalation structure that uses governance records as its evidence base.

The five types of governance process disputes (authorization, amendment, home perimeter violation, withdrawal, and documentation) each concern a specific governance requirement and are each resolvable through a specific class of governance record. The three resolution levels (direct governance dialogue, cross-organizational agreement invocation, external governance) escalate in scope while maintaining record-grounded resolution throughout. The external governance body at Level 3 is what makes the architecture viable for high-stakes cross-organizational coordination: a credible backstop that functions through the same evidence base as the internal levels.

The viability of this architecture depends entirely on documentation completeness. Unrecorded process is not a minor compliance failure; it is the structural anti-pattern that defeats the dispute resolution mechanism at every level. Documentation requirements are the precondition for dispute resolvability, not overhead on top of it.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Event Dispute Resolution.* May 15, 2026. ORCID: 0009-0004-8065-3235. Derivation note #540 in the CKS Derivation Note Series (Series D, Phase D2).
