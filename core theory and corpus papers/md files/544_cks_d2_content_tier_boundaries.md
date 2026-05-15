# FAI Content Tier Boundaries at Aspect Contribution

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When a Self contributes an aspect to the shared substrate during a Full Aspect Integration (FAI) event, not all of the contributing Self's governance content enters the shared substrate. This note formalizes the tier boundaries that govern what enters, drawing on the three-tier architecture established in Paper 2 (cell, aspect, Self) and the aspect-as-exchange-unit commitment of Paper 3. The default aspect contribution is a two-tier disclosure: cell-level content is surfaced through the contributed aspect, and aspect-level content is directly contributed. Self-level integration content — the contributing Self's cross-aspect coordination architecture — remains within the home perimeter by default. Self-level content can enter the shared substrate only through explicit governance decision expressed in the sharing scope configuration. This default boundary is a governance privacy mechanism: organizations can coordinate at domain scope through aspect contribution without disclosing their full integration architecture. The note formalizes the three tiers, the conditions for tier elevation, the governance consequences of the boundary, and an operational test for verifying tier compliance in a deployed FAI event.

---

## 1. Why tier boundaries require formalization

Paper 3 establishes the aspect as the unit of exchange in FAI: when a Self contributes to the shared substrate, it contributes aspects, and the constituent cells, DNA-layer content, and action-layer content of those aspects surface into the shared substrate. This exchange-unit framing answers what travels during FAI. It does not, on its own, answer a second question: at what structural depth does the contribution stop?

The three-tier architecture from Paper 2 makes this a non-trivial question. A Self in the Paper 2 architecture organizes at three distinct structural levels — cells are the operational units, aspects group cells around a coordination purpose, and the Self integrates across all aspects into a coherent organizational whole. Each level carries its own DNA layer and action layer: governance architecture specific to that level of organization. When a Self contributes an aspect to the shared substrate, governance content exists at all three levels simultaneously. The question of tier boundaries is the question of which levels' governance content enters the shared substrate and which does not.

This question has governance consequences far beyond bookkeeping. The Self level is where an organization's full integration architecture lives: how it coordinates across all domains, how its aspects relate to one another, what its overall operational strategy is. If aspect contribution silently drew in Self-level content, FAI participation would effectively require each contributing organization to disclose its full governance architecture to every FAI partner. That would make FAI impractical for any organization with sensitivity about its internal integration design — which, in practice, includes most organizations operating in competitive or regulated environments.

D2.49 formalizes the tier boundaries as a named architectural commitment. The formalization draws on D1.06 (aspect as exchange unit) and the Paper 2 three-tier structure.

---

## 2. The three tiers and what enters the shared substrate

Paper 2 establishes three structural levels within a Self, each with its own DNA layer (governance specifications: orchestration rules, coordination rules, purpose statement, content-domain specification) and action layer (operational records of execution at that level).

### Tier 1 — Cell-level content (surfaced through aspect)

The cells that constitute the contributed aspect each carry cell-level DNA-layer content and cell-level action-layer content. Cell DNA-layer content includes each cell's orchestration rules, harness substrate references, and content-domain specification. Cell action-layer content includes each cell's operational records — the accumulated history of that cell's execution.

When an aspect is contributed to the shared substrate, the cell-level content of its constituent cells is **surfaced** into the shared substrate through the aspect. The organizational framing matters: cell content enters the shared substrate as organized under the contributed aspect's governance structure. It is accessible within the shared substrate through the aspect of origin. The cells do not enter the shared substrate as free-standing entities; they enter as the constituent operational layer of the contributed aspect.

Cell-level content enters the shared substrate as a consequence of aspect contribution. No additional governance configuration is required to bring cell-level content into scope — it is part of what aspect contribution means.

### Tier 2 — Aspect-level content (directly contributed)

