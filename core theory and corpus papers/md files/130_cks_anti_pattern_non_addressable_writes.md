# Anti-Pattern: Non-Addressable Writes — Substrate Writes That Lack the Addressable Provenance Required by Path Retraceability in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one anti-pattern — *non-addressable writes* — as a standalone failure mode against which CKS deployments can be tested, distinct from the failure modes formalized in adjacent notes on the substrate-as-source-of-truth and AI-as-substrate-mediator commitments.

## Abstract

The CKS pattern's path retraceability commitment requires every substrate state change to be addressable through provenance metadata that a reader can recover from substrate content alone. The source paper specifies six required provenance fields — actor identity, rule or orchestration reference, timestamp, prior-state reference, change description, and (for cell-mediated writes) cell-execution-id. *Non-addressable writes* is the anti-pattern in which substrate writes occur but lack one or more of these fields, producing substrate state changes that the path retraceability commitment cannot reconstruct. The anti-pattern is operationally common in 2024–2026 deployments because database defaults, LLM frameworks, bulk-operation patterns, and shared-account scenarios all produce writes whose provenance is incomplete in one or more of the six fields. This note states the anti-pattern in four operational components, identifies the CKS commitments it violates, traces the failure mode, specifies the architectural correction, distinguishes it from four adjacent legitimate patterns, and provides an operational test with three sharpening properties.

## 1. Why this anti-pattern needs to be formalized as standalone

The CKS pattern's path retraceability commitment, formalized in a separate derivation note, requires that every substrate state change be reconstructable from substrate content alone. The commitment decomposes into six provenance metadata fields the substrate must carry for each change, and four accountability questions those fields make answerable.

Non-addressable writes is the anti-pattern that violates this commitment specifically at the write-provenance layer. The substrate is the source of truth in the deployment; writes do flow into it; but the writes lack one or more of the six required fields, and the changes they produce are no longer addressable. This is architecturally distinct from a related cluster of failures — formalized in adjacent notes — in which authoritative content is held outside substrate altogether. There, the substrate is bypassed; here, the substrate is written to but the writes are not retraceable. A deployment can exhibit either failure independently of the other, and a single deployment can exhibit both at once.

The motivating cases are operationally common: automated processes attributing writes to "system"; data migrations writing thousands of records under a single aggregated provenance entry; LLM-mediated writes that record the LLM as actor but not the orchestration rule that authorized the cell; cron-scheduled writes that record a timestamp but not the trigger context; shared operational accounts whose writes resolve to the account rather than to the human; deployments that maintain an external audit log and treat it as a substitute for substrate-resident provenance. Naming the anti-pattern as standalone — separate from the broader path retraceability commitment it violates and from the source-of-truth-migration cluster it is sometimes confused with — gives downstream readers a precise specification of the failure mode and gives subsequent inventive work a smaller territory in which to claim novel contribution.

## 2. The anti-pattern, defined precisely

A deployment exhibits **non-addressable writes** when substrate writes occur whose provenance metadata is incomplete in the sense that the path retraceability commitment cannot reconstruct the writes from substrate content alone. The anti-pattern has four operational components; a deployment that exhibits any one of them partially exhibits the anti-pattern, and a deployment that exhibits all four exhibits it fully.

**(a) Substrate writes lacking actor identity.** The write is recorded but the actor that produced it — a specific human, a specific cell execution, or a specific automated process — is not identified at the resolution the path retraceability commitment requires. Common instantiations: writes attributed to "system," to a default admin user, to a shared operational account, or to no actor at all (anonymous writes).

**(b) Substrate writes lacking rule or orchestration provenance.** The write is recorded and the actor may be named, but the orchestration rule (or, for non-cell writes, the operational authority) under which the write was authorized is not recorded. Common instantiations: automated writes with no rule reference; LLM-direct writes that record the LLM as actor but omit the cell rule that governed the cell's behavior; bulk operations that aggregate rule references across records.

