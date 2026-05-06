# Path Retraceability and Accountability Vocabulary: Full Operational Treatment of Claim 4 in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the architectural structure of the path-retraceability commitment named in §3.1 of the source paper as Claim 4 — a structure consisting of four accountability questions the substrate must answer, six provenance metadata fields that carry the answers, and a substrate-only-paths property that distinguishes CKS retraceability from external-tracking architectures. This note serves as the integrating frame for a series of standalone derivations that specialize each accountability question, each provenance field, and the substrate-only-paths property at full operational depth.

## Abstract

Claim 4 of the CKS pattern (§3.1) requires that any decision or piece of substrate content produced by deployment activity be traceable through substrate content alone — without consulting external audit logs, observability dashboards, or tracking systems — to the writer that produced it, the authority under which it was produced, and the rationale (where applicable) for its production. The commitment has three architectural elements that compose to form the integrated commitment: four accountability questions ("what was decided," "by whom," "under what authority," "with what rationale") that name the operational content the substrate must support; six provenance metadata fields (writer attribution, timestamp, antecedent reference, rule reference, rationale, relationship metadata) that carry the infrastructure for those answers; and a substrate-only-paths property requiring that path reconstruction depend only on substrate content. This note articulates the integrating frame: how the elements compose, how downstream commitments depend on specific elements, and what an operational test for the integrated commitment requires. Standalone treatments of each accountability question, each provenance field, and the substrate-only-paths property develop the elements at full operational depth in subsequent notes.

## 1. Why the path-retraceability commitment needs to be formalized at full operational depth

The parent foundational note commits to path retraceability as Claim 4 of the source paper, articulating the relationship between two named vocabularies — *path retraceability* (Rajabi & Kafaie, 2022) and the *accountability plan* / *accountability trace* pair (Naja et al., 2021). It does not, however, decompose the commitment into the architectural elements that downstream notes can specialize standalone. This note provides that decomposition as integrating frame.

Three motivations make the integrating-frame treatment worth stating standalone. First, deployments with audit, compliance, or multi-stakeholder accountability requirements need a precise specification of which retraceability properties the architecture commits to providing universally, separate from deployment-specific layering. Second, the strategic prior-art posture: subsequent derivations focused on accountability architectures, audit-trail patterns, or provenance-tracking features become more defensibly contested when the accountability commitments are publicly formalized as a structured architectural set with named elements. Third, connectivity: path retraceability supports the human-governed commitment (humans cannot govern what they cannot trace), the conflict-as-first-class commitment (resolution decisions reference their antecedent contradictions through provenance), the AI-as-substrate-mediator commitment (LLM-written content is distinguishable through writer attribution under Property E of the mediator role), and the source-of-truth commitment (the substrate is authoritative because its claims are supported by traceable paths). The integrating-frame treatment is what makes these connections operationally specific.

## 2. The four accountability questions, stated as a structured set

The substrate's source-of-truth commitment is operationalized through four questions the substrate must be able to answer about any piece of content produced by deployment activity. The questions are not arbitrary; they are the operational content of the source-of-truth commitment, in the sense that a substrate that cannot answer them has claims it cannot support with evidence and is therefore not authoritative on those claims.

**Question 1 — "What was decided?"** The substrate carries the decision itself as substrate content. For any decision the deployment has made — through cell execution under orchestration rules, direct human exercise of override authority, or the authoring of an orchestration rule — the substrate contains the decision as a piece of substrate state that readers can inspect through the inspect right.

The question architecturally commits the substrate to making decisions concrete rather than abstract or implicit. A decision must be addressable as substrate content in its own right and must persist across sessions per the substrate's persistence commitment, in contrast to architectures where decisions exist transiently in agent state, in inference logs, or in derived projections — none of which constitute substrate content the source-of-truth commitment can authoritatively cite.

**Question 2 — "By whom?"** The substrate carries writer attribution for each piece of substrate content. The writer may be a human acting under preserved override authority, an LLM mediator within a cell operating under a specific orchestration rule, or a stable cell automating writes under rules without LLM involvement.

