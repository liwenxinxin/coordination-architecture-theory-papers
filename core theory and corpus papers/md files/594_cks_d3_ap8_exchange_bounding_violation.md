# AP-8: Exchange Bounding Violation

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes AP-8, the second anti-pattern in Taxonomy Category 5 (Perimeter and Content Failures) of the Phase D3 Series D derivation series. AP-8 names the Exchange Bounding Violation: content that is outside the exchange boundary — instinct-layer harness substrate content or LLM weight representations — is present in the shared substrate during a Full Aspect Integration (FAI) event. The exchange bounding commitment (Paper 3 Claim 2, D1.10) restricts FAI exchange to DNA-layer and action-layer substrate content; instinct-layer and LLM-weight content must not cross the inter-Self perimeter. The violation strikes at the outside-the-model commitment that forms the architectural spine of all three CKS papers, now at the widest governance scope the trilogy defines. Detection, governance commitment violated, consequences, intra-Self analog, and resolution — including emergency dissolution — are formalized in the seven-element Phase D3 structure.

---

## 1. Anti-Pattern Name and Category

**AP-8: Exchange Bounding Violation**

**Category 5 — Perimeter and Content Failures.** This category covers failures in which the inter-Self perimeter does not hold as an architectural boundary: content that should remain inside one Self's home governance scope crosses into the shared substrate, or content that the shared substrate's construction excludes is introduced into it. AP-8 is the second of four Category 5 anti-patterns and addresses the specific case in which the violated boundary is the exchange-bounding commitment — the commitment that restricts FAI exchange to DNA-layer and action-layer substrate content and excludes instinct-layer and LLM-weight content categorically.

---

## 2. Description

The exchange bounding violation occurs when content that is outside the exchange boundary is present in the shared substrate during an FAI event. Two distinct content classes are categorically excluded from exchange by the architecture's commitments: instinct-layer harness substrate content (the governance specifications that define each participating Self's instinct layer) and LLM weight representations (model parameter content, including gradient-level representations and any equivalent encoding of model-internal state).

The prohibition is not conditional on content sensitivity or on whether contributing Selves have similar instinct configurations. The exchange bounding commitment (D1.10) is a categorical architectural commitment inherited from Paper 2's instinct/reasoning separation (Paper 2 Claim 1, B0.01) and carried through the inter-Self boundary without modification. The underlying reason is foundational: the CKS trilogy's architectural spine is that authoritative coordination state lives outside the LLM — in the substrate, under governance, subject to the three rights (inspect, modify, override) that define human-governed operation. Instinct-layer content and LLM weights are inside-the-model territory or its closest governance analog. Allowing them to cross the inter-Self perimeter would mean that model-internal content or its governance-specification equivalent enters the authoritative coordination space of another Self — the spine's commitment violated at the highest governance scope the trilogy defines.

The complementary commitment — Paper 3 D1.19, the instinct non-crossing commitment — names this exclusion as an active architectural commitment, not merely an absence. The shared substrate is not simply missing instinct-layer content because no one contributed it; the architecture affirmatively commits that such content will not cross. A violation of D1.10 is therefore simultaneously a violation of D1.19's active commitment: it is not a gap in the record but a breach of an affirmative architectural obligation.

The violation can manifest in two distinguishable forms. In the first form, instinct-layer harness substrate content from a contributing Self appears in the shared substrate — identifiable by content-type classification as harness substrate. This might occur when the AP-6 (Sharing-Scope Misconfiguration) failure analyzed in the prior note produces an over-broad sharing scope that includes instinct-layer content in the contribution package, or when a contributing Self's FAI implementation does not correctly filter content by layer before contribution. In the second form, LLM weight representations or model parameter content appear in the shared substrate, with no provenance chain traceable to any DNA-layer or action-layer contribution. This form is rarer in properly implemented architectures but architecturally more severe: it would mean that model-internal content — the layer that the trilogy commits to keeping outside the governance substrate — has entered the shared substrate that constitutes the authoritative inter-Self coordination state.

---

## 3. Detection Criteria

Detection operates through the exchange bounding verification procedure (D2.16), which specifies four checks. AP-8 is indicated when Check 2 (instinct-layer absence verification) or Check 3 (LLM-weight absence verification) fails, or when any of the following subsidiary signals is present:

**Unattributed content in the shared substrate.** Content in the shared substrate that cannot be attributed to any contributing Self's DNA-layer or action-layer content via contribution records (D2.06) is an exchange bounding violation candidate. The contribution record system is specifically designed to establish provenance for all shared substrate content; content without a traceable provenance chain is structurally suspect.

