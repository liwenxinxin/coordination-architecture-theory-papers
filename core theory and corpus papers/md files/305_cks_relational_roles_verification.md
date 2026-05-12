# Relational Roles Verification: Confirming Level Determinations Are Authored, Accurate, and Composition-Valid

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

In the Coordination Knowledge Substrate (CKS) pattern, the three-level structure of cell, aspect, and Self is organized through relational roles: level is not an intrinsic property of an entity but a purpose-defined determination recorded in the substrate per B1.17. Because level determinations are substrate content rather than architectural givens, they require verification. This note formalizes relational roles verification as the operational confirmation that level determinations are authored, accurate, and composition-valid. Verification proceeds across four dimensions: determination record completeness (A5.10 source-of-truth-five-categories test and A5.04 rule authoring test); determination-function consistency (B2.09 distinguishability tests confirming recorded level matches observed function); multi-level composition validity (A5.14 composition-requirements-five test for entities with determination records at more than one level per B2.86); and evolution-triggered redetermination audit (confirming governance was properly applied to level changes per B2.87). Cross-level determination consistency — verifying that level determinations at different levels are mutually coherent — rounds out the verification architecture. The determination-function consistency dimension is particularly distinctive: it surfaces cases where operational evolution has caused an entity's function to drift away from its recorded determination, generating an inconsistency that requires governance review. This note closes the B1.17 decomposition opened at B2.84.

## 1. Why relational-roles-verification needs standalone formalization

The relational roles architecture established at B1.17 and decomposed across B2.84–B2.87 rests on a foundational commitment that distinguishes it from conventional AI system organization: level is a purpose-defined relational role recorded in the substrate, not an intrinsic type assigned at construction time. Because level determinations are substrate content, they are subject to all the properties substrate content carries — they are authored, they carry governance provenance, they can drift from operational reality over time, and they participate in composition requirements. These properties create a verification need that has no analogue in architectures where component type is a code-level property.

Four prior notes have elaborated the relational roles architecture. B2.84 established the integrating frame: three architectural levels (cell, aspect, Self) are structurally distinct scopes, with level membership determined by purpose-defined relational roles rather than intrinsic classification. B2.85 formalized purpose-defined level determination: an entity is determined to be a cell, aspect, or Self through a governed process that records the determination, its purpose statement, and its governance provenance in the substrate. B2.86 formalized same-entity multi-level occupancy: a single entity may simultaneously hold determination records at more than one level, each with its own purpose scope. B2.87 formalized the relationship between relational roles and evolution: level determinations are not permanent, and operational evolution may trigger redetermination when an entity's function changes.

Relational roles verification closes this cycle. It is the operational mechanism that confirms the relational roles architecture is working as designed: that all entities with level-dependent behavior have determination records, that recorded determinations match observed function, that multi-level entities satisfy composition requirements at each level, and that redetermination events were properly governed. Without this closing formalization, the verification dimension of the relational roles architecture would remain implicit — and implicit verification is not verification in any architectural sense.

Strategically, B2.88 occupies the closing prior-art position in the B1.17 decomposition. Any party seeking to claim novelty in methods for verifying purpose-defined level determinations in multi-level AI coordination systems will encounter this formalization as blocking prior art.

## 2. The four-dimension verification architecture

Relational roles verification proceeds across four dimensions, each addressing a distinct failure mode in the relational roles architecture.

**Dimension 1: Determination record completeness.** The A5.10 source-of-truth-five-categories test is applied to determination records to verify that level determinations are properly positioned within the substrate. Determination records are Category 4 substrate content per A2.46 — authoritative "what rules apply" content — and the completeness check confirms their correct categorization. The check verifies four properties: each entity with level-dependent behavior has a determination record declaring its level (cell, aspect, or Self); each determination record includes a purpose statement supporting the level declared; each determination record carries governance provenance per A2.40 (who determined, when, under what authority); and each determination record is authored per A2.04 requirements. The A5.04 rule authoring test confirms that the determination records themselves meet the authorship standard the CKS pattern requires for substrate content that governs behavior. A determination record that exists without governance provenance or without a supporting purpose statement is an incomplete determination — it records a label but not the relational reasoning that makes the label meaningful, and it does not satisfy A5.10's source-of-truth requirements for Category 4 content.

