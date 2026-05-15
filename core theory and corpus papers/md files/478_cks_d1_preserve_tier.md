# Preserve Tier as Inter-Self Conflict Preservation

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 of the CKS theory series establishes a three-tier inter-Self conflict-handling mechanism — preserve, resolve via orchestration, escalate to humans — as what Paper 1's substrate-level conflict preservation principles produce when extended to coordination across the inter-Self perimeter. This note formalizes the first tier: **preserve**. The preserve tier applies when the task conducted under a Full Aspect Integration (FAI) event does not require resolution of a particular conflict. Under this tier, both sides of the conflict are retained as first-class objects in the shared substrate's conflict registry, with full provenance; neither side is marked authoritative; and the conflict remains in the shared substrate for the duration of the FAI event. At dissolution, preserved conflicts carry through to each participating Self's home substrate as governance annotations, feeding each home action-feedback evolution path. The note states when preserve applies, what it does structurally in the shared substrate, how carry-through to home substrates operates, and how the tier inherits from Paper 1 Claim 2's conflict-as-first-class-substrate-state commitment. Four failure modes the sub-commitment defends against are named. An operational test closes the note. D1.13 opens the three-note Claim 3 sub-commitment set; D1.14 (resolve via orchestration) and D1.15 (escalate to humans) follow.

---

## 1. Position in the derivation series

