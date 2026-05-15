# Action-Feedback Feed Locus at the FAI Hand-Off Boundary

**Series:** CKS Derivation Notes — Series D, Phase D1 (Foundational Sub-Commitments)
**Note ID:** D1.17
**Sequential Number:** #482
**Parent Claim:** D0.04 — Paper 3 Claim 4 (Four-locus evolution-feed mechanism at the FAI hand-off boundary)
**Claim 4 Sub-Commitment Position:** First of five (D1.17–D1.21)

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D1.17 formalizes the action-feedback feed locus at the FAI hand-off boundary: the architectural commitment that, at FAI dissolution, event outcomes become action-layer content in each participating Self's home substrate and feed directly into each Self's home action-feedback evolution mechanism. This locus is the first of four loci at Paper 3's FAI hand-off boundary (D0.04/Claim 4) and the first of five Claim 4 sub-commitments (D1.17–D1.21). The central prior-art claim is that no new evolution mechanism is required: FAI outcomes are action-layer content; home action-feedback evolution already processes action-layer content; the FAI origin is provenance metadata carried alongside each record, not a signal that routes the record to a different processing path. This note identifies what categories of FAI outcomes enter the home action layer, traces how home action-feedback evolution processes them under the unchanged Paper 2 mechanism, states the inheritance from Papers 1 and 2, and specifies four failure modes the sub-commitment defends against. An operational test closes the note.

---

## 1. The Sub-Commitment Stated

At the moment an FAI event dissolves, the event's outcomes enter each participating Self's home substrate as **action-layer content**. Once in the home action layer, these records are processed by home action-feedback evolution exactly as Paper 2 specifies for any action-layer content. The FAI origin is part of each record's provenance — it identifies which FAI event produced the record, which shared substrate it transited through, and which contributing aspect it traces to — but this provenance metadata does not alter the processing path. Home action-feedback evolution evaluates FAI-origin records alongside all other action-layer records using the same evaluation machinery.

The claim is negative as well as positive. FAI outcomes do not bypass the action-feedback mechanism. FAI outcomes do not trigger a separate evolution pathway. FAI outcomes do not require governance to implement a new evaluation loop. The mechanism Paper 2 established for processing action-layer content is sufficient, without modification, to process action-layer content that originates from an FAI event.

This is D1.17, the action-feedback feed locus sub-commitment, opening the Claim 4 sub-commitment set. The four remaining Claim 4 sub-commitments are: D1.18 (DNA evolution locus — governance-authorized selective absorption of DNA content from FAI into home DNA via directed selection), D1.19 (instinct exclusion — LLM weights and instinct-layer content do not cross the inter-Self perimeter), D1.20 (hand-off boundary as architectural object — the boundary is governance-configured, inspectable, and attribution-carrying), and D1.21 (substrate ingestion mechanism — the mechanics by which dissolution triggers home-perimeter ingestion). D1.17 covers the first locus at the boundary; the remaining four sub-commitments cover the second locus, the explicit exclusion, the boundary object itself, and the ingestion mechanics respectively.

---

## 2. What FAI Outcomes Become in the Home Action Layer

Three categories of FAI outcomes enter a participating Self's home action layer at dissolution.

**Operational results.** The coordination work the FAI event performed — what the shared substrate produced, what outputs were generated within it, what the event achieved as a coordination episode — becomes a class of action-layer records. From each Self's home perspective, the FAI event is an episode of operational experience. Its results are recorded in the same action layer that holds records of every other operational episode: cells executed, conflicts encountered, decisions made, outputs produced. There is no separate store for inter-Self experience. The action layer is the authoritative operational history of the Self, and FAI experience is part of that history.

**Conflict carry-through annotations.** D1.16 formalizes how conflicts preserved within the shared substrate during an FAI event carry through as evolution-feed annotations to participating Selves' home substrates. These annotations are one category of action-layer content entering through the D1.17 locus. A conflict preserved during the FAI event — not resolved within the shared substrate, not escalated to human resolution during the event itself — arrives in each participating Self's home action layer as an annotated record flagging a boundary that home governance must address during evolution-mechanism operation. D1.17 and D1.16 are complementary sub-commitments: D1.16 formalizes the preservation and annotation of conflicts during the FAI event; D1.17 formalizes that these annotations, together with operational results and authorized evolution inputs, enter home evolution through the action-feedback locus. The carry-through annotation is not routed to a different mechanism. It enters the home action layer and is evaluated by home action-feedback evolution as a class of operational evidence — specifically, evidence of a coordination boundary that proposals may need to address.

