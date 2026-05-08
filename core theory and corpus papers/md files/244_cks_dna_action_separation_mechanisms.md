# DNA–Action Layer Separation Operational Mechanisms in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the operational mechanisms by which the DNA layer and the Action layer specified in the source paper's two-layer commitment are kept architecturally distinct in deployment.

## Abstract

Paper 2's structural-modularity commitment includes the proposition that within every cell two distinguishable substrate layers operate: a DNA layer carrying stabilized orchestration content, and an Action layer carrying recorded task instances. Two prior notes formalize each layer in isolation. What those notes leave underspecified is the operational architecture by which the layers are kept distinct once a deployment exists. Without enforcing mechanisms, layer confusion can propagate through deployment evolution. This note formalizes the mechanisms CKS commits to: substrate-resident type declarations, scope-validation rules, cross-layer operation provenance, layer-distinct evolution mechanisms, layer-distinct governance, and layer-aware inspection semantics. The mechanisms are mutually reinforcing — each alone is insufficient; together they make the layer distinction operationally enforced rather than nominally specified. The note states each mechanism precisely, contrasts the resulting architecture with conventional AI systems whose internal state is unified, identifies the implicit-drift failure mode the mechanisms protect against, names the inherited Paper 1 commitments each rests on, and provides an operational test for whether a deployment instantiates the commitment.

## 1. Why the separation mechanisms need to be formalized as standalone

Paper 2's two-layer commitment names DNA and Action as distinguishable substrate layers within every cell with distinct governance semantics. The DNA layer carries stabilized orchestration content — schemas, conflict-handling rules, lifecycle policies, the harness logic that defines what the cell is governed to do. The Action layer carries recorded task instances and their outputs — what actually happened when DNA met an actual task. Both are substrate content under Paper 1's commitments; what distinguishes them is governance semantics, with DNA stabilized and human-governed at modification, and Action accumulating as the cell operates.

Two prior decomposition notes formalize each layer on its own. Neither answers the operational question that follows once a deployment exists with both layers present: what keeps them distinct during operation? Architectural specification of two-layer-ness establishes the layers as objects of theory; it does not by itself supply the machinery a deployment uses to maintain the distinction across substrate writes, cell executions, evolution events, and human interventions.

The risk of leaving this underspecified is concrete. Without operational mechanisms, several failure modes propagate quietly: DNA modifications misapplied to Action records; accumulated Action context silently reshaping DNA — a particularly load-bearing risk because action-feedback evolution is itself an architecturally-sanctioned cross-layer operation, but only when explicitly governed; evolution mechanisms operating on the wrong layer; inspection losing track of which content is which. Together these failures erode the two-layer architecture into one undifferentiated substrate that has two layers in description but not in operation.

The remedy is to name the operational mechanisms as a standalone commitment alongside the per-layer specifications. This note formalizes them as the third of five derivation notes decomposing the source paper's two-layer commitment.

## 2. The mechanisms, precisely stated

CKS commits to six operational mechanisms that together enforce DNA–Action layer separation. None alone is sufficient.

**(a) Substrate-resident type declarations.** Content within a cell is declared as DNA-typed or Action-typed. The type declaration is itself substrate content — authoritative, inspectable, and human-governed under Paper 1's source-of-truth commitment. Type declarations are part of the substrate the cell carries, not annotations applied externally; they govern how downstream operations interpret the content they classify.

**(b) Scope-validation rules.** Orchestration rules — human-authored under Paper 1's rule-authoring commitment — specify that operations on DNA respect DNA scope and operations on Action respect Action scope. A rule that reads, modifies, or evolves substrate content carries a scope constraint: it operates on DNA only, on Action only, or — for the small set of cases governed explicitly — across both. A routine recording rule cannot silently rewrite DNA; a DNA-evolution rule cannot accidentally overwrite an Action record.

**(c) Cross-layer operation provenance.** When operations span layers — for example, action-feedback evolution that reads Action evidence to propose DNA changes — the provenance fields the substrate carries explicitly record the cross-layer character. Cross-layer operations are not handled by hiding their cross-layer nature; they are recorded as cross-layer in the provenance metadata that accompanies every substrate write. Audit can identify cross-layer operations by reading provenance and verify they were authored as such rather than slipping through as mis-scoped within-layer operations.

**(d) Layer-distinct evolution mechanisms.** DNA evolves through directed selection — predictable trajectory under human-governed orchestration substrate updates — and through action-feedback evolution, which reads accumulated Action evidence to inform DNA refinement. Action accumulates routinely as the cell operates and as writers under orchestration rule produce records of what happened. The two evolution shapes are mutually distinct because the layers they operate on are mutually distinct.

