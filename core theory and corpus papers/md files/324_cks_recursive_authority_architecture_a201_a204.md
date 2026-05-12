# Recursive Authority Architecture (A2.01–A2.04): How the Four Governance Affordances Apply at Cell, Aspect, and Self Scope, Enabling Entity-Level Governance at Every Structural Granularity

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

It does not introduce new axioms. Its contribution is to formalize, as a standalone derivation, the recursive application of the four Paper 1 governance affordances (A2.01 inspect, A2.02 modify, A2.03 override, A2.04 rule authoring) across the three structural levels that Paper 2 defines: cell, aspect, and Self. This is the tenth note in the B1.20 recursive Paper 1 commitments decomposition series, following B2.98–B2.106.

## Abstract

Paper 1 established four governance affordances — the rights to inspect, modify, override, and author orchestration rules — as properties of the human-governed architectural commitment (A1.01). Paper 2 extends the CKS architecture to three structural levels (cell, aspect, Self) and specifies, through its recursive Paper 1 commitments treatment, that all four affordances apply at every level. This note formalizes that recursive application as a standalone architectural commitment: the recursive authority architecture (A2.01–A2.04). The note states what is constant across levels (the four affordances are present at each), what differs (what the affordances operate on at each level), how authority is distributed (A2.47 specifies who holds which affordances at which level), and what affordance independence means (exercising an affordance at one level does not automatically trigger affordances at other levels). The note contrasts recursive authority architecture with deployment-level-only affordance models, articulates the biological analog of multi-level regulatory mechanisms, names the inherited Paper 1 commitments, derives the operational implications, and states the architectural limits. The central result is that any entity in a CKS deployment — every cell, every aspect, the Self — can be independently inspected, modified through directed selection, overridden on specific decisions, and governed through rule authoring at its own scope, enabling surgical governance at the precise structural granularity where improvement is needed.

## 1. Why recursive authority architecture needs to be formalized as a standalone derivation

Paper 1 establishes human governance as an authority architecture: the rights to inspect, modify, and override substrate content and orchestration rules, plus the authoring of orchestration rules that govern cell-level behavior (A1.01, A2.01–A2.04). These four governance affordances are defined at the cell level, which is the architectural scope Paper 1 defends. Paper 2 extends the architecture to three composition levels — cell, aspect, Self — and commits, through B1.20's recursive Paper 1 commitments treatment, that all four affordances apply at each level. This recursive application is architecturally substantive: it is not a trivial restatement that "governance applies everywhere" but a precise specification of what each affordance operates on at each level, who holds each affordance at each level (A2.47 authority distribution), and how affordance exercise at one level relates to affordance exercise at other levels (affordance independence as the architectural default).

The recursive authority architecture merits standalone formalization for three reasons. First, prior-art territory: the combination of four specific affordances applied independently at three specific structural levels, with level-appropriate subject matter and explicit authority distribution, is a patentable architectural derivation that requires its own public record. Second, derivation precision: naming the recursive application at each level makes explicit what the source paper specifies but does not enumerate in tabular form, and this precision is what downstream notes (B2.108 recursive conflict-first-class, B2.109 recursive operational tests, B2.110 recursive commitments verification) depend on. Third, architectural distinctiveness: conventional AI governance architectures typically afford inspection, modification, override, and rule authoring only at deployment scope — the whole system — rather than at cell, aspect, and Self scope independently. Formalizing the recursive application makes this distinction explicit.

This note is the tenth of thirteen notes decomposing B1.20. B2.98–B2.106 have formalized recursive inspect (A2.01), recursive lineage per B2.43, recursive directed selection per B1.14, recursive level determination per B2.85, and recursive composition requirements (A1.13). B2.107 (this note) formalizes the recursive authority architecture across all four affordances at each level. B2.108 formalizes recursive conflict-as-first-class (A1.03). B2.109 and B2.110 close the decomposition with recursive operational tests and recursive commitments verification.

## 2. The recursive application precisely stated

### 2.1 What is constant across levels

At every composition level — cell, aspect, Self — the same four governance affordances are present:

- **A2.01 (inspect):** humans can read the substrate content at that level.
- **A2.02 (modify):** humans can modify the substrate content at that level, specifically through directed selection per B1.14 for DNA-layer content.
- **A2.03 (override):** humans can override specific operational decisions at that level without modifying the standing rules that produced those decisions.
- **A2.04 (rule authoring):** humans author the orchestration rules governing behavior at that level.

The full governance architecture is present at each scope. No level is missing any affordance. This is the recursive authority architecture: the same authority structure that Paper 1 establishes at cell scope applies, by Paper 2's commitment, at aspect scope and Self scope as well.

### 2.2 What differs across levels: level-appropriate subject matter

The affordances are constant; what they operate on differs per level.

**A2.01–A2.04 at cell scope.** The cell is the atomic unit Paper 1 defends, and the affordances operate on cell substrate content:

- *A2.01 (inspect at cell scope):* humans can inspect cell substrate content — cell DNA per B2.25, which carries the orchestration rules and behavior substrates governing this cell's operation; cell action layer per B2.26, which records what this cell has done; cell level determination records per B2.85; cell lineage per B2.43.
- *A2.02 (modify at cell scope):* humans can modify cell DNA per B2.25 through directed selection per B1.14. Cell DNA modification is the cell-level A2.02 operation; it changes the standing rules and behavior substrates that govern subsequent cell executions.
- *A2.03 (override at cell scope):* humans can override specific cell operational decisions without modifying cell DNA. A cell-level override addresses a particular decision produced during a particular execution. It does not change the rules that would produce similar decisions in the future; that would be A2.02 (cell DNA modification). Override and modify are architecturally distinct operations at cell scope.
- *A2.04 (rule authoring at cell scope):* humans author cell DNA rules. Cell DNA authoring is the primary cell-level governance mechanism, as B2.21 specifies for the DNA layer.

**A2.01–A2.04 at aspect scope.** An aspect is a coordination arrangement of cells serving a particular purpose, operating over its constituent cells as content domain. The affordances operate on aspect substrate content:

- *A2.01 (inspect at aspect scope):* humans can inspect aspect substrate — aspect coordination DNA per B2.16, which carries the orchestration rules governing how cells coordinate within this aspect; aspect membership per B2.08, which records which cells participate in this aspect arrangement; aspect purpose statement per B2.15; aspect lineage per B2.43.
- *A2.02 (modify at aspect scope):* humans can modify aspect coordination DNA through directed selection per B1.14. Aspect DNA modification changes the rules governing how constituent cells coordinate without modifying individual cell DNA at cell scope.
- *A2.03 (override at aspect scope):* humans can override specific aspect coordination decisions — particular coordination outputs produced during a particular aspect execution — without modifying aspect coordination DNA.
- *A2.04 (rule authoring at aspect scope):* humans author aspect coordination rules. These rules govern how cells are arranged, how their outputs are synthesized, and how coordination conflicts are handled at aspect scope.

**A2.01–A2.04 at Self scope.** The Self is the integrated whole holding multiple aspects under unified human governance. The affordances operate on Self substrate content:

- *A2.01 (inspect at Self scope):* humans can inspect Self substrate — Self integration DNA per B2.21, which carries the integration rules governing how aspects are held together; Self instinct/reasoning configuration per B2.23, which specifies how the instinct layer and reasoning layer divide responsibilities at Self scope; the full collection of aspects the Self holds; Self lineage per B2.43.
- *A2.02 (modify at Self scope):* humans can modify Self integration DNA through directed selection per B1.14. Self DNA modification changes the integration architecture — how aspects are coordinated into a unified whole — without modifying individual aspect DNA at aspect scope.
- *A2.03 (override at Self scope):* humans can override specific Self integration decisions without modifying Self integration DNA.
- *A2.04 (rule authoring at Self scope):* humans author Self integration rules per B2.21 and instinct/reasoning configuration per B2.23. Self-level rule authoring is the governance mechanism for the architecture of the Self as integrated whole.

### 2.3 Authority distribution per A2.47

The recursive authority architecture specifies that all four affordances are present at each level. It does not specify that the same human holds all four affordances at all levels. Authority distribution — who holds A2.01–A2.04 at which level — is specified by A2.47 (authority distribution), which is a deployment configuration commitment.

Several distribution patterns follow from the architecture:

- A2.01 (inspect) may be broadly distributed: understanding what a particular cell does, what rules govern it, and what it has produced may be appropriate for a wide range of human roles.
- A2.04 at Self scope (Self DNA authoring) may be restricted to deployment architects: the rules governing how a Self integrates its aspects define the whole entity's architecture, and authority over that may be confined to a small set of principals.
- A2.02 at cell scope (cell DNA modification through directed selection) may be distributed to cell operators: the humans responsible for a particular cell's performance are the natural holders of modification authority at cell scope.
- A2.03 (override) may carry specific authority requirements at each level: override authority may be held by different roles at cell, aspect, and Self scope depending on what decisions are being overridden and what organizational accountability attaches.

A2.47 does not prescribe a universal distribution; it specifies the commitment that distribution is explicit, substrate-recorded, and governed. What A2.47 rules out is undistributed or implicit authority — a deployment in which it is unclear who holds A2.02 at aspect scope, or in which A2.03 at Self scope is exercisable by any actor without architectural specification, is not consistent with the recursive authority architecture as Paper 2 specifies it.

### 2.4 Affordance independence

Affordance exercise at one level does not automatically trigger affordances at other levels. This is the affordance independence property, and it is the architectural default.

Exercising A2.03 (override) at cell scope — addressing a specific decision produced by a specific cell — does not modify cell DNA (that would be A2.02 at cell scope) and does not trigger A2.03 at aspect scope (which would address an aspect coordination decision). The levels are independent governance domains; a human acting on cell substrate is not automatically acting on aspect substrate.

Similarly, exercising A2.02 (modify) at aspect scope — changing how cells coordinate within an aspect — does not modify the DNA of the constituent cells at cell scope. The aspect coordination rules change; the individual cell rules do not, unless A2.02 at cell scope is separately exercised.

Independence is the architectural default. Cross-level effects can occur through vertical evolution per B1.16 — which is the governed pathway for propagating changes across levels — but that pathway requires its own governed decision. It does not flow automatically from affordance exercise at any level.

## 3. What makes recursive authority architecture architecturally distinctive

Conventional AI governance architectures typically support governance affordances at deployment scope: the deployment as a whole can be inspected, modified, overridden, and governed through configuration rules. This is deployment-level-only affordance architecture. What it lacks is entity-level governance affordances at each composition level.

The architectural consequence of deployment-level-only governance is that governance is undifferentiated across scale: inspecting a deployment means inspecting everything; modifying a deployment means modifying a deployment-level artifact; overriding a deployment means overriding a deployment-level decision. Surgical governance — addressing a specific cell, a specific aspect coordination arrangement, or the Self integration architecture — is not supported as a first-class architectural operation. It requires decomposing the deployment artifact manually each time.

Recursive authority architecture creates entity-level governance affordances at cell, aspect, and Self granularity. Any entity in a CKS deployment can be:

- Independently inspected: a human can read cell DNA for one specific cell without requiring access to Self-level substrate.
- Modified through directed selection: cell DNA modification addresses one cell's behavior without affecting other cells or changing aspect coordination rules.
- Overridden on specific decisions: a cell-level override is targeted at a specific execution decision, not at the cell's standing architecture.
- Governed through rule authoring: authoring rules for one aspect's coordination does not require authoring rules for the whole Self.

This surgical governance property is what the recursive authority architecture enables. The governance action can be targeted at exactly the structural level where improvement is needed — no broader, no narrower.

The recursive authority architecture also enables level-appropriate governance review. A governance review of a specific cell's behavior can be conducted by humans holding A2.01–A2.03 at cell scope, without those humans requiring Self-level access (which A2.47 may restrict). An architectural review of Self integration can be conducted by principals holding A2.04 at Self scope, without those principals needing cell-level modification authority. Scope separation is an architectural property, not an organizational workaround.

## 4. The biological analog as conceptual scaffold

Biological regulatory systems exhibit multi-level regulatory mechanisms in which the same type of regulatory operation applies at different structural scales, operating on level-appropriate biological substrate:

- At the molecular level, gene expression regulation modifies which genes are active under which conditions — analogous to cell-level A2.04 (rule authoring on cell DNA) and A2.02 (modification of cell DNA through directed selection).
- At the epigenetic level, modifications to chromatin structure and methylation patterns alter gene expression without changing the underlying DNA sequence — analogous to cell-level A2.03 (override of a specific operational output without modifying cell DNA).
- At the cellular level, signaling pathways produce override-equivalent responses — temporary modifications to cellular behavior in response to external signals, without permanent genetic change.
- At the organism level, regulatory mechanisms govern how cell populations and tissue arrangements coordinate — analogous to Self-level and aspect-level governance affordances operating on integration substrate.

The biological system does not have explicit human-authored rules governing each level, explicit authority distribution across human actors, or the affordance independence property. These are specifically architectural commitments that CKS adds. The biological analog provides the conceptual framing — the same governance operation types apply at multiple structural levels, operating on level-appropriate substrate — and the architectural substance is the explicit human affordances at each level scope.

Paper 2's biology engagement is bounded per §2.2 of the source paper: biology supplies load-bearing terminology for the structural concepts, not a comprehensive architectural theory. The recursive authority architecture is an architectural commitment derived from Paper 2's governance extension; the biological analog is the conceptual scaffold, not the derivation base.

## 5. Inherited Paper 1 commitments

The recursive authority architecture inherits the following Paper 1 commitments directly:

**A2.01–A2.04 (the four governance affordances).** These are the commitments being formalized recursively. Paper 1 establishes them at cell scope; Paper 2 through B1.20 extends them to aspect and Self scope. The recursive authority architecture is the per-level formalization of this extension.

**A1.01 (human governance as authority, not labor).** The recursive authority architecture is an extension of the human-governed architectural commitment. At each level — cell, aspect, Self — governance is an authority architecture: humans hold the rights to inspect, modify, override, and author rules. That the same authority structure applies at three levels rather than one does not change what human governance means; the definition from A1.01 holds at each level without modification.

**A2.40 (provenance: six metadata requirements per piece of substrate content).** Affordance exercise events at each level produce substrate events — a cell DNA modification through A2.02, an aspect-level override through A2.03, a Self-level rule authoring act through A2.04. Each such event is substrate content subject to A2.40's provenance requirements. The affordances are rights; exercising them produces recorded events; those events carry full provenance metadata. This is what makes affordance exercise at each level inspectable, attributable, and retraceably linked to the governance action that produced it.

**A2.47 (authority distribution).** Who holds A2.01–A2.04 at each level is specified by A2.47. The authority distribution is substrate content, not external policy; it is inspectable, modifiable through the same governance architecture, and provenance-recorded per A2.40.

## 6. Operational implications

**Configure A2.47 authority distribution per level.** Deployments instantiating the recursive authority architecture must specify, as substrate content under A2.47, who holds which of A2.01–A2.04 at cell scope, aspect scope, and Self scope. This is a deployment configuration decision, but it is architecturally required; the recursive authority architecture cannot operate without explicit authority distribution at each level.

**Conduct level-appropriate governance reviews.** Because each level has independent governance affordances, governance review can be scoped to the level where improvement is needed. A review of a specific cell's orchestration rules requires A2.01 (inspect cell DNA) and A2.02 or A2.04 at cell scope; it does not require Self-level access. An architectural review of Self integration requires A2.01–A2.04 at Self scope; it does not require reviewing every constituent cell. Level-appropriate review is both more efficient and more precise than deployment-level review.

**Use affordance independence to isolate governance scope.** Because affordance exercise at one level does not automatically affect other levels, governance actions can be scoped to exactly the level that requires attention. A cell that is producing suboptimal decisions can be overridden at cell scope (A2.03) or have its DNA modified through directed selection (A2.02 at cell scope) without triggering review or modification of the aspect it participates in or the Self it belongs to. The surgical governance property means governance debt does not propagate upward by default.

**Treat vertical evolution per B1.16 as the governed cross-level pathway.** When governance action at one level should produce effects at another — for example, a cell DNA modification that should inform an aspect coordination rule change — that cross-level effect should flow through vertical evolution per B1.16, which is the governed pathway for cross-level propagation. Affordance independence is the architectural default; vertical evolution is the governed exception.

**Record affordance events with provenance per A2.40.** Every exercise of A2.01–A2.04 at any level produces a substrate event. These events carry provenance metadata — who exercised which affordance, at which level, on which substrate content, under which authority — per A2.40. This is what makes the authority architecture auditable and the governance record retraceably linked to specific actors at specific levels.

