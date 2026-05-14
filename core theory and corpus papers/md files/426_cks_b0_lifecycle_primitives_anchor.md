# Lifecycle Primitives as Paper 2's Third Architectural Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its contribution is to anchor the source paper's third architectural claim — that birth, mating, and death are governed primitives applicable recursively at every structural level — as a named, severable prior-art claim, with the four foundational sub-commitments and the operational decomposition and anti-pattern series that derive from it.

## Abstract

The source paper's third architectural claim is that three lifecycle operations — birth, mating, and death — are governed primitives that apply, with identical governance requirements, at all three structural levels (cell, aspect, Self). Each is a human-authorized event with a governance record, and the chain of such records across an entity's existence is itself substrate content that extends path retraceability from substrate-content scope (Paper 1, sub-commitment A1.07) to entity scope. This note states the claim, restates each primitive in operational form, identifies the severable prior-art content inside each (three mating pattern variants; multiple death types; archival reactivatability), names the lineage chain as the artifact that carries entity-scope retraceability, distinguishes what is inherited from Paper 1 from what is new in Paper 2, maps the four foundational sub-commitments (B1.05–B1.08) and the operational and anti-pattern note series that descend from it, and provides an operational test.

## 1. Why the claim needs to be anchored

The source paper names six architectural claims; the third commits to lifecycle primitives at every level. Four properties are bundled into the phrase, each independently defensible.

**(a) The set is closed at three.** Birth, mating, and death are the only entity-scope lifecycle primitives the architecture recognizes. Other operations on entities — re-anchoring, re-scoping, decomposition, recomposition — reduce to combinations of the three plus orchestration-rule changes; they are not additional primitives.

**(b) Each is human-governed.** Every birth produces a governance record; every mating produces a mating record; every death produces a death record. None occurs without human authorization. The commitment is governance, not labor: humans may directly perform the originating, combining, or closing work, or LLMs may perform it under human direction, but the authorization remains human.

**(c) The same three apply at every level.** Cell, aspect, and Self share governance requirements for each primitive. The level affects the scope of the governance record but not the structure of the operation. Recursive applicability is itself a prior-art claim, severable from the existence of the primitives.

**(d) The lineage chain is a substrate artifact.** The chain of governance records accumulated across an entity's existence is substrate content, not metadata produced by a logging layer — inspectable, modifiable only under authority, persistent across archival states.

These four properties are severable: a system could implement any one without the others, and each is defensible independently. Naming them explicitly is what makes the claim a checkable architectural commitment rather than an informal lifecycle convention.

## 2. The claim, stated

The Coordination Knowledge Substrate pattern, as extended by the source paper, commits to the following as a single architectural claim, hereinafter **Claim 3**:

> Birth, mating, and death are governed primitives. Each is a human-authorized event with a governance record. The three apply, with identical governance requirements, at every structural level (cell, aspect, Self). Across an entity's lifecycle, the governance records form a lineage chain that is itself substrate content and that extends path retraceability from substrate-content scope to entity scope.

The structure is **{three primitives} × {three levels} × {one lineage-chain artifact}**, with the four severable properties of §1 distributed across that structure.

## 3. The three primitives in operational detail

