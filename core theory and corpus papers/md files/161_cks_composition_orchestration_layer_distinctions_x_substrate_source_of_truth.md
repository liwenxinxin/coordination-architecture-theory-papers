# Composition Pair: Orchestration Layer Distinctions × Substrate-as-Source-of-Truth — The Orchestration Source-of-Truth Distinction as Emergent Architectural Property

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize the emergent architectural property that arises when two foundational CKS commitments — orchestration layer distinctions (the three-layer separation of coordination-knowledge, coordination-mechanism, and control-plane concerns) and substrate-as-source-of-truth (the substrate as authoritative answer to coordination questions) — compose. The composition produces an architectural property that neither commitment yields independently: a clean distinction between non-authoritative orchestration definitions on the one hand and substrate-resident authoritative rules on the other.

## Abstract

The CKS pattern's orchestration-layer distinctions commit a deployment to separating coordination-knowledge state (in the substrate) from coordination-mechanism behavior (in workflow engines or agent frameworks). The substrate-as-source-of-truth commitment specifies that the substrate is authoritative for five categories of coordination state — including, by name, the orchestration rules that govern cell-level behavior. Each commitment, taken alone, leaves a question the other answers. Orchestration-layer distinctions specify that workflow engines occupy a different layer than the substrate but do not specify which layer's content is authoritative for coordination. Substrate-as-source-of-truth specifies that the substrate holds authoritative content but does not, in itself, distinguish workflow definitions from substrate-resident rules at the orchestration boundary. Composed, the two commitments produce a sharper distinction than either yields alone: workflow definitions, scheduling logic, and triggering conditions are non-authoritative orchestration definitions; orchestration rules per A2.46 (Category 4: substrate authoritative for "what rules apply") are authoritative substrate content; orchestration triggers cells, but rules — not orchestration — determine what the cell does. This note names the property *orchestration source-of-truth distinction*, states its four operational components, identifies the architectural decisions the composition forces, names the anti-patterns it forbids, and gives a three-property operational test for whether a deployment maintains the distinction.

## 1. Why the composition needs to be formalized as standalone

A1.15 (orchestration layer distinctions) and A1.08 (substrate-as-source-of-truth) are each load-bearing CKS commitments. A1.15 separates the coordination-knowledge layer from the coordination-mechanism layer (workflow engines, agent frameworks) and from the control-plane layer; it identifies workflow execution state and agent-framework memory as non-substrate state. A1.08 specifies which categories of state are substrate-authoritative — what was decided, by whom, under what authority, with what rationale, and what conflicts remain — and includes orchestration rules among them by name. The two commitments operate at different architectural granularities: A1.15 names the layer; A1.08 names what the substrate's content is authoritative *for*.

The composition's standalone formalization earns its place on three grounds.

First, the property the composition produces is not derivable from either commitment alone. A1.15 alone tells a deployment that workflow engines occupy a different layer than the substrate; it does not, in itself, tell the deployment which layer's content is authoritative. A1.08 alone tells a deployment that the substrate is authoritative for orchestration rules and four other categories; it does not, in itself, draw a line between substrate-resident rules and workflow-engine-resident definitions. The architectural distinction this note formalizes — workflow logic non-authoritative, rules per A2.46 authoritative, orchestration triggers but does not determine cell behavior — is what falls out only when the two commitments are read together against the same deployment.

Second, the composition is what determines whether common deployment patterns are CKS-compatible. A workflow engine triggering a CKS cell is a pattern source paper §4.4 names directly and the composition pattern §6 of A1.15 develops as the canonical layering. The pattern is coherent only if the workflow engine's definitions are not treated as authoritative content for coordination decisions while the cell's substrate-resident rules are; otherwise the deployment has two competing sources of truth at the orchestration boundary, and the substrate's commitments degrade quietly.

Third, the composition is the pair most easily violated by drift in compliance-driven deployments. Deployments under regulatory or audit pressure often migrate workflow definitions into vendor governance systems and start treating them as authoritative policy artifacts. The migration looks like governance because the workflow definitions are reviewed, versioned, and signed off — but the architectural commitment they violate is not visible at the artifact level. The composition makes the violation visible: a workflow definition is non-authoritative orchestration regardless of how many sign-offs it carries, because authority sits with substrate-resident rules per A2.46 and not with definitions held in any layer outside the substrate.

