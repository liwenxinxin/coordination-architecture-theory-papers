# Expression as Governed Activation: The Harness Substrate Mechanism for Per-Goal DNA-Layer Selection in CKS-Governed AI Selves

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the **expression mechanism** as a standalone foundational architectural commitment under Paper 2 — the intra-cell mechanism that determines which DNA-layer substrates activate for a given cell goal, with each cell carrying a harness substrate that is itself substrate-resident, human-governed, fully inspectable, modifiable, and overridable.

## Abstract

Paper 2 distinguishes two layers within every cell — the DNA layer (stabilized orchestration substrates and behavior substrates that define how the cell functions) and the action layer (recorded task instances and their outputs). Not every DNA-layer substrate is active for every task the cell performs. Paper 2's *expression* mechanism is the architectural primitive that determines, for a given cell goal, which DNA-layer substrates activate. Each cell carries a **harness substrate** — itself substrate-resident, governed by Paper 1's human-governed commitment, and subject to the same inspect, modify, and override rights — that selects which sub-substrates are active for the cell's current activity. The carry-strategy — full Self DNA with selective expression versus partial slices — is a per-deployment design choice governed by orchestration substrate. This note formalizes expression as Paper 2's foundational intra-cell architectural commitment: a meta-architectural primitive in which substrate governs substrate activation while remaining itself first-class substrate-resident authoritative content. The note states the commitment, distinguishes it from neighboring framings, names the biological analog as conceptual scaffold, identifies the inherited Paper 1 commitments that compose into the mechanism, and provides an operational test for whether a system instantiates expression in the CKS sense.

## 1. Why expression needs to be formalized as standalone foundational commitment

Paper 2 introduces three intra-cell structural commitments that together carry its second claim's architectural content: the cell as atomic unit (inherited from Paper 1), the DNA/action layer distinction within every cell, and the expression mechanism that governs which DNA-layer substrates activate for a given cell goal. The first two have been formalized in earlier Phase B1 notes. Expression is the third and is operationally the most distinctive of them, because it names the mechanism by which a cell's stabilized configuration becomes dynamically active under governance.

The motivation for separating expression as a standalone commitment is that the alternative framings — all DNA always active, or rigid design-time module boundaries determined once and frozen — collapse what Paper 2 keeps separable. In conventional LLM-only architectures, all model weights are "expressed" through every inference; activation has no architectural target outside the inference pass itself, and there is nothing to govern in the "what is active right now" sense distinct from the model's behavior overall. In conventional rigid-module architectures, the boundary between active and inactive logic is a design-time choice baked into module interfaces, with runtime configurability either absent or handled through capability switches outside the host system's authority architecture. Neither alternative gives the deployment a per-goal activation mechanism governable in the same sense substrate contents are governable. Naming expression as a standalone commitment is what makes that mechanism architecturally describable rather than emergent or implicit.

The seventh position in Phase B1 is operationally precise. The two-layers-within-every-cell commitment establishes the DNA layer as the architectural target expression operates over; without that distinction, expression has no target. Subsequent Phase B1 commitments — modularity, lifecycle primitives, the three evolution mechanisms, structural properties — all compose with expression in ways that depend on its having been specified first. Mating combines harness-substrate content along with DNA and action; DNA evolution refactors the content the harness selects from; action-feedback evolution may propose harness-rule changes under human mediation. Expression is foundational not because it adds new theoretical content but because the rest of Paper 2's intra-cell architecture operates over the activation mechanism it specifies.

## 2. The expression mechanism, defined precisely

In the CKS pattern as extended by Paper 2, **expression** is the architectural mechanism that determines, for a given cell goal, which sub-substrates within the cell's DNA layer are active during the execution of that goal. The mechanism has three load-bearing components.

