# AI-as-Mediator at Every Layer: A Standalone Specification of Requirement D for Multi-Substrate CKS Compositions

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in standalone form, Requirement D — the commitment that the AI-as-substrate-mediator role per Claim 2 (§4.1, §4.2) holds at every architectural layer of a multi-substrate CKS composition — as one of five composition requirements first formalized as a constraint set in *Composition Without Erasure: What Multi-Substrate CKS Systems Must Preserve to Remain Traceable* (Li, 24 April 2026).

## Abstract

The CKS source paper commits at Claim 2 (§4.1, §4.2) to AI-as-substrate-mediator: the LLM operates as mediator over the substrate — reading substrate content as primary source of state, writing under human-authored orchestration rules, and not exercising authority over substrate content — rather than as autonomous agent over the workflow. The commitment is defended at the single-substrate scope; the source paper acknowledges cell-to-system composition at §13.3 as an open question for future work. Compositions involving multiple substrates and adjacent AI components reintroduce a question the within-substrate commitment does not address by itself: at which architectural layers does the mediator commitment hold, and where in a composition could autonomous LLM operation legitimately enter? This note formalizes Requirement D — AI-as-mediator at every layer — as a standalone architectural specification. It states the requirement as four operational components, distinguishes it from three adjacent cross-system AI patterns commonly conflated with it, names the failure modes that violate it, and provides an operational test. The contribution is a standalone specification that allows Requirement D to be defended, implemented, and tested independently of the four sibling requirements (A, B, C, E) and of the broader composition-requirements frame.

## 1. Why Requirement D needs to be formalized as standalone

The parent foundational note *Composition Without Erasure* (Li, 24 April 2026) commits to five composition requirements that any multi-substrate CKS composition must preserve. Three sibling specializations treat Requirements A (per-substrate human governance preservation), B (conflict preservation across boundaries), and C (addressable provenance across boundaries) as standalone architectural commitments, and a fifth treats Requirement E (human-selective composition). This note treats Requirement D.

The motivation for the standalone treatment is that the AI-as-substrate-mediator commitment is defended by the source paper at the within-substrate scope. §4.1 names the commitment; §4.2 elaborates it as a core-theory commitment that applies to single-human coordination and extends to multi-human coordination at Claim 6. Neither treatment addresses what happens to the commitment when CKS substrates compose with one another, or with adjacent systems that themselves contain LLMs, or when LLM operations cross substrate boundaries. The within-substrate frame is silent on the every-layer question because the within-substrate frame does not have layers.

Composition introduces layers. A composition between a CKS substrate S1 and a system S2 has at minimum three architectural locations where LLMs may operate: inside S1's cells, inside S2 (whether S2 is a second CKS substrate or a non-CKS adjacent component), and at the boundary where content, references, and operations cross from one to the other. Each is a potential site at which the within-substrate mediator commitment could either continue to hold or fail to hold. Without a standalone specification, the question is left implicit, and implementations drift toward arrangements in which the commitment holds in some places and not in others. Compositions in which LLMs operate autonomously at one or more layers — as integration intermediaries, as cross-system orchestrators, as autonomous distributed agents — are commercially active design targets the field is currently pursuing; implementations adopting these patterns may satisfy the within-substrate mediator commitment inside each underlying substrate while violating the every-layer extension. The two commitments compose: the foundational mediator commitment specifies what the role is within a substrate; Requirement D specifies that composition does not provide an architectural escape hatch from it.

## 2. The Requirement D commitment, defined precisely

The architectural commitment can be stated as four operational components.

**(a) Mediator commitment within composing systems.** When CKS substrate S1 composes with a system S2, and LLMs operate inside S2 with respect to CKS-substrate content — whether S2 is itself a CKS substrate or a non-CKS adjacent component holding or producing content that participates in the composition — those LLMs satisfy the five mediator properties with respect to that content. They read the authoritative state as primary source. They write under orchestration rules that govern their cell-level behavior. They do not hold substrate-relevant state outside the substrate. They do not exercise authority over substrate content. Their outputs that affect substrate state are recorded with attribution. If S2 is a CKS substrate, the commitment is the same as the within-S2 mediator commitment. If S2 is non-CKS, the commitment narrows to LLMs in S2 that touch CKS-substrate content; LLMs in S2 that operate entirely within S2's own non-CKS architecture and never interact with composition content are out of Requirement D's scope.

