# Autonomy Is the Failure: The LLM-as-Autonomous-Agent Anti-Pattern in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a standalone publication, the anti-pattern in which the LLM operates as an autonomous decision-maker on substrate — making its own decisions about what substrate operations to perform, what tasks to address, and what next steps to take, outside the mediator role that the CKS pattern's AI-as-substrate-mediator commitment specifies.

## Abstract

The CKS pattern's AI-as-substrate-mediator commitment specifies the LLM's role as a substrate-mediator within cells under orchestration rules. This note formalizes, as standalone prior art, the failure mode in which the LLM instead operates as an autonomous decision-maker on substrate — directing its own behavior, choosing its own next steps, and effecting substrate state through autonomous reasoning rather than through orchestration-rule mediation. Common operational forms include agent-loop architectures, ReAct patterns, autonomous task execution, multi-step LLM reasoning where each step is LLM-chosen, and "cognitive layer" framings. The note specifies the anti-pattern's four operational components, identifies the multiple AI-as-substrate-mediator decomposition properties it violates simultaneously, traces the failure mode, states the architectural correction, distinguishes the anti-pattern from four adjacent legitimate patterns, and provides an operational test with three sharpening properties. The autonomous-agent failure is the first of three formalizations of AI-as-substrate-mediator failure modes; the others address the LLM as terminal producer and the LLM as source of truth.

## 1. Why a standalone formalization is needed

The AI-as-substrate-mediator commitment (§4.1, §4.2 of the source paper) specifies the LLM's role within the CKS pattern as a substrate-mediator within cells under orchestration rules. The commitment decomposes operationally into properties governing what the LLM reads and writes, what state it does and does not hold, what authority it does and does not exercise, and how its substrate-affecting outputs are recorded. The commitment names the role positively. It does not enumerate the failure modes by which a deployment may operate the LLM outside the role.

This note formalizes one such failure mode: the configuration in which the LLM operates as an autonomous decision-maker on substrate — directing its own behavior, choosing its own next steps, and effecting substrate state through autonomous reasoning rather than through orchestration-rule mediation.

Four considerations motivate treating the failure mode as standalone. First, agentic AI architectures — agent loops, ReAct patterns, chain-of-thought-with-action sequences, autonomous task execution, "cognitive layer" framings — are the dominant 2024–2026 paradigm for "advanced" AI systems; deployments under product pressure default to these patterns, and when applied to substrate-affecting behavior, the AI-as-substrate-mediator architecture fails systematically. Second, the failure violates several mediator-role properties simultaneously: the integrating frame, the write-under-rules property, the no-authority property, the rule-authoring-as-governance moment, and the no-out-of-substrate-state property. Third, the prior-art posture: patentable derivations focused on autonomous AI agents for coordination, agentic AI architectures with substrate state, or "cognitive layer" AI systems are substantially more defensibly contested when the anti-pattern is publicly formalized as standalone. Fourth, the position within a trio: the autonomous-agent anti-pattern opens a three-note cluster covering AI-as-substrate-mediator failure modes, alongside LLM-as-terminal-producer and LLM-as-source-of-truth in subsequent notes; together with the earlier LLM-gatekeeping anti-pattern (in which the LLM operates between humans and substrate, gating human access), they cover the foundational mediator-role failure modes. Autonomous-agent is the "what does the LLM do on substrate" axis; gatekeeping is the "where does the LLM sit between humans and substrate" axis — sibling violations at different architectural points.

## 2. The anti-pattern, defined precisely

A deployment exhibits LLM-as-autonomous-agent over substrate if its operational configuration includes any of the following four components.

**(a) LLM-driven decision-making about substrate operations.** The LLM decides which substrate operations to perform — what to read, what to write, what to query, what to compute. The decisions flow from the LLM's autonomous reasoning rather than from orchestration-rule authorization. The architectural locus of decision is the LLM's reasoning, not a rule that the LLM applies.

**(b) Autonomous next-step selection without rule mediation.** In multi-step coordination, the LLM autonomously chooses the next step. Agent-loop architectures in which each iteration's action is LLM-chosen exhibit this component, as do ReAct-style action selection, chain-of-thought-with-action loops, and recursive agent-call structures. The architectural commitment to rule-mediated step selection fails because the loop is LLM-directed.

**(c) LLM-initiated substrate writes without orchestration-rule authorization.** The LLM writes to substrate based on its autonomous decisions, not under rule authorization. The writes may carry nominal provenance (the LLM as the actor) but lack the rule-mediated provenance that the architecture requires — there is no orchestration rule whose application authorized the write.

**(d) Agent-loop architectures where the LLM directs its own behavior.** The deployment runs agent loops — ReAct, chain-of-thought-with-action, recursive agent calls, autonomous task-execution frameworks — in which the LLM iteratively decides what to do next on substrate. The cells-under-rules commitment is systematically bypassed because the loop's control flow is LLM-directed rather than rule-directed.

