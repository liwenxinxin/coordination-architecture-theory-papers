# Composition Pair 3: Competition Variant and Preserve Tier Dominance

**Derivation Note D4.04 — Phase D4 Composition Pairs**
**Series D: Paper 3 Derivations**
**Note #609 in the CKS Defensive-Publication Series**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes Composition Pair 3 in the Phase D4 series: the pairing of the competition/cooperation variant selection (D2.20, Dimension 4 of FAI event configuration) with the preserve tier as a first-class conflict-handling tier (D1.13). The central finding is that these two commitments, when applied together for a competition-oriented inter-AI governance event, impose three governance requirements that neither commitment imposes independently: (1) variant selection and conflict routing rules are separate configured objects requiring two distinct governance acts; (2) conflict classification must be sufficiently granular to distinguish approach-difference conflicts from factual-inconsistency conflicts — a requirement that only surfaces from the composition; and (3) full carry-through must be explicitly configured for preserved conflicts when the event's purpose is comparative intelligence. Failure to satisfy requirement (1) produces AP-14 (competitive intelligence misrouting), the anti-pattern formalized in D3.08. This note identifies Composition Pair 3 as the generative source of AP-14 and establishes the two-object configuration requirement as prior art.

---

## 1. Pair Identification

**Commitment A — Competition/Cooperation Variant (D2.20, Dimension 4).**
The FAI event configuration includes a dimension governing whether the event is oriented toward cooperative or competitive exchange. In cooperative mode, orchestration rules optimize for mutual benefit across participating parties. In competitive mode, orchestration rules scope contribution and protect strategic content. Both are the same architectural object — the shared substrate with FAI as canonical operation — operating under different rule sets. The selection between them is a human-authored governance decision made as substrate content, subject to the same recursive governance properties as all other configuration dimensions.

**Commitment B — Preserve Tier as First-Class Tier (D1.13).**
The three-tier conflict-handling mechanism (preserve / resolve via configured orchestration / escalate to humans) treats the preserve tier not as a fallback or failure state but as a first-class governance output. A conflict routed to the preserve tier is retained as addressable substrate state, with both sides of the conflict kept distinct, the divergence point identified, and provenance attached. Preservation is the architectural default at the substrate level, inherited from Paper 1's conflict-as-first-class commitment and extended to the inter-Self scope.

The pairing under examination is the configuration of a competition-variant FAI event in which preserve-tier dominance is the intended conflict routing policy — that is, an event designed to produce comparative governance intelligence by holding approach differences in place rather than resolving them.

---

## 2. Governance Scenario Requiring Both Simultaneously

Governance is configuring a competition-variant FAI event intended to generate comparative governance intelligence. Two parties are operating under distinct coordination approaches — different rule sets, different schema conventions, or different orchestration patterns — and the event's purpose is to surface those differences as retained, inspectable substrate state. The comparison is the output; resolution would destroy it.

For the event to produce its intended output, two things must be true simultaneously. First, the event must be configured as competition variant (Commitment A), so that orchestration rules scope contribution appropriately and strategic content is protected — cooperative orchestration would apply merge logic that blurs rather than preserves the distinction. Second, the preserve tier must be configured as the dominant conflict routing destination (Commitment B), so that approach differences encountered during the merge are retained rather than resolved or escalated — routing to resolve would collapse the comparison; routing to escalate would remove it from substrate state into a human workflow.

Neither commitment alone produces the governance outcome. A competition-variant event without preserve-tier-dominant routing will misroute the approach-difference conflicts that are the event's primary analytical content. A preserve-tier-dominant configuration without competition-variant selection will apply cooperative merge logic that may inadvertently integrate rather than contrast the two parties' approaches. The scenario requires both, simultaneously and explicitly.

---

## 3. Non-Obvious Governance Requirements from the Composition

### Requirement 1 — Variant Selection and Routing Rules Are Separate Configured Objects

The most important non-obvious requirement is also the most operationally consequential: competition variant selection (Dimension 4 of the FAI event configuration) and conflict tier routing rules (the configured object specifying which conflict classes route to which tiers) are two distinct authored governance objects. Selecting competition variant does not automatically configure preserve-tier-dominant routing. The two are independently authored, independently stored as substrate content, and independently inspectable.

This separation is not an implementation accident. Dimension 4 governs the orchestration posture for the exchange — how contribution is scoped, how strategic content is protected, how the merge operation proceeds. The routing rules govern what happens when conflicts surface during that exchange — which conflict classes go to which tier. These are different governance questions answered by different governance acts. An author can select competition variant and then configure routing to send all conflicts to the resolve tier; this would be a valid (if purpose-defeating) governance configuration. The architecture does not prevent it; the governance requirement is that the author must explicitly choose.

Failure to author both objects produces an incomplete governance configuration. The routing rules default state in a competition-variant event is not automatically preserve-tier-dominant. If governance authors Dimension 4 and omits the routing rules, the event runs with whatever routing default is in effect. In a competition-variant event designed for comparative intelligence, this produces AP-14 (competitive intelligence misrouting): the approach-difference conflicts that constitute the event's analytical output are routed away from the preserve tier, and the comparative intelligence the event was designed to generate is lost or corrupted. AP-14 is not a failure of intent; it is a failure of configuration completeness. Composition Pair 3 identifies the exact gap: two objects, one authored, one omitted.

