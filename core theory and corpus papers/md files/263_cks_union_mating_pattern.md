# Union Mating Pattern — Formalizing the Inclusive No-Selection Combination Pattern Where All DNA Elements from Both Parent Sources Are Combined into Offspring DNA with Conflicting Parent DNA Elements Preserved as First-Class Conflicts per A1.03

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the Union mating pattern as the first and most inclusive of three mating pattern variants within the lifecycle mating primitive B1.10, formalizing how all DNA elements from both parent sources are combined into offspring DNA without selection or filtering, and how conflicting parent DNA elements are preserved as first-class architectural artifacts per A1.03 rather than auto-resolved at mating time.

## Abstract

Paper 2 (Li, April 2026) commits to mating as a governed lifecycle primitive applicable at every level of the CKS architectural hierarchy — cell, aspect, Self — with three pattern variants configuring how parent content is combined. The first and most inclusive variant is Union: all DNA elements from both parent sources are included in the offspring DNA, with no selection rules applied and no element filtering performed. Offspring DNA equals the superset of both parents' DNA elements. When parent sources carry DNA elements covering the same operational concern with conflicting specifications, Union does not auto-resolve the conflict by preferring one parent; it registers the conflict as a first-class substrate artifact per A1.03, preserving it in the offspring DNA as persistent state for post-birth governance review. This note formalizes the Union mating pattern: its precise architectural definition, what makes it architecturally distinctive relative to biology's allele dominance resolution model, the inherited Paper 1 commitments it carries, its operational implications for deployments, and its limits. Union is the second decomposition of B1.10, following B2.45 (mating mechanism operational specification).

---

## 1. Why the Union mating pattern requires standalone formalization

Paper 2's B1.10 establishes mating as a governed lifecycle primitive with three pattern variants. The three variants — Union, Selective merge, and Lineage-preserved union — are named in the source paper's core theory section as distinct configurations of the mating primitive, each with its own architectural commitments and its own appropriate use conditions. Naming three variants is not the same as formalizing each variant's operational specification. B2.45 established the mating mechanism's overall operational structure. The present note addresses the first variant specifically.

Union is not merely the "default" or "simplest" mating pattern. It carries a precise architectural commitment — the inclusive superset combination — and a distinctive treatment of parent DNA conflicts that diverges from the dominant-and-recessive allele resolution model biology uses. That divergence is architecturally load-bearing: it is what makes Union a pattern that preserves parent DNA conflicts for human governance rather than silently resolving them at mating time. This treatment inherits from A1.03 (conflict as first-class object) and constitutes the Union pattern's most consequential property for downstream governance.

The strategic position within Phase B2 is equally important. B2.46 is the forty-sixth of approximately 110 Phase B2 operational variants and decompositions, and the second of six notes decomposing B1.10. Formalizing Union as a standalone note is what makes B2.47 (Selective merge) and B2.48 (Lineage-preserved union) legible as distinct patterns by contrast: each subsequent note can identify precisely what it does differently from Union. Together the three pattern notes, combined with B2.49 (mating governance and lineage establishment) and B2.50 (mating verification), close the B1.10 decomposition and establish complete prior-art coverage of mating as a governed lifecycle primitive.

---

## 2. The architectural pattern precisely stated

The Union mating pattern is defined by four properties taken together.

**Totality.** Every DNA element from parent source A and every DNA element from parent source B is included in the offspring DNA. No element from either parent is excluded, filtered, or deprioritized. If parent A carries elements {a₁, a₂, a₃} and parent B carries elements {b₁, b₂, b₃}, the offspring carries {a₁, a₂, a₃, b₁, b₂, b₃}. The offspring's DNA is the superset of both parents' DNA.

**No selection rules applied.** Union does not apply curation rules that pre-select which elements cross from each parent into the offspring. Curation-based combination is the Selective merge pattern formalized in B2.47. Union applies no such rules: the combination is total and unconditional on element content.

**Conflict preservation per A1.03.** When parent A and parent B carry DNA elements that cover the same operational concern with conflicting specifications, Union registers the conflict as a first-class architectural artifact in the offspring DNA. Both conflicting elements are present in the offspring's substrate. The conflict is preserved — not merged, not resolved, not silently overridden — as persistent substrate state with provenance attached, per A1.03's commitment to conflict as a first-class addressable object. Resolution of the conflict is a post-birth governance event, not a mating event. The appropriate resolution mechanism is directed selection per B1.14, operating after the offspring has been born and its conflict registry has been populated.

**Governance authorization required.** Union mating is not an autonomous architectural operation. The decision to mate two parent sources using the Union pattern is a governance decision under B2.41. Humans hold authority over the mating decision, over the choice of Union as the applicable pattern (versus Selective merge or Lineage-preserved union), and over the subsequent governance review of the offspring's conflict registry.

