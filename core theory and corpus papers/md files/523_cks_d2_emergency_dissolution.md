# FAI Event Failure and Emergency Dissolution

**Derivation Note D2.28 — Series D, Phase D2 (Note #523)**
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI) events are governed from construction through dissolution. D2.02 addressed planned dissolution — the case in which an event completes its purpose and the shared substrate dissolves under normal governance. This note addresses the complementary case: emergency dissolution, triggered not by planned completion but by governance failure, unresolvable escalation, exchange bounding violation, or joint governance determination that the event is no longer viable. D2.28 derives directly from D1.01 (shared substrate as temporary construction whose dissolution is governed) and D1.15 (escalate-to-humans as the third tier of conflict handling, with early dissolution as one of its response options). The note formalizes four emergency dissolution triggers, five governance requirements that apply to emergency dissolution, how those requirements compare with planned dissolution, the anti-pattern of silent failure, and the operational test an observer can apply to verify that emergency dissolution was properly governed.

---

## 1. Derivation basis

D1.01 commits that the shared substrate is constructed for an interaction and dissolves on that interaction's conclusion — and that dissolution is governed. The word "governed" in D1.01 does not carry a qualifier restricting it to planned conclusions. Whether dissolution is planned or forced, the governance commitment holds: dissolution must be authorized, documented, and followed by the appropriate persistence-policy execution and hand-off boundary activation.

D1.15 commits to escalation-to-humans as the third tier of conflict handling across joint authority — the mechanism by which unresolvable conflicts surface to the participating Selves' human governance for determination. One of the four responses available in the escalation protocol is early dissolution of the FAI event: governance determines that the conflict cannot be resolved within the event's scope, and the event ends rather than continuing under a governance impasse.

D2.28 is the operational decomposition of these two parent commitments for the failure case. Where D2.02 operationalized governed dissolution for the planned case, D2.28 operationalizes governed dissolution when the trigger is not planned completion but failure.

---

## 2. Four emergency dissolution triggers

Emergency dissolution is dissolution that occurs before the FAI event has achieved its intended purpose, authorized by the appropriate governance structure rather than by planned completion. Four distinct triggers warrant emergency dissolution. They are distinct because they have different authorization requirements and produce different documentary obligations.

**Trigger 1 — Governance capacity failure.** The participating Selves' governance determines that it cannot fulfill the governance requirements of the active FAI event. Governance capacity failure is not a prediction that future governance will be difficult; it is a determination that the current governance structure is presently unable to process conflicts at the rate they are arising, unable to respond to pending escalations within any viable time frame, or unable to maintain the exchange bounding verification that ensures instinct-layer and LLM-weight content remains outside the shared substrate. When governance capacity fails, continuing the event without adequate governance is worse than dissolving it — the shared substrate would operate in a condition that the architecture does not permit.

**Trigger 2 — Escalation with no viable resolution.** The escalation tier (D1.15) surfaces a conflict to human governance across joint authority. After deliberation, governance determines that the conflict is fundamentally irresolvable within the current event's scope — not merely difficult to resolve, but structurally irresolvable given the architectural constraints of the event configuration, the authority structures of the participating Selves, or the nature of the disagreement itself. Early dissolution in this case is Option 4 of the escalation response protocol: governance does not choose continued operation under unresolved conflict, resolution by one party's authority overriding the other, or scope deferral — it chooses to end the event and carry the unresolved conflict forward as preserved-tier content that each participating Self's home governance can address independently.

**Trigger 3 — Exchange bounding violation detected.** Exchange bounding (D2.16) requires that the FAI exchange operate over reasoning-layer content — DNA-layer and action-layer substrate content — and that instinct-layer content and LLM weights not enter the shared substrate. When exchange bounding verification detects that this constraint has been violated, the governance integrity of the event is compromised: content that the architecture requires to remain outside the inter-Self exchange is present within it. Emergency dissolution is triggered immediately to prevent further governance integrity failure. This trigger differs from the others in one important respect: it does not require a governance determination about whether to dissolve. The violation itself triggers dissolution; governance's role is to authorize and document, not to deliberate about whether dissolution is warranted.

**Trigger 4 — Joint governance decision.** The participating Selves' governance structures, acting through joint authority, determine by deliberate decision that the FAI event is no longer serving its intended purpose. This trigger is distinct from the others because it does not arise from a detected failure: the event may be technically operating within all its constraints. But governance determines — based on changed circumstances, revised priorities, revised understanding of what the event's participation would produce, or recognition that the event's original purpose has become irrelevant — that continuing the event would produce no useful result. Joint governance decision is emergency dissolution by choice rather than by compulsion; it carries the same governance requirements as the other triggers.

