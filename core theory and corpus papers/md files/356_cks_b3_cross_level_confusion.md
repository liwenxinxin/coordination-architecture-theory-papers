# Cross-Level Confusion — The Cross-Cutting Anti-Pattern Where Entities Simultaneously Perform Functions at Multiple Structural Levels Without Governed Level Determination, Violating B1.17 Relational Roles, B1.19 Cross-Level Access, and B1.20 Recursive Governance by Making Level-Appropriate Governance Scope Application Impossible

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Cross-Level Confusion is a cross-cutting anti-pattern in the Coordination Knowledge Substrate (CKS) architectural framework. It names the failure mode in which one or more entities simultaneously perform functions appropriate to multiple structural levels — cell, aspect, and Self — without governed level determination having been made, making it impossible to apply level-appropriate governance scope. This note formalizes the pattern using the B3.01 anti-pattern structure, identifies four recognizable sub-forms, traces three emergence conditions, articulates four operational consequences, specifies detection procedures, and provides remediation guidance. Cross-Level Confusion is cross-cutting because it simultaneously violates B1.17 (relational roles — level membership is determined by function, but function is ambiguous across levels), B1.19 (cross-level access — entities performing multi-level functions collapse the governed access architecture), B1.20 (recursive governance — which level's Paper 1 commitments apply is undetermined), and B2.85 (purpose-defined level determination — level cannot be determined when function spans levels). The note distinguishes Cross-Level Confusion from two related anti-patterns: B3.03 Flat Architecture, which removes level structure entirely, and B3.18 Intrinsic Type Assignment, which assigns a fixed wrong single type. Cross-Level Confusion is the pattern where level structure nominally exists but entities operate across multiple levels simultaneously without governance.

---

## 1. Pattern name and cross-cutting character

**Pattern name:** Cross-Level Confusion

**Cross-cutting character.** Cross-Level Confusion is not localized to a single structural level or a single architectural commitment. It is cross-cutting in two senses. First, it touches multiple commitments simultaneously: an entity that performs functions at all three structural levels without governed level determination violates relational role membership (B1.17), collapses the governed cross-level access architecture (B1.19), makes recursive governance scope application impossible (B1.20), and defeats the purpose-defined level determination procedure (B2.85). Second, the anti-pattern may manifest at any level of the CKS hierarchy — a confusion about cell-versus-aspect membership is structurally identical in its governance consequences to a confusion about aspect-versus-Self membership. The cross-cutting designation signals that detection and remediation efforts cannot be scoped to one layer of the architecture; the full relational structure must be audited.

**Distinction from B3.03 Flat Architecture.** Flat Architecture is the anti-pattern where level structure is removed entirely — the system treats all entities as undifferentiated, and there are no levels to be confused about. Cross-Level Confusion requires that level structure nominally exist in the architecture. The anti-pattern is not the absence of levels but the failure to assign entities to determinate levels within a level structure that the architecture commits to.

**Distinction from B3.18 Intrinsic Type Assignment.** Intrinsic Type Assignment assigns an entity a fixed, wrong structural type — the entity is placed in one level, but that level is incorrect relative to the entity's function. The misassignment is singular and stable. Cross-Level Confusion is the pattern where no single level can be assigned because the entity actively performs functions at multiple levels simultaneously or context-dependently. The problem is not a wrong single assignment but the absence of a single assignment that governance can operate against.

---

## 2. Commitments violated

Cross-Level Confusion violates four CKS architectural commitments:

**B1.17 — Relational roles.** Under B1.17, an entity's level membership is determined relationally: level is a function of what the entity does, which structural arrangement calls upon it, and for what purpose. The relational commitment presupposes that a level determination can be made — that one relational answer is returned when the level-determination procedure is applied. When an entity performs cell-level, aspect-level, and Self-level functions simultaneously, the relational determination procedure does not fail cleanly; it returns multiple answers. The relational commitment is violated because the entity's role is not a coherent element of any single structural arrangement.

**B1.19 — Cross-level access.** Under B1.19, access patterns between entities at different structural levels are governed: the architecture specifies when and how higher-level entities may access lower-level entities, and those access events are architecturally visible. Cross-Level Confusion defeats this architecture by eliminating the cross-level boundaries it governs. An entity that operates at all three levels simultaneously does not need governed cross-level access; it already occupies all levels. The cross-level access events the architecture was designed to govern either disappear or become indistinguishable from ordinary intra-entity operations.

**B1.20 — Recursive governance.** Under B1.20, Paper 1's six architectural commitments — human-governed, substrate-as-coordination-artifact, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, and linear-cost scaling — apply recursively at every level. Cells have Paper 1 commitments at cell scope; aspects have them at aspect scope; the Self has them at Self scope. The recursive application presupposes that each entity belongs to a determinate level so that the appropriate scope can be identified. When level is indeterminate, the recursive application cannot be made: governance cannot be scoped to the level at which it should operate because no level has been determined.

**B2.85 — Purpose-defined level determination.** B2.85 is the operational procedure by which entities are assigned to levels based on their purpose and function: a cell is determined by task-execution purpose, an aspect by purpose-defined coordination of peer cells, the Self by the integration of multiple aspects under unified governance. Cross-Level Confusion arises when this procedure, applied honestly to an entity's actual functions, cannot produce a single level determination — because the entity's functions span multiple levels.

---

## 3. Recognizable forms

Cross-Level Confusion presents in four recognizable sub-forms.

**Form 1 — The Chameleon Entity.** A single entity simultaneously performs functions that span all three structural levels. It executes specific informational tasks in the manner of a cell, coordinates peer entities for a purpose in the manner of an aspect, and governs integration architecture in the manner of a Self. No level determination has been made; the entity was constructed to handle whatever functions its architects needed without the structural question being posed.

The recognition signals for Form 1 are distinctive. The B2.85 purpose-defined level determination procedure, applied to the entity's actual functions, cannot produce a single level determination: the entity's purposes include task execution, purpose-defined coordination, and integration governance simultaneously. The B2.09 level-distinguishability tests, when applied to the entity, produce contradictory results: the entity partially passes the tests for multiple levels at the same time. Most concretely, governance cannot apply level-appropriate Paper 1 commitments because there is no single level to scope them to — applying cell-scope governance to Self-level functions is architecturally inappropriate, and applying Self-scope governance to cell-level functions is disproportionate.

**Form 2 — The Level-Switching Entity.** The entity performs cell-level functions in some operational contexts and aspect-level or Self-level functions in others, switching based on input type, caller, or operational mode, without governed level redetermination between contexts. The entity does not perform all levels simultaneously in every operation, but across the full range of its operations, it functions at multiple levels without the level transitions being governed.

The recognition signals for Form 2 differ from Form 1. The entity's DNA per B2.25 contains both task-execution behavior substrates — appropriate to cell-level function — and coordination rules — appropriate to aspect-level function — coexisting as a single entity's behavioral repertoire. The B2.85 level determination record specifies one level, but the entity's actual operational behavior instantiates multiple levels depending on context. The B2.87 evolution-triggered role change procedure is never performed even as the entity shifts between functional levels in operation: the level transitions happen silently through behavioral selection rather than through governed architectural change.

**Form 3 — The Governance-Scope Conflict Entity.** The entity has been granted governance affordances per A2.01–A2.04 at multiple levels simultaneously. The same entity can modify its own DNA (a cell-level governance act under A2.02), modify peer coordination rules (an aspect-level governance act under A2.02), and modify integration architecture (a Self-level governance act under A2.02). Governance authority that should be scoped to distinct entities at distinct levels has been aggregated into one entity.

The recognition signals for Form 3 appear in the authority records. The A2.47 authority distribution records show the same entity as authorized for governance acts at multiple structural levels — a configuration that the authority architecture should not permit because authority scope is how level-appropriate governance is enforced. The B2.107 recursive authority architecture reveals scope conflicts: the same entity's authority record contains entries scoped at multiple levels, producing contradictions in what governance can be applied to the entity itself.

**Form 4 — Cross-Level Access Collapse.** The entity's multi-level operation means it bypasses the governed cross-level access architecture per B1.19 entirely. Whereas Forms 1 through 3 are primarily problems of the entity's internal structure and governance status, Form 4 names the architectural consequence for the system as a whole: when one entity operates at all levels, it need not request cross-level access because it already possesses it natively. The cross-level access events that the B1.19 architecture was designed to make visible and governed are swallowed into the entity's internal operation.

The recognition signal for Form 4 appears at the B2.97 cross-level access verification audit. That audit finds the entity creating what amounts to implicit cross-level access through multi-level operation — access that is functionally cross-level in effect but that does not appear in the governed access record because it was never transacted through the governed access mechanism. The cross-level access architecture is nominally present in the system but operationally defeated for this entity.

---

## 4. Emergence conditions

**Monolith decomposition in progress.** Large monolithic systems being decomposed into CKS architecture pass through intermediate states in which single entities perform multi-level functions. The decomposition has separated the system into entities, but level assignment has not yet been completed. The result is entities that carry functions from multiple levels of the target architecture — not because anyone decided to violate level structure, but because the decomposition is not yet done. When a system is operated in this intermediate state rather than being driven to completion before production use, Cross-Level Confusion becomes the live architectural condition.

**Convenience consolidation.** Architects and developers consolidate related functions into one entity to avoid creating multiple entities. The motivating reasoning is economy: "it is simpler to have one entity that handles everything relevant to this domain than to define three entities at different levels." The convenience motivation is real — multiple entities require governance overhead, birth procedures, and explicit coordination — but it silently trades governance tractability for implementation simplicity. The result is an entity whose functional scope was determined by developer convenience rather than by level-appropriate function assignment.

**Governance architecture unfamiliarity.** Architects unfamiliar with CKS level distinctions create entities that perform whatever functions they need without the structural question being posed. The failure is not convenience consolidation — there is no decision to consolidate — but rather absence of awareness that the distinction between cell function, aspect function, and Self function is architecturally load-bearing. In this condition, Cross-Level Confusion is the default outcome: entities accumulate functions as the system is built, and level assignment is never performed because the need for it was never understood.

---

## 5. Operational consequences

**Governance scope is unknowable.** The first and most fundamental consequence is that when an entity operates across multiple levels, the question of which level's governance applies cannot be answered. Cell-scope governance applied to Self-level functions is architecturally inappropriate — the governance mechanisms are calibrated for task-execution scope, not integration-architecture scope. Self-scope governance applied to cell functions is disproportionate and imposes governance overhead calibrated for the whole integrated system on a single task-execution operation. There is no scope at which governance can be correctly applied, because the entity's function does not occupy a single scope.

**Paper 1 recursive commitments are inapplicable.** Under B2.99–B2.101, Paper 1's architectural commitments — human-governed, substrate-as-coordination-artifact, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, linear-cost scaling — apply at each level with scope appropriate to that level. These per-level applications are the mechanism through which the recursive governance commitment of B1.20 is discharged. When an entity's level is indeterminate, no per-level application can be made. Each of the six Paper 1 commitments has a different operational meaning at cell scope than at Self scope; when the entity occupies both scopes simultaneously, neither application is coherent. Compliance demonstrations are impossible because there is no determinate scope at which compliance could be evaluated.

**Cross-level access governance is bypassed.** The B1.19 governed cross-level access architecture exists to make inter-level access events visible, auditable, and subject to human governance. That architecture depends on level separation: access is cross-level only if the accessing entity and the accessed entity are at different levels. When a single entity operates at all levels, its access events are intra-entity by definition and fall outside the governed cross-level access architecture entirely. The level separation that the architecture's governance rests on is nominal rather than operational, and the governance that depended on it cannot be exercised.

**Evolution direction is indeterminate.** Bidirectional evolution per B1.16 distinguishes horizontal evolution — content change within existing level structure — from vertical evolution — structural reorganization in which the composition relationships between levels change. Both forms of evolution require that entities have determinate level membership: horizontal evolution applies to entities at the same level, and peer entities can be identified only if levels are known; vertical evolution acts on the composition relationships, and those relationships can be named only if their endpoints are level-determined. When an entity occupies multiple levels simultaneously, its peer entities cannot be identified with confidence, the direction of evolution applicable to it cannot be determined, and the structural reorganization that vertical evolution performs cannot be coherently targeted at it.

---

## 6. Detection

Three detection procedures apply to Cross-Level Confusion.

**B2.85 level determination.** Apply the purpose-defined level determination procedure to the entity's actual functions. Ask: does this entity execute specific informational tasks (cell-level function), coordinate peer entities for a purpose (aspect-level function), or govern integration architecture across multiple aspects (Self-level function)? If the procedure returns multiple answers — if the entity genuinely performs functions at more than one level — Cross-Level Confusion is present. The detection condition is not ambiguity in the determination but the return of multiple positive results rather than one.

**B2.09 level-distinguishability tests.** Apply the level-distinguishability tests to the entity. These tests are designed to determine, for any entity, which level it belongs to by examining the character of its functions, its operational scope, and its relationships to other entities. An entity that passes tests for a single level is correctly assigned. An entity that passes tests for multiple levels simultaneously — exhibiting cell-level properties in some tests, aspect-level properties in others, Self-level properties in yet others — is exhibiting Cross-Level Confusion.

**Function scope audit.** Examine the entity's DNA and behavioral repertoire directly. Ask whether the entity's DNA contains behavior substrates for task execution simultaneously with coordination rules simultaneously with integration architecture governance. If all three categories of behavior substrate are present in a single entity's DNA, Cross-Level Confusion is present regardless of what level label the entity has been assigned.

---

## 7. Remediation

**Decompose multi-level entities.** The primary remediation for Cross-Level Confusion is decomposition of the multi-level entity into level-appropriate entities through governed birth per B1.09. Each function class — task execution, purpose-defined coordination, integration architecture governance — is assigned to a newly born entity at the appropriate level. The decomposition is not a simple split; it requires running the B2.85 level determination procedure for each candidate entity to verify that the decomposition has produced entities with determinate, single-level function assignments.

**For level-switching entities (Form 2).** When the entity switches functional levels by context, first apply B2.85 to identify the dominant level — the level at which the entity performs the majority of its functions or the level at which its defining purpose is most clearly expressed. Assign the entity to that level. Then identify the minority-level functions — the functions the entity performs at other levels in other contexts — and separate them into new entities born at the appropriate minority levels. This is a dominant-level-first decomposition: anchor the entity at its primary level, then externalize the secondary-level functions.

**For monolith decomposition in progress.** The immediate remediation is to complete the decomposition rather than to operate on the intermediate state. Cross-Level Confusion arising from incomplete decomposition is a progress problem, not a design decision problem; the correction is to carry the decomposition work to completion. Once decomposition is complete, the B2.09 level-distinguishability tests should be run for all entities to confirm that the decomposition has succeeded in producing a level-determinate population.

**Post-remediation verification.** After any remediation, run B2.09 level-distinguishability tests for all entities produced by the decomposition. The tests should return single-level results for each entity. Any entity for which multiple tests still pass simultaneously has not been fully remediated and requires further decomposition or function reassignment. The level-determinate population required for B1.17, B1.19, and B1.20 to operate correctly cannot be assumed; it must be verified through the level-distinguishability tests.

---

## 8. Summary

Cross-Level Confusion is the cross-cutting anti-pattern in which entities simultaneously perform functions appropriate to multiple structural levels without governed level determination. It is cross-cutting because it cannot be scoped to a single commitment or a single level: it defeats relational role membership (B1.17), collapses the governed cross-level access architecture (B1.19), makes recursive governance scope application impossible (B1.20), and defeats the purpose-defined level determination procedure (B2.85). It differs from Flat Architecture (B3.03) because level structure nominally exists, and from Intrinsic Type Assignment (B3.18) because the problem is not a wrong-but-single type assignment but the absence of any single type assignment. It presents in four forms: the Chameleon Entity, the Level-Switching Entity, the Governance-Scope Conflict Entity, and the Cross-Level Access Collapse. It emerges from monolith decomposition in progress, convenience consolidation, and governance architecture unfamiliarity. Its operational consequences — governance scope unknowable, Paper 1 recursive commitments inapplicable, cross-level access governance bypassed, and evolution direction indeterminate — all trace to the same root cause: the level structure the CKS governance architecture requires cannot operate against entities whose level membership is undetermined. Remediation is decomposition into level-appropriate entities through governed birth, with B2.09 level-distinguishability tests applied post-remediation to verify that the level-determinate population has been achieved.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cross-Level Confusion — The Cross-Cutting Anti-Pattern Where Entities Simultaneously Perform Functions at Multiple Structural Levels Without Governed Level Determination, Violating B1.17 Relational Roles, B1.19 Cross-Level Access, and B1.20 Recursive Governance by Making Level-Appropriate Governance Scope Application Impossible.* May 12, 2026. ORCID: 0009-0004-8065-3235.
