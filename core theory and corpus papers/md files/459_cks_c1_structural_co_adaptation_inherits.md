# Structural Co-Adaptation Inherits Paper 1's Tool-Agnosticism and Non-Specialist Governance

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to establish publicly that Paper 2's structural co-adaptation commitment derives from and extends two named Paper 1 commitments — tool-agnosticism (A0.05/Claim 5) and non-specialist governance (A1.11) — so that downstream work can engage with the derivation rather than treating structural co-adaptation as an independent invention.

## Abstract

Paper 2 of the CKS theory series introduces structural co-adaptation: the architectural commitment that the three-level organization (cells, aspects, Self) is designed to evolve as the enterprise's operational needs change. Cells are added and retired as tasks emerge and become obsolete; aspects are reconstituted as coordination domains shift; the Self's integration architecture is updated as enterprise strategy evolves. This note establishes that structural co-adaptation is a joint extension of two Paper 1 commitments, not a novel invention. From tool-agnosticism (Claim 5), Paper 2 inherits host-independence: adding a cell, reassigning it to a different aspect, or restructuring the Self architecture does not require changing the host tool, because the structural configuration is governed content in the substrate, not tool-embedded configuration. From non-specialist governance (A1.11), Paper 2 inherits practitioner accessibility: the people who understand the evolving operational needs — not only the architects who designed the system — can govern structural changes. What is new in Paper 2 is the explicit naming of three co-adaptation types, the commitment that the three-level architecture is designed for structural change over time, and the positioning of operational need (not technical requirement) as the primary driver of structural governance. An operational test closes the inheritance argument: when an enterprise's operational domain expands to require a new cluster of cells and a new aspect, a non-architect operational practitioner using the existing host tool must be able to author the necessary governance events (cell births, aspect birth, membership rules) without technical re-architecture of the deployment. This note also closes Series C — thirty inheritance-edge notes establishing the complete Paper 2 → Paper 1 derivation tree.

## 1. Why this inheritance edge needs to be stated

Paper 2 defends structural co-adaptation as an architectural commitment of the three-level CKS organization. The defense is made at the level of Paper 2's own arguments, which cover cell lifecycle events, directed selection at the DNA layer, and vertical evolution propagating cell and aspect insights to the Self architecture. None of these arguments require Paper 1 as a premise. A reader could therefore conclude — incorrectly — that structural co-adaptation is genuinely novel relative to the CKS prior art, and that an enterprise governance architecture capable of structural self-organization would constitute patentable territory independent of Paper 1.

The inference is wrong for a precise reason: structural co-adaptation requires both that structural changes are tool-independent (so that the organizational structure can change without changing the deployment infrastructure) and that structural changes are accessible to the practitioners who understand operational needs (so that structural governance is practically sustainable). Both of these properties are already committed to in Paper 1. Tool-agnosticism (Claim 5) establishes host-independence as an architectural property of any CKS substrate. Non-specialist governance (A1.11) establishes practitioner accessibility as an architectural property of any CKS governance arrangement. Paper 2's structural co-adaptation is the direct application of these two properties to structural decisions — the same host-independence and the same accessibility, now applied to decisions about which cells exist, how they are organized into aspects, and how the Self's integration architecture is configured.

Naming the inheritance precisely forecloses the adversarial reading. This note provides that naming.

## 2. The two inherited Paper 1 commitments

Structural co-adaptation draws on two Paper 1 commitments jointly. Neither alone is sufficient.

**Tool-agnosticism (Claim 5).** Paper 1 commits that the CKS architecture is host-independent: any environment satisfying three minimal requirements — persistent structured state, direct human read/write access, LLM access to substrate content — can host a CKS substrate, and no environment failing any of those requirements can. The architectural consequence that matters for structural co-adaptation is this: because the three minimal requirements are met by commodity tools, and because those tools satisfy the requirements regardless of what substrate content they carry, adding or removing cells, reassigning cells between aspects, or updating the Self's integration architecture produces no change in the host environment requirements. The host tool does not embed the organizational structure; the organizational structure is substrate content, governed like any other substrate content, migrable between qualifying hosts. Structural changes are host-independent as a direct consequence of the substrate-as-content architecture Paper 1 establishes.