---

## 3. Five governance requirements for emergency dissolution

Emergency dissolution follows the same baseline governance requirements as planned dissolution: a dissolution record must be produced, the event's persistence policy must be executed, and the hand-off boundary must be activated for evolution-feed purposes. These requirements carry over from D2.02 without modification. Emergency dissolution adds five requirements that apply specifically to the failure case.

**Requirement 1 — Emergency dissolution authorization.** Emergency dissolution must be authorized by the participating governance structure(s) with the appropriate authority for the trigger type. For Trigger 2 (escalation with no viable resolution), one participating Self's governance may authorize early dissolution per the escalation response protocol, because the escalation mechanism already surfaces the conflict to human governance and early dissolution is one of the named response options. For Triggers 1, 3, and 4, joint authorization is required: the dissolution is not attributable to a single Self's conflict position or to a contractual escalation pathway, and the authority to end the event is a joint authority. The authorization must be recorded as part of the dissolution record.

**Requirement 2 — Emergency dissolution record.** The dissolution record produced for emergency dissolution must document, in addition to the standard dissolution record fields from D2.02: which of the four triggers caused the dissolution; the governance authorization (who authorized, under what authority, by which procedure); and references to any violation records, escalation records, or governance capacity assessment records that preceded and caused the dissolution. The standard dissolution record documents what happened at dissolution; the emergency dissolution record also documents why dissolution occurred outside the planned trajectory.

**Requirement 3 — Violation records preserved.** If emergency dissolution is triggered by a governance violation — Trigger 3 specifically, but also any case where a violation of an architectural constraint contributed to the dissolution trigger — the violation records are preserved as durable shared-substrate content regardless of the normal persistence policy. This requirement overrides the persistence policy. The persistence policy is governance-configurable and may specify that little or nothing is retained after dissolution. That configuration cannot reach violation records: governance violations detected during a FAI event are preserved for post-dissolution investigation. The audibility of governance failures is not a function of what the event's configuration happened to specify about retention. It is a function of the architecture's commitment to accountability.

The same principle applies to escalation records that preceded an early dissolution under Trigger 2. Records of what was escalated, what governance determined, and why early dissolution was chosen are preserved regardless of the persistence policy, because they document the governance process that produced the dissolution decision.

**Requirement 4 — Partial evolution feed.** Emergency dissolution does not require discarding all evolution-feed potential from the event. If useful evolution outputs exist at the time of dissolution — DNA-layer content, action-layer content, or conflict-preservation annotations that carry genuine learning value — home governance may authorize ingesting them at the hand-off boundary under the four-locus mechanism (D1.20). The decision belongs to each home governance operating at its own perimeter; emergency dissolution does not remove the governance authority to make that decision, it only removes the assumption that useful outputs necessarily exist. Some emergency dissolution events will produce no useful evolution feed, because the failure may have occurred before useful content accumulated or because the failure itself invalidates what was produced. Others will produce partial useful feed alongside the records of failure. Home governance assesses which is the case and exercises its authority accordingly. The failure is investigated; useful work is not automatically forfeited.

**Requirement 5 — Post-dissolution investigation record.** Emergency dissolution should produce a post-dissolution investigation record that documents: the governance failure that occurred (its nature, its scope, what constraints were violated or what capacity was exceeded); what was learned from the failure; and what governance changes are warranted for future FAI events involving the same Selves. The investigation record is a forward-looking document, not merely a retrospective account. Its purpose is to make the failure informative — to ensure that the same governance failure does not recur because the failure was undocumented and no corrective governance design followed. The post-dissolution investigation record is produced under home governance at each participating Self's perimeter; it is not required to be shared across Selves, though governance configurations may authorize sharing where the failure was a joint one.

---

## 4. Comparison with planned dissolution

Planned dissolution (D2.02) and emergency dissolution share a governance baseline: both require a dissolution record, both require executing the persistence policy, and both require activating the hand-off boundary for evolution-feed purposes. The governance baseline is not conditional on whether the dissolution was planned or forced.

Emergency dissolution adds three documentary layers that planned dissolution does not require: emergency trigger documentation (Requirement 2), violation record preservation overriding the persistence policy (Requirement 3), and a post-dissolution investigation record oriented toward future governance design (Requirement 5).

The authorization structure also differs. Planned dissolution is authorized by the governance configuration established at event construction — the event was designed to complete at a certain point under certain conditions, and dissolution follows from that design. Emergency dissolution requires active authorization at the time of dissolution, because the event is ending outside its designed trajectory. For most triggers, that authorization is joint. The authorization requirement is not a formality; it ensures that governance is exercised over the dissolution decision itself rather than over only the post-dissolution steps.

