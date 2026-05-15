# Scenario-Specific Operational Test Subsets

**Series:** D5.09 — Derivation Note #644  
**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** May 15, 2026  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

The FAI governance test battery defined in D2.24 and elaborated across Phase D5 contains 55 tests distributed across multiple functional clusters: construction and dissolution governance (D2.24 baseline), authority and participation governance (AP-series), governance quality (Tests 41–45), evolution learning (Tests 46–50), and governance relationship management (Tests 51–55). Running all 55 tests for every FAI event is comprehensive but may exceed governance capacity for simple, low-frequency, or operationally bounded events. This note defines six scenario-specific test subsets — First FAI Event (9 tests), Knowledge Transfer Event (8 tests), Competitive Intelligence Event (8 tests), High-Frequency Operations Audit (10 tests), Relationship Governance Audit (9 tests), and Governance Quality Deep Audit (14 tests) — that enable governance practitioners to run the most relevant tests for their specific context. Subset selection is justified by scenario relevance: each subset contains the tests whose FAIL conditions are most likely and most consequential in that specific governance context, not the tests that are easiest to run. Subset 6 is additionally identified as the pre-assessment instrument for organizations preparing for regulatory audit.

---

## 1. The governance capacity constraint

The 55-test FAI governance battery is theoretically complete. It covers every architectural commitment that Paper 3 makes about FAI events — from the construction and dissolution lifecycle through authority documentation, conflict handling, governance quality, evolution learning, and sustained-relationship governance. An organization that runs all 55 tests on every FAI event has comprehensive governance evidence for every event in its record.

Governance capacity, however, is finite. For organizations at the beginning of FAI participation, for events of limited structural complexity, or for relationships in routine operation with no unusual features, running all 55 tests per event may impose documentation and review costs that exceed what the event's risk profile warrants. The question governance practitioners face is not whether the 55 tests are correct but which tests are most likely to surface real failures given the specific characteristics of the event they are assessing.

This note addresses that question by defining six scenario-specific subsets. Each subset contains the tests whose FAIL conditions are most characteristically triggered by the governance scenario the subset is designed for. The subsets do not replace the full battery; they enable principled triage when governance capacity constrains comprehensive application. An organization may always run more tests than a subset specifies. An organization running fewer than the subset specifies should document the rationale for omission.

Two framing points apply across all six subsets. First, subset membership is determined by FAIL-condition relevance in the scenario, not by test complexity or test importance in the abstract. A test that is architecturally foundational but whose FAIL condition is unlikely to trigger in a specific scenario type does not belong in that scenario's subset. Second, subsets are not mutually exclusive. A given FAI event may qualify for multiple subsets simultaneously — a first participation in a competition-variant event qualifies for both Subset 1 and Subset 3, and the practitioner should run the union of those subsets' tests.

---

## 2. Subset 1 — First FAI Event (9 tests)

The first FAI participation for any organization is the governance event at which foundational infrastructure is most likely to be incomplete, misconfigured, or formally undocumented. Governance failures at this stage typically involve absence — missing conflict registry entries, undocumented authorization chains, evolution feed configurations that were assumed rather than governed — rather than the operational drift failures more common in mature FAI programs.

**Core tests:** Test 36 (AP-1, authority documentation), Test 37 (AP-2, authority chain completeness), Test 31 (AP-6, escalation path existence), Test 34 (AP-8, authority chain terminus), Test 3 (conflict registry construction), Test 9 (evolution feed authorization), Test 42 (documentation accessibility standards), Test 44 (non-specialist accessibility), Test 45 (non-delegation of governance authority).

