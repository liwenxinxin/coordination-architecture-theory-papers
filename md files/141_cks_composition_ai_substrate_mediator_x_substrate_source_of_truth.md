# Mediation Without Authority Migration: The Composition of AI-as-Substrate-Mediator and Substrate-as-Source-of-Truth in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 6 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the architectural property that emerges when two of the source paper's foundational commitments — AI-as-substrate-mediator and substrate-as-source-of-truth — compose, and to articulate that property as a standalone derivation citable independently of either commitment.

## Abstract

Two of the CKS pattern's foundational architectural commitments — AI-as-substrate-mediator (§4.2) and substrate-as-source-of-truth (§11.3) — produce, when they hold simultaneously, an emergent architectural property that neither yields alone. This note formalizes that property as *AI-mediated authority preservation*: the architectural pattern in which AI mediation specifically preserves authority on substrate across all five categories of authoritative coordination state, even in deployments where AI operations dominate cell-level work. The property is operationally what makes vendor-provided AI architecturally acceptable in CKS: vendor AI processes substrate state without becoming substrate or assuming substrate's authoritative role. The note states the property in four operational components, identifies what the composition forces beyond either commitment in isolation, names four classes of anti-pattern that violate the composition while individual commitments may appear satisfied, distinguishes the composition from four adjacent architectural patterns commonly conflated with it, and provides an operational test with three sharpening properties.

## 1. Why the composition pair needs to be formalized as standalone

The CKS pattern's AI-as-substrate-mediator commitment specifies that the LLM operates within five properties governing reads, writes, state-locality, authority-non-exercise, and write-attribution. The substrate-as-source-of-truth commitment specifies that the substrate is authoritative for five categories of coordination state — what is the case, what is current, what is in conflict, what rules apply, and who has what authority. Each commitment is independently load-bearing and has its own decomposition in the source paper.

What the source paper develops, but does not formalize as a standalone architectural property, is the *joint* commitment that arises when both hold at once. AI-as-substrate-mediator alone is satisfiable by deployments in which the LLM operates in mediator-shape over a store — reading from it, writing under rules — without that store being the source of truth in the §11.3 sense. Substrate-as-source-of-truth alone is satisfiable by deployments in which the substrate is authoritative but the AI participates in some non-mediator role: as autonomous agent, as terminal producer, or as source of truth for a subset of coordination questions. Neither commitment, taken alone, forces the architectural pattern in which AI operations occur with substrate-as-authoritative-primary at every step. The composition does.

The property the composition produces is what operationally permits vendor-provided AI in a CKS deployment. The architectural concern any 2024–2026 AI deployment must address is whether using a vendor LLM means the LLM becomes the source of truth — a concern raised by vendor memory features, agent-state APIs, and stateful chat surfaces. The composition answers no: the AI's role is bounded by mediator constraints on a substrate that holds authoritative state. Without naming the composition as a standalone derivation, this acceptability property is implicit in the foundational commitments rather than architecturally specified. The sibling Phase A4 notes formalize four other foundational composition pairs covering governance, AI-rule-mediation, authority-locus, and AI-accountability; the present note completes the foundational set by formalizing how AI mediation operates with substrate as authoritative primary across all five categories of coordination state.

## 2. The emergent property, in four operational components

In a deployment satisfying both foundational commitments simultaneously, AI mediation preserves authority on substrate through four operational components. All four must hold for the composition to be satisfied.

**Component 1 — Substrate-primary reads across all five categories.** When the LLM consults state to perform a cell operation, the read targets substrate as primary source for any coordination question. The five categories of authoritative coordination state — what is the case, what is current, what is in conflict, what rules apply, who has what authority — are each read from substrate, not from a vendor cache, an external knowledge base, an embedding store, or training-time parametric memory. In-context information not drawn from substrate is admissible only insofar as it does not serve as a substitute for substrate state the operation depends on.

**Component 2 — Rule-mediated writes under substrate-resident rules.** When LLM activity results in changes to authoritative state, the change occurs through a cell operating under an orchestration rule, with the orchestration rule itself living in substrate as authoritative content. The cell-rule-write chain operates with rules as authoritative input, not as configuration external to the substrate. Rules that live in vendor configurations, deployment manifests, prompt templates outside the substrate, or runtime middleware do not satisfy this component, because they are not substrate-resident authoritative content.

**Component 3 — No authority exercise by the LLM.** The LLM does not make authoritative decisions. Every change to authoritative coordination state results from a rule-mediated substrate write, not from an LLM decision treated directly as the answer to a coordination question. LLM outputs are inputs to cells; cells under rules write substrate; the rules — not the LLM — determine what becomes authoritative. Authority is exclusively a property of substrate state, never of LLM decisions.

**Component 4 — No substrate-relevant state in LLM-internal stores.** The LLM does not hold substrate-relevant state outside substrate. LLM context, agent memory, embedding stores, per-session caches, or any other LLM-internal state cannot hold content that is substrate-relevant and is treated as authoritative across operations. Authority cannot migrate to LLM-internal state regardless of the technical sophistication of the holding mechanism. Substrate-relevant state lives in the substrate.

