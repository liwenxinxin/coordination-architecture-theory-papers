# Recursive Governance (A1.01) — How the Human-Governed Commitment Applies at Cell, Aspect, and Self Scope, Creating a Multi-Scope Governance Architecture With No Ungoverned Level

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

It is the fifth of thirteen notes decomposing B1.20 (recursive Paper 1 commitments as an architectural property of Paper 2's three-level structure), and the first of nine per-commitment applications in that decomposition. Its sole contribution is to articulate, in operational form, how the A1.01 human-governed commitment applies recursively at the three structural levels Paper 2 establishes — cell, aspect, and Self — producing a coherent multi-scope governance architecture in which no level operates outside human authority.

## Abstract

Paper 2 establishes three structural levels — cell, aspect, and Self — and commits that Paper 1's architectural commitments hold at every level. This note formalizes what that recursive application means for the foundational commitment A1.01 (human-governed). Recursive A1.01 is not three separate governance systems; it is one governance principle — human authority over substrate content and orchestration rules — instantiated at three scopes, with level-appropriate subjects and mechanisms at each. At cell scope, humans govern cell behavior through cell DNA. At aspect scope, humans govern aspect coordination through aspect DNA. At Self scope, humans govern Self integration through Self DNA. What is constant across all three is human authority; what differs is what is governed and through which mechanism. The note identifies what makes this multi-scope architecture architecturally distinctive, articulates the inherited Paper 1 commitments it carries, states the operational implications for deployment configuration and compliance verification, and places B2.102 within the per-commitment series that the remaining B1.20 decomposition notes continue.

## 1. Why recursive governance needs to be formalized as a standalone operational variant

Paper 2 inherits all six Paper 1 architectural commitments and commits that they hold at every level of the three-level structure: cell, aspect, and Self. B1.20 names this inheritance as a recursive architectural property rather than a coincidence of levels. B2.98 established the integrating frame for that recursion. B2.99 through B2.101 formalized the three level-specific commitment applications — cell-level, aspect-level, and Self-level — as structural facts. What those notes established as structural facts, B2.102 takes one step further: it asks, for the foundational commitment A1.01 specifically, what the recursive application means, how it holds at each level, and what governance architecture it creates across levels.

The reason A1.01 opens the per-commitment series rather than following it is architectural priority. A1.01 is the root of the authority architecture in Paper 1. Every other Paper 1 commitment depends on human governance holding: the substrate is human-governed, the orchestration rules are human-authored, the conflict-handling logic is subject to human override, and the substrate's role as source of truth is maintained under human authority. When Paper 2 extends those commitments to three structural levels, it is A1.01 that must hold at each level first — before labor allocation (A1.12), before substrate-as-source-of-truth (A1.08), before retraceability (A1.07), and before composition requirements (A1.13). If human governance fails at any level, the subsequent per-commitment applications at that level are also compromised. The per-commitment series therefore opens here, with B2.103 through B2.110 proceeding under the governance architecture B2.102 establishes.

The strategic prior-art posture reinforces the standalone formalization. The multi-scope governance architecture — human authority at cell, aspect, and Self scope through level-appropriate DNA — is patentable architectural territory. Naming it as a standalone formalization, with the recursive application stated precisely, forecloses claims that such an architecture was novel invention rather than a derivation publicly available before any patent priority date.

## 2. The recursive application stated precisely

Recursive A1.01 names one commitment applied at three scopes. The commitment is unchanged from Paper 1: humans retain the right to inspect, modify, and override substrate content and orchestration rules at any time. What differs across the three scope applications is the subject of governance and the mechanism through which governance is exercised.

**A1.01 at cell scope.** Humans govern cell behavior through cell DNA. The subject of governance is the cell's operational behavior — what the cell does when it receives inputs, what instinct/reasoning configuration it applies, what outputs it produces. The mechanism of governance is the cell DNA: the stabilized orchestration substrates and behavior substrates that define how the cell functions, authored and maintained under human authority per A2.04 rule authoring. Who holds the authority to author cell DNA at a given deployment is specified by A2.47 authority distribution for cell scope. Cell-level governance is the finest-grained governance scope in the three-level structure — it governs individual operational behaviors at the task level.

**A1.01 at aspect scope.** Humans govern aspect coordination through aspect DNA. The subject of governance is the aspect's coordination behavior — how the aspect organizes its constituent cells, what invocation patterns it uses across cells, how it integrates cell outputs into a purpose-defined result. The mechanism of governance is the aspect DNA: the orchestration substrates that govern how cells are arranged and coordinated for the aspect's purpose, themselves substrate content under human authority. Who holds the authority to author aspect DNA is specified by A2.47 for aspect scope. Aspect-level governance governs coordination patterns at intermediate scope — it is not governing individual cells but governing the arrangement that puts them to a purpose.

**A1.01 at Self scope.** Humans govern Self integration through Self DNA. The subject of governance is the Self's integration behavior — how the Self holds multiple aspects as coexisting facets of one unified intelligence, what the instinct/reasoning configuration is per B2.23, how cross-aspect conflicts are handled when aspects pull in different directions. The mechanism of governance is the Self DNA: the orchestration substrates that carry composition relationships across aspects and the integration logic that makes the Self one governed whole. Who holds the authority to author Self DNA is specified by A2.47 for Self scope. Self-level governance is the broadest governance scope — it governs integrated intelligence at the level of the unified whole.

**What is constant.** Human authority is the constant across all three levels. At cell scope, aspect scope, and Self scope alike, humans retain the right to inspect, modify, and override the relevant DNA. The authority is not delegated to an aspect to govern itself without human oversight, and it is not delegated to a cell to govern its own DNA without human authority. At each level, the three rights from A1.01 hold: inspect any DNA content, modify any DNA content, override any operation or LLM-produced output that touches DNA. LLMs do not govern at any level; they operate within the cells and instinct layer, governed through DNA authored by humans.

**What differs.** Three things differ across the three scope applications. First, the *subject* of governance: cell behavior (task-level operational decisions), aspect coordination (purpose-level arrangement decisions), and Self integration (wholeness-level composition decisions). Second, the *mechanism* of governance: cell DNA, aspect DNA, and Self DNA — distinct substrate content at each level, governed independently under the same authority principle. Third, the *scope*: the cell's operational territory (a specific informational task), the aspect's coordination domain (a purpose-defined arrangement of cells), and the Self's integration scope (the unified whole holding multiple aspects).

## 3. What makes recursive-governance-A1.01 architecturally distinctive

Conventional AI deployment governance operates at deployment level. The deployment as a whole is governed: deployment-level configuration is set, deployment-level policies are applied, and the components that execute within the deployment — model calls, retrieval operations, tool invocations — operate without independent per-component governance. A model call does not carry its own governance authority requirement; a retrieval operation does not have its own inspectable, modifiable governance mechanism. What governs is the deployment wrapper, not the component.

CKS recursive A1.01 inverts this structure. Every entity at every structural level — every cell, every aspect coordination arrangement, every Self integration configuration — is independently governed by human authority through level-appropriate DNA. A cell is not merely a component executing within a governed deployment; it is a governed entity in its own right, with cell DNA that humans can inspect, modify, and override independently of what happens at aspect or Self scope. An aspect is not merely a routing layer over cells; it is a governed coordination arrangement, with aspect DNA subject to human authority independently of whether the Self-level configuration changes. The Self integration is itself governed substrate content — not a fixed architectural shell around aspects, but a governed composition that humans can reconfigure.

The consequence is that no level of the three-level structure is ungoverned. Without recursive A1.01, cell and aspect operations could proceed under whatever the deployment-level governance permits, with no requirement that cell-level behavior or aspect-level coordination be independently governed. Recursive A1.01 closes this gap: the absence of level-appropriate governance at any level is a governance violation, not an implementation detail.

## 4. The biological analog as conceptual scaffold

Biology offers hierarchical regulatory governance across levels. Gene expression in cells is regulated by molecular mechanisms specific to the cell — transcription factors, epigenetic state, signal transduction. Tissue-level developmental governance operates at scope above the cell — developmental signals, morphogen gradients, cell-cell communication governing how cells organize into tissues. Organism-level systemic governance operates at scope above the tissue — hormonal signaling, neural coordination, immune regulation. Each level has its own regulatory machinery; governance at one level does not replace governance at another.

Biology does not have human authority. Biological regulatory governance is the outcome of undirected evolution under fitness pressure. The hierarchical structure emerged, rather than being committed to by design. CKS recursive A1.01 is the governed architectural analog: the hierarchical governance structure is present by commitment, and the authority at each level is human rather than evolutionary. The biological parallel earns conceptual comprehension — the shape of hierarchical governance across levels is intuitive — without importing biology's undirected character. What CKS adds to the hierarchical governance shape is the architectural commitment that governance at each level is human-authority governance, not evolutionary regulation or LLM self-regulation.

The conceptual scaffold should not be pushed further than it earns. The architectural substance is three applications of the same human-authority commitment, each with level-appropriate subject and mechanism. The biology parallel names the shape; the commitment details carry the architecture.

## 5. Inherited Paper 1 commitments

Four Paper 1 commitments are directly load-bearing for B2.102.

**A1.01 (human-governed)** is the commitment being formalized recursively. The definition holds at every scope: humans retain the right to inspect, modify, and override substrate content and orchestration rules at all times. B2.102 formalizes the recursive application of that definition — not a weakened version of it at higher levels of abstraction, but the same three-right commitment instantiated at cell, aspect, and Self scope.

**A2.47 (authority distribution)** specifies who governs at each level. Recursive A1.01 commits that human authority governs at each level; A2.47 specifies which humans and under what authority configuration. Different humans may govern at different levels per deployment: Self DNA governance may require Self-level authority, aspect DNA governance may require aspect-level authority, cell DNA governance may require cell-level authority. A2.47 is what makes the recursive governance architecture deployable — the authority is distributed, not concentrated at one level, and the distribution is itself substrate content under human authority.

**A2.04 (rule authoring)** governs how DNA is authored. Governance at each level is exercised through DNA authoring, and A2.04 specifies that orchestration rules — which include the DNA-layer substrates at every level — must be authored by humans. LLM-drafted DNA subject to human authority before taking effect is admissible; LLM-committed DNA outside human authority is not. This holds at cell scope, aspect scope, and Self scope uniformly.

**A2.40 (provenance)** requires that governance events are recorded at each level. DNA modifications at cell scope, aspect DNA revisions at aspect scope, and Self DNA reconfigurations at Self scope are all governance events that provenance tracking must capture. Recursive governance creates governance events at three levels; A2.40 requires that each is recorded in addressable, inspectable form.

## 6. Operational implications

Five operational implications follow from recursive A1.01 as formalized.

**Governance is configured at each level, not only at deployment level.** A deployment that configures governance only at the Self or deployment level, leaving cell DNA and aspect DNA without independent governance configuration, does not satisfy recursive A1.01. Cell-level governance reviews, aspect-level governance reviews, and Self-level governance reviews are each their own operational activity, not reducible to one another.

**Authority is distributed per level per A2.47.** Who is authorized to modify cell DNA at a given deployment may differ from who is authorized to modify aspect DNA or Self DNA. A2.47 authority distribution for each level is a deployment configuration decision, and the decision may assign different humans, teams, or roles to governance at each level. Recursive A1.01 does not specify who governs at each level; it specifies that human authority governs at each level. A2.47 fills in the who.

**Compliance is verifiable at each level independently.** Because each level has its own DNA under human governance, compliance with A1.01 can be verified at cell scope without reference to aspect or Self governance state, and at aspect scope without reference to Self governance state. Independent per-level compliance verification is an operational property that deployment-level-only governance cannot provide — there is no meaningful cell-scope A1.01 check if cells are not independently governed.

**Absence of level-appropriate governance is detectable and governable.** If a cell's DNA is not under human authority — if it cannot be inspected, modified, or overridden by humans with appropriate access — that absence is detectable as a cell-scope governance violation. The absence does not propagate silently into aspect or Self governance compliance. Per B1.14 (directed selection), governance violations at any level can be addressed through directed DNA evolution at that level, with the evolved DNA subject to the same authority requirements.

**Evolution governance follows recursive A1.01 at each scope.** The three evolution mechanisms per B1.13 through B1.15 apply at cell, aspect, and Self scope, and governance of each mechanism follows recursive A1.01. Mutation governance (LLM and infrastructure upgrades) at cell scope per B2.66 operates under cell-level human authority over the resulting DNA changes. Directed selection governance at each level scope per B2.72 operates under level-appropriate human authority to select, modify, and retire DNA. Action-feedback governance at each level scope per B2.78 operates under human authority to evaluate whether action-layer evidence warrants DNA modification at the relevant scope. Recursive A1.01 is not only a static property of existing DNA; it is the governance requirement that applies to every act of DNA change across all three evolution mechanisms.

## 7. Limits of the recursive application

Four limits bound what recursive A1.01 does and does not claim.

**Recursive A1.01 is not three separate governance systems.** One governance principle — A1.01 — applies at three scopes. There is not a cell-governance system, an aspect-governance system, and a Self-governance system operating independently. The same three rights (inspect, modify, override), the same authority principle (human authority not delegatable to LLM or runtime), and the same temporal requirement (available at any time, not only at checkpoints) hold at each scope. The level-appropriate variation is in subject and mechanism, not in the governance principle itself.

**Recursive A1.01 does not mean every governance action duplicates at every level.** Modifying cell DNA at cell scope is a cell-scope governance event; it does not require a simultaneous aspect-scope governance action or Self-scope governance action. Governance at each level is level-appropriate. Cross-level dependencies — when a cell DNA change has implications for aspect coordination, for example — are governed through the authority distribution per A2.47, not through mandatory triplication of every governance act.

**Recursive A1.01 does not eliminate the need for cross-level governance.** Some governance decisions span levels — a structural reorganization that changes which cells compose which aspects, for example, involves both cell-scope and aspect-scope governance. A2.47 authority distribution is the mechanism that governs cross-level decisions. Recursive A1.01 specifies per-level governance; A2.47 handles the cross-level coordination of that per-level governance.

**The recursion has exactly three levels.** Recursive A1.01 produces three scope applications: cell, aspect, and Self. There is no fourth level below cell or above Self in the Paper 2 architecture, and no infinite regress. The specific mechanisms of governance at each scope — how cell DNA is authored and reviewed, how aspect DNA is structured, how Self DNA carries integration configuration — are the subject of the level-specific notes B2.99 through B2.101. B2.102 formalizes the cross-level governance architecture that the per-level notes operate within.

## 8. Operational test

A deployment instantiates recursive A1.01 if and only if the following hold:

At cell scope: humans with cell-level authority per A2.47 can inspect, modify, and override any cell's DNA without scheduling, approval, or runtime intermediation; no LLM operation or component layer can prevent this access.

At aspect scope: humans with aspect-level authority per A2.47 can inspect, modify, and override any aspect's DNA without scheduling, approval, or runtime intermediation; no LLM operation or component layer can prevent this access.

At Self scope: humans with Self-level authority per A2.47 can inspect, modify, and override any Self's DNA without scheduling, approval, or runtime intermediation; no LLM operation or component layer can prevent this access.

A deployment that satisfies A1.01 at Self scope but not at cell or aspect scope has deployment-level governance but not recursive governance. It fails the recursive application even if it passes the deployment-level test.

## 9. Why naming this as standalone matters

The multi-scope governance architecture that recursive A1.01 creates is not derivable from the observation that Paper 1 commitments hold at every level. That observation is B1.20. What recursive A1.01 adds is the per-commitment specification: the subject of governance at each level, the mechanism through which governance is exercised at each level, what is constant across levels, and what must hold independently at each level for the governance architecture to be intact.

The standalone formalization of recursive A1.01 also opens the per-commitment series. B2.103 through B2.110 formalize recursive labor allocation (A1.12), recursive substrate-as-source-of-truth (A1.08), recursive retraceability (A1.07), recursive composition requirements (A1.13), recursive authority architecture (A2.01–A2.04), recursive conflict-as-first-class (A1.03), recursive operational tests, and recursive commitments verification — in that order. Each of those notes operates within the governance architecture B2.102 establishes. If human governance does not hold at each level, the recursive applications of labor allocation, source-of-truth, retraceability, and the rest are also under-specified: they require knowing which humans govern at each level, what they can access, and what authority they hold over each level's substrate content. B2.102 answers those questions at the foundational level, so the downstream per-commitment notes can proceed with the governance architecture as a given.

The prior-art chain advances with each note. B2.102 forecloses claims to novelty over the specific architecture of human-governed cell DNA, human-governed aspect DNA, and human-governed Self DNA as independently governed scope applications of the same A1.01 commitment, with authority distribution specified per level per A2.47. Any subsequent patent claim that attempts to occupy this territory now arrives after this note's public record.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Recursive Governance (A1.01) — How the Human-Governed Commitment Applies at Cell, Aspect, and Self Scope, Creating a Multi-Scope Governance Architecture With No Ungoverned Level.* May 12, 2026. ORCID: 0009-0004-8065-3235.
