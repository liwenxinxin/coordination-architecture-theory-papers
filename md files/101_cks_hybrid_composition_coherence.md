# Hybrid Composition Coherence: Why the Three Adjacency Boundaries Operationally Matter

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the architectural commitment to *hybrid composition coherence* — the operational consequence of naming the three adjacency boundaries — as a standalone object that can be defended, implemented, and tested independently of the boundary specifications themselves.

## Abstract

The CKS source paper distinguishes the substrate pattern from three adjacent design objects (RAG, parametric memory, external structured memory of the KO/OIDA family) at §1.2 and §2.3, and develops the load-bearing differentiations across §§3.1, 5.2, 6.1, 6.2, and 8.2. The integrating treatment at the foundational level (the three-adjacencies note A1.14, with operational integrating frame A2.81) and its three boundary specializations (A2.82, A2.83, A2.84) name the architectural distinctions; this note formalizes why naming those boundaries operationally matters. The architectural commitment is *hybrid composition coherence*: each composition between CKS and an adjacent object is coherent only when the layers are named explicitly, and the three adjacency boundaries are what make the explicit naming possible. The note states the commitment as four operational components, surveys the three operationally common hybrids and the specific incoherence failure mode each exhibits when its boundary is unnamed, distinguishes the commitment from four adjacent patterns commonly conflated with it, names ten failure modes that violate it, and supplies an operational test for whether a hybrid satisfies the commitment.

## 1. Why hybrid composition coherence needs to be formalized as standalone

The parent foundational note (A1.14) commits to the three adjacencies. The integrating-frame note (A2.81) names hybrid composition coherence at the integrating level. The three adjacency specializations (A2.82 for RAG, A2.83 for parametric memory, A2.84 for external structured memory of the KO/OIDA family) formalize each boundary as standalone. This note formalizes the operational commitment those boundaries together enable: the architectural property that each composition between CKS and an adjacent object is coherent only when the layers are named explicitly.

The motivating cases are operational. A regulated coordination workflow with a CKS substrate at its center is typically embedded in a larger AI system: a RAG retrieval index sits over source documents the substrate references; the cell's LLM mediator may be fine-tuned on domain content; an enterprise KO or OIDA deployment may sit alongside the substrate at the structured-memory layer. Each scenario requires hybrid composition coherence — the layers must be named explicitly so that each operates architecturally as designed.

The strategic posture also matters. Architectures that present hybrid AI systems as unified objects combining substrate, retrieval, parametric, and structured-memory layers are substantially more defensibly contested when hybrid composition coherence is publicly formalized as standalone. The standalone treatment forecloses readings that present hybrids as single architectural objects, because such readings are inconsistent with the four operational components this note specifies.

The connection to the broader composition framework also matters. The composition-requirements foundational note (A1.13) specifies five requirements any composition must satisfy; the hybrid-systems composition foundational note (A1.16) specifies the three patterns by which a composition structures (input to a cell, derivative view of substrate, separate concern). Hybrid composition coherence is what makes these frameworks operationally applicable to compositions involving adjacent objects. Without the boundary-naming the three adjacency specializations provide, the requirements cannot be enforced and the patterns cannot be applied, because the layers across which the requirements must hold and the patterns must operate are not architecturally distinguishable.

## 2. Hybrid composition coherence, defined precisely

The architectural commitment has four operational components.

**(a) Explicit layer naming.** Each layer in a hybrid composition is named architecturally — the CKS layer is identified as CKS; the adjacent-object layer is identified as that specific adjacent object (RAG, parametric memory, or external structured memory of the KO/OIDA family). The naming operates at the architectural level, not at the deployment-feature level: the layers are architecturally distinguishable through the boundaries the three adjacency specializations formalize, and the distinction is carried in the architecture's own description rather than left to deployment convention.

**(b) Preservation of each layer's architectural commitments.** Each layer retains its architectural commitments in the hybrid. The CKS layer preserves human-governed authority (A1.01), the substrate-cell boundary (A1.02), AI-as-substrate-mediator (A1.04), linear-cost scaling (A1.06), and the other foundational commitments per the source paper. The adjacent-object layer retains its own architectural commitments — RAG's retrieval architecture, parametric memory's in-weight storage, KO/OIDA's structured-memory commitments. Neither layer absorbs the other's commitments; each layer's commitments hold as the architecture specifies them, even within the hybrid.

