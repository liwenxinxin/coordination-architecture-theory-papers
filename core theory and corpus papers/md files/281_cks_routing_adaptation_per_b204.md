# Routing Adaptation per B2.04 — Decomposing B1.13 Mutation as Instinct Evolution by Formalizing How Routing Rules per B2.04 Adapt in Response to Mutation Events Following Verification per B2.63, Including Gradual and Complete Transition Routing, Split Routing Across LLM Versions During Transition, and Routing Return to Uniform Post-Integration

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

This note is the sixty-fourth in Phase B2 of the Series B derivation chain, and the fourth of six notes decomposing B1.13 multi-level simultaneous evolution. It formalizes routing adaptation per B2.04 as the operational mechanism by which CKS deployments manage the transition of cells to new LLM versions following mutation events per B2.61 and verification outcomes per B2.63. Routing adaptation is not a single operation but a family of five routing patterns — complete transition routing, gradual transition routing, split routing, routing around bad instinct, and return to uniform — each triggered by specific verification outcomes and governance decisions. The note argues that the architectural distinctiveness of routing adaptation lies in its cell-type-specific granularity: whereas conventional AI model updates typically affect all consuming components uniformly, routing adaptation enables concurrent per-cell-type LLM version management, making "routing around bad instinct" per B1.13 operationally realizable and enabling risk-calibrated mutation integration. All routing rule changes are substrate-resident governance events: authored per A2.04, recorded with provenance per A2.40, and retroactively preserved per A6.02. Routing adaptation is reversible. The note distinguishes routing adaptation from pinning per B2.65, states the inherited Paper 1 commitments it carries, enumerates operational implications including high-stakes cell ordering and cross-partner routing authority, and states limits including the absence of any guarantee that a new LLM version will produce stable behavior in production.

## 1. Why routing-adaptation-per-B2.04 requires standalone formalization

B2.61 established the mutation event: when an LLM provider releases a new model version, a mutation event enters the CKS deployment from upstream. B2.62 established mutation detection: the operational mechanisms by which the deployment identifies that a new version has arrived. B2.63 established verification gate triggering: the conditions under which a verification substrate engages to evaluate the new version and produce a PASS, PARTIAL, or FAIL outcome. What B2.61 through B2.63 do not formalize is the step that follows: how routing rules per B2.04 are updated in response to verification outcomes to direct cells toward or away from the new LLM version.

That step — routing adaptation — is the deployment's primary operational control over which LLM version each cell type consults. It is not self-specifying from B2.63's output. A verification PASS does not automatically route any cell to the new version; a FAIL does not automatically block all cells. Each outcome informs a governance decision, and the governance decision is implemented through routing rule changes authored per A2.04. Routing adaptation is the mechanism that converts verification outcomes into operational state.

The need for standalone formalization is both architectural and strategic. Architecturally, routing adaptation is the mechanism through which "routing around bad instinct" per B1.13 — Paper 2's named governance shape for mutation — is operationally instantiated. Without a precise account of how routing rules change in response to mutation events and verification results, the "routing" element of mutation governance is a commitment without a specified realization. Strategically, the note occupies the sixty-fourth position in Phase B2's prior-art chain, and formalizes a cluster of patentable design decisions — granular cell-type-specific LLM version management, split routing across versions during transition periods, high-stakes-last ordering, routing reversibility — that are distinguishable from the general concept of model versioning or canary deployment and that the prior-art chain requires be placed in evidence explicitly.

## 2. The architectural adaptation precisely stated

Routing adaptation per B2.04 is the governed modification of routing rules that specify which LLM version each cell type consults, executed in response to mutation events per B2.61 and informed by verification outcomes per B2.63. The adaptation takes five operationally distinct patterns, each applicable under specific conditions.

**Complete transition routing.** After verification returns a full PASS outcome per B2.63 and governance determines that the verification coverage is sufficient to support deployment-wide adoption, routing rules are updated per A2.04 to specify the new LLM version for all eligible cells. All cell types that previously routed to the prior version are rerouted to the new version as a single coordinated governance event. Complete transition is appropriate when the verification substrate has covered the deployment's relevant behavioral surface and governance judges the residual risk acceptable for full adoption.

