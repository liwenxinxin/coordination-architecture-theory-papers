# Composition Pair: Conflict as First-Class × Path Retraceability — Conflict-Provenance as the Architectural Pattern Making Conflict Lifecycle Auditable in the Coordination Knowledge Substrate

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the architectural property that emerges when two foundational CKS commitments — *conflict as first-class* and *path retraceability* — are required to hold together, so that downstream work has a precise specification of what *conflict-provenance* names in CKS and what a deployment must do to instantiate it.

## Abstract

The CKS pattern names conflict as first-class and path retraceability as two of its foundational architectural commitments. Each is independently formalizable; each has its own operational test. This note formalizes the property that emerges when both commitments must hold simultaneously — *conflict-provenance*, also called *traceable conflict history* — under which every contradiction in substrate is traceable through its complete lifecycle, from the conflicting writes that produced it, through its persistence as a substrate-resident contradiction edge, through its rule-mediated cell-level resolution, with provenance recorded at each step. Neither commitment yields this property alone. Conflict-as-first-class without retraceability produces preserved contradictions whose creation and resolution events lack accountable provenance. Retraceability without conflict-as-first-class produces a substrate whose changes are auditable in general but in which conflict events are not architecturally distinguished from non-conflict events. The composition produces *conflict-events-specifically-retraceable* as the architectural commitment. The note defines the emergent property in four operational components, identifies what the composition forces beyond either commitment, names the anti-patterns that specifically violate it, and provides an operational test with three sharpening properties.

## 1. Why the composition needs standalone formalization

The two commitments are individually defended in separate derivation notes. Conflict as first-class is formalized as the source paper's two-level handling pattern in §5: substrate-level preservation of contradictions as addressable, provenance-bearing first-class objects, and cell-level resolution under human-authored orchestration rules, with the resolution itself recorded as substrate content rather than as mutation of the contradicting content. Path retraceability is formalized as the traceability commitment of §3.1: every piece of substrate content carries enough provenance that the path back to its antecedents is reconstructable from substrate content alone, with the substrate schema and orchestration rules together specifying what the trace must contain to be complete.

The property downstream work most often invokes when reaching for "auditable conflict resolution" or "explainable disagreement handling" — the property that lets a human auditor reconstruct, for any historical conflict, *when the contradiction arose, how long it persisted, what rule resolved it, and who initiated the resolution* — is not delivered by either commitment alone. Conflict as first-class delivers preservation of the contradicting content with explicit relationship to what it contradicts; it does not, by itself, mandate that the contradiction's *creation event* and the cell's *resolution event* carry the full provenance fields the retraceability commitment requires for substrate writes generally. Path retraceability delivers provenance for substrate writes; it does not, by itself, mandate that conflict events be architecturally distinguished from non-conflict events, nor that the rule a cell invoked to resolve a contradiction be specifically attributed in the trace.

Both commitments together deliver the property. The composition's content is the requirement that conflict events — contradiction creation, contradiction persistence, contradiction resolution — be retraceable on the same terms as ordinary substrate writes, with the addition that conflict events are architecturally identifiable as such. This note formalizes the requirement so a deployment claiming CKS-style auditable conflict-handling has a precise specification to implement against, and so the silent slide into systems that satisfy each commitment partially while failing the joint property becomes describable as a specific failure mode rather than as a variant satisfaction.

## 2. The emergent property: conflict-provenance, in four components

A substrate exhibits **conflict-provenance** if and only if all four of the following components hold at all times during its existence.

**(a) Contradiction-creation events carry full provenance.** When two or more writes produce a contradiction edge — the substrate-resident structural artifact recording that two pieces of content contradict each other, on what dimension — the creation of the edge is itself a recorded substrate event with the provenance fields the retraceability commitment requires: the writers whose conflicting writes produced the edge, the orchestration rules each was made under (where applicable), timestamp, prior-state, change description identifying the event as a contradiction creation rather than an ordinary write, and cell-execution references where applicable. The contradiction edge is not inferred by a reader from the contradicting content; its creation is a substrate event in its own right.

