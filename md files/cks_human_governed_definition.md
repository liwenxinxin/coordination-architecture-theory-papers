# Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 24 April 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes a single architectural commitment introduced in the Coordination Knowledge Substrate (CKS) pattern: *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the precise meaning of the term *human-governed* as that term is used in the source paper, so that downstream work can adopt or argue against the term without ambiguity.

## Abstract

The Coordination Knowledge Substrate (CKS) design pattern names "human-governed" as one of its six architectural commitments. The term is load-bearing: every other commitment in the pattern — substrate-as-coordination-artifact, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, linear-cost scaling — depends on what "human-governed" means. The term is also commonly misread, most often as a synonym for "human-curated," "human-authored," or "human-in-the-loop." This note formalizes "human-governed" as the source paper uses it: a commitment to *human authority* (the right to inspect, modify, and override substrate content and orchestration rules at any time), not a commitment to *human labor* (the work of writing, curating, or maintaining substrate content). The note states the definition, distinguishes it from five neighboring concepts it is commonly conflated with, identifies the two moments at which governance is exercised, and provides an operational test for whether a given system instantiates the commitment.

## 1. Why a precise definition is needed

The CKS pattern uses "human-governed" as the architectural anchor for its central design move: locating coordination knowledge, governance semantics, and conflict-handling logic in a persistent substrate outside the LLM, rather than inside the LLM's inference or in specialized runtime middleware around it. The substrate is what makes the pattern coherent; "human-governed" is what makes the substrate's role defensible against the alternative that an LLM-maintained store would do the same work.

The term is not self-defining. In the surrounding literature, the adjacent terms "human-curated," "human-authored," "human-reviewed," "human-in-the-loop," and "human-generated" all name closely related but distinct commitments. Each of these neighbors implies a different scaling profile, a different cost model, and a different kind of obligation on the humans involved. If "human-governed" is read as any of them, the rest of the CKS pattern misreads with it — most consequentially as a per-element review bottleneck that scales linearly with substrate size, which the source paper explicitly rules out (§3.3, §6.3).

This note pins down the definition the source paper commits to.

## 2. The definition

In the CKS pattern, a substrate is **human-governed** if and only if humans retain the following properties at all times during the substrate's existence:

1. **The right to inspect** any substrate content and any orchestration rule that governs cell-level behavior.
2. **The right to modify** any substrate content and any orchestration rule.
3. **The right to override** any operation, default, or LLM-produced output that touches substrate content or orchestration rules.

These three rights together are what "governance" names. They apply to two scope objects:

- **Substrate content** — the structured representations the substrate carries (entities, relationships, decisions, rationale, conflicts).
- **Orchestration rules** — the human-authored rules that determine how a cell behaves when it executes over substrate content.

The commitment is *architectural*: the rights must be available as a property of the system's design, not as a procedural promise that depends on a particular deployment, vendor, or workflow. A system in which an LLM, a vendor, or a runtime middleware layer can in principle prevent a human from inspecting, modifying, or overriding substrate content or orchestration rules is not human-governed in the CKS sense, regardless of how rarely that prevention occurs in practice.

The commitment is also *temporal*: the rights must be available *at any time*, not only at predetermined checkpoints. A system that grants inspection rights only during scheduled review windows, or modification rights only to designated reviewers operating under a workflow approval gate, may satisfy other governance frameworks; it does not satisfy the CKS commitment.

## 3. What human-governed is NOT

The definition above is precise about what human-governed *is*. It is equally important to state what it is not, because each of the following neighbors is a real and reasonable commitment in some other architecture, and conflating any of them with human-governed produces a misreading of the CKS pattern.

**Not human-generated.** Human-governed says nothing about who or what produces substrate content. Content may be drafted by humans directly, drafted by LLMs operating under human direction, populated by automated extraction from prior artifacts, or produced by stable cells executing under orchestration rules. What the architecture requires is that whatever produced the content remains subject to the three rights named in §2.

**Not human-authored.** "Human-authored" describes a labor commitment — that the humans named perform the writing work. The CKS pattern does use "human-authored" in one specific place: the orchestration rules that govern cell-level behavior must be authored by humans. But substrate content as a whole is not required to be human-authored. The labor of authoring is allocable; the authority over the result is not.

**Not human-reviewed.** A human-governed substrate does not require that a human review every element it contains. Review is an option the architecture preserves (via the inspect right), not an obligation it imposes. The misreading "human-governed implies human-reviews-everything" is the central misreading the source paper preempts (§3.3) under the portable phrase *governance is an authority architecture, not a review workflow*.

