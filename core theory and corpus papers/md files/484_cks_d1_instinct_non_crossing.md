# Instinct-Evolution Non-Crossing as Active Architectural Commitment

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note ID:** D1.19 (#484)
**Derivation parent:** D0.04 — Paper 3 Claim 4 (Four-locus evolution-feed mechanism)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3's Claim 4 specifies that instinct evolution takes no FAI input — LLM weights and instinct-layer content do not exchange across Full Aspect Integration events. This note formalizes the instinct-evolution non-crossing as an **active architectural commitment**, not a default or technical limitation. Two classes of content are excluded: parametric LLM weights (which are not substrate content and live inside the model) and instinct-layer harness substrates (which are authored substrate content but govern each Self's instinct behavior within its home perimeter). Three reasons independently require the non-crossing: the outside-the-model spine established by Paper 1, the instinct/reasoning separation established by Paper 2, and the home governance sovereignty that both papers defend at their respective scopes. The note distinguishes D1.19 from its companion D1.10: where D1.10 established what is within FAI exchange bounds (DNA-layer and action-layer content), D1.19 formalizes the explicit non-crossing of the excluded classes as a positive design commitment that a conforming architecture must enforce. Four failure modes the commitment defends against are named, and an operational test is provided.

---

## 1. The commitment stated precisely

D1.19 states: **In any conforming FAI implementation, LLM weights and instinct-layer content are architecturally committed to not crossing the inter-Self perimeter; this non-crossing is an active design decision required by three independently sufficient architectural reasons, not an absence of capability or a feature deferred for future implementation.**

The distinction between active commitment and passive absence is load-bearing. A claim that "FAI does not happen to include weight exchange in its current specification" leaves open that future versions could add weight exchange as an extension. D1.19 closes that opening: the non-crossing is not a gap in the specification but a property the specification positively requires. An architecture that introduced LLM weight exchange at the inter-Self perimeter — even wrapped in governance — would not be implementing Paper 3's architecture; it would be implementing something architecturally different, because it would contradict at least one of the three reasons that make the non-crossing commitment necessary.

This note is the second half of a two-part pair with D1.10. D1.10 established what **is** within FAI exchange bounds: the unit of exchange is the aspect from Paper 2, and the exchange is bounded to DNA-layer content (orchestration substrates, behavior substrates, schemas, rules) and action-layer content (recorded task instances, outputs, lived experience). D1.19 establishes what **is not** and why — not as the logical inverse of D1.10 but as its own positive commitment. D1.10 asks: what may cross? D1.19 asks: what is committed to not crossing, and on what grounds? Both sides of the pair are necessary for a complete account of FAI's exchange bounding.

---

## 2. What does not cross: two classes

**Class 1 — LLM weights.** Parametric model weights are the numerical parameters that govern a Self's LLM execution behavior: the values that determine how the model responds to any given input context. LLM weights are not substrate content. Paper 1 draws the substrate/LLM division at the governance boundary, not the capability boundary: the substrate carries what humans govern (coordination, rationale, authority policies, conflict state), while the LLM carries fast-pattern instinct behavior that humans cannot and need not encode directly. LLM weights live inside the LLM — they are part of the tool-agnostic host layer that Paper 1 treats as infrastructure. They are not authored by governance as substrate content; they are not structured representations under the three human governance rights (inspect, modify, override at any time). Because LLM weights are not substrate content, they are not candidates for FAI exchange in the first place: FAI exchanges substrate content, and weights are not substrate content. The non-crossing is architecturally upstream of any question about governance configuration.

**Class 2 — Instinct-layer content (harness substrates).** Instinct-layer content — the explicitly authored specifications that govern each Self's fast-pattern instinct behavior within its home LLM — is a different case. Unlike LLM weights, harness substrates are authored substrate content; they are written by humans and are subject to the three governance rights. They are legitimate substrate content within the home perimeter. Their exclusion from FAI exchange therefore cannot rest on the same ground as LLM weight exclusion. The reason harness substrates do not cross is that they govern each Self's instinct behavior *under its home perimeter and within its home LLM*. They are home-perimeter content: their scope of authority, their governance structure, and their meaning are all indexed to the home perimeter. Transferring harness substrates across the inter-Self perimeter would not merely be moving substrate content — it would be moving instinct-governance authority from one Self's home perimeter into another Self's inter-Self exchange channel, which the instinct/reasoning separation (Paper 2 Claim 1) commits to preventing at every scope.

Both classes are excluded, but for architecturally distinct reasons: LLM weights because they are not substrate content at all; instinct-layer content because it is home-perimeter substrate content that governs through the home LLM and may not cross without dissolving the instinct/reasoning separation.

---

## 3. Three reasons the non-crossing is architecturally necessary

The following three reasons are each independently sufficient. No one of them requires the others to justify the commitment. Together they make the non-crossing architecturally load-bearing across the full trilogy.

### Reason 1 — The outside-the-model spine (Paper 1)

Paper 1's foundational commitment is that all authoritative coordination lives outside the LLM in human-governed substrate. The substrate/LLM division is drawn at the governance boundary: what humans govern lives in the substrate; what the LLM carries is infrastructure. This is the architectural spine that runs through all three papers.

