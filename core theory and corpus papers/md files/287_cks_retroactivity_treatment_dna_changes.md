# Forward-Only Governance: Retroactivity Treatment for DNA Changes in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the precise retroactivity treatment that applies when directed selection changes DNA — formalizing how the A6.02 rule-retroactivity boundary case from Paper 1 governs DNA change events under Paper 2's directed-selection mechanism (B1.14).

## Abstract

In the Coordination Knowledge Substrate (CKS) pattern, directed selection (B1.14) changes a cell's DNA layer under the standard authority architecture. When DNA changes, a retroactivity question arises: does new DNA govern only forward operations, or does it reach back to re-govern operations already recorded under prior DNA? This note formalizes the answer: new DNA applies forward from the modification timestamp; prior DNA is preserved in version history (per B2.69); and operational records in the Action layer are governed by the DNA version that was active at the time of their creation — they are not re-governed by new DNA. This is the A6.02 rule-retroactivity boundary case applied specifically to directed selection. The note articulates the four operational implications of this treatment (behavioral audit, regulatory compliance, A2.40 provenance field 4, and A1.10 determinism preservation), the role of DNA rollback, cross-level retroactivity, the contrast with implicit retroactivity in conventional AI model updates, and the limits that bound the treatment. Retroactivity treatment is an architectural requirement, not a deployment option.

---

## 1. Why retroactivity treatment for DNA changes needs its own formalization

Directed selection (B1.14) is the mechanism by which human governance changes a cell's DNA layer. Paper 2's "Governance shapes across evolution mechanisms" section specifies that directed selection is governed through the standard authority architecture from Paper 1 — humans hold authority over which DNA changes are accepted, retained, or reverted, and selection criteria are themselves substrate content. B2.67 formalized the scope of directed selection; B2.68 formalized the modification governance process; B2.69 formalized DNA version management. Each of those notes addressed a different dimension of what directed selection produces.

What none of those notes addressed is the temporal question that arises every time a DNA version changes: what happens to the operational record that accumulated under prior DNA? Does new DNA reach backward? Does it re-govern what cells did before the modification? Does a compliance analyst reading records from the prior period use the new DNA or the old DNA to evaluate what happened?

These questions have a precise answer in the CKS pattern, derived directly from the A6.02 rule-retroactivity boundary case that Paper 1 establishes. But that answer is not visible from B2.67, B2.68, or B2.69 alone. It requires a standalone formalization that states the retroactivity treatment explicitly, connects it to its load-bearing antecedents, and draws out its operational implications. B2.70 provides that formalization.

The strategic role of this note is to establish retroactivity treatment as a named, publicly documented derivation — closing one of the patentable territories that DNA version management alone leaves open. Version management (B2.69) specifies how DNA versions are stored and retrieved. Retroactivity treatment specifies the rule that governs how those versions relate to the operational history they governed. These are distinct architectural commitments; both require independent prior-art publication.

---

## 2. The retroactivity treatment precisely stated

### 2.1 New DNA applies forward from the modification timestamp

When directed selection modifies a cell's DNA, the new DNA version takes effect from the modification timestamp. Cell behavior from that point onward is governed by the new DNA. This is the forward-only application rule: the modification creates a before/after boundary at the timestamp, and the new DNA governs everything after that boundary.

The modification timestamp is itself substrate content. It is the event record of the directed selection decision — recorded per A2.40 as a governance action with the standard provenance fields. The timestamp is what makes the before/after boundary addressable rather than implicit.

### 2.2 Prior DNA is preserved in version history

The prior DNA version is not discarded when new DNA takes effect. It is preserved in version history per B2.69. This preservation is not optional: it is what makes the retroactivity treatment auditable. An auditor who needs to know what DNA governed a cell's behavior in a prior period must be able to retrieve the DNA version that was active during that period. Without preservation, the retroactivity rule would be architectural claim without operational basis.

Prior DNA versions are inspectable per A2.01. Any human exercising the inspect right can retrieve a prior DNA version and read it against the Action records that were created while it was active.

### 2.3 Action records are governed by the DNA active at the time of their creation

Operational records in the Action layer record what a cell did under the DNA that was active at the time. Those records are not re-governed by new DNA. They reflect the behavior that prior DNA produced, evaluated against prior DNA.

This is the core retroactivity rule: no DNA change reaches backward. A cell that operated under DNA version V1 has Action records that belong to V1. When DNA changes to V2, those V1 Action records remain V1 records. V2 governs new operations; it does not reinterpret old ones.

### 2.4 DNA modification as a retroactivity event

