# Provenance Internalization Governance at FAI Dissolution

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When an FAI event dissolves and each participating Self internalizes evolution outputs into its home substrate, a governance decision must be made: how much provenance from the FAI event is retained in the home substrate records? Paper 3 names this as Dimension 6 — provenance preservation on internalization — one of the six configurable dimensions of the FAI mechanism. This note, D2.25, formalizes the operational content of that dimension. It specifies three depth options (FAI event reference only; contributing Self reference; full provenance chain), the governance overhead and audit depth tradeoffs of each, and their implications for home action-feedback and DNA absorption attribution. It establishes that depth is governed independently per Self as a home governance decision — not a joint FAI configuration decision — and explains the relationship between Dimension 6 and Dimension 5 (provenance carry-over depth) as two distinct decisions at two distinct perimeter crossings. It names the retrospective provenance loss anti-pattern and provides an operational test for confirming depth configuration.

---

## 1. Position in the derivation series

D2.25 is the operational decomposition of D1.22, Dimension 6 of the six configurable FAI dimensions. D1.22 committed that each participating Self's governance can configure, independently, how much provenance of FAI-origin content is preserved in home substrate records when internalizing evolution outputs at dissolution. D2.25 formalizes what that governance decision consists of: what the options are, what each option implies, and what governance should attend to when choosing.

The parent commitment in Paper 3 reads: "When a Self ingests evolution outputs from an FAI event into home substrate, governance specifies how much provenance detail is retained — supporting later audit, supporting subsequent FAI events that reference prior interactions, or pruned where storage and home cognitive load matter more." D2.25 articulates the decision structure implied by that sentence in operational form.

---

## 2. The internalization decision and why it requires governance specification

At FAI dissolution, two evolution pathways are available to each participating Self (D2.10, D2.11): action-layer ingestion, through which FAI-derived action records enter the receiving Self's home action layers as lived-experience input to action-feedback evolution; and DNA absorption, through which orchestration patterns, schemas, or rules from another Self's contributed aspects are selectively absorbed into the receiving Self's DNA under home governance authorization. Both pathways produce records in the home substrate.

For every such record, a provenance question arises: what does this home substrate record say about where this content came from? The answer is not architecturally prescribed — Paper 3 surfaces it as a configurable dimension under home authority. Governance must specify a depth, because not specifying is itself a choice, and an unexamined choice is a governance gap.

The significance of the decision is asymmetric in the two directions. Under-specification (shallow depth) is irreversible at the home substrate level: once a record is written with minimal provenance, the richer provenance that was available at the shared substrate is no longer accessible from that home record. Over-specification (full chain) carries storage and cognitive overhead that may be unnecessary for the event's accountability needs. The decision should be made deliberately, matched to the receiving Self's accountability context, not defaulted to either extreme.

---

## 3. The two-moment structure: Dimension 5 and Dimension 6

Before specifying the depth options, it is essential to distinguish Dimension 6 from Dimension 5, because both concern provenance and both concern the same FAI event, but they operate at different moments and under different authority.

**Dimension 5 — Carry-over depth at contribution time.** When a Self contributes an aspect to the shared substrate at the start of an FAI event, Dimension 5 governs the provenance depth that travels with that aspect. This decision is made at contribution time, as part of the joint FAI configuration that the participating Selves' governance structures collectively author before substrate construction begins. The authority is joint: the configuration substrate carrying the Dimension 5 setting is authored under joint authority across the participating Selves.

**Dimension 6 — Internalization depth at dissolution time.** When each Self internalizes evolution outputs from the shared substrate into its home records at FAI dissolution, Dimension 6 governs how much provenance is retained in those home records. This decision is made at internalization time, which is after the FAI event has concluded. The authority is home: each Self's own governance structure configures its Dimension 6 setting independently, without requiring agreement from the other participating Selves. The setting governs home substrate records, not shared-substrate records.

The two dimensions are logically complementary: Dimension 5 describes what provenance is *available* on the shared substrate, and Dimension 6 describes what provenance each Self *retains* from that availability. They can be configured independently at any combination. Self A may contribute at full carry-over depth (Dimension 5 deep) while configuring shallow internalization (Dimension 6 shallow), or the reverse. The independence is architectural — two distinct perimeter crossings, two distinct authority holders.

This distinction has a practical consequence: a receiving Self's Dimension 6 setting cannot exceed what Dimension 5 provided. If a contributing Self carried no provenance into the shared substrate, there is nothing to internalize at full depth. The Dimension 6 ceiling is set by Dimension 5; the Dimension 6 floor is set by what the receiving Self's governance decides its accountability needs require.

---

## 4. Three depth options

Governance configuring Dimension 6 chooses among three depth options for home substrate records produced by FAI-origin content.

### Option A — FAI event reference only

Home substrate records carry a reference to the FAI event identifier as provenance. An observer inspecting a home substrate record can determine that this content originated from a specific FAI event, but cannot navigate from that record to the contributing Self or to the shared-substrate content without consulting the shared substrate directly (if it persisted) or the FAI event log separately.

