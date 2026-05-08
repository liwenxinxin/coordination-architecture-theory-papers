# Level-Instantiation Patterns: Operational Specialization of Birth at Cell, Aspect, and Self Scope in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as an operational variant of the birth primitive committed in B1.09, the three level-specific instantiation patterns by which new entities are brought into being at the cell, aspect, and Self levels of the three-level structure committed in B1.02. This note closes a four-note decomposition of B1.02 (B2.07 level-distinct scope, B2.08 level-membership, B2.09 level-distinguishability, B2.10 level-instantiation patterns); subsequent Phase B2 notes begin the B1.03 cell level decomposition with B2.11–B2.14.

## Abstract

Paper 2 of the CKS theory series introduces three architectural levels — cell, aspect, and Self — and specifies that birth is the human-governed creation of new entities at any of these levels. Paper 2 commits the levels to having distinct scope (the cell handles a specific informational task, the aspect coordinates cells for a purpose-defined mode of engagement, the Self holds multiple aspects as facets of one CKS-governed intelligence) and commits birth to operating across all three levels. What Paper 2 does not separately formalize is that the birth primitive necessarily admits three operational specializations — one per level — because the level-specific scope each level carries determines what specifications the birth event must compose. This note formalizes those three specializations as **level-instantiation patterns**: cell instantiation, aspect instantiation, and Self instantiation. Each pattern is a governable specialization of birth that takes level-appropriate specifications and produces a level-distinct entity inheriting Paper 1 commitments at the level's scope per B1.20. The note states each pattern precisely, identifies what is shared across patterns and what is level-specific, distinguishes the level-specific structure from the single-pattern instantiation typical of conventional AI architectures, and provides an operational test for whether a deployment instantiates the patterns as the architecture commits them.

## 1. Why level-instantiation patterns need to be formalized as standalone

The B1.02 commitment — three architectural levels, with relational rather than intrinsic role membership — is operationally underspecified until the question is answered: when a deployment creates a new cell, a new aspect, or a new Self, what does the creation event consist of, and in what does it differ across the three levels?

The B1.09 commitment — birth as human-governed origination — answers half of this question by stating the governance posture: humans govern, labor is allocable per A1.12, the birth event is recorded with provenance per A2.40. What B1.09 does not separately answer, because B1.09 is stated at the generic-level scope shared across cell, aspect, and Self, is what the level-specific specifications inside the birth event must contain. A cell birth event composes a different specification set than an aspect birth event, which composes a different specification set than a Self birth event. Treating birth as a single undifferentiated primitive blurs the level-distinct scope that B2.07 commits to and leaves deployments without a principled vocabulary for the three different operational moves they actually perform.

The remedy is to name the three operational specializations of birth as standalone patterns. B1.09 commits the governance posture; this note commits the level-specific specification structure. The two together — generic governance plus level-specific specification — close the operational decomposition of B1.02 across its four notes (B2.07 scope, B2.08 membership, B2.09 distinguishability, B2.10 instantiation). After B2.10, Phase B2 proceeds to decompose B1.03 (the cell level) starting at B2.11.

This note is thus the closing decomposition note for B1.02. Its strategic role in the series is to formalize the operational moves that produce entities at each level, given that the three levels are now committed to having distinct scope (B2.07), substrate-resident membership (B2.08), and operational distinguishability (B2.09).

## 2. The three patterns precisely stated

A **level-instantiation pattern** is a governable specialization of the birth primitive (B1.09) that takes level-appropriate specifications and produces a new entity at the corresponding level. Three patterns are committed: one for each of the three levels of B1.02.

### Cell instantiation

Creating a new cell composes the following specifications, authored as substrate-resident rules per A2.04:

- **Cell substrate content** — the structured representations the cell will carry as its informational task domain.
- **DNA-layer initial content** per B1.06 — the orchestration and behavior substrates that define how the cell functions (harness logic, conflict-handling rules, lifecycle policies, schemas).
- **Harness substrate** per B1.07 — the human-governed substrate that determines which sub-substrates of the cell's DNA are active for current activity.
- **Carry-strategy choice** — full Self DNA with selective expression (when lineage and reconstitution matter) or partial slice (when storage and cognitive load matter more); the choice is per-cell and per-deployment.
- **Initial empty Action layer** — the layer that will accumulate recorded task instances; empty at instantiation.
- **Type declaration** per B2.09 — the operational marker identifying the new entity as a cell, supporting level-distinguishability.