**(a) The harness substrate.** Each cell carries a substrate dedicated to selecting which DNA-layer sub-substrates are active for the cell's current activity. The harness substrate is itself substrate content under Paper 1's substrate-as-source-of-truth commitment. It is not a runtime feature of the host platform, not a vendor-managed configuration layer, and not an LLM-internal mechanism. It is content the substrate carries, alongside other substrate content, with the same architectural status — readable in inspectable form, modifiable under authority, overridable for specific cases, recorded with provenance.

**(b) Per-goal selective activation.** Not all DNA-layer content is active at all times. The harness substrate determines, given the cell's current goal, the subset of DNA-layer sub-substrates relevant to that goal. Different goals may produce different activation subsets within the same cell; the same goal under the same harness rules produces the same activation subset, preserving the determinism Paper 1 commits to at the coordination layer.

**(c) Carry-strategy as per-deployment design choice.** The cell carries either the full Self's DNA with selective expression at runtime, or only the subset of DNA-layer slices its purpose requires. The first carry-strategy supports lineage reconstitution — a copy of the cell preserves the full Self's genetic content and can be reactivated under different expression rules — and is appropriate where audit reach matters, such as in regulated work. The second reduces storage and cognitive load and is appropriate for high-throughput cells where efficiency matters. The choice is recorded as substrate-resident authoritative content and governed by orchestration substrate.

The harness substrate's three governance affordances follow from Paper 1 directly. Humans inspect it to read the activation logic the cell is operating under. Humans modify it to change what activates under what conditions. Humans override its activation decisions for specific cells or specific executions. The mechanism preserves Paper 1's full governance affordances at the meta-level of *which DNA activates*, not only at the level of what the DNA contains.

## 3. What makes expression architecturally distinctive

Three contrasts with neighboring framings clarify what expression commits to specifically.

**Distinct from all-active inference.** In LLM-only architectures, all model weights participate in every inference pass; there is no architectural target for selective activation external to the model. CKS expression is a substrate-layer mechanism that operates over the cell's DNA-layer content alongside whatever inference the cell's instinct layer performs. The selection is governed at the substrate layer, not at the model layer, and the governance is exercised over the harness substrate as substrate content rather than over model parameters.

**Distinct from rigid module boundaries.** In rigid module-based architectures, the boundary between active and inactive logic is a design-time choice frozen into module interfaces; configurability is typically limited to capability flags outside the host system's authority architecture. CKS expression is configurable activation at the substrate layer, with the configuration itself substrate-resident and human-governed. The flexibility is architectural, not opt-in: any deployment that satisfies the CKS commitments instantiates a configurable activation mechanism by virtue of the architecture, not by virtue of having opted into a configurability feature.

**Distinct from feature-flag and configuration-management framings.** Feature-flag systems are a recognized software-architecture pattern for deployment-time and runtime activation of code paths. CKS expression shares the shape of capability-defined-by-content-plus-activation-state but differs in commitment. Feature-flag systems are typically capability-motivated (release safety, gradual rollout, A/B testing); their governance treatment is deployment-safety governance rather than substrate-content governance. Configuration-management systems reconcile runtime state toward declared policy; CKS expression selects active substrates per deployment under orchestration-substrate authority, with the selection criteria themselves substrate-resident. The architectural shape is shared with both neighbors; the governance commitment is CKS's own. Feature-flag platforms and configuration managers are admissible adjacent tools; neither is the architectural mechanism.

A fourth contrast bears mention because it bridges to the biological analog: expression in CKS is a degree of freedom over biology. Biological cells must carry the full genome because biology has no other delivery mechanism. CKS makes carry-strategy a per-deployment design choice. The selective-activation shape parallels biology; the carry-strategy flexibility exceeds it.

## 4. The biological analog as conceptual scaffold

The biological reference for the expression mechanism is gene expression and gene regulatory networks. Most cells in a multicellular organism carry the full genome, but only a subset of genes are expressed in any given cell type — a hepatocyte and a neuron differ in the regulatory state that determines which transcription factors are active, not in the genomic content they hold. Gene regulatory networks are the mechanism that determines, for a cell type and condition, which genes are transcribed.

