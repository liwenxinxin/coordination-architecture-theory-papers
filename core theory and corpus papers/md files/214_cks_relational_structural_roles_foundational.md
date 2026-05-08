# Structural Roles as Relational and Purpose-Defined: A Foundational Architectural Commitment in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as standalone foundational architectural commitment, the property already named in Paper 2's three-level structural framework: that structural roles in CKS architectures are *relational and purpose-defined* rather than intrinsic, with the same underlying CKS artifact able to participate as a cell in one structural arrangement, as part of an aspect in another, or as a component of multiple aspects simultaneously, depending on what the structure is for.

## Abstract

Paper 2 introduces three architectural levels — cell, aspect, Self — and states at the opening of its three-level structural development that structural roles are relational and purpose-defined rather than intrinsic. Paper 2's "where CKS exceeds biology" subsection names the property again as architectural advantage: biological cells are fixed in their tissue and organ memberships through development, while CKS cells can participate in multiple aspects simultaneously. This note formalizes the property as a standalone foundational commitment, distinct from the level-definition work it does inside the three-level framework. Standalone treatment is necessary because the property's reach extends beyond defining what cells, aspects, and Selves are: it is what makes vertical evolution operationally available, what gives aspect membership its flexibility, what enables cross-level access patterns, and what supports cells participating across multiple aspects without copy-and-instantiate semantics. The note states the commitment precisely, distinguishes it from the conventional intrinsic-role pattern in adjacent architectures, names where CKS exceeds biology, traces the inherited Paper 1 commitments that hold across role assignments, articulates the operational implications, names the limits, and provides an operational test.

## 1. Why structural-roles-as-relational-and-purpose-defined needs to be formalized as standalone

The relational-and-purpose-defined property is named twice in Paper 2's core theory: at the opening of the three-level structural development ("Structural roles are relational and purpose-defined rather than intrinsic — the same underlying CKS artifact can participate as a cell in one structural arrangement, as part of an aspect in another, or as a component of different aspects simultaneously, depending on what the structure is for") and again in the disclaim that Paper 2 is not a rigid three-level hierarchy. Paper 2 §5.2 develops the commitment further as one of two architectural commitments shaping how the three levels relate, naming it *relational structural roles* alongside governance-boundary inheritance.

A separate Series B note formalizes the three-level structural framework, where the relational property does load-bearing work — it is what makes the three levels not a rigid hierarchy. But the property's reach extends beyond level definition. Vertical evolution reorganizes structural arrangements through governed reorganization, and the reorganization works because role assignments are relational; if cells were intrinsically bound to their aspects, vertical evolution as architectural primitive would not be operationally available. Aspect membership flexibility — cells participating in multiple aspects simultaneously — requires the same relational framing. Content-domain relationships and cross-level access patterns treat higher-to-lower level relationships as structural arrangement rather than fixed containment, again depending on the relational property. And Paper 2's "where CKS exceeds biology" subsection names relational rather than intrinsic structural roles as a point at which CKS holds an architectural property biology cannot match.

Naming the property as standalone foundational commitment makes these consequences traceable to one underlying architectural choice. It also opens the structural properties cluster within Phase B1 — B1.17 (this note), B1.18 (content-domain relationships), B1.19 (cross-level access patterns), B1.20 (recursive Paper 1 commitments at every level) — which together elaborate the structural framework Paper 2 introduces.

## 2. The architectural commitment, precisely stated

In a CKS architecture, **structural roles are relational and purpose-defined rather than intrinsic.** The commitment has four operational components.

**(a) Relational role assignment.** The role an artifact occupies — cell within an arrangement, member of an aspect, component participating in a Self — is determined by its relational position within a structural arrangement, not by intrinsic properties of the artifact. The artifact is the bearer of identity; the role-instance inheres in the bearer per the structural arrangement that calls on it.

**(b) Purpose as the determinant.** The structural arrangement is itself defined by the purpose it serves. An aspect is a coordination arrangement of cells serving a particular purpose; cells participate in that arrangement because the purpose calls for what they carry. Roles are not intrinsic identity properties because purpose, not artifact, drives the assignment.

**(c) Multiple-arrangement participation.** The same underlying CKS artifact can participate as a cell in one structural arrangement, as part of an aspect in another, and as a component of multiple aspects simultaneously. The question "is X a cell or part of an aspect" has the answer "X participates as a cell within arrangement Y for purpose P, and as part of an aspect within arrangement Z for purpose Q." Multiple participation is operationally legitimate, not a degraded or ambiguous state.

**(d) Reassignability through governed reorganization.** Role assignments are not permanent. Vertical evolution reassigns roles through governed reorganization: cells move between aspects, aspects gain or lose constituent cells, new aspects are introduced, existing aspects are dissolved or merged. Governance for these reassignments is human-governed per Paper 1's commitments and substrate-resident per the source-of-truth commitment.