The question architecturally distinguishes these three writer classes from one another with sufficient specificity to support downstream governance and accountability operations. Property E of the AI-as-substrate-mediator role makes LLM-mediated writes architecturally distinguishable from direct human writes; this is what the writer-attribution element of question 2 carries at the integrating-frame level. Collapsing the distinction produces systems where humans cannot tell which substrate content reflects their authority and which reflects automated production, which makes both governance and conflict resolution unworkable.

**Question 3 — "Under what authority?"** The substrate carries authority context for each piece of substrate content. For content produced by cells under orchestration rules, the authority context includes the rule reference — which specific rule authorized the write, per Property B of the AI-as-substrate-mediator role. For content produced by direct human override, the authority context includes the human's authority position in the deployment's governance structure, which is itself substrate content under the human-governed commitment's authority-not-labor framing. For content produced by rule authoring, the authority context includes the human-authorship metadata for the rule.

The question architecturally distinguishes rule-derived authority from direct-override authority, and both from the rule-authoring authority that produces the rules under which cells operate. A system whose authority context cannot distinguish these mechanisms cannot answer question 3, even if it records that "some authority" was exercised.

**Question 4 — "With what rationale?"** The substrate carries rationale for substrate content where the orchestration rule or deployment schema specifies that rationale must be captured. The rationale is recorded as substrate metadata, readable through normal substrate inspection.

The question is conditional in a way the other three are not. Questions 1, 2, and 3 admit no exceptions for content produced by deployment activity. Question 4's "where applicable" qualifier reflects the architectural choice that some content does not need rationale (a routine status update under a rule that specifies no rationale field), while other content does (a resolution of a first-class conflict, for which the resolution's rationale is part of the two-level handling pattern). The architectural commitment is that the substrate carries rationale where rules or schema require it; deployment design specifies which content classes require it.

The four questions together define what the substrate must be able to answer about its own content. A substrate that cannot answer all four (with question 4 conditional on rule and schema specification) fails the architectural commitment to path retraceability, even if it answers some of them in some cases.

## 3. The six provenance metadata fields, as integrating-level infrastructure

The four accountability questions are answered through six provenance metadata fields the substrate carries per piece of content produced by deployment activity. The fields are the infrastructure that makes the questions operationally answerable; a subsequent note treats each field standalone with the operational depth its individual specification requires. At the integrating-frame level, the six fields are: writer attribution (who or what produced the content); timestamp (when the content was committed); antecedent reference (what substrate content the writer read as input that informed this write); rule reference (what orchestration rule authorized the write, where applicable); rationale (where applicable, why the writer produced the content); and relationship metadata (for content that contradicts other substrate content, the relationship to the contradicting content per the conflict-preservation specialization).

The six fields stand under the four accountability questions as the infrastructure those questions are answered through. A substrate that records all six but cannot use them to answer the four questions — because the fields are not linked across substrate content, or the writer-attribution field collapses the human / LLM-mediator / stable-cell distinction — records infrastructure without the commitment that infrastructure exists to support. A substrate that records only some of the fields can answer only some of the questions. The architectural commitment is to all six being present where they apply.

The relationship-metadata field deserves note at the integrating-frame level because it specializes for the conflict-preservation case rather than applying universally. The four-field specialization for first-class conflicts (writer, timestamp, rationale, relationship) is the conflict-specific case of the broader six-field general case this note specifies; the relationship between the conflict-specific specialization and the integrating-frame treatment is one of specialization, not contradiction.

## 4. The substrate-only-paths property

The architectural commitment that distinguishes CKS retraceability from external-tracking architectures is that paths through substrate content are reconstructible from substrate alone. The property has four operational components.

**Substrate-alone reconstruction.** For any decision recorded as substrate content, a reader exercising the inspect right can reconstruct the path leading to that decision using only substrate content and provenance metadata, without consulting external audit logs, observability dashboards, tracking systems, or other non-substrate sources.

**Completeness in the substrate-only sense.** All four accountability questions can be answered from substrate alone, with the answers traceable through the substrate's provenance metadata to other substrate content (antecedent decisions, applicable rules, authority context recorded as substrate content under the human-governed commitment).

