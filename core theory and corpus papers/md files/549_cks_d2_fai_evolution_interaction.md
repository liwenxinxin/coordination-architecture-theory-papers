# FAI and Intra-Self Evolution Interaction

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D2.54 is a Phase D2 operational-variant note deriving from D2.23 (temporal interleaving and version-fixing), D2.53 (lifecycle isolation principle), and Paper 2's three evolution mechanisms. D2.53 established that Paper 2 lifecycle events — birth, mating, and death — occurring within a participating Self's home perimeter during an active FAI event are isolated from FAI operations, with cross-scope implications requiring explicit governance action. D2.54 extends the same analysis to Paper 2's three evolution mechanisms: mutation (LLM upgrades), directed selection, and action-feedback evolution. The note establishes that all three operate within home governance scope and are isolated from the concurrent FAI event, with each mechanism presenting a distinct isolation profile. Mutation produces no DNA change and is completely isolated; directed selection produces DNA changes that create an observable version-divergence between the home substrate and the shared substrate; action-feedback evolution follows the same logic as directed selection when it produces a directed-selection approval during the event. The note formalizes the **evolution isolation principle** — home evolution events are isolated from FAI operations, and each scope operates under its own governance — and introduces the **two-trajectory design**: during a FAI event, each participating Self maintains two concurrent evolutionary trajectories, one in the home perimeter and one accumulating in the shared substrate. These trajectories diverge intentionally during the event and reconnect at dissolution through the governed four-locus evolution feed (Paper 3 Claim 4). The isolation is not a loss; it is the design that makes governance independence and inter-Self learning simultaneously achievable. The note also names the anti-pattern **evolution cross-contamination** and provides an operational test.

---

## 1. Derivation context

D2.54 is the fifty-fourth Phase D2 note in the CKS derivation series for Paper 3 (*Inter-Self Coordination via Shared Substrate / Full Aspect Integration*, Li, April 2026). It derives from three parents.

D2.23 established the version-fixing principle for contributed aspects: when a Self contributes an aspect to the shared substrate at FAI contribution time, the shared substrate captures the version of that aspect as it stands at that moment. Subsequent changes to the aspect in the home substrate — revisions, corrections, directed selection updates — do not retroactively update the shared-substrate content. The two records are distinct and independently auditable.

D2.53 established the lifecycle isolation principle: Paper 2 lifecycle events (birth, mating, and death) occurring within a participating Self's home perimeter during an active FAI event do not affect the shared substrate and do not alter the FAI event's operation. Home lifecycle governance and FAI governance are concurrent and independent. Cross-scope implications, where they exist, require explicit governance action: a participating Self whose internal structure changes in ways that affect contributed-aspect validity may evaluate configuration amendment or withdrawal, but no automatic propagation occurs.

D2.54 extends D2.53's analysis from lifecycle events to evolution mechanisms. Paper 2's three evolution mechanisms — instinct evolution (mutation), DNA evolution (directed selection), and action-feedback evolution — operate continuously within each Self's home perimeter throughout the Self's existence. They do not pause when a FAI event begins. This note formalizes what happens when each mechanism runs concurrently with an active FAI event.

---

## 2. Paper 2's three evolution mechanisms in brief

Paper 2 (*The Instinct/Reasoning Separation Outside the Model*, Li, April 2026) commits each CKS-governed AI Self to three evolution mechanisms in productive tension, operating across all levels of the Self's architecture simultaneously.

**Instinct evolution (mutation)** proceeds through LLM upgrades and substrate-platform infrastructure changes. It operates at the instinct layer — the LLM weights that constitute the AI's base capabilities and behavioral disposition. Instinct evolution is undirected in the sense that its trajectory is not determined by the Self's governance authority directly; governance configures the verification substrate through which upgrades are integrated, but does not author the upgraded LLM. Crucially, instinct evolution produces no DNA change: LLM weights are not substrate content under Paper 2's architecture, and upgrading them does not modify any aspect's DNA record.

**DNA evolution (directed selection)** proceeds through human-governed updates to the orchestration substrate — the structured content that encodes the Self's decision patterns, schemas, and operational rules. Directed selection is explicitly governed: humans hold authority over which changes are proposed, evaluated, and approved. It produces direct, traceable changes to the DNA of cells, aspects, or the Self at the level where selection is applied.

**Action-feedback evolution** proceeds through the proposal-and-acceptance machinery: lived experience within the Self's action layers generates improvement proposals, which are evaluated and, when accepted through directed selection, update DNA. Action-feedback is the mechanism through which the Self's own operational experience feeds back into its governed structure. When an action-feedback proposal is approved via directed selection, the result is a DNA change governed through the same directed-selection machinery.

---

## 3. Mutation during FAI

**Case.** A participating Self's LLM is upgraded — a mutation event — while a FAI event is active.

