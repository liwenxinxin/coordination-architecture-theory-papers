# Twelve FAI Event Anti-Patterns

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note is a synthesis derivation over D2.01–D2.18. Those nineteen prior notes establish the operational sub-commitments for Paper 3's five core claims governing Full Aspect Integration (FAI) events: shared substrate construction and dissolution; FAI as the exchange primitive; three-tier conflict handling; four-locus evolution feed; and configuration as substrate content. D2.19 consolidates the governance failure modes that appear across D2.01–D2.18 into a named set of twelve anti-patterns, groups them into five taxonomy categories, identifies Paper 2 intra-Self analogs where the inheritance chain runs through Series B, and provides a binary operational test for each anti-pattern. The twelve named anti-patterns — Ungoverned Construction, Ungoverned Dissolution, Silent Conflict Collapse, Automatic DNA Absorption, Non-Attributed Ingestion, Implicit Configuration, Home Perimeter Erosion, Exchange Bounding Violation, Pseudo-Selective Merge, Shallow-Reference Merge, Unresponsive Escalation, and Informal Resolution Rules — constitute public prior art establishing that these FAI governance failure modes were anticipated by the CKS trilogy.

---

## 1. Purpose and Position in the Series

D2.01 through D2.18 decompose Paper 3's five core claims into operational variants: the requirements for pre-construction authorization and construction records (D1.01/D1.02); the exchange bounding commitment that excludes instinct-layer content and LLM weights from FAI exchange (D1.10/D1.19); the three-tier conflict-handling protocol with its preserve, resolve, and escalate tiers (D1.13–D1.16); the four-locus evolution feed routing FAI-origin content into each participating Self's home substrate through governed pathways (D1.17–D1.21); and the configuration substrate commitment specifying that all six configurable dimensions of an FAI event are authored substrate content, not infrastructure defaults (D1.22–D1.25).

Across those notes, governance failure modes appear in passing — as the negative cases that establish why each positive commitment matters. D2.19 makes these failure modes first-class. It names each one, states the commitment it violates, identifies the Paper 2 intra-Self analog where one exists, and provides the operational test that would detect its presence.

Three framing decisions govern this note:

**Naming as prior art.** Naming a failure mode is a dated prior-art act. Each of the twelve names below records that this failure mode was identified, described, and published as a known governance problem in the CKS FAI architecture. Any subsequent claim of novelty in identifying or solving one of these problems must contend with this publication date.

**Inheritance chain continuity.** Three anti-patterns have direct intra-Self analogs in Series B: AP-1 (Ungoverned Construction) is the inter-Self analog of Paper 2's B3.10 (Ungoverned Birth); AP-2 (Ungoverned Dissolution) is the inter-Self analog of B3.11 (Ungoverned Death); AP-3 (Silent Conflict Collapse) is the inter-Self analog of B3.08 (Untracked Conflict Resolution). These connections show that the FAI governance failure modes are structurally the same failure modes already formalized at intra-Self scope — the prior-art chain runs continuously from Paper 1 through Paper 2 through Paper 3 at both the positive-commitment level and the failure-mode level.

**Taxonomy as scaffold for Phase D3.** The five-category taxonomy introduced here — Lifecycle, Conflict Handling, Evolution Feed, Configuration, and Perimeter Integrity — provides the organizational structure Phase D3 anti-pattern notes will inherit. D2.19 is the overview; D3 will develop each anti-pattern to standalone depth within the same taxonomy.

---

## 2. The Twelve Anti-Patterns

### AP-1: Ungoverned Construction

A shared substrate begins operation without pre-construction authorization from the participating Selves' governance structures and without a construction record authored as substrate content before the FAI event commences. Participating Selves begin exchanging aspects through a substrate whose existence has not been jointly authorized and whose construction has not been recorded. There is no dated, governed artifact establishing what was agreed before the shared substrate came into being.

*Paper 2 analog:* B3.10 (Ungoverned Birth) — an intra-Self cell or aspect begins operation without governance authorization or a birth record in the home substrate. The inter-Self and intra-Self failure modes are structurally identical: a governed object begins operation without the governance record that makes its existence traceable.

