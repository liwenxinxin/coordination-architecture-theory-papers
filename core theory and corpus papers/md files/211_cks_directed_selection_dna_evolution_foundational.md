# Directed Selection (DNA Evolution) Under Standard Authority Architecture: A Foundational Architectural Commitment Establishing the Second Evolution Mechanism in the Coordination Knowledge Substrate Pattern Extended to AI Selves

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the architectural commitment that **directed selection** — the evolution mechanism operating on the DNA layer of cells, aspects, and Selves through deliberate human authoring of orchestration substrates and behavior substrates — is governed through Paper 1's standard authority architecture, without any new evolution-specific governance machinery, and that this fact is what makes directedness an architectural property of CKS-governed AI Selves alongside the undirected variation of mutation.

## Abstract

Paper 2 of the CKS theory series identifies three evolution mechanisms operating on a CKS-governed AI Self in productive tension. A separate Phase B1 note formalizes the integrating frame; another formalizes the first mechanism, **mutation** — undirected variation of the instinct layer through vendor LLM updates and infrastructure upgrades, integrated through verification, routing, and pinning rather than authored. This note formalizes the second mechanism: **directed selection**, which operates on the DNA layer through human-deliberate authoring, modification, and revision of orchestration substrates and behavior substrates. The architectural claim has two parts. First, that directed selection is *deliberate and targeted* in a way mutation is not — humans choose what to evolve based on intended improvements, rather than receiving variation from outside the substrate. Second, that the governance shape is *the standard authority architecture from Paper 1* — the same A2.01 inspect, A2.02 modify, A2.03 override, and A2.04 rule-authoring affordances that govern substrate operations also govern DNA-layer evolution, with no new evolution-specific machinery introduced. The note states the commitment, names what makes it architecturally distinctive, identifies the biological analog and where CKS exceeds biology, enumerates the inherited Paper 1 commitments at work, names operational implications and limits, and supplies a one-sentence test.

## 1. Why directed selection under standard authority architecture needs standalone formalization

Within Phase B1, the evolution-mechanisms cluster (B1.12 integrating frame, B1.13 mutation, B1.14 directed selection, B1.15 action-feedback) is the load-bearing development of how a CKS-governed AI Self changes over time. B1.12 named the three mechanisms and their productive tension. B1.13 formalized mutation as undirected variation introduced from outside the substrate by vendor LLM updates and infrastructure upgrades, integrated through verification, routing, and pinning rather than authored. This note formalizes the second mechanism. The standalone treatment is required for three reasons.

First, **directed selection is operationally distinct** from mutation. Mutation arrives from outside the substrate; directed selection is variation authored deliberately *within* the substrate by humans intending specific improvements. Mutation's source is opaque (vendor weights, vendor pretraining choices); directed selection's source is fully retraceable substrate-side authorship. Mutation requires governance machinery downstream of the variation (verification substrates, routing rules, pinning policies); directed selection requires no machinery beyond what Paper 1 already provides.

Second, **the governance shape itself is the architectural claim**. Paper 2 does not introduce new governance machinery for directed selection; it extends Paper 1's standard authority architecture to evolutionary dynamics. The four affordances Paper 1 commits to — A2.01 inspect, A2.02 modify, A2.03 override, A2.04 rule authoring — apply directly to DNA-layer content. This parsimony is itself a derivation worth formalizing: a deployment running a Paper 1 system already has the entire infrastructure for directed selection.

Third, **directedness is what makes the productive tension claim operational**. Mutation provides capability the directed process couldn't have planned; directed selection provides stability and trajectory the mutations couldn't provide alone. Without directed selection formalized, the second half of the tension is gestural; with it formalized, the architecture's central evolutionary claim becomes specifiable, testable, and prior-art available.

## 2. The architectural commitment, precisely stated

In a CKS-governed AI Self per Paper 2, **directed selection** is the evolution mechanism that operates on the DNA layer of cells, aspects, and Selves through human-deliberate authoring of orchestration substrates and behavior substrates, governed through Paper 1's standard authority architecture without modification.

The commitment has five operational components.

