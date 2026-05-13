# Operational Tests for Instinct/Reasoning Separation (B1.01): Six Deployment-Facing Tests Including the Architectural Separation Test, Reproducibility Test, Mediator Role Test, Routing Verification, High-Stakes Pinning Test, and Verification Gates Test, Each With Question, Mechanism, Pass Condition, Fail Condition, and Remediation Signal

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, in operational test form per the B5.01 framework, the deployment-facing conditions under which a cell can be confirmed to instantiate the instinct/reasoning separation as B1.01 commits to it.

## Abstract

The instinct/reasoning separation (B1.01) is the foundational architectural commitment of Paper 2: a CKS-governed cell separates fast-pattern instinct (the LLM, operating as a System-1 analogue) from deliberate reasoning (the DNA layer of the CKS substrate, operating as a System-2 analogue) into two independently-governed layers under unified human authority. This separation does specific architectural work — it allows the reasoning layer to route around bad instinct, allows conflict preservation to catch what instinct would otherwise silently merge, and provides corrective signal without weight modification — but none of this work is observable from the architectural commitment alone. Observable confirmation requires operational tests applied to running deployments. This note formalizes six such tests. Test 1 (Architectural Separation Test, B2.03) asks whether the DNA layer governs the LLM or merely suggests to it. Test 2 (Reproducibility Test, A5.16) asks whether same DNA plus same inputs yields same outputs across invocations. Test 3 (Mediator Role Test, A5.05) asks whether the LLM operates within all five substrate-mediation properties. Test 4 (Routing Rules Test, B2.04) asks whether routing rules are present and operational for each cell. Test 5 (High-Stakes Pinning Test, B2.05) asks whether high-stakes decisions are identified and pinned to DNA rules. Test 6 (Verification Gates Test, B2.06) asks whether verification suites exist and run on mutation events. Each test specifies a question, a mechanism, a pass condition, a fail condition, and a remediation signal. A cell passes the B1.01 operational test when all six tests pass. The primary anti-patterns these tests detect are Instinct-Reasoning Collapse (B3.02) and Ungoverned Mutation (B3.14).

## 1. Why operational tests for the instinct/reasoning separation

B1.01 is an architectural commitment, not a self-confirming claim. A deployment can assert that it instantiates the instinct/reasoning separation while its LLM operates in practice as the entire system — producing outputs that reflect LLM inference rather than DNA governance, varying across invocations without DNA accountability, and handling high-stakes decisions through instinct rather than through pinned rules. The commitment at the architectural level does not prevent any of these failures at the deployment level. What prevents them — or more precisely, what makes them detectable and remediable — is operational testing.

The six tests in this note formalize six distinct dimensions along which the instinct/reasoning separation can fail in practice. Each test names a specific question a deployment reviewer can ask, a specific mechanism for getting an answer, specific conditions that constitute passing or failing, and a specific remediation signal pointing to the B3-series anti-pattern or the B2-series decomposition the failure indicates. The tests are deployment-facing rather than design-facing: they are applied to a running cell with real substrate content, real orchestration rules, and real LLM integration.

Two anti-patterns provide the primary diagnostic targets. Instinct-Reasoning Collapse (B3.02) names the failure in which the instinct and reasoning layers are not architecturally separated — in which the LLM carries what the DNA layer should carry, or in which the DNA layer nominally exists but exerts no governing constraint over LLM outputs. Ungoverned Mutation (B3.14) names the failure in which the cell changes — through LLM version updates, routing changes, or high-stakes decision accumulation — without governance discipline over what changes and what is preserved. Tests 1, 2, and 3 primarily detect B3.02; Tests 4, 5, and 6 primarily detect B3.14.

All six tests use the structure established in B5.01: TEST QUESTION, TEST MECHANISM, PASS CONDITION, FAIL CONDITION, REMEDIATION SIGNAL.

## 2. Test 1 — Architectural Separation Test (B2.03)

**TEST QUESTION:** For each cell, does the DNA layer (the reasoning layer) govern LLM behavior, or does it merely suggest to the LLM?

The governing/suggesting distinction is the load-bearing question for B1.01. A DNA layer that suggests provides prompts, context, or framing that the LLM may or may not honor; a DNA layer that governs constrains LLM outputs such that violations are architecturally detectable and redirected rather than silently passed through. The architectural separation the source paper commits to (§4) is a governance relationship, not an advisory one.

