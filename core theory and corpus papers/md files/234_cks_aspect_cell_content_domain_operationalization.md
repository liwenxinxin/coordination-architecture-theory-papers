# Reasoning Over, Not Commanding: How Aspects Operate Over Cells as Content Domain in the Coordination Knowledge Substrate Pattern Extended to AI Selves

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, in operational form, how Paper 2's content-domain relationship between an aspect and its constituent cells (B1.18 at aspect-cell scope) is realized through the source paper's substrate operations and Paper 1's three composition patterns, while preserving the cell-level autonomy that Paper 1 commits to.

## Abstract

Paper 2 introduces three architectural levels — cell, aspect, Self — and commits to a specific relationship between adjacent levels: a higher level operates over the levels below it as *content domain*, not as commanded subordinates (B1.18). At aspect-cell scope, this commitment carries operational consequence: the aspect asks pattern questions across its constituent cells for the aspect's purpose; the questions execute through Paper 1's composition patterns A/B/C (consultation, derived view, separate concern); cells continue cell-level work autonomously while the aspect reasons over cell content; cell substrate remains authoritative for cell content, while aspect substrate carries aspect-level outputs. This note formalizes that operationalization. It states the architectural specification, contrasts it with the orchestrator-commands-tool shape common in conventional AI hierarchies, identifies the Paper 1 commitments inherited at aspect-cell scope, and provides an operational test. It is the third of five notes decomposing B1.04 (aspect as coordination arrangement); together with B2.15 (aspect as purpose-defined coordination) and B2.16 (aspect coordination rules), it triangulates what an aspect *is* operationally before B2.18 and B2.19 close out the decomposition.

## 1. Why this needs to be formalized as a standalone operational variant

Paper 2 introduces two commitments that interact tightly at aspect-cell scope, and the interaction is what this note formalizes. The first is B1.04: an aspect is a coordination arrangement of cells serving a purpose. The second is B1.18: higher levels operate over lower levels as content domain. Each commitment is defended in the source paper. Their joint application at aspect-cell scope is not separately stated.

The omission is not benign. Without an explicit operational specification, the aspect-cell relationship is open to a misreading the source paper does not support. The misreading treats the aspect as the commanding party in an orchestrator/tool relationship: the aspect decides what cells should produce; cells produce on demand; the aspect gates cell behavior. That shape is common in conventional AI hierarchies, and a reader importing it from outside the paper will produce systems that look CKS-coherent at the aspect layer but break Paper 1's commitments at the cell layer — most consequentially, they break cell-level autonomy and the substrate-as-source-of-truth commitment that makes cells a defensible architectural unit in the first place.

This note pins down the architecture the source paper actually commits to, which is structurally different from orchestrator-commands-tool. It is also the third of five notes decomposing B1.04. The first (B2.15) names what the aspect is *for* (purpose-defined coordination). The second (B2.16) names how the aspect *coordinates* (its rules). This third note names how the aspect *relates* to the cells under its coordination — by reasoning over them as content domain, not by commanding them.

## 2. The architectural specification

In the CKS pattern extended to AI Selves, an aspect operates over its constituent cells as **content domain** when the following operational specification holds at every aspect-cell pairing in the deployment.

**(a) The aspect asks pattern questions across constituent cells for the aspect's purpose.** The questions are reasoning operations whose answers serve the aspect's purpose, not directives that prescribe what cells do. A "pattern question" is the source paper's term (core theory, "Aspect" subsection): the aspect formulates a question over constituent cell content, and the question's resolution produces an aspect-level result.

**(b) Pattern questions are themselves substrate operations under human-authored rules.** Per A2.04, the rules that specify *what* questions the aspect asks, *of which* cells, *through what* mechanism are orchestration-rule content authored by humans. The aspect is not free-form; its questions are structured by human-governed rules that determine the aspect's reasoning shape.