**Authorized evolution inputs.** The shared substrate may contain content that the participating Self's governance has designated, in advance, for action-layer ingestion at dissolution. This is governance-configured scope: the home perimeter's authority structure specifies which content classes from shared-substrate activity are eligible to enter the home action layer. Content outside the authorized scope does not enter. Content within it enters as action-layer records attributed to the FAI event. The asymmetric ingestion property (D1.21) elaborates that different Selves may take different things from the same FAI event — each governed by its own home perimeter authority — but the mechanism is the same: authorized content enters as action-layer records.

All three categories enter the home action layer with full provenance. Each record carries attribution to the FAI event, traceability to the shared substrate it originated in, and attribution to the contributing aspect and contributing Self where applicable. Provenance is structural: it travels with the record. It does not require a lookup after the fact. An observer examining the home action layer after dissolution can identify every FAI-origin record, trace it to the specific FAI event, and confirm its category.

---

## 3. How Home Action-Feedback Evolution Processes Them

Once in the home action layer, FAI-origin records are processed by home action-feedback evolution under the unchanged Paper 2 mechanism. The processing path is:

Proposing substrates evaluate the action-layer records. Proposals for substrate changes that the operational evidence — including FAI-origin operational evidence — supports are generated and surfaced. Stage 1 governance review examines proposals. Stage 2 human governance decides which proposals to accept. Accepted proposals are implemented through directed selection operating on home DNA. The FAI origin is part of the provenance of the operational records that inform proposals; it is not a variable in the evaluation logic itself.

This is the key architectural point: the mechanism does not inspect the provenance of action-layer records to select an evaluation procedure. It evaluates action-layer content. FAI-origin content is a class of action-layer content. The same evaluation procedure that applies to action-layer content generated entirely within the home Self's operational history applies to action-layer content that originated in an FAI event and entered through the D1.17 locus. The FAI origin is visible to governance — it is in the provenance record — but governance evaluates proposals through the same authority architecture it uses for all action-layer-informed proposals.

The absence of a new mechanism is the substantive prior-art claim this note formalizes. A design that routes FAI-origin action-layer records to a separate evaluation loop — even one that resembles the home action-feedback mechanism closely — is not the CKS architecture. The CKS architecture commits to a single action-feedback evaluation pipeline at the home perimeter. FAI events add a new category of input to that pipeline; they do not multiply the number of pipelines.

---

## 4. Inheritance from Papers 1 and 2

D1.17 inherits from two prior-paper commitments that jointly make the action-feedback locus work.

**Paper 1 substrate-as-source-of-truth (A1.08).** The home substrate is the authoritative persistent record of the Self's operational history. FAI outcomes entering the home action layer at dissolution become authoritative records: they are in the substrate, they carry provenance, they are subject to the full rights of inspection, modification, and override that the human-governed commitment preserves. There is no secondary record-keeping layer for inter-Self experience. The home substrate holds it, exactly as it holds every other category of the Self's operational history. This is what makes the action-layer content authoritative rather than advisory — the substrate-as-source-of-truth commitment extends to FAI-origin content without a special case.

**Paper 2 action-feedback evolution (B1.15 / C1.19).** Paper 2 establishes the action-feedback mechanism as the third of three evolution mechanisms operating in productive tension within each Self. The mechanism runs from operational experience to proposals to governance review to directed selection. D1.17 does not redesign this mechanism. It specifies that FAI outcomes are a class of operational experience — that they enter the action layer as action-layer content and are therefore within the scope of what the Paper 2 mechanism already processes. The inheritance is direct: the mechanism is complete as Paper 2 specifies it; the D1.17 commitment is that FAI events are a source of action-layer content for it, not that the mechanism needs to be extended to accommodate inter-Self experience.

Together, these two inheritance points establish the sufficiency condition: the existing substrate architecture (Paper 1) and the existing evolution mechanism (Paper 2) are sufficient to handle action-layer content that originates from FAI events. No extension of either is required. The action-feedback locus is the name for the point at which FAI outcomes enter the scope of what these prior-paper commitments already cover.

---

## 5. Failure Modes the Sub-Commitment Defends Against

Four failure modes constitute the design space D1.17 closes:

**FAI outcomes not entering the home action layer.** A design in which FAI results are recorded in the shared substrate but not ingested into participating Selves' home action layers at dissolution fails this sub-commitment. FAI experience remains outside each Self's operational history. Home action-feedback evolution cannot evaluate evidence it does not have. The sub-commitment requires that dissolution trigger ingestion into each home action layer, not merely archiving in a shared or external record.

