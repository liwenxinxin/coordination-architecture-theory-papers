# Untracked Mating — The Anti-Pattern That Arises When DNA Combination Bypasses the Governed Mating Mechanism per B1.10, Recognizable as Ad-Hoc DNA Combination Without Pattern Selection, Unrecorded Combination Breaking Cross-Lineage Ancestry, and Conflict-Ignoring Combination That Silently Resolves Parent DNA Conflicts

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

B1.10 establishes mating as the governed mechanism through which entities in a Coordination Knowledge Substrate (CKS) deployment combine DNA-layer content from multiple parent sources. Three pattern variants — Union, Selective merge, and Lineage-preserved union — are available, each with distinct architectural commitments governing how parent content is carried into offspring, how conflicts are handled, and how cross-lineage ancestry is preserved. Untracked Mating is the anti-pattern that arises when DNA combination happens outside this governed framework: when architects copy rules across entities without recognizing the event as a mating event requiring governance, when combination is performed without governance authorization or mating event records, or when Union-pattern combination is carried out but parent DNA conflicts are silently resolved rather than registered as first-class objects per A1.03. This note formalizes the anti-pattern under the B3 anti-pattern structure, identifies its three recognizable sub-forms, traces the emergence conditions that produce it, characterizes the operational consequences it produces, and specifies the detection and remediation paths.

---

## 1. Commitment Violated

**B1.10 — Mating as governed cross-layer DNA combination through defined patterns.**

B1.10 commits to mating as a CKS lifecycle primitive: the mechanism through which a new entity's DNA-layer content is derived from multiple parent sources, with the specific combination configured by orchestration substrate and governed at every step. The commitment encompasses three pattern variants — Union (keep all parent content, preserve conflicts as first-class substrate state per A1.03), Selective merge (pre-curate what crosses the boundary from each parent under human authority), and Lineage-preserved union (offspring carries pointers to parent cells so every element's provenance is traceable) — and requires that the choice among them be made through governance selection, that the mating event be recorded, that governance authorization accompany the combination, and that cross-lineage ancestry references appear in the offspring birth record per B2.43.

Untracked Mating violates this commitment when DNA combination takes place but the governed mating framework is not engaged: no pattern is selected, no event is recorded, no governance authorization is obtained, or parent DNA conflicts are quietly resolved rather than preserved. The offspring entity exists with multi-source DNA but without the governance infrastructure the commitment requires.

---

## 2. Recognizable Form

Untracked Mating presents in three distinct sub-forms. They share a common structural feature — offspring DNA derives from multiple parent sources without the governed mating mechanism having been applied — but differ in which governance component is absent.

### Form 1 — Ad-Hoc Combination

DNA from multiple parent sources is combined to create a new entity's DNA without selecting and applying any of the formal mating patterns. The combination is informal: an architect copies rules that work from one entity and adds rules from another, producing a new entity whose DNA contains elements from both parents but whose creation is not preceded by a mating event and is not preceded by pattern selection.

Recognition signals: the new entity's DNA contains elements traceable to multiple parent sources; no mating pattern application record exists; B2.50 mating verification finds no pattern record for the combination; the entity was born per B1.09 but the birth record carries no cross-lineage references per B2.43; no mating event record under A2.40 exists for the combination.

Ad-hoc combination is typically invisible to the architects who perform it because it does not feel like an event. It feels like setup work — assembling the configuration for a new entity from parts that are already known to work. The absence of governance engagement is not experienced as a violation but as an efficiency. That invisibility is what makes the anti-pattern persistent.

### Form 2 — Unrecorded Combination

DNA combination is performed with some intentionality — the architect recognizes that content from multiple parent sources is being combined — but governance authorization per B2.49 is not obtained, and the combination is not recorded as a mating event per A2.40. Parent sources may be identifiable after the fact by inspecting the offspring's DNA, but they are not documented at combination time.

Recognition signals: offspring DNA contains elements from multiple identifiable sources; mating event records per A2.40 are absent; governance authorization for the combination is missing from the birth record; parent source lineages are not referenced in the offspring birth record per B2.43; B2.50 mating verification finds governance authorization absent.

Unrecorded combination typically emerges from the same practical disposition as ad-hoc combination but in contexts where some intentionality is present. The architect may recognize that they are drawing from two sources but treat governance engagement as an administrative step that can be deferred or omitted without structural consequence. The structural consequence is that the cross-lineage ancestry the deployment depends on for retraceability is not created.

### Form 3 — Conflict-Ignoring Combination

Union or Lineage-preserved union combination is performed — a formal mating pattern is applied — but A1.03's conflict-as-first-class commitment is not honored at merge time. Parent DNA conflicts are silently resolved: one parent's rule wins when both parents carry content covering the same operational territory, and the winning resolution is written into the offspring's DNA without the conflict being registered in the offspring's conflict registry.

