# AP-23: Authorization Chain Gap

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When two or more governance-distinct organizations coordinate through a shared substrate using Full Aspect Integration (FAI), every governance outcome that flows from that coordination must be traceable back, link by link, to a complete chain of human governance authorizations. Paper 3 formalizes this chain as four ordered links spanning the contributing Self's home authorization, the joint FAI event authorization, the shared-substrate governance of content use, and the absorbing Self's home absorption authorization. AP-23, Authorization Chain Gap, is the anti-pattern in which one or more of these four links is absent or broken, making it impossible to prove that the affected governance outcome rests on complete human governance authorization. The anti-pattern has four break types corresponding to the four links, but all four are manifestations of the same underlying failure: a gap in the cross-organizational accountability chain that violates the path retraceability commitment of Paper 1 A1.07 at inter-Self scope. This note names the anti-pattern, describes its four break types, provides detection criteria, identifies the governance commitment violated and the consequences of the violation, draws the intra-Self analog, and specifies both preventive and remedial resolution approaches.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-23 — Authorization Chain Gap

**Category:** Taxonomy Category 6 — Governance Quality Failures

**Position in series:** D3.24 (the twenty-fourth Phase D3 anti-pattern note; note #599 in the derivation series)

**One-sentence statement:** A break at any of the four links in the cross-organizational authorization chain makes it impossible to trace a FAI governance outcome back to the complete chain of human governance authorizations that legitimized it.

---

## 2. Description

Paper 3 establishes that every governance outcome flowing from a FAI event must be traceable through an ordered four-link authorization chain (D2.67). The four links are:

**Link 1 — Home authorization for contribution.** The contributing Self's home governance authorized the contribution of aspects to the shared substrate (D2.06). This link records that the decision to participate was itself a governed decision, made by the contributing organization's human governance.

**Link 2 — Joint authorization for the FAI event.** The governance outcome in the shared substrate traces to a jointly authorized configuration or orchestration rule that governed the FAI event (D2.12). This link records that the governance basis for the shared substrate operation was established by joint human governance of the participating Selves, not by an autonomous system decision.

**Link 3 — Shared-substrate governance of content use.** The use of FAI-origin content within the shared substrate traces to the governing configuration at the time of use (D2.15 / D2.14). This link records that the content operated under governed conditions throughout its presence in the shared substrate.

**Link 4 — Home authorization for absorption.** FAI-origin content that was absorbed into a home substrate traces to the absorbing Self's home governance authorization of that absorption (D2.11). This link records that the decision to bring cross-organizational content into the home substrate was itself a governed decision by the absorbing organization's human governance.

**AP-23 occurs when any one of these four links is absent or broken.** A gap at any link means the accountability trail from the governance outcome back to the complete chain of human governance authorizations is broken at that point. Governance decisions occurred. Records may exist at other links. But the chain is not whole, and therefore governance sovereignty cannot be proven for the affected outcome.

The four break types are named as variants of a single anti-pattern rather than as four separate anti-patterns because they are all instances of the same commitment violation — a breach of path retraceability at inter-Self scope (A1.07). The specific link at which the gap occurs determines where remediation must be directed, but the accountability failure is the same in structure regardless of which link fails.

**Break Type 1 — Missing Home Authorization.** Substrate content exists that cannot be traced to the contributing Self's home governance authorization decision. The contribution record (D2.06) is absent. The contribution happened, but no record establishes that home governance decided to authorize it.

**Break Type 2 — Missing Joint Authorization.** A governance outcome in the shared substrate cannot be traced to a jointly authorized configuration or orchestration rule. The configuration record (D2.12) is absent. The FAI event produced a governance outcome, but no record establishes the joint governance basis under which it operated.

**Break Type 3 — Missing Absorption Authorization.** FAI-origin content is present in a home substrate, but no absorption authorization record exists (D2.11). The directed selection record is absent. Content crossed the perimeter into the home substrate without a record that home governance decided to authorize that crossing.

**Break Type 4 — Missing Cross-Organizational Provenance.** FAI-origin home substrate content carries a local provenance record that documents events within the home perimeter, but the provenance chain does not extend across the inter-Self perimeter to the contributing Self's governance history. The records exist, but provenance internalization was configured at too shallow a depth for the context — the provenance chain reaches the FAI event but does not extend back to the contributing Self's home authorization. A backward trace test applied at sufficient depth fails because the chain terminates before it reaches Link 1.

Break Type 4 is structurally distinct from the first three breaks and deserves separate attention. In Break Types 1 through 3, the gap is a missing record: an authorization was not documented, and the gap is immediately visible to anyone who looks for the record and finds it absent. In Break Type 4, all records exist. The local provenance record is present, the FAI event record is present, and the absorption record may be present. The gap is not missing documentation — it is a configuration-adequacy failure. Provenance internalization depth (D2.25) was set at Option A (local-only provenance) when the context required a deeper attribution chain extending to the contributing Self's governance history. The result is a provenance chain that terminates before it can answer the backward-trace question that the context requires. Practitioners who examine the records and find them complete may not recognize Break Type 4 as a gap, because nothing is visibly absent. The gap is only visible when the backward trace is applied at the depth required by context and found to terminate prematurely.

---

## 3. Detection Criteria

Detection applies the backward trace test from D2.67 to any governance outcome arising from FAI events:

1. **Link 1 traceable?** Can the contributing Self's home governance authorization for the contribution (D2.06) be reached by following the provenance chain from the governance outcome? If no: Break Type 1.

2. **Link 2 traceable?** Can the joint authorization for the FAI event (D2.12) — the configuration or orchestration rule under which the shared substrate operation occurred — be identified and verified as jointly authorized? If no: Break Type 2.

3. **Link 3 traceable?** Can the shared-substrate governance of the content's use (D2.15 / D2.14) be traced — is there a record of the governing configuration at the time of use? If no: Break Type 3.

4. **Link 4 traceable?** For content absorbed into a home substrate: can the absorbing Self's home governance authorization for that absorption (D2.11) be reached? If no: Break Type 3 applies. For content present in the home substrate with local provenance only: can the provenance chain be extended through the FAI event back to the contributing Self's governance history? If no at the required depth: Break Type 4.

A "no" at any link identifies AP-23 at that link. A "yes" at every link satisfies the path retraceability requirement at inter-Self scope for that governance outcome.

When examining a system for AP-23, the most common discovery paths are:

- Regulatory audit (D2.63) that requests provenance documentation and reaches a terminus before the full four-link chain is complete.
- Contributing Self governance review that seeks to verify its governance decisions are reflected in shared substrate provenance, and finds that reflection absent.
- Absorbing Self governance review that seeks to verify absorbed content carries full authorization chains, and finds that the chain terminates at the local perimeter.
- Routine backward trace testing of a sample of FAI governance outcomes, where Break Type 4 surfaces only when the trace depth required by context exceeds the configured provenance internalization depth.

---

## 4. Governance Commitment Violated

**Primary commitment violated:** Paper 1 A1.07 — path retraceability.

Paper 1's path retraceability commitment requires that every piece of substrate content carry sufficient provenance that the path back to its antecedents — including the human governance authorizations under which it was produced or used — is reconstructable from substrate content alone. This commitment holds at intra-Self scope (Paper 1) and extends to inter-Self scope by inheritance when FAI events are involved (Paper 3). At inter-Self scope, "the path back to antecedents" includes the four-link cross-organizational authorization chain. A gap at any link means the path cannot be fully reconstructed, and path retraceability fails at inter-Self scope.

**Secondary commitment violated:** Paper 1 Claim 3 — human-governed authority.

The governance sovereignty property requires that every step in the governance of substrate content be traceable to human governance authorization. A gap in the four-link chain means at least one step in the cross-organizational governance sequence lacks traceable human authorization. The claim that the affected governance outcome is fully human-governed cannot be sustained, because the chain of human authorizations is not complete.

**Operational reference:** D2.67 — path retraceability at inter-Self scope. D2.67 defines the four-link structure and specifies that a gap at any link constitutes the authorization chain gap failure.

---

## 5. Consequences

**Governance sovereignty cannot be proven for the affected outcome.** The core consequence is not administrative — it is architectural. The chain of human authorizations is the mechanism by which governance sovereignty is demonstrated. A gap in the chain means the demonstration cannot be completed. The affected governance outcome cannot be certified as fully human-governed, regardless of how well-governed the other links in the chain are. This is a governance accountability failure, not a record-keeping inconvenience.

**Regulatory audit fails at the gap point.** When an audit (D2.63) requests the full authorization chain for a governance outcome, auditors trace link by link. A gap terminates the trace before the full chain is presented. For Break Types 1–3, the gap is immediately visible as a missing record. For Break Type 4, the gap surfaces when auditors apply the trace at the depth required by context and find the chain terminates at the local provenance boundary. In both cases, the audit fails at the gap point.

**The gap may be permanent.** For Break Types 1–3, the missing record corresponds to a governance action that either was taken but not recorded, or was never taken. If the governance action was taken but not recorded, retroactive reconstruction may be possible — the record can be produced with documentation of what is known about when and by whom the authorization was given. If the governance action was never taken, no retroactive record can substitute for the authorization itself; the gap is a permanent accountability deficiency and must be documented as such. For Break Type 4, the gap is typically remediable going forward by reconfiguring provenance internalization depth — but past governance outcomes recorded under Option A cannot retroactively acquire deeper provenance that was not captured at the time.

**Cross-organizational trust is undermined.** Contributing Selves that expect their home governance decisions to be reflected in the shared substrate's authorization chain have no mechanism to verify that reflection if Link 1 records are absent. Absorbing Selves that expect their absorption decisions to complete the chain have no mechanism to verify that prior links are intact if Links 2 or 3 records are absent. The shared substrate's reliability as an accountability artifact depends on all four links being maintained; gaps at any link erode the trust between participating organizations that their shared governance arrangements are functioning as intended.

---

## 6. Intra-Self Analog

Paper 1's path retraceability commitment (A1.07) applies at intra-Self scope: every piece of substrate content must carry provenance sufficient to trace it back, through the substrate alone, to the human governance authorization under which it was produced or used. The intra-Self version of this commitment involves a single organizational perimeter: the provenance chain runs within one Self's home substrate, and the accountability question is whether any given piece of content can be traced to the human governance decisions — orchestration rules authored, overrides exercised — that authorized it.

AP-23 at inter-Self scope is the structural extension of this same failure to the cross-organizational case. The intra-Self gap involves a single broken link in a single organizational perimeter. The inter-Self gap involves a broken link in one of the four links of the cross-organizational chain. The commitment being violated is the same (path retraceability); the scope at which it fails is broader (across the inter-Self perimeter); and the consequence is the same in kind but compounded in scope (governance sovereignty cannot be proven for the affected outcome, and the affected outcome is one that spans organizational boundaries rather than remaining within a single home perimeter).

The intra-Self analog makes clear that AP-23 is not a novel failure mode introduced by Paper 3. It is the Paper 1 failure mode extended to the inter-Self case. Paper 3's contribution is to specify the four-link structure that defines what "complete chain" means at inter-Self scope — a specification that does not exist at intra-Self scope, because intra-Self scope has a single organizational perimeter rather than four ordered inter-organizational links.

---

## 7. Resolution

**Prevention — establishing all four links at each FAI event lifecycle step.**

The authorization chain is established prospectively, at the moment each link is created:

- *Link 1 established at contribution time (D2.06):* The contributing Self's home governance records the authorization decision to contribute aspects to the shared substrate. This record must exist before the aspects are contributed, or must be created contemporaneously with the contribution.

- *Link 2 established at configuration time (D2.12):* The joint FAI event configuration is produced as a jointly authorized governance artifact — a configuration or orchestration rule in the shared substrate that reflects joint human governance authorization. The record of joint authorization accompanies the configuration.

- *Link 3 established during operation (D2.15 / D2.14):* The shared substrate's governance configuration at the time of FAI-origin content use is recorded and traceable. Operations that use FAI-origin content occur under governed conditions that are themselves substrate content.

- *Link 4 established at absorption time (D2.11):* The absorbing Self's home governance records the authorization decision to absorb FAI-origin content into the home substrate. This record must exist before or contemporaneously with the absorption.

For Break Type 4 specifically, prevention requires governance-level attention to provenance internalization depth configuration. Before a FAI event, participating Selves' governance must assess what depth of backward trace will be required by context — regulatory obligations, audit requirements, contributing Self expectations — and configure provenance internalization at the depth that satisfies that requirement. Option A (local-only provenance) may satisfy some contexts; deeper attribution chains are required in others. The configuration decision itself should be governed and recorded as substrate content.

**Remediation of discovered gaps.**

When a gap is discovered after the fact:

- *If the missing governance action was taken but not recorded:* A retroactive record may be produced with documentation of what is known — when the authorization was given, by whom, under what circumstances, and why it was not recorded contemporaneously. The retroactive record should explicitly identify itself as retroactive and document the basis for the reconstruction. This approach preserves partial accountability even when the contemporaneous record is absent.

- *If the missing governance action was never taken:* No retroactive record can substitute for an authorization that was not given. The gap must be documented as a permanent accountability deficiency in the provenance chain of the affected governance outcomes. Governance should assess whether any downstream decisions made in reliance on the ungapped chain need to be revisited, and should establish controls to prevent the same omission in future FAI events.

- *For Break Type 4 gaps:* Going forward, reconfigure provenance internalization depth to the level required by context. For past governance outcomes recorded under Option A, document the depth limitation explicitly in the provenance record so that any backward trace applied to those outcomes encounters an accurate explanation of why the chain terminates at the local boundary, rather than encountering an unexplained terminus.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-23: Authorization Chain Gap.* Derivation note D3.24 (#599) in the CKS derivation series. May 15, 2026. ORCID: 0009-0004-8065-3235. License: CC BY 4.0.
