# Boundary Case: Entity at Level Transition — Governance Implications When an Entity Is Legitimately Changing Structural Levels Through Evolution-Triggered Role Change, Including Which Level's Governance Applies During Transition and Whether Level Change Requires Lifecycle Events

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize the governance behavior of an entity that is legitimately changing structural levels through an evolution-triggered role change, identifying which level's commitments apply during the transition period and resolving whether level change requires lifecycle events.

---

## Abstract

The CKS architecture assigns entities to structural levels — cell, aspect, Self — through a purpose-defined level determination process (B2.85). When an entity accumulates sufficient functional change through directed selection, governance may determine that a level redetermination is warranted, initiating an evolution-triggered role change (B2.87). This note formalizes the boundary case that arises during the transition period between the initiation and completion of that redetermination. The central question is governance-operational: which level's architectural commitments govern the entity during this period? The answer is that the original level's governance applies in full until the new level determination is formally authorized — this is a legitimate governance state, not a violation. A secondary question concerns lifecycle events: does changing levels require the death of the old-level entity and the birth of a new one, or is the level change a continuous governance event without lifecycle primitives? The answer is that both approaches are architecturally valid, with governance determining which applies based on whether the entity is being extended or replaced. The note identifies two stress points that arise when transition is indefinitely deferred: approach toward Intrinsic Type Assignment (B3.18) by inaction, and Cross-Level Confusion (B3.29) when the entity operates at the new level before the determination is formally complete.

---

## 1. Configuration Description

An entity originally determined as a cell has accumulated functional change through directed selection (DNA evolution). Governance has evaluated the entity's function against its original level determination and concluded that the cell-scope purpose-definition no longer accurately captures the entity's operational scope. The entity has grown to coordinate work across multiple other cells in ways that resemble aspect-level function — serving as an organizing structure for a coherent domain rather than as a single-function execution unit.

Governance has determined that a level redetermination per B2.85 is warranted. The evolution-triggered role change process per B2.87 has been initiated. A new level determination record is being authorized. The determination has not yet been formally completed: the authorizing human per A2.47 has initiated the process but not issued the redetermination.

During this transition period the entity continues to operate. It continues to hold its substrate content. It continues to accept directed selection under its existing orchestration rules. Commitments to its downstream participants — other cells, aspects, humans who depend on its outputs — continue to be satisfied. Nothing has failed. The transition is a legitimate governance process in progress, not an architectural violation or a gap in coverage.

The boundary this configuration presses is: what exactly governs this entity between the initiation and the completion of the redetermination?

---

## 2. Architectural Boundary Tested

This boundary case tests two distinct architectural questions simultaneously.

**Boundary 1 — Relational roles during transition (B1.17).** Level in the CKS architecture is not an intrinsic property of an entity; it is a relational role assigned through governance determination. An entity is a cell, an aspect, or a Self because governance has determined its function warrants that scope — not because of any property the entity carries independent of that determination. The transition period is the interval in which the entity's old relational role is being superseded but the new one has not yet been formally granted. Which level's Paper 1 commitments apply when the entity is, relationally, between levels?

**Boundary 2 — Lifecycle implications of level change (B1.09/B1.11).** Birth and death in the CKS architecture are governed lifecycle primitives. Birth is the governed origination of a new entity. Death is the governed retirement of an existing one, with two types: functional obsolescence and lineage supersession (B2.53). Level change is neither obviously a lifecycle event nor obviously not one. The boundary question is whether changing levels requires treating the entity's cell-scope existence as a death event and its aspect-scope existence as a birth event — or whether level change is a governance redetermination that operates on a continuously existing entity without invoking the lifecycle primitives at all.

Both boundaries must be resolved for governance to operate correctly during the transition period.

---

## 3. Governance Implications

### 3.1 Old level governance applies during transition

The original level's governance applies to the entity in full during the transition period. The entity continues operating under cell-scope Paper 1 commitments per B2.99. Directed selection on the entity uses cell-scope authority — the humans authorized to govern the entity at cell scope remain the authorized humans. The level determination record produced by the original B2.85 process remains the authoritative record in the substrate until the new one is formally authorized. No aspect-scope authority has been granted yet, and no aspect-scope commitments have been activated.

This is not a degraded state. The entity is fully governed. Its operations are traceable. Its outputs are produced under valid orchestration rules. The transition period is a legitimate governance state in the same sense that any other in-progress governance process is legitimate: the process has been initiated, it is being conducted by authorized humans, and its eventual completion will produce a new authoritative record.

