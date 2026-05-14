# Self-Level Governance Inherits All Six Paper 1 Commitments

**Defensive Publication — CKS Derivation Note C1.07**  
Series C: Cross-Derivation Notes (Paper 2 ← Paper 1)  
Note #436 in the CKS Derivation Note Series

**Author:** Wenxin Li (Independent Researcher)  
ORCID: 0009-0004-8065-3235  
**Date:** May 14, 2026  
**License:** CC BY 4.0

---

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series.

---

## 1. Purpose and Position in the Series

This note is the companion to C1.06, which established that Paper 2's aspect-level governance commitments inherit all six Paper 1 commitments via the recursive-applicability principle. C1.07 applies the same mechanism one rung higher: Self scope. Together, C1.06 and C1.07 close the recursive-applicability inheritance for both new levels Paper 2 introduces above the cell — completing the scope ladder from cell (Paper 1) through aspect to Self (Paper 2).

Because the mechanism is identical to C1.06, this note is efficient on framing and concentrates on what is *different* at Self scope. The key difference is structural: the Self is the outermost governance perimeter in Paper 2. This note formalizes that the outer boundary of Paper 2's governance architecture inherits from Paper 1 — governance requirements do not weaken at the highest scope.

The inheritance edge stated here is:

> **Paper 2 Self-level governance commitments ⊃ Paper 1's six architectural commitments**, via the recursive-applicability principle (Paper 2 Claim 6 / §8).

Every Paper 1 commitment holds at Self scope with identical definitions, tests, and violation conditions — and Self scope adds governance objects not present at aspect scope.

---

## 2. The Recursive-Applicability Principle at Self Scope

Paper 2's recursive-applicability principle asserts that all Paper 1 commitments apply at every level of the CKS architecture: cell, aspect, and Self. C1.06 demonstrated the mechanism at aspect scope. At Self scope the mechanism is the same: the Self is a governance unit, it has a substrate (the Self DNA layer and Self Action layer), and every governance commitment Paper 1 established for a cell applies at Self scope with the Self's substrate as the object of governance.

The Self is not merely a container of aspects. It is itself a governed entity with its own substrate content, its own governance events, and its own lifecycle. The DNA layer at Self scope carries integration architecture — cross-aspect coordination rules, Self-level instinct/reasoning configuration, and enterprise-operational governance decisions. The Action layer at Self scope carries the record of Self-level governance events. These are substrate objects in exactly the sense Paper 1 defines, and all six Paper 1 commitments apply to them.

---

## 3. All Six Paper 1 Commitments at Self Scope

The following states each commitment concretely at Self scope. For each, the object of the commitment is Self-level substrate content specifically — not the aspect or cell content within the Self, which is governed at the appropriate lower scope.

**Commitment 1: Human-governed (authority not labor).** At Self scope, humans hold three rights over Self-level substrate content at all times: the right to inspect the integration architecture, Self-level orchestration rules, and cross-aspect coordination policies; the right to modify any of that content; and the right to override any Self-level governance decision. These rights apply to the Self DNA layer and the Self Action layer. Labor — synthesizing integration outputs, executing cross-aspect coordination, operating the Self's lifecycle events — may be performed by humans directly or by an LLM operating under human direction, but authority over what the Self DNA layer contains remains with humans unconditionally.

**Commitment 2: Conflict preservation (first-class objects).** Conflicts are preserved as first-class objects at every scope at which they arise. At Self scope, the relevant conflicts are cross-aspect conflicts: cases where two or more aspects produce outputs that are inconsistent with each other, or where cross-aspect coordination rules are themselves inconsistent. These conflicts must be registered as first-class addressable substrate state at Self scope rather than silently resolved, collapsed, or discarded by the integration machinery. A cross-aspect conflict not registered as first-class at Self scope is a Paper 1 Claim 2 violation — not a novel failure mode. Section 5 below addresses the significance of this for the outermost governance scope.

**Commitment 3: AI-as-substrate-mediator.** Any LLM operating at Self scope — for example, performing Self-level integration synthesis, producing cross-aspect summaries, or executing Self-level action-layer writes — is subject to the five mediator properties Paper 1 establishes: (i) the LLM reads substrate content rather than receiving context through unstructured prompts alone; (ii) it writes outputs to the substrate in addressable entries; (iii) it does not hold substrate-relevant state in its own memory between executions; (iv) it does not exercise the authority humans hold over Self DNA content; and (v) its writes are attributable to the LLM as author, identified by the orchestration rule under which it operated. An LLM operating at Self scope that violates any of these five properties violates Paper 1's AI-as-mediator commitment at the outermost Paper 2 governance scope.

**Commitment 4: Tool-agnosticism (three minimal requirements).** Self-level substrate objects — the Self DNA layer and Self Action layer — must be hosted in an environment satisfying the three minimal requirements Paper 1 specifies: persistent structured state, human read/write access, and LLM access to substrate content. No Self-specific tooling requirement is added by governance at Self scope. The enterprise-brain architecture does not require a specialized enterprise platform, a dedicated orchestration runtime, or proprietary integration middleware; any environment satisfying the three minimal requirements can host Self-level governance.