**Non-specialist governance (A1.11).** Paper 1 commits that governance practitioners — the humans who operate the system once deployed — can author and modify orchestration rules and substrate content using commodity tools they already use, without requiring architect-level expertise in AI or in the architecture itself. This accessibility is not a procedural convenience; it is an architectural property produced by the conjunction of tool-agnosticism, the authority-not-labor interpretation of human governance, and linear-cost scaling (Paper 1, §7.4). Together, these ensure that exercising governance rights — to inspect, modify, and override substrate content and orchestration rules — remains accessible to non-specialists regardless of how large the substrate grows. Practitioners closest to operational needs can govern the system, because the architecture does not require specialist tools or specialist knowledge to exercise authority.

The two commitments are jointly necessary for structural co-adaptation. Tool-agnosticism without non-specialist governance would leave structural changes tool-independent but architecturally accessible only to specialists — the same host tool could carry the changes, but only architects could author them. Non-specialist governance without tool-agnosticism would leave structural changes practitioner-accessible in principle but dependent on a specific host tool that would need to change whenever the organizational structure changed. Neither alone delivers structural co-adaptation as an operational reality. Both together do: the organizational structure lives in substrate content on a host-independent surface, and practitioners who understand what the enterprise needs can govern it.

## 3. Paper 2's structural co-adaptation: three types

Paper 2 names three types of structural co-adaptation, each with specific governance mechanisms. These types are what Paper 2 adds to the inherited foundation; they are not in Paper 1.

**Cell additions and retirements.** As new operational tasks emerge, new cells are born: practitioners initiate cell birth events, authoring the DNA layer (orchestration substrates, behavior substrates, schemas, lifecycle policies) that defines how the new cell will function. As tasks become obsolete or are superseded, existing cells are retired: retirement is governed as a lifecycle event (death) with records preserved in the archival substrate for the lineage. The cell count and composition of the organizational structure therefore evolves continuously as the enterprise's operational landscape changes. Paper 1 names substrate origination and retirement as patterns; Paper 2 names them as first-class structural governance events at the three-level architecture.

**Aspect restructuring.** Aspects are coordination arrangements of cells serving a particular operational purpose. As operational domain boundaries shift — because business strategy changes, because two adjacent functions converge, because a domain that was unified needs to be split — aspects can be reconstituted: cells reassigned between existing aspects, aspects dissolved, new aspects created to group cells around an emerging coordination purpose. Each of these events is governed: a membership-rule change, a cell reassignment, or an aspect birth event authored by practitioners who understand the new domain structure. The aspect-level organizational map is substrate content, not tool-embedded configuration.

**Self architecture evolution.** The Self is the integrated whole that holds the multiple coexisting aspects as facets of one CKS-governed intelligence. As enterprise strategy evolves — as new aspects are added, as the integration architecture that ties aspects together becomes outdated — the Self's integration architecture is updated through vertical evolution: cell and aspect insights propagate upward to Self-level orchestration substrates, and the Self's composition rules are refined to reflect the new organizational reality. Vertical evolution is a directed, human-governed process; it propagates what operational practitioners have learned at lower levels into the structural configuration of the highest level.

All three co-adaptation types share the same governance properties as any other CKS governance: they are recorded as substrate events (path retraceability), they occur under human authority (human-governed), they are accessible to practitioners using commodity tools (non-specialist governance), and they do not require changing the host tool (tool-agnosticism).

## 4. What is preserved, what is new

**Preserved from tool-agnosticism.** Every structural co-adaptation event — cell birth, cell retirement, aspect reconstitution, Self architecture evolution — is a change to substrate content. The host tool does not need to be reconfigured when the organizational structure changes, because the organizational structure is not embedded in the host tool. A deployment on a spreadsheet host, a structured document store, or a relational database carries the organizational structure as substrate content that is equivalent across hosts satisfying the three minimal requirements. Migration between qualifying hosts does not change the structural configuration. Paper 2 directly inherits this host-independence and extends it to structural decisions.

**Preserved from non-specialist governance.** Structural governance — deciding that a new operational domain warrants new cells, that two aspects should be merged, that the Self's integration architecture needs updating — does not require architect expertise. The practitioners who understand that the enterprise has moved into a new domain, that a coordination boundary has shifted, or that a prior structural decision no longer fits operational reality are the same practitioners who can author the governance events that implement the change. This is the direct extension of Paper 1's accessibility principle: non-specialists can govern not only the rules that govern how cells operate, but the organizational structure itself.

