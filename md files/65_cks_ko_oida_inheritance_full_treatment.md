# KO and OIDA Inheritance Along the Multi-Human Axis: An Integrating Frame for the Prior-Art Positioning Decomposition in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 5 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to provide the integrating frame for the CKS prior-art positioning decomposition: naming, at the integrating level, what CKS inherits from Knowledge Objects (KO), what CKS inherits from OIDA, the two-axis extension structure under which both inheritances are extended, the architectural-difference-vs-feature-addition claim that distinguishes CKS from the naive composition "OIDA + multi-human capability," and the multi-human operational requirements introduced by the extension. Each component is specialized at full operational depth in a sibling note; this note's contribution is the integration that makes the specializations compose into one defensible prior-art posture.

## Abstract

The CKS pattern positions itself relative to two adjacent prior-art lines — Knowledge Objects (Zahn & Chana 2026) and OIDA (2026 preprint) — and the relationship is consequential for the architecture's prior-art posture. The parent foundational treatment consolidates the inheritance into one continuous derivation. This note takes the further step of decomposing the inheritance into five components — KO inheritance, OIDA inheritance, the two-axis extension structure, the architectural-difference claim, and the multi-human operational requirements — and provides the integrating frame under which the components compose. The note articulates what each component contributes, names the simultaneity of the two extension axes (multi-human + governance) as the load-bearing architectural content, identifies five clarifications that bound the integrating-frame claim, and provides an integrating-frame operational test. Sibling notes specialize each component standalone; this note's contribution is the integration that lets the specializations compose into one defensible prior-art posture.

## 1. Why the prior-art inheritance commitment needs an integrating frame

The parent foundational note formalizes CKS's inheritance from KO and OIDA along the multi-human axis as a single architectural commitment. The treatment is correct as far as it goes, and this note does not contradict it. What it adds is a decomposition: the inheritance commitment has internal structure, and that structure can be specialized into five components — KO inheritance, OIDA inheritance, the two-axis extension structure, the architectural-difference claim, and the multi-human operational requirements — each of which carries independent derivational weight. A specialization cannot stand on its own without an integrating frame, because the components' coherence is what makes the inheritance commitment what it is.

The motivating cases are deployments and analyses that need to position CKS in relation to its prior-art landscape. Without precise specification of what CKS inherits from KO versus what it inherits from OIDA, what is fresh in CKS, and how the extension structure operates, CKS appears either over-claimed (presented as wholly novel when much is inherited) or under-claimed (presented as an incremental variant when the architectural-difference claim is load-bearing). Both drifts produce inaccurate positioning. The integrating-frame treatment, paired with the five specializations, makes the inheritance specific.

A second motivation is the connection to the already-formalized treatment of OIDA signed contradiction edges as cited prior art for the relationship-metadata requirement in conflict provenance. That treatment is one specific inheritance point at one specific architectural commitment (conflict-as-first-class). The integrating frame this note establishes makes that case visible as one instance of a broader inheritance pattern, with KO and OIDA each contributing distinct architectural elements that compose into the CKS foundation. The component specializations articulate other inheritance points at other commitments; the integrating frame is what lets those points compose into a single posture rather than scattering as independent borrowings.

## 2. KO inheritance, named at the integrating level

CKS inherits from Knowledge Objects (Zahn & Chana 2026) the substrate-and-cell decomposition pattern for human-LLM coordination at single-human scope. At the integrating level, the inheritance covers four elements:

(a) **Substrate as persistent inspectable artifact.** The substrate is the persistent, addressable, human-readable carrier of coordination state, separable from session memory and from LLM-internal representations.

(b) **Cells as operational units over substrate.** Cells are the operational units that read from and write to substrate content under structured rules.

(c) **The substrate-cell boundary.** The boundary between persistent substrate state and ephemeral cell computation is the architectural separator that makes both layers independently describable.

(d) **Orchestration governing cell behavior.** Cells operate over substrate content under orchestration that determines how they execute, what they read, what they write, and under what conditions.

CKS extends each of these elements from single-human to multi-human scope and from procedural to architectural governance. The extensions are specialized in the multi-human-axis specialization, the two-axis-structure specialization, and the architectural-difference specialization. The KO inheritance proper — what carries forward from KO into CKS, and on what terms — is specialized standalone in the KO-inheritance sibling note.

## 3. OIDA inheritance, named at the integrating level

CKS inherits from OIDA (2026 preprint) the structured-information-flow pattern with provenance-aware relationships and signed contradiction edges. At the integrating level, the inheritance covers four elements:

(a) **Information as structured content with schema-defined relationships.** Substrate content is not opaque text or unstructured retrieval target; it is structured content with typed relationships that the substrate's schema makes explicit.

(b) **Decisions as first-class outputs of orchestrated processes.** Decisions produced by orchestrated cell execution are themselves substrate content, attributed to the orchestration step that produced them, and addressable as first-class state rather than as ephemeral inference outputs.

