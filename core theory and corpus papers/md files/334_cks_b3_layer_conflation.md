# Layer Conflation: The Anti-Pattern That Arises When the DNA Layer and Action Layer per B1.06 Are Not Maintained as Distinct Layers

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

The Coordination Knowledge Substrate (CKS) pattern, as extended in Paper 2, commits every cell to maintaining two distinct substrate layers: the DNA layer, which carries stabilized orchestration specifications and defines what the cell is governed to do, and the Action layer, which carries recorded task instances and their outputs as the cell's accumulated operational history. These two layers serve different governance purposes, evolve through different mechanisms, and must be kept architecturally separate for the cell's evolution machinery to function correctly. This note formalizes Layer Conflation — the anti-pattern that arises when this separation is not maintained. Layer Conflation appears in three recognizable forms: DNA-as-log, in which operational records are written into the DNA layer; Action-as-spec, in which governance specifications are written into the Action layer; and single-layer design, in which no two-layer distinction is maintained at all. Each form disables one or more of the evolution mechanisms that the two-layer architecture supports. The note identifies the emergence conditions that make conflation predictable, traces the operational consequences through the evolution and accountability commitments, specifies detection tests, and provides a remediation path.

---

## 1. The Commitment Violated: B1.06

B1.06 establishes two distinct layers within every cell.

The DNA layer carries stabilized orchestration content — harness logic, conflict-handling rules, lifecycle policies, schemas — that defines how the cell is governed to behave. DNA is the cell's specification, the substrate that human governance acts on directly and that the directed selection mechanism (B1.14) refactors when the cell's governing logic needs to change. DNA is authoritative by definition: it is what the cell is, in the sense that governs all its operations.

The Action layer carries recorded task instances and their outputs — what actually happened when the DNA's governing logic met actual tasks. Action is operational history, not specification. It accumulates as the cell's lived experience. It is what the action-feedback evolution mechanism (B1.15) draws on when proposing substrate refinements back toward DNA. Action is evidential by nature: it is the record of what the cell did.

Both layers are substrate content under Paper 1's commitments. Both are human-governed, human-inspectable, and human-modifiable. What distinguishes them is governance semantics: DNA is authoritative specification, Action is operational history. The authority runs one way — DNA constrains and shapes what Action can produce; Action does not autonomously rewrite DNA. The loop that closes Action evidence back into DNA refinement is governed and human-mediated.

B2.25 specifies the DNA layer as the recipient of stabilized orchestration substrates. B2.26 specifies the Action layer as the repository of recorded operational instances. B2.27 establishes the separation mechanisms that maintain these two layers as architecturally distinct. B2.28 specifies the layer-level governance affordances that each layer requires. B2.29 provides the two-layer verification test that confirms both layers are present and hold only their appropriate content.

Layer Conflation violates B1.06 by collapsing this distinction — either partially, by contaminating one layer with the other's content type, or completely, by eliminating the distinction altogether.

---

## 2. Recognizable Forms

Layer Conflation presents in three distinct forms. All three violate B1.06, but they do so in structurally different ways and produce different operational failures.

### Form 1: DNA-as-Log

In DNA-as-log conflation, operational records of task executions are written into the DNA layer rather than the Action layer. The DNA layer accumulates task instance records — specific dates on which tasks were executed, specific inputs processed, specific outputs produced, specific edge cases encountered — mixed in with the orchestration rules that are supposed to be its sole content.

The recognition signals are characteristic. Inspection of the DNA layer per B2.25 reveals records of specific past operations alongside governing rules: a conflict-handling rule followed by a log of the three conflicts handled last week, a schema definition followed by entries recording the specific documents parsed under that schema in a given month. The content of the DNA layer is heterogeneous in a way that the specification does not permit. Some elements are governing — they define what the cell does. Other elements are historical — they describe what the cell did. Both live in the same layer.