Emergency dissolution does not suspend the evolution-feed pathway. Requirement 4 preserves home governance's authority to ingest useful content from an event that failed. This is consistent with the four-locus mechanism's design: the mechanism operates at the home perimeter under home governance authority, and that authority is not removed by the fact that the event dissolved under failure rather than under planned completion. Asymmetric ingestion holds in the emergency case as it does in the planned case: different participating Selves may take different things from the same failed event.

The most significant structural difference between planned and emergency dissolution is Requirement 3: violation record preservation that overrides the persistence policy. Planned dissolution executes the persistence policy without exception — the configuration specified what to retain, and dissolution implements that specification. Emergency dissolution, where a governance violation triggered or contributed to the dissolution, preserves violation records regardless of what the configuration specified. The override is architectural, not governance-configurable. Governance violations are always retained for post-dissolution investigation; the persistence policy cannot remove them.

---

## 5. Anti-pattern: silent failure

The anti-pattern this note exists to prevent is silent failure: a FAI event that stops operating — no activity, no evolution outputs, no dissolution record — without any governance documentation of the termination.

Silent failure is recognizable by the absence of a dissolution record at the time the event ceased operating. An event that produced some outputs before it stopped, but produced no dissolution record, is in the silent failure state. An event that was effectively abandoned — the participating Selves simply stopped engaging, with neither a planned completion nor an emergency dissolution — is in the silent failure state. An event that terminated because one Self withdrew without jointly authorized dissolution is in the silent failure state unless a dissolution record was subsequently produced.

Silent failure is a governance accountability failure that is distinct from and in addition to whatever governance failure caused the event to stop. The event may have stopped because of a genuine and serious governance failure — an exchange bounding violation, an unresolvable escalation, a governance capacity collapse. Those failures are real and should be documented. But even they do not excuse the absence of a dissolution record. The dissolution requirement applies to emergency dissolution exactly as it applies to planned dissolution. If the event failed badly, the failure must be documented. The dissolution record for an emergency dissolution does not need to be a positive account; it can be a frank record of what went wrong, what was violated, and what was not achieved. What it cannot be is absent.

The prevention mechanism for silent failure is the same as the authorization requirement for emergency dissolution: governance must act. Emergency dissolution requires governance action at two moments — authorization of the dissolution and production of the dissolution record. Silent failure is what happens when governance does not act at those moments. This means that preventing silent failure is ultimately a governance design question, not a technical one. Governance configurations for FAI events should specify who holds responsibility for producing the dissolution record under emergency conditions, how that responsibility is triggered when normal event completion does not occur, and what the timeline for post-dissolution documentation is. These are not architectural commitments Paper 3 specifies at this scope; they are governance design requirements that D2.28 surfaces as necessary for the architecture's accountability commitments to hold in the failure case.

---

## 6. Operational test

For a FAI event that underwent emergency dissolution, an observer with appropriate access verifies that the following are all true:

1. A dissolution record exists, containing the standard dissolution record fields from D2.02 plus: which of the four emergency dissolution triggers caused the dissolution; the governance authorization for the dissolution (who authorized, under what authority); and references to any preceding violation, escalation, or governance capacity records.

2. If the dissolution was triggered by a governance violation (Trigger 3) or involved a governance violation as a contributing factor, violation records exist as durable content and their existence is not contingent on what the event's persistence policy specified for normal retention.

3. If escalation records preceded an early dissolution under Trigger 2, those escalation records are preserved alongside the dissolution record, documenting what was escalated, what governance determined, and why early dissolution was chosen.

4. A post-dissolution investigation record exists, produced under home governance, documenting the nature of the governance failure, what was learned, and what governance design changes are warranted for future FAI events with the same Selves.

5. Home governance has made a documented determination regarding evolution-feed ingestion at the hand-off boundary — either authorizing partial ingestion of content that accumulated before the failure or documenting the determination that no useful feed exists. The determination is present as a governance record; its absence, in either direction, is not permissible.

A FAI event that underwent emergency dissolution and satisfies all five conditions has met the governance requirements of D2.28. A FAI event that stopped operating without meeting these conditions is either in the silent failure state (if no dissolution record exists) or in a partial compliance state (if some but not all requirements are satisfied). Both conditions represent governance accountability failures traceable to the specific requirements not met.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Event Failure and Emergency Dissolution. Derivation Note D2.28 (Note #523), CKS Derivation Note Series.* May 15, 2026. ORCID: 0009-0004-8065-3235.
