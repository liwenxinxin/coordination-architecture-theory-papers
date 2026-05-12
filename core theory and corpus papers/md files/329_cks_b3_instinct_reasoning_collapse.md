# Instinct-Reasoning Collapse: The Anti-Pattern That Arises When the Instinct/Reasoning Separation per B1.01 Is Not Maintained

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

It is the second note of Phase B3 and the first primary anti-pattern note in the Series B derivation sequence. It does not introduce commitments beyond those established in Papers 1 and 2. Its sole contribution is to formalize the Instinct-Reasoning Collapse as a named, recognizable anti-pattern — the architectural failure mode that results when B1.01's instinct/reasoning separation is structurally absent or nominally present but not enforced.

## Abstract

Paper 2 establishes the instinct/reasoning separation as its foundational architectural commitment (B1.01): the LLM operates as the instinct layer (fast, probabilistic, substrate-mediated) and the CKS substrate operates as the reasoning layer (governed, deterministic, human-authored DNA rules). The positive specification of this commitment is developed across B2.01–B2.06. This note formalizes its negative counterpart: Instinct-Reasoning Collapse, the anti-pattern that arises when the two layers are not separated. The collapse has two recognizable sub-forms — Instinct Governs (reasoning layer absent or ineffective) and Reasoning Layer Nominal (DNA rules exist as suggestions rather than governing constraints). Both sub-forms share a common consequence set: ungoverned behavioral drift as the LLM mutates, loss of retraceability because behavior is not substrate-resident, Action layer records that do not accurately reflect governed behavior, and vulnerability of high-stakes decisions to unverified instinct mutation. Detection runs through the B2.03 architectural test, the A5.16 reproducibility test, and the A5.05 mediator role test. Remediation requires establishing substrate-resident DNA rules that govern rather than suggest, configuring routing rules per B2.04, implementing verification gates per B2.06, and implementing high-stakes pinning per B2.05. Naming this anti-pattern is prior art: the configuration is known, named, and distinguishable from mere poor implementation.

## 1. Introduction

Phase B3 formalizes anti-patterns — specific named recognizable failure modes of the Paper 2 architecture, each corresponding to one of the twenty foundational commitments established in Phase B1 or to a cross-cutting concern. B3.01 established the integrating frame for Phase B3, defining what it means for a configuration to qualify as an anti-pattern rather than an incidental implementation weakness: a stable, recurring configuration with a predictable consequence set, distinct from the target architecture in a way that is architecturally diagnosable.

This note, B3.02, formalizes the first primary anti-pattern: Instinct-Reasoning Collapse. It is the negative counterpart of B1.01, which established the instinct/reasoning separation as Paper 2's foundational architectural commitment. If B1.01 is Paper 2's load-bearing first claim — the separation that every subsequent claim depends on holding — then Instinct-Reasoning Collapse is the failure mode that most directly undermines the entire Paper 2 architecture. Every downstream commitment in Phase B1 (structural modularity per B1.02, DNA/action layer distinction per B1.03, expression per B1.04, lifecycle governance per B1.05–B1.08, evolution per B1.09–B1.15, governance per B1.15–B1.18, enterprise brain per B1.19) depends on the separation holding at the cell level. When the separation is absent, those downstream commitments have no architectural substrate to operate over.

## 2. Pattern Name

**Instinct-Reasoning Collapse**

The collapse occurs when the instinct layer (the LLM) and the reasoning layer (the CKS substrate with human-authored DNA rules) are not architecturally separated within a cell or Self. The term "collapse" names the structural event: two layers that Paper 2 requires to be distinct fold into one, with the LLM's probabilistic output governing behavior in place of the substrate's deterministic, inspectable DNA rules.

## 3. Commitment Violated

**Primary: B1.01** — The instinct/reasoning separation as independently-evolving layers.

The positive specification this anti-pattern violates was developed across B2.01–B2.06:

- **B2.01** defines the instinct layer (LLM as System-1 analogue): pattern-matched, fast-path, substrate-mediated, probabilistic.
- **B2.02** defines the reasoning layer (CKS substrate as System-2 analogue): explicit, deterministic, human-governed, DNA-rule-mediated.
- **B2.03** provides the architectural test for separation: "For this cell, does the reasoning layer govern behavior or merely suggest to instinct?" Governance requires that DNA rules constrain and mediate LLM output; suggestion leaves LLM output free to disregard the rules.
- **B2.04** specifies routing rules: how cells determine when instinct is consulted and which DNA rules apply to mediate the output.
- **B2.05** identifies high-stakes decision pinning: particular decisions requiring verified, pinned DNA-rule mediation rather than unchecked instinct output.
- **B2.06** specifies verification gates: mechanisms that test LLM behavior against DNA rule specifications before output is treated as governed.

