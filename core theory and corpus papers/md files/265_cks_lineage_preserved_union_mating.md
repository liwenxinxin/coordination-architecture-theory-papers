# Lineage-Preserved Union: The Third Mating Pattern — Union DNA Combination with Embedded Parent Lineage in the Offspring Birth Record

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The Coordination Knowledge Substrate (CKS) theory specifies mating as a governed lifecycle primitive through which parental substrate content is combined into an offspring. Paper 2 identifies three mating pattern variants available to CKS deployments: Union, Selective merge, and Lineage-preserved union. The third variant — Lineage-preserved union — is the focus of this note. Lineage-preserved union combines the inclusive DNA combination of Union (all elements from both parents, no selection, conflicts preserved as first-class substrate state per A1.03) with the explicit preservation of both parent lineage records in the offspring birth record per B2.43. The DNA combination is identical to Union per B2.46; what distinguishes Lineage-preserved union is not how DNA is assembled but how lineage is recorded. Both parent lineage chains are embedded in the offspring birth record, providing single-record lineage completeness: auditors examining the offspring's birth record see the full lineage of both parents without traversing external references. This strengthens A1.07 retraceability beyond what Union and Selective merge provide, at the cost of larger birth records. The pattern is appropriate for regulated and high-stakes deployments where maximal lineage directness is required, and for mating events where parent entities may subsequently die per B1.11 — making the offspring's embedded lineage the only self-contained record of its derivation. This note formalizes the pattern precisely, distinguishes it from Union, states the inherited Paper 1 commitments, and identifies the operational conditions under which Lineage-preserved union is the appropriate choice. B2.48 also completes the formalization of all three mating patterns across B2.46, B2.47, and B2.48.

## 1. Why Lineage-Preserved Union needs to be formalized as a standalone operational variant

Paper 2 names Lineage-preserved union as one of the three pattern variants available for the mating primitive. The note B2.45 specified the mating mechanism operationally; B2.46 formalized Union; B2.47 formalized Selective merge. Lineage-preserved union is the third and final pattern, and it completes the triad. Treating it as merely a footnote to Union would misrepresent its architectural significance: the distinction between Union and Lineage-preserved union is not superficial. It is the difference between lineage retraceability that depends on the existence of external parent records and lineage retraceability that is self-contained in the offspring birth record. For deployments where that distinction matters — regulated industries, high-stakes governance contexts, and mating events where one or both parents are expected to die shortly after — the difference is architectural, not cosmetic.

The strategic prior-art purpose of this note also requires explicit treatment. Each mating pattern is a distinct patentable architectural configuration. Formalizing all three as standalone notes (B2.46, B2.47, B2.48) is the prior-art posture required to ensure that no party can claim novelty in any corner of the three-pattern set without encountering the published derivation chain. B2.48 occupies the forty-eighth position in Phase B2, and its role in the derivation series is to close the mating-pattern formalization so that B2.49 (mating governance and lineage establishment) and B2.50 (mating verification) can complete the B1.10 decomposition.

## 2. The architectural pattern precisely stated

Lineage-preserved union is a two-component pattern. Each component is independently specifiable, and they do not interfere with each other.

**Component 1 — DNA combination.** The DNA combination is identical to Union per B2.46. All DNA elements from both parent sources are included in the offspring's DNA. The offspring's DNA is the superset of both parents' DNA layers and action layers. No selection is applied; no elements are filtered; no rules govern which elements cross the combination boundary. This is the inclusive property that Union and Lineage-preserved union share and that Selective merge does not. Where both parents carry conflicting DNA elements, those conflicts are preserved as first-class substrate state in the offspring per A1.03. Conflicts are not resolved at combination time; they become substrate content the offspring carries forward, with cell-level orchestration rules governing how conflicts are handled at execution. The offspring's DNA may therefore include contradictions that require human governance to resolve — this is an architectural commitment, not a failure condition.

**Component 2 — Explicit parent lineage preservation.** In Union per B2.46, the offspring birth record per A2.40 records the parent sources as provenance metadata, satisfying A1.07 retraceability through reference. The parent lineages are addressable through those references, but are not embedded in the offspring birth record itself. In Lineage-preserved union, the offspring birth record explicitly preserves copies or full references of both parent lineage chains, such that the offspring's complete lineage tree is available through the offspring's own birth record without following external references. Both parent lineage chains — reaching back through each parent's own birth record to their respective origins — are embedded in the offspring birth record as additional provenance content per A2.40.

