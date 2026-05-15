# P3↔P2 Governance Boundary Cases

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** CC — Cross-Paper Synthesis (Note CC.18, #684)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026). It does not introduce new architectural axioms. Its sole contribution is to identify, with precision, where Paper 2 governance applies and where Paper 3 governance applies at three specific boundary cases that governance practitioners encounter when operating across the two scopes simultaneously.

---

## Abstract

The CKS trilogy establishes two adjacent governance scopes: Paper 2 governs coordination within a single Self through its home governance architecture; Paper 3 governs coordination between aspects contributed by different Selves through a shared substrate. Where exactly one scope ends and the other begins — and whether they can apply simultaneously — is a practical governance question the papers leave implicit. This note makes it explicit at three boundary cases: (1) when coordination between aspects is intra-Self versus inter-Self; (2) when a content-combination event is an intra-Self mating versus an inter-Self FAI event; and (3) when action-layer content processed by Paper 2's action-feedback mechanism originates from an FAI event rather than from home cell operations. Cases 1 and 2 share a common boundary criterion — the governance authority independence test. Case 3 introduces the subtlest boundary: Paper 2's mechanism applies to Paper 3-origin content, and FAI-origin provenance must survive the transition intact. At FAI dissolution, the sharpest boundary dissolves entirely: both papers apply simultaneously to different aspects of the same event.

---

## 1. Why boundary cases require explicit treatment

Paper 2 and Paper 3 are structurally continuous. Paper 3 is not a replacement for Paper 2 governance; it is an extension that adds an inter-Self coordination layer above Paper 2's home governance architecture. Because the two papers are extensions of the same underlying architecture rather than independent alternatives, their governance scopes overlap in practice wherever a Self both participates in FAI events and continues operating its home governance during those events.

The overlap produces three specific boundary cases that governance practitioners encounter without explicit guidance from either paper taken alone:

- When aspects from two different locations within an architecture are coordinating, how does a practitioner determine whether that coordination is a Paper 2 matter (intra-Self, handled through the Self's integration architecture) or a Paper 3 matter (inter-Self, handled through the shared substrate)?
- When content from two aspects is being combined, how does a practitioner determine whether that combination is a Paper 2 mating event or a Paper 3 FAI event?
- When action-layer content inside a participating Self's home architecture originated from an FAI event rather than from the Self's own cell operations, which paper's governance applies to the processing of that content?

This note answers each question with the applicable boundary criterion.

---

## 2. The common boundary criterion for Cases 1 and 2: governance authority independence

Cases 1 and 2 share a single boundary criterion, stated once here and applied to both:

**The governance authority independence test.** A coordination event (Case 1) or a content-combination event (Case 2) is intra-Self — governed by Paper 2 — if and only if a single governance authority holds all three rights (the right to inspect, the right to modify, and the right to override) over all aspects participating in the event. If two or more independent governance authorities each hold the three rights over one or more of the participating aspects, the event is inter-Self and governed by Paper 3.

The test is binary and applies at event scope, not at aspect scope individually. An aspect may be a member of a Self that participates in Paper 3 FAI events while also participating in intra-Self coordination governed entirely by Paper 2. What determines which governance scope applies is whether the governance authorities over all participating aspects are identical (one authority: Paper 2) or independent (two or more authorities: Paper 3).

The consistency of this test across two different boundary types is architecturally deliberate. A practitioner who can apply the governance authority independence test resolves both boundary cases simultaneously with one inquiry.

---

## 3. Boundary Case 1 — Intra-Self versus inter-Self coordination

Paper 2 governs coordination between aspects within one Self through the Self's integration architecture: the Self-level governance content, cross-aspect coordination rules, and the aspect-level governance structures that operate under unified Self-level authority. This coordination is intra-Self because a single governance authority holds the three rights over all aspects being coordinated.

Paper 3 governs coordination between aspects from different Selves through the shared substrate. The shared substrate is a coordination medium that spans the home perimeters of the participating Selves; its governance configuration is substrate content held under joint authority across those Selves' governance structures. This coordination is inter-Self because independent governance authorities each hold the three rights over one or more of the contributing aspects.

**The boundary:** Apply the governance authority independence test. If one authority holds the three rights over all coordinating aspects, Paper 2 governs the coordination through that Self's integration architecture. If independent authorities each hold the three rights over different participating aspects, Paper 3 governs the coordination through the shared substrate.

An important edge case follows from this: a Self participating in an FAI event continues to operate its home Paper 2 governance architecture throughout the event — for all intra-Self coordination that continues during the FAI event. The FAI event does not suspend Paper 2 governance within either participating Self; it adds a Paper 3 coordination layer above both home perimeters. Both scopes are active simultaneously during the event, applying to different coordination relationships.

---

## 4. Boundary Case 2 — Intra-Self mating versus inter-Self FAI

Paper 2 defines mating as a governed lifecycle operation combining two or more parent entities' content to produce outputs, with three pattern variants: full union, selective merge, and lineage-preserved union. This operation applies at cell, aspect, and Self scope within one Self, governed by the Self's home governance authority.

Paper 3 defines the FAI event as the canonical operation over the shared substrate, combining aspects contributed by participating Selves. The same three pattern variants apply at the inter-Self scope. The structural parallel between intra-Self mating and inter-Self FAI is direct: both use the same merge primitive, the same three pattern variants, and the same provenance-preservation options. What differs is the scope and governance structure.

**The boundary:** Apply the governance authority independence test. If the aspects being combined are both governed by the same home governance authority, the combination is a Paper 2 mating event. If the aspects being combined are governed by independent home governance authorities, the combination is a Paper 3 FAI event.

This boundary has a practical implication: the choice of pattern variant (full union, selective merge, lineage-preserved union) does not determine which paper applies. Either pattern variant can appear in a Paper 2 mating event or in a Paper 3 FAI event. The governance authority structure over the participating aspects is the only operative distinction.

---

## 5. Boundary Case 3 — Home-generated versus FAI-origin action-feedback

This is the most operationally subtle of the three boundary cases, because it involves a situation where Paper 2's mechanism applies to Paper 3-origin content.

Paper 2's action-feedback mechanism processes action-layer records: operational evidence accumulates in each cell's action layer, is surfaced as proposals through the proposal-and-acceptance machinery, and can result in directed selection updates to DNA. This mechanism operates entirely within each Self's home governance perimeter.

Paper 3's FAI event, at dissolution, feeds content back into participating Selves' home substrates through layer-routing: action-layer content from the shared substrate enters each participating Self's home action layer through the home ingestion mechanism. Once inside the home action layer, that content is processed by Paper 2's action-feedback mechanism — the same mechanism that processes home-generated action-layer content.

**The boundary:** The provenance of the action-layer record determines which scope governs its origin.

- **Home-generated action-layer content** — produced by the Self's own cell operations without FAI input — is governed by Paper 2's action-feedback mechanism at every stage. No inter-Self provenance applies.
- **FAI-origin action-layer content** — content that entered the home action layer through FAI dissolution ingestion — is processed by Paper 2's action-feedback mechanism, but its provenance is Paper 3 origin. That provenance must be maintained through the Paper 2 processing. Losing provenance at the transition point breaks the accountability chain across the P3↔P2 seam.

The governance bridge at this boundary is provenance maintenance. Paper 2's action-feedback mechanism governs the processing; Paper 3's provenance requirements govern the record's attributability. Both apply simultaneously to the same content. A governance architecture that passes FAI-origin content through Paper 2's action-feedback mechanism while stripping the FAI-event provenance satisfies neither paper's requirements correctly.

The practical implication: governance practitioners should treat FAI-origin provenance as a required attribute of action-layer records that persists through the vertical evolution process, not as metadata that can be dropped when the content crosses from the shared substrate into the home action layer.

---

## 6. Simultaneous governance at dissolution

FAI dissolution is where the P3↔P2 boundary is most visible and most important to understand correctly.

At the close of an FAI event, the shared substrate dissolves and content propagates to each participating Self's home substrate under governance-configured ingestion. This dissolution moment is not a strict handoff from Paper 3 to Paper 2. Both papers' governance applies simultaneously to different aspects of the same event:

- **Paper 3 governs what flows from the shared substrate:** which content propagates, under what provenance depth, under what ingestion configuration authored as substrate content under joint authority.
- **Paper 2 governs what home governance does with the flows:** the absorption of content into home substrates, the action-feedback processing of ingested action-layer content, the directed selection decisions over ingested DNA-layer content.

These are not sequential — Paper 3 governance over what flows does not complete before Paper 2 governance over what to do with flows begins. They apply to different aspects of the same dissolution moment. A practitioner who treats dissolution as purely a Paper 3 event will miss the Paper 2 governance obligations that activate at the home perimeter as ingestion occurs. A practitioner who treats dissolution as purely a Paper 2 event — absorption and processing under home authority — will miss the Paper 3 provenance requirements and ingestion-configuration governance that bind on what the home perimeter receives.

The lifecycle isolation principle reinforces this: each participating Self's home governance processes — including the action-feedback mechanism, lifecycle operations, and directed selection — continue operating throughout the FAI event under Paper 2 governance. The FAI event operates above the home perimeter, not instead of it.

---

## 7. Prior-art significance

The three boundary cases and the governance authority independence test establish, with precision, where Paper 2 governance ends and Paper 3 governance begins, and where the two papers apply simultaneously.

Adversarial claims that Paper 3's scope is unclear — that it is indeterminate where Paper 2 governance applies and where Paper 3 governance applies — must address these specific boundary cases. The governance authority independence test provides a single deterministic criterion that resolves Cases 1 and 2 without ambiguity. Case 3's provenance-through-mechanism requirement establishes that the two papers are not incompatible at the action-feedback boundary but that they impose joint requirements on the same content.

Adversarial claims that Paper 2 and Paper 3 overlap inappropriately — that one paper's scope encroaches on the other's — must also address these boundary cases. The papers do not encroach on one another; at dissolution and in FAI-origin action-feedback processing, both papers' governance applies by design to different aspects of the same events. That simultaneous application is what the four-locus evolution-feed architecture requires: Paper 3-origin content must flow into Paper 2's existing evolution mechanisms without Paper 3's provenance requirements being lost in the transition.

---

*This work derives from and formalizes commitments across the CKS theory trilogy: "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026), and "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026).*
