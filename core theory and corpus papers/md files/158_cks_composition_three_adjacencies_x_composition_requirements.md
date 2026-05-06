# Adjacency Composition Requirements: How CKS's Five Composition Requirements Apply Uniformly to Each of Its Three Adjacencies

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a standalone composition pair, the emergent architectural property that arises when the three-adjacencies commitment (A1.14) and the composition-requirements commitment (A1.13) are taken together: the property under which CKS's five composition requirements apply uniformly to each of CKS's three adjacencies in hybrid systems.

## Abstract

Two of the CKS pattern's six architectural commitments are themselves about composition. A1.14 names the three architectural neighbors with which CKS is most often confused or composed — retrieval-augmented generation (RAG), parametric memory, and external structured memory of the Knowledge Objects / OIDA family. A1.13 names what any composition involving CKS substrates must preserve — five requirements covering governance preservation, retraceability preservation, determinism preservation, AI-as-substrate-mediator at every layer, and human-selective composition. Each commitment has its own decomposition cluster; their composition has not been stated as an architectural property in its own right. This note states it. The composition produces an emergent architectural property — *adjacency composition requirements* — under which all five A1.13 requirements apply uniformly to each of the three A1.14 adjacencies, producing a complete specification of how each adjacency must behave under composition. The note states the composition's four operational components, the architectural decisions it forces, the anti-patterns that specifically violate the uniform-application principle, what the composition is not, and an operational test with three sharpening properties. With this composition formalized, the A1.14 cluster (A4.19 pattern relationships, A4.20 authority status, A4.21 AI mediation, A4.22 composition requirement preservation) fully specifies the architectural behavior of the three adjacencies.

## 1. Why this composition needs to be formalized as standalone

A1.14 and A1.13 occupy adjacent territory in the CKS pattern. A1.14 names the architectural neighbors — three design objects with which CKS is most often conflated and most often composed in hybrid systems. A1.13 names the requirements — five constraints any multi-substrate composition must satisfy to remain CKS-coherent. Each commitment has its own decomposition (A2.81–A2.85 for A1.14; A2.75–A2.80 for A1.13), and each commitment's composition cluster operationalizes its own internal structure: A4.19, A4.20, A4.21 for the A1.14 cluster; A4.14 through A4.18 for the A1.13 cluster's five Requirements taken one at a time.

What none of those notes does is specify what holds at the intersection. A1.14-alone specifies architectural positions adjacent to the substrate but does not say what the adjacencies must satisfy when CKS composes with them. A1.13-alone specifies requirements over multi-substrate composition but does not say how those requirements apply when the composition crosses one of A1.14's three named adjacencies — when a substrate fronts a RAG retrieval index, sits alongside a fine-tuned mediator that carries parametric memory of the domain, or is composed with an OIDA-style structured memory store. The intersection is where the operational content of hybrid CKS systems lives, and the intersection has not been named.

The composition specifies that intersection. Three adjacencies, five requirements, fifteen cells of architectural specification — each cell answers a single question: under what mechanism does this requirement hold at this adjacency boundary? The composition is also meta-architectural in a sense neither parent commitment is. Both A1.14 and A1.13 are themselves about composition: A1.14 names the architectural neighbors that CKS composes with; A1.13 names what composition must preserve. Their composition specifies how composition operates *across the named adjacencies* — and in so doing closes the A1.14 cluster. With A4.19, A4.20, A4.21, and A4.22 in place, the three adjacencies have a complete Phase A4 treatment: pattern relationships, authority status, AI mediation at boundaries, and requirements under composition.

## 2. The emergent property: adjacency composition requirements as four operational components

The composition produces a single emergent architectural property — *adjacency composition requirements* — whose operational content has four components.

**Component 1 — Each adjacency satisfies all five A1.13 requirements.** When CKS is composed with a RAG retrieval index, the composition preserves governance over substrate content, retraceability across the substrate-index boundary, determinism on the substrate side, the AI-as-substrate-mediator role at every layer of the composition, and human-selective composition over what the RAG layer is permitted to inform. When CKS is composed with parametric memory in the form of a fine-tuned mediator, the same five requirements hold at the substrate-parametric boundary. When CKS is composed with external structured memory of the KO/OIDA family, the same five hold at the substrate-structured-memory boundary. No adjacency is exempt; no requirement is reduced.

