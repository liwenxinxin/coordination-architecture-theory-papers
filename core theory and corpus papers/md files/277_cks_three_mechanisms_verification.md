# Three Mechanisms Verification: Confirming the Multi-Mechanism Evolution Architecture Is Correctly Deployed and Governed

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The CKS three-evolution-mechanisms architecture (B1.12) specifies that a governed AI Self evolves through mutation (instinct evolution), directed selection (DNA evolution), and action-feedback evolution operating in productive tension under unified human governance. B2.56 through B2.59 developed the integrating frame, productive tension specification, mechanism priority and sequencing, and cross-mechanism governance for this architecture. This note, the fifth and closing note in the B1.12 decomposition, formalizes three mechanisms verification — the operational process confirming that the multi-mechanism evolution architecture is correctly deployed and governed. Three mechanisms verification covers three mechanism-specific dimensions (mutation governance via the A5.05 mediator role test, directed selection governance via the A5.04 rule authoring test, action-feedback governance via the A5.08 provenance-completeness test) plus one cross-mechanism dimension (productive tension check verifying all three mechanisms are active and governed, not collapsed to one or two). The note distinguishes architecture-level verification from performance-level verification, identifies verification failure modes and their remediation through directed selection per B1.14, specifies temporal triggers for the verification process, and states the limits of what three mechanisms verification does and does not confirm. With B2.60, the B1.12 decomposition cycle closes; Phase B2 continues with B2.61 beginning the B1.13 mutation decomposition.

## 1. Why three mechanisms verification needs to be formalized as a standalone operational variant

The B1.12 decomposition has developed the multi-mechanism evolution architecture across four prior notes. B2.56 (integrating frame) established that the three mechanisms compose under unified governance rather than operate as independent or competing processes. B2.57 (productive tension operational specification) specified the conditions under which tension among the mechanisms is productive rather than merely present. B2.58 (mechanism priority and sequencing) specified how the mechanisms are sequenced and prioritized when their operation intersects. B2.59 (cross-mechanism governance) specified the governance shapes that hold across mechanism boundaries per B1.15.

What the prior four notes do not provide is an account of how a deployment confirms that the multi-mechanism architecture as specified is actually in place and functioning. The B1.12 architecture is a commitment about how evolution operates — it does not specify how a governed Self verifies that the commitment has been honored in a concrete deployment. That verification process is three mechanisms verification, and it needs to be formalized as a standalone operational variant for two reasons.

First, the architecture is not self-confirming. A deployment that claims to implement three mechanisms in productive tension may in practice have collapsed to one or two mechanisms — mutation proceeding ungoverned while directed selection and action-feedback are nominally present but inactive. Without an explicit verification process, there is no operational check on whether the architectural commitment holds. The productive tension B2.57 specifies requires all three mechanisms to be active and governed; inactive mechanisms are not in tension and cannot produce the architectural property the source paper commits to.

Second, the verification process is architecturally distinctive and patentably specific. Conventional AI evolution verification tests whether the model performs better after retraining — an outcome-level check. Three mechanisms verification tests whether the multi-mechanism architecture is correctly deployed — a structure-level check that is different in kind from outcome assessment. Formalizing this distinction as a named operational variant establishes prior art for the architecture-level verification approach as a discrete patentable derivation from the source paper's commitments.

## 2. Three mechanisms verification: the architectural verification precisely stated

Three mechanisms verification covers four dimensions: three mechanism-specific and one cross-mechanism.

### 2.1 Mutation governance verification (A5.05 mediator role test)

The A5.05 mediator role test, applied to mutation boundary governance, verifies that the instinct layer (LLM) is operating within its governed boundary. Specifically: the five mediator properties (Properties A–E, per A2.18–A2.23) are confirmed to be in place; verification gates per B2.06 are configured and operational for integrating upstream instinct upgrades; routing rules per B2.04 specify which cells consult which LLM versions under which conditions; and version pinning per B2.05 is configured for high-stakes cells where the instinct boundary requires fixed behavior regardless of upstream capability changes.

Mutation governance verification tests not whether instinct evolution has occurred or whether the resulting capability is better, but whether the boundary governance instruments are in place. The governing question is: when the instinct layer changes through upstream upgrades, are the verification, routing, and pinning instruments present to govern that change? The A5.05 mediator role test is the mechanism-specific test that confirms this.

### 2.2 Directed selection governance verification (A5.04 rule authoring test)