**(b) Mediator commitment for cross-boundary operations.** LLMs whose operations cross the composition boundary — for instance, an LLM in a cell in S1 that reads content from S2, or an LLM in S2 that reads content from S1 — satisfy the mediator commitment in the cell context where they execute. The cross-boundary content the LLM reads is a referenced object, not a co-mediated one: the LLM mediates within its native cell, and the cross-boundary reference is carried by the mechanism Requirement C specifies. The LLM does not acquire authority over the referenced substrate's content in virtue of reading from it; it does not write to the referenced substrate outside that substrate's own orchestration rules; it does not retain referenced content as state outside its native substrate beyond the duration of its native operation.

**(c) Preservation of the five mediator properties across composition layers.** The five mediator properties are not relaxed at composition layers. They hold uniformly: within each composing substrate at the same strength they hold within a single substrate per the foundational commitment, and at the composition boundary at the same strength. Composition does not introduce a weaker reading of any property. A composition that satisfies a property within S1 but a relaxed version of the property at the S1↔S2 boundary fails Requirement D regardless of the per-substrate satisfaction.

**(d) No autonomous LLM operation at any composition layer.** No LLM in the composition, at any architectural layer, operates as autonomous agent, terminal producer, or authority-bearer with respect to CKS-substrate content. The Property-D commitment that LLMs do not exercise authority over substrate content holds at every layer; the Property-B commitment that LLMs write under orchestration rules holds for cross-boundary writes; and orchestration logic that governs cross-boundary operations lives in human-authored orchestration rules, not in an LLM situated between substrates.

The four components together define Requirement D architecturally. A composition that satisfies all four has Requirement D in the architectural sense. The components are mutually reinforcing and cannot be partially adopted: a composition that satisfies (a), (b), and (c) but permits autonomous LLM operation at any layer fails (d) and therefore fails Requirement D.

## 3. What Requirement D does not claim

The standalone treatment is precise about what the requirement commits to. It is equally important to state what it does not, because each of the following is a distinct question Requirement D leaves unaddressed.

**Not a mandate for LLM presence and not a requirement that composing systems be CKS substrates.** Requirement D does not require composing systems to use LLMs, nor does it require composing systems to themselves be CKS substrates. The hybrid-systems composition framework supports compositions in which an adjacent component is a structured database, a rule-based system, or any other non-LLM or non-CKS artifact. Requirement D specifies how LLMs that exist in the composition behave with respect to CKS-substrate content; it does not require LLM presence or wholesale adoption of CKS commitments by non-CKS components.

**Not a prohibition on cross-boundary LLM operations.** Cross-boundary LLM operations are architecturally permitted. An LLM in S1's cell may read content from S2 as input to its mediated operation; the architectural commitment is that the LLM operates as mediator with respect to that content (reading deterministically, writing back under rules, not exercising authority), not that the cross-boundary operation is forbidden.

**Not a specification of implementation patterns and not a uniform-rule mandate.** Requirement D does not commit to particular mechanisms for enforcing the four components — rule-validation infrastructure, output-validation pipelines, cross-boundary audit, or any specific runtime arrangement; the choice of mechanism is a deployment-level decision. It also does not require all LLMs across a composition to share rules; different LLMs in different composing systems may operate under rule sets appropriate to their own substrate's domain, provided each LLM's operations are rule-governed within its own context.

**Not a claim that mediator preservation is operationally simple.** Cross-boundary LLM operations may require coordination of orchestration rules across substrates, validation of outputs across architectural contexts, and audit infrastructure spanning the composition boundary. The architectural commitment is to the mediator properties holding; the operational complexity of realizing them is a separate matter the architecture does not minimize.

## 4. What Requirement D is not — three adjacent patterns

Three architectural patterns from the broader cross-system AI design space are commonly conflated with the every-layer mediator commitment and need to be distinguished from it. Each is a real and reasonable design target in some contexts; conflating any of them with Requirement D produces a misreading of the commitment.

**Not LLM-driven cross-system integration.** A common architecture inserts an LLM as integration intermediary between systems: the LLM interprets requests in one system's vocabulary, decides how to translate them into another system's calls, and integrates responses. In this pattern the LLM operates as autonomous decision-maker at the integration layer — choosing routes, transforming representations, sometimes reconciling conflicts on its own authority. Requirement D forecloses this layer: orchestration logic across composition boundaries lives in human-authored rules per Property B, not in an integration LLM. LLM-mediated APIs across services, routing-LLMs, translation-LLMs, and natural-language interface layers across composing systems are realizations of the same pattern; each variant fails (d) at the integration layer.

