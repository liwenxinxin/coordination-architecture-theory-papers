# AP-10: Shallow-Reference Merge

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes AP-10: Shallow-Reference Merge, the third Taxonomy Category 5 (Perimeter and Content Failures) anti-pattern in the Phase D3 series. The anti-pattern occurs when a Full Aspect Integration (FAI) event is configured to use the provenance-carry-over merge pattern — the highest-auditability merge variant, distinguished by bidirectional navigability between shared-substrate content and the contributing Self's home governance records — but the provenance depth is set to minimal, producing level-1 references that name the FAI event without enabling navigation to the contributing Self's home governance history. The form is provenance-carry-over merge; the substance is full merge with FAI-event attribution only. The violation is misrepresentation: the configuration record claims governance properties the event does not deliver. The note identifies detection criteria, traces the governance commitments violated (Paper 3 D1.09 primary; Paper 1 A1.07 and Paper 3 D2.09 secondary), articulates four categories of consequence including chain laundering risk, maps the intra-Self analog in Paper 2's lineage-preserved-union mating, and provides the complete prevention through D2.09's three requirements and the bidirectional traceability test.

---

## 1. Anti-Pattern Name and Category

**Anti-pattern:** AP-10: Shallow-Reference Merge

**Category:** Taxonomy Category 5 — Perimeter and Content Failures

**Series position:** D3.20, note #595 in the CKS derivation note series.

Taxonomy Category 5 covers failures at the boundary between governance scopes: failures that occur not within a single Self's home governance architecture but at the point where content crosses the perimeter — contributed from a home substrate into the shared substrate, carried across the inter-Self boundary, or referenced back across it for accountability purposes. AP-10 is a boundary failure of a specific and consequential kind: it does not involve a malformed contribution or a content error, but a governance record that misrepresents the traceability properties of an event that was, in every other respect, correctly executed.

---

## 2. Description

The provenance-carry-over merge pattern (D1.09 Pattern Variant 3) is the highest-auditability merge variant available for FAI events. Its defining feature is bidirectional traceability: an observer holding shared-substrate content produced by a provenance-carry-over merge event can navigate from that content to the contributing Self's home governance records at the authorized depth, and the contributing Self's home governance records carry forward-references to the shared substrate where that content now lives. This bidirectionality is not an enhancement on top of full merge — it is the architectural property that makes provenance-carry-over merge a distinct pattern rather than a relabeled version of full merge. Full merge (D1.08) absorbs contributing content into the shared substrate without establishing navigable cross-perimeter references; provenance-carry-over merge does the same absorption and adds the navigable reference structure that makes the event's origin chain recoverable by any authorized observer.

Shallow-Reference Merge occurs when an FAI event is configured to use the provenance-carry-over pattern but the provenance depth configuration (D1.22 Dimension 5) is set to Option A — the minimal setting that produces only a level-1 reference: "this content came from FAI event X." A level-1 reference names the originating event. It does not provide a navigable path to the contributing Self's home governance records, does not reference the specific aspects whose content was contributed, and does not allow an observer to follow the provenance chain beyond the FAI event boundary. From the shared substrate, the origin chain terminates at the event label. The home governance history that produced the contributed content is unreachable.

The result is a false equivalence in the governance record. The event's configuration block reads: provenance-carry-over merge, Pattern Variant 3. An observer consulting that record, whether a partner Self, a governance oversight function, or an external auditor, has reasonable grounds to believe that bidirectional traceability exists. It does not. The actual auditability of the event is identical to what full merge would have produced: the content is present in the shared substrate, attributed to the FAI event that brought it there, with no navigable path to its home governance origin. The provenance-carry-over label adds no traceability; it adds only a misrepresentation.

This is governance theater at the merge pattern level. The configuration makes a promise the event does not keep. The promise is not incidental: it is the specific commitment that distinguishes the pattern selected from the default alternative.

---

## 3. Detection Criteria

Three conditions, individually sufficient and jointly diagnostic, identify AP-10 in a governed inter-Self coordination architecture:

