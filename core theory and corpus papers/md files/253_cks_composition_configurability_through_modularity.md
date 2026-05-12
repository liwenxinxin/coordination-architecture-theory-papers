# Composition Configurability Through Modularity: How the Modular Architecture Enables Configurable Composition Across Structural Levels in CKS Paper 2

**Note ID:** B2.36
**Series:** B — Paper 2 Derivation Notes
**Phase:** B2 — Operational Variants and Decompositions
**Parent note:** B1.08 (Modularity from Architectural Commitment)
**Companion note:** B2.35 (Modularity as Architectural Consequence)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

*This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).*

---

## Abstract

B1.08 established modularity as an architectural commitment in Paper 2's three-level structure of cells, aspects, and Selves. B2.35 formalized modularity as an architectural consequence — the product of four inherited properties (A1.02, A1.13, A1.14, A1.16) composing into structural independence with governance-boundary inheritance at every level. This note, B2.36, formalizes the *operational output* of that modularity: composition configurability. Composition configurability is the architectural capacity that enables cells to configure into aspects, aspects to configure into Selves, and the same modular unit to participate in different configurations simultaneously — all through substrate-resident membership records and integration architecture, bounded by A1.13 composition requirements, and subject to governed reorganization without modification of unit internals. The note articulates the four configurability mechanisms, distinguishes CKS configurable composition from conventional fixed composition and from biology's developmental commitment, traces the inherited Paper 1 obligations, identifies operational implications, and names the limits that bound the configurability. B2.36 is the second of five notes decomposing B1.08.

---

## 1. Why Composition Configurability Needs Its Own Formalization

B2.35 established what modularity is in the CKS architecture — a structural property arising from the conjunction of substrate-cell boundary integrity, composition requirements, level-membership substrate residency, and hybrid composition patterns. But establishing that an architecture is modular does not, by itself, establish what can be *done* with the modularity. Modularity is a structural prerequisite; composition configurability is what the modularity makes possible operationally.

The distinction matters for prior-art purposes. A claim that an architecture is modular does not automatically cover a claim that the same modular unit can participate in multiple structural configurations simultaneously, or that configurations can change through governed reorganization without modifying unit internals, or that all configuration states are substrate-resident authoritative content subject to the same governance properties as any other substrate content. These are distinct derivations, and each occupies patentable territory independently. Naming them as a cluster under the heading of composition configurability establishes that territory as prior art under the author's name.

B2.36 sits at the thirty-sixth position in Phase B2 and the second position in the five-note B1.08 decomposition. Its role in the phase's structural logic is to convert the architectural description produced by B2.35 into an operational specification: given that the architecture is modular in the ways B2.35 describes, what configurations does it support, how do those configurations change, and what constraints bound them?

---

## 2. The Architectural Specification: Four Configurability Mechanisms

The modular architecture per B1.08 and B2.35 enables four distinct configurability mechanisms. Each is specified below.

**Cell-into-aspect configuration.** Cells configure into aspects through membership rules that are substrate-resident authoritative content per A2.46. A configuration record specifies which cells participate in a given aspect and for what purpose within that aspect's coordination arrangement. Multiple cells can be configured into one aspect — the aspect is precisely the coordination arrangement of cells serving a particular purpose, not a container that holds a single cell. The same cell can simultaneously be configured into multiple aspects per B1.17's relational structural roles: the cell's identity is the bearer; the role-instances inhere in the bearer per each structural arrangement that calls on them. Cell-to-aspect configuration records are not held inside the cell's own substrate; they are substrate content at the membership level per B2.08's level-membership-as-substrate-resident treatment.

**Aspect-into-Self configuration.** Aspects configure into Selves through Self integration architecture per B2.21. The configuration specifies which aspects are facets of the Self and how they relate to one another within the integrated whole. Multiple aspects configure into one Self; a Self is not one aspect scaled up but a genuinely integrated structure in which multiple aspects coexist as facets of one unified CKS-governed intelligence. Aspect-to-Self configuration is substrate-resident integration architecture per A2.46 — the same authoritative content status applies here as at the cell-to-aspect level.

**Multi-structural participation.** The same modular unit — whether cell or aspect — can participate in different configurations simultaneously per B1.17. One cell configured into multiple aspects does not duplicate the cell's DNA layer, action layer, or harness substrate content. The modular unit's content is shared, not copied. What changes across configurations is the set of membership records that reference the unit, not the unit itself. This is the architectural mechanism that makes relational structural roles executable rather than merely notional: the substrate holds multiple role-instances against one unit identity, each membership record carrying its own structural context and governance properties per arrangement.