**Component 2 — Requirement preservation operates through adjacency-specific mechanisms.** Uniform application of the requirements does not entail undifferentiated mechanism. The mechanism by which retraceability is preserved at the substrate-RAG boundary differs from the mechanism by which it is preserved at the substrate-parametric boundary; the former carries the path through the index reference and the retrieval policy, while the latter carries the path through the mediator-role attribution and the orchestration rule that authorized the parametric mediator's involvement. What is uniform across the three adjacencies is the requirement; what is adjacency-specific is the mechanism.

**Component 3 — Cross-adjacency operations preserve all requirements at boundaries.** Hybrid systems are not always single-adjacency. A deployment may compose CKS with RAG and a fine-tuned mediator simultaneously, or with a KO/OIDA-style structured memory and a RAG layer over its source documents. At every cross-adjacency boundary — every point where state, control, or decisions cross from one adjacency-bearing layer to another — the five requirements continue to hold. Cross-adjacency operations are not granted requirement exemptions because of their cross-adjacency status; they inherit all five requirements at every such boundary, with mechanisms specified per boundary.

**Component 4 — A2.95 composition anti-patterns are excluded by adjacency requirement satisfaction.** The composition is also a negative specification: the A2.95 anti-pattern catalog enumerates failure modes of multi-substrate composition (governance erasure, conflict masking, retraceability loss across boundaries, mediator-role bypass, ungoverned composition selection), and satisfaction of each requirement-adjacency cell excludes the corresponding anti-pattern at that adjacency. A hybrid system whose three-by-five matrix is fully populated with mechanism specifications is, by construction, a system in which the A2.95 anti-patterns cannot occur at any of its named adjacencies.

The four components together are the operational content of *adjacency composition requirements*. A1.14 gives the rows of the matrix; A1.13 gives the columns; the composition gives the cells.

## 3. What the composition forces beyond either commitment alone

The composition forces four architectural decisions that neither A1.14 nor A1.13 alone forces.

**Uniform application of all five requirements to all three adjacencies.** The composition rules out per-adjacency requirement subsets. A hybrid system cannot satisfy "governance and retraceability" at the RAG boundary while satisfying only "governance" at the parametric boundary; the application is uniform.

**Cross-adjacency requirement preservation as architectural commitment.** The composition forces hybrid systems involving multiple adjacencies to preserve requirements at the cross-adjacency boundaries where adjacencies meet, not only at single-adjacency boundaries in isolation. This rules out designs in which "each adjacency is fine on its own" but the composition itself loses requirements at the seams.

**Architectural review covers the requirement-adjacency intersection.** A review that confirms each of the three adjacencies in isolation, or each of the five requirements in isolation, is incomplete; the review must cover the fifteen cells of the matrix and the cross-adjacency boundaries that arise when more than one adjacency is involved. The review is matrix-level, not row-level or column-level.

**A2.95 anti-pattern exclusion through positive specification.** Deployments must specify mechanism per cell as the means by which anti-patterns are excluded, rather than relying on default behavior or vendor properties to keep anti-patterns out. The exclusion is architectural commitment, not architectural luck.

These four decisions follow from the composition; none follows from A1.14 or A1.13 alone.

## 4. Anti-patterns specifically violating the composition

Five anti-patterns specifically violate the composition. Each can be stated as a violation of a particular component, and each corresponds to a recognizable failure mode in deployed hybrid systems.

**Adjacency-with-incomplete-requirements.** A composition in which one of the three adjacencies satisfies some but not all five A1.13 requirements. A CKS-fronting-RAG deployment that preserves governance and retraceability across the substrate-index boundary but does not preserve human-selective composition over which retrieved content informs which substrate operation satisfies four of five requirements at the RAG adjacency. The architecture is not partly CKS-coherent at that adjacency; it is not CKS-coherent at that adjacency, because component 1's uniform-application principle is violated. This is the canonical violation of the composition.

