# AP-4: Automatic DNA Absorption

**Series D — Phase D3 Anti-Pattern Formalization, Note #584**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

AP-4, Automatic DNA Absorption, is the first formalized anti-pattern in Category 3 (Evolution Feed Failures) of the Phase D3 series. The anti-pattern arises when FAI-origin DNA-layer content from another Self's contributed aspects enters a participating Self's home DNA without a directed selection governance event and without explicit home governance authorization. The violation is not about what was absorbed — even DNA content that home governance would have willingly approved is implicated when it enters through automatic absorption. The violation is that the directed selection process was bypassed. Paper 2's directed selection governance commitment (B1.14) requires that all DNA changes proceed through a governed event with human authorization; Paper 3's Claim 4 DNA evolution locus requires that this requirement hold at inter-Self scope. Automatic absorption violates both. The consequences include substrate version corruption, path retraceability failure, and — most distinctively — the permanent foreclosure of decline decisions: content that home governance would have rejected enters anyway, silently shaping what the Self is. Remediation proceeds through Paper 1 Claim 3's override right, which enables home governance to remove automatically absorbed content through a governed removal event and restore governance sovereignty over its own substrate.

---

## 1. Anti-Pattern Name and Category

**AP-4: Automatic DNA Absorption**
**Category 3 — Evolution Feed Failures** (opening anti-pattern of the category)

Category 3 formalizes failure modes at the evolution feed boundary — the boundary at which FAI dissolution hands off content to each participating Self's home evolution mechanisms. Paper 3's Claim 4 commits to a four-locus evolution-feed mechanism that routes FAI-derived content through each Self's existing Paper 2 evolution machinery under home governance authority. Evolution feed failures are anti-patterns in which that routing occurs without the governance authority the architecture requires. AP-4 is the first and most direct: DNA-layer content takes the shortest unauthorized path, entering home DNA without ever encountering a governance decision.

---

## 2. Description

When a Full Aspect Integration (FAI) event dissolves, the shared substrate releases content back to each participating Self's home perimeter. Paper 3's Claim 4 is precise about what happens next: content reaches each Self's home evolution mechanisms through the existing per-mechanism governance shapes that Paper 2 establishes. For DNA-layer content, that governance shape is directed selection — the process by which home governance identifies candidate content, reviews it, makes an explicit absorption decision, and authorizes a directed selection event that records the decision and its authorization chain. The absorption is governed. The decision is explicit. The record exists.

Automatic DNA absorption is what happens when this governance shape is absent. FAI-origin DNA-layer content from another Self's contributed aspects enters the participating Self's home DNA without a directed selection event being generated and without home governance having authorized the absorption. The mechanism of automatic absorption takes two forms: the FAI infrastructure itself may perform the absorption without routing through a governance decision, or the governance process may treat participation in an FAI event as implicit authorization for whatever DNA content emerges at dissolution, making the absorption automatic in practice even when governance nominally exists.

The critical framing is that the violation is process-level, not content-level. The anti-pattern does not depend on whether the absorbed DNA content is harmful, neutral, or genuinely beneficial to the home Self. DNA content that home governance would have reviewed, approved, and absorbed through directed selection is equally implicated when it enters without that process. The governance commitment is to the directed selection event — to the existence of a human-authorized governance decision in the record — not to a particular outcome. An architecture that allows automatic absorption on the grounds that the content is "obviously good" has abandoned the commitment. What governance decides and how governance decides are both load-bearing; removing the how invalidates the commitment regardless of the what.

---

## 3. Detection Criteria

Three detection signals identify automatic DNA absorption in a deployed system.

The first signal is provenance without authorization record. DNA content found in a participating Self's home substrate that traces through provenance to another Self's FAI contribution — establishing that the content entered via an FAI pathway — but that lacks a corresponding directed selection event record in the home governance history is automatically absorbed content. The provenance chain and the governance chain must both exist and must link to the same absorption event. Content with provenance but no authorization record has been absorbed without governance.

The second signal is version history coincidence without selection record. When the home substrate's DNA version history shows changes that coincide with FAI event dissolution — when version timestamps or event markers place DNA changes at or immediately after the dissolution boundary — and when no directed selection records exist for those changes, the coincidence establishes that dissolution triggered absorption and that absorption happened without a governed selection event. The timing signal alone is sufficient to flag for governance audit; the absence of selection records confirms the anti-pattern.

The third signal is the attribution gap. When DNA changes at dissolution time are attributed to the FAI event in operational records but carry no corresponding governance authorization record for the absorption decision itself, the attribution is to an infrastructure action rather than a governance action. Infrastructure-attributed DNA changes are the signature of automatic absorption: the system did something that governance should have done.