**Complementarity, not substitution.** Operational features that record substrate operations externally — observability systems, audit logs, monitoring infrastructure — are deployment-layer concerns. They may complement the architectural commitment but cannot substitute for it. A substrate that can answer the accountability questions only with help from external systems fails the architectural commitment, even if those external systems are reliable in deployment.

**Migration safety.** The property holds across substrate migration. Per the migration-safety property of tool-agnosticism, substrates moved between hosts retain their architectural commitments; the migrated substrate can answer the accountability questions on the new host without requiring migration of external systems.

The substrate-only-paths property is what makes path retraceability architecturally sound: paths depend only on the substrate, which is the architectural object the deployment commits to maintaining, not on external infrastructure that may be replaced, fail, or be bypassed. The property operationalizes the architectural-rather-than-procedural qualifier on the human-governed commitment: governance is architectural because retraceability operates through substrate alone, and substrate is the architectural object the governance commitment binds.

## 5. The relationship between accountability questions and provenance fields

The four accountability questions are answered through the six provenance fields, but the correspondence is not one-to-one. Some questions are answered through multiple fields; some fields support multiple questions. The integrating-frame treatment specifies the relationships:

— **Question 1 ("what was decided")** is answered through the substrate content itself, with the antecedent-reference field allowing readers to trace back through the path leading to the decision.

— **Question 2 ("by whom")** is answered through the writer-attribution field, which architecturally distinguishes human writers, LLM mediators, and stable-cell automated writers per Property E of the AI-as-substrate-mediator role.

— **Question 3 ("under what authority")** is answered through the rule-reference field for cell-produced writes, and through the writer's position in the deployment's authority structure for direct human writes — itself substrate content under the human-governed commitment. Both branches come from substrate.

— **Question 4 ("with what rationale")** is answered through the rationale field where rules or schema require rationale capture; the conditional applicability of question 4 reflects the conditional applicability of the rationale field.

The relationships are operational, not nominal: implementations recording all six fields make all four questions answerable; implementations recording only some fields make only some questions answerable. Partial field coverage produces partial question coverage, and the architectural commitment is to the full set.

## 6. What the path-retraceability commitment does NOT claim

Stating precisely what the integrating-frame commitment does not require keeps the standalone framing from drifting into something stronger than the source paper supports.

**It does not claim that retraceability is automatic.** Cells must record provenance during cell-to-substrate writes per the boundary-crossing specialization; humans must capture rationale where rules require it. The commitment is that the substrate is structured to carry the necessary metadata; whether deployments populate it is a deployment concern, governed by orchestration rules and substrate schema.

**It does not claim that retraceability is human-readable in surface form.** Provenance metadata may be structured for machine processing; readers may need tooling to traverse paths. The commitment is to metadata being present in substrate content, not to its presentation format.

**It does not claim that all paths are reconstructible instantly.** Path traversal may require substrate queries and traversal logic, with associated cost. The commitment is reconstructability from substrate alone, not instantaneous or low-cost reconstruction.

**It does not claim that retraceability covers all operational events.** Events external to substrate — host operations, deployment configuration changes, personnel changes — are deployment concerns. The commitment is to substrate content paths.

**It does not specify retention duration.** Substrate content persists per the substrate's persistence commitment; how long is a deployment concern. Retraceability holds for as long as the substrate content the path runs through persists.

**It does not require external accountability features.** Audit interfaces, compliance reporting tools, observability dashboards, and visualization layers are deployment-layer features that may build on architectural retraceability; the commitment is to retraceability through substrate, not to any specific feature built on it.

## 7. Why the integrating-frame treatment is load-bearing for downstream commitments

The integrating-frame treatment is load-bearing for several CKS commitments that depend on specific elements of path retraceability holding.

**The human-governed commitment.** Human governance requires that humans can trace what they govern. The four accountability questions are what humans need answers to in order to exercise meaningful governance. Without retraceability, the commitment becomes nominal: humans hold authority but cannot trace what happens under it.

