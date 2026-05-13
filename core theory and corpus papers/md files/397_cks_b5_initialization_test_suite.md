# Deployment Initialization Test Suite: The Test Battery Governance Runs When First Initializing a CKS Deployment to Confirm Complete Paper 2 Architecture Is Correctly Instantiated Before Operational Readiness Is Declared

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its contribution is to assemble the commitment-specific operational tests from the B5 series into a deployment-initialization-specific governance workflow, so that governance can confirm the complete Paper 2 architecture is correctly instantiated before declaring a deployment operationally ready.

---

## Abstract

The Coordination Knowledge Substrate (CKS) pattern, as extended in Paper 2, commits a deployment to a specific architecture: three structural levels (cell, aspect, Self), a DNA layer and action layer within each cell, a correct instinct/reasoning separation, an authority distribution across those levels, three evolution mechanisms configured for governed operation, and lifecycle operations that proceed through governed origination. Declaring a deployment operationally ready without first confirming these commitments are in place is a governance failure — the deployment would be operating without the architectural guarantees it claims to provide. This note formalizes the deployment initialization test suite: a sequenced six-stage governance workflow that tests each commitment area in dependency order, specifies the pass conditions and fail signals for each stage, and defines the operational readiness gate that stages 1–5 must clear before readiness can be declared. The suite is temporal in structure — organized by when governance runs it (at initialization, before operation begins) rather than by which architectural commitment it tests. It assembles tests from commitment-specific notes in the B5 series into a coherent initialization workflow. A deployment that passes all six stages enters ongoing operation with its Paper 2 architecture correctly instantiated and its governance record established.

---

## 1. Purpose and position of the initialization test suite

Paper 2's architecture is not self-enforcing. The commitments it defends — three-level structure, instinct/reasoning separation, governed lifecycle, evolution mechanism configuration, authority distribution — are architectural properties that a deployment either instantiates correctly or does not. Whether they are correctly instantiated is not knowable from the commitments alone; it requires governance action to confirm.

The deployment initialization test suite is that governance action. It is the first governance checkpoint in a deployment's life: the test battery run once, before the deployment accepts its first ongoing operation, to confirm the complete Paper 2 architecture is correctly in place. The suite does not test whether the deployment has performed well; it tests whether the deployment is structured correctly to perform at all.

The suite is temporal in orientation. It is organized by *when* governance runs it — at initialization, before operation — not by *which* commitment it tests. This is the defining feature of the B5.10–B5.13 temporal suite series. The commitment-specific tests developed in B5.02–B5.09 test individual architectural commitments in depth. The temporal suites assemble those tests into coherent governance workflows appropriate to specific governance moments: initialization (B5.10), ongoing monitoring (B5.11), and the evolution governance events that follow (B5.12–B5.13). The same test content appears in both the commitment-specific and temporal-suite notes; the temporal suite provides the sequencing logic and operational readiness gate that commitment-specific notes do not supply on their own.

The initialization suite covers six areas in sequence: entity inventory and governance origin; DNA specification completeness; authority and access configuration; evolution mechanism configuration; an initialization anti-pattern scan; and initialization verification recording. The sequence is not arbitrary. Each stage confirms properties that later stages assume. A deployment that fails Stage 1 cannot meaningfully proceed to Stage 2; the structural foundation is absent. The suite therefore operates as a fail-early pipeline: a failed stage halts the workflow and requires remediation before the next stage begins.

---

## 2. Stage 1 — Entity inventory and governance origin

Stage 1 establishes the deployment's complete entity inventory and confirms that all entities entered existence through governed origination.

**What Stage 1 tests.** Governance enumerates all initial entities in the deployment. For each entity, it confirms the presence of a governed birth record per B2.44 — the substrate-resident record that a birth event occurred under governance, who authorized it, and what authority scope applied. Governance also confirms that all three structural levels (cell, aspect, Self) are instantiated per B2.10 level-instantiation patterns — a deployment with cells but no aspect-level structure is structurally incomplete even if functionally capable in a narrow sense. For each entity, governance confirms the presence of a correct level determination record per B2.85: a record of which level this entity belongs to and by what determination.

**Stage 1 pass condition.** Complete entity inventory with governed birth records and correct level determinations for all entities. Three structural levels instantiated per B2.10 patterns.

