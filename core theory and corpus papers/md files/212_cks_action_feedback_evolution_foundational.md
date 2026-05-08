# Action-Feedback Evolution as Human-Mediated Mechanism: Two-Stage Governance over the Action-to-DNA Pathway in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one of three evolution mechanisms Paper 2 commits to — **action-feedback evolution** — as a standalone foundational architectural commitment with content separable from the other two mechanisms (mutation and directed selection), with the specific shape of human-mediation distinguishing it from autonomous feedback loops in conventional AI systems and from biology's autonomous epigenetic and cultural inheritance.

## Abstract

Paper 2 names three evolution mechanisms operating on a CKS-governed AI Self: mutation on the instinct layer, directed selection on the DNA layer through the standard authority architecture, and **action-feedback evolution** on the Action-to-DNA pathway. Action-feedback is the only mechanism that lets the Self learn from its own operation rather than only from external upgrades or human design decisions. It is also the most delicate of the three: because the mechanism couples two substrate layers, it carries the highest risk of silent drift if not governed correctly. Paper 2 commits action-feedback to be **human-mediated** — accumulated lived experience in the action layer informs *proposed* DNA changes through substrates humans govern, with proposals subject to human *approval* before they take effect. This note states the two-stage human-mediation precisely, distinguishes the mechanism from automatic feedback patterns, identifies inherited Paper 1 commitments, enumerates operational implications and limits, and provides an operational test.

## 1. Why action-feedback evolution as human-mediated needs to be formalized as standalone

Paper 2 commits the CKS-governed AI Self to three evolution mechanisms in productive tension. Separate derivation notes formalize the integrating frame, mutation as undirected instinct evolution, and directed selection on the DNA layer. This note formalizes the third mechanism and closes the evolution-mechanisms cluster within Phase B1.

The architectural reason action-feedback warrants standalone treatment is that it is the only one of the three whose cause and target both sit inside the CKS substrate. Mutation enters from outside the substrate — LLM weight changes and substrate-platform infrastructure upgrades arrive from upstream. Directed selection acts on substrate DNA but originates from human-defined goals carried by the standard authority architecture. Action-feedback is structurally different: the action layer accumulates content as cells execute, that content carries patterns about what works and what fails, and those patterns flow back toward the DNA layer that defines how the cell behaves. Cause inside the substrate, target inside the substrate, two layers coupled by a feedback path. That coupling is what makes the mechanism delicate: without explicit governance, it would be the architecturally obvious place for accumulated experience to silently reshape orchestration logic over time. The risk it specifically introduces is the implicit-context-affecting-behavior-without-recording drift the source pattern is designed to preclude.

The two-stage human-mediation Paper 2 commits to is the architectural answer to that risk. Naming the mechanism as a standalone foundational commitment makes the answer legible: action-feedback is not an automatic loop with humans nearby; it is a mechanism whose every stage — what proposes, how proposals are formed, what becomes a DNA change — sits under explicit human authority.

## 2. The architectural commitment precisely stated

Action-feedback evolution is the evolution mechanism that operates on the Action-to-DNA pathway. The commitment has five operational components.

**(a) The action layer carries accumulated lived experience.** Per the two-layer architecture, the action layer holds recorded task instances and the outputs cells produced when DNA met actual tasks. Over time, accumulation produces evidence — patterns of success and failure, classes of inputs the DNA underspecifies, edge cases its orchestration rules handle awkwardly. This evidence is substrate content under Paper 1's commitments: inspectable, modifiable, governed.

**(b) Substrates propose DNA changes from action evidence.** Examining action evidence and translating patterns into candidate DNA modifications is itself substrate-resident labor. The substrates that perform that labor — *proposing substrates* — are themselves substrate content authored under the rule-authoring commitment. They specify what counts as evidence, what change patterns are considered, and what threshold triggers proposal generation. As substrate content, they inherit the inspect, modify, and override rights named in the human-governed commitment. They are not opaque automation; they are first-class governable artifacts.

**(c) Stage 1: humans govern the proposing substrates.** Humans hold authority over the proposing substrates' specification — what they read from the action layer, what patterns they recognize, what proposals they construct, under what conditions. This first stage of human-mediation operates through Paper 1's standard authority architecture. LLMs may participate in proposing-substrate labor under the labor-allocation framework, but the rules under which they work are human-authored and human-governable.

**(d) Stage 2: humans approve the proposed DNA changes.** Proposals do not become DNA changes automatically. A separate human approval gate operates on each proposed change before it is committed to the DNA layer. The approval rules — who approves, what review depth, what audit trail, what reversion paths — are themselves substrate content authored under the rule-authoring commitment.

**(e) Action-feedback events are recorded with provenance.** Every traversal of the Action-to-DNA pathway is recorded with the six-field provenance metadata the path-retraceability commitment requires: what action evidence informed the proposal, when, which proposing substrate produced it, what change was proposed, what approval was given, and what resulting DNA change took effect.

