# Selective Merge Mating Pattern — Decomposing B1.10 Mating as Cross-Layer Combination by Formalizing the Selective Merge Pattern Where Governance-Authored Selection Rules per A2.04 Specify Which DNA Elements from Each Parent Source Are Included in Offspring DNA, Enabling Targeted Combination with Reduced Conflict Risk Compared to Union per B2.46

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

B1.10 establishes mating as a governed primitive for combining parental content across the DNA and action layers of CKS cells at every composition level. Paper 2 specifies three mating pattern variants; B2.45 stated the mating mechanism operational specification and B2.46 formalized the Union pattern. This note formalizes the Selective Merge mating pattern — the second of three variants — as the targeted combination pattern. In Selective Merge, governance-authored selection rules per A2.04 specify which DNA elements from each parent source are included in offspring DNA; not all elements cross the combination boundary. Selection rules are substrate-resident authoritative content per A2.46, authored and held under the same governance commitment that governs all substrate content. Offspring DNA is the selected subset from parent A plus the selected subset from parent B — a deliberately designed result rather than a full union of parental content. Selective Merge reduces conflict risk compared to Union because selection rules can deliberately exclude elements that would conflict; any conflicts that do survive selection are preserved as first-class substrate state per A1.03. Selective Merge has no direct biological analog: biological mating transmits whole genomes, and selective breeding selects which organisms reproduce rather than which elements cross. The architectural substance of Selective Merge is element-level combination under explicit governance — a combination structure available in no prior AI architecture at element granularity.

---

## 1. Why Selective Merge needs to be formalized as a standalone operational variant

B1.10 commits to mating as a governed primitive for cross-layer content combination. Paper 2 specifies three pattern variants — Union, Selective Merge, and Lineage-preserved union — each with distinct architectural commitments about what crosses the boundary from parent to offspring. B2.45 stated the mating mechanism operational specification. B2.46 formalized Union as the inclusive combination pattern, where all elements from both parents are included and all merge-time conflicts are preserved as first-class substrate state. Selective Merge is the second pattern and warrants independent formalization because it makes different architectural commitments from Union across every dimension that governs the combination result: what is included, how inclusion is decided, what conflict risk attaches, and what kind of offspring DNA results.

The standalone-formalization rationale is directly strategic. The territory at stake is element-level governed combination under selection rules. A party seeking to claim this territory as novel invention would need to show that no prior publication has named selection rules, per A2.04, as the mechanism specifying which elements from each parent source cross into offspring DNA under governance authority. This note establishes that publication. B2.47 is the forty-seventh Phase B2 note and the third of six notes decomposing B1.10 — following B2.45 and B2.46, preceding B2.48 (Lineage-preserved union), B2.49 (mating governance and lineage establishment), and B2.50 (mating verification). The six notes together close the B1.10 decomposition before Phase B2 turns to the B1.11 death decomposition beginning at B2.51.

---

## 2. The architectural pattern precisely stated

**Definition.** The Selective Merge mating pattern is the second of three mating pattern variants per B1.10. In Selective Merge, specific DNA elements from each parent source are selected for inclusion in offspring DNA by governance-authored selection rules per A2.04. Not all elements are included. Selection rules specify which elements cross from parent A and which cross from parent B. The offspring's DNA is the selected subset from parent A plus the selected subset from parent B — and nothing more.

**Selection rules.** Selection rules are substrate-resident authoritative content per A2.46. They are authored under the same governance commitment that governs all orchestration rules — per A2.04, rule authoring is itself a governance act. Selection rules may operate at any of three specification granularities:

- *Element-specific*: include element X from parent A, include element Y from parent B, identified by element identifier.
- *Type-specific*: include all elements of type T (for example, all schema elements, all conflict-handling rules, all invocation patterns) from a designated parent source.
- *Function-specific*: include all elements serving function F (for example, all domain-knowledge elements, all process-optimization elements) from a designated parent source.

Rules at each granularity are authored, held in substrate, and inspectable. Selection is never implicit; the rules that determine what crosses the boundary must be explicitly authored per A2.04 as substrate-resident authoritative content before a Selective Merge mating event proceeds.

