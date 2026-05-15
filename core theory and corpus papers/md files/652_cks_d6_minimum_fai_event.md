# Minimum Valid FAI Event

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

A Full Aspect Integration (FAI) event under the Paper 3 inter-Self coordination architecture qualifies as compliant when it meets exactly the seven minimum viable governance floor requirements (D2.37): authored configuration, joint authorization, construction record, exchange bounding verification, conflict registry, home perimeter integrity check, and dissolution record with hand-off governance. This note formalizes the minimum boundary — the simplest possible inter-Self coordination scenario that still qualifies — as a Type A (minimum boundary) derivation note. The boundary resolves two edge cases that carry prior-art significance: (1) a conflict registry containing zero entries satisfies the registry requirement, because the requirement is that the registry exists and was consulted, not that it found anything; (2) a two-Self, one-aspect-each, single-event interaction with no standing configurations, no cross-organizational agreement, no post-mortem, and no DNA absorption qualifies as a compliant FAI event when all seven floor requirements are met. The note states the boundary scenario, the architecture's resolution, and a binary boundary test applicable to any inter-Self coordination scenario.

---

## 1. Boundary case identification and type

**Type:** A (minimum boundary)

**Location in the architecture:** The minimum boundary of the FAI event definition — the simplest governance scenario that qualifies as a compliant FAI event under Paper 3.

**Why it matters:** The minimum boundary is the most consequential boundary case for prior-art coverage. An adversary seeking to characterize a simple inter-AI coordination scenario as novel must first contend with the scope of the minimum valid FAI event. If the simplest compliant event already covers two-Self, single-aspect, single-occurrence coordination governed by the seven-requirement floor, then the prior art's coverage extends to every scenario at or above that minimum. The minimum boundary forecloses the argument that "lightweight" inter-AI coordination — by virtue of its simplicity — lies outside the architecture's scope.

The complementary boundary (D6.03) addresses the maximum: unbounded cardinality, arbitrarily complex configuration, and population-scale persistence. This note addresses only the minimum floor.

---

## 2. The boundary scenario

Two organizations each operate a CKS-governed Self. They decide to coordinate on a single task. Each Self contributes one aspect to a temporary shared substrate. The shared substrate is constructed, the two contributed aspects are merged within it, the merge is examined for conflicts, and the results are noted. The shared substrate is then dissolved. No standing configuration exists between the two organizations. No cross-organizational agreement has been formalized. No post-mortem review is scheduled. No DNA absorption is intended; neither Self plans to incorporate content from the other's aspect into its own home substrate's DNA layer. The event is brief, transactional, and unrepeated.

The question this boundary scenario poses: does this interaction qualify as a compliant FAI event under Paper 3's inter-Self coordination architecture?

The answer depends entirely on whether the seven minimum viable governance floor requirements are met — not on the event's simplicity, brevity, cardinality, or lack of post-event evolution activity.

---

## 3. The architecture's resolution

### 3.1 The seven-requirement floor

The minimum viable governance floor (D2.37) specifies seven requirements. An FAI event is compliant if and only if all seven are present. The floor is both the minimum for compliance and the boundary below which a scenario falls outside the prior art's FAI scope.

**Requirement 1 — Authored configuration.** The event must be governed by a human-authored configuration substrate specifying at minimum: the cooperation variant (cooperative, competitive, or dissolution-only), a full merger or scoped-contribution policy, a full dissolution policy, and basic conflict routing. The configuration need not be elaborate; the requirement is that it exists, is human-authored, and specifies the minimum governance parameters before substrate construction begins.

**Requirement 2 — Joint authorization.** Both participating Selves' governance structures must authorize the configuration before the shared substrate is constructed. The mechanics of authorization are governance-configurable — sequential approval, simultaneous sign-off, designated trustee — but both Selves' authority structures must be on record as having authorized the event's configuration.

**Requirement 3 — Construction record.** The authorization described in Requirement 2 must be documented as substrate content. The construction record establishes that the shared substrate was built under joint authority, and that the authority existed before the substrate's existence.

