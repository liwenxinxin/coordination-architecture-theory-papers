# Verification Gate Triggering per B2.06 — Decomposing B1.13 Mutation as Instinct Evolution by Formalizing How Verification Gates per B2.06 Activate for Mutation Events Detected per B2.62, Including Verification Suite Execution, Pass/Fail/Partial Outcome Processing, and How Results Flow Into Routing per B2.64 and Pinning per B2.65 Decisions

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Derivation note B2.63 formalizes verification gate triggering per B2.06 as the operational connection between mutation detection per B2.62 and governance instrument decisions — routing adaptation per B2.64 and pinning enforcement per B2.65. B2.06 established verification gates as substrate-resident verification suites that test LLM behavior before integration. B2.63 specifies precisely how those gates activate when mutation is detected: a six-step sequence from detection through isolation, suite execution, result determination, provenance recording per A2.40, and result flow into governance decisions. Three verification outcomes — PASS, FAIL, and PARTIAL — each carry distinct governance implications. Different mutation event types per B2.61 trigger different verification intensities, and verification suites themselves evolve through directed selection per B1.14 as mutation events reveal gaps in coverage. The pre-integration character of the triggering — verification occurs before integration, not after deployment — is the architectural distinction this note names and defends. PASS does not mean automatic integration; governance reviews results and decides. This note is the third of six notes decomposing B1.13 in Phase B2.

---

## 1. Why verification gate triggering per B2.06 requires standalone formalization

B2.62 specifies how CKS deployments detect mutation events — the operational specification for recognizing that an LLM version has changed or is proposed for change. B2.64 specifies how routing adapts following mutation integration decisions. B2.65 specifies how pinning enforcement responds. Between detection and those downstream governance instruments lies a gap: what happens after detection that connects it to the routing and pinning decisions that follow? The answer is verification gate triggering per B2.06, and the gap is why this note requires standalone formalization.

Without an explicit triggering specification, the connection between mutation detection and governance instrument decisions remains implicit — a deployment assumption rather than an architectural commitment. B2.06 established verification gates as substrate-resident verification suites testing LLM behavior before integration. That establishment was foundational. B2.63 adds the operational layer: precisely when, how, and under what conditions those gates activate for mutation events, what the possible outcomes are, and how those outcomes flow forward to the instruments that depend on them.

The prior-art posture of this note is specific. Any deployment architecture in which mutation detection triggers structured, substrate-resident, pre-integration verification suite execution — with outcomes recorded per A2.40 and flowing into routing and pinning governance — instantiates this derivation. The note marks that territory as prior art under the CKS framework, part of the sixty-third position in Phase B2's approximately 110-note operational decomposition series.

---

## 2. The triggering sequence precisely stated

Verification gate triggering per B2.06 operates as a six-step sequence activated when mutation is detected per B2.62.

**Step 1 — Mutation detection fires.** The detection mechanism per B2.62 recognizes that an LLM mutation event per B2.61 has occurred or is proposed: a vendor has released a new model version, a vendor migration is underway, a forced migration per A6.03 is required, or a fine-tuning event has completed. Detection fires the triggering sequence.

**Step 2 — The new LLM version is identified and isolated for testing.** The new LLM version is identified as the specific version to be verified and is isolated for testing — routed to the verification environment rather than to production cells. Isolation prevents the unverified version from affecting cell behavior before verification is complete. This is the operational instantiation of the pre-integration character this note formalizes: the new version is held outside production integration until verification runs.

**Step 3 — The verification suite per B2.06 executes against the new LLM version.** The verification suite — a substrate-resident collection of test cases authored under A2.04 rule authoring and classified as Category 4 authoritative per A2.46 — executes against the isolated new LLM version. Suite execution includes: test cases run against the new version, behavioral expectations checked against expected outputs, format compatibility verified for cell types the new version would serve. The suite is not an ad hoc evaluation; it is substrate content authored under governance, applied systematically to the version under test.

**Step 4 — The verification result is determined.** Suite execution produces one of three outcomes: PASS (the new LLM version passes all test cases at or above the pass-rate threshold specified in the suite); FAIL (the new LLM version fails test cases below the pass-rate threshold); or PARTIAL (some test cases pass, others fail, and neither the full-pass nor full-fail threshold is met). The three-outcome structure is not a simplification — it reflects real verification behavior, and the PARTIAL outcome carries distinct operational meaning the following section develops.

