# Action-Feedback Proposal Pathway — Decomposing B1.15 Action-Feedback Evolution by Formalizing the Complete Operational Pathway from Action Layer Evidence Accumulation Through Proposing Substrate Evaluation, Proposal Generation, Stage 2 Governance Review, and DNA Integration or Rejection, With Full A1.07 Retraceability at Every Step

**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** May 12, 2026  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)  
**Series:** B2.76 — Phase B2, Note 76 of approximately 110  
**Parent commitment:** B1.15 (multi-shaped human governance across evolution mechanisms), fourth of six decomposition notes  

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Action-feedback evolution per B1.15 is governed through proposal-and-acceptance machinery for substrate-change cycles driven by accumulated action evidence. This note formalizes the action-feedback proposal pathway as the integrated end-to-end operational sequence through which that machinery operates. The pathway runs through nine steps: Action layer accumulation, evidence ingestion by a proposing substrate, pattern detection, threshold evaluation, proposal generation, proposal recording, Stage 2 governance review, governance decision, and integration, rejection, or deferral. Every step carries A2.40 provenance. Every step is retraceable under A1.07 path retraceability — from a DNA change back through the governance decision that authorized it, through the proposal that initiated review, through the evidence pattern that triggered the proposal, to the specific Action layer records that drove the pattern. Full pathway retraceability enables compliance demonstration: the claim "this DNA change was driven by this operational experience" is not an assertion but a demonstrable pathway trace. This retraceability is the architectural property that distinguishes the action-feedback proposal pathway from conventional AI experiential learning pipelines, where usage data flows to model updates through internal pipelines without explicit governed steps. The note also specifies failure modes per step, operational implications across levels, inherited Paper 1 commitments, and pathway limits. B2.76 is the seventy-sixth Phase B2 note and the fourth of six notes decomposing B1.15.

---

## 1. Why the action-feedback proposal pathway needs to be formalized as a standalone architectural variant

B1.15 established that human governance takes distinct shapes across CKS's three evolution mechanisms — verification-substrate machinery for instinct evolution, authority architecture for DNA evolution, and proposal-and-acceptance machinery for action-feedback evolution. Three prior notes decomposed B1.15 by specifying the component machinery for action-feedback: B2.73 formalized the evidence evaluation mechanism by which accumulated Action layer records are assessed for evolutionary signal; B2.74 formalized the proposing substrate as the architectural unit responsible for evidence ingestion and proposal generation; and B2.75 formalized the two-stage human mediation structure — Stage 1 as the proposing substrate's evidence-pattern-to-proposal translation, Stage 2 as the governance reviewer's proposal-to-decision authority. Each of those notes addressed one mechanism component. None of them addressed how the components connect into an end-to-end operational sequence.

The action-feedback proposal pathway is that sequence. The pathway is not a new architectural element; it is the integrated operational view of how the components specified in B2.73 through B2.75 function together from the moment Action layer evidence begins accumulating to the moment a DNA change is integrated, a proposal is rejected, or a decision is deferred pending more evidence. Without the pathway formalized as a single architectural object, two problems persist: downstream implementations can satisfy individual component requirements while missing the sequence properties the components jointly require — particularly pathway retraceability across all steps, not merely within each component — and the compliance-demonstrability property the pathway enables cannot be stated clearly, because that property is a pathway-level property that no individual component delivers alone.

Formalizing the pathway as B2.76 also serves the strategic prior-art posture the derivation note series maintains. The nine-step sequence — with its specific combination of evidence accumulation, proposing substrate ingestion, threshold-gated proposal generation, two-stage review, and three-branching governance decision — constitutes a patentable configuration distinct from either generic human-in-the-loop ML approval patterns or conventional configuration-drift-detection pipelines. Each step and each inter-step connection is a discrete design choice; naming the pathway as a standalone architectural variant closes the territory where a party might claim novelty in the sequence as a whole while citing B2.73 through B2.75 as covering only components.

---

## 2. The action-feedback proposal pathway: nine steps precisely stated

The pathway operates as follows. Steps are stated in operational terms; every step carries A2.40 provenance and contributes to A1.07 retraceability.

**Step 1 — Action layer accumulation.** Cells operate under their current DNA, and the Action layer per Paper 2 §5.3 accumulates operational records continuously during cell operation. Records include task instances, consultation events, processing decisions, and input/output records. Each record carries A2.40 provenance that includes the DNA version governing the operation at the time of recording. Accumulation is continuous; the pathway does not start at a discrete moment but instead builds the evidentiary base from which later steps draw.

