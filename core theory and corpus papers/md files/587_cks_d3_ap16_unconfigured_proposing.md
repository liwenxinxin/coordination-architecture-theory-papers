# AP-16: Unconfigured Proposing Substrate

**Derivation Note #587 — Phase D3, Anti-Pattern 12 (D3.12)**
**Series:** D — Paper 3 Anti-Pattern Formalizations
**Taxonomy Category:** 3 — Evolution Feed Failures (closing note)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

AP-16 formalizes the anti-pattern in which a participating Self correctly ingests FAI-origin action-layer records into its home substrate but never configures its proposing substrate to recognize and handle FAI-origin provenance distinctly. The proposing substrate processes all action-layer content identically — FAI-origin records and home-generated records receive the same pipeline treatment — regardless of the governance intelligence value that distinguishing them would provide. AP-16 is a governance *optimization* failure rather than a governance *integrity* failure: the default same-pipeline behavior is architecturally valid, and a system exhibiting AP-16 is not broken. The anti-pattern is about a Self that accepts the default in circumstances where governance-configured differentiation would yield meaningful intelligence return on FAI participation investment. The violation is of Paper 3 Claim 5 (configuration as substrate content), specifically the sub-commitment that leaving a configurable governance dimension at system default when that configuration would provide governance intelligence value is itself an implicit configuration choice — one that governance should make explicitly. The note closes Taxonomy Category 3 (Evolution Feed Failures) and signals that Category 4 (Configuration Failures) follows.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-16 — Unconfigured Proposing Substrate

**Category:** Taxonomy Category 3 — Evolution Feed Failures (fourth and final)

**Severity:** Governance optimization failure (not governance integrity failure)

Category 3 covers failure modes in which FAI-derived content either does not reach the home substrate's evolution mechanisms at all, reaches the wrong mechanism, or — as in AP-16 — reaches the proposing substrate correctly but without the governance intelligence scaffolding that would make the feed actively useful. The four Category 3 anti-patterns together exhaust the evolution feed failure space: AP-4 (no ingestion from FAI dissolution), AP-5 (wrong layer routing at ingestion), AP-15 (instinct-layer boundary violation), and AP-16 (unconfigured proposing substrate). AP-16 is the last of the four and closes Category 3.

---

## 2. Description

A participating Self correctly applies D2.10 at FAI dissolution: FAI-origin action-layer records are ingested into the home action layer through governance-configured hand-off, arriving with their provenance intact. The ingestion step is not the problem. The problem begins downstream, at the proposing substrate.

Paper 2's proposing substrate (B1.15) is the component through which action-layer evidence generates improvement proposals for governance consideration. In AP-16, this component has never been configured to recognize FAI-origin provenance as a distinct evidence category. It has no authored orchestration rules specifying how FAI-origin records should be processed differently from home-generated records. The result is that all action-layer content — regardless of whether it originated within the Self's own operations or arrived from a joint FAI event — is processed identically through the same proposal-generation pipeline.

D2.59 defines three governance-configured enhancements to the proposing substrate that a participating Self may author:

- **Config A — FAI-specific proposal flagging:** Proposals that are FAI-informed are marked distinctly, surfacing them in the proposal stream without changing how they are evaluated. This is the minimum useful configuration: it enables governance to identify which improvement proposals carry inter-Self learning, even if the evaluation process remains unchanged.

- **Config B — Comparative proposal generation:** For competition-variant FAI relationships, the proposing substrate generates comparative proposals that explicitly surface approach differences between the Self and its FAI partners. This is the mechanism through which competition events yield actionable governance intelligence about relative approaches — the distinctive value that a competition FAI relationship offers over cooperation.

- **Config C — Conflict annotation processing:** Conflict carry-through annotations (D1.16) that arrived in the home action layer during ingestion receive specific processing through the proposing substrate, ensuring that governance boundary signals embedded in the FAI event's preserved conflicts are surfaced as proposals rather than absorbed silently into the undifferentiated proposal stream.

In AP-16, none of these configurations has been authored. The governance configuration opportunity that D2.59's three options represent is left unused. FAI learning is absorbed but not actively leveraged.

**Severity calibration.** This is an explicit and important framing decision for the note. AP-16 is not in the same severity class as AP-4, AP-5, or AP-15. Those three anti-patterns involve governance integrity failures — ingestion not occurring, content routed to a mechanism that should not receive it, or content reaching the instinct layer in violation of the Paper 2 architectural boundary. AP-16 involves none of these. The system is functioning correctly by architectural standards. FAI-origin records are in the home action layer. The proposing substrate is generating proposals. Governance is receiving them. What governance is not receiving is the *differentiated intelligence* that configured proposing-substrate behavior would provide. The anti-pattern is about a missed governance intelligence investment, not a broken governance architecture. Practitioners triaging remediation effort should address integrity-failure anti-patterns before optimization failures; AP-16 remediation is appropriate when the question is maximizing governance improvement return on FAI participation investment.

