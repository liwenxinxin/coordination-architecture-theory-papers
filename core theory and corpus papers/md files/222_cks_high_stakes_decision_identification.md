# High-Stakes Decision Identification: The Substrate-Resident Classification Mechanism Driving Reasoning-Layer Pinning in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one operational variant of the instinct/reasoning separation — the **identification mechanism by which deployments classify decisions as high-stakes for reasoning-layer pinning** — as an architecturally distinctive primitive whose substrate-resident, governable, auditable form distinguishes it from the no-classification and implicit-classification approaches characteristic of conventional AI architectures.

## Abstract

Paper 2's core theory commits, in its "Governance shapes across evolution mechanisms" section, that mutation (instinct evolution) is governed through verification, routing, and *the orchestration rules that pin high-stakes decisions to reasoning*. Pinning protects high-stakes decisions from delegation to the instinct layer regardless of how capable that layer becomes. But pinning by itself has no architectural target: every cell either becomes pinned (eliminating the instinct layer's utility) or no cell is pinned (eliminating the reasoning layer's protection). The middle — pinning the right decisions, at the right granularity, under governable rules — depends on a separate operational primitive: the identification mechanism by which the substrate classifies a cell goal or cell input as high-stakes. This note formalizes that mechanism. Identification rules per A2.04 are authored by humans and live as substrate-resident authoritative content per A2.46; identification decisions are recorded with provenance per A2.40; identification operates within Paper 1's human-governed authority architecture (A1.01); rule changes follow A6.02 retroactivity treatment. The note states the mechanism, distinguishes it from no-classification and implicit-classification approaches, enumerates the operational rule forms, lists inherited Paper 1 commitments, names operational implications and limits, and provides an operational test.

## 1. Why high-stakes decision identification needs to be formalized as standalone

Paper 2 specifies three instruments through which mutation (instinct evolution) is governed: verification of the instinct layer's outputs, routing of cell goals between instinct and reasoning layers, and pinning of high-stakes decisions to the reasoning layer. Pinning is the strongest of the three: it removes the option of instinct-only processing for the decisions that warrant the reasoning layer's substrate-rule-bounded behavior, regardless of how the instinct layer's pattern-matching capability evolves under upstream upgrades.

The strength of pinning depends on what it is applied to. A separate decomposition note (B2.04) formalizes the routing patterns by which cells are dispatched between layers; pinning is more architecturally severe than routing — it forecloses the instinct option for a class of cells rather than choosing the reasoning option for a particular cell — and presupposes that the deployment can identify, in advance and durably, which decisions warrant pinning. Without identification, the deployment must pin everything (forfeiting the speed the instinct layer provides for routine work) or pin nothing (forfeiting the protection the reasoning layer provides for consequential work). Either extreme defeats the separation Paper 2 commits to.

The middle — pinning the right decisions, under governable rules, at granularities the deployment chooses — is where high-stakes decision identification operates. Naming this mechanism as a standalone operational variant of B1.01 is what makes the architecturally-governable middle describable. Identification is not a prerequisite that lives outside the architecture, nor an implicit feature of developer judgment. It is substrate-resident authoritative content with a governance affordance equal to any other substrate content: inspectable, modifiable, overridable, versioned, provenance-bearing. This note is the fifth Phase B2 note decomposing B1.01, following B2.01–B2.04 and preceding B2.06's verification-gate decomposition that closes the B1.01 series.

## 2. The identification mechanism, precisely stated

In a CKS Self with the instinct/reasoning separation operating per B1.01, **high-stakes decision identification** is the operational mechanism by which the deployment classifies a cell goal or cell input — at design time, at execution time, or both — as high-stakes for the purpose of triggering pinning per B1.13. Six properties characterize the mechanism.

**(a) Identification rules are substrate-resident authoritative content.** Per A2.46, the substrate is authoritative for which rules apply to which cells; identification rules live within that scope. They are not configuration of an external runtime, not constants embedded in cell code, and not implicit in developer judgment.

**(b) Identification rules are authored by humans.** Per A2.04, orchestration rule authoring is one of the two moments at which governance is exercised. Identification rules are orchestration rules in the same sense — they determine cell-level behavior, specifically whether the cell processes through the reasoning layer per B1.13. As with other orchestration rules, identification rules may be drafted by LLMs operating under human direction; the authority over their content sits with humans.

**(c) Identification operates against criteria the deployment chooses.** Common criteria include regulatory compliance (decisions affecting medical, legal, financial-reporting, privacy, or accessibility outcomes), financial impact (material consequences above a threshold), safety implications (human safety, property safety, system stability), irreversibility (outcomes that cannot be corrected after the fact), contractual obligations, fiduciary duties, and audit-relevance. The enumeration is illustrative, not prescriptive; deployments author criteria appropriate to their operational context, may use a subset, and may add criteria specific to their domain.

**(d) Identification operates at multiple levels.** Cell-level identification classifies a specific cell execution; cell-class identification classifies all cells of a certain type; input-conditional identification classifies a cell's specific execution when its inputs match specified characteristics; combination identification composes these — for example, a cell-class baseline overridden upward when input thresholds are met. The mechanism does not commit to one level.

**(e) Identification decisions are recorded with provenance.** Per A2.40, substrate content carries six provenance metadata fields. Which classification rule fired, which version was active, which cell or input it applied to, when the classification was performed — all are recorded under the same machinery. The classification is not opaque after the fact.

**(f) Identification drives pinning.** Once a decision is identified as high-stakes, B1.13's pinning instrument applies: the cell processes through the reasoning layer, where substrate-resident rules bound its behavior. Identification is what gives pinning its architectural target. Deployments with weak or absent identification rules have weak pinning operationally, even if pinning is configured architecturally — because decisions that should be pinned never trigger the pinning condition.

The six properties are inherited rather than novel: each is a direct consequence of Paper 1 commitments composed with Paper 2's instinct/reasoning separation. The contribution of this note is to name their composition as a standalone operational primitive distinct from the pinning instrument it serves.

## 3. What makes high-stakes decision identification architecturally distinctive

Conventional AI architectures handle "which decisions warrant extra scrutiny" in one of two ways, both of which differ from the CKS treatment.

**No classification.** The first approach treats all decisions identically: every model output goes through the same path, and any additional scrutiny — human review, policy check, escalation — is applied as an external workflow rather than as an architectural property of the system. The approach can be operationally adequate when stakes are uniformly low or uniformly high, but it collapses the middle: there is no architectural primitive for "this decision warrants the slower, governed path while that decision does not."

**Implicit classification.** The second approach embeds the classification in developer judgment: developers decide, in code, which decisions get extra checks, which prompts include guardrail language, which outputs go to human review. The classification exists, but it is implicit — not represented as substrate content, not auditable as such, not modifiable without redeployment, not visible to inspectors who do not read code.

CKS makes high-stakes decision identification first-class architectural content. Identification rules are substrate-resident (A2.46), human-authored (A2.04), inspectable (A2.01), modifiable (A2.02), overridable (A2.03), versioned (A6.14), and provenance-bearing (A2.40). Three operational consequences follow. *Identification is auditable* — an auditor reads the active rules, the version history, and specific past classifications directly from substrate content rather than from a derived report. *Identification is modifiable under governance* — when operational context changes, rules are modified per A2.02 within the standard authority architecture, applying forward while existing classifications retain their original rule version. *Identification is overridable* — a specific classification can be overridden per A2.03 without justification, with the override recorded and the rule itself revised only if the override pattern becomes systematic.

## 4. Operational identification rule forms

Identification rules per A2.04 take operational forms appropriate to the criteria they encode. *Explicit classification rules* name a decision class directly: "decisions about regulated medical recommendations are high-stakes." *Threshold-based rules* classify by quantitative criteria: "decisions with financial impact above $X are high-stakes," with the threshold itself substrate content modifiable as scale changes. *Context-based rules* classify by execution context: "decisions in audit-relevant contexts are high-stakes," with the determination of which contexts count as audit-relevant itself substrate content. *Client-specific rules* classify by the cell's client or aspect-domain, accommodating deployments that serve multiple clients with different regulatory or contractual stake profiles. *Combination rules* compose the above — "decisions matching any of A, B, C are high-stakes," or "A and B but not C" — expressing deployment-specific stake profiles that no single primitive criterion captures.

Identification rules are versioned per A6.14. Long-lifecycle deployments accumulate revisions: thresholds adjust as financial scale changes; client categories evolve; new regulatory frameworks introduce new criteria; existing categories retire when their underlying obligation lapses. Rule changes follow A6.02 retroactivity treatment — historical decisions classified under prior rules retain their classification under those rules; new identification applies forward. Audit reach into the historical record is preserved by the rule-versioning machinery rather than by retroactive reclassification, which would silently rewrite the deployment's classification history.

## 5. Inherited Paper 1 commitments

Every property of high-stakes decision identification is inherited from Paper 1 commitments composed with Paper 2's instinct/reasoning separation. The inheritances are direct: A2.04 (rule authoring) — identification rules are orchestration rules; A2.46 (substrate authoritative for what rules apply) — identification rules live in this scope; A2.40 (six-field provenance metadata) — identification decisions are recorded under the same metadata machinery; A1.01 (human-governed) — humans hold authority over what counts as high-stakes; A2.01 (inspect right) — rules and decisions are inspectable at the time of an authority-holder's choosing; A2.03 (override right) — specific classifications are overridable without justification; A1.07 (path retraceability) — identification history is retraceable through the substrate's accountability vocabulary; A1.04 (AI-as-substrate-mediator) — when LLMs propose identification rules from observed patterns or apply classification logic at execution time, they operate within the mediator role under human authority. The note introduces no commitment outside this inheritance.

## 6. Operational implications

Deployments configure identification rules per their operational context: regulatory frameworks, internal policies, and risk frameworks all inform the rules. The mechanism does not prescribe categories; it provides the substrate-level affordance under which deployments express them. Identification rules evolve through B1.14's directed-selection mechanism on DNA — deployments refine what counts as high-stakes as operational experience accumulates, under the standard authority shape. Identification is testable through inspection: an auditor reads the active rules, examines past classifications, and forms a judgment about whether the deployment's identification reflects its stated stake profile.

Identification interacts with the routing patterns formalized in B2.04: high-stakes decisions typically use pure-reasoning or hybrid-with-pinning routing, since pure-instinct routing does not provide the substrate-rule-bounded protection the reasoning layer carries. Identification connects to the verification gates formalized in B2.06: high-stakes paths may invoke verification gates that non-high-stakes paths do not. Deployments may use multi-tier identification — distinct stakes levels with distinct pinning intensities and verification regimes — with the tier structure itself substrate content under governance. When CKS substrates compose across partners (per A2.47), identification may need cross-partner authority for unified classification; the resolution of asymmetric classification across partners is governance content, not local cell content.

## 7. Limits

The standalone framing does not extend beyond what the source paper supports.

Non-identified decisions are not unimportant — they are governed differently. Identification distinguishes decisions warranting the reasoning layer's substrate-rule-bounded path from those that do not; decisions classified as not-high-stakes remain under A1.01 governance. Identification does not eliminate all-decision governance: substrate content remains inspectable, orchestration rules remain modifiable, override rights apply, regardless of classification. Identification is not absolute — the classification is governable per A2.04 and revisable. Identification does not prescribe specific stake categories — the criteria enumerated in §2 are illustrative; deployments author categories appropriate to their context. Identification does not substitute for cell-level governance — within the cell layer, the standard cell-level commitments still apply; identification operates above the cell layer rather than in place of it. Identification rules are not exhaustive — a deployment may author rules that miss categories that later prove relevant, and the rule machinery affords the addition of new categories under governance.

## 8. Operational test

A deployment instantiates high-stakes decision identification when all of the following hold at all times during the substrate's existence:

1. The substrate carries human-authored identification rules per A2.04 specifying which decisions are high-stakes.
2. The identification rules are inspectable (A2.01), modifiable (A2.02), and overridable in their applications (A2.03), at the time of an authority-holder's choosing.
3. Identification rules carry version metadata (A6.14) and identification decisions are recorded with provenance (A2.40) sufficient to retrace which rule fired on which cell at which version.
4. Cells classified high-stakes are pinned to the reasoning layer per B1.13, with the pinning operationally enforced rather than advisory.
5. Rule revisions follow A6.02 retroactivity treatment: historical classifications are not retroactively altered by rule changes.

A deployment that fails any of (1)–(5) may be a useful AI system, and its high-stakes scrutiny may be operationally adequate, but it does not instantiate high-stakes decision identification in the architectural sense this note formalizes.

## 9. Why naming as standalone matters

The instinct/reasoning separation Paper 2 commits to under B1.01 is a class of architectural decisions, not a single primitive. The Phase B2 decomposition makes those decisions individually addressable: B2.01 names the instinct layer, B2.02 the reasoning layer, B2.03 the architectural test for separation, B2.04 the routing patterns, B2.05 (this note) the identification mechanism that determines what reasoning-pinning applies to, and B2.06 (next) the verification gates that operate on instinct-routed cells. None of the decomposition notes is a new commitment; each is the inheritance of Paper 1 commitments composed with Paper 2's separation, named at the granularity at which patentable territory accrues. The fifth-position note formalizes the operational pre-condition for the strongest of mutation-governance instruments — pinning — and the property under which the architecturally-governable middle is realizable as a substrate-resident, governable, auditable classification mechanism rather than as code, developer judgment, or workflow.

Subsequent work that adopts the instinct/reasoning separation, extends it, composes it with adjacent patterns, or argues against it should treat high-stakes decision identification as the mechanism formalized here. Subsequent work that locates this classification outside the substrate is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *High-Stakes Decision Identification: The Substrate-Resident Classification Mechanism Driving Reasoning-Layer Pinning in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
