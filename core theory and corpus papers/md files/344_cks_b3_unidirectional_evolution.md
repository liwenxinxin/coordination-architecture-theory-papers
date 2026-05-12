# Unidirectional Evolution: The Anti-Pattern That Arises When Bidirectional Evolution per B1.16 Is Not Practiced

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Bidirectional evolution per B1.16 specifies that an AI Self governed by the Coordination Knowledge Substrate (CKS) pattern evolves on two axes — horizontal (within levels, across peer entities) and vertical (across levels, between cells, aspects, and the Self) — and that this evolution operates continuously on operational timescales under human governance, not only at the moment of deployment design. Unidirectional Evolution is the anti-pattern that arises when one or both of these axes is absent, or when evolution is confined to design time. The anti-pattern presents in three recognizable forms: Horizontal-Absent Evolution, in which improvements to one cell never propagate to peers; Vertical-Absent Evolution, in which cell-level improvements never inform aspect or Self architecture and Self-level changes never propagate downward; and Design-Time-Only Evolution, in which the deployment is evolved at the moment of design and then frozen until the next planned re-deployment window. Each form violates a distinct dimension of B1.16 and produces characteristic operational damage — siloed knowledge, architectural incoherence, and mounting misalignment with operational needs. This note formalizes the anti-pattern, its three forms, the conditions under which each emerges, its operational consequences, and the detection and remediation procedures that restore bidirectional governance.

---

## 1. Commitment Violated

**B1.16 — Bidirectional evolution: horizontal within-level and vertical cross-level, on operational timescales.**

B1.16 establishes that a governed AI Self does not merely evolve; it evolves on two distinct axes simultaneously. Horizontal evolution refines content within existing structure: cells improve their DNA, aspects refine their cell composition, Selves refine their aspect arrangement. Vertical evolution reorganizes structure itself: cells, aspects, and Selves gain or lose constituent members; relational roles reconfigure; the orchestration substrates defining composition — which are themselves substrate content humans govern — are edited. Because both axes operate on substrate content, both are available to human governance on the same timescales as any other substrate edit, not only at the special moments of system design or planned redeployment.

The commitment has three load-bearing properties. First, both axes must be present; architecture that evolves only within existing structure is not bidirectional, regardless of how actively it refines content. Second, both axes must be governed, not ungoverned drift; evolution that reorganizes structure without governance is structural instability, not bidirectional evolution. Third, governance must operate continuously on operational timescales, not only at design time; an architecture that evolves only when humans convene a redesign process is a waterfall architecture that happens to call its redesigns evolution.

B2.79 establishes the bidirectional frame that B1.16 names. B2.80 specifies horizontal evolution as the within-level refinement axis. B2.81 specifies vertical evolution as the cross-level reorganization axis. B2.82 specifies operational timescales as the governance readiness property that makes both axes continuously available. B2.83 provides the bidirectional evolution verification procedure that confirms both axes are configured and operational.

Unidirectional Evolution violates B1.16 by suppressing one or both axes, or by making governance available only at design time. The suppression may be partial — one form of the anti-pattern may be present without the others — but each form constitutes a violation of B1.16's requirements for that axis or that timescale.

---

## 2. Recognizable Forms

Unidirectional Evolution presents in three distinct forms. Each form is recognizable by characteristic architectural signals and each violates a distinct dimension of B1.16.

### Form 1 — Horizontal-Absent Evolution

In Horizontal-Absent Evolution, improvements made to one cell are never propagated to peer cells at the same level. Each cell evolves in isolation: when operators discover a better orchestration pattern for one cell, they implement it in that cell alone. When governance identifies a refinement to how a particular class of interactions is handled, the cell that handles that interaction class receives the update; peer cells serving similar operational domains do not. The deployment as a whole grows more capable, but the knowledge of *how* it grew more capable is siloed within the individual cell where the improvement originated.

The organizational learning benefit of horizontal evolution per B2.80 is absent. B2.80 specifies that horizontal evolution propagates content refinements across peer entities through governed directed selection per B1.14: governance reviews whether improvements in one cell should be offered to peers, makes the propagation decision, and executes the update through the standard authority architecture. Horizontal-Absent Evolution is the failure mode in which this review never occurs, not because governance has decided that propagation is inappropriate, but because governance has not established the workflow through which such a decision would be made and acted on.

