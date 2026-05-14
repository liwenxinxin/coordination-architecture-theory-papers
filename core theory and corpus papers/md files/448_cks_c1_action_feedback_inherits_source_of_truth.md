# Action-Feedback Evolution Inherits Paper 1's Substrate-as-Source-of-Truth

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its contribution is to show that Paper 2's action-feedback evolution mechanism inherits Paper 1's substrate-as-source-of-truth commitment — that the evolution loop's evidence pipeline closes through authoritative substrate records, that no stage of the loop exits to ungoverned external sources, and that the proposing substrate, as a new architectural component, is made possible by Paper 1's source-of-truth commitment while extending it with new structure. This note also closes the three-evolution-mechanism inheritance triple established by C1.17 and C1.18.

## Abstract

Paper 2 introduces action-feedback as a third evolution mechanism for CKS Selves, operating alongside mutation (instinct evolution) and directed selection (DNA evolution). Action-feedback closes the loop from accumulated operational experience back into governed substrate refinement: recorded action evidence is evaluated by a proposing substrate, which generates improvement proposals for governance review and, upon approval, implementation as directed selection events. This note formalizes the inheritance edge: Paper 2's action-feedback evolution mechanism inherits Paper 1's substrate-as-source-of-truth commitment (A1.08) because the entire four-stage loop — accumulation, evaluation, review, implementation — operates on substrate content and never exits the governance boundary. The Action layer, which holds the loop's evidence, is the substrate's own operational record; using it as the evidence source directly applies Paper 1's principle that the substrate is the authoritative answer to operational questions. What is new in Paper 2 is the proposing substrate as evidence-to-proposal mechanism, the two-stage governance review structure, the indirection between evidence and implementation, and governance over the evidence window the proposing substrate evaluates. With this edge formalized, the three-evolution-mechanism inheritance triple (C1.17 through C1.19) is complete: each of Paper 2's three evolution mechanisms inherits a distinct Paper 1 commitment, and together they cover the full inherited architecture of CKS evolution.

## 1. This note's position in the inheritance triple

Paper 2 introduces three evolution mechanisms for CKS Selves. Instinct evolution — undirected capability change arriving through LLM upgrades and infrastructure upgrades — was addressed in C1.17, which formalized the inheritance from Paper 1's tool-agnosticism commitment: the LLM and substrate platform are the host layer, and instinct evolution operates by replacing or upgrading that layer from outside the Self's governance boundary. DNA evolution — directed selection on the substrate's orchestration content under governance-defined goals — was addressed in C1.18, which formalized the inheritance from Paper 1's human-governed commitment: changes to DNA-layer content exercise exactly the modify right Paper 1 requires humans to hold at all times.

This note addresses the third mechanism: action-feedback evolution. The inheritance target is Paper 1's substrate-as-source-of-truth commitment (A1.08). The claim formalized here is that action-feedback inherits this commitment because the mechanism's evidence pipeline is built on the substrate's authoritative operational record — the loop cannot function otherwise, and the way it functions directly applies Paper 1's source-of-truth principle to the evolution context.

Formalizing this edge closes the triple. C1.17, C1.18, and C1.19 together establish that each of Paper 2's three evolution mechanisms is grounded in a distinct Paper 1 commitment, and that none of the three is an independent invention disconnected from Paper 1's architecture. Section 6 restates the triple explicitly.

## 2. Paper 1's substrate-as-source-of-truth commitment

Paper 1 commits the substrate to being the authoritative answer to coordination questions — specifically: what was decided, by whom, under what authority, with what rationale, and what contradictions remain unresolved (§11.3 of Paper 1). This is not a generic claim that all state in an operating environment lives in the substrate; it is a precise claim about which state the system treats as authoritative for coordination questions.

Several adjacent commitments depend on this one. Path retraceability requires that the trace run through authoritative content; it is meaningless if the substrate is not where the answer actually sits. The AI-as-mediator commitment — that LLMs operate over substrate content as mediators rather than as autonomous actors — presupposes the substrate is what the LLM operates over. The anti-pattern most directly opposed to A1.08 is agent memory as source of truth (A3.14): a system in which LLM context or agent memory is treated as the authoritative record of what happened violates Paper 1's Claim 4 and the source-of-truth commitment directly.

