# The Hybrid Commitment as Paper 1's First Architectural Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, at paper-claim level, the first of the six architectural commitments the source paper defends — the hybrid commitment, drawing the structural separation between the substrate layer and the LLM mediator at the governance boundary — and to map the Series A sub-commitments and operational variants that derive from it as a single decomposition tree.

## Abstract

The source paper defends six architectural commitments in turn (§2.1). The first, stated as "hybrid with a governance boundary," is the structural separation between the human-governed substrate and the LLM mediator that operates over it. It is the load-bearing architectural move from which the other five commitments inherit their referent. This note formalizes it as Paper 1's first architectural claim: states the commitment as three structural facts, names the two counterfactual designs the source paper argues against — *LLM-as-sovereign* and *human-as-operator-with-no-substrate* — maps the Series A sub-commitments (A1.01, A1.02, A1.04, A1.08, A1.10) and their A2.xx operational decompositions as derivations of this parent, and provides an operational test for whether a system instantiates it.

## 1. Why a paper-claim-level anchor is needed

The CKS source paper organizes its architectural content in two registers: the six-commitment summary at §2.1, where each commitment is stated without defense, and §§3–7 and §9, where six Claims defend the commitments. The two numberings do not align — §4 (Claim 2) is the principal defense of the hybrid commitment that §2.1 names as commitment 1 — so this note uses "Claim 1" in the Phase A0 anchor convention to refer to the first §2.1 commitment, and references defenses by section.

Phase A0 of the present derivation series anchors the §2.1 commitments as named architectural claims, so that the sub-commitments formalized in Phase A1 and the operational variants formalized in Phase A2 have an explicit named parent at paper level. Five Phase A1 notes — human-governed (A1.01), substrate-cell boundary (A1.02), AI-as-substrate-mediator (A1.04), substrate-as-source-of-truth (A1.08), and the determinism contract (A1.10) — each formalize one operational consequence of the hybrid commitment. What they did not yet have, before this anchor, was a named parent claim from which they collectively derive.

The other reason for the anchor is interpretive. "Hybrid" in current AI architecture vocabulary most often names a *capability-layer* hybrid: two processing strategies combined in one pipeline. The CKS hybrid commitment is a different claim — a *governance-layer* hybrid, drawing the boundary not between two processing capabilities but between two locations where authoritative state lives and who governs it. The anchor distinguishes the commitment from the capability-layer reading by stating what the hybrid is *structurally*, not what it does procedurally.

## 2. The hybrid commitment, stated precisely

The source paper states the commitment at §2.1 item 1 as the first of six architectural commitments. Stated as a paper-level claim:

> The Coordination Knowledge Substrate pattern is a structural hybrid between two architecturally distinct layers — a persistent, human-governed substrate and an LLM mediator operating over it — with the division between them drawn at the governance boundary, not the capability boundary. The substrate is the coordination medium and the source of authoritative state for coordination questions; the LLM is the mediating agent that reads from and writes to the substrate under human-authored orchestration rules and does not itself hold substrate-relevant state. Humans hold authority at the governance boundary over both layers.

The commitment fixes three architectural facts at once. Each is independent of the others.

**Fact 1 — Two layers, structurally separated.** The architecture is composed of exactly two layers at the coordination layer: a substrate (persistent, structured content humans can inspect and edit) and an LLM (a process that operates over the substrate when invoked). The two are not interchangeable processing components — one is state, the other is execution. A system that collapses them into a single layer — by putting substrate-relevant state inside the LLM, or by replacing the LLM with substrate-only execution — is not a CKS hybrid.

**Fact 2 — The division is drawn at the governance boundary, not the capability boundary.** The substrate handles what is *deterministic, human-governed, auditable* (§4.1); the LLM handles what is *high-dimensional and non-deterministic*. The division is not between what each layer is *capable of computing* but between what each layer is *authorized to be authoritative for*. Some operations the LLM is technically capable of — silently overwriting substrate content, resolving contradictions across sessions, maintaining authoritative coordination state in agent memory — fall on the substrate's side and are out of bounds regardless of capability. The boundary is an authority partition, not a competence partition.

**Fact 3 — Humans govern both layers at the governance boundary.** Human authority is exercised over the substrate directly (the rights to inspect, modify, override substrate content and orchestration rules) and over the LLM indirectly (through the orchestration rules the LLM is bound by, and through the preserved right to override any LLM-produced substrate write). The hybrid is not two independently-governed components in loose composition; it is two layers held under a single governance regime that draws the boundary between them.

The commitment is *architectural*: the three facts must hold as properties of the system's design, not as procedural promises that depend on a particular deployment, vendor, or workflow.

## 3. What the hybrid commitment is NOT — the two counterfactual designs

