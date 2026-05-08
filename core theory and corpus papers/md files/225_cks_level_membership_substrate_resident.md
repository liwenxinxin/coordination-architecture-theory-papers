# Level-Membership as Substrate-Resident Authoritative Content in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one operational property the three-level structure (B1.02) depends on: that **level-membership** — the answer to *which artifacts participate as cells in this Self*, *which cells are members of which aspects*, *which aspects are facets of this Self* — is itself substrate-resident authoritative content under A1.08 + A2.46 (Category 4: what rules apply), and is therefore a first-class architectural artifact subject to the inspect, modify, and override rights (A2.01–A2.03), authored through rules (A2.04), and recorded with provenance (A2.40).

## Abstract

Paper 2 commits the architectural Self to three levels — cell, aspect, and Self — with multi-level composition under unified human governance and relational structural roles per B1.17. The companion B2.07 note formalizes the *level-distinct scope* property of those three levels. This note formalizes a different operational property the three-level structure depends on: that **level-membership** records — which artifacts participate at which levels — exist in substrate as authoritative content rather than as implicit deployment configuration. Membership assignments are authored through rules per A2.04, changes recorded with A2.40 six-field provenance, and the records subject to A2.01 inspect, A2.02 modify, and A2.03 override at any time. The substrate-resident character of membership is what makes structural arrangement governable — what makes vertical evolution per B1.16 architecturally available, what makes audit reconstruct historical structure, and what makes multiple-aspect participation per B1.17 concretely operationalizable as multiple membership records per artifact. The note states the property precisely, distinguishes membership records from artifact identity, locates the property within Paper 1's inherited commitments, names operational implications, and bounds the claim against seven common misreadings.

## 1. Why level-membership needs to be formalized as standalone

Paper 2's three-level structure (B1.02) is one of Claim 2's two architectural moves — multi-level composition under unified human governance, with relational role membership rather than intrinsic structural binding (§5.2). The companion B2.07 note formalizes *level-distinct scope* — the property of *what each level does*. Level-membership — the property of *which artifacts are at which level* — is separable, and two facts about it justify a standalone treatment.

First, in conventional AI architectures the structural arrangement of components is typically implicit deployment configuration — orchestrator wiring, framework initialization, registry tables, container labels — none of which is governable substrate content in the CKS sense. The structure is real, but it is not architecturally addressable as something humans can inspect, modify, and override under the human-governed commitment.

Second, several Paper 2 commitments depend operationally on the structural arrangement being a governable artifact. Vertical evolution per B1.16 — restructuring by reassigning cells across aspects, splitting, merging, dissolving — operates on membership records; without substrate-resident records, the operations have no authoritative artifact to act on. Multiple-aspect participation per B1.17 — same cell, several aspects, governance propagating per arrangement — requires the arrangement be specifiable as content; if membership is intrinsic to the artifact, the relational property cannot be expressed.

Naming level-membership as substrate-resident authoritative content gives downstream implementers a precise specification of what the structural arrangement must be — content under A1.08, governed under A2.46 Category 4, authored through A2.04 rules, recorded with A2.40 provenance — and prevents the slide into deployment-configuration substitutes.

## 2. The property, stated precisely

In CKS, **level-membership records** are substrate-resident authoritative content recording which artifacts participate at which levels of a Self. The records have four operational components.

**(a) The records exist in substrate per A1.08.** Membership records are substrate content of the same kind as decisions, rationale, and authority assignments. Reading the substrate yields the answer to *which cells are members of which aspects* and *which aspects are facets of which Selves*; reading any other location is not authoritative for these questions.

**(b) The records fall under A2.46 Category 4 — what rules apply.** Membership specifies which architectural rules apply to a given artifact in a given level position. A cell whose membership record places it in aspect *A* operates under aspect *A*'s orchestration rules in that role; the same cell with a second record placing it in aspect *B* operates under aspect *B*'s rules in *that* role. The substrate is authoritative for the rule-applicability question that membership answers.

**(c) Assignments are authored through rules per A2.04.** Membership rules are substrate content authored by humans (LLM-drafted rules subject to human authority before they take effect are admissible). Rules may be specific (this cell is a member of aspect *A*) or pattern-based (cells matching property *P* are members of aspect *A*); both forms are substrate-resident authoritative content under the same governance commitments.

**(d) Changes are recorded with A2.40 six-field provenance.** When membership changes — added, removed, reassigned — the change is recorded as substrate content with the six provenance fields A2.40 specifies: who authored the change, when, under which rule, what the previous membership was, the rationale, and the authority basis. Membership history is preserved per A6.02 retroactivity.

