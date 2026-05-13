# Operational Tests for Anti-Pattern Detection: Five Deployment-Facing Detection Tests for the Most Dangerous Cross-Cutting Anti-Patterns

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Phase B3 of the CKS derivation note series formalizes thirty anti-patterns specific to deployments of the instinct/reasoning separation architecture. Five of these anti-patterns are distinguished from the rest by two properties: they are cross-cutting (each spans multiple architectural commitments, corrupting the deployment at a structural level rather than within a single commitment's scope) and self-concealing (each produces surface artifacts that resemble correct behavior, making them invisible to commitment-specific tests). This note formalizes five operational detection tests, one for each cross-cutting anti-pattern: Governance Theater (B3.22), Provenance Void (B3.23), LLM Governance Conflation (B3.25), Specification Integrity Collapse (B3.30), and Evidence Blindness (B3.28). Each test follows the standard B5 structure: TEST QUESTION, TEST MECHANISM, PASS CONDITION, FAIL CONDITION, and REMEDIATION SIGNAL. The tests use qualitative detection mechanisms — authorizer explanation interviews, governance awareness probes, DNA content quality analysis — that go beyond record inspection to test governance substance directly. These five tests are complementary to the commitment-specific tests in B5.02–B5.07: where the commitment-specific tests verify that individual CKS structural commitments are present, the anti-pattern detection tests verify that those structures are substantively functioning, not merely formally populated.

---

## 1. Why these five anti-patterns require dedicated detection tests

The thirty B3 anti-patterns cover failures across every layer of the instinct/reasoning separation architecture: malformed lifecycle events, misconfigured evolution mechanisms, broken governance boundaries, and coordination failures between architectural levels. Most of these anti-patterns are detectable through targeted commitment tests because they corrupt the structural properties those tests measure. A misconfigured DNA evolution pathway, for example, produces detectable anomalies in the governance record structure that a B5 commitment test for DNA evolution can identify.

Five anti-patterns resist this approach. They do not corrupt the structural properties the commitment tests measure — they hollow them out while leaving the structural shell intact. A deployment exhibiting Governance Theater produces governance records that pass structural inspection because the records exist; the test cannot detect that the humans named in those records did not make the decisions the records attribute to them. A deployment exhibiting Evidence Blindness accumulates a well-formed Action layer; the structural test passes because the layer is present and correctly formatted. The anti-pattern is not in the structure — it is in the absence of any connection between the structure and governance behavior.

This hollowing-out property is what makes these five anti-patterns the most dangerous in the B3 catalog. They are also cross-cutting: Governance Theater simultaneously corrupts the human-governed commitment, the path retraceability commitment, and the DNA evolution commitment, because all three depend on governance being substantive rather than performative. Specification Integrity Collapse simultaneously corrupts the determinism contract, the DNA layer commitment, and the expression mechanism. A deployment can fail all five of these anti-patterns simultaneously while passing every commitment-specific B5 test, because the commitment tests verify structural presence and the anti-patterns corrupt structural function.

The five detection tests in this note are designed around this property. Each mechanism probes substance rather than structure, and each uses detection approaches that the anti-patterns cannot survive without genuine governance being present.

---

## 2. Structural position of detection tests in the B5 series

The B5 operational test series covers twenty tests for the instinct/reasoning separation architecture. Tests B5.02 through B5.07 address individual architectural commitments: birth as governed origination, mating with three patterns, death with two types, instinct evolution governance, and related commitments. These tests verify that the structures the commitments require are present and correctly formed.

B5.09 occupies a distinct position in the series. Its five tests do not target individual commitments; they target the five anti-patterns that span commitments. The tests are additive, not substitutive: a deployment should run both the commitment-specific tests and the anti-pattern detection tests. Passing commitment-specific tests and failing anti-pattern detection tests is a coherent outcome — it identifies a deployment that has the structural components of correct CKS architecture while exhibiting governance failures that the structural components cannot self-report.

B5.10 through B5.15 will address remaining B5 test subjects. B5.09 sits immediately after B5.08 (instinct evolution governance) because the cross-cutting nature of these five anti-patterns means they can manifest in any evolution mechanism, lifecycle event, or governance process — making their detection a necessary precondition for interpreting the results of all commitment-specific tests.

---

## 3. Test 1 — Governance Theater Detection (B3.22)

**TEST QUESTION:** Is governance in this deployment substantive — genuine human authority over cell behavior exercised through DNA specification, birth authorization, and death decision — or is it performative: governance-shaped activities that produce governance-format artifacts without governance substance?

**TEST MECHANISM:** Three substance tests applied in combination.

*(a) Authorizer Explanation Test.* Select five recent governance events from the substrate record — at least one DNA modification, one birth authorization, and one death decision. Identify the human whose name appears in the authorization record for each event. Ask each named human to explain the governance reasoning behind their authorization, in their own words, without consulting substrate records or LLM assistance during the explanation. Evaluate coherence and specificity: a genuine governance actor can explain what inputs they considered, what constraints the DNA modification was intended to enforce or relax, why the birth was authorized at that scope, or what failure mode the death decision was responding to. A theater participant cannot produce this explanation without records because the decision was made by or with an LLM rather than by the named human.

*(b) Behavior-Specification Alignment Test.* Select three DNA specifications covering different input types. Invoke cells with inputs specifically covered by those specifications. Verify that cell outputs match the behavior the DNA specification predicts. In a genuine governance deployment, DNA specifications are operational constraints that predict cell behavior because they were written to constrain it; in a theater deployment, DNA reads as guidance prose that does not actually govern cell behavior, producing a gap between specified and observed behavior.

*(c) Provenance Timing Pattern Analysis.* Examine the timestamps in the governance record section of the substrate. A genuine governance deployment produces governance records distributed temporally across operational periods, reflecting governance decisions made in the course of operations. A theater deployment produces records clustered around audit windows, reflecting retroactive record creation.

**PASS CONDITION:** Named authorizers can explain governance reasoning coherently and specifically without consulting records; cell behavior matches DNA-specified behavior for selected inputs; governance record timestamps are distributed across operational periods rather than clustered around audit events.

**FAIL CONDITION:** Named authorizers cannot explain governance reasoning, express uncertainty about what they authorized, or attribute the decision to LLM recommendation; cell behavior does not match DNA specifications; record timestamps cluster around audit windows.

**REMEDIATION SIGNAL:** B3.22 Governance Theater. Cultural and process remediation is required alongside any technical remediation; structural fixes alone are insufficient because the anti-pattern is a governance culture failure, not a substrate configuration failure. The governance team must understand that CKS architecture requires genuine human decision-making at named governance events, not record creation that documents LLM outputs as human decisions.

---

## 4. Test 2 — Provenance Void Detection (B3.23)

**TEST QUESTION:** Is provenance infrastructure systematically present across all event categories in this deployment, or are there systematic category-level gaps where classes of events exist without substrate records?

**TEST MECHANISM:** Systematic provenance audit applying the A5.08 provenance-completeness test comprehensively across all event categories rather than within a single commitment.

*Lifecycle event categories:* Are birth records present for every currently active entity? For entities with multi-parent DNA, is a mating record present? For entities that are no longer active, is a death record present with the appropriate death type?

*Evolution event categories:* Are DNA modification records present for every version change in active cells' DNA layers? For instinct evolution events (LLM updates, infrastructure changes), are mutation event records present? For action-feedback evolution events, are both Stage 1 evidence review records and Stage 2 approval records present for any completed pipeline executions?

*Governance event categories:* Are authority exercise records present for every event that required explicit governance authorization? For any override events, are override records present with the overriding actor identified?

*Temporal distribution:* Are records across all categories distributed temporally in patterns consistent with operational creation, or do records in one or more categories appear in bursts suggesting batch retroactive creation?

**PASS CONDITION:** The A5.08 provenance-completeness test passes across all event categories; no systematic category-level gaps are present; record timestamps are distributed across operational periods.

**FAIL CONDITION:** One or more event categories have systematic gaps (classes of events for which records are consistently absent); records in one or more categories appear in creation-timestamp bursts inconsistent with operational creation; entities exist for which no birth record is present.

**REMEDIATION SIGNAL:** B3.23 Provenance Void. Determine the sub-form (infrastructure void — provenance tooling is absent; governance void — provenance requirements were not communicated; cultural void — governance actors do not create records as part of their practice) and establish provenance infrastructure for the missing categories. Note that retroactive record creation has limited defensive value: a record created months after the event it documents cannot support the accountability claims the architecture requires.

---

## 5. Test 3 — LLM Governance Conflation Detection (B3.25)

**TEST QUESTION:** Are governance decisions in this deployment genuinely human-made — humans determining what operational constraints the DNA layer carries and what actions the Stage 2 approval process authorizes — or are LLM outputs being treated as governance decisions, with human actors serving as approval stamps on LLM-determined outcomes?

**TEST MECHANISM:** Three governance substance investigations.

*(a) DNA Content Quality Analysis.* Review the DNA specifications in the substrate for active cells. Examine the language and structure of DNA content. LLM-generated governance is identifiable by its prose characteristics: it reads as guidance to an LLM rather than as operational constraint — it uses second-person advisory framing ("when faced with X, you should consider…"), hedged language ("generally prefer…"), or subjective heuristics ("use judgment to balance…") rather than concrete operational specifications that admit unambiguous interpretation. Genuine governance DNA reads as operational constraint: it specifies what inputs trigger what behaviors, what conditions require what escalations, and what constraints are absolute.

*(b) Stage 2 Approval Substance Review.* Review action-feedback Stage 2 approval records per the B2.75 governance commitment. For each approval record examined, determine whether the record contains human reasoning — what pattern the approving human identified, what they concluded about its governance implications, what change they authorized and why — or whether the record contains LLM assessment outputs with a human approval notation. Also examine the decision duration pattern: genuine human review of evidence patterns and their governance implications takes measurable time; approvals that complete in seconds consistently suggest the human is approving a pre-formed LLM conclusion rather than forming an independent judgment.

*(c) A5.09 Accountability Test for governance acts.* Apply the accountability test to a sample of governance decisions: "why was this governance decision made?" Genuine governance produces answers rooted in human reasoning about operational context, observed behavior, or strategic intent. LLM Governance Conflation produces answers that reference LLM assessment as the primary basis: "the LLM assessed the pattern as appropriate," "the model recommended the DNA change," "the system flagged this for approval."

**PASS CONDITION:** DNA specifications are concrete operational constraints in unambiguous language; Stage 2 approval records contain human reasoning with temporal patterns consistent with genuine review; A5.09 answers for governance decisions are grounded in human judgment about operational context.

**FAIL CONDITION:** DNA reads as LLM prompting material rather than operational constraint; Stage 2 approvals consistently complete in implausibly short durations or cite LLM assessments as primary reasoning; governance decisions cannot be explained without reference to LLM outputs.

**REMEDIATION SIGNAL:** B3.25 LLM Governance Conflation. Distinguish the legitimate from the illegitimate role of LLM outputs in governance: LLMs may draft DNA specifications, summarize evidence patterns, and surface candidate changes as substrate mediators — this is LLM labor under human governance. LLMs may not determine what the governance decision is — this is governance authority, which the CKS architecture locates exclusively with humans. Cultural remediation is required to reestablish this boundary in practice.

---

## 6. Test 4 — Specification Integrity Collapse Detection (B3.30)

**TEST QUESTION:** Is the deployment's DNA specification internally coherent — are the rules governing each cell's behavior consistent with each other and with the cell's actual behavioral scope — or have accumulated directed selection events, incremental modifications, and uncoordinated additions created specification contradictions that undermine the determinism contract?

**TEST MECHANISM:** Four-part coherence audit.

*(a) Contradiction Scan.* For each entity in the deployment, inspect the DNA behavior substrates per the B2.25 commitment. Identify rules that specify contradictory behavior for the same input type or condition: two rules that together require a cell to produce incompatible outputs for a given input. Check the A1.03 conflict registry: are detected DNA rule conflicts registered as first-class conflicts, or are they unregistered inconsistencies that the cell resolves silently?

*(b) Determinism Spot-Check.* Apply the A5.06 and A5.16 determinism tests to a sample of recently evolved cells — cells whose DNA has been modified within the most recent governance cycle. Nondeterministic behavior on equivalent inputs in recently evolved cells is a strong indicator of specification contradictions: the LLM is resolving contradictions at execution time by making ad-hoc choices, producing behavior that varies across executions.

*(c) DNA Volume Monitoring.* Compare the current volume of DNA specification content (number of rules, total specification size, rule density per input type) against the baseline specification at deployment initialization. DNA specification volume should grow proportionally with the operational scope of the cell. Disproportionate volume growth — specification size growing significantly faster than operational scope — signals specification bloat: rule accumulation without coherence review, the characteristic trajectory of Specification Integrity Collapse.

*(d) Governance Comprehension Test.* Ask the cell governance actor to state, without consulting substrate records, the complete set of DNA rules governing a specific input type for a cell within their governance scope. The ability to provide a coherent, complete, and accurate explanation is a proxy for specification complexity being within the bounds of human comprehension. Inability to provide such an explanation — or provision of an explanation that contradicts the actual specification — signals that the specification has grown beyond the governance actor's ability to govern it.

**PASS CONDITION:** No contradictory rules detected in the contradiction scan; A5.06 and A5.16 pass for recently evolved cells; DNA volume growth is proportionate to operational scope growth; governance actors can provide accurate explanations of rule sets governing specific input types.

**FAIL CONDITION:** Contradictory rules present in one or more cells' DNA layers; determinism test failures in recently evolved cells; DNA volume growth disproportionate to operational scope; governance actors cannot accurately characterize the rules they nominally govern.

**REMEDIATION SIGNAL:** B3.30 Specification Integrity Collapse. Determine the sub-form (contradiction accumulation — the collapse is in rule consistency; comprehension overflow — the collapse is in governance-to-specification ratio; bloat — the collapse is in volume without scope justification). Establish coherence review as a standing component of the directed selection governance process: DNA modifications should be reviewed not only for the change they introduce but for consistency with the existing specification.

---

## 7. Test 5 — Evidence Blindness Detection (B3.28)

**TEST QUESTION:** Is operational evidence in the Action layer — the recorded outputs of cell executions over time — being actively used to inform DNA evolution through the action-feedback evolution mechanism, or is the Action layer accumulating as an unused archive while governance decisions proceed without reference to it?

**TEST MECHANISM:** Three-part evidence utilization audit.

*(a) Action Layer Growth versus Proposing Substrate Activity Correlation.* Compare the rate of Action layer record accumulation against the rate of proposing substrate output generation. The action-feedback evolution mechanism requires that evidence in the Action layer flow through proposing substrates (B2.74) into candidate DNA modifications. A deployment in which the Action layer is growing — new cell execution records accumulating — while proposing substrate activity is absent or minimal is exhibiting Evidence Blindness: evidence exists but is not being processed into governance signals.

*(b) Pipeline Completeness Check.* For a deployment that has been operational for a governance cycle of sufficient duration, determine whether any action-feedback pipeline execution per the B2.76 commitment has ever completed from evidence identification through Stage 1 review and Stage 2 approval to an actual DNA modification. For a mature deployment with a functioning action-feedback evolution mechanism, at least one complete pipeline execution should be traceable in the substrate. The absence of any complete execution in a mature deployment is a strong diagnostic signal: either the proposing substrates are not configured, the Stage 1 review capacity does not exist, or the governance team does not engage with proposing substrate outputs.

*(c) Governance Awareness Test.* Ask governance team members — without advance notice — to identify two behavioral patterns visible in the Action layer that could plausibly inform DNA improvements. This test probes whether governance actors know that the Action layer contains this kind of evidence, whether they are capable of identifying it, and whether they are engaged with it as a governance resource. Inability to identify any such pattern, or unawareness that the Action layer is a governance resource at all, indicates evidence blindness at the governance culture level rather than merely the configuration level.

**PASS CONDITION:** Action layer growth correlates with proposing substrate activity at a ratio consistent with the deployment's evidence-to-signal filtering design; at least one complete action-feedback pipeline execution is traceable for mature deployments; governance team members are aware of and can engage with Action layer evidence.

**FAIL CONDITION:** Action layer growing without corresponding proposing substrate activity; no complete pipeline execution traceable in a deployment of sufficient maturity; governance team members are unaware of Action layer evidence potential or cannot identify behavioral patterns within it.

**REMEDIATION SIGNAL:** B3.28 Evidence Blindness. Determine the sub-form (configuration blindness — proposing substrates are absent or misconfigured; capacity blindness — Stage 1 review capacity does not exist for proposing substrate outputs; cultural blindness — governance team does not understand or engage with Action layer evidence). Configure proposing substrates per B2.74, establish Stage 1 governance review capacity for their outputs, and communicate to the governance team that the Action layer is a primary source of evidence for DNA evolution.

---

## 8. Composite result and relationship to commitment-specific tests

The five detection tests above form a cross-cutting anti-pattern detection suite. They are designed to be run as a complement to the commitment-specific B5 tests, not as a substitute for them. The relationship between the two test classes is not redundant coverage of the same properties — it is complementary coverage of different diagnostic dimensions.

The commitment-specific tests (B5.02–B5.07) answer: *are the structural components of the CKS architecture present and correctly formed?* They detect structural absence, structural malformation, and structural misconfiguration. A deployment that passes them has the right architectural components.

The anti-pattern detection tests in B5.09 answer: *are those structural components substantively functioning as governance?* They detect substantive absence: governance records without governance decisions behind them, DNA specifications without operational constraints in them, Action layers without governance engagement toward them. A deployment that passes both test classes has the right architectural components and is using them for their intended governance purpose.

The five anti-patterns also interact with each other in characteristic ways. Governance Theater (B3.22) and LLM Governance Conflation (B3.25) frequently co-occur: a deployment where LLM outputs are treated as governance decisions will produce governance records that look legitimate to structural inspection — it is performing governance theater. Provenance Void (B3.23) and Evidence Blindness (B3.28) frequently co-occur: a deployment that does not systematically record evolution events is unlikely to be using Action layer evidence for governance improvement. Specification Integrity Collapse (B3.30) may emerge from LLM Governance Conflation: when LLM outputs drive DNA modifications, coherence review is typically absent because the human actors who approved the modifications are not reviewing them for consistency with the existing specification.

This interaction pattern means that detection of any one of the five anti-patterns should increase the urgency of running the other four detection tests. The five tests together constitute a diagnostic cluster, and a deployment that fails one has an elevated probability of failing others.

---

## 9. Source and derivation

This note derives from "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), specifically from the governance architecture commitments in §8, the evolution mechanism architecture in §7, and the lifecycle governance architecture in §6. The five anti-patterns these tests target are formalized in B3.22 (Governance Theater), B3.23 (Provenance Void), B3.25 (LLM Governance Conflation), B3.28 (Evidence Blindness), and B3.30 (Specification Integrity Collapse). The test structure follows B5.01. Referenced tests A5.06, A5.08, A5.09, and A5.16 derive from the Phase A5 operational test series on the Paper 1 architecture.

**Self-citation:** This note is part of the CKS derivation note series. Related notes in the B5 series include B5.02 through B5.07 (commitment-specific operational tests) and B5.08 (instinct evolution governance test). The anti-pattern notes B3.22, B3.23, B3.25, B3.28, and B3.30 provide the foundational definitions on which these detection tests depend.
