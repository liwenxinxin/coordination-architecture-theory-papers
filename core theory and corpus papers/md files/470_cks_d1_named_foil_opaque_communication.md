# Opaque Agent-to-Agent Communication as Paper 3's Named Foil

**Series D — Paper 3 Derivation Notes | Note D1.05 | #470**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 names its architectural foil explicitly: opaque agent-to-agent communication, the dominant pattern of inter-AI coordination in 2024–2026 multi-agent systems, conducted through message-passing, tool-calls, or shared-memory access whose substantive content is not human-governable as authored substrate. This note formalizes the foil as prior art. It defines the three foil forms, identifies the "governance retrofitted" failure mode in which governance wrappers are added around an opaque exchange medium without converting that medium into substrate, states four properties that make the shared substrate architecturally distinct from all foil forms, identifies three adversarial equivalence claims the foil formalization forecloses, and provides an operational test for distinguishing substrate-mediated inter-AI coordination from governance-retrofitted coordination. The note closes the five-note Claim 1 sub-commitment set (D1.01–D1.05).

---

## 1. Purpose of this note

D1.05 is the fifth and final note in the Claim 1 sub-commitment set. D1.01 formalized the temporary construction commitment: that the shared substrate is constructed specifically for an inter-Self coordination event and dissolved afterward. D1.02 formalized the six Paper 1 commitments operating within the shared substrate. D1.03 formalized the inter-Self perimeter property: that the shared substrate spans the governance boundary between two or more Selves. D1.04 formalized the persistence policy governing how long the shared substrate persists and what happens to its content at dissolution.

This note addresses the fifth sub-commitment: the named architectural foil. Paper 3 does not merely describe what the shared substrate is; it names what the shared substrate is *not*, and positions itself explicitly against that alternative. Formalizing the foil is prior-art work. It establishes, at a dated publication, the architectural distinction between the shared substrate approach and the foil approaches, and forecloses adversarial claims that governance additions to the foil approaches are equivalent to the shared substrate.

---

## 2. The named foil: opaque agent-to-agent communication

The foil Paper 3 names is the pattern by which most inter-AI coordination is conducted as of 2024–2026: exchange through messages, tool-call payloads, or shared-memory access patterns whose substantive content is not first-class human-governed substrate. Paper 3 calls this **opaque agent-to-agent communication**. It is not a straw man. It describes the architectural posture taken by multi-agent frameworks, inter-agent protocol specifications, and agent orchestration platforms that treat inter-AI coordination as a capability and protocol selection problem, with governance located in deployment wrappers, contract layers, or institutional arrangements outside the exchange medium itself.

The foil takes three structural forms.

### 2.1 Message-passing

AI agents exchange structured or unstructured messages directly. The messages may be formatted, typed, versioned, and logged. What they are not is human-governed substrate content. The rules that determine what content can enter the exchange medium, how conflicts within that content are handled, what authority governs the content, and how the AI's role relative to the content is constrained — none of these are authored substrate under human governance. They are either absent, implicit in the agents' behavior, or specified in framework-level configuration outside the exchange medium. Governance can observe what messages were sent after they were sent. It cannot author the exchange medium itself before exchange occurs.

### 2.2 Tool-calls

AI agents invoke each other's capabilities through API-style calls. The inputs and outputs of those calls may be logged and audited. What they are not is first-class substrate content subject to human governance. The coordination happening through the tool-call exchange — what one agent is asking another to do, on what basis, with what authority, subject to what conflict-handling rules — is not located in a substrate that carries the six Paper 1 commitments. Governance observes call records. It does not govern the exchange medium as authored substrate content.

### 2.3 Shared-memory access

Multiple AI agents read from and write to a shared memory object. The memory contents may be inspectable. What they are not is substrate content governed by the six Paper 1 commitments. The shared memory carries data; it does not carry human-authored orchestration rules, conflict preservation as a first-class property, human governance over the medium's content before and during access, or the AI-as-mediator constraints. Whether the memory is a key-value store, a vector index, a structured document, or a typed schema does not change this: the architectural question is whether the exchange medium is governed substrate content, not what format it takes.

---

## 3. The governance-retrofitted failure mode