**The source-of-truth commitment.** The substrate is authoritative for coordination questions because it can support its claims with traceable paths. A substrate whose claims cannot be supported by paths through its own content is asserting authority it cannot back with evidence.

**The conflict-as-first-class commitment.** Conflict resolution decisions reference their antecedent contradictions through the relationship-metadata provenance field. Without retraceability, the substrate-level preservation and cell-level resolution would be nominally coupled but operationally untraceable.

**The AI-as-substrate-mediator commitment.** LLM-written content is architecturally distinguishable through writer attribution per Property E of the mediator role. The architectural distinction depends on path retraceability's writer-attribution field carrying enough discriminating content to mark LLM mediation as such.

**The architectural-property qualifier on governance.** Substrate-only paths are what make accountability architectural rather than procedural. A deployment whose retraceability depends on procedural infrastructure — audit cycles, manual reviews, periodic reconciliation, external systems that may fail or be bypassed — fails the architectural-property qualifier even if its procedural infrastructure is sound.

The downstream dependencies are specific, not abstract. Each commitment depends on identifiable elements of the path-retraceability commitment, and weakening any element weakens the commitments downstream of it.

## 8. Operational test at the integrating-frame level

A system implements path retraceability at the integrated level if and only if all of the following are true at all times during the substrate's existence.

1. The substrate carries the four accountability questions' answers for all content produced by deployment activity: what was decided is the substrate content itself; by whom is in writer attribution; under what authority is in rule reference and authority context; with what rationale is in the rationale field where rules or schema require it.

2. The substrate carries the six provenance metadata fields per piece of substrate content produced by deployment activity, with the fields' content sufficient to answer the four accountability questions to the discriminating depth the questions require.

3. Paths through substrate content are reconstructible from substrate alone — answers to the four accountability questions can be found in substrate without consulting external audit logs, observability systems, or tracking infrastructure.

4. The substrate-only-paths property holds across substrate migration: migrated substrates can answer the accountability questions on the new host without external infrastructure migration.

5. Path retraceability operates through architectural mechanisms — substrate metadata, provenance fields, reference linkages encoded as substrate content — not through procedural mechanisms such as audit cycles, manual reviews, periodic reconciliation, or after-the-fact reporting from external systems.

A system that fails any of (1)–(5) does not implement path retraceability at the integrated level. Subsequent decomposition notes specify finer-grained tests for each accountability question, each provenance field, and the substrate-only-paths property; the integrated test asks whether the architectural set composes correctly, not whether each element is independently implemented.

## 9. Why naming the integrating frame as standalone matters

Implementations under operational pressure to add audit features, compliance reporting, or governance dashboards consistently drift toward external accountability infrastructure where the substrate becomes one source among many. External systems are operationally familiar and easy to integrate; the substrate-only-paths property feels architecturally restrictive compared to flexible external tracking. The drift is rarely a deliberate decision to abandon the architectural commitment but the cumulative effect of small, defensible-in-isolation choices to use external systems for accountability work the architecture commits the substrate to handle. Implementations that drift produce systems where accountability appears to function but is actually held in external systems with their own failure modes — surfacing when external systems become unavailable, when migration moves the substrate without moving the external systems, when external systems disagree with the substrate, or when the deployment changes hosts and the external systems do not.

Naming the path-retraceability integrating frame as a standalone architectural commitment — with the four accountability questions, the six provenance fields, the substrate-only-paths property, the question-field relationships, the limitations, the load-bearing connections, and the integrated operational test specified above — gives downstream implementers a precise specification of what the architectural commitment to retraceability requires. The subsequent decomposition notes specialize each accountability question, each provenance field, and the substrate-only-paths property at full operational depth; together with this integrating frame, they give the full operational decomposition of the path-retraceability commitment named as Claim 4 in §3.1 of the source paper.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Path Retraceability and Accountability Vocabulary: Full Operational Treatment of Claim 4 in the Coordination Knowledge Substrate Pattern.* May 4, 2026. ORCID: 0009-0004-8065-3235.
