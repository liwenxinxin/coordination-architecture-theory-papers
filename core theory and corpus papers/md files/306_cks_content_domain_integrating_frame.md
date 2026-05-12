# Content-Domain Integrating Frame: The Governed Operational Territory of Each CKS Entity at Each Structural Level

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

The Coordination Knowledge Substrate (CKS) pattern assigns every entity at every structural level — cell, aspect, Self — an explicit, authored specification of what that entity handles: its content-domain. Content-domain is the governed operational territory of the entity: the specification of what inputs the entity accepts, what outputs it produces, and what operational concerns fall within its scope. Content-domain is not incidental to an entity's existence; it is authored substrate-resident content, specified at birth, and evolved through directed governance. This note formalizes the content-domain integrating frame — the architectural claim that every CKS entity at every structural level has a content-domain; that content-domain is authored, substrate-resident, and governed; that level role and content-domain together specify an entity's territorial position; and that the explicit authoring of content-domain makes CKS entities governable, inspectable, and evolvable in ways unavailable to architectures with implicit scope. The note opens the B1.18 content-domain decomposition (B2.89–B2.93) and establishes the integrating frame that subsequent notes on content-domain specification requirements, boundaries, composition, and verification presuppose.

## 1. Why the content-domain integrating frame requires standalone formalization

The CKS architecture specifies that every entity at every structural level — cell, aspect, Self — has a content-domain. This specification is not peripheral decoration; it is the architectural mechanism by which CKS entities acquire defined operational territory. Without explicit content-domain, an entity's scope would be determined by runtime behavior — by what the LLM happens to produce or accept under prevailing conditions — rather than by governed human authorship. The content-domain integrating frame is the architectural claim that explicit, authored territorial specification is a requirement at every level, not an optional annotation.

Formalizing the frame as a standalone derivation note serves a specific purpose in the Phase B2 series. Five notes decompose B1.18's content-domain commitment: B2.89 (this note) establishes the integrating frame; B2.90 establishes content-domain specification requirements; B2.91 formalizes content-domain boundaries and their enforcement; B2.92 addresses content-domain and composition; B2.93 addresses content-domain verification. Each downstream note presupposes the frame this note establishes. Without an explicit formalization of what content-domain is architecturally — authored operational territory at each structural level, specified through level-appropriate mechanisms, governed as substrate content — the downstream notes have no shared referent.

The strategic prior-art position is correspondingly precise. Content-domain as the explicitly authored operational territory of each CKS entity at each structural level is the patentable territory this note formalizes. Prior work in multi-agent architectures, hierarchical systems, and modular AI does not commit to explicit authored territorial specification as an architectural requirement at every structural level under human governance. The formalization here closes that gap as public prior art under the author's name.

## 2. The architectural frame precisely stated

Content-domain in CKS is the governed specification of what an entity handles: what inputs the entity accepts, what outputs it produces, and what operational concerns fall within its scope. The definition applies at every structural level, with level-appropriate mechanisms operationalizing it at each.

**Content-domain defined.** Content-domain is not the entity's behavior — behavior is determined by DNA and action layers operating under orchestration rules. Content-domain is the entity's operational territory: the scope within which behavior occurs. An entity's content-domain specifies the territory; the entity's rules specify how the entity operates within that territory. The two are complementary, not substitutable.

**Cell content-domain.** At the cell level, content-domain is the cell's operational territory as an atomic informational task performer. Cell content-domain specifies: the particular informational task the cell performs; the input types the cell accepts, defined through schemas per B2.25; the output types the cell produces; and the behavioral scope the cell's DNA covers. The mechanism through which cell content-domain is operationalized is the cell's DNA specification per B2.25: schemas specify input and output types, and behavior substrates specify which behaviors fall within the cell's scope. A clinical-decision-support cell's content-domain is not the same as a regulatory-reporting cell's content-domain, even if both operate in the same aspect. Cell content-domain is the most fine-grained specification of territorial scope in the architecture.