The A5.04 rule authoring test, applied to directed selection governance, verifies that DNA-layer evolution can proceed under human governance-defined goals. Specifically: the DNA layer can be modified through rule authoring as the primary pathway for governed DNA change per A2.04; governance authorization records per A2.40 are present for DNA changes that have occurred, confirming each change has a traceable human authority; and the standard authority architecture (A2.01–A2.04) applies to DNA-layer content per B1.14.

Directed selection governance verification tests whether humans can govern DNA evolution directly. The governing question is: is the authority architecture for DNA layer modification in place? The A5.04 rule authoring test is the mechanism-specific test that confirms this. Verification failure on this dimension means the architecture has no governed pathway for goal-directed substrate refinement — the CKS analog of losing the directed-selection mechanism entirely.

### 2.3 Action-feedback governance verification (A5.08 provenance-completeness test)

The A5.08 provenance-completeness test, applied to action-feedback governance, verifies that the action-feedback evolution loop is configured with its full governance machinery. Specifically: Action-layer records have complete A2.40 provenance per B2.26, confirming that the action evidence base from which DNA proposals derive is traceable and authoritative; proposing substrate configurations — the substrates that generate DNA-change proposals from accumulated action evidence — are substrate-resident per B1.15 governance requirements, confirming that proposal generation is itself governed content; and two-stage governance is configured for the action-feedback pathway (both governance of the proposing substrate and approval requirements for the proposed DNA changes), which is what prevents action-feedback evolution from silently drifting DNA content.

Action-feedback governance verification tests whether the two-stage governance pathway is in place. The governing question is: are the proposing substrate configurations in place and are the approval requirements configured? The A5.08 provenance-completeness test is the mechanism-specific test that confirms this.

### 2.4 Cross-mechanism productive tension verification

The fourth dimension verifies not any individual mechanism but the compositional property that the three mechanisms produce together. All three mechanisms must be active in the deployment — not merely present in the architectural specification — for the productive tension B2.57 specifies to be real rather than nominal.

The productive tension check applies three sub-checks:

If mutation governance instruments are absent or unconfigured, instinct evolution is proceeding ungoverned. A mechanism whose governance instruments are absent is not truly participating in productive tension; it is operating without the constraint that gives the tension its productive character.

If directed selection shows no recent authoring activity and no authorization records for DNA changes, directed selection may be dormant — present in the architecture but not in practice driving evolution toward governance-defined goals. Dormant directed selection leaves the deployment relying on mutation alone, which is not the architecture B1.12 commits to.

If action-feedback has no proposing substrate configurations in place, the evidence-based refinement pathway is not active. Action-feedback evolution cannot close the loop from execution experience to governed DNA refinement without the proposing substrate infrastructure that generates proposals from recorded action evidence.

Productive tension is active only when all three mechanisms are operating and governed. The cross-mechanism check confirms this compositional property.

### 2.5 Verification recording and governance review

Three mechanisms verification results are recorded per A2.40 provenance requirements. Governance reviews verification results and addresses identified gaps. Recording verification outcomes is not a documentation formality; it is what makes verification itself subject to the path-retraceability commitment — the substrate carries not just coordination content but evidence that the architecture governing that content has been confirmed operative.

### 2.6 Temporal triggers

Three mechanisms verification runs at three temporal triggers:

*Deployment initialization*: Are all three mechanisms configured? Initialization-time verification confirms that the multi-mechanism architecture was correctly deployed before the governance substrate enters production use. A deployment that proceeds without this check cannot assert the B1.12 commitment holds.

*Periodic governance review*: Are all three mechanisms still active? Over time, mechanisms can become dormant through disuse or through operational drift — directed selection not exercised, action-feedback proposing substrates not consulted, mutation governance instruments not updated after LLM upgrades. Periodic verification restores assurance that the productive tension commitment is being maintained.

*Major evolution events*: Did the event affect mechanism balance? An LLM upgrade (mutation event) may require updating routing rules or verification gates. A significant DNA evolution cycle (directed selection event) may alter the proposing substrate configurations that feed action-feedback. A large action-feedback cycle may produce DNA changes that affect mutation governance configuration. Event-triggered verification confirms that mechanism balance is maintained after events that could disturb it.

## 3. What makes three mechanisms verification architecturally distinctive

