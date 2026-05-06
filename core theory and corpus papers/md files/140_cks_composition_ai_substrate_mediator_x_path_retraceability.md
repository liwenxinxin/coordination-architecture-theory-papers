# Accountable AI by Composition: How AI-as-Substrate-Mediator and Path Retraceability Compose to Produce Architectural Accountability for AI Behavior in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a single standalone architectural object, the emergent property that arises when two of the source paper's foundational commitments — AI-as-substrate-mediator and path retraceability — compose, so that downstream work has a precise specification of the property and an operational test for whether a given system instantiates it.

## Abstract

Two of the foundational architectural commitments of the CKS pattern — AI-as-substrate-mediator (§4.1, §4.2) and path retraceability (§3.1) — are individually formalized as standalone derivation notes elsewhere in this series. This note formalizes their *composition* as standalone. The composition produces an emergent architectural property neither commitment yields independently: AI-mediated substrate changes are *specifically* retraceable through cell-execution-id and rule attribution, and the four accountability questions — who, what, why, when — are answerable for AI behavior through a substrate-resident cell-rule-mediation chain. The portable label is *AI-mediated retraceability*, and the property is what most directly distinguishes CKS from black-box AI systems whose outputs lack retraceable rationale. The note states the four operational components of the property, identifies what the composition forces beyond either commitment in isolation, distinguishes the property from four adjacent patterns it is commonly conflated with, identifies five anti-patterns that violate the composition distinctively from the way they violate either commitment alone, and provides an operational test with three sharpening properties.

## 1. Why the composition pair needs to be formalized as standalone

The CKS pattern names AI-as-substrate-mediator and path retraceability among its foundational architectural commitments. Each is independently formalized: the mediator role as a five-property specification of how LLMs operate over the substrate, and path retraceability as a structural property of substrate content carrying enough provenance to reconstruct causal antecedents from substrate reads alone. The two commitments compose in a way that produces an architectural property neither yields independently — AI-mediated changes are *specifically* retraceable through cell-execution-id and rule attribution, and the four accountability questions are answerable for AI behavior through the cell-rule-mediation chain.

The source paper's §4.4 is where the cell-rule-mediation discussion most directly resides; the discussion is load-bearing for what makes AI behavior architecturally accountable in CKS, but the property the discussion produces is implicit in the relationship between two foundational commitments rather than named as a standalone architectural object. Without naming the composition as standalone, the architecturally distinguishing property of CKS — that AI behavior is retraceable through substrate-resident provenance rather than opaque to subsequent inspection — remains implicit, with no independent citation target for downstream work to adopt or argue against.

The motivating observation is operational. A deployment may satisfy A1.04 individually (LLM operating as mediator nominally) and may satisfy A1.07 individually (substrate writes carrying provenance) yet still fail to produce specific AI accountability, because A1.04-alone admits mediator operation without retraceability attribution and A1.07-alone admits generic write provenance without AI-specific attribution. The composition is what forces the AI-mediation-specifically-retraceable property; naming it makes the gap between individual-commitment satisfaction and emergent-property satisfaction explicitly identifiable. Naming it as standalone is also consequential for prior-art purposes in a 2024–2026 environment in which "AI accountability" and "explainable AI" are dominant commercial concerns.

This note is the fourth in Phase A4. It follows three sibling notes: A4.01 (the A1.01 × A1.08 composition formalizing where governance lands — on authoritative substrate content), A4.02 (the A1.01 × A1.04 composition formalizing how AI is governed — through human-authored rules), and A4.03 (the A1.02 × A1.08 composition formalizing where authority is located — on the substrate side of the boundary). The four opening compositions together cover four foundational architectural patterns: governance-against-authority, governance-of-AI-through-rules, authority-locus-on-state-side, and AI-mediated retraceability. A4.04 supplies the fourth.

## 2. The emergent architectural property

In the CKS pattern, a deployment satisfies the **A1.04 × A1.07 composition** if and only if all four of the following operational components hold for every AI-mediated substrate change at all times during the deployment's existence.

1. **Every AI-mediated substrate change carries a cell-execution-id** (A2.40 field 6). Every AI mediation occurs within a specific cell instance, and the substrate write produced by that cell records the cell-execution-id as a provenance field. The cell-execution-id is the architectural anchor for tracing AI mediation back to its specific occurrence — not the LLM model, not a generic "AI" actor, but the named cell instance that performed the mediation.