**Configuration change through governed reorganization.** Configurations can change over time. Cells can be reassigned across aspects through membership rule changes authorized per A2.04 rule authoring. Aspects can join or leave Selves through integration architecture changes authored under the same authority. The critical architectural property is that configuration changes do not require modification of the modular unit's internal specifications. When a cell is reassigned from one aspect to another, the cell's DNA layer, action layer, and harness substrate remain unchanged. Only the membership records per B2.08 change. This is what makes configuration change tractable at operational timescales — the scope of the change is bounded to the configuration records, not extended to the units being reconfigured.

All four mechanisms share a common substrate treatment: every configuration is substrate-resident authoritative content per A2.46. Configurations are authored per A2.04. Configurations are inspectable per A2.01. Configuration history is auditable per A1.07's path retraceability requirement. The entire configurability apparatus is bounded by A1.13 composition requirements — a valid configuration is not any arbitrary arrangement of modular units but one that satisfies the five composition requirements Paper 1 establishes.

---

## 3. What Makes Composition Configurability Architecturally Distinctive

The contrast with conventional AI architectures is specific. Conventional modular AI systems — including multi-agent frameworks, microservices-based AI deployments, and hierarchical orchestration platforms — are typically configured once at deployment. Component membership in a larger structure is fixed at initialization; structural arrangement is static after the deployment stage. The pattern is not incapable of change, but changes to structural arrangement typically require re-deployment, reconfiguration at the infrastructure level, or modification of the components themselves.

CKS modular architecture takes a different structural position. Because configurations are substrate-resident authoritative content rather than deployment-time parameters or infrastructure settings, they are subject to the same governance properties as any other substrate content: they can be modified by humans with appropriate access at any time per A1.01's three rights, without re-deployment and without modification of the modular units whose configurations change. The configurability is not a runtime side-effect; it is an architectural commitment encoded in the substrate.

The biological analog is instructive precisely where it breaks down. Biology evolved modular cell architectures because modularity supports evolvability — cells composing into tissues supports differentiation and development. But biological cells commit to tissue membership through developmental processes that are, for most cell types, effectively irreversible. A liver cell does not reassign to become a neuron on operational timescales. CKS cells are not subject to this developmental commitment. A cell configured into an aspect for one operational purpose can be reconfigured into a different aspect configuration through governed membership rule changes, on the timescales that operational requirements demand. CKS exceeds biology in configurable composition precisely at this point.

This is what enables vertical evolution per B1.16 to operate at operational timescales. Vertical evolution — the restructuring of composition relationships rather than the modification of unit content — operates through configuration changes. Cells reassigning across aspects, aspects restructuring within Selves — these are configuration-level changes enabled by the architecture's composability. Without substrate-resident configurable membership, vertical evolution would require the architectural equivalent of developmental recommitment, which biology cannot do and which CKS specifically avoids.

---

## 4. The Cognitive Analog and the Biological Analog as Conceptual Scaffold

Paper 2 uses the cognitive analog — the human Self as composed of multiple aspects corresponding to different modes of engagement — as a conceptual scaffold for the three-level structural architecture. The cognitive analog is useful at cell-into-aspect configuration: a person's competitive sports mode and calm study mode draw on the same underlying cognitive capacities but configure them into distinct coordination arrangements for distinct purposes. The analog carries the intuition that the same underlying units can participate in multiple purpose-defined arrangements.

The analog functions as conceptual scaffold only. The architectural substance is substrate-resident configurable membership under governance. A human's cognitive engagement with different purposes does not produce substrate records; it does not carry six-field provenance metadata per A2.40; it is not subject to human modification rights per A1.01; and it does not satisfy A1.13 composition requirements in any checkable sense. The cognitive analog supplies the intuition that same-unit-multiple-configurations is a natural and coherent structural pattern; the CKS architecture supplies the machinery that makes it executable, governable, and auditable.

The biological analog — biology's modular cell architecture — functions as a scaffold for the concept of modularity itself and as a reference point for evolutionary advantage. At cell-into-tissue configuration, however, the biological analog breaks down. CKS's configurable membership is not biologically available, and the architectural advantage CKS holds over biology at this point is one of the six points where CKS architecture exceeds the biological model per B1.20. The analog is bounded by the source paper's explicit framing: biological terminology is adopted where it illuminates; where it imports commitments the architecture does not share, the differences are named rather than concealed.

---

## 5. Inherited Paper 1 Commitments

Composition configurability inherits from six Paper 1 commitments, with four carrying direct load.

