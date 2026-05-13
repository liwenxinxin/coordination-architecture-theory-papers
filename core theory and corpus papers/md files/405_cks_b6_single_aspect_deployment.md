# Boundary Case: Single-Aspect Deployment — Multiple Cells Organized Into One Aspect Under One Self, Testing What Self-Level Integration Means When Only One Aspect Exists and What Aspect-Level Coordination Implies When Governing a Large Cell Population

**Note identifier:** B6.03
**Series:** B — Paper 2 Derivation Notes
**Phase:** B6 — Boundary Cases
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

The Coordination Knowledge Substrate (CKS) pattern at Self scope commits to three architectural levels — cell, aspect, Self — with aspects serving as coordination arrangements of cells and the Self as the integrated whole holding multiple coexisting aspects. A single-aspect deployment instantiates this architecture at its structural minimum: multiple cells, all organized as members of one aspect, that one aspect integrated into one Self, three levels present, all architectural commitments applying without exception. This note formalizes the single-aspect deployment as a boundary case that stresses two distinct architectural boundaries simultaneously. The first boundary is Self-level integration at minimum scale: with only one aspect, the Self's cross-aspect conflict handling function is absent, but the Self level retains governance value through the integration architecture container it provides, the instinct/reasoning configuration scope it holds, and the expansion readiness it maintains. The second boundary is aspect-level coordination at maximum scale for a single-aspect deployment: as cell count grows within one aspect, coordination rule complexity grows with it, and the aspect approaches governance capacity limits that the architecture acknowledges but does not specify. The A1.03 conflict registry rate at aspect scope is identified as an operational indicator of scale-limit approach. The decomposition trigger — when the single aspect should be decomposed into multiple aspects — is identified as a governance decision point this boundary case formalizes, with content-domain heterogeneity and conflict registry rate as its primary signals.

---

## 1. Configuration Description

A single-aspect deployment is a CKS Self that is structurally complete but organized at minimum aspect count: multiple cells (five to twenty is a representative range, though the boundary case is not count-specific), all organized as members of one aspect, that one aspect integrated into one Self. Three architectural levels are present and populated.

**Cell level.** Each cell is a full CKS artifact carrying the Paper 1 commitments: substrate content, orchestration rules, human-governed authority, the determinism contract, path retraceability, and all other Paper 1 commitments at cell scope. No cell is simplified or truncated. Cell multiplicity is the defining feature of this configuration — there are enough cells that aspect-level coordination is substantively necessary rather than trivial.

**Aspect level.** One aspect holds all cells as members. The aspect has a defined content domain (B1.18) and coordination rules governing membership, invocation, output integration, and conflict handling (B2.16). The aspect level is populated by a substantive cell population rather than a trivially small one. The single aspect is doing real coordination work across a real cell population.

**Self level.** One Self holds one aspect. The Self carries integration architecture (B2.21), instinct/reasoning configuration (B2.23), and Self DNA governing how the single aspect's outputs are handled at integration scope. The Self level is present and structurally complete, not elided.

All CKS commitments apply in this configuration without exception or modification. The single-aspect deployment is a valid architectural configuration, not a degenerate or incomplete one. What distinguishes it as a boundary case is not that anything is missing — it is that two architectural structures are being exercised at the edges of their respective design ranges simultaneously: the Self is being exercised at minimum aspect count (one), and the aspect is being exercised at maximum cell count for a single-aspect configuration.

---

## 2. Architectural Boundary Being Tested

Three boundaries are tested simultaneously in this configuration.

**Boundary 1 — Self-level integration at minimum aspect count (B1.05).** The Self is defined as the integrated whole that holds multiple coexisting aspects. With one aspect, the Self-level function of integrating multiple aspects has no cross-aspect work to perform. The question this boundary tests is whether Self-level governance adds architectural value beyond what aspect-level governance already provides when only one aspect exists. The question is real: a deployment designer could reasonably ask whether the Self level adds anything the aspect level does not already supply when the aspect count is one.

