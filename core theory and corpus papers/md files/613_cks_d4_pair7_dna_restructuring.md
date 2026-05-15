# Composition Pair 7: DNA Absorption and Aspect Restructuring

**Series D — Phase D4 Composition Pairs | Note D4.08 | #613**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes the governance requirements that emerge when DNA Absorption Governance (D2.11) and Aspect Restructuring and FAI (D2.55) operate simultaneously. Three non-obvious requirements appear only at the composition: absorption targeting a specific aspect must complete before that aspect is restructured; restructuring governance records must reference the absorbed DNA as provenance; and declined absorption candidates must be reviewed as restructuring inputs alongside absorbed DNA. The note identifies these as a governance race-condition prevention rule, a two-step accountability trail, and a structural-gap detection mechanism — none of which are visible in either commitment studied alone.

---

## 1. Pair Identification

**Commitment A — DNA Absorption Governance (D2.11)** specifies the five-step protocol by which a Self's governance absorbs DNA-layer content — orchestration patterns, schemas, behavioral rules — that originated in a Full Aspect Integration (FAI) event and was carried on the shared substrate. The five steps are: candidate identification (which shared-substrate DNA content is eligible for absorption), fit evaluation (whether the content maps to a home aspect's existing governance), absorption decision (approve or decline, recorded by governance), integration (approved DNA content incorporated into the target aspect's DNA layer under directed selection), and record closure (the decision record is finalized with the absorption target, the FAI event of origin, and the outcome).

**Commitment B — Aspect Restructuring and FAI (D2.55)** specifies the governance process by which a Self revises its aspect structure — merging, splitting, renaming, or eliminating aspects — when FAI evolution outputs indicate that the existing structure no longer fits the Self's operating reality. D2.55 introduces the structural co-adaptation cycle: FAI events generate evidence about how well current aspects serve inter-Self coordination, that evidence is reviewed in restructuring governance, and restructuring decisions update the aspect structure to better serve future FAI events. The cycle makes FAI experience a driver of structural governance, not merely operational experience.

---

## 2. Governance Scenario Requiring Both Simultaneously

A Self has participated in a FAI event. Following dissolution, two governance processes open concurrently. First, governance is working through D2.11's absorption protocol: it has identified DNA candidates from the FAI event and is evaluating each for fit with home aspects. Several candidates are targeted at Aspect X — a specific aspect in the Self's home structure whose governance logic the FAI event has enriched. Second, governance is conducting a D2.55 restructuring review: pattern analysis of prior FAI events suggests that Aspect X and Aspect Y, which have grown to overlap substantially, should be merged into a single consolidated aspect.

Both processes are legitimate governance activity. Neither is deferred. The question this composition raises is whether they can proceed independently, in whatever order they complete — or whether their interaction creates requirements that neither commitment, studied alone, would impose.

---

## 3. Non-Obvious Governance Requirements from the Combination

### Requirement 1 — Absorption Completion Before Target-Aspect Restructuring

When a DNA absorption candidate from a FAI event targets Aspect X, and Aspect X is simultaneously a candidate for restructuring, governance must complete the absorption decision for Aspect X before restructuring Aspect X.

The reason is architectural, not procedural. The absorption decision in D2.11 Step 3 records the absorption target by aspect identity. If Aspect X is merged into Aspect Y before the absorption decision is made, the target no longer exists in the form the absorption review assumed. The DNA candidate was evaluated for fit with Aspect X's current governance structure — its orchestration patterns, schemas, scope. The merged Aspect Y has a different governance structure. The fit evaluation that preceded the decision is now stale: it assessed the wrong target. Governance cannot simply carry forward an absorption approval that was made against an aspect that no longer exists; it would be incorporating DNA into a governance structure the DNA was never evaluated against.

This is a governance race condition. Running absorption and restructuring concurrently for the same target aspect allows the absorption process to complete against a governance structure that the restructuring process has already invalidated — or, symmetrically, allows restructuring to proceed against an aspect whose governance content is in mid-change from absorption. The ordering requirement — absorb first, then restructure — is the race-condition prevention rule. It does not appear in D2.11 (which specifies the absorption protocol within a stable aspect structure) or in D2.55 (which specifies restructuring governance without prescribing its sequencing relative to ongoing absorption). It is a property of the composition.

### Requirement 2 — Restructuring Records Must Reference Absorbed DNA as Provenance

When D2.55's structural co-adaptation cycle informs a restructuring decision, and the evidence base for that decision includes DNA that was absorbed from a FAI event under D2.11, the restructuring governance record must cite the specific absorbed DNA as its evidential basis.

The accountability trail for how inter-Self learning reached a structural governance decision runs through two recorded steps:

**Step 1 — Absorption decision record (D2.11 Step 4):** records which DNA candidate, from which FAI event, was absorbed into which aspect, approved by which governance authority.

**Step 2 — Restructuring governance record (D2.55):** records which aspects were restructured, why, and on the basis of what evidence — including references to the Step 1 absorption records that supplied the structural evidence.

Without Step 2 explicitly referencing Step 1, the accountability trail is broken at the seam. An observer reviewing the restructuring record would see that the Self restructured Aspect X, but could not trace whether that restructuring was informed by the FAI event, and if so which DNA candidates were the operative evidence. The two-step chain makes the full audit possible: FAI event → contribution record → shared-substrate DNA content → absorption decision (D2.11 Step 4) → restructuring governance record (D2.55).

Neither commitment alone specifies this cross-record reference requirement. D2.11 does not require that its decision records be cited in downstream governance decisions. D2.55 does not require that its evidential basis be traceable to specific absorption records. The requirement emerges from the combination, because the combination is what creates the multi-step chain.

### Requirement 3 — Declined Absorption Records Are Also Restructuring Inputs

When governance declines to absorb a DNA candidate from a FAI event — recording in D2.11 Step 3 that the candidate does not fit any current aspect's governance structure — that decline record is not merely administrative closure. It is governance intelligence about the current aspect structure, and it must be reviewed as an input in D2.55's restructuring process alongside absorbed DNA.

The inference pattern is: if a DNA candidate from a FAI event carries genuine governance content (as evidenced by its presence on the shared substrate and its selection as a candidate), but does not fit any existing aspect, the mismatch is informative. It may indicate that the Self's current aspect structure does not include an aspect that its operating context now requires. The declined DNA is not defective — it is a signal about structural gap.

This requirement is non-obvious because the natural practitioner instinct treats absorbed DNA and declined DNA asymmetrically: absorbed DNA goes forward as an evolution input; declined DNA closes the record. The composition reveals that declined records contain structural fit information that absorbed records do not. Absorbed DNA confirms fit with existing structure. Declined DNA, precisely because it did not fit, identifies the boundary of existing structure — and that boundary, reviewed during restructuring governance, may indicate where new aspects should be created.

---

## 4. Prior-Art Significance

Any governance system that connects AI-assisted learning at the inter-Self scope to structural adaptation of a governance architecture must address the three requirements this composition formalizes. The absorption-before-restructuring ordering requirement is a race-condition prevention rule for governance processes that share an object — the aspect — as both input and output of concurrent operations. The two-step provenance chain is the minimum accountability trail for a governance decision that is downstream of two prior recorded governance acts. The declined-absorption-as-restructuring-input requirement is a structural-gap detection mechanism that uses governance rejection data as positive evidence.

Prior work on organizational learning, knowledge management, and configuration governance does not address this exact combination, because it does not operate at the intersection of a substrate-bound absorption protocol and a substrate-governed structural adaptation cycle. The combination is specific to architectures in which inter-Self exchange produces DNA-layer content that feeds both operational governance and structural governance simultaneously.

---

## 5. Operational Test

For a Self that absorbed FAI DNA and subsequently restructured aspects, an observer can verify the composition pair's requirements were met by examining governance records:

**(a) Ordering:** Were absorption decisions for aspects that were later restructured completed before those aspects were restructured? Governance records for Requirement 1 compliance must show that D2.11 Step 4 record timestamps precede the D2.55 restructuring decision timestamps for any aspect that was both an absorption target and a restructuring target in the same post-FAI governance cycle.

**(b) Provenance citation:** Do restructuring governance records reference the specific absorbed DNA that informed the restructuring decision? Requirement 2 compliance requires that D2.55 restructuring records carry explicit citations to D2.11 absorption decision records — not only to the FAI event, but to the specific absorption step that brought the DNA into the home substrate.

**(c) Decline review:** Were declined absorption records reviewed as part of the restructuring governance process? Requirement 3 compliance requires that the restructuring governance record acknowledge which declined DNA candidates were reviewed, and whether any declined candidates were identified as structural-gap signals.

A governance record set that passes all three checks demonstrates that the Self's governance treated the composition as a single integrated process rather than two independent commitments. A record set that fails any check — absorption and restructuring records with ambiguous ordering, restructuring records citing only FAI events rather than specific absorption decisions, or restructuring records with no evidence of declined-candidate review — indicates that the composition was not governed as a unit.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Composition Pair 7: DNA Absorption and Aspect Restructuring.* CKS Derivation Note D4.08 (#613). May 15, 2026. ORCID: 0009-0004-8065-3235.
