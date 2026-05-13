# Specification Integrity Collapse — The Cross-Cutting Anti-Pattern Where DNA Specifications Become Internally Inconsistent Through Accumulated Directed Selection Without Coherence Reviews, Violating A1.08 Substrate-as-Source-of-Truth, A1.03 Conflict-as-First-Class, and A1.10 Determinism, Closing Phase B3

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

This note is the thirtieth and final note in Phase B3 of the CKS derivation series. It formalizes Specification Integrity Collapse as a cross-cutting anti-pattern and closes the Phase B3 anti-pattern catalog.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern designates the DNA layer — the collection of orchestration substrates, behavior substrates, schemas, and rules that constitute a Self's instinct layer — as a substrate under human governance. This designation carries a foundational authority claim: DNA content is the source of truth for cell-level behavioral specification. Specification Integrity Collapse names the cross-cutting failure mode in which that authority claim degrades from within. Each individual modification to the DNA specification is locally authorized under directed selection (B1.14) and individually coherent; but no governance process reviews cumulative coherence across modifications. Over time, independently authorized rules contradict each other, the specification grows beyond the governance capacity of the humans holding modify authority (A2.02), and directed selection verification (B2.72) catches authorization failures without ever catching coherence failures. The result is a DNA specification that is simultaneously governed in the narrow sense — each change was approved — and ungovernable in the substantive sense — no human or governance process can assert that the specification as a whole is consistent, authoritative, or safe to modify. This note names three recognizable sub-forms of the collapse, distinguishes the anti-pattern from Ungoverned DNA Modification (B3.15), characterizes the emergence conditions and operational consequences, and specifies detection and remediation paths. It closes Phase B3.

## 1. The Authority Claim at Stake

The DNA layer's authority claim is foundational to the CKS Self architecture. Paper 2's instinct/reasoning separation places stabilized orchestration and behavior specifications in the DNA layer precisely because doing so makes those specifications persistent, inspectable, modifiable, and authoritative: whatever the DNA layer says about how a cell should behave is what governs that behavior. This is the substrate-as-source-of-truth commitment (A1.08) applied to behavioral specification. The commitment does not merely require that DNA content be human-readable; it requires that DNA content be internally consistent enough to be authoritative — that when the substrate says a cell should do X under condition C, there is no other rule in the same substrate saying it should do Y under condition C.

The determinism contract (A1.10) makes the same requirement from the behavioral side: given the same substrate state and the same input, cell behavior should be predictable. Predictability under the determinism contract is not a guarantee about LLM output variance; it is a guarantee about rule-level consistency. If the DNA specification contains contradictory rules, the determinism contract is violated at the specification level before any LLM inference occurs.

Specification Integrity Collapse is the failure mode in which the DNA layer accumulates contradictions, bloat, or coherence gaps through individually authorized modifications, degrading both the source-of-truth authority claim and the determinism contract. It is cross-cutting because it does not violate a single commitment in isolation; it degrades the substrate's foundational capacity to hold any commitment reliably.

## 2. Commitments Violated

Specification Integrity Collapse is cross-cutting across six commitments:

**B1.14 — Directed selection.** Each directed selection event is individually authorized and recorded, but cumulative coherence across events is not reviewed. The directed selection mechanism functions correctly at the event level and fails at the specification level.

**A1.08 — Substrate-as-source-of-truth.** When the DNA specification contains contradictory rules, no rule can be fully authoritative for the input domain where the contradiction applies. The substrate cannot serve as source of truth for behavioral specification when the specification disagrees with itself.

**A1.03 — Conflict as first-class object.** The conflict registration mechanism (B2.108) applies to conflicts between cells and between substrate content objects. Specification Integrity Collapse introduces a structurally similar problem at the rule level: DNA rules that conflict with each other are not registered as first-class conflicts. They accumulate silently, unregistered and unresolved.

**A1.10 — The determinism contract.** Contradictory DNA rules produce non-deterministic behavior: the same input may produce different outputs at different invocations, depending on evaluation order among conflicting rules. This violates the representation-level determinism the contract requires.

