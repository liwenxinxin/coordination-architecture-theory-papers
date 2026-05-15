# FAI and Home Governance Temporal Interleaving

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note ID:** D2.23 (#518)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

A participating Self's home governance does not pause during a Full Aspect Integration (FAI) event, and a FAI event does not pause for home governance operations. These two governance domains run concurrently: the inter-Self perimeter and each home perimeter coexist operationally throughout the event's duration. This note formalizes that concurrency as the **no-pause principle**, identifies four types of home governance decisions that may occur during an active FAI event and specifies how each is handled, examines the governance attention allocation challenge that FAI participation creates, and distinguishes the FAI hand-off boundary from the timing of home evolution processing. An anti-pattern — treating FAI as requiring exclusive governance attention and therefore suspending home operations — is stated and rejected. An operational test for auditing concurrent governance continuity is provided.

---

## 1. Position in the derivation series

D2.23 is an operational decomposition of two D1 sub-commitments. D1.03 established that home perimeters remain intact during FAI: each participating Self's home authority structure continues to operate, and the inter-Self perimeter does not absorb or displace it. D1.01 established that the shared substrate is a temporary construction: it is built for the event, operates for its duration, and dissolves at the event's close.

Together, D1.03 and D1.01 imply a temporal coexistence condition. If home perimeters remain intact and the shared substrate exists only for a bounded period, then the home governance operations that were running before the FAI event began continue running during it, and they will continue running after it dissolves. The FAI event is an interval of additional inter-Self governance activity, not a replacement for or suspension of home governance activity. D2.23 formalizes the operational content of that coexistence: what it means for two governance domains to run concurrently, and what happens when they interact.

D2.17 previously confirmed that home operations continue independently during FAI. D2.23 goes further by specifying the temporal structure of that independence — not merely that it holds, but how it holds operationally, and what specific categories of home governance decision require careful handling because they bear on an active FAI event.

---

## 2. The no-pause principle

**A participating Self's home governance does not pause during a FAI event.** This is the foundational statement of D2.23. It applies in both directions:

Home governance operations — directed selection events, mutation governance, action-feedback evolution, aspect lifecycle events, configuration amendments — continue on their normal schedules throughout the FAI event's duration. The FAI event does not hold authority over home governance timing. The inter-Self perimeter does not require home operations to wait.

Equally, the FAI event does not pause for home governance operations. The shared substrate proceeds on its own operational logic: contributions are active, conflict handling operates, orchestration rules run, exchange bounding is enforced. None of this waits for home governance cycles to complete.

The no-pause principle is not a default that governance can override by choosing to pause; it is what D1.03's home perimeter independence commitment produces in the temporal dimension. A home governance that did pause would be, during the pause, failing to exercise its home authority — a governance continuity failure, not a permissible operational choice.

Practical consequence: governance practitioners managing a participating Self must hold in mind that two governance domains are running simultaneously, each on its own timeline, neither subordinate to the other in scheduling.

---

## 3. Four types of relevant home governance decisions during FAI

Not all home governance decisions made during an active FAI event are consequential for the event. A mutation governance cycle on an aspect unrelated to any contribution to the shared substrate proceeds without any interaction with the FAI event at all. But four categories of home governance decision do bear on the ongoing event, and each requires specific handling.

### Type 1 — Home DNA changes to a contributed aspect

If home governance conducts directed selection on an aspect that is currently contributing content to the shared substrate, the contributed content in the shared substrate is from the prior version of that aspect — the version that was contributed at contribution time. The home DNA change does not retroactively update the shared-substrate content.

This is not an edge case to be resolved by policy; it is an architectural commitment with direct audit consequences. The contribution record established at D2.06 captures the version that was contributed. An observer reviewing the FAI event's shared-substrate content at any point during or after the event should see exactly the version that was contributed, not a version that the home substrate has since superseded. The shared substrate is not a live feed to the home substrate; it is a governed copy of a specific version under joint authority for the event's duration. Subsequent home changes to the contributed aspect are a separate governance event, entirely within home authority, entirely outside the scope of the FAI event.

The implication for home governance practitioners is that directing selection on an aspect currently contributed to a FAI event does not require coordination with the FAI event governance. The two operations are independent. The home change takes effect in the home substrate; the shared substrate retains the version that was contributed.

### Type 2 — Aspect birth or death in the home substrate

If a new aspect is born in the home substrate during the FAI event — created through mutation governance or other home lifecycle processes — the FAI event is unaffected. Newly born aspects are not automatically contributing members of an ongoing event; only the aspects specified in the contributing configuration participate.

Symmetrically, if an existing aspect dies during the FAI event — retires, is dissolved, or is deprecated through home lifecycle governance — the FAI event is unaffected. The contributed content from that aspect remains in the shared substrate under joint authority for the event's duration, even though the source aspect no longer exists in the home substrate. The contribution was made; what happens to the contributing aspect afterward does not reach back to undo it.

Both cases follow directly from the contributed-version principle: the FAI event governs what was contributed, not the current state of the home substrate.

### Type 3 — Configuration amendment decision

If a participating Self's governance determines during an active event that the standing configuration (D2.21) or a per-event configuration parameter should be amended, the governance initiates a configuration amendment through the joint modify right (D2.04). This is the appropriate channel: configuration content is substrate content under joint authority, and amendment requires joint authorization.

Depending on the nature and scope of the amendment, this may pause the FAI event's operation pending joint authorization. Unlike Types 1 and 2, which require no coordination with the event, a Type 3 decision does engage the inter-Self governance channel directly. Governance practitioners should anticipate this: configuration amendments during an active event carry the cost of potential event suspension, and standing configurations established before the event begins reduce the need for mid-event amendment.

### Type 4 — Early dissolution request

A participating Self's governance may determine during the event that early dissolution is warranted — the circumstances that motivated the event have changed, or a governance condition has arisen that makes continuation contrary to the Self's interests. This triggers the escalate tier (D1.15) at the event level. Early dissolution is an available option per D2.14 (Option 4 in the dissolution taxonomy), but it engages the inter-Self escalation pathway and requires handling across the joint authority structure.

The governance decision to request early dissolution is made within home authority. The request's effect on the event is governed jointly. Home governance practitioners should distinguish between the decision to request (entirely home-side) and the processing of the request (inter-Self).

---

## 4. Governance attention allocation

FAI participation creates a governance attention demand that does not exist for a Self operating purely within its home perimeter. During an active FAI event, governance practitioners must allocate attention across two concurrent domains:

The **FAI event domain** includes: monitoring the conflict registry, responding to escalations, reviewing exchange bounding compliance, and — if the event involves standing configurations that may require amendment — configuration management.

The **home governance domain** includes: ongoing directed selection, action-feedback evolution review, mutation governance, aspect lifecycle management, and whatever configuration and oversight activity the home substrate requires on its normal cycle.

This is a governance capacity consideration that parallels the minimal governance capacity boundary case identified in Paper 2 (B6.09). Paper 2 named a boundary condition at which governance capacity falls below what the home substrate requires — where the volume of governance-requiring operations exceeds the practitioners' ability to govern them without degradation. FAI participation adds to the governance load that boundary case describes. An organization that is already near its governance capacity ceiling before FAI participation may find that participation pushes it past the ceiling.

Two architectural features of the FAI design reduce this burden. Standing configurations (D2.21) establish governance parameters before events begin, reducing the decisions that must be made during events. Pre-authorized orchestration rules (D2.15) handle classes of inter-Self interaction through pre-specified logic, reducing the escalation rate during events. Both features front-load governance work to a point in time when practitioners are not also managing concurrent home operations under event pressure.

The practical implication for organizations considering FAI participation volume is explicit: governance capacity assessment should precede commitment to event volume. An organization committing to concurrent FAI events or to high event frequency without assessing its governance capacity is operating in the same territory Paper 2's B6.09 boundary case identifies — governance load that exceeds capacity produces degraded governance, which is a failure mode for both home governance and inter-Self governance simultaneously.

---

## 5. Temporal separation of hand-off from home evolution processing

The FAI hand-off boundary (D1.20) occurs at a defined time: dissolution. At dissolution, the shared substrate closes and the governance-configured ingestion event at each home perimeter processes the content that home governance has authorized to cross from the dissolved shared substrate.

Home evolution processing of FAI outputs — what Paper 3 §7 calls the four-locus mechanism by which FAI events feed back into each participating Self's Paper 2 evolution mechanisms — occurs *after* dissolution, under home governance, on home governance timelines. There is no architectural requirement that home governance run FAI evolution outputs through its evolution mechanisms immediately upon dissolution.

This temporal separation has governance significance. The moment of dissolution and the moment of home evolution processing need not coincide. A participating Self may ingest dissolution content at dissolution and queue it for evolution processing on a governance-scheduled cycle that runs hours or days later. Another Self may process the same content immediately. The asymmetry is permissible; it is one expression of the per-home-perimeter governance authority that D1.03 and Paper 3's asymmetric ingestion commitment jointly produce.

The temporal flexibility at this locus is what makes governance attention allocable efficiently across the two concurrent domains described in §4. Practitioners do not need to surge home evolution processing capacity at the moment of dissolution. They can let the dissolution event complete, record what was ingested, and process the evolution implications on the home substrate's normal governance schedule. The FAI event and the home evolution processing of its outputs are two temporally distinct governance operations, related by content but separated by time and authority.

---

## 6. Anti-pattern: home governance pause

The anti-pattern D2.23 formally rejects is: a Self that halts home governance operations during a FAI event, treating the event as requiring exclusive governance attention.

This anti-pattern may arise from a reasonable intuition: FAI events are complex inter-Self governance operations, practitioners have limited attention, and managing an event well seems to demand focus. The anti-pattern is the error of resolving that attention pressure by suspending home governance rather than by using standing configurations and pre-authorized rules to reduce the FAI monitoring burden.

The anti-pattern produces two harms. First, home governance continuity is broken: aspects that would have undergone directed selection do not; mutation governance cycles are missed; action-feedback evolution that should have run is deferred beyond its intended schedule. This accumulates as governance debt in the home substrate. Second, the anti-pattern misrepresents the architecture: it treats the FAI event as having displaced home authority rather than as having added an additional governance domain alongside it. That misrepresentation, if persistent, shapes the organization's understanding of what FAI participation means — producing a belief that FAI requires exclusive attention that is false to the architectural commitment.

The correct response to governance attention pressure is to reduce the FAI monitoring burden (through standing configurations and pre-authorized rules), to staff governance for concurrent operation, and — if neither is sufficient — to reduce FAI participation volume to a rate that governance capacity can sustain without pausing home operations.

---

## 7. Operational test

For a completed FAI event, an observer auditing the governance record of a participating Self should be able to confirm all of the following:

1. Home governance records show continuous operations during the FAI event period: directed selection events, mutation governance cycles, action-feedback evolution reviews, and lifecycle events appear on their normal schedules throughout the interval the FAI event was active, with no gap attributable to FAI participation.

2. Any home governance decision made during the FAI event that falls into Types 1–4 (§3) is recorded with proper attribution — as a home governance record independent of the FAI event records. Type 1 decisions (home DNA changes) are recorded in home governance history; the contribution record in the shared substrate continues to show the version that was contributed, unchanged. Type 2 decisions (aspect births and deaths) are recorded in home lifecycle records, with no corresponding entry in the FAI event record. Type 3 decisions (configuration amendments) are recorded in both the home governance record (the decision to initiate) and the FAI event record (the joint authorization process). Type 4 decisions (early dissolution requests) are recorded in both records correspondingly.

3. The dissolution event and the home evolution processing of dissolution outputs are recorded as separate events with distinct timestamps, confirming that home evolution processing was governed on home governance timelines and not assumed to be simultaneous with dissolution.

4. No entry in the home governance record indicates that normal governance was suspended, deferred, or placed on hold due to FAI participation.

A home governance record that fails items (1) or (4) evidences the anti-pattern stated in §6. A record that fails item (2) evidences a Type-categorization failure — a home governance change that should have been recorded as independent of the FAI event was instead merged with it, or vice versa. A record that fails item (3) may indicate either that home evolution processing was treated as architecturally required to occur at dissolution (an incorrect assumption) or that the separation between dissolution and evolution processing was not preserved in the governance record.

---

## 8. Conclusion

FAI events and home governance operations run concurrently, with no pause requirement in either direction. The no-pause principle is not a preference but the operational expression of home perimeter independence under D1.03. Four categories of home governance decision bear on an active FAI event — home DNA changes to contributed aspects, aspect births and deaths, configuration amendment decisions, and early dissolution requests — and each is handled through a defined pathway that preserves the independence of the two governance domains. Governance attention allocation is a real capacity consideration that parallels the minimal governance capacity boundary case from Paper 2, and it is the governing reason to invest in standing configurations and pre-authorized orchestration rules before committing to FAI participation volume. The FAI hand-off boundary at dissolution and home evolution processing of FAI outputs are temporally separate events; no architectural requirement collapses them. Home governance pause during FAI is an anti-pattern that breaks home governance continuity and misrepresents the architecture.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI and Home Governance Temporal Interleaving.* May 15, 2026. ORCID: 0009-0004-8065-3235. Note D2.23 (#518) in the CKS Derivation Notes series.