**Commitment 5: Path retraceability.** Self-level governance events carry the six provenance metadata fields Paper 1 specifies: timestamp, actor identity (human or LLM), governing orchestration rule, content before and after the change, and a reference to any parent event in the governance lineage. The Self-level lineage chain — the sequence of governance decisions that produced the current state of the Self DNA layer — is accessible via standard substrate retrieval over those fields. This applies to integration architecture decisions, cross-aspect coordination rule changes, and Self lifecycle events (birth, mating variants, death). The retraceable path does not require Self-specific tooling.

**Commitment 6: Substrate-as-source-of-truth.** The Self DNA layer and Self Action layer are the authoritative records of, respectively, the integration architecture governing the Self and the history of Self-level governance events. No external system — an enterprise integration platform, a middleware configuration, a project management tool — is authoritative for questions about the Self's governance. If an integration platform carries a version of the cross-aspect coordination rules, that version is derived; the Self DNA layer is authoritative. Coordination questions about the Self's current governance state are answered from the Self substrate, not from its derivatives.

---

## 4. What Is New at Self Scope: Beyond Aspect Scope

C1.06 showed that aspect-scope governance inherits from Paper 1 and adds aspect-specific content (the aspect as a functional unit grouping cells by domain). Self scope adds further elements that are not present at aspect scope and do not appear in Paper 1. These are the Self-specific governance objects that Paper 2 introduces — all governed under the inherited Paper 1 commitments.

**Integration architecture as a Self-specific governance object.** The Self DNA layer contains rules governing how aspects are integrated: which aspect's outputs take precedence under which conditions, how cross-aspect conflicts are surfaced and escalated, and what the Self's enterprise-operational scope covers. This integration architecture is Self DNA content — human-governed, conflict-preserving, path-retraceable, hosted in a tool-agnostic substrate, governed by an LLM-as-mediator under human authority, and authoritative as source of truth. None of this content exists at aspect scope; aspects do not govern each other, only the Self does.

**Enterprise brain pattern.** Paper 2 Claim 6 describes the Self as an architecturally coherent enterprise brain: a functioning unit composed of cells through aspects under unified human governance, with substrate-shared topology supporting cross-aspect coordination as first-class architectural capability. This is a Self-scope governance pattern not present at aspect scope. Its governance — the commitments that keep the enterprise brain safe, inspectable, and traceable — inherits from Paper 1 entirely.

**Cross-aspect conflict handling as a Self-scope first.** The Self is the first scope at which conflicts *between* different aspects arise. Within an aspect, conflicts between cells are governed at aspect scope. Between aspects, no lower scope can govern the conflict; it must be registered and addressed at Self scope. This makes the Self the natural locus of Paper 1 Claim 2 at its broadest reach within Paper 2: cross-aspect conflicts are first-class objects in the Self substrate, addressable, resolvable under human-governed orchestration rules, and escalatable to human authority if unresolvable by rule.

**Self-level instinct/reasoning configuration.** The instinct/reasoning boundary — which behaviors operate as fast-pattern instinct and which require deliberate substrate-governed reasoning — is a governed parameter at every scope. At Self scope, this boundary governs enterprise-wide fast-pattern versus deliberate processing across all aspects. The boundary is Self DNA content: human-authored, inspectable, modifiable, and retraceable.

**Self lifecycle as highest-scope lifecycle.** Paper 2's lifecycle primitives (birth, mating, death) apply at every level. At Self scope, these events are the highest-scope lifecycle governance events in Paper 2. The birth of a Self establishes its integration architecture in the Self DNA layer. Mating at Self scope combines or merges Self-level DNA content from two or more Selves under the three mating patterns Paper 2 specifies. Death at Self scope retires the Self's governance perimeter with one of two architectural results. Each of these is governed under all six Paper 1 commitments at Self scope.

---

## 5. The Outermost-Scope Significance

