# The Reasoning Layer: An Operational Definition in the Instinct/Reasoning Separation of the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one of the two layers named in the source paper's central architectural separation — the **reasoning layer** — as a precise operational specification, complementing a separate note's formalization of the instinct layer and giving downstream work an unambiguous referent for the term.

## Abstract

The CKS instinct/reasoning separation organizes Paper 2's architectural theory around a precise division: the **instinct layer** is the LLM operating in its bounded mediator role (formalized separately), and the **reasoning layer** is the CKS substrate from Paper 1 — explicit, deliberate, human-governed processing analogous to System 2 cognition. The reasoning layer is not new architecture introduced by Paper 2; it is the substrate Paper 1 already specifies, named in its specifically-functional role within Paper 2's two-layer organization. This note states that operational identity precisely, distinguishes the reasoning layer from the passive-memory framing common in adjacent AI architectures, articulates the cognitive-theory analog (System 2) as conceptual scaffold rather than architectural substance, enumerates the Paper 1 commitments that operationally specify reasoning-layer behavior, and provides an operational test for whether a given system's substrate qualifies as the reasoning layer of a CKS-governed AI Self.

## 1. Why an operational definition of the reasoning layer needs to be formalized

Paper 2's central architectural move is the separation of fast-pattern instinct from deliberate reasoning into independently-evolving layers within one CKS-governed AI Self ("Overview"). The separation rides on two referents — instinct layer and reasoning layer — and the entire claim structure of Paper 2 either establishes structures the separation requires, develops dynamics it enables, or specifies governance that keeps it safe. If either referent is ambiguous, the separation framing degrades: readers cannot tell which layer holds which property, the inheritance from Paper 1 cannot be traced cleanly, and the high-stakes-pinning behavior the separation enables ("instinct/reasoning boundary as governed substrate content") loses operational meaning.

A separate note formalizes the instinct layer. This note formalizes the reasoning layer.

There is a second reason the formalization earns its keep. In the surrounding literature on AI memory systems, vector stores, retrieval-augmented systems, knowledge graphs, and shared agent state, the substrate analog is typically framed as **passive storage** — content the model reads from and writes to, but whose role is to hold state rather than to process it. The CKS reasoning layer is not passive in this sense. It is **active processing** through substrate-resident rules: orchestration rules govern how cells process consultation inputs from the instinct layer to produce substrate writes (Paper 1, §4.1; A2.04). The rules themselves are substrate content, authored by humans, governed under the same authority architecture as everything else the substrate carries. Without an operational specification, the reasoning layer reads as the same thing as those adjacent storage objects, and the architectural property — that processing logic lives in the substrate, not in the LLM — becomes invisible.

## 2. The operational definition

In the CKS instinct/reasoning separation, the **reasoning layer is the CKS substrate from Paper 1**, in its specifically-named role within Paper 2's two-layer architecture.

The identity is precise. The reasoning layer is not a new structure Paper 2 introduces alongside the substrate; it is the substrate as Paper 1 specifies it, named for the function it performs within Paper 2's separation. Every architectural commitment Paper 1 makes about the substrate is a commitment about the reasoning layer. Every operational test Paper 1 provides for the substrate is a test of the reasoning layer.

Operationally, the reasoning layer carries three defining properties.

**(a) Explicit.** Every operation the reasoning layer performs has explicit substrate-state inputs, explicit processing logic, and explicit substrate-state outputs. There is no hidden processing — what the reasoning layer does is what its rules say it does, over the inputs the substrate names, producing the outputs the substrate records. This contrasts with the instinct layer, where pattern-matched responses emerge from learned weights and the intermediate processing is opaque.

**(b) Deliberate.** Reasoning-layer operations follow rules per A2.04 — orchestration rules that specify how cells process inputs to produce outputs. The rules state intended behavior in advance; the operations are not emergent or pattern-recognized but deliberately specified. This is what makes the reasoning layer governable: humans can read the rules, modify them, override their effects, and audit their operation against intent.

