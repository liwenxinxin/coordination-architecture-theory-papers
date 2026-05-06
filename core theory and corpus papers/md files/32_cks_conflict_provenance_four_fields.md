# Four Metadata Fields for First-Class Conflicts: The Provenance Requirements That Make Contradictions Architecturally Addressable in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 02 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the four metadata fields that contradicting substrate content must carry to function as first-class objects in the architectural sense — writer attribution, timestamp, rationale (where applicable), and explicit relationship to the contradicting content — so that downstream work has a precise specification of what conflict provenance the substrate must register for the conflict-as-first-class commitment to hold.

## Abstract

The CKS pattern's conflict-preservation commitment (Claim 3 of the source paper) requires that contradictions in substrate content be promoted to first-class addressable objects. Sibling decomposition notes formalize substrate-level preservation, cell-level resolution under orchestration rules, and the coupling between the two levels. This note formalizes the fourth piece of the decomposition: the metadata that contradicting content must carry to be first-class architecturally rather than merely co-resident in the substrate. Four fields are jointly required — writer attribution, timestamp, rationale where applicable, and explicit relationship to the contradicting content. The first three are the conflict-specific specialization of the broader substrate-content provenance commitment treated separately under the path-retraceability decomposition; the fourth — explicit relationship — is what specifically distinguishes a contradiction-as-object from accumulated inconsistency. The note states each field's content, gives the joint-necessity argument (each absent field downgrades a contradiction from first-class to substrate-content-with-partial-provenance), distinguishes the four fields from four adjacent metadata patterns, names seven failure modes, and provides an operational test for whether a substrate's conflict provenance is CKS-coherent.

## 1. Why the four-field specification needs to be formalized as standalone

The parent foundational note on conflict as first-class object commits to two-level handling: substrate-level preservation of contradictions, and cell-level resolution under orchestration rules. Sibling decomposition notes formalize substrate-level preservation alone, cell-level resolution alone, and the coupling between them. The decomposition leaves one piece untreated as standalone: the metadata that contradicting content must carry for the first-class commitment to hold. Without that metadata stated, "first-class" is a term of art possessed by any substrate that carries contradictions in any form. With the metadata stated, "first-class" names a precise architectural property, distinct both from substrate content with partial provenance and from accumulated inconsistency.

The motivating distinction is between contradictions-as-state and contradictions-as-objects. A substrate may carry contradicting content as state — two pieces that together are inconsistent — and still fail the first-class commitment, because the contradictions are accumulated rather than registered as architectural objects. The four fields are what convert accumulation into registration: with all four present, the substrate carries contradictions navigable from either contradicting piece; with any one missing, the contradiction is inconsistency a reader must reconstruct.

A second motivation is the relationship to path retraceability. The retraceable path of any decision that resolved a contradiction must include enough metadata about the contradiction itself to reconstruct what was contradicted, by whom, when, with what rationale, and how the two pieces relate. The four fields are what the retraceable path requires for the contradiction node within the path; without them, retraceability fails specifically at the contradiction.

A third motivation is the strategic posture of this derivation series. Patentable derivations focused on conflict-handling metadata — schemas for contradiction tracking, conflict-tagging systems, contradiction-relationship graphs — are more defensibly contested when the four-field specification is publicly formalized as standalone, because any "conflict metadata innovation" can be evaluated against the specific four-field structure CKS commits to.

## 2. The four metadata fields, defined precisely

In the CKS pattern, a piece of contradicting substrate content is **first-class** if and only if the substrate carries the following four metadata fields for it.

**Field 1 — Writer attribution.** Each piece of contradicting content carries the identity of the writer that produced it. The writer may be a human exercising the modify or override right under the human-governed commitment, an LLM mediator operating within a cell under orchestration rules per the AI-as-substrate-mediator commitment, or a stable cell automating writes under rules. The field identifies the agent: humans by their identity within the substrate's authority structure; cells by their identity. (For cell writes, the rule under which the cell wrote is the natural companion of the cell identity in the broader substrate-content provenance treated under the path-retraceability decomposition; the cell identity itself is what Field 1 here requires.) The attribution must be sufficient to support governance actions on the writer — challenge, audit, or override of subsequent content of the same kind.

**Field 2 — Timestamp.** Each piece of contradicting content carries the time at which it was written into the substrate. Timestamps enable reconstructing when contradictions emerged, which subsequent cells encountered them in what order, and how long they persisted before resolution. The architectural commitment is to the timestamp existing as substrate metadata, not to any specific format or precision; deployments may use clock time, logical clocks, or substrate-internal sequence numbers, provided the metadata is comparable across contradicting content within the same substrate.

**Field 3 — Rationale, where applicable.** When the writer produced the content under conditions where rationale is architecturally required — the orchestration rule that authorized the cell write specifies that rationale must be captured; the human exercising modify or override authority chose to record rationale; the substrate's schema makes rationale mandatory for content of this type — the rationale is recorded as substrate metadata for the content. The architectural commitment is conditional: rationale is required when schema or orchestration rules specify it, and is permitted but not architecturally required otherwise. The conditional nature distinguishes Field 3 from the unconditionally required Fields 1, 2, and 4. What the architecture does not support is missing rationale where the schema or rules said it would be present.