This mixing produces a governance sorting problem at every moment that DNA must be acted on. A6.02 retroactivity — the commitment that allows a historical query to identify which version of governing rules was in effect for a given past operation — becomes confused, because what counts as a governing rule and what counts as an operational record is not structurally distinguishable. Directed selection per B1.14 must carefully sort rule elements from log elements before it can act on the DNA layer, adding a pre-governance step that the architecture is not designed to require. The B2.27 DNA-Action separation mechanisms are absent in this form; what should be an architectural boundary is a content-mixing zone instead.

### Form 2: Action-as-Spec

In Action-as-spec conflation, orchestration rules or governance specifications are written into the Action layer rather than the DNA layer. Action records — which are supposed to contain only records of what happened — also contain rules governing what should happen, behavior specifications, or schema definitions.

The recognition signals here are the inverse of Form 1. Inspection of the Action layer per B2.26 reveals governance content — rules that define how conflicts should be handled, definitions of what a valid input looks like, instructions for how outputs should be formatted — mixed in with the operational records that are its proper content. A6.02 Category 4 authoritative content, which belongs in the substrate's governing layer, is dispersed across Action records. A1.08, the commitment that the substrate is the source of truth, is violated in a specific way: the Action layer's operational records are being treated as authoritative governing content, when their purpose is to serve as operational history.

The practical consequence is that the DNA layer per B2.25 is incomplete as a statement of what the cell is governed to do. Queries against the DNA layer will miss governance content that has migrated into Action records. Any human seeking to understand the cell's governing logic must inspect both layers and synthesize the result — defeating the architectural clarity the separation provides. The source-of-truth property per A1.08 is violated not because governance content is absent, but because it is in the wrong layer.

### Form 3: Single-Layer Design

Single-layer design is the most complete form of Layer Conflation. No two-layer distinction is maintained. The deployment has one undifferentiated substrate layer that holds both orchestration specifications and operational records without distinction. There is no separate DNA layer, no separate Action layer; there is only a substrate that accumulates whatever is added to it.

The B2.25 DNA layer specification is absent as a distinct structure. The B2.26 Action layer specification is absent. The B2.27 separation mechanisms have no layers to separate. B2.29 two-layer verification fails completely — not because one layer is contaminated but because neither layer exists as a distinct architectural object.

Single-layer design often arises as the initial architecture for a new deployment, before the need for layer separation has been recognized. It may also arise from a deliberate simplification decision — if one layer works well enough for an early deployment, why add the overhead of a second? The answer is that the single layer works well enough only until the evolution mechanisms need to engage, at which point the absence of layer separation becomes a structural obstacle rather than a simplification.

---

## 3. Emergence Conditions

Layer Conflation is predictable. Three conditions recur across implementations that produce it.

**Implementation convenience.** Maintaining two architecturally distinct layers requires design discipline. At the moment of initial deployment, there is often no immediate operational difference between a properly separated two-layer design and a single-layer design: both can process tasks, both can record outputs, both can be queried. The costs of conflation are deferred to the evolution phase, when the separate mechanisms that operate on DNA and Action respectively need to engage. An architect who has not reasoned through the evolution machinery in advance will tend toward the simpler design — one layer, not two — because the immediate costs of separation are visible and the deferred costs of conflation are not.

**Logging into governing rules.** A specific path to DNA-as-log conflation runs through the practice of keeping everything in one place. An architect maintaining a rules document for a cell adds operational notes directly to that document — a log of which rules were invoked for recent edge cases, a record of which inputs required special handling, a history of which conflicts were resolved and how. Each addition seems low-cost and locally useful. Over time, the DNA layer has become a hybrid document that mixes specification with chronicle. No single addition caused the conflation; the accumulation did.

**Rule discovery from operations.** A specific path to Action-as-spec conflation runs through the practice of deriving rules from observed operations. An architect who observes that tasks with a certain property consistently require a certain handling approach writes that observation into the Action record, tagging it as a provisional governance rule until it can be formalized. The intent is to eventually migrate the rule into DNA, but the migration is deferred, then forgotten, then superseded by further operational observations written into Action. The Action layer accumulates governance content not through a single design decision but through a deferred-migration pattern that never completes.