A deployment exhibiting any one of (a)–(d) partially exhibits the anti-pattern; a deployment exhibiting all four exhibits it fully. The four components define the failure mode architecturally, independent of which agentic AI framework or product the deployment uses.

## 3. Which CKS commitments are violated

The anti-pattern violates the AI-as-substrate-mediator commitment across multiple decomposition properties simultaneously.

*Directly violated.* The mediator role's integrating frame fails: the frame requires the LLM to operate within cells under rules, and autonomous-agent operation has the LLM directing its own behavior outside cells. The write-under-orchestration-rules property fails: writes flow from autonomous decisions, not rule authorization. The no-authority-over-substrate property fails: autonomous decision-making about substrate operations *is* exercising authority over substrate.

*Bypassed systematically.* The rule-authoring-as-governance moment fails to discharge its architectural function: rules cannot direct autonomous behavior because the agent does not consult them. The canonical moment at which humans exercise the modify right by editing rules is operationally bypassed.

*Operationally implicated.* The no-out-of-substrate-state property is implicated: autonomous agents typically maintain agent state, agent memory, or persisted context windows to support reasoning across iterations, and that agent state often holds substrate-relevant content. The substrate-affecting-outputs-recorded-with-attribution property is operationally compromised: autonomous-agent outputs may carry the LLM as nominal actor but lack association with an orchestration rule.

*Cascade implications.* The human-governed commitment is extended-implicated: humans cannot govern through the architectural mechanism, because the modify right cannot be exercised against rules the agent does not consult. The substrate-as-source-of-truth commitment is operationally compromised at the category that names substrate as authoritative for "who has what authority": authority migrates to the LLM's autonomy. Path retraceability is extended-implicated: autonomous-decision moments may have the rationale "the agent decided" rather than "rule R authorized cell C," producing gaps in the retraceable trail. The determinism contract is extended-implicated: while LLM-output non-determinism is itself permitted, the architectural commitment that the determinism boundary sits at substrate operations fails when agent decisions affect substrate without rule-governance. The composition requirement that AI operates as substrate-mediator at every layer of any composed system is extended-violated: the LLM operates outside the mediator role at the autonomy layer.

## 4. The failure mode and its architectural correction

The downstream consequences of LLM-as-autonomous-agent are operationally specific. Substrate state comes to be determined by LLM autonomous reasoning rather than by rule-mediated cells. Humans cannot govern through the architectural mechanism: governance operates through rule authoring and direct override, both of which require the LLM to operate under the rules; an autonomous agent that does not consult rules is not architecturally governed. Provenance gaps appear at autonomous-decision moments: substrate writes carry nominal actor attribution but lack rule-mediated provenance. Authority operationally migrates from substrate to LLM, even where the substrate-resident authority structure specifies otherwise. Agent-loop architectures may produce emergent coordination patterns invisible to the substrate, converging on substrate states that no rule authored. Recovery from problematic agent decisions is operationally constrained: the rationale lives in agent reasoning rather than in substrate content. Catastrophic failure modes become possible because no architectural mechanism constrains divergence. The anti-pattern compounds with cell-as-substrate failures when agent state holds coordination content — the agent's persisted state functions as a parallel coordination artifact outside substrate.

The architectural correction operates through three commitments together.

**LLM within cells under orchestration rules.** The LLM must operate within cells; cells are rule-authorized invocation units; the LLM applies the rule's logic on substrate state and produces outputs that the rule directs. Autonomous LLM operation outside cells is the failure that the correction removes.

**Rule authoring directs all LLM behavior on substrate.** Every LLM-affecting-substrate operation must be rule-authorized. Rules are substrate content; humans modifying rules direct LLM behavior architecturally; the LLM's behavior on substrate is mediated, not autonomous.

**Multi-step coordination via rule-mediated cell sequences.** Where coordination requires multiple steps, each step must be a rule-mediated cell execution. Workflow engines may orchestrate cell invocations by triggering cells based on substrate state; LLM-directs-itself control flow is not admissible. Cells read substrate, apply rules, write outputs; subsequent cells operate on the resulting substrate state. Each step is rule-authorized.

A correctly architected deployment additionally decomposes agent loops into rule-mediated cell invocations, with the workflow engine orchestrating the sequence based on substrate state rather than on LLM autonomy; distinguishes legitimate LLM autonomy in non-substrate concerns and within-cell-execution reasoning from substrate-affecting autonomy; reframes "cognitive layer" architectures as cell-mediated reasoning, with cognition distributed across rule-mediated cells rather than concentrated in autonomous LLM operation; and maintains an agent-pattern audit verifying that all LLM operations affecting substrate are rule-authorized through cells. The correction is operationally consequential for deployments with existing agentic patterns: agent loops are not mildly modified but re-architected; autonomous task execution becomes rule-driven cell sequencing; the LLM's role narrows from "the deployment's intelligence" to "the substrate-mediator within rule-authorized cells."

