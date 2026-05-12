# Directed Selection Evolution Patterns — Decomposing B1.14 Directed Selection (DNA Evolution) Under Standard Authority Architecture by Formalizing Operational Patterns for Applying Directed Selection Including Incremental Improvement, Targeted Correction, Structural Redesign, and Anticipatory Design, with Governance Intensity Calibrated to Pattern Scope

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Directed selection — the CKS architecture's second evolution mechanism — operates through A2.04 rule authoring under the standard authority architecture from Paper 1. The mechanism is well-defined; what B2.67 through B2.70 have not yet addressed is the operational level at which humans apply directed selection in practice. Different evolutionary needs call for different approaches: adjusting a single rule differs operationally from redesigning an entire orchestration architecture, and both differ from applying directed selection in response to mutation novelty. This note formalizes five directed-selection evolution patterns — incremental improvement, targeted correction, structural redesign, anticipatory design, and response to productive tension — as operational guidance for how directed selection is applied within its established governance framework. The patterns are illustrative, not exhaustive; they represent the range of operational approaches deployments use to apply directed selection, each with distinct scope characteristics, governance intensity implications, and retroactivity profiles. All five patterns operate under the same underlying governance: A1.01 human-governed authority, A2.04 rule authoring as the implementation mechanism, A6.02 retroactivity treatment for all DNA changes, A2.40 provenance for all pattern events. Pattern selection is deployment judgment, not architectural prescription.

---

## 1. Why directed-selection-evolution-patterns requires standalone formalization

The prior four notes in this B1.14 decomposition have established the governance infrastructure for directed selection: B2.67 defined the scope of directed selection activity, B2.68 formalized the DNA modification governance framework, B2.69 established the version management commitment that applies to all DNA changes, and B2.70 specified the retroactivity treatment that applies when DNA changes propagate through the cell population. Together these four notes answer the questions of *what* directed selection modifies, *how* modifications are governed, *how* versions are tracked, and *what* happens retroactively when DNA changes.

What they do not answer is the question of *how* directed selection is applied operationally — the practical approaches humans use when exercising the mechanism. This operational gap is the subject of the present note.

The gap matters for two reasons. First, a deployment governance team that knows the governance framework but lacks operational pattern vocabulary is forced to re-invent pattern distinctions from scratch, independently, in each deployment. The pattern vocabulary this note provides makes those distinctions portable. Second, different patterns have materially different governance intensity implications — applying the same review intensity to a single-rule adjustment as to an architectural overhaul wastes governance capacity and can make the lightweight patterns impractical. Governance intensity calibration, which this note formalizes, is therefore not an aesthetic choice; it is what makes the mechanism usable across the full range of operational needs.

The strategic prior-art position of this note is the seventy-first in Phase B2 of Series B. A party seeking to claim novel invention in the domain of operational pattern diversity for AI substrate evolution must reckon with this note's publication date and the specific operational patterns it articulates. The note covers the distinctive combination of pattern multiplicity, governance intensity calibration per pattern, and cross-mechanism interaction through Pattern 5, within the CKS directed selection framework.

---

## 2. The five operational patterns

The five patterns presented here are characterized along four dimensions: scope (how many DNA rules are affected), governance intensity (how much governance process the event requires), retroactivity profile (what B2.70 treatment applies), and primary use case (the operational context in which the pattern is typically chosen). All five patterns operate through A2.04 rule authoring and remain within the B2.67 scope framework. None of them is an architectural requirement; each is operational guidance.

### Pattern 1 — Incremental Improvement

Incremental improvement involves making targeted small changes to one or a small number of specific DNA rules without restructuring the broader DNA architecture. The scope is deliberately limited: the governing humans identify a specific rule, assess its current behavior against the desired behavior, and author a modification that closes the gap.

Scope characteristics: one to a few rules; no architectural restructuring; no change to orchestration topology. Governance intensity: lighter governance is appropriate because the behavioral consequence is bounded; targeted review covering the specific rule and its immediate dependencies suffices; comprehensive review of the full DNA set is not warranted. Retroactivity profile: small behavioral change means the B2.70 retroactivity determination is typically low-impact, though existing cells whose behavior is governed by the modified rule still undergo the standard A6.02 determination. Primary use case: routine operational improvement where behavior is slightly off in specific input conditions and a targeted rule adjustment corrects it.