**Gradual transition routing.** After verification returns a PASS outcome — or a PASS outcome on a sufficiently broad subset of test cases — governance may elect to route cells to the new LLM version incrementally rather than all at once. A subset of cell types is rerouted to the new version initially; additional cell types are added as operational experience with the new version accumulates and confirms that the verification results hold in production. Gradual transition is the risk-management routing pattern: it enables mutation integration without requiring governance to accept full deployment-wide adoption before production evidence is available.

**Split routing.** During any gradual transition period, the deployment operates in a split routing state: some cell types consult the new LLM version and others consult the prior version concurrently. Split routing is not an intermediate failure state; it is an intentional and governed operational configuration in which different cell types may be on different LLM versions simultaneously. Routing rules specify which cell types route to which version. Different cell types may have different transition timelines based on their behavioral surface, their stakes, and the evidence accumulating from earlier-transitioned cells.

**Routing around bad instinct.** When verification returns a FAIL outcome per B2.63, routing rules maintain the current LLM version for all affected cells. The new LLM version is detected per B2.62 and evaluated per B2.63, but routing does not expose cells to it. This is the operational realization of "routing around bad instinct" per B1.13: the new version's instinct capability may be degraded or behaviorally incompatible in the ways verification revealed, and routing prevents that degraded instinct from reaching cell execution. Routing around bad instinct is also the appropriate pattern when a PARTIAL outcome per B2.63 reveals that specific cell types would be harmed by the new version: those cell types remain routed to the prior version while cell types with passing test cases may proceed to gradual or complete transition.

**Return to uniform.** After a complete transition has concluded — all cell types now routing to the new LLM version — routing returns to a uniform state in which all cells consult one version. The prior version is no longer referenced in routing rules. Return to uniform closes the transition period and re-establishes the simple routing state that preceded the mutation event. Routing rules may retain a reference to the prior version as an archived routing target if governance elects to preserve a reversion path, but uniform operation is re-established for normal execution.

All five patterns share the same governance structure. Routing rule changes are authored by authorized humans per A2.04. Each change is recorded with provenance per A2.40's six metadata fields. Routing rule history is preserved retroactively per A6.02 — prior routing states remain addressable after change. Routing rules are substrate-resident authoritative content per A2.46, meaning they are not implementation details but governed artifacts subject to the same authority architecture as all other substrate content.

## 3. What makes routing adaptation architecturally distinctive

The architectural distinctiveness of routing adaptation per B2.04 is its granularity: cell-type-specific LLM version management that allows different cells to consult different LLM versions concurrently.

Conventional AI model updates do not have this property. When a deployment adopts a new model version in a non-CKS context, the update typically applies uniformly — either the deployment has adopted the new version or it has not. Some production engineering practices provide partial analogs: canary deployments route a percentage of traffic to a new model version, blue-green deployments maintain two complete environments, shadow launches run the new version in parallel without serving its outputs. These practices address deployment risk, but they operate at the traffic or environment level, not at the level of per-cell-type behavioral surface. They do not encode cell-type-specific routing rules as governed substrate content, and they do not have a mechanism for routing specific cell types around specific verification failures while allowing other cell types to proceed.

CKS routing adaptation operates at the cell-type level. A deployment with many distinct cell types — each with its own DNA layer content, action layer behavior, and role in the Self — can simultaneously route some cell types to the new LLM version, hold other cell types on the prior version pending further verification evidence, and completely exclude cell types whose test cases failed verification from any contact with the new version. This granularity is what makes "routing around bad instinct" per B1.13 architecturally realizable: a mutation that degrades instinct quality for some cell types does not require holding all cell types on the prior version. The deployment can extract the capability gains the new version provides for the cell types where verification passed while protecting the cell types where it failed.