**Offspring DNA structure.** The offspring receives the selected subset from parent A and the selected subset from parent B. Offspring DNA size and content depend entirely on the selection rules applied. Where Union produces offspring DNA that is the full union of both parents' DNA (subject to conflict preservation), Selective Merge produces offspring DNA whose scope is governably constrained. The offspring's capabilities are deliberately designed through selection rule authoring rather than being the maximal combination of both parents.

**Conflict handling per A1.03.** Selective Merge reduces conflict risk compared to Union because selection rules can deliberately exclude elements that would conflict with elements already selected from the other parent. A governance-authored selection rule may specifically exclude element X from parent A because element X conflicts with element Y selected from parent B, and the selection rule authors have determined that the conflict should not propagate into offspring DNA. This is the primary architectural mechanism by which Selective Merge reduces conflict risk.

However, conflict reduction is not conflict elimination. If selected elements from parent A and selected elements from parent B conflict — either because the conflict was not foreseen in rule authoring or because both conflicting elements were deliberately selected — the conflict is preserved as first-class substrate state per A1.03. Selective Merge does not auto-resolve remaining conflicts. A1.03's commitment holds for whatever conflicts survive selection: they are persistent, addressable substrate state, not merge-time markers that must be resolved before the mating event completes.

**Governance authorization.** Selective Merge, like all mating operations, requires governance authorization per B2.41. The authorization covers both the mating event itself and the selection rules that govern it. Cross-partner Selective Merge per A2.47 requires cross-partner authority.

**Offspring birth.** Selective Merge produces an offspring specification. Birth per B1.09 and birth verification per B2.44 apply. Offspring lineage references both parent lineages per B2.43.

**Provenance recording per A2.40.** Selective Merge mating events record all six provenance metadata fields: parent sources, selection rules applied, selected elements, resulting offspring specification, governance authorization, and timestamp. The selection rules applied are themselves substrate content and remain inspectable after the mating event completes.

---

## 3. What makes Selective Merge architecturally distinctive

Three properties together constitute the architectural distinctiveness of the Selective Merge pattern.

**Element-level governed combination.** Conventional AI architectures do not combine components at element granularity under selection rules. They may version components, replace modules, or compose pipelines — but none of these operations targets specific elements within a component for cross-source combination under governance-authored rules. Selective Merge introduces element-level combination as a governed architectural primitive. The granularity of the selection and the governance of the rules are both novel; neither appears individually in prior AI architecture, and their conjunction has no prior architectural name.

**Purposeful offspring design.** Because selection rules specify which elements appear in offspring DNA, the offspring's capabilities are a design product rather than an inheritance product. A governance actor who authors selection rules for a Selective Merge event is, in effect, specifying what the offspring can do — which domain knowledge elements it carries, which process rules it applies, which conflict-handling logic it inherits. This is a qualitatively different relationship between governance and offspring capability than Union provides. Union offspring capabilities are the union of both parents' capabilities (less any capabilities disabled by unresolved conflicts); Selective Merge offspring capabilities are exactly what the selection rules prescribe.

**Governable conflict risk.** The ability to author selection rules that deliberately exclude conflicting elements before combination makes conflict risk itself a governed property of the mating event. Governance actors can choose between a higher-capability but higher-conflict-risk combination (Union) and a more constrained but lower-conflict-risk combination (Selective Merge). This is an architectural capability with no prior analog: the choice is not between combining and not combining, but between inclusive combination and targeted combination, with the target specified under human authority.

---

## 4. The biological analog — and its limits

Biology is the domain that has treated two-parent combination as a fundamental lifecycle primitive, and the CKS mating machinery imports that status from biology into AI Self architecture under governance. For the Union pattern, the biological analog is reasonably direct: biological syngamy fuses two parents' genetic content into an offspring that carries both. For the Selective Merge pattern, no direct biological analog exists.

