# Aspect as Exchange Unit in Full Aspect Integration

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI) is the canonical operation over the shared substrate that Paper 3 establishes for inter-Self coordination. This note formalizes one foundational sub-commitment of FAI: the aspect is the unit of exchange. When a Self participates in an FAI event, it contributes aspects — not individual cells, not the Self as a whole, not raw content extracted from cells and stripped of its governance structure. The aspect carries the governance context — purpose statement, coordination rules, content-domain specification, and membership structure — that makes the contributing cells' content interpretable by the receiving Self's governance. This note states the sub-commitment precisely, explains why the aspect is the correct granularity of exchange, explains why finer and coarser alternatives fail, and establishes selective contribution as the governance property that permits organizations with proprietary governance structures to participate in inter-Self coordination without exposing their full architecture. D1.06 opens the Claim 2 sub-commitment set (D1.06–D1.12); subsequent notes in this set cover n-ary cardinality, full-merge as architectural default, three pattern variants, exchange bounding to substrate content, three persistence loci, and FAI as the inter-Self analog of Paper 2's intra-Self combination primitive.

---

## 1. Position of this sub-commitment

Paper 3's Claim 2 establishes Full Aspect Integration as the canonical operation over the shared substrate. Claim 2 carries seven architectural sub-commitments: the exchange unit (D1.06, this note), cardinality (D1.07), the full-merge default (D1.08), the three pattern variants (D1.09), exchange bounding to substrate content (D1.10), the three persistence loci at FAI dissolution (D1.11), and FAI's status as the inter-Self analog of Paper 2's intra-Self combination primitive (D1.12). Each sub-commitment is independently formalizable and independently defensible; each inherits from Claim 2 as a whole and contributes a distinct piece of the Claim 2 architecture.

D1.06 is the gateway sub-commitment. The other six sub-commitments presuppose a settled answer to the exchange-unit question: what object crosses the inter-Self boundary during an FAI event? Until that question is answered at architectural level, the semantics of cardinality, merge default, pattern variants, bounding, and persistence are underspecified. D1.06 answers it: the aspect crosses the boundary.

The sub-commitment inherits its ancestry from Paper 3, §5 (Claim 2) and from Paper 2's aspect-as-coordination-unit (T1.03 in the trilogy ambiguity map). It does not introduce a new architectural object. It formalizes the role the Paper 2 aspect acquires when it operates at the inter-Self boundary.

---

## 2. The sub-commitment stated

**D1.06:** When a Self participates in an FAI event, the unit at which it contributes content to the shared substrate is the aspect. The contributing Self contributes one or more aspects from its governance architecture; each contributed aspect surfaces its constituent cells' DNA-layer and action-layer content within the shared substrate under the aspect's coordination structure. No finer-grained unit (the individual cell) and no coarser-grained unit (the Self as a whole) constitutes the exchange unit. The aspect is the minimum unit of meaningful inter-Self exchange because it carries the governance context that makes the cells' content interpretable and composable by the receiving Self's governance.

The sub-commitment has two parts that are equally necessary:

**Part A — Aspect granularity:** The object that crosses the inter-Self boundary is the aspect, not a fragment of the aspect and not an aggregation of aspects equivalent to the Self.

**Part B — Governance context travels with the object:** When an aspect crosses the boundary, it carries its coordination structure — purpose statement, coordination rules, content-domain specification, and membership structure — into the shared substrate. The cells' content does not travel naked; it travels inside the aspect that governs it.

These two parts are not separable. An architectural design that uses aspect-granular exchange units but strips the governance structure at the boundary satisfies Part A while violating Part B, and the sub-commitment requires both.

---

## 3. What the aspect carries: the four governance context components

The aspect is the Paper 2 coordination layer that groups cells by content-domain and integrates them under a unified governance structure within a Self. When an aspect crosses the inter-Self boundary during FAI, it carries four components that together constitute the governance context:

**Purpose statement.** The aspect's purpose statement names what the aspect coordinates for — the content-domain problem it addresses within the contributing Self's architecture. Without this, the receiving Self's governance cannot determine what function the contributed content serves or whether that function is relevant to the coordination task at hand.

**Coordination rules.** The aspect's coordination rules specify how its member cells' outputs are integrated — what aggregation logic, sequencing constraints, or conflict-handling procedures apply within this aspect. Without coordination rules, the receiving Self encounters a set of cell outputs with no specification of how they compose. Composability at the inter-Self level requires that the receiving governance understand the integration logic the contributing governance applied.