The two human-mediation stages together — governance over proposing substrates, separate approval of proposed changes — distinguish action-feedback evolution as Paper 2 commits to it. Either stage alone is insufficient: governable proposing substrates without approval gates allow the substrate to commit DNA changes humans have not reviewed; approval gates without governable proposing substrates leave humans approving outputs from machinery whose internal rules they did not author.

## 3. What action-feedback-evolution-as-human-mediated is NOT

Five adjacent commitments are commonly conflated with the human-mediated mechanism Paper 2 names; each is reasonable in some other architecture, and naming what action-feedback evolution is *not* keeps the commitment's content precise.

**Not automatic feedback.** Conventional AI systems with feedback loops typically commit feedback to automation: usage data trains models, telemetry adjusts behavior, observational data updates parameters. Action-feedback evolution is the opposite commitment at the architectural layer. The loop does not close automatically. Automation may live inside any single stage — LLMs may scan the action layer or draft proposals — but the loop's per-stage machinery is itself substrate humans govern.

**Not auto-adaptation.** A system that automatically modifies orchestration rules from accumulated experience is an auto-adapting system. CKS architecturally prohibits auto-adaptation at the DNA layer, because the prohibition is what preserves the human-governed commitment across the Action-to-DNA pathway.

**Not per-action review.** The commitment to human-mediation does not commit humans to reviewing every action. Humans review *proposed DNA changes*, which are aggregated patterns surfaced by the proposing substrates over many action-layer events. The action layer may grow at high throughput; the proposal stream is many orders of magnitude smaller; the approval workload is bounded by proposal frequency, not by action-layer size. Governance cost grows with proposal variety and approval frequency, not with substrate size.

**Not a substitute for directed selection.** Directed selection is intentional DNA refinement toward governance-defined goals; action-feedback evolution is experience-informed refinement humans may not have planned. The two operate in productive tension: directed selection brings purposeful direction; action-feedback brings empirical grounding directed selection cannot generate from intent alone.

**Not a substitute for mutation.** Mutation operates on the instinct layer and arrives from outside the CKS substrate as undirected variation. Action-feedback operates on the DNA layer through experience-informed proposals from inside the substrate. The mechanisms touch different layers, originate from different sources, and serve different evolutionary work.

## 4. The biological analog and where CKS exceeds biology

Action-feedback evolution loosely parallels two biological inheritance channels: **epigenetic inheritance** — methylation patterns, chromatin marks, and other heritable modifications that propagate without changing the underlying genome — and **cultural inheritance**, the transmission of behavioral patterns through teaching, imitation, and accumulated practice. Both are mechanisms by which lived experience shapes future behavior; both share with action-feedback the structural property that operational state influences what is later stabilized.

The biological mechanisms are autonomous. There is no governance over what experience shapes future behavior; methylation patterns propagate through cellular machinery; cultural transmission flows through whatever channels behavior creates. Biology has no architectural place for an authority that approves the experience-to-inheritance pathway, because biology has no architecture in the design-pattern sense.

CKS exceeds biology by making the mechanism human-governed. The two-stage human-mediation is the architectural delta: experience can shape future behavior, but only through proposing substrates humans govern and proposals humans approve. The biology mimicry functions as conceptual scaffold; the architectural substance is explicit governance over what would otherwise be an autonomous loop.

## 5. Inherited Paper 1 commitments

Action-feedback evolution composes with several inherited Paper 1 commitments without modifying any of them.

**Human-governed in the human-mediated shape.** Both stages instantiate the three rights named in the human-governed commitment (inspect, modify, override). The "human-mediated" shape is what governance looks like when the underlying mechanism couples two substrate layers: authority operates twice, once at the proposing-substrate boundary and once at the DNA-write boundary.

**Rule authoring.** Proposing substrates and approval rules are both authored under the rule-authoring commitment. The labor of authoring is allocable across direct human work, LLM work under human direction, and stable-cell work; the authority over the resulting rules is not.

**Path retraceability.** Action-feedback events are recorded with the six provenance fields the path-retraceability commitment requires — the recording is what enables a later human exercising the inspect right to reconstruct why any DNA change took the form it did.

**Conflict as first-class.** When a proposed DNA change conflicts with existing DNA — a pre-existing rule, a parallel proposal, or content authored by another partner under multi-author rule authoring — the conflict is preserved as substrate state and resolved through the standard authority architecture. The human approval stage is the natural site for resolution; what matters architecturally is that conflicts are not silently merged on the way through the pathway.

**Determinism.** Given inputs including the approval, action-feedback DNA changes are deterministic. Approval is part of the input; the DNA layer's deterministic state behavior is preserved.

These compositions are not new commitments; they are the existing Paper 1 commitments operating across the additional pathway Paper 2 introduces.

## 6. Operational implications

Five implications follow directly from the commitment.