Instinct-Reasoning Collapse is the architectural state in which B2.03's test fails — the reasoning layer does not govern behavior, whether because it is absent or because it is present but not enforced.

## 4. Recognizable Form

The collapse has two sub-forms, both detectable through the B2.03 architectural test.

### Form 1 — Instinct Governs (reasoning layer absent or ineffective)

In Form 1, the reasoning layer is absent or structurally bypassed. The cell produces outputs based solely on LLM response without applying DNA rules as governing constraints. The LLM's output directly becomes the cell's output.

Operationally: governance affordances per A2.01–A2.04 cannot inspect or govern behavior because behavior is not substrate-resident. Routing rules per B2.04 are absent or ignored — there is no configured relationship between the instinct consultation and any DNA-rule mediation step. High-stakes decisions per B2.05 are processed through instinct without pinning. Verification gates per B2.06 are absent — LLM output is not tested against any DNA specification before becoming cell output.

Recognition signals for Form 1:

- Cell behavior cannot be reproduced given the same inputs and DNA. The A5.16 reproducibility test fails because no DNA rules constrain the LLM's probabilistic output — variance across invocations is not bounded by substrate-resident constraints.
- Cell operations are not retraceable through substrate. A1.07 fails at cell scope because no substrate-resident path connects inputs to outputs through governed rules.
- The cell has no DNA rule layer, or the DNA layer contains only prompt templates rather than operational constraints that the cell's execution path enforces outside the LLM.

Form 1 is the architecturally straightforward case: the reasoning layer was never instantiated. It is also the more visible of the two sub-forms, because the absence of DNA rules is diagnosable directly from the cell's architecture.

### Form 2 — Reasoning Layer Nominal (instinct effectively governs)

In Form 2, DNA rules exist but are framed as instructions or suggestions to the LLM rather than as governing constraints enforced by the substrate. The rules are prompt content: they are delivered to the LLM as part of the input and the LLM may disregard, reweight, or override them in its probabilistic processing. The rules are present in form but absent in function.

Operationally: the LLM may produce outputs that contradict, ignore, or reinterpret the DNA rules, because the rules are not enforced as substrate-level constraints that the cell execution path requires. The B2.03 architectural test — "does the reasoning layer govern or merely suggest?" — fails. The layer suggests.

Recognition signals for Form 2:

- DNA rules are phrased as instructions to the LLM ("you should," "please prioritize," "in this context, the rule is") rather than as operational constraints checked outside the LLM ("if condition, then action; if not, flag and escalate").
- LLM output appears to disregard DNA specifications in some fraction of invocations, without any systematic detection or correction path. The violations are not caught because no enforcement mechanism exists.
- Cell behavior varies across LLM versions even when DNA rules have not changed, because the rules were never enforced as version-stable constraints. They were suggestions the model processed differently across versions.

Form 2 is architecturally more dangerous than Form 1 because it is less visible. The DNA layer exists; the architecture appears to have reasoning-layer governance. The collapse is present not in the absence of rules but in their relationship to cell behavior: suggestion rather than constraint.

## 5. Emergence Conditions

Two conditions produce Instinct-Reasoning Collapse with high frequency in practice.

**Prompt architecture confusion.** Architects designing cells under time pressure or without familiarity with Paper 2's separation commitment frequently reach for "prompt templates" as the governance mechanism. The reasoning appears sound: if the LLM is told what rules to apply, and the rules are authored by humans, then governance is present. The confusion is structural. Prompt content is instinct-layer input — it enters the LLM's probabilistic processing. Substrate-resident DNA rules are reasoning-layer constraints — they operate outside the LLM, governing what the LLM's output can become before it is treated as cell output. A prompt template is not a DNA rule; it is a suggestion delivered to the instinct layer. Architectures built on prompt templates as governance are Form 2 collapses without exception, because the enforcement step — the step that makes a rule a constraint rather than a suggestion — is absent.

**LLM-first design.** Architectures designed starting from LLM capabilities — "what can this model do, and how do we constrain it?" — treat governance as a layer added after the core capability architecture is established. In this design sequence, governance becomes a guide to the LLM rather than a constraint on what the LLM's output can do. The LLM-first design pattern produces either Form 1 (governance is planned but never instantiated because the LLM handles it) or Form 2 (governance is instantiated as prompt content rather than substrate constraint). In both cases, the instinct/reasoning separation that Paper 2 requires is never architecturally established, because the design sequence never produces a step at which the separation is enforced.