The four components together define the property as it operates in CKS architectures. A system in which any of (a)–(d) fails does not instantiate the property even if it satisfies the others.

## 3. What makes the relational property architecturally distinctive

The standard pattern in adjacent modular-software architectures commits to *intrinsic* structural membership: a service belongs to one bounded context, an aggregate to one service, a component to one composite. Microservices-plus-DDD treats service boundaries as identity-conferring; component frameworks treat composite membership as a property of the component's instantiation. CKS commits to the inverse — same underlying unit of identity, multiple structural role-instances per arrangement, governance attached per arrangement rather than per unit.

Two consequences follow from the inversion. First, an artifact's role is not "what it is" but "how it participates in structures." The artifact's identity persists across role assignments; what changes is the arrangement that calls on it. Second, multiple-aspect participation is the *same* artifact participating in multiple arrangements, not copies of the artifact. Substrate operations on the artifact are observable across all aspects in which it participates, and changes propagate per arrangement rather than requiring synchronization across copies. The sports-vs-study analogy Paper 2 uses to render the framework intuitive captures this property: a person's competitive-sports mode and calm-study mode draw on the same underlying capacities, not on copies of the capacities, but on the same capacities through different relational arrangements.

The architectural mechanism — same underlying state, different role-instances per arrangement, governance per arrangement rather than per unit — has lineage in three closest-adjacent strands Paper 2 §5.2 names: object-capability formalisms (one underlying object referenced through multiple capabilities, each conferring distinct rights), formal-ontology work on roles and qua-entities (multiple roles inhering in the same bearer simultaneously), and deontic-token agent-community formalisms (the same agent filling different roles in different communities, each role carrying its own obligations per arrangement). The CKS commitment synthesizes these three at multi-level composition scope over a human-governed substrate under Paper 1's commitments.

## 4. The biological analog and where CKS exceeds biology

The biological analog functions as conceptual scaffold rather than architectural authority. Biological cells differentiate during development and become fixed in their tissue and organ memberships. Once a cell differentiates into a neuron, it is a neuron; once it is part of a particular tissue, it stays in that tissue. Membership is intrinsic in the biological case because biological tissue formation requires cells to commit to roles for organ formation — biology had no mechanism for relational membership at multicellular scale.

CKS architectures do not inherit this constraint. Aspects are coordination arrangements rather than physical tissues; the artifact is not consumed by joining an arrangement, and joining one arrangement does not preclude joining others. The contrast belongs alongside the other points where CKS exceeds biology — directedness alongside undirectedness, modularity from the start rather than evolved, reversibility through archived addressability, cross-lineage mating compatibility, structural evolvability on operational timescales — as architectural property the engineered design pattern can commit to upfront because the constraints that produced biological fixity do not apply.

The relational-and-purpose-defined property is therefore not a property biology has and CKS imitates. It is a property biology lacks (because of mechanism) and CKS holds (because of design). The biological vocabulary functions as conceptual scaffold; the architectural substance is relational identity through participation in human-governed structural arrangements.

## 5. Inherited Paper 1 commitments at relational roles

Every Paper 1 commitment holds for the artifact regardless of which role it participates in. The relational property does not weaken any inheritance; it places the inheritance at the artifact rather than at the role.

**Human-governed authority** holds for role assignments themselves: assignments are substrate content under human authority; humans inspect, modify, and override them at any time, and the orchestration rules that bind artifacts to arrangements for purposes are human-authored. **The substrate-cell boundary** is intrinsic to the artifact and persists across role assignments — same artifact, same boundary, multiple role-instances. **Composition requirements** apply to the arrangement, not to a fixed identity property of any artifact in it. **Path retraceability** holds across role changes because each reassignment is a substrate operation with provenance; the audit trail tracks which artifact participated in which role at which time, under what authority, for what purpose. **Substrate-as-source-of-truth** places role assignments themselves in the substrate as authoritative content — "which artifacts participate in which structures for what purposes" is answered by reading the substrate, not by querying agent state, vendor configuration, or runtime middleware. **AI-as-substrate-mediator** persists unchanged: the LLM may participate in role-assignment work — drafting reorganization proposals, identifying candidate aspect compositions, assisting with provenance interpretation — under human authority and substrate mediation. **Tool-agnosticism** carries: role assignments are realizable in any environment that satisfies the three minimal requirements (persistent structured state, human read/write access, LLM access).

The inheritance is direct because the relational property attaches to roles, not to artifacts. Paper 1's commitments remain commitments to the artifact; the role is what changes per arrangement.

## 6. Operational implications

Five implications follow from the commitment.

**Role assignments configure through orchestration rules.** Deployments specify which artifacts participate as cells, in which aspects, for what purposes, by authoring orchestration rules that bind artifacts to arrangements. Rule authoring is governance exercised at design time and amortized across every cell execution that follows.

