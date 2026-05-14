# Multi-Shaped Governance as Paper 2's Fifth Architectural Claim

*A derivation note from the Coordination Knowledge Substrate (CKS) pattern.*

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize Paper 2's fifth architectural commitment — multi-shaped governance — as a named claim, and to map the derived sub-commitments under it.

## Abstract

Paper 2 defends six architectural commitments through six claims. Conventional reading treats the first — the instinct/reasoning separation — as "the paper's claim" and the remaining five as supporting structure. The remaining five in fact carry equal architectural weight, and the fifth carries weight that downstream work routinely needs but rarely cites by name. This note formalizes Paper 2's fifth claim as a standalone commitment and serves as the parent anchor for the Series B sub-commitments derived from it. The claim commits human governance across the Self's evolution as *multi-shaped*: distinct governance shapes co-determined with the distinct evolution mechanisms Claim 4 establishes, the instinct/reasoning boundary as governed substrate content rather than fixed architectural property, and distinct death-type governance processes per cause. The architectural prior art is not that governance exists, but that governance *shape* is plural, authored, and substrate-resident rather than uniform and overlaid as mechanism-agnostic policy.

## 1. The claim stated precisely

In the CKS pattern as extended by Paper 2, a Self holds **multi-shaped governance** if and only if the three following commitments hold simultaneously and as properties of the system's architectural design.

1. **Per-mechanism governance shape.** Each of Claim 4's three evolution mechanisms — instinct evolution, DNA evolution, action-feedback evolution — operates under a distinct governance shape co-determined with the mechanism's shape rather than overlaid as mechanism-agnostic policy. The three shapes specified in Paper 2 §8.2 are verification-substrate machinery for instinct evolution, an authority architecture for DNA evolution, and a proposal-and-acceptance machinery for action-feedback evolution.
2. **The instinct/reasoning boundary as substrate content.** The line dividing what the instinct layer handles (fast-pattern, LLM-mediated) from what the reasoning layer handles (deliberate, substrate-mediated) is itself authored substrate content subject to the inspect, modify, and override rights Paper 1 Claim 3 establishes — not a fixed architectural property, not a vendor configuration, not an emergent consequence of LLM capability.
3. **Distinct death-type governance processes.** Each of the death types Paper 2 Claim 3 names — functional obsolescence (deletion) and lineage supersession (archival), with capability supersession as the evolution-driven succession-variant of lineage supersession — operates under a per-cause decision process appropriate to the irreversibility profile of the resulting architectural action.

The commitment is *architectural*: each of the three properties must be available as a property of the system's design, not as a procedural promise that depends on a particular deployment, vendor, or workflow. The commitment is also *plural*: different entities within the same deployment can carry different values for each of the three commitments and remain governance-coherent. Multi-shaped governance is the architectural commitment that this plurality is *authored* rather than tolerated.

## 2. Why "multi-shaped" is the load-bearing modifier

Governance is a saturated term. The published landscape carries it from at least three other domains — biological regulation (feedback-driven), political theory (consensus-driven), and corporate compliance (audit-driven) — each importing connotations the CKS pattern does not adopt (Paper 2 §8.1). What Paper 2 Claim 5 commits to is authority-driven governance, instantiated as substrate machinery rather than overlaid as policy. The *multi-shaped* modifier carries two specific commitments inside that broader frame.

**Shape co-determined with mechanism.** Different evolution mechanisms demand different governance machinery, and Paper 2 §8.2 specifies the three shapes separately rather than as parameterizations of one shape. Instinct evolution is governed through verification substrates that gate integration on outcomes against substrate-authored test surfaces. DNA evolution is governed through an authority architecture decomposing proposal, authorization, verification, and reversion rights — itself substrate content recursively governable under the same rights it instantiates. Action-feedback evolution is governed through a proposal-and-acceptance machinery in which recorded action produces substrate-change proposals subject to authorization rather than autonomous writes. These three are architecturally distinct machineries, not knob-settings of one machinery, and the multi-shaped commitment requires them to be co-resident.

**Diversity across entities is governed plurality, not inconsistency.** Within a single Self — and within an enterprise deployment of multiple Selves — different entities can carry different instinct/reasoning boundary specifications, different death-type applicability rules, and different per-mechanism shapes. A clinical-care-delivery aspect may pin high-stakes diagnostic decisions to the reasoning layer regardless of how capable instinct becomes; a routine-correspondence aspect in the same Self may delegate similarly-shaped tasks to instinct (Paper 2 §10). The architecture commits that this divergence is itself authored substrate content under the three rights, not an inconsistency to be reconciled. *Authored* plurality is what makes the property architectural rather than incidental.

## 3. The three components in detail

### 3.1 Per-mechanism governance shape