Incremental improvement is the pattern for operational fine-tuning. It is designed to be applied frequently, with governance intensity proportional to its limited scope. The governance framework does not change; only the scope of review is calibrated to the event.

### Pattern 2 — Targeted Correction

Targeted correction addresses a specific identified behavioral deficiency through DNA modification. Unlike incremental improvement, which is opportunistic optimization, targeted correction is deficiency-driven: some specific problem has been identified, and the pattern is the governed response to that problem.

Scope characteristics: scope is determined by the extent of the deficiency, not pre-bounded to a small number of rules; deficiencies that span multiple rules require proportionally larger correction scope. Governance intensity: moderate, calibrated to the severity of the deficiency; a deficiency that surfaced in safety-critical operation requires more intensive governance review than a deficiency in low-stakes operation; high-stakes cells per B2.05 may escalate governance intensity for any targeted correction that touches their operation. Retroactivity profile: the B2.70 retroactivity determination examines the scope of the corrected deficiency — a deficiency that affected many cells may produce non-trivial retroactivity determination. Primary use case: post-mutation verification per B2.65 reveals specific behavioral concerns; targeted correction addresses those concerns through directed selection.

Targeted correction illustrates the productive tension connection established in B2.57: mutation (instinct evolution through LLM upgrade) may introduce behavioral changes that do not pass pinning verification; targeted correction is the directed selection mechanism by which governance responds. The pattern formalizes this cross-mechanism dynamic without requiring it — targeted correction may arise from any identified deficiency, not only from post-mutation verification results.

### Pattern 3 — Structural Redesign

Structural redesign modifies the DNA architecture substantially — reorganizing orchestration rule structure, redesigning coordination rule topology, changing integration architecture across substrates, or otherwise altering how the DNA layer is organized rather than merely what specific rules contain.

Scope characteristics: broad; many rules may change, be reorganized, or be deprecated; the DNA architecture as a whole is under review. Governance intensity: highest of the five patterns; structural redesign affects many behaviors simultaneously and requires comprehensive governance review before any changes are deployed; the standard authority architecture from Paper 1 §3.3 operates at full intensity; retroactivity determination per B2.70 covers the full scope of changed rules; version management per B2.69 creates a major version event. Retroactivity profile: significant; many rules changing at once means many cells may be affected; the B2.70 determination must be comprehensive and is itself a governance event. Primary use case: deployment discovers a fundamental architectural inadequacy that cannot be addressed through targeted fixes — an orchestration design that systematically produces coordination failures, a rule topology that cannot accommodate required scale, an integration architecture that prevents necessary evolution.

Structural redesign is the pattern for when directed selection must operate at the architecture level rather than the rule level. Because its governance intensity is highest, it is also the pattern that most clearly illustrates why governance intensity calibration matters: applying structural-redesign-level governance to an incremental improvement event would make routine fine-tuning prohibitively expensive; applying incremental-improvement-level governance to a structural redesign event would leave major architectural decisions under-reviewed.

### Pattern 4 — Anticipatory Design

Anticipatory design is the proactively future-oriented pattern: humans govern the operational trajectory of the deployment, anticipate future requirements, and author DNA changes that position the deployment for those requirements before the requirements activate.

Scope characteristics: variable, determined by the anticipated future state; anticipatory changes may be incremental or structural depending on how much evolution is required to reach the anticipated state. Governance intensity: moderate, with the distinctive feature that governance review includes trajectory analysis — the governing humans must assess not just whether the DNA changes are sound in isolation, but whether the anticipated future requirements justify the changes now; trajectory analysis is the specific governance addition that distinguishes anticipatory design from the other patterns. Retroactivity profile: anticipatory changes may have limited immediate behavioral impact because the conditions they are designed for have not yet activated; the B2.70 retroactivity determination applies but may find limited immediate consequence. Primary use case: deployment is expected to operate in a new domain or under new conditions in the foreseeable future; DNA evolution prepares the orchestration architecture before the new domain or conditions activate.

