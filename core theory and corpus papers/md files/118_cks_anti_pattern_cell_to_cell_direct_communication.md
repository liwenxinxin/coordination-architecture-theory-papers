# Anti-Pattern: Cell-to-Cell Direct Communication — Standalone Formalization of the Failure Mode Where Cells Communicate Directly Without Substrate Mediation, Bypassing the Substrate-Cell Boundary and Breaking Path Retraceability in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one architectural failure mode — *cell-to-cell direct communication* — as a standalone anti-pattern, so that downstream deployments and reviewers can identify, distinguish, and correct it without ambiguity.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern commits to two architectural properties that fail simultaneously when cells communicate directly with each other rather than through substrate: the substrate-cell boundary, which carries the commitment that substrate is the medium for inter-cell coordination, and path retraceability, which carries the commitment that retraceable paths flow only through substrate. *Cell-to-cell direct communication* names the deployment configuration where these commitments break through the same operational mechanism — inter-cell flow that bypasses substrate. The configuration is operationally common in 2024–2026 workflow-engine and agent-framework deployments, where direct data passing between steps is positioned as a feature, and the pattern naturally extends to CKS-style deployments unless the architectural distinction between *triggering cells to read and write substrate* and *passing data directly between cells* is preserved. This note formalizes the anti-pattern by stating its four operational components, the CKS commitments it violates, the failure modes it produces, the architectural correction, the four legitimate orchestration patterns it must not be conflated with, and the operational test by which any deployment can be classified.

## 1. Why a standalone formalization is needed

The substrate-cell boundary commits to architectural separation between substrate (state and inter-cell medium) and cells (behavior). Within that boundary's operational decomposition, one specific commitment holds that substrate is the medium for inter-cell coordination — cells coordinate by writing to and reading from substrate, not by communicating directly. Path retraceability commits to a retraceable trail across substrate writes; within its decomposition, one specific commitment holds that retraceable paths flow only through substrate.

Cell-to-cell direct communication is the failure mode where these commitments break together. Cell A produces output, sends it directly to Cell B (via API call, message queue, function pipeline, shared memory, or workflow-engine-mediated handoff), and Cell B receives and processes the output without the inter-cell flow ever passing through substrate. The boundary is bypassed in the inter-cell direction; the retraceable trail breaks at the moment communication crosses cell boundaries; two foundational commitments fail through one operational configuration.

The motivating scenarios are everyday: workflow engines that pass data directly between cell invocations; cells calling each other's APIs synchronously; message-queue-based handoffs; cell pipelines where one cell's return value becomes the next cell's input; framework-managed shared memory between cells. Each is operationally attractive because workflow engines and agent frameworks commonly support direct data passing as a default integration pattern.

This note also closes a trio at the substrate-cell boundary's foundational level. Cell-as-substrate (cells holding state outside substrate) collapses the boundary by misallocating state; substrate-as-cell (substrate executing behavior) collapses it by misallocating behavior; cell-to-cell direct communication bypasses it by routing coordination outside the medium it requires. Without all three formalized as standalone, the boundary's anti-pattern coverage is incomplete.

## 2. The anti-pattern, defined precisely

A deployment exhibits cell-to-cell direct communication when any of the following four operational components is present.

**(a) Direct API calls between cells.** Cell A invokes Cell B's interface synchronously with arguments derived from substrate or from Cell A's internal processing; Cell B returns a result that Cell A uses, optionally writing some downstream artifact to substrate. The request and response flow between cells without traversing substrate.

**(b) Message-queue-based cell-to-cell handoffs.** Cell A publishes a message to a queue; Cell B subscribes and receives it; the message contains coordination data — task assignments, intermediate computations, decision outputs — that flows from Cell A to Cell B without corresponding substrate writes recording the flow. The queue operates as a side-channel for inter-cell coordination, distinct from any role it plays as an event source derived from substrate state.

**(c) Function-pipeline cell chains.** Cells are arranged in a pipeline where one cell's output is immediately the next cell's input. The pipeline mechanism — workflow runtime, code-level chaining, declarative DAG runner — passes the result to the next cell as input; the pipeline handles inter-cell data flow directly without writing through substrate at each stage.