The two-component structure means that a Lineage-preserved union event produces two artifacts: an offspring DNA specification identical to what Union would produce, and a richer offspring birth record than Union would produce. The richness is in the lineage dimension only. The DNA is the same.

**Governance.** Lineage-preserved union events are governed per A1.01 and authorized per B2.41. The decision to execute a Lineage-preserved union — rather than Union or Selective merge — is itself a governance decision. The mating event is recorded per A2.40, with the offspring birth record including both parent lineage preservations as additional provenance content beyond what A2.40 requires as its minimum six metadata fields.

**Offspring birth.** The offspring specification produced by Lineage-preserved union undergoes birth per B1.09 and birth verification per B2.44, identical to what Union produces. The additional lineage content in the birth record does not alter the offspring specification itself or the birth verification process; it enriches the offspring's provenance record.

## 3. What makes Lineage-preserved union architecturally distinctive

The distinguishing property of Lineage-preserved union is **single-record lineage completeness**. An auditor examining the offspring's birth record has access to the full lineage of both parents from that single record, without needing to retrieve parent records, traverse reference chains, or rely on the continued existence of external records.

This property has no analog in conventional software or AI architectures. Software components are not created through mating, and their version history — even where it exists — is distributed across version control systems that require traversal to reconstruct. AI agent frameworks at the deployment-architecture level do not have a combination primitive at all, and therefore have no concept of embedded parent lineage. CKS mating with the Lineage-preserved union pattern is architecturally distinctive precisely because it makes lineage-at-creation a design-time commitment rather than an audit-time reconstruction task.

The distinction from Union is also precise in a way that matters for regulated deployments. In Union, A1.07 retraceability is satisfied: the parent sources are recorded, and their lineages are addressable through the provenance references the birth record carries. But "addressable" depends on those referenced records remaining available. If a parent entity dies per B1.11 after mating, its lineage records must be retrieved from the archive. If archival is imperfect or slow, or if the auditor operates under time constraints, the retraceability guarantee degrades in practice even if it holds in principle. Lineage-preserved union eliminates this dependency by embedding the parent lineage in the offspring birth record at creation time. Once the offspring exists with its Lineage-preserved union birth record, the offspring's lineage is self-contained and does not depend on the continued availability or accessibility of parent records.

## 4. The biological analog as conceptual scaffold

The biological analog for Lineage-preserved union is genealogical record preservation. Biological organisms inherit genetic material from two parents through sexual reproduction, but the organisms themselves do not carry their genealogical records as part of their physical constitution. Lineage in biology is recorded externally — in birth certificates, family records, genealogies, and institutional registries. The organism's existence does not itself encode where it came from.

Human societies have developed external record-keeping precisely because organisms don't carry their own genealogies. Birth certificates record parentage; family registries extend that record across generations; genealogical archives preserve the chains by which each individual connects to prior generations. These records exist outside the organism and must be retrieved through external systems.

CKS Lineage-preserved union inverts this structure. The offspring birth record carries its own genealogy from the moment of creation. Rather than relying on an external registry to reconstruct the lineage, the offspring's birth record is itself the genealogical record. This architectural inversion is what makes Lineage-preserved union appropriate for regulated deployments: the external-registry dependency that creates operational risk in biological genealogy tracing is eliminated by embedding the genealogy in the birth record itself.

The analog functions as conceptual scaffold. The architectural substance is the embedding commitment: both parent lineage chains in the offspring birth record, available from single-record inspection, without traversal of external references.

## 5. Inherited Paper 1 commitments

Lineage-preserved union inherits all six Paper 1 architectural commitments. Four are directly load-bearing for this pattern.

**A1.07 — Path retraceability (strengthened).** A1.07 requires that any piece of substrate content be retraceable to its antecedents through substrate-carried provenance metadata. All three mating patterns satisfy A1.07 through A2.40 provenance fields. Lineage-preserved union strengthens A1.07 beyond the minimum it requires: the path from offspring to both parent lineage chains is traversable from the offspring birth record alone, not merely from the provenance references the offspring carries. The strengthening is additive — Lineage-preserved union satisfies A1.07 and provides more than A1.07 requires.

