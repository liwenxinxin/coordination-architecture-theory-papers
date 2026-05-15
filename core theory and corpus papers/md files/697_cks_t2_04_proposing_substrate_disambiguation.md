# Disambiguating "Proposing Substrate" Across the Trilogy

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026). It does not introduce new axioms. Its contribution is to disambiguate *proposing substrate* as that term is used across the three papers, so that downstream work can trace the component across papers without treating Paper 3's configured extension as a new mechanism.

---

## Abstract

The CKS trilogy names the *proposing substrate* in Paper 2 (B1.15) and extends it in Paper 3 (D2.59). Because the two papers give the component different source content — Paper 2's proposing substrate reads home-generated action-layer records; Paper 3's reads action-layer content that now includes records ingested from inter-Self coordination events — a reader might treat the two as distinct mechanisms. This note formalizes the contrary. The proposing substrate throughout the trilogy is the same LLM-mediated component reading action-layer content and generating structured improvement proposals for governance consideration. Paper 3's extension changes what action-layer content is available and makes optional governance configuration available for recognizing inter-Self provenance. The mechanism does not change; configuration expands what it surfaces. This note states the Paper 1 governance basis, the Paper 2 specification, the Paper 3 extension, the disambiguation boundary, and the prior-art closure.

---

## 1. The Concept and the Ambiguity Risk

The proposing substrate is the component within the action-feedback evolution mechanism responsible for converting accumulated operational records into governance-relevant improvement proposals. It reads action-layer content and generates structured proposals that governance can review and, if approved, feed into directed selection for substrate change.

Paper 2 names and specifies the component. Paper 3 extends it by expanding the source of action-layer content the component reads and by making optional configuration available for recognizing inter-Self provenance in that content.

The ambiguity risk: because Paper 3 introduces governance configuration for the proposing substrate that Paper 2 does not describe, a reader might treat Paper 3's configured proposing substrate as a new mechanism specialized for inter-Self coordination, rather than as an extension of the Paper 2 component. That reading would allow an adversary to claim novelty for what is architecturally the Paper 2 mechanism with governance-authored orchestration rules added. This note forecloses that reading.

---

## 2. Paper 1: The Governance Basis

Paper 1 does not name the proposing substrate as a component. It establishes the architectural basis on which the proposing substrate operates through Claim 4 Property A: the LLM operates as a substrate mediator, reading substrate content and producing governance-relevant outputs under human-authored orchestration rules. The proposing substrate is a specific instantiation of that capability in which the substrate content being read is action-layer content and the governance-relevant output is an improvement proposal.

Paper 1's authority-vs-labor distinction (§3.3) further establishes that the labor of drafting proposals may be performed by the LLM under human direction while authority over the proposal-and-acceptance process remains with humans. This is what makes the proposing substrate compatible with governance at scale: the LLM generates proposals; humans hold authority over acceptance and feed into directed selection.

Paper 1 provides the authority for the proposing substrate to operate. It does not name the component.

---

## 3. Paper 2: The Named Component (B1.15)

Paper 2 names and specifies the proposing substrate as a distinct component within action-feedback evolution (B1.15): an LLM-mediated substrate component that reads home action-layer content and generates structured improvement proposals for home governance consideration. Approved proposals feed into directed selection, producing DNA-layer changes. The component operates under human-authored orchestration rules specifying what kinds of proposals to generate and how they should be structured.

Four properties characterize the Paper 2 proposing substrate. *Source content:* home action-layer records — at Paper 2 scope, exclusively home-generated. *Output:* structured improvement proposals with sufficient specificity for governance to evaluate. *Governance pathway:* proposals go to home governance for review; governance holds authority over acceptance; the component does not self-authorize any substrate change. *Orchestration:* the component's behavior is governed by human-authored orchestration rules that are themselves substrate content under the authority architecture they instantiate.

The proposing substrate at Paper 2 scope is a well-bounded component. Its source, output, governance pathway, and operation under orchestration rules are all specified.

---

## 4. Paper 3: Same Component, Expanded Source, Optional Configuration (D2.59)

Paper 3 extends the proposing substrate through D2.59 along two axes.