**Criterion 1 — Depth mismatch in event configuration.** The FAI event configuration record specifies provenance-carry-over merge as the pattern variant but sets provenance depth to Option A (minimal — FAI event reference only). Option A is the correct depth configuration for operational scenarios where the contributing Self has not authorized home record access across the perimeter. It is incompatible with a provenance-carry-over merge commitment, which requires at minimum Option B (aspect-level references enabling navigation to the contributing Self's governance records for the contributed aspects). The combination of provenance-carry-over pattern label with Option A depth is definitionally a shallow-reference merge configuration.

**Criterion 2 — Level-2 navigation failure.** Attempting to navigate from any shared-substrate content produced by the event to the contributing Self's home governance records fails at level 2. Level-1 navigation — reaching the FAI event record — succeeds, because the FAI event reference exists and is addressable. Level-2 navigation — proceeding from the FAI event reference to the contributing Self's home governance records for the contributed aspects — finds either a non-existent reference, an inaccessible record, or no reference at all. The provenance chain is navigable to the FAI event boundary and opaque beyond it.

**Criterion 3 — Reference structures with broken endpoints.** Provenance reference structures exist in the shared substrate (satisfying the syntactic requirements of a provenance-carry-over merge record) but point to records in contributing Selves' home substrates that are non-existent, have not been created, or are inaccessible under the governing perimeter configuration. The reference structures are present; what they reference is not reachable. This is structurally different from an event that simply has no provenance references: it is an event whose provenance structures create the appearance of navigability while blocking the navigation.

---

## 4. Governance Commitment Violated

**Primary violation — Paper 3 D1.09 (provenance-carry-over merge pattern).**

D1.09 specifies the provenance-carry-over merge pattern as the merge variant committed to bidirectional traceability as its architectural distinguishing property. The pattern is not merely full merge plus a provenance field; it is full merge with a structural commitment that the provenance field is navigable in both directions across the perimeter. Shallow-reference merge satisfies the syntactic form of D1.09 Pattern Variant 3 — it uses the correct pattern label, produces provenance reference structures, and is recorded in the configuration as provenance-carry-over. It does not satisfy the semantic commitment: the distinguishing feature that separates Pattern Variant 3 from Pattern Variant 1 (full merge) is absent. The pattern label is present; the pattern is not.

**Secondary violation — Paper 1 A1.07 (path retraceability).**

Path retraceability requires that the provenance chain for any governed substrate content be navigable — that an authorized observer can follow the chain from the content to its origin, step by step, without encountering broken links or inaccessible records. Shallow-reference merge produces a provenance chain that terminates at the FAI event boundary. The contributing Self's home governance history — the actual origin of the contributed content — is unreachable. Nominal references that cannot be followed do not satisfy path retraceability. A reference that exists in the substrate but points to a record the observer cannot reach is not a provenance link; it is an unredeemable IOU in the accountability chain.

**Operational reference — Paper 3 D2.09 (provenance-carry-over merge requirements).**

D2.09 establishes three requirements for a compliant provenance-carry-over merge: Requirement 1 — depth authorization must specify a non-minimal depth, at minimum Option B; Requirement 2 — reference construction at contribution time must establish navigable references to the contributing Self's home governance records at the authorized depth; Requirement 3 — the bidirectional traceability test must pass, meaning navigation from shared-substrate content to the contributing Self's home records succeeds at the authorized depth. Shallow-reference merge fails all three: it specifies Option A depth (violating Requirement 1), constructs no navigable cross-perimeter references (violating Requirement 2), and fails the bidirectional traceability test at level 2 (violating Requirement 3).

---

## 5. Consequences

**Consequence 1 — False governance record.**

The event produces a configuration record that claims higher auditability than the event delivers. The configuration says: provenance-carry-over merge, the highest-auditability pattern. The actual auditability is: full merge with FAI-event attribution. Any party consulting the governance record to understand what traceability exists will be misled. The error is not in the record's accuracy about what happened mechanically — the content was contributed, the event completed, the shared substrate was updated. The error is in the record's characterization of the governance properties the event established. Governance records that misrepresent governance properties are worse than incomplete records: they actively direct oversight attention to a level of assurance that does not exist.

**Consequence 2 — Audit failure.**

Regulatory or governance audit functions (D2.63) that rely on the provenance-carry-over event record to verify traceability will find, upon attempting level-2 navigation, that the references are non-navigable. This may be treated as a documentation failure, a record-keeping failure, or a governance breach, depending on the audit framework. In each case the governing parties face a finding that their governance records do not support the traceability they represent. The practical impact is significant: the distinction between "we configured this event for maximum auditability" and "we configured this event for maximum auditability but the references don't work" is not a technicality in an audit context. It is the difference between the governance record being correct and the governance record being false.

**Consequence 3 — Trust miscalibration across governance perimeters.**

Governance trust calibration (D2.29) depends on each party to an inter-Self relationship having accurate knowledge of the traceability properties governing their shared-substrate relationship. Shallow-reference merge causes partner Selves to believe that provenance-carry-over depth exists when it does not. A partner Self that accepts content from a shared substrate, believing the provenance chain to be navigable to the contributing Self's home governance records, is making governance decisions on false premises. The partner may rely on the perceived provenance depth for its own governance purposes — its own audit trail, its own evolution authorization decisions — and all of those reliant decisions inherit the false premise. Trust that is calibrated to governance properties that do not exist is, in operational terms, misplaced trust.

**Consequence 4 — Chain laundering conditions.**

Chain laundering (D2.26) occurs when FAI-origin content is re-contributed to a subsequent FAI event without the provenance chain that would allow the subsequent event's participants to trace the content's origin. Shallow references from an AP-10 event create the structural preconditions for chain laundering in exactly this way. The content in the shared substrate carries what appears to be a provenance-carry-over reference — the label is present, the reference structure exists — but the reference is non-navigable. When that content is re-contributed in a subsequent FAI event, the receiving parties may accept the apparent provenance depth as sufficient to satisfy their own provenance-carry-over requirements. The actual origin chain cannot be recovered. Each subsequent FAI event that relies on the shallow references as an adequate provenance basis moves the origin further out of reach. The laundering is not intentional — it is structural. AP-10 events are the upstream condition that makes chain laundering in subsequent events probable rather than exceptional.

---

## 6. Intra-Self Analog

The intra-Self analog is Paper 2's lineage-preserved-union mating (C1.14 / B1.06): the mating of two entities within a single Self's governance structure that is configured to be lineage-preserved-union — the pattern variant that maintains navigable cross-lineage references so that offspring content can be traced to both contributing lineages — but produces only nominal cross-lineage references that do not actually support navigation through the lineage chains.

The structural parallel is exact. Lineage-preserved-union mating is the highest-auditability intra-Self combination primitive, distinguished from union mating by the same property that distinguishes provenance-carry-over merge from full merge: navigable references that make the origin chain traceable rather than merely labeled. A lineage-preserved-union mating that produces references pointing to non-existent or inaccessible lineage records has the form of the most rigorous pattern while delivering only nominal compliance. An observer trying to trace an offspring entity's governance history finds the lineage chain terminating at the mating event boundary — the same level-2 navigation failure AP-10 produces at the inter-Self boundary.

The form-versus-substance problem is identical at both scopes. At intra-Self scope, the governance record claims lineage-preserved-union mating; the actual traceability is union mating. At inter-Self scope, the governance record claims provenance-carry-over merge; the actual traceability is full merge. In each case the distinguishing feature of the claimed pattern — navigable cross-lineage references intra-Self, navigable cross-perimeter references inter-Self — is absent. In each case the absence is invisible to an observer consulting only the configuration record. In each case the correct resolution is either to deliver the navigable references the claimed pattern requires or to configure the honest lower-auditability pattern.

The intra-Self analog is useful not only as a structural mapping but as an indication of how pervasive the form-versus-substance failure mode is across the trilogy's governance architecture. The pattern — claiming the most rigorous combination primitive while delivering only the default — is structurally available at every scope where multiple combination primitives exist. AP-10 is the inter-Self instance of a failure mode that the trilogy's intra-Self architecture has already identified and addressed.

---

## 7. Resolution

The complete prevention for AP-10 is provided by D2.09's three requirements and the bidirectional traceability test. No additional mechanism is required; the existing machinery is sufficient if applied correctly.

**Requirement 1 — Non-minimal depth authorization.** An event configured as provenance-carry-over merge must specify a provenance depth of at minimum Option B. Option A is incompatible with provenance-carry-over merge by definition. If governance authorization for the event cannot produce a depth authorization above Option A — because the contributing Self has not agreed to provide navigable home record access — then provenance-carry-over merge is not available for the event. The correct response is Requirement 1 failure: the authorized depth does not support the requested pattern. The event should not proceed as provenance-carry-over merge.

**Requirement 2 — Reference construction at contribution time.** When a Self contributes aspects to the shared substrate under a provenance-carry-over merge configuration, the reference construction step must establish navigable references to the contributing Self's home governance records at the authorized depth. This means the references must point to records that exist, that are accessible to authorized observers crossing the perimeter, and that support the level-2 navigation the pattern commits to. Reference structures that satisfy the syntactic form without establishing the navigable endpoint do not satisfy Requirement 2. Reference construction should be verified at contribution time, not discovered as a failure during audit.

**Requirement 3 — The bidirectional traceability test.** The operational test for compliance is direct: take any piece of shared-substrate content produced by the event, follow its provenance references, and attempt to navigate to the contributing Self's home governance records at the authorized depth. If navigation succeeds — the records are reachable, the chain is followable — the event satisfies the bidirectional traceability commitment. If navigation fails at level 2, regardless of whether the reference structures are syntactically present, shallow-reference merge is present and the event record is non-compliant.

**The honest configuration fallback.** When governance cannot produce a depth authorization above Option A — when the contributing Self does not agree to provide navigable home record access across the perimeter — the correct configuration is full merge (D1.08), honestly recorded. Full merge with accurate configuration is a legitimate governance choice. It does not provide cross-perimeter traceability, and it does not claim to. Partners and auditors who consult the configuration record will find an accurate representation of the event's governance properties. The traceability they receive is limited; their knowledge of that limitation is correct.

Nominal provenance-carry-over merge — Option A depth with a provenance-carry-over label — is not a compromise between the two patterns. It is a misrepresentation. It delivers full-merge auditability while claiming provenance-carry-over auditability, creating a false record and all four categories of consequence documented in §5. The governance principle is: configure honestly at the actual auditability level the event delivers, and choose a higher-auditability configuration only when the governance authorization and reference infrastructure to support it are in place.

If systematic AP-10 conditions are discovered in an existing event record — events labeled as provenance-carry-over merge whose references fail level-2 navigation — the remediation sequence is: first, reclassify each affected event in the governance record to its actual pattern (full merge with FAI-event attribution); second, notify partner Selves whose trust calibration may have been affected; third, determine whether any chain laundering conditions have propagated to subsequent events using the affected content as provenance basis; fourth, update the FAI event configuration templates to enforce the depth authorization check before pattern selection is recorded.

---

## Conclusion

AP-10: Shallow-Reference Merge names the governance failure that occurs when provenance-carry-over merge is configured with minimal provenance depth, producing a nominal pattern label that claims the architecture's highest-auditability merge commitment while delivering only the traceability properties of full merge. The anti-pattern is not a content failure, an exchange failure, or a conflict-handling failure: it is a misrepresentation failure, in which the governance record asserts properties the event does not establish. The distinguishing feature of provenance-carry-over merge — bidirectional navigability from shared-substrate content to the contributing Self's home governance records — is the feature shallow-reference merge destroys while preserving the label. The consequence is governance theater: confidence in the provenance record is calibrated to assurance that does not exist, and every downstream governance decision that relies on that confidence inherits the false premise. The resolution is architectural discipline at the configuration stage: select the pattern the depth authorization can actually support, or configure full merge honestly when it cannot.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *AP-10: Shallow-Reference Merge.* May 15, 2026. ORCID: 0009-0004-8065-3235.