**Birth** is the operation by which a new entity begins governed existence. The architecture requires four things: a governance record authored by humans or by an LLM under human direction; an initial DNA specification (the entity's DNA-layer content at the moment of birth, possibly minimal); a level determination (cell, aspect, or Self); and a lineage anchor (a parental reference when birthed through mating, or an origination anchor when birthed *de novo* under direct authorization). Birth that fails any of the four is what B3.10 names *Ungoverned Birth*.

**Mating** is the operation by which two or more parent entities' content is combined to produce one or more offspring. Mating combines parental content across both the DNA layer and the action layer (recorded task instances and their outputs), governed by orchestration substrate. The architecture requires three things: human authorization (direct, or under orchestration rules humans have authored); a mating record (naming parents, offspring, timestamp, and pattern variant); and a pattern variant selection (§4). The offspring is birthed in the sense above, with the mating record as its lineage anchor. Mating without authorization is what B3.11 names *Ungoverned Mating*; mating without a record is what B3.12 names *Untracked Mating*, which produces lineage loss.

**Death** is the operation by which an entity closes its governed existence. The architecture requires three things: human authorization; a death record naming the closed entity, the cause-of-death classification, the authorization, and (where applicable) the superseding entity; and preservation of the entity's records in archival state, with reactivation under new governance authorization remaining architecturally available. Death here is operational retirement with record preservation, not deletion of state. §5 treats the multiple death types and archival reactivatability as severable sub-claims.

## 4. Three mating pattern variants as severable sub-claims

*How* parental content is combined is itself a governed choice; the source paper names three variants. Each is severable as prior art: a deployment could implement one, two, or all three, and each produces different downstream governance implications.

**Variant 1 — Union.** All content from all parents is combined in the offspring. Conflicts between parental content — contradictory DNA rules, incompatible action-layer records, incoherent schema overlaps — are preserved as first-class substrate state in the offspring, in the Paper 1 conflict-preservation sense. The offspring inherits the work of resolving the conflicts under governance, as one of its post-birth activities.

**Variant 2 — Selective merge.** Governance — humans directly, or LLMs under human direction — pre-curates what crosses the mating boundary. Some parental content is selected into the offspring; the rest remains in the parents. The offspring is born with content humans have authorized into it; it inherits less work than a Union offspring, at the cost of placing the merge decisions in the mating event itself.

**Variant 3 — Lineage-preserved union.** All parental content is combined as in Union, and the offspring additionally carries explicit cross-references to each contributing parent for every element. The offspring's substrate content becomes queryable by provenance: any element can be traced to the parent (or parents) it descended from. This variant fits regulated domains, high-stakes decisions, and environments where reconstitution of the parents from the offspring must remain architecturally possible.

The three share the same three mating governance requirements but impose different subsequent governance work: Union front-loads conflict-handling into the offspring; Selective merge front-loads selection into the mating event; Lineage-preserved union maintains parent-traceability indefinitely as substrate content. Naming them severably is what makes each independently defensible and what makes the operational decompositions in the B2.40–B2.56 series sensible — each variant requires its own treatment.

## 5. Death types and archival reactivatability as severable sub-claims

### 5.1 Multiple death types

The source paper distinguishes governed death patterns by underlying cause. Three are named:

- **Functional obsolescence.** The entity is no longer operationally needed for the deployment's current work.
- **Lineage supersession.** The entity is retired because DNA evolution has produced a superior offspring whose orchestration handles what this entity's orchestration handled. The cause is downstream from a mating event whose offspring outperforms.
- **Capability supersession.** The entity is retired because the class of capability it provided is now handled elsewhere — through instinct evolution (the fast-path layer now handles what previously required explicit reasoning) or through DNA evolution that consolidates or automates the capability into another entity.

Each type implies a different decision process. The three are severable: a deployment may implement any subset; each is defensible as prior art independently.

### 5.2 Archival reactivatability

A distinct property of death, severable from the multiple-death-types property, is that **death does not destroy**. The entity's substrate content, its lineage chain, and its full state at closure are preserved in an archival state from which reactivation under new governance authorization remains architecturally possible. Reactivation is itself a governed event — it produces its own record appended to the lineage chain — but the architecture does not foreclose it.

Archival reactivatability has three independently defensible components: (a) **records persist** — the entity's birth record, mating records, any prior reactivation records, and its death record remain substrate content after closure, inspectable under the same rights that apply to active substrate content; (b) **state remains addressable** — the entity's DNA-layer and action-layer content remain queryable in archival form, not erased; (c) **reactivation is architecturally available** — a new governance event can move the entity from archival to active state, with the reactivation record appended to its lineage chain. The architecture does not promise reactivation will be exercised; it commits only that the path remains open.

A system that retires entities by deletion does not satisfy this property. A system that preserves state but forecloses reactivation as a matter of architecture (rather than as a matter of operator choice in a specific case) does not satisfy it either.

## 6. The lineage chain as entity-scope path retraceability

Paper 1 established **path retraceability** as an accountability commitment at substrate-content scope (Paper 1 Claim 3, sub-commitment A1.07): any substrate content can be traced backward to the decisions, rationale, and conflicts that produced it. Paper 2's third claim extends the commitment to a new scope — the entities (cells, aspects, Selves) that hold substrate content. The **lineage chain** carries the extension.

Across an entity's existence the architecture accumulates: the birth record, with its initial DNA specification and lineage anchor; every mating record the entity participated in, as parent or offspring; every directed-selection event applied to the entity under DNA evolution; and, on closure, the death record with its cause-of-death classification and archival state pointer. The chain is substrate content. It is inspectable; it is modifiable only under authority (corrections to historical records are themselves governed events, recorded as such); it persists through archival state.

The chain is what makes the operational test in §8 answerable. For any entity an observer with appropriate access can find the birth record, trace mating history, identify directed-selection events, verify lifecycle state, and — with appropriate authority — reconstitute the entity's DNA-layer content as of any point in its history. The chain is not an audit log produced by a logging layer; it is substrate content produced by the lifecycle primitives themselves. A deployment that produces audit logs but does not carry lineage as substrate content may satisfy compliance frameworks; it does not satisfy this claim.

## 7. Recursive application and relationship to Paper 1

The three primitives apply recursively to all three levels: cells, aspects, and Selves can each be birthed, mated, and closed. The governance requirements of §3 are the same at each level. The level affects only the scope of the governance record — who must authorize a Self birth differs from who must authorize a cell birth — but the structural requirements (birth record, initial DNA specification, level determination, lineage anchor) are the same. Recursive applicability is itself a prior-art claim, severable from the existence of the primitives: a system could implement lifecycle primitives only at the cell level, with aspects and Selves architecturally fixed, without satisfying it.

The claim inherits from Paper 1 that the substrate is human-governed (the three rights apply to lifecycle records and lineage chains as to all other substrate content), that path retraceability holds at substrate-content scope (extended, not replaced), and that conflicts are preserved as first-class substrate state (directly relevant to the Union mating variant). The claim adds, beyond Paper 1: that entities are first-class architectural objects with governed lifecycle events; that the closed set of entity-scope operations is three; that mating has three severable pattern variants; that death has multiple severable cause-of-death types and an archival-reactivatability property; that the lineage chain extends retraceability to entity scope; and that all of the above apply recursively at all three levels. The extension is monotonic: Paper 1 deployments remain valid; Paper 2 deployments are Paper 1 deployments that additionally satisfy these entity-scope commitments.

## 8. Operational test and sub-commitment map

### 8.1 Operational test

A deployment instantiates this claim if and only if, for every entity in the deployment, all of the following are true at all times during the entity's existence (including archival states):

1. There is a birth record, locatable from the entity, identifying the authorizing party, the initial DNA specification, the level determination, and the lineage anchor.
2. For every mating event the entity participated in, there is a mating record, locatable from the entity, identifying the parties, the pattern variant, and the offspring.
3. If the entity is archived, there is a death record, locatable from the entity, identifying the cause-of-death classification, the authorization, and the archival state pointer; the entity's substrate content remains addressable in archival form; reactivation under new governance authorization remains architecturally available.
4. The full lineage chain across (1)–(3) is substrate content (not an external log), is inspectable, and persists across active and archival states.
5. The above hold regardless of whether the entity is a cell, an aspect, or a Self.

A deployment that fails any of (1)–(5) for any entity may be useful in some other architectural setting, but does not satisfy this claim.

### 8.2 Sub-commitment map

The four foundational sub-commitments that decompose this claim, derived in the Phase B1 series, are:

- **B1.05** — Birth as governed lifecycle event (the four requirements of §3; failure mode B3.10 *Ungoverned Birth*).
- **B1.06** — Mating as governed lifecycle event with three pattern variants (the three requirements of §3, the three severable variants of §4; failure mode B3.11 *Ungoverned Mating*).
- **B1.07** — Death as governed lifecycle event with multiple death types and archival reactivatability (the three requirements of §3, the three severable death types of §5.1, the three-component archival reactivatability property of §5.2).
- **B1.08** — Lineage chain integrity across all lifecycle events as governance artifact (the entity-scope path retraceability commitment of §6; failure mode B3.12 *Untracked Mating / Lineage Loss*).

The operational decompositions of B1.05–B1.08 are formalized across **B2.40–B2.56** (seventeen notes), covering birth-record verification at each level; the three mating variants in operational detail; the three death types in operational detail; archival state representation and addressability; reactivation operations under new governance authorization; lineage-chain extensions across each lifecycle event type; and the recursive application of each at the cell, aspect, and Self levels. The anti-pattern formalizations for this claim are **B3.10** (Ungoverned Birth), **B3.11** (Ungoverned Mating), and **B3.12** (Untracked Mating / Lineage Loss).

## 9. Conclusion

The claim names a small set of primitives (three), a uniform governance structure (the same requirements at every level), and an artifact (the lineage chain) that extends path retraceability from substrate content to the entities that hold it. It is severable into independently defensible properties — the closed set of three primitives, the human-governed structure of each, the three mating pattern variants, the multiple death types, archival reactivatability, recursive application at all three levels, and the lineage chain itself — each formalized in the sub-commitments that descend from this claim and tested by the procedure of §8.1.

A system that births entities without governance records, mates them without recording the operation or its pattern variant, or closes them by destroying their state does not instantiate the third claim of *The Instinct/Reasoning Separation Outside the Model*, and the properties that derive from it — entity-scope path retraceability, the productive tension between mutation and directed selection (Claim 4) operating over a stable lineage, multi-level composition coherence under reorganization — do not apply to it. Subsequent work that uses the terms *birth*, *mating*, or *death* without governance records, without the lineage chain, without recursive applicability, or with deletion in place of archival reactivatability is using different concepts, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Lifecycle Primitives as Paper 2's Third Architectural Claim.* May 14, 2026. ORCID: 0009-0004-8065-3235.