The contributed aspect itself carries aspect-level DNA-layer content and aspect-level action-layer content. Aspect DNA-layer content includes the aspect's own coordination rules, purpose statement, content-domain specification, and membership structure (which cells belong to this aspect and under what organizational logic). Aspect action-layer content includes the aspect's coordination history — the operational record of how this aspect has coordinated its cells over time.

Aspect-level content is **directly contributed** to the shared substrate. This content is the aspect's own governance architecture — it belongs to the aspect as a structural level, not to any individual cell within it. It is the content that defines what the aspect is and how it operates, and it travels with the aspect as part of the contribution.

Together, Tier 1 and Tier 2 constitute the default scope of an aspect contribution. When governance configures an FAI event and specifies that Self A will contribute aspect X, the shared substrate receives aspect X's own governance architecture (Tier 2) and the cell-level governance content of all cells within aspect X (Tier 1). Nothing further enters by default.

### Tier 3 — Self-level content (home perimeter by default)

The contributing Self carries Self-level DNA-layer content and Self-level action-layer content. Self DNA-layer content includes the Self's cross-aspect coordination rules, the Self's integration architecture (how it organizes and coordinates across all aspects), the Self-level purpose statement, and expression specifications. Self action-layer content includes the Self's cross-aspect operational records — the record of how the Self has coordinated across its entire aspect portfolio over time.

Self-level content **does not enter the shared substrate through aspect contribution by default.** It remains within the home perimeter. An observer with full visibility into the shared substrate sees what aspects have been contributed (Tier 2) and the cells within those aspects (Tier 1), but sees nothing about how the contributing Self organizes across all its aspects, how its governance distributes authority at the Self level, or what its overall integration architecture looks like.

This is the default. It is not a limitation on what FAI can carry — it is a governance privacy protection that the architecture provides automatically unless explicitly overridden.

---

## 3. Tier elevation: when Self-level content can be contributed

Self-level content is not permanently excluded from the shared substrate. The sharing scope configuration (the governance-configurable first dimension of FAI event specification) can be extended to include Self-level content through explicit tier elevation.

Tier elevation means that the sharing scope configuration explicitly specifies Self-level content as in scope for the FAI event. This is not a consequence of contributing more aspects or more cells; it requires a separate, explicit governance decision to include the contributing Self's integration architecture in the contribution.

Several consequences follow from explicit tier elevation:

**What becomes visible.** A participating Self that contributes Self-level content surfaces its cross-aspect coordination architecture into the shared substrate. FAI partners can observe not only what the contributing Self does in the specific domains covered by contributed aspects, but how the contributing Self organizes across all domains — how aspects relate to one another within the Self, what the Self-level integration logic is, and what the overall governance design looks like.

**The governance requirement.** Because Self-level content disclosure is a materially different kind of disclosure than aspect-level disclosure, the governance decision to elevate must be explicit. Governance cannot arrive at tier elevation by accident through a sharing scope configuration that was intended only to specify which aspects to contribute. The configuration must name Self-level content as in scope. This explicitness requirement is the architectural protection against unintended disclosure.

**Why elevation is sometimes appropriate.** There are FAI configurations where Self-level integration architecture is precisely what partners need to coordinate effectively — particularly in close institutional partnerships where the goal is not just domain-level coordination but deep integration of governance architectures across two or more Selves. In these cases, tier elevation is the correct configuration. The architecture does not prohibit it; it requires that it be chosen consciously.

**The default is not elevation.** Standard aspect contribution — specifying which aspects each Self contributes — does not trigger tier elevation. Sharing scope configuration is by default aspect selection without tier elevation. A configuration that names five aspects for contribution does not implicitly include the contributing Self's integration architecture; that would require explicit tier elevation in addition to aspect selection.

---

## 4. Why the tier boundary matters

The tier boundary between aspect-level and Self-level content has architectural consequences across three downstream mechanisms.

### 4.1 Governance privacy

