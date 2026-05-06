# Requirement B — Conflict Preservation Across Boundaries: Standalone Treatment of How Composition Preserves First-Class Conflict State Across Composing Systems in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, Requirement B of the composition-requirements specification — conflict preservation across boundaries — as a standalone architectural commitment that can be defended, implemented, and tested independently of the four sibling requirements.

## Abstract

The CKS source paper commits to conflict-as-first-class state at §3 (Claim 3) and §5, with substrate-level preservation at §5.1 and cell-level resolution under orchestration rules at §5.2. The paper's composition requirements at §13 include Requirement B: contradictions that span composing systems are preserved as first-class architectural state across the composition boundary. This note formalizes Requirement B as a standalone specification. It identifies the four operational components of the requirement (preservation of cross-substrate contradicting content, conflict relationships, conflict provenance, and resolution decisions); states what the requirement does not claim; distinguishes Requirement B from four adjacent cross-system conflict-handling patterns commonly conflated with it (eventual-consistency reconciliation, last-write-wins across systems, automatic data harmonization, integration-layer conflict suppression); names the downstream commitments the requirement is load-bearing for; enumerates ten failure modes; and supplies an operational test.

## 1. Why Requirement B needs to be formalized as standalone

The parent foundational note A1.13 commits to the five composition requirements as the architectural conditions any multi-substrate composition must satisfy to remain CKS-coherent. The integrating-frame note A2.75 named the five requirements at the composition level. The first specialization, A2.76, formalized Requirement A — per-substrate human governance preservation. This note formalizes Requirement B as having independent architectural content with particular weight on the cross-boundary conflict preservation that distinguishes it from cross-system data integration patterns commonly used in enterprise contexts.

The motivating cases are deployments where CKS substrates compose with systems that may produce contradicting content. A CKS substrate may compose with another team's CKS substrate where the two teams have different views of the same coordination object — different decisions about a shared resource, different characterizations of an ambiguous requirement, different rationales recorded in parallel. A CKS substrate may compose with an enterprise data system that contains contradicting state — the enterprise system asserts one decision while the CKS substrate records the team's contradicting decision. Multiple CKS substrates may compose where contradictions emerge naturally from independent coordination across time or teams. Each scenario requires the architectural commitment Requirement B names: preservation of contradicting state across the composition boundary, with the cross-boundary relationship and its provenance preserved as substrate content.

The connection to A1.03 and to Guarantee D per A2.60 is the second motivation. A1.03 commits to conflicts being preserved as first-class substrate state; Guarantee D commits to that preservation being deterministic within a substrate; Requirement B commits to preservation across composition boundaries. The three commitments compose: A1.03 specifies the foundational conflict commitment, Guarantee D its determinism within a substrate, Requirement B its preservation across compositions. Without Requirement B, A1.03 holds only inside individual substrates and breaks at every composition seam — the foundational commitment becomes scope-limited in a way the source paper does not authorize. Requirement B is the architectural condition that prevents composition itself from becoming a mechanism for conflict erasure.

## 2. The Requirement B commitment, defined precisely

The architectural commitment decomposes into four operational components.

**(a) Preservation of cross-substrate contradicting content.** When CKS substrate S1 composes with system S2 and S1's content contradicts S2's content, the contradicting content is preserved within each substrate. S1's content remains within S1 per A2.13 (substrate-level preservation). S2's content remains within S2 — per S2's own architectural commitments if S2 is itself CKS, or per the composition's information-exchange architecture if S2 is non-CKS, with the cross-boundary reference preserved within S1. Composition does not alter, mask, or remove either substrate's contradicting content as a side effect of being composed.

**(b) Preservation of cross-substrate conflict relationships.** The relationship between contradicting content across the boundary is preserved as substrate content within S1, and within S2 if S2 is also CKS. The relationship metadata per A2.16 — bidirectional reference, signed contradiction edge per A2.17, contradiction characterization — is preserved across the boundary, allowing the cross-substrate contradiction to be navigable from substrate reads per A2.25 Requirement 2. A reader of S1 can locate the cross-boundary contradiction through normal substrate-read operations; the relationship is not retrievable only through extra-substrate channels.