**(b) Contradiction edges are addressable, with persistence-duration tracking.** Every contradiction edge has a stable substrate address that survives across the deployment's lifecycle, separate from the addresses of the contradicting content the edge connects. The address supports re-entry by participants and by humans exercising the inspect right, and carries timestamps that bracket the edge's persistence — at minimum the creation timestamp from (a) and, when the edge is resolved, the resolution timestamp from (c). The duration the contradiction persisted is computable from substrate content alone.

**(c) Resolution events carry full provenance, including rule reference.** When a cell executing under an orchestration rule resolves a contradiction — by recording a decision that closes the edge, by superseding one side of the contradiction with new content the rule authorizes, or by recording the contradiction as deferred with a terminal recorded outcome — the resolution event carries the same provenance fields as creation: the cell instance as actor, the specific orchestration rule the cell was operating under (identified as a substrate-resident rule), timestamp, prior-state, change description identifying the event as the resolution of a specific contradiction edge, and cell-execution reference. The rule reference is the load-bearing field: it points to the substrate-resident orchestration rule that authorized the resolution, in a form that lets a reader recover *why this specific resolution* by reading the rule.

**(d) The four accountability questions are answerable for every conflict event.** For any contradiction edge in substrate — currently persistent or resolved — a human exercising the inspect right can answer the four accountability questions the retraceability commitment names: *who* (which writers produced the conflict, which cell resolved it), *what* (the conflicting content and the resolution decision), *why* (the orchestration rules each writer was operating under, the rule the resolving cell invoked), and *when* (creation and resolution timestamps), entirely from substrate content. The answerability is what makes conflict-handling architecturally accountable to human governance, not merely operationally observable through external logs.

The four components are jointly necessary. A substrate satisfying (a)–(c) but failing (d) — for example, by carrying provenance fields in a form inspectable individually but not assemblable into the four-question answer — does not satisfy the composition. A substrate satisfying (b)–(d) but failing (a) — recording contradictions but not their creation events — does not satisfy it either.

## 3. What the composition forces beyond either commitment alone

Conflict as first-class commits the substrate to preservation of contradictions and to cell-level resolution under rules; it does not, in its own terms, commit to the resolution event carrying the same provenance fields as ordinary substrate writes. A deployment satisfying the conflict commitment with thin provenance — recording resolutions with timestamps but without the rule reference identifying which specific orchestration rule was invoked — is conflict-preserving in the source paper's sense but does not satisfy the composition. The composition forces resolution provenance to be full and specifically *rule-attributing*.

Path retraceability commits the substrate to provenance fields for substrate content generally; it does not mandate that conflict events be architecturally distinguished from non-conflict events. A deployment satisfying retraceability with generic provenance — every write carrying writer, timestamp, antecedents — but in which the contradiction edge is implicit rather than substrate-resident, or in which the resolution event is indistinguishable in form from any other write, satisfies retraceability but not the composition. The composition forces conflict events to be identifiable as such in the trace, so that conflict-specific querying — *show me all contradictions that arose in the past quarter, how long each persisted, what rule resolved each* — is answerable from substrate content alone.

The composition also forces two further commitments each individual commitment is silent on: contradictions must have stable addressability across the deployment's lifecycle (so retracing across sessions is possible), and conflict provenance must be substrate-resident (a deployment that records conflict-handling provenance only in an external audit log fails the composition because the conflict-event path runs through content the substrate does not authoritatively carry).

## 4. Anti-patterns that specifically violate the composition

Five anti-pattern classes violate the composition distinctively, beyond the violations of either commitment alone.