**(e) Layer-distinct governance.** Different orchestration rules govern DNA modification and Action modification. DNA modification is typically deliberate, with retroactivity preserved — a DNA change does not retroactively rewrite the historical Action records produced under prior DNA. Action modification is typically restricted, with override per the human-governed override right preferred over direct in-place modification, so historical Action remains retraceable rather than silently restated.

**(f) Layer-aware inspection semantics.** Humans exercising the inspect right see content with its layer typing surfaced. Inspecting a cell's DNA shows specification — what the cell is governed to do; inspecting a cell's Action shows history — what the cell did. Inspection tools support layer-aware queries — "show me all DNA content," "show me all Action records," "show me cross-layer operations recorded against this cell." The two layers are visibly distinct on inspection rather than indistinguishable runs of substrate content the human has to classify by reading.

The six mechanisms are not options to choose from. Each addresses a specific way layer separation could erode without it, and removing any one degrades the architecture in a way the others cannot fully compensate for.

## 3. What makes the mechanisms architecturally distinctive

Three properties distinguish the separation mechanisms from generic data-segregation patterns.

**Operational, not nominal.** Conventional AI architectures often have unified internal state — governance content and execution history mixed without architectural separation. A model's weights carry both what it has been trained to do and traces of what it has been trained on; a tool-using agent's prompt carries both its instructions and the running record of its operations. The distinction CKS draws between DNA and Action either is not made in such systems or exists only nominally. CKS makes it operational through the six mechanisms — not what the architect reports, but what the substrate carries and the rules enforce.

**Mutually reinforcing, not single-mechanism.** Each mechanism addresses a failure mode the others cannot fully cover, and the chain runs straight through: type declarations require scope-validation to enforce them; scope-validation requires cross-layer provenance to record sanctioned exceptions; provenance requires layer-distinct evolution to keep DNA and Action changes from operating on each other; that requires layer-distinct governance; that requires layer-aware inspection so humans can read what they are exercising authority over. A deployment that implements only some of the six has a partial architecture in which layer confusion can propagate through whichever mechanism is omitted.

**Protective against implicit drift.** The most consequential failure the mechanisms guard against is the silent absorption of Action evidence into DNA without governance — the case where action-feedback evolution, legitimate when explicit, degenerates into uncontrolled drift when implicit. Without the mechanisms, accumulated Action context could quietly reshape what the cell is governed to do, with no trace in provenance and no opportunity for humans to inspect, modify, or override the change. With the mechanisms, any DNA modification is recorded as such, governed under the appropriate layer-distinct rules, and inspectable by humans. The protection is what makes the action-feedback evolution loop safe to close; without it, the loop is itself a failure mode.

The biological analog is direct. Biological cells separate genetic material in the nucleus from operational cytoplasm activity through structural mechanisms — nuclear membrane, transcription machinery, regulatory pathways governing when DNA is read or modified. The separation is structural, not nominal. CKS DNA–Action separation is similarly structural through its own architectural mechanisms; the biology functions as conceptual scaffold while the architectural substance is the six mechanisms. CKS exceeds biology in being human-governed.

## 4. What the mechanisms do NOT do

Stating the mechanisms precisely makes it equally important to state what they do not accomplish.

**They do not prevent cross-layer operations.** Action-feedback evolution explicitly reads Action evidence to propose DNA refinements; the mechanism is sanctioned by the source paper as one of three evolution shapes. The separation mechanisms do not block such operations; they make them identifiable as cross-layer, recorded with their cross-layer character, and governed under appropriate rules. What the mechanisms prevent is unrecorded or unauthorized cross-layer operation.

**They do not eliminate the need for cell-level governance.** Layer-distinct governance is one component of the architecture, not a replacement for the broader human-governed commitment from Paper 1. A cell whose DNA and Action are perfectly distinguished but whose modification authority is otherwise ungoverned still fails the broader architectural commitments.

**They are not exhaustive.** Deployments may add additional layer-aware mechanisms — cryptographic signing of DNA content, explicit ratification workflows for cross-layer evolution events, parallel verification substrates. The six mechanisms are what CKS commits to architecturally; deployments are free to extend.

**They do not prescribe specific implementations.** Tool-agnosticism from Paper 1 holds at this layer as elsewhere. A type declaration may be a column on a spreadsheet substrate, a typed field in a database, a tag in a graph store, or a structured comment in a versioned text artifact. Scope-validation may be enforced by application-layer guards, by orchestration rules invoked by a stable cell, or by the substrate's native constraint mechanisms.

