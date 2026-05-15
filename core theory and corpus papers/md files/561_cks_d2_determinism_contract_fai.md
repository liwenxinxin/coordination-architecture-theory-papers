# FAI and the Determinism Contract

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

Paper 1 of the CKS theory series establishes a determinism contract over the substrate: governance decisions are reproducible from the substrate's governance records, and an independent reader with access to those records can verify every governance outcome without requiring information held outside the substrate. Note D2.66 formalizes how this contract holds at inter-Self scope within a shared substrate during a Full Aspect Integration (FAI) event. The inter-Self scope introduces a condition Paper 1's intra-Self treatment does not address: the governance records that must be sufficient for reproducibility now span contributed content from distinct organizational Selves, a shared FAI configuration authored under joint authority, a conflict registry produced by inter-Self conflict surfacing, and authorization records governing the event itself. D2.66 states five reproducibility requirements the determinism contract imposes on FAI governance records — configuration completeness, conflict routing reproducibility, resolution reproducibility, evolution feed reproducibility, and amendment reproducibility — and establishes that satisfying all five is what makes a FAI event auditable in the sense D2.63 defines. The note also formalizes the cross-organizational dimension of determinism unique to inter-Self scope: contributing Selves can verify that their contributed content was treated as the shared governance records specify, a verification right that exists only when the contract holds. The note closes by naming the black box shared substrate as the determinism anti-pattern and providing an operational test.

## 1. D2.66 as operational decomposition of D1.02

D2.66 is an operational decomposition of D1.02, which states that all six Paper 1 architectural commitments hold within the shared substrate at inter-Self scope. Among those six commitments, the determinism contract is the one that directly conditions auditability: it specifies what the governance records must contain and how they must be structured so that governance decisions are reproducible from those records alone. D2.66 makes this requirement concrete at the inter-Self scope that FAI events occupy.

Paper 1's determinism contract binds the *representation layer* of the substrate — what is recorded, how it is addressable, and whether conflicts are preserved or silently collapsed. The contract does not bind LLM outputs, which are non-deterministic by nature; it binds what gets written to the substrate under orchestration rules. The same scope applies within the shared substrate: the determinism contract binds what enters the shared substrate's governance records during a FAI event, not what intermediate text any LLM produces in the course of operating over that substrate.

At intra-Self scope, the contract is satisfied when one governance authority can read its own substrate and reproduce its own decisions. At inter-Self scope, the contract must be satisfied across a substrate constructed for a specific event, spanning contributed content from distinct Selves governed by distinct home authorities, under a configuration authored jointly. This is a strictly larger scope than Paper 1 addresses. The five requirements this note derives are what Paper 1's determinism contract produces when it is applied at that larger scope.

## 2. The determinism contract at inter-Self scope

Within a shared substrate, the determinism contract holds if and only if the following condition is satisfied: an independent observer — one who has access to the shared-substrate governance records and no other information — can reproduce every governance decision the shared substrate produced during the FAI event.

The governance records that must be sufficient for this reproduction are four classes of substrate content:

**(a) Contributed aspect content.** What each participating Self contributed — the aspects surfaced, their constituent cells, their DNA-layer and action-layer content. This is the raw material over which governance operated.

**(b) The FAI configuration.** The authored configuration specifying how the event was governed: which aspects each Self contributed, which orchestration rules applied within the shared substrate, how conflict routing was determined, what the persistence policy was, and what evolution feed eligibility scope applied at dissolution.

**(c) The conflict registry.** The record of conflicts surfaced during the event: what conflicted, which tier was selected for each conflict, what resolution was applied or escalated where applicable, and the provenance of each routing and resolution decision.

**(d) The governance authorization records.** Who held what authority during the event, what amendments to the configuration were authorized, and the authorization chain for each governance act.

When these four classes are complete and internally consistent, the shared substrate satisfies the determinism contract at inter-Self scope. When any class is incomplete, opaque, or missing, the contract fails at that gap. Reproducibility is only as strong as the completeness of all four.

## 3. Five reproducibility requirements

The determinism contract at inter-Self scope decomposes into five specific reproducibility requirements. Each addresses a distinct class of governance decision that must be traceable from the shared-substrate records.

**Requirement 1 — Configuration completeness.** The FAI configuration must be complete and recorded as substrate content. Configuration completeness means that an observer reading the configuration can determine every governance parameter that applied during the event: which aspects were contributed, what orchestration rules governed the shared substrate, how routing tiers were assigned, and what the persistence and evolution feed policies were. An incomplete configuration is one where some governance parameters applied during the event but were not recorded in the substrate — perhaps held in a separate policy file, in an LLM's context window, or in an informal agreement between participants. Any such gap makes governance decisions that depended on those parameters non-reproducible from the shared-substrate records. The configuration's role in the determinism contract is foundational: every other reproducibility requirement depends on a complete configuration being available.

