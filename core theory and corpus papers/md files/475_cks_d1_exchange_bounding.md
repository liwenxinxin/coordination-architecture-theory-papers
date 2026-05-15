# FAI Exchange Bounded to DNA-Layer and Action-Layer Content

**Series D Derivation Note — D1.10 (#475)**
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI) is the canonical operation over the shared substrate in the CKS trilogy's third paper. This note formalizes one of FAI's foundational sub-commitments: the exchange is bounded to substrate content — specifically to the DNA-layer content and action-layer content of contributed aspects. LLM weights and instinct-layer content are explicitly excluded from the exchange. The note states what is within bounds and what is outside bounds, with concrete examples for each category; explains why this bounding preserves the trilogy's outside-the-model architectural spine at inter-Self scope; articulates the connection to Paper 2's instinct/reasoning separation; addresses the common misreading that frames FAI as a form of training data sharing or model weight exchange; identifies four failure modes the sub-commitment defends against; and provides an operational test for verifying exchange bounding in a given FAI event.

---

## 1. Why the bounding needs explicit statement

FAI operates over a shared substrate that spans the governance perimeters of two or more Selves. When a Self contributes content to that shared substrate, the architecture must specify what content can cross the inter-Self perimeter and what cannot. Without explicit bounding, the question is open — and an open question at the inter-Self perimeter is an architectural vulnerability, not a design choice.

The trilogy's spine is the outside-the-model commitment introduced in Paper 1: all authoritative coordination lives outside the LLM in governed substrate, not inside the LLM's inference or in model parameters. Paper 2 extends this commitment inward to the Self structure, distinguishing the instinct layer (fast-pattern behavior governed through the LLM) from the reasoning layer (governed through substrate content outside the LLM). Paper 3 extends the commitment outward to the inter-Self scope. For that extension to be coherent, the exchange that occurs at the inter-Self perimeter must respect the same principle: only what is outside the model — substrate content — may cross.

Exchange bounding is what articulates this principle as an architectural commitment at FAI mechanism level. It is not an incidental restriction; it is the mechanism by which FAI inherits and carries the outside-the-model commitment across the new scope Paper 3 introduces.

---

## 2. What is within bounds: DNA-layer content

When a Self contributes an aspect to the shared substrate during an FAI event, the aspect surfaces its constituent cells' DNA-layer content for exchange. DNA-layer content is the authored governance specification that lives in the contributing aspect's DNA layer. It is substrate content — it exists as structured, human-governed records outside the LLM, readable and modifiable by governance authority.

The categories of DNA-layer content within exchange bounds include the following:

**Orchestration rules** — the rules that govern how the contributing aspect's cells operate under governance. These specify routing logic, modification authority, conflict-handling behavior, and the boundaries of what an LLM is authorized to do within the aspect's cells. When contributed to the shared substrate, they make the receiving Selves legible about how the contributing aspect's governance actually works.

**Behavior specifications** — the authored specifications of what the aspect's cells are specified to do. These are the per-cell behavioral contracts that define the aspect's operational scope.

**Coordination rules** — the rules governing how cells within the aspect coordinate with one another. Cross-cell routing, dependency specifications, and sequencing rules fall within this category.

**Content-domain specifications** — the authored governance records defining what operational territory the aspect governs: what is in-domain, what is out-of-domain, and what conditions bound the aspect's scope.

**Other DNA-layer objects specific to the aspect** — any additional authored governance specifications that live in the contributing aspect's DNA layer and are specific to that aspect's governance structure.

All of these are substrate content in the Paper 1 and Paper 2 sense: they are authored by governance, exist as structured records outside the LLM, and are subject to the three governance rights (inspect, modify, override) at all times. They are what the contributing aspect's governance actually consists of. Exchanging them across the inter-Self perimeter via FAI is what makes inter-Self coordination governed rather than opaque.

---

## 3. What is within bounds: action-layer content