**(c) Human-governed.** Every part of the reasoning layer — content and rules alike — is governed under the human-governed commitment from Paper 1 (§2.1, §3.3). Humans hold the right to inspect, modify, and override at all times; the reasoning layer is the substrate, and the substrate is human-governed, so the reasoning layer is human-governed by inheritance, not by separate stipulation.

The reasoning layer's content is enumerated by the source-of-truth categories (A2.42–A2.47): work content, audit history, conflict registry, rules currently applying, and authority distribution. Where Paper 2 introduces additional substrate content beyond Paper 1's enumeration — DNA-layer and Action-layer substrates within every cell ("two layers within every cell"), aspect-coordination rules, harness substrates, Self-integration architecture — those are also reasoning-layer content. The reasoning layer is the union of all substrate-resident authoritative content under Paper 1's and Paper 2's specifications.

## 3. What makes the reasoning layer architecturally distinctive

The reasoning layer is distinctive in two respects the operational definition is meant to make namable.

**Active processing, not passive memory.** Many adjacent AI architectures provide some form of persistent state external to the model — vector stores, knowledge graphs, retrieval indexes, scratchpads, shared agent memory — and call that state the architecture's "substrate" or "memory." In each, the state is passive: it holds content the model reads from and writes to, but the processing logic over that content lives in the model's weights or in code surrounding the model. The CKS reasoning layer reverses the locus. The processing logic — the orchestration rules per A2.04 — is itself substrate content. Humans write rules into the substrate; cells execute them when consulting the instinct layer; the rules' specifications determine what the cells do with the consultation outputs. Reasoning is not a property of the LLM's responses to substrate content; it is what the substrate-resident rules do *with* those responses. The contrast names what the CKS reasoning layer commits to that adjacent passive-memory architectures do not. If the rules lived in the model's weights, the reasoning layer would be inseparable from the instinct layer; the separation would be a vocabulary distinction without an architectural one.

**Identity with Paper 1's substrate makes Paper 1's full specification apply.** Because the reasoning layer is the CKS substrate from Paper 1 in a named role rather than a new architectural object, every commitment, test, and pattern from Paper 1 carries forward without re-specification. Section 5 enumerates the most directly load-bearing inheritances; the broader point is that the reasoning layer is not architecturally new content but Paper 1's substrate operating in Paper 2's named separation. All Series A operational tests apply to it; all Series A anti-pattern formalizations apply to it.

## 4. The cognitive analog as scaffold, not substance

The Paper 2 source frames the reasoning layer as analogous to System 2 cognition in dual-process cognitive theory ("Overview"). System 2 is slow, deliberate, sequential, traceable, and governable; System 1 is fast, parallel, automatic, pattern-matched, and largely opaque. Paper 2 maps the reasoning layer to System 2 and the instinct layer to System 1. The analog functions as a quick-orientation device for readers carrying the dual-process framing — it maps a lot of intuition onto the architecture for free.

The analog is not the architectural substance. The reasoning layer's properties come from its identity with Paper 1's substrate, not from cognitive theory. If the dual-process framing were retracted from cognitive science tomorrow, the reasoning layer's specification would be unaffected — it would still be the CKS substrate from Paper 1, still hold the explicit/deliberate/human-governed properties, still operate through substrate-resident rules, still inherit Paper 1's commitments. The analog earns its place by accelerating reader comprehension; it does not carry architectural weight. This distinction matters for downstream work: implementations that take the cognitive analog as the architectural specification — building "System 2 modules" inside or alongside an LLM — do not necessarily build CKS reasoning layers. The reasoning layer is the CKS substrate operating per Paper 1's specification within Paper 2's separation; the System 2 framing is a conceptual aid, not a build target.

## 5. Inherited Paper 1 commitments operationally specifying the reasoning layer

Because the reasoning layer is the CKS substrate from Paper 1, its substantive operational specification is given by Paper 1's commitments and Series A's formalizations. Several are most directly load-bearing for the separation framing.

