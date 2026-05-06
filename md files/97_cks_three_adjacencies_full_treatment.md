# The Three Adjacencies as an Integrating Frame: Operational Treatment of the Architectural Boundaries Between the Coordination Knowledge Substrate Pattern and Retrieval-Augmented Generation, Parametric Memory, and External Structured Memory

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the integrating frame of the three adjacencies — the structure that organizes how CKS distinguishes itself from retrieval-augmented generation (RAG), parametric memory, and external structured memory of the KO/OIDA family — at the operational depth required for the standalone treatments of each adjacency, and of the hybrid-composition coherence the boundaries enable, to specialize from a single integrating frame.

## Abstract

The Coordination Knowledge Substrate (CKS) design pattern is most often conflated with three adjacent design objects: retrieval-augmented generation (RAG), parametric (in-weight) memory, and external structured memory of the Knowledge Objects (KO) and OIDA family. The parent foundational note A1.14 names the three adjacencies and identifies the load-bearing differentiating commitment for each. This note formalizes the integrating frame that organizes the three: it identifies the single underlying axis on which the adjacencies cluster (the architectural location of memory or knowledge state relative to the LLM), specifies the relationship between A1.14's adjacency treatment and A1.09's inheritance treatment, names the connection to A1.13's composition requirements and A1.16's hybrid composition patterns, and provides an integrating-frame operational test that composites the standalone tests deferred to A2.82 (RAG), A2.83 (parametric memory), A2.84 (KO/OIDA-family external structured memory), and A2.85 (hybrid composition coherence). Those subsequent notes specialize this integrating frame.

## 1. Why the integrating frame needs to be formalized as standalone

The parent foundational note A1.14 commits to the three adjacencies, names each adjacent object, identifies the load-bearing distinguishing commitment for each, and gives a one-sentence test for distinguishing CKS from each adjacent object in a specific instance. The foundational treatment is correct as far as it goes. What it leaves underspecified is the *integrating frame* — the structure that organizes the three adjacencies, locates them within the broader composition framework of A1.13 and A1.16, and makes A2.82–A2.85 readable as specializations of a single architectural commitment rather than three loosely related disambiguations.

The motivating cases are deployments and analyses where CKS is conflated with one or more of the adjacent objects. A deployment that presents CKS as "RAG with governance metadata" misses the coordination-and-decision-layer move (§2.1) that distinguishes CKS from asset-layer work in data governance and enterprise knowledge bases — governance attached to retrieval is not the same as governance located in a coordination artifact. An analysis that treats CKS as a parametric pattern imports cost-curve assumptions the architecture does not have — parametric expansion is superlinear (§6.2), while CKS expansion is linear-in-additions per A1.06 (§6.1). An evaluation that treats CKS as KO with extra fields misses that the extra fields do disambiguation work CKS requires to be explicit (§6.2). Each pattern requires the adjacency boundaries to be operationally specified at a depth the foundational treatment alone does not deliver.

Two further motivations follow. *Strategic prior-art posture.* The three adjacencies are consequential prior art because they specify the architectural boundaries CKS commits to. Patentable derivations that focus on AI-coordination architectures with governance, hybrid AI architectures with retrieval and substrate layers, or external-substrate AI systems with human authority are substantially more defensibly contested when the three adjacencies are publicly formalized as standalone with the integrating frame named explicitly. *Connection to the composition framework.* A1.13 specifies what any multi-substrate composition must preserve; A1.16 specifies the three patterns by which CKS composes with non-CKS components (input, derived view, separate concern); A1.14 names the boundaries at which those compositions occur. The three commitments compose: A1.14 names the boundaries; A1.13 specifies what compositions across them must preserve; A1.16 specifies the patterns by which they occur. The integrating frame is what makes that composition operationally meaningful at concrete adjacency boundaries.

Two scope notes apply throughout. First, "outside the model" carries the source paper's §1.2 sense — the architectural location of coordination, governance, and decision state in a persistent, human-governed substrate, not the narrower parametric-vs-non-parametric distinction standard in retrieval-augmented generation and external-memory work. This wider sense is what makes CKS distinct from the three adjacencies that take "outside the model" in the narrower sense. Second, the source paper enumerates five disambiguations at §1.2; three of them (RAG, parametric memory, multi-agent protocol / external structured memory) cluster as memory-location adjacencies and are the subject of A1.14 and this treatment. The remaining two (governance platform, complete system architecture) address a different architectural concern and are treated in other Series A notes. Per-session in-context memory is not a top-level adjacency: it is the failure mode external-memory patterns (CKS included) address, treated at §6.2.

## 2. Adjacency 1 — CKS is not RAG (named at the integrating level)

Retrieval-augmented generation is an architectural pattern in which an LLM, at inference time, queries an external index over a corpus of source documents and uses retrieved content as additional context for generation. The primary design goal is retrieval quality — getting the right source content into the LLM's context window — and the design object is a corpus-plus-index pair.

