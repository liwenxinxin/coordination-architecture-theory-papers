# How Versus What: The DNA Layer and Action Layer as the Two Kinds of Substrate Content Within Every CKS Cell

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the precise meaning of the two-layer distinction the second paper draws within every cell — the **DNA layer** and the **Action layer** — so that downstream work can adopt or argue against the distinction without ambiguity.

## Abstract

The second CKS paper draws an architectural distinction within every cell between two kinds of substrate content. The **DNA layer** holds the stabilized orchestration substrates and behavior substrates that define how the cell functions: the harness logic, the conflict-handling rules, the lifecycle policies, the schemas. The **Action layer** holds recorded task instances and their outputs: what actually happened when the DNA met an actual task. Both layers are substrate content under the architectural commitments inherited from the first paper — both inside substrate, human-governed, retraceable, and authoritative source-of-truth — but they differ in what they are authoritative *about* and in the mechanisms by which they evolve. This note states the distinction precisely, distinguishes it from the conventional weights-plus-logs framing, situates the biological analog as conceptual scaffold, identifies the Paper 1 commitments inherited at both layers, names the operational implications, and provides limits.

## 1. Why the two-layer distinction needs to be formalized as standalone

The first paper specifies what a cell is: a CKS artifact carrying substrate content under orchestration rules, with the six architectural commitments holding at cell scope. Substrate content there is treated as one kind of thing — the cell's content domain, governed under one set of rules. The second paper retains that and adds an intra-cell structural distinction: within every cell, two kinds of substrate content are architecturally distinguished, with different operational characters and different evolution mechanisms.

The distinction does much of Paper 2's load-bearing work. It enables the lifecycle machinery, enables the three evolution mechanisms to be operationally distinguished (DNA evolves through directed selection; Action accumulates and feeds back into DNA refinement under human mediation), and is what the expression mechanism operates over. Without the distinction, none of these can be specified coherently.

The distinction is also commonly absent from conventional AI architectures, which makes it a candidate for misreading by readers who expect the familiar "weights and logs" framing. A standalone treatment is the remedy: the distinction is not weights-versus-logs, both layers are first-class substrate content, and what differentiates them is the authoritative content each carries and the mechanism by which each changes.

## 2. The commitment, defined precisely

In the second CKS paper, every cell carries substrate content distinguished into two architectural layers. Both layers are substrate content under the first paper's commitments; the distinction is between two kinds of substrate content within the cell, not between substrate and non-substrate.

**The DNA layer** holds the stabilized orchestration substrates and behavior substrates that define how the cell functions: the harness logic that selects which sub-substrates are active for current activity, the conflict-handling rules, the lifecycle policies, the schemas, and the orchestration rules that govern cell-level behavior. The DNA layer defines the cell's potential — what the cell is architecturally capable of when it meets a task. It is what mating combines in the genetic sense, what evolution refactors, and what expression selectively activates.

**The Action layer** holds the recorded task instances and their outputs — what actually happened when the DNA met an actual task: instances handled, outputs produced, decisions and rationale, conflicts surfaced and outcomes, with provenance per A2.40. The Action layer is what accumulates as the cell's lived experience. It is what mating combines in the epigenetic and cultural sense — analogous to the education and training a parent provides a child beyond genetic inheritance — and what feeds back into DNA refinement when accumulated experience becomes evidence for a proposed change to how the cell functions.

The commitment is *architectural*: every cell, by design, distinguishes its substrate content into the two layers. The commitment is *operational*: the layers do different work and evolve through different mechanisms — DNA through directed selection (B1.14), Action through accumulation that feeds back human-mediated to DNA (B1.15). The commitment is *intra-cell*: it holds within every cell at every structural level (B1.02), and does not introduce a new structural level.

## 3. What the distinction is NOT

The distinction is precise about what it commits to. It is equally important to state what it does not commit to, because each adjacent framing is a real and reasonable position in some other architecture, and conflating any of them with the two-layer distinction misreads the second paper.

**Not a substrate/non-substrate boundary.** Both layers are substrate content. The distinction is intra-cell organization of authoritative content, not a redrawing of the substrate-cell boundary inherited from the first paper (A1.02). Action-layer content is no less substrate than DNA-layer content; A1.08 holds for both.