**(c) Preservation of cross-substrate conflict provenance.** The provenance per A2.16 attached to cross-boundary conflicts is preserved as substrate content: the conflict's writer attribution (who or what detected the contradiction), the timestamp (when the contradiction was observed), the antecedent references (what content in each substrate was contradicting), the rule reference (if a rule detected the contradiction), and the rationale (where applicable). The provenance is substrate-resident per A2.46 (Category 4 source-of-truth: substrate authoritative for "what rules apply") for the rule-reference component, and is addressable per Requirement C per A2.78 for the cross-boundary references that point at content in S2.

**(d) Preservation of cross-substrate resolution decisions.** When cross-boundary conflicts are resolved per A2.14 (cell-level resolution under orchestration rules), the resolution decisions are preserved as additional substrate content per Guarantee C per A2.59 — the resolution does not erase the original cross-boundary conflict per Guarantee D per A2.60. Resolution-without-erasure holds for cross-boundary conflicts on the same terms as for within-substrate conflicts: the cell that executes a resolution rule produces a new substrate write recording the resolution and its rule reference, layered over the contradiction, and the contradiction itself remains addressable.

The four components together define Requirement B architecturally. A composition that satisfies all four has Requirement B in the architectural sense; a composition that fails any one does not.

## 3. What Requirement B does NOT claim

The standalone treatment must be precise about scope so it is not overstated.

It does not claim that all cross-system data exchanges produce conflicts. Most exchanges produce coherent content; conflicts are specifically the cases where composing systems hold contradicting content for the same identified subject matter. The commitment is that *when* contradictions exist, they are preserved across boundaries.

It does not require composing systems to themselves preserve conflicts internally. Compositions with non-CKS systems are architecturally supported per A1.16; the commitment is that the CKS substrate preserves cross-boundary conflicts in its own substrate and provenance, while the composing system may have any internal conflict-handling model.

It does not foreclose cross-boundary resolution. Resolution decisions under human-authored orchestration rules per A2.14 may operate across boundaries; the commitment is that resolution does not erase the original conflict, not that resolution is forbidden.

It does not specify implementation patterns. Implementations may use cross-system reference tables, cross-boundary provenance records, distributed conflict logs, or other mechanisms; the four components must be operationally satisfied, but specific implementations are deployment choices.

It does not require all cross-boundary conflicts to be retained indefinitely. Deployments may have retention policies for conflict records; the commitment holds for the retention period the deployment specifies, and the retention policy itself is governed by humans authoring the substrate's rules.

It does not require cross-boundary conflicts to be visible regardless of authority. Visibility may be authority-scoped per A2.47; the commitment is that conflicts are preserved as substrate content with their relationship and provenance, not that they are universally visible regardless of what authority a particular reader holds.

## 4. What Requirement B is NOT

Four adjacent cross-system conflict-handling patterns are commonly conflated with Requirement B.

**Not eventual-consistency reconciliation across systems.** Eventual-consistency patterns — vector clocks, conflict-free replicated data types, last-write-wins reconciliation in distributed systems — reconcile contradicting state by selecting one value or merging values to produce a single converged result. Requirement B preserves contradictions as first-class state across boundaries; reconciliation that erases the contradiction violates the commitment regardless of the consistency model used.

**Not last-write-wins across systems.** LWW supersedes earlier writes across composing systems with the most recent write, deleting or marking superseded the earlier writes without reference to the contradiction they expressed. Requirement B preserves both contradicting writes with their cross-substrate relationship.

**Not automatic data harmonization.** Harmonization patterns — schema reconciliation, value translation, semantic mapping — transform composing systems' data to produce coherent unified state for downstream consumption. Requirement B preserves contradictions when they exist; harmonization that erases the contradiction by transformation violates the commitment regardless of operational utility.