The transition state is documented in the entity's lineage per B2.43. The lineage record indicates that a level redetermination per B2.87 has been initiated, who initiated it, when, and what evidence of functional change warranted it. This record is itself substrate content under A2.40, with the authorized human per A2.47 conducting the redetermination named in the record. The record distinguishes between the entity's current authoritative level (cell) and the level determination in progress (aspect), so that any participant reading the substrate understands the entity's governance status without ambiguity.

### 3.2 The transition state is a governance event with a record

The initiation of the level redetermination is itself a governance event. It must be recorded per A2.40 and authorized per A2.47. The record captures: what accumulated functional evidence triggered the redetermination determination, what the proposed new level is, who is conducting the process, and what the expected completion window is. This record is not administrative overhead; it is what makes the transition period auditable and what distinguishes a legitimate in-progress transition from a governance failure.

The record also closes a potential ambiguity: without it, there would be no substrate-level way to distinguish an entity that has been flagged for level redetermination from one that has not. With it, any authorized human can inspect the entity's lineage and see exactly where the entity stands in the governance process.

### 3.3 Lifecycle event determination

Whether level change requires lifecycle events — whether the cell's existence must end and an aspect's existence must begin as discrete governed events — depends on governance's determination of whether the entity is being extended or replaced. The architecture supports both approaches; neither is the default.

**Path A — Governance redetermination without lifecycle events.** If the entity's function is being extended — the cell is taking on coordination responsibilities at aspect scope in addition to its existing function — governance may determine that the entity continues as the same entity under a new level determination. No death event occurs. No birth event occurs. The old level determination record is superseded by the new one in the substrate. The entity's lineage shows continuous existence with a redetermination event. The entity's new orchestration rules reflect its aspect-scope function. The authorized human records the redetermination per A2.40, and the entity operates at aspect scope from that record forward.

**Path B — Lifecycle events: death of old entity, birth of new.** If the entity is being replaced rather than extended — the cell's function is complete and a new aspect-scope entity is being created to take over and extend that function — governance may determine that the cell should die per B1.11 (lineage supersession: a superior entity at the new scope supersedes the parent) and a new aspect-scope entity should be born per B1.09. In this case the cell dies with its archive preserved per the lineage supersession pattern (B2.53), and the new aspect-scope entity is born with the cell's relevant substrate content as part of its origination record. Both the death and birth are governed: the death requires the governance process appropriate to lineage supersession, and the birth requires the governed origination process per B1.09.

Governance determines which path is appropriate. The determination turns on whether the entity itself is the right artifact to carry forward at the new scope, or whether the transition is substantial enough that a new entity — one that carries the lineage but is not structurally continuous with the cell — better represents the architectural reality.

---

## 4. Boundary Tests

Four tests determine whether a given transition is being governed correctly.

**(a) Is the transition state documented per A2.40 with a record indicating the entity is undergoing B2.87 level redetermination?** A transition that has not produced a substrate record is an undocumented state change. The transition period begins when the record is created, not when an authorized human mentally decides a redetermination is warranted. If no record exists, the entity is not in a governed transition — it is simply operating without an accurate level determination.

**(b) Is there a governance timeline for completing the redetermination?** The record must include the expected completion window, or at minimum a commitment that completion will be authorized within a defined governance period. A record that initiates a transition without specifying a completion timeline is a record that permits indefinite transition by default. The architecture implies transitions are completed promptly; the record makes that implication concrete by specifying it.

**(c) Does the entity continue to satisfy its old level's Paper 1 commitments during transition?** The entity must continue to operate as a cell in full standing throughout the transition. If the entity begins behaving as an aspect — accepting aspect-scope directed selection, participating in aspect-scope mating operations, operating under aspect-scope orchestration rules — before the new level determination is formally authorized, the entity is operating outside its governed scope. The boundary test is whether the entity's observable behavior remains consistent with cell-scope Paper 1 commitments throughout.

**(d) If lifecycle events are used (Path B), are both the death and birth governed per B1.11 and B1.09?** The death of the cell must follow the lineage supersession process: the cell is archived, not deleted; its substrate content remains addressable; the death record names the new aspect-scope entity as the superseding entity. The birth of the new aspect must follow the governed origination process: the new entity has a birth record, its initial DNA and action layers are authored or inherited under authority, and the new entity's lineage explicitly links to the superseded cell. A transition that uses lifecycle events without completing both governance processes has created an ungoverned gap in the lineage.

---