**Not human-in-the-loop (HITL).** HITL names a runtime pattern in which a human is inserted as an approval or correction step in an otherwise automated process. HITL is one *implementation* of governance over a particular operation; CKS-style governance is the *architectural property* that makes HITL (or any other intervention pattern) exercisable when chosen. A human-governed substrate may be operated with no HITL gates at all and still satisfy the commitment, provided the three rights remain available.

**Not human-curated.** "Human-curated" typically describes the labor of selecting, organizing, and maintaining content over time. CKS supports human curation as one mode of substrate maintenance, but does not require it. A substrate maintained primarily by LLMs under human direction, with humans exercising authority only at the rule-writing layer and at moments of override, is human-governed in the CKS sense even if no human performs day-to-day curation labor.

## 4. The two moments at which governance is exercised

Governance in the CKS sense is exercised at two moments, and naming them precisely is what makes the commitment compatible with substrate size growth (§3.3, §6.3 of the source paper).

**Moment 1 — Orchestration rule authoring (design time).** Humans write the orchestration rules that determine cell-level behavior: who can modify the substrate, how conflicts are handled, what the LLM is authorized to do on the substrate's behalf, what conditions trigger which response. This cost is paid once per rule and amortizes across every cell execution that follows. It is not proportional to substrate size; it is proportional to the variety of behaviors the cells need to support.

**Moment 2 — Direct override (intervention time).** Humans use their preserved override right to directly modify substrate content or orchestration rules — adding, editing, deleting, or restructuring as they see fit. This cost is paid only when a human chooses to intervene. It is not proportional to substrate size; it is proportional to the frequency of human-initiated change.

Neither moment requires per-element human action at the time of substrate growth. This is the architectural feature that makes "human-governed" compatible with substrates that scale to large sizes. The reading that mistakes governance for per-element review breaks the cost model; the definition above preserves it.

## 5. Implications

Three implications follow directly from the definition.

**Labor is allocable.** Because authority and labor are distinct commitments, the labor of authoring, curating, and maintaining substrate content can be allocated across three modes in the same deployment: humans performing the work directly, LLMs performing it under human direction, and stable cells largely automating it under orchestration rules. The architecture supports all three; it requires none of them in particular. Allocation is a deployment decision, not an architectural one.

**Governance cost is not size-proportional.** Because governance is exercised at the two moments named in §4 — neither of which scales with substrate size — the cost of maintaining governance does not grow with the substrate. Governance cost grows with rule variety (Moment 1) and intervention frequency (Moment 2), both of which are bounded by the system's design and the operators' choices, not by how much content the substrate holds.

**Non-specialist governance is meaningful.** Because the three rights (inspect, modify, override) can be exercised in any environment that supports persistent structured state, human read/write access, and LLM access to substrate content, "human-governed" is realizable in commodity tools by non-specialists. This is what the source paper means when it commits to non-specialist governance as an architectural property (§7.4) — the rights are available to anyone who can read and write the substrate, not only to designated reviewers operating inside a specialized governance runtime.

## 6. Operational test

A system instantiates the CKS "human-governed" commitment if and only if all of the following are true at all times during the substrate's existence:

1. A human with appropriate access can read any substrate content and any orchestration rule, without scheduling, approval, or runtime intermediation.
2. A human with appropriate access can write to, edit, or delete any substrate content and any orchestration rule, with the change taking effect as substrate state.
3. No LLM operation, vendor policy, or runtime middleware layer can in principle prevent (1) or (2).
4. Orchestration rules are authored by humans (LLM-drafted rules subject to human authority before they take effect are admissible; LLM-committed rules outside human authority are not).
5. Override actions taken under (2) do not require justification to the system or to a higher authority within the architecture (they may be logged, audited, or socially reviewed; they are not architecturally gated).

A system that fails any of (1)–(5) may be a useful system, and may be governed in some other sense, but is not human-governed in the CKS sense.

## 7. Conclusion

"Human-governed" in the CKS pattern names an architectural commitment to human authority — the rights to inspect, modify, and override substrate content and orchestration rules at any time — and not a commitment to human labor. The distinction matters because labor is allocable across humans, LLMs under human direction, and automated cells, while authority is not. The same distinction is what allows the CKS pattern to scale: governance is exercised at two moments that do not grow with substrate size, neither of which is per-element review.

Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "human-governed" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.
