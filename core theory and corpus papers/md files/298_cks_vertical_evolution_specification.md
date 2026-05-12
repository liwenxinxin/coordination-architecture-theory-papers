# Vertical Evolution Specification: Decomposing B1.16 Bidirectional Evolution by Formalizing Cross-Level Evolution in Both Upward Direction (Cell Improvements Informing Aspect Evolution, Aspect Improvements Informing Self Evolution) and Downward Direction (Self DNA Changes Affecting Cell Behavior Through Expression Mechanism per B2.30), With Level-Boundary Governance per A6.06

**Derivation Note B2.81 — Phase B2, Series B**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Paper 2's bidirectional evolution commitment (B1.16) encompasses two orthogonal axes: horizontal evolution that refines content within existing structural levels, and vertical evolution that propagates change across levels. This note formalizes vertical evolution as the cross-level propagation specification. Vertical evolution operates in both directions: upward, carrying improvements from lower levels to higher levels (cell-level DNA improvements informing aspect coordination rule evolution, aspect-level improvements informing Self integration architecture evolution); and downward, carrying changes from higher levels to lower levels (Self DNA changes affecting aspect operation, Self DNA changes reaching cell behavior through the expression mechanism per B2.30, aspect coordination rule changes affecting cell participation patterns). Crossing any level boundary in either direction requires governance at both the origin level and the destination level — not governance at origin alone. The authority distribution change boundary per A6.06 applies when vertical evolution changes which humans hold authority over which architectural components. Vertical evolution may trigger birth events per B1.09; all such births follow the full birth governance framework. This is the eighty-first Phase B2 note and the third of five notes decomposing B1.16 (B2.79, B2.80, B2.81, B2.82, B2.83).

---

## 1. Why vertical-evolution-specification needs standalone formalization

B2.79 established the integrating frame for bidirectional evolution: that B1.16 governs two distinct axes, and that treating them as a unified blob produces underspecification of each. B2.80 formalized horizontal evolution — the within-level axis — precisely enough to serve as prior art against claims to the within-level refinement pattern. This note addresses the cross-level axis.

Vertical evolution is architecturally distinct from horizontal evolution in a way that demands separate formalization. Horizontal evolution leaves the structural arrangement intact and refines content within it; vertical evolution crosses the arrangement itself. An aspect-level coordination rule update triggered by cell-level improvement is not a cell-level event extending upward — it is a level-crossing event that requires governance at the destination level, not only at the origin. A Self-level DNA change that reaches cell behavior through the expression mechanism is not a Self-level event that happens to affect cells — it is a governed propagation through a specific architectural path, requiring governance at the Self level before propagation and operating through the expression mechanism as the architectural vehicle, not through implicit configuration.

The defensive-publication purpose of this note is specific. Three sub-patterns of vertical evolution each represent independently patentable derivations: the upward propagation path with level-boundary governance at each crossing; the downward propagation path through the expression mechanism as governed vehicle; and the A6.06 authority distribution change boundary as the operationally complex case that arises when vertical evolution changes which humans hold authority over which components. Formalizing all three in a single note, as the eighty-first in Phase B2, places them in the prior-art record under the series author's name before any party can claim novel invention over any of them.

The load-bearing source is Paper 2's dual-axis evolution section, which specifies that vertical evolution "reorganizes structure itself" — cells split or merge, aspects gain or lose constituent cells, Selves gain or lose aspects, relational roles reconfigure — and that the substrate-content commitment is what makes vertical evolution architecturally available, because structural reorganization is a substrate-edit operation rather than a developmental-program rewrite.

---

## 2. The architectural specification

### 2.1 Upward vertical evolution

Upward vertical evolution carries improvements from lower structural levels to higher structural levels. Two crossing paths are specified.

**Cell-to-aspect upward.** When cell-level DNA improvements substantially change how a cell processes inputs, produces outputs, or handles its internal lifecycle, the improvements may warrant review at the aspect level. Aspect coordination rules per B2.16 include membership rules (which cells participate in the aspect), invocation rules (how cells are called), and output-integration rules (how cell outputs are assembled into aspect-level results). If a cell substantially improves its output schema, existing aspect-level output-integration rules may no longer fit the improved output. If a cell substantially changes its input-processing logic, existing invocation rules may require updating. If a cell's improved behavior changes the conditions under which its participation adds value to the aspect, membership rules may need revision. Governance at the aspect level reviews cell improvements and determines whether aspect-level changes are warranted. The cell-level governance that authorized the cell's DNA change is origin governance; the aspect-level governance that determines whether coordination rules require updating is destination governance. Both are required before aspect-level changes are made.