**(a) The mechanism operates on the DNA layer per B1.06.** DNA-layer content is the stabilized substrate content that defines how cells, aspects, and Selves function: orchestration substrates governing how behaviors compose, behavior substrates specifying what those behaviors are, harness logic selecting which substrates activate per goal per B1.07, conflict-handling rules per A1.03, lifecycle policies, and schemas. The action layer — recorded task instances and outputs — is not directly modified by directed selection (the mechanism converting action evidence to DNA changes is action-feedback evolution per B1.15, which is human-mediated rather than directly authoring).

**(b) The variation is human-authored, not received from outside.** Humans choose what to evolve based on intended improvements: tightening a conflict-handling rule, adding a verification substrate, refactoring a harness substrate's expression logic, narrowing a behavior substrate's scope, introducing a new orchestration substrate. The variation enters through A2.04 rule authoring, applied to the substrate's evolution rather than its origination.

**(c) The governance shape is Paper 1's standard authority architecture.** Humans use A2.01 inspect to read DNA-layer content, A2.02 modify to change it, A2.03 override to change specific decisions or rule applications produced by current DNA-layer content, and A2.04 rule authoring to specify the new patterns future cell behavior will follow. No new governance affordances are introduced; the four Paper 1 affordances are jointly sufficient.

**(d) DNA-evolution events carry A2.40 provenance per A1.07.** Each event records what changed, who authored, when, the prior version pointer, the scope of change, and any rule justification or approval state. The retraceability commitment from Paper 1 holds at the DNA-evolution layer in the same shape it holds at the substrate operations layer.

**(e) Retroactivity treatment follows A6.02.** Historical state is preserved with the original DNA version recorded; new DNA specifications apply forward. Replay of historical task instances uses the historical DNA version, not the current one. This preserves the determinism contract per A1.10 across DNA evolution events: given inputs and a recorded DNA version, cell behavior is reproducible.

The commitment is *architectural* — directed selection is a property of how CKS-governed AI Selves evolve, not a procedural promise — and *level-recursive*: the same five components apply at cell DNA (harness, behavior, schemas), aspect DNA (aspect coordination rules, cell-membership rules, purpose specifications), and Self DNA (Self integration architecture, instinct/reasoning separation configuration, aspect-collection structure). What differs across levels is which content is at stake and which humans hold the authority per A2.47, not the architectural shape of directed selection itself.

## 3. What makes the commitment architecturally distinctive

The distinctiveness runs along three axes.

**Against conventional AI evolution, directed selection is a first-class mechanism.** Conventional AI evolution typically has only one mechanism — model retraining or fine-tuning of the inside-the-model layer. There is no explicit DNA layer outside the model that can be deliberately evolved, because there is no explicit DNA layer at all. Coordination, governance, and reasoning are either inside the model weights (where they are not deliberately editable except through retraining) or in ad hoc runtime configuration (where they are editable but not recognized as a layer with its own evolution semantics). The two-layer cell structure per B1.06 is what makes directed selection possible in the first place.

**Against biology, directed selection is an addition, not a parallel.** Biological evolution is autonomous: random mutation provides variation, natural selection acts on it through differential survival. There is no agent inside the system deliberately authoring variation toward intended improvements. Even in breeding (the closest biological parallel), the breeder must wait for the variation that produces the trait and then select for it. CKS goes further: directed selection here does not require waiting for variation. Humans directly author the desired DNA changes. The "directedness alongside undirectedness" point in Paper 2's "Where CKS exceeds biology" section is what this commitment makes operational.

**Against frameworks introducing evolution-specific governance, the commitment is parsimonious.** A natural temptation is to introduce separate governance surfaces for runtime operation and evolutionary change, with workflow approvals specific to evolution. Paper 2 declines that move. The same A2.01–A2.04 affordances govern both, because the DNA layer *is* substrate content per A2.46 and the standard authority architecture is what governs substrate content. A deployment running a Paper 1 system has, by the act of running it, all the infrastructure required for directed selection. What it lacks is not affordance but recognition — that authoring orchestration substrates and behavior substrates is itself the second evolution mechanism in a multi-mechanism architecture.

## 4. The biological analog and where CKS exceeds biology

The biology mimicry is at its weakest for directed selection because the mechanism has no direct biological parallel. Natural selection in biology is differential reproduction over undirected variation, not directed authoring. Breeding is the closest analog, and even there the directedness is partial — the breeder selects for traits but cannot author them; mutation remains the upstream source of variation. In every biological case, undirected variation is the prerequisite.

