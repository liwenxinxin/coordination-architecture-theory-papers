# Distributed Failure Localization Inherits Paper 1's Substrate-Cell Boundary

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to establish, in operational form, that Paper 2's distributed failure risk property — the architectural commitment that failures in a multi-level CKS Self are localized rather than catastrophic — inherits directly from the substrate-cell boundary failure localization that Paper 1 commits to in its Claim 1 hybrid and A1.02 sub-commitments. The three-level structure Paper 2 introduces extends one localization boundary to three equivalent boundaries, each functioning by the same four mechanisms Paper 1 established. The extension is addition, not substitution.

## Abstract

Paper 1 commits to a substrate-cell boundary (A1.02) that localizes failures at cell scope: when a cell produces bad output, the substrate remains independently persistent, the bad output is captured as a first-class conflict object rather than propagating silently, cells cannot directly affect each other's state (A2.12, no-direct-channels), and human governance can correct the failure directly via the inspect, modify, and override rights. This single localization boundary is load-bearing for Paper 1's conflict preservation and governance commitments. Paper 2's three-level architecture — cell, aspect, Self — creates three equivalent localization boundaries: cell-to-aspect, aspect-to-Self, and the inherited substrate-cell boundary operating within each cell. Each boundary uses the same four mechanisms. This note formalizes the inheritance edge (Paper 2 distributed failure risk ⊃ Paper 1 substrate-cell boundary failure localization), identifies what is preserved at each boundary, names what is genuinely new in Paper 2's extension, connects the failure localization property to Series B's anti-pattern analysis, and provides an operational test for verifying cell-level failure containment in a live deployment.

## 1. Paper 1's substrate-cell boundary as a failure localization mechanism

Paper 1's substrate-cell boundary is commonly read as a structural boundary between two layers — the substrate that holds persistent coordination knowledge and the cell that executes over it. The boundary is that, but it is also a failure localization mechanism. The localization property follows directly from the four things the boundary commits to.

**Substrate persistence through cell failures.** The substrate is governed independently of cell behavior. A cell that produces bad output, halts midway, or executes incorrectly cannot corrupt the substrate because the substrate's persistence and structure are architectural properties independent of any particular cell execution. The bad outputs a failing cell produces are not invisible to the system; they are recorded as substrate content with attribution and provenance.

**Bad outputs as first-class conflict objects.** Once recorded as substrate content, a failing cell's bad outputs become subject to Paper 1's conflict preservation commitment (Claim 2 / A1.03). Contradictions in substrate content — including contradictions between a failing cell's output and prior substrate state — are preserved as live, addressable substrate state rather than collapsed silently. A bad output does not disappear; it becomes a first-class conflict object that governance can inspect and act on. This is the failure capture mechanism: failures do not propagate silently through the substrate because any output that contradicts established substrate content registers as a conflict rather than overwriting it.

**No-direct-channels between cells.** The no-direct-channels commitment (A2.12) means that cells cannot directly affect each other's state. A failing cell cannot reach into an adjacent cell's execution state or directly corrupt what another cell reads. Failure propagation can occur only through substrate content: if a failing cell writes bad content to the substrate, and another cell later reads that content, the substrate's conflict preservation mechanism catches the contradiction at the substrate layer, where governance can act on it. The failure path always runs through governed substrate content, never through ungoverned cell-to-cell channels.

**Governance correction via the three rights.** Human governance can inspect any substrate content, modify it, and override any operation touching it at any time. If a cell failure produces bad substrate content, governance can correct the substrate directly without needing to reach inside cells, restart the system, or wait for a scheduled checkpoint. The correction mechanism is available at the substrate layer, which is the layer where failures are captured.

These four mechanisms together make the substrate-cell boundary a structural fence: failures in the cell layer are contained at the substrate layer's edge rather than propagating outward through the system.

## 2. The inheritance edge: Paper 2 ⊃ Paper 1

Paper 2's three-level architecture — cell, aspect, Self — introduces two structural levels above the cell. Each level has its own substrate layers: the DNA layer (orchestration content carrying behavioral rules) and the Action layer (recorded task instances and execution traces). Each level boundary creates a new localization fence that functions using exactly the same four mechanisms Paper 1's substrate-cell boundary uses.

The inheritance relationship is: **Paper 2's distributed failure risk property contains Paper 1's substrate-cell boundary failure localization as its foundation**. Paper 2 does not replace Paper 1's single boundary; it extends the architecture so that the same localization mechanisms operate at three boundaries rather than one.

### What is preserved at each level boundary

**Substrate persistence through failures.** At the cell-to-aspect boundary: a failing cell does not corrupt the aspect's DNA layer or Action layer. The DNA layer — the aspect's orchestration content — is governed independently of any cell execution within the aspect. A cell producing bad output writes to substrate content that the aspect's DNA layer is not identical with; the DNA layer persists. At the aspect-to-Self boundary: a failing aspect does not corrupt the Self's structural substrate objects. The Self's integration architecture is governed independently of any individual aspect's coordination outputs. Substrate persistence inherited from Paper 1 operates at every level.