**Not a weights-plus-logs framing.** Conventional AI architectures pair weights (which determine system behavior) with logs (auxiliary outputs). Weights are first-class operational artifacts; logs are not. The two-layer distinction elevates both kinds of content to first-class substrate. The Action layer is not a log of the DNA layer — it is co-equal substrate, authoritative for what the cell did in the same architectural sense in which the DNA layer is authoritative for how the cell functions.

**Not a hierarchy of importance.** Neither layer is architecturally privileged. The two layers do different work; ranking them as "more" or "less" important is a category error. DNA-layer changes are governance events with high deliberation; Action-layer accumulation is routine. Different operational character does not entail different architectural standing.

**Not a replacement for the source-of-truth categories.** A1.08 specifies five categories of authoritative content (decisions, rationale, conflicts, entities, relationships per A2.43–A2.47). The categories cross-cut the two-layer distinction: each can have content in either layer or both. The same content kind can be a "decision in the DNA layer" (a stabilized policy) or a "decision in the Action layer" (a particular adjudication), and the architectural treatment differs accordingly.

**Not a new structural level.** The structural levels are cell, aspect, and Self per B1.02. The two-layer distinction operates *within* every cell. Aspects and Selves contain cells; the cells they contain carry the two-layer structure.

## 4. The biological analog as conceptual scaffold

The labels *DNA* and *Action* invoke the biological distinction between genetic inheritance and lived experience (with its epigenetic and cultural channels). The analogy is intuitive and the second paper relies on it as conceptual scaffold: an organism's potential is partly defined by what it inherits and partly shaped by what happens to it, with very different fidelity and very different evolution mechanisms in each channel.

The architectural substance is more specific and does not require the analogy to hold strictly. **DNA layer** = stabilized orchestration substrates and behavior substrates that define how the cell functions. **Action layer** = recorded task instances and their outputs. Both are substrate content, both human-governed, both retraceable, and both authoritative for what they're authoritative about. Whether the biological analog is read as parallel, as inspiration, or as decorative metaphor does not change the architectural specification.

The analog earns its keep on the *different mechanisms* point. Biological DNA evolves through inheritance with low-frequency mutation across generations; biological epigenetics and lived experience evolve through within-generation accumulation that does not modify the genome but shapes phenotypic expression. The CKS commitment that DNA evolves through directed selection while Action accumulates and feeds back human-mediated to DNA has a genuine structural parallel. Where it exceeds biology is in directedness, in fidelity (substrate content is retraceable per A1.07), and in governability.

## 5. Inherited Paper 1 commitments at both layers

The two-layer distinction is intra-cell organization of substrate content; the first paper's architectural commitments hold at both layers without modification.

**Human-governed (A1.01).** Both layers are human-governed in the precise sense of authority, not labor. Humans hold inspect, modify, and override rights over DNA-layer content (orchestration rules, harness logic, schemas, policies — typically authored by humans per Moment 1) and over Action-layer content (task instances, outputs, decisions, rationale, conflict records — accumulated through cell operation but inspectable, modifiable, and overridable at any time per Moment 2).

**Path retraceability (A1.07).** Both layers carry retraceability under the six provenance metadata fields of A2.40. DNA-layer changes and Action-layer accumulation are each retraceable, and the provenance distinguishes layer membership of a given content element.

**Substrate as source of truth (A1.08).** Both layers are authoritative substrate content. The DNA layer is authoritative for *how the cell functions*; the Action layer is authoritative for *what the cell did*. The five categories per A2.43–A2.47 cross-cut both layers.

**Substrate-cell boundary (A1.02).** Both layers are inside substrate. The boundary is preserved with substrate content organized into two intra-cell layers.

The remaining Paper 1 commitments hold at both layers: AI mediates over both under orchestration rules; tool-agnosticism implies neither layer requires a specialized runtime; conflict preservation applies to both (DNA-layer conflicts between competing policy proposals, Action-layer conflicts between competing decisions on parallel tasks); linear-cost scaling holds because governance cost is rule-variety-bounded and intervention-frequency-bounded, neither proportional to layer size.

## 6. Operational implications

Five operational implications follow directly from the distinction.

**DNA-layer changes are governance events with high deliberation.** Because the DNA layer defines how the cell functions, changes propagate to every subsequent task. A1.01 makes such changes admissible at any time, but their operational character is deliberate.

**Action-layer accumulation is routine.** Action content accumulates through normal cell operation under orchestration rules. No per-element governance event is required; governance is exercised over the rules that govern accumulation (Moment 1) and via direct override when chosen (Moment 2).

