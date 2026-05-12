# Same Entity at Multiple Levels: Formalizing Multi-Role Occupancy in the CKS Relational Architecture

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the precise meaning and governance requirements of same-entity-at-multiple-levels as that architectural possibility is entailed by Paper 2's commitment to relational structural roles.

## Abstract

Paper 2 of the Coordination Knowledge Substrate (CKS) theory series establishes that structural level membership is relational rather than intrinsic: the same underlying substrate artifact participates as a cell in one arrangement, as part of an aspect in another, or as a component of different aspects simultaneously, depending on what the structure is for. This note formalizes an immediate architectural consequence of that commitment — same-entity-at-multiple-levels — as a standalone derivation (note B2.86, third of five notes decomposing B1.17). Because level determination is relational and purpose-defined rather than intrinsic, the same substrate entity can occupy roles at different structural levels. This manifests as two distinct scenarios: in different deployment contexts, where the same artifact receives different level determinations in different deployments, each independently authored; and simultaneously within one deployment, where the same entity occupies cell and aspect roles concurrently. The second scenario is architecturally more complex: it requires explicit governance authorization per A1.01, a separate complete level determination record for each level role per B2.85, composition validity at each level independently per A1.13, and Paper 1 commitments applied at each level scope per B1.20. The note distinguishes multi-level occupancy from the shared-cells pattern established in B1.03, articulates the biological analog as conceptual scaffold, identifies the inherited Paper 1 commitments that apply, and specifies the limits that multi-level does not override.

---

## 1. Why same-entity-at-multiple-levels requires standalone formalization

Paper 2 commits to relational structural roles: the same underlying CKS artifact participates in different structural arrangements, with the role it occupies at each level inhering in the arrangement rather than in the artifact. B2.84 (the relational roles integrating frame) established the general case. B2.85 (purpose-defined level determination) established that level determination is deployment-specific authored content, not a fixed property of the artifact. These two notes together make an architectural consequence visible that requires its own formalization: if level determination is relational and purpose-defined, then the same substrate entity can, in principle, occupy roles at different structural levels — either across separate deployments or, more remarkably, simultaneously within a single deployment.

This consequence is not a curiosity. It is architecturally distinctive: conventional AI component architectures do not permit this. A model in a conventional AI system is always a model; a service orchestrator is always a service orchestrator. The type of a component is fixed at design time, intrinsic, and exclusive. CKS's relational architecture opens the possibility of multi-level role occupancy — not as an arbitrary relaxation, but as a governed architectural property that follows directly from the relational commitments Paper 2 defends.

Without a standalone formalization, the governance requirements for multi-level occupancy remain implicit, the distinction from within-level shared cells (B1.03) remains undrawn, and the two scenarios — different contexts versus simultaneous within one deployment — remain conflated. B2.86 supplies the missing specificity. Its position as the eighty-sixth Phase B2 note and the third in the B1.17 decomposition sequence reflects its role: it extends what B2.84 and B2.85 established into the operationally most complex case the relational role commitment generates.

---

## 2. The architectural specification: two scenarios

**Scenario 1 — Different deployment contexts.** The same substrate artifact — the same CKS object with its substrates, orchestration rules, and architectural commitments — receives different level determinations in different deployments. In deployment A, governance determines the artifact to be a cell performing a specific informational task. In deployment B, governance determines the same artifact to be an aspect coordinating other cells toward a particular purpose. Both determinations are valid. Neither overrides the other. Each is authored independently as deployment-specific substrate content per A2.04, in its respective deployment's substrate.

This scenario is architecturally natural given B2.85's commitment that level determination is deployment-specific authored content, not an intrinsic property of the artifact. The artifact's underlying capabilities are what they are; different deployments can put those capabilities to different structural uses. Each deployment independently governs what level the artifact occupies within that deployment's composition.

**Scenario 2 — Simultaneous multi-level within one deployment.** The same substrate entity simultaneously occupies roles at different structural levels within a single deployment. The clearest instance: an entity that (a) performs specific informational tasks as a cell within one aspect, and (b) coordinates other sub-cells as an aspect for another coordinated purpose. This entity would be determined as both a cell — relative to the higher aspect that includes it — and an aspect — relative to the cells it coordinates. Its role at each level is real and concurrent; neither determines the other; both are active within the same deployment simultaneously.

This scenario is architecturally possible because roles are relational: the entity's role depends on what it relates to, not on what the entity intrinsically is. Relative to the higher structure including it, it is a cell. Relative to the sub-cells it organizes, it is an aspect. Both relations hold simultaneously within the same deployment.

The governance requirements for Scenario 2 are more demanding than those for Scenario 1:

- **Explicit governance authorization per A1.01.** Simultaneous multi-level occupancy must be explicitly authorized by the humans holding governance authority over the deployment. The three governance rights — inspect, modify, override — apply to the multi-level configuration itself. Governance authorization is not assumed; it is authored.

- **Separate complete level determination records per B2.85.** Each level role requires its own complete level determination record in the deployment's substrate. The cell-level determination and the aspect-level determination are distinct authored events, each with its own provenance per A2.40. A single determination record cannot carry both roles.

