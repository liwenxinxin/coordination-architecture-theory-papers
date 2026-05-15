# Anti-Pattern Detection Tests 31–40

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This derivation note presents ten binary detection tests (Tests 31–40) targeting the ten highest-priority anti-patterns from the Phase D3 taxonomy. The first five tests — covering Implicit Configuration (AP-6), Automated Governance (AP-24), Silent Conflict Collapse (AP-3), Exchange Bounding Violation (AP-8), and Automatic DNA Absorption (AP-4) — correspond to D3.29's top five detection priorities: failure modes whose presence most immediately undermines the governance integrity of a Full Aspect Integration event or a shared substrate deployment. The remaining five tests — covering Ungoverned Construction (AP-1), Ungoverned Dissolution (AP-2), Black Box Shared Substrate (AP-22), Governance Theater (AP-21), and Time-Pressure Governance Bypass (AP-19) — extend coverage to the next critical tier. Each test is binary: YES or NO from records alone, without inference. Every FAIL interpretation names the Phase D3 anti-pattern explicitly, creating a navigational bridge from test failure to the full anti-pattern treatment.

---

## 1. Purpose and Scope

Phase D5 of the CKS derivation series formalizes operational tests for Paper 3's commitments. Phase D2 operational variants establish the expected structural properties; Phase D3 anti-pattern formalizations name the failure modes that arise when those properties are absent or corrupted. The D5 test library serves practitioners conducting governance audits of shared substrate deployments and Full Aspect Integration events.

Two classes of tests exist within Phase D5. Compliance tests (D5.01 and D5.02) verify that the required structural elements are present: does a shared substrate exist, does it carry the required content types, are the required records in place? Anti-pattern detection tests (this note, D5.03) ask a different question: is a specific named failure mode demonstrably absent? The two classes are complementary. A deployment can satisfy every structural compliance check while harboring a governance anti-pattern detectable only through a targeted binary question. For example, a configuration record may exist — satisfying a compliance check — while having been authored after event operation began, which is the specific failure AP-6 names. Only a test that asks about joint authorization dating will surface it.

Tests in this note are binary. The auditor examines specified records and answers YES or NO. No contextual judgment, weighting, or partial credit applies. PASS means the evidence positively confirms the governance property's presence. FAIL means the evidence confirms, or fails to refute, the named anti-pattern's presence. Every FAIL closes with the anti-pattern identifier and name, enabling the auditor to navigate from failure to the full Phase D3 treatment.

The ten tests cover the ten most critical anti-patterns per D3.29's detection priority ordering. Tests 31–35 map to D3.29's top five priorities; Tests 36–40 extend to the next tier.

---

## 2. Anti-Pattern Detection Tests 31–40

---

### Test 31 — Implicit Configuration Detection

**Anti-pattern targeted:** AP-6 (Implicit Configuration)

**Records to examine:**
The shared substrate content store; the FAI configuration record, if any, with its timestamp and authorization fields; any record identifying the participating governance authorities.

**Binary question:**
Does an authored FAI configuration record exist as substrate content, jointly authorized by all participating governance authorities before the event began operation, covering all three minimum required dimensions?

**PASS indicates:**
A configuration record exists in the shared substrate as authored content; its authorization fields identify all participating governance authorities; the authorization timestamp predates the event operation start time; and the record covers, at minimum, cardinality specification, conflict-handling rules, and dissolution conditions. The configuration was established before the event began operating — there is no retroactive documentation of decisions already made implicitly.

**FAIL indicates:**
The configuration record is absent; or the record exists but one or more required dimensions are unaddressed; or the authorization is unilateral (one party only) rather than joint; or the authorization timestamp postdates the event operation start. Any of these conditions confirms that the event operated under implicit governance assumptions rather than explicit substrate-content configuration — **AP-6 (Implicit Configuration)**. Note that AP-6 commonly co-occurs with AP-1 (Ungoverned Construction); Test 36 should be applied in conjunction when this test fails.

---

### Test 32 — Automated Governance Detection

**Anti-pattern targeted:** AP-24 (Automated Governance)

