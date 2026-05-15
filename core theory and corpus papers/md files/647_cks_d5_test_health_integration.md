# Test Library Integration with Governance Health Monitoring

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

Governance quality assurance for Full Aspect Integration (FAI) relationships requires two distinct monitoring modes: continuous health monitoring via the six governance health indicators (H1–H6, established in D2.35) and episodic deep assessment via the 60-test library (established in D5.02–D5.10). Neither mode alone is sufficient. Health indicators provide real-time anomaly detection but can miss governance gaps that fall between their six measurement dimensions. Tests provide thorough verification against specific governance requirements but do not detect trends or signal accumulating governance drift between assessment cycles. D5.12 formalizes how these two systems integrate into a unified governance quality assurance framework through three interaction protocols — health indicators trigger targeted test runs, test failures update indicator thresholds, and the combination produces a three-color governance quality score — and through a governance quality assurance cycle that makes the integration self-correcting over time.

## 1. The two-system problem

The 60-test library and the six governance health indicators address governance quality from opposite directions.

The test library is periodic and deep. At scheduled intervals, a governance practitioner runs applicable test subsets against an FAI relationship and receives structured PASS/FAIL verdicts on each of sixty specific governance requirements. The depth of the test library is its strength — it covers every dimension of governance quality from conflict registry integrity through post-mortem completeness to standing configuration currency. Its limitation is its periodicity: between test cycles, governance quality may be degrading in ways that the next scheduled assessment would catch, but that no current signal reveals.

The six health indicators operate on the opposite profile. They run continuously against observable governance metrics, flagging anomalous readings in real time. Their strength is trend detection — a declining escalation response rate (H2) or accumulating post-mortem backlog (H5) surfaces immediately as a warning signal rather than waiting for the next test cycle. Their limitation is coverage: the six indicators measure six specific metrics, and governance gaps that do not register against those metrics can persist without triggering any warning.

Health indicators without tests may miss governance gaps. Tests without health indicators miss trend detection. The integrated system closes both coverage gaps simultaneously because each mode compensates for the blind spot the other mode carries.

## 2. Mapping tests to health indicators

Each of the six health indicators maps to a specific subset of tests in the 60-test library. When an indicator shows a warning signal, the mapped test subset functions as an investigation set — the practitioner runs those tests to determine whether the warning reflects an actual governance issue or a false positive.

**H1 — Conflict Registry Completeness** maps to Test 33 (silent collapse detection for AP-3 patterns), Test 3 (conflict registry structural integrity), and Test 38 (black box resolution detection). H1 measures whether the FAI relationship's conflict registry is maintaining complete records of surfaced conflicts. A warning on H1 signals potential silent collapse — conflicts resolved without proper registry entries — or undocumented resolution reasoning. Tests 33, 3, and 38 verify each of these failure modes directly.

**H2 — Escalation Response Rate** maps to the D2.24 escalation routing and response tests, plus Test 41 (determinism check for governance decisions). H2 measures how reliably escalated governance decisions receive responses within the required timeframe. A warning on H2 signals either routing failures (escalations not reaching decision-makers) or response failures (escalations pending resolution beyond threshold). Test 41 is included because escalation response is itself a governance decision that must meet the determinism standard.

**H3 — Evolution Feed Activation** maps to Test 35 (AP-4 automatic absorption detection), Test 49 (carry-through completeness), Test 50 (vertical propagation verification), and the D2.24 tests covering evolution feed mechanics. H3 measures whether the evolution feed mechanism is activating at appropriate rates following FAI events. A warning on H3 signals potential AP-4 patterns — FAI-derived content absorbed automatically without proper governance machinery — or carry-through failures where content does not propagate from shared substrate to home substrates under the configured ingestion rules.

**H4 — Governance Record Completeness** maps to Test 42 (documentation standards compliance), Test 39 (governance theater detection), Test 43 (authorization chain verification), and D2.24 Test 20 (complete governance record). H4 measures the completeness of governance records across the FAI relationship. A warning on H4 may signal documentation gaps or governance theater — records that satisfy the form of governance documentation without its substance. The full governance quality test subset (Tests 41–45) provides the most comprehensive investigation for H4 warnings.

**H5 — Post-Mortem Completion Rate** maps to Test 47 (post-mortem quality standard). H5 measures whether post-mortems required by governance policy are being completed within the required timeframe. A warning on H5 has a narrow investigation path: Test 47 verifies both that post-mortem records exist and that they meet the quality standard rather than being pro forma entries that satisfy completion rates without substantive analysis.

**H6 — Standing Configuration Currency** maps to Test 25 (parent-child hierarchy verification), Test 53 (configuration currency check), and the D2.24 test covering standing configuration review schedules. H6 measures whether the FAI relationship's standing configuration is being kept current as the participating Selves' governance configurations evolve. A warning on H6 prompts the relationship governance test subset (D5.09 Subset 5) as the investigation set.