---

## 4. Governance Commitment Violated

Automatic DNA absorption violates three governance commitments with one primary, one secondary, and one tertiary violation.

**Primary violation: Paper 2 directed selection governance (B1.14).** Paper 2's directed selection governance commitment establishes that all DNA changes require a directed selection event with human governance authorization. This is the intra-Self rule: no cell or aspect DNA changes except through a governed directed selection event. Automatic absorption violates this requirement at its foundation. It does not merely skip a step in the directed selection process; it eliminates the process entirely. DNA enters home substrate without any of the governance machinery that directed selection requires — no candidate identification by governance, no review, no explicit decision, no authorization record.

**Secondary violation: Paper 1 Claim 3 (human-governed authority).** Paper 1's human-governed commitment establishes that humans retain the right to inspect, modify, and override any substrate content and any orchestration rule at any time. DNA changes to the home substrate are substrate content changes, and substrate content changes require governance authorization. Automatic absorption bypasses that authorization, producing substrate content whose existence was not authorized by home governance. A substrate that contains content entered without governance authorization is not fully human-governed — a portion of its content exists outside the governance approval chain.

**Tertiary violation: Paper 3 Claim 4 (four-locus evolution feed — DNA evolution locus).** Paper 3's Claim 4 specifies that the DNA evolution locus of the four-locus feed mechanism operates through directed selection, using the existing per-mechanism governance shapes that Paper 2 §8 establishes. The DNA evolution locus is not an open channel through which FAI content flows freely; it is a governed pathway requiring directed selection. Automatic absorption bypasses the DNA evolution locus's governance shape entirely, routing DNA content directly into home substrate without touching the locus machinery.

**Operational reference: D2.11 (five-step DNA absorption protocol).** D2.11 establishes the complete operational protocol for governed DNA absorption following FAI dissolution: (1) candidate identification by home governance, (2) governance review of candidates, (3) explicit absorption decision — absorb, decline, or defer — (4) directed selection event with authorization, (5) absorption record with FAI-origin provenance. Automatic absorption violates all five steps simultaneously. No candidate is identified by governance. No review occurs. No decision is made. No directed selection event is generated. No absorption record with authorization exists.

---

## 5. Consequences

Five consequences follow from automatic DNA absorption.

**Substrate authorization chain corruption.** DNA changes enter the home substrate without governance authorization, bypassing the approval chain that directed selection requires. The home substrate thereafter contains content whose presence was not authorized. Every subsequent governance decision that operates on the assumption that home substrate DNA reflects governed choices is potentially operating on corrupted assumptions. The corruption is architectural: it cannot be corrected merely by reviewing the content; the authorization chain itself is broken and must be reconstructed or the content removed.

**Version history integrity failure.** The home substrate's DNA version history is a governance record — each version should correspond to a governed change event. Automatic absorption produces DNA versions without corresponding governance records. The version history becomes internally inconsistent: versions exist, but the governance events that should have generated them do not. This is not a documentation failure; it is a governance record integrity failure that undermines the reliability of the entire version history for audit and accountability purposes.

**Path retraceability failure at Link 4.** D2.67's path retraceability requirement establishes that the full authorization chain for any substrate content change must be reconstructible. For FAI-origin DNA content, the chain runs through four links: the FAI event generating the content, the dissolution hand-off, the home governance absorption review, and the home governance absorption authorization. Automatic absorption eliminates Link 4 — the home governance absorption authorization link is absent. The authorization chain cannot be retraced past dissolution. Content that cannot be retraced to a home governance authorization is unaccountable content in the substrate.

**Governance operating on incorrect assumptions.** Home governance may be entirely unaware of what DNA content has entered its substrate through automatic absorption. Governance decisions that proceed on the assumption that home DNA reflects only content that governance has reviewed and authorized are based on incorrect assumptions when automatic absorption has occurred. Governance architecture built on unknown foundations can produce systematically incorrect decisions — decisions that would have been made differently had governance known the full content of its own substrate.

**Decline decisions permanently foreclosed.** This is the most architecturally significant consequence of automatic DNA absorption, and it is irreversible once absorption occurs. Directed selection governance does not only authorize absorptions — it enables declines. Home governance may review FAI-origin DNA candidates and decide that specific content conflicts with home governance philosophy, that it duplicates existing architecture in ways that create inconsistency, or that it represents a direction the home governance has specifically chosen not to pursue. These are legitimate governance decisions, and directed selection is the architectural mechanism through which they are made.