**B2.68 — DNA modification governance.** DNA modification governance is the architectural requirement that modifications to the DNA layer occur through governed processes. Specification Integrity Collapse does not bypass this requirement; it satisfies it narrowly while violating its purpose. The governance process reviews individual modifications without reviewing the cumulative specification, and so cannot catch coherence degradation.

**B2.72 — Directed selection verification.** Directed selection verification confirms that a proposed change is authorized, recorded, and traceable. It does not, in the absence of an explicit coherence dimension, confirm that the proposed change is coherent with the existing specification. Specification Integrity Collapse is the systematic consequence of this gap across many verification events.

## 3. Recognizable Form

Specification Integrity Collapse presents in three sub-forms, which may appear independently or in combination.

**Form 1 — Accumulated Contradiction.** The DNA specification has grown through many directed selection events (B1.14). Each individual modification was locally authorized and locally coherent at the time of authorization. No governance review examined the cumulative effect. Over time, rules added at different periods — often by different governance participants, addressing different operational concerns — now produce contradictory behavioral specifications for overlapping input types.

Recognition signals: the A1.03 conflict registry at cell scope (B2.108) is populated with rule conflicts that were never registered as first-class because they were introduced incrementally, each modification appearing non-conflicting when reviewed in isolation; the A5.06 determinism test fails because the same input under the same DNA produces different outputs depending on which conflicting rule prevails; governance cannot answer the question "for input type X, what does the specification require?" with a single authoritative response.

**Form 2 — Specification Bloat.** The DNA specification has accumulated rules through directed selection to the point where the specification is too large and complex for governance to meaningfully inspect or govern. The specification has grown beyond the governance capacity of the humans holding A2.02 modify authority. The A2.01 inspect right is nominally exercisable — the humans can open the specification and read it — but inspection no longer produces comprehensible output at the whole-specification level.

Recognition signals: DNA volume has grown orders of magnitude beyond initial specification scale; directed selection under B1.14 has become operationally risky because modifying any rule may have unintended interactions with accumulated rules that no governance participant can enumerate in advance; governance decisions are made without full understanding of the specification's content or its interaction structure; the practical effect is that directed selection velocity decreases toward zero as governance participants recognize they cannot safely authorize modifications.

**Form 3 — Coherence-Unchecked Evolution.** Each directed selection event is reviewed in isolation. The governance process confirms that the proposed change is authorized, that the proposed rule is locally well-formed, and that the change is recorded with appropriate provenance metadata (A1.07). No governance process reviews whether the new rule is coherent with the entire existing specification. Coherence degradation is systematic because governance is scoped to individual changes rather than to cumulative coherence.

Recognition signals: B2.72 directed selection verification has no coherence dimension — it verifies authorization and recording but not coherence; directed selection events (A2.40) show frequent modifications but no coherence review records exist in the substrate; the A1.03 conflict count in DNA rules increases monotonically as a function of directed selection frequency without any coherence review frequency providing a countervailing mechanism.

## 4. Distinction from B3.15 Ungoverned DNA Modification

B3.15 (Ungoverned DNA Modification) covers DNA modifications that bypass governance authorization: changes made to the DNA layer without directed selection authorization, without recording, or outside the governance process. The violation in B3.15 is at the event level — the modification itself was not governed.

Specification Integrity Collapse covers a structurally different failure. Every individual modification is governed. The authorization record is complete. The directed selection mechanism was followed. The failure is not at the event level but at the specification level: governance reviewed each change without ever reviewing whether changes collectively produced a coherent specification. This distinction matters for remediation. B3.15 is remediated by closing the authorization gap — ensuring all modifications go through governance. Specification Integrity Collapse is remediated by adding a coherence governance activity that did not exist and was not required by the existing governance process.

A substrate that has never experienced B3.15 — every modification fully authorized and recorded — can nonetheless exhibit advanced Specification Integrity Collapse. Proper authorization of each change is necessary but not sufficient for specification integrity.

## 5. Emergence Conditions