**(c) Pattern questions execute through Paper 1's composition patterns A, B, or C.** The same three patterns Paper 1 names for composing CKS substrates with adjacent components (A1.16, A2.92–A2.94) supply the canonical mechanisms. *Pattern A — consultation* (A4.27): the aspect consults specific cells with specific questions and integrates the responses. The aspect asks cell A "what is your assessment of X?" and cell B "what is your assessment of Y?" and integrates the readings into an aspect-level conclusion. *Pattern B — derived view* (A4.28): the aspect derives a view over multiple cells' authoritative substrate content per A1.08. The aspect builds an aggregated reading from cell substrates rather than consulting cells through their cell-level interface. *Pattern C — separate concerns* (A4.29): the aspect performs reasoning that uses substrate but does not consult cells directly. The aspect operates separately and composes its result with cell-level work at a higher integration point.

**(d) Pattern selection is per aspect-question pair.** Same aspect, different questions, different patterns. A consultation-shaped question may sit beside a derived-view-shaped question within the same aspect, both governed by the same coordination rules (B2.16) but instantiated through different composition patterns.

**(e) Cells preserve cell-level autonomy throughout.** Pattern questions do not block cell operations, do not modify cell internals, and do not gate cell behavior. Cells continue cell-level work asynchronously with the aspect's questions. Whether the aspect is currently asking a question of cell A or not, cell A continues to do cell-level work under cell-level rules.

**(f) Cell substrate is authoritative for cell content; aspect substrate is authoritative for aspect-level outputs.** Per A1.08, cell substrate holds the source of truth for cell content; the aspect reads cell content but does not become authoritative for it. Aspect-level outputs are themselves substrate-resident — the aspect carries its own substrate content where outputs reside — and that substrate is authoritative for aspect-level state.

**(g) Pattern questions and aspect-level outputs are recorded with scope-distinguishing provenance.** Per A2.40, six metadata fields record what was asked, by which aspect, of which cells, through which pattern, under which rule, with which result. The provenance distinguishes aspect-level operations from cell-level operations; path retraceability per A1.07 holds across the boundary.

These seven components together define the aspect-cell content-domain relationship at the operational layer. Each is recoverable from the source paper; the contribution of this note is to assemble them into a single specification that the architecture's downstream consumers can implement against.

## 3. What this is not: the orchestrator-commands-tool contrast

The architectural shape above is structurally different from a pattern that recurs throughout conventional AI hierarchies and is the most common misreading the present specification preempts.

In orchestrator-commands-tool, a higher-level component (an "agent," a "planner," an "orchestrator") decides what its tools should produce, calls tools to produce it, and integrates the outputs into a higher-level result. Tools are commanded; their outputs are determined by what the orchestrator asked for; their existence is in service of the orchestrator's plan. This is a coherent design pattern in many contexts, and the present note does not argue with it abstractly.

The CKS aspect-cell relationship is not this. The aspect does not decide what cells produce. Cells produce what cells produce, under cell-level rules, governed by cell-level human authority. The aspect *reasons over* cell output — it formulates pattern questions whose resolution requires reading what cells have produced or will produce on their own schedule, and integrates the readings into an aspect-level conclusion. The aspect's authority extends to the aspect's own substrate (where its outputs reside) and to the orchestration rules that specify its pattern questions; it does not extend to the cells' substrate or the cells' rules. This is what preserves Paper 1's commitments at the cell layer when cells participate in aspects: cell orchestration rules continue to govern cell behavior, cell substrate remains authoritative for cell content, and cell human-governance rights remain intact. The aspect adds reasoning over cell content; it does not subtract cell architectural autonomy.

## 4. The cognitive analog

The source paper's biology positioning supplies a parallel that is useful as a conceptual scaffold rather than as architectural substance. When a person asks themselves "what is my overall sense of this situation," the integrated reasoning operates over cognitive sub-modes — perceptual readings, emotional responses, embodied intuitions — as content domain rather than commanding them. The sub-modes continue their own work autonomously: perception keeps perceiving, the embodied response continues to register, emotion is still felt. The integrated reasoning produces a higher-level understanding by reading what the sub-modes are saying, not by directing what they should say.

The analog is conceptual scaffold, not architectural commitment. The architectural substance is the seven-component specification in §2 above: pattern questions formulated under rules, executed through composition patterns, against autonomous cells whose substrate remains authoritative for their content, with results recorded as scope-distinguishing provenance. The cognitive parallel makes the shape easier to absorb on first reading; the commitment the architecture defends is the operational specification, not the parallel.

