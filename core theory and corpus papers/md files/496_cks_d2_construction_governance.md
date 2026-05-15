# Construction Event Governance Requirements

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

D2.01 is the first Phase D2 operational decomposition note in the CKS derivation series. It derives from D1.01, which commits that the shared substrate's construction is a governed event. This note formalizes what that commitment means operationally: the specific requirements that must be satisfied before and at the moment of construction. Six requirements are identified and grouped into two classes — three pre-construction requirements (joint configuration authorization, initial orchestration rules, joint authority configuration) and three at-construction requirements (construction record, birth-record structure, lineage origin). The satisfaction criterion is stated as a biconditional: a construction is properly governed if and only if all six requirements are present as substrate content before and at the construction timestamp. Partial satisfaction does not constitute a governed construction. The failure mode — a shared substrate that begins operation without these records — is named as the inter-Self analog of Paper 2's Ungoverned Birth anti-pattern (B3.10). Inheritance from Paper 1's path-retraceability commitment (A1.07) and Paper 2's entity birth governance (B1.05/B1.06) is stated.

---

## 1. Position and derivation

D2.01 is the first note in Phase D2 of the CKS Series D derivation. Phase D2 contains operational decompositions of the Phase D1 foundational sub-commitments, following the same structure as Phase B2 in the Series B derivation.

D1.01 commits that the shared substrate's construction is a **governed event** — it is not an implementation detail left to deploying parties, but an architectural commitment with specific conditions that must be met before and at the moment the shared substrate comes into existence. D1.01's commitment is parent to a family of operational questions: What does governed construction require? When must governance be exercised? What records are produced? What constitutes failure?

D2.01 addresses one operational aspect of D1.01: the specific governance requirements that apply to the construction event itself. It does not address the full scope of D1.01 (which also commits to the temporary nature of the shared substrate, its perimeter-spanning property, and its dissolution conditions). D2.01's scope is bounded: it covers what must be true before and at the moment of construction for the construction to count as governed in the Paper 3 sense.

The shared substrate is the architectural object Paper 3 introduces as the medium of inter-Self coordination. Within its scope, the shared substrate carries Paper 1's six architectural commitments — it is human-governed; conflicts within it are first-class; AI operates as mediator; it is tool-agnostic; its composition is linear-cost; the substrate-LLM division is the same hybrid commitment Paper 1 establishes. The perimeter-spanning property is the added commitment at this scope: the shared substrate's governance perimeter spans more than one Self's home governance perimeter. Everything that follows about construction event governance flows from these inherited commitments applied at the moment of the shared substrate's creation.

---

## 2. Three pre-construction requirements

Pre-construction requirements are conditions that must be satisfied and recorded as substrate content **before** the construction timestamp. A shared substrate that reaches operational status without these records present does not satisfy the D1.01 construction-as-governed-event commitment, regardless of what is added later.

### 2.1 Joint configuration authorization

Before a shared substrate can be constructed, the FAI configuration — specifying which aspects each Self contributes, the depth of provenance carry-over at the perimeter, and the persistence policy after the event dissolves — must be authorized by all participating Selves' governance structures. Authorization is not an informal understanding between parties; it is a governance artifact that must exist as substrate content before construction proceeds.

The authorization record must carry: which governance authority within each participating Self authorized the configuration; the timestamp of authorization; and a reference linking the authorization to the configuration content being authorized. This record is the pre-construction warrant for the shared substrate's existence. A shared substrate constructed without it lacks the governance basis for its own creation.

Paper 3's configuration substrate is authored within whichever participating Self holds origination authority for the event — typically the initiating Self under its home governance, with the other participating Selves' governance approving the configuration before construction begins. The approval mechanics are themselves governance-configurable; what is not configurable is the requirement that the authorization record exist as substrate content before construction.

### 2.2 Initial orchestration rules authored

A shared substrate cannot be constructed as an empty container and filled with governance content after it begins operating. Three categories of orchestration rules must be authored as substrate content before the construction timestamp:

**Conflict-handling orchestration rules for the resolve tier.** The resolve tier of Paper 3's three-tier conflict-handling mechanism operates through human-authored orchestration rules that govern how conflicts within the shared substrate are addressed when preservation alone is insufficient. These rules must exist before the shared substrate begins accepting content, because conflicts may surface immediately upon contribution of aspects from participating Selves.

**Hand-off boundary configuration.** The configuration governing what content may flow from the shared substrate back into each participating Self's home substrate at dissolution must be authored before construction. Content that enters the shared substrate during the FAI event may need to return to home substrates; the governance rules for that return are a precondition for the shared substrate's operation, not an afterthought.

**Sharing scope for each participating Self.** For each participating Self, governance must specify which aspects are contributed, at what provenance depth, and under what content-domain restrictions. This is the Dimension 1 configuration commitment from Paper 3 Claim 5. Without it, the shared substrate lacks the authority basis for accepting contributions from participating Selves.

These three categories represent the minimum orchestration content for a shared substrate to operate as a governed object. Deploying parties may author additional orchestration rules; these three are the floor.

