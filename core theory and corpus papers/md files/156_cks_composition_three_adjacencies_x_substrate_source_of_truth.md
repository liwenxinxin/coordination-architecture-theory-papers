# Composition Pair: Three Adjacencies × Substrate-as-Source-of-Truth — Adjacency-vs-Substrate Distinction as the Architectural Property Ensuring Substrate Authority and Adjacency Non-Authority

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the architectural property that emerges when two foundational CKS commitments — the three-adjacencies disambiguation (CKS is not RAG, not parametric memory, not external structured memory of the KO/OIDA family) and substrate-as-source-of-truth — compose, producing the *adjacency-vs-substrate distinction* as a single architectural property neither commitment yields independently.

## Abstract

The CKS source paper makes two foundational commitments that, taken individually, do not fully specify how a hybrid system allocates authoritative content. The three-adjacencies commitment (§1.2, §2.3) names three architectural positions distinct from substrate — RAG, parametric memory, and external structured memory of the KO/OIDA family — but does not in itself specify whether those adjacent positions can hold authoritative coordination state. The substrate-as-source-of-truth commitment (§11.3) names substrate as authoritative for five categories of state — what was decided, by whom, under what authority, with what rationale, and what contradictions remain unresolved — but does not in itself specify the relationship between substrate and the three adjacencies a hybrid deployment may include. The composition forces what neither commitment alone forces: the three adjacencies are *non-authoritative* for the five categories; they may exist as architectural positions in a hybrid system, but cannot be substrate substitutes. This note formalizes the composition as a standalone architectural property, articulates it as four operational components, identifies the decisions it forces, names the anti-patterns it excludes, and provides an operational test with three sharpening properties.

## 1. Why the composition pair is formalized as a standalone property

The three-adjacencies commitment states that CKS is architecturally distinct from RAG, parametric memory, and external structured memory of the KO/OIDA family (§§1.2, 2.3). §4.5 frames all three as legitimate composition partners in hybrid systems where a CKS substrate may sit alongside a RAG retrieval index, a fine-tuned mediator, or a KO-family structured store. The substrate-as-source-of-truth commitment, developed at §11.3, names substrate as the authoritative answer to coordination questions across five categories: decisions, writer attribution, rule-of-authority references, captured rationale, and unresolved-contradiction records.

Stated separately, neither commitment closes a question that arises in any actual hybrid deployment. The closure is the composition itself: substrate's source-of-truth scope is exclusive on the five categories, and the three adjacencies — being architectural positions distinct from substrate — are by composition non-authoritative for those categories.

The closure earns standalone formalization on three grounds. First, it is consequential for any "AI architecture" proposal that names an adjacent system as a substrate alternative: if the proposed alternative is one of the three adjacencies, the composition pins down that the proposal is not a CKS-conformant substitute, regardless of how the proposal is named. Second, it is the architectural property that distinguishes a CKS-fronting hybrid from a "RAG-with-governance-metadata" deployment, a parametric-memory-with-operator-overrides deployment, or a KO deployment with CKS-shaped decoration. Third, it is what makes adjacency-pattern mapping (the sibling first cluster note) architecturally meaningful: the patterns by which adjacencies are operationally engaged are coherent only because substrate holds the authoritative content. This note is the second in the three-adjacencies cluster of Phase A4: the first cluster note formalizes *how* adjacencies are engaged; this note formalizes the prior architectural distinction those patterns rest on — *which architectural position holds authority*. Subsequent cluster notes cover AI mediation across adjacencies and the adjacency composition requirements that close the cluster.

## 2. The emergent architectural property as four operational components

The composition produces *adjacency-vs-substrate distinction* as a single architectural property, operationally specified by four components.

**(i) Substrate is exclusively authoritative for the five categories.** Decisions, writer attribution, rule-of-authority references, captured rationale, and unresolved-contradiction records are answerable from substrate content alone. The substrate is the single architectural position designated as authoritative.

**(ii) The three adjacencies are explicitly non-authoritative architectural positions for the five categories.** A RAG retrieval index that supplies source documents for a coordination decision is non-authoritative for what the decision was, who made it, under what authority, why, and whether it conflicts with another. A parametric mediator is non-authoritative for the same five categories, whatever its retrieval fluency over them. An external structured memory of the KO or OIDA family is non-authoritative for the five categories *as CKS scopes them*, even where the structured memory carries typed knowledge with provenance fields, because the source-of-truth commitment binds authority to substrate content alone.

**(iii) The source-of-truth-vs-mirror distinction applies to the substrate–adjacency relationship.** Adjacencies in a hybrid CKS deployment are mirrors, derived views, or non-authoritative input sources, not sources of truth for the five categories. Substrate may be projected into a RAG index for retrieval-time use; the projection is a mirror. A KO-family store may receive substrate content extracted into typed structured form; the extraction produces a mirror. An LLM mediator may be fine-tuned over substrate content; the parametric weights are non-authoritative — when substrate and parametric content disagree, substrate wins by definition.

