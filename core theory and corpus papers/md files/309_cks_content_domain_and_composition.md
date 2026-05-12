# Content-Domain and Composition: How Content-Domain Specifications Enable and Constrain Composition in the CKS Pattern

**Derivation Note B2.92 — Phase B2, Series B**
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, how content-domain specifications enable and constrain composition at every structural level of the CKS pattern, so that downstream work can adopt or argue against the content-domain-and-composition relationship without ambiguity.

## Abstract

The CKS pattern specifies that entities at every structural level — cell, aspect, Self — carry content-domain specifications describing the informational territory each entity operates over. Composition per A1.13 requires not only structural compatibility but content-domain compatibility: for a cell to be validly composed into an aspect, the cell's content-domain must meaningfully address the aspect's coordination purpose; for an aspect to be validly integrated into a Self, the aspect's content-domain must fit within the Self's integration scope. Content-domain compatibility is a semantic requirement, distinct from and additional to technical interface compatibility (API type matching). When an aspect's content-domain contains gaps uncovered by any of its cells, or when two cells in the same aspect carry overlapping content-domains, both conditions register as first-class conflicts per A1.03 and are submitted to governance resolution rather than silently tolerated or automatically blocked. The A5.14 composition-requirements-five test includes a content-domain compatibility check as one of its five requirements. This note formalizes the content-domain-and-composition relationship as the fourth decomposition of B1.18, following B2.89 (content-domain integrating frame), B2.90 (content-domain specification requirements), and B2.91 (content-domain boundaries and enforcement).

---

## 1. Why content-domain-and-composition requires standalone formalization

B2.89 established the integrating frame for content-domain: what a content-domain specification is, what it describes, and why every structural level in the CKS pattern carries one. B2.90 formalized the requirements a content-domain specification must satisfy to be operational. B2.91 formalized how boundaries are drawn and enforced. Each of these is necessary groundwork. None of them, however, answers the question that the A1.13 composition requirements make pressing: given that entities at every level carry content-domain specifications, what does composition require of those specifications?

The question matters architecturally because composition without content-domain compatibility produces structurally valid but semantically incoherent assemblies. A cell whose content-domain covers financial transaction processing can be syntactically composed into an aspect for clinical care coordination if the APIs type-match — both might accept structured data objects. But the cell's operational scope does not address the aspect's coordination purpose. The composition is technically complete and semantically hollow: the cell cannot contribute meaningfully to the aspect's work because the cell operates over a territory that has nothing to do with the aspect's territory.

This failure mode is not exotic or unusual. It is the standard failure mode of technically-interface-driven composition: components that type-match get composed; semantic scope is assumed to follow from technical fit; the assembly misbehaves in ways that are hard to diagnose because the misbehavior is not a crash but a content mismatch that propagates through governance records. The CKS pattern's response is to make content-domain compatibility an explicit composition requirement, register violations as A1.03 first-class conflicts, and include a content-domain check in the A5.14 composition validity test.

Naming content-domain-and-composition as a standalone derivation makes this response legible as an architectural commitment rather than an implementation hint. It places in the prior-art record the specific relationship between content-domain specifications (formalized in B2.89–B2.91) and composition requirements (formalized in A1.13), so that the combination is available as a defensible pattern under the author's name.

This note is the ninety-second note in Phase B2 and the fourth of five notes decomposing B1.18 content-domain. B2.93 (content-domain verification) will close the B1.18 decomposition. Subsequent Phase B2 notes will proceed to B1.19 cross-level access.

---

## 2. The architectural relationship precisely stated

### Cell-to-aspect composition compatibility

For a cell to be validly composed into an aspect, the cell's content-domain must be compatible with the aspect's content-domain. Compatibility requires three conditions to hold simultaneously:

**Operational scope relevance.** The cell's operational scope — what it does when executing — must address part of the aspect's coordination purpose. A cell that operates over employee scheduling data is operationally relevant to a workforce-coordination aspect; it is not operationally relevant to a regulatory-reporting aspect even if both aspects could in principle read scheduling data as input.

**Input type relevance.** The cell's input types must be relevant to the aspect's coordination domain. The inputs the cell consumes must bear on what the aspect is coordinating. Input type relevance is a content-domain test, not a data-type test: a cell may consume structured JSON objects (data-type match) while consuming structured JSON objects that describe financial instruments, not clinical decisions (content-domain mismatch for a clinical coordination aspect).

