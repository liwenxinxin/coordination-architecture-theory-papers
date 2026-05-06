# Anti-Pattern: LLM Context as Source of Truth — A Standalone Formalization in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one specific failure mode — the configuration in which the LLM's context window during invocation operates as authoritative reference for coordination questions — as a standalone anti-pattern, distinct from the persistent-state anti-pattern that addresses agent memory across invocations and from the broader LLM-content-as-authoritative anti-pattern.

## Abstract

The CKS pattern commits to two architectural properties simultaneously: substrate as the single source of truth for coordination state across five categories, and a determinism contract that requires substrate operations to be deterministic from substrate state alone. This note formalizes a deployment configuration in which both commitments fail through the same operational mechanism — the LLM's context window during invocation operates as the authoritative reference for coordination questions, and context construction is non-deterministic from substrate state. The note states the four operational components that define the anti-pattern, identifies the CKS commitments it violates (substrate-as-source-of-truth, the determinism contract, and the AI-as-substrate-mediator's Property C, all directly), traces the failure mode and its compounding behaviors, specifies the architectural correction that distinguishes legitimate context-as-cell-input patterns from context-as-authoritative-reference, and provides an operational test with three sharpening properties.

## 1. Why standalone formalization is needed

The CKS pattern's substrate-as-source-of-truth commitment names substrate as authoritative for five categories of coordination state ("what is the case," "what is current," "what is in conflict," "what rules apply," "who has what authority"). The determinism contract names substrate operations as deterministic from substrate state, with non-determinism allowed only in narrowly enumerated categories. Both commitments are load-bearing: source-of-truth establishes substrate authority over coordination, and determinism is what makes that authority operationally exercisable.

There exists a deployment configuration in which both commitments fail through the same operational mechanism. In it, coordination questions are answered from the LLM's context window during invocation — the content currently loaded into the LLM's prompt, including system instructions, retrieved RAG content, conversation history loaded into context, prompt-engineered scaffolding, and in-context examples. Substrate may exist in the deployment, but it is not consulted; the authoritative answer is whatever the context-loaded LLM produces.

Standalone treatment is warranted for three reasons. First, the configuration violates two foundational commitments simultaneously. Among the source-of-truth-migration anti-patterns, this one is distinctive: persistent agent memory, hidden cell state, external tool state, and caches each violate the source-of-truth commitment without specifically violating the determinism contract. LLM context as source of truth violates both, because context construction (RAG retrieval, prompt engineering, truncation, history loading, in-context example selection) is non-deterministic from substrate state in ways the determinism contract does not admit. Second, the configuration is operationally common in 2024–2026 RAG-augmented and prompt-engineered deployments; a deployment that uses RAG to "give the LLM relevant context" reads as standard architecture, but the consequence — that retrieved content becomes operationally authoritative when downstream operations consume context-derived answers as ground truth — is rarely named as a foundational-commitment failure. Third, the distinction from the persistent-state-across-invocations anti-pattern (agent memory) must be operationally clean: that anti-pattern addresses state held outside the LLM across invocations, while the within-invocation anti-pattern addressed here is operationally distinct, even though the two commonly compound when persistent memory loads into LLM context.

## 2. The anti-pattern, defined precisely

In the CKS pattern, a deployment exhibits **LLM context as source of truth** when the LLM's context window during invocation operates as the authoritative reference for coordination questions. The anti-pattern has four operational components.

**(a) LLM context loaded with coordination-scope content.** The LLM's context window during invocation contains content within one or more of the five source-of-truth categories — assertions about what is the case, currency markers, conflict states, applicable rules, or authority assignments — arriving through any mechanism: RAG retrieval, prompt-engineered scaffolding, conversation-history loading, in-context examples, or system-instruction injection.

**(b) LLM context consulted as authoritative.** Coordination operations route questions to an LLM whose context contains the relevant content; the LLM's response, derived from that context, is treated as the operational answer. The deployment's reference for "what is the case" is the LLM's response under context, not the substrate's recorded state.

**(c) LLM-context-derived answers winning over substrate.** When LLM-context-derived answers and substrate state disagree, LLM-context-derived answers are operationally trusted; substrate may exist as a record-keeping layer, but it does not arbitrate. This component distinguishes the anti-pattern from a deployment in which the LLM is consulted but substrate remains arbitral.