**(iv) The substrate-substitute anti-pattern is identifiable through the composition.** The composition gives a sharp test for the anti-pattern *adjacent component as substrate substitute*: any deployment in which one of the three adjacencies is treated as authoritative for any of the five categories instantiates it, regardless of the adjacency's local technical merit. The composition makes the anti-pattern detectable architecturally rather than only after a coordination question fails to be answerable.

## 3. What the composition forces beyond either commitment alone

The composition forces four architectural decisions that follow from neither parent commitment in isolation.

*Decision 1.* Each of the three adjacencies, where present in a deployment, must be specifically documented as non-authoritative for the five categories — a RAG index, a parametric mediator, and a KO- or OIDA-family external structured memory each documented as non-authoritative for decisions, writer attribution, authority references, rationale, and unresolved contradictions.

*Decision 2.* The substrate is documented as the *exclusive* authority for the five categories in any deployment that includes one or more of the three adjacencies. The source-of-truth commitment alone is consistent with substrate being one of multiple authoritative locations; the composition with the three-adjacencies commitment forecloses that reading by naming three architectural positions specifically excluded from authority.

*Decision 3.* The source-of-truth-vs-mirror distinction applies to each adjacency's relationship to substrate. The deployment names which adjacency mirrors which substrate content, in which direction (substrate-to-adjacency projection vs. adjacency-to-substrate extraction), and at what cadence.

*Decision 4.* Architectural review verifies that no adjacency in the deployment functions as a substrate substitute. The verification is not a one-time check; it is a structural property maintained through the deployment's lifetime, regardless of whether the substrate-substitute use of the adjacency would be locally convenient.

## 4. Anti-patterns specifically violating the composition

The *adjacent-component-as-substrate-substitute* anti-pattern is the canonical composition violation. Any deployment in which one of the three adjacencies — RAG index, parametric mediator, or KO/OIDA-family structured memory — holds authoritative content for any of the five categories instantiates it. The local merits of the adjacency are not in scope.

Three further anti-patterns are violations when the architectural position they describe functions as one of the three adjacencies and holds authoritative content. *External tool state authoritative for coordination questions* — the external tool is one of the three adjacencies and the system reads from it to answer the five categories. *Agent memory as source of truth* — an agent's per-session or external memory is structured as a KO-family typed store and is read as authoritative; the memory functions as one of the three adjacencies while also being treated as authoritative. *LLM context as source of truth* — the LLM's in-context state is treated as authoritative, and parametric content fills gaps the in-context state does not cover; the parametric mediator is being treated as authoritative through its weights.

Three further patterns are violations at the deployment-shape level. *"Adjacency-with-authoritative-content" generally* is the composition violation in its most general form. *"RAG-as-knowledge-base"* places a RAG retrieval index in the architectural slot the substrate is supposed to occupy, with retrieval policy and provenance attached to retrieved units; the arrangement is RAG-with-governance, not CKS, and treating it as CKS-conformant violates the composition. *Vendor adjacency authority claims* — a vendor frames a product in one of the three adjacency categories as a substitute for a CKS substrate; the framing violates the composition independent of the product's other properties.

## 5. Operational decisions

Five operational decisions instantiate the composition in a deployment. (a) *Each adjacency present is documented as non-authoritative for the five categories.* The documentation is architectural, not procedural; it appears in the deployment's source-of-truth specification, not in operational runbooks. (b) *The substrate is documented as the exclusive authority for the five categories;* "the substrate is authoritative" without naming the exclusion of adjacencies fails to instantiate the composition. (c) *Architectural review verifies non-authority of each adjacency at deployment time;* unverified non-authority is a deployment defect. (d) *The substrate-substitute architectural test is applied at design time and at every architectural change;* any proposal to add or alter an adjacency triggers the test, and a yes answer makes the proposal non-adoptable as designed. (e) *Substrate-to-adjacency and adjacency-to-substrate flows are named with their authority direction;* a projection from substrate to a RAG index is a substrate-authoritative flow producing a mirror, while an extraction from a KO-family store into substrate content under cell mediation is an adjacency-as-input flow producing authoritative substrate content.

## 6. What the composition is NOT

The composition is not the three-adjacencies commitment alone. That commitment names three adjacencies as architecturally distinct from substrate but does not specify the authority asymmetry. A deployment can satisfy the three-adjacencies commitment by naming the adjacencies as composition partners and still violate source-of-truth by treating one as authoritative.

The composition is not the source-of-truth commitment alone. That commitment names substrate as authoritative for the five categories but does not specify the relationship to the three adjacencies. A deployment can satisfy source-of-truth with an authoritative substrate and still mis-handle adjacency relationships by leaving adjacency authority status unspecified.

