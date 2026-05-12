# DNA Activation Patterns: The Operational Realization of Expression Through Harness Substrate Rules in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize the operational patterns by which the harness substrate per B2.30 determines which DNA-layer substrates activate for which conditions, as the second of five notes decomposing Paper 2's expression mechanism (B1.07).

## Abstract

Paper 2's expression mechanism names the harness substrate as the component that determines which DNA-layer substrates activate for a given cell goal. A separate note (B2.30) formalizes the harness substrate as a substrate-resident, human-governed configuration object. This note formalizes the operational patterns through which the harness substrate's rules realize differential DNA activation: input-conditioned, context-conditioned, aspect-conditioned, multi-condition, time-bounded, conditional routing within an activated element, scheduled, and priority-based. The enumeration is illustrative, not exhaustive; the architectural commitment is that activation patterns are substrate-resident, rule-specified, governed under Paper 1's rule-authoring authority (A2.04), recorded as authoritative substrate content (A2.46), provenance-tagged per the six-field accountability vocabulary (A2.40), and deterministic given conditions (A1.10). The biological analog is differential gene expression; CKS exceeds the analog by making the regulatory mechanism itself an inspectable, modifiable, and overridable substrate object rather than a product of evolution.

## 1. Why DNA activation patterns need to be formalized as a standalone operational variant

Paper 2's expression mechanism distinguishes the cell's DNA layer (stabilized orchestration substrates and behavior substrates) from the cell's harness substrate (the human-governed object that decides which DNA-layer substrates participate in current activity). B2.30 formalizes the harness substrate's representational form, governance posture, and place in the substrate-cell boundary. That note answers *what is the harness substrate?* The question this note answers is the operational sequel: *by what configurable patterns do harness rules realize the activation decisions the harness is responsible for?*

A harness substrate that supports differential activation but specifies no patterns by which the differentiation is governed is unspecified at the operational layer. Differential activation under substrate-resident, rule-specified governance is the operational form the expression mechanism takes; naming the patterns explicitly closes the territory where any party could later claim that this or that conditional-activation scheme is novel invention. Conventional AI components — fixed pipelines, monolithic prompts, undifferentiated retrieval over vector indexes — typically have no such layer; CKS deployments do.

This is the thirty-first Phase B2 note and the second of five notes decomposing B1.07: B2.30 specifies the harness substrate; this note (B2.31) specifies the activation patterns; B2.32 will specify the carry-strategy decisions; B2.33 will treat expression evolution; B2.34 will close the decomposition with expression-mechanism inheritance verification against Paper 1's commitments.

## 2. The activation patterns, precisely stated

Each pattern is realized through harness rules. The harness substrate carries the rules; the rules are authored under A2.04's rule-authoring authority; the rules are categorically authoritative substrate content per A2.46. Every activation event the rules produce is recorded with the six provenance metadata fields per A2.40. Activation is deterministic given conditions per A1.10: the same harness, the same DNA, the same input, the same context, and the same aspect produce the same activation.

**Input-conditioned activation.** A DNA element activates when the input has a specified property. The rule has the form *"DNA element X activates when input has property Y"* — where Y may be a type match, a value-range match, a structural-pattern match, or any other condition expressible as a function over the input the harness can evaluate.

**Context-conditioned activation.** A DNA element activates based on cell context — the deployment phase, the time of day, the deployment configuration, the presence or absence of specific substrate content, or any other condition expressible as a function over substrate-resident context state per A1.08. The same input may produce different activations in different contexts.

**Aspect-conditioned activation.** A DNA element activates based on which aspect the cell is currently participating in. The rule has the form *"DNA element X activates when the cell is participating in aspect A"* and is authored per the multi-aspect-participation commitment (B1.17). Aspect-conditioned activation is the operational pattern that realizes B1.17 at expression scope: the same cell, participating in different aspects, expresses different DNA. Without it, multi-aspect participation would be a labeling property without operational consequence.

**Multi-condition activation.** A DNA element activates when a combination of input, context, and aspect conditions all hold — *"DNA element X activates when input has Y AND context is Z AND aspect is A"*. Multi-condition rules support fine-grained activation control where no single dimension is sufficient.

**Time-bounded activation.** A DNA element activates within a bounded time window — *"DNA element X activates from timestamp T1 to T2"*. Time-bounding supports A/B testing periods, seasonal behavior, scheduled operational changes, and emergency mode windows opened and closed under governance.

**Conditional routing within an activated element.** Once a DNA element activates, conditional sub-rules within the activated content may further route processing to specific sub-paths. Activation chooses the element; routing within the element chooses a path within it. Both layers are rule-specified.