**Output utility.** The cell's outputs must be useful for the aspect's coordinated outputs. The cell's produced content must contribute to what the aspect produces as its coordination outputs. A cell that produces scheduling summaries contributes to a workforce-coordination aspect's output; it does not contribute to a regulatory-reporting aspect's output, even if the summary is a valid data structure the aspect could technically receive.

**Compatibility does not require identity.** A cell's content-domain need not cover the entire aspect's content-domain. The aspect is a coordination arrangement of multiple cells; each cell covers a portion of the aspect's coordination purpose. Compatibility requires meaningful contribution, not full coverage. Cells that each contribute distinct portions of an aspect's coordination purpose are jointly compatible; no single cell is required to be as broad as the aspect it serves.

### Aspect-to-Self composition compatibility

For an aspect to be validly integrated into a Self, the aspect's content-domain must be compatible with the Self's integration scope. This operates by the same logic at a higher level:

**Purpose fit.** The aspect's coordination purpose must fit within the Self's integration scope. An aspect organized around clinical care coordination fits within a Self that integrates clinical, regulatory, and operational intelligence as facets of one enterprise AI. It does not fit within a Self whose integration scope is confined to financial transaction processing.

**Output integrability.** The aspect's outputs must be integrable with other aspects' outputs within the Self. The Self holds multiple coexisting aspects under unified governance; those aspects' outputs must be capable of being integrated into the Self's collective intelligence. An aspect whose outputs are semantically foreign to every other aspect's domain cannot be integrated; it produces content that has no place in the Self's unified coordination.

**Integration scope coverage.** Taken together, the aspects composing a Self should collectively address the Self's integration scope. No single aspect need cover the entire Self scope; the Self's integration is the arrangement of aspects, each covering a portion of the scope. But significant portions of the Self's integration scope that are unaddressed by any aspect are composition gaps requiring governance attention.

### Content-domain gaps in composition

When an aspect's content-domain has regions not covered by any of the cells composed into that aspect, the gap is a composition concern. The aspect's coordination purpose extends into territory where no cell operates. Outputs and decisions in that territory have no cell-level basis; governance records lack cell-level provenance for that portion of the aspect's work.

Gaps register as A1.03 first-class conflicts. The conflict is semantic: the aspect's declared scope commits to more territory than its cell composition covers. Governance resolves the conflict through one of two paths: adding cells whose content-domains address the gap, or narrowing the aspect's content-domain specification per B2.91 boundary adjustment to match what its actual cell composition covers. The gap is not silently tolerated (which would leave the aspect's coordination purpose partially unfulfilled without record) and not automatically blocked (which would prevent valid deployments from building aspects incrementally).

### Content-domain overlaps in composition

When two or more cells composed into the same aspect carry overlapping content-domains — when both operate over the same portion of the aspect's coordination territory — the overlap is a composition concern. Both cells will produce outputs bearing on the same territory; the aspect must determine how to integrate or adjudicate those outputs.

Overlaps also register as A1.03 first-class conflicts. The conflict is coordination-semantic: the aspect carries redundant or competing coverage of a portion of its purpose, without a governance-authorized resolution of how the redundancy is to be handled. Governance resolves the conflict through directed selection per B1.14: the governance authority may reduce the overlap by restricting each cell's domain specification to a non-overlapping portion of the shared territory, by retiring one cell whose contribution is wholly superseded by the other, or by explicitly authorizing both cells' contributions and specifying how their outputs are to be combined. The overlap is not automatically rejected; it is registered and presented for governance decision.

### A5.14 composition validity test

The composition-requirements-five test includes content-domain compatibility as one of its five checks. For any proposed composition, the test verifies:

- That each cell's content-domain is compatible with the aspect into which it is composed.
- That each aspect's content-domain is compatible with the Self into which it is integrated.
- That no ungoverned content-domain gaps exist between an aspect's declared scope and its cell composition.
- That no ungoverned content-domain overlaps exist between cells in the same aspect.

Failing any of these sub-checks produces an A1.03 conflict in the governance record. The composition is not automatically invalidated by a failed check — A1.03 governs conflict as first-class object requiring resolution, not as automatic rejection — but the composition is flagged for governance attention before it is treated as valid.

### Content-domain as composition design tool

Beyond validation, content-domain specifications function as design instruments for building compositionally coherent assemblies:

Aspect design begins with a purpose statement per B2.15. The aspect's coordination purpose defines a content-domain: the territory of informational work the aspect is organized to perform. Cell selection follows from that domain: cells whose content-domains address the aspect's purpose are candidates for composition; cells whose domains do not address the purpose are candidates for other aspects or for retirement.

Self design begins with an integration scope per B2.21. The Self's integration scope defines the collective territory of its aspects. Aspect selection follows: aspects whose content-domains collectively address the integration scope compose the Self; aspects whose domains fall outside the scope do not belong.

Content-domain specifications thus propagate design intent downward through the structural hierarchy: Self scope → aspect purpose → cell operational scope. The specifications make the propagation explicit in substrate-held governance records rather than implicit in assembly conventions.

### Content-domain changes and composition validity

When content-domain boundaries change per B2.91 — through governance-authorized expansion or contraction — composition validity may be affected:

Expanding a cell's content-domain may improve its fit with the aspect it serves (covering a previously uncovered portion of the aspect's purpose) or may introduce new overlaps with other cells in the same aspect. Both effects require governance review.

