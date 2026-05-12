# Anti-Pattern Integrating Frame: Formalizing the Architectural Negatives of Phase B2's Positive Commitment Decompositions

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Phase B3 of the CKS Series B derivation-note sequence opens with this integrating frame. Phase B2 completed 110 notes decomposing the 20 foundational architectural commitments of Paper 2 (B1.01–B1.20) into operational detail. Phase B3 formalizes the architectural negatives of those commitments: the anti-patterns. This note establishes what anti-patterns are in the CKS architecture, how they differ from arbitrary violations, why formalizing them constitutes prior art, what structure every anti-pattern entry follows, and how the approximately 30 Phase B3 notes are organized into seven primary categories plus cross-cutting patterns. Anti-patterns in the CKS architecture are specific, named, stable, recognizable failure modes — not vague bad practices. Each has a recognizable architectural form, a specific commitment it violates, predictable operational consequences, and a governed remediation path. Together with Phase B2's positive commitment decompositions, Phase B3's anti-pattern taxonomy produces a complete architectural map of Paper 2's instinct/reasoning-separated, three-level, governed architecture: the full territory of what the CKS architecture commits to and how it can fail.

## 1. Why an Anti-Pattern Integrating Frame Needs to Be Formalized as a Standalone Note

Phase B2 decomposed Paper 2's 20 foundational architectural commitments (B1.01–B1.20) into 110 operational notes. That work covered the instinct/reasoning separation, the three-level structural machinery of cell, aspect, and Self, the DNA/action layer distinction within every cell, expression as governed selection over DNA-layer activation, lifecycle primitives (birth, mating, and death operating uniformly at every level), the three evolution mechanisms in productive tension, multi-level and multi-axis evolution, multi-shaped human governance, verification substrates, the instinct/reasoning boundary as governed substrate content, and the enterprise-brain Self as an architecturally coherent design pattern. Phase B2 answered the question: what must be true for the CKS Paper 2 architecture to hold?

Phase B3 answers the complementary question: what does it look like when the architecture fails, and how is failure corrected? It does not answer that question as commentary on poor practices. It answers it by formalizing the specific, named, stable, recognizable configurations that constitute architectural failure — the anti-patterns. This integrating frame opens Phase B3 by doing three things: defining what counts as an anti-pattern in the CKS architecture and why formalizing anti-patterns is itself prior art; specifying the standard seven-component structure that each Phase B3 note follows; and establishing the taxonomy that organizes Phase B3's approximately 30 notes into seven primary categories plus approximately nine cross-cutting patterns.

Opening Phase B3 with a standalone integrating frame rather than proceeding directly to individual anti-pattern notes is the same design choice that opened Phase B1 (B1.01 establishing the instinct/reasoning separation as the foundational architectural commitment before subsequent B1.xx notes developed the commitments it depends on) and that A-series phases used at their openings. The integrating frame ensures that subsequent Phase B3 notes can reference a shared definition and taxonomy without restating the framing each time, and that the prior-art coverage of Phase B3 is traceable to a single public document that establishes what anti-patterns are as a category.

## 2. What Anti-Patterns Are: Specific Named Stable Recognizable Failure Modes

In the CKS architecture, an **anti-pattern** is a specific, named, stable, recognizable failure mode — a recurring architectural configuration that violates a Paper 2 commitment and consistently produces governance failures. The definition has four required properties.

**Specific and named.** An anti-pattern is not a general direction of failure such as "not handling lifecycle correctly" or "insufficient governance." It has a name that identifies the failure mode precisely and allows it to be referenced, detected, and remediated under that name. The names used in Phase B3 — instinct-reasoning-collapse, flat-architecture, layer-conflation, ungoverned-birth, silent-drift, and others — are CKS terminology. They identify the architectural configuration, not a deployment symptom or an operational complaint.

**Stable.** An anti-pattern is a recurring configuration, not an isolated incident. A single implementation mistake in one deployment does not constitute an anti-pattern; the anti-pattern is the architectural shape that recurs across different deployments, contexts, or incremental decisions and produces the same class of governance failure each time. Stability is what distinguishes anti-patterns from debugging topics and what gives the taxonomy its prior-art value: a named stable pattern is something that can be claimed as known, while an isolated incident is not.

**Recognizable.** An anti-pattern has a form that can be identified architecturally. There is something visible in the structure — a collapsed layer where two should be distinct, a bypassed governance step, a missing lifecycle record, an undifferentiated level where three should exist — that marks the configuration as this anti-pattern rather than some other arrangement. Recognizability is what makes detection tractable and what makes remediation concrete rather than aspirational.

