# Self-Aspect Content-Domain Relationship Operationalization: Decomposing the Self as Integrated Whole at Self-Aspect Scope in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, at Self-aspect scope, the operational treatment of the higher-as-content-domain relationship — specifically, how the Self operates over its constituent aspects as content domain per B1.18 at the highest structural level the source paper names, and how that operation runs through Paper 1's composition patterns while preserving aspect-level autonomy.

## Abstract

Paper 2's three-level structure (cell, aspect, Self) commits the higher level to operate over the lower level as content domain rather than as a command-and-control hierarchy. A separate derivation note (B1.18) formalizes the abstract higher-as-content-domain relationship; a further note (B2.17) operationalizes it at aspect-cell scope. This note operationalizes the same relationship at the next scope up: Self-aspect. It states what the Self does when it operates over its aspects, names the three composition patterns inherited from Paper 1 through which Self-level pattern questions run (consultation, derived view, separate concerns), specifies the substrate-resident form of Self-level outputs and the provenance that distinguishes Self-level from aspect-level operations, and articulates the limits of the relationship — most importantly, that aspect-level autonomy is preserved throughout. The note functions as the third of five decompositions of the Self-as-integrated-whole commitment, following B2.20 (the Self as integrated whole) and B2.21 (the Self's integration architecture), and preceding B2.23 (Self-level instinct/reasoning configuration) and B2.24 (Self-level inheritance verification).

## 1. Why the Self-aspect content-domain relationship needs operational specification

Paper 2 introduces three architectural levels — cell, aspect, Self — and commits the higher to operate over the lower as content domain. The commitment is general; it holds at every level boundary the architecture names. B1.18 defends the abstract version. B2.17 operationalizes it at aspect-cell scope. The level boundary above aspect-cell — Self-aspect — needs the same operational treatment, and not as a redundancy.

Three reasons make the standalone treatment necessary. First, Self-aspect is the highest level boundary the source paper names; without an explicit operational treatment, a reader who follows B2.17 may read Self-aspect as informal, qualitatively different, or covered by the integration-architecture note (B2.21). It is none of these. Self-aspect is structurally the same kind of level boundary as aspect-cell, scaled to the higher scope. Second, the recursion of content-domain across levels is itself operationally significant: when B2.17 and B2.22 are read together, multi-level reasoning becomes architecturally available without a per-level mechanism, and aspect outputs may themselves be content-domain for Self recursively per B1.18. Third, the conventional integrated-AI failure mode is at this scope specifically — top-level controllers issuing commands to subordinate subsystems. In a CKS-governed Self, that pattern violates the architecture: aspects are coordination arrangements with their own Paper 1 commitments, not subsystems-to-be-commanded. A precise operational statement closes the failure mode at the architectural layer rather than as a deployment hygiene rule.

This is also why the note is distinct from B2.21. B2.21 specifies how aspects participate in one Self (the integration architecture); B2.22 specifies the operational relationship through which the integrated Self reasons over those participants. The two are coupled but distinct architectural commitments.

## 2. The architectural specification, precisely stated

In the CKS pattern at Self-aspect scope, the Self operates over its constituent aspects through the following operational specification.

**(a) The Self asks pattern questions across constituent aspects.** The mechanism by which the Self reasons over its aspects is pattern questions — questions whose form is specified by orchestration rules and whose execution produces Self-level outputs. Pattern questions are substrate operations in the sense of A2.04 + A2.46: authored as rules, executed as substrate-mediated operations, with results that are themselves substrate content.

**(b) Pattern questions run through Paper 1's three composition patterns.** Three patterns from A1.16 — operationalized in A2.92–A2.94, with sharpening properties at A4.27–A4.29 — apply at Self-aspect scope.

- *Pattern A — consultation* (A2.92, A4.27). The Self consults specific aspects with specific questions and integrates the responses for a Self-level decision. Example: a Self consults a patient-assessment aspect ("what is the assessment") and a billing aspect ("what is the billing status"), then integrates both into a Self-level decision. Aspects are not commanded; they answer the questions they are configured to answer, and the Self reasons over their answers.
- *Pattern B — derived view* (A2.93, A4.28). The Self derives a view over multiple aspect outputs — an integrated narrative, a unified picture, a synthesis — without consulting aspects question-by-question. Example: a Self builds an integrated case narrative from substrate content already produced by aspects in their normal operation.
- *Pattern C — separate concerns* (A2.94, A4.29). The Self performs Self-level reasoning that operates over substrate content but does not consult aspects directly. Example: a Self reasons about its own configuration or substrate-level matters that do not require aspect input.

Pattern selection is per Self-question pair: the same Self may use Pattern A for one question, Pattern B for another, and Pattern C for a third, depending on what the question requires.

**(c) Aspects preserve aspect-level autonomy.** Whether or not the Self asks pattern questions, aspects continue aspect-level work. The Self's reasoning over aspect content does not block aspect operations, modify aspect internals, or commandeer aspect schedules. Aspects participate in the Self's reasoning by being available to be reasoned over, not by being directed.

