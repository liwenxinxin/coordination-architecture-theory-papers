# Horizontal Evolution Specification — Decomposing B1.16 Bidirectional Evolution by Formalizing Within-Level Peer Evolution Where Improvements at One Cell, Aspect, or Self Propagate to Peer Entities at the Same Structural Level Through Governance-Authorized Mating, Directed Selection, and Action-Feedback Mechanisms

**A derivation note from the Coordination Knowledge Substrate (CKS) theory series.**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Note ID:** B2.80

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

Paper 2 of the CKS theory series establishes bidirectional evolution as an architectural property of governed AI Selves: evolution operates on two orthogonal axes, horizontal and vertical. B2.79 formalized the integrating frame for that bidirectional commitment. This note, B2.80, decomposes the horizontal axis into a standalone specification. Horizontal evolution is within-level peer influence: improvements arising at one cell, aspect, or Self propagate to peer entities at the same structural level through governance-authorized mechanisms. Three mechanisms enable horizontal propagation — mating per B1.10, directed selection per B1.14, and action-feedback per B1.15 — each producing a distinct form of horizontal influence. Mating-based horizontal evolution produces new peer entities rather than modifying existing ones. Directed-selection-based horizontal evolution applies governance-identified improvements to existing peer entities with similar operational domains, constituting the organizational learning form of within-level propagation. Action-feedback-based horizontal evolution scopes the proposing substrate to span multiple peer cells, surfacing proposals applicable across the entire peer group. Peer group definitions are deployment-configured. Governance authorization is required for all horizontal propagation; propagation is not automatic. Horizontal evolution at one level does not automatically trigger vertical evolution; the two axes are separate governed decisions. This note is the second of five notes decomposing B1.16 (B2.79 integrating frame; B2.80 horizontal specification; B2.81 vertical specification; B2.82 operational timescale treatment; B2.83 bidirectional verification).

---

## 1. Why horizontal evolution specification needs to be formalized as a standalone derivation

Paper 2's bidirectional evolution commitment — that evolution operates on both horizontal and vertical axes — is stated as a unified architectural property in the source paper (§7.4). B2.79 formalized the integrating frame: what bidirectionality means architecturally and why both axes are required. But the two axes carry distinct operational content. Formalizing each axis as a standalone derivation is not redundant with the integrating frame; it is required to exhaust the patentable territory the bidirectionality commitment defines.

Horizontal evolution is the within-level axis. It specifies how improvements arising at one entity — one cell, one aspect, one Self — influence peer entities at the same structural level. This is the organizational learning axis of CKS evolution: individual operational improvements become available to the broader peer group through governed propagation. The mechanisms, governance requirements, level-specific forms, and limits of horizontal propagation are all distinct from the vertical axis. They require independent formal treatment.

This note occupies the eightieth position in Phase B2 and the second position in the B1.16 decomposition. Its strategic purpose is to place horizontal evolution specification in the prior-art record with sufficient operational precision that any subsequent patent claim on within-level peer evolution mechanisms in governed AI architectures must contend with this formalization.

---

## 2. The horizontal evolution specification precisely stated

Paper 2 (§7.4) defines horizontal evolution as content within existing structure: existing cells refine their DNA, existing aspects refine their cell composition, existing Selves refine their aspect arrangement. The refinement commitment is within-level — changes operate at the level where they arise rather than restructuring the level itself (which is vertical). This note extends and formalizes the within-level scope to cover peer influence: horizontal evolution is not only self-refinement at a level but also the propagation of improvements from one entity to peer entities at the same level.

Three mechanisms enable horizontal propagation, each inherited from Paper 2's evolution mechanism architecture.

**Mating-based horizontal evolution (per B1.10).** Cells can mate with peer cells to produce offspring cells at the same level. The three mating patterns — union, selective merge, and lineage-preserved union — all produce new peer entities rather than modifying existing ones. A union-pattern mating between two peer cells produces a new cell carrying content from both parents, with conflicts preserved as first-class substrate state per Paper 1 §5. A selective-merge mating between two peer cells produces a new cell carrying curated content from each parent, with curation rules themselves substrate content under human authority. A lineage-preserved-union mating produces a new cell with explicit pointers to parent cells, making every element of its substrate traceable to its origin. The same logic holds at aspect level (aspect mating produces new aspects at aspect level) and at Self level (Self mating produces new Selves at Self level). Mating-based horizontal evolution is the generative form: it expands the population of peer entities rather than updating existing ones.