**TEST MECHANISM:** Inspect the cell's DNA specifications. For each DNA rule, ask: would the LLM's producing an output that violates this rule change the cell's observable output, or merely prompt different LLM behavior on the next invocation? Then run a direct behavioral test: present the cell with an input designed to trigger a specific DNA-governed behavior — an input for which the DNA specifies a particular response regardless of what LLM inference would independently produce. Verify that the cell's output reflects the DNA specification, not LLM inference. This test is per B2.03's treatment of the reasoning layer's governing role.

**PASS CONDITION:** DNA specifications constrain LLM outputs. The direct behavioral test produces an output that reflects DNA governance — the output is what the DNA specifies for that input, regardless of what an unconstrained LLM invocation would produce. Across multiple inputs designed to trigger DNA-governed behaviors, outputs consistently reflect DNA governance.

**FAIL CONDITION:** One or more of the following: (a) LLM outputs vary in ways that are not governed by DNA specifications, suggesting the LLM operates outside DNA constraint; (b) DNA "rules" are phrased as instructions, framing, or prompts that the LLM interprets rather than as governing constraints it operates within; (c) the direct behavioral test produces an output that reflects LLM inference rather than DNA specification; (d) there are no DNA specifications for the cell's behavioral domain, meaning all behavior is instinct-layer output.

**REMEDIATION SIGNAL:** Any fail condition signals Instinct-Reasoning Collapse (B3.02), specifically Form 2 — DNA nominally present but not governing. The remediation path is to establish governing DNA rules per B2.25 (the full decomposition of how governing DNA rules are structured and applied), distinguishing governing constraints from instructional prompts, and verifying that the governing constraints produce the behavioral test outcomes the separation requires.

## 3. Test 2 — Reproducibility Test (A5.16)

**TEST QUESTION:** Given the same cell DNA and the same inputs, does the cell produce the same outputs across multiple invocations?

The reproducibility question follows from what the instinct/reasoning separation requires of the reasoning layer. The DNA layer carries deliberate, human-governed reasoning outside the LLM — and deliberate reasoning, by definition, produces consistent results from consistent premises. If same DNA plus same inputs produces different outputs across invocations, the cell's output is being determined by something other than its DNA: by LLM instinct variation, by context drift, or by state held outside the substrate. Any of these indicates that the reasoning layer is not governing the instinct layer.

**TEST MECHANISM:** Invoke the cell with identical inputs under the same DNA version (same substrate content, same orchestration rules, same version identifier). Record outputs across a minimum of three independent invocations with no intervening state changes. Compare the outputs. This is A5.16's reproducibility test applied to Paper 2's two-layer architecture.

**PASS CONDITION:** Outputs are identical across invocations, within acceptable variation bounds for elements explicitly governed as non-deterministic in the DNA. The source paper's determinism contract (A1.10) permits non-determinism only for elements that are governed as such — meaning the DNA explicitly specifies which elements may vary and within what bounds. Reproducibility passes when the governing DNA produces consistent outputs and any variation is traceable to DNA-governed non-determinism.

**FAIL CONDITION:** Outputs vary across invocations in ways not governed by DNA specifications — the cell produces different results from the same DNA and inputs without any DNA rule accounting for the variation. This includes variation in structured outputs (content that should be determinate under DNA rules), variation in routing (the same input takes different paths across invocations), and variation in conflict handling (the same conflicting inputs are handled differently across invocations).

**REMEDIATION SIGNAL:** Output variation under same DNA and inputs signals A1.10 determinism violation. In the B1.01 context, the specific form is Instinct-Reasoning Collapse (B3.02): the LLM instinct layer is producing outputs that the DNA layer is not governing. The remediation path is to examine whether DNA rules are governing outputs or merely framing LLM invocations, whether LLM outputs are being passed through without DNA constraint, and whether any state relevant to the cell's outputs is held inside the LLM rather than in the substrate.

## 4. Test 3 — Mediator Role Test (A5.05)

**TEST QUESTION:** Does the LLM instinct layer operate within all five substrate-mediation properties (A5.05 Properties A through E)?

The A5.05 mediator role is the governing characterization of what the LLM's relationship to the substrate must be for the CKS pattern to hold. Paper 1's five-property formulation establishes that the LLM consults the DNA substrate before producing outputs, is governed by it, records its outputs in the action layer, operates within DNA-governed conflict resolution when its outputs conflict with DNA specifications, and is replaceable without changing the DNA governance architecture. In the Paper 2 context, these five properties are the operational expression of the instinct/reasoning separation at the cell level.

