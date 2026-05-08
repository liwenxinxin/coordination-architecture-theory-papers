# Aspect as Coordination Arrangement of Cells for Purpose: A Foundational Commitment Establishing the Middle Structural Level of the CKS Self

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one of the foundational architectural commitments Paper 2 develops — the **aspect** as the middle structural level of the three-level structure (cell, aspect, Self) — as a standalone commitment with independent operational content.

## Abstract

Paper 2 of the CKS theory series introduces three architectural levels — cell, aspect, Self — as the structure within which the instinct/reasoning separation operates. Separate Phase B1 notes formalize the three-level structure as joint commitment, the cell as the atomic unit inheriting Paper 1's commitments without modification, and the Self as the integrated whole holding multiple aspects. This note formalizes the level between them. An aspect is a coordination arrangement of cells serving a particular purpose. Multiple aspects coexist within one Self, each organized around its own purpose. Cells participate in multiple aspects simultaneously through relational role-assignment rather than intrinsic membership. The aspect operates over its constituent cells as content domain — asking pattern questions across the cells for the aspect's purpose — rather than commanding them as subordinates. The note states the commitment, names what makes the aspect-level architecturally distinctive, identifies the inherited Paper 1 commitments at aspect scope, names operational implications and limits, and supplies an operational test.

## 1. Why the aspect needs to be formalized as standalone foundational commitment

Paper 2 introduces three architectural levels — cell, aspect, Self — as the structure within which the instinct/reasoning separation operates. Two prior Phase B1 notes formalize the three-level structure as joint commitment and the cell as the atomic unit inheriting Paper 1's commitments without modification; a subsequent note formalizes the Self as the integrated whole holding multiple aspects. This note pins down the level between them.

The aspect carries operational content distinct from either neighbor. It is not the atomic unit handling a specific informational task — that is the cell's role. It is not the integrated whole holding multiple coexisting structural perspectives — that is the Self's role. The aspect is the level at which cells are coordinated for purpose. Without formalizing the aspect as standalone, Paper 2's three-level structure collapses to two, and the structural arguments in the rest of Paper 2 that depend on the middle level lose their architectural anchor.

## 2. The architectural commitment, precisely stated

In the CKS pattern as Paper 2 develops it, an **aspect** is a coordination arrangement of cells serving a particular purpose. Six properties carry the commitment.

**(a) Purpose-defined.** The aspect's purpose defines what the arrangement is for — which cells participate, how they are coordinated, what cross-cell pattern the arrangement is organized around. The purpose is what makes the arrangement an arrangement, and is recorded as substrate content humans can inspect, modify, and override.

**(b) Coordination of cells.** The aspect coordinates cells. Cells are not subsumed; they retain their cell-level commitments — Paper 1 commitments, orchestration rules, atomic-unit status — while participating in the aspect-level coordination. The aspect's work is over the cells, not the cells' work performed at aspect scope.

**(c) Multiple aspects coexisting within one Self.** A Self holds multiple aspects simultaneously, each organized around its own purpose. The aspects coexist as facets of one Self; they are not stages a Self moves through sequentially or alternative configurations a Self switches between.

**(d) Cells shared across aspects through relational role-assignment.** The same underlying cell can participate in multiple aspect arrangements simultaneously. A cell is not "owned" by one aspect; it participates through relational role-assignment per the three-level-structure commitment. Cell-aspect membership is a relational property, governed and recordable as substrate content, rather than an intrinsic property of the cell. A subsequent Phase B1 note will formalize relational-and-purpose-defined membership as standalone; this note names it as a property the aspect commitment carries.

**(e) Pattern questions across constituent cells.** The aspect operates over its cells for its purpose by asking pattern questions across them — what the cells collectively reveal, what coordination follows from their joint state, what cross-cell arrangement the purpose calls for. The aspect's substantive work is the cross-cell pattern; the cells supply the content the pattern operates over.

**(f) Cells as content domain.** The aspect's relationship to its cells is content-domain: the cells are the substantive material the aspect coordinates over, not the subordinates the aspect commands. A subsequent Phase B1 note will formalize the higher-as-content-domain relationship as standalone; this note names it as a property the aspect commitment carries.

The sports-vs-study analogy maps directly. A person in competitive sports mode and the same person in calm study mode are exercising distinct purpose-defined coordinations of the same underlying capacities — the same body, attention, and memory. The two modes coexist as facets of one person; the underlying capacities (cells in the analog) participate in both arrangements through relational role-assignment. The architectural substance is purpose-defined coordination of cells; the analogy is conceptual scaffold.

## 3. What makes the aspect level architecturally distinctive

Three properties distinguish the aspect from the alternatives a designer might reach for first.

