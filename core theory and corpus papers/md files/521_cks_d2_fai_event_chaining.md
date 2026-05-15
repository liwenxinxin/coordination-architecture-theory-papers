# FAI Event Chaining and Provenance Continuity

**Series:** CKS Derivation Notes — Phase D2, Note D2.26 (Publication #521)
**Parent notes:** D1.01 (shared substrate as temporary construction); D1.18 (DNA evolution feed locus)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Network for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When a participating Self absorbs evolution outputs from one FAI event and subsequently contributes content informed by that absorption to a subsequent FAI event, a chain of inter-Self provenance dependencies is created. D2.26 formalizes the governance requirements for this chained-event scenario — specifically: provenance chain continuity across events, chain transparency as a configurable governance requirement, and the anti-pattern of chain laundering (re-contributing absorbed content as if it originated with the re-contributing Self, without provenance tracing to its original inter-Self source). The note explains how the Dimension 6 internalization depth choice at each absorption step determines whether chain traceability is available to future observers, and connects FAI event chaining to the population-scale collective evolution mechanism of Claim 6. An operational test is provided for auditors and governance architects assessing whether a chained-event deployment preserves provenance continuity.

---

## 1. D2.26 as operational decomposition

D2.26 is an operational decomposition of two parent sub-commitments. From D1.01, the shared substrate is a temporary construction — it exists for the duration of an FAI event, then dissolves, with evolution outputs persisting in each participating Self's home substrate under governance-configured ingestion. From D1.18, DNA-layer content produced through FAI can feed a participating Self's DNA evolution mechanism: orchestration patterns, schemas, and governance rules absorbed via the DNA evolution locus become content within the absorbing Self's home substrate, subject to that Self's authority structure and directed selection machinery from that point forward.

D2.26 asks: what happens when a Self that has absorbed content through one FAI event subsequently participates in a second FAI event, contributing aspects that now include the absorbed content? This creates a chain — FAI Event 1 produces content that travels through Self A's home substrate, then reappears as part of Self A's contribution to FAI Event 2. The governance requirements for this chain are not fully specified by D1.01 or D1.18 individually; D2.26 formalizes them as an operational decomposition specific to the chained-event dimension.

---

## 2. What FAI event chaining means

A concrete example establishes the pattern.

Self A and Self B participate in **FAI Event 1**. The event proceeds under its configured governance; both Selves contribute aspects; the shared substrate carries content from both. On dissolution, Self A's governance authorizes absorption of some of Self B's DNA-layer content — an orchestration schema, a conflict-handling rule, a coordination pattern — via the DNA evolution locus (D1.18). Self A's home substrate now contains content that traces back to Self B as original author through FAI Event 1.

Time passes. Self A's governance further develops the absorbed content through directed selection — it is refined, extended, integrated with other home substrate content. It is now part of Self A's own governance architecture, but its origin is traceable: Self A absorbed it from FAI Event 1, and Self B was the contributing Self.

Self A now participates in **FAI Event 2**, alongside Self C and Self D. Self A contributes aspects that include content derived from the absorbed material. Self C and Self D encounter, in the shared substrate of FAI Event 2, content that traces — through Self A's home substrate — back through FAI Event 1 to Self B's original contribution.

This is an FAI event chain: Event 2 contains content whose provenance runs through Event 1 via Self A's intermediate absorption. The chain creates inter-event provenance dependencies that governance must handle explicitly.

---

## 3. Three governance requirements for chained events

### Requirement 1 — Provenance chain continuity

When Self A contributes to FAI Event 2 content that was absorbed from FAI Event 1, the provenance chain must remain intact at the depth configured by the relevant provenance governance dimensions. Observers tracing content in FAI Event 2's shared substrate should be able to navigate back through Self A's absorption record to FAI Event 1, and from there to Self B's original contribution — at whatever depth the governance configuration of the relevant events supports.

Provenance chain continuity does not require infinite historical depth in all cases; the architecture's configurable carry-over and internalization dimensions govern how far back the chain can be traced. What it does require is that the chain *not be broken by default* when Self A's home governance configured depth is sufficient to support it. A chain that exists in principle but is severed by governance misconfiguration is a different failure mode from a chain that is explicitly configured to terminate at a given depth.

### Requirement 2 — Chain transparency

FAI Event 2's governance configuration should specify whether contributing Selves' aspects may contain FAI-origin content from prior events and, if so, whether disclosure is required. Chain transparency, when configured as a requirement, means that Self A discloses at the time of contribution that its aspects include content absorbed from prior FAI events — identifying the prior event(s) and, if internalization depth supports it, the original contributing Selves.

Chain transparency is not an unconditional architectural requirement; it is a governance choice that operators of FAI Event 2 may make under their joint authority. The architecture surfaces it as a configurable dimension. What is architecturally required is that the configuration point exists and is governed explicitly — the absence of chain transparency as a requirement is itself a governance decision, not an oversight.

### Requirement 3 — No chain laundering

Content cannot be laundered through an FAI chain. Chain laundering is the anti-pattern in which a Self absorbs content from another Self via a prior FAI event, then re-contributes that content to a subsequent FAI event as if it originated with the re-contributing Self — without provenance tracing to the original inter-Self source.

The harm of chain laundering is not aesthetic. Organizations and external auditors may need to understand where governance approaches, schemas, and coordination architectures originated across organizational boundaries. If Self B developed a governance architecture that Self A absorbed and Self C later adopted via FAI Event 2, the fact that Self B is the originating organization may be material — to attribution, to intellectual property accounting, to understanding which organizations' governance practices are propagating through a network. Chain laundering forecloses this understanding by presenting inter-organizational content as if it were internally developed.

The architecture forecloses chain laundering through the combined operation of provenance carry-over depth at the perimeter (Dimension 5) and provenance preservation on internalization (Dimension 6). If both are configured to preserve inter-Self attribution, the chain from Self B through FAI Event 1 through Self A to FAI Event 2 is traceable, and laundering — presenting content as Self A's own — is contradicted by the substrate record. If either is configured to discard the attribution, the chain is broken, and laundering becomes possible not through deception but through architectural omission.

---

## 4. Chain provenance depth: the Dimension 6 implication

The connection between Dimension 6 (provenance preservation on internalization) and chain traceability is the critical forward-looking implication of this note.

When Self A internalizes content from FAI Event 1, Dimension 6 governs how much provenance detail is retained in Self A's home substrate. At one end of the configuration space — call it Option A — Self A's records show only "absorbed from FAI Event 1" without recording Self B as the original contributing Self. At the other end, Self A's records carry the full cross-perimeter provenance: "absorbed from FAI Event 1; original contribution by Self B."

The Dimension 6 choice Self A makes at absorption time determines what provenance information will be available to FAI Event 2's shared substrate and its participants. If Self A chose Option A, then when Self A contributes to FAI Event 2, the chain from Self B through FAI Event 1 is not traceable from FAI Event 2's perspective — not because the chain did not exist, but because Self A did not preserve the attribution needed to navigate it. The shared substrate of FAI Event 2 can record that Self A contributed content, and Self A's home records can record that the content traces to FAI Event 1, but the link from FAI Event 1 to Self B is absent.

This means that Dimension 6 choices are not purely local decisions. A Self that anticipates participating in recurring FAI events — or that is participating in an ongoing relationship with other Selves across a sequence of events — should configure internalization depth with future chain traceability in mind. Option A may be appropriate when chain traceability is not anticipated to matter; it is the wrong choice when the Self or its governance authorities expect that the provenance chain will need to be navigated by future FAI participants or external auditors.

The forward-looking implication generalizes: governance architects designing Self A's internalization policy should ask not only "what do we need to retain for our own home governance?" but also "what will future participants in FAI events we contribute to need to trace?" The answer to the second question may require deeper internalization depth than the first question alone would suggest.

---

## 5. Chaining as a mechanism of population-scale collective evolution

FAI event chaining is one of the concrete mechanisms through which Claim 6's population-scale collective evolution operates (D1.27).

Claim 6 commits to population-scale collective evolution as the architectural object that accumulates across many FAI events among many CKS-governed Selves under joint authority across population-level governance perimeters. The mechanism by which governance architectures propagate through the population is not abstract; it runs through the specific absorption-and-re-contribution pattern that D2.26 formalizes.

Self B's governance approach reaches Self A through FAI Event 1. Self A's governance-directed selection refines and integrates it. Self A's contribution to FAI Event 2 carries the evolved content to Selves C and D, who may in turn absorb, refine, and re-contribute it through subsequent events. A governance architecture that Self B developed propagates through the network in a way that is bounded by each step's home governance directed selection — not every absorbing Self takes every piece of content, and every absorption is subject to the authority structure of the receiving Self.

This is what distinguishes governed collective evolution from ungoverned spread. In ungoverned spread, content propagates without checkpoint or authority structure. In the FAI chaining mechanism, every propagation step is a home governance directed selection event: the absorbing Self's authority structure decides what content is candidate for absorption, which candidates are approved, and which are declined. The content that reaches FAI Event 2 is not what Self B contributed unmodified; it is what Self A's governance selected, refined, and approved from Self B's contribution. The content that reaches Selves C and D is what Self A's further evolution produced from that selection. At every step, human authority is architecturally available to inspect, modify, and override.

The population-scale result — governance architectures propagating through a network of CKS-governed Selves — emerges from the accumulation of individually governed steps. Claim 6's collective evolution commitment is not a claim about emergence beyond governance; it is a claim about what the accumulation of governed steps produces at scale.

---

## 6. The chain laundering anti-pattern: formal statement

**Chain laundering** occurs when a Self absorbs content from another Self via a prior FAI event and subsequently re-contributes that content — or content materially derived from it — to a subsequent FAI event without provenance tracing to the original inter-Self source, presenting the content as if it originated with the re-contributing Self.

Chain laundering has two enabling conditions: (a) provenance carry-over depth at the perimeter is configured not to include inter-Self attribution when Self A contributes to FAI Event 2, and (b) provenance preservation on internalization at Self A's home is configured at a depth insufficient to retain Self B as the original source.

Chain laundering has two harmful consequences: (a) participants in FAI Event 2, including Selves C and D, cannot determine that the content they are encountering traces to Self B — they cannot evaluate it in light of Self B's governance context, reputation, or approach; (b) external auditors examining FAI Event 2's record cannot reconstruct the true governance architecture lineage, potentially misstating which organizations originated the approaches that are propagating through the network.

The architecture forecloses chain laundering when Dimension 5 and Dimension 6 are configured to preserve inter-Self attribution across the relevant events. The anti-pattern is not possible when the provenance chain is intact and carried through the shared substrate; it becomes possible only when governance configuration — intentionally or by default — discards attribution at one of the two configuration points.

The remedy is not a new architectural mechanism. It is governance architects attending explicitly to chain traceability when configuring internalization depth, and FAI Event operators configuring chain transparency as a requirement when the governance context demands it.

---

## 7. Operational test

For a deployment in which contributing aspects in an FAI event may include content absorbed from prior FAI events, the deployment instantiates D2.26's governance requirements if and only if all of the following are true:

1. For any content item in the shared substrate of FAI Event 2, an observer with appropriate access can determine whether the item traces to content absorbed from a prior FAI event by a contributing Self.

2. If (1) is true for a given content item, the observer can navigate the provenance chain back through the contributing Self's home substrate absorption record to the prior FAI event.

3. If (2) is true and the prior FAI event's provenance configuration preserved inter-Self attribution, the observer can identify the original contributing Self in the prior event.

4. No contributing Self can represent content absorbed from a prior FAI event as independently originating with that Self in a way that is contradicted by the substrate record — the provenance chain either supports attribution to the original source or is explicitly recorded as truncated at a configured depth.

5. The FAI Event 2 governance configuration explicitly addresses whether chain transparency is required, with the absence of such a requirement recorded as a governance decision rather than an omission.

A deployment that fails any of (1)–(5) may be useful and may satisfy other governance requirements, but does not instantiate D2.26's chained-event provenance continuity requirements.

---

## 8. Conclusion

FAI event chaining is not an edge case; it is the natural structure of any ongoing network of CKS-governed Selves engaged in recurring inter-Self coordination. As FAI events accumulate, absorption outputs from earlier events become aspects contributed to later events, creating chains of inter-event provenance dependencies that governance must handle explicitly.

Three requirements govern chained events: provenance chain continuity, which preserves the navigability of the chain at configured depth; chain transparency, which requires disclosure of FAI-origin content when governance specifies it; and no chain laundering, which prevents the re-presentation of absorbed inter-organizational content as independently originated.

The Dimension 6 internalization depth choice is the critical point at which the chain is either preserved or broken. Selves anticipating recurring FAI participation should configure internalization depth with future chain traceability in mind — the choice made at absorption time determines what future observers can navigate, and the costs of under-configuration accumulate silently until the moment when traceability is needed.

Understood at population scale, FAI event chaining is the concrete mechanism of Claim 6's collective evolution: governance architectures propagating through a network, one governed absorption at a time. The population-scale property is the accumulation of many individually governed steps. Every step is governed. Ungoverned spread is architecturally foreclosed.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Network for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Event Chaining and Provenance Continuity.* CKS Derivation Notes, Phase D2, Note D2.26 (Publication #521). May 15, 2026. ORCID: 0009-0004-8065-3235.
