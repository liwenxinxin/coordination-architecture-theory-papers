# Relational Roles Integrating Frame: Formalizing What Makes Cell, Aspect, and Self Relational Rather Than Intrinsic Types in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the architectural frame that governs how entities come to occupy the cell, aspect, and Self levels in the Coordination Knowledge Substrate (CKS) pattern — specifically, that these roles are relational rather than intrinsic, and that level membership is authored governance content rather than a property inferred from substrate artifacts alone.

This note is B2.84 in the CKS derivation note series. It opens the five-note B1.17 decomposition (B2.84–B2.88). Subsequent notes B2.85–B2.88 decompose purpose-defined level determination, same-entity multi-level occupancy, relational roles and evolution, and relational roles verification, respectively.

## Abstract

Paper 2 of the CKS theory series establishes three architectural levels — cell, aspect, and Self — and commits to a relational roles architecture: the same underlying substrate artifact may occupy different levels in different deployment contexts, because level membership is determined by what function an entity performs within the deployment, not by what kind of artifact it is. This note formalizes the integrating frame behind that commitment. A role is relational when its identity is defined by the relationship of an entity to other entities and to a purpose, not by the entity's internal properties alone. A cell is a cell because it performs a specific informational task; an aspect is an aspect because it coordinates cells for a purpose; a Self is a Self because it integrates aspects into a coherent whole. None of these definitions is substrate-intrinsic. All are function-determined, governance-specified, and authored as substrate content per A2.04. The note states the frame, distinguishes it from intrinsic-type membership in conventional AI architectures, articulates the biological analog as conceptual scaffold, identifies the inherited Paper 1 commitments the frame depends on, specifies the operational implications for deployment practice, states the limits on what relational roles permit and prohibit, and provides an architectural test.

## 1. Why formalizing the relational roles integrating frame matters

Paper 2's multi-level architecture — cell, aspect, Self — requires an account of how entities come to occupy levels. Without such an account, a reader might assume that level membership is an intrinsic property of a substrate artifact: that a particular artifact simply is a cell or an aspect by virtue of what it is, in the same way that a neural network layer simply is a layer by virtue of its position in a model graph. Paper 2 rejects this assumption explicitly. The relational roles commitment establishes that membership at each level is function-determined: an entity occupies a level because of what it does in a deployment context, not because of what it is as an artifact.

This commitment has downstream consequences throughout the architecture. It determines how level-distinguishability tests work, because the tests must probe functional role rather than artifact type (B2.09). It determines how governance operates over level membership, because role assignments are authored content that humans write and can change, not derived properties that the architecture computes from substrate artifacts (A2.04). It determines how the same substrate artifact can serve different roles in different deployments, which is the architectural basis for the deployment flexibility Paper 2 identifies as a property of multi-level composition. And it determines how role-specific Paper 1 commitments apply, because B1.20 ties which commitments apply at which scope to the role the entity occupies — and if roles were intrinsic, that dependency structure would collapse.

B2.84 formalizes the integrating frame that makes all of these downstream consequences coherent. It is the first of five notes decomposing B1.17, and it establishes the conceptual foundation that B2.85 through B2.88 build on.

## 2. The relational roles integrating frame precisely stated

**What makes a role relational.** A role is relational when its identity is constituted by the relationship of an entity to other entities and to a purpose, rather than by the entity's internal properties alone. A role that is constituted by internal properties is an intrinsic type. CKS entities carry relational roles, not intrinsic types.

The distinction is precise and consequential. For an intrinsic type, knowing what kind of artifact an entity is tells you its type membership directly. For a relational role, knowing what kind of artifact an entity is does not tell you its role membership; knowing what the entity does in relation to other entities and to a deployment purpose does.

**The cell role.** A cell is a cell because it performs a specific informational task within a deployment's operational architecture — processing inputs, consulting instinct and reasoning substrates, producing outputs under orchestration rules, and carrying the six architectural commitments Paper 1 defends. Being a cell is a functional role. An artifact that performs this function in a deployment occupies the cell role in that deployment. The same artifact does not occupy the cell role in contexts where it performs a different function. Level membership follows function; it does not precede it.

**The aspect role.** An aspect is an aspect because it coordinates cells for a purpose — organizing cells to address an operational domain, operating over its constituent cells as content domain, and asking pattern questions across those cells for the purpose the aspect serves. Being an aspect is a coordinative role. An artifact occupies the aspect role when it performs this coordination function with respect to a set of cells and a purpose in a deployment. The artifact is not inherently an aspect; it becomes an aspect through the function it performs and through the governance decision that authorizes that function.