**Filling the middle-level gap.** Conventional AI architectures — agent frameworks, multi-agent orchestration platforms, microservice meshes, workflow engines — typically lack a middle level between individual processing units and the overall system. What sits in the middle is typically a controller, a router, an orchestrator, or a coordination service whose role is to direct subordinate units. CKS aspects fill the gap with purpose-defined coordination arrangements where cells participate as coordinated parts rather than as subordinates being directed.

**Relational role-assignment of cells across aspects.** Biological cells are fixed in their tissue and organ memberships; the same property holds in most modular software, where a service belongs to one bounded context, an aggregate to one service, a component to one composite. CKS commits to the inverse — the same cell can participate in multiple aspects simultaneously, with role-instances inhering in the cell per the aspect arrangement that calls on it. This is the relational-and-purpose-defined property, named here and formalized as standalone in a subsequent Phase B1 note.

**Content-domain relationship vs. rigid orchestration.** An orchestrator commands subordinates; a router dispatches requests; a coordinator schedules tasks. None of these names what an aspect does. The aspect operates over its cells as content domain — asking pattern questions across them, observing what cross-cell coordination the purpose calls for, producing aspect-scope output that depends on but does not replace cell-scope output. This is the higher-as-content-domain property, named here and formalized as standalone in a subsequent Phase B1 note.

## 4. The cognitive analog as conceptual scaffold

Aspects parallel "modes of engagement" — the same person operating in distinct purpose-defined modes drawing on the same underlying capacities. Sports mode coordinates body, attention, and memory toward competitive performance; study mode coordinates the same capacities toward sustained reading and synthesis. The modes coexist as facets of one person; the underlying capacities are shared across both rather than duplicated for each.

The analog is conceptual scaffold, not architectural specification. Paper 2 names it because the framing captures the structural shape quickly. The architectural substance lives in the six properties §2 names.

## 5. Inherited Paper 1 commitments at aspect level

Paper 2 inherits Paper 1's six architectural commitments at every level of structure. Four bear directly on the aspect's operational content.

**Human-governed (A1.01).** Aspects are human-governed. The three rights — to inspect, to modify, and to override — apply to the aspect's coordination logic, purpose specification, and cell-membership relations, available at any time. A vendor or runtime layer that could in principle prevent any of the three rights from being exercised over aspect-level content disqualifies the deployment from CKS coherence at aspect scope.

**Composition requirements (A1.13).** Aspects are compositions. The five composition requirements A1.13 formalizes — per-substrate human governance, conflict preservation across boundaries, addressable provenance across boundaries, AI-as-substrate-mediator at every layer, human-selective composition — apply twice over: to the aspect-internal composition (cells composing within the aspect arrangement) and to the aspect-external composition (the aspect coordinating with other aspects within the Self). Both must satisfy the constraint set; neither is exempt by virtue of operating at a different scope.

**Three adjacencies (A1.14).** Aspect operations engage substrate, mediator, and human adjacencies in the manner Paper 1 specifies. The aspect's coordination logic lives in substrate; the aspect's pattern questions are answered by the LLM operating as mediator over substrate content; humans hold authority over aspect-level governance. The adjacencies do not change shape at aspect scope.

**Hybrid systems composition (A1.16).** Aspect-level coordination is hybrid in the Paper 1 sense. Substrate handles aspect-level coordination logic and governance; the LLM handles pattern-matching where the aspect's questions call for it. The three composition patterns A1.16 names — adjacent component as input to a cell, as derived view of substrate, as separate concern — extend to aspect scope.

## 6. Operational implications

Naming the aspect as standalone foundational commitment has four operational implications at the architectural layer.

**Aspects are operationally addressable.** A deployment can name an aspect, operate over it, govern it as a unit, and refer to it from other substrate content. The aspect's coordination logic is itself substrate-resident authoritative content per the substrate-as-source-of-truth commitment. What the aspect coordinates, how its coordination proceeds, what pattern questions it asks, and what its purpose specifies are all addressable substrate content.

**Aspect-cell membership is substrate-resident and governable.** Which cells participate in which aspects is substrate content, governable per A1.01, recordable per A1.07 (path retraceability), and auditable. This makes aspect arrangements first-class architectural artifacts rather than implicit groupings emerging from runtime behavior. A human exercising the inspect right reads cell-membership relations directly; the modify right changes them; the override right dissolves them or reassigns cells across aspects without justification to the system.

**Aspects can be created, modified, or dissolved through governance.** Lifecycle operations apply at the aspect level. Aspects can be born under human governance, modified as their purpose evolves, split when distinct purposes emerge, merged when purposes consolidate, or dissolved when no purpose obtains. Subsequent Phase B1 notes formalize each lifecycle operation; the present note names that the operations apply at aspect scope.

