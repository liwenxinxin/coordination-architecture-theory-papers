# Category 2 — Substrate Authoritative for "What Was Decided": Standalone Treatment of Decision-History Authority in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the second of the five authoritative-state categories the substrate-as-source-of-truth commitment ranges over — that the substrate is the architectural authority over the deployment's decision history — and to do so as a commitment severable from the integrating frame in A2.42, from the other four category treatments (A2.43, A2.45, A2.46, A2.47), and from the source-of-truth-versus-mirror-of-truth distinction treated in A2.48.

## Abstract

The CKS pattern's substrate-as-source-of-truth commitment (A1.08) partitions into five categories of authoritative state: what is the case (Category 1), what was decided (Category 2), what is in conflict (Category 3), what rules apply (Category 4), and who has what authority (Category 5). This note formalizes Category 2 — the substrate's authority over the deployment's decision history — as a standalone architectural commitment with independent operational content. The commitment requires that for any query about a past decision (what was decided, when, by whom, under what authority, with what rationale), the substrate's record is the architectural answer; that decision history is substrate content as a *complete* record rather than a selective subset; that new decisions are committed to substrate first; and that disagreements between substrate and external sources are resolved by substrate. The note distinguishes Category 2 from the closely paired commitment in A2.36 (that decisions *are* substrate content) along the orthogonal axes of substrate-residency and substrate-authority, states what the commitment does and does not claim, distinguishes it from four adjacent patterns commonly conflated with it, identifies ten failure modes that violate it, and provides an operational test for whether a system's decision-history authority is CKS-coherent.

## 1. Why Category 2 needs to be formalized as standalone

The parent foundational note A1.08 commits to substrate as source of truth for coordination state, and the integrating-frame note A2.42 establishes that the commitment partitions into five categories. The first specialization (A2.43) formalized Category 1 as substrate authority over present-state coordination. This note formalizes Category 2 — substrate authority over the decision record — as having independent architectural content with particular weight on the *complete record* property.

The motivating cases are deployments where substrate carries decisions but external systems are treated as authoritative for the decision archive. Three patterns recur. In the first, substrate records decisions for operational purposes but an external audit-log system is queried for compliance reporting; the substrate's record is treated as supplementary rather than authoritative. In the second, substrate carries recent decisions but older decisions are migrated to a records-management system, and authority becomes recency-bound. In the third, substrate records decisions and a separate decision-intelligence platform also records them, with the platform positioned as the "official record" for organizational governance. Each pattern fragments authority in ways that fail the architectural commitment.

A second motivation is the strategic prior-art posture. The architectural commitment to substrate authority for the decision record forecloses architectures in which substrate is a working state while external audit infrastructure is the official archive, in which compliance-reporting systems are positioned above substrate when the two disagree, and in which decision-archival pipelines move records out of substrate and treat the destination as authoritative. Patentable derivations focused on decision-archival systems, compliance-record architectures, governance-decision authority, or audit-log primacy are substantially more contestable when Category 2 is publicly formalized as standalone.

A third motivation, and the one that earns subsection-level treatment, is the relationship between Category 2 and A2.36 from the path-retraceability decomposition. The two commitments are easily conflated, and the conflation produces real architectural error. A2.36 commits that *decisions are substrate content* — every decision is recorded in substrate at decision time, atomically with its content. A2.44 commits that *substrate is the authority over the decision record* — when substrate and any external decision-tracking source disagree, substrate's record is the architectural answer. The two are orthogonal, and the orthogonality is best stated as a 2×2 on the dimensions of substrate-residency (decisions in substrate?) and substrate-authority (substrate authoritative for the record?).