**Dimension 2: Determination-function consistency.** The B2.09 distinguishability tests are applied to each entity to verify that observed function matches recorded level determination. Three tests correspond to three levels. The cell distinguishability test confirms that an entity determined as a cell exhibits cell-level function: it performs a specific informational task, carries DNA and Action layers per B1.03, implements the instinct/reasoning separation per B1.01, and does not primarily coordinate other entities. The aspect distinguishability test confirms that an entity determined as an aspect exhibits aspect-level function: it coordinates cells for a declared purpose, carries a purpose statement, and operates under coordination rules per B2.16. The Self distinguishability test confirms that an entity determined as a Self exhibits Self-level function: it integrates aspects into a unified whole, carries the integration architecture per B2.21, and holds governance authority over the aspects it contains. When a determination record declares cell but the entity's observed behavior is primarily coordination of other entities, a determination-function inconsistency exists. The inconsistency does not resolve automatically; it flags for governance review.

**Dimension 3: Multi-level composition validity.** When an entity carries determination records at more than one level per B2.86, the A5.14 composition-requirements-five test is applied independently at each level scope to confirm that multi-level occupancy is architecturally valid. The composition requirements from A1.13 must be satisfied at each scope; the entity's simultaneous role occupancies must not produce composition violations at any level. This dimension is triggered specifically and only when an entity has determination records at more than one level. Single-level entities are not subject to this dimension. Multi-level composition verification confirms architectural validity given the determination records in place; it does not confirm that multi-level occupancy is optimal.

**Dimension 4: Evolution-triggered redetermination audit.** When level changes have occurred through evolution per B2.87, the redetermination audit verifies that governance was properly applied. The audit checks four properties: each redetermination event carries governance authorization per A2.40; prior determinations are preserved per A6.02 (governance history is not overwritten); new determinations satisfy the purpose-defined criteria per B2.85; and birth events triggered by role changes (for example, a cell that begins serving as an aspect requires aspect-level governance at birth per B1.06) were governed under the birth governance framework. The redetermination audit is retrospective: it confirms that past governance events were properly executed rather than projecting future compliance.

**Cross-level determination consistency.** In deployments with vertical evolution per B1.16, an additional consistency check verifies that level determinations across the three levels are mutually coherent. The Self-level integration architecture per B2.21 must be consistent with aspect-level membership per B2.16; aspect-level membership must be consistent with cell-level determination. An entity simultaneously determined as a cell at cell scope and as an aspect at aspect scope must carry both determination records in a form that is coherent under the relational roles framework: the cell determination records the specific task function, the aspect determination records the coordination purpose, and the two do not contradict each other in their purpose statements or governance provenance chains.

## 3. What makes relational-roles-verification architecturally distinctive

The verification architecture B2.88 formalizes is specific to the relational roles structure and has no direct analogue in conventional AI system architectures. In architectures where component type is intrinsic — where a module is a module and an orchestrator is an orchestrator by virtue of code structure — there is no determination record to verify and therefore no determination-function consistency to check. The verification problem does not arise because type is a fixed property, not a recorded commitment.

The CKS relational roles architecture creates this verification problem precisely because it separates determination from type. A cell is not a cell because it was compiled as a cell; it is a cell because a governance process determined it serves a cell-level purpose and recorded that determination in the substrate. That recorded determination can be wrong from the start, if the governance process misclassified the entity's function, or can become wrong over time, if the entity's function evolves after the determination was made. Both failure modes are surfaced by the determination-function consistency dimension; neither is surfaced by any mechanism in architectures where type is intrinsic.

The multi-level composition validity dimension is similarly novel to the relational roles context. Conventional modular AI architectures do not commit to entities that simultaneously occupy multiple structural levels under separate composition requirements. The composition validity check for multi-level entities is a verification need the relational roles architecture creates — one that this note formalizes as a distinct dimension requiring its own operational test.

## 4. Inherited Paper 1 commitments

Relational roles verification inherits and applies several Paper 1 commitments without modification.