Failing any one of (a)–(d) — even with the others robustly satisfied — fails the property architecturally and shifts the structural arrangement into implicit configuration the architecture cannot govern.

## 3. Membership is not artifact identity

A common conflation has to be ruled out at the start. **Level-membership is not artifact identity.** The artifact has its own substrate content — its DNA layer (orchestration substrates and behavior substrates per B1.06–B1.07), its action layer (recorded task instances), its harness substrate, its lineage. Membership is the *relational assignment* of the artifact to a level position; it is recorded *about* the artifact, not *as* the artifact. Two operational consequences follow.

First, the same artifact bears multiple membership records simultaneously. A clinical-data cell carrying a patient cohort's longitudinal information may have membership records placing it in the clinical-care-delivery aspect, the regulatory-and-quality-reporting aspect, the financial-and-operations aspect, and the institutional-learning aspect. The artifact is one; the membership records are four; each carries its own provenance and falls under the orchestration rules of its target aspect. This is what operationalizes B1.17's relational structural roles concretely.

Second, changing membership does not change the artifact. A cell reassigned from aspect *A* to aspect *B* retains its substrate content; what changes is the membership record. The cell's DNA layer, action layer, and lineage are not edited by the reassignment. This is what makes vertical evolution per B1.16 a substrate-edit operation rather than the kind of extensive often-lethal genetic rewiring biology requires for body-plan change at the species level.

## 4. What makes the substrate-resident character architecturally distinctive

Conventional AI architectures often have *implicit* membership: a component is "in the orchestrator" through configuration that is not specified as governable architectural content. CKS makes membership *explicit* first-class architectural content. Three downstream properties follow.

**Auditability.** Because membership records are substrate content with A2.40 provenance, audit can reconstruct *what was a member of what at any historical point* by reading the substrate. The retroactivity commitment A6.02 preserves historical membership across rule changes; the retraceability commitment A1.07 makes the trace coherent across composition operations. A reviewer answers "which cells were in this aspect last quarter" the same way they answer any other coordination question — by reading the substrate.

**Evolvability.** Because membership records are substrate content, vertical evolution per B1.16 operates as a substrate-edit operation under orchestration rules. Reassigning cells across aspects, splitting an aspect into two, merging two aspects, or dissolving an aspect are all rule-governed reorganizations of membership records. The architectural commitment is what makes restructuring a routine operational property rather than an exceptional re-architecture event.

**Inspectability and revisability.** Auditors and reviewers exercising the inspect right (A2.01) read the structural arrangement directly from the substrate, without depending on framework introspection or vendor tooling. Humans exercising the modify right (A2.02) and the override right (A2.03) change membership through rule authoring per A2.04 or direct override; structural arrangements are revisable at any time, not only at scheduled re-architecture checkpoints.

These properties are not new commitments; they follow from treating membership as having the same architectural status as any other Category 4 substrate content.

## 5. The biological analog as conceptual scaffold

Biological tissues and organs maintain membership through molecular markers — a hepatocyte "knows" through surface molecules and gene-expression state that it is part of liver tissue; cells migrate, differentiate, and assemble into organs through developmental programs. The biological analog is useful as conceptual scaffold for what membership records make architecturally available: a recorded answer to *what is part of what*, alongside the cell rather than embedded in it.

The architectural substance is not the analogy. CKS exceeds biology in two respects relevant to the architectural claim. First, CKS membership is *relational* per B1.17 — the same artifact participates in multiple aspects, supported concretely as multiple membership records per artifact; biological cells typically belong to one tissue at a time, and molecular-marker schemes are not designed for multi-membership. Second, CKS membership is *governable on operational timescales* — humans modify membership through rule authoring or direct override, with the change taking effect as substrate state; biological membership evolves only through development and disease, on timescales the organism cannot route around.

## 6. Inherited Paper 1 commitments

Level-membership as substrate-resident authoritative content does not introduce commitments outside Paper 1's specification; it composes inherited commitments in a specific configuration. Membership records are substrate content per A1.08 and fall under A2.46 Category 4 (what rules apply to which artifact in which level position). Membership rules are authored under human authority per A2.04 (LLM-drafted rules subject to human authority before they take effect are admissible). Membership changes are recorded with A2.40 six-field provenance, with history preserved per A6.02 retroactivity and reconstructible per A1.07 retraceability. The records are subject to A2.01 inspect, A2.02 modify, and A2.03 override at any time. Authority for membership changes is itself substrate content per A2.47 (Category 5: who has what authority); cross-partner membership requires cross-partner authority. The note's contribution is the configuration in which these commitments compose to make level-membership a first-class architectural artifact, not a new commitment beyond them.

## 7. Operational implications