**Boundary 2 — Aspect-level coordination at large cell count (B1.04).** The aspect is defined as a coordination arrangement of cells serving a particular purpose, operating over its constituent cells as content domain. With many cells in one aspect, the aspect's coordination rules must govern a large population: membership rules covering each cell's participation criteria, invocation rules specifying which cells handle which input types, output integration rules combining outputs from many cells, and conflict handling for conflicts between any pair of cells in the population. Coordination rule complexity grows with cell count. This boundary tests the governance capacity limits of single-aspect coordination.

**Boundary 3 — Three-level value with one aspect (B1.02).** The three-level architecture — cell, aspect, Self — is designed to provide distinct governance value at each level. With one aspect, the aspect-to-Self level boundary is under stress: does the Self level provide distinct governance value, or does it collapse into the aspect level functionally? This boundary tests whether three-level governance remains architecturally meaningful at minimum aspect count.

---

## 3. Governance Implications

**Self-level value with one aspect.** The Self still provides governance value in a single-aspect deployment, but that value is exercised differently than in multi-aspect deployments. Three sources of Self-level value survive the reduction to one aspect.

First, the Self level is the container for the integration architecture per B2.21 — the substrate content that defines how the instinct/reasoning separation operates at integration scope. Even with one aspect, the integration architecture is present and governs how the single aspect's outputs are handled, how they are assembled into the Self's outputs, and how the instinct/reasoning boundary is configured at Self scope per B2.23. This architecture is not trivially equivalent to the aspect's coordination rules; it operates at integration scope, above aspect scope, and it governs the deployment's whole-organism-level behavior rather than the aspect's coordination of its member cells.

Second, Self DNA per B2.21 governs the Self's own operational parameters and behavioral substrates at integration scope. These are distinct from the aspect's DNA content — they pertain to the Self as integrated whole, not to the aspect as coordination arrangement of cells.

Third, the Self level maintains expansion readiness — the architectural preparation for a second aspect to be added. The Self-level integration architecture is a pre-existing governance structure into which a new aspect can be integrated under governance without requiring architectural reconstruction. A deployment without a Self level would need to construct that architecture from scratch when the second aspect arrives; the single-aspect deployment with a Self level has it already in place.

What the Self level does not provide in a single-aspect deployment is cross-aspect conflict handling — the resolution of conflicts between outputs from different aspects. This absence is not a deficiency; it reflects the configuration. The Self level's cross-aspect conflict handling is on standby, ready to activate when a second aspect is added. The absence of cross-aspect conflicts in a single-aspect deployment is architecturally expected, not architecturally concerning.

The governance risk is the converse: if the Self-level integration architecture is not kept substantively current — if it degrades into a nominal container without genuine integration governance substance — the deployment approaches the Unintegrated Self anti-pattern (B3.06, Form 1: nominal Self without integration governance substance). Preventing this requires that the humans governing the deployment actively maintain the Self-level integration architecture as a live governance artifact, not merely as a structural placeholder.

**Aspect coordination complexity with large cell count.** A single aspect coordinating many cells bears a governance burden that grows with cell count. Four coordination rule categories each increase in complexity.

Membership rules (B2.08) must define each cell's participation criteria precisely enough that the aspect's operations produce coherent outputs rather than incoherent mixtures. With many cells, these rules must be comprehensive and non-overlapping in their coverage.

Invocation rules must specify which cells handle which input types. With many cells, this specification grows into a routing governance structure — one that must be authorable, maintainable, and legible by the humans governing the aspect.

Output integration rules must combine outputs from potentially many cells into a single aspect-level output. The complexity of these rules grows with the number of cells whose outputs must be integrated, particularly when cell outputs are heterogeneous in form or scope.

Conflict handling per A1.03 must address conflicts between any pair of cell outputs. In a population of N cells, the potential conflict surface is large — not every pair will conflict, but the coordination rules must specify how conflicts are handled for any pair that does. The A1.03 conflict registry at aspect scope records conflicts as first-class objects; as cell count grows, the conflict registry rate (conflicts per unit of operations) becomes an operational indicator of whether the cell population is too heterogeneous for single-aspect coordination to govern coherently.

A conflict registry rate that grows steadily over the period during which new cells were added, without a corresponding growth in governance-authored conflict resolutions, suggests that cells in the aspect are serving functionally distinct content domains that have been placed under one aspect by structural convenience rather than by genuine content-domain coherence. This is the primary operational signal that aspect decomposition may be warranted.

