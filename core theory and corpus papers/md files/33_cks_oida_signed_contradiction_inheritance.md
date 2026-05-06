# Signed Contradiction Edges as Cited Prior Art: How CKS Inherits from OIDA on the Relationship Field of First-Class Conflicts

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 2 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one inheritance edge — the edge between CKS and OIDA on the architectural commitment of contradiction relationships — as a standalone derivation, articulating what CKS draws from cited prior art on this specific axis, what CKS adds beyond it, and what this note does not claim from that prior art.

## Abstract

The CKS pattern's conflict-as-first-class commitment, decomposed across A2.13–A2.17, requires that contradictions in substrate content carry four provenance fields: writer, timestamp, rationale where applicable, and explicit relationship to the contradicting content. The fourth field — the relationship to contradicting content, with three sub-properties (identifier reference, characterization of the contradiction's nature, bidirectional symmetry) — was specified in A2.16 as required, with a forward reference to this note for its prior-art grounding. The source paper at §5.2 (with secondary treatments at §8.2 and §9.4) cites OIDA's *signed contradiction edges* as the strongest 2024–2026 architectural precedent for treating contradictions as substrate-level addressable relationships. This note formalizes the inheritance edge: what OIDA's contribution carries as cited prior art, what CKS inherits from that contribution into the relationship field's content, what CKS adds beyond inheritance (the multi-human governance overlay specific to the relationship field, as a specialization of CKS's already-distinct three-axis posture per A1.09), and what this note does not claim from OIDA's specific implementation territory. The note then states the load-bearing connections from the inheritance to other CKS commitments, gives an operational test that distinguishes pattern-inheritance from CKS-instantiation, and closes the conflict-as-first-class decomposition by tying the five notes (A2.13–A2.17) to their joint architectural function.

## 1. Why the inheritance edge needs to be formalized as standalone

The parent foundational note A1.03 commits to conflicts as first-class objects in the substrate, with two-level handling (substrate-level preservation; cell-level resolution under orchestration rules) as the operational structure that makes the commitment tractable. The four prior decomposition notes formalize, in turn, the substrate-level half alone (A2.13), the cell-level half alone (A2.14), the two-level coupling (A2.15), and the four-field provenance specification that distinguishes first-class contradictions from mere accumulation of inconsistent content (A2.16). A2.16's fourth required field — explicit relationship to the contradicting content, with three sub-properties (identifier reference, characterization of the contradiction's nature, bidirectional symmetry) — ends with a forward reference: the architectural content of the relationship field is grounded in cited prior art treated separately. This note delivers on that forward reference.

Three motivations make the standalone treatment worth a separate note rather than a paragraph appended to A2.16.

The first is the strategic prior-art posture. The contradictions-as-relationships architectural pattern — treating a contradiction as an addressable substrate-content object connecting contradicting pieces, rather than as inconsistency a reader infers from reading the pieces — is established prior art. OIDA documents the pattern in 2026 with signed contradiction edges between Knowledge Objects, and the source paper at §5.2 cites that contribution explicitly. Without an inheritance treatment that names what is and is not inherited, downstream readers may assume the relationship field is a CKS innovation; with the treatment, the prior art is publicly visible and CKS's relationship-field-level contribution — the multi-human governance overlay applied to the inherited pattern — is identifiable as the specific axis on which CKS extends rather than originates.

The second is the architectural completeness of A2.16, which specified the relationship field as required and named its three sub-properties briefly with a forward reference. This note completes the specification by stating where that architectural content comes from, what it inherits, and what it adds.

The third is the relationship to A1.09. A1.09 formalizes the broader CKS-OIDA inheritance as a two-axis structure: CKS differs from OIDA on three architectural axes at the core-theory scope (governance, role/authority, AI-as-substrate-mediator), and the multi-human axis is the scope along which the resulting three-axis-distinct posture extends. The full inheritance treatment lives in A1.09; this note specializes for one specific manifestation — the relationship field of first-class conflicts — as a standalone derivation in the same sequence as A2.13–A2.16.

## 2. What OIDA's signed contradiction edges contribute, as cited prior art

The source paper at §5.2 cites OIDA — "Retrieval Is Not Enough: Why Organizational AI Needs Epistemic Structure" (2026 preprint) — as the strongest 2024–2026 precedent for treating contradictions as first-class substrate state. The specific OIDA contribution the source paper attributes is the *signed contradiction edge*: a structural realization of conflict-as-object with identity, where the edge has its own schema presence, points to both conflicting Knowledge Objects, and persists in the substrate rather than existing as transient state consumed in a single inference pass. Section 8.2 of the source paper restates the family-level positioning, and §9.4 carries the architectural-difference framing at the extension scope.

