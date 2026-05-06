# LLM as Source of Truth: Standalone Formalization of the Anti-Pattern Where LLM-Produced Content Becomes Authoritative for Coordination Questions in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** 6 May 2026  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one architectural anti-pattern — *LLM as source of truth* — as a standalone failure mode that can be defensively published as prior art. The note specifies the four operational components that diagnose the anti-pattern, identifies the foundational CKS commitments it violates, traces the failure mode, names the architectural correction, distinguishes the anti-pattern from four adjacent legitimate patterns commonly conflated with it, and provides an operational test.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern commits to two architectural properties whose joint operation locates coordination authority outside the LLM: AI-as-substrate-mediator (the LLM operates within cells under rules and does not exercise authority over substrate content) and substrate-as-source-of-truth (the substrate is authoritative for the five coordination categories — what is the case, what is current, what is in conflict, what rules apply, and who has what authority). This note formalizes the *LLM as source of truth* anti-pattern: a deployment configuration in which LLM-produced content is treated as authoritative for one or more of those categories, so that downstream operations consult LLM outputs rather than substrate state and the LLM wins when its outputs disagree with substrate. The anti-pattern violates both foundational commitments simultaneously through a single operational mechanism, which makes it the most consequential anti-pattern at the AI-as-substrate-mediator commitment. It is the canonical "context rot" failure named in the source paper (§6.2) and is operationally common in 2024–2026 AI products that position LLMs as knowledge engines or truth oracles. The note states the four operational components that diagnose the anti-pattern, identifies the violated commitments, traces the failure mode, states the architectural correction, distinguishes the anti-pattern from four adjacent legitimate patterns, and provides an operational test with three sharpening properties.

## 1. Why a standalone formalization is needed

The CKS pattern locates coordination authority in the substrate and assigns the LLM a bounded mediator role. AI-as-substrate-mediator (§4.1, §4.2) commits the LLM to operating within cells under orchestration rules, informing reasoning but not exercising authority over substrate content. Substrate-as-source-of-truth (§3.1, §11.3) commits the substrate to being authoritative for the five coordination categories — "what is the case," "what is current," "what is in conflict," "what rules apply," and "who has what authority."

Two further anti-pattern notes formalize related failures of the mediator commitment: an autonomous-agent failure at the *decision* layer (the LLM autonomously decides what to do) and a terminal-producer failure at the *output* layer (LLM outputs flow directly to the substrate without cell mediation). This note formalizes a third, distinct from the other two and architecturally more consequential because it violates substrate-as-source-of-truth at the same time. In a deployment exhibiting this anti-pattern, cells may exist, rule-mediated writes may be in place, and LLM autonomy may be bounded — and yet, when the deployment needs an answer to a coordination question, it reads that answer from LLM-generated content rather than from substrate state.

Standalone formalization is needed for three reasons. The anti-pattern is operationally common in the 2024–2026 AI product landscape, where LLMs are routinely positioned as "knowledge engines" or "single sources of truth"; when these patterns extend to coordination state, they produce the failure this note names. The anti-pattern is also the canonical mechanism for the "context rot" failure the source paper describes (§6.2), where substrate content has been compressed, summarized, or re-embedded out of fidelity with what the substrate actually carries, and the LLM's outputs become the operationally consulted reference. And because the anti-pattern combines two foundational violations through a single configuration, naming it as standalone — distinct from the autonomy and terminal-production failures — gives downstream readers a specification of the failure at the *authority* layer that they can defend against, test for, and remediate.

## 2. The anti-pattern, defined precisely

A CKS deployment exhibits the **LLM-as-source-of-truth** anti-pattern when LLM-produced content is treated as authoritative for coordination questions: when humans, cells, or downstream operations seek answers about "what is the case," "what is current," "what is in conflict," "what rules apply," or "who has what authority," the answer comes from LLM-generated content rather than substrate state. The anti-pattern has four operational components.

**(a) LLM-produced content is treated as authoritative for one or more source-of-truth categories.** Common operational forms include LLM-generated knowledge graph entries treated as authoritative facts; LLM-produced summaries treated as authoritative for historical decisions; LLM-generated entity descriptions treated as authoritative for entity identity; LLM-driven embeddings treated as authoritative for semantic relationships; LLM-produced rule interpretations treated as authoritative for "what rules apply"; LLM-generated authority assignments treated as authoritative for "who has what authority."