**Not cross-system AI orchestration platforms.** A second common architecture deploys an AI orchestrator that coordinates work across multiple systems: the orchestrator decides which system to invoke, in what order, with what parameters, and integrates the results. Requirement D is incompatible with this pattern wherever the orchestrator's decision-making authority touches CKS-substrate content. Orchestration logic in the CKS frame lives in orchestration rules at the cell level, not in an orchestrating LLM situated above the composing systems. An AI orchestration platform that happens to invoke a CKS substrate as one of several backend systems is not made compatible with Requirement D by the invocation; the orchestration LLM still violates Property B and Property D at the orchestration layer.

**Not autonomous AI agents in distributed systems.** A third common architecture deploys autonomous agents that operate across distributed system boundaries, communicating via APIs or message buses, each agent making its own decisions about action selection. Requirement D forecloses this pattern wherever the agents touch CKS-substrate content. LLMs in CKS compositions are not autonomous; they operate as mediators within architectural contexts that bound their authority. An agent architecture that spans a composition boundary with autonomy intact violates (d) at every layer the agent operates.

The three patterns share a structural feature: each places autonomous LLM decision-making at a layer that Requirement D requires to be governed by rules and bounded by the mediator role. The standalone specification is what makes the incompatibility precise; without it, the patterns can be adopted while nominally claiming continuity with the within-substrate mediator commitment by pointing to the per-substrate scope where it is preserved.

## 5. Why Requirement D is load-bearing

Requirement D is what allows the AI-as-substrate-mediator role to extend coherently across compositions. Without it, the foundational commitment would hold only within single substrates; compositions would become a venue in which the mediator commitment could be quietly suspended at every layer between substrates while still being claimed at the per-substrate scope. Requirement D also composes with Requirement A (per-substrate human governance preservation) to preserve human authority across compositions: Requirement A states that humans retain inspect, modify, and override rights at every participating substrate, and Requirement D ensures that LLMs at composition layers do not exercise authority that would compromise those rights — an autonomous integration LLM that overwrites cross-substrate state, or an autonomous orchestrator that routes around human-authored rules, would render Requirement A nominally satisfied while operationally broken. The two requirements are separately specifiable and together preserve human governance across composition boundaries. Requirement D similarly composes with the hybrid-systems composition framework's three patterns (adjacent component as input, as derived view, as separate concern), specifying that LLMs in any of the three satisfy the mediator commitment within their architectural context, and with the determinism contract, ensuring at every composition layer the same boundary the contract establishes within a single substrate: substrate state remains deterministic and addressable; LLM non-determinism remains bounded inside the cell context the orchestration rules specify.

## 6. Failure modes that violate Requirement D

Six failure modes name distinct ways an implementation can fail the requirement. The list is not exhaustive; each names a concrete architectural pattern that violates one or more of the four operational components in §2.

**(i) Autonomous LLMs in composing systems.** LLMs in S2 that interact with CKS-substrate content operate without orchestration-rule governance — making decisions, writing to substrate state, executing actions on their own authority. Component (a) fails; Property D and Property B fail for S2's LLMs.

**(ii) Autonomous LLMs at the composition boundary.** LLMs whose operations cross the boundary execute without orchestration-rule governance over the cross-boundary operation — making cross-boundary decisions, exercising authority in cross-boundary writes, or holding cross-boundary state outside their native substrate. Component (b) fails.

**(iii) Cross-boundary orchestration logic in an LLM.** Orchestration logic that governs cross-boundary operations is encoded in an LLM rather than in human-authored orchestration rules — typically as an integration intermediary or as an orchestration platform deciding how content flows across the composition. Property B fails for the cross-boundary operation; component (d) fails.

**(iv) Mediator-property relaxation at composition layers.** The implementation enforces the five mediator properties within S1 but relaxes them at composition layers — for instance, by permitting LLMs in S2 to hold cross-boundary state outside S2 indefinitely, or by permitting LLMs at the boundary to make authority claims over cross-substrate content. Component (c) fails: the properties hold inside the substrates but not at the layers between them.

