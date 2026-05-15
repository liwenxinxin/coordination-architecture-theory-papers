# Phase D4 Overview and Composition Pair Framework

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** D — Paper 3 Derivation Notes
**Note ID:** D4.01 (#606)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Phase D4 introduces composition pair analysis as a distinct phase within the Series D derivation note program. A composition pair is a governance scenario in which two architecture commitments must be applied simultaneously, and their interaction produces governance requirements that are not apparent from studying either commitment in isolation. Phase D2 covered each commitment's operational requirements separately; Phase D3 catalogued failure modes for individual commitments; Phase D4 covers what happens when two commitments must be correctly applied together. This note defines composition pairs, explains why non-obvious interaction governs the selection criterion, establishes the consistent five-element structure used across D4.02–D4.18, enumerates the seventeen planned pairs with brief descriptions, and positions the synthesis and closure notes at D4.19–D4.30.

---

## 1. Why a separate phase for composition pairs

The Series D derivation note program follows the same six-phase structure used in Series A (Paper 1) and Series B (Paper 2): foundational sub-commitments (D1), operational variants (D2), anti-patterns (D3), composition pairs (D4), operational tests (D5), and boundary cases (D6). Each phase addresses a distinct adversarial vulnerability.

Phase D2 addresses the vulnerability that an adversary might challenge any single commitment's scope or operational meaning. By decomposing each of Paper 3's six claims into their constituent sub-commitments and variants, Phase D2 forecloses challenges to individual commitments at the granular level.

Phase D3 addresses the vulnerability that an adversary might claim novelty for a failure mode or anti-pattern within the architecture. By cataloguing the canonical failure modes for each commitment — what happens when a commitment is violated or partially instantiated — Phase D3 establishes prior art for the failure modes themselves.

Phase D4 addresses a third vulnerability: adversaries may claim novelty not for a commitment in isolation, but for the specific governance scenario that arises when two commitments must be applied simultaneously. A claim such as "the governance requirements that emerge when time-sensitive coordination constraints interact with minimum viable governance floors is a novel contribution" cannot be foreclosed by any single-commitment note in Phase D2 or D3. Phase D4 closes this gap by establishing prior art for the specific governance requirements that emerge from two-commitment combinations — requirements that would not be apparent from either commitment's standalone treatment and that therefore cannot be attributed to either Phase D2 or Phase D3 notes individually.

This framing identifies the structural position of Phase D4 in the derivation note program: it is not a recombination exercise over Phase D2 content, but a distinct analysis of interaction effects. Every composition pair note contributes prior art that no Phase D2 or D3 note can provide.

---

## 2. What a composition pair is

A composition pair is defined by three properties.

**Two commitments identified.** Each composition pair specifies exactly two architecture commitments — drawn from Paper 3's claims and sub-commitments, or from cross-paper combinations with Papers 1 and 2 — by reference to their Series D note IDs.

**A governance scenario requiring both simultaneously.** Each composition pair identifies a specific governance scenario that requires both commitments to operate at the same time. The scenario is not an edge case or unusual configuration; it is a normal operational situation in which both commitments' requirements are active and must be satisfied together.

**Non-obvious governance requirements emerge from the combination.** This is the selection criterion. A composition pair is included in Phase D4 only if the governance requirements that emerge from applying the two commitments simultaneously are not predictable from reading either commitment's standalone treatment. If combining two commitments produces no requirements beyond what each demands independently — if the combination is additive and transparent — there is no composition pair and no Phase D4 note. A composition pair exists only where interaction produces governance requirements that are genuinely non-obvious from the commitments taken individually.

The non-obvious requirement is the analytical work of each composition pair note. Identifying which governance requirements emerge only from the combination — and would not be found by a reader who studied each commitment's standalone notes in sequence — is what distinguishes a composition pair note from a summary of two Phase D2 notes.

---

## 3. The five-element structure

Each composition pair note from D4.02 through D4.18 follows a consistent five-element structure. Consistency across the phase serves two purposes: it makes each note efficient and focused — covering one specific interaction between two commitments, rather than surveying either commitment broadly — and it makes each note's prior-art contribution explicit and auditable.

**Element 1 — Pair identification.** Names the two commitments and provides their Series D reference note IDs.

**Element 2 — The governance scenario that requires both simultaneously.** Describes the specific operational situation in which both commitments are active. The scenario is concrete enough that a reader can recognize it in practice.

**Element 3 — Governance requirements that emerge from the combination.** States the requirements that are not apparent from either commitment's standalone treatment. This is the analytical core of each note and the primary source of its prior-art value.

**Element 4 — Prior-art significance.** Identifies the specific adversarial claim the composition pair forecloses — the novelty argument an adversary could otherwise make about the combined governance scenario.

**Element 5 — Operational test for the combined requirements.** Provides a test that can be applied to a candidate implementation to determine whether the combined governance requirements are met. The test must be derivable from the combined requirements, not from either commitment's standalone test alone; if it can be derived from a single commitment's standalone test, the pairing does not meet the non-obvious selection criterion.

D4.19–D4.27 (additional pairs identified during Phase D4 development), D4.28 (cross-pair analysis), D4.29 (Phase D4 key claims index), and D4.30 (Phase D4 closure) follow adapted structures suited to synthesis and index functions rather than single-pair analysis.

---

## 4. Phase D4 scope: within-Paper-3 and cross-paper pairs

Phase D4 covers two categories of composition pairs.

**Within-Paper-3 pairs** combine two of Paper 3's six claims or their sub-commitments. These pairs arise because Paper 3's architecture is a composed system: shared substrate, Full Aspect Integration, three-tier conflict handling, four-locus evolution feed, configuration as substrate content, and population-scale evolution interact continuously in operation. Governance scenarios routinely require two of these commitments to operate simultaneously, and the interaction effects between them are not always transparent. Within-Paper-3 pairs establish prior art for these interaction effects.

**Cross-paper pairs** combine a Paper 3 commitment with a commitment from Paper 1 or Paper 2. These pairs arise because Paper 3 inherits from and extends both prior papers, and the full architecture operates across all three layers simultaneously. Cross-paper pairs are distinct from Series CC inheritance edge notes: a CC note establishes that a Paper 3 commitment inherits from a prior commitment without requiring fresh defense; a D4 cross-paper pair note establishes that a specific combined-governance scenario involving one Paper 3 commitment and one prior-paper commitment produces non-obvious governance requirements that neither commitment's standalone treatment predicts.

The partition rule follows the master plan: composition pairs that defend a Paper 3 commitment against a combined-commitment novelty claim go in D4; composition pairs that formalize inheritance edges go in Series CC; composition pairs that disambiguate cross-paper concept reuse go in Series T.

---

## 5. The seventeen planned pairs (D4.02–D4.18)

The following seventeen pairs constitute the planned D4.02–D4.18 sequence. Each entry names the pair and its governance scenario. The detailed governance requirements, prior-art significance, and operational tests are developed in the individual notes.

**Pair 1 (D4.02) — Minimum viable governance + time-sensitive coordination.** Governance requirements when an FAI event must be completed rapidly and must simultaneously meet the minimum viable governance floor. The non-obvious requirement concerns what minimum viable governance means when speed is a hard constraint — a question neither commitment answers alone.

**Pair 2 (D4.03) — Standing configurations + multi-Self events.** How standing configurations scale to N>2 participation without requiring N-specific amendments for every new cardinality. The non-obvious requirement concerns how a configuration authored for a known participant set remains governably applicable when cardinality increases.

**Pair 3 (D4.04) — Competition variant + preserve tier dominance.** How competition variant selection during an FAI event interacts with conflict tier routing configuration to produce the required governance instrumentation. The non-obvious requirement concerns what instrumentation is necessary at the intersection of variant selection and tier routing logic.

**Pair 4 (D4.05) — Exit rights + active FAI events.** Governance requirements when a Self exercises exit rights during an active FAI event rather than at a natural dissolution boundary. The non-obvious requirement concerns what obligations persist in the shared substrate after exit and who holds authority over them.

**Pair 5 (D4.06) — High-frequency events + governance health monitoring.** How governance health monitoring scales to high-frequency participation without requiring per-event review. The non-obvious requirement concerns what monitoring architecture is necessary to detect governance health degradation at rates that make event-by-event review impractical.

**Pair 6 (D4.07) — Population-scope participation + governance capacity.** How network participation configuration interacts with governance capacity constraints at the home perimeter. The non-obvious requirement concerns what participation configurations remain governable given bounded home perimeter capacity.

**Pair 7 (D4.08) — DNA absorption + aspect restructuring.** How DNA absorption decisions made at FAI dissolution inform and interact with subsequent aspect restructuring governance within the absorbing Self. The non-obvious requirement concerns what governance dependencies exist between the absorption decision and downstream restructuring authority.

**Pair 8 (D4.09) — Conflict carry-through + vertical evolution.** How preserved conflict carry-through annotations from the shared substrate enter and traverse the vertical evolution hierarchy within a home perimeter. The non-obvious requirement concerns what governance is required at the entry point and at each traversal step.

**Pair 9 (D4.10) — Regulatory audit + documentation standards.** Documentation requirements that emerge when both regulatory audit requirements and the architecture's documentation standards must be satisfied simultaneously. The non-obvious requirement concerns what documentation must be produced at the intersection of the two obligation sets — content neither set requires independently.

**Pair 10 (D4.11) — Knowledge transfer + DNA absorption.** Governance requirements that emerge specifically in the knowledge transfer context for DNA absorption decisions. The non-obvious requirement concerns how the knowledge transfer framing changes what home perimeter governance must authorize at the absorption boundary.

**Pair 11 (D4.12) — Competitive intelligence + post-mortem review.** Requirements for governing post-mortem access to competitive intelligence surfaced during FAI events. The non-obvious requirement concerns what access controls and authority structures are required when post-mortem review would reveal content that was protected under competition variant governance during the event.

**Pair 12 (D4.13) — Cross-organizational agreement + standing configuration.** How cross-organizational agreements at the shared substrate level interact with standing configurations maintained within each home perimeter. The non-obvious requirement concerns which layer's configuration takes precedence when the two conflict, and what governance is required to establish that precedence rule.

**Pair 13 (D4.14) — Emergency dissolution + evolution feed.** Governance requirements for evolution feed integrity when FAI dissolution is triggered by an emergency condition rather than by normal completion. The non-obvious requirement concerns what feed content is governable under emergency dissolution conditions versus what must wait for post-dissolution review.

**Pair 14 (D4.15) — Partial withdrawal + conflict registry.** How partial withdrawal from a shared substrate interacts with the obligation to maintain a complete conflict registry across all participating Selves. The non-obvious requirement concerns what registry obligations survive partial withdrawal and who holds authority over the residual registry entries.

**Pair 15 (D4.16) — Asymmetric Selves + standing configurations.** Standing configuration requirements when participating Selves have asymmetric governance authority or substrate maturity at the time a standing configuration is authored. The non-obvious requirement concerns how standing configurations remain governable when the authority asymmetry changes after authoring.

**Pair 16 (D4.17) — High-frequency events + cross-organizational agreement.** How cross-organizational agreements must be structured to remain governable under high-frequency event rates. The non-obvious requirement concerns what agreement provisions are necessary to sustain governance integrity at rates that would otherwise make per-event agreement amendment impractical.

**Pair 17 (D4.18) — Population participation governance + exit rights.** Governance requirements for population-scope participation when individual Selves exercise exit rights at different points in a collective evolution cycle. The non-obvious requirement concerns what population-level governance commitments survive individual exits and what re-entry conditions those commitments impose.

---

## 6. Additional pairs, synthesis, and closure (D4.19–D4.30)

D4.19 through D4.27 cover additional composition pairs identified during Phase D4 development. These notes follow the same five-element structure as D4.02–D4.18. Their specific pair assignments are determined during the drafting sequence as the interaction analysis of D4.02–D4.18 surfaces additional non-obvious combination effects not captured in the seventeen planned pairs.

D4.28 provides cross-pair analysis: an examination of patterns across the full Phase D4 corpus — recurring governance requirements, shared structural features, and higher-order interaction effects that are visible only when the pairs are considered together rather than individually. Cross-pair analysis serves the prior-art record by identifying structural regularities in two-commitment interactions; these regularities may themselves be relevant to adversarial claims at the pattern level.

D4.29 provides the Phase D4 key claims index: a structured summary mapping each composition pair to its prior-art claim, organized by the commitment combinations it covers. The index serves as the auditable record of what Phase D4 establishes collectively and as a navigation reference for subsequent work in Series D, Series CC, and Series T that draws on Phase D4 as a source.

D4.30 closes Phase D4 and positions the composition pair record for use by Phase D5 (operational tests), Phase D6 (boundary cases), Series CC (inheritance edge notes), and Series T (cross-paper concept disambiguation), each of which draws on Phase D4 in distinct ways.

---

## 7. Position in the Series D program

Phase D4 occupies the fourth position in a six-phase program. It depends on Phases D1 and D2 for the operational specifications of the commitments it combines, and on Phase D3 for the failure mode vocabulary it can reference when distinguishing composition pair analysis from anti-pattern analysis. The distinction matters: a D3 anti-pattern note establishes prior art for what happens when a single commitment fails; a D4 composition pair note establishes prior art for what governance is required when two commitments operate correctly together. The two phases address different adversarial vulnerabilities and neither subsumes the other.

Phase D5 (operational tests) draws on Phase D4 for combined-requirement tests that cannot be derived from single-commitment tests. Phase D6 (boundary cases) draws on Phase D4 for boundary behavior at commitment-combination boundaries — cases where the interaction between two commitments at an architectural edge produces unusual or contested governance requirements.

The practical value of Phase D4 for the defensive publication record is adversarial closure at the combination level. A reader who has reviewed Series D through Phase D3 has access to prior art covering all single-commitment governance requirements and all single-commitment failure modes. Phase D4 extends that record to cover two-commitment interaction scenarios, closing the gap that would otherwise allow novelty claims at the combination level to escape the prior art record. The seventeen planned pairs, plus additional pairs identified during development, constitute the Phase D4 contribution to that closure.

---

*Series D Derivation Note — D4.01 (#606)*
*Phase D4 — Composition Pairs*
