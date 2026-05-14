# Boundary Case: Cross-Partner Composition — Governance Implications When Entities From Different Organizational Partners Are Composed Together, Testing Cross-Partner Authority Distribution, Content-Domain Compatibility Across Organizational Boundaries, and Governance Accountability for Composed Multi-Partner Deployments

**Note ID:** B6.08
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026).

---

## Abstract

The CKS architecture supports composition across organizational boundaries: cells developed by one deployment partner can be composed with aspect frameworks developed by another, under a coordinating governance body. This note formalizes the boundary case in which that cross-partner composition is attempted. Three architectural boundaries are stressed simultaneously: the cross-partner authority distribution commitment (A2.47), which specifies who holds authority over which entities but does not automatically assign composition-level governance authority; the expression mechanism and carry-strategy commitment, which determines whether Partner A's cells arrive in Partner B's context carrying Partner A's Self-level DNA and thereby conflict with Partner B's Self; and the composition-requirements test (A5.14), which must run across organizational boundaries to verify that a cell's content-domain semantically addresses the receiving partner's aspect purpose. The note identifies four boundary tests, three stress points, and the architectural limits within which governance must operate.

---

## 1. Configuration description

Partner A is an organizational entity that has developed cells under its own governance authority. Each cell carries a DNA layer — stabilized orchestration and behavior substrates governing what the cell does — and an action layer of recorded task instances and outputs from past execution. Partner A's cells have defined content-domains: the coordination work each cell is governed to perform is specified in its DNA layer as orchestration substrate. These cells were designed to serve coordination purposes within Partner A's deployment context, governed by Partner A's governance authority, and shaped in part by Partner A's Self-level DNA where the deployment involves a CKS Self.

Partner B is a distinct organizational entity that has developed an aspect framework under its own governance authority. Partner B's aspects are coordination arrangements of cells serving Partner B's organizational purposes. Each aspect has a defined coordination purpose that cell content-domains must address for composition to be valid. Partner B's Self-level DNA governs the behavioral and orchestration norms that apply to cells operating within Partner B's Selves.

A coordinating governance body — which may be both partners acting jointly or an independent third party authorized by both — has determined that certain of Partner A's cells can be composed into Partner B's aspect framework to form a composed deployment. The basis for this determination is the commitment at A1.13 that composition is governed: no entity enters a composition without governance specification, and all architectural commitments apply to all entities in the composition. The cross-partner composition boundary case formalizes what the architecture requires at the inter-organizational boundary for this composition to be architecturally valid.

---

## 2. Architectural boundaries being tested

**A2.47 — Cross-partner authority distribution.** The architecture specifies that authority over entities remains with their governing partner unless explicitly transferred or jointly held under a governance agreement. In a single-partner deployment, authority over cells, aspects, and Self composition is unified. In cross-partner composition, authority is distributed: Partner A retains authority over Partner A's cells; Partner B retains authority over Partner B's aspect framework. But A2.47 does not by itself specify who holds authority over the *composition* — the aspect membership assignments, the cross-level access rules, and the interaction governance that determines how Partner A's cells behave within Partner B's aspects. This composition-level governance authority is the gap A2.47 creates but does not close. The boundary tests whether that gap has been explicitly addressed by the governance agreement.

**Expression mechanism and carry-strategy.** The expression mechanism determines which DNA-layer substrates activate for a given cell goal. Per the architecture, cells may carry the full Self's DNA with selective expression, or they may carry partial DNA slices, as a per-deployment design choice governed by orchestration substrate. When Partner A's cells were developed, the carry-strategy specification determined what DNA content the cells hold and how it activates at runtime. If Partner A's cells carry Self-level DNA from Partner A's deployment — governance norms, Self-identity anchors, behavioral constraints embedded at the Self level — that content travels with the cells into Partner B's deployment context. If Partner B's Self has its own Self-level DNA, which any architecturally coherent Self should, Partner A's Self-level DNA arriving inside cells may conflict with Partner B's Self-level governance. The carry-strategy must be explicitly specified for cross-partner deployment; the default is not a permissible substitute.

**B1.18 — Content-domain compatibility across contexts.** Cells developed for Partner A's deployment context carry content-domains appropriate for that context. Content-domain is not a technical property but a semantic one: it specifies what coordination work the cell is governed to do, what purposes it can serve, and what aspect purposes it can address. When a cell is placed in Partner B's aspect framework, the composition-requirements test (A5.14) must establish that the cell's content-domain semantically addresses the receiving aspect's coordination purpose. Cross-partner context differences mean that a cell well-suited for Partner A's aspect purposes may not address Partner B's aspect purposes — a compatibility failure that is not visible from cell architecture inspection alone and must be positively demonstrated rather than assumed.

---

## 3. Governance implications

