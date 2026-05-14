# Expression Mechanism Inherits Paper 1's Substrate-Governed Rule Selection

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series.

## Abstract

Paper 2 of the Coordination Knowledge Substrate (CKS) theory series introduces *expression* as the mechanism that determines which DNA-layer substrates activate for a given cell goal within a higher-level coordination context. This note formalizes the inheritance edge between that mechanism and Paper 1's commitment to substrate-governed rule selection via orchestration rules. The inheritance is substantive: expression preserves Paper 1's core principle that rule selection is governed by substrate content the LLM reads and follows rather than determined by the LLM's own inference. What is new in Paper 2 is the cross-level dimension — higher-level DNA (at aspect or Self scope) governing which lower-level rules are active within that scope's coordination context — and the non-destructive character of that governance: expression activates or constrains cell rules within a higher-level scope without modifying the cell's own DNA. The note distinguishes expression from directed selection as two distinct inheritance branches from Paper 1's orchestration rule governance, explains why both inherit the substrate-governed selection principle despite operating through different mechanisms, and provides an operational test for verifying that Paper 1's governance commitments hold in a deployment regardless of whether the expressed rules are at cell, aspect, or Self scope.

## 1. The inheritance edge

Paper 1 commits to orchestration rules as the mechanism that specifies which behavior applies in which context. Orchestration rules are substrate content — human-authored, stored outside the LLM, subject to the three governance rights (inspect, modify, override). The LLM does not determine its own applicable rules; it reads the rules from the substrate and operates within them. This is the substrate-governed selection principle: the selection of which rules apply is itself a governed substrate operation.

Paper 2 introduces expression as the mechanism that determines which DNA-layer substrates activate for a given cell goal. The expression specification — which sub-substrates are active for the current coordination context — lives in the DNA layer at aspect or Self scope. It is authored by humans, stored in the substrate, and fully subject to the three governance rights. The LLM reads the expression specification and activates the corresponding substrates; it does not self-select what to activate.

The inheritance edge is: **Paper 2's expression mechanism ⊃ Paper 1's substrate-governed rule selection by orchestration rules**. Expression is not an independent invention of a rule-activation logic; it is what Paper 1's substrate-governed selection principle produces when it extends from within-cell rule selection to cross-level rule selection, at aspect and Self scope.

## 2. What is preserved: the substrate-governed selection identity

Four properties from Paper 1's orchestration rule governance carry through to expression without modification.

**Selection is substrate-governed.** In Paper 1, the orchestration rules that select which behavior applies are substrate content. In Paper 2, the expression specification that selects which DNA-layer substrates are active is likewise substrate content — DNA layer content at aspect or Self scope. In both cases, what performs the selection is not the LLM's inference; it is a specification that lives in the substrate and that the LLM reads and follows. The substrate-governs-selection principle is structurally unchanged across the level extension.

**Selection is human-authored.** Paper 1 commits to orchestration rules as human-authored substrate content. The expression specification in Paper 2 inherits this property: governance authors which cell rules are expressed in which context, at which scope. The authority-versus-labor distinction from Paper 1 carries through — humans hold authority over the expression specification; the labor of authoring it is available to humans directly or to LLMs operating under human direction. What humans own is authority over what expression mechanisms exist and how activation decisions are made.

**The LLM does not determine its own applicable rules.** This is the sharpest formulation of the substrate-governed selection principle, and it holds in Paper 2 without qualification. The expression specification is a governed artifact in the DNA layer. The LLM's task is to read that specification and activate the corresponding substrates. The LLM has no architectural role in deciding what the expression specification contains; that decision is substrate content under human governance. Expression is not the LLM autonomously narrowing its own operational scope — it is the LLM following a governed specification that human-authored substrate content defines.

**Conflict preservation and path retraceability apply to expression.** Paper 1 establishes that conflicts are first-class substrate state and that substrate content carries provenance metadata. Both properties extend to expression in Paper 2. If two cell rules are expressed within the same higher-level coordination context and conflict, the conflict is a first-class addressable substrate object handled by the same conflict-preservation mechanism Paper 1 establishes. Expression specifications carry provenance metadata; changes to what is expressed within a scope are traceable. The governance properties that make orchestration rules auditable in Paper 1 make expression specifications auditable in Paper 2.

## 3. What is new: cross-level selection, non-destructive activation, and the three-level hierarchy

Three properties of expression are genuinely new in Paper 2 and constitute the prior-art territory this note claims.