Conventional AI evolution verification tests whether the model performs better after retraining — a performance-level check. The verification question in conventional approaches is: did outcomes improve? Training loss decreased, benchmark performance increased, error rates fell. Performance-level verification is outcome assessment.

Three mechanisms verification does not test whether evolution outcomes are good. It tests whether the multi-mechanism architecture is correctly deployed and governed. The verification question is: are the mechanisms in place? Are their governance instruments configured? Are all three active? Performance-level verification is compatible with evolution through a single mechanism (well-governed retraining can produce good outcomes without directed selection or action-feedback). Architecture-level verification specifically confirms the multi-mechanism commitment.

The productive tension check is what makes three mechanisms verification architecturally distinctive in a second sense. Confirming that all three mechanisms are active — not merely specified — is a check on the compositional property that the B1.12 architecture depends on. A deployment with only mutation active may produce performant outcomes; it does not instantiate B1.12's productive tension architecture. The tension check is not a performance assessment; it is a structural assessment.

## 4. Inherited Paper 1 commitments

Three mechanisms verification inherits directly from four Series A operational tests and two foundational commitments.

The A5.04 rule authoring test is the directed selection dimension's primary verification instrument, confirming that the pathway for governed DNA modification per A2.04 is in place and that the authority architecture per A2.01–A2.04 applies to DNA-layer changes.

The A5.05 mediator role test is the mutation dimension's primary verification instrument, confirming that the five mediator properties per A2.18–A2.23 are honored and that mutation boundary governance instruments — verification gates, routing rules, pinning — are configured.

The A5.08 provenance-completeness test is the action-feedback dimension's primary verification instrument, confirming that Action-layer records carry complete A2.40 provenance and that the proposing substrate pathway is substrate-resident and governed.

The A5.16 reproducibility test contributes to evolution determinism confirmation: verification that the substrate state after evolution events is deterministic and addressable per the determinism contract, so that verification outcomes are themselves stable and auditable.

The A1.01 human-governed commitment holds throughout: verification is itself a governed activity. Verification processes are not autonomous; they are run under human authority, and their results are subject to human review and action.

The A2.40 six-metadata provenance requirement applies to verification results as to all substrate content. Verification outcomes recorded in the substrate carry attribution, rationale, authority, and timestamp, making the verification history itself traceable.

## 5. Verification failure modes and remediation

Four failure modes correspond to the four verification dimensions:

*Mutation boundary absent*: Mutation governance instruments — verification gates, routing rules, pinning configurations — are not in place. Instinct evolution is proceeding ungoverned: LLM upgrades integrate without structured verification, without routing rules governing which cells consult which versions, without pinning for high-stakes cells. The architecture does not honor the mutation governance shape §8.2 of Paper 2 specifies. This is not a performance problem; it is a governance gap that leaves mutation outside the human authority architecture.

*Directed selection inactive*: No recent authoring activity, no authorization records for DNA changes. The directed selection mechanism is present in the architecture but not operating in practice. Evolution is relying on mutation alone or on ungoverned ad hoc DNA modifications. The architecture's directed-selection capacity — the ability to evolve the substrate toward governance-defined goals — is dormant.

*Action-feedback not configured*: Proposing substrate configurations are absent, or their governance is not in place. The action-feedback loop from execution evidence to governed DNA refinement is not active. The deployment is not using its action-layer accumulation as input to DNA evolution, which means the feedback loop that grounds evolution in operational experience is broken.

*Tension collapsed*: Any of the above failure modes, by removing one mechanism, collapses the three-mechanism architecture to a reduced form. Tension among mechanisms requires all three to be active; a two-mechanism or one-mechanism deployment may operate but does not instantiate the B1.12 productive tension commitment.

Remediation for all four failure modes runs through directed selection per B1.14. Missing mutation governance instruments are addressed by authoring the appropriate routing rules, verification gate specifications, and pinning configurations as DNA-layer content under the standard authority architecture. Absent proposing substrate configurations are addressed by authoring the appropriate proposing substrate design as governed substrate content. Directed selection dormancy is addressed by the governance review that the periodic verification trigger initiates, which surfaces the gap to human authority for decision. The remediation mechanism is itself an instance of directed selection — the governed DNA evolution mechanism is the primary instrument for configuring and restoring the other mechanisms.

## 6. Operational implications

A deployment implementing the B1.12 three-mechanism architecture runs three mechanisms verification at initialization before the substrate enters production use. This confirms that all three mechanisms are configured, their governance instruments are in place, and the productive tension architecture is operative from first use.