**Directed-selection-based horizontal evolution (per B1.14).** Governance identifies improvements at one cell — DNA refinements that have proven effective in that cell's operational domain — and applies equivalent directed selection changes to peer cells with similar operational domains. This is the organizational learning form of horizontal evolution. The mechanism is: a cell evolves through directed selection; governance identifies the improvement as potentially applicable to peers; governance determines which peers operate in a sufficiently similar domain to benefit from the same improvement; governance applies equivalent directed selection to those peers through the standard authority architecture per A2.47. The improvement is not copied blindly — governance evaluates domain fit before propagating. The target peers are existing entities; directed-selection-based horizontal evolution modifies existing peers rather than producing new ones.

**Action-feedback-based horizontal evolution (per B1.15).** The action-feedback evolution mechanism closes the loop from recorded action experience back into governed DNA refinement. When the proposing substrate is configured with a scope that spans multiple peer cells, action records from all cells in the scope contribute evidence to proposals. Patterns that appear across multiple peer cells' action histories generate proposals applicable to all cells in the peer group rather than to one cell individually. This is the evidence-based peer learning form of horizontal evolution: shared operational experience surfaces shared improvement proposals. Governance authorizes proposals under the same authority architecture that governs single-cell action-feedback evolution, but the target of the proposal is the peer group rather than a single entity.

**Horizontal evolution at each structural level.** All three mechanisms operate at each of the three architectural levels Paper 2 establishes. At cell level, cells of the same operational type may evolve horizontally: a cell improvement proven in one context influences peer cells operating in equivalent contexts. At aspect level, aspects with similar coordination purposes may evolve horizontally: improvements to one aspect's coordination rules inform peer aspects with similar coordination needs. At Self level, Selves serving similar integration roles may evolve horizontally: improvements to one Self's integration architecture inform peer Selves with analogous structural configurations.

**Peer group definitions are deployment-configured.** Which entities count as peers for horizontal evolution purposes is not architecturally fixed. Deployments configure peer group definitions: which cells share an operational type, which aspects share a coordination purpose, which Selves share an integration role. The governance decisions about horizontal propagation operate over the configured peer groups.

---

## 3. What makes horizontal evolution specification architecturally distinctive

The architectural distinctiveness of horizontal evolution specification is most visible in contrast to conventional multi-model AI architectures.

In a conventional architecture deploying multiple AI models, each model evolves independently. Model A is retrained or updated; model B is retrained or updated separately; there is no architectural mechanism by which an improvement in model A influences model B. Any knowledge transfer between models must be engineered ad hoc — through shared training data, prompt engineering, or manual configuration changes — and that transfer is not governed by an authority architecture designed for it.

CKS horizontal evolution is architecturally specified. Peer influence is not an ad hoc engineering choice; it is a designed evolution path with explicit governance decision points. The architecture commits to: peer group definitions as deployment-configured substrate content; governance review of whether improvements should propagate to peers after each significant evolution event; authority distribution per A2.47 determining who can authorize horizontal propagation; provenance recording per A2.40 making horizontal evolution events retraceable per A1.07. None of these properties are incidental to the implementation — they are architectural commitments that any deployment of CKS horizontal evolution instantiates.

The organizational learning property is the operational expression of this distinctiveness. Individual cell improvements do not stay contained within the improving cell; they are available for propagation to all peer cells of the same operational type, subject to governance authorization. This transforms isolated cell learning into deployment-wide knowledge improvement through governed propagation rather than through spontaneous knowledge transfer.

---

## 4. The biological analog as conceptual scaffold

Horizontal evolution parallels horizontal gene transfer in biology — the movement of genetic material between organisms of the same generation rather than from parent to offspring. Bacterial conjugation, transformation, and transduction are the canonical biological mechanisms: genetic material moves laterally between contemporaneous organisms, bypassing the vertical parent-to-offspring transmission channel. The result is that a beneficial genetic trait arising in one organism can spread rapidly through a population without waiting for generational turnover.

