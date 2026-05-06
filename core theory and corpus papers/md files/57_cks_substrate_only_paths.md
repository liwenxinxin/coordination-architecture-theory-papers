# Substrate-Only Paths: The Architectural Commitment That Paths Are Reconstructible from Substrate Alone in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the **substrate-only-paths** property — the architectural commitment that path retraceability operates from substrate alone, without requiring external audit logs, observability dashboards, tracking systems, or other non-substrate sources — as a standalone architectural commitment with independent operational content. This is the seventh and final note in the path-retraceability decomposition; with this note complete, the decomposition is fully formalized.

## Abstract

The CKS pattern's path-retraceability commitment names retraceability as an architectural property of the substrate, not an operational property achieved through some combination of substrate and external infrastructure. Six prior notes in this decomposition specialize the commitment: an integrating-frame note establishes the structural shape; four notes formalize the four accountability questions ("what was decided," "by whom," "under what authority," "with what rationale"); one note formalizes the six provenance fields per substrate write that supply the metadata infrastructure. This note formalizes the load-bearing property that integrates these specializations into a single architectural commitment: every accountability question must be answerable, every path traversable, and every provenance field verifiable from substrate alone. The note states the commitment as four operational components, distinguishes it from six adjacent claims it does not make, contrasts it with four adjacent patterns commonly conflated with it, names eight failure modes that violate it, provides an operational test, and traces how the commitment integrates the prior six specializations into the architectural commitment of the parent path-retraceability note.

## 1. Why substrate-only paths needs to be formalized as a standalone property