**Not conflict suppression in integration layers.** Suppression patterns filter or hide conflicts from readers — dashboards displaying only one substrate's view, integration APIs selecting one source as authoritative, query layers presenting a single coherent answer assembled from contradicting underlying state. Requirement B keeps conflicts addressable through substrate reads; suppression that hides them from authorized readers violates the commitment, even where the underlying substrates retain the contradicting state.

The four patterns are architecturally distinguishable from Requirement B even where the operational behavior they produce is sometimes preferable for non-coordination workloads. Requirement B is also distinct from distributed-systems consistency models more broadly. CAP-theorem trade-offs, ACID across distributed transactions, and eventual-consistency models address how concurrent or distributed operations interact; Requirement B addresses how contradicting content is preserved across composing systems. The two concerns are orthogonal: a system may have strong distributed-consistency properties while violating Requirement B, or weak distributed-consistency properties while satisfying it.

## 5. Why Requirement B is load-bearing for downstream commitments

Requirement B is load-bearing for several CKS commitments. The integrating composition-requirements specification per A1.13 and A2.75 names Requirement B as one of five requirements; without cross-boundary conflict preservation, the architectural commitment to conflicts as first-class state per A1.03 is broken at composition boundaries. The conflict-as-first-class commitment per A1.03 and the conflict decomposition A2.13–A2.17 commit to first-class preservation at the substrate level; Requirement B extends the commitment to cross-substrate cases, without which A1.03 would hold only within single substrates.

The substrate-level conflict preservation per A2.13 and the cell-level resolution per A2.14 give within-substrate preservation and rule-governed resolution respectively; Requirement B extends both across boundaries, giving complete conflict-handling coverage with no scope between them where contradictions can be silently erased. The Category 3 source-of-truth commitment per A2.45 commits to substrate being authoritative for "what is in conflict"; Requirement B extends this authority to cross-substrate conflicts. Guarantee D (conflict states preserved) per A2.60 specifies determinism of conflict preservation within a substrate; Requirement B specifies the parallel preservation commitment across compositions, giving a determinism contract that holds at single-substrate scope and at composition scope. The path-retraceability commitment per A1.07 and Requirement C per A2.78 require paths reconstructible across boundaries; Requirement B's preservation of cross-substrate conflict relationships supports this by ensuring the conflict edges path reconstruction needs to traverse are themselves substrate-resident.

## 6. Failure modes that violate Requirement B

Each failure mode names a way an implementation can fail by reconciling, suppressing, or erasing cross-boundary conflicts.

*Cross-system reconciliation that erases conflicts.* The implementation operates substrate in eventually-consistent architecture across composing systems, with reconciliation that erases the original contradiction once convergence is reached; component (a) fails.

*Last-write-wins across composition boundaries.* The implementation uses LWW concurrency control across composing systems, with the most recent write superseding earlier writes regardless of substrate origin; cross-substrate preservation fails at the moment of supersession.

*Cross-substrate data harmonization.* The implementation applies harmonization transforms that erase contradictions by transforming composing systems' data to a unified representation; even if underlying substrates retain their original content, the composed view fails component (b).

*Integration-layer conflict suppression.* The implementation hides cross-boundary conflicts from readers in integration interfaces — dashboards, APIs, or query responses present a single substrate's view as authoritative without indicating cross-boundary contradictions exist; navigability per A2.25 Requirement 2 fails.

*Cross-boundary conflict-relationship stripping.* The implementation preserves contradicting content within each substrate but does not preserve the cross-substrate relationship — there is no addressable reference within S1 identifying the contradiction with content in S2; component (b) fails and the contradiction is implicit but not first-class.

*Cross-boundary conflict-provenance stripping.* The implementation preserves contradicting content but strips the cross-substrate provenance — no record of when the contradiction was detected, by what rule, or what the contradicting content references are; component (c) fails and the contradiction is recorded but unaccountable.

*Resolution-erases-cross-boundary-conflict.* The implementation records resolution decisions per A2.14 by overwriting the original cross-boundary conflict rather than recording resolution as additional substrate content per Guarantee C; component (d) fails — the resolution exists but the contradiction it resolved does not.

