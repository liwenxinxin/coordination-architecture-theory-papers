# Single-Mechanism Evolution: The Anti-Pattern That Arises When Deployments Rely on Only One Evolution Mechanism Rather Than Maintaining All Three in Productive Tension per B1.12

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

B1.12 commits CKS-governed AI Selves to evolution through three mechanisms operating in productive tension: instinct evolution (undirected mutation through LLM and infrastructure upgrades), DNA evolution (directed selection through human-governed orchestration substrate updates), and action-feedback evolution (the loop from recorded action experience back into governed DNA refinement). The productive tension among these three mechanisms, formalized in B2.57, is itself the architectural commitment — not merely the presence of each mechanism individually, but their simultaneous operation across architecturally separated layers under unified governance. Single-Mechanism Evolution is the anti-pattern that arises when a deployment configures and practices only one of the three mechanisms, or collapses two into absent status, leaving a single evolutionary dimension where B1.12 requires three in productive tension. The anti-pattern presents in three recognizable forms: Mutation-Only Evolution, in which LLM vendor updates are the sole source of behavioral change; Directed-Selection-Only Evolution, in which human-initiated DNA changes are the sole mechanism with neither mutation governance nor action-feedback pathways; and Action-Feedback-Absent Evolution, in which mutation governance and directed selection both operate but no proposing substrates per B2.74 are configured to close the loop from the action layer per B2.26 back into DNA. Each form loses a distinct evolutionary dimension, collapses productive tension, and introduces specific governance blind spots. Detection proceeds through the B2.60 three mechanisms verification check and a mechanism instrument audit. Remediation configures the missing mechanisms through directed selection per B1.14, with B2.60 verification confirming restoration.

---

## 1. The Commitment Violated

B1.12 establishes that a CKS-governed AI Self evolves through three mechanisms operating in productive tension: instinct evolution as undirected mutation, DNA evolution as directed selection, and action-feedback evolution as the closing-the-loop mechanism. The parent framing of Claim 4 in the source paper is clear that productive tension is not incidental to the three-mechanism architecture — it is the architecture's central evolutionary claim. Instinct evolution provides exploratory capacity that directed evolution cannot plan for. DNA evolution provides directionality and trajectory that undirected mutation cannot supply alone. Action-feedback evolution provides the empirical grounding that operational experience uniquely generates, feeding back from the action layer per B2.26 into governed DNA refinement through proposing substrates per B2.74. The three mechanisms compose because they operate on architecturally separated layers — Claim 1's instinct/reasoning separation, Claim 2's DNA/action distinction within every cell — and governance integrates them rather than arbitrates between them.

B2.57 formalizes the productive tension property: each mechanism contributes something the others cannot substitute. B2.60 establishes the verification instrument that confirms all three mechanisms are configured and active. B2.59 establishes cross-mechanism governance as the integration requirement that keeps the three mechanisms from operating as isolated islands even when all three are present.

Single-Mechanism Evolution violates B1.12 by collapsing this three-mechanism architecture to a single operational dimension. The violation is not the absence of a mechanism that was never intended; it is the absence of a mechanism that B1.12 commits to maintaining alongside the others. A deployment that configures only one mechanism has not achieved a simplified version of the B1.12 architecture; it has lost two evolutionary dimensions that the architecture requires for robustness, adaptability, and governance completeness.

---

## 2. Recognizable Form

Single-Mechanism Evolution presents in three distinguishable sub-forms, each collapsing to a different single mechanism as the sole evolutionary pathway.

### Form 1 — Mutation-Only Evolution

In Mutation-Only Evolution, the deployment's only source of behavioral change is LLM vendor updates. Instinct evolution per B1.13 is the sole active mechanism: the cells' behavior changes when the LLM changes and not otherwise. Directed selection per B1.14 is not practiced — no human governance process initiates DNA layer per B2.25 modifications in response to observed needs, accumulated inefficiencies, or governance-defined goals. No proposing substrates per B1.15 and B2.74 are configured to surface action-layer evidence as improvement proposals.

The recognition signals for Form 1 are specific. The DNA layer per B2.25 is rarely or never modified between LLM version transitions; examination of the substrate's authoring history shows long intervals with no directed selection events. No directed selection event records exist — there is no audit trail of human-authorized DNA changes made for governance-defined reasons. No proposing substrates per B2.74 are present in the architecture. B2.60 three mechanisms verification finds directed selection and action-feedback instruments absent. The deployment's improvement timeline tracks LLM vendor release cadences rather than governance decisions.

