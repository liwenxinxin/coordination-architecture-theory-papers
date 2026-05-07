# Outside the Model at Self Scope: The Instinct/Reasoning Separation as the Foundational Architectural Commitment of CKS-Governed AI Selves

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the precise meaning of the instinct/reasoning separation as the source paper's unifying architectural commitment, so that downstream work and subsequent derivation notes can adopt or argue against the commitment without ambiguity.

## Abstract

The second CKS paper extends the design pattern from a single coordination cell to a complete AI Self by committing to the architectural separation of fast-pattern *instinct* from deliberate *reasoning* into independently-evolving layers under unified human governance. The instinct layer is the LLM, providing pattern-matched, fast-path responses. The reasoning layer is the CKS substrate inherited from the first paper, providing explicit, deliberate, human-governed processing. The commitment is the unifying architectural move of the second paper: every other commitment the paper defends — the three structural levels, the lifecycle primitives, the three evolution mechanisms, the multi-shaped governance — either establishes structures the separation requires, develops dynamics it enables, or specifies governance properties that keep it safe. It is also the natural extension of the first paper's hybrid commitment: the substrate/LLM division drawn at the governance boundary at cell scope generalizes to the instinct/reasoning division at Self scope. This note states the commitment, identifies its foil, distinguishes its architectural substance from the System-1/System-2 cognitive scaffold, names the inherited Paper 1 commitments it composes with, articulates its operational implications and limits, and supplies an architectural test by which a deployment is recognizable as instantiating it.

## 1. Why the separation needs to be named as foundational commitment

The first paper in the CKS theory series defends a design pattern at the scope of a single coordination cell: substrate handles coordination and governance, LLM handles high-dimensional reasoning, division at the governance boundary rather than the capability boundary. The commitment holds at cell scope and was demonstrated in commodity infrastructure with a commercially available LLM integration. What the first paper does not address is what happens when the cell stops being the largest architectural object the design pattern reasons about — when cells compose into larger structures, persist through life and evolution under continued human governance, and stand as one functioning AI Self at deployment scope.

The second paper takes up this question. Its response is the instinct/reasoning separation: at Self scope, the full population of the Self's instinct behavior and the full population of its deliberate reasoning are held as architecturally distinct layers rather than blended into one model-as-system, with the two layers composing under unified human governance. The separation is the second paper's *unifying* architectural move. The structural machinery the second paper introduces — three levels (cell, aspect, Self), two layers within every cell (DNA layer, action layer), expression as governed selection — gives the separation a coherent home; the dynamic machinery (birth, mating, death, three evolution mechanisms, bidirectional evolution) develops how the two layers move in time; the governance machinery (multi-shaped governance, the boundary as governed substrate content, distinct death-type processes) keeps the separation safe at scope. Reading the second paper without naming its unifying move first reduces it to a list of independent commitments rather than the coherent architectural posture it presents.

This note opens Series B, which parallels the Series A notes that formalized the first paper. B1.01 articulates the unifying architectural move all subsequent Series B notes elaborate.

## 2. The architectural commitment

In a CKS-governed AI Self, fast-pattern instinct and deliberate reasoning are held as two architecturally distinct layers, independently-evolving on different timescales by different actors, and composed into one Self under unified human governance.

**The instinct layer.** The LLM, operating as the System-1 analogue. Its content is pattern-matched, fast-path, no-reasoning-needed responses to inputs the LLM is competent to handle directly. The instinct layer's authority is bounded by the AI-as-substrate-mediator role specified in the first paper at §4.1–§4.2 and formalized as Series A note A1.04: the LLM reads from the substrate as primary state, writes only under human-authored orchestration rules, holds no substrate-relevant state outside the substrate, exercises no authority over substrate content, and has its writes recorded with attribution. The LLM's capability is essential at every scope of the Self; the separation does not relax that requirement.

**The reasoning layer.** The CKS substrate inherited from the first paper, operating as the System-2 analogue. Its content is the persistent, structured, human-governed coordination knowledge — entities, relationships, decisions, rationale, conflicts, and the human-authored orchestration rules that determine how cells behave. The substrate is the source of truth for coordination state per A1.08; the inspect/modify/override authority over substrate content and orchestration rules holds at all times per A1.01; conflicts in coordination state are preserved as first-class substrate content rather than collapsed by the LLM, per the first paper's third claim.

The separation operates within the hybrid commitment the first paper defends. The first paper draws the substrate/LLM division at the governance boundary rather than the capability boundary at cell scope; the second paper extends that same division to Self scope.

## 3. What makes the separation architecturally distinctive

The foil the commitment positions against is the monolithic LLM-only architecture in which the model is the entire system. In the foil, coordination, governance, conflict-handling, and reasoning all live inside the LLM's inference, and what the second paper calls the "outside-the-model" layer either does not exist or is treated as incidental scaffolding around the model. Contemporary LLM-only architectures genuinely instantiate this pattern, and the absorption pressure on the architecture grows as LLM capability sharpens — every workflow component the model can plausibly subsume becomes a candidate for absorption, and every absorption further centralizes the locus of error correction inside weights humans cannot inspect, modify, or version-control with the granularity governance requires.