**Cross-adjacency-requirement-loss.** A composition in which all five requirements hold at each single-adjacency boundary in isolation, but at least one requirement breaks at a boundary between two adjacencies. A deployment that composes CKS with both RAG and a fine-tuned mediator may preserve retraceability at the substrate-RAG boundary and at the substrate-parametric boundary, while losing it at the boundary where the parametric mediator interprets RAG-retrieved content before it reaches the substrate. The single-adjacency cells are populated; the cross-adjacency requirement is lost; component 3 is violated.

**Different-requirements-per-adjacency.** A design that treats each adjacency as having distinct architectural requirements — "RAG only needs governance and retraceability; parametric memory only needs determinism and mediator-role; external structured memory only needs governance and human-selective composition" — rather than uniform application of A1.13's five. A1.13's requirements are not adjacency-relative; they apply per-substrate at every composition boundary, and the composition with A1.14 inherits the per-substrate uniformity rather than relaxing it.

**Vendor-specific adjacency requirements.** A design in which requirement satisfaction at an adjacency depends on a particular vendor's behavior — a particular RAG vendor's logging, a particular fine-tuning provider's lineage tracking, a particular structured-memory product's contradiction-edge semantics — rather than on architectural commitment carried by the composition. Vendor-determined behavior is not architectural commitment, and a hybrid system whose adjacency requirements rest on vendor behavior is not adjacency-composition-requirement-coherent regardless of how reliable the vendor is in practice.

**Adjacency-without-mediator.** A design in which AI-as-substrate-mediator holds at the substrate but does not hold at one or more adjacency boundaries. A fine-tuned LLM that operates as terminal producer over CKS-retrieved content (rather than under the five mediator properties) bypasses the mediator role at the parametric adjacency. A RAG layer permitted to write into the substrate directly bypasses it at the RAG adjacency. The bypass violates component 1 and produces the failure mode A2.95 names as ungoverned-writer-through-adjacency.

## 5. What the composition is NOT

Five clarifications close the property's boundary.

**Not A1.14-alone.** A1.14 names the three adjacencies as architectural positions. The composition adds the requirements that each adjacency must satisfy under composition with CKS. A specification that names the adjacencies but leaves their requirements unspecified is not a specification of adjacency composition requirements.

**Not A1.13-alone.** A1.13 names five requirements over multi-substrate composition. The composition specializes those requirements to A1.14's three named adjacencies. A specification of the five requirements that treats all composition boundaries as undifferentiated does not address the adjacency-specific mechanism content the composition forces.

**Not a default applied implicitly.** The composition forces the matrix to be populated by deployment-specific mechanism specifications; in their absence, the deployment does not inherit a default that would satisfy the property.

**Not vendor-determined.** Requirement satisfaction is architectural commitment carried by the composition, not a property of the vendor whose adjacency-bearing component is involved. The property holds independently of which RAG vendor, fine-tuning service, or structured-memory product realizes the adjacency.

**Not exhaustive coverage of adjacency interactions.** The property specifies *requirements* at adjacencies. The hybrid-systems composition commitment (A1.16) specifies *patterns* through which adjacencies are composed with CKS — Pattern A (adjacency provides input to substrate), Pattern B (adjacency provides derived view of substrate), Pattern C (adjacency operates as separate concern alongside substrate). A1.14 × A1.13 gives the requirement matrix; A1.16 gives the composition patterns; the two are complementary.

## 6. Operational test

A hybrid CKS system instantiates the *adjacency composition requirements* property if and only if, at all times during the system's existence, for each cell of the three-by-five matrix — each pairing of one of CKS's three adjacencies (RAG, parametric memory, external structured memory) with one of A1.13's five composition requirements (governance preservation, retraceability preservation, determinism preservation, AI-as-mediator at every layer, human-selective composition) — the architecture's design specifies the mechanism by which that requirement holds at that adjacency, with no cell unspecified, no requirement weakened, and no adjacency exempt.

Three sharpening properties refine the test.