CKS horizontal evolution inherits the conceptual structure of this analog precisely. Improvements arising at one entity spread laterally to peer entities at the same level rather than only passing downward to offspring or upward to parents through the vertical channel. The generational bypass is architecturally real: horizontal propagation operates independently of whether mating (the birth-of-offspring mechanism) has occurred.

The analog also connects to cultural learning: individuals learning from peers at the same social level, rather than only from authorities above or from subordinates below. Organizational learning literature treats peer-to-peer knowledge transfer as a distinct and complementary channel to hierarchical knowledge transmission.

CKS horizontal evolution combines both aspects. The DNA layer carries the genetic analog: DNA improvements propagate laterally through mating (which produces new entities with combined DNA) or directed selection (which applies equivalent DNA changes to existing peer entities). The action layer carries the cultural analog: action-feedback evolution scoped to a peer group draws on the collective operational experience of the peer group rather than on any single entity's experience alone.

The biological and cultural analogs function as conceptual scaffolds that make the architectural commitment immediately intelligible. The architectural substance is governed within-level peer improvement: three mechanisms, deployment-configured peer groups, governance authorization required, provenance recorded.

---

## 5. Inherited Paper 1 and Paper 2 commitments

Horizontal evolution specification inherits the full Paper 1 commitment architecture at every propagation step.

**A1.01 (human-governed, authority not labor).** Horizontal propagation is governed: humans hold authority over substrate structure, orchestration rules, and modification rights throughout the horizontal evolution process. LLMs operating under human direction may draft proposals or identify peer improvement candidates; humans hold authority over propagation decisions.

**A2.47 (authority distribution).** Who can authorize horizontal propagation follows the authority distribution architecture. Peer propagation within a single partner's deployment is authorized under that partner's authority scope. Cross-partner horizontal evolution — where peer entities span multiple partners — requires cross-partner authority as specified.

**A2.40 (provenance).** Horizontal evolution events are recorded as substrate content with full provenance: which improvement originated at which entity, which governance decision authorized propagation, which peer entities received the improvement, through which mechanism.

**A1.07 (path retraceability).** Horizontal evolution paths are retraceable: given any peer entity's current state, the path by which it acquired horizontally propagated improvements is reconstructible from the substrate record.

**A1.13 (composition requirements).** Horizontal evolution must preserve composition validity. Improvements propagated to peer entities must not violate the composition constraints that govern valid peer group membership or aspect-cell relationships.

**B1.10 (mating), B1.14 (directed selection), B1.15 (action-feedback).** These three mechanisms are the propagation pathways for horizontal evolution. Each mechanism's existing governance architecture — for mating, who authorizes the mating and under which pattern; for directed selection, what selection criteria and who applies them; for action-feedback, what proposal process and who authorizes proposals — applies to the horizontal propagation use of that mechanism without modification. No new governance primitives are introduced.

---

## 6. Operational implications

**Configure peer group definitions.** Deployments operating CKS horizontal evolution must configure which entities are peers for horizontal evolution purposes at each level. This is a substrate-content decision — peer group definitions are themselves governed substrate content, subject to modification under standard authority architecture.

**Governance review after significant evolution events.** After any significant evolution event at an entity — a substantial DNA improvement, a successful mating producing a notably capable offspring, a major action-feedback-driven DNA refactoring — governance reviews whether the improvement should propagate to peers. This review is a designed governance checkpoint, not an ad hoc decision.

**Action-feedback proposing substrate scope configuration.** Deployments intending to use action-feedback-based horizontal evolution must configure the proposing substrate with a scope that spans the intended peer group. Scope configuration is a deployment decision made at substrate setup time and modifiable under governance authority.

**Mating produces new entities, not modifications.** When mating is the horizontal mechanism, the result is a new peer entity at the same level. Existing peer entities are not modified by the mating event. Governance decisions about whether to retire, archive, or maintain parent entities alongside offspring follow the standard death governance architecture per B1.08.