**(c) Operationally observable boundaries.** The boundaries between layers are operationally observable in the deployed system. Substrate writes produce substrate-resident content with provenance; retrieval results produce corpus-grounded context for cells; fine-tuned mediator outputs are operationally distinguishable from substrate content; structured-memory operations are distinguishable from substrate operations. The boundaries are not implicit, convention-only, or recoverable only through architectural exegesis; they are operationally specific in the deployed system.

**(d) No inter-layer absorption of commitments.** The CKS layer does not absorb the adjacent-object layer's commitments — the substrate does not become the retrieval index, parametric memory, or the structured-memory store. The adjacent-object layer does not absorb the CKS layer's commitments — RAG-with-governance-metadata does not become CKS, a fine-tuned LLM does not become substrate, KO with extra fields does not become CKS. Each layer operates within its own architectural commitments, and commitments do not migrate across the boundary.

The four components together define hybrid composition coherence architecturally. A hybrid that satisfies all four has coherence in the architectural sense; one that fails any component does not, regardless of how operationally combined the layers may appear.

## 3. The three hybrids, named precisely with their specific failure modes

The three operationally common hybrids exhibit operationally distinct content. Each depends on the corresponding adjacency specialization, and each has a specific incoherence failure mode if its boundary is unnamed.

**(a) CKS-fronting-RAG.** A CKS substrate fronts a RAG retrieval index when source-document grounding is needed for content the substrate references. The substrate carries the decisions, rationale, role/authority assignments, and preserved contradictions; the RAG layer supplies the source material those decisions rest on. The architectural pattern uses the input-to-a-cell pattern from the hybrid-systems composition framework (A1.16, Pattern A): the RAG layer provides retrieved context as input to cells that write to the CKS substrate under orchestration rules. The substrate is not the retrieval index, and the retrieval index is not the substrate; the two are architecturally distinct objects composed across an explicit boundary.

The specific incoherence failure mode if the layers are not named: the RAG layer is mistaken for the substrate, and governance is read as retrieval policy rather than as authority over a coordination artifact. The human-governed commitment (A1.01) collapses into retrieval-time policy enforcement; the inspect, modify, and override rights at any time become "what content the index returns," which is a different operational object than authority over decisions, rationale, and preserved contradictions. The boundary the corresponding adjacency specialization formalizes (A2.82) is what enables explicit naming and prevents the collapse.

**(b) CKS-with-fine-tuned-mediator.** A CKS cell uses an LLM mediator that has been fine-tuned on domain content. The mediator's parametric memory improves its fluency in the domain — terminology, conventions, characteristic patterns — while the substrate remains the authoritative artifact for what has been decided in that domain. The architectural pattern operates within the cell-execution layer: the fine-tuned mediator is the LLM in the cell, operating under the five mediator properties the source paper develops at §4 and the mediator decomposition (A2.18–A2.23) formalizes. Fine-tuning improves the mediator's behavior within those properties; it does not change the properties themselves, and it does not relocate authority from the substrate to the model weights.

The specific incoherence failure mode if the layers are not named: the parametric memory is mistaken for the substrate, and expansion cost curves become unintelligible. The architecture appears to commit to linear-cost scaling (A1.06) while in fact carrying parametric expansion as a hidden term — additional domain content requires retraining with the superlinear cost dynamics the source paper surveys at §6.2 (sequential fine-tuning disrupting 15–23% of attention heads in lower layers; ROME beginning catastrophic forgetting between 100 and 1,000 edits depending on settings; MEND degrading toward zero F1 before 100 edits). The cost commitment becomes inconsistent because the parametric expansion is hidden behind the substrate framing. The boundary the corresponding adjacency specialization formalizes (A2.83) is what makes the parametric expansion architecturally visible and prevents the commitment from collapsing.

**(c) CKS-composed-with-KO/OIDA.** A CKS substrate is composed with an external structured-memory store of the KO or OIDA family. The structured-memory layer holds typed facts and contradictions at scale — the database-like cost regime the source paper validates at §6.2 — while the CKS layer adds the human governance, role/authority schema, and substrate-mediator semantics the structured-memory layer does not commit to. The architectural pattern uses the input-to-a-cell pattern (Pattern A) when the structured-memory layer feeds cells, the derivative-view pattern (Pattern B) when the structured-memory layer is a derived view of substrate content, or both depending on architecture; specific deployments may use either pattern or both.