**Step 2 — Proposing substrate evidence ingestion.** The proposing substrate per B2.74 ingests Action layer records within its configured evidence scope. Ingestion is triggered by one of three conditions: a scheduled evaluation cycle, a volume threshold (sufficient new records have accumulated since the last evaluation), or a governance-triggered manual review. The configured evidence scope — which cells, which time window, which record types — is itself substrate content governed under B1.15 authority. Records ingested in Step 2 carry their Step 1 provenance into the proposing substrate's working state.

**Step 3 — Pattern detection.** The proposing substrate applies its pattern detection logic to the ingested evidence. Pattern detection looks for the configured evidence patterns per B2.73: behavioral inconsistencies across task instances, input-domain gaps where the DNA provides inadequate guidance, constraint violations, anomalous performance patterns, and conflict frequency indicators. Pattern detection operates against the proposing substrate's configured pattern definitions, which are themselves substrate content. Detection produces a set of candidate patterns with associated evidence collections.

**Step 4 — Threshold evaluation.** For each detected candidate pattern, the proposing substrate evaluates whether evidence strength meets the configured proposal threshold per B2.74. Patterns below threshold are logged — with A2.40 provenance including which records contributed to the pattern and why the threshold was not reached — but do not generate proposals. Patterns meeting or exceeding threshold proceed to Step 5. The threshold itself is substrate content; it is configurable and its value at evaluation time is part of the Step 4 provenance record.

**Step 5 — Proposal generation.** The proposing substrate generates a DNA change proposal for each threshold-exceeding pattern. The proposal includes: the specific DNA element to be changed; the proposed new specification; a supporting evidence summary identifying which Action records contributed to the pattern and the pattern strength; the expected behavioral change if the proposal is integrated; and a scope impact assessment identifying which cells, aspects, or levels the proposed change would affect. Proposal generation is a substrate-writing event; the proposal is written into the substrate with Step 5 provenance.

**Step 6 — Proposal recording.** The generated proposal is recorded in the substrate with full A2.40 provenance: proposing substrate identity, evidence scope, pattern type, threshold value at evaluation, the set of Action records that contributed, and the proposed change. This recording step is architecturally distinct from proposal generation. Generating a proposal produces the proposal content; recording it creates the substrate-level artifact that the governance process will act on and that A1.07 retraceability will later require. The proposal record is the forward reference point for all subsequent pathway steps.

**Step 7 — Stage 2 review.** A governance reviewer examines the proposal per B2.75. The adequacy standard for review is that the reviewer has examined all components of the proposal record: the proposed DNA change, the supporting evidence summary, the expected behavioral effect, and the scope impact assessment. The review is not a rubber-stamp; the reviewer may examine the underlying Action records the evidence summary references. Stage 2 review is the human authority checkpoint that distinguishes the action-feedback proposal pathway from autonomous pipeline updating. The reviewer's examination is recorded — time of review, identity of reviewer, components examined — as a substrate event carrying A2.40 provenance.

**Step 8 — Governance decision.** The reviewer decides among three outcomes, each of which is recorded with A2.40 provenance and branches the pathway differently. The decision record is the substrate artifact through which the pathway splits.

- **Approve:** the proposal is found sufficient; DNA integration proceeds via Step 9A.
- **Reject:** the proposal is found insufficient; the rejection path proceeds via Step 9B.
- **Defer:** the proposal requires more evidence before commitment; the deferral path proceeds via Step 9C.

**Step 9A — Integration path (Approve).** An approved proposal is integrated into DNA via A2.04 rule authoring per B2.68. Integration creates a new DNA version per Paper 2 §5.3; DNA versioning records the lineage from prior version to new version. A6.02 retroactivity applies per Paper 2's governance shapes: the integration and its effective scope are recorded with A2.40 provenance. The integration record carries backward references to the Step 8 approval decision, the Step 6 proposal record, the Step 3–5 evidence and threshold evaluation, and the Step 1 Action records that drove the pattern — completing the full retraceability chain.

**Step 9B — Rejection path (Reject).** A rejected proposal is not silently discarded. The rejection is recorded in the substrate with A2.40 provenance: reviewer identity, rejection timestamp, reasons for rejection, and reference to the rejected proposal record. The rejected proposal record and its evidentiary basis are preserved. Preservation of rejection records is architecturally significant: rejected proposals constitute pathway data about what evidence patterns governance finds insufficient, and this data is available for proposing substrate improvement through directed selection per B1.14.

