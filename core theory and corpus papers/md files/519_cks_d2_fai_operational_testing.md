# FAI Event Operational Test Suite

**Series D — Phase D2, Note D2.24 (Derivation Note #519)**
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D2.24 is a synthesis note drawing from D2.01–D2.23. It presents the FAI Event Operational Test Suite: twenty binary tests organized across five lifecycle phases — Pre-Construction, Construction, Operation, Dissolution, and Home Substrate — that governance can run to verify whether a Full Aspect Integration (FAI) event instantiates Paper 3's architectural commitments. Each test has a binary result: pass or fail. A FAI event is compliant when all twenty tests pass. A failed test identifies a governance gap and maps to a named anti-pattern from D2.19, making the suite diagnostic rather than merely evaluative. The suite is the inter-Self analog of the Phase B5 operational tests from Series B: the same binary structure, phase organization, and anti-pattern mapping applied at the inter-Self coordination scope Paper 3 introduces.

---

## 1. Purpose and Position

D2.18 established the complete governance record that a compliant FAI event must produce. D2.19 named twelve anti-patterns — governance failure modes that a FAI event instantiates when its architectural commitments are violated. D2.24 synthesizes these into an operational instrument.

The synthesis takes the following form. Each anti-pattern from D2.19 is addressable by one or more binary tests that governance can run against the FAI event's governance record. The tests are organized by lifecycle phase, matching the temporal structure of a FAI event: the phases through which every FAI event passes from initial configuration to post-dissolution home substrate evolution. Running the tests at the appropriate phase provides governance with timely information — pre-construction tests catch configuration failures before they are built in; operation tests catch contribution and conflict failures before dissolution locks them; home substrate tests verify that the event's dissolution fed home evolution under governance.

The twenty tests published here are prior art. They establish that operationally verifiable governance compliance for FAI events is not only possible but specifically enumerated. Each test is a concrete claim about what a compliant FAI event can demonstrate from its governance record. The prior-art value of the suite lies in its specificity: the tests are named, numbered, phase-assigned, and mapped to failure modes, foreclosing any later claim that FAI governance compliance is inherently unverifiable.

---

## 2. Inheritance from Paper 2 Phase B5

The Phase B5 operational test suite in Series B applied the same structural pattern to intra-Self deployment compliance: binary pass/fail tests organized by lifecycle phase, with failed tests mapped to named anti-patterns from Phase B3. D2.24 applies that pattern at inter-Self scope.

The inheritance is architectural, not merely structural. Paper 3's FAI mechanism is the inter-Self analog of Paper 2's cell mating mechanism — both are governed substrate-mediated coordination events with configuration, construction, operation, dissolution, and post-event evolution consequences. The governance test discipline that applies to one applies, at the appropriate scope, to the other. The same principle extends the prior-art chain: the test discipline is not an ad hoc addition to Paper 3 but a consistent architectural commitment that carries through the trilogy.

Where Phase B5 addressed single-Self deployment compliance, D2.24 addresses inter-Self FAI event compliance. The additional complexity at the inter-Self scope — joint authorization across multiple governance perimeters, home perimeter integrity during operation, cross-perimeter conflict handling — produces five additional tests relative to Phase B5's fifteen. The structure otherwise holds: phases, binary results, anti-pattern mapping.

---

## 3. The FAI Event Operational Test Suite

The suite contains twenty tests across five lifecycle phases. Each test is binary: **PASS** or **FAIL**. The test is run against the FAI event's governance record. Pass requires affirmative evidence in the governance record. The absence of a required record is a failure.

---

### Phase 1 — Pre-Construction Tests

*Run before the shared substrate is constructed. All five must pass before construction proceeds.*

**T1 — Configuration Authored as Substrate Content**
Is the FAI configuration authored as substrate content under the initiating Self's home governance, rather than as an infrastructure default or deployment parameter outside the substrate?

*Pass:* The governance record includes a configuration substrate with authorship provenance traceable to human authority within the initiating Self's home governance.
*Fail:* Configuration exists only as infrastructure default, platform parameter, or undocumented convention.

**T2 — All Six FAI Dimensions Specified**
Does the configuration specify all six configurable FAI dimensions: sharing scope, cardinality, persistence policy, cooperation/competition variant, provenance carry-over depth at the perimeter, and provenance preservation on internalization?

*Pass:* All six dimensions have explicit values in the configuration substrate.
*Fail:* One or more dimensions are unspecified, left to default, or deferred.

**T3 — Joint Authorization by All Participating Selves' Governance**
Is the configuration authorized by the governance of all participating Selves, not only the initiating Self?

*Pass:* The governance record includes authorization records from each participating Self's authority structure.
*Fail:* Authorization exists from only one Self, or authorization from any participating Self is absent or implicit.

**T4 — Conflict Resolution Rule Coverage Assessment Documented**
Is there a documented assessment of which conflict types the configured orchestration rules cover, and which are designated for escalation?

*Pass:* A coverage assessment exists in the governance record, identifying coverage and escalation designations.
*Fail:* No coverage assessment exists; conflict handling is left to runtime improvisation.

**T5 — Exchange Bounding Specification Present**
Does the configuration include an explicit specification that instinct-layer content and model weights are excluded from exchange — that only substrate content crosses the perimeter?

*Pass:* The configuration substrate contains an explicit exchange-bounding specification.
*Fail:* Exchange bounding is assumed, undocumented, or absent.

---

### Phase 2 — Construction Tests

*Run at the time the shared substrate is constructed. All three must pass for the construction to be governed.*

**T6 — Construction Record with Full Provenance**
Does a construction record exist in the governance record, with provenance linking the constructed shared substrate to the configuration substrate that authorized it?

*Pass:* A construction record exists with timestamps, participating-Self identification, and provenance link to the Phase 1 configuration.
*Fail:* No construction record exists, or the record lacks provenance linkage.

**T7 — Construction Record References Joint Authorization**
Does the construction record reference the joint authorization from T3?

*Pass:* The construction record explicitly references the joint authorization records from all participating Selves.
*Fail:* The construction record references only one Self's authorization, or references no authorization at all.

**T8 — Initial Orchestration Rules Present in Shared Substrate**
Are the initial orchestration rules that will govern operation present as substrate content in the shared substrate at the time of construction?

*Pass:* Orchestration rules are present as substrate content with authorship provenance, not injected later or held outside the substrate.
*Fail:* Orchestration rules are absent from the shared substrate at construction, or held only as platform configuration outside governance.

---

### Phase 3 — Operation Tests

*Run during the active event — periodically, and at any point where a governance question arises. All six must pass for the active event to be compliant.*

**T9 — Contribution Records in Both Home Substrate and Shared Substrate**
For each aspect contributed by each participating Self, does a contribution record exist in both the contributing Self's home substrate and the shared substrate?

*Pass:* Contribution records exist on both sides for every contribution, with provenance linking the two.
*Fail:* Contribution records exist on only one side, or a contribution is present in the shared substrate without a corresponding home-substrate record.

**T10 — Exchange Bounding Verified**
Is exchange bounding verified for each contribution? The four checks from D2.16 apply: (i) only substrate content crosses the perimeter; (ii) no instinct-layer content is present in the contribution; (iii) no model weights or weight-derived parameters are present; (iv) the contribution's content type is consistent with the exchange-bounding specification from T5.

*Pass:* All four checks pass for every contribution.
*Fail:* Any check fails for any contribution.

**T11 — Detected Conflicts in Conflict Registry with Both Sides Preserved**
Is each detected conflict recorded in the shared substrate's conflict registry, with both sides of the conflict preserved as substrate state?

*Pass:* Every detected conflict has a registry entry retaining both sides.
*Fail:* Any conflict is collapsed, silently resolved, or recorded with only one side.

**T12 — Conflict Registry Entries Have Tier Assignment and Status**
Does each conflict registry entry have a tier assignment (orchestration-resolvable, escalation-required, or preserved-unresolved) and a current status?

*Pass:* Every registry entry has both a tier assignment and a current status.
*Fail:* Any entry lacks a tier assignment, a status, or both.

**T13 — Governance Response Records for Escalated Conflicts**
For each conflict designated for escalation, does a governance response record exist, or has the escalation been acknowledged with an active response timeline?

*Pass:* Every escalated conflict has either a response record or an acknowledged active timeline within the governance response window.
*Fail:* Any escalation has no response record and no acknowledged timeline.

**T14 — Home Perimeter Integrity Maintained**
Is home perimeter integrity maintained for each participating Self throughout the event? The three checks from D2.17 apply: (i) no shared-substrate orchestration rules have modified home-substrate content outside the contribution pathway; (ii) home-substrate content not designated for contribution remains isolated from the shared substrate; (iii) the contributing Self's home governance retains authority over its home substrate throughout the event.

*Pass:* All three checks pass for every participating Self.
*Fail:* Any check fails for any participating Self.

---

### Phase 4 — Dissolution Tests

*Run at the time of dissolution. All three must pass for dissolution to be governed.*

**T15 — Dissolution Record Exists**
Does a dissolution record exist in the governance record, documenting that the shared substrate was formally dissolved and the event ended?

*Pass:* A dissolution record exists with timestamps and participating-Self identification.
*Fail:* No dissolution record exists; the event ended without formal closure.

**T16 — Persistence Policy Execution Documented**
Is the execution of the persistence policy documented — specifically, what content was retained, what was deleted, and where retained content was placed?

*Pass:* A persistence policy execution record exists, matching the policy specified in T2 and accounting for all shared substrate content.
*Fail:* Persistence policy execution is undocumented, or the executed policy differs from the T2 specification without governance authorization for the change.

**T17 — Hand-Off Boundary Activation Record Present**
Is there a hand-off boundary activation record specifying what content flowed to each participating Self's home substrate at dissolution, and under what governance authorization?

*Pass:* A hand-off record exists for each participating Self, identifying content, destination, and authorization.
*Fail:* No hand-off record exists, or any participating Self's hand-off is undocumented.

---

### Phase 5 — Home Substrate Tests

*Run post-dissolution, as home substrates process ingested content. All three must pass for home evolution to be governed.*

**T18 — Ingestion Authorization Records with FAI-Origin Provenance**
For each home action-layer ingestion of FAI-derived content, does an ingestion authorization record exist with FAI-origin provenance?

*Pass:* Every home action-layer ingestion of FAI-derived content has an authorization record naming the content, the authorizing human authority, and the FAI event of origin.
*Fail:* Any FAI-derived action-layer content enters a home substrate without an authorization record or without FAI-origin provenance.

**T19 — DNA Absorption Records with Home Governance Authorization and FAI-Origin Provenance**
For each DNA absorption of FAI-derived content, does a directed selection event record exist with home governance authorization and FAI-origin provenance?

*Pass:* Every DNA absorption of FAI-derived content has a directed selection event record naming the absorbed content, the human authority who authorized the selection, and the FAI event of origin.
*Fail:* Any FAI-derived DNA content is absorbed into a home substrate without a directed selection event record, without home governance authorization, or without FAI-origin provenance.

**T20 — Home Perimeter Integrity Verified Post-Event**
Is home perimeter integrity verified for each participating Self after the event concludes and ingestion is complete?

*Pass:* A post-event perimeter integrity verification record exists for each participating Self, confirming that home substrate authority structures are intact and no shared-substrate orchestration rules persist in home substrate operation.
*Fail:* No post-event verification record exists, or verification finds a perimeter integrity breach.

---

## 4. Complete Test Result

**Compliant:** A FAI event is **compliant** when all twenty tests pass across all five phases.

**Governance gap:** A FAI event has a **governance gap** at each test that fails. Failed tests identify specific gaps in the governance record and name the lifecycle phase at which the gap occurred. A governance gap does not retroactively void the event; it identifies what is missing from the governance record and what remediation is required.

**Phase-level result:** A FAI event may be compliant at some phases and have governance gaps at others. Phase-level compliance is meaningful independently: a FAI event compliant through Phase 3 but with Phase 4 failures has a dissolution governance gap, not a construction or operation governance gap.

**Partial compliance:** Tests within a phase are not ordered by severity. Any failure within a phase constitutes a governance gap at that phase. Governance should address all failures in a phase before treating the phase as complete.

---

## 5. Anti-Pattern Mapping

Failed tests map to the anti-patterns named in D2.19. The mapping makes the test suite diagnostic: when a test fails, governance knows not only that a gap exists but which named failure mode was instantiated. This identification is the basis for targeted remediation.

| Failed Test(s) | Anti-Pattern (D2.19) |
|---|---|
| T1, T2, T3 | AP-6 — Implicit Configuration |
| T4 | AP-3 — Silent Conflict Collapse (coverage gap) |
| T5 | AP-8 — Exchange Bounding Violation (specification absent) |
| T6, T7, T8 | AP-1 — Ungoverned Construction |
| T9 | AP-5 — Non-Attributed Contribution / AP-12 — Informal Record |
| T10 | AP-8 — Exchange Bounding Violation (operational) |
| T11 | AP-3 — Silent Conflict Collapse (operational) |
| T12 | AP-3 — Silent Conflict Collapse (tier/status absent) |
| T13 | AP-11 — Unresponsive Escalation |
| T14, T20 | AP-7 — Home Perimeter Erosion |
| T15, T16, T17 | AP-2 — Ungoverned Dissolution |
| T18 | AP-5 — Non-Attributed Ingestion |
| T19 | AP-4 — Automatic DNA Absorption |

**Multiple anti-patterns from a single failed test:** T9 maps to two anti-patterns because a missing contribution record may indicate either a provenance failure (AP-5) or an informality failure (AP-12), and both possibilities warrant investigation. T5 and T10 both map to AP-8 because exchange bounding can be violated at specification (T5) or at operation (T10); both failures instantiate the same anti-pattern at different lifecycle phases.

**Compounding failures:** Several anti-patterns can be instantiated by failures at multiple tests. AP-3 (Silent Conflict Collapse) can appear through T4 (coverage gap), T11 (operational collapse), or T12 (tier/status absent). A governance audit that finds all three T4/T11/T12 failures is encountering a systemic AP-3 instantiation, not three independent gaps. Remediation should address the pattern.

---

## 6. Operational Guidance: When to Run Each Phase

**Phase 1 tests (T1–T5)** are run before the shared substrate is constructed. The appropriate trigger is governance review of the configuration substrate — the moment when participating Selves' governance are approving the configuration. Failure at Phase 1 should prevent construction from proceeding. Constructing over unresolved Phase 1 failures does not resolve the failures; it carries them forward as latent governance gaps.

**Phase 2 tests (T6–T8)** are run at the time of construction, or immediately after construction records are created. The appropriate trigger is construction record creation. Phase 2 tests verify that the construction event was captured with adequate provenance and that orchestration rules are in place. They are fast to run because they depend only on the construction record, not on operation history.

**Phase 3 tests (T9–T14)** are run during the active event. Governance may run them periodically — at scheduled intervals during a long-running event, or event-triggered by significant contributions, new conflicts, or escalations. T9 and T10 should be run at each contribution. T11, T12, and T13 should be run whenever the conflict registry is updated. T14 should be run at regular intervals and whenever a perimeter integrity concern arises. A full Phase 3 review should be run before dissolution is authorized.

**Phase 4 tests (T15–T17)** are run at dissolution. The appropriate trigger is the dissolution decision itself: before the shared substrate is decommissioned, governance should confirm that T15–T17 pass. Running Phase 4 tests post-dissolution is possible but requires that the governance record be preserved; the tests assess the governance record, not the shared substrate directly.

**Phase 5 tests (T18–T20)** are run post-dissolution, as each participating Self's home governance processes ingested content. T18 and T19 are run at each ingestion event — action-layer ingestion and DNA absorption respectively. T20 is run once ingestion is complete, as a final verification of home perimeter integrity. Phase 5 tests are home-governance responsibilities; each participating Self runs them for its own home substrate independently.

---

## 7. Prior-Art Significance

Twenty specific, named, phase-assigned, anti-pattern-mapped tests for FAI governance compliance now exist as published prior art. Several implications follow.

The tests establish that FAI governance compliance is verifiable. Each test is a concrete claim about what a compliant FAI event can demonstrate from its governance record. The suite forecloses any later argument that FAI governance compliance is inherently abstract, unverifiable, or dependent on context-specific judgment. The twenty tests are specific enough to run.

The anti-pattern mapping establishes that governance gaps are characterizable. A compliance audit that finds failures does not produce a generic "non-compliant" result; it produces a specific diagnosis: which anti-patterns were instantiated, at which lifecycle phase, by which missing or deficient record. This characterizability is what makes the suite a diagnostic instrument rather than merely a compliance checklist.

The lifecycle-phase organization establishes that governance responsibility is temporally distributed. Pre-construction governance failures are distinct from construction failures, which are distinct from operation failures, dissolution failures, and post-event home-substrate failures. Temporal specificity clarifies which authority structure is responsible for remediation: configuration failures are joint-governance failures; construction failures are initiating-Self failures; home substrate failures are home-governance failures of the respective Self.

The inheritance from Paper 2 Phase B5 establishes that the test discipline is a trilogy-level architectural commitment. The same binary structure, phase organization, and anti-pattern mapping that applies to single-Self deployment compliance (Phase B5) applies to inter-Self FAI event compliance (D2.24). The test discipline is not introduced for the first time at Paper 3 scope; it is extended to that scope from the foundation Phase B5 established. This consistency across the trilogy is itself a form of prior art: it demonstrates that the CKS governance framework includes operational testability as a standing commitment at each architectural scope.

---

## 8. Summary

Twenty binary tests organized across five lifecycle phases — Pre-Construction (T1–T5), Construction (T6–T8), Operation (T9–T14), Dissolution (T15–T17), and Home Substrate (T18–T20) — constitute the FAI Event Operational Test Suite. A FAI event is compliant when all twenty pass. Failures identify governance gaps and map to the twelve anti-patterns named in D2.19. The suite is the inter-Self analog of Paper 2's Phase B5 operational tests, inheriting the same binary structure, phase organization, and anti-pattern mapping at the scope Paper 3 introduces. Governance should run Phase 1 tests before construction, Phase 2 tests at construction, Phase 3 tests periodically during operation, Phase 4 tests at dissolution, and Phase 5 tests as home ingestion proceeds post-dissolution.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *FAI Event Operational Test Suite.* Series D — Phase D2, Note D2.24 (Derivation Note #519). May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