The characteristic failure mode of Form 1 is complete evolutionary passivity on the governance side. The humans responsible for the deployment are not participants in its evolution; they are consumers of whatever behavioral changes the LLM vendor's update cycle delivers. There is no mechanism by which governance-defined goals can be pursued through substrate content change, and no mechanism by which the operational experience accumulated in the action layer can improve how the cells perform their work.

### Form 2 — Directed-Selection-Only Evolution

In Directed-Selection-Only Evolution, human governance initiates DNA changes per B1.14 as the sole active evolutionary mechanism. Directed selection operates — the DNA layer per B2.25 is modified by human-authorized authoring events, selection criteria are substrate content, improvement decisions are governance-defined. But neither of the flanking mechanisms is present. Mutation governance instruments per B1.13 — verification gates per B2.06, routing and behavioral-testing regimes, LLM version pinning — are absent. LLM versions change without behavioral testing against existing DNA content, producing ungoverned instinct-layer transitions that may introduce behavioral discontinuities invisible to the governance process. No proposing substrates per B2.74 are configured; action-feedback as an evolutionary mechanism does not exist in the deployment.

The recognition signals for Form 2 differ from Form 1. DNA authoring events do appear in the substrate's history — directed selection is practiced and leaves a record. But B2.62 mutation detection is absent; there are no verification gates per B2.06 through which LLM version changes are managed. Examination of the deployment's infrastructure governance reveals that LLM version transitions are handled as platform events rather than evolutionary events requiring behavioral verification. No proposing substrates per B2.74 exist. All DNA changes are human-initiated without any evidence-informed proposals rising from operational experience.

The characteristic failure mode of Form 2 is a split between the evolutionary dimension humans can observe and the evolutionary dimension they cannot. Governance sees and controls what directed selection produces; governance is blind to what instinct-layer mutation introduces, and governance makes improvement decisions without the benefit of systematic evidence drawn from how the cells actually perform their work. Improvement quality is bounded by what humans can observe and reason about without operational evidence.

### Form 3 — Action-Feedback-Absent Evolution

In Action-Feedback-Absent Evolution, mutation governance and directed selection both operate — instinct evolution per B1.13 is managed through verification instruments, and DNA evolution per B1.14 is practiced through human-authorized authoring — but no proposing substrates per B2.74 are configured. The action layer per B2.26 accumulates records of what worked, what failed, what surprised, and what proved inefficient, but no mechanism examines those records to surface evidence-informed improvement proposals. The loop from operational experience back into governed DNA refinement per B2.60 is absent.

The recognition signals for Form 3 require closer examination than Forms 1 or 2. The deployment appears well-governed from the outside: verification gates per B2.06 are present, directed selection event records exist, LLM version transitions are managed. The absence is in the action-feedback pathway. The action layer per B2.26 accumulates records but no proposing substrates examine them. B2.60 three mechanisms verification finds action-feedback instruments absent. Directed selection decisions are made on the basis of human judgment, stakeholder input, and explicit governance goals, but never on the basis of systematically mined operational evidence. The substrate-change cycles per B2.75 do not include a Stage 2 review cadence that incorporates proposals derived from action-layer evidence.

The characteristic failure mode of Form 3 is that improvement decisions are made without access to what the cells' operational experience reveals. Governance may be deliberate and authoritative while remaining systematically uninformed about the specific inefficiencies, scope mismatches, and repeated failure patterns that only accumulated action-layer evidence can surface. The directed selection mechanism produces changes; those changes are governed; but the governance is operating without one of the three informational inputs the architecture requires.

---

## 3. Emergence Conditions

Three conditions explain why Single-Mechanism Evolution emerges in practice rather than remaining a hypothetical failure.

**Governance simplicity preference.** Configuring all three evolution mechanisms requires governance architecture investment at three distinct levels: mutation governance instruments including verification gates and behavioral testing regimes; directed selection governance including authority architecture, selection criteria as substrate content, and proposal-and-acceptance machinery; and action-feedback governance including proposing substrates, evidence-mining instruments, and Stage 2 review cadences. Each level is a non-trivial investment. Architects working under resource constraints or timeline pressure configure what they understand first and defer or omit what is unfamiliar. The result is a deployment with one well-configured mechanism and two absent ones. The absence is not intentional; it is the residue of scoped-down configuration.