The source paper argues against two specific alternative designs the hybrid commitment forecloses. Naming them is what makes the commitment a substantive architectural claim rather than a stipulation.

**Counterfactual 1 — LLM-as-sovereign.** Authoritative coordination state lives inside the LLM — in agent memory, in long-context windows, in fine-tuned parameters, or in vendor-managed conversational state. Humans interact with the LLM as the authoritative interlocutor; any persistent store the LLM writes to is auxiliary, treated as cache or log rather than as source of truth. LLM-as-sovereign has one authoritative layer, not two, and that layer is the LLM. The source paper's §6.2 *context rot* framing names the failure mode this produces at coordination scope: substrate-relevant state held outside any substrate decays, drifts, and is lost at session boundaries. This counterfactual is what Fact 1 and Fact 2 jointly foreclose.

**Counterfactual 2 — Human-as-operator-with-no-substrate.** Humans use the LLM as a tool but maintain no substrate outside it. All coordination state lives in conversation transcripts, documents, tickets, chat logs, and ad-hoc prompts; the LLM has no persistent structured artifact to read from or write to, and humans coordinate by re-supplying context at each interaction. This is the dominant pattern in current LLM-mediated work (§1.1). There is still only one authoritative layer — the human's working memory, scattered across artifacts that do not compose. What this pattern cannot do is what the source paper claims for CKS: cross-session coordination, conflict preservation as substrate state, role-and-authority structure at the cell level, and audit-bearing decision records the system stands behind. This counterfactual is what Fact 1 forecloses by requiring a substrate to exist as a distinct architectural layer, and what Fact 3 reinforces by locating governance at a boundary that requires both sides to be present.

The hybrid commitment is the architectural posture that *neither* alternative is. Both layers must exist; both must be governed; the division must be drawn at the governance boundary; and humans must hold authority at that boundary over both sides. A system that fails any one of these conditions is one of the two counterfactuals, not a CKS hybrid.

## 4. The architectural consequence — why the hybrid commitment is *first*

Three consequences follow directly from the hybrid commitment, and each is the precondition for one or more of the other §2.1 commitments.

**Consequence 1 — Substrate-attached governance becomes coherent.** Because the substrate exists as a distinct architectural object, the human-governed commitment (§2.1 item 3) has a coherent attachment point: humans govern the substrate. Without the hybrid commitment, "human-governed" would have to attach to "the system" — a category that includes the LLM, the runtime, the vendor, the orchestration layer, and the deployment environment, no one of which is naturally subject to the three rights the human-governed commitment names.

**Consequence 2 — The LLM's mediator role becomes exercisable.** Because the substrate is the authoritative artifact and the LLM operates over it, the AI-as-substrate-mediator commitment (§2.1 item 4) has structural content. Without the hybrid commitment, "mediator" has no architectural referent — there is nothing for the LLM to mediate *between*, because either there is no substrate (counterfactual 2) or the LLM is itself the substrate (counterfactual 1).

**Consequence 3 — Conflicts can be preserved as state rather than reasoned over as inference traces.** Because the substrate holds persistent structured content separately from the LLM's reasoning, conflicts have a place to live as first-class addressable objects (§2.1 item 2). Without the hybrid commitment, conflicts can only be reasoned over within the LLM's inference — detected, resolved, or forgotten as the §5 *detect-resolve-forget* foil describes.

Tool-agnosticism (§2.1 item 5) and linear-cost composition (§2.1 item 6) are also downstream: the first specifies what a host must satisfy *to provide a substrate*; the second specifies the cost profile *of substrate growth*. Both presuppose a substrate as their architectural referent. The hybrid commitment is the primitive on which the other five §2.1 commitments depend for coherence — which is why it earns its own claim-level anchor as the first commitment.

## 5. Derived sub-commitments — the Series A decomposition tree

Phase A1 decomposes the hybrid commitment into five foundational sub-commitments, each formalized as an independently citable architectural property. Phase A2 further decomposes each into operational variants. The decomposition tree is mapped below, keyed to the three structural facts named in §2.

**A1.01 — Human-governed (authority, not labor).** Derives from Fact 3. Formalizes the three rights (inspect, modify, override) humans retain over substrate content and orchestration rules at all times, and distinguishes governance (authority) from authoring, curation, maintenance (labor). A1.01 propagates into A2.01–A2.07 (inspect-right, modify-right, override-right, design-time rule authoring, intervention-time direct override, non-specialist governance, labor allocation).

**A1.02 — Substrate-cell boundary.** Derives from Fact 1. Formalizes the substrate as the state layer and the cell as the execution layer, names what each commits to, and identifies what crosses the boundary in each direction. A1.02 propagates into A2.08–A2.12 (substrate-as-state-only, cell-as-execution-only, cell-writes-recorded-with-attribution, substrate-at-rest as inspectable, the rule against cell-internal persistent state).

