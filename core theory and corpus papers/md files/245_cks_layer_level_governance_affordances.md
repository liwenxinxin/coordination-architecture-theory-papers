# Layer-Level Governance Affordances at the DNA and Action Layers of a CKS Cell

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize how Paper 1's four named governance affordances — the inspect right, the modify right, the override right, and rule authoring — apply distinctly at the DNA layer and the Action layer named in Paper 2's two-layer architecture within every cell, with layer-distinct operational character reflecting the different architectural roles of specification and history.

## Abstract

Paper 1's "human-governed" commitment names four governance affordances: the right to inspect substrate content and orchestration rules, the right to modify them, the right to override LLM-produced or rule-driven outputs touching them, and the right to author the orchestration rules under which cells operate. Paper 2 inherits these affordances and applies them recursively at every level of the Self's structural composition. At the cell level, the substrate is internally distinguished into two layers — DNA (stabilized orchestration content; specification) and Action (recorded task instances; history) — whose distinct architectural roles are formalized in companion derivation notes. This note formalizes how the four governance affordances apply with layer-distinct operational character. The affordances themselves are unchanged; what changes is the operational character of their exercise. DNA inspection and Action inspection are both freely available; DNA modification proceeds through deliberate directed selection while Action modification is operationally protected by preference for override-as-correction over direct modification, preserving path retraceability; rule authoring at DNA targets DNA content directly while rule authoring at Action targets Action's recording behavior. Authority distribution may be layer-distinct. The note states the application precisely, names what it inherits from Paper 1, articulates the role differences that drive operational character, names operational implications, and bounds the claim against six misreadings.

## 1. Why layer-level governance affordances need to be formalized as a standalone derivation

Paper 2 commits to a two-layer architecture within every cell. DNA carries the cell's stabilized orchestration content — harness logic, conflict-handling rules, lifecycle policies, schemas — that defines what the cell is governed to do. Action carries the cell's recorded task instances and outputs — what actually happened when the DNA met an actual task. Both layers are substrate content under Paper 1's commitments; both are human-governed; both are inspectable, modifiable, and overridable. The DNA/Action distinction lives within Paper 1's substrate framework, not outside it.

The recursive-Paper-1 commitment holds that Paper 1's architectural commitments apply at every level Paper 2 introduces — at cell, aspect, and Self scope. The four governance affordances are part of the inherited commitment set. Stating that the affordances "apply" at the cell layer does not, however, exhaust the operational content. At cell scope the substrate is internally two-layered, and the layers do different architectural work. Treating governance as if the affordances apply uniformly across both layers misses what the role differences entail for how they are exercised.

The differentiation is consequential for path retraceability. Paper 1's six-field provenance metadata makes any substrate state attributable to a specific actor, action, time, rule, and rationale; its operational value depends on records remaining intact as historical evidence. When Action governance protects historical records through override-preferred correction, the audit trail remains intact; when Action is freely modifiable, retraceability becomes a procedural promise that discipline alone holds in place. Naming the layer-distinct operational character moves the protection from procedural to architectural-by-convention.

This note formalizes the layer-distinct operational character so that downstream implementations have a precise specification of how the four affordances apply at each layer. It is the fourth of five decompositions of Paper 2's two-layer architecture; companion notes specify the DNA layer, the Action layer, and the separation mechanisms between them, and a closing note will verify two-layer architecture inheritance from Paper 1.

## 2. The architectural application, precisely stated

Paper 1's four governance affordances apply at the cell's two layers as follows. The architectural commitment is unchanged from Paper 1 in every case; what is specified here is the operational character matched to layer role.

**Inspect right at layers.** Humans inspect DNA content freely. DNA carries the cell's specification; it is meant for understanding and review. Humans inspect Action content freely. Action carries the cell's operational history; it is meant for retraceability and audit. Both layers satisfy the inspect-right requirements named in Paper 1: read access without LLM intermediation as a precondition, in inspectable form, at the time of choosing. The layers differ in what inspection serves operationally; the architectural affordance is uniform.

**Modify right at layers.** DNA modification is exercised deliberately through directed selection: humans propose changes, the orchestration substrate's authority architecture determines who authorizes, modifications are recorded with provenance, and changes follow Paper 1's rule-retroactivity treatment — historical DNA preserved as substrate content with new DNA applying forward. Action records under prior DNA remain interpretable under the prior DNA's specification context; audit reach across DNA evolution is preserved. Action modification has strong operational protection: direct modification of historical Action records would compromise path retraceability, since the provenance metadata that makes the substrate auditable rests on Action records being preserved as evidence. Deployments typically prefer override over direct modification for Action — adding new records that supersede prior records, with both preserved as Action content. The protection is operational practice arising from the layer's role, not a restriction on the modify right itself; the right remains exercisable, configured to preserve retraceability.