**Silent conflict resolution.** Cells resolve contradictions without recording that resolution occurred or what rule authorized it. The resolution event is missing from substrate, or is present but lacks the rule reference component (c) requires. This is the canonical composition violation: it can occur in deployments that otherwise satisfy retraceability for non-conflict writes and that otherwise preserve contradictions, and the failure is precisely at the joint property.

**Detect-resolve-forget with resolution-trace-loss.** Conflicts are detected, resolved, and the resolution is initially recorded, but the contradiction and its resolution are pruned, garbage-collected, or "cleaned up" once considered settled. Retraceability for current substrate state may remain intact; the composition fails because historical conflict-handling is no longer reconstructable from substrate content. The composition's commitment is to traceability across the deployment's lifecycle, not to traceability of currently-live state only.

**Contradiction collapse by automation, with rule attribution absent or generic.** Automated mechanisms — last-writer-wins, CRDT-style merge functions, ML-driven reconciliation, vendor-managed conflict-resolution APIs — resolve contradictions without invocation of a substrate-resident orchestration rule. The resolution may be timestamped and attributed to the automation as actor, but the rule reference field either points to nothing, points to implementation code outside the substrate, or carries a generic placeholder. A reader cannot recover *why this specific resolution* by reading substrate content.

**Non-addressable conflict events.** Contradiction edges or resolution events are written in forms that do not carry stable addresses — embedded in opaque blobs, generated as transient objects without persistence keys, or addressed only relative to a session that ends. The composition is violated specifically because conflict events are exactly the events for which cross-session retracing is most often required.

**Vendor-specific conflict resolution outside substrate-only paths.** Conflicts are routed through a vendor system whose conflict-resolution provenance lives in vendor logs rather than as substrate content. A reader exercising the inspect right against the substrate alone cannot reconstruct the conflict's lifecycle. A related sub-class is *resolution without rule*: human participants directly override contradiction edges through inspect-modify operations bypassing cell-mediated rule-governed resolution. The override itself is governed by the override right, but if the resolution event is not recorded with the same provenance fields a cell-mediated resolution would carry, the composition fails on conflicts resolved this way.

These five are not exhaustive, but they are the classes most often encountered in deployments that satisfy the individual commitments while failing the joint property. The composition is what makes them describable as failures rather than as design choices.

## 5. What the composition is NOT

Four adjacent commitments are commonly conflated with conflict-provenance.

**Not conflict-handling-with-thin-provenance.** A substrate that preserves contradictions and records resolution events with timestamps and actor attribution but without rule reference — or with rule reference present but not traceable to a substrate-resident orchestration rule — is conflict-preserving in the source paper's sense but does not exhibit conflict-provenance. The rule reference is load-bearing because it is what carries the *why* of the resolution into substrate-resident form; without it, the resolution is observable but not accountable.

**Not retraceability-without-conflict-distinction.** A substrate in which all writes carry full provenance but in which conflict events are not architecturally distinguished from ordinary writes does not exhibit conflict-provenance. The distinction is what enables conflict-specific querying and accountability.

**Not external audit logging of conflicts.** Audit logs in systems external to the substrate that record conflict events are not on the substrate-resident provenance path. Conflict-provenance is a property of the substrate as the source of truth; audit logs about substrate state are a different commitment, valuable for other purposes but not what conflict-provenance names.

**Not automated-resolution-with-fabricated-rule-attribution.** Automated mechanisms can be configured to record a "rule reference" field, satisfying the form of (c) without the substance. If the rule reference does not point to a substrate-resident, human-authored orchestration rule that a reader can inspect and that actually authorized the resolution, the composition is not satisfied. The form of provenance without substrate-resident rule authority is observably similar to conflict-provenance but is architecturally a different artifact.

## 6. Operational test

A deployment instantiates the composition if and only if all of the following are true at all times during the substrate's existence:

1. Every contradiction-creation event is recorded as a substrate event satisfying component (a) of §2 — full provenance including the conflicting writes that caused the edge, with the event identifiable in change description as a contradiction creation.