**(c) Substrate writes lacking prior-state reference.** The write records the new state but not the substrate state that preceded it, leaving rollback or re-application unreconstructable from substrate content alone. Common instantiations: full-replacement writes that overwrite without prior-state capture; distributed writes whose prior-state references diverge under race conditions; write paths in which the prior state is held in memory rather than recorded as substrate content.

**(d) Bulk or aggregated writes that do not decompose to per-record addressability.** Operations that affect many substrate records record one provenance entry for the whole operation rather than one per record. Even if the aggregated provenance is itself well-formed, the per-record changes the operation produced are not individually addressable. Common instantiations: data migrations, batch processors, ETL operations, scheduled syncs, and bulk imports that compress per-record provenance into single operation entries.

The four components correspond, respectively, to the actor-identity field of the six-field specification, the rule-reference field, the prior-state field, and the architectural commitment that addressability is per-change rather than per-batch.

## 3. CKS commitments the anti-pattern violates

The anti-pattern violates the path retraceability commitment directly by failing to carry one or more of the six provenance fields the commitment specifies; from that direct violation, several adjacent commitments are compromised in specific ways.

**Path retraceability and the four accountability questions.** Path retraceability is directly violated for any write whose provenance is incomplete: the antecedent path the commitment names is not reconstructable from substrate content alone. The four accountability questions become correspondingly unanswerable. Missing the actor-identity field makes "who" unanswerable; missing the rule reference makes "why" unanswerable; missing the prior-state reference makes "what was changed" partially unanswerable, since the delta cannot be computed from the recorded new state alone; missing temporal context (even when a raw timestamp is present) makes "when" partially unanswerable in deployments where ordering relative to other changes is what matters.

**Determinism, mediator attribution, and substrate-only paths.** The determinism contract's change-addressability guarantee is directly violated: the substrate's deterministic state behavior at the coordination layer rests on each change being individually reapplicable, which non-addressable writes prevent. The AI-as-substrate-mediator commitment's attribution property is directly violated for LLM-mediated writes that lack the cell-execution-id, the rule reference, or the consultation context — such writes look indistinguishable from human-mediated writes once they are in substrate, and the architectural separation collapses. The substrate-only-paths commitment is violated when external audit logs are treated as a substitute for substrate-resident provenance; external monitoring is a permissible adjacent system, not a permissible substitute.

**Composition and cascade-implications.** A composed substrate cannot recover the provenance of an upstream substrate's writes if those writes were non-addressable; the composition requirement that addressable provenance hold per substrate fails at the upstream layer. Several foundational commitments are cascade-implicated: the human-governed commitment depends on the inspect right being able to answer accountability questions, and the orchestration-rule-authoring-as-governance moment depends on the rule's application being retraceable. The cascade shows that path retraceability is load-bearing for several adjacent commitments.

## 4. The failure mode

Non-addressable writes produce a deployment in which some or all substrate state changes cannot be retraced from substrate content alone. Humans exercising the inspect right see substrate content but cannot answer the accountability questions for the affected changes; the substrate looks coherent at the content layer, and the failure shows only at the provenance layer. Recovery from incorrect substrate state becomes operationally constrained, because the chain of changes cannot be walked backward at the affected steps.

LLM-mediated writes that lack rule-governance attribution become indistinguishable from human-mediated writes once they are in substrate. The mediator commitment's purpose — that LLM authority be visible as such, so the human-governed commitment's authority architecture applies meaningfully — is operationally defeated. Bulk operations whose per-record provenance has been aggregated produce undecomposable change history: when a downstream problem is traced to a record the bulk operation wrote, the per-record context is not recoverable. Automated processes that lack trigger context operate as opaque sources of substrate change. Shared-account scenarios obscure the actual actor. Audit-log substitution shifts retraceability outside substrate, making the retention, availability, and integrity of external logs into coupling factors the substrate-only-paths commitment is meant to insulate retraceability from. Race-conditioned writes can produce changes whose causal ordering is not addressable from the recorded provenance, even when timestamps are present.

