# AP-11: Unresponsive Escalation

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

AP-11 formalizes the Unresponsive Escalation anti-pattern: a failure mode in which conflict registry entries escalated to the human governance tier during a Full Aspect Integration (FAI) event receive neither a governance response nor a triggered default action within the configured response timeline. The escalate tier is architecturally present but operationally non-functional. The pattern violates Paper 1 Claim 3's human-governed authority commitment and Paper 3 Claim 3's escalate-to-humans tier. The root cause is most often governance capacity overextension: the organization is running more FAI events than its governance practitioners can service. The architectural safeguard is the configured default action, whose absence or non-execution is the proximate mechanism of failure. A compounding consequence is the cultural erosion of the escalate tier itself: practitioners who learn that escalations go unanswered route fewer items upward, degrading the three-tier mechanism over time.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-11 — Unresponsive Escalation

**Category:** Taxonomy Category 2 — Conflict Handling Failures (the second of four Category 2 anti-patterns in Phase D3)

**One-line statement:** The escalate tier is present in the architecture but non-functional in practice — escalated conflicts accumulate without receiving governance responses or triggering default actions.

---

## 2. Description

Paper 3's three-tier inter-Self conflict-handling mechanism (Claim 3) commits, at the escalate tier, that conflicts which cannot be resolved by prebuilt orchestration rules are surfaced to the joint human governance arrangement spanning participating Selves' home governance structures. This commitment is structural: escalation is not a best-effort signal but an invocation of governance authority over a conflict the architecture has judged to require human decision. The commitment implies that a response path exists and functions — escalation events reach practitioners who are reachable and capable of responding within the configured response timeline.

AP-11 names the failure mode in which this implication is violated. Conflict registry entries carry an ESCALATED status. The configured response timeline expires. Neither a human governance response nor the automatic default action materializes. The entries remain in ESCALATED status indefinitely. The escalate tier is structurally intact in the configuration but operationally non-functional.

The proximate mechanism has two paths. Every FAI event configuration is required to specify a default action — preserve-and-continue (the event proceeds with the conflict in first-class substrate state) or early dissolution (the event terminates at the expiry point) — to be triggered automatically when the timeline expires without a human response. AP-11 therefore requires one of two sub-failures: either (a) no default action was configured (an implicit configuration failure analogous to the AP-6 class), leaving the architecture with no fallback, or (b) a default action was configured but the orchestration layer did not execute it at timeline expiry. Both sub-failures share the same observable signature but carry different remediation implications.

The root cause is most often an organizational condition rather than a configuration error: governance practitioners across participating Selves' home governance structures are insufficient to service the volume of escalated conflicts the organization's FAI event frequency generates. Unresponsive escalation is the visible symptom of this overextension, appearing first as occasional timeline breaches and then as a persistent backlog that practitioners have tacitly stopped monitoring.

---

## 3. Detection Criteria

A deployment exhibits AP-11 when all of the following hold simultaneously:

- **Criterion 1 — Aged ESCALATED entries.** Conflict registry entries carry ESCALATED status with timestamps showing the configured response timeline has been exceeded; not in RESOLVED, PRESERVED, or DISSOLVED status.
- **Criterion 2 — No governance response record.** No response record exists for the aged entries. The protocol specifies four response forms (D2.14 Option 1–4: directed resolution, acceptance of a resolution proposal, default action invocation, dissolution instruction); none is present.
- **Criterion 3 — No default action record.** The configured default action was not triggered at timeline expiry. If it had executed, the entry would carry PRESERVED or DISSOLVED status, not ESCALATED. Its absence distinguishes AP-11 from a governed-but-slow response.
- **Criterion 4 — Escalation notification records without corresponding response records.** The governance notification log shows escalation was dispatched but no corresponding response record exists — distinguishing AP-11 from notification routing failure and confirming the failure is at the response stage.

Secondary indicators frequently accompanying AP-11 include a growing ratio of ESCALATED-to-resolved entries across recent FAI events, practitioners unfamiliar with outstanding escalations, and events concluding with open ESCALATED conflict registry entries.

---

## 4. Governance Commitment Violated

**Primary — Paper 1 Claim 3, human-governed authority.** The human-governed commitment requires that humans retain the right to inspect, modify, and override substrate content and orchestration rules at any time. When the escalate tier invokes human governance authority over a conflict, the structural commitment is that human governance authority is reachable and can be exercised. An escalation that receives no response — neither a human decision nor a triggered default — is an invocation of governance authority that goes unanswered. This is not merely a workflow failure; it is a structural violation of the human-governed commitment at the tier where human authority is most directly engaged.

**Secondary — Paper 3 Claim 3, Tier 3, escalate-to-humans.** The escalate tier's fresh Paper 3 content is the cross-perimeter shape of escalation: conflicts surface to the joint-governance arrangement of participating Selves' home governance structures. This cross-perimeter escalation is an architectural commitment, not a routing suggestion. A non-functional escalate tier does not merely underperform; it cancels the architectural guarantee that unresolvable inter-Self conflicts have a governed path to resolution.

**Operational reference — D2.14, escalation routing and response protocol.** D2.14 specifies both the response timeline requirement and the default action requirement; AP-11 violates both simultaneously.

---

## 5. Consequences