**Vendor dependency assumption.** LLM vendors release improved models on a continuous basis, and the improvements are real: capability jumps, reasoning quality improvements, instruction-following refinements. Architects who treat LLM vendor updates as the primary source of AI system improvement — a reasonable assumption in the context of rapid model capability growth — may configure no additional evolutionary machinery because they do not perceive the need. The DNA layer per B2.25 exists but is treated as a one-time configuration artifact rather than as the substrate for ongoing directed selection. The action layer per B2.26 accumulates records that are never systematically examined. Mutation-Only Evolution emerges from this assumption without architects recognizing it as an architectural choice.

**Evidence mining unfamiliarity.** The action-feedback pathway — proposing substrates per B2.74 examining action-layer records and surfacing evidence-informed DNA change proposals — is the most conceptually novel of the three mechanisms. It has no precise analog in conventional software deployment practice. Verification gates and directed selection both have recognizable software-engineering neighbors (canary deployments, GitOps pull requests); proposing substrates and the action-feedback loop do not map cleanly onto familiar patterns. Architects default to what they know. Action-Feedback-Absent Evolution (Form 3) emerges specifically from this pattern: the two more familiar mechanisms are configured; the less familiar one is omitted.

---

## 4. Operational Consequences

**Evolutionary dimension loss.** Each missing mechanism loses a specific evolutionary dimension that the others cannot substitute for. Without mutation governance per B1.13, the instinct layer changes through upstream upgrades that the governance process neither shapes nor verifies, and the behavioral effects of LLM version transitions are invisible until they manifest in operations. Without directed selection per B1.14, no human-initiated improvement is possible; the only evolutionary pathway is what vendor update cycles happen to deliver. Without action-feedback per B1.15, operational experience never informs evolution; the Self cannot learn from its own operation in any governed sense. These are losses of architectural capability, not losses of operational convenience.

**Productive tension absent.** B2.57 establishes that the productive tension among the three mechanisms is the architecture's central evolutionary property. The mechanisms compose in a way that none individually achieves: instinct evolution's exploratory capacity is integrated through governance; directed selection's trajectory is grounded by action-layer evidence; action-feedback's empirical signal is processed into governed substrate change. Collapse to a single mechanism does not produce a simpler version of this architecture; it produces an architecture with no productive tension, because tension requires at least two mechanisms operating across the gap their architectural separation creates.

**Evolution brittle.** Single-mechanism evolution is brittle in a form-specific way. Mutation-Only deployments are entirely dependent on vendor update timing and content; an LLM vendor's decision to delay a release, change a model's behavior, or discontinue a version produces evolutionary stall or discontinuity with no governance response available. Directed-Selection-Only deployments produce improvement on the axes governance can see while accumulating ungoverned instinct-layer drift and undetected operational inefficiency. Action-Feedback-Absent deployments improve deliberately but systematically miss the improvement opportunities that only operational evidence reveals.

**Governance blind spots.** Without action-feedback, governance makes directed selection decisions without access to the empirical record of how cells perform their work. Patterns of repeated failure, recurring scope mismatches, and cumulative inefficiency that only action-layer evidence surfaces are invisible to the improvement process. Without mutation governance, governance is unaware of the behavioral changes that LLM version transitions introduce; the instinct layer changes beneath the governance process without verification, without behavioral testing, and without any record that the change occurred as an evolutionary event.

---

## 5. Detection

Two instruments detect Single-Mechanism Evolution.

