# Composition Pair 14: Partial Withdrawal and Conflict Registry

**Series D — Phase D4 — Composition Pair Note #620**
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes the governance requirements that arise when two Paper 3 commitments operate simultaneously: Partial Participation and Withdrawal (D2.27) and the Conflict Registry (D2.13). Each commitment addresses a distinct governance problem — governing mid-event withdrawal of contributed aspects, and maintaining a seven-field record of all conflicts detected during a Full Aspect Integration (FAI) event. When both apply together, the combination generates three governance requirements that neither commitment produces alone: (1) every conflict registry entry involving a withdrawn aspect must be updated with a new WITHDRAWN-SIDE status; (2) each WITHDRAWN-SIDE conflict requires an explicit routing decision, because conflicts where one contributing side is no longer present form a conflict class that does not exist in events without partial withdrawal; and (3) a second conflict detection pass is required after the withdrawal, because the changed substrate composition may surface new conflicts invisible to the initial detection run. The note identifies these as prior-art-significant governance requirements and supplies an operational test for verifying compliance.

---

## 1. Pair Identification

**Commitment A — Partial Participation and Withdrawal (D2.27):** A participating Self may withdraw some, but not all, of its contributed aspects from an active FAI event. The withdrawal is governed: it is recorded, the shared substrate is updated to reflect the withdrawn aspects' absence, and the remaining contributed aspects from the withdrawing Self remain active in the event. Partial withdrawal differs from complete withdrawal (in which the Self exits the event entirely) in that the event continues with the withdrawing Self's remaining aspects still present.

**Commitment B — Conflict Registry (D2.13):** The conflict registry is the seven-field record maintained during an FAI event for all conflicts detected between contributed aspects across participating Selves. The seven fields capture: a conflict identifier, the participating Selves involved, the specific aspects in conflict, the nature of the conflict, the detection timestamp, the current routing status, and a resolution record. All conflicts detected by the D2.07 detection protocol are entered into the registry. The registry is a governance artifact — it preserves both sides of each conflict as first-class substrate state, consistent with Paper 3's Claim 3 inheritance from Paper 1's conflict-as-first-class commitment.

These two commitments are independent: D2.27 governs what happens when a Self changes its contributed aspects mid-event; D2.13 governs how conflicts between contributed aspects are recorded throughout the event's lifecycle. The composition forces them to interact.

---

## 2. Governance Scenario Requiring Both Simultaneously

Consider a FAI event with two participating Selves, Self X and Self Y. Self X has contributed five aspects; Self Y has contributed four aspects. At the time the governance scenario arises, the conflict registry contains twelve registered conflicts, detected during the D2.07 initial detection pass. Several of these twelve conflicts involve aspects contributed by Self X.

Midway through the event, Self X exercises its partial withdrawal right under D2.27: it withdraws two of its five contributed aspects, Aspects 3 and 4. Its remaining three aspects — Aspects 1, 2, and 5 — remain in the shared substrate. The event continues.

At this moment, both commitments are simultaneously in force. D2.27 requires that the withdrawal be governed: recorded, attributed to Self X, timestamped, and the shared substrate updated. D2.13 requires that the conflict registry accurately reflect the conflict state of the shared substrate. The twelve existing registry entries were accurate before the withdrawal. They may not all be accurate after it.

The governance question the composition poses is this: what does accurate and complete conflict governance require when the substrate's composition changes mid-event through a governed partial withdrawal?

---

## 3. Non-Obvious Governance Requirements from the Combination

Three requirements emerge from the composition that neither D2.27 nor D2.13 generates independently.

### Requirement 1 — Conflict Registry Update Is Required After Withdrawal

When Self X withdraws Aspects 3 and 4, any conflict registry entry that names either of those aspects as a contributing side has a changed governance status. The withdrawal does not automatically resolve those conflicts. The aspects have been removed from the shared substrate, but the conflicts they generated were real — they were detected against aspects contributed by Self Y that remain in the substrate. The governance record of those conflicts must not silently expire.

Under D2.13's Field 7 (resolution record and status), each affected conflict entry must be updated to reflect the withdrawal: the contributing aspect is no longer present in the shared substrate; the conflict's status is updated to WITHDRAWN-SIDE. The update preserves the conflict's history — the original detection, both sides of the conflict as recorded at detection time, and all prior routing decisions — while accurately describing the conflict's current state. A conflict registry entry that continues to list a withdrawn aspect as an active contributing side without any status annotation misrepresents the shared substrate's content.

This update requirement comes from the composition, not from either commitment alone. D2.27 governs the withdrawal itself; it does not reach into the conflict registry. D2.13 governs the conflict record; it does not specify what withdrawal does to existing entries. The requirement exists only because both commitments apply at the same time.

### Requirement 2 — WITHDRAWN-SIDE Conflicts Require an Explicit Routing Decision

The withdrawal creates a conflict class that does not exist in FAI events without partial withdrawal: the WITHDRAWN-SIDE conflict. A WITHDRAWN-SIDE conflict is one where one contributing side — the aspect whose content generated one half of the conflict — is no longer present in the shared substrate, while the other side remains.

This class is not governed by the conflict routing rules designed for standard conflicts, in which both contributing sides are present and the routing decision operates over two live substrate positions. For WITHDRAWN-SIDE conflicts, the routing decision has a different structure: (a) preserve the conflict entry as-is, retaining both sides in the registry even though one is now absent — appropriate when the governance record of the original conflict has independent value; (b) resolve by accepting the remaining side — treating the withdrawal as having effectively vacated the withdrawn aspect's position; or (c) collapse — retiring the conflict entry on the grounds that it no longer describes an active substrate tension.

