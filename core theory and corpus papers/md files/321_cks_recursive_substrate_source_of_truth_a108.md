# Recursive Substrate-as-Source-of-Truth (A1.08): Level-Specific Substrate Authority Across Cell, Aspect, and Self Scope

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Paper 2 specifies through its recursive Paper 1 commitments (B1.20) that the substrate-as-source-of-truth commitment (A1.08) from Paper 1 applies recursively at all three architectural levels introduced in Paper 2: cell, aspect, and Self. This note formalizes recursive A1.08 as the per-commitment specification of level-specific substrate authority. At cell scope, cell substrate — comprising cell DNA per B2.25 and the cell action layer per B2.26 — is the authoritative source of truth for cell behavior. At aspect scope, aspect substrate — comprising aspect coordination DNA per B2.16, aspect membership records per B2.08, and aspect purpose specification per B2.15 — is the authoritative source of truth for aspect coordination. At Self scope, Self substrate — comprising Self integration architecture per B2.21, instinct/reasoning configuration per B2.23, and the Self's aspect collection — is the authoritative source of truth for Self integration. The constant across all three levels is the authority principle: substrate content governs behavior at that scope; runtime behavior inconsistent with substrate is substrate-governed, not runtime-governed. What differs across levels is what constitutes substrate content. Together, cell, aspect, and Self substrates form a coherent substrate hierarchy — from finest-grained cell authority to broadest Self authority — that enables deployment-wide audit and governance correction at every level.

---

## 1. Why recursive substrate-as-source-of-truth needs standalone formalization

Paper 1 established A1.08 — the substrate is the source of truth — as one of its six foundational architectural commitments. A1.08 specifies that substrate content, not runtime state, not LLM context, and not agent memory, is the authoritative record for what governs behavior in a CKS deployment. The five categories of authoritative state reside in the substrate; what a cell does is governed by what the substrate specifies for that cell.

Paper 2 extends the CKS architecture from cells to three levels: cell, aspect, and Self. With that extension comes a structural question that A1.08 at cell scope alone does not answer: what is the authoritative source of truth at aspect scope, and at Self scope? Paper 2 answers this question through its recursive Paper 1 commitments specification (B1.20): A1.08 applies recursively, meaning each level has its own substrate that is authoritative at that level's scope.

Recursive A1.08 is not a restatement of A1.08. It is an architectural specification for how A1.08 applies at each of three levels, what constitutes substrate content at each level, and how the three level-specific substrates relate to one another as a coherent hierarchy. Without formalizing recursive A1.08 as a standalone derivation, the per-level substrate authority relationships remain implicit in the three-level extension Paper 2 introduces. This note makes them explicit.

This is the seventh of thirteen notes in the B1.20 decomposition series within Phase B2. It follows B2.103 (recursive labor allocation, A1.12) and opens the substrate-related per-commitment sub-series. B2.105 will formalize recursive retraceability (A1.07), continuing the per-commitment treatment of Paper 1's commitments at Paper 2's three architectural levels.

The strategic purpose, consistent with the series, is defensive publication of public prior art. Formalizing recursive A1.08 as a named and dated prior-art claim narrows the territory in which any party could assert novel invention over level-specific substrate authority architectures in multi-level AI systems governed by explicit substrate content.

---

## 2. The recursive application precisely stated

### A1.08 at cell scope

At cell scope, A1.08 holds without modification from Paper 1. Cell substrate comprises two components.

**Cell DNA per B2.25.** The DNA layer contains stabilized orchestration substrates, behavior substrates, harness substrate, schemas, and lifecycle policies. Cell DNA specifies what rules govern this cell: what inputs it accepts, what behaviors it performs, how it handles conflicts, what lifecycle transitions it undergoes. Cell DNA is Category 4 authoritative content per A2.46 — it specifies "what rules apply" for this cell. The DNA layer is what mating combines in the genetic sense, what evolution refactors, and what defines the cell's behavioral potential.