**Records to examine:**
All governance decision records in the shared substrate: routing decisions, conflict resolution records, absorption authorizations, and any other record that constitutes a governance act over shared substrate content.

**Binary question:**
For every governance decision record in the shared substrate, does a human governance authorization record exist that the decision directly traces to?

**PASS indicates:**
Every governance decision record in the shared substrate cites or directly references a human governance authorization. The chain of authority terminates at a human-authored authorization, not at an automated system output. Automated systems may have executed or implemented decisions, but the authority for every decision traces back to a human authorization record that predates or coincides with the decision.

**FAIL indicates:**
Any governance decision record traces its authority to an automated system output — a routing algorithm's decision, an AI system's assessment, a rules-engine evaluation — rather than to a human governance authorization. A single such record is sufficient for failure. The architecture commits to human authority over governance decisions; when automated systems not only implement but also *authorize* decisions, the human-governed property of the shared substrate is violated — **AP-24 (Automated Governance)**. This is distinct from automated *execution* of human-authorized decisions, which does not fail this test.

---

### Test 33 — Silent Conflict Collapse Detection

**Anti-pattern targeted:** AP-3 (Silent Conflict Collapse)

**Records to examine:**
The content-domain specifications for each contributing aspect (identifying what domain of knowledge each aspect covers); the conflict registry for the shared substrate event.

**Binary question:**
For every pair of contributing aspects with overlapping content-domain specifications, does the conflict registry contain entries corresponding to the identified domain-overlap conflicts?

**PASS indicates:**
A systematic review of contributing aspects' content-domain specifications identifies all pairs with domain overlaps. For every such identified overlap, a corresponding registry entry exists in the conflict registry, carrying provenance to the contributing aspects and a status field. Conflicts are treated as first-class substrate state. The registry count of domain-overlap conflicts is consistent with the number of overlapping aspect-domain pairs.

**FAIL indicates:**
Domain overlaps exist among contributing aspects' specifications, but the conflict registry has no corresponding entries for some or all of those overlaps. The conflicts were not registered — they were collapsed (silently merged, overwritten, or discarded) during or before the FAI operation. The shared substrate presents a surface appearance of coherence without surfacing the genuine disagreements the contributing aspects carry — **AP-3 (Silent Conflict Collapse)**. This test requires that content-domain specifications be legible as substrate content; if they are absent or opaque, Test 38 (AP-22, Black Box Shared Substrate) should also be applied.

---

### Test 34 — Exchange Bounding Verification

**Anti-pattern targeted:** AP-8 (Exchange Bounding Violation)

**Records to examine:**
The D2.16 exchange bounding verification record for the FAI event; the shared substrate content inventory or content-type classification record.

**Binary question:**
Does a D2.16 exchange bounding verification record exist showing all four checks — DNA-and-action-layer content only, instinct-layer content absent, LLM-weight content absent, content-type classification complete — as passed?

**PASS indicates:**
A verification record exists that explicitly documents all four checks. The DNA-and-action-layer-only check confirms that all substrate content is classifiable as DNA-layer or action-layer content. The instinct-layer-absent check confirms that no instinct-layer content is present in the shared substrate. The LLM-weight-absent check confirms that no LLM-weight content is present. The content-type-classification-complete check confirms that every content item in the shared substrate has been classified. All four checks have PASS status.

**FAIL indicates:**
The verification record is absent entirely; or the record exists but one or more of the four checks is unresolved, incomplete, or marked as failed. If instinct-layer or LLM-weight content has entered the shared substrate, the exchange-bounding commitment from Paper 3's Claim 2 and Paper 2's instinct/reasoning separation are violated — **AP-8 (Exchange Bounding Violation)**. The exchange boundary is an architectural commitment, not a deployment preference; its violation corrupts the layer separation that the trilogy establishes as a non-negotiable structural spine.

---

### Test 35 — Automatic DNA Absorption Detection

**Anti-pattern targeted:** AP-4 (Automatic DNA Absorption)

