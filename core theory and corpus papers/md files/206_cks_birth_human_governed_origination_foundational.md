# Birth as Human-Governed Origination: A Foundational Lifecycle Commitment in the Coordination Knowledge Substrate Pattern (Paper 2 Derivation)

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note ID:** B1.09 (Series B, Phase B1)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one foundational lifecycle commitment named in the source paper — *birth* — as a standalone architectural commitment with independent operational content, and to make precise the distinction between governance and labor the commitment carries.

## Abstract

Paper 2 introduces three lifecycle operations — birth, mating, death — that apply at every structural level (cell, aspect, Self) within a CKS-governed AI Self. The first, *birth*, is the creation of new cells, aspects, or Selves. The source paper states the commitment in one sentence: *birth is the creation of new cells, aspects, or Selves under human governance, where origination may be performed by humans directly or by LLMs operating under human direction, with the architectural commitment being governance, not labor.* This note formalizes that commitment, distinguishes it from two adjacent framings (fully-manual creation and fully-automated creation), names the inherited commitments birth composes with, identifies the operational implications, and provides an operational test. The note opens the lifecycle cluster within Phase B1: B1.09 establishes the origination pattern, B1.10 (mating) builds on it for cross-entity combination, B1.11 (death) for retirement.

## 1. Why birth needs to be formalized as a standalone foundational commitment

Paper 2 names lifecycle machinery — birth, mating, death — as architectural primitives operating at every level within a CKS-governed Self. Each is a governed transition over the population of structural units that compose the Self, but they are distinct: birth creates entities, mating combines existing entities into new ones, death retires entities. Conflating them under a single "lifecycle" header obscures what each commits to and leaves downstream implementations without a precise specification for any of them.

A CKS deployment that scales beyond its initial configuration must add new cells, aspects, and Selves over time. Each addition is a birth event. If birth is treated only as one bullet under a generic lifecycle header, deployments tend to handle it as either an unspecified manual step or an unspecified automated step. Both violate the source paper's commitment in different directions: the first collapses labor and governance into one bottleneck; the second abandons governance to gain labor flexibility. Naming birth as standalone gives downstream implementations a principled vocabulary for origination that satisfies governance without forcing labor onto any particular party.

This is the ninth Phase B1 note and opens the lifecycle cluster (B1.09 birth, B1.10 mating, B1.11 death). It precedes the evolution-mechanism notes (B1.12–B1.15), bidirectional-evolution note (B1.16), and structural-property notes (B1.17–B1.20) that complete the foundational set.

## 2. The commitment, precisely stated

A system instantiates the **birth** commitment when origination of a new cell, aspect, or Self is governed by humans, with origination labor allocable across humans and LLMs operating under human direction, and with the resulting entity inheriting all applicable architectural commitments at its level from the moment of instantiation. The commitment has six operational components.

**(a) Birth is the creation of a new structural unit at one of three levels.** A cell is birthed when a new informational task requires handling, an aspect when a new purpose requires coordination across cells, a Self when a new integrated CKS-governed intelligence is needed. Each level has level-distinct specification content — cell birth specifies DNA-layer initial content, harness substrate, carry-strategy, and an empty Action layer; aspect birth specifies aspect coordination rules, initial cell membership, and aspect purpose; Self birth specifies Self integration architecture, initial aspect collection, and instinct/reasoning separation configuration — but every birth follows the same governance pattern across levels.

**(b) Birth is governed by humans.** Every birth event requires human authorization within whatever authority architecture the deployment configures. An entity instantiated by an LLM or runtime middleware without human authorization is not a CKS-coherent birth, regardless of how plausible the resulting specification appears.

**(c) Birth labor is allocable.** The labor of producing the birth specification — drafting initial DNA-layer content, writing the harness substrate, choosing the carry-strategy, defining aspect coordination rules, specifying Self integration architecture — may be performed by humans directly or by LLMs operating under human direction. The architectural commitment is to governance over the resulting authorization; labor distribution is a deployment decision.

**(d) Birth specifications are substrate-resident authoritative content.** What gets birthed, with what initial content, with what harness substrate and carry-strategy, is recorded as substrate content under the same source-of-truth and inspectability commitments that apply to any substrate content. The specification is durable substrate content that subsequent operations can reference.

**(e) Birth events are recorded with full provenance.** A birth event includes the six provenance metadata fields the antecedent paper commits to for any substrate write — who authorized the birth, when, under what rule, with what specifications, with what verifying signature where applicable, and with what relationship to prior substrate content. The event itself becomes part of the substrate history.

