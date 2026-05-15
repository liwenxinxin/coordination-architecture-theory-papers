# Inter-Self Conflict Registry Structure

**Series:** CKS Derivation Notes — Series D (Paper 3), Phase D2
**Note:** D2.13 — #508
**Working title:** Inter-Self Conflict Registry Structure: Seven-Field Registry Entry (Conflict ID, Both Sides, Attribution, Class, Tier Assignment, Resolution Status, Outcome Record) With Lifecycle From Detection Through Dissolution as the Compliance Record for Paper 1 Claim 2 at Inter-Self Scope
**Derives from:** D1.13–D1.15 (three-tier conflict handling sub-commitments)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

The three-tier inter-Self conflict-handling mechanism established in Paper 3 Claim 3 requires a concrete governance artifact within the shared substrate: a conflict registry that records every conflict arising during a Full Aspect Integration (FAI) event from initial detection through final resolution or preservation. This note formalizes the registry's entry structure as seven fields — Conflict ID, Both Sides Preserved, Attribution, Conflict Class, Tier Assignment, Resolution Status, and Outcome Record — and its lifecycle across three phases: at merge (creation), during operation (status transitions), and at dissolution (persistence and carry-through). The note establishes the registry as the compliance record for Paper 1 Claim 2 at inter-Self scope, states the inheritance relationship to the Paper 2 A1.03 conflict registry at intra-Self scope, identifies the incomplete-registry anti-pattern, and provides an operational test an auditor can apply to a completed FAI event to verify that no conflict was silently collapsed.

---

## 1. Position and derivation

D2.13 is the thirteenth note in Phase D2 of the Series D derivation sequence. It derives from the D1.13–D1.15 cluster, which formalizes the three sub-commitments of the three-tier conflict-handling mechanism: D1.13 (preserve as substrate-level state default), D1.14 (resolve via orchestration with inspectable rules), and D1.15 (escalate to humans across joint authority). Each of those sub-commitments presupposes a governance artifact that tracks which conflicts exist, which tier is handling them, and what their current status is. D2.13 formalizes that artifact: the inter-Self conflict registry maintained within the shared substrate.

The source claim is Paper 3 Claim 3, which establishes the three-tier mechanism as the operational form of Paper 1 §5.3's two-level conflict handling when extended to the inter-Self coordination scope. Paper 1 Claim 2 commits, at cell scope, to conflicts being preserved as substrate content with both sides retained and neither side auto-collapsed. D2.13 operationalizes what that commitment requires at inter-Self scope: a registry entry structure that makes the commitment verifiable, and a lifecycle that keeps the registry current as a live governance document throughout the FAI event.

---

## 2. Why the registry is the operational form of Paper 1 Claim 2 at inter-Self scope

Paper 1 Claim 2 states that conflicts are preserved as substrate content, with both sides retained. The claim is architectural: it is a commitment about how the substrate is structured, not merely a policy about how conflicts are processed. At cell scope, this commitment is operationalized by recording conflicts as first-class entries in the substrate with explicit content on both sides rather than overwriting one side or silently merging.

At inter-Self scope, the same commitment produces the same requirement: conflicts arising during an FAI event must be recorded as first-class entries in the shared substrate, each with both contributed sides preserved in full. But the inter-Self scope adds dimensions that the cell-scope implementation does not face. The conflicting specifications originate from distinct contributing Selves' aspects, so attribution must be traceable across the perimeter. The three-tier mechanism introduces a tier-selection decision that itself requires governance documentation. And the cross-perimeter joint-authority escalation tier requires a record of when and how human governance responded.

The seven-field structure formalizes all of these dimensions. The fields are not decorative metadata appended to a simpler conflict record; each field implements a specific aspect of the Paper 1 Claim 2 commitment at inter-Self scope. The fields together constitute a complete conflict-as-first-class implementation for the inter-Self coordination environment.

---

## 3. Seven-field entry structure

Each entry in the inter-Self conflict registry contains the following seven fields.

### Field 1 — Conflict ID

A unique identifier for this conflict within the shared substrate. The Conflict ID is the addressing handle that allows the registry entry to be referenced by other substrate content, by the three-tier mechanism's operation, by escalation records, and by auditors reviewing governance compliance. The Conflict ID is assigned at the moment of detection (at merge, per §4 below) and does not change through the entry's lifecycle. The uniqueness requirement is scope-wide within the shared substrate for the duration of the FAI event.

