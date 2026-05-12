# Purpose-Defined Level Determination: How Purpose Assigns an Entity to a Structural Level in the Coordination Knowledge Substrate

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

The Coordination Knowledge Substrate (CKS) pattern structures composed AI systems across three architectural levels — cell, aspect, and Self — with structural roles defined relationally and by purpose rather than intrinsically. This note formalizes the process by which an entity is assigned to a level: purpose-defined level determination. Level determination is not a design-time technical classification; it is a governed act, recorded as authoritative substrate content, based on criteria specific to each level. A cell is determined at cell level when its purpose is to perform a specific informational task; an entity is determined at aspect level when its purpose is to coordinate cells for a purpose; a Self is determined at Self level when its purpose is to integrate aspects into a coherent whole. The determination record is substrate-resident and authoritative per the source-of-truth commitment (A1.08). Determination is made at birth and may change through governance when purpose changes substantially. Distinguishability tests provide the operational verification mechanism. This note is the second of five notes decomposing B1.17 (relational and purpose-defined roles), following B2.84 (relational roles integrating frame).

---

## 1. Why purpose-defined level determination requires standalone formalization

Paper 2's commitment that structural roles are "relational and purpose-defined rather than intrinsic" (§5.2) establishes the foundation for how entities acquire their structural position in a CKS deployment. The B2.84 integrating frame established the full shape of that commitment: roles are relational in that the same underlying artifact can participate in multiple structural arrangements, and they are purpose-defined in that level membership is based on what the structure is for rather than on technical attributes intrinsic to the artifact. B2.85 formalizes the second half of that commitment more precisely. What does purpose-defined mean, operationally, when assigning an entity to a level? What criteria determine whether an entity belongs at cell, aspect, or Self level? Where is the determination recorded? How does it change when purpose changes?

This precision matters for the defensive-publication series. The claim that structural roles are purpose-defined is defensible as prior art only if purpose-defined is pinned down as an architectural operation rather than left as a design philosophy. A competitor seeking to claim novelty in purpose-based component classification, runtime type assignment based on function, or dynamic role determination will find this note in the prior-art chain. The note also establishes the substrate-residency and governance requirements that distinguish CKS level determination from ad hoc classification schemes that perform similar categorization without the provenance, authority, and governed-change properties the CKS pattern commits to.

Within the B1.17 decomposition, B2.84 established the relational structure — that the same artifact can participate at multiple levels across different deployment arrangements. B2.85 establishes the determination process — how an entity acquires its level assignment in the first place, and what governs that assignment over time. The subsequent notes B2.86 through B2.88 develop same-entity-at-multiple-levels, relational roles and evolution, and verification of role assignments respectively.

---

## 2. The architectural determination precisely stated

Purpose-defined level determination in the CKS pattern operates through five interlocking elements: level-specific criteria, substrate-resident records, determination at birth, governed changes when purpose changes, and distinguishability-test verification.

**Level determination is the process of assigning an entity to a structural level based on its purpose in a specific deployment.** Level assignment is not inferred from technical attributes such as model type, API surface, or storage format. It is determined by asking what the entity is for in this deployment context and applying the level-specific criteria below.

**Three level-specific criteria govern the determination:**

*Cell level determination.* An entity is determined to be at cell level when its purpose is to perform a specific informational task. The determination criteria are: the entity has a defined input domain; it processes inputs through the instinct and reasoning layers per the Paper 2 separation to produce outputs; its primary function is task execution rather than coordination of other entities; and it has a specific operational role rather than a coordinating one. The cell determination test asks: does this entity perform a specific informational task? If yes, the entity is determined at cell level. If no, the criteria for the next level are applied.

*Aspect level determination.* An entity is determined to be at aspect level when its purpose is to coordinate cells for a purpose. The determination criteria are: the entity has a defined purpose statement; it organizes cell participation through coordination rules; its outputs emerge from coordinating cell outputs rather than from direct task processing; and it does not integrate multiple aspects. The aspect determination test asks: does this entity coordinate cells to achieve a purpose? If yes, the entity is determined at aspect level. If no, the criteria for the next level are applied.