Paper 2's commitment that CKS has *directedness alongside undirectedness*, rather than *directedness instead of undirectedness*, handles this honestly. CKS does not replace mutation with directed selection; it adds directed selection alongside mutation per B1.13, the two operating on different layers (mutation on the instinct layer, directed selection on the DNA layer) and in productive tension per B1.12. What makes directed selection genuinely exceed biology is three properties together: it operates *within* the substrate, not over external variation; it requires no waiting for random variation; and it is governable through the same authority architecture that governs substrate operations. Biology lacks each of these. The biological analog is conceptual scaffolding for readers approaching the architecture; the architectural substance is CKS's own.

## 5. Inherited Paper 1 commitments

Directed selection composes with Paper 1's commitments without modification.

**Human-governed (A1.01).** The mechanism is governed by humans in the precise authority-not-labor sense. Humans hold the rights to inspect DNA-layer content, modify it, override decisions derived from it, and author the rules that govern how the layer is used. Directed selection is the most direct expression of A1.01 applied to evolutionary dynamics — humans use the same standard rights to evolve the substrate that they use to operate it.

**Inspect, modify, override, rule authoring (A2.01–A2.04).** Each Paper 1 affordance carries its own work into the evolutionary case. A2.01 supports reading current DNA before authoring changes. A2.02 supports changing DNA. A2.03 handles the transition between current and new DNA for in-flight cases — operationally distinct from directed selection in that override changes specific state without changing rules, while directed selection changes rules without overriding any specific past state. A2.04 is the foundational mechanism: authoring an orchestration rule that specifies new behavior is what directed selection *is*, in operational form. The note's central claim — that no new governance machinery is required — reduces precisely to the claim that A2.04, applied to DNA-layer content, is sufficient as the evolution affordance.

**Path retraceability (A1.07), determinism (A1.10), and substrate as source of truth (A1.08, with A2.46 specifically).** DNA-evolution events are retraceable through the six provenance metadata fields of A2.40. Determinism is preserved because version pinning per A6.02 makes historical and current DNA each separately referenced; given inputs and a recorded DNA version, cell behavior remains deterministic. A2.46 commits the substrate to being authoritative for "what rules apply"; DNA-layer content is part of A2.46's authoritative scope, so directed selection operates on substrate-resident, authoritative content with no parallel rule store outside substrate that it might modify.

The composition is what makes directed selection coherent. Each Paper 1 commitment carries its own work into the evolutionary case unchanged.

## 6. Operational implications

**Existing Paper 1 infrastructure suffices.** A deployment running a Paper 1 system already has the affordances needed for directed selection. No new governance UI, no new approval system, no new evolution-specific tooling is architecturally required. Whatever interface humans use to inspect and modify substrate content and to author orchestration rules is the same interface they use for directed selection.

**DNA evolution is auditable.** Each DNA-evolution event carries A2.40 provenance per A1.07; historical DNA versions are preserved per A6.02. The audit trail for evolution has the same shape as the audit trail for substrate operations. A6.14's deployment-evolution rule version compatibility treatment governs replay of historical task instances under their historical DNA, migration of long-running cells across DNA versions, and verification of behavioral consistency across evolution events.

**Concurrent operation with other mechanisms.** Directed selection operates concurrently with mutation per B1.13 and action-feedback per B1.15. The productive tension of B1.12 is held in concurrent operation: a deployment may receive a vendor LLM update (mutation, integrated through verification) while authoring a new orchestration substrate (directed selection) and approving a DNA refactoring proposed by accumulated action evidence (action-feedback). Each mechanism's governance shape is independent; they compose at the substrate without interference.

**High-stakes work emphasizes directed selection.** Because directed selection is the most directly governable of the three mechanisms — its variation is authored under standard authority rather than received from outside — high-stakes deployments can emphasize it. Pinning high-stakes decisions to reasoning per Paper 2 §8.3 is, in evolutionary terms, an emphasis on directed selection.

**Cross-partner authority per A2.47.** When DNA evolution affects cells or aspects spanning multiple composition partners, A2.47's authority distribution governs who can author the evolution; A6.12's multi-author rule authoring conflict treatment applies if multiple authors propose conflicting DNA changes. Nothing new is introduced.

