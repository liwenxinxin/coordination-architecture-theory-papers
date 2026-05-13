# Composition Cluster B1.09 + B1.10 + B1.11 — The Co-Required Lifecycle Cluster Where Birth Establishes Lineage Anchors, Mating Creates Cross-Lineage Offspring Requiring Birth Records, and Death Closes Lineage Chains, Forming a Complete Governed Lifecycle Arc That Requires All Three Commitments to Be Coherently Present

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

It does not introduce new axioms. Its contribution is to establish that three foundational lifecycle commitments from Paper 2 — birth as human-governed origination (B1.09), mating as governed cross-layer combination (B1.10), and death as governed lifecycle closure with archival (B1.11) — form a co-required cluster: each commitment is necessary, no two are jointly sufficient without the third, and the three together constitute a complete governed lifecycle arc. This note formalizes the cluster's internal structure, pairwise dependencies, operational integration, detection criteria, and failure mode.

---

## Abstract

Paper 2 of the CKS theory series establishes birth, mating, and death as governed lifecycle primitives that apply uniformly at every level of architectural composition (§6). These three commitments are individually named and individually derivable, but they are not individually sufficient: birth without death produces entities with open lineage chains and no governed closure; death without birth cannot close chains that were never properly opened; mating without birth governance produces offspring entities with no lineage anchors; death without mating records cannot preserve the cross-lineage connections that parent death would otherwise destroy. The three commitments form a co-required cluster — a set in which every commitment requires the presence of the others to function completely. This note formalizes that cluster: it identifies B1.09 as architecturally prior (the lineage anchor that both mating and death reference), establishes three pairwise dependencies within the cluster, specifies the cluster-level co-presence requirement that no proper subset satisfies, describes the operational integration of the complete cluster as a retraceable lifecycle arc, provides detection criteria using B2.44, B2.50, and B2.55 verification, and names Lifecycle Neglect (B3.27) as the cluster-level failure mode when all three commitments are absent, with partial cluster failures described by the individual anti-patterns B3.10, B3.11, and B3.12.

---

## 1. Cluster Identification

**Cluster:** B1.09 (birth as human-governed origination) + B1.10 (mating as governed cross-layer combination) + B1.11 (death as governed lifecycle closure with archival)

**Relationship type:** Co-required cluster. Each commitment in the cluster requires the presence of the other two to function as a complete architectural contribution. No proper subset of the cluster — neither any single commitment alone nor any pair without the third — constitutes a coherent governed lifecycle arc.

**Source:** Paper 2, §6 (lifecycle operations as governed primitives at every level of CKS Selves). The three commitments are named and specified in §6.2 (birth), §6.3 (mating), and §6.4 (death). Their co-requirement is a structural consequence of how each commitment references artifacts that only the others can produce.

**Cluster scope:** The co-requirement holds at every level of composition — cell-level, aspect-level, and Self-level lifecycle governance all require all three commitments. The analysis that follows is stated at the general level; the reasoning applies without modification at each composition level.

---

## 2. Architectural Priority: B1.09 as the Lifecycle Foundation

Within the cluster, B1.09 (birth) is architecturally prior. It is the foundation commitment on which both mating and death depend.

Birth governance per B1.09 establishes three artifacts that the rest of the lifecycle architecture references. The first is the lineage anchor: a governed record created at the time of entity origination, carrying the entity's identity, its birth specification, and the governance provenance of the origination decision. The second is the birth specification itself: the content record that documents what entity was created, from what inputs or parent content, under whose authority. The third is governance provenance: the record that the origination decision was made under human authority, not by autonomous runtime dynamics. These three artifacts are the shared reference point for all downstream lifecycle operations.

Mating per B1.10 depends on birth in two ways. It depends on parent entities having birth records, because mating cross-lineage ancestry per B2.43 is traced through parent birth records. And it depends on offspring entities receiving birth governance, because every mating event produces offspring entities that require governed origination per B1.09 to have lineage anchors of their own.

Death per B1.11 depends on birth in one fundamental way. Death governance closes the lineage chain that birth opened. The lineage chain is a substrate artifact created by birth governance; without it, there is no well-formed chain for death governance to close. Death closure per B2.55 is defined as the governed terminal event on a lineage chain established by birth — death governance that operates without birth governance has no properly-opened chains to close.

