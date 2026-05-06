# Source-of-Truth vs. Mirror-of-Truth: The Standalone Architectural Distinction in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the **source-of-truth vs. mirror-of-truth distinction** as a standalone architectural commitment — the load-bearing differentiation that determines whether a substrate is the architectural authority for the five categories of authoritative state, or a derivative view of authoritative state held elsewhere. This is the seventh and final note in the source-of-truth decomposition (with companion notes treating the integrating frame and the five category specializations).

## Abstract

The CKS pattern's substrate-as-source-of-truth commitment names the substrate as authoritative for five categories of state: what is the case, what was decided, what is in conflict, what rules apply, and who has what authority. Companion derivation notes formalize each category specialization and the integrating frame. This note formalizes a distinct architectural commitment underlying all five — the **direction of flow** between substrate and external systems. In source-of-truth, updates to authoritative content flow outward from substrate to derivative views in external systems; in mirror-of-truth, updates flow inward to substrate from external authoritative sources. The distinction is load-bearing because per-category authority claims can be made nominally — in documentation, runbooks, interface specifications — while the underlying flow direction operationally inverts the commitment. This note states the architectural commitment as four operational components, distinguishes it from operationally-similar patterns commonly conflated with it (eventual consistency, materialized views, write-through caches, event-sourcing projections, CQRS read models, change-data-capture pipelines), enumerates the failure modes that cause substrate to operate as mirror-of-truth even when nominally claiming source-of-truth status, and provides an operational test for whether a system's source-of-truth commitment is architecturally rigorous.

## 1. Why the source-of-truth vs. mirror-of-truth distinction needs to be formalized as standalone

The parent foundational note A1.08 commits to substrate as source of truth across five categories. The integrating-frame note A2.42 articulated the source-of-truth-vs-mirror-of-truth distinction at the integrating level. Notes A2.43 through A2.47 specialized each of the five categories, committing to substrate authority over what is the case, what was decided, what is in conflict, what rules apply, and who has what authority respectively. This note completes the decomposition by formalizing the underlying architectural distinction that makes those per-category commitments defensible *in principle*.

The motivating cases are deployments where substrate carries rich content but the architectural relationship between substrate and external systems is ambiguous about flow direction. Substrate may be treated as the source for some categories and a mirror for others; the flow direction may vary depending on which subsystem is interacting with substrate; or the flow direction may be documented as source-of-truth while operationally functioning as mirror-of-truth because external systems prevail in disagreements. Each pattern fragments the architectural commitment in ways that fail full source-of-truth, even when each individual per-category claim might pass a narrow inspection.

A second motivation is the strategic prior-art posture: the source-of-truth-vs-mirror-of-truth distinction forecloses architectures that nominally claim source-of-truth while operating as mirror-of-truth, and patentable derivations centered on substrate-as-derivative architectures — materialized-view governance, eventually-consistent substrate designs, change-data-capture-fed coordination layers — are substantially more defensibly contested when the distinction is publicly formalized as standalone.

A third motivation is the connection to migration safety from A1.05 and to substrate-only paths from A2.41. Source-of-truth substrates can migrate between hosts without breaking architectural commitments because the substrate is self-contained authority, and they support substrate-only paths because the substrate is authoritative for accountability questions. Mirror-of-truth substrates break both: their authority depends on external sources whose co-migration is not guaranteed, and authoritative answers require consulting external sources that the substrate merely reflects. The distinction is what makes both downstream properties architecturally coherent.

## 2. The source-of-truth commitment, defined precisely in contrast with mirror-of-truth

The source-of-truth commitment is an architectural commitment about the **direction of flow** between substrate and external systems for content in the five categories named in A2.43–A2.47. The commitment has four operational components, each of which differs from its mirror-of-truth equivalent.

**(a) Authority direction.** In source-of-truth, substrate is the architectural authority for the five categories; when substrate and external sources disagree, substrate prevails. In mirror-of-truth, external sources are the authority and prevail in disagreements. The architectural commitment is to substrate as the resolver — disagreement-resolution flows in favor of substrate.

**(b) Update direction.** In source-of-truth, updates to authoritative content occur in substrate first; derivative views in external systems update downstream from substrate. In mirror-of-truth, updates occur in external systems first; substrate updates downstream from them. The architectural commitment is to substrate-first updates — substrate is the writer's destination, not a downstream consumer.

