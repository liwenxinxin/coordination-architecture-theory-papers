# AP-22: Black Box Shared Substrate

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** D3 — Paper 3 Anti-Pattern Formalizations
**Note ID:** D3.23 (#598)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

A black box shared substrate is a shared substrate in which governance decisions occur — conflicts are routed and resolved, evolution feed outputs are determined, configuration takes effect — but the decisions cannot be traced to specific authored governance content. An independent observer can confirm that activity happened, but cannot identify which authored rule governed it, which authored configuration determined it, or which authored orchestration logic authorized it. This is not a matter of governance quality: records that are present but poor describe AP-21 (governance theater). AP-22 names the more severe condition in which the tracing path does not exist at all — governance decisions were made, but no authored governance content made them. The shared substrate is a governance black box: inputs go in, outputs come out, and the connection between them is opaque. This note formalizes AP-22 using the seven-element Phase D3 structure: anti-pattern name and category, description, detection criteria, governance commitment violated, consequences, intra-Self analog, and resolution.

---

## 1. Anti-Pattern Name and Category

**AP-22: Black Box Shared Substrate**

**Category:** Taxonomy Category 6 — Governance Quality Failures (second of four).

AP-22 is the second Category 6 anti-pattern and the most severe. Category 6 anti-patterns concern the quality of governance that nominally exists: the shared substrate functions as an operational artifact and records show that governance decisions were made, but the governance itself is deficient in ways that undermine the determinism contract and the human-governed commitment. Within Category 6, the four anti-patterns form a severity gradient. AP-22 occupies the highest severity position: not deficient governance records, but an absence of any governance record to which decisions can be traced.

The distinction from AP-21 (governance theater, the first Category 6 anti-pattern) is structural and categorical, not merely a matter of degree. AP-21 describes a shared substrate where governance records exist and are linked to governance decisions, but the records fail quality standards — rationale entries are placeholders, routing rules are boilerplate catch-alls that do not actually discriminate between cases, resolution logs are present but uninformative. In AP-21, the governance artifact exists; it is simply inadequate. Repair requires improving the content of existing records. In AP-22, no such artifact exists as a traceable basis for governance decisions. The decisions were made — the conflict registry shows resolved entries, the evolution feed produced outputs — but no authored orchestration rule, authored configuration, or authored routing logic can be identified as the governing basis for those decisions. Repair requires creating governance content that does not exist, not improving content that is poor. AP-21 is governance appearance; AP-22 is governance absence.

---

## 2. Description

A shared substrate operating as a Full Aspect Integration (FAI) mechanism hosts governance decisions across three dimensions. First, conflicts surfaced during FAI events are routed and resolved through the shared substrate's conflict-handling tiers; the routing decision (which tier applies) and the resolution decision (what the outcome is) are each governance acts that must trace to authored orchestration rules under joint authority across participating Selves' governance. Second, evolution feed outputs are determined at dissolution through a configured eligibility scope; the determination of what content is eligible to flow through the hand-off boundary is a governance act that must trace to authored configuration expressing the scope. Third, configuration itself — the six dimensions of FAI configuration that Paper 3 specifies — takes effect as substrate content authored under joint authority; the configuration decisions must trace to substrate content that was authored by humans acting within their governance authority.

A black box shared substrate is one where one or more of these tracing paths is absent. An observer examining the substrate after a FAI event can confirm that the conflict registry shows RESOLVED entries, that the hand-off boundary produced evolution outputs, that configuration effects are visible in the substrate's behavior — but cannot follow the chain: this resolution happened because this authored rule governed this conflict class under this configuration. The tracing path is missing. The governance decision happened, but not through authored governance content.

This is distinct from cases where records are present but inadequate (AP-21), where tracing is technically possible but difficult (a quality failure, not an absence), or where records were destroyed after the fact (a record-keeping failure, not a structural one). AP-22 describes a substrate that was never governed by authored content for the decisions it made — not a substrate that lost its governance records. The black box condition is architectural: the substrate was configured, operated, and produced outputs without authored governance content determining what happened.

The most consequential form of AP-22 arises when an LLM operating within the shared substrate makes governance decisions without traceable orchestration rules authorizing what it was permitted to do. The AI-as-mediator commitment (Paper 1, Claim 4, Property B) specifies that an LLM operating on substrate content does so under authored orchestration rules that define the scope of its authorized action. When those rules are absent or untraceable, the LLM is not executing a human-authorized delegation. It is making autonomous decisions about governance-relevant substrate content — routing conflicts, determining eligibility, shaping resolution outcomes — without any authored basis authorizing those decisions. The black box condition is the operational state where AI autonomy has replaced AI governance at inter-Self scope. The substrate has not failed to implement a mediator; it has replaced a governed mediator with an unconstrained actor.

---

## 3. Detection Criteria

AP-22 is detected by applying the five determinism requirements from D2.66 and examining whether each can be satisfied from substrate content alone. A black box shared substrate fails one or more requirements and the failure cannot be remedied by examining substrate content, because the content needed to satisfy the requirement was never authored.

**Configuration completeness fails** when the six FAI configuration dimensions are not expressed as authored substrate content. If a governance participant cannot identify authored substrate content specifying participant scope, exchange scope, conflict-handling policy, evolution feed eligibility, amendment authority, and dissolution conditions, the configuration was not governed by authored content — it operated as an implicit default, a runtime decision, or an LLM-generated parameter outside the governance record.

**Conflict routing reproducibility fails** when conflict registry entries carry RESOLVED status but no authored routing rule can be identified that governed the routing decision. The conflict class was classified, a tier was selected, a routing outcome was produced — but the rule that produced it is not in the substrate as authored governance content. A second observer examining the substrate cannot identify which rule would govern an identical conflict class in a future FAI event.

**Resolution reproducibility fails** when the resolution outcome in a conflict registry entry cannot be traced to an authored orchestration rule specifying what the resolution should be for the conflict class under the prevailing configuration. The resolution happened, but the governance basis for it is absent.

**Evolution feed reproducibility fails** when evolution outputs at dissolution cannot be traced to a configured eligibility scope. Content flowed through the hand-off boundary, but no authored configuration can be identified that specified what was eligible to flow — and therefore a second observer cannot confirm that the flow was governed by any authored governance decision.

**Amendment reproducibility fails** when configuration changes cannot be traced through a version history of authored substrate content. The configuration changed between FAI events, but the change is not recorded as an authored amendment to substrate content under joint authority.

Two co-occurrence patterns should trigger heightened AP-22 suspicion during diagnosis. When AP-12 (informal resolution rules) is present — meaning conflict resolution rules exist in participant representatives' shared understanding rather than as authored substrate content — the conflict routing and resolution reproducibility requirements will fail structurally. When AP-6 (implicit configuration) is present — meaning FAI configuration exists as an implied shared understanding rather than as authored substrate content — the configuration completeness and evolution feed reproducibility requirements will fail structurally. The combination of AP-12 and AP-6 acting together produces AP-22 by construction: no authored rules governing conflict handling plus no authored configuration governing evolution eligibility leaves the shared substrate without any authored governance basis for the decisions it makes. Practitioners diagnosing AP-22 should therefore trace backward to AP-12 and AP-6 as probable root causes, and should expect to find both when AP-22 is present in severe form.

---

## 4. Governance Commitment Violated

**Primary: The determinism contract (D2.66 / Paper 1, §4.1, §11.3).**

The determinism contract requires that governance decisions made in the shared substrate be reproducible from substrate content alone. Five guarantees compose the contract: read determinism, write determinism modulo LLM, write addressability, conflict preservation, and substrate as source of truth. A black box shared substrate fails the contract for every governance decision it makes. Write addressability fails because governance decisions cannot be traced to an authored origin. Conflict preservation fails because resolutions cannot be confirmed as the product of human authority or human-authored orchestration rules. Substrate as source of truth fails because the answers to what happened, under what governance basis, and why cannot be derived from substrate content — they are either nowhere or in LLM context, agent memory, or participant representatives' tacit understanding, none of which the contract covers.

The contract failure is not partial. A substrate that fails the determinism contract for its governance decisions is not operating as a governed shared substrate in the CKS sense. It may be a useful coordination artifact for other purposes, but it cannot be called a CKS-coherent shared substrate, because the determinism contract is a constitutive commitment of the CKS pattern.

**Secondary: AI-as-mediator Property B (Paper 1, Claim 4).**

Property B of the AI-as-mediator commitment specifies that an LLM operating on substrate content writes to the substrate under orchestration rules that are themselves substrate content. When the shared substrate is a black box and the LLM operating within it makes governance-relevant decisions without traceable orchestration rules, Property B is violated. The LLM is not operating as a governed mediator executing an authored delegation; it is operating as an autonomous actor whose outputs enter the substrate without governance authorization. This is the precise condition the AI-as-mediator commitment is designed to prevent. At inter-Self scope, the stakes of this violation are amplified: the autonomous LLM is not making decisions about content within a single Self's governance perimeter, but decisions that affect what multiple Selves ingest through the evolution feed and how conflicts between them are resolved.

**Tertiary: Human-governed authority — the three rights (Paper 1, Claim 3).**

The three governance rights — inspect, modify, override — require that governance can be exercised meaningfully by humans. A black box shared substrate does not provide anything meaningful for the inspect right to operate over. A human exercising the inspect right can confirm that activity occurred (the conflict registry shows entries, the evolution feed produced outputs), but cannot inspect the governance logic that produced those outcomes, because no authored governance content instantiates that logic. The right to inspect is preserved in form but hollowed in substance: there is nothing in the substrate that constitutes the governance record the inspect right is designed to surface. Modification and override are similarly affected — humans cannot modify or override governance content that does not exist as authored substrate content.

---

## 5. Consequences

**The FAI event is not compliant.** Without satisfying the determinism contract, the shared substrate is not functioning as a governed shared substrate for the FAI event in question. The event may have produced outputs — evolution feed content, resolved conflicts, configuration effects — but those outputs are not the product of a Paper 3-compliant governance process. Contributing Selves cannot represent to their own home governance structures that the FAI event was conducted under authored governance.

**Every governance decision made in the black box is effectively ungoverned.** Not ungoverned in the colloquial sense of proceeding without attention or care, but ungoverned in the architectural sense: no authored governance content authorized what happened. The decisions fall outside the governance record entirely. A compliance audit of the shared substrate would find activity without authorization, in the same sense that a financial audit would find expenditures without approved purchase orders. The problem is not that the decisions were wrong; it is that there is no basis on which to confirm or deny that they were right.

**Post-event disputes are unresolvable.** When a contributing Self disputes the resolution of a conflict that affected content it contributed — or disputes that the evolution feed outputs it received were consistent with the FAI event's governing scope — there are no governance records to consult. The conflict registry shows that a resolution occurred; it does not show the rule that governed it or the configuration under which it was made. The dispute cannot be resolved by examining the substrate, because the information needed to resolve it was never authored into the substrate. D2.45's dispute-resolution mechanism, which requires that disputes be adjudicable from substrate content, is inapplicable: the substrate does not carry the content the mechanism requires.

**Contributing Selves cannot verify governance of their contributions.** Each participating Self's home governance structure has an obligation to ensure that content contributed through FAI events was handled according to an authored governance specification. In a black box shared substrate, no such verification is possible. The Self's governance can confirm that content was contributed and that something was received in return through the evolution feed, but cannot confirm what governance logic determined how the contribution was handled. Cross-organizational governance trust cannot be established or maintained with a black box partner, because trust requires the ability to inspect the governance basis for decisions — and that basis does not exist.

**The severity of AI autonomy at inter-Self scope is compounded.** When the black box condition results from an LLM making governance decisions without authored orchestration rules, the AI autonomy problem is not confined to a single Self's internal operations. The autonomous LLM is determining what content multiple distinct Selves ingest through their evolution machinery, and how conflicts between content from those Selves are resolved. These are decisions with organizational and evolutionary consequences that extend beyond the FAI event itself. The absence of authored rules governing LLM behavior in this context means that the LLM's judgment — unconstrained by authored governance — is shaping the post-FAI trajectory of multiple distinct governed systems.

---

## 6. Intra-Self Analog

The black box condition at inter-Self scope mirrors the same failure at intra-Self scope, which Paper 1 formalizes as the constitutive commitment against non-addressable substrate writes and silent conflict resolution.

Within a single Self, the determinism contract applies to every cell's operation over the substrate. A cell that permits an LLM to make content decisions without authored orchestration rules governing what the LLM is authorized to do produces substrate writes that cannot be traced to an authored origin — non-addressable writes in the contract's terminology. Conflicts silently collapsed by LLM operations without a recorded resolution decision violate the conflict-preservation guarantee. Content derived from LLM context rather than substrate state violates the source-of-truth guarantee. A single Self whose substrate exhibits these patterns is operating with a black box at intra-Self scope: governance decisions about substrate content are being made, but no authored governance content is making them.

Black box shared substrate is the inter-Self extension of this same failure. The architectural commitment violated is identical — governance decisions must trace to authored substrate content — but the scope is enlarged from a single Self's governance perimeter to a shared substrate that spans multiple Selves' governance perimeters under joint authority. The consequences of the failure are also enlarged proportionally: where an intra-Self black box affects a single Self's substrate integrity, an inter-Self black box affects the governance integrity of every contributing Self's evolution outputs and every conflict resolution that crossed organizational boundaries.

This parallel is instructive for practitioners inheriting the AP-22 diagnosis. The intra-Self version of the black box condition is the more familiar failure mode; teams that have encountered it within their own substrate operations will recognize the same structural signature at inter-Self scope. The difference is not the nature of the failure but the number of governance perimeters it crosses and the multiplied difficulty of repair when the authored governance content must be jointly produced under authority arrangements that span organizational boundaries.

---

## 7. Resolution

The complete prevention of AP-22 requires satisfying all five determinism requirements from D2.66. None of the five is optional; a substrate that satisfies four of five is not a governed shared substrate for the governance decisions covered by the requirement it fails.

**Requirement 1 — Configuration completeness.** All six FAI configuration dimensions must be expressed as authored substrate content under joint authority across participating Selves' governance before the FAI event begins. Participant scope, exchange scope, conflict-handling policy, evolution feed eligibility, amendment authority, and dissolution conditions are each a governance dimension; each must exist as authored substrate content, not as implied agreement, runtime default, or LLM-generated parameter. Configuration completeness is the prerequisite for all other requirements: without an authored configuration, the scope within which routing rules and resolution rules operate is itself ungoverned.

**Requirement 2 — Conflict routing reproducibility.** Every routing decision — which conflict-handling tier applies to which conflict class — must be traceable to an authored routing rule that is itself substrate content under joint authority. The routing rule specifies the conditions under which each tier applies and is authored before conflicts arise, not created in response to a specific conflict instance. A second observer examining the substrate after the FAI event must be able to identify the routing rule and confirm that the routing decision was consistent with it.

**Requirement 3 — Resolution reproducibility.** Every resolution outcome must be traceable to an authored orchestration rule specifying what the resolution is for the conflict class under the prevailing configuration. Resolution rules are substrate content authored under joint authority; they determine outcomes for defined conflict classes in advance, not on an ad hoc basis. An LLM operating to implement a resolution is executing an authored delegation under an authored rule — not making a governance decision itself.

**Requirement 4 — Evolution feed reproducibility.** Every evolution output at dissolution must be traceable to a configured eligibility scope that is itself authored substrate content. What was eligible to flow through the hand-off boundary, what layer-routing rule governed where it went within each receiving Self's evolution machinery, and what asymmetry in ingestion was authorized by each home perimeter's governance — each of these must exist as authored configuration, not as an implicit or emergent property of the FAI event.

**Requirement 5 — Amendment reproducibility.** Every configuration change between FAI events must be traceable through a version history of authored substrate content. The version history is itself substrate content under joint authority; amendment authority specifies who is authorized to make changes and under what conditions. A configuration change that cannot be traced to an authorized amendment is a black box change — even if the resulting configuration is authored, the change process was not.

When AP-12 and AP-6 are identified as root causes of AP-22, resolution requires addressing all three anti-patterns in the correct order: AP-6 first (author the configuration as substrate content), then AP-12 (author the resolution rules as substrate content), and confirm that AP-22 is resolved only after all five determinism requirements can be satisfied from the authored substrate content. Resolving AP-12 alone, without addressing AP-6, leaves the evolution feed reproducibility requirement unmet. Resolving AP-6 alone, without addressing AP-12, leaves the conflict routing and resolution reproducibility requirements unmet. AP-22 is eliminated only when the authored configuration and authored rules together provide a complete governance basis for every governance decision the shared substrate makes.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-22: Black Box Shared Substrate.* May 15, 2026. ORCID: 0009-0004-8065-3235.