The architectural consequence of the foil is that errors can only be addressed by modifying the model itself: fine-tuning, prompt engineering, RLHF rounds, retraining. The architectural consequence of the separation is that errors are addressable at the layer where they occur. When the LLM mis-pattern-matches, the reasoning layer can route around the mistake under orchestration rules; when the LLM silently collapses a contradiction the architecture must preserve, the conflict-preservation commitment from the first paper catches it and surfaces it as substrate state for human resolution; when the LLM produces an output that violates a coordination invariant, the rule that authorizes substrate writes refuses the write. None of these corrections requires modifying model weights; the human-governed substrate provides corrective signal as substrate content and orchestration rules.

The distinction is detectable by architectural inspection. A deployment in which all corrections to AI behavior require some form of model modification has the foil's architecture; a deployment in which corrections can be made by authoring or modifying substrate content and orchestration rules, with the LLM held to the bounded mediator role, has the separation. The architectural test consolidates these in one operational sentence: *can humans correct AI behavior without modifying model weights or prompt context?*

## 4. The cognitive analog as conceptual scaffold

The System-1/System-2 framing the second paper uses, drawing on the dual-process literature in cognitive science and on its precedents in the dual-process AI tradition, is conceptual scaffold rather than load-bearing theoretical grounding. The scaffold imports warrant readers absorb quickly because the parallel between fast-pattern responses and deliberate reasoning is intuitive across human and machine cognition. The architectural substance, however, is independent of the cognitive theory.

Architecturally, the instinct layer is the LLM with its authority bounded by the mediator role of A1.04; the reasoning layer is the substrate with its content authoritative per A1.08 and its rights of inspection, modification, and override held by humans at all times per A1.01; the separation is the design decision to keep the two layers distinct while composing them under unified governance, with the boundary itself substrate content the orchestration substrate governs. The architectural argument would hold with the cognitive scaffold replaced. What the second paper Claim 1 commits to is the layered architecture and its governance posture, not the cognitive theory the layer names borrow from. The architectural contribution is the specific configuration in which the System-2-analogue is a runtime-governable human-authored coordination substrate rather than weights, fine-tuned variants, or fixed engineered configuration, and in which independent evolvability of the two layers is treated as architectural requirement rather than incidental modular flexibility.

## 5. Inherited Paper 1 commitments composing with the separation

The instinct/reasoning separation does not stand on fresh axioms. It composes with the first paper's commitments, each held at every level of the second paper's architecture and referenced by the corresponding Series A note as inherited foundation.

*Human-governed (A1.01).* Both layers operate within the authority architecture the first paper defends. The reasoning layer is governed through inspect/modify/override rights over substrate content and orchestration rules at all times; the instinct layer is governed through the mutation-management mechanisms the second paper develops — verification substrates, routing decisions, and orchestration substrates that pin high-stakes decisions to reasoning regardless of LLM capability.

*Substrate-cell boundary (A1.02), substrate as source of truth (A1.08).* The two-layer substrate-cell structure generalizes naturally: the boundary the first paper draws between substrate and cell at cell scope generalizes to the boundary between reasoning and instinct at Self scope. The reasoning layer is *substrate-resident* in the strict sense — substrate-relevant state lives in the substrate, the instinct layer holds none outside it, and this is what makes corrective signal at the reasoning layer possible without weight modification.

*AI-as-substrate-mediator (A1.04).* Directly relevant. The mediator role with its five properties *is* what the instinct layer's bounded authority looks like. The second paper does not redefine the LLM's role at Self scope; it inherits the mediator role and uses it as the precise specification of what the instinct layer is authorized to do.

*Hybrid systems composition (A1.16).* Directly relevant. The first paper's note on hybrid composition specifies three legitimate positions adjacent AI components can occupy relative to a CKS substrate at cell scope. The instinct/reasoning separation operationalizes the hybrid commitment at Self scope: the LLM is the adjacent AI component, and its position relative to the reasoning substrate is precisely the bounded mediator role of A1.04. The separation is what the first paper's hybrid pattern looks like when the cell is replaced by the Self as the unit of composition.

The other first-paper commitments — conflict preservation, tool-agnosticism, linear-cost scaling — hold across the separation as well; subsequent Series B notes will trace their interactions with it.

## 6. Operational implications

Three classes of operational consequence follow.

*The separation enables the rest of the second paper's architecture.* The three structural levels are the architectural objects on which the separation operates. Lifecycle primitives operate at every level. The three evolution mechanisms — instinct evolution sharpening the LLM and infrastructure layer, DNA evolution updating orchestration substrate under directed selection, action-feedback evolution closing the loop from recorded experience back into governed substrate refinement — operate on the two separated layers and the boundary between them. None of these structures is coherent without the prior commitment that instinct and reasoning are held as distinct layers.