**TEST MECHANISM:** Verify each of the five properties independently. (A) Substrate consultation: inspect LLM invocations to confirm DNA substrate content is provided as governing context before the LLM produces outputs, not merely appended for reference. (B) DNA governance: confirm that LLM outputs are constrained by DNA specifications, not merely informed by them — per the mechanism of Test 1. (C) Action layer recording: confirm that LLM outputs that become cell outputs are recorded in the action layer as per the action-layer commitment in B1.03. (D) Conflict governance: present the cell with an input where the LLM would independently produce an output conflicting with a DNA specification; confirm the conflict is handled per the DNA's verification gates (B2.06) rather than passed through. (E) LLM replaceability: verify that the cell's DNA specifications are stated in terms of what the reasoning layer requires, not in terms specific to a particular LLM version — such that replacing the LLM would require reverifying DNA governance but not rewriting DNA content.

**PASS CONDITION:** All five properties hold. The LLM consults DNA before producing outputs (A), DNA governs LLM outputs (B), LLM outputs are recorded in the action layer (C), conflicts between LLM outputs and DNA are handled per verification gates (D), and the LLM is replaceable without changing DNA governance architecture (E).

**FAIL CONDITION:** Any property is violated. Specific fail conditions: (A) LLM is invoked without DNA substrate context, or DNA is appended as reference rather than provided as governing constraint; (B) LLM overrides DNA specifications or produces outputs outside DNA constraint — this is B3.02 form; (C) LLM outputs are not recorded in the action layer, making the execution invisible to governance; (D) conflicts between LLM outputs and DNA are passed through rather than governed, removing the conflict-catching function the separation provides; (E) replacing the LLM would require rewriting DNA content, indicating that reasoning is coupled to a specific instinct-layer implementation.

**REMEDIATION SIGNAL:** Violation of Property A or B indicates Instinct-Reasoning Collapse (B3.02) — the LLM is operating outside the governance relationship the separation requires. Violation of Property C indicates action-layer failure (B1.03). Violation of Property D indicates verification gate failure (B2.06). Violation of Property E indicates tool-agnosticism failure at the instinct layer (B1.10) — the reasoning and instinct layers are coupled in a way that the instinct/reasoning separation does not permit.

## 5. Test 4 — Routing Rules Test (B2.04)

**TEST QUESTION:** Are routing rules per B2.04 present and operational for each cell?

One of the concrete mechanisms through which the reasoning layer governs the instinct layer is routing: DNA rules that determine when to invoke the LLM, when to apply DNA rules directly without LLM involvement, which LLM version to route particular inputs to, and how to handle LLM unavailability. Routing rules are the DNA layer's authority over which instinct-layer resources are engaged for which inputs. Without routing rules, the cell treats all inputs as equivalent — routing all invocations to the current LLM version regardless of what the input requires — which is an Ungoverned Mutation failure mode.

**TEST MECHANISM:** Inspect the cell's DNA substrate per B2.25 for routing substrates. Verify: (i) routing rules specify conditions under which the LLM is invoked versus conditions under which DNA rules are applied directly; (ii) routing rules specify which LLM version or capability profile handles which input types; (iii) routing rules specify behavior when the LLM is unavailable — fallback to DNA rules, human escalation, or graceful degradation per cell design. Then test operationally: present the cell with inputs designed to trigger different routing paths and verify that the routing rules govern which path is taken.

**PASS CONDITION:** Routing rules are present, specific, and tested. The cell's DNA includes explicit routing substrates that govern LLM engagement. Operational testing confirms that different input types route per the routing rules, not per default LLM invocation patterns.

**FAIL CONDITION:** Routing rules are absent or effectively uniform — the cell routes all inputs to the current LLM version without discrimination. This includes: (a) no explicit routing substrate in DNA; (b) routing rules that are equivalent to "always invoke LLM" without differentiation; (c) routing rules that exist but are not tested and may be non-operational.

**REMEDIATION SIGNAL:** Absent or uniform routing rules signal Ungoverned Mutation (B3.14) Form 2 — the cell's behavior under input variation is governed by instinct-layer defaults rather than by DNA-layer routing rules. The remediation path is to establish routing rules per B2.04's routing-around-bad-instinct commitment, implemented through directed selection per B1.14 (DNA evolution under human governance), with routing substrates authored as human-governed DNA content specifying the conditions and targets of LLM engagement.

## 6. Test 5 — High-Stakes Pinning Test (B2.05)

**TEST QUESTION:** Are high-stakes decisions within the cell's operational scope identified, and are those decisions pinned to DNA rules rather than exposed to instinct-layer variation?