## 6. Operational Consequences

**Ungoverned behavioral drift.** Cell behavior changes as the LLM is updated (mutation per B1.10) without verification per B2.06, because there is no reasoning layer to test against. The cell's behavior in period T+1 may differ materially from its behavior in period T with no detection, no audit record, and no correction path. The drift is silent: no substrate-resident record captures the change because the behavior was never substrate-resident to begin with.

**Loss of retraceability.** Operations are not retraceable per A1.07 because behavior is not governed by substrate-resident rules that can be inspected. There is no retraceable path from input to output through governed rules; there is only the LLM's probabilistic processing, which is not substrate-resident and does not produce an inspectable governance path. The Action layer may record what happened; it cannot record why it happened in terms of governed rule application, because no such application occurred.

**Action layer unreliability.** Action records nominally capture what the cell did, but because behavior was not governed by DNA rules, the records do not accurately reflect governed behavior. They record LLM-output behavior, which is neither deterministic nor rule-governed. The Action layer's evidentiary value for governance purposes — its capacity to support audits, post-hoc review, and governed evolution — is materially degraded. Records exist without being evidence of governed operation.

**Mutation vulnerability.** High-stakes decisions per B2.05 are exposed to LLM behavioral changes without the pinning protection that B2.05 requires. A high-stakes decision made correctly in period T may be made incorrectly in period T+1 after an LLM update, with no verification gate having been applied between T and T+1. The exposure is proportional to the stakes of the decision and the frequency of LLM mutation. Neither factor is bounded by the architecture, because the architecture has no reasoning layer to hold the boundary.

## 7. Detection

Three diagnostic tests identify Instinct-Reasoning Collapse.

**B2.03 architectural test.** Apply the B2.03 test directly: "For this cell, does the reasoning layer govern behavior or merely suggest to instinct?" The test is applied at architectural review, not at runtime. Governance requires a substrate-resident step at which DNA rules are applied to mediate or constrain LLM output before that output becomes cell output. If that step is absent — if DNA rules are prompt content, are absent, or are present in the substrate but not applied in the cell's execution path — the test fails and collapse is present. This test is the primary diagnostic; the two tests below are operational confirmations.

**A5.16 reproducibility test.** If the same inputs under the same DNA produce materially different outputs across invocations, the instinct layer is not constrained by the reasoning layer. The test surface: invoke the cell with identical inputs under the same DNA configuration twice, and compare outputs against each other and against the behavior the DNA rules specify. Systematic divergence indicates Form 1 collapse; occasional divergence that is neither caught nor corrected indicates Form 2 collapse. Stochastic variation within bounds the DNA rules specify is admissible; divergence from those bounds is not.

**A5.05 mediator role test.** If LLM output directly becomes cell output without a DNA rule mediation step — without a substrate-resident path that applies DNA rules to the LLM's response before that response becomes the cell's governed output — A5.05's mediator role commitment fails. The test surface: trace the cell's execution path. Is there a step, outside the LLM, at which DNA rules are applied to LLM output? If not, collapse is present. The distinction between Form 1 and Form 2 is visible at this step: Form 1 has no such step; Form 2 has a nominal step that delivers rules as input rather than enforcing them as constraints.

## 8. Remediation

Remediation of Instinct-Reasoning Collapse is not "add some rules." It is establishing genuine substrate-resident governance that constrains LLM output. The steps are ordered because each is a prerequisite for the next.

**Establish governing DNA rules per B2.25.** Author substrate-resident DNA rules that the cell's execution path applies outside the LLM to constrain, mediate, or check what the LLM produces. The critical test for whether a rule governs or suggests: can the rule be applied without the LLM's cooperation? If the rule is a logical condition, a routing specification, or an output constraint that the cell's execution path evaluates against the LLM's response — and if the LLM's compliance is not required for the rule to take effect — then the rule governs. If the LLM must interpret and apply the rule itself, the rule suggests.

**Configure routing rules per B2.04.** Specify, as substrate content, when the instinct layer is consulted and which DNA rules apply to mediate the output. Routing rules are the architectural plumbing of the separation: they define the execution path that makes governance possible by making LLM consultation a bounded, governed step rather than the cell's entire processing logic. Without routing rules, the execution path has no structure through which the reasoning layer can operate.