**Expansion readiness as an ongoing governance obligation.** A single-aspect deployment with many cells may be stable for a long period, but governance should treat it as a deployment that is approaching — rather than safely distant from — the point where aspect decomposition becomes warranted. This means: reviewing the aspect's content domain per B1.18 periodically to assess whether it has become heterogeneous; monitoring the conflict registry rate at aspect scope; and maintaining documented awareness of which groups of cells could be decomposed into which candidate aspects if decomposition were authorized. This awareness does not require action until the governance decision is made; it requires readiness.

---

## 4. Boundary Tests

Three operational tests determine whether a single-aspect deployment is maintaining architectural integrity under this configuration.

**(a) Self-level integration architecture substance test.** Does the Self level carry a meaningful integration architecture per B2.21 that would survive multi-aspect expansion? A Self-level integration architecture that is substantive will specify: how the single aspect's outputs are assembled at integration scope, how the instinct/reasoning boundary per B2.23 is configured at Self scope, and how Self-level DNA governs the deployment's whole-organism behavior. A nominal Self — one present in structure but carrying no integration governance substance — fails this test and exhibits B3.06 Form 1 symptoms. The test is passed if the integration architecture could be extended to govern a second aspect without requiring reconstruction — that is, if the architecture is genuinely built for multi-aspect integration rather than retrofitted for single-aspect pass-through.

**(b) Aspect coordination coverage test.** Do the single aspect's coordination rules per B2.16 effectively govern all member cells, or are some cells effectively ungoverned within the large membership? Each cell in the aspect should be covered by: at least one membership rule establishing its participation criteria, at least one invocation rule establishing the input conditions under which it is invoked, and conflict-handling rules covering its pairwise interactions with other cells whose content domains overlap. A cell population in which some cells lack explicit coordination rule coverage has governance gaps — portions of the aspect's coordination that depend on implicit or emergent behavior rather than authored rules. The test is passed if every cell has explicit coverage across all three rule categories.

**(c) Conflict registry rate as heterogeneity indicator.** Does the A1.03 conflict registry at aspect scope show a growing conflict rate, suggesting the cell population is too heterogeneous for single-aspect coordination? The test is not a threshold — the architecture does not specify a conflict rate above which decomposition is required. Rather, the test is directional: a conflict rate that has grown steadily over the period during which new cells were added is evidence that the aspect's content domain has expanded beyond its coherent governance range. A stable conflict rate, even at a non-trivial level, suggests the aspect's coordination rules are governing the conflicts effectively. The test is passed if the conflict rate is stable and governance is actively resolving conflicts through authored rules rather than allowing them to accumulate as deferred obligations.

---

## 5. Stress Points

**Self-level governance hollowness.** The most serious stress point in a single-aspect deployment is that the Self level may develop nominal presence without governance substance. With no cross-aspect conflict handling to perform, the humans maintaining the Self-level integration architecture may allow it to remain static — present in structure, but not updated to reflect the deployment's current operational state. Over time, a static Self-level integration architecture becomes governance debt: the architecture becomes harder to extend when a second aspect is added because it has not been kept current with the deployment's evolving capabilities and cell population. The stress point is managed by treating the Self-level integration architecture as a live governance artifact requiring periodic review even in the absence of cross-aspect conflict handling pressure.

**Aspect scale limit approach.** As cell count grows, the single aspect approaches coordination complexity limits. The specific form of stress is authoring burden: the humans governing the aspect must maintain coordination rules that cover an increasingly large cell population. At some point, the authoring burden becomes unmanageable not because the architecture fails but because human governance capacity for rule authoring and maintenance has a practical ceiling. The stress point manifests as: invocation rules that become difficult to maintain as a coherent whole; conflict handling rules that increasingly depend on general policies rather than specific authored resolutions; and output integration rules that approximate rather than precisely combine cell outputs. Each of these is a governance quality indicator rather than an architectural failure mode — the architecture does not break, but governance quality degrades. In the limit, the aspect may develop coordination governance failures in which cells are nominally members but are governed only by general fallback policies rather than by purposive authored rules. This configuration is related to, but distinct from, the Monolithic Cell anti-pattern (B3.09): rather than one cell being too large, many cells governed by rules of inadequate specificity create the equivalent coordination failure at aspect scope.