**Aspect-to-Self upward.** When aspect-level improvements substantially change how an aspect coordinates its constituent cells, the improvements may warrant review at the Self level. Self integration architecture per B2.21 includes cross-aspect conflict handling rules, cross-aspect output composition rules, and the structural arrangement by which the Self holds multiple aspects as facets of one unified whole. If an aspect restructures its coordination rules substantially, Self integration architecture may need updating to reflect the changed aspect behavior. Self instinct/reasoning configuration per B2.23 may need adjustment if aspect changes affect which decisions route to instinct versus reasoning at the Self level. Governance at the Self level reviews aspect improvements and determines whether Self-level architectural changes are warranted. Aspect-level governance is origin governance; Self-level governance is destination governance. Both are required before Self-level changes are made.

### 2.2 Downward vertical evolution

Downward vertical evolution carries changes from higher structural levels to lower structural levels. Three paths are specified.

**Self-to-aspect downward.** Self-level DNA changes affect aspect operation through the Self integration architecture per B2.21. Changes to cross-aspect conflict handling rules affect how aspects interact with each other and with Self-level coordination. Changes to instinct/reasoning configuration per B2.23 affect which decisions aspects route to instinct versus reasoning. These Self-level changes do not require aspects to independently authorize them, but aspect-level governance reviews implications for aspect operation and may raise concerns through the governance path before Self-level changes are applied.

**Self-to-cell downward through the expression mechanism.** Self-level DNA changes reach cell behavior through the expression mechanism per B2.30. The expression mechanism is the architectural path: Self-level DNA activates or deactivates cell DNA elements per deployment configuration; changes to expression configuration in Self DNA change which cell DNA is active; changes to orchestration rules in Self DNA that bear on expression change what cells express at runtime. This is not implicit configuration that happens to affect cells — it is a governed mechanism with a specific architectural shape. The cell does not receive arbitrary top-down commands; it operates on whatever DNA is currently expressed, and what is expressed is determined by the expression mechanism operating on governed Self DNA. Self-level governance authorizes the DNA change before it propagates; the expression mechanism is the channel through which the authorized change reaches cell behavior.

**Aspect-to-cell downward.** Changes to aspect coordination rules per B2.16 affect cell participation patterns. Membership rule changes determine which cells participate in the aspect. Invocation rule changes determine how cells are called and what inputs they receive. Output-integration rule changes determine how cell outputs are weighted and assembled. These aspect-level changes are authorized by aspect-level governance and propagate to cell participation through the normal operation of the aspect's coordination rules.

### 2.3 Level-boundary governance

Crossing a level boundary in vertical evolution requires governance at both the origin level and the destination level. The rule applies in both directions.

For upward evolution: the origin level's governance authorizes the change at the originating level; the destination level's governance separately determines whether the change warrants updates at the destination level. These are not the same governance decision made twice — they are distinct decisions with distinct authority scopes. Origin governance answers: is this change at this level authorized? Destination governance answers: does this origin-level change require a response at the destination level, and if so, what response?

For downward evolution: origin-level governance authorizes the change before propagation; destination-level governance reviews implications. The expression mechanism handles the Self-to-cell path technically, but governance precedes and governs the change that the expression mechanism propagates.

### 2.4 The A6.06 authority distribution change boundary

A6.06 applies when vertical evolution changes the authority distribution — that is, when vertical evolution results in a change to which humans hold authority over which architectural components. This is the operationally most complex boundary case in vertical evolution.

Examples of authority-distribution-changing vertical evolution: a cell is reassigned from one aspect to another as part of upward-driven restructuring, and the reassigning aspect has a different governance scope and different human authority holders; a new aspect is created through vertical evolution, requiring assignment of human authority over the new aspect's governance; vertical evolution produces a new cell through birth, and that cell's governance authority must be assigned. In each case, A6.06 governs the authority-distribution change as a substrate event requiring its own governance process, separate from but concurrent with the vertical evolution event that triggered it.

### 2.5 Birth events triggered by vertical evolution

