# Cell-Internal Architecture in the CKS Paper 2 Framework: Four Substrate-Resident Components Inside the Cell Boundary

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize **cell-internal architecture** as the substrate-resident architecture inside the cell boundary, comprising four components — DNA layer, Action layer, harness substrate, and processing logic — operating together under human governance, complementing the external interface treatment in B2.11.

## Abstract

Paper 1 specifies the cell as the atomic unit of the coordination pattern; Paper 2 develops what each cell is internally. This note formalizes a four-component architecture inside the cell: a DNA layer of stabilized orchestration and behavior substrates, an Action layer of recorded task instances, a harness substrate that determines which DNA elements activate for which inputs, and processing logic specified by orchestration rules. A separate note (B2.11) treats the cell at its external interfaces; this note treats the complementary internal architecture. The four components are layered, not flat; they are governed at every component; they are what makes Paper 2's evolution mechanisms (instinct evolution, DNA evolution, action-feedback evolution) operationally meaningful at cell level. The note states the four components precisely, names what makes the explicit-internal-architecture framing distinctive, traces inherited Paper 1 commitments through the architecture, lists operational implications, and bounds the framing against six adjacent misreadings.

## 1. Why cell-internal architecture needs to be formalized as standalone

Paper 1 introduces the cell as the atomic unit of the coordination pattern (§2.1, §4.1) and commits the substrate-cell boundary as the architectural separation between persistent state and bounded execution. Paper 2 extends the cell from atomic unit into composable structure — cells form aspects, aspects form Selves — and in doing so makes precise commitments about what is *inside* the cell. Paper 2's "Two layers within every cell" subsection commits each cell to a layered internal structure (DNA layer plus Action layer); the "Expression" subsection within Three Levels of Structure commits each cell to a harness substrate that determines DNA activation. Together with the orchestration-rule processing logic Paper 1 commits at §2.1 and §2.3, these commitments specify a four-component architecture inside the cell.

The cell-as-modular-unit treatment (B2.11) covers how cells interact with adjacencies — what crosses the cell boundary, what does not, how cells compose into aspects and Selves — and leaves cell internals deliberately opaque. That framing is correct for the composition layer but leaves a load-bearing class of architectural decisions unspecified, and several of Paper 2's central commitments — the evolution mechanisms in particular — operate *inside* the cell, on its internal components, and cannot be stated coherently without naming what those components are. The remedy is to formalize cell-internal architecture as a standalone derivation. Naming the four internal components explicitly is what makes Paper 2's evolution mechanisms operationally meaningful, makes cell-level governance describable component-by-component, and prevents the slide into implicit-internal-architecture framings in which cell internals exist in any concrete deployment but are not properties of the architecture.

## 2. The architectural specification

A cell's internal architecture comprises four substrate-resident components operating together, all on the substrate side of the substrate-cell boundary, all subject to the human-governance commitment, all carried as authoritative substrate content.

**(a) DNA layer.** The DNA layer holds the cell's stable behavioral specification — the harness logic, the conflict-handling rules, the lifecycle policies, the schemas, the orchestration substrates and behavior substrates that define how the cell processes inputs and what outputs it is authorized to produce. DNA layer content is substrate-resident authoritative content; humans inspect, modify, and override it, and author the orchestration rules that compose it. The DNA layer is what mating combines in the genetic sense, what evolution refactors through directed selection, and what action-feedback evolution refines on the basis of accumulated lived experience.

**(b) Action layer.** The Action layer accumulates recorded task instances — what tasks the cell performed, what inputs it processed, what outputs it produced, what consultations it made to the LLM mediator, what conflicts it preserved or resolved. Action layer content is substrate-resident with full provenance metadata: writer, timestamp, rationale, source, authority, decision context. The Action layer is what makes path retraceability operational at cell scope, and is the evidence base on which action-feedback evolution proposes DNA refinements.

**(c) Harness substrate.** Each cell carries a harness substrate that determines which DNA-layer elements activate for the current cell goal. The harness substrate operationalizes Paper 2's *expression* mechanism: cells may carry the full Self's DNA with selective expression (when lineage and reconstitution matter, such as in regulated work) or partial slices (when storage and cognitive load matter more). The harness substrate is itself substrate-resident, itself human-governed, and itself authoritative architecture content — the per-cell expression policy, made first-class.

**(d) Processing logic.** Processing logic is the orchestration-rule content that governs how the cell processes consultation inputs and Action-layer interactions. It operationalizes the AI-as-substrate-mediator commitment at cell scope: orchestration rules specify what the LLM mediator is authorized to do on the cell's behalf, what conflict-handling rules apply when the cell encounters a preserved conflict, what schemas the cell's outputs must conform to, and what routing rules send certain inputs to instinct (the LLM, external to the cell) and others to deliberate reasoning (cell-internal substrate processing). Processing logic is itself substrate-resident, itself authored under the rule-authoring commitment.