*Deployments instantiating the separation can correct AI behavior at substrate layer.* A deployment that recognizes the separation can author a rule pinning a class of decisions to the reasoning layer regardless of LLM capability; modify substrate content to overwrite a state the LLM produced incorrectly; introduce a verification substrate that runs reasoning and instinct in parallel and surfaces disagreements as conflict state; retire a reasoning substrate that instinct now handles reliably while keeping it as fallback. None of these actions modifies model weights or prompt context, which is the architectural property the separation makes available.

*Deployments that collapse the layers cannot benefit from substrate-mediated correction.* Without the separation, the path of correction is constrained to model modification, and the cost properties the first paper defends do not transfer. The collapse is not always visible from outside the system; a deployment with a CKS-shaped substrate that nonetheless allows the LLM to write coordination state outside cell mediation, hold substrate-relevant state in agent memory across sessions, or exercise authority over orchestration rules has collapsed the layers in practice even where the substrate exists nominally. Recognizing the separation is therefore as much about what the LLM is *not* authorized to do as about what the substrate carries.

## 7. What the separation is NOT

Each of the following misreadings is a real and reasonable position in some other architecture; conflating any of them with the separation produces an incorrect picture of the second paper's commitment.

*Not LLM-optional.* The LLM's capability is essential at every scope — pattern-matching over unstructured inputs, language understanding, drafting, interpretation, the high-dimensional reasoning the substrate cannot encode. A sharper LLM makes the Self more capable, not less; what the separation commits to is the architectural posture in which the LLM's capability is exercised under bounded authority while the substrate carries what humans govern.

*Not substrate-replaces-LLM.* The substrate provides coordination, governance, and the deliberate reasoning humans govern; it does not replace the pattern-matched capability the LLM provides. The two layers do different work, and neither is a substitute for the other. Architectures that propose to replace LLM capability with symbolic engineering, retrieval-only systems, or formal specification languages are taking different positions on different design questions.

*Not error-eliminating.* Pattern-matching mistakes, hallucinations, and reasoning failures will continue at the instinct layer; what the separation provides is that they are addressable at the architectural layer where corrective signal can be applied. The separation makes errors *governable* without requiring the LLM itself to be modified each time.

*Not a rigid layering.* The separation does not propose impermeability. The action layer of every cell records what happened when the LLM met a task, and that record feeds action-feedback evolution into DNA-layer refinement under human governance. Verification substrates run reasoning and instinct in parallel and use accumulated agreement evidence. The boundary itself is substrate content the orchestration substrate governs. The commitment is to the architectural distinctness of the layers, not to the absence of governed flow between them.

## 8. Architectural test

A system instantiates the instinct/reasoning separation if and only if all of the following hold at all times during the Self's existence:

1. The LLM operates as a substrate mediator in the sense of A1.04: reads from substrate as primary state, writes under orchestration rules, holds no substrate-relevant state outside the substrate, exercises no authority over substrate content, and has writes recorded with attribution.
2. The reasoning layer is substrate-resident in the sense of A1.08: coordination knowledge, decisions, rationale, conflicts, and orchestration rules live in the substrate and are read as authoritative on coordination questions.
3. Humans retain inspect/modify/override rights over substrate content and orchestration rules at all times in the sense of A1.01, and AI behavior corrections take effect through changes to substrate content and orchestration rules rather than through model modification.
4. The boundary between instinct and reasoning is itself substrate content the orchestration substrate governs: humans can modify where instinct is trusted and where reasoning is required, and high-stakes decisions can be pinned to the reasoning layer regardless of LLM capability.
5. The two layers evolve independently on their respective timescales: an LLM upgrade does not require revalidating the substrate, and a substrate modification does not require retraining the LLM.

A deployment that fails any of (1)–(5) may be a useful AI system, and may be governed in some other sense, but is not instantiating the instinct/reasoning separation in the sense the second paper defends. The test consolidating these conditions in one operational sentence is: *can humans correct AI behavior without modifying model weights or prompt context?*

## 9. Why naming the separation as foundational matters

The instinct/reasoning separation is the second paper's unifying architectural move because every other commitment the paper defends operates over it. The structural commitments (three levels, DNA/action layers, expression as governed selection) are the architectural objects on which the separation operates; reading them without the unifying move reduces them to a list of independent design choices. The dynamic commitments (lifecycle, three evolution mechanisms, bidirectional evolution) develop how the two separated layers move in time and are coherent only against the prior commitment that the layers are distinct. The governance commitments (multi-shaped governance, the boundary as governed substrate content, distinct death-type processes) specify the properties that keep the separation safe at scope.

Series B proceeds from this note. B1.02 develops the three-level structure (cell, aspect, Self) as the architectural primitive on which the separation operates. The remaining Phase B1 notes elaborate the structural, dynamic, and governance dimensions of the unifying move; subsequent phases decompose each foundational commitment into operational variants, anti-patterns, composition pairs, operational tests, and boundary cases. Every Series B note presupposes the commitment formalized here.

Subsequent work that adopts the second paper's architecture, extends it, composes it with adjacent patterns, or argues against it should use *the instinct/reasoning separation* in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Outside the Model at Self Scope: The Instinct/Reasoning Separation as the Foundational Architectural Commitment of CKS-Governed AI Selves.* May 7, 2026. ORCID: 0009-0004-8065-3235.