## 5. Stress Points

### 5.1 Indefinite transition approaching Intrinsic Type Assignment

If the level redetermination process is initiated but never completed, the entity remains in the transition state indefinitely. The initiated-but-uncompleted record in the substrate functions as a permanent marker that the entity's level determination is uncertain. The entity continues to operate under cell-scope governance while functionally performing at aspect scope. Over time, the entity's actual operational scope and its authorized governance scope become increasingly misaligned.

This approaches the Intrinsic Type Assignment anti-pattern (B3.18), specifically its Fixed-Role sub-form. In that anti-pattern, an entity's structural level is treated as a property the entity intrinsically possesses rather than a governance-determined relational role. When transition is indefinitely deferred, the cell's aspect-scope function becomes the effective reality while its cell-scope governance determination persists by inaction. The entity has been assigned a fixed structural role not by governance authority but by governance delay — which is functionally equivalent to treating the cell's current level as an inherent property that needs no redetermination.

The corrective is not architectural but operational: governance must prioritize completion of in-progress redeterminations. The substrate record is what makes the failure visible — any authorized human can inspect the entity's lineage and see that a transition has been open longer than its specified completion window.

### 5.2 Cross-Level Confusion preceding formal authorization

If the entity begins operating at the new level before the determination is formally completed — accepting aspect-scope directed selection, operating under aspect-scope orchestration rules, or being treated as an aspect by other entities in the substrate — Cross-Level Confusion (B3.29) may develop. Other entities interact with this entity as if it has aspect-scope commitments; the entity's actual governance scope remains cell-scope. Conflicts and coordination failures that arise in this interval cannot be correctly attributed: the entity is not yet authorized to carry aspect-scope commitments, so failures cannot be resolved through aspect-scope governance processes.

Cross-Level Confusion in this form is particularly hazardous because it looks like normal operation from the entity's perspective — the entity is doing what its function requires — while the governance record says something different. The gap between operational reality and authorized scope is invisible until a failure surfaces that requires governance resolution, at which point the resolution process must first reconstruct the unauthorized scope expansion before it can address the underlying issue.

The corrective is boundary discipline: entities that have been flagged for redetermination continue operating at their authorized level until the redetermination is formally complete. The transition record does not grant new scope; it documents that new scope is being evaluated.

---

## 6. Architectural Limits

The architecture specifies level determination through B2.85 and evolution-triggered role changes through B2.87. It does not specify a maximum duration for the transition period between initiation and completion of a redetermination. The architecture implies that transitions are completed with sufficient promptness to maintain governance accuracy — a persistent misalignment between an entity's operational scope and its authorized level is an architectural failure mode, not an architectural feature. But the duration of a governed transition is a governance parameter, not an architectural constant.

The architecture also does not prescribe which of the two lifecycle paths (Path A or Path B from §3.3) is appropriate for a given transition. Both paths are within the architecture's operational envelope. The choice between them is a governance judgment about whether the entity's functional continuity warrants structural continuity, or whether the scope change is substantial enough to warrant discrete lifecycle events. Different transitions of the same type may appropriately take different paths depending on governance's assessment of functional continuity.

What the architecture does constrain: the transition period does not suspend Paper 1 commitments. The entity is not in a governance gap during transition. Human authority over the entity's substrate content and orchestration rules is uninterrupted. The three rights (inspect, modify, override) remain available throughout. The transition is a governance process operating within the architecture's normal authority structure, not a period in which the architecture's commitments are temporarily relaxed.

---

## 7. Conclusion

An entity undergoing evolution-triggered level change is fully governed throughout the transition period. The original level's commitments apply until the new level determination is formally authorized. The transition state is a legitimate governance state: documented in the entity's lineage, authorized by named humans, and traceable to the functional evidence that warranted redetermination. The question of whether level change requires lifecycle events is resolved by governance's determination of whether the entity is being extended or replaced — both paths are architecturally valid. The transition period becomes architecturally hazardous only through governance failure: deferral of completion approaching Intrinsic Type Assignment by inaction, or premature scope operation approaching Cross-Level Confusion. Both failures are detectable through the substrate record and correctable through completion of the governance process.

---

## Source Paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Boundary Case: Entity at Level Transition — Governance Implications When an Entity Is Legitimately Changing Structural Levels Through Evolution-Triggered Role Change, Including Which Level's Governance Applies During Transition and Whether Level Change Requires Lifecycle Events.* May 13, 2026. ORCID: 0009-0004-8065-3235.