**(b) The LLM operates as a "truth oracle" for ambiguous coordination questions.** When substrate state is ambiguous, contested, or silent, the deployment routes the question to the LLM and treats the LLM's answer as authoritative. The LLM is operationally the deployment's oracle for residual coordination cases, even when the substrate is, in principle, the architecture's authority.

**(c) LLM-generated content overrides substrate-resident content when the two disagree.** When LLM-produced content and substrate-resident content disagree, the LLM-produced content wins. The architectural commitment that substrate is authoritative (§11.3) fails specifically at the conflict-resolution moment, with substrate effectively demoted to a record the deployment may not consult.

**(d) Downstream operations consume LLM outputs as authoritative inputs.** Operations that depend on coordination state — decisions, validations, lookups, downstream reasoning — read LLM-generated content as their authoritative input. The LLM's outputs flow into operational pipelines as ground truth, with substrate either bypassed or consulted only as a secondary cross-check.

A deployment that exhibits any one of (a)–(d) partially exhibits the anti-pattern; a deployment exhibiting all four exhibits it fully. The four are operationally inspectable: a reviewer can examine where coordination questions are answered from, what wins when LLM and substrate disagree, what downstream operations read as their inputs, and whether the LLM is positioned as an oracle for residual cases.

## 3. Which CKS commitments are violated

The anti-pattern violates two foundational commitments simultaneously through a single operational configuration.

**AI-as-substrate-mediator (§4.1, §4.2) is violated at the authority layer.** The mediator commitment assigns the LLM a bounded role: operating within cells under orchestration rules, informing reasoning, producing outputs that cells process under rule-mediation to produce substrate state. As one of its constituent properties, the commitment requires that the LLM does not exercise authority over substrate content. LLM-as-source-of-truth violates this property directly: when LLM-produced content is operationally authoritative, the LLM is, by operational fact, exercising authority. The integrating frame for the mediator role is operationally vacated even when its other components (rule-mediated cell processing, attribution, write-under-orchestration-rules) are nominally satisfied, because the authority constraint is the load-bearing element at the authority layer.

**Substrate-as-source-of-truth (§3.1, §11.3) is violated across one or more of the five categories.** The source-of-truth commitment assigns the substrate authoritative status for "what is the case," "what is current," "what is in conflict," "what rules apply," and "who has what authority." LLM-as-source-of-truth fails this commitment by making LLM-produced content authoritative for one or more of the five — and the anti-pattern may operate at any subset, with the most operationally severe forms at "what rules apply" (because rules are themselves substrate content authored by humans as the governance moment) and "who has what authority" (because authority structure is the foundation of the human-governed commitment).

The dual violation is what makes this the most consequential anti-pattern at the AI-as-substrate-mediator commitment. The decision-layer and output-layer mediator failures each violate AI-as-substrate-mediator alone; LLM-as-source-of-truth violates both AI-as-substrate-mediator and substrate-as-source-of-truth through the same mechanism. The two are not co-occurrent violations but two architectural readings of one configuration: the LLM's exercise of authority *is* the substrate's loss of source-of-truth status, viewed from the other side.

The anti-pattern further produces extended implications across foundational commitments that follow as cascade rather than direct mechanism: path retraceability (§3.1) is extended-violated because authoritative content originates from LLM generation rather than substrate state changes; the human-governed commitment (§2.1, §3.3) is extended-implicated because authority lives in LLM outputs that humans cannot inspect, modify, or override at the substrate level; and the determinism contract (§4.1, §11.3) is extended-implicated because LLM-produced authority is non-deterministic — different runs may produce different authoritative content. These cascades are not the primary violation but mark how widely the anti-pattern propagates through the rest of the architecture.

## 4. The failure mode

LLM-as-source-of-truth produces deployments where substrate state nominally exists but is not authoritative. The downstream consequences are operationally specific.

**LLM hallucinations become authoritative content.** Under legitimate cell-mediated processing, LLM-produced content not present in inputs would be substrate-recorded with attribution and could be reviewed or rejected. Under source-of-truth operation, hallucinated content is treated as authoritative; deployment operations consume hallucinations as ground truth, and the architecture has no mechanism to distinguish hallucinated content from substrate-grounded content because the LLM's output is the reference.

**LLM-generated content overrides substrate when they disagree.** When substrate state and LLM output disagree on a coordination question, the operationally authoritative answer is the LLM's. The deployment may have substrate state recording one answer — possibly authored by humans, possibly produced by prior cell-rule transformations — but downstream operations consume the LLM's answer instead. Substrate becomes a record the deployment does not consult.