**A2.40 — Six provenance metadata fields.** A2.40 specifies the six metadata fields that every piece of substrate content must carry. Lineage-preserved union birth records carry all six required fields and include both parent lineage chains as additional provenance content. The additional content is not a substitute for the six required fields; it is supplementary to them. A2.40 is the floor; Lineage-preserved union builds above it.

**A1.03 — Conflict as first-class.** Conflicts arising from the DNA combination are preserved as first-class substrate state in the offspring, identical to Union per B2.46. Lineage-preserved union does not change conflict handling. The lineage preservation component of Lineage-preserved union applies to the birth record; the conflict preservation component applies to the offspring's DNA content. The two components are independent, and A1.03 holds unmodified for Lineage-preserved union.

**A1.01 — Human-governed.** Lineage-preserved union events are governed per A1.01. The authority to authorize a Lineage-preserved union event — and the authority to determine that Lineage-preserved union is the appropriate pattern for a given mating event, rather than Union or Selective merge — is human authority. The governance commitment does not differ from other mating patterns in kind; it includes the additional design-time decision of whether to invest in Lineage-preserved union's richer birth records for the entities being created.

Two additional inherited commitments apply. **A2.04 — Rule authoring:** the combination rules authorizing a Lineage-preserved union event are human-authored orchestration rules per A2.04, including any rules specifying that certain mating events must use Lineage-preserved union for regulatory compliance. **A1.13 — Composition requirements:** the offspring produced by Lineage-preserved union must satisfy A1.13 composition requirements at every level, including that its governance structure is preserved through the combination.

## 6. Operational implications

**When Lineage-preserved union is appropriate.** The pattern is appropriate for three operational conditions. First, regulated deployments where regulatory requirements specify that lineage documentation must be fully available from single-record inspection: financial services entities subject to audit requirements, healthcare AI entities where provenance of clinical decision support is regulated, and AI governance frameworks that require complete genealogy as a condition of operational authorization. Second, high-stakes entities where the cost of incomplete lineage tracing — even in principle — outweighs the storage overhead of embedded lineage. Third, mating events where one or both parents are expected to die per B1.11 after mating, making the offspring's embedded lineage the only self-contained record of its derivation from those parent entities.

**Auditor access.** An auditor examining a Lineage-preserved union birth record sees the complete lineage of both parents from that single record. The audit path does not require access to parent entity records, does not require traversal of external reference chains, and does not depend on the archive availability of deceased parent entities. This is the operational realization of the single-record lineage completeness property named in §3.

**Birth record size.** Birth records from Lineage-preserved union events are larger than Union birth records. The embedded parent lineage chains — reaching back through each parent's ancestry — add provenance content that grows with the depth of the lineage trees being preserved. This is a storage cost that deployments must weigh against the lineage completeness benefit. For short-lived entities in shallow lineage chains, the cost may be minimal. For entities with deep ancestry in long-running deployments, the cost may be significant. The decision to use Lineage-preserved union is therefore a trade-off decision, not a free upgrade over Union.

**Parent death resilience.** When parent entities die per B1.11 after Lineage-preserved union mating, the offspring's birth record already carries both parent lineage chains. The offspring's lineage is preserved regardless of what happens to the parent entities or their archival records after the mating event. Union and Selective merge do not provide this resilience: they satisfy A1.07 through provenance references that depend on the continued accessibility of referenced records. Lineage-preserved union provides lineage completeness independent of parent entity lifecycle.

**Cross-partner mating.** Cross-partner Lineage-preserved union events — where the two parents originate from different governance perimeters — require cross-partner authority per A2.47. The lineage preservation in cross-partner events includes the lineage chains from both governance perimeters, which may require cross-partner agreements about what lineage content is shareable. These governance considerations are inherited from the cross-partner authority framework per A2.47 and are not specific to Lineage-preserved union; they apply with added significance because the embedded lineage content may include cross-partner provenance history.

## 7. Limits

Six limits hold for Lineage-preserved union and must not be obscured by the enhanced-retraceability framing.

