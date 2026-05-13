# Operational Tests for Composition Pair Integrity: Five Tests Verifying That the Most Critical Phase B4 Composition Pairs Are Not Only Individually Present But Operationally Coupled

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Phase B4 of the CKS derivation-note series formalized composition pairs: combinations of architectural commitments whose joint presence defines a property that neither commitment establishes alone. A system can satisfy every Phase B4 commitment individually and still fail to instantiate the pair — if the commitments are present but not operationally coupled. This note formalizes five operational tests for composition pair integrity: the Instinct/Reasoning Substrate Cluster Integrity test (B1.01 + B1.06 + B1.07), the Evolution Cluster Productive Tension test (B1.12 + B1.13 + B1.14 + B1.15), the Substrate-Retraceability Compliance Foundation test (A1.08 + A1.07), the Governance-Recursive Foundational Pair test (A1.01 + B1.20), and the Evidence-to-Evolution Pipeline test (B1.15 + B2.26 + B1.14). Each test follows the five-field structure from B5.01: TEST QUESTION, TEST MECHANISM, PASS CONDITION, FAIL CONDITION, REMEDIATION SIGNAL. The composite integrity result requires all five tests to pass.

---

## 1. The Coupling Problem: Why Individual Presence Is Not Sufficient

Phase B4 composition pair notes established that certain architectural commitments are not merely additive — their conjunction is the architectural commitment. The instinct/reasoning separation (B1.01) and the DNA/action two-layer distinction (B1.06) together mean that the DNA layer specifically contains reasoning-layer governance that actively constrains instinct; neither commitment alone requires this. Governance (A1.01) and recursive governance (B1.20) together mean that human authority is present not only at deployment scope but at each entity level independently.

The critical operational problem: a deployment can satisfy every individual commitment while failing to instantiate the pair architecture. The DNA layer may contain governance content, and instinct/reasoning separation may be described as a design principle, without the DNA layer's governance ever actively constraining what the instinct layer does. The evolution mechanisms may each be present in substrate documentation without any cross-mechanism interaction having occurred.

Individual presence is necessary but not sufficient. Composition pair integrity tests verify operational coupling — that the commitments are working together as the pair architecture specifies, with evidence of that coupling in the substrate record. A deployment that passes individual commitment checks and fails coupling checks is exhibiting the class of failure B3.22 (Governance Theater) names: governance that satisfies the form while missing the substance.

---

## 2. Test 1: Instinct/Reasoning Substrate Cluster Integrity

**TEST QUESTION.** Are B1.01 (instinct/reasoning separation), B1.06 (two-layer DNA/action distinction), and B1.07 (expression mechanism) operationally coupled — not just individually present?

**TEST MECHANISM.** Coupling verification in two sub-checks.

Sub-check (a) — B1.01 + B1.06 coupling: Inspect the DNA layer of at least one cell. Determine whether the DNA layer contains reasoning-layer governance specifications — orchestration rules, conflict-handling policies, lifecycle rules — that govern what the instinct layer (LLM) is authorized to do during cell execution. Verify that the DNA layer does *not* contain action records. Verify that this separation is maintained for the reason B1.01 motivates: the reasoning layer must be able to route around or correct instinct, and a DNA layer that mixes records with rules cannot play that corrective governance role cleanly.

Sub-check (b) — B1.01 + B1.07 coupling: Verify the expression mechanism is present in the cell's harness substrate per B2.30. Verify that the expression mechanism functions as a reasoning-layer governance extension pathway — that which DNA-layer substrates activate for a given cell goal is governed by the harness substrate, not by arbitrary selection or operational default. Verify that carry-strategy per B2.32 is specified as a governed substrate choice with A2.40 provenance.

**PASS CONDITION.** DNA layer contains reasoning-layer governance rules that actively constrain instinct; DNA layer holds no operational records; Action layer holds operational records only; expression mechanism is present and governed by the harness substrate; carry-strategy is specified per B2.32; expression demonstrably extends reasoning governance cross-level.