**Override right at layers.** Humans override DNA-driven decisions per Paper 1's general specification — the override action is recorded as an override event affecting a specific decision without modifying the underlying DNA. The DNA itself is unchanged; the override is targeted at the specific operation. Humans override Action records by adding override records that supersede prior records without modifying them. The prior record is preserved as substrate content; the superseding record is preserved alongside it; the lineage between them is recorded. Override is the typical mechanism for Action correction, reflecting the layer's history role.

**Rule authoring at layers.** DNA content is authored under Paper 1's rule-authoring affordance — the orchestration rules and the DNA they constitute are themselves the foundational substrate of cell behavior. Action content is not directly authored as rules in the same sense; what humans author at the Action layer are the recording rules — orchestration-substrate rules specifying what gets recorded, at what level of detail, with what retention. The recording rules govern Action's recording behavior; the Action records themselves are the recorded outcomes.

**Authority distribution may be layer-distinct.** Paper 1's broader authority architecture admits fine-grained authority configuration, and Paper 2's layer architecture admits layer-distinct authority within that configuration. Some humans may hold authority for DNA modification (deployment architects, governance committees) while others hold only Action inspection authority (auditors, operational analysts). Layer-distinct authority is enabled architecturally; it is not prescribed.

## 3. What makes layer-level governance affordances architecturally distinctive

Conventional AI architectures often have undifferentiated governance: roles distinguish actors by access scope, but the substrate the actors act over is structurally homogeneous. An administrator can modify any part of the system; an auditor can read any part. Where structural differentiation does appear, it is typically a deployment convention held in place by procedural discipline.

CKS layer-level governance is structurally differentiated by architectural role. DNA is specification — meant to be modified deliberately to evolve cell behavior. Action is history — meant to be preserved as evidence. The four governance affordances apply consistently across both in architectural commitment, but their operational character matches the role each layer plays. Modifying DNA is operationally different from modifying Action; the difference is consequential, not stylistic; and it follows from the layers' inherent role rather than from a policy overlay.

Three consequences follow. For retraceability: Action governance protection makes retraceability a property of the Action layer's content rather than a procedural promise. For evolution: DNA modifications evolve specification under DNA governance while Action records accumulate under Action governance, with the action-feedback loop crossing the layers under both layers' governance simultaneously. For audit: Action content is examined with confidence in its integrity, with override events preserved as substrate content rather than overwriting what they correct.

## 4. Inherited Paper 1 commitments

Layer-level governance affordances inherit and depend on Paper 1's broader commitment set; the inheritances are explicit.

The four governance affordances are Paper 1's; this note does not introduce new ones. Path retraceability is preserved by Action governance protection: records are preserved as evidence under override-preferred correction, the six-field provenance vocabulary remains attributable, and the audit trail remains intact across operational corrections. Authority distribution per Paper 1 admits fine-grained allocation; layer-distinct authority sits within that admission. Rule retroactivity is what DNA modifications follow: prior DNA preserved as substrate content with new DNA applying forward, and Action records under prior DNA remain interpretable under the prior specification. The "human-governed" commitment overall — authority over substrate content and orchestration rules at all times — is preserved across both layers; what is specified here is operational character, not commitment scope.

## 5. Architectural role differences driving operational character

The operational character of the four affordances at each layer follows from the layers' architectural roles.

DNA carries the stabilized orchestration content that defines what the cell is governed to do. It is meant to be modified — to evolve cell behavior as deployment requirements change, as evidence accumulates, as governance committees authorize new rules. The deliberate-modification character of DNA exercise reflects this role.

Action carries the recorded experience of what the cell has done. It is meant to be preserved as evidence: audit reach, retraceability, and the action-feedback evolution loop all depend on Action being reliably what it claims to be. The strong-protection character of Action exercise reflects this role: correction proceeds through override (adding records that supersede) rather than through direct modification, so prior records are preserved even when current state is corrected.

The four rights are general and apply consistently in architectural commitment. The operational character differs by layer because the layers' roles differ — operational character matched to inherent role, not policy-overlay above an undifferentiated substrate.

## 6. Operational implications

