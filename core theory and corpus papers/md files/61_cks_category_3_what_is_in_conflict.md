# Category 3 — Substrate Authoritative for "What Is in Conflict": Standalone Treatment of Conflict-State Authority in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize Category 3 of the substrate-as-source-of-truth commitment — the substrate's architectural authority for *what is in conflict* — as a standalone commitment with independent operational content, separable from the four sibling categories with which it composes.

## Abstract

The CKS pattern's substrate-as-source-of-truth commitment names five categories of state for which the substrate is architecturally authoritative. This note formalizes the third — substrate authoritative for *what is in conflict*, that is, for the contradiction state the deployment recognizes as first-class substrate content — as having independent architectural content separable from the other four. The category is closely paired with, but distinct from, the conflict-as-first-class commitment: that commitment requires contradictions to be preserved as substrate state; this category requires the substrate to be the architectural authority over the resulting conflict record. The two compose. This note states the four operational components of the commitment, distinguishes Category 3 from four adjacent patterns commonly conflated with it, names ten failure modes — three at expanded length — and provides an operational test for whether a system's conflict-state authority is CKS-coherent specifically.

## 1. Why Category 3 needs to be formalized as standalone

The CKS pattern commits to the substrate being the architectural source of truth for coordination state across five categories, named canonically in §11.1 and developed across §11.2 (source-of-truth-vs-mirror-of-truth) and §11.3 (path retraceability as operationalization). The parent foundational note formalizes the joint commitment; the integrating-frame note formalizes the five-category structure. The first two specialization notes formalize Category 1 (*what is the case*) and Category 2 (*what was decided*). This note does the same for Category 3.

The motivating cases are deployments where contradictions exist in substrate but external systems are treated as authoritative for the conflict record: substrates preserve contradictions per the conflict-as-first-class commitment but external dispute-management systems are queried for status, ownership, or escalation; substrates record cell-level resolutions but external audit systems are treated as the authoritative resolution record; substrates carry conflict content but external data-quality dashboards are treated as the source for inconsistency analysis. Without an explicit Category 3 treatment, such deployments can be described as "conflict-preserving" — they satisfy substrate-level preservation per §5.1 — while still failing to make the substrate authoritative for the conflict record, and the architectural failure has no portable name. A second motivation is the prior-art posture: substrate authority over conflict state forecloses architectures where substrate is the working store while external systems are the official conflict record, and patentable derivations focused on conflict-tracking, dispute-resolution, or inconsistency-management patterns are more defensibly contested when Category 3 is publicly formalized as standalone.

**The conflict-as-first-class commitment commits to preservation; Category 3 commits to authority.** The two are easily conflated, and the distinction is foundational for the standalone claim. The conflict-as-first-class commitment from §5 commits to contradictions being preserved as substrate state — to *where conflicts live*. Its decomposition specifies substrate-level preservation per §5.1, cell-level resolution under orchestration rules per §5.2, the two-level coupling between them, and the four conflict-specific provenance fields (writer, timestamp, rationale where applicable, relationship to contradicting content) per §5.3. Category 3 commits to something different: that the substrate is the architectural authority over the resulting conflict record — that is, to *whose answer counts* when something asks what is in conflict. A deployment can satisfy the conflict-preservation commitment in full and still fail Category 3 if an external system is treated as the official conflict-status record when it disagrees with substrate. The two compose: conflicts must be preserved in substrate **and** the substrate must be authoritative for the conflict record. This note formalizes the second; it presupposes the first and does not re-derive it.

## 2. The Category 3 commitment, defined precisely

In the CKS pattern, the substrate is **authoritative for what is in conflict** if and only if the following four operational components hold across the full conflict record at all times during the substrate's existence.

**(a) The substrate is the architectural answer to conflict-state queries.** For queries about the deployment's conflict state — what content contradicts what other content, what the relationship between contradicting content is, how a conflict was resolved at a cell, what conflicts remain unresolved at substrate level — the architectural answer is the substrate's record per the conflict-as-first-class commitment and its decomposition. External systems may be consulted for visualization, analysis, or operational convenience, but the substrate's answer is the authoritative answer.

