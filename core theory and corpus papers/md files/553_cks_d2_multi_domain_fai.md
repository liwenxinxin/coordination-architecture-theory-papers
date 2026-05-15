# FAI Governance for Multi-Domain Selves

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

A Self whose governance architecture spans multiple distinct content-domains — each covered by a different aspect — faces a structurally differentiated participation problem in Full Aspect Integration (FAI) events: not all aspects are relevant to all FAI partners, and contributing all aspects to all events is a governance failure mode, not a default. This note formalizes D2.58, an operational decomposition of D1.06 (aspect as FAI exchange unit) and D1.22 Dimension 1 (sharing scope as governance-configured parameter), applied to the multi-domain case. It shows that the sharing-scope configuration already present in Paper 3's architecture is the mechanism that enables domain-selective FAI participation — no new architecture is required. The note characterizes three governance properties that domain-selective participation produces (domain privacy, conflict prediction from domain compatibility, and domain-specific standing configurations), explains how a multi-domain Self organizes its FAI relationships as a portfolio organized by domain, identifies a home-synthesis opportunity available uniquely to multi-domain Selves, and states the anti-pattern — domain-indiscriminate sharing — that violates all three governance properties simultaneously. An operational test closes the note.

---

## 1. Position in the derivation series

D2.58 is an operational decomposition in Phase D2 of the Series D derivation notes. Its parent sub-commitments are D1.06 (aspect as the unit of exchange in FAI: when a Self contributes to the shared substrate, it contributes aspects, surfacing the constituent cells' DNA-layer and action-layer content) and D1.22 Dimension 1 (sharing scope: the governance-configured specification of which aspects a participating Self contributes to a given FAI event). A third inheritance is active: B2.16 from Paper 2's derivation series, which established content-domain as an authored governance specification for each aspect — the authored statement of what operational territory the aspect governs. D2.58 asks what happens when these three elements — exchange at aspect granularity, sharing scope as a configurable governance parameter, and content-domain as authored per-aspect specification — are composed in a Self whose aspects cover multiple distinct content-domains.

The answer is that the existing architecture already handles the multi-domain case cleanly. D2.58 does not introduce new mechanisms. It formalizes the governance implications of operating the existing architecture at a Self whose aspect portfolio is domain-differentiated.

---

## 2. The multi-domain scenario

Consider a Self — call it Self A — whose governance architecture includes three aspects with distinct content-domains:

- **Aspect P**: content-domain covering product development
- **Aspect M**: content-domain covering market analysis
- **Aspect O**: content-domain covering operations

Each aspect covers operational territory that is functionally distinct from the other two. A product development governance architecture (orchestration rules, coordination patterns, decision rationale, recorded task instances) addresses different problems than a market analysis architecture or an operations architecture. The three aspects may share cells through relational role membership, but their content-domains are authored as distinct in Self A's governance substrate.

Self A participates in FAI events with three partners, each relevant to a different one of Self A's domains:

- **Partner X**: a Self whose governance architecture covers product development
- **Partner Y**: a Self whose governance architecture covers market analysis
- **Partner Z**: a Self whose governance architecture covers operations

The governance question D2.58 addresses is: for each FAI event, which of Self A's aspects should the sharing-scope configuration include?

The answer follows directly from D1.22 Dimension 1 applied to content-domain as the relevance criterion:

- **FAI event with Partner X**: sharing scope includes Aspect P only. Aspects M and O are excluded.
- **FAI event with Partner Y**: sharing scope includes Aspect M only. Aspects P and O are excluded.
- **FAI event with Partner Z**: sharing scope includes Aspect O only. Aspects P and M are excluded.

This is domain-selective FAI participation. The sharing-scope configuration — a governance-authored parameter stored as substrate content under Paper 3's Claim 5 — specifies the domain-relevant aspect for each event. Aspects outside the event's domain are not excluded by technical constraint; they are excluded by governance decision. The governance author specifies a sharing scope that matches the event's domain, and the architecture honors that specification.

---

## 3. Sharing scope as the domain-selectivity mechanism

D1.22 Dimension 1 established that sharing scope is a configurable governance dimension of each FAI event — authored as substrate content, subject to the three Paper 1 governance rights (inspect, modify, override) at all times. The dimension answers the question: which aspects does this Self contribute to this event?

In the single-domain case, sharing scope is typically configured around purpose coherence and governance readiness. A Self contributing aspects to a FAI event selects aspects whose content-domain is relevant to the coordination purpose the event serves, and whose governance state is ready for inter-Self exchange (merge patterns configured, conflict routing specified, evolution eligibility authored).

The multi-domain case makes the content-domain criterion load-bearing in a way the single-domain case does not. A single-domain Self has all its aspects covering the same territory; domain-relevance is not the discriminating criterion. A multi-domain Self has aspects covering fundamentally different territories; content-domain compatibility between the contributing aspect and the FAI event's purpose is now the primary sharing-scope criterion.

The governance architecture requires no modification for the multi-domain case. Sharing scope is already a per-event, governance-authored parameter. The author of Self A's governance substrate must configure, for each FAI event, a sharing scope that includes only the domain-relevant aspects. This is the governing authority exercising Moment 1 governance (orchestration rule authoring) per the Paper 1 commitment: the rule specifying which aspects participate in each event's sharing scope is authored by humans and stored as substrate content. The execution of that rule — the actual exclusion of non-relevant aspects from a given event's shared substrate — is a downstream consequence of the governance specification, not a separate architectural act.

---

## 4. Three governance properties of domain-selective participation

Executing domain-selective FAI participation through sharing-scope configuration produces three governance properties that are worth naming separately, because each has independent governance value.

### Property 1 — Governance privacy by domain

Aspects not included in a FAI event's sharing scope remain within Self A's home governance perimeter. Their DNA-layer content, action-layer content, orchestration rules, and conflict history are not surfaced in the shared substrate for that event. Partner X, participating in a product development FAI event with Self A, has no access to Self A's market analysis governance architecture or operations governance architecture through that event.

This is governance privacy at the domain level. It is not security in the sense of access-control enforcement against an adversarial partner; it is the architectural consequence of a sharing-scope specification that excludes non-relevant aspects. The privacy is as strong as the governance specification that produces it: if the governance author configures a sharing scope that inadvertently includes Aspect M in the product development event, the privacy boundary does not hold. The architecture preserves the option; governance exercises it.

Domain-level privacy matters practically because governance architectures contain decision rationale, conflict history, and coordination patterns that are competitively or strategically sensitive. A product development FAI relationship does not require exposure of market analysis decision rationale to function. Keeping non-relevant aspects within the home perimeter is both a privacy practice and a governance hygiene practice: the shared substrate for a domain-specific event is smaller, more coherent, and more directly useful to the event's purpose when it contains only domain-relevant aspects.

### Property 2 — Domain compatibility as conflict predictor

D2.07 established conflict density — the proportion of aspects in a shared substrate that surface at least one governance conflict — as a measurable governance signal. When Self A contributes Aspect P to a FAI event with Partner X, the aspects in the shared substrate are drawn from a common content-domain. Conflicts that surface reflect genuine differences in how Self A and Partner X approach product development governance: different orchestration patterns, different conflict-handling rules, different coordination conventions for the same operational territory.

This makes conflict density in a domain-specific FAI event meaningful governance intelligence. High conflict density signals that two Selves govern the same domain differently in ways worth examining: either one has developed more effective approaches that the other can learn from, or they have diverged in ways that require explicit joint resolution before further coordination proceeds. Low conflict density signals strong domain-governance alignment.

By contrast, if Self A contributed all three aspects to the product development FAI event with Partner X, some portion of the conflict density would reflect domain mismatches — conflicts arising not from different approaches to product development governance but from the simple fact that Partner X does not have a market analysis or operations governance architecture, so no basis for productive merge exists for those aspects. This mismatch-generated conflict density is noise that obscures the signal from genuine domain-approach differences.

Domain-selective participation preserves the signal value of conflict density by ensuring that all conflicts in the shared substrate arise from actual governance approach differences within a shared domain.

### Property 3 — Domain-specific standing configurations

D2.21 established standing configurations as pre-authored FAI parameter sets that persist across multiple events with the same partner — specifying merge patterns, conflict routing, and evolution eligibility for the relationship, so that governance does not re-author these parameters from scratch for each event. A standing configuration is a sustained governance relationship with a partner, stored as substrate content under the recursive governance of Claim 5.

For a multi-domain Self, the appropriate standing-configuration architecture is one standing configuration per domain-specific FAI relationship, not one standing configuration covering all relationships or all domains. Self A's product development relationship with Partner X has different governance character than its market analysis relationship with Partner Y: different merge patterns may be appropriate, different conflict-routing rules may apply, different evolution eligibility specifications may reflect the domain's maturity and the relationship's history.

Maintaining domain-specific standing configurations allows governance to tailor sustained FAI relationship parameters to the specific character of each domain relationship. This is portfolio management work in the governance substrate: the standing configurations are substrate content, authored under human governance authority, updated as the domain relationships develop, and versioned with the provenance that Paper 1's accountability structure requires. A single standing configuration that covers all of Self A's FAI relationships would aggregate governance parameters across fundamentally different domains — the equivalent of applying a single merge policy to product development, market analysis, and operations coordination simultaneously. The aggregation produces neither the precision nor the tailoring that domain-specific relationships warrant.

---

## 5. Multi-domain FAI portfolio organization

A Self with multiple domain-specific FAI relationships has what may be called a FAI portfolio organized by domain. Portfolio management (D2.33) applied to the multi-domain case has a natural organizing dimension: the content-domain of each active FAI relationship.

The portfolio view tracks, for each domain in Self A's aspect architecture:

- Whether an active FAI relationship exists for that domain, and with which partner
- The sharing-scope configuration for that relationship (which aspect is contributed)
- The standing configuration governing that relationship (merge patterns, conflict routing, evolution eligibility)
- The governance health of the relationship (D2.35): whether conflict density is at an expected level, whether evolution-feed inputs are propagating appropriately, whether the standing configuration reflects the relationship's current governance state

A domain with no active FAI relationship is a domain in which Self A's governance architecture develops without inter-Self learning input. This may be appropriate — some domains may not have suitable FAI partners, or governance may have determined that the domain is not ready for inter-Self exchange — or it may represent a portfolio gap worth addressing. The portfolio view makes the gap visible.

A domain with multiple potential FAI partners presents a selection and sequencing governance question: which partner to engage first, whether to run simultaneous FAI relationships within the same domain, and how to manage the evolution-feed inputs from multiple domain-specific FAI events into the same aspect's home evolution pathway. D2.58 does not resolve these questions but names them as the governance territory the multi-domain portfolio view makes visible.

Portfolio management for a multi-domain Self thus operates at two levels: within each domain, the standard FAI relationship governance work (event configuration, conflict routing, evolution-feed management, standing configuration maintenance); and across domains, the portfolio-level oversight of which domains are active, which are inactive, and whether the portfolio's domain-coverage is consistent with Self A's governance architecture's overall purpose.

---

## 6. Cross-domain integration opportunity: home synthesis from multiple FAI relationships

A multi-domain Self with active FAI relationships across its domains is positioned for a governance synthesis opportunity that a single-domain Self cannot access: the identification of cross-domain integration patterns from the learning inputs of multiple domain-specific FAI relationships.

The mechanism is home governance synthesis, not a new joint FAI operation. When Self A runs domain-selective FAI events with Partners X, Y, and Z, each event's evolution feed delivers domain-specific learning inputs into Self A's home substrate via the four-locus evolution pathway (D1.17–D1.21): DNA-layer updates routing to appropriate aspects and Self-level governance, action-layer outputs propagating into action-feedback pathways, conflict annotations attaching to the home substrate's conflict records. These inputs arrive in Self A's home perimeter domain-specifically — product development learning into Aspect P's evolution pathway, market analysis learning into Aspect M's pathway, operations learning into Aspect O's pathway.

Self A's home governance layer may then synthesize across these domain-specific inputs. A coordination pattern that proved effective in the product development FAI relationship — a particular conflict-routing approach, a merge-pattern configuration that reduced conflict density, an evolution-eligibility criterion that produced high-quality DNA-layer inputs — may be relevant to the market analysis relationship with Partner Y. Self A's home governance synthesis identifies this cross-domain applicability and propagates it to the appropriate aspect's governance architecture.

This synthesis is strictly home governance work. It happens within Self A's governance perimeter, under Self A's governance authority, without requiring Partner X or Partner Y to be involved. The cross-domain insight is Self A's internal governance production, sourced from the intersection of two FAI relationships whose inputs both flow into the same home substrate. Partners X and Y need not be aware of each other; the synthesis is not a new inter-Self coordination event.

The cross-domain integration opportunity is available only to a Self with genuine content-domain diversity in its aspect portfolio and active FAI relationships in multiple domains. A single-domain Self may develop rich FAI relationships in its domain; it does not have the structural basis for cross-domain synthesis. Multi-domain governance architecture thus carries a compounding advantage at the portfolio level: diverse FAI relationships produce not only domain-specific evolution inputs but also home-synthesizable cross-domain governance learning.

---

## 7. Anti-pattern: domain-indiscriminate sharing

The anti-pattern that D2.58 formalizes against domain-selective participation is domain-indiscriminate sharing: contributing all of Self A's aspects to all FAI events regardless of domain relevance.

Domain-indiscriminate sharing violates all three governance properties established in §4:

It eliminates domain-level governance privacy. Partner X, in a product development FAI event, receives access to Self A's market analysis and operations governance architectures — governance content whose relevance to the product development coordination purpose is absent or marginal. Exposing non-relevant aspects to a FAI event is a governance scope failure: the shared substrate contains content that has no coordination purpose for that event, and that content may be strategically or competitively sensitive.

It corrupts the conflict-density signal. When aspects from all three of Self A's domains are present in a FAI event with Partner X — who may have only a product development aspect — the shared substrate generates domain-mismatch conflicts: conflicts arising not from different governance approaches to a shared domain but from the absence of any shared domain basis for merge. These mismatch conflicts inflate conflict density without carrying governance intelligence about approach differences. An observer reading conflict density on a domain-indiscriminate shared substrate cannot distinguish domain-approach conflicts from domain-absence artifacts.

It forces a single standing configuration across domain-heterogeneous relationships. If Self A maintains one standing configuration for its FAI relationships across all three partners, that configuration must average governance parameters across fundamentally different domain relationships. The product development relationship's appropriate merge pattern may differ from the market analysis relationship's; the operations relationship's appropriate conflict routing may differ from both. Aggregating them into a single standing configuration produces governance parameters suited to none.

Domain-indiscriminate sharing is a failure of governance specificity: treating all aspects as equally relevant to all FAI events, and all FAI relationships as interchangeable, when the content-domain architecture of the Self's aspects establishes that relevance is domain-selective and relationships are domain-differentiated. The correction is not architectural — the sharing-scope parameter already exists. The correction is governance authoring: authors of Self A's governance substrate must configure domain-appropriate sharing scopes for each FAI event rather than defaulting to full-aspect contribution.

---

## 8. Operational test

A system implements D2.58's domain-selective FAI governance if and only if all of the following are verifiable for a multi-domain Self A participating in multiple FAI events:

1. For each FAI event Self A participates in, the governance substrate contains an authored sharing-scope specification identifying which of Self A's aspects are included in that event's shared substrate.

2. For each FAI event, the included aspects are those whose content-domain is relevant to the event's coordination purpose; aspects whose content-domains are not relevant to the event's purpose are identified as absent from the sharing scope.

3. An observer with access to each event's shared substrate can confirm that aspects outside the event's domain are not present in that substrate — the exclusion specified in the sharing-scope configuration is reflected in the substrate's actual content.

4. Self A's governance substrate contains distinct standing configurations for each domain-specific FAI relationship, rather than a single standing configuration covering all FAI relationships.

5. Self A's portfolio-level governance record tracks, for each domain in Self A's aspect architecture, the active or inactive status of FAI relationships in that domain.

A system in which (3) fails — where aspects outside the event's domain appear in the shared substrate despite the sharing-scope specification excluding them — has a governance execution gap: the specification is correct but its enforcement is not reliable. A system in which (4) fails — where a single standing configuration governs domain-heterogeneous relationships — has collapsed the domain-specificity that separate standing configurations are designed to preserve. A system in which (1) fails — where no authored sharing-scope specification exists and aspects are contributed by default — is operating domain-indiscriminate sharing as its participation pattern.

---

## 9. Conclusion

D2.58 formalizes the governance of FAI participation for a Self whose aspect portfolio spans multiple distinct content-domains. The core finding is simple: the sharing-scope configuration established in D1.22 Dimension 1 is the mechanism that enables domain-selective participation. Governance authors a sharing scope that includes domain-relevant aspects and excludes domain-irrelevant aspects. The three governance properties that follow — domain privacy, conflict-density signal preservation, and domain-specific standing configurations — are the downstream consequences of applying this authoring discipline consistently across a multi-domain Self's FAI portfolio.

The note adds two further observations. First, multi-domain FAI relationships are best managed as a portfolio organized by domain, with portfolio-level oversight tracking which domains have active relationships and what the governance health of each is. Second, a multi-domain Self with diverse FAI relationships is positioned for home-synthesis opportunities — identifying cross-domain governance learning from the intersection of multiple FAI evolution-feed inputs — that are structurally unavailable to single-domain Selves. Both observations follow from the existing architecture; neither requires new mechanisms.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance for Multi-Domain Selves.* May 15, 2026. ORCID: 0009-0004-8065-3235.