*Commits violated:* D1.01 (pre-construction authorization), D1.02 (construction record as substrate content).

---

### AP-2: Ungoverned Dissolution

A shared substrate dissolves without a dissolution record, without execution of the configured persistence policy, and without activation of hand-off boundary records that route FAI-origin content into each participating Self's home substrate. Content from the shared substrate flows into home substrates without governance attribution. The event's end is operationally present but architecturally absent.

*Paper 2 analog:* B3.11 (Ungoverned Death) — an intra-Self cell or aspect dissolves without a dissolution record or persistence policy execution, losing its governance trace at the moment of ending. The inter-Self failure mode extends this to the cross-perimeter case: dissolution without record means neither participating Self's home governance can account for what originated in the shared substrate.

*Commitments violated:* D1.04 (dissolution record), D1.05 (persistence policy as substrate content), D1.20 (hand-off boundary activation).

---

### AP-3: Silent Conflict Collapse

Conflicts detected during merge of contributed aspects are auto-resolved — one side discarded, one side retained — without first-class registration of the conflict in the shared substrate's conflict registry. Neither the discarded content nor the resolution decision is preserved as substrate state. The conflict existed operationally but does not exist in the governance record.

*Paper 2 analog:* B3.08 (Untracked Conflict Resolution) — an intra-Self conflict between substrate entries is resolved by overwriting one entry without preserving the conflict as a first-class object. Paper 1 Claim 2 requires conflict preservation at cell scope; Paper 3 requires it at inter-Self scope; B3.08 and AP-3 are the same failure mode at different scopes.

*Commitments violated:* Paper 1 Claim 2 (conflict as first-class state) at inter-Self scope; D1.13 (preserve tier as default); D1.15 (conflict registry as substrate content).

---

### AP-4: Automatic DNA Absorption

FAI-origin DNA content — aspects or cells originating in the shared substrate — enters a participating Self's home DNA layer without a directed selection event and without home governance authorization for that entry. The Self's home DNA changes as a result of FAI participation, but the change is traceable to no human-authorized selection decision. Home DNA evolution occurs without governance accountability.

*Paper 2 analog:* None directly named in Series B, but the failure mode violates the directed-selection governance requirements Paper 2 establishes for intra-Self DNA evolution (B2.xx directed-selection sub-commitments). AP-4 applies those requirements at the FAI ingestion boundary: what enters home DNA from an inter-Self event must be selected under the same governance discipline as what enters home DNA from intra-Self operations.

*Commitments violated:* D1.18 (directed selection for DNA-layer ingestion), D1.21 (home governance authorization for each ingestion pathway).

---

### AP-5: Non-Attributed Ingestion

FAI-origin action-layer records enter a participating Self's home action layer without provenance metadata identifying their origin in the shared substrate and their contributing Self. Home action-layer content accumulated through FAI participation is indistinguishable from content generated through that Self's own operations. Inter-Self learning cannot be separated from home-generated learning in the governance record.

*Paper 2 analog:* None directly named in Series B, but the failure mode violates the provenance requirement Paper 1 establishes at A1.07 and Paper 2 extends to the action-layer feed. AP-5 applies the provenance requirement to the inter-Self ingestion boundary: FAI-origin action-layer content carries a provenance chain that must name both the shared substrate and the contributing Self.

*Commitments violated:* Paper 1 A1.07 (provenance as substrate content); D1.19 (action-layer ingestion with provenance carry-over).

---

### AP-6: Implicit Configuration

An FAI event operates without an authored configuration substrate. The six configurable dimensions of the event — which aspects each Self contributes, merge mode, provenance depth, conflict-handling protocol, persistence policy, and dissolution terms — are not authored as substrate content under joint governance. The event runs on infrastructure defaults rather than on governed, human-authored configurations.

*Paper 2 analog:* None directly named, but the failure mode parallels the B2.xx cell-configuration anti-patterns in which cell behavior is governed by runtime defaults rather than authored orchestration rules.

