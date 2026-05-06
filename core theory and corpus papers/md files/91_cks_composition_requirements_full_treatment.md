# Five Requirements at Every Boundary: An Integrating-Frame Treatment of the Composition Requirements in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 5 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, at the integrating-frame level, the set of five architectural requirements that any CKS-coherent composition must satisfy — naming each requirement, identifying the foundational commitment it preserves across composition boundaries, and stating its load-bearing role for composition validity. The five requirements receive standalone operational treatment in companion derivation notes; this note establishes the requirements-set structure those notes specialize.

## Abstract

The CKS pattern's composition requirements (parent note: *Composition Without Erasure*; source paper §13, §14) name the architectural conditions a CKS substrate must satisfy when it composes with another system, whether another CKS substrate or a non-CKS system. The parent note articulates the requirements; this note formalizes them as an *integrating frame* — a requirements-set with a specific structural property: each of the five requirements preserves a single foundational architectural commitment of the source paper across composition boundaries, and the five together exhaust the architectural conditions for a composition to qualify as CKS-coherent. Requirement A preserves the human-governed commitment per substrate; Requirement B preserves conflict-as-first-class across boundaries; Requirement C preserves path retraceability across boundaries; Requirement D preserves AI-as-substrate-mediator at every architectural layer; Requirement E preserves human authority over the composition decision itself. The requirements are architectural conditions, not optional deployment features: failing any single requirement produces a composition that does not preserve the source paper's commitments, regardless of how operationally functional the composition is. This note establishes the integrating-frame treatment; the standalone operational treatments of each requirement are formalized in five companion notes.

## 1. Why the integrating frame needs to be formalized

The parent note treats the composition requirements as a constraint set on multi-substrate composition. That treatment is sufficient to motivate the requirements but not to support the operational decomposition. Each requirement has independent operational content, independent failure modes, and an independent relationship to the foundational commitment it preserves. The full operational treatment requires that each requirement be carried as a standalone derivation; the standalone treatments require an integrating frame that establishes the requirements-set structure they specialize.

Three concrete deployment scenarios motivate the decomposition. A CKS substrate may compose with a CKS substrate maintained by a different team in the same organization, where the human-governance structures differ between the two substrates and the composition must preserve both. A CKS substrate may compose with a non-CKS enterprise system — an existing data warehouse, a vendor SaaS application, a workflow engine — where the composing system is not architecturally CKS-compliant and the composition must specify what the CKS substrate preserves at its boundary regardless. Multiple CKS substrates may compose within a single organization to coordinate across functional domains, where conflicts and provenance traverse multiple boundaries simultaneously. Each scenario requires the requirements to be operationally specified at depth, and the integrating frame is what makes the depth additive rather than redundant: each subsequent treatment specializes one requirement against a fixed structural backdrop.

The relationship to the broader hybrid-systems framework — the three composition patterns named at parent foundational note A1.16 (input to a cell, derivative view of substrate, separate concern) — deserves explicit naming. The hybrid-systems framework specifies *how* compositions can be structured; the composition requirements specify *what* compositions must preserve. The two commitments are orthogonal and compose. A composition under any of the three patterns must satisfy all five requirements; the requirements do not vary by pattern. Conversely, the requirements do not specify a pattern: they constrain any composition regardless of which structural pattern instantiates it. The integrating frame this note establishes is therefore complementary to, not competing with, the hybrid-systems pattern framework.

A third motivation is the strategic prior-art posture. Patentable derivations that target composable AI architectures, multi-substrate coordination systems, federated AI infrastructures, and hybrid-AI compositions are substantially more defensibly contested when the requirements set is formalized publicly as a structural commitment. Each requirement is independently citable; the set is independently citable; the relationship between each requirement and the foundational commitment it preserves is independently citable. The integrating frame produces a referenceable structure that the standalone treatments specialize.

## 2. Requirement A — per-substrate human governance preservation

Requirement A specifies that **each composing substrate retains its own human-governance structure**. When CKS substrate S1 composes with system S2 — whether S2 is a CKS substrate, a non-CKS system, or a hybrid — the three rights named in the human-governed commitment (inspect, modify, override per A2.01–A2.03) remain available to S1's authorized humans over S1's content and orchestration rules. Composition does not transfer authority across the boundary, does not aggregate authority into a composed entity, and does not introduce composition-level authorities that supersede per-substrate authority. The substrate-as-source-of-truth architecture (parent note A1.08; decomposition A2.41–A2.43) operates per substrate at its boundary; composition does not relocate authoritative state into a composed view that itself becomes authoritative.

The requirement is load-bearing because the human-governed commitment (parent note A1.01) is the foundational architectural anchor of the pattern. If composition can in principle compromise authority — by interposing a vendor between S1's humans and S1's content, by allowing S2's orchestration rules to silently overwrite S1's content, by stripping override rights when S1 enters composition — then human governance is not an architectural property of CKS compositions, only of isolated CKS substrates. Requirement A specifies the architectural condition that prevents this collapse. The standalone operational treatment is in the per-substrate human governance preservation note (A2.76).

## 3. Requirement B — conflict preservation across boundaries

