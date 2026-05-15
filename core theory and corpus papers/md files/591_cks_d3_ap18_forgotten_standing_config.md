# AP-18: Forgotten Standing Configuration

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

A standing configuration is the substrate artifact that governs how Full Aspect Integration (FAI) events run — what aspects are contributed, under what sharing scope, with what escalation routing, and at what conflict thresholds. Paper 3 Claim 5 commits to configuration as substrate content: all configurable dimensions of the FAI mechanism are themselves substrate content, authored under joint governance authority and subject to all six Paper 1 commitments. The Forgotten Standing Configuration anti-pattern (AP-18) is the failure mode in which a standing configuration was jointly authorized at some point in the past, but has never been reviewed since. The participating Selves' governance architectures, organizational contexts, and coordination structures have evolved; the standing configuration has not. FAI events continue to run under this frozen historical artifact without governance awareness that the configuration no longer reflects current governance intent. This note formalizes AP-18 as the fourth of five Taxonomy Category 4 (Configuration Failure) anti-patterns. It states the description, detection criteria, governance commitment violated, consequences, intra-Self analog, and resolution.

---

## 1. Anti-Pattern Name and Category

**AP-18: Forgotten Standing Configuration**
**Category:** Taxonomy Category 4 — Configuration Failure

---

## 2. Description

A standing configuration (D2.21) is the substrate artifact that encodes governance intent for a recurring class of FAI events. When two or more Selves engage in FAI events on a regular or predictable basis, jointly authoring a standing configuration is the efficient governance move: rather than configuring each event individually, governance authors one configuration artifact that applies across events of the specified type, subject to per-event override. The standing configuration is substrate content under Paper 3 Claim 5 — it carries all six Paper 1 commitments, including inspectability, human-governed authority, and the right to modify or override at any time.

AP-18 is the failure mode that arises when a standing configuration, once jointly authorized, is never revisited. The authorization act is historical; the governance intent that motivated it was current at the time of authoring; but governance intent is not static. Participating Selves restructure their aspect registries. Governance practitioners move into or out of roles. Organizational priorities shift. Coordination patterns that once dominated a relationship give way to new ones. The substrate evolves; the standing configuration does not.

The defining characteristic of AP-18 is not that the standing configuration is wrong in any detectable per-event sense — it may produce FAI events that appear to run normally. The defining characteristic is that governance is no longer actively governing the configuration. The configuration governs itself through inertia. It is still formally authored substrate content; Paper 1's authorship criterion is technically satisfied. But it no longer expresses current governance intent. This is the subtle form of AP-6 (implicit configuration) that AP-18 represents: the problem is not the absence of a configuration, but the decoupling of an existing configuration from the governance intent it was written to encode.

The mechanism of decoupling is time. Governance intent does not broadcast its own changes. Nothing in the substrate automatically detects that a governance practitioner has left a role, that an aspect no longer exists in a contributing Self's home substrate, or that a sharing scope that was once appropriate is now too broad or too narrow. The standing configuration persists, unchanged, as the accumulation of small unreflected changes in the Selves' governance architectures converts a carefully authored artifact into a historical curiosity that runs FAI events under conditions its original authors would no longer endorse.

---

## 3. Detection Criteria

Five detection signals indicate that a standing configuration may be in AP-18 territory:

**Elapsed review window.** The standing configuration's last review or amendment timestamp exceeds the review cadence the configuration itself specifies (D2.21 Requirement 5). Where no review cadence was specified, the standing configuration has no scheduled review mechanism at all — itself a configuration authoring deficiency.

**Absent aspects.** The standing configuration specifies aspects for contribution that no longer exist in one or more contributing Selves' home substrates, because the Selves have restructured their aspect registries (D2.55) since the configuration was authored. The standing configuration commits the Selves to share content that no longer exists as specified.

**Stale escalation routing.** The escalation routing in the standing configuration references governance practitioners who have left their roles. An FAI event requiring escalation under this configuration routes to an empty seat. The result is an escalation failure (AP-11 may follow).

**Unactioned post-mortem findings.** Post-mortem reviews (D2.39) conducted after FAI events run under this configuration consistently identify configuration gaps — wrong conflict thresholds, inappropriate sharing scope, stale aspect references — but no amendments to the standing configuration follow. The gap between observed configuration deficiency and substrate amendment is the signature of AP-18's inertia.

**Absence of review confirmation records.** A standing configuration that remains current over time should have a record of being confirmed as current — governance practitioners reviewing it and producing a review confirmation record that attests their deliberate judgment that the configuration still reflects governance intent. The absence of review confirmation records since the configuration's creation date is itself a detection signal: it is the difference between a configuration that has been confirmed as current and a configuration that has merely not been amended. These are not the same thing.

---

## 4. Governance Commitment Violated

**Primary: Paper 3 Claim 5 — configuration as substrate content.**

Claim 5 commits to configuration as substrate content under all six Paper 1 commitments, with joint governance authority over every configurable dimension of the FAI mechanism. The commitment is not satisfied by the one-time authorship of a standing configuration. Claim 5's substrate-content commitment carries the full Paper 1 governance architecture: the right to inspect, modify, and override at any time. A standing configuration that is never reviewed is, in operational effect, a configuration whose modify and override rights are not being exercised. Governance has withdrawn from active governance of the configuration without formally surrendering the configuration. The configuration is substrate content in form; it is ungoverned content in practice.

This is the sense in which AP-18 represents a Claim 5 violation at the subtlest level: the configuration exists as substrate content, was jointly authored, and carries the appropriate authorship record. But Paper 1's human-governed commitment is temporal — the rights must be available and exercised at any time, not only at the moment of initial authorship. A standing configuration that governance has functionally abandoned is one whose governance authority has lapsed in practice even while remaining formally intact.