**A1.13 (composition requirements)** bounds all valid configurations. The five requirements — per-substrate governance preservation, conflict preservation at composition boundaries, provenance continuity, path retraceability, and plan-trace co-preservation — apply to any configuration arrangement. A configuration record that would produce a composition violating any of the five requirements is not a valid CKS configuration, regardless of whether the structural arrangement is otherwise operationally convenient. The configurability is bounded, not unconstrained.

**A1.16 (hybrid systems composition)** governs how components participate across composition patterns A, B, and C. Each configuration arrangement follows one of these composition patterns within its structural level. The patterns specify how substrate content, governance authority, and conflict state cross composition boundaries. Configuration records cannot specify arrangements that would cause a pattern-A composition to operate as a pattern-C composition, or that would mix pattern semantics arbitrarily.

**A2.04 (rule authoring)** applies to all configuration rule changes. When cells reassign across aspects or aspects restructure within Selves, the configuration changes are authored per A2.04 — they are human-authorized rule-level changes to substrate content, not automatic rearrangements triggered by operational conditions without governance authorization. This is what preserves the governed character of composition configurability: the architecture supports configuration change, but every change is authored.

**A2.46 (Category 4 authoritative content)** establishes that configurations — membership records, integration architecture records — are substrate-resident authoritative content. They are not metadata, not deployment parameters held outside the substrate, and not implicit properties of the modular units themselves. They are substrate content subject to all governance properties: inspectable, auditable, modifiable, and carrying provenance per A2.40.

**A2.40 (six provenance metadata fields)** applies to configuration events. When a configuration changes — a cell reassigns, an aspect joins a Self, membership rules update — the change event is recorded with the six provenance fields. The configuration history is preserved per A1.07's path retraceability requirement. This means that for any present configuration state, humans can trace the sequence of authorized changes that produced it.

**A6.06 (authority distribution change boundary)** applies as a boundary case when configuration changes alter authority distribution. A configuration that reassigns cells across aspects in ways that change which human authorities govern which substrate content crosses the authority distribution boundary per A6.06 and requires the governance processes appropriate to authority distribution changes, not merely routine membership rule authoring.

---

## 6. Operational Implications

Several operational implications follow from the composition configurability specification.

Configurations are established during cell and aspect birth per B1.09. The birth event is not only the origination of the modular unit itself but also the assignment of that unit into its initial structural configuration. Birth produces both the unit (with its DNA layer, action layer, and harness substrate) and the membership records that place the unit in its initial configuration.

Configuration changes occur through vertical evolution per B1.16. Vertical evolution is precisely the operation of changing composition relationships — which cells belong to which aspects, how aspects are structured within Selves — rather than changing the content of individual units. B2.37, the next note in the B1.08 decomposition, will develop this relationship in full.

Multi-structural participation per B1.17 is enabled without content duplication. A deployment in which one cell participates in three aspects does not maintain three copies of that cell's substrate content. It maintains three membership records. The substrate overhead of multi-structural participation scales with the number of configuration records, not with the number of times a unit's content would need to be copied in an architecture that requires structural duplication for multi-membership.

Deployments can support many configuration arrangements. The constraint is not on the number of configurations but on the validity of each configuration per A1.13. A large deployment with many cells, multiple aspects, and multiple Selves will have a rich set of configuration records; the architecture requires that each configuration satisfies composition requirements, not that the total number of configurations is bounded to some small number.

Configurations are inspectable at any time. Because configurations are substrate-resident authoritative content per A2.46, humans with appropriate access can read the current configuration state of any unit, aspect, or Self without scheduling, approval, or runtime intermediation per A1.01's inspect right. Configuration changes are visible as substrate changes, not as side-effects hidden inside operational execution.

High-stakes configuration changes — particularly those that cross authority distribution boundaries per A6.06 — may require additional governance review before taking effect. The architecture does not prescribe review workflows, but it preserves the governance authority through which review requirements can be established as orchestration rules.

Cross-partner configurations per A2.47 follow authority distribution per A6.06. When configurations span organizational boundaries — cells from one authority domain participating in aspects governed by another authority domain — the authority distribution governing those configurations must be explicitly specified in substrate content per A2.47 and must satisfy A1.13 composition requirements across the organizational boundary.

---

## 7. What Composition Configurability Does Not Mean

Six limits bound the composition configurability specification and prevent over-reading.

**Not unlimited configuration.** A1.13 composition requirements must be satisfied by any valid configuration. Configurability is the capacity to arrange and rearrange modular units within the space of valid configurations, not the capacity to produce any arbitrary arrangement. Configurations that would violate per-substrate governance preservation, conflict preservation at boundaries, or path retraceability are not available regardless of operational convenience.