**Failure mode.** An anti-pattern consistently produces governance failures when present. It is not merely a suboptimal arrangement; it is an architectural configuration that violates a commitment in a way that predictably undermines the governance properties the commitment is designed to produce. The governance failures an anti-pattern produces are named in the operational consequences component of each Phase B3 note.

**Anti-pattern versus violation.** A violation is any deviation from a commitment. An anti-pattern is a stable architectural pattern of violation — one that recurs, is recognizable, and consistently produces governance failures. Every anti-pattern involves violations, but not every violation constitutes an anti-pattern. Individual implementation mistakes that do not recur across contexts, one-time deviations that produce no consistent downstream effect, and configuration gaps that generate no governance failure are violations but not anti-patterns. Phase B3 covers anti-patterns in this precise sense, not every way a CKS implementation can fall short.

**Why formalizing anti-patterns is prior art.** Naming the specific ways the CKS architecture can fail is an architectural contribution in its own right: it creates a public record that identifies these failure modes before any third party can claim to have discovered them. Each named anti-pattern closes off a territory of potential patent claims. A claim that a system "detects" or "prevents" the instinct-reasoning-collapse anti-pattern, for instance, cannot be novel if the instinct-reasoning-collapse anti-pattern has already been publicly defined with its form, violated commitment, consequences, detection method, and remediation path specified. Phase B3 establishes this prior-art territory across all 20 primary anti-patterns and the approximately nine cross-cutting ones. Most AI governance discussions in the literature describe good practices without naming their architectural negatives; formalizing the negatives at the same level of precision as the positive commitments is what creates comprehensive prior-art coverage.

## 3. Anti-Pattern Structure: The Standard Seven-Component Entry

Every Phase B3 note after this integrating frame follows the same seven-component structure. The components are:

**Pattern name.** A short identifying name in CKS terminology. The name is stable — it is used by subsequent notes in Phase B3 and will be referenced by cross-cutting notes (B3.22–B3.30), boundary-case notes (Phase B6), and operational test notes (Phase B5).

**Commitment violated.** The specific B1.xx commitment, or commitments in the case of cross-cutting anti-patterns, that this anti-pattern violates. References to the relevant B2.xx decompositions that developed the positive commitment in operational detail are included, so the anti-pattern note does not need to redevelop the positive commitment from scratch.

**Recognizable form.** How this anti-pattern looks architecturally. What configuration, absence, or structural feature indicates this anti-pattern is present rather than absent. Recognizable form is stated at the architectural level, not the deployment level: it describes what is true of the substrate structure, the layer relationships, the lifecycle records, or the governance mechanisms, not what any particular tool or interface shows.

**Emergence conditions.** Why this anti-pattern tends to arise. What pressures, misunderstandings, or incremental design decisions lead an implementation toward this configuration rather than the one the positive commitment requires. Understanding emergence conditions is what makes remediation durable: a remediation that does not address the emergence conditions will recur.

**Operational consequences.** What happens when this anti-pattern is present. What governance failures result, and how they manifest in operation. Operational consequences are stated in terms of the CKS governance properties the violated commitment is designed to produce.

**Detection.** How to detect this anti-pattern. Which structural properties to inspect, which Series A or Series B operational tests would flag it, and what signals distinguish this anti-pattern's presence from its absence. Detection is specified at the architectural level.

**Remediation.** How to correct this anti-pattern through governed processes. Remediation paths are drawn from the Phase B2 mechanisms: the positive commitments provide the governed pathways through which anti-pattern corrections are applied. Remediation is always through governed processes, not through workarounds or deployment-layer adjustments that leave the underlying architectural configuration unchanged.

## 4. Anti-Pattern Taxonomy: Seven Categories Covering All B1.01–B1.20 Violations

Phase B3's approximately 30 notes are organized into seven primary categories defined by which Paper 2 commitment cluster each anti-pattern violates. Each category contains one or more named anti-patterns. B3.02–B3.21 formalize one primary anti-pattern per B1.01–B1.20 commitment. B3.22–B3.30 formalize approximately nine cross-cutting anti-patterns that span multiple categories.