Anticipatory design reflects the directed character of directed selection at its most explicit: the governing humans are not responding to current deficiency but are projecting forward and authorizing DNA evolution based on that projection. The governance framework permits this; trajectory analysis is the specific governance form that makes it governed rather than arbitrary.

### Pattern 5 — Response to Productive Tension

Response to productive tension is the cross-mechanism pattern. It formalizes directed selection as the governed mechanism that responds to the other two evolution mechanisms: mutation (instinct evolution through LLM upgrades and infrastructure changes) and action-feedback evolution (proposals produced by the action-feedback loop per B1.12).

The pattern has two sub-forms. In the mutation sub-form, instinct evolution introduces new capabilities through an LLM upgrade; the governing humans recognize that the new instinct capabilities create opportunities for DNA evolution, and directed selection is applied to leverage those capabilities — authoring orchestration rules that assign appropriate work to the new instinct capacity, updating routing rules that previously directed work to the reasoning layer because the instinct layer could not handle it, or redesigning coordination patterns to take advantage of new model capability. In the action-feedback sub-form, the action-feedback mechanism per B1.12 produces proposals derived from accumulated operation evidence; the governing humans review those proposals and, where authorized, apply directed selection to author DNA changes that incorporate the proposals.

Scope characteristics: determined by the scope of the mutation novelty or the action-feedback proposals being incorporated; may range from incremental to structural depending on the scope of the triggering event. Governance intensity: determined by the scope of the resulting DNA changes, calibrated to whichever other pattern the changes most closely resemble; the distinctive governance addition is cross-mechanism review — governance must assess not just the DNA changes in isolation but whether the triggering mechanism's output supports those changes. Retroactivity profile: follows from the scope of the DNA changes per B2.70; the cross-mechanism trigger does not alter the retroactivity treatment. Primary use case: post-mutation verification reveals new capabilities not previously available; or action-feedback accumulation produces proposals for DNA refinement; in both cases, directed selection is the mechanism by which governance authors DNA evolution in response.

Response to productive tension is architecturally significant because it operationalizes the productive tension commitment from B2.57. The productive tension between mutation and directed selection is not merely an abstract architectural property; it is exercised operationally through Pattern 5 each time humans apply directed selection in response to mutation novelty or action-feedback proposals.

---

## 3. What makes directed-selection-evolution-patterns architecturally distinctive

The pattern diversity established in this note marks a substantive difference from how AI system evolution is conventionally understood. In the prevailing model, an AI system evolves through one mechanism: model retraining, with the implicit assumption that every evolutionary need is addressed through the same approach — accumulate new data, retrain, redeploy. The architectural logic does not distinguish between the operational context of fine-tuning, correction, architectural redesign, anticipatory positioning, or response to new capabilities; these are all collapsed into the single retraining mechanism.

CKS directed selection operates differently. The five patterns formalized here each address a distinct operational context with distinct governance intensity requirements. The deployment governance team is not forced to apply the same review process to every evolutionary event; they select the pattern appropriate to the evolutionary need and calibrate governance to that pattern's scope. This calibration is not a minor operational convenience — it is what makes directed selection practically sustainable across the full range of evolutionary needs a deployment will encounter over its operational life.

The biological analog provides useful conceptual scaffolding without constraining the architecture. Selective breeding in agriculture produces approximate parallels: gradual line improvement through iterative selection for small trait improvements corresponds roughly to incremental improvement; corrective breeding to address a specific heritable deficiency corresponds roughly to targeted correction; deliberate breed redesign to establish a substantially different phenotypic profile corresponds roughly to structural redesign. But the analog has significant limits. Biology cannot cleanly distinguish between patterns that do and do not change architectural topology; DNA is not modular in the CKS sense. CKS patterns operate on explicit, human-readable rule content that can be modified with surgical precision; the biological mechanisms that produce heritable variation do not afford this control. The analog is a conceptual scaffold, not an architectural specification. The architectural substance is operational pattern diversity within the directed selection framework.

---

## 4. Inherited Paper 1 commitments

All five directed selection evolution patterns inherit the full set of Paper 1 commitments without modification. These inheritances are not re-argued here; they are stated precisely so that the cross-reference chain is unambiguous.