**Field 4 — Explicit relationship to contradicting content.** Each piece of contradicting content carries an explicit, addressable reference to the other content it contradicts. This is the field specifically distinctive to first-class conflicts. It has three sub-properties.

(a) *Identifier reference.* The field includes an identifier referencing the other contradicting substrate content (or contents — a single piece of content may contradict multiple others). The identifier is addressable: a reader holding one piece can navigate to the other through the substrate's normal addressability mechanisms.

(b) *Characterization of the contradiction's nature.* The field includes a characterization of the dimension on which the content contradicts — the decision, the rationale, the authority, the interpretation — at minimum sufficient for a downstream reader to understand why the two pieces are contradicting rather than merely related.

(c) *Bidirectional symmetry.* The relationship is symmetric: if content A references content B as contradicting, content B carries a corresponding reference to content A. This is what makes the relationship architecturally first-class — the contradiction is a substrate object connecting two pieces of substrate content, not a property of one piece pointing to another.

The relationship field's full architectural inheritance — including OIDA's signed contradiction edges as cited prior art (§5.2 and §6.2 of the source paper) — is treated in the next decomposition note. What this note specifies is that the field is required and that its three sub-properties are jointly required.

## 3. Why all four fields are jointly necessary

A piece of contradicting content with three of the four fields is not architecturally a first-class conflict object; it is substrate content with partial provenance, and the kind of partial provenance determines the kind of architectural failure.

**Without writer attribution.** A contradiction exists as substrate content but cannot be traced to its source. Humans exercising the inspect right see contradicting content but cannot identify which agents produced which side, which prevents downstream governance (the modify and override rights have no addressable target), prevents accountability review of which cells or humans produced contradicting outputs, and breaks path retraceability — the path through the contradiction cannot be reconstructed because its writer node is missing. The agent producing the contradiction is not architecturally addressable.

**Without timestamp.** A contradiction exists but cannot be temporally located. Subsequent cells and humans cannot determine which contradicting content was written first, which was a later response or revision, or how long the contradiction has persisted unresolved. This breaks retraceability for any decision depending on temporal ordering, prevents identification of long-standing unresolved contradictions, and prevents reconstruction of the substrate's coordination history. The temporal location of the contradiction is not architecturally addressable.

**Without rationale, where rules required it.** A contradiction is traceable to its writer and time but cannot be understood in the writer's terms when rationale was architecturally required. Humans inspecting the contradiction see that two writers produced contradicting content but cannot evaluate why each writer produced what they did. Cells operating under rules that need to consider rationale in choosing among contradicting content cannot do so. The reasoning behind contradicting positions is not architecturally addressable when the architecture said it would be.

**Without relationship.** A contradiction exists as two pieces of substrate content with full attribution, time, and rationale — but the substrate carries no architectural connection between them. Subsequent cells and humans see two pieces of content that may or may not be contradicting, depending on how the reader interprets them; the contradiction is implicit, not registered. The substrate has accumulated inconsistency but has not registered a contradiction-as-object. This is the failure mode that most directly converts first-class conflicts into accumulated noise.

The four fields are therefore jointly necessary. A substrate that carries three of the four for contradicting content has substrate content with partial provenance, not first-class conflicts in the architectural sense.

## 4. What the four-field specification is NOT

Four adjacent metadata patterns are commonly conflated with the four-field specification. Each is real and reasonable in some other architecture; conflating any with the conflict-provenance specification produces a misreading of what CKS requires.

**Not generic audit logs.** Audit logs record events external to the substrate — who accessed what, when, from where — for after-the-fact review. The four-field specification names metadata embedded in substrate content itself: properties of the contradicting content that humans inspecting the substrate see directly. Audit logs may complement the four fields but cannot substitute for them.

**Not version history.** Version history records changes to substrate content over time. The four fields are not a history of the substrate's state; they are properties of contradicting content that exists in the substrate now. A substrate where the fields exist only in version history fails, because the contradiction-as-object has to be navigable from the substrate's current content, not reconstructible from its history.

**Not tagging schemes.** Tags can carry metadata about contradictions ("in dispute," "contradicted") but tags themselves are not the four fields. The fields are specifically writer (who), time (when), rationale (why), and relationship (what other content). A tag indicating contradiction status without these four fields does not satisfy the specification.

**Not comment threads.** Comments can record rationale informally and may include references to other content, but comments are typically not part of the substrate's authoritative state — they are commentary on it. The four fields must be part of the substrate's authoritative metadata for contradicting content, not commentary attached to it.

## 5. How the four fields produce architectural properties downstream

The four fields together support three architectural properties that depend on conflict provenance for their content.

**Auditability of resolution decisions.** The two-level coupling's auditability property requires that resolution decisions be evaluable against the contradictions they addressed. The four fields make that evaluation architecturally complete: the resolution decision references its antecedent contradiction (the relationship field permits this from the contradiction side; the broader substrate-content provenance supplies the antecedent reference from the resolution side), and the contradiction's writer, time, and rationale are themselves visible to the auditor.