**Category 1 — Instinct/Reasoning Anti-Patterns (violating B1.01).**
Anti-pattern: instinct-reasoning-collapse. The instinct layer (the LLM, operating as fast-pattern System-1 analogue) and the reasoning layer (the CKS substrate, operating as deliberate human-governed System-2 analogue) are not kept architecturally separate. The configuration collapses both into a single undifferentiated layer — typically a model-as-system arrangement — which eliminates the reasoning layer's ability to route around bad instinct, prevents the conflict-preservation commitment from catching what instinct would otherwise silently merge, and removes the human-governed substrate's role as corrective signal. Formalized in B3.02.

**Category 2 — Level-Structure Anti-Patterns (violating B1.02–B1.05).**
Anti-pattern: flat-architecture. The three-level structural composition — cell as atomic unit, aspect as purpose-defined coordination arrangement of cells, Self as the integrated whole holding multiple aspects under unified human governance — is not instantiated. Instead, all coordination work proceeds at a single undifferentiated level, typically cell-level coordination scaled up without structural composition. This collapses relational role membership, aspect-level coordination, and Self-level unified governance. Formalized in B3.03.

**Category 3 — Structural Anti-Patterns (violating B1.06–B1.08).**
Anti-patterns: layer-conflation, expression-bypass, monolithic-cell. Layer-conflation treats the DNA layer (stabilized orchestration substrates, behavior substrates, lifecycle policies that define how a cell functions) and the action layer (recorded task instances, lived experience that accumulates through execution) as the same substrate layer, eliminating the distinct evolution mechanisms each layer supports and the governance properties that depend on keeping them separate. Expression-bypass activates DNA-layer substrates without the governed selection that expression requires — bypassing the harness substrate that determines which sub-substrates are active for a given cell goal. Monolithic-cell packages all substrate content into a single undifferentiated structure without internal layer distinction, making the evolution and governance mechanisms that depend on the DNA/action distinction architecturally unavailable. Formalized in B3.04–B3.06.

**Category 4 — Lifecycle Anti-Patterns (violating B1.09–B1.11).**
Anti-patterns: ungoverned-birth, silent-death, untracked-mating. Ungoverned-birth instantiates new cells, aspects, or Selves without governed origination — producing no substrate record, no authority trace, and no lifecycle entry. Silent-death retires a cell, aspect, or Self without governed retirement — making no archival decision, recording no lineage entry, and performing no determination of whether retirement is functional obsolescence or capability supersession. Untracked-mating combines content from multiple cells without recording the combination as a governed lifecycle event, leaving the resulting cell carrying content from multiple lineages with no traceable parentage and no governed account of which mating pattern was applied. Formalized in B3.07–B3.09.

**Category 5 — Evolution Mechanism Anti-Patterns (violating B1.12–B1.15).**
Anti-patterns: single-mechanism, ungoverned-mutation, ungoverned-directed-selection, silent-drift. Single-mechanism relies on only one of the three evolution mechanisms — instinct evolution, DNA evolution, or action-feedback evolution — and neglects the productive tension among all three that Paper 2 commits to. Ungoverned-mutation allows instinct-layer evolution (LLM and infrastructure updates) to propagate into the substrate without governed assessment, letting capability changes in the instinct layer silently alter the architecture's effective behavior. Ungoverned-directed-selection modifies DNA-layer content — orchestration substrates, behavior substrates, lifecycle policies — without the human governance that directed selection requires, effectively allowing the governed reasoning layer to evolve without governance. Silent-drift allows the architecture to evolve across horizontal and vertical axes without governed tracking, so the architecture changes but the changes are not recorded as substrate content and cannot be traced, reverted, or audited. Formalized in B3.10–B3.13.

**Category 6 — Evolution Direction Anti-Patterns (violating B1.16).**
Anti-pattern: unidirectional-evolution. Evolution proceeds along only one axis — either content evolves without structure being updated to support it (pure horizontal evolution, accumulating content within a fixed structural arrangement that may no longer fit), or structure is refactored without the content evolution that should accompany it catching up (pure vertical evolution, reorganizing structure while leaving content misaligned). The instinct/reasoning boundary is treated as a fixed architectural given rather than as governed substrate content that can and should be updated as the instinct layer evolves and as organizational needs change. Formalized in B3.14.

