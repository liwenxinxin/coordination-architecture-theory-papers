# Selective-Merge Pattern Inherits Paper 1's Human-Governed Write Authority

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series.

## Abstract

Paper 2's mating mechanism offers three pattern variants for combining parental entity content into an offspring entity. The middle variant — selective merge — is the governance-curated combination pattern: governance explicitly selects which rules from each parent entity enter the offspring's DNA, rather than accepting all rules from both parents (union) or accepting all rules while maximally preserving provenance pointers (lineage-preserved union). This note formalizes the inheritance edge: selective merge directly inherits Paper 1's human-governed write authority (Claim 3 / A0.03). The write authority identity is preserved because no rule enters the offspring without a governance selection decision, the selection decisions are authority acts not labor acts, and governance is operating the modify right at mating scope. What is new in Paper 2 is the entity-DNA scope of the write authority exercise, the comparative-selection task that makes the governance decision structurally different from ordinary substrate modification, the strategic use of governance authority to reduce the offspring's conflict density at mating time, and the richer mating record that documents selection rationale rule-by-rule. The note positions C1.13 within the three-pattern mating triple (C1.12: union inherits conflict preservation; C1.13: selective merge inherits write authority; C1.14: lineage-preserved union inherits path retraceability), states prior-art significance, and provides an operational test.

---

## 1. The three-pattern triple and where C1.13 sits

Paper 2's mating mechanism makes three governance commitments in parallel. Each commitment is carried by a different pattern variant, and each variant inherits a different Paper 1 principle as its primary governance mechanism.

The first pattern, union, keeps all rules from both parents and preserves all merge-time conflicts as first-class substrate state in the offspring. Its primary governance commitment is to preserve everything — to accept both parents' specifications intact and carry any resulting contradictions forward as addressable objects. The Paper 1 principle it inherits is conflict preservation (Paper 1 §5): the same commitment that prevents contradictions from being silently resolved or discarded in coordination substrate applies at mating time when two entities' rules are combined. Note C1.12 formalizes this edge.

The third pattern, lineage-preserved union, also keeps all rules from both parents, but its defining architectural move is to carry explicit pointers from every offspring rule back to its source in the parent DNA. The paper 1 principle it inherits is path retraceability: the offspring substrate is constituted so that the origin of every element is permanently traceable. Note C1.14 formalizes this edge.

The second pattern — selective merge — occupies the middle position in the triple. Its defining move is not to accept everything from both parents but to have governance explicitly select which rules cross the boundary from each parent into the offspring. Where union exercises the modify right by preserving all conflicts forward, and lineage-preserved union exercises the modify right by ensuring all provenance is traceable, selective merge exercises the modify right as a filtering decision at mating time: governance determines what enters, what is excluded, and which conflicting rules from one parent supersede the corresponding rules from the other. The Paper 1 principle it inherits is human-governed write authority (Claim 3 / A0.03). This note formalizes that edge.

Positioning the three patterns together makes the triple's internal logic visible: the three variants do not differ in kind — all three are governed operations over heritable content — but in what governance is most actively doing. Union governs by accepting and preserving. Lineage-preserved union governs by accepting and tracing. Selective merge governs by selecting and filtering. The three Paper 1 principles they respectively inherit — conflict preservation, path retraceability, and write authority — are not arbitrary pairings; each is the Paper 1 commitment that is most structurally activated by its pattern variant's governance move.

---

## 2. What Paper 1's human-governed write authority commits to

Paper 1's Claim 3 (A0.03) commits to a substrate in which humans retain the right to inspect, modify, and override substrate content and orchestration rules at any time during the substrate's existence. The modify right is the write authority: humans can add, change, or delete any substrate content without requiring justification or permission from any system component.

The authority-not-labor distinction is load-bearing here. The modify right is a structural property of the architecture — it says where authority sits, not who performs the labor of writing content. LLMs operating under human direction may perform the labor of drafting, editing, and proposing substrate content; automated cells may execute under orchestration rules that generate substrate content; but the modify right remains with humans. A substrate in which an LLM can commit content to the substrate without human authority — not just without human labor, but without human authority — fails the commitment. A substrate in which humans can always override, delete, or replace LLM-committed content satisfies it.

Two moments characterize when governance is exercised under this commitment. At design time, humans author the orchestration rules that govern cell-level behavior, including rules that authorize LLMs to perform content-creation labor under human direction. At intervention time, humans exercise the direct override right to modify substrate content as they choose. Neither moment is proportional to substrate size; the cost of governance does not grow with the quantity of content the substrate carries.

This write authority commitment is what selective merge inherits at mating scope, as §3 develops.

---

## 3. Selective merge as an exercise of the modify right at mating scope