**(b) Conflict state is substrate content.** The substrate carries the complete record of conflicts the deployment recognizes as first-class state — substrate-level preserved contradictions per §5.1, cell-level resolutions per §5.2, and the conflict-specific provenance per §5.3. No selective subset, no summary representation held outside, no relationship metadata external to substrate.

**(c) New conflicts and resolutions are committed to substrate first.** When the deployment recognizes contradicting content as a first-class conflict, the conflict is preserved in substrate with the four conflict-specific provenance fields per §5.3 alongside the broader six-field provenance per §3.1. External conflict-tracking systems, if present, update downstream from substrate. New cell-level resolutions per §5.2 are committed to substrate — as new substrate content layered over the contradicting content — before any external resolution-tracking system is updated.

**(d) Substrate prevails on disagreement.** When the substrate's conflict record and an external source's conflict record disagree on relationship characterization, resolution outcome, provenance, or ownership, the architectural commitment is to update the external source to match substrate, not to update substrate to match the external source. Substrate authority is not contingent on external agreement.

The four components together define the commitment architecturally. A system satisfying fewer than four cannot reliably claim Category 3 authority, because each component closes one path along which authority can drift to external sources.

## 3. What the commitment does NOT claim

Stating precisely what the commitment does not claim keeps the standalone framing from drifting into something stronger than the source paper supports.

**Not authority over inconsistencies the deployment does not recognize as conflicts.** Operational inconsistencies — data-quality issues, integration mismatches, format discrepancies — that the deployment has not raised to first-class conflict status are not Category 3 content.

**Not all-contradictions-as-first-class.** Some contradictions may be handled at deployment layer through filtering, normalization, or human review outside substrate. The commitment is to substrate authority over what is treated as first-class conflict, not to elevating every contradiction to that status.

**Not automatic conflict resolution.** Conflicts may be resolved at cell level under orchestration rules, escalated to humans for direct override, or remain preserved indefinitely. The commitment is to substrate authority over the conflict state regardless of how each conflict is handled.

**Not a specification of conflict-detection mechanisms.** How the deployment detects contradictions is a deployment concern.

**Not a requirement that external conflict-tracking systems be absent.** Deployments may have dispute-management applications, data-quality dashboards, or conflict-visualization tools as derivative systems. Removing them is not a CKS requirement; subordinating them to substrate is.

**Not a specification of retention duration.** Category 3 authority holds for as long as the substrate carries the conflicts.

## 4. What the commitment is NOT

Four adjacent patterns are commonly conflated with Category 3 authority. Each is reasonable in some other architecture; naming what Category 3 is not prevents the misreading.

**Not conflict tracking in external dispute-management systems.** Some implementations preserve contradictions in substrate but use external dispute-management applications as the official conflict-status record — tracking status, escalation, ownership, and SLA state externally while the substrate carries content as a working store. This pattern fails Category 3 because authority is split — substrate for content, external systems for status — and a conflict's status is part of its first-class substrate identity per the conflict-preservation commitment.

**Not inconsistency monitoring as authoritative.** Some implementations treat data-quality monitoring tools as the authoritative inconsistency record; when the monitoring system disagrees with substrate, it prevails because it is "the data quality system." This pattern fails Category 3 because conflicts the substrate preserves are subordinated to external monitoring whose authority derives from organizational convention rather than from architectural commitment.

**Not conflict reconciliation in eventually-consistent systems.** Some implementations operate substrate within a broader eventually-consistent architecture where conflicts arise from concurrent updates and are reconciled by the underlying consistency mechanism — last-writer-wins, vector-clock merging, CRDT collapse. Substrate-level contradictions appear briefly during eventual-consistency windows but are dissolved by infrastructure before promotion to first-class state. This pattern fails Category 3 because substrate authority is overridden by infrastructure-layer reconciliation that does not honor the conflict-as-first-class commitment.

