# Coherence of the Three Patterns: How Pattern A, Pattern B, and Pattern C Together Specify Legitimate Hybrid Composition in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize a single architectural property — **the coherence of the three legitimate composition patterns** — by showing that Pattern A, Pattern B, and Pattern C together provide a complete architectural specification of legitimate hybrid composition in CKS, in the precise sense that they are exhaustive of legitimate composition flows, mutually distinguishable through their architectural behavior, and coherent in jointly excluding the composition anti-patterns the source paper rules out.

## Abstract

A separate note in this series formalizes hybrid composition as supporting exactly three legitimate patterns by which an adjacent AI component can sit relative to a CKS substrate: as input to a cell (Pattern A), as a derived view of substrate content (Pattern B), or as a separate concern (Pattern C). Subsequent notes formalize each Pattern as a standalone architectural commitment with its own operational test. The present note formalizes the meta-architectural property those three Pattern operationalizations together imply but do not individually state: that the three patterns *jointly* constitute a complete architectural specification of legitimate hybrid composition. The completeness has three components — *exhaustiveness* (every legitimate composition flow between substrate and adjacent component is one of consultation, derivation, or no-flow), *mutual distinguishability* (each pattern carries a distinct architectural specification, so that for any given adjacent component the position it occupies is unambiguous), and *coherence in exclusion* (the three together rule out the composition anti-patterns the architecture preempts). The note states what three-patterns coherence requires, how it is operationally verifiable, and which failure modes violate the meta-property specifically. It closes Phase A4 of the composition-pair derivation series.

## 1. Why three-patterns coherence needs to be formalized as standalone

Hybrid composition in CKS is named at three levels of granularity in this derivation series. A foundational note formalizes that an adjacent AI component can occupy exactly one of three legitimate positions relative to the substrate. Sibling notes specialize that commitment into the integrating frame, the three patterns named individually as Pattern A (cell-to-adjacent consultation), Pattern B (substrate-derived view), and Pattern C (separate concern), and the composition anti-patterns the legitimate patterns exclude. A further set of sibling notes operationalizes each Pattern with its own architectural test.

Across those three layers, one architectural property remains unstated. The three Pattern operationalizations each say what their Pattern specifies; none says what the *three together* specify. The completeness of the composition space is implicit in the foundational commitment but not formalized as an independent architectural property. Without that formalization, downstream work has no precise vocabulary for the question that arises in deployment review: *given a hybrid system using all three patterns, what does it mean to verify that the composition is legitimate?* The intuitive answer — verify each adjacent component fits one of the three patterns — depends on the three patterns being exhaustive (so that every legitimate component fits one) and mutually distinguishable (so that fit is unambiguous). Each is an architectural property of the pattern set, not of any individual pattern. Naming them is what makes the verification procedure principled rather than ad hoc.

The standalone formalization is what closes Phase A4. The phase covers composition pairs of foundational commitments through a tiered structure that tracks the source paper's commitment hierarchy; the closing note synthesizes the three Pattern operationalizations into completeness for hybrid composition as a whole. Subsequent series-A phases move to operational tests as standalone (Phase A5) and boundary cases (Phase A6); after Series A, the project moves to Series B (Paper 2 derivation) and Series C (cross-derivation).

## 2. Exhaustive coverage of legitimate composition flows

The three patterns are exhaustive in the precise sense that every legitimate composition flow between a CKS substrate and an adjacent AI component is one of three architectural behaviors.

**Pattern A — consultation flow.** A CKS cell, executing under its orchestration rule, consults an adjacent component (a retrieval index, a fine-tuned model, a vector database, an external structured store) for additional context, then writes its outputs back to the substrate under its rule. The flow direction is cell-to-adjacent for consultation and cell-to-substrate for the write. The adjacent component is part of the cell's reasoning environment.