The CKS-distinguishing commitment, named at the integrating level: the substrate is a coordination artifact humans read from, write into, and hold authority over (§§1.2, 2.3, 3.1). Its primary function is to encode decisions, rationale, authority, and preserved contradictions, not to retrieve source material. It is not an index over a corpus; the design object is the substrate itself, not a corpus-plus-index pair. A2.82 formalizes this adjacency standalone, including the conflation pattern ("RAG with governance metadata"), the failure modes that violate the boundary, and the one-sentence test for distinguishing CKS from RAG in a specific instance.

## 3. Adjacency 2 — CKS is not parametric memory (named at the integrating level)

Parametric memory locates content in the model weights themselves — knowledge stored within the LLM's parameters, recovered through forward passes over weight-encoded content. Continual learning, fine-tuning, and knowledge editing all operate on parametric memory.

The CKS-distinguishing commitment, named at the integrating level: the substrate is external to the LLM and deterministic, and its state changes through human-governed writes rather than through training (§2.3). Substrate content is added by human authorship, by LLM drafting under human authority, or by automated cells operating under human-authored orchestration rules — never by gradient updates to the model. The cost model is database-like: storage grows linearly per A1.06 (§6.1), inheriting the empirical cost curve from external-substrate work most directly demonstrated by KO (§6.2). The substrate is not the model; the model does not change as the substrate grows. A2.83 formalizes this adjacency standalone, including the cost-curve consequences of the misreading and the one-sentence test for distinguishing CKS from parametric memory in a specific instance.

## 4. Adjacency 3 — CKS is not external structured memory of the KO/OIDA family (named at the integrating level)

External structured memory is a family of architectures — represented in the 2026 literature by KO and OIDA — in which knowledge is stored as typed structured units in an external store the LLM reads as a substrate client. The shared commitment across the family is that coordination-grade knowledge is a schema-level object with typed structure and maintained state, not a retrieval target recovered from a corpus at inference time.

CKS sits in the same architectural family as KO and OIDA — typed external substrate, separation of concerns between storage and processing, addressable units with provenance — and inherits the database-like cost model per A1.09 (§6.2). Four architectural commitments distinguish CKS from the rest of the family. *First*, human governance of the substrate as a design requirement per A1.01 (§3.1): CKS commits to human authority over substrate content as a property of the architecture, whereas KO and OIDA commit to maintenance architectures (KO's hash addressing, OIDA's Knowledge Gravity Engine) that operate deterministically without locating authority. *Second*, formal role and authority schema at the cell level: CKS encodes who may decide what, on what evidence, under which policy, as substrate content; KO commits to a single `provenance_metadata` field, and OIDA's Knowledge Objects carry epistemic class but not institutional role-authority provenance (§5.2). *Third*, the AI's architectural role per A1.04: CKS frames AI as substrate mediator (§5.2, §8.2), whereas KO and OIDA frame AI as substrate client. *Fourth*, where disambiguation work lives: KO disambiguates computationally at retrieval time, while CKS disambiguates through human-authored schema at cell level, encoding distinctions into substrate structure at authoring time rather than recovering them by runtime algorithm (§6.2). A2.84 formalizes this adjacency standalone.

A1.14's adjacency treatment and A1.09's inheritance treatment are complementary: A1.09 names what CKS shares with the family and grounds the cost-model inheritance per A1.06; A1.14 names what differs and grounds the four-commitment differentiation above. A2.53 operationalizes the KO/OIDA case specifically, treating the architectural-difference-vs-feature-addition claim — CKS is architecturally different from OIDA on the multi-human axis, not OIDA plus multi-human — that distinguishes adjacency from feature increment.

## 5. Hybrid composition coherence (named at the integrating level)

CKS composes with each of the three adjacent objects in coherent hybrid systems, and the boundaries the integrating frame formalizes are what makes the composition possible without confusion. A CKS substrate may front a RAG retrieval index when source-document grounding is needed — the substrate carries decisions and rationale; the RAG layer supplies the source material those decisions rest on. A CKS cell may use an LLM mediator fine-tuned on domain content — the mediator's parametric memory improves its fluency, while the substrate remains the authoritative artifact for what has been decided. A CKS substrate may compose with an external structured memory store of the KO or OIDA family — the structured memory holds typed facts and contradictions at scale, while the CKS layer adds the human governance, role/authority schema, and substrate-mediator semantics the structured memory does not commit to.

Each composition is coherent only when the layers are named explicitly. Without the boundaries the integrating frame formalizes, hybrid systems become incoherent in characteristic ways: RAG-fronting hybrids get governance read as retrieval policy rather than as authority over a coordination artifact; fine-tuned-mediator hybrids carry parametric expansion as a hidden term while appearing to commit to linear-cost scaling; KO-composed hybrids reduce the CKS layer to decoration when the role/authority schema and the AI-as-substrate-mediator commitment disappear without anyone noticing. A2.85 formalizes hybrid-composition coherence standalone, instantiating A1.16's three patterns at each adjacency boundary, applying A1.13's composition requirements, and naming the failure modes that follow from boundary collapse.