**Cell action layer per B2.26.** The action layer contains recorded task instances and their outputs — what actually happened when this cell's DNA met actual tasks. The action layer is authoritative for what this cell has done: what operations it has executed, what outputs it has produced, what feedback it has generated. The action layer is what accumulates as the cell's lived experience and what feeds back into DNA refinement over time.

Together, cell DNA and action layer constitute the complete cell substrate. A1.08 at cell scope means: what a cell does is governed by what its cell substrate specifies, not by observed runtime behavior. If observed behavior diverges from cell substrate, the substrate governs and the divergence requires correction.

**Cell substrate is authoritative for:** what inputs this cell accepts, what behaviors this cell performs, what outputs this cell produces, and what operations this cell has executed.

### A1.08 at aspect scope

An aspect is a coordination arrangement of cells serving a particular purpose. Aspect substrate comprises three components.

**Aspect coordination DNA per B2.16.** This contains membership rules, invocation rules, output-integration rules, and conflict-handling rules — the full specification of how this aspect coordinates its constituent cells. Aspect coordination DNA is Category 4 authoritative content per A2.46: it specifies "what rules apply" for this aspect's coordination. It is authoritative for how cells are invoked, how cell outputs are combined, and how conflicts across cells are handled within this aspect's purpose.

**Aspect membership records per B2.08.** These records specify which cells participate in this aspect. They are the authoritative record of aspect composition — which cells are members, under what conditions, and with what relational roles.

**Aspect purpose specification per B2.15.** This specifies what this aspect coordinates for — the purpose that defines the structural arrangement of cells as a named mode of engagement. Aspect purpose specification is authoritative for the scope of this aspect's coordination activity.

Together, aspect coordination DNA, membership records, and purpose specification constitute the complete aspect substrate. A1.08 at aspect scope means: how an aspect coordinates is governed by what its aspect substrate specifies, not by observed coordination behavior. Coordination inconsistent with aspect substrate requires governance correction at the aspect level.

**Aspect substrate is authoritative for:** which cells are members, how cells are invoked, how cell outputs combine, and how conflicts within the aspect are handled.

### A1.08 at Self scope

The Self is the integrated whole that holds multiple aspects as facets of one CKS-governed intelligence. Self substrate comprises three components.

**Self integration architecture per B2.21.** This specifies how this Self integrates its aspects — cross-aspect coordination rules, cross-level access configuration, and the integration architecture that makes multiple coexisting aspects a unified whole rather than a collection of independent arrangements.

**Self instinct/reasoning configuration per B2.23.** This specifies how the instinct/reasoning separation operates in this Self — how the LLM (instinct layer) and the CKS substrate (reasoning layer) compose under unified governance, and where the instinct/reasoning boundary is drawn for this Self's particular deployment.

**Self aspect collection.** The complete set of aspects this Self integrates is the authoritative record of Self composition. The aspect collection is authoritative for which aspects are active, which cells participate across aspects, and how cross-aspect relationships are configured.

Together, Self integration architecture, instinct/reasoning configuration, and aspect collection constitute the complete Self substrate. A1.08 at Self scope means: how a Self integrates is governed by what its Self substrate specifies. Observed integration behavior inconsistent with Self substrate requires governance correction at the Self level.

**Self substrate is authoritative for:** which aspects are integrated, how cross-aspect conflicts are handled, how instinct/reasoning separation operates, and what cross-level access is governed.

### What is constant: the authority principle

Across all three levels, one thing is constant: substrate content is authoritative for behavior at that level's scope. Runtime behavior inconsistent with substrate is substrate-governed, not runtime-governed — the substrate defines what should obtain, and divergence requires correction, not redefinition of the substrate based on what is observed.

### What differs: substrate content per level

What differs across levels is what constitutes substrate content. At cell scope: DNA plus action layer. At aspect scope: coordination DNA plus membership records plus purpose specification. At Self scope: integration architecture plus instinct/reasoning configuration plus aspect collection. Each level has its own substrate content, and each level's substrate is independently authoritative at that scope.