Paper 1 also commits that all LLM outputs affecting coordination state are recorded in the substrate with attribution (AI-as-mediator Property E). This means the substrate holds not only governance decisions but also the operational record of what the LLM did: tasks executed, outputs produced, coordination state affected. These recorded task instances are part of the five categories of authoritative state the substrate holds. The substrate is therefore the authoritative record of what actually happened operationally — not LLM context, not external logs, not agent memory.

## 3. Paper 2's action-feedback evolution: the four-stage pipeline

Paper 2 introduces action-feedback as the mechanism by which accumulated operational experience closes back into governed substrate refinement. The mechanism operates in four stages.

**Stage 1 — Accumulation.** Normal cell operation produces action-layer records: task executions, outputs, patterns of usage, efficiency observations, and anything else in scope under the governing orchestration rules. These records are substrate content — they are written to the substrate under cell mediation with attribution, per Paper 1's AI-as-mediator Property E and the source-of-truth commitment. Over time they accumulate as the substrate's authoritative operational history.

**Stage 2 — Evaluation.** A proposing substrate reads from the Action layer — the substrate's accumulated operational records — and generates improvement proposals. The proposing substrate is a new architectural object introduced by Paper 2: a substrate component whose function is to reason about patterns in the Action layer evidence and produce structured proposals for DNA improvements (scope refinements, orchestration optimizations, refactorings informed by lived inefficiency). The proposing substrate does not reason from LLM context, from agent memory, or from any source external to the substrate. Its evidence source is the Action layer content the substrate holds authoritatively.

**Stage 3 — Human governance review.** The proposals generated at Stage 2 are presented to human governance for decision. Humans hold authority to accept, reject, modify, or defer each proposal. The proposals are reviewed as governance artifacts — they are substrate content, attributed to the proposing substrate that generated them, reviewable as such. The governance decision at Stage 3 is a direct exercise of the modify and override rights Paper 1 requires humans to hold at all times.

**Stage 4 — Implementation as directed selection.** Approved proposals are implemented as directed selection events on the DNA layer — exactly the mechanism C1.18 addressed. The implementation is an authorized, human-approved substrate edit. Rejected proposals are archived or discarded; they do not affect DNA content without governance approval.

The loop runs: accumulation (substrate writes) → evaluation (substrate reads by proposing substrate) → review (human governance decision) → implementation (substrate edit under authority). No stage of this pipeline exits the substrate governance boundary. No stage reads from or writes to an ungoverned external source. The evidence is substrate content; the proposals are substrate content; the implementation is a substrate edit; the authorization is a human governance act over substrate content.

## 4. What is inherited: source-of-truth identity preserved

Four properties of Paper 1's source-of-truth commitment are directly inherited by the action-feedback mechanism.

**Substrate as authoritative evidence.** The Action layer is the substrate's operational record. Using it as the evidence source for improvement proposals does not introduce a new relationship between evidence and substrate — it applies Paper 1's source-of-truth principle directly. The system reasons about operational history from the authoritative record, not from ephemeral or derivative sources. If the Action layer content and any other source (LLM context, external logs, agent memory) disagree, the substrate content is authoritative by Paper 1's commitment. The action-feedback mechanism inherits this: the proposing substrate reasons from authoritative content, not from whatever the LLM happens to remember.

**No LLM memory as evidence source.** Anti-pattern A3.14 — agent memory as source of truth — is the canonical violation of Paper 1 Claim 4 and A1.08. An action-feedback mechanism that derived improvement proposals from LLM context or agent memory would instantiate this anti-pattern directly: it would treat ephemeral, non-attributed, non-persistent state as authoritative for proposing changes to the substrate's governance structure. Paper 2's mechanism forecloses this: the proposing substrate reads the Action layer, not LLM context. The source-of-truth commitment is inherited precisely because the mechanism is built against the anti-pattern.

**Operational history as governance artifact.** Action layer records are authoritative governance artifacts under Paper 1's attribution commitment. They are attributed (written by identified cell executions), traceable (path retraceability applies to them), and persistent (substrate writes are durable, not ephemeral). The proposing substrate at Stage 2 therefore reasons from governance-grade evidence — the same quality of evidence Paper 1 commits the substrate to holding. The action-feedback mechanism does not introduce a lower-quality evidence tier; it reasons from the substrate's own authoritative record.

