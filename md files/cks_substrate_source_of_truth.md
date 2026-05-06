# The Substrate Is the Source of Truth: Where State Lives in CKS Systems and Where It Cannot

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 26 April 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the source-of-truth commitment the CKS pattern makes about substrate state — what the substrate is authoritative for, what it is not, and which categories of state must therefore live inside the substrate versus may legitimately live elsewhere.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern commits to a specific source-of-truth claim about its substrate, stated canonically in §11.3 of the source paper: the substrate is the authoritative answer to coordination questions — what was decided, by whom, under what authority, with what rationale, and where contradictions remain unresolved. The commitment is more specific than database-style "single source of truth," and it is what distinguishes a CKS substrate from a generic data store. It is also load-bearing: several other CKS commitments — path retraceability, determinism on the substrate side of the governance boundary, AI-as-substrate-mediator, conflict preservation, and linear-cost scaling — depend on it and lose operational meaning without it. This note states the commitment in precise form, names the five categories of coordination state for which the substrate is authoritative, names the categories of state that may legitimately live outside, identifies the failure modes that violate the commitment, and provides an operational test for whether a system implements it.

## 1. Why the source-of-truth commitment needs to be stated as its own architectural property

The CKS pattern locates coordination knowledge in a persistent substrate outside the LLM (§2.1) and treats that substrate as the artifact downstream cells read from and write into (§3.1). The source paper develops a specific source-of-truth commitment about that substrate in §11.3, with deliberate scope: the substrate is the source of truth for what was decided, by whom, under what authority, with what rationale, and where contradictions remain. This is not a generic claim that all state in the operating environment lives in the substrate; it is a precise claim about which state the system treats as authoritative for *coordination questions*.

Naming the commitment as its own architectural property earns its keep on two grounds. First, it distinguishes a CKS substrate from any persistent structured store the cells happen to write into: the substrate is a CKS substrate when the system commits to reading from it, and only from it, when answering coordination questions, and treats every other location where coordination state may incidentally appear as non-authoritative. Second, several adjacent CKS commitments are operationally meaningful only if this one holds. Path retraceability (§3.1) traces coordination state through the substrate to its rationale and provenance; the trace is meaningless if the substrate is not where the answer sits. The deterministic, auditable characterization of the substrate side of the governance boundary (§4.1) presupposes that what is deterministic is what the system reads from. AI-as-substrate-mediator (§4.1, §4.2) presupposes that what the LLM mediates over is treated as authoritative. The commitment is the architectural anchor several others hang from.

## 2. The commitment, stated precisely

In the CKS pattern, the substrate is the source of truth for the following categories of state:

(a) **What was decided.** Any decision the system has made or recorded about the coordination work — scope, scheduling, ownership, constraints, accepted definitions, outcomes — is answerable from substrate content.

(b) **By whom.** The writer attribution for any piece of substrate content is itself substrate content; the substrate answers "who decided this" without external reference to logs, session histories, or vendor metadata.

(c) **Under what authority.** The orchestration rule under which a decision was made — or the human override that produced it — is answerable from substrate content. Rule references travel with the content they govern.

(d) **With what rationale.** Where rationale is captured (per the accountability plan §3.1 imports from Naja et al.), it lives in the substrate as addressable content rather than in the conversational trail that produced it.

(e) **What contradictions are unresolved.** Active contradictions — between definitions, between specifications, between competing positions — are answerable from the substrate as first-class content, per the conflict-preservation commitment (§2.1, §5).

The commitment scopes specifically to coordination state. The substrate is *not* the source of truth for unstructured source documents the cells read as inputs, for LLM model weights or parametric knowledge, for environmental state external to the coordination work, or for facts about the world the substrate references but does not own. Section 4 elaborates the scope; what matters here is that the commitment is narrow and precise.

## 3. What "source of truth" means architecturally — and what it does NOT mean

**What it means.** When the system needs to answer a coordination question — what is the current state of this work, who decided what, what conflicts exist, under what rules — the answer is read from the substrate. Reading from any other location to answer such a question is an architectural error, even if the other location happens to agree at the moment of reading. The commitment is about *where the answer comes from*, not whether the answer would also be obtainable elsewhere by chance.