Contracting a cell's content-domain may create composition gaps (the cell now covers less of the aspect's purpose) or may resolve overlaps (the cell's domain no longer overlaps another cell's domain). Both effects also require governance review.

Governance reviews composition validity after any content-domain boundary change that affects a composed entity. The review uses the A5.14 composition validity test and registers any newly arising conflicts as A1.03 objects.

---

## 3. What makes content-domain-and-composition architecturally distinctive

Conventional AI component composition relies primarily on technical interface compatibility: component A can be composed with component B if A's output type is a valid input type for B. The composition is valid when APIs match. Semantic scope — what A and B are actually doing, what informational territory they each address — is left to the engineer's judgment and typically not enforced by the architecture.

This is a pragmatic choice in component ecosystems where the cost of semantic compatibility verification is high and the component providers do not share a common semantic vocabulary. It is not, however, a costless choice: assemblies built on technical-only compatibility can misbehave in ways that are semantically coherent from neither component's perspective, and the misbehavior does not manifest as a type error or API exception.

CKS content-domain composition adds a semantic compatibility layer that runs alongside technical interface compatibility. Both checks are required; they are separate checks rather than one check. A cell may type-match an aspect's API while having a non-compatible content-domain, and a cell may have a compatible content-domain while failing a technical interface check. Neither check subsumes the other.

The semantic layer is what A1.13 composition requirements formalize. Composition requirements in the CKS pattern are not only structural; they include the semantic requirement that composing entities address compatible informational territories. This is the distinctive move: formalizing semantic compatibility as an architectural requirement with the same standing as structural compatibility.

The A1.03 conflict treatment amplifies this distinctiveness. In conventional component ecosystems, semantic scope mismatches are not errors — they are design decisions that produce suboptimal outcomes without triggering governance machinery. In CKS, content-domain gaps and overlaps register as first-class conflicts in the governance record. They become visible, addressable, and provenance-tracked. Governance resolves them; the resolution is recorded. This transforms the failure mode from a silent runtime drift into a visible governance concern.

---

## 4. The biological analog

The biological analog for content-domain composition is the functional specificity that governs cellular composition into tissues. Blood cells — red blood cells carrying oxygen, white blood cells mediating immune response — compose into blood tissue because their functional domains address the tissue's functional purpose: oxygen transport and immune defense. Neurons compose into neural tissue because their functional domains address that tissue's purpose: signal processing and transmission. Cardiac muscle cells compose into cardiac muscle tissue because their functional domains address that tissue's purpose: rhythmic contraction. A red blood cell does not compose into cardiac muscle tissue; its functional domain does not address that tissue's purpose, regardless of whether the cell could mechanically occupy the tissue's physical space.

CKS content-domain composition is the governed architectural analog of this biological principle. Cells whose content-domains address an aspect's coordination purpose compose into that aspect; cells whose content-domains do not address the purpose do not belong in that aspect's composition, regardless of whether they could mechanically satisfy a technical interface check. The parallel is not incidental: Paper 2 develops the biological scaffold precisely because content-domain-governed composition is among the architectural commitments the biology makes intuitive.

The analog functions as conceptual scaffold. The architectural substance is content-domain specifications held in human-governed substrate, compatibility requirements authored per A2.04, and gaps and overlaps registered as A1.03 conflicts. The biology motivates the pattern; the CKS pattern instantiates it with properties biology cannot provide: content-domain specifications are explicit and inspectable rather than encoded in protein expression; compatibility requirements are human-authored and modifiable rather than fixed by evolutionary history; gaps and overlaps are governance-visible rather than resolved silently through selective pressure.