**Authority distribution specification.** A2.47 cross-partner authority must be made explicit in the composed deployment. The governance specification must answer three distinct authority questions. First, which entity holds authority over Partner A's cells in the composed deployment — Partner A alone, the coordinating governance body, or both under a joint authority arrangement? Second, which entity holds authority over Partner B's aspect framework? Third, which entity holds composition-level authority — authority over aspect membership decisions, cross-level access rules, and the interaction governance between Partner A's cells and Partner B's aspects? These are distinct questions, and silence on any of them is not a permissible default. An unspecified authority question at the composition interface is Authority Ambiguity (B3.26), and Authority Ambiguity at composition scope means that no defined authority exists to register and address conflicts when Partner A's cells and Partner B's aspects interact during execution.

**Composition governance agreement.** Cross-partner composition requires a governance agreement — a substrate artifact held under human governance by the coordinating body — that specifies at minimum: which partner governs which entities; how conflicts between partners' governance decisions are themselves registered as first-class objects per A1.03 at composition scope, rather than collapsed by the coordination mechanism; how directed selection events on Partner A's entities are authorized when those entities are deployed in Partner B's context; and what the scope of composition-level governance authority is and who holds it. The coordinating governance body must be explicitly identified as the holder of composition-level authority before the composition is architecturally valid. This governance agreement is substrate content, not a procedural promise; it must be authored under human governance and accessible to both partners.

**Carry-strategy specification for cross-partner deployment.** Before Partner A's cells enter Partner B's context, the carry-strategy must be explicitly configured for cross-partner use. Two architecturally permissible configurations exist. Under partial-slice configuration, the cells carry only the DNA content relevant to the coordination purpose they serve in Partner B's context, with Partner A's Self-level DNA substrates excluded from the slice. Under full-DNA-with-governed-expression configuration, the cells retain full DNA, but the expression harness is governed to suppress Partner A's Self-level DNA substrates when executing within Partner B's aspects, so that only content-domain-relevant DNA activates. Either configuration is valid; the choice must be made, recorded as substrate content under the coordinating governance body's authority, and accessible for inspection. The impermissible default is to allow Partner A's cells to carry unspecified DNA content into Partner B's context without a governance decision having been made about what Self-level content travels with them.

**Content-domain validation across organizational boundaries.** The composition-requirements test (A5.14) must be run with both partners' governance inputs. The test must establish that each of Partner A's cells to be composed into Partner B's aspect framework has a content-domain that semantically addresses the relevant aspect's coordination purpose. This validation requires understanding of both the cell's content-domain (which Partner A governs) and the aspect's coordination purpose (which Partner B governs), making it inherently a cross-partner governance exercise. The test may reveal cells that are well-formed for Partner A's deployment context but carry content-domains that do not address Partner B's aspect purposes — a cross-partner content-domain mismatch that is not a defect of either partner's cells individually but a compatibility failure at the composition boundary. Such failures must be registered as first-class conflicts per A1.03 and resolved through explicit governance action by the coordinating body before those cells enter the composition.

**Provenance chain governance.** Partner A's cells have provenance chains established under Partner A's governance authority, satisfying the six-field provenance metadata requirement (A1.07). In the composed deployment, those provenance chains must remain accessible to the coordinating governance body for compliance demonstration. The path retraceability commitment does not relax at an organizational boundary: if the coordinating governance body needs to retrace a decision or action that originated in Partner A's cell, it must have access to Partner A's provenance records. The governance agreement must therefore specify the access arrangements under which the coordinating body can read cross-partner provenance records, and provenance entries generated during the composed deployment must identify the composition context alongside the originating cell identity, so that the trail remains coherent across the organizational boundary.

---

## 4. Boundary tests

Four boundary tests determine whether the cross-partner composition is architecturally valid.

**(a)** Is A2.47 cross-partner authority distribution explicitly specified for the composed deployment, covering entity-level authority for both partners' contributions and, separately and explicitly, composition-level authority?

**(b)** Does the A5.14 composition-requirements test pass across partner boundaries, positively demonstrating that each Partner A cell to be composed has a content-domain that semantically addresses the receiving Partner B aspect's coordination purpose?

**(c)** Are conflicts between Partner A's and Partner B's entities' content-domains — including any governance conflicts that arise from partner-specific orchestration assumptions embedded in the cells — registered as first-class objects per A1.03 and addressed through the governance agreement before composition proceeds?

**(d)** Is the carry-strategy for Partner A's cells explicitly specified for cross-partner deployment, with Self-level DNA conflict either eliminated through partial-slice configuration or suppressed through governed expression harness configuration, and is that specification recorded as substrate content under the coordinating governance body's authority?

A composed deployment that passes all four tests is architecturally valid at the composition boundary. A deployment that fails any test has an open governance obligation that must be resolved before the composition proceeds.

---

## 5. Stress points

