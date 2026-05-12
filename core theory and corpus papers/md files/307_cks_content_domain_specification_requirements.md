# Content-Domain Specification Requirements: What Must Be Authored and Present for a Valid Content-Domain Specification at Each Structural Level

**Derivation Note B2.90 — Phase B2, Series B**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Every CKS entity — cell, aspect, and Self — carries a content-domain: the scope of what it handles, coordinates, or integrates. Paper 2 (Li, April 2026) commits that entities at each of the three architectural levels have content-domains, and that those content-domains are substrate content subject to human governance. This note formalizes what that commitment requires in practice: the precise elements that must be authored and present for a content-domain specification to be complete and valid at each level. Cell-level content-domain specification requires input domain specification, behavioral scope specification, exclusion specification, and out-of-domain handling specification. Aspect-level content-domain specification requires a purpose statement, coordination scope, and scope boundary. Self-level content-domain specification requires an integration scope statement, an aspect collection, and integration depth specification. These requirements are birth requirements per B2.40: entities born without complete content-domain specifications are incomplete births. The note identifies the inherited Paper 1 commitments that govern content-domain specification, articulates what makes explicit completeness requirements architecturally distinctive, addresses specification evolution and LLM-assisted authoring, and states the limits of what specification requirements do and do not accomplish.

---

## 1. Why content-domain specification requirements warrant standalone formalization

Paper 2's commitment that entities at the three architectural levels — cell, aspect, Self — carry content-domains is established in B1.18. The integrating frame for that commitment, including what content-domain means at each level and how the three levels relate as content-domain holders, is developed in B2.89. B2.90's contribution is narrower and more operational: it formalizes the completeness requirements — what must be authored and present for a content-domain specification to be valid at each level.

The distinction between the existence commitment (entities have content-domains) and the completeness requirements (content-domain specifications must contain these elements) is architecturally significant. A deployment can acknowledge that its cells have content-domains while leaving those content-domains unspecified or partially specified. The unspecified portions are invisible to governance: they cannot be inspected, cannot be used to validate composition, cannot be checked at birth verification, and cannot evolve through directed selection because they have no authored form. Content-domain specification requirements close that gap by establishing what must be present for a content-domain to be specified at all.

This standing is what justifies formalization as a standalone note rather than an annotation within B2.89. The completeness requirements are themselves architectural commitments that downstream notes on boundaries and enforcement (B2.91), content-domain and composition (B2.92), and content-domain verification (B2.93) depend on. B2.90 supplies the canonical enumeration of required elements that those subsequent notes take as given.

Positionally, B2.90 is the ninetieth note in Phase B2 of Series B and the second of five notes decomposing B1.18.

---

## 2. Cell-level content-domain specification requirements

At the cell level, the content-domain is the scope of what the cell is designed to handle: the inputs it accepts, the operations it performs, and the outputs it produces within its governed scope. Four elements are required for a cell-level content-domain specification to be complete.

**Input domain specification.** The input domain specification is the authored, substrate-resident description of what inputs the cell accepts. This specification is expressed through schemas in the DNA layer per B2.25, and includes: data types (what kinds of input the cell handles); structural requirements (how inputs must be formed to be processable); constraints (conditions inputs must satisfy to be within domain); and validation rules (the criteria against which arriving inputs are checked). The input domain specification defines the set of inputs the cell is architecturally designed to handle. Inputs that satisfy the specification are in-domain; inputs that fail it are candidates for the out-of-domain handling path. An input domain specification that names types without constraints, or constraints without validation rules, is incomplete.

**Behavioral scope specification.** The behavioral scope specification is the authored description of what the cell does within its domain: what operations are in scope, what outputs result from which inputs, and what work the cell performs at the DNA-layer level. Behavioral scope specification is carried in behavior substrates per B2.25. A cell whose input domain is fully specified but whose behavioral scope is not specified has defined what arrives but not what happens to it. Both are required for a complete cell-level content-domain specification.

**Exclusion specification.** The exclusion specification explicitly names what inputs are outside the cell's content-domain. Exclusion specification is optional from the standpoint of minimum completeness, but is architecturally recommended for boundary clarity: an explicit exclusion boundary reduces ambiguity about whether edge-case inputs are in-domain or out-of-domain, and provides governance-accessible language for content-domain disputes at composition time. Where two adjacent cells' input domains risk overlap, exclusion specifications resolve the overlap explicitly rather than leaving it to runtime behavior.