**Scheduled activation.** A DNA element activates per schedule, independent of any specific input — cron-like activation for periodic behavior such as nightly summarization or weekly review. This is a degenerate case of context-conditioned activation against the wall-clock; the case is common enough to warrant explicit naming.

**Priority-based activation.** When multiple DNA elements could activate under their respective rules, the harness rules specify priority — *"if elements X and Y both qualify, X activates"* or *"X has priority Z; the highest-priority qualifying element activates"*. Priority-based resolution makes activation determinate in cases of overlap rather than relying on implicit ordering or LLM-inference judgment.

The eight patterns are illustrative, not exhaustive. Deployments may author additional patterns under A2.04 — pattern authoring is itself rule authoring. The architectural commitment is not to a closed list but to the property that whatever patterns the deployment uses are substrate-resident, rule-specified, recorded under A2.40, and deterministic given conditions per A1.10.

## 3. What makes activation patterns architecturally distinctive

Conventional AI components frequently exhibit monolithic processing: the same component does the same thing regardless of input characteristics, deployment context, or organizational role. Monolithic processing is simple to specify and test, but it forces deployment-level differentiation outward — into multiple component instances tuned for different purposes, or into runtime parameters that are not themselves substrate-resident or governed.

CKS deployments support configurable activation patterns within a single cell. Two deployments of the same cell may have different activation patterns; one cell within a deployment may have different activation patterns from another with the same DNA; one cell may evolve its activation patterns over time through directed selection (per B1.14) while its DNA content remains stable. The architectural difference is not merely about whether activation can vary — many systems support some form of conditional execution — but about *where the variation lives*. In CKS, it lives in human-governed substrate-resident harness rules, inspectable per A1.07, modifiable and overridable at any time per A1.01, and recorded with provenance per A2.40 so that any past activation decision can be replayed against its rule and its conditions. The variation is not buried in the LLM, not encoded in implicit middleware, and not distributed across deployments where it cannot be governed as a unit.

## 4. The biological analog and where CKS exceeds it

Biology has a loose analog in differential gene expression. The same genome, present in essentially every cell of a multicellular organism, expresses different genes in different tissues — liver cells and neurons share DNA but produce different proteins because their regulatory mechanisms (transcription factors, chromatin state, signaling pathways) activate different genes. The analog is loose because the regulatory mechanism in biology is itself a product of evolution: the activation patterns are encoded in the genome's regulatory regions, are not directly inspectable as intentional artifacts, and are not modifiable at operational timescales.

CKS exceeds the analog at the same point Paper 2 names elsewhere: explicit governance over the regulatory layer. Activation patterns are substrate content, not emergent regularities. They are inspectable, modifiable, and overridable. They evolve at operational timescales rather than evolutionary ones, through directed selection per B1.14 and action-feedback per B1.15. And they are *intentional*: the deployer decides which patterns the cell uses by authoring the harness rules. The analog orients the framework; the architectural commitment is what the analog cannot deliver.

## 5. Inherited Paper 1 commitments

DNA activation patterns inherit governance and accountability properties from Paper 1's foundational commitments via the chain established in B2.30 and prior notes. Activation patterns are governed in the standard human-governed sense per A1.01, and activation history is preserved in the substrate per A1.07's path-retraceability commitment, not in volatile cell state or LLM memory.

**A2.04 — rule authoring as governance.** Activation patterns are realized through harness rules; harness rules are authored by humans (or by LLMs operating under human direction with human authority over the result). The activation patterns inherit the authority property by virtue of being rule-specified.

**A2.46 — Category 4 substrate content.** Harness rules and the activation patterns they encode are categorically authoritative substrate content. They are not transient runtime parameters, not application-layer configuration, and not LLM-resident. Their categorical authority is what makes their inspection and modification governance actions in the architectural sense.

**A2.40 — six-field provenance metadata.** Every activation event is recorded with the six provenance metadata fields. Activation history is path-retraceable: any past activation can be inspected to determine which rule fired, against which input, in which aspect, at which time, producing which DNA-element selection.

**A1.10 — determinism contract.** Given the same harness, the same DNA, the same input, the same context, and the same aspect, activation is deterministic. Determinism is a property of the activation patterns as rules over inputs, not a guarantee about LLM-side processing once a DNA element is activated. The activation layer is the substrate-deterministic layer; processing within an activated element follows the cell's own determinism posture per A2.20.

## 6. Operational implications

