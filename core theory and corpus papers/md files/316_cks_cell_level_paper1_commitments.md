# Cell-Level Paper 1 Commitments: Decomposing B1.20 by Formalizing How Each Paper 1 Governance Commitment Applies at Cell Scope

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its contribution is to articulate, in operational form, how each Paper 1 governance commitment applies specifically at cell scope, as the second step in the thirteen-note decomposition of B1.20 (recursive Paper 1 commitments) initiated by B2.98 (recursive commitment integrating frame).

## Abstract

Paper 2 establishes that the three architectural levels of a CKS Self — cell, aspect, Self — are recursive in their architectural commitments: Paper 1's governance commitments hold at every level without modification. B1.20 formalizes this recursive commitment as a foundational architectural property of Paper 2. The present note, B2.99, is the second of thirteen notes decomposing B1.20, and it focuses specifically on the cell level. The note enumerates each Paper 1 commitment and specifies precisely what that commitment means when scoped to a cell's operational territory: A1.01 (humans govern cell behavior through authored cell DNA), A1.04 (the LLM serves as mediator within the cell's instinct layer per B1.01), A1.05 (cell behavior is specified in substrate regardless of which LLM the instinct layer uses), A1.07 (cell operations are retraceable through the cell's Action layer per B2.26), A1.08 (cell DNA and Action layer constitute the authoritative cell substrate), A1.10 (determinism holds given cell DNA specifications and inputs), A1.12 (the LLM performs cell operations as labor while humans govern cell DNA), A1.13 (cells satisfy composition requirements within their aspects), A2.01–A2.04 (governance affordances apply at cell scope), A2.40 (each cell operational event records provenance), and A2.46 (cell DNA is Category 4 authoritative content). The note articulates what makes cell-level governance architecturally distinctive — entity-level audit at cell granularity rather than only at deployment level — draws the biological analog of cell-level regulatory governance, identifies the operational implications, and states the limits. B2.14 (cell-level inheritance verification) is the verification counterpart: B2.99 specifies what commitments apply; B2.14 verifies they are met.

---

## 1. Why cell-level Paper 1 commitments require a standalone formalization

B1.20 establishes that Paper 1's governance commitments hold at every level of a CKS Self — cell, aspect, and Self — without modification. That claim is architecturally load-bearing: it is what allows Paper 2's expanded architecture to remain governed in exactly the sense Paper 1 defends, rather than merely analogously governed or governed at a different layer. But the claim as stated in B1.20 is integrating — it asserts recursive application without specifying, level by level, what that application means in concrete operational terms.

The decomposition of B1.20 (B2.98 through B2.110) provides that specification. B2.98 established the integrating frame: why recursive commitment is architecturally necessary, what it means for a commitment to apply at multiple scopes simultaneously, and how each scope contributes its own distinct commitment content without duplicating or displacing the others. B2.99, the present note, is the second step: the cell-level specification, which is the foundation all subsequent levels build on.

The cell deserves first treatment in this decomposition for two reasons. First, it is the unit Paper 1 originally defended. Every Paper 1 commitment was formulated with a cell in view; cell-level application is not an extrapolation but a direct instantiation. Second, and more architecturally consequential, the cell is where Paper 2's most novel contribution — the instinct/reasoning separation per B1.01 — operates. Cell-level application of A1.04 (AI-as-substrate-mediator) is not simply the Paper 1 commitment restated; it is that commitment as expressed through the instinct/reasoning separation, making each cell a governed LLM-consulting entity in the specific sense Paper 2 establishes.

Standing alone, the cell-level specification is a complete statement of how Paper 1 governs the atomic unit. Without it, the decomposition of B1.20 lacks its foundation; with it, aspect-level (B2.100) and Self-level (B2.101) specifications can reference cell-level commitments as already established ground.

The ninety-ninth position in Phase B2 reflects this note's role as a foundation-layer formalization within the final decomposition cluster: not a boundary case or anti-pattern, but the architectural substrate on which the rest of the B1.20 decomposition rests.

---

## 2. Cell-level application of each Paper 1 commitment

### A1.01 — Human-governed at cell scope