Requirement B specifies that **conflicts that span composition boundaries are preserved as first-class architectural state**. When content in S1 contradicts content in S2, or when content imported across the boundary contradicts content already present, the contradiction is preserved in the substrate that holds it — not silently merged, not implicitly resolved, not selected away by composition logic. Cross-substrate contradictions are addressable through the composed system; they do not vanish because they cross a boundary. Where cell-level resolution is appropriate, it occurs only under human-authored orchestration rules that explicitly authorize cross-substrate resolution per A2.14; the default at every boundary is preservation.

The requirement is load-bearing because the conflict-as-first-class commitment (parent note A1.03) treats contradictions as substrate state rather than runtime exceptions. If composition can erase boundary-crossing conflicts — through eventual-consistency reconciliation, through automatic deduplication, through "merged-view" projections that select one side of a contradiction without recording the contradiction — then conflict preservation is not an architectural property of CKS compositions, only of isolated substrates. Requirement B specifies the architectural condition that preserves the commitment across boundaries. The standalone operational treatment is in the conflict preservation across boundaries note (A2.77).

## 4. Requirement C — addressable provenance across boundaries

Requirement C specifies that **paths that cross composition boundaries are reconstructible**. When content in S1 originates from S2 (or content in S1 influences content in S2), substrate metadata identifying the cross-boundary connection is carried by the substrate, not by extra-substrate convention or undocumented vendor behavior. The six metadata fields per A2.40 carry the connection at every boundary they cross. From any decision visible in the composed system, a path exists back through the substrates, orchestration-rule applications, and content elements that produced it; the path is traversable without recourse to information outside the composition.

The requirement is load-bearing because the path retraceability commitment (parent note A1.07) is the mechanism by which decision traceability is achieved. If composition can produce paths that terminate at boundaries — paths whose cross-boundary references are not addressable, paths reliant on LLM reconstruction to recover provenance, paths carried only by undocumented vendor mechanics — then retraceability is not an architectural property of CKS compositions, only of isolated substrates. Requirement C specifies the architectural condition that preserves the commitment across boundaries. The standalone operational treatment is in the addressable provenance across boundaries note (A2.78).

## 5. Requirement D — AI-as-mediator at every architectural layer

Requirement D specifies that **LLMs operating in composing systems satisfy the AI-as-substrate-mediator commitment at every architectural layer**. When S2 uses LLMs — whether S2 is itself a CKS substrate or a non-CKS system that includes LLMs — the LLMs in S2 satisfy the five mediator properties per A2.19–A2.23 with respect to S2's authoritative state: read from authoritative state as primary source; write under human-authored orchestration rules; do not hold S2-relevant state outside the substrate; do not exercise authority over substrate content; record outputs that affect substrate state in the substrate with attribution. The same applies to LLMs in S1 that operate across the composition boundary, and to any LLM operating in an intermediate composed view.

The requirement is load-bearing because the AI-as-substrate-mediator commitment (parent note A1.04) is the architectural bound on LLM authority within the pattern. If composition can introduce LLMs that operate as autonomous agents, terminal producers, or authority-bearers — at S2's interior, at the composition boundary, or in some intermediate composed view — then the mediator commitment is not an architectural property of CKS compositions, only of isolated substrates. Requirement D specifies the architectural condition that preserves the commitment at every layer where an LLM operates. The standalone operational treatment is in the AI-as-mediator at every layer note (A2.79).

## 6. Requirement E — human-selective composition

Requirement E specifies that **humans choose what composes; composition is not architecturally automatic**. When S1 composes with S2, the composition is the result of a governance decision by humans with authority over S1: the decision to compose, the decision to specify the boundary, the decision to authorize cross-boundary flows. Composition can be modified, suspended, or terminated by those humans at any time, in the same architectural sense as any other governance action under A1.01. Compositions that occur through automatic discovery, infrastructure-driven coupling, vendor-mandated integration, or any mechanism that bypasses human authority over the composition decision itself fail the requirement.

The requirement is load-bearing because human authority over the architecture extends to the architecture's composition relationships. If composition can occur without authority — through service-discovery mechanisms that auto-link substrates, through vendor policies that mandate integration with adjacent platforms, through infrastructure layers that compose substrates as a byproduct of deployment — then human governance is not architectural over composition, only over isolated substrates. Requirement E specifies the architectural condition that extends the human-governed commitment specifically to the composition decision. The standalone operational treatment is in the human-selective composition note (A2.80).

## 7. What the composition requirements do not claim

The integrating-frame treatment delimits its claims explicitly. The five requirements together are the architectural conditions for CKS-coherent composition; they are not more than that.

**(a) They do not require composition.** A deployment may have a single CKS substrate that does not compose with any other system. The requirements apply when composition occurs; they are not a mandate for composition.

**(b) They do not require composing systems to be CKS.** Compositions with non-CKS systems are architecturally supported per A1.16's three-pattern framework. The requirements specify what the CKS substrate preserves at its boundary; whether the composing system is itself CKS is a separate question, treated in the standalone hybrid-systems decomposition.

