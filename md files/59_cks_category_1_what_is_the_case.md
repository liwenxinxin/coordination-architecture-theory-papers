# Category 1 — Substrate Authoritative for "What Is the Case": Standalone Treatment of Current-State Authority in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the first of the five authoritative categories named by the source paper's substrate-as-source-of-truth commitment — the substrate's authority for **what is the case** about coordination state at the present moment — as a standalone architectural commitment with independent operational content, separable from the other four categories with which it composes.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern's substrate-as-source-of-truth commitment names five categories of authoritative state, framed jointly in a separate integrating-frame note. This note formalizes the first — **Category 1: substrate authoritative for "what is the case"** — as a commitment with independent operational content that can be defended, implemented, and tested independently of the other four. The motivation is that current-state queries are the most operationally pervasive class of substrate read in any CKS deployment: nearly every coordination question — the status of this entity, the value of this property, the relationships in this scope — is a current-state query. Implementations under pressure to integrate with enterprise operational systems consistently drift toward architectures in which substrate carries history while external systems carry the live operational state, fragmenting authority in ways that fail the commitment. The note states the four operational components of the Category 1 commitment, distinguishes it from four adjacent patterns commonly conflated with it (cache, denormalization, event-stream projection, periodic snapshot), names the load-bearing connections to other CKS commitments, enumerates ten failure modes, and provides an operational test for whether a system implements current-state authority in the CKS sense.

## 1. Why Category 1 needs to be formalized as standalone

The CKS pattern's parent commitment to substrate-as-source-of-truth (A1.08) names five categories of authoritative state for which the substrate is the architectural answer. The integrating-frame treatment (A2.42) establishes the five-category structure and the source-of-truth-vs-mirror-of-truth distinction that gives the commitment its operational content. This note specializes Category 1 — the substrate's authority for current coordination state, the answer to "what is the case" about any coordination object the deployment maintains — as a standalone commitment.

Three motivations make the standalone treatment load-bearing.

The first is **operational pervasiveness**. Of the five categories, Category 1 carries the most operational weight by a wide margin, because nearly every read query against the substrate is a current-state query. A reader asks the status of an entity, the value of a property, the relationships in a scope — these are all Category 1 queries. Categories 2–5 (decision history, conflicts, rule applicability, authority assignments) are queried less frequently in normal operation; Category 1 is queried continuously. A failure that touches Category 1 affects nearly every query the deployment serves; a failure that touches Category 4 affects only the rule-applicability queries.

The second is the **drift profile in real deployments**. Implementations under pressure to integrate with enterprise operational systems consistently drift toward architectures in which the substrate is governance-authoritative for archival or audit purposes while external systems are operationally authoritative for live state. The drift is steady because external operational systems are typically high-performance, organizationally established as authoritative for the operational concerns they were built for, and familiar to operators in ways the substrate is not. A standalone formalization of Category 1 makes this drift architecturally visible at design time rather than at the moment two observers reading what each takes to be the authoritative source disagree about current state.

The third is the **strategic prior-art posture**. The architectural commitment to substrate authority for current state is consequential prior art: it forecloses architectures in which substrate is treated as a record of past coordination decisions while external systems are treated as the source for current operational state — exactly the pattern toward which deployments drift. Patentable derivations focused on coordination-state architectures, current-state-management patterns, or operational-state authority are substantially more defensibly contested when Category 1 is publicly formalized as standalone.

## 2. The Category 1 commitment, defined precisely

In the CKS pattern, the substrate is **authoritative for what is the case** when the following four operational components hold for the coordination state the deployment maintains in substrate.

**(a) The substrate is the architectural answer to current-state queries.** For any query about the present state of a coordination object the deployment maintains in substrate — entity status, property values, relationships within substrate scope — the architectural answer is the substrate's current content. External systems may be consulted for performance or convenience, but the substrate's answer is the authoritative answer.

**(b) Current state is substrate content.** The substrate carries the coordination state in addressable form per A2.08's foundational substrate commitments. Queries about state operate over substrate content directly, not over external derivations of substrate content. The state lives in substrate, not behind it (in operational systems the substrate is a view of) and not in front of it (in caches the substrate is the slow-path answer to). Substrate content *is* the current state, architecturally.

**(c) Updates to current state occur in substrate first.** When the deployment changes coordination state — through cell execution under orchestration rules, through direct human override per A2.03, or through rule authoring per A2.02 — the change is committed to substrate per A2.10's boundary-crossings discipline. Derivative views in external systems are updated downstream from substrate. Updates that bypass substrate (writing to external systems first, then propagating to substrate) violate the commitment because they make the external systems the authoritative writer.

**(d) Disagreements between substrate and external sources are resolved in favor of substrate.** When substrate's current state and external systems' representations of the same coordination content disagree, the substrate prevails. Disagreement may be resolved by updating external sources to match substrate, by treating external sources as stale, or by flagging external systems as out-of-sync; what the architecture forbids is treating external sources as authoritative and updating substrate to match them for the substrate's own coordination state.