Vertical evolution may trigger birth events per B1.09. Three patterns arise: aspect splitting, in which a substantially evolved aspect is governed into two aspects with distinct coordination rules; new aspect creation, in which vertical evolution identifies a coordination need that warrants a new aspect rather than modification of existing aspects; and new cell birth, in which vertical evolution identifies a functional gap that warrants a new cell rather than modification of existing cells.

All births triggered by vertical evolution follow the full birth governance framework per B2.40–B2.44. The vertical evolution event that triggers the birth and the birth event itself are governed through their respective governance frameworks concurrently; the vertical evolution framework does not absorb birth governance.

---

## 3. What makes vertical-evolution-specification architecturally distinctive

Conventional AI architectures do not have cross-level evolution in any sense analogous to what vertical evolution specifies here. Model updates in a neural network do not have "levels" in the cell/aspect/Self sense; a model update changes parameters that affect behavior at every scope simultaneously, without level-boundary governance at any point. The levels in a hierarchical multi-agent architecture may have distinct scopes, but evolution of one level — typically through prompt engineering or system configuration — does not propagate to other levels through a governed mechanism with specified crossing requirements. There is no expression mechanism through which higher-level configuration changes reach lower-level behavior in a governed, inspectable, substrate-content way; higher-level changes affect lower-level behavior through implicit configuration paths that are architecturally opaque.

CKS vertical evolution is distinctive at three specific points. First, it is architecturally specified: the two directions, the three downward paths, the level-boundary governance rule, and the expression mechanism as the Self-to-cell channel are all named as architectural commitments, not implementation choices. Second, the downward path through the expression mechanism is governed rather than implicit. Self-level DNA changes that reach cell behavior do so through a mechanism that is itself substrate content, fully inspectable, and modifiable under human authority — not through implicit parameter propagation. Third, the level-boundary governance rule is bidirectional and symmetric: both upward and downward crossings require governance at both levels, not only at the level initiating the change. This prevents higher-level governance from unilaterally imposing changes on lower levels without lower-level review, and prevents lower-level improvements from propagating to higher levels without higher-level authorization.

---

## 4. The biological analog as conceptual scaffold

Biology offers useful analogic scaffolding for both directions of vertical evolution.

Upward vertical evolution parallels embryological induction in developmental biology. In induction, signals from one group of cells influence the developmental fate of adjacent or distant tissue layers; lower-level cellular signals propagate upward to shape higher-level tissue and organ organization. The pattern — lower-level changes informing higher-level developmental evolution — is structurally analogous to cell improvements informing aspect evolution, and aspect improvements informing Self evolution. The causal direction and the cross-level character are shared.

Downward vertical evolution parallels hormonal regulation. Systemic hormonal signals — originating at high-level regulatory structures — propagate through the organism and affect the behavior of individual cells in tissue-specific and cell-type-specific ways. The cells do not receive arbitrary commands; they respond to signals according to their own receptor configurations, which determine which signals they respond to and how. The pattern — high-level systemic changes reaching cell behavior through a governed mechanism rather than direct instruction — is structurally analogous to Self-level DNA changes reaching cell behavior through the expression mechanism, which determines which DNA is active per deployment configuration.

Both analogs function as conceptual scaffold — they help locate the architectural commitment in a space readers already understand intuitively. The architectural substance is governed cross-level propagation with level-boundary governance at every crossing. The expression mechanism's role in downward vertical evolution is not the same as hormonal signaling biologically; the analog is structural, not mechanistic. As in all CKS biological analogies, the scaffold carries the reader to the architectural shape and then steps back.

---

## 5. Inherited Paper 1 commitments

Vertical evolution specification inherits the full set of Paper 1 foundational commitments through Paper 2.

**A1.01 governance.** Human governance is an architectural property, not a procedural promise. Level-boundary governance in vertical evolution instantiates this commitment at each crossing: governance is required at both origin and destination levels as a property of the architecture, not as a workflow gate inserted by deployment choice.

**A6.06 authority distribution change.** When vertical evolution changes which humans hold authority over which components, A6.06 governs the authority-distribution change as a substrate event. This is the most operationally sensitive inheritance: vertical evolution's potential to create new entities, reassign cells, or restructure aspects means that authority distributions change as a consequence of architectural evolution, not only through deliberate authority-reassignment processes.