**(d) Prompt-engineered context as authoritative reference.** Prompt-engineering scaffolding that injects "system instructions," "behavioral rules," or "constraint specifications" into LLM context becomes operationally authoritative for those constraints; the deployment's effective rules are what the prompt scaffolding currently carries, not what the substrate's orchestration-rule layer specifies.

A deployment that exhibits any one of (a)–(d) partially exhibits the anti-pattern; one exhibiting all four exhibits it fully. The boundary against legitimate adjacent patterns — context-as-cell-input, RAG-as-cell-consultation, prompt-engineering-for-cell-behavior, in-context-examples-for-guidance — is treated in §6.

## 3. Which CKS commitments are violated

LLM context as source of truth violates several CKS commitments. The two foundational commitments violated directly are listed first; the cascade follows.

**Substrate as source of truth — directly violated.** The source-of-truth commitment names substrate as authoritative across five categories. LLM context as source of truth fails this commitment by making LLM context, rather than substrate, the operational reference for those categories — most operationally severe at "what is current," because RAG-retrieved content and conversation-history-loaded content most commonly answer currency questions, but applicable to all five wherever context-resident content addresses the category.

**The determinism contract — directly violated, and uniquely so within the source-of-truth-migration cluster.** The determinism contract names substrate operations as deterministic from substrate state, with non-determinism allowed only in narrowly enumerated categories that do not include LLM-context construction. Context construction is non-deterministic in several specific ways: RAG retrieval may select different content across model versions, retrieval configurations, or index updates; prompt-engineering layers may inject different scaffolding based on operational decisions outside substrate; context truncation may drop different content based on token-budget management; conversation-history loading may include different content based on out-of-substrate session state; in-context example selection may rotate or vary across invocations. Each path produces different "authoritative" answers from the same substrate state across invocations, and admitting any of them to the contract's allowed-non-determinism enumeration would mean giving up the contract for any deployment that uses RAG, prompt engineering, history loading, or context-budget management. The required structure is that these paths remain on the cell-reasoning side of the substrate boundary, not on the authoritative-reference side.

Persistent agent memory, hidden cell state, external tool state, and caches each violate the source-of-truth commitment, but none of them, in itself, introduces context-construction non-determinism into authoritative answers. LLM context as source of truth is the cluster member that uniquely violates the determinism contract through the operational mechanism that defines it.

**The AI-as-substrate-mediator's Property C — directly violated.** Property C names that the LLM does not hold substrate-relevant state outside substrate. The LLM's context window during invocation IS substrate-relevant state held outside substrate, by construction, whenever the context contains source-of-truth-category content.

**Path retraceability — extended-implicated.** LLM context content is not substrate-recorded; decisions made on the basis of context cannot be retraced through substrate. The retraceable trail breaks at every context-consultation moment that produces an authoritative answer.

**Human-governed — extended-implicated.** Humans exercising the inspect right inspect substrate; when LLM context is the operational locus of authority, humans inspecting substrate cannot inspect what was in the LLM's context at the moment of authoritative consultation, because context is ephemeral and its construction is non-deterministic.

**Composition requirements — extended-violated.** Where multiple substrates compose, LLM context that aggregates content across substrates and operates as authoritative collapses governance distinctions the substrate layer preserves; per-substrate governance does not extend to LLM context.

## 4. The failure mode

The downstream consequences of LLM context as source of truth are operationally specific.

**Context-construction non-determinism producing different answers across invocations.** Because context construction varies, the same substrate state produces different "authoritative" answers depending on what is in context at the moment of consultation; a coordination question asked twice under unchanged substrate may receive two different answers, neither traceable to a substrate change.

**Prompt injection becoming authoritative.** When LLM context is the operational locus of authority, content injected into context — through adversarial prompt injection, accidental contamination from upstream sources, or unintended content in retrieved RAG documents — becomes authoritative. The substrate-as-source-of-truth commitment, when honored, provides natural defense by requiring rule-governed substrate changes as the only path to authoritative content; the anti-pattern removes that defense.

**RAG-retrieved content as ground truth.** Errors in RAG — retrieval misses, irrelevant retrievals, outdated indexed content, embedding drift across model versions — become errors in authoritative answers. Substrate may carry the correct content; if it is not retrieved into context, it is not authoritative for the operation.