**Stage 1 fail signals.** *Ungoverned Birth (B3.10)* — one or more entities lack a governed birth record; the deployment contains entities whose origins are not architecturally accounted for. *Flat Architecture (B3.03)* — the three-level structure is not instantiated; the deployment is missing one or more required structural levels. Both signals require halting and remediating before Stage 2.

The logic of Stage 1 priority is direct: subsequent stages test properties of specific entities and structural arrangements. If the entity inventory is incomplete, or if entities lack governed origins, or if the structure is flat, the subsequent stages are testing against an incomplete or ungoverned foundation. Stage 1 pass is the prerequisite for all that follows.

---

## 3. Stage 2 — DNA specification completeness

Stage 2 confirms that all entities have complete, level-appropriate DNA specifications and that the instinct/reasoning separation is correctly instantiated within each cell.

**What Stage 2 tests.** For each entity identified in Stage 1, governance confirms B2.90 content-domain specification completeness — the DNA-layer substrates that define the entity's function, rules, and behavior are fully specified, not partially drafted or implicitly understood. Governance also confirms that an initial DNA version per B2.69 is present with birth provenance: a substrate-resident record linking the initial DNA version to the birth event that established the entity. For each cell specifically, governance applies the B2.03 architectural test for instinct/reasoning separation: is the cell structured so that the fast-path instinct layer (LLM) and the deliberate reasoning layer (CKS substrate) are distinct and do not collapse into one another? Governance also confirms that routing rules per B2.04, high-stakes pinning per B2.05, and verification gates per B2.06 are configured for each cell.

**Stage 2 pass condition.** All entities have complete level-appropriate DNA specifications. All cells have instinct/reasoning separation instruments configured (routing rules, high-stakes pinning, verification gates).

**Stage 2 fail signals.** *Implicit Content-Domain (B3.19)* — one or more entities lack complete DNA specification; their content domain is assumed rather than substrate-resident. *Instinct-Reasoning Collapse (B3.02)* — one or more cells lack the architectural instruments that keep the instinct and reasoning layers separate. Both signals require remediation before Stage 3.

The logic here reflects Paper 2's foundational commitment. The instinct/reasoning separation is not just an organizational preference; it is what makes the CKS-governed Self's reasoning layer capable of routing around bad instinct, preserving conflicts that instinct would silently merge, and providing human-governed corrective signal without requiring model modification. A deployment without the separation correctly instantiated is not operating the Paper 2 architecture regardless of what it claims.

---

## 4. Stage 3 — Authority and access configuration

Stage 3 confirms that authority is distributed correctly across the three structural levels and that cross-level access rules are in place.

**What Stage 3 tests.** Governance confirms that A2.47 authority distribution is configured per level scope per B2.107 — each level (cell, aspect, Self) has a defined authority scope, and the governance actors who hold authority at each scope are specified. This is not about who happens to be available; it is about the architectural assignment of who can govern what. Governance also confirms that cross-level access rules per B2.95 are authored and substrate-resident: the rules governing when and how the Self can access cells directly, when aspects access cells in their arrangement, and what constraints apply to cross-level operations are recorded, not merely understood. Finally, governance confirms that B1.20 recursive governance architecture is in place: the Paper 1 architectural commitments (human-governed, substrate-cell boundary, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, linear-cost scaling) apply at each structural level, and the governance instruments that enforce these commitments at cell, aspect, and Self scope are all present.

**Stage 3 pass condition.** Authority distribution complete across all three levels per A2.47 and B2.107. Cross-level access rules authored and substrate-resident per B2.95. Recursive governance architecture established per B1.20.

**Stage 3 fail signals.** *Authority Ambiguity (B3.26)* — authority assignment at one or more levels is absent or ambiguous; governance actors do not have defined scope. *Ungoverned Cross-Level Access (B3.20)* — cross-level access rules are not substrate-resident; access patterns are operating without explicit governance. Both signals require remediation before operational deployment.

The governance logic: in ongoing operation, governance decisions about substrate content, evolution, and lifecycle events will require clear authority scope. A deployment that begins operation with ambiguous authority or ungoverned access patterns will face compounding governance failures as those decisions arrive without a clear resolution path.

---

## 5. Stage 4 — Evolution mechanism configuration

Stage 4 confirms that all three evolution mechanisms are configured for governed operation. This stage tests configuration, not exercise — at initialization, no evolution has occurred, and no such test would be meaningful. The question is whether the governance instruments required for each mechanism are in place and the governance workflow for each mechanism is established.

