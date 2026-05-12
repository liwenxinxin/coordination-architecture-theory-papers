# Expression Evolution Operational Treatment: Governed Refinement of Harness Substrate, DNA Activation Patterns, and Carry-Strategy in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the operational treatment of expression evolution — how the harness substrate (per B2.30), DNA activation patterns (per B2.31), and carry-strategy (per B2.32) evolve through Paper 2's governed evolution mechanisms — so that downstream work can adopt or argue against the treatment without ambiguity.

## Abstract

Paper 2 commits expression to be a governable architectural mechanism: every cell carries a harness substrate that is itself human-governed and that determines DNA-layer activation. Three prior derivation notes specify the harness substrate (B2.30), the DNA activation patterns it realizes (B2.31), and the carry-strategy it implements (B2.32). What those three notes do not yet pin down is how each of those substrate-resident components evolves once a deployment is operating. This note formalizes expression evolution as governed operational mechanism: directed selection per B1.14 is the primary mechanism, action-feedback per B1.15 is the secondary mechanism with human mediation, and mutation per B1.13 does not directly apply because mutation is the LLM-instinct-layer mechanism external to the cell. The note enumerates the categories of expression evolution that arise (harness rule evolution, pattern evolution, carry-strategy migration, context-awareness evolution, aspect-activation evolution), specifies how evolution events are recorded under A2.40 and how A6.02 retroactivity preserves historical expression rules, and provides a one-sentence operational test for the treatment.

## 1. Why expression evolution operational treatment needs to be formalized as standalone

Paper 2 names expression as a governable mechanism within *Three levels of structure*: every cell carries a harness substrate, itself human-governed, that selects which DNA-layer sub-substrates are active for current activity. Paper 2 also commits to three evolution mechanisms — directed selection, undirected mutation, and action-feedback evolution — each governed in a different shape. The two commitments are stated in adjacent sections of the source paper, but Paper 2 does not stop to articulate operationally how the harness substrate, the activation patterns, and the carry-strategy evolve once a deployment is running, which evolution mechanisms apply at the expression layer specifically, and how governance is exercised over each evolution event.

Three classes of failure follow when implementers fill the gap on their own. First, deployments may treat expression as fixed at cell birth — a design-time configuration that no mechanism updates afterward. This forfeits the operational improvement that should accumulate as understanding of the deployment matures and as scope changes. Second, deployments may evolve expression informally through ad-hoc edits to harness substrates outside any governance discipline. This forfeits the inheritance from Paper 1's authority architecture, A2.04 rule authoring, and A2.40 provenance recording. Third, deployments may conflate expression evolution with DNA evolution — treating any change to how cells behave as a DNA edit. This collapses two architecturally distinct evolution targets: DNA evolution changes specifications themselves; expression evolution changes how specifications activate.

The remedy is to formalize expression evolution as a governed operational mechanism with explicit operational content, distinct from DNA evolution and from instinct mutation, and to enumerate the categories of expression-layer change that the mechanism handles. This note does that. The strategic posture is defensive publication of public prior art: the more explicitly the operational treatment of expression evolution is recorded as derived from Paper 2, the smaller the territory in which any party could later claim novel invention of an expression-rule-evolution mechanism, a carry-strategy-migration mechanism, an aspect-activation refinement mechanism, or a context-awareness evolution mechanism, without bumping into this prior-art chain.

This is the thirty-third note in Phase B2 and the fourth of five notes decomposing B1.07 (expression mechanism). It follows B2.30 (harness substrate), B2.31 (activation patterns), and B2.32 (carry-strategy). The next note, B2.34, will close the B1.07 decomposition by formalizing expression mechanism inheritance verification. Phase B2 then continues with B1.08 modularity decomposition (B2.35 onward).

## 2. The architectural specification, precisely stated

In the CKS pattern as extended by Paper 2, **expression evolution** is the governed operational mechanism by which the harness substrate (B2.30), the DNA activation patterns it realizes (B2.31), and the carry-strategy it implements (B2.32) are refined over a deployment's lifecycle, under governance inherited from Paper 1 and through the evolution mechanisms specified by Paper 2. The treatment has four operational components.

**(a) Mechanism scope.** Expression evolution operates through two of Paper 2's three evolution mechanisms. **Directed selection** per B1.14 is the **primary** mechanism: humans deliberately modify harness rules, activation patterns, and carry-strategy configurations to refine expression behavior, operating through Paper 1's authority architecture by authoring rule changes per A2.04. **Action-feedback evolution** per B1.15 is the **secondary** mechanism, with human mediation: substrates that propose expression refinements examine Action-layer evidence and produce candidate changes, but the proposed changes do not take effect until a human approves them. **Mutation** per B1.13 does **not** directly apply to expression evolution. Mutation is the mechanism for the instinct layer — LLM upgrades, substrate-platform infrastructure upgrades — which is external to the cell. LLM-behavior changes through mutation may indirectly affect cell processing, but expression specifications themselves are within the reasoning layer, where mutation is not the operative mechanism.

