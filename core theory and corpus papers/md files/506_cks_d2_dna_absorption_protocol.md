# DNA Absorption Governance Protocol

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

D2.11 is an operational decomposition of D1.18, which commits that DNA absorption from Full Aspect Integration (FAI) events operates through Paper 2's directed selection mechanism under home governance authority. D2.11 formalizes the protocol through which that absorption occurs: a five-step sequence — candidate identification, governance review, absorption decision, directed selection event, absorption record — constituting the complete governance lifecycle of each DNA absorption from an FAI event into a participating Self's home DNA. Three framing commitments govern the protocol: absorption is a genuine Paper 2 directed selection event, not a special inter-Self transfer mechanism; decline decisions are governance content equal in standing to absorption decisions; and absorption can occur after the FAI event has dissolved, using durable records retained from the event. An anti-pattern is named: automatic DNA absorption — absorbing FAI DNA content without home governance authorization and a directed selection event. The operational test asks whether, for any DNA change in a participating Self's home substrate attributed to a FAI event, an observer can locate the directed selection event record with home governance authorization, FAI-origin provenance, DNA version history entry, and decline records for non-absorbed candidates.

## 1. Derivation and scope

D1.18 commits that FAI dissolution produces a DNA evolution locus: at or after the hand-off boundary, DNA-layer content from the shared substrate — or from a durable record of the FAI event, if it has dissolved — is eligible for selective absorption into each participating Self's home DNA, with absorption operating through Paper 2's directed selection mechanism under home governance authority. D1.18 names the locus and the mechanism; it does not specify the operational protocol through which governance exercises that authority. D2.11 provides that specification.

The operational scope of this note is the governance lifecycle of a single DNA absorption decision within a single participating Self's home governance. The note covers what governance does, in what order, and what records are produced. It does not cover the configuration of which DNA-layer content from a FAI event is eligible for absorption — that is governed by the sharing-scope and hand-off configuration established before or during the FAI event. It does not cover instinct-layer content, which does not cross the inter-Self perimeter and is therefore out of scope for any absorption protocol.

The five steps that constitute the protocol are: (1) candidate identification, (2) governance review, (3) absorption decision, (4) directed selection event, (5) absorption record. Each step produces governance-traceable output. Together they constitute a complete, auditable governance transaction with a defined entry point, defined decision states, and a closed record.

## 2. The five-step protocol

**Step 1 — Candidate Identification.** At or after the FAI hand-off boundary, the receiving Self's governance identifies DNA-layer content from the shared substrate — or from the Locus 2 durable record, if the FAI event has already dissolved — that is eligible for absorption into the receiving Self's home DNA. Eligibility is governed by the sharing-scope and hand-off configuration; not all DNA-layer content contributed to the shared substrate is necessarily eligible for absorption by every participating Self. Governance determines which eligible items to present as candidates for review. The candidate identification step produces a list of items to be reviewed, which is itself a governance record.

**Step 2 — Governance Review.** Home governance reviews each candidate item. The review considers: whether the content is relevant to the receiving Self's operational context; whether it is compatible with the receiving Self's existing DNA; and whether absorbing it aligns with the receiving Self's governance intent. The review is a human governance act — it is not automated, and it cannot be delegated to a substrate process or an AI system operating outside human authority. An AI system may support the review by surfacing compatibility assessments or drafting governance analysis, but the review conclusion is a human governance judgment.

**Step 3 — Absorption Decision.** For each candidate item, governance reaches a decision: ABSORB, DECLINE, or DEFER. ABSORB authorizes the content for incorporation into home DNA through a directed selection event. DECLINE records that the content was reviewed and not selected; declined content is not discarded (see §4). DEFER records that the decision is postponed for subsequent review — the item returns to candidate status at the deferred review point. Each decision is itself a governance authorization record, regardless of outcome.