The instantiation event is recorded with provenance per A2.40. The newly instantiated cell inherits Paper 1 commitments at cell scope per B1.20.

### Aspect instantiation

Creating a new aspect composes the following specifications, authored as substrate-resident rules per A2.04:

- **Aspect coordination rules** per B1.04 — the rules that govern how the aspect asks pattern questions across its constituent cells for its purpose.
- **Initial cell-membership assignments** per B2.08 — the substrate-resident records that mark which cells participate in the aspect at the moment of instantiation.
- **Aspect purpose specification** — the purpose-defined frame that determines the aspect's coordination mode of engagement and selects which cells are members.
- **Type declaration** per B2.09 — the operational marker identifying the new entity as an aspect.

The instantiation event is recorded with provenance per A2.40. The newly instantiated aspect inherits Paper 1 commitments at aspect scope per B1.20.

### Self instantiation

Creating a new Self composes the following specifications, authored as substrate-resident rules per A2.04:

- **Self integration architecture** per B1.05 — the structure by which multiple aspects are held as facets of one CKS-governed intelligence.
- **Initial aspect collection** — the aspects the Self holds at the moment of instantiation.
- **Instinct/reasoning separation configuration** per B1.01 — the deployment-specific configuration that pins the boundary between the LLM instinct layer and the CKS reasoning substrate at Self scope.
- **Self-level rules** per B1.05 — the rules that govern Self-level behavior, including cross-aspect coordination and the instinct/reasoning boundary's substrate content.
- **Type declaration** per B2.09 — the operational marker identifying the new entity as a Self.

The instantiation event is recorded with provenance per A2.40. The newly instantiated Self inherits Paper 1 commitments at Self scope per B1.20.

### Shared governance pattern, level-specific specifications

Across all three patterns, the governance posture is the same: humans govern the instantiation per A1.01; labor is allocable across the three modes named in A1.12 (direct human, LLM under human direction, stable cells executing under orchestration rules); the instantiation event is recorded with the six provenance metadata fields named in A2.40; the result is path-retraceable per A1.07 and deterministic given the specifications per A1.10. What differs across the three patterns is the **specification content** the birth event composes — cell-specific specifications differ from aspect-specific, which differ from Self-specific. The patterns share the architectural shape of governance and differ in the level-specific specification structure. Naming this shared-governance/level-specific-specifications split is what the standalone treatment formalizes.

## 3. What makes level-instantiation patterns distinctive

Conventional AI architectures often treat instantiation as a single pattern: a component is "created" through a configuration step that is uniform regardless of the component's role in the larger system. A model is loaded; an agent is launched; a tool is provisioned; the operation is one operation, parameterized.

CKS commits to a different shape. Because the three levels of B1.02 carry distinct scope per B2.07 — cell handles a specific informational task, aspect coordinates cells for a purpose, Self integrates aspects as one whole — the instantiation operation cannot be uniform across them without losing the level-distinct character that B2.07 commits to. Cell instantiation produces an entity whose architectural character is task-handling at cell scope; aspect instantiation produces an entity whose architectural character is purpose-coordination at aspect scope; Self instantiation produces an entity whose architectural character is integrated-intelligence at Self scope. The pattern distinction is not cosmetic; it tracks the level-distinct scope.

Two further architectural features distinguish the patterns from single-pattern instantiation.

**The patterns are governable per A2.04.** Each pattern is itself substrate-resident authoritative content per A2.46, authored as rules. Deployments can inspect, modify, and override the instantiation specifications under the human-governed authority architecture committed in A1.01. Conventional infrastructure-as-code or component-provisioning frameworks may parameterize creation, but they typically do not commit to the specifications themselves being substrate-resident under the same authority architecture as the entities they instantiate. In CKS, the instantiation rules and the entities they produce share one authority layer.

**The patterns produce entities subject to recursive Paper 1 inheritance per B1.20.** A newly instantiated cell carries Paper 1's commitments at cell scope; a newly instantiated aspect carries them at aspect scope; a newly instantiated Self carries them at Self scope. Recursive inheritance is committed at instantiation — it is not added later, and it is not optional per level. This is what makes the levels architecturally homogeneous in their commitments while remaining scope-distinct in their operations.

The level-specific patterns are thus governable, level-scoped, and Paper-1-inheriting at the moment of instantiation. The contrast with conventional single-pattern instantiation is at all three points.