**Not conflict suppression that erases the contradiction.** Some implementations resolve conflicts by removing one of the contradicting positions from substrate, treating the resolution as the new authoritative state with no record of the prior contradiction. This pattern fails Category 3 because conflict state is erased rather than preserved per §5.1; substrate authority over the conflict record is replaced by substrate authority over the resolved state alone.

## 5. Why Category 3 is load-bearing for downstream commitments

Category 3 standalone treatment makes visible its load-bearing role across several CKS commitments. The integrating source-of-truth commitment relies on it: substrate authority for current state and for past decisions does not by itself produce substrate authority over contradictions; without Category 3, the source-of-truth commitment would be partial. The conflict-as-first-class commitment relies on it: §5 commits to contradictions being preserved as first-class state with full provenance, but Category 3 closes the loop by making the substrate the architectural authority over the record, not merely the location of it. The two-level coupling between substrate-level preservation per §5.1 and cell-level resolution per §5.2 relies on it: the coupling holds substrate-residentially, and Category 3 makes substrate authoritative for both halves, foreclosing implementations that place preservation in substrate but treat resolutions as external operational records. The path-retraceability commitment from §3.1 relies on it: a path that traces through a conflict resolution traces through substrate-authoritative content rather than through references whose authoritative version sits elsewhere. The human-governed commitment from §2.1 and §2.3 relies on it: humans cannot exercise meaningful governance over conflicts they cannot authoritatively read, and the three rights — to inspect, to modify, to override — apply to substrate content; Category 3 makes the conflict record substrate content authoritatively, not by convention.

## 6. Failure modes that violate the commitment

A system can fail Category 3 specifically, even when it satisfies the four sibling categories and broader CKS commitments. Ten failure modes name the most common ways this happens. Three — external-dispute-management-primary, data-quality-system-overrides, and conflict-aggregation-overrides — recur in deployments integrated with enterprise compliance and data-quality infrastructure, and are treated at expanded length below.

**(a) External-dispute-management-primary.** The deployment treats an external dispute-management system — an enterprise ticketing platform, a regulatory-compliance dispute portal, a vendor-supplied dispute-resolution application — as the official conflict-status record. The substrate carries contradiction content per the conflict-preservation commitment, but the dispute-management system is queried as authoritative for whether the conflict is open, who owns it, what resolution is pending, and what the escalation history is. The pattern is particularly common where compliance regimes require specific dispute-tracking platforms or where organizational practice has accumulated around an enterprise system that predates the substrate. The architectural failure is precise: the substrate is treated as the working store and the external system as the authority, inverting what Category 3 requires.

**(b) Data-quality-system-overrides.** A data-quality monitoring system — a profiling tool, a master-data-management platform, an inconsistency-reporting dashboard — is treated as authoritative for inconsistency detection and tracking. When the monitoring system disagrees with substrate about whether a conflict exists, what its severity is, or how it relates to other inconsistencies, the monitoring system prevails. The pattern is particularly common in deployments with mature data-quality infrastructure that predates the substrate, where the data-quality team is organizationally responsible for inconsistency reporting and the substrate is treated as one source the team monitors among others. The architectural failure is precise: the deployment recognizes some inconsistencies as first-class conflicts in substrate per the conflict-preservation commitment, but the monitoring system is then treated as authoritative for those same conflicts because it is the system whose reports are read and acted on.

**(c) Eventually-consistent reconciliation.** Concurrent updates produce conflicts that are reconciled automatically by the underlying consistency infrastructure, overriding the substrate's first-class commitment. Substrate-level contradictions briefly appear during eventual-consistency windows but are dissolved by infrastructure before they can be promoted to first-class state.

**(d) Conflict suppression.** Resolutions remove contradicting positions from substrate, erasing the conflict record. Substrate authority is over the resolved state alone, not over the conflict that produced the resolution.

**(e) Cell-level-resolution-external-record.** Cell-level resolutions per §5.2 occur in substrate but are recorded externally for audit purposes; the external record is treated as authoritative for the resolution decision.

**(f) Substrate-summary-external-detail.** Substrate carries conflict summaries; external conflict-tracking systems carry full conflict details. The substrate is summary-authoritative but not detail-authoritative.