## 3. Three integration protocols

Three protocols govern how the test library and health indicators interact operationally.

**Protocol 1 — Health indicator warning triggers targeted test run.** When any health indicator H1–H6 crosses its warning threshold, the governance practitioner initiates a targeted test run using the mapped test subset for that indicator. The test run delivers one of two outcomes: FAIL on one or more mapped tests confirms that the health indicator warning reflects an actual governance issue, enabling directed remediation; PASS on all mapped tests establishes that the warning was a false positive, enabling the practitioner to clear it and document the false-positive event. Protocol 1 converts health indicator warnings from unresolved anomaly signals into verified governance findings or cleared anomalies. Without the test library, indicator warnings would require unstructured investigation; with the mapped test subsets, investigation is immediate and structured.

**Protocol 2 — Test failures update health indicator thresholds.** When a test FAIL reveals a governance gap that no health indicator had signaled prior to the test cycle, this is evidence that the indicators missed a real governance issue. The appropriate response is not only to remediate the governance gap but to review the thresholds for the indicators that should have signaled it. If Test 39 (governance theater) produces a FAIL but H4 showed no warning, the H4 threshold for governance record completeness may be calibrated too loosely to detect the theater pattern the test identified. Protocol 2 operationalizes the D4.26 composition pair's feedback requirement: test failures that precede health indicator warnings are calibration data for the continuous monitoring system. The test library makes health indicator calibration actionable. Over time, Protocol 2 produces a continuous monitoring system whose indicators are sensitive enough to signal the governance gaps that the tests consistently detect, shrinking the detection lag cycle by cycle.

**Protocol 3 — Combined outputs produce unified governance quality score.** The outputs of continuous health monitoring and periodic test assessment are combined into a single three-color governance quality score for each FAI relationship:

- **GREEN**: all health indicators in normal range and test pass rate above the established threshold. Governance quality is confirmed as satisfactory across both monitoring modes.
- **YELLOW**: one or more health indicators showing a warning signal, or test pass rate declining toward threshold but not yet below it. YELLOW is the early warning state — governance quality may be degrading, but the evidence is not yet confirmed. Protocol 1 (run the mapped test subset) is the appropriate response to a YELLOW triggered by an indicator warning; more frequent monitoring and closer test scheduling is the appropriate response to a YELLOW triggered by declining pass rate.
- **RED**: one or more health indicators above warning threshold and one or more FAIL results on the mapped tests for those indicators. RED confirms that an active governance issue exists in a dimension where continuous monitoring has signaled and periodic testing has verified. RED triggers remediation, not further investigation — investigation is already complete — directed toward the confirmed governance failure.

The three-color score is the practical output of the integrated system. Governance practitioners need to know not only that tests passed or failed in the last cycle, but what the current governance quality state is for the FAI relationship they govern. GREEN/YELLOW/RED provides that signal in a form that supports immediate governance action.

## 4. The governance quality assurance cycle

The three protocols compose into a self-correcting governance quality assurance cycle. Continuous health monitoring operates at all times, producing real-time signals against H1–H6. When indicator warnings occur, Protocol 1 dispatches targeted test runs against the mapped test subsets. Test results either confirm or clear the warning; both outcomes update the governance quality score. Scheduled test cycles run regardless of indicator state, providing comprehensive periodic assessment even when indicators show no anomalies. When test FAILs occur without preceding indicator warnings, Protocol 2 applies: the indicator thresholds for the relevant dimensions are reviewed and tightened.

Tighter thresholds improve the sensitivity of continuous monitoring, making it more likely that future governance gaps in those dimensions will surface as indicator warnings before the next test cycle. Each iteration of the cycle therefore produces a more accurate and more sensitive governance quality assurance system. The cycle implements the D4.26 composition pair's feedback loop in operational terms: indicators inform when to run tests; test results calibrate indicators; calibrated indicators provide more accurate continuous monitoring; more accurate continuous monitoring generates early warnings more closely correlated with actual governance issues; more targeted early warnings produce more efficient use of the test library. The improvement compounds across cycles rather than resetting with each assessment.

## 5. Conclusion

D5.12 formalizes the integration of two complementary governance monitoring modes — the continuous health indicators H1–H6 and the 60-test library — into a unified governance quality assurance framework. The framework specifies how each indicator maps to its investigation test subset, how the three interaction protocols govern the operational relationship between the two systems, and how their combined outputs produce the three-color governance quality score that supports actionable governance decisions. The governance quality assurance cycle makes the integration self-correcting: each Protocol 2 calibration event improves the sensitivity of continuous monitoring, compounding the value of the test library across every subsequent assessment cycle.

---

## Source papers

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Test Library Integration with Governance Health Monitoring.* May 15, 2026. ORCID: 0009-0004-8065-3235.
