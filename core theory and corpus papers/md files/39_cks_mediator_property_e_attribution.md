# Recorded, Not Inferred: Property E of the AI-as-Substrate-Mediator Role in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 2, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize Property E of the AI-as-substrate-mediator role — the commitment that LLM operations producing substrate writes are recorded in substrate state with provenance metadata distinguishing the LLM as the writer — as a standalone architectural commitment that can be defended, implemented, and tested independently of the other four mediator properties. Property E is the fifth and final specialization in the AI-as-substrate-mediator decomposition (A2.18–A2.23).

## Abstract

The CKS pattern defines AI-as-substrate-mediator as a five-property role; A1.04 names the role and A2.18 establishes the five properties as severable architectural commitments. This note formalizes Property E — when an LLM operation within a CKS cell produces a substrate write, the substrate's provenance metadata for that content architecturally distinguishes the LLM as the writer — as a standalone commitment. Property E is the LLM-specific specialization of the writer-attribution field within the broader provenance commitment from §3.1 (path retraceability) and the planned six-field commitment in A2.40. The note states four operational components of Property E, five things it does not require, four adjacent provenance patterns it is conflated with, eight failure modes, its load-bearing role across five downstream commitments, and a four-condition operational test. With this note, the AI-as-substrate-mediator decomposition (A2.18–A2.23) is fully specified.

## 1. Why Property E needs to be formalized as standalone

A1.04 commits to AI-as-substrate-mediator as a five-property role. A2.18 establishes the five properties as severable architectural commitments — each holds independently of how the others are realized, and each fails independently when violated. Properties A through D have been formalized as standalone in A2.19–A2.22. This note formalizes Property E.

Property E has independent operational content for three reasons.

First, implementations frequently satisfy Properties A through D and still fail at Property E. The motivating cases are recognizable. An LLM mediator commits substrate writes through a service account that the substrate treats as a human user. A cell records "cell X wrote this" without distinguishing which of its writes were LLM-mediated. A deployment uses an anonymous commit identity for all substrate writes, on the reasoning that schema simplicity is preferable to attribution complexity. An external audit log records the LLM operations behind specific writes, but the substrate's own provenance metadata for those writes carries human or anonymous attribution. In each case, Properties A–D are intact: the LLM reads from the substrate, writes under rules, holds no external state, and exercises no authority. What fails is the architectural distinguishability of the writes once committed.

Second, the strategic prior-art posture. Patentable derivations of CKS that target AI-output attribution mechanisms — content provenance for AI-generated material, AI-versus-human distinction patterns, AI accountability systems — are substantially more contestable as novel inventions when Property E is publicly formalized as a standalone commitment with a precise operational specification.

Third, the connection to source of truth (A1.08). The substrate is authoritative for "by whom" as one of the five categories of source-of-truth content. Property E makes "by whom" architecturally specific for LLM-mediated content: the substrate's authoritative answer to "who wrote this" must distinguish LLM writers from human writers as part of substrate state, rather than collapsing the two and recovering the distinction (if at all) from external systems.

## 2. The Property E commitment, defined precisely

In the CKS pattern, a system satisfies **Property E** if and only if the following four components hold for substrate content produced by LLM operations within cells.

**(a) Substrate-internal attribution.** The substrate's provenance metadata for the content architecturally distinguishes the LLM as the writer. The distinction is sufficient for downstream consumers — humans exercising the inspect right, cells reading substrate content as input, audit operations, governance reviews — to identify that the content was produced by an LLM operation, not by a human directly and not by a non-LLM-mediated cell operation. The mechanism by which the substrate encodes the distinction (writer-type field, structured writer-identifier, metadata layer, cryptographic signature, or any other approach) is a deployment choice; what is committed is the distinction.

**(b) Atomic commitment with content.** The attribution is recorded as part of the cell→substrate write operation per A2.10, not as a side effect or post-hoc annotation. The attribution and the content commit atomically; no intermediate state exists in which the content is in substrate state without its attribution.