The four components together define the commitment. A system that satisfies fewer than four cannot reliably claim Category 1 authority architecturally, regardless of how its current-state queries appear to function operationally.

## 3. What the commitment does NOT claim

The standalone treatment of Category 1 is not maximalist. Stating precisely what the commitment does not claim is what keeps the standalone framing from drifting into something stronger than the source paper supports.

**It does not claim substrate authority over external-system state.** The substrate is authoritative for the coordination state it maintains; external systems remain authoritative for their own state. A deployment may have an HR system carrying employee records; the HR system is authoritative for those records, not the substrate. If the substrate carries employee references for coordination purposes, the references are derivative, and the HR system prevails on employee state. The architectural commitment is about substrate authority for substrate-resident state, not about substrate authority over all content the substrate happens to reference.

**It does not require all coordination-relevant data to live in substrate.** Operational telemetry, infrastructure state, business analytics, and other categories may legitimately live in external systems. The substrate is authoritative for coordination state — the state the deployment maintains for coordination purposes — not for all data that touches coordination at any layer.

**It does not claim substrate omniscience.** The substrate's current state may be incomplete, outdated, or erroneous. Humans exercising the modify and override rights per A2.02 and A2.03 may revise substrate based on knowledge from external sources. The commitment is to substrate authority for the questions the commitment names, not to substrate content being beyond revision.

**It does not specify update mechanisms.** How substrate is updated — cell writes under orchestration rules, direct human writes, batch ingest, streaming integrations — is a deployment concern. The architectural commitment is to substrate being the authoritative writer for its own current state, not to specific update mechanics.

**It does not constrain external-system architectures.** External systems may be highly sophisticated, real-time, distributed, or eventually-consistent in their own right. The commitment governs their relationship to substrate for the five authoritative categories; it does not constrain their internal designs.

## 4. What the commitment is NOT

Four adjacent patterns are commonly conflated with the Category 1 commitment. Each is a real architecture in some other context; naming what the commitment is not prevents the misreading.

**Not substrate as cache of operational state.** Some implementations treat the substrate as a cache that captures snapshots of operational state held authoritatively in external systems. Reads return cached values; the live authoritative state lives in the operational systems, and substrate updates are batch refreshes from those systems. This pattern fails the commitment because substrate is derivative — when substrate and operational systems disagree, the operational systems prevail by design.

**Not substrate as denormalization of database state.** Some implementations treat the substrate as a denormalized read-model over normalized state held in external databases. The normalized databases are the authoritative source; the substrate is a read-optimized projection. This pattern fails the commitment because substrate authority is read-only and derivative; writes go to the normalized stores first, and substrate is rebuilt downstream.

**Not substrate as projection of event streams.** Some implementations treat the substrate as a projection materialized from event streams held in external messaging infrastructure. The event streams are authoritative; substrate is one projection of the events among several possible. This pattern fails the commitment because the events are the source. (This is the architectural commitment that distinguishes a CKS substrate from a CQRS read-model.)

**Not substrate as snapshot of authoritative state.** Some implementations treat the substrate as a periodic snapshot of state held authoritatively elsewhere, refreshed nightly or on-demand. The snapshots may be useful for governance, audit, or analysis, but they are not the source. This pattern fails the commitment because substrate authority is snapshot-bound; the live state is elsewhere, and substrate lags by the snapshot cadence.

The four distinctions together preserve the commitment's precision: the substrate is the live authoritative source for current coordination state, not a derivative artifact built downstream from authority that lives in some other system.

## 5. Why Category 1 is load-bearing for other CKS commitments

The Category 1 commitment is not isolated. Several CKS commitments depend on it specifically.

**The integrating source-of-truth commitment from A1.08.** Category 1 is the most operationally pervasive of the five categories because nearly every coordination query is a current-state query. Without it, the source-of-truth commitment would be partial — substrate authoritative for history (the territory of A2.36 and Category 2) and for conflicts (Category 3) but not for present state. The integrating commitment cannot be coherent with Category 1 missing.

**Substrate-only paths from A2.41.** Substrate-only paths requires that substrate alone be sufficient to answer the questions the commitment scopes. Current-state queries are the most operationally pervasive class. Without Category 1 authority, substrate-only paths would be aspirational.

**The human-governed commitment from A1.01.** Humans cannot exercise meaningful governance over content they cannot authoritatively read. Category 1 is what makes substrate reads architecturally authoritative — humans inspecting substrate see the current coordination state, not a derivative view that may disagree with what the deployment is operationally doing.

**The AI-as-substrate-mediator commitment from A1.04.** LLM mediators read substrate as primary source of state per Property A from A2.19. Category 1 is what makes substrate authoritative for the LLM's read — the LLM operates on the deployment's actual current coordination state, not on a derivative view that lags the operational truth.