At cell scope, A1.01 means that the cell's behavior is human-governed through authored cell DNA. The cell DNA per B2.25 is the substrate content that specifies how the cell functions: the orchestration rules, the conflict-handling logic, the behavioral constraints, the schemas. Humans govern each cell individually through their authority over that cell's DNA — the right to inspect any cell DNA content, the right to modify it, and the right to override any cell operational output, at any time.

Cell-level governance means humans govern each cell's operational behavior, not just the deployment as a whole. A deployment of fifty cells does not have one governance layer covering all cells collectively; it has governance operating at each cell's own substrate. This is the cell-scope specificity of A1.01: individual cell behavior is individually governed.

### A1.04 — AI-as-substrate-mediator at cell scope

At cell scope, A1.04 means the LLM (instinct layer) serves as mediator within the cell, consulting substrate — the cell's DNA rules — to produce outputs. The LLM does not govern the cell; it executes within it under the governance the cell DNA establishes. The cell's instinct/reasoning separation per B1.01 is the cell-level application of A1.04. The instinct layer (LLM) provides high-dimensional processing capacity; the reasoning layer (cell substrate, including DNA rules) provides the governed coordination content that the instinct layer consults.

This cell-level application of A1.04 is particularly notable within Paper 2 because it unifies two independently established commitments. A1.04 from Paper 1 establishes the mediator role architecturally; B1.01 from Paper 2 establishes the instinct/reasoning separation as the structural form that mediator role takes. At cell scope, these are the same commitment seen from two directions: the LLM-as-mediator is the instinct layer consulting cell DNA, and the instinct/reasoning separation is A1.04 operating at cell-scale through Paper 2's biological vocabulary.

### A1.05 — Tool-agnosticism at cell scope

At cell scope, A1.05 means the cell's behavior is specified in substrate — in cell DNA — regardless of which LLM the cell's instinct layer uses. The cell DNA is the substrate content that carries behavioral specification; the instinct layer is the host that executes under it. Tool-agnosticism at cell scope means that replacing the LLM does not change what the cell is committed to doing, only what capacity is executing that commitment.

The carry-strategy per B2.32 is the operational mechanism for this: cell DNA can be carried across LLM changes at cell scope. The behavioral specification is substrate-resident, not LLM-resident, which is precisely what A1.05 requires. A cell whose behavioral specification depends on LLM-internal capacity rather than cell-DNA-external specification does not satisfy A1.05 at cell scope.

### A1.07 — Retraceability at cell scope

At cell scope, A1.07 means each cell's operations are independently retraceable through the cell's Action layer per B2.26. The Action layer records task instances and their outputs — what actually happened when the cell's DNA met an actual task. It is the operational history of that specific cell. Cell-level retraceability means each cell's operations can be audited independently of every other cell in the deployment.

Lineage per B2.43 — birth through current state — provides the complementary dimension: the cell's provenance through its lifecycle, not just its operational record within a given state. Together, Action layer records and lineage records give the full traceability picture at cell scope. Neither requires consulting deployment-level records to constitute a complete cell-level trace.

### A1.08 — Substrate-as-source-of-truth at cell scope

At cell scope, A1.08 means cell substrate — cell DNA per B2.25 together with the cell's Action layer per B2.26 — is the authoritative source of truth for that cell's behavior and operational history. Cell DNA is authoritative for what governs the cell's behavior (orchestration rules, conflict-handling logic, behavioral constraints). The Action layer is authoritative for what the cell has done (operational records, task outputs, provenance entries).

No LLM inference, no external record, and no deployment-level aggregate is the authoritative source for an individual cell's behavior or history. The cell's own substrate holds that authority. This cell-scope formulation of A1.08 is what makes independent cell-level audit possible: the source of truth is cell-resident.

### A1.10 — Determinism at cell scope

At cell scope, A1.10 means that given cell DNA specifications and a set of inputs, cell behavior is deterministic in the CKS sense: the same inputs processed under the same cell DNA produce the same outputs, in the sense that the cell's governed behavior does not vary across identical configurations. The determinism is over the substrate-mediated component of cell behavior — the coordination and governance content — not over the instinct layer's inference, which is allowed its characteristic non-determinism within the governed behavioral envelope.