**A2.40 provenance.** Vertical evolution events are substrate events and are recorded in the provenance substrate. The cell improvement that triggered aspect review, the aspect-level governance decision, the Self-level DNA change that propagated through expression, the birth event triggered by vertical evolution — each is a recorded event with traceable provenance. Provenance recording is not optional for vertical evolution events; it is inherited from Paper 1's provenance commitment.

**A1.07 retraceability.** Vertical evolution paths are retraceable in both directions. A cell behavior change is retraceable to the Self-level DNA change that propagated through expression that produced it. A Self-level architectural change is retraceable to the aspect improvements that informed it. Retraceability applies across level boundaries, not only within levels.

**A1.13 composition.** Vertical evolution must preserve composition validity at all levels. A Self-to-cell downward change that breaks composition at the cell level is not a valid vertical evolution event, even if it is authorized at the Self level. Composition validity is a constraint that vertical evolution inherits from Paper 1's composition commitment and cannot waive through level-boundary governance.

**B1.09 birth.** Birth events triggered by vertical evolution follow the birth governance framework. Vertical evolution may identify that restructuring warrants new entities, but the birth of those entities is governed through birth's own framework, not absorbed into the vertical evolution framework.

**B2.30 expression mechanism.** The expression mechanism is the architectural path for Self-to-cell downward vertical evolution. Changes to expression configuration in Self DNA are the mechanism by which Self-level evolution reaches cell behavior. B2.30's full specification of the expression mechanism — as governed selection, as substrate content, as per-deployment design choice — applies to its role in downward vertical evolution.

---

## 6. Operational implications

Deployments that take vertical evolution seriously operate differently from deployments that treat evolution as level-local.

Governance bodies at every level maintain awareness of the vertical evolution events that their level either initiates or receives. A cell-level governance process that approves a DNA improvement should ask whether the improvement is substantial enough to warrant aspect-level review, and should initiate that review when the answer is yes. An aspect-level governance process should maintain a mapping from aspect coordination rules to the Self-level integration architecture they depend on, so that aspect improvements can be assessed for Self-level implications before being finalized.

Downward evolution requires Self-level governance to think about cell-level consequences. A Self-level DNA change that modifies expression configuration should be evaluated for its cell-level effects before authorization — which cells will express different DNA after this change, and are those effects desirable at the cell level? This requires governance to work with the expression mechanism specification per B2.30 actively, not as a passive implementation detail.

When vertical evolution triggers births, the birth governance framework per B2.40–B2.44 is engaged concurrently with the vertical evolution governance process. These two governance processes are not the same, and deployments must maintain both. The vertical evolution governance process answers whether restructuring warrants new entities; the birth governance process answers how those entities come into existence under governance.

When vertical evolution changes authority distributions, A6.06 governance is engaged. Deployments should anticipate authority-distribution changes as a regular consequence of vertical evolution — particularly aspect splitting, new aspect creation, and cell reassignment across aspects — and have A6.06 processes ready to handle them promptly, so that vertical evolution events are not blocked by unresolved authority ambiguity.

Cross-level verification after vertical evolution per B2.83 ensures that the changes made at origin and destination levels are mutually consistent and that composition validity is preserved across levels. Verification is not optional; it is the governance-closing step for vertical evolution events.

---

## 7. Limits

Several limits hold with the same force as the positive commitments above.

**Vertical evolution does not propagate automatically.** Governance decisions are required at each level boundary. A cell improvement that warrants aspect-level consideration does not automatically produce an aspect-level update; aspect-level governance must separately decide. A Self-level DNA change does not automatically trigger cell-level adjustments beyond what the expression mechanism produces; cell-level governance reviews implications. Propagation without governance decisions is not vertical evolution in the CKS sense.

**The expression mechanism does not bypass level-boundary governance.** The expression mechanism is the architectural path for Self-to-cell propagation, but it does not substitute for Self-level governance of the DNA change that the expression mechanism propagates. Governance authorizes the DNA change; the expression mechanism is the vehicle through which the authorized change reaches cell behavior. These are sequential, not alternatives.

**Vertical evolution does not guarantee coherent outcomes.** The governance quality at each level boundary determines whether outcomes are coherent. Level-boundary governance that reviews changes perfunctorily, that applies inconsistent criteria across levels, or that fails to consider composition validity will produce incoherent outcomes despite having exercised governance technically. The architecture provides the framework; governance quality is a deployment responsibility.

