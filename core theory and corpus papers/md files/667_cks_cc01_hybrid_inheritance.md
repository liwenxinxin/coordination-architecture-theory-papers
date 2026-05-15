# P3↔P1 Hybrid Commitment Inheritance

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026). It does not introduce new axioms. Its contribution is to make explicit the inheritance edge connecting Paper 3's exchange bounding commitment and its use of a shared substrate as an inter-Self coordination spine to Paper 1's foundational hybrid commitment — that coordination governance belongs outside the model, in a human-governed substrate, not inside the LLM.

---

## Abstract

Paper 1 established the hybrid commitment: coordination governance is placed in a persistent, human-governed substrate outside the LLM rather than inside model weights, inference context, or runtime middleware. The substrate is the authoritative coordination state; the LLM operates as a substrate mediator under governance-authored orchestration rules. Paper 3 extends this commitment to the inter-Self scope through two architectural moves: the shared substrate as the outside-the-model inter-Self coordination spine, and exchange bounding as the mechanism that enforces the hybrid commitment at the inter-Self perimeter. This note formalizes the inheritance edge. The architectural principle is identical across Papers 1 and 3; what changes is the scope at which it applies.

---

## 1. Cross-Paper Inheritance Identification

Paper 3's inter-Self architecture rests on two commitments that are not independent of Paper 1. The first is that the medium of inter-Self coordination is a shared substrate — itself a CKS substrate, constructed temporarily for an interaction, with all six Paper 1 commitments holding within scope and a governance perimeter that spans more than one organization's home boundary. The second is that what crosses the inter-Self perimeter is bounded to substrate content: DNA-layer and action-layer content exchange across the shared substrate; LLM weights and instinct-layer content do not.

Both commitments are expressions of a single architectural principle Paper 1 established at cell scope: that coordination governance belongs outside the model. Paper 1 drew this as the hybrid commitment — the substrate handles coordination, governance, and conflict-handling; the LLM handles high-dimensional reasoning; the division is drawn at the governance boundary, not the capability boundary. Paper 3 does not introduce a new principle when it builds the shared substrate as an outside-the-model inter-Self coordination spine or when it enforces exchange bounding at the perimeter. It applies Paper 1's principle to a larger scope.

The inheritance edge this note formalizes: Paper 3's shared-substrate-as-inter-Self-coordination-spine and exchange bounding commitment are direct extensions of Paper 1's hybrid commitment to inter-Self scope. Paper 2's instinct/reasoning separation supplies the vocabulary that makes exchange bounding precise (the instinct layer is what must not cross; the reasoning layer is what may), but the governing architectural principle is Paper 1's.

---

## 2. Source Commitment at Original Scope

Paper 1 introduced the hybrid commitment as the foundational architectural move of the CKS pattern. The commitment has two sides: what belongs outside the model and what belongs inside it. Outside the model, in the human-governed substrate, belongs coordination state, governance semantics, conflict records, and orchestration rules — everything whose authoritative status depends on human authority rather than on LLM inference. Inside the model, in the LLM, belongs high-dimensional reasoning — everything whose value comes from the model's learned capabilities rather than from human governance. The division is architectural, not incidental: it is drawn at the governance boundary rather than the capability boundary, which means that even as LLM capability increases, the things that require human authority remain in the substrate, not because the LLM could not in principle handle them, but because governance requires that they be inspectable, modifiable, and overrideable by humans at any time.

The substrate, not the LLM, is the authoritative coordination state. When a cell executes, it reads from and writes to the substrate under governance-authored orchestration rules. The LLM's output is input to the substrate; it is not itself the coordination record. This is what makes the CKS pattern human-governable at scale: the authoritative state lives where humans can reach it.

At intra-Self scope — the scope Paper 1 defends — the hybrid commitment means that each cell's coordination is governed by its substrate content, not by what the LLM "knows." The LLM has no privileged role as a coordination authority. Its inference outputs matter precisely because they flow into the substrate, where they become part of the authoritative record subject to human governance. The hybrid commitment is what prevents the pattern from collapsing into one in which the model is the system and governance is an afterthought.

---

## 3. Extension to Inter-Self Scope

Paper 3 faces an architectural question Paper 1 did not need to answer: how do distinct organizations' AI systems coordinate with each other in a way that preserves human governance? The natural foil — the dominant pattern in 2024–2026 multi-agent and inter-agent systems — is what Paper 3 calls opaque agent-to-agent communication: inter-AI exchange conducted through message passing, untyped state transfers, tool calls, or shared LLM context windows whose substantive content is not first-class human-governed substrate. This foil is, precisely, an inside-the-model approach to inter-AI coordination: the coordination medium is LLM context, API payloads, or message queues, not governed substrate content. The foil is not simply less governed than the CKS alternative; it is architecturally different in the same way that an LLM-as-authoritative-state-store is architecturally different from the CKS hybrid at cell scope.