---

## 4. Operational Consequences

The operational consequences of Layer Conflation are not immediately visible at the task-execution level. A conflated cell can execute tasks and produce outputs. The consequences emerge when the evolution mechanisms engage.

**Action-feedback evolution blocked.** The action-feedback evolution mechanism per B1.15 operates by reading the Action layer as a body of evidence — a clean record of what the cell has done — and proposing substrate refinements based on patterns in that evidence. When the Action layer contains governance specifications mixed with operational records, the evidence-reading step becomes compromised. Proposing substrates per B2.74 requires distinguishing patterns in what the cell has done (evidence) from existing governance rules (specification). In a conflated Action layer, this distinction is not structurally enforced; it must be performed as a pre-processing step, and it is error-prone. The action-feedback mechanism cannot cleanly close the loop between operational evidence and DNA refinement when the evidence pool contains governance content that the loop is supposed to be acting on.

**Directed selection confusion.** The directed selection mechanism per B1.14 operates on the DNA layer as a body of governing specifications — modifying, extending, or restructuring the rules that define what the cell is governed to do. When the DNA layer contains operational records mixed with governing rules, directed selection faces a pre-governance sorting problem: it must first distinguish what to modify (rules) from what to preserve (historical records) before it can act. This is not a governance decision; it is an architectural sorting task that the two-layer design is supposed to have already resolved. In a conflated DNA layer, directed selection inherits this sorting burden, and any error in sorting — treating a log entry as a rule to be modified, or treating a rule as a historical record to be preserved — corrupts the cell's governing logic.

**Retraceability degradation.** A6.02 retroactivity depends on the ability to identify, for any past operation, which version of the cell's governing rules was in effect at the time. This depends on the DNA layer containing only governing rules, so that DNA version history is a clean record of rule changes. When DNA contains operational records, DNA version history becomes a record of both rule changes and log additions — and distinguishing rule changes from log additions in historical DNA versions requires the same sorting problem that current-state governance requires. A5.08 provenance-completeness fails: the substrate cannot provide a complete and unambiguous provenance record for past operations because the governing rule state at any past moment is not cleanly recoverable from the DNA version at that moment.

**Determinism violation.** A1.10, the determinism contract, requires that the same inputs processed under the same governing rules produce the same outputs — and that the authoritative source of those governing rules is identifiable and stable. In Action-as-spec conflation, the authoritative governing rules are distributed across two layers: the DNA layer holds part of the governance specification, and the Action layer holds another part. The source-of-truth property per A1.08 is ambiguous: querying DNA alone does not yield the cell's complete governance specification. Depending on what has migrated into Action, the cell's behavior may be governed by rules that no single layer inspection can fully recover. This produces a functional determinism violation — not because the cell behaves non-deterministically in execution, but because the governance specification that is supposed to determine its behavior is not locatable in one authoritative substrate.

---

## 5. Detection

Layer Conflation is detectable through direct inspection of layer content and structure.

**B2.27 DNA-Action separation mechanisms.** The primary structural test: are the DNA and Action layers architecturally distinct? Does the deployment maintain each as a separate substrate structure with its own identity, version history, and access semantics? If the answer is no — if there is one undifferentiated substrate, or if the two "layers" are organizational conventions within one substrate rather than architecturally distinct structures — then the B2.27 separation mechanisms are absent and Layer Conflation in its Form 3 (single-layer design) is confirmed.

**B2.29 two-layer verification.** The primary content test: does each layer contain only its appropriate content type? Inspection of the DNA layer should reveal governing specifications — orchestration rules, conflict-handling logic, schemas, lifecycle policies — and nothing else. Inspection of the Action layer should reveal operational records — task execution instances, inputs, outputs, timestamps, resolution records — and nothing else. If DNA inspection reveals operational records (dates of past executions, specific inputs processed, task outcomes), DNA-as-log conflation is confirmed. If Action inspection reveals governance specifications (rules for handling certain input types, schema definitions, behavior constraints), Action-as-spec conflation is confirmed.

