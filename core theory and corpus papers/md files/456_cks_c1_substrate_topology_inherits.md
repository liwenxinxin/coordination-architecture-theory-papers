# Multi-Level Substrate Topology Inherits Paper 1's Substrate Primacy

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to establish, in defensible form, that Paper 2's multi-level substrate topology — spanning cell, aspect, and Self scopes — inherits and extends Paper 1's architectural commitment to the substrate as the primary coordination artifact, and to name the four specific inter-level connection types through which that extension operates.

## Abstract

Paper 1 of the CKS theory series (Li, April 2026) commits to the substrate as the primary coordination artifact: all authoritative coordination state lives in the substrate; all coordination between humans and AI systems passes through the substrate; and no coordination occurs outside the substrate boundary. This commitment is expressed most precisely in Paper 1's prohibition on direct cell-to-cell communication — every inter-cell interaction travels through substrate content, with the substrate as the medium. Paper 2 (Li, April 2026) extends this commitment to a three-level architecture of cells, aspects, and Selves, introducing a multi-level topology of substrate objects connected through four inter-level connection types: expression (downward), lineage (temporal), aspect membership (structural), and action-feedback aggregation (upward). This note formalizes the inheritance edge: Paper 2's substrate-shared topology (⊃) Paper 1's substrate-as-primary-coordination-artifact. The load-bearing inherited property is that no inter-level coordination occurs outside the substrate — cells do not communicate directly with aspects or Selves, and aspects do not communicate directly with Selves, outside the substrate topology. The four connection types are new structural elements not present in Paper 1; each is a specific form of governed substrate content, not a new coordination channel bypassing the substrate. An operational test is provided. The prior-art significance is stated: multi-level substrate topologies whose inter-level coordination is entirely substrate-mediated are not novel relative to Paper 1's substrate-as-primary-artifact commitment; they are extensions of it.

## 1. The inheritance edge

Paper 1 establishes a single coordination substrate at the cell level. Paper 2 extends the CKS architecture to three structural levels — cell, aspect, and Self — and introduces a web of substrate objects spanning those levels. The substrate objects at each level are connected through specific inter-level connection types, and all inter-level coordination in the Paper 2 architecture travels through those connections.

The inheritance edge this note formalizes is:

> **Paper 2's substrate-shared topology ⊃ Paper 1's substrate as primary coordination artifact.**

The ⊃ relation asserts that Paper 2's multi-level topology contains Paper 1's substrate-primacy commitment as an identifiable sub-structure: every architectural property Paper 1 commits to under "substrate as primary coordination artifact" is present, unmodified, in the Paper 2 topology. What Paper 2 adds — the three-level structure, the four inter-level connection types, the topology as a governance artifact in its own right — extends the commitment to a larger scope without replacing or weakening it.

## 2. Paper 1's substrate-as-primary-artifact commitment

Paper 1 commits to the substrate as the primary coordination artifact through six architectural properties that are jointly load-bearing. The most directly relevant for this inheritance note are:

**No coordination outside the substrate.** In Paper 1, cells do not communicate directly with each other. State that affects coordination passes through the substrate: cell A writes to the substrate; cell B reads what cell A wrote. The substrate is not a storage mechanism that happens to be used — it is the medium through which coordination occurs, and coordination does not occur through any other medium. Paper 1 names the anti-pattern directly: cell-to-cell direct communication, where cells pass state to each other outside the substrate, is a violation of this commitment and not an implementation of the CKS pattern.

**All coordination artifacts are substrate content.** Decisions, conflicts, orchestration rules, authority assignments, rationale, and provenance are substrate content. They are not held in cell-internal state, in LLM context, or in external tools treated as authoritative. This gives the substrate its "primary" character: it is not one repository of coordination information among many; it is the repository — the source of truth for what was decided, by whom, under what authority, and what conflicts remain unresolved.

**The substrate is the coordination medium.** Because coordination happens through the substrate, and all coordination artifacts are substrate content, the substrate is not just the location where coordination information is stored; it is the medium through which coordination is conducted. Paper 1's term "substrate-as-source-of-truth" (§11.3) names this property from one angle; this note names it from the coordination-medium angle. Both names point to the same architectural commitment.