**(c) Authoritative-state membership.** The attribution is part of the substrate's authoritative state, readable through normal substrate inspection without consulting external audit logs, runtime tracking systems, or vendor-side telemetry. Audit logs may carry additional context about the LLM operation — execution traces, intermediate computation, prompt content — and this complements the attribution; it does not substitute for it.

**(d) Durability over time.** The attribution persists as long as the substrate content persists. Automated processes — compression, normalization, schema migration, deduplication — do not strip, degrade, or normalize the attribution out of substrate state. The attribution remains a property of the substrate content for the content's lifetime.

A system that satisfies fewer than four of (a)–(d) produces LLM-mediated substrate content that is partially attributable, breaking the architectural commitment.

## 3. What Property E does not require

Each of the following is sometimes mistaken for a requirement of Property E, but is not.

**Specific LLM identification.** The architectural commitment is to LLM-versus-human distinction. Identifying which specific model, version, or vendor produced the write is a deployment choice. A deployment recording only "an LLM produced this" satisfies Property E; one additionally recording the model identifier satisfies Property E plus a deployment-chosen extension.

**Human-readable encoding.** The attribution may be encoded in any form the substrate's schema supports — boolean flags, enumerated types, structured identifiers, cryptographic signatures, or any other representation. What matters is architectural distinguishability for substrate consumers, which may include programmatic consumers as well as humans.

**UI prominence.** The architectural commitment is about substrate state, not user experience. Interfaces may present LLM-written content without visually distinguishing it from human-written content, provided the underlying substrate state preserves the distinction and humans exercising the inspect right can access the attribution when needed.

**Sub-write granularity.** When a single substrate write contains content jointly produced by an LLM and a human — for example, a human-edited LLM draft committed by the human — the attribution reflects how the substrate's schema and orchestration rules treat the write, typically as a human write with rationale referencing LLM input. Token-, sentence-, or field-level attribution within a single write is a deployment choice beyond the architectural commitment.

**LLM reasoning preservation.** Reasoning, intermediate computation, and decision logic during the LLM's execution are cell-internal state per A2.11; they are not substrate content and are not subject to Property E. What Property E requires is attribution of the substrate write, not preservation of the path the LLM took to produce it.

## 4. What Property E is not — adjacent patterns it is conflated with

**Not generic audit logging.** Audit logs record events external to the substrate: which user accessed which content, which API calls were made, which processes ran. They may include LLM-write events, but they are not the architectural mechanism Property E requires. Property E requires attribution embedded in the substrate's provenance metadata for the content itself; audit logs may complement this but cannot substitute for it.

**Not anonymous cell attribution.** Some implementations attribute all cell-mediated writes to "the cell" without distinguishing LLM-mediated from non-LLM-mediated cell behavior. The attribution captures cell origin but not the LLM's specific role within the cell's execution. Property E is finer: the architecture requires distinguishing LLM mediation specifically, not just cell origin.

**Not post-hoc attribution.** Some implementations track LLM involvement after-the-fact through inference — analyzing content for LLM characteristics, looking up cell execution history, consulting external tracking systems. Post-hoc attribution may produce reasonable identification of LLM-written content in many cases, but it is not part of the substrate's authoritative state. Property E requires attribution as part of the substrate's authoritative state at write time; post-hoc inference does not satisfy the commitment, regardless of how reliable the inference is in practice.

**Not signed-by-LLM as authority.** Some patterns have LLMs cryptographically sign their outputs, positioning the LLM as a signing authority over the content. Property E is architecturally different: the LLM is being attributed as a writer, not positioned as an authority. Property D specifically forbids LLMs from exercising authority over substrate content; Property E records the LLM as the writer of content authorized by an orchestration rule. Cryptographic signatures may be used to realize Property E's attribution mechanism, but the architectural meaning is attribution, not authority. Conflating the two is the most consequential of the four confusions, because it undoes Property D as well as Property E.

## 5. Why Property E is load-bearing for downstream commitments