**The conflict-as-first-class commitment from A1.03.** Conflicts are first-class substrate state; their current presence is the architectural truth about what is unresolved. Category 1 supports conflict authority — the substrate's current state on contradictions is the authoritative state, queried as Category 3 supports.

These connections are not new commitments; they follow from treating Category 1 as having independent operational content.

## 6. Failure modes that violate the commitment

Ten anti-patterns recur where Category 1 fails. Each names a way an implementation can be operationally functional but architecturally non-coherent on current-state authority.

**(a) Substrate as cache.** Substrate is updated periodically from external operational systems; reads return potentially stale cached values. The authoritative live state is elsewhere.

**(b) Substrate as projection.** Substrate is materialized from event streams or external data; the events or external data are authoritative; substrate is one projection among several possible.

**(c) External-write-first patterns.** Writes go to external systems first and propagate to substrate downstream. Substrate's current state lags the external systems and depends on them for accuracy.

**(d) Bidirectional synchronization without primacy.** Substrate and external systems exchange updates bidirectionally with no architectural primacy; conflicts are resolved by latest-write or by manual reconciliation. Neither system is authoritative.

**(e) Read-from-external, write-to-substrate.** Reads against the deployment go to external systems for current state; writes for governance purposes go to substrate. Substrate is governance-authoritative but not operationally authoritative; the architectural commitment is split.

**(f) Substrate-as-archival.** Substrate carries historical records; current operational state is in external systems. Substrate authority is over history but not over present; the Category 1 commitment fails specifically (note that this is a way of failing Category 1 even when Category 2 may be satisfied).

**(g) Substrate-as-snapshot.** Periodic snapshots of external state populate substrate; between snapshots, substrate is stale. Substrate authority is snapshot-time-bound, not continuous.

**(h) External-event-driven substrate updates.** Substrate updates are triggered by external events; if external event emission fails, substrate is missing updates. Substrate's current state depends on external event-delivery reliability.

**(i) View-only substrate.** Substrate is materialized for read but not written by the deployment. Writes occur in external systems; substrate is a view. Substrate authority for the writer-side of current state is absent.

**(j) Substrate updated by external scheduler.** An external scheduler determines when substrate is updated; substrate's current state lags the scheduler's cycle. Substrate is not the writer of its own current state.

Across all ten, implementations tend to look operationally functional until two observers reading what each takes to be the authoritative source disagree about current state, with no architectural rule available for which observer's source prevails.

## 7. Operational test

A system implements the Category 1 commitment if and only if all of the following are true at all times during the substrate's existence.

1. Queries about current coordination state — entity status, property values, relationships within substrate scope — are answered authoritatively from substrate.

2. Updates to current coordination state are committed to substrate first per A2.10's boundary-crossings discipline; derivative views in external systems update downstream from substrate.

3. When substrate and external sources disagree on current coordination state, the deployment resolves the disagreement in favor of substrate — by updating the external sources, treating them as stale, or flagging them out-of-sync, but not by updating substrate to match them for substrate's own coordination state.

4. The substrate's current state is queryable through standard read operations per A2.25 Requirement 2, without requiring consultation of external systems for completeness or accuracy.

5. External systems carrying related content — caches, search indexes, dashboards, materialized views, business intelligence projections — operate as derivative views of substrate, not as authoritative sources for coordination state.

A system that fails any of (1)–(5) does not satisfy the Category 1 commitment in the architectural sense, even when its current-state queries function operationally for users who do not consult multiple sources.

## 8. Conclusion

Implementations under pressure to integrate with enterprise operational systems, leverage existing infrastructure, or optimize for read performance consistently drift toward substrate-as-derivative patterns. The result is a system in which substrate authority is partial — substrate authoritative for governance and audit, external systems authoritative for live operational state.

The downstream consequences are concrete. Coordination ambiguity emerges (which system to consult for which current-state question). Governance fails (humans cannot exercise meaningful governance over state held authoritatively elsewhere). The AI-as-substrate-mediator commitment fails (LLM mediators read derivative state rather than the operational truth). And the source-of-truth commitment fails across the other four categories: Categories 2, 3, 4, and 5 cannot be coherent without Category 1, because each presupposes that the substrate's view of "what is" is the architectural truth the categorical claims about decisions, conflicts, rules, and authority hang from.

Naming Category 1 as a standalone commitment gives downstream implementers a precise specification of what substrate authority over current state requires. The companion notes A2.44, A2.45, A2.46, and A2.47 specialize Categories 2 through 5; A2.48 specializes the source-of-truth-vs-mirror-of-truth distinction; together with A2.42's integrating frame, they give the full decomposition of A1.08.

Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should treat substrate authority for current state as the load-bearing commitment it is. Implementations that fragment current-state authority across substrate and external operational systems are using a different architecture, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Category 1 — Substrate Authoritative for "What Is the Case": Standalone Treatment of Current-State Authority in the Coordination Knowledge Substrate Pattern.* May 4, 2026. ORCID: 0009-0004-8065-3235.