### 2.3 Joint authority configuration specified

The specification of how joint authority over the shared substrate will be exercised during operation must be authored as substrate content before construction. Joint authority is the property that makes the shared substrate's governance perimeter span multiple organizational boundaries — it is not a background property but an explicitly configured architectural commitment.

The joint authority configuration specifies: which governance actors from each participating Self hold authority during operation; under what conditions each actor's authority applies; how conflicts between the governance positions of different participating Selves are handled at the governance level (distinct from conflicts within the substrate's coordination content); and what escalation pathway applies if joint authority cannot resolve a governance-level disagreement.

This requirement flows from Paper 1's human-governed commitment applied at the inter-Self perimeter. Paper 1 commits that humans retain the right to inspect, modify, and override substrate content and orchestration rules at any time. At the inter-Self scope, that commitment must specify which humans hold those rights and how they exercise them jointly. The joint authority configuration is the artifact that instantiates Paper 1's governance commitment at inter-Self scope.

---

## 3. Three at-construction requirements

At-construction requirements are conditions that must be satisfied and recorded **at the moment of construction**, producing governance artifacts that establish the shared substrate's existence with full provenance from origination.

### 3.1 Construction record

The construction event is recorded as substrate content with full provenance. Following Paper 1's path-retraceability commitment (A1.07), the construction record must carry six provenance metadata fields applied to the construction event as a whole:

- which Selves are participating in the shared substrate
- the construction timestamp
- references to the pre-construction authorization records (requirement 2.1) establishing the governance warrant for construction
- the initial configuration as it existed at the moment of construction
- the identity of the governance authority under which construction proceeded
- the version or instance identifier establishing this shared substrate's uniqueness within its participating Selves' records

The construction record is not a summary of what happened; it is the authoritative substrate-content artifact establishing that the shared substrate exists, when it came into existence, under whose authority, and what its initial state was. All subsequent governance events within the shared substrate are recorded relative to this anchor.

### 3.2 Birth-record structure

The construction event produces a record analogous in structure to Paper 2's entity birth record (B1.05/B1.06) — a governance artifact that establishes the shared substrate's existence with provenance from origination.

Paper 2's entity birth governance commits that a new cell, aspect, or Self comes into existence when humans authorize its creation, with the birth record establishing the entity's governance history from that moment forward. D2.01 extends this commitment to the shared substrate's creation at inter-Self scope. The shared substrate's birth record carries the same structural commitments: it is a substrate-content artifact; it is produced at the moment of creation; it establishes the governance basis for everything that follows within the shared substrate's operation; and it is the starting point of the shared substrate's provenance chain.

The inter-Self extension adds one property the intra-Self birth record does not require: the birth record must be accessible within each participating Self's governance records, not only within the shared substrate itself. Because the shared substrate's existence spans multiple organizational boundaries, the record of its creation must be present where each participating Self's governance can access it.

### 3.3 Lineage origin established

The shared substrate's provenance chain is established at construction. All subsequent governance events within the shared substrate — conflict preservations, conflict resolutions, escalations, configuration changes, content contributions from participating Selves — can be traced back to the construction record as the lineage origin.

This requirement instantiates Paper 1's path-retraceability commitment at the shared substrate scope. Path retraceability commits that every decision and output within a substrate is linkable to the substrate content and orchestration rules that authorized it. For the shared substrate, this chain begins at the construction record. A shared substrate whose subsequent governance events cannot be traced to a construction record has broken the path-retraceability commitment at the moment it began operating.

Establishing the lineage origin at construction is not a logging requirement; it is an architectural requirement. The provenance chain that supports later audit, later FAI events that reference this event, and governance accountability across organizational boundaries requires that the chain begin at a well-formed origination record.

---

## 4. The satisfaction criterion

**A construction is properly governed if and only if all six requirements are met as substrate content before or at the construction timestamp.**

The biconditional is the prior-art claim. Each direction carries distinct content:

**If all six requirements are met, then the construction is properly governed.** A shared substrate whose pre-construction authorization exists, whose minimum orchestration rules are authored, whose joint authority configuration is specified, whose construction record carries full provenance, whose birth-record structure follows Paper 2's entity birth pattern, and whose lineage origin is established at construction — this shared substrate satisfies the D1.01 construction-as-governed-event commitment. All of Paper 3's subsequent operational commitments (conflict-handling, configuration management, evolution feed) may proceed from this foundation.

**If the construction is properly governed, then all six requirements are met.** A shared substrate that begins operation with any of the six requirements absent is not a governed shared substrate in the Paper 3 sense, regardless of how closely it approximates Paper 3's architecture in other respects. Partial satisfaction does not constitute governed construction. A shared substrate with a construction record but no pre-construction authorization lacks the governance warrant for its own existence. A shared substrate with authorization records but no initial orchestration rules has a governance warrant but no governance machinery. Each requirement is individually necessary; together they are sufficient.

---

## 5. The anti-pattern: ungoverned construction

A shared substrate that begins operation without satisfying the six requirements is the inter-Self scope analog of Paper 2's Ungoverned Birth anti-pattern (B3.10).