**Aspect content-domain.** At the aspect level, content-domain is the aspect's operational territory as a coordination arrangement. Aspect content-domain specifies: the coordination domain the aspect covers, as expressed through its purpose statement per B2.15; what operational concerns the aspect coordinates cells for; what inputs trigger the aspect's coordination; and what outputs emerge from the aspect's coordinated cell activity. The mechanism through which aspect content-domain is operationalized is the aspect's purpose statement and coordination rules per B2.16. A clinical-care-delivery aspect's content-domain is the territory of clinical care coordination; a regulatory-and-quality-reporting aspect's content-domain is the territory of regulatory compliance and quality reporting. Aspect content-domain is intermediate in granularity — broader than any individual cell's content-domain, narrower than the Self's.

**Self content-domain.** At the Self level, content-domain is the Self's operational territory as an integrated intelligence. Self content-domain specifies: the overall integrated operational scope the Self governs; what aspects the Self integrates; what overall operational purposes the Self serves; and what inputs the Self processes across all aspects. The mechanism through which Self content-domain is operationalized is the Self's integration architecture per B2.21 and the collection of aspects the Self holds. The Self's content-domain is the broadest in the architecture — the territorial scope of the entire enterprise brain as a unit.

**Level role and content-domain together.** Level role (per B1.17) specifies the kind of operational territory an entity has: a cell's level role is that of atomic informational task performer; an aspect's level role is that of purpose-defined coordination arrangement; a Self's level role is that of integrated intelligence. Content-domain specifies which specific territory within that kind. Level role answers the question of what kind of territorial specification is appropriate; content-domain answers the question of which specific territory the entity covers. Together they fully specify an entity's territorial position in the architecture. Neither alone is sufficient: level role without content-domain says only what kind of entity something is; content-domain without level role says which territory is covered but not at what structural granularity.

**Authored per A2.04.** Content-domain specification is a governance act. Humans decide what an entity's content-domain is. Content-domain is not inferred from runtime behavior, not derived automatically from the LLM's capabilities, and not determined by the substrate's existing content. It is authored — written into the substrate as authoritative content specifying the entity's operational territory. The authority-vs-labor distinction from A1.01 applies: LLMs may assist in drafting content-domain specifications, but the authority to commit a content-domain specification to the substrate belongs to humans.

**Substrate-resident per A1.08.** Content-domain specification lives in the substrate as authoritative content. The substrate specification is the source of truth for what an entity handles — not runtime observation, not inference from execution history, not external documentation. A system that determines an entity's content-domain from runtime behavior rather than from substrate specification does not implement the CKS content-domain commitment.

## 3. What makes the content-domain integrating frame architecturally distinctive

Conventional AI architectures characteristically operate with implicit scope. A model handles what it can handle — the boundary of its operational territory is determined by its training, its context window, and the prompts it receives. There is no explicit authored territorial specification; the question of what an AI component handles is answered empirically, by testing, not architecturally, by authored specification. Multi-agent systems add routing logic, but that routing logic characteristically routes inputs to agents based on capability classification, not based on an authored territorial specification that precedes and constrains routing.

The CKS content-domain frame introduces three architectural properties unavailable in implicit-scope architectures.

**Governability.** Because content-domain is authored substrate content, it is governed as substrate content is governed. A human with appropriate authority can inspect the content-domain specification, modify it, and override it at any time per A1.01's three rights. Expanding or contracting an entity's content-domain is a governance event, not an emergent consequence of runtime behavior. The human-governed commitment applies to content-domain specification as it applies to all substrate content.

**Inspectability.** Because content-domain is substrate-resident, it is inspectable per A2.01. An auditor, a governance authority, or a deployment operator can read the content-domain specification for any entity at any time. The question "what does this entity handle?" has a substrate-addressable answer, not an empirical-testing answer. Inspectability of content-domain is operationally significant: it makes routing decisions auditable, territorial overlap detectable, and governance decisions about content-domain evolution traceable.

**Evolvability.** Because content-domain is governed and authored, it evolves through directed selection per B1.14 rather than through undirected drift. As deployment scope expands, content-domain specifications are updated through governance decisions and DNA modifications. The same underlying CKS artifact can have different content-domains in different deployments, matching different relational role configurations — the same cell participating in different aspects with different content-domain expressions. This is the content-domain analog of the relational role concept established in B1.17: the artifact's identity is the bearer; the content-domain inheres in the bearer per the deployment configuration that authors it.

## 4. The biological analog as conceptual scaffold