This note is the third in the A1.15 cluster. A4.23 formalized orchestration-mediator separation (A1.15 × A1.04) by clarifying that the LLM mediates over substrate content rather than over workflow execution state. A4.24 formalized orchestration retraceability (A1.15 × A1.07) by clarifying that path retraceability traces decisions through substrate provenance rather than through workflow execution logs. A4.25 — this note — formalizes orchestration source-of-truth distinction by clarifying which of the layers A1.15 distinguishes is authoritative for which categories of state. A4.26 will close the cluster.

## 2. The emergent architectural property

The property the composition produces — *orchestration source-of-truth distinction* — has four operational components.

**Component 1. Workflow logic is non-authoritative orchestration definition.** Workflow definitions, scheduling logic, and triggering conditions held in workflow engines are not authoritative content for any of the five coordination-state categories A1.08 specifies. They describe when execution happens; they do not, by themselves, encode what was decided, by whom, under what authority, with what rationale, or what conflicts remain unresolved. A workflow engine that records "cell X ran at time T with input I" records execution state at the coordination-mechanism layer; the record is not a substrate write, and the system does not read from it to answer coordination questions.

**Component 2. Rules per A2.46 are authoritative substrate content.** Orchestration rules — the human-authored rules that govern cell-level behavior under A2.04 — are substrate content per Category 4 of A1.08's source-of-truth scope (substrate authoritative for "what rules apply"). The rules sit in the substrate, are addressable, carry their own provenance, and are subject to the three governance rights of A1.01 (inspect, modify, override). Workflow conditions and orchestration rules are different objects at different layers: workflow conditions trigger execution; rules govern execution.

**Component 3. Orchestration triggers cells but does not determine cell behavior.** Workflow engines per A2.87 may decide *when* a cell runs and *with what inputs*; what the cell *does* once it runs, and what it produces as output, follows from the substrate-resident rules per A2.04. The workflow engine's role is invocation; the rule's role is behavior specification. Cell behavior is not a function of workflow conditions, and a deployment in which it is has collapsed two layers into one.

**Component 4. The source-of-truth-versus-mirror distinction (A2.48) applies at the orchestration boundary.** Workflow engines and agent frameworks may legitimately hold derived views of substrate content — a workflow's branching condition may, for example, reflect a substrate-recorded authority assignment — but such derived views are mirrors, not sources. The mirror–source distinction A2.48 develops is what licenses the composition: the substrate is authoritative; downstream layers may carry views derived from it; the views are non-authoritative by construction; if a view disagrees with the substrate, the substrate wins by definition.

## 3. What the composition forces beyond either commitment alone

The composition forces four architectural decisions that neither A1.15 nor A1.08 forces in isolation.

**Workflow definitions are documented as non-authoritative.** A composition-respecting deployment names its workflow definitions as orchestration material rather than as policy artifacts. This is a documentation discipline as well as a runtime configuration: the definitions' role must be legible to participants exercising the inspect right of A1.01, so a participant looking for the operative rules does not find them in workflow-engine state by mistake.

**Rules per A2.04 are verified as substrate-resident authoritative content.** Where an orchestration rule sits — in the substrate, in a workflow engine's definition, in vendor configuration — is itself an architectural property the composition makes auditable. The verification is concrete: take any rule the system invokes when a cell runs; check whether the rule is addressable, inspectable, modifiable, and overridable as substrate content per the human-governed commitment. If it is not, the rule has migrated outside the substrate, and Component 2 has been violated.

**Orchestration cannot determine cell behavior.** Cell behavior follows from the rules the cell executes against substrate content; it does not follow from workflow branching, scheduling parameters, or triggering conditions. A deployment in which a workflow's branching logic encodes the actual behavioral specification of a cell — what to write to the substrate, which conflicts to flag, which authority assignment to apply — has placed authoritative content at the orchestration layer, and Component 3 has been violated even if the workflow engine and the substrate sit at correctly separated layers.

