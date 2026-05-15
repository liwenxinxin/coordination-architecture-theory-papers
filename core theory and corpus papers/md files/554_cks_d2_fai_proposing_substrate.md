# FAI Evolution Feed and the Proposing Substrate

**Derivation Note D2.59 — Phase D2, Note #554**
**CKS Defensive Publication Series**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** CC BY 4.0

---

## Position in the Series

This note is the fifty-ninth Phase D2 derivation note (#554). It formalizes the interaction between two mechanisms that the series has established in prior notes: FAI-origin action-layer records entering the home action layer (D2.10), and the proposing substrate component that reads the home action layer and generates improvement proposals for home governance to consider (Paper 2 B1.15). D2.59 is cross-paper operational synthesis: it requires Paper 3's FAI evolution feed architecture and Paper 2's action-feedback evolution machinery to be held simultaneously.

The note covers four topics in sequence: (1) the default interaction, in which the proposing substrate processes FAI-origin records as action-layer evidence without distinguishing their origin; (2) three governance-configured enhancements that make FAI learning explicitly visible in the proposal stream; (3) the governance implication that all three configurations are authored orchestration rules — Claim 5 substrate content applied to the proposing substrate; and (4) the anti-pattern that results when a Self ingests FAI-origin records but leaves the proposing substrate unconfigured to attend to them.

---

## Background: The Two Mechanisms

**The proposing substrate (B1.15).** Paper 2 established that action-feedback evolution — the third of the three Paper 2 evolution mechanisms — operates through a proposal-and-acceptance cycle. Operational evidence accumulates in the home action layer. A substrate component, mediated by an LLM operating under human-authored orchestration rules, reads that action-layer content and generates improvement proposals for home governance to consider. Governance reviews, authorizes, or declines proposals. Authorized proposals become directed changes to home DNA. This is the proposing substrate: an LLM-mediated mechanism whose inputs are action-layer records and whose outputs are governance-reviewable improvement proposals. The orchestration rules under which proposals are constructed are themselves substrate content — humans hold authority over those rules and can modify them under the same authority architecture that governs everything else in the home substrate.

**FAI-origin action-layer records (D2.10).** Paper 3 established that when a Full Aspect Integration event dissolves, content from the shared substrate propagates to each participating Self's home substrate per governance-configured ingestion at the home perimeter. The layer-routing rule specifies that action-layer content from the FAI event feeds action-feedback evolution at home. D2.10 formalized this: FAI-origin records enter the home action layer carrying FAI-origin provenance, entering the same pipeline through which home-generated records flow. A home Self that participates in an FAI event acquires a new class of action-layer content — records of what the shared substrate accomplished, what approaches the participating Selves contributed, what outcomes were produced — alongside its own home-generated operational records.

The D2.59 question is: how do these two mechanisms interact, and what governance choices determine whether the interaction is maximally useful?

---

## The Default Interaction: Same Pipeline

By default, the proposing substrate has no awareness of FAI-origin provenance. It reads the home action layer as a unified body of operational evidence. FAI-origin records and home-generated records both enter this body. The proposing substrate processes all of them, generating improvement proposals from the full action layer.

This default behavior is both the minimum viable case and a fully legitimate operating mode. A Self that participates in FAI events and ingests FAI-origin records into its home action layer will, in the default mode, have its proposing substrate generate proposals informed by the richer evidence base that FAI produced. FAI learning enters the proposal stream — it just enters without explicit identification of its inter-Self origin. For many deployments, this is sufficient. The proposals are governance-relevant; governance reviews and authorizes or declines them; authorized proposals improve the home deployment. The fact that some of those proposals were informed by FAI-origin evidence rather than purely home-generated evidence does not diminish their value.

The "same pipeline" principle (D2.10) is exactly this: FAI-origin records are first-class action-layer content. The proposing substrate's default behavior honors that principle. It does not need to be configured to benefit from FAI learning — the benefit enters automatically through the action layer.

The three governance-configured enhancements described below are enhancements above this default floor. They make FAI learning *explicitly visible* in the proposal stream rather than mixed with home-generated proposals. Whether this visibility is worth the configuration cost is a governance judgment that depends on the deployment's FAI relationships, the volume and frequency of FAI events, and how actively home governance wants to track inter-Self learning as a distinct source of improvement proposals.

---

## Three Governance-Configured Enhancements

When governance wants inter-Self learning to be explicitly visible — not merely present in the action layer but specifically surfaced as a distinct category of improvement signal — it can configure the proposing substrate's orchestration rules to attend to FAI-origin provenance. Three configurations are available.

### Config A: FAI-Specific Proposal Generation

The proposing substrate's orchestration rules are authored to identify FAI-origin records in the action layer and generate proposals specifically flagged as arising from inter-Self learning. The output is a distinct category of improvement proposal — not mixed into the general proposal stream, but tagged for governance attention as proposals whose evidential basis comes from another Self's operational experience contributing to a shared event.

What Config A produces: governance can see, in the proposal stream, which proposals are grounded in FAI-origin evidence. A governance reviewer looking at a proposal about, say, how a particular class of tasks should be handled in the DNA layer can see whether that proposal was generated from home-generated operational evidence, from FAI-origin evidence, or from both. This supports governance judgments about how much weight to give a proposal — a proposal grounded in inter-Self learning from a well-established FAI relationship may carry different authority than a proposal grounded in a single home-generated operational incident.

Config A does not require that FAI-origin proposals be treated differently in the authorization process. It requires only that they be *identified* in the proposal stream. What governance does with that identification — apply different review criteria, require additional authorization, fast-track for consideration, or treat identically to home-generated proposals — is a further governance choice.

### Config B: Comparative Proposal Generation

The proposing substrate's orchestration rules are authored to generate proposals in comparative form when FAI-origin records include content from another Self's governance approach that differs from the home Self's approach. The proposal format is explicitly comparative: "Self A's approach to X differs from our approach; consider whether our approach should be updated."

This configuration requires more from the orchestration rules than Config A. It is not sufficient to flag FAI-origin provenance; the rules must be authored to construct a comparative analysis — identifying what the other Self's approach was, how it differs from the home approach, and surfacing that difference as an explicit governance question. The LLM mediating the proposing substrate performs this comparative reasoning under the authored orchestration rules.

Config B is particularly valuable for the competition variant of FAI (D2.20). When a Self uses competitive FAI to evaluate its approach against those of other Selves — participating in a shared event where the explicit purpose is to compare governance approaches, operational patterns, or DNA content — the action-layer records from that event will contain rich evidence of what the other Selves' approaches produced. Without Config B, the proposing substrate may generate proposals informed by that evidence but will not make the comparison explicit. With Config B, the proposals directly surface the governance question that competition FAI was designed to address: is our approach better or worse than the alternatives, and should we update? The competition FAI event produces not just comparative awareness but comparative improvement proposals. This is how competition FAI closes the loop: the shared event generates action-layer evidence; the proposing substrate configured for comparative generation turns that evidence into explicit governance proposals; governance reviews and selects which improvements to authorize.

Config B also applies in cooperative FAI, wherever another Self's approach to a shared domain differs from the home Self's and the difference is governance-relevant. The comparative format makes the difference explicit and actionable rather than leaving it for governance to discover by reading unstructured proposal text.

### Config C: Conflict Annotation Processing

Paper 3's three-tier conflict handling (D1.16) specifies that when an FAI event dissolves with conflicts preserved at the first tier — conflicts that could not be resolved via configured orchestration and were not escalated to joint human authority — those conflicts can carry through as annotations in the content that enters each home Self's substrate. D2.10 established that these conflict carry-through annotations enter the home action layer with FAI-origin provenance.

Config C authorizes the proposing substrate's orchestration rules to treat conflict carry-through annotations as a specific class of governance boundary signal, distinct from ordinary operational evidence. When the proposing substrate encounters a conflict carry-through annotation in the home action layer, it generates a proposal specifically addressed to the identified conflict boundary: what the home Self's governance needs to consider, decide, or specify in order to resolve the conflict that the FAI event could not resolve through its own orchestration.

What Config C produces: conflict boundaries that the shared substrate surfaced during the FAI event — places where the participating Selves' approaches were genuinely incompatible and neither automatic orchestration resolution nor joint governance escalation resolved them — become home governance proposals. The home Self does not need to discover these conflict boundaries independently through its own operational experience; the FAI event already identified them. Config C makes the proposing substrate the mechanism by which that identification becomes actionable home governance work.

Config C is architecturally important because it closes a loop that would otherwise require governance to manually inspect FAI-origin records for conflict annotations. Without Config C, governance must know to look for conflict annotations and to interpret them as governance boundary signals — a workload that is likely to be inconsistent in practice. With Config C, the proposing substrate performs that interpretation automatically under authored orchestration rules, generating specific proposals for governance review.

---

## The Governance Implication: Configurations as Authored Orchestration Rules

All three configurations share a structural property: they are authored orchestration rules within the home substrate. They are not settings toggled in infrastructure; they are not capability switches in the LLM; they are substrate content — specifically, the orchestration rules that govern how the proposing substrate's LLM-mediation operates over the action layer.

This is Claim 5 from Paper 2 (configuration as substrate content) applied to the proposing substrate specifically. The governance choice of whether to operate in default mode or in one or more of the three configured modes is expressed as substrate content under the home authority architecture. The orchestration rules specifying "attend to FAI-origin provenance and generate flagged proposals" (Config A), "construct comparative proposals when FAI-origin records show divergent approaches" (Config B), or "treat conflict carry-through annotations as specific governance boundary signals" (Config C) are authored by humans or LLMs operating under human direction, are subject to the same governance processes as all other substrate content, and are inspectable, modifiable, and reversible through the same authority architecture.

This means the governance decision about how explicitly to surface inter-Self learning is itself a governed, documented, authoritative choice rather than an informal practice or undocumented implementation detail. A governance reviewer can examine the proposing substrate's orchestration rules and determine from them what class of proposals the substrate is configured to generate, which FAI-origin signals it is configured to attend to, and what proposal format it will produce for each signal type. The configuration choice is legible in the substrate.

It also means the configurations can be changed without modifying the LLM or the proposing substrate's underlying mechanism. Shifting from default mode to Config B, or from Config A to a combination of Config A and Config C, is a substrate content change under the home authority architecture — the same kind of change as any other DNA evolution under directed selection.

---

## The Proposing Substrate as FAI Learning Integrator

When the proposing substrate is configured for FAI learning — in any of the three configurations — it becomes the home governance component that integrates FAI learning into the ongoing improvement cycle. The full cycle is:

FAI event → shared substrate dissolution → governance-configured ingestion at home perimeter → FAI-origin records enter home action layer with provenance (D2.10) → proposing substrate (configured to attend to FAI-origin provenance) → improvement proposals in the configured format → governance review and authorization → directed DNA change

Each step in this cycle is governed and traceable. The FAI event's outcomes are preserved in the action layer with provenance. The proposing substrate's processing is governed by authored orchestration rules. The proposals are governance-reviewable artifacts. The authorized changes are DNA evolution under the home authority architecture. At no point does FAI learning enter the home Self's DNA through a path that bypasses governance review.

This is the architectural property that makes FAI a sustainable long-term improvement mechanism rather than an uncontrolled import of another Self's patterns. The proposing substrate is the chokepoint: all FAI learning that becomes home improvement passes through it, under home governance authority, on terms home governance has specified in authored orchestration rules.

The multi-Self implication is significant: a network of Selves that each configure their proposing substrates for FAI learning will, over repeated FAI events, systematically surface inter-Self learning as actionable governance proposals. Each Self's improvement cycle incorporates evidence from the full set of Selves it has FAI relationships with, processed through its own governance-authorized orchestration rules, producing home-specific improvement proposals rather than copies of another Self's DNA. The inter-Self learning that Paper 3 positions as a collective evolution mechanism at population scope operates, at the individual Self level, through this proposing substrate interaction.

---

## Anti-Pattern: The Unconfigured Proposing Substrate

A Self that ingests FAI-origin records into its home action layer but leaves the proposing substrate with no configuration for FAI-origin provenance is operating in a mode where FAI learning enters the proposal stream but remains invisible as such. The proposals the proposing substrate generates may be informed by FAI-origin evidence — the default same-pipeline mode guarantees that — but governance cannot distinguish which proposals reflect inter-Self learning from which reflect home-generated operational evidence.

This is a governance visibility gap, not an architectural failure. The substrate is functioning correctly. The proposals are legitimate. But governance is not positioned to:

- Evaluate proposals with awareness of their inter-Self evidential basis
- Track whether FAI relationships are producing improvement proposals at the expected rate
- Identify which conflict boundaries from FAI events still require home governance attention
- Generate comparative governance proposals when FAI events have surfaced approach divergences

For a Self with low FAI event frequency or strong governance preferences against distinguishing inter-Self from home-generated proposals, the unconfigured mode may be a deliberate and justified choice. For a Self that participates in FAI events precisely to accelerate learning from other Selves — particularly competition FAI (D2.20), where the entire purpose is comparative improvement — the unconfigured proposing substrate is a missed opportunity. FAI learning enters the action layer; it reaches the proposal stream; but governance cannot see it as a distinct signal and cannot act on it as such.

The anti-pattern is particularly consequential when conflict carry-through annotations (Config C's territory) are present in the home action layer. Those annotations represent unresolved governance boundaries that the FAI event identified. Without Config C, the proposing substrate will not specifically surface them as governance work items. They will exist in the action layer — inspectable by humans who think to look — but will not be converted into governance proposals. The conflict boundaries the FAI event worked hard to identify will not automatically become home governance attention.

---

## Operational Test

For a Self with active FAI relationships, the following test determines whether the proposing substrate is configured for FAI learning:

**Step 1.** Examine the proposing substrate's authored orchestration rules. Are there rules that attend to FAI-origin provenance in the action layer? If no such rules exist, the proposing substrate is operating in default mode.

**Step 2.** If provenance-attending rules exist, identify which configuration they implement: flagged proposal generation (Config A), comparative proposal generation (Config B), conflict annotation processing (Config C), or some combination.

**Step 3.** Examine the proposal stream from a period containing FAI events. Can proposals generated during that period be traced to specific FAI-origin action-layer records? Is the traceability legible from the proposal's form (Config A or B) or from the proposal's explicit reference to a conflict annotation (Config C)?

**Step 4.** For competition FAI events specifically (D2.20): do the proposals generated following those events include comparative proposals in the Config B form? If competition FAI events produce no comparative proposals in the proposal stream, the proposing substrate is not configured to make competition FAI's learning output actionable.

A Self that passes all four steps has a proposing substrate that is not only configured for FAI learning but produces a traceable chain from inter-Self event to home improvement proposal. A Self that fails at Step 1 is operating in default mode — legally and architecturally correct, but without explicit inter-Self learning visibility. A Self that passes Step 1 but fails Step 3 or Step 4 has authored orchestration rules but those rules are not producing the proposal outputs the configurations are meant to generate — a substrate content problem requiring governance attention to the orchestration rules themselves.

---

## Summary

D2.59 establishes the interaction between FAI-origin action-layer records (D2.10) and the proposing substrate (B1.15) at three levels of governance configuration. The default interaction is same-pipeline: FAI-origin records enter the home action layer and the proposing substrate processes them as action-layer evidence, generating proposals that may be informed by inter-Self learning but do not identify it as such. This is the minimum viable case — sufficient for most deployments, consistent with D2.10's same-pipeline principle, and architecturally correct without any configuration.

Above the default floor, three governance-configured enhancements make FAI learning explicitly visible. Config A generates flagged proposals identifying FAI-origin evidence. Config B generates comparative proposals when FAI-origin records show approach divergence — the mechanism that makes competition FAI produce actionable governance improvement proposals. Config C processes conflict carry-through annotations as specific governance boundary signals, converting FAI-identified conflict boundaries into home improvement proposals.

All three configurations are authored orchestration rules — Claim 5 substrate content applied to the proposing substrate. They are governed, inspectable, modifiable, and reversible under the home authority architecture. The governance choice of which configuration to use determines how explicitly the home Self's improvement cycle incorporates inter-Self learning as a visible, traceable signal.

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

*License: CC BY 4.0. This note is deposited as a defensive publication establishing prior art for the architectural pattern described. No patent rights are asserted. Reuse permitted with attribution.*