Biology offers a useful conceptual analog in the ecological niche. Organisms occupy specific ecological niches defined by what they eat, where they live, how they interact with other organisms, and what environmental conditions they tolerate. The niche is not defined by the organism's behavioral capabilities in isolation — it is defined by the organism's functional position in an ecosystem, constrained by both what the organism can do and what the ecosystem makes available. Cells in biological tissues occupy functional niches: liver cells occupy a metabolic-transformation niche; immune cells occupy a threat-detection-and-response niche; neurons occupy a signal-processing niche.

The CKS content-domain is the governed architectural analog of ecological niche specification. CKS cells occupy specific informational-task niches; aspects occupy specific coordination niches; Selves occupy specific integrated-intelligence niches. The niche specification is authored rather than evolved — a CKS entity's content-domain is committed to the substrate by human authority, not selected by environmental pressures over generations. This is one of the points at which CKS architecture surpasses the biological analog: per B1.20, the architecture enables per-deployment configuration of content-domain on operational timescales, not evolutionary timescales. The analog functions as conceptual scaffold; the architectural substance is explicit authored operational territory at each structural level, with level-appropriate mechanisms operationalizing the specification and human governance controlling its evolution.

## 5. Inherited Paper 1 commitments

Content-domain as architected here inherits without modification six Paper 1 commitments.

**A1.08 — Substrate as source of truth.** Content-domain specification is substrate content; the substrate specification is the source of truth for what an entity handles. The boundary against agent memory applies: an entity that maintains a de facto content-domain in LLM context that differs from its substrate specification violates A1.08's source-of-truth commitment.

**A2.46 — Category 4 authoritative content.** Content-domain specification is Category 4 content: authoritative content that governs entity behavior. It is not ephemeral; it is not advisory; it is the substrate record of what the entity's territorial scope is.

**A2.04 — Rule authoring as governance.** Content-domain specification is authored through the same governance act as orchestration rules. The humans who author an entity's content-domain are exercising governance authority, not performing labor that can be delegated without authority consequences. Authority over content-domain specification is not delegable to LLMs or automated processes without human approval.

**A1.01 — Human-governed.** Changes to content-domain are changes to substrate content under governance. The three rights — inspect, modify, override — apply to content-domain specifications. No LLM operation, automated process, or runtime middleware layer can silently expand or contract an entity's content-domain.

**A2.40 — Provenance.** Content-domain specification events — initial authoring at birth, subsequent modifications through directed selection — are recorded as substrate content with writer, timestamp, and rationale. The history of an entity's content-domain is substrate-addressable.

**A1.10 — Determinism contract.** Given an entity's content-domain specification and an input within that domain, the entity's processing is governed by its DNA and orchestration rules. The determinism guarantee applies within the content-domain boundary; what falls outside the content-domain boundary is a separate routing and governance question.

## 6. Operational implications

Four operational implications follow from the content-domain integrating frame.

**Author at birth.** Content-domain specification is part of the birth specification per B2.40 for every entity at every level. A cell cannot be born without a content-domain; an aspect cannot be instantiated without a purpose statement specifying its content-domain; a Self cannot be constituted without an integration scope specification. Omitting content-domain at birth is not an acceptable simplification — it leaves the entity's operational territory undefined and routing decisions ungoverned.

**Inspectable for audit.** Because content-domain specifications are substrate-resident, they are inspectable per A2.01. Auditing an entity's operational territory means reading its content-domain specification from the substrate. Routing decisions that directed inputs to or away from an entity are auditable against the entity's content-domain specification at the time of the routing decision.

**Basis for routing.** Content-domain specifications are the operational basis for routing decisions. An input is routed to an entity when the input falls within the entity's content-domain. Routing logic that does not reference content-domain specifications — that routes based on runtime capability inference rather than authored territorial specification — falls outside the CKS content-domain commitment.

**Cross-partner governance.** When entities handle cross-partner inputs per A2.47, their content-domain specifications must reflect that cross-partner scope, and cross-partner authority is required to commit a cross-partner content-domain specification. Content-domain is not a local deployment detail when it covers cross-partner territory; it is a joint governance artifact.

## 7. Limits of the content-domain integrating frame

Five limits bound what the content-domain integrating frame commits to.

