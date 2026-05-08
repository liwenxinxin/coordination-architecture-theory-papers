# Action Layer Operational Specification: The Substrate-Resident Accumulating Record of Cell Operational History in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a standalone operational variant, the architectural specification of one of the two layers Paper 2 commits to within every cell — the **action layer** — by stating precisely what content the layer carries, how that content accumulates, what governance affordances apply to it, and how it composes with the inherited Paper 1 commitments. It is the second of five notes decomposing Paper 2's two-layer commitment, complementing the companion specification of the DNA layer formalized separately.

## Abstract

Paper 2 commits, within every cell of a CKS Self, to two architecturally distinct layers: a DNA layer of stabilized orchestration and behavior substrates that defines how the cell functions, and an action layer of recorded task instances and their outputs that records what actually happened when the DNA met an actual task. The companion derivation note formalizes the DNA layer. This note formalizes the **action layer** as substrate-resident **accumulating operational history**: the structured, provenance-bearing record of cell task instances, consultation events, processing decisions, substrate-write history, and input/output records that grows as the cell runs. The note states the operational specification precisely, distinguishes the layer from neighbors with which it is commonly conflated (DNA content, internal computation state, audit logging as workflow feature), enumerates the inherited Paper 1 commitments that determine its content, names operational implications and limits, and provides an operational test.

## 1. Why the action layer needs an operational specification

Paper 2 commits to two layers within every cell — DNA and action — and names each by what it carries (DNA: stabilized orchestration and behavior substrates; action: recorded task instances and their outputs). Naming is not the same as specifying. A downstream reader can take Paper 2's "recorded task instances and their outputs" formulation and reasonably ask: which task instances, recorded how, with what metadata, accumulating where, governable by whom, distinct from what? Without an operational specification, the answers slip toward whatever conventions the implementer happens to know — most commonly, ad hoc audit logging at an application layer, or implicit operational history recoverable only by re-running the cell. Both substitute a workflow feature for an architectural commitment.

The companion note formalized the DNA layer as substrate-resident stabilized specification — what the cell does. This note formalizes the action layer as the architectural counterpart — what the cell did, accumulating as it does it. Naming the two as paired specifications, both substrate-resident but architecturally distinct, preserves Paper 2's two-layer commitment as a load-bearing architectural property rather than a descriptive shorthand. The remaining three notes in the decomposition formalize separation operational mechanisms, layer-level governance affordances, and inheritance verification.

## 2. The action layer, specified precisely

Within every cell, the **action layer** is the substrate-resident accumulating record of the cell's operational history, structured for provenance-bearing audit and retraceability. It is what Paper 2 names as "recorded task instances and their outputs," extended through Paper 1's inherited commitments to a precise operational form.

**Content carried by the action layer.** The action layer records, at a minimum, five kinds of content:

- **Recorded task instances.** Each instance captures one cell execution: when the cell ran, what inputs were processed, what processing happened, what outputs were produced. The task instance is the unit of accumulation.
- **Consultation events.** When the cell consulted an instinct-layer counterpart under the cell's routing rules, what was consulted, and what response came back. Consultation events are part of what the cell did, not separate metadata about it.
- **Processing decisions.** Which DNA-layer rules applied for the inputs at hand, what routing pattern was used, and what conflict-handling occurred under the cell's rules. These are the cell's decisions about its own conduct, recorded as fact rather than re-derived after.
- **Substrate-write history.** What the cell wrote to the surrounding substrate during the task instance — the writes the cell made, in the order it made them, with reference to the surrounding state at the time.
- **Input/output records.** The actual inputs and outputs of cell operations, in the form the cell processed and produced them.

**Provenance for each event.** Every event recorded in the action layer carries the six provenance metadata fields the inherited Paper 1 commitment requires: who, what, when, why, under what rule, and what previous state. The provenance is not adjacent to the action layer; it is part of what makes a record an action-layer record at all.

**Substrate-resident location and source-of-truth authority.** The action layer is on the substrate side of the substrate-cell boundary. Action content is substrate content — held in the substrate the way every other piece of substrate content is held, not inside cell processing, in transient runtime memory, or in vendor-specific operational telemetry. As substrate content, the action layer is authoritative within the inherited source-of-truth taxonomy for two categories: "what happened" (the factual record of cell operations) and "what's the history" (the temporally ordered accumulation of those operations over time). An auditor asking either question reads the action layer, not a re-derivation, summary, or system self-report.

**What retraceability operates on.** The inherited Paper 1 commitment to path retraceability at cell scope operates on the action layer. Without the action layer, retraceability would have nothing to operate on; with it, the question "how did this cell come to produce this output" is answered by reading provenance-bearing records of the cell's actual operations.

