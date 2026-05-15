# Composition Pair 8: Conflict Carry-Through and Vertical Evolution

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When two Paper 3 sub-commitments are applied simultaneously — conflict carry-through annotations (D1.16) and the FAI-and-vertical-evolution mechanism (D2.57) — three governance requirements emerge that are not apparent from either commitment alone. First, the tier at which a carry-through annotation enters the home substrate hierarchy determines its full propagation path and the timeline along which Self-level governance receives the signal; this entry tier must be tracked explicitly. Second, carry-through annotations traversing the vertical hierarchy must carry supplementary metadata identifying their origin, or upper-tier governance cannot distinguish inter-Self conflict signals from home-generated content, producing the vertical propagation break (AP-15). Third, multiple cell-level carry-through annotations from the same Full Aspect Integration (FAI) event must be aggregated into a coherent pattern view before reaching Self-level governance; that aggregation logic is authored orchestration content, not an automatic property of the propagation mechanism. Together these three requirements constitute the governance specification for "inter-AI conflict signals informing organizational governance at multiple levels."

---

## 1. Pair Identification

**Commitment A — Conflict Carry-Through Annotations (D1.16).** When a FAI event preserves conflicts rather than resolving them, those preserved conflicts do not disappear at dissolution. They become carry-through annotations entered into each participating Self's home action layer as substrate content — flagging, in human-legible form, the specific governance boundaries that the FAI event surfaced. The annotations are action-layer content: they record what happened (which conflict classes, which Selves, what the two sides were) and carry that record into the home perimeter under home governance authority.

**Commitment B — FAI and Vertical Evolution (D2.57).** Paper 2's vertical evolution mechanism operates at cell, aspect, and Self scope within each home substrate. FAI-origin action-layer records are eligible to propagate upward through this hierarchy: a record that enters at the cell tier can inform aspect-level governance, which can in turn inform Self-level governance. This is the same vertical propagation mechanism that carries any home action-layer content upward — carry-through annotations are not exempt from it and are not given special treatment by it.

The composition scenario: a FAI event generates several preserved conflicts. Each produces a carry-through annotation that enters the action layer of one or more home substrates. Under Commitment B, these annotations are now candidates for vertical propagation toward Self-level governance. Both commitments apply simultaneously, and the joint application generates requirements that neither specifies independently.

---

## 2. Governance Scenario Requiring Both Simultaneously