### The substrate hierarchy

The three level-specific substrates form a coherent hierarchy. Cell substrate is the finest-grained authority — governing behavior at the level of individual informational tasks. Aspect substrate is the intermediate-grained authority — governing coordination across cells within a purpose-defined arrangement. Self substrate is the broadest authority — governing the integration of multiple aspects into one unified whole. Together they constitute the complete deployment's authoritative content at every level of granularity.

---

## 3. What makes recursive substrate-as-source-of-truth architecturally distinctive

Conventional AI architectures typically rely on implicit authority: a deployed model is authoritative because it is deployed. There is no separate substrate specifying what rules govern the model's behavior; no explicit record of what the model has done that is distinct from the model's weights or context window; no per-level substrate hierarchy whose content can be inspected independently of runtime behavior. What the system does is what the system is; there is no separate authoritative record to diverge from.

Recursive A1.08 introduces a structurally different arrangement. Each architectural level has its own explicit substrate content that is authoritative at that scope. Cell behavior is governed not by what the cell is observed to do but by what cell DNA specifies. Aspect coordination is governed not by what aspects are observed to produce but by what aspect coordination DNA specifies. Self integration is governed not by what the Self is observed to do but by what Self integration architecture specifies.

This structural difference has three architectural consequences that are unavailable in implicit-authority systems. First, entity-level substrate inspection is possible at every level: any cell's substrate can be inspected to understand the rules governing that cell; any aspect's substrate can be inspected to understand how that aspect coordinates; any Self's substrate can be inspected to understand its integration architecture and instinct/reasoning configuration. Second, the substrate hierarchy enables coherent deployment-wide audit: starting from Self substrate, an auditor can traverse to aspect substrates — understanding which aspects exist and how they coordinate — and from there to cell substrates — understanding which cells participate and under what rules. The complete authoritative content chain from Self to cell is substrate-resident and independently readable. Third, governance correction is possible at the appropriate level without system-wide intervention: a cell-level divergence requires correction at cell scope; an aspect-level divergence requires correction at aspect scope; a Self-level divergence requires correction at Self scope. The substrate hierarchy localizes both the authority and the governance responsibility.

---

## 4. The biological analog

The biological parallel is useful as a conceptual scaffold, though the architectural substance is independent of it. In biological systems, DNA is the authoritative substrate for cellular behavior at cell scope: what a cell does is governed by its DNA, not by observed cellular behavior as the primary standard. At higher organizational levels, regulatory and epigenetic mechanisms carry authority that is not reducible to the DNA sequence alone — governing how DNA is expressed and how cells coordinate across tissues and organs in service of the organism's integration.

Recursive A1.08 is the governed architectural analog of this structure. Cell DNA is the authoritative substrate for cell behavior, paralleling genetic authority at cell scope. Aspect coordination DNA is the authoritative substrate for inter-cell coordination within a purpose-defined arrangement, paralleling intermediate-level regulatory authority over tissue-level coordination. Self integration architecture is the authoritative substrate for integrating multiple coexisting arrangements into one whole, paralleling the highest-level integrative authority over the organism's unified functioning.

Where the analog reaches its limit is in governance: biological substrates are not human-governed in the CKS sense. Cell DNA is not subject to human inspect, modify, and override rights in ordinary operation; epigenetic mechanisms are not authored by humans in the CKS sense of orchestration rule authorship. Recursive A1.08 introduces explicit human governance at every substrate level — every level's substrate is governed per A1.01, meaning the three rights (inspect, modify, override) apply to cell DNA, aspect coordination DNA, and Self integration architecture alike. CKS substrate authority is explicit, human-governed, and independently addressable; biological substrate authority is implicit and emergent. The biological analog illuminates the structure; the governance commitment is what makes it architecturally defensible.

---

## 5. Inherited Paper 1 commitments

