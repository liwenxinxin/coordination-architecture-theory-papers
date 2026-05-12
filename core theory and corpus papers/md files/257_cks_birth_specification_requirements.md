# Birth Specification Requirements: Decomposing B1.09 Birth as Human-Governed Origination by Formalizing What Must Be Authored and Recorded at Birth for Valid Cell, Aspect, and Self Creation Events

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the birth specification requirements that make a creation event governance-valid at each structural level of a CKS-governed AI Self — cell, aspect, and Self — as those requirements derive from the source paper's lifecycle commitment and its inherited Paper 1 foundations.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern commits to birth as human-governed origination: a new cell, aspect, or Self comes into existence under human governance authority, with its substrate content authored or drafted under human direction. This note formalizes the birth specification requirements that a creation event must satisfy to be governance-valid. The requirements are level-specific: cell birth requires a minimum specification covering DNA layer initial content, carry-strategy choice, Action layer initialization, harness substrate configuration, type declaration, membership assignment, instinct layer configuration, and a birth record with provenance. Aspect birth requires purpose specification, coordination rules, initial cell membership assignments, type declaration, and birth record. Self birth requires integration architecture specification, instinct/reasoning configuration, initial aspect collection, type declaration, and birth record. A birth event is governance-valid if and only if the level-appropriate minimum specification is authored and recorded at the moment of creation; incomplete specification produces an incomplete entity that may fail composition requirements and obscure the lineage starting point. Birth specification is a governance act under A2.04; LLM drafting of specifications is labor under A1.12. The minimum completeness requirements are verifiable through substrate inspection, giving governance a concrete standard against which to evaluate creation events.

---

## 1. Why birth specification requirements need standalone formalization

Paper 2's lifecycle commitment treats birth, mating, and death as governed primitives at every structural level of a CKS Self. Birth is the creation of a new cell, aspect, or Self under human governance. The source paper's §6.2 states the commitment plainly: "Birth's architectural commitment is governance over creation, not labor of creation." This commitment, however, does not by itself specify what a governed birth event must contain. It establishes who holds authority over the creation decision; it does not enumerate what content must be authored and recorded for a creation event to be architecturally complete.

That gap is consequential. A birth event that is governed in the authority sense — humans authorized the creation — but incomplete in the specification sense produces an entity that may not satisfy Paper 1's composition requirements (A1.13), may not provide the lineage starting point that path retraceability (A1.07) requires, and may not carry the substrate content downstream evolution mechanisms operate over. Governance over birth is necessary but not sufficient for governance-valid birth; the completeness of the specification authored at birth is the second required condition.

This note formalizes the birth specification requirements as the architectural completeness standard for governance-valid birth events. It is the fortieth Phase B2 note and opens the five-note B1.09 decomposition arc. B2.41 will treat the birth governance vs. birth labor distinction in detail; B2.42 will formalize birth triggers as an operational treatment; B2.43 will address birth lineage establishment; B2.44 will address birth verification. The present note establishes the specification content that the subsequent notes in the arc presuppose.

---

## 2. Level-specific minimum specifications

Birth specification requirements are level-specific because each structural level carries distinct architectural commitments with distinct substrate content. What must be present at a cell's creation differs from what must be present at an aspect's or a Self's creation. The minimum specification at each level is the set of substrate content items whose absence at birth produces an entity that is incomplete in an architecturally meaningful sense — incomplete not merely by preference but in a way that leaves required structural functions underdetermined.

### 2.1 Cell birth minimum specification

A governance-valid cell birth requires, at minimum, the following to be authored and recorded:

**DNA layer initial content.** The DNA layer carries the cell's stabilized orchestration and behavior substrates. At birth, the initial content of the orchestration substrates, behavior substrates, and schemas must be specified. These do not need to be fully mature — cells evolve after birth — but they must be present as the starting substrate content the cell operates over from its first execution.

**Carry-strategy choice.** Each cell carries either the full Self's DNA with selective expression or a partial slice of it. This carry-strategy is a per-deployment design choice governed by orchestration substrate. At birth, the choice must be made and recorded; an unspecified carry-strategy leaves expression behavior underdetermined.