**What Stage 4 tests.** Governance confirms the presence of all three mechanisms per B2.60: instinct evolution, DNA evolution, and action-feedback evolution are all configured in the deployment's substrate. This is a configuration-presence check: all three must be present, not just the mechanism the operators expect to use first. Governance confirms that mutation governance instruments per B2.66 are configured for instinct evolution: verification gates, routing rules, and high-stakes pinning are in place so that when an LLM upgrade or infrastructure migration occurs, the governance response is pre-specified rather than improvised. Governance confirms that proposing substrates per B2.74 are configured with governed specifications for action-feedback evolution: the substrate-resident mechanism that converts action-layer evidence into DNA change proposals is present and its authority scope is defined. Governance confirms that the directed selection governance workflow is established for DNA evolution: the governance actors with authority per A2.47 to authorize DNA changes are identified, and the process by which proposed modifications are evaluated, authorized, and recorded is substrate-resident.

**Stage 4 pass condition.** All three mechanisms (instinct evolution, DNA evolution, action-feedback evolution) present and configured. Governance instruments for each mechanism present. Governance workflow for each mechanism established.

**Stage 4 fail signal.** *Single-Mechanism Evolution (B3.13) configuration state* — one or more of the three mechanisms is absent or not configured. The specific missing mechanism must be identified and established before ongoing operation begins.

The logic of configuration-only testing at initialization is direct. Evolution is dynamic; it happens over time. What initialization can confirm is whether the architecture is prepared to govern evolution when it occurs. A deployment missing instinct evolution instruments will be unequipped when the first LLM upgrade arrives. A deployment without action-feedback proposing substrates will be unable to close the learning loop from lived operation. Establishing the mechanisms before operation is not formalism; it is the precondition for governed operation when those moments arrive.

---

## 6. Stage 5 — Initialization anti-pattern scan

Stage 5 applies a focused anti-pattern scan to the initial state of the deployment, targeting patterns that are detectable at initialization and whose presence at initialization predicts governance failures in ongoing operation.

**What Stage 5 tests.** Governance scans for DNA content quality failures per B3.25: are the DNA specifications authored as CKS substrate content — explicit, structured, human-governed orchestration and behavior substrates — or are they effectively LLM prompt text stored in a substrate field? This distinction matters architecturally because LLM prompts in substrate fields are governed by a different logic than genuine DNA specifications, and a deployment that initializes with prompt-text DNA has not instantiated the DNA layer correctly regardless of how the content is labeled. Governance confirms that provenance infrastructure is present and operational per B3.23 scan: the substrate-resident machinery for recording birth provenance, DNA version history, and governance authorization is in place. Governance applies an early-detection scan for specification contradictions in initial DNA per B3.30: contradictions within the initial DNA state that, if left unresolved, will compound as the deployment operates. Governance also applies the B3.22 scan for birth governance substance: do the initial governance acts reflected in the deployment's birth records reflect substantive governance decisions, or are they records of a process that was carried out as procedure without meaningful review? Governance theater at initialization leaves the deployment without the genuine oversight that the birth record appears to provide.

**Stage 5 pass condition.** Initial anti-pattern scan clear: no B3.25 DNA content quality failures, B3.23 provenance infrastructure present and operational, no B3.30 specification contradictions, no B3.22 governance theater in initial records.

**Stage 5 fail signals.** Each anti-pattern requires immediate remediation per its specific failure mode. Stage 5 failures may be remediatable before or shortly after deployment depending on severity; a B3.23 provenance infrastructure absence is typically a hard block since subsequent governance recording depends on infrastructure being present; a B3.25 DNA content quality issue in a subset of cells may permit conditional deployment with immediate remediation timeline.

---

## 7. Stage 6 — Initialization verification recording and operational readiness declaration

Stage 6 records the results of the initialization test suite and, if stages 1–5 have all passed, declares the deployment operationally ready.

**What Stage 6 does.** Governance records the initialization test suite results per A2.40 with governance authorization: the record is substrate-resident, carries the identity of the governance actors who ran and authorized the suite, includes the timestamp of the initialization event, and specifies which stages were tested and what their outcomes were. If all stages pass, governance declares operational readiness: the deployment is confirmed to have the complete Paper 2 architecture correctly instantiated and may enter ongoing operation. If any stage has deferred items — remediations committed to but not yet complete at the time of the initialization event — governance records those items with remediation timelines and assigned responsibility. Deferred items do not prevent operational readiness declaration if their severity is consistent with governed conditional deployment; this determination is itself a governance act that must be recorded.