The most important foil clarification for prior-art purposes is the failure mode in which governance is added around one of the three foil forms rather than being intrinsic to the exchange medium. This is the **governance-retrofitted** posture: governance is not a property of the exchange medium; it is a layer applied to the medium from outside, after exchange occurs or as a wrapper around the process by which exchange occurs.

Governance-retrofitted approaches include:

- Adding structured logging to message-passing exchanges, so that messages can be reviewed after the fact
- Applying access controls to shared memory, so that not all agents can read all entries
- Auditing tool-call records, so that call patterns can be analyzed after they are generated
- Adding approval gates that human operators can use to review or block certain classes of agent action
- Attaching policy metadata to messages or memory entries, specifying what uses are permitted

None of these converts the exchange medium into governed substrate content. The architectural structure in every case is: exchange occurs through an opaque medium; governance is then applied around, over, or after that medium. The distinction from the shared substrate approach is not that the shared substrate has more governance or better governance. The distinction is where governance is located relative to the exchange: retrofitted governance locates governance outside the exchange medium; substrate-mediated coordination locates governance *within* the exchange medium, because the exchange medium *is* authored substrate content from the start.

This distinction is architectural, not procedural. A retrofitted governance wrapper can be arbitrarily thorough — logging every message, auditing every call, requiring human review of every memory write — without satisfying the shared substrate commitment. Conversely, a substrate-mediated system can operate with very little active human intervention and still satisfy the commitment, because governance is an authority structure over the medium rather than a workflow applied around it.

The pattern that distinguishes retrofitted from intrinsic governance is the temporal and structural order of operations:

- **Governance retrofitted**: exchange medium exists → exchange occurs through the medium → governance is applied to the record or the process
- **Governance intrinsic**: governance authors the exchange medium → the exchange medium carries human-authored orchestration rules and the six Paper 1 commitments → exchange occurs through the governed medium

---

## 4. Four properties that distinguish the shared substrate from the foil

The shared substrate is not merely a better-governed version of the foil approaches. It is architecturally distinct along four dimensions.

**Property 1: The exchange medium is substrate content.** In the shared substrate approach, the exchange medium is not a message channel, a function-call interface, or a memory object external to governance. It is substrate content — the same kind of content the CKS pattern uses within a Self for coordination, governance, and reasoning. Its content is authored substrate content from the moment of construction. The exchange happens through substrate, not around it.

**Property 2: The six Paper 1 commitments hold within the exchange medium.** The foil approaches do not carry the six Paper 1 commitments within the exchange medium. The shared substrate does. Those six commitments — human-governed authority over content, conflict preservation as a first-class property, AI-as-mediator constraints, tool-agnosticism, linear-cost composition, and the substrate-as-coordination-artifact commitment — apply to the shared substrate's content in the same way they apply to each participating Self's home substrate. D1.02 formalizes this inheritance. The point here is the contrast: foil approaches lack this structural inheritance, regardless of what governance wrappers are added around them.

**Property 3: Human governance over the exchange medium precedes and accompanies exchange.** In the shared substrate approach, governance authors what enters the shared substrate, how it is governed, what conflicts are preserved, and what the AI's role is relative to the content — before and during the inter-Self event. Governance is not a review of what exchange produced; it is an authority structure over the medium through which exchange occurs. The foil approaches' governance wrappers, however thorough, operate on outputs or records rather than on the exchange medium itself.

**Property 4: Conflicts arising within the exchange medium are first-class objects.** Paper 3 Claim 3 (formalized in separate D1-series notes) establishes the three-tier conflict-handling mechanism — preserve, resolve via orchestration, escalate to humans — that operates over the shared substrate. Conflicts that arise during inter-Self coordination are preserved as first-class substrate state rather than filtered, averaged, or discarded. Foil approaches do not systematically preserve conflicts as first-class objects within the exchange medium. They may surface conflicts through alerts, error codes, or human-readable logs, but the architectural-pattern-register treatment of conflict as a preservable substrate property is not present.

---

## 5. Why foil formalization is prior art

Formalizing the named foil is not explanatory context. It is prior-art work that forecloses three categories of adversarial equivalence claim.