The reasoning layer is the **source of truth for coordination state** (A1.08) — what was decided, by whom, under what authority, with what rationale, and what conflicts remain unresolved. The instinct layer's outputs are inputs to reasoning-layer processing; the reasoning layer's writes are authoritative. The three governance rights — **inspect, modify, override** (A1.01) — apply to all reasoning-layer content and all reasoning-layer rules at all times. The reasoning layer sits on the substrate side of the **substrate-cell boundary** (A1.02); cells are the execution units that read from and write to it. **Conflicts are preserved** (A1.03) as first-class reasoning-layer content; cell-level processing resolves them under rules, but substrate-level commitment is to preserve until resolved.

The instinct layer is the AI in its **substrate-mediator role** (A1.04); the reasoning layer is what it mediates over. The reasoning layer is **tool-agnostic** in its host (A1.05) — any environment satisfying the three minimal requirements (persistent structured state, human read/write access, LLM access to substrate content) suffices, and specific substrate technologies are not prescribed. Reasoning-layer state is **deterministic** under appropriate authority (A1.10): the instinct layer's non-determinism does not propagate into reasoning-layer state, because what enters the substrate enters under cell-level processing governed by rules, not under direct LLM write. The **five source-of-truth categories** (A2.42–A2.47) — work content, audit history, conflict registry, rules applying, authority distribution — are all carried in the reasoning layer. **Orchestration rules** (A2.04) are themselves reasoning-layer content, authored by humans (LLM drafting under human authority is admissible; LLM-committed rules outside human authority are not), and are what specify the reasoning layer's deliberate processing.

These are inheritances, not new commitments. Naming them assembled gives the reasoning layer its operational specification by reference rather than by re-statement. Path retraceability (A1.07), linear-cost scaling (A1.06), and the remaining Paper 1 commitments through A1.16 apply equivalently.

## 6. Operational implications

Stating the operational definition has several consequences for how CKS deployments are described, tested, and operated.

**Identification and testability.** A deployment's reasoning layer is whatever it has implemented as its CKS substrate per Paper 1. There is no separate "reasoning layer" component to build alongside the substrate; the substrate is the reasoning layer in its named role within the separation. Deployments seeking to instantiate the instinct/reasoning separation identify their existing CKS substrate as the reasoning layer and the LLM in mediator role as the instinct layer. Reasoning-layer behavior is verifiable through Paper 1's full operational test suite; the Series A operational tests apply without translation.

**Evolution.** The reasoning layer's DNA-layer content evolves through directed selection — human-governed orchestration substrate updates with predictable trajectory, evaluated by intent and outcome together — and through action-feedback — accumulated lived experience driving substrate refinement and DNA refactoring under human mediation. Both mechanisms are distinct from the instinct layer's evolution through mutation (LLM upgrades, infrastructure migrations); the distinction is operationally consequential, because each evolution mechanism is governed in a different shape per Paper 2's "Governance shapes across evolution mechanisms."

**Governance locus and mediation.** Humans inspect, modify, override, and author rules in the reasoning layer. The reasoning layer is what the rights operate on; the instinct layer is governed indirectly, through what the reasoning layer specifies about how its outputs are routed and used. When a cell consults the instinct layer, the consultation output is processed by reasoning-layer rules before becoming substrate state. The instinct layer's output is non-authoritative until the reasoning layer's rules accept it as substrate content.

**Pinning target for high-stakes decisions.** Paper 2's "instinct/reasoning boundary as governed substrate content" specifies that humans can architecturally pin high-stakes decisions to the reasoning layer regardless of how capable instinct becomes. The pinning operation routes such decisions through reasoning-layer rules; bounded behavior follows from substrate-resident rule specification rather than from instinct-layer pattern recognition.

## 7. Limits

Stating what the operational definition does not commit to is what keeps the standalone framing precise.

**Does not include the LLM.** The LLM is the instinct layer (formalized separately). Architectures that locate reasoning logic inside the LLM — chain-of-thought as the model's private sequence, fine-tuned reasoning behaviors, learned planning heuristics — are valuable in their own right but are not the reasoning layer in the CKS sense. The CKS reasoning layer is outside the model; that is what "outside the model" names in Paper 1 and what Paper 2 carries forward in the separation.