Property E does specific work that several other CKS commitments depend on.

**Path retraceability (A1.07).** The retraceable path of any decision must include attribution of who wrote each piece of substrate content along the path. Property E is what makes LLM-written content distinguishable in this path; without it, paths through LLM-mediated content have ambiguous writer identity at every LLM-mediated node, and the path retraceability commitment §3.1 imports from Rajabi and Kafaie (2022) holds in form but not in substance.

**Source of truth (A1.08).** The substrate is authoritative for "by whom" as one of the five source-of-truth categories. Property E specializes "by whom" for LLM-mediated content: the substrate distinguishes LLM writers from human writers as part of authoritative state, rather than admitting two definitions — one in substrate state, another in audit logs. A substrate that requires consulting external systems to answer "by whom" for some writes is no longer authoritative for that category; the commitment has been outsourced.

**Human-governed and the inspect right (A1.01, A2.01).** Human governance depends on humans being able to differentially review what LLMs produced and what humans produced when exercising the three rights. The inspect right operates differently when applied to LLM-mediated content (a human reviewing what an LLM wrote under rules) than to human-mediated content (a human reviewing what another human wrote): the questions, the standards, and the appropriate level of skepticism are not the same. Property E lets the inspect right know which mode it is operating in.

**Labor allocation (A1.12).** The labor allocation framework distinguishes Mode 1 (direct human labor), Mode 2 (LLM under rule), and Mode 3 (stable-cell automation). Property E is what makes Mode 2 outputs architecturally distinguishable from Mode 1 outputs in substrate content; without it, the modes are distinct at the cell layer but blur at the substrate state layer. A deployment loses the ability to read its own substrate and answer "which writes here were Mode 2?"

**Conflict-as-first-class (A1.03).** When LLM-mediated content contradicts other substrate content, the contradiction's relationship metadata may need to reflect that one side is LLM-mediated and another is human-mediated, because the resolution rule for "human-versus-LLM contradiction" is not generally the same as for "human-versus-human" or "LLM-versus-LLM." Property E provides the architectural distinction the conflict relationship metadata can reference.

**Property B as write-axis pair.** Property E and Property B together close the write loop. B specifies how LLM writes happen — under orchestration rules. E specifies how the writes are recorded — with LLM-distinguishing attribution. A system satisfying B without E produces LLM writes that are rule-governed at the write moment but indistinguishable from non-LLM writes afterward; a system satisfying E without B produces correctly-attributed LLM writes that occurred without rule authorization. Together — and only together — they make LLM writes architecturally complete: rule-governed at commit, traceable thereafter.

## 6. Failure modes that violate Property E

Each of the following names a way an implementation can fail Property E specifically.

**(a) Anonymous attribution.** The substrate records that a write happened without identifying the writer at all. The attribution metadata field is empty, null, or populated with a placeholder. LLM-written and human-written content are indistinguishable in substrate state. The most common cause is schema simplification chosen ahead of any consumer needing to differentially handle writes by writer identity.

**(b) Human-only attribution.** The substrate records all writes as human-written, even when LLM operations produced them. This typically arises when LLM mediators commit through service accounts the substrate treats as ordinary human users. From the substrate's perspective, the LLM is invisible; its writes appear under whatever account name the service account holds.

**(c) Cell-only attribution.** The substrate records "cell X wrote this" without distinguishing whether the cell's write was LLM-mediated. Downstream consumers can identify the cell but not the LLM's role; they would have to know, out-of-band, which of the cell's code paths involve LLM operations.

**(d) External-only attribution.** The substrate's provenance metadata for the content is anonymous or human-only, but an external audit log identifies LLM mediation. The attribution exists, but not in the substrate's authoritative state. Consumers reading substrate content directly do not see LLM attribution; they would have to consult external systems to recover it.

**(e) Post-hoc attribution.** The deployment infers LLM mediation from content characteristics or execution history after the fact. The inference may be reasonable but is reconstructed from evidence rather than recorded as authoritative state. The attribution is approximate where Property E requires it to be definite.