Several consequences follow from the layer-distinct operational character. Deployments configure layer-distinct governance per requirements: who can modify DNA, who can override Action, who can author recording rules. Layer-distinct governance is testable per layer: Paper 1's inspect-right and modify-right tests apply at each layer with character appropriate to layer role. High-stakes deployments typically have stricter Action protection, making override-only correction operationally enforced rather than merely preferred. Cross-partner deployments may have layer-distinct authority, expressing partner-specific governance through fine-grained authority allocation. Layer-distinct evolution operates under layer-distinct governance: DNA evolves under DNA governance, Action accumulates under Action governance, and the action-feedback loop closes the layers under both layers' governance simultaneously, as a governed cross-layer operation rather than as an automatic flow. Deployment audit examines layer governance — that Action protection is operationally enforced, that DNA modifications are recorded with provenance, that authority distribution matches what the deployment claims. Layer governance is itself an audit object.

## 7. Limits

The standalone treatment is bounded; stating the limits precisely is what keeps it from drifting into commitments the source paper does not support.

**It does not modify the affordances themselves.** Paper 1's specifications of inspect, modify, override, and rule authoring are unchanged. What this note adds is operational character of their exercise per layer.

**It does not eliminate layer-distinct authority configuration.** Layer-distinct authority is enabled architecturally; whether a deployment configures distinct authority is a deployment decision that Paper 1's general admission of fine-grained authority covers.

**It does not prescribe specific operational practices.** Override-preferred correction at the Action layer is the typical operational character, not a hard rule that direct modification of Action is forbidden. Deployments may permit direct modification under stricter authority gating, may forbid all modification of historical records, or may configure access in other ways consistent with Paper 1's affordances.

**It does not prevent cross-layer operations.** Action-feedback evolution is a cross-layer operation: Action evidence drives DNA modification proposals, and the resulting DNA modifications affect what Action subsequently records. Layer-distinct governance specifies how each layer is governed; cross-layer operations are governed under both layers' governance simultaneously.

**It is not a separate governance mechanism.** Layer-level governance affordances are Paper 1's authority architecture applied with layer-distinct operational character. They are not a fifth governance affordance alongside the four named in Paper 1.

**It does not replace the separation mechanisms.** A companion derivation note specifies the separation mechanisms that structurally distinguish DNA from Action at the substrate level; this note operates at the authority level. The two operate together; replacing one with the other would lose architectural commitments either supplies.

## 8. Operational test

A deployment instantiates layer-level governance affordances if and only if all of the following hold at all times during the cell's existence, at both DNA and Action layers:

1. Inspection is exercisable at each layer with character matched to layer role (DNA for specification review, Action for audit and retraceability), without LLM intermediation as a precondition, at the time of choosing.
2. Modification is exercisable at each layer, with DNA modification proceeding through directed selection with provenance and rule-retroactivity treatment, and Action modification operationally protected by preference for override-as-correction over direct modification.
3. Override is exercisable at each layer, with DNA override targeting specific decisions without modifying underlying DNA and Action override adding records that supersede prior records without modifying them.
4. Rule authoring is exercisable at each layer, with DNA content authored directly and Action recording rules authored to specify what gets recorded, at what level of detail, with what retention.
5. Authority distribution admits layer-distinct configuration; deployments may configure distinct authority across layers per requirements.
6. The operational character at each layer preserves Paper 1's broader commitments — human governance, path retraceability, authority distribution, rule retroactivity.

A deployment that fails any of (1)–(6) does not instantiate layer-level governance affordances as the source paper supports them, even if the four affordances are nominally satisfied.

## 9. Conclusion

Treating Paper 1's four governance affordances as if they apply uniformly across the cell's two layers misses what the layers' role differences entail for how they are exercised. DNA is specification, meant for deliberate modification; Action is history, meant for preservation as evidence. The affordances apply consistently in architectural commitment across both, but their operational character matches each layer's architectural role: DNA modification proceeds through deliberate directed selection with rule-retroactivity treatment; Action modification proceeds through override-preferred correction that preserves prior records as evidence; DNA inspection serves specification review while Action inspection serves audit and retraceability; rule authoring at DNA targets DNA content directly while rule authoring at Action targets Action's recording behavior. Authority distribution may be layer-distinct.

Naming the layer-level governance affordances as a standalone derivation gives downstream implementers a precise specification of how Paper 1's four affordances apply at each of the cell's two layers, separable from how they apply at higher composition scopes. Subsequent work that uses governance affordances differently at the cell's two layers is using a different specification, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Layer-Level Governance Affordances at the DNA and Action Layers of a CKS Cell.* May 8, 2026. ORCID: 0009-0004-8065-3235.