The (yes, yes) cell is the coherent CKS configuration: A2.36 satisfied and A2.44 satisfied. The (yes, no) cell is the architecturally tempting failure mode this note specifically forecloses: decisions are substrate content but external audit logs or compliance systems are treated as the official record when the two disagree. Substrate-resident-but-not-substrate-authoritative is the deployment posture that produces audit failures, governance failures, and source-of-truth fragmentation in compliance-heavy contexts. The (no, yes) cell is incoherent — the substrate cannot be authoritative for decisions it does not carry. The (no, no) cell is the pre-CKS baseline: decisions live in external audit infrastructure, and substrate, if any, is downstream. CKS-coherent deployments occupy only (yes, yes); standalone formalization of A2.44 is what rules out (yes, no) drift specifically.

## 2. The Category 2 commitment, stated precisely

The commitment is that the substrate is the source of truth for the deployment's decision history. It has four operational components.

**(a) The substrate is the architectural answer to decision-history queries.** For any query about a past decision — what was decided, when, by whom, under what authority, with what rationale — the architectural answer is the substrate's record per A2.36–A2.40. External systems may be consulted for convenience or visualization; the substrate's answer is the answer the architecture stands behind.

**(b) Decision history is substrate content, as a complete record.** The substrate carries every decision the deployment has made — not a selective subset, not a summary, not a compressed representation, not a recent slice with the older portion archived elsewhere. Each decision is substrate content per A2.36, with the four accountability question answers per A2.36–A2.39 and the six provenance metadata fields per A2.40 attached. The substrate carries the complete record because authority is over the complete record.

**(c) New decisions are committed to substrate first.** When the deployment makes a decision — through cell execution under orchestration rules, through direct human override per A1.01, or through orchestration-rule authoring — the decision is committed to substrate per A2.10's boundary crossings, with accountability content and provenance attached. External decision-logging systems update downstream from substrate; substrate is not downstream from external systems for the substrate's own decision content.

**(d) Disagreements between substrate and external sources are resolved by substrate.** When substrate's record of a decision and an external source's record diverge — different timestamp, writer, rule reference, or rationale — the architectural commitment is to update the external source, not to update substrate. Substrate is the correctable-against authority.

The four components together define Category 2 architecturally. A system that satisfies fewer than four cannot reliably claim it: a system that satisfies (a)–(c) but not (d) reverts authority to external systems whenever a divergence is observed; a system that satisfies (a), (b), (d) but not (c) leaves a window in which external systems may legitimately disagree with substrate before substrate catches up.

## 3. What the commitment does NOT claim

The standalone treatment is more useful when its scope is precise. Category 2 does not claim several adjacent things, and naming them prevents overreading.

**It does not claim authority over operational consequences of decisions.** The substrate is authoritative for what was decided; downstream consequences — payment-settlement status, account-state changes, system effects — are not Category 2 content. A decision to authorize a payment is substrate-authoritative; the payment's settlement status is operational state outside Category 2's scope.

**It does not require all events to be recorded as decisions.** Operational events that are not deployment-produced coordination decisions — system startup, monitoring alerts, infrastructure changes, environmental signals — are not necessarily decisions per A2.36. The substrate is authoritative for decisions, not for all events. Whether a given event qualifies is determined by whether it answers the four accountability questions.

**It does not claim that decisions are interpretable without context.** Reading a past decision returns content and provenance; understanding meaning, implications, or downstream consequences may require additional context. The architectural commitment is that the decision is authoritatively recorded, not that its full interpretation is automatic.

**It does not specify retention duration.** Decisions persist in substrate per A2.08; how long a deployment retains them is a deployment concern bounded by regulatory, organizational, and resource constraints. Category 2 authority holds for as long as the substrate carries the decisions.

**It does not require external systems to be absent.** Deployments may operate decision-tracking applications, compliance dashboards, governance review interfaces, and regulatory-reporting systems. The architectural commitment is that these are derivative — they may add operational value but cannot substitute for substrate authority over the record.

**It does not claim that decisions cannot be revised.** Per A1.01, humans may revise substrate content, including decisions. What Category 2 commits to is that revisions themselves become substrate content — new decisions that supersede or amend earlier ones, with their own provenance — and that substrate's authority over the *complete revised record* holds. Revision does not create authority elsewhere.