For each evolution mechanism, the governance shape carries its own machinery and its own substrate footprint. **Instinct evolution's verification substrate** is a set of test surfaces — authored as substrate content — against which a candidate upstream change is run before integration is authorized; the decision logic is gate-on-outcome. **DNA evolution's authority architecture** decomposes who can propose substrate changes, who can authorize, what verification regime applies, and what reversion paths exist; the architecture is itself substrate content, recursively governable, with software-engineering neighbors in Apache PMC-style decomposition and GitHub CODEOWNERS-style role specification (Paper 2 §8.2). **Action-feedback evolution's proposal-and-acceptance machinery** treats recorded action as a source of governance-checked proposals; an unaccepted proposal does not modify the DNA layer, which keeps action-feedback from silently drifting governed substrate without authorization.

The three shapes share Paper 1 §3.3's authority-vs-labor distinction — humans own authority over rules, acceptance criteria, and verification regimes; labor is allocable. What they differ on is the machinery instantiating the authority, and that differentiation is what Component 1 commits to.

### 3.2 The instinct/reasoning boundary as substrate content

The boundary between instinct and reasoning is the load-bearing structural commitment Paper 2 Claim 1 establishes. Claim 5 commits the further property that the boundary's *location* — which cells, which decisions, which substrates fall on which side — is authored substrate content rather than fixed at architecture-instantiation time. Where the boundary sits is configurable per cell, per aspect, and per aspect-domain; it is inspectable, modifiable, and overridable under the same three rights Paper 1 Claim 3 commits to for all substrate content. As instinct sharpens with LLM capability, previously-reasoned decisions may architecturally collapse to instinct under governed boundary-tuning; conversely, as new safety-critical paths emerge, additional reasoning substrates may be added under the same machinery (Paper 2 §8.3). The boundary is dynamic governance content, not static architecture.

The differentiation against the published landscape's dominant pattern is sharp. SOFAI's S2-to-S1 skill migration treats boundary-shift as automated property of a metacognitive controller; the boundary moves as the system observes itself doing well on certain decision types. Claim 5's commitment is different: the boundary moves only under explicit human-authored substrate change.

### 3.3 Distinct death-type governance processes

Paper 2 Claim 3 names two primary death types and Claim 4 names capability supersession as their evolution-driven succession-variant within the lineage-supersession territory. The three architectural results are distinct:

- **Functional obsolescence** results in deletion (irreversible). Resource release follows; the substrate is no longer addressable.
- **Lineage supersession** results in archival (reactivatable). The retired substrate remains addressable at the same identifier for audit and historical reference; the system is designed to resolve the identifier into the prior state.
- **Capability supersession** — the evolution-driven case where a substrate's function is now handled elsewhere — proceeds as either standard lineage supersession (retired-with-archival) or as retained-as-fallback (architectural option preserved for safety-critical paths).

Claim 5 commits that the applicability of each death type is authored substrate content. Governance must determine which death type applies *before* closure; ad hoc retirement, unauthored at the moment of closure, is the failure mode this component defends against. The two-type architectural distinction — irreversible deletion versus reactivatable archival — binds different governance shapes because the irreversibility profile is what makes the per-cause distinction load-bearing rather than parameterizable. Mature software-engineering practice (PEP 387, API lifecycle, Microsoft Purview) treats retirement as one primitive with type-specific parameters; Claim 5 adds per-cause governance machinery rather than unified-with-parameters processing (Paper 2 §8.4).

## 4. Composition with Claim 2's content-domain framing

Paper 2 Claim 2 (§5.2) establishes that aspects operate over their constituent cells as *content domain*, with multiple aspects coexisting within one Self and potentially sharing cells across arrangements. Multi-shaped governance composes naturally with this content-domain framing: the per-mechanism governance shapes, the instinct/reasoning boundary specification, and the death-type applicability rules are themselves authorable *per aspect-domain*. Paper 2 §10's healthcare rendering makes the composition concrete — clinical-care-delivery, regulatory-and-quality-reporting, financial-and-operations, and institutional-learning aspects each carry their own governance shape per Claim 5, with cross-aspect content (such as HIPAA-governed patient data) propagating across aspect-domains under aspect-specific governance.

This composition is an inheritance, not a fourth Claim 5 component. The content-domain specification of an aspect lives as substrate content under Paper 1 Claim 3's three rights independently of Claim 5; Claim 5 adds that the governance shape carried over that content domain is per-mechanism, per-boundary, and per-death-type plural.

## 5. Inheritance and what is new

**Inherited from Paper 1.** All six Paper 1 architectural commitments hold. Most load-bearing for Claim 5 is the authority-vs-labor distinction at Paper 1 §3.3: humans own authority; labor is allocable. The three rights from Paper 1 Claim 3 — inspect, modify, override — apply to every governance-configuration item Claim 5 names as substrate content. The substrate/LLM division at the governance boundary (Paper 1 §4) holds across all three per-mechanism shapes. The linear-cost commitment (Paper 1 §6) underwrites archival and fallback retention without superlinear scaling cost.

**Inherited from prior Paper 2 claims.** Claim 1 establishes the instinct/reasoning separation Component 2 specifies as governed boundary. Claim 2 establishes the three-level structure and the DNA/action layer distinction the three governance shapes operate on. Claim 3 establishes the lifecycle primitives Component 3 specifies governance machinery for. Claim 4 establishes the three evolution mechanisms Component 1 specifies per-mechanism shapes for.