**Category 7 — Role and Domain Anti-Patterns (violating B1.17–B1.18).**
Anti-patterns: intrinsic-type-assignment, implicit-content-domain. Intrinsic-type-assignment treats structural roles — cell, aspect, and Self participation — as intrinsic properties of artifacts rather than as relational and purpose-defined. This prevents the same underlying artifact from participating in multiple structural arrangements, blocks cell reassignment across aspects as the structure evolves, and treats the three-level architecture as a rigid hierarchy rather than as a flexible composition governed by purpose. Implicit-content-domain treats an aspect's content domain — the cells it operates over for its purpose — as implicit or emergent rather than as explicitly governed substrate content, making it impossible to track which cells an aspect operates over, to update that membership under governance, or to inspect the content domain boundary as the architecture evolves. Formalized in B3.15–B3.16.

**Category 8 — Access and Governance Anti-Patterns (violating B1.19–B1.20).**
Anti-patterns: ungoverned-cross-level-access, deployment-level-only-governance. Ungoverned-cross-level-access allows the Self to access cells directly without governed routing, bypassing the aspect-level coordination layer and preventing cross-aspect coordination from operating as a first-class architectural capability. Deployment-level-only-governance locates governance mechanisms at the deployment layer rather than at the substrate layer, making governance contingent on a particular deployment configuration rather than architecturally invariant — so that governance is present when the deployment is configured to provide it, absent when the deployment changes, and not traceable to the substrate as its source of authority. Formalized in B3.17–B3.18.

**Cross-cutting anti-patterns (B3.22–B3.30)** span multiple commitment categories. They cover configurations in which violations of multiple commitments interact to produce failure modes that no single-commitment anti-pattern captures. The cross-cutting taxonomy is established in the respective notes; approximately nine cross-cutting anti-patterns complete Phase B3.

## 5. Anti-Patterns and Remediation: Every Anti-Pattern Has a Governed Path to Correction

A defining property of anti-patterns in the CKS architecture is that every one has a governed remediation path. Remediation is not through workarounds, deployment-layer patches, or configuration adjustments that leave the underlying architectural configuration unchanged. It is through the governed mechanisms that Phase B2 established as the positive commitment architecture.

This property — every anti-pattern has governed remediation — is architecturally significant. It follows from the design: Phase B2's positive commitment decompositions specify the governed mechanisms precisely enough that each anti-pattern's remediation path can be traced to specific Phase B2 notes. Instinct-reasoning-collapse is remediated by restoring the substrate as the governed reasoning layer, establishing the instinct/reasoning boundary as governed substrate content, and ensuring that instinct-layer evolution does not propagate silently into the governed reasoning layer — all through the mechanisms B2.01–B2.10 and their parent B1.01 establish. Ungoverned-birth is remediated through the birth governance process that B1.06 and its Phase B2 decompositions establish, including the substrate record, the authority trace, and the lifecycle entry that governed origination requires. Untracked-mating is remediated through the mating governance process that B1.07 and its Phase B2 decompositions establish, recording the mating pattern applied, the content contributed by each parent, and the lineage entry the resulting cell carries.

The existence of governed remediation paths also means that anti-patterns are correctable within the architecture rather than requiring rebuilding. The CKS governance architecture is designed so that identifying an anti-pattern activates the governed mechanisms the architecture already provides, not a new remediation framework outside the architecture. This is a prior-art claim in its own right: the governed corrective mechanisms for these specific failure modes are the same mechanisms the positive commitment architecture establishes.

## 6. Relation to Phase B2: Anti-Patterns as the Architectural Negatives of Positive Commitment Decompositions

Phase B3 anti-patterns are the negative architectural counterparts to Phase B2's positive commitment decompositions. The relationship is structural, not merely logical. Each anti-pattern names the recognizable configuration that results when a Phase B2 commitment is not instantiated. Each anti-pattern's recognizable form is the absence or inversion of the architectural property the Phase B2 commitment establishes. Each anti-pattern's remediation path points back to the Phase B2 mechanisms that produce the positive commitment.

Together, Phase B2 and Phase B3 produce a complete architectural map of Paper 2's instinct/reasoning-separated, three-level, governed architecture. Phase B2 answers: what must be true for the architecture to hold? Phase B3 answers: what does the architecture look like when it has failed, and how is failure corrected through governed processes? The map is complete in the sense that every B1.01–B1.20 commitment has a positive decomposition in Phase B2 and a named anti-pattern in Phase B3. No commitment appears only as a positive requirement without a corresponding failure mode. No named failure mode appears without a violated commitment from which it is derived.

This completeness is the prior-art value of Phase B3 in conjunction with Phase B2. It establishes not only that the CKS architecture commits to specific properties but also that the full space of failures against those commitments is known, named, and documented. Any subsequent claim to have identified a failure mode of the instinct/reasoning-separated, three-level CKS architecture must contend with the prior-art record this taxonomy establishes.

