# "By Whom" as Standalone Accountability Question: Writer Attribution as Architectural Commitment in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the second of the four accountability questions §3.1 commits to — *by whom* — as a standalone architectural commitment with independent content, distinguishable from the other three accountability questions and from adjacent attribution patterns commonly conflated with it.

## Abstract

The CKS pattern's path-retraceability commitment (§3.1) requires that substrate content support four accountability questions: what was decided, by whom, under what authority, and with what rationale. The four questions compose into the integrated retraceability commitment treated in the integrating-frame note A2.35, but each has independent architectural content and is severable for purposes of design, implementation, and operational testing. This note formalizes the second question — *by whom* — as a standalone architectural commitment to writer attribution. The commitment is more specific than generic provenance: it requires that every piece of substrate content produced by deployment activity carry writer attribution; that the attribution architecturally distinguish humans, LLM mediators, and non-LLM-mediated cells as three writer classes; that human-writer attribution link to the writer's position in the deployment's authority structure; and that attribution be committed atomically with the content it accompanies. The note states the four operational components, distinguishes the commitment from four adjacent attribution patterns, identifies nine failure modes, traces how downstream CKS commitments depend on it, and provides an operational test for whether a system satisfies the commitment.

## 1. Why "by whom" needs to be formalized as a standalone accountability question

The parent foundational note A1.07 commits to four accountability questions as the operational content of the CKS path-retraceability commitment: what was decided, by whom, under what authority, and with what rationale. The integrating-frame note A2.35 establishes these four questions as a structured set and shows that each is severable — its architectural content is statable independently of how the others are answered. A2.36 specializes "what was decided" along this severable axis. This note specializes "by whom."

The motivating cases are deployments in which the substrate carries decisions but does not architecturally distinguish writers. Examples include: substrates where every write is attributed to a single system or service account, with the actual writer recoverable only from runtime logs; substrates where human writes and LLM-mediated writes use the same attribution mechanism with no architectural distinguishability between them; substrates where attribution is recorded only in audit logs external to the substrate, leaving substrate content with placeholder attribution; substrates where writers are identified by opaque user-account identifiers with no architectural link to the deployment's authority structure; and substrates where attribution is post-hoc inferred — by analyzing content for stylistic features or by correlating timestamps with login records — rather than committed at write time. Each of these patterns produces a substrate that cannot answer "by whom" from substrate alone, even when the substrate is otherwise rich enough to answer "what was decided" from substrate alone.

A second motivation is the strategic prior-art posture of the derivation-note series. The architectural commitment to writer attribution with class distinguishability is consequential prior art because it forecloses architectures where AI-generated and human-authored substrate content are indistinguishable in the substrate. Derivative work that treats writer attribution as a logging concern or a deployment-layer feature can be evaluated against the standalone commitment articulated here.

A third motivation is the relationship to Property E from the AI-as-substrate-mediator decomposition (A2.23). Property E is the mediator-side commitment that LLM operations resulting in substrate writes are recorded in substrate with attribution sufficient to identify them as LLM-authored. A2.37 is the substrate-side commitment that "by whom" is architecturally answerable for *all* writer classes — humans, LLM mediators, and non-LLM-mediated stable cells per A1.12 Mode 3. The two notes share content on LLM attribution at the cell→substrate boundary; they diverge on scope. Property E covers LLM-mediated writes; A2.37 covers the substrate's commitment to the writer-class taxonomy itself, of which the LLM class is one member.

## 2. The "by whom" commitment, defined precisely

The "by whom" commitment is the conjunction of four operational components. A system satisfies the commitment if and only if all four hold for substrate content produced by deployment activity, at all times during the substrate's existence.

**(a) Every piece of substrate content carries writer attribution.** For every decision §3.1 names — cell executions that write, direct human overrides per A2.03, rule authorings per A2.04 — the resulting substrate content carries non-empty writer attribution. The architectural commitment is that writer attribution is a required field of the substrate schema, not an optional or dispensable annotation. Substrate content with empty, null, or placeholder writer attribution does not satisfy the commitment regardless of what else it carries.