The aspect also surfaces its constituent cells' action-layer content for exchange. Action-layer content is the operational record of what the aspect's cells have actually done in operation. It is the lived experience of the contributing aspect as captured in substrate records.

The categories of action-layer content within exchange bounds include the following:

**Operational records** — recorded instances of what the aspect's cells have executed: the tasks they have handled, the decisions they have produced, the outputs they have generated. These are the substrate records accumulated through the aspect's operational history.

**Execution history** — the chronological substrate record of the aspect's activity over time. This is distinct from the behavior specifications in the DNA layer: the DNA layer says what the aspect is specified to do; the action layer records what it has done.

**Evidence that can seed action-feedback evolution in receiving Selves** — operational records carry evidential weight for a receiving Self's evolution mechanisms. When a receiving Self ingests contributed action-layer content through the governance-configured evolution feed (the D0.04 / Claim 4 mechanism), it can use that evidence as input to its own action-feedback evolution, updating its aspect governance based on another Self's accumulated operational experience.

Action-layer content is substrate content by the same logic as DNA-layer content: it exists as structured records outside the LLM, accumulated through governed cell operation, and subject to governance authority. Its value in FAI is different from DNA-layer content's value — it is evidence and experience rather than specification — but it is equally substrate content, and equally within exchange bounds.

---

## 4. What is outside bounds: LLM weights

LLM weights — the underlying model parameters that govern the LLM's behavior within a Self — are not substrate content and are not exchanged in FAI. The distinction is architectural, not incidental.

Substrate content, as established in Paper 1, is content that lives outside the LLM in governed records. LLM weights live inside the LLM: they are the internal parameters of the model that an LLM provider maintains, trains, and deploys. They are not authored by governance as substrate records; they are not subject to the governance rights (inspect, modify, override) in the CKS sense; they are not structured records in a coordination substrate. They are part of the LLM infrastructure — the tool layer that substrate-governed systems use as a resource, not as a coordination substrate.

FAI is an operation over substrate content. It has no access to, no authority over, and no mechanism for exchanging LLM weights. Any architecture in which FAI were construed to exchange model parameters would not be extending the outside-the-model commitment to the inter-Self scope — it would be abandoning it in favor of a model-internal coordination mechanism. That is the opposite of what FAI is.

The exclusion of LLM weights from exchange is therefore not a limitation of FAI; it is a consequence of FAI being a substrate-content operation. The outside-the-model commitment that runs through the trilogy precludes model-weight exchange as an FAI operation by construction.

---

## 5. What is outside bounds: instinct-layer content

Instinct-layer content — the harness substrates that govern each Self's fast-pattern instinct behavior — is also outside exchange bounds in FAI. The reason is distinct from the reason LLM weights are excluded, and requires separate statement because Paper 2's instinct/reasoning separation is the underlying commitment being carried through.

Paper 2 establishes the instinct/reasoning separation as a foundational architectural commitment. The instinct layer governs each Self's fast-pattern behavior: it operates through harness substrates that shape how the LLM responds within the Self's instinct-governed contexts. This layer is within the home perimeter of each Self — it governs behavior within that Self's governance structure, under that Self's governance authority.

The instinct layer is substrate content in a limited sense: its harness substrates are governed records outside the LLM. But its proper scope is the home perimeter of the Self that owns it. It governs that Self's instinct behavior; it is not authored for exchange; and its governance authority belongs to the home Self, not to any inter-Self coordination mechanism.

If instinct-layer content were permitted to cross the inter-Self perimeter via FAI, two problems would follow. First, the instinct/reasoning separation would be broken at inter-Self scope: instinct governance, which Paper 2 commits to keeping within each Self's home perimeter, would become available for export and import across organizational boundaries. Second, the governance authority over the instinct layer would become ambiguous — the receiving Self would hold imported instinct governance that was authored by the contributing Self's governance authority, with no clear mechanism for the receiving Self's governance to authorize it.