The most direct consequence is governance privacy: the default tier boundary protects each contributing Self's full integration architecture from exposure in every FAI event. An organization that participates in FAI across multiple domains, with multiple partners, over multiple events, does not cumulatively disclose its full governance architecture through those participations. Each event discloses the aspects contributed in that event (Tiers 1 and 2) and nothing more, unless tier elevation is explicitly configured.

This governance privacy property is what makes FAI adoptable at scale. An organization evaluating whether to participate in an FAI event with a partner — potentially a competitor, a regulator, or an organization operating under different governance norms — can reason about what it is disclosing: the governance architecture of specific aspects contributed. It does not have to accept that participation discloses its entire integration architecture. The bounded nature of the default disclosure makes the risk calculus tractable.

### 4.2 Conflict resolution scope

Conflict handling within the shared substrate operates over the content present in the shared substrate. Because Self-level content is not present by default, conflict handling during a standard FAI event operates over cell-level and aspect-level content from contributing Selves. Conflicts between the contributed aspects of different Selves — how their coordination rules interact, how their cell memberships overlap, how their operational histories are compatible — can be identified, preserved, and resolved within this scope.

Conflict resolution does not require exposing the Selves' full integration architectures to operate. Two Selves can have their contributed aspects in the same shared substrate, work through conflicts between those aspects through orchestration-configured resolution, and complete the FAI event — all without either Self's integration architecture having been present in the shared substrate. The scope of conflict resolution is bounded by what is in the shared substrate, and the tier boundary is what determines that scope.

### 4.3 Evolution feed granularity

FAI events feed back into each participating Self's evolution mechanisms. DNA evolution from FAI absorbs orchestration patterns, schemas, or rules from another Self's contributed aspects into the receiving Self's DNA. Action-feedback evolution operates on outcomes recorded during the FAI event. The granularity of what is available for absorption is bounded by what entered the shared substrate.

Where tier elevation has not occurred, evolution feed operates over cell-level and aspect-level content from contributing Selves. The receiving Self can absorb cell-level operational patterns and aspect-level coordination architectures from FAI partners, but does not absorb Self-level integration architecture — because that content was not present in the shared substrate. Where tier elevation has occurred, Self-level content is present in the shared substrate and becomes available for evolution absorption, subject to the receiving Self's governance-configured ingestion policy.

The tier boundary thus determines not only what is disclosed during the FAI event but what becomes available as evolution input afterward. This makes tier boundary governance consequential not just for the event itself but for the long-term evolution trajectories of participating Selves.

---

## 5. Tier boundary as sharing scope mechanism

The sharing scope configuration — the governance-configurable dimension that specifies what each Self contributes to a given FAI event — can be understood through the lens of the tier boundary as performing two distinct operations:

**Aspect selection** is the primary operation: governance specifies which aspects each contributing Self contributes. This is the operational core of sharing scope configuration in standard FAI events. Aspect selection determines which domains enter the shared substrate, which cells are surfaced through those aspects, and what the operational footprint of the FAI event is.

**Tier elevation** is an optional secondary operation: governance explicitly extends the sharing scope to include Self-level content from one or more contributing Selves. Tier elevation is not implied by aspect selection. Adding more aspects to the contribution does not trigger tier elevation. Tier elevation requires a separate governance specification naming Self-level content as in scope.

This two-operation structure means the sharing scope configuration has a natural default posture — aspect selection without tier elevation — and a named extension — aspect selection plus tier elevation. Governance authoring a sharing scope configuration can reason clearly about which posture it is in and whether it has made an explicit decision about tier elevation.

The absence of tier elevation in a sharing scope configuration should be a named affirmative governance position, not an oversight. The recommended practice is for governance to explicitly confirm the tier posture when authoring the sharing scope: "this configuration contributes aspects X, Y, Z at aspect scope (no tier elevation)" rather than simply listing the aspects and leaving the tier posture implicit.

---

## 6. Anti-pattern: unintended Self-level exposure

