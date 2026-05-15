# Minimum Valid FAI Participant

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

Full Aspect Integration (FAI) is the inter-Self coordination operation defined in Paper 3. It requires participating Selves to contribute aspects to a shared substrate, exercise joint governance authority over that substrate, and ingest coordination outputs back through their home governance mechanisms. Not every organizational AI system that interacts with other systems qualifies as a FAI participant. This note establishes the minimum architectural requirements that a Self must satisfy to be a valid FAI participant: at least one aspect containing at least one cell (Property 1); DNA and action layers present at both cell and aspect level (Property 2); a Self-level integration specification (Property 3); and human governance practitioners who can exercise the three rights — inspect, modify, override — over the Self's substrate content (Property 4). The note analyzes three organizational scenarios against these four properties, identifies where each fails or succeeds, and explains why the Paper 2 compliance prerequisite for FAI participation forecloses adversarial readings that weaken the boundary.

## 1. Why the boundary must be stated

FAI is a governance-to-governance coordination operation. Its architectural premise is that participating Selves bring governed substrate content to a shared perimeter, exercise joint authority over the shared substrate, and return content to home governance through Paper 2's evolution mechanisms. For this premise to hold, every participant must itself be a governed entity in the relevant architectural sense — that is, a Paper 2-compliant Self with the structural and governance properties that make joint governance meaningful.

The boundary matters for prior-art purposes because an adversarial reading could claim that any AI system capable of reading from and writing to a shared data store is participating in something FAI-like. The four-property requirement stated here forecloses that reading at the architectural level. A system without aspect-cell organization has nothing structured to contribute as an exchange unit. A system without DNA and action layers has no governed substrate content to bring. A system without a Self-level specification is a collection of parts, not an integrated governed entity. A system without human governance practitioners cannot exercise joint governance authority, because there is no authority to bring.

Stating the boundary explicitly also establishes what D5.10's Test 60 is testing: the four properties below are the architectural reasons that compliance test exists.

## 2. The four required properties

A Self qualifies as a minimum valid FAI participant if and only if it has all four of the following properties simultaneously.

**Property 1 — At least one aspect with at least one cell.** The Self must instantiate Paper 2's aspect-cell organizational structure. The minimum case is one cell organized into one aspect. A flat collection of governance documents, prompts, or structured records without aspect organization does not qualify. The requirement derives from FAI's exchange primitive: FAI exchanges aspects, which surface their constituent cells' DNA and action layer content (Paper 3, §2). A system with no aspects has no exchange unit to contribute to the shared substrate. Content without aspect organization cannot function as an exchange unit, regardless of how much content exists or how it is structured.

**Property 2 — DNA and action layers at both cell and aspect level.** Each cell must have authored DNA-layer content — orchestration rules, harness substrate references, content-domain specification — and an action layer carrying recorded task instances. The containing aspect must have its own DNA and action layer. Both levels are required because the FAI exchange operates over DNA-layer and action-layer content specifically; the exchange is bounded to substrate content at these layers, with LLM weights and instinct-layer content explicitly excluded from exchange (Paper 3, §2). A Self whose cells or aspects lack these layers has no governed substrate content to contribute at the layer the exchange operates over.