## 6. What the three adjacencies do NOT claim

The integrating-frame treatment is not maximalist. Six precisions keep it from drifting into something stronger than the source paper supports.

**They do not claim that the adjacent objects are inferior to CKS.** Each adjacent object is a different design object serving a different design goal. The value of naming the boundaries is that it lets all three coexist with CKS in the same system without ambiguity about which layer is doing what.

**They do not claim that CKS replaces the adjacent objects.** CKS composes with each adjacent object in coherent hybrid systems per §5 and A2.85; it does not subsume or supersede them.

**They do not foreclose other adjacencies.** The three named in A1.14 are the most common conflations addressed in the source paper; future work may identify additional adjacencies that warrant their own boundary-naming. The integrating frame addresses the three foundational adjacencies established in A1.14.

**They do not specify implementation patterns for boundary preservation.** Implementations may use various mechanisms (explicit layer naming, architectural documentation, cross-layer interfaces); the architectural commitment is to the boundaries being operationally meaningful, not to any specific implementation.

**They do not require all CKS deployments to compose with adjacent objects.** A deployment may operate purely as CKS without adjacent layers; the architectural commitment is that when adjacent objects are involved, the boundaries are preserved.

**They do not foreclose architectural drift toward the adjacent objects.** Implementations under pressure may drift toward treating CKS as one of the adjacent objects; the boundary-naming makes the drift recognizable as architectural deviation rather than natural evolution.

## 7. Operational test at the integrating-frame level

A system instantiates the three-adjacencies boundary structure at the integrating-frame level if and only if all of the following are true at all times during the substrate's existence.

1. CKS is operationally distinguishable from RAG per A2.82 — the substrate is a coordination artifact humans hold authority over, not a retrieval index over a corpus.

2. CKS is operationally distinguishable from parametric memory per A2.83 — the substrate is external to the LLM, with state changing through human-governed writes rather than through training, and with linear-cost scaling per A1.06.

3. CKS is operationally distinguishable from external structured memory of the KO/OIDA family per A2.84 — the substrate has human governance as a design requirement per A1.01, formal role and authority schema at the cell level, AI as substrate mediator (not client) per A1.04, and human-authored disambiguation at cell level.

4. Hybrid compositions with adjacent objects are coherent per A2.85 — layers are named explicitly, with the CKS layer preserving its architectural commitments while each adjacent layer serves its design goal, under A1.13's composition requirements and A1.16's composition patterns.

5. The adjacency boundaries operate at the architectural-pattern level, not at the deployment-feature level; specific deployments may have varied operational features while the architectural boundaries hold.

A system that fails any of (1)–(5) does not instantiate the three-adjacencies boundary structure at the integrating-frame level. The individual operational tests for each adjacency and for hybrid composition are specified in A2.82, A2.83, A2.84, and A2.85; the test above composites them.

## 8. Why naming the integrating frame as standalone matters

Implementations under commercial-positioning pressure consistently drift toward presentations that conflate CKS with one of the three adjacencies. The drift is steady because the adjacencies are operationally familiar — RAG is the dominant LLM-system pattern in 2024–2026; parametric memory is the foundational LLM concern; external structured memory is well-understood through KO/OIDA work — and CKS's distinguishing commitments operate at the architectural-pattern level rather than at the operational-feature level where audiences typically engage.

Such drift produces systems where CKS is architecturally indistinguishable from the adjacent objects, with four downstream consequences: commercial-positioning failures (the architectural distinction is lost, and CKS appears as incremental enhancement of an adjacent object), prior-art failures (the architectural commitments cannot be defensively contested when CKS is conflated with adjacent prior art), hybrid-composition failures (compositions with adjacent objects become incoherent), and architectural-commitment failures (the foundational commitments of A1.01, A1.04, and A1.06 are obscured).

Naming the integrating frame as a standalone architectural commitment gives downstream readers a precise specification of what CKS is not, organized around a single underlying axis, and locates the adjacency treatment within the broader composition framework. A2.82, A2.83, A2.84, and A2.85 specialize each adjacency and the hybrid-composition coherence; together with this frame, they give the full operational decomposition of A1.14.

Subsequent work that adopts, extends, composes, or argues against the CKS pattern at the boundaries with adjacent objects should use the integrating frame in the sense formalized here; work that uses it differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Related notes in this series

Li, W. (2026). *Three Adjacencies: Why CKS Is Not RAG, Not Parametric Memory, and Not External Structured Memory.* 24 April 2026. ORCID: 0009-0004-8065-3235. [parent foundational note A1.14]

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235. [A1.01]

## How to cite this note

Li, W. (2026). *The Three Adjacencies as an Integrating Frame: Operational Treatment of the Architectural Boundaries Between the Coordination Knowledge Substrate Pattern and Retrieval-Augmented Generation, Parametric Memory, and External Structured Memory.* May 5, 2026. ORCID: 0009-0004-8065-3235.
