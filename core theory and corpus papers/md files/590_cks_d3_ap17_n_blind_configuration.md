# AP-17: N-Blind Configuration

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

N-Blind Configuration is a Category 4 (Configuration Failure) anti-pattern in which a Full Aspect Integration (FAI) event with N>2 participating Selves is operated under a configuration authored for N=2 participation. The configuration does not reflect the governance authority, contribution scope, or escalation routing of the third or Nth participating Self. That Self is present in the event — contributing aspects to the shared substrate, generating conflicts, occupying governance territory — but is absent from the governance record that is supposed to cover it. This is a governance rights violation: the architecture commits every participating Self to governance rights over the shared substrate, and N-blind configuration breaks that commitment for the Nth Self. This note formalizes the anti-pattern across all seven elements of the Phase D3 structure: name and category, description, detection criteria, governance commitment violated, consequences, intra-Self analog, and resolution.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-17 — N-Blind Configuration

**Category:** Taxonomy Category 4 — Configuration Failures

Configuration Failures are anti-patterns in which the configuration of a FAI event — which Paper 3 Claim 5 establishes as substrate content that must be authored under joint human authority — is authored incorrectly, incompletely, or not at all. AP-17 is the third of five Category 4 anti-patterns. It is distinguished from other Category 4 failures by its cardinality-specific character: the configuration is not missing entirely and is not internally self-contradictory; it was authored correctly for an event of a different size and then applied, without amendment, to an event for which it is wrong.

---

## 2. Description

A FAI event with N>2 participating Selves uses a configuration authored for N=2 participation without being updated to account for the additional participants. The joint authorization mechanics, contribution scope, and conflict-handling routing were designed for two-Self exchange. When a third — or more — Self joins, the configuration does not reflect their governance authority, contribution scope, or escalation routing. One or more participating Selves are effectively outside the governance framework of the FAI event.

The architecture of FAI is n-ary in cardinality: two-Self exchange is the simplest instance, not the canonical one. Paper 3 Claim 2 explicitly specifies cardinality as a governed configuration dimension (the sharing scope, cardinality floor, and persistence policy are among the six FAI-event-level configurable dimensions). Paper 3 Claim 5 then establishes that all such configurable dimensions are themselves substrate content authored under joint human authority. Cardinality is not an implementation detail to be inferred at runtime — it is an explicitly authored governance dimension that determines whose authority is recognized, whose contributions are scoped, and whose escalation paths are assigned.

N-blind configuration violates this architecture at the simplest possible level: the cardinality value in the configuration is wrong. But because cardinality is a load-bearing governance dimension, a wrong cardinality value has cascading governance consequences that touch every other dimension of the event's configuration.

**Two onset paths.** N-blind configuration most commonly arises retrospectively: the event was originally designed for two Selves, a third Self is added during or before construction, and no configuration amendment is triggered. The third Self's participation is recorded at the event level, but the configuration was never updated to govern it. This is the amendment-failure path. It is the more common path because adding a Self to an existing event is an operational action that may not automatically surface the need for a configuration update.

N-blind configuration can also arise at inception: governance authors the configuration before construction begins but does not account for all N Selves planned to participate. A configuration authored for two Selves in a three-Self event, before any Self has joined, is N-blind from the start. This is the inception-failure path. It is less common — the error is made before the event exists — but it produces the same downstream consequences and requires the same resolution.

Both paths leave the Nth Self ungoverned by the configuration. The amendment path (D2.38) resolves the retrospective case. For the inception case, governance discipline before construction is the prevention.

---

## 3. Detection Criteria

N-blind configuration is detectable from the governance record without access to the event's operational data. Four criteria, each individually sufficient, collectively constitute a reliable detection pattern:

**Criterion 1 — Participation count exceeds configuration count.** The FAI event has N>2 participating Selves but the configuration references only two governance authorities for joint authorization. Participation records show three (or more) Selves; the configuration governs two. This inconsistency between event participation and governance configuration is the clearest and most direct detection signal for N-blind configuration. When the participation count and the governance count diverge, the diagnosis is N-blind configuration until demonstrated otherwise.

**Criterion 2 — Contribution records span more Selves than the sharing scope configuration covers.** Contribution records exist for aspects from all N Selves, but the sharing scope configuration only specifies scope for two Selves. Aspects contributed by the Nth Self are present in the shared substrate without a sharing scope assignment in the configuration. The contributions are real — they occupy the substrate — but the governance account of their scope is absent.

