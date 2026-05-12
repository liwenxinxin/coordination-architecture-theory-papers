# Silent DNA Drift: The Anti-Pattern That Arises When DNA Changes Based on Operational Evidence Bypass the Two-Stage Human Mediation of B1.15

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

B1.15 of the CKS architectural commitment series establishes multi-shaped human governance across all three evolution mechanisms — instinct evolution, DNA evolution, and action-feedback evolution. For action-feedback evolution specifically, the commitment specifies a two-stage governance structure: Stage 1 governs the proposing substrates that evaluate action evidence and generate DNA-change proposals; Stage 2 governs the approval of individual proposals before they integrate into DNA. This note formalizes **Silent DNA Drift** — the anti-pattern that arises when either or both stages are absent, allowing DNA to evolve based on operational evidence without governance oversight. The anti-pattern manifests in three recognizable forms: ungoverned proposing substrates (Stage 1 absent), auto-integrating proposals (Stage 2 absent), and evidence-driven autonomous modification (neither stage present). Silent DNA Drift is specifically the failure mode B1.15 was designed to prevent; the source paper (Li, April 2026, §8) states the requirement directly: action-feedback evolution must be "human-mediated rather than automatic, which prevents the action layer from silently drifting the DNA over time." The note identifies the emergence conditions that produce this anti-pattern, its operational consequences, the detection mechanism (B2.78 anti-silent-drift check) that catches it, and the per-form remediation pathway.

---

## 1. Why this anti-pattern requires a dedicated note

B1.15 names three distinct governance shapes — one per evolution mechanism. The governance shape for instinct evolution (verification substrates, routing rules, orchestration rules pinning high-stakes decisions to the reasoning layer) and the governance shape for DNA evolution (the standard authority architecture from Paper 1, with proposal, authorization, verification, and reversion roles explicitly allocated) are each recognizable as patterns with direct engineering analogs. A deployer who misconfigures either of those shapes will typically produce a visible failure: instinct without verification produces capability integration outside any governance record; DNA evolution without authority architecture produces substrate changes that cannot be traced to authorization events.

The governance shape for action-feedback evolution is architecturally distinct, and its failure mode is qualitatively different. The two stages are: (1) governing the proposing substrates — the substrate content that encodes evidence-evaluation logic, pattern-detection rules, and proposal-generation rules, authored through the governed rule-authoring process per A2.04; and (2) governing the proposal-acceptance decision — the human-held authority to review, approve, or reject each DNA-change proposal before it integrates. The failure mode for action-feedback is not loud and visible. DNA can silently evolve based on accumulated action evidence through an automated feedback loop, and the deployment will continue operating and improving, producing no immediate error signal. The drift is detectable only through an explicit audit of whether proposals were integrated through both governance stages.

This is the property that makes Silent DNA Drift merit its name and a dedicated note: the failure is operationally silent, the system continues to function and may appear to improve, and the violation of A1.01 human-governed authority at DNA scope accumulates invisibly. B2.78 formalizes the specific detection mechanism — the anti-silent-drift check — precisely because the failure does not announce itself.

---

## 2. Commitment violated: B1.15 action-feedback governance

B1.15 commits to multi-shaped human governance across all three evolution mechanisms. The action-feedback component of that commitment is the most precisely specified governance shape of the three, and the one whose violation is hardest to detect without an explicit audit mechanism.

The source paper states the commitment at §8: action-feedback evolution is governed "through humans governing the substrates that propose DNA changes from action evidence and approving the changes — making it human-mediated rather than automatic, which prevents the action layer from silently drifting the DNA over time." The framing is precise and load-bearing. "Human-mediated" is not a description of a single approval gate; it names a two-stage structure in which both the machinery that generates proposals (Stage 1) and the acceptance decision for each proposal (Stage 2) are under human governance. The phrase "silently drifting the DNA" names exactly the failure mode this commitment prevents.

The B2.73–B2.78 decomposition of B1.15's action-feedback component establishes the positive specification against which Silent DNA Drift is the negative:

- **B2.73** — Action evidence evaluation: the process by which accumulated action-layer content is evaluated for patterns indicating DNA-change opportunities.
- **B2.74** — Proposing substrate specification: the proposing substrate, as substrate content authored through A2.04 rule authoring, that encodes the evaluation logic and generates proposals. The proposing substrate is itself substrate content under the governance architecture, not arbitrary pattern-matching code outside it.
- **B2.75** — Two-stage human mediation: Stage 1 governs the proposing substrates (their specification is authored and authorized by humans); Stage 2 governs each individual proposal (a human holds authority over the acceptance decision before DNA changes integrate).
- **B2.76** — Action-feedback proposal pathway: the full five-step pathway from action evidence to DNA integration, at every step of which the governance record is required.
- **B2.78** — Action-feedback verification: the anti-silent-drift check, which audits whether any proposals were integrated without Stage 2 approval and whether proposing substrates carry Stage 1 governance records.