**New in Claim 5.** What Claim 5 contributes beyond Paper 1 and Paper 2's prior claims is the specific identification of three governance-configuration items as authored substrate content: per-mechanism shape machinery, the instinct/reasoning boundary location, and death-type applicability. The architectural prior art is the move from "governance exists" to "governance shape is authored, plural, and substrate-resident under the three rights."

## 6. Failure modes the claim defends against

Four failure modes the claim explicitly precludes.

1. **Mechanism-agnostic governance policy.** A single uniform governance policy applied to instinct, DNA, and action-feedback evolution alike — typically rendered as document or training-time constitution — fails the per-mechanism shape commitment. The published landscape's dominant pattern is this shape, and Paper 2 §8.2 differentiates against it directly.
2. **Static instinct/reasoning boundary.** A boundary hardwired by the architecture, the vendor, or the LLM's emergent capability — not authored as substrate content, not inspectable, not modifiable under the three rights — fails Component 2. SOFAI-style automated S2-to-S1 skill migration is the closest architectural neighbor (Paper 2 §4.3, §8.3).
3. **Undifferentiated death-type governance.** Treating retirement as one parameterized primitive with shared decision process — even when underlying causes differ in irreversibility — fails Component 3 by collapsing the per-cause architectural distinction the source paper defends (§8.4).
4. **Uniform governance shape across entities.** Forcing all entities in a deployment into one governance configuration — same boundary location, same death-type applicability, same per-mechanism shape — collapses the multi-shaped property to single-shaped and forfeits the per-aspect-domain composition Claim 5 enables.

## 7. Operational test

A Self instantiates Paper 2 Claim 5's multi-shaped governance commitment if and only if, for any entity in the deployment, an observer with appropriate access can locate within the substrate:

1. The applicable per-mechanism governance shape for instinct evolution, DNA evolution, and action-feedback evolution as it applies to the entity, with the governance machinery — verification surfaces, authority decomposition, proposal-and-acceptance routing — inspectable as substrate content.
2. The entity's instinct/reasoning boundary specification, with the boundary location authored, inspectable, and modifiable under Paper 1 Claim 3's three rights.
3. The entity's applicable death-type rules authored as substrate content, with the per-cause decision process specified *before* any closure event.
4. Confirmation that different entities in the deployment can — and where appropriate, do — carry different values for items (1), (2), and (3), without any architectural mechanism forcing uniformity.

A system that fails any of (1)–(4) may be a useful system, and may be governed in some other sense, but is not multi-shaped-governed in the CKS sense.

## 8. Derived sub-commitments mapped

Per the Series B enumeration in the master plan, the following B1.xx and B3.xx notes are derived from Claim 5 and find their parent anchor here.

**Phase B1 — foundational sub-commitments:**

- **B1.15** — Multi-shaped human governance across evolution mechanisms (umbrella; parent of B2.79–B2.86).
- **B1.16** — The instinct/reasoning boundary as governed substrate content (Component 2).
- **B1.17** — Verification substrates as governance over instinct integration (one per-mechanism shape within Component 1; parent of B2.87–B2.94).
- **B1.18** — Distinct death-type governance processes, including the per-cause distinction between functional obsolescence and lineage supersession with capability supersession as evolution-driven succession-variant (Component 3).

**Phase B3 — anti-pattern formalizations:**

- **B3.19** — Undifferentiated death-type governance (Failure mode 3 above).
- **B3.20** — Instinct evolution without verification governance (one face of Failure mode 1, specific to the instinct-evolution shape).
- **B3.27** — Instinct/reasoning boundary as static configuration (Failure mode 2).
- **B3.30** — Structural rigidity versus structural co-adaptation with human organization (Failure mode 4 at organizational scope, where uniform shape forecloses per-aspect-domain composition).

Operational variants under Phase B2 and operational tests under Phase B5 inherit from this anchor transitively through their B1.xx parents. The anchor introduces no commitments beyond what the source paper §8 already defends; its function is to give the B1.xx and B3.xx sub-commitments an explicit named-claim parent.

## 9. Conclusion

The fifth of Paper 2's six architectural commitments is multi-shaped governance: distinct governance shapes co-determined with distinct evolution mechanisms, the instinct/reasoning boundary as governed substrate content, and distinct death-type governance processes per cause. The contribution is not that governance exists; it is that governance *shape* is plural, authored within the substrate, and inspectable per entity. The multi-shaped property — different entities in the same deployment can carry different values for each governance-configuration item under explicit authoring — is what distinguishes the commitment from the mechanism-agnostic policy overlays, static architectural boundaries, and undifferentiated retirement primitives the surrounding landscape dominantly carries.

Subsequent Series B notes derive sub-commitments under this anchor without restating the umbrella. Subsequent work that adopts, extends, composes with, or argues against the CKS pattern should use "multi-shaped governance" in the sense formalized here; subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Multi-Shaped Governance as Paper 2's Fifth Architectural Claim.* May 14, 2026. ORCID: 0009-0004-8065-3235.