**FAIL CONDITION.** DNA layer contains both rules and records (B1.06 + B1.01 coupling broken). Expression mechanism is absent, undocumented, or operating as an implementation convenience rather than a governed reasoning-layer pathway (B1.07 + B1.01 coupling broken).

**REMEDIATION SIGNAL.** Layer Conflation (B3.07) if sub-check (a) fails. Expression Mechanism Bypass (B3.08) if sub-check (b) fails.

---

## 3. Test 2: Evolution Cluster Productive Tension

**TEST QUESTION.** Are B1.12 (mutation — instinct evolution), B1.13 (directed selection — DNA evolution), B1.14 (action-feedback evolution), and B1.15 (multi-shaped governance) in productive tension — not just individually present but actively interacting?

**TEST MECHANISM.** Tension verification requiring event-record evidence from the substrate history.

Sub-check (a) — mutation–directed-selection tension: For each LLM update event (mutation, B1.12), verify whether a directed selection review event (B1.13) was triggered. When the instinct layer changed, did the reasoning-layer governance process review whether DNA content required update? Conversely, have directed selection changes prompted mutation re-verification?

Sub-check (b) — directed-selection–action-feedback pipeline: For action-feedback proposals generated from Action layer evidence (B1.14): have any produced directed selection events? Has directed selection been demonstrably informed by action-feedback evidence — evidenced in the substrate record, not merely possible in principle?

Sub-check (c) — productive tension indicator: Are all three mechanisms showing event records within the most recent governance cycle? Single-mechanism dominance with no cross-mechanism interaction events is the failure pattern.

**PASS CONDITION.** Mutation events have triggered directed selection reviews; action-feedback proposals have produced directed selection events; all three mechanisms have substrate event records within the recent governance period with demonstrable cross-mechanism interaction.

**FAIL CONDITION.** Mechanisms are documented individually but no cross-mechanism interaction events exist in the substrate record. Mutation occurs without triggering directed selection review. Action-feedback proposals are generated but never become directed selection events.

**REMEDIATION SIGNAL.** Single-Mechanism Evolution (B3.13) if mechanisms exist but lack cross-mechanism interaction. Establish cross-mechanism governance triggers: mutation events should generate directed-selection review items; action-feedback proposals should have a defined governance path to directed selection. Evolution Stasis (B3.24) if no evolution mechanism shows recent event activity.

---

## 4. Test 3: Substrate-Retraceability Compliance Foundation

**TEST QUESTION.** Are A1.08 (substrate authority — source of truth) and A1.07 (path retraceability) mutually reinforcing — can any current substrate content be traced through its governance history to confirm its authority?

**TEST MECHANISM.** Select any current DNA rule in the deployment (the selection should be arbitrary, not targeted at content known to be well-documented). Execute:

Step 1: Identify the directed selection event that created or last modified this rule. The rule's origin must be a nameable governance act with A1.07 retraceability.

Step 2: Verify the identified event carries A2.40 provenance metadata — writer identity, timestamp, rationale, authority basis — confirming authorized governance (A1.08).

Step 3: Trace backward to the rule's birth. Verify the authority claim holds throughout the lineage chain and no gap exists where governance history becomes unverifiable.

Systematic check: Apply A5.08 (operational test: substrate-as-source-of-truth) and A5.10 (operational test: determinism contract) together. A5.08 confirms the substrate's authoritative state categories are properly bounded; A5.10 confirms writes are addressable with provenance. Together they verify that A1.08 authority is demonstrable *through* A1.07 retraceable evidence, not merely asserted alongside it.

**PASS CONDITION.** Any selected DNA rule is traceable to an authorized governance act with full A2.40 provenance; the lineage chain to birth has no gaps; the authority claim holds at each point; A5.08 and A5.10 together confirm the source-of-truth property is demonstrable, not merely claimed.