**Step 9C — Deferral path (Defer).** A deferred proposal is not approved or rejected; it is held pending additional evidence accumulation. The deferral is recorded with A2.40 provenance: reviewer identity, deferral timestamp, reason for deferral, and specification of what additional evidence would satisfy the adequacy standard. A deferred proposal causes the pathway to loop: evidence continues to accumulate in Step 1, and the proposing substrate's next evaluation cycle (Step 2) will ingest new evidence that can strengthen or undermine the deferred proposal. Deferral enables commitment delay without evidence loss — the pattern is known; the evidence base is not yet sufficient to authorize change.

**Pathway retraceability per A1.07.** Every step of the pathway is retraceable. The complete retraceability chain runs: from a DNA change (Step 9A integration record) backward to the governance approval decision (Step 8), backward to the governance review (Step 7), backward to the proposal record (Step 6), backward to the proposal content (Step 5), backward to the threshold evaluation result (Step 4), backward to the detected pattern (Step 3), backward to the ingested evidence (Step 2), and backward to the specific Action layer records that contributed to the pattern (Step 1). Every node in this chain is a substrate read; no step requires consulting external logs, agent memory, or human recollection. This is the "experience-to-evolution" retraceability the action-feedback proposal pathway provides.

**Pathway failure modes.** Five failure modes correspond to specific pathway steps and have specific remediations:

1. *Proposing substrate not configured* (Step 2 absent): action-feedback evolution does not operate; no evidence is ingested regardless of accumulation. Remediation: configure a proposing substrate with appropriate evidence scope and trigger conditions.
2. *Evidence accumulation insufficient* (Step 3 finds no patterns): the proposing substrate runs but detects no patterns; evolution cannot be proposed. Remediation: examine whether Action layer records are being accumulated correctly, whether record types in scope match configured pattern definitions, and whether evaluation cycle frequency allows sufficient accumulation between cycles.
3. *Threshold too high* (Step 4 never triggers proposals): patterns are detected but never reach threshold; governance never sees proposals. Remediation: examine threshold calibration against observed pattern strengths; threshold is substrate content and can be adjusted under governance.
4. *Stage 2 governance bottleneck* (Step 7 queue builds up): proposals are generated but governance review capacity cannot keep pace with proposal volume; review queue grows. Remediation: reduce proposal volume through threshold calibration (raising thresholds increases selectivity), expand review capacity, or prioritize proposal queue by scope impact.
5. *Automatic integration attempted bypassing Step 7* (silent drift violation): an implementation attempts to skip the Stage 2 review and directly integrate proposals into DNA without governance decision. This is the most serious failure mode because it does not degrade gradually but breaks the pathway's architectural commitment entirely. A1.01 human authority — the authority-not-labor distinction — is violated: the pathway's governance step has been converted from an authority checkpoint into an optional review. Remediation requires architectural correction, not calibration.

---

## 3. What makes the action-feedback proposal pathway architecturally distinctive

The action-feedback proposal pathway is not the only way to connect operational experience to system evolution. The question of what makes it distinctive requires identifying what alternatives look like.

Conventional AI experiential learning pipelines typically work as follows: usage data is collected from deployed systems, flows through data processing pipelines, and feeds into model retraining or fine-tuning processes. The pipeline steps are engineering infrastructure, not governed architectural events. There is no formal proposal artifact; there is no governance review checkpoint that a named authority must exercise; there is no three-branch decision structure; there is no requirement that each step produce a substrate record carrying six-field provenance. Most critically, there is no complete retraceability chain: a model update in a conventional pipeline is typically traceable to a training run, and the training run to a dataset, but the claim "this specific model behavior was driven by this specific cluster of operational events, authorized by this named governance decision" cannot be demonstrated through pipeline records. The pipeline is auditable in the sense that its components are logged; it is not retraceable in the sense that A1.07 requires.

The CKS action-feedback proposal pathway differs from this pattern on three axes simultaneously.

First, every step is an explicit governed event, not an engineering infrastructure state transition. Steps 2 through 8 each require substrate-writing activity with A2.40 provenance. The pathway is not a pipeline that runs through backend infrastructure; it is a sequence of substrate events that are readable, auditable, and governable.