Allowing LLM weight exchange at the inter-Self perimeter would directly violate this commitment. LLM weights carry authoritative behavioral state: they determine how the Self responds to any input. If FAI events could exchange weights, then the authoritative state governing a Self's behavior would be originating from outside the receiving Self's substrate — from another Self's LLM, which is inside the model. The coordination object would have moved inside the model. Paper 1's commitment is not that authoritative coordination *prefers* to live in substrate but that it must: the architecture's value comes from the principled separation. Introducing weight exchange at inter-Self scope would dissolve that separation at the inter-Self boundary.

This reason applies to LLM weights directly. It applies to instinct-layer content indirectly: harness substrates govern through the LLM, and transferring them without perimeter boundary would create a vector for cross-perimeter influence over LLM behavior that the outside-the-model spine commits to keeping within each Self's home perimeter.

### Reason 2 — The instinct/reasoning separation (Paper 2)

Paper 2 Claim 1 commits to the instinct layer being separately governed within each Self's home perimeter. The instinct layer is the LLM, operating as a System-1 fast-pattern analogue. The reasoning layer is the CKS substrate, operating as a System-2 deliberate analogue. The separation is not merely structural — it is a governance commitment: each layer evolves through distinct mechanisms under per-mechanism governance shapes, and human authority over each layer is maintained through distinct substrate machinery. The instinct/reasoning separation is what makes each Self an architecturally coherent unit under unified human governance.

Allowing instinct-layer transfer across the inter-Self perimeter would dissolve the governance boundary that Paper 2 commits to maintaining. If a Self's harness substrates could be transferred to or from a shared substrate, the receiving Self's instinct behavior would be governed by content that originated under a different perimeter's governance authority — content that the receiving Self's human governance did not author, did not approve through the receiving Self's per-mechanism governance machinery, and cannot cleanly locate within the receiving Self's instinct/reasoning architecture. The separation between layers would not merely be stretched; it would be violated at the inter-Self boundary.

Instinct evolution within each Self continues through the mechanisms Paper 2 specifies — LLM upgrades and substrate-platform infrastructure changes — independently of FAI events. This independence is a feature, not a constraint: it ensures that instinct evolution remains under each Self's home governance without inter-Self interference.

### Reason 3 — Home governance sovereignty

Both LLM weight exchange and instinct-layer transfer share a third defect that is independent of the first two reasons: they would give participating Selves influence over each other's instinct behavior from outside the receiving Self's substrate governance.

Paper 2's governance architecture assigns distinct per-mechanism governance shapes to each evolution mechanism. For instinct evolution specifically, the mechanism requires verification-substrate machinery that operates under home governance — changes to instinct behavior require the receiving Self's human governance to authorize them through the appropriate machinery. This authority structure is not transferable through substrate exchange: it depends on home governance exercising authority within the home perimeter.

If LLM weights or instinct-layer content could enter a Self through FAI exchange, that entering content would influence the receiving Self's instinct behavior without passing through the receiving Self's home governance machinery for instinct evolution. The influence would arrive inside the model (in the case of weight transfer) or inside the harness content governing the model (in the case of instinct-layer transfer), bypassing the governance layer that Paper 1 and Paper 2 jointly commit to keeping authoritative. The receiving Self's human governance would not have exercised the authority over instinct behavior that the architecture reserves for it.

Home governance sovereignty is the governance-facing articulation of what the outside-the-model spine and the instinct/reasoning separation require at the human-authority level: the three governance rights (inspect, modify, override) over each Self's instinct-governing content must remain within each Self's home perimeter, and no inter-Self exchange may create a vector that bypasses them.

---

## 4. The D1.10/D1.19 pair as complementary bounding

D1.10 and D1.19 together constitute the complete exchange-bounding account for FAI. Neither note is sufficient alone.

D1.10 established the positive bounds: the unit of exchange is the aspect from Paper 2, and exchange is bounded to DNA-layer and action-layer substrate content. This is the permissive side of the bound — what a conforming implementation may include in shared-substrate exchange.

D1.19 establishes the negative commitment: LLM weights and instinct-layer content are architecturally excluded from exchange, and this exclusion is a positive design requirement, not a silence in the specification. This is the restrictive side of the bound — what a conforming implementation must not include.

The pair structure matters because the two notes answer different questions about potential extension. A reader of D1.10 alone might ask: can the bounds be widened in a future variant by including additional content types? D1.10 does not answer that question. D1.19 answers it for the two excluded classes: the bounds cannot be widened to include LLM weights or instinct-layer content without producing a different architecture, because the exclusion is required by three independent reasons that are part of the trilogy's foundational commitments. Any future variant that adds weight or instinct-layer exchange is, by that fact, not a variant of Paper 3's architecture but a different design.

The pair also maps cleanly onto Paper 2's layer structure. Paper 2 distinguishes three substrate-adjacent layers within each Self: the DNA layer (orchestration substrates, behavior substrates, schemas, rules — the Self's governed logic), the action layer (recorded task instances, outputs, lived experience — the Self's governed record), and the instinct layer (the LLM and its governing harness substrates — the Self's fast-pattern system). D1.10 says: DNA and action layers exchange through FAI. D1.19 says: the instinct layer and the model infrastructure that hosts it do not. The D1.10/D1.19 pair is the inter-Self extension of Paper 2's layer structure.