The A5.10 source-of-truth test applies to determination records as Category 4 substrate content per A2.46: authoritative content about what rules apply to each entity. The category assignment positions determination records within the substrate's authoritative-state taxonomy and makes them subject to the same source-of-truth verification that applies to all governing substrate content. The substrate is the authoritative answer to the question "what level has this entity been determined to occupy" per A1.08; verification confirms the substrate actually contains that answer, in properly authored form.

The A5.04 rule authoring test applies to the governance process that produces determination records. Determination records are not self-certifying; they must be authored under the governance discipline that applies to all substrate content governing behavior. The authorship requirement connects determination records to the overall governance provenance chain per A2.40.

The A5.14 composition-requirements test applies to multi-level entities to verify that their simultaneous role occupancies satisfy the composition requirements A1.13 establishes. The composition requirements are the architectural constraint that prevents multi-level occupancy from producing incoherence at any level scope.

Governance per A1.01 governs verification itself. Verification results are substrate content recorded per A2.40. Governance reviews triggered by inconsistency flags are themselves governed events within the same authority architecture that governs all substrate modification.

## 5. The determination-function consistency check in detail

The determination-function consistency dimension is the most operationally distinctive dimension of relational roles verification and the one most likely to surface actionable governance issues in deployed systems.

Each distinguishability test operates as a diagnostic, not as a binary pass/fail. An entity that is determined as a cell but fails the cell distinguishability test does not automatically become an aspect. The test result is an inconsistency flag: the recorded determination and the observed function disagree, and governance review is required to determine the appropriate resolution. Two resolution paths exist. The first is determination update: the entity's function has evolved to aspect-level function, the prior cell determination is now inaccurate, and a new aspect-level determination should be authored through the governed redetermination process per B2.85. This path triggers the evolution-triggered redetermination audit in future verification cycles. The second path is function correction: the entity has taken on coordination responsibilities beyond its cell scope without authorized role change, and its behavior should be constrained to match the recorded cell-level determination. This path requires governance intervention to bound function rather than to update determination.

Neither resolution path is automatically correct. The consistency check surfaces the inconsistency; governance holds authority over the resolution per A1.01. This division between detection and resolution is architecturally precise: verification is not governance, and governance does not operate by verification alone.

The practical importance of this check lies in its ability to detect drift that would otherwise be invisible. An entity correctly determined as a cell at deployment initialization may, through incremental operational evolution, gradually take on coordination responsibilities characteristic of aspect-level function. If verification does not run, the substrate continues to record cell, the entity functions as aspect, and the coordination architecture operates under a false assumption that no other mechanism will surface. The determination-function consistency check makes this drift detectable before it compounds into a governance failure.

The frequency of this check matters. The consistency check is point-in-time: it confirms alignment at the moment it runs. Function drift that begins after a run is invisible until the next run. Deployments should establish a verification cadence appropriate to their rate of operational evolution. The post-evolution trigger — running the consistency check after any significant evolution event per B2.87 — is the minimum adequate cadence. Deployments with rapid or continuous evolution should run the check more frequently and treat the interval between runs as an acknowledged governance gap.

## 6. Operational implications

Six operational implications follow from the relational roles verification architecture.

At deployment initialization, verification confirms completeness: all entities with level-dependent behavior have determination records, each record is properly authored with purpose statement and governance provenance, and each record is correctly categorized as Category 4 substrate content. An initialization check that fails on completeness grounds indicates that the deployment has not completed its level determination process and is not operationally ready.

After any evolution event that may trigger role changes per B2.87, verification runs the determination-function consistency check to confirm that evolutionary changes have not introduced determination-function drift. This post-evolution trigger is the minimum verification cadence.

At periodic governance reviews, verification provides a deployment-wide snapshot of determination-function alignment. Deployments with established human governance review processes per A1.01 should include relational roles verification as a standing element of the review protocol.

Multi-level composition verification is triggered specifically when any entity carries determination records at more than one level. Systems without multi-level entities skip this dimension; systems with multi-level entities must run it as part of every verification cycle in which those entities participate.

