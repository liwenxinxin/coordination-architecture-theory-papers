# AP-14: Competitive Intelligence Misrouting

**Series:** CKS Derivation Notes — Phase D3 (Paper 3 Anti-Pattern Formalizations)
**Note number:** D3.08 (#583)
**Anti-pattern:** AP-14 — Competitive Intelligence Misrouting
**Category:** 2 — Conflict Handling Failures *(fourth and final entry; Category 2 closes with this note)*
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

AP-14 formalizes a misconfiguration anti-pattern specific to competition-variant Full Aspect Integration (FAI) events: the event is correctly designated as the competition variant but its conflict routing rules are configured with resolve-tier dominance rather than preserve-tier dominance. Because preserved conflicts are the primary output of competition-variant FAI — they are the record of where the two Selves' governance approaches differ — resolve-dominant routing destroys the event's competitive intelligence value entirely. The anti-pattern violates Paper 3 Claims 3 and 5: Claim 5 because two governed configuration objects (variant selection and conflict routing rules) are internally inconsistent within the same governed substrate, and Claim 3 because the preserve tier is the architecturally appropriate tier for approach-difference conflicts in competition-variant events. AP-14 closes Category 2 (Conflict Handling Failures) of the Phase D3 anti-pattern taxonomy.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-14 — Competitive Intelligence Misrouting

**Category:** 2 — Conflict Handling Failures (fourth and final entry; Category 2 closes with this note)

Category 2 collects anti-patterns in which inter-Self conflict handling is misconfigured or misapplied: conflicts that should be preserved are resolved, conflicts that should be escalated are suppressed, or — as in AP-14 — the conflict routing configuration contradicts the event variant it is intended to serve. AP-14 is the only Category 2 entry that operates at the configuration-coherence level rather than at the conflict-handling mechanism level directly. The failure is not that the preserve tier is broken; it is that the preserve tier is not invoked because routing rules direct approach-difference conflicts away from it. The mechanism is sound; the configuration governing which conflicts reach which tier is self-contradictory.

---

## 2. Description

A Full Aspect Integration event is configured as the competition variant (D2.20, D1.22 Dimension 4). The organizational intent is comparative governance learning: the two participating Selves bring aspects covering the same coordination domain, and the event is designed to surface where their approaches differ. Those differences are the event's product — the governance intelligence the participating organizations intend to carry home and absorb into their respective evolution machinery.

The misconfiguration occurs at the conflict routing rules (D2.51 Configured Object 1). The routing rules, which are themselves governed substrate content specifying which conflict classes route to which tier, direct approach-difference conflicts to the resolve tier rather than the preserve tier. In a well-configured competition-variant event, approach-difference conflicts should route to the preserve tier: the differences are retained as first-class substrate state, annotated with provenance, and carried through to each participating Self's home governance via carry-through annotations (D1.16) as the comparative intelligence the event was designed to produce. Under AP-14's misconfiguration, the orchestration rules instead collapse those differences — conflicts are resolved within the shared substrate, a single outcome is recorded, and the divergence point disappears from the substrate record.

The result is that a competition-variant event produces cooperation-variant outputs. The conflict registry for the event shows predominantly RESOLVED entries. The preserved conflict registry — which is the competitive intelligence product — is absent or nearly empty. When governance staff review the event's outputs, they find little actionable comparative information about where the two Selves' approaches differ, because the routing rules eliminated that information during event execution.

The misconfiguration is an internal contradiction between two governed substrate objects: the variant selection designates competition, but the conflict routing rules behave as if the event were cooperation-variant. Both objects are governed substrate content under Paper 3 Claim 5's recursive governance commitment. Their contradiction is a governance failure at the configuration layer — two substrate entries that cannot both be honored simultaneously, authored under the same joint governance authority, left in conflict.

---

## 3. Detection Criteria

Three signals distinguish AP-14 from correctly configured competition-variant events.

**Routing-rules mismatch.** The FAI event configuration carries the competition variant designation (D2.20), but inspection of the conflict routing rules (D2.51 Configured Object 1) reveals that the dominant routing path directs conflicts — including approach-difference conflicts — toward the resolve tier. Both configuration objects are inspectable substrate content; their contradiction is directly visible to governance staff exercising the inspection right Paper 1 §3.3 establishes. The mismatch is detectable before the event executes if a configuration review step checks for variant-routing consistency.

**Inverted conflict registry.** The conflict registry for the event shows predominantly RESOLVED entries and few or no PRESERVED entries. In a correctly configured competition-variant event, the distribution should be inverted: approach-difference conflicts should generate PRESERVED entries as the normal case, with RESOLVED entries limited to factual inconsistencies and other conflict classes for which resolution is the appropriate governance response. An event yielding an overwhelmingly RESOLVED registry under a competition-variant designation is a signature of AP-14.

**Post-mortem intelligence gap.** Post-mortem review (D2.39) of the event finds little actionable comparative intelligence about governance approach differences. Governance staff cannot point to a preserved conflict registry showing where the two Selves diverge. The event record contains coordination outcome entries rather than conflict boundary signals. The evolution feed (Paper 3 Claim 4) from the event delivers resolution records to each participating Self's home governance machinery rather than preserved-conflict annotations. The third signal is the consequence-level manifestation of the first two; organizations without mature post-mortem practices may diagnose it as unexpected approach similarity rather than as misconfiguration.

---

## 4. Governance Commitment Violated

**Primary violation — Paper 3 Claim 5 (configuration as substrate content).**

Claim 5 establishes that every configurable dimension of an FAI event is itself substrate content governed under all six Paper 1 commitments. This applies to variant selection and to conflict routing rules equally. Because both are governed substrate objects, their internal consistency is a governance responsibility: a substrate carrying two self-contradicting configuration objects has not been maintained under coherent governance. Competition variant selection paired with resolve-dominant conflict routing is a configuration contradiction — the two objects designate incompatible event behaviors within the same governed substrate. Claim 5 does not merely require that configuration objects exist as substrate content; it requires that the substrate carrying them be governed coherently. Internally inconsistent configuration is a governance failure at the Claim 5 layer.

The authority-vs-labor distinction Paper 1 §3.3 establishes applies here without modification: governance is an authority architecture, not a review workflow. The humans holding governance authority over the competition-variant event configuration hold both the right to set the variant designation and the right to set the conflict routing rules. When those two rights are exercised inconsistently — competition variant selected, resolve-dominant routing left in place — the resulting configuration contradiction is a governance failure, not an architectural limitation of the substrate.

**Secondary violation — Paper 3 Claim 3, Tier 1 (preserve tier).**

Claim 3's three-tier conflict-handling mechanism assigns the preserve tier to conflicts best handled by retaining both sides as first-class substrate state. For competition-variant FAI events, approach-difference conflicts are precisely the class for which the preserve tier is the architecturally appropriate response: the organizational value of those conflicts lies entirely in their preservation. Routing them to the resolve tier instead violates the governance intent behind Claim 3's preserve tier as it applies at competition-variant scope. The preserve tier is not broken; it is bypassed by misconfigured routing.

**Operational reference — D2.51 (configuration governs conflict handling).**

D2.51 establishes that conflict routing rules are configured objects, not architectural constants. Their misconfiguration is a governance failure, not an architectural limitation. The correct configuration is specifiable and available; AP-14 is a failure to specify it consistently with the variant designation already in place.

---

## 5. Consequences

**Competitive intelligence output is absent.** The primary deliverable of a competition-variant FAI event is the preserved conflict registry documenting where the two Selves' governance approaches differ. Under AP-14's misconfiguration, this registry is empty or near-empty. The event produces no comparative intelligence. The organizational motivation for running a competition-variant event — learning where governance approaches diverge — is not served.

**Governance resources are misallocated.** Competition-variant FAI events require organizational investment: aspects must be identified, configured, and contributed; joint governance authority must be established across participating Selves' governance structures; post-mortem review must be planned. These investments are predicated on the event yielding comparative intelligence. When resolve-dominant routing is active, the event spends those resources to produce cooperation-variant outputs — records of resolutions, not records of differences. The investment in a competition-variant event returns cooperation-variant value.

**Carry-through annotations do not reach home governance.** Paper 3 Claim 4's four-locus evolution feed depends, for competition-variant events, on preserved conflicts carrying through as evolution-feed annotations to each participating Self's home substrate (D1.16). When approach-difference conflicts are resolved rather than preserved, there is nothing to carry through. The comparative learning that competition-variant events are designed to inject into home governance evolution machinery does not occur. Each participating Self's home substrate evolves as if the comparative differences had not surfaced during the event.

**Evolution feed delivers the wrong signal class.** The action-feedback evolution machinery at each home perimeter receives coordination outcome records rather than conflict boundary signals from the event. These are not equivalent inputs. Coordination outcome records indicate that coordination was achieved; conflict boundary signals indicate where the two Selves' approaches created friction that the preserve tier captured. The former is low-information input for governance evolution at comparative scope; the latter is high-information input. AP-14 systematically delivers low-information input in place of the high-information input the competition-variant design was intended to produce.

**Standing configuration propagates the failure.** If the resolve-dominant routing rules are encoded in the standing configuration for competition-variant events (D2.21), every future competition-variant event inherits the misconfiguration. A single standing-configuration error propagates forward across the entire series of subsequent events until detected and corrected. Post-mortem review of the first affected event (D2.39) that identifies the gap has the opportunity to correct the standing configuration before subsequent events repeat the failure; organizations that lack rigorous post-mortem practices may run multiple misconfigured events before the pattern is recognized.

---

## 6. Intra-Self Analog (or Absence Explanation)

No direct intra-Self analog exists for AP-14. The anti-pattern is specific to competition-variant inter-Self FAI governance — an architectural construct introduced in Paper 3 that has no counterpart in Papers 1 or 2.

The competition variant of FAI configures an inter-Self event to surface governance approach differences rather than to resolve them. This is a Paper 3 invention. A single Self does not run competition-variant operations against itself. Papers 1 and 2's conflict handling addresses conflicts that arise during coordination within a Self's own architecture; neither paper introduces a concept of deliberately staging coordination events to surface and preserve approach-difference conflicts as an inter-organizational intelligence-gathering exercise. The structural prerequisite for an intra-Self analog — a formal competition-variant designation at cross-cell or cross-aspect scope, paired with a matching preserve-dominant routing intent that could be misconfigured — is absent from the intra-Self architecture.

The closest intra-Self parallel that could be constructed is configuring an aspect to suppress cross-cell conflicts rather than preserve them when cross-domain coordination differences are the governance intelligence being sought. But this is a weak and incomplete parallel. The intra-Self architecture as specified in Papers 1 and 2 does not introduce a formal "competitive learning variant" designation at any scope. Without that designation, there is no substrate object analogous to the variant selection in D2.20, and therefore no configuration-coherence failure analogous to AP-14's contradiction between variant selection and routing rules. The anti-pattern requires two governed objects that can contradict each other; the intra-Self architecture, as scoped through Paper 2, does not introduce the relevant pair.

Honest acknowledgment of this gap is preferable to a forced mapping. AP-14 is among the Phase D3 anti-patterns that are genuinely novel at Paper 3 scope — configurations that can fail only in ways that Paper 3's architectural additions introduce. The absence of a B3.xx counterpart is not a deficiency; it is a reflection of the fact that competition-variant FAI governance is a Paper 3 contribution without antecedent at intra-Self scope.

---

## 7. Resolution

The resolution requires aligning two configuration objects that AP-14 leaves in contradiction: the variant selection and the conflict routing rules. Both are governed substrate content; the alignment is achieved through governance authority over those objects, not through architectural modification.

**Correct configuration for future events.** D2.65 (competitive intelligence FAI configuration) specifies the correct pairing: competition variant selection (D2.20, D1.22 Dimension 4) combined with preserve-tier-dominant conflict routing rules (D2.51 Configured Object 1). The routing rules should direct approach-difference conflicts to the preserve tier and factual inconsistency conflicts to the resolve tier. These two routing classes cover the dominant conflict types in competition-variant events; their tier assignments should reflect the organizational intent behind each class. Approach differences are the intelligence being sought; factual inconsistencies are coordination housekeeping. The routing rules should treat them accordingly, and the two assignments together constitute a coherent, internally consistent competition-variant configuration.

**Governance inspection as pre-event detection.** Because both configuration objects are inspectable substrate content under Paper 3 Claim 5, governance staff can detect the contradiction before an event executes. A configuration review step that checks for variant-routing consistency — competition variant paired with preserve-dominant routing, cooperation variant paired with resolve-dominant routing — catches AP-14 before the event wastes governance resources. The inspection right that Claim 5 and Paper 1 §3.3 secure is the operational mechanism for this detection; it requires no additional architectural machinery beyond the substrate rights the architecture already commits to.

**Post-mortem correction for completed events.** For events already completed with misconfigured routing, post-mortem review (D2.39) should document the configuration gap explicitly. The post-mortem record should note that the conflict registry does not represent the competitive intelligence the event was designed to produce, that carry-through annotations to home governance are incomplete as a result, and that the standing configuration (D2.21) requires correction before subsequent competition-variant events are run. The post-mortem record is itself governed substrate content and becomes part of the auditable history of the configuration failure.

**Standing configuration update.** If the misconfiguration is encoded in the standing configuration for competition-variant events (D2.21), the correction must update the standing configuration, not only individual event configurations. A standing-configuration correction propagates forward to all future events that inherit from it, addressing the propagation consequence identified in §5. The correction is a single governed write to substrate content; the modification right Paper 1 §3.3 establishes makes it available to governance staff at any time without architectural constraint.

---

## Closing Note on Category 2

AP-14 is the fourth and final anti-pattern in Category 2 (Conflict Handling Failures). Category 2's four entries address failure modes at different layers of the inter-Self conflict-handling architecture: anti-patterns in which conflict recognition fails, anti-patterns in which tier assignment is incorrect for a given conflict class, anti-patterns in which escalation paths are bypassed, and — in AP-14 — anti-patterns in which the configuration objects governing conflict routing contradict the event variant they are intended to serve. AP-14 is the configuration-coherence failure mode that Category 2 required to be complete. The four entries together cover the conflict-handling failure space from mechanism to configuration to meta-configuration, providing a taxonomy of the ways inter-Self conflict handling can fail at each layer of the architecture. With AP-14, Category 2 closes.