**The Self role.** A Self is a Self because it integrates aspects into a coherent whole — providing unified governance over a complete operational intelligence, holding multiple coexisting aspects as facets of one CKS-governed deployment, and carrying the composition-level commitments Paper 2 introduces. Being a Self is an integrative role. The Self is not a bigger aspect; it is not defined by scale but by function: integration of aspects under unified human governance.

**Level membership is authored.** Because roles are relational and function-determined, level membership is not a property the architecture infers from substrate artifacts. It is authored content: a governance decision, written into the substrate per A2.04, specifying what role an entity plays in a deployment. This is the same authoring commitment that A1.08 establishes for substrate content as source of truth. Level membership is substrate content, not metadata derived from artifact properties. It is authoritative, per A2.46, because it is authored and human-governed.

**Level membership can change.** Because membership is relational and authored, an entity's level role can change when its function changes. A substrate artifact that performs an informational task in one deployment occupies the cell role there. The same artifact, redeployed to coordinate other cells in a different context, occupies the aspect role there. Role change requires a governance decision — a human decision to reassign the entity's role — and a substrate update that makes the new role assignment authoritative. Role changes do not happen automatically when function changes; they require a governance act.

**Role-specific Paper 1 commitments.** B1.20 establishes that Paper 1 commitments apply recursively at each role scope, and that which commitments apply at which scope depends on the role the entity occupies. Because roles are relational and authored, the scope at which Paper 1 commitments operate is determined by the role assignment, not by artifact type. An artifact operating at cell scope carries cell-level Paper 1 commitments. The same artifact, if its role changes to aspect scope, carries aspect-level commitments. The recursion structure of B1.20 depends on the relational roles frame: without it, the scope at which commitments apply would be indeterminate.

## 3. Contrast with intrinsic-type membership in conventional AI architectures

Conventional AI system architectures typically treat component types as intrinsic. A model is a model. An API is an API. A microservice belongs to a bounded context by its deployment configuration, and that belonging is not ordinarily understood as a governance decision about the role the service plays relative to other services — it is understood as a static membership assignment. When the membership changes, code changes. The type of a component does not depend on its function relative to other components; it depends on what the component is.

CKS's relational roles commitment inverts this. The same underlying substrate artifact can participate as a cell in one structural arrangement, as part of an aspect in another arrangement, or at different levels in different deployments, depending on what the structure is for and what governance has authorized. The artifact's identity as an artifact is stable; its role membership is not.

This distinction is architecturally significant for three reasons.

First, role changes in conventional architectures typically require code changes: to move a component from one bounded context to another, to reassign a module from one service to another, requires engineering work at the code layer. Role changes in CKS require governance decisions and substrate updates, not code changes. The substrate carries the role assignment; updating the substrate updates the role.

Second, level-distinguishability tests in CKS must probe functional role, not artifact type. A cell is distinguishable as a cell when it performs informational tasks per cell definition; an aspect is distinguishable as an aspect when it performs coordination functions per aspect definition. These tests are behavioral and relational, not structural and intrinsic. Per B2.09, the distinguishability mechanisms formalize exactly this kind of functional probe.

Third, the governance authority over role membership is architecturally explicit. In conventional architectures, who decides that a component occupies a given structural role is often implicit — it may be the architect, the team lead, or the build configuration. In CKS, role membership is authored substrate content, subject to the full set of human-governed commitments from A1.01: humans retain the right to inspect, modify, and override role assignments at any time. Role membership is not just relational; it is governed.

## 4. The biological analog as conceptual scaffold

Paper 2 draws on biological analogy for the relational roles commitment, and the analogy is direct enough to be more than metaphor. In developmental biology, stem cells are not inherently liver cells or brain cells. A pluripotent stem cell's identity as a particular cell type is not determined by its internal genome alone — every cell in an organism carries essentially the same genome — but by the developmental context it occupies: the signals it receives, the neighboring cells it interacts with, the tissue environment it is embedded in. Cell type identity is relational, not intrinsic, even though the underlying cellular substrate is genetically identical across cell types.

CKS entities parallel this structure. The underlying substrate artifact — with its substrates, orchestration rules, and accumulated content — is analogous to the cellular genome: the underlying bearer of functional potential. The role the artifact occupies — cell, aspect, Self — is analogous to the cell type: determined by the functional context, the governance signals it has received (role assignment authored per A2.04), and the structural arrangement it participates in.