**Requirement 4 — Exchange bounding verification.** The event must include a verification step confirming that the exchange is bounded to DNA-layer and action-layer content — that is, to orchestration substrates, behavior substrates, schemas, rules, and recorded task instances — and that LLM weights and instinct-layer content have not crossed the inter-Self perimeter. The verification need not be complex; it need only be present and recorded.

**Requirement 5 — Conflict registry.** A conflict registry must exist for the event. The registry records any conflicts surfaced during the merge of contributed aspects within the shared substrate. An empty registry — one that was created, consulted, and found no conflicts — satisfies this requirement. A registry that was never created does not. The distinction is precise: the requirement is on the existence and consultation of the registry, not on its contents. See §3.2 below for the empty-registry edge case.

**Requirement 6 — Home perimeter integrity check.** Each participating Self's governance must verify that the event has not compromised the integrity of its home perimeter. The check addresses the risk that content from the shared substrate has migrated into a home substrate's instinct layer or has otherwise bypassed home governance's authority over what enters the home perimeter.

**Requirement 7 — Dissolution record with hand-off governance.** The shared substrate's dissolution must be recorded, and the record must specify the hand-off governance: what happens to each artifact produced during the event, which content (if any) returns to which home substrate, and under what home governance authority the returned content is received. A dissolution that leaves the fate of the shared substrate's content unspecified is not a governed dissolution; it is an ungoverned termination that fails Requirement 7 regardless of whether the substrate ceases to exist.

### 3.2 The empty conflict registry edge case

Requirement 5 will be contested on the following argument: if no conflicts were detected, the conflict registry is vacuous, and a vacuous registry is indistinguishable from no registry at all. The architecture's resolution rejects this argument on a structural ground.

The conflict registry is not a record of conflict outcomes. It is the operational artifact that makes the three-tier conflict-handling mechanism available. A conflict registry that was created, that participated in the merge process, and that returned zero entries is evidence that the three-tier mechanism was operational and found nothing to escalate. A missing registry is evidence that the mechanism was never engaged — that conflicts, had they existed, would have gone undetected and unhandled. These are architecturally distinct states. The empty registry documents governance operation; the missing registry documents governance absence. Only the former satisfies Requirement 5.

This distinction is not procedural formalism. It is the same structural distinction Paper 1 draws between conflict preservation and conflict elimination: the architecture requires that conflicts be detectable and preserved as first-class substrate state, which requires that the detection mechanism exist, which requires a registry. An event that produces no conflicts is fully consistent with Requirement 5; an event that skips the mechanism is not.

### 3.3 What the minimum does not require

The boundary scenario in §2 includes several features — no standing configuration, no cross-organizational agreement, no post-mortem, no DNA absorption — that might appear to disqualify it. They do not. The following are explicitly not required by the minimum:

- **Standing configurations.** An event can be fully governed by a per-event authored configuration with no reference to any prior or standing arrangement.
- **Cross-organizational agreement.** The architecture does not require a durable inter-organizational relationship formalized outside the substrate. The joint authorization under Requirement 2 is itself the governance event that authorizes the FAI event; no prior agreement is required to make that authorization legitimate.
- **Post-mortem review.** Post-mortem review is recommended as a governance practice, particularly for events intended to feed DNA evolution. It is not required for compliance at the minimum floor.
- **DNA absorption.** DNA absorption is available where governance authorizes it; it is an optional feature of the four-locus evolution-feed mechanism. An event that produces no DNA absorption is fully compliant; the evolution machinery is simply not invoked for that locus.
- **More than one aspect per Self.** The architecture establishes two-Self cardinality as the floor for FAI (one-Self cases are intra-Self territory under Paper 2, not FAI). Within that floor, each Self contributing one aspect is sufficient. There is no minimum-aspect-count requirement above one per Self.
- **Health monitoring.** Health monitoring during the event is an optional governance enhancement for multi-event or sustained-duration interactions. It is not required at the minimum floor.