The instinct/reasoning separation permits LLM outputs for a wide range of cell behaviors. It does not permit LLM instinct to govern high-stakes decisions — decisions whose consequences are significant enough that variation across LLM versions, or variation across invocations under the same version, is not acceptable as a governance posture. For these decisions, the reasoning layer pins outputs to DNA rules regardless of what LLM inference would independently produce. Pinning is how the separation ensures that the most consequential cell behaviors remain in the reasoning layer where human governance directly applies, rather than drifting into the instinct layer where LLM variation applies.

**TEST MECHANISM:** Conduct a B2.05 high-stakes identification audit. Review the cell's operational scope — the full range of outputs the cell produces and the consequences of variation in those outputs — to identify decisions where incorrect or variable outputs carry significant consequences: safety consequences, compliance consequences, financial consequences, or governance-integrity consequences. For each identified high-stakes decision, verify that the cell's DNA contains pinning rules that govern the output for that decision class regardless of LLM instinct response. Then test operationally: present the cell with inputs designed to trigger high-stakes decision paths and verify that outputs reflect DNA pinning rather than LLM variation.

**PASS CONDITION:** All high-stakes decisions within the cell's operational scope are identified. Each identified high-stakes decision has DNA pinning rules that override LLM instinct outputs. Operational testing confirms that high-stakes decision paths produce outputs governed by DNA pinning.

**FAIL CONDITION:** One or more of the following: (a) high-stakes decisions are present in the cell's operational scope but not identified — the audit reveals consequential decision classes that have no pinning rules; (b) high-stakes decisions are identified but pinning rules are absent or advisory — the DNA specifies the desired output but does not architecturally override LLM instinct when the LLM would produce a different output; (c) pinning rules exist but are not tested for operational effectiveness.

**REMEDIATION SIGNAL:** Unidentified or unpinned high-stakes decisions signal Ungoverned Mutation (B3.14) Form 3 — consequential cell behavior is exposed to instinct-layer variation rather than governed by the reasoning layer. The remediation path is to conduct a complete high-stakes identification audit per B2.05, establish governing pinning rules in the DNA per B2.25 for each identified decision class, and implement pinning through the directed selection mechanism per B1.14 so that human governance directly controls the outputs that matter most.

## 7. Test 6 — Verification Gates Test (B2.06)

**TEST QUESTION:** Are verification gates per B2.06 present and operational for the cell — specifically, do they test LLM outputs against DNA specifications and do they run when the LLM version changes?

The verification gates commitment is the operational mechanism that makes instinct evolution governable. When the instinct layer (LLM) evolves — through version upgrades, infrastructure changes, or capability shifts — the previously established DNA governance may or may not continue to hold. LLM version N may have honored a set of DNA-governed constraints that LLM version N+1 violates, not through any change in the DNA but through shifts in the LLM's instinct behavior. Without verification gates that run at mutation events and test the instinct layer's behavior against the DNA layer's specifications, instinct evolution is ungoverned.