**Configuration at birth, evolution thereafter.** Deployments configure activation patterns per cell purpose during cell birth (B1.09). The patterns evolve through Paper 2's evolution mechanisms: directed selection per B1.14 refines patterns based on intentional improvement; action-feedback per B1.15 may propose pattern refinements based on accumulated action-layer evidence under human-mediated approval. Evolution operates on harness rules as substrate content, not on the DNA elements the rules activate.

**Multi-aspect participation realized at expression scope.** Aspect-conditioned activation operationalizes B1.17. A cell participating in two aspects with different DNA expression in each is, operationally, a cell whose harness contains aspect-conditioned activation rules. The relational nature of aspect membership becomes mechanical at this layer.

**High-stakes decisions and the pinning instrument.** B2.05 commits high-stakes inputs to identification at the substrate layer; B1.13 names the pinning instrument of mutation governance — the architectural pattern that ensures high-stakes processing remains DNA-rule-bounded rather than instinct-routed. Activation patterns may realize the pinning instrument by routing identified high-stakes inputs to specific DNA elements whose execution is constrained by explicit reasoning rather than instinct shortcuts.

**Replay testability, tool-agnosticism, and scale.** Activation patterns are testable through A5.16's reproducibility commitment: given recorded conditions, activation events can be replayed against current or historical harness rules. Per A1.05, activation patterns prescribe no specific implementation — the harness substrate may be a spreadsheet, a database, a configuration file, a dedicated rule engine, or any combination. Where authority is distributed across partners per A2.47, activation patterns follow the same distribution. High-volume cells may use caching of activation decisions where the patterns permit, without altering the architectural commitment to rule-specified, deterministic, recorded activation.

## 7. Limits

The standalone treatment of DNA activation patterns does not extend the architecture beyond what Paper 2 commits.

Activation patterns do not bypass the harness — they are realized through harness rules, not parallel to them. They do not operate without governance — all are subject to A2.04. The enumeration is not exhaustive — deployments may author additional patterns. Activation patterns do not modify DNA content; they determine *which* DNA elements participate, not what those elements are. They do not eliminate cell-level governance — they add an expression-layer governance, they do not subtract a cell-layer one. They do not prescribe specific implementations — per A1.05, the harness implementation is unconstrained beyond the three minimal-host-environment requirements. Pattern selection is per cell-condition pair: different cells may use different patterns; the same cell may use different patterns for different conditions. And activation patterns do not override cell processing — per A2.20, processing operates on the activated DNA element after activation has been determined; the activation layer precedes processing, it does not displace it.

## 8. Operational test

A system instantiates DNA activation patterns in the CKS sense if and only if all of the following hold at all times during the substrate's existence:

1. Activation rules are substrate-resident and inspectable as substrate content within authorized scope, in a form readable by humans directly.
2. Activation rules are authored by humans (or by LLMs operating under human direction with human authority over the result) per A2.04, and are modifiable and overridable at any time by humans with appropriate access per A1.01.
3. Every activation event is recorded with the six provenance metadata fields per A2.40, such that the rule that fired, the conditions under which it fired, the input it fired against, and the DNA element it selected are each path-retraceable.
4. Given the same harness, the same DNA, the same input, the same context, and the same aspect, the same activation occurs deterministically per A1.10.
5. No LLM operation, vendor policy, or runtime middleware can in principle prevent (1) through (4) for authorized humans and authorized inputs.

A system that fails any of (1) through (5) does not implement DNA activation patterns in the CKS sense, even if it provides conditional execution by some other mechanism. The conditional execution may be useful and governable in some other framework; it is not the activation layer Paper 2 commits to.

## 9. Why naming the patterns as standalone matters

The B1.07 expression-mechanism decomposition proceeds in five notes: B2.30 specifies the harness substrate as the governing object; this note (B2.31) specifies the operational patterns by which the harness's rules realize differential activation; B2.32 will specify the carry-strategy decisions (full-DNA-with-selective-expression versus partial-slice carriage); B2.33 will treat expression evolution; B2.34 will verify that the expression mechanism inherits Paper 1's commitments correctly. Each note contributes a separable architectural object to the decomposition.

Without explicit treatment of the activation patterns, the harness substrate per B2.30 would name a place where activation is decided without specifying how decisions are configured at that place. Downstream implementations would then either invent conditional-execution schemes possibly inconsistent across deployments, or default to a single hidden pattern (typically input-conditioned) and lose the other seven. Naming the patterns explicitly closes that territory. Subsequent work that adopts CKS at the expression layer, extends the activation patterns, or argues against them should use the patterns in the sense formalized here. Subsequent work that uses different patterns is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *DNA Activation Patterns: The Operational Realization of Expression Through Harness Substrate Rules in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
