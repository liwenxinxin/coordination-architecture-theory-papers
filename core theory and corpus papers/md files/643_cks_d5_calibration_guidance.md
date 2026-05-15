# Operational Test Calibration Guidance

**Derivation Note D5.08**
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

The 55-test governance library established in D5.01–D5.07 uses binary YES/NO tests. In practice, governance records produce ambiguous results: partially complete records, retrospectively produced records, and records where specialists prepared documentation while governance authority remained with non-specialist practitioners. This note provides calibration guidance for governance practitioners handling these borderline cases, establishes the procedure for setting a governance baseline before a first FAI event, specifies how per-event test scores support governance quality monitoring over time, describes cross-organization trust calibration through shared test scores, and provides a priority order for organizations operating under limited governance capacity. The note's central discipline is that the binary framework is maintained throughout: borderline results are FAIL with a deficiency note, not partial PASS. The guidance makes the test library operational in practice while preserving the prior-art precision the binary structure provides.

---

## 1. Purpose of calibration guidance

The 55-test library (D5.01–D5.07) is a binary instrument. Each test returns YES or NO: either the governance requirement is met, or it is not. This binary structure is deliberate. It preserves the library's precision as a prior-art record, eliminates ambiguity in governance assessments, and makes test scores comparable across events and organizations.

Practice, however, surfaces grey areas. Governance records exist but are incomplete. Records appear after the governance period they are meant to cover. Specialists prepare documentation under the direction of non-specialist governance practitioners. These cases do not fit cleanly into YES or NO without guidance. Calibration guidance fills that gap.

The discipline this note establishes: calibration guidance does not introduce a middle category. It provides rules for mapping each borderline case back to the binary framework, together with structured notation for recording what the borderline case reveals about governance quality. A governance practitioner who applies this note will always reach a binary result, always record the deficiency or mitigating factor, and always preserve the test score's comparability across events and organizations.

---

## 2. Handling borderline test results

### 2.1 Partial records

A partial record exists when a governance record is present but incomplete — for example, a construction record that documents the substrate boundary decision but omits the required authorization reference, or an exchange-bounding record that names the bounding constraint but does not record the governance practitioner who approved it.

**Calibration rule:** Treat as FAIL. Record the specific deficiency: which required element is absent.

The partial record is not equivalent to a pass. The governance requirement specifies what the record must contain; a record that satisfies some but not all of those elements does not satisfy the requirement. Partial credit does not exist in the binary framework. The deficiency note serves a constructive purpose: it specifies exactly what remediation is needed to convert the FAIL to a PASS on a subsequent assessment.

Governance practitioners should not be deterred by the FAIL designation on a partial record. A partial record with a clear deficiency note represents a better governance state than no record at all — the deficiency is identified, bounded, and actionable. The FAIL designation is not a penalty; it is a precise description of where the governance requirement is unmet.

### 2.2 Retrospective records

A retrospective record is a governance record produced after the fact to cover a period where records were absent. The governance decision existed — the action was taken, the boundary was set, the exchange was bounded — but the record was not produced at the time the decision was made.

**Calibration rule:** Treat as FAIL. Note that retrospective records were produced.

Retrospective records may accurately describe the governance decision that was made. They do not retroactively satisfy the governance requirement at the time the record should have existed. The test asks whether the governance record was present when the governance requirement applied, not whether an explanation can be constructed afterward.

This rule is not punitive. Retrospective documentation is better than nothing: it may reduce ambiguity about what decision was made, support future governance work, and demonstrate that the organization is aware of the gap. But it does not convert a FAIL to a PASS. The notation that retrospective records were produced is itself informative — it tells future assessors that the gap was recognized and addressed, which is relevant to trend analysis (§4 below) and to the calibrated-humility register for governance trust (§4.3).

### 2.3 Specialist assistance records

A specialist assistance record arises when specialists — technical staff, consultants, or AI systems operating under human direction — prepare the documentation, but the governance authority decisions recorded in that documentation were made by non-specialist governance practitioners.

**Calibration rule:** Treat as PASS if the authority decisions are documented as being made by governance practitioners.

The distinction at stake is authority versus labor. Specialist assistance with record preparation is a labor allocation decision; it does not affect who holds governance authority over the decisions recorded. What the test evaluates is whether governance authority was exercised by governance practitioners, not who performed the writing work. A record drafted by a specialist but documenting a governance practitioner's authority decision satisfies the governance requirement when the authority decision is legible in the record.

If the record prepared with specialist assistance does not document who made the authority decision — if the specialist's labor displaces the governance practitioner's documented authority — the test fails under Category 2.1 (partial record, missing authority documentation). The specialist assistance calibration rule applies only where authority decisions are present and traceable to governance practitioners in the record itself.

---

## 3. Establishing governance baselines

### 3.1 Pre-participation assessment

Organizations new to the FAI governance framework should run Tests 1–20 before their first FAI event. This set — the baseline test battery — evaluates the governance foundations that must be in place before inter-Self coordination can proceed under appropriate governance. Tests 1–20 cover the structural governance properties established in Papers 1 and 2: substrate boundary governance, conflict-as-first-class state, AI-as-substrate-mediator governance, tool-agnostic substrate commitment, non-specialist governance accessibility, and path retraceability.

A PASS on all twenty baseline tests indicates governance readiness for a first FAI event. This result is the quantitative expression of what the onboarding checklist (D2.69) validates procedurally: the two instruments address the same readiness question from complementary angles. The onboarding checklist covers process and role preparation; the baseline test battery covers the documentary governance record. Together they constitute the pre-participation governance assessment — each reinforcing what the other establishes from its respective register.

