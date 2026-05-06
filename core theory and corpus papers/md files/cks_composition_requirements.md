# Composition Without Erasure: What Multi-Substrate CKS Systems Must Preserve to Remain Traceable

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 24 April 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the set of properties that any composition of multiple CKS substrates must preserve in order for the resulting multi-substrate system to remain CKS-coherent. The note formalizes a constraint set; it does not propose composition primitives, mechanisms, or architectures.

## Abstract

The CKS source paper defines its design pattern at the level of one substrate and one cell, and explicitly defers cell-to-system composition to future work (§7.1, §13.2, §13.3). The paper is silent on what composition mechanisms should look like. It is not silent on what composition mechanisms must preserve: every architectural commitment the source paper defends at the single-substrate scope continues to apply across substrate boundaries when substrates are composed, because composition that violates those commitments produces a system that is no longer CKS-coherent. This note formalizes that constraint set. It identifies five requirements that any multi-substrate composition must satisfy — per-substrate human governance, conflict preservation across boundaries, addressable provenance across boundaries, AI-as-substrate-mediator at every layer, and human-selective composition — and treats the accountability-plan / accountability-trace distinction (Naja et al. 2021, imported by the source paper at §3.1) as a sixth requirement on what gets preserved. The note provides an operational test for whether a given composition satisfies the requirements. The requirements layer constrains the design space that future composition-primitive work must operate within, without itself occupying that space.

## 1. When does multi-substrate composition arise?

The CKS source paper introduces two levels of structure. A substrate is the atomic unit — a structured representation of one informational task. A cell is the functional whole — "a coordinated collection of substrates, possibly just one for a simple task, together with human-authored orchestration rules" (§2.1). Multi-substrate composition is therefore not an extension of the pattern; it is built into the pattern at the cell level. Any cell that aggregates more than one substrate is already a composition.

Beyond the within-cell case, three further composition contexts arise naturally in deployment. Multiple cells in the same workflow may share a substrate, or one cell's substrate may reference content in another cell's substrate. Cells may be organized into pipelines or hierarchies in which the output state of one cell becomes input state for another. Substrates may need to compose across organizational boundaries — substrate interoperability across organizations is named at §13.3 as a separate extension theory the source paper does not defend. The scope of this note is composition within a cell and across cells inside a single organizational governance domain. Cross-organizational composition, substrate-as-regulatory-artifact, and substrate-mediated human-AI-agent composition are out of scope; the source paper treats each as its own extension theory (§13.3).

The constraint set this note formalizes applies at every composition boundary inside the in-scope cases. A composition boundary is any location where content, conflicts, provenance, or control crosses from one substrate to another, regardless of whether the substrates sit inside the same cell or across cells. The requirements that follow do not distinguish between within-cell and cross-cell boundaries because the source paper's commitments do not distinguish between them: the substrate is the atomic unit, and the commitments apply per-substrate.

## 2. Five composition requirements

### Requirement 1 — Per-substrate human governance must be preserved

Every substrate participating in a composition must remain human-governed in the sense the source paper defends at Claim 1 (§3): humans retain the rights to inspect, modify, and override substrate content and the orchestration rules that govern cell-level behavior, at any time. A composition that grants any substrate authority over another substrate's content outside human authorization breaks Claim 1 and the human-governed commitment. This includes compositions in which one substrate's orchestration rules are permitted to silently overwrite content in another substrate, compositions in which a "parent" substrate strips override rights from a "child," and compositions in which a vendor or runtime layer interposes between the human and any participating substrate.

The requirement is per-substrate and not aggregate: the composition does not satisfy the commitment by being human-governed in the aggregate while individual substrates inside it are not. Authority is exercised at the substrate level because that is where the source paper locates it.

### Requirement 2 — Conflict preservation must hold across substrate boundaries

The source paper defends conflict preservation at the substrate level as Claim 3 (§5): contradictions, inconsistencies, and unresolved ambiguities are persisted as first-class addressable objects, and "no LLM operation over the substrate may silently merge, discard, or force resolution of them" (§5.3). This commitment does not weaken at composition boundaries. A composition that resolves a conflict in one substrate by overwriting it from another substrate's content — outside human-authored orchestration rules that explicitly authorize such resolution — breaks Claim 3.