**Cross-level selection.** Paper 1's orchestration rules select behavior within a single cell's scope: the rules that apply to a given input are selected by the cell's own orchestration substrate. This is within-cell rule selection. Paper 2 extends to cross-level selection: higher-level DNA (aspect DNA or Self DNA) governs which lower-level rules (cell DNA rules) are active within the higher-level coordination context. An aspect's expression specification determines, for coordination activity within that aspect's scope, which of its constituent cells' rules are engaged. A Self's expression specification can govern which rules are active across its aspects. The direction of governance is downward across levels — higher-level DNA selecting from lower-level content — and this cross-level dimension has no analog in Paper 1's single-cell architecture.

This cross-level extension is the architectural move that makes Paper 2's multi-level governance coherent. Without it, aspect and Self governance would have no mechanism to specialize cell behavior for different coordination contexts. With it, the same cell can behave differently within different aspect scopes — not because the cell's DNA differs, but because what is expressed from that DNA differs by scope.

**Non-destructive activation.** Expression activates or constrains cell rules within a higher-level scope without modifying the cell's own DNA. The cell's DNA is unchanged; what changes is which part of that DNA is engaged within the current coordination context. This non-destructive character is an important structural property: it means that cell DNA remains a stable, governable artifact even as its expressed behavior varies across deployment contexts. Different aspects can express different subsets of the same cell's rules; the cell's underlying governance properties are preserved throughout.

This distinguishes expression from directed selection, the other mechanism in Paper 2 that involves rule governance. Directed selection is the mechanism by which DNA evolution operates: humans or LLMs under human direction modify cell DNA — adding, refining, or removing orchestration rules — as part of the DNA evolution mechanism. Directed selection is destructive in the technical sense: it changes the cell's DNA content. Expression is non-destructive: it changes what is active within a scope while leaving cell DNA intact. Both inherit from Paper 1's orchestration rule governance, but through different branches (§4 develops this distinction).