The contribution operates at four architectural levels that this note will refer to throughout, treating OIDA respectfully as external prior art whose specific implementation territory the source paper cites without entering.

**Identification.** Contradictions are identifiable as substrate-content objects, not as patterns inferred from reading contradicting pieces. A reader navigating the substrate sees contradiction objects directly, addressable in their own right, rather than encountering two pieces of content that imply a contradiction.

**Addressability.** Contradiction objects can be referenced, queried, and operated on as units within the substrate's operations. Subsequent substrate content can name a specific contradiction; cells executing over the substrate can address the contradiction itself rather than reasoning about general inconsistency among substrate content.

**Bidirectional connection.** The contradiction object connects the contradicting pieces from both sides. A reader approaching from either contradicting piece sees the contradiction object linking to the other piece. The relationship is architecturally symmetric, not directional from one piece to the other.

**Characterization.** The contradiction object carries metadata describing the contradiction's nature — what kind of contradiction it is, on what dimension the pieces are contradicting — not just that the two pieces are related. The "signed" in "signed contradiction edges" carries architectural content in OIDA: the contradiction itself is annotated, not merely identified.

The note treats OIDA as the cited source for these architectural properties, not as a system whose specific data structures, signing semantics, edge formalisms, or maintenance mechanisms CKS adopts. CKS adopts the architectural pattern these properties characterize; OIDA's specific design choices remain OIDA's authorship territory, addressed separately in section 5.

## 3. What CKS inherits from this contribution