## 7. Limits

**Directed selection does not operate on the instinct layer.** Vendor LLM weights are mutation per B1.13, integrated through verification rather than authored under directed selection.

**Directed selection does not operate on the action layer directly.** The mechanism that converts accumulated action evidence into DNA changes is action-feedback evolution per B1.15, which is human-mediated through substrates that propose DNA changes from action evidence and humans who approve those proposals.

**Directed selection does not eliminate other mechanisms.** The productive tension per B1.12 means all three operate. A deployment that suppresses mutation entirely loses the capability mutation provides; a deployment that suppresses action-feedback loses the loop-closing function. Directed selection is one of three.

**Directed selection does not auto-resolve conflicts with prior DNA.** When new DNA-layer content conflicts with existing DNA-layer content, A6.01 rule conflict resolution applies. The conflict is preserved as substrate-resident state per A1.03 and resolved through orchestration-rule application, not through silent merge or automatic deduplication.

**Directed selection is not the same as override.** Override per A2.03 corrects specific decisions through rule authoring or direct state change. Directed selection modifies DNA structurally — affecting all future cell behavior under the new DNA. The two compose without conflict but have different scopes.

**Standard authority architecture does not mean directed selection is trivial.** A DNA change is a governance event. The architecture provides the affordance; the deployment's configuration may impose review processes, approval gates, or multi-author requirements on top of it per A2.06's procedural-not-architectural distinction.

## 8. One-sentence test

A CKS-governed AI Self instantiates the directed-selection commitment if and only if humans can author, modify, and revise the DNA-layer content (orchestration substrates, behavior substrates, harness logic, conflict-handling rules, lifecycle policies, schemas) of cells, aspects, and the Self through Paper 1's A2.01–A2.04 standard authority affordances at any time during the Self's operation, with each evolution event recorded under A2.40 provenance per A1.07, with retroactivity treated per A6.02 such that historical state is preserved with original DNA version and new DNA applies forward, and with no separate evolution-specific governance surface required as a precondition for the affordance.

A system that lacks directly editable DNA-layer content, that requires LLM intermediation as a gate to DNA changes, that lacks recorded DNA-evolution provenance, that retroactively rewrites historical state under new DNA, or that requires evolution-specific governance machinery beyond Paper 1's standard affordances may be a useful system, but is not a CKS-governed AI Self under the directed-selection commitment.

## 9. Conclusion: second mechanism in the evolution cluster

Phase B1's evolution-mechanisms cluster has four notes. B1.12 named the three mechanisms and their productive tension. B1.13 formalized mutation as undirected variation introduced from outside the substrate, integrated through verification, routing, and pinning. This note formalizes directed selection as deliberate human authoring of DNA-layer content through Paper 1's standard authority architecture. B1.15 will close the trio by formalizing action-feedback evolution as the human-mediated loop from action evidence to DNA refinement.

With B1.14 in place, the productive tension claim per B1.12 becomes operational at both ends. Mutation provides capability the directed process couldn't have planned. Directed selection provides stability and trajectory the mutations couldn't provide alone. Biology has only mutation; CKS Selves have both. Subsequent Phase B1 notes move from mechanisms to bidirectional structure (B1.16 horizontal vs. vertical evolution) and structural properties of the levels-and-layers architecture (B1.17–B1.20).

Directed selection in particular needs naming as standalone commitment because it is the most architecturally direct form of CKS evolution. It uses Paper 1's standard authority architecture without modification, which means deployments running Paper 1 systems already have the directed-selection infrastructure — extending to Paper 2 means recognizing what they are doing as evolution and applying it deliberately to DNA-layer content. It is also the commitment that makes "directedness alongside undirectedness" operational. Without it formalized, the productive tension is gestural; with it formalized, the tension is architecturally specifiable and prior-art available.

Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "directed selection" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Directed Selection (DNA Evolution) Under Standard Authority Architecture: A Foundational Architectural Commitment Establishing the Second Evolution Mechanism in the Coordination Knowledge Substrate Pattern Extended to AI Selves.* May 7, 2026. ORCID: 0009-0004-8065-3235.