**Non-deterministic content is presented as deterministic answers.** LLM-as-source-of-truth deployments often present LLM outputs as authoritative answers in structured form — confidence indicators, JSON-formatted responses, knowledge-graph-shaped output. The presentation makes outputs appear deterministic, but the underlying generation is non-deterministic, and the same coordination question may receive different authoritative answers across runs.

**"Single source of truth" framing masks the architectural failure.** Deployment teams and product positioning often describe LLM-as-knowledge-source as a "single source of truth" feature — a positive operational concept borrowed from data architecture. The framing makes the anti-pattern look like operational success and resists architectural correction, because it presents substrate-as-authority and LLM-as-authority as instances of the same desideratum rather than as architecturally opposite configurations.

**The deployment may operate with mismatched authoritative content.** Because substrate continues to exist, the deployment may have substrate state recording one answer while LLM-as-oracle returns another, and the mismatch is operationally invisible — downstream operations consume only the LLM, so the disagreement never surfaces. Recovery from authoritative LLM errors is operationally constrained: identifying that the LLM was wrong requires re-architecting authority back to substrate, a substantial change rather than a localized correction.

The consequences manifest in characteristic form even when the decision-layer and output-layer mediator failures are absent. A deployment with rule-mediated cells and bounded LLM autonomy can still exhibit LLM-as-source-of-truth.

## 5. The architectural correction

The architectural correction operates through the two violated commitments together. The substrate must be restored as the source of truth across all five categories, and the LLM must be restored to a mediator role that does not exercise authority. The two restorations are not independent; they are two readings of the same architectural state.

**Substrate is authoritative across the five source-of-truth categories.** Coordination questions are answered from substrate state, not from LLM outputs. "What is the case," "what is current," "what is in conflict," "what rules apply," and "who has what authority" all resolve to substrate content — regardless of whether that content was originally authored by humans, produced by cells under orchestration rules, or written as the substrate-recorded result of cell-mediated LLM consultation. Substrate residency is what makes content authoritative; the form of its authorship is separable.

**The LLM operates as mediator, not as authority.** LLM outputs inform cell reasoning but are not authoritative for coordination questions. The architectural pipeline is LLM-output → cell-rule transformation → substrate-state-as-authoritative. The LLM's outputs may be substrate-recorded with attribution as part of this pipeline, but LLM-produced content is never the authoritative answer that downstream operations consume.

**Cells process LLM outputs through rules to produce substrate state.** Cells are the architectural locus where LLM outputs are transformed into substrate content. The orchestration rules cells apply determine what becomes substrate content, what is rejected, what is flagged for human review, and what is recorded as a contradiction edge to be preserved as first-class substrate content.

**Coordination questions are routed to substrate, not to the LLM.** Deployment operations that need answers consult substrate. LLMs may inform reasoning during cell execution, render substrate content for human consumption, or help humans compose substrate modifications — none of these uses produce authoritative content.

**LLM outputs are validated against substrate authority where appropriate.** Cells processing LLM outputs may include validation logic that checks LLM outputs against substrate state; substrate-contradicting LLM outputs may be rejected, flagged for human review, or recorded as contradiction edges. The architectural commitment to substrate authority operationally bounds the cell's acceptance of LLM contributions.

**The deployment's authority-locus posture is operationally inspectable.** A reviewer can examine where downstream operations read their authoritative inputs from, what wins when LLM output and substrate state disagree, and whether the LLM is positioned as an oracle for residual coordination questions. The correction is not only architectural but operationally testable, which allows deployments to detect drift back into the anti-pattern over time.

Re-architecting an AI-knowledge deployment back to substrate-authoritative is operationally consequential for systems built around LLM-as-knowledge-engine framings, but the change is what restores both foundational commitments and closes the canonical context-rot failure mode.

## 6. What the anti-pattern is NOT

Four adjacent legitimate patterns are commonly conflated with LLM-as-source-of-truth. Each is a real and reasonable use of LLMs in CKS deployments, and naming what the anti-pattern is not is what prevents the misreading.

**Not LLM as cell-consultation.** A cell may consult an LLM as an adjacent component during its execution — the LLM informs the cell's reasoning, the cell applies orchestration rules to the LLM's output, the result is substrate-recorded with attribution. The cell-consultation pattern is legitimate when the cell remains the architectural primary and the resulting substrate state is authoritative. The anti-pattern arises only when the consultation outputs themselves become authoritative.