The two-level structure §5.3 names carries through composition. At the substrate level, conflicts are preserved by default in every participating substrate. At the cell level, when a cell encounters a preserved conflict — whether the conflict lives inside one substrate or arises between substrates that have been composed — the response is determined by orchestration rules humans authored in advance. Composition does not authorize cross-substrate conflict resolution unless an orchestration rule explicitly does so; the default at every boundary is preservation.

A specific failure mode worth naming is conflict masking through composition. A composition that produces an aggregate view in which the conflicts present in the underlying substrates are not visible — for instance, a "merged" view that selects one side of a contradiction without recording the contradiction itself — fails Requirement 2 even if neither underlying substrate has been modified. Preservation requires the conflict to remain addressable through the composed view, not merely to remain present in some underlying store.

### Requirement 3 — Provenance must be addressable across substrate boundaries

The source paper imports the formulation "path retraceability over explicit structure" (Rajabi & Kafaie 2022, cited at §3.1) as the mechanism by which decision traceability is achieved. Claim 1 (§3.1) names traceability as one of four constitutive design goals of the CKS pattern. A composition that loses path retraceability at any boundary — that produces a composed output whose origin cannot be traced back to the substrates, cell-level orchestration rules, content, and rationale that produced it — breaks the traceability commitment.

Practical realizations of this requirement vary, and the source paper does not commit to any specific mechanism. What the requirement commits to is the property: from any decision visible in the composed system, a path must exist back to the substrate elements and orchestration-rule applications that produced the decision, and that path must be traversable without recourse to information outside the composition. Compositions that rely on extra-substrate conventions, undocumented vendor behavior, or LLM reconstruction to recover provenance fail the requirement; the path must be carried by the composition itself.

### Requirement 4 — AI-as-substrate-mediator must hold at every layer of composition

Claim 2 (§4.1, §4.2) establishes the AI-as-substrate-mediator role as a core-theory commitment: "the LLM operates as mediator over the substrate — helping humans read, write, interpret, and compose substrate content, and executing cell operations in accordance with human-authored orchestration rules — rather than as an autonomous agent over the workflow" (§4.1). The substrate is always the authoritative artifact; the LLM operates relative to it.

A composition in which the LLM operates over the composed output without operating over the underlying substrates breaks this commitment. Concretely, a composition that produces a new aggregate object — a "summary substrate," a "view," a "rollup" — and routes LLM operations to that aggregate without preserving the LLM's relationship to the underlying substrates loses the mediator role at the aggregate layer. The LLM, operating only on the aggregate, becomes effectively autonomous with respect to the underlying content; its outputs cannot be traced back through the aggregate to the substrate elements that produced them. The requirement is that the mediator role hold at every layer of the composition — at the underlying substrates, at any intermediate composed views, and at the cell aggregating them.

### Requirement 5 — Composition must remain human-selective, not automatic

Claim 4 (§6.1) commits the source paper to a specific architectural stance on composition: "composition of knowledge across cells is human-governed and selective, not automatic aggregation." A composition mechanism that aggregates substrates without human authority over what gets composed — for instance, an automatic discovery layer that decides which substrates to include in a composed view based on content similarity, or an LLM that decides which substrates to consult for a query without operating under human-authored orchestration rules that govern that selection — breaks Claim 4.

The requirement is not that humans must perform the composition labor. As §6.3 makes clear, labor is allocable: LLMs operating under human direction can perform composition work, and stable cells can largely automate it under orchestration rules. The requirement is that authority over what gets composed must remain human; the rules that govern selection must be human-authored, and the human's right to inspect, modify, and override those rules at any time must be preserved.

## 3. The accountability-plan / accountability-trace distinction applied to composition

The source paper imports a vocabulary distinction from Naja, Markovic, Edwards, and Cottrill (2021) at §3.1: an *accountability plan* is "what the system specifies must be captured across the AI lifecycle"; an *accountability trace* is "what actually occurred in any given run." The source paper commits to this vocabulary and uses it across Claims 2 through 6 without further definition (§3.1). The distinction does specific work at composition boundaries that Requirement 3 alone does not capture, and so it is treated here as a sixth requirement on what composition must preserve.

A composition can preserve the trace without preserving the plan. A composition that records every operation that occurred during an execution — every read, every write, every cell-rule application, every conflict encounter — but does not preserve the specification of what *should have been* captured produces a trace that cannot be evaluated. There is no record against which to check whether the trace is complete, whether expected events failed to occur, or whether the composition's behavior conformed to design intent. Audit becomes interpretive rather than evidentiary.