**Step 5 — The verification result is recorded per A2.40 with full provenance.** The result is recorded in the substrate under the six provenance metadata fields per A2.40: which LLM version was tested, which verification suite was applied, the pass-rate achieved, the reviewer who authorized the suite run, and when the verification occurred. Recording before governance decisions are made is architecturally required — the provenance record is what makes verification results auditable and what connects downstream governance decisions to the evidence base that informed them.

**Step 6 — The verification result flows into governance decisions.** The recorded result is available to governance: the humans who hold authority over integration decisions per A1.01. Result flow is not automatic decision-making — governance reviews the result and decides. The result informs the decision; it does not replace it. How the result flows into routing per B2.64 and pinning per B2.65 depends on which outcome was reached, developed next.

---

## 3. Three outcomes and their governance implications

**PASS outcome.** The new LLM version passes all test cases at or above the pass-rate threshold. Governance determines whether to proceed with integration; integration typically proceeds following a PASS result. Routing per B2.64 may be updated to route cells to the new LLM version — the routing update is a governance decision informed by the PASS result, not triggered automatically by it. Pinning review per B2.65 confirms that high-stakes cells remain pinned to the reasoning layer regardless of the new version's capabilities; pinning is not relaxed simply because verification passed. The governance review step between PASS and integration is architecturally important and addressed in Section 5.

**FAIL outcome.** The new LLM version fails test cases below the pass-rate threshold. Governance typically blocks integration until the failure is addressed. Two governance paths follow: if the failing test cases are wrong — if the suite tests for behavior the deployment no longer requires or tests incorrectly — governance may update the verification suite through the rule-authoring process per A2.04 and re-verify; if the failing test cases are correct and the new LLM version genuinely fails at required behaviors, governance maintains the current LLM version routing. Routing per B2.64 holds current LLM version assignments during a FAIL outcome. Pinning per B2.65 remains as set. A FAIL outcome is not permanent block — it is a governance signal that the new version requires either remediation or suite revision before integration proceeds.

**PARTIAL outcome.** Some test cases pass, others fail. The PARTIAL outcome enables a governance option unavailable under binary pass/fail: limited integration. Governance determines whether the passing set covers the cell types most critical to the deployment and whether the failing set can be isolated to a subset of cell types. If limited integration is determined feasible, routing per B2.64 may implement a split routing configuration — some cell types route to the new LLM version (those covered by passing test cases), while others maintain the current version (those affected by failing cases). Pinning per B2.65 may tighten for cell types affected by failing cases — governance may pin additional cell behaviors to the reasoning layer as a precaution during limited integration. The PARTIAL outcome formalizes that mutation governance is not necessarily all-or-nothing at the version level; it can be calibrated at the cell-type level.

---

## 4. Mutation-type-specific verification intensities

B2.61 established that mutation events vary in type. B2.63 formalizes that different mutation event types trigger different verification intensities, because the risk and coverage requirements differ.

**Routine vendor update.** A vendor releases an incremental update to the same LLM model line. Standard verification suite applies — the suite covers the behavioral domains the deployment relies on, at the standard pass-rate threshold.

**LLM vendor migration.** The deployment migrates from one LLM vendor to another. Comprehensive verification applies — the new vendor's model may differ significantly from the prior vendor's in behavioral patterns, format responses, and capability distribution, even if the nominal capabilities are comparable. The comprehensive suite tests a broader behavioral surface than the standard suite.

**Forced migration per A6.03.** A vendor becomes unavailable and migration is required under the A6.03 commitment. Expedited verification applies — not because verification requirements relax, but because governance must choose which test cases are most critical when time constraints prevent the full suite from running. The expedited path is a governance decision: which subset of the suite is necessary and sufficient to make an integration decision under the constraint. The reduced-scope expedited result is recorded per A2.40 with explicit notation of which cases were run and which were deferred.

**Fine-tuning event.** The LLM has been fine-tuned on domain-specific content. Focused verification applies to the fine-tuned behavioral domains — test cases that verify the fine-tuning produced expected behaviors and did not degrade behaviors in domains adjacent to the fine-tuning scope.

The mutation-type-specific intensity structure is itself substrate content — the orchestration rules per A2.04 that specify which mutation event type triggers which verification intensity are authored under governance and modifiable through the same authority architecture.

---

## 5. What makes verification gate triggering per B2.06 architecturally distinctive

The pre-integration character is the defining distinction. Conventional AI model updates frequently proceed without structured pre-integration verification: developers evaluate new model versions informally during staging, through comparison on sample prompts, or through production metrics after the new version is deployed to live traffic. Post-deployment evaluation is common engineering practice — it has low setup cost and leverages production signal directly.