**Stage 6 pass condition.** Initialization test suite results recorded with governance authorization. Operational readiness declared if all stages 1–5 pass. Deferred items, if any, recorded with remediation timelines.

---

## 8. The operational readiness gate

The initialization test suite enforces a single operational readiness gate: a deployment that has not passed stages 1–5 is not operationally ready and may not be declared so.

The gate is strict for stages 1–4. A deployment that fails Stage 1 (ungoverned births or flat architecture) is missing the foundational structure the Paper 2 architecture requires. A deployment that fails Stage 2 (incomplete DNA or instinct-reasoning collapse) is operating cells without the separation and specification that make their behavior governable. A deployment that fails Stage 3 (authority ambiguity or ungoverned cross-level access) is entering operation without defined governance scope for the decisions that operation will require. A deployment that fails Stage 4 (single-mechanism evolution configuration) is unprepared for the evolution events that ongoing operation will generate. These are structural failures, not operational preferences, and the deployment is not the Paper 2 architecture until they are corrected.

Stage 5 permits more calibrated judgment. The anti-pattern scan identifies quality and integrity failures in the initial state. Some of these — absent provenance infrastructure — are hard blocks equivalent to stages 1–4. Others — DNA content quality failures in a subset of cells, or early-detected specification contradictions — may be remediatable in close proximity to operation. The governance judgment of which stage 5 failures are hard blocks and which permit conditional deployment is itself a governance act, must be substantive rather than theater (per B3.22), and must be recorded in the initialization verification record.

The gate's purpose is not formalism. A deployment that enters operation without confirmed architecture is a deployment that will attribute its operational failures to the wrong causes, apply corrective governance to the wrong locations, and build a governance record that misrepresents the deployment's state. The initialization test suite establishes the baseline against which all subsequent governance is measured.

---

## 9. Relationship to ongoing governance

The initialization test suite is the first of the B5 temporal test suites. It is designed to run once, at deployment initialization. It does not repeat in ongoing operation; its results are the baseline record of the deployment's initial state.

The second temporal suite, B5.11, covers the ongoing governance test suite — the test battery governance runs at regular intervals and at specific event triggers throughout the deployment's operational life. Where the initialization suite asks "is the architecture correctly instantiated?", the ongoing suite asks "is the correctly instantiated architecture continuing to function as committed?" The two suites are complementary: initialization establishes the baseline; ongoing monitoring measures against it.

Stage 6 of the initialization suite produces the recorded result that B5.11 will use as its starting reference. A deployment that records a clean initialization result and then encounters a discrepancy in ongoing monitoring has a well-defined governance signal: something changed between initialization and the monitoring event. A deployment without a clean initialization record has no such baseline, and ongoing monitoring cannot determine whether it is detecting new divergence or detecting a divergence that was present from the start. The initialization suite is therefore not just the first governance checkpoint but the precondition for meaningful ongoing governance.

---

## 10. Conclusion

The deployment initialization test suite formalizes the governance workflow that confirms a CKS deployment's complete Paper 2 architecture is correctly instantiated before operational readiness is declared. It proceeds in six stages: entity inventory and governance origin; DNA specification completeness; authority and access configuration; evolution mechanism configuration; initialization anti-pattern scan; and initialization verification recording. Each stage has explicit pass conditions and fail signals. Stages 1–5 enforce the operational readiness gate; Stage 6 records the results and declares readiness when all prior stages pass.

The suite's temporal orientation distinguishes it from commitment-specific tests. It does not repeat what those tests establish for individual architectural commitments. It provides the sequencing logic, dependency ordering, and readiness gate that transform commitment-specific tests into a coherent governance workflow appropriate to the initialization moment. A deployment that passes the initialization test suite has confirmed that it instantiates the Paper 2 architecture and has established the governance baseline against which all ongoing governance will be measured.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Deployment Initialization Test Suite: The Test Battery Governance Runs When First Initializing a CKS Deployment to Confirm Complete Paper 2 Architecture Is Correctly Instantiated Before Operational Readiness Is Declared.* May 13, 2026. ORCID: 0009-0004-8065-3235.
