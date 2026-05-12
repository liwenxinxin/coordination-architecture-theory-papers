# Action-Feedback vs. Directed Selection: Formalizing the Operational Distinction Between the Second and Third CKS Evolution Mechanisms

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The Coordination Knowledge Substrate (CKS) pattern commits to three evolution mechanisms operating in productive tension: instinct evolution (undirected mutation), directed selection (human-initiated deliberate DNA improvement), and action-feedback evolution (evidence-initiated two-stage-mediated DNA refinement). The second and third mechanisms both produce DNA changes, operate on the same DNA layer scope, apply at all three levels of the CKS architecture, and operate under human governance. This note formalizes the operational distinction between them: directed selection is human-initiated and uses direct governance; action-feedback is evidence-initiated and uses two-stage mediated governance. The note states the distinction precisely across four axes — trigger origin, governance shape, initiative type, and knowledge source — then formalizes the interface mechanism through which the two converge without collapsing: Stage 2 approval of an action-feedback proposal integrates the resulting DNA change using the same A2.04 rule-authoring machinery that directed selection uses. The distinction enables productive tension between genuinely different evolutionary pulls and produces clear audit trails traceable by mechanism origin. This is the seventy-seventh Phase B2 note and the fifth of six notes decomposing B1.15 multi-shaped human governance across evolution mechanisms.

---

## 1. Why the distinction needs to be formalized as a standalone derivation

Paper 2's core theory section "Three evolution mechanisms in productive tension" establishes that directed selection and action-feedback evolution are distinct mechanisms (§7.2). Paper 2's "Governance shapes across evolution mechanisms" specifies that they operate under different governance shapes (§8.2). Both commitments are foundational to B1.15, which this note sits within as the fifth of six decomposition notes.

The operational motivation for formalizing the distinction is straightforward: both mechanisms produce DNA changes, both operate under human governance, and both apply at every level of the three-level architecture per B2.65–B2.67. Without a precise statement of what separates them, a deployment reviewing its evolution history cannot reliably determine which governance records to inspect, whether a given DNA change originated from human deliberate intent or from accumulated operational evidence, or how the pathway from origin to integration differed. The distinction is load-bearing for governance traceability per A1.07.

The prior four B1.15 decomposition notes build the necessary context. B2.73 formalized the evidence-evaluation mechanism by which the action layer accumulates data for action-feedback proposals. B2.74 specified the proposing substrate that detects patterns and generates proposals from that evidence. B2.75 formalized the two-stage mediation structure through which humans govern both the proposing substrate and each specific proposal. B2.76 formalized the complete action-feedback proposal pathway from evidence accumulation through substrate detection through two-stage approval to DNA integration. B2.77 now formalizes the distinction between that pathway and directed selection's separate pathway — not to isolate the mechanisms from each other, but to name precisely where and how they differ, and where they converge.

The strategic prior-art posture is consistent with the B2.57–B2.76 chain: formalizing the distinction as a named standalone commitment places the architectural choice — two explicitly separated mechanisms with explicitly different governance shapes — in the public record before any party can claim novelty in the distinction or in the interface through which the mechanisms converge.

---

## 2. The architectural distinction precisely stated

Directed selection and action-feedback evolution differ across four axes. The shared properties are named first to establish that the distinction is not a division between governed and ungoverned, or between DNA-affecting and non-DNA-affecting.

**Shared properties.** Both mechanisms operate on the DNA layer per B2.67: their outputs are changes to stabilized orchestration and behavior substrates. Both produce DNA versions subject to A6.02 retroactivity per B2.69–B2.70. Both produce changes governed under A1.01: human authority over substrate content and orchestration rules holds for both. Both are traceable under A2.40 provenance per the six metadata requirements, and both produce pathway records subject to A1.07 retraceability. Both use A2.04 rule authoring as the integration mechanism at the point where a DNA change takes effect.

**Axis 1: Trigger origin.** Directed selection is human-initiated: a human governance decision to improve DNA initiates the process. Humans identify an improvement opportunity — through deliberate analysis, anticipatory design, or response to any information source — and author the change. The evolution event begins with human intent. Action-feedback evolution is evidence-initiated: the action layer accumulates operational records per B2.73, the proposing substrate per B2.74 detects patterns crossing a threshold, and that threshold crossing generates a proposal that then enters the two-stage mediation pathway per B2.75–B2.76. The evolution opportunity is surfaced by operational experience, not by prior human deliberate intention.