*Authority-shifting conflict resolution.* The implementation resolves cross-boundary conflicts by automatically selecting the composing system's value as authoritative regardless of which substrate has authority for the content category per A2.47; cross-boundary preservation fails because the resolution is neither human nor rule-governed.

*Composition-creates-implicit-conflict-resolution.* The implementation treats composition itself as resolving contradictions — the act of composing automatically resolves contradictions to S2's values, S1's values, or some composition-mechanism hybrid — and the conflict is erased by the act of composition with no rule a human authored governing the resolution.

*Cross-boundary-conflict archival without substrate reference.* The implementation archives cross-boundary conflicts to external systems while removing them from substrate; conflicts become retrievable only through external archives, and substrate reads no longer surface the contradiction.

## 7. Operational test

A composition satisfies Requirement B if and only if all of the following are true at all times during the composition's existence.

1. Cross-substrate contradicting content is preserved within each substrate per component (a) of section 2.

2. Cross-substrate conflict relationships are preserved as addressable substrate content per component (b), with the cross-boundary references navigable from standard substrate reads.

3. Cross-substrate conflict provenance per A2.16 is preserved per component (c), with writer attribution, timestamp, antecedent references, rule reference where applicable, and rationale where applicable all substrate-resident.

4. Cross-substrate resolution decisions per A2.14 are preserved as additional substrate content per component (d), without erasing the original cross-boundary conflict.

5. Cross-boundary conflicts are not reconciled, harmonized, or suppressed by composition-layer or integration-layer mechanisms, even where such mechanisms would produce a more easily consumed downstream view.

6. Cross-boundary conflicts are queryable through standard substrate read operations per A2.25 Requirement 2 and through substrate-only paths per A2.41, with the cross-boundary references being substrate-resident rather than reconstructible only through extra-substrate channels.

A composition that fails any of (1)–(6) does not satisfy Requirement B in the architectural sense, even if conflicts within each participating substrate appear individually preserved.

## 8. Why naming Requirement B as standalone matters

Implementations under pressure to integrate AI systems with enterprise infrastructure consistently drift toward cross-system reconciliation patterns that violate Requirement B. The drift is steady and not accidental. Reconciliation is operationally simpler — a single unified view is easier to present, consume, and display than two contradicting ones. Reconciliation is commercially familiar — enterprise integration architectures have spent decades harmonizing data across systems. Reconciliation is rhetorically appealing — audiences understand "we resolved the discrepancy" more easily than "we preserved the disagreement."

Implementations that drift away from Requirement B produce systems where composition becomes a conflict-erasure mechanism. The downstream consequences manifest as conflict-as-first-class commitment failure (A1.03 fails specifically at composition boundaries while continuing to appear satisfied at single-substrate scope), source-of-truth fragmentation (the Category 3 source-of-truth per A2.45 fails for cross-boundary conflicts because no substrate is authoritative for contradictions the composition has erased), retraceability failures (paths cannot be reconstructed across boundaries that have erased conflict context), and architectural-commitment failure at the foundational layer.

Naming Requirement B as a standalone architectural commitment — with the four operational components in §2, the limitations in §3, the four adjacent-pattern distinctions in §4, the load-bearing connections in §5, the ten failure modes in §6, and the six-part operational test in §7 — gives downstream readers a precise specification of what cross-boundary conflict preservation the architecture requires. Subsequent work that adopts the CKS pattern at composition scope, extends it to multi-substrate deployments, or composes it with adjacent AI components should treat Requirement B in the sense formalized here. Subsequent work that uses a weaker commitment is using a different architectural commitment, and the difference should be named.

The subsequent notes A2.78–A2.80 specialize Requirements C through E. Together with this Requirement B specification and the prior Requirement A specification at A2.76, they will close the decomposition of A1.13 begun by the integrating-frame note A2.75.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Requirement B — Conflict Preservation Across Boundaries: Standalone Treatment of How Composition Preserves First-Class Conflict State Across Composing Systems in CKS.* May 5, 2026. ORCID: 0009-0004-8065-3235.