**Action layer initialization.** The Action layer records task instances and outputs as the cell executes. At birth, the Action layer initializes empty but must be typed as Action and structurally initialized so that subsequent execution populates it in the correct addressable form.

**Harness substrate configuration.** The harness substrate governs which DNA-layer sub-substrates activate for given cell goals. At birth, the harness substrate configuration must be specified: which activation rules govern expression, what the default selection behavior is, and what override conditions apply.

**Type declaration as cell.** The entity's structural type must be recorded at birth. Type declaration is what makes the entity a cell rather than an aspect or a Self in the substrate's governance vocabulary.

**Membership assignment to initial aspects, if applicable.** If the cell is born into one or more aspects, its membership assignments must be recorded at birth. Membership is relational; it is not inferred from the cell's content but explicitly recorded.

**Instinct layer configuration, if not inherited.** The instinct layer configuration — which LLM instance the cell routes to, what routing rules govern that routing — must be specified at birth if not inherited from Self-level configuration. An unspecified instinct configuration leaves the cell's operational behavior underdetermined from the first execution.

**Birth record with provenance.** A birth record satisfying A2.40's six provenance metadata fields must be created at the moment of birth. The birth record is the lineage starting point; it is what makes subsequent evolution traceable back to the cell's origin.

### 2.2 Aspect birth minimum specification

An aspect is a purpose-defined structural arrangement of cells coordinating toward a shared purpose. A governance-valid aspect birth requires:

**Purpose specification.** The aspect's purpose must be stated, scoped, and bounded. Purpose specification covers the purpose statement itself, the scope of work the aspect coordinates over, the constraints on that scope, and the policy governing how purpose evolves over the aspect's lifecycle. An aspect without a recorded purpose specification is structurally present but functionally undefined.

**Coordination rules.** The rules that govern cell coordination within the aspect must be specified at birth: membership rules (which cells may participate and under what conditions), invocation rules (how and when cells are invoked), output-integration rules (how cell outputs combine into aspect-level outputs), and conflict-handling rules (how conflicts arising within the aspect are handled). These rules are the orchestration substrate at the aspect level; they must be present from birth for the aspect to coordinate cells in a governed way.

**Initial cell membership assignments.** The cells that are members of the aspect at birth must be recorded. Membership is explicit substrate content, not implicit.

**Type declaration as aspect.** The entity's structural type must be recorded as aspect.

**Membership assignment to Self, if applicable.** If the aspect is born as a member of an existing Self, that assignment must be recorded at birth.

**Birth record with provenance.** A birth record satisfying A2.40's six provenance metadata fields must be created at the moment of birth.

### 2.3 Self birth minimum specification

A Self is the integrated whole that holds multiple aspects under unified human governance. A governance-valid Self birth requires:

**Integration architecture.** The Self's integration architecture must be specified at birth: the rules governing aspect coexistence, the Self-level operations that cross aspect boundaries, cross-aspect conflict handling rules, cross-aspect integration rules, and the cross-level access configuration that determines when Self-level operations may act directly on cells. This specification defines the topology of governance within the Self.

**Instinct/reasoning configuration.** The instinct/reasoning configuration at the Self level must be specified: which LLM instances serve the instinct function, how the substrate serves the reasoning function, what high-stakes identification logic applies, what verification configuration governs instinct integration, and what mutation governance policies apply. This configuration is load-bearing for the Self's operational integrity from its first execution.

**Initial aspect collection.** The aspects that constitute the Self at birth must be recorded. A Self without a recorded initial aspect collection has no governed internal structure.

**Type declaration as Self.** The entity's structural type must be recorded as Self.

**Birth record with provenance.** A birth record satisfying A2.40's six provenance metadata fields must be created at the moment of birth.

---

## 3. What makes birth specification requirements architecturally distinctive

Conventional AI component creation — agent instantiation in AutoGen, LangGraph, CrewAI, or comparable frameworks — treats creation as configuration-plus-instantiation. Components are created through code or configuration files; the question of what must be specified for a creation event to be architecturally complete is not posed as a formal requirement. What a component needs to operate is what its runtime requires; there is no substrate-resident minimum specification that must be authored at creation for the component to be governance-valid.

