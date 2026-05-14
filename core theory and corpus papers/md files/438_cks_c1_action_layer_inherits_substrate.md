# Action Layer Inherits Paper 1's Operational Substrate Content

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to establish, in operational form, that Paper 2's named Action layer is the explicit, bounded form of an operational substrate content category Paper 1 already commits to — and that all Paper 1 governance commitments for that content category travel unchanged into the Action layer as Paper 2 defines it.

---

## Abstract

Paper 2 of the CKS theory series names and bounds a distinct layer within every cell: the Action layer, which carries recorded task instances, LLM output records, conflict instances, and evidence of past operational behavior. This note establishes that the Action layer is not a novel object introduced by Paper 2. It is the explicitly named and structurally bounded form of a substrate content category Paper 1 already commits to: operational records held in the substrate as authoritative coordination state, subject to human governance, attributable, retraceable, and persistent across session boundaries. The governance commitments that Paper 1 makes for operational substrate content — source-of-truth authority, human-governed three rights, six-field path retraceability, LLM output attribution, first-class conflict preservation, and persistent structured state — travel unchanged into the Action layer. What is new in Paper 2 is not the governance of the records but three structural contributions: the Action layer is explicitly named and bounded as a layer distinct from the DNA layer; the accumulation property (records append through operation, unlike the DNA layer which changes through directed selection) is explicitly characterized; and the Action layer is designated as the evidence source for the action-feedback evolution mechanism, giving operational records a formal role in Paper 2's evolution architecture. This note is the second of a two-note pair with C1.08; together they close the internal structure inheritance for a Paper 2 cell, establishing that both of the cell's two layers — DNA and Action — inherit their governance from Paper 1 substrate content categories.

---

## 1. The inheritance claim

C1.09 formalizes the following inheritance edge:

**Paper 2's Action layer ⊃ Paper 1's operational substrate content (recorded task instances)**

The claim is that every piece of Action layer content in a Paper 2 deployment is, in substrate-governance terms, an instance of the operational substrate content category Paper 1 already commits to. The governance obligations Paper 1 places on that category — specifically, that operational records are authoritative substrate content held as the source of truth for what happened during cell operation, are human-governed, carry attribution, satisfy path retraceability, and persist across session boundaries — apply to Action layer content without modification. Paper 2 does not create a new governance category when it names the Action layer. It names and structurally bounds an existing one.

---

## 2. What Paper 1 commits to: operational substrate content

Paper 1 establishes the substrate as the source of truth for all authoritative coordination state (§11.3). It names five categories of this authoritative state, of which operational records — the records of task executions, LLM outputs that affect coordination state, and related operational outputs — are one. The source-of-truth commitment applies to operational records specifically: they are not ephemeral. They are governed substrate content.

For operational records, as for all substrate content, Paper 1's governance commitments hold:

**Human-governed three rights.** Humans retain, at all times, the right to inspect any operational record, the right to modify any operational record, and the right to override any operation or LLM-produced output that touches operational records. These rights are architectural properties of the system's design, not procedural promises.

**LLM output attribution (AI-as-mediator Property E).** Every LLM output that affects coordination state — including operational records — is recorded in the substrate with attribution. The record identifies the LLM, the cell execution, and the orchestration rule under which the output was produced.

**Six-field path retraceability.** Operational substrate content must carry six provenance metadata fields: writer attribution, timestamp, antecedent reference, rule reference, rationale (where the orchestration rule requires it), and relationship to contradicting content (where applicable). These six fields make any decision or output in the system reconstructable from substrate content alone.

**Persistent structured state (tool-agnosticism Requirement 1).** Operational records persist across session boundaries. They are not held in agent memory, which is session-scoped; they live in the substrate, which is persistent. The tool-agnosticism commitment is what makes this property architecture-level rather than deployment-level.

**Conflict preservation as first-class objects.** Conflict instances — including those arising during cell operation — are first-class substrate content. They are preserved, not silently resolved, and they carry the same governance obligations as any other substrate content.