*Self level determination.* An entity is determined to be at Self level when its purpose is to integrate aspects into a coherent whole. The determination criteria are: the entity holds multiple aspects as facets; it provides integrated operational intelligence across those aspects; and it holds governance authority over aspect coexistence. The Self determination test asks: does this entity integrate aspects into a coherent intelligence? If yes, the entity is determined at Self level.

**Determination is substrate-resident authoritative content.** The level determination is recorded in substrate as authoritative content (A2.46). The determination record contains three elements: the level declaration (cell, aspect, or Self); the purpose statement supporting the determination; and the determination governance record specifying who made the determination, when, and under what authority (per A2.40 and A2.47). This record — not the entity's observed behavior — is the authoritative source of what level the entity occupies, per A1.08's substrate-as-source-of-truth commitment.

**Determination is made at birth.** Level is determined at birth as part of birth specification requirements. Birth specification includes a type declaration as cell, aspect, or Self; this declaration is the governed origination of the entity's level membership. Birth determination is a governance act: governance decides the level assignment, and labor implements the determination record in substrate.

**Determination changes when purpose changes substantially.** An entity originally determined at cell level may be redetermined at aspect level if its purpose develops to include the coordination of other cells. Redetermination requires a governance decision to update the determination record; the decision and its rationale are recorded per A2.40. Purpose changes do not automatically update the determination. A purpose change is an event that may trigger governance review of whether a level redetermination is warranted; whether redetermination follows is a governance decision, not an automatic architectural inference.

**Distinguishability tests per B2.09 verify determination-function consistency.** The three distinguishability tests — one per level — provide the operational mechanism for verifying that a recorded determination matches the entity's actual function in deployment. After recording a determination, governance can apply the relevant test to confirm consistency. Where the test reveals inconsistency between the recorded level and the entity's actual function, governance correction is required. The correction is a governance event recorded per A2.40; it is not an automatic update.

---

## 3. What makes purpose-defined level determination architecturally distinctive

Conventional AI architectures assign component types at design time based on technical function. This component is a model; that one is an API; this other is a database. Type is fixed and intrinsic — the component's classification is determined by what it is technically, not by what it is for in a particular deployment. If a component begins performing coordination functions it was not originally designed for, the mismatch is an engineering problem to be resolved by redesign or refactoring. Type does not change through a governed event; it changes (or fails to change) through technical modification.

CKS level determination differs in three respects. First, determination is purpose-based: the same underlying substrate artifact may be determined at cell level in one deployment context and at aspect level in another, depending on what it is for in each. The criteria apply to purpose-in-deployment, not to technical construction. Second, determination is substrate-resident: the authoritative record of what level an entity occupies lives in substrate as governed content with provenance, inspection rights, and modification authority. Third, determination is changeable through governance: when purpose changes substantially, the level assignment can change through a governed event rather than through technical redesign, with the change recorded and traceable per the full provenance architecture.

These three properties together make level assignment an ongoing governance responsibility rather than a one-time technical design decision. The architecture does not freeze level membership at construction; it makes level membership the subject of governed, inspectable, and modifiable substrate records that can evolve with the deployment's organizational reality.

---

## 4. The biological analog as conceptual scaffold

Biological cell fate determination provides a conceptual scaffold for understanding purpose-defined level determination. In developmental biology, cells are assigned specific functional roles — liver cell, neuron, muscle fiber — based on developmental signals received during differentiation. Fate is substrate-resident in that genetic expression patterns encode the committed state; those patterns can in principle be reprogrammed, as demonstrated by induced pluripotent stem cell research. The committed fate is not simply inferred from observed behavior at any given moment; it is encoded as a persistent developmental record that shapes how the cell responds to subsequent signals.

CKS level determination is the governed architectural analog. An entity's level is its functional commitment within the deployment. The determination record is the substrate-resident encoding of that commitment. Redetermination through governance is the architectural analog of reprogramming: not a routine occurrence, but an available governed capability with procedural requirements and recorded provenance.