CKS makes three moves that depart from this pattern. First, it makes the specification level-specific: the completeness standard is not uniform across all entity types but is differentiated by the architectural function of cells, aspects, and Selves. Second, it makes completeness verifiable through inspection: the required substrate content items are named, enumerated, and substrate-resident, so a governance actor inspecting the substrate at or after birth can determine whether the minimum specification is present. Third, it makes incompleteness consequential in an architectural sense: an entity created without its minimum specification may fail composition requirements (A1.13), may fail to provide the lineage starting point that retraceability (A1.07) requires, and may operate in ways that are not determined by governed substrate content. These three departures together constitute what is architecturally distinctive about CKS birth specification requirements.

---

## 4. The biological analog as conceptual scaffold

The biological vocabulary of birth reflects the source paper's broader use of biological analogy as conceptual scaffold. In biological development, cells form through developmental processes that establish specific gene expression profiles, cellular structures, and functional roles at the moment of formation. Developmental biology recognizes that cells missing required structures are non-viable — developmental completeness has consequences. The CKS birth specification requirements are the architectural analog of developmental completeness requirements.

The analog has an important limit: biological cells cannot govern their own developmental specification. The developmental program is encoded in the genome and executed through molecular processes without external authority architecture. CKS departs from biology at exactly this point. CKS birth specification requirements are authored by humans under governance authority (A2.04), are substrate-resident and inspectable (A2.46), and are recorded with provenance that anchors subsequent retraceability (A1.07, A2.40). The biological analog supplies the conceptual frame — formation completeness has structural consequences — while the architectural substance is specifically CKS: governable, inspectable, authored, recorded.

---

## 5. Inherited Paper 1 commitments

Birth specification requirements inherit directly from the full set of Paper 1's architectural commitments.

**A1.01 (human-governed).** Birth is governed: the creation decision and the authoring of the minimum specification are governed acts. The three governance rights — inspect, modify, override — apply to birth specifications as substrate content from the moment of creation.

**A1.12 (labor allocation).** The governance-over-birth commitment is consistent with labor allocation across all three modes. Humans may author birth specifications directly. LLMs may draft specifications under human direction, with humans governing the authoring decision. Stable cells may populate specification templates under orchestration rules. What the architecture requires is that whatever produced the specification remains subject to human authority before it takes effect as the governing birth content.

**A2.04 (rule authoring).** Birth specification authoring is a rule authoring act in the sense of A2.04: the specification records the governance content that determines the entity's behavior from birth onward.

**A2.46 (Category 4 — substrate-authoritative content).** Birth specifications are substrate-resident authoritative content from the moment of creation. They are not advisory, not configuration files outside the substrate's governance scope, and not implicit. The substrate is what they live in; the substrate is the source of truth about what was specified at birth.

**A2.40 (six provenance metadata fields).** Birth records satisfy A2.40's six provenance metadata requirements. The birth record is the lineage starting point and must carry the provenance fields that make subsequent retraceability possible.

**A1.13 (composition requirements).** The minimum specifications at each level are what enable composition-valid entities. A cell whose DNA layer initial content is unspecified, or an aspect whose coordination rules are absent, does not satisfy the composition requirements that make CKS Selves architecturally coherent.

**A1.07 (path retraceability).** Birth is the lineage starting point. All subsequent evolution — directed selection, action-feedback, instinct evolution — traces back to the entity's birth specification. Birth specification completeness is therefore not merely an initial condition; it is the anchor of the entire retraceability chain.

**A1.10 (determinism contract).** Given a complete birth specification, the entity's behavior from its first execution is determined by governed substrate content. Incomplete birth specifications introduce behavioral underdetermination that the determinism contract does not permit.

---

## 6. Operational implications

**Standard templates per level and type.** Deployments implementing CKS governance define birth specification templates for each cell type, aspect type, and Self type in use. Standard templates encode the minimum specification requirements and reduce the governance cost of verifying completeness at each new creation event. Templates are themselves substrate content, authored under A2.04, and evolve through directed selection as the deployment matures.

**LLM drafting with human approval.** LLMs may generate drafts of birth specifications under human direction per A1.12. Human approval of the draft is the governance act that converts a draft into an authored specification. The approval event carries its own provenance under A2.40.

**Birth specification review as governance event.** Reviewing a birth specification for completeness against the minimum requirements is a governance event, not merely a technical check. It may be performed by the same human who authorized the creation or by a distinct governance actor, depending on deployment policy. The review event and its outcome are substrate-recorded.

