# Conflict Preservation as Paper 1's Second Architectural Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to anchor the paper-level claim that conflict preservation in the substrate is a first-class architectural property, to name the architectural commitment that claim makes, and to map the Series A derivation tree of sub-commitments that decompose from it. The note functions as a parent node in the Series A derivation graph; the operational mechanics of two-level conflict handling are formalized in the foundational sub-commitment note that derives from this anchor, not restated here.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern is defended in *Coordination Outside the Model* through six architectural commitments. The second of those commitments — conflict preservation as first-class substrate state — is an architectural property of the substrate itself, not a process recommendation about how teams should handle disagreement. It commits the substrate to *structurally support* holding conflicting states simultaneously, with each conflicting state addressable as a first-class object carrying its own identity and provenance, and it commits cell-level behavior over conflicting state to be determined by human-authored orchestration rules rather than by LLM-driven resolution. This anchor note formalizes the claim as the source paper states it, identifies its two-level structure, names the three anti-patterns it defends against (silent conflict resolution, detect-resolve-forget, contradiction collapse by automation), acknowledges OIDA's signed contradiction edges as cited prior art on the conflict-as-first-class-object axis, and maps the Series A sub-commitments that derive from this parent claim. It is the parent anchor for the Series A derivation tree on conflict preservation; operational decomposition is the work of the notes that derive from it.

## 1. Position of this claim within Paper 1's six commitments

The source paper defends the CKS pattern through six architectural commitments, listed in its abstract as: hybrid substrate-LLM division of labor; conflict preservation as first-class substrate state; human-governed authority; AI as substrate mediator; tool-agnosticism at the substrate layer; and linear-cost scaling. The second of these commitments — conflict preservation as first-class substrate state — is what this anchor formalizes. The paper develops the commitment in §5 (and its subsections §5.1–§5.4) and references it in Claim 1's enumeration of substrate properties (§3.1) as the conflict-preserving property of any CKS substrate.

The claim's position in the six-commitment list, second after the hybrid substrate-LLM division, is load-bearing. The first commitment establishes the substrate as a distinct architectural object held outside the LLM; the second specifies what kind of object that substrate must be at the conflict layer — not only persistent and structured, but *capable of holding contradiction as substrate content*. The remaining four commitments layer governance, role, portability, and cost properties over a substrate already committed to first-class conflict preservation. Removing this second commitment collapses the rest of the pattern back toward conventional structured-memory designs in which contradictions are defects to be cleaned rather than substrate content to be carried.

## 2. The claim, stated precisely

Paper 1's second architectural claim is this:

> Contradictions, inconsistencies, and unresolved ambiguities encountered during AI-mediated coordination are persisted in the substrate as first-class, addressable structured objects with their own identity and provenance — attached directly to the conflict itself (which rule, from which prior decision, under which role or context), not only to downstream decisions the conflict influenced. These objects are re-addressable across sessions. At the substrate level, conflicts are preserved by default. At the cell level, responses to preserved conflicts follow human-authored orchestration rules rather than LLM-driven resolution.

This is paraphrased from §5.1 of the source paper, retaining the four load-bearing architectural ingredients §5.1 explicitly identifies: conflict-as-object with identity, provenance attached to the conflict itself, deferral as terminal recorded outcome, and cross-session re-addressability.

Two properties of the claim are worth pulling out before any decomposition.

**The claim is architectural, not procedural.** It does not recommend a meeting cadence, a review protocol, or a workflow stage at which conflicts get aired. It commits the *substrate*, as an architectural object, to structurally support holding conflicting states simultaneously. A substrate that cannot carry two contradicting pieces of content addressably and with attached provenance is not a CKS substrate, regardless of what processes operate over it. A substrate that can carry such content but does so only in an append-only log behind the working state — so that cells executing over the substrate never see the contradiction as live state — also fails the architectural commitment; the contradiction must be carried *as state*, not as history about state.

**The claim is symmetric in scope to the human-governance commitment.** It binds the substrate at the same level "human-governed" binds it: the property must be available at any time during the substrate's existence, not at predetermined checkpoints, and the preservation must be guaranteed against operations performed by the LLM, by automated processes, and by runtime middleware. §5.3 states this absolutely — no LLM operation over the substrate may silently merge, discard, or force resolution of preserved contradictions, regardless of delegation level. Conflict preservation is therefore an inviolable architectural property of the substrate, in the same sense the inspect/modify/override rights are inviolable architectural properties under the human-governance commitment.

## 3. The two-level structure

The claim has a two-level architectural structure, developed in §5.3 of the source paper.