**Axis 2: Governance shape.** Directed selection uses direct governance: humans author DNA changes through A2.04 rule authoring directly, without a separate proposal-and-acceptance stage. The standard authority architecture from Paper 1 applies without modification. Action-feedback uses two-stage mediated governance per B2.59 and B2.75: Stage 1 has humans governing the proposing substrate (the rules under which proposals are generated, the thresholds that trigger them, the patterns that qualify), and Stage 2 has humans approving or rejecting specific proposals before any DNA change takes effect. The governance shape is co-determined with the mechanism shape — the two-stage structure is not an optional overlay but the architecture through which action-feedback evolution operates.

**Axis 3: Initiative type.** Directed selection is initiative-driven: a human proactively decides to improve DNA and executes that decision. The human brings the change to the system. Action-feedback is response-driven: operational patterns surface a proposal that the deployment then evaluates. The system brings a potential change to the human.

**Axis 4: Knowledge source.** Directed selection draws on human knowledge and judgment about what should improve: the change reflects what humans know about goals, design intent, best practices, and anticipated needs. Action-feedback draws on accumulated operational evidence of what has happened: the change reflects what the action layer recorded about actual usage, actual failure, actual inefficiency. Directed selection can draw on evidence — humans initiating directed selection may do so in response to information they have reviewed — but the use of evidence is optional and external to the mechanism's governance structure. Action-feedback's evidentiary grounding is architectural: the mechanism requires accumulated action-layer records as its input.

**The interface mechanism.** When Stage 2 per B2.75 approves an action-feedback proposal, the integration uses A2.04 rule authoring — the same mechanism that directed selection uses directly. At the integration point, the two mechanisms converge: a DNA change is authored through A2.04 regardless of whether the origination was human-initiated or evidence-initiated. This convergence does not collapse the distinction. The distinction is trigger origin and governance shape, not integration mechanics. A directed-selection event still begins with human intent and follows direct governance throughout; an action-feedback event still begins with evidence threshold and follows two-stage mediated governance up to integration. The A2.04 convergence means that the DNA layer's modification mechanics are uniform; it does not mean the pathways leading to that modification are equivalent.

---

## 3. What makes the distinction architecturally distinctive

Most AI system evolution operates through a single pipeline. When a model is updated, whether through deliberate design or through feedback from operational data, the update process runs through the same machinery — retraining, fine-tuning, or configuration change — regardless of whether a human decided to improve the system or whether operational data revealed a pattern worth addressing. The distinction between human deliberate intent and evidence-surfaced opportunity is not architecturally encoded; it is at best a documentation practice.

CKS makes the distinction architecturally explicit. Two separate mechanisms with different governance shapes produce the same kind of output — DNA changes — through different pathways. This is not a documentation convention; it is a commitment that the system's governance structure treats the two origins differently. The proposing substrate required by action-feedback does not exist in directed selection's pathway. The two-stage mediation structure required by action-feedback does not apply to directed selection. Conversely, the human deliberate intent required to initiate directed selection is not present in action-feedback's triggering condition.

The architectural explicitness is what enables productive tension per B2.57. Productive tension requires that the mechanisms genuinely pull in different directions — directed selection improving what humans currently understand should improve; action-feedback surfacing what operational experience reveals could improve regardless of prior human understanding. If the mechanisms share a single pipeline, the tension collapses: all improvement goes through the same process regardless of origin. Architecturally separated mechanisms with distinct governance shapes preserve the separateness that makes productive tension possible.

The distinction also produces audit trail clarity. When a deployment reviews its evolution history — whether for compliance, operational analysis, or architectural review — the mechanism origin of each DNA change determines which governance records are relevant. An event identified as directed selection must have records of human initiation: the deliberate governance decision to author a change, the authority under which that authoring was executed, the provenance per A2.40. An event identified as action-feedback must have records of the complete B2.76 pathway: action-layer accumulation records per B2.73, proposing-substrate detection records per B2.74, Stage 1 governance records per B2.75, Stage 2 approval records per B2.75, and pathway traceability per A1.07. The two record sets differ because the pathways differ. Clear mechanism origin is what makes the distinction operationally useful rather than merely conceptual.

---

## 4. Inherited Paper 1 commitments

Both mechanisms inherit the full set of Paper 1 commitments as they operate.

**A1.01 (human-governed: authority not labor)** holds for both mechanisms. Directed selection exercises the governance rights — to initiate DNA changes, to author them, to accept or reject outcomes — through direct human action under the authority architecture. Action-feedback exercises governance rights at two stages: at Stage 1, humans govern the proposing substrate and the rules under which proposals are generated; at Stage 2, humans approve or reject specific proposals before any DNA change takes effect. In both cases, governance is an authority architecture, not a review workflow. Neither mechanism requires per-element human review; both require human authority at structurally specified points.