**Bad outputs as first-class conflict objects.** At each level boundary, bad outputs crossing the boundary become first-class conflict objects by direct inheritance of Paper 1's conflict preservation commitment. A cell within an aspect that produces bad output captures that output as a conflict at the cell-aspect boundary. An aspect whose coordination rules produce bad outputs crossing to the Self level creates a conflict at the aspect-Self boundary. At no level is a bad output silently absorbed; the conflict preservation mechanism operates at every boundary.

**No-direct-channels at each level.** Cells within an aspect cannot directly affect each other's state — the A2.12 no-direct-channels commitment applies at cell scope within aspects as the direct inheritance of Paper 1's commitment. At the aspect level, aspects do not directly affect each other's substrate state; inter-aspect coordination runs through the Self's governed substrate content, not through direct aspect-to-aspect channels. The no-direct-channels property that localizes cell failures in Paper 1 generalizes to every level of the Paper 2 architecture.

**Governance correction at each level via the three rights.** Human governance retains the inspect, modify, and override rights at every level boundary. A cell-level failure is addressable at cell scope — governance does not need to reach into the aspect's DNA layer or the Self's integration architecture to correct a cell's bad output. An aspect-level failure is addressable at aspect scope. Self-level failures are addressable at Self scope. The three rights that Paper 1 commits to as the failure recovery mechanism operate at every level in Paper 2.

## 3. What is new in Paper 2

The inheritance described in §2 establishes continuity. Three features of Paper 2's failure localization commitment are genuinely new — not derivable from Paper 1's single substrate-cell boundary.

**Three-level failure localization.** Paper 1 committed to one failure localization boundary: the substrate-cell boundary. Paper 2 commits to three: cell-to-aspect, aspect-to-Self, and the inherited substrate-cell boundary operating within each cell as each cell's own internal localization fence. The count of boundaries is new. A deployment with one aspect containing ten cells has, by architecture, eleven localization fences active simultaneously — ten cell-internal substrate-cell boundaries (one per cell, inherited from Paper 1) plus the cell-to-aspect boundary that contains failures from any of those ten cells within aspect scope rather than propagating them to the Self level.

**Level-specific failure types with distinct governance responses.** Paper 1's failure localization addressed one failure type: a cell producing bad output or failing to execute at cell scope. Paper 2 introduces a taxonomy of three failure types with level-specific governance responses. A cell failure — a cell producing bad output or halting — is localized within cell scope; other cells in the same aspect continue operating; governance addresses it at cell scope without touching the aspect's DNA layer or the Self's integration architecture. An aspect failure — an aspect whose coordination rules produce bad cross-cell outputs — is localized within aspect scope; other aspects in the Self continue operating; Self-level integration continues operating over healthy aspects. A Self failure — a Self whose integration architecture produces bad cross-aspect outputs — is localized within Self scope. In a multi-Self deployment extending beyond Paper 2's single-Self scope, other Selves continue operating independently. This failure type taxonomy — cell failure, aspect failure, Self failure, each with distinct governance responses and distinct localization properties — is new relative to Paper 1's single failure type.

**Multi-level failure localization as an explicit architectural property.** Paper 1's substrate-cell boundary produced failure localization as a consequence of the boundary's structural commitments; the localization was a property of the boundary rather than a named architectural property of the paper's design. Paper 2 explicitly positions multi-level failure localization as a named architectural property of the three-level design — the architecture is designed to contain failures at the level where they occur, and this designed containment is one of Paper 2's three enterprise-application architectural properties (alongside linear-cost composition at Self scope and structural co-adaptation). The explicit architectural naming and the positioning of failure localization as a design outcome, rather than a structural consequence, is new.

## 4. Why anti-patterns are locally bounded: the failure localization explanation

Series B's anti-pattern catalogue includes two governance failures at the structural level that are relevant here. The Unintegrated Self anti-pattern (a Self whose aspects are not integrated into a coherent whole) and the Purposeless Aspect anti-pattern (an aspect that holds cells without a coordination purpose that serves the Self) are governance failures — they represent states that should not persist under active governance — but they are not catastrophic system failures. A deployment in the Unintegrated Self state does not collapse; it operates with degraded cross-aspect coordination. A deployment containing a Purposeless Aspect does not corrupt the cells outside that aspect or bring down the Self.

The failure localization commitment explained in §2 and §3 is the structural reason why. The aspect-to-Self boundary localizes the effects of an Unintegrated Self within the Self's boundary, preventing failure propagation to other Selves in a multi-Self deployment. The cell-to-aspect boundary localizes the effects of a Purposeless Aspect within that aspect's boundary, leaving other aspects in the Self unaffected. The no-direct-channels property at the aspect level prevents a Purposeless Aspect from directly corrupting the substrate content other aspects operate over. The governance correction mechanism is available at aspect scope to address either failure directly.