**B2.60 three mechanisms verification.** This verification check asks whether all three mechanisms are configured and active: Is mutation governance present (verification gates per B2.06, LLM version management instruments, behavioral testing regimes)? Is directed selection practiced (recent DNA authoring events in the substrate's history, selection criteria present as substrate content, authority architecture for DNA changes)? Is action-feedback operative (proposing substrates per B2.74 configured, Stage 2 review cadences per B2.75 established, action-layer records being examined for evidence-informed proposals)? A deployment in which any of the three answers is no exhibits Single-Mechanism Evolution, and the pattern of absences identifies which form applies.

**Mechanism instrument audit.** The instrument audit examines whether the specific governance instruments each mechanism requires are present, not merely whether the mechanism is nominally intended. For mutation governance: are verification gates per B2.06 configured? Do they activate when LLM version transitions are deployed? Is there a record of behavioral testing conducted at recent LLM transitions? For directed selection: are DNA authoring events present in the substrate history? Do they reflect governance-defined goals rather than only initial configuration? Is there an authority architecture defining who proposes and who authorizes DNA changes? For action-feedback: are proposing substrates per B2.74 configured and pointed at action-layer records? Are Stage 2 governance review cadences per B2.75 established? Do improvement proposals in the governance record ever cite action-layer evidence as their source?

Detection is more reliable when both instruments are applied together. B2.60 verification can surface form at a coarse level; the mechanism instrument audit confirms whether the instruments nominally present are active in practice.

---

## 6. Remediation

Remediation configures the missing mechanisms. The remediation pathway is itself a directed selection event per B1.14 — the governance process decides which mechanisms to configure, authors the relevant substrate content and governance instruments, and authorizes the configuration as DNA change.

**For Mutation-Only deployments (Form 1).** Governance must establish directed selection practices: define selection criteria as substrate content, establish authority architecture for DNA authoring, and conduct an initial directed selection event that modifies the DNA layer per B2.25 in response to governance-defined goals. This first directed selection event produces both improvement and the governance record that evidences the mechanism's activation. Governance must also configure proposing substrates per B2.74 and establish a Stage 2 review cadence per B2.75 so that the action-layer evidence accumulated during Mutation-Only operation can be mined for its first evidence-informed proposals. B2.60 three mechanisms verification confirms restoration.

**For Directed-Selection-Only deployments (Form 2).** Governance must establish mutation governance instruments: configure verification gates per B2.06, define a behavioral testing regime for LLM version transitions, and establish a record-keeping practice for instinct-layer evolutionary events per B2.62–B2.66. The first LLM version transition after configuration provides an initial test of the mutation governance instruments. Governance must also configure proposing substrates per B2.74 and Stage 2 review cadences per B2.75. The challenge specific to Form 2 is that the deployment has likely accumulated unverified LLM version transitions whose behavioral effects are ungoverned; governance should conduct a retrospective audit of recent transitions as part of the remediation process. B2.60 three mechanisms verification confirms restoration.

**For Action-Feedback-Absent deployments (Form 3).** The remediation scope is narrower: mutation governance and directed selection are already operative. Governance must configure proposing substrates per B2.74 — defined as substrate-mediated instruments that examine action-layer records per B2.26 and surface evidence-informed DNA change proposals — and establish the Stage 2 governance review cadence per B2.75 through which those proposals enter the directed selection process. The first Stage 2 review session that incorporates action-layer-derived proposals constitutes activation of the action-feedback mechanism. B2.60 three mechanisms verification confirms restoration.

Across all three forms, B2.60 three mechanisms verification is run after configuration to confirm that all three mechanisms are present and active. Confirmation requires instrument presence plus demonstrated activation: at least one mutation governance event on record, at least one directed selection event on record, and at least one action-feedback-derived proposal surfaced or processed. Instrument configuration without activation record does not constitute restoration of productive tension.

---

## 7. Conclusion

Single-Mechanism Evolution is the failure mode that produces the architectural appearance of an evolutionary AI Self — mechanisms nominally understood, deployment running, cells operating — while eliminating two of the three evolutionary dimensions B1.12 requires. The pattern is consequential precisely because it is not obviously wrong. A deployment with only directed selection is a deployment where humans govern improvement; the failure is that improvement is systematically incomplete because the other two informational dimensions are absent. A deployment with only mutation is a deployment that receives LLM capability improvements; the failure is that no governed evolutionary process shapes or verifies what those improvements deliver. A deployment with mutation governance and directed selection but no action-feedback appears well-governed; the failure is that the improvement process is operating blind to the operational evidence that accumulates in the action layer every day the deployment runs.

B1.12's productive tension is not a design aspiration; it is an architectural commitment whose value comes from holding all three mechanisms simultaneously, not from any one alone. Restoring that tension through configured and verified activation of all three mechanisms is the specific remediation target that B2.60 three mechanisms verification is designed to confirm.

---

*CKS Derivation Note B3.13. Series B — Paper 2 derivation. Phase B3 — Anti-pattern formalizations. Commitment violated: B1.12 (three evolution mechanisms in productive tension). Related notes: B2.57 (productive tension as architectural property), B2.60 (three mechanisms verification), B2.59 (cross-mechanism governance), B1.13 (instinct evolution as undirected mutation), B1.14 (DNA evolution as directed selection), B1.15 (action-feedback evolution as the closing-the-loop mechanism), B2.25 (DNA layer), B2.26 (action layer), B2.74 (proposing substrates), B2.06 (verification gates), B2.62–B2.66 (mutation governance instruments), B2.75 (Stage 2 governance review cadence).*