- **Composition validity at each level independently per A1.13.** The composition requirements that A1.13 specifies must be satisfied at each level scope independently. The entity's participation as a cell must satisfy cell-level composition requirements. Its operation as an aspect must satisfy aspect-level composition requirements. Cross-level composition interactions — places where the entity's cell-role and aspect-role interact — must themselves be governed. Multi-level occupancy does not relax A1.13; it multiplies its application.

- **Paper 1 commitments at each level scope per B1.20.** When the entity occupies multiple level roles, Paper 1 commitments apply at each scope independently. As a cell, cell-level commitments apply — the same commitments Paper 1 defends at cell scope. As an aspect, aspect-level commitments apply — the same governance-boundary inheritance and substrate-mediated composition requirements. The commitments at different scopes are independent applications, not contradictions. They stack.

---

## 3. What makes multi-level role occupancy architecturally distinctive

The contrast with conventional AI component architectures is informative. In conventional architectures, components have fixed types determined at design time. A model is a model. A service orchestrator is a service orchestrator. A database is a database. These type assignments are intrinsic and exclusive: a component cannot simultaneously be a model and an orchestrator within the same deployment, because the type determines the component's structural function and that function is built into the component's implementation.

CKS's relational architecture inverts this. The artifact carries no intrinsic level assignment. The artifact's role is determined by the structural arrangement that calls on it and by the governance decisions that author that arrangement. This means the same artifact can be called on in different structural roles in different arrangements. Multi-level occupancy is the most complex instance of this architectural property: the artifact is called on in two different structural roles simultaneously within one deployment, and both callings are genuine, governed, and concurrent.

This is not architectural permissiveness. Governance authorization requirements, composition validity requirements at each level, separate determination records, and level-specific Paper 1 commitments together make multi-level occupancy governed, not arbitrary. The architecture enables it; governance controls whether and how it occurs.

---

## 4. The biological analog and its limits

Biology offers a conceptual scaffold for multi-level role occupancy. Certain biological structures serve simultaneously as functional units at one organizational level and as coordinators of sub-structures at another. A liver cell is a functional unit executing specific biochemical tasks within the liver, but it also coordinates internal sub-cellular processes — organelles and metabolic pathways — that serve the cell's own coordinated purposes. An organ is a functional unit within the body serving systemic purposes, and also the coordinator of its constituent cellular architecture. The same biological entity occupies roles at multiple levels of biological organization simultaneously.

The analog functions as conceptual scaffold for what makes multi-level role occupancy coherent: the same entity can genuinely bear multiple organizational roles when those roles are defined relationally by the organizational structures that include or are included by the entity. The roles are not in conflict; they are perspectives from different organizational stances on the same underlying entity.

The architectural substance of B2.86 is not derived from biology, however. It is derived from Paper 2's relational roles commitment and the governance requirements that apply to multi-level occupancy within a human-governed substrate. Biology has no governance authorization requirement, no determination record authoring, no composition validity test at each level. The biological analog illustrates the conceptual possibility; Paper 2's architecture specifies the governed form that possibility takes in CKS.

---

## 5. Inherited Paper 1 commitments

Multi-level role occupancy operates within the full inheritance structure Paper 2 carries from Paper 1. The following inherited commitments bear directly on B2.86:

**A1.01 (human-governed).** Multi-level role occupancy within one deployment requires explicit governance authorization. The three governance rights — inspect, modify, override — apply to each level role the entity occupies and to the cross-level configuration as a whole.

**A1.13 (composition requirements).** Composition requirements apply at each level scope independently. Multi-level occupancy satisfies A1.13 at each level, not merely at one level or as an aggregate. Cross-level composition interactions must be governed.

**B1.20 (recursive Paper 1 commitments).** Paper 1 commitments apply at each level scope where the entity has a role. As a cell, the entity is governed by cell-level Paper 1 commitments. As an aspect, it is governed by aspect-level Paper 1 commitments. These are independent applications of the same commitments at different scopes.

**A2.04 (rule authoring).** Each level determination is authored as deployment-specific substrate content. Multi-level occupancy requires that both determinations are authored, not inferred or assumed.

**A2.47 (authority distribution).** Multi-level authority must be explicitly specified. If the entity participates in a cross-partner deployment, cross-partner authority at each level must be governed per A2.47.

**A2.40 (provenance).** Each level determination event is recorded with provenance in the substrate. Multi-level determination events are distinct provenance-carrying records.

---

## 6. Operational implications

**Explicit multi-level authoring.** Deployments that require an entity to occupy roles at multiple levels must explicitly author both level determinations as substrate content. There is no implicit multi-level designation. The governance act of authoring both determinations is the operational moment at which multi-level occupancy is established.

**Governance complexity.** Multi-level role occupancy involves more governance than single-level assignment. Governance requirements apply at each level — each level determination must be authored, each level composition must be validated, each level's Paper 1 commitments must be actively maintained. Deployments should weigh this complexity against the architectural flexibility multi-level occupancy provides.