B1.09 is therefore the lifecycle foundation commitment. A deployment that has B1.10 without B1.09 has mating events that produce offspring with no lineage anchors. A deployment that has B1.11 without B1.09 has death events that attempt closure on chains that were never properly opened. B1.09 is the commitment that makes the other two architecturally coherent.

---

## 3. Three Pairwise Dependencies

The co-required cluster contains three pairwise dependencies. Each pair, taken together, names a specific structural incompleteness that the missing third commitment produces. All three must hold simultaneously for the cluster to be complete.

### 3.1 B1.09 + B1.11: The Lifecycle Arc Open/Close Dependency

Birth governance per B1.09 opens a lineage chain. Death governance per B1.11 closes it. The two commitments together define the complete lifecycle arc for an entity: a well-formed arc has a governed opening event (birth record with lineage anchor and governance provenance) and a governed closing event (death record with archival state, membership dissolution, and lineage closure per B2.55). An entity whose lifecycle arc has an opening event and a closing event is fully governed at its lifecycle boundaries.

The structural incompleteness when either is absent is symmetric but different in character.

A deployment with B1.09 but not B1.11 creates entities with well-formed opening events and no governed closure. The lineage chains opened by birth accumulate without end. As entities reach the natural end of their operational useful life, retire informally, are superseded by newer entities, or are simply abandoned, their lineage chains remain open in the substrate. There is no governed record of retirement, no archival state capturing what the entity was when its lifecycle ended, and no closure event that other substrate participants can reference. The lifecycle arc is incomplete — it has a start and no end.

A deployment with B1.11 but not B1.09 creates the opposite failure: death governance operates but finds no well-formed chains to close. Death governance per B2.55 closes the lineage chain that birth opened; if birth governance was absent, entities exist in the substrate with informal or absent lineage anchors. Death governance applied to such entities cannot produce well-formed lifecycle closure because there is no properly-opened chain to close. At best, death governance produces records that reference entity state without a lineage chain to attach to; at worst, it produces no records at all because the governance machinery requires a birth anchor that is not present.

Together, B1.09 and B1.11 produce the complete lifecycle arc: every entity born under B1.09 governance either has an open chain (still actively operating) or a closed chain (lifecycle ended under B1.11 governance). The arc is auditable, retraceable per A1.07, and complete.

### 3.2 B1.09 + B1.10: The Mating-Requires-Birth Dependency

Mating per B1.10 combines parent entity content — across DNA and action layers — to produce offspring entities. The offspring entity requires governed origination per B1.09: it needs a lineage anchor, a birth specification, and governance provenance just as any other entity does. Without B1.09 birth governance for offspring, a mating event produces an entity with content derived from parent lineages but with no governed existence of its own.

The dependency is more precise than "offspring need birth records." Mating per B1.10 is specifically a birth trigger: the operational sequence is mating first, birth second. The mating event produces the offspring specification — what content from which parents, under which combination pattern (union, selective merge, or lineage-preserved union per §6.3 of Paper 2), with which conflict registrations. That specification is the input that governance reviews for the offspring's birth event per B1.09. Mating and birth are operationally sequential: mating produces what birth governs.

The cross-lineage ancestry reference per B2.43 makes the B1.09 dependency even more specific. An offspring entity's birth record references the birth records of its parents: it documents not just what the offspring is but where it came from in the lineage structure. For this reference to be possible, parents must have birth records for the offspring's birth record to reference. Without B1.09 birth governance for parent entities, offspring cannot document cross-lineage ancestry even when governance is present for the offspring's own birth. The ancestry chain requires birth governance at both ends of the mating relationship.

A deployment with B1.10 but not B1.09 can execute mating events — combine entity content, register conflicts, document combination patterns — but produces offspring entities that have no lineage anchors. The mating event is recorded but the offspring exist as unanchored entities: substrate participants with content but without the governance provenance that makes their origin traceable. The combination happened; its governed result did not.