**(d) Authority allocation respects level scope.** Aspect substrate is authoritative for aspect content per A1.08 at aspect scope. The Self reads aspect content but does not become authoritative for it. Self substrate is authoritative for Self-level outputs — the integrations, derived views, and Self-level reasoning results that pattern questions produce.

**(e) Self-level outputs are substrate-resident.** Pattern questions produce outputs serving the integrated Self's reasoning. These outputs reside in the Self's substrate per A2.46. They are first-class architectural artifacts subject to the same inspection, modification, and override authority as any other substrate content under Paper 1's authority architecture.

**(f) Questions and outputs are recorded with scope-distinguishing provenance.** Per A2.40, every pattern question and every Self-level output carries provenance metadata that distinguishes Self-level from aspect-level operations. Path retraceability per A1.07 holds across the level boundary: a Self-level decision can be traced through the pattern question to the aspect content it consulted, and from there into the aspect-level operations that produced that content.

**(g) Recursion of content-domain across levels.** The same architectural pattern operates at aspect-cell scope (B2.17) and at Self-aspect scope (B2.22). Aspect outputs may be content-domain for Self recursively per B1.18: when an aspect's substrate output is itself the input to a Self-level pattern question, the aspect-level and Self-level content-domain operations compose without requiring a third architectural mechanism.

These seven components are jointly necessary to instantiate the Self-aspect content-domain operationalization at the architectural layer.

## 3. What makes the Self-aspect content-domain operationalization architecturally distinctive

Conventional AI systems that integrate multiple specialized subsystems — multi-agent frameworks, hierarchical task planners, top-level orchestrators with subordinate workers — frequently rely on command-flow from the integrator down to the subsystems. The integrator decides what each subsystem should do; the subsystems do what they are told. The pattern is recognizable and operationally sufficient for many tasks; it is also distinct from what CKS commits to at the Self-aspect boundary.

Three architectural distinctions follow. *Reasoning over content, not command-flow.* The Self does not direct aspects; it reasons over their content. A Self-level question that would, in a command-flow architecture, be issued as an instruction to a subsystem is, in CKS, a pattern question whose answer is substrate content the Self reads. *Aspect-level Paper 1 commitments preserved at Self scope.* Because aspects are not commanded, the architectural commitments Paper 1 defends at aspect scope continue to hold even as aspects participate in Selves. A Self that issued commands would, in effect, override those commitments at the aspect boundary; the content-domain relationship preserves them. *Recursion as architectural feature rather than special case.* Because content-domain is the same architectural pattern at every level boundary, the multi-level reasoning that emerges from composing aspect-cell and Self-aspect operations is not separately engineered; it is what the architecture produces when the same pattern is instantiated at adjacent scopes.

## 4. The cognitive analog as conceptual scaffold

The Self-aspect content-domain relationship has an intuitive parallel in human integrated personhood reasoning over modes of engagement. When a person asks "what is my overall assessment of this situation," the integration operates over modes — cognitive, emotional, embodied — as content domain rather than commanding the modes. The cognitive mode does not stop processing because the integrated self is asking; the emotional mode continues its work; the embodied mode keeps its background activity. The integrated reasoning produces a Self-level understanding by reading across the modes' contributions.

The analog functions as conceptual scaffold readers absorb quickly because the parallel is intuitive. The architectural substance is not the analogy; it is reasoning over aspect content while preserving aspect autonomy, instantiated through Paper 1's composition patterns and recorded with scope-distinguishing provenance.

## 5. Inherited Paper 1 commitments at Self-aspect scope

The operationalization satisfies inherited Paper 1 commitments without requiring new defensive ground. **A1.13 composition requirements** are satisfied at Self-aspect scope: per-substrate human governance is preserved; conflicts between aspect outputs are preserved as first-class substrate content; provenance is addressable across the boundary; AI-as-mediator operates at every layer; humans remain selectively in composition. **A1.16 hybrid systems composition** applies through Patterns A, B, and C with their A4.27–A4.29 sharpening properties; **A2.92–A2.94** operationalize the patterns at Self-aspect scope without modification. **A1.02 substrate-cell boundary** is preserved at the Self-aspect boundary: Self operations on aspect content respect the aspect's substrate boundary; the Self does not write through the boundary into aspect internals. **A1.08 substrate-as-source-of-truth** holds at each scope: aspect substrate is authoritative for aspect content; Self substrate is authoritative for Self-level outputs. **A2.04 rule authoring** governs the pattern question rules — what the Self asks, of which aspects, through which pattern, are human-authored substrate content. **A2.40 provenance** records the operations with scope-distinguishing metadata. **A1.07 path retraceability** holds across the level boundary. No new architectural commitment is introduced at Self-aspect scope; the note formalizes the operational form of inherited commitments at the highest level boundary the source paper names.

## 6. Operational implications