**Foreclosed claim (a): Governance wrappers around message-passing are equivalent to the shared substrate.** This claim would hold that adding structured logging, policy metadata, or human-review gates to a message-passing exchange produces a system that satisfies Paper 3's Claim 1 shared substrate commitment. The foil formalization forecloses it: the shared substrate commitment requires that the exchange medium itself be human-governed substrate content carrying the six Paper 1 commitments. Governance wrappers around message-passing do not convert the message channel into such a medium. The architectural distinction established in this note and dated by this publication record cannot be claimed by subsequent work without departure from the prior art.

**Foreclosed claim (b): Logging tool-call exchanges constitutes substrate-mediated inter-AI coordination.** This claim would hold that maintaining an auditable record of inter-agent tool invocations satisfies the substrate-mediated coordination commitment. The foil formalization forecloses it: substrate-mediated coordination requires that the coordination medium — not its audit log — be governed substrate content. A tool-call log is a record of exchange; the shared substrate is the medium of exchange. These are not the same architectural object.

**Foreclosed claim (c): Shared memory with access controls satisfies Paper 3's architectural commitments.** This claim would hold that a shared memory object, protected by access-control rules and inspectable by operators, satisfies the shared substrate commitment. The foil formalization forecloses it: the shared substrate commitment is not satisfied by making a memory object inspectable. It requires that the memory object carry the six Paper 1 commitments — including human-authored orchestration rules governing how the AI mediates content, conflict preservation as a structural property, and human-governed authority over the content as a design-time architectural property. An access-controlled shared memory object does not carry these commitments within itself.

Each foreclosed claim is a real and plausible approach. They are not straw men in the sense of being implausible or easily dismissed. They are plausible precisely because they genuinely add governance to inter-AI coordination relative to ungoverned baselines. The foil formalization's contribution is not to dismiss these approaches but to establish, at a dated publication, that they are architecturally distinct from the shared substrate approach and do not satisfy the commitments Paper 3 names.

---

## 6. Operational test

For a proposed inter-AI coordination mechanism, the following test distinguishes substrate-mediated coordination from governance-retrofitted coordination.

**Question 1**: Is the exchange medium itself authored substrate content? That is, does the medium through which the coordinating agents exchange content have the same status as the substrate content each participating system uses for its own internal coordination, governance, and reasoning?

- If yes: proceed to Question 2.
- If no: the mechanism is not substrate-mediated, regardless of what governance is applied around it. It is a foil-form mechanism.

**Question 2**: Do the six Paper 1 commitments — human-governed authority over content, conflict preservation as a first-class property, AI-as-mediator constraints, tool-agnosticism, linear-cost composition, and substrate-as-coordination-artifact — hold within the exchange medium, not merely around it?

- If yes: proceed to Question 3.
- If no: the mechanism does not carry the Paper 1 inheritance into the inter-Self exchange. It may carry those commitments within each participating system's home substrate; it does not carry them in the exchange medium.

**Question 3**: Is governance — specifically, the human right to inspect, modify, and override the exchange medium's content and orchestration rules — a property of the exchange medium's design, exercisable before and during exchange and not only after exchange concludes?

- If yes: the mechanism satisfies the substrate-mediated coordination commitment.
- If no: governance is retrofitted around the exchange rather than intrinsic to it.

A mechanism that fails Question 1 may be a useful coordination mechanism. It is not substrate-mediated coordination in the sense Paper 3 commits to. A mechanism that passes Question 1 but fails Question 2 carries substrate-level infrastructure without the Paper 1 inheritance. A mechanism that passes Questions 1 and 2 but fails Question 3 has substrate form without governance intrinsicness. The shared substrate approach, as Paper 3 describes it, passes all three.

---

## 7. Closing the Claim 1 sub-commitment set

D1.01 through D1.05 together cover the five sub-commitments of Paper 3 Claim 1: temporary construction, the six Paper 1 commitments within the exchange medium, the inter-Self perimeter property, persistence policy, and the named architectural foil. D1.06 begins the Claim 2 (Full Aspect Integration) sub-commitments.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Opaque Agent-to-Agent Communication as Paper 3's Named Foil.* Series D — Paper 3 Derivation Notes, Note D1.05 (#470). May 14, 2026. ORCID: 0009-0004-8065-3235.