2. **Every AI-mediated cell records the authorizing rule** (A2.40 field 2). Every cell that performs AI mediation is rule-authorized per A2.04, and the substrate write records a reference to the specific rule that authorized the cell's execution. The rule reference is the architectural anchor for tracing AI mediation back to its governance — to a substrate-resident, human-authored rule rather than to an unattributed LLM judgment.

3. **LLM consultation outputs are recorded with attribution** (A2.23 Property E). When a cell's execution involves an LLM consultation that affects substrate state, the cell's substrate write records attribution sufficient to identify the write as the result of an LLM operation under a named rule in a named cell execution. Property E specifies that attribution is recorded; the composition with A2.40 specifies the form attribution takes — the rule reference and cell-execution-id named above, plus the standard provenance fields.

4. **The four accountability questions are answerable for every AI-mediated change** (A2.36–A2.39). For any AI-mediated substrate change, a human exercising the inspect right per A2.01 can answer:

   - **Who** — the cell instance that performed the mediation, traceable via cell-execution-id;
   - **What** — the change made, with prior state and change description;
   - **Why** — the rule that authorized the cell, traceable via the rule reference, and itself a piece of human-authored substrate content;
   - **When** — the timestamp at which the cell's write was committed, in the substrate's temporal order.

The four components together name the emergent architectural property. The portable label is **AI-mediated retraceability**. The portable label most directly distinguishing the property from black-box AI systems is **accountable AI**.

A deployment satisfying all four components exhibits the emergent property; a deployment failing any component fails the composition. Each component is operationally inspectable from substrate content alone — none of the four requires consulting external logs, runtime middleware state, or vendor systems — which is what makes the accountability *architectural* rather than procedural.

## 3. What the composition forces beyond either commitment in isolation

Each of A1.04 and A1.07 is satisfiable individually in ways that do not produce the composition's emergent property. Naming what the composition forces precisely is the work of this section.

**A1.04 alone is satisfiable without retraceability attribution.** A deployment can satisfy the five-property mediator role — LLM reads substrate as primary state, LLM writes under orchestration rules, no out-of-substrate authoritative state, no LLM authority over substrate, LLM outputs recorded with attribution — and still produce AI-mediated writes whose attribution is generic ("the LLM did this") rather than specifically retraceable to the cell instance and authorizing rule. Property E (A2.23) commits the system to recording attribution; it does not, alone, specify which fields the attribution must include for AI mediation specifically.

**A1.07 alone is satisfiable without AI-specific attribution.** A deployment can satisfy the path-retraceability commitment — every substrate write carries the six provenance fields per A2.40, antecedent paths reconstructable from substrate reads alone — and still treat AI-mediated writes as generic system writes, with the actor field populated as "system" or "AI" rather than as the specific cell instance, and with the rule reference populated generically or omitted. A1.07 alone does not, on its own, force cell-mediated writes to name a rule per A2.04 specifically.

**The composition forces what neither commitment alone forces.** Specifically: AI mediation must be cell-bounded, ruling out LLM operations producing substrate effects outside the cell scope where attribution can be recorded; cells performing AI mediation must be rule-authorized per A2.04, with the rule itself resident in substrate; cell-execution-id (A2.40 field 6) — otherwise an optional provenance field — becomes required for AI-mediated writes; the rule reference (A2.40 field 2) for AI-mediated writes must point to a specific rule per A2.04, not to a generic system identifier; and A2.36–A2.39's four accountability questions must admit the AI-specific answers named in §2 above, not just generic answers about substrate state's overall provenance.

## 4. What the composition is NOT

Four adjacent architectural patterns are commonly conflated with AI-mediated retraceability, and each conflation produces a different misreading of what the composition requires.

**Not AI-mediator-without-retraceability.** Architectures in which an LLM operates as mediator without explicit retraceability attribution may satisfy A1.04 individually but do not produce AI-mediated retraceability. A deployment that nominally instantiates the mediator role but writes "the LLM did this" without naming the cell or rule has not produced the emergent property; the composition forces AI-mediation-attribution through the cell-execution-id and rule-reference fields specifically.