**Incomplete birth specifications rejected at governance review.** A creation event whose specification fails the minimum completeness threshold is not governance-valid. Governance review may reject incomplete specifications and require re-authoring before the entity is instantiated. This rejection is substrate-recorded with provenance.

**Template evolution through directed selection.** As a deployment accumulates operational experience, birth specification templates evolve through directed selection per B1.14. Templates that produce better-performing entities, or that reflect refined understanding of what completeness requires in a given context, supersede prior templates under governed template evolution.

**Cross-partner birth.** Where an entity is created for use across organizational boundaries, cross-partner authority requirements apply to the birth specification. The specification must record the authority under which cross-partner creation was authorized.

**Mating-derived specifications.** Birth from mating (B1.10) uses specifications derived from parent entities rather than fully authored from scratch. Mating-derived specifications satisfy the same minimum completeness requirements; their provenance records trace to the parental birth records.

---

## 7. Limits

Birth specification requirements do not prescribe every content detail of the minimum specifications. The requirements define minimum completeness — what must be present — not what the content must say. The DNA layer initial content of a newly created cell must be present; the requirements do not specify what orchestration substrates it must contain beyond the structural initialization minimum.

The requirements do not eliminate human judgment about what constitutes adequate specification in a given deployment context. The architectural minimum is a floor, not a ceiling. Deployments may set higher completeness thresholds for particular entity types or use cases.

The requirements are not static. As deployments mature and deployment standards develop, what counts as a complete birth specification may be extended beyond the architectural minimum through directed selection of standard templates.

The requirements do not prescribe specific implementations. Tool-agnosticism per A1.05 holds. A substrate implemented in any tool that satisfies Paper 1's three minimal requirements can carry birth specifications that satisfy these requirements.

Birth specification is not the same as birth labor. Authoring the minimum specification is a governance act; the labor of drafting that specification may be performed by LLMs. The governance/labor distinction (treated in detail in B2.41) is preserved at the birth specification layer.

Birth specification requirements do not replace post-birth verification per B2.44. The requirements specify what must be present at birth; post-birth verification confirms that what was specified produces the intended architectural behavior over time.

---

## 8. The operational test

A birth event is governance-valid under CKS architecture if and only if, at the moment of entity creation: (a) the level-appropriate minimum specification — cell, aspect, or Self — has been authored and recorded in the substrate; (b) the specification satisfies the content requirements for that level as stated in §2; (c) a birth record with the six provenance metadata fields per A2.40 has been created; and (d) the authoring of the specification was a governance act performed or approved by a human with appropriate authority under A2.04. A birth event that satisfies (a)–(d) is governance-valid regardless of whether a human performed the drafting labor. A birth event that fails any of (a)–(d) produces an entity that may be instantiated but is not governance-valid in the CKS sense.

---

## 9. Standalone formalization and position in the B1.09 decomposition

Naming birth specification requirements as a standalone derivation establishes a formal prior-art boundary around the architectural completeness standard for CKS birth events. The territory being claimed is specific: the level-differentiated minimum specification requirements, the completeness-verifiable-through-inspection commitment, and the governance-act framing of specification authoring — as a composed package applied to the creation of cells, aspects, and Selves under Paper 2's lifecycle architecture.

This note opens the five-note B1.09 decomposition arc within Phase B2. B2.41 will treat the birth governance vs. birth labor distinction as a standalone derivation, taking the governance-not-labor framing introduced here and examining its operational boundaries. B2.42 will address birth triggers — what conditions in a governance-valid deployment warrant a new cell, aspect, or Self creation event. B2.43 will address birth lineage establishment — how the birth record becomes the starting point of the entity's traceable lineage. B2.44 will address birth verification — what post-birth checks confirm that the born entity satisfies its specification. After B2.44, Phase B2 continues into the B1.10 mating decomposition at B2.45–B2.50.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Birth Specification Requirements: Decomposing B1.09 Birth as Human-Governed Origination by Formalizing What Must Be Authored and Recorded at Birth for Valid Cell, Aspect, and Self Creation Events.* May 12, 2026. ORCID: 0009-0004-8065-3235.