The analog has a precise limit. Biological cell type determination is autonomous: developmental signals drive cell fate commitment through molecular mechanisms without a supervising decision-maker. CKS role determination is governed: humans author role assignments, govern role changes, and retain override authority over role memberships at all times per A1.01. The biological analog provides the conceptual structure of context-determined identity; the architectural substance is governed function-determined level membership, not autonomous differentiation.

Within that limit, the analog functions as a useful conceptual scaffold for several reasons. It makes clear why the same artifact can occupy different roles without contradiction — just as a stem cell can become a liver cell or a brain cell without contradiction, since neither type is intrinsic to the cell's underlying substance. It makes clear why role is not a fixed property — type identity is a contextual determination, not a permanent feature. And it makes clear why understanding role requires understanding context — the question "what role does this entity occupy?" cannot be answered by examining the entity alone; one must also examine the deployment context and the governance decisions that have been made.

## 5. Inherited Paper 1 and Paper 2 commitments

The relational roles integrating frame depends on a set of commitments inherited directly from Paper 1 and Paper 2.

**A1.08 — Substrate as source of truth.** Level membership is substrate content. It is not stored elsewhere, inferred at runtime, or held by a middleware layer. The substrate is the authoritative record of what role each entity occupies. This commitment is what makes relational role assignments inspectable, modifiable, and overridable under A1.01.

**A2.04 — Rule authoring.** Level membership is authored: a human writes the role assignment into the substrate as governed content. This is the same authoring commitment that applies to orchestration rules; role assignments are a category of authored substrate content. The authoring requirement is what makes role membership a governance act rather than a derived property.

**A2.46 — Category 4 authoritative content.** Role membership specifications are a category of authoritative substrate content — they are not advisory annotations or configuration hints but authoritative records of what function an entity performs in a deployment. This commitment is what gives role assignments their normative force within the architecture.

**A1.01 — Governance commitment.** Level membership is human-governed. Humans retain the right to inspect any role assignment, modify any role assignment, and override any role-related operation at any time. Role assignments are not locked by the architecture; they are subject to the full governance commitment at all times.

**B2.09 — Level-distinguishability mechanisms.** The distinguishability tests that allow an observer to determine what role an entity occupies probe functional role, not substrate artifact type. These mechanisms are the operational expression of the relational roles frame: they detect role membership through behavioral and coordinative evidence, not through artifact-structural evidence. B2.09 specifies these mechanisms; B2.84 establishes the frame that motivates why the mechanisms must work that way.

**B1.20 — Recursive Paper 1 commitments.** Paper 1 commitments apply at each level scope, and which commitments apply at which scope depends on the role the entity occupies. This commitment depends on relational roles: if roles were intrinsic, the scope at which Paper 1 commitments apply would be fixed by artifact type. Because roles are relational and authored, the applicable commitment scope is determined by the governance-authored role assignment.

## 6. Operational implications

**Explicit role assignments are required.** Because level membership is authored content and not inferred from artifact properties, deployments must explicitly author role assignments for each entity. A substrate artifact does not automatically become a cell, aspect, or Self by virtue of its structure. A human governance decision assigns the role and records it in the substrate.

**Role assignments are substrate-resident and governable.** Role assignments live in the substrate under the full set of human-governed commitments. They are inspectable, modifiable, and overridable. The architecture provides no mechanism by which a role assignment can be made beyond the reach of governance authority.

**Role reassignment requires governance decision and substrate update.** Because roles are not automatic, changing an entity's role requires two things: a governance decision by a human with appropriate authority, and a substrate update that makes the new role assignment authoritative. The first without the second leaves the substrate inconsistent. The second without the first is not admissible — substrate changes without governance authorization do not satisfy the A2.04 authoring requirement.

**Deployment design flexibility follows from relational roles.** Because the same substrate artifact can occupy different roles in different deployments based on its function, deployment designers have flexibility to repurpose components by changing their role assignment rather than by rebuilding them. An artifact that was designed to perform an informational task in one deployment can be redeployed in a coordinative role in another deployment, provided a governance decision authorizes the new role and the artifact's function in the new deployment satisfies the aspect role definition. This flexibility is an architectural property, not an implementation convenience.

**Cross-partner role assignments.** Where role assignments involve artifacts operated across partner authority boundaries, the cross-partner authority requirements per A2.47 apply. Role assignment is not a purely internal governance act when the artifact spans authority boundaries; it requires cross-partner authority to govern role assignment across those boundaries.

## 7. Limits

The relational roles integrating frame has precise limits. Formalizing the limits is as important as formalizing the commitments.

