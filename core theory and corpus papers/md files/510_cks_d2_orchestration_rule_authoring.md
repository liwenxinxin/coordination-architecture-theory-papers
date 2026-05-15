# Orchestration Rule Authoring for Inter-Self Conflict Resolution

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

The resolve-via-orchestration tier of inter-Self conflict handling operates through pre-authored orchestration rules within the shared substrate. This note formalizes D2.15, the governance requirements for authoring those rules. A well-formed conflict resolution rule has four parts, each serving a distinct governance function: a conflict class definition (which conflicts the rule governs), resolution logic (what the rule does when it fires), a resolution record specification (what governance trace the rule leaves), and a scope declaration (whether the rule applies to this event or to a standing pattern of future events between the same Selves). A rule missing any part is governance-incomplete — it may appear to cover a conflict class while leaving matching, execution, traceability, or temporal applicability undefined. Rule authoring carries its own governance requirements: joint authorization by both participating Selves' governance, full provenance on each rule as authored substrate content, overridability via the shared substrate's joint modify right, and pre-event assessment of which conflict classes have no authored rule coverage. Coverage gaps are governance information, not failures; they determine which conflicts will escalate or be preserved rather than resolved by rule. Standing-scope rules compound over time into a richer conflict resolution framework, connecting rule authoring to the collective evolution dynamic.

---

## 1. Position within the derivation series

D2.15 is the operational decomposition of D1.14, which committed that the resolve-via-orchestration tier of the three-tier inter-Self conflict handling mechanism operates through pre-authored orchestration rules within the shared substrate. D1.14 named the tier and established that the rules governing it are substrate content authored under joint authority. D2.15 formalizes what that means in practice: what a well-formed rule contains, how rules are authorized and attributed, and how governance accounts for the conflict classes that no authored rule covers.

The note sits within Phase D2, which decomposes the operational requirements of D1's architectural commitments. D2.01 through D2.14 established the shared substrate's construction, rights architecture, content governance, and conflict handling tiers up through the escalation response options (D2.14). D2.15 turns to the rule library that makes the resolve tier function: what must be true of each rule in that library for the tier to operate with governance integrity.

---

## 2. Why rule authoring requires its own governance specification

The three-tier conflict handling mechanism — preserve, resolve via orchestration, escalate to humans — depends on the resolve tier having a populated and well-formed rule library. A tier without rules is a tier that never fires; a tier with poorly formed rules may fire in ways that are unpredictable, untraceable, or unauthorized. Neither outcome satisfies the architectural commitment D1.14 makes.

The deeper issue is that conflict resolution rules occupy a sensitive position in the governance architecture. Unlike ordinary substrate content, which records coordination state, conflict resolution rules govern how other substrate content is handled. A rule that incorrectly specifies which conflicts it covers, or that fires without recording what it did and why, or that applies to future events without the participating Selves' governance understanding that it will do so, produces governance failures that are difficult to detect and may compound across events. The four-part structure below is the minimum specification that gives governance the precision it needs.

---

## 3. The four-part rule structure

A well-formed conflict resolution rule has four parts. Each serves a distinct governance function; a rule missing any one part is governance-incomplete.

### Part 1 — Conflict class definition

The rule specifies which class of conflicts it governs. The conflict class definition uses content-domain and specification-type criteria to identify which conflicts match. A canonical example: "Conflicts where two aspects specify different response patterns for the same input category." The class definition must be precise enough that governance can reliably determine, for any specific conflict surfaced during a Full Aspect Integration (FAI) event, whether that conflict falls within the class this rule covers.

The governance function of Part 1 is matching reliability. If two conflict resolution rules have overlapping or ambiguous class definitions, the tier cannot reliably determine which rule applies. If the class definition is too broad, the rule may fire for conflicts the authoring governance did not intend it to cover. If too narrow, the rule leaves a larger-than-anticipated coverage gap. Precision in Part 1 is what gives the rule library its governance integrity as a set.

### Part 2 — Resolution logic

The rule specifies what resolution to apply when a matching conflict is detected. Three resolution logic types are available:

A **precedence rule** specifies which contributing Self's aspect specification takes precedence when the conflict class it covers is detected. The rule names the precedence and the conditions under which it applies. A **synthesis rule** specifies how to combine the two sides of the conflict into a resolution — for example, taking the union of both specifications, or applying a specific synthesis procedure the authoring governance defined. A **context rule** specifies which side of the conflict to apply based on contextual factors present in the shared substrate at the time the rule fires — for example, which Self's domain context is active for the portion of the FAI event in which the conflict arises.

The governance function of Part 2 is determinism. Resolution logic that is not fully specified for the conflict class it covers produces variable outcomes across otherwise identical conflicts, which breaks the path-retraceability requirement downstream. The resolution logic must be specified completely enough that two independent executions over the same conflict produce the same resolution.

### Part 3 — Resolution record specification

The rule specifies what the resolution record must contain when it fires. At minimum: which rule fired, identified by its authored-substrate-content identifier; what the resolution is; why the rule applies to this conflict (the matching rationale); and attribution to the governance authority that authored the rule.

