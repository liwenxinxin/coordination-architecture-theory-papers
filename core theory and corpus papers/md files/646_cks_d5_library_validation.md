# Operational Test Library Validation

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

A test library is only as useful as its tests are well-formed and its coverage is adequate. This note provides the validation framework for the 60-test operational library developed across Phase D5 of the CKS theory derivation series. Three well-formedness criteria are stated: each test must be answerable by reading governance records alone without specialist interpretation (binary from records); each test must cover a governance requirement not fully covered by another test (distinct requirement coverage); and both pass and fail must be realistically achievable outcomes (non-trivial pass/fail). A coverage assessment maps the 60 tests against the governance commitment categories they address and identifies three acknowledged gaps where dedicated tests do not yet exist: the five-step aspect contribution governance protocol, the Full Aspect Integration configuration amendment governance, and post-mortem compliance (as distinct from post-mortem quality). The note concludes by identifying Tests 61–63 as the natural gap-closing extensions and establishing that the existing 60 tests provide adequate coverage for an initial governance audit of a CKS-governed inter-Self coordination deployment.

## 1. The validation question

Phase D5 developed 60 operational tests for governance auditing of deployments that implement the inter-Self coordination architecture introduced in Paper 3 (Li, April 2026). Each test takes the form of a yes/no question answerable from governance records — the shared substrate, configuration documents, event logs, and authorization records maintained by the deployment under audit.

The 60 tests are only useful if they are themselves well-formed. A test that requires specialist technical expertise to answer is not a governance test; it is an implementation audit. A test that duplicates the coverage of another test dilutes governance capacity without adding signal. A test whose answer is predetermined — always passing because the bar is trivially low, or always failing because the bar is impossibly high — produces no actionable governance information.

D5.11 provides the framework for assessing whether the 60-test library clears these three hurdles, states the library's coverage profile across governance commitment categories, and honestly acknowledges where gaps remain.

## 2. Criterion 1 — Binary from records

**Statement.** A well-formed test must be answerable YES or NO by reading governance records alone, without requiring implementation access, technical system inspection, or specialist interpretation.

**Rationale.** The non-specialist governance principle established in D2.75 holds that governance authority must be exercisable by humans who understand the governance commitments without requiring the technical expertise needed to evaluate whether the underlying implementation correctly executes those commitments. A test that requires a governance practitioner to inspect running code, query an API, or interpret technical system state is not a governance test — it is a system audit. The two activities are distinct, and conflating them undermines the governance-is-authority-not-labor commitment that runs across the CKS trilogy.

**Validation method.** For each of the 60 tests, confirm that a governance practitioner with access to the governance records — but no system access and no technical implementation knowledge — could answer the test question unambiguously. Tests that pass this check are governance-answerable. Tests that fail it should be reconsidered as system audit tasks rather than governance tests.

**Application to the 60-test library.** The tests developed across D5.01–D5.10 were constructed with this criterion as the primary design constraint. Each question targets governance record state — whether a document exists, whether a field is populated, whether an authorization chain is recorded, whether a conflict is logged — rather than system behavior. A governance practitioner can assess Test 34 (whether exchange bounding is recorded in the shared substrate configuration) by reading the configuration document; they do not need to observe a live FAI event. A governance practitioner can assess Test 43 (whether the authorization chain for a governance decision is traceable) by following the documented record; they do not need to trace execution logs.

## 3. Criterion 2 — Distinct requirement coverage

**Statement.** Each test must cover a governance commitment not fully covered by any other test in the library. Tests that map to the same governance commitment are redundant; redundancy dilutes governance capacity without adding coverage value.

**Rationale.** A governance audit operates under resource constraints. Governance practitioners have finite time; audit cycles have scope limits. A test library that spends two tests on the same commitment is spending twice as much audit capacity to gain the same signal. The library should maximize coverage breadth across governance commitments rather than depth on any single commitment.

**Validation method.** For each test, identify the specific governance commitment it assesses. No two tests should map to the same commitment. Where two tests address closely related commitments, confirm that the commitments are genuinely distinct — that a deployment could pass one while failing the other.

**Application to the 60-test library.** The 60 tests were developed against distinct governance commitment targets drawn from Paper 3's six claims and their Phase D1–D2 sub-commitments. Tests 36, 37, and 56 address lifecycle governance but at distinct commitment levels: Test 36 assesses whether a lifecycle event is recorded; Test 37 assesses whether the governance authorization for that event is documented; Test 56 assesses whether lifecycle records are preserved in the shared substrate after dissolution. These are distinct commitments — a deployment can satisfy record-keeping (Test 36) while failing to document authorization (Test 37). The mapping is one commitment per test across the library.

## 4. Criterion 3 — Non-trivial pass/fail

**Statement.** Both PASS and FAIL must be realistically achievable outcomes in governance practice. A test that always passes (because the requirement is trivially met in any governance deployment) or always fails (because the requirement is impossibly high) provides no governance signal.

**Rationale.** Tests that are predetermined provide no discriminating information. A test library populated with trivially passing tests creates false assurance; one populated with impossibly failing tests creates useless deficits. Useful tests occupy the zone where governance effort determines the outcome.

**Validation method.** For each test, confirm that both outcomes have occurred or could realistically occur in a governance deployment. A test that has never been known to fail in any deployment warrants reconsideration as a governance test — it may be documenting an invariant rather than testing a commitment.