(c) **Signed contradiction edges as a representation primitive.** Contradicting content is preserved through signed edges that carry their own schema presence and persist as substrate state. The already-formalized treatment of this inheritance point at the conflict-as-first-class scope is one specialized rendering of this element.

(d) **Provenance fields attached to content for auditability.** Substrate content carries provenance metadata that makes the path from input to current state traceable.

CKS extends each of these elements along both the multi-human axis and the governance axis, with extensions formalized in the two-axis-structure specialization, the architectural-difference specialization, and the multi-human-requirements specialization. The OIDA inheritance proper — what carries forward from OIDA into CKS, including the relationship to the already-formalized signed-contradiction-edge inheritance point — is specialized standalone in the OIDA-inheritance sibling note.

## 4. The two-axis extension structure

CKS extends the inherited KO and OIDA architectural patterns along two axes simultaneously. The simultaneity is the load-bearing architectural content; sequential extension along the two axes would not produce CKS.

**Multi-human axis.** The first axis is the move from single-human authority (the scope at which KO and OIDA operate) to multi-human authority structure (the scope CKS commits to). The substrate carries the authority structure as substrate content; provenance distinguishes multiple human writers; conflict-handling operates across multi-human authority boundaries; substrate-only paths operate within multi-human governance. The multi-human-requirements specialization renders these properties at full operational depth.

**Governance axis.** The second axis is the move from procedural governance (workflows, approval processes, scheduled audit cycles) to architectural governance (substrate-resident authority, three rights at all times per the human-governed commitment, no-justification-as-precondition for override per the override-right specialization, and the architectural-vs-procedural qualifier per the governance-architecturalness specialization).

The two axes operate together rather than sequentially. Each axis requires the other to be operationally coherent. Multi-human authority requires architectural governance because procedural governance fragments under multiple human authorities — workflow gates designed for one principal cannot consistently arbitrate among many, and approval cycles introduce ordering that is not architecturally meaningful when authority is genuinely distributed. Architectural governance requires multi-human authority because single-human architectural governance collapses to single-user authorization — the three rights become trivially satisfied by the lone principal, and the no-justification-as-precondition property of override loses architectural content when there is no other party for justification to be owed to.

The simultaneity is what distinguishes the extension from a feature addition. A feature-addition extension treats one axis as the base and the other as decoration on top; the architectural extension treats both as constitutive. The two-axis-structure specialization renders the simultaneity at full operational depth.

## 5. The architectural-difference-vs-feature-addition claim

CKS is architecturally different from the naive composition "OIDA + multi-human capability" rather than being a feature-extension of OIDA. The claim is load-bearing for prior-art positioning because the most plausible reviewer or implementer misreading at the scope where OIDA is silent and CKS is most distinctive is precisely the "OIDA plus multi-human" reading. The source paper protects the phrase across §5.2 (core scope) and §9.4 (extension scope) for this reason.

At the integrating level, the architectural difference manifests in four ways.

(a) **Authority is architecturally substrate-resident, not procedurally enforced.** "OIDA + multi-human capability" would add authorization workflows on top of an OIDA core; CKS bakes authority structure into substrate content. The location of authority is an architectural commitment, not a deployment policy choice.

(b) **Conflict handling operates at substrate level as first-class state, not at orchestration level as exception management.** OIDA's signed contradiction edges are inherited as a representation primitive but extended to first-class architectural status under the conflict-as-first-class commitment. The extension is not a feature added on top of OIDA; it is the substrate's stance toward contradiction.

(c) **Path retraceability operates through substrate alone, not through external audit infrastructure.** OIDA's auditability is procedurally extensible; CKS's retraceability is architecturally substrate-bounded under the substrate-only-paths commitment. The audit story does not depend on infrastructure outside the substrate.

(d) **Tool-agnosticism makes CKS host-agnostic.** OIDA implementations are typically platform-bound; CKS commits to commodity-tool realizability under the tool-agnosticism commitment and its specializations. Hosting flexibility is an architectural property, not an implementation accident.

The architectural-difference specialization renders the four manifestations at full operational depth, including operational tests by which a candidate system can be assessed against each.

## 6. Multi-human axis operational requirements, at the integrating level

The multi-human extension introduces five operational requirements not present in single-human KO/OIDA architectures. Naming them at the integrating level fixes their referents; the multi-human-requirements specialization renders each one standalone.

(a) **Authority structure as substrate content.** Who holds what authority over what substrate scope is itself substrate-resident state, not external configuration.

(b) **Writer attribution distinguishing multiple human writers.** Provenance fields carry human identity at write time; substrate content can be traced to the human who wrote it under the path-retraceability commitment.

(c) **Conflict-handling rules across human-authority boundaries.** When human writers under different authority scopes produce conflicting content, the substrate preserves the conflict as first-class state under the conflict-as-first-class commitment, and the orchestration rules govern the cell-level response.

(d) **Substrate-only paths across multi-human governance.** Audit and accountability paths run through substrate content alone, not through external coordination infrastructure that bridges multi-human authority outside the substrate.