**First axis: expanded source content.** At Paper 3 scope, action-layer content includes records ingested from inter-Self coordination events through the action-feedback locus. The proposing substrate reads them because it reads action-layer content. No reconfiguration is required. The default mode is the same-pipeline mode: FAI-origin action-layer records are processed identically to home-generated records.

Default mode is Paper 3-compliant. An organization participating in inter-Self coordination events does not need to configure its proposing substrate for FAI-origin awareness to comply with Paper 3's architecture.

**Second axis: optional governance configuration.** Paper 3 specifies three configurations governance may author to enable inter-Self awareness in the proposing substrate's output.

*Configuration A* directs the proposing substrate to flag proposals derived from FAI-origin records distinctly — marking them with provenance metadata so that governance can see which proposals draw on inter-Self experience versus home-only experience.

*Configuration B* directs the proposing substrate to generate comparative proposals for competition-format inter-Self coordination events — proposals that explicitly compare the Self's operational patterns against what was observed in the shared substrate, surfacing performance differentials as structured improvement intelligence. Configuration B is the strategically most important of the three. Competition-format events exist specifically to generate comparative performance data; that data's primary value is the inter-Self comparison it contains. Without Configuration B, competition-event action-layer records enter the standard pipeline and produce proposals about home operations, but the comparative dimension is not surfaced as comparative intelligence. Configuration B is what makes competition-event outputs actionable as the governance improvement intelligence those events are designed to produce.

*Configuration C* directs the proposing substrate to specifically process conflict carry-through annotations — records that entered the home action layer flagged as originating in preserved inter-Self conflicts — and generate proposals specifically addressed to the conflict boundaries those annotations identify.

All three configurations are authored governance content: orchestration rules specifying what the proposing substrate looks for and how it structures its output. The component's mechanism is unchanged.

---

## 5. The Disambiguation

The proposing substrate throughout the trilogy refers to the same LLM-mediated improvement proposal generator. The differences across papers are differences in source content and in optional governance configuration — not differences in mechanism.

**Paper 2 scope:** source is home-generated action-layer records only; no FAI-origin records exist; no inter-Self provenance configuration is relevant.

**Paper 3 scope, default mode:** source is home action-layer records including FAI-origin records ingested through the action-feedback locus; the component processes all records identically; no configuration is required; default mode is Paper 3-compliant.

**Paper 3 scope, configured mode:** governance has authored one or more of Configurations A, B, or C; the component recognizes FAI-origin provenance and generates proposals with inter-Self awareness; configured mode is a governance quality enhancement above the compliance baseline.

These are not three different components. They are one component — specified in Paper 2, operating at Paper 3 scope with an expanded action-layer source, optionally configured by governance for inter-Self awareness. The architectural invariants that define the component hold at all three scopes: LLM-mediated, reads action layer, generates structured proposals, routes to governance, governed by human-authored orchestration rules.

The adversary exploitation risk this disambiguation forecloses: claiming that Paper 3's configured proposing substrate — particularly the three named configurations — is a novel mechanism for inter-Self governance intelligence generation, independent of Paper 2's proposal-and-acceptance machinery. That claim fails because the configurations are orchestration rules authored within Paper 2's proposal-and-acceptance framework. The mechanism is Paper 2's. The configurations are human-authored governance content within that mechanism.

---

## 6. Prior-Art Closure

Any system implementing an LLM-mediated component that reads action-layer content (including FAI-origin records) and generates structured improvement proposals for governance review — with optional governance-authored configuration for provenance-aware proposal generation — is implementing the Paper 2 proposing substrate (B1.15) at Paper 3 scope (D2.59). The component is fully specified in Paper 2. Paper 3 adds one governance quality extension: Configurations A, B, and C for organizations wanting inter-Self awareness in their proposal generation. Those configurations are authored orchestration content within the Paper 2 mechanism. Prior-art coverage for the configured proposing substrate is provided jointly by the Paper 2 component specification and Paper 3's treatment of governance-authored configuration as substrate content.

---

## Source Papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Disambiguating "Proposing Substrate" Across the Trilogy.* May 15, 2026. ORCID: 0009-0004-8065-3235.