**Authority vacuum at composition scope.** If neither partner explicitly holds composition-level governance authority, and the coordinating governance body is not specified or is underspecified, Authority Ambiguity (B3.26) develops at the composition interface. The condition is insidious: both partners may have well-governed entities, and the entity-level authority questions may be fully resolved, while the composition-level question remains open. Composition-level ambiguity produces undefined behavior on cross-partner conflict: when Partner A's cells and Partner B's aspects generate a conflict during execution, no authority is specified to register, address, or resolve it as a first-class object. The A1.03 first-class conflict requirement cannot be met without a specified authority at composition scope, and in its absence conflicts will be handled ad hoc — or not at all — with no provenance trace of how they were resolved.

**Content-domain mismatch producing composition validity failure.** Cells developed for one partner's deployment context were authored with implicit assumptions about the coordination work the relevant aspect serves, the level of abstraction at which the cell operates, and the organizational context in which its outputs are used. When composed into a different partner's aspect framework, these assumptions may be wrong in ways that make the A5.14 test fail: the cell's content-domain does not address the receiving aspect's coordination purpose. This is a semantic failure, not a technical one, and it may not be visible from cell architecture inspection alone. The mismatch will surface during the composition-requirements test if that test is run across the organizational boundary with both partners' governance inputs. It will surface as operational failures during execution if the test is not run. Cross-partner content-domain validation is not optional even when both partners' cells and aspects are individually well-formed.

**Carry-strategy conflict introducing Self-level DNA contamination.** If Partner A's cells arrive in Partner B's context carrying Partner A's Self-level DNA — governance norms, Self-identity anchors, behavioral constraints that reflect Partner A's organizational context — those substrates may activate within Partner B's Self and conflict with Partner B's Self-level governance. The conflict may not surface immediately; Self-level DNA conflicts often manifest as subtle behavioral inconsistencies rather than explicit execution errors, because the relevant DNA may only activate in particular cell goal configurations. The stress point is structural: the expression mechanism gives deployments control over what DNA content travels with cells and what activates, but that control must be consciously exercised at the cross-partner boundary. If the carry-strategy decision is deferred or left to default, Partner A's Self-level governance context silently enters Partner B's Self without a governance decision having authorized or specified it.

---

## 6. Architectural limits

The architecture specifies A2.47 cross-partner authority distribution provisions, the expression mechanism and carry-strategy as per-deployment design choices, the A5.14 composition-requirements test, the A1.03 first-class conflict commitment, and the A1.07 path retraceability requirement. It does not specify a maximum organizational complexity for cross-partner compositions, the minimum number of parties required in the coordinating governance body, or the legal or contractual instruments through which governance agreements must be established. Joint-partner and third-party coordinating body arrangements are both architecturally permissible; the architecture specifies what the coordinating body must govern, not what form it takes.

Governance determines the appropriate composition governance agreement, the authority structure of the coordinating body, and the procedures for resolving partner-level conflicts that cannot be addressed at the composition interface alone. The architecture's role is to specify the commitments that must be met — explicit authority distribution, carry-strategy specification, content-domain validation, provenance accessibility — and the stress points that arise when they are not. The specific organizational, contractual, and procedural form through which the governance agreement is established lies outside the architecture's scope.

The boundary case formalizes the governance requirements at the inter-organizational boundary. A cross-partner composition that satisfies all four boundary tests is architecturally indistinguishable, in its operational properties, from a single-partner composition of the same scale. The inter-organizational boundary does not introduce new architectural primitives; it introduces new governance coordination requirements around the primitives that already exist. The cell's modularity — its designed separability from any one deployment context — is what makes cross-partner composition architecturally available. The governance agreement is what makes it architecturally valid.

---

## 7. Operational summary

Cross-partner composition is architecturally available in CKS. It is not architecturally automatic. The cells and aspects that partners contribute bring their governance histories with them; those histories must be coordinated at the composition boundary rather than overwritten or assumed compatible. Three commitments require explicit governance action at that boundary: authority distribution must be specified at composition scope, not only at entity scope; carry-strategy must be configured to prevent Self-level DNA conflicts across organizational lines; and content-domain compatibility must be positively demonstrated through the composition-requirements test with both partners' governance inputs.

The architecture's general composition commitment — that all CKS commitments apply to all entities in any composition (A1.13) — is what makes cross-partner composition tractable rather than arbitrary. It means that Partner A's cells do not lose their provenance, their governance semantics, or their conflict-preservation properties when they enter a cross-partner deployment. It also means that Partner B cannot absorb Partner A's cells as undifferentiated content; the cells arrive with their authority structures intact, and those authority structures require explicit coordination at the composition boundary. The governance agreement that satisfies the four boundary tests is the instrument through which that coordination is formalized.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Boundary Case: Cross-Partner Composition — Governance Implications When Entities From Different Organizational Partners Are Composed Together.* CKS Derivation Note B6.08. May 13, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