The rationale for this selection is foundational absence: each of these tests probes for infrastructure that must exist at the governance level before any FAI event can be competently governed. Test 36 and Test 37 together establish whether the organization has documented who holds authority and whether that documentation is complete. Tests 31 and 34 establish whether escalation paths are real and whether authority terminates at a human. Test 3 establishes whether the conflict registry is in place. Test 9 establishes whether evolution-feed authorization has been governed rather than left to implicit assumption. Tests 42 and 44 together establish whether the documentation the organization has produced is usable — legible to non-specialist governance actors and accessible without specialized tooling. Test 45 closes the set by confirming that governance authority has not been delegated out of human hands.

Organizations conducting their first FAI event may additionally run D2.24 baseline Tests 1 (event construction governance), 2 (dissolution governance), and 3 (configuration documentation) as the foundational lifecycle record. These three baseline tests appear in multiple subsets and represent the minimum lifecycle evidence any FAI event should produce.

---

## 3. Subset 2 — Knowledge Transfer Event (8 tests)

Knowledge transfer FAI events are asymmetric by design: one Self contributes aspects for another to learn from, with explicit intent that the receiving Self will absorb content into its DNA evolution or action-feedback evolution. The distinctive governance risk in this scenario is absorption without appropriate scrutiny — the receiving Self internalizing contributed content under an assumed obligation to accept rather than a governed decision to absorb.

**Core tests:** Test 30 (non-obligation statement), Test 35 (AP-4, absorption decision governance), Test 48 (absorption reasoning documentation), Test 46 (trust calibration currency), D2.24 baseline Test 6 (contribution record completeness), D2.24 baseline Test 9 (evolution feed authorization), D2.24 baseline Test 11 (absorption governance record).

The rationale centers on the contribution-absorption boundary. Test 30 establishes that contribution to the shared substrate creates no obligation on the receiving Self to absorb the contributed content — the non-obligation principle that Paper 3 commits to at its evolution-feed boundary. Test 35 (AP-4) confirms that absorption decisions are governed rather than automatic. Test 48 confirms that where absorption occurs, the reasoning for selecting, modifying, or declining specific content is documented as substrate state. Test 46 assesses whether trust calibration between the two Selves reflects actual shared substrate experience rather than inherited or assumed trust levels, which matters distinctively in asymmetric events where the contributing Self may hold established authority not yet earned at the inter-Self scope. The three D2.24 baseline tests provide the lifecycle record within which the absorption governance sits.

---

## 4. Subset 3 — Competitive Intelligence Event (8 tests)

Competition-variant FAI events operate the same architectural primitive as cooperation-variant events — shared substrate construction, aspect exchange, dissolution — under a different orchestration rule set that scopes contribution and protects strategic content. The characteristic failure mode in this scenario is AP-14 (competition-variant collapse): an event that begins under competition orchestration rules progressively acquires characteristics of full-disclosure cooperation, either through gradual scope expansion in what is contributed, through conflicts being resolved in ways that reveal protected reasoning, or through post-event absorption that transfers content governance did not authorize for absorption.

**Core tests:** Test 23 (competition pair consistency), Test 33 (AP-3, silent collapse detection), Test 49 (carry-through completeness), Test 47 (post-mortem governance quality), Test 3 (conflict registry construction), Test 4 (conflict tier routing), Test 38 (black box substrate absence), Test 12 (escalation response appropriateness).

Test 23 is the defining test for this subset. It verifies that competition-variant event pairs — where the same two Selves participate in both cooperative and competitive events across a relationship — are governed consistently: the same conflict-handling rules, the same contribution-scope definitions, and the same absorption boundaries apply in competition events regardless of relationship familiarity. Test 33 probes for the AP-3 silent collapse pattern directly: whether the competition-variant orchestration rules remained in force throughout the event or whether the event drifted into unscoped disclosure without a formal governance decision to change scope. Test 49 confirms that whatever content the event produced carries through to post-dissolution records with complete provenance, preventing selective retention of strategically convenient content. Test 47 confirms that post-mortem documentation captures what competition orchestration rules were applied, not merely that the event occurred. Tests 3 and 4 together ensure the conflict infrastructure was in place and that conflicts were routed through the tier appropriate to their classification — a critical concern in competition events where conflicts may involve strategically sensitive content that the standard conflict resolution pathway would expose. Test 38 confirms that no substrate content existed outside the governed shared substrate during the event. Test 12 confirms that escalation was available and used appropriately for conflicts that exceeded standing authority.