**FAIL CONDITION.** DNA content with governance history gaps (A1.07 broken — content exists but its origin cannot be traced). DNA content whose authority is claimed but not demonstrable through retraceable history (A1.08 not supported by A1.07 evidence).

**REMEDIATION SIGNAL.** Provenance Void (B3.23) if systematic governance history gaps are found across multiple DNA rules — the substrate's source-of-truth property is structurally compromised. Ungoverned DNA Modification (B3.15) for specific unauthorized content identified during the trace.

---

## 5. Test 4: Governance-Recursive Foundational Pair

**TEST QUESTION.** Are A1.01 (human governance — three rights at all times) and B1.20 (recursive governance — governance at each entity level) operationally coupled throughout the deployment — not just at deployment scope but at each entity level?

**TEST MECHANISM.** Entity sampling and governance act attribution. Select one cell, one aspect, and one Self from the deployment.

For each selected entity, verify: Can governance acts at that entity's own level scope — governance acts whose scope is that specific entity's substrate content — be traced to human governance acts (A1.01) at that specific scope? Are there cell-scope governance events (cell DNA modifications, orchestration rule changes) authored by authorized humans with A2.40 provenance? Aspect-scope events? Self-scope events?

Critical verification: Are these governance acts at entity scope, not merely deployment-scope acts propagating downward by implication? Recursive governance (B1.20) requires that the governance architecture reaches each level with its own governance acts. Verify the authority coupling in both directions: entity-scope governance acts must also be traceable upward to authorized human actors (A1.01).

**PASS CONDITION.** Governance acts at cell, aspect, and Self scope are individually traceable to authorized humans; events exist at each entity level with A2.40 provenance; these are entity-scope acts, not deployment-scope acts applied by inheritance; the authority chain from entity-scope act to authorized human is unbroken.

**FAIL CONDITION.** Governance acts appear only at deployment scope — no independent cell-scope or aspect-scope governance events in the substrate record (B1.20 not met). Or governance acts exist at entity scope but cannot be attributed to authorized human actors (A1.01 not met at that scope). Or entity-scope governance exists only through downward propagation from deployment-scope rules.

**REMEDIATION SIGNAL.** Deployment-Level-Only Governance (B3.21) if governance has not been instantiated at entity level. Governance Theater (B3.22) if governance acts exist at entity scope but are performative rather than substantive — the form of governance is present without the substance of human authority exercised over that entity's content.

---

## 6. Test 5: Evidence-to-Evolution Pipeline

**TEST QUESTION.** Is the complete B1.15 + B2.26 + B1.14 evidence-to-evolution pipeline operational — from Action layer record accumulation through proposal generation through Stage 1 review through Stage 2 approval through DNA change?

**TEST MECHANISM.** Attempt to trace at least one complete pipeline execution through the substrate record. A complete execution has five stages, each identifiable as a distinct substrate event with A2.40 provenance:

Stage 1 (B2.26): Identify an Action layer record pattern constituting evidence that could inform DNA refinement.
Stage 2 (B1.14): Find the substrate output — a proposal or evidence summary — that references the Stage 1 pattern. This is the evidence-to-proposal translation.
Stage 3 (B1.15 Stage 1 review): Find the governance review event evaluating whether the proposal warrants advancement.
Stage 4 (B1.15 Stage 2 approval): Find the Stage 2 authorized approval event for the proposed DNA modification.
Stage 5: Find the DNA modification with A2.40 provenance linking it to Stage 4 approval.

If no complete execution has occurred — the deployment is new or no pattern has yet accumulated sufficient evidence — verify all five stages are *configured and ready*: accumulation active at Stage 1, proposal-generation capacity at Stage 2, human review capacity assigned at Stages 3 and 4, authorized modification pathways at Stage 5. Verify no stage is a structural bottleneck.

