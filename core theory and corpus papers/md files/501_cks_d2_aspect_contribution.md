# Aspect Contribution Mechanics in FAI

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D1.06 commits that the aspect is the exchange unit in Full Aspect Integration (FAI). D2.06 formalizes what contributing an aspect operationally involves — the steps that must occur, the records that must exist, and the governance acts that must be performed for a contribution to be fully governed. A contribution event has five required elements: (1) aspect selection under governance, (2) provenance carry-over depth determination, (3) a contribution record in the contributing Self's home substrate, (4) a contribution record in the shared substrate, and (5) content structured by aspect-of-origin within the shared substrate. This note defines each element, states what contribution does not mean for the contributing Self's home governance, identifies the anti-pattern of unrecorded contribution, and provides an operational test with three observable artifacts that confirm a contribution is complete.

---

## 1. Position in the derivation sequence

D1.06 established the aspect as the exchange unit in FAI: when a participating Self contributes content to the shared substrate, the contribution surfaces the constituent cells, DNA-layer content, and action-layer content of the contributed aspect. D1.06 is a structural commitment about what the unit of exchange *is*. D2.06 is the operational decomposition of that commitment — what contributing an aspect *involves* as a sequence of governance acts and recorded events.

The decomposition matters because the unit-of-exchange commitment, taken alone, does not specify the governance structure around the act of contribution. It does not say who decides which aspects to contribute, how that decision is recorded, what provenance information travels with the contributed content, or how the receiving substrate organizes what it receives. D2.06 fills those gaps by stating the five elements that together constitute a fully governed contribution event.

---

## 2. The five elements of the contribution event

A contribution event is the act by which a participating Self's governance-selected aspect enters the shared substrate. Five elements are required for the event to be fully governed.

### 2.1 Aspect selection under governance

The contributing Self's governance decides which aspects to contribute to a given FAI event. The selection is governed by the sharing-scope configuration established for the event — a governance-configured set of parameters that specifies which aspects are in scope for contribution, following the configurable dimension structure Paper 3 §8 commits to (D1.22, Dimension 1).

The selection decision is a governance act in the full architectural sense: the contributing Self's governance reviews the aspects it governs, evaluates them against the event's purpose and sharing-scope configuration, and determines which aspects are both relevant and appropriate for contribution. The determination may be performed by humans directly, by LLMs operating under human direction, or by orchestration rules authored by humans — the labor allocation is a deployment decision. What is not a deployment decision is the authority: only the contributing Self's governance can make the selection.

The selection decision is recorded as governance content within the contributing Self's home substrate before contribution proceeds. This recording is the first trace of the contribution event in the governance record.

### 2.2 Provenance carry-over depth determination

Before contributing, governance determines how much of the selected aspect's provenance history travels with it into the shared substrate. This is the provenance carry-over depth determination, corresponding to D1.22 Dimension 5.

An aspect accumulates provenance over time: records of the cells that compose it, the actions that shaped its content, the governance decisions that modified it, and its own prior FAI participation. When the aspect is contributed to a shared substrate, some or all of this history may travel with it. The depth is governance-configured: at minimum depth, only the aspect's current content travels; at greater depth, the history of the content's formation travels alongside it.

The depth determination is itself a governance act. It governs what is "attached" to the contributed content in the shared substrate — and therefore what is available to receiving Selves' governance when they inspect the shared substrate's provenance records. A deeper provenance carry-over gives receiving Selves more context about where the contributed content came from and how it evolved; a shallower carry-over limits what is visible across the inter-Self perimeter. The determination is not a technical parameter; it is a governance decision about information sharing at the perimeter.

### 2.3 Contribution record in the contributing Self's home substrate

When the contribution event occurs, the contributing Self's home substrate records the event. The home contribution record contains at minimum: which aspect was contributed, to which FAI event, at what time, and under what governance authorization.

This record is the contributing Self's own governance documentation that it participated in the FAI event. It is not a copy of the shared substrate record (§2.4); it is the contributing Self's home-governance trace of the act of contribution. Its function is to close the governance loop on the contributing Self's side: after the contribution, an observer examining the contributing Self's home substrate can find evidence that the governance decision to contribute was made, when it was made, and what it authorized.