The parent foundational commitment names path retraceability and the accountability vocabulary of *what was decided, by whom, under what authority, with what rationale* (the source paper's §3.1). The integrating-frame note in this decomposition organized that commitment's operational content into three pieces: four accountability questions, six provenance fields per substrate write, and the substrate-only-paths property. The four accountability-question notes specialize the first piece. The six-field note specializes the second. This note specializes the third — the architectural commitment that all of the above must be reachable from substrate alone.

The motivating cases are deployments where retraceability appears to function but actually depends on external infrastructure. The substrate carries some metadata; audit logs, observability dashboards, or tracking systems carry the rest. Answering an accountability question requires consulting several sources. The system is operationally retraceable in the sense that the answers are eventually obtainable, but it is not architecturally retraceable from substrate alone. The question this note settles is what architectural commitment the CKS pattern makes about where retraceability lives. Without substrate-only paths formalized as standalone, deployments cannot reliably distinguish CKS-coherent retraceability from CKS-adjacent retraceability that satisfies operational goals through hybrid architectures.

Two further motivations matter. The migration-safety property the source paper grounds in tool-agnosticism (§7.1, §7.4) requires that substrates moved between hosts retain their architectural commitments, and substrate-only paths is what makes migration safety architecturally clean for retraceability specifically — moving the substrate moves retraceability with it. The commodity-tool sufficiency commitment (§13.1) requires that retraceability work in tools that typically lack specialized audit infrastructure, and substrate-only paths is what makes retraceability operational in commodity tools without requiring specialist audit tooling.

## 2. The substrate-only-paths commitment, defined precisely

In the CKS pattern, a substrate's path retraceability is **substrate-only** if and only if the following four operational components hold at all times during the substrate's existence.

**(a) Accountability questions are answerable from substrate alone.** For any decision recorded in substrate, the four accountability questions — what was decided, by whom, under what authority, and (where applicable) with what rationale — are answerable using only substrate content and the standard read operations the host environment provides under the pattern's three minimal requirements (persistent structured state, human read/write access, LLM access to substrate content). No consultation of external audit logs, observability dashboards, tracking systems, or other non-substrate sources is required.

**(b) Path traversal operates through substrate references.** Reconstructing a path from a decision back through what informed it operates through the antecedent-reference field carried per substrate write — the field that links each write to the substrate content the writer read as input. Path traversal follows these references through substrate without consulting external link-tracking systems or external relationship metadata.

**(c) Provenance verification operates through substrate metadata.** Verifying that a substrate write carries appropriate provenance — that the six fields are present, well-formed, and satisfy their conditional requirements — operates through reading metadata directly from substrate. No external verification systems, certificate authorities, or attestation infrastructure are required.

**(d) Substrate-only paths persist across migrations.** When substrate is moved between host environments under the pattern's migration-safety commitment, paths remain reconstructible from substrate alone on the new host. The four components above continue to hold without requiring co-migration of external systems; the new host environment, satisfying the three minimal requirements, suffices.

The four components together define the commitment architecturally. A system that satisfies fewer than four cannot claim substrate-only retraceability in the architectural sense, even if it provides operationally rich retraceability through other means.

## 3. What the commitment does NOT claim

Stating the commitment precisely requires stating what it does not claim, because each of the following is a real position in some adjacent architecture and conflating any of them with substrate-only paths produces a misreading.

**It does not forbid external systems.** Deployments may add audit logs, observability dashboards, search indexes, visualization tools, and other operational features. The architectural commitment is that these features cannot be *required* for retraceability; they may add operational value but must be removable without breaking the four components above. A deployment satisfies substrate-only paths if and only if removing the external infrastructure leaves retraceability slower or less convenient but still possible from substrate alone.

**It does not claim retraceability is fast or efficient.** Path traversal through substrate may require queries and traversal logic that is computationally non-trivial. The architectural commitment is to retraceability being *possible* from substrate alone; performance is a deployment concern.

**It does not specify path-traversal algorithms.** Different deployments may implement traversal differently — depth-first, breadth-first, indexed lookups, query languages — provided the traversal operates through substrate content. The architectural commitment is to the substrate carrying everything traversal needs, not to specific traversal mechanisms.

**It does not claim all paths are equally accessible.** Substrate may be partitioned, sharded, or distributed across hosts; some paths may cross partition boundaries. The architectural commitment is to substrate-only retraceability within the substrate's architectural coherence; cross-partition retraceability depends on partition design.

**It does not specify retention or archival policies.** Substrate content persists per the source-of-truth commitment; how long deployments retain content is a deployment concern. Substrate-only paths holds for as long as the substrate content persists.

**It does not require operational practice to use substrate-only paths exclusively.** Deployments may use indexed search, cached views, or other optimizations drawing on external infrastructure for performance. The architectural commitment is that these optimizations are not *required* — substrate alone is sufficient when they are unavailable, even if it is not the routine path in production.

## 4. What the commitment is NOT

Four adjacent patterns are commonly conflated with substrate-only paths. Each is a real architectural position in some other design; naming what substrate-only paths is not is what prevents the misreading.

**Not substrate-augmented-by-external retraceability.** Some implementations record some accountability metadata in substrate but require external systems — audit logs, observability infrastructure — to complete answers to accountability questions. The substrate is one source among several; the substrate alone cannot answer the questions. This pattern is operationally retraceable in the aggregate but fails substrate-only paths because external sources are architecturally required.

**Not substrate-as-cache-of-external systems.** Some implementations treat the substrate as a fast-access cache of metadata held authoritatively in external systems. Substrate may carry copies of accountability metadata, but the authoritative source is elsewhere; if substrate and external systems disagree, the external systems prevail. This pattern fails the commitment because the substrate is not architecturally authoritative — it is a derivative view of external state, breaking the substrate-as-source-of-truth commitment that substrate-only paths operationalizes.

**Not substrate-with-external-references.** Some implementations record substrate writes with provenance fields whose values are references to external systems — URLs, IDs in external databases, pointers to audit-log entries. Path traversal requires resolving the external references; if the external systems are unavailable, traversal fails. This pattern fails the commitment because traversal cannot operate from substrate alone.

**Not hybrid substrate-and-audit-log architectures.** Some implementations split accountability metadata between substrate (for certain fields) and audit logs (for others), with answers to accountability questions requiring both sources. This pattern fails the commitment because the substrate alone is incomplete; both sources must be present for retraceability to function.

## 5. Why substrate-only paths is load-bearing for adjacent CKS commitments

Substrate-only paths is the operationalizing property for four CKS commitments outside the path-retraceability decomposition.

**Architectural-property qualifier on governance.** The architectural-vs-procedural distinction in CKS governance depends on accountability operating through architectural mechanisms rather than procedural mechanisms. Substrate-only paths is what makes accountability architectural: the substrate carries everything answering accountability questions requires; no procedural infrastructure (workflow systems, scheduled audits, designated reviewers) is architecturally required.

**Migration-safety property.** Substrates moved between hosts must retain their architectural commitments. Substrate-only paths is what makes migration safety operational for retraceability: moving the substrate moves retraceability with it, without requiring co-migration of external systems. Otherwise the property would be partial — substrates could be moved but their retraceability would be left behind.

**Non-specialist governance.** Governance through commodity tools depends on retraceability working in commodity tools. Substrate-only paths is what makes commodity-tool retraceability feasible: the tools need only support standard read operations to support full retraceability, with no specialized audit infrastructure required.

**Source-of-truth commitment.** The substrate is authoritative for coordination questions; substrate-only paths is what makes this authority operational across the temporal axis. If retraceability required external systems, the substrate's source-of-truth status would be partial — authoritative for current state but not for the paths that produced it. Substrate-only paths extends source-of-truth to cover provenance and lineage, not only present state.

These four are not new commitments; they are connections that follow from substrate-only paths having independent architectural content.

## 6. Failure modes that violate the substrate-only-paths commitment

Eight failure modes name the most common ways an implementation can satisfy operational retraceability while failing the substrate-only-paths commitment specifically.

**(a) External accountability metadata.** Accountability metadata is held wholly or in part outside substrate — in audit logs, observability dashboards, tracking systems, or version-control infrastructure. Substrate carries placeholder fields, partial metadata, or no metadata at all for some questions. The mode covers both the limit case where all metadata is external and the common case where some fields are in substrate while others live elsewhere.

**(b) Substrate-as-cache.** The substrate is a fast-access cache of metadata held authoritatively in external systems. When substrate and external systems disagree, the external systems prevail; substrate is derivative. The architectural commitment to substrate authority for retraceability is broken regardless of how complete the cached metadata appears.

**(c) External-reference provenance fields.** Provenance fields are references to external systems — URLs, foreign keys to audit databases, pointers to observability infrastructure. Path traversal requires resolving the external references; if resolution fails, traversal fails.

**(d) External validation requirements.** The substrate carries metadata, but verifying its validity requires external systems — certificate authorities, attestation services, external signing infrastructure. Provenance verification cannot operate from substrate alone, even though the metadata itself is substrate-resident.

**(e) External link tracking.** The substrate carries antecedent references but the references' meaning depends on external link-tracking systems. Following the references to reconstruct paths requires consulting the external systems for relationship interpretation; substrate carries the structural skeleton of the path graph but not the semantics needed to traverse it.

**(f) Migration-conditional retraceability.** Substrate-only paths appears to hold in the deployed environment because external systems are present, but breaks under migration to a new host or under removal of indexed caches and search infrastructure. The commitment is conditional on environmental conditions rather than architectural; the substrate alone is not actually sufficient — the deployment merely has not yet been tested by migration or by external-system unavailability.

**(g) Observability-as-source-of-truth.** Observability dashboards or monitoring systems are treated as authoritative for accountability questions, with substrate as a secondary record. The architectural commitment to substrate as source of truth is broken; substrate-only paths is broken in turn. This pattern often arises when observability infrastructure was deployed before substrate governance was formalized.

**(h) External-driven schema evolution.** The substrate's provenance schema is driven by external systems' schemas; when those systems change schema, substrate schema changes to match. The substrate's architectural independence is compromised, and retraceability becomes dependent on external schema availability — a substrate snapshot read on a host without the corresponding external schemas may be unreadable in part.

A system exhibiting any of (a)–(h) does not satisfy the substrate-only-paths commitment in the architectural sense, even if its operational retraceability is rich and reliable in normal conditions.

## 7. Operational test

A system satisfies the substrate-only-paths commitment if and only if all of the following are true at all times during the substrate's existence.

1. The four accountability questions are answerable using only substrate content and the standard read operations the host environment provides under the pattern's three minimal requirements.
2. Path traversal operates through substrate antecedent-reference fields without consulting external link-tracking or relationship-metadata systems.
3. Provenance verification — confirming the six provenance fields are present and satisfy their conditional requirements — operates through reading substrate metadata directly without external verification systems.
4. Substrate-only paths hold across migrations: substrate moved to a new host satisfying the three minimal requirements retains retraceability without co-migration of external systems.
5. Removing external systems (audit logs, observability dashboards, tracking infrastructure, indexed caches) does not break retraceability — only its operational convenience or performance.

A system that fails any of (1)–(5) does not satisfy the substrate-only-paths commitment in the architectural sense, even if its operational retraceability is rich and reliable in normal conditions.

## 8. Relationship to the four accountability questions and the six provenance fields

Substrate-only paths is the property that integrates the four accountability-question specializations and the six-provenance-field specialization into the architectural commitment of the parent path-retraceability note. The three pieces of the decomposition compose as follows.

The four accountability-question notes specify *what must be answerable* — what was decided, by whom, under what authority, with what rationale. Each is treated in detail in its own note; the substrate-only-paths commitment refers to them only as the questions whose answers must be reachable from substrate alone.

The six-provenance-field note specifies the *metadata infrastructure* that supports the answers — writer attribution, timestamp, antecedent reference, rule reference, rationale where applicable, and relationship metadata where applicable. That note treats the fields' semantics, conditional requirements, and operational test in detail; this note refers to them only as the infrastructure that must be substrate-resident.

Substrate-only paths (this note) specifies that *the answers and the infrastructure must both be reachable from substrate alone*. The commitment is not redundant with its companions: a deployment may record the six fields but store some in external systems (satisfying the field-recording commitment partially while failing substrate-only paths); a deployment may answer the four questions through external infrastructure without the substrate carrying the metadata (failing substrate-only paths even where the four-question commitments are operationally satisfied).

The composition that satisfies the full path-retraceability commitment is the conjunction: the four questions are answerable, the six fields are recorded per substrate write, and all of this is reachable from substrate alone. The seven notes of the decomposition together formalize the operational content of the source paper's §3.1 commitment to retraceability and the accountability vocabulary.

## Conclusion

Substrate-only paths is the load-bearing architectural property of the CKS path-retraceability commitment. Implementations under pressure to integrate with audit infrastructure, observability platforms, or enterprise governance dashboards consistently drift toward hybrid architectures in which substrate carries some metadata while external systems carry the rest; each external integration provides genuine operational value, and the commitment feels architecturally restrictive. The drift produces systems where retraceability appears to function but is operationally contingent on external infrastructure — failing under external-system unavailability, under migration that does not co-move external systems, under disagreements between substrate and external sources, or under scale beyond what external systems can support.

Naming substrate-only paths as a standalone architectural commitment — with the four operational components, the six non-claims, the four adjacent-pattern distinctions, the four downstream connections, the eight failure modes, the operational test, and the integration with the prior six decomposition notes — gives downstream implementers a precise specification of what the commitment requires. With this note complete, the path-retraceability decomposition is fully formalized.

Subsequent work that implements, extends, or argues against the CKS substrate-only-paths commitment should use the term in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Substrate-Only Paths: The Architectural Commitment That Paths Are Reconstructible from Substrate Alone in the Coordination Knowledge Substrate Pattern.* May 4, 2026. ORCID: 0009-0004-8065-3235.