The governance function of Part 3 is traceability. When a conflict has been resolved by the orchestration tier, any observer with inspect rights must be able to reconstruct the full governance chain: which rule fired, who authored it, under what joint authorization, and what the rule specified should happen. Part 3 is what connects the rule's execution back to the governance authority that authorized it. A rule that resolves a conflict without leaving the specified record produces a resolution whose governance provenance cannot be verified.

### Part 4 — Rule scope and expiry

The rule specifies whether it applies to this FAI event only (event-scoped) or to a standing pattern of future FAI events between the same Selves (standing-scoped). A rule without a scope declaration is ambiguous about its temporal applicability, which creates governance uncertainty: the participating Selves' governance cannot know, without re-examining the rule, whether it will apply to the next FAI event.

The governance function of Part 4 is temporal clarity. Event-scoped rules are consumed by the FAI event that triggered them and do not persist as active governance instruments after substrate dissolution. Standing-scoped rules persist as active substrate content that governs future FAI events; they accumulate over time into a richer conflict resolution framework. The power differential between the two scope types — standing-scope rules govern more future conduct and therefore require more ongoing governance attention — is the reason scope must be declared explicitly rather than left implicit.

---

## 4. Rule authoring governance requirements

The four-part structure specifies what a well-formed rule contains. The following requirements specify how rules enter the shared substrate and remain governed throughout their existence.

### Joint authorization

Conflict resolution rules are shared-substrate orchestration rules. They are authored as substrate content under the joint authority that governs the shared substrate (D1.25). Both participating Selves' governance must authorize rules that determine how their contributed aspect content is handled when conflicts arise. A rule authored by one Self's governance alone, without the other's authorization, is not a valid shared-substrate orchestration rule; it is a unilateral governance act that the joint-authority architecture does not recognize.

Joint authorization does not require simultaneous action. The mechanics are governance-configurable: one Self's governance may author and propose a rule; the other's governance reviews and approves it before the rule takes effect as shared-substrate content. What the requirement prohibits is a rule taking effect over the shared substrate without both participating Selves' governance having authorized it.

### Provenance

Each conflict resolution rule is authored substrate content with full attribution: who authored it, when, and under what governance authority. Provenance is not a logging convention appended after the fact; it is a property of the rule as substrate content. The rule carries its own governance lineage. This is what makes the resolution record (Part 3) meaningful: when a rule fires and records that it fired, the provenance chain connects that resolution backward to the joint governance decision that authorized the rule.

### Overridability

Rules are substrate content. The shared substrate's joint modify right (D2.04) applies to them: either participating Self's governance, acting jointly, can modify or revoke a rule that produces unexpected outcomes, that no longer accurately describes the conflict class it was authored to cover, or that generates resolutions the participating Selves' governance no longer endorses. A rule that cannot be modified or revoked is not governed substrate content; it is a hardcoded constraint outside the governance architecture.

The practical implication is that a rule library is never frozen. Governance capacity to amend rules mid-event — when the shared substrate is active and a rule has just fired in an unexpected way — is an architectural requirement, not an exception procedure.

### Coverage gap assessment

The rule library at any FAI event is finite. Governance must assess, before construction begins (this assessment is part of pre-event configuration governance, D2.12), which conflict classes are covered by authored rules and which are not. The gaps are governance information: they determine which conflicts will proceed to the preserve tier (D1.13) or the escalation tier (D1.15) rather than the resolve tier, and they inform the choice between full merge and selective merge of contributed aspects.

Coverage gaps are not failures. A gap in the rule library means governance has not yet encountered or prioritized this conflict class, or that the conflict class is intentionally left to escalation or preservation. A documented gap is more governable than an undocumented one: governance that knows in advance which classes will escalate can prepare the escalation pathway; governance that discovers gaps only when conflicts arise mid-event has less control over outcomes.

---

## 5. Standing-scope rules and collective evolution

Standing-scope rules (Part 4) connect D2.15 to the collective evolution dynamic (D1.27). An FAI event that surfaces a novel conflict class — one not covered by any pre-authored rule — may, through the escalation tier, produce a human-authorized resolution that the participating Selves' governance decides to codify as a standing-scope rule. When that rule is authored and deposited in the shared substrate, it governs all future FAI events between these Selves for the same conflict class.

The compounding effect is structural: each FAI event that triggers new rule authoring expands the resolve tier's coverage for subsequent events. Over time, the rule library reflects the accumulated governance decisions of all prior FAI events between the Selves. This is one mechanism of collective evolution — the inter-Self analog of the evolution dynamics Paper 2 develops at the intra-Self level. The rule library is not static infrastructure; it is a living substrate of governed conflict resolution knowledge that grows with the relationship between the Selves.

The governance discipline this requires is ongoing: standing-scope rules need periodic review to confirm they remain accurate for the conflict classes they were authored to cover, that the resolution logic still reflects the participating Selves' governance intent, and that scope has not outlasted the governance conditions under which the rule was authorized.

---

