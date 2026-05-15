# The FAI/Foil Governance Boundary

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

It does not introduce new axioms. Its contribution is to formalize the exact boundary between compliant Full Aspect Integration (FAI) — inter-Self coordination within the prior art's governed scope — and the named architectural foil of the third paper: ungoverned inter-AI coordination through message-passing, tool-calls, or shared-memory access patterns whose substantive content is not human-governable as authored substrate.

---

## Abstract

The third paper in the CKS trilogy introduces Full Aspect Integration (FAI) as the canonical operation for inter-Self coordination via shared substrate, and names its architectural foil as opaque agent-to-agent communication in which inter-AI exchange proceeds without the governance commitments the architecture requires. This note formalizes the exact boundary between compliant FAI and the foil. The boundary is the seven-requirement minimum viable governance floor: an inter-organizational AI coordination mechanism that meets all seven requirements is compliant FAI, within the prior art's governed scope; a mechanism that fails any one requirement is the foil, outside that scope. The note develops the three-scenario boundary case — full foil, partial governance, and minimum FAI — and establishes that partial governance falls decisively in the foil zone. The boundary test admits no partial credit. Proximity to governance is not governance.

---

## 1. The boundary problem

The third paper in the CKS trilogy defends FAI — Full Aspect Integration — as the canonical operation for coordination across distinct governance perimeters. Two organizations' AI systems exchange governance content through a temporary shared substrate, with their participating Selves' human governance authorities jointly authorizing the exchange, contributed aspects merging with conflict preservation as the architectural default, and the shared substrate dissolving back to home perimeters when the coordination event concludes.

The named architectural foil is opaque agent-to-agent communication: inter-AI exchange conducted through messages, tool-calls, or memory-access patterns without authored substrate content, joint human governance authorization, or systematic conflict handling. The foil is not a different kind of coordination; it is the absence of the architecture's governance commitments over the same inter-organizational space.