**(f) Birthed entities inherit all applicable architectural commitments at their level.** A newly birthed cell inherits the antecedent paper's six commitments at the cell level. A newly birthed aspect inherits Paper 2's aspect-level commitments. A newly birthed Self inherits Paper 2's Self-level integration commitments and the antecedent paper's commitments at every internal level. Inheritance is architectural, not procedural: the birthed entity is CKS-coherent at instantiation, not after a subsequent configuration step.

These six together define what the commitment requires; failing any one fails the commitment. The defining slogan: **the architectural commitment is governance, not labor**.

## 3. What makes birth-as-human-governed-origination architecturally distinctive

Two adjacent framings each capture some aspect of birth but not the whole.

**Not fully-manual creation.** Conventional system configuration treats new-component instantiation as an entirely human-performed labor event: humans write all configuration files, define all schemas, draft all rules, populate all initial content. This satisfies governance trivially but pays for it in labor. The CKS commitment does not require this. Specification labor can be performed by LLMs operating under human direction, with humans exercising governance through authorization, review, and override. Fully-manual creation is one permissible deployment of CKS birth, not the architectural commitment.

**Not fully-automated creation.** Some recent AI-system architectures treat new-component instantiation as fully autonomous: the system identifies the need, generates the specification, and instantiates without human authorization. This satisfies labor flexibility maximally but pays for it in governance. The CKS commitment rules this out. Even when LLMs produce the entire specification, humans must govern the resulting authorization. Fully-automated creation is not a permissible deployment of CKS birth.

**The CKS commitment combines the two.** Birth is governance-fixed and labor-flexible. Humans govern every origination event (architectural property); labor is allocable across humans and LLMs operating under human direction (deployment property). This is what allows CKS deployments to scale operationally without forfeiting governance.

## 4. Biological analog as conceptual scaffold

Paper 2 makes regular use of biological analogs as conceptual scaffolding. The analog functions to orient intuition, not to specify architectural substance.

Biological cells are birthed through mitosis; biological organisms through reproduction. In both cases the resulting entity is *autonomous*: no external authority gates the event.

CKS birth differs in three architecturally consequential ways. First, it is not autonomous: every birth event is human-governed, with human authorization required as an architectural precondition. Second, it does not follow a fixed genetic program: the birth specification is human-authored or LLM-drafted under human direction, and is itself substrate content subject to inspection, modification, and override. Third, it is not labor-rigid: specification work can be allocated flexibly, while biology has no analog of labor allocation. The analog orients intuition; the architectural substance — governance, with flexible labor, over a recorded specification — sits in the CKS commitment, not in the analog.

## 5. Inherited commitments from the antecedent paper

Birth composes with six commitments from the antecedent paper.

**Human-governed authority architecture (A1.01).** Birth is governed by humans. The three rights named in the human-governed commitment (inspect, modify, override) apply: humans can inspect any specification, modify it before or after instantiation, and override any birth event after the fact by retiring or reconfiguring the resulting entity. Birth operates under the regime the antecedent paper establishes.

**Labor allocation framework (A1.12).** Birth labor is allocable across the three modes the antecedent paper names: humans performing the work directly, LLMs performing it under human direction, and stable cells largely automating it under orchestration rules. The third mode applies when birth specifications are themselves produced by stable substrate-resident processes governed by rules.

**Path retraceability (A1.07).** Birth events carry the six-field provenance metadata the antecedent paper commits to for substrate content. They are retraceable like any other substrate event.

**Determinism contract (A1.10).** Birth operations are deterministic given their recorded specifications. Replaying a recorded birth event from substrate state reproduces the entity that the original event produced. Non-deterministic content the antecedent paper allows (LLM-mediated drafting) sits before the recorded specification, not after.

**Substrate as source of truth (A1.08).** Birth specifications are substrate content. The specification is the authoritative record of what was birthed; the resulting entity's initial state is a function of the specification, not of any LLM session, cached state, or runtime artifact.

**Orchestration rule authoring (A2.04).** Where a deployment chooses to govern birth through rules — specifying what kinds of births can be authorized by which humans, under what conditions, with what review processes — those rules are human-authored orchestration rules in the antecedent paper's sense.

The composition of these six commitments, applied to a single primitive, yields the birth commitment formalized here — not a new axiom but a named composition of inherited axioms applied to lifecycle origination.

## 6. Operational implications

**Birth governance is configurable per deployment.** A deployment chooses who can authorize birth at each level, what review processes apply, what audit trails are generated. The architecture commits to the configuration's *presence*, not to its content. This allows CKS deployments to range from informal individual settings to formally governed organizational ones without changing the architectural commitment.