**(g) Conflict-archival-external.** Recent conflicts are in substrate; old conflicts are archived to external systems. Substrate authority is recency-bound and fails for the archived portion of the conflict record.

**(h) Relationship-metadata-external.** Substrate carries the contradicting content but the relationship metadata per §5.3 lives in external systems. Substrate authority for the contradiction itself fails because the relationship — what makes the contradiction a conflict per the conflict-preservation commitment — is external.

**(i) Resolution-provenance-external.** Cell-level resolutions occur in substrate but the resolution provenance per §5.3 lives externally. Substrate authority over the resolution decision is technically present but the supporting provenance is fragmented.

**(j) Conflict-aggregation-overrides.** Aggregation processes combine multiple conflicts into composite records — *issues*, *incidents*, *patterns* — held in external systems treated as authoritative for the aggregate. Substrate's authority over individual conflicts is subordinated to external authority over their aggregations. The pattern is particularly common in deployments where executive reporting, regulatory disclosure, or risk-management workflows operate on aggregated conflict views, and where the aggregation system has accumulated the organizational role of "the conflict view that is acted on." The architectural failure is subtler than (a) and (b) but equivalent in consequence: individual conflicts in substrate are authoritative on paper, but the aggregate view that drives action lives elsewhere, and disagreements between substrate-derived aggregates and the external aggregate authority resolve in favor of the external system.

A system exhibiting any of (a)–(j) does not satisfy Category 3 in the architectural sense, even if its conflict-tracking functions operationally.

## 7. Operational test

A system satisfies the Category 3 commitment if and only if all of the following are true at all times during the substrate's existence:

1. Queries about the conflict record are answered authoritatively from substrate per the conflict-as-first-class commitment and its decomposition.
2. The substrate carries the complete record of conflicts the deployment recognizes per the conflict-preservation commitment; no selective summaries, no archived portions held externally, no relationship metadata external to substrate.
3. New conflicts and cell-level resolutions are committed to substrate first; external conflict-tracking systems update downstream from substrate, not the other way around.
4. When substrate and external sources disagree on the conflict record, the deployment resolves the disagreement in favor of substrate.
5. Conflict suppression — resolution by erasing the contradicting content — is forbidden; resolutions update the substrate with new content layered over the contradicting content while preserving the conflict record per substrate-level preservation.
6. The conflict record is queryable from substrate alone through standard read operations, without depending on external services to render any portion of it.

A system that fails any of (1)–(6) does not satisfy the Category 3 commitment in the architectural sense, even if its conflict-tracking functions operationally and even if the four sibling categories are satisfied.

## 8. Conclusion

Implementations under pressure to integrate with enterprise dispute-management systems, leverage existing data-quality infrastructure, or support sophisticated conflict-analysis features consistently drift toward conflict authority being held in external systems. The drift is steady because external systems are operationally familiar and often required by compliance regimes, and it is invisible at the conflict-preservation layer: substrates that preserve contradictions in full, with full provenance, can satisfy the conflict-as-first-class commitment while still failing Category 3 because the authoritative answer to *what is in conflict* sits elsewhere.

Naming Category 3 as a standalone architectural commitment gives downstream implementers a precise specification of what substrate authority over conflict state requires. The integrating-frame note treats the joint five-category commitment; the Category 1 and Category 2 specialization notes treat the present-state and decision categories; the subsequent specialization notes treat Category 4 (rules) and Category 5 (authority structure); a final note treats the source-of-truth-vs-mirror-of-truth distinction. Together they formalize the source-of-truth commitment from §11 across the full decomposition.

Subsequent work that adopts, extends, composes, or argues against the CKS source-of-truth commitment in its conflict-state dimension should use Category 3 in the sense formalized here. Subsequent work that uses substrate authority over conflict state differently is using a different commitment, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Category 3 — Substrate Authoritative for "What Is in Conflict": Standalone Treatment of Conflict-State Authority in CKS.* May 4, 2026. ORCID: 0009-0004-8065-3235.