**Loop closure within the governance boundary.** Paper 1 commits the substrate to being the place where coordination questions are answered and coordination state is held. The action-feedback loop's closure within the governance boundary is the evolution-context application of this commitment: the loop does not consult sources outside the boundary, does not write to locations outside the boundary, and does not implement changes without traversing the governance decision at Stage 3. The boundary remains what Paper 1 defines it to be.

## 5. What is new in Paper 2

Four structural additions distinguish Paper 2's action-feedback mechanism from anything expressly present in Paper 1.

**Proposing substrates as a new architectural object.** Paper 1 commits the substrate to holding authoritative operational records and requires LLMs to operate over substrate content as mediators. It does not introduce a substrate component whose specific function is to read Action layer evidence and generate structured improvement proposals. The proposing substrate is a new architectural object: a substrate that reads from the operational record layer and produces structured output in the form of governance-reviewable proposals. Its existence is enabled by Paper 1's source-of-truth commitment — there is an authoritative record worth reading — but the proposing-substrate pattern itself is new in Paper 2.

**Two-stage governance review.** Paper 1's governance commitment establishes that humans hold the rights to inspect, modify, and override substrate content and orchestration rules at any time. It does not specify a structured two-stage review sequence for evidence-derived improvement proposals. Paper 2 introduces this structure: Stage 2 (proposing substrate evaluation, producing proposals) and Stage 3 (human governance decision on those proposals) as a named, sequenced review process. The two-stage structure makes the governance work visible and auditable as a governance process, not just as an exercise of the modify right.

**Indirect evolution: evidence does not automatically become implementation.** In the action-feedback mechanism, evidence does not directly produce DNA changes. The chain is: evidence → proposal → governance decision → directed selection event. This indirection is architecturally deliberate and is new. It means that even a very clear pattern in the Action layer — strong evidence that a particular DNA change would improve performance — does not cause that change without traversing the governance decision at Stage 3. The loop is governed at the point of transition from evidence to implementation, not just at the implementation step.

**Evidence window governance.** Governance specifies what portion of the Action layer the proposing substrate evaluates: recent operational history, longer historical windows, per-LLM-version evidence, cross-version evidence. This configurability over the evidence window is a new governance surface introduced by Paper 2. It means that the action-feedback mechanism's sensitivity — how much operational history it draws on, which historical periods it weights — is itself a governance decision, not an internal parameter of the proposing substrate.

## 6. Closing the three-evolution-mechanism triple

With C1.19, the three-evolution-mechanism inheritance triple is complete. The three notes together establish that Paper 2's full three-mechanism evolution architecture inherits, rather than replaces, Paper 1's foundational commitments, with each mechanism inheriting a distinct Paper 1 property.

**C1.17 — Mutation (instinct evolution) ⊃ Paper 1 tool-agnosticism.**
Instinct evolution arrives through LLM upgrades and substrate-platform infrastructure upgrades — external changes to the host layer. Paper 1 commits to tool-agnosticism: the LLM and substrate platform are replaceable, and the governance commitment does not depend on any specific tool. Instinct evolution inherits this directly: the LLM is the replaceable host, and instinct evolution is the mechanism by which that replacement or upgrade is governed and integrated. The inheritance relationship is: the undirected-mutation character of instinct evolution is possible because the host layer is architecturally external and replaceable, which is exactly what Paper 1's tool-agnosticism commits to.

**C1.18 — Directed selection (DNA evolution) ⊃ Paper 1 human-governed.**
DNA evolution operates on the substrate's orchestration content — schemas, rules, orchestration patterns — under explicit goals defined by human governance. Paper 1 commits that humans hold the rights to inspect, modify, and override substrate content and orchestration rules at any time. DNA evolution inherits this directly: it is an exercise of the modify right at DNA scope, with selection criteria themselves authored and maintained as substrate content under human authority. The inheritance relationship is: directed selection on the governance substrate is precisely what Paper 1's human-governed commitment enables and requires.

