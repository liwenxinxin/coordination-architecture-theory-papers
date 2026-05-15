# AP-6: Implicit Configuration

**Series D — Phase D3 Anti-Pattern Formalizations, Note #588**
**Category 4: Configuration Failures — Opening Note**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

AP-6 (Implicit Configuration) names the failure mode in which a Full Aspect Integration (FAI) event operates without an authored configuration substrate. The six configurable dimensions specified in Paper 3 Claim 5 (D1.22) are not present as authored governance content — they are either absent entirely or implicitly determined by infrastructure defaults. This note formalizes the anti-pattern, identifies its detection criteria, traces the governance commitments it violates, catalogs its consequences, states its intra-Self analog, and specifies the resolution. AP-6 is the foundational configuration failure: the anti-pattern from which AP-1 (Ungoverned Construction), AP-11 (Unresponsive Escalation), and AP-12 (Informal Resolution Rules) can develop as co-occurring or downstream failures. A FAI event operating under implicit configuration is not a Paper 3 compliant FAI event; it is an ungoverned inter-Self information exchange — the named foil from D1.05.

---

## 1. Anti-Pattern Name and Category

**Anti-Pattern:** AP-6 — Implicit Configuration

**Category:** Category 4 — Configuration Failures (opening note)

**Position in series:** D3.13, note #588. Category 4 groups anti-patterns that arise when one or more of the six configurable FAI dimensions (D1.22) are absent, informal, or insufficiently authored as governance content. AP-6 is the foundational member of this category — the condition of zero authored configuration from which the other Category 4 failures are derived.

---

## 2. Description

A FAI event operates without an authored configuration substrate. The six FAI dimensions identified in D1.22 — sharing scope, cardinality, persistence policy, cooperation or competition variant, provenance carry-over depth, and conflict-routing rules — are not specified as authored governance content. They are either absent entirely or implicitly determined by whatever the shared substrate's host infrastructure does when no governance specification is present.

The shared substrate is constructed and the event operates. But there is no jointly-authorized governance specification of what the event is configured to do. Governance happens by assumption rather than by authored specification.

A critical distinction governs this anti-pattern: *infrastructure defaults* are not *governance defaults*. Infrastructure defaults are what the system does absent any governance specification — the host environment's fallback behavior, over which no governance authority has made any authored claim. Governance defaults, by contrast, are authored governance content that specifies how to behave absent event-specific instruction. Standing configurations (D2.21), for example, are governance defaults: they are authored, jointly authorized, and can be inspected, modified, and overridden by governance authority at any time. A standing configuration that is current and jointly authorized satisfies Paper 3 Claim 5's authored-configuration requirement in full. It is not implicit configuration.

AP-6 occurs when practitioners mistake infrastructure defaults for governance choices — treating the consistent behavior produced by infrastructure as though it reflected an authored governance decision. The consistency of infrastructure defaults can make this mistake easy to make and hard to detect. The behavior is repeatable, so it may appear to be governed. It is not.

AP-6 is foundational within Category 4 because the other major configuration anti-patterns are specific instances or downstream consequences of it. AP-12 (Informal Resolution Rules) is AP-6 applied specifically to the conflict-routing dimension — one dimension absent rather than all six. AP-1 (Ungoverned Construction) frequently co-occurs because an event constructed without governance is also almost certainly constructed without authored configuration; the two anti-patterns share a common cause. AP-11 (Unresponsive Escalation) can develop downstream because escalation paths are a configuration dimension, and absent authored configuration, escalations have nowhere governed to route. A reviewer who identifies AP-6 should treat it as a signal to inspect for all three co-occurring anti-patterns.

---

## 3. Detection Criteria

The following indicators, individually or in combination, identify AP-6:

- No FAI configuration substrate exists as authored substrate content in either participating Self's home substrate or the shared substrate.
- The sharing scope cannot be identified as authored governance content: which aspects were selected for contribution is unknown from any governance record.
- The persistence policy is absent: what Locus 2 content will be retained after dissolution is unspecified in any authored document.
- Conflict-routing rules are absent or informal. (Where conflict-routing rules specifically are the only missing dimension, AP-12 applies; where all dimensions are absent, AP-6 applies at the foundational level.)
- The FAI configuration references cannot be found in the construction record required by D2.01 Requirement 1.
- When asked to produce or reproduce the governance decisions that shaped how the event operates, no authored governance record can supply them.

The last criterion is the functional test: if the event's operating parameters cannot be traced to authored governance content, they are being supplied by infrastructure defaults, and AP-6 is present.

---

## 4. Governance Commitment Violated

**Primary — Paper 3 Claim 5 (configuration as substrate content, D1.22).** Claim 5 requires that all six configurable FAI dimensions be authored governance content, inspectable and modifiable under joint authority. Implicit configuration means zero of the six dimensions are governed in the Claim 5 sense. The commitment is violated in its entirety, not partially.

**Secondary — Paper 1 Claim 3 (human-governed authority — the three rights).** Paper 1 establishes that humans must retain the rights to inspect, modify, and override substrate content and orchestration rules at any time. These three rights cannot be meaningfully exercised over a shared substrate that has no authored governance specification. There is nothing for governance to inspect that represents a governance decision; nothing to modify that was authored under authority; nothing to override that was committed under joint authorization. The rights exist in principle but have no authored substrate content to operate on. The governance architecture is formally present but functionally empty.

