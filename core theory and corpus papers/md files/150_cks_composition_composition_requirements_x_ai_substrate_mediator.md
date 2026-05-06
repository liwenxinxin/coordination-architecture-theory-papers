# Mediator at Every Layer: How the AI-as-Substrate-Mediator Role Is Preserved Across Multi-Substrate Composition in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the emergent architectural property produced when two foundational CKS commitments — composition requirements and AI-as-substrate-mediator — compose, and to specify how that property operationalizes the source paper's commitment that AI-as-substrate-mediator must hold at every layer of composition.

## Abstract

The CKS pattern's composition-requirements commitment names five constraints that any multi-substrate composition must satisfy, one of which — AI-as-mediator at every layer — is named as a requirement but is not architecturally specified through the mediator role's operational properties. The mediator commitment, in turn, specifies the LLM's role through five properties that govern reads, writes, state-locality, authority, and attribution at the scope of a single substrate, but does not by itself specify how the role extends across composition partners. Each commitment in isolation underspecifies what an actually-coherent multi-substrate deployment must look like at the layer where the two meet. This note formalizes the emergent architectural property the two commitments produce when composed: *mediator preservation across composition*. The property has four operational components, three sharpening properties suitable for an operational test, and a set of anti-patterns it specifically rules out — including any composition in which one or more partners host LLM-as-autonomous-agent, LLM-as-terminal-producer, or LLM-as-source-of-truth patterns alongside substrates that satisfy the mediator role on their own. The note opens the cluster of composition pairs that operationalize the composition-requirements commitment through compositions with the foundational architectural commitments it constrains.

## 1. Why the composition pair needs to be formalized as standalone

Two CKS architectural commitments — composition requirements and AI-as-substrate-mediator — sit at adjacent layers of the architecture. Composition requirements specifies what any multi-substrate composition must preserve to remain CKS-coherent: per-substrate human governance, conflict preservation across boundaries, addressable provenance across boundaries, AI-as-mediator at every layer, and human-selective composition. The mediator commitment specifies the LLM's role at the scope of a single substrate through five properties — substrate-content reads as primary state, writes only under orchestration rules, no substrate-relevant state outside the substrate, no authority over substrate content, and writes recorded as substrate content with attribution. Each commitment is independently coherent and independently formalized in prior derivation notes in this series.

The pair is not exhausted by its members read separately. Composition requirements names AI-as-mediator at every layer as a requirement that any composition must preserve, but the requirement is named rather than operationally specified. The mediator commitment specifies the role through five properties, but the specification is at single-substrate scope and does not by itself say what it means for the role to hold "at every layer" of a composition that includes multiple substrates inside one cell, multiple cells sharing or referencing each other's substrates, multiple substrate–cell pairs operating across organizational units, and adjacent components composed under the three legitimate hybrid patterns. Either commitment can be satisfied at its own scope while the composition that involves both fails — a deployment may satisfy the five composition requirements at the requirements layer and may host LLMs that satisfy the five mediator properties on each substrate read in isolation, while still drifting into a composed system in which one or more partners operate the LLM as something other than a substrate mediator.

The note formalizes the closure as the emergent architectural property *mediator preservation across composition*: the architectural pattern in which the mediator role's five properties hold at every layer of the composition, with cross-substrate operations preserving the role at each side of every boundary, and with no composition partner authorized to host a non-mediator LLM pattern. The property distinguishes CKS deployments at composition scale from systems in which AI mediation operates inconsistently across composition partners — coherent on the primary substrate, incoherent on the components composed alongside it. The load-bearing source-paper sections are §4.1 and §4.2 (the mediator commitment as core-theory and as cross-claim spine), and §11.3 (the substrate as source of truth, including in the multi-role multi-cell instantiation the POC exhibits).

## 2. The emergent architectural property as four operational components

Mediator preservation across composition is operationally specified through four components, each of which addresses a class of composition boundary the source paper's commitments imply.

**Per-substrate mediator role.** Every substrate participating in the composition has its own mediator role, instantiated at that substrate's scope. The five mediator properties hold for every LLM operation that touches that substrate's content: reads come from the substrate as primary state, writes are under orchestration rules humans authored for that substrate, no substrate-relevant state for that substrate is held outside it, the LLM does not exercise authority over its content, and writes are recorded with attribution. The role is not an aggregate property of the composition but a property each substrate carries individually.