**(b) Writer attribution architecturally distinguishes writer classes.** The attribution distinguishes among three classes: (i) human writers — humans exercising the modify or override rights per A2.02 and A2.03 directly; (ii) LLM mediators — LLMs operating within cells under orchestration rules per A2.23 Property E; and (iii) non-LLM-mediated cells — stable cells per A1.12 Mode 3 that automate writes under rules without LLM involvement. The class distinction is *architectural* in the same sense the human-governed commitment from A1.01 is architectural: it is a property the substrate's schema commits to, not a property recoverable by inspection of content style or by consultation of external systems. Implementations that flatten the three classes into a single attribution mechanism — for example, attributing all writes to a single user-account-style identifier without an architectural class field — fail this component because readers cannot determine the writer class from substrate alone.

**(c) Human-writer attribution links to authority structure.** For human writers, the attribution does more than identify which human wrote: it supports queries that connect the human to their position in the deployment's authority structure per A1.01. Authority structure is itself substrate content — the human-governed commitment locates rights at the architectural layer, which means the rights' beneficiaries and scopes are recorded in the substrate. The architectural commitment is that the human-writer attribution is queryable in a way that recovers the writer's authority context at write time. An opaque human-user identifier with no architectural connection to authority structure fails this component because the attribution does not support governance operations: a reader can answer "which human wrote this" but not "which human, with what authority, wrote this."

**(d) Attribution is committed atomically with the content.** The cell→substrate write per A2.10 commits substrate content and attribution metadata as a single architectural commit. There is no window during which substrate content exists without attribution attached. Implementations in which content lands in substrate first and attribution is appended afterward — by a runtime annotator, by a post-write enrichment pipeline, by an offline log-correlation step — fail this component because the substrate has, however briefly, content whose architectural answer to "by whom" is empty.

The four components together define the commitment. Three components alone are not sufficient: dropping (a) admits anonymous writes; dropping (b) admits LLM-human conflation; dropping (c) admits opaque human attribution; dropping (d) admits race conditions during which "by whom" is unanswerable. Each component is independently load-bearing.

## 3. What the commitment does NOT claim

The standalone treatment is precise about what the commitment requires; the same precision distinguishes what it does *not* require, so that downstream implementers do not over-read the architectural content into deployment specifics.

**It does not require attribution to identify natural persons by name.** The architectural commitment is that attribution identifies the writer within the deployment's authority structure. Names, account identifiers, role-and-individual pairs, cryptographic keys, or any other scheme are admissible, provided the class distinguishability and authority-linkage components hold.

**It does not specify the attribution format.** Attribution metadata may be encoded as structured fields, identifier strings, signed objects, enumerated types, or any combination. The commitment is to what the metadata must distinguish and link to, not how it is encoded.

**It does not require visual prominence in interfaces.** Interfaces may render substrate content with various levels of attribution visibility. The commitment is to attribution as substrate metadata accessible through the inspect right per A2.01; presentation choices are deployment-layer.

**It does not require specific tooling for queries.** Attribution must be queryable through standard substrate read operations per A2.25 Requirement 2. Specialized querying tools may add convenience, but the commitment is to queryability through the standard substrate interface, not through any specific tool — which is what makes the commitment compatible with the tool-agnosticism commitment from A1.05.

**It does not require sub-write attribution granularity.** A single cell→substrate write may contain content jointly produced — for example, a human reviewer editing an LLM draft and committing the edited result. The commitment is to write-level attribution, not to token-level or field-level attribution. How a deployment treats jointly-produced writes is a schema-and-rule decision; the architectural commitment is that whatever the schema records is the writer of the write, attributed at the time of commit.