The conflict routing rules (D2.51) must include explicit handling for this class. An implementation that routes WITHDRAWN-SIDE conflicts through standard routing logic is misapplying D2.51 to a conflict class D2.51 was not designed to cover. The WITHDRAWN-SIDE class is a composition artifact: it arises only when partial withdrawal and the conflict registry operate together.

For each WITHDRAWN-SIDE conflict, a routing decision record must exist, documenting which of the three options was selected, by whom, and when. The routing decision record is itself governance-required substrate content — it is what makes the WITHDRAWN-SIDE conflict's treatment inspectable and retraceable.

### Requirement 3 — Post-Withdrawal Conflict Detection Is Required

The withdrawal changes the shared substrate's composition. Self X's Aspects 3 and 4 were, before withdrawal, present alongside all of Self Y's contributed aspects and Self X's remaining aspects. Some of Self Y's content may have been in balance — not conflicting — specifically because Aspects 3 and 4 were present to mediate or offset it. When Aspects 3 and 4 are removed, that balance changes.

Content that was previously non-conflicting may now conflict with remaining content from other Selves. The initial D2.07 detection pass ran over the pre-withdrawal composition and cannot have detected conflicts that only emerge when Aspects 3 and 4 are absent. A second detection pass over the post-withdrawal composition is therefore required.

The results of this second pass must be recorded in the conflict registry, with attribution to the withdrawal as the triggering event. If the second pass detects new conflicts, those conflicts enter the registry as new entries with their own conflict identifiers, contributing aspects, and detection timestamps, noting that the triggering event was Self X's partial withdrawal of Aspects 3 and 4. If the second pass detects no new conflicts, that negative result must also be recorded — the governance record must show that post-withdrawal detection was conducted and found nothing, not merely that it was never run.

This requirement is invisible to either commitment independently. D2.27 governs the withdrawal and its immediate substrate update; it does not require a subsequent conflict detection pass. D2.13 governs the conflict registry and its contents; it does not specify when detection must be re-run. The post-withdrawal detection requirement appears only when both commitments apply at the same time and the changed substrate composition is recognized as a new detection scope.

---

## 4. Prior-Art Significance

The three requirements identified in §3 jointly establish that any governed partial withdrawal from a multi-party AI coordination event — any architecture in which a participating contributor can withdraw a subset of its contributed content from an active event with a maintained conflict record — must address the following:

**WITHDRAWN-SIDE as a named conflict class.** Prior art in multi-party coordination systems, multi-agent frameworks, and federated coordination architectures does not name WITHDRAWN-SIDE conflicts as a distinct class requiring distinct routing logic. The class is architecturally invisible unless the coordination framework simultaneously commits to (a) partial withdrawal as a governed operation and (b) a persistent conflict registry that survives individual aspect lifecycle events. The combination is what makes the class visible.

**Conflict registry entry persistence across aspect withdrawal.** Prior art in conflict-tracking systems typically either retires conflict entries when one party exits or resolves conflicts when the triggering condition is removed. The CKS composition requires neither retirement nor resolution — it requires status update with governance record preservation. This is a specific position in a design space where prior art occupies different positions.

**Post-withdrawal detection as a completeness requirement.** The requirement to run a second conflict detection pass after a composition change is a governance completeness commitment. It is non-obvious because the initial detection pass correctly covers the initial composition; the gap it leaves is visible only when the composition is understood as mutable mid-event under governed partial withdrawal. Prior art in conflict detection for multi-party coordination does not, to the author's knowledge, name post-modification re-detection as a required governance step in a maintained conflict registry.

Any implementation of governed partial withdrawal within a conflict-registry-maintaining multi-party AI coordination architecture that does not address all three requirements is incomplete with respect to the governance commitments Paper 3 establishes.

---

## 5. Operational Test

For a FAI event in which partial withdrawal has occurred, the governance compliance of the composition can be verified against the following three checks.

**Check (a) — WITHDRAWN-SIDE status updates.** Every conflict registry entry that names a withdrawn aspect as a contributing side has been updated in Field 7 with WITHDRAWN-SIDE status, including the identity of the withdrawn aspect, the withdrawing Self, and the date of withdrawal. No registry entry names a withdrawn aspect as an active contributing side without a corresponding Field 7 status update.

**Check (b) — Routing decision records for WITHDRAWN-SIDE conflicts.** For every conflict registry entry carrying WITHDRAWN-SIDE status, a routing decision record exists in the registry (or in an associated governance record) that documents which of the three routing options was selected (preserve as-is, resolve by accepting remaining side, or collapse), by which governance authority, and at what time. The routing decision was made under the conflict routing rules' WITHDRAWN-SIDE handling provisions, not under the standard conflict routing logic.

**Check (c) — Post-withdrawal detection conducted and recorded.** A conflict detection pass was conducted after the partial withdrawal, covering the post-withdrawal shared substrate composition. The results of that pass are recorded in the conflict registry: either new conflict entries attributed to the withdrawal as triggering event, or a governance record explicitly noting that post-withdrawal detection was conducted and returned no new conflicts. The absence of such a record is a governance gap, not evidence that no new conflicts exist.

A governance implementation that passes all three checks satisfies the composition requirements for Partial Withdrawal and Conflict Registry operating simultaneously. An implementation that fails any check has incomplete governance for at least one of the three composition-specific requirements.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Composition Pair 14: Partial Withdrawal and Conflict Registry.* Derivation Note #620, CKS Theory Series, Phase D4. May 15, 2026. ORCID: 0009-0004-8065-3235.