**Aspects participate in vertical evolution.** Paper 2's vertical-evolution mechanism reorganizes structure itself: aspects gain or lose cells, aspects split or merge, new aspects are introduced, relational roles reconfigure. Vertical evolution operates on aspects as first-class substrate-resident architectural artifacts. Without aspect addressability, vertical evolution would have to operate on implicit groupings, which would lack the substrate-resident inspectability the architecture commits to.

## 7. What the aspect is NOT

The standalone treatment is not maximalist. Naming what the aspect is not keeps the framing from drifting into stronger commitments than the source paper supports.

**Not an orchestrator controlling cells.** The aspect is a coordination arrangement using cells as content domain, not a controller commanding subordinates. Cells continue to operate under their own orchestration rules and cell-level Paper 1 commitments while participating in the aspect arrangement. The aspect does not strip cells of their cell-scope authority structure; it adds an aspect-scope coordination over what the cells produce.

**Not permanent.** Aspects are not permanent fixtures of a Self. They can be created, modified, split, merged, or dissolved through governance, like any other substrate content.

**Not exclusive in cell membership.** A cell participating in one aspect is not thereby barred from another. Cell-aspect membership is relational; one cell can participate in many aspects simultaneously. Exclusive membership would collapse the relational-role-assignment commitment back into intrinsic membership and break the architectural distinctiveness §3 identifies.

**Not a replacement for cell-level work.** Aspects do not subsume cells or take over cells' informational tasks. Cells remain where informational tasks happen. The aspect's coordination is a separate layer of work — the cross-cell pattern that the aspect's purpose specifies — not a higher-level repetition of what cells already do.

A system that exhibits aspect behavior under any of these strengthened readings is not what Paper 2 commits the term to.

## 8. Operational test

A structure within a CKS-governed Self is an aspect in the Paper 2 sense if and only if all of the following hold at all times during the structure's existence:

1. The structure has a defined purpose, recorded as substrate content humans can inspect, modify, and override.
2. The structure coordinates cells; the cells continue to satisfy Paper 1 commitments and the cell-as-atomic-unit commitment while participating.
3. The structure's cell-membership is relational — cells can participate in this structure and in other aspects simultaneously, with membership recorded as substrate content rather than as intrinsic property.
4. The structure asks pattern questions across its constituent cells for its purpose, operating over the cells as content domain rather than commanding them as subordinates.
5. The structure is substrate-addressable — its coordination logic, purpose specification, and cell-membership relations are substrate-resident content humans can inspect, modify, and override at any time, with no operation, vendor, or runtime layer in principle preventing those rights.
6. The structure coexists within one Self with other aspects, each organized around its own purpose, without requiring exclusivity of cell membership.

A structure that fails any of (1)–(6) may be useful and may be governable in some other sense, but is not an aspect in the Paper 2 sense.

## 9. Conclusion

The aspect is the middle structural level of Paper 2's three-level structure — a coordination arrangement of cells serving a particular purpose, with multiple aspects coexisting within one Self and cells shared across aspects through relational role-assignment. The aspect operates over its cells as content domain by asking pattern questions across them for the aspect's purpose; it is not an orchestrator, not a controller, and not a permanent or exclusive grouping. Paper 1's commitments apply at aspect scope: aspects are human-governed, satisfy composition requirements, engage the three adjacencies as Paper 1 specifies, and compose hybrid via the patterns A1.16 names. Aspects are operationally addressable; their cell-membership relations are substrate-resident and governable; lifecycle operations apply at aspect scope; vertical evolution operates on aspects as first-class architectural artifacts.

Naming the aspect as standalone foundational commitment is what makes the middle level architecturally available. Without it, downstream work would have to choose between collapsing the aspect into the cell — treating coordination as a within-cell concern — or collapsing it into the Self — treating coordination as a Self-scope concern. Both collapses break Paper 2's three-level structure and lose the purpose-defined coordination the aspect specifies.

A subsequent Phase B1 note formalizes the Self as the integrated whole holding multiple aspects. Subsequent Phase B1 notes formalize the DNA and action layers within every cell, lifecycle primitives at every level, evolution mechanisms in productive tension, and structural properties — including the relational-role-assignment commitment and the higher-as-content-domain commitment as standalone, both of which the present note names as properties the aspect commitment carries. The Phase B1 sequence, taken together, gives Paper 2 its complete defensive prior-art coverage at the foundational architectural-commitment level.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Aspect as Coordination Arrangement of Cells for Purpose: A Foundational Commitment Establishing the Middle Structural Level of the CKS Self.* May 7, 2026. ORCID: 0009-0004-8065-3235.