The four components are layered, not flat. The harness substrate determines which DNA-layer elements activate; the activated DNA specifies how the cell processes inputs; processing operates on consultation inputs and on Action-layer interactions; results are recorded back into the Action layer as new task instances with full provenance. The layering is what enables Paper 2's central distinction between *stabilized behavioral specification* (DNA) and *operational history* (Action) to do architectural work, and what makes each component independently governable while integrated operation produces cell behavior.

## 3. What makes the explicit-internal-architecture framing distinctive

Conventional AI components — agents, tools, microservices, plugin endpoints — have internal architecture in any concrete implementation, but the internal structure is typically implicit at the architectural layer: the component has processing logic, perhaps a configuration store, perhaps a memory of past interactions, but the layered substrate-resident decomposition is not a property of the architecture, only of the implementation. Two consequences follow. Governance attaches to the component as a whole, not to its internal layers; a human cannot exercise inspect, modify, or override authority over (say) "the configuration that determines which model is invoked for which input" as a distinct architectural object, because that configuration is not architecturally named. Evolution likewise attaches to the component as a whole; updating its behavior typically means redeploying the component, not refining its DNA layer while preserving its Action layer history.

The CKS Paper 2 framework's explicit-internal-architecture commitment is what makes the four components separately governable, separately evolvable, and separately inspectable. Modifications operate at component granularity: a directed-selection refinement to DNA does not perturb the Action layer; an Action-layer accumulation does not modify DNA except through the explicit, human-mediated action-feedback path. The layered structure is what enables Paper 2's evolution mechanisms — directed selection on DNA, routine accumulation on Action, action-feedback closing the loop from Action evidence back to DNA — to be stated as separate architectural mechanisms operating on separate architectural objects, rather than as overloaded operations on a monolithic component.

## 4. The biological analog as conceptual scaffold

Cell-internal architecture parallels biological cell internals in a loose, scaffolding sense. Biological cells have a nucleus that stores genetic content, cytoplasm in which active processing occurs, organelles specialized for specialized work, and signaling and regulatory mechanisms that determine which genes activate under which conditions. The CKS cell's four components map approximately: DNA layer to nucleus-stored genetic content; Action layer to cellular history that does not reside in the genome but accumulates from lived activity; harness substrate to the regulatory machinery that determines gene expression; processing logic to the metabolic and signaling routines that carry out the cell's day-to-day work. The analog is conceptual scaffold; it is not architectural substance. The architectural substance is substrate-resident layered architecture under human governance — a property of the engineered system, not a derivation from biology. Treating the analog as scaffold is what allows Paper 2's biological vocabulary (DNA, expression, cell, lineage, mating, death) to do conceptual work without committing the architecture to biological mechanisms it does not in fact instantiate.

## 5. Inherited Paper 1 commitments operationalized through the four components

Paper 2's recursive-commitment principle states that all Paper 1 commitments hold at the cell level. The four internal components are how those commitments operationalize at cell scope.

The substrate-cell boundary commitment defines what is inside the cell architecturally: all four components sit on the substrate side of the boundary, and the cell as bounded execution context operates *over* its internal substrate content rather than holding execution state outside it. The substrate-as-source-of-truth commitment holds at cell scope: DNA, Action, harness, and processing-logic content are all authoritative substrate state. The AI-as-substrate-mediator commitment is operationalized in processing logic, whose orchestration rules specify what the LLM mediator is authorized to do, when consultations occur, and how their results are written back to the Action layer. The rule-authoring commitment extends to all four components: DNA, harness, and processing-logic content are authored under human authority, and Action-layer content accumulates under that same authority through orchestration rules that determine what gets recorded and how. The path-retraceability commitment is operationalized through the Action layer, whose recorded task instances carry the provenance metadata that makes audit and traceability possible at cell scope. The human-governed commitment holds at every component: humans inspect each, modify each, and override each at any time during the cell's existence.

Cell-internal architecture is what makes the recursive Paper 1 commitments operationally meaningful at cell scope, rather than merely asserted at cell scope.

## 6. Operational implications

Six implications follow directly from the architectural specification.

**Internal architecture is designed per cell purpose.** Different cell types — a deliberative-reasoning cell, a pattern-recognition cell, a verification cell, a decision-rationale cell — have different DNA contents, different harness configurations, and different processing logics. The four-component framework is the architectural specification; per-purpose specialization is a deployment decision the framework supports without prescribing.

**DNA is configured during birth.** Paper 2's birth lifecycle operation populates a cell's initial DNA. Birth may be performed by humans directly or by LLMs operating under human direction; the architectural commitment is that the resulting DNA is human-governed regardless of which mode produced it.

**Harness is configured per deployment context.** Whether the cell carries the full Self's DNA with selective expression, or only a partial slice, is a per-deployment design choice the harness substrate encodes. The architecture supports both choices and makes the encoding inspectable.

**Action accumulates operationally.** Action layer content grows as the cell processes tasks, bounded by the cell's scope and by orchestration rules that govern what gets recorded; it is not unbounded mere accumulation.

