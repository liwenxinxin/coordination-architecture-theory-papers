# P3↔P2 Lifecycle Governance Inheritance: Shared Substrate Construction Is Governed Birth, Dissolution Is Governed Death — Paper 2's Lifecycle Pattern Applied to the Temporary Inter-Self Entity, With Lifecycle Isolation Preserving Home Governance Independence

**Derivation Note #677 — Series CC, Note CC.11**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in derivation form, how Paper 3's governance of the shared substrate's construction and dissolution directly inherits Paper 2's lifecycle governance pattern — applied to a new entity type at inter-Self scope — and how the lifecycle isolation principle (D2.53) preserves the independence of home lifecycle governance while inter-Self coordination is active.

---

## Abstract

Paper 2 establishes birth, mating, and death as governed lifecycle primitives that apply uniformly at every level of a CKS-governed Self: cells, aspects, and Selves are each created, combined, and retired through governed events, with records at creation and dissolution, human authority over each lifecycle decision, and type-appropriate architectural results. Paper 3 extends this lifecycle governance pattern to the shared substrate — a temporary, multi-organizational coordination entity that exists between home substrates during a Full Aspect Integration (FAI) event. The shared substrate's construction inherits Paper 2's governed birth pattern; its dissolution inherits Paper 2's governed death pattern. Paper 3 does not introduce a new lifecycle governance framework. It applies an existing one to a new entity type. The lifecycle isolation principle (D2.53) ensures that home lifecycle events — births, matings, and deaths within each Self's home substrate — do not automatically propagate to the shared substrate during FAI, preserving the independence of home lifecycle governance from inter-Self lifecycle governance. Mating as a lifecycle primitive is addressed separately in CC.13, where the Paper 2 mating pattern's direct extension to FAI is developed in full.

---

## 1. The inheritance identification

Paper 2 (Li, April 2026b), §6, establishes Claim 3: the lifecycle primitives of birth, mating, and death apply as governed events at every level of the structural machinery a CKS-governed Self comprises. Every entity that comes into existence does so through a governed creation event. Every entity that ceases operation does so through a governed dissolution event. Records accompany both. Authority over each lifecycle decision belongs to humans; labor is allocable across humans and LLMs operating under human direction.

Paper 3 (Li, April 2026c), §4, introduces the shared substrate as a new entity type: a CKS substrate constructed temporarily to mediate inter-Self coordination, with a governance perimeter that spans multiple Selves' home perimeters, and a lifecycle that is bounded to the FAI event by architectural commitment rather than by operational choice. The shared substrate comes into existence through a governed construction event; it ceases operation through a governed dissolution event.

The inheritance claim this note formalizes is specific: the shared substrate's construction and dissolution governance are not fresh architectural machinery. They are Paper 2's birth and death lifecycle governance patterns applied to a new entity. The pattern is preserved; the entity is new.

---

## 2. The source commitment: Paper 2's lifecycle governance pattern

Paper 2's lifecycle governance commitment has three components for each entity type. This note focuses on birth and death; mating is addressed in CC.13.

**Governed birth.** A new cell, aspect, or Self comes into existence when humans authorize its creation under their governance authority. The creation event produces a construction record: the initial configuration of the entity's content layers, the governance authorization under which it was created, and the scope it is authorized to operate within. The entity's existence is documented at the moment of creation. The labor of specifying the entity's content is allocable — humans may author it directly, or LLMs operating under human direction may draft it — but the authority over that content is not allocable. Humans hold governance authority over the created entity from the moment of its creation.

**Governed death.** A cell, aspect, or Self ceases operation through a governed dissolution event, not through silent expiration or unrecorded deprecation. Paper 2 names two death types with distinct architectural results: functional obsolescence (deletion of an entity whose function is no longer needed, releasing its substrate resources) and lineage supersession (retirement-with-archival of a parent entity after a superior offspring emerges, with archived content remaining substrate-addressable). Across both types, dissolution requires a dissolution record — what is being retired, what persists, what governance obligations are closed by the dissolution, and what obligations carry forward. The entity's end is documented as the entity's existence was.

**Records at creation and dissolution.** The lifecycle governance pattern requires documentation at both endpoints of an entity's existence. The substrate knows when an entity was created, under what authorization, and — when the entity ceases operation — when it was dissolved and what the dissolution produced. This record-keeping is what makes the lifecycle governable rather than merely operational.

---

## 3. Extension to inter-Self scope: construction as governed birth, dissolution as governed death

Paper 3 extends the lifecycle governance pattern to the shared substrate. The extension does not change the pattern. It applies the pattern to an entity type Paper 2 did not address: a temporary, multi-organizational coordination object whose governance perimeter spans more than one Self's home perimeter.

**Construction as governed birth (D2.01).** The shared substrate comes into existence when both participating organizations' governance authorities authorize its construction. The pre-construction configuration — which aspects each Self contributes, the depth of provenance carry-over at the perimeter, and the persistence policy after the event dissolves — is authored as substrate content under joint authority before construction begins. The approval mechanics are themselves governance-configurable. The shared substrate's construction record documents the initial configuration, the joint authorization, and the governance scope the substrate is authorized to operate within. This is Paper 2's governed birth pattern at inter-Self scope: a new entity is created through a governed specification event, with records and authorization, and human authority over the created entity from the moment of its existence.