The governance overhead of Option A is the lowest of the three. Home substrate records are compact; no contributing-Self attribution is maintained at the home record level; action-feedback evolution operating over these records treats them as FAI-origin without further attribution. Option A is appropriate for routine coordination events where the receiving Self's accountability needs do not require knowing which participating Self contributed which content — for example, events where the shared substrate contained contributions that the receiving Self's governance authorized without distinguishing sources.

The audit depth provided by Option A is limited to identifying that a class of home records traces to FAI events. This is sufficient for frequency analysis (how often does this Self participate in FAI events, and how much of its current home DNA traces to FAI-origin content?) but insufficient for inter-Self attribution (which Self's approaches is this Self learning from?).

### Option B — Contributing Self reference

Home substrate records carry provenance identifying both the FAI event and the contributing Self or Selves whose aspects were the source of the internalized content. An observer inspecting a home substrate record can determine that this content originated from Self A's contribution in FAI event X.

The governance overhead of Option B is moderate. Maintaining contributing-Self attribution in home records requires that the internalization pathway carry the contributing Self identifier from the shared substrate into the home record at the time of ingestion. This is additional metadata per record but does not require the full aspect lineage chain.

Option B enables two capabilities that Option A does not. First, home action-feedback evolution and DNA absorption attribution can be attributed to source Selves: governance can ask which Self's approaches are appearing in this Self's evolution trajectory. Second, future FAI participation decisions can reference attribution data: if this Self's DNA absorptions from FAI events consistently trace to Self B's contributions, governance may seek to increase FAI frequency with Self B or to examine what about Self B's approaches this Self is finding evolutionarily productive.

For most organizational FAI participation contexts, Option B is the appropriate operating depth. The question "which Self did this learning come from?" is answerable; the question "what was the full governance history of that aspect in the contributing Self's home substrate?" is not, and is typically not required. Option B is the practical default.

### Option C — Full provenance chain preserved

Home substrate records carry the complete provenance chain: FAI event reference, contributing Self identifier, contributing aspect identifier, and the aspect lineage chain back to the origins of that aspect in the contributing Self's home governance. An observer can navigate from the home substrate record all the way back to the contributing Self's governance history for the specific content that was contributed and internalized.

The governance overhead of Option C is the highest of the three. Full provenance chains are larger; maintaining them requires that the contributing Self provided full carry-over depth (Dimension 5 full) so that the lineage chain was available on the shared substrate; and home records are more complex. DNA absorption at Option C depth produces records that embed cross-organizational governance history within the receiving Self's home substrate.

Option C enables complete inter-organizational audit trails. An external auditor examining a receiving Self's home DNA can trace specific content back through FAI events to the contributing Self's original governance decisions — when an aspect was first created, under what authority, through what evolution history. This capability is appropriate for contexts where inter-organizational accountability is formally required: regulated industries where AI system governance must be traceable to specific organizational decisions, multi-party contracts where each party's AI evolution must be auditable by the others, or high-stakes coordination events whose downstream consequences are significant enough to warrant complete traceability.

Option C should be configured when the accountability context demands it. Outside such contexts, the overhead is not warranted, and Option B provides the attribution functionality that most governance needs.

---

## 5. Governance implications for home evolution pathways

The depth option selected for Dimension 6 has different implications depending on which home evolution pathway it applies to.

**For action-layer ingestion (D2.10):** FAI-derived action records entering home action layers are the substrate from which action-feedback evolution operates. At Option A depth, the evolution system knows these records are FAI-origin but cannot attribute them to contributing Selves; the evolution trajectory can be analyzed as "FAI-influenced" without further source granularity. At Option B depth, evolution analysts can identify which Selves' approaches are producing action records that the home Self is accumulating. At Option C depth, the full action-record lineage is available within the home substrate, enabling complete traceability of the home Self's action-layer evolution to specific cross-organizational interactions.

**For DNA absorption (D2.11):** DNA absorption records indicate that a specific piece of the home Self's DNA originated from a FAI event. At Option A depth, the record indicates FAI-event origin without contributing-Self attribution; over time, the home Self's DNA may contain content from multiple FAI events without governance being able to identify differential contributions by source Self. At Option B depth, governance can attribute each DNA absorption to the contributing Self, supporting analysis of which inter-Self learning has been most evolutionarily productive. At Option C depth, the full governance history of absorbed DNA content is available within the home substrate, enabling an observer to understand not only that a DNA element came from Self B via FAI event X, but what the provenance of that element was within Self B's own governance trajectory before it was contributed.

---

## 6. Depth is governed independently per Self

A property that must be stated precisely: Dimension 6 depth is each participating Self's home governance decision, not a joint decision of the FAI event configuration.

Each Self configures its own Dimension 6 depth for its own home substrate records. Self A may configure Option C while Self B configures Option A for the same FAI event. Neither Self's choice constrains the other. The depth choice governs the receiving Self's home records — records that exist within the receiving Self's home perimeter under that Self's governance authority — not the shared substrate records, which are joint.

This independence means that the same FAI event can produce home substrate records at different depths in different participating Selves. An external observer comparing the home substrates of Self A and Self B after the same FAI event may find that Self A's records contain full contributing-Self attribution and aspect lineage, while Self B's records contain only FAI event references. Both outcomes are architecturally correct; they reflect different governance configurations by different home authorities.

The practical implication is that each Self must configure Dimension 6 according to its own accountability context rather than coordinating with other participating Selves about a shared depth standard. If an inter-organizational audit standard requires a specific depth across all participating Selves, that standard must be communicated through the joint FAI configuration process and adopted by each Self's home governance independently — it cannot be architecturally imposed from the shared substrate.

---

## 7. Anti-pattern: retrospective provenance loss

The retrospective provenance loss anti-pattern is a specific failure mode in Dimension 6 configuration: configuring shallow internalization depth after having received deep carry-over from a contributing Self.

The pattern proceeds as follows. A contributing Self configured Dimension 5 at full carry-over depth, providing the receiving Self's shared-substrate view with complete provenance chains for its contributed aspects — FAI event reference, contributing Self identifier, aspect identifier, and full aspect lineage. The receiving Self thus has access to full provenance on the shared substrate at dissolution time. However, the receiving Self's governance configured Dimension 6 at Option A depth. The home substrate records produced by internalization carry only FAI event references. The full provenance chain that was available is not retained.

The provenance loss is retrospective because the information was present and accessible at internalization time. The loss is not caused by the contributing Self withholding provenance or by the shared substrate failing to maintain it; it is caused by the receiving Self's governance choosing not to retain it. After internalization, the richer provenance is no longer accessible from the home substrate records. If the shared substrate has since dissolved without a persistence policy that preserves it, the full provenance chain may be unrecoverable.

Governance should avoid this anti-pattern by calibrating Dimension 6 depth to match or exceed its accountability needs — not by defaulting to the shallowest option available simply because that option is technically permitted. The relevant accountability question is not "what is the minimum I am required to retain?" but "what depth of provenance will I need for home governance decisions, future FAI participation analysis, and any inter-organizational audit obligations this event may produce?"

If Dimension 5 provided full carry-over depth, the marginal cost of configuring Dimension 6 at Option B or Option C is the home substrate storage and record overhead — not the work of obtaining the provenance, which was already provided. Discarding available provenance incurs irreversibility costs that are often larger than the overhead costs it avoids.

Symmetrically, there is no anti-pattern in choosing Option A when the contributing Self provided only Option A carry-over depth (Dimension 5 shallow). In that case, the full provenance chain was not available, and configuring Dimension 6 at Option A simply reflects the ceiling that Dimension 5 established. The anti-pattern is specifically the mismatch: deep provision, shallow retention.

---

## 8. Operational test

A participating Self's Dimension 6 configuration is correctly applied if and only if the following conditions hold for FAI-origin records in that Self's home substrate:

1. **Depth is readable from the record.** An observer examining a home substrate record that originated from an FAI event can determine, from the provenance fields of that record, which depth option was applied: whether the record carries only a FAI event reference (Option A), a FAI event reference plus contributing Self identifier (Option B), or a complete provenance chain including aspect lineage (Option C).

2. **Depth matches configuration.** The depth present in the record matches what the Self's Dimension 6 governance configuration specified for the event class or event instance that produced the record.

3. **Depth is consistent across a single event.** All home substrate records produced by internalization of a single FAI event carry the same depth, unless governance explicitly configured different depths for different record types from the same event (which is architecturally permitted as a governance extension but must be explicitly configured, not produced by inconsistent application).

4. **No higher depth than Dimension 5 provided.** Records do not carry provenance depth that exceeds what the contributing Self's Dimension 5 carry-over depth made available. A record claiming full aspect lineage when the contributing Self provided only FAI event reference is a data integrity failure, not a Dimension 6 misconfiguration.

5. **Anti-pattern check.** For events where Dimension 5 carry-over depth was Option B or Option C, the receiving Self's home records carry at least Option B depth. If Option A depth is present in home records for such an event, governance should confirm whether this was an explicit governance decision (appropriate accountability context for Option A) or an unreflective default that discarded available provenance (retrospective provenance loss anti-pattern).

---

## 9. Summary

D2.25 formalizes the governance decision structure for Dimension 6 — provenance preservation on internalization — as committed in D1.22. The three depth options (FAI event reference only; contributing Self reference; full provenance chain) represent a tradeoff between governance overhead and audit depth, with Option B as the appropriate default for most FAI participation contexts, Option A for routine events where inter-Self attribution is not required, and Option C for high-accountability contexts where complete inter-organizational traceability is required.

Depth is governed independently per Self as a home governance decision, not a joint FAI configuration decision. It operates at dissolution/internalization time, after the FAI event concludes, under each Self's own authority.

Dimension 6 and Dimension 5 are independent decisions at different moments — contribution time versus internalization time — with different authority holders, but they interact: Dimension 5 sets the ceiling of what is available; Dimension 6 sets what is retained. Governance should configure Dimension 6 to match its accountability needs and should not default to shallow depth after receiving deep carry-over, as this produces irreversible provenance loss at the home substrate level.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Provenance Internalization Governance at FAI Dissolution.* May 15, 2026. ORCID: 0009-0004-8065-3235.