**Three-level expression hierarchy.** Paper 2 introduces a three-level structure for expression that has no counterpart in Paper 1. Cell DNA rules can be expressed at cell scope (the cell's own orchestration rules governing its behavior as a standalone unit, which is the Paper 1 default), at aspect scope (an aspect's DNA governing which of a constituent cell's rules are active within the aspect's coordination context), or at Self scope (the Self's DNA governing rule application across its aspects as part of integration-level coordination). Each level has distinct scope and distinct governance authority: cell-level expression is under cell governance, aspect-level expression is under aspect governance, Self-level expression is under the Self's integrated governance. The three-level hierarchy is new in Paper 2 and is what makes expression a composable mechanism rather than a flat one.

**Composability of expression.** Because expression operates non-destructively at aspect scope, different aspects can express different subsets of their constituent cells' rules. Two aspects sharing the same underlying cell can present different operational faces within their respective coordination contexts. This composability is new in Paper 2 and is what makes multi-aspect architecture tractable: aspect-level governance can specialize cell behavior for each aspect's purpose without creating per-aspect copies of cell DNA. The substrate-governed selection principle from Paper 1 is what makes this composability safe — each expression specification is governed substrate content, not an autonomous specialization decision the system makes for itself.

## 4. Two inheritance branches from Paper 1's orchestration rules

Paper 1's orchestration rule governance is the common ancestor for two mechanisms in Paper 2 that are sometimes conflated: expression and directed selection. Distinguishing them as two inheritance branches clarifies what each mechanism inherits and what each adds.

**Expression inherits the substrate-governed selection principle.** Expression is the mechanism that determines which DNA-layer substrates are active within a coordination context. It inherits from Paper 1's rule selection: the selection of what is active is governed by substrate content the LLM reads and follows. What is new in expression (§3) is the cross-level dimension and non-destructive character. Expression does not modify the content being selected from; it selects from that content within a scope.

**Directed selection inherits the substrate-governed modification principle.** Directed selection is the mechanism by which DNA evolution changes cell DNA — the orchestration rules and behavior substrates that define how a cell functions. It inherits from Paper 1's commitment that orchestration rules are human-authored substrate content subject to the three governance rights. What is new in directed selection is the explicit evolution mechanism: governance-defined goals drive modifications to cell DNA, with LLMs available to draft changes under human authority. Directed selection changes the content that expression subsequently selects from.

The two branches share the same root — Paper 1's commitment that rule governance is substrate-governed and human-authored — and diverge at the operation type: selection-without-modification (expression) versus modification-under-governance (directed selection). A deployment instantiates both simultaneously: directed selection governs how cell DNA evolves over time; expression governs which part of that DNA is active in each coordination context. The inheritance structure is branching, not sequential — expression does not depend on directed selection having operated first, and directed selection is not a prerequisite for expression to function.

This two-branch structure matters for prior-art purposes. An adversarial claim that expression introduces novel rule-application logic unrelated to Paper 1's orchestration rules fails because expression is the cross-level, non-destructive extension of exactly the substrate-governed selection that Paper 1's orchestration rules perform at cell scope. An adversarial claim that directed selection is the only legitimate inheritance of Paper 1's rule governance — and that expression is therefore novel relative to it — fails because both branches inherit from Paper 1, not from each other.

## 5. Prior-art significance

This note forecloses three adversarial claim lines.

**Claim line (a): Paper 2's expression mechanism introduces novel rule-application logic unrelated to Paper 1's orchestration rules.** This fails. Expression is the cross-level extension of Paper 1's substrate-governed rule selection. The principle is unchanged — the LLM reads a governed specification and activates the corresponding rules — and the expression specification inherits all four preservation properties enumerated in §2. The fact that expression operates across levels rather than within a single cell's scope does not make it a new kind of rule-application logic; it makes it the same kind of logic applied at a different architectural scope.

**Claim line (b): Cross-level rule governance is novel relative to Paper 1's within-cell rule governance.** This fails as a novelty claim. Paper 2 explicitly names expression as the mechanism that extends Paper 1's orchestration rule governance to aspect and Self scope. Cross-level selection is an extension, not a departure. The substrate-governed selection principle that Paper 1 establishes at cell scope is the same principle operating at higher levels in Paper 2's expression mechanism. Both papers are published under the same author in April 2026; the inheritance relationship is documented in both papers and formalized in this note.

**Claim line (c): Non-destructive rule activation is novel.** This fails. Non-destructive activation is the structural property that follows from extending substrate-governed selection to higher levels: because expression operates by selecting from existing cell DNA rather than modifying it, the activation is necessarily non-destructive. The non-destructive character is what substrate-governed selection produces when it extends to the cross-level dimension; it is not an independent mechanism requiring independent prior-art establishment.

## 6. Operational test

For any deployment of Paper 2's expression mechanism, the following test verifies that Paper 1's substrate-governed selection governance commitments hold at expression scope, independently of whether the expressed rules are at cell, aspect, or Self scope.

A deployment instantiates the inherited substrate-governed selection commitment for expression if and only if all of the following are true:

1. **The expression specification is substrate content.** The specification of which DNA-layer substrates are active within a given coordination context is stored in the substrate (DNA layer), not held implicitly in LLM inference or in runtime middleware. An observer can locate, inspect, and read the expression specification without interrogating the LLM.

2. **The expression specification is subject to the three governance rights.** Humans can inspect the expression specification at any time. Humans can modify the expression specification at any time. Humans can override any expression decision the system has made. None of these rights requires LLM cooperation to exercise; they follow from the substrate's accessibility to humans.

3. **The LLM does not determine its own expressed rules.** The LLM's role is to read the expression specification and activate the corresponding substrates. There is no step in the expression mechanism at which the LLM infers, decides, or proposes what should be expressed; that decision is encoded in substrate content. If the LLM's behavior in a given coordination context appears to deviate from what the expression specification authorizes, that deviation is diagnosable and correctable by inspecting and modifying the substrate.

4. **Conflicts among expressed rules are first-class substrate state.** If two cell rules are expressed within the same coordination context and conflict, the conflict surfaces as a first-class addressable substrate object. It is not silently resolved by the LLM, not suppressed by the expression mechanism, and not deferred to runtime inference. The conflict is visible, inspectable, and resolvable through the governance mechanisms the substrate supports.

5. **Expression specifications carry provenance metadata.** Changes to what is expressed within a given coordination context are traceable: the prior expression specification, the change event, and the authority under which the change was made are recoverable from the substrate. The expression history at any scope (cell, aspect, Self) is auditable.

A deployment that satisfies all five conditions has preserved Paper 1's substrate-governed selection principle through Paper 2's cross-level extension. A deployment in which any condition fails has introduced a governance gap — the most consequential being condition 3 (LLM self-selection of applicable rules), which violates the substrate-governed selection principle at its core.

## 7. Next note

The next note in this series, C1.11, formalizes the inheritance edge at the birth lifecycle primitive: Paper 2's cell, aspect, and Self birth operations inherit from Paper 1's governance-authorized origination commitment, with new properties introduced at the multi-level structure.

---

## Source papers

- Paper 1: *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026).
- Paper 2: *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance* (Li, April 2026).

## Self-citation

This note is part of a derivation-note series on the Coordination Knowledge Substrate pattern. Preceding Series C notes (C1.01–C1.09) formalize earlier inheritance edges between Paper 2 and Paper 1. Subsequent notes continue from C1.11.