FAI forecloses this by architectural commitment: instinct-layer content stays within the Self that owns it, and does not cross the inter-Self perimeter. The exchange bounding at FAI mechanism level is how Paper 2's instinct/reasoning separation is preserved at Paper 3's new scope.

---

## 6. Why this bounding preserves the trilogy's outside-the-model spine

The trilogy's outside-the-model commitment has a precise meaning: authoritative coordination lives in governed substrate records outside the LLM. Paper 1 establishes this at cell scope. Paper 2 extends it to Self scope, with the instinct/reasoning separation as the mechanism for distinguishing what lives in substrate records (reasoning-layer coordination) from what governs through the LLM (instinct-layer behavior). Paper 3 extends it to inter-Self scope, with the shared substrate as the medium of coordination across governance perimeters.

Exchange bounding is what ensures that the extension in Paper 3 actually carries the commitment rather than only resembling it. If FAI exchanged LLM weights, the inter-Self coordination would be grounded in model-internal content — the commitment would be reversed at the new scope. If FAI exchanged instinct-layer content, inter-Self coordination would extend into fast-pattern behavioral governance that belongs within each Self's home perimeter — the instinct/reasoning separation would be broken at the new scope.

By bounding exchange to DNA-layer and action-layer content — the substrate content layers of contributed aspects — FAI ensures that every object that crosses the inter-Self perimeter is: (a) authored by governance, (b) residing in governed substrate outside the LLM, (c) subject to governance rights on both sides of the exchange, and (d) within the scope for which the outside-the-model commitment applies. The exchange is governed coordination, not model exchange.

---

## 7. "Training data sharing" is not what FAI is

A common surface-level misreading maps FAI onto familiar federated-learning or training-data-sharing concepts. The misreading usually takes one of two forms: that FAI is a mechanism for sharing training data between Selves so that receiving Selves can fine-tune their LLMs, or that FAI is a form of model averaging in which LLM weights are aggregated across Selves to produce an improved shared model.

Both readings are architectural misfires. FAI does not touch LLM weights and does not exchange training data. What FAI exchanges is governed substrate content: the orchestration rules that specify how aspects operate, the behavior specifications that define what aspects do, the coordination rules that govern intra-aspect cell behavior, and the operational records that accumulate as aspects execute.

The content exchanged in FAI is not input to model training. It is input to the receiving Self's governance: the receiving Self can ingest contributed aspect content through its governance-configured evolution mechanisms, updating its own governance specifications and operational knowledge based on the contributing Self's experience. This is governance evolution, not model training.

The distinction matters for prior-art positioning. Federated learning (in its various FedAvg-family forms) aggregates at the parameter or gradient level — the instinct layer in trilogy terms. Model fusion merges at full-parameter granularity. These operate entirely within what the trilogy calls the model-internal domain. FAI operates entirely outside it. The conjunction of aspect-level exchange, full-merge default, and layer bounding to the reasoning layer is what occupies the architectural position that federated learning and model fusion do not.

---

## 8. Four failure modes the sub-commitment defends against

**Failure mode 1 — Model weight exchange as an FAI operation.** A construction in which FAI is understood to exchange LLM weights as part of inter-Self coordination. This misreads FAI as a model-sharing mechanism rather than a substrate-content-exchange mechanism. The exchange bounding sub-commitment forecloses this: FAI has no mechanism for accessing or exchanging model weights; weights are outside bounds by construction.

**Failure mode 2 — Instinct-layer transfer as an FAI operation.** A construction in which FAI is understood to exchange instinct-layer harness substrates as part of inter-Self coordination. This would break Paper 2's instinct/reasoning separation at inter-Self scope by permitting instinct governance to cross governance perimeters without the home perimeter's ongoing authority. The exchange bounding sub-commitment forecloses this: instinct-layer content stays within the home perimeter and does not cross the inter-Self boundary via FAI.