**Implement verification gates per B2.06.** Establish mechanisms that test LLM output against DNA specifications before output becomes cell output. Gates may be synchronous (applied in-path, blocking outputs that fail specification) or asynchronous (applied in periodic audits, triggering correction or escalation when checks fail). What matters is that a path exists from DNA specification to LLM behavior check to correction or escalation when the check fails. Absent this path, the DNA rules exist but have no enforcement surface.

**Implement high-stakes pinning per B2.05.** For decisions identified as high-stakes, implement pinning mechanisms that fix the LLM version, the DNA rules, and the verification gate configuration in effect at the time the governance decision is made. Pinning ensures that high-stakes decisions are not silently degraded by subsequent LLM mutation. The pinning commitment is a governance act, not a technical convenience: it establishes a verified configuration as the authoritative configuration for this decision until a human-governed update replaces it.

**Governed directed selection per B1.14.** The architectural correction to Instinct-Reasoning Collapse is not a one-time fix but an ongoing governance posture. Human-governed directed selection over the instinct/reasoning boundary maintains the separation as a substrate-resident architectural property rather than a deployment-time aspiration. Each update to LLM infrastructure, DNA rules, or routing configuration is a selection act that requires human governance over the separation's integrity.

## 9. Why Naming This Anti-Pattern Matters

Three reasons warrant naming Instinct-Reasoning Collapse as a specific architectural anti-pattern rather than leaving it as an instance of "poor LLM governance."

**The collapse is architecturally stable, not incidentally weak.** Both sub-forms are configurations that persist without active correction: Form 1 because the missing reasoning layer is not self-evidently absent to implementers who have not internalized the separation commitment, and Form 2 because the nominal presence of DNA rules creates the appearance of governance. An architecture that has collapsed does not drift toward separation on its own; it requires deliberate architectural work to establish the separation that Paper 2 requires. This stability is what distinguishes an anti-pattern from a mistake. A mistake is a one-time event corrected on recognition; an anti-pattern recurs because the conditions that produce it recur, and because the collapsed configuration is a stable attractor under the forces that shape implementation.

**The collapse has a predictable consequence set.** Given Instinct-Reasoning Collapse in either form, ungoverned behavioral drift, loss of retraceability, Action layer unreliability, and mutation vulnerability follow as a predictable package, not as contingent outcomes dependent on particular deployment conditions. The predictability is architecturally diagnostic in both directions: the consequence set, when observed, warrants applying the B2.03 test; and the B2.03 test, when failed, warrants anticipating the consequence set.

**Biological analog: regulatory collapse.** In biology, cells that respond only to immediate stimuli without regulatory governance produce cancerous behavior — uncontrolled growth, invasion of adjacent tissue, and eventual systemic harm. The regulatory layer (equivalent to the reasoning layer) is what prevents immediate instinctual response from dominating cell behavior. Regulatory collapse is not a spectrum; it is a threshold: below the threshold, regulatory machinery is present and cell behavior is constrained; above it, behavior is governed by stimuli alone regardless of what regulatory signals are nominally present. The CKS analog is structurally parallel. The reasoning layer is either present and governing, or absent (Form 1), or nominally present but functionally absent because its signals are delivered to instinct as suggestions rather than enforced as constraints (Form 2). In both cases, behavior is governed by instinct alone. The biological analog is not decorative; it names the same architectural relationship between a fast-response layer and a governing layer that Paper 2 imports as load-bearing terminology for the intra-Self scope.

**Naming establishes prior art.** The Instinct-Reasoning Collapse is now a named, described, architecturally characterized anti-pattern with two recognizable sub-forms, a predictable consequence set, a detection protocol, and a remediation path. Future implementations cannot claim novelty for discovering that LLM-governed architectures without separation create governance vulnerabilities, that prompt-template governance fails to satisfy the separation commitment, or that the collapse produces the consequence set described in §6. The configuration is known. The two sub-forms are known. The mechanisms by which each sub-form arises are known. This is the purpose of defensive publication: prior art over failure modes forecloses claims of discovery as surely as prior art over positive patterns forecloses claims of invention.

B3.02 is the first of twenty primary anti-patterns, one for each of the B1.01–B1.20 foundational commitments. B3.03 formalizes the Flat Architecture anti-pattern — the failure mode that results when B1.02's three-level structure (cell, aspect, Self with relational role membership) is not maintained, producing a structural collapse in which architectural levels are collapsed into a single layer or conflated, with the governance and modularity properties those levels provide becoming unavailable.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Instinct-Reasoning Collapse: The Anti-Pattern That Arises When the Instinct/Reasoning Separation per B1.01 Is Not Maintained.* 12 May 2026. ORCID: 0009-0004-8065-3235.