2. Every contradiction edge satisfies component (b): a stable substrate address surviving the deployment's lifecycle, with timestamps bracketing its persistence, such that persistence duration is computable from substrate content alone.

3. Every resolution event is recorded as a substrate event satisfying component (c), including a rule reference that resolves to a substrate-resident, human-authored orchestration rule that authorized the resolution. Generic, fabricated, or external rule references do not satisfy this requirement.

4. For any contradiction edge in substrate — currently persistent or resolved — the four accountability questions (who, what, why, when) are answerable from substrate content alone, without consulting external logs, agent memory, or human recollection.

5. Three sharpening properties hold under operational review:

   - **Contradiction-creation-provenance test.** Selecting any contradiction edge in substrate and tracing back to its creation event yields the full provenance fields of (1), with the conflicting writes identified as the antecedents that caused the edge.

   - **Resolution-provenance test.** Selecting any resolved contradiction edge and tracing the resolution event yields the full provenance fields of (3), with the rule reference resolvable to a substrate-resident orchestration rule a reader exercising the inspect right can read and inspect.

   - **Conflict-lifecycle-traceability test.** For any contradiction edge sampled from substrate history, a human can reconstruct the full lifecycle — creation, persistence duration, resolution where applicable — entirely from substrate content, in the sense the four accountability questions name.

A deployment that fails any of (1)–(4) or any of the three sharpening properties does not satisfy the composition. A deployment that satisfies all of them does, regardless of how much further machinery (external logging, dashboards, replay tooling) it adds.

## 7. Why naming the composition matters

Two failure patterns recur in deployments that claim auditable conflict resolution, and naming the composition as standalone is what makes them describable as failures rather than as variant satisfactions.

The first is partial-satisfaction-without-the-joint-property. A deployment satisfies conflict preservation and satisfies retraceability for general substrate writes — but the resolution event lacks the rule reference, or the contradiction edge has no stable address, or the four accountability questions are answerable for ordinary writes but not specifically for conflict events. Each individual commitment is satisfiable on its own terms; the composition is not. Without the composition named as a separate property, the deployment can claim CKS conformance on both axes while missing the property auditable conflict-handling actually requires.

The second is form-without-substance. Provenance fields are populated on conflict events, but the rule reference points to automation rather than to a substrate-resident rule, or the resolution event is recorded in a vendor system rather than in substrate, or the address of a contradiction edge is session-local rather than lifecycle-stable. The form of conflict-provenance is satisfied; the substance — substrate-resident, lifecycle-traceable conflict accountability — is not.

The composition is also what positions CKS distinctively against the architectural patterns the source paper takes as foils. Detect-resolve-forget systems are architecturally incapable of satisfying it: the resolution event's recording is what they treat as the *opposite* of correct behavior, since the contradiction's disappearance is what they define success as. Automated-collapse systems satisfy the form of resolution recording but not the rule-attribution substance. External-audit-log systems satisfy accountability in some sense but not on the substrate-resident path. Each is identifiable as failing the composition in a specific way only because the composition is named as a single property.

This note belongs to a sequence of composition-pair derivation notes that formalize the architectural properties emerging from pairs of foundational CKS commitments. It complements the prior composition that establishes reproducibility as the joint property of retraceability and the determinism contract: where that composition makes substrate state reproducible in general, the present composition makes conflict-affected state reproducible in particular, since reproducibility of substrate-resident conflict events requires both the determinism contract's conflict-handling guarantee and the conflict-events-specifically-retraceable property the present composition names.

Subsequent work that adopts, extends, composes, or argues against the CKS conflict-provenance commitment should use the term in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Composition Pair: Conflict as First-Class × Path Retraceability — Conflict-Provenance as the Architectural Pattern Making Conflict Lifecycle Auditable in the Coordination Knowledge Substrate.* May 6, 2026. ORCID: 0009-0004-8065-3235.