**A5.10 source-of-truth test.** As a cross-series detection check: is the DNA layer the authoritative repository of Category 4 governing content, and is the Action layer the repository of Category 5 operational records? If the answer to either half is no — if governance content is distributed across both layers, or if operational records have accumulated in the DNA layer — the A5.10 source-of-truth test fails and Layer Conflation is confirmed.

**Content type audit.** A practical instantiation of the above tests: for each item in the DNA layer, determine whether it governs what the cell does or records what the cell has done. Governing items belong in DNA; historical items belong in Action. For each item in the Action layer, apply the same test in reverse. Items that govern belong in DNA; items that record belong in Action. Any item found in the wrong layer confirms conflation in the corresponding form.

---

## 6. Remediation

Remediation for Layer Conflation proceeds through layer establishment, content migration, and verification.

**Establish clean DNA per B2.25.** Through directed selection per B1.14, define the DNA layer as containing only stabilized orchestration specifications: the governing rules, conflict-handling logic, lifecycle policies, and schemas that define what the cell is governed to do. This is a human governance act — it requires humans to decide, for each item currently in the substrate, whether it is a governing specification or an operational record. Items identified as governing specifications constitute the initial clean DNA layer content.

**Establish clean Action per B2.26.** Define the Action layer as containing only operational records: task execution instances, inputs processed, outputs produced, conflicts encountered and resolved, timestamps. Items identified as operational records from the content type audit constitute the initial clean Action layer content.

**Migrate operational records from DNA to Action.** Any operational record found in the DNA layer during the content audit is migrated to the Action layer under its appropriate provenance — preserving the timestamp and context of the original record, but relocating it to the layer where operational history belongs. This migration must preserve the integrity of the Action layer's temporal record; migrated items should be inserted at their original chronological position, not appended as new entries.

**Migrate governance specifications from Action to DNA.** Any governance specification found in the Action layer is migrated to the DNA layer under directed selection governance. This migration is not a simple copy; it is a formal governance act, because governance specifications must be authored, versioned, and governed as DNA-layer content. If a governance specification found in Action is provisional or unverified, it requires review before DNA migration — directed selection is the appropriate mechanism for this review.

**Run B2.29 two-layer verification.** After migration is complete, the two-layer verification test is run to confirm that DNA contains only governing specifications and Action contains only operational records. Any remaining conflation found in this verification round is addressed through additional migration. B2.29 verification should be run again after each migration batch until both layers are clean.

The remediation does not require rebuilding the cell's operational history or re-executing past tasks. It requires only that the substrate content already present be correctly allocated across two layers. The cell's operational continuity is preserved; what changes is the architectural organization of the substrate content it carries.

---

## 7. Summary

Layer Conflation is the failure to maintain the DNA and Action layers as architecturally distinct structures within every cell, in violation of B1.06. It appears as DNA-as-log (operational records in DNA), Action-as-spec (governance rules in Action), or single-layer design (no layer distinction at all). It is predictable from implementation convenience pressures, logging practices that consolidate records and rules, and deferred rule-migration habits. Its consequences are not visible at task execution time but emerge when evolution engages: action-feedback evolution cannot cleanly read contaminated Action evidence, directed selection cannot cleanly act on contaminated DNA, retraceability degrades when DNA version history is a mix of rule changes and log additions, and the determinism contract is violated when the authoritative governance specification is not locatable in one layer. Detection runs through the B2.27 structural separation test, the B2.29 content type verification, and the A5.10 source-of-truth cross-check. Remediation establishes clean layers through directed selection and content migration, completed by a confirming B2.29 verification pass.

The two-layer architecture is not bureaucratic overhead. It is the structural precondition for the evolution mechanisms to operate correctly. Without it, the cell can execute but cannot evolve in a governed way.

---

*Derivation note B3.07 in the CKS defensive publication series. This note formalizes prior art from the source papers named in the Attribution section. No new axioms are introduced.*