### Requirement 2 — Conflict Classification Granularity Is the Composition-Specific Prerequisite

For preserve-tier-dominant routing in a competition-variant event to function as designed, the conflict routing rules must be able to distinguish two conflict classes: approach-difference conflicts (arising from genuinely different coordination methods) and factual-inconsistency conflicts (arising from contradictory factual claims about the same state of affairs). The governance intent is to route approach-difference conflicts to preserve — these are the event's analytical content — and factual-inconsistency conflicts to resolve — these are errors that would corrupt the comparison if left standing.

This classification requirement is composition-specific. Commitment A (competition variant) does not independently require approach-difference vs. factual-inconsistency classification; it requires orchestration rules appropriate to competitive exchange, but does not specify what those rules must distinguish at the conflict-class level. Commitment B (preserve tier as first-class) does not independently require this classification either; it requires that conflicts can be preserved, but does not specify that the preserve tier must be dominant or that particular conflict classes must be routed there selectively.

The requirement surfaces only when both commitments are applied together in the context of a comparative-intelligence event. The composition creates a governance purpose — retain the comparison, correct the errors — that neither commitment alone produces, and that purpose is what makes the classification granularity necessary. A governance author designing this event for the first time may implement Dimension 4 and the routing rules without recognizing that the routing rules must be written to a classification resolution that the event's purpose demands. This is the paradigmatic composition-pair insight: the composition imposes a requirement that inspecting each commitment in isolation would not reveal.

### Requirement 3 — Carry-Through Configuration for Competitive Intelligence

When preserve-tier dominance is the routing policy and the event's purpose is comparative learning, the carry-through configuration for preserved conflicts should be set to full carry-through. Preserved conflicts that carry through into each participating party's evolution feed become annotations within home substrates — flagging the coordination boundaries that further work must address. For a competition-variant event designed to generate comparative intelligence, partial or minimal carry-through would truncate the event's output at the home-perimeter boundary.

This carry-through requirement is also composition-specific. Competition variant alone specifies nothing about carry-through depth. Preserve-tier dominance alone specifies that conflicts are retained in the shared substrate but does not specify the carry-through depth at dissolution. The carry-through commitment implied by the composition — full carry-through for preserved conflicts in a comparative-intelligence event — must be explicitly authored. It does not follow automatically from either commitment.

---

## 4. Prior-Art Significance

Composition Pair 3 establishes prior art for a governance requirement that any inter-AI coordination system implementing competition mode must satisfy: the two-object configuration requirement.

Any governance system that claims to "support competition mode for inter-AI governance comparison" — meaning any system that allows competition variant selection and that handles conflicts — must implement competition variant selection and conflict routing rules as separately authored governance objects. Treating them as a single configuration act, or inferring routing policy from variant selection, is architecturally unsound under the CKS pattern and produces AP-14.

The prior-art significance is not limited to the CKS architecture. The underlying governance logic — that operational mode selection and conflict routing policy are distinct governance concerns answerable by distinct governance acts — applies to any coordination architecture that separates orchestration configuration from conflict handling configuration. Composition Pair 3 is the first formalization of this as a named, citable prior-art claim in the context of inter-AI governance coordination.

The AP-14 cross-reference strengthens both notes. D3.08 established AP-14 as a named anti-pattern with a defined mechanism. D4.04 identifies the exact composition pair whose incomplete satisfaction activates that mechanism. Together, the two notes provide a closed account: the failure mode is AP-14; the cause is incomplete satisfaction of Composition Pair 3; the remedy is explicit authoring of both configured objects.

---

## 5. Operational Test

For a competition-variant FAI event configured with preserve-tier-dominant routing for comparative governance intelligence, an observer verifies the following four conditions:

**(a) Dimension 4 — competition variant — is set in the authored configuration.** The event configuration, readable as substrate content, explicitly records competition variant as the selected orchestration posture. This is an authored value, not inferred from event purpose or participant identity.

**(b) Routing rules explicitly route approach-difference conflicts to the preserve tier.** The conflict routing rules, separately authored and readable as substrate content, specify that conflicts classified as approach-difference conflicts are routed to the preserve tier. The routing rule is a positive, explicit specification — not a default, not an absence of routing-to-resolve instructions.

**(c) Conflict classification is sufficiently granular to distinguish approach-difference from factual-inconsistency conflicts.** The conflict classification specification within the routing rules defines both classes at sufficient resolution to make the routing distinction operational. An observer can inspect the classification specification and determine whether a given conflict would be classified as approach-difference or factual-inconsistency under the authored rules.

**(d) Full carry-through is configured for preserved conflicts.** The carry-through configuration, readable as substrate content, specifies full carry-through for conflicts routed to the preserve tier. This specification is an authored governance act, not a default.

A competition-variant comparative-intelligence event that satisfies all four conditions is fully configured under Composition Pair 3. An event that satisfies (a) but not (b) has produced the configuration gap that generates AP-14. An event that satisfies (a) and (b) but whose routing rules lack the classification granularity required by condition (c) has satisfied the form of the two-object requirement without satisfying the function — the routing rules exist, but they cannot make the distinction they need to make.

---

## How to Cite This Note

Li, W. (2026). *Composition Pair 3: Competition Variant and Preserve Tier Dominance.* Derivation Note D4.04, CKS Defensive-Publication Series, Note #609. May 15, 2026. ORCID: 0009-0004-8065-3235. License: CC BY 4.0.