The cell-level formulation is important because it makes determinism granular. A deployment's overall behavior is deterministic at cell scope when each cell satisfies this commitment at its own scope. Cell DNA evolution changes the cell's scope of determinism, but that change is itself substrate-visible: the change is a governed event in the cell's history.

### A1.12 — Labor allocation at cell scope

At cell scope, A1.12 means the LLM performs cell operations as labor within the cell's instinct layer, while humans govern the cell DNA that defines those operations. The labor/authority distinction is particularly clear at cell scope: the LLM does the work of executing the cell's tasks; humans hold the authority over what the cell is supposed to do in executing them. There is no ambiguity at this granularity about what is labor and what is authority, because the cell's architecture makes the boundary explicit — instinct layer is the labor carrier, cell DNA is the authority substrate.

This cell-level clarity is one of the reasons the CKS architecture scales: governance cost at cell scope is proportional to the variety of behaviors specified in cell DNA (orchestration rule authoring) and the frequency of human-initiated changes (override exercise), not to the volume of cell operations the instinct layer performs.

### A1.13 — Composition requirements at cell scope

At cell scope, A1.13 means cells satisfy composition requirements within their aspects. Composition validity per A5.14 applies at cell scope: a cell that participates in an aspect must satisfy the composition requirements that participation implies — it cannot, for instance, fail to preserve conflict-handling commitments or drop governance affordances when participating in a higher-level arrangement. Cell composition validity is a per-cell property, not an aggregate property of the aspect.

### A2.01–A2.04 — Governance affordances at cell scope

The four governance affordances apply specifically at cell scope:

**A2.01 (Inspect):** Humans can inspect cell DNA content and the cell's Action layer records at any time, without scheduling, approval, or intermediation. Inspection rights are not deployment-level grants that happen to include cells; they apply as per-cell properties.

**A2.02 (Modify):** Humans can modify cell DNA content — amending orchestration rules, conflict-handling logic, behavioral constraints, schema definitions. Modification rights apply per cell, so a human with appropriate access can modify cell DNA without needing to modify other cells.

**A2.03 (Override):** Humans can override cell operational decisions — any output or behavior a cell produces is subject to human override. Override is not a deployment-level reset; it is available at the granularity of individual cell operations.

**A2.04 (Rule authoring):** Humans author cell DNA rules — the orchestration rules that govern how the cell behaves. LLM-drafted rules subject to human authority before taking effect are admissible at cell scope; rules the LLM commits to cell DNA outside human authority are not.

### A2.40 — Provenance at cell scope

At cell scope, A2.40 means each cell operational event records provenance in the cell's Action layer. Cell Action records include the provenance metadata A2.40 specifies — the who, what, when, and under-what-authority of each cell operation. Provenance at cell scope is per-event and per-cell: each event in a cell's history carries its own provenance, and that provenance is cell-Action-resident.

### A2.46 — Authoritative content at cell scope

At cell scope, A2.46 means cell DNA is Category 4 authoritative content — the substrate content that specifies what rules govern this cell. Cell DNA holds authoritative specification of the cell's behavioral commitments, conflict-handling logic, lifecycle policies, and orchestration rules. Its authoritative status means it is the definitive record of how the cell is governed, not a derived or summary record.

---

## 3. What makes cell-level Paper 1 commitments architecturally distinctive

The distinctive feature of cell-level Paper 1 commitments is not their content — the commitments are the same Paper 1 principles — but their granularity. Conventional AI architectures do not apply governance commitments at the scope of individual model components or execution units. Governance applies at deployment level, system level, or access-control level; individual components operate without their own governance architecture. A deployment of twenty AI components has one governance layer, not twenty.

CKS applies the full Paper 1 governance architecture at each cell. A deployment of twenty cells has twenty cells, each independently satisfying Paper 1 commitments at its own scope. This means entity-level governance and audit are possible at cell granularity. A question about a specific cell's behavior can be answered by examining that cell's substrate — its DNA and Action layer — without pulling in the full deployment. A question about whether a specific cell satisfies A1.07 (retraceability) is answerable cell by cell, not only across the deployment as a whole.

This architecture has three consequences that deployment-level-only governance does not produce:

First, cell-level governance reviews are possible. An operator can review a single cell's DNA and Action layer as a self-contained governance unit. The review does not require understanding the full deployment context unless the question specifically concerns cross-cell relationships.

Second, cell-level compliance demonstrations are possible at cell granularity. A cell can be demonstrated to satisfy each Paper 1 commitment independently — its DNA is human-governed, its LLM executes as mediator, its operations are traceable through its Action layer, and so on — without the demonstration being hostage to the behavior of sibling cells.

Third, cell-level failures are locally bounded. When a cell fails to satisfy a commitment — when its DNA is not properly authored, or its Action records are incomplete — the failure is diagnosable at cell scope. The governance failure does not propagate automatically to the deployment level.

---

## 4. The biological analog: cell-level regulatory governance

The biological analog for cell-level Paper 1 commitments is cell-level regulatory governance in biological systems. Biological cells are not governed only at the organism level; each cell operates under regulatory mechanisms that apply at cell scope. Gene expression regulation determines which genes are active in which cells under which conditions. Membrane transport governance controls what enters and exits each cell. Metabolic regulation governs each cell's energy and biosynthetic activity. These mechanisms operate at cell scope, not only at tissue or organism scope, even though cells also operate within tissues and organisms that impose higher-level constraints.

The analogy is conceptually useful but bounded. Biological cell-level regulation evolved without being designed; CKS cell-level commitments are authored and governed by humans. Biological regulatory mechanisms are encoded in the cell's own biochemistry; CKS cell DNA is human-readable substrate content that humans can inspect, modify, and override at any time. The biological analog illuminates why individual-entity governance is architecturally coherent (cells can be governed individually even within larger wholes) without claiming that CKS replicates biological mechanisms or that biological systems satisfy CKS commitments.

The architectural substance of this note is not the biological analogy but the commitment enumeration in §2. The analogy is scaffolding for understanding the design move; the commitments are the defensible architectural specification.

---

## 5. Inherited Paper 1 commitments: all at cell scope

All Paper 1 commitments apply at cell scope. The note above does not introduce new commitments; it specifies what application at cell scope means for the commitments Paper 1 defends. The specification is complete: every commitment Paper 1 establishes is addressed by its cell-scope counterpart in §2.

The cell-scope specification and the verification of that specification are separate contributions. B2.99 specifies what commitments apply and what cell-scope application means for each. B2.14 (cell-level inheritance verification) is the verification counterpart: it establishes the framework for verifying that a given cell actually satisfies the Paper 1 commitments B2.99 specifies. These two notes are complementary, not redundant. B2.14 cannot do its verification work without the specification B2.99 provides; B2.99's specification is most useful when B2.14's verification tests can be applied to confirm it.

The boundary between specification (B2.99) and verification (B2.14) is itself architecturally important: it separates what the architecture commits to from whether a particular instantiation meets that commitment. Both sides of that boundary are defensible as independently publishable prior art.

---

## 6. Operational implications

**Cell DNA authoring as primary mechanism.** The primary governance mechanism at cell scope is A2.04 — humans authoring cell DNA rules. This is where governance is exercised most consequentially: rule authoring sets the behavioral envelope within which the cell's instinct layer operates. Every subsequent cell operation occurs within the behavioral space cell DNA defines. Governance of the behavioral envelope is governance of the cell.

**Action layer as retraceability substrate.** The cell's Action layer per B2.26 is the operational substrate through which A1.07 retraceability is achieved at cell scope. Each cell's Action records must be maintained as the authoritative cell-level operational history. Deployments that fail to maintain cell Action layer records do not satisfy A1.07 at cell scope, regardless of what deployment-level logging exists.

**Cell-level governance reviews.** Because each cell carries its own DNA and Action layer, governance reviews can be organized at cell granularity. A review of cell C's governance consists of examining cell C's DNA (is it properly authored? are the rules consistent with A1.01, A1.04, A1.10, A1.13, A2.04, A2.46?) and cell C's Action layer (are records present? do they carry provenance per A2.40? are operations traceable per A1.07?). The review is scoped to one cell.

**Cell-level compliance demonstrations.** A cell can be demonstrated compliant with Paper 1 commitments at its own scope. Demonstrating cell-level compliance does not require demonstrating deployment-level compliance; it requires only that the cell's own substrate satisfies each commitment at its own scope.