---

## 5. Subset 4 — High-Frequency Operations Audit (10 tests)

Organizations conducting FAI events at daily or weekly cadence face a distinct governance risk: operational familiarity producing governance drift. What begins as rigorous per-event governance progressively becomes abbreviated documentation, assumed authorization, and pre-authorization patterns that bypass the deliberate review the governance architecture requires. The high-frequency operations audit subset is designed for sampled-event review in mature programs — not for every event, but for a regular sample sufficient to detect systematic drift.

**Core tests:** Test 21 (pre-authorization scope and currency), Test 25 (parent-child hierarchy compliance), Test 46 (trust calibration currency), Test 39 (governance theater detection), Test 41 (determinism in event records), Test 40 (time-pressure bypass detection), plus D2.24 baseline Tests 1 (construction governance), 2 (dissolution governance), and 3 (configuration documentation) for the sampled events.

The rationale is drift detection. Test 21 asks whether pre-authorization — the mechanism that allows high-frequency events to proceed without per-event deliberation — covers what it is being used to authorize, and whether it is current. Pre-authorization scope creep is the typical vector by which high-frequency programs begin authorizing more than governance intentionally committed to. Test 39 probes for governance theater: documentation that appears to satisfy governance requirements but records decisions that were made without actual deliberation. Test 41 confirms that event records are deterministic — that the same event would produce the same governance record regardless of who documents it, which is the operational signal that governance is being applied consistently rather than post-hoc. Test 40 identifies whether time-pressure has been used to justify bypassing deliberate governance steps — a failure mode that becomes normalized under operational tempo in high-frequency programs. Test 25 confirms that parent-child hierarchy compliance is maintained; in high-frequency programs, parent-entity approval is the governance step most frequently abbreviated. Test 46 confirms trust calibration is current, not inherited from relationship history. The three D2.24 baseline tests on construction, dissolution, and configuration provide the lifecycle record for the sampled events.

High-frequency organizations should run Subset 4 for a representative sample of events — not every event — and should apply Subsets 1, 2, or 3 to individual events when those events qualify for those scenario types.

---

## 6. Subset 5 — Relationship Governance Audit (9 tests)

A sustained FAI relationship — one in which the same two or more Selves participate in multiple events over an extended period — accumulates governance configurations, standing authorizations, and relationship-level agreements that require periodic review independent of any individual event audit. The relationship governance audit subset addresses this level: not what happened in a specific event but whether the governance infrastructure for the relationship as a whole remains current, coherent, and correctly scoped.

**Core tests:** Test 25 (parent-child hierarchy compliance at relationship scope), Test 22 (N-ary governance completeness for multi-party relationships), Test 43 (authorization chain integrity), Test 51 (participation configuration currency), Test 52 (capacity ceiling appropriateness), Test 53 (configuration currency), Test 55 (forced propagation absence), D2.24 baseline Test 14 (standing configuration review), D2.24 baseline Test 15 (agreement validity).

This subset operates at the relationship level, not the event level. Tests 51, 52, 53, and 55 are the relationship-configuration tests: they ask whether participation configurations remain accurate for the relationship as it currently exists (not as it was configured when the relationship began), whether capacity ceilings reflect current operational reality, whether configuration content is current, and whether the relationship record is free of forced propagation — content that moved across the perimeter without governed authorization. D2.24 baseline Tests 14 and 15 assess the standing configuration and the foundational agreement validity at the relationship level. Tests 25, 22, and 43 complete the governance infrastructure review: parent-child hierarchy compliance, N-ary governance completeness for multi-party relationships, and the integrity of the authorization chain through which relationship-level authority flows.