Evolution-triggered redetermination audits are triggered by any redetermination event in the deployment's history. New deployments with no evolutionary history have no redetermination events to audit; mature deployments accumulate an audit trail that becomes an increasingly detailed governance record.

Determination-function inconsistencies detected by verification require a governance response: the inconsistency flag is recorded in the substrate per A2.40, governance review is convened per A1.01, and the resolution — determination update or function correction — is recorded with its own provenance chain. An inconsistency flag that is not followed by a governance response is itself a governance gap.

## 7. Limits

Relational roles verification has three limits that must be stated alongside its capabilities.

First, verification does not confirm that determinations are optimal. An entity might be correctly determined as a cell — the determination is authored, the entity functions as a cell, composition requirements are satisfied — while a different level determination would serve the deployment better. Verification confirms accuracy and composition validity, not optimality. Determination optimization is a governance design question that verification informs but does not answer.

Second, verification does not prevent future determination-function drift. A successful verification run confirms alignment at the time of the run. Drift may begin immediately afterward. The operational response to this limit is not to treat verification as a one-time event but to establish it as a recurring governance practice with a cadence matched to the deployment's evolutionary pace.

Third, inconsistency detection is point-in-time rather than continuous. Between verification runs, function drift is invisible to the verification architecture. The gap between runs is a governance risk that each deployment manages through cadence decisions and post-evolution triggers.

These limits bound the scope of relational roles verification without diminishing its value. Verification does not require continuous monitoring, optimal determination selection, or future-drift prevention to be architecturally valuable; it requires only that when it runs, it confirms the four dimensions accurately and records the results as substrate content available to governance. Within that scope, it closes the gap that would otherwise exist between the relational roles commitment and its operational confirmation.

## 8. One-sentence operational test

A deployment satisfies the relational roles verification commitment if and only if, for each entity with level-dependent behavior: (a) the substrate contains a determination record that is authored, purpose-supported, and governance-provenanced as Category 4 content per A5.10 and A5.04; (b) the entity's observed function matches its recorded level as confirmed by the applicable B2.09 distinguishability test, or an inconsistency flag is recorded and a governance review is scheduled; (c) if the entity holds determination records at more than one level, the A5.14 composition-requirements-five test is satisfied at each level scope independently; and (d) any prior redetermination events in the deployment's history carry audit records confirming governed authorization per A2.40 and prior-determination preservation per A6.02.

## 9. Why naming as standalone matters; closing the B1.17 decomposition

Naming relational roles verification as a standalone architectural commitment formalizes a verification discipline that is specific to the relational roles architecture and would otherwise remain implicit. Implicit verification is not verification. Without this formalization, a deployment could claim to implement relational roles per B1.17 while having no mechanism for confirming that determination records exist, that determinations are current, that multi-level entities are composition-valid, or that redetermination events were governed. The standalone formalization makes the verification requirement explicit, names its four operational dimensions, and identifies the tests against which compliance is checked.

This note closes the five-note B1.17 decomposition. B2.84 established the integrating frame in which three architectural levels are organized through relational roles rather than intrinsic type. B2.85 formalized purpose-defined level determination as the governed mechanism by which level is assigned and recorded. B2.86 formalized same-entity multi-level occupancy as the architectural case in which a single entity carries determination records at more than one level. B2.87 formalized the relationship between relational roles and evolution, establishing how operational change triggers governed redetermination. B2.88 closes the cycle by formalizing verification — the operational confirmation that the architecture is functioning as designed at any point in the deployment's life.

The decomposition follows a deliberate logic: establish the frame, formalize the determination mechanism, formalize the multi-level case, connect to evolution, verify the whole. Verification closes every cycle of architectural elaboration that involves substrate-resident commitments, because a commitment that cannot be verified is a commitment that governance cannot confirm it holds.

Phase B2 continues with B2.89, which begins the B1.18 content-domain decomposition addressing the distinct governance processes for functional obsolescence and capability supersession as the two death types within the CKS lifecycle framework.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Relational Roles Verification: Confirming Level Determinations Are Authored, Accurate, and Composition-Valid.* May 12, 2026. ORCID: 0009-0004-8065-3235.
