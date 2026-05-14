# Human-Governed Authority as Paper 1's Third Architectural Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to anchor — as a single named architectural claim — what the source paper commits to under the term *human-governed*, and to map the previously published sub-commitments that decompose this claim into derivation children with an explicit named parent.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern names six architectural commitments. This note formalizes the third of them as the **human-governed authority** claim: humans retain three rights — to inspect, to modify, and to override substrate content and orchestration rules — as a structural property of the system's design, available at any time during the substrate's existence, separable from any commitment about who or what performs the labor of maintaining the substrate. The claim's load-bearing architectural move is the separation of *authority* (what humans hold) from *labor* (what humans, LLMs, or stable cells may perform). The claim's temporal property — rights exercisable *at any time*, not only at scheduled checkpoints — is what distinguishes architectural governance from procedural governance promises. Together, these two properties rule out four anti-patterns: vendor-revocable governance, scheduled-review-window governance, workflow-approval-gated governance, and LLM-gatekept governance. This anchor states the claim precisely, names the load-bearing distinctions that make it operational, maps the sub-commitments (A1.01, A1.11, A2.01–A2.07, A2.57–A2.59, A3.01–A3.04) that decompose it, situates the claim against the prior two Phase A0 anchors, and gives a single-question operational test.

## 1. Why an anchor note for the human-governed authority claim is needed

The CKS pattern's six architectural commitments are stated across Paper 1's §2–§7 with varying degrees of consolidation. The human-governed commitment is the most distributed of the six: §2.1 names it as the substrate's defining adjective; §2.3 distinguishes it from human-curated and human-authored alternatives; §3.3 commits its temporal property and the authority-vs-labor disambiguation as a Kantara reviewer-attack response; §6.3 ties it to the cost contract by which governance does not scale with substrate size; §7.4 commits its accessibility as non-specialist governance; §11.3 ties it to the substrate-as-source-of-truth role within the determinism contract. A reader who works through the paper assembles the commitment from these pieces; the paper does not present a single landing site that names *human-governed authority* as one architectural claim with a definite list of sub-properties.

The previously published derivation notes — A1.01 on authority-not-labor, A1.11 on non-specialist governance, A2.01–A2.07 decomposing the three rights and the two moments, A2.57–A2.59 decomposing non-specialist governance, A3.01–A3.04 ruling out specific anti-patterns — already enumerate the commitment's architectural content at high resolution. What those notes did not have until this anchor is an explicit named parent at paper-claim level. This note serves that role and no other: it does not introduce new commitments; it gathers the previously defended ones under their proper named claim, states the load-bearing distinctions that make the claim operational, and makes the decomposition citable as such — giving downstream and cross-derivation work a paper-claim-level target distinct from any single sub-commitment.

## 2. The claim, stated precisely

In the CKS pattern, a substrate is **human-governed** if and only if humans retain the following three rights as a structural property of the system, available at any time during the substrate's existence:

1. **The right to inspect** any substrate content and any orchestration rule that governs cell-level behavior.
2. **The right to modify** any substrate content and any orchestration rule.
3. **The right to override** any operation, default, or LLM-produced output that touches substrate content or orchestration rules, without justification to the system or to a higher authority within the architecture.

The three rights together name what the term *governance* commits to. They apply over two scope objects: **substrate content** (the structured representations the substrate carries — entities, relationships, decisions, rationale, conflicts, provenance) and **orchestration rules** (the human-authored rules that determine how a cell behaves when it executes over substrate content).

Two properties of the rights are load-bearing for the claim and are stated explicitly. The commitment is **architectural**, not procedural: the rights must be available as a property of the system's design, not as a promise that depends on a particular vendor's policy, a particular workflow's configuration, or a particular runtime middleware layer's behavior. A system in which an LLM, a vendor, or any system component can in principle prevent a human from exercising any of the three rights is not human-governed in the CKS sense, regardless of how rarely such prevention occurs in practice. The commitment is also **temporal**: the rights are available *at any time*, not only at predetermined checkpoints. A system that grants inspection rights only during scheduled review windows, modification rights only inside approval-gated workflows, or override rights only with vendor or LLM sign-off, may satisfy other governance frameworks; it does not satisfy this claim.

These two properties, together with the three-rights structure, are what the human-governed authority claim consists of. Everything else this anchor formalizes is decomposition of or consequence from this content.

## 3. The authority-vs-labor distinction as the load-bearing move

The single architectural move that makes the human-governed authority claim coherent and scalable is the separation of *authority* from *labor*. The source paper makes this disambiguation explicitly in §2.3 and §3.3 and applies it across §6.3, §7.4, and §11.3. A1.01 already formalizes the distinction at sub-commitment level; this anchor names what A1.01 is a decomposition of.

