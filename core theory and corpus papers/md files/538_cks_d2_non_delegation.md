# FAI Governance Non-Delegation Principle

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 1 of the CKS theory series commits that human governance holds *structural authority* over substrate content and orchestration rules — not procedurally promised authority that can be reassigned, outsourced, or substituted. This note formalizes how that commitment applies at inter-Self scope, where Full Aspect Integration (FAI) events coordinate across organizational boundaries over a shared substrate. The resulting principle is the FAI governance non-delegation principle: governance authority over FAI events cannot be delegated to non-governance actors, including automated systems, infrastructure platforms, and third-party services. The note distinguishes governance authority (the right to decide configuration, conflict resolution, absorption, and dissolution) from governance labor (the execution work of constructing substrates, producing records, and routing notifications), identifies three classes of permissible automation and three classes of impermissible delegation, explains why joint authority across participating Selves is shared authority rather than delegation, and states the automated-governance anti-pattern that the principle guards against.

---

## 1. Derivation context

This note is derivation D2.43 in Phase D2 of the CKS defensive publication series. It derives from D1.02 — the six paper-level claims Paper 1 commits to — specifically Paper 1 Claim 3: that human governance holds structural authority over substrate content and orchestration rules at all times.

D1.02 establishes six commitments for a single-Self substrate: hybrid with governance boundary; conflict preservation; human-governed authority; AI as substrate mediator; tool-agnosticism; and linear-cost composition. Of these, Claim 3 is the load-bearing commitment for what follows. It is the claim that makes the others defensible: conflicts are preserved *because* humans hold override authority; the AI is a mediator *rather than* an authority holder; the substrate is the coordination artifact *rather than* the LLM's inference *because* the substrate is what humans can govern.

Paper 3 extends the architecture to inter-Self scope, where two or more CKS-governed Selves coordinate over a shared substrate constructed for a FAI event. The shared substrate is itself a CKS substrate; all six Paper 1 commitments hold within it by inheritance. What D2.43 formalizes is the application of Claim 3 specifically at this inter-Self scope: the human-governed authority commitment does not weaken when the substrate spans an organizational boundary. It applies with the same structural force. Governance authority over the FAI event cannot be delegated to any non-governance actor, regardless of how much of the execution work is automated.

---

## 2. The authority-not-labor distinction at FAI scope

The distinction that makes governance non-delegation operable — at intra-Self scope in Paper 1 and at inter-Self scope here — is the distinction between governance authority and governance labor.

**Governance authority** at FAI scope names the right to decide:

- What the FAI configuration is: which aspects each Self contributes, the cooperation or competition variant, the cardinality, the persistence policy, the provenance carry-over depth at the perimeter.
- What constitutes conflict resolution: which orchestration rule class applies to a given inter-Self conflict, and whether conflicts are resolved in the shared substrate, preserved for home-governance action, or escalated across the joint authority of participating Selves.
- What is absorbed via DNA evolution: which orchestration patterns, schemas, or rules from another Self's contributed aspects are candidates for absorption into a receiving Self's DNA, and which are approved or declined.
- Whether to withdraw: whether a participating Self's governance withdraws from or terminates the FAI event.
- Whether to escalate: whether a conflict or ambiguity in the shared substrate is escalated to the participating Selves' governance structures for direct resolution.

These are governance decisions. They cannot be executed by an automated system, an infrastructure platform, or a third-party service without the underlying authorization having been held by human governance. The execution of a pre-authorized decision by an automated system does not transfer authority. The test is not who presses the button; it is who authorized the decision the button enacts.

**Governance labor** at FAI scope names the execution work:

- Constructing the shared substrate for the event, per the governance-authorized configuration.
- Registering conflicts surfaced during the event as first-class substrate entries.
- Producing contribution records, provenance annotations, and conflict registry entries.
- Routing escalation notifications to the participating Selves' governance structures.
- Executing the dissolution hand-off at event termination, transferring outputs to each Self's home substrate per the persistence policy.

These are execution tasks. They can be performed by automated systems, LLMs operating as substrate mediators, or infrastructure components — provided they operate under governance authorization. The authority does not move when the labor is automated. What moves is only the work.

---

## 3. Permissible automation