**Independent cell audit.** Because cell substrate is cell-resident and self-sufficient as a source of truth per A1.08, cell-level audit is independent. An auditor with access to a cell's DNA and Action layer has everything needed to assess that cell's governance compliance at cell scope.

---

## 7. Limits

**Cell-level commitments are not deployment-level commitments.** A cell satisfying Paper 1 commitments at cell scope does not constitute deployment-level satisfaction. Deployment-level commitments are at a different scope and are not reducible to the aggregate of cell-level commitments. The relationship between cell-level and deployment-level governance is additive: both apply; neither replaces the other.

**Cell-level governance does not replace deployment-level governance.** Governing each cell individually is not sufficient for deployment-level governance. Questions about cross-cell coordination, aspect-level behavioral coherence, and Self-level integration require governance at those levels. Cell-level governance contributes to but does not complete the governance architecture.

**Cell-level commitment application is principle-preserving.** Each Paper 1 commitment applied at cell scope preserves the principle of the original commitment. A1.01 at cell scope is still about human authority over behavior, not human labor. A1.07 at cell scope is still about operational traceability, not approval workflows. The cell-scope specification elaborates the scope; it does not modify the commitment's content or intent.

**B2.14 is the verification counterpart, not a replacement.** This note specifies what commitment applies at cell scope. B2.14 provides the framework for verifying whether it is met. Neither replaces the other, and a deployment cannot substitute specification for verification or verification for specification.

---

## 8. Operational test

A cell satisfies cell-level Paper 1 commitments if and only if all of the following hold:

1. A human with appropriate access can inspect any content in the cell's DNA and any record in the cell's Action layer, without scheduling, approval, or runtime intermediation.
2. A human with appropriate access can modify cell DNA content, with the change taking effect as cell substrate state.
3. A human with appropriate access can override any cell operational output.
4. Cell DNA rules are authored by humans; LLM-drafted rules subject to human authority before taking effect are admissible; LLM-committed rules outside human authority are not.
5. The cell's instinct layer (LLM) consults cell DNA to produce outputs and does not hold authoritative behavioral specification in LLM-internal state.
6. Cell behavioral specification is cell-DNA-resident and is carried intact across LLM changes at cell scope.
7. The cell's Action layer records operational events with provenance metadata sufficient for independent cell-level audit.
8. Given identical cell DNA specifications and identical inputs, the cell's governed behavior is equivalent.
9. The LLM performs cell operations as labor; humans govern cell DNA as the authority substrate.
10. The cell satisfies composition requirements within its aspects.

A cell that fails any of (1)–(10) does not satisfy cell-level Paper 1 commitments in the CKS sense, regardless of whether deployment-level governance is otherwise satisfied.

---

## 9. Conclusion

Cell-level Paper 1 commitments are the complete specification of how Paper 1 governs the atomic unit of a CKS Self. The specification is not a reduced or adapted version of Paper 1; it is Paper 1's full governance architecture applied at the scope of a single cell's operational territory. What makes cell-level application architecturally distinctive is the granularity: entity-level governance and audit are possible at cell scope, enabling per-cell governance reviews, per-cell compliance demonstrations, and per-cell failure localization that deployment-level-only governance cannot provide.

B2.99 is the second of thirteen notes decomposing B1.20. The decomposition proceeds in sequence: B2.100 will specify aspect-level Paper 1 commitments, B2.101 Self-level commitments, B2.102–B2.108 per-commitment recursive formalizations, B2.109 recursive operational tests, and B2.110 recursive commitments verification, which closes Phase B2. The cell-level specification established here is the foundation that aspect-level and Self-level specifications reference as already-formalized ground.

The prior-art posture is complete at cell scope. Any claim that a novel architecture applies governance commitments at the scope of individual AI operational entities rather than only at deployment scope now bumps into the cell-level specification this note and its predecessor notes provide.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cell-Level Paper 1 Commitments: Decomposing B1.20 by Formalizing How Each Paper 1 Governance Commitment Applies at Cell Scope.* May 12, 2026. ORCID: 0009-0004-8065-3235.