The second distinctive property is reversibility. Routing rules are substrate content authored per A2.04 and preserved per A6.02. If the new LLM version proves problematic in production after routing adaptation has completed — whether due to behavior outside the verification scope or due to capability degradation that emerges over time — governance can reverse the routing adaptation by authoring new routing rules that restore the prior version for affected cell types. Reversal is a governance event of the same type as the original adaptation: it goes through the same authoring, recording, and retroactivity mechanisms. This is architecturally different from deployment practices that do not formally preserve prior routing state as modifiable governed substrate content.

## 4. Inherited Paper 1 commitments

Routing adaptation per B2.04 carries all Paper 1 architectural commitments as inherited references. Six are directly load-bearing for this note.

**B2.04 (routing patterns specification)** is the parent of routing adaptation. B2.04 formalizes the reasoning layer's ability to route around bad instinct as an architectural commitment. B2.64 operationalizes B2.04 for the mutation-event scenario: the routing patterns specification is what makes routing adaptation a governed operation rather than an ad hoc implementation practice.

**A2.04 (rule authoring)** is the mechanism through which routing rule changes are enacted. Every routing adaptation — whether complete transition, gradual addition of cell types, FAIL-triggered maintenance, or return to uniform — is realized through routing rules authored per A2.04. The authoring constraint is not procedural; it is architectural: routing rules take effect as substrate content only through the authoring mechanism A2.04 specifies.

**A2.46 (Category 4 authoritative content)** establishes that routing rules are substrate-resident authoritative content. Routing rules are not runtime configuration, deployment tooling configuration, or implementation details; they are Category 4 content in the substrate's authority architecture. This classification is what makes routing adaptation a governance event rather than an engineering change.

**A2.40 (six provenance metadata fields)** establishes that routing rule changes are recorded with full provenance. Each routing adaptation event — which cell types were rerouted, from which version, to which version, by whom, under what verification outcome, at what time — is recorded per A2.40's six fields. The provenance record is what makes routing adaptation auditable and what supports the retroactivity commitment below.

**A1.01 (governance)** establishes that humans hold the authority over substrate content and orchestration rules at all times. Routing adaptation inherits this commitment directly: the routing rules that determine which LLM version cells consult are substrate content under human authority per A1.01. Governance is not limited to the authoring moment; humans retain the right to inspect, modify, and override routing rules at any time.

**A6.02 (retroactivity)** establishes that prior substrate states are preserved in history. For routing adaptation, retroactivity means that the prior routing rules — the routing state before any mutation-triggered adaptation — remain addressable after the adaptation is complete. This preserved history supports reversion (governance can restore prior routing rules) and audit (governance can reconstruct the sequence of routing states through which the deployment transitioned).

## 5. Routing patterns and their triggers

The five routing patterns defined in §2 are not governance options of equal standing in all circumstances. Each has a specific trigger based on verification outcome and governance judgment.

A full PASS outcome per B2.63 opens two patterns: complete transition routing and gradual transition routing. The choice between them is a governance decision about risk appetite. A deployment with high confidence in the verification coverage's completeness — because the verification substrate's test cases cover the deployment's full behavioral surface — may elect complete transition. A deployment that acknowledges residual risk in the gap between verification coverage and production behavior will typically elect gradual transition as the default, regardless of the verification outcome.

A PARTIAL outcome per B2.63 opens gradual transition routing for cell types with passing test cases and routing around bad instinct for cell types with failing test cases. The partial outcome is the natural trigger for split routing: the deployment enters a state where different cell types are managed differently, with the split determined not by arbitrary staging but by the verification substrate's specific findings. Governance authors routing rules for each cell type based on whether its relevant test cases passed or failed.

A FAIL outcome per B2.63 triggers routing around bad instinct for all affected cells. The new LLM version is blocked from cell access by routing rule maintenance. This is not a passive state — it is a governed outcome in which routing rules are explicitly maintained at the current version, with that maintenance recorded per A2.40 as a routing governance event.

Return to uniform is not triggered by a verification outcome; it is triggered by the completion of a transition. When all cell types have been successfully rerouted to the new LLM version and operational experience has confirmed the transition, governance authors routing rules that remove the prior version references and re-establish uniform routing state.