**Not LLM-generated derived views that are non-authoritative.** An adjacent component may serve as a derived view of substrate content — a generated summary, a rendered narrative, a search-friendly projection. Such views are legitimate when explicitly non-authoritative: the substrate remains the operational reference, and the derived view is consulted for human convenience or adjacent tooling rather than as ground truth.

**Not LLM as drafting assistant under human direction.** An LLM may produce drafts that humans review and choose to record as substrate content. The human directs what becomes authoritative; the LLM contributes the draft. The pattern is legitimate because authority remains with the human author at the moment of recording. The anti-pattern is the operational treatment of LLM outputs as authoritative *without* human direction at that moment.

**Not LLM as informational presenter.** An LLM may render substrate content for human consumption in natural language, summarize substrate state for human review, or translate substrate content across representations. The pattern is legitimate when the rendering does not become the operationally consulted answer for downstream operations — it serves human reading rather than machine consumption as ground truth.

The four distinctions preserve a wide space of legitimate LLM use within CKS deployments. The anti-pattern is narrow and specific: LLM-produced content is treated as authoritative for coordination questions.

## 7. Operational test

A deployment exhibits the LLM-as-source-of-truth anti-pattern if any of the following are true at any time during the deployment's existence.

1. Coordination questions are answered from LLM-generated content rather than substrate state for one or more of the five source-of-truth categories.
2. The LLM operates as a "truth oracle" for ambiguous coordination questions; its answers are treated as authoritative resolutions.
3. When LLM-produced content and substrate-resident content disagree, the LLM-produced content is treated as authoritative; substrate does not win.
4. Downstream operations (decisions, validations, lookups) consume LLM outputs as authoritative inputs rather than substrate state.

Three sharpening properties make the test operationally executable in deployment review.

**Source-of-truth-locus test.** Identify, for each of the five categories, where downstream operations read their authoritative inputs from. Consultation of LLM outputs rather than substrate for any category indicates the anti-pattern at that category. Conducted by tracing operational dependency chains: for a representative downstream operation, what does it actually read as its authoritative input?

**LLM-vs-substrate-conflict-resolution test.** Construct or identify a case where LLM output and substrate state disagree, and observe what the deployment treats as authoritative. The LLM winning indicates the anti-pattern at the conflict-resolution moment.

**Downstream-operations-authoritative-input test.** Trace the inputs to operationally consequential downstream operations and identify whether they originate from substrate state or from LLM-generated content. The test is operationally distinct from the locus test: the locus test asks where the answer is read from; the consumption test asks what the operation actually does with the input.

A deployment that satisfies any of (1)–(4) and any of the three sharpening properties exhibits the anti-pattern. The architectural correction stated in §5 specifies the operational changes required.

The one-sentence form, for reviewers needing rapid classification: if a deployment treats LLM-produced content as authoritative for coordination questions and the LLM wins when LLM and substrate disagree, the deployment exhibits LLM-as-source-of-truth, and the foundational commitments to AI-as-substrate-mediator and substrate-as-source-of-truth both fail through the same operational mechanism.

## 8. Conclusion

Implementations under pressure to deliver AI products with knowledge or reasoning capabilities consistently default to LLM-as-source-of-truth because LLMs are positioned as "knowledge engines" or "AI single sources of truth" in the surrounding product landscape. The drift is steady because the framing makes it look like standard AI architecture without surfacing the architectural consequence — that the substrate ceases to be the source of truth and the foundational AI-as-substrate-mediator and substrate-as-source-of-truth commitments fail through a single configuration.

Naming LLM-as-source-of-truth as a standalone anti-pattern gives downstream readers a precise specification of the failure and its correction. Together with the decision-layer and output-layer formalizations of mediator failure, this note completes the architectural coverage of the AI-as-substrate-mediator anti-pattern landscape at three layers: decision, output, and authority. It also opens the substrate-as-source-of-truth anti-pattern cluster, where subsequent notes formalize specific instantiations of source-of-truth migration to non-substrate locations — agent memory, LLM context, hidden cell state, external tools, caches — each of which produces the canonical context-rot failure (§6.2) in its own way.

Subsequent work that adopts, extends, composes with, or argues against the CKS pattern should use "LLM as source of truth" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *LLM as Source of Truth: Standalone Formalization of the Anti-Pattern Where LLM-Produced Content Becomes Authoritative for Coordination Questions in the Coordination Knowledge Substrate Pattern.* 6 May 2026. ORCID: 0009-0004-8065-3235.
