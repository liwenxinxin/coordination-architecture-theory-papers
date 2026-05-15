# The Intra-Self and Inter-Self Governance Boundary

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

The CKS architecture distinguishes between intra-Self coordination — governed by Paper 2's integration architecture — and inter-Self coordination — governed by Paper 3's Full Aspect Integration (FAI) framework. The boundary between the two is not organizational or legal; it is defined by governance authority. Aspects governed by the same governance authority are intra-Self regardless of how many entities, subsidiaries, or departments are involved. Aspects governed by different governance authorities are inter-Self and require FAI regardless of how closely those authorities are organizationally related. This note states the boundary criterion precisely, applies it to three structural scenarios, articulates the three-rights independence test that operationalizes the criterion, addresses the grey zone of partially shared governance elements, and establishes the prior-art significance of a governance-authority-based boundary criterion.

---

## 1. Why the boundary needs a precise criterion

Paper 2 governs coordination within a Self: cross-cell rules, cross-aspect integration, Self-level DNA. Paper 3 governs coordination across Selves: the shared substrate, Full Aspect Integration, the three-tier conflict-handling mechanism, and the four-locus evolution feed. Both governance regimes are fully specified. What neither paper states explicitly is the test for which regime applies in structural edge cases — cases where two parties coordinating their AI-assisted work are neither obviously one entity nor obviously two unrelated parties.

The gap has practical consequences, because the answer determines which architecture must be deployed. If two parties are intra-Self, Paper 2's cross-aspect coordination rules suffice; no shared substrate needs to be constructed, no FAI event configured, no inter-Self conflict escalation path established. If two parties are inter-Self, Paper 3's full machinery is architecturally required. A party that applies Paper 2's lighter governance to a situation that is architecturally inter-Self leaves an ungoverned inter-Self perimeter — a direct failure mode against which the FAI architecture was designed. Stating the boundary criterion precisely closes that gap and ensures the correct regime is deployed in all organizational configurations, not only in the most obvious ones.

---

## 2. The boundary scenario: three organizational structures

Three organizational structures raise the boundary question concretely:

**(a) Single organization with unified governance.** A single legal entity with one set of governance practitioners. All aspects operated by the organization are governed by the same authority: the same practitioners hold the three rights (inspect, modify, override) over all aspects without requiring sign-off from any other governance body.

**(b) Holding company with subsidiaries exercising independent governance.** A parent organization and one or more subsidiaries. Nominally, the parent has authority over the subsidiaries. In practice, each subsidiary operates its own governance: the subsidiary's governance practitioners make decisions about their own aspects independently, and the parent's practitioners cannot exercise the three rights over a subsidiary's aspects without the subsidiary's governance approval.

**(c) Two separate organizations.** Two legally and operationally independent entities, each with its own governance authority and aspects. No shared governance structure exists.

The intuitive answer — that scenario (a) is intra-Self and scenario (c) is inter-Self, with (b) genuinely ambiguous — is directionally correct but architecturally incomplete. Scenario (b) is not architecturally ambiguous once the boundary criterion is stated; it resolves cleanly from the same test that resolves (a) and (c).

---

## 3. The boundary criterion: governance authority, not organizational structure

The intra-Self / inter-Self boundary is defined by whether the aspects being coordinated are governed by **the same home governance authority** or by **different home governance authorities**.

This is a governance-authority criterion, not an organizational or legal criterion. The organizational relationship between the parties — parent and subsidiary, peer divisions of one company, two strangers — is architecturally irrelevant to the boundary determination. What matters is whether a single set of governance practitioners holds the three rights (inspect, modify, override) over the aspects in question.

Applying the criterion to the three scenarios:

**Scenario (a) — intra-Self.** A single set of governance practitioners holds all three rights over all aspects. Coordination between those aspects is intra-Self. Paper 2's integration architecture governs. FAI is not required.

**Scenario (b) — inter-Self.** Each subsidiary exercises independent governance authority over its own aspects: the subsidiary's practitioners hold the three rights over its aspects; the parent's practitioners cannot exercise those rights over the subsidiary's aspects without subsidiary governance sign-off. The legal relationship — the parent nominally controls the subsidiary — does not determine the governance boundary. Two entities each exercising independent governance authority over their own aspects are different Selves for coordination purposes. Coordination between their aspects is inter-Self. Paper 3's FAI architecture governs.

**Scenario (c) — inter-Self.** Two independent governance authorities constitute two Selves. Inter-Self FAI is required. This is the clear case.

The counterintuitive result is scenario (b): a parent company and its subsidiary can be different Selves architecturally, even though they are one legal enterprise. This is not an anomaly; it is the direct consequence of a governance-authority criterion consistently applied. The Self boundary follows the three-rights map. When the three rights are split between independent authorities, the inter-Self perimeter exists regardless of what the organizational chart says.

---

## 4. The three-rights independence test

The operational boundary test follows directly from the boundary criterion:

> **Does a single set of governance practitioners hold the three rights — inspect, modify, and override — over both aspects, without requiring sign-off from a different governance authority?**