**(e.1) Adjacency-requirement matrix.** For each of the fifteen matrix cells, the deployment carries a specification stating how the requirement holds at the adjacency. The specification is part of the architecture, addressable and reviewable, not an implicit assumption about default vendor behavior. A cell that is "covered by vendor defaults" without an explicit mechanism specification fails (e.1).

**(e.2) Cross-adjacency requirement preservation.** When the deployment involves more than one adjacency simultaneously, the requirements continue to hold at the cross-adjacency boundaries where adjacencies meet. The single-adjacency cells being populated does not by itself satisfy the cross-adjacency condition; cross-adjacency boundaries carry their own mechanism specifications.

**(e.3) Composition-cluster closure.** The architectural treatment of the three adjacencies in the deployment is consistent with the four-note A1.14 cluster taken together: pattern relationships (A4.19), authority status (A4.20), AI mediation (A4.21), and adjacency composition requirements (A4.22). A deployment that specifies three of the four but not the fourth is not adjacency-cluster-coherent and does not satisfy the test.

A one-sentence form: a hybrid CKS system satisfies the *adjacency composition requirements* commitment if and only if for each of CKS's three adjacencies and each of CKS's five composition requirements, the architecture specifies the mechanism by which the requirement holds at that adjacency, with no adjacency exempt, no requirement weakened, and cross-adjacency boundaries carrying their own mechanism specifications. A hybrid system that fails any of (e.1)–(e.3) may be a useful system and may instantiate other valid design patterns; it is not adjacency-composition-requirement-coherent.

## 7. Why this composition is load-bearing — and where it sits in Phase A4

The composition is load-bearing on three grounds. *First*, it closes the A1.14 composition cluster: the four notes A4.19, A4.20, A4.21, and A4.22 together specify the architectural behavior of the three adjacencies under composition — pattern relationships, authority status, AI mediation at boundaries, and requirements under composition — and after A4.22 the three adjacencies have a complete Phase A4 treatment. *Second*, it overlaps the A1.13 cluster at the adjacency intersection: the five A1.13 cluster notes (A4.14 through A4.18) operationalize each requirement at the substrate boundary; A4.22 brings those operationalizations together at the three adjacency boundaries A1.14 names, and the two clusters meet at A4.22's matrix in a way neither cluster, taken alone, would specify. *Third*, it distinguishes hybrid CKS systems from systems with partial adjacency requirements — systems whose adjacencies satisfy only some of the five requirements, or whose requirements vary by adjacency, or whose cross-adjacency boundaries lose requirements — allowing hybrid systems to be evaluated on architectural grounds rather than on case-by-case judgment.

The progression beyond A4.22 follows the master plan's structural logic. With the A1.14 cluster closed, Phase A4 moves to its fourth tier — the A1.15 orchestration-layer-distinctions cluster (A4.23–A4.26), formalizing compositions involving the three layer distinctions (CKS vs. workflow engine, CKS vs. agent framework, CKS vs. control plane). The fifth and final tier covers the A1.16 hybrid-systems Pattern A / Pattern B / Pattern C operationalizations (A4.27–A4.30), which close Phase A4 by specifying the composition patterns whose requirements A4.22 has now specified at the adjacency level.

The composition formalized here is a single emergent property arising from two existing commitments. Its standalone publication adds no new commitments and no new requirements to the decomposition clusters that flank it. Its contribution is the matrix — three adjacencies by five requirements, fifteen cells of architectural specification — and the closing of the A1.14 cluster around the matrix.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Related notes in this series

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* April 24, 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Three Adjacencies: Why CKS Is Not RAG, Not Parametric Memory, and Not External Structured Memory.* April 24, 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Composition Without Erasure: What Multi-Substrate CKS Systems Must Preserve to Remain Traceable.* April 24, 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Mediator, Not Authority: The Architectural Role of LLMs in the Coordination Knowledge Substrate Pattern.* April 24, 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Hybrid Systems: How CKS Substrates Compose with Adjacent AI Components.* April 24, 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Adjacency Composition Requirements: How CKS's Five Composition Requirements Apply Uniformly to Each of Its Three Adjacencies.* May 6, 2026. ORCID: 0009-0004-8065-3235.