**Step 4 — Directed Selection Event.** Approved absorption is implemented as a Paper 2 directed selection event in the receiving Self's home governance. This is the core mechanical step. The directed selection event: (a) is human-authorized under home governance authority; (b) modifies the receiving Self's home DNA to incorporate the absorbed content; (c) produces a DNA version history entry in the receiving Self's lineage chain; and (d) carries provenance identifying the FAI event as the source of the absorbed content and identifying the contributing Self's aspect from which the content originated. The directed selection event is an instance of the Paper 2 B1.14 governance requirement for DNA changes — the same event type that governs all DNA evolution within a Self's home substrate. The FAI origin of the content is recorded in provenance; it does not alter the event's governance requirements or the authority architecture under which the event operates.

**Step 5 — Absorption Record.** The completed absorption is recorded as home governance content: what content was absorbed; from which FAI event and which contributing Self's aspect it originated; at what time; under what directed selection authorization. This record enables traceability of inter-Self DNA learning within the receiving Self's governance history. An observer examining the receiving Self's governance record can follow the chain from the current DNA state backward to the FAI event that supplied the absorbed content, and forward from the FAI event to the directed selection event that effected the absorption.

## 3. Genuine directed selection: why the framing matters

The most important framing commitment for D2.11 is that DNA absorption from FAI is not a special inter-Self transfer mechanism. It is Paper 2's standard directed selection event operating on FAI-origin content as the improvement source.