**Requirement 2 — Conflict routing reproducibility.** For every conflict recorded in the conflict registry, the routing decision — which tier handled it — must be traceable to the authored routing rules in the configuration. An observer reading the routing rules and the conflict entry must be able to reproduce the routing decision: given this conflict class, the authored rules specified this tier. Routing reproducibility fails when the routing rules are not recorded as substrate content, when the conflict class is not identified in the registry entry, or when the connection between the authored rule and the routing outcome is not explicit. Silent routing — where conflicts are assigned to tiers by a process whose logic is not substrate content — violates this requirement regardless of whether the outcomes happened to be correct.

**Requirement 3 — Resolution reproducibility.** For every conflict handled at the orchestration tier — resolved by an authored orchestration rule rather than escalated to humans — the resolution must be traceable to the specific rule that fired. The conflict registry entry must identify the rule, and reading that rule must yield the resolution recorded. Resolution reproducibility fails when the resolution record does not identify which rule applied, when the applicable rule is not substrate content, or when the recorded resolution cannot be derived by reading the rule. This requirement has a specific scope: it applies only to the orchestration tier. Conflicts escalated to human authority are resolved by governance acts that are themselves authorization records — those fall under Requirement 5's amendment and authorization coverage, not under this requirement.

**Requirement 4 — Evolution feed reproducibility.** What content was eligible to enter each participating Self's home evolution machinery at dissolution must be traceable to the configured evolution feed eligibility scope. The FAI configuration specifies which content classes, from which aspects, were eligible to enter each Self's evolution mechanisms at dissolution; an observer reading the configuration should be able to reproduce what was eligible for each evolution locus. Evolution feed reproducibility fails when the eligibility scope is not recorded in the configuration, when what actually entered each Self's evolution machinery departed from the configured eligibility scope without recorded authorization, or when the layer-routing rule (DNA-layer content to DNA evolution; action-layer content to action-feedback evolution; instinct evolution receiving no FAI input) was applied inconsistently with the authored configuration. The asymmetric ingestion property — different Selves may absorb different content from the same event under their respective home governance — is admissible and does not violate this requirement, provided the asymmetry is configured and recorded.

**Requirement 5 — Amendment reproducibility.** Every amendment to the FAI configuration made during the event must be recorded with the prior value, the amended value, the authorization for the amendment, and the moment at which it took effect. An observer reading the amendment history must be able to reconstruct the effective configuration at any moment during the event. Amendment reproducibility is what makes the determinism contract hold across events that change their own configuration mid-execution — which is architecturally permitted under Paper 3's configuration-as-substrate-content commitment. Without amendment records, a time-slice of the event cannot be audited: the observer cannot determine which configuration was in effect at a given point, and governance decisions made under an amended configuration become non-reproducible from the records.

These five requirements are independent: a shared substrate can satisfy any subset and fail the others. The determinism contract requires all five.

## 4. Determinism as the foundation of FAI event auditability

FAI event auditability — the capacity for a qualified reviewer to assess the governance quality of a FAI event after it has occurred — depends directly on the determinism contract. An auditor who has access to the shared-substrate governance records but no other information must be able to verify governance decisions; if the records do not support that verification, the event is not auditable regardless of how well it was actually governed.

The relationship is causal in one direction: determinism is necessary for auditability. A FAI event that satisfies all five requirements gives an auditor a complete record from which to work. The auditor can read the configuration, trace every conflict routing decision to the authored routing rules, trace every orchestration-tier resolution to the rule that fired, verify that the evolution feed followed the configured eligibility scope, and reconstruct the configuration at any moment using the amendment history. Every governance decision is checkable, and checking does not require external information.

A FAI event that fails any of the five requirements produces a gap in the audit record. The auditor encountering that gap cannot verify the governance decision that depended on the missing or opaque record — and cannot know whether the decision was sound or unsound. The gap does not indicate failure; it indicates that the audit cannot be completed at that point. Auditability fails at the point where the determinism contract fails.

This asymmetry matters for implementation: a shared substrate that satisfies the determinism contract is not necessarily a well-governed substrate, but it is an auditable one. An auditor can evaluate governance quality in a determinism-compliant substrate. The evaluation may reveal governance failures. In a non-compliant substrate, even that evaluation is unavailable.

## 5. Cross-organizational determinism — the inter-Self dimension