Three classes of automation at FAI scope are permissible because they execute governance-authorized decisions rather than making governance decisions independently.

**Pre-authorized rule execution.** Orchestration rules governing FAI events are human-authored substrate content. When a conflict arises that matches a pre-authorized rule's class, the rule executes automatically. This is not delegation of governance authority. The authority happened at rule-authoring time, when human governance wrote the rule that specified what this class of conflict resolves to. The automated execution is enacting an already-made governance decision. The authority structure is intact; the labor has been moved from per-instance human action to rule-execution.

**Automated record production.** The shared substrate produces contribution records, conflict registry entries, dissolution records, and provenance annotations automatically as the FAI event proceeds. This is automated governance labor. The records are substrate content; they remain subject to the three rights — inspect, modify, override — that human governance holds over the shared substrate at all times. Automated production of records does not transfer authority over the records.

**Standing configuration application.** A standing configuration — a governance-authorized configuration that applies automatically to new FAI events within its defined scope — takes effect without requiring fresh configuration authoring for each event. This is not delegation. Human governance jointly authorized the standing configuration; it is the execution of a governance decision made in advance. The participating Selves' governance structures authorized the configuration; its automated application to new in-scope events is execution under that prior authorization.

In each of these three cases, the permissibility derives from the same structural fact: the governance decision was made by human governance at an earlier moment; the automation executes that decision. Authority is not reallocated by the automation; it was held and exercised by humans at the decision point.

---

## 4. Impermissible delegation

Three classes of delegation at FAI scope are impermissible because they transfer the governance decision itself — not only the execution — to a non-governance actor.

**LLM governance authority.** An LLM may perform governance labor under governance authorization — drafting a configuration for human review and approval, producing records, executing conflict resolution after a rule has been authorized. What an LLM may not do is hold governance authority: deciding, without human authorization, what the FAI configuration should be, which conflicts to resolve and how, or whether to absorb DNA content into a receiving Self's home substrate. These are governance decisions. An LLM that makes them without governance authorization is not executing a human-authorized decision; it is making the decision itself. This is governance delegation to a non-governance actor.

**Infrastructure-determined configuration.** A FAI infrastructure platform may execute the configuration once governance has authorized it — constructing the shared substrate per the specified parameters, applying the persistence policy at dissolution, routing records as specified. What the infrastructure platform may not do is determine the configuration parameters itself, whether through optimization defaults, platform-side inference about suitable parameters, or gap-filling where governance has not specified. Determination of configuration is a governance decision. Platform execution of a governance-authorized configuration is permissible; platform determination of a configuration in the absence of governance authorization is not.

**Third-party governance authority.** A third-party service — including an external AI governance service — may provide governance labor under authorization from the participating Selves' governance structures: executing records, routing escalations, producing dissolution artifacts. What a third-party service may not hold is governance authority itself over the shared substrate. Authority over the shared substrate belongs to the participating Selves' governance structures jointly. It cannot be transferred to a third party through service engagement, contractual arrangement, or platform dependency. Third-party services operate under governance authorization; they do not hold governance authority.

---

## 5. Joint authority as shared authority, not delegation

Paper 3 introduces joint authority across participating Selves as the governance structure for the shared substrate. Joint authority warrants explicit treatment here because it could superficially appear to implicate the non-delegation principle: if each Self's home governance holds authority within its home perimeter, and the FAI event operates under joint authority, has either Self delegated away some of its authority?

The answer is no. Joint authority between participating Selves is not delegation — it is shared authority between organizations that each hold their own governance. The joint authority arrangement is itself an expression of each participating Self's governance authority, not a retreat from it. Each Self's home governance authorizes the FAI event, approves the configuration, and retains the three rights — inspect, modify, override — over the shared substrate for the event's duration. The shared substrate's governance scope is *in addition to* each Self's home governance scope, not a substitution for it.

The non-delegation principle applies without modification to joint authority structures. What the principle prohibits is the transfer of governance authority to a non-governance actor — an LLM, an infrastructure platform, a third-party service. Joint authority among multiple governance structures is not that. It is an expansion of the governance perimeter to cover the shared substrate, with all participating Selves' governance structures holding authority within that expanded scope.

---

## 6. Inheritance from Paper 1