The specific incoherence failure mode if the layers are not named: the structured memory is mistaken for CKS, and the role/authority schema and the AI-as-substrate-mediator commitment (A1.04) disappear without anyone noticing. The hybrid is then a KO or OIDA deployment with the CKS layer reduced to decoration — metadata, labels, or annotations that have no architectural force. The two-axis extension structure the source paper specifies at §6.2 (governance-semantics axis; disambiguation-locus axis) collapses into a single-axis "KO with extra fields" reading, which the source paper preempts directly at §6.2 with the load-bearing phrase deployed at §5.2 and §9.4: *CKS is architecturally different from OIDA on the multi-human axis, not OIDA plus multi-human*. The boundary the corresponding adjacency specialization formalizes (A2.84) is what enables the structured-memory layer and the CKS layer to coexist without one absorbing the other.

## 4. What hybrid composition coherence is not, and what it does not claim

The standalone treatment is bounded in two directions: by what the commitment does not claim, and by adjacent patterns commonly conflated with it.

**Bounded claims.** Hybrid composition coherence does not claim that hybrids are necessarily preferable to single-layer architectures; deployments may use single-layer CKS, single-layer RAG, or single-layer KO/OIDA depending on operational concerns, and the architectural commitment is to coherence when hybrids exist rather than to hybrid presence as a default. It does not specify implementation patterns for layer naming; deployments may use architectural documentation, layered API design, or substrate-resident layer markers, and the commitment is to the four operational components being satisfied rather than to a particular implementation. It does not foreclose hybrids beyond the three named — multi-adjacency hybrids combining CKS with two or all three adjacent objects (e.g., CKS-fronting-RAG-with-fine-tuned-mediator) are operationally feasible and are coherent when the multiple boundaries are all named explicitly. It does not require hybrids to use the same composition pattern from A1.16; different hybrids may use Pattern A, Pattern B, or Pattern C as appropriate. It does not foreclose architectural evolution within hybrids — layers may be added, removed, or modified per the human-selective composition requirement (A2.80) — but coherence must hold at any moment during the hybrid's existence. And it does not claim hybrids are operationally simple; the commitment is to coherence, not to operational simplicity.

**Adjacent patterns to distinguish from.** Four patterns are commonly conflated with hybrid composition coherence and are not what the commitment specifies.

*Not architectural unification.* Architectural unification is the framing that hybrids produce a single unified architecture combining the constituent layers' features. Hybrid composition coherence is different: hybrids compose layers with explicit boundaries, each layer retains its architectural commitments, and no unified architecture emerges from the composition. Audiences who understand hybrid composition as unification miss the boundary-naming commitment that makes coherence possible. The unification framing is the dominant commercial framing the standalone treatment has to displace.

*Not feature-additive composition.* Feature-additive composition is the framing that hybrids combine the constituent layers' feature lists ("CKS-fronting-RAG has both substrate features and retrieval features"). Hybrid composition coherence is different: hybrids preserve architectural commitments, which are not feature lists, and each layer's commitments remain architecturally distinct. The hybrid is not a feature super-set of its constituent layers.

*Not vendor-bundled integration.* Vendor-bundled integration is the operational pattern of vendors offering pre-integrated systems that combine multiple architectural objects. Hybrid composition coherence operates at the architectural level — boundary-naming, commitment preservation — not at the vendor-packaging level. Vendor-bundled integrations may operationally support hybrid coherence if architectural boundaries are preserved, or may violate it if the bundle conflates layers; the bundling is orthogonal to coherence.

*Not organizational coherence.* Organizational coherence is the pattern of organizations developing consistent practices across their AI systems. Hybrid composition coherence operates at the architectural-pattern level within a specific hybrid composition; organizational practices may operationally support or undermine architectural coherence but do not substitute for it.

## 5. Why hybrid composition coherence is load-bearing for downstream commitments

Several CKS commitments depend on hybrid composition coherence holding when the deployment is hybrid rather than single-layer.