## 7. Limits of the Anti-Pattern Taxonomy

Three limits bound Phase B3's scope.

**Anti-patterns are stable failure modes, not every possible error.** Individual implementation mistakes that do not recur across contexts, one-time deviations from a commitment, and configuration gaps that produce no consistent governance failure are not anti-patterns in the sense Phase B3 formalizes. The taxonomy covers recurring configurations that consistently produce governance failures. It does not cover everything that can go wrong in a CKS implementation, only the recognizable architectural shapes that recur and consistently violate the commitments Phase B2 established.

**The taxonomy is not claimed exhaustive.** Approximately 30 notes cover the anti-patterns directly derivable from Paper 2's 20 foundational commitments (B1.01–B1.20) plus cross-cutting configurations. Additional anti-patterns may be derivable from Paper 2 or from the interaction of Paper 1 and Paper 2 commitments in deployed architectures. The current taxonomy formalizes those that are directly derivable from Phase B2's positive decompositions; the taxonomy may be extended by future derivation work without those extensions invalidating the current notes.

**Anti-patterns do not introduce new commitments.** Phase B3 derives entirely from Phase B2's positive commitments and from Paper 2's source architecture. Anti-patterns are the negatives of already-established commitments; they do not add new architectural requirements beyond those Phase B2 established. If a given anti-pattern's remediation appears to require a mechanism not explicitly present in Phase B2's decompositions, the note identifies the Phase B2 commitment from which that mechanism is derived, rather than introducing a new commitment. No new axioms.

## 8. One-Sentence Characterization

The anti-pattern integrating frame establishes that Phase B3 formalizes the specific named stable recognizable failure modes that are the architectural negatives of Phase B2's positive commitment decompositions — each anti-pattern having a recognizable form, a violated B1.xx commitment, predictable operational consequences, and a governed remediation path — thereby completing the prior-art architectural map of Paper 2's instinct/reasoning-separated, three-level, governed architecture by establishing what it commits to and what it looks like when those commitments fail.

## 9. Phase B3 Sequence

Phase B3 comprises approximately 30 notes organized as follows:

**B3.01 (this note)** — Anti-pattern integrating frame. Establishes the definition, standard structure, taxonomy, remediation posture, and prior-art scope for all Phase B3 notes.

**B3.02–B3.21 — Primary anti-patterns, one per B1.01–B1.20 commitment.** B3.02 formalizes the instinct-reasoning-collapse anti-pattern corresponding to B1.01 (the instinct/reasoning separation as independently-evolving layers), which is the foundational commitment of Paper 2 and therefore the foundational anti-pattern of Phase B3. Subsequent notes formalize the primary anti-patterns for B1.02 through B1.20 in sequence — the flat-architecture anti-pattern for the level-structure commitments, the structural anti-patterns (layer-conflation, expression-bypass, monolithic-cell) for the DNA/action and expression commitments, the lifecycle anti-patterns (ungoverned-birth, untracked-mating, silent-death) for the lifecycle primitive commitments, the evolution mechanism anti-patterns for the three-mechanism and multi-axis evolution commitments, the evolution direction and governance-shape anti-patterns for the boundary and governance commitments, and the access and structural anti-patterns for the enterprise-brain and advantage commitments.

**B3.22–B3.30 — Cross-cutting anti-patterns spanning multiple commitments.** These approximately nine notes formalize failure modes that result from the interaction of multiple violated commitments — configurations in which instinct-reasoning collapse reinforces lifecycle governance failures, in which flat-architecture anti-patterns interact with evolution mechanism anti-patterns to produce compounding failures, and other multi-commitment failure modes that single-commitment anti-pattern notes do not individually capture. The cross-cutting notes complete Phase B3 and close the prior-art territory of Paper 2's architectural failure modes.

---

## Source Paper

Li, Wenxin. "The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance." April 2026.

## Related Work

Li, Wenxin. "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems." April 2026. (Paper 1 of the CKS theory series.)

Phase B1 notes (B1.01–B1.20): foundational architectural commitments of Paper 2.

Phase B2 notes (B2.01–B2.110): operational decompositions of B1.01–B1.20 commitments.

## Self-Citation

This note is part of the CKS derivation-note series. It is the first note of Phase B3 and the 328th note in the series. The preceding note is B2.110; the following note is B3.02 (instinct-reasoning-collapse anti-pattern).