**They are intra-cell, not inter-cell.** The mechanisms operate within the cell boundary. Inter-cell layer questions are different in kind: cells do not share DNA or Action across cells, and the architecture's combination primitives handle inter-cell layer composition through their own machinery, with the within-cell separation mechanisms holding for each participating cell.

## 5. Inherited Paper 1 commitments

Each of the six mechanisms rests on a specific Paper 1 commitment carried forward. The substrate–cell boundary applies at intra-cell scope through layer typing, with DNA and Action both being substrate content under the boundary commitment. Type declarations are authoritative in Paper 1's source-of-truth sense: when the system needs to answer "is this DNA or Action?" the answer is read from substrate type declarations, not inferred from content shape. Scope-validation rules are orchestration rules under Paper 1's rule-authoring commitment — human-authored, substrate-resident, exercisable through the same authority architecture. Cross-layer operation provenance uses the same six provenance fields Paper 1 commits to substrate writes carrying, with the cross-layer character recorded in the rule reference and antecedent fields. Layer-aware inspection follows from the inspect right Paper 1 names as one of the three rights composing the human-governed commitment. Retroactivity preservation under Paper 1's accumulating-record commitment is what makes layer-distinct governance work: a DNA change does not retroactively rewrite Action records produced under prior DNA.

## 6. Operational implications

Several implications follow when the mechanisms are realized in a deployment. Type declarations are configured at cell creation — DNA elements receive DNA typing, the Action layer is initialized as Action-typed substrate space. Scope-validation rules are configured per deployment, with strict enforcement preferred for high-stakes deployments and permissive scope with explicit cross-layer authorization appropriate for early-stage deployments where boundaries are still being worked out. Cross-layer operations have explicit recording: action-feedback evolution writes provenance naming the read of Action and the proposed write to DNA as one cross-layer event, not as two within-layer events. DNA evolution and Action accumulation happen concurrently on different timescales without contention. Deployment audit verifies separation is operationally maintained by sampling provenance, scope-validation logs, and inspection results against the deployment's specified policy.

Without the separation mechanisms, action-feedback evolution risks degenerating into the kind of implicit drift Paper 1's accountability architecture is designed to make impossible. With them, action-feedback is exactly as governed as any other DNA modification: explicit, recorded, inspectable, and overridable.

## 7. Operational test

A deployment instantiates the DNA–Action layer separation operational mechanisms commitment if and only if all of the following are true at all times during the cell's existence:

1. Every piece of substrate content within the cell carries a type declaration identifying it as DNA, as Action, or — for cross-layer artifacts produced by sanctioned cross-layer operations — as cross-layer with the operation type recorded.
2. Operations on substrate content within the cell are subject to scope-validation rules that constrain each operation to a specified layer or layers, with cross-layer operations explicitly authorized rather than implicitly permitted.
3. Provenance recorded with every substrate write identifies the layer or layers the write touched, and cross-layer writes are recorded as cross-layer rather than as a sequence of within-layer writes.
4. Evolution operations targeting DNA are governed by orchestration rules distinct from those governing Action accumulation, and the rules' specified scope is respected by the operations they govern.
5. Modification authority for DNA is governed under rules distinct from those governing Action modification, with retroactivity preservation holding such that DNA changes do not retroactively rewrite historical Action records.
6. A human exercising the inspect right can query content within the cell with layer-aware filters and receive layer-distinguished results.

A deployment that fails any of (1) through (6) does not instantiate the separation mechanisms commitment, even if it satisfies the per-layer specifications in some other respect. Such a deployment may still be a useful system; it does not maintain the two-layer architecture operationally.

## 8. Conclusion

The DNA–Action layer separation mechanisms are what make Paper 2's two-layer commitment operational rather than nominal. Naming each layer specifies what each is; specifying the mechanisms that keep them distinct in deployment is what prevents the architecture from eroding into one undifferentiated substrate that has two layers in description but not in operation. The six mechanisms — substrate-resident type declarations, scope-validation rules, cross-layer operation provenance, layer-distinct evolution mechanisms, layer-distinct governance, and layer-aware inspection semantics — are mutually reinforcing; the combination is what enforces the distinction across the cell's lifetime.

The mechanisms inherit from Paper 1 without redefense, specialized to intra-cell scope. They do not prevent cross-layer operations; they make legitimate cross-layer operations identifiable as such and prevent illegitimate ones from slipping through unrecorded. They do not stand in for cell-level governance; they add layer-aware semantics to it. They do not prescribe specific implementations; they specify what any implementation must accomplish.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *DNA–Action Layer Separation Operational Mechanisms in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