The architectural correspondences map cleanly. The genome corresponds to the DNA layer — the complete catalog of stabilized orchestration substrates and behavior substrates the cell carries. The gene regulatory network corresponds to the harness substrate — the mechanism that selectively activates the relevant subset. Cell-type-specific gene expression corresponds to per-goal selective activation.

Two bounds belong with the analogy. First, biological gene expression is mechanistically determined by molecular dynamics that arose through undirected evolution; CKS expression is mechanistically determined by harness-substrate rules under human governance. The selective-activation shape is shared; the governance commitment is CKS's own. Second, biological cells do not choose their carry-strategy; the genome they hold is what they inherit by mechanism. CKS deployments choose carry-strategy as a design parameter. The biology framing helps readers absorb the mechanism quickly; the architectural substance is configurable activation governed by substrate-resident, human-governed harness.

## 5. Inherited Paper 1 commitments at expression

The expression mechanism is fully constituted by inherited Paper 1 commitments composed at the meta-level of "which substrates activate." No commitment new to Paper 2 is required for expression's governance properties; each property follows from a Paper 1 commitment applied to the harness substrate as a special case of substrate content.

**Human-governed.** Humans hold authority over the harness substrate. Activation rules are authored by humans, and humans may directly override activation decisions. The authority-not-labor distinction holds: harness rules may be drafted by LLMs operating under human direction, but the authority over the resulting harness content remains with humans.

**Substrate as source of truth.** The harness substrate is itself substrate-resident — not held in agent memory, vendor control plane, or LLM-internal context buffer. It is authoritative state of the substrate, with the same architectural status as the DNA-layer content it governs.

**Inspect, modify, override.** The three rights apply to the harness substrate as they apply to all substrate content. The harness substrate is meta-architectural — substrate that governs substrate activation — but its governance affordances are Paper 1's, not new.

**Tool-agnosticism.** The expression mechanism imposes no specific platform, vendor, or runtime requirements. Carry-strategy is a per-deployment design choice realizable in any environment satisfying Paper 1's three minimal requirements (persistent structured state, human read/write access, LLM access to substrate content).

**Path retraceability.** Expression decisions are recorded with the six-field provenance metadata Paper 1 requires of substrate operations. Humans inspecting cell behavior can identify which DNA-layer subset was active during a given cell execution and under which harness configuration.

**Determinism contract.** Given the same harness rules and the same cell goal, expression selects the same active subset, preserving the substrate-layer determinism Paper 1 commits to.

The mechanism's novelty is not in its governance affordances, which are Paper 1's; it is in the architectural target — the meta-level "which substrates are active" — to which those affordances are applied.

## 6. Operational implications

Three operational implications follow directly from the formalization.

**Deployments choose carry-strategy per cell purpose.** Regulated work cells — substrates that must support audit reach, lineage reconstitution, and historical addressability — carry the full Self's DNA with selective expression. High-throughput cells — substrates whose dominant cost is storage and cognitive load — carry partial slices. The choice is recorded as substrate-resident authoritative content and is revisable through standard rule-authoring under Paper 1's two-moments-of-governance framing.

**Expression at birth specification.** Newly birthed cells are configured with their carry-strategy and harness substrate at birth. A cell that is mated, rather than originated from scratch, inherits its harness substrate through the mating mechanism — Union, Selective merge, or Lineage-preserved union — under orchestration-substrate governance, with the offspring's harness substrate produced by the same combination machinery that produces its DNA and action content.

**Activation patterns are testable.** Per the determinism contract, given the same harness rules and the same cell goal, expression's activation decisions are deterministic. Test patterns may exercise harness rules under controlled goals to confirm activation matches authored intent. Where activation diverges from authored intent, the divergence is observable through standard inspection of the harness substrate and remediable through standard substrate modification, not through opaque retraining or vendor-mediated intervention.