**FAI outcomes bypassing governance review.** A design in which FAI outcomes directly trigger changes to a Self's DNA or behavior without passing through the action-feedback governance pipeline fails this sub-commitment. The action-feedback mechanism's governance stages — Stage 1 review, Stage 2 human decision — are not optional for FAI-origin proposals. The commitment that FAI outcomes enter the action layer and are processed by the unchanged action-feedback mechanism is simultaneously the commitment that they are subject to the same governance stages every other action-layer-informed proposal passes through.

**Unattributed action-layer records.** A design in which FAI-origin records enter the home action layer without provenance linking them to the FAI event fails this sub-commitment. Provenance is structural. Records must carry attribution to the FAI event, traceability to the shared substrate, and attribution to the contributing aspect. Without provenance, governance cannot distinguish FAI-origin evidence from within-Self evidence, cannot calibrate its evaluation accordingly, and cannot exercise the path-retraceability the substrate-as-source-of-truth commitment (A1.08) requires.

**Separate FAI evolution mechanism.** A design that routes FAI-origin action-layer content to a distinct evaluation pipeline — however similar in structure to the home action-feedback mechanism — fails this sub-commitment. The sub-commitment is not merely that FAI-origin records are evaluated by *some* proposal-and-acceptance machinery; it is that they are evaluated by the *home* action-feedback mechanism, in the same pipeline as all other action-layer content. A separate pipeline creates governance complexity, introduces a second authority surface over the same behavioral output, and undermines the productive tension that Paper 2's three-mechanism architecture achieves through their operation within a unified evaluation framework.

---

## 6. Opening the Claim 4 Sub-Commitment Set

D1.17 is the first of five sub-commitments that together formalize Paper 3's Claim 4. The full set is:

D1.17 (this note) — action-feedback feed locus: FAI outcomes as home action-layer content, processed by the unchanged Paper 2 action-feedback mechanism.

D1.18 — DNA evolution locus: governance-authorized selective absorption of DNA content from the shared substrate into the receiving Self's DNA via directed selection under home governance authority.

D1.19 — instinct exclusion: LLM weights and instinct-layer content do not exchange across FAI, consistent with Claim 2's exchange-bounding and the instinct/reasoning separation Paper 2 establishes.

D1.20 — hand-off boundary as architectural object: the boundary is governance-configured (what enters each home perimeter at dissolution is a governance decision), inspectable, and attribution-carrying; it is not an incidental boundary but a designed architectural object in the CKS pattern.

D1.21 — substrate ingestion mechanism: the mechanics by which dissolution triggers home-perimeter ingestion, including the trigger condition, the ingestion scope determination, and the transition from shared-substrate content to home-substrate input.

D1.17 is the entry point for the Claim 4 set because the action-feedback locus is what makes FAI events productive for home evolution without requiring new mechanisms. The subsequent sub-commitments (D1.18–D1.21) elaborate the second locus, the explicit exclusion, the boundary object, and the mechanics — all of which presuppose the action-feedback locus as established here.

---

## 7. Operational Test

After an FAI event involving two or more participating Selves:

1. An observer examines each participating Self's home substrate. The observer can identify, in the home action layer, records attributed to the FAI event. These records are distinct from records of within-Self operational history by their provenance metadata, which carries the FAI event identifier, the shared substrate identifier, and the contributing aspect attribution.

2. The observer can confirm that the FAI-origin action-layer records — including operational result records, conflict carry-through annotation records, and authorized evolution input records — are present in the same action layer as within-Self operational records. There is no separate store for inter-Self experience.

3. The observer can confirm that proposals generated by proposing substrates that draw on FAI-origin action-layer evidence pass through Stage 1 governance review and Stage 2 human governance decision under the same authority architecture as proposals drawing on within-Self action-layer evidence. There is no separate evaluation pipeline for FAI-origin proposals.

4. The observer can confirm that FAI-origin records carry the full provenance chain: FAI event → shared substrate → contributing aspect → contributing Self, with the provenance embedded in the record structure and not dependent on external lookup.

If all four conditions are satisfied, the system instantiates the D1.17 action-feedback feed locus sub-commitment. If any condition fails — if FAI-origin records are absent from the home action layer, if they enter without provenance, if they bypass governance review stages, or if they are routed to a separate evaluation pipeline — the sub-commitment is not instantiated.

---

## References

Li, W. (April 2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems*. Independent publication. (Paper 1 of the CKS theory series.)

Li, W. (April 2026). *The Instinct/Reasoning Separation Outside the Model*. Independent publication. (Paper 2 of the CKS theory series.)

Li, W. (April 2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration*. Independent publication. (Paper 3 of the CKS theory series.)
