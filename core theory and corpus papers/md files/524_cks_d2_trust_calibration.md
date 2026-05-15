# Inter-Self Governance Trust Calibration

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** CKS Derivation Notes — Phase D2, Note D2.29 (Note #524)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

In the CKS inter-Self coordination architecture, governance trust between participating Selves is not a declaration, an organizational relationship, or an expression of intent — it is a calibration based on governance compliance evidence accumulated across prior FAI events. This note formalizes governance trust as an evidence-based concept, distinguishes it from its nearest misreadings, articulates what high and low trust each enable operationally, enumerates four calibration mechanisms through which trust evidence is accumulated (prior FAI event records, contribution record verification, conflict handling quality, and standing configuration evolution), and establishes that trust calibration is operationally expressed through FAI configuration choices rather than through a separate declaration process. The note closes by connecting trust accumulation to Claim 6's population-scale collective evolution mechanism and naming trust inflation — configuring deeper sharing scope than governance evidence warrants — as the primary anti-pattern.

---

## 1. Position: D2.29 as operational decomposition of D1.25 and D1.27

D2.29 derives from two Phase D1 sub-commitments.

D1.25 formalizes joint authority over FAI configuration as a sub-commitment of Paper 3 Claim 5 (configuration as substrate content). FAI event configuration — sharing scope, merge pattern, provenance carry-over depth, escalation routing — is substrate content authored under joint authority across participating Selves' governance. No participating Self configures the event unilaterally; configuration choices are themselves part of the governed substrate record. D1.25 establishes the authority structure within which configuration decisions are made and recorded.

D1.27 formalizes accumulated FAI events as the mechanism of collective evolution, a sub-commitment of Paper 3 Claim 6 (population-scale collective evolution). Each FAI event leaves a governance record — contribution records, conflict registry entries, orchestration rules, evolution feed outcomes — and the accumulation of these records across many events and many participating Selves is what drives the population-scale integration that Claim 6 articulates. D1.27 establishes the role of event history in the architecture's evolution dynamic.

D2.29 asks: how does a participating Self use the governance records from D1.27 to inform the configuration choices it makes under D1.25? The answer is inter-Self governance trust calibration. Trust calibration is the operational link between the record produced by past events and the configuration proposed for future events.

---

## 2. Governance trust defined: compliance evidence, not intent

In the CKS context, "trust" between participating Selves names something specific and narrow. It does not name organizational relationship — two Selves may be operated by the same organization, operate under a shared commercial arrangement, or share personnel, and still have limited governance trust in the CKS sense. It does not name intent — a contributing Self's stated commitment to governed exchange is not governance trust. It does not name reputation in a general sense.

CKS governance trust names the evidence that a contributing Self applies the Paper 3 architectural commitments to its contributions. A participating Self trusts another Self's contributions to the extent that it has governance compliance evidence: records showing that the contributing Self maintained proper contribution provenance, that its conflict registry entries preserved both sides of conflicts, that its orchestration rules were coherent and human-authored, and that its evolution feed requests carried proper home governance authorization. Trust is earned through the governance record, not asserted through the governance relationship.

This definition has a sharp implication that is easy to miss. Two Selves operated by organizations with no formal relationship may carry strong mutual governance trust if they have conducted prior governed FAI events with clean compliance records. Two Selves operated by the same organization may carry limited governance trust if they have not yet conducted governed FAI events and therefore have no compliance record to review. Organizational proximity and governance compliance evidence are orthogonal. The CKS architecture does not prohibit close organizational partners from having high governance trust; it requires that such trust be earned through the compliance record rather than inherited from the organizational relationship.

The same definition applies in reverse. A Self should not accept another Self's claimed governance compliance as evidence. The record — the actual configuration substrate from prior events, the actual contribution records, the actual conflict registry entries — is the evidence. Claims about governance practices that are not reflected in a reviewable substrate record do not constitute governance compliance evidence.

---

## 3. What high and low trust enable operationally

Governance trust calibration is consequential because it determines the configuration choices a Self makes when entering a FAI event with another Self.

**High governance trust.** A Self with strong compliance evidence about another Self's governance practices may configure a FAI event with deeper sharing scope — more aspects contributed to the shared substrate — with less restrictive selective merge — more contributed content included in the home substrate following the event — and with deeper provenance carry-over — more of the contributing Self's provenance chain accepted into home records. High trust lowers governance overhead because the compliance evidence substitutes for per-event manual review of contributed content. A Self with ten prior FAI events showing clean contribution records, intact conflict preservation, and coherent orchestration rules has earned the configuration flexibility that deeper sharing scope represents.

**Low governance trust.** A Self with limited compliance evidence about another Self's governance practices should configure a FAI event with narrower sharing scope, more restrictive selective merge — manually reviewing more contributed content before including it in the home substrate — and shallower provenance carry-over. Low trust increases governance overhead per event but reduces governance risk: the participating Self is not incorporating content whose governance lineage it cannot verify. This is the conservative starting position for any new participating Self relationship and for any relationship where prior event records show governance compliance gaps.

The important observation is that both configurations — high trust and low trust — are fully governed. Low trust does not mean ungoverned exchange; it means more conservative configuration within the governed architecture. The governance framework operates identically at both trust levels; what varies is how much of that framework the participating Self delegates to the contributing Self's prior compliance record versus how much it applies directly through manual review.

---

## 4. Four trust calibration mechanisms

Governance trust does not arrive at the start of a relationship and does not update arbitrarily. It accumulates through four mechanisms.

**Mechanism 1 — Prior FAI event records.** The primary trust calibration mechanism is review of the governance records from prior FAI events with the same participating Self. Governance asks: did their contributions arrive with proper provenance chains? Did their conflict registry entries show both sides preserved, rather than one-sided resolution? Were their orchestration rule contributions coherent and internally consistent? Did their evolution feed requests carry home governance authorization, or did content appear in the shared substrate without traceable authorization? Each prior event provides governance compliance evidence. A Self with ten prior events showing strong compliance across all these dimensions carries substantially more governance trust than a Self entering its first FAI event.

**Mechanism 2 — Contribution record verification.** During an active FAI event, governance verifies that the contributing Self's contribution records match what is actually present in the shared substrate. Contribution records — the formal registry of what a Self contributed, when, and under what authorization — are themselves substrate content under joint authority. A contributing Self whose contribution records consistently and accurately reflect their actual contributions builds trust evidence through this mechanism. Discrepancies between records and actual substrate content are governance compliance failures that reduce trust calibration.

**Mechanism 3 — Conflict handling quality.** How a contributing Self handles conflicts arising from its contributions is a direct signal of governance quality. A Self that responds promptly to conflict escalations, authors new orchestration rules to address recurring conflict classes rather than relying on ad hoc resolution, maintains conflict registry integrity across events, and does not attempt to resolve conflicts by simply overwriting contributed content — all of these behaviors constitute governance compliance evidence at the conflict handling level. Poor conflict handling quality is one of the most informative trust calibration signals because it tests governance behavior under conditions of genuine disagreement rather than under normal operation.

**Mechanism 4 — Standing configuration evolution.** Standing configurations — the pre-negotiated configuration baselines that participating Selves use across a series of events — encode accumulated governance trust as substrate content. As trust increases through the first three mechanisms, governance may update the standing configuration to allow deeper sharing scope, richer provenance carry-over, or less restrictive merge patterns. Standing configuration amendments record the governance reasoning for trust changes — why the configuration was updated, what compliance evidence supported the update. These records make trust calibration history inspectable: an observer reviewing the standing configuration amendment history can reconstruct how governance trust between two Selves developed over time.

---

## 5. Trust calibration as governance-configurable

A participating Self does not declare its governance trust level in a separate process. Trust calibration is expressed entirely through FAI configuration choices — the sharing scope proposed for the event, the selective merge pattern selected, the provenance carry-over depth negotiated. These configuration choices, made and recorded under the joint authority structure of D1.25, are the operational form of trust calibration.

This makes trust calibration visible and auditable in a way that a separate declaration process would not. Two Selves' mutual trust calibration is readable in their configuration history: deeper sharing scope and richer provenance carry-over reflect higher trust; narrower scope and shallower provenance reflect lower trust or a new relationship without compliance history. An observer with access to the configuration substrate for a series of events between two Selves can reconstruct both the current trust calibration and the trajectory by which it was reached.

The implication is that trust calibration is not a pre-event administrative step. It is woven into the event configuration process. When governance for Self A proposes a FAI event configuration with Self B, the configuration itself encodes governance's current assessment of Self B's compliance evidence. When Self B accepts, modifies, or rejects the proposed configuration, it reflects its own assessment. The negotiation over configuration terms is the trust calibration process, made visible in substrate-content form.

---

## 6. Trust accumulation as population-scale integration driver

The connection to Paper 3 Claim 6 and its D1.27 derivation runs through the accumulation dynamic.

Claim 6 articulates population-scale collective evolution as what the preceding five claims compose to when accumulated FAI events across many participating CKS-governed Selves operate under joint authority across population-level governance perimeters. The evolution dynamic is not merely that FAI events occur, but that they accumulate governance records and that those records inform subsequent events. Trust calibration is one of the primary mechanisms through which accumulated records shape subsequent events.

As governance trust between a pair of Selves accumulates through evidence across FAI events, deeper sharing and richer exchange become governance-appropriate. What begins as a narrow, manually reviewed exchange — appropriate for two Selves without a prior compliance history — may, through a series of events with clean compliance records, evolve toward a standing configuration that permits substantially deeper integration. Across the population of Selves, this dynamic means the network becomes more deeply integrated where governance evidence supports integration. Integration depth is governed by compliance history rather than by capability availability or commercial interest.

This is the mechanism connecting D2.29 to D1.27's accumulated FAI events as collective evolution. The population-scale integration that Claim 6 articulates is not a uniform increase in integration across all participating Selves. It is a differentiated integration, deeper where governance trust has been earned through compliance evidence and shallower where it has not. Trust calibration is the mechanism that enforces this differentiation.

---

## 7. Anti-pattern: trust inflation

The named anti-pattern for D2.29 is trust inflation: configuring a FAI event with deeper sharing scope, richer provenance carry-over, or less restrictive selective merge than governance compliance evidence warrants.

Trust inflation is a governance failure that is easy to miss because it does not produce an obvious immediate breakdown. The event may proceed without incident. The shared substrate may contain no conflicts that escalate. The home substrates may absorb the contributed content without visible disruption. The governance records produced — contribution records, conflict registry entries, standing configuration terms — may all appear well-formed. But the governance records reflect a configuration that was not calibrated to compliance evidence. The provenance chains carried over may not have been earned through verified compliance. The merge decisions made without manual review may have incorporated content whose governance lineage was not actually verified.

The risk of trust inflation is that it produces exchanges that are nominally governed — the records exist, the substrate content has the right form — but effectively ungoverned: the depth of exchange authorized by the configuration exceeds the depth of compliance verification that justifies it. Over time, as this miscalibrated trust compounds through the standing configuration evolution mechanism, the governance record becomes a progressively less accurate representation of actual compliance history.

Trust inflation is most likely to occur when trust is calibrated to organizational relationship or commercial interest rather than to compliance evidence — when two Selves configure a FAI event with deep sharing scope because their operators are close partners, without examining whether prior governed FAI events have produced the compliance record that deep sharing scope requires. The CKS governance trust definition — evidence, not relationship — is the direct preventive. Governance that asks "what does the compliance record support?" rather than "how much do we trust our partners?" is governance that holds against trust inflation.

---

## 8. Operational test

For a FAI event between two Selves with a prior event history, an observer can assess governance trust calibration by reviewing the configuration record in relation to the prior compliance record. The assessment has three dimensions.

First, sharing scope: does the sharing scope configured for the current event reflect the depth of compliance evidence available from prior events? A first event between two Selves with no prior compliance history should show conservative sharing scope. A tenth event between two Selves with nine prior events showing clean contribution records, intact conflict preservation, and coherent orchestration rules may appropriately show broader sharing scope. The configuration trajectory across events should track the compliance record.

Second, selective merge pattern: does the degree of manual review required before content is incorporated into the home substrate reflect the current trust calibration? Higher governance trust should correspond to less restrictive merge — more content passing through without per-element manual review — justified by the compliance evidence that substitutes for that review. Lower governance trust should correspond to more restrictive merge, with the manual review requirement reflecting the absence of compliance evidence.

Third, provenance carry-over depth: does the depth of provenance chain accepted from the contributing Self reflect the governance record that chain is built on? Deeper provenance carry-over is governance-appropriate when prior events have verified that the contributing Self's provenance chains are accurate. Shallower provenance carry-over is appropriate when the contributing Self's provenance practices have not been verified through prior events or have shown inconsistencies.

A configuration that shows deep sharing scope, less restrictive merge, and rich provenance carry-over for a Self with limited prior compliance history fails the trust calibration test. A configuration that shows conservative sharing scope for a Self with an extensive and clean compliance history is either under-calibrated — governance has not updated its configuration to reflect the accumulated evidence — or reflects a specific governance concern that the record should document. Both mismatches are observable in the configuration substrate, which is the architecture's mechanism for making trust calibration reviewable.

---

## 9. Summary

CKS governance trust between participating Selves is governance compliance evidence, accumulated through prior FAI event records, contribution record verification, conflict handling quality, and standing configuration evolution. It is not organizational relationship, commercial interest, or stated intent. Trust calibration is expressed operationally through FAI configuration choices — sharing scope, merge pattern, provenance carry-over depth — rather than through a separate declaration process. This makes trust calibration visible and auditable through the configuration substrate. As trust accumulates across the population of participating Selves, deeper integration becomes governance-appropriate in more relationships, driving the differentiated population-scale collective evolution that Claim 6 articulates. Trust inflation — configuring deeper exchange than compliance evidence warrants — is the primary anti-pattern, producing nominally governed but effectively under-verified exchange and degrading the governance record over time.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Inter-Self Governance Trust Calibration.* CKS Derivation Notes, Phase D2, Note D2.29 (#524). May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