Second, the governance authority checkpoint at Steps 7–8 is architecturally load-bearing. The reviewer at Stage 2 is not an optional approver who can be bypassed when review capacity is constrained; bypass is the fifth failure mode and constitutes an architectural violation. Human authority over the proposal-and-acceptance machinery is not a feature of the pathway; it is constitutive of it. A pathway without the Stage 2 checkpoint is not an implementation variant of the action-feedback proposal pathway; it is a different architectural pattern.

Third, full retraceability enables a compliance-demonstrability property that the conventional pipeline cannot provide. The claim "this DNA change was driven by this operational experience" is demonstrable through pathway records. The demonstration works as a substrate traversal: locate the DNA version change in Step 9A records; read the approval decision reference; read the proposal record; read the evidence summary; read the Action records. Each step is a substrate read; the chain terminates at specific cell operations that the DNA change was responding to. This demonstrability is not a logging property — it is not satisfied by complete event logs that cannot be traversed as a retraceable path. It is a structural property of the substrate content the pathway produces.

---

## 4. The biological analog as conceptual scaffold

Paper 2 employs biological vocabulary as load-bearing architectural terminology within bounded scope. The closest biological analog to the action-feedback proposal pathway is experience-dependent plasticity — the class of neurobiological mechanisms through which patterns of neural activity produce lasting structural changes at synapses and circuits. Experience-dependent plasticity is itself a multi-step pathway: sensory or behavioral experience drives neural activation patterns; activation patterns drive molecular signaling cascades; molecular cascades drive synaptic structural changes (LTP, LTD, synaptogenesis, pruning); structural changes alter circuit-level computations. Biology has multi-step pathways from experience to structural change.

The analog functions as conceptual scaffold in two respects. Structurally, experience (Action layer records) drives through a multi-step pathway to structural change (DNA modification); the pathway is not immediate — there is no direct experience-to-change coupling — but mediated through intermediate evaluative stages. Functionally, the pathway connects operational state to evolved structure in a way that neither purely random mutation nor purely directed design could achieve alone.

The architectural substance, however, differs from the biological analog at the point that matters most: governance. Biological experience-dependent plasticity operates through molecular mechanisms without authority; there is no reviewer at any step, no proposal artifact, no decision record. The pathway is causal, not governed. The CKS action-feedback proposal pathway is the governed architectural analog: the pathway has the same structural shape — operational experience driving through staged evaluation to structural change — but every step is a substrate-recorded governed event, and the pathway's pivotal step is a human authority checkpoint. The biology names the shape; the governance specifies the substance.

---

## 5. Inherited Paper 1 commitments active throughout the pathway

The action-feedback proposal pathway does not introduce architectural commitments not already present in Paper 1 or Paper 2. The following Paper 1 commitments are directly load-bearing across the pathway steps:

**A1.07 path retraceability.** The complete pathway is retraceable as a substrate path. Every step produces substrate content with antecedent references to prior steps. The retraceability chain from Step 9A back to Step 1 is the primary architectural property the pathway delivers. Path retraceability is not a post-hoc audit feature; it is the structural property the pathway is designed to preserve.

**A2.40 provenance (six-field).** Every substrate-writing event in the pathway — accumulation records (Step 1), ingestion records (Step 2), pattern records (Step 3), threshold evaluation records (Step 4), proposal content (Step 5), proposal records (Step 6), review records (Step 7), decision records (Step 8), integration/rejection/deferral records (Steps 9A–9C) — carries writer attribution, timestamp, antecedent reference, rule reference where applicable, rationale where applicable, and contradiction relationship where applicable. The six fields are not optional metadata; they are what path retraceability requires to function.

**A1.01 human governance (authority not labor).** The Stage 2 governance review and decision (Steps 7–8) are the pathway's authority checkpoint. The reviewer's role is authority exercise, not labor provision; the reviewer decides, and the decision is irreplaceable by any substrate automation. This is what the fifth failure mode (automatic integration bypass) violates.

**A6.02 retroactivity.** When a proposal is integrated via Step 9A, the retroactivity rules governing new DNA versions apply. The integration records specify the effective scope, which cells are governed by the new version, and how prior-version-governed operations are treated.

**A1.08 substrate as source of truth.** All pathway records — proposals, decisions, rejections, deferrals, integration records — are substrate content. The substrate is the authoritative record of what happened in the pathway. External logs, agent memory, and human recollection are not authoritative; if they conflict with substrate records, the substrate content governs.