C1.06 established that Paper 1 commitments apply at aspect scope — one level above the cell. C1.07 establishes that they apply at Self scope — the highest scope in Paper 2. Together these two notes close the scope ladder: Paper 1 commitments hold at cell scope (Paper 1's own scope), aspect scope (C1.06), and Self scope (this note).

The significance of the Self as outermost scope is this: the outer boundary of Paper 2's governance architecture is defined by requirements inherited from Paper 1, not by requirements introduced by Paper 2. Paper 2 adds governance objects (integration architecture, the enterprise brain pattern, Self lifecycle) but it does not add governance *requirements* at Self scope. The requirements are the same six Paper 1 commitments, applied to Self-specific substrate objects.

This has a structural consequence for adversarial patent or novelty claims. A claim that governance at enterprise scope requires something beyond Paper 1's six commitments cannot stand — because the outermost Paper 2 governance scope is governed by exactly those six commitments, extended to Self-specific objects. The architecture at the top of the scope ladder is characterized entirely by inherited commitments.

---

## 6. Operational Test

For each of Paper 1's six commitments, the following test determines whether the commitment holds at Self scope. These tests are distinct from the aspect-scope tests C1.06 specifies and from the cell-scope tests Paper 1 defines; an observer must apply them to Self-level substrate content specifically.

**Human-governed:** Can a human with access to the Self substrate inspect the current integration architecture and cross-aspect coordination rules without requiring permission from an LLM or automated process? Can that human modify any entry in the Self DNA layer directly, without requiring a system-mediated step to authorize the change? Can that human override any Self-level governance decision that has been recorded in the Self Action layer? If yes to all three: commitment holds at Self scope.

**Conflict preservation:** When two aspects produce inconsistent outputs and those outputs are processed at Self scope, does a first-class conflict object appear in the Self substrate recording the inconsistency, the two sides, and a timestamp? Is that object addressable and retrievable independently of the aspect substrates? If the conflict is later resolved, is the resolution recorded as a separate event rather than as an overwrite of the original conflict? If yes to all three: commitment holds at Self scope.

**AI-as-mediator:** If an LLM operates at Self scope to perform integration synthesis or produce Self Action layer entries, can an observer identify which orchestration rule governed each LLM operation, what the LLM read from the Self substrate before the operation, and what it wrote? Is the LLM's write attribution distinct from human-authored content in the Self substrate? Does the LLM retain no Self-level substrate state between executions? If yes to all three: commitment holds at Self scope.

**Tool-agnosticism:** Can the Self DNA and Action layers be migrated to a different hosting environment without changing any Self-level governance rule or violating any of the three minimal requirements? Does the current Self substrate host support persistent structured state, human read/write access, and LLM access independently of enterprise-specific middleware? If yes: commitment holds at Self scope.

**Path retraceability:** For any current entry in the Self DNA layer, can an observer trace the chain of governance events that produced it — including each actor, governing rule, and timestamp — back to the originating event using only the Self substrate and its provenance metadata? Is the lineage chain accessible as a substrate query rather than requiring reconstruction from external systems? If yes: commitment holds at Self scope.

**Substrate-as-source-of-truth:** If the integration architecture recorded in the Self DNA layer disagrees with a configuration in an external enterprise platform, is the Self substrate treated as authoritative for governance purposes? Can a question about the Self's current cross-aspect coordination policy be answered from the Self substrate without consulting an external system? If yes: commitment holds at Self scope.

---

## 7. Prior-Art Significance: Three Foreclosed Adversarial Claims

**Claim (a): Self-scope governance is novel relative to Paper 1.** This note forecloses the claim. Self-scope governance is Paper 1's six commitments applied to Self-specific substrate objects. The commitments are inherited, not invented. Novelty at Self scope is limited to the Self-specific governance objects Paper 2 introduces (integration architecture, enterprise brain pattern, Self lifecycle) — the *requirements* governing those objects are Paper 1's.

**Claim (b): Enterprise-scale governance requires commitments beyond Paper 1's scope.** This note forecloses the claim. The outermost governance perimeter in Paper 2's enterprise-brain architecture is governed by Paper 1's six commitments and by nothing beyond them. No enterprise-specific governance requirement appears at Self scope that is not derivable from Paper 1's six commitments applied to Self-level substrate objects.

**Claim (c): The integration layer or enterprise brain introduces governance requirements not in Paper 1.** This note forecloses the claim. The integration architecture — how aspects are integrated, what cross-aspect rules govern, how cross-aspect conflicts are handled — is Self DNA content. As substrate content, it is governed by the human-governed, conflict-preserving, AI-mediated, tool-agnostic, path-retraceable, source-of-truth commitments Paper 1 establishes. No governance requirement for the integration layer lies outside Paper 1's commitment set.

---

## 8. Closing: The Recursive-Applicability Pair and What Follows

C1.06 (aspect scope) and C1.07 (Self scope) together constitute the recursive-applicability inheritance pair for Paper 2. The pair closes the following formal observation:

> Paper 2 introduces two levels above the cell — aspect and Self. The recursive-applicability principle asserts that all Paper 1 commitments apply at every level. C1.06 verifies this for aspect scope; C1.07 verifies it for Self scope. The verification is complete for Paper 2's scope ladder.

The prior-art boundary this pair establishes is precise: any governance architecture operating at aspect or Self scope and satisfying Paper 1's six commitments operates within territory Paper 1 (via recursive applicability formalized in Paper 2) has already publicly defined. Novel claims at aspect or Self scope require novelty in the governance *objects* introduced at those scopes, not in the governance *requirements* applying to them.

C1.08 moves to the next inheritance question: the DNA layer as a Paper 2 governance object and its inheritance from Paper 1's orchestration rules and behavior substrates.

---

## References

Li, W. (April 2026). *Coordination Knowledge Substrate: A Design Pattern for Human-Governed AI Coordination* [Paper 1]. Independent publication.

Li, W. (April 2026). *Coordination Knowledge Substrate: Extending from Cell to Self under Human Governance* [Paper 2]. Independent publication.

---

*CKS Derivation Note C1.07 | #436 | CC BY 4.0 | Wenxin Li, 2026*