## 4. The biological analog

The patterns parallel biological developmental processes. Different biological cell types — neurons, muscle cells, epithelial cells — are instantiated through different developmental pathways within an organism. Tissues form through specific organogenesis processes. Organisms develop through embryonic development. Biology has level-specific developmental patterns, and the parallels are precise enough that readers absorb the structure quickly.

The architectural substance differs from the biological analog in two respects committed in Paper 2's *Where CKS exceeds biology* treatment. First, biological developmental patterns are evolved, not authored — they are the result of selection over evolutionary timescales, and they are not directly governable. CKS instantiation patterns are authored as rules per A2.04 and revisable through vertical evolution under human governance. Second, biological developmental commitments are bound at species scope and slow to change; CKS instantiation patterns can be revised on operational timescales under directed selection.

The biological analog functions as conceptual scaffold readers absorb quickly because the parallels are intuitive. The architectural work — level-specific governable instantiation under unified human authority — is CKS's own.

## 5. Inherited Paper 1 commitments

Each instantiation pattern inherits the Paper 1 commitments at the appropriate point in the operation:

- **A1.01 human-governed.** Each pattern is governed by human authority over substrate content and orchestration rules. Humans govern instantiation; labor is allocable.
- **A1.07 path retraceability.** Each instantiation event is recorded with the six provenance metadata fields per A2.40, supporting later retracing of the entity's lineage from its instantiation point onward.
- **A1.10 determinism.** Given the specifications, instantiation produces a deterministic entity at the coordination layer; the substrate's deterministic state behavior holds from the moment of instantiation.
- **A1.12 labor allocation.** Instantiation labor — drafting the specifications, populating the initial substrate content, recording the event — is allocable across direct human, LLM-under-human-direction, and stable-cell modes. The architecture supports all three; deployments choose per their requirements.
- **A1.13 composition requirements.** Newly instantiated entities compose with the existing deployment per Paper 1's composition requirements; the patterns do not bypass composition constraints.
- **A2.04 rule authoring.** Each pattern's specifications are authored as orchestration rules — substrate-resident, human-authored, subject to inspection and modification under the broader governance posture.
- **A2.40 provenance.** Each instantiation event carries the six provenance metadata fields, supporting retraceability and accountability per A1.07.
- **A2.46 substrate-resident authoritative content.** The specifications themselves are substrate-resident; they are not held in vendor-side configuration that the human-governed authority architecture cannot reach.
- **B1.20 recursive Paper 1 commitments.** Each instantiated entity inherits all Paper 1 commitments at the appropriate level scope — cell scope for cell instantiation, aspect scope for aspect instantiation, Self scope for Self instantiation.

The patterns do not introduce new commitments; they specialize the birth primitive to the level-distinct scope of B2.07 while preserving the inherited commitments without modification.

## 6. Operational implications

Six implications follow from the patterns at the architectural layer.

**Deployments configure instantiation per level.** A deployment authors three sets of instantiation rules — cell-instantiation rules, aspect-instantiation rules, Self-instantiation rules — informed by what kinds of cells the deployment needs, what aspects coordinate them, and what Selves integrate the aspects. The configuration is per-deployment; the patterns are architectural.

**Patterns evolve through directed selection.** As deployments accumulate operational experience, the instantiation specifications are refined. Birth specifications are themselves substrate content, and DNA evolution as committed in Paper 2 applies — humans direct refinement of the patterns through governed orchestration substrate updates.

**Deployment design produces patterns informed by operational requirements.** What kinds of cells a deployment needs, what aspects coordinate them, what Selves integrate the aspects — each shapes the instantiation specifications. Large deployments may have many instantiation patterns for different cell types, aspect types, and Self configurations.

**Triggers vary, patterns persist.** Instantiation can be triggered by deployment initialization (creating the initial entities at deployment startup), operational expansion (creating new entities as deployment scales), vertical evolution (creating new aspects through restructuring), or mating (creating offspring through cross-layer combination). Each trigger uses level-appropriate patterns; the trigger does not change the pattern, it activates it at the appropriate moment.

**Cross-partner instantiation.** When entity instantiation spans composition partners per A2.47, cross-partner authority is needed for the instantiation specification. The treatment follows A6.12's resolution of multi-author rule authoring conflict during composition — the instantiation specification becomes a multi-authored rule subject to the cross-partner authority architecture.