In Paper 2's intra-Self scope, Ungoverned Birth names the failure mode in which a cell, aspect, or Self comes into existence without a governance record of its creation — no authorization, no birth record, no provenance from origination. The entity may function; its function is simply not governed at the moment it matters most, which is the moment of creation. Subsequent governance actions cannot repair the absence of a birth record; they can only add records to an entity whose origin is already ungoverned.

At inter-Self scope, the analog is a shared substrate that begins accepting contributions and producing coordination outputs before the pre-construction authorization is complete, before initial orchestration rules are authored, or before the construction record is produced. The consequences are structurally identical: the shared substrate may function; its function is not governed from origination; subsequent records cannot establish a provenance chain that begins from a governed creation. The path-retraceability commitment (A1.07) is broken from the start.

Three variant forms of ungoverned construction are identifiable:

**Form 1 — Missing pre-construction authorization.** The shared substrate is constructed and begins operating before all participating Selves' governance structures have authorized the configuration. This variant breaks the joint authority commitment: the shared substrate operates with content from Selves whose governance has not endorsed the configuration under which that content enters.

**Form 2 — Absent initial orchestration rules.** The shared substrate is constructed with the authorization record present but without minimum orchestration rules authored. Conflicts that surface within the shared substrate have no governance machinery to handle them; the conflict-handling tier either fails silently or defaults to ungoverned behavior.

**Form 3 — Construction without record.** The shared substrate begins operating without a construction record. Even if pre-construction requirements were satisfied informally, the absence of a construction record means there is no provenance anchor from which subsequent governance events can be traced. The shared substrate is operationally present but architecturally invisible to the provenance chain.

---

## 6. Inheritance from Papers 1 and 2

D2.01 does not introduce novel governance commitments; it applies existing commitments from Papers 1 and 2 to the shared substrate's construction event.

**From Paper 1, A1.07 (path retraceability).** The six provenance metadata fields Paper 1 commits to for all substrate content apply to the construction record (requirement 3.1). The path-retraceability commitment is what makes the construction record more than a log entry: it is the anchor for the full provenance chain the shared substrate carries throughout its operation.

**From Paper 1's human-governed commitment.** The three rights — inspect, modify, override — must be instantiated across the inter-Self perimeter at the moment of construction. The joint authority configuration (requirement 2.3) is the artifact that carries this instantiation. Without it, the human-governed commitment exists at the participating Selves' home perimeters but has no specified form at the shared substrate's inter-Self perimeter.

**From Paper 2, B1.05/B1.06 (entity birth governance).** Paper 2's commitment that every lifecycle creation event produces a governance artifact with provenance from origination is the architectural precedent for the shared substrate's birth-record structure (requirement 3.2). The inter-Self extension generalizes the intra-Self birth record from a single-Self governance artifact to a multi-Self governance artifact accessible across all participating Selves' home governance records.

The derivation direction is: Paper 1 establishes provenance requirements for all substrate content; Paper 2 applies those requirements to entity lifecycle events as birth records; Paper 3 applies the same requirements to the shared substrate's construction event as the inter-Self-scope extension of entity birth governance.

---

## 7. Operational test

For any deployed shared substrate, an observer applying the following test can determine whether its construction was governed:

**Step 1.** Locate the construction timestamp — the moment at which the shared substrate first accepted operational content from any participating Self.

**Step 2.** Check for pre-construction authorization (requirement 2.1): Is there a substrate-content record, dated before the construction timestamp, showing that each participating Self's governance structure authorized the FAI configuration? Does the record identify who authorized, when, and under what governance authority?

**Step 3.** Check for initial orchestration rules (requirement 2.2): Are the conflict-handling rules for the resolve tier, the hand-off boundary configuration, and the sharing scope for each participating Self present as substrate content, dated before the construction timestamp?

**Step 4.** Check for joint authority configuration (requirement 2.3): Is there a substrate-content specification, dated before the construction timestamp, stating how joint authority over the shared substrate is exercised during operation?

**Step 5.** Check for the construction record (requirement 3.1): Is there a substrate-content record at the construction timestamp carrying all six provenance metadata fields — participating Selves, timestamp, authorization references, initial configuration, authorizing governance identity, and instance identifier?

**Step 6.** Check for birth-record structure (requirement 3.2): Is the construction record structured as a governance artifact establishing the shared substrate's existence from origination, and is it accessible within each participating Self's governance records?

**Step 7.** Check for lineage origin (requirement 3.3): Is the construction record referenced in the provenance chains of subsequent governance events within the shared substrate? Can any subsequent governance event within the substrate be traced back to this record?

If the answer to any of these checks is no, the shared substrate's construction was not governed in the D2.01 sense, regardless of how it operates subsequently. The satisfaction criterion is biconditional: all six requirements, present as substrate content at or before the construction timestamp, are both necessary and sufficient.

---

## References

Li, W. (April 2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* Independent publication.

Li, W. (April 2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* Independent publication.

Li, W. (April 2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* Independent publication.
