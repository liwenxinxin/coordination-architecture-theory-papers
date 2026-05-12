# Mechanism Priority and Sequencing: Formalizing the Operational Scheduling Framework for Three Concurrent Evolution Mechanisms in the CKS Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The CKS pattern's three evolution mechanisms — instinct evolution (mutation-like), DNA evolution (directed selection), and action-feedback evolution — operate concurrently but at different operational cadences and under priority relationships that govern their interaction. This note formalizes the mechanism priority and sequencing framework: the operational scheduling specification that allows deployments to reason coherently about three mechanisms running at the same time. The three mechanisms each have a cadence determined by their trigger type: mutation follows external LLM vendor update cadence and is not deployment-controlled in timing; directed selection follows internal governance deliberation cadence and is fully deployment-controlled; action-feedback follows evidence accumulation cadence and is operationally-determined by throughput. The one architecturally specified priority relationship is high-stakes priority through pinning: in high-stakes contexts, directed selection has priority over mutation through substrate-resident pinning rules. Outside high-stakes contexts, concurrent operation is the default, with no fixed priority between directed selection and action-feedback. Deployments may optionally configure sequencing constraints for specific operational scenarios. All priority rules are substrate-resident authoritative content authored per the Paper 1 rule-authoring pattern. The framework is the third of five decompositions of B1.12 (three evolution mechanisms in productive tension), following B2.56 (integrating frame) and B2.57 (productive tension operational specification).

## 1. Why mechanism priority and sequencing requires standalone formalization

B2.56 established the integrating frame for the three evolution mechanisms: that instinct evolution, DNA evolution, and action-feedback evolution operate concurrently in productive tension, each targeting architecturally separated layers, with governance integrating the results. B2.57 formalized productive tension operationally — specifying precisely what it means for mechanisms to be in tension and what governance structures prevent that tension from becoming conflict. B2.58 addresses the next decomposition question: given that three mechanisms operate concurrently, what is the scheduling framework that governs their interaction?

The question is not trivial. Each mechanism operates at its own rate, triggered by a different kind of event. Mutation fires when an LLM vendor releases an update; a deployment does not choose the release schedule and cannot prevent it. Directed selection fires when humans deliberate and authorize DNA changes; a deployment controls this timing entirely. Action-feedback fires when evidence from the Action layer accumulates to a threshold sufficient to generate meaningful proposals; the timing depends on operational throughput and the proposal-generation logic in the substrate. Three mechanisms, three trigger types, three cadences — operating concurrently on overlapping content.

Without a scheduling framework, concurrent mechanisms would produce unmanageable operational situations: mutation arriving mid-directed-selection review cycle; action-feedback proposals accumulating while a mutation integration is pending verification; high-stakes cells whose behavior could be changed by mutation before pinning rules are applied. The scheduling framework is the architectural answer to how a deployment manages this.

This note formalizes the scheduling framework as a standalone derivation because the framework is architecturally distinct from the mechanisms themselves and from the productive tension between them. B2.56 names the mechanisms and their tension. B2.57 formalizes the tension. B2.58 formalizes the scheduling. Each is a separable architectural commitment.

The note occupies the fifty-eighth position in Phase B2 of Series B — the third of five notes in the B1.12 decomposition cluster (B2.56, B2.57, B2.58, B2.59, B2.60) — and establishes prior art for the scheduling-framework aspect of concurrent multi-mechanism AI system evolution.

## 2. The architectural framework precisely stated

The mechanism priority and sequencing framework has five components.

**Three mechanism-specific cadences.** Each mechanism has a cadence determined by its trigger type:

- *Mutation cadence* is externally triggered. Mutation fires when an LLM vendor releases a new model version or when a substrate-platform infrastructure upgrade becomes available. The deployment does not author or control the vendor's release schedule. The deployment may delay integration — pending verification gate passage per the governance pattern for instinct integration — but it cannot control when the trigger arrives. Mutation cadence is therefore external and asynchronous with respect to deployment governance schedules.

- *Directed selection cadence* is internally triggered. DNA evolution fires when human governance deliberates and authorizes DNA layer changes. The timing is fully deployment-controlled: weekly review cycles, quarterly architectural reviews, event-triggered reviews — whatever governance schedule the deployment configures. No external actor compels a directed selection round; it fires when humans with appropriate authority choose to act.