The integrating three-adjacencies specification (A1.14, A2.81) names the architectural distinctions; hybrid composition coherence is the operational consequence of those distinctions. Without coherence, the boundaries the three adjacency specializations formalize would be operationally inert — they would describe distinctions that hybrids fail to respect.

The composition-requirements foundational note (A1.13) and its decomposition (A2.75–A2.80) specify five requirements operating at the boundaries the three adjacency specializations formalize: per-substrate human governance preservation (A2.76), conflict preservation across boundaries (A2.77), addressable provenance across boundaries (A2.78), AI-as-mediator at every layer (A2.79), and human-selective composition (A2.80). Each requirement depends on the boundaries being explicit; without coherence, none of the five can be operationally enforced because the layers across which the requirement must hold are not architecturally distinguishable.

The hybrid-systems composition framework (A1.16) specifies three patterns by which compositions structure. Hybrid composition coherence is what makes the patterns operationally applicable to compositions with adjacent objects: a Pattern A composition with a RAG layer requires the RAG layer to be architecturally distinguishable from the CKS substrate, and the boundary specialization is what supplies the distinction.

The human-governed commitment (A1.01) depends on coherence in CKS-composed-with-KO/OIDA hybrids. The CKS layer's authority structure must be preserved despite the structured-memory layer's absence of governance commitments; without coherence, A1.01 collapses into the structured-memory layer's maintenance posture. The linear-cost commitment (A1.06) depends on coherence in CKS-with-fine-tuned-mediator hybrids: the substrate's cost commitment must hold despite the parametric layer's superlinear cost dynamics; without coherence, the commitment becomes inconsistent because parametric expansion is hidden. The AI-as-substrate-mediator commitment (A1.04) depends on coherence in all three hybrids: the CKS layer's mediator role must hold despite the adjacent layers' different AI-role assumptions (substrate client for KO/OIDA, retrieval consumer for RAG, parametric host for fine-tuned mediator); without coherence, A1.04 collapses into the adjacent layer's AI role.

## 6. Failure modes that violate hybrid composition coherence

Ten failure modes name ways an implementation can fail by collapsing layers or absorbing commitments. The list is enumerative rather than exhaustive; each item names an operationally distinct way the four components in §2 can be violated.

(a) *CKS-fronting-RAG with governance read as retrieval policy.* The hybrid is implemented but the RAG layer is positioned as the source of governance — retrieval policies are treated as authority over content. Component (b) fails for the CKS layer; A1.01 collapses into retrieval-time policy enforcement.

(b) *CKS-with-fine-tuned-mediator with parametric expansion as hidden term.* The hybrid is implemented but the parametric memory's superlinear cost dynamics are not architecturally visible. The architecture appears to commit to linear-cost while carrying parametric expansion as a hidden architectural term; A1.06 becomes inconsistent.

(c) *CKS-composed-with-KO/OIDA with CKS layer as decoration.* The hybrid is implemented but the CKS layer's commitments operate only nominally — the architectural force is in the KO/OIDA layer, with CKS reduced to metadata or labels. A1.04 and the role/authority schema collapse.

(d) *Hybrid presented as unified architecture.* The implementation presents the hybrid as a single architectural object rather than as composed layers with explicit boundaries. Component (a) fails; audiences cannot tell which layer is doing what.

(e) *Boundaries documented but not operationally observable.* The implementation includes architectural documentation describing layer boundaries, but the boundaries are not observable in the deployed system — operational behavior conflates layers despite the documentation. Component (c) fails.

(f) *Inter-layer commitment absorption — CKS absorbs adjacent object's commitments.* The implementation has CKS attempt to satisfy commitments belonging to the adjacent layer (e.g., the substrate becomes the retrieval index, with retrieval-quality commitments held in CKS). Layer roles are conflated; component (d) fails.

(g) *Inter-layer commitment absorption — adjacent object absorbs CKS's commitments.* The implementation has the adjacent layer attempt to satisfy CKS's commitments (e.g., RAG with governance metadata claiming to be CKS-equivalent; KO with extra fields claiming to be CKS-equivalent). The architectural distinction collapses; component (d) fails in the other direction.