**New in Paper 2.** Three things are genuinely new. First, the three co-adaptation types are named and given specific governance mechanisms; Paper 1 had modifiable orchestration rules but did not name cell addition, aspect restructuring, and Self architecture evolution as distinct structural governance events. Second, co-adaptation is an explicit architectural commitment of the three-level design: Paper 2's architecture is not designed as an immutable deployment structure that happens to allow changes at the edges; it is designed from the outset to support structural evolution over time. Third, and most forward-looking: Paper 2 positions operational need — not technical requirement — as the primary driver of structural co-adaptation. The person who initiates a cell birth is not the architect who built the system; it is the practitioner who recognized that a new operational task requires a new coordination unit. This completes the non-specialist governance principle from Paper 1: not just governing the rules within a fixed structure, but governing the structure itself, is accessible to the people closest to operational needs.

## 5. Operational test

A system instantiates the structural co-adaptation commitment derived in this note if and only if the following scenario succeeds:

An enterprise's operational domain expands. A new area of work emerges that requires its own cluster of coordination cells and its own aspect grouping them. A practitioner with operational knowledge of the new domain — not an architect, not an AI engineer, not a specialist in the CKS architecture — is the person who recognizes the need and initiates the structural change.

The test passes if and only if all of the following are true:

1. The practitioner can author the cell birth events (DNA layer: orchestration substrates, behavior substrates, schemas, lifecycle policies) for each new cell using the existing host tool, without any change to the host tool's deployment or configuration.
2. The practitioner can author the aspect birth event (membership rules, purpose definition, coordination arrangement) grouping the new cells into a new aspect, using the existing host tool, again without deployment changes.
3. The practitioner can update the Self's integration architecture to incorporate the new aspect, through the Self's orchestration substrates, using the same host tool and the same commodity affordances.
4. All three governance events are recorded as substrate content with path retraceability (originator, timestamp, rationale linkage) without requiring specialized tooling beyond what the host environment provides.
5. No step in (1)–(4) requires architect-level expertise in AI, in software engineering, or in the CKS architecture's internal design to perform.

A system that fails any of (1)–(5) may support structural changes of some kind, but does not instantiate the structural co-adaptation commitment as derived in this note from Paper 1's tool-agnosticism and non-specialist governance. Specifically: a system in which adding a new aspect requires reconfiguring the host tool fails (1)–(3); a system in which structural changes are only authorable by designated architects fails (5); a system in which structural events are not recorded as substrate content fails (4).

## 6. Series C closure

This note is the thirtieth and final note of Series C of the CKS derivation-note publication series. Series C establishes the complete Paper 2 → Paper 1 inheritance tree: thirty notes, each formalizing one inheritance edge from a Paper 2 architectural commitment back to one or more named Paper 1 commitments. Together, they place on public record that Paper 2's entire architectural vocabulary derives from Paper 1, extends it, and does not constitute independent prior art relative to it.

The thirty notes are organized across six coverage clusters:

**Core architecture (C1.01–C1.05).** These five notes establish the foundational identity claims: Paper 2's instinct/reasoning separation inherits Paper 1's substrate/LLM hybrid at cell scope (C1.01); the reasoning layer preserves Paper 1's substrate identity (C1.02); the instinct layer preserves Paper 1's LLM identity (C1.03); Paper 2's governance boundary inherits Paper 1's governance boundary at cell scope (C1.04); and Paper 2's cell is identical to Paper 1's cell as foundational unit (C1.05). These five notes ensure that Paper 2 cannot be read as establishing a new architectural vocabulary for the entities Paper 1 already named.

**Recursive applicability (C1.06–C1.07).** Two notes establish that the three-level architecture does not introduce new commitments at the aspect and Self levels; it applies Paper 1's full commitment set recursively. Aspect-level commitments (C1.06) and Self-level commitments (C1.07) are both direct instances of Paper 1's architectural properties at extended scope.

**Internal structure (C1.08–C1.10).** Three notes cover Paper 2's within-cell architecture. The DNA layer (C1.08) inherits Paper 1's orchestration rules and behavior substrates; the action layer (C1.09) inherits Paper 1's substrate content for recorded task instances; expression (C1.10) inherits Paper 1's substrate-selection-by-orchestration-rules mechanism.