The Conflict ID implements first-class registration: a conflict without an identifier has not been registered and does not exist as a governance object, regardless of whether it was detected. The presence of an identifier is the marker that a conflict has been elevated from a detected condition to a first-class substrate state.

### Field 2 — Both Sides Preserved

The complete content of each conflicting specification, with both sides retained in full as substrate content. This field is the direct implementation of Paper 1 Claim 2 at inter-Self scope. Neither side is summarized, truncated, or replaced by a merged representation. Both sides remain addressable as substrate content throughout the entry's lifecycle.

"Both sides" is a minimum cardinality, not a constraint on maximum. If an FAI event involves three or more participating Selves and a conflict arises among more than two contributed aspects, the field holds all conflicting sides, each in full. The architectural commitment is complete preservation of every conflicting specification, not preservation of exactly two.

The Both Sides Preserved field is what makes the registry an evidence artifact rather than a log. An auditor reviewing the registry can read the original specifications as they existed at the moment of conflict detection. No reconstruction from other sources is required.

### Field 3 — Attribution

The identity of which contributing Self's aspect produced each side of the conflict, with provenance references linking each side to the contributing aspect within the shared substrate. Attribution is the inter-Self extension of the provenance requirement that Paper 1 imposes at cell scope. At cell scope, conflicts are attributed to the operations or inputs that produced each side. At inter-Self scope, attribution identifies the participating Self whose contributed aspect is the source of each side.

Attribution serves two governance functions. First, it allows the three-tier mechanism's escalation tier to route a conflict to the correct joint-governance arrangement — the governance authorities of the Selves whose aspects are in conflict. Second, it allows the dissolution-time carry-through operation (§4.3 below) to attach resolution or preservation records to the home substrates of the contributing Selves, so that each Self's home substrate reflects the inter-Self governance outcome for that Self's contributed content.

Attribution does not assign fault or priority. It is a provenance record, not a ranking. The preservation commitment of Field 2 holds for all sides regardless of which Self contributed them.

### Field 4 — Conflict Class

A classification of this conflict against the taxonomy of conflict classes defined in the shared substrate's orchestration rules. The Conflict Class field records whether this conflict matches a known class for which a pre-authored resolution rule exists — making it eligible for the resolve tier — or is an unknown class that the orchestration rules do not cover, making it ineligible for the resolve tier at its current configuration.

The Conflict Class is the routing input for tier assignment (Field 5). It is not determined by the conflict's content alone; it is determined by the content in relation to the orchestration rules in force at the time of detection. The same substantive conflict may be a known class in one FAI event configuration and an unknown class in another if the orchestration rules differ.

The Conflict Class field is itself subject to governance: orchestration rules are substrate content under joint authority (per Paper 3 Claim 5), and the taxonomy of conflict classes can be extended by the participating Selves' governance authorities. An entry marked as unknown class creates an implicit governance signal: the conflict class taxonomy may need extension.

### Field 5 — Tier Assignment

The tier to which this conflict is assigned by the three-tier mechanism, along with the governance rationale for the assignment. Possible values are: **Preserve** (tier 1 — conflict is held as first-class substrate state without resolution); **Resolve** (tier 2 — conflict matches a known class and is eligible for orchestration-rule resolution); **Escalate** (tier 3 — conflict is an unknown class or is otherwise not resolvable under current orchestration rules and must be surfaced to human governance).

The governance rationale records why this tier was selected. For a Preserve assignment, the rationale may record that preservation is the configured default for this event. For a Resolve assignment, the rationale identifies the orchestration rule applied. For an Escalate assignment, the rationale identifies the reason for escalation — unknown class, orchestration rule conflict, or governance authority determination that this conflict exceeds the resolve tier's scope.

Tier Assignment is not a permanent property. The three-tier mechanism can reassign a conflict's tier if circumstances change — for example, if a previously unknown conflict class is resolved at the governance level and a new orchestration rule is authored and applied, a conflict initially assigned to the Escalate tier may be reassigned to the Resolve tier. Each reassignment is recorded in this field with an updated rationale and a timestamp.

### Field 6 — Resolution Status

The current governance status of this conflict. The status vocabulary has five values:

- **OPEN** — the conflict has been detected and registered, tier assignment is in progress or complete, but the conflict has not yet reached a terminal state. This is the initial status assigned at entry creation.
- **PRESERVED** — tier 1 outcome. The conflict has been designated for preservation as first-class substrate state without resolution. This is a terminal status.
- **RESOLVED** — tier 2 outcome. The conflict has been resolved under an orchestration rule. This is a terminal status.
- **ESCALATED** — tier 3 outcome, pending. The conflict has been surfaced to human governance but a governance response has not yet been received. This is a non-terminal status: the entry remains open to governance action.
- **RESOLVED-BY-ESCALATION** — tier 3 outcome, complete. Human governance has responded and a resolution has been reached. This is a terminal status.

The Resolution Status field is the current-state indicator for the conflict as a governance object. OPEN entries are active governance obligations: the three-tier mechanism has not yet completed its operation on these conflicts. Non-terminal ESCALATED entries are pending governance obligations: human governance response is required. Terminal-status entries (PRESERVED, RESOLVED, RESOLVED-BY-ESCALATION) are closed governance obligations whose outcomes are recorded in Field 7.

### Field 7 — Outcome Record

For entries in terminal states, the content of the governance outcome. The form of the Outcome Record varies by terminal status:

- For **PRESERVED** entries: the preservation record, which documents the governance decision to preserve rather than resolve, the preservation format, and the carry-through designation (whether and how the preserved conflict will be annotated to participating Selves' home substrates at dissolution per §4.3).
- For **RESOLVED** entries: the resolution content — the outcome specification produced by applying the orchestration rule, the rule identifier, and the content of the resolution as it will be or has been applied to the contributing aspects.
- For **RESOLVED-BY-ESCALATION** entries: the escalation record (when escalation occurred, to which joint-governance arrangement, under what authority specification) and the governance response (the decision reached, the authority identifier, and the resolution content).

For entries in non-terminal states (OPEN, ESCALATED), the Outcome Record is empty or holds the partial escalation record pending governance response.

The Outcome Record closes the compliance chain. Field 2 preserves both sides; Field 7 records what happened to them. Together, these two fields are what allow an auditor to verify not only that both sides were retained but that the retention produced an auditable governance outcome rather than a silent dead end.

---

## 4. Registry lifecycle

The inter-Self conflict registry is a live governance document. It is not prepared retrospectively at the end of an FAI event. It is maintained continuously from the first merge operation and reflects the current governance status of all detected conflicts at every moment during the event.

### 4.1 At merge: entry creation

Conflict detection occurs during merge operations (per D2.07). When a merge operation detects a conflict between two or more contributed aspects, a registry entry is created immediately. The entry is initialized with Fields 1 through 5 populated (Conflict ID assigned, both sides recorded, attribution established, conflict class determined, initial tier assignment made) and Field 6 set to OPEN. Field 7 is empty at creation.

The creation of the entry at the moment of detection is the operational implementation of first-class registration. A conflict that has been detected but not yet registered is not a first-class governance object. The transition from detected to registered is the transition from a merge artifact to a substrate state.

The timing requirement — entry creation at detection rather than deferred to a later processing step — is what preserves the registry's completeness guarantee. A registry that batches entry creation or defers it to a separate processing phase creates a window during which detected conflicts are not yet registered, and the registry does not reflect the full set of detected conflicts.

### 4.2 During operation: status transitions

As the three-tier mechanism operates on registered conflicts, entries transition through status values. The transitions follow the tier assignment:

- A Preserve-assigned entry transitions from OPEN to PRESERVED when the preservation operation is complete and the preservation record is written to Field 7.
- A Resolve-assigned entry transitions from OPEN to RESOLVED when the orchestration rule is applied and the resolution content is written to Field 7.
- An Escalate-assigned entry transitions from OPEN to ESCALATED when the escalation is transmitted to the designated joint-governance arrangement. It transitions from ESCALATED to RESOLVED-BY-ESCALATION when the governance response is received and the outcome record is written to Field 7.

The registry's current state at any moment is the complete governance picture of the FAI event to that point: OPEN entries are active obligations, ESCALATED entries are pending obligations, and entries in terminal states are closed obligations with recorded outcomes.

The registry is substrate content within the shared substrate. This means it is subject to the governance properties that Paper 3 §4 establishes for the shared substrate: it is readable and modifiable by the participating Selves' governance authorities under the three-rights framework (inspect, modify, override), and changes to the registry are themselves subject to the shared substrate's provenance and accountability mechanisms.

### 4.3 At dissolution: persistence and carry-through

At FAI event dissolution, the registry enters its terminal lifecycle phase. Registry entries in terminal states are subject to the shared substrate's persistence policy (D1.04). The persistence policy — itself substrate content under joint authority (per Paper 3 Claim 5) — determines which registry entries are retained as Locus 2 content (content that persists in the dissolution record) and which are not carried forward.

Two additional operations occur at dissolution for specific entry types:

Entries with status PRESERVED undergo the carry-through operation: preserved conflicts are annotated to the participating Selves' home substrates as evolution-feed annotations (per D1.16 and Paper 3 §7). The preserved conflict, with both sides retained, becomes a substrate annotation in each contributing Self's home substrate, so that the inter-Self governance outcome is visible within each Self's reasoning layer in subsequent operations.

The registry as a whole, to the extent it is retained under the persistence policy, becomes the dissolution-record evidence that the FAI event's conflict governance was conducted in compliance with Paper 1 Claim 2 at inter-Self scope.

---

## 5. The registry as compliance record for Paper 1 Claim 2 at inter-Self scope

The inter-Self conflict registry is the compliance record for Paper 1 Claim 2 at inter-Self scope. Paper 1 Claim 2 commits to conflicts being preserved as substrate content with both sides retained. At inter-Self scope, this commitment is verifiable if and only if there exists a record in which every detected conflict has been registered with both sides preserved and a documented governance outcome.

The registry is that record. Its role as compliance record is not a secondary function added for auditing convenience; it is the primary architectural function that gives the registry its design requirements. The seven-field structure exists because the compliance function requires each field: first-class addressing (Field 1), both-sides retention evidence (Field 2), attribution trail (Field 3), tier-selection documentation (Fields 4 and 5), current governance status (Field 6), and terminal outcome record (Field 7).

The compliance function has a specific adversarial implication: the silent-conflict-collapse failure mode. In silent conflict collapse, a merge operation detects a conflict, selects one side, and discards the other without registration. The result appears to be a successful merge; no evidence of the discarded side remains in the substrate. The conflict registry closes this gap by making silent collapse detectable: if a conflict was detected and no entry was created, the detection-without-registration gap is itself a governance failure that leaves a forensic trace (in merge operation logs, in the discrepancy between contributed aspects and registered conflicts, or in the absence of expected entries). An auditor cannot prove a negative — cannot prove that no unregistered conflict occurred — but can verify that for every registered conflict, both sides are preserved. The registry converts the Paper 1 Claim 2 commitment from an asserted property to a verifiable one.

---

## 6. Inheritance from Paper 2: the A1.03 conflict registry at intra-Self scope

The inter-Self conflict registry is the analog, at inter-Self scope, of the Paper 2 A1.03 conflict registry at intra-Self scope. Paper 2 establishes a conflict registry at intra-Self scope that records conflicts arising within a single Self across the cell, aspect, and Self levels of the multi-level governance architecture. The A1.03 registry applies the same Paper 1 Claim 2 commitment at intra-Self scope: every conflict is registered as a first-class entry with both sides preserved.

The structural relationship is direct inheritance with scope extension. The entry structure at inter-Self scope uses the same seven-field architecture as the A1.03 registry. The differences are in the scope of the attribution field (inter-Self attribution identifies contributing Selves' aspects rather than intra-Self governance objects) and the scope of the escalation tier (inter-Self escalation surfaces to the joint-governance arrangement of participating Selves rather than to intra-Self governance authorities). Everything else — the conflict ID, the both-sides preservation, the conflict class classification, the tier assignment, the status vocabulary, the outcome record structure — is directly inherited.

This inheritance is architecturally significant. The registry pattern is the same pattern applied at progressively larger coordination scopes: within-cell (Paper 1 substrate), within-Self at multiple levels (Paper 2 A1.03), across Selves (Paper 3 D2.13). The consistency of the pattern across scopes is what allows the Paper 1 Claim 2 compliance function to operate at every scope level using the same audit discipline.

---

## 7. Anti-pattern: the incomplete registry

An inter-Self conflict registry that fails to include all detected conflicts, or that has entries with one side of a conflict missing, violates Paper 1 Claim 2 at inter-Self scope. This is the incomplete-registry anti-pattern, and it takes two forms.

**Form 1 — Missing entries.** A conflict was detected during a merge operation but no entry was created in the registry. The detection-without-registration gap may arise from a merge operation that applies resolution logic before registration (so that by the time the registry is updated, one side has already been discarded), from a batch registration process that drops entries under error conditions, or from a deliberate architectural choice to treat certain conflict classes as not requiring registration. All three produce the same governance outcome: a conflict has been silently collapsed. The registry does not reflect the full set of detected conflicts, and the compliance record for Paper 1 Claim 2 is incomplete.

**Form 2 — One-sided entries.** A conflict has an entry in the registry, but the entry holds only one side of the conflict in Field 2. The other side has been omitted, summarized, or replaced by a merged representation. This entry satisfies the first-class registration requirement (the conflict has an identifier and a registry presence) but violates the both-sides preservation requirement. An auditor reviewing the entry cannot verify what the discarded side contained. The compliance record is present but incomplete.

Both forms of the incomplete-registry anti-pattern are violations of Paper 1 Claim 2 at inter-Self scope, regardless of the governance motivation that produced them. A conflict class that is excluded from registration on the grounds that it is "too minor" or "routinely resolvable" is not a class for which the Paper 1 Claim 2 commitment has been satisfied; it is a class for which the commitment has been waived without architectural authority to waive it.

---

## 8. Operational test

For a completed FAI event, an observer can apply the following test to verify that the inter-Self conflict registry satisfies its compliance function.

**Step 1 — Coverage.** For each conflict detected during the FAI event's merge operations, verify that a registry entry exists with the conflict's Conflict ID. The set of detected conflicts is derivable from merge operation records within the shared substrate. Coverage is satisfied if and only if every detected conflict has a corresponding entry.

**Step 2 — Both-sides preservation.** For each registry entry, verify that Field 2 holds the complete content of both (or all) conflicting specifications, not summaries or merge products. Both-sides preservation is satisfied if and only if each side is independently readable as its original contributed content.

**Step 3 — Tier assignment.** For each registry entry, verify that Field 5 holds a tier assignment and a governance rationale for that assignment. Tier assignment is satisfied if and only if every entry has a designated tier with a documented rationale.

**Step 4 — Terminal status and outcome record.** For each registry entry, verify that Field 6 holds a terminal status (PRESERVED, RESOLVED, or RESOLVED-BY-ESCALATION) and that Field 7 holds an outcome record consistent with that status. Terminal closure is satisfied if and only if no entry remains in OPEN or ESCALATED status at the conclusion of the event.

The test passes if and only if all four steps are satisfied for all entries. A failure at Step 1 indicates the incomplete-registry anti-pattern (Form 1). A failure at Step 2 indicates the incomplete-registry anti-pattern (Form 2). A failure at Step 3 indicates a tier-assignment governance gap (a conflict was registered but not processed by the three-tier mechanism). A failure at Step 4 indicates an unresolved governance obligation (a conflict was processed but not brought to closure, or was escalated and the governance response was not recorded).

An observer who cannot access the merge operation records for Step 1 can still apply Steps 2 through 4 to all existing entries. This partial test verifies the integrity of registered entries but cannot verify coverage. Full compliance verification requires access to the merge operation records.

---

## 9. Relationship to downstream notes

D2.13 supplies the registry structure that several downstream Phase D2 notes presuppose. D2.14 (tier-selection logic as substrate content) specifies how the Conflict Class and Tier Assignment fields are populated. D2.15 (escalation record structure) specifies the detailed structure of the escalation record within Field 7 for ESCALATED and RESOLVED-BY-ESCALATION entries. D2.16 (preservation record carry-through at dissolution) specifies how PRESERVED entries in Field 7 are formatted for the home-substrate annotation operation at dissolution. Notes in Phase D3 will formalize the incomplete-registry anti-pattern at the violation level, identifying the governance failure modes that produce Form 1 and Form 2 incomplete registries and the detection methods available to auditors.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Inter-Self Conflict Registry Structure.* CKS Derivation Notes, Series D, Note D2.13 (#508). May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