Automatic absorption eliminates the possibility of these decisions. Content that home governance would have declined enters the home substrate. The Self becomes shaped by another Self's FAI contribution in ways that home governance explicitly would have rejected. This is a governance sovereignty violation: the home Self's identity and behavioral architecture are partially determined by content from another Self's governance context, without the home Self's governance ever having the opportunity to say no. The damage is not merely procedural — it is to the home Self's architectural integrity as a governed entity.

---

## 6. Intra-Self Analog

The intra-Self analog of automatic DNA absorption is any mechanism that modifies cell or aspect DNA within a Self without a governed directed selection event. Paper 2's directed selection governance requirement (B1.14) applies at intra-Self scope: DNA evolution within a Self proceeds through directed selection, not through automatic or infrastructure-driven modification. A cell whose DNA is modified by an automated process without a human-authorized directed selection event is experiencing the intra-Self version of this anti-pattern — substrate content is changing outside the governance architecture that the commitment requires.

The relationship between the intra-Self analog and AP-4 is one of scope extension rather than analogy by accident. Paper 3's Claim 4 explicitly extends Paper 2's directed selection governance requirement to the inter-Self scope: the DNA evolution locus of the four-locus feed mechanism operates through directed selection at the home perimeter, using Paper 2's existing governance shapes. The intra-Self rule and the inter-Self rule are the same commitment applied at two different scopes. Automatic DNA absorption is the inter-Self scope version of ungoverned DNA modification — the same failure mode, the same bypassed governance shape, the same corrupted version history, expressed at the boundary where FAI content meets home substrate rather than at the boundary where cell content meets aspect DNA.

---

## 7. Resolution

**Prevention: D2.11's five-step absorption protocol.** The complete prevention of automatic DNA absorption is the five-step protocol established in D2.11: (1) candidate identification by home governance — governance actively identifies which FAI-origin DNA content is available for potential absorption; (2) governance review of candidates — each candidate is reviewed against home governance philosophy, existing architecture, and strategic direction; (3) explicit absorption decision — governance makes an explicit absorb, decline, or defer decision for each candidate; (4) directed selection event with authorization — the absorption decision is executed through a directed selection event that generates a governance authorization record; (5) absorption record with FAI-origin provenance — the record captures both that the content was absorbed and that its origin traces to a specific FAI event and contributing Self. All five steps are required; the absence of any single step is the anti-pattern.

The protocol makes the governance sovereignty commitment concrete. Step 3 is where decline decisions are made. When governance reviews a candidate and finds that it conflicts with home architecture, home philosophy, or home strategic direction, step 3 is where that finding becomes a governance record: the content was reviewed, it was declined, and home substrate DNA reflects that decision. The five-step protocol is not bureaucratic overhead; it is the mechanism through which governance sovereignty is exercised as a positive architectural property of the system.

**Remediation: override right under Paper 1 Claim 3.** When automatic absorption is discovered after the fact — when audit reveals that DNA content entered home substrate without a directed selection event — the remediation path runs through Paper 1 Claim 3's override right. Paper 1 establishes that home governance retains the right to inspect, modify, and override any substrate content at any time. This right is precisely what enables retroactive remediation of automatic absorption.

The remediation procedure is:

First, identify all DNA content that entered the home substrate through ungoverned FAI absorption. Provenance tracing against governance history records produces the complete set of implicated content — content with FAI-origin provenance and no corresponding directed selection authorization.

Second, conduct retroactive governance review of that content. Governance reviews each piece of automatically absorbed content as it would have reviewed it had the five-step protocol been followed at dissolution time. The review produces an explicit decision for each candidate: absorb, decline, or defer for further review.

Third, for content that governance would have declined — content that conflicts with home governance philosophy, creates architectural inconsistency, or represents a direction governance has chosen not to pursue — exercise the override right. Paper 1 Claim 3 authorizes home governance to remove that content from the home substrate through a governed removal event. The removal event generates a governance record: the content was automatically absorbed, it was identified through audit, governance reviewed it retroactively, governance decided it should not have been absorbed, and governance exercised its override right to remove it. The removal event is itself a directed selection event — a governance decision recorded with authorization — and it restores the integrity of the home substrate's DNA version history and authorization chain.

The override right does not undo the past. The automatic absorption happened, and the governance record will reflect that it happened. What the override right restores is governance sovereignty going forward: after the governed removal event, the home substrate's DNA reflects only content that home governance has authorized, and the authorization chain is intact from the remediation point forward. Governance sovereignty is restored not by pretending the violation did not occur but by exercising the architectural authority that always existed and that the anti-pattern temporarily circumvented.

---

## References

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

---

## How to cite this note

Li, W. (2026). *AP-4: Automatic DNA Absorption. CKS Derivation Note Series D, Phase D3, Note #584.* May 15, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
