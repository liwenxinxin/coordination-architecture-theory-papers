# Disambiguating "Provenance" and "Record" Across the Trilogy

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026), and "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026).

## Abstract

The terms "provenance," "governance record," "FAI-origin provenance," and "authorization chain" appear across all three papers of the Coordination Knowledge Substrate (CKS) trilogy with meanings that are consistent in structure but expand in scope at each paper. This note disambiguates each term at every paper scope and identifies the two Paper 3 extensions — FAI-origin provenance at the inter-Self perimeter (Dimensions 5 and 6 of the configurable governance dimensions) and the four-link cross-organizational authorization chain — that are specific to inter-Self governance and do not introduce new concepts. The core disambiguation: provenance throughout the trilogy names the same six-field governance accountability metadata; Paper 3 extends its scope to cross-organizational governance while preserving the six-field structure at every link of the chain. "Record" throughout the trilogy names substrate content carrying provenance; Paper 3 formalizes seventeen standard categories for the governance records that FAI events produce. Neither extension is a new concept; both are the operationalization of Paper 1's provenance and record commitments at larger governance scope.

---

## 1. Concept identification

Four terms require disambiguation across the trilogy:

- **"Provenance"** — used in all three papers; structurally consistent throughout; scope expands at each paper
- **"Governance record"** — used in all three papers; a general concept at Papers 1 and 2; a formalized taxonomy at Paper 3
- **"FAI-origin provenance"** — a Paper 3 term for the provenance properties specific to the inter-Self perimeter
- **"Authorization chain"** — the sequence of governance authorizations that provenance documents; extended from single-authority (Papers 1–2) to multi-authority (Paper 3)

The status of these terms across the trilogy is as follows. Provenance is established in Paper 1, extended in Paper 2 to entity-lifecycle chains, and extended in Paper 3 to cross-organizational scope. The record concept is established in Paper 1 as any substrate content carrying provenance, extended in Paper 2 to named record types for entity-lifecycle events, and formalized in Paper 3 into seventeen standard categories for FAI governance records. The two Paper 3 terms — FAI-origin provenance and the four-link chain — are Paper 3's specifications of what provenance and authorization chain mean when multiple governance authorities participate in a shared substrate event. None of these terms introduces a new architectural concept; each applies the Paper 1 foundation at a larger governance scope.

---

## 2. Provenance and records at Paper 1 scope

Paper 1 (§A1.07) establishes provenance through six mandatory metadata fields that every substrate content item carries:

1. **Author** — who authored the content
2. **Timestamp** — when it was authored
3. **Authorization** — what governance authorization applies
4. **Derivation** — what source content it derives from
5. **Version** — its version within the governance sequence
6. **History** — what came before it in the chain

These six fields are the atomic provenance unit. They are what makes a piece of substrate content traceable — not through a log external to the substrate, but through the substrate itself. Path retraceability holds when these fields are present on every substrate content item; it fails when any field is absent. The accountability plan (the substrate schema and orchestration rules together) specifies that the fields must be present; the accountability trace (substrate content as it accumulates) is the record of their having been captured.

At Paper 1 scope, any substrate content item carrying these six fields is a governance record. The six fields are what distinguishes a traceable record from an anonymous piece of content. This is the foundational definition of "record" in the trilogy: a governance record is substrate content with provenance.

The authorization chain at Paper 1 scope spans a single governance authority. The chain documents the sequence of authorizations that brought a piece of content into existence: what governance decision authorized it, under what rule, at what time, by whom. The chain is readable by traversing the substrate; each link in the chain is itself a substrate content item carrying the six fields.

---

## 3. Provenance and records at Paper 2 scope

Paper 2 extends both concepts to entity-lifecycle scope within a single Self. Every entity in the three-tier hierarchy — cell, aspect, Self — has a provenance chain from birth through all directed selection events, matings, and death. The six fields from Paper 1 apply at every record in this chain. Every directed selection record, every mating record, and every lifecycle record carries the six fields; the chain is traceable by substrate traversal at every link.