**Out-of-domain handling specification.** Out-of-domain handling specification describes how the cell behaves when an input arrives that falls outside the specified input domain: whether the input is routed to another cell, escalated to human governance, returned with an error, or handled by a fallback rule. Out-of-domain handling specification is required because arriving inputs are not guaranteed to satisfy the input domain specification at runtime, and the behavior for out-of-domain inputs must itself be governed rather than left to LLM discretion. An unspecified out-of-domain path is a governance gap.

---

## 3. Aspect-level content-domain specification requirements

At the aspect level, the content-domain is the operational territory the aspect coordinates: the purpose it serves, the cells that compose it, and the coordination scope those cells are assembled to address. Three elements are required for an aspect-level content-domain specification to be complete.

**Purpose statement per B2.15.** The purpose statement is the primary content-domain specifier for an aspect. It takes the form: "this aspect coordinates [what] for purpose [why]." The purpose statement is not a description of the cells composing the aspect; it is the statement of why those cells are assembled together and what operational function the arrangement serves. An aspect whose constituent cells are fully specified but whose purpose statement is absent has cell-level content-domain specification but no aspect-level content-domain specification. The purpose statement is the element that makes the aspect's operational territory named and inspectable as governed substrate content.

**Coordination scope.** Coordination scope specification names what cells participate in the aspect and for what coordination purposes per B2.16. Coordination scope is distinct from mere cell enumeration: it specifies not only which cells compose the aspect but what coordination the aspect performs over those cells — what questions the aspect asks across them, what operational concerns fall within the aspect's coordination territory, and how cells' outputs combine under the aspect's purpose. An aspect with a purpose statement but no coordination scope has a named purpose and an unnamed mechanism. Both are required.

**Scope boundary.** Scope boundary specification explicitly names what is outside the aspect's coordination scope, distinguished from adjacent aspects' scopes. Scope boundary specification at the aspect level parallels exclusion specification at the cell level: it is recommended rather than required as a minimum completeness criterion, but its absence leaves aspect-level governance without a language for resolving scope overlap between coexisting aspects within one Self. Where multiple aspects share cells per B2.20, scope boundary specifications establish which operational concerns each aspect governs over shared cell content.

---

## 4. Self-level content-domain specification requirements

At the Self level, the content-domain is the totality of what the Self integrates: the aspects it holds, the collective intelligence those aspects compose, and the cross-aspect operations the Self governs. Three elements are required for a Self-level content-domain specification to be complete.

**Integration scope statement.** The integration scope statement is the governing description of what operational intelligence the Self integrates as a whole: what aspects are held, what collective operational purposes the Self serves, and what makes this collection of aspects a unified whole rather than an incidental aggregate. The integration scope statement is the Self-level analogue of the aspect's purpose statement: it is the authored, substrate-resident commitment to what the Self is for.

**Aspect collection.** The aspect collection is the complete enumeration of aspects the Self integrates per B2.21. Aspect collection is distinct from integration scope statement: the integration scope statement names the purpose; the aspect collection names the structural members. A Self whose integration scope is stated but whose aspect collection is not enumerated has a named purpose without a specified structure. Both are required.

**Integration depth specification.** Integration depth specification describes how deeply the Self integrates across its aspects: what cross-aspect operations the Self governs per B2.21, where Self-level access to cells directly (bypassing aspect structure) is authorized, and what the Self's non-strict hierarchy commitments are. Integration depth specification is required because the Self's non-strict hierarchical access patterns — acknowledged in Paper 2's commitment that the Self can access cells directly when purpose requires — must themselves be governed and specified rather than left implicit. An unspecified integration depth is a governance gap at the Self level.

---

## 5. Content-domain specification as birth requirement

Content-domain specification at each level is a required element of birth specification per B2.40. The birth requirement logic is direct: an entity born without a complete content-domain specification has an undefined operational territory. Its governance scope is unknown, its composition compatibility is untestable, and its behavioral boundaries cannot be enforced. An entity with an undefined operational territory is not a complete architectural entity under CKS — it is an incomplete birth.