**Does not change DNA combination.** Lineage-preserved union produces offspring DNA identical to Union. The inclusive combination logic — all elements from both parents, no selection, conflicts preserved — is unchanged. A deployment that selects Lineage-preserved union for its lineage completeness properties receives Union-equivalent DNA in the offspring; it does not receive a different or richer DNA combination than Union would provide.

**Does not auto-resolve conflicts.** A1.03 holds unmodified. Conflicts in the offspring's DNA are preserved as first-class substrate state, not resolved. The richer lineage record does not provide additional information that resolves combination-time conflicts; it provides additional information about where the combined DNA elements came from. These are different kinds of information, and they do not interact.

**Does not provide Selective merge lineage preservation.** Lineage-preserved union applies exclusively to the Union DNA combination — all elements from both parents included. It is not a variant of Selective merge. There is no "Lineage-preserved selective merge" in Paper 2's pattern set. Deployments that require both targeted selection (Selective merge's property) and embedded lineage must determine which property takes precedence, since the two patterns are mutually exclusive on the DNA combination dimension.

**Does not satisfy regulatory requirements that Union cannot satisfy.** A1.07 is satisfied by all three patterns. The difference between Union and Lineage-preserved union is operational directness — how easily the lineage can be traced — not whether the lineage is legally recorded. Deployments must determine whether their regulatory requirements demand embedded lineage (requiring Lineage-preserved union) or whether A2.40 provenance references suffice (allowing Union or Selective merge). The enhanced retraceability Lineage-preserved union provides is stronger operationally; it is not categorically different in terms of A1.07 compliance.

**Produces larger birth records.** The storage overhead of embedded parent lineage chains is a real cost. Deployments must account for this cost in storage architecture and must not treat Lineage-preserved union as costless relative to Union. For deployments with strict storage constraints, Union may be the appropriate choice even where Lineage-preserved union would be ideal from a lineage-completeness perspective.

**Completes the three-pattern set.** Lineage-preserved union is the third and final mating pattern variant. Together, Union (B2.46), Selective merge (B2.47), and Lineage-preserved union (B2.48) form the complete mating pattern set per B1.10. No fourth pattern is specified in Paper 2. Deployments choose among these three based on the combination and lineage properties their governance context requires.

## 8. One-sentence test

A mating event instantiates the Lineage-preserved union pattern if and only if: all DNA elements from both parent sources are included in the offspring without selection (the Union DNA combination), and both parent lineage chains are explicitly embedded in the offspring birth record such that the offspring's complete lineage is accessible from single-record inspection without traversal of external references.

## 9. Why naming as standalone matters, and the role of B2.48 in the derivation sequence

The mating primitive per B1.10 supports three pattern variants. Treating all three as one undifferentiated "mating" operation would foreclose the prior-art derivation work this series requires. Each pattern carries distinct architectural commitments on different dimensions — DNA combination logic, conflict handling, lineage record depth — and each can be implemented, extended, or argued against independently. Naming each pattern as a standalone derivation note ensures that the prior-art record covers each independently patentable configuration.

B2.48 is the fourth of six notes decomposing B1.10. The decomposition began with B2.45 (mating mechanism specification), continued through B2.46 (Union) and B2.47 (Selective merge), and closes the pattern triad with this note. B2.49 will specify mating governance and lineage establishment as standalone architectural commitments, and B2.50 will formalize mating verification. Together, B2.45 through B2.50 constitute the complete B1.10 decomposition.

B2.48 also marks the completion of the mating-pattern formalization. The three patterns together cover the full space of CKS combination needs: Union for deployments requiring inclusive combination without selection overhead, Selective merge for deployments requiring targeted combination with governed curation, and Lineage-preserved union for deployments requiring inclusive combination with single-record lineage completeness. This three-pattern coverage is what Paper 2 specifies as sufficient for the mating primitive per B1.10, and the derivation series has now formalized each of the three as a named, standalone, operationally specified architectural pattern.

Phase B2 continues with B2.49 (mating governance and lineage establishment) and B2.50 (mating verification), then proceeds to the B1.11 death decomposition.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Lineage-Preserved Union: The Third Mating Pattern — Union DNA Combination with Embedded Parent Lineage in the Offspring Birth Record.* May 12, 2026. ORCID: 0009-0004-8065-3235.