**(d) Shared-memory cell coordination.** Cells coordinate through shared memory, in-memory caches, framework-managed scratchpads, or any non-substrate state store accessible to multiple cells. The shared store is operationally a non-substrate medium for inter-cell coordination.

The four components together define the anti-pattern. A deployment exhibiting any one of them partially exhibits it; a deployment exhibiting all four exhibits it fully. The anti-pattern is configuration-shaped, not implementation-shaped: any operational arrangement that produces inter-cell coordination flow outside substrate satisfies the definition, regardless of the specific technology used.

## 3. Which CKS commitments are violated

Cell-to-cell direct communication violates two foundational commitments directly and several others by cascade.

**The substrate-cell boundary** is directly violated. Within its operational decomposition, the specific commitment that substrate is the medium for inter-cell coordination is the one most directly broken: the medium commitment fails when cells coordinate without it.

**Path retraceability** is directly violated. Within its decomposition, the specific commitment that retraceable paths flow only through substrate is the one most directly broken: communication flowing through paths that do not pass through substrate cannot be retraced.

**Provenance metadata** is operationally compromised. The provenance fields specified for substrate writes — actor, basis, rule version, timestamp, source identifiers, derivation chain — may not be generated for inter-cell flow because no substrate writes record it. Provenance has gaps at every cell-to-cell boundary the anti-pattern produces.

**The four accountability questions** — what was decided, by whom, under what authority, with what rationale — are operationally compromised. The questions are answerable when substrate records the answers; decisions made via inter-cell flow are not substrate-recorded, and so the questions cannot be answered from substrate alone.

**Three further commitments are extended-violated.** AI-as-substrate-mediator fails at the inter-cell boundary because the architectural pattern that LLM-mediated outputs flow through substrate fails when those outputs flow directly to other cells, even when the mediator role within each cell is preserved. The determinism contract fails because cell-to-cell direct communication may introduce non-determinism not visible in substrate state — message ordering across queues, async delivery races, in-flight transient state, pipeline retry semantics — categories the contract does not allow. The composition requirements fail at the inter-cell boundary: cross-boundary addressable provenance is not addressable across boundaries the anti-pattern produces, and the AI-as-mediator-at-every-layer requirement is bypassed at the inter-cell layer.

## 4. The failure mode

Cell-to-cell direct communication produces deployments where inter-cell coordination flows are operationally invisible to substrate. The downstream consequences are specific.

The retraceable trail breaks at inter-cell boundaries. The trail records substrate state changes; coordination flows that produce no substrate state changes leave it incomplete at the moment they cross the inter-cell boundary, so decisions made via inter-cell flow cannot be retraced. The accountability questions cannot be answered from substrate, since an analyst attempting to answer them will find gaps where inter-cell coordination occurred. Provenance fragments correspondingly: even when substrate writes occur after inter-cell flow, the provenance fields may be incomplete because the intermediate handoffs are not recorded.

The inspect right is operationally compromised. Humans exercising the inspect right inspect substrate; inter-cell communication flowing outside substrate is not visible to inspection. Humans cannot see what cells are coordinating about, what data is flowing between them, or what decisions are being made through inter-cell flow.

Emergent inter-cell coordination becomes invisible to substrate. Cells communicating directly may form coordination patterns that no substrate state reflects; the deployment may operate with complex inter-cell coordination while substrate shows only fragmentary indications. Pipeline-error cascades go unrecorded along the same path: errors propagate through stages without being substrate-recorded at each stage, becoming visible only at the final substrate write.

Workflow-engine-direct-handoff masks substrate bypass. Workflow engines that pass data directly between cells may appear architecturally legitimate (workflow engines themselves are not anti-patterns) while operationally enabling cell-to-cell direct communication. The architectural distinction — workflow engines triggering cells (legitimate) versus workflow engines passing data directly between cells (anti-pattern) — is operationally subtle.