**TEST MECHANISM:** Inspect the cell's verification infrastructure per B2.06. Verify: (i) verification suites exist for the cell type, covering the cell's content domain per B1.18 (the cell's type-specific governance properties); (ii) suites test LLM outputs against DNA specifications — for each DNA-governed behavior, the suite includes test cases that confirm the LLM's outputs under that DNA governance produce the expected results; (iii) suites are configured to run automatically when LLM version changes (mutation events per B1.13); (iv) suite results produce explicit pass/fail outputs that governance processes can act on. Then test operationally: run the verification suite against the current LLM integration and confirm it produces actionable results.

**PASS CONDITION:** Verification gates are present, covering the cell's content domain, and operational for mutation governance. The suite runs at LLM version changes and produces pass/fail results. Suite results are reviewed as part of the governance process before LLM version changes take effect in production.

**FAIL CONDITION:** One or more of the following: (a) verification suites do not exist for the cell; (b) suites exist but do not test LLM outputs against DNA specifications — they test general LLM performance rather than governance-specific behavior; (c) suites are not configured to run at mutation events, meaning LLM version changes proceed without verification; (d) suite results are not reviewed as part of the governance process, making them inert as governance instruments.

**REMEDIATION SIGNAL:** Absent or non-operational verification gates signal Ungoverned Mutation (B3.14) Form 1 — the most direct form, in which instinct evolution proceeds without governance over what changes and what is preserved. The remediation path is to establish verification gates per B2.06, with suites authored to cover the cell's DNA-governed behaviors per B1.18, integrated into the mutation governance process per B1.13, and implemented through directed selection per B1.14 so that the verification gates are themselves DNA-governed rather than ad-hoc testing infrastructure.

## 8. Composite test result and anti-pattern detection

A cell passes the B1.01 operational test — confirming that it instantiates the instinct/reasoning separation as Paper 2's foundational architectural commitment requires — when all six tests pass. Each test is necessary; none is sufficient alone.

The composite result is not merely an AND of six independent conditions. The six tests are structurally related: Test 1 (governing vs. suggesting) is the foundational question; Tests 2 and 3 are behavioral confirmations that the governance relationship Test 1 establishes is operating as required; Tests 4, 5, and 6 are governance-coverage tests confirming that the reasoning layer's authority extends to routing, high-stakes decisions, and mutation events respectively. A cell that passes Tests 1–3 but fails Test 4 has an architectural separation that holds in static operation but lacks routing governance — instinct evolution can bypass the separation through version changes that routing rules would have caught. A cell that passes Tests 1–4 but fails Test 5 has a separation that holds for routine outputs but exposes consequential decisions to instinct-layer variation. A cell that passes Tests 1–5 but fails Test 6 has a separation that holds at a moment in time but is not maintained across the instinct-layer mutations that occur in every production deployment.

The two primary anti-patterns these tests detect have distinct signatures across the six tests:

**Instinct-Reasoning Collapse (B3.02)** is primarily detected by Tests 1, 2, and 3. A cell exhibiting B3.02 fails Test 1 because the LLM is not governed by the DNA layer; fails Test 2 because LLM instinct variation produces output variation that DNA governance does not account for; and fails Test 3 because one or more of the five mediator-role properties is violated — most commonly Property A (substrate consultation is nominal rather than governing) or Property B (DNA does not actually constrain LLM outputs). B3.02 can also appear in Test 4 as routing rules that are instructional rather than governing, and in Test 5 as high-stakes pinning rules that are advisory rather than constraining.

**Ungoverned Mutation (B3.14)** is primarily detected by Tests 4, 5, and 6. A cell exhibiting B3.14 may pass Tests 1–3 in a static snapshot — the architectural separation holds at the moment of testing — while failing to maintain that separation across evolution. Test 4 catches B3.14 Form 2 (routing without governance over LLM-version targeting); Test 5 catches B3.14 Form 3 (high-stakes decisions exposed to mutation-driven variation); Test 6 catches B3.14 Form 1 (instinct evolution without verification governance). A cell that fails any of Tests 4–6 is exhibiting Ungoverned Mutation even if its current instinct/reasoning separation appears intact, because the separation is not maintained by any governance mechanism that survives mutation.

When a cell fails one or more tests, the remediation signals point to the specific B3-series anti-pattern and the specific B2-series operational variant that the failure indicates. A cell that fails Test 1 needs governing DNA rules per B2.25. A cell that fails Test 3 Property E needs instinct-layer replaceability governance per B1.10. A cell that fails Test 5 needs high-stakes identification and pinning per B2.05 and B1.14. Each remediation path is specific because each failure is specific — the six-test structure ensures that a composite failure does not flatten into undifferentiated "the separation is broken," but preserves the diagnostic precision that governance attention requires.

## 9. Conclusion

The instinct/reasoning separation is architecture's answer to the failure mode in which the LLM is the entire system. It does specific work — routing around bad instinct, catching silent merges, providing corrective signal without weight modification — but none of that work is observable from the commitment alone. These six operational tests make it observable: they are the instruments by which a deployment reviewer confirms that the separation is not merely asserted but instantiated, not merely present at design time but maintained across the mutations that production deployment entails. A cell that passes all six tests has demonstrated that its DNA layer governs rather than suggests, that its outputs are reproducible under DNA governance, that its LLM operates within all five mediator-role properties, that its routing rules are present and operational, that its high-stakes decisions are identified and pinned, and that its verification gates run at mutation events. That is the full operational content of B1.01 as a deployment-facing commitment.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Operational Tests for Instinct/Reasoning Separation (B1.01): Six Deployment-Facing Tests Including the Architectural Separation Test, Reproducibility Test, Mediator Role Test, Routing Verification, High-Stakes Pinning Test, and Verification Gates Test, Each With Question, Mechanism, Pass Condition, Fail Condition, and Remediation Signal.* May 13, 2026. ORCID: 0009-0004-8065-3235.