Three Paper 1 commitments are directly load-bearing for recursive A1.08.

**A1.08 itself.** The substrate is the source of truth at cell scope is the commitment being extended. Recursive A1.08 applies A1.08 at cell, aspect, and Self scope, with cell-scope A1.08 inherited unchanged from Paper 1. The recursive extension does not modify A1.08 at cell scope; it specifies how A1.08 applies at the two additional levels Paper 2 introduces.

**A2.46 — Category 4 authoritative content.** At each level, the DNA component of substrate is Category 4 content: it specifies "what rules apply" at that scope. Cell DNA specifies what rules govern this cell. Aspect coordination DNA specifies what rules govern this aspect's coordination. Self integration architecture specifies what rules govern this Self's integration. A2.46 applies at every level, making each level's DNA the categorical authority over what governs behavior at that scope.

**A2.01 — Inspect right.** The three rights from A1.01 (inspect, modify, override) apply to substrate content at every level. A2.01 specifically grounds the inspect right as a substrate-level architectural requirement. Cell substrate inspection enables understanding of any cell's governing rules. Aspect substrate inspection enables understanding of any aspect's coordination rules. Self substrate inspection enables understanding of Self integration architecture and instinct/reasoning configuration. The inspect right applied recursively is what makes deployment-wide audit from Self to cell architecturally available rather than operationally dependent on runtime accessibility.

**A2.02 — Modify right.** The modify right applies to substrate content at every level. Governance correction at any level is exercisable through the modify right over that level's substrate: correcting cell DNA, updating aspect coordination rules, revising Self integration architecture. The modify right applied recursively is what makes level-specific governance correction possible without cross-level interference.

---

## 6. Operational implications

Four operational implications follow from recursive A1.08.

**Maintain substrate at each level.** Deployments under recursive A1.08 maintain substrate content at cell, aspect, and Self granularity as the authoritative record. Cell DNA is maintained as the cell's governing specification; aspect coordination DNA is maintained as the aspect's governing specification; Self integration architecture is maintained as the Self's governing specification. Each level's substrate is the ground truth for that level, and must be kept accurate through governance rather than allowed to drift from observed behavior.

**Entity-level substrate inspection enables governance.** Because substrate content at every level is independently inspectable per A2.01, governance does not require observing and interpreting runtime behavior. Inspecting cell substrate tells the governing human what rules govern that cell; inspecting aspect substrate tells them how that aspect coordinates; inspecting Self substrate tells them how the Self integrates. Governance can proceed from substrate inspection rather than relying on runtime behavior observation, which may be ambiguous, incomplete, or inaccessible during failure modes.

**Deployment-wide audit from Self to cell.** The substrate hierarchy enables coherent, complete auditing of an entire deployment. Starting from Self substrate, the aspect collection identifies which aspects exist; aspect membership records identify which cells participate in which aspects; cell DNA specifies the rules governing each cell. The complete authoritative content chain is substrate-resident and independently traversable. An auditor starting at Self scope can follow the substrate hierarchy to any cell without needing to observe runtime behavior at any step.

**Governance correction at the appropriate level.** When runtime behavior diverges from substrate specification, correction proceeds at the level where the divergence originates. A cell behaving inconsistently with cell DNA requires cell-level substrate correction or cell DNA modification. An aspect coordinating inconsistently with aspect coordination rules requires aspect-level correction. A Self integrating inconsistently with Self integration architecture requires Self-level correction. The substrate hierarchy localizes governance responsibility and prevents governance actions at one level from inadvertently disrupting substrate authority at another level.

---

## 7. Limits

Recursive A1.08 has precisely bounded scope. Naming the limits is as important as naming the commitment.

**Recursive A1.08 does not mean cross-level substrate governance.** Each level has its own independently authoritative substrate. Self substrate does not override cell substrate; aspect substrate does not override cell DNA. Each level's substrate is authoritative at its scope, not at other scopes. The substrate hierarchy is not a chain of command in which higher-level substrates issue directives that lower-level substrates must execute. It is independent authoritative content at each level, each governing behavior at its own scope.