The FAI governance non-delegation principle is Paper 1's authority-not-labor distinction applied at inter-Self scope. The structural form is identical.

At intra-Self scope, Paper 1 commits that LLMs act as substrate mediators — they execute over substrate content under governance authorization — rather than as governance authority holders. The governance authority resides with humans; the execution work can be delegated to the LLM under orchestration rules that humans have authored. The LLM cannot determine what the orchestration rules are; it executes what those rules specify.

At inter-Self scope, the same structure holds. LLMs mediate the shared substrate; they do not govern it. Infrastructure executes the configuration; it does not determine it. Third parties provide execution labor; they do not hold authority. The scope has expanded from a single Self's substrate to a shared substrate spanning the inter-Self perimeter. The commitment has not changed.

This inheritance is not coincidental. Paper 3 explicitly commits that all six Paper 1 commitments hold within the shared substrate. D2.43 formalizes the application of Claim 3 — human-governed authority — specifically at the inter-Self boundary. The formalization is necessary because the inter-Self scope introduces new actors (infrastructure platforms, multi-party services, third-party governance services) and new structures (joint authority, standing configurations, pre-authorized escalation rules) that could, without explicit treatment, be misread as softening the commitment. They do not soften it. They instantiate it at a larger scope.

---

## 7. Anti-pattern: automated governance

The automated governance anti-pattern names the failure mode D2.43 guards against.

An automated governance FAI event is one in which all governance functions — configuration, conflict resolution, absorption decisions, dissolution — are executed by automated systems without human governance authorization at the decision point. The automation produces records and executes operations; no human governance structure holds the authority over what those operations are.

This anti-pattern is the FAI-scope analog of the intra-Self failure mode Paper 1's authority-not-labor distinction guards against: governance authority held by the LLM rather than by humans. At inter-Self scope, the equivalent failure mode is governance authority held by automated systems, infrastructure platforms, or third-party services rather than by the participating Selves' governance structures.

The anti-pattern may be difficult to detect in a fully automated implementation because execution and authority can superficially appear identical when no human action is required for routine operation. The operational test in §8 is designed specifically to surface this distinction.

---

## 8. Operational test

For a FAI event with high automation — one where configuration, conflict resolution, record production, and dissolution all proceed without per-instance human action — the governance non-delegation principle is satisfied if and only if all of the following hold:

1. The FAI configuration (sharing scope, cooperation/competition variant, persistence policy, provenance carry-over depth) traces to a human governance authorization decision: either a specific per-event authorization or a standing configuration that human governance jointly authorized within its defined scope.
2. Every conflict resolution that occurs during the event either (a) executes a pre-authorized orchestration rule that human governance authored, or (b) is escalated to the participating Selves' governance structures for direct resolution, with no conflicts resolved by infrastructure or LLM determination outside of (a) or (b).
3. Every absorption decision — selection of content from the shared substrate as candidate for ingestion into a participating Self's home DNA — traces to an authorization decision made under the receiving Self's home governance authority.
4. The dissolution of the shared substrate executes the governance-authorized persistence policy; the dissolution event itself is not determined by infrastructure optimization or platform defaults operating outside of governance authorization.
5. At any point during the event, a human with appropriate access to the participating Selves' governance structures can inspect the shared substrate, modify the configuration, override any conflict resolution, or withdraw from the event — without requiring approval from the automated systems executing the event.

A FAI event that satisfies (1)–(5) instantiates the governance non-delegation principle regardless of how automated its routine operation is. A FAI event that fails any of (1)–(5) has delegated governance authority — in whole or in part — to a non-governance actor.

---

## 9. Conclusion

The FAI governance non-delegation principle is a direct application of Paper 1's authority-not-labor distinction at inter-Self scope. Governance authority over FAI events — the right to decide configuration, conflict resolution, absorption, and dissolution — cannot be delegated to automated systems, infrastructure platforms, or third-party services. These actors may execute governance-authorized decisions; they may not hold governance authority. Joint authority among participating Selves is shared authority among governance structures, not delegation away from them. The scope of the commitment expands at inter-Self scope to encompass a shared substrate spanning organizational boundaries; the structural commitment does not weaken.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance Non-Delegation Principle.* May 15, 2026. ORCID: 0009-0004-8065-3235.