**Not optional, not a single component.** Every CKS architecture has a substrate, therefore every CKS architecture has a reasoning layer. A deployment that consists only of an LLM with no human-governed substrate is not a degraded CKS system; it is not a CKS system. The reasoning layer is the union of all substrate-resident authoritative content across cells, aspects, and Selves; it is distributed by architectural design rather than centralized into one store. The operational definition treats the reasoning layer as a single named layer for the purpose of the separation; it does not treat it as a single component.

**Not just memory, but does not exclude LLM consultation.** The reasoning layer is active processing through substrate-resident rules. Naming it "memory" or "context" is a category error in the CKS framing — those names describe a different architectural commitment, where the rules are not in the substrate. At the same time, cells in the reasoning layer routinely consult the instinct layer per the AI-as-substrate-mediator commitment; what makes the processing reasoning-layer processing is that the substrate-resident rules govern how the consultation output is used, not that consultation is absent.

**Does not prescribe specific substrate technologies.** Tool-agnosticism (A1.05) holds. The operational definition does not require knowledge graphs, vector databases, dedicated CKS platforms, or any particular technology stack.

## 8. Operational test

A system's substrate qualifies as the **reasoning layer** of a CKS-governed AI Self under the instinct/reasoning separation if and only if all of the following are true at all times during the substrate's existence:

1. The substrate satisfies Paper 1's full architectural specification — A1.01 (human-governed), A1.02 (substrate-cell boundary), A1.03 (conflict preservation), A1.04 (AI-as-substrate-mediator), A1.05 (tool-agnosticism), A1.06 (linear-cost scaling), A1.07 (path retraceability), A1.08 (substrate-as-source-of-truth), A1.10 (determinism contract), and the remaining commitments A1.09 and A1.11–A1.16.
2. The five source-of-truth categories (A2.42–A2.47) — work content, audit history, conflict registry, rules applying, authority distribution — are all carried in the substrate.
3. Orchestration rules per A2.04 are themselves substrate content, authored by humans, and govern how cells process instinct-layer consultation outputs into substrate writes.
4. The substrate's processing is explicit (every operation has explicit inputs, processing logic, and outputs), deliberate (operations follow specified rules rather than emerging from pattern recognition), and human-governed (inspect/modify/override rights hold over all content and rules).
5. The substrate is the layer to which high-stakes decisions can be architecturally pinned, in the sense that orchestration rules can require a decision to be processed within the substrate rather than relying on instinct-layer behavior alone.

A system that fails any of (1)–(5) does not have a reasoning layer in the CKS sense, even if it has persistent state external to its LLM. Such a system may be useful and may even satisfy adjacent commitments from non-CKS architectures, but its substrate is not the reasoning layer of an instinct/reasoning separation as Paper 2 specifies it.

## 9. Conclusion

Naming the reasoning layer operationally as the CKS substrate from Paper 1, in its specifically-functional role within Paper 2's instinct/reasoning separation, is what gives the separation framing precise architectural content. The reasoning layer is not a new structure Paper 2 invents; it is Paper 1's substrate operating under a name that locates it within Paper 2's two-layer organization. The cognitive-theory analog (System 2) helps readers orient quickly; the architectural substance is the substrate as Paper 1 specifies it. The active-processing-through-substrate-resident-rules property is what distinguishes the reasoning layer from the passive-memory framing in adjacent architectures, and what makes the instinct/reasoning separation an architectural separation rather than a vocabulary one.

This note is the second of approximately six formalizing the decomposition of the instinct/reasoning separation. A separate note formalizes the instinct layer; subsequent notes will formalize the architectural test for separation, the routing patterns for instinct vs. reasoning, the identification of high-stakes decisions, and the verification gates that apply to instinct outputs.

Subsequent work that adopts, extends, or argues against the CKS instinct/reasoning separation should use "the reasoning layer" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Reasoning Layer: An Operational Definition in the Instinct/Reasoning Separation of the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