**Records to examine:**
The home substrate DNA version history for each participating Self, with provenance fields for each version change; directed selection event records, if any; FAI dissolution records showing the evolution-feed pathway.

**Binary question:**
For each DNA change in a participating Self's home substrate that carries FAI-origin provenance, does a corresponding directed selection event record with governance authorization exist?

**PASS indicates:**
The DNA version history is legible with provenance fields. Every DNA change marked with FAI-origin provenance — indicating that the change source was content arriving through the FAI evolution-feed pathway — has a corresponding directed selection event record. Each such record carries a governance authorization from the home Self's governance authority. FAI-derived content reached DNA evolution through the directed selection mechanism with explicit human governance, not through automatic or unmediated absorption.

**FAIL indicates:**
FAI-origin DNA changes appear in the home substrate version history without corresponding directed selection records. FAI-derived content has been absorbed into the home DNA layer without directed selection governance — through mutation pathways, automatic ingestion rules, or unmediated write operations. This bypasses the governance-configured ingestion architecture Paper 3 §7 commits to, allowing inter-Self coordination outcomes to modify a Self's foundational DNA without the authority structure that directed selection requires — **AP-4 (Automatic DNA Absorption)**.

---

### Test 36 — Ungoverned Construction Detection

**Anti-pattern targeted:** AP-1 (Ungoverned Construction)

**Records to examine:**
The shared substrate construction record; pre-construction authorization records from all participating governance authorities.

**Binary question:**
Do construction records exist showing pre-construction authorization from all participating governance authorities before the shared substrate began operation?

**PASS indicates:**
A shared substrate construction record exists naming the event, the participating Selves, and the governance authorities of each. Pre-construction authorization records from every participating governance authority exist with timestamps predating the event operation start. All participating governance authorities are represented; no participant's governance authority is missing from the pre-construction record set.

**FAIL indicates:**
No construction record exists; or a construction record exists but one or more participating governance authorities' authorizations are absent; or authorizations exist but their timestamps postdate the shared substrate's operation start. A shared substrate that began operating without pre-construction authorization from all participating governance authorities was constructed outside the governance architecture — **AP-1 (Ungoverned Construction)**. This is the foundational anti-pattern: if construction is ungoverned, every subsequent governance claim about the event rests on a substrate whose origin is not itself authorized.

---

### Test 37 — Ungoverned Dissolution Detection

**Anti-pattern targeted:** AP-2 (Ungoverned Dissolution)

**Records to examine:**
The dissolution record for the FAI event; the persistence policy execution record; the hand-off boundary activation record.

**Binary question:**
Do dissolution records exist showing persistence policy execution and hand-off boundary activation with governance authorization?