**Not retraceability-without-AI-specific-attribution.** Architectures in which substrate writes are retraceable but AI operations carry generic attribution may satisfy A1.07 individually but do not produce AI-mediated retraceability. A substrate whose writes are all retraceable but whose AI-mediated writes do not name the specific cell and rule has not produced the emergent property; the composition forces AI-specific attribution.

**Not "explainable AI" through model interpretation.** AI systems providing model-level explanations — attention visualizations, feature importance, prompt traces, chain-of-thought transcripts — produce a different kind of accountability at a different scope. The CKS composition produces *architectural* accountability, residing in substrate state and answerable through substrate reads. The composition does not require, and does not in itself produce, model-level explanation; a deployment may compose model-level explainability with the architectural pattern, but the architectural pattern stands without it.

**Not external audit logging of AI operations.** External logs that record AI operations — vendor-side request logs, runtime monitoring traces, observability-platform records — are not substrate-resident retraceability. The composition forces substrate-only paths per A2.41: the retraceability lives in substrate, not in external logs. A deployment whose AI accountability requires consulting an external system to answer the four accountability questions has not produced the emergent property the composition specifies.

## 5. Anti-patterns specifically violating the composition

Five anti-patterns formalized as standalone notes elsewhere in this series each violate the composition distinctively from the way each violates either commitment in isolation. In each case below, individual-commitment satisfaction is achievable in isolation but the composition fails at a specific architectural layer; naming the layer is what makes the composition's contribution explicit.

**A3.11 (LLM-as-autonomous-agent) — decision-layer composition violation.** Autonomous-agent decisions are not rule-authorized: the agent decides what to do, and the deciding is the agent's role, not a rule's. The composition fails at the decision layer because "why" cannot be answered as "rule R authorized this" — no rule did. A cell-execution-id may exist, but it does not trace to a substrate-resident rule, because no rule was the source of authorization.

**A3.12 (LLM-as-terminal-producer) — output-layer composition violation.** Terminal-producer outputs flow to consumers without cell-mediation, and any substrate effect they have is downstream of the LLM's role rather than within it. The composition fails at the output layer because the LLM-produced substrate content lacks cell-execution-id (no cell wrapped the output) and rule reference (no rule authorized the wrap).

**A3.13 (LLM-as-source-of-truth) — authority-layer composition violation.** When the LLM is treated as the authoritative source of substrate content, the LLM's output is the answer rather than a draft a cell records under a rule. The composition fails at the authority layer because authoritative content sourced from the LLM lacks rule-governance attribution — there is no rule per A2.04 the LLM was operating under, only its own judgment.

**A3.19 (non-addressable writes) — provenance-gap composition violation.** Non-addressable writes are the general failure mode in which substrate writes lack the provenance fields A2.40 specifies. The general failure is specifically severe for AI-mediated writes: absent cell-execution-id and rule reference, AI-mediated writes are unaccountable in precisely the way the composition forbids. A3.19 instances arising from AI-mediation provenance gaps are the most operationally consequential cases of the general failure.

**A3.04 (LLM-gatekeeping) — chain-interruption composition violation.** When the LLM gates substrate access — cells cannot operate without the LLM mediating their access — the cell-rule-mediation chain is interrupted. The cell does not operate under a rule; it operates under whatever the LLM is gating. The chain from rule to cell to AI mediation to substrate write cannot be reconstructed: the cell's authorization runs through the LLM's gating, not through the rule, and the four accountability questions admit no rule-grounded "why."

## 6. Operational test

A deployment satisfies the A1.04 × A1.07 composition if and only if the following hold at any time during the deployment's existence:

1. Every AI-mediated substrate change carries a cell-execution-id (A2.40 field 6) identifying the specific cell instance that performed the mediation.

2. Every AI-mediated cell records the authorizing rule (A2.40 field 2) as a reference to a specific substrate-resident rule per A2.46 authored under A2.04.

3. LLM consultation outputs that affect substrate state are recorded with attribution per A2.23 Property E.

4. The four accountability questions per A2.36–A2.39 (who, what, why, when) are answerable for every AI-mediated change from substrate content alone, without consulting external logs, runtime middleware state, or vendor systems.

Three sharpening properties are operationally testable on a deployment and together cover the load-bearing failure surfaces.