**(b) Evolution categories.** Five categories of expression-layer change arise operationally, illustrative rather than exhaustive. **Harness rule evolution** refines specific activation rules under A2.04. **Pattern evolution** adds new activation patterns per B2.31 or modifies existing ones (for example, introducing a context-conditioned activation rule where previously only input-conditioned activation was used). **Carry-strategy migration** per B2.32 transitions a cell from one strategy to another through a governed multi-step process — operationally significant because cells may need DNA reorganization, harness restructuring, and governance adjustment together. **Context-awareness evolution** refines context conditions, adds new context types, and removes obsolete contexts as the deployment's understanding matures. **Aspect-activation evolution** per B1.17 refines aspect-specific activation as multi-aspect participation patterns mature.

**(c) Recording and retroactivity.** All expression evolution events are recorded per A2.40's six-field provenance metadata: what changed, when, by whom, under what rule, with what rationale, in what version. Historical expression rules are preserved per A6.02 retroactivity — pre-evolution expression behavior remains addressable, replayable, and auditable, even after the rules that produced it have been superseded.

**(d) Governance timing.** Directed selection is **event-triggered** by human decision: a human determines that an expression refinement is warranted and authors the change. Action-feedback evolution is **evidence-triggered** by accumulated operational signal: the proposing substrate produces a candidate refinement when Action-layer evidence meets the substrate's surface conditions, and the candidate then enters the human-mediated approval path. Both are governed events with full provenance; neither is automatic substrate modification.

The four components together define what expression evolution operationally consists of. A deployment that satisfies these components without satisfying Paper 1's commitments is not CKS-coherent on the expression-evolution axis; a deployment that satisfies Paper 1's commitments but treats expression as static does not realize Paper 2's expression mechanism as the governable architectural property the source paper commits to.

## 3. What makes the operational treatment architecturally distinctive

Conventional AI architectures treat expression as a configuration rather than as an evolvable layer. A model is configured for a task; the configuration may change between deployments, but within a deployment the components do what they were configured to do until the system is reconfigured or replaced. There is no architectural mechanism within the running system for expression behavior to evolve under governance — expression refinement is a redeployment cost, not an operational property. The governance shape is correspondingly external: expression decisions live in the deployment artifact, not in inspectable substrate state.

The CKS pattern as extended by Paper 2 makes expression evolution a governable architectural mechanism within the running system. Expression specifications are substrate-resident authoritative content (per A2.46 inside the A1.02 boundary), authored under A2.04, modifiable and overridable at any time per A2.01–A2.03, and recorded with full provenance per A2.40. The mechanisms by which expression specifications evolve — directed selection and action-feedback — are themselves Paper 2 commitments, governed in the shapes Paper 2 specifies. As deployments mature and operational evidence accumulates, expression behavior improves through governed evolution rather than through reconfiguration cycles or runtime drift.

The biological analog is loose. Biology has expression evolution in the cellular sense — gene regulatory networks change over evolutionary timescales through epigenetic modification, developmental plasticity refines expression patterns over an organism's life. But biological expression evolution is autonomous, with no governance over which regulatory changes happen, and biological timescales are very different from operational ones. CKS exceeds biology at exactly the points where biology cannot reach: human-governed selection over expression changes, operational-timescale refinement, and substrate-resident specification of evolution events with full provenance. The biology mimicry functions as conceptual scaffold; the architectural substance is governed evolution of substrate-resident expression specifications.

## 4. The cognitive analog as conceptual scaffold

A second analog is cognitive. Over time, humans refine their modes of engagement: the contexts that trigger different modes shift, the behaviors associated with each mode mature, the boundary cases that route to deliberate reasoning rather than automatic response are revised as experience accumulates. The cognitive analog is closer to operational timescale than the biological analog and parallels the categories enumerated in §2(b).

The architectural substance is still governed evolution of substrate-resident specifications. A CKS-coherent expression evolution treatment differs from cognitive learning specifically in being inspectable, in being modifiable by humans other than the cell, in being recorded with full provenance, and in inheriting the at-any-time temporal property from Paper 1's human-governed commitment. None of those properties hold for individual cognitive learning in the human sense.

## 5. Inherited Paper 1 commitments

Expression evolution inherits the full set of Paper 1 commitments without modification.

The **human-governed commitment** holds: humans retain the right to inspect any expression rule (A2.01), modify any expression rule (A2.02), and override any LLM-proposed expression change (A2.03), at any time during the deployment's existence. **Rule authoring** per A2.04 holds: expression-rule changes are authored by humans (LLM-drafted candidates subject to human authority before they take effect are admissible; LLM-committed changes outside human authority are not). **Provenance** per A2.40 holds: every expression evolution event is recorded with the six-field metadata. **Retroactivity** per A6.02 holds: historical expression rules are preserved, addressable, and replayable. **Path retraceability** per A1.07 holds across evolution events: a cell's expression state at any point in its history is reconstructable from substrate state plus the recorded evolution sequence. **Determinism** per A1.10 holds at the coordination layer: given current expression specifications and inputs, expression behavior is deterministic in the sense Paper 1 specifies.