**Governance implication.** Mutation isolation from FAI is complete, and for a structurally distinct reason from the other two mechanisms. LLM weights and instinct-layer content do not exchange across the inter-Self perimeter. Paper 3 Claim 2's exchange-bounding commits that FAI exchanges DNA-layer and action-layer content; it explicitly excludes instinct-layer content from the exchange. This commitment is an extension of Paper 2's instinct/reasoning separation at the inter-Self scope: the separation that holds within a single Self at home also holds across Selves at the inter-Self boundary.

Because mutation does not produce a DNA change, there is no version-divergence artifact to account for. The upgraded LLM takes effect within the home perimeter. The instinct-layer behavior of the participating Self may shift as a result. None of this crosses the inter-Self perimeter. The FAI event continues under the same shared-substrate configuration, with the same contributed aspects, under the same orchestration rules. There is no shared-substrate content whose version could have diverged. Mutation during FAI is a home governance event with no FAI-facing surface.

---

## 4. Directed selection during FAI

**Case.** A participating Self's home governance conducts a directed selection event that modifies the DNA of an aspect currently being contributed to the FAI event.

**Governance implication.** The version-fixing principle from D2.23 applies directly. The shared substrate contains the version of the aspect at contribution time. The directed selection update modifies the home aspect's DNA under home governance authority. It does not retroactively update the shared-substrate content.

The result is an observable version-divergence: an observer reviewing the FAI event will see the pre-directed-selection version of the aspect; an observer reviewing the home substrate will see the post-directed-selection version. These are two independently legitimate records. The pre-selection version represents what the Self contributed and what the FAI event operated on. The post-selection version represents the current state of the Self's governed knowledge in that domain. Both are auditable, and neither invalidates the other.

**Governance-relevant case.** When the directed selection event significantly changes the contributed aspect in ways that affect the FAI event's validity — the selection corrects an error in the aspect, or fundamentally reframes the domain it covers — the participating Self's governance may determine that the FAI event's current configuration no longer accurately reflects what the Self would contribute if contributing today. In this case, home governance has a decision to make. The architecture makes available two governed paths: a configuration amendment (D2.38), which updates the shared substrate under the FAI event's amendment procedures; or a withdrawal (D2.27), which removes the contributed aspect from the active event under the event's withdrawal procedures. Neither path is automatic. Automatic propagation — the directed selection update reaching the shared substrate without explicit governance action — is precisely the anti-pattern named in §8 of this note.

---

## 5. Action-feedback evolution during FAI

**Case.** Home action-feedback evolution produces an improvement proposal that is approved via directed selection during an active FAI event, changing the DNA of a contributed aspect.

**Governance implication.** The same analysis as §4 applies. Action-feedback evolution, when it produces an approved directed-selection change to a contributed aspect's DNA, is a directed selection event for governance purposes. The version-fixing principle applies. Home DNA is updated; shared-substrate content is not. The version-divergence described in §4 follows.

**Additional case.** Action-feedback evolution may produce proposals relevant to the FAI event's domain without yet reaching directed-selection approval. A cell may flag an inefficiency in an orchestration pattern currently being contributed; an aspect may generate a proposal that identifies an improvement to the very content under FAI exchange. These proposals are in-progress home evolution activity. They do not automatically enter the shared substrate. However, the participating Self's governance may evaluate whether the insights from in-progress proposals should inform the FAI event's configuration — potentially by initiating a configuration amendment that updates the contributed aspect's scope or by flagging the insight as a discussion item within the event's orchestration substrate. This evaluation and any resulting action are explicit governance decisions, not automatic propagation.

---

## 6. The evolution isolation principle

**Stated.** Home evolution events — mutation, directed selection, and action-feedback evolution — occurring within a participating Self's home perimeter during an active FAI event are isolated from FAI operations. Each operates within its own governance scope. The FAI event operates under the shared substrate's configuration and the contributed aspects as they stood at contribution time. Home evolution proceeds under home governance without coordination with the shared substrate. Neither scope interrupts or modifies the other's operation.

**Cross-scope implications require explicit governance action.** When home evolution events produce outcomes that affect the FAI event's validity or appropriateness — such as a directed selection change that corrects a contributed aspect — the participating Self's governance evaluates whether explicit action (amendment or withdrawal) is warranted. The evaluation is a governance judgment, not an automatic trigger. The isolation principle does not prevent cross-scope action; it requires that any such action be explicit and governed.

**The isolation is not asymmetric.** Home evolution is isolated from the FAI event; equally, the FAI event's shared substrate does not inject into home evolution during the event. The shared substrate accumulates content under the FAI event's orchestration. That content does not reach the home perimeter until dissolution and the governed evolution feed. Isolation holds in both directions during the event's active duration.

---

## 7. The two-trajectory design

The evolution isolation principle is not a limitation imposed on FAI. It is the architectural design that makes two things simultaneously achievable: governance independence for each participating Self, and inter-Self learning through the FAI event.

During an active FAI event, each participating Self has two concurrent evolutionary trajectories.