Two additional properties follow from these four. **Cross-lineage offspring:** the Union offspring carries provenance to both parent sources per B2.43, establishing two lineage ancestors. The offspring's substrate content is traceable through both parent lineages, not a single lineage. **Birth per B1.09:** Union produces an offspring specification; the offspring then undergoes birth per B1.09 and birth verification per B2.44 before it operates as an active entity in the architectural hierarchy.

The parent sources in Union mating may be: the DNA layers of two existing cells per B2.25; one or both may be Action-layer distillations processed into DNA-format specifications per B2.26. The Union pattern does not restrict parent source type; both DNA-to-DNA combination and Action-distillation-to-DNA combination are within its scope.

Provenance of the Union mating event is recorded per A2.40's six metadata fields: parent A identity, parent B identity, Union pattern applied, the resulting offspring specification, governance authorization identifier, and timestamp.

---

## 3. What makes the Union mating pattern architecturally distinctive

The Union pattern's most consequential architectural property is its conflict treatment. Biology's closest analogue — genetic recombination in sexual reproduction — combines genetic material from two parent organisms. But biological recombination resolves parent conflicts through allele dominance: where two alleles exist for the same genetic locus, the dominant allele suppresses the recessive one in the organism's expressed phenotype. The conflict is resolved at combination time by an architectural rule (dominance hierarchy) that the organism inherits and cannot override.

CKS Union inverts this. Where parent DNA elements conflict on the same operational concern, Union does not resolve the conflict. It preserves both conflicting specifications in the offspring's substrate as a named, addressable conflict per A1.03. The conflict is not suppressed; it is made visible as a first-class object that occupies a position in the offspring's substrate with its own provenance. Governance then addresses it — specifically, post-birth directed selection per B1.14 allows humans to decide which specification governs for which operational contexts, or whether the conflict requires architectural redesign upstream.

This inversion is not incidental. It is the direct inheritance of Paper 1's conflict-as-first-class commitment (A1.03) applied to the mating context. Paper 1 establishes that contradictions encountered during AI-mediated coordination are preserved in the substrate as first-class addressable objects rather than silently merged or overridden. Union extends that commitment to merge-time conflicts arising when two parent DNA sources are united. The closest computational neighbor is Git two-parent merge with conflict markers, but Git markers are transient: the merge cannot complete without resolving them, and they disappear after resolution. Union's commitment is the inverse: conflicts become persistent substrate state that the offspring carries forward indefinitely, until governance-directed resolution occurs.

The second distinctive architectural property is cross-layer applicability. Biological genetic recombination operates exclusively on genomic DNA through meiosis. CKS Union applies wherever two DNA-format parent sources exist, regardless of whether those sources originated as DNA layers of existing cells or as Action-layer distillations processed into DNA-format specifications. This cross-layer applicability is a degree of freedom over biology, enabling combination of operational knowledge that originated in different layers of the architectural hierarchy.

---

## 4. The biological analog and where CKS Union diverges

The biological analog for Union is genetic recombination in sexual reproduction — the combination of chromosomal material from two parent organisms to produce offspring carrying heritable content from both. The analog is useful as an orientation to the pattern's purpose: Union, like genetic recombination, is an inclusive two-parent combination that produces offspring carrying heritable content from both sources.

The divergence is on conflict resolution. Biology resolves allelic conflicts at combination time through dominance hierarchies. These hierarchies are not governance decisions; they are encoded in the organism's molecular biology and operate without human authority or review. A recessive allele in a heterozygous organism is present in the genotype but suppressed in phenotype — the conflict is resolved at the architectural level, silently.

CKS Union treats this as an architectural choice that should not be automatic. The architecture's commitment to human governance (A1.01) and conflict-as-first-class (A1.03) precludes silent conflict resolution at any layer. When parent DNA conflicts, the conflict is a coordination question — which parent's specification governs this operational concern in this offspring? — that is answerable only through human authority. Resolving it silently would be a governance violation. Union therefore preserves the conflict and makes it a subject of post-birth directed selection under human authority.

The CKS advantage is not that Union handles conflicts "better" in some abstract sense. The advantage is that Union makes conflicts visible as addressable substrate state, enabling governance review and traceability. The trade-off is that a Union offspring may carry an unresolved conflict registry that requires governance attention before the offspring operates fully. This trade-off is architectural: it is not a defect in Union but the correct expression of A1.03's commitment at mating time.

---

## 5. Inherited Paper 1 commitments