**(f) Degraded attribution over time.** The substrate initially records LLM attribution, but automated processes (compression, normalization, schema migration, deduplication) strip the attribution metadata as part of operations targeting other concerns. The substrate carries the content but no longer the LLM-write distinction. This failure mode is particularly subtle because it produces a substrate that satisfies Property E for recent content but fails it for older content; the failure is invisible at write time and surfaces only when historical content is consulted.

**(g) Atomic-decoupled attribution.** The substrate records the content and the attribution in separate write operations, with the possibility that one commits while the other does not. Intermediate states exist in which one is in substrate state without the other. The decoupling can arise from architectures that treat attribution as a secondary metadata layer with its own write path, or from migration patterns that backfill attribution into pre-existing content.

**(h) Selective attribution.** The substrate records LLM attribution for some content types but not others, based on deployment configuration or schema choices that vary by entity type. The architectural commitment is to attribution for all LLM-mediated substrate content; selective coverage produces a substrate where the same question — "who wrote this?" — has architecturally different answers depending on which entity is being asked about.

## 7. Operational test

A system satisfies Property E if and only if all of the following are true at all times during the substrate's existence.

1. Every piece of substrate content produced by LLM operations within cells carries provenance metadata that architecturally distinguishes the LLM as the writer, sufficient for downstream consumers to identify it as LLM-mediated rather than human-mediated or non-LLM-mediated cell-mediated.

2. The attribution is recorded as part of the cell→substrate write operation, committed atomically with the content; no intermediate state exists in which the content is in substrate state without its attribution.

3. The attribution is part of the substrate's authoritative state, accessible through normal substrate inspection without consulting external audit logs, runtime telemetry, or vendor-side tracking systems.

4. The attribution persists as long as the substrate content persists; automated processes do not strip, degrade, or normalize the attribution out of substrate state.

A system that fails any of (1)–(4) does not satisfy Property E in the architectural sense, even if its other mediator properties are preserved and even if external systems track LLM involvement with high reliability.

## 8. Why naming Property E as standalone matters

Implementations under pressure to simplify substrate schemas, normalize content for clean presentation, or unify writer identification across humans and LLMs consistently drift toward losing the LLM-versus-human distinction at the substrate layer. The drift is steady because attribution feels like an implementation detail rather than an architectural commitment; the substrate appears to work whether or not LLM attribution is preserved, because the failure mode does not produce immediate operational error. It produces governance ambiguity, traceability gaps, source-of-truth failures, and labor-allocation indistinguishability — failures that surface downstream of the missing attribution, often in different operations than the writes that lacked attribution.

Naming Property E as a standalone architectural commitment — with the four components in section 2, the limitations in section 3, the four adjacent-pattern distinctions in section 4, the load-bearing connections in section 5, and the eight failure modes in section 6 — gives downstream implementers a precise specification of what Property E requires and what it does not. Subsequent work that adopts the CKS pattern in implementations involving LLM-mediated substrate writes should preserve Property E as formalized here. Subsequent work that argues against it should name the difference.

With this note complete, the AI-as-substrate-mediator decomposition (A2.18–A2.23) is fully formalized. A2.18 established the severable-set structure; A2.19 through A2.23 specialized each of the five properties — substrate as primary input (A), writes under rules (B), no external state (C), no authority (D), and attribution on write (E). Together the six notes constitute the operational decomposition of A1.04. Any system claiming CKS-coherence on the mediator-role axis must satisfy all five properties; any system claiming a novel innovation on the LLM-attribution axis specifically must do so in territory not already specified by the five-component definition, the four-distinction taxonomy, the five load-bearing connections, the eight failure modes, and the four-condition operational test established in this note.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Recorded, Not Inferred: Property E of the AI-as-Substrate-Mediator Role in the Coordination Knowledge Substrate Pattern.* May 2, 2026. ORCID: 0009-0004-8065-3235.