A deployment that violates any component of this two-stage structure instantiates Silent DNA Drift at the corresponding stage.

---

## 3. Recognizable form

Silent DNA Drift manifests in three distinct sub-forms, distinguished by which governance stage is absent and how completely the two-stage structure has been bypassed.

### Form 1 — Ungoverned Proposing Substrates (Stage 1 absent)

The deployment contains proposing substrates per B2.74 — substrate content intended to evaluate action evidence and generate DNA-change proposals — but those substrates were not authored through the A2.04 governed rule-authoring process. Their evaluation logic, pattern-detection rules, and proposal-generation criteria were set without Stage 1 governance oversight. Proposals emerge from whatever patterns the substrate happens to detect, not from evidence-evaluation criteria that humans have reviewed and authorized.

Recognition signals: proposing substrates exist in the deployment, but their content has no Stage 1 governance event records per B2.75. The proposing substrate configuration was generated — perhaps by LLM assistance or by automated tooling — without human governance of the substrate specification. Humans have not reviewed and authorized what patterns the proposing substrates are looking for or what change-proposal criteria they apply. Stage 1 governance records in the substrate's modification history are absent.

This form can be invisible in operation. Proposals are generated and reviewed at Stage 2; Stage 2 governance records exist for each approved proposal. An auditor examining Stage 2 records will find a functioning approval process. The gap is at Stage 1: the proposing substrates that generated those proposals were themselves not governed. The action-feedback loop is partially governed, but the part that determines what gets proposed — which is architecturally the part where deployment purposes are encoded — operates outside human authority.

### Form 2 — Auto-Integrating Proposals (Stage 2 absent)

Proposing substrates exist and may carry Stage 1 governance records, but proposals integrate directly into DNA without a Stage 2 human approval decision. DNA changes when operational patterns exceed configured thresholds, without a human reviewing each proposal and holding authority over the acceptance decision.

Recognition signals: proposals per B2.76 are generated and recorded. But examination of DNA modification records per B2.68 that originated from the action-feedback pathway reveals no Stage 2 approval records per A2.40. The B2.78 anti-silent-drift check fails — proposals were integrated without Stage 2. The deployment may have a proposal queue that is visible to humans, and humans may receive notifications of integrated changes, but the acceptance decision is not held by humans; it executes automatically when proposal-generation conditions are met.

This form is common in deployments that implement threshold-based automation: when a pattern is observed in a sufficient number of action records, a DNA change is automatically applied. The deployers may have reasoned that Stage 1 governance — having humans review the proposing substrate specification — is sufficient, and that per-proposal Stage 2 review is unnecessary overhead once the proposing substrate is trusted. The B1.15 commitment rejects this reasoning: the authority architecture requires humans to hold the acceptance decision for each proposal, not only for the machinery that generates proposals. DNA changes from action evidence that were not approved through Stage 2 are not human-governed DNA changes, regardless of whether the machinery that generated them was governed.

### Form 3 — Evidence-Driven Autonomous Modification (neither stage present)

The deployment is designed so that operational evidence modifies DNA directly through an automated feedback loop with no governance stage at any point. Neither proposing substrates as substrate content under B2.74 nor Stage 2 approval decisions exist. Action-feedback is implemented as automatic learning: accumulated operational evidence feeds directly into DNA changes through a system that operates outside the governance architecture.

Recognition signals: DNA-layer changes correlate with action-layer accumulation without any governance event records intervening. No proposing substrates exist as governed substrate content per B2.74. No Stage 2 approval records exist in the modification history. The deployment has, in effect, implemented online learning at the DNA layer — behavioral adaptation driven by operational evidence — without the governed loop that B1.15 requires.

This is the most severe form. Forms 1 and 2 are partial implementations of the two-stage structure: some governance machinery exists, but one stage is missing or ungoverned. Form 3 has made no architectural commitment to governed action-feedback at all. The loop may be technically sophisticated — with evidence aggregation, pattern analysis, and change generation operating at scale — while being entirely outside the governed substrate architecture. A deployment that implemented sophisticated ML-based DNA adaptation would be a canonical Form 3 instance.

---

## 4. Emergence conditions

Silent DNA Drift arises from three recognizable pressures that individually and in combination produce deployments that bypass one or both governance stages.