**(c) Failure semantics.** In source-of-truth, external-system failures do not affect substrate authority; substrate remains authoritative for the five categories even when external systems are unavailable. In mirror-of-truth, external-system failures leave substrate stale or unable to receive updates. The architectural commitment is to failure-independent substrate authority.

**(d) Migration semantics.** In source-of-truth, migrating substrate to a new host (per A1.05's three minimal requirements) preserves substrate authority on the new host without requiring co-migration of external systems. In mirror-of-truth, migrating substrate without co-migrating external authoritative sources produces a substrate that is authoritatively empty or stale on the new host. The architectural commitment is to migration-coherent substrate authority.

The four components together define the source-of-truth commitment architecturally. A system that satisfies fewer than four cannot reliably claim source-of-truth status: such a system is a hybrid that operates as source-of-truth on some axes and mirror-of-truth on others, which is itself architectural ambiguity rather than a degraded form of source-of-truth.

## 3. What the source-of-truth commitment does NOT claim

The standalone treatment is not a maximalist treatment. Stating precisely what the commitment does not claim keeps the standalone framing from drifting into something stronger than the source paper supports.

**It does not forbid external systems.** Deployments may have rich derivative views — search indexes, dashboards, analytics platforms, business intelligence tools, integration systems — that derive from substrate. The commitment is about flow direction (substrate-outward to derivative views, not substrate-inward from authoritative sources), not about external-system absence.

**It does not claim that substrate is performance-optimal.** Source-of-truth substrate may be slower than performance-optimized derivative views for full-text search, complex analytics, geospatial queries, or high-throughput aggregations. Deployments may use derivative views for performance while preserving source-of-truth substrate authority over the five categories.

**It does not require substrate to carry all content related to the deployment.** The commitment is to substrate authority over the five categories specifically. Operational telemetry, infrastructure metrics, business analytics, log streams, and many other categories may live in external systems without being derivative of substrate.

**It does not preclude substrate from carrying mirror-of-truth derivations of non-five-category content.** A deployment may pull observability metrics, business-analytics summaries, or external reference data into substrate for context, with the authoritative source for that content remaining external. Such substrate-resident mirrors are compatible with source-of-truth provided the five categories themselves are not mirrored from external authority. The commitment scopes specifically to the five categories.

**It does not specify external-system architectures.** Derivative views may be implemented as caches, materialized views, search indexes, data warehouses, lakehouses, event streams, or any other form the deployment supports. The commitment is to their derivative status (downstream from substrate), not to specific architectural choices.

**It does not claim that substrate content is metaphysically correct.** Substrate is architecturally authoritative for the five categories — disagreements are resolved in its favor — but its content can be wrong, outdated, or in need of revision. Humans exercising the modify and override rights from A1.01 may revise substrate based on knowledge from external sources. The commitment is to substrate authority over the *questions*, not to substrate content being beyond revision.

## 4. What the distinction is NOT

Six operationally-similar patterns are commonly conflated with the source-of-truth commitment. Each is a real and reasonable design pattern in some other architecture; naming what the distinction is *not* prevents the misreading.

**Not eventual consistency.** Distributed-systems eventual consistency may produce substrate-and-external-system disagreement during synchronization windows, but eventual consistency itself is neither source-of-truth nor mirror-of-truth — the distinction is determined by how disagreements resolve once synchronization completes. If substrate eventually prevails, the commitment holds; if external systems eventually prevail, it fails. Eventual consistency is an operational property of timing; source-of-truth is an architectural commitment about authority direction.

**Not materialized views.** Materialized views in databases or data systems are derivative projections of authoritative state held in base tables. A substrate organized as a materialized view — including the special case of a primary-replica replication target where substrate is the replica — is inherently mirror-of-truth: it is a derivation, with the base tables as authoritative source. Source-of-truth substrate is itself the base from which materialized views in external systems may be derived.

**Not write-through caches.** Write-through caches ensure that writes to the cache propagate to authoritative storage, with the cache as a fast-access layer over authoritative state. A substrate operating as a write-through cache is mirror-of-truth — the authoritative state is the storage behind the cache. Source-of-truth substrate is itself the authoritative storage, not a fast-access projection over storage held elsewhere.

**Not event-sourcing projections.** Event-sourcing systems materialize current state as projections from event streams; the events are authoritative, and projections (including substrate-shaped projections) are derivative. A substrate materialized from an event stream is mirror-of-truth. Source-of-truth substrate may emit events as derivative outputs to downstream observers, but does not derive from events held elsewhere.

**Not the read model in CQRS.** Command-query responsibility segregation separates write models (authoritative for state changes) from read models (optimized projections of write-model state). A substrate cast as a CQRS read model is mirror-of-truth — the write model is the authoritative source. Source-of-truth substrate may itself function as the write model, with CQRS-style read models in external systems as derivative views; what it cannot do is occupy the read-model role and still satisfy the commitment. The pattern is widespread and easily misapplied because the read-model framing makes substrate look like a substrate while remaining derivative in flow.

**Not the target of change-data-capture pipelines.** CDC streams transactional changes from authoritative source systems — databases, transaction logs, application stores — to downstream consumers. A substrate populated by CDC streams from external authoritative systems is mirror-of-truth: substrate is a downstream consumer. Source-of-truth substrate may be the *origin* of a CDC stream emitted to external consumers; it cannot be the *destination* of a CDC stream from external authoritative sources and still satisfy the commitment. Federated-query and data-virtualization patterns where substrate resolves reads against external authoritative sources at query time are a particularly pure form of mirror-of-truth in this family — there is no persistent substrate state at all, only a virtualization layer over authoritative sources held elsewhere.

## 5. Why the distinction is load-bearing for downstream commitments

The source-of-truth-vs-mirror-of-truth distinction is load-bearing for several CKS commitments. For the integrating source-of-truth commitment from A1.08, the distinction is the architectural differentiation that makes substrate authority defensible in principle; without it, the commitment could be nominally claimed while operationally violated. For the five category specializations from A2.43–A2.47, the distinction is the architectural foundation that makes per-category authority defensible: each specialization commits to substrate authority over its specific content, but the per-category claim is only defensible if the underlying flow direction is substrate-outward.

For the migration-safety property from A1.05 and the substrate-only-paths property from A2.41, the distinction is what makes those properties architecturally coherent. Source-of-truth substrate can migrate cleanly because it is self-contained authority, and it supports substrate-only paths because it is authoritative for accountability questions. Mirror-of-truth substrate breaks both: migration depends on external sources whose co-migration is not guaranteed, and authoritative answers require consulting external sources rather than substrate alone.

For the architectural-property qualifier from A2.06 and non-specialist governance from A1.11, the distinction is what keeps both architectural rather than procedural. Source-of-truth substrate is the architectural authority, and it is self-contained authority that commodity tools can interface with directly. Mirror-of-truth substrate makes authority depend on synchronization processes that may fail, be bypassed, or be reconfigured — converting governance from architectural to procedural — and requires interfacing with the external authoritative sources rather than substrate alone, breaking commodity-tool sufficiency.

## 6. Failure modes that violate the distinction

Each of the following anti-patterns names a way an implementation can fail the architectural commitment to source-of-truth by causing substrate to operate as mirror-of-truth, even when the implementation nominally claims source-of-truth status.

**(a) External-system-precedence.** When substrate and external systems disagree, the deployment resolves in favor of external systems. The flow direction is inverted — substrate operates as mirror.

**(b) Substrate-as-write-through-cache.** Substrate operates as a fast-access cache over authoritative storage held in external systems. Writes propagate from substrate to the storage, but the storage is the authority for persistence and disagreement resolution.

**(c) Substrate-as-materialized-view.** Substrate is materialized from external authoritative state through a projection process. Updates to the projection occur when source state changes; substrate is downstream.

**(d) Substrate-as-event-sourcing-projection.** Substrate is a projection materialized from external event streams. The events are authoritative; substrate is one possible projection.

**(e) External-driven substrate updates.** Substrate updates are triggered exclusively by external systems through CDC pipelines, ETL jobs, or integration adapters. The deployment does not write directly to substrate but writes to external systems that propagate updates to substrate.

**(f) Substrate-as-snapshot-of-authoritative-state.** Substrate is periodically refreshed from external authoritative state through snapshot processes. Between snapshots, substrate may be stale; authoritative state lives in the source.

**(g) Bidirectional-synchronization-without-primacy.** Substrate and external systems exchange updates bidirectionally with no architectural primacy. Conflicts are resolved by latest-write or by manual reconciliation, with no commitment to substrate prevailing. Authority is shared rather than substrate-resident.

**(h) Mirror-of-truth-with-source-of-truth-claims.** The deployment documents the architecture as source-of-truth but operationally functions as mirror-of-truth — runbooks describe substrate as authoritative while operational practice resolves disagreements in favor of external systems. Architectural claim and operational practice diverge.

**(i) Per-category-mixed-flow.** Substrate is source-of-truth for some of the five categories (e.g., decisions) but mirror-of-truth for others (e.g., authority structure synchronized from an external identity provider, or rules synchronized from an external policy engine). The commitment to substrate as authority is partial.

**(j) External-write-on-failure-fallback.** Substrate operates as source-of-truth in normal conditions, but when substrate is unavailable, writes go to external systems that later propagate to substrate when it returns. The fallback path makes external systems authoritative for the failure window.

## 7. Operational test

A system satisfies the source-of-truth commitment over mirror-of-truth if and only if all of the following are true at all times during the substrate's existence.

1. **Authority direction is substrate.** When substrate and external sources disagree on any of the five categories per A2.43–A2.47, the deployment resolves disagreements in favor of substrate.

2. **Update direction is substrate-first.** Updates to authoritative content for the five categories are committed to substrate before propagating to external derivative views.

3. **Failure semantics preserve substrate authority.** When external systems are unavailable, substrate remains architecturally authoritative for the five categories; the deployment can continue to read from and write to substrate without external systems being operational.

4. **Migration semantics preserve substrate authority.** Substrate moved to a new host (satisfying A1.05's three minimal requirements) is architecturally authoritative on the new host without co-migration of external systems.

5. **Architectural claim and operational practice align.** Documentation that claims source-of-truth status is consistent with operational practice — disagreements are resolved in substrate's favor, updates flow substrate-outward, and external systems function as derivative views.

A system that fails any of (1)–(5) does not satisfy the source-of-truth commitment in the architectural sense, even if it nominally claims source-of-truth status.

## 8. Why naming the distinction as standalone matters

Implementations under pressure to integrate with enterprise systems, leverage existing infrastructure, or optimize for performance consistently drift toward mirror-of-truth patterns where substrate becomes a derivative view of authoritative state held elsewhere. The drift is steady because external systems are operationally familiar, well-tooled, and organizationally established for the data categories they traditionally manage. The path of least resistance for an implementer asked to add a CKS-style coordination layer to an existing deployment is to feed it from existing systems-of-record via CDC, ETL, or event-driven projection — producing a substrate that is operationally a mirror, even when the design document calls it a source. The downstream consequences manifest as authority ambiguity (which system is consulted for authoritative answers depends on which subsystem is asking), migration failures (substrate cannot be migrated cleanly because external authoritative sources are not co-migrated), substrate-only-paths failures (paths require consulting external sources for authoritative answers), and architectural-property failures (governance becomes procedural because substrate authority depends on synchronization processes that may fail).

Naming the source-of-truth-vs-mirror-of-truth distinction as a standalone architectural commitment — with the four components specified in §2, the limitations clarified in §3, the six operationally-similar pattern distinctions in §4, the load-bearing connections in §5, the ten failure modes in §6, and the five-criterion operational test in §7 — gives downstream implementers a precise specification of what the architectural commitment requires.

With this note complete and its companions A2.42 through A2.47 already drafted, the source-of-truth decomposition is fully formalized. The integrating frame established the five-category structure; the five category specializations formalized substrate authority for each category; this distinction closes the decomposition with the architectural differentiation that makes substrate authority defensible in principle. Together the seven notes constitute the operational decomposition of A1.08's substrate-as-source-of-truth commitment.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Source-of-Truth vs. Mirror-of-Truth: The Standalone Architectural Distinction in the Coordination Knowledge Substrate Pattern.* May 5, 2026. ORCID: 0009-0004-8065-3235.