**PASS CONDITION.** At least one complete pipeline execution is traceable end-to-end with A2.40 provenance at each stage; or all stages are configured and ready with governance capacity and no bottleneck. The pipeline connects evidence to DNA change through authorized human governance at Stages 3 and 4.

**FAIL CONDITION.** The pipeline has never executed despite Action layer evidence accumulating across multiple governance cycles. Or Stage 3 or Stage 4 has no assigned governance capacity — the human review stages are structurally absent. Or no designed pathway connects Action layer content to DNA refinement.

**REMEDIATION SIGNAL.** Evidence Blindness (B3.28) if the pipeline has never executed despite accumulating evidence — operational experience is not feeding the governed evolution pathway. Identify the bottleneck stage: Stage 2 inactivity indicates B1.14 (action-feedback) is not operating; Stage 3 or Stage 4 absence indicates B1.15 (multi-shaped governance) is uninstantiated for the evolution pathway.

---

## 7. Composite Composition Pair Integrity Result

All five pair integrity tests must pass. The tests are not independent — failures cross-implicate.

A Test 1 failure (B3.07 Layer Conflation) implicates Test 3: when the DNA layer contains records as well as rules, the governance history trace becomes ambiguous because the governed-rule / operational-record boundary is unclear. A Test 4 failure (B3.22 Governance Theater) implicates Test 3: performative governance acts at entity scope also fail the authority-chain requirement the compliance foundation trace depends on. A Test 5 failure (B3.28 Evidence Blindness) implicates Test 2: if the evidence-to-evolution pipeline has never executed, action-feedback (B1.14) has no substrate event record, so Test 2's productive tension check fails for the B1.14–B1.13 interaction.

**Anti-pattern map:**

| Anti-pattern | Test | Coupling failure |
|---|---|---|
| B3.07 Layer Conflation | Test 1 | DNA holds records as well as rules |
| B3.08 Expression Mechanism Bypass | Test 1 | Expression absent or not functioning as reasoning-layer extension |
| B3.13 Single-Mechanism Evolution | Test 2 | Mechanisms present individually; no cross-mechanism interaction events |
| B3.22 Governance Theater | Test 4 | Entity-scope governance acts are performative, not substantive |
| B3.23 Provenance Void | Test 3 | Systematic governance history gaps undermine authority demonstration |
| B3.28 Evidence Blindness | Test 5 | Evidence accumulates but does not reach the governed evolution pathway |

A deployment that passes all five tests has demonstrated that its most architecturally critical composition pairs are not governance theater but functioning architecture — that the commitments are coupled in operation, not merely adjacent in documentation.

---

## 8. Relationship to Source Paper

The five pairs tested here derive from specific sections of the source paper. The Instinct/Reasoning Substrate Cluster (Test 1) derives from §4's separation architecture: the DNA layer constrains instinct for governance reasons, not storage reasons — the coupling is what §4's independently-evolving-layers-composing-into-one-governed-Self framing requires. The Evolution Cluster (Test 2) derives from §7's multi-mechanism architecture and §8's multi-shaped governance: §8 specifies distinct governance shapes for each mechanism, and governance shapes interact when the mechanisms do. The Compliance Foundation pair (Test 3) derives from Paper 1's §3.1 and §11.3: authority demonstrable through retraceability, not merely asserted alongside it. The Governance-Recursive pair (Test 4) derives from Paper 1's human-governed commitment extended by Paper 2's recursive levels: the enterprise brain (§10) is fully governed only if governance is present at each structural level independently. The Evidence-to-Evolution Pipeline (Test 5) derives from §7.2's action-feedback mechanism and §8's Stage 2 governance requirement: the evolution loop closes through authorized governance, not automatic substrate modification.

---

## Source

"The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance" (Li, April 2026), §4, §5, §6.2, §6.3, §7, §8, §10; and "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026), §3.1, §11.3.

---

*This note is part of the CKS derivation-note series. Note ID: B5.08. Series B — Paper 2 derivation. Phase B5 — Operational tests as standalone.*