**C1.19 — Action-feedback evolution ⊃ Paper 1 substrate-as-source-of-truth.**
Action-feedback evolution uses the Action layer — the substrate's authoritative operational record — as the evidence source for generating improvement proposals. The loop closes through the substrate: accumulation to the substrate, evaluation from the substrate, review of substrate content, implementation as a substrate edit. Paper 1 commits that the substrate is the authoritative answer to operational questions and that agent memory is not. Action-feedback inherits this directly: the mechanism is built on the authoritative substrate record and forecloses the anti-pattern of reasoning from ephemeral agent memory. The inheritance relationship is: action-feedback's evidence pipeline is possible and coherent because Paper 1 already commits the substrate to holding authoritative operational records.

The triple is exhaustive with respect to the three evolution mechanisms Paper 2 introduces. Each mechanism has a named Paper 1 parent commitment. No mechanism is architecturally free-floating.

## 7. Operational test

A system implements the C1.19 inheritance edge — action-feedback evolution that inherits Paper 1's substrate-as-source-of-truth commitment — if and only if all of the following are true.

1. **Evidence traceability.** For any improvement proposal generated by the action-feedback mechanism, an observer can identify the specific Action layer records from which the proposal was derived, and can confirm that those records are substrate content — attributed, persistent, and present in the substrate rather than in LLM context or agent memory.

2. **No external evidence source.** The proposing substrate does not read from any source outside the substrate's governance boundary when generating proposals. Any information informing a proposal is either substrate content (Action layer records or other substrate content) or derives from substrate content through a governed read.

3. **Governance gate before implementation.** No improvement proposal derived from Action layer evidence is implemented as a DNA change without traversing human governance review at Stage 3. Implementation requires explicit governance approval; evidence alone does not authorize a substrate edit.

4. **Loop boundary integrity.** The four stages of the action-feedback pipeline (accumulation, evaluation, review, implementation) all occur within the substrate governance boundary. No stage exits to an ungoverned external system for evidence, review, or implementation authority.

A system in which a proposing component reads from LLM context rather than the Action layer, or in which action-derived proposals are automatically implemented without governance review, does not implement the C1.19 inheritance edge, regardless of whether it calls the mechanism "action-feedback."

## 8. Prior-art significance

This note forecloses three families of adversarial claims.

First, it forecloses claims that using operational substrate records as evidence for improvement proposals is a novel contribution relative to Paper 1's source-of-truth commitment. Paper 1 commits the substrate to holding authoritative operational records (recorded task instances as one of the five categories of authoritative state). That Paper 2 uses those records as evidence for improvement proposals is an application of Paper 1's source-of-truth commitment, not a departure from it or an independent invention over it.

Second, it forecloses claims that proposing substrates as evidence-evaluation components are novel architectural objects without prior-art grounding. The proposing substrate is a new architectural object, but its novelty is bounded by Paper 1's source-of-truth commitment: it is a new pattern for reading from an already-committed authoritative substrate. Its novelty does not extend to the claim that authoritative substrate content is a legitimate evidence source for operational review — that claim is Paper 1's.

Third, it forecloses claims that evidence-based evolution loops closing through the substrate are novel relative to Paper 1's operational record commitments. The loop-closure-through-substrate property of action-feedback is directly enabled by Paper 1's commitment that the substrate holds the authoritative operational record. A party claiming novelty over this property would need to argue over a gap that Paper 1 already closed.

## Conclusion

Paper 2's action-feedback evolution mechanism inherits Paper 1's substrate-as-source-of-truth commitment in a direct and load-bearing way. The mechanism's evidence pipeline is built on the substrate's own authoritative operational record; the loop closes through the substrate at every stage; no stage exits to ungoverned external sources; and the anti-pattern of reasoning from agent memory is excluded by construction. What Paper 2 adds is the proposing substrate as a new architectural object that reads that authoritative record and generates structured proposals, the two-stage governance review structure, the deliberate indirection between evidence and implementation, and configurability over the evidence window. These additions extend the substrate-as-source-of-truth commitment into the evolution context rather than departing from it.

With this formalization, the three-evolution-mechanism inheritance triple is complete: mutation inherits tool-agnosticism, directed selection inherits human-governed, and action-feedback inherits substrate-as-source-of-truth. Paper 2's full three-mechanism evolution architecture is grounded in Paper 1's foundational commitments, with each mechanism's inheritance relationship now named and statable.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Action-Feedback Evolution Inherits Paper 1's Substrate-as-Source-of-Truth.* May 14, 2026. ORCID: 0009-0004-8065-3235.
