# Shared Substrate as Paper 3's First Architectural Claim

**Note ID:** D0.01 | **Series:** D | **Number:** #460  
**Author:** Wenxin Li (Independent Researcher)  
**ORCID:** 0009-0004-8065-3235  
**Date:** May 14, 2026  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 of the Coordination Knowledge Substrate (CKS) theory series takes the architecturally complete AI Self established in Paper 2 as its starting unit and develops the architecture of inter-Self coordination: how two or more CKS-governed Selves exchange content, handle conflict, feed evolution, and configure coordination behavior, all under unified human governance. Paper 3's first and foundational claim establishes the **shared substrate** as the architectural object through which this coordination occurs — a CKS substrate temporarily constructed for an inter-Self interaction, spanning the governance perimeters of more than one participating Self, carrying all six Paper 1 architectural commitments within its scope, and dissolving upon the interaction's completion, with what persists afterward governed as authored substrate content. This note formalizes Claim 1 as the anchor commitment for Series D, Paper 3's derivation series in the CKS defensive-publication program. It states the claim precisely, explains its four defining properties, identifies its named architectural foil (opaque agent-to-agent communication), maps the inheritance relationship to Papers 1 and 2, maps the five sub-commitments (D1.01–D1.05) that derive from Claim 1, and provides an operational test for whether a given system instantiates it.

---

## 1. Paper 3's place in the trilogy and the role of Claim 1

Paper 1 of the CKS theory series establishes the substrate as the medium of coordination within a single cell: a persistent, human-governed object outside the LLM whose content is authoritative, whose governance is exercised through human authority over inspection, modification, and override, and whose relationship to the LLM is that of mediator rather than producer. Paper 1 defends six architectural commitments at cell scope — substrate-as-coordination-artifact, human governance, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, and linear-cost scaling — that jointly specify what it means for a cell-level system to be CKS-governed.

Paper 2 extends the substrate commitment across cells, aspects, and the complete AI Self under the instinct/reasoning separation. At Self scope, the substrate continues to carry coordination, governance, and reasoning content, while the LLM carries fast-pattern instinct. The Self's internal architecture composes cells into aspects and aspects into the Self under a three-level DNA and action layer structure, with Paper 2's six claims specifying the instinct/reasoning separation, multi-level composition, lifecycle primitives, three evolution mechanisms, multi-shaped governance, and the enterprise brain Self as design pattern.

Paper 3 extends the substrate commitment one further step: to the medium through which two or more complete CKS-governed Selves coordinate with each other. This extension occupies Rung 5 of the substrate-mediator ladder that the trilogy observes across six configurations of progressively larger scope. Paper 3's six claims specify what that inter-Self coordination architecture commits to, beginning with Claim 1's establishment of the architectural object the remaining five claims operate over, within, and through.

Claim 1 is Paper 3's foundational commitment in a precise sense: Claims 2 through 6 presuppose its existence. Full Aspect Integration (Claim 2) operates over the shared substrate. Three-tier conflict handling (Claim 3) operates within it. The four-locus evolution feed (Claim 4) runs from it. Configuration as substrate content (Claim 5) applies recursively to it. Population-scale collective evolution (Claim 6) composes across accumulated instances of it. If Claim 1 is not in place, none of the remaining claims have a substrate to operate over.

---

## 2. Claim 1 stated precisely

**Claim 1:** The architectural object of inter-Self coordination in a CKS-governed multi-Self system is a shared substrate — a CKS substrate constructed temporarily for a Full Aspect Integration event, whose governance perimeter spans the home governance perimeters of two or more participating Selves, within which all six Paper 1 architectural commitments hold, and which dissolves upon the event's completion with what persists afterward specified as authored substrate content under joint human authority.