This is why the anti-patterns are bounded rather than catastrophic: the architecture that produces the distributed failure risk property is the same architecture that contains the governance failures Series B formalizes. The localization commitment is not an add-on; it is the structural explanation for the anti-patterns' bounded character.

## 5. Prior-art significance

This inheritance note forecloses three classes of adversarial claims.

First, a claim that multi-level failure localization in AI governance architectures — the property that cell, aspect, and Self failures are each contained at their respective boundaries — is a novel architectural contribution relative to Paper 1's substrate-cell boundary localization. The inheritance established here shows that multi-level localization is a direct structural extension of Paper 1's single-boundary localization: the same four mechanisms operating at three boundaries rather than one. The count of boundaries is new; the localization mechanisms are not.

Second, a claim that level-specific failure types (cell failure, aspect failure, Self failure) require novel containment mechanisms beyond Paper 1's substrate-cell boundary commitments. This note establishes that each level-specific failure type is contained by the same substrate persistence, conflict capture, no-direct-channels, and governance correction mechanisms that Paper 1 committed to. The taxonomy of failure types is a Paper 2 contribution; the containment mechanism at each type is inherited.

Third, a claim that the no-direct-channels property at aspect scope — aspects cannot directly affect each other's substrate state — is novel relative to Paper 1's cell-to-cell no-direct-channels commitment (A2.12). The aspect-level no-direct-channels property is a direct structural generalization of Paper 1's commitment, applying the same architectural rule at the next level of composition.

## 6. Operational test

For a deployment implementing Paper 2's three-level architecture, the following test verifies that cell-level failure localization is functioning as the inheritance from Paper 1 predicts.

Suppose a cell within a named aspect produces bad output — for concreteness, a cell whose execution yields a substrate write that contradicts established substrate content at the cell's own level.

An observer verifying correct failure localization should be able to confirm all of the following:

1. **Aspect-level DNA and Action layer unaffected.** The aspect's DNA layer — the orchestration content governing cell behavior within the aspect — is unchanged by the cell failure. No cell execution, however malformed, can write to the DNA layer directly; writes to the DNA layer require the governed evolution machinery. The aspect's Action layer records the cell's bad output as a substrate entry with attribution, but the layer's structure — the schema and organization of the action-layer substrate — is unaltered. An observer can read the aspect's DNA and Action layer content after the cell failure and verify that neither has been corrupted relative to their pre-failure state.

2. **Failure captured as first-class conflict at the cell-aspect boundary.** The bad output has been recorded as substrate content with provenance. If it contradicts prior substrate state, the contradiction is preserved as a live, addressable conflict object rather than silently resolved or silently absorbed. An observer can inspect the conflict in the substrate directly — reading its constituent claims, their provenance records, and the timestamp of the contradiction's registration — without needing to reconstruct it from logs.

3. **Governance correction at cell scope is sufficient.** Human governance can address the cell failure by acting on the substrate content at cell scope — modifying or overriding the bad output directly via the modify right, or resolving the conflict object via a human-authored orchestration rule — without requiring any action at aspect scope or Self scope. The aspect's DNA layer does not need to be modified. The Self's integration architecture does not need to be touched. Other cells in the aspect do not need to halt. An observer confirms this by verifying that the governance correction action targets only the cell-level substrate content, that the aspect and Self continue operating normally during and after the correction, and that the correction is itself recorded as substrate content with the correcting actor's attribution.

A deployment that fails any of (1)–(3) has allowed cell-level failure to propagate beyond the cell-aspect boundary, violating the localization commitment this note formalizes.

## 7. Conclusion

Paper 1's substrate-cell boundary commits to four mechanisms — substrate persistence through failures, bad outputs as first-class conflict objects, no-direct-channels between cells, and governance correction via the three rights — that together make the boundary a structural failure localization fence. Paper 2's three-level architecture extends this single fence to three equivalent fences: cell-to-aspect, aspect-to-Self, and the inherited substrate-cell boundary operating within each cell. Each fence uses the same four mechanisms. The distributed failure risk property that Paper 2 names as an enterprise-application architectural property inherits its localization mechanisms entirely from Paper 1's substrate-cell boundary commitment. What Paper 2 adds is three-level coverage, a taxonomy of level-specific failure types with distinct governance responses, and the explicit architectural positioning of multi-level failure localization as a design property rather than a structural consequence. The inheritance is substantive continuity plus genuine extension.

Series C continues with C1.30, the final note in this series, formalizing the inheritance edge between Paper 2's structural co-adaptation commitment and Paper 1's tool-agnosticism and non-specialist governance commitments.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Distributed Failure Localization Inherits Paper 1's Substrate-Cell Boundary.* May 14, 2026. ORCID: 0009-0004-8065-3235.