**A2.04 (rule authoring)** is load-bearing at integration for both mechanisms. Directed selection uses A2.04 directly throughout. Action-feedback reaches A2.04 at the Stage 2 integration point. The convergence on A2.04 means that DNA changes — regardless of mechanism origin — are subject to the rule-authoring requirements that make substrate content authoritative and addressable.

**A6.02 (retroactivity)** applies to DNA versions produced by both mechanisms per B2.70. Prior cells governed under superseded DNA versions are covered retroactively when DNA changes take effect, following the retroactivity commitment the source paper carries forward from Paper 1 §6.

**A2.40 (provenance)** applies to DNA changes produced by both mechanisms. The six metadata requirements — including who authored the change, under what authority, at what time, with what rationale — apply regardless of mechanism origin. The mechanism origin is one dimension of the provenance record: it determines which of the remaining metadata fields are relevant (e.g., action-feedback events carry proposing-substrate records and Stage 2 approval records; directed-selection events carry initiation and authority records).

**A1.07 (path retraceability and the accountability vocabulary)** applies to both pathways. The complete pathway from origination to integration must be retraceable: for directed selection, from human initiation through authoring through integration; for action-feedback, from action-layer accumulation through proposing-substrate detection through two-stage approval through integration per B2.76. The retraceability requirement is the architectural basis for the audit trail clarity the distinction enables.

---

## 5. When to use each mechanism

The architectural distinction defines when each mechanism applies.

**Use directed selection when:** humans have specific improvement intent for the DNA layer; the improvement opportunity is not being surfaced by operational evidence (or the timing does not permit waiting for the action-feedback pathway); proactive architectural improvement is needed in advance of operational experience; or anticipatory design is appropriate — the Pattern 4 scenario from B2.71 where directed selection improves DNA ahead of problems rather than in response to them. Directed selection is also appropriate when humans want to initiate improvement in response to evidence they have gathered themselves, outside the action-feedback pathway.

**Use action-feedback when:** improvement opportunities are being discovered through operational patterns that were not anticipated in advance; humans do not know beforehand what to improve but the action layer is accumulating evidence of what is working and what is not; evidence-driven discovery is valuable relative to the cost of the two-stage mediation structure; or the deployment has configured proposing substrates to surface patterns from specific cell types per B2.73–B2.74.

**Use both, with Pattern 5 cross-mechanism interaction (per B2.71), when:** directed selection explicitly responds to action-feedback proposals that have completed Stage 2 approval. Pattern 5 in directed selection per B2.71 formalizes this cross-mechanism interaction: a directed-selection event is initiated in response to an approved action-feedback proposal. The interaction is not collapse — the proposal still required evidence initiation and two-stage mediation before reaching the directed-selection event that authors the integration. The cross-mechanism interaction preserves both pathways while enabling coordination between them.

Deployments may configure which cell types or aspect domains primarily use which mechanism. High-stakes domains where proactive human intent is preferable may rely predominantly on directed selection. Domains where operational patterns are the most reliable signal of needed improvement may rely more heavily on action-feedback. The architectural commitment is that both mechanisms are available and that both operate under their respective governance shapes; which mechanism predominates in a given deployment context is a deployment design decision per the governing orchestration substrate.

---

## 6. Operational implications

**Mechanism origin recognition in evolution review.** When a deployment reviews its evolution history — for compliance, operational analysis, or architectural governance — the first determination is mechanism origin: was this DNA change produced by directed selection or by action-feedback? The origin determines which governance records are relevant to inspect and which pathway to retrace.

**Governance record sets by mechanism.** For directed-selection events: inspect the human initiation record, the authoring authority, the A2.04 rule-authoring record, and the A2.40 provenance metadata. For action-feedback events: inspect the action-layer accumulation records per B2.73, the proposing-substrate detection records per B2.74, the Stage 1 governance records per B2.75, the Stage 2 approval records per B2.75, and the complete B2.76 pathway records through to integration. The two-stage structure of action-feedback governance means the record set is larger; the direct structure of directed-selection governance means the record set is more compact but requires unambiguous evidence of human initiation.

**Cross-mechanism Pattern 5 record structure.** When a DNA change results from Pattern 5 — directed selection responding to an action-feedback proposal — both record sets apply: the action-feedback pathway records through Stage 2 approval, and the directed-selection authoring records for the integration step. The compound pathway is retraceable end-to-end under A1.07.

**Cell-type mechanism configuration.** Deployments operating at scale may configure specific cell types or proposing substrates to emphasize one mechanism. A cell type operating in a domain with rich operational data may have proposing substrates configured to surface action-feedback proposals actively. A cell type operating in a domain where anticipatory design is critical may have governance that emphasizes directed selection. The architecture accommodates both within the same deployment because the mechanisms are separated and governed independently.