**Criterion 3 — Conflict routing gaps corresponding to the Nth Self's contributions.** Conflict registry entries from the Nth Self's contributed aspects lack routing assignments because the routing rules were authored before that Self's participation was known. Conflicts that should route to the Nth Self's governance authority have no routing target in the configuration. The conflict-handling tier system operates over two Selves only; conflicts involving the Nth Self's contributions are effectively routing to a configuration that doesn't know they exist.

**Criterion 4 — Escalation routing incomplete for the Nth Self.** The escalation routing specifies governance authorities for two Selves only; escalations involving the Nth Self's contributions have no routing target. This is the highest-tier failure: when conflicts survive the preserve and resolve tiers and reach the escalate tier, they must route to human governance authorities across the joint authority. If the Nth Self's governance authority is not in the escalation routing, those escalations have no destination.

---

## 4. Governance Commitment Violated

**Primary violation — Paper 3 Claim 5, Dimension 2 (cardinality).**

Paper 3 Claim 5 establishes that all configurable dimensions of a FAI event are substrate content authored under joint human authority. Cardinality — the number of participating Selves — is the second of the six FAI-event-level configuration dimensions §5 of Paper 3 enumerates. The commitment is that cardinality must be explicitly authored as substrate content, not assumed or inherited from a prior configuration.

Using a two-Self configuration for a three-Self event means the cardinality configuration is factually wrong. The error is not that cardinality was left unspecified — it is specified, but incorrectly. A configuration that specifies N=2 for an event with N=3 participation is an instance of Claim 5's configuration-as-substrate-content commitment being violated: the authored substrate content does not accurately represent the governed event. Every downstream configuration dimension — sharing scope, escalation routing, joint authorization — inherits the wrong cardinality as its basis.

**Secondary violation — Paper 1 Claim 3 (human-governed authority).**

Paper 1 Claim 3 commits the architecture to human governance over the substrate and its orchestration rules. The CKS architecture's governance commitment applies to every participating Self in a FAI event: every Self's governance practitioners hold governance rights over the shared substrate during the event. These rights are architectural — they exist by virtue of participation, not by virtue of being named in a particular configuration field.

N-blind configuration creates a situation in which the Nth Self's governance authority is not named in the joint authority specification. The Nth Self's governance practitioners may not know they hold governance rights over the shared substrate. The architecture commits those rights to them; the configuration does not surface them. This is a governance rights violation: the rights exist at the architectural level but are inaccessible at the operational level because the configuration fails to recognize them.

**Operational reference — D2.22 (multi-Self FAI governance).**

D2.22 identifies N-blind configuration as a named failure mode for multi-Self FAI governance and specifies that cardinality must be explicit for all N participants. D2.12 (configuration authoring) provides the authoring discipline that prevents both onset paths. D2.38 (configuration amendment) provides the mechanism for the retrospective case.

---

## 5. Consequences

**The Nth Self's governance authority is not operational.** The Nth Self's governance practitioners may not know they hold governance rights over the shared substrate. Even if they know in principle that the architecture commits these rights to them, there is no path in the configuration through which they can exercise those rights operationally: they are not named in the joint authorization specification, so the configuration does not route governance actions through them. The rights exist architecturally; they are inaccessible practically. This is not a minor operational gap — it means the Nth Self is participating in a FAI event without functioning governance, which is the condition the architecture is specifically designed to prevent.

**Aspects contributed by the Nth Self lack governance attribution in the configuration.** Contribution records exist for aspects the Nth Self contributed to the shared substrate — those contributions are real and recorded. But the sharing scope configuration does not reference that Self's contribution scope. The aspects occupy the substrate without a governed sharing scope. This creates a condition in which the content of the shared substrate is not fully accounted for in the configuration that is supposed to govern it. From the perspective of the configuration, those aspects exist without a governance account of their scope.

**Conflicts involving the Nth Self's contributions may have no routing assignment.** The conflict registry may contain entries from aspects the Nth Self contributed, but the routing rules were authored for a two-Self event. Those conflict entries either default to a routing tier not designed for them or escalate without a proper routing destination. The three-tier conflict-handling mechanism — preserve, resolve, escalate — requires routing rules that account for all participating Selves. When routing rules are blind to the Nth Self, conflicts from that Self's contributions fall outside the governed routing structure.

