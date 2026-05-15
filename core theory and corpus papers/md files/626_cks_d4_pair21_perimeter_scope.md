# Additional Composition Pair: Home Perimeter Integrity and Aspect Contribution Scope

**Series D — Phase D4, Note D4.21 (Note #626 in the derivation series)**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes the composition of two Paper 3 operational commitments: Home Perimeter Integrity Verification (D2.17) and Aspect Contribution Governance (D2.06). The composition produces three governance requirements that are non-obvious from either commitment alone: (1) a two-line perimeter defense structure in which contribution scope governance is the primary prevention mechanism and integrity verification is the secondary detection mechanism; (2) scope-calibrated integrity checks that focus governance resources on contributed aspects rather than all home aspects; and (3) incremental integrity checks as a pre-condition for each mid-event scope expansion. These requirements apply to any architecture that claims to provide governed selective AI knowledge contribution with integrity verification.

---

## 1. Pair Identification

**Commitment A — Home Perimeter Integrity Verification (D2.17).** Following participation in a Full Aspect Integration (FAI) event, a Self's home governance is required to run three checks confirming that the event did not alter the home governance architecture. Check A verifies that the home DNA of contributed aspects is unchanged. Check B verifies that contributed aspects remain governed by home rules. Check C verifies that home governance authority over contributed aspects is undiminished. These three checks are the post-event verification mechanism confirming that the home perimeter remains intact.

**Commitment B — Aspect Contribution Governance (D2.06).** Before and during a FAI event, home governance is required to govern two decisions: which aspects are included in the sharing scope, and what contribution record documents that scope. The sharing scope configuration is a Dimension 1 configuration object within the D1.22 governance-configured-sharing-scope commitment. The contribution record is the substrate-content artifact that documents the scope decision and makes it auditable.

These two commitments address adjacent stages of the same governance sequence. D2.06 governs what enters the inter-Self perimeter; D2.17 verifies that the home perimeter was not affected by what crossed it. The composition joins these two stages into a single governance flow.

---

## 2. Governance Scenario Requiring Both Simultaneously

Two organizations, each operating a CKS-governed Self, participate in a FAI event. Organization A contributes two of its aspects to the shared substrate; it withholds its remaining three aspects. The event completes and the shared substrate dissolves. Organization A's home governance must now confirm that FAI participation has not altered the home governance architecture.

Both commitments apply simultaneously. D2.06 governs what was contributed: the contribution governance record documents that precisely two aspects were in the sharing scope and three were not. D2.17 governs verification of the outcome: the three integrity checks confirm that the home perimeter was not affected by the event.

The scenario reveals the dependency between the two commitments. The D2.17 integrity checks cannot be properly executed without knowing the contribution scope the D2.06 record documents. If the scope record is absent or ambiguous, the integrity checks have no defined target: they cannot be calibrated to the aspects that were actually exposed. The composition establishes that D2.06 produces the input that D2.17 requires. Neither commitment alone specifies this dependency; the composition makes it explicit.

---

## 3. Non-Obvious Governance Requirements from the Combination

**Requirement 1 — Contribution Scope Is the First Line of Perimeter Defense.**

The sharing scope configuration produced by D2.06 governance is the primary mechanism protecting home perimeter integrity. The scope decision determines which aspects cross into the inter-Self perimeter. An overly broad scope — admitting aspects that should have remained home — is the most common root cause of home perimeter erosion (Anti-Pattern AP-7). The D2.17 integrity checks are the second line: post-event verification that the first line worked correctly.

This ordering has a non-obvious causal implication. A well-governed scope decision — one that is narrow, intentional, and documented — should produce clean integrity check results. A poorly-governed scope decision — one that is broad, reflexive, or underdocumented — will tend to produce integrity check failures or ambiguous results, because more of the home governance architecture was exposed than necessary. The composition establishes a prevention-then-detection architecture: scope governance (D2.06) is prevention; integrity verification (D2.17) is detection.

The implication for governance priority is direct: governing the scope decision carefully matters more than running the integrity checks efficiently, because the checks can only detect problems that the scope decision has already created. An architecture that treats D2.17 as the primary governance mechanism while treating D2.06 as administrative overhead has the priority inverted.

**Requirement 2 — Integrity Checks Must Be Calibrated to Contribution Scope.**

The three D2.17 checks must be calibrated to the specific aspects that the D2.06 record documents as contributed. Without this calibration, integrity verification is either under-inclusive or over-inclusive.

Under-inclusive verification occurs when the checks target aspects other than the contributed ones. An aspect that crossed the inter-Self perimeter may undergo governance-architecture change during the event; if the checks do not target that aspect specifically, the change goes undetected. Over-inclusive verification occurs when the checks target all home aspects indiscriminately. Aspects that were never near the inter-Self perimeter are expected to be unchanged; checking them for perimeter-related integrity violation wastes governance resources and introduces noise into the verification record.

Scope-calibrated checks apply each of the three D2.17 checks to the contributed aspects specifically. Check A verifies that the home DNA of contributed aspects is unchanged. Check B verifies that contributed aspects remain governed by home rules. Check C verifies that home governance authority over contributed aspects is undiminished. Non-contributed aspects are expected to be unchanged and are not the focus of D2.17 post-event verification.

The practical significance is greatest at high-frequency operations. An organization that participates in FAI events regularly, contributing small subsets of its aspects, will run D2.17 checks after every event. If the checks are not scope-calibrated, governance overhead grows with the size of the home governance architecture rather than with the size of the actual perimeter exposure. Scope calibration keeps verification cost proportional to exposure, not to architecture size.

**Requirement 3 — Scope Expansions During Events Require Incremental Integrity Checks.**

A FAI event may proceed through a governance-configured scope expansion: additional aspects are added to the contribution mid-event, via a configuration amendment of the kind D2.38 governs. Each scope expansion creates a new perimeter exposure for the newly added aspects. Those aspects were not in scope at the event's start; they had not been analyzed for perimeter integrity prior to the expansion.

The composition produces a pre-condition requirement: the D2.17 integrity checks must be run for the newly added aspects before the scope expansion takes effect. The incremental check is not a post-hoc audit; it is a gate. If the check reveals a governance-architecture concern for the newly added aspects, the expansion does not proceed until the concern is resolved under home governance authority.

This requirement emerges from the composition, not from either commitment alone. D2.06 governs the scope expansion decision; it does not specify what must happen before the expansion takes effect. D2.17 specifies three integrity checks; it does not specify when they must be run relative to scope changes during an event. The composition of the two commitments is what produces the incremental-check-as-gate requirement: each scope expansion is a new D2.06 decision, and each new D2.06 decision requires the D2.17 checks for the newly exposed aspects before the decision takes effect.

The governance risk addressed by this requirement is a race condition. Without the incremental check gate, an organization could expand the contribution scope, complete additional event activity with the expanded aspects, and then run D2.17 post-event only to discover that the expansion created perimeter erosion. At that point, event activity has already occurred under the compromised architecture. The incremental check gate closes the race condition by requiring detection before the exposure is acted upon.

---

## 4. Prior-Art Significance

Any architecture that claims to provide governed selective AI knowledge contribution with integrity verification must address the three requirements formalized above. The two-line defense structure — scope governance as prevention, integrity verification as detection — establishes a specific priority ordering that is not entailed by treating the two mechanisms as parallel or interchangeable. The scope-calibrated-checks requirement establishes that integrity verification must be targeted rather than comprehensive. The incremental-check-as-gate requirement establishes that scope changes during an event are not purely administrative — they create new verification obligations that must be discharged before the change takes effect.

These are specific governance properties of the composition. An architecture that runs integrity checks comprehensively across all home aspects does not instantiate Requirement 2. An architecture that treats scope expansions as administrative without verification pre-conditions does not instantiate Requirement 3. An architecture that treats integrity verification as the primary governance mechanism and scope governance as supporting does not instantiate the priority ordering Requirement 1 establishes.

The prior-art significance is that each of these properties is a specific, testable architectural commitment. They are not design preferences or implementation choices; they follow from the composition of D2.06 and D2.17. Any prior-art system that does not instantiate all three does not implement the composition this note formalizes.

---

## 5. Operational Test

For a completed FAI event, an observer can verify whether the D2.17 + D2.06 composition was properly instantiated by asking three questions:

**(a) Contribution record completeness.** Does the D2.06 contribution governance record document the specific aspects that were in the sharing scope at event start? The record must identify contributed aspects by name or identifier with sufficient precision to serve as the target specification for the D2.17 checks. A record that identifies contribution in general terms without naming specific aspects does not satisfy this test.

**(b) Scope calibration of integrity checks.** Do the D2.17 check records target the specific aspects identified in the D2.06 contribution record, rather than all home aspects or an undifferentiated set? The check records must be traceable to the contribution record: an observer should be able to confirm that Check A, Check B, and Check C each targeted the contributed aspects and not others. Check records that do not reference the contribution scope cannot be confirmed as scope-calibrated.

**(c) Incremental check records for mid-event scope expansions.** If the D2.06 record documents a scope expansion during the event, is there a corresponding D2.17 incremental check record for the newly added aspects that is timestamped before the expansion took effect? For each scope expansion, there must be an incremental check record that pre-dates the expanded-scope activity. A D2.17 check record that post-dates the expanded-scope activity does not satisfy the incremental-gate requirement.

A FAI event for which all three questions are answered affirmatively instantiates the D2.17 + D2.06 composition as formalized in this note. A FAI event for which any question cannot be answered affirmatively — either because the record is absent, undifferentiated, or post-dated — does not.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Additional Composition Pair: Home Perimeter Integrity and Aspect Contribution Scope.* Derivation Note D4.21 (#626), CKS Derivation Series. May 15, 2026. ORCID: 0009-0004-8065-3235.