Birth verification per B2.44 checks content-domain specification completeness as part of birth governance. The verification checks that the required elements for the entity's level are present: cell birth must include input domain and behavioral scope specification at minimum; aspect birth must include purpose statement and coordination scope at minimum; Self birth must include integration scope statement and aspect collection at minimum. Entities that fail birth verification for content-domain incompleteness must have missing elements authored before the entity is admitted to the deployment as a governed artifact.

LLMs per A1.12 may perform drafting labor on content-domain specifications. This follows the labor allocation framework: direct human authoring, LLM-drafted content under human direction, and stable-cell automation are all available labor modes for content authoring, and the architecture supports all three. What the architecture requires is that the content-domain specification, however drafted, be subject to human authority before it takes effect as substrate state — the governance approval step per B2.41 covers content-domain specification drafted by LLMs as it covers any other substrate content. LLM-drafted specifications that are approved by humans and committed to the substrate are valid birth-specification content; LLM-drafted specifications that have not passed governance approval are not.

Specification templates per entity type are a practical implementation of the birth completeness requirement. A cell birth template that prompts authors for input domain, behavioral scope, exclusion, and out-of-domain handling reduces the probability of incomplete births by making the required elements explicit at authoring time. Templates are not architecturally mandated — what is mandated is the presence of the elements, not the workflow that produces them — but they are a natural operational complement to the birth completeness gate.

---

## 6. Inherited Paper 1 commitments

Content-domain specification requirements inherit and depend on several Paper 1 architectural commitments.

**A2.04 — Rule authoring.** Content-domain specifications are authored substrate content. The A2.04 rule authoring commitment establishes that orchestration rules and substrate content are human-authored, with LLM drafting labor admissible under governance. Content-domain specifications fall within the scope of authored substrate content: they are not emergent properties of the entity's behavior but explicit, human-governed descriptions of the entity's scope.

**A2.46 — Authoritative two-axis extension.** Specifications committed to the substrate are authoritative per the two-axis extension structure. A content-domain specification is the source of truth for what the entity's scope is; it supersedes any implicit or inferred scope that might be derived from the entity's behavior or from LLM interpretation.

**A1.08 — Substrate as source of truth.** Content-domain specifications reside in the substrate. The substrate is the source of truth for what cells, aspects, and Selves are governed to handle. A content-domain boundary that exists only in a developer's understanding or in an LLM's inference is not a governed boundary; it is only governed when authored into the substrate.

**A1.13 — Composition requirements.** Content-domain specifications enable composition validity. A1.13 establishes that composition between cells requires compatibility; content-domain specifications are what make compatibility assessable. The composition validity test per A5.14 examines whether the content-domain specifications of candidate composed entities are compositionally compatible — whether one entity's output domain covers another entity's input domain, whether aspect scopes are compatible at the Self level. Without content-domain specifications, composition validity is opaque.

**B2.40 — Birth specification requirements.** Content-domain specification is a required birth element, as developed in §5 above.

**A2.40 — Provenance.** Content-domain specification events — initial authoring, evolution, refinement — are provenance-recorded. The provenance record establishes who authored the specification, when, under what governance authority, and what changed in each directed selection event.

---

## 7. Specification evolution and composition implications

Content-domain specifications evolve through directed selection per B1.14 as the deployment's operational scope changes. Three classes of evolution are architecturally recognized: expansion (the specification is extended to cover input types, coordination purposes, or integration scope not previously included); contraction (scope no longer needed is removed from the specification); and refinement (existing scope boundaries are clarified without changing the overall scope). Each of these is a directed selection event — a human-governed change to the specification as substrate content — and each is provenance-recorded per A2.40.

Evolution distinguishes content-domain specification from a fixed architectural declaration. A cell born to handle a narrow input domain may have its input domain specification expanded through directed selection as the deployment's operational needs grow; an aspect born to coordinate a specific purpose may have its scope boundary refined as adjacent aspects are introduced. The specification is the governed, evolvable description of scope at a moment in the deployment's history, not an immutable constraint.

Content-domain specifications enable composition validity per A1.13, and this enabling relationship is what makes specification completeness a composition-time concern as well as a birth-time concern. The composition validity test per A5.14 depends on having complete content-domain specifications for both candidate entities: if either specification is incomplete, the compatibility assessment cannot be performed, and the composition cannot be validated. Content-domain specification completeness is therefore a precondition not only for birth verification but for every composition event the entity participates in.