Six implications follow. *Pattern question rules are configured per Self purpose:* different Self-level reasoning needs require different pattern questions, configured under A2.04; there is a configuration surface, not a canonical question set. *Pattern question rules evolve through directed selection (B1.14) and action-feedback (B1.15):* rules are themselves substrate content that evolves under governance, so the Self's pattern-question repertoire changes over time. *Pattern selection is per Self-question pair:* Patterns A, B, and C are properties of the Self–question pair, not of the Self; the same Self may use different patterns for different questions, and the same question may be answered through different patterns under different rules. *Self operations are concurrent with aspect operations:* because aspects are not blocked by Self pattern questions, Self-level reasoning runs concurrently with aspect-level work; the architecture does not require synchronization at the level boundary, only that the substrate accesses each operation performs are well-formed. *The relationship is testable:* the hybrid systems composition operational test (A5.16) applies at Self-aspect scope — a deployment can be inspected and replayed to confirm that pattern questions run through admissible patterns, that aspect autonomy is preserved, and that provenance distinguishes scope. *Cross-level access per B1.19 coexists:* when the Self accesses cells directly per B1.19 — bypassing the aspect level — the Self-aspect content-domain relationship is bypassed for that operation; typical operations use content-domain, specific purposes that warrant cross-level access use B1.19, and both are governed.

A seventh implication concerns deployment visibility: Self-level outputs may be the externally visible behavior of the deployment. When a Self-level output is what the deployment produces — a clinical decision summary, a case ruling, an integrated recommendation — the operationalization specified here is what makes that output an architectural artifact rather than an emergent property of subsystem composition.

## 7. Limits

Stating what the Self-aspect content-domain operationalization does *not* commit to is what keeps the framing within Paper 2's specification.

It does **not** command aspects (the Self reasons over aspect content, does not direct aspect work). It does **not** bypass A1.02 (Self operations respect the aspect's substrate-cell boundary; no through-boundary writes). It does **not** make the Self authoritative for aspect content (A1.08 holds at each scope). It does **not** block aspect operations (aspects continue concurrently with Self pattern questions). It does **not** prescribe specific pattern questions (deployments configure questions per Self purpose; the architecture specifies how, not what). It does **not** eliminate aspect-level governance (aspects retain their Paper 1 commitments and their own governance). It is **not** one-directional only (feedback through human-mediated governance per A2.04 may flow from observed Self operations into aspect-rule changes; what the architecture rules out is direct Self-to-aspect command-flow, not human-mediated feedback loops). It does **not** eliminate level distinctions (Self, aspect, and cell remain architecturally distinct levels per B2.07; the content-domain relationship is the relation across the boundary, not the dissolution of the boundary).

A system that misreads the operationalization as licensing direct Self-to-aspect commands, as making the Self authoritative for aspect content, or as collapsing the level distinction, has departed from the specification regardless of how it describes itself.

## 8. Operational test (one-sentence form)

A deployment instantiates the Self-aspect content-domain operationalization if and only if, at all times, the Self operates over its constituent aspects through pattern questions whose execution runs through Paper 1's composition patterns A, B, or C; aspects continue aspect-level work autonomously and remain authoritative for aspect content per A1.08; Self-level outputs are substrate-resident in Self substrate per A2.46; and questions and outputs are recorded per A2.40 with provenance distinguishing Self-level operations from aspect-level operations.

A deployment that fails any clause may be a useful integrated AI system and may compose subsystems coherently in some other architecture; it does not instantiate the Self-aspect content-domain operationalization specified here.

## 9. Why naming the operationalization as standalone matters

This note is the third of five decompositions of the Self-as-integrated-whole architectural commitment within Phase B2:

- B2.20 — the Self as integrated whole (what the integrated whole is)
- B2.21 — the Self's integration architecture (how aspects participate in one Self)
- B2.22 — Self-aspect content-domain relationship operationalization (this note: how the integrated Self reasons over its aspects)
- B2.23 — Self-level instinct/reasoning configuration (how the instinct/reasoning separation manifests at Self scope)
- B2.24 — Self-level inheritance verification (how Paper 1 commitments are verified to hold at Self scope)

Together, the five decompositions specify what is required to instantiate Paper 2's Self at the operational layer. Subsequent Phase B2 notes after B2.24 decompose B1.06 (two layers within every cell) starting at B2.25 and continuing through B2.29 and beyond.

Naming the Self-aspect content-domain operationalization as standalone is what allows downstream implementations to specify their Self-level reasoning mechanism precisely — what pattern questions, of which aspects, through which patterns, with what provenance — without conflating the mechanism with integration architecture (B2.21), with command-flow patterns the architecture rules out, or with the abstract higher-as-content-domain commitment (B1.18) the operationalization realizes at this scope.

Subsequent work that adopts, extends, composes with, or argues against the Self-aspect content-domain operationalization should use the term in the sense formalized here. Subsequent work that uses it differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Self-Aspect Content-Domain Relationship Operationalization: Decomposing the Self as Integrated Whole at Self-Aspect Scope in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