Six implications follow from the substrate-resident character of level-membership.

**Deployments configure structure through rules.** Per-deployment structural arrangement is produced during birth (B1.09) by authoring membership rules — explicit cell specifications, aspect membership rules, Self composition rules — under human authority. Rule variety is bounded by the deployment's structural needs; per-element membership review is not required.

**Specific and pattern-based rules coexist.** Specific rules ("this cell is a member of aspect *A*") are appropriate for individual exceptions or small deployments; pattern-based rules ("cells matching property *P* are members of aspect *A*") are operationally efficient for large deployments. Both are substrate-resident authoritative content under the same governance commitments.

**Multi-aspect participation operationalizes as multiple records.** A cell participating in *n* aspects has *n* membership records, each with its own provenance and rule reference. Governance properties propagate per arrangement rather than per cell, exactly as B1.17 commits.

**Vertical evolution modifies records.** Restructuring operations (reassigning, splitting, merging, dissolving) are substrate edits over membership records under orchestration rules, leaving the artifacts themselves unchanged.

**Audit reads the records.** Reconstructing structural arrangement at any historical point is a substrate read against the membership records, with A2.40 provenance making the trace coherent.

**Cross-partner membership requires cross-partner authority.** When a cell from one composition partner is to be a member of an aspect from another partner, A2.47 authority distribution must include authority spanning the partners. Without such authority, cross-partner membership cannot be authored — the multi-author rule-authoring conflict treatment (A6.12) applies.

## 8. What the property does NOT entail

Seven misreadings have to be ruled out to keep the standalone framing precise.

**It does not override artifact identity.** The artifact has its own substrate content; membership is the relational assignment, not a redefinition of the artifact.

**It does not bypass governance.** Membership assignments are authored under human authority per A2.04; rules are not exempt from inspect, modify, and override.

**It is not permanent.** Membership evolves under B1.16 vertical evolution and under A2.03 override; the substrate-resident character is what makes evolution possible, not a guarantee of stability.

**It does not prescribe specific membership patterns.** The architectural commitment is that membership is substrate-resident authoritative content; *which* memberships a deployment configures is a deployment design decision under that commitment.

**It does not replace cell-level work.** Cells still do cell-level processing regardless of which aspects they are members of. Membership specifies relational arrangement; it does not absorb the work cells do at cell scope.

**Membership records are not the artifacts themselves.** They are records *about* artifacts; reading a membership record yields a relational fact, not the cell's DNA layer or action layer.

**Membership is not the only inter-level relationship.** Content-domain operations (higher levels operating over lower levels as content domain) and cross-level access (Self accessing cells directly when purpose requires, per the non-strict-hierarchy property) are also relationships the three-level structure carries. This note formalizes the membership relation specifically.

## 9. The one-sentence test

A system implements the level-membership-as-substrate-resident commitment if and only if, at any time during the substrate's existence, *which artifacts participate at which levels* can be answered by reading substrate content authored under A2.04 rules and recorded with A2.40 provenance, and the answer can be inspected, modified, and overridden under A2.01–A2.03 without scheduling, approval, or runtime intermediation.

A system that fails this test may handle structural arrangement in some other way and may be useful, but does not treat level-membership as substrate-resident authoritative content in the CKS sense, and downstream work that relies on its structural-governance guarantees should be scoped accordingly.

## 10. Why naming as standalone matters

Treating level-membership as substrate-resident authoritative content rather than as implicit deployment configuration is what makes the three-level structure architecturally complete. Without this property, the structure of the system sits outside the human-governed commitment — visible at deployment time, perhaps editable through redeployment, but not governable as substrate state under the inspect, modify, and override rights humans hold over everything else the substrate carries. With this property, the structure of the system joins decisions, rationale, authority, and conflicts as content the substrate is authoritative for, governed under the same architecture as the rest.

This note is the second of four formalizing the three-level structure (B1.02). B2.07 formalized level-distinct scope; B2.09 will formalize the operational mechanisms by which the three levels remain distinguishable in practice; B2.10 will formalize the level-instantiation patterns through which deployments produce concrete three-level Selves. After B2.10 closes the B1.02 decomposition, Phase B2 turns to the cell level (B1.03) for similar standalone treatment of the DNA-layer and action-layer distinctions.

Subsequent work that adopts Paper 2's three-level structure, extends it, composes it with adjacent patterns, or argues against it should treat level-membership as substrate-resident authoritative content in the sense formalized here. Work that uses the term differently — most often by treating structural arrangement as deployment configuration outside the substrate's governance — is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: A Multi-Level Architectural Pattern for AI Systems Beyond the LLM.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Level-Membership as Substrate-Resident Authoritative Content in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