## 7. Limits

Five limits keep the standalone formalization disciplined.

**Expression does not introduce non-substrate content.** The harness substrate is substrate-resident in the same sense as the DNA-layer content it governs. A system that holds activation rules in a runtime middleware layer, a vendor control plane, or an LLM-internal mechanism is not instantiating CKS expression, regardless of whether the activation behavior superficially resembles harness-substrate selection.

**Expression does not replace the substrate-cell boundary.** It operates within cell substrate; it does not introduce a new layer or cross-cell mechanism. A cell's harness substrate selects from that cell's DNA-layer content; it does not reach across cell boundaries.

**Expression is not vendor-specific.** Feature-flag platforms, configuration managers, and AI policy frameworks are admissible adjacent tools; none is the architectural mechanism. The architectural mechanism is configurable activation governed by substrate-resident harness, realizable across deployment choices satisfying Paper 1's minimal requirements.

**Expression is not auto-adaptive.** The harness substrate does not learn what to activate from execution outcomes; activation is rule-governed. Outcome-driven refinement of harness rules is the province of action-feedback evolution, which is itself human-mediated — humans approve proposed changes before they take effect on harness content.

**Carry-strategy is revisable, not one-time.** A deployment may revise carry-strategy through standard rule-authoring under standard authority. The decision is not architecturally locked at birth; it is substrate-resident content under the same revision affordances that apply to any substrate content.

## 8. Operational test

A system instantiates the CKS expression mechanism if and only if all of the following are true at all times during the substrate's existence:

1. Each cell that participates in expression carries a harness substrate, held as substrate-resident authoritative content readable in inspectable form.
2. The harness substrate determines, given the cell's current goal, which subset of the cell's DNA-layer sub-substrates is active during execution of that goal.
3. The harness substrate is human-governed: humans with appropriate access can inspect, modify, and override its content under the rights Paper 1 commits to.
4. Carry-strategy (full Self DNA with selective expression vs. partial slice) is recorded as substrate-resident content and is revisable under standard rule-authoring authority.
5. Expression decisions are recorded with provenance per the six-field metadata requirement, such that humans can identify which DNA-layer subset was active during a given cell execution and under which harness configuration.
6. Given the same harness rules and the same cell goal, expression's activation decisions are deterministic and reproducible.
7. No vendor policy, runtime middleware, or LLM operation can in principle prevent (1)–(6) for authorized humans.

A system that fails any of (1)–(7) may activate DNA-layer content in some other architecturally meaningful way, but does not instantiate the CKS expression mechanism specifically.

## 9. Conclusion

The expression mechanism names the architectural primitive by which CKS-governed cells convert stabilized DNA-layer content into per-goal active behavior under governance. The mechanism is meta-architectural — substrate that governs substrate activation — but its governance is Paper 1's, not new: the harness substrate is itself substrate, the three rights apply, the determinism contract holds, retraceability composes naturally, tool-agnosticism is preserved. The carry-strategy distinction is a per-deployment design choice exceeding biology, where biological cells must carry the full genome by mechanism rather than choice.

Naming expression as a standalone foundational commitment gives downstream implementers a precise specification of what their activation mechanism must satisfy under the CKS commitment, distinguishes it from feature-flag platforms and configuration managers that share its shape but not its governance, and preserves the place expression occupies in the Phase B1 sequence — the DNA/action layer distinction provides the architectural target without which expression has nothing to operate over, and subsequent commitments (mating across layers including harness substrate, DNA evolution operating on the content the harness selects from, action-feedback evolution that may propose harness-rule changes under human mediation) all depend on expression having been formalized first. Subsequent work that adopts the CKS pattern, extends it, or argues against any of its commitments should use "expression" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Expression as Governed Activation: The Harness Substrate Mechanism for Per-Goal DNA-Layer Selection in CKS-Governed AI Selves.* May 7, 2026. ORCID: 0009-0004-8065-3235.