(h) *Implicit composition without explicit naming.* The implementation operates a hybrid implicitly — the architectural composition exists operationally but is not named in architectural documentation, deployment design, or system-level reasoning. Component (a) fails; audiences cannot reason about the hybrid as a coherent architectural object.

(i) *Multi-boundary collapse with partial coherence.* The implementation composes CKS with multiple adjacent objects but the three boundaries (CKS-vs-RAG, CKS-vs-parametric, CKS-vs-KO/OIDA) are not all named. Some layers are architecturally distinguishable while others are conflated, producing partial coherence that is not coherence in the architectural sense.

(j) *Boundary-naming as marketing only.* The implementation names the layers in commercial documentation but the architectural commitments of each layer are not preserved operationally. Naming is performative rather than architectural; one or more of components (b), (c), or (d) fails despite the surface-level naming.

## 7. Operational test, and why naming the commitment as standalone matters

A hybrid composition satisfies hybrid composition coherence if and only if all of the following hold at all times during the composition's existence.

1. Layers are named explicitly per component (a) of §2 — the CKS layer and the adjacent-object layer(s) are architecturally identified and operationally distinguishable.
2. Each layer's architectural commitments are preserved per component (b) — the CKS layer satisfies A1.01, A1.02, A1.04, A1.06, and the other foundational commitments; each adjacent layer satisfies its own architectural commitments.
3. Boundaries between layers are operationally observable per component (c) — substrate writes, retrieval results, parametric outputs, and structured-memory operations are operationally distinguishable in the deployed system.
4. No inter-layer absorption of commitments occurs per component (d) — neither layer absorbs the other's architectural commitments.
5. The hybrid does not produce a single unified architecture; each layer can be reasoned about independently while operating in composition.
6. Composition requirements per A1.13 (per A2.75–A2.80) hold at the boundaries — per-substrate human governance is preserved, conflicts are preserved across boundaries, provenance is addressable across boundaries, AI-as-mediator commitment holds at every layer, and the composition decision is human-selective.

A hybrid that fails any of (1)–(6) does not satisfy hybrid composition coherence in the architectural sense, even if it operationally appears to combine the layers' features.

Implementations under pressure to deliver "comprehensive AI architectures" consistently drift toward presentations that frame hybrids as unified architectures. The drift is steady because unified-architecture framings are commercially attractive (audiences understand "one system" more readily than "composed layers with explicit boundaries"), operationally simpler in the short term (single-architecture management is easier to staff), and rhetorically appealing (unified architectures appear more sophisticated than composed architectures). Implementations that drift produce systems where hybrids collapse into one of their constituent layers operationally even when both layers are physically present, with downstream consequences manifesting as commitment-absorption failures (A1.01, A1.04, or A1.06 commitments collapse into the adjacent layer's posture), prior-art failures (the architectural distinction is lost, and the hybrid is treated as covered by the adjacent object's prior art), composition-requirement failures (A1.13's five requirements per A2.76–A2.80 cannot be operationally enforced because the boundaries are not observable), and architectural-credibility failures (the architecture's commitments cannot be defended when audiences read the hybrid as a unified system).

Naming hybrid composition coherence as a standalone architectural commitment — with the four operational components in §2, the three hybrids and their specific incoherence failure modes in §3, the limitations and adjacent-pattern distinctions in §4, the load-bearing connections in §5, and the ten failure modes in §6 — gives downstream readers a precise specification of why the boundary-naming the prior specializations provide matters operationally. With the integrating-frame note (A2.81) establishing the structure, the three adjacency specializations (A2.82, A2.83, A2.84) specifying the boundaries between CKS and RAG, parametric memory, and external structured memory, and this note specifying why those boundaries operationally matter, the three-adjacencies decomposition is fully formalized. The five notes together constitute the operational decomposition of A1.14: the boundaries enable coherent hybrid systems where CKS composes with one or more adjacent objects without confusion about which layer is doing what, and none of the three adjacent objects is a competitor to CKS in the zero-sum sense — each is a different design object serving a different design goal, and the value of naming the boundaries is precisely that it lets all three coexist with CKS in the same system without ambiguity about which layer is doing what.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Hybrid Composition Coherence: Why the Three Adjacency Boundaries Operationally Matter.* Derivation Note A2.85. May 5, 2026. ORCID: 0009-0004-8065-3235.