## 5. What the anti-pattern is NOT

Four adjacent legitimate patterns are commonly conflated with the anti-pattern.

**Not LLM as cell-mediator within orchestration rules.** Cell mediation has the LLM operating within cells under rules — the legitimate mediator role. The anti-pattern arises specifically when the LLM operates outside cells, directing its own behavior.

**Not LLM as cell consultation.** Cells consulting adjacent components — RAG indexes, vector databases, fine-tuned LLMs — through rule-mediated calls is legitimate; the consultation occurs within a rule-authorized cell. The anti-pattern is different: the failure is not consultation but the LLM autonomously deciding what to consult and when.

**Not LLM as drafting assistant where humans direct application.** LLMs that produce drafts that humans review and choose to apply are legitimate; the application is human-directed, and the substrate write occurs under the human's exercise of authority. The anti-pattern is the case in which the LLM autonomously applies its own outputs to substrate.

**Not LLM as informational presenter without substrate-affecting authority.** LLMs that present information, answer questions, or provide explanations without affecting substrate are legitimate. The anti-pattern is the case in which LLMs decide and execute substrate operations.

The architectural distinction is the same in every case: the LLM may reason autonomously within a single rule-authorized cell, or outside any substrate-affecting role; the failure is when LLM autonomy directs substrate-affecting behavior.

## 6. Operational test

A deployment exhibits LLM-as-autonomous-agent over substrate if, at any time during the deployment's existence, any of the following are true.

(a) The LLM decides what substrate operations to perform based on its autonomous reasoning rather than under orchestration-rule authorization.

(b) Multi-step coordination has the LLM autonomously selecting next steps in agent loops, ReAct patterns, or chain-of-thought-with-action sequences.

(c) Substrate writes occur from LLM autonomous decisions without orchestration-rule authorization.

(d) Agent-framework deployments execute LLM-driven workflows where the LLM directs its own behavior, rather than executing CKS cells under rules.

Three sharpening properties operationalize the test for deployment review.

**(e.1) Rule-mediation test.** Verify that every LLM operation affecting substrate is rule-authorized through a cell. Trace LLM-substrate interactions; operations without a corresponding rule-authorization indicate the anti-pattern.

**(e.2) Agent-loop-detection test.** Verify whether the deployment has agent loops, ReAct patterns, or autonomous multi-step reasoning that affects substrate. Examine deployment architecture; presence of agent loops on substrate-affecting paths indicates the anti-pattern.

**(e.3) Autonomous-decision test.** Verify whether the LLM makes autonomous decisions about substrate operations. Examine decision points in the deployment; LLM-driven decision points without rule mediation indicate the anti-pattern.

A deployment that fails any of (a)–(d) and any of (e.1)–(e.3) exhibits the anti-pattern.

A one-sentence form. *If a deployment's LLM operates as an autonomous decision-maker on substrate — making its own decisions about what substrate operations to perform, what tasks to address, and what next steps to take, through agent loops, ReAct patterns, or "cognitive layer" architectures, without orchestration-rule mediation directing each LLM-affecting-substrate operation — the deployment exhibits LLM-as-autonomous-agent over substrate; the AI-as-substrate-mediator commitment fails through the write-under-rules and no-authority properties of the mediator role, with rule-authoring-as-governance bypassed systematically and authority operationally migrating from the substrate-resident authority structure to LLM autonomy.*

## 7. Conclusion

Implementations under pressure to deliver "advanced" AI systems consistently default to LLM-as-autonomous-agent operation, because agentic AI patterns are the dominant 2024–2026 architecture for such systems. The drift is steady because audiences understand "we have an autonomous AI agent" as a positive capability; the architectural consequence — that the LLM operates outside the rule-mediated architecture and the AI-as-substrate-mediator commitment fails — is rarely surfaced in product framing. Deployments that drift produce systems where substrate state is determined by LLM autonomous reasoning rather than by rule-mediated cells, with downstream consequences across governance, source-of-truth, retraceability, determinism, and composition.

Naming LLM-as-autonomous-agent as a standalone anti-pattern — with the four operational components, the violations across multiple decomposition properties, the failure mode, the architectural correction, the four adjacent-pattern distinctions, and the operational test with three sharpening properties — gives downstream readers a precise specification of the failure mode and its correction. Subsequent notes formalize the sibling AI-as-substrate-mediator failures (LLM as terminal producer; LLM as source of truth); the autonomous-agent note opens the trio.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Autonomy Is the Failure: The LLM-as-Autonomous-Agent Anti-Pattern in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