**Not the elimination of modular unit integrity.** A modular unit's internal specifications — DNA layer, action layer, harness substrate — maintain their architectural identity through reconfigurations. When a cell is reassigned from one aspect to another, the cell is not modified. Configuration change is a change to the records that locate a unit in a structure, not a change to the unit's own content. Units are not dissolved, reformatted, or internally altered by the configurations they participate in.

**Not the bypass of governance.** All configuration changes are authored per A2.04. The architecture does not provide a mode in which configurations rearrange automatically outside human authorization, even when operational conditions might suggest a reconfiguration would be beneficial. Configurability is governed flexibility, not ungoverned dynamism.

**Not arbitrary arrangement.** Configurations are governed architectural content, not free parameters available for any value. The distinction from "arbitrary" is carried by A1.13's requirements and by A1.16's composition patterns: valid configurations are those that pass composition requirements checks and follow pattern semantics.

**Not the prescription of specific configuration patterns.** The architecture specifies that configurations exist, that they are substrate-resident, that they can change through governed reorganization, and that they must satisfy composition requirements. It does not specify which configurations a deployment must adopt, how many aspects a Self must have, or how cells must be distributed across aspects. These are deployment decisions made by humans with authority over the deployment's orchestration rules.

**Not the interchangeability of modular units.** Composition configurability means that the same modular unit can participate in different structural configurations. It does not mean that any cell can substitute for any other cell in any configuration. Each unit has its own operational character — its own DNA layer content specifying what the cell is governed to do, its own action layer recording what it has done. Configuration change assigns units into structural positions; it does not make units operationally equivalent to one another.

---

## 8. Operational Test

A deployment instantiates the CKS composition configurability commitment if and only if all of the following are true:

1. Cell-to-aspect membership records and aspect-to-Self integration architecture records are held as substrate-resident authoritative content per A2.46, readable and modifiable by humans with appropriate access at any time.
2. The same cell can hold membership records in multiple aspects simultaneously without duplication of the cell's own substrate content.
3. A configuration change — reassignment of a cell across aspects, restructuring of aspects within a Self — is effected through changes to configuration records authored per A2.04, without modification to the reconfigured unit's internal substrate content.
4. Every configuration satisfies A1.13's five composition requirements; no configuration arrangement is valid that would violate per-substrate governance preservation, conflict preservation at composition boundaries, provenance continuity, path retraceability, or plan-trace co-preservation.
5. Configuration change events are recorded with six-field provenance per A2.40, making the configuration history retraceable per A1.07.
6. Configuration changes that alter authority distribution are treated as A6.06 authority distribution boundary events and receive the governance handling appropriate to authority distribution changes.

A system that fails any of (1)–(6) may support some form of configuration flexibility but does not instantiate the CKS composition configurability commitment as formalized here.

---

## 9. Why Naming as Standalone Matters: Second Decomposition of B1.08

B1.08 established modularity as an architectural commitment, and B2.35 formalized modularity as an architectural consequence — the structural property arising from four inherited commitments composing into modular independence. B2.36 closes the gap between what modularity *is* and what modularity *makes possible*. Modularity enables configurable composition; configurable composition is the operational specification of how structural arrangement works across all three levels of the Paper 2 architecture.

The five-note B1.08 decomposition structure is:

- **B2.35** — Modularity as architectural consequence (the structural property arising from inherited commitments)
- **B2.36** — Composition configurability through modularity (this note; the operational output of the modular structure)
- **B2.37** — Modularity enabling vertical evolution per B1.16 (the evolutionary consequence of configurable composition)
- **B2.38** — Modularity across cross-partner compositions (the cross-boundary extension)
- **B2.39** — Modularity verification (the governance test for modularity claims)

Each note in the decomposition formalizes a distinct patentable derivation from B1.08. B2.36's specific territory — substrate-resident configurable composition records enabling multi-structural participation without content duplication, configuration change through governed record modification without unit-internal change, configurability bounded by composition requirements — is independently patentable and independently prior-art-establishing.

Following B2.39, Phase B2 continues with B1.09 birth decomposition (B2.40–B2.44 and beyond), carrying the same operational-variant-as-architectural-decomposition logic into Paper 2's lifecycle architecture.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Composition Configurability Through Modularity: How the Modular Architecture Enables Configurable Composition Across Structural Levels in CKS Paper 2.* May 12, 2026. ORCID: 0009-0004-8065-3235.