The relationship governance audit is appropriately run on a periodic schedule — annually or at major relationship milestones — rather than triggered by individual events. Organizations that run Subset 5 annually have a periodic governance record that demonstrates active relationship-level oversight, not only event-level compliance.

---

## 7. Subset 6 — Governance Quality Deep Audit (14 tests)

The governance quality deep audit is the most comprehensive of the six subsets. It is not a per-event assessment; it is a periodic relationship-level governance quality review appropriate for annual governance assessment, significant relationship expansion, or regulatory audit preparation. Subset 6 produces the most complete governance quality evidence record in the 55-test library and is the pre-assessment instrument practitioners should run before submitting to formal regulatory audit.

**Core tests:** All five governance quality tests (Tests 41–45: determinism, documentation accessibility, process documentation completeness, non-specialist accessibility, non-delegation), all five evolution learning tests (Tests 46–50: trust calibration currency, post-mortem quality, absorption reasoning, carry-through completeness, evolution pathway documentation), Test 38 (black box substrate absence), Test 39 (governance theater detection), Test 33 (AP-3 silent collapse detection), Test 43 (authorization chain integrity), plus D2.24 baseline Test 20 (complete governance record).

The rationale for this composition is audit-surface coverage. A regulatory auditor examining an FAI governance program will probe three dimensions: whether governance decisions were made through genuine deliberation rather than performed compliance (Tests 39, 41, 42, 44 together); whether the organization learned from its FAI experience and governed that learning (Tests 46–50 together); and whether the governance record is complete, traceable, and internally consistent (Tests 38, 33, 43, and D2.24 Test 20 together). The five quality tests and five learning tests form the core of the first two dimensions. The black box, theater, and silent collapse tests address the authenticity dimension that sits beneath compliance surface — an auditor who suspects that governance documentation was produced post-hoc or under competitive-scope drift will probe exactly these tests. Test 43 and D2.24 Test 20 provide the structural spine that the rest of the record hangs on.

Organizations preparing for regulatory audit (D2.63) should run Subset 6 as a self-assessment before the formal audit. A clean Subset 6 run produces a governance quality evidence record that addresses the dimensions most likely to be examined. A Subset 6 run that surfaces failures — even FAIL conditions that are subsequently remediated — provides the organization with information about governance gaps before those gaps are encountered in an adversarial review context.

---

## 8. Subset usage guidance

Four operational points govern how the six subsets should be applied:

**Subsets are not mutually exclusive.** An event may qualify for multiple subsets simultaneously. Where subsets overlap, the practitioner should run the union of the two subsets' test lists. For example, a first participation in a competition-variant event qualifies for both Subset 1 and Subset 3; the combined test list covers both the foundational-absence risks characteristic of first events and the competition-drift risks characteristic of competition-variant events.

**Subset 6 is periodic, not per-event.** Unlike Subsets 1–5, which are triggered by event type or operational cadence, Subset 6 is a relationship-level periodic assessment. It is not appropriate to run Subset 6 for each FAI event; it is appropriate to run it on a defined periodic schedule (annually is the baseline recommendation) and before any formal regulatory engagement.

**Subsets are floors, not ceilings.** Governance capacity permitting, practitioners may run more tests than a subset specifies. The subset defines the minimum test set whose FAIL conditions are most likely and most consequential in the scenario; it does not define the maximum test set that may be applied.

**Subset inapplicability should be documented.** Where a practitioner determines that a subset does not apply to an event that would ordinarily qualify — for example, a high-frequency event that is omitted from the sampled Subset 4 review — that determination and its rationale should be documented as substrate content. The omission record is itself governance evidence.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Scenario-Specific Operational Test Subsets.* Derivation Note D5.09 (#644), CKS Theory Series. May 15, 2026. ORCID: 0009-0004-8065-3235.