The boundary between FAI and the foil requires precise formalization. Both involve AI systems at different organizations exchanging governance content. The distinction is not what content crosses organizational boundaries but how it crosses. The governance structure — present in FAI, absent in the foil — is what the boundary turns on. Formalizing this boundary is the most important definiteness case for the prior-art corpus: any adversarial claim that a "partially-governed AI coordination mechanism" is novel must either demonstrate it meets the seven-requirement floor (making it prior-art FAI) or acknowledge it is the foil (outside the prior art's governed coordination scope).

---

## 2. The seven-requirement minimum viable governance floor

The third paper establishes a minimum viable governance floor for compliant FAI events. The floor specifies seven requirements that together constitute the minimum set of governance commitments an inter-organizational AI coordination mechanism must satisfy to fall within the architecture's governed scope. The requirements are:

1. **Authored configuration** — the shared substrate carries configuration authored as substrate content, not as a separate policy artifact evaluated against the substrate at decision time.
2. **Joint authorization** — the coordination event is authorized by human governance actors across participating organizations, with the authorization itself as substrate content.
3. **Construction record** — the establishment of the shared substrate is recorded as authored substrate state.
4. **Exchange bounding** — the exchange is bounded to substrate content per the instinct/reasoning separation; instinct-layer content does not cross the inter-Self perimeter.
5. **Conflict registry** — conflicts surfaced during the FAI event are preserved as first-class substrate state, not silently resolved or discarded at the merge point.
6. **Home perimeter check** — each participating Self's home governance authority is consulted before content is contributed and before ingestion occurs; the exchange does not bypass home perimeter governance.
7. **Dissolution record** — the dissolution of the shared substrate back to home perimeters is recorded as authored substrate state, with the dissolved state traceable.

These seven requirements are not a graded rubric. They are a conjunctive floor. An exchange that satisfies six of seven fails the floor. The floor is the governance line in the sand — below it is the foil; meeting it is FAI.

---

## 3. The three-scenario boundary case

Three versions of an inter-organizational AI coordination event illustrate where the boundary falls:

**Scenario (a) — Full foil.** Two organizations' AI systems exchange governance content via direct API calls. No authored substrate content is created. No human governance actors authorize the exchange. No conflict registry records disagreements between the contributed configurations. No dissolution record exists. This scenario fails all seven floor requirements. It is the architectural foil in its clearest form: ungoverned inter-AI coordination, the pattern the architecture is designed to replace.

**Scenario (b) — Partial governance.** The same exchange occurs, but the organizations maintain records around it: an email thread documenting what was shared, a shared document noting two points of conflict, calendar evidence of a call in which the exchange was discussed. No authored substrate content is created. No joint human authorization exists as substrate state. No systematic conflict registry operates. This scenario fails at minimum three floor requirements (authored configuration, joint authorization, conflict registry) and likely more. It is still the foil.

This is the most important scenario for the boundary analysis. Organizations in this position often believe they have "some governance" and that their position is meaningfully closer to FAI than the full foil is. The architecture's answer is that proximity to governance is not governance. The boundary test has no partial credit. Informal records, however numerous and however carefully maintained, do not satisfy any of the seven floor requirements. Email threads are not authored substrate content. A shared document noting conflicts is not a conflict registry with first-class substrate state. The grey zone that scenario (b) appears to occupy does not exist in the architecture's definiteness framework. Scenario (b) is the foil.

**Scenario (c) — Minimum FAI.** The exchange is conducted through a temporary shared substrate established under joint human authorization across both organizations' governance structures. Configuration is authored as substrate content. The construction event is recorded. The exchange is bounded to reasoning-layer content. Conflicts are preserved as first-class substrate state with a systematic registry. Each home perimeter governance authority has been consulted. Dissolution is recorded. This scenario meets all seven floor requirements. It is compliant FAI, within the prior art's governed scope.

---

## 4. What makes the foil the foil

The foil is not characterized by what content is exchanged. Both FAI and the foil can involve governance content — configuration schemas, orchestration rules, behavioral policies, precedent records — crossing organizational boundaries between AI systems. The content itself does not determine the classification.

The foil is characterized by the *absence* of the architecture's governance commitments:

- No authored configuration as substrate content (the governance content exists, but not in a form that is inspectable, governable, and modifiable as substrate state under the Paper 1 commitments).
- No joint human governance authorization (the exchange proceeds without both organizations' human governance actors placing their authorization into the shared substrate).
- No conflict preservation as first-class governance state (conflicts are resolved at the merge point or silently absorbed, not preserved as addressable substrate state with downstream traceability).
- No governed evolution feed (what each Self ingests from the exchange is not routed through the home perimeter's Paper 2 evolution machinery with asymmetric ingestion under home governance authority).
- No path retraceability (the governance decisions, rationales, and authority provenance of the exchange cannot be reconstructed from authored substrate state).

Each of these absences is individually sufficient to place a coordination mechanism in the foil zone. Together they constitute the foil's structural signature — and the signature of everything the seven-requirement floor is designed to prevent.

---

## 5. The boundary test

For any inter-organizational AI coordination mechanism, the boundary test operates as follows:

Ask whether the mechanism meets all seven minimum viable governance floor requirements enumerated in §2. If it meets all seven, it is compliant FAI — within the prior art's governed inter-Self coordination scope. If it fails any one requirement, it is the architectural foil — outside the prior art's governed scope.

The test is binary. There is no intermediate category between the foil and FAI. An exchange that meets six of seven requirements is the foil. An exchange that has extensive informal governance records but meets zero floor requirements is the foil. An exchange that meets all seven requirements with no additional governance infrastructure is minimum FAI — governed, within scope, and prior art.

The significance of this test for the defensive publication corpus is precise. A claim to novelty over a "partially-governed AI coordination mechanism" must be evaluated against this boundary. If the claimed mechanism meets all seven floor requirements, it is prior-art FAI, not novel. If it fails any requirement, it is the foil — but the foil is itself prior art as the named architectural contrast the third paper develops at §§4.2, 5.2, 6.2, and 7.2. The space in which a novel claim can land is architecturally narrow: it must be a governed inter-Self coordination mechanism that is neither the foil nor compliant FAI, which the seven-requirement floor closes.

---

## 6. Conclusion

The boundary between compliant FAI and the named architectural foil is the seven-requirement minimum viable governance floor. An exchange that meets all seven requirements is FAI — within the prior art's governed inter-Self coordination scope. An exchange that fails any one requirement is the foil — outside that scope.

The partial-governance grey zone is the most practically significant case: organizations with informal records, email trails, or shared documents noting conflicts are operating the foil, not a degraded form of FAI. The boundary test has no partial credit because governance is an architectural commitment, not a proximity gradient. Proximity to governance is not governance.

Both FAI and the foil involve content crossing organizational boundaries between AI systems. The foil is not defined by the absence of cross-organizational exchange but by the absence of authored configuration, joint authorization, conflict registry, and the other commitments the floor requires. The same governance content can cross the same organizational boundary in two categorically different ways — one of which is FAI, and one of which is the foil — and the distinction is entirely in the governance structure, not in the content itself.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The FAI/Foil Governance Boundary.* May 15, 2026. ORCID: 0009-0004-8065-3235.