Three conditions, individually or in combination, produce Specification Integrity Collapse.

**Incremental modification culture.** Governance develops a practice of reviewing each proposed DNA change on its own merits: "this rule is locally correct; approve." The practice produces correct governance decisions at the event level. It does not produce correct governance outcomes at the specification level, because a sequence of locally correct decisions can produce a globally inconsistent specification. The culture reinforces itself: early modifications are small enough that coherence degradation is not visible; by the time degradation is visible, the pattern is entrenched.

**Coherence review absent.** No governance process conducts periodic specification coherence reviews. Coherence is implicitly assumed to be maintained by individual-change review, which is a structural assumption that fails as specification complexity grows. The absence of coherence review is not experienced as a gap until the consequences appear; by then, significant accumulation has already occurred.

**Specification scale underestimated.** The initial deployment specification is small enough that coherence can be maintained by governance participants who hold the whole specification in working memory. As the deployment evolves through hundreds of directed selection events over months or years, specification scale grows in ways that were not anticipated at deployment design time. Governance processes calibrated to the initial scale do not scale with the specification.

## 6. Operational Consequences

**Determinism failure.** Conflicting DNA rules under Form 1 produce non-deterministic behavior that violates A1.10. The same inputs produce different outputs at different invocations depending on which conflicting rule prevails in evaluation order. This failure is particularly difficult to diagnose because it manifests as inconsistent cell behavior rather than as a visible error — the cell produces outputs, just not the same ones.

**Substrate authority degraded.** A1.08's substrate-as-source-of-truth requires that substrate content is authoritative. When the substrate contains contradictions, it cannot be fully authoritative for the domains where contradictions apply. The question "which rule is authoritative when two conflict?" has no answer within the specification itself, because the specification contains both rules and no meta-rule for resolving the conflict. The substrate becomes advisory rather than authoritative in practice, even as it nominally retains the source-of-truth designation.

**Governance paralysis.** Specification bloat under Form 2 makes governance unable to safely modify DNA. The risk of unintended interactions between a proposed new rule and accumulated existing rules is not assessable when the specification is too large to inspect comprehensively. Governance participants rationally become reluctant to authorize changes, and directed selection velocity decreases toward operational paralysis.

**Audit complexity unmanageable.** Compliance audit of a bloated, contradictory specification requires governance effort that scales with specification size and contradiction count. Audit that was straightforward at initial scale becomes unmanageable as both dimensions grow. Path retraceability (A1.07) is preserved at the individual change level, but the audit question "does this specification correctly implement the intended governance policy?" cannot be answered without coherence-level review.

**Evolution quality degrades.** Action-feedback proposals (B2.76) that propose DNA changes based on observed operational patterns may conflict with accumulated contradictory rules in ways that are not visible to the proposal process. As specification integrity decreases, the quality of directed selection decisions decreases with it, because those decisions are made against an incomplete or internally inconsistent picture of the specification.

## 7. Detection