**Premature decomposition.** The converse stress point is decomposing an aspect that does not yet require decomposition. If the aspect's content domain is genuinely coherent and the conflict registry rate is stable, decomposing the aspect into multiple aspects introduces coordination overhead at the Self level — cross-aspect conflict handling now required, Self-level integration architecture now governing multiple aspects — without proportionate governance benefit. Decomposition should be governed by indicators, not by cell count alone. A large cell population under coherent single-aspect governance is architecturally sound; an aspect that governs an incoherent cell population is the failure mode, regardless of absolute cell count.

---

## 6. Architectural Limits

The CKS architecture does not specify a maximum cell count per aspect. This is a deliberate architectural choice: the architecture's commitments apply at any cell count, and specifying a maximum would introduce a constraint the architecture does not need to enforce in order for its commitments to hold. The architecture's commitments — governance-boundary inheritance at every level, conflict preservation, human-governed authority, path retraceability — are count-independent.

What the architecture does not specify, human governance must determine. The practical governance capacity limit — the cell count at which a single aspect becomes too complex for its coordination rules to be authored and maintained with acceptable quality — is a function of the content domain's heterogeneity, the humans' governance capacity, and the organizational context of the deployment. It is not a universal number, and the architecture rightly does not attempt to fix it.

The single-aspect deployment boundary case formalizes the governance considerations approaching that determination. Its contribution is not to specify the limit but to name the indicators governance should monitor — Self-level integration architecture substance, aspect coordination rule coverage, A1.03 conflict registry rate — and the architectural consequence of passing the limit without acting: coordination governance failures in which the aspect nominally governs its cells but some cells are effectively ungoverned by authored rules, with coordination quality degrading across the cell population.

The decomposition decision, when governance makes it, is architecturally straightforward: it is a reorganization of cells into multiple aspects under the same Self, a substrate-edit operation under human authority per the Paper 1 human-governed commitment. The architecture supports the operation without modification. What precedes the decision is the governance readiness this boundary case describes — the ongoing monitoring, the expansion readiness maintained at Self level, and the documented awareness of which cells would constitute which candidate aspects when the time comes.

Two additional architectural observations bound the analysis. First, the single-aspect deployment is not an unstable transitional configuration that governance must resolve quickly; it may be the correct long-term configuration for a deployment whose cell population serves a genuinely coherent content domain. The boundary case does not argue for adding aspects; it argues for monitoring the indicators that would warrant doing so. Second, the Self-level integration architecture is not idle in a single-aspect deployment even in the absence of cross-aspect conflict handling. It is performing the integration governance work that makes the deployment coherent as a Self — holding the instinct/reasoning boundary, governing the deployment's whole-organism behavior, and maintaining the architectural readiness for expansion. That work is the Self level's value in this configuration.

---

## 7. Summary

The single-aspect deployment tests two architectural boundaries simultaneously: Self-level integration at minimum aspect count and aspect-level coordination at large cell count. The Self level retains governance value in this configuration through three mechanisms — the integration architecture container, the instinct/reasoning configuration scope, and expansion readiness — even though cross-aspect conflict handling is absent. The aspect level approaches governance capacity limits as cell count grows, with the A1.03 conflict registry rate at aspect scope serving as the primary operational indicator of approaching limits. The decomposition trigger is a governance decision point, not an architectural threshold; the architecture does not specify a maximum cell count per aspect, but governance must act before coordination quality degrades to the point where cells are effectively ungoverned within the aspect's membership. The Self-level integration architecture must be maintained as a live governance artifact throughout, regardless of whether cross-aspect conflict handling is active, in order to prevent the nominal-Self failure mode that would undermine the deployment's three-level architectural integrity.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Boundary Case: Single-Aspect Deployment — Multiple Cells Organized Into One Aspect Under One Self, Testing What Self-Level Integration Means When Only One Aspect Exists and What Aspect-Level Coordination Implies When Governing a Large Cell Population.* May 13, 2026. ORCID: 0009-0004-8065-3235.