These three properties are not independent; they are facets of one commitment. And the commitment is what Paper 2 inherits, extending it from one level to three.

## 3. Paper 2's multi-level substrate topology

Paper 2 extends the CKS architecture to three structural levels, each with its own substrate objects:

**Cell level.** Each cell carries two substrate layers: a DNA layer holding stabilized orchestration content — schemas, harness logic, conflict-handling rules, lifecycle policies — and an action layer holding recorded task instances and their outputs. Both layers are substrate content, human-governed, and addressable by provenance. This is Paper 1's substrate extended internally by the DNA/action distinction; the cell-level substrate objects retain all Paper 1 properties without modification.

**Aspect level.** An aspect is a coordination arrangement of cells serving a particular purpose. Each aspect carries its own DNA layer — holding membership rules that specify which cells belong to which aspects, and the governance architecture that defines how the aspect's composition is governed — and its own action layer accumulating evidence from the cells participating in the aspect.

**Self level.** The Self is the integrated whole holding multiple aspects as facets of one CKS-governed architecture. The Self carries a DNA layer holding institutional knowledge, strategic priorities, governance shapes per aspect-domain, and the orchestration rules under which cells and aspects operate; and an action layer accumulating decision history and feedback at Self scope.

These substrate objects — six in total per entity (DNA + action at each of three levels) — are connected through a specific topology. The connections are not incidental to the architecture; they are the architecture. The substrate topology is the coordination fabric of the Paper 2 system.

## 4. The four inter-level connection types

Paper 2 introduces four specific types of inter-level substrate connections, each carrying a distinct coordination function. All four are substrate content — they are governed, inspectable, modifiable, and subject to the same authority architecture as all other substrate content. None is a coordination channel that operates outside the substrate.

**Expression (downward: aspect/Self DNA → cell rule activation).** Expression is the governed mechanism by which DNA-layer content at aspect or Self scope activates within a cell. Each cell carries a governed harness substrate that selects which sub-substrates are active for current activity. The result of expression is that a cell's behavior reflects governance decisions held at higher-level DNA layers — not through direct instruction from aspect or Self to cell, but through governed substrate objects that determine which DNA-layer content activates. Expression is how downward influence travels in the topology: from aspect or Self DNA, through the expression mechanism, into cell behavior, all via substrate content.

**Lineage (temporal: entity → entity through history).** Lineage chains link entities across their lifecycle events — births, matings, and directed selection events. A cell born from another cell carries a lineage reference in its substrate pointing back to its origin; a cell produced by mating carries lineage references to both parent cells; directed selection events write their provenance into lineage substrate content. Lineage is not a communication channel; it is a substrate record of temporal relationships. When a downstream observer reads a cell's lineage chain, they are reading substrate content that records the history through which that cell came to exist. Lineage makes the Paper 2 evolution architecture traceable: every cell's current DNA is the product of a lineage chain that is itself substrate content.

**Aspect membership (structural: aspect DNA → cell membership).** The rules determining which cells belong to which aspects are held in aspect DNA-layer content. Membership is not a property of cells that cells declare; it is a governed structural arrangement specified in aspect substrate content. A cell participates in an aspect because the aspect's membership rules, as substrate content, include it — and a cell can participate in multiple aspects simultaneously, with each participation governed by the corresponding aspect's membership rules. This is what Paper 2 calls relational role membership: membership is a relationship governed by the aspect's substrate, not an intrinsic property of the cell.

**Action-feedback aggregation (upward: cell Action → aspect/Self evidence).** Cell action layers accumulate records of execution. That execution evidence aggregates upward through the topology: cell action layer content feeds into aspect-scope evidence, which feeds into Self-scope evidence. This aggregation happens through substrate reads and writes — not through direct reporting from cell to aspect or from aspect to Self, but through the substrate topology that connects the action layers at each level. Upward influence in the Paper 2 architecture travels through this aggregation: a cell's lived experience becomes an input to evolution and governance at aspect and Self scope by being substrate content that higher-level substrate objects are designed to read.