## 4. What Category 2 is NOT — adjacent patterns it is commonly conflated with

Four patterns sit adjacent to Category 2 closely enough that conflation is common.

**Not audit-log-as-authoritative.** Some implementations treat runtime audit logs as the authoritative decision record, with substrate as a working state that may or may not match. This pattern fails Category 2 because authority sits in the audit logs — when the two disagree, the audit logs prevail. The pattern is operationally tempting in compliance-heavy deployments because audit-log infrastructure is regulatory-familiar, but it locates authority outside substrate.

**Not external-decision-logging-system-as-authoritative.** Some implementations use specialized decision-logging applications — governance platforms, decision-intelligence tools, regulatory repositories — as the authoritative record. The substrate may carry decision content, but the external system is positioned as the "official record" for organizational or compliance purposes. This pattern fails Category 2 because architectural authority resides in the external system.

**Not retroactive decision reconstruction.** Some implementations reconstruct decision history retroactively by analyzing substrate state changes, operational logs, or external-system activity, and treat the reconstructed history as authoritative. The reconstruction may be sophisticated and accurate in many cases, but its authority is over a derived inference rather than over decisions recorded *as decisions* at decision time per A2.36's atomic-with-content commitment.

**Not substrate-as-summary-of-external-decisions.** Some implementations record summaries — decision identifier, brief description, rough timestamp — in substrate while leaving full content (rationale, full authority chain, complete antecedent references) in external systems. The substrate's summary is not authoritative for the full decision; the external system is. The commitment is over the complete decision content per A2.40's six provenance fields, not over a substrate-resident pointer.

## 5. Why Category 2 is load-bearing for downstream commitments

Category 2 is not isolated; several other CKS commitments depend on it operationally.

The integrating source-of-truth commitment from A1.08 partitions into five categories per A2.42, and Category 2 is the temporal-history complement to Category 1's present-state authority. Without it, the source-of-truth commitment would be partial — substrate authoritative for the present but not for the past — and the partition would be incomplete on its temporal axis.

The path-retraceability commitment from A1.07 requires that decisions are substrate content (per A2.36) and that paths reconstruct from substrate alone (per A2.41). Category 2 makes substrate authoritative for the decision record retraceability traces through; without it, retraceability would trace through a record whose authority derives from external sources.

The conflict-as-first-class commitment from A1.03 treats conflict-resolution decisions as themselves decisions per A2.15. Category 2 makes resolution decisions substrate-authoritative; without it, conflict-handling decisions could legitimately be tracked in external conflict-management systems with authority over the resolution record.

The human-governed commitment from A1.01 grants humans rights to inspect, modify, and override substrate content at any time. Humans cannot exercise meaningful governance over a decision record they cannot authoritatively read from substrate. Category 2 makes the decision record architecturally authoritative for governance review; without it, override decisions would themselves be subject to disagreement with external sources.

The AI-as-substrate-mediator commitment from A1.04 includes Property A from A2.19 — the LLM reads from substrate as primary source. Category 2 makes substrate authoritative for the historical decisions the LLM may consult during cell execution; without it, the LLM could legitimately consult external authoritative decision sources, and substrate would lose its position as the primary source of decision-historical content.

## 6. Failure modes that violate the commitment

Ten anti-patterns each name a way an implementation can fail Category 2. Each is operationally observable.

**(a) Audit-log-primary architectures.** Runtime audit logs are the official decision record; substrate is operational but not authoritative when the two disagree.

**(b) External-decision-logging primary.** A specialized decision-logging application — governance platform, decision-intelligence tool, regulatory repository — is the authoritative record; substrate is a working interface that updates the external system.

**(c) Substrate-summary-external-detail.** Substrate carries decision summaries; external systems carry full content. Substrate is summary-authoritative but not detail-authoritative.

**(d) Retroactive reconstruction.** The decision record is reconstructed from state changes, operational logs, or external-system activity; authority is over the reconstruction, not over decisions as recorded at decision time per A2.36's atomic-with-content commit.