Biological mating transmits whole genomes. An offspring in canonical sexual reproduction does not receive a selected subset of each parent's genes chosen by an external governance actor; it receives a full complement of genetic material determined by the mechanics of meiosis and fertilization. Selective breeding as practiced in agriculture selects which organisms reproduce — which parents are mated — but not which elements within each parent's genome cross into the offspring. The selection is between organisms, not between elements within organisms.

Genetic engineering techniques are closer: they select specific genes for transfer. But genetic engineering operates on organisms through laboratory intervention, not through an architectural governance primitive that is part of the organism's lifecycle machinery. A CKS deployment that executes Selective Merge is not performing an exceptional laboratory operation; it is executing a standard lifecycle primitive under the same governance commitment that governs birth and death.

The closest computational neighbor, noted by Paper 2, is software product-line engineering's selective composition, where feature models declare valid product configurations and product derivation selects subsets subject to compatibility constraints. The differentiation is on the governance dimension: software product-line selective composition is constraint-driven, with curation framed as engineering work; CKS Selective Merge is governance-driven, with the curation rules themselves substrate-resident authoritative content under human authority per A2.04 and A2.46.

The architectural substance of Selective Merge is not borrowed from biology. It is a distinctive commitment: governance-authored selection rules specify element-level combination, producing offspring whose DNA is a purposefully designed subset of parental DNA rather than a full inheritance.

---

## 5. Inherited Paper 1 commitments

Selective Merge inherits all six Paper 1 architectural commitments without modification. The most directly load-bearing are:

**A1.03 — Conflict as first-class substrate state.** Conflicts that survive selection are preserved as first-class addressable substrate state per A1.03. The selective mechanism reduces the number of conflicts that reach offspring DNA but does not change their treatment when they do. A1.03 holds for selected elements exactly as it holds for all substrate content.

**A1.01 — Human-governed.** Selective Merge is authorized per B2.41, and the selection rules governing element inclusion are authored per A2.04. Both the mating event and the rules that configure it are governed. Humans retain the right to inspect, modify, and override selection rules at any time. Selection rules are not implicit or derived; they are explicitly authored substrate-resident content exercisable under the three governance rights.

**A2.04 — Rule authoring as governance.** Selection rules are the specific form of orchestration rule that governs Selective Merge combination. Authoring them is a governance act. The labor of drafting selection rules may be performed by humans directly or by LLMs operating under human direction; authority over the rules remains with humans.

**A2.46 — Authoritative substrate content.** Selection rules are substrate-resident authoritative content. They carry the same authoritative status as all other Category 4 content. Their presence in the substrate makes them inspectable, modifiable, and subject to override — and makes the Selective Merge event they governed retraceable.

**A2.40 — Six provenance metadata fields.** Selective Merge events record all six fields. The selection rules applied are themselves part of the provenance record, enabling complete retraceability of the combination decision.

**A1.07 — Path retraceability.** Offspring traces through both parent lineages per B2.43. The selection rules applied to each parent are recorded. The path from offspring DNA to each parent source is fully retraceable.

**A1.13 — Composition requirements.** Offspring produced by Selective Merge must satisfy the five composition requirements at every boundary. Selective Merge does not relax composition requirements by virtue of being more targeted than Union.

---

## 6. Operational implications

Deployments use Selective Merge when targeted combination is needed and when both the desired capabilities from each parent and the undesired elements (including potential conflicting elements) are identifiable enough to specify in selection rules.

The canonical deployment case is combining specific capabilities from two parents: take parent A's domain-knowledge elements and parent B's process-optimization elements into an offspring cell specialized for both. The offspring carries the capabilities needed from each parent without carrying the full DNA of either. A Union of the same parents would produce a larger, more capable, and potentially more conflicted offspring; Selective Merge produces a smaller, more targeted, and more governably conflict-reduced offspring. Neither is the correct general answer; the choice is a governance decision made by the actors who author the selection rules.

Selective Merge for aspect creation follows the same logic at aspect scope: take parent aspect A's conflict-handling rules and parent aspect B's invocation patterns, producing an offspring aspect that combines specific governance machinery from each parent.