Each directed selection DNA change is a retroactivity event in the following precise sense: it is a governance decision that creates a new DNA version, recorded as a new version event per A2.40, with the modification timestamp marking the boundary from which the new version governs forward. The event itself is substrate content — it records who authorized the change, under what rule, at what time, and what changed. Prior operations remain governed by prior DNA in the Action record.

This distinguishes a DNA modification from other substrate changes. Most substrate changes update content under constant DNA. A DNA modification changes the governing specification itself — and thus produces a retroactivity boundary that no other substrate change produces.

### 2.5 DNA rollback creates a new version that applies forward

When directed selection reverts DNA to a prior version — a rollback per B2.69 — the rollback produces a new DNA version with the same content as the prior version. This new version applies forward from the rollback timestamp. The retroactivity treatment is the same as for any other DNA change: the new (rolled-back) DNA governs from the rollback timestamp onward; it does not reach back to re-govern the intermediate period.

This means: records created between the original version and the rollback point remain governed by the DNA versions that were active during that intermediate period. Rollback does not undo those records. It creates a new governing version going forward. The intermediate period's records are preserved as-recorded, governed by the DNA that was active during that period, inspectable per A2.01.

---

## 3. Four retroactivity implications for directed selection

The forward-only application rule has four operational implications that extend the architectural treatment into domains where retroactivity decisions matter concretely.

### 3.1 Behavioral audit

An auditor examining Action records to assess cell behavior must read those records against the DNA version that was active at the time the records were created — not against the current DNA version. If a cell operated under DNA version V1 during period P, the behavioral audit for period P reads against V1. The fact that the cell now operates under V2 does not change the audit. V2 governs future behavior; V1 governs the audit of period P.