An organization that completes the onboarding checklist but cannot pass all twenty baseline tests has identified specific governance gaps before its first event — an informative result that directs pre-event remediation rather than allowing governance deficiencies to enter the first event uncorrected.

### 3.2 Baseline documentation

The results of the pre-participation assessment — which tests passed, which failed, and the deficiency notes for each FAIL — should be recorded as governance content in the organization's home substrate. This baseline record serves three functions.

First, it establishes the starting point for governance quality improvement tracking. Future per-event assessments can be compared against the baseline to determine whether governance quality has improved, remained stable, or declined since the organization entered the FAI framework.

Second, it documents the governance state at entry. This record is relevant to governance trust calibration (§4.3 below) when the organization first appears in a shared governance network: other participants can observe that a baseline assessment was conducted and what the organization's starting governance quality was.

Third, it creates accountability for remediation. FAIL results at baseline, together with their deficiency notes, generate a specific list of governance improvements the organization committed to address before or alongside its first FAI event. Future assessments can confirm whether those improvements were made.

---

## 4. Tracking governance quality over time

### 4.1 Per-event test scores

After each FAI event, governance practitioners run the relevant tests and record the results. The governance quality score for an event is the ratio of tests passed to tests run. This score is a point-in-time measure of governance quality — the quantitative expression of governance health monitoring.

Per-event scores are meaningful individually and as a series. A single event's score identifies which governance requirements were met and which were not, producing a bounded remediation agenda. A series of scores across multiple events reveals the direction of governance quality over time.

### 4.2 Trend analysis and governance health triggers

Three consecutive events with declining test scores indicate a governance decay trend. This pattern triggers an unscheduled governance review — the same response mechanism that health indicator warnings activate. The trigger is structural: three consecutive declining scores are evidence that governance quality is deteriorating, not noise around a stable baseline. Waiting for a fourth declining event before responding allows the decay to entrench further and makes remediation more costly.

The trend trigger is directional, not threshold-based. An organization with high governance quality that declines over three consecutive events warrants review even if its absolute score remains high; the trajectory, not the level, is what the trigger responds to. Conversely, an organization with low governance quality that improves over three consecutive events is not triggered; improvement is the desired direction regardless of starting level.

Governance practitioners should record their trend analysis alongside per-event test scores. The trend record — not just the score — is the governance quality monitoring artifact. Future assessors and partner organizations benefit from observing both the scores and the trend interpretation the organization produced at the time, rather than reconstructing trend analysis retrospectively.

### 4.3 Cross-organization comparison in the calibrated-humility register

Organizations in a shared FAI network may share their governance test scores as part of governance trust calibration. Higher test scores legitimately support higher trust in an organization's governance quality; lower scores legitimately inform lower trust. This use of test scores as trust evidence is a population-scope governance property: the test library produces evidence that travels across organizational boundaries, enabling governance trust to be grounded in observable record rather than assertion alone.

The qualifier "calibrated humility" is intentional. Test scores are governance quality evidence, not governance quality proof. An organization with high scores may still carry governance gaps the current test library does not cover; an organization with lower scores may have governance strengths the scores do not capture. Scores inform trust calibration; they do not replace it. The register for sharing test scores across organizations is evidence-offering, not certification.

---

## 5. Priority order for limited governance capacity

Not all organizations can run all 55 tests after every event. Where governance capacity limits how many tests can be run in a given cycle, the following priority order applies.

**First priority — Tests 36–37 (lifecycle governance: AP-1 and AP-2).** Cell birth and cell death governance are the load-bearing lifecycle commitments. Governance failure at the lifecycle level affects the structural integrity of the substrate itself. These two tests take priority over all others because no downstream governance property is reliable if lifecycle governance is unverified.

**Second priority — Test 31 (implicit configuration: AP-6).** Implicit configuration — undocumented substrate behavior arising from unexamined defaults — is among the highest-risk governance failure modes. This test takes priority over most others because implicit configuration failures compound: they are difficult to detect retrospectively, tend to persist across events, and may propagate through FAI interactions into partner substrates.

**Third priority — Test 34 (exchange bounding: AP-8).** Exchange bounding governs what crosses the inter-Self perimeter during an FAI event. Where exchange bounding fails, content crosses perimeters without appropriate governance, creating accountability gaps that are difficult to reconstruct after the fact and that affect partner organizations, not only the organization whose governance record is deficient.

**Fourth priority — Tests 41–43 (governance quality).** These tests directly assess the quality of the governance process itself — whether governance records are produced, whether they are complete, and whether the review cycle is functioning. After the highest-risk structural tests, governance quality tests provide the broadest available signal about the overall governance state.

**Fifth priority — Remaining baseline tests (Tests 1–20).** The baseline battery covers the structural governance foundations established before the first FAI event. Organizations running limited tests should work through the baseline battery in full before the lifecycle, configuration, and exchange tests crowd them out, because the baseline tests are prerequisites for reliable interpretation of all subsequent test results.

**Sixth priority — Tests 21–30 (composition pairs).** Composition pair tests are valuable for organizations operating multiple cells or aspects but are lower priority than structural and high-risk tests when capacity is constrained.

The priority order is a triage rule for cycles where running all 55 applicable tests is not possible — not a recommendation to run fewer tests. Organizations with full governance capacity should run all applicable tests per event.

---

*This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).*