**First-order operational harm.** Conflicts requiring governance resolution remain unresolved. If the FAI event continued past the point where the escalated conflicts were relevant to its outputs, those outputs were produced in an ungoverned state. If the event is ongoing, it is operating outside its governed state: the architecture specifies that conflicts at the escalate tier require human governance attention, and that attention has not been provided.

**Governance record integrity.** The FAI event's governance record contains open governance authority invocations — escalations dispatched but never closed by response, default action, or dissolution. This is a substantive audit finding: the record cannot truthfully represent the event as fully governed, and downstream uses of the event's outputs that rely on the record's integrity are affected.

**Second-order compounding consequence — escalate tier degradation.** This consequence is qualitatively distinct from the first-order operational harm. Governance practitioners who observe that escalations go unanswered adapt their behavior: they route fewer conflicts to the escalate tier, raise the internal threshold for what justifies escalation, or develop informal bypasses. This adaptation is individually rational but collectively harmful. The three-tier mechanism's effectiveness depends on the escalate tier actually functioning. When practitioners learn it does not function reliably, the tier becomes nominal rather than operational. The architecture retains its three-tier structure on paper while the live conflict-handling mechanism has effectively become two-tier. This degradation is difficult to reverse because it is embedded in organizational practice rather than in configuration.

**Governance capacity failure risk.** If escalation backlogs accumulate, the governance capacity failure condition (D2.28 Trigger 1) may be reached, requiring emergency dissolution of the FAI event — a higher-severity outcome that may affect participating Selves' operations beyond the immediate event.

---

## 6. Intra-Self Analog

AP-11 does not have an exact Paper 2 intra-Self analog. Within a single Self, escalation runs through the Self's internal governance hierarchy — a path that does not cross an inter-Self perimeter and does not require joint authority across distinct home governance structures. The cross-perimeter shape of the Paper 3 escalate tier, and the coordination demands it places on governance capacity across multiple organizations, has no direct counterpart in the intra-Self setting.

The closest intra-Self analog is the general failure mode of governance practitioners not acting on governance items — for example, directed selection proposals undecided past their window, or conflict registry entries in a multi-cell Self escalated to a senior governance layer and not addressed. This analog is structurally weaker: within a single Self, the governance pathway is internal and enforceable by organizational hierarchy and tooling without cross-perimeter coordination. The inter-Self governance capacity challenge — requiring multiple organizations to maintain responsive governance practitioners under joint-authority arrangements — is a genuinely new coordination burden the intra-Self analog does not illuminate.

AP-11 is therefore primarily a consequence of the inter-Self governance capacity challenge rather than a general governance discipline failure that would appear at both scopes.

---

## 7. Resolution

Resolution for AP-11 operates at two levels: prevention (addressed architecturally before events run) and remediation (addressed operationally after AP-11 is discovered). Below these, root-cause resolution addresses the underlying governance capacity condition.

### Prevention

**Configure the default action.** Every FAI event configuration must specify a default action — preserve-and-continue or early dissolution — before the event runs. This specification is not optional and cannot be deferred to event runtime. Its absence means no fallback exists if human response does not arrive: the configured default action is the mechanism that closes the escalated entry's governance lifecycle at the timeline boundary even when human governance practitioners are unreachable.

**Verify default action execution.** Configurations that specify a default action but require a manual trigger to execute it do not satisfy the requirement. Execution must be automatic on timeline expiry. This verification should be part of FAI event configuration review.

**Set response timelines that match governance capacity.** The configured response timeline must reflect the actual responsiveness of practitioners across participating Selves' home governance structures, not an aspirational target. Calibrating the timeline to governance capacity is part of event configuration.

### Remediation for Discovered Unresponsive Escalation

**Immediately invoke governance responses for outstanding escalated conflicts.** For every conflict registry entry in ESCALATED status with an exceeded timeline, a governance response must be produced and recorded. The four response options remain available (D2.14 Option 1–4). If the FAI event is ongoing, the response should be applied promptly. If the event has concluded, the response should be recorded to close the open invocation.

**Trigger emergency dissolution if the event has progressed past useful response.** If the FAI event has advanced to a stage where governance responses can no longer meaningfully affect outputs, the appropriate remediation is emergency dissolution (D2.28 Trigger 2), with the cause recorded in the governance record.

### Root-Cause Resolution — Governance Capacity Assessment

Neither immediate remediation nor configuration improvements address the underlying condition producing AP-11 at scale: an organization conducting more FAI events than its governance practitioners can service. If AP-11 appears as a pattern across multiple events rather than an isolated incident, the appropriate response is a formal governance capacity assessment (D2.33).

The assessment determines whether capacity — qualified practitioners available across participating Selves' home governance structures, their response bandwidth, and the coordination arrangements in place — is sufficient for the volume and escalation rate of current events. Two remediation paths follow: reducing FAI event frequency to match existing capacity, or expanding capacity (adding practitioners, improving tooling, streamlining cross-perimeter coordination). The assessment should also confirm that escalation routing is functioning and that escalation thresholds are calibrated, to rule out over-escalation as a contributing factor.

Governance capacity assessment is not a one-time remediation; it should be revisited whenever FAI event volume changes materially.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-11: Unresponsive Escalation.* May 15, 2026. ORCID: 0009-0004-8065-3235.