For deployments that span composition partners, **authority distribution** per A2.47 holds: cross-partner expression-rule changes are authored under the authority distribution the composition specifies, and conflicts during composition are handled per A6.12 multi-author rule-authoring conflict treatment. None of these commitments are weakened by the operational treatment; the treatment is what allows them to apply to expression-layer change specifically, rather than only to DNA-layer or substrate-content change.

## 6. Operational implications

Six implications follow from the treatment. **Deployments configure expression evolution per requirements** — which expression elements may evolve, who may author evolution, what verification is required, and how often action-feedback proposals are surfaced are deployment configuration decisions. **Expression evolution is operationally distinct from DNA evolution per B1.14** — DNA evolution changes specification content; expression evolution changes how specifications activate, and most operational expression refinement should not require DNA edits. **Deployments will have many expression evolution events over a lifecycle**, often at fine grain (a single rule, one context condition, one aspect-activation pattern). **High-stakes deployments may impose stricter expression-evolution governance** — tighter authoring authority, mandatory verification, multi-party approval, or pinning of certain rules against modification — as governance configurations layered over the operational treatment, not departures from it. **Vertical evolution per B1.16 may require expression migration**: when structural reorganization changes how cells participate in aspects, the activation rules conditioning on aspect membership often require refinement, triggering an expression-evolution event. **Expression-evolution determinism is testable per A5.16**: reproducibility verification confirms that expression behavior under a given specification version is deterministic, and tests against superseded versions remain reproducible against the substrate's preserved historical state per A6.02.

## 7. What expression evolution operational treatment is NOT

The treatment is bounded by what Paper 2 commits to. **It does not include mutation** (per B1.13) — that is the instinct-layer mechanism, operating outside the cell. **It does not eliminate the need for verification** — expression-rule changes may trigger inheritance verification per B2.34 to confirm Paper 1 commitments still hold. **It does not bypass governance** — all expression evolution is governed per A1.01, and a treatment that allowed expression to evolve outside Paper 1's authority architecture would not be CKS-coherent regardless of operational utility. **It does not prescribe specific evolution patterns** — the treatment specifies the mechanism's content and the inherited commitments, not which deployment configurations are correct. **It does not eliminate cell-level governance** — expression-evolution governance is a layer of cell-level governance, not a replacement for it. **It is not evolutionary biology in the literal sense** — the biological analog is conceptual scaffold; the architectural substance is governed substrate evolution under human authority. **It does not modify DNA content directly** — DNA evolution per B1.14 modifies DNA content; expression evolution modifies how DNA content activates.

## 8. Operational test

A system implements the expression evolution operational treatment if and only if all of the following are true at all times during the deployment's existence:

1. Expression-rule changes (harness rules, activation patterns, carry-strategy configuration, context conditions, aspect-activation rules) are authored under A2.04 by humans with appropriate authority, with the change taking effect as substrate state.
2. Action-feedback proposals affecting expression specifications do not take effect without explicit human approval.
3. Mutation events (LLM upgrades, substrate-platform changes) do not modify expression specifications directly.
4. Each expression evolution event is recorded with the A2.40 six-field provenance metadata at the time the change takes effect.
5. Historical expression rules superseded by evolution remain addressable, inspectable, and replayable per A6.02 retroactivity.
6. No LLM operation, vendor policy, or runtime middleware can in principle prevent (1)–(5) for authorized humans.

A system that fails any of (1)–(6) does not implement the operational treatment, even if it satisfies Paper 1's broader commitments and other Paper 2 commitments in some respect.

## 9. Conclusion

Treating expression as static after birth forfeits the architectural property Paper 2 commits to: a substrate-resident, human-governed expression mechanism that improves over a deployment's lifecycle through governed refinement. Treating expression evolution informally — as ad-hoc edits outside the authority architecture — forfeits the inheritance from Paper 1 that makes the change auditable, reproducible, and reversible. Conflating expression evolution with DNA evolution collapses two architecturally distinct targets into one and obscures which mechanism applies.

Naming expression evolution as a standalone operational treatment gives downstream implementers a precise specification of which evolution mechanisms apply (directed selection primary, action-feedback secondary with mediation, mutation does not apply), which categories of change the mechanism handles (harness rule, pattern, carry-strategy migration, context-awareness, aspect-activation), and which Paper 1 commitments are inherited. It is the fourth of five decomposition notes for B1.07: B2.30 specifies the harness substrate, B2.31 specifies the activation patterns it realizes, B2.32 specifies the carry-strategy it implements, this note specifies how all three evolve, and B2.34 will verify that Paper 1 commitments hold across the decomposition. Phase B2 then continues with B1.08 modularity decomposition.

Subsequent work that implements, extends, or argues against the CKS expression evolution treatment should use the term in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Expression Evolution Operational Treatment: Governed Refinement of Harness Substrate, DNA Activation Patterns, and Carry-Strategy in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