**Mediator role for AI in composition partners.** When the composition includes adjacent components that host substrate content of their own — under Pattern A consultation (a cell consults the adjacent component during execution) or under Pattern B derived views (the substrate's content is indexed or projected into the adjacent component) — any LLM that operates over that hosted content operates as substrate mediator within that composition partner's substrate. The role does not stop at the primary substrate's boundary and pick back up arbitrarily at the next; it holds for every LLM that operates over substrate content anywhere the composition extends. Pattern C separate-concern composition does not host coordination substrate and so does not impose the role on the adjacent component, but the test for whether a composition is Pattern C rather than Pattern A or Pattern B is itself made through the mediator role: an adjacent component is operating outside the role only if it is operating outside the coordination substrate altogether.

**Cross-substrate AI operations preserve the role at each side.** Operations spanning multiple substrates — a cell that reads from one substrate and writes to another, a derived view that aggregates multiple substrates' content, a Pattern A consultation that draws on one substrate's adjacent component while operating over a different substrate — preserve the mediator role on each substrate involved. The LLM does not become more authoritative because the operation crosses a substrate boundary; the five properties hold at the read substrate, hold at the write substrate, and hold at every substrate the operation passes through. Cross-substrate operations are operations involving two or more mediator instantiations, not operations that earn an exception from the role.

**Composition partners cannot host non-mediator AI patterns.** The composition is closed against any partner that hosts the LLM in one of the canonical non-mediator roles. A composition with one substrate satisfying the mediator role and another partner hosting LLM-as-autonomous-agent is not a CKS-coherent composition with one good substrate and one bad partner; it is a composition that fails mediator preservation at the layer where the two meet. The same holds for partners hosting LLM-as-terminal-producer (the partner's LLM produces deliverables outside any substrate write) and LLM-as-source-of-truth (the partner's LLM holds authority over content humans should hold authority over). The failure is architectural rather than aggregate; one non-mediator partner is enough.

The four components together specify what *mediator at every layer* operationally means once it is read alongside the mediator role's five properties.

## 3. What the composition forces beyond either commitment alone

The composition forces three architectural decisions that neither commitment in isolation forces.

**The mediator role is uniform across composition.** Every substrate exhibits the same five mediator properties; no substrate is exempted by virtue of being adjacent, secondary, derived, or "just an index." Uniformity is what makes mediator preservation testable as a single property rather than as a per-substrate negotiation. Composition requirements alone permits a composition in which each substrate satisfies its own commitments without specifying the relationship between them; the composition with the mediator commitment forecloses that latitude — the relationship between substrates' LLM roles is also constrained, not only the substrates themselves.

**Cross-substrate operations are specified architecturally, not procedurally.** The composition does not allow cross-substrate operations to operate the LLM as something other than mediator on the strength of the operation's complexity. An aggregating cell that reads from three substrates and writes to a fourth operates as four mediator instantiations, not as a higher-order LLM exercising authority across substrate boundaries. The mediator role does not relax under composition pressure; it holds at every layer the operation touches.

**Composition partners must be verifiable as mediator-architecture before composition.** The composition treats the mediator architecture of each prospective partner as an architectural precondition for inclusion, not as a property to be remediated after the fact. A partner that hosts LLM-as-autonomous-agent does not become CKS-coherent by being placed alongside a substrate that satisfies the mediator role; the placement makes the composition fail. The architectural test runs at composition time, not at deployment audit.

A consequence worth naming: the composition supports vendor-portability across partners. Even when partners use different LLM vendors, different fine-tunings, or different inference runtimes, the mediator role is architectural rather than vendor-specific. The five properties constrain how the LLM is operated relative to the substrate, not what the LLM is. Partners using different vendors are CKS-coherent jointly so long as each instantiates the mediator role on its own substrates; vendor diversity across partners does not threaten preservation any more than vendor singularity guarantees it.

## 4. Anti-patterns the composition specifically rules out

Four composition anti-patterns are made architecturally identifiable by the composition that neither commitment in isolation makes identifiable in the same form.

**Mixed mediator and non-mediator AI across composition.** A composition in which one substrate's LLM operates under the mediator role while another partner's LLM operates as autonomous agent — holding goals, plans, and intermediate state across multiple steps, exercising judgment about what coordination state to write — fails the composition by failing the fourth operational component. The architectural test does not depend on how the autonomous agent is implemented or how rarely it writes; it depends on whether the LLM's role on that partner's substrate is the mediator role.

**Cross-substrate operations bypassing the mediator role on one side.** An operation that reads from a CKS substrate and writes to an adjacent component without operating the LLM as mediator on the write side — for example, a cell that reads substrate state and dispatches an autonomous agent to act on an adjacent component — fails preservation at the boundary. Mediator preservation requires the role at each side of every cross-substrate operation, not at the side that matters most.

**Composition partners hosting LLM-as-terminal-producer.** A partner whose LLM produces outputs as the deliverable, with no substrate write recording the output as substrate content, fails the composition. The partner may produce useful outputs; what it does not do is operate the LLM as substrate mediator, because the mediator role requires that LLM operations affecting substrate state be recorded as substrate content with attribution. A partner that produces outputs without substrate writes has placed the LLM in a non-mediator role; the composition's commitment to mediator-at-every-layer fails at that partner.

**Composition partners hosting LLM-as-source-of-truth.** A partner whose LLM is treated as authoritative on coordination questions — whose answers are taken as the substrate's content rather than reasoning over it — fails the composition. Authority migration from substrate to LLM violates the mediator role's fourth property at the partner's scope, and violates the substrate-as-source-of-truth commitment §11.3 defends across the composition.

A common thread runs through the four. Each is a composition in which a partner has acquired, by virtue of its position, an LLM role the architecture does not name. Composition requirements names AI-as-mediator at every layer as the architectural commitment that closes the door against the unnamed roles; the composition with the mediator commitment specifies what the closure operationally requires.

## 5. Operational test

A multi-substrate composition instantiates *mediator preservation across composition* if and only if all of the following are true at every composition boundary at all times during the composition's existence.

**(e.1) Per-substrate-mediator-role.** Every substrate in the composition has a documented mediator role. For each substrate, an inspecting human can verify that the LLM operating over that substrate satisfies the five mediator properties (reads as primary state, writes under human-authored orchestration rules, no substrate-relevant state held outside the substrate, no authority over substrate content, writes recorded with attribution).

**(e.2) Cross-substrate-mediator-preservation.** For every operation that crosses a substrate boundary in the composition — including cell aggregations, derived-view updates, adjacent-component consultations, and cross-cell substrate references — the mediator role holds at each side of the boundary. The operation can be traced to a sequence of mediator instantiations rather than to a higher-order LLM action across substrates.

**(e.3) Composition-partner-mediator-architecture.** Every composition partner's LLM architecture is verifiable as mediator-architecture at composition time. No partner hosts the LLM as autonomous agent, terminal producer, or source of truth. Partners whose role in the composition is Pattern C separate-concern do not host coordination substrate and so do not require the test; the architectural verification that Pattern C applies is itself part of the test.

A composition that fails any of (e.1)–(e.3) at any boundary at any time may be a useful composition, may even be governed in some other sense, and may instantiate other valid design patterns; it is not a CKS-coherent multi-substrate composition with respect to the AI-as-mediator-at-every-layer requirement the composition-requirements commitment names.

## 6. One-sentence test

A composition preserves mediator-at-every-layer if and only if, for every substrate in the composition and for every LLM operation that touches any substrate's content, the LLM operates as substrate mediator under the five properties §2 of the mediator-commitment derivation note specifies, with no partner exempted and no cross-substrate operation excused.

## 7. What the composition is not

The composition is not the composition-requirements commitment in isolation. Composition requirements names AI-as-mediator at every layer as the fourth of five requirements but does not specify the mediator role through the five operational properties; satisfying the requirements layer does not by itself satisfy the operational-layer specification this composition produces.

The composition is not the mediator commitment in isolation. The mediator commitment specifies the role at single-substrate scope; satisfying the role at one substrate does not by itself make a composition involving that substrate CKS-coherent if other partners host non-mediator LLM patterns.

The composition is not "mostly mediator" architecture across the deployment. Mediator preservation is a property of the composition at every layer, not of the composition in aggregate. A deployment in which most LLM operations satisfy the mediator role but one partner hosts an autonomous agent does not preserve the role; partial preservation is non-preservation, because the failure mode the requirement protects against is exactly the partner where the role lapses.

## 8. Why naming this composition matters

Two reasons, and both apply to the broader cluster this note opens.

The first is intellectual. The composition-requirements commitment names five requirements; four of them — per-substrate governance, conflict preservation, addressable provenance, human-selective composition — read directly to architectural commitments the source paper defends elsewhere with their own operational specifications. The fifth, AI-as-mediator at every layer, requires the mediator commitment to supply its operational specification. Naming the composition is what writes that specification down. Subsequent notes in this cluster — composition-requirements × human-governed (governance preservation), × path retraceability (retraceability preservation), × determinism contract (determinism preservation), × hybrid composition (composition coherence) — perform the analogous specification work for the other four requirements, each through composition with the foundational commitment that supplies the operational properties.

The second is structural. Multi-substrate deployments are the common case in real organizational AI systems. A regulated coordination workflow with one CKS substrate at its center is typically embedded in a larger system with multiple substrates per organizational unit, multiple cells sharing references across substrates, and adjacent components composed under the three hybrid patterns. The architectural commitment that distinguishes a CKS-coherent composition from one that has accumulated non-mediator partners is mediator preservation; the operational specification of that commitment is the four-component property this note formalizes; the test that surfaces violations at composition time is the three-property test §5 specifies. Without the composition named, the same deployment decisions can drift into compositions in which mediator-at-every-layer fails silently — a fine-tuned partner hosting an autonomous agent, an adjacent component hosting an LLM as authoritative on coordination state, a cross-substrate operation that skips the mediator role on the write side. With the composition named, the same decisions are visible as composition decisions and can be made architecturally rather than implicitly.

The note opens a cluster of composition-pair derivations within this series. Subsequent notes in the cluster extend the same composition-pair logic across the remaining composition-requirement specifications; later clusters cover the three-adjacencies compositions, the orchestration-layer-distinction compositions, and the hybrid-systems-composition operationalizations. The cluster's contribution is the requirements-layer-meets-foundations layer that any future composition-mechanism work in CKS must satisfy — the layer at which "the composition requirement is named" becomes "the requirement is operationally what the foundation specifies."

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Mediator at Every Layer: How the AI-as-Substrate-Mediator Role Is Preserved Across Multi-Substrate Composition in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