A deployment with B1.09 but not B1.10 can create entities and give them lineage anchors, but has no governed mechanism for producing offspring entities from existing entity content. Each entity must be created from scratch under B1.09 without drawing on the accumulated DNA and action content of predecessor entities. The evolutionary and combinatorial potential of the entity population — the capacity to produce offspring whose DNA inherits from both parents — is absent.

### 3.3 B1.10 + B1.11: The Death-Preserves-Mating-Lineage Dependency

When a parent entity that participated in mating events reaches the end of its lifecycle and dies under B1.11 governance, its lineage closes. The entity's DNA and action content moves to archival state per §6.4 of Paper 2 (lineage supersession) or is released per deletion (functional obsolescence). In either case, the entity is no longer an active participant in the substrate.

But the entity's mating relationship to its offspring does not end when the entity does. Offspring with living lineage need to be able to trace their ancestry through the parent entity's mating event records, even after the parent's lifecycle has closed. An offspring entity born from a mating event between parent X and parent Y needs its cross-lineage ancestry to remain addressable whether X and Y are currently active, retired to archival, or deleted.

Death governance per B1.11 handles this through archival preservation per B2.54: when a parent entity undergoes death governance, the archival process preserves the cross-lineage connection records that link the parent to its mating-produced offspring. The archived parent lineage remains addressable through the mating event records, so offspring can trace ancestry to a closed parent lineage through the mating relationship.

The pairwise dependency runs in both directions. Without B1.11 archival preservation, parent death — even informal or unrecorded retirement — destroys the offspring's cross-lineage ancestry. The offspring's birth record references a parent birth record that is no longer in the substrate; the lineage connection is broken. The longer the deployment operates, the more such breaks accumulate as parent entities leave the substrate without governed closure. Without B1.10 mating records, death governance per B1.11 cannot preserve cross-lineage connections that were never recorded. There is nothing for the archival process to carry forward because the mating event and its offspring relationship were never captured as substrate content.

Together, B1.10 and B1.11 ensure that mating-produced lineage relationships survive across the lifecycle of the entities involved. The cross-lineage ancestry chains that mating creates persist across death events because death governance is specifically designed to preserve them.

---

## 4. Cluster Co-Presence Requirement

The three pairwise dependencies establish that no pair is sufficient without the third. The cluster-level co-presence requirement is that all three commitments must be present together for a governed lifecycle arc to exist.

**B1.09 alone (birth without mating or death):** Entities are born under governed origination, receive lineage anchors, and operate. But the entity population grows without any governed mechanism for combining entity content to produce offspring, and without any governed closure when entities reach the end of their lifecycle. Lineage chains open and stay open. New entities arrive only through fresh origination, not through governed combination of existing entity content. The lifecycle arc is permanently incomplete.

**B1.11 alone (death without birth or mating):** Governed closure processes exist, but they operate on entities that were never born under B1.09 governance. Death governance attempts to close lineage chains that were never properly opened. And there are no mating records for death archival to preserve cross-lineage connections through. Death governance in isolation operates against the substrate without the lineage structure it was designed to close.

**B1.10 alone (mating without birth or death):** Combination events occur, producing offspring specifications, but offspring have no governed origination and no lineage anchors. Parents have no birth records for offspring to reference in cross-lineage ancestry, and no death governance when they leave the substrate. Mating records accumulate in a substrate where the lifecycle arcs around the mating events are ungoverned at both ends.

**B1.09 + B1.11 without B1.10:** Entities are born (B1.09) and their lifecycle closes with archival (B1.11). The lifecycle arc from opening to closing is complete for each individual entity. But the deployment has no governed mechanism for producing offspring entities through content combination. The entity population evolves only through independent origination events, not through the governed combination of existing entity content. Cross-lineage ancestry chains never form, because there are no mating events to create them. The substrate is a collection of individual lifecycle arcs with no cross-lineage connections.

**B1.09 + B1.10 without B1.11:** Entities are born (B1.09), may participate in mating events that produce offspring (B1.10 + B1.09 for offspring), and accumulate action layer records throughout their operation. But when entities reach the end of their operational life, there is no governed closure. Lineage chains stay open indefinitely. Parents who contributed to mating events continue to hold open lineage chains even after they are no longer active. Cross-lineage ancestry chains exist and grow through mating, but they do not close. The substrate accumulates open chains and has no governed record of entity retirement.