The analog functions as conceptual scaffold only. Biological fate determination is neither governed nor inspectable in the CKS sense; developmental signals are not authored by identified humans with specified authority; and cell fate reprogramming in biology requires extensive technical intervention rather than a governance decision to update a substrate record. Where the analog is useful, it is in pointing toward the concept of purpose-committed functional identity encoded as a persistent record subject to revision under defined conditions. Where it diverges, the architectural substance — governed purpose-based level assignment with substrate-resident authoritative records — is what matters.

---

## 5. Inherited Paper 1 commitments

Purpose-defined level determination carries the following Paper 1 commitments forward directly.

**A1.08 (substrate as source of truth).** The determination record in substrate is the authoritative source of what level an entity occupies. Observed function that appears inconsistent with the record does not override the record; it triggers governance review. The substrate commitment to source-of-truth applies to determination records with the same force it applies to any other substrate content.

**A2.46 (authoritative content).** The level determination record is authoritative substrate content. It is not a comment, label, configuration flag, or informal annotation. It is governed content with provenance, subject to the same inspection and modification rights that apply to all substrate content under Paper 1's human-governance commitment.

**A2.04 (rule authoring).** Level determination criteria are authored governance content. The criteria are not inferred from training data or dynamically computed; they are authored specifications of how level assignment works in the deployment. Humans author the determination criteria; labor of applying them to produce a determination record may be performed by humans or by LLMs operating under human direction.

**A2.40 (provenance).** Every determination event — initial determination at birth and any subsequent redetermination — is recorded with the who, when, and under-what-authority fields that A2.40 specifies. The determination history is inspectable. The provenance chain for a level assignment extends from the initial birth determination through any redetermination events.

**A2.47 (authority distribution).** Who has authority to make level determinations, and at which level, is itself governance content. Cross-partner level determination requires cross-partner authority appropriate to that context. Single-deployment determination requires appropriate authority within that deployment's governance structure. Level determination is not a self-service operation; it is a governed act by identified humans with specified authority.

**A1.01 (governance).** Level determination is a governed act in the full CKS sense: governance is the authority to determine and to redetermine; labor of drafting the determination record is allocable to humans or LLMs operating under human direction. The authority-not-labor architecture applies to determination as it applies to all other governed substrate operations.

---

## 6. Operational implications

**Author at birth.** Every entity deployment must include a level determination as part of birth specification. Level declaration with a supporting purpose statement and determination governance record is a required birth artifact. A deployment that instantiates entities without level declarations has not completed birth governance for those entities and lacks the substrate-resident foundation that level-specific governance requires.

**Inspectable per A2.01.** Determination records are substrate-resident and therefore inspectable as substrate content. Audit processes can examine what level any entity has been determined to occupy, on what purpose basis, and by whose authority. The determination record's inspectability is not contingent on additional disclosure workflow; it follows from the substrate-as-source-of-truth commitment that makes all substrate content inspectable by humans with appropriate access.

**Monitor purpose changes.** As deployments evolve, entities may develop purposes different from those recorded at birth. Governance responsibility includes monitoring whether actual operational purpose has shifted substantially enough to warrant level redetermination review. This monitoring is a human governance responsibility. The architecture does not automate purpose-change detection; it provides the governance infrastructure to act when humans determine that a purpose change has occurred.

**Redetermination is a governance event.** A level determination change is not a configuration update or a technical patch. It is a governance event: humans decide whether the purpose change warrants redetermination, the decision is recorded per A2.40, and labor implements the record update in substrate. The governance structure mirrors birth governance — governance decides, labor implements — ensuring that level changes carry the same provenance and authority accountability as level assignments at birth.

**Cross-partner contexts per A2.47.** In cross-partner deployments, level determination for entities that participate in multiple organizational substrates requires authority appropriate to that cross-partner governance context. The determination record specifies the authority under which determination was made, which matters for cross-partner accountability.

**Enables level-specific governance per B1.20.** Knowing an entity's level determines which governance commitments apply to it. A cell-determined entity carries the full set of Paper 1 cell-level architectural commitments. An aspect-determined entity carries aspect-level governance expectations including purpose-statement requirements. A Self-determined entity carries Self-level governance obligations over the aspects it integrates. Without substrate-resident determination records, level-specific governance cannot be systematically and consistently applied across a deployment's entities.

