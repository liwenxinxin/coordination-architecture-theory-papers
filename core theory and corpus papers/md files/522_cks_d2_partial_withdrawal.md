# Partial Participation and Withdrawal Governance

**Series:** CKS Derivation Note Series — Phase D2, Note D2.27 (#522)
**Parent Notes:** D1.03 (Inter-Self Governance Perimeter), D1.25 (Joint Authority over FAI Configuration)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When a participating Self exercises its home governance authority to reduce or end its participation during an active Full Aspect Integration (FAI) event, the architecture requires that act to be governed — producing a withdrawal record in the shared substrate, notifying other participants, preserving the provenance of prior contributions, and leaving the remaining participants' governance with defined response options. This note formalizes the two withdrawal types, five governance requirements that together distinguish governed from ungoverned withdrawal, the full withdrawal implications for remaining participants, and the governance sovereignty basis on which the right to withdraw rests. The anti-pattern — ungoverned withdrawal, in which a Self's contributions disappear from the shared substrate without a governance record — is identified and its failure mode stated. An operational test closes the note.

---

## 1. Derivation context

D1.03 committed that each participating Self's home governance perimeter remains intact during an FAI event. The inter-Self perimeter that surrounds participating Selves during an active event does not dissolve, subordinate, or merge home governance perimeters; each Self's governance authority over its own aspects and substrate content continues unmodified for the duration of the event.

D1.25 committed that the FAI configuration governs joint authority. Configuration dimensions — sharing scope, cardinality, persistence policy, conflict-handling rules, dissolution conditions — are substrate content under the joint authority of all participating Selves' governance. Changes to those dimensions during an active event are joint-authority governance acts.

D2.27 derives from these two parent commitments and formalizes what happens when a participating Self's home governance decides, during an active FAI event, to reduce or end its participation. The question D2.27 answers is structural, not exceptional: any architecture that preserves home governance sovereignty during inter-Self coordination must specify what it means for home governance to exercise that sovereignty against continued participation, and must define what the shared substrate retains afterward.

---

## 2. Two withdrawal types

**Type 1 — Partial withdrawal.** A participating Self withdraws some, but not all, of its contributed aspects from the shared substrate during an active event. The Self remains a participant; its remaining contributed aspects stay active; only the specified withdrawn aspects are retracted from active contribution status. Partial withdrawal may occur for any number of governance reasons: the contributing Self's governance discovers that contributed aspects contain content whose sensitivity was not anticipated at contribution time; the organizational context that motivated contributing certain aspects changes during the event; governance determines that a specific subset of its contributions should no longer be treated as active input to merge operations or conflict resolution.

**Type 2 — Full withdrawal.** A participating Self withdraws entirely from the FAI event before the event reaches dissolution. All of the withdrawing Self's contributed aspects are retracted from active contribution status. Full withdrawal may occur for similar governance reasons scaled to the participation decision as a whole, or for reasons affecting the Self's judgment about the event's purpose, the other participants, or the inter-Self configuration itself.

Both types are exercises of home governance authority over home participation decisions. The distinction between them is one of scope — which aspects are retracted — not one of procedural kind. Both require the same five governance requirements described in Section 3.

---

## 3. Five governance requirements

The following five requirements jointly define what makes a withdrawal a governed act. A withdrawal satisfying all five is a governed withdrawal. A withdrawal failing any one of them — particularly Requirements 1 and 3, which establish the governance record — is ungoverned withdrawal.

**Requirement 1 — Withdrawal as governance act.** Partial or full withdrawal is an exercise of the modify right over shared-substrate content. It is not a passive cessation or a technical dropout. Home governance must authorize the withdrawal, and that authorization must be attributable to identifiable governance authority within the withdrawing Self's home perimeter. The modification right at inter-Self scope — the same right that governs any change to what a Self has contributed to the shared substrate — governs withdrawal. A withdrawal not authorized and recorded under home governance does not satisfy this requirement.

**Requirement 2 — Joint notification via the shared substrate.** Withdrawal must be communicated to other participating Selves' governance through the shared substrate itself. The shared substrate is the coordination medium; communication of a governance act affecting the shared substrate must travel through that medium, not through a side channel. Other participants' governance holds the inspect right over shared-substrate content and will observe the withdrawal record. Notification is not a courtesy: it is a structural consequence of the inspect right. A participating Self that withdraws without producing a substrate-level record reachable through other participants' inspect right fails this requirement regardless of any out-of-band communication.

**Requirement 3 — Withdrawal record content.** The withdrawal record created in the shared substrate must contain four elements: (a) which aspects were withdrawn — identified specifically, not by category or implication; (b) which Self's governance authorized the withdrawal — attributed to the withdrawing Self's governance perimeter; (c) when the withdrawal occurred — a timestamp that places the withdrawal in the event's timeline relative to prior contributions and merge operations; (d) under what governance authorization the withdrawal was made — the authorization reference that makes the withdrawal traceable to a home governance act rather than to an automated process, a technical failure, or an unauthorized agent.

**Requirement 4 — Contributed content treatment.** Content already contributed to the shared substrate at the time of withdrawal is not deleted. Contributed content that pre-dates the withdrawal is part of the shared substrate's governance record, and its provenance chain is not severed by the contributing Self's subsequent withdrawal. The treatment differs by withdrawal scope. For partial withdrawal: the withdrawn aspects' contributions are flagged as withdrawn-by-contributing-Self in the conflict registry and contribution records; their content remains in the shared substrate, accessible to other participants' inspect right, but is no longer treated as active contributions going forward — it is not input to new merge operations and is not the active position of the contributing Self in subsequent conflict resolution. For full withdrawal: all of the withdrawing Self's contributed aspects are flagged as withdrawn under the same regime. In both cases, the content remains with its provenance intact; it is the contribution's status that changes, not its existence in the governance record.

**Requirement 5 — Impact on merge operations.** Withdrawal after merge operations have already occurred requires governance attention. Merged content that incorporated the withdrawn aspects' contributions carries provenance that now links to withdrawn material. Where conflicts were resolved — through the orchestration tier of three-tier conflict handling — using the withdrawn aspects' content as input to that resolution, the merged output may need re-evaluation. Remaining participants' governance must consider whether conflict resolutions based substantially on now-withdrawn content should be revisited, preserved with annotation, or escalated for fresh governance determination. This requirement does not mandate re-running prior merges; it requires that the withdrawal record trigger governance attention to prior merge outputs where the withdrawn content was material.

---

## 4. Full withdrawal implications: three response options

When a Self fully withdraws from an active FAI event, the remaining participating Selves' governance must determine how to proceed. Three architecturally distinct responses are available:

**Continue.** The remaining participants' governance determines that the FAI event's purpose can still be achieved without the withdrawing Self. The event continues with reduced cardinality. No amendment to the FAI configuration is strictly required if the event's purpose and the remaining contributions support continuation under the existing configuration. The withdrawal record in the shared substrate documents the changed participant set. This option is available when the withdrawing Self's contributions were not structurally necessary to the event — when the remaining aspects support the merge and conflict-handling operations the event was configured to perform.

**Amend the configuration.** The remaining participants' governance determines that continuation is appropriate but that the FAI configuration should be updated to reflect the reduced cardinality. Configuration amendment is a joint-authority governance act under D1.25 — all remaining participants' governance must authorize the amendment, and the amended configuration is substrate content. Grounds for choosing this option over simple continuation include: the original configuration assumed a specific cardinality in its conflict-handling rules or merge pattern variant; the withdrawal changes the balance of governance authority among participants in a way the original configuration does not accommodate; or the remaining participants' governance judges that an explicit configuration update better reflects the event's operating conditions going forward.

**Dissolve.** The remaining participants' governance determines that the withdrawing Self was essential to the event's purpose and that continuation without it is not appropriate. Dissolution follows the dissolution mechanism specified in the FAI configuration. Content disposition at dissolution follows the configured persistence policy. This option is not a failure mode; it is the governed outcome when a withdrawal makes an event's purpose unachievable or makes continued operation under the existing configuration ungoverned.

The choice among these three options is a joint governance decision by the remaining participants. No single remaining participant's governance can unilaterally compel continuation or dissolution against the judgment of others; the joint-authority commitment of D1.25 applies to this decision as to any other configuration-level determination.

---

## 5. Governance sovereignty of withdrawal

The right to withdraw is an exercise of home governance sovereignty. It is structural, not conditional.

A participating Self does not require permission from other participants to withdraw. Withdrawal is the exercise of home governance authority over a home participation decision — the decision whether this Self continues contributing to this event. Other participants' governance may prefer that the withdrawing Self remain; that preference does not override the withdrawing Self's governance determination.

This parallels Paper 1 Claim 3's override right. Paper 1 established that human governance holds the right to override any orchestration-layer determination without providing justification to the orchestration layer. The withdrawal right operates at the same register: just as the override right does not require governance to justify its override to the system being overridden, the withdrawal right does not require governance to justify its withdrawal to other participants. Governance decides; governance acts; governance records.

The justification-not-required character of the withdrawal right does not eliminate the governance record requirements of Section 3. The no-justification-required commitment means withdrawal does not require governance to produce reasons for other participants; it does not mean withdrawal requires no governance record at all. Requirements 1 through 5 establish what makes withdrawal a governed act — they operate as procedural architecture, not as conditions on the substantive governance decision. Home governance may decline to explain its reasons while fully satisfying all five requirements.

---

## 6. Anti-pattern: ungoverned withdrawal

**Definition.** Ungoverned withdrawal occurs when a participating Self's aspects become absent from the shared substrate without a withdrawal record satisfying the five requirements of Section 3. Content disappears; no withdrawal record is produced; no governance authorization is attributable; no notification reaches other participants through the shared substrate.

**Failure mode.** Ungoverned withdrawal violates contribution record integrity and the provenance chain. Other participants' governance inspects the shared substrate and observes that aspects previously present are no longer present, but finds no withdrawal record explaining why. The shared substrate's state cannot be attributed to a governance act. Conflict resolutions that incorporated the now-absent content have provenance that leads to content whose status is unknown — it was not withdrawn in a governed way, but it is no longer present. The governance record of the event is broken.

**Two common forms.** Form 1: technical failure or network dropout causes a Self's contributions to become inaccessible without any governance record being produced. This is ungoverned withdrawal even if unintentional; the architecture's requirement is that any absence of contributed content be attributed to a governance act. Form 2: a Self's governance informally decides to stop contributing — perhaps through out-of-band communication with other participants' governance — but does not produce a withdrawal record in the shared substrate. The informal communication may be genuine, but the shared substrate does not carry it; the governance record of the event does not reflect it.

**Distinction from governed withdrawal.** Governed withdrawal and ungoverned withdrawal produce the same observable outcome in one sense: the withdrawing Self's contributions are no longer active. They differ structurally in what the shared substrate retains. Governed withdrawal leaves a withdrawal record, flagged contribution records with intact provenance, and a governance-attributable change to the event's state. Ungoverned withdrawal leaves an absence — a gap in the governance record that subsequent governance actors cannot interpret, rely on, or trace.

---

## 7. Operational test

For a FAI event in which a withdrawal occurred, an observer reviewing the shared substrate should be able to answer the following questions affirmatively for the withdrawal to be governed:

1. Is there a withdrawal record in the shared substrate identifying which aspects were withdrawn, by which Self's governance, at what time, and under what governance authorization?

2. Are the withdrawn aspects' prior contributions accessible in the shared substrate with their provenance intact, and are they flagged as withdrawn-by-contributing-Self in the contribution records and conflict registry?

3. If merge operations incorporated the withdrawn aspects' content before withdrawal, is there governance attention documented in the shared substrate addressing those prior merge outputs — whether in the form of re-evaluation, preserved annotation, or escalation?

4. Is there a documented governance decision by the remaining participants — continue, amend the configuration, or dissolve — reflecting a joint governance determination made after the withdrawal?

A FAI event failing any of these four checks has a withdrawal governance gap at the failing check. A FAI event satisfying all four has a fully governed withdrawal record.

---

*D2.27 is one of approximately 80 Phase D2 notes in the CKS derivation series. Phase D2 notes are operational decompositions of Phase D1 sub-commitments. This note derives from D1.03 and D1.25.*