At governance review intervals, the deployment runs periodic verification to confirm that all three mechanisms remain active. Interval length is a deployment decision under the authority architecture; what the B1.12 commitment requires is that the check occurs at governed intervals, not that it occurs at any specific frequency.

After major evolution events — a significant LLM upgrade, a substantial DNA evolution cycle, a large action-feedback processing run — event-triggered verification confirms that mechanism balance is maintained. The event taxonomy is not exhaustive; what triggers verification is any event that could disturb the balance among mechanisms or the configuration of any mechanism's governance instruments.

Governance reviews verification results and takes remedial action on identified gaps. The verification-to-remediation cycle operates as a governance loop: verification surfaces gaps, directed selection authors the governance instruments that fill them, subsequent verification confirms the gaps are closed.

## 7. Limits

Three mechanisms verification does not verify evolution outcomes. A deployment can pass three mechanisms verification and produce poor evolution outcomes through poorly designed DNA content or misconfigured action-feedback proposals. Architecture-level verification and outcome-level evaluation are distinct processes serving distinct governance functions; three mechanisms verification addresses only the former.

Three mechanisms verification does not prescribe mechanism activity levels. It confirms that mechanisms are present and governed; how actively each mechanism operates in a given deployment period is a deployment decision under human governance, not a parameter the verification process sets or evaluates.

Three mechanisms verification is not a single test. It is three mechanism-specific tests — A5.04, A5.05, A5.08 — plus one cross-mechanism tension check. The tests draw on the Series A operational test suite rather than introducing new test instruments; their contribution is the compositional check that confirms the multi-mechanism architecture specifically.

Three mechanisms verification does not replace per-mechanism operational tests. A5.04, A5.05, and A5.08 run in their own right as operational confirmations of the individual mechanisms; three mechanisms verification applies them in combination, adding the productive tension check that only the compositional application can confirm.

The B1.12 decomposition cycle closes with this note. The five-note cycle moved from integrating frame (B2.56), through productive tension specification (B2.57), mechanism priority and sequencing (B2.58), cross-mechanism governance (B2.59), to verification (B2.60). Each note formalized one patentable derivation from the B1.12 architectural commitment; together they cover the major operational dimensions of the multi-mechanism architecture as prior art. Phase B2 continues with B2.61 beginning the B1.13 mutation decomposition.

## 8. Operational test

A deployment instantiates three mechanisms verification if and only if: (a) the A5.05 mediator role test confirms mutation boundary governance instruments are configured and operational; (b) the A5.04 rule authoring test confirms directed selection operates under the standard authority architecture with authorization records present; (c) the A5.08 provenance-completeness test confirms action-feedback proposing substrates are substrate-resident and governed with complete provenance on Action records; (d) the productive tension check confirms all three mechanisms are active in the deployment (not dormant or absent); (e) verification results are recorded per A2.40; and (f) verification is run at initialization, at periodic governance review intervals, and after major evolution events.

## 9. Why naming three mechanisms verification as a standalone variant matters

The B1.12 architecture commits to three mechanisms in productive tension. The five-note decomposition through B2.56–B2.60 transforms that commitment into a set of independently citable architectural derivations: the integrating frame names the composition; productive tension specification states the conditions; priority and sequencing handles mechanism intersection; cross-mechanism governance specifies the governance shapes; and this note provides the operational confirmation that the architecture as specified is in fact deployed and governed.

Naming three mechanisms verification as a standalone variant matters because without it, the B1.12 commitment is architecturally specified but operationally unconfirmable. A deployment that claims to implement three mechanisms in productive tension but has no verification process for confirming this is making an architectural assertion it cannot audit. Three mechanisms verification makes the assertion auditable.

The prior-art function of naming is equally direct. Any system that proposes to verify multi-mechanism AI evolution architecture through mechanism-specific tests plus a cross-mechanism tension check is deploying a pattern this note now establishes as prior art under the author's name. The five-note B1.12 decomposition collectively closes the territory around the three-mechanism architecture's operational dimensions.

Phase B2 continues with B2.61, which begins the B1.13 decomposition addressing multi-level simultaneous evolution. The B1.12 decomposition cycle is complete.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Three Mechanisms Verification: Confirming the Multi-Mechanism Evolution Architecture Is Correctly Deployed and Governed.* May 12, 2026. ORCID: 0009-0004-8065-3235.