- *Action-feedback cadence* is evidence-triggered. Action-feedback evolution fires when the Action layer accumulates sufficient evidence to generate meaningful proposals for DNA layer refinement. The cadence depends on operational throughput: high-throughput cells accumulate evidence faster and generate proposals more frequently; lower-throughput cells accumulate more slowly. The deployment determines the evidence threshold and the proposal-generation logic, but the trigger itself is operational — evidence-driven rather than schedule-driven.

**High-stakes priority through pinning.** In high-stakes contexts, directed selection has architectural priority over mutation through pinning. Pinning is the substrate-resident mechanism by which high-stakes cell behavior is committed to the reasoning layer regardless of how capable instinct becomes. A pinned cell's behavior cannot be changed by mutation arriving from upstream: the verification and routing rules that govern mutation integration will not accept mutations affecting pinned cell behavior without directed-selection-level governance authorization. This is the one architecturally specified priority relationship. It is not a value hierarchy; it is a structural constraint that ensures high-stakes decisions continue to go through the reasoning layer under human governance.

**Concurrent operation as default.** Outside high-stakes pinning contexts, the three mechanisms operate concurrently with no fixed priority relationship between them. Directed selection and action-feedback can both produce DNA layer changes at the same time. Mutation integration can proceed while a directed selection round is in progress. Mechanisms do not wait for each other by default. This is the intended default because the mechanisms target architecturally separated content and trigger at different cadences; coordination is the exception, not the rule.

**Optional sequencing constraints.** Deployments may configure sequencing constraints for specific operational scenarios where concurrent operation is not appropriate. Examples: complete mutation integration and verification before evaluating pending action-feedback proposals (so that proposal evaluation reflects the latest instinct capability); complete a directed selection round before admitting mutation integration (so that the DNA layer is stable during a governance review cycle). Sequencing constraints are deployment configuration, not architectural requirements. Their absence is the architectural default.

**Substrate-resident priority rules.** All priority relationships — high-stakes pinning and any deployment-configured sequencing constraints — are authored as substrate-resident rules per the Paper 1 rule-authoring pattern. Priority rules are authoritative content: they are governed, inspectable, modifiable, and testable. No priority relationship exists except through authored rules. Unspecified priority situations resolve to the concurrent default.

## 3. What makes mechanism priority and sequencing architecturally distinctive

The contrast with conventional AI evolution is instructive. Conventional AI system evolution is typically sequential and single-mechanism: train a new model version, evaluate the version, deploy the version, deprecate the prior version. Scheduling is trivial because there is one mechanism and it operates in discrete phases that do not overlap. If a second mechanism exists — such as prompt engineering or fine-tuning — the mechanisms typically operate at different organizational layers with no architectural integration.

The CKS scheduling framework differs on two axes. First, three mechanisms operate concurrently by architectural commitment. The integration of mutation, directed selection, and action-feedback is not a product of the particular mechanisms chosen; it is the architectural design. Scheduling complexity is therefore inherent, not accidental. Second, the scheduling framework is itself architecturally specified: it is not ad-hoc deployment policy but substrate-resident rules authored under governance, subject to the same inspection and override rights that govern all substrate content.

Cadence differences reflect mechanism character rather than scheduling convenience. Mutation cadence is externally determined because the mechanism's defining property is that it arrives from upstream — capability changes the deployment does not author. Directed selection cadence is internally determined because the mechanism's defining property is that it operates under governance-defined goals on a human-chosen timeline. Action-feedback cadence is evidence-determined because the mechanism's defining property is that it closes the loop from operational experience. Understanding cadences as reflections of mechanism character, rather than as scheduling parameters to optimize, is what makes coherent deployment management possible: each mechanism is managed on the terms appropriate to its nature.

## 4. Inherited Paper 1 commitments

Four Paper 1 commitments are directly load-bearing for the scheduling framework.

**Rule authoring (Paper 1 §A2.04).** Priority rules are authored rules. The rule-authoring pattern specifies how humans write orchestration rules that govern cell-level and deployment-level behavior. Priority and sequencing rules are a category of orchestration rules: they specify, under what conditions, which mechanism constraints are active. The authoring pattern's properties — that rules are substrate-resident, human-authored, and modifiable — hold for priority rules without modification.