**Hallucinations in context becoming authoritative.** LLMs occasionally produce content that is treated within the same conversation as if it were substrate-grounded. Under the anti-pattern, hallucinations-carried-in-context become authoritative for subsequent operations within the invocation; substrate's record-keeping role does not catch the hallucination because substrate is not consulted as the arbitral source.

**Context truncation and substrate atrophy.** When context exceeds token budgets, truncation drops content; the deployment may operate as if truncated content does not exist, even though substrate carries it. Operational reasoning shifts, often gradually, from "let's check substrate" to "let's ask the LLM"; as fewer operations consult substrate, substrate atrophies as a coordination artifact.

**Recovery requires reconstructing the context.** When operational decisions need review, recovery requires reconstructing what was in the LLM's context at the moment of decision — operationally difficult or impossible, since context construction is non-deterministic, context is ephemeral, and the inputs to context construction are not generally substrate-recorded. Reproducibility under unchanged substrate state, which the determinism contract is structured to preserve, is operationally compromised.

**Compounding with persistent agent memory and with the broader LLM-content-as-authoritative anti-pattern.** When persistent agent memory is loaded into LLM context during invocations, the within-invocation and across-invocation anti-patterns compound: persistent memory provides the durable reservoir of non-substrate authority, ephemeral context the per-invocation surface where it operates. LLM context as source of truth is also the specific instantiation of the broader failure mode in which any LLM-produced or LLM-held content becomes authoritative.

## 5. The architectural correction

The architectural correction operates through three foundational commitments together: substrate as source of truth, the determinism contract, and the AI-as-substrate-mediator's Property C. A deployment that satisfies all three honors the architecture; a deployment drifting on any one drifts toward the anti-pattern.

**Substrate as the operational locus of authority.** All content in the five source-of-truth categories must be substrate-resident and substrate-arbitral. Coordination questions are answered by consulting substrate, not by consulting an LLM whose context happens to contain related content. LLM context during invocation may inform reasoning within a cell, but the operational answer to a coordination question is read from substrate.

**Determinism preservation through substrate-arbitral reads.** Authoritative answers must be deterministic from substrate state. Non-determinism in context construction is therefore tolerable on the cell-reasoning side, where it does not affect what the deployment treats as authoritative, but is not tolerable on the authoritative-reference side. The boundary between the two is the substrate-cell boundary itself.

**Property C preservation through ephemeral-input framing.** LLM context windows during invocation are admissible only as ephemeral inputs to cell reasoning that do not become authoritative. If context becomes authoritative — if downstream operations consume context-derived answers as ground truth — Property C is violated and the configuration becomes the anti-pattern by definition.

A correctly architected deployment treats LLM context as cell-reasoning input rather than authoritative reference: context supplies content the cell uses for reasoning during the invocation; the cell processes the LLM's output and writes substrate state under orchestration rules; the substrate state is the authoritative record, and the context that produced it is ephemeral input. Downstream operations consume substrate state, not LLM context or context-derived content, as their authoritative input.

The distinction between **RAG-as-cell-consultation and RAG-as-source-of-truth** is operationally consequential. Under the cell-consultation pattern, cells consult RAG indexes as adjacent components; the consultation supplies cell-reasoning input under rule mediation, and the cell's output becomes substrate-authoritative. Under the anti-pattern, RAG-retrieved content is operationally authoritative for the questions it addresses, with no substrate arbitration. The correction preserves the first and prohibits the second: RAG remains useful as a consultation pattern that feeds cell reasoning, not as a retrieval pattern that determines authoritative answers. For RAG-augmented deployments that have drifted into the anti-pattern, the correction may require substantive re-architecting — downstream operations must consume substrate state rather than retrieved-content-derived answers.

A correctly architected deployment also maintains a substrate-vs-context audit — examining what downstream operations consume as authoritative input, and whether that input is substrate-resident or context-derived — and treats ephemeral within-invocation context as architecturally distinct from persistent state, since context loaded with content meant to persist (or persistent state held in context-loaders without substrate backing) exhibits a compound of the within-invocation and across-invocation anti-patterns.

## 6. What the anti-pattern is NOT

Four adjacent legitimate patterns are commonly conflated with LLM context as source of truth. Each is a useful pattern in CKS deployments; naming what the anti-pattern is not prevents the misreading that any RAG, prompt-engineering, or context-construction pattern is itself the anti-pattern.