**It does not specify how authority changes propagate.** Authority structure may evolve: humans gain or lose authority, take or leave roles. Attribution recorded at write time reflects the writer's authority at write time. The commitment is to retraceable write-time authority, not to dynamically updated authority on past writes; the corresponding anti-pattern is named in §6.

## 4. What the commitment is NOT

Four adjacent attribution patterns are commonly conflated with the "by whom" commitment. Each is a coherent design choice in some other architecture and a failure of the architectural commitment in CKS.

**Not anonymous attribution.** Some implementations record writes with empty, null, or placeholder writer fields, treating attribution as optional or context-dependent. The architectural commitment is that every piece of substrate content has non-empty writer attribution; anonymous writes fail it because "by whom" is not architecturally answerable for that content.

**Not role-only attribution.** Some implementations record writes with role identifiers ("decision-maker," "reviewer," "administrator") without distinguishing which specific human or LLM occupied the role at write time. Role-only attribution fails the architectural commitment because multiple writers may share a role; the architecture must distinguish them. A deployment may record both role and specific writer; role alone is insufficient.

**Not system-account attribution.** Some implementations route all writes through a single system or service account, with the actual writer identified only in external systems — runtime traces, agent execution logs, identity-broker records. System-account attribution fails the architectural commitment because the substrate cannot answer "by whom" from substrate alone. This pattern is particularly common in deployments where LLM mediators commit through service accounts shared with humans, producing the LLM-human conflation named in §6.

**Not post-hoc attribution inference.** Some implementations infer writer attribution after the fact — by analyzing content for stylistic features, by correlating substrate writes with login or session records, by consulting external execution traces. Post-hoc inference may approximate attribution but fails the architectural commitment because attribution is reconstructed rather than recorded; the atomic-with-content commit (§2(d)) is what the architectural commitment names, and reconstruction is what replaces it when the commitment is dropped.

## 5. Why "by whom" is load-bearing for downstream commitments

The "by whom" commitment is load-bearing for several CKS commitments; weakening it weakens them.

It is load-bearing for **the human-governed commitment from A1.01.** Human governance requires that humans can be held accountable for the decisions they make, and "by whom" is what makes accountability architecturally specific: substrate carries who made each decision, with the human's authority context recoverable.

It is load-bearing for **the AI-as-substrate-mediator commitment from A1.04 and A2.23 Property E.** Property E specifies that LLM-mediated writes carry attribution sufficient to identify them as LLM-authored; A2.37 is the substrate-side commitment that the writer-class taxonomy this attribution participates in is itself architectural. Property E presupposes the class distinction A2.37 commits to.

It is load-bearing for **the conflict-as-first-class commitment from A1.03.** Conflict resolution decisions reference contradicting content through provenance per A2.15; "by whom" is part of that provenance for both the contradicting writes and the resolution.

It is load-bearing for **the labor-allocation framework from A1.12.** The framework's three modes — direct human, LLM-under-rule, stable-cell automation — produce writes attributable to different writer classes. "By whom" is what makes the modes architecturally distinguishable in substrate state; without the class taxonomy, the modes blur in substrate.

It is load-bearing for **the architectural-property qualifier from A2.06.** Governance is architectural rather than procedural in part because attribution is in substrate, not in process. "By whom" being substrate metadata is what makes attribution part of the architectural commitment.

## 6. Failure modes that violate the commitment

Each of the following anti-patterns names a way an implementation can fail the architectural commitment. The patterns appear in deployments under operational pressure to integrate with enterprise identity systems, simplify audit overhead, or accommodate LLM tooling that does not natively expose attribution at the substrate boundary.

**(a) Service-account attribution.** All writes are attributed to a single service account; actual writers are identified only in external systems. The substrate cannot answer "by whom" from substrate alone, and substrate-only paths (treated in A2.41) are broken with respect to writer attribution.

**(b) LLM-human conflation.** LLM-mediated writes and human writes are recorded with the same attribution mechanism, with no architectural distinguishability between them. This is the most common failure in deployments that mediate LLM writes through identity systems originally designed for human user accounts.