The failure mode compounds with adjacent anti-patterns. Hidden state in cells produces non-addressable substrate effects when the hidden state's transitions reach substrate without attribution; contradiction-collapse-by-automation produces non-addressable writes when automated collapse processes write without per-collapse provenance; LLM-as-source-of-truth configurations produce non-addressable writes when LLM-direct writes lack the rule-governance attribution the mediator commitment requires. A deployment exhibiting non-addressable writes alongside any of these is harder to remediate than one that exhibits any of them in isolation.

## 5. The architectural correction

A deployment corrects the anti-pattern by enforcing the path retraceability commitment at the write path. Three architectural commitments together constitute the correction.

The six-field provenance specification holds for every substrate write. The substrate-write infrastructure records actor identity at the resolution required (a specific human, a specific cell execution, a specific automated process — not a default account, not a shared role, not "system"); the orchestration rule or operational authority under which the write was authorized; the timestamp with sufficient temporal context for ordering; the prior substrate state the write modified; the change description, whether as delta or as complete new state; and, for cell-mediated writes, the cell-execution-id. The fields are mandatory at the write path, not optional.

Substrate writes carry their own provenance, not an external system's. The substrate-only-paths commitment requires that provenance live in substrate, addressable as substrate content. External monitoring may exist as adjacent tooling; it does not substitute for substrate-resident provenance, and the deployment does not rely on it for retraceability.

Bulk operations decompose to per-record addressable writes. Whatever interface produces the bulk operation, the substrate writes it produces are recorded as individually addressable changes, each with its own provenance. The aggregated operation may itself be recorded as a substrate object the per-record changes reference; what is not permitted is that the per-record changes share a single aggregated provenance entry as their only provenance.

From these three commitments, several operational practices follow. LLM-mediated writes record the cell-execution-id, the orchestration rule, the LLM consultation (when one occurred), and the transformation applied. Automated processes record their trigger context — what scheduled them, what rule authorized them, what prior state they modified. Shared-account scenarios resolve to specific actors at write time, through whatever mechanism the deployment chooses. The substrate-write infrastructure enforces the six fields architecturally: a write attempt that lacks any required field fails at the write path rather than succeeding without attribution.

## 6. What the anti-pattern is NOT

Four adjacent patterns are commonly conflated with non-addressable writes; each is a legitimate pattern in some deployment, and naming what the anti-pattern is not is what prevents misreadings of the architectural commitment.

**Not writes with full six-field provenance.** A write that records all six fields, regardless of which actor produced it, satisfies the commitment. The anti-pattern is specifically about writes whose provenance is incomplete.

**Not bulk operations whose per-record provenance is preserved.** A bulk operation that writes thousands of records, each carrying its own actor identity, rule reference, timestamp, prior-state reference, and change description, is operating within the architecture. The anti-pattern is bulk operations that *aggregate* provenance, not bulk operations as such.

**Not automated writes whose trigger context is recorded.** A scheduled automated write that records what scheduled it, what rule authorized it, and what prior state it modified satisfies the commitment. Automation is not the failure mode; automation without trigger context is.

**Not LLM-mediated writes that record cell and rule attribution.** An LLM-mediated write that records the cell-execution-id, the orchestration rule, the LLM consultation, and the transformation applied satisfies the mediator commitment's attribution property and the path retraceability commitment together. The anti-pattern is specifically LLM-direct writes that omit rule-governance attribution.

## 7. Why this anti-pattern is load-bearing as a standalone formalization

Several properties make non-addressable writes worth formalizing as a separate note rather than treating it as a generic failure mode of the broader path retraceability commitment.

It violates the commitment with field-level specificity. The six provenance fields are architecturally precise; failures at the write-provenance layer can be located to specific missing fields, and the architectural correction is correspondingly specific. Without the standalone treatment, deployments may have writes that fail addressability without recognizing which field's absence caused the failure or what enforcement would prevent its recurrence.

