# Action Evidence Evaluation Mechanism: Decomposing B1.15 Action-Feedback Evolution by Formalizing How Proposing Substrates Examine Accumulated Action Layer Content to Identify DNA Improvement Opportunities

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the precise mechanism by which proposing substrates examine accumulated Action layer content to identify DNA improvement opportunities — the first step in the action-feedback evolution pathway established in B1.15 and the first of six notes decomposing that pathway.

## Abstract

Action-feedback evolution per B1.15 closes the loop from recorded operational experience back into governed DNA refinement. The loop does not begin with a proposal; it begins with evaluation — the examination of accumulated Action layer content for patterns that suggest DNA improvement opportunities. This note formalizes the Action evidence evaluation mechanism: the Action layer per B2.26 constitutes the evidence base; proposing substrates examine that base for five categories of evidence pattern; evaluation behavior is configured through substrate-resident orchestration rules per A2.04; threshold triggering calibrates the conversion of patterns into proposals; the evaluation configuration is Stage 1 of the two-stage governance architecture B1.15 establishes; LLMs per A1.12 may perform pattern-recognition operations as labor under human governance; and the mechanism applies recursively at every structural level per B1.20. The mechanism is architecturally distinctive because the evaluation is explicitly governed — what evidence is examined, what patterns are sought, and what thresholds trigger proposals are all authored rather than automatic — which prevents the action layer from silently drifting DNA content over time. Evidence patterns identified by evaluation are correlational rather than causal; they identify improvement candidates, but governance review determines whether any proposed change is appropriate.

---

## 1. Why the Action Evidence Evaluation Mechanism Requires Standalone Formalization

B1.15 establishes action-feedback evolution as the third of three evolution mechanisms in the CKS Self architecture — the mechanism that closes the loop from accumulated operational experience to governed DNA refinement. Paper 2's core theory specifies that action-feedback evolution is governed through humans governing the substrates that propose DNA changes from action evidence, with humans holding authority over the proposal-and-acceptance machinery and the orchestration rules under which proposals are constructed. That formulation names the endpoint (DNA changes proposed and accepted under human governance) and the overall character of the mechanism (human-mediated rather than automatic). What it does not yet decompose is how the pathway from accumulated experience to a proposal actually operates — specifically, how accumulated Action layer content is examined, what is looked for, and how examination results in a proposal request.

That decomposition is what the six-note B1.15 series provides. B2.73 opens the series by formalizing the Action evidence evaluation mechanism — the first step in the pathway, without which no proposal can be responsibly generated. The subsequent notes address: B2.74, the proposing substrate's operational specification; B2.75, the two-stage human mediation architecture; B2.76, the full action-feedback proposal pathway; B2.77, the distinction between action-feedback and directed selection; and B2.78, action-feedback verification. The six notes together provide complete architectural coverage of B1.15; B2.73 is logically prior to all of them because evaluation precedes proposal.

The strategic position of B2.73 in Phase B2 is also relevant. Following B2.67–B2.72, which completed the B1.14 directed-selection decomposition, B2.73 is the seventy-third note in Phase B2. It opens the final major mechanism decomposition before Phase B2 reaches the horizontal/vertical evolution and recursive-architecture notes. Formalizing evidence evaluation as a standalone prior-art claim establishes that the governed pattern-detection step — separate from both the proposing substrate's behavior and the human-mediation stages — is an independently identifiable architectural commitment.

---

## 2. The Architectural Mechanism Precisely Stated

### 2.1 The Evidence Base: Action Layer per B2.26