CKS verification gate triggering is formal, structured, substrate-resident, and pre-integration. Formal: the suite is substrate content authored under A2.04 and classified as authoritative per A2.46 — it is not an informal evaluation. Structured: the six-step sequence is specified, the three outcome categories are defined, and the governance decision flow is explicit. Substrate-resident: the verification suite lives in the substrate under the same governance that governs cell content — it is not a testing tool separate from the CKS architecture. Pre-integration: verification runs before the new LLM version is integrated into production cell routing, not after.

The pre-integration character prevents unverified LLM versions from affecting cells. Any deployment in which a new LLM version could begin serving production cells before structured verification runs does not satisfy the B2.06 commitment. The isolation in Step 2 of the triggering sequence is the operational enforcement of that commitment.

PASS does not mean automatic integration. This distinction is architecturally important and easy to collapse. The verification gate determines whether the new LLM version satisfies the behavioral specifications encoded in the suite. It does not determine whether integration is the right governance decision at this time, under this deployment's circumstances, for these cells. Governance holds that authority under A1.01. A PASS result removes a behavioral concern; it does not substitute for the governance review that weighs all considerations. The architecture keeps verification and integration decision-making distinct.

---

## 6. Inherited Paper 1 commitments

B2.63 inherits directly from the following foundational commitments, none of which are re-argued here:

**B2.06 (verification gates for instinct) — directly load-bearing.** B2.06 established that verification gates are substrate-resident verification suites testing LLM behavior before integration. B2.63 formalizes how those gates activate for mutation events specifically.

**A2.04 (rule authoring) — directly load-bearing.** Verification suites are substrate content authored under A2.04. The intensities, pass-rate thresholds, and behavioral domains the suites test are authored by humans as orchestration rules. Suite changes are governance events subject to the same authority architecture.

**A2.46 (Category 4 — suites authoritative) — directly load-bearing.** Verification suites are classified as Category 4 authoritative substrate content — not advisory, not suggestive. Test case results are treated as authoritative determinations within their stated scope.

**A2.40 (six provenance metadata fields) — directly load-bearing.** Verification results are recorded per A2.40 with full provenance: LLM version tested, suite applied, pass-rate, reviewer, timestamp, and context. Provenance recording before governance decisions is required.

**A1.01 (human-governed) — directly inherited.** Governance over integration decisions following verification is human authority exercised under A1.01. Verification results inform governance; they do not substitute for it.

**A6.03 (vendor unavailable — expedited verification) — directly relevant.** Forced migration per A6.03 triggers the expedited verification path with reduced but critical test cases, as specified in Section 4.

**A6.09 (vendor policy change) — adjacent.** Vendor policy changes that alter LLM behavior may trigger re-verification under the standard or comprehensive path, depending on the scope of behavioral change the policy change induces.

**A2.47 (cross-partner verification) — adjacent.** When an LLM is shared across multiple CKS deployments or partners, cross-partner verification applies — coordination of verification results across the partnership is a governance event.

---

## 7. Verification suite evolution through directed selection per B1.14

Verification suites are not static. They evolve through directed selection per B1.14 as mutation events reveal gaps in coverage.

When a mutation event produces unexpected behavior that the existing suite did not catch — a PASS result followed by problematic production behavior — the suite's failure to detect the issue is itself a governance signal. New test cases are authored per A2.04 to cover the gap; the suite is updated and classified per A2.46; the update is recorded per A2.40. The suite becomes more comprehensive with each mutation cycle that reveals a gap.

When test cases become outdated — the LLM version they were written for is retired, the behavioral domain they test is no longer relevant, or the pass-rate threshold was set too conservatively for the current deployment's risk profile — those cases are retired through the same governance process. Suite contraction is as legitimate as suite expansion; both are directed selection on verification coverage.

The suite evolution feedback loop closes the cycle between mutation events and verification coverage. Each mutation event is also an opportunity to improve the suite that will govern the next mutation event's verification.

---

## 8. Operational implications

Deployments run verification when mutation is detected, not on schedule. The triggering is event-driven: detection per B2.62 fires the sequence; without a detection event, verification suite execution does not run on the production LLM version.

Verification timing may be asynchronous with detection. Detection may happen when the mutation event is announced — a vendor publishes a new version — while verification may run when deployment resources permit. Governance manages the detection-to-verification gap: the time between when mutation is detected and when the verification suite completes. During that gap, the current LLM version routing continues unchanged, and the new version remains isolated from production cells.