Selection rules evolve through directed selection per B1.14 as combination patterns mature. What begins as element-specific rules may be generalized to type-specific or function-specific rules as governance actors identify patterns in which elements should routinely cross from which parents. This evolution of selection rules is itself governed substrate content modification — modifying selection rules is a governance act per A2.04.

Selective Merge verification per B2.50 includes verifying that selection rules were correctly applied: that the elements in offspring DNA are exactly the elements the selection rules specified, that no additional elements crossed the boundary, and that the provenance record per A2.40 accurately captures the rules applied.

---

## 7. What Selective Merge does not do

The scope of Selective Merge is precisely bounded. Naming what it does not do is as important as naming what it does.

**Selective Merge does not auto-resolve remaining conflicts.** A1.03 holds for any conflicts that survive selection. If selected elements conflict, the conflict is preserved as first-class substrate state, addressable in the offspring's substrate. Auto-resolution is not within the pattern's commitment.

**Selective Merge does not include all elements.** That is Union's commitment per B2.46. Selective Merge is the targeted-combination pattern; Union is the inclusive-combination pattern. A deployment that needs to include all elements from both parents should use Union.

**Selective Merge does not explicitly preserve parent lineage in offspring DNA.** Offspring lineage references both parent lineages per B2.43, but the offspring does not carry pointers to parent cells as substrate content. That is Lineage-preserved union's commitment per B2.48. Selective Merge produces offspring that know their lineage but do not carry parent cell references as DNA content.

**Selective Merge does not guarantee conflict-free offspring.** Selection rules reduce conflict risk by enabling exclusion of conflicting elements, but they do not guarantee that selected elements are conflict-free among themselves. Governance actors who author selection rules must reason about potential conflicts among selected elements; the architecture does not perform that reasoning automatically.

**Selective Merge selection rules are not exhaustive by default.** Selection rules must be explicitly authored per A2.04 for the elements to be included. An element not named or typed in any selection rule is not included. This is the correct default: the selection is what the rules say, nothing more and nothing less.

**Selective Merge is not reversible after birth.** The offspring is a new substrate entity. After birth per B1.09, the offspring's DNA is its own. Retiring the offspring requires death per B1.11; Selective Merge does not itself provide a mechanism for undoing the combination after birth.

**Selection rules are not implicit.** Selection cannot be performed without explicitly authored selection rules. There is no default selection, no inferred selection, and no emergent selection. The rules must exist as substrate-resident authoritative content before the Selective Merge event proceeds.

---

## 8. One-sentence architectural test

A mating event instantiates the CKS Selective Merge pattern if and only if: governance-authored selection rules per A2.04, held as substrate-resident authoritative content per A2.46, specify which DNA elements from each identified parent source are included in offspring DNA, such that offspring DNA contains exactly the selected subset from parent A plus the selected subset from parent B, with any conflicts among selected elements preserved as first-class substrate state per A1.03, and the event and its selection rules are recorded in full per A2.40.

---

## 9. Why naming Selective Merge as a standalone pattern matters

B1.10 commits to mating as a governed lifecycle primitive. Within that commitment, Paper 2 specifies three distinct pattern variants. The distinction matters architecturally because the three patterns are not interchangeable approximations of the same operation — they make different commitments about what crosses the combination boundary, what conflict risk attaches, and what kind of offspring results. A prior-art chain that names only mating in general, or names only Union, does not establish the Selective Merge commitment. This note fills that gap.

The element-level governed combination that Selective Merge formalizes — selection rules per A2.04 specifying which elements cross the boundary, held as authoritative substrate content per A2.46, producing purposefully designed offspring whose capabilities are a governance product — is the architectural substance being placed into the public record. Any party seeking to claim this combination of properties as novel invention after this publication must contend with this note as prior art.

B2.47 is the third of six notes decomposing B1.10. B2.48 will formalize Lineage-preserved union — the third mating pattern, which is the inclusive-combination variant with explicit parent cell pointers as offspring DNA content. B2.49 will address mating governance and lineage establishment. B2.50 will address mating verification, including verification that selection rules were correctly applied in Selective Merge events. After B2.50, Phase B2 will turn to the B1.11 death decomposition, beginning with functional obsolescence at B2.51.