**A1.04 — AI as substrate mediator.** Derives from Fact 2 and Fact 1. Formalizes the LLM's role with five severable properties: substrate-content reads as primary state, substrate-content writes under orchestration rules, no substrate-relevant state outside the substrate, no authority over substrate content, and LLM writes recorded as substrate content with attribution. A1.04 propagates into A2.18–A2.23, decomposing each property as independently testable.

**A1.08 — Substrate as source of truth.** Derives from Fact 1 and Fact 2. Formalizes the substrate as the authoritative answer to coordination questions — what was decided, by whom, under what authority, with what rationale, where contradictions remain — scoped specifically to coordination state. A1.08 propagates into A2.41–A2.43 (the categories the substrate is authoritative for, the categories that may legitimately live outside, the failure modes that violate the commitment).

**A1.10 — Determinism contract.** Derives from Fact 1 and Fact 2 as the consequence of treating the substrate as the deterministic side of the governance boundary. Formalizes the five guarantees a CKS-coherent substrate satisfies at all times — same-state-same-read, same-state-same-rule-equivalent-behavior, addressability of state changes, conflict preservation under non-resolution, substrate as source of truth — and excludes LLM outputs from the contract's scope. A1.10 propagates into A2.49–A2.56 (per-guarantee variants, the two-layer scope distinction, permitted non-determinism, named anti-patterns).

The decomposition tree therefore reads:

```
A0.01 — Claim 1 (the hybrid commitment)
├── A1.01 — human-governed (authority, not labor)   [Fact 3]
│   └── A2.01–A2.07
├── A1.02 — substrate-cell boundary                 [Fact 1]
│   └── A2.08–A2.12
├── A1.04 — AI as substrate mediator                [Fact 1 + Fact 2]
│   └── A2.18–A2.23
├── A1.08 — substrate as source of truth            [Fact 1 + Fact 2]
│   └── A2.41–A2.43
└── A1.10 — determinism contract                    [Fact 1 + Fact 2]
    └── A2.49–A2.56
```

The five A1.xx commitments are independent — a system can satisfy any subset and fail others — and Claim 1 coherence requires all five together. The A2.xx variants introduce no architectural content beyond what their parents commit to.

## 6. Operational test

A system instantiates the hybrid commitment if and only if all of the following are true at every moment during the system's existence:

1. **An observer can identify, at any point in time, which architectural layer holds the authoritative state for any given coordination question.** The answer must be "the substrate" for the §11.3 scope — what was decided, by whom, under what authority, with what rationale, and where contradictions remain. If the answer is "the LLM," "the agent's memory," or "depends on which session you ask," the system fails the test.

2. **The substrate layer and the LLM layer are structurally distinct.** The substrate must be inspectable and modifiable by humans independently of any LLM operation; the LLM must operate over the substrate's content rather than carrying authoritative coordination state of its own. A system whose "substrate" is in fact the LLM's context window, or whose "LLM" is a deterministic rule engine over substrate state, fails the structural-distinctness condition.

3. **The division between the two layers is drawn at the governance boundary.** Operations that touch authoritative coordination state — substrate content, orchestration rules, conflict resolution, decision provenance — sit on the substrate side; operations that exercise high-dimensional non-deterministic reasoning sit on the LLM side. A system that authorizes the LLM to silently overwrite substrate content, modify orchestration rules, or resolve preserved conflicts outside human-authored rules fails this condition regardless of how cleanly the two layers are structurally separated.

4. **Humans hold authority at the governance boundary over both layers.** The three rights — inspect, modify, override — must be available over substrate content and orchestration rules at all times. A system in which an LLM, a vendor, or a runtime middleware layer can in principle prevent a human from exercising these rights fails this condition regardless of how rarely the prevention occurs in practice.

The four conditions are independent. The hybrid commitment requires all four together. A system that fails any of (1)–(4) may be a useful system, and may be a hybrid in some other sense, but is not a CKS hybrid as the source paper commits to the term.

## 7. Conclusion

The hybrid commitment is Paper 1's first architectural claim and the load-bearing structural move from which the other five §2.1 commitments derive. It names a governance-layer hybrid, not a capability-layer one: two layers, structurally separated, with the division drawn at the governance boundary and humans holding authority on both sides. It defends against two counterfactual designs — *LLM-as-sovereign* and *human-as-operator-with-no-substrate* — by foreclosing the architectural patterns each rests on. The Series A sub-commitments A1.01, A1.02, A1.04, A1.08, and A1.10 decompose this parent claim into independently citable architectural properties; their A2.xx operational variants decompose each in turn. Subsequent work that uses "the hybrid commitment" in a different sense is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Hybrid Commitment as Paper 1's First Architectural Claim.* May 14, 2026. ORCID: 0009-0004-8065-3235.