**A5.06 determinism test.** Does the same input under the same DNA specification produce the same output across repeated invocations? Failure indicates either non-deterministic LLM behavior (permitted under the determinism contract's allowed non-determinism categories) or conflicting DNA rules (a Form 1 signal). Distinguishing these two sources of output variance is the first diagnostic step.

**A1.03 conflict registry.** Are DNA rule conflicts registered as first-class conflicts? A conflict registry that grows monotonically without corresponding directed selection events to resolve registered conflicts indicates Form 1 accumulation. A conflict registry that has never been populated for a mature specification indicates either that no conflicts exist or that the coherence-unchecked evolution of Form 3 is producing conflicts that are not being registered.

**DNA coherence audit.** Does the complete DNA specification contain rules that produce contradictory behavioral specifications for overlapping input domains? This audit is the direct detection mechanism for Form 1 and requires a governance activity — full-specification coherence review — that is distinct from individual-change review.

**B2.72 directed selection verification.** Does the verification process for proposed DNA modifications include a coherence dimension? Verification processes that confirm authorization and recording but include no coherence check against the existing specification are structurally producing Form 3 at every directed selection event.

**Specification size monitoring.** Has DNA volume grown disproportionately relative to the operational scope the specification governs? Specification volume that is orders of magnitude larger than the initial deployment specification, without corresponding expansion of the operational scope, is a Form 2 signal.

## 8. Remediation

**Establish periodic specification coherence review.** The foundational remediation is structural: add a governance activity that reviews the complete DNA specification for internal consistency at intervals calibrated to directed selection frequency. This activity is distinct from individual-change review and must be explicitly resourced. The coherence review should produce a coherence status record in the substrate, providing a dated and attributed record of specification integrity at review time.

**For accumulated contradiction (Form 1).** Identify conflicting rule pairs through coherence audit. Resolve each conflict through directed selection (B1.14): authorized modification to remove the contradiction, with full provenance recording. Register existing conflicts that cannot be immediately resolved in the A1.03 conflict registry (B2.108), making them first-class governed objects. The conflict registry is the appropriate home for DNA rule conflicts that are known but not yet resolved, just as it is the appropriate home for conflicts between cells.

**For specification bloat (Form 2).** Conduct specification rationalization: a governance-led review to identify and remove redundant rules, consolidate overlapping rules, and simplify the specification without changing its substantive behavioral requirements. Specification rationalization requires governance authority (A2.02 modify authority) and should be treated as a directed selection event with full provenance recording. The goal is to restore the specification to a scale that governance participants can comprehend and safely modify.

**For coherence-unchecked evolution (Form 3).** Add a coherence dimension to B2.72 directed selection verification. Each proposed directed selection event requires, as part of verification, a check confirming that the proposed new rule does not produce contradictory behavioral specifications when evaluated against the existing specification. This is the most technically demanding remediation for complex specifications, as it requires automated coherence checking infrastructure or governance discipline sufficient to perform the check manually. For large specifications, automated rule consistency checking may be a necessary precondition for coherence-checked directed selection to be operationally sustainable.

## 9. Phase B3 Closure

This note, B3.30, is the final note in Phase B3 of the CKS derivation series. Phase B3 comprises thirty notes:

- **B3.01** — The integrating frame establishing the Phase B3 anti-pattern catalog structure and the seven-element format (name, commitments violated, recognizable form, emergence conditions, operational consequences, detection, remediation).
- **B3.02–B3.21** — Twenty primary anti-patterns, one per B1.01–B1.20 foundational commitment, each formalizing the failure mode that results when a specific Paper 2 architectural commitment is violated.
- **B3.22–B3.30** — Nine cross-cutting anti-patterns, each addressing a failure mode that cuts across multiple commitments and cannot be assigned to a single parent commitment without loss of structural accuracy.

Specification Integrity Collapse closes the Phase B3 catalog as its ninth cross-cutting anti-pattern because it represents a failure mode of a distinctive kind: not the violation of a specific commitment, but the systematic erosion of the substrate's foundational capacity to hold any commitment reliably. A specification that is internally contradictory is not merely wrong about specific rules; it is unable to be authoritative, deterministic, or governable in the full CKS sense. Placing this anti-pattern last in Phase B3 reflects its structural position: the substrate's authority claim is what makes every other commitment in the catalog meaningful, and Specification Integrity Collapse is the failure mode that undermines that claim from within.

**Phase B4 — Composition Pairs** follows Phase B3. Phase B4 formalizes the interaction between two specific Paper 2 commitments, producing a catalog of approximately forty notes that address the architectural consequences of commitment composition: what the simultaneous satisfaction or violation of two commitments produces that the individual commitments do not predict in isolation.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Specification Integrity Collapse — The Cross-Cutting Anti-Pattern Where DNA Specifications Become Internally Inconsistent Through Accumulated Directed Selection Without Coherence Reviews, Violating A1.08 Substrate-as-Source-of-Truth, A1.03 Conflict-as-First-Class, and A1.10 Determinism, Closing Phase B3.* May 12, 2026. ORCID: 0009-0004-8065-3235.