**Dissolution as governed death (D2.02).** The shared substrate dissolves at the close of the FAI event. This dissolution is a governed event: a dissolution record documents what the shared substrate contained, what persistence policy applies to its content, and what each participating Self's home substrate will receive through the hand-off boundary. Persistence policy is governance-configured substrate content — the range of options runs from nothing-retained to durable-record, and the configuration is made before construction begins. Post-dissolution obligations are specified: the hand-off boundary activation triggers ingestion of FAI-derived content into each home substrate under each home perimeter's governance authority. The shared substrate's dissolution is Paper 2's governed death pattern at inter-Self scope: an entity ceases operation through a documented, authorized event, with records, persistence policy, and specified post-dissolution obligations.

**The temporary-by-design property as lifecycle expression.** Paper 3's commitment that the shared substrate is temporary by design (D1.01) is the inter-Self scope expression of lifecycle governance's requirement that every entity's existence is bounded and governed at both endpoints. A shared substrate whose lifecycle is governed has a defined creation event and a defined dissolution event. Temporary-by-default is not merely an operational policy; it is the lifecycle governance pattern applied to an entity whose coordinating purpose is bounded to the FAI event that occasions its construction.

---

## 4. Lifecycle isolation: preserving home governance independence

The lifecycle isolation principle (D2.53) completes the extension by specifying what the shared substrate's lifecycle governance does not affect. Home lifecycle events — births, matings, and deaths within each participating Self's home substrate — continue during FAI without automatically propagating to the shared substrate.

This isolation is an architectural commitment, not an operational option. The governance boundary between home lifecycle governance and inter-Self lifecycle governance is maintained by design. If a cell within one participating Self is born during the FAI event, that birth is a governed event within the home substrate under home governance authority; it does not automatically create content in the shared substrate. If a cell within one participating Self is retired during the FAI event, that dissolution is governed within the home substrate; it does not automatically dissolve content in the shared substrate that was contributed by that cell. Home lifecycle governance and inter-Self lifecycle governance are structurally independent during FAI.

The isolation principle produces a specific architectural property: Paper 2's lifecycle governance machinery and Paper 3's lifecycle governance machinery can operate simultaneously without interference. Participating Selves do not need to pause their home lifecycle operations to participate in inter-Self coordination. The shared substrate's lifecycle — construction through dissolution — is governed as a unit, and the home substrates' lifecycle operations are governed within their home perimeters. Neither lifecycle governance scope subordinates the other.

This independence is the governance protection that makes the shared substrate viable as a temporary coordination entity across organizational boundaries. Each participating organization retains full governance authority over its home lifecycle operations. The inter-Self coordination event does not require either organization to cede home lifecycle governance during FAI.

---

## 5. What is preserved, what is new, and the prior-art inheritance claim

**What is preserved.** The lifecycle governance pattern: governed creation with authorization and construction record, governed termination with dissolution record and post-dissolution obligations, documentation at both lifecycle endpoints. This pattern holds for every entity type Paper 2 names — cells, aspects, and Selves — and it holds for the shared substrate Paper 3 introduces. The pattern does not change.

**What is new.** The entity type: the shared substrate is a multi-organizational temporary entity that exists between home substrates, with a governance perimeter spanning multiple Selves' home perimeters. Paper 2 did not address this entity type. Paper 3 extends the lifecycle governance pattern to cover it. The extension is the contribution; the pattern is the inheritance.

**Mating is addressed in CC.13.** The lifecycle primitives note (CC.11) covers birth and death. Mating — the Paper 2 lifecycle event through which parental content is combined under governance — is the primitive that directly extends to FAI at inter-Self scope. FAI is Paper 2's mating primitive applied to the inter-Self coordination context: aspects from multiple Selves combine in the shared substrate under governance, with three pattern variants governing how combination is performed. That inheritance is developed fully in CC.13. This note acknowledges the distinction and defers mating's inter-Self inheritance to its dedicated treatment.

**Prior-art inheritance claim.** Paper 3's construction and dissolution governance directly inherit Paper 2's birth and death lifecycle governance patterns. The shared substrate's governed lifecycle is Paper 2's lifecycle governance applied to a new entity type at inter-Self scope. Anyone implementing a shared substrate for inter-Self coordination with governed construction and governed dissolution is implementing Paper 2's lifecycle governance at inter-Self scope. The lifecycle isolation principle (D2.53) is a novel specification of how home lifecycle governance and inter-Self lifecycle governance coexist; the underlying lifecycle governance pattern that isolation protects is Paper 2's.

---

## Source papers

Li, W. (2026a). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *P3↔P2 Lifecycle Governance Inheritance: Shared Substrate Construction Is Governed Birth, Dissolution Is Governed Death.* Derivation Note #677, Series CC, Note CC.11. May 15, 2026. ORCID: 0009-0004-8065-3235. License: CC BY 4.0.