**Upward propagation does not mean that lower-level changes always warrant higher-level changes.** The governance decision at the destination level may be that no higher-level update is needed. Many cell improvements will not require aspect-level rule changes; many aspect improvements will not require Self-level architectural changes. The architecture requires review; it does not predetermine outcomes.

**Vertical evolution is not the same as horizontal evolution per B2.80.** Vertical evolution crosses structural levels; horizontal evolution refines content within a level. The two axes are orthogonal. A deployment event may involve both — an aspect restructuring may include both within-aspect rule refinement (horizontal) and identification that the restructuring warrants Self-level review (vertical) — but the axes remain analytically distinct. Conflating them produces both underspecification of each and overspecification of neither.

**Birth events triggered by vertical evolution follow full birth governance.** Vertical evolution identifies the need for new entities; it does not govern those entities into existence. Birth governance per B2.40–B2.44 handles the birth, with all its own requirements intact. Vertical evolution's identification of a birth need is an input to birth governance, not a substitute for it.

---

## 8. One-sentence test

A CKS architecture instantiates vertical evolution specification if and only if cross-level propagation in both upward and downward directions is governed at each level boundary with explicit governance at both origin and destination levels, downward propagation from Self to cell operates through the expression mechanism per B2.30 as a governed architectural path rather than implicit configuration, the A6.06 authority distribution change boundary is engaged when vertical evolution changes authority distributions, and birth events triggered by vertical evolution follow the full birth governance framework per B2.40–B2.44.

---

## 9. Why naming as standalone matters

Naming vertical evolution specification as a standalone derivation note accomplishes three things. It separates the cross-level-propagation specification from the within-level specification so that each can be independently evaluated, independently anticipated in prior art, and independently built upon in subsequent derivation work. It forces explicit articulation of the expression mechanism's role in downward vertical evolution — a role that is architecturally load-bearing but easily obscured if vertical evolution is treated as a generic "cross-level" concept without specifying the path. And it places the level-boundary governance rule — governance at both origin and destination, not governance at origin only — in the record as a named commitment that any architecture claiming bidirectional evolution must address.

This note is the third of five decomposing B1.16. B2.79 established the integrating frame: two axes, each requiring standalone specification. B2.80 formalized horizontal evolution. This note, B2.81, formalizes vertical evolution. B2.82 will address the operational timescale treatment — the temporal dimension of how vertical evolution events are paced, triggered, and sequenced across deployment maturation. B2.83 will close the B1.16 decomposition with bidirectional evolution verification: the cross-level consistency check that governs vertical (and horizontal) evolution events to completion. After B2.83, Phase B2 notes move to B1.17 relational roles decomposition, beginning the B2.84–B2.88 block.

The series architecture — each note formalizing one architectural derivation, the notes building prior-art density through accumulation — is the strategic mechanism. Vertical evolution specification occupies a high-value position in that architecture: it formalizes the cross-level propagation paths, the expression mechanism's downward role, and the level-boundary governance rule in a single note that any downstream claim to bidirectional-evolution or multi-level-propagation architecture in AI systems must now address.

---

## Cross-references

**Directly load-bearing:**
B1.16 (bidirectional evolution — parent commitment); B2.79 (bidirectional evolution integrating frame — immediate predecessor); B2.80 (horizontal evolution — B2.81's axis complement); B2.30 (expression mechanism — architectural path for Self-to-cell downward); A6.06 (authority distribution change — triggered by authority-affecting vertical evolution); A1.01 (human-governed definition — level-boundary governance instantiates this commitment); A1.13 (composition — vertical evolution must preserve composition validity).

**Directly relevant:**
B2.21 (Self integration architecture — destination of aspect-to-Self upward; affected by Self-to-aspect downward); B2.16 (aspect coordination rules — destination of cell-to-aspect upward; origin of aspect-to-cell downward); B2.23 (instinct/reasoning configuration — affected by aspect-to-Self upward and Self-to-aspect downward); B1.09 (birth — triggered by vertical evolution); B2.40–B2.44 (birth governance framework — governs all vertical-evolution-triggered births); A2.40 (provenance — vertical evolution events recorded); A1.07 (retraceability — vertical evolution paths retraceable); B2.83 (bidirectional evolution verification — cross-level consistency check closing B1.16 decomposition).