(a) **AI-mediation-cell-execution-id test.** Sample AI-mediated substrate changes and verify that A2.40 field 6 is populated with a cell-execution-id traceable to a specific cell instance. Missing field 6 on AI-mediated writes indicates composition failure.

(b) **AI-mediation-rule-attribution test.** Sample AI-mediated substrate changes and verify that A2.40 field 2 is populated with a reference resolving to a specific substrate-resident rule per A2.46. Generic, missing, or non-rule-resolving field-2 references on AI-mediated writes indicate composition failure.

(c) **AI-accountability-questions-answerability test.** Sample AI-mediated substrate changes and attempt to answer who, what, why, and when for each using only substrate reads. Inability to answer any of the four questions from substrate content alone indicates composition failure.

A deployment that passes (1)–(4) and (a)–(c) instantiates AI-mediated retraceability in the composition's sense.

**The one-sentence test.** *If a deployment's AI-mediated substrate changes specifically record cell-execution-id per A2.40 field 6 and rule attribution per A2.40 field 2, with LLM consultation outputs attributed per A2.23 Property E, and the four accountability questions per A2.36–A2.39 are answerable for every AI-mediated change through substrate-resident provenance per A2.41, the deployment satisfies the A1.04 × A1.07 composition pair, and AI behavior in the deployment is architecturally accountable rather than opaque.* The one-sentence test names the most operationally distinctive properties for any specific deployment and is useful for analysts and reviewers needing to classify a system quickly; the four-component specification of §2 plus the operational test above provide the full architectural definition for cases requiring detailed analysis.

## 7. Why naming the composition pair as standalone matters

The A1.04 × A1.07 composition is what makes CKS architecturally distinguishable from black-box AI systems. The distinguishing property is operational, not aspirational: AI-mediated changes can be answered through substrate reads alone for who, what, why, and when, and the answers run through cell-execution-id and rule-reference fields that are part of substrate state rather than external observability data. Without publishing the composition as standalone, the property remains implicit in the foundational commitments rather than architecturally specified.

Implementations that satisfy A1.04 individually or A1.07 individually but fail the composition produce systems where AI behavior is architecturally opaque even though individual commitments are formally satisfied — autonomous-agent decisions lack rule attribution (A3.11), terminal outputs lack cell-execution-id (A3.12), authority decisions lack rule-governance attribution (A3.13), generic write-provenance gaps fall hardest on AI-mediated writes (A3.19), or LLM gatekeeping interrupts the cell-rule-mediation chain (A3.04). The composition specifically prevents these failure modes by forcing AI-specific attribution as an architectural property of every AI-mediated substrate change.

The composition supports A1.10's Guarantee C per A2.59 (change addressability) for AI-mediated changes specifically: the deployment can re-apply an AI-mediated change by re-executing the named cell with the named rule against the recorded prior state, because the cell-execution-id and rule-reference fields make the change architecturally identifiable. The property also extends temporally per A2.07 — humans can investigate AI behavior from any point in deployment history because the cell-rule-mediation chain produces persistent retraceable provenance — and across the multi-human scope, with the inspect right per A2.01 carrying retraceability across all participants and sessions.

A4.04 follows A4.01, A4.02, and A4.03 in Phase A4. Together the four opening compositions cover the foundational architectural patterns of the CKS approach: governance-against-authority (A4.01), governance-of-AI-through-rules (A4.02), authority-locus-on-state-side (A4.03), and AI-mediated retraceability (A4.04). Subsequent Phase A4 notes will formalize approximately twenty-six additional architecturally significant composition pairs — among them A1.04 × A1.08 (mediator × source-of-truth), A1.07 × A1.10 (retraceability × determinism), A1.03 × A1.07 (conflict × retraceability), and A1.05 × A1.06 (tool-agnosticism × linear-cost). The opening four cover what is foundational: where governance lands, how AI is governed, where authority is located, and how AI behavior is accountable.

Subsequent work that adopts, extends, composes, or argues against the CKS pattern's accountable-AI property should use AI-mediated retraceability in the sense formalized here. Subsequent work that satisfies one or both of A1.04 and A1.07 individually but does not produce the four operational components of §2 is using a different architectural property, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Accountable AI by Composition: How AI-as-Substrate-Mediator and Path Retraceability Compose to Produce Architectural Accountability for AI Behavior in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
