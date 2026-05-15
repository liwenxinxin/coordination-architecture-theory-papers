# FAI Event Exit Rights and Governance Sovereignty

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes D2.46 of the CKS derivation series: the exit right that each participating Self's home governance holds over its ongoing Full Aspect Integration (FAI) relationship with another Self. D2.27 formalized per-event withdrawal — a Self withdrawing from a single FAI event. D2.46 addresses the broader relationship-level question: can a Self terminate the FAI relationship entirely, and what governance requirements govern that termination? The note derives D2.46 as an operational decomposition of D1.03 (the inter-Self governance perimeter) and D2.27 (partial participation and withdrawal). It defines the exit right and its four components, states the exit right as an expression of home governance sovereignty parallel to Paper 1 Claim 3's override right, specifies four governance requirements for exercising exit, states what governance records persist after exit, identifies the forced lock-in anti-pattern, and provides an operational test for a compliant exit.

---

## 1. Derivation context

### 1.1 Parent commitments

D2.46 derives from two parent commitments in the CKS derivation chain.

**D1.03** formalizes the inter-Self governance perimeter as a first-class architectural object. The inter-Self perimeter surrounds the participating Selves during a FAI event. Each participating Self's home governance perimeter remains intact within it; the inter-Self perimeter adds a coordination scope above the home perimeters without displacing them. D1.03 commits that each home governance perimeter retains its authority within the inter-Self scope — the inter-Self perimeter is a coordination extension, not a governance merger.

**D2.27** formalizes per-event withdrawal: a participating Self's governance right to withdraw from a specific FAI event, including the governance requirements for withdrawal and the dissolution consequences. D2.27 establishes that per-event withdrawal is a home governance act, requires no justification to the other participating Self, and triggers dissolution per D2.28 Trigger 3 when a participating Self exits during an active event.

**D2.46** addresses the dimension neither D1.03 nor D2.27 covers: the right to terminate the ongoing FAI relationship with another Self entirely — not merely withdrawing from one event, but ending the governance arrangement that enables future FAI events between the two Selves.

### 1.2 What this note adds

D2.27's per-event withdrawal right operates within the FAI relationship: a Self withdraws from one event; the relationship — the cross-organizational governance agreement, the standing configurations, the capacity to initiate future events — remains in place. D2.46 formalizes the exit right as the governance authority to end the relationship itself. The exit right is not a variant of per-event withdrawal; it is a distinct governance act that terminates the forward relationship while leaving the historical record intact.

---

## 2. The exit right defined

The exit right is each participating Self's home governance authority to take four termination actions:

1. **Active event termination.** Trigger dissolution of any active FAI events in which the exiting Self is a participant. The dissolution follows D2.02 governance requirements under the emergency dissolution trigger established in D2.28 Trigger 4 (joint governance decision with the exiting Self's exit as the trigger event).

2. **Standing configuration revocation.** Revoke any standing configurations (D2.21) with the other Self. Standing configurations are substrate content under the exiting Self's home governance; revocation is a home governance act over that content.

3. **Cross-organizational agreement termination.** Declare termination of the cross-organizational governance agreement (D2.34) per the agreement's own termination governance (D2.34 Component 5). If no such agreement exists, this action has no application.

4. **Future invitation declination.** Decline any future FAI event invitations from the other Self. The exiting Self is under no architectural obligation to respond to future FAI invitations from a Self it has exited a relationship with.

These four components together constitute the complete exit right. A governance arrangement that grants some but not all four — for example, one that allows active event termination but prevents standing configuration revocation — is a partial exit right, not a full exit right, and is assessed under the forced lock-in anti-pattern established in §5.

---

## 3. Exit right as governance sovereignty

The exit right is an expression of home governance sovereignty. It is not a negotiated permission, a consent-required procedure, or a contractual right that the other participating Self can architecturally withhold.

The parallel is Paper 1 Claim 3's override right: just as a Self's governance can override any substrate content at any time without justifying that override to the substrate system or to the LLM operating over it, a Self's governance can exit any FAI relationship without justifying the exit to the other participating Self. The override right and the exit right share the same architectural foundation: home governance sovereignty is not subordinate to the continued preferences of another party in a coordination arrangement.

Three corollaries follow from the sovereignty framing.

**No justification required to the other Self.** The exiting Self's governance decides to exit for whatever reasons its governance judges appropriate. Those reasons may be organizational strategy, a change in inter-organizational trust, concerns about the content emerging from FAI events, regulatory developments, or any other governance judgment. The architecture does not require the exiting Self to communicate or justify those reasons to the other participating Self. The other Self may request an explanation; the exiting Self may or may not provide one; neither position is an architectural requirement.

**The other Self cannot prevent exit.** The other participating Self holds no architectural veto over the exiting Self's exit right. An inter-Self governance arrangement that gives one Self the ability to prevent the other from exercising exit rights violates home governance sovereignty and falls under the forced lock-in anti-pattern (§5).

**No minimum notice period is architecturally required.** A cross-organizational governance agreement (D2.34) may include a notice-period commitment as a contractual term in the agreement's termination governance (Component 5). Such a term is admissible — it is a configurable element of a governance-agreed term. But the architecture itself does not impose a minimum notice period as a pre-condition of exercising the exit right. The exit right is available at any time for any reason.

---

## 4. Governance requirements for exit

Exercising the exit right is a home governance act that must satisfy four governance requirements. These requirements are not prerequisites that must be satisfied before the exit is legally effective — the exit is effective when the exiting Self's governance decides it is effective. The requirements are what make the exit a properly recorded governance act rather than an opaque operational termination.

### Requirement 1 — Exit declaration record

The exit decision is recorded in the exiting Self's home substrate as home governance content. The record includes the authorization (who in the home governance structure authorized the exit), the timestamp, the identity of the other Self, and the governance reasoning (whatever the home governance has chosen to record). The exit declaration record is the home-governance documentation of the exit decision. It is the source of truth for whether an exit has occurred and when it took effect.

The record need not be lengthy. A minimal compliant record identifies the exiting party, the other party, the authorization source, and the effective date. Detailed reasoning is admissible and may be valuable for internal governance continuity; it is not architecturally required.

### Requirement 2 — Active event dissolution

Any active FAI events with the exiting Self trigger emergency dissolution per D2.28 Trigger 4. The dissolution follows D2.02 governance requirements: each participating Self takes the content it is entitled to take under the dissolution governance of the event; the shared substrate dissolves; the four-locus evolution feed (D1.21) operates at dissolution.

The emergency dissolution triggered by exit is not a penalizing consequence — it is an architectural consequence of the fact that an active FAI event requires the ongoing participation of its constituent Selves, and a Self that has exercised its exit right is no longer an active participant. The dissolution must complete before the exit is fully effective at the event level, though the exit right itself is exercised at the home governance level independently.

### Requirement 3 — Standing configuration revocation

Standing configurations (D2.21) with the other Self are revoked as home governance acts. Each standing configuration that pre-approved FAI event parameters, aspect contribution profiles, or other inter-Self coordination parameters is substrate content in the exiting Self's home substrate. Revocation is a write operation over that content, recorded with authorization in the home substrate.

The revocation record identifies each revoked standing configuration, the authorization source, and the effective date of revocation. After revocation, no standing configuration with the exiting Self's signature can serve as the basis for a future FAI event invitation from the other Self.

### Requirement 4 — Agreement termination notice

If a cross-organizational governance agreement (D2.34) exists between the two Selves, the exiting Self follows the agreement's termination governance (Component 5). Every compliant cross-organizational governance agreement must include a termination clause per the anti-forced-lock-in commitment (§5); that clause governs the notice form and content. The termination notice is substrate content communicated through the shared substrate of any active event being dissolved (Requirement 2), or through formal organizational communication channel specified in the agreement, or through whatever formal channel the exiting Self's governance judges appropriate when no active event remains.

Where the agreement specifies a notice period, the exiting Self satisfies that commitment. The notice period is a contractual term within the agreement; it does not suspend the exit right itself at the home governance level.

---

## 5. What persists after exit

The exit right terminates the forward relationship. It does not retroactively delete, modify, or revoke what existed before exit. Three categories of prior content persist explicitly.

**Governance records from prior FAI events persist.** All governance records from completed FAI events — the seventeen categories established in D2.18 — persist per the persistence policies that governed those events at the time of dissolution. The exit right has no authority over what retention policies were established at event dissolution; those policies were executed when the events dissolved. An auditor reviewing the history of the FAI relationship after exit can access whatever governance records those persistence policies retained.

**Home-substrate evolution records persist.** DNA absorptions and action-layer ingestions that entered the exiting Self's home substrate from prior FAI events (via the four-locus evolution feed, D1.21) remain in the home substrate. The exiting Self's governance may modify, supersede, or remove those records under its own home governance authority — but the exit right does not automatically remove them. What was absorbed into the home substrate during the relationship remains part of the home substrate's history. The exit right terminates the future relationship; it does not undo the past evolution.

**Provenance chains remain navigable.** Provenance references in the exiting Self's home substrate that trace to prior FAI events with the other Self remain navigable for audit purposes. An auditor who needs to understand the provenance of a content item in the exiting Self's home substrate — where it came from, which FAI event contributed it, which aspect from which Self — can follow the provenance chain to its source even after exit. The exit right does not sever provenance chains; severing provenance chains retroactively would undermine the audit-continuity commitment the architecture is built to support.

Together, these three persistence properties mean that the complete history of the FAI relationship between the two Selves is auditable after exit. Exit changes the forward relationship entirely; it changes the historical record not at all.

---

## 6. Anti-pattern: forced lock-in

**Name:** Forced lock-in.

**Form:** A FAI governance arrangement — whether a standing configuration, a cross-organizational governance agreement, or a combination — that prevents a participating Self from exercising one or more components of the exit right established in §2.

**Examples of the anti-pattern:**
- A standing configuration that includes a provision stating it cannot be revoked without the other Self's consent.
- A cross-organizational governance agreement that lacks a termination clause, giving neither party a compliant exit path.
- A cross-organizational governance agreement whose termination clause requires the other party's affirmative approval for termination to take effect.
- A governance arrangement structured to make standing configuration revocation contingent on completing a new FAI event with the other Self.

**Why this violates the architecture.** Forced lock-in is not a configuration choice within the architecture's latitude; it is a violation of the home governance sovereignty commitment the architecture is built on. Paper 1 Claim 3's override right is unconditional: a Self's governance can override any substrate content at any time. The exit right is the override right applied at the FAI relationship level. Any governance arrangement that removes or conditions the exit right is structurally equivalent to a standing configuration that cannot be overridden — a direct violation of the unconditional override commitment.

The practical risk the anti-pattern creates is not hypothetical. In multi-organizational AI governance settings, a FAI relationship may involve significant coordination infrastructure — standing configurations, accumulated provenance chains, shared governance records — that create practical switching costs. The architecture protects against the possibility that those practical switching costs are converted into architectural obligations by removing the exit right. They are not. The exit right remains unconditional regardless of how deeply embedded the FAI relationship has become.

**Compliant design.** Every standing configuration must include a revocation clause that the owning Self can exercise unilaterally. Every cross-organizational governance agreement must include a termination clause (D2.34 Component 5) that the exiting Self can invoke without the other party's affirmative consent. Notice periods, wind-down obligations, and post-termination cooperation commitments are admissible as agreement terms; consent-gated termination is not.

---

## 7. Operational test

For a Self that has exercised exit rights, an observer verifying compliance with D2.46 asks the following questions:

1. **Exit declaration record present?** Is there a record in the exiting Self's home substrate that identifies the exit decision, names the other Self, records the authorization source, and carries a timestamp?

2. **Active event dissolution records present?** For each FAI event that was active at the time of exit, is there an emergency dissolution record (per D2.28 Trigger 4) showing that dissolution completed per D2.02 governance requirements?

3. **Standing configuration revocation records present?** For each standing configuration the exiting Self held with the other Self, is there a revocation record in the home substrate identifying the configuration, the authorization, and the effective date?

4. **Agreement termination notice executed?** If a cross-organizational governance agreement was in effect, did the exiting Self provide termination notice per the agreement's termination governance (Component 5)?

5. **Provenance chains intact?** Do provenance references in the exiting Self's home substrate that trace to prior FAI events with the other Self remain navigable?

A compliant exit satisfies all five questions affirmatively. A failed exit — one where no exit declaration record exists, where active events were abandoned rather than dissolved, or where standing configurations were silently invalidated without revocation records — is not a compliant exercise of the exit right. It is an operational termination without governance documentation, which undermines the audit-continuity that the persistence requirements in §5 are designed to preserve.

---

## 8. Relationship to D2.27 and forward derivations

D2.27's per-event withdrawal right and D2.46's exit right are related but distinct governance acts. D2.27 operates within the FAI relationship: the participating Selves remain in a governance relationship after per-event withdrawal; the relationship's standing configurations and cross-organizational agreement remain in effect; future events remain possible. D2.46 terminates the relationship: standing configurations are revoked, the agreement is terminated, and future events require a new relationship to be established from the beginning.

A Self may exercise per-event withdrawal multiple times within an ongoing FAI relationship (D2.27). Each per-event withdrawal is a home governance act that does not imply exit. A pattern of repeated per-event withdrawals may be evidence that the FAI relationship is not functioning as the participating Selves' governance intends — which may lead a Self's governance to exercise the exit right — but no number of per-event withdrawals constitutes automatic exit. Exit is a distinct governance act, governed by the four requirements of §4 and recorded as an exit declaration (Requirement 1).

The exit right established in D2.46 does not foreclose a future FAI relationship between the same two Selves. After exit, the two Selves may establish a new cross-organizational governance agreement (D2.34), define new standing configurations (D2.21), and conduct new FAI events. The new relationship is a new governance arrangement with its own provenance chain; it does not automatically reinstate the prior relationship or inherit its configuration state. Whether and under what terms a new relationship is established is entirely within each Self's home governance authority — which is precisely what the exit right protects.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Event Exit Rights and Governance Sovereignty.* May 15, 2026. ORCID: 0009-0004-8065-3235.