**Accumulation, not authoring.** The action layer accumulates routinely as the cell processes tasks. Action records grow as a consequence of cell operation, not as the result of deliberate authoring. This is the architectural distinction from the DNA layer, which is authored under governance and changes only when authored to change.

**Recording rules as substrate content; factual, not prescriptive.** What the action layer records — the level of detail, the kinds of events captured, the retention windows — is itself governed by orchestration rules that are substrate-resident authoritative content. The rules that determine what gets recorded are subject to the same governance affordances as any other substrate content. The action layer records what happened; it does not specify what should happen. The prescriptive role belongs to the DNA layer; the descriptive role belongs to the action layer.

## 3. What makes the action-layer specification architecturally distinctive

Conventional AI architectures often have implicit operational history. A cell, agent, pipeline, or component produces outputs; whatever record of "how it ran" exists is held in application-layer logs, vendor-specific telemetry, or runtime traces that the architecture treats as adjacent infrastructure rather than as primary content. The history is recoverable in many cases; it is not architecturally specified to exist, to live in a particular location, or to be governable as substrate content.

The CKS action-layer specification departs from this in three respects.

**Operational history is named.** The action layer is one of two layers Paper 2 commits to within every cell. It is not an implementation byproduct, an adjacent log, or a feature of a particular telemetry vendor. It is part of the architectural specification of what a cell is.

**Operational history has a location.** The action layer is substrate-resident. It lives where every other piece of substrate content lives, accessible through the same governance affordances, governed by the same authority architecture.

**Operational history is governable.** The action layer is subject to the inherited Paper 1 governance commitment. The rights to inspect, modify, and override apply to action-layer content the way they apply to any other substrate content (with a practice-level caveat on modification noted in §7). The recording rules that determine what gets captured are themselves governable substrate content.

These three properties — named, located, governable — are what make the action-layer specification a derivation worth formalizing as standalone. Without them, "the cell records what it does" reads as a description of normal operation; with them, as an architectural commitment with operational consequences.

## 4. Cognitive and biological analogs as conceptual scaffold

The action layer admits two analogs from neighboring domains, each useful as conceptual scaffolding and each limited in ways that make the architectural substance the part that does the actual work.

**Episodic memory (cognitive analog).** Human episodic memory accumulates the record of specific experiences — what happened, when, where, with whom, under what context — and is retrieved as needed for reflection, learning, and decision-making. The action layer parallels this in being an accumulating record of specific operational events with provenance, retrievable for audit, retraceability, and downstream evolution.

**Cellular memory (biological analog).** Biological cells have a loose analog of operational memory through molecular markers, protein states, and epigenetic modifications. The analog is much weaker than the cognitive one because biological cellular memory is not structured in a form that supports retraceable audit; it is a state-bearing mechanism rather than a record-bearing one.

The CKS action layer exceeds both analogs by being a structured, governable, auditable record with explicit provenance for each event. The analogs are conceptual scaffold; the architectural substance is the substrate-resident accumulating operational history with provenance.

## 5. Inherited Paper 1 commitments

The action layer's operational specification is determined as much by what Paper 1 commits to as by what Paper 2 names. The inherited commitments fix the content the layer must hold.

- **The substrate-cell boundary.** Action content sits on the substrate side; it is not cell-internal computation state.
- **Path retraceability.** The action layer is what retraceability operates on at cell scope; the accountability vocabulary (who, what, when, why, under what rule, what previous state) is what action-layer events carry.
- **Substrate as source of truth.** The action layer carries source-of-truth authority for "what happened" and "what's the history" categories.
- **Six-field provenance.** Each action-layer event carries the six metadata fields named above.
- **Rule authoring.** The orchestration rules that determine what the action layer records, at what detail, with what retention, are themselves authored under the human-governed authority architecture.
- **Inspect, modify, override.** The three rights apply to action-layer content as they do to any substrate content, with a practice-level caveat on modification that preserves retraceability (§7).
- **Determinism contract.** The action layer accurately reflects the deterministic state operations of the cell.

The action-layer specification does not introduce new commitments; it specifies how Paper 1's commitments operate on Paper 2's named layer.

## 6. Operational implications

**Recording rules and retention are configured per cell purpose.** Detail level, events captured, and retention are deployment configuration choices governed through the inherited rule-authoring commitment. A regulated decision cell may record at high detail with long retention; a high-volume routine cell may record more selectively with archival retention for older content. The architectural commitment is substrate residency with provenance and governable recording rules; configuration is a deployment decision.

**The layer is testable.** Operational tests on provenance completeness and on the four accountability questions (who, what, when, why) operate on action-layer content. A system whose action layer fails such a test fails the specification itself.