Recognition signals: offspring DNA contains no A1.03 conflict registry entries despite deriving from two parents whose DNA covered overlapping operational territories; post-birth governance review has no conflict registry to work from; B2.50 mating verification finds absent conflict registration for Union-pattern or Lineage-preserved union mating; the offspring's orchestration substrate reflects one parent's approach to contested territory without recording that the other parent covered the same territory differently.

Conflict-ignoring combination is the most operationally sophisticated of the three forms because a formal mating event does take place. The violation is not in the event's absence but in the handling of what the event surfaces. The conflict resolution impulse — the instinct to produce a clean, conflict-free offspring rather than an offspring that carries first-class conflicts for governance review — is what converts a properly-initiated mating event into a partially-untracked one.

---

## 3. Emergence Conditions

Three conditions reliably produce Untracked Mating:

**Copy-paste DNA reuse.** When architects assemble a new entity's DNA by copying rules from existing entities, the copy-paste action does not announce itself as a governance-triggering event. The architect experiences it as reuse of known-good configuration, not as a combination of parent DNA requiring a mating event. The structural consequence — that the offspring now has multi-source DNA whose cross-lineage ancestry is unrecorded — is invisible at the moment of action. This emergence condition produces Form 1 and Form 2 most directly.

**Governance overhead avoidance.** When mating governance is framed — internally or organizationally — as overhead on what appears to be a technical implementation step, the incentive to engage it is undermined. The architect knows the governance mechanism exists but treats it as optional for what seems like a straightforward combination. The mating event, the pattern selection, the authorization, the mating record — each appears to add process cost without adding to the entity's functional capability. The consequence that becomes visible only later is the absent audit trail and the severed cross-lineage ancestry. This emergence condition produces Form 2 most directly.

**Conflict resolution impulse.** When two parents carry DNA covering the same operational territory, the conflict appears as a practical problem to resolve rather than as a first-class signal to preserve for governance. The architect resolves it at combination time, producing a clean offspring. A1.03's commitment is that the conflict is the governance information — it records that two parents disagreed on how this territory should be handled, which is exactly what post-birth governance review needs to evaluate. Resolving it silently removes the record that the disagreement existed. This emergence condition produces Form 3.

---

## 4. Operational Consequences

**Cross-lineage ancestry severed.** Offspring entities without mating records have no documented cross-lineage ancestry. A1.07's retraceability commitment applies at the parentage scope of the offspring — the path from offspring to parent sources must be retraceable. When neither the mating event nor the cross-lineage references in the birth record exist, this path does not exist. Auditors can inspect the offspring's DNA and may be able to infer parent sources by pattern recognition, but that inference is not the substrate-level retraceability A1.07 requires.

**Conflict registry absent.** Conflict-ignoring combination produces offspring whose conflict registry is empty despite the fact that parent DNA conflicts were encountered and resolved at combination time. A1.03's commitment is that conflicts are preserved as first-class addressable objects with their own identity and provenance. When conflicts are resolved silently, they produce no addressable substrate objects. Post-birth governance review has no conflict registry to work from. The governance surprises that later emerge from the silent resolutions — when the de-facto resolution embedded in the offspring's DNA turns out not to reflect the governance intent — have no substrate record to explain their origin.

**Governance integrity compromised.** Unrecorded mating events mean the deployment's governance history is incomplete in a specific and non-obvious way. The deployment may carry other governance records in good standing — birth records, death records, evolution records — while the mating layer of its history is absent. Auditors cannot determine which entities were created through combination of existing entities' DNA and from which sources. Lineage supersession decisions that depend on knowing which offspring supersede which parents cannot be made reliably when the parent-offspring relationships are unrecorded.

**Pattern verification impossible.** B2.50 mating verification is the mechanism that confirms a mating event applied the right pattern for its governance intent and produced the expected structural results in the offspring. It cannot run for combinations that have no pattern records. The detection mechanism that would catch downstream pattern-application errors is unavailable because no pattern application was recorded.

---

## 5. Detection

**B2.50 mating verification.** Run mating verification for all entities whose DNA contains elements from multiple identifiable sources. Mating verification requires a pattern record to execute; entities for which no pattern record exists are positive indicators of Form 1 or Form 2.

**A2.40 mating event audit.** Audit the deployment's mating event records against the population of entities whose DNA inspection reveals multi-source content. Every apparent combination should have a corresponding mating event record with governance authorization. Gaps identify Form 2.

**B2.43 cross-lineage audit.** Inspect the birth records of entities with multi-parent DNA. Birth records should carry cross-lineage references to parent entities. Birth records that lack these references for entities known to carry multi-source DNA identify Form 1 and Form 2.