Named record types at Paper 2 scope include: directed selection records (documenting governance decisions to alter an entity's composition), mating records (documenting the governance authorization of mating events), and lifecycle records (documenting birth, maturity, and death events in the entity's governance history). Each is a Paper 1 governance record — substrate content with the six provenance fields — instantiated at the specific event types Paper 2 introduces.

The authorization chain within a single Self spans tiers: a cell-level governance decision leading to aspect-level governance review leading to Self-level governance approval, as appropriate to the event. The chain is still single-authority (one Self's governance structure), but the tier structure adds depth. The six fields apply at each tier-level record in the chain. Cross-lineage references in lineage-preserved-union mating maintain bifurcated provenance trails across the participating entities; both trails carry the six fields throughout.

"Record" at Paper 2 scope is still any substrate content with the six provenance fields. Paper 2 extends the concept by naming the specific record types that entity-lifecycle governance produces, not by redefining what makes a piece of content a record.

---

## 4. Provenance and records at Paper 3 scope

Paper 3 extends both concepts to inter-Self scope. Two extensions are specific to Paper 3 and do not appear at Papers 1 or 2 scope.

**Extension 1: FAI-origin provenance (Dimensions 5 and 6 of the configurable governance dimensions).** When one Self contributes aspects to the shared substrate in a Full Aspect Integration event, the contributed content carries provenance from the contributing Self's home substrate. Two questions arise at the inter-Self perimeter that do not arise within a single Self's governance scope:

*Dimension 5 — Provenance carry-over depth:* How deeply does the contributing Self's governance history carry into the shared substrate? What provenance from home substrates crosses the inter-Self perimeter with the contributed content? This is governance-configurable: the depth of provenance carry-over is a dimension of the FAI event's governance configuration, authored as substrate content under joint authority of the participating Selves' governance structures.

*Dimension 6 — Provenance preservation on internalization:* When content from the shared substrate is absorbed into a home substrate after the FAI event's dissolution, is FAI-origin provenance maintained in the receiving Self's home substrate? Whether the cross-organizational governance history persists through absorption is also governance-configurable.

Both dimensions build on Paper 1's six fields by specifying what happens to those fields at organizational boundaries. The six fields are not replaced or supplemented with additional fields; what is specific to Paper 3 is the question of how deeply they travel across the inter-Self perimeter and whether they survive absorption into home substrates. The term "FAI-origin provenance" names this class of provenance questions — provenance properties that are specifically interrogated at the inter-Self perimeter — and does not name a different provenance structure or a different set of fields.

**Extension 2: The four-link cross-organizational authorization chain.** Paper 1's single-authority authorization chain extends to four links when multiple governance authorities participate in a FAI event:

*Link 1 — Home governance authorization of contribution:* The contributing Self's governance authorizes the contribution of aspects to the shared substrate.

*Link 2 — Joint FAI event authorization:* The participating Selves' joint governance authorizes the FAI event itself.

*Link 3 — Shared-substrate governance decisions:* Governance decisions made within the shared substrate during the event's active period.

*Link 4 — Home governance absorption authorization:* The receiving Self's governance authorizes the absorption of evolution outputs post-dissolution.

Paper 1's six provenance fields apply at each link. The four-link chain is four applications of the six-field structure at the authority transitions that cross-organizational governance introduces. The chain extends the single-authority provenance chain to multi-authority context without replacing its structure; each link is a governance record in the Paper 1 sense — substrate content with the six fields.

**Paper 3 governance records: the seventeen-category standard taxonomy.** Paper 3 (§D2.18) formalizes seventeen standard governance record categories for FAI events. At Paper 3 scope, "governance record" in FAI event context specifically means one of these seventeen categories, or an additional category explicitly recognized within the taxonomy. This is a more specific usage than the general record concept at Papers 1 and 2.

The seventeen categories are the operational specification of what "record" means at FAI event scope — the enumeration of what the general concept produces when applied to the full set of governance decisions and events that a FAI event involves. This formalization does not introduce a new concept; it applies the Paper 1 definition (substrate content with the six provenance fields) to the complete set of event types that inter-Self governance generates and names each category. Each of the seventeen categories is a substrate content item carrying Paper 1's six provenance fields.

---

## 5. The disambiguation

The precise cross-paper relationships are as follows.

**Provenance** names the same commitment throughout the trilogy: the six metadata fields that establish the governance accountability chain for any substrate content item. What differs across papers is the scope of the chain, not its structure. At Paper 1 scope, the chain is single-authority and operates within one governance perimeter. At Paper 2 scope, the chain spans entity-lifecycle events and tiers within a single Self's governance structure. At Paper 3 scope, the chain spans multiple governance authorities across the inter-Self perimeter. The six-field structure applies at every scope; provenance at any scope is the same provenance, evaluated against the governance authority that applies at that scope.

**FAI-origin provenance** is not a different provenance concept; it is Paper 3's name for the provenance properties that are specifically interrogated at the inter-Self perimeter. Dimension 5 specifies what happens to the six fields when content crosses organizational boundaries under governance configuration; Dimension 6 specifies what happens to the six fields when content is absorbed post-dissolution under governance configuration. Both questions presuppose the six fields and extend their specification to the boundary conditions that inter-Self governance introduces.

**Governance record** (Papers 1 and 2) names any substrate content item carrying the six provenance fields. The concept is general: any piece of governed substrate content is a governance record. **Governance record** (Paper 3, §D2.18) names one of the seventeen standard categories for FAI governance records. This is the specific usage: at Paper 3 scope in FAI event context, "governance record" means one of those categories. The general usage does not disappear at Paper 3 scope; the specific usage applies when discussing what records a FAI event produces. Both usages name substrate content with the six fields; they differ in how specifically the content type is named.

**Authorization chain** (Papers 1 and 2) is the single-authority chain the six fields document for any substrate content item, traceable by substrate traversal. **Authorization chain** (Paper 3) is the four-link cross-organizational chain — four applications of the six-field structure at the authority transitions that cross-organizational governance requires. The four-link chain is not a new concept; it is the single-authority chain applied four times at the authority transitions that multi-governance-authority participation introduces, with each link being a governance record in the Paper 1 sense.

The risk of misreading runs in both directions. Reading Paper 3's four-link chain as a novel provenance structure independent of Paper 1's six fields mistakes what is an extension for an invention. Reading Paper 3's seventeen-category taxonomy as a new record concept independent of Papers 1 and 2's general definition mistakes what is an operational specification for a new definition. Both misreadings break the trilogy's inheritance structure: every Paper 3 provenance and record commitment inherits from Paper 1 without redefense and extends at inter-Self scope without introducing new foundations.

---

## 6. Prior-art claim

This note establishes as public prior art that:

1. The six provenance metadata fields established in Paper 1 (§A1.07) constitute the atomic governance accountability unit that applies at every scope in the trilogy — intra-cell, entity-lifecycle, and cross-organizational. Paper 3's four-link authorization chain is not a new provenance structure; it is four applications of the six-field structure at the authority transitions that multi-governance-authority participation introduces. Any claim that Paper 3's cross-organizational provenance chain introduces a provenance concept not present in Paper 1 is contrary to this record.

2. FAI-origin provenance (Dimensions 5 and 6 of the governance-configurable dimensions) names the provenance questions specific to the inter-Self perimeter — provenance carry-over depth and provenance preservation on internalization — and builds on Paper 1's six fields by specifying their behavior at organizational boundaries under governance configuration. These two dimensions are extensions of the six-field structure, not additions to it.

3. The seventeen-category governance record taxonomy formalized at Paper 3 (§D2.18) is the operational specification of the general record concept established in Papers 1 and 2. The formalization enumerates what the general concept produces at FAI event scope; it does not introduce a new definition of "record." Each of the seventeen categories is substrate content carrying Paper 1's six provenance fields.

4. The general record concept — substrate content with the six provenance fields — is the unifying definition across all three papers. Paper 2's named record types (directed selection records, mating records, lifecycle records) and Paper 3's seventeen-category FAI taxonomy are both applications of this definition at their respective governance scopes, not departures from it.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Disambiguating "Provenance" and "Record" Across the Trilogy.* May 15, 2026. ORCID: 0009-0004-8065-3235.