The composition is not a "primary substrate, secondary adjacency authority" pattern. A pattern in which substrate is the primary authority while one of the three adjacencies is a "secondary" authority — a fallback when substrate is unavailable, a faster-but-less-trusted source, a "mostly authoritative" parametric mediator — violates the composition. The composition is exclusionary on authority for the five categories; "secondary authority" instantiates the substrate-substitute anti-pattern.

The composition is not a vendor-product property. The exclusion of authority applies to architectural positions, not vendor identity. A KO/OIDA-family external structured memory is non-authoritative whether the product is an open-source library, an enterprise service, or a research artifact. The composition tracks the architectural slot, not the product name.

## 7. Why the composition is load-bearing

The composition continues the three-adjacencies cluster: the first cluster note specifies how adjacencies are engaged; this note specifies the authority asymmetry that makes those engagement patterns architecturally meaningful. Without it, the engagement patterns lose their architectural anchor — consultation of an adjacency makes architectural sense only because substrate is authoritative. The composition also supports two other Phase A4 properties: AI-mediated authority preservation is verifiable only because the adjacency-vs-substrate distinction prevents a parametric mediator from being a covert authority through its weights; and vendor-independent authoritative content holds because a substrate hosted alongside a vendor's KO-family store inherits the adjacency's non-authority for the five categories. The composition distinguishes CKS from substrate-substitute architectures at the architectural-pattern level rather than the product-feature level — what gives CKS its standing as a non-overlapping design pattern in a literature where adjacent design objects are sometimes proposed as functional substitutes.

## 8. Operational test

A deployment instantiates the composition pair if and only if the following three sharpening properties hold throughout the substrate's existence.

*(e.1) Substrate-exclusive-authority test.* For each of the five categories — decisions, writer attribution, rule-of-authority references, captured rationale, unresolved-contradiction records — the deployment's source-of-truth specification names substrate as the exclusive authoritative location, with no adjacency named as alternative or fallback authority.

*(e.2) Adjacency-non-authority test.* For each architectural position in the deployment functioning as one of the three adjacencies — RAG index, parametric mediator, KO/OIDA-family external structured memory — the deployment's documentation explicitly names the position as non-authoritative for each of the five categories. Unstated authority status fails the test; the composition requires positive non-authority documentation, not silence.

*(e.3) Substrate-substitute-pattern-excluded test.* No architectural position in the deployment functions as a substrate substitute. The test walks each adjacency and asks: does the system read from this position to answer any of the five questions? A yes for any adjacency fails the test and instantiates the substrate-substitute anti-pattern.

A deployment that fails any of (e.1)–(e.3) may instantiate the three-adjacencies commitment, may instantiate the source-of-truth commitment, but does not instantiate the composition.

## 9. One-sentence test

A deployment instantiates the three-adjacencies × source-of-truth composition if and only if substrate is the exclusive architectural location read for the five coordination categories, the three adjacencies — RAG, parametric memory, external structured memory of the KO/OIDA family — are each documented as non-authoritative for those categories, and no adjacency in the deployment functions as a substrate substitute.

## 10. Why naming the composition as a standalone matters

Naming three-adjacencies × source-of-truth as a standalone composition pair earns its keep because it forecloses a class of mis-deployments that satisfies each parent commitment in isolation but violates the joint property. A deployment satisfying the three-adjacencies commitment but silent on adjacency authority can host an authority-leaking adjacency without overtly contradicting the commitment. A deployment satisfying source-of-truth but silent on adjacency relationships can declare substrate authoritative while operating an adjacency as a parallel authoritative source. The composition is what catches both.

The continuing-cluster framing makes the gain cumulative. The first cluster note names the adjacency engagement patterns; this note names the authority asymmetry those patterns rest on; the third will name the AI-mediation property that crosses adjacencies under the asymmetry; the fourth will name the composition requirements that close the cluster. Subsequent work that adopts or extends the CKS pattern in deployments with adjacency partners should treat three-adjacencies × source-of-truth as the joint property it is, and should name where the substrate-exclusive authority sits in the deployment, alongside where each adjacency's documented non-authority sits.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235. Source sections: §1.2 (three adjacencies), §2.3 (adjacency disambiguation), §3.3 (architectural and temporal qualifiers), §4.5 (hybrid system composition with adjacent components), §11.3 (substrate as source of truth).

## Related notes in this series

Li, W. (2026). *Three Adjacencies: Why CKS Is Not RAG, Not Parametric Memory, and Not External Structured Memory.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Substrate Is the Source of Truth: Where State Lives in CKS Systems and Where It Cannot.* 26 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Composition Pair: Three Adjacencies × Substrate-as-Source-of-Truth — Adjacency-vs-Substrate Distinction as the Architectural Property Ensuring Substrate Authority and Adjacency Non-Authority.* May 6, 2026. ORCID: 0009-0004-8065-3235.