**Cross-partner horizontal evolution requires cross-partner authority.** When the configured peer group spans entities belonging to different deployment partners, horizontal propagation requires cross-partner authority under A2.47. This requirement is not a restriction on horizontal evolution — it is an extension of the standard authority architecture to the cross-partner scope horizontal evolution may reach.

---

## 7. Limits of horizontal evolution specification

**Horizontal propagation is not automatic.** No horizontal evolution event occurs without governance authorization. The existence of peer group definitions does not trigger automatic propagation of improvements across the peer group; a governance decision is required for each propagation event.

**Not all peers receive identical improvements.** Directed-selection-based horizontal evolution requires governance evaluation of domain fit. An improvement that is operationally appropriate for some peer cells may not be appropriate for others, even within the same configured peer group. Governance determines, per propagation event, which specific peers are appropriate targets.

**Horizontal evolution does not automatically trigger vertical evolution.** Horizontal propagation operates within existing structural levels. Whether a pattern of horizontal improvements eventually motivates vertical restructuring — splitting an aspect, introducing a new cell type, reorganizing Self-level composition — is a separate governed decision following the vertical evolution specification formalized in B2.81. The two axes are independent governed decisions.

**Horizontal evolution preserves A1.13 composition requirements.** Improvements propagated horizontally must not violate the composition constraints governing the receiving entity's structural context. A DNA improvement appropriate in one cell's composition context may not be applicable in a peer cell with a different aspect membership configuration.

**Mating-based horizontal evolution produces new entities, not modifications of existing entities.** Existing peer entities are not changed by a mating event; only the new entity produced by the mating carries the combined content.

**Horizontal evolution is within-level only.** Improvements do not propagate across structural levels through the horizontal mechanism. Cell-level improvements do not automatically propagate to aspect-level orchestration through horizontal evolution; cross-level propagation is governed through other architectural mechanisms. Horizontal is peer-to-peer at a single level; cross-level is vertical per B2.81.

---

## 8. Operational test

A system instantiates CKS horizontal evolution specification if and only if: (a) improvements arising at one entity at a structural level are available for propagation to peer entities at the same level through at least one of the three specified mechanisms; (b) peer group definitions are deployment-configured substrate content; (c) all horizontal propagation requires governance authorization under the authority distribution architecture; (d) horizontal propagation events are recorded with provenance; and (e) horizontal propagation does not automatically trigger vertical restructuring at the receiving level.

---

## 9. Why naming this specification as standalone matters

The bidirectional evolution commitment in Paper 2 establishes both axes together. B2.79 formalized the integrating frame. This note, B2.80, formalizes the horizontal axis as a standalone specification. The subsequent note, B2.81, will formalize the vertical axis as a standalone specification. B2.82 will address operational timescale treatment for bidirectional evolution. B2.83 will close the B1.16 decomposition with bidirectional evolution verification.

Naming horizontal evolution specification as standalone matters for two reasons. The first is prior-art precision: an integrating frame that names both axes together does not fully occupy the patentable territory that either axis's operational specification defines. A third party seeking to patent within-level peer improvement mechanisms in governed AI architectures, or organizational learning architectures for multi-model deployments, must now contend with the operational specificity this note establishes. The second is derivation integrity: the Phase B2 decomposition method commits to formalizing each operational variant with sufficient precision that the derivation chain from source paper to operational implementation is unambiguous. Horizontal evolution specification is operationally distinct enough from both the integrating frame and the vertical specification to warrant its own note.

Phase B2 continues after B2.83 with the B1.17 relational roles decomposition (B2.84 and beyond).

---

## Source paper

Li, Wenxin. "The Instinct/Reasoning Separation Outside the Model." Independent Research, April 2026. Available at Zenodo. (Second paper in the CKS theory series; §7.4 is the load-bearing section for this note.)

Li, Wenxin. "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems." Independent Research, April 2026. Available at Zenodo. (First paper in the CKS theory series; §2.1, §3.3, §5, §6.2, §7.4 are directly inherited.)

---

## Self-citation

This note is B2.80 in the CKS derivation note series. It follows B2.79 (bidirectional evolution integrating frame) and precedes B2.81 (vertical evolution specification). The B1.16 decomposition continues through B2.81, B2.82 (operational timescale treatment), and B2.83 (bidirectional evolution verification).