**Substrate level — preservation.** Conflicts in substrate content are recorded as substrate content. They have writers, timestamps, rationale (where applicable), and explicit relationship to the contradicting content. They are addressable and re-addressable across sessions. They persist until a human exercising authority over the substrate, or a human-authored orchestration rule explicitly authorizing collapse for the specific case, resolves them. They are never collapsed silently by an LLM operation, an automated process, or a runtime middleware layer.

**Cell level — resolution under orchestration rules.** When a cell executes over substrate content containing active conflicts, the cell's response is determined by orchestration rules humans authored in advance. The rules may direct the cell to preserve and skip, to surface the conflict to a participant, to delegate it to another substrate, to defer with a recorded outcome, or to apply a pre-specified resolution logic under specified conditions. The resolution decision is itself recorded as substrate content, with its own writer (the cell, executing under a named rule), its own timestamp, and its own reference to the rule that authorized it.

**The coupling.** The two levels are halves of a single commitment, not separable. Substrate-level preservation makes cell-level resolution decisions auditable: because the underlying contradiction persists, a later participant can see both what the cell resolved and what it resolved against. Cell-level resolution under rules makes substrate-level preservation operationally tolerable: cells do not halt at every conflict, so the substrate can carry conflicts indefinitely without blocking the work the cells exist to perform. The architectural constraint, as §5.3 puts it, is not on *whether* conflicts get resolved — they often do — but on *who decides* resolution logic and *where the resolution lives*. Humans decide; resolutions live as new substrate content layered over the contradicting content, not as deletions of it.

This two-level structure is what distinguishes the claim from two adjacent but unworkable readings: a never-resolve commitment (substrate carries conflicts forever, cells halt forever) and a resolve-as-usual commitment (cells resolve conflicts by the same means everyone else does, with substrate-level history kept only for retrospective audit). Neither captures what the source paper commits to.

## 4. What the claim defends against

The claim defends against three architectural patterns, each of which collapses one of its halves or its coupling. Each pattern is formalized as a Series A anti-pattern note (A3.08–A3.10) that derives from this anchor.

**Silent conflict resolution (A3.08).** A pattern in which the system detects a contradiction in substrate content, applies a resolution rule automatically, and writes only the resolved value back. The contradiction never becomes substrate content; the resolution is not attributed to any rule a human authored; subsequent participants see the resolved state and no record of what was resolved. The pattern violates substrate-level preservation: the conflict is collapsed before becoming substrate state.

**Detect-resolve-forget (A3.09).** The pattern §5.4 of the source paper names explicitly as the dominant alternative in current LLM agent frameworks. Contradictions are detected at inference time, reconciled in-session through clarification, majority voting, or judge-LLM arbitration, and discarded once the session ends. Instantiations in the 2024–2025 literature include RAG contradiction-detection with context validators, explanation-generation work that succeeds by flipping a contradiction label to entailment, clarification-question agents that overwrite prior estimates, and stress-testing frameworks that synthesize contradictions for evaluation rather than preservation. The pattern violates substrate-level preservation and cross-session re-addressability together: the contradiction is transient state in the LLM's working context, not substrate content.

**Contradiction collapse by automation (A3.10).** A pattern in which cell-level resolution proceeds, but the rule under which it proceeds is not human-authored — the cell applies a default arbitration policy embedded in the runtime, a vendor-specified merge rule, or an LLM-selected resolution. The contradiction may or may not be preserved as substrate content; what is violated is the *who decides* constraint. Resolution logic is outside human authority, and the architectural commitment Claim 2 makes is specifically that humans decide resolution logic, either directly by editing substrate content or indirectly by authoring the rules cells execute under.

The three anti-patterns are not redundant. Silent resolution violates the substrate-level half; detect-resolve-forget violates both halves and the cross-session property; collapse-by-automation may satisfy preservation but violates the authority-over-resolution-logic property. A pattern that fails any of the three fails Claim 2.

## 5. OIDA's signed contradiction edges as cited prior art

The source paper is explicit, in §5.2, that the strongest 2024–2026 adjacent precedent for treating contradictions as first-class addressable substrate state is OIDA's *signed contradiction edges*: a typed edge between two Knowledge Objects that has its own schema presence, points to both conflicting objects, and persists in the substrate rather than existing as transient state consumed in a single inference pass. The architectural move OIDA makes — promoting the contradiction relationship to first-class substrate state, on the same terms as the contradicting objects themselves — is precedent for the relationship-as-first-class half of Claim 2's provenance requirements.