The shared substrate is not a communication channel. It is not a message-passing layer. It is not a shared-memory store whose access patterns are governed separately from its content. It is a CKS substrate — the same architectural object Paper 1 establishes at cell scope — instantiated at inter-Self scope. Everything that makes a Paper 1 substrate a Paper 1 substrate applies within the shared substrate's governance perimeter: content is authoritative and persistent within that perimeter; governance is human authority over inspection, modification, and override; conflict is preserved as first-class substrate content rather than resolved silently at exchange time; the AI systems participating in the exchange are substrate-mediators, not substrate-owners; tools used to access or modify the substrate are interchangeable without substantive governance loss; and governance cost does not scale with substrate volume.

The only property that is genuinely new at inter-Self scope is the governance perimeter's shape: it spans more than one Self's home perimeter. This produces a perimeter that crosses organizational boundaries, that requires joint human authority from the governance structures of the participating Selves, and whose configuration — including which content crosses, under what conditions, and under whose authority — is itself substrate content governed by the joint authority the perimeter represents.

---

## 3. The four defining properties of the shared substrate

**Property 1: Temporary construction for an FAI event.** The shared substrate is constructed at the initiation of a Full Aspect Integration event and dissolves upon that event's completion. It is not a persistent inter-Self coordination infrastructure that exists independently of specific inter-Self interactions. Each FAI event produces its own shared substrate instance. This property matters architecturally because it prevents the accumulation of ungoverned inter-Self state: there is no standing shared substrate whose contents drift beyond the scope of any particular interaction's governance configuration. The construction-and-dissolution cycle is itself architecturally governed.

**Property 2: All six Paper 1 commitments hold within scope.** The shared substrate inherits Paper 1's full commitment set without modification. Human governance holds within the shared substrate's perimeter: participating humans retain the authority to inspect, modify, and override substrate content at any time during the FAI event. Conflict preservation holds: conflicting content contributed by different Selves is preserved as first-class substrate state rather than silently merged or resolved. AI-as-substrate-mediator holds: AI systems operating over the shared substrate mediate access to and transformation of substrate content; they do not author the substrate's governance rules. Tool-agnosticism holds: the shared substrate's governance commitments do not depend on any particular tooling for their integrity. Linear-cost scaling holds: adding content to the shared substrate does not cause governance cost to scale super-linearly. These commitments hold not by Paper 3's independent assertion but by inheritance from Paper 1 through the shared substrate's identity as a CKS substrate.

**Property 3: Governance perimeter spanning multiple Selves' home perimeters.** This is the property that distinguishes the shared substrate from any single Self's internal substrate. A home perimeter is the governance boundary within which a Self's internal CKS architecture operates as specified by Paper 2. The shared substrate's governance perimeter contains the home perimeters of all participating Selves without replacing or collapsing them: each Self's internal architecture continues to operate exactly as Paper 2 specifies throughout the FAI event. The shared substrate adds an inter-Self coordination scope alongside the home perimeters; it does not substitute for them. The perimeter-spanning property requires joint human authority: no single Self's governance structure governs the shared substrate unilaterally. What crosses the inter-Self perimeter, under what conditions, and on whose authority are all themselves substrate content under that joint authority.