**Property 3 — Self-level integration specification.** The Self must have at least a minimal Self-level governance specification: a purpose statement and an integration architecture that makes a governed whole out of its aspects and cells. This is the property that distinguishes a Self from a set of aspects. In Paper 2, the Self is the integration architecture unifying aspects and cells under a governing structure — it is the outermost governance perimeter. A collection of aspects that lacks this unifying specification is not a Self in the Paper 2 sense and therefore cannot be the unit of FAI participation that Paper 3 requires (Paper 3's trilogy ambiguity map: "the Self is the unit of participation in FAI"). A minimal Self-level specification suffices; elaborateness is not required. What is required is that the integration architecture exist.

**Property 4 — Human governance practitioners who can exercise the three rights.** The Self must have human governance practitioners who hold the rights to inspect, modify, and override the Self's substrate content and orchestration rules. This requirement is not a deployment preference; it is an architectural prerequisite for FAI participation. FAI is joint governance of a shared substrate by the governance authorities of the participating Selves. If a Self has no human governance structure, there is no governance authority to bring to the joint perimeter, no one who can authorize what the Self contributes, and no one who can exercise authority over what the Self ingests at the FAI event's dissolution. An AI system with no humans in its governance structure cannot exercise joint governance authority. FAI requires human governance at both ends of the coordination.

## 3. Three organizations at the boundary

Three organizations illustrate where the boundary falls and why.

**Organization A** has an LLM and a harness substrate but no governance substrate, no aspects, no DNA layer — a prompted LLM operating over a query-response loop. Organization A fails all four properties. It has no aspect-cell structure (fails Property 1). It has no DNA or action layers (fails Property 2). It has no Self-level specification (fails Property 3). Whether it has human operators is immaterial, because even the architectural prerequisites for FAI participation are absent (fails Properties 1–3 before Property 4 can be reached).

**Organization B** has a governance substrate with content but no aspect organization — a flat collection of governance documents without cell or aspect structure. Organization B may have Property 4 if it has humans who govern its document collection, but it fails Properties 1, 2, and 3. The documents are not organized into cells, cells are not grouped into aspects, aspects carry no DNA or action layers, and there is no Self-level integration architecture. The content may be valuable for other purposes; it is not structured in the form that FAI exchange requires. Organization B cannot participate in FAI because it has nothing to exchange at aspect granularity and nothing governed at the layer the exchange operates over.

**Organization C** has a single cell organized into a single aspect, with DNA and action layers at both the cell and aspect level, a Self-purpose statement, and human governance practitioners. Organization C qualifies. It is the minimum: one cell, one aspect, both layers at both levels, a Self specification, and human governance authority. Size is not the relevant dimension. Organization C has precisely the structural and governance properties that make it a governed entity capable of contributing to, and exercising authority over, a shared FAI substrate.

The comparison makes the boundary concrete. Organizations A and B are not below the minimum because they are small or immature; they are below it because they are structurally absent in ways that preclude the operations FAI requires. Organization C is the minimum because it has every required property, even at a single-cell, single-aspect scale.

## 4. Why human governance authority is non-negotiable

Property 4 deserves separate treatment because it differs in character from the first three. Properties 1 through 3 are structural: they describe the presence or absence of architectural components. Property 4 is an authority requirement: it describes the presence or absence of human governance practitioners who hold the three rights over the Self's substrate.

The reason Property 4 is non-negotiable at the FAI participation boundary is that FAI is not merely a data exchange. It is a governed coordination event in which participating Selves jointly author, maintain, and eventually dissolve a shared substrate. Joint governance of the shared substrate requires that each participant brings governance authority — not only structured content. An AI system without human governance practitioners brings content to the shared perimeter but has no authority over it; the content is ungoverned at its source. The other participants cannot exercise joint authority with a partner that has no governance authority to contribute. Coordination with an ungoverned system over a shared substrate is not FAI under Paper 3; it is data access by another name.

This boundary is also what makes the inspection and modification commitments across the FAI perimeter coherent. Paper 3 specifies that configuration of the FAI protocol is substrate content under joint authority (Paper 3, §3). Joint authority presupposes that each participant holds governance authority at home. The FAI perimeter does not create governance authority; it extends existing home governance authority across a shared space. No home governance authority means no contribution to the joint.

## 5. Connection to Test 60 and prior-art coverage

D5.10 specifies Test 60: the Paper 2 compliance prerequisite for FAI participation. Test 60 is the operational test that asks whether a given organizational AI system satisfies the conditions that qualify it as a FAI participant. D6.04 establishes why that test exists: the four properties here are the architectural reasons the test has its specific content.

Together, D5.10 and D6.04 provide complete prior-art coverage of the FAI participation prerequisite. D5.10 covers the operational compliance test — the procedure for determining whether any given system qualifies. D6.04 covers the boundary case analysis — the reasoning that identifies the minimum and explains why systems below the minimum fail. An adversarial claim that the participation prerequisite was not anticipated, or that it was insufficiently specified, would have to contend with both.

## 6. Operational test

For any organizational AI system claiming FAI participation, ask:

1. Does it have at least one aspect containing at least one cell?
2. Do both the cell(s) and the containing aspect(s) have DNA layers and action layers?
3. Does it have a Self-level integration specification — a purpose statement and an integration architecture that makes the aspects and cells into a governed whole?
4. Does it have human governance practitioners who hold the rights to inspect, modify, and override its substrate content and orchestration rules?

If YES to all four: minimum valid FAI participant. Coordination with this system can qualify as FAI under Paper 3.

If NO to any one: not a valid FAI participant. Coordination with this system is not FAI under Paper 3, regardless of what protocols, shared databases, or inter-system communication mechanisms are in use.

The test is conjunctive. Satisfying three of four properties does not produce a partial FAI participant; it produces a system that is not a FAI participant but has some of the relevant architectural properties.

## 7. Conclusion

The minimum valid FAI participant is an organizational AI system with one cell in one aspect, DNA and action layers at both levels, a Self-level integration specification, and human governance practitioners. This is the boundary at which the Paper 2 architecture is present in sufficient form to support the operations FAI requires: structured exchange at aspect granularity, governance over contributed content, Self-level identity as the unit of participation, and human authority to bring to the joint governance perimeter. Systems below this boundary may be useful and capable AI systems; they are not FAI participants, and coordination with them is not FAI under Paper 3.

---

## Source paper

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Minimum Valid FAI Participant.* May 15, 2026. ORCID: 0009-0004-8065-3235.