The most operationally significant failure mode this formalization is designed to prevent is unintended Self-level exposure: a sharing scope configuration that includes Self-level content when the governance authors intended only to contribute specific aspects.

This failure mode is possible because sharing scope configuration is substrate content authored by humans under governance authority — it is subject to authoring errors. A governance author who does not understand the tier boundary may write a sharing scope configuration that reaches into Self-level content without intending to, believing they have specified only aspect contribution. The content that enters the shared substrate is then more revealing than governance intended.

The operational protection against this failure mode is explicit tier-posture confirmation in sharing scope authoring. Governance should confirm two things when authoring a sharing scope: (1) which aspects are included (aspect selection), and (2) whether Self-level content is explicitly included (tier elevation yes/no). A sharing scope configuration that has confirmed both dimensions leaves no ambiguity about what enters the shared substrate.

Where a sharing scope configuration omits tier-posture confirmation, auditors and governance reviewers should treat the omission as a compliance gap, not an implicit answer. Tier elevation is a consequential governance decision; it should not be inferred from silence.

---

## 7. Operational test

For a given FAI event and its associated shared substrate, the following test verifies compliance with the tier boundary formalization:

1. **Content classification.** For each item of content present in the shared substrate (DNA-layer entries, action-layer records, governance structures), can an observer classify it as cell-level content (surfaced through a contributed aspect), aspect-level content (directly contributed as part of a contributed aspect's own governance), or Self-level content (contributed as part of a contributing Self's integration architecture)?

2. **Self-level authorization check.** For any content classified as Self-level, does the sharing scope configuration for this FAI event include an explicit tier elevation specification authorizing Self-level content from the relevant contributing Self? If Self-level content is present without explicit tier elevation authorization, the configuration is non-compliant with the tier boundary.

3. **Absence of unclassifiable content.** Is there content in the shared substrate that cannot be classified as Tier 1, Tier 2, or Tier 3? Such content would indicate that the contribution mechanism has surfaced content outside the tier framework, which is a structural anomaly requiring governance review.

4. **Tier-posture confirmation audit.** Does the sharing scope configuration for this FAI event include an explicit tier-posture statement confirming whether tier elevation was or was not included? If no tier-posture statement is present, flag for governance review regardless of what content is actually in the shared substrate.

A shared substrate that passes all four checks instantiates the tier boundary formalization correctly. A shared substrate that fails check (2) has Self-level content present without governance authorization. A shared substrate that fails check (4) has an incomplete sharing scope configuration that, while it may happen to be correct in content, lacks the explicit governance confirmation that makes the configuration auditable.

---

## 8. Conclusion

The tier boundary formalized in D2.49 specifies what enters the shared substrate when a Self contributes an aspect during a FAI event. Cell-level content is surfaced through the contribution (Tier 1); aspect-level content is directly contributed (Tier 2); Self-level integration content stays within the home perimeter by default (Tier 3 default position). Self-level content can enter the shared substrate only through explicit tier elevation in the sharing scope configuration — an explicit governance decision that the contributing Self's full integration architecture should be present in the shared substrate for the event.

The tier boundary is a governance privacy mechanism. It is what allows organizations with sensitive integration architectures to participate in FAI at domain scope without disclosing their full organizational governance design to every FAI partner. This bounded disclosure property is what makes FAI practically adoptable rather than theoretically available. Organizations can reason about what any specific FAI participation discloses — the contributed aspects and their constituent cells, no more — and govern their participation accordingly.

The anti-pattern this formalization guards against is unintended tier elevation: a sharing scope configuration that includes Self-level content without an explicit governance decision to do so. The operational protection is explicit tier-posture confirmation in sharing scope authoring, making the tier boundary a visible governance checkpoint rather than a background default that may or may not have been considered.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Content Tier Boundaries at Aspect Contribution.* May 15, 2026. ORCID: 0009-0004-8065-3235.