---

## 7. Limits

Five limits bound the formalization and prevent misreadings.

**Determination is not subjective.** The criteria are architectural: cell performs a specific informational task, aspect coordinates cells for a purpose, Self integrates aspects into a coherent whole. These are not preference statements or flexible interpretations that different human governors may resolve differently based on judgment. They are the committed determination criteria derived from Paper 2's three-level structure. The purpose-based framing means the criteria apply to the entity's function-in-deployment rather than to its technical construction; the criteria themselves are not malleable.

**Determination changes are not automatic.** When an entity's observed function begins diverging from its recorded level, the determination does not update automatically. The record remains authoritative until governance decides to change it per the redetermination process. An entity executing coordination functions while recorded as a cell is not an aspect by observation; it is a cell whose governance record may need review. The distinction matters: automatic updates based on observed behavior would remove the substrate-as-source-of-truth guarantee.

**The determination record is authoritative over observed behavior.** This follows directly from A1.08. The substrate is the source of truth. Observed behavior provides input to governance review; it does not override the substrate record. A system that infers level changes from behavioral observation without a governance decision is not operating under CKS level determination in the sense this note formalizes.

**Criteria are mutually exclusive within a deployment context.** An entity is determined at one level per deployment context. The same underlying substrate artifact may be determined at cell level in deployment A and aspect level in deployment B, depending on what it is for in each. But within a single deployment context, an entity occupies one level. The relational structure from B2.84 — that the same artifact can participate in multiple structural arrangements — is a cross-deployment property; within a deployment, each entity has one determination record specifying its level.

**Determination does not change the three-level structure.** Determination assigns entities to the existing three levels. It does not add levels, modify the definitions of the three levels, or alter the governance relationships among levels. The three-level structure — cell for specific informational tasks, aspect for coordinating cells for a purpose, Self for integrating aspects — is the fixed architectural commitment Paper 2 defends. Purpose-defined level determination is the governed process of populating that fixed structure with specific entities in specific deployment contexts.

---

## 8. Operational test

An entity is purpose-determined in the CKS sense if and only if: its level assignment (cell, aspect, or Self) is recorded as substrate-resident authoritative content based on a purpose statement meeting the level-specific determination criteria; the determination event is recorded with identified humans and specified authority per A2.40 and A2.47; the record is inspectable and modifiable under the same human-governance architecture that governs all substrate content per A1.08; and any change to the determination is made through a governed event rather than automatically inferred from observed function.

---

## 9. Why naming this as standalone matters; position in the B1.17 decomposition

Naming purpose-defined level determination as a standalone derivation establishes the prior-art claim for the full operational specification of purpose-based level assignment: level-specific criteria, substrate-resident records, governed changes, distinguishability-test verification, and the determination-record-as-authoritative-over-observed-behavior commitment. This claim is not fully visible from B1.17 alone, which establishes the relational and purpose-defined framing at the foundational level, nor from B2.84 alone, which establishes the integrating frame for the decomposition. B2.85 makes the determination mechanism explicit — the operational process that gives "purpose-defined" its architectural meaning and that distinguishes CKS level assignment from any classification scheme that lacks substrate-residency, provenance, and governed-change properties.

B2.85 is the second of five notes decomposing B1.17. B2.84 established the integrating frame, placing the B1.17 relational-and-purpose-defined commitment in the context of the full relational roles architecture. B2.86 will formalize the same-entity-at-multiple-levels property — how relational level membership produces the multi-level participation pattern B2.84 introduced. B2.87 will address how relational roles interact with the evolution mechanisms Paper 2 develops, and B2.88 will close the B1.17 decomposition with relational roles verification. After B2.88, Phase B2 continues with the B1.18 content-domain decomposition beginning at B2.89.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Purpose-Defined Level Determination: How Purpose Assigns an Entity to a Structural Level in the Coordination Knowledge Substrate.* May 12, 2026. ORCID: 0009-0004-8065-3235.