**Not prescribing behavior.** Content-domain specifies the territory within which an entity operates; it does not prescribe what the entity does within that territory. A cell with a content-domain covering regulatory-reporting inputs may produce accurate or inaccurate regulatory reports, complete or incomplete ones, depending on the quality of its DNA rules. Content-domain scope and behavioral quality are distinct commitments; content-domain addresses scope, not quality.

**Boundaries authored, not auto-detected.** Content-domain boundaries are authored into the substrate; they are not inferred from runtime behavior. A deployment that infers content-domain from observed LLM behavior — even accurately — is not implementing the CKS content-domain commitment. The substrate specification must exist prior to and independently of runtime observation.

**No quality guarantee.** Content-domain specification does not guarantee that all inputs within the domain are handled correctly. Correctness is a property of DNA rules operating on inputs within the content-domain; it depends on rule quality, not on the scope of the territory. Correct territorial specification and correct behavioral execution are independent architectural concerns.

**Level-appropriate granularity.** Cell content-domain is the most specific; aspect content-domain is intermediate; Self content-domain is broadest. The levels are not interchangeable. Specifying an aspect-level content-domain at cell-level granularity (too specific for the level role) or at Self-level granularity (too broad for the level role) misuses the framework. Level-appropriate granularity is a requirement, not a preference.

**Not determining level role.** Content-domain does not determine level role; level role determines the kind of content-domain that is appropriate. A cell's content-domain is the specific informational task territory within the kind "atomic informational task performer." Knowing an entity's content-domain does not tell you what level it operates at; knowing its level tells you what kind of content-domain to expect. The direction of determination runs from level role to content-domain kind, not from content-domain to level role.

## 8. Operational test

A CKS architecture implements the content-domain integrating frame if and only if all of the following hold at all times during the substrate's existence:

1. Every entity at every structural level — cell, aspect, Self — has an explicit content-domain specification in the substrate.
2. Content-domain specifications are authored by humans as governance acts, using level-appropriate mechanisms: schemas and behavior substrates for cells; purpose statements and coordination rules for aspects; integration architecture and aspect collection for Selves.
3. Content-domain specifications are substrate-resident and constitute the source of truth for what each entity handles; runtime behavior does not silently expand or contract an entity's content-domain.
4. Content-domain modifications are governance events with provenance recorded in the substrate per A2.40.
5. Routing decisions reference content-domain specifications; routing that bypasses authored content-domain specifications and routes on runtime capability inference does not satisfy the CKS content-domain commitment.

A system that satisfies all five conditions implements the CKS content-domain integrating frame. A system that fails any condition — including systems that determine scope from runtime behavior, that omit content-domain specifications at birth, or that allow silent runtime expansion of content-domain — does not implement the commitment.

## 9. Conclusion and placement in the B2.89–B2.93 decomposition

The content-domain integrating frame names the architectural commitment that every CKS entity at every structural level has an explicitly authored specification of its operational territory — and that this specification is substrate-resident, governed, and evolved through directed selection. The frame operates through a two-part mechanism: level role specifies what kind of operational territory an entity has; content-domain specifies which specific territory within that kind. Together they fully specify an entity's territorial position in the architecture.

Naming this as a standalone derivation note matters for three reasons. First, it establishes the common referent for the four notes that follow: content-domain specification requirements (B2.90), content-domain boundaries and enforcement (B2.91), content-domain and composition (B2.92), and content-domain verification (B2.93). Each of those notes presupposes the frame articulated here. Second, it establishes the contrast with implicit-scope architectures as an explicit architectural commitment rather than an incidental property: CKS content-domain is explicitly authored; implicit-scope architectures rely on runtime inference. Third, it formalizes the full inheritance chain from Paper 1 commitments — A1.08, A2.46, A2.04, A1.01, A2.40, A1.10 — through Paper 2's multi-level composition commitment to the content-domain integrating frame, as standalone public prior art.

Phase B2 continues after the B1.18 content-domain decomposition (B2.89–B2.93) with the B1.19 cross-level access decomposition at B2.94–B2.97 and beyond.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Content-Domain Integrating Frame: The Governed Operational Territory of Each CKS Entity at Each Structural Level.* May 12, 2026. ORCID: 0009-0004-8065-3235.