---

## 5. Failure modes the commitment defends against

The instinct-evolution non-crossing commitment defends against four categories of architectural failure or mischaracterization.

**Failure mode 1 — Model weight transfer as FAI evolution mechanism.** A design that allows participating Selves to exchange LLM weights through or alongside the shared substrate — treating weight parameters as a class of substrate content available for integration — violates the outside-the-model spine directly. No governance wrapping makes this conforming: the defect is structural, not procedural. The weights would carry authoritative behavioral state from outside the receiving Self's substrate, contradicting Paper 1's foundational commitment regardless of how carefully the exchange is administered.

**Failure mode 2 — Instinct-layer transfer as FAI evolution mechanism.** A design that allows harness substrates governing each Self's instinct behavior to be contributed to or drawn from the shared substrate violates the instinct/reasoning separation at inter-Self scope. The defect is not that harness substrates are illegitimate substrate content (they are) but that transferring home-perimeter instinct-governance content across the inter-Self perimeter dissolves the home-perimeter boundary for instinct governance that Paper 2 commits to maintaining.

**Failure mode 3 — "FAI-plus-weights" architectures.** A design that adopts the FAI framework for DNA-layer and action-layer exchange but adds a parallel weight-exchange channel alongside it — treating FAI as the substrate-exchange component of a hybrid evolution architecture that also exchanges weights — is not a superset of Paper 3's architecture. It is a different architecture. The non-crossing is not a module within Paper 3's architecture that can be swapped out or supplemented; it is a constraint that the entire architecture rests on. Framing weight exchange as an "extension" of FAI misrepresents the relationship.

**Failure mode 4 — Technical-limitation framing.** Characterizing the non-crossing as a current technical limitation — that LLM weights are not yet efficiently transferable, or that instinct-layer transfer is practically difficult — misrepresents the commitment as an empirical observation about present capability rather than an architectural design decision. The non-crossing is not waiting for the technology to catch up. It is a property that a conforming architecture must maintain regardless of what becomes technically feasible. If LLM weight transfer becomes straightforwardly easy, a conforming implementation of Paper 3's architecture still does not do it, because the three reasons that require the non-crossing are architectural, not technological.

---

## 6. Operational test

For any claimed implementation of FAI, the instinct-evolution non-crossing commitment is satisfied if and only if all of the following are verifiable:

1. The shared substrate constructed for each FAI event contains no LLM weight representations from any participating Self — no numerical parameters, no compressed weight snapshots, no weight-derived encodings intended to influence another Self's model behavior.

2. The shared substrate contains no instinct-layer harness substrate content from any participating Self — no authored specifications that govern fast-pattern instinct behavior within a participating Self's home LLM.

3. The governance configuration of the FAI event explicitly specifies that LLM weights and instinct-layer content are outside the sharing scope, and this specification is itself substrate content under human authority, inspectable by any human with appropriate access.

4. The excluded content remains available to each Self for home-perimeter instinct evolution operating through Paper 2's mechanisms (LLM upgrades, substrate-platform infrastructure changes) and is not affected by the FAI event — instinct evolution proceeds per home governance independently of the FAI outcome.

5. The governance configuration satisfying (3) cannot be modified by AI action alone: modification requires human authority exercised within the home perimeter, consistent with the governance-rights requirements each paper establishes.

A claimed FAI implementation that fails any of (1)–(5) is not conforming to D1.19. A failure at (1) or (2) is a direct non-crossing violation. A failure at (3) indicates the non-crossing is treated as a default rather than a governed commitment. A failure at (4) indicates instinct evolution has been coupled to inter-Self exchange in a way that violates its independence. A failure at (5) indicates the governance configuration itself is not under adequate human authority.

---

## 7. Conclusion

The instinct-evolution non-crossing commitment is one of Paper 3's foundational constraints on FAI evolution architecture. It excludes two classes of content — LLM weights and instinct-layer harness substrates — from inter-Self exchange, and it does so by positive architectural design, not by default or omission. Three independent reasons require the exclusion: the outside-the-model spine that Paper 1 establishes at cell scope and carries forward through both extensions; the instinct/reasoning separation that Paper 2 establishes as the governance boundary between each Self's fast-pattern and deliberate layers; and the home governance sovereignty that both papers jointly require over each Self's instinct-governing machinery. Any one of these reasons is sufficient; together they make the non-crossing load-bearing throughout the trilogy.

D1.10 and D1.19 together complete the FAI exchange-bounding account. D1.10 states what the exchange includes; D1.19 states what it is committed to excluding and why. Neither is reducible to the other, and both are necessary for a complete picture of how FAI respects the trilogy's architectural spine while enabling substrate-layer evolution across organizational boundaries.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Instinct-Evolution Non-Crossing as Active Architectural Commitment.* Derivation Note D1.19 (#484), CKS Derivation Series. May 14, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