**Aspects manage membership relationally, not by ownership.** An aspect names a coordination arrangement and a purpose; cells participate per the purpose it serves, and the same cells may participate in other aspects under other arrangements simultaneously. Aspect-level orchestration coordinates the cells through substrate-mediated composition; it does not constrain them to single membership.

**Vertical evolution reassigns roles through governed reorganization.** Reassigning a cell across aspects, splitting an aspect, merging two aspects, introducing a new aspect, dissolving an unused aspect — all proceed as governed substrate edits over role-binding content, under the same machinery as lifecycle primitives and DNA evolution, not as code changes requiring redeployment.

**Multiple-aspect participation is operationally distinct from copy-and-instantiate.** A cell that participates in multiple aspects is the same cell, not copies. Substrate operations on the cell — DNA-layer refinements, action-layer accumulation, expression configuration — are observable across all arrangements in which it participates. This is what makes substrate-shared topology operationally available at Self scope: cross-aspect coordination becomes first-class capability because the cells are shared, not because integration glue ties separate copies together.

**Inspectable through substrate inspection.** Humans inspecting substrate can see which artifacts participate in which arrangements for what purposes by reading role-binding content directly. Provenance for role changes is substrate-resident per the path-retraceability commitment.

## 7. Limits

The standalone treatment must not extend the commitment beyond what Paper 2 supports.

**Not role-less artifacts.** Artifacts have intrinsic content — substrate content they carry, processing logic, harness configuration, lineage. The relational property is about *roles in structures*, not about artifact identity entirely. The artifact is the bearer of intrinsic identity; what is relational is its structural-role-instance per arrangement.

**Not unlimited flexibility.** Role assignments are governed per Paper 1's authority architecture. An artifact cannot self-assign to an arrangement; arrangements cannot pull artifacts in without governance. The property names *governed reassignability*, not *unconstrained mobility*.

**Not unrecorded changes.** Reassignments are substrate-resident with provenance; each change leaves an audit trail per the path-retraceability commitment. The relational property does not weaken the accountability vocabulary; it strengthens it by making role changes first-class substrate events.

**Not elimination of level distinctions.** Cells, aspects, and Selves remain architecturally distinct levels with distinct scopes — cell handling a specific informational task, aspect grouping cells for a purpose-defined mode of engagement, Self holding multiple aspects and their collective intelligence as one whole. The relational property is about which artifacts participate in which roles within those levels, not about collapsing the levels.

**Not a general identity claim.** The property is about CKS artifacts in CKS structural arrangements. It is not a general claim about identity in distributed systems, in software architectures broadly, or about identity philosophically.

**Not lacking Paper 1 commitments.** Paper 1's six commitments hold for the artifact regardless of role. The relational property composes with Paper 1; it does not displace any inheritance.

## 8. Operational test

A system instantiates the relational-and-purpose-defined commitment if and only if all of the following hold at all times during the substrate's existence:

1. The same underlying CKS artifact can be assigned to participate as a cell within one structural arrangement and as part of an aspect within another, simultaneously, without copy-and-instantiate.
2. Role assignments are determined by relational position within a structural arrangement and the purpose that arrangement serves, and are not derivable from intrinsic properties of the artifact alone.
3. Role assignments are substrate-resident authoritative content, authored under human authority through orchestration rules, with provenance.
4. Role assignments are reassignable through governed reorganization without violating Paper 1 commitments to the artifact.
5. Substrate operations on the artifact are observable across all arrangements in which the artifact participates; the artifact is the same artifact across role-instances, not copies.

A system that fails any of (1)–(5) does not instantiate the commitment specifically, regardless of how robustly it satisfies other Paper 2 commitments.

## 9. Why naming as standalone matters

Embedded within the three-level structural framework, the relational property does load-bearing work for level definition. As foundational commitment in its own right, it does additional work: it grounds vertical evolution as architectural primitive, makes aspect-membership flexibility describable, supports cross-level access patterns where purpose requires, names one of the points where CKS exceeds biology, and provides the architectural shape that substrate-shared topology depends on at Self and enterprise-brain scope.

This note opens the structural properties cluster (B1.17 relational-and-purpose-defined, B1.18 content-domain relationships, B1.19 cross-level access patterns, B1.20 recursive Paper 1 commitments) which closes Phase B1. Together the cluster elaborates the structural framework Paper 2 introduces — what the levels are, how they relate, what access patterns hold across them, what Paper 1 commitments hold at each. The relational-and-purpose-defined property is what makes the elaboration cohere: without it, the levels would be a rigid hierarchy, the access patterns would be strictly downward, and the inheritance would be confined to single-arrangement membership. With it, the structural framework holds the flexibility Paper 2 commits to while preserving the Paper 1 commitments the architecture inherits.

Subsequent work that adopts, extends, composes with, or argues against Paper 2's structural framework should use *relational and purpose-defined* in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Structural Roles as Relational and Purpose-Defined: A Foundational Architectural Commitment in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