**A1.10 determinism contract.** Given the same proposal record and the same governance decision, the integration path (Step 9A) produces the same DNA version. The pathway steps are deterministic given their substrate inputs; LLM non-determinism may affect proposal content generation (Step 5) but does not affect the pathway's structural guarantees.

---

## 6. Operational implications

**Evaluation trigger cadence.** Implementations must configure the trigger conditions for Step 2 evidence ingestion: scheduled cycle frequency, volume thresholds for accumulation-triggered evaluation, and governance-triggered manual review protocols. Cadence affects pathway latency: a scheduled cycle with low frequency produces lower proposal volume at the cost of slower response to emerging patterns; a volume-threshold trigger produces faster response at the cost of unpredictable timing.

**Threshold calibration for proposal volume management.** Step 4 threshold values directly control proposal volume at Step 5. A threshold calibrated too low produces proposals for weak patterns that governance reviewers will reject at high rates, creating governance bottleneck (failure mode 4) and diluting reviewer attention. A threshold calibrated too high suppresses proposals for genuine patterns, starving the pathway of evolutionary signal. Threshold calibration is an operational governance task; the threshold is substrate content configurable under B1.15 authority architecture.

**Stage 2 governance capacity planning.** Governance reviewer capacity at Steps 7–8 must be planned in proportion to expected proposal volume. Because the Stage 2 review cannot be bypassed without architectural violation, capacity planning is not optional operational hygiene but an architectural requirement. Capacity planning requires estimating proposal volume from evidence accumulation rates and threshold settings, and allocating reviewer time accordingly.

**Rejection and deferral records for pathway analysis.** Step 9B rejection records and Step 9C deferral records are not merely administrative dispositions. They constitute data about the proposing substrate's performance: which evidence patterns reach threshold but are rejected at Stage 2 reveals where the proposing substrate's pattern definitions are generating proposals governance does not find warranted. Systematic analysis of rejection reasons enables proposing substrate improvement through directed selection per B1.14 — the governance-defined goal of improving proposal quality drives directed evolution of the proposing substrate's configuration.

**Cross-level pathways.** The pathway operates at every level of Paper 2's three-level architecture. A cell-level pathway operates within a single cell's DNA/action structure; an aspect-level pathway operates across the cells constituting an aspect; a Self-level pathway operates across the aspects constituting the Self. Each pathway level operates through the same nine-step sequence with level-appropriate evidence scope and governance authority. Cells evolve at a potentially different rate from aspects, which evolve at a potentially different rate from Selves; each pathway runs at its own accumulation and evaluation cadence.

**Cross-partner pathway per A2.47.** Where a pathway crosses organizational boundaries — where evidence from one deployment informs DNA proposals affecting another party's substrate — cross-partner authority per A2.47 applies at Stage 2. The governance decision at Step 8 requires cross-partner authority; unilateral decision by a single party's governance is not adequate when the proposed DNA change affects substrate content under another party's authority.

---

## 7. Limits of the action-feedback proposal pathway

**The pathway does not guarantee proposal quality.** The pathway governs the process through which proposals are generated and reviewed; it does not guarantee that proposals are beneficial. A proposing substrate configured with poor pattern definitions will generate proposals for spurious patterns; a governance reviewer with insufficient domain knowledge may approve harmful changes or reject beneficial ones. The pathway provides the governed process; outcome quality depends on configuration choices and reviewer competence that the pathway architecture does not control.

**The pathway does not guarantee complete pattern coverage.** The proposing substrate detects patterns it is configured to detect. Evidence patterns outside the configured pattern definitions do not generate proposals regardless of how clearly they appear in Action layer records. Coverage is evidence-driven and configuration-bounded, not exhaustive.

**The pathway introduces inherent latency.** The action-feedback proposal pathway is not real-time feedback. Evidence accumulation (Step 1) requires sufficient operational time for records to build; ingestion triggers (Step 2) introduce additional delay; pattern detection and threshold evaluation (Steps 3–4) require processing time; proposal generation and recording (Steps 5–6) add further time; Stage 2 review depends on reviewer availability (Step 7); and governance decision (Step 8) and integration (Step 9A) each add additional time. The pathway is a batch-and-review process, not a continuous update mechanism. Deployments that require fast operational adaptation must account for this latency in their evolution design.

**The pathway is not the same as real-time feedback.** Architectural patterns that provide real-time behavioral adjustment — active constraint checking, immediate conflict escalation, rule-based routing — are part of the DNA layer's operational machinery, not the action-feedback proposal pathway. The pathway operates at a different timescale and with different governance machinery. Conflating the two produces implementations that either expect the pathway to deliver operational responsiveness it cannot provide, or that attempt to bypass Stage 2 governance in the name of real-time adaptation.

