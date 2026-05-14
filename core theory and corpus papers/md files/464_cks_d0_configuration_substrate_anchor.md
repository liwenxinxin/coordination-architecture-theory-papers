# Configuration as Substrate Content: Paper 3's Fifth Architectural Claim

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** CKS Defensive Publication Series D, Note D0.05 (#464)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3's fifth architectural claim establishes that every configurable dimension of the Full Aspect Integration (FAI) protocol is substrate content under joint human authority, and that the governance of those configurations is itself substrate content — recursively, bottoming at human-authored authority. This note anchors that claim as prior art. It states the claim precisely, treats each of the six configurable FAI dimensions as an independently claimable sub-commitment, explains recursive applicability in two senses, describes joint authority over the configuration substrate and governance-configurable approval mechanics, traces inheritance from Papers 1 and 2, names the four failure modes the claim defends against, maps the four derived sub-commitments D1.22–D1.25, acknowledges that Claim 5 is the explicit statement of a principle that Claims 1–4 each presuppose, and provides an operational test for whether a given implementation satisfies the commitment.

---

## 1. Position in the Paper 3 claims sequence

Paper 3 introduces six architectural commitments. The first four claims establish the shared substrate as the architectural object of inter-Self coordination (Claim 1), Full Aspect Integration as the canonical operation over that substrate (Claim 2), a three-tier conflict-handling mechanism (Claim 3), and a four-locus evolution-feed mechanism at the FAI dissolution boundary (Claim 4). Each of Claims 1–4 presupposes that its configurable parameters are substrate content under human authority. None of them names that presupposition explicitly.

Claim 5 names it. The claim is: every configurable dimension of the FAI protocol is substrate content authored under joint human authority, and the governance of that configuration is itself substrate content under the same authority structure — recursively, with the recursion bottoming at human-authored authority rather than at fixed architectural invariants.

This double role — standalone claim and unifying articulation of a principle implicit in Claims 1–4 — is the structural position Claim 5 occupies. The note addresses both roles. The claim is claimable as a standalone prior-art commitment (an adversary who hardens FAI configurations into system parameters rather than substrate content introduces an architecture that this claim forecloses). It is also claimable as the unifying prior-art commitment that explains why Claims 1–4 are each governed: configuration-as-substrate-content is the shared principle; Claim 5 makes it visible.

---

## 2. The claim stated precisely

Claim 5 establishes three architectural commitments jointly.

**Commitment (a) — Enumeration of configurable dimensions.** The configurable parameters of the FAI mechanism accumulated across Paper 3's §§5–7 are substrate content authored under joint authority across the governance structures of participating Selves. Each dimension is independently inspectable, modifiable, and overridable under the three rights Paper 1 establishes. No FAI parameter is hardwired into the system; each lives as authored content in the shared substrate.

**Commitment (b) — Recursive applicability.** The configuration substrate is itself substrate content under joint authority. The governance structure that governs FAI configurations is also governed substrate content. This recursion extends without fixed depth: configuration of configuration is substrate content, governance of that configuration is substrate content, and so on. The recursion bottoms at human-authored authority: the base of the recursion is not a system invariant but a human-authored governance commitment. Recursive depth is itself a configurable dimension.

**Commitment (c) — Multi-mediator coordination as configurable pattern.** The coordination pattern active during an FAI event — which mediator roles operate, how they relate, which patterns govern coordination across participating Selves — is a runtime substrate dimension under explicit governance. Pattern selection is governed-substrate content, not an architectural default fixed outside governance.

Together, the three commitments describe an architecture in which every parameter of every aspect of FAI operation is accessible, governable, and modifiable under the same authority structure that governs the coordination substrate itself.

---

## 3. The six configurable dimensions as independent sub-claims

Six configurable dimensions originate from Paper 3's §5 treatment of the FAI-event level. Each is a distinct configuration object. Each is independently claimable as prior art, because an adversary could attempt to claim novelty for any one by presenting it as a novel architectural knob without acknowledging that it is simply a governed substrate dimension. This note closes all six simultaneously.

**3.1 Sharing scope.** Sharing scope specifies which aspects each participating Self contributes to the shared substrate for a given FAI event. This is not an architectural default; it is authored substrate content determined per event under the governance of participating Selves. Limiting contribution to a specified set of aspects, contributing all aspects, or contributing only aspects within a specified content domain are all instances of sharing-scope configuration as substrate content.

**3.2 Cardinality.** Cardinality specifies how many Selves participate in one FAI event. The architecture supports two-Self FAI as the simplest instance and n-ary FAI without fixed ceiling. Cardinality is not an architectural constant; it is a governed substrate dimension specified per event. The governance structures of the initiating Self and of each invited Self hold joint authority over the cardinality specification before the shared substrate is constructed.

**3.3 Persistence policy.** Persistence policy governs what substrate content remains after FAI dissolution and where it persists. The range extends from full dissolution — no content retained anywhere outside the dissolution-time evolution feed — to full audit record in shared-substrate form retained under one or more participating Selves' governance. Policy is authored substrate content, specified per event, not a system-level default. This dimension directly governs the accountability record of each FAI event.

**3.4 Cooperation/competition variant.** The same shared-substrate primitive can operate under different orchestration rule sets: cooperation-oriented rule sets that maximize productive synthesis, competition-oriented rule sets that surface productive tension, and mixed configurations. The rule set is substrate content authored under governance authority. The architecture surfaces the variant as a configuration dimension; governance chooses which rule set applies per event.

**3.5 Provenance carry-over depth at the perimeter.** When a Self contributes an aspect to the shared substrate, governance specifies how much of that aspect's provenance history travels with it across the perimeter. Full carry-over makes the contributed aspect's complete governance history visible within the shared substrate. Partial carry-over carries only a specified depth. Minimal carry-over carries only the identity of the contributing Self and the event timestamp. Depth is authored substrate content, not a fixed architectural floor.

**3.6 Provenance preservation on internalization.** When a Self ingests evolution outputs from an FAI event — via the four-locus feed mechanism Claim 4 establishes — governance specifies how much provenance detail from the FAI event is retained in the home substrate. Full retention enables the home substrate to trace every governance decision from the FAI event forward into home evolution. Minimal retention records only the event identifier. The depth of retention is governed substrate content, not a system default.

Each of the six dimensions satisfies the same test: it is a parameter that an alternative architecture might harden into a system configuration outside human authority. Treating it instead as authored substrate content under the three rights is the architectural commitment this note establishes as prior art.

---

## 4. Recursive applicability in two senses

The recursion in Claim 5 operates in two distinct senses, and conflating them produces either under-claim or over-claim. This section states each sense precisely.

**Sense 1 — Configuration-of-configuration is also substrate content.** The specification of how FAI configurations are authored, approved, and revised is itself substrate content. The governance structure that governs the six configurable dimensions listed in §3 is not an external policy mechanism or a vendor-managed parameter layer; it is authored substrate content under the same three rights. Configuration of that governance structure is also substrate content. The recursion is not architecturally bounded at a fixed depth: it continues until it reaches human-authored governance authority, which is where it bottoms. The base of the recursion is not an architectural invariant (a layer that cannot be modified) but a human-authored commitment (a layer that has been authored under human authority and that humans retain the right to modify). Recursive depth is itself a configurable dimension, which means the recursion is governed at every level by the same authority structure it is instantiating.

This sense is the key inheritance from Paper 2 Claim 6, which established recursive governance at the intra-Self scope: governance parameters are substrate content, and the governance of those parameters is also substrate content. Paper 3 Claim 5 extends this recursion across the inter-Self perimeter and applies it to the FAI configuration substrate specifically.

**Sense 2 — The principle applies across all Paper 3 claims.** The configuration-as-substrate-content principle does not apply only to the six dimensions listed in §3. It applies to every configurable parameter of every Paper 3 architectural commitment. The construction parameters of the shared substrate (Claim 1), the operational parameters of the FAI mechanism (Claim 2), the orchestration rules governing conflict handling (Claim 3), the ingestion policy and per-mechanism feed configurations of the evolution-feed mechanism (Claim 4) — all are substrate content under the same principle. Claim 5 is the explicit statement of a property that Claims 1–4 each presuppose. Placing the prior-art claim explicitly at this level ensures that the principle cannot be claimed as novel in application to any one of the four prior claims individually.

The distinction between the two senses matters for defensive publication. Sense 1 addresses depth: how far the recursion goes. Sense 2 addresses breadth: which claims the principle governs. Both senses must be in the prior-art record to foreclose adversarial claims at either dimension.

---

## 5. Joint authority over the configuration substrate

Authority over the FAI configuration substrate is held jointly by the governance structures of the participating Selves. This joint authority structure has three components.

**Origination authority.** The initiating Self — the Self whose governance originates the FAI event — holds primary authority over the initial configuration substrate. The initiating Self authors the initial values of the six configurable dimensions and proposes them to the invited Selves' governance structures.

**Approval authority.** Each participating Self's governance holds approval authority over the configuration substrate before the shared substrate is constructed. A Self's participation in the FAI event is conditional on its governance approving the configuration. Approval mechanics are themselves governance-configurable substrate content: the architecture does not mandate a specific approval workflow, approval threshold, or approval recording format. What is mandated is that approval authority is held by each participating Self's governance, that the configuration substrate is available for inspection before approval, and that each Self's three rights apply to the configuration substrate at the approval stage.

**Modification authority.** During the FAI event, configuration substrate may be modified only under joint authority. No single Self's governance can unilaterally modify configuration dimensions that were approved jointly. The joint-modification mechanics are themselves governance-configurable substrate content.

Each of the three components satisfies the authority-not-labor principle Paper 1 §3.3 establishes: humans hold authority over the configuration substrate; AI systems operating as substrate mediators may draft, populate, or propose modifications to configuration substrate, but the authority to approve, modify, or revoke configuration substrate is not delegable to an AI system.

---

## 6. Inheritance from Papers 1 and 2

Claim 5 inherits without re-defense from six prior commitments across Papers 1 and 2.

**From Paper 1 Claim 3 (human-governed authority).** All substrate content — including configuration content — is subject to the three rights (inspect, modify, override) at any time. This is the foundational commitment Claim 5 applies to FAI configuration dimensions. The three rights are the mechanism by which configuration-as-substrate-content is meaningful: configuration substrate that cannot be inspected, modified, or overridden is not governed in the CKS sense regardless of where it resides.

**From Paper 1 §3.3 (authority-vs-labor distinction).** The portable phrase Paper 1 renders — governance is an authority architecture, not a review workflow — holds at FAI configuration scope. Humans hold authority over the configuration substrate; AI systems acting as substrate mediators draft, suggest, and populate configuration substrate operating under human direction. This distinction is what allows configuration governance to scale with FAI event frequency: governance cost is proportional to rule-variety and intervention-frequency, not to the number of FAI events.

**From Paper 2 Claim 5 (multi-shaped governance as substrate content).** Paper 2 established that governance parameters — including the instinct/reasoning boundary specification, content-domain specification, and death-type configuration — are substrate content. Paper 3 Claim 5 extends this commitment from intra-Self governance parameters to FAI protocol parameters. The architecture of the extension is the same: governance parameters live in the substrate, are subject to the three rights, and are authored under human authority.

**From Paper 2 Claim 6 (recursive applicability).** Paper 2 established recursive governance at intra-Self scope: the governance of governance parameters is also substrate content. Paper 3 Claim 5 inherits this recursion and extends it to the inter-Self scope, applying it to the FAI configuration substrate and its governing governance structures. The bottom-out commitment — that the recursion grounds at human-authored authority rather than at architectural invariants — is inherited directly from Paper 2's formulation.

**From Paper 3 §4 (shared substrate commitment).** The shared substrate carries configuration as substrate content as an architectural commitment for the shared substrate scope. Claim 5 elaborates this commitment across the configurable-dimensions and recursive-governance angle rather than re-defending it. The §4 commitment is the most load-bearing inheritance for Claim 5: Claim 5 is articulation of what §4's commitment produces when accumulated across the configurable dimensions §§5–7 establish.

**From Paper 3 §§5–7 (cumulative configurable dimensions).** The six FAI-event-level dimensions (§3 above) plus the conflict-handling-level dimensions (tier-selection rules, conflict-class definitions, escalation-path configurations, joint-authority configurations, recursive-governance depth, authority-articulation mechanics) and the evolution-feed-level dimensions (hand-off push-vs-pull, per-mechanism feed configurability, content-class availability at home, ingestion-policy enumeration, conflict-annotation propagation depth) collectively carry the substantive content of Commitment (a). Claim 5 states that all of these — seventeen dimensions accumulated across §§5–7 — are substrate content authored under joint authority. None of them is architecturally prescribed; all are human-governed configuration points.

---

## 7. Failure modes the claim defends against

Claim 5 defends against four failure modes, each of which represents an architecture that the prior-art commitment forecloses.

**Hardwired FAI configurations.** An architecture in which FAI parameters — cardinality, sharing scope, persistence policy, and others — are fixed at the infrastructure level, not authored as substrate content. In such an architecture, governance cannot inspect, modify, or override the parameters; they are system behavior rather than governed content. The prior-art commitment forecloses this by establishing each parameter as substrate content subject to the three rights.

**FAI configurations governed outside the substrate.** An architecture in which FAI parameters are adjustable but are governed through mechanisms outside the substrate — configuration files, vendor-managed policy layers, platform settings, environment variables. In such an architecture, the three rights may nominally apply to the configuration values but the governance mechanism is not itself substrate content and is not inspectable or modifiable under the substrate-governance commitment. The prior-art commitment forecloses this by requiring that the configuration governance mechanism itself is substrate content.

**Non-recursive governance.** An architecture in which FAI configurations are substrate content but the governance of those configurations is not — where the specification of how configurations are authored and approved lives outside the substrate in a non-governed layer. In such an architecture, the recursion halts at the configuration values rather than extending through the governance structure to human-authored authority. The prior-art commitment forecloses this by establishing recursive applicability as an architectural property of the substrate-content commitment rather than an optional extension.

**Vendor-determined FAI parameters.** An architecture in which FAI parameters are set by the infrastructure provider rather than by the governance authority of participating Selves. In such an architecture, the three rights are absent from the configuration dimension: the infrastructure provider holds effective authority over parameters that determine the operational character of every FAI event. The prior-art commitment forecloses this by requiring that joint authority over configuration substrate is held by the participating Selves' governance structures, not by any third party.

---

## 8. Derived sub-commitments D1.22–D1.25

Claim 5 decomposes into four derived sub-commitments for Phase D1 treatment.

**D1.22 — All six FAI-event-level configurable dimensions as substrate content.** Each of the six dimensions enumerated in §3 — sharing scope, cardinality, persistence policy, cooperation/competition variant, provenance carry-over depth at the perimeter, and provenance preservation on internalization — is independently claimable prior art. D1.22 covers each dimension as a separately claimable commitment. The Phase D1 note for D1.22 will treat each dimension with the same structural care as the six Paper 1 sub-commitments receive in Phase A1 and the twenty Paper 2 sub-commitments receive in Phase B1.

**D1.23 — Configuration-of-configuration as substrate content.** The specification of how FAI configurations are authored, approved, and modified is itself substrate content under the three rights. This sub-commitment is the recursive-applicability formalization at Sense 1 as defined in §4: the governance structure governing FAI configuration is governed substrate content. The Phase D1 note for D1.23 will establish this as prior art at the FAI scope, inheriting from Paper 2 Claim 6's intra-Self formulation.

**D1.24 — Recursive applicability bottoming at human-authored authority.** The recursion in D1.23 is bounded — it does not recurse to an infinite meta-hierarchy but bottoms at human-authored governance commitments that humans retain the right to modify. The bottom-out point is not an architectural invariant but a human-authored authority commitment. Recursive depth is itself a governed substrate dimension. The Phase D1 note for D1.24 will establish the bounded-recursion commitment as prior art, distinguishing it from fixed-floor recursion and from unbounded meta-governance architectures.

**D1.25 — Joint authority over configuration substrate across participating Selves; approval mechanics as governance-configurable substrate content.** The joint-authority structure described in §5 — origination authority, approval authority, modification authority — is itself a prior-art commitment. The approval mechanics (what workflow, what threshold, what recording format) are governance-configurable substrate content. The Phase D1 note for D1.25 will establish joint-authority configuration as prior art at the inter-Self scope, inheriting from Paper 2's multi-shaped governance commitment at intra-Self scope.

---

## 9. Operational test

A system instantiates Paper 3 Claim 5 if and only if all of the following are true for every FAI event the system performs.

**Test 1 — Six dimensions locatable.** For any FAI event, an observer with appropriate access can locate the six configurable dimensions listed in §3 — sharing scope, cardinality, persistence policy, cooperation/competition variant, provenance carry-over depth, and provenance preservation on internalization — as authored substrate content within the shared substrate or within the governance substrate governing the event. If any dimension is absent from the substrate and instead hardwired into system behavior or encoded in a vendor-managed layer outside the substrate, the test fails.

**Test 2 — Human authorization verifiable.** For each of the six dimensions, an observer can verify that the configuration value was authorized under the three rights by the governance of at least one participating Self (origination), and approved by the governance of all participating Selves (approval), before the shared substrate was constructed. If configuration values were set without human authorization or were set by a party without governance authority over the participating Selves, the test fails.

**Test 3 — Configuration-of-configuration also in substrate.** An observer can locate the specification of how the FAI configuration was authored and approved — the governance structure governing the configuration — as substrate content accessible under the three rights. If the governance-of-configuration lives outside the substrate (in a vendor policy layer, a platform setting, or an informal process not recorded as substrate content), the test fails.

**Test 4 — Three rights apply at configuration scope.** An observer can confirm that any participating Self's governance holds the right to inspect, modify, and override any of the six configuration dimensions and any part of the configuration-of-configuration substrate, without requiring authorization from the infrastructure provider or from a non-governance party. If any configuration dimension is inspectable but not modifiable, or modifiable only with external authorization, the test fails.

**Test 5 — Principle applies across Claims 1–4.** An observer can verify that the construction parameters of the shared substrate (Claim 1), the operational parameters of the FAI mechanism (Claim 2), the conflict-handling orchestration rules (Claim 3), and the evolution-feed governance configurations (Claim 4) are all substrate content accessible under the three rights. If any of the four prior-claim parameter sets is hardwired or externally governed, the test fails for Sense 2 of recursive applicability.

A system that passes all five tests instantiates Claim 5. A system that fails any one of Tests 1–4 has hardwired or externally governed FAI configuration; it may be a functional inter-Self coordination architecture but it is not a CKS-architecture implementation of Paper 3 Claim 5. A system that passes Tests 1–4 but fails Test 5 has correctly implemented configuration-as-substrate-content for the six FAI-event-level dimensions while leaving the broader principle unapplied to Claims 1–4; the prior-art commitment at Sense 2 forecloses that partial implementation as novel.

---

## 10. Conclusion

Paper 3 Claim 5 establishes that every configurable dimension of the FAI protocol is substrate content under joint human authority, with the governance of those configurations recursively also substrate content, bottoming at human-authored authority. The claim operates on two levels simultaneously: as a standalone prior-art commitment closing six independently claimable configuration dimensions, and as the explicit statement of a principle that Claims 1–4 each presuppose. Sub-commitments D1.22–D1.25 carry the claim forward into Phase D1 derivation, with each sub-commitment independently claimable and jointly exhaustive of the claim's prior-art coverage.

The governing phrase from Paper 1 §3.3 — governance is an authority architecture, not a review workflow — holds at FAI configuration scope without modification. Human authority over configuration substrate is the architectural commitment; how that authority is exercised, how the approval workflow is structured, and how deep the configuration-of-configuration recursion extends are all governed substrate dimensions under the same authority.

---

## Source papers

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Configuration as Substrate Content: Paper 3's Fifth Architectural Claim.* CKS Defensive Publication Series D, Note D0.05 (#464). May 14, 2026. ORCID: 0009-0004-8065-3235. License: CC BY 4.0.
