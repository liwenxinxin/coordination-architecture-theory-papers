# AP-9: Pseudo-Selective Merge

**Series:** D3 — Anti-Pattern Formalizations (Paper 3)
**Note:** D3.14 (#589)
**Category:** Taxonomy Category 4 — Configuration Failures
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

Pseudo-Selective Merge (AP-9) is the ninth anti-pattern in the CKS derivation note series and the second of five Taxonomy Category 4 (Configuration Failures) anti-patterns. It describes a Full Aspect Integration (FAI) event whose configuration specifies the selective merge pattern variant but produces no governance selection decisions: content inclusion and exclusion from the shared substrate's merged state is determined by system defaults, filters, or automated criteria — not by governance authorization. The anti-pattern appears to use selective merge (the configuration says so, and the merged state may reflect exclusions) but the actual merge process is not governed by human selection decisions. This produces governance theater at the merge level: records suggest governance curation that did not occur. The primary governance commitment violated is Paper 1 Claim 3 — the modify right requires governance authorization, and selective merge is an exercise of the modify right over what enters the shared substrate's combined state; automated or default-driven exclusions are not governance exercises of the modify right. The secondary violation is Paper 3 Claim 5 — selection decisions in a selective merge are configuration content that must be authored by governance; not authoring them means they are implicit configuration. The resolution is D2.08's five-step selective merge governance protocol, particularly its content-review, selection-decision, and selection-record steps; when governance capacity cannot support those steps, the correct response is to switch to full merge rather than to run pseudo-selective merge without governance.

---

## 1. Anti-Pattern Name and Category

**Anti-pattern:** AP-9 — Pseudo-Selective Merge
**Category:** Taxonomy Category 4 — Configuration Failures

Taxonomy Category 4 covers FAI events whose configuration specifies a pattern variant but whose execution does not fulfill the governance requirements that pattern variant entails. The configuration choice is not wrong in itself; what is wrong is the gap between what the configuration declares and what governance actually does. AP-8 opened Category 4 by formalizing an analogous failure at a different pattern variant. AP-9 addresses the same structural gap — declared governance that does not materialize — applied specifically to selective merge, the pattern variant whose governance requirements are most demanding and therefore most susceptible to nominal compliance without substantive exercise.

---

## 2. Description

A Full Aspect Integration event specifies the selective merge pattern (D1.09 Pattern Variant 2) in its configuration. Selective merge is the most governance-intensive of the three FAI pattern variants: it requires governance practitioners to review contributed content, make explicit include, exclude, or hold decisions for each content category, and record those decisions as substrate content with governance authorization. The pattern produces a shared substrate whose merged state reflects deliberate curation — content is present because governance decided it should be present, and content is absent because governance decided it should be absent, with the reasoning recorded and inspectable.

Pseudo-Selective Merge is the failure mode in which the configuration specifies selective merge but the governance requirements are not fulfilled. No governance review of contributed content occurs at Step 2. No include, exclude, or hold decisions are made by authorized governance practitioners at Step 3. No selection record is authored and stored as substrate content at Step 4. The merged state reflects some exclusions — perhaps all content from one contributing Self, or all content of a particular structural type — but those exclusions were determined by system defaults, automated filters, or implicit criteria, not by governance.

The external appearance is of a governed selective merge: the configuration says selective merge, and the merged state is not a simple union of all contributed content. The substance is implicit configuration (AP-6) applied to merge content — the system's defaults and filters are doing the curation work that governance was supposed to do. The form is selective merge; the substance is ungoverned exclusion operating beneath a governance label. AP-9 is AP-6 (implicit configuration) instantiated specifically at the merge operation, compounded by the additional misdirection that the selective merge label actively signals governance authority that was never exercised.

---

## 3. Detection Criteria

A FAI event instantiates AP-9 if any of the following conditions holds:

- The FAI configuration specifies the selective merge pattern but no selection decision records (D2.08 Step 3) exist — no include, exclude, or hold decisions with governance authorization are present in the substrate for the relevant event.
- The shared substrate's merged state reflects content exclusions, but no governance records document which governance authority made the exclusion decisions and why.
- Content exclusion appears systematic or filter-based — for example, all content from one contributing Self is absent from the merged state, or all content of a particular structural type is absent — without governance reasoning records explaining the exclusion scope and its authorization.
- The selection record (D2.08 Step 4) is absent or contains only system-generated entries without governance authorization.

Detection requires examining both the configuration layer (which pattern variant is declared) and the governance record layer (what selection decisions are recorded as substrate content). A discrepancy between a declared selective merge and an absent or unauthorized selection record is the diagnostic signature of AP-9. A configuration that specifies selective merge alongside a selection record that was generated by system logic rather than authored by governance practitioners satisfies the detection criterion even if entries appear in the record field — the test is governance authorization, not the presence of entries.

---

## 4. Governance Commitment Violated

**Primary violation — Paper 1 Claim 3 (human-governed authority, modify right):**

The modify right requires governance authorization. Selective merge is an exercise of the modify right over what enters the shared substrate's combined state: to exclude a content category from the merged state is to modify what the shared substrate contains, and that modification must be authorized by governance. Automated or default-driven exclusions are not governance exercises of the modify right. They are system operations that produce the same surface effect as governed exclusions — content is absent — without the governance act that gives the absence its authority and its traceability.

A system that allows filters or defaults to determine merge content while labeling the process "selective merge" treats governance authorization as optional decoration on a system-driven outcome. The modify right is not decoration; it is the architectural commitment that distinguishes governed modification from ungoverned system behavior. Paper 1 Claim 3 does not permit the label to substitute for the exercise.

**Secondary violation — Paper 3 Claim 5 (configuration as substrate content):**

The selection decisions in a selective merge are configuration content: they specify which content enters the shared substrate's merged state and which does not. Paper 3 Claim 5 commits to configuration as substrate content — authored by governance, held in the substrate, inspectable and modifiable under the three rights. In AP-9, the selection decisions are not authored at all; they are implicit in system behavior. Implicit configuration is not substrate content. It cannot be inspected, modified, or overridden as substrate content because it has no substrate representation. Not authoring the selection decisions means the effective configuration of the merge is held in system defaults rather than in the substrate — a Claim 5 violation of the same class as AP-6, applied at the merge configuration register.

**Operational reference — D2.08 (selective merge governance protocol):**

D2.08 specifies a five-step protocol for governed selective merge. AP-9 executes Step 1 (configuration) and Step 5 (merge completion) while bypassing Steps 2, 3, and 4 — the three governance steps. The five-step protocol is not administrative process layered around an otherwise technical operation; Steps 2, 3, and 4 are the mechanism by which the modify right is exercised at merge scope and by which the selection decisions become substrate content. Bypassing them produces a merge that looks governed and is not.

---

## 5. Consequences

**Governance theater at the merge level.** AP-9 produces the appearance of governance curation without the substance (D2.36). Records indicate that a selective merge was configured; the merged state shows that not everything contributed was included. But no governance authority actually curated what was included or excluded. Future governance, auditors, and participating Selves' oversight structures face a substrate state that signals more governance authority than was exercised — the most damaging variety of governance theater because it is the merged state itself, the primary output of the FAI event, that carries the false signal.

**Excluded content is permanently lost without governance reasoning.** In governed selective merge, exclusion decisions are authored as substrate content (D2.08 Step 4 selection record). Future governance can examine whether the exclusions were appropriate, revisit them in light of changed circumstances, or restore excluded content to a subsequent merge. In AP-9, no exclusion reasoning exists as substrate content. The content is absent from the shared substrate's merged state, and no substrate record explains why. Future governance cannot evaluate whether systematic exclusions were appropriate or mistaken — the decision-making that produced the absences left no trace in the substrate, and the content excluded is not recoverable from the merged state.

**The determinism contract fails for the merge result.** D2.66 commits to the determinism contract: the logic that produced a substrate state must be traceable from authored governance records. In AP-9, the selection logic is held in system defaults or filters that are not substrate content. The merge result cannot be traced from authored records. The determinism contract fails at merge scope, meaning no future observer can reconstruct from the substrate why the merged state has the shape it has.

**Process disputes become unresolvable.** If a participating Self disputes why its contributed content was excluded from the merged state, or if governance later questions the curation of a historical merge, there are no governance selection records from which to reconstruct the decision. D2.45 process disputes about content exclusion are permanently unresolvable because the decision-making infrastructure that would resolve them — the selection record with attributed governance authorization — was never instantiated.

**The modify right has no authored object to operate on.** Governance's ability to review, revise, or override selection decisions presupposes that the selection decisions exist as substrate content. In AP-9 they do not. Even if governance later wishes to correct the exclusions that system defaults produced, there is no selection record to modify or override. The modify right is impotent not because it has been blocked but because AP-9 failed to create the substrate content over which the right would operate.

---

## 6. Intra-Self Analog

The intra-Self analog of AP-9 is a Paper 2 selective-merge mating event that claims to use selective merge but produces offspring with some parent rules excluded based on system defaults rather than governance selection decisions. The configuration declares selective merge mating; the offspring's substrate reflects content from one or both parents as absent; but no governance authority made and recorded the selection decisions. The selection logic is implicit in system behavior, not explicit in substrate content.

The intra-Self analog makes clear that AP-9 is not a failure mode introduced by the inter-Self perimeter. The modify-right violation and the implicit-configuration violation occur wherever selective merge is declared without governance selection decisions — within a single Self's mating events as much as across the inter-Self boundary. The inter-Self context of Paper 3's FAI mechanism amplifies the consequences (the merged state reflects contributions from governance-distinct Selves, and each Self's governance structure has standing to question the curation of its contributed content) but does not create the failure mode. The failure mode is structural: declared selective merge without Steps 2, 3, and 4 of the governance protocol, at any scope.

---

## 7. Resolution

The complete prevention for AP-9 is D2.08's five-step selective merge governance protocol, with particular attention to the three steps that AP-9 bypasses.

**Step 2 — Content review.** Governance practitioners must actually review the content contributed by each participating Self before the merge proceeds. This is not a formality to be satisfied by acknowledging that contributions were received; it is substantive engagement with the content, sufficient to support informed selection decisions at Step 3. Automated pre-filtering applied before governance review converts Step 2 into a pseudo-review of pre-filtered content, which reproduces the AP-9 failure at a finer level of nesting.

**Step 3 — Selection decisions.** Explicit include, exclude, or hold decisions must be made by authorized governance practitioners for each content category. The decisions must carry governance authorization — they must be attributable to a governance authority with the modify right over the shared substrate. Decisions produced by system logic, even logic that governance configured at an earlier time, are not Step 3 decisions. The step requires a present governance act, not a past configuration that has downstream automated effects.

**Step 4 — Selection record.** The Step 3 decisions must be recorded as substrate content with governance authorization. The selection record is what makes the merge result traceable, what gives future governance something to review, what satisfies the determinism contract for the merged state, and what creates the substrate content over which the modify right can later be exercised if governance wishes to revisit the curation.

**When governance capacity cannot support these steps, switch to full merge.** This is the most important resolution guidance for teams facing conditions that would otherwise produce AP-9. Selective merge requires governance work at merge time that full merge does not: content review, per-category decisions, and a selection record authored as substrate content. If governance capacity — available practitioner time, the scope of content categories to be reviewed, the timeline of the FAI event — cannot support Steps 2, 3, and 4, the correct governance response is to configure the event as full merge (D1.08, the architectural default for FAI) rather than to declare selective merge and skip the governance steps.

Full merge with conflicts surfacing as first-class substrate state is more architecturally honest than pseudo-selective merge without governance decisions. Full merge produces a shared substrate in which all contributed content is present and conflicts are addressable through the three-tier conflict-handling mechanism (D1.13–D1.16) under governance authority. The conflict density may be higher than a well-executed selective merge would produce — that is the tradeoff the selective merge pattern variant exists to manage. But the governance posture of full merge is sound: nothing is excluded without governance reasoning, all contributed content is present and inspectable, and conflicts are explicit substrate state rather than silent absences. Pseudo-selective merge produces a cleaner-looking merged state whose cleanliness is an artifact of ungoverned exclusion. Governance should prefer the honest higher-conflict-density result of full merge over the misleadingly curated appearance of AP-9.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-9: Pseudo-Selective Merge.* May 15, 2026. ORCID: 0009-0004-8065-3235.