Self A and Self B complete a FAI event. Three conflicts were preserved: one between Cell X (a cell in Self A's contributed Aspect P) and Self B's corresponding content; one between Cell Y (in the same Aspect P) and Self B's content; and one between Aspect P as a whole and Self B's parallel aspect. At FAI dissolution, these conflicts become carry-through annotations.

The cell-level annotations for Cells X and Y enter the action layer of those cells — cell tier. The aspect-level annotation for Aspect P enters the action layer of Aspect P — aspect tier. Under Commitment B (D2.57), all three annotations are now eligible to propagate upward through Paper 2's vertical evolution hierarchy.

The question this scenario poses is not answered by either commitment individually: how does each annotation travel through the hierarchy, how does its transit affect the governance intelligence it carries, and what does Self-level governance receive when multiple annotations from the same FAI event arrive via different paths?

---

## 3. Non-Obvious Governance Requirements

### Requirement 1 — Entry Tier Determines Propagation Path

The tier at which a carry-through annotation enters the home substrate is not uniform across FAI conflicts. A conflict that originated between a specific cell and the partner Self's content enters at the cell tier and must traverse cell → aspect → Self to reach top-level governance. A conflict that originated between two contributing aspects enters at the aspect tier and needs only one propagation step. The difference is not cosmetic: it is the difference between a signal that reaches Self-level governance after two propagation steps versus one.

This matters because propagation steps take time and consume governance attention. Self-level governance making coordination decisions about whether to pursue a second FAI event with Self B, or to reconfigure which aspects participate, needs the conflict signals promptly. An annotation that entered at cell tier but is delayed or dropped at the aspect tier represents lost governance intelligence.

The entry tier is therefore the critical parameter for any carry-through annotation that will traverse the vertical hierarchy. Governance must record it explicitly — not infer it retroactively from the annotation's content — because it determines the annotation's full propagation path and the governance intelligence value timeline: how quickly Self-level governance receives the signal. Neither D1.16 (which specifies that annotations exist and carry certain content fields) nor D2.57 (which specifies that FAI-origin action-layer records propagate upward) individually requires entry-tier tracking. The requirement becomes visible only when both commitments apply simultaneously.

### Requirement 2 — Carry-Through Annotations Require Vertical-Propagation-Specific Metadata

Paper 2's vertical evolution mechanism propagates action-layer content upward as proposals or inputs to higher-tier governance. When aspect-tier governance receives a proposal derived from action-layer content, the standard metadata identifies which cell the content came from and which action sequence produced it. This is sufficient for home-generated content.

Carry-through annotations are not home-generated content. They originated in an inter-Self FAI event. If they arrive at aspect-tier or Self-tier governance carrying only standard action-layer metadata, the receiving governance tier has no way to determine: (a) that this is a FAI conflict annotation rather than a home-generated conflict; (b) which aspect and cells generated the conflict during FAI; (c) which FAI event the annotation belongs to.

Without this identification, the annotation is indistinguishable from ordinary home conflict content. The governance response to a home-generated conflict is different from the appropriate response to a carry-through signal from a specific inter-Self event. Conflating them produces wrong governance responses — and, specifically, produces the failure mode identified as AP-15 (vertical propagation break): FAI conflict signals reaching upper-tier governance in a form that governance cannot act on correctly, because the origin information was lost in transit.

The metadata required to prevent AP-15 is: (1) entry tier at the home substrate; (2) full propagation path from entry tier to current tier; (3) FAI event reference identifying which inter-Self event produced the conflict; (4) identification of which aspects and cells on each side of the FAI event generated the conflict. These four fields supplement — they do not replace — standard carry-through annotation content (Selves involved, conflict classes, the two sides). Together they enable every tier of governance that encounters the annotation to recognize it as FAI-origin and act appropriately.

This metadata requirement is a composition-specific requirement. D1.16 specifies carry-through annotation content for home-perimeter governance. D2.57 specifies that FAI-origin action-layer content propagates upward. Neither specifies what the annotation must carry to remain recognizable as FAI-origin after vertical transit. The requirement is visible only at the intersection.

### Requirement 3 — Self-Level Governance Receives Aggregated Pattern Views

A single FAI event between Self A and Self B may produce multiple carry-through annotations entering at different tiers and via different propagation paths through different aspects. By the time they approach Self-level governance, they represent a pattern — not isolated signals. The pattern has meaning that no individual annotation carries: "FAI event X with Self B surfaced boundary issues across Aspect P (cell-level conflicts in Cells X and Y) and at the aspect level itself, suggesting that the coordination surface between these two Selves at Aspect P's scope requires governance attention."

Self-level governance cannot construct this pattern view automatically. The vertical propagation mechanism moves individual records upward; it has no native aggregation logic over records sharing the same FAI event reference. Without authored aggregation, Self-level governance receives a set of individually-propagated carry-through annotations from the same event, with no mechanism connecting them. The pattern view — the governance intelligence that the combination is supposed to deliver — is absent.

The aggregation logic must be authored as orchestration content in the proposing substrate. It is a composition-specific requirement: the need for it arises only when carry-through annotations (D1.16) are being vertically propagated (D2.57), and only when multiple annotations from the same FAI event are in transit simultaneously. The aggregation content identifies records sharing a FAI event reference, collects entry-tier and propagation-path information across them, and presents a consolidated pattern view to Self-level governance alongside the individual annotation details.

---

## 4. Prior-Art Significance

Any system implementing "inter-AI conflict signals informing organizational governance at multiple levels" must address all three requirements above. The entry-tier-determines-propagation-path requirement means that conflict signal architecture must track where in the receiving hierarchy a signal enters, not merely that a signal was received. The metadata requirement means that inter-AI conflict signals must carry sufficient origin information to remain identifiable after transit through the receiving system's governance hierarchy — failure to satisfy this is the AP-15 failure mode. The aggregation requirement means that organizational governance at the top level must receive pattern-synthesized views of inter-AI events, not raw aggregations of individual signals.

Systems that route inter-AI conflict notifications directly to a top-level governance layer without entering the receiving hierarchy skip the vertical propagation problem but lose the intermediate governance value — aspect-tier and cell-tier governance authorities who are closer to the content do not receive the signal. Systems that enter the hierarchy without supplementary origin metadata produce the AP-15 failure. Systems that enter the hierarchy with correct metadata but without authored aggregation logic deliver unconnected signals to Self-level governance, defeating the pattern-view purpose of carry-through annotations.

The three requirements are jointly necessary. Satisfying any two while failing the third produces a governance system that partially implements the composition but fails to deliver the full governance intelligence the pair is designed to provide.

---

## 5. Operational Test

For carry-through annotations from a completed FAI event, an observer should be able to verify:

**(a) Entry tier recorded.** For each carry-through annotation produced by the FAI event, can the observer determine the tier at which the annotation entered the home substrate — specifically, whether it entered at cell tier (because the conflict originated between a specific cell and the partner Self's content) or at aspect tier (because the conflict originated between contributing aspects)? If entry tier is not recorded as an explicit field, the requirement is not met.

**(b) Vertical-propagation metadata present.** For any carry-through annotation that has been propagated upward from its entry tier — whether it has moved from cell tier to aspect tier, or from aspect tier to Self tier — does the annotation carry the four supplementary metadata fields (entry tier, propagation path, FAI event reference, contributing aspects and cells)? If aspect-tier or Self-tier governance cannot identify the annotation as FAI-origin by inspection of the annotation's content, the requirement is not met and AP-15 conditions are present.

**(c) Aggregated pattern view at Self level.** When Self-level governance receives carry-through signals from a FAI event that produced multiple annotations (entering at cell or aspect tier from different cells and aspects), does governance receive a synthesized pattern view — a coherent summary identifying which aspects and cells surfaced boundary issues and attributing them to the specific FAI event — in addition to individual annotation records? If Self-level governance receives only individual records with no authored aggregation, the requirement is not met.

All three tests must pass for the composition pair to be correctly implemented. Entry tier must be tracked (Requirement 1), origin metadata must be present at each propagation step (Requirement 2), and authored aggregation must synthesize the pattern view at Self-level governance (Requirement 3).