**Instantiation events are lineage starting points.** Subsequent operations on the entity — mating, death, evolution — reference the birth event recorded at instantiation. The lineage chain begins at the instantiation event; path retraceability per A1.07 traces back to it.

## 7. Limits

Seven limits keep the patterns scoped to what Paper 2 commits to and prevent them from being read as broader than the architecture supports.

**Patterns do not bypass governance.** Each operates within the human-governed authority architecture committed in A1.01. The patterns are governable; they are not governance-replacing.

**Patterns do not prescribe specific specification content.** Deployments configure the specifications per their operational requirements; the patterns commit the structure (what specifications a level-N instantiation must compose), not the content (what those specifications say in any particular deployment).

**Patterns are not exhaustive.** Additional specialized instantiation patterns may be authored at sub-types within a level — different kinds of cells, different kinds of aspects — without contradicting the three level-instantiation patterns. The three patterns commit the level-scoping of instantiation; specialization within a level is open.

**Patterns do not eliminate cross-level coordination.** Cell instantiation may add to aspect membership per B2.08; aspect instantiation may add to Self integration; Self instantiation may compose with adjacent Selves. The patterns operate at level scope, but their effects often touch adjacent levels.

**Patterns do not auto-instantiate.** Every instantiation is an explicit human-governed event under A1.01. The patterns do not prescribe automatic creation; LLMs may perform instantiation labor under A1.12, but the authority remains human.

**Patterns do not replace lifecycle operations.** They operationalize birth per B1.09, but mating per B1.10 and death per B1.11 are separate operations with their own architectural treatments. The lifecycle as a whole is broader than instantiation.

**Patterns do not exempt instantiated entities from recursive Paper 1 inheritance.** Each instantiated entity is subject to all Paper 1 commitments at the appropriate level scope per B1.20. Instantiation is the moment when recursive inheritance becomes operational; it is not an exemption mechanism.

## 8. Operational test

A deployment instantiates the level-instantiation patterns as the architecture commits them if and only if all of the following are true at the time of any instantiation event:

1. The instantiation specification composes the level-appropriate structure: cell substrate + DNA-layer initial content + harness substrate + carry-strategy choice + initial empty Action layer + type declaration for cell instantiation; coordination rules + initial cell-membership assignments + aspect-purpose specification + type declaration for aspect instantiation; Self integration architecture + initial aspect collection + instinct/reasoning separation configuration + Self-level rules + type declaration for Self instantiation.
2. The specification is substrate-resident per A2.46, authored as a rule per A2.04 under human authority per A1.01.
3. The instantiation event is recorded with the six provenance metadata fields per A2.40.
4. The instantiated entity carries the Paper 1 commitments at the level's scope per B1.20.
5. The entity carries the type declaration per B2.09 supporting level-distinguishability.
6. No LLM operation, vendor policy, or runtime middleware can in principle prevent humans from inspecting, modifying, or overriding the instantiation specification or the resulting entity per A1.01.
7. The instantiation occurs under explicit human-governed authority — not automatically — even when LLMs perform the instantiation labor under A1.12.

A deployment that fails any of (1)–(7) at any instantiation event has an instantiation operation that is not CKS-coherent on at least one of the architectural axes the patterns commit to.

## 9. Conclusion

Treating birth as a single undifferentiated primitive blurs the level-distinct scope that B2.07 commits to and leaves deployments without a principled vocabulary for the three different operational moves they actually perform when creating cells, aspects, and Selves. Naming the three patterns as level-specialized operational variants of birth restores the level-distinct scope at the moment of instantiation, commits the specifications to substrate-residence under A2.04 governance, and makes recursive Paper 1 inheritance per B1.20 operational at the right point — the entity-creation event itself, not later.

This note closes the four-note B1.02 decomposition. B2.07 commits each level to having distinct scope; B2.08 commits level membership to substrate-resident records; B2.09 commits operational distinguishability through type declarations; B2.10 commits the level-specific instantiation patterns that produce entities of distinct architectural character at the time of creation. Together the four notes specify, for each of the three levels, what scope it carries, who its members are, how it is distinguished from the other levels, and how new entities at that level are brought into being. After B2.10, Phase B2 proceeds to decompose B1.03 (the cell level itself) starting at B2.11.

Subsequent work that implements, extends, or argues against the CKS instantiation commitments should use "level-instantiation patterns" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Level-Instantiation Patterns: Operational Specialization of Birth at Cell, Aspect, and Self Scope in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