**Application to the 60-test library.** The tests target governance requirements that are structurally achievable but operationally demanding. Test 33 (whether conflict records carry the original conflicting content from both contributing Selves) can fail if a deployment logs only the resolution outcome without preserving the conflict state. Test 45 (whether no governance authority has been silently delegated to an AI substrate without human authorization record) can pass in a well-governed deployment and fail in a deployment where AI substrate autonomy was extended without documentation. Both outcomes are realistic. The non-trivial threshold is met across the library.

## 5. Coverage assessment

The 60 tests, assessed against governance commitment categories, distribute as follows.

**Comprehensively covered.** Lifecycle governance is addressed by Tests 36, 37, and 56, covering record-keeping, authorization documentation, and post-dissolution preservation respectively. Exchange bounding is addressed by Tests 34 and 58, covering the instinct/reasoning boundary at the FAI hand-off and the exchange scope documentation in the shared substrate. Configuration governance is addressed by Tests 31 and 40, covering the substrate-content status of configuration and the human-authority requirement at the configuration layer. Conflict handling is addressed by Tests 33 and 38, covering preservation of conflict state and the tier escalation pathway respectively. Aspect contribution governance (the population of the shared substrate by participating Selves) is addressed by Tests 35, 28, and 48, covering contribution scope, DNA-layer content integrity, and action-layer content integrity respectively. Documentation quality is addressed by Tests 39 and 42, covering governance record legibility and the traceability of rationale chains. Authorization chain governance is addressed by Test 43. Non-delegation of governance authority is addressed by Test 45.

**Partially covered.** Population-scope governance (Tests 51–55) is addressed in the calibrated-humility register appropriate to Paper 3's extension claim. These tests are advisory rather than required compliance tests; full coverage would require empirical validation work at population scale that Paper 3 explicitly scopes as downstream. The tests provide a governance framework for assessing population-scope coordination practices, but implementers should treat them as advisory rather than mandatory compliance requirements.

**Adequately covered for initial audit.** The distribution above provides sufficient coverage to conduct a meaningful first governance audit of a CKS-governed inter-Self coordination deployment. The comprehensively covered categories address the governance commitments that Paper 3 defends as architectural claims. The partially covered category is appropriately scoped to the calibrated-humility posture of Paper 3's extension claim.

## 6. Three acknowledged gaps

Honest coverage assessment requires acknowledging where dedicated tests do not yet exist. Three gaps are identified.

**Gap 1 — Aspect contribution scope governance (beyond Test 8 in D2.24).** Paper 3's Claim 2 includes a five-step contribution governance protocol specifying how a participating Self selects which aspects to contribute, validates exchange scope, documents the selection authority, records the contribution event, and preserves the contribution record in the shared substrate. Test 8 in D2.24 addresses the general aspect contribution commitment, but no dedicated test in the 60-test library targets the five-step protocol as a complete governance object. A deployment could satisfy the general contribution requirement (Test 8) while operating the five-step protocol without full documentation at each step.

**Gap 2 — FAI configuration amendment governance.** Paper 3's Claim 5 establishes configuration as substrate content with recursive applicability, including the requirement (D2.38) that configuration amendments be recorded with version history under human authorization. Test 43 addresses the authorization chain for governance decisions and partially covers configuration amendment governance, but no dedicated amendment governance test exists. The version history requirement — that each configuration amendment preserves the prior version alongside the amendment record — is not independently assessed by any test in the current library.

**Gap 3 — Post-mortem completion compliance.** Test 47 assesses post-mortem quality: whether a post-mortem document meets the documentation standard. However, no test in the library assesses whether a post-mortem was conducted for every qualifying event. A deployment could produce high-quality post-mortems for the events it chooses to review while failing to review events that qualified for post-mortem under the governance configuration. The compliance question (was a post-mortem conducted?) is distinct from the quality question (did the post-mortem meet the standard?), and only the quality question is currently tested.

## 7. Future test development path

The three gaps identified above are the natural candidates for Tests 61–63 in the Phase D5 library, should Phase D5 notes continue to add tests:

**Test 61 (Gap 1 closure):** Does the governance record document all five steps of the aspect contribution governance protocol for each FAI event within the audit scope?

**Test 62 (Gap 2 closure):** Does the configuration amendment record include the version history required by the configuration governance commitment, with the prior version preserved alongside the amendment authorization record?

**Test 63 (Gap 3 closure):** For every event qualifying for post-mortem review under the governance configuration within the audit scope, does a post-mortem record exist?

These three tests are identified here as gaps rather than produced as complete derivation notes, for two reasons. First, the existing 60 tests provide adequate coverage for an initial governance audit; the gaps are marginal, not central to the Paper 3 governance commitments. Second, identifying the gaps as potential tests 61–63 provides a specific, actionable roadmap for future prior-art development — one that is concrete enough to constitute prior art itself against the gap territory while accurately representing the current state of the library.

The forward-looking identification also demonstrates that this prior-art corpus is actively maintained rather than static. Gap acknowledgment is not weakness; it is the evidence of a validation framework rigorous enough to identify its own limits.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Operational Test Library Validation.* May 15, 2026. ORCID: 0009-0004-8065-3235.