Together these commitments describe a category of substrate content that records what happened during cell operation, holds those records as authoritative, keeps them under human governance authority, and keeps them retraceable and persistent. This is the category the Action layer names.

---

## 3. What Paper 2 names: the Action layer

Paper 2 (§5.3) introduces the DNA/action layer distinction within every cell as a formal architectural commitment. The Action layer carries recorded task instances and their outputs — what actually happened when the DNA met an actual task. Both layers are substrate content under Paper 1's commitments. The DNA layer carries stabilized orchestration content; the Action layer carries operational history.

Paper 2 is explicit that both layers are substrate content and that both carry Paper 1's governance commitments. The DNA/action distinction is not a distinction between governed and ungoverned content; it is a distinction between two substrate content categories that differ in their governance semantics and in how they change over time.

The Action layer's relationship to Paper 1's operational substrate content is one of naming and bounding, not of introduction. Paper 2 does not extend governance to a previously ungoverned category. It assigns an explicit name — the Action layer — to the category Paper 1 already governs, and it bounds that category structurally by distinguishing it from the DNA layer within the cell.

---

## 4. What is preserved: governance travels unchanged

The following Paper 1 governance commitments apply to Action layer content without modification or qualification:

**Source-of-truth authority for operational history.** The Action layer is the authoritative record of what the cell has done. Answers to operational questions — what tasks were executed, what LLM outputs were produced, what conflicts arose, what resolutions were recorded — come from the Action layer as substrate content, not from agent memory, not from external logs, not from inference. This is the operational-records instance of Paper 1's §11.3 source-of-truth commitment.

**Human-governed three rights apply to all Action layer records.** Any human with appropriate access can inspect any Action layer record, can modify any Action layer record, and can override any operation that writes to the Action layer. These rights are available at all times, not only at scheduled checkpoints. An Action layer record cannot be made inaccessible to a human exercising the inspect right by an LLM operation, a vendor policy, or a runtime middleware layer.

**Attribution travels with Action layer writes.** Every LLM-produced record in the Action layer carries attribution identifying the LLM, the orchestration rule, and the cell execution under which it was produced. The boundary between LLM-attributed and human-attributed Action layer content is inspectable. This is the operational application of AI-as-mediator Property E to the Action layer.

**Six-field path retraceability applies to Action layer records.** Each Action layer record carries writer attribution, timestamp, antecedent reference, rule reference (for cell-mediated writes), rationale (where the orchestration rule requires it), and relationship to contradicting content (where applicable). These fields make any operational event in the cell's history reconstructable from substrate content alone.

**Action layer records are not ephemeral.** They persist across session boundaries per tool-agnosticism Requirement 1. An Action layer built up during one session is available in subsequent sessions. The accumulation of operational history is a substrate property, not a session property.

**Conflict instances in the Action layer are first-class objects.** Where cell operation produces or surfaces a conflict, the conflict instance is preserved in the Action layer as first-class substrate content. It is not silently resolved or discarded. It carries the same governance obligations as any other Action layer record.

---

## 5. What is new in Paper 2: three structural contributions

Three things are new in Paper 2 that are not present in Paper 1's operational substrate content commitment:

**The Action layer is explicitly named and bounded as a distinct layer.** Paper 1 identifies operational records as a category of authoritative substrate content but does not name them as a unified layer or distinguish them structurally from governance rules (orchestration content) within the substrate. Paper 2 names the Action layer as a distinct layer within every cell and explicitly contrasts it with the DNA layer. This naming and bounding is an architectural clarification, not a new governance commitment. It makes the category explicit and operationally addressable in the two-layer cell structure.

**The accumulation property is explicitly characterized.** Paper 2 specifies that the Action layer grows through operation: records accumulate as the cell executes tasks, and this accumulation is the layer's defining dynamic. The DNA layer, by contrast, changes through directed selection — records are versioned under human governance authority when the cell's orchestration content is intentionally refined. The accumulation vs. modification distinction is new in Paper 2. It characterizes how the two layers behave differently over time without altering the governance commitments that apply to either. Both layers are governed; they grow differently. Accumulation (Action) means operational records append as work occurs; modification (DNA) means orchestration records change when governance-directed refinement takes place. Understanding this distinction is what makes the action-feedback loop architecturally legible.