---

## 3. Detection Criteria

Three indicators identify AP-16 in a participating Self:

**Criterion 1 — FAI records present, configuration absent.** FAI-origin records are present in the home action layer (D2.10 correctly applied), but no authored orchestration rules for the proposing substrate specify FAI-origin record handling. Inspection of the proposing substrate's configuration substrate reveals no rules that branch on FAI-origin provenance, no flagging logic for FAI-informed proposals, and no comparative proposal generation for competition FAI partners.

**Criterion 2 — Post-mortem indistinguishability.** Post-mortem review (D2.39) following FAI events finds that governance cannot determine which improvement proposals in the proposal stream were FAI-informed and which were home-generated. The proposal stream is a flat sequence without provenance markers. Governance looking back at a period of FAI participation cannot identify the governance value that participation contributed to the proposal record.

**Criterion 3 — No comparative proposals for competition FAI.** For Selves participating in competition-variant FAI relationships (D2.65), the proposing substrate produces no proposals that specifically surface approach differences between the Self and its FAI partners. Competition events contribute action-layer records that flow into the general proposal stream and are processed identically to cooperation-FAI records and home-generated records. The approach-difference intelligence that Config B would generate is absent from governance's deliberation materials.

Criterion 3 is the most consequential indicator and the primary trigger for remediation prioritization when competition FAI relationships are active.

---

## 4. Governance Commitment Violated

**Primary:** Paper 3 Claim 5 — Configuration as substrate content.

Claim 5 establishes that every configurable dimension of the FAI mechanism is itself substrate content under all six Paper 1 commitments: inspectable, governable, modifiable under authority. How FAI-origin records are processed by the proposing substrate is a configurable dimension of how FAI evolution outputs are used. D2.59 makes this concrete by specifying three configuration options that governance may author. Leaving all three unused when FAI participation is active is an implicit configuration choice — the choice to accept the system default — and Claim 5's commitment is that this choice should be made explicitly by governance, with awareness of the governance intelligence value each configuration option would provide. Implicit default-acceptance is not what Claim 5 permits; it is what Claim 5's explicit-governance-authority commitment is designed to replace.

**Operational reference:** D2.59 (three governance-configured enhancements to the proposing substrate). All three configuration options available under D2.59 are unused in AP-16; the governance intelligence value of each — proposal visibility (Config A), competitive approach-difference analysis (Config B), conflict-boundary surfacing (Config C) — is unrealized.

---

## 5. Consequences

Four consequence classes follow from AP-16:

**Consequence 1 — FAI learning absorbed but not leveraged.** FAI-origin records enter the home action layer and generate proposals, but governance receives no signal indicating which proposals are FAI-informed. The learning is absorbed into the proposal stream and may influence which proposals are eventually accepted, but governance cannot direct attention toward FAI-informed proposals, cannot track the governance improvement return from specific FAI events, and cannot evaluate FAI participation value against its costs. The governance intelligence that provenance-aware proposing substrate behavior would provide is entirely absent.

**Consequence 2 — Competition FAI intelligence gap.** For competition-variant FAI relationships, Consequence 1 is especially acute. The primary governance intelligence value of competition FAI — understanding how the Self's approaches compare to those of its FAI partners, identifying where partner approaches offer improvement potential — depends on Config B's comparative proposal generation. Without it, competition events produce action-layer records that merge into the undifferentiated proposal stream. Governance receives proposals informed by the competition event but cannot identify them as such and receives no comparative framing. The governance investment in competition FAI participation yields substantially less actionable learning than configured behavior would provide. Practitioners with active competition FAI relationships should treat the absence of Config B as the highest-priority remediation item within Category 3's optimization failure class.

**Consequence 3 — Conflict annotations silently absorbed.** Conflict carry-through annotations (D1.16) in the home action layer — governance boundary signals preserved from FAI events where conflicts were not resolved before dissolution — receive no special governance attention through the proposing substrate. Config C would route these annotations through specific processing that surfaces their boundary-signaling content as proposals. Without Config C, annotations are present in the home action layer but do not generate the targeted governance attention their information value warrants. Governance boundary signals from FAI are absorbed into the general proposal stream at the same weight as routine action-layer evidence.

**Consequence 4 — Reduced FAI participation return.** Across all three consequence classes, the unifying effect is that the governance improvement return on FAI participation investment is lower than it could be with configured proposing substrate behavior. FAI participation requires operational investment: the shared substrate construction, the FAI event itself, the ingestion process at dissolution. AP-16 means this investment yields a reduced intelligence return. The shortfall is not visible to governance — governance receives proposals, does not recognize the gap — making AP-16 a self-concealing optimization failure. It produces no governance errors and triggers no escalation signals; it simply produces less than it could.

---

## 6. Intra-Self Analog