**The substrate hierarchy is not a strict access hierarchy.** Paper 2 specifies that access patterns across levels are not strictly hierarchical: the Self can access cells directly when purpose requires. Recursive A1.08 is a commitment about where substrate authority resides, not about what can access what. Cell substrate is accessible to aspects and to the Self; the hierarchy is about authority, not access restriction.

**Incorrect substrate content is still authoritative.** A1.08 at each level means substrate content governs, regardless of whether that content is accurate. Incorrect cell DNA is still authoritative for cell behavior; incorrect aspect coordination rules are still authoritative for aspect coordination. This is not a design flaw — it is the architecture's mechanism for forcing governance accountability. Incorrect substrate requires governance correction through the modify right; it does not get silently corrected by observed behavior or runtime inference.

**Substrate content accuracy depends on governance quality.** The guarantee that recursive A1.08 provides is that substrate governs behavior. It does not guarantee that substrate content is itself correct, complete, or well-designed. That depends on the quality of governance exercised through the modify and override rights at each level. Governance quality is a deployment responsibility, not an architectural guarantee.

**Runtime state inconsistent with substrate requires correction, not substrate revision.** When observed runtime behavior diverges from what substrate specifies, the appropriate response is governance correction at the appropriate level — not revision of the substrate to match observed behavior. The substrate-governs principle means the substrate defines the normative state. Divergence is a failure of instantiation; it does not constitute evidence that the substrate is wrong or that runtime behavior has superseded substrate authority.

---

## 8. Operational test

A deployment instantiates recursive substrate-as-source-of-truth (A1.08) if and only if: for each cell in the deployment, cell DNA and action layer constitute the cell's authoritative governing record; for each aspect, aspect coordination DNA, membership records, and purpose specification constitute the aspect's authoritative governing record; for each Self, Self integration architecture, instinct/reasoning configuration, and aspect collection constitute the Self's authoritative governing record; and in each case, substrate content — not observed runtime behavior — is what governs, so that divergence between runtime behavior and substrate specification is treated as a governance failure requiring correction at the appropriate level, not as an update to the substrate reflecting what the system has learned to do.

---

## 9. Why naming recursive A1.08 as standalone matters

A1.08 is a well-established commitment in the CKS series — Paper 1's formalization of substrate-as-source-of-truth at cell scope is already published prior art. The novel territory requiring standalone formalization is the recursive application: the specification that A1.08 applies at each of Paper 2's three levels, with distinct substrate content at each level, as a coherent substrate hierarchy enabling deployment-wide audit.

The substrate hierarchy — cell substrate as finest-grained authority, aspect substrate as intermediate-grained authority, Self substrate as broadest authority — is a specific architectural pattern. The composition of substrate content at each level (cell DNA plus action layer; aspect coordination DNA plus membership plus purpose; Self integration architecture plus instinct/reasoning configuration plus aspect collection), the deployment-wide audit chain from Self to cell, and the level-specific governance correction model are architectural specifics not derivable as obvious consequences of cell-scope A1.08 alone. Naming them publicly under this date, traced to the source paper, constitutes prior art over these specific architectural arrangements in multi-level AI systems.

This is the seventh of thirteen decompositions of B1.20 within Phase B2. B2.104 opens the substrate-related per-commitment series; B2.105 will formalize recursive retraceability (A1.07), extending the per-commitment treatment to provenance and accountability at cell, aspect, and Self scope. The full B1.20 decomposition series — through B2.110 — provides per-commitment prior-art coverage for the complete set of Paper 1 commitments as they apply under Paper 2's recursive three-level extension.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Recursive Substrate-as-Source-of-Truth (A1.08): Level-Specific Substrate Authority Across Cell, Aspect, and Self Scope.* May 12, 2026. ORCID: 0009-0004-8065-3235.