**Content-domain specification with boundary rules.** The content-domain specification names the aspect's scope — what subject matter the aspect addresses and what its boundaries are. Boundary rules specify what falls inside and outside the domain. Without domain specification, the receiving Self cannot locate the contributed content within its own governance architecture or determine which of its own aspects should compose with the contribution.

**Membership structure.** The membership structure records which cells belong to the aspect. When the aspect surfaces its constituent cells' DNA-layer and action-layer content, the membership structure is what authorizes that surfacing — it specifies which cells' content is governed by this aspect and therefore which cells' content the aspect may represent in the shared substrate.

Together these four components constitute the governance context that makes the cells' content meaningful to an external governance architecture. The aspect is the minimum unit that carries all four. An individual cell carries none of them in the form that an external governance can use without the aspect's framing.

---

## 4. Why not cells: the governance-opacity problem

The alternative of contributing individual cells — directly, without their parent aspect — fails because it produces governance-opaque exchange.

When a cell is contributed without its parent aspect, the receiving Self's governance encounters a unit of content with no purpose statement (it cannot determine what the cell addresses), no coordination rules (it cannot determine how the cell's output composes with other cells), no content-domain specification (it cannot locate the cell within its own governance architecture), and no membership context (it cannot determine which governance structure is responsible for the cell's behavior).

The receiving Self can observe the cell's DNA-layer content — its orchestration substrate and behavior substrate — and its action-layer content — its recorded task outputs and lived experience. But it cannot interpret what this content is for within the contributing Self's architecture, and it cannot determine how to integrate the content with its own cells without improvising a governance structure that was never specified by the contributing Self.

This is not merely an inconvenience. Cell-level exchange would require the receiving Self to construct governance context from scratch for every received cell, which is neither scalable nor safe. It is not scalable because the governance-construction cost grows with the number of cells contributed and would negate the efficiency case for inter-Self coordination. It is not safe because governance constructed by inference rather than by explicit contribution would represent the contributing Self's architecture inaccurately — the receiving Self would be making governance decisions based on an interpretation of the contribution, not based on the contribution's actual governance structure.

The aspect-as-exchange-unit sub-commitment forecloses this failure mode by requiring that the governance context travel with the content.

---

## 5. Why not the Self: the over-exposure problem

The alternative of contributing the Self as a whole — exposing the full governance architecture of the contributing Self to the shared substrate — fails for a different and equally serious reason: it over-exposes the contributing Self's proprietary governance structures.

A Self contains aspects the contributing organization may not wish to share: aspects governing proprietary operational patterns, aspects whose content-domain is sensitive, aspects whose coordination rules represent competitive intelligence, aspects that are irrelevant to the specific coordination task at hand. It also contains DNA content that may be confidential — organizational governance rules, operational policies, instinct-layer configurations — and action-layer records that cover the full operational history of the contributing Self, not only the history relevant to the current FAI event.

Contributing the full Self to a shared substrate exposes all of this. The contributing organization loses the ability to govern what it shares and retains the exposure risk of full disclosure even for an FAI event whose scope is narrow and whose coordination task requires access to only a small subset of the contributing Self's content.

The aspect-as-exchange-unit sub-commitment preserves the contributing Self's governance authority over its own architecture by making the exchange unit smaller than the Self. Contributing an aspect is a governed act of selective disclosure: the contributing Self's governance determines which aspects to contribute and which to retain. The full Self is never at risk of involuntary disclosure through the act of participating in FAI.

---

## 6. Selective contribution as a governance property

The preceding sections establish why the aspect is the correct granularity — it carries sufficient governance context (more than a cell, less exposure than the full Self). This section establishes the consequence: selective contribution is a governance property of FAI participation, not an implementation detail.

The contributing Self's governance decides, per FAI event, which aspects to contribute to the shared substrate. This decision is governed by the sharing-scope configuration (Paper 3 Claim 5; D1.22–D1.25 in the derivation note series), which is itself substrate content subject to the contributing Self's governance authority. The governance property has three components:

**Per-event selection.** The aspects contributed in one FAI event need not be the same aspects contributed in another FAI event between the same Selves. The contributing Self's governance may determine, based on the coordination task at hand, that different aspects are appropriate for different events. The sub-commitment does not require a fixed mapping from FAI participation to aspect contribution; it requires that whatever aspects are contributed are contributed at aspect granularity.

**Partial contribution as the norm.** The architecture does not presuppose or require that all aspects be contributed. Partial contribution — some aspects contributed, others retained within the contributing Self's home perimeter — is the expected case for organizations with governance structures that include proprietary, sensitive, or irrelevant content-domains. The sub-commitment is compatible with any non-empty selection of aspects.

**Non-contributed aspects remain home.** Aspects that the contributing Self's governance does not select for contribution to a given FAI event remain exclusively within the contributing Self's home perimeter. They are not visible to, accessible by, or composable with the receiving Self's governance unless and until the contributing Self's governance elects to contribute them in a subsequent event. The inter-Self perimeter is not a transparency boundary; it is a governed exchange boundary.

This governance property is what makes FAI safe for multi-organizational coordination. Organizations with proprietary governance structures, confidential operational histories, or governance architectures they are not prepared to expose fully can participate in inter-Self coordination by contributing the aspects whose content-domains are appropriate to the task, without surrendering the governance architecture as a whole.

---

## 7. Inheritance from Paper 2

The aspect-as-exchange-unit sub-commitment does not introduce a new architectural object. The aspect in FAI is the Paper 2 aspect fulfilling an additional role at the inter-Self boundary. This inheritance is explicit and precise.

Paper 2 establishes the aspect as the coordination layer within a Self that groups cells by content-domain. The aspect carries a purpose statement, coordination rules, content-domain specification, and membership structure. The aspect is a governance structure within a Self — it is how the Self organizes the coordination work its cells perform.

Paper 3's FAI adds an exchange role to the Paper 2 aspect: the same architectural object that coordinates cells within a Self also serves as the unit at which inter-Self content exchange occurs. The aspect's internal definition is unchanged. Its purpose statement still names what it coordinates for; its coordination rules still govern how its member cells' outputs integrate; its content-domain specification still bounds its scope; its membership structure still names which cells belong to it. FAI adds no new components to the aspect's definition. It adds a role: the aspect can be contributed to a shared substrate.

The trilogy ambiguity map (T1.03) formalizes this inheritance relationship precisely: "The aspect is the same architectural object — a governed coordination unit grouping cells — that serves as both the internal coordination structure within a Self (P2) and the unit at which inter-Self content exchange occurs (P3). The aspect's role expands at the inter-Self scope; its definition does not change."

The inheritance matters for the defensive publication record. An adversary claiming that Paper 3's "aspect as exchange unit" is a novel concept unrelated to Paper 2's "aspect as coordination unit" would be wrong. The exchange role is a fresh-at-Paper-3 architectural commitment; the object fulfilling that role is the Paper 2 aspect. What is fresh at Claim 2 is the commitment that the aspect serves as the inter-Self exchange unit specifically — Paper 2 does not name this role. What is not fresh is the aspect itself, which is fully established by Paper 2.

---

## 8. Four failure modes defended against

D1.06 defends against four specific failure modes that an incomplete or alternative implementation of FAI might instantiate:

**Failure mode 1 — Cell-level exchange.** An implementation that uses individual cells as the exchange unit, without their parent aspects, performs governance-opaque exchange. The receiving Self cannot interpret the contributed content without constructing governance context it was not given. This failure mode produces inter-Self coordination that is formally structured but governancely incomplete: cells are shared, but the coordination structure that makes them meaningful is not.

**Failure mode 2 — Full-Self exchange.** An implementation that requires contributing Selves to expose their full architecture in order to participate in FAI imposes an over-exposure requirement that most organizations with proprietary governance structures cannot accept. This failure mode conflates participation with full disclosure and undermines the governance safety property that makes inter-Self coordination viable.

**Failure mode 3 — Raw content exchange.** An implementation that extracts DNA-layer or action-layer content from cells and transmits it to the shared substrate without the aspect governance structure — stripping purpose statement, coordination rules, and content-domain specification before transmission — produces content that is present in the shared substrate but ungoverned within it. The receiving Self cannot locate this content within its governance architecture or determine how it composes with its own governed content.

**Failure mode 4 — Mandatory full-aspect-set contribution.** An implementation that requires contributing Selves to contribute all of their aspects to a shared substrate eliminates selective contribution as a governance property. This failure mode renders FAI incompatible with organizations that have proprietary or sensitive content-domains in their governance architecture. It is the full-Self problem at aspect scope: every aspect is contributed by requirement, not by governance decision.

---

## 9. Operational test

D1.06 is instantiated if and only if, for a given FAI event, all of the following are true:

1. **Aspect granularity:** Each contribution the contributing Self makes to the shared substrate during the FAI event is an aspect — not an individual cell without its parent aspect, and not the contributing Self's full governance architecture.

2. **Governance context present:** Each contributed aspect carries its purpose statement, coordination rules, content-domain specification, and membership structure into the shared substrate. An observer can inspect the shared substrate and find, for each contributed aspect, these four components alongside the aspect's cells' DNA-layer and action-layer content.

3. **Non-contributed aspects retained:** Aspects that the contributing Self's governance did not select for this FAI event are not accessible from the shared substrate. An observer with access to the shared substrate cannot retrieve governance content from aspects the contributing Self chose not to contribute. The contributing Self's home perimeter remains the exclusive location of non-contributed aspects during and after the event.

4. **Contribution governed by Self:** The selection of which aspects to contribute was made by the contributing Self's governance — it was not automatic, not externally mandated, and not determined by the shared substrate or the receiving Self. The contributing Self's governance holds authority over its own contribution scope.

A system that satisfies (1) through (4) for every FAI event it executes instantiates D1.06. A system that fails any of (1) through (4) may perform inter-Self coordination in some sense, but does not instantiate the aspect-as-exchange-unit sub-commitment.

---

## 10. Position in the Claim 2 sub-commitment set

D1.06 is the first of seven D1-phase sub-commitments derived from Paper 3's Claim 2. It establishes the exchange unit, which is the presupposition the remaining six sub-commitments build on.

The six sub-commitments that follow address related but distinct architectural questions. D1.07 addresses n-ary cardinality: how many Selves can participate in a single FAI event, and what the cardinality floor of two reflects about FAI's inter-Self scope. D1.08 addresses the full-merge default: why FAI's architectural default is full merge of contributed aspects, and why this is fresh at inter-Self scope relative to Paper 2's neutral treatment of its three pattern variants. D1.09 addresses the three pattern variants — union, selective merge, lineage-preserved union — as Paper 2 inheritance carrying across the inter-Self perimeter. D1.10 addresses exchange bounding: why the exchange is bounded to substrate content per Paper 2's instinct/reasoning separation, and what this means at the FAI mechanism level. D1.11 addresses the three persistence loci at FAI dissolution: where contributed aspects, merged substrate content, and conflict records reside after the shared substrate dissolves. D1.12 addresses FAI as the inter-Self analog of Paper 2's intra-Self combination primitive: the structural correspondence between the two primitives and the inheritance relationship that makes FAI recognizable as an extension rather than a departure.

D1.06 through D1.12 together constitute the full foundational sub-commitment decomposition of Claim 2.

---

## 11. Conclusion

The aspect-as-exchange-unit sub-commitment (D1.06) formalizes one of the seven foundational architectural commitments Paper 3's Claim 2 makes about Full Aspect Integration. The aspect is the unit of exchange because it carries the governance context — purpose statement, coordination rules, content-domain specification, and membership structure — that makes the contributing cells' content interpretable by the receiving Self's governance. Contributing individual cells without their parent aspect strips this context and produces governance-opaque exchange. Contributing the full Self exposes governance architecture beyond what the coordination task requires and beyond what most organizations with proprietary structures can accept.

The aspect as exchange unit enables selective contribution: the contributing Self governs which aspects to contribute per FAI event, retaining all non-contributed aspects exclusively within its home perimeter. This governance property is what makes inter-Self coordination compatible with organizational privacy, proprietary governance structures, and the principle that participation in coordination does not require full disclosure.

The aspect that serves as exchange unit in FAI is the Paper 2 aspect. Its definition is unchanged; its role is extended. What is fresh at Paper 3 is the commitment that the aspect is the inter-Self exchange unit specifically. The governance object itself, and the four components of governance context it carries, are Paper 2 architecture applied at the inter-Self scope.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Aspect as Exchange Unit in Full Aspect Integration.* May 14, 2026. ORCID: 0009-0004-8065-3235.