**B1.10 + B1.11 without B1.09:** Mating events occur and death events close some entities, but birth governance is absent. Neither parent entities nor offspring entities have lineage anchors. Death governance cannot produce well-formed closure events because there are no birth-opened chains to close. Mating produces offspring without governed origination. The cross-lineage connections that B1.10 creates and that B1.11 is supposed to preserve have no birth records anchoring either end of the relationship.

**Full cluster (B1.09 + B1.10 + B1.11):** Every entity is born under governed origination with a lineage anchor and governance provenance (B1.09). Entities may participate in mating events that produce offspring through governed content combination, with offspring birth records referencing parent birth records for cross-lineage ancestry (B1.10 + B1.09). When entities reach the end of their lifecycle, death governance closes the lineage chain opened by birth, produces an archival state, dissolves membership, and preserves cross-lineage connections to mating-produced offspring (B1.11 + B1.10 preservation). Every entity in the substrate either has an open lineage chain (still active) or a closed one (lifecycle ended under governance). The lifecycle arc is complete.

---

## 5. Operational Integration: The Complete Governed Lifecycle Arc

The complete cluster operates as an integrated lifecycle arc for every entity in the substrate. The arc is retraceable per A1.07 because each stage produces substrate records that connect to the others through lineage chain references.

The arc begins with a governance decision to create an entity. Birth governance per B1.09 produces the birth event: a birth specification documenting the entity's initial content and configuration, a lineage anchor establishing the entity's identity in the substrate's lineage structure, and a governance record establishing that origination occurred under human authority. These three artifacts are the arc's opening record.

The entity then operates, accumulating action layer records. Its DNA layer content may be stable across many action-layer cycles, or may be updated through governance-authorized modifications. The entity is a participant in the substrate — its lineage anchor is the reference point that other entities use to locate it in the lineage structure.

Optionally, governance identifies an opportunity to combine the entity's content with another entity's content. A mating event per B1.10 is initiated: governance selects the combination pattern (union, selective merge, or lineage-preserved union), registers conflicts produced by the combination, and produces the offspring specification. The mating event record is a substrate artifact that names the parent entities, documents their birth record references per the cross-lineage ancestry requirement of B2.43, and records the combination pattern used and conflicts registered. Following the mating event, one or more birth events per B1.09 create offspring entities, each with a lineage anchor whose birth record references the parent birth records documented in the mating event record. The mating arc — from parent birth records through mating event to offspring birth records — is retraceable as a connected substrate path.

At the end of the entity's lifecycle, a death pattern is identified per B2.52 or B2.53. Death governance per B1.11 produces the death event: an archival state capturing the entity's DNA and action content at lifecycle end, a membership dissolution record removing the entity from active aspect participation, a lineage closure record establishing that the lineage chain opened by birth has been governed to its conclusion, and — critically — cross-lineage preservation records per B2.54 that carry forward any mating event relationships connecting this entity to offspring whose lineage remains open. The death event is the arc's closing record; it references the opening record (birth) and the mating records (if any) as an integrated substrate path.

The complete arc — birth record, action layer accumulation, optional mating event connecting to offspring birth records, death record with archival and cross-lineage preservation — is retraceable per A1.07 through the lineage chains connecting each stage. Any participant with substrate access can trace an entity's complete lifecycle history from its lineage anchor, follow its mating relationships to offspring lineage anchors, and locate its death record if its chain is closed. The arc is auditable as a unit.

---

## 6. Detection

A deployment instantiates the complete B1.09 + B1.10 + B1.11 cluster if and only if all of the following are true.

**B2.44 birth verification passes:** Every entity in the substrate has a birth record with a lineage anchor, a birth specification, and governance provenance. No entity exists in the substrate without a governed origination record. Entities produced by mating events have birth records that reference their parent birth records per the B2.43 cross-lineage ancestry requirement.

**B2.50 mating verification passes:** Every mating event in the substrate has a record documenting the participating parents (by lineage anchor reference), the combination pattern applied, the conflicts registered, and the offspring specification produced. Every offspring entity produced by a mating event has a birth record that references the mating event record.