Recognition signals for this form are characteristic and auditable. Peer cells with similar or overlapping operational domains have significantly divergent DNA despite serving comparable purposes — divergence that cannot be explained by intentional differentiation but reflects the independent evolution of isolated units. No horizontal propagation events per B2.80 are recorded in the substrate's provenance metadata. Governance review processes do not include a step for assessing whether cell improvements should propagate to peers. Deployment knowledge circulates informally among cell operators rather than through governed substrate-level propagation.

### Form 2 — Vertical-Absent Evolution

In Vertical-Absent Evolution, the horizontal axis may function — cells may improve and, in some deployments, peer improvements may propagate — but the vertical axis is absent. Cell-level improvements are never propagated upward to inform aspect-level DNA per B2.16 or Self-level DNA per B2.21. Self-level architecture changes, when they occur, are never propagated downward through the expression mechanism to inform how cells execute. The deployment evolves at cell level but the aspects and Self that coordinate and integrate those cells remain static.

This form has two sub-directions, and both can be absent or only one. Upward vertical evolution absent means that cell-level operational learning never reaches aspect and Self architecture. A cell may develop sophisticated orchestration patterns for handling a particular coordination challenge; those patterns, having demonstrated their value in operation, should inform how the aspect coordinating that cell is structured and how the Self integrates that aspect's outputs. When upward vertical evolution is absent, this informing never occurs. Aspects and Selves are designed once and maintained in that original configuration regardless of what cell-level operation has demonstrated.

Downward vertical evolution absent means that when governance does evolve Self-level architecture — adding or removing aspects, restructuring integration patterns — that structural change never propagates through the expression mechanism to inform how cells execute within the restructured architecture. Cells continue executing under orchestration patterns calibrated for the prior structure, introducing a growing mismatch between what the Self's architecture specifies and what cells actually do.

Recognition signals include: aspect DNA per B2.16 and Self DNA per B2.21 that have never been updated despite significant cell-level evolution over the deployment's operational lifetime; absence of vertical evolution events per B2.81 in governance records; authority distribution changes per A6.06 that should follow vertical restructuring being absent or unrecorded; and cell improvements accumulating in individual cells without corresponding substrate entries at aspect and Self levels identifying what architectural implications have been reviewed and decided.

### Form 3 — Design-Time-Only Evolution

Design-Time-Only Evolution is the form in which the deployment is evolved at deployment design time and then frozen until a planned re-deployment window. All evolution is front-loaded: the architects who design the deployment invest significant effort in configuring DNA, orchestration rules, and structural relationships. That investment produces an initial configuration that may be sophisticated and well-considered. Then the deployment is handed off to operations, and governance as an ongoing activity stops.

This form may present as a waterfall development discipline in which system design and operational management are organizationally separated: the architects who designed the deployment have no ongoing role in its governance, and the operations team has neither the authority nor the tooling to evolve the deployment's substrate content. It may also present as a continuous-operations model in which governance is nominally ongoing but in practice occurs only when a re-deployment event is scheduled — a quarterly review cycle, an annual architecture refresh, or a triggered redesign following significant operational failure.

B2.82 specifies operational timescale governance readiness as the property that makes both horizontal and vertical evolution continuously available: governance must be configured, staffed, and authorized to act on evolutionary signals as they emerge from operation, not only when a planned review window arrives. Design-Time-Only Evolution is the absence of this readiness. The deployment's operational outputs signal improvement opportunities continuously; governance is not in a position to act on those signals continuously.

Recognition signals include: no directed selection events per B1.14 occurring after initial deployment; no action-feedback cycle per B1.15 operating in connection with substrate evolution; governance review occurring only at planned re-deployment windows; and B2.82 operational timescale governance readiness being absent from deployment documentation because it was never configured.

---

## 3. Emergence Conditions

Two conditions, individually or in combination, generate Unidirectional Evolution.

**Waterfall development treating governance as a design-time activity.** The deployment is conceived, designed, and handed off under a project model in which the project ends at deployment. Governance — the ongoing exercise of human authority over substrate content and orchestration rules — is understood as design-time work performed by the architecture team, not as a continuous operational function. After handoff, the operational team maintains the deployment but does not govern its evolution. This condition generates Design-Time-Only Evolution directly, and generates Horizontal-Absent and Vertical-Absent Evolution indirectly because the governance workflows through which propagation decisions would be made are never established.