If yes: the two aspects share a governance authority → intra-Self → Paper 2 governs.

If no: the two aspects are governed by different authorities → inter-Self → Paper 3 FAI governs.

The test has three components corresponding to the three rights:

**Inspect independence.** Can governance practitioners for aspect A read the full substrate content of aspect B — its DNA-layer content, action-layer content, orchestration rules — without requiring B's governance practitioners to authorize that access? If access to B requires B's governance approval, the inspect right is not shared.

**Modify independence.** Can governance practitioners for aspect A modify aspect B's substrate content or orchestration rules without B's governance sign-off? If modification requires B's governance approval, the modify right is not shared.

**Override independence.** Can governance practitioners for aspect A override operations, defaults, or outputs that touch aspect B's substrate content without B's governance sign-off? If override requires B's governance approval, the override right is not shared.

For the intra-Self classification, all three independence conditions must hold in both directions: the same practitioners must hold all three rights over both aspects. Partial independence — for example, shared inspect rights but independently held modify rights — does not satisfy the intra-Self test. The presence of any independently held right indicates that the aspects are governed by different authorities. The inter-Self classification applies, and FAI governs.

---

## 5. Grey zone: partially shared governance elements

Some organizational structures include partially shared governance elements that complicate the straightforward test. A common compliance function may hold override rights over any aspect across a group of subsidiaries. A central architecture team may hold modify rights over all DNA-layer content regardless of which subsidiary originates it. A shared audit function may hold universal inspect rights.

These structures do not require a different criterion; they require careful application of the same three-rights test to the shared element's actual authority:

If the shared governance element holds **all three rights** (inspect, modify, and override) over all aspects in question — and the aspects' respective home practitioners cannot block any of those rights — then for coordination purposes those aspects share a governance authority. The shared element constitutes the governance authority that defines the Self boundary. Coordination between those aspects is intra-Self; Paper 2 governs.

If the shared governance element holds **fewer than all three rights**, or holds three rights in principle but requires home-practitioner approval to exercise any of them, the partial sharing does not constitute a shared governance authority. The aspects remain governed by their respective home authorities. The inter-Self classification applies; Paper 3 FAI governs.

The grey zone is therefore resolvable by the same test as the clear cases. Nominal authority — the shared element "has authority" in principle — does not substitute for the actual three-rights test. What the shared element can exercise, unconditionally, over both aspects determines the classification.

---

## 6. Prior-art significance

Establishing governance authority as the boundary criterion for the intra-Self / inter-Self distinction carries three prior-art consequences.

**First, the FAI scope covers all cross-governance-authority coordination**, not only coordination between obviously unrelated legal entities. Holding companies whose subsidiaries exercise independent governance authority fall within the inter-Self FAI scope. Any implementation that constructs shared AI coordination infrastructure across independently governed entities — regardless of the legal or organizational relationships between them — falls within the scope of the prior art that Paper 3 establishes.

**Second, a narrowing interpretation of Paper 3's scope to "obviously separate companies" is foreclosed.** An adversary who argues that FAI is required only for clearly independent legal entities and not for subsidiaries of a common parent cannot sustain that argument against the governance-authority boundary criterion. The criterion expressly addresses the subsidiary case, applies the three-rights test, and reaches the inter-Self conclusion where subsidiaries operate independent governance authority.

**Third, the boundary criterion connects to the three-rights test already established in Papers 1 and 2.** The same three rights that define human governance over a substrate at cell scope (Paper 1 §3.3) and at Self scope (Paper 2) also define the governance-authority boundary that determines which coordination regime applies at the inter-Self scope. Prior-art coverage for the three-rights test as the fundamental governance-authority measure carries forward to this inter-Self boundary determination without requiring a new test or a new concept. The architecture is consistent across all scopes: who holds the three rights determines the governance boundary at every level.

---

## 7. Conclusion

The intra-Self / inter-Self boundary is defined by governance authority, not by organizational structure. Aspects governed by the same authority — meaning a single set of practitioners holds the inspect, modify, and override rights over both aspects without requiring sign-off from a different governance body — are intra-Self, and Paper 2's integration architecture governs their coordination. Aspects governed by different authorities are inter-Self, and Paper 3's FAI architecture governs regardless of the legal or organizational relationship between those authorities.

The three-rights independence test operationalizes this criterion and resolves all three structural scenarios, including the holding-company case that intuitive analysis leaves ambiguous. Subsidiaries with independent governance authority are different Selves; departments without independent governance authority are intra-Self; the grey zone of partially shared governance elements resolves by applying the same three-rights test to what the shared element can actually exercise over both aspects. Organizational charts and legal ownership structures are irrelevant to the determination.

The prior-art consequence is that Paper 3's FAI architecture covers all cross-governance-authority coordination. Any system that coordinates AI-assisted work across independently governed entities — whatever the organizational relationship between them — falls within the scope of the inter-Self FAI architecture this derivation series publishes as prior art.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Intra-Self and Inter-Self Governance Boundary.* May 15, 2026. ORCID: 0009-0004-8065-3235.