**Composition validation at each level.** Each level role must independently satisfy A1.13. Deployment governance must validate composition at each scope, not only at the level most visible in the deployment's primary purpose. Failure to satisfy composition requirements at either level is a governed violation regardless of satisfaction at the other level.

**Inspectability at each scope per A2.01.** Multi-level entities are inspectable at each level scope. The governance inspect right extends to both level roles the entity occupies. Humans exercising the inspect right over the deployment can examine the entity's cell-level participation and its aspect-level coordination as distinct but both available inspection surfaces.

**Level-specific evolution governance.** When a multi-level entity evolves, evolution at one level scope does not automatically propagate to the other level scope. Cell-level evolution is governed through cell-level evolution governance. Aspect-level evolution is governed through aspect-level evolution governance. The two evolution paths are independent; cross-level evolution propagation, if intended, requires explicit governed authorization.

---

## 7. Limits

**Multi-level does not eliminate level distinctions.** An entity occupying roles at multiple levels does not cause the levels to collapse. Cell-level and aspect-level commitments remain distinct architectural scopes even when one entity occupies both. The entity holds both roles; it does not unify the levels into a single undifferentiated scope.

**Multi-level is not the same as shared cells.** B1.03 established that cells can be shared across aspects at the same level — one cell participating in multiple aspects, all as cell-level membership. Shared cells are within-level multi-membership: the entity occupies cell roles in multiple aspects, but all those roles are at the same structural level. Multi-level occupancy crosses levels — the entity occupies cell and aspect roles simultaneously, or aspect and Self roles. The two patterns are distinct. Shared cells do not require the multi-level governance requirements specified in §2.

**Multi-level may be rare in practice.** Governance complexity may make simultaneous multi-level occupancy uncommon in operational deployments. Most deployments may prefer entities with single level assignments for governance simplicity. The architectural possibility is real; its frequency in practice is a deployment decision, not an architectural mandate.

**A1.13 applies at each level independently.** Multi-level occupancy does not relax, aggregate, or trade off composition requirements across levels. Satisfying A1.13 at the cell level does not satisfy it at the aspect level. Both must be independently satisfied.

**Different contexts is not simultaneous multi-level.** Scenario 1 (same artifact, different deployments, different determinations) and Scenario 2 (same entity, simultaneous cell and aspect roles within one deployment) are architecturally distinct. In Scenario 1, the entity holds one level role in each deployment — the multi-level feature is distributed across deployments, not concentrated within one. In Scenario 2, the entity holds both roles within one deployment simultaneously. The two scenarios have different governance requirements and should not be conflated.

---

## 8. Operational test

A deployment instantiates the same-entity-at-multiple-levels architectural pattern if and only if: the same substrate entity has at least two complete, separately authored level determination records in the deployment's substrate — each at a distinct structural level (cell, aspect, or Self), each satisfying A1.13 composition requirements at its respective level independently, each carrying the Paper 1 commitments applicable at that level scope per B1.20, and each authorized by explicit governance action per A1.01.

---

## 9. Why naming as standalone matters; position in the B1.17 decomposition

The prior art value of B2.86 lies in its specificity. Any architecture that relies on the combination of (a) relational level determination, (b) simultaneous multi-level role occupancy within one deployment, (c) level-specific governance authorization, (d) independent composition validity at each level, and (e) recursive Paper 1 commitment application at each level scope must contend with this formalization as established prior art. The named pattern is narrower than generic role-based architecture (which does not commit to relational level determination) and narrower than generic multi-role patterns (which do not apply governance and composition requirements at each level independently within a unified human-governed substrate).

B2.86 is the third of five notes decomposing B1.17 in Phase B2. B2.84 established the relational roles integrating frame: the general case that structural membership is relational rather than intrinsic, with the artifact as bearer and the role-instances inhering in the arrangement. B2.85 established purpose-defined level determination: that level assignment is deployment-specific authored content, not a fixed property, with the consequence that the same artifact can have different determinations in different deployments. B2.86 formalizes the most complex operational consequence of these two commitments: simultaneous multi-level role occupancy within one deployment and the governance requirements it carries. B2.87 will address the interaction between relational roles and evolution — how multi-level role occupancy behaves under the three evolution mechanisms and what level-specific evolution governance requires. B2.88 will close the B1.17 decomposition with relational roles verification: the operational tests for whether a deployment correctly instantiates relational role membership at each level.

After B2.88, Phase B2 continues with the B1.18 content-domain decomposition, taking up the architectural treatment of distinct content types across the three levels and how content-domain distinctions interact with the relational role architecture B2.84 through B2.88 establish.

---

## Source paper

Li, Wenxin. "The Instinct/Reasoning Separation Outside the Model." April 2026. Second paper in the Coordination Knowledge Substrate (CKS) theory series.

## Self-citation

This note is part of the CKS derivation note series. The foundational note for the human-governed commitment — the direct stylistic and structural template for this series — is: Li, Wenxin. "Authority, Not Labor: A Precise Definition of 'Human-Governed' in the Coordination Knowledge Substrate Pattern." April 2026. Note A1.01. Related notes in the B1.17 decomposition: B2.84 (relational roles integrating frame), B2.85 (purpose-defined level determination).