**Governance capacity limits preventing continuous evolutionary review.** Even in deployments whose architects understand bidirectional evolution as an architectural requirement, the governance team may lack the staffing, tooling, or process design to monitor evolutionary signals continuously and act on them. Peer improvement propagation requires an ongoing review workflow: someone must track which improvements have been made in which cells, evaluate each for propagation, make the propagation decision, and execute the update. Vertical evolution review requires an ongoing assessment of whether cell-level operational knowledge has implications for aspect and Self architecture. Neither workflow is costless, and both require governance capacity that is not always resourced when the deployment transitions from design to operation. When this capacity is absent, Horizontal-Absent and Vertical-Absent Evolution emerge even in organizations that nominally understand what bidirectional evolution requires.

---

## 4. Operational Consequences

**Incoherent architecture.** Without vertical evolution, cell-level improvements accumulate independently of the aspect and Self architecture that coordinates and integrates them. Over time, the three-level structure becomes architecturally incoherent: cells execute with sophistication developed through operational experience, while aspects and Selves coordinate using structural assumptions that predate that experience. The coordination context and the coordination content progressively misalign. Interventions at the aspect and Self level produce unexpected effects because the cells they coordinate have evolved beyond what those levels' architecture anticipates.

**Siloed knowledge.** Without horizontal evolution, each improvement to one cell must be independently rediscovered at peer cells. Two cells serving similar operational domains may each discover, through their respective operational experience, an effective orchestration pattern for a recurring coordination challenge — but do so independently, without the benefit of the other's discovery. Deployment knowledge is re-created rather than propagated. The cost of learning is multiplied by the number of cells that serve similar domains, while the quality of each cell's operation remains limited to what that cell's operators have individually discovered.

**Stale architecture.** Design-time-only evolution produces deployments whose architecture grows progressively misaligned with operational needs. The operational environment changes — the humans who use the deployment develop new coordination patterns, the problems the deployment encounters shift in character, the optimal orchestration configurations change — while the deployment's substrate content remains calibrated for the conditions that existed at design time. Governance is reactive: evolution occurs in response to accumulated pain at re-deployment windows, not continuously in response to emerging operational signals.

**Vertical evolution blocked at both directions.** Without governed vertical evolution pathways, the Self-level integration architecture cannot benefit from accumulated cell-level operational knowledge. The deployment's most operationally grounded learning — the knowledge that emerges from cells operating against real coordination challenges over time — cannot reach the level at which architectural integration decisions are made. Simultaneously, Self-level architectural decisions cannot propagate downward to inform how cells operate within the structures those decisions create. The three levels operate increasingly independently of each other, and the coherence that the three-level architecture is designed to provide is progressively lost.

---

## 5. Detection

**B2.83 bidirectional evolution verification.** The primary detection procedure is B2.83, which asks whether horizontal and vertical evolution governance workflows are configured. A deployment that cannot answer affirmatively to both questions — are there governance workflows for horizontal propagation decisions, and are there governance workflows for vertical evolution review? — has not established the infrastructure B1.16 requires. This test is binary at the configuration level and does not require observation of actual evolution events; the absence of configured workflows is the finding.

**Horizontal propagation audit.** For deployments in which horizontal evolution workflows are nominally present, the horizontal propagation audit examines whether those workflows produce outcomes. The audit examines the substrate's provenance metadata for horizontal propagation events: are there governance records of decisions to propagate a cell's improvement to peer cells? Are there cases in which propagation was reviewed and declined, with the decision recorded? A substrate with peer cells serving similar operational domains, significantly divergent DNA, and no propagation events in its governance record indicates Horizontal-Absent Evolution regardless of whether a propagation workflow nominally exists.

**Vertical evolution audit.** The vertical evolution audit examines whether aspect DNA per B2.16 and Self DNA per B2.21 have evolved in response to cell-level improvements. It asks: have there been vertical evolution events per B2.81 recorded in the governance history? Has the authority distribution per A6.06 been updated following any structural reorganization that vertical evolution should have triggered? A deployment with significant cell-level evolution and static aspect and Self architecture is exhibiting Vertical-Absent Evolution.