**Pattern B — derivation flow.** Substrate content is indexed, embedded, or summarized into an adjacent component to support specific queries — a vector index for semantic search, a derived knowledge graph, a search-optimized projection. The flow direction is substrate-to-adjacent. The adjacent component is read as a derived view; it is not authoritative on coordination questions, and any conflict with the substrate is resolved in the substrate's favor.

**Pattern C — no flow.** The adjacent component handles a distinct concern that does not affect coordination state — a retrieval system answering reference-document queries entirely outside coordination scope, a fine-tuned model used for tasks the substrate does not represent. There is no architectural coupling between the two systems on coordination questions.

These three flows — consultation, derivation, and no-flow — exhaust the architecturally legitimate possibilities. Every other compositional behavior an adjacent component might exhibit either reduces to one of the three (and is governed by that pattern's requirements) or fails to be a legitimate composition at all (and is governed by the anti-pattern formalizations in §4 below). The exhaustiveness is what makes "is the composition legitimate?" a question with a finite answer space: the deployment maps each adjacent component to one of three known patterns, or it does not.

## 3. Mutual distinguishability through architectural specification

The three patterns are mutually distinguishable in the sense that each carries a distinct architectural specification, and the specifications do not overlap. The distinguishability is operationally testable through the sharpening properties the individual Pattern operationalizations articulate.

Pattern A is distinguished by *cell-mediated consultation flow with rule-governed write*. The cell reads from the substrate as the source of truth, may also query the adjacent component, and writes back to the substrate under its orchestration rule with provenance recording the consultation. The architectural signature is unidirectional consultation followed by rule-mediated processing of the consultation response into substrate content; the adjacent component does not gain write authority through the consultation.

Pattern B is distinguished by *unidirectional substrate-to-adjacent derivation with non-authoritative views*. The view is regeneratable from substrate state, is read but not written by participants in the coordination work, and yields to the substrate on conflict. The architectural signature is one-way flow with the adjacent component holding no authority the substrate does not delegate to it as derived content.

Pattern C is distinguished by *no coordination flow*. The adjacent component does not consult substrate content for its own operation, does not produce derived views of substrate content, and does not write substrate content. The architectural signature is the absence of architectural coupling on coordination questions; the two systems coexist without their coordination-state behaviors entangling.

The three signatures are non-overlapping. A composition cannot exhibit consultation flow and derivation flow simultaneously over the same content — that would be bidirectional coupling, which is precisely what the hidden-bidirectional-coupling anti-pattern names. A composition cannot exhibit consultation flow and no flow over the same coordination concern — the consultation, by definition, is a coordination flow. A composition cannot exhibit derivation flow and no flow over the same content — the derivation, by definition, makes the adjacent component a view of that content. The non-overlap is what makes pattern mapping unambiguous: for any adjacent component and any coordination concern it touches, the position it occupies relative to the substrate is one and only one of the three.

## 4. Coherence in excluding the composition anti-patterns

The three patterns are coherent in the sense that, together, they exclude the composition anti-patterns the source paper preempts. Three anti-patterns are formalized in this derivation series; each is excluded by the joint operation of the three legitimate patterns.

*Ungoverned writer.* An adjacent component writes coordination state outside cell mediation and orchestration-rule authorization. Pattern A processes consultation responses through the cell and its rule, never giving the adjacent component direct write authority; Pattern B is unidirectional from substrate to adjacent, with no adjacent-to-substrate write; Pattern C admits no coordination coupling at all. No legitimate pattern grants the adjacent component the write authority the anti-pattern requires.

*Hidden bidirectional coupling.* Substrate and adjacent component update each other through automated processes that no human-authored orchestration rule governs. The flow shape does not match Pattern A (cell-to-adjacent then cell-to-substrate under rule), Pattern B (substrate-to-adjacent only), or Pattern C (empty). The composition either resolves into a Pattern A plus Pattern B configuration with each direction governed by an orchestration rule, or it sits outside the legitimate space.

*Substrate substitute.* The deployment treats an adjacent component as the source of truth for coordination questions, gradually replacing or competing with the substrate. Pattern A's consultation semantics keep the substrate authoritative; Pattern B's non-authoritativeness blocks displacement through derivation; Pattern C handles a concern that is by construction not coordination state. No legitimate pattern provides the adjacent component the authoritative coordination role the anti-pattern requires.

The coherence claim is the conjunction: there is no composition flow outside Pattern A, Pattern B, and Pattern C that satisfies the source paper's commitments. The three legitimate patterns and the three anti-patterns together partition the composition space — three legitimate patterns inside, three anti-patterns outside, no fourth legitimate pattern between them.

## 5. The four operational components of three-patterns coherence

Three-patterns coherence is the architectural property a hybrid deployment exhibits when four conditions hold of its composition.

**(a) Exhaustive of legitimate composition flows.** Every coordination-relevant flow between the substrate and an adjacent component fits one of the three patterns: consultation (Pattern A), derivation (Pattern B), or no-flow (Pattern C). No coordination-relevant flow sits outside the three.

**(b) Mutually distinguishable for each adjacent component.** For each adjacent component, and each coordination concern it touches, the pattern it occupies is determined by the architectural signature of the flow — non-overlapping with the signatures of the other two patterns. The mapping is unambiguous.

**(c) Coherent in excluding the composition anti-patterns.** The composition exhibits no instance of ungoverned writing, hidden bidirectional coupling, or substrate substitute. Each anti-pattern is excluded jointly by the requirements of the three legitimate patterns; the absence of any legitimate pattern that admits the anti-pattern is what makes the exclusion architectural rather than procedural.

**(d) One pattern per adjacent component per concern.** Each adjacent component, considered against each coordination concern it touches, occupies exactly one of the three patterns. A single component may occupy different patterns for different concerns — a vector index may be a derived view of substrate content under Pattern B while answering ad-hoc reference queries under Pattern C — but on each concern, the pattern is uniquely determined.

The four components are not independent. (a) and (b) together imply a function from adjacent-component-and-concern pairs to patterns, defined on the legitimate composition space and total over coordination-relevant flows. (c) is what makes that function the right one — it maps to legitimate patterns rather than to anti-patterns. (d) is what makes the function single-valued. Together they constitute the meta-architectural property the three Pattern operationalizations imply but do not individually state.

## 6. Anti-patterns specifically violating three-patterns coherence

Three failure modes violate three-patterns coherence as a meta-property, distinct from the composition anti-patterns the individual patterns exclude.

*Pattern confusion.* A deployment claims to instantiate one pattern but actually exhibits the architectural signature of another — for example, presenting a Pattern A consultation that, on inspection, allows the adjacent component to write substrate content directly (and so functions as an ungoverned writer). The confusion may be deliberate (a marketing posture) or accidental (a mislabel because the deployment team has not separated the architectural signatures cleanly). Either way, mutual distinguishability fails: the adjacent component is not in the pattern the deployment claims it is in.

*"Fourth pattern" claims.* A deployment asserts that its composition is legitimate but does not fit any of the three patterns — typically by framing the composition as a novel arrangement the architecture has not yet contemplated. The framing concedes the structural claim; the architecture *has* contemplated the legitimate composition space and named it as exactly three patterns. A fourth pattern is not an open extension point; it is the claim that the composition is legitimate without being any of the three, which the coherence property rules out.

*Blended-pattern composition.* A deployment runs the same flow as a mixture of two patterns — for example, treating an adjacent component as a derived view (Pattern B) for some operations and as a cell consultation source (Pattern A) for others, *over the same content with the same flow*, in a way that fails to specify which pattern governs which operation. The blend is not a Pattern A or a Pattern B composition; it is an unspecified composition that participants resolve at runtime, with no architectural commitment determining which. Coherence requires that the pattern be determinate; blended compositions are determinate only by accident.

The three meta-anti-patterns share a common structure: the deployment asserts that its composition is legitimate but the assertion fails the coherence property by mislabeling (pattern confusion), by claiming a position outside the space (fourth pattern), or by failing to commit to a position within the space (blended pattern). Naming the three is what makes the failures visible at deployment review.

## 7. Operational test

A hybrid deployment instantiates three-patterns coherence if and only if all of the following are true at all times during the deployment's existence.

1. **Adjacent-component-pattern-mapping.** Every adjacent AI component the deployment uses is mapped to one of the three patterns for each coordination concern it touches, and the mapping is recorded as part of the deployment's architectural specification rather than left implicit.

2. **Pattern distinguishability.** For each adjacent component and each concern, the architectural signature of the composition matches the requirements of the mapped pattern: Pattern A's cell-mediated consultation with rule-governed write and provenance for the consultation, Pattern B's unidirectional substrate-to-adjacent derivation with non-authoritative regeneratable views, or Pattern C's absence of coordination coupling. The signature is verifiable by reading the substrate's provenance records, the orchestration rules that govern cell behavior, and the adjacent component's interface with the substrate.

3. **Anti-pattern exclusion.** No adjacent component, on any concern, exhibits the signature of an ungoverned writer, hidden bidirectional coupling, or substrate substitute.

The single-sentence form: *every adjacent component is mapped to exactly one pattern per concern, the mapped pattern's architectural signature is exhibited by the actual composition behavior, and no anti-pattern signature appears anywhere in the composition.* A deployment that satisfies this sentence instantiates three-patterns coherence; one that fails any clause does not, even if it satisfies the individual Pattern requirements for the components it does map cleanly.

## 8. Why naming three-patterns coherence as standalone matters; closing Phase A4

Three-patterns coherence is what makes hybrid-composition verification a finite, principled procedure rather than an ad hoc one. With the meta-property unnamed, deployment review must reason about each adjacent component in isolation, with no architectural vocabulary for "is the composition as a whole legitimate?" — the only available framing is "does this component fit a pattern?", which leaves "are the three patterns the right pattern set?" implicit. Naming the meta-property gives review a vocabulary for the second question and a procedure for verifying the answer (the four operational components of §5 and the three sharpening properties of §7).

Beyond verification, the meta-property carries a completeness claim that distinguishes CKS from architectures with unspecified composition flows. Many AI architectures admit hybrid composition as a deployment concern but do not commit to which compositional behaviors are legitimate; the design space is open-ended, and "novel composition" is treated as something to be discovered case by case. CKS commits to the opposite stance: the legitimate composition space is exactly three patterns, the three are exhaustive of legitimate composition flows, mutually distinguishable, and coherent in excluding the anti-patterns; any composition outside the three is an anti-pattern by construction, not a fourth-pattern candidate. The completeness is what makes the architecture defensible against the drift that produces the anti-patterns the architecture explicitly excludes.

The standalone formalization closes Phase A4 of Series A. The phase has covered foundational composition pairs of A1's commitments at its first tier; the meta-architectural clusters around composition requirements, three adjacencies, and orchestration-layer distinctions at its second through fourth tiers; and the three legitimate patterns operationalized individually at the first three notes of the fifth tier. The closing note synthesizes the fifth tier into completeness, articulating that the three Pattern operationalizations together specify the legitimate composition space rather than each specifying a fragment of it. With the closing note in place, Phase A4's thirty-note corpus provides comprehensive operationalization of A1 foundational commitments through composition pairs covering all architecturally significant pairs and the meta-architectural commitment clusters. Subsequent work in Series A moves to Phase A5 (operational tests as standalone) and Phase A6 (boundary cases and edge scenarios); after Series A, the project moves to Series B and Series C. Subsequent work that adopts, extends, or argues against the CKS hybrid-composition commitment should use *three-patterns coherence* in the sense formalized here — the joint property of exhaustiveness, mutual distinguishability, and anti-pattern exclusion — and should treat any composition that fails the property as outside the architecture's legitimate space, regardless of whether the individual adjacent components fit specific Pattern operationalizations in isolation.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Coherence of the Three Patterns: How Pattern A, Pattern B, and Pattern C Together Specify Legitimate Hybrid Composition in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