**A1.03 conflict registry check.** For entities born through Union-pattern or Lineage-preserved union mating, inspect the offspring's conflict registry. Union-pattern mating that encountered overlapping operational territory in the parent DNA should produce populated conflict registry entries. An empty conflict registry in a Union-pattern offspring that derives from parents with overlapping DNA coverage is a positive indicator of Form 3.

---

## 6. Remediation

**For ad-hoc combinations (Form 1).** Retroactively document the combination as a mating event. Determine, to the extent possible from inspection of the offspring's DNA and the parent entities' DNA, which mating pattern best characterizes how the combination was performed. Create mating records per A2.40. Create cross-lineage references in the offspring's birth record per B2.43. Where pattern determination is ambiguous — the combination does not clearly fit Union, Selective merge, or Lineage-preserved union — governance review should determine which pattern to retroactively assign and should record the determination and its rationale.

**For unrecorded combinations (Form 2).** Retroactive governance review and authorization. The review should treat the mating event as requiring the same governance engagement it would have required at combination time, including pattern selection and authorization. The outcome of review should be recorded as a retroactive mating event record with explicit notation that the record is retroactive and the date of the original combination where determinable. Cross-lineage references should be created in the offspring's birth record.

**For conflict-ignoring combinations (Form 3).** Retroactively identify parent DNA conflicts that were present at combination time and silently resolved. This requires inspecting both parent entities' DNA for overlapping operational territory and comparing to the offspring's DNA to determine which resolution was applied. Register the identified conflicts in the offspring's conflict registry per A1.03, with notation that they were retroactively registered and that the current offspring DNA reflects a specific resolution. Address the registered conflicts through directed selection per B1.14, which produces a governed resolution path that can either ratify the silent resolution as the governance-intended one or correct it.

**Structural prevention.** Establish governance workflows that trigger mating governance whenever DNA from multiple parent sources is combined to produce a new entity's DNA. The workflow trigger should be source-based — any combination of DNA-layer content from more than one entity source — not intent-based (architects may not recognize their action as a mating event). The workflow should require pattern selection, governance authorization, mating event record creation, cross-lineage reference creation in the offspring birth record, and, for Union and Lineage-preserved union patterns, conflict registry population for overlapping operational territories. Making the mating governance entry point low-friction reduces the governance overhead avoidance emergence condition that produces Form 2.

---

## 7. Relationship to Adjacent Commitments

Untracked Mating intersects with several other commitments in ways that make its effects non-local:

A1.03 (conflict-as-first-class) is violated directly by Form 3 but is indirectly undermined by Forms 1 and 2 as well, because ad-hoc and unrecorded combinations that happened to encounter parent DNA conflicts produce offspring with unregistered conflicts even if the architect did not actively resolve them — they were simply never examined.

A1.07 (path retraceability) is the commitment that Untracked Mating most directly severs. Retraceability at the offspring scope requires that the path from offspring to its origins be substrate-level addressable. Mating records, cross-lineage references in birth records, and mating event records under A2.40 are the substrate artifacts that make this path addressable. Their absence converts a retraceable lineage into one that must be reconstructed by inspection — possible in some cases, unavailable in others, and not the architectural property A1.07 commits to in either case.

B2.50 (mating verification) names the detection mechanism Untracked Mating makes unavailable. The relationship is bidirectional: Untracked Mating disables mating verification by producing entities with no pattern records, and mating verification is the mechanism through which Untracked Mating is detected. Running mating verification against all multi-source entities is therefore both a detection protocol and a confirmation that the mating framework is being applied.

---

## 8. Summary

Untracked Mating is the failure mode that arises when the governed mating mechanism B1.10 establishes is bypassed at DNA combination time. Its three forms — ad-hoc combination without pattern selection, unrecorded combination without governance authorization or mating event records, and conflict-ignoring combination that silently resolves parent DNA conflicts — each sever a different piece of the governance infrastructure the deployment depends on. The emergence conditions that produce it are specific and recognizable: copy-paste DNA reuse that does not announce itself as a governance event, governance overhead avoidance that treats the mating framework as optional, and the conflict resolution impulse that converts a governance signal into a silent implementation decision. Detection runs through B2.50 mating verification, A2.40 mating event audit, B2.43 cross-lineage audit, and A1.03 conflict registry inspection. Remediation requires retroactive documentation, retroactive governance authorization, retroactive conflict registration, and structural workflow changes that make mating governance the default path whenever multi-source DNA combination occurs.

---

*This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its contribution is to formalize, as a named anti-pattern with detection and remediation paths, the failure mode that arises when the governed mating mechanism established in B1.10 is bypassed during DNA combination.*