This framing matters because it determines what governance requirements apply. If DNA absorption were treated as a distinct mechanism — an "inter-Self DNA transfer" with its own governance framework — the requirements might be lighter, or different in kind, from those that apply to ordinary directed selection. The CKS architecture makes no such accommodation. The source of the content being absorbed (another Self's contribution to a shared substrate) does not relax or alter the governance requirements that apply to a DNA change in the receiving Self's home substrate. The same human authorization, the same DNA version history entry, the same provenance attribution, the same directed selection event type — these apply whether the content being incorporated was developed internally within the receiving Self's own governance or arrived through a FAI event.

This commitment also determines what records must exist. The directed selection event record for a DNA absorption must be findable in the receiving Self's home governance history. An implementation that absorbs DNA content from FAI without producing a directed selection event record violates Paper 2 B1.14, regardless of whether the content originated inside or outside the receiving Self. The boundary-crossing character of the content's origin is a fact about provenance, not a license for reduced governance.

The practical implication is that the five-step protocol is not a new compliance framework layered on top of existing governance. Steps 1–3 are preparation for Step 4. Step 4 is Paper 2 directed selection. Step 5 is the record that makes Step 4 traceable to its FAI source. The protocol formalizes the preparation and record steps that the FAI context requires; the core governance event is the standard mechanism Paper 2 establishes.

## 4. Decline records as governance content

DNA content that governance declines to absorb is not discarded. Two preservation properties hold.

First, the declined content itself remains accessible. If the FAI event's Locus 2 durable record is retained under the governing persistence policy, the content persists there. If the durable record is not retained, the content is still accessible via the contributing Self's governance records through provenance references established at the time of the FAI event. Governance can retrieve and review declined content at any later time, including to reconsider a DEFER decision.

Second, and more important, the decline decision is itself governance content. Recording that a candidate item was reviewed and declined creates a governance-quality improvement loop. Over time, a receiving Self's governance can examine its own decline record and ask: What was offered from FAI events? What was accepted, and what was declined? Are there patterns in what was declined — content types consistently out of scope, compatibility issues that recur, misalignments with governance intent that could be resolved through other DNA changes? These questions are only answerable if decline decisions are recorded with the same fidelity as absorption decisions.

This symmetry — absorption and decline as equal-standing governance records — is the architectural commitment D2.11 formalizes. Governance that accepts FAI content without recording declines has an incomplete governance history. Governance that records only absorptions knows what entered the DNA but cannot audit what was considered and rejected. The complete governance record covers both, enabling review of the absorption protocol itself as a governance practice.

The DEFER path carries the same record requirement: a deferred decision is a governance record, not a silence. Governance can defer; it cannot ignore.

## 5. Post-dissolution absorption

The directed selection event for DNA absorption can occur after the FAI event has dissolved. This follows from the Locus 2 persistence mechanism: if the FAI event's durable record is retained, the DNA-layer content from the shared substrate persists in that record and remains available for absorption by participating Selves after dissolution. Absorption is not time-bounded to the FAI event's active phase.

The practical implications are significant. A participating Self's governance may not have the bandwidth to conduct the full five-step absorption protocol while the FAI event is active. The event may dissolve before all candidate content has been reviewed. Post-dissolution absorption allows governance to complete the absorption protocol on its own schedule, using the durable record as the source of candidate content.

Post-dissolution absorption uses the same five-step protocol as absorption during active operation. The directed selection event is identical in form: it is human-authorized, it produces a DNA version history entry, and it carries provenance identifying the FAI event as the source. The timing of the absorption relative to the event's active phase does not alter the governance requirements or the record requirements.

The provenance record produced in Step 5 must accurately reflect the timing: that the absorption occurred after the event dissolved, and that the content was retrieved from the durable record. This is standard provenance practice — the record reflects what actually occurred.

When the Locus 2 durable record is not retained under the governing persistence policy, post-dissolution absorption is still possible if the contributing Self's governance records are accessible via provenance references. The mechanism is provenance-traceable retrieval rather than direct durable-record access, but the five-step protocol applies identically. The contributing Self's governance retains its own record of what it contributed to the FAI event, and this record provides the content source for the absorption.

## 6. Anti-pattern: automatic DNA absorption

The anti-pattern for D2.11 is automatic DNA absorption: absorbing DNA-layer content from a FAI event into a participating Self's home DNA without home governance authorization and a directed selection event.

Automatic DNA absorption can take several forms. A system may be configured so that DNA-layer content from the shared substrate is automatically incorporated into participating Selves' home DNA at dissolution — without a governance review step and without a directed selection event being logged. A system may treat FAI-origin DNA content as pre-approved and bypass the candidate identification and governance review steps on the assumption that content from a trusted inter-Self source requires no further review. A system may record the absorption as an infrastructure operation rather than as a governance event, producing no DNA version history entry and no governance authorization record.

Each of these forms violates Paper 2 B1.14's governance requirements for DNA changes at home scope. The violation is not diminished by the fact that the content originated from a trusted source. The receiving Self's home governance has not approved the change; no directed selection event record exists; the DNA version history entry is absent; and declined candidates have no record. The receiving Self's governance history is incomplete, and the link between the current DNA state and the FAI event that produced the absorbed content is unauditable.

The anti-pattern also undermines the governance-quality improvement loop described in §4. Without decline records, governance cannot review what was offered and what was accepted. Without the full five-step protocol, the absorption is invisible to the governance record — it appears as a DNA change with no traceable authorization.

Automatic DNA absorption may appear efficient. The five-step protocol imposes review costs that automatic absorption avoids. The architectural position is that those costs are the cost of governed DNA evolution, and that the alternative — ungoverned DNA change through a trusted inter-Self channel — is a governance violation regardless of how trusted the channel is.

## 7. Operational test

For a DNA change in a participating Self's home substrate attributed to a FAI event, the following must all be findable in the receiving Self's governance records:

1. A directed selection event record, produced under home governance authority, authorizing the specific DNA change and identifying the FAI event as the source of the absorbed content.
2. A DNA version history entry in the receiving Self's lineage chain corresponding to the directed selection event.
3. FAI-origin provenance: the provenance carried by the directed selection event record identifies the FAI event, the contributing Self's aspect, and — if post-dissolution — the durable record or provenance-traceable access path from which the content was retrieved.
4. Decline records for non-absorbed candidates: for each eligible DNA-layer content item reviewed and not absorbed in the same absorption governance session, a governance record documenting the DECLINE or DEFER decision.

A system in which (1) or (2) cannot be found has not implemented the directed selection mechanism required by Paper 2 B1.14. A system in which (3) cannot be found has absorbed DNA content without auditable FAI-origin provenance. A system in which (4) cannot be found has an incomplete absorption governance record, even if the absorptions themselves are correctly authorized.

A partial pass — absorptions correctly authorized but declines unrecorded — satisfies the individual directed selection requirement but violates the governance completeness requirement D2.11 formalizes. All four criteria must pass for the protocol to be considered correctly instantiated.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *DNA Absorption Governance Protocol.* May 15, 2026. ORCID: 0009-0004-8065-3235.