### 3.4 What falls below the minimum

The complement of §3.3: absence of any one of the seven floor requirements drops the scenario below the minimum. The failure mode associated with each absent requirement is named:

- No authored configuration → the event's cooperation variant, merger policy, and conflict routing are unspecified at the governance level (anti-pattern class: ungoverned configuration).
- No joint authorization → one Self's governance sovereignty over the event is unestablished; the shared substrate was not authorized by both authorities (governance sovereignty violation).
- No construction record → the authorization has no documentary substrate existence; the event's governance foundation is unverifiable.
- No exchange bounding verification → compliance with the instinct/reasoning separation at the inter-Self perimeter is unverified for this event.
- No conflict registry → the three-tier conflict-handling mechanism was not operational; conflicts, had they occurred, would be undetected and unrecorded.
- No home perimeter integrity check → the risk that home perimeter governance authority has been bypassed is unmitigated.
- No dissolution record → the fate of shared substrate content is ungoverned at the event's close; hand-off governance is absent.

A scenario missing any of these requirements may be a useful inter-AI interaction; it is not a compliant FAI event within Paper 3's prior-art scope.

---

## 4. Prior-art significance

The minimum boundary carries two distinct prior-art implications.

**First implication — coverage of simple scenarios.** The prior art covers the minimum: a two-Self, one-aspect-per-Self, single-event coordination scenario governed by the seven-requirement floor. Any claim that a simple governance wrapper around inter-AI content exchange is novel must address whether the claimed scenario differs architecturally from the minimum valid FAI event in a way that the prior art's architecture does not already reach. Simplicity alone — fewer aspects, shorter duration, lower cardinality, no post-event activity — does not constitute novelty with respect to the prior art. The minimum boundary is precisely calibrated to foreclose this argument.

**Second implication — the floor as the architecture's coverage anchor.** Because the minimum is defined by the presence of the seven requirements rather than by the event's scale or complexity, the architecture's coverage extends continuously from the minimum upward. Any inter-Self coordination scenario at or above the minimum — in cardinality, aspect count, duration, evolution-feed activity, or governance elaboration — is within prior-art scope if it meets the seven requirements. The minimum boundary is not a narrow special case; it is the lower anchor of a continuous coverage range.

---

## 5. Boundary test

For any inter-Self AI coordination scenario, the following binary test determines which side of the minimum boundary it occupies.

**Step 1.** Identify whether the scenario involves two or more distinct CKS-governed Selves contributing substrate content to a shared substrate for a bounded coordination purpose. If no: the scenario is either intra-Self (Paper 2 territory) or ungoverned inter-system communication. If yes: proceed to Step 2.

**Step 2.** Check each of the seven minimum viable governance floor requirements in turn:

1. Is there an authored configuration specifying cooperation variant, merger policy, dissolution policy, and basic conflict routing?
2. Do both Selves' governance structures have documented authorization of the configuration prior to substrate construction?
3. Is the authorization recorded as substrate content in a construction record?
4. Has exchange bounding been verified and recorded — confirming that the exchange is bounded to DNA-layer and action-layer content?
5. Does a conflict registry exist for this event, regardless of whether it contains any entries?
6. Has a home perimeter integrity check been performed and recorded for each participating Self?
7. Is there a dissolution record specifying hand-off governance for all shared substrate content?

**Result.** If all seven checks return yes: the scenario is a compliant FAI event within Paper 3's prior-art scope. If any check returns no: the scenario falls below the minimum; it is either not a FAI event or an instance of a governance anti-pattern at the specific locus of the absent requirement.

The test is binary at each requirement. Partial compliance at any single requirement — a configuration that specifies three of four required dimensions, or an exchange bounding verification that is performed but not recorded — does not satisfy the requirement.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Minimum Valid FAI Event.* May 15, 2026. ORCID: 0009-0004-8065-3235.