Union mating carries all six Paper 1 architectural commitments. The directly load-bearing ones for this pattern are as follows.

**A1.03 — Conflict as first-class object.** Union's defining treatment of parent DNA conflicts is the direct inheritance of A1.03. Where parent A and parent B conflict on an operational concern, the conflict is preserved in the offspring's substrate as a named, addressable, first-class object with provenance. This is not optional; it is the pattern's architectural commitment.

**A1.01 — Human-governed.** Governance authorization for Union mating is required per B2.41. The decision to use Union (versus Selective merge or Lineage-preserved union) is a governance decision. The subsequent review of the offspring's conflict registry is a governance event. The right to inspect, modify, and override all substrate content — including the Union offspring's DNA and its conflict registry — remains with humans at all times.

**A2.04 — Rule authoring.** The orchestration rules governing how the offspring's cells handle its conflict registry are human-authored per A2.04. Union preserves the conflicts; orchestration rules in the offspring govern how the offspring cell behaves when it encounters a conflicting specification during operation.

**A2.40 — Provenance metadata.** Union mating events are recorded with the six provenance metadata fields per A2.40: parent A identity, parent B identity, pattern applied, offspring specification, governance authorization, and timestamp. This ensures that the Union event is traceable from the offspring backward through both parent lineages.

**A1.07 — Path retraceability.** The Union offspring's substrate content traces through two lineage ancestors. The provenance record per A2.40 and the cross-lineage architecture per B2.43 together ensure that every element of the offspring's DNA is reachable backward through the mating event to its source parent.

**A1.13 — Composition requirements.** The Union offspring must satisfy composition requirements per A1.13. Union producing a valid offspring specification is necessary but not sufficient; birth verification per B2.44 must pass for the offspring to become an active entity. Compositional validity is verified post-birth, not guaranteed by the Union operation itself.

---

## 6. Operational implications

**Use condition: complementary parent DNA.** Union is architecturally appropriate when parent A and parent B carry primarily complementary DNA elements — elements that cover different operational concerns without conflict. In that case, Union produces an offspring that combines both parents' full operational repertoires without populating a conflict registry. The offspring is operationally richer than either parent individually.

**Offspring DNA size.** Because Union includes all DNA elements from both parents without filtering, the offspring's DNA is at least as large as each parent's DNA individually, and larger than either parent if the parents carry non-overlapping elements. Deployments using Union should anticipate offspring DNA that is larger than individual parent DNA and plan storage and expression-substrate configuration accordingly.

**Post-Union conflict registry.** When parent sources carry conflicting DNA elements, Union populates the offspring's conflict registry. The conflict registry is substrate state per A1.03 — it persists across sessions, carries provenance, and requires governance attention. Post-birth governance review processes the registry through directed selection per B1.14, where humans decide which specification governs and record that decision as substrate content.

**Specialized cell combination.** A primary operational application of Union is combining cell A's domain knowledge DNA with cell B's process knowledge DNA to produce an offspring that carries both. Where the two knowledge domains are complementary rather than conflicting, Union produces the combined DNA without populating a conflict registry, enabling a full-repertoire offspring in a single mating event.

**Aspect coordination combination.** Union is applicable at the aspect level: combining aspect A's coordination rules with aspect B's coordination rules when full combination is needed and both aspects' full DNA repertoires should be available in the offspring aspect. The same conflict-preservation commitment applies at the aspect level.

**Cross-partner Union.** Cross-partner Union mating — combining DNA from cells belonging to different organizational partners — requires cross-partner authority per A2.47. The governance authorization for such Union events must carry cross-partner authority, not just intra-partner mating authority.

---

## 7. Limits

The Union mating pattern has precise limits. Naming these limits is as important as naming the pattern itself, because each limit corresponds to a distinct architectural pattern that handles the case Union does not.

**Union does not auto-resolve parent DNA conflicts.** A1.03 conflict-first-class preservation holds unconditionally. Any implementation that resolves parent DNA conflicts during the Union mating event — by preferring one parent over the other, by merging conflicting specifications, or by applying a dominance hierarchy — is not instantiating Union. It may be instantiating Selective merge (B2.47) or a conflict-resolution operation separate from mating.

**Union does not filter DNA elements.** Filtering — pre-curating which elements cross from each parent into the offspring — is the Selective merge pattern per B2.47. Union applies no filtering: all elements from both parents are included unconditionally.

**Union does not explicitly preserve parent lineage pointers in the birth record.** Explicit parent lineage pointers in the offspring's substrate are the commitment of the Lineage-preserved union pattern per B2.48. Union produces cross-lineage provenance per B2.43 through the mating event's provenance record per A2.40, but does not commit to explicit per-element parent lineage pointers in the offspring's substrate. That is Lineage-preserved union's additional commitment.