**Authoritative content (Paper 1 §A2.46).** Priority rules are Category 4 authoritative content: content that governs system behavior and whose integrity is architecturally protected. Authoritative content cannot be overridden by LLM output or automated processes without human authorization. Priority rules authored under this commitment are therefore stable unless a human with appropriate authority modifies them.

**Human governance (Paper 1 §A1.01).** The three rights — inspect, modify, override — apply to priority rules as to all substrate content. A deployment operator can inspect the active priority rules at any time, modify them when governance circumstances change, and override any priority determination that has produced an incorrect result. Governance of the scheduling framework is exercised through these rights, not through specialized mechanisms.

**Rule conflict resolution (Paper 1 §A6.01).** Concurrent mechanism operation can produce situations where two mechanisms have independently produced DNA layer changes that conflict. Rule conflict resolution applies: conflicts are preserved as explicit substrate content rather than silently resolved, and governance processes address them. The scheduling framework does not prevent concurrent evolution from generating conflicts; it ensures conflicts are handled through governed resolution rather than silent overwrite.

**Determinism (Paper 1 §A1.10).** Given authored priority rules and the relevant inputs — the current deployment context, the high-stakes classification of cells, the active sequencing constraints — the scheduling framework's behavior is deterministic. The same priority rules applied to the same context produce the same scheduling decisions. This property enables testability and retrospective inspection.

## 5. Cadence specifics

Understanding each cadence in operational terms equips deployment management.

*Mutation cadence in practice.* An LLM vendor releases a new model version. The deployment's mutation governance process activates: verification gates per the instinct integration governance pattern initiate parallel-run evaluation; routing rules for the new model are evaluated; pinning reviews confirm whether high-stakes cell classifications remain appropriate given the new instinct capability. The deployment cannot choose when this trigger arrives. It can configure how long the integration verification process takes before the new instinct layer becomes operative — typically bounded by the governance commitment to timely integration — but it cannot prevent the trigger or its eventual resolution.

*Directed selection cadence in practice.* A weekly governance review meeting produces an authorized DNA change: a new orchestration rule, a revised schema, a clarified policy. The change is applied to the substrate under the authority architecture. The next scheduled review occurs on its configured schedule. An event-triggered review fires when a significant operational incident or strategic shift warrants unscheduled governance attention. The deployment controls all of these timings through its governance configuration.

*Action-feedback cadence in practice.* A high-throughput cell accumulates Action layer evidence over several hundred operations. The proposing substrate configured for that cell reaches its evidence threshold and generates a proposal for DNA layer refinement — perhaps a scope reduction informed by usage patterns, perhaps a routing optimization informed by accumulated inefficiency. The proposal enters the human-mediated approval process. The cadence at which proposals arrive is determined by throughput; the cadence at which they are reviewed and approved is determined by governance configuration.

## 6. Operational implications

**Configure priority rules first.** Before a deployment admits concurrent mechanism operation, it should author its priority rules. At minimum: configure pinning for all cells classified as high-stakes. Priority rules for sequencing constraints, if desired, should be authored for the specific scenarios where concurrent operation creates management problems.

**High-stakes pinning is foundational.** The one architecturally specified priority relationship is also the one that most directly affects safety properties. Deployments should treat pinning rule configuration as a first-order governance task, not an optional optimization. A cell is either pinned or subject to mutation; there is no intermediate state.

**Manage mutation integration timing.** Because mutation arrives on external cadence, deployments benefit from maintaining a mutation integration queue: mutations pending verification are held in governed state while verification proceeds. The integration queue state is substrate content, inspectable and auditable. Integration decisions should be governed, not automated.

**Standard review cadences.** For directed selection and action-feedback, governance review cadences should be configured explicitly rather than left implicit. The scheduling framework provides no default cadences for internally and evidence-triggered mechanisms — that is precisely what "deployment-controlled" and "operationally-determined" mean. Explicit configuration produces inspectable, modifiable governance schedules.