**What it does NOT mean.** The substrate is not required to be the only place coordination state ever appears. Cells may hold cell-internal state during execution; the LLM may hold context within a single cell invocation; external systems may hold derived views of substrate content. What the commitment requires is that none is treated as authoritative when a coordination question is asked. If any disagrees with the substrate, the substrate wins by definition; the disagreement is not a question the system adjudicates, it is non-authoritative state to be discarded or reconciled back to substrate content.

**The database-style "single source of truth" comparison.** The phrase "single source of truth" is also used in database design, and the CKS commitment is not the same claim. The database concept typically describes a normalization decision: one canonical record per entity, no duplicated state, derived data computed from the canonical record. The CKS commitment is different and more specific. It is not a claim about deduplication; it is a claim about which state the system treats as authoritative for a specific class of question — coordination questions — regardless of whether other state exists. A CKS substrate may coexist with derived views, caches, search indexes, and materialized projections without violating the commitment, provided those projections are derived from the substrate and treated as non-authoritative. A database can be normalized and still not be a CKS substrate; a CKS substrate can have substantial derived state around it and still satisfy the commitment.

## 4. Scope: state that must live in the substrate vs. state that may legitimately live outside

Stating both halves prevents two common misreadings: that the commitment is empty (because everything that matters has to live somewhere) and that it is total (because every piece of state in the operating environment has to live in the substrate).

**State that must live in the substrate.**

(a) *Decisions.* Any decision the system or its operators may later need to recall, audit, or build on is substrate content.

(b) *Decision provenance.* Writer attribution, timestamp, rule reference, and antecedent references — all substrate content.

(c) *Active contradictions.* Per the conflict-preservation commitment (§2.1, §5), contradictions are first-class addressable substrate objects with their own identity and provenance, not error conditions held outside.

(d) *Conflict resolutions.* When a cell resolves a contradiction under an orchestration rule, the resolution decision — which version was used, under which rule, by which cell — is itself substrate content. Resolving does not erase the contradiction record; it records a resolution against it.

(e) *Orchestration rules.* The human-authored rules governing cell-level behavior are substrate content (§2.1, §2.3); changes to rules are themselves traceable substrate events.

(f) *Authority assignments.* Who has what governance authority over what substrate content is itself substrate content; authority is not a runtime configuration external to the substrate.

**State that may legitimately live outside the substrate.**

(a) *Source documents and unstructured inputs.* Cells may read source material — transcripts, documents, code, logs, prior artifacts — that is not substrate content. The substrate references and extracts from these inputs but does not own them, and the cells' reads are not themselves substrate writes.

(b) *LLM model weights and parametric knowledge.* The mediator's parametric knowledge is not substrate content. The substrate is what the LLM operates over, not what the LLM is.

(c) *Cell-internal execution state.* State that exists only during a cell's execution and is discarded when the cell completes is not substrate content. Only what the cell writes back to the substrate becomes part of the source-of-truth scope.

(d) *Derived views, caches, and projections.* A search index built over the substrate, a dashboard rendering substrate content, a backup, a materialized query result — all may exist outside the substrate without violating the commitment, provided they are derived from the substrate and treated as non-authoritative.

(e) *External systems with their own sources of truth.* Other systems the CKS substrate interacts with — databases, APIs, ticketing tools, workflow systems — maintain their own state under their own authority. The CKS substrate does not claim authority over them; the commitment is about coordination state, not about all state in the operating environment.

## 5. Failure modes that violate the commitment

Five failure modes recur. For each, the anti-pattern can be named and the adjacent CKS commitments it also violates identified.

(a) *Agent memory as source of truth.* The system answers "what was decided" from per-session or external agent memory rather than from substrate content. Violates source-of-truth and AI-as-substrate-mediator. Produces the failure mode the source paper names at §6.2 via Knowledge Objects' "context rot" framing: agent memory degrades through capacity overflow, compaction loss, and goal drift, but the system continues reading from it as if authoritative.