**Home evolution trajectory.** Mutation, directed selection, and action-feedback evolution continue within the home perimeter under home governance authority. The Self's knowledge continues to develop. The Self's LLM may be upgraded. The Self's DNA may be updated in response to directed selection or approved action-feedback proposals. None of this requires coordination with the FAI event's shared substrate. Home governance retains full authority over the home evolution trajectory throughout.

**FAI evolution trajectory.** The shared substrate is accumulating content through the FAI event's operation: contributed aspects from all participating Selves are merging, conflicts are being handled under three-tier procedures, and orchestration is producing outputs. This accumulated content will constitute the evolution feed at dissolution. Each participating Self has a stake in this trajectory — what accumulates in the shared substrate during the event will become, at dissolution, the input to that Self's home evolution mechanisms.

These two trajectories diverge during the active FAI event. The home substrate and the shared substrate both evolve, but independently, under independent governance. The divergence is intentional. It is what preserves governance independence: neither Self's home evolution is blocked, constrained, or synchronized with the FAI event's shared-substrate evolution. Each home authority operates at home pace on home priorities.

**Reconnection at dissolution.** When the FAI event dissolves, the shared substrate's content propagates to each participating Self's home substrate through the four-locus evolution feed specified in Paper 3 Claim 4. The four loci — hand-off mechanism at dissolution, per-mechanism feed structure, layer-routing rule with three-case explicitness, asymmetric ingestion — constitute the governed path through which inter-Self learning enters home evolution. DNA-layer content from the shared substrate feeds the receiving Self's DNA evolution under home governance. Action-layer content feeds action-feedback evolution. Instinct evolution takes no FAI input by architectural commitment, consistent with exchange-bounding throughout.

At dissolution, the two trajectories reconnect: home evolution absorbs what the FAI event produced. The reconnection is governed — home governance determines, per the configured ingestion policy, what the home perimeter takes from the dissolution feed. Asymmetric ingestion is an architectural property: different participating Selves may absorb different content from the same FAI event under their respective governance authority.

The design pattern is: isolate during the event, reconnect at dissolution through governance. This is the architectural reason why evolution isolation during FAI is not a loss. The governed evolution feed is the mechanism through which inter-Self learning reaches home evolution — not during the event, but at its close, under explicit governance.

---

## 8. Anti-pattern: evolution cross-contamination

**Named.** Evolution cross-contamination is a FAI implementation in which home directed selection events — or home action-feedback approvals — automatically update shared-substrate content during an active FAI event.

**Form 1: automatic aspect synchronization.** A directed selection event updates a contributed aspect's DNA at home, and the FAI implementation automatically propagates the update to the shared-substrate version of that aspect. The shared-substrate content is updated without explicit governance action by the participating Self, without notification to other participating Selves, and without the event's configuration amendment procedures.

**Form 2: automatic action-feedback injection.** An action-feedback proposal relevant to a contributed aspect is approved at home, and the FAI implementation automatically injects the resulting DNA change into the shared-substrate version of the aspect.

**Why this is a violation.** Both forms violate the version-fixing principle from D2.23, which commits the shared-substrate content to the version at contribution time. More broadly, both forms collapse the two-trajectory design: home evolution and shared-substrate evolution can no longer diverge, which means governance independence is lost. The participating Self's home governance no longer controls when and whether home evolution outcomes enter the inter-Self scope. Other participating Selves' contributions and any conflict-handling that has already occurred are potentially invalidated by an automatic update they did not authorize. The auditability of the FAI event is compromised — an observer reviewing the event record cannot determine what version of each aspect was operative at what time.

**The governed alternative.** When home evolution produces outcomes that the participating Self's governance determines should enter the FAI event, the governed path is explicit: evaluate whether a configuration amendment is appropriate, initiate the amendment under the event's amendment procedures if so, and allow the amendment to be subject to the event's conflict-handling mechanisms. This path is auditable, reversible, and under joint governance of all participating Selves.

---

## 9. Operational test

For a FAI event during which a home directed selection event occurred on a contributed aspect:

1. Can an observer retrieve the shared-substrate version of the contributed aspect and confirm it matches the version at contribution time, prior to the directed selection event?
2. Can an observer retrieve the home-substrate version of the same aspect and confirm it reflects the post-directed-selection DNA?
3. Is the difference between (1) and (2) attributable to the directed selection event, with its timing recorded under home governance records?
4. Is there an absence of any automatic propagation pathway — no shared-substrate update timestamp that corresponds to the directed selection event's timestamp without an intervening explicit governance action?
5. If a configuration amendment was initiated following the directed selection event, is the amendment recorded in the shared substrate with its own governance record, distinct from the original contribution?

A FAI implementation that satisfies (1)–(5) instantiates the version-fixing principle, the evolution isolation principle, and the two-trajectory design. A FAI implementation that fails (4) — where the shared-substrate content was automatically updated at the moment of home directed selection — instantiates the evolution cross-contamination anti-pattern.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI and Intra-Self Evolution Interaction.* May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