**Failure mode 3 — Unbounded exchange.** A construction in which any content present in a contributing Self's architecture is available for exchange across the inter-Self perimeter via FAI — a maximally permissive reading that treats the shared substrate as an unrestricted mirror of each participating Self's internal state. The exchange bounding sub-commitment forecloses this: exchange is bounded to the DNA-layer and action-layer content of contributed aspects. The scope of what crosses the inter-Self perimeter is governed, not unbounded.

**Failure mode 4 — "Training data sharing" framing.** A construction in which FAI is classified as a training data sharing or federated learning mechanism, with the DNA-layer and action-layer content reframed as training examples or gradient signals intended for LLM fine-tuning. This misreads the purpose of the exchange: the content is governed substrate material exchanged for governance evolution, not model inputs exchanged for parameter adjustment. The exchange bounding sub-commitment, read in conjunction with the instinct-layer exclusion, forecloses this: FAI exchanges substrate-layer content that feeds governance evolution; it does not produce model inputs or touch the model-internal domain.

---

## 9. Operational test

For a given FAI event, the exchange bounding sub-commitment is satisfied if and only if an independent observer, examining the shared substrate at any point during or after the event, can verify all of the following:

1. **DNA-layer content present is bounded to contributed aspects.** The shared substrate contains DNA-layer content — orchestration rules, behavior specifications, coordination rules, content-domain specifications — and that content is traceable to the aspects contributed by participating Selves. No DNA-layer content from non-contributing aspects or from outside the contributed aspects' scope is present.

2. **Action-layer content present is bounded to contributed aspects.** The shared substrate contains action-layer content — operational records, execution history — and that content is traceable to the operational history of the aspects contributed by participating Selves.

3. **No LLM weight representations are present.** The shared substrate contains no model parameters, gradient representations, weight matrices, or other content that represents the internal state of any LLM used within a participating Self. No mechanism within the FAI event produced or transported such content.

4. **No instinct-layer harness substrates from contributing Selves are present.** The shared substrate contains no content that is properly classified as the instinct-layer governance of any contributing Self — no harness substrates governing fast-pattern instinct behavior that belong within the home perimeter of any participating Self. Any substrate content that would constitute instinct governance remains within the home perimeter of the Self that owns it.

5. **The exchange is governance-traceable.** Each item of DNA-layer or action-layer content present in the shared substrate is traceable to a specific contributing aspect under a specific contributing Self's governance, with provenance sufficient for the receiving Self's governance authority to evaluate and act on the content.

A shared substrate that fails any of (1) through (5) does not instantiate the exchange bounding sub-commitment. A shared substrate in which (3) or (4) fails does not instantiate the exchange as consistent with the trilogy's outside-the-model commitment.

---

## 10. Conclusion

FAI's exchange bounding to DNA-layer and action-layer content is not a constraint imposed from outside the architecture; it is what FAI is. The outside-the-model commitment that runs through the trilogy as its architectural spine means, at inter-Self scope, that exchange operates over governed substrate content — the records that live outside the LLM, authored by governance, subject to governance authority. DNA-layer and action-layer content of contributed aspects is exactly this. LLM weights and instinct-layer content are not.

The bounding carries two inheritance chains simultaneously. From Paper 1, it carries the outside-the-model principle: substrate content is the medium of coordination; model-internal content is not. From Paper 2, it carries the instinct/reasoning separation: instinct governance belongs within the home perimeter; reasoning-layer governance is what extends across coordination scopes. FAI at inter-Self scope inherits both chains by bounding its exchange to the substrate content that Paper 2's reasoning layer consists of.

What exchanges in FAI is what governance consists of: the authored specifications that define how an aspect operates, and the accumulated operational records that document what it has done. This is not training data. It is not model weights. It is the substance of coordination knowledge itself, made available for inter-Self governance evolution through a governed, bounded, substrate-mediated exchange.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Exchange Bounded to DNA-Layer and Action-Layer Content.* May 14, 2026. ORCID: 0009-0004-8065-3235. CKS Derivation Note D1.10 (#475).