**Secondary: Paper 3 Claim 1 — joint authority across participating Selves' governance.**

The joint authorization of a standing configuration represents the governance intent of the participating Selves at the time of authorization. Governance authority is current, not historical. The joint authorization does not constitute a permanent delegation of governance intent to the configuration. As the participating Selves' governance architectures evolve, the original joint authorization becomes a record of past governance intent rather than an expression of present governance authority. Running FAI events under a standing configuration that neither participating governance has recently confirmed is running those events under historical joint authority rather than current joint authority.

**Operational reference: D2.21, Requirement 5** — review cadence as a required element of every standing configuration.

---

## 5. Consequences

**FAI events run under outdated governance conditions.** The sharing scope, aspect selection, conflict thresholds, and escalation routing active during FAI events reflect the governance intent at the time of configuration authoring, not the governance intent at the time of event execution. Governance may now want to restrict sharing that the configuration authorizes, or expand sharing that the configuration constrains. In either direction, the FAI event produces outcomes governance would not currently sanction.

**Escalation failures.** Where the standing configuration's escalation routing references practitioners who have left their roles, escalation events during FAI execution route to vacant seats. The result is an escalation routing failure under AP-11's pattern: an event requiring human governance judgment reaches no human. The downstream governance risk of an unresolved escalation is borne by both participating Selves without either governance being aware of the gap.

**Wrong-tier conflict routing.** Conflict routing rules authored at configuration time may be inappropriate for the evolved governance architectures of the participating Selves. Conflicts that now warrant escalation may be routed to orchestration resolution; conflicts that could now be handled at orchestration may be escalated unnecessarily. The routing rule is correct for a governance architecture that no longer exists.

**Misleading trust calibration signals.** Governance trust calibration (D2.29) between participating Selves is informed by the standing configuration's content. If the standing configuration's sharing scope, aspect selection, and conflict thresholds reflect historical governance intent rather than current governance intent, the trust signals it generates are artifacts of configuration history rather than genuine expressions of current governance posture. Partner Selves calibrate their trust relationship against a governance position that the other governance has effectively abandoned.

---

## 6. Intra-Self Analog

The intra-Self analog is Paper 2 orchestration rules that no longer reflect governance intent. Within a single Self, orchestration rules govern cell-level behavior: who can modify the substrate, how conflicts are handled, what the AI is authorized to do on the substrate's behalf. These rules are authored by governance at a point in time. As the Self's coordination work evolves, the governance intent that produced the original rules may shift — but if no governance review occurs, the rules continue to govern cell behavior under conditions their authors would no longer endorse.

Paper 2 identifies this failure mode as the primary motivation for the governance modification right: governance must be able to update orchestration rules to match current intent, and the architecture must preserve that right at all times. The modification right is not useful if governance never exercises it; the architecture's preservation of the right does not substitute for the governance act of review and amendment when the rules' scope has drifted from current intent.

AP-18 is the inter-Self scope version of the same failure mode. The standing configuration is the inter-Self analog of intra-Self orchestration rules: both are human-authored substrate content encoding governance intent for a class of recurring operations; both are subject to Paper 1's modification and override rights; both become frozen historical artifacts when governance does not exercise those rights on a scheduled basis. The intra-Self case is one governance perimeter failing to maintain its own rules; the AP-18 case is two or more governance perimeters jointly failing to maintain their shared configuration.

---

## 7. Resolution

**Prevention: D2.21 review cadence requirement.** Every standing configuration should specify a review cadence as a required authoring element (D2.21 Requirement 5). The review cadence is a governance commitment made at the time of configuration authoring: governance agrees to revisit the configuration on a specified schedule. The schedule is substrate content; its presence in the configuration is itself a detection criterion for the absence of AP-18.

**The review confirmation record.** When governance conducts a scheduled review and determines that the standing configuration remains current, they should produce a review confirmation record: a substrate artifact recording that governance practitioners from both participating Selves deliberately reviewed the configuration, found it to reflect current governance intent, and confirmed it without amendment. The review confirmation record is the positive governance artifact that distinguishes an actively governed standing configuration from one that has merely not been amended. The absence of review confirmation records since a configuration's creation date is the AP-18 detection signal even when the configuration's content happens to be technically accurate.

**The post-mortem → amendment cycle.** Post-mortem reviews (D2.39) conducted after FAI events are the natural review trigger for standing configurations. Post-mortems generate operational intelligence about configuration gaps that only become visible under real event conditions: escalation routes that failed to reach a living practitioner; conflict thresholds that routed incorrectly; aspect references that returned empty. This intelligence is the input to standing configuration review. The healthy governance cycle is: FAI event execution → post-mortem review → standing configuration review (confirm or amend) → review confirmation record or amendment record (D2.38) as appropriate. AP-18 is what happens when post-mortem intelligence accumulates evidence of configuration gaps and the cycle between post-mortem finding and standing configuration amendment is never completed.

**Amendment mechanics.** Where a standing configuration review produces amendments, the amendments are authored as amendment records (D2.38) under the same joint governance authority that produced the original configuration. Amendments do not replace the configuration's authorship history; they extend it. The amended configuration carries the full record of its evolution: original authorship, subsequent reviews, and each amendment with its authoring governance and its articulated governance rationale. This record is what allows governance of either participating Self to reconstruct the configuration's governance history and understand what intent each version encoded.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-18: Forgotten Standing Configuration.* May 15, 2026. ORCID: 0009-0004-8065-3235.