**Non-finality of resolution.** The architectural commitment that resolution decisions are not final — that subsequent cells and humans can revisit contradictions under different rules or different judgments — requires that revisiting be operationally meaningful. The four fields are what makes revisiting meaningful: a later reader can evaluate the contradicting positions on their merits and arrive at a different resolution than earlier cells did. Without the four fields, revisiting is operationally impossible because the necessary context is missing.

**Path retraceability for paths through contradictions.** Decisions depending on contradicting content require traceable paths through the contradictions. The four fields are the contradiction-side metadata that makes those paths complete; the rule reference and antecedent reference of the broader substrate-content provenance are the resolution-side metadata that completes the path.

## 6. Failure modes that violate the four-field specification

Each failure mode below names a way an implementation can fail one or more fields, with the architectural failure that follows.

(a) **Anonymous writes.** Substrate content is committed without writer attribution, through deployment configurations that allow anonymous commits or implementations that lose writer identity in the commit chain. Field 1 fails; contradictions cannot be governance-evaluated by author.

(b) **Untimestamped writes.** Substrate content is committed without timestamps — through implementations that do not record commit time, or normalization processes that strip timestamp metadata. Field 2 fails; contradictions cannot be temporally located.

(c) **Missing rationale where rules required it.** Orchestration rules specify that rationale must be captured for certain content types, but cells write the content without rationale (LLM mediators omitting rationale fields when the rule's prompt did not enforce them; humans bypassing rationale fields in interfaces). Field 3 fails for content where it was required; the architectural commitment is violated even though the field is conditional.

(d) **Implicit contradictions without explicit relationships.** Two pieces of substrate content contradict each other by their content, but no explicit relationship metadata connects them. A reader must infer the contradiction by comparing the content; the substrate carries no first-class object marking it. Field 4 fails; the contradiction is accumulated inconsistency, not a first-class object.

(e) **Asymmetric relationship metadata.** Content A references content B as contradicting, but content B carries no corresponding reference. Readers approaching from content B do not see the contradiction. Field 4's symmetry sub-property fails; the contradiction is partially first-class but not architecturally complete.

(f) **Relationship without characterization.** Content A references content B as contradicting, but no metadata characterizes the contradiction's dimension. Readers know the two pieces are linked but cannot evaluate what specifically is contradicting. Field 4's characterization sub-property fails; downstream resolution under rules cannot operate on the contradiction's substantive content.

(g) **Generic provenance treated as conflict provenance.** The substrate carries generic substrate-content provenance for all content but does not specialize for contradictions — contradicting content has writer and timestamp like any other content but no relationship field marking the contradiction. The substrate has provenance but not conflict provenance specifically; the first-class commitment fails because contradictions are not architecturally distinguished from non-contradicting content.

## 7. Operational test

A substrate's conflict provenance satisfies the four-field specification if and only if all of the following are true at all times during the substrate's existence.

1. Each piece of contradicting substrate content carries writer attribution sufficient to support governance actions on the writer.
2. Each piece carries timestamp metadata sufficient to support temporal reconstruction of contradiction emergence.
3. Each piece carries rationale metadata when orchestration rules or substrate schema require rationale for content of that type.
4. Each piece carries explicit relationship metadata that includes an addressable identifier of the contradicting content, a characterization of the contradiction's dimension, and bidirectional symmetry between the contradicting pieces.
5. The four fields are part of the substrate's authoritative state for contradicting content — readable through normal substrate inspection, not bypassed in audit logs, version history, tagging schemes, or comment threads.

A substrate that fails any of (1)–(5) does not satisfy the four-field conflict-provenance specification, even if it carries rich metadata of other kinds for contradictions.

## 8. Why naming the four-field specification as standalone matters

Implementations under pressure to keep substrates lightweight or to minimize metadata overhead consistently drift toward partial provenance: writers but no rationale, timestamps but no relationships, relationships without characterization. Each shortcut is reasonable in some other architectural context; in CKS, each one downgrades contradictions from first-class objects to accumulated content.

Implementations that drift toward partial provenance produce systems where the conflict-as-first-class commitment looks satisfied — the substrate preserves contradictions, cells resolve under rules — but operationally fails when downstream consumers try to use the contradictions architecturally. Audits cannot evaluate resolutions; subsequent cells cannot revisit contradictions meaningfully; humans cannot exercise override authority on the substantive merits of contradicting positions. Each downstream failure traces to a missing field.

Naming the four-field specification as a standalone architectural commitment gives downstream implementers a precise specification of what conflict provenance must carry. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "first-class conflict" in the sense formalized here. Subsequent work that uses the term differently is using a different commitment, and the difference should be named. The next decomposition note formalizes OIDA's signed contradiction edges as cited prior art for the relationship field, completing the conflict-as-first-class decomposition.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Four Metadata Fields for First-Class Conflicts: The Provenance Requirements That Make Contradictions Architecturally Addressable in the Coordination Knowledge Substrate Pattern.* 02 May 2026. ORCID: 0009-0004-8065-3235.