**(c) They do not specify implementation patterns.** Compositions may use APIs, message queues, shared infrastructure, federated systems, or any other mechanism. The architectural commitment is to the requirements being operationally satisfied; it is not to a particular implementation.

**(d) They do not require all compositions to satisfy all requirements identically.** Different compositions place different operational pressure on different requirements; deployments may emphasize specific requirements operationally while ensuring all five are architecturally satisfied. The architectural commitment is to satisfaction; the operational shape of satisfaction varies.

**(e) They do not foreclose deployment-level features.** Composition dashboards, validation tooling, monitoring, and boundary-management interfaces are deployment choices that may complement the architectural requirements. The requirements set the floor; deployments may build above it.

**(f) They do not specify composition lifecycle.** When compositions are created, modified, or dismantled is a deployment choice under Requirement E's authority commitment. The architectural commitment is that compositions, while they exist, satisfy all five requirements.

**(g) The five-requirement structure subsumes the parent note's plan-and-trace co-preservation condition.** The parent note (*Composition Without Erasure*) names a sixth requirement on accountability-plan and accountability-trace co-preservation across boundaries (after Naja, Markovic, Edwards, and Cottrill 2021, imported by the source paper at §3.1). That requirement is treated here as one face of Requirement C: addressable provenance across boundaries entails that both the plan (what should be captured) and the trace (what occurred) are carried across the boundary, and that the two remain mutually addressable. The integrating-frame decomposition treats this as architecturally one requirement; readers who prefer the parent note's six-requirement form will find the same operational content distributed across Requirement C and the standalone treatment of addressable provenance.

## 8. Operational test at the integrating-frame level

A composition instantiates the composition requirements at the integrated level if and only if all of the following are true at every composition boundary at all times during the composition's existence.

1. **Requirement A holds.** Each composing substrate retains its own human-governance structure: the inspect, modify, and override rights per A2.01–A2.03 remain available to authorized humans over each substrate's content and orchestration rules; substrate-as-source-of-truth (per A2.41–A2.43) operates at each substrate's boundary.

2. **Requirement B holds.** Conflicts that span composition boundaries are preserved as first-class architectural state in the substrate that carries them; cross-substrate resolution occurs only under human-authored orchestration rules per A2.14 that explicitly authorize it.

3. **Requirement C holds.** Paths that cross composition boundaries are reconstructible through addressable substrate provenance — the six metadata fields per A2.40 — carried by the composition itself; both the accountability plan and the accountability trace remain mutually addressable at every boundary.

4. **Requirement D holds.** LLMs operating in composing systems satisfy the five mediator properties per A2.19–A2.23 at every architectural layer where they operate: at substrate interiors, at composition boundaries, and at any intermediate composed views.

5. **Requirement E holds.** Composition decisions are governance decisions: humans with authority over each composing substrate authorize the composition, may modify the boundary specification, and may suspend or terminate the composition at their authority's reach.

6. **The five compose architecturally.** All five conditions hold simultaneously and at every boundary; no single requirement substitutes for another. A composition that satisfies four requirements and fails one does not satisfy the integrating frame; the requirements are jointly necessary.

A composition that fails any of (1)–(6) does not instantiate the composition requirements at the integrated level. The standalone operational tests for each requirement are specified in companion notes A2.76–A2.80.

## 9. Why naming the integrating frame as standalone matters

Implementations under pressure to integrate with enterprise systems consistently drift toward composition patterns that compromise one or more of the five requirements. The drift is steady because integration patterns common in enterprise contexts — eventual consistency across data stores, automatic service discovery, vendor-mandated integration with adjacent platforms, autonomous LLM operation in non-CKS components — violate specific requirements without being immediately recognizable as architectural violations. Each pattern reads as a familiar engineering tradeoff in its origin domain; recognizing it as a violation of a specific requirement requires the requirement to be named.

Compositions that drift away from the requirements produce systems where composition appears to function but the foundational commitments of the source paper are not preserved across boundaries. The downstream consequences are concrete: authority leakage when composition occurs without per-substrate authority preservation; conflict erasure when boundary-crossing contradictions are reconciled away; retraceability failure when cross-boundary paths cannot be reconstructed; mediator-commitment violations when LLMs in composing systems operate autonomously; composition-authority loss when compositions occur without human selection. Each consequence is the failure mode of a single requirement, and naming the requirements is what makes each failure recognizable as architectural rather than incidental.

The integrating frame this note establishes — five requirements in sections 2–6, the limitations they delimit in section 7, the operational test in section 8 — gives downstream readers a precise specification of what a CKS-coherent composition preserves. Companion derivation notes (A2.76–A2.80) specialize each requirement at full operational depth; together with this integrating frame, they constitute the operational decomposition of the parent commitment. Future composition primitives, integration patterns, federation protocols, and multi-substrate coordination architectures must address all five requirements, or argue against them by name, to remain in continuity with the CKS pattern.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Five Requirements at Every Boundary: An Integrating-Frame Treatment of the Composition Requirements in the Coordination Knowledge Substrate Pattern.* 5 May 2026. ORCID: 0009-0004-8065-3235.