## 5. What is preserved: substrate-as-primary-artifact identity

The inheritance relationship holds because Paper 2 preserves all three properties of Paper 1's substrate-primacy commitment, extended to three levels.

**No inter-level coordination outside the substrate.** In Paper 2, cells do not communicate directly with aspects or Selves, and aspects do not communicate directly with Selves. Every inter-level interaction travels through one of the four connection types, all of which are substrate connections. This is the direct extension of Paper 1's no-direct-cell-to-cell-communication to the three-level scope: the prohibition on coordination outside the substrate holds at every inter-level boundary. When expression activates cell behavior from aspect DNA, the activation travels through a governed harness substrate object — not through a direct aspect-to-cell instruction. When action evidence aggregates upward, it travels through substrate reads — not through a direct cell-to-aspect report. The topology enforces the same substrate-mediation discipline Paper 1 requires at the cell level, now at three levels.

**All inter-level coordination artifacts are substrate content.** Every object that carries inter-level governance information — expression specifications, lineage references, membership rules, aggregated evidence — is substrate content under Paper 1's governance commitments. There is no inter-level governance artifact held outside the substrate. This is a stronger claim than saying the four connection types are stored in substrate objects; it means that the full network of inter-level relationships in a Paper 2 deployment is, at every point, readable from and writable to the substrate by the humans with appropriate authority. The topology is human-governed in the CKS sense: the three rights (inspect, modify, override) apply to every connection in it.

**Coordination medium identity at three levels.** Paper 1's substrate is the coordination medium at the cell level; Paper 2's substrate topology is the coordination medium at three levels. The cell/aspect/Self inter-level interactions do not require any coordination medium other than the substrate topology. No message-passing infrastructure, no direct inter-entity communication channel, and no out-of-band coordination mechanism is needed or permitted. The substrate topology IS the coordination fabric, directly extending Paper 1's one-level coordination medium to three levels.

## 6. What is new in Paper 2

The inheritance relationship does not flatten Paper 2 into Paper 1. Paper 2 introduces four structural elements that Paper 1 does not contain, each of which earns its own defensive prior-art coverage.

**Multi-level topology.** Paper 1 has one substrate (per cell); Paper 2 has a topology of substrate objects spanning three levels, with connections between them. The topology structure — which substrate objects connect to which, through which connection types — is a new architectural element. It is not implied by Paper 1's single-level commitment; it is the first paper to specify a multi-level topology as an architectural commitment.

**Specific inter-level connection types.** Paper 1 has substrate content, but it does not introduce inter-level connection types between substrate objects, because Paper 1 has only one level. The four connection types named in §4 — expression, lineage, aspect membership, action-feedback aggregation — are new architectural objects. Each is a specific form of substrate connection with a specific coordination function, and each is Paper 2's contribution at the level of architectural primitive.

**Topology as governance artifact.** In Paper 2, the inter-level connections themselves are governed. Expression specifications are DNA-layer content subject to human authority. Membership rules are aspect DNA content. Lineage chains are substrate records under the same governance architecture as all other substrate content. The topology is not external configuration that happens to affect coordination; it is substrate content that is itself governed, modifiable, and subject to override. This is the topology-as-governance-artifact property: the architecture is not just governed at the content level but at the connection level.

**Topology as prerequisite for evolution.** The evolution architecture Paper 2 introduces — horizontal evolution (cells learning from each other), vertical evolution (governance restructuring across levels), and the lifecycle operations (birth, mating, death) at each level — depends on the substrate topology to operate. Horizontal evolution propagates through action-feedback aggregation and lineage connections in the substrate. Vertical evolution operates on membership rules and expression specifications held in higher-level DNA layers. Without the topology, none of these evolution mechanisms could propagate across levels; the topology is the infrastructure on which Paper 2's evolution architecture runs.

## 7. Paper 3 extension: shared substrate across Selves