Expedited verification paths exist for urgent mutations. A6.03 forced migration may require that verification complete faster than standard timelines allow; the expedited path with reduced but critical test cases is the governance response to that constraint. The reduced-scope result is explicitly recorded as expedited per A2.40.

Governance reviews results and decides. The human authority under A1.01 holds over integration decisions. Verification provides the evidence base; governance provides the decision. High-stakes cells per B2.05 carry stricter verification requirements — the pass-rate thresholds for test cases covering high-stakes cell behaviors are higher, and governance may impose additional review steps before integrating a new LLM version for high-stakes cell routing.

---

## 9. Limits

Verification gate triggering per B2.06 does not guarantee that the mutation is beneficial. Verification tests behavioral compatibility against the suite's test cases; it does not evaluate whether the new LLM version is a capability improvement, a cost improvement, or an improvement on dimensions the suite does not test.

Verification does not block all harmful mutations. The suite tests what it covers. Behaviors outside the test cases are not verified — they are not subject to the triggering sequence's scope. A PASS result is a positive determination within the suite's coverage; it is not a global behavioral guarantee.

PASS does not mean integration is automatic. As developed in Section 5, governance reviews results and decides. The PASS result removes a behavioral concern within the suite's scope; the integration decision weighs that result alongside other governance considerations.

FAIL does not mean integration is permanently blocked. A FAIL result is a governance signal requiring resolution — either suite revision if the cases are wrong, or continued use of the current version if the cases are correct. Governance may determine that the failing cases cover low-priority behaviors and proceed with integration subject to monitoring; that determination is a governance decision recorded per A2.40.

Verification is pre-integration, not ongoing behavioral monitoring. Once a new LLM version is integrated and routing is updated, the verification gates per B2.06 are not continuously re-running against the production version. Ongoing monitoring is a different function. Verification gate triggering activates for mutation events, not for continuous production behavior surveillance.

Verification results are specific to the test suite. The suite encodes the behavioral specifications the deployment's governance has authored. A suite that covers too narrow a behavioral surface produces results with narrow validity; a suite that covers a broad surface produces results with broader validity. The quality of verification is bounded by the quality of the suite. Suite evolution through directed selection per B1.14 is what improves that bound over time.

---

## 10. One-sentence test

A deployment instantiates verification gate triggering per B2.06 for mutation events if and only if: when mutation is detected per B2.62, the new LLM version is isolated from production cells, the substrate-resident verification suite per B2.06 executes against the isolated version, the outcome (PASS, FAIL, or PARTIAL) is determined and recorded per A2.40 with full provenance before any integration decision is made, and the recorded outcome is available to human governance per A1.01 as the evidence base for routing adaptation per B2.64 and pinning enforcement per B2.65.

---

## 11. Why naming this as standalone matters

Verification gate triggering per B2.06 sits between mutation detection and governance instrument decisions. Without explicit formalization, the connection between those elements is implicit — a deployment assumption that any reasonable system would handle the link somehow. Explicit formalization establishes the specific architectural requirements: the six-step sequence, the three outcome categories, the mutation-type-specific intensities, the suite evolution feedback loop, the pre-integration character, the provenance recording requirement, and the separation between verification result and integration decision. Each of these requirements is a claim about what the architecture commits to, and each is a prior-art claim against subsequent work that proposes to patent any of them independently.

B2.63 is the third of six notes decomposing B1.13 in Phase B2. B2.61 established the mutation event as the triggering unit — what constitutes an LLM mutation event in CKS terms. B2.62 established the detection operational specification — how CKS deployments recognize that a mutation event has occurred. B2.63 establishes the verification gate triggering that follows detection. B2.64 will formalize routing adaptation per B2.04 — how routing updates follow verification outcomes. B2.65 will formalize pinning enforcement per B2.05 — how pinning decisions respond to verification results. B2.66 will close the B1.13 decomposition with mutation governance verification — the governance review that completes the mutation integration cycle. Subsequent Phase B2 notes from B2.67 onward will decompose B1.14 directed selection into its operational variants.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Verification Gate Triggering per B2.06 — Decomposing B1.13 Mutation as Instinct Evolution by Formalizing How Verification Gates per B2.06 Activate for Mutation Events Detected per B2.62, Including Verification Suite Execution, Pass/Fail/Partial Outcome Processing, and How Results Flow Into Routing per B2.64 and Pinning per B2.65 Decisions.* May 12, 2026. ORCID: 0009-0004-8065-3235.