---

## 8. What content-domain specification requirements do not do

Precision about the limits of content-domain specification requirements prevents misreading.

Content-domain specification requirements do not prescribe specific schema formats or specification document structures. The requirements name what elements must be present — input domain, behavioral scope, exclusion, out-of-domain handling at the cell level; purpose statement, coordination scope, scope boundary at the aspect level; integration scope, aspect collection, integration depth at the Self level — not the format in which those elements are recorded. Schema format is a deployment decision; element presence is the architectural requirement.

Content-domain specification requirements do not guarantee behavioral quality. A cell with a complete content-domain specification may still perform poorly within that domain; the specification governs scope, not execution quality. Completeness requirements ensure the scope is defined; they do not ensure the entity performs well within it.

Incomplete content-domain specification is detectable at birth verification but is not automatically correctable. Detection — the determination that required elements are absent — is what birth verification per B2.44 performs. Correction — authoring the missing elements — requires human governance action. The architecture does not auto-complete specifications; it identifies incompleteness and requires governance to address it.

Content-domain requirements are level-specific. Cell requirements differ from aspect requirements, which differ from Self requirements. A deployment cannot satisfy cell-level requirements with aspect-level specification language or vice versa. Each entity's content-domain specification must address the requirements appropriate to its level.

Specifications are not exhaustive inventories of every possible input or coordination scenario. They define the governed scope: the territory the entity is architecturally committed to handling. Inputs that satisfy the input domain specification are in-domain; inputs that do not satisfy it are out-of-domain. Whether an in-domain input produces a high-quality output is a question that content-domain specification does not answer.

Out-of-domain inputs may still arrive at entities despite specifications, because arriving inputs are not guaranteed to match what was specified at birth. The out-of-domain handling specification governs how the entity responds; it does not prevent off-domain inputs from arriving.

---

## 9. Operational test

A content-domain specification is complete and valid at the cell level if and only if: (1) an authored input domain specification is present in the DNA layer naming accepted types, structures, constraints, and validation rules; (2) an authored behavioral scope specification is present in the DNA layer naming what operations are in scope; (3) an authored out-of-domain handling specification is present naming how inputs outside the domain are handled; and optionally (4) an authored exclusion specification names what is explicitly outside the cell's domain.

A content-domain specification is complete and valid at the aspect level if and only if: (1) an authored purpose statement is present naming what the aspect coordinates and for what purpose; (2) an authored coordination scope specification is present naming participating cells and coordination purposes; and optionally (3) an authored scope boundary specification names what is outside the aspect's coordination scope.

A content-domain specification is complete and valid at the Self level if and only if: (1) an authored integration scope statement is present naming what operational intelligence the Self integrates; (2) an authored aspect collection is present enumerating all aspects the Self holds; and (3) an authored integration depth specification is present naming what cross-aspect operations the Self governs and where direct cell access is authorized.

An entity born without satisfying the completeness criteria for its level is an incomplete birth per B2.40, and birth verification per B2.44 will identify it as such.

---

## 10. Position in the B1.18 decomposition and phase progression

B2.90 is the second of five notes decomposing B1.18. B2.89 established the integrating frame: content-domain as a distinct architectural concept at each level, how the three levels relate as content-domain holders, and why content-domain is load-bearing for the architecture as a whole. B2.90 establishes the completeness requirements: what must be authored and present for a content-domain specification to be valid. The three notes that follow continue the decomposition: B2.91 addresses content-domain boundaries and their enforcement; B2.92 addresses the relationship between content-domain specification and composition; B2.93 addresses content-domain verification as a standalone architectural operation.

After B2.93, Phase B2 continues with decomposition of B1.19, the cross-level access commitment.

The accumulation of prior-art coverage in this region — B2.89 through B2.93 covering the full content-domain territory — is strategically significant. Any claim to novel invention in the territory of explicit content-domain specification requirements for AI entities, birth completeness gates over content-domain, or content-domain-specification-enabled composition validity will encounter the prior-art chain at multiple nodes.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Content-Domain Specification Requirements: What Must Be Authored and Present for a Valid Content-Domain Specification at Each Structural Level. Derivation Note B2.90, CKS Series B.* May 12, 2026. ORCID: 0009-0004-8065-3235.