**Harness substrate content present in the shared substrate.** Content classified as harness substrate — the type-classification that identifies instinct-layer governance specifications — appearing in the shared substrate is a direct indicator of an instinct-layer bounding violation. Content-type classification is the operative check here; harness substrate has a distinguishable type from DNA-layer and action-layer content.

**LLM weight or model parameter content present.** Content in the shared substrate that represents LLM weights, model parameters, or gradient-level encodings — content with no provenance chain to any DNA-layer or action-layer contribution — is a direct indicator of the more severe form of the violation.

**D2.16 Check 2 or Check 3 failure.** The exchange bounding verification procedure's Check 2 explicitly tests for instinct-layer content absence; Check 3 tests for LLM-weight content absence. Either failure triggers the emergency response protocol immediately. Governance does not wait for a second signal when the verification procedure fails.

---

## 4. Governance Commitment Violated

**Primary violation: Paper 3 Claim 2, D1.10** — the exchange bounding commitment. FAI exchange is restricted to DNA-layer and action-layer substrate content. Instinct-layer and LLM-weight content must not cross the inter-Self perimeter. AP-8 is the direct violation of this commitment: the prohibited content is present in the shared substrate.

**Secondary violation: Paper 3 D1.19** — the instinct non-crossing commitment. This is not merely a restatement of D1.10 but a distinct commitment in its own right: the architecture affirmatively commits that instinct-layer content will not cross the inter-Self perimeter, as an active architectural obligation. A bounding violation negates this affirmative commitment. Its violation is architecturally significant in itself, independent of the operational consequences.

**Tertiary violation: Paper 1 Claim 1** — the outside-the-model commitment, which is the architectural spine that all three CKS papers share. Paper 1 draws the governance boundary between the substrate (outside the model, subject to human authority) and the LLM (inside the model, operating under substrate-mediated governance). Paper 2 extends this boundary to the instinct/reasoning separation at Self scope. Paper 3 extends it to the inter-Self perimeter through exchange bounding. If LLM weights cross the perimeter and enter the shared substrate, authoritative coordination state would include model-internal content — the outside-the-model commitment violated at the widest governance scope in the trilogy. The tertiary violation applies specifically when the exchange bounding violation involves LLM-weight content; its invocation signals the most severe form of AP-8.

**Operational reference: D2.16** — the exchange bounding verification procedure, which defines the four checks and specifies that bounding violation detection triggers an emergency response protocol.

---

## 5. Consequences

The consequences of AP-8 are severe and operate at three levels simultaneously.

**Trilogy-level architectural consequence.** The instinct/reasoning separation that Paper 2 Claim 1 establishes, and that Paper 3 D1.19 carries through the inter-Self perimeter as an active commitment, is violated at inter-Self scope. If instinct-layer content from one Self has crossed into the shared substrate, that content is now accessible to another Self through the shared substrate — potentially influencing the other Self's instinct governance through a channel the architecture explicitly closes. The separation that the trilogy treats as foundational is breached at the scope where Selves coordinate with each other, which is the scope where the breach has the widest potential propagation.

**Outside-the-model backbone consequence.** If LLM-weight content has crossed the perimeter, the consequence is of the highest architectural severity the trilogy defines. The shared substrate is the authoritative inter-Self coordination state. If that state contains model-internal content — content from inside the LLM — the outside-the-model commitment that constitutes the trilogy's architectural spine is violated at its widest scope. Authoritative coordination state now includes content whose provenance is inside a model, not in a human-governed substrate. This is not a localized failure; it is a failure of the foundational architectural commitment at the level of inter-Self coordination.

**Operational consequence.** The shared substrate cannot be characterized as a Paper 3-compliant shared substrate while bounding-violating content is present. Governance cannot safely continue the FAI event. Any FAI operations that proceed against a shared substrate containing out-of-bounds content may produce evolution-feed outputs that carry the violation forward into participating Selves' home substrates at the FAI dissolution hand-off — spreading the consequence from the shared substrate into each home governance scope. Stopping the event is not a precautionary measure; it is the operationally correct response to an architecture breach that, if not stopped, propagates.

---

## 6. Intra-Self Analog

Within a single Self, Paper 1's substrate-cell boundary (A1.08) defines the governance boundary between inside-the-model content and substrate content. Content from inside the LLM — model outputs, or model internal state — must be mediated by governance before it enters the substrate. If model-generated content enters the substrate without proper governance mediation (without an orchestration-rule-governed write that subjects the content to the substrate's authority architecture), the substrate-cell boundary is violated at the intra-Self scope.