At intra-Self scope, the determinism contract primarily serves one governance authority: the authority that governs the substrate can verify its own decisions. The verifying party and the governing party are the same entity.

At inter-Self scope, this symmetry breaks. The shared substrate is governed under joint authority, but the contributing Selves are organizationally distinct. Each contributing Self brings aspects from its own home substrate under its own home governance; what happens to those aspects within the shared substrate is governed by the FAI configuration under joint authority. A contributing Self has a legitimate interest in verifying how its contributed content was treated: whether it was included as configured, how conflicts involving its contributions were routed and resolved, and what entered its home evolution machinery at dissolution.

This cross-organizational verification right exists only when the determinism contract holds. When the shared substrate satisfies all five requirements, a contributing Self can read the governance records and verify the treatment of its contributions without requiring access to any other information — including the home substrates of the other participating Selves. The shared-substrate governance records are the complete and sufficient record of how each contribution was treated.

When the contract fails, this verification right fails with it. A contributing Self whose contributions enter a non-determinism-compliant shared substrate cannot verify how those contributions were governed. The contributing Self may have observable outputs — what entered its evolution machinery at dissolution — but cannot trace those outputs to the governance decisions that produced them. The shared substrate, from the contributing Self's perspective, is opaque.

Cross-organizational determinism is therefore not merely an auditability property at the level of an abstract reviewer. It is an operational property that determines whether each participating Self can trust the shared governance process. A shared substrate that satisfies the determinism contract makes the governance process legible to all contributing Selves simultaneously. A substrate that fails the contract makes the governance process legible to no one, including the joint authorities who configured it.

## 6. Anti-pattern: the black box shared substrate

The determinism anti-pattern at inter-Self scope is the **black box shared substrate** — a shared substrate where governance decisions occur but cannot be traced to specific authored governance content in the shared-substrate records.

The black box condition can arise in several forms. A shared substrate where the FAI configuration is not recorded as substrate content — where the governing parameters exist only in a policy engine, a contract document, or an LLM's context window — is a black box with respect to Requirement 1. Governance decisions were made, but the records do not support reproducing them.

A shared substrate where conflict routing is performed by a process whose logic is not authored substrate content is a black box with respect to Requirement 2. Conflicts were assigned to tiers, but the routing cannot be verified without access to information held outside the substrate.

A shared substrate where conflicts are resolved at the orchestration tier by a process that does not record which rule fired is a black box with respect to Requirement 3. Resolutions appear in the registry, but are not traceable to the governance content that produced them.

A shared substrate where the evolution feed at dissolution follows an eligibility scope that is not recorded in the configuration is a black box with respect to Requirement 4. Content entered each Self's home evolution machinery, but the eligibility basis is not recoverable from the records.

A shared substrate where configuration amendments during the event are not recorded with prior values and authorization is a black box with respect to Requirement 5. The effective configuration at any given moment cannot be reconstructed, and governance decisions made under amended configurations cannot be audited.

In each form, the black box condition is not produced by a deliberate policy of opacity. It typically arises when governance decisions are delegated to processes — automated pipelines, LLM-mediated rule application, runtime policy evaluation — that operate correctly but do not write their logic and decisions back to the shared substrate as addressable records. The substrate carries outcomes but not the governance lineage that produced them. The outcome of a black box substrate may look correct; what is lost is the capacity to verify that it is correct, and to verify it again in the future.

## 7. Operational test

A shared substrate satisfies the determinism contract at inter-Self scope if and only if all of the following are true at the close of the FAI event:

1. An independent observer with access to only the shared-substrate governance records — contributed aspect content, FAI configuration, conflict registry, and governance authorization records — can reproduce every conflict routing decision by reading the authored routing rules.

2. The same observer can reproduce every orchestration-tier conflict resolution by reading the orchestration rule identified in the resolution record.

3. The same observer can verify that what was eligible to enter each Self's home evolution machinery at dissolution matches the configured evolution feed eligibility scope.

4. The same observer can reconstruct the effective FAI configuration at any moment during the event by reading the configuration and the amendment history.

5. At no point in steps 1–4 does the observer require information held outside the shared-substrate governance records.

If any of these five conditions fails, the determinism contract fails at that point. Auditability of the FAI event fails at the same point. The failure is localizable: it corresponds to one of the five requirements, which in turn corresponds to one of the four classes of governance record that must be complete for the contract to hold.

The test does not require that every governance decision was correct — only that the records are sufficient for an independent observer to assess whether it was correct. Correctness is a governance quality question; the determinism contract addresses the prior question of whether governance quality can be assessed at all.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI and the Determinism Contract.* May 15, 2026. ORCID: 0009-0004-8065-3235.