**Not LLM context as input to cell reasoning.** Cells whose LLM context contains content used for reasoning during invocation are legitimate when substrate remains authoritative: the LLM reasons with context as input; outputs become substrate state through rule-governed processing; substrate state is the authoritative record. The anti-pattern arises specifically when context-derived content becomes authoritative downstream.

**Not RAG retrieval as cell-consultation pattern.** The cell-consultation pattern has cells consulting RAG indexes; retrieval supplies cell-reasoning input under rule mediation, and the cell's output is substrate-authoritative. The anti-pattern is different: RAG-retrieved content as authoritative for downstream operations, with no substrate arbitration.

**Not prompt engineering for cell behavior.** Prompt engineering that shapes how the LLM processes inputs within a cell — defining behavior patterns, output formats, processing instructions — is legitimate when applied to cell execution. The anti-pattern is different: prompt-engineered content as authoritative reference for coordination questions, replacing substrate-resident orchestration rules.

**Not in-context examples for cell guidance.** Including examples in the LLM context to guide cell reasoning is legitimate when the examples inform processing rather than define authoritative content. The anti-pattern is different: in-context examples that become authoritative for coordination, where downstream operations consume the example content as ground truth.

The line between legitimate adjacent pattern and anti-pattern, in each case, is the same: whether context-resident content is reasoning input that produces substrate-authoritative output, or is itself the authoritative reference for downstream operations.

## 7. Operational test

A deployment exhibits LLM context as source of truth if any of the following conditions hold at any time during the deployment's existence:

(a) LLM context during invocation contains content in one or more of the five source-of-truth categories;

(b) coordination questions are answered from LLM context — RAG-retrieved content, prompt-engineered scaffolding, in-context examples, conversation history loaded into context — rather than from substrate consultation;

(c) when LLM-context-derived answers and substrate state disagree, LLM-context-derived answers win operationally;

(d) prompt-engineered or RAG-retrieved context is treated as authoritative reference for the deployment's coordination state or rules.

Three sharpening properties further test for the anti-pattern at the level of operational architecture.

**Substrate-vs-context-locus property.** For each downstream operation, identify the input that determines authoritative behavior, and verify that input is substrate-resident. Consultation of LLM context (or context-derived content) rather than substrate indicates the anti-pattern.

**Context-construction-determinism property.** Hold substrate state fixed, run the same coordination operation across invocations, and observe whether the authoritative answer varies. Variation under fixed substrate state indicates context-construction non-determinism affecting authority — the determinism-contract violation specifically.

**Downstream-operations-context-input property.** Trace each operation back to its input and verify that the operation consumes substrate state, not LLM context or context-derived content. Operations consuming context-derived content as authoritative input indicate the anti-pattern.

A deployment that satisfies any of (a)–(d), confirmed by any of the three sharpening properties, exhibits the anti-pattern. The architectural correction in §5 specifies the operational changes required.

## 8. The one-sentence test, and why naming this anti-pattern as standalone matters

If a deployment treats the LLM's context window during invocation — the content currently loaded into the LLM's prompt, including system instructions, retrieved RAG content, conversation history, prompt-engineered scaffolding, and in-context examples — as authoritative for coordination questions, with context-derived answers winning over substrate when conflicts arise and context construction being non-deterministic from substrate state, the deployment exhibits LLM context as source of truth: substrate-as-source-of-truth and the determinism contract both fail through the same operational mechanism, with Property C directly violated and read-determinism specifically compromised by context-construction non-determinism not in the contract's allowed categories.

The reason for naming this configuration as a standalone anti-pattern is that implementations under pressure to deliver RAG-augmented and prompt-engineered AI products consistently default to it. The drift is steady because the audience reads "we use RAG to give the LLM relevant context" as standard architecture without registering the consequence — that retrieved content becomes the operational reference when downstream operations consume context-derived answers as ground truth.

This note is the second of five anti-pattern formalizations addressing source-of-truth migration to non-substrate locations. The persistent-state-across-invocations note treats agent memory; this note treats ephemeral within-invocation context; subsequent notes treat hidden cell state, external tool state, and caches. Together, the cluster will close source-of-truth-migration coverage at the locations where it most commonly occurs operationally.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Anti-Pattern: LLM Context as Source of Truth — A Standalone Formalization in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