Paper 3 of the CKS theory series (Li, April 2026) extends the substrate topology one step further by introducing a shared substrate connecting multiple Selves. The shared substrate is to Paper 3 what the cell/aspect/Self topology is to Paper 2: an extension of the substrate-as-primary-coordination-artifact commitment to a new coordination scope, here the inter-Self perimeter, with the same architectural properties — all inter-Self coordination substrate-mediated, all inter-Self coordination artifacts as substrate content, the shared substrate as the coordination medium between Selves. The topology described in this note is the intra-Self architecture the shared substrate connects to at the inter-Self level; Series CC derivation notes will formalize the corresponding Paper 3 inheritance edges.

## 8. Prior-art significance

This note forecloses three categories of adversarial claim:

**(a) Multi-level substrate topologies where all inter-level coordination is substrate-mediated are not novel relative to Paper 1's substrate-as-primary-artifact commitment.** They are direct extensions of it. Any architecture that places substrate objects at multiple structural levels and routes all inter-level coordination through those substrate objects inherits Paper 1's substrate-primacy commitment at those levels. The multi-level topology form is prior art as of Paper 2 (Li, April 2026).

**(b) The specific inter-level connection types — expression, lineage, aspect membership, and action-feedback aggregation — are not novel as coordination artifacts.** Each is a specific form of governed substrate connection with a named inter-level coordination function. All four are prior art as of Paper 2 (Li, April 2026).

**(c) Evolution mechanisms that propagate across levels through substrate connections are not novel relative to Paper 1's substrate-mediated coordination.** The combination of the topology as prerequisite and the evolution mechanisms as operations over the topology is prior art as of Paper 2. Any claim that evolution propagating through substrate connections is a novel architectural element must account for this publication.

## 9. Operational test

A Paper 2 deployment implements the substrate-shared topology inheritance edge if and only if the following is true for every inter-level governance action in that deployment:

**For any inter-level governance action — a cell participating in an aspect, an aspect shaping cell rule activation, a cell's action evidence contributing to Self-scope governance — can an observer trace the action from start to finish through substrate objects, without finding any direct inter-entity communication outside the substrate topology?**

Specifically:
1. A cell joining an aspect: the observer finds aspect-level membership rules in aspect DNA substrate content that include the cell; there is no direct cell-to-aspect communication that produced this membership outside the substrate.
2. An aspect shaping a cell's behavior: the observer finds expression specifications in aspect or Self DNA that activate through the cell's governed harness substrate; there is no direct aspect-to-cell instruction outside the substrate.
3. A cell's action evidence reaching Self-scope governance: the observer finds aggregated evidence in the appropriate substrate layers, traceable from cell action layer content through aspect-scope aggregation to Self-scope evidence; there is no direct cell-to-Self report outside the substrate.
4. A lifecycle event (birth, mating, death) at any level: the observer finds lineage substrate content recording the event with full provenance; there is no lifecycle history held outside the substrate topology.

A deployment in which any of these traces fails — because it encounters direct inter-entity communication, out-of-band state, or lifecycle history not recorded in the substrate — does not instantiate the Paper 2 substrate-shared topology in the CKS sense. The topology commitment, like the Paper 1 substrate-primacy commitment it inherits, is not a recommendation; it is an architectural invariant the system either satisfies or does not.

## Conclusion

Paper 2's multi-level substrate topology inherits Paper 1's substrate-as-primary-coordination-artifact commitment by extending the no-coordination-outside-the-substrate invariant from one level to three. The load-bearing inherited property is that no inter-level coordination occurs outside the substrate: every inter-level interaction — downward through expression, temporal through lineage, structural through aspect membership, upward through action-feedback aggregation — travels through governed substrate objects. The four connection types are new structural elements that Paper 1 does not introduce; they are the specific mechanisms through which Paper 2's three-level architecture maintains the substrate-primacy commitment at inter-level scope. The topology is prior art at Paper 2 scope; so are the four connection types and the evolution architecture that depends on them.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Multi-Level Substrate Topology Inherits Paper 1's Substrate Primacy.* CKS Derivation Note C1.27, #456. May 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