The selective merge mating pattern is a governed composition event in which humans explicitly decide which rules from each parent entity's DNA will enter the offspring's DNA. The pattern's defining structural feature is that the offspring's DNA content is not determined by a combination function applied to the parents — it is determined by governance selection decisions. Each rule that enters the offspring does so because governance authorized it to enter.

Three structural features of the selective merge pattern constitute a direct instantiation of the write authority principle.

**No rule enters without governance selection.** The most direct expression of the write authority principle is that nothing appears in the substrate without human governance authorization. Selective merge applies this principle at the DNA level: the offspring's rule set is a governance-curated subset of the union of both parents' rule sets. A rule present in Parent A's DNA and absent from the mating selection does not appear in the offspring. A rule present in Parent B's DNA and excluded by governance does not appear. The only rules that enter are those governance explicitly selected. This is the modify right operating as a content-entry filter: governance is not merely able to intervene if unwanted content appears, but is structurally positioned as the entry gate.

**Authority not labor at the selection decision point.** Governance must make the selection decisions; governance need not perform the labor of identifying what decisions to make. The comparative analysis labor — examining Parent A's rules, examining Parent B's rules, identifying conflicts, mapping which rules cover which domains, proposing candidate selection sets — may be performed by LLMs operating under human direction. This is exactly the authority-not-labor structure Paper 1 Claim 3 establishes: LLM assistance with the labor of content preparation does not displace human authority over the content decision. A selective merge in which an LLM proposes a selection and governance approves it, modifies it, or rejects it satisfies the write authority principle. A selective merge in which an LLM commits the selection without governance authorization does not.

**The modify right exercised before finalization.** Paper 1's modify right applies at any time during the substrate's existence. Selective merge applies the modify right at a specific moment: the mating event, before the offspring's DNA is finalized. This is the modify right operating prospectively — governance is not correcting content that entered without authorization, but is the mechanism by which content authorization is granted in the first place. The selection decisions at mating time are the governance acts that constitute the offspring's initial DNA specification. Once finalized, the offspring's DNA is substrate content subject to the same human-governed write authority for all subsequent modifications; selective merge is the governance act that created the initial state.

---

## 4. What is new in Paper 2

The selective merge pattern inherits the write authority principle, but its deployment in Paper 2's mating mechanism introduces four architectural contributions that are not present in Paper 1.

**Entity-DNA scope.** Paper 1's write authority principle applies to substrate content generally — cells, entities, relationships, decisions, conflicts, orchestration rules, and whatever other structures the substrate carries. Selective merge applies write authority to a specific class of substrate content: the entity DNA that specifies an entity's operating rules and behaviors. DNA-level write authority at mating time is a specific instantiation of the general principle: governance is not simply modifying existing content but is specifying, through selection, the heritable rule set that the offspring entity will operate under. The scope is new even though the principle is inherited.

**The comparative selection task.** Paper 1's write authority principle governs modification of substrate content that exists in one place. Selective merge introduces a new governance task structure: governance is simultaneously examining two parent DNA sets and making selection decisions relative to both. This comparative governance task — which of these two coverage-domain-overlapping rule sets should govern the offspring in this domain? — is structurally different from the ordinary substrate modification Paper 1 governs. The governance decision requires access to and evaluation of two specification sets, not one. The mating record that captures this decision is correspondingly richer: it must record not just what governance chose but what governance chose between.

**Conflict reduction as governance goal.** Union accepts all conflicts as first-class substrate state. Selective merge deploys governance authority with a different strategic aim: reducing the offspring's conflict density before the offspring begins operating. When Parent A and Parent B carry conflicting rules for the same domain, selective merge allows governance to choose one parent's rule and exclude the other's, thereby preventing the conflict from entering the offspring's DNA at all. This is the modify right operating preventively: governance is not correcting a conflict that already exists in the substrate but is configuring the offspring's rule set so that the conflict does not arise. Union and selective merge both exercise the modify right; they differ in what governance is trying to accomplish. Conflict reduction as a governance goal at mating time is a Paper 2 contribution not present in Paper 1.

**A richer mating record.** Union's mating record captures that two parents were combined and, where conflicts arose, that the conflicts are preserved in the offspring. Selective merge's mating record must capture which rules from each parent were selected, which were excluded, and — ideally — the governance rationale for selection decisions where non-obvious. This is a governance record of greater informational density than union's: it documents not just the outcome of mating but the decision process governance engaged in at each selection point. This richer record is not a separate architectural feature appended to selective merge; it is the natural expression of what selective merge requires governance to do. A selective merge mating record that cannot be inspected to determine which parent supplied each offspring rule, and whether both parents' original rules are accessible for comparison, is not a complete governance record.

---

## 5. Positioning within the three-pattern triple