The Action layer per B2.26 accumulates operational history as the evidence base for action-feedback evolution. This accumulated content includes: recorded task instances (inputs received, outputs produced, processing paths taken); consultation events (interactions in which the cell sought or received external input); processing decisions (rule-application outcomes, conflict-resolution events, escalation events); substrate-write history (changes made to the cell's DNA or coordination content during operation); and input/output records more broadly. Over a cell's operational life, this content constitutes a structured record of how the cell has actually behaved across a range of situations.

The Action layer is authoritative substrate content per A1.08. Its records are substrate-resident, subject to the same governance architecture as all other substrate content, and carry provenance metadata per A2.40. This means the evidence base is not an ephemeral log maintained by the LLM or by runtime middleware; it is substrate-resident operational history available for governed examination.

### 2.2 Evidence Pattern Types

Proposing substrates examine the evidence base for patterns that suggest DNA improvement opportunities. Five categories of evidence pattern are architecturally relevant:

**Behavioral inconsistency patterns.** Cases where similar inputs produced materially different outputs across instances. Inconsistency of this kind may indicate that the DNA rules governing the cell's behavior are underspecified for this input category — they leave room for LLM behavioral variation that the DNA should be constraining more tightly — or that LLM behavioral drift has occurred. Either way, the pattern is a candidate for DNA rule refinement.

**Input-domain gap patterns.** Cases where inputs that fell outside the range the DNA rules were designed for produced unexpected, suboptimal, or inconsistent outputs. Gap patterns indicate that the DNA's coverage of the operational domain is incomplete; rules addressing the uncovered domain are improvement candidates.

**Constraint violation patterns.** Cases where cell behavior approached or exceeded configured behavioral constraints. Repeated approach-to-constraint events may indicate that the constraints themselves are set incorrectly for the actual operational conditions, or that the rules governing behavior near constraints need strengthening. These patterns are improvement candidates for constraint-governing DNA rules.

**Performance patterns.** Operational efficiency patterns — execution times, resource use, processing-path frequencies — that suggest DNA rule optimization opportunities. If particular processing paths are consistently slower or more resource-intensive than alternatives, DNA rules that steer cells toward more efficient paths are improvement candidates.

**Conflict frequency patterns.** High-frequency conflict events in specific input categories may indicate that the DNA's conflict-handling rules are inadequate for those categories — they trigger conflicts that better-specified rules would handle before escalation, or they fail to preserve conflicts that should be preserved. Conflict frequency patterns are improvement candidates for conflict-governance rules.

None of these five categories is novel in isolation: operational monitoring, anomaly detection, and feedback mechanisms exist across many architectures. What is architecturally distinctive is the governance of the evaluation process itself — formalized in §2.3.

### 2.3 Evaluation Configuration per A2.04

The proposing substrate's evaluation behavior is configured through substrate-resident orchestration rules authored per A2.04. This configuration specifies four things explicitly:

**What patterns to look for.** The evaluation is not open-ended pattern recognition over arbitrary features of Action layer content; it looks for the categories of pattern the configuration designates. The configuration identifies which of the five categories are in scope, what specific manifestations count as instances of each, and whether additional deployment-specific patterns warrant evaluation.

**What Action layer scope to examine.** The configuration specifies the evidence horizon: whether evaluation covers all Action records accumulated by the cell, a recency window, records associated with specific input categories, records from specific partner or aspect scopes, or some combination. Evidence scope is a design choice — narrower scope produces faster evaluation; broader scope surfaces patterns that recency-windowed evaluation would miss.

**What threshold triggers a proposal.** Patterns identified below threshold are recorded — the evaluation notes the observation — but do not generate a proposal. Patterns at or above threshold produce a proposal request, which then enters the two-stage mediation architecture per B2.75. Threshold specification is where the deployment calibrates the balance between governance overhead (higher thresholds produce fewer proposals, each requiring human-mediated review) and improvement opportunity (lower thresholds surface weaker patterns that may still warrant consideration).

**What change pattern to propose for a given evidence pattern.** The configuration does not simply flag a pattern and leave the nature of the proposal unspecified; it maps evidence pattern categories to change pattern categories. A behavioral inconsistency pattern maps to a candidate rule-tightening change; an input-domain gap maps to a candidate rule-addition change; a constraint violation pattern maps to a candidate constraint-specification change; and so on. The mapping is itself authored and governed, which means the proposing substrate is not free to generate arbitrary DNA change proposals — it generates proposals of the types the configuration authorizes for the patterns it has identified.

### 2.4 Stage 1 Governance and LLM Labor

Evidence evaluation configuration is substrate-resident authoritative content per A2.46. Humans author the configuration per A2.04 — they decide what patterns are sought, what scope is examined, what thresholds are set, and what change categories are authorized for which evidence categories. This is Stage 1 of the two-stage governance architecture B1.15 establishes: governing the proposing substrate's evaluation behavior. Stage 2 — the review and approval of specific proposals — is formalized in B2.75.

Stage 1 governance is what prevents the action layer from autonomously modifying DNA content. An ungoverned action-feedback loop would allow operational history to silently shape DNA rules without human authorization at any step. The CKS architecture prevents this by requiring that the evaluation mechanism itself be configured under human authority — before any proposal is generated, humans have authored what the evaluation looks for and what proposal types it can produce.

LLMs per A1.12 may perform the operational work of evidence evaluation: examining Action layer content, identifying instances of configured patterns, calculating pattern strength against configured thresholds, and assembling the pattern-summary input to the proposal generation step. Pattern recognition over large Action layer corpora is precisely the kind of high-dimensional processing for which LLMs are suited as labor. The governance architecture is maintained not by restricting what LLMs may process but by requiring that what they process, what they look for, and what they are authorized to produce be configured under human authority per A2.04.

### 2.5 Recursive Application per B1.20

Evidence evaluation applies at every structural level of the CKS Self architecture per B1.20's recursive inheritance commitment. At the cell level, evaluation examines cell Action records. At the aspect level, evaluation examines the operational records accumulated across the aspect's constituent cells and aspect-level coordination substrates. At the Self level, evaluation examines Self-level operational records spanning all aspects. Each level has a level-appropriate proposing substrate configured through level-appropriate evaluation rules. Evidence richness varies across levels — high-throughput operational cells accumulate denser Action records than recently-born cells — which is relevant to threshold calibration at each level.

---

## 3. What Makes the Action Evidence Evaluation Mechanism Architecturally Distinctive

The contrast class that makes the mechanism's distinctiveness visible is the automatic feedback loop common in conventional learning systems. In such systems, usage data updates model behavior through a continuous, ungoverned pathway: interaction logs feed training pipelines; preference signals update model weights; deployment telemetry automatically adjusts system behavior. The feedback is efficient — the system learns from experience without requiring human authorization at each update step — but the learning cannot be targeted, bounded, or authorized at the pattern-recognition layer. What the system learns is determined by what patterns are statistically dominant in the data, not by what patterns humans have authorized the system to act on.

CKS evidence evaluation operates differently across three dimensions.

**The evaluation is explicitly configured.** What evidence is examined, what patterns are sought, and what thresholds trigger proposals are all authored per A2.04 and are themselves substrate content. This means the evaluation cannot surface patterns outside its configuration scope. A cell whose evaluation configuration does not include performance patterns will not generate performance-motivated DNA proposals, regardless of what its Action layer records contain about operational efficiency. The configuration is the boundary of the evaluation.

**The evaluation produces candidates, not changes.** Evidence evaluation does not produce DNA changes. It produces pattern observations and, when thresholds are met, proposal requests. The proposal request enters the two-stage mediation architecture per B2.75 where humans authorize the change. The separation between evaluation and authorization is architecturally enforced — evaluation output is a pattern assessment, not a substrate write.

**The evaluation is governed, not just audited.** Post-hoc audit of automatic learning can identify what changed and when, but it cannot prevent changes from occurring before the audit. CKS evidence evaluation governance is pre-proposal: the evaluation configuration itself is authored, the evaluation behavior is governed, and the evaluation results in proposals only of the types the configuration authorizes. Governance shapes the process, not just the record of it.

Together, these three properties prevent the action layer from silently drifting DNA content — the architectural risk that Paper 2 specifically identifies as what human-mediated action-feedback governance prevents.

---

## 4. The Biological Analog as Conceptual Scaffold

The biological analog Paper 2 engages for action-feedback evolution is West-Eberhard's plasticity-first framing: phenotypes leading genotypes via environmental induction, with subsequent selection and genetic accommodation. The shape — operational state shaping what is later stabilized — is structurally parallel to CKS's action-feedback pathway: operational experience generating evidence that shapes what DNA content is proposed for stabilization.

Within that analog, evidence evaluation corresponds to environmental sensing for epigenetic regulation — the biological process by which organisms sense environmental conditions and the sensing influences which genes are expressed. Organisms do not evaluate environmental conditions against authored criteria and threshold specifications; the sensing is chemical, continuous, and non-deliberate. The analog is a conceptual scaffold, not an architectural claim.

CKS evidence evaluation is richer than the biological analog in the ways that matter for the architecture. First, it is structured: the evidence base is not raw chemical signal but substrate-resident records with provenance metadata per A2.40, making evaluation addressable and auditable in ways biological sensing is not. Second, it is configured: what patterns are sought and what thresholds apply are authored choices, not chemically determined constants. Third, it is governed: the evaluation configuration is itself substrate content under human authority, which means humans can modify what the evaluation looks for as their understanding of the operational domain deepens. The biological analog provides the intuition — experience feeds evolution through a sensing layer — but the architectural substance is governed pattern recognition over accumulated operational history.

---

## 5. Inherited Paper 1 Commitments

Action evidence evaluation inherits directly from six Paper 1 commitments.

**A2.46 (Category 4 authoritative content).** Evidence evaluation configuration is substrate-resident authoritative content. The configuration rules specifying what patterns to evaluate, what scope to examine, what thresholds to apply, and what change categories to authorize for which patterns are governed substrate content — they are subject to the same authority architecture as all other substrate content and may not be modified except under that authority.

**A2.04 (Rule authoring).** Evaluation configuration rules are orchestration rules authored per A2.04. Humans author the evaluation behavior of proposing substrates the same way they author the orchestration rules that govern cell-level behavior more broadly. LLM-drafted evaluation rules subject to human authority before they take effect are admissible; LLM-committed evaluation rules outside human authority are not.

**A1.12 (Labor allocation framework).** Pattern recognition over Action layer content is LLM-suitable labor. The labor allocation framework permits LLMs to perform evidence evaluation operations under human governance — examining records, identifying configured pattern instances, calculating threshold status — without LLMs holding authority over what is evaluated or what proposals are generated. The three-mode labor framework (direct human, LLM under rule, stable cell) applies to evidence evaluation as to other substrate operations.

**A2.40 (Six provenance metadata fields).** Evidence evaluation events are substrate operations that generate provenance records. When a proposing substrate conducts an evaluation cycle, the evaluation event — what scope was examined, what patterns were identified, what threshold assessments were made, when the evaluation occurred, under what configuration version it operated — is recorded with the six provenance metadata fields. This makes the evaluation pathway auditable from Action layer content through pattern assessment through proposal generation.

**A1.01 (Human-governed: authority, not labor).** The governance of evidence evaluation configuration is authority-not-labor governance in the A1.01 sense. Humans hold the right to inspect, modify, and override evaluation configuration at any time. This does not require humans to perform every evaluation operation; it requires that the evaluation be configured under human authority and remain subject to human override. The cost is not proportional to evaluation volume; it is proportional to configuration rule variety and override frequency.

**A1.08 (Substrate as source of truth).** The Action layer is authoritative as the evidence source — its records are substrate-resident state, not ephemeral runtime logs or LLM memory. Evidence evaluation operates on the substrate's authoritative operational history, not on LLM-reconstructed or middleware-held approximations of that history. This is what makes evaluation results traceable: they are derived from substrate-authoritative evidence under substrate-authoritative configuration.

---

## 6. Operational Implications

**Deployment-specific configuration.** Deployments configure evidence evaluation per cell type and operational requirements. A cell handling high-stakes decisions may have narrower pattern scope (fewer categories in evaluation) and higher thresholds (stronger evidence required before proposals are generated) to limit proposal volume and keep governance overhead manageable. A cell handling high-throughput routine operations may have broader scope and lower thresholds, because evidence richness and proposal volume are both sustainable at scale.

**High-throughput cells and evidence richness.** High-throughput operational cells accumulate Action layer content faster than lower-volume cells, enabling more frequent evaluation cycles and producing statistically denser evidence for pattern detection. Evidence richness is an operational variable that affects threshold calibration — thresholds appropriate for sparse evidence may be too restrictive for dense evidence, and vice versa.

**Evaluation configuration evolves through directed selection.** As operational understanding of evidence patterns deepens, the evaluation configuration rules that specify what to look for and how are themselves subject to refinement through B1.14's directed-selection mechanism. Evaluation configuration is DNA content; DNA evolution per B1.11 applies to it. Configuration refinement is the governed pathway through which the deployment improves the quality of its evidence evaluation over time.

**LLM pattern-surfacing.** LLMs performing evidence evaluation per A1.12 may surface patterns that human reviewers examining the same Action layer content would not readily identify — scale effects, subtle correlation patterns, cross-cell regularities. This is a productive feature of LLM labor in the evaluation context. The governance architecture is maintained by the fact that LLMs evaluate against configured patterns and produce pattern assessments, not against open-ended criteria and not directly producing proposals.

**Threshold calibration as governance design.** Threshold specification is not a technical tuning parameter; it is a governance design choice. Setting thresholds determines how frequently the action-feedback pathway will deliver proposals to human-mediated review. Deployments calibrate thresholds against the governance overhead they can sustain, the improvement opportunity density they expect from the Action layer, and the risk tolerance for missed improvement candidates. Miscalibrated thresholds — set too low — generate proposal volume that exceeds the governance capacity and degrades review quality. Set too high, they suppress improvement candidates that the governance process could beneficially address. Threshold calibration is a recurring governance responsibility.

**Cross-partner evidence evaluation.** Where Action layer content spans partner boundaries per A2.47, evidence evaluation that examines cross-partner evidence requires cross-partner authority. Evaluation configuration that draws on another partner's Action layer records is not a unilateral architectural decision of the proposing substrate's home governance; it requires the authority architecture that A2.47 specifies for cross-partner operations.

---

## 7. Limits

**Evaluation does not produce DNA changes.** Action evidence evaluation produces pattern assessments and, when thresholds are met, proposal requests. DNA changes require the full two-stage mediation architecture per B2.75, including human authorization. No evaluation output, however strong the pattern evidence, directly modifies DNA content. The separation is enforced: evaluation output is substrate-resident assessment content, not a substrate write to the DNA layer.

**Evaluation does not guarantee beneficial proposals.** A proposing substrate that has identified a strong pattern and generated a proposal request has not established that the proposed change is beneficial. Evidence evaluation is a pattern-detection mechanism operating under correlational evidence; it identifies cases where action evidence is consistent with a DNA improvement need. Whether the improvement need is real, whether the proposed change addresses it correctly, and whether the change's effects on other dimensions of cell behavior are acceptable — these are governance review determinations, not evaluation outputs. Stage 2 mediation per B2.75 is the mechanism that makes these determinations.

**Evidence patterns are correlational, not causal.** Behavioral inconsistency patterns do not establish that DNA rules are the cause of inconsistency; LLM behavioral variation, input distribution drift, or partner behavior changes are also consistent with the same pattern. Input-domain gap patterns do not establish that the gap is a DNA authoring error rather than an expected edge case handled correctly. The evaluation identifies patterns in operational history that are consistent with improvement opportunities; it does not diagnose root causes.

**Configuration coverage determines evaluation coverage.** Evidence evaluation identifies patterns within the scope its configuration specifies. Pattern categories not included in the configuration are not evaluated. Evidence scope not covered by the configuration is not examined. Gaps in evaluation configuration are gaps in the evaluation — they do not indicate that no improvement opportunity exists in the uncovered territory, only that the current configuration does not look there. Configuration completeness is a deployment responsibility.

**Evidence richness varies.** Recently-born cells with sparse Action records do not have the operational history to support reliable pattern detection. Threshold calibration that works well for mature high-throughput cells may be inappropriate for newer cells. Evaluation produces less reliable pattern assessments when evidence is sparse; deployments should configure evaluation scope and thresholds per cell maturity as well as per cell type.

---

## 8. Operational Test

A deployment instantiates the Action evidence evaluation mechanism in the CKS sense if and only if: (1) Action layer content per B2.26 constitutes the evidence base, available as substrate-resident operational history for governed examination; (2) proposing substrates examine that evidence base for one or more of the five configured pattern categories under authored evaluation configuration per A2.04; (3) evaluation configuration — what patterns are sought, what scope is examined, what thresholds apply, what change categories are authorized per pattern — is substrate-resident authoritative content per A2.46, subject to human authority at all times; (4) threshold triggering governs the conversion of pattern observations into proposal requests, with below-threshold patterns recorded but not proposed; (5) evaluation operations may be performed by LLMs per A1.12 as labor under the authored configuration; and (6) evaluation output is a pattern assessment and a proposal request — not a DNA layer write — so that human-mediated governance per B2.75 remains the authorization gate for any DNA change.

A system in which operational history automatically updates orchestration or behavioral content without governed evaluation configuration, without threshold-mediated proposal triggering, and without human-mediated authorization is not operating the Action evidence evaluation mechanism in the CKS sense. It may have useful adaptive properties; it does not have the governed-pattern-detection architecture this note formalizes.

---

## 9. Conclusion: Why Naming the Mechanism Matters and What the Decomposition Covers

Naming the Action evidence evaluation mechanism as a standalone architectural commitment establishes that the governed pattern-detection step is independently identifiable — distinct from the proposing substrate's operational specification (B2.74), from the two-stage mediation architecture (B2.75), from the full proposal pathway (B2.76), from the contrast with directed selection (B2.77), and from the verification machinery (B2.78). A party that claims novel invention over any of these subsequent steps without acknowledging the prior-art formalization of the evaluation mechanism that makes them possible has an incomplete prior-art search.

The six-note B1.15 decomposition this note opens proceeds through the full action-feedback pathway in architectural sequence: evaluation (B2.73) → proposing substrate specification (B2.74) → two-stage mediation (B2.75) → proposal pathway (B2.76) → action-feedback/directed-selection distinction (B2.77) → verification (B2.78). After B2.78, the B1.16 bidirectional evolution decomposition begins at B2.79.

The core architectural claim this note defends is that action-feedback evolution is not a passive or automatic consequence of operational activity. It is a governed pathway whose first step — evidence evaluation — is explicitly configured, threshold-mediated, and Stage 1 governed. Humans author what the evaluation looks for before any proposal reaches human-mediated review. This is what makes action-feedback evolution human-mediated rather than automatic, and what prevents operational history from silently drifting DNA content over time.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Action Evidence Evaluation Mechanism: Decomposing B1.15 Action-Feedback Evolution by Formalizing How Proposing Substrates Examine Accumulated Action Layer Content to Identify DNA Improvement Opportunities.* May 12, 2026. ORCID: 0009-0004-8065-3235.