**The Action layer is designated as the evidence source for the action-feedback evolution mechanism.** Paper 2's action-feedback evolution mechanism explicitly reads the Action layer as its evidence source for generating improvement proposals. The loop from action evidence to DNA refinement is governed and human-mediated: Action layer accumulation produces evidence of what worked, what failed, and what surprised; that evidence feeds proposals for DNA refinement; proposals are authorized under the governance machinery Paper 2 §8 specifies; humans hold authority over the proposal-and-acceptance process. The Action layer's role as evolution evidence source is entirely new in Paper 2. Paper 1 commits to operational records being authoritative substrate content; it does not specify that those records constitute evidence for a governed evolution mechanism that reads them to propose governance-layer changes. That specific architectural role — the Action layer as the input to action-feedback evolution — is Paper 2's contribution. The governance of the records that play this role is inherited from Paper 1.

---

## 6. C1.08 and C1.09 as a completing pair

C1.08 and C1.09 together close the internal structure inheritance for a Paper 2 cell.

C1.08 establishes: **DNA layer ⊃ Paper 1's governed specifications** (orchestration rules + behavior substrates). The DNA layer is the explicitly named and bounded form of the governed-specification category of Paper 1 substrate content — the orchestration rules, conflict-handling logic, schemas, and lifecycle policies that define what the cell is governed to do.

C1.09 establishes: **Action layer ⊃ Paper 1's governed history** (operational records + task instance substrate content). The Action layer is the explicitly named and bounded form of the operational-records category of Paper 1 substrate content — the records of task executions, LLM outputs, conflict instances, and past behavior that accumulate as the cell's lived experience.

Together, these two notes establish that the two-layer internal structure of a Paper 2 cell — DNA and Action — inherits, as a pair, from two distinct Paper 1 substrate content categories. Paper 2 does not introduce novel substrate objects that require independent governance justification. It names and structurally differentiates what Paper 1 already commits to governing. Both of the cell's two layers are grounded in Paper 1's substrate content framework and carry Paper 1's governance commitments intact.

The pair also illustrates the general principle that Paper 2's architectural extensions are extensions rather than additions: they operate within Paper 1's substrate governance framework, adding structure (three-level composition, named layers, lifecycle operations, evolution mechanisms) while preserving the governance properties Paper 1 establishes as foundational.

---

## 7. Relationship to C1.10

C1.10 formalizes the next inheritance edge in the Series C sequence: Paper 2's expression mechanism inherits from Paper 1's substrate selection by orchestration rules. Expression is the mechanism that determines which DNA-layer substrates activate for a given cell goal. Having established in C1.08 and C1.09 that both internal layers inherit their governance from Paper 1 substrate content categories, C1.10 addresses how the activation of DNA-layer content — the governed selection process that determines what the cell does for a given goal — inherits from Paper 1's orchestration rule machinery. C1.09 is a prerequisite for C1.10 in the following sense: the Action layer's identity as governed substrate content (established here) is what distinguishes expression — which operates on DNA-layer content — from action-feedback evolution — which reads Action-layer content. Without the DNA/Action distinction grounded in Paper 1 governance, the expression mechanism would lack its inheritance anchor.

---

## 8. Prior-art significance

C1.09 forecloses three classes of adversarial claim:

**Claim class (a): Paper 2's Action layer introduces novel operational record objects unrelated to Paper 1's substrate.** This claim is foreclosed because C1.09 establishes that Action layer content is operational substrate content under Paper 1's governance commitments. The source-of-truth authority, human-governed three rights, attribution, path retraceability, persistent state, and first-class conflict preservation commitments all apply to Action layer content through direct inheritance. Any assertion that the Action layer is a novel object requiring independent prior art would have to show that operational records in Paper 2 differ in governance structure from Paper 1's operational substrate content — which they do not.