The home contribution record is permanent governance content in the contributing Self's substrate. It does not dissolve when the shared substrate dissolves. A contributing Self that participated in ten FAI events carries ten home contribution records — one per event — regardless of whether any of those shared substrates persist after their events conclude.

### 2.4 Contribution record in the shared substrate

The shared substrate records the incoming contribution: from which Self, which aspect, at what time, and with what provenance depth. This record satisfies the six provenance fields Paper 1 commits to (A1.07), applied at inter-Self scope as D2.03 formalizes.

The shared substrate contribution record is the inter-Self provenance record. It is what makes the contributed content traceable across the perimeter: any participant in the FAI event, any human exercising their inspect right over the shared substrate, and any receiving Self's governance considering ingestion can consult this record to learn where the content came from and under what governance it was contributed.

The contributed content, once recorded, is shared-substrate content. It falls under the shared substrate's governance perimeter — the joint authority of all participating Selves' governance structures — and is subject to all six Paper 1 commitments within that scope. The content is no longer solely within the contributing Self's home governance perimeter; it is now jointly governed within the shared substrate for the duration of the event.

**The relationship between §2.3 and §2.4:** Both records are required. The home record establishes that the contributing Self's governance authorized and recorded the act. The shared substrate record establishes that the content's origin and provenance are visible to all parties with access to the shared substrate. A contribution with only the home record leaves the shared substrate with content whose origin is not provenance-tracked within the shared scope — the shared substrate's provenance chain is broken. A contribution with only the shared substrate record leaves the contributing Self's home governance without a trace that the contribution occurred — the home-governance loop is unclosed. Full governance requires both.

### 2.5 Content structure by aspect-of-origin within the shared substrate

Once contributed, the aspect's content — its constituent cells, DNA-layer content, and action-layer content — is organized within the shared substrate by aspect-of-origin. The aspect-of-origin structure is the shared substrate's organizational principle for contributed content: an observer examining the shared substrate can identify which contributing Self's aspect provided which content.

The aspect-of-origin structure is not an optional indexing convenience. It does two downstream jobs that the shared substrate's architecture depends on.

First, conflict handling. When content from two contributing Selves' aspects conflicts within the shared substrate, the three-tier conflict-handling mechanism (Paper 3 §6, D1.13–D1.16) needs to know which aspects contributed the conflicting elements. Without aspect-of-origin structure, a conflict surface within the shared substrate cannot be attributed to its source aspects, and the preserve-resolve-escalate mechanism cannot operate at the right level of granularity.

Second, evolution tracing at ingestion. When the shared substrate dissolves and participating Selves' governance considers ingesting content into their home substrates (Paper 3 §7, D1.17–D1.21), the receiving governance needs to know which content came from which contributing aspect. The aspect-of-origin structure makes that attribution available, enabling governed ingestion decisions rather than undifferentiated absorption of the shared substrate's full content.

---

## 3. What contribution does not mean

Three misreadings of the contribution commitment require explicit correction.

**Contribution does not transfer home authority.** The contributing Self's home governance retains full authority over the original aspect — the three rights (inspect, modify, override) apply to the original aspect in the home substrate without modification before, during, and after the FAI event. The shared substrate receives a governed copy of the aspect's content for the duration of the event; the original remains home-governed. This is the architectural feature that makes FAI participation safe: a Self shares without surrendering. A governance structure that required contributing Selves to transfer authority over contributed aspects as a condition of participation would constitute a different architectural pattern — one that concentrates authority at the shared substrate level and reduces participating Selves to subordinate contributors. That is not the FAI architecture.

**Contribution does not expose non-contributed aspects.** Only governance-selected aspects (§2.1) enter the shared substrate. A Self's aspects that were not selected for a given FAI event are not visible within that shared substrate, not subject to that shared substrate's governance perimeter, and not available to other participating Selves through the event. The selection decision at §2.1 is precisely the governance act that limits the inter-Self boundary crossing: what passes through is what governance authorized to pass through.