§5.2 also states that OIDA does not scoop the claim. Three architectural axes separate the two designs: OIDA does not commit to human governance of the substrate as a design requirement; OIDA does not encode formal role/authority semantics at the cell level; and OIDA frames the AI as a substrate client consuming structured memory, not as a mediator over a human-governed artifact. Claim 2's contribution is the *architectural combination* — substrate-level preservation, provenance attached to the conflict itself, cross-session re-addressability, deferral as terminal outcome, all under the human-governance commitment, with cell-level resolution under human-authored orchestration rules — of which OIDA realizes a portion. The cited prior art strengthens defensibility on the contradiction-as-first-class-object axis specifically; the wider two-level commitment that combines that axis with human-governed authority and rule-governed cell-level resolution is what Claim 2 contributes as architectural pattern.

A separate Series A note (A2.17) treats the OIDA prior-art relationship in its own right, identifying which architectural ingredient OIDA supplies and which ingredients Claim 2 contributes on top of it. This anchor names the relationship; A2.17 develops it.

## 6. Derived sub-commitments in the Series A tree

The following Series A sub-commitments derive from Claim 2 as decompositions, operational variants, anti-patterns, and prior-art treatments under this anchor.

**Foundational sub-commitment (Phase A1):**

- **A1.03** — Conflict as first-class object: the two-level handling commitment, formalized in operational detail with the four-property provenance requirement (writer, timestamp, rationale, relationship-to-contradicting-content), the contrast with detect-resolve-forget, and the operational test. A1.03 is the primary decomposition node beneath this anchor.

**Operational variants (Phase A2):**

- **A2.13** — Substrate-level conflict preservation as a stand-alone architectural property, formalized independently of cell-level resolution so the substrate-level half is portable to architectures that do not adopt the cell-level half.
- **A2.14** — Cell-level conflict resolution under human-authored orchestration rules as a stand-alone architectural property, formalized independently of substrate-level preservation so the cell-level half is portable to architectures that do not adopt the substrate-level half.
- **A2.15** — The two-level coupling property: the architectural argument that neither half is workable alone and that their combination is what produces Claim 2's pattern. A2.15 is the load-bearing companion to A2.13 and A2.14.
- **A2.16** — Provenance requirements for first-class conflicts: the four-property requirement (writer, timestamp, rationale, explicit relationship to contradicting content) formalized as a substrate-content schema rather than as a property of the system overall.
- **A2.17** — OIDA's signed contradiction edges as cited prior art for the contradiction-relationship-as-first-class architectural move, with the three-axis differentiation §5.2 of the source paper develops.

**Anti-patterns (Phase A3):**

- **A3.08** — Silent conflict resolution.
- **A3.09** — Detect-resolve-forget.
- **A3.10** — Contradiction collapse by automation.

These eight subordinate notes, taken together with this anchor, formalize Claim 2 as a Series A derivation subtree. The anchor states the paper-level claim; A1.03 supplies the operational decomposition; A2.13–A2.17 supply portable component variants and prior-art treatment; A3.08–A3.10 supply the architectural foils. No new architectural commitments are introduced in this tree; the tree formalizes a single Paper 1 commitment as a set of derivation nodes traceable back to §5 of the source paper.

## 7. Operational test for the parent claim

An anchor-level operational test for Claim 2, applicable to a substrate as a whole, is:

> *Can an observer with appropriate access find both sides of any preserved conflict in the substrate at any time, with provenance for each side and explicit relationship between them, and is there a recorded cell-level resolution outcome (when one exists) attributable to a human-authored rule?*

A substrate that satisfies this test instantiates Claim 2. A substrate that fails it fails on one or more of substrate-level preservation, provenance attachment to the conflict itself, relationship-as-addressable-content, or authority-over-resolution-logic. The test is anchor-level; finer-grained tests for the specific sub-commitments are the work of A1.03's operational test and the per-sub-commitment tests carried by A2.13–A2.17.

The test is symmetric to the operational test for the human-governance commitment in the foundational definition note: both are existence checks against the substrate's design properties at any moment of its existence, not against a particular workflow stage or audit interval.

## 8. Why this anchor matters

The Series A derivation tree on conflict preservation existed in prior derivation notes — A1.03 carries the foundational operational decomposition, A2.13–A2.17 carry component decompositions and prior-art treatment, A3.08–A3.10 carry the anti-pattern foils — but the paper-level claim from which all of those notes derive was not previously formalized as a named claim in its own right. This anchor closes that gap. It names the parent, states the commitment as a paper-level architectural property, identifies its two-level structure and its three anti-pattern foils, acknowledges the OIDA prior-art relationship explicitly, and maps the derivation tree below.

Subsequent work that adopts, extends, composes with, or argues against Paper 1's conflict-preservation commitment should reference this anchor as the parent claim and the subordinate notes for the operational decompositions. Work that uses "conflict preservation" or "first-class conflict" in a sense other than the one formalized in this anchor and its derived sub-commitments is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Conflict Preservation as Paper 1's Second Architectural Claim.* May 14, 2026. ORCID: 0009-0004-8065-3235.