**(v) Autonomous distributed-agent patterns spanning the composition.** The implementation deploys autonomous AI agents that operate across the composition, with decision-making authority distributed across the agent network. Component (d) fails at every layer the agents operate; each agent violates Property D within its operating scope.

**(vi) Mediator-bypass mechanisms or hidden LLM autonomy.** The implementation nominally preserves mediator commitments at the documented architectural layers but provides operational bypass mechanisms — pre-processing LLMs that shape inputs before cells operate, post-processing LLMs that modify outputs after cells produce them, monitoring LLMs that act autonomously on observed flows — through which LLMs operate outside the rule-governed layers. The architectural commitment is nominally present and operationally violated.

Each failure mode is identifiable independently of the others and corresponds to one or more of the four operational components in §2. An implementation may exhibit several simultaneously; an implementation that exhibits any of them does not satisfy Requirement D.

## 7. Operational test

A multi-substrate CKS composition satisfies Requirement D if and only if all of the following hold at every architectural layer where LLMs operate within or across the composition, at all times during the composition's existence.

1. **Mediator commitment within composing systems.** Every LLM operating in a composing system with respect to CKS-substrate content satisfies the five mediator properties within its architectural context.

2. **Mediator commitment at composition boundaries.** Every LLM operating across the composition boundary satisfies the mediator commitment in its native cell context, with cross-boundary content treated as referenced (per Requirement C) rather than co-mediated.

3. **Uniform property preservation.** The five mediator properties hold at the same strength at composition layers as they hold within single substrates; no property is relaxed at any layer.

4. **No autonomous LLM operation at any layer.** No LLM in the composition exercises authority over substrate content, operates outside orchestration-rule governance, or holds substrate-relevant state outside its native substrate, at any architectural layer.

5. **Cross-boundary orchestration logic in rules.** Orchestration logic that governs cross-boundary operations is carried by human-authored orchestration rules, not by an LLM situated between substrates.

A composition that fails any of (1)–(5) does not satisfy Requirement D in the architectural sense, even if individual LLM operations within the composition appear to be bounded at some layers. The test is uniform: the commitment either holds at every layer or it fails the requirement.

## 8. Why naming Requirement D as standalone matters

Implementations operating under feature pressure to deliver cross-system AI capabilities consistently drift toward autonomous-LLM patterns at composition layers, because such patterns are operationally simpler in the short term than rule-governed mediator preservation: an autonomous integration LLM can be deployed without first authoring the orchestration rules that would govern its operations; an autonomous orchestration platform can be adopted without first specifying the cross-boundary rule set that would constrain it. The architectural cost — silent compromise of the AI-as-substrate-mediator commitment at composition layers — does not surface immediately, and may not surface until governance failures, audit gaps, or accountability disputes force the question.

Implementations that drift away from Requirement D produce systems in which composition becomes the mechanism by which autonomous LLMs are introduced. Failures manifest as compromise of the AI-as-substrate-mediator commitment specifically at composition layers (the within-substrate commitment holds; the every-layer extension fails), Requirement A nominally preserved but operationally compromised by autonomous LLM authority across substrates, Requirement C preserved at the substrate level but losing meaning at the boundary where effective authors are autonomous LLMs not subject to orchestration rules, and architectural-commitment failure that compounds across compositions as more layers are introduced.

Naming Requirement D as a standalone architectural commitment — with the four operational components, the limitations, the three adjacent-pattern distinctions, the load-bearing connections, the six failure modes, and the five-point operational test enumerated above — gives downstream implementers, auditors, and architects a precise specification of what the every-layer mediator commitment requires, separate from the four sibling requirements and from the broader composition-requirements frame. Future composition mechanisms must satisfy Requirement D, or argue against it by name, to remain in continuity with the CKS pattern's AI-as-substrate-mediator commitment.

The note formalizes the every-layer commitment. Specific composition primitives, mediator-enforcement mechanisms, and rule patterns at composition boundaries remain open work.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Parent foundational note

Li, W. (2026). *Composition Without Erasure: What Multi-Substrate CKS Systems Must Preserve to Remain Traceable.* 24 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *AI-as-Mediator at Every Layer: A Standalone Specification of Requirement D for Multi-Substrate CKS Compositions.* May 5, 2026. ORCID: 0009-0004-8065-3235.