**PASS indicates:**
Three records exist and are complete: a dissolution record confirming that the shared substrate dissolution was executed per the authored dissolution conditions; a persistence policy execution record confirming which content was preserved (per the shared substrate's persistence policy), which was returned to home substrates, and which was discarded; and a hand-off boundary activation record confirming that each participating Self's home substrate received its evolution-feed content through the governance-configured hand-off pathway. All three records carry governance authorization.

**FAIL indicates:**
Any of the three required dissolution records is absent. If the dissolution record is missing, the event has no documented end. If the persistence policy execution record is missing, content disposition is undocumented and potentially ungoverned. If the hand-off boundary activation record is missing, the evolution-feed pathway to home substrates is unverifiable — **AP-2 (Ungoverned Dissolution)**. Ungoverned dissolution is the closing-bracket anti-pattern: even a well-governed FAI event produces an ungoverned outcome if its dissolution is not executed and documented under governance authority.

---

### Test 38 — Black Box Substrate Detection

**Anti-pattern targeted:** AP-22 (Black Box Shared Substrate)

**Records to examine:**
The conflict registry, filtered to RESOLVED entries; the authored orchestration rules for the shared substrate; resolution record fields for each RESOLVED conflict entry.

**Binary question:**
For each RESOLVED conflict in the registry, can the specific authored orchestration rule that governed the resolution be identified by name or reference in the resolution record?

**PASS indicates:**
Every RESOLVED conflict entry in the registry contains a rule citation field that names or references a specific authored orchestration rule — one that exists in the shared substrate's authored orchestration rules set. The resolution is traceable: an auditor can read the resolution record, identify the rule cited, locate that rule in the authored rules set, and confirm that the rule's logic is consistent with the resolution outcome. No resolution is attributed to unspecified system behavior, default behavior, or unattributed judgment.

**FAIL indicates:**
Any RESOLVED conflict entry lacks a rule citation, cites a rule that does not appear in the authored orchestration rules set, or contains only a generic attribution such as "system default" or "automated resolution." Governance decisions within the shared substrate are not fully traceable to authored governance content — **AP-22 (Black Box Shared Substrate)**. The substrate is opaque to audit: it produces governance outcomes that cannot be explained by reference to explicit human-authored rules. This undermines the inspectability commitment that Paper 3 §6's conflict-handling architecture and Paper 1's human-governed commitment jointly require.

---

### Test 39 — Governance Theater Detection

**Anti-pattern targeted:** AP-21 (Governance Theater)

**Records to examine:**
All FAI governance records (construction authorization, configuration record, conflict registry entries, dissolution record, evolution-feed authorization records); a documentation standard assessment against D2.36's four-part standard.

**Binary question:**
Do all FAI governance records satisfy all four D2.36 documentation standards: non-specialist format, complete provenance, mutual accessibility, and retention period specified?

**PASS indicates:**
Each governance record in the FAI record set satisfies all four standards. Non-specialist format: the record is legible to a governance authority who is not a technical specialist, without requiring access to system internals to interpret. Complete provenance: the record identifies who authorized it, when, and under what authority. Mutual accessibility: the record is accessible to all participating governance authorities, not only to the authority that created it. Retention period specified: the record carries an explicit retention period that covers at minimum the dissolution window and the evolution-feed ingestion period.

**FAIL indicates:**
Any governance record fails any of the four standards. Records that exist in form but fail in substance — records that are legible only to technical specialists, records with incomplete provenance, records accessible to only one party, records with no retention specification — satisfy the appearance of governance without its function. The governance record set is theater: it produces artifacts that resemble governance records without enabling the governance authority that those records are supposed to support — **AP-21 (Governance Theater)**. This anti-pattern is specifically dangerous because it passes superficial record-existence checks while failing meaningful governance quality tests.

---

### Test 40 — Time-Pressure Governance Bypass Detection

**Anti-pattern targeted:** AP-19 (Time-Pressure Governance Bypass)

**Records to examine:**
The construction record; all configuration authorization records; event timing records showing the event operation start time; any records containing urgency justifications, timeline exceptions, or expedited-process acknowledgments.

**Binary question:**
Do all pre-construction governance requirements have authorizations dated before the event start, with no urgency justifications substituting for governance process?

**PASS indicates:**
All pre-construction governance requirements are satisfied by records whose timestamps predate the event operation start. No record in the governance record set contains an urgency justification, a timeline exception, a waiver of governance process, or language acknowledging that a required governance step was deferred due to time pressure. Governance was completed before operation began; urgency did not compress or bypass the governance timeline.

**FAIL indicates:**
Any pre-construction governance requirement has an authorization timestamp postdating the event start; or any record contains urgency justifications, waivers, expedited-process language, or acknowledgments of deferred governance. Time pressure was permitted to override the pre-authorization requirement — **AP-19 (Time-Pressure Governance Bypass)**. This anti-pattern is particularly important to detect because urgency is a real operational pressure, and the records that document it are often candid about the bypass. When urgency language appears in governance records, it should be treated as a direct indicator of AP-19 rather than as a mitigating explanation.

---

## 3. Relationship to the Phase D3 Anti-Pattern Taxonomy

The ten tests in this note are not the full Phase D3 taxonomy. They target the ten anti-patterns D3.29 identifies as the highest detection priorities — those whose presence most immediately undermines governance integrity and whose detection is most reliably achievable from records alone.

Tests 31–35 cover D3.29's top five priorities in order: AP-6, AP-24, AP-3, AP-8, and AP-4. These five represent the anti-patterns most likely to be present in deployments that appear structurally compliant. AP-6 (Implicit Configuration) and AP-1 (Ungoverned Construction) are the most common initiating anti-patterns — they create conditions under which downstream anti-patterns are likely to follow. AP-24 (Automated Governance) is the single highest-risk failure mode at runtime because it replaces human authority with automated authority invisibly. AP-3 (Silent Conflict Collapse) is undetectable without a targeted domain-overlap check; compliance tests will not surface it. AP-8 (Exchange Bounding Violation) represents a breach of the trilogy's architectural spine; its presence corrupts the instinct/reasoning separation that Papers 2 and 3 jointly commit to. AP-4 (Automatic DNA Absorption) is the evolution-feed failure mode most likely to propagate inter-Self coordination outcomes into home substrates without governance.

Tests 36–40 extend coverage to the next critical tier. AP-1 and AP-2 (Ungoverned Construction and Dissolution) are the framing anti-patterns: they concern the event's authorized beginning and end, not its internal operation. AP-22 (Black Box Shared Substrate) concerns the inspectability of governance decisions after they are made. AP-21 (Governance Theater) concerns the quality, not merely the existence, of governance records — it is specifically designed to surface failures that pass compliance tests. AP-19 (Time-Pressure Governance Bypass) concerns the temporal integrity of governance sequencing.

---

## 4. Relationship to the D2.24 Compliance Tests

The D5 anti-pattern detection tests are designed to complement, not replace, the D2.24 compliance tests. The two test classes audit different properties:

D2.24 compliance tests ask: *Is the required element present?* Does a shared substrate exist? Does a configuration record exist? Does a conflict registry exist?

D5 anti-pattern detection tests ask: *Is the named failure mode demonstrably absent?* The question is not whether elements exist but whether their specific structural and authorization properties rule out the failure mode.

A governance audit is comprehensive only when both classes are applied. Compliance tests establish baseline structural presence; anti-pattern tests verify that presence does not mask a governance failure. An FAI event that passes all compliance tests but fails Test 39 (Governance Theater) has records that look compliant while being informationally inadequate. An event that passes all compliance tests but fails Test 31 (Implicit Configuration) has a configuration record that is structurally present but temporally out of sequence with the governance requirements.

The test classes are complementary by design: neither is a substitute for the other.

---

## 5. Audit Application Notes

**Applying tests in priority order.** When conducting a governance audit under time or resource constraints, apply Tests 31–35 first. These five tests surface the highest-priority failure modes, and their failures are often diagnostic for the anti-patterns that follow. AP-6 failure frequently co-occurs with AP-1 failure (Test 36). AP-24 failure is often associated with AP-22 failure (Test 38). Applying the tests in D3.29 priority order allows early stopping when a critical failure is identified.

**Record availability as a prerequisite.** Several tests presuppose that specific records exist as readable substrate content (Tests 34, 35, 37). If the records a test requires are not available for inspection, that unavailability is itself a finding: the architecture requires these records as substrate content under the human-governed commitment. Record unavailability should be noted as a probable AP-22 indicator and escalated alongside the specific test result.

**Binary tests do not produce partial results.** The YES/NO structure is not simplified — it is the point. The tests are designed to produce actionable binary findings. A finding that a test "almost passes" or "passes in spirit" is not a finding this test library produces. If evidence is insufficient to answer YES, the answer is NO.

---

## 6. Note Position in the Series

This note is the third Phase D5 note in Series D. The Phase D5 sub-series covers:

- D5.01 — Compliance tests for shared substrate construction and configuration properties
- D5.02 — Compliance tests for FAI event properties
- **D5.03 (this note) — Anti-pattern detection tests for the ten highest-priority Phase D3 anti-patterns**
- D5.04 and beyond — Additional detection tests and boundary-condition test variants

Together, D5.01 through D5.03 form the core audit toolkit for governance practitioners working with shared substrate deployments and FAI events.

---

*End of note D5.03.*