A deployment that exhibits all four components exhibits AI-mediated authority preservation; a deployment failing any of the four fails the composition, even if the individual commitments are nominally satisfied in isolation.

## 3. What the composition forces beyond either commitment alone

The mediator commitment alone leaves open whether the substrate the LLM mediates over is itself authoritative — the LLM may operate in mediator-shape over a vendor cache, a search index, or a derived projection. The source-of-truth commitment alone leaves open how the LLM participates in authoritative state — the LLM may operate as autonomous agent, terminal producer, or source of truth for some subset of coordination questions. Neither commitment alone forces the joint configuration in which AI operations occur with substrate-as-authoritative-primary at every step.

The composition closes both openings. It forces the following architectural decisions jointly:

- LLM reads must target substrate, *and* substrate must be authoritative for what is read. Reads from non-authoritative stores fail the composition even if the LLM is otherwise mediator-shaped.
- LLM writes must occur under rules, *and* the rules must themselves be substrate-resident authoritative content. Configuration-as-rules architectures fail the composition even if substrate is authoritative for non-rule content.
- Authority must be exclusive to substrate, uniformly across all five categories of coordination state. Hybrid-authority architectures, in which the LLM is authoritative for some questions while substrate is authoritative for others, fail the composition because authority is partially migrated.
- LLM-internal state must remain non-authoritative. Architectures that treat LLM context, agent memory, or embedding state as authoritative for what was decided or what is current fail the composition even if a substrate exists in parallel.
- Vendor-portability is preserved as a structural consequence. Because authority sits with substrate and AI is mediator, vendor AI can be substituted without architectural change to authority distribution.

The architectural shape forced by the composition is therefore stricter than either commitment alone: a joint configuration of substrate-side authority and LLM-side mediator role that holds uniformly across all five categories of coordination state.

## 4. Anti-patterns that violate the composition

Some violations of the composition leave the individual commitments nominally intact and become visible only when the joint property is checked. Naming them by class makes the joint failure mode addressable at design-time review.

**Authority-exercise violations.** The composition is most directly violated when the LLM exercises authority on coordination questions. The canonical case is the LLM operating as source of truth for some category of coordination state — answering "what was decided" or "who has what authority" from in-LLM state rather than from substrate. Adjacent cases include autonomous-agent architectures in which reasoning across steps yields authoritative coordination decisions without rule-mediation, and architectures in which LLM classifications are treated as authoritative substrate content directly rather than as inputs to a rule-governed cell. In each case the mediator commitment may be partially satisfied (the LLM is mediator-shaped on some operations) and the source-of-truth commitment may be partially satisfied (substrate exists for some content), but the composition fails because authority is exercised somewhere other than at the rule-mediated substrate-write boundary.

**Output-layer violations.** The composition is violated when LLM outputs flow to substrate or to downstream systems that treat them as authoritative without rule-mediated transformation. The terminal-producer pattern — LLM produces an artifact, the artifact is the deliverable, downstream systems consume it as authoritative — fails the composition because the cell-rule-write chain is bypassed. Authority is conferred at the LLM-output layer rather than at the rule-mediated-substrate-write layer. The substrate may still hold the LLM output for the record, but the architectural primary for downstream consumption is the LLM's output.

**Cell-side and ephemeral authoritative-content violations.** The composition is violated when authoritative coordination state lives in LLM-internal or cell-internal stores rather than in substrate. The two principal cases are agent memory holding authoritative content across LLM invocations, and LLM context holding authoritative content within an invocation. Both are architecturally distinct from substrate writes and cannot be inspected, modified, or overridden through the substrate's governance interface. The composition fails on Component 4 because authority has migrated to LLM-internal or cell-internal state, and on Component 1 because subsequent operations read from those stores as primary source rather than from substrate.

**Architectural-replacement violations.** The composition is violated most severely when the substrate is replaced by an AI-driven adjacent component as the architectural primary: a retrieval-augmented store treated as the source of truth, a vector database treated as substrate, a context window treated as the persistent coordination artifact, or an opaque agent memory treated as the architectural primary. The source-of-truth commitment fails entirely because no human-governed substrate exists as architectural primary, and the mediator commitment fails because the LLM cannot operate as mediator on a non-existent substrate. These are architectural replacements rather than failures within an otherwise-intact architecture; they are named here because the surface presentation of an AI-driven coordination architecture can be confused with a CKS deployment in which AI is mediator on substrate.

## 5. What the composition is NOT

Four adjacent architectural patterns are commonly conflated with AI-mediated authority preservation and should be distinguished.

**Not mediator-without-authority-specification.** Architectures in which the LLM operates in mediator-shape over a store without specifying that the store is authoritative do not satisfy the composition. Mediation without authority-substrate-coupling is a useful pattern for some purposes; it is not the composition this note formalizes.