**(c) Anonymous writes.** Some writes carry empty, null, or placeholder writer fields. The commitment to every substrate content carrying attribution is broken; "by whom" is unanswerable for the affected content.

**(d) Role-only attribution.** Writes are attributed to roles without specific writer identification. Multiple writers occupying the role are indistinguishable in substrate.

**(e) Authority-context detached.** Writers are identified, but human-writer attribution does not link to the deployment's authority structure. Readers can determine who wrote but not what authority they held.

**(f) Post-hoc attribution inference.** Attribution is inferred after the fact rather than recorded at write time. The atomic-with-content commit is broken.

**(g) Attribution drift after authority changes.** When authority structure changes, the implementation updates attribution on past writes to reflect current authority rather than preserving write-time authority. Historical retraceability is forfeited for current consistency.

**(h) External-only attribution.** Substrate carries placeholder attribution; the actual attribution lives in audit logs or external identity systems. Substrate-only paths fail because answering "by whom" requires consulting external systems.

**(i) Stable-cell-as-human attribution.** Writes produced by stable cells (Mode 3 from A1.12) are attributed to the humans who configured the cell, blurring the distinction between cell-produced writes and human-produced writes. The architectural class distinction fails: Mode 3 writes appear in substrate as Mode 1 writes.

## 7. Operational test

A system satisfies the "by whom" commitment if and only if all of the following are true at all times during the substrate's existence:

1. Every piece of substrate content produced by deployment activity carries non-empty writer attribution.
2. Writer attribution architecturally distinguishes among humans, LLM mediators, and non-LLM-mediated cells; a reader can determine the writer class from attribution alone.
3. For human writers, the attribution links to the writer's position in the deployment's authority structure at write time, and the link is queryable from substrate (since authority structure is itself substrate content).
4. Attribution is committed atomically with the content at the cell→substrate write per A2.10; there is no window during which substrate content exists without attribution.
5. Attribution is queryable from substrate alone through standard read operations per A2.25 Requirement 2; answering "by whom" does not require consulting external systems. The substrate-only-paths property in full is treated in A2.41; here it appears as a derivable consequence of the previous four conditions plus tool-agnosticism per A1.05.

A system that fails any of (1)–(5) does not satisfy the "by whom" commitment in the architectural sense, regardless of how attribution is provided through other means.

## 8. Why naming "by whom" as a standalone commitment matters

Implementations under pressure to integrate with enterprise identity systems, simplify audit overhead, or accommodate LLM tooling that does not natively expose attribution at the substrate boundary consistently drift toward one or more of the failure modes in §6. The drift is steady because identity infrastructure is operationally complex, and the shortcuts — service accounts, role-only attribution, external-only logging — feel architecturally simpler than committing to the four operational components in §2.

The downstream consequences are not abstract: governance failures, where humans cannot be held accountable for decisions made through service accounts; AI-versus-human ambiguity, where LLM-generated content blends with human-authored content in substrate; authority-context loss, where writers cannot be queried for the authority they held at write time; and substrate-only-paths failures, where retraceability requires external attribution systems the architecture's traceability commitment explicitly rules out.

Naming "by whom" as a standalone architectural commitment gives downstream implementers a precise specification of what writer attribution requires architecturally. The remaining specializations of A1.07 — A2.38 ("under what authority"), A2.39 ("with what rationale"), A2.40 (the six provenance metadata fields), and A2.41 (substrate-only paths) — give the rest of the operational decomposition. Together with A2.35 (the integrating frame) and A2.36 ("what was decided"), they specify what a CKS substrate must carry for the path-retraceability commitment §3.1 introduces to be operationally exercisable rather than nominally claimed.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *"By Whom" as Standalone Accountability Question: Writer Attribution as Architectural Commitment in the Coordination Knowledge Substrate Pattern.* May 4, 2026. ORCID: 0009-0004-8065-3235.