## 5. Inherited Paper 1 commitments at aspect-cell scope

Paper 2's three-level architecture is recursive in Paper 1's commitments — Paper 1's commitments hold at each level. Restating which of them specifically apply at the aspect-cell content-domain relationship is what makes the recursion concrete.

**A1.02 — substrate-cell boundary.** The aspect's operations on cells respect the cell substrate boundary. The aspect reads from cell substrate; it does not modify cell internals; cell-internal state stays cell-internal. The boundary holds across aspect-cell scope as it holds within a cell.

**A1.08 — substrate as source of truth.** Cell substrate is authoritative for cell content; the aspect's reading of cell substrate does not migrate authority to the aspect. Aspect substrate is authoritative for aspect-level outputs in the same way.

**A1.13 — composition requirements.** Per-substrate human governance, conflict preservation across boundaries, addressable provenance across boundaries, AI-as-mediator at every layer, and human-selective composition all hold at aspect-cell scope. The aspect's pattern questions cross a substrate boundary; the five composition requirements are what keep that crossing CKS-coherent.

**A1.16 with A2.92–A2.94 and A4.27–A4.29 — composition patterns.** The three patterns and their operationalizations supply the canonical mechanisms for pattern-question execution. The "sharpening properties" Paper 1 names for each pattern apply at aspect-cell scope: in Pattern A, the consulting party (the aspect) does not become authoritative for the consulted party's (the cell's) content; in Pattern B, the derived view (the aspect's aggregated reading) does not become authoritative for cell content; in Pattern C, the aspect's separately-handled work does not silently couple back to cell behavior.

**A2.04, A2.40, A1.07 — rule authoring, provenance, retraceability.** The orchestration rules specifying what pattern questions the aspect asks are authored by humans (A2.04). Pattern questions and aspect-level outputs are recorded with six metadata fields (A2.40), distinguishing aspect-level from cell-level operations. The retraceable path (A1.07) runs through aspect-level operations and into cell-level operations without breaking — a reader inspecting an aspect-level output can trace it back to the pattern question that produced it, the cells the question was asked of, the cell content read, and the rule that authorized the question.

The Paper 1 commitments are not duplicated work at aspect-cell scope; they are the same commitments applied at a new scope. What the present note formalizes is which of them are load-bearing for the aspect-cell content-domain relationship specifically.

## 6. Operational implications

Five implications follow from the specification.

**Pattern questions are deployment-configurable per aspect purpose.** Different aspect purposes warrant different questions. A competitive-mode aspect asks different questions than a calm-study aspect, even when both reason over overlapping cells. The questions are orchestration-rule content under A2.04; configuration is a deployment decision.

**Pattern question rules evolve through Paper 2's directed-selection (B1.14) and action-feedback (B1.15) mechanisms.** Like other DNA-layer substrate content, the rules specifying pattern questions can be revised under human governance based on what the aspect's outputs revealed about whether the questions were well-formed. Evolution at the rule layer is governed evolution.

**Pattern selection is per aspect-question pair, not per aspect.** The same aspect can use Pattern A for one of its pattern questions, Pattern B for another, and Pattern C for a third. Pattern selection is determined by the question's shape, not by a global aspect-level setting.

**Aspect operations are concurrent with cell operations, and content-domain operations are testable.** Pattern questions do not block cells. Cells continue cell-level work whether or not the aspect is currently formulating, executing, or completing a pattern question; concurrency is what makes pattern questions a reasoning operation rather than a control operation. The reproducibility test (A5.16) extends Paper 1's determinism contract to aspect-cell scope: given the same cell substrate state and the same aspect rules, pattern-question execution produces equivalent aspect-level outputs.

**Recursion to higher scope is supported, with cross-level access coexisting.** Aspect-level outputs can themselves be content domain for the Self (B1.18 applied at Self-aspect scope, with B1.20). The same operational specification re-applies one level up: the Self asks pattern questions across aspects, executed through composition patterns, with aspect substrate authoritative for aspect-level outputs. The architecture scales recursively because the relationship between adjacent levels is a single uniform specification. Cross-level access per B1.19 — which permits the Self to access cells directly when purpose requires — coexists with content-domain composition; typical operations use the content-domain relationship, while specific purposes may invoke direct cross-level access. The two architectures are compatible because both respect the substrate-cell boundary at A1.02.

## 7. Limits

The aspect-cell content-domain relationship has bounds. Stating them precisely is what keeps the specification from being read as broader than the source paper supports.

**Not commanding cells.** The aspect's pattern questions are reasoning, not direction. A "pattern question" that prescribes what a cell shall produce is not a pattern question in this specification; it is a command, and the architecture does not authorize it from the aspect layer.

**Not bypassing the substrate-cell boundary.** The aspect reads from cell substrate through the cell's substrate interface. Aspect operations that reach into cell internals violate A1.02 regardless of whether they look like "questions" linguistically.

**Not making the aspect authoritative for cell content, and not blocking cell operations.** Cell substrate is the source of truth for cell content; the aspect's aggregated readings, derived views, and integrated conclusions are aspect-level state, not cell-level state. Conflicts on cell content are resolved in the cell substrate's favor. Cells run autonomously of pattern-question execution; an aspect that gates, suspends, or otherwise blocks cell-level work is not operating under this specification.

**Not prescribing specific questions, and not eliminating cell-level governance.** The architecture supplies the relationship; deployments configure the questions per purpose. The note does not fix what questions any particular aspect must ask. Cell-level governance — authoring of cell rules, override at cell scope, inspection of cell substrate — operates as Paper 1 specifies, untouched by aspect participation.

**Not one-directional only.** Aspect operations may surface evidence that motivates cell rule changes through human-mediated governance per A2.04. The flow from aspect-level findings back into cell-level rule revision is human-mediated, not automatic.

**Not eliminating level distinctions.** The aspect is not a "bigger cell," and cells are not "smaller aspects." Per B2.07, level distinctions are architectural; the content-domain relationship is what connects adjacent levels without collapsing them.

## 8. Operational test

A system instantiates the aspect-cell content-domain relationship as the source paper specifies it if and only if all of the following hold at every aspect-cell pairing in the deployment:

1. The aspect's operations on cells consist of pattern questions formulated under human-authored orchestration rules, not commands prescribing cell output.
2. Pattern questions execute through one of the three composition patterns (A consultation, B derived view, C separate concerns), with pattern selection per question.
3. Cells continue cell-level work autonomously whether or not the aspect is currently asking a pattern question.
4. Cell substrate remains authoritative for cell content; aspect substrate is authoritative for aspect-level outputs.
5. Pattern questions and aspect-level outputs are recorded with provenance that distinguishes aspect-level from cell-level scope, and the retraceable path runs across the aspect-cell boundary without breaking.

A system that fails any of (1)–(5) is operating an aspect-cell relationship the source paper does not commit to, and downstream work that relies on its content-domain guarantees should be scoped accordingly.

## 9. Why naming this as standalone matters

The aspect is the source paper's named architectural unit between cell and Self, and its operational shape is what makes the three-level structure work or fail. B2.15 names what the aspect is for; B2.16 names how it coordinates; this note names how it relates to the cells it coordinates. B2.18 (multi-aspect cell participation) and B2.19 (aspect-level inheritance verification) will close out the decomposition by naming, respectively, what happens when a single cell participates in multiple aspects and how Paper 1 commitments are verified to hold at aspect scope. Subsequent Phase B2 notes step up to the Self level (B2.20–B2.24, decomposing B1.05).

Naming this relationship as standalone matters for two reasons. First, it preempts the orchestrator-commands-tool misreading at the place that misreading is most likely to import — the aspect-cell interface, which superficially resembles the agent-tool interface in conventional hierarchies but is structurally different in the architecture the source paper defends. Second, it makes Paper 1's commitments at cell level explicitly portable into the aspect context: a system designer reading only B1.04 might be uncertain whether cell-level commitments survive aspect participation; the present note makes the answer concrete and the test five-point.

Subsequent work that builds aspect structures, composes aspects with Self-level integrators, or argues against the three-level structure should use "aspect-cell content-domain relationship" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Reasoning Over, Not Commanding: How Aspects Operate Over Cells as Content Domain in the Coordination Knowledge Substrate Pattern Extended to AI Selves.* May 8, 2026. ORCID: 0009-0004-8065-3235.