---

## 5. Inherited Paper 1 commitments

Several Paper 1 architectural commitments are directly load-bearing for content-domain-and-composition:

**A1.13 — Composition requirements.** Content-domain compatibility is one of the five composition requirements the composition-requirements-five test verifies. A1.13 establishes the requirement set; content-domain compatibility is the semantically distinctive addition Paper 2 specifies at each structural level.

**A5.14 — Composition-requirements-five test.** The operational test that checks whether a proposed composition satisfies A1.13's requirements. The content-domain compatibility check is one of the five sub-checks the test runs. A5.14 is the formal verification mechanism for composition validity.

**A1.03 — Conflict as first-class object.** Content-domain gaps and overlaps in composition register as A1.03 conflicts. The first-class conflict architecture is what makes composition domain issues visible and governable rather than silent. A1.03's two-level handling applies: substrate-level preservation of the conflict record, and cell-level (or governance-level) resolution under orchestration rules.

**A2.04 — Rule authoring.** Content-domain compatibility requirements are authored as orchestration rules under A2.04. The rules specify what compatibility means for a given aspect's purpose, what counts as an unacceptable gap, and how overlaps are to be resolved. Human authorship of these rules is what makes content-domain compatibility a governed requirement rather than an emergent property.

**A1.01 — Governance.** Composition validity — including content-domain compatibility — is governed under A1.01's human-governed commitment. Governance authority over composition means humans hold the rights to inspect, modify, and override composition decisions, including decisions about whether a content-domain gap or overlap is acceptable in a given deployment.

**A2.40 — Provenance.** Composition validity events — including content-domain compatibility checks and their outcomes — are recorded with provenance metadata per A2.40. The record of which content-domain compatibility checks passed, which generated A1.03 conflicts, and how those conflicts were resolved is substrate-held, traceable, and inspectable.

---

## 6. Operational implications

Deployments that instantiate content-domain-and-composition as formalized here face several operational implications:

**Aspect design starts with purpose.** The aspect's coordination purpose per B2.15 is the design anchor for cell selection. Before cells are selected for composition, the aspect's content-domain must be specified. Cell selection then proceeds by matching candidate cells' content-domains against the aspect's specified domain.

**Self design starts with integration scope.** The Self's integration scope per B2.21 is the design anchor for aspect selection. Before aspects are integrated into a Self, the Self's integration scope must be specified. Aspect selection proceeds by matching candidate aspects' content-domains against the specified scope and verifying collective coverage.

**Gap and overlap analysis runs at design time and periodically during operation.** At composition design time, the A5.14 test identifies gaps and overlaps and registers them as A1.03 conflicts before the composition is treated as valid. During operation, as cells are added, retired, or modified, gap and overlap analysis re-runs to detect newly arising composition issues.

**A1.03 conflict registry is populated with composition domain conflicts.** The governance record of a deployed CKS system holds content-domain composition conflicts alongside behavioral and coordination conflicts. Operators reviewing the A1.03 registry see composition domain issues as named, addressable governance concerns. This is the operational form of the A1.03 first-class treatment.

**Governance resolves through directed selection.** The A1.03 conflict resolution path for composition domain issues is directed selection per B1.14: governance refines domain specifications, adds or removes cells, or explicitly authorizes overlap arrangements with specified resolution rules. Each resolution action is substrate-held and provenance-tracked per A2.40.

**Content-domain boundary changes trigger composition review.** Any governance-authorized change to a content-domain boundary per B2.91 requires re-running the A5.14 test for all compositions involving the entity whose boundary changed. This is an operational discipline rather than an optional review.

**Cross-partner composition requires cross-partner content-domain compatibility verification.** For compositions that cross organizational boundaries per A2.47, content-domain compatibility verification extends across the boundary. The partner's cell or aspect content-domain must be verified against the local aspect or Self content-domain. The same compatibility requirements apply; the governance machinery must extend to cover the cross-partner case.

---

## 7. Limits

Content-domain compatibility, as formalized here, operates within explicit limits:

**Compatibility does not guarantee behavioral correctness.** A cell whose content-domain is compatible with an aspect's coordination purpose may still behave incorrectly in that aspect. Content-domain compatibility verifies semantic scope fit — that the cell operates over the right informational territory — not that the cell operates correctly over that territory. Behavioral correctness is a separate verification concern addressed by other CKS architectural commitments.