**Claim class (b): Using operational records as evolution evidence (action-feedback) is novel relative to Paper 1's substrate-as-source-of-truth commitment.** This claim is partially foreclosed. The governance of the operational records that feed action-feedback evolution is inherited from Paper 1: the records are authoritative substrate content before they play any evolution role, and their authority does not depend on the evolution mechanism that reads them. A claim that the records themselves are novel objects cannot succeed. What remains legitimately new in Paper 2 is the action-feedback mechanism's designation of these records as its evidence source — but the records that constitute the evidence are Paper 1 substrate content.

**Claim class (c): The accumulation property of operational records is novel relative to Paper 1's persistent state commitment.** This claim is foreclosed because Paper 1's tool-agnosticism Requirement 1 commits to persistent structured state that survives session boundaries — and the accumulation property is the operational expression of that persistence for a category of records that grow through cell operation. Records that persist across sessions and that are appended as the cell executes tasks are, by definition, accumulating. Paper 2 names and characterizes this property explicitly; it does not introduce a new kind of persistence.

---

## 9. Operational test

For any Action layer record in a Paper 2 deployment, an observer can verify the following governance properties independently of the action-feedback mechanism that reads from the layer:

1. The record is readable by a human with appropriate access, without scheduling, approval, or runtime intermediation. (Human-governed inspect right.)
2. The record is modifiable by a human with appropriate access, with the modification taking effect as substrate state. (Human-governed modify right.)
3. No LLM operation, vendor policy, or runtime middleware layer can in principle prevent (1) or (2). (Human-governed override right.)
4. The record carries writer attribution, timestamp, and antecedent reference. (Path retraceability fields a, b, c.)
5. If the record was produced by a cell-mediated write, it carries a rule reference identifying the orchestration rule under which it was written. (Path retraceability field d.)
6. The record persists across session boundaries; it is not held in session-scoped agent memory. (Persistent structured state, tool-agnosticism Requirement 1.)
7. If the record is a conflict instance, it is preserved as first-class substrate content and not silently resolved. (Conflict preservation.)

An observer performing this test verifies Paper 1's operational substrate content governance commitments directly from the Action layer record — without consulting the action-feedback mechanism, without running a cell evolution operation, and without reference to how Paper 2's evolution architecture uses the record. The governance properties hold on the record as substrate content. The action-feedback mechanism reads records that already satisfy these properties; it does not confer the properties on them.

A system in which Action layer records fail any of (1)–(7) may be a system with operational history, but it does not instantiate the CKS Action layer in the Paper 2 sense. The governance commitments are part of the definition of what the Action layer is, not options for which specific deployments may opt in.

---

## 10. Conclusion

Paper 2's Action layer is the explicitly named and structurally bounded form of the operational substrate content category Paper 1 already governs. All governance commitments Paper 1 makes for operational records — source-of-truth authority, human-governed three rights, LLM output attribution, six-field path retraceability, persistent structured state, and first-class conflict preservation — travel unchanged into the Action layer. What is new in Paper 2 is structural: the explicit naming of the layer, the characterization of its accumulation dynamic relative to the DNA layer's directed-selection dynamic, and the designation of the Action layer as the evidence source for the action-feedback evolution mechanism.

C1.08 and C1.09 together close the internal structure inheritance for a Paper 2 cell: the DNA layer inherits from Paper 1's governed specifications; the Action layer inherits from Paper 1's governed history. Both layers of every Paper 2 cell are Paper 1 substrate content under Paper 1 governance. Paper 2 adds structure to that content — naming it, differentiating it, and giving it a role in an evolution architecture — but does not add new governance or introduce new objects outside Paper 1's framework.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235. [Paper 1]

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235. [Paper 2]

## How to cite this note

Li, W. (2026). *Action Layer Inherits Paper 1's Operational Substrate Content.* May 14, 2026. ORCID: 0009-0004-8065-3235.