This makes behavioral auditing precise: for any Action record, the governing DNA version is identifiable (via A2.40 provenance field 4, addressed in §3.3 below), retrievable (from version history per B2.69), and applicable (as the standard against which that record's behavior is evaluated).

### 3.2 Regulatory compliance

Compliance demonstration for a regulated period uses the DNA version active during that period. If a regulatory regime evaluates cell behavior from January through March under a set of rules, and DNA changed in April, the compliance analysis for January through March uses the January-through-March DNA version. The April DNA change does not alter the compliance analysis for the prior period.

This scopes compliance claims accurately. A deployment that changes DNA to improve compliance going forward does not automatically become retroactively compliant for periods when prior DNA governed. Compliance for those periods must be demonstrated under the DNA that actually governed them. The retroactivity treatment is what makes this scoping architecturally explicit rather than a procedural assertion.

### 3.3 A2.40 provenance field 4: "under what rule"

A2.40 specifies six provenance metadata fields that each piece of substrate content carries. Field 4 — "under what rule" — records which DNA version governed the operation that produced the content. This field is the operational mechanism that makes retroactivity treatment auditable at the record level.

Without provenance field 4, retroactivity would be a claim about how DNA versions relate to Action records, but no individual record would carry the evidence of which DNA version it was governed by. With provenance field 4, every Action record is self-documenting on this point: an auditor reading any single record can identify which DNA version governed it, without needing to reconstruct the version-history timeline separately.

Provenance field 4 is therefore not merely a logging convenience. It is the substrate-level mechanism that converts the retroactivity architectural rule into an operationally verifiable property.

### 3.4 A1.10 determinism preservation

The A1.10 determinism contract specifies that, given the DNA version active at a time and the inputs, cell behavior was deterministic. This contract applies to prior operations under prior DNA. New DNA does not retroactively change the deterministic relationship between prior DNA, prior inputs, and prior behavior.

Retroactivity treatment preserves this determinism for the record. Because prior DNA is preserved (per B2.69) and Action records carry provenance field 4 (per A2.40), the deterministic relationship is reconstructible: an auditor can retrieve the prior DNA version, the inputs recorded for a given operation, and the output recorded for that operation, and verify that the output followed deterministically from the DNA and inputs that were active at the time. New DNA does not disturb this reconstruction.

---

## 4. What makes retroactivity treatment architecturally distinctive

### 4.1 The contrast with conventional AI model updates

In conventional AI deployments, model updates commonly apply implicitly to all subsequent use. When a model is replaced with a newer version, the newer version governs all future queries. There is typically no architectural record of which model version governed which prior interaction. Audit questions of the form "what model governed this output?" may be answerable from deployment logs, but the answer is not embedded in the output's substrate record — it requires external reconstruction.

CKS retroactivity is architecturally explicit. The modification timestamp is substrate content. Provenance field 4 on every Action record identifies the governing DNA version. Prior DNA versions are preserved in version history. The before/after boundary is not implicit or reconstructed; it is recorded.

### 4.2 Why explicit boundaries make behavioral auditing precise

The explicit boundary is what makes it possible to ask — and answer precisely — the question: "What governed cell behavior at time T?" The answer is not "whatever DNA is current" and not "I need to check the deployment logs." The answer is: retrieve the DNA version that was active at time T from version history, confirm it matches provenance field 4 on the Action records from time T, and read those records against that version.

This precision is what distinguishes CKS retroactivity from retroactivity treatment in systems that lack explicit governance substrate. In those systems, retroactivity questions may be answerable as a matter of fact-finding; in CKS, they are answerable as a matter of substrate-record inspection.

---

## 5. The biological analog as conceptual scaffold

The biological analog for DNA retroactivity is mutation propagation: a mutation that occurs at time T affects organisms born after T, not organisms born before T. Prior organisms had prior genetic material; the mutation does not retroactively change what they were. The mutation applies forward through reproduction, not backward through reinterpretation.

CKS DNA retroactivity is the architectural analog. A directed selection DNA change at time T applies to cell behavior from T onward; prior Action records reflect the DNA that was active before T. The mutation-propagation framing makes this intuitive: just as a genetic mutation does not retroactively alter the phenotypes of prior organisms, a DNA modification does not retroactively alter the Action records created under prior DNA.

The analog functions as conceptual scaffold, not as architectural substance. The architectural substance is the explicit forward-only application rule, provenance field 4, and version history preservation. The biology provides a frame for understanding why the rule has the shape it has; the CKS architecture provides the substrate-level enforcement mechanisms that biology does not possess and cannot possess. Biology's mutations operate through differential reproduction over generations; CKS's DNA changes operate through explicit governance decisions recorded in substrate with precise timestamps. The analog is structurally suggestive; the implementation is entirely architectural.

---

## 6. Inherited Paper 1 commitments

Retroactivity treatment for DNA changes draws on five Paper 1 commitments as directly load-bearing antecedents.

**A6.02 rule retroactivity.** The foundational treatment. Paper 1 establishes that rule changes apply forward; prior operations governed by prior rules remain governed by those prior rules in the substrate record. B2.70 applies this treatment specifically to the DNA changes that directed selection produces, operationalizing A6.02 at the directed-selection scope Paper 2 introduces.

**A2.40 provenance field 4.** "Under what rule" — the substrate-level field that records which DNA version governed each Action record. Without this field, the retroactivity rule is architectural claim without operational basis. With it, every Action record is self-evidencing on which version governed it.

**A1.07 path retraceability.** The commitment that any path through substrate state is retraceable from the current state. Retroactivity treatment supports retraceability for the temporal dimension: given any Action record, the path from that record back to the DNA version that governed it is retraceable through provenance field 4 and version history. Retraceability and retroactivity treatment are architecturally complementary — retraceability names the substrate property; retroactivity treatment names the rule that makes temporal retracing meaningful.

**A1.10 determinism.** Given DNA version and inputs, cell behavior was deterministic. Retroactivity treatment preserves this: prior DNA plus prior inputs plus prior outputs constitute a deterministically reconstructible record, undisturbed by subsequent DNA changes.

**A2.01 inspect.** The right to inspect any substrate content. Prior DNA versions are substrate content; they are inspectable. Version history is not a black box; it is an inspectable substrate record that any human with appropriate access can read.

---

## 7. Operational implications

### 7.1 Governance with retroactivity awareness

Deployments configure directed selection governance processes with the awareness that each DNA modification produces a retroactivity boundary. Governance review at modification time understands that new DNA will govern forward from the modification timestamp, and that the record of what governed behavior before that timestamp is preserved and auditable. This awareness shapes how governance frames modification decisions — not as retroactive corrections of prior behavior, but as forward-looking governance changes.

### 7.2 Compliance scope accuracy

Compliance frameworks that rely on CKS architecture use the A6.02 retroactivity treatment to scope compliance claims accurately. A compliance demonstration for period P uses the DNA version active during P. A DNA change that improves compliance for future periods does not alter the compliance analysis for prior periods. Compliance teams reading this note understand that the DNA version active at the regulated time — not the current DNA version — is the correct standard against which to evaluate period-P records.

### 7.3 Audit teams read against the active version at time

Audit teams examining Action records know to retrieve the DNA version active at the time of the records being audited, not the current version. Provenance field 4 on each record is the primary reference; version history per B2.69 is the retrieval mechanism; A2.01 inspect right is the access vehicle. Auditors do not need to reconstruct which version governed a record through external documentation — the record carries the reference.

### 7.4 Cross-level retroactivity

Self DNA changes have retroactivity at the Self level. A Self DNA change at time T applies forward at the Self level from T onward. Cell-level Action records created before T remain governed by the Self DNA version that was active before T. Cross-level DNA changes — where a Self DNA change affects what cell-level DNA governs — have retroactivity at each level independently: Self DNA change applies forward at Self level from T; cell-level Action records before T remain under the Self DNA version before T. The retroactivity treatment does not collapse levels; it applies the forward-only rule at each level where governance operates.

---

## 8. Limits of the treatment

The retroactivity treatment is precise in both directions — what it requires and what it does not permit.

**Prior Action records are not reinterpretable under new DNA.** When DNA changes to V2, records created under V1 do not become V2 records. There is no architectural mechanism by which new DNA reaches backward. A governance process that attempts to re-evaluate V1 records as if V2 had been active earlier is operating outside the CKS retroactivity treatment; such re-evaluation may be a useful analytical exercise, but it is not what the substrate records show.

**New DNA is not blocked from governing future behavior.** Retroactivity treatment addresses the backward direction only. New DNA applies forward without restriction: all cell behavior from the modification timestamp onward is governed by new DNA. Retroactivity does not create a sunset period or a grace period in which prior DNA continues to govern after the modification.

**Prior DNA was not wrong.** Prior DNA was the governing specification at the time it was active. The fact that it was modified does not make it incorrect retroactively. It was the authoritative, human-governed specification for the period it governed. Rollback similarly does not retroactively make the intermediate version an error; it is a governance decision that creates a new version going forward.

**Rollback does not undo history.** A rollback produces a new DNA version with prior content. It does not delete the intermediate version from version history. Action records created during the intermediate period remain governed by the intermediate version's DNA. The history of governance decisions — including the intermediate version and its period of active governance — is preserved.

**Retroactivity treatment is not the same as version management.** B2.69 formalizes how DNA versions are stored, retrieved, and compared. B2.70 formalizes the rule governing how those versions relate to the operational history they produced. These are distinct architectural commitments. Version management is the mechanism; retroactivity treatment is the rule the mechanism serves. A system that stores DNA versions without applying the forward-only retroactivity rule has version management without retroactivity treatment; a system that claims retroactivity treatment without storing prior versions has the rule without the mechanism to enforce it.

**All DNA changes follow retroactivity treatment equally.** There is no class of directed selection change that bypasses the A6.02 treatment. Emergency modifications, minor edits, major restructurings, and rollbacks all follow the same rule: new DNA applies forward from the modification timestamp; prior records remain governed by the DNA active at the time of their creation.

---

## 9. One-sentence test

A CKS deployment correctly implements retroactivity treatment for DNA changes if and only if: for any Action record in the system, an auditor can identify — from provenance field 4 on that record — which DNA version governed the operation, retrieve that version from version history, and verify that the behavior recorded is consistent with the DNA and inputs that were active at the time, without the current DNA version affecting this analysis in any way.

---

## 10. Why naming this treatment as standalone matters

Retroactivity treatment is architecturally load-bearing for three domains simultaneously: behavioral audit, regulatory compliance, and determinism preservation. Each domain places distinct requirements on the system, and each requirement is satisfied by the same underlying architectural structure — the forward-only application rule enforced by A2.40 provenance field 4 and version history preservation. A deployment that understands the retroactivity rule can satisfy all three domain requirements from a single architectural commitment rather than from three separate procedural controls.

Naming this as a standalone note in the B1.14 decomposition places it in the public record as a named, derivable commitment with specific operational implications. B2.67 established directed selection scope. B2.68 established modification governance. B2.69 established version management. B2.70 establishes retroactivity treatment — the rule that version management serves. B2.71 will formalize directed selection evolution patterns; B2.72 will formalize directed selection verification. Together, these six notes close the B1.14 decomposition and establish every patentable dimension of directed selection as prior art under the author's name.

Subsequent Phase B2 notes (B2.73–B2.78) will continue with the B1.15 action-feedback decomposition, where a parallel set of retroactivity and provenance questions arises in the context of action-evidence-driven DNA proposals. The retroactivity treatment formalized here for directed selection provides the foundational rule that the action-feedback treatment will inherit and extend.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Forward-Only Governance: Retroactivity Treatment for DNA Changes in the Coordination Knowledge Substrate Pattern.* May 12, 2026. ORCID: 0009-0004-8065-3235.