**Union does not guarantee compositional validity of offspring.** Birth verification per B2.44 must pass independently. Union produces the offspring specification; whether that specification satisfies composition requirements per A1.13 is determined by birth verification, not by the Union operation.

**Union is not always the appropriate mating pattern.** When parent DNA elements conflict extensively — when a significant fraction of parent A's and parent B's DNA elements cover the same operational concerns with conflicting specifications — Union produces a conflict-registry-heavy offspring that requires substantial post-birth governance work before it operates. In that scenario, Selective merge per B2.47 may be more appropriate: it allows governance to pre-curate what crosses the boundary from each parent, reducing the conflict registry at the cost of additional pre-mating governance labor.

**Union is not reversible after birth.** The offspring is a new entity. Once born per B1.09, it has its own substrate identity and lineage. Undoing a Union mating event after birth is not an operation within Union's scope; it would require the offspring's retirement per B1.11.

**Union governance authorization does not dissolve the parent sources.** The parent cells or aspects that participate in a Union mating event continue as active entities unless they are separately subject to death per B1.11. Union produces a new offspring; it does not retire the parents. Retirement of parents after mating is a separate governance decision under death governance per B1.11.

---

## 8. Operational test

A mating event instantiates the Union mating pattern if and only if: (1) all DNA elements from both parent sources are included in the offspring DNA without selection or filtering; (2) any conflicting parent DNA elements are preserved in the offspring substrate as first-class conflict artifacts per A1.03 rather than auto-resolved; (3) governance authorization for the Union event has been obtained per B2.41; and (4) the offspring undergoes birth per B1.09 with provenance recorded per A2.40 and cross-lineage attribution per B2.43.

---

## 9. Why naming Union as a standalone pattern matters

The formalization here establishes Union as a specific, named, defensible architectural pattern within the CKS theory's mating primitive. Without standalone formalization, the term "Union" in Paper 2's core theory section is a label with a brief description. With standalone formalization, it becomes a pattern with: a precise architectural definition (inclusive superset combination with A1.03 conflict preservation); a named set of inherited commitments (A1.03, A1.01, A2.04, A2.40, A1.07, A1.13); an operational test; explicit limits distinguishing it from Selective merge (B2.47) and Lineage-preserved union (B2.48); and operational guidance for deployments.

This formalization is the second of six notes decomposing B1.10. B2.45 established the mating mechanism's overall operational specification. B2.46 (this note) formalizes Union. B2.47 will formalize Selective merge — the filtering pattern, contrasting Union's no-filtering commitment with governed pre-curation. B2.48 will formalize Lineage-preserved union — the explicit-lineage-pointer pattern, extending Union's cross-lineage provenance with per-element parent attribution. B2.49 will address mating governance and lineage establishment as a composite treatment. B2.50 will address mating verification as a standalone commitment. Together, these six notes close the B1.10 decomposition and establish complete prior-art coverage of mating as a governed lifecycle primitive in CKS architecture.

Following B2.50, Phase B2 proceeds to decompose B1.11 death as governed retirement, beginning with B2.51.

---

## Source paper

Li, Wenxin. "The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance." April 2026. §6.3 (Mating as one governable primitive over content combination), §6 (Claim 3 — Lifecycle operations as governed primitives at every level of CKS Selves).

## Self-citation and cross-references

- A1.01: "Authority, Not Labor: A Precise Definition of 'Human-Governed' in the Coordination Knowledge Substrate Pattern" — foundational governance commitment
- A1.03: Conflict as first-class object — directly load-bearing for Union's conflict preservation treatment
- A1.07: Path retraceability and the accountability vocabulary — directly load-bearing for Union provenance
- A1.13: Composition requirements — directly load-bearing for Union offspring validity
- A2.04: Rule authoring — directly relevant for Union offspring's orchestration rules
- A2.40: Six provenance metadata fields — directly relevant for Union event recording
- B1.10: Mating as cross-layer combination (three patterns) — parent note for this decomposition
- B2.25: DNA-layer mating — parent source type directly relevant
- B2.26: Action-layer mating — parent source type directly relevant
- B2.43: Lineage establishment — cross-lineage provenance for Union offspring
- B2.44: Birth verification — required for Union offspring
- B2.45: Mating mechanism operational specification — immediately prior decomposition note
- B2.47: Selective merge mating pattern — contrasting pattern; next decomposition note
- B2.48: Lineage-preserved union mating pattern — extending pattern; subsequent decomposition note
- B2.49: Mating governance and lineage establishment — subsequent decomposition note
- B2.50: Mating verification — subsequent decomposition note