**Relational does not mean arbitrary.** Each role has specific functional requirements that an entity must satisfy to occupy it. A cell must perform a specific informational task per the cell definition. An aspect must coordinate cells for a purpose per the aspect definition. A Self must integrate aspects into a coherent whole per the Self definition. An entity that does not perform the requisite function does not occupy the role regardless of what governance authors into the substrate. Role definitions are architecturally fixed; role assignments are relational.

**Relational does not mean automatic multi-role occupancy.** The fact that an entity can occupy different roles in different deployments does not mean it automatically occupies multiple roles simultaneously in a single deployment. Multiple simultaneous role occupancy is a separate question, addressed in B2.86. B2.84 establishes only that roles are relational and context-determined; it does not resolve the multi-level question.

**Role definitions are fixed; role assignments are relational.** The definitions of cell, aspect, and Self are architecturally fixed commitments of Paper 2. These definitions are not themselves relational or context-dependent. What is relational is the assignment of an entity to one of these defined roles in a particular deployment context. The distinction is between the role taxonomy (fixed) and role membership (governed and context-determined).

**Relational roles do not eliminate the three-level structure.** The relational roles frame specifies how entities come to occupy the three levels; it does not render the three levels optional, negotiable, or collapsible. Deployments governed under Paper 2 commitments operate with three distinct levels — cell, aspect, Self — with fixed functional definitions. Relational roles is the account of membership in those levels, not an account that dissolves the levels themselves.

**Relational roles do not make membership informal.** Role membership is authored governance content subject to the full formal commitments of A1.08, A2.04, and A2.46. It is not an informal annotation, a soft label, or a descriptive tag. The relational character of roles refers to how membership is determined — by function and governance rather than by artifact type — not to any reduction in the formality or authority of the resulting assignment.

## 8. Architectural test

A deployment instantiates the CKS relational roles integrating frame if and only if all of the following hold:

1. Level membership for each entity (cell, aspect, Self) is recorded as authored substrate content, not derived from artifact-structural properties at runtime.
2. Each role assignment satisfies the functional definition of the role it assigns: cells perform informational tasks, aspects coordinate cells for a purpose, Selves integrate aspects under unified governance.
3. The role assignment for any entity can be inspected, modified, and overridden by humans with appropriate authority at any time, under the commitments of A1.01.
4. Level-distinguishability probes for any entity test functional role — what the entity does in the deployment — rather than artifact type.
5. Role reassignment is effected through a governance decision and substrate update, not through code changes alone.
6. Role-specific Paper 1 commitments per B1.20 are applied at the scope defined by the authored role assignment, not at a scope derived from artifact type.

A deployment that fails any of (1)–(6) may implement a useful multi-level architecture, but does not instantiate the relational roles integrating frame as Paper 2 specifies it.

## 9. Why naming this as a standalone derivation matters; opening the B1.17 decomposition

B2.84 is the eighty-fourth Phase B2 derivation note and the first of five notes decomposing B1.17. The note's standalone value lies in making the relational roles integrating frame an independently citable architectural commitment — not merely a background assumption implicit in multi-level composition, but an explicit formal specification of why level membership is function-determined and governance-authored rather than artifact-intrinsic.

The framing has prior-art value precisely because the relational-roles-versus-intrinsic-types distinction is architecturally consequential. A system that implements three-level composition with intrinsic type membership makes different claims than one that implements three-level composition with relational role membership. The distinguishability mechanisms differ, the governance architecture differs, the deployment flexibility differs, and the applicability scope of level-specific commitments differs. Formalizing the distinction as a named architectural commitment establishes public prior art for the relational character of CKS level membership, not merely for multi-level composition considered abstractly.

The five-note decomposition of B1.17 that B2.84 opens proceeds as follows:

- **B2.84** (this note): relational roles integrating frame — what makes roles relational, how membership is authored, the integrating conceptual structure.
- **B2.85**: purpose-defined level determination — how purpose determines which level an entity occupies; the functional criteria for each level in deployment context.
- **B2.86**: same entity at multiple levels — the conditions under which the same substrate artifact can simultaneously occupy roles at more than one level within a single deployment.
- **B2.87**: relational roles and evolution — how relational role membership interacts with the evolution mechanisms Paper 2 introduces; how role changes during the lifecycle are governed.
- **B2.88**: relational roles verification — the verification commitments that establish whether a deployment has correctly implemented relational role membership per the architectural frame.

Following B2.88, Phase B2 continues with B2.89–B2.93 decomposing B1.18 content-domain material.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Relational Roles Integrating Frame: Formalizing What Makes Cell, Aspect, and Self Relational Rather Than Intrinsic Types in the Coordination Knowledge Substrate Pattern.* May 12, 2026. ORCID: 0009-0004-8065-3235.