**The event's governance record is internally inconsistent.** Participation records show N Selves; configuration shows N-1 Selves. This inconsistency between the event-level participation record and the configuration is itself a governance artifact: the shared substrate carries an accurate participation record and an inaccurate governance configuration simultaneously. The substrate is internally inconsistent in a way that is visible from the governance record alone. This inconsistency is the clearest detection signal but is also itself a consequence — a governance record that cannot be internally reconciled is not a reliable basis for the event's operations or for the evolution-feed that follows.

---

## 6. Intra-Self Analog

The N-blind configuration anti-pattern at inter-Self scope has a direct analog in Paper 2's intra-Self governance.

Paper 2 establishes that each Self is composed of aspects, and that the Self's governance configuration — the per-mechanism governance shapes co-determined with mechanism shape — must account for the full aspect population of the Self. A governance configuration authored when the Self had fewer aspects, and not updated when new aspects were added, is blind to the new aspects: their governance shapes are not specified, their contribution to the Self's evolution mechanisms is ungoverned, and the governance record of the Self is internally inconsistent in the same way.

The structure of the failure is identical at both scopes:

- At intra-Self scope: the governance configuration accounts for M aspects, but the Self has M+k aspects. The k new aspects participate in the Self's mechanisms without governance specification.
- At inter-Self scope: the governance configuration accounts for N-1 Selves, but the FAI event has N Selves. The Nth Self participates in the event without governance specification.

In both cases, the configuration's cardinality is wrong. In both cases, the wrong cardinality propagates through every downstream configuration dimension. In both cases, the consequence is that a participating entity — an aspect or a Self — is inside the event or Self's operations but outside the governance framework that is supposed to cover it.

The resolution path is also parallel. At intra-Self scope, the governance configuration must be updated to account for the new aspect population before the new aspects participate in governed mechanisms. At inter-Self scope, a configuration amendment is required before the new Self's contributions can be governed. The amendment is not retroactive — contributions made before the amendment are not retroactively governed — but the amendment prevents further ungoverned participation from the point of authoring forward.

The intra-Self analog is important for establishing that N-blind configuration is not a pathology unique to multi-Self events. It is a general failure mode of governance-by-cardinality: any architecture that requires explicit cardinality specification as a governance dimension is susceptible to this failure when cardinality changes without triggering a corresponding configuration update.

---

## 7. Resolution

The prevention and resolution of N-blind configuration are specified across three operational references: D2.22 (multi-Self FAI governance), D2.12 (configuration authoring), and D2.38 (configuration amendment).

**Prevention at inception.** For each FAI event, the cardinality must be authored explicitly as substrate content before construction begins. The configuration must name all N participating Selves and must include, for each:

- *Joint authorization:* all N governance authorities named in the joint authorization specification. Every Self's governance practitioners must be able to exercise their governance rights over the shared substrate from the moment the event begins.
- *Sharing scope:* one contribution scope specification per participating Self. The sharing scope cannot be authored for a subset of participants and left silent for others; each Self's sharing scope is a distinct governance dimension requiring explicit authoring.
- *Escalation routing:* one routing entry per participating Self in the escalation routing specification. When conflicts escalate to the human governance tier, every Self's governance authority must have a routing destination.

**Resolution in the retrospective case (D2.38 — configuration amendment).** When a Self is added to an existing event, a configuration amendment is required before the new Self's contributions can be governed. The amendment must add the new Self's governance authority to the joint authorization specification, add the new Self's sharing scope to the sharing scope configuration, and add the new Self's governance authority to the escalation routing. The amendment must be authored as substrate content under the joint authority of the Selves already participating in the event plus the new Self, to ensure that the amendment itself is a governed governance action.

Contributions made by the Nth Self before the amendment are not retroactively governed by the amendment. The amendment governs forward participation only. If ungoverned contributions already exist in the shared substrate — aspects contributed by the Nth Self before the configuration amendment — those contributions require separate governance remediation: either retrospective scope assignment under the amendment, or removal from the shared substrate with explicit governance decision. The amendment alone does not resolve the governance gap for content that already exists under N-blind conditions.

**Detection as a governance practice.** Because N-blind configuration is detectable from the governance record — the inconsistency between participation count and configuration count is visible without access to operational data — periodic governance audits that compare participation records to configuration cardinality are sufficient to detect N-blind configuration before its consequences become severe. The detection criteria in §3 can be operationalized as a governance checklist applied at event construction, at each configuration amendment, and at any point where a new Self joins an event. The checklist is: count the Selves in the participation record; count the Selves in the configuration's joint authorization specification; if the counts differ, N-blind configuration is present.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-17: N-Blind Configuration.* May 15, 2026. ORCID: 0009-0004-8065-3235.