**The layer feeds action-feedback evolution.** Action-feedback evolution proposes DNA-layer changes by examining accumulated action evidence under human-mediated governance: the proposing happens through governable substrates, the proposals require human approval, and the result is DNA changes under directed-selection authority. The action layer is the evidence base for that loop.

**The layer interacts with DNA changes through retroactivity-preservation.** When DNA evolves under governance, prior action records are preserved as historical fact rather than rewritten in light of new rules. Audit reads an old action record against the rules in force when the cell ran, not against the current rules.

**The layer enables operational understanding.** Debugging, performance analysis, behavior pattern detection, and downstream compliance review all operate on action-layer content.

## 7. Limits

The action-layer specification is precise about what the layer is. It is equally important to state what it is not, because each of the following neighbors is a real and reasonable commitment in some other architecture, and conflating any of them with the action-layer specification produces a misreading.

**Not DNA content.** The action layer does not carry stabilized orchestration or behavior substrates; that content is the DNA layer's. The two layers are substrate-resident, but they are architecturally distinct.

**Not specification, not behavior-prescribing.** The action layer records; it does not specify. The question "what should the cell do under these conditions" is answered by DNA content, not by reading historical action records. The presence of a precedent in the action layer does not, by architectural commitment alone, prescribe future cell behavior; whether and how past action informs future behavior is governed through DNA content (potentially evolved through action-feedback).

**Modification is operationally constrained even where architecturally permitted.** The inherited modify right applies to action-layer content, but modifying historical action records would compromise retraceability — the very property the action layer exists to support. In practice, deployments handle "corrections" through the override right with provenance preserving the original record, rather than through direct modification of the historical entry. This is operational practice rather than architectural rule, but it is significant for any deployment whose audit posture depends on the action layer.

**Conflicts in action content are handled the same way as any substrate conflict.** When two action records appear to disagree, the conflict-as-first-class-object commitment from Paper 1 applies. The action layer does not auto-resolve such conflicts; it preserves them.

**Not the pinning target, not the verification baseline.** When a deployment commits to a stable specification a cell must follow, the pinning target is DNA content. Verification mechanisms validate cell behavior against DNA-layer specification, not against accumulated action history. The action layer is what gets verified; it is not what verification verifies against.

**Not cell-internal computation state.** Transient runtime state — variables held during a single inference, intermediate working data within one task instance — is cell-internal processing, not action-layer content. The action layer is the post-task record of what the cell did, not the in-task working memory of how it did it.

## 8. Operational test

A system instantiates the action-layer commitment as Paper 2 specifies it (extended through Paper 1's inherited commitments) if and only if all of the following are true at all times during the cell's existence:

1. The cell records task instances, consultation events, processing decisions, substrate-write history, and input/output records as substrate content addressable as part of the substrate.
2. Each recorded event carries the six-field provenance metadata (who, what, when, why, under what rule, what previous state) as part of the record itself.
3. The action layer is authoritative for "what happened" and "what's the history" questions about the cell's operations; these are answered by reading action-layer content, not by re-derivation, system self-report, or vendor-specific telemetry.
4. Path retraceability for cell operations operates on action-layer content; an auditor can reconstruct what the cell did, when, under which rules, by reading the layer.
5. The recording rules that determine what gets captured at what detail with what retention are substrate-resident orchestration rules authored under the human-governed authority architecture.
6. The action layer accumulates as a consequence of cell operation; growth happens through operation rather than through deliberate authoring.
7. Action-layer content is held in inspectable form and is governable through the inspect, modify, and override rights, with modification practice preserving retraceability per §7.
8. The action layer is architecturally distinct from DNA-layer content: prescriptive specification lives in DNA; descriptive history lives in action.

A system that fails any of (1)–(8) does not implement the action-layer commitment as specified, even if it satisfies the DNA-layer and other CKS commitments in some other respect.

## 9. Conclusion

The action layer is one of two layers Paper 2 commits to within every cell. The companion derivation note formalizes the DNA layer as substrate-resident stabilized specification of cell behavior; this note formalizes the action layer as substrate-resident accumulating operational history. They differ in what they carry (specification versus history), how they accumulate (authored versus operationally accumulating), what they are authoritative for (what should happen versus what happened and what's the history), and how modification practice handles them (DNA changes through governed authoring; action changes through override-with-provenance to preserve retraceability).

This is the second of five notes decomposing Paper 2's two-layer commitment; the remaining notes formalize separation operational mechanisms, layer-level governance affordances, and inheritance verification.

Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "the action layer" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Action Layer Operational Specification: The Substrate-Resident Accumulating Record of Cell Operational History in the Coordination Knowledge Substrate Pattern.* May 8, 2026. ORCID: 0009-0004-8065-3235.