A composition can preserve the plan without preserving the trace. A composition that carries forward a specification of what each participating substrate and the cell aggregating them must capture, but loses the actual record of what occurred at composition boundaries, produces a plan that cannot be checked against any execution. The plan describes a system whose runs are unrecoverable.

The sixth requirement — call it Requirement 6 — is that any multi-substrate composition must preserve both the accountability plan and the accountability trace at every composition boundary, and that the two must remain mutually addressable: a participant must be able to take a trace element and locate the plan element it corresponds to, and take a plan element and locate the trace elements that realized (or failed to realize) it. Compositions that carry one without the other, or carry both without the cross-reference, fail the source paper's traceability commitment as Naja et al.'s vocabulary specifies it.

## 4. Operational test

A multi-substrate composition is CKS-coherent if and only if all of the following are true at every composition boundary at all times during the composition's existence:

1. **Per-substrate governance.** Every participating substrate satisfies the human-governed commitment in the sense formalized by the source paper and the prior derivation note: humans retain the rights to inspect, modify, and override substrate content and orchestration rules at any time, with no operation, vendor, or runtime layer in principle preventing those rights.

2. **Cross-boundary conflict preservation.** No conflict present in any participating substrate is silently merged, discarded, or resolved by the composition itself. Cross-substrate resolution occurs only when explicitly authorized by human-authored orchestration rules, and conflicts the rules do not address remain addressable through the composed view.

3. **Cross-boundary path retraceability.** Any decision visible in the composed system can be traced to the substrate elements, orchestration rules, content, and rationale that produced it, via a path carried by the composition itself rather than reconstructed from outside it.

4. **AI-as-substrate-mediator at every layer.** The LLM's role as mediator over substrate content, executing under human-authored orchestration rules, holds at the underlying substrates, at any intermediate composed views, and at the aggregating cell. No layer operates the LLM as an autonomous agent over a composed output disconnected from underlying substrates.

5. **Human-selective composition.** Authority over what gets composed remains human; the rules governing composition selection are human-authored; the human's right to inspect, modify, and override those rules is preserved.

6. **Plan and trace co-preserved.** Both the accountability plan (what must be captured) and the accountability trace (what occurred) are preserved at every composition boundary, and the two remain mutually addressable.

A composition that fails any of (1)–(6) may be a useful composition, may be governed in some other sense, and may instantiate other valid design patterns; it is not a CKS-coherent multi-substrate composition.

## 5. What this note does not do

This note does not propose composition primitives. It does not specify how substrates should be combined, what mechanisms should realize cross-boundary path retraceability, what orchestration-rule grammar should express composition behavior, or what runtime architectures should host composed cells. The source paper explicitly defers cell-to-system composition to future work at §7.1 ("open questions and long-term vision, not contributions of this paper"), at §13.2 (under scope limits), and at §13.3 (the first of four open questions, asking "how individual cells aggregate into an organizational-scale coordination fabric, how composition is governed when many cells touch overlapping domains, and what the architectural primitives for that aggregation look like").

The note's contribution is the requirements layer that any future answer to those questions must satisfy. Naming the requirements does not occupy the design space; it constrains it. Future composition-primitive work — by the author or by others — must address these requirements (or argue against them by name) to remain in continuity with the CKS pattern.

## 6. Why the requirements layer matters

Two reasons. The first is intellectual. The CKS source paper's commitments do not weaken at substrate boundaries, and stating the commitments in their composition-scope form makes the design implications explicit. Any reader who accepts the single-substrate commitments has, by transitivity, already accepted the multi-substrate constraints; this note simply does the work of writing them down.

The second is structural. The requirements layer is independently citable, independently usable, and independently extendable. A composition primitive proposed by any party can be evaluated against the requirements without re-examining the source paper: a primitive that fails one or more requirements can be flagged precisely; a primitive that satisfies all six can claim CKS-coherence with a clear basis. Constraints precede mechanisms in logical order and are published before them in time, which is the proper sequence.

The note formalizes the constraints. The mechanisms remain open work.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Composition Without Erasure: What Multi-Substrate CKS Systems Must Preserve to Remain Traceable.* 24 April 2026. ORCID: 0009-0004-8065-3235.