It cascades broadly. Path retraceability, the determinism contract's change-addressability guarantee, the mediator commitment's attribution property for LLM-mediated writes, and the substrate-only-paths commitment are all directly violated; several foundational commitments are cascade-implicated. The anti-pattern is consequential at the architectural layer, not only at the write-path layer.

It is architecturally orthogonal to the source-of-truth-migration cluster of anti-patterns: those failures hold authoritative content outside substrate; this failure writes into substrate without addressability. The two are independent and can co-occur, and naming non-addressable writes as standalone keeps the orthogonal failure mode visible rather than absorbed into the source-of-truth treatment.

## 8. Operational test

A deployment exhibits non-addressable writes if, at any time during the deployment's existence, any of the following are true.

1. Substrate writes lack actor identity at the resolution the path retraceability commitment requires — "system" attribution, default admin attribution, anonymous writes, or shared-account-only attribution.
2. Substrate writes lack rule or orchestration provenance — automated writes without rule reference, LLM-direct writes without cell-rule context, or operationally authorized writes without authority reference.
3. Substrate writes lack prior-state reference — full-replacement writes without prior-state capture, or distributed writes whose prior-state references diverge under concurrency.
4. Bulk or aggregated writes do not decompose to per-record addressability — operations that affect multiple records carry one aggregated provenance entry rather than per-record entries.

Three sharpening properties further specify the test. Each is independently inspectable; failing any one indicates the anti-pattern at the corresponding layer.

**Six-field-completeness property.** Every substrate write carries all six provenance fields the specification requires. The reviewer samples writes across substrate and verifies that no required field is missing for any write; missing fields indicate the anti-pattern at that field.

**Bulk-operation-decomposition property.** Operations that produce multiple substrate changes record per-record provenance for each change. The reviewer examines the substrate effects of bulk operations; aggregated provenance indicates the anti-pattern.

**LLM-write-attribution property.** Writes whose actor is an LLM or a cell operating with LLM consultation record the cell-execution-id, the orchestration rule, and the consultation context. The reviewer examines LLM-mediated write provenance; missing attribution indicates the anti-pattern.

A one-sentence test, useful for triaging a deployment quickly: *if the deployment's substrate writes lack one or more of the six required provenance fields — actor identity, rule or orchestration reference, timestamp, prior-state reference, change description, or cell-execution-id — through "system" attribution, bulk aggregation, automated-process attribution without trigger context, LLM-direct writes without rule reference, shared-account scenarios, or audit-log substitution, the deployment exhibits non-addressable writes, and the path retraceability commitment fails for the affected writes.*

## 9. Conclusion

Implementations under pressure to deliver coordination capability through automation, scheduled jobs, bulk operations, and LLM-driven writes consistently default to write paths whose provenance is incomplete. The drift is steady because the surrounding patterns — database defaults, LLM framework conventions, bulk-operation aggregation, cron scheduling — produce writes that are operationally functional and apparently complete, while quietly omitting one or more of the provenance fields the path retraceability commitment requires. Readers of those writes encounter "the system updated this" as ordinary automated-system attribution and do not recognize the architectural consequence: substrate state has changed without the deployment being able to retrace what produced the change. Naming non-addressable writes as a standalone anti-pattern — with its four operational components, the violations of adjacent commitments, the failure mode, the architectural correction, the four adjacent-pattern distinctions, and the operational test with three sharpening properties — gives downstream readers a precise specification of the failure mode and its correction, separable from the broader path retraceability commitment it violates and from the other anti-patterns that may compound with it.

Subsequent work that adopts the CKS pattern, extends it, or composes it with adjacent patterns should test its candidate deployments against the operational test in §8. Subsequent work that argues against the CKS pattern should be specific about whether the path retraceability commitment, the six-field provenance specification, or the architectural enforcement at the write path is the commitment being argued against, since each is a different commitment and the architectural consequences of arguing against each differ.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Anti-Pattern: Non-Addressable Writes — Substrate Writes That Lack the Addressable Provenance Required by Path Retraceability in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