**Vendor workflow logic is mapped to architectural non-authority.** A workflow engine sold or operated as a "policy management" or "compliance authority" system is not, by virtue of that positioning, a substrate. The composition forces an explicit architectural mapping of any vendor workflow product to its layer: coordination-mechanism layer if it triggers and runs cells; not coordination-knowledge layer regardless of how it is marketed. The mapping is the deployment's responsibility; the composition specifies what the mapping must conclude.

## 4. Anti-patterns the composition forbids

Five anti-patterns are specific instantiations of composition violation.

**Workflow-as-policy.** Workflow definitions are treated as authoritative policy artifacts — versioned, signed, audited as if they were the operative rules — and read from to answer "what rules apply" rather than from substrate content. Violates Components 1, 2, and 4 simultaneously and is the canonical composition violation under regulatory pressure.

**Workflow-engine-as-source-of-truth.** The deployment answers coordination questions — what was decided, by whom, under what authority — by querying workflow execution history rather than substrate content. Violates A1.08's source-of-truth commitment directly; the composition specifies the same violation at the layer level rather than only at the level of an individual misread system.

**Orchestration-defines-cell-behavior.** Workflow conditions encode the cell's actual decision logic — if condition C, write value V; otherwise, write value W — placing the operative rule at the orchestration layer. Violates Component 3, and tends to make path retraceability impossible at the substrate side, because the trace runs through workflow-engine state rather than through substrate provenance per A1.07.

**Vendor-managed workflow logic as compliance authority.** A vendor's workflow management product is treated as the authoritative compliance system on the strength of its audit features, while the substrate is relegated to a passive store of execution outputs. Violates Component 4 (the mirror–source distinction) and tends to be combined with workflow-as-policy in deployments where vendor positioning reinforces the misreading.

**Workflow-conditions-as-rules.** A subtler version of orchestration-defines-cell-behavior: workflow conditions are written in rule-like form (tests, predicates, constraint specifications) and read by the deployment as if they were the operative orchestration rules. The conditions may be syntactically rule-shaped; that does not make them substrate-resident or A1.01-governable. Violates Component 2.

## 5. Operational decisions the composition produces

Composition-respecting deployments take four operational steps that distinguish them from layer-collapsing deployments. (i) Workflow definitions are documented as non-authoritative orchestration material at the architectural layer they occupy. (ii) Rules per A2.04 are verified as substrate-resident addressable content; the verification is performable by any participant exercising the inspect right. (iii) Cell-orchestration separation is verified by tracing one execution end-to-end: the workflow engine's record shows when the cell ran with what inputs, and the substrate shows what the cell decided, under which rule, with what rationale — two records, two layers, no double-counting. (iv) Vendor workflow products are mapped to the coordination-mechanism layer regardless of vendor positioning; the mapping is documented; the mapping is the architectural fact.

## 6. What the composition is NOT

The composition is not A1.15 alone. A1.15-alone tells a deployment that workflow engines and substrates occupy different layers; it does not specify which layer's content is authoritative. A deployment may correctly separate the layers and still place authoritative rules at the wrong layer.

The composition is not A1.08 alone. A1.08-alone tells a deployment that the substrate is authoritative for five categories of coordination state; it does not specify how the substrate's authority interacts with workflow-engine state at the orchestration boundary. A deployment may correctly treat the substrate as source of truth in the abstract and still misread workflow-engine state as substrate content for orchestration purposes.

The composition is not "compliance-driven workflow." Compliance-driven workflow systems may be architecturally compatible with CKS — when the workflow engine triggers cells whose rules sit in the substrate — or architecturally incompatible — when the workflow engine's definitions are read as the operative rules. The composition specifies which of the two a given deployment is.

The composition is not "policy-as-orchestration." A deployment that treats orchestration as where policy lives has placed authoritative content at the coordination-mechanism layer, which is the workflow-as-policy anti-pattern of §4.

## 7. Why the composition is load-bearing