**Lifecycle (C1.11–C1.16).** Six notes cover the cell lifecycle. Birth (C1.11) inherits Paper 1's substrate origination patterns. The three mating patterns — mating-union (C1.12), selective-merge (C1.13), and lineage-preserved-union (C1.14) — inherit Paper 1's conflict preservation, human-governed write authority, and path retraceability respectively. Death (C1.15) inherits Paper 1's substrate retirement under governance. Archival of dead cells (C1.16) inherits Paper 1's substrate-as-source-of-truth property, establishing that retired cells remain addressable.

**Evolution (C1.17–C1.23).** Seven notes cover the three evolution mechanisms and their governance shapes. Instinct evolution (C1.17) inherits Paper 1's tool-agnosticism, since LLM and infrastructure upgrades operate at the host layer. DNA evolution (C1.18) inherits Paper 1's human-governed commitment, since rule changes operate under governance authority. Action-feedback evolution (C1.19) inherits Paper 1's substrate-as-source-of-truth, since the feedback loop closes through authoritative substrate content. Multi-level evolution (C1.20) inherits Paper 1's linear-cost property, preserving cost properties at Self scope. Horizontal evolution (C1.21) inherits Paper 1's substrate content evolution. Vertical evolution (C1.22) inherits Paper 1's orchestration-rule evolution. Multi-shaped governance (C1.23) inherits Paper 1's authority-not-labor architecture, extended to cover distinct authority shapes across the three evolution mechanisms.

**Verification (C1.24).** One note establishes that Paper 2's verification substrates inherit Paper 1's conflict preservation, with parallel-run verification functioning as a form of conflict detection at the instinct/reasoning boundary.

**Boundaries and scale (C1.25–C1.30).** Six notes cover Paper 2's extension claims and boundary commitments. The instinct/reasoning boundary (C1.25) inherits Paper 1's governance boundary at cell scope. The enterprise brain (C1.26) inherits Paper 1's cell concept as its direct extension claim. Substrate-shared topology (C1.27) inherits Paper 1's substrate as primary artifact. Linear-cost at Self scope (C1.28) inherits Paper 1's Claim 5 cost contract. Distributed failure risk (C1.29) inherits Paper 1's substrate-cell boundary, with the cell-boundary commitment producing failure localization as an architectural property. And this note, structural co-adaptation (C1.30), inherits Paper 1's tool-agnosticism and non-specialist governance jointly.

Series C does not exhaust what could be said about the Paper 2 → Paper 1 relationship. Series B covers Paper 2's own architectural commitments in depth, and Series B4 covers composition pairs between Paper 2 and Paper 1 concepts at greater granularity than Series C's inheritance-edge register. What Series C establishes, at the level it is written to establish, is the complete derivation tree: no Paper 2 commitment is without Paper 1 ancestry, and that ancestry is now on public record.

## 7. Prior-art significance

This note forecloses three adversarial claim patterns.

First: that structurally adaptable AI governance architectures — systems where the organizational structure of cells and aspects evolves as operational needs change — are novel relative to Paper 1's tool-agnosticism and non-specialist governance. They are not. The properties that make structural co-adaptation architecturally possible (host-independence of substrate content, practitioner accessibility of governance authority) are both present in Paper 1. Paper 2's three named co-adaptation types are applications of those properties to structural decisions.

Second: that non-architect operational practitioners governing structural changes — authoring cell births, aspect restructuring events, Self architecture updates — is a novel governance capability relative to Paper 1. It is not. Paper 1's non-specialist governance principle commits that governance is accessible to practitioners who can read and write substrate content in commodity tools. Paper 2 applies this principle to structural governance events, which are substrate content like any other. The accessibility does not change in kind when applied to structural decisions.

Third: that enterprise AI governance capable of adapting its organizational structure over time requires commitments beyond Paper 1's scope. It does not. All structural co-adaptation events — cell birth, aspect birth, Self architecture evolution — are instances of Paper 1's governed substrate modification: substrate content is created, modified, or retired under human authority, using commodity tools, with path retraceability. The three-level architecture adds composition scope; it does not add governance commitments that Paper 1 did not already contain.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Multi-Level CKS Composition with DNA/Action Layers, Three Evolution Mechanisms, and Self-Level Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Structural Co-Adaptation Inherits Paper 1's Tool-Agnosticism and Non-Specialist Governance.* May 14, 2026. ORCID: 0009-0004-8065-3235.