**Not partial-authority hybrids.** Architectures in which substrate is authoritative for some coordination questions while the LLM is authoritative for others — for example, substrate authoritative for what was decided while the LLM is authoritative for intent classification — do not satisfy the composition. The composition forces authority-on-substrate uniformly across all five categories. Partial authority is a form of authority migration, not partial satisfaction of the commitment.

**Not AI-augmented-with-auto-apply.** Architectures in which AI suggestions auto-apply to substrate without rule-mediation do not satisfy the composition, even if a human can later inspect and revert. The composition forces rule-mediation per the mediator commitment's second property — AI suggestions are inputs to cells; cells under rules write substrate. Auto-apply confers authority at the LLM-output layer, regardless of post-hoc inspection capability.

**Not authority-with-explanations.** Architectures in which the LLM exercises authority but provides explanations for its decisions do not satisfy the composition. Explanation is not the same architectural property as authority-non-exercise. The composition's third component is that the LLM does not exercise authority; explanations of LLM authority decisions are an explainability property layered on a different architecture.

## 6. Why naming the composition matters

The composition is the architectural answer to "how does AI participate in coordination without disrupting authority?" — through mediation on substrate-as-authoritative-primary, with the four components of §2 holding jointly across all five categories of coordination state. Several downstream architectural properties depend on this answer.

Vendor-portability follows from the composition: because authority is on substrate and AI is mediator, the deployment can substitute AI vendors without architectural change to authority distribution. The composition makes this property a structural consequence of the architecture rather than a contingent property of vendor compatibility. The composition also distinguishes CKS from AI-driven coordination architectures, in which the AI is the architectural primary and any persistent store is incidental — CKS treats substrate as primary with AI as mediator, and the composition specifies this distinction at the operational level of reads, writes, state-locality, and authority-locus.

The composition produces a named class of joint-failure anti-patterns. The authority-exercise, output-layer, cell-side, and architectural-replacement violations of §4 are joint failures, not failures of either commitment alone. Naming them as composition failures gives reviewers a precise vocabulary for design-time critique that individual-commitment review does not provide. The composition is also detectable through architectural review: the four operational components and the three sharpening properties of §7 are inspectable in a deployed system, which makes the composition a usable acceptance criterion for deployments that wish to claim CKS-coherence.

## 7. Operational test

A deployment satisfies the composition of AI-as-substrate-mediator and substrate-as-source-of-truth if and only if all of the following hold for every LLM operation in the system, at all times during the deployment's existence.

1. LLM reads target substrate as primary source for all five categories of coordination state — what is the case, what is current, what is in conflict, what rules apply, who has what authority.
2. LLM writes occur through cell-rule mediation, with the orchestration rules under which the cell operates being substrate-resident authoritative content rather than configuration external to the substrate.
3. The LLM does not exercise authority over coordination state; every change to authoritative state results from a rule-mediated substrate write, not from an LLM decision.
4. The LLM does not hold substrate-relevant state outside substrate; LLM context, agent memory, embedding state, and other LLM-internal stores are ephemeral and non-authoritative.
5. LLM outputs that affect substrate state are recorded with attribution that traces to the substrate state read at cell-execution time and to the orchestration rule under which the cell operated.

Three sharpening properties make the test operationally exercisable in a deployed system rather than only at design time.

*Substrate-primary-read property.* For each LLM consultation that addresses a coordination question, the read targets substrate as primary source. Reads of non-substrate primary sources for coordination questions — vendor APIs treated as authoritative, external knowledge bases treated as primary, training-data parametric memory treated as the answer — indicate composition failure.

*LLM-authority-absence property.* Every authoritative-state change traces to a rule-mediated substrate write. Changes that result from LLM decisions without rule-mediation, LLM classifications used directly as substrate content, or LLM outputs auto-applied to substrate indicate composition failure.

*LLM-state-locality property.* LLM-internal state — context, agent memory, embedding state — does not hold substrate-relevant content treated as authoritative across operations. Presence of substrate-relevant authoritative content in LLM-internal stores indicates composition failure regardless of the technical sophistication of the holding mechanism.

A one-sentence test summarizes the joint property: if a deployment's LLM operations read substrate as primary source for the five categories of coordination state, write under rules that themselves live in substrate as authoritative content, do not exercise authority over coordination state, and do not hold substrate-relevant authoritative state outside substrate, the deployment satisfies the composition — the emergent architectural property is AI-mediated authority preservation, with vendor-provided AI architecturally acceptable because AI operates as mediator on substrate-as-authority.

A deployment that fails any of (1)–(5) or any of the three sharpening properties may instantiate some other architectural composition, but does not implement AI-mediated authority preservation in the CKS sense.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Mediation Without Authority Migration: The Composition of AI-as-Substrate-Mediator and Substrate-as-Source-of-Truth in the Coordination Knowledge Substrate Pattern.* 6 May 2026. ORCID: 0009-0004-8065-3235.