(b) *LLM context as source of truth.* Coordination state is held in the LLM's context across turns rather than written to the substrate. Violates source-of-truth and the substrate–cell boundary; also violates the deterministic characterization of the substrate side of the governance boundary (§4.1), because LLM context is not deterministic state.

(c) *Hidden state in cells.* Cells maintain coordination state between executions in cell-internal storage rather than substrate writes. Violates source-of-truth and the substrate–cell boundary, and undermines path retraceability because the trace runs through state the substrate cannot expose.

(d) *External tool state treated as authoritative for coordination questions.* The system answers "what was decided" or "who has authority" from a project-management tool, chat log, issue tracker, or other system not designed as a CKS substrate. Treating their content as authoritative is the violation. The acceptable pattern is the converse: extract the external tool's content into substrate content under cell mediation, and let the substrate be authoritative for the extracted state.

(e) *Caches treated as authoritative.* A derived view, cache, or projection is treated as the answer to a coordination question instead of as a derived view. The commitment requires that the substrate, not its projections, be authoritative; a stale projection that disagrees with the substrate is by construction wrong.

Across all five, implementations tend to look fine until a coordination question is asked the supposed source cannot answer correctly — and by then, recovery is expensive and traceability has already failed.

## 6. How the commitment depends on and enables other commitments

The source-of-truth commitment is not independent of the other CKS commitments; it depends on a small set and enables a larger set.

**Depends on.**

- *The substrate–cell boundary* (§2.1). Cells write to the substrate; cell-internal state is non-authoritative. Without this boundary, the substrate cannot be source of truth.
- *Tool-agnosticism's three minimal requirements* (§7.1): persistent structured state, human read/write access, and LLM access to substrate content. The substrate must be persistent and human-readable for it to function as source of truth at all.

**Enables.**

- *Path retraceability* (§3.1). The retraceable path runs through the substrate; if the substrate is not authoritative, the trace runs to a non-authoritative location and retraceability is meaningless.
- *Determinism on the substrate side of the governance boundary* (§4.1). Deterministic substrate content can be a source of truth; non-deterministic state cannot.
- *Conflict preservation* (§2.1, §5). Contradictions are first-class objects in the source of truth, not errors to be resolved away from the authoritative artifact.
- *Linear-cost scaling* (§6). Cell execution cost depends on selective substrate reads, which presupposes the substrate is the authoritative thing to read.

The commitment is the architectural anchor several other commitments hang from.

## 7. Operational test

A system implements the CKS substrate-as-source-of-truth commitment if and only if all of the following are true at all times during the substrate's existence:

1. Coordination questions — what was decided, by whom, under what authority, with what rationale, and what conflicts remain unresolved — are answered from substrate content alone.
2. State that affects coordination but lives outside the substrate (cell-internal execution state, LLM context, external systems, caches, derived views) is treated as non-authoritative; if it conflicts with substrate content, the substrate wins by definition.
3. When external state must affect coordination, it does so by being extracted into substrate content under cell mediation, not by being treated as authoritative in place.
4. Orchestration rules and authority assignments are themselves substrate content, not configuration external to the substrate.

A system that fails any of (1)–(4) may be useful, and may be governed in some other sense, but does not implement the substrate-as-source-of-truth commitment in the CKS sense.

## Conclusion

The CKS pattern's source-of-truth commitment is a precise and narrow claim: the substrate is the authoritative answer to coordination questions, with five named categories of coordination state in scope and a deliberate set of state categories explicitly out of scope. It is not a generic "single source of truth" claim, and it is not a database normalization decision. It is the architectural anchor that path retraceability, determinism, conflict preservation, AI-as-substrate-mediator, and linear-cost scaling all depend on, and it is the commitment most easily violated by drift — implementations that fail it tend to look like they are working until a coordination question is asked the substrate cannot answer.

Naming the commitment explicitly, and naming the failure modes that violate it, makes the architectural choice visible at design time rather than at the moment it becomes a problem. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should treat substrate-as-source-of-truth as the load-bearing commitment it is, and should name where the source of truth actually sits in any system claiming to instantiate the pattern.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Substrate Is the Source of Truth: Where State Lives in CKS Systems and Where It Cannot.* 26 April 2026. ORCID: 0009-0004-8065-3235.