**B2.82 operational timescale governance readiness check.** The timescale check asks whether governance is configured to operate continuously rather than only at design time. The check examines whether governance processes are staffed and authorized for ongoing operation, whether the tooling that surfaces evolutionary signals (action-feedback cycle per B1.15, directed selection events per B1.14) is connected to governance review, and whether governance review cadence is event-triggered or only schedule-triggered. A deployment in which governance review occurs only at planned re-deployment windows fails this check regardless of how sophisticated its design-time governance was.

---

## 6. Remediation

Remediation addresses each form and its associated detection finding.

**Establish horizontal evolution governance workflows per B2.80.** Configure a governance review process, connected to directed selection per B1.14, that periodically examines whether improvements made to individual cells should be offered to peer cells serving similar operational domains. The review process need not propagate every improvement to every peer; its function is to make the propagation decision explicitly and record it. The record of that decision — propagate, propagate with modification, or decline with rationale — is the horizontal evolution event that the horizontal propagation audit checks for. Configure the workflow before operation begins, not after Horizontal-Absent Evolution has been diagnosed.

**Establish vertical evolution governance workflows per B2.81.** Configure a governance review process that examines whether cell-level operational improvements have implications for aspect and Self architecture, and whether Self-level architectural changes should propagate downward through the expression mechanism to inform cell execution. The vertical evolution workflow is distinct from the horizontal evolution workflow in its scope — it asks questions about structural relationships rather than content refinements — and in its authority requirements, which involve governance actors with authority over aspect and Self DNA per B2.21, not only over cell-level orchestration. Confirm that the authority architecture per A6.06 covers the governance actors needed for vertical evolution decisions.

**Configure operational-timescale governance capacity per B2.82.** Remediate Design-Time-Only Evolution by establishing governance as an ongoing operational function, not a design-time project activity. This requires staffing the governance function for continuous operation, connecting the action-feedback cycle per B1.15 and directed selection per B1.14 to governance review, and ensuring that governance authority is available to act on evolutionary signals as they emerge rather than at scheduled intervals. The organizational design of the governance function is outside the scope of B1.16's architectural requirements; B1.16 requires that the governance function exist and be ready to operate on operational timescales, not that it take any particular organizational form.

**Run B2.83 bidirectional evolution verification after configuration.** Once horizontal evolution governance workflows, vertical evolution governance workflows, and operational-timescale governance capacity are in place, run B2.83 verification to confirm that the infrastructure required for bidirectional evolution is fully configured. B2.83 is not a one-time check; it should be run periodically as part of ongoing governance health assessment, and its findings should be treated as governance findings requiring remediation, not as architectural diagnosis completed once.

---

## 7. Conclusion

Unidirectional Evolution is the anti-pattern that arises when a deployment governed under the CKS instinct/reasoning separation architecture fails to practice bidirectional evolution per B1.16. The anti-pattern presents in three forms, each suppressing a distinct dimension of what B1.16 requires: Horizontal-Absent Evolution suppresses peer improvement propagation within levels; Vertical-Absent Evolution suppresses cross-level propagation in both the upward (cell-to-aspect, aspect-to-Self) and downward (Self-to-cell) directions; and Design-Time-Only Evolution suppresses operational-timescale governance, confining evolution to the moment of deployment design.

The three forms are not mutually exclusive. A deployment may exhibit all three simultaneously — a common presentation in deployments built under waterfall development disciplines that never establish ongoing governance infrastructure. They are also not individually rare; the organizational and resourcing conditions that produce them are the default conditions for AI deployment in many enterprises, where AI projects are managed as implementation projects rather than as governed operational systems.

B1.16's requirement that evolution operate on both axes and on operational timescales is the architectural commitment that distinguishes a deployment capable of compounding improvement from one that improves only through periodic redesign. Bidirectional evolution is what allows the three-level structure to remain coherent over time, what allows deployment knowledge to propagate across peer cells rather than being re-discovered in each, and what allows the governance investment made in each cell's operational improvement to inform the architecture that coordinates and integrates it. Unidirectional Evolution forfeits these properties one axis and one timescale at a time.

---

## Source Papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Unidirectional Evolution: The Anti-Pattern That Arises When Bidirectional Evolution per B1.16 Is Not Practiced.* May 12, 2026. ORCID: 0009-0004-8065-3235.