Paper 2's proposing substrate (B1.15) is a configured governance component. Its proposal-generation behavior is co-determined with its mechanism shape through governance-authored orchestration rules. Operating it with no configuration for evidence-type awareness is the intra-Self analog: a proposing substrate that cannot distinguish between different types of action-layer evidence, processing all content through a single undifferentiated pipeline regardless of the governance intelligence value that evidence-type distinctions would provide.

The intra-Self analog is real but weaker than AP-16 for a structural reason. Within a single Self, action-layer evidence varies in type — different operational contexts, different cells, different periods — but these differences are differences of *degree* along dimensions the proposing substrate's home governance already understands. FAI-origin records are qualitatively different in kind: they represent inter-Self learning, carrying provenance from a governance perimeter outside the Self's own authority architecture. The governance intelligence value of identifying this evidence type is categorically different from distinguishing, say, high-volume routine evidence from low-volume exception evidence within the home action layer. The intra-Self analog captures the structural form of the failure — a proposing substrate operating without evidence-type configuration — but does not capture the governance significance of the specific evidence type that AP-16's proposing substrate fails to recognize. FAI-origin records are not just another subtype of home evidence; they are the product of inter-Self coordination, and their governance treatment should reflect that distinction.

---

## 7. Resolution

D2.59's three configuration options constitute the resolution spectrum. Resolution does not require implementing all three; the appropriate configuration depends on the FAI relationship type and the governance intelligence goals the Self's governance holds for FAI participation.

**Config A — FAI-specific proposal flagging (minimum useful configuration).** Governance authors orchestration rules for the proposing substrate that mark proposals generated from FAI-origin action-layer records with a provenance flag. The flag does not change how proposals are evaluated; it makes FAI-informed proposals visible in the proposal stream. This minimum configuration closes the post-mortem indistinguishability problem (Criterion 2) and enables governance to track FAI participation return over time. Config A is appropriate for any Self with active FAI participation and represents the baseline below which no participating Self should remain.

**Config B — Comparative proposal generation (priority for competition FAI).** Governance authors orchestration rules that instruct the proposing substrate to generate comparative proposals when processing action-layer records from competition-variant FAI events. Comparative proposals surface specific approach differences between the Self and its FAI partners, framing them as governance-actionable improvement candidates. This configuration realizes the primary governance intelligence value of competition FAI relationships. Governance practitioners with active competition FAI relationships should prioritize Config B; its absence is the most consequential manifestation of AP-16. Config B is also applicable, in attenuated form, to cooperation FAI where approach-comparison is a governance interest.

**Config C — Conflict annotation processing (targeted for boundary surfacing).** Governance authors orchestration rules that route conflict carry-through annotations in the home action layer through specific processing in the proposing substrate, generating proposals that surface the governance boundary signals those annotations carry. Config C is targeted: it is most valuable when FAI events regularly produce preserved conflicts whose boundary-signaling content would otherwise be absorbed without governance attention. It is appropriate when D1.16 annotations are present in meaningful volume and when governance holds explicit interest in the boundary conditions FAI events have surfaced.

The resolution sequence for most participating Selves: implement Config A first to close the post-mortem gap, then evaluate whether competition FAI relationships are active (implement Config B if so), then assess whether conflict annotation volume warrants Config C. All three configurations are substrate content under Claim 5: the orchestration rules that implement them are authored by governance under its authority, inspectable and modifiable at any time, and subject to the same governance disciplines as all other substrate content in the home perimeter.

---

## Category 3 Closure Note

AP-16 is the fourth and final anti-pattern in Taxonomy Category 3 (Evolution Feed Failures). The four Category 3 anti-patterns exhaust the ways evolution feed from FAI participation can fail:

- **AP-4** — No ingestion at FAI dissolution: FAI-origin records never reach the home substrate.
- **AP-5** — Wrong layer routing: FAI-origin records are ingested but routed to the wrong evolution mechanism, mismatching content type to mechanism.
- **AP-15** — Instinct-layer boundary violation: Action-layer records are routed to instinct evolution, violating the Paper 2 architectural boundary that AP-16's fourth Category 3 note follows.
- **AP-16** — Unconfigured proposing substrate: Records reach the correct mechanism but the proposing substrate's governance configuration opportunity is left unused.

AP-4 and AP-5 are ingestion-layer failures. AP-15 is a boundary-integrity failure. AP-16 is a post-ingestion optimization failure. Together they form a complete failure taxonomy for the evolution feed dimension of FAI participation governance.

**Category 4 (Configuration Failures) follows.** Category 4 addresses anti-patterns in which the broader configuration-as-substrate-content commitment of Paper 3 Claim 5 is violated — not only at the proposing substrate but across the configurable dimensions of FAI mechanism operation. AP-16 bridges the two categories: it is formally a Category 3 failure (proposing substrate receives evolution-feed content without differentiation) that is diagnosed and resolved through Category 5's governing framework (Claim 5). This bridge makes AP-16 a natural closing note for Category 3 and an orientation note for the configuration failure territory that follows.

---

*End of Derivation Note #587*