**Deployments configure proposing substrates and approval processes explicitly.** A deployment chooses what kinds of action evidence trigger proposals, what classes of DNA change patterns are considered, what proposal threshold applies, who approves at what scope, what review depth attaches to which classes of change, and what audit and reversion paths exist. These choices are substrate content under governance, not configuration of opaque feedback machinery.

**LLMs may do proposing-substrate labor under the labor-allocation framework.** Pattern recognition over the action layer is work LLMs are well-suited to: surveying many task instances, identifying recurring failure modes, surfacing candidate refinements. The labor-allocation framework admits this as LLM-under-rule labor. What does not admit is LLM-committed DNA change without human approval; the labor allocation is silent on authority, and the approval stage is where authority operates.

**Action-feedback emphasis is a deployment decision.** Deployments where learning from experience is operationally important may emphasize the mechanism. Deployments where DNA stability is paramount may de-emphasize it, leaving directed selection as the primary DNA evolution mechanism.

**Harness substrate evolution is a natural application.** The harness substrate that governs which DNA-layer substrates activate per goal is itself substrate content. Action-feedback evolution can refine the harness substrate based on observed activation outcomes — but only through the same two-stage mediation that governs any other DNA change.

**Cross-partner action-feedback follows the multi-author treatment.** When proposing substrates authored by different partners produce conflicting proposals, or when proposed changes touch DNA jointly authored across partners, the multi-author rule-authoring conflict treatment applies during composition. Each partner's authority over its proposing substrates and its approvals is preserved.

## 7. Limits

Five limits keep the commitment's scope precise. Action-feedback **does not operate automatically**: both stages are human-governed, and a system in which either runs without human authority does not instantiate the commitment. Action-feedback **does not eliminate the need for directed selection**: directed selection is intentional, action-feedback is experience-informed, and the two operate concurrently to do different evolutionary work. Action-feedback **does not eliminate the need for mutation**: mutation operates outside the CKS substrate on the instinct layer, while action-feedback operates inside the substrate on the DNA layer. Action-feedback **does not replace cell-level operations**: action-layer accumulation is a cell-level operation, not an evolution event; evolution begins when proposing substrates examine accumulated content and the approval stage commits or rejects proposed changes. Action-feedback DNA changes **do not bypass rule retroactivity treatment**: historical state preserved at the time of any prior cell execution remains preserved; new DNA from approved action-feedback proposals applies forward.

## 8. Operational test

A system instantiates the action-feedback-evolution commitment as Paper 2 commits to it if and only if all of the following are true at all times during the substrate's existence:

1. The action layer accumulates recorded task instances and outputs as substrate content under Paper 1's commitments.
2. Proposing substrates that examine action evidence and produce DNA-change proposals exist as authored substrate content humans inspect, modify, and override.
3. Proposed DNA changes do not become DNA changes without human approval at a separately-governed approval stage.
4. The approval stage operates through Paper 1's standard authority architecture and produces six-field provenance recording the action evidence, the proposing substrate, the proposal, the approval, and the resulting DNA change.
5. No automation, vendor configuration, or runtime middleware can in principle bypass either the proposing-substrate governance stage or the approval stage.

A system that fails any of (1)–(5) may include feedback machinery, may improve over time, and may be governed in some other sense, but does not instantiate the action-feedback evolution commitment in the CKS sense.

## 9. Closing the evolution-mechanisms cluster

Within Phase B1, action-feedback evolution as human-mediated is the closing note of the evolution-mechanisms cluster. The cluster runs from the integrating frame for three mechanisms in productive tension, through mutation as undirected instinct evolution, through directed selection as DNA evolution under standard authority, to this note's commitment. The progression is principled: the integrating frame establishes that three mechanisms exist; the mutation and directed-selection notes specify the two whose governance shapes are the most direct extensions of Paper 1's commitments; this note specifies the third, whose governance shape is the most architecturally distinctive because the mechanism couples two substrate layers within the substrate.

Action-feedback's standalone treatment matters specifically because it is where architectural risk is highest. Mutation's risk is bounded by the verification regimes that govern instinct integration; directed selection's risk is bounded by the standard authority architecture that governs DNA writes. Action-feedback couples two substrate layers and runs experience-informed loops between them; without explicit two-stage mediation, the mechanism would be the natural conduit through which accumulated context could reshape orchestration logic in ways that escape audit. Naming the commitment with this risk in mind — proposing substrates governed, proposals approved, events recorded — is what holds the architecture's overall governance properties together across the Action-to-DNA pathway.

Subsequent Phase B1 notes shift to bidirectional evolution and structural properties that follow from the foundational commitments the cluster establishes. Subsequent work that adopts CKS's evolutionary architecture, extends it, or argues against it should treat action-feedback evolution as the human-mediated mechanism specified here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Action-Feedback Evolution as Human-Mediated Mechanism: Two-Stage Governance over the Action-to-DNA Pathway in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