Composition coherence breaks. Hybrid compositions require substrate as the architectural anchor; cell-to-cell direct communication establishes flows outside substrate. When the deployment composes with adjacent components, the coherence is compromised because some inter-cell flows are substrate-invisible, and the cross-boundary addressable-provenance and AI-as-mediator-at-every-layer requirements fail at exactly the boundaries the anti-pattern produces.

## 5. The architectural correction

The correction operates through three commitments together.

**Substrate as inter-cell medium.** All inter-cell coordination must flow through substrate. Cell A writes its output to substrate; Cell B reads its input from substrate; the substrate is the unique medium for inter-cell coordination, and no direct cell-to-cell paths are permitted regardless of orchestration mechanism.

**Substrate-only paths.** Retraceable paths flow only through substrate. Every coordination decision must have a substrate path that can be retraced; inter-cell flow that bypasses substrate cannot be retraced and is therefore architecturally disallowed.

**Workflow engines as cell triggers, not data routers.** Workflow engines may legitimately orchestrate cell invocations, but must do so by triggering cells to read from and write to substrate rather than by passing data directly between cell invocations. The orchestration concern (when to invoke which cell) and the coordination concern (how data flows between cells) are architecturally separated; the engine handles the first, substrate handles the second.

A correctly architected deployment additionally maintains a substrate-mediation audit, operationally verifying that every inter-cell coordination has corresponding substrate writes and reads. It distinguishes cell-internal computation (a single cell performs work, including potentially complex internal logic) from inter-cell communication (work flows from one cell to another), the architectural commitment applying only to the latter. And it preserves Pattern A consultation as legitimate, recognizing that cell-to-adjacent-component consultation differs architecturally from cell-to-cell coordination.

## 6. What the anti-pattern is NOT

Four legitimate orchestration patterns are commonly conflated with cell-to-cell direct communication. Distinguishing them is the operationally critical clarification.