**(e) Decision-archival-to-external.** Recent decisions are in substrate; older decisions are archived to external retention systems and removed from substrate. Substrate authority is recency-bound; the complete history splits across substrate and external archives.

**(f) Compliance-system overrides.** Compliance reporting systems override substrate decisions when they disagree, typically for regulatory consistency. Substrate is overridden; the architectural commitment fails at the moment of override.

**(g) Decision-summary-displaces-detail.** Periodic processes compress substrate decisions into summary form, removing the original content. Substrate's authority is over the summary, not the original; complete-record authority fails through loss of detail.

**(h) External-decision-import.** The deployment imports decisions from external systems into substrate; the external systems remain authoritative for those decisions; substrate is downstream from external systems for that content.

**(i) Decision-record fragmentation.** Different categories of decisions are recorded in different systems — governance decisions in substrate, operational decisions in operational systems, compliance decisions in compliance platforms. Substrate authority is partial by category; the complete record fragments across systems.

**(j) Decision-revision-without-substrate-authority.** When humans revise decisions per A2.02 or A2.03, the revisions are recorded in external systems — document-management workflows, governance-tracking applications — rather than in substrate. The substrate's record of original decisions persists but is no longer authoritative because the revisions live elsewhere.

Each of (a)–(j) can be present in a deployment that otherwise satisfies many CKS commitments; each is sufficient to fail Category 2; and each is observable through the operational test in section 7.

## 7. Operational test

A system satisfies the Category 2 commitment if and only if all of the following are true at all times during the substrate's existence.

1. Queries about past decisions — what was decided, when, by whom, under what authority, with what rationale — are answered authoritatively from substrate per A2.36–A2.40.
2. The substrate carries the complete record of decisions the deployment has made: no selective summaries, no archived portions held externally, no summaries displacing details.
3. New decisions are committed to substrate first per A2.10's boundary crossings; external decision-tracking systems update downstream from substrate.
4. When substrate and external sources disagree on the decision record, the deployment resolves the disagreement in favor of substrate; the external source is corrected, not the substrate.
5. Decision revisions — humans modifying earlier decisions through their authority per A2.02 or A2.03 — are recorded in substrate as new decisions that supersede or amend earlier ones; substrate's authority over the revised record holds.
6. The decision record is queryable from substrate alone through standard read operations per A2.25 Requirement 2 and substrate-only paths per A2.41.

A system that fails any of (1)–(6) does not satisfy Category 2 in the architectural sense, even if its decision-record queries function operationally and even if the failure would be invisible in normal operation.

## Conclusion

Implementations under pressure to integrate with enterprise compliance infrastructure, leverage existing audit-log systems, or support sophisticated decision-tracking features drift toward decision authority being held in external systems. The drift is steady because external audit and compliance systems are operationally familiar, organizationally established, and often regulatory-mandated for specific decision categories. Implementations that drift produce systems where substrate carries decisions for operational purposes but external systems are authoritative for the decision record. The downstream consequences are audit failures (the substrate's record is not the official record for compliance), governance failures (humans cannot exercise meaningful governance over a record they cannot authoritatively access from substrate), retraceability failures (paths trace through substrate decisions but authoritative decisions live elsewhere), and source-of-truth fragmentation (substrate authoritative for the present per Category 1 but not for the past per failed Category 2).

The standalone formalization gives downstream implementers a precise specification of what substrate authority over the decision record requires, and the 2×2 in section 1 separates Category 2 from A2.36 — the path-retraceability commitment that decisions are substrate content — making substrate-resident-but-not-substrate-authoritative drift architecturally visible rather than implicit. Subsequent notes A2.45, A2.46, and A2.47 specialize the remaining three categories; A2.48 specializes the source-of-truth-versus-mirror-of-truth distinction; together they complete the decomposition of A1.08.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Category 2 — Substrate Authoritative for "What Was Decided": Standalone Treatment of Decision-History Authority in CKS.* May 4, 2026. ORCID: 0009-0004-8065-3235.