**Property 4: Persistence policy as governed substrate content.** When the shared substrate dissolves at FAI event completion, what persists — and where it persists — is governance-configured per event. The configurable range runs from nothing retained (the shared substrate dissolves completely, leaving no trace in either participating Self's home substrate) to the full shared substrate retained as a durable cross-perimeter record. Between those extremes, per-event governance configuration specifies which content feeds which Self's home substrate through the four-locus evolution feed mechanism Paper 3's Claim 4 develops. The persistence policy is not an operational decision external to the architecture; it is authored substrate content within the shared substrate itself, under joint human authority, before or during the FAI event it governs.

---

## 4. The named foil: opaque agent-to-agent communication

Claim 1 is a claim rather than a description because it takes a position against a specific architectural alternative. The named foil is **opaque agent-to-agent communication**: inter-AI exchange conducted through message-passing, tool-call sequences, or shared-memory access patterns whose substantive content is not human-governable as authored substrate.

Opaque agent-to-agent communication takes several architectural forms, all sharing the same structural property: the exchange medium is not itself a CKS substrate. Message-passing between AI agents produces exchange content whose provenance, conflict structure, and authority trail are internal to the message stream rather than authored and persistent in a human-governed substrate. Tool-call-based inter-AI exchange produces coordination through a sequence of calls and responses whose aggregate content is not organized as substrate content subject to the six Paper 1 commitments. Shared-memory access patterns produce coordination through memory reads and writes whose governance, if any, is retrofitted around the exchange rather than intrinsic to it.

The retrofit framing is the architectural diagnostic. An approach is in the foil category when CKS commitments are added around an opaque exchange medium — when governance wraps the exchange — rather than when the exchange medium is itself CKS substrate from the start. Governance-retrofitted approaches preserve the structural feature that makes them foils: the substantive exchange content is not human-governable as authored substrate during the exchange, only after the fact and only incompletely.

Claim 1's response to the foil is not to add governance around inter-AI exchange but to specify the exchange medium itself as a CKS substrate from the start. The shared substrate is the exchange medium; it is CKS-governed in the same sense Paper 1's substrate is CKS-governed at cell scope. Governance is not retrofitted around it; governance is the substrate's architectural identity.

Four specific foil patterns that Claim 1 forecloses:

- Agent-to-agent message passing whose substantive content is not organized as authored substrate with provenance, conflict registration, and human override authority
- Shared-memory coordination where memory access patterns produce effective coordination that is not governed as authored substrate content
- Tool-call-based inter-AI exchange where the exchange medium is not a CKS substrate and the exchange's content trail is not human-inspectable as substrate content
- Governance-retrofitted approaches where Paper 3 commitments are applied around an opaque exchange rather than being intrinsic to the exchange medium

---

## 5. Inheritance from Papers 1 and 2

The shared substrate's relationship to Papers 1 and 2 is inheritance and extension, not replacement. Three inheritance relationships are architecturally load-bearing for Claim 1.

**From Paper 1: The substrate-as-medium commitment at inter-Self scope.** Paper 1 defends the substrate as the medium of coordination within a cell. Claim 1 carries that commitment one scope further. The architectural move is identical in structure: the substrate is the medium; the medium carries the governance commitments; governance is human authority within the medium's perimeter. What changes is only the perimeter's scope — cell scope in Paper 1, inter-Self scope in Paper 3.

**From Paper 2: The Self as the unit of participation.** The shared substrate's perimeter spans the home perimeters of CKS-governed Selves in the sense Paper 2 specifies. Each participating Self's internal architecture — instinct/reasoning separation, multi-level composition, three evolution mechanisms, governance shape — continues to operate exactly as Paper 2 specifies during the FAI event. The shared substrate adds an inter-Self coordination scope alongside home operations; it does not modify them. The unit of contribution to the shared substrate is the aspect from Paper 2: when a Self contributes content to the shared substrate, the contribution surfaces the constituent cells, DNA-layer content, and action-layer content of contributed aspects. Instinct-layer content does not cross the inter-Self perimeter; the instinct/reasoning separation Paper 2 establishes extends at the inter-Self boundary.

**Trilogy position: Rung 5 of the substrate-mediator ladder.** The substrate-mediator commitment progresses across the trilogy at six configurations of progressively larger scope. Rung 1 is single human ↔ LLM within one cell (Paper 1 core theory). Rung 2 is multiple humans ↔ LLM within one cell (Paper 1 extension claim). Rung 3 is cell ↔ aspect ↔ Self within one Self (Paper 2 core theory). Rung 4 is the enterprise brain Self (Paper 2 extension claim). Rung 5 is Self ↔ Self mediated by shared substrate — the scope Claim 1 establishes. Rung 6 is population-scale collective dynamics across many Selves (Paper 3 extension claim, Claim 6). Claim 1 occupies the architectural position where the substrate-mediator commitment crosses the inter-Self perimeter for the first time.

---

## 6. Derived sub-commitments: D1.01–D1.05

Claim 1's four defining properties decompose into five foundational sub-commitments that Phase D1 formalizes as standalone prior-art notes. The mapping is:

**D1.01 — Shared substrate as temporary construction.** The shared substrate is constructed at FAI event initiation and dissolves at completion. Construction and dissolution are architectural events governed by the same CKS commitments that govern the substrate's contents. This sub-commitment formalizes the lifecycle property: the shared substrate is an event-scoped object, not a standing infrastructure.

**D1.02 — All six Paper 1 commitments holding within shared substrate scope.** Within the shared substrate's governance perimeter, all six Paper 1 architectural commitments apply without modification by inheritance. This sub-commitment formalizes the inheritance relationship precisely: the shared substrate is a Paper 1 substrate at inter-Self scope, and each of the six commitments holds within it on the same basis it holds in a Paper 1 cell-scope substrate.

**D1.03 — Governance perimeter spanning multiple Selves' home perimeters.** The shared substrate's governance perimeter is a new scope of operation that contains the home perimeters of participating Selves without replacing them. Joint human authority governs the inter-Self perimeter. Home perimeter governance continues to govern intra-Self operations. This sub-commitment formalizes the perimeter-spanning property as a structural addition to the participating Selves' architecture rather than a modification of their internal governance.

**D1.04 — Persistence policy as governed substrate content.** The persistence policy specifying what remains after FAI event dissolution is itself authored substrate content within the shared substrate, subject to all six Paper 1 commitments, and governed by joint human authority. This sub-commitment formalizes the self-referential governance property: the shared substrate governs what happens to itself at dissolution, and that governance is substrate content rather than an external operational decision.

**D1.05 — The named foil as the architectural alternative Claim 1 rejects.** Opaque agent-to-agent communication — exchange whose substantive content is not human-governable as authored substrate — is the architectural alternative Paper 3's Claim 1 explicitly positions against. This sub-commitment formalizes the foil as a named architectural category, establishing prior art that forecloses claims that the shared substrate pattern is compatible with or equivalent to opaque-exchange approaches.

---

## 7. Operational test

The following test determines whether a given inter-Self coordination system instantiates Claim 1. An observer who cannot inspect the system's design documentation should be able to answer all three questions affirmatively by examining the system's deployed architecture.

**Question 1: Is there an identifiable, distinct substrate object that serves as the medium of inter-Self coordination?** The observer should be able to identify a specific architectural object — separate from the participating Selves' home substrates, separate from any message-passing infrastructure, separate from any shared-memory store not organized as CKS substrate content — that carries the coordination content of the inter-Self interaction. If the coordination content is distributed across message streams, tool-call logs, or memory access patterns rather than organized in a single identified substrate object, Claim 1 is not instantiated.

**Question 2: Do all six Paper 1 architectural commitments hold within that substrate object's governance perimeter?** The observer should be able to verify, for each of the six Paper 1 commitments, that it holds within the shared substrate's scope: (a) the substrate is the authoritative coordination artifact; (b) human authority over inspection, modification, and override is intact; (c) conflicts are preserved as first-class substrate state; (d) AI systems are mediators, not owners, of substrate content; (e) tooling is substitutable without governance loss; (f) governance cost does not scale super-linearly with content volume. If any of the six commitments is not verifiable within the shared substrate's scope, Claim 1 is not fully instantiated.

**Question 3: Is the persistence policy — specifying what remains after the inter-Self interaction concludes — itself authored substrate content within the identified object, under joint human authority?** The observer should be able to locate, within the shared substrate, content that specifies what will persist when the substrate dissolves and under whose authority that specification was authored and can be modified. If the persistence policy is an external operational configuration, a hardcoded system parameter, or is simply absent (defaulting to full retention or full deletion without explicit governance), Claim 1's fourth defining property is not instantiated.

A system that passes all three questions instantiates Claim 1. A system that fails any question either does not implement the shared substrate pattern or implements a version that deviates from one or more of the pattern's defining properties. The deviation should be named and its architectural consequences evaluated against the full Claim 1 commitment set.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Shared Substrate as Paper 3's First Architectural Claim.* CKS Derivation Note D0.01 (#460). May 14, 2026. ORCID: 0009-0004-8065-3235.