## 7. Limits

**Recursive affordances do not mean the same human holds all affordances at all levels.** The recursive authority architecture specifies that all four affordances exist at each level. It does not distribute them uniformly. A2.47 authority distribution specifies who holds what at which level, and different humans may hold different affordances at different levels. A cell operator may hold A2.02 at cell scope without holding A2.04 at Self scope. A deployment architect may hold A2.04 at Self scope without holding A2.03 at cell scope. The architecture is recursive; the distribution is not necessarily uniform.

**Affordance independence is the default; it is not absolute.** Independence means affordance exercise at one level does not automatically trigger affordances at other levels. It does not mean cross-level effects are impossible. Vertical evolution per B1.16 is the governed pathway through which changes at one level are propagated to other levels. That pathway requires its own governed decision and its own provenance record; it does not flow automatically.

**A2.03 (override) at cell scope is not A2.02 (modify cell DNA).** These are distinct operations. Override addresses a specific decision produced during a specific execution, without modifying the rules that produced it. Modification through directed selection changes the DNA — the standing rules and behavior substrates — that govern future executions. Conflating them produces governance actions with unintended scope: an operator intending to address one bad decision should use A2.03; an operator intending to change the cell's standing behavior should use A2.02. The distinction is architectural, not terminological.

**The affordances are rights, not actions.** A2.01–A2.04 at each level are governance affordances — the ability to exercise them. A deployment instantiating the recursive authority architecture may operate for extended periods without any affordance being exercised. That is not a failure of the architecture; it is the architecture working as specified. Governance cost is not a function of how often affordances are exercised (per A1.01's authority-not-labor framing); it is a function of rule variety (Moment 1 in A1.01's governance-moments analysis) and intervention frequency (Moment 2), neither of which is proportional to substrate size.

**The specific mechanisms per affordance at each level are covered by prior decomposition notes.** B2.99–B2.101 formalize the specific mechanisms for inspect, modify, and override at each level. B2.68 and B2.75 formalize the directed selection mechanism and the lineage properties that modification through A2.02 produces. This note establishes the recursive authority architecture as the overarching affordance framework; the mechanism notes fill in the operational detail per affordance per level.

## 8. Operational test

A CKS deployment instantiates the recursive authority architecture if and only if, at each of the three structural levels (cell, aspect, Self), all four governance affordances (A2.01 inspect, A2.02 modify, A2.03 override, A2.04 rule authoring) are available to the humans specified by A2.47 authority distribution, with affordance exercise at one level neither automatically triggering nor automatically blocked by affordance state at any other level, and with every affordance exercise event recorded as provenance-carrying substrate content per A2.40.

## 9. Why naming this as a standalone derivation matters

The recursive authority architecture is the architectural claim that makes entity-level governance at every structural granularity possible. Without it, the extension of Paper 1's governance commitments to Paper 2's three-level composition structure would be an informal generalization rather than a specified commitment. With it, the affordance architecture is precise: four affordances, three levels, level-appropriate subject matter, explicit authority distribution, affordance independence as the default.

Naming this as a standalone derivation establishes public prior art for the combination: a governance affordance architecture in which the same four affordances (inspect, modify, override, rule authoring) apply independently at each of three specified composition levels (cell, aspect, Self), with authority distribution configured per level, and with affordance exercise at one level not automatically producing cross-level effects. This combination is not found, as an architectural commitment with this specificity, in multi-agent governance frameworks, hierarchical state machine governance models, or deployment-level governance architectures for AI systems. The prior-art record established here covers the architectural pattern and its named components.

B2.107 is the tenth of thirteen notes decomposing B1.20. Three remain: B2.108 (recursive conflict-as-first-class, A1.03), B2.109 (recursive operational tests), and B2.110 (recursive commitments verification). Together they complete the B1.20 recursive Paper 1 commitments decomposition, closing the operational-variant phase of the Series B derivation record.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Recursive Authority Architecture (A2.01–A2.04): How the Four Governance Affordances Apply at Cell, Aspect, and Self Scope, Enabling Entity-Level Governance at Every Structural Granularity.* May 12, 2026. ORCID: 0009-0004-8065-3235.