This note is D1.13 in the Series D derivation chain, the thirteenth Phase D1 note (#478 in the continuous series numbering). Phase D1 derives sub-commitments from Paper 3's six claims. D1.13 derives from Paper 3 Claim 3, which establishes the three-tier inter-Self conflict-handling mechanism. D1.13 is the first of three notes opening the Claim 3 sub-commitment set:

- **D1.13 (this note):** The preserve tier — when it applies; what it does; how it carries through to home substrates.
- **D1.14:** The resolve via orchestration tier — conflict classes for which prebuilt orchestration rules in the shared substrate determine the response.
- **D1.15:** The escalate to humans tier — conflicts for which no automated resolution is warranted, surfaced across the inter-Self perimeter to the joint governance authorities of participating Selves.

The three-tier mechanism is not fresh conflict-handling architecture. Paper 3 Claim 3 articulates what Paper 1's two-level conflict-handling principles — substrate-level preservation as architectural default, cell-level resolution under orchestration rules — produce when composed with the shared substrate and the FAI operation at inter-Self scope. D1.13's sole work is to state precisely what the preserve tier does, when it applies, and what its structural commitments are, in operational form.

---

## 2. When the preserve tier applies

The preserve tier is the appropriate response to a conflict surfaced during an FAI event in three classes of situation.

**Informational conflicts.** Two participating Selves' aspects may carry different specifications for the same operational domain — different default behaviors, different priority orderings, different decision rules — that are both legitimate within their respective Selves' governance. Neither specification is wrong; each reflects the governance choices of the Self that produced it. No authoritative resolution is available within the shared substrate, nor is one needed: the task being conducted under the FAI event does not depend on selecting one specification over the other. The conflict is informational: it records that the two Selves approach the same domain differently. The preserve tier keeps both specifications in the shared substrate without selecting between them.

**Boundary-marking conflicts.** Some conflicts are valuable not despite their irresolvability but because of it. When two Selves' governance approaches diverge at a particular operational boundary, the conflict itself is the record of where that boundary lies. Resolving such a conflict — picking one side over the other, or merging both into a compromise specification — erases the boundary signal. Home governance for each Self needs that signal: it tells each Self where its own governance approach ends and another's begins, information that feeds future governance decisions about how to configure FAI events, what aspects to contribute, and how to handle similar encounters. The preserve tier treats boundary-marking conflicts as first-class boundary information rather than as problems to eliminate.

**Conflicts beyond the shared substrate's resolution authority.** A third class arises when the conflict would require governance authority that the shared substrate's orchestration rules do not cover and that escalation to human governance is not warranted. In this class, the appropriate response is to preserve the conflict in the shared substrate for the duration of the FAI event and carry it through to home governance at dissolution, where each Self's own governance authorities can determine how to treat the conflict boundary independently.

The common thread across all three classes is the same: when the task does not require selecting one side, preservation is the architecturally honest response. Selecting a side when the task does not require it destroys information the shared substrate has no mandate to destroy.

---

## 3. What the preserve tier does in the shared substrate

When the preserve tier applies to a conflict surfaced during an FAI event, four structural commitments hold in the shared substrate.

**Both sides retained.** Both conflicting specifications are registered in the shared substrate's conflict registry as first-class objects. Neither is discarded, neither is demoted to a subordinate annotation on the other, and neither is silently merged into a single synthesis entry. Both sides exist as coordinate, equal substrate content for the duration of the FAI event. This is the foundational commitment: preservation means both sides, not a processed representative of both sides.

**Neither side marked authoritative.** Conflict registration in the preserve tier assigns no authority weight to either side. The conflict registry entry records which contributing Self's aspect produced each specification, but it does not record a resolution verdict. Both sides remain unresolved substrate content. No downstream orchestration within the FAI event operates on the assumption that either side was selected; operations that require one of the two specifications to proceed must either trigger the resolve tier or the escalate tier, or must operate on a parameter of the task that does not depend on resolving the conflict.

**Full provenance carried.** Each side of a preserved conflict carries its provenance record: which contributing Self's aspect produced the specification; the governance authority under which that aspect was contributed to the shared substrate; the timestamp of contribution; and the FAI event identifier within which the conflict was surfaced. Provenance is not a supplement to the conflict registry entry — it is constitutive of it. A conflict registry entry without provenance is not a first-class substrate object in the CKS sense; it is a content fragment without an accountability chain.

**Duration in the shared substrate.** A preserved conflict remains in the shared substrate for the full duration of the FAI event. It does not expire during the event, it is not garbage-collected when the task that surfaced it is completed, and it is not overwritten if the same conflict class is encountered again. Subsequent encounters of the same conflict class during the same FAI event add their own registry entries; they do not supersede the original. This duration commitment is what makes carry-through possible: the conflict must still be in the shared substrate at dissolution for the carry-through mechanism to function.

---

## 4. Carry-through to home substrates as governance annotations

Preservation in the shared substrate is not the end of the preserve tier. The tier includes a carry-through mechanism that operates at dissolution: when the FAI event concludes and the shared substrate returns the coordination outputs to each participating Self's home substrate, preserved conflicts travel as governance annotations rather than as resolved content.

**The annotation.** The carry-through annotation is action-layer content in each participating Self's home substrate. Its content is: during FAI event *X*, conflict *Y* was encountered; both sides are preserved; the two sides are specified in the attached provenance record; home governance should determine how to treat this boundary. The annotation does not resolve the conflict. It does not recommend a resolution. It records the boundary as encountered, preserves both sides, and identifies the governance question the conflict raises for the home Self.

**Why carry-through is constitutive of the preserve tier.** Without carry-through, preservation is conflict-deferral rather than governance-productive information transfer. A conflict that is preserved in the shared substrate for the duration of the FAI event, then discarded at dissolution, produces no benefit to either home governance structure. The information the conflict carries — where the two Selves' governance approaches diverge, what the specific divergence is, when and under what authority it arose — never reaches the governance context in which it can be acted upon. Carry-through is what transforms preservation from a passive architectural default into an active governance input.

**Feeding home action-feedback evolution.** The annotation lands in each home substrate's action layer. This is the content stratum that feeds action-feedback evolution (the third evolution mechanism of Paper 2), through which home governance updates its operational rules and behavioral specifications in response to accumulated operational experience. A carry-through annotation about a preserved inter-Self conflict is exactly the kind of operational experience that action-feedback evolution is designed to process: encountered at inter-Self scope, carried to home scope, ingested through the home perimeter's governance-configured ingestion rules, and available to home governance as evidence about where governance attention is warranted.

**Independent treatment at each home substrate.** The annotation is delivered to each participating Self's home substrate independently. Each Self's home governance determines how to treat the boundary the annotation records — whether to revise its own aspect specifications for future FAI events, whether to propose a shared orchestration rule to the joint governance of future events, or whether to treat the boundary as a standing feature of inter-Self coordination with this partner. These are governance decisions each Self makes under its own authority; the preserve tier does not coordinate them.

---

## 5. Inheritance from Paper 1 Claim 2

The preserve tier is Paper 1 Claim 2's conflict-as-first-class-substrate-state commitment applied at inter-Self scope. The inheritance is direct.

**Both sides retained.** Paper 1 Claim 2 commits to retaining both sides of a conflict as substrate content, without auto-resolution. The preserve tier's both-sides-retained commitment at inter-Self scope is this commitment with no modification other than scope: the two sides are now two Selves' contributed aspects rather than two cells' entries, but the structural commitment is identical.

**First-class registration.** Paper 1 Claim 2 requires that conflicts be registered as first-class substrate objects — addressable, inspectable, and subject to the three governance rights — rather than as implementation artifacts or transient runtime state. The preserve tier's conflict registry entry is this requirement at inter-Self scope: the conflict entry is a first-class object in the shared substrate, subject to the same governance rights that apply to all shared substrate content.

**Not auto-resolved.** Paper 1 Claim 2 explicitly rules out auto-resolution as a response to conflict. The preserve tier's neither-side-marked-authoritative commitment is this prohibition at inter-Self scope: no resolution verdict is recorded, and no downstream orchestration operates on a resolution assumption.

The fresh content Paper 3 Claim 3 contributes at the preserve tier is the inter-Self specification: the conflict is now between two contributing Selves' aspects within a shared substrate, rather than between two cells within one substrate; the conflict registry is a shared substrate object rather than a home substrate object; and the carry-through annotation mechanism is new at this scope (Paper 1 has no FAI dissolution event). Paper 3 does not redesign preservation — it states what Paper 1's preservation commitment produces when the coordination scope crosses the inter-Self perimeter.

---

## 6. Four failure modes the sub-commitment defends against

**Auto-resolution of boundary-marking conflicts.** A conflict that signals where two Selves' governance approaches diverge is resolved rather than preserved — one side selected by orchestration logic that treats the conflict as a resolve-tier conflict when no prebuilt resolution rule applies. The boundary signal is erased. Home governance for both Selves is deprived of information about the encountered divergence. The preserve tier defends against this by requiring that conflicts without applicable orchestration rules and without escalation justification default to preservation, not to resolution.

**Silent preservation.** A conflict is preserved in implementation — both sides retained in the shared substrate's working state — but not registered as a first-class conflict registry object. The conflict is not addressable by governance inspection; it cannot be subject to the three governance rights; it has no accountability chain. The preserve tier defends against this by requiring conflict registry registration as constitutive of preservation, not supplementary to it.

**One-sided preservation.** One side of the conflict is retained in the shared substrate; the other is silently discarded during the FAI operation. The conflict registry records only the retained side, or records both sides with one marked as superseded. The preserve tier defends against this by requiring both sides as coordinate, equal substrate content with no authority differential recorded.

**Non-carry-through.** Conflicts are preserved in the shared substrate for the duration of the FAI event and then discarded at dissolution without annotation to home substrates. Home governance receives no record of the encountered boundary. The preserve tier defends against this by making carry-through constitutive of preservation at dissolution: a preserved conflict that does not carry through to home substrates as a governance annotation is not a preserved conflict in the CKS sense — it is conflict-deferral with a disclosure gap.

---

## 7. Operational test

A system implements the preserve tier of the inter-Self conflict-handling mechanism if and only if all of the following are true for any conflict preserved during a completed FAI event.

1. Both sides of the conflict are locatable as first-class objects in the shared substrate's conflict registry (or, post-dissolution, in the Locus 2 durable record of the FAI event). Neither side is absent, demoted, or merged into a single synthesis entry.

2. The conflict registry entry for each side carries full provenance: the contributing Self's identity; the governance authority under which contribution occurred; the timestamp of contribution; and the FAI event identifier.

3. Neither side of the conflict carries an authority weight, resolution verdict, or "selected" marker. Both sides exist as unresolved substrate content.

4. In each participating Self's home substrate, an action-layer annotation exists that records: the FAI event identifier; the conflict identifier; both sides of the conflict (by reference to the provenance record); and the governance question the conflict raises for home governance.

5. The action-layer annotation in each home substrate is addressable by home governance under the standard three governance rights (inspect, modify, override) — it is not a hidden system record or an implementation artifact.

A system in which any of (1)–(5) fail does not implement the preserve tier in the CKS sense. It may preserve conflicts in an implementation-level sense, or carry information forward through other mechanisms, but the structural commitments that make preservation governance-productive — first-class registration, both-sides retention, full provenance, and carry-through as action-layer annotation — are not all satisfied.

---

## 8. Conclusion

The preserve tier is the first response to conflict in the CKS three-tier inter-Self conflict-handling mechanism, applying when the task conducted under a FAI event does not require resolution. Its structural commitments — both sides retained as first-class substrate content, neither side marked authoritative, full provenance carried, duration in the shared substrate through dissolution, and carry-through to home substrates as action-layer governance annotations — are Paper 1 Claim 2's conflict-as-first-class-state commitment extended to inter-Self scope. The tier is not conflict-deferral: carry-through is constitutive of preservation, and it is carry-through that transforms a preserved conflict boundary into actionable governance input for each participating Self's home governance structure. D1.14 takes up the resolve via orchestration tier; D1.15 takes up the escalate to humans tier.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Preserve Tier as Inter-Self Conflict Preservation.* May 14, 2026. ORCID: 0009-0004-8065-3235.