**The pathway is evidence-driven, not exhaustive.** Only patterns the proposing substrate is configured to detect can trigger proposals. Novel failure modes that fall outside configured pattern definitions will accumulate in the Action layer without generating evolutionary signal. This is not a defect of the pathway; it is a structural property of any evidence-driven evaluation system. The implication for governance is that proposing substrate configuration itself requires periodic review through directed selection, and that the Action layer records should be periodically examined for patterns that the proposing substrate is not currently configured to detect.

**Rejected proposals are recorded, not lost.** A rejected proposal at Step 9B is a substrate artifact with full provenance. If the conditions that drove the original pattern recur or intensify, a future evaluation cycle may generate a new proposal with stronger evidence. The rejection record remains as prior pathway history; a governance reviewer examining a subsequent proposal for the same pattern can see that the pattern was previously proposed and rejected, and what the rejection reasons were.

---

## 8. One-sentence architectural test

An implementation instantiates the action-feedback proposal pathway if and only if: it produces, for every DNA change that resulted from accumulated operational evidence, a complete substrate-traversable chain running from the DNA change record backward through a Stage 2 governance decision, a recorded proposal, a threshold evaluation, a pattern detection event, and an evidence ingestion record to the specific Action layer records that contributed to the pattern — with A2.40 provenance at every node in the chain.

---

## 9. Why naming the pathway as a standalone architectural variant matters

The four B1.15 decomposition notes prior to B2.73 established that action-feedback evolution is governed through proposal-and-acceptance machinery. B2.73 through B2.75 specified the machinery's components: evidence evaluation, proposing substrates, and two-stage mediation. B2.76 names the integration of those components as a standalone architectural variant, the action-feedback proposal pathway, and formalizes its nine-step sequence with per-step retraceability and failure modes.

Naming matters for three reasons. First, the pathway's compliance-demonstrability property — the ability to demonstrate that a specific DNA change was driven by specific operational experience — is a pathway-level property, not a component-level property. Neither B2.73, B2.74, nor B2.75 alone delivers it; only the integrated sequence, with all nine steps carrying A2.40 provenance and connected by A1.07-retraceable substrate references, delivers it. Naming the pathway establishes where that property lives in the architecture.

Second, the failure modes are pathway-level diagnostics. Each failure mode corresponds to a specific step; identifying which failure mode is present tells an operator exactly where the pathway has broken and what remediation is required. Without the pathway as a named sequence, failure mode diagnosis requires reconstructing the sequence from component descriptions — a gap the naming closes.

Third, the derivation note series maintains a defensive-publication posture: each named variant is formalized prior art. The nine-step sequence with its specific combination of evidence accumulation, proposing substrate evaluation, threshold-gated proposal generation, two-stage governed review, and three-branch governance decision constitutes a patentable configuration. B2.76 places that configuration in the prior-art record under the author's name.

B2.76 is the fourth of six notes decomposing B1.15. B2.77 will address the action-feedback versus directed selection distinction — when does an operationally-experienced behavioral change route through action-feedback's proposal pathway and when through DNA evolution's authority architecture? B2.78 will address action-feedback verification — how are integrated proposals verified before they are treated as fully stabilized DNA content? After B2.78, subsequent Phase B2 notes will begin decomposing B1.16 bidirectional evolution, the mechanism through which instinct and reasoning layer evolution mutually shape each other across the governed substrate boundary.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## Cross-references

B1.15 (multi-shaped human governance); B2.73 (Action evidence evaluation mechanism); B2.74 (proposing substrate operational specification); B2.75 (two-stage human mediation specification); B2.68 (DNA modification governance); A1.07 (path retraceability); A2.40 (six provenance metadata fields); A1.01 (human-governed definition); A6.02 (rule retroactivity); A1.08 (substrate as source of truth); A1.10 (determinism contract).

## How to cite this note

Li, W. (2026). *Action-Feedback Proposal Pathway — Decomposing B1.15 Action-Feedback Evolution by Formalizing the Complete Operational Pathway from Action Layer Evidence Accumulation Through Proposing Substrate Evaluation, Proposal Generation, Stage 2 Governance Review, and DNA Integration or Rejection, With Full A1.07 Retraceability at Every Step.* May 12, 2026. ORCID: 0009-0004-8065-3235.