**A1.01 (human-governed).** Every pattern event is governed under A1.01's authority architecture. The right to inspect, modify, and override substrate content and orchestration rules is preserved across all five patterns. Governance intensity calibration operates within this framework — lighter governance for incremental improvement means a lighter review process, not the suspension of human authority over the changes.

**A2.04 (rule authoring).** All five patterns implement directed selection through A2.04 rule authoring. Pattern selection determines the scope and intensity of the authoring event; it does not change the mechanism. Humans (or LLMs under human direction per Paper 1 §3.3's authority-vs-labor distinction) draft the rule changes; humans hold authority over the acceptance decisions across all five patterns.

**A2.40 (provenance).** All five patterns produce provenance-bearing events. Every rule change through any pattern creates a provenance record: who authorized it, what pattern governed it, when it occurred, what it replaced. The provenance record is the same structural event across patterns; the pattern identity is one of its fields.

**A6.02 (retroactivity).** All five patterns produce DNA changes that undergo the B2.70 retroactivity determination under A6.02. Pattern selection does not alter the retroactivity framework; it affects the expected magnitude of the retroactivity event (structural redesign typically producing larger retroactivity events than incremental improvement), but the determination process applies uniformly.

**A1.10 (determinism).** Determinism is preserved across all five patterns. Pattern events that change DNA rules do not introduce non-determinism; the cell's behavior becomes deterministic under the new DNA version as it was deterministic under the prior version. Version management per B2.69 is what makes the transition auditable.

---

## 5. Operational implications

**Pattern recognition as governance skill.** The five patterns in this note are useful only if the governance team can recognize which pattern applies to a given evolutionary need. This recognition is not algorithmic; it requires human judgment about the scope of the need, the severity of any deficiency, the architectural implications of proposed changes, and the trajectory of the deployment. Pattern recognition is therefore a governance skill — something the governing humans develop over the deployment's operational life, not something the architecture supplies automatically.

**Pattern diary.** Deployments benefit from maintaining a record of which patterns were applied to which evolutionary events: the pattern identity, the triggering context, the scope of changes, the governance process applied, and the outcome. This pattern diary serves two organizational functions. First, it accumulates institutional knowledge about which patterns the deployment's governance team has applied, which supports organizational learning about the deployment's evolutionary trajectory. Second, it provides a governance audit trail that distinguishes the governance intensity applied to different events — auditors can verify that structural redesign events received comprehensive review rather than incremental-improvement-level review.

**Cadence interaction with mechanism priority per B2.58.** Different patterns have different natural cadences. Incremental improvement may run frequently — routine operational governance produces incremental improvements across the deployment's life as governance teams refine specific rules. Structural redesign, by contrast, runs rarely; a deployment may undergo structural redesign a handful of times in its operational life because the architecture is fundamentally sound most of the time. Anticipatory design runs at governance planning horizons, not at operational ticks. The different cadences interact with mechanism priority per B2.58: governance must ensure that frequent incremental improvements do not collectively produce de facto structural redesign without the comprehensive review that structural redesign warrants.

**High-stakes escalation.** High-stakes cells per B2.05 may require escalated governance intensity for any pattern. A deployment where certain cells carry patient-safety, regulatory compliance, or financial reporting consequences may apply structural-redesign-level governance intensity even to what would otherwise be an incremental improvement event, if that event touches the high-stakes cell's governing rules. The pattern calibration in §2 is the default; high-stakes escalation is the deployment-specific override.

**Cross-partner DNA evolution.** Deployments operating under cross-partner governance per A2.47 apply patterns within that governance framework. Pattern 5 (response to productive tension) is particularly relevant in cross-partner contexts where mutation at one partner's instinct layer may affect shared DNA, requiring coordinated directed selection across governance authorities. The pattern framework does not change; the governance coordination requirement is a cross-partner constraint that A2.47 addresses.

---

## 6. Limits

**Patterns are operational guidance, not architectural requirements.** A deployment is not required to use the five patterns named in this note. The enumeration is illustrative — the five patterns cover the major operational approaches that emerge from the directed selection mechanism's characteristics, but they do not exhaust the space. A deployment may identify additional patterns appropriate to its specific context; those patterns are equally valid so long as they operate within the B2.68 governance framework and follow B2.70 retroactivity treatment.

**Pattern selection is deployment judgment.** No architectural rule determines which pattern applies to which evolutionary event. A governance team that applies targeted correction where this note would suggest incremental improvement — because they judge the situation more severe — is exercising governance judgment, not making an architectural error. The patterns provide vocabulary and calibration guidance; they do not constrain governance discretion.

**Patterns do not change the underlying governance framework.** All five patterns use the same governance affordances: A2.04 rule authoring, A1.01 authority architecture, A6.02 retroactivity, A2.40 provenance. Pattern selection changes governance intensity and review scope; it does not change the governance mechanism. A party seeking to claim that pattern-specific governance constitutes a distinct governance architecture is wrong; the governance architecture is constant and is specified by B2.68, not by pattern identity.

**Patterns do not change retroactivity treatment.** The B2.70 retroactivity determination applies uniformly to all pattern events. The expected magnitude of the retroactivity event varies with pattern scope — structural redesign events typically produce larger retroactivity events than incremental improvement events — but the determination process does not vary. A2.06 and A6.02 apply in all cases.

**Patterns are not mutually exclusive.** A single directed selection event may combine elements of multiple patterns. A governance team addressing a specific deficiency (targeted correction) may discover during the correction process that the deficiency reflects an architectural inadequacy (structural redesign) while simultaneously recognizing that a mutation has created new capability that can be leveraged (response to productive tension). The three patterns can be combined in a single governed event that applies the appropriate governance intensity for the combined scope.

---

## 7. One-sentence test

A directed-selection evolution system instantiates the operational patterns formalized in this note if the governing humans apply directed selection through A2.04 rule authoring using operationally distinct approaches — among them incremental improvement of specific rules, targeted correction of identified deficiencies, structural redesign of the DNA architecture, anticipatory design for future requirements, and response to productive tension from mutation and action-feedback outputs — with governance intensity calibrated to the scope of each pattern, all under A1.01 human-governed authority, A6.02 retroactivity treatment, and A2.40 provenance across every pattern event.

---

## 8. Why naming as standalone matters; position in Phase B2

B2.71 is the seventy-first Phase B2 note and the fifth of six notes decomposing B1.14 directed selection. The decomposition sequence is:

- B2.67 — directed selection scope (what directed selection can modify)
- B2.68 — DNA modification governance (the governance framework)
- B2.69 — DNA version management (how versions are tracked)
- B2.70 — retroactivity treatment (what happens when DNA changes propagate)
- B2.71 — directed selection evolution patterns (this note: how directed selection is applied operationally)
- B2.72 — directed selection verification (how directed selection events are verified)

The decomposition is designed so that each note contributes non-overlapping prior-art coverage of the directed selection mechanism. B2.67 through B2.70 established the governance infrastructure; B2.71 establishes the operational pattern vocabulary that governance teams use within that infrastructure; B2.72 will close the decomposition by formalizing the verification that confirms directed selection events have produced intended behavioral outcomes.

Naming the operational patterns as a standalone note rather than embedding them in the governance note (B2.68) or the retroactivity note (B2.70) is architecturally and strategically appropriate. Architecturally, patterns are a distinct layer from governance affordances — knowing the governance framework does not tell a deployment team how to apply it across the range of evolutionary needs; the patterns layer provides that operational guidance. Strategically, the standalone formalization creates independent prior-art coverage for the combination of pattern diversity and governance intensity calibration, which is the specific architectural contribution this note makes.

Following B2.72, Phase B2 continues with the B1.15 action-feedback decomposition (B2.73 and beyond), which will develop the operational specifics of the third evolution mechanism under its distinct governance shape.

---

## References

Li, Wenxin. "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems." April 2026.

Li, Wenxin. "The Instinct/Reasoning Separation Outside the Model." April 2026.

Li, Wenxin. "Authority, Not Labor: A Precise Definition of 'Human-Governed' in the Coordination Knowledge Substrate Pattern." April 2026. (Series A, Note A1.01.)