**Testability through inspection and replay.** Because priority rules are substrate-resident authoritative content and evolution scheduling is deterministic given the rules, priority and sequencing decisions are testable through inspection and replay. A deployment can ask: given these priority rules, what would the scheduling framework have done with this evolution event? Retrospective inspection of evolution decisions is available for all evolution events whose triggering conditions and active priority rules are preserved in substrate state.

## 7. Limits

**Not prescribing fixed cadences.** The scheduling framework does not specify how frequently mutation integration should occur, how often directed selection review cycles should happen, or what evidence threshold should trigger action-feedback proposals. These are deployment configuration decisions that depend on operational context, risk tolerance, and governance capacity.

**Not suppressing lower-priority mechanisms.** Priority does not mean lower-priority mechanisms are deactivated or suppressed. All three mechanisms operate. High-stakes priority through pinning constrains what mutation can change for pinned cells; it does not prevent mutation from operating on unpinned cells or prevent directed selection from occurring on any cell. Priority relationships constrain specific interactions, not overall mechanism operation.

**Cadence differences are not value hierarchies.** The fact that mutation cadence is externally triggered and directed selection cadence is internally controlled does not imply that directed selection is more important than mutation, or that mutation is less trusted. Cadences reflect trigger type, not value. Both mechanisms contribute capabilities the other cannot; the productive tension between them is the architecture's central evolutionary property.

**Concurrent is default, not requirement.** Deployments may configure explicit sequencing constraints if concurrent operation creates unmanageable situations. The default of concurrent operation is not a requirement that sequencing is prohibited. The architecture permits sequencing constraints as deployment-configured options precisely because some operational contexts benefit from sequential evolution event management.

**High-stakes pinning is the one architectural constraint.** All other priority relationships are deployment-configurable. There is no architectural hierarchy beyond pinning. Deployments that have no high-stakes cells — or that have not yet classified any cells as high-stakes — operate with the concurrent default and no architectural priority relationships active. The scheduling framework is not a complex hierarchy; it is a minimal framework anchored to one architectural constraint with deployment-configurable extensions.

## 8. One-sentence test

A deployment instantiates the mechanism priority and sequencing framework if and only if: (a) mutation integration is governed separately from directed selection and action-feedback, with verification gates controlling admission; (b) all cells classified as high-stakes are pinned, so that mutation cannot change their behavior without directed-selection-level governance authorization; (c) all priority and sequencing rules are substrate-resident authoritative content authored under the Paper 1 rule-authoring pattern; and (d) the concurrent default is operative for all mechanism interactions not governed by authored priority rules.

## 9. Position in the B1.12 decomposition and Phase B2 progression

B2.56 established the integrating frame: three mechanisms, three layers, concurrent operation, governance integration. B2.57 formalized productive tension operationally: what tension means, what it takes for tension to remain productive rather than becoming conflict, and how governance maintains the productive relationship. B2.58 formalizes the scheduling framework: the operational specification that makes concurrent multi-mechanism evolution manageable.

B2.59 will address cross-mechanism governance — the governance structures that operate across rather than within individual mechanisms: how governance authority is distributed when mechanisms interact, how concurrent evolution events are governed jointly, and what the authority architecture looks like when all three mechanisms are active simultaneously. B2.60 will address three mechanisms verification — the operational tests that confirm a deployment has correctly instantiated the full three-mechanism framework as described across B2.56 through B2.59.

After B2.60 completes the B1.12 decomposition cluster, Phase B2 continues into the B1.13 mutation decomposition (approximately B2.61 onward), which will formalize mutation governance patterns in progressively finer-grained operational terms.

Naming mechanism priority and sequencing as a standalone derivation establishes prior art for the scheduling-framework aspect of multi-mechanism concurrent AI evolution. The specific conjunction — three mechanism-specific cadences differentiated by trigger type, high-stakes priority through pinning as the one architectural constraint, concurrent default, optional sequencing constraints, substrate-resident authoritative priority rules — is what this note places in the public record. Subsequent work that instantiates this conjunction, or any substantial component of it, without independent development encounters this prior art.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Mechanism Priority and Sequencing: Formalizing the Operational Scheduling Framework for Three Concurrent Evolution Mechanisms in the CKS Pattern.* May 12, 2026. ORCID: 0009-0004-8065-3235.