(e) **Override authority distribution without architectural escalation hierarchy.** Multiple humans hold override rights within their scopes; the architecture does not require a single privileged human as escalation endpoint. The no-justification-as-precondition property of override holds for each authority-holder within scope.

Each requirement is the multi-human-scope rendering of a commitment that already had architectural content at the single-human scope. None is a feature added on top of an unchanged base.

## 7. What the inheritance commitment does NOT claim

The integrating-frame treatment is bounded. Five clarifications keep it from drifting into something stronger than the source paper supports.

**(a) KO and OIDA are not the only prior-art sources.** Other architectures — workflow systems, business-process-management platforms, data-flow architectures, multi-agent systems — are adjacent to CKS in various ways. The three-adjacencies treatment and the orchestration-layer-distinctions treatment specialize the principal adjacencies (RAG, parametric memory, external structured memory; workflow engines, agent frameworks, control planes). The KO/OIDA inheritance is the primary architectural lineage; the other adjacencies are positioned as distinctions, not as inheritances.

**(b) CKS does not reproduce KO or OIDA in their entirety.** Specific KO and OIDA features may be absent from CKS where they conflict with the multi-human axis or the governance axis. The inheritance is selective: architecturally-coherent elements carry forward; elements specific to single-human or procedurally-governed contexts do not.

**(c) The two-axis extension is not exhaustive.** Future architectural extensions may add additional axes — the multi-Self extension introduced in the second CKS theory paper, the inter-Self extension introduced in the third, and any further extensions subsequent papers introduce. The two-axis structure named here is the foundational extension within the source paper's scope, not the final structure.

**(d) CKS is not a strict superset of KO or OIDA.** Some KO/OIDA capabilities may not be expressible in CKS architecture without modification. The inheritance is by architectural pattern, not by feature equivalence.

**(e) The inheritance does not specify implementation lineage.** CKS implementations may or may not derive operationally from KO or OIDA implementations, and the architectural inheritance does not commit either way. The inheritance is at the architectural-pattern level, not at the codebase level.

## 8. Operational test at the integrating-frame level

A system instantiates the CKS prior-art inheritance commitment at the integrated level if and only if all of the following are true.

1. The system inherits the KO substrate-and-cell decomposition pattern: substrate as persistent inspectable artifact, cells as operational units, the substrate-cell boundary as architectural separator, and orchestration governing cell behavior over substrate content.

2. The system inherits the OIDA structured-information-flow pattern: information as structured content with schema-defined relationships, decisions as first-class outputs of orchestrated processes, signed contradiction edges as a representation primitive where applicable, and provenance fields attached to content for auditability.

3. The system extends the inheritance along the multi-human axis and the governance axis simultaneously, not sequentially. Each axis is constitutive; neither operates as decoration on top of the other.

4. The system is architecturally different from "OIDA + multi-human capability," with the difference manifesting in substrate-resident authority, first-class substrate-level conflict state, substrate-only retraceability, and tool-agnostic hosting.

5. The system satisfies the five multi-human operational requirements: authority structure as substrate content, writer attribution distinguishing multiple human writers, conflict-handling rules across human-authority boundaries, substrate-only paths across multi-human governance, and override authority distribution without architectural escalation hierarchy.

A system that fails any of (1)–(5) does not instantiate the prior-art inheritance commitment at the integrated level. The component-level operational tests for each inheritance source, the two-axis structure, the architectural-difference claim, and the multi-human operational requirements are specified in the corresponding component specializations.

## 9. Why naming the integrating frame as standalone matters

Implementations under pressure to position CKS against prior art consistently drift in two directions. One drift is over-claiming: presenting CKS as wholly novel, obscuring the inheritance from KO and OIDA, and weakening the architectural-difference-vs-feature-addition claim that depends on the inheritance being specifically named. The other drift is under-claiming: presenting CKS as an OIDA variant or a KO-with-extras, conceding territory the source paper does not concede, and admitting "OIDA + multi-human" implementations as CKS-equivalent. Both drifts produce inaccurate positioning. The over-claim drift loses credibility when the inheritance is identified independently; the under-claim drift weakens the prior-art posture, conceding precisely the framing the architectural-difference claim is designed to refuse.

Naming the prior-art inheritance integrating frame as a standalone architectural commitment — with KO inheritance specified in §2, OIDA inheritance in §3, the two-axis extension structure in §4, the architectural-difference claim in §5, the multi-human operational requirements in §6, the limitations in §7, and the operational test in §8 — gives downstream readers a precise specification of what the commitment integrates. The component specializations render each component at full operational depth; together with this integrating frame, they give the full operational decomposition of the parent foundational note. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should address the inheritance commitment as integrated here. Subsequent work that uses the inheritance differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion notes

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inheritance and Extension: How CKS Builds on Knowledge Objects and OIDA Along the Multi-Human Axis.* 27 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *KO and OIDA Inheritance Along the Multi-Human Axis: An Integrating Frame for the Prior-Art Positioning Decomposition in the Coordination Knowledge Substrate Pattern.* 5 May 2026. ORCID: 0009-0004-8065-3235.