The composition continues the A1.15 cluster by clarifying what A4.23 and A4.24 left implicit. A4.23 keeps the LLM's mediator role at the substrate side; A4.24 keeps path retraceability traceable through substrate provenance; A4.25 keeps the source-of-truth commitment intact at the orchestration boundary. Each of the three compositions answers a different question about how A1.15's layer distinctions interact with another foundational commitment, and the three together describe the architectural shape A4.26 will close as orchestration composition coherence.

The composition also extends A4.20's adjacency-vs-substrate distinction (A1.14 × A1.08) to the orchestration layer. A4.20 named the boundary between substrate and adjacent design objects (RAG indices, parametric memory, external structured memory) on the source-of-truth axis. A4.25 names the same boundary at the orchestration axis: the substrate is authoritative for orchestration rules; workflow engines and agent frameworks hold non-authoritative orchestration definitions. The two notes together describe the source-of-truth boundary as a property the substrate carries against multiple distinct adjacent layers, not only against generic data stores.

The composition is what distinguishes CKS from workflow-as-policy systems in deployment. A system that satisfies A1.15 alone (correct layer separation) but violates A1.08 at the orchestration layer (workflow definitions read as authoritative) is a workflow-as-policy system, not a CKS deployment. The composition makes the distinction operational rather than only definitional.

## 8. Operational test

A deployment maintains the orchestration source-of-truth distinction if and only if all three of the following are true at all times during the substrate's existence.

**Property e.1 — Workflow-non-authoritative.** No coordination question — what was decided, by whom, under what authority, with what rationale, what conflicts remain — is answered by reading workflow-engine definitions or workflow execution state. If a participant needs the answer, they read the substrate; if a workflow record is consulted, it is for execution history, not for the answer to a coordination question.

**Property e.2 — Rules-substrate-resident.** Every orchestration rule the system invokes during cell execution is addressable as substrate content per A2.46. The rule is inspectable, modifiable, and overridable under the human-governed commitment of A1.01; it does not live in workflow-engine configuration, vendor policy storage, or any location outside the substrate's source-of-truth scope.

**Property e.3 — Orchestration-trigger-not-determine.** Workflow engines decide *when* cells run and *with what inputs*; cell behavior — what the cell decides, what it writes, how it handles conflicts — follows from the substrate-resident rules the cell executes. A deployment where workflow conditions encode the cell's actual decision logic fails this property even if the conditions are reviewed and versioned.

A deployment that fails any of e.1–e.3 has placed authoritative content at the orchestration layer, and the composition has been violated. Such a deployment may still be operating a workflow engine and a substrate at separate layers; it is not maintaining the orchestration source-of-truth distinction.

## 9. One-sentence test

Read one rule the system invokes during cell execution; if the rule is addressable, inspectable, modifiable, and overridable as substrate content, and the workflow engine's role is to trigger the cell that executes the rule rather than to encode it, the deployment maintains the distinction.

## 10. Why naming the composition as standalone matters

The two commitments the composition pairs are each defended at length in the source paper, and a careful reader of either may believe the architectural property this note formalizes is implied by the commitment they have read. It is implied — when both commitments are held simultaneously and read against the same deployment. The reader who holds only one will produce systems that look governed at the layer they understand and degrade at the layer they did not. Naming the composition as a standalone formalization gives the property a name a deployment can be tested against, an anti-pattern set it can be audited against, and an operational test that distinguishes composition-respecting deployments from workflow-as-policy ones at the architectural level rather than the artifact level.

The A1.15 cluster has one more composition to formalize. A4.26 — A1.15 × A1.16 — closes the cluster by stating how the three preceding compositions cohere as a single architectural shape under the composition-requirements commitment, and what an orchestration-layer-aware multi-substrate deployment must satisfy for the shape to remain coherent at scale. A4.23, A4.24, and A4.25 supply the components; A4.26 supplies the closure.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Composition Pair: Orchestration Layer Distinctions × Substrate-as-Source-of-Truth — The Orchestration Source-of-Truth Distinction as Emergent Architectural Property.* May 7, 2026. ORCID: 0009-0004-8065-3235.