AP-8 is the direct inter-Self analog of this intra-Self violation. The exchange bounding violation at inter-Self scope is the same type of boundary failure as the substrate-cell boundary violation at intra-Self scope: content from a governance territory where it must remain (the instinct layer or the LLM interior) crosses into a governance territory where it must not be (the shared substrate). The scope difference matters — inter-Self violations propagate across Selves and affect multiple home substrates rather than one — but the architectural structure of the failure is identical. Both are breaches of the outside-the-model commitment at the relevant governance scope.

This structural identity across scopes is not coincidental. It is the consequence of the trilogy's explicit design: Paper 3 carries Paper 1's commitments through to inter-Self scope without modification, and the exchange bounding commitment is precisely the commitment that performs this carry-through for the instinct/reasoning boundary.

---

## 7. Resolution

Resolution for AP-8 is governed by D2.16's immediate bounding violation response protocol. The protocol is not advisory. Detection of a bounding violation triggers it immediately. Governance cannot defer the response or treat the violation as a non-urgent anomaly to be reviewed at the next scheduled checkpoint.

**Step 1 — Preserve the violation record.** The bounding violation is recorded as a first-class conflict in the conflict registry (D2.13), under the conflict preservation commitment that Paper 1 Claim 3 establishes and that carries through to inter-Self scope via Paper 3 Claim 3. The record includes: the content identified as out-of-bounds, its content-type classification, the D2.16 check(s) that failed, the time of detection, and the state of the shared substrate at detection. This record is not erasable under the protocol — it is the authoritative account of the violation and the basis for investigation.

**Step 2 — Quarantine or remove the out-of-bounds content.** The out-of-bounds content is removed or quarantined from the shared substrate under joint governance authority (joint modify right, D2.04). Governance must act promptly; the shared substrate cannot safely resume operational use while bounding-violating content is present. Quarantine is appropriate when removal might destroy evidence needed for root-cause investigation; removal is appropriate when the content is unambiguously out-of-bounds and its quarantine would introduce additional governance complexity.

**Step 3 — Suspend FAI event operations.** Governance does not resume FAI event operations against a shared substrate that has been found to contain out-of-bounds content until the exchange bounding verification procedure (D2.16) has been completed with all four checks passing. Suspension is not optional when the bounding has been violated; it is the operationally required state while the protocol is active.

**Step 4 — Investigate the source of the violation.** Exchange bounding violations do not occur accidentally in a properly governed shared substrate. The presence of instinct-layer or LLM-weight content is a signal that something failed upstream. The investigation must identify the specific root cause. Two primary sources account for the vast majority of violations: first, an AP-6 (Sharing-Scope Misconfiguration) in a contributing Self's contribution configuration — a sharing scope that was not correctly restricted to DNA-layer and action-layer content before contribution, allowing instinct-layer content to be included in the contribution package; second, a defect in the FAI implementation itself — a failure in the mechanism that processes contributions into the shared substrate, which did not enforce the layer-bounding at the contribution boundary. The investigation concludes with a written root-cause finding and a governance decision on corrective action for each identified source.

**Step 5 — Consider emergency dissolution.** If the bounding violation cannot be quickly remediated — if the scope of the out-of-bounds content is unclear, if the investigation cannot identify the source within a reasonable operational window, or if the violation involves LLM-weight content whose provenance cannot be traced — the correct governance response is emergency dissolution under D2.28 Trigger 3. Emergency dissolution is not a failure of governance; it is the governance response the architecture provides precisely for cases in which the shared substrate can no longer be safely operated and remediation cannot be accomplished within the event's operational scope. The decision to dissolve rather than continue is a joint governance decision under joint authority (D2.04).

**Step 6 — Re-verify before resumption.** Following remediation, exchange bounding verification (D2.16) must be completed with all four checks passing before FAI event operations resume. A single passing run of D2.16 is the minimum condition for resumption. Governance may require additional verification steps depending on the scope of the violation found.

The severity gradient across forms of AP-8 is relevant to governance response calibration: an instinct-layer content violation from a misconfigured contribution scope is serious and requires the full protocol, but remediation — removing the out-of-bounds content and correcting the contributing Self's sharing-scope configuration — is usually tractable within the event's operational scope; an LLM-weight content violation triggers the same protocol but with a stronger presumption toward emergency dissolution, because LLM-weight content in the shared substrate represents a more severe breach of the outside-the-model backbone and its source is structurally more difficult to attribute through the contribution record system.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-8: Exchange Bounding Violation.* May 15, 2026. ORCID: 0009-0004-8065-3235.