---

## 7. Limits of the distinction

**The distinction does not eliminate interaction.** Directed selection and action-feedback interact through Pattern 5 (B2.71) and through integration convergence on A2.04. The distinction is not a wall between mechanisms; it is a precise statement of where they differ. The interaction is architecturally explicit — named as Pattern 5 in directed selection's decomposition — rather than emergent or uncontrolled.

**The distinction does not establish one mechanism as superior.** Both mechanisms are necessary for productive tension per B2.57. Directed selection alone cannot surface what operational experience would reveal; action-feedback alone cannot execute proactive architectural improvement. The tension between initiative-driven improvement and response-driven refinement is the architectural value — both mechanisms are required to hold the tension.

**Stage 2 approval converts, not pre-converts.** An action-feedback proposal, even one that has passed Stage 1 governance, is not a directed-selection event until Stage 2 approves it and integration executes. The approval act is the conversion point. An unapproved proposal is not a DNA change; it is a substrate artifact representing a candidate change pending review.

**The distinction applies to directed selection and action-feedback, not to instinct evolution.** Instinct evolution is a separate mechanism — undirected mutation through LLM and infrastructure upgrades — that is distinct from both. The axis between directed selection and action-feedback (trigger origin and governance shape) does not apply to instinct evolution, which operates on the instinct layer through upstream upgrades under different governance machinery (verification substrates per B1.17). The three-mechanism structure per B1.09 is preserved; this note concerns the distinction between the second and third mechanisms only.

**The distinction is not supervised vs. unsupervised learning.** Both directed selection and action-feedback are fully governed. Neither operates autonomously. The distinction is pathway of initiation, not degree of human oversight. Characterizing action-feedback as "less governed" because it is evidence-initiated misreads the two-stage mediation structure: Stage 1 governs the proposing substrate itself, and Stage 2 requires explicit human approval before any DNA change takes effect.

**Humans can respond to evidence through directed selection without using the action-feedback pathway.** The distinction is not "humans vs. evidence": humans govern both mechanisms and may initiate directed selection in response to evidence they have gathered and evaluated outside the action-feedback pathway. A human who reviews operational data and decides to initiate a directed-selection event is not using action-feedback; the mechanism is determined by the pathway, not by whether evidence informed the human's decision. The action-feedback pathway requires evidence accumulation in the action layer, proposing-substrate detection, and two-stage mediation. Human-initiated directed selection in response to evidence bypasses that pathway and carries its own, more compact governance record structure.

---

## 8. One-sentence test

A DNA change in a CKS deployment is a directed-selection event if it originates from a human governance decision to improve DNA and proceeds through direct governance; it is an action-feedback event if it originates from action-layer evidence crossing a proposing-substrate threshold and proceeds through two-stage mediated governance — both converging on A2.04 rule authoring at integration.

---

## 9. Position in the B1.15 decomposition and significance

This note is the fifth of six notes decomposing B1.15, which formalizes multi-shaped human governance across evolution mechanisms. The decomposition proceeds as follows: B2.73 (action evidence evaluation mechanism), B2.74 (proposing substrate operational specification), B2.75 (two-stage human mediation specification), B2.76 (action-feedback proposal pathway), B2.77 (this note: action-feedback vs. directed selection distinction), and B2.78 (next: action-feedback verification, which will close the B1.15 decomposition). Subsequent Phase B2 notes will decompose B1.16 bidirectional evolution.

The significance of naming the distinction as a standalone derivation is threefold. First, it formalizes an architectural choice — two explicitly separated mechanisms with distinct governance shapes — that is not the default in AI system design and that requires deliberate commitment to maintain. Second, it names the interface mechanism (Stage 2 approval → A2.04 integration) through which the mechanisms converge, establishing that convergence at integration does not eliminate separation in governance shape or trigger origin. Third, it provides the operational vocabulary — mechanism origin, governance record sets by mechanism, Pattern 5 cross-mechanism record structure — that makes the distinction actionable in compliance, audit, and architectural review rather than merely theoretical.

Subsequent work that adopts the CKS pattern, composes it with adjacent architectural patterns, or argues against it should use the directed-selection vs. action-feedback distinction in the sense formalized here: trigger origin (human-initiated vs. evidence-initiated) and governance shape (direct vs. two-stage mediated), with A2.04 convergence at integration.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Action-Feedback vs. Directed Selection: Formalizing the Operational Distinction Between the Second and Third CKS Evolution Mechanisms.* May 12, 2026. ORCID: 0009-0004-8065-3235.