**Mating combines both layers under orchestration.** When two parent cells mate (B1.10), the orchestration substrate specifies how content from each layer combines — DNA might be merged selectively under human direction; Action might be inherited as union with conflict preservation; lineage-preserved patterns may apply to both.

**Expression operates over the DNA layer.** Expression (B1.07) selects which DNA-layer sub-substrates are active for current activity. Cells can carry the full Self's DNA with selective expression (when lineage and reconstitution matter) or partial slices (when storage and cognitive load matter). Expression does not operate over the Action layer in the same sense — Action content is recorded and retained according to the cell's policies, not selectively activated.

**Action-to-DNA feedback is human-mediated.** When accumulated Action-layer evidence suggests a DNA refinement, the architecture does not silently update the DNA. The substrates that propose DNA changes from action evidence are themselves human-governed, and the proposed changes are approved by humans before they take effect (B1.15). This is what prevents the Action layer from drifting the DNA over time. The feedback loop closes through human authority, not through automatic reconfiguration.

## 7. Limits

The distinction does not introduce non-substrate content. Both layers are substrate-resident. A system that locates "what the cell did" outside substrate — in vendor logs, in runtime traces, in derived projections that are not authoritative — is not implementing the Action layer in the second paper's sense.

The distinction does not imply that one layer is more important than the other. Treatments that prioritize DNA-layer content as "primary" and Action-layer content as "secondary" miss the architectural commitment.

The distinction does not replace the source-of-truth categories per A2.43–A2.47. The categories cross-cut both layers; mapping them one-to-one ("decisions go in DNA, entities go in Action") is not what the second paper commits to.

The distinction does not eliminate the substrate-cell boundary per A1.02. Both layers are inside substrate; cells continue to be the atomic unit per B1.03.

The distinction does not require that every conceivable content element be cleanly assignable to one layer. Layer membership of borderline content is determined by the cell's orchestration substrate, not by intrinsic property of the content.

## 8. Operational test

A system instantiates the second paper's two-layer commitment if and only if all of the following hold for every cell in the system:

1. The cell carries content of two architecturally distinguished kinds: stabilized substrates and behavior substrates that define how the cell functions (the DNA layer), and recorded task instances and their outputs (the Action layer).
2. Both kinds of content are inside substrate per A1.02 — not located in LLM weights, vendor logs, runtime traces, or derived projections that are not authoritative.
3. Both kinds of content are human-governed per A1.01 — humans retain inspect, modify, and override rights at any time over both.
4. Both kinds of content are retraceable per A1.07 — provenance per the six metadata fields of A2.40 distinguishes, among other things, layer membership.
5. The two kinds of content evolve through architecturally distinguishable mechanisms — DNA-layer changes are governance events, Action-layer accumulation is routine, and Action-to-DNA feedback is human-mediated rather than automatic.

A system that satisfies (1)–(4) but not (5) is treating the distinction as static categorization rather than as the architectural primitive that enables Paper 2's lifecycle and evolution machinery. A system that satisfies (5) but not (1)–(4) is implementing different mechanisms over content that does not carry the architectural distinctions. The commitment requires all five.

## 9. Why naming the distinction as standalone matters

Phase B1 of the derivation series names Paper 2's foundational architectural commitments one at a time so that subsequent notes can refer to each as already-named ground. The first five notes establish the unifying architectural move (B1.01) and the three structural levels (B1.02, with elaborations at B1.03–B1.05). The two-layer distinction is the sixth foundational commitment and the first to operate intra-cell.

The standalone naming sets up four immediately downstream notes: expression (B1.07) operates over the DNA layer; mating across layers (B1.10) combines parental content from both layers; DNA evolution (B1.14) is the directed-selection mechanism over the DNA layer; Action-to-DNA feedback (B1.15) is the human-mediated mechanism by which accumulated Action-layer evidence proposes DNA refinement. Phase B1 continues through modularity (B1.08), lifecycle (B1.09–B1.11), evolution mechanisms (B1.12–B1.15), bidirectional evolution (B1.16), and structural properties (B1.17–B1.20). Every Phase B1 note from this point onward presupposes the distinction formalized here.

Subsequent work that adopts the second paper's architecture, extends it, or argues against it should use *DNA layer* and *Action layer* in the senses formalized here. Subsequent work that uses the terms differently is using different concepts, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *How Versus What: The DNA Layer and Action Layer as the Two Kinds of Substrate Content Within Every CKS Cell.* May 7, 2026. ORCID: 0009-0004-8065-3235.