**Tertiary — Paper 3 Claim 1 (shared substrate as architectural object).** A governed shared substrate requires authored configuration. A shared substrate operating under implicit configuration is not a Paper 3 compliant shared substrate — it is a transiently constructed information store whose operating parameters are set by infrastructure rather than governance.

**Operational reference — D2.12 (configuration authoring protocol).** The minimum required configuration content established by D2.12's five-phase configuration authoring protocol must exist. Implicit configuration means the protocol was not executed.

---

## 5. Consequences

**All governance is determined by infrastructure defaults.** Every aspect of the event's operation — what is shared, how conflicts are handled, what persists after dissolution, what flows to home evolution machinery — is determined by whatever the infrastructure does in the absence of governance specification. No governance decision was made; no governance decision was recorded; no governance decision is available for later inspection, reproduction, or dispute resolution.

**The determinism contract (D2.66) fails completely.** The determinism contract requires that governance decisions be reproducible from authored governance rules. With no authored governance rules, there are no rules from which to reproduce any governance decision. The event cannot be audited, its decisions cannot be explained, and its behavior cannot be predicted from any governance record.

**Process disputes (D2.45) are unresolvable.** When a participating Self later questions how the event operated — why certain content persisted, why a conflict was handled the way it was, what was jointly agreed — there are no authored governance records to consult. Dispute resolution requires authored records of what was jointly agreed; implicit configuration produces none.

**Co-occurring and downstream anti-patterns.** AP-1 (Ungoverned Construction) typically co-occurs: a FAI event without authored configuration was most likely constructed without governance review. AP-11 (Unresponsive Escalation) may develop downstream: with no authored escalation-path configuration, escalations arising during the event have no governed route to joint authority. AP-12 (Informal Resolution Rules) is a specific instance of the same failure at the conflict-routing dimension.

**The event does not qualify as a Paper 3 FAI event.** This is the most severe consequence. An event operating under implicit configuration is not a Paper 3 compliant FAI event. It is an ungoverned inter-Self information exchange — the named foil from D1.05. This is a categorical disqualification, not a matter of degree. The event may exchange information between Selves; it may produce useful outputs. But it does not satisfy the architectural requirements Paper 3 specifies for an FAI event, and the governance properties Paper 3 guarantees — inspectability, joint authority, reproducible decisions, governed persistence — do not hold. Governance authorities who believe they are operating a Paper 3 architecture when AP-6 is present are operating a foil they have mistaken for the architecture.

---

## 6. Intra-Self Analog

Paper 1's requirement for authored orchestration rules establishes the same commitment at intra-Self scope. Cells operating under implicit or system-default rules rather than authored governance specifications violate Paper 1's human-governed commitment in exactly the same way AP-6 violates Paper 3 Claim 5 at inter-Self scope.

The failure mode is structurally identical at both scopes: behavior is produced; behavior may even be consistent; but no authored governance record exists from which that behavior can be explained, reproduced, or overridden under authority. Consistency is not governance. The CKS architecture requires authored governance content at every level — implicit configuration at any scope, intra-Self or inter-Self, is the same failure.

The intra-Self analog also clarifies why the distinction between infrastructure defaults and governance defaults matters. Intra-Self, an orchestration rule specifying cell behavior absent event-specific instruction is authored governance content. An infrastructure runtime that fills in missing behavior because no orchestration rule was written is an infrastructure default. The distinction between the two is precisely the distinction between Paper 1 compliance and Paper 1 violation at intra-Self scope — and the same distinction governs AP-6 at inter-Self scope.

---

## 7. Resolution

**D2.12's five-phase configuration authoring protocol** is the complete prevention. The protocol specifies the minimum required configuration content, the authoring sequence, the joint-authorization requirements, and the construction-record entries that must be present for a FAI event to operate under authored governance rather than infrastructure defaults.

**D2.37's minimum required configuration content** — three critical dimensions as the floor — is the threshold below which no FAI event should proceed. A FAI event that cannot meet the three-dimension floor does not have sufficient authored governance to operate as a Paper 3 compliant event.

**Standing configurations (D2.21)** resolve AP-6 when they are current and jointly authorized. A standing configuration is authored governance content: it specifies the configurable dimensions for recurring FAI events between the same Selves under the same conditions, reduces the authoring burden at the event level, and satisfies Claim 5's authored-configuration requirement in full. Practitioners who operate recurring FAI events without per-event configuration authoring are not committing AP-6 if a current, jointly-authorized standing configuration governs those events. Standing configurations are governance defaults — the correct alternative to infrastructure defaults — and their existence is a complete answer to AP-6 for the events they cover.

The resolution strategy in order: first, determine whether a standing configuration exists and is current; if so, no further action is required for the events it covers. If no standing configuration exists, execute D2.12's five-phase protocol before the FAI event proceeds. If a FAI event has already operated under implicit configuration, the remediation path is retrospective documentation of whatever governance decisions can be reconstructed, followed by prospective configuration authoring before any subsequent event.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-6: Implicit Configuration.* Derivation Note #588, Series D Phase D3. May 15, 2026. ORCID: 0009-0004-8065-3235.