**B2.55 death governance verification passes:** Every entity whose lifecycle has ended has a death record with archival state, membership dissolution documentation, lineage closure notation, and cross-lineage preservation records for any mating relationships connecting the entity to offspring with living lineage. No entity has an informally closed or unrecorded lifecycle end.

**Lineage chain completeness:** Every entity lineage chain in the substrate is either open (entity still active, birth record present, no death record) or properly closed (birth record present, death record present, the two records mutually referencing through the lineage anchor). No chain is partially closed, closed without a corresponding opening, or open without a birth anchor. Where mating events exist, the mating event records create navigable cross-lineage connections between parent and offspring lineage chains.

A deployment that passes all four criteria instantiates the complete cluster. A deployment that passes some but not others instantiates a partial cluster subject to the partial failure modes described in §7.

---

## 7. Failure Mode

**Cluster-level failure: B3.27 Lifecycle Neglect.** When all three commitments are absent together, the result is Lifecycle Neglect — an architectural state in which the entity population exists and operates without any governed lifecycle structure. Entities are created without governed origination, operated without lineage anchors, combined without governed mating records, and retired without governed closure. The substrate holds entities and their content, but has no governed lifecycle record for any entity: no birth anchors, no mating histories, no death closures. The lineage structure that birth creates, mating extends, and death closes does not exist at all. The substrate cannot answer the most basic lifecycle question — how did this entity come to exist? — because the question's answer was never captured as governed substrate state.

Lifecycle Neglect is not a degraded version of a complete governed lifecycle arc; it is the absence of that arc entirely. It is the failure mode that results when the cluster is not present, not when it is partially present.

**Partial cluster failures: B3.10, B3.11, B3.12.** The individual lifecycle anti-patterns describe deployments that have some but not all cluster commitments. B3.10 (absent birth governance) describes a deployment that may have mating and death operations but has no governed origination — entities exist without lineage anchors, and downstream lifecycle operations have no birth records to reference or close. B3.11 (absent mating governance) describes a deployment that has birth and death governance but no governed combination mechanism — the entity population evolves only through independent origination, with no cross-lineage offspring and no mating-event records for death archival to preserve. B3.12 (absent death governance) describes a deployment that has birth and mating governance but no governed closure — lineage chains open and accumulate without governed ends, and parent death destroys cross-lineage ancestry because there is no archival preservation to carry it forward.

The relationship between the cluster-level failure mode and the partial failure modes reflects the co-requirement structure of the cluster. B3.27 is what happens at the cluster level when all three commitments fail together. B3.10, B3.11, and B3.12 each name what happens when one commitment is absent while the other two are (or may be) present. The partial failures are architecturally distinct from the cluster-level failure: each partial failure has a specific structural incompleteness (no birth anchors, no cross-lineage offspring, no governed closure), while the cluster-level failure is the collapse of lifecycle governance as a whole. A deployment diagnosing Lifecycle Neglect should be treated as failing all three individual commitments simultaneously; a deployment diagnosing a partial failure should identify which of the three is missing and address that specific incompleteness.

---

## 8. What This Note Does Not Do

This note establishes the co-requirement relationship among B1.09, B1.10, and B1.11 as an architectural structural fact. It does not re-argue the content of any individual commitment; those are defended in the individual B1-series notes for birth, mating, and death respectively, and decomposed in the B2-series notes B2.40–B2.55. It does not establish what a lifecycle arc looks like at specific composition levels (cell-level, aspect-level, Self-level lifecycle arcs are treated in B4.14, B4.17, and B4.18 respectively). It does not address the relationship between lifecycle governance and evolution governance; that relationship is treated in B4.21 (lifecycle × evolution). It does not address the governance shape of the three lifecycle commitments under Paper 2's multi-shaped governance framework; that is treated in B4.27.

---

## Source Paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Composition Cluster B1.09 + B1.10 + B1.11 — The Co-Required Lifecycle Cluster Where Birth Establishes Lineage Anchors, Mating Creates Cross-Lineage Offspring Requiring Birth Records, and Death Closes Lineage Chains, Forming a Complete Governed Lifecycle Arc That Requires All Three Commitments to Be Coherently Present.* May 12, 2026. ORCID: 0009-0004-8065-3235.