CKS inherits, into the relationship field of first-class conflicts (A2.16's fourth required field), the architectural commitment that the four properties of section 2 are present in the relationship the substrate carries between contradicting pieces. The inheritance maps as follows.

**The relationship field is required.** The meta-commitment that the relationship is substrate content at all — that a substrate cannot satisfy CKS's first-class-conflicts commitment without carrying the relationship as substrate content — traces directly to OIDA's identification property. Contradictions cannot be inferred from reading contradicting pieces; the substrate must carry the relationship as substrate state in its own right. A2.16 specifies the field as required jointly with the other three provenance fields; the inheritance grounds why this field specifically is required and not merely allowed.

**The relationship field is addressable.** A2.16's identifier-reference sub-property — that the relationship field names which other piece or pieces of substrate content the content contradicts — traces to OIDA's addressability. The relationship is an architectural object that can be referenced and operated on by name, not a property a reader has to reconstruct by reading both contradicting pieces.

**The relationship field is bidirectional.** A2.16's bidirectional-symmetry sub-property — that approaching from either contradicting piece, a reader can navigate to the relationship and from there to the other piece — traces to OIDA's bidirectional connection. The architectural symmetry is what makes the relationship a real edge between the pieces rather than a one-directional annotation on one of them.

**The relationship field carries characterization.** A2.16's characterization sub-property — that the relationship field describes the dimension on which the pieces are contradicting — traces to OIDA's characterization. The contradiction itself carries metadata about its nature, not merely a pointer to the contradicting piece.

The four inheritance points map onto A2.16's three sub-properties (identifier reference, characterization, bidirectional symmetry) plus the meta-commitment that the relationship is required at all. Together they constitute the architectural content of A2.16's fourth provenance field that this note grounds in cited prior art rather than introducing as new commitment.

## 4. What CKS adds beyond inheritance

CKS extends the inherited relationship field along the multi-human governance axis A1.09 formalizes for the broader CKS-OIDA inheritance. The extension at the relationship-field level manifests in three specific additions.

**The relationship field is human-governed substrate content.** The architectural pattern OIDA contributes is silent on whether the contradiction relationship is subject to authority, modification, and override by humans operating over the substrate. CKS's inherited relationship field is human-governed substrate content per A1.01: the three rights (inspect, modify, override) apply at all times. Humans with appropriate access can inspect the relationship, modify its characterization, override the architectural existence of the contradiction itself when authority is exercised, and do so directly over the substrate rather than through any LLM or runtime middleware layer. The relationship field is not an immutable structural property; it is governable substrate content.

**The relationship field carries provenance per A2.16's four-field specification.** The architectural pattern OIDA contributes is silent on whether the contradiction relationship has a writer, a timestamp, a rationale, and (recursively) a relationship to the substrate content it sits between. CKS specifies that the relationship is itself a substrate write performed by some agent (human or cell, the latter operating under named orchestration rules) at some time, possibly under some rule, with the same four provenance fields A2.16 requires. The relationship is not a static derived property; it is authored substrate content with its own authorship history.

**The relationship field operates within the cell-level resolution mechanism per A2.14.** The architectural pattern OIDA contributes is silent on how cells executing over substrate content engage with contradiction relationships under human-authored rules. CKS specifies that A2.14's cell-level resolution mechanism operates on the addressable contradiction the relationship field exposes, with the resolution decision itself becoming substrate content that references the relationship through the four-field provenance specification. The relationship field is the addressable handle the cell-level resolution mechanism reaches for; the resolution is recorded substrate content, not a mutation of either contradicting piece.

A reconciliation point with A1.09 is worth stating because the easy misreading of these three additions is "OIDA plus governance overlay," and the source paper at §9.4 preempts that reading at the broader scope. The multi-human governance overlay at the relationship-field level is not a layer added atop an OIDA base; it is the relationship-field-scope specialization of CKS's already-distinct three-axis architectural posture, as A1.09 formalizes that posture. CKS is architecturally different from OIDA on the multi-human axis, not OIDA plus multi-human; the relationship-field-level extension is one specific manifestation of that broader architectural difference, not a counterexample to it.

## 5. What this note does NOT claim from OIDA

The bounded shape of the inheritance is what makes the prior-art posture defensible. The note does not claim, and the inheritance edge does not extend to, the following five categories.

**Not OIDA's specific data structures.** OIDA's signed contradiction edges are realized in specific data structures the OIDA preprint specifies. CKS's inherited relationship field can be realized in any data structure that supports the four architectural properties of section 2 — identification, addressability, bidirectional connection, characterization — and is human-governed and provenance-bearing per section 4. The specific edge formalisms, schema details, and storage representations OIDA chooses are OIDA's implementation territory; a CKS deployment can match them, diverge from them, or use entirely different structures, and the inheritance edge is unchanged.

**Not OIDA's specific signing semantics.** The "signed" in "signed contradiction edges" carries architectural content in OIDA — the specific way the contradiction's polarity, direction, or kind is encoded — that this note does not reproduce. What CKS inherits is the architectural property of characterization: that the contradiction object carries metadata describing the contradiction's nature. The specific signing mechanism by which OIDA realizes characterization is OIDA's design choice; CKS commits to characterization as an architectural property without committing to any particular realization of it.

**Not OIDA's broader architectural commitments beyond the cited contribution.** OIDA is a complete architecture with its own commitments to typed Knowledge Objects, epistemic class, importance scores with class-specific decay, the deterministic Knowledge Gravity Engine as a maintenance mechanism, and QUESTION-as-modeled-ignorance as a first-class primitive. The source paper at §5.2 names several of these commitments in establishing OIDA's architectural identity, but cites specifically the signed-contradiction-edge contribution as the architectural prior art for Claim 3's relationship requirement. CKS does not inherit the rest of OIDA's architecture comprehensively; it inherits the specific contribution to the contradictions-as-relationships pattern.

**Not the multi-human governance overlay as something OIDA committed to.** The source paper at §5.2 and §9.4 is explicit that OIDA does not specify a governance architecture; OIDA specifies a maintenance architecture (the Knowledge Gravity Engine) which operates over the substrate deterministically without locating authority over substrate content in any particular actor. The multi-human governance overlay this note treats is CKS's own architectural posture, not an extension of an OIDA commitment. The inheritance edge from OIDA is to the architectural pattern; the governance overlay applied to the inherited pattern is CKS's contribution, distinguishable from inheritance as such.

**Not continuous engagement with OIDA's development.** OIDA is cited prior art at the time the source paper was written, with the signed contradiction edge contribution attributed to the 2026 preprint. Subsequent OIDA developments — refinements to the schema, additional primitives, alternative formalisms, peer-reviewed publication — are not within the inheritance edge formalized here. The inheritance is to the cited contribution as documented in the source paper's references; later OIDA work, if any, neither extends nor contracts this note's inheritance treatment.

The five non-claims, taken together, draw the boundary of the inheritance edge: CKS inherits an architectural pattern with four properties at one specific field of one specific provenance specification; CKS does not inherit OIDA's complete architecture, OIDA's specific implementations, OIDA's broader commitments, or OIDA's design choices outside the cited contribution.

## 6. Why naming the inheritance edge as standalone matters architecturally

The inheritance edge is load-bearing for several CKS architectural properties already formalized in adjacent notes, and naming it as standalone is what makes those connections visible.

The first-class-conflicts commitment per A1.03 depends on contradictions being addressable substrate content, which depends on the relationship field carrying architectural content beyond inferred-from-pieces inconsistency. The OIDA inheritance grounds this dependency: addressability is not a CKS axiom, it is an inherited property the source paper cites prior art for. The two-level coupling per A2.15 depends on cell-level resolution being able to operate on addressable contradictions; cells reach for the relationship through its addressability sub-property, which traces to OIDA's contribution. The cell-level resolution mechanism per A2.14 depends on cells engaging contradiction relationships under orchestration rules with dimensional information about what is being contradicted; the characterization sub-property — that the relationship carries metadata about the contradiction's nature — is what makes this engagement well-defined, and it traces to OIDA's signing contribution. The auditability property A2.15 names depends on humans exercising the inspect right being able to navigate contradiction relationships from either contradicting piece; the bidirectional-symmetry sub-property supports this navigation, and traces to OIDA's bidirectional connection.

The four connections explain why naming the inheritance edge as standalone has consequences beyond formal acknowledgment. The inheritance performs three architectural functions at once: it grounds the relationship field's content as derivation rather than innovation, separating inherited from original; it preserves OIDA's authorship boundary by specifying what is and is not inherited; and it makes CKS's relationship-field-level contribution visible as the multi-human governance overlay applied to the inherited pattern, distinguishable from the inherited content. Without the standalone treatment, downstream readers reconstruct the inheritance from distributed source-paper sections; with it, the inheritance is a single citable derivation.

## 7. Operational test

A substrate's relationship field for first-class conflicts inherits the OIDA-cited architectural pattern if and only if all of the following are true at all times during the substrate's existence.

1. Contradictions are identifiable as substrate-content objects, not as patterns inferred from reading contradicting pieces.
2. Contradiction objects are addressable — referenced, queried, and operated on as units within the substrate's operations.
3. Contradiction objects are bidirectionally connected — readers approaching from either contradicting piece can navigate to the contradiction relationship.
4. Contradiction objects carry characterization metadata describing the dimension on which the pieces are contradicting.

A substrate that satisfies (1)–(4) inherits the architectural pattern. CKS additionally requires the following three properties for the relationship field to instantiate the CKS commitment, not merely the inherited pattern.

5. The relationship field is itself human-governed substrate content per A1.01: humans retain inspect, modify, and override rights over the relationship at all times, and no LLM operation, vendor policy, or runtime middleware layer can prevent the exercise of those rights.
6. The relationship field carries provenance per A2.16's four-field specification: writer, timestamp, rationale where applicable, and (recursively) relationship to the substrate content it sits between.
7. The relationship field operates within the cell-level resolution mechanism per A2.14: cells executing over the substrate engage the relationship under human-authored orchestration rules, and resolution decisions reference the relationship through the four-field provenance specification.

A substrate that satisfies (1)–(7) inherits OIDA's architectural pattern at the relationship-field level and adds CKS's multi-human governance overlay. A substrate that satisfies (1)–(4) but not (5)–(7) inherits the pattern without the overlay; it stands in the broader OIDA-cited lineage but does not instantiate the CKS commitment at the relationship-field level. A substrate that satisfies neither (1)–(4) nor (5)–(7) does not implement first-class contradiction relationships in the sense the CKS commitment requires; whatever its conflict-handling does, it is doing it through some other architectural pattern.

## 8. Why naming this inheritance edge as standalone matters for prior-art purposes

The strategic posture for CKS at the relationship-field level is that the inherited content is OIDA's prior art — publicly available, citable, and not CKS's claim to novelty — while CKS's claim is the multi-human governance overlay applied to the inherited pattern. Implementations that adopt the contradictions-as-relationships pattern without acknowledging OIDA's prior art produce work substantially harder to defend if the pattern becomes contested; implementations that adopt the pattern with the multi-human governance overlay but without distinguishing inherited from original content cannot identify what is novel beyond the inheritance. Naming the inheritance edge as standalone — with the four inherited properties of section 2, the four inheritance points of section 3, the three CKS additions of section 4, and the five non-claims of section 5 — gives downstream readers a precise specification of what CKS does and does not claim on this axis.

With this note complete, the conflict-as-first-class decomposition is fully formalized. A2.13 specified substrate-level preservation as standalone; A2.14 specified cell-level resolution under orchestration rules as standalone; A2.15 specified the two-level coupling between them; A2.16 specified the four-field provenance requirements; and A2.17 specifies the OIDA inheritance grounding the fourth field's architectural content. The five notes together render A1.03's parent commitment as five separately-defensible derivations: the substrate-level half, the cell-level half, the joint coupling, the metadata structure, and the prior-art grounding. Subsequent work that adopts, extends, composes with, or argues against the conflict-as-first-class commitment can address whichever derivation is at issue without reconstructing the others.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion notes

Li, W. (2026). *Conflict as First-Class Object: Two-Level Conflict Handling in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inheritance and Extension: How CKS Builds on Knowledge Objects and OIDA Along the Multi-Human Axis.* 27 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Signed Contradiction Edges as Cited Prior Art: How CKS Inherits from OIDA on the Relationship Field of First-Class Conflicts.* 2 May 2026. ORCID: 0009-0004-8065-3235.