**LLMs may perform birth labor under human direction.** A deployment may configure LLMs to draft initial DNA-layer content, write harness substrates, generate cell coordination rules, propose aspect compositions, or sketch Self integration architectures. The human role then shifts from authorship to governance: review, modify, authorize, or reject. Governance is satisfied at authorization; labor is satisfied without bottleneck.

**Birthed entities are testable at birth.** Because the birthed entity inherits the antecedent paper's commitments at its level, the operational tests the antecedent paper names apply at birth. A birth that fails any applicable test is an architectural failure.

**Birth events constitute lineage starting points.** Subsequent operations on the birthed entity — mating, death, evolution, action-feedback flows — reference the birth event as the entity's lineage origin. Because the event is recorded with provenance, the entity's lineage is retraceable from any subsequent state back to instantiation.

**Birth specifications can be governed by orchestration rules.** A deployment may author general birth rules — for instance, that cells handling regulated work are birthed with full-DNA-with-selective-expression and a particular harness substrate, while cells handling exploratory work are birthed with a partial-DNA-slice and a lighter harness. Births then instantiate per the rules; audit can trace any birth event back to the governing rule.

**Level-distinct specifications hold.** Cell birth, aspect birth, and Self birth share the governance pattern but have distinct specification content. Implementations should not treat birth as a single uniform operation.

## 7. Limits

**Birth does not occur without human governance.** A birth event without human authorization is an architectural failure, not a permitted operational variant. Labor flexibility operates entirely on the labor side; the governance side is fixed.

**Birth does not bind labor to humans.** A deployment that requires humans to perform every step of specification production is one permitted configuration; the architecture does not prescribe it.

**Birth does not eliminate configuration burden.** What the commitment shifts is *who* performs the labor, not whether the labor exists. Humans may delegate authoring to LLMs under direction, but the resulting specification still requires review and authorization. A deployment that imagines birth as cost-free because LLMs produce specifications has misread the commitment.

**Birth does not replace the substrate-cell boundary.** A birthed entity is itself a CKS artifact: the substrate-cell boundary applies at the entity's scope. Birth instantiates a new entity that respects the boundary; it does not collapse it.

**Birth is not a one-time event.** A birthed entity continues through mating, death, and evolution operations across its lifecycle. Birth is the origination operation, not the only operation.

## 8. Operational test

A system instantiates the CKS birth commitment if and only if all of the following are true at every birth event during the substrate's existence:

1. The birth event has identifiable human authorization within the deployment's authority architecture.
2. The birth specification is recorded as substrate content with full provenance (authorship, timestamp, governing rule where applicable, content, verifying signature where applicable, prior-content relationship).
3. Origination labor is permitted to be performed by humans, by LLMs operating under human direction, or by stable cells operating under orchestration rules — with the labor distribution as a deployment choice.
4. The birthed entity is CKS-coherent at instantiation: applicable architectural commitments hold from the moment of birth, not after a subsequent configuration step.
5. No LLM operation, vendor policy, or runtime middleware can in principle perform an authoritative birth without human authorization; auto-generation outside human governance is not a permissible deployment variant.

A system that fails any of (1)–(5) does not implement the CKS birth commitment, even if it produces operationally functional new entities. Such a system is not CKS-coherent on the origination axis.

## 9. Why naming birth as standalone matters

Conflating birth with manual configuration tempts implementers to treat origination as labor-bound, paying the labor cost in full and forgoing the operational scaling that LLM-mediated specification production provides. Conflating birth with auto-generation tempts implementers to treat origination as governance-free, gaining labor flexibility but forfeiting the architectural property the rest of the CKS pattern depends on. The standalone treatment names governance and labor as distinct concerns over a single primitive, with one fixed and one flexible, and gives downstream implementations a principled vocabulary for the configurations that combine them.

The lifecycle cluster (B1.09 birth, B1.10 mating, B1.11 death) is the place in Phase B1 where the population of structural units is named as something that grows, combines, and retires under governance. Birth opens the cluster because origination establishes the population. Mating combines existing entities; death retires them. Without a precise standalone treatment of birth, the downstream operations have no principled origin to reference.

Subsequent work that adopts, extends, or argues against the CKS lifecycle commitments should use "birth" in the sense formalized here — governance-fixed, labor-flexible, specification-recorded, level-distinct, inheritance-preserving, retraceable. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## Antecedent paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Birth as Human-Governed Origination: A Foundational Lifecycle Commitment in the Coordination Knowledge Substrate Pattern (Paper 2 Derivation).* May 7, 2026. ORCID: 0009-0004-8065-3235.