**Authority** is what humans hold at all times: the three rights named in §2 above. Authority is not allocable. A system that delegates inspect, modify, or override authority to an LLM, a vendor, or a workflow component is no longer governed in the CKS sense, regardless of how the delegation is implemented.

**Labor** is what humans, LLMs, or stable cells may perform: the work of writing substrate content, populating it from raw inputs, maintaining it over time, drafting orchestration rules, and executing cells under those rules. Labor is allocable across three modes — direct human labor, LLM labor under orchestration rules, and stable-cell labor under stable rules. The architecture supports all three and requires none of them in particular. The labor allocation is a deployment decision; the authority structure is not.

This separation is what permits the human-governed authority claim to scale. Governance is exercised at two moments — orchestration-rule authoring (paid once per rule, amortized over every cell execution) and direct override (paid only when humans choose to intervene) — neither of which is proportional to substrate size. The claim is therefore compatible with substrates that grow large, because the governance cost is bounded by rule variety and intervention frequency rather than by substrate volume. Without the authority-vs-labor distinction, the claim collapses into one of two adjacent commitments — human-curated (a labor commitment about who maintains the substrate) or human-in-the-loop (a runtime pattern about who approves what passes through an automated process) — neither of which is the architectural property the CKS pattern requires.

## 4. The temporal property and the four anti-patterns it rules out

The temporal property — *at any time, not at scheduled checkpoints* — is the second load-bearing component of the human-governed authority claim, and the property that carries the rejection of the four anti-patterns the claim is most often confused with in practice.

**Anti-pattern 1 — Vendor-revocable governance.** A system in which a vendor can in principle restrict, gate, or revoke any of the three rights — by policy change, by tier-based feature limitation, by silent product update, or by service-level discretion — is not human-governed in the CKS sense. The architectural property cannot rest on vendor goodwill. A3.01 formalizes this anti-pattern.

**Anti-pattern 2 — Scheduled-review-window governance.** A system in which inspection, modification, or override rights are exercisable only during predetermined review windows — quarterly governance reviews, scheduled audit cycles, time-locked inspection portals — fails the temporal property even when the windows are frequent. Authority that can be exercised only when a calendar permits is not authority *at any time*. A3.02 formalizes this anti-pattern.

**Anti-pattern 3 — Workflow-approval-gated governance.** A system in which the modify or override rights require sign-off from an LLM, a workflow engine, a multi-step approval chain, or any other system component before taking effect on substrate state fails the architectural property. Override that requires the system's approval is not override; it is a request the system may grant or deny. A3.03 formalizes this anti-pattern.

**Anti-pattern 4 — LLM-gatekept governance.** A system in which the LLM controls what humans can read, modify, or override — by mediating substrate access exclusively through generated views, by deciding which content surfaces to which roles, by silently filtering or summarizing what is shown — places the LLM in an authority position the claim assigns to humans. The LLM may be present as a tool over the substrate (search, summarization, semantic navigation), but it cannot be the gate. A3.04 formalizes this anti-pattern.

These four anti-patterns are not exhaustive, but they cover the most common practical misimplementations. Each fails the claim along a distinct axis — vendor discretion, time-window restriction, workflow gating, and LLM mediation — and naming them precisely is what allows downstream implementations to be assessed against the claim rather than against a softer paraphrase of it.

## 5. Derived sub-commitments — the decomposition map

This anchor names the previously published sub-commitments that decompose the human-governed authority claim. The decomposition is structural: each sub-commitment formalizes independent operational content within the claim, with no overlap that would create double-counting and no gap that would leave part of the claim unstructured.

**A1.01 — Authority not labor.** The most foundational decomposition. Formalizes the authority-vs-labor distinction discussed in §3 above and establishes it as a sub-commitment in its own right rather than as a clarification.

**A2.01 — The inspect right as standalone.** Formalizes the inspect right with independent operational content, separable from modify and override. Establishes that oversight-only roles (auditors, compliance reviewers, regulatory inspectors, security reviewers) exercise real architectural authority rather than a derived or simulated form of it.

**A2.02 — The modify right as standalone.** Formalizes the modify right as having independent operational content covering authorized read-and-write authority over substrate content and orchestration rules, separable from inspect and override.

**A2.03 — The override right: no-justification-required.** Formalizes the override right with its distinctive architectural property: override actions do not require justification to the system or to a higher authority within the architecture. Override may be logged, audited, or socially reviewed; it is not architecturally gated.