**Cell internals evolve through Paper 2's evolution mechanisms.** Directed selection refines DNA on the basis of human design decisions and outcome evaluations. Routine accumulation populates the Action layer. Action-feedback evolution closes the loop by proposing DNA changes from Action evidence under human mediation — the cell-level mechanism by which the Self learns from its own operation rather than only from external upgrades or human design decisions. Instinct evolution sits external to the cell and is integrated through governed responses, not by direct internal modification of any cell.

**Cell internals are inspectable at multiple granularities.** Inspection at component granularity supports oversight roles that need to verify specific properties of the cell without inspecting all of its internals. Cross-partner internal inspection along the multi-human axis introduced in Paper 1's Claim 6 may be scoped narrower than within-organization inspection on the basis of authority distribution; the architecture supports both.

## 7. Limits

Six adjacent misreadings should be named so the framing does not over-claim.

**Cell-internal architecture does not eliminate external interfaces.** Internal and external are complementary; B2.12 and B2.11 together specify the cell. A cell's external behavior is determined by its internal architecture *and* its boundary conventions; treating either alone produces a partial specification.

**Cell-internal architecture is not a single component.** Conflating the four components into a unitary "cell internals" object discards the architectural content the layering provides. Treating them as a single black box reverses Paper 2's central architectural move.

**Cell-internal architecture does not prescribe specific implementation technologies.** The tool-agnosticism commitment holds for cell internals as for the substrate generally: any environment supporting persistent structured state, human read/write access, and LLM access to substrate content can host the four components. The four components are the architectural specification, not the implementation specification.

**Cell-internal architecture does not eliminate the need for cell-level governance.** Each component is governed; governance is exercised at every component, not at the cell as a whole. A cell that hides its DNA from inspection while exposing its Action layer is not internally governed at full architectural scope.

**Cell-internal architecture does not prevent multiple cell types.** Different cell types may have different internal specializations — different DNA sizes, different harness policies, different processing logics. The four-component framework is what every cell instantiates; per-type specializations are what differentiates cells within that framework.

**Cell-internal architecture does not include the LLM.** The LLM is the instinct layer, external to the cell. The cell consults the LLM through the AI-as-substrate-mediator adjacency. This boundary — cell internals on one side, LLM on the other — is what makes the instinct/reasoning separation operational at cell level.

## 8. Operational test

A cell's internal architecture conforms to the CKS Paper 2 framework if and only if all of the following are true at all times during the cell's existence:

1. The cell carries a DNA layer of stabilized orchestration and behavior substrates, substrate-resident, inspectable, modifiable, and overridable by humans with appropriate authority.
2. The cell carries an Action layer of recorded task instances with full provenance metadata, substrate-resident, inspectable.
3. The cell carries a harness substrate that determines which DNA-layer elements activate for current activity, substrate-resident, inspectable, modifiable, and overridable.
4. The cell's processing is governed by orchestration-rule content (processing logic), substrate-resident, authored under human authority.
5. The four components are independently inspectable and independently governable; modifications to one do not implicitly modify the others.
6. No part of the cell's behavioral specification, recorded history, expression policy, or processing logic is held outside the substrate — not in LLM context, not in vendor-specific runtime state, not in any storage humans cannot inspect through the substrate.
7. The LLM is consulted as the external instinct layer through the substrate-mediator adjacency, not held inside the cell as an internal component.

A cell that fails any of (1)–(7) does not instantiate the framework's cell-internal architecture commitment, regardless of how well it satisfies external interface conventions in other respects.

## 9. Why naming as standalone matters

This note is the second of four decompositions of the cell-as-atomic-unit foundation. B2.11 treats the cell as modular unit at its external interfaces; this note treats the complementary internal architecture; B2.13 will treat cell-to-cell relationships within aspects; B2.14 will treat cell-level inheritance verification — the operational test that all Paper 1 commitments do, in fact, hold at cell scope through the four-component architecture. Together these four decompositions specify the cell as Paper 2's framework requires. Subsequent Phase B2 notes will turn to aspect-level decomposition, where the same internal-vs-external pattern recurs at the higher structural level.

Naming cell-internal architecture as standalone — rather than collapsing it into the broader cell concept or into the cell-as-modular-unit treatment — is what makes Paper 2's evolution mechanisms describable at component granularity, makes governance describable component-by-component, and makes inspection describable at the right resolution for oversight roles that need to verify specific properties of cells without inspecting every aspect of them. Subsequent work that adopts, extends, or argues against the CKS Paper 2 cell-internal architecture should use the four-component decomposition in the sense formalized here. Subsequent work that uses a different decomposition, or that treats cell internals as monolithic, is using a different architectural object, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cell-Internal Architecture in the CKS Paper 2 Framework: Four Substrate-Resident Components Inside the Cell Boundary.* May 8, 2026. ORCID: 0009-0004-8065-3235.