## 6. Inheritance from Papers 1 and 2

D2.15 inherits from two sources without re-defending either.

**Paper 1, Claim 4 (orchestration rules as substrate content):** Conflict resolution rules are orchestration rules in the Paper 1 sense. They are human-authored, they govern cell-level behavior (here, the behavior of the FAI event's orchestration layer when it encounters a conflict), and they are substrate content subject to the same inspect, modify, and override rights that apply to all substrate content. Paper 1 §5.3's "humans decide resolution logic, not the LLM" axis holds without modification at inter-Self scope: the LLM executes the rules but does not author them, modify them, or determine whether they cover a given conflict.

**Paper 2, aspect coordination rules (B2.16):** Conflict resolution rules at inter-Self scope are the inter-Self analog of aspect coordination rules that handle cross-cell conflicts within a single Self. Paper 2 established that conflicts arising from multiple cells within a Self are handled by human-authored coordination rules operating within the substrate. D2.15 applies the same structure at the cross-perimeter level: conflicts arising from multiple Selves' contributed aspects within the shared substrate are handled by human-authored conflict resolution rules operating within the shared substrate. The architectural logic is continuous; the scope of the joint authority is what changes.

---

## 7. The anti-pattern: informal resolution rules

The anti-pattern this note guards against is conflict resolution through informal understanding rather than authored substrate content. In this anti-pattern, the participating Selves' governance understands between themselves how certain conflict classes should be resolved — which Self's specification takes precedence, when synthesis applies, how contextual factors are weighted — but this understanding is not authored as shared-substrate orchestration rule content. It exists as shared expectation, prior conversation, or informal agreement.

The governance failures informal resolution rules produce are structurally predictable. First, matching is unreliable: informal understanding cannot be executed deterministically against a specific conflict surfaced in a shared substrate. Second, records are absent: because no rule fired, there is no resolution record of the type Part 3 specifies; governance cannot reconstruct which resolution logic was applied or why. Third, scope is undefined: informal understanding may be applied inconsistently across FAI events, with different governance actors applying it differently in different events without either inconsistency being visible in the substrate. Fourth, joint authorization cannot be verified: an informal understanding between governance actors is not the same as a jointly authorized substrate content entry that both governance structures can inspect.

The test for whether informal resolution is operating is simple: if a conflict was resolved by the orchestration tier but governance cannot locate the specific rule that fired as authored substrate content with joint authorization and provenance, the resolution was informal regardless of whether the outcome was the one the participating Selves' governance intended.

---

## 8. Operational test

For any conflict resolved by the resolve-via-orchestration tier during an FAI event:

1. Can an observer with inspect rights locate the specific conflict resolution rule that fired, as authored substrate content within the shared substrate, carrying full provenance (author, date, governance authority)?

2. Does the rule carry all four parts: a conflict class definition that matches the conflict in question, resolution logic that is deterministic for that class, a resolution record specification, and a scope declaration?

3. Does the resolution record generated when the rule fired match the record structure the rule's Part 3 specified?

4. Is joint authorization for the rule verifiable — can an observer confirm that both participating Selves' governance authorized the rule before it took effect?

5. Has governance assessed, prior to the FAI event, which conflict classes the rule library covers and which it does not, and is that assessment recorded as substrate content in the pre-event configuration (D2.12)?

A conflict resolution that fails any of (1)–(5) may have produced the correct substantive outcome, but does not satisfy the governance requirements D1.14 commits to for the resolve-via-orchestration tier. A resolution that fails (1) is informal, regardless of intent. A resolution that fails (2) is produced by a governance-incomplete rule. A resolution that fails (3) breaks path-retraceability. A resolution that fails (4) is not jointly authorized. A resolution that fails (5) indicates that coverage gap assessment was not performed, leaving governance without the information needed to anticipate which conflicts will escape the resolve tier.

---

## 9. Conclusion

The resolve-via-orchestration tier is only as strong as the rule library behind it. Well-formed rules have four parts: a conflict class definition that enables reliable matching, resolution logic that is deterministic for the class, a resolution record specification that preserves governance traceability, and a scope declaration that makes temporal applicability explicit. Each part serves a distinct governance function; a rule missing any part is incomplete in a specific and identifiable way.

Rule authoring itself requires joint authorization, provenance, overridability, and pre-event coverage gap assessment. These are not procedural preferences; they follow directly from the shared substrate's joint-authority architecture and the path-retraceability requirement the CKS pattern carries through Papers 1, 2, and 3. The anti-pattern — informal resolution through shared understanding rather than authored substrate content — is the failure mode the four-part structure and these governance requirements together foreclose.

Standing-scope rules connect rule authoring to the longer arc of inter-Self coordination: each FAI event that produces new rule authoring improves the resolve tier for future events, accumulating conflict resolution knowledge as governed substrate content over the life of the relationship between the participating Selves.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

---

## How to cite this note

Li, W. (2026). *Orchestration Rule Authoring for Inter-Self Conflict Resolution.* May 15, 2026. ORCID: 0009-0004-8065-3235.