**A2.04 — Orchestration rule authoring as governance.** Formalizes the first of the two moments at which governance is exercised: the authoring of orchestration rules by humans, paid once per rule and amortized over every cell execution that follows under that rule.

**A2.05 — Direct override as governance.** Formalizes the second moment at which governance is exercised: direct human modification or override at intervention time, paid only when humans choose to intervene.

**A2.06 — Architectural property vs. procedural promise.** Formalizes the architectural-vs-procedural distinction that makes the claim defensible against systems that promise the same behavior at the policy or workflow layer.

**A2.07 — Temporal property: at-any-time vs. scheduled.** Formalizes the temporal property as standalone operational content, distinguishing the claim from governance frameworks that schedule access to rights.

**A1.11 — Non-specialist governance, not non-specialist authorship.** Formalizes a consequence of the claim's exercisability in commodity tools: humans without specialist tooling expertise can exercise the three rights, even though authoring of substrate content or orchestration rules may require domain or technical expertise.

**A2.57–A2.59 — Non-specialist governance decomposed.** Formalize three operational facets: the affordances the host environment must provide for non-specialist rights exercise (A2.57); the boundary between governance authority and authorship expertise (A2.58); and the cost property under which non-specialist governance cost does not grow with substrate size (A2.59).

**A3.01–A3.04 — The four anti-patterns.** Formalize the four anti-patterns named in §4: vendor-revocable governance (A3.01), scheduled-review-window governance (A3.02), workflow-approval-gated governance (A3.03), and LLM-gatekept governance (A3.04).

The decomposition is closed in the sense that any operational question the claim raises — which rights, over what content, with what temporal availability, under what architectural vs. procedural guarantee, with what relationship to labor allocation, with what consequences for non-specialist exercisability, against which anti-patterns — has a formalized derivation note as its answer. The anchor's role is to name what those notes are decompositions *of*.

## 6. Relationship to the prior Phase A0 anchors

The human-governed authority claim does not stand alone within the CKS pattern. Two prior Phase A0 anchors establish architectural commitments that this claim presupposes.

**A0.01 — Hybrid commitment with substrate-LLM division at governance boundary.** A0.01 anchors the architectural commitment that there *is* a substrate as a distinct artifact from the LLM, with a governance boundary between them. Without this commitment, the human-governed authority claim has no object: the three rights are rights over substrate content and orchestration rules, and the substrate must exist as a separable architectural element for the rights to refer to anything. A0.01 establishes what; A0.03 (this note) establishes who holds authority over it.

**A0.02 — Conflict preservation as first-class architectural property.** A0.02 anchors the architectural commitment that conflicting states within the substrate are preserved as substrate content rather than auto-resolved by the LLM or by silent overwrite. Without conflict preservation, the override right would be operating over a substrate whose state had already been collapsed by automated reconciliation — the override would arrive after the architectural moment at which it could have effect. A0.02 establishes that the substrate holds the material an authority structure can act on; A0.03 establishes the authority structure that acts on it.

The three claims compose in a definite order. A0.01 commits the substrate exists; A0.02 commits its conflicting states are preserved for human authority to act on; A0.03 commits humans hold the three rights at all times to exercise that authority. Subsequent anchors (A0.04–A0.06) develop the pattern further but presuppose this three-anchor foundation.

## 7. Operational test and conclusion

The human-governed authority claim is exercised — and verifiable — moment by moment. A single-question operational test captures the architectural content:

> *Can a human with appropriate access exercise any of the three rights — inspect, modify, override — over any substrate content or any orchestration rule at this exact moment, without requesting permission from any system component (LLM, vendor, workflow gate, or runtime middleware)?*

A system that answers *yes* at any moment within the substrate's existence satisfies the claim at that moment. A system that answers *no* at any moment fails the claim at that moment, regardless of how it answers at other moments. The temporal property is what makes the question's *exact moment* clause necessary.

This anchor's contribution is not new architectural content; it is the explicit naming of the paper-level claim from which the previously published sub-commitments derive, the explicit decomposition map, and the explicit statement of the load-bearing distinctions — authority vs. labor, architectural vs. procedural, at-any-time vs. scheduled — that make the claim operational rather than rhetorical. Subsequent work that cites the human-governed commitment now has a paper-claim-level target distinct from any single sub-commitment, and the sub-commitments themselves now have an explicit named parent that locates them within the CKS pattern's broader claim structure.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Human-Governed Authority as Paper 1's Third Architectural Claim.* CKS Derivation Note #420 (Phase A0.03). May 14, 2026. ORCID: 0009-0004-8065-3235.
