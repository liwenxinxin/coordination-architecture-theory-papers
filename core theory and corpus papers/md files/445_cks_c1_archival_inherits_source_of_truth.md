# Entity Archival State Inherits Paper 1's Source-of-Truth Addressability

**Working title:** C1.16 — Paper 2 Archival of Dead Entities Inherits Paper 1 Substrate-as-Source-of-Truth: Preserved Addressability of Complete Governance Records as Entity-Scope Extension of Historical State Preservation, Enabling Reactivatability and Compliance Tracing

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series position:** Derivation Note C1.16 — Series C Cross-Derivation (#445)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its contribution is to establish, in explicit form, that Paper 2's archival state for retired entities directly inherits Paper 1's source-of-truth addressability commitment, and to identify what is genuinely new in Paper 2's treatment.

---

## Abstract

When a CKS entity dies by lineage supersession, it transitions to archival state: its complete governance record is preserved in the substrate and remains addressable by the same provenance references that identified it during active life. This note establishes that archival state is not an independent invention. It directly inherits Paper 1's substrate-as-source-of-truth commitment (A1.08), specifically the properties that historical decisions remain authoritative in the substrate and that every piece of substrate content is addressable by its provenance metadata. What is genuinely new in Paper 2 is threefold: archival state is formalized as a named entity lifecycle state distinct from active state; the specific record types preserved are enumerated; and archival addressability is the prerequisite for the reactivatability property established in C1.15. This note is the complement to C1.15, which covered the death event; C1.16 covers the archival state that results.

---

## 1. The inheritance edge this note establishes

**C1.16 states:** Paper 2's archival of dead entities (lineage supersession type) inherits Paper 1's substrate-as-source-of-truth commitment, specifically the addressability and historical-state-authority properties. The archival state is an entity-scope extension of what Paper 1 already committed to for substrate content generally.

This note is the sixteenth in Series C of the CKS derivation note series. Series C formalizes inheritance edges between Paper 2 and Paper 1 — each note establishing that a given Paper 2 commitment extends a specific Paper 1 commitment rather than originating independently. C1.15 (note #444) covered the death event as governed retirement; this note covers the archival state that results from lineage-supersession death and demonstrates that its properties are continuous with Paper 1's source-of-truth architecture.

---

## 2. The two Paper 1 commitments involved

Two Paper 1 commitments jointly constitute the inherited foundation.

**A1.08 — Substrate as source of truth.** Paper 1 commits to the substrate as the authoritative answer to coordination questions — what was decided, by whom, under what authority, with what rationale, and where contradictions remain unresolved. Critically, this commitment does not scope to present-tense state only. Paper 1's source-of-truth claim encompasses *historical* decisions: any decision the system has recorded about coordination work remains answerable from substrate content. A substrate that held only current state and discarded the record of past decisions would not satisfy Paper 1's commitment. The historical dimension is built in.

**A1.07 + A1.08 combined — Addressability.** Paper 1 commits to determinism and addressability as substrate properties: every piece of substrate content carries writer, timestamp, rationale, and provenance metadata. This metadata is not decorative — it is the mechanism by which substrate content is retrieved. The path-retraceability commitment (A1.07) depends on addressability: tracing the full chain of any authoritative state back to its provenance requires that each node in the chain is directly retrievable by its identifier. Addressability is the operational form of source-of-truth: content is authoritative only if it can be found.

Together, these two commitments establish that Paper 1 substrates hold historical state as authoritative content, and that this content is directly retrievable by provenance references. C1.16 asks whether Paper 2's archival state for dead entities is continuous with these commitments. The answer is yes, on both dimensions.

---

## 3. What archival state preserves — the inherited properties

When a CKS entity dies by lineage supersession, four properties of its substrate content are preserved, each directly continuous with a Paper 1 commitment.

**Historical state remains authoritative.** The archived entity's governance record is not demoted to advisory or reference-only status. It is authoritative for the entity's historical governance state — the complete record of what the entity was, what decisions were made about it, and what its lifecycle history was. An observer reading the archived record reads the same authoritative content that existed during the entity's active life; nothing has been revised, softened, or marked as approximate. This is a direct expression of Paper 1's commitment that historical decisions remain authoritative in the substrate. Paper 1 did not restrict its source-of-truth claim to active content; Paper 2's archival state gives that general commitment an entity-specific form.

**Addressability is preserved.** The provenance references that identified the entity during active life continue to resolve the entity after death. The entity's identifier does not change on archival; the archival flag is a status attribute of the same addressable record, not a migration to a different location or a different identifier. An observer who holds a reference to the entity obtained before death can use that same reference after death and reach the same content, now flagged as archived. This is a direct inheritance of Paper 1's addressability commitment: content does not become unaddressable because it is historical. Historical content that cannot be addressed is not, in Paper 1's terms, held in the substrate — it is simply lost.

**No degradation.** The archived record preserves the full content of the entity's governance record. It is not summarized, compressed, or reduced to a tombstone marker. Paper 1's source-of-truth requirement is that the substrate answers coordination questions from its own content — this requires that the content be complete, not approximated. A substrate that held only a summary of historical decisions would fail Paper 1's test: summaries cannot answer the original coordination questions that the full record answers. Archival state inherits this completeness requirement directly.

**Accessible for compliance demonstration.** The archived record can be retrieved for governance compliance demonstration at any time — not only during the entity's active life. This is a consequence of addressability and historical-state authority combined: if the record is addressable and authoritative, it is accessible whenever the governance question that requires it arises, regardless of when in the system's lifecycle that question is asked. Paper 1's path-retraceability commitment (A1.07) established that the full historical chain is accessible; archival addressability extends this to entity-scope records.

---

## 4. What is genuinely new in Paper 2

Paper 2 does not merely apply Paper 1's existing commitments to entity records. Three additions are genuinely new.

**Archival state as a named entity lifecycle state.** Paper 1 held substrate content that was historical — past decisions retained in the substrate as authoritative content. But Paper 1 did not formalize a named, recognized lifecycle state for substrate content that is no longer active. Paper 2 formalizes ARCHIVAL STATE as a distinct lifecycle state for entities, explicitly part of the entity lifecycle alongside active state. The entity lifecycle is: birth → active → archived (for lineage supersession) or birth → active → deleted (for functional obsolescence). This is not a parameterization of one lifecycle; it is a two-branch structure where the archival branch explicitly names and governs the resulting state. Paper 1's historical content was simply historical; Paper 2's archival state is a governance-recognized status with specific properties, specific access rules, and specific relationships to other lifecycle operations.

**Enumeration of specific record types preserved.** Paper 1's source-of-truth commitment applied to substrate content generally — decisions, provenance, authority assignments, active contradictions. It did not name a specific set of entity-scope governance record types that constitute the complete governance record of an individual entity. Paper 2 specifies what is preserved in archival state: the birth record, the lineage chain, the DNA version history, the Action layer records, and the death record itself. This enumeration does not override Paper 1's general commitment; it gives it a specific operational form at entity scope. An implementer who has Paper 1 alone knows that historical decisions are authoritative in the substrate; Paper 2 tells that implementer which record types constitute the entity-complete historical record that archival state must preserve.

**Archival addressability as prerequisite for reactivatability.** Paper 2 commits to reactivatability for lineage-supersession deaths: an archived entity can, under governance, be brought back to active state. This commitment was established in C1.15 as the property that distinguishes CKS from systems where retirement is irrevocable. But reactivatability is only architecturally available if the archived record can be located and read. The reactivation process — whether through point-in-time restoration, snapshot mount, or capability reactivation — must begin by addressing the archived entity's governance record and reading its content. Archival addressability is the prerequisite for reactivatability: you can only reactivate what you can address. This means C1.16 is a silent dependency of C1.15: the property C1.15 claims (reactivatability) presupposes the property C1.16 establishes (archival addressability). Both notes are stronger for making this dependency explicit.

---

## 5. C1.15 and C1.16 as complementary notes — event and resulting state

C1.15 and C1.16 are complementary; neither subsumes the other.

C1.15 established that the death event in Paper 2 inherits Paper 1's governed retirement pattern. The focus of C1.15 is the event itself: death as a governed lifecycle operation, the governance authority over the retirement decision, and the reactivatability commitment that distinguishes lineage supersession from functional obsolescence. C1.15 covers what happens — the governed transition from active to retired.

C1.16 establishes that the archival state resulting from lineage-supersession death inherits Paper 1's source-of-truth addressability. The focus is the state that results from the event: what properties does the archived entity's record have, and which of those properties are continuous with Paper 1's commitments. C1.16 covers what persists — the archival state and its properties.

The relationship between the two notes is also asymmetric in one direction. C1.15's reactivatability claim depends on archival addressability being maintained — C1.16 is a prerequisite for the reactivatability property C1.15 asserts. The dependency does not run the other way: archival addressability does not depend on reactivatability. C1.16 would be a valid property even in a system that committed to archival without reactivation; it is the reactivatability commitment of C1.15 that requires C1.16 to hold.

---

## 6. Operational test

**Test for C1.16:** For any entity that has undergone lineage-supersession death in a CKS-compliant system, select the entity's provenance identifier as it existed during the entity's active life. Attempt to retrieve the entity's complete governance record — birth record, lineage chain, DNA version history, Action layer records, and death record — using that same identifier, making no additional queries or transformations beyond the identifier and the substrate access mechanism used for active entities. The test passes if and only if:

(a) The identifier resolves without modification;
(b) The full record is returned, not a summary or tombstone;
(c) The record is marked as archived but is otherwise identical in content to what it held during the entity's final active state;
(d) The record's provenance metadata (writer attributions, timestamps, rule references) is intact and readable.

A system where archived entity identifiers fail to resolve, where archived records return only a deletion marker or summary, or where archived records require a different access mechanism than active records, fails the C1.16 test and does not implement Paper 1's addressability inheritance at entity scope.

The governance version of the same test: present the archived record to a human auditor and ask whether the full governance history of the entity — every decision made about it, every version of its DNA, every action it recorded, and the circumstances of its retirement — is answerable from the record alone, without access to any other source. If the auditor cannot answer any governance question from the record alone, the record is not complete and the archival commitment is not satisfied.

---

## 7. Prior-art significance

C1.16 forecloses three categories of adversarial claim.

**Claim (a): Preserving dead entities' governance records as addressable substrate content is novel relative to Paper 1's source-of-truth commitment.** This claim fails. Paper 1 committed to historical decisions as authoritative substrate content and to all substrate content as addressable by provenance references. Preserving an archived entity's governance record as addressable substrate content is a direct application of Paper 1's existing commitment at entity scope, not an independent invention.

**Claim (b): Archival state as a formal entity lifecycle state is novel relative to Paper 1's historical state preservation.** This claim partially fails and partially succeeds. What is not novel is the preservation of historical content as authoritative and addressable — Paper 1 committed to that. What is genuinely new in Paper 2 is the formalization of archival state as a named, recognized lifecycle state with enumerated properties, specific record types, and distinct access rules. The line between what is inherited and what is new is explicit in §3 and §4 of this note.

**Claim (c): The specific record types preserved in archival state are novel architectural objects.** This claim fails as to novelty against Paper 1. The individual record types — birth records, DNA version histories, Action layer records — are themselves Paper 2 additions whose own inheritance is documented in C1.09, C1.11, and adjacent notes. The enumeration of these types as the specific content of an entity's archival record is a Paper 2 specification decision, but it does not create novel substrate content; it names the content whose preservation is already required by Paper 1's source-of-truth commitment applied at entity scope.

---

## 8. Summary

Paper 2's archival state for lineage-supersession deaths is not an independent commitment. It is the entity-scope application of two Paper 1 commitments that were already in place: that historical decisions remain authoritative substrate content (A1.08), and that all substrate content is addressable by its provenance references (A1.07 + A1.08). The archived entity's governance record is authoritative, complete, undegraded, and reachable by the same provenance references that identified the entity in active life. What Paper 2 adds is the formalization of archival state as a named lifecycle state, the enumeration of the specific record types it preserves, and the recognition that archival addressability is a prerequisite for the reactivatability property established in C1.15. C1.15 covers the death event; C1.16 covers the archival state that results. Together, they establish the complete picture of lineage-supersession death in CKS: a governed retirement producing an addressable, authoritative, reactivatable record.

---

*Derivation Note C1.16 in the CKS Cross-Derivation Series (#445). Part of a defensive-publication series establishing inheritance edges between CKS Paper 2 (Li, April 2026) and CKS Paper 1 (Li, April 2026). License: CC BY 4.0.*