Paper 3's response to this question is the hybrid commitment applied at inter-Self scope. The shared substrate is the outside-the-model inter-Self coordination spine: the medium of inter-Self coordination is itself a CKS substrate, with governance perimeter spanning more than one home boundary and all six Paper 1 commitments holding within scope. Inter-Self coordination, governance, and conflict-handling live in the shared substrate outside any single LLM. The shared substrate's content is human-governed substrate content from the start — not a governed wrapper around an opaque exchange, but a governed exchange medium.

Exchange bounding is how the hybrid commitment is enforced at the inter-Self perimeter specifically. Per Paper 2's instinct/reasoning separation, every CKS-governed AI Self has two layers: the instinct layer (the LLM, carrying fast-pattern behavior) and the reasoning layer (the CKS substrate, carrying governed, explicit, human-authored coordination content). When two Selves coordinate through a shared substrate, only reasoning-layer content may cross the inter-Self perimeter. LLM weights and instinct-layer content do not exchange. This boundary is not a restriction that Paper 3 adds to the hybrid commitment; it is the hybrid commitment's natural expression at the inter-Self perimeter. The hybrid commitment says that coordination governance belongs outside the model. At the inter-Self boundary, that means what crosses must be outside-the-model content — substrate content — not inside-the-model content, such as weights, latent representations, or model-internal context windows. Exchange bounding is the inter-Self scope operationalization of the hybrid commitment, not a new principle layered on top of it.

---

## 4. What Is Preserved vs. What Is Extended

**What is preserved.** The fundamental architectural commitment is identical in Papers 1 and 3: coordination governance belongs outside the model, in the human-governed substrate, not inside LLM weights, inference, or runtime context. The LLM operates as a substrate mediator under governance-authored orchestration rules. The substrate, not the LLM, is the authoritative coordination state. Human governance holds authority over the substrate. These properties hold without modification at intra-Self scope (Paper 1) and at inter-Self scope (Paper 3). The outside-the-model vs. inside-the-model spine that organizes Paper 1 runs through Papers 2 and 3 unchanged.

**What is extended.** The scope of application is extended: from individual cells within a single organization's system (Paper 1) to coordination across multiple organizations' systems (Paper 3). The specific operationalization is extended: at intra-Self scope, the hybrid commitment is expressed as the substrate/LLM division within each cell, with the substrate as the authoritative coordination state and the LLM's outputs as substrate inputs. At inter-Self scope, the hybrid commitment must also address what crosses the organizational boundary. Exchange bounding is Paper 3's inter-Self scope operationalization of this question: substrate content (outside the model) may cross; instinct-layer content (inside the model) may not. This is not a new principle — it is the same hybrid commitment, now specifying the inter-Self perimeter as an additional location where inside vs. outside the model matters. The shared substrate itself is also new at Paper 3's scope: it is a new architectural object, temporarily constructed with a perimeter spanning multiple home boundaries, but its internal architecture is governed by Paper 1's six commitments without modification.

---

## 5. Prior-Art Inheritance Claim

Paper 3's exchange bounding commitment and its use of the shared substrate as an outside-the-model inter-Self coordination spine are direct extensions of Paper 1's hybrid commitment to inter-Self scope. The architectural principle — coordination governance belongs outside the model, in a human-governed substrate, not inside LLM inference or context — is Paper 1's. Paper 3 applies it at a larger scope.

Any adversarial claim that placing inter-organizational AI coordination governance outside the model — in a shared substrate rather than in LLM mechanisms, shared context windows, or ungoverned message-passing protocols — is a novel architectural invention must address that this is precisely Paper 1's hybrid commitment applied one scope level outward. The principle existed. The inter-Self scope application is what Paper 3 contributes.

Similarly, any claim that bounding what may cross an inter-organizational AI perimeter to substrate content (excluding LLM weights and instinct-layer content) is novel must address that this is the hybrid commitment's natural expression at a perimeter where inside vs. outside the model must be specified at the exchange boundary. Exchange bounding is not an additional commitment; it is what the hybrid commitment requires when the relevant boundary is between organizations rather than between a substrate and an LLM within one cell.

The prior-art chain is explicit. Paper 1 established the hybrid commitment at cell scope. Paper 2 extended it to Self scope as the instinct/reasoning separation. Paper 3 extends it to inter-Self scope as the shared-substrate-as-coordination-spine and exchange bounding. Each extension changes the scope; none changes the principle. The principle is Paper 1's prior art.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *P3↔P1 Hybrid Commitment Inheritance.* May 15, 2026. ORCID: 0009-0004-8065-3235.