**Contribution does not require the contributing Self's home aspect to change based on FAI events.** The home aspect is modified only through home governance — by the contributing Self's own governance acting on its own substrate. What happens within the shared substrate during the FAI event (conflict handling, merge operations, evolution feed) does not flow back into the contributing Self's home aspect automatically. If the contributing Self's governance chooses to ingest FAI-derived content into its home substrate, that ingestion is a separate governed act under home governance, not a consequence of having contributed. The direction of governed change is always: home governance acts on home substrate.

---

## 4. Anti-pattern: Unrecorded contribution

The anti-pattern for D2.06 is unrecorded contribution: a participating Self's aspect content appearing in the shared substrate without a contribution record — specifically, without the shared substrate contribution record specified at §2.4.

Unrecorded contribution breaks the provenance chain at the point of inter-Self crossing. The six Paper 1 commitments, inherited by the shared substrate through D1.02, include path retraceability (A1.07's provenance fields). When content enters the shared substrate without a provenance record, path retraceability within the shared scope fails at the first query: "where did this content come from?" cannot be answered from the substrate's own records.

The failure is not merely administrative. Without a provenance record, conflict handling cannot attribute conflicts to their source aspects. Ingestion decisions cannot be made on the basis of aspect-of-origin. The shared substrate's audit trail is incomplete at the boundary where inter-Self coordination actually occurs — exactly the boundary the shared substrate architecture is designed to make transparent.

Unrecorded contribution may arise from several causes: a contributing Self whose governance did not complete the recording step before content was absorbed; a technical implementation that deposited content without triggering the record-creation step; or a governance configuration that treated the shared substrate as a passive repository rather than a governed record. The cause does not affect the status: contribution without a record is ungoverned contribution, and ungoverned contribution violates the shared substrate's inherited Paper 1 commitments.

The home contribution record (§2.3) failing without the shared substrate record (§2.4) produces the same violation by a different path. The home record documents that the contributing Self acted; the shared substrate record documents what entered. Both are required for the contribution to be verifiable from either side of the inter-Self perimeter.

---

## 5. Operational test

For a completed aspect contribution to be fully governed, an observer must find three artifacts:

**Artifact (a) — Selection record in the contributing Self's home substrate.** The contributing Self's home substrate carries a record of the governance decision to contribute: which aspect was selected, for which FAI event, under what governance authorization, at what time. This record must exist before or concurrent with the contribution event, not retroactively.

**Artifact (b) — Contribution record in the shared substrate with full provenance.** The shared substrate carries a contribution record from the contributing Self: identifying the contributing Self, the contributed aspect, the contribution time, and the provenance carry-over depth applied. The six Paper 1 provenance fields (A1.07) are satisfied within this record at inter-Self scope.

**Artifact (c) — Contributed content organized by aspect-of-origin within the shared substrate.** The contributed aspect's content — cells, DNA-layer content, action-layer content — is organized within the shared substrate in a way that attributes it to the contributing Self's aspect. An observer can identify which contributing Self's aspect provided which content without consulting sources outside the shared substrate.

A contribution that satisfies all three artifacts is fully governed. A contribution missing any one of the three is incomplete: missing (a) leaves the contributing Self's governance loop unclosed; missing (b) leaves the shared substrate's provenance chain broken at the boundary; missing (c) leaves the shared substrate's organizational structure unable to support conflict handling and ingestion attribution.

---

## 6. Summary

D2.06 formalizes the operational structure of the contribution event that D1.06's aspect-as-exchange-unit commitment requires. Five elements compose the event: aspect selection under governance, provenance carry-over depth determination, home substrate contribution record, shared substrate contribution record, and aspect-of-origin content structure. Two contribution records are always required — neither substitutes for the other. Contributing does not transfer home authority, does not expose non-contributed aspects, and does not compel the contributing Self's home aspect to change. The anti-pattern is unrecorded contribution, which breaks the provenance chain at the inter-Self boundary and violates the shared substrate's inherited Paper 1 commitments. The operational test confirms full governance through three observable artifacts: a selection record at home, a provenance record in the shared substrate, and aspect-of-origin structure organizing the contributed content.