**Not workflow engines that trigger cells.** A workflow engine that orchestrates cell invocations by triggering Cell A, allowing Cell A to read from and write to substrate, then triggering Cell B to read from substrate (now containing Cell A's output) and write to substrate, is legitimate. The workflow engine is the orchestration mechanism; the substrate is the inter-cell medium; the architectural concerns are separated. The anti-pattern arises specifically when the workflow engine becomes the inter-cell medium itself — when the engine takes Cell A's return value and passes it to Cell B as an argument without writing through substrate. The two patterns are mechanically similar from the engine's perspective but architecturally distinct: the legitimate one preserves substrate-as-medium; the anti-pattern bypasses it. Reviewers should look specifically at whether each cell invocation reads its inputs from and writes its outputs to substrate, or whether the engine's data-passing facilities are doing that work. This is the most commonly drifted-into form of the anti-pattern in 2024–2026 deployments.

**Not agent frameworks that execute cells.** Agent frameworks that execute CKS cells under orchestration rules are legitimate when the executed cells read from and write to substrate. The anti-pattern arises when the framework's inter-step memory — scratchpad, conversation buffer, framework-managed state — operates as the medium for inter-cell coordination. Frameworks are not themselves anti-patterns; specific framework configurations that route inter-cell flow through framework memory are.

**Not control planes that authorize substrate access.** Control planes operate at the access-authorization layer (who may read or write what substrate content, under what conditions). Cell-to-cell direct communication operates at the inter-cell-flow layer (whether coordination passes through substrate at all). The two architectural concerns address different problems and should not be conflated.

**Not cells consulting adjacent components.** Cells consulting adjacent AI components — RAG indexes, vector databases, fine-tuned LLMs — under Pattern A are legitimate when the cell maintains substrate authority and records provenance for what was consulted and used. The architectural commitment is that *cell-to-cell* coordination requires substrate; *cell-to-adjacent-component* consultation is a different pattern with different requirements. The anti-pattern is specifically about coordination between CKS-internal architectural units, not about consultation of components outside the CKS architecture.

## 7. Why cell-to-cell direct communication is load-bearing as an anti-pattern

The anti-pattern is load-bearing because it closes the substrate-cell-boundary trio with cell-as-substrate and substrate-as-cell, violates two foundational commitments simultaneously through a single operational mechanism, is operationally common in workflow-engine and agent-framework deployments, cascades into accountability and inspection failures, is operationally subtle in complex deployments because the distinction between triggering cells and passing data between cells may not be apparent without specific review, and has a clear architectural correction operating through three named commitments.

## 8. Operational test

A deployment exhibits cell-to-cell direct communication if any of the following four configuration tests is true at any time during the deployment's existence: (a) cells call other cells' APIs directly with arguments and the call returns a result without substrate mediation; (b) cells communicate through message queues containing coordination data that flows between cells without substrate writes recording the flow; (c) cells operate in pipelines where one cell's output is immediately the next cell's input without substrate mediation between stages; (d) cells coordinate through shared memory or in-memory caches that operate as inter-cell coordination media outside substrate.

Three sharpening properties operationalize the test as a deployment review.

**Substrate-mediation property.** Trace every inter-cell flow in the deployment. Verify operationally that each flow has corresponding substrate writes (the producing cell's output) and substrate reads (the consuming cell's input). Flows lacking either component fail the property.

**Inter-cell-trail property.** Select an inter-cell coordination outcome — any decision or artifact that involved more than one cell. Verify that the trail from the initial substrate state to the outcome is retraceable through substrate alone, without requiring inspection of inter-cell flows external to substrate. Trails that require inspecting non-substrate flows fail the property.

**Accountability-completeness property.** Select decisions made in the deployment. For each decision, ask the four accountability questions and attempt to answer them from substrate. Decisions whose answers require inter-cell flow inspection fail the property.

A deployment that fails any of (a)–(d) and any of the three sharpening properties exhibits the anti-pattern; the architectural correction in §5 specifies the operational changes required to bring the deployment into compliance.

## 9. The one-sentence test

If a deployment's cells communicate directly with each other — through API calls, message queues, function pipelines, shared memory, or workflow-engine-direct handoffs — without the inter-cell flow passing through substrate, the deployment exhibits cell-to-cell direct communication; the substrate-cell boundary's commitment to substrate-as-inter-cell-medium and path retraceability's commitment to substrate-only paths both fail, and the four accountability questions are unanswerable from substrate alone for any decision made via inter-cell flow.

The one-sentence test names the most operationally distinctive properties — direct inter-cell flow, non-substrate medium — for any specific deployment. The four-component specification in §2 plus the operational test in §8 provide the full architectural definition for cases requiring detailed analysis.

## 10. Why naming the anti-pattern as standalone matters

Implementations under pressure to deliver multi-cell AI workflows consistently default to cell-to-cell direct communication because workflow engines and agent frameworks commonly support direct data passing. The drift is steady: audiences understand "we use a workflow engine to chain our AI cells" as standard architecture without recognizing the consequence — inter-cell flow may bypass substrate, the retraceable trail breaks at the cell-to-cell boundaries the chain produces, and decisions made along the chain are not substrate-recorded.

Naming cell-to-cell direct communication as a standalone anti-pattern — with the four operational components, the violations, the failure mode, the architectural correction, the four adjacent-pattern distinctions, the operational test, and the one-sentence test — gives downstream readers a precise specification of the failure mode and its correction. With cell-as-substrate and substrate-as-cell, this note completes the substrate-cell-boundary anti-patterns at the boundary's foundational level. Subsequent anti-pattern notes formalize failure modes at additional foundational commitments.

---

## Source

Li, Wenxin. *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. The architectural commitments treated here are introduced in §2.1 (substrate-cell boundary), §3.1 (substrate-as-source-of-truth and path retraceability), §4.1 (substrate authority over coordination), §5 (path retraceability formalization), and §11.3 (substrate-cell separation, substrate as inter-cell medium).

## Cite as

Li, Wenxin. *Anti-Pattern: Cell-to-Cell Direct Communication — Standalone Formalization of the Failure Mode Where Cells Communicate Directly Without Substrate Mediation, Bypassing the Substrate-Cell Boundary and Breaking Path Retraceability in CKS.* May 6, 2026. Derivation note in the CKS series.