**The machine-learning analogy.** Architects and engineers with backgrounds in machine learning have internalized a design pattern in which systems improve through feedback loops without requiring human approval of each parameter update. Online learning, reinforcement learning, and adaptive systems all commit to this pattern: operational experience shapes system behavior without discrete human decisions intervening in the update process. When these architects design action-feedback evolution, the pattern transfer is natural — operational evidence should feed back into the system's behavior, and requiring human approval of each change seems architecturally inconsistent with how feedback loops work. The B1.15 commitment runs directly against this intuition. The commitment is that action-feedback in CKS is specifically not a machine-learning feedback loop; it is a governed loop in which the machinery that generates proposals and the acceptance of each proposal are both under human authority. The analogy to ML feedback loops is the most common source of Form 3 deployments.

**Governance overhead avoidance.** Once a deployment is operating at scale, the Stage 2 approval process — reviewing each proposal before DNA integration — can become a practical bottleneck. Proposing substrates generate proposals at a rate that reflects the volume of action evidence accumulated; at high volumes, per-proposal human review consumes governance attention that architects may determine is disproportionate to the risk. The pressure is to configure proposals to auto-integrate when they meet quality thresholds, reserving human review for edge cases or anomalies. This produces Form 2. The B1.15 commitment does not make an exception for high-volume deployments or high-confidence proposals. The acceptance authority is held by humans as an architectural requirement, not as a configuration option that can be disabled under efficiency conditions. Deployments that bypass Stage 2 to avoid review overhead have made a deployment optimization that violates an architectural commitment.

**Efficiency optimization.** More broadly, the action-feedback loop is valuable specifically because it enables behavioral improvement informed by lived operational experience. Deployments are under pressure to realize this value rapidly. Each governance stage adds latency between operational evidence accumulating and DNA changes integrating — Stage 1 adds the time required to govern proposing substrate specifications; Stage 2 adds the time required for human review of each proposal. The optimization pressure is to shorten this latency, ideally to zero. Form 1 deployments cut Stage 1 by generating proposing substrates without governance oversight. Form 2 deployments cut Stage 2 by automating proposal acceptance. Both cuts accelerate behavioral improvement while degrading governance integrity in ways that are invisible to operational monitoring.

---

## 5. Operational consequences

**Governance integrity violation.** DNA content modified through the action-feedback pathway without both governance stages is not human-governed DNA content in the A1.01 sense. A1.01 requires that humans hold the authority to inspect, modify, and override substrate content at any time — but authority requires that the content's origin and acceptance history be traceable through governed decisions. DNA changes with no Stage 2 approval record have no governed acceptance event in their history. The substrate is no longer authoritative per A1.08 for the full set of behaviors the deployment has drifted toward, because the authoritative-modification requirement of A1.08 is not satisfied for action-feedback-originated changes that bypassed Stage 2.

**Behavioral drift undetectable.** Without governance records at both stages, DNA changes from operational evidence are invisible to audit. Path retraceability per A1.07 breaks for action-feedback-originated modifications: the six-field provenance metadata that A1.07 requires includes the authority event under which a modification was made. For auto-integrated proposals, no authority event exists. DNA content that originated from operational patterns rather than governed decisions cannot be distinguished from governed DNA content without examining the modification records specifically for Stage 2 approval events. In large deployments with continuous action-feedback, the proportion of ungoverned DNA content can grow over time without any operational signal indicating that drift has occurred.

**Misaligned evolution.** Ungoverned proposing substrates (Form 1) encode evidence-evaluation logic that was not reviewed against deployment purposes. Whatever patterns the proposing substrate detects and converts into proposals reflects the logic it was designed with, not the logic humans would have specified had they governed Stage 1. The proposals generated from ungoverned proposing substrates may align with deployment purposes by coincidence, but they may also encode patterns that optimize for operational metrics that diverge from deployment intent. DNA that evolves through ungoverned proposals has followed a selection process that humans did not author.

**Compliance impossibility.** A deployment that cannot demonstrate that DNA changes were governed — because Stage 2 approval records are absent — cannot satisfy governance accountability requirements. Retroactive reconstruction of whether a given DNA change was appropriate is possible only if the proposal that produced it was reviewed against deployment purposes at the time of integration. Without Stage 2 records, the question of whether a DNA change was authorized is not merely difficult to answer; it has no governed answer in the record. The deployment cannot demonstrate compliance with the human-governed requirement at DNA scope regardless of how well it is performing operationally.

---

## 6. Detection

**B2.78 anti-silent-drift check (primary).** The anti-silent-drift check is the specific detection mechanism for this anti-pattern, and it is the primary audit to run whenever action-feedback evolution is in scope. The check asks: were any proposals integrated into DNA without Stage 2 approval? The detection procedure examines DNA modification records for all changes that originated from the action-feedback pathway (identifiable by their pathway record per B2.76), then cross-checks each against Stage 2 approval records per A2.40. Any action-feedback-originated DNA modification without a corresponding Stage 2 approval record is a Silent DNA Drift finding.