**Compatibility is a necessary but not sufficient condition.** A composition that fails content-domain compatibility is certainly compositionally invalid. A composition that passes content-domain compatibility has satisfied one of the A1.13 requirements; it must also satisfy the remaining four requirements the A5.14 test checks. Content-domain compatibility clears one gate; it does not clear all gates.

**Technical interface compatibility is separate.** Content-domain compatibility and technical interface compatibility (API type matching) are two distinct checks that both apply to valid compositions. A cell may pass content-domain compatibility while failing technical interface checks, or pass technical interface checks while failing content-domain compatibility. The two checks are independent; neither subsumes the other; both are required.

**Compatibility is not equivalence.** For a cell's content-domain to be compatible with an aspect's content-domain, the cell need not cover the entire aspect's territory. Compatibility requires meaningful contribution, not identity of scope. This is the design freedom that makes multi-cell aspects possible: distinct cells with distinct but compatible content-domains collectively address the aspect's coordination purpose.

**Gaps and overlaps are governance concerns, not automatic blockers.** The A1.03 first-class conflict registration for gaps and overlaps means they are visible and require governance resolution. It does not mean they automatically invalidate a composition. A deployment may operate with a known content-domain gap for a period while governance decides how to resolve it — the gap is in the conflict registry, under active governance attention, with provenance tracking. The absence of automatic blocking is a deliberate architectural choice: it preserves governance authority over the resolution rather than delegating that authority to automatic rejection logic.

**Content-domain specifications are substrate-held and governance-revisable.** No content-domain specification in the CKS pattern is fixed by a technical constraint external to the substrate. Specifications are substrate content, authored and modifiable by governance authority per A1.01. This means content-domain compatibility is not a permanent binary judgment; it is a current governance determination that can evolve as deployment understanding deepens and as content-domain specifications are revised.

---

## 8. Operational test

A composition instantiates content-domain-and-composition validity in the CKS sense if and only if all of the following are true:

1. Each cell composed into an aspect has a content-domain whose operational scope addresses part of the aspect's coordination purpose; whose input types are relevant to the aspect's coordination domain; and whose outputs contribute to the aspect's coordinated outputs.
2. Each aspect integrated into a Self has a content-domain whose coordination purpose fits within the Self's integration scope and whose outputs are integrable with the outputs of other aspects within the Self.
3. The A5.14 composition validity test has been run against the composition and any content-domain gaps or overlaps it identified are registered as A1.03 conflicts in the governance record.
4. Each A1.03 conflict registered under (3) is under active governance attention, with resolution path recorded in the substrate per A2.40.
5. No content-domain boundary change has been made to any participating entity since the last A5.14 test run without triggering a re-run of the test.

A composition that fails any of (1)–(5) may be a technically functional composition, but it is not a content-domain-valid composition in the CKS sense.

---

## 9. Why naming content-domain-and-composition as standalone matters

B2.89 through B2.92 together decompose B1.18 content-domain into its four operational dimensions: the integrating frame that situates content-domain across all three structural levels; the specification requirements a content-domain must satisfy; the boundary and enforcement mechanisms that keep content-domains operationally stable; and the composition relationship that makes content-domain functionally consequential.

Of these four dimensions, content-domain-and-composition is the one that ties content-domain back to the architectural machinery of A1.13 composition requirements and A5.14 composition validity. Without the composition relationship formalized, content-domain specifications are descriptive metadata — they describe what entities do without having architectural standing in the composition process. With the composition relationship formalized, content-domain specifications are composition prerequisites — their compatibility is required, their gaps and overlaps are first-class conflicts, and their evolution triggers composition review.

This transformation from descriptive metadata to composition prerequisite is what requires a standalone note. It is not a corollary of B2.89–B2.91; it is the architectural consequence of combining the content-domain commitment (B1.18) with the composition requirements commitment (A1.13). Formalizing the combination as prior art under the author's name, with the specific content-domain-gap-as-A1.03-conflict and A5.14-content-domain-check provisions named explicitly, places this combination in the defensible prior-art record before any party can claim novelty over it.

B2.93 will close the B1.18 decomposition with content-domain verification — the mechanisms by which content-domain compatibility claims are verified and the verification record is held in governed substrate. After B2.93, Phase B2 proceeds to the B1.19 cross-level access decomposition.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Content-Domain and Composition: How Content-Domain Specifications Enable and Constrain Composition in the CKS Pattern.* Derivation Note B2.92, Series B, Phase B2. May 12, 2026. ORCID: 0009-0004-8065-3235.