Within the gradual transition and split routing patterns, high-stakes cells per B2.05 — cells whose decisions are architecturally pinned to the reasoning layer because of their operational significance — complete the transition after non-high-stakes cells. The ordering is deliberate: non-high-stakes cells provide production evidence for the new LLM version's behavior before high-stakes cells are exposed to it. This ordering is itself a governance decision implemented through routing rule sequencing.

## 6. Operational implications

Several operational properties follow from routing adaptation as formalized above.

Routing adaptation enables controlled LLM version transitions. Because routing rules determine which version cells consult and those rules change only through governed authoring events, no cell is exposed to a new LLM version without a routing rule explicitly directing it there. The transition is not a background capability upgrade that propagates automatically; it is a sequence of governed routing events.

Gradual transition reduces mutation integration risk. By limiting initial exposure to a subset of cell types, governance accumulates production evidence before committing the full deployment to the new version. The gradual pattern is available independently of whether the verification substrate produced a full PASS or a PARTIAL outcome; governance may elect gradual transition even for well-verified mutations as a matter of operational prudence.

Split routing enables partial mutation integration. A deployment that reaches a PARTIAL verification outcome is not forced to choose between full adoption and full rejection of the new LLM version. Split routing allows the deployment to extract the capability gains the new version provides for cell types where it verified correctly, while protecting cell types where it did not. This granularity is architecturally unavailable in uniform-update deployment models.

Deployments may maintain multiple LLM version routing rules during transition periods. The routing substrate during a gradual transition or split routing state references multiple LLM versions concurrently. This is not a transient anomaly to be minimized; it is a governed operational state with explicit routing rules specifying the assignment of cell types to versions. The routing substrate's provenance record per A2.40 tracks when each version entered the routing rules and when it was retired.

Routing adaptation integrates with verification results from B2.63 as described in §5, but it does not replace the governance decision. Verification outcomes are inputs to governance; governance decisions are implemented through routing rule changes. No verification outcome automatically triggers a routing change; each routing change is a governance event requiring explicit authorization per A2.04.

Routing adaptation works with pinning per B2.65 as a complementary instrument. Pinning — the subject of B2.65 — specifies which decisions bypass the LLM entirely, regardless of which version routing would otherwise direct cells to consult. Routing and pinning address different aspects of mutation governance: routing determines which LLM version cells consult when they do consult the LLM; pinning determines which decisions do not consult the LLM at all. A high-stakes cell may simultaneously be subject to routing rules specifying which version it consults (routing) and to pinning rules specifying which of its decisions must reach the reasoning layer regardless of LLM output (pinning). The two instruments are composable and non-redundant.

Cross-partner routing per A2.47 requires cross-partner authority when routing adaptation affects shared LLM access. In multi-partner deployments where a shared LLM instance is accessed by cells across partner boundaries, routing rule changes that affect which version the shared instance serves require the authority of all partners with access, not unilateral authority from one partner's governance. The routing adaptation mechanism does not override the cross-partner authority constraint.

## 7. Limits of routing adaptation

Routing adaptation is a powerful operational instrument. Its limits are equally important to state precisely.

**Routing adaptation does not directly change LLM versions.** Routing rules specify which version cells are directed to consult; they do not change what the LLM vendor has deployed. If a vendor retires a prior version from availability, routing rules that direct cells to that version cannot preserve access to it regardless of their content. Routing adaptation is the deployment's control mechanism over which version cells consult; it presupposes that the version it specifies remains available.

**Routing adaptation does not prevent LLM from changing.** Mutation events per B2.61 arrive from upstream without the deployment's authorship or approval. Routing adaptation is the governed response to mutation events; it is not a mechanism for preventing them. A vendor that silently replaces one version with another — without the detection mechanism per B2.62 being triggered — is outside routing adaptation's scope.