**B2.75 two-stage governance audit.** Are both stages configured and recorded as active governance structures in the deployment? The two-stage governance audit verifies not only that approval records exist for individual proposals, but that the governance structure at both stages is part of the deployment's architectural specification — that Stage 1 and Stage 2 are named, their authority holders are identified, and their records are maintained. A deployment with Stage 2 records for past proposals but no architectural commitment to the two-stage structure is not in compliance; it has produced Stage 2 records opportunistically rather than as governed process.

**B2.74 proposing substrate governance check.** Do proposing substrates carry Stage 1 governance records? The check examines each proposing substrate as substrate content and verifies that it was authored through A2.04 rule authoring with governance oversight — that the Stage 1 governance event (reviewing and authorizing the proposing substrate's specification) is recorded in the substrate's modification history. Proposing substrates that were generated without such records are Form 1 indicators.

**A2.40 modification records audit.** Do action-feedback-originated DNA modifications carry the full modification record required by A2.40? The A2.40 record requirement applies to all substrate modifications; for action-feedback-originated modifications specifically, the record must include the Stage 2 approval event. Modifications that carry pathway records indicating action-feedback origin but lack Stage 2 approval entries are Form 2 findings.

**Form 3 structural check.** Does the deployment have any proposing substrates as governed substrate content, or does it instead implement action-feedback as a feedback loop that operates outside the governed substrate architecture? A deployment with no proposing substrates at all — but with DNA that changes in correlation with action-layer accumulation — is a Form 3 deployment. This check is structural rather than record-based: it examines whether the action-feedback mechanism is architecturally integrated into the governed substrate pathway or is a parallel automated system operating outside it.

---

## 7. Remediation

Remediation is form-specific. The appropriate intervention depends on which stage is absent and how completely the two-stage structure has been bypassed.

**For Form 1 — Ungoverned proposing substrates:** Govern all proposing substrates through Stage 1 governance per B2.75. Each proposing substrate specification must be reviewed through A2.04 rule authoring: the evaluation logic, pattern-detection criteria, and proposal-generation rules must be reviewed, revised where necessary against deployment purposes, and authorized through a Stage 1 governance event with a record in the substrate's modification history. Proposals generated before Stage 1 governance was established must be treated as ungoverned proposals pending the Stage 2 audit described under Form 2 remediation. The Stage 1 governance process is not retroactive; prior proposals carry the ungoverned-proposing-substrate taint of their origin.

**For Form 2 — Auto-integrating proposals:** Disable automatic integration immediately. All proposal-integration mechanisms that execute without Stage 2 human review must be suspended. The proposal queue — including any proposals already generated and queued for integration — must be placed in pending status. A retroactive Stage 2 review of already-integrated action-feedback-originated DNA changes must be conducted: for each such change, a governance decision must be made to authorize it retroactively or revert it. DNA content for which retroactive authorization cannot be established should be reverted to the last governed state. The Stage 2 review process must be established as an ongoing architectural commitment — not a workflow optional layer over automated integration, but the integration gate itself.

**For Form 3 — Evidence-driven autonomous modification:** Disable the automatic learning loop entirely. The automated feedback mechanism that connects action-layer evidence to DNA changes must be suspended pending establishment of the governed action-feedback pathway. The governed pathway per B2.76 must be implemented with both stages: proposing substrates authored through Stage 1 governance, and proposal acceptance held at Stage 2 by human authority. DNA changes made by the automated loop must be audited as ungoverned modifications; those that cannot be retroactively authorized must be reverted. Form 3 remediation is the most extensive because it requires both establishing the two-stage structure from scratch and conducting a full retrospective audit of DNA content that originated outside any governance structure.

**Verification after remediation:** Run B2.78 anti-silent-drift check after remediation is complete. The check should return no findings: all action-feedback-originated DNA modifications in the record should carry Stage 2 approval events, and all proposing substrates should carry Stage 1 governance records. The check should then be scheduled as a regular operational audit for deployments in which action-feedback evolution is active. Because Silent DNA Drift is by definition silent, the anti-silent-drift check is not redundant in a correctly-governed deployment; it is the mechanism by which the deployment maintains and demonstrates that the two-stage structure is operating as committed.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Silent DNA Drift: The Anti-Pattern That Arises When DNA Changes Based on Operational Evidence Bypass the Two-Stage Human Mediation of B1.15.* May 12, 2026. ORCID: 0009-0004-8065-3235.