*Commitments violated:* D1.22 (all six dimensions as substrate content), D1.25 (configuration-of-configuration as substrate content, requiring that even the meta-level of FAI configuration is human-authored).

---

### AP-7: Home Perimeter Erosion

FAI participation produces unintended changes to a participating Self's home DNA, reduction of that Self's home governance authority over its own substrate, or involuntary exposure of non-contributed aspects to other participating Selves. The inter-Self perimeter's additive property fails: the shared substrate extends each Self's governance scope rather than operating within the contributed scope, and home governance is diminished rather than preserved.

*Paper 2 analog:* None directly named in Series B, which operates within a single Self's perimeter. AP-7 is specific to the inter-Self construction.

*Commitments violated:* D1.03 (perimeter's additive property — the shared substrate's scope is the union of contributed aspects, not a superset of any Self's home scope).

---

### AP-8: Exchange Bounding Violation

Instinct-layer content or LLM weight representations are present in the shared substrate. The exchange bounding commitment that restricts FAI exchange to DNA-layer and action-layer substrate content fails. The inter-Self exchange includes content that Paper 2's instinct/reasoning separation assigns to the inside-the-model domain, and that content now crosses organizational and governance perimeters.

*Paper 2 analog:* None directly named in Series B, but the failure mode violates the instinct/reasoning separation Paper 2 defends as a core architectural commitment. AP-8 is the inter-Self expression of a violation that Paper 2 prohibits at intra-Self scope: instinct-layer content must not cross into the reasoning (substrate) layer. AP-8 extends that prohibition across Self boundaries.

*Commitments violated:* D1.10 (exchange bounded to substrate content); D1.19 (LLM weights excluded from FAI exchange); Paper 2 instinct/reasoning separation at inter-Self scope.

---

### AP-9: Pseudo-Selective Merge

Governance documentation claims a selective merge configuration — in which explicit selection decisions determine which cells or aspects from the contributed content enter the merged result — but no explicit selection decisions with governance records are made during the event. Content inclusion and exclusion are determined by system defaults rather than by human-authorized selection. The selective merge configuration exists in name but not in operation.

*Paper 2 analog:* None directly named in Series B. AP-9 is specific to FAI merge configuration.

*Commitments violated:* D2.08 (modify-right governance requirement for selective merge — the selection decisions that distinguish selective merge from full merge must themselves be governed acts with substrate records).

---

### AP-10: Shallow-Reference Merge

A provenance-carry-over merge configuration is used, but the provenance references provided are nominal: they name contributing Selves at level-1 without enabling actual navigation to each contributing Self's home governance records for the specific content that entered the shared substrate. The bidirectional traceability requirement fails — content in the merged substrate nominally points back to its origin but the path cannot be traversed.

*Paper 2 analog:* None directly named in Series B, but the failure mode is a provenance-chain violation that parallels Paper 1 A1.07's requirement that substrate content carries traceable provenance. AP-10 is the inter-Self expression of nominal vs. navigable provenance.

*Commitments violated:* D2.09 (bidirectional traceability requirement for provenance-carry-over merge — provenance references must enable navigation in both directions: from shared-substrate content to home-substrate records, and from home-substrate records to where that content was contributed).

---

### AP-11: Unresponsive Escalation

A conflict has been escalated to the cross-perimeter joint authority designated in the FAI configuration substrate, but no governance response is received and no default action specified in the configuration is triggered. The conflict remains in ESCALATED status indefinitely. Governance completeness fails: the architecture provides an escalation pathway, but the pathway does not reach a resolution.

*Paper 2 analog:* None directly named in Series B for the escalation tier specifically. The intra-Self escalation pathway in Paper 2 reaches human authority within a single Self's governance; AP-11 is specific to the cross-perimeter escalation case where joint authority across two or more organizations must respond.

*Commitments violated:* D2.14 (governance completeness — every escalated conflict must reach either a human governance response or a triggered default action; indefinite ESCALATED status is not a resolved state).

---

### AP-12: Informal Resolution Rules

Conflict resolution logic for the FAI event is understood between the participating Selves and their governing humans, but is not authored as orchestration rule content within the shared substrate. Conflicts are resolved according to informal shared understanding rather than governed, authored rules. Paper 3 inherits Paper 1 Claim 4's requirement that what governs AI behavior is substrate content; orchestration rules that exist only as informal understanding among participants are not substrate content and therefore do not satisfy the commitment.

*Paper 2 analog:* None directly named in Series B, but the failure mode is a direct violation of Paper 1 Claim 4 (AI-as-substrate-mediator) at inter-Self scope. Claim 4 requires that AI behavior at cell level be governed by authored substrate rules; AP-12 applies that requirement to the orchestration rules that govern conflict resolution within the shared substrate.

*Commitments violated:* Paper 1 Claim 4 (AI-as-substrate-mediator — AI operates over authored substrate content, not over informal understandings); D1.15 (conflict-handling protocol as authored substrate content).

---

## 3. Five-Category Taxonomy

The twelve anti-patterns group into five categories by the governance dimension they violate. The taxonomy provides the organizing structure for Phase D3 standalone anti-pattern notes.

### Category 1: Lifecycle Governance Failures (AP-1, AP-2)

These anti-patterns involve failure at the construction and dissolution boundaries of the FAI event lifecycle. AP-1 (Ungoverned Construction) and AP-2 (Ungoverned Dissolution) are the inter-Self analogs of Paper 2's B3.10 and B3.11, establishing that the lifecycle governance discipline required within a Self is equally required at the boundaries of an inter-Self event. A governed FAI event has a traceable beginning and a traceable end; lifecycle anti-patterns remove one or both traces.

### Category 2: Conflict Handling Failures (AP-3, AP-11, AP-12)

These anti-patterns involve failure in the three-tier conflict-handling protocol. AP-3 (Silent Conflict Collapse) removes conflict from the governance record before the three-tier protocol can operate on it. AP-11 (Unresponsive Escalation) allows the escalation tier to stall without resolution. AP-12 (Informal Resolution Rules) allows the resolve tier to operate on informal understanding rather than authored substrate rules. Together they cover failure at entry to the protocol (AP-3), at the top tier of the protocol (AP-11), and in the authored logic that drives the protocol (AP-12).

### Category 3: Evolution Feed Attribution Failures (AP-4, AP-5)

These anti-patterns involve failure in the attribution of FAI-origin content as it enters participating Selves' home substrates through the four-locus evolution feed. AP-4 (Automatic DNA Absorption) allows FAI-origin content to enter home DNA without directed selection authorization. AP-5 (Non-Attributed Ingestion) allows FAI-origin action-layer records to enter without provenance identifying their inter-Self origin. Both anti-patterns dissolve the governance boundary between what a Self generated itself and what it received through FAI participation.

### Category 4: Configuration Failures (AP-6, AP-9)

These anti-patterns involve failure in the configuration substrate that specifies FAI event parameters. AP-6 (Implicit Configuration) removes the configuration substrate entirely, allowing the event to operate on infrastructure defaults. AP-9 (Pseudo-Selective Merge) allows a selective merge configuration to exist nominally while the selection decisions that make it selective are absent. Both anti-patterns produce a gap between the governance record and the actual operation of the event.

### Category 5: Perimeter and Boundary Integrity Failures (AP-7, AP-8, AP-10)

These anti-patterns involve failure at the perimeters and content boundaries that the shared substrate must respect. AP-7 (Home Perimeter Erosion) allows FAI participation to degrade home governance authority. AP-8 (Exchange Bounding Violation) allows content that should not cross inter-Self boundaries — instinct-layer content, LLM weights — to be present in the shared substrate. AP-10 (Shallow-Reference Merge) allows provenance references to nominally satisfy the bidirectional traceability requirement without enabling actual navigation. All three anti-patterns involve boundary commitments that appear satisfied in form while failing in substance.

---

## 4. Operational Tests

For each anti-pattern, one binary governance check detects its presence. A check that fails (answer: No) confirms the anti-pattern is instantiated.

| AP | Anti-Pattern | Operational Test |
|----|-------------|-----------------|
| AP-1 | Ungoverned Construction | Does a pre-construction authorization record authored by all participating Selves' governance structures exist as substrate content, dated before the FAI event commenced? |
| AP-2 | Ungoverned Dissolution | Does a dissolution record exist as substrate content, with a persistence policy execution record and hand-off boundary activation records authored at dissolution time? |
| AP-3 | Silent Conflict Collapse | Are all conflicts detected during merge present in the shared substrate's conflict registry as first-class objects, with neither side discarded without a registry entry? |
| AP-4 | Automatic DNA Absorption | Is every entry of FAI-origin content into a participating Self's home DNA layer traceable to a directed selection event with a home governance authorization record? |
| AP-5 | Non-Attributed Ingestion | Do all FAI-origin action-layer records in participating Selves' home substrates carry provenance metadata naming the shared substrate and the contributing Self? |
| AP-6 | Implicit Configuration | Does an authored configuration substrate exist for this FAI event, specifying all six configurable dimensions as human-authorized substrate content? |
| AP-7 | Home Perimeter Erosion | Is each participating Self's home DNA unchanged except through the governed evolution feed pathways, and is each Self's home governance authority over its own substrate undiminished by FAI participation? |
| AP-8 | Exchange Bounding Violation | Is the shared substrate free of instinct-layer content and LLM weight representations, containing only DNA-layer and action-layer substrate content from contributing Selves? |
| AP-9 | Pseudo-Selective Merge | Does a governance record of explicit selection decisions exist for every inclusion and exclusion of content in a claimed selective merge, with each decision traceable to human authorization? |
| AP-10 | Shallow-Reference Merge | Can provenance references in the merged substrate be navigated to the specific home governance records for each contributing Self's contributed content? |
| AP-11 | Unresponsive Escalation | Has every conflict in ESCALATED status received either a human governance response or a triggered default action within the timeframe specified in the configuration substrate? |
| AP-12 | Informal Resolution Rules | Are all conflict resolution rules governing this FAI event authored as orchestration rule content within the shared substrate, with no conflict resolution logic left to informal understanding? |

---

## 5. Relation to Phase D3

D2.19 names the twelve anti-patterns and organizes them into five taxonomy categories. Phase D3 develops each anti-pattern to standalone depth, with the same Form-1/Form-2 variant structure Series B anti-pattern notes use in the B3.xx range. The five D3 sub-phases correspond to the five taxonomy categories:

- D3.01–D3.xx: Lifecycle governance failures (AP-1, AP-2 and their variants)
- D3.xx–D3.xx: Conflict handling failures (AP-3, AP-11, AP-12 and their variants)
- D3.xx–D3.xx: Evolution feed attribution failures (AP-4, AP-5 and their variants)
- D3.xx–D3.xx: Configuration failures (AP-6, AP-9 and their variants)
- D3.xx–D3.xx: Perimeter and boundary integrity failures (AP-7, AP-8, AP-10 and their variants)

D2.19 is the parent note for all D3 anti-pattern work. D3 notes should cite D2.19 as the source of their named anti-pattern and taxonomy assignment, and should refer back to the Paper 2 intra-Self analog where one is named above.

---

## 6. Conclusion

Twelve FAI event anti-patterns are named and formalized as public prior art. The taxonomy (Lifecycle, Conflict Handling, Evolution Feed, Configuration, Perimeter Integrity) provides the scaffold for Phase D3 standalone development. The Paper 2 analog connections for AP-1, AP-2, and AP-3 complete the inheritance chain from intra-Self governance failure modes (B3.08, B3.10, B3.11) to their inter-Self counterparts, establishing that the architecture's awareness of these failure modes predates any subsequent attempt to claim them as novel governance problems. The twelve binary operational tests provide the detection instrument for each anti-pattern.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Twelve FAI Event Anti-Patterns.* May 15, 2026. ORCID: 0009-0004-8065-3235.