Stating the triple's internal structure as a single paragraph: union inherits conflict preservation because its governance commitment is to accept both parent DNA sets and carry all resulting contradictions forward as addressable substrate state; selective merge inherits write authority because its governance commitment is to explicitly select what enters the offspring DNA, making governance the content-entry mechanism at mating scope; lineage-preserved union inherits path retraceability because its governance commitment is to ensure every element of the offspring's DNA remains traceable to its source, making the provenance graph permanently available for inspection.

Each pattern is available as a configuration choice for a given mating event. A deployment may use different patterns at different mating events depending on governance requirements: if the deployment priority is maximum specification coverage and the governance capability for handling conflicts downstream is strong, union is appropriate; if the priority is a clean offspring specification with minimal inherited conflict, selective merge is appropriate; if the priority is permanent auditability of heritable lineage, lineage-preserved union is appropriate. The three patterns are not in competition; they are governance choices that activate different Paper 1 commitments.

The triple's position in the derivation series reflects this structure. C1.12 (union → conflict preservation), C1.13 (selective merge → write authority), and C1.14 (lineage-preserved union → path retraceability) are three parallel inheritance edges, each from a different mating pattern variant to a different Paper 1 principle. They are presented in series rather than in a single note because each inheritance relationship has distinct operational content, distinct prior-art significance, and a distinct operational test.

---

## 6. Prior-art significance

Publishing this inheritance edge as dated prior art forecloses three classes of adversarial claims.

**Governance-curated specification combination is novel relative to Paper 1.** It is not. Paper 1 commits to human-governed write authority over substrate content. Applying that write authority to the combination of two entity specification sets at mating time is a direct instantiation of the principle at entity-DNA scope. The governance move — explicit selection of what enters the substrate — is the same governance move, applied to a specific substrate content class at a specific lifecycle event.

**Selective merge introduces a novel governance mechanism for specification management.** It does not. The governance mechanism is the modify right, which Paper 1 commits to. Selective merge applies the modify right comparatively at mating time. The application is new; the mechanism is inherited.

**Comparative selection between specification sets at composition time is novel.** It is not. Paper 1's write authority principle does not restrict the modify right to single-source substrate content. Any deployment in which governance evaluates two candidate content sets and selects one is applying the modify right in a comparative context. Selective merge formalizes this application pattern at entity-DNA scope in Paper 2; the underlying authority commitment is Paper 1's.

---

## 7. Operational test

A mating event instantiates the selective merge pattern in a CKS-coherent way if and only if all of the following are true:

1. A human with appropriate authority can inspect the offspring's full DNA after mating and trace each rule to the parent from which it was selected.
2. Both parents' original rule sets are accessible in the mating record, so that a reviewer can determine what governance chose between at each selection decision.
3. The mating record identifies, for each included rule, that it was governance-selected (not automatically included by a combination function operating without governance authorization).
4. No rule appears in the offspring's DNA that was not included by a governance selection decision; LLM-proposed selections are admissible only if governance authorized the selection before it was committed to the offspring's DNA.
5. Where governance made exclusion decisions — rules present in one or both parents that do not appear in the offspring — the mating record captures the exclusion (the record does not need to capture every exclusion rationale, but the fact of exclusion must be traceable).
6. The mating record and both parents' original rule sets remain substrate content subject to the human-governed write authority commitment: a human may inspect, modify, or override any element of the mating record after the fact.

A mating event that satisfies (1)–(6) demonstrates the selective merge pattern and demonstrates that the pattern exercises human-governed write authority at entity-DNA mating scope. A mating event that fails any of (1)–(6) may produce an offspring entity, but does not instantiate selective merge as Paper 2 defines it, because the governance-selection structure that constitutes the pattern is absent or incomplete.

---

## 8. Conclusion

The selective merge mating pattern in Paper 2 inherits Paper 1's human-governed write authority commitment directly and specifically. The inheritance relationship holds at three levels: structurally, because no rule enters the offspring without governance selection and LLM assistance with selection labor does not displace governance authority over the selection decision; mechanically, because the modify right is what governance is operating at mating time; and strategically, because governance is using the modify right with a goal — conflict reduction — that is expressed at the DNA-specification level before the offspring begins operating.

What is new in Paper 2 is the entity-DNA scope, the comparative selection task, conflict reduction as a mating-time governance goal, and the richer mating record these require. None of these are new governance mechanisms; all are applications and extensions of the write authority principle Paper 1 commits to.

The three mating patterns together demonstrate that Paper 2's lifecycle machinery is built on Paper 1's governance commitments, with each pattern variant activating a different Paper 1 principle as its primary governance mechanism: union activates conflict preservation; selective merge activates write authority; lineage-preserved union activates path retraceability. The patterns are the lifecycle-level expressions of the Paper 1 architecture.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Selective-Merge Pattern Inherits Paper 1's Human-Governed Write Authority.* May 14, 2026. ORCID: 0009-0004-8065-3235.