**Routing adaptation is substrate content, not a runtime guarantee.** Routing rules are inspectable and auditable per A2.01. Their being substrate content is what makes them governed; it also means that any human with appropriate authority per A1.01 can modify them. Routing rules do not provide a runtime enforcement mechanism that is independent of the substrate's governance architecture.

**Routing adaptation is not the same as pinning per B2.65.** Routing adaptation specifies which LLM version cells consult when they consult the LLM. Pinning specifies which decisions bypass the LLM entirely. These are distinct operations: routing adaptation does not protect against bad instinct from a version the cell is routed to, only against exposure to a version that has not been authorized. Pinning addresses the case where no LLM version should influence a particular decision. Neither instrument substitutes for the other.

**Routing adaptation does not guarantee behavior stability.** After a routing adaptation routes cells to a new LLM version following a verification PASS, the new version may still produce unexpected behavior in production. Verification substrates provide operational assurance, not epistemic certainty; the behavioral surface covered by verification test cases is necessarily smaller than the full behavioral surface encountered in production. Routing adaptation implements the governance decision informed by verification; it does not eliminate the residual risk that the verification coverage was incomplete.

**Routing adaptation is reversible.** If a new LLM version proves problematic in production after routing adaptation has been completed, routing rules can be authored per A2.04 to direct cells back to the prior version — provided the prior version remains available from the vendor. Reversal is a routing governance event of the same type as the original adaptation and carries the same authoring, recording, and retroactivity properties.

## 8. Operational test

A CKS deployment instantiates routing adaptation per B2.04 if and only if: when a mutation event per B2.61 occurs and produces a verification outcome per B2.63, the routing rules specifying which LLM version each cell type consults are updated through governed authoring per A2.04 in a manner that reflects the verification outcome — routing cells to the new version after PASS, maintaining the prior version after FAIL, and enabling split routing across versions after PARTIAL — with each routing change recorded with provenance per A2.40 and preserved retroactively per A6.02, and with routing rules remaining subject to human authority per A1.01 at all times, including after transition.

## 9. Why naming this adaptation as standalone matters

Routing adaptation per B2.04 could in principle be treated as implicit in the mutation governance discussion of B1.13 and the routing patterns specification of B2.04. The case for standalone formalization is that implicit treatment would leave five architecturally distinct design decisions — the five routing patterns enumerated in §2 — without named prior-art status. A party seeking to patent cell-type-specific LLM version management, split routing across concurrent LLM versions, high-stakes-last transition ordering, PARTIAL-outcome-triggered split routing, or routing rule reversibility as preserving reversion paths would find no named prior art in the implicit treatment. Standalone formalization places each of these decisions explicitly in the prior-art record.

The note occupies the fourth position in the six-note decomposition of B1.13:

- **B2.61** established the mutation event as the entry of a new LLM version from upstream.
- **B2.62** established mutation detection as the operational identification of that entry.
- **B2.63** established verification gate triggering as the conditions under which the verification substrate engages and the outcomes it produces.
- **B2.64** (this note) formalizes routing adaptation as the mechanism that converts verification outcomes into governed routing rule changes.
- **B2.65** (next) will formalize pinning enforcement as the complementary mutation governance instrument specifying which decisions bypass LLM influence entirely.
- **B2.66** will formalize mutation governance verification as the closing coordination of the B1.13 decomposition.

After B2.66, subsequent Phase B2 notes will decompose B1.14 directed selection through B2.67 and beyond. The B1.13 decomposition — six notes accounting for mutation event, detection, verification gate, routing adaptation, pinning enforcement, and governance verification — establishes the full operational architecture of mutation governance as prior art, protecting the field from fragmented claims against individual mechanisms that are jointly specified by the decomposition as a whole.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Routing Adaptation per B2.04 — Decomposing B1.13 Mutation as Instinct Evolution by Formalizing How Routing Rules per B2.04 Adapt in Response to Mutation Events Following Verification per B2.63, Including Gradual and Complete Transition Routing, Split Routing Across LLM Versions During Transition, and Routing Return to Uniform Post-Integration.* May 12, 2026. ORCID: 0009-0004-8065-3235.
