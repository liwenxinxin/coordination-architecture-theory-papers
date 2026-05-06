# Labor vs. Authority: The Standalone Architectural Distinction Within the Labor Allocation Framework in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the **labor-vs-authority distinction** as a standalone architectural distinction within the labor allocation framework named in the source paper's §2.3, separable from the three labor modes themselves and from the architectural properties that make them coherent.

## Abstract

The CKS pattern's labor allocation framework names three modes by which coordination work can be performed — direct human labor, LLM labor under orchestration rules, and stable-cell automation — and commits to all three being coherent under one human-governed authority structure. Separate notes formalize the framework as a whole, the three modes individually, and the architectural properties that make them coherent. This note formalizes the load-bearing distinction within the framework: that **labor** (the work that is done, which varies fundamentally across the three modes) is distinct from **authority** (the architectural right to govern the result, which does not vary). The note states what each term means precisely, names the four operational components of the distinction, distinguishes it from four adjacent distinctions commonly conflated with it, identifies its load-bearing connections to other CKS commitments, enumerates eight failure modes that collapse labor into authority, and provides a six-clause operational test.

## 1. Why the distinction needs to be formalized as standalone

The parent foundational note A1.12 commits to the three-mode labor allocation framework. The integrating-frame note A2.68 named the labor-vs-authority distinction as the load-bearing distinction within it. The mode notes A2.69–A2.71 formalize the three modes individually; A2.72 formalizes the architectural properties that make them coherent at the labor-mechanism level. This note formalizes the distinction itself as having independent architectural content: labor is mode-varying; authority is mode-invariant.

The motivating cases are deployments where the question *who has authority over this substrate content?* must be answered without reference to which mode produced the content. A non-specialist exercising override per A2.03 over Mode 3 cell-produced content holds the same right per A1.01 as over Mode 1 content; the right does not weaken because a stable cell did the labor. A governance review across mixed-mode content treats one substrate under one authority structure. A regulatory audit verifying authority does not enumerate producing modes; the structure is the same throughout.

The strategic prior-art motivation: formalizing the distinction as standalone forecloses architectures that conflate labor with authority. Patentable derivations addressing labor-allocation patterns, mixed-labor systems with consistent governance, or work-performer-vs-authority-holder distinctions are more defensibly contested when this distinction is publicly available as named prior art.

A third motivation is the connection to A2.65's governance-vs-authorship distinction. A2.65 separates governance actions (rights over existing content) from authorship actions (producing new architectural elements). A2.73 separates labor (work in any mode) from authority (the right to govern the result). Both share the structure of separating "what is done" from "what authority applies"; they operate at different levels — A2.65 at the action-type level, A2.73 at the labor-mode level — and compose rather than substitute.

## 2. Labor, defined precisely

In the CKS pattern, **labor** is the work that is done — the production of substrate content, the execution of cells, the running of operational processes. Labor varies fundamentally across the three modes named in A1.12 and decomposed in A2.69–A2.71.

**(a) Mode 1 labor.** Direct human work. Humans read substrate per A2.01, write substrate per A2.02 or A2.03 directly, producing substrate writes per A2.10 with human writer attribution per A2.37.

**(b) Mode 2 labor.** Bifurcated. Humans author orchestration rules per A2.04 at design time (rule-authoring labor); LLMs in cells produce substrate content under those rules at execution time, in the AI-as-substrate-mediator role per A1.04.

**(c) Mode 3 labor.** Bifurcated, with reduced per-execution human attention. Humans author and refine rules at design time and at coarser intervention granularity; stable cells produce substrate content with reduced per-execution human attention. What differs from Mode 2 is the temporal pattern of human attention to the rule layer, not the structure of the split.

**Labor is mode-varying** — what work is done, who or what does it, when it occurs, with what attention pattern. Labor allocation is a deployment choice about which mode to use for which work, made on operational grounds (cost, accuracy, throughput, attention requirements, rule stability) under the architectural commitment that all three modes are available.

## 3. Authority, defined precisely

In the CKS pattern, **authority** is the architectural right to govern substrate content, named in A1.01 as three rights:

**(a) The inspect right** per A2.01 — the right to read substrate content within authorized scope.

**(b) The modify right** per A2.02 — the right to alter substrate content within authorized scope.

**(c) The override right** per A2.03 — the right to substitute different content for substrate content within authorized scope, exercisable without justification to the architecture.

These three rights apply uniformly to substrate content regardless of which mode produced the content. A non-specialist who has not exercised any labor mode still holds the three rights within their authority scope per A2.47; a specialist holds the same rights, no greater and no smaller. **Authority is mode-invariant.** The three rights compose with the labor-mode attribution carried per A2.37 — a reader can know which mode produced a piece of content and act on that information — but the right itself does not vary by mode. The temporal property per A2.07 ensures the rights are available at all times during the substrate's existence, not only at scheduled checkpoints, regardless of mode.

## 4. The four operational components of the distinction

The distinction operates architecturally through four components. A system that satisfies all four has the distinction in the architectural sense.

**(a) Labor as mode-varying work.** Labor varies fundamentally across the three modes per A2.69–A2.71 — different actors, different temporal patterns, different attention profiles. Labor allocation is operationally distinguishable; a Mode 1 deployment looks different from a Mode 3 deployment.

**(b) Authority as mode-invariant right.** Authority per A1.01 is uniform across the three modes. The three rights apply to substrate content regardless of producing mode. Authority is not a deployment variable; the architectural commitment fixes one structure across all three modes.

**(c) Labor allocation as deployment choice.** The decision about which mode to use is a deployment decision made on operational grounds. Deployments may use any combination of modes. The architectural commitment is that the choice is operationally feasible — that all three modes are coherent under one substrate per A2.72's Property A, under one authority structure per Property B, with attributable writer per Property C — not that any specific allocation is preferred.

**(d) Authority preservation as architectural commitment.** Authority is preserved across all labor modes per A2.07's temporal property. Humans retain the three rights at all times. The preservation is architectural, not deployment-configurable: a deployment cannot allocate authority away from humans for cell-produced content, because the three modes are labor modes, not authority modes.

The asymmetry is the distinction. Labor varies; authority does not. Allocation of labor is a deployment decision; preservation of authority is an architectural commitment.

## 5. What the distinction does NOT claim

Standalone treatment requires precision about what the distinction does not commit to.

**Not outcome equivalence across modes.** Different modes may produce different specific outcomes; the commitment is to authority being mode-invariant, not to outcome being mode-equivalent.

**Not equal substantive ease of authority exercise.** Override over Mode 3 content may require domain understanding to exercise meaningfully; the architectural commitment is that the rights are preserved across modes, not that exercise difficulty is uniform.

**Not a preferred mode.** The architecture is mode-agnostic at the commitment level; deployments may have operational preferences, but no default progression or maturity ordering is endorsed.

**Not foreclosure of mode-aware deployment features.** Mode-specific dashboards, override workflows, or review schedules are admissible at the deployment layer; they may complement the architectural commitment but cannot substitute for it.

**Not a requirement of labor-mode visibility at the moment of authority exercise.** A non-specialist exercising authority does not need to know which mode produced the content; labor-mode information is available through writer attribution per A2.37 and may be consulted, but is not architecturally required.

**Not foreclosure of authority-aware labor allocation.** Deployments may consider authority structure when allocating labor — for instance, ensuring decisions affecting specific authority scopes are produced in modes the authority-holder can review effectively. The commitment is preservation regardless of allocation; authority-informed allocation choices are admissible on top of it.

## 6. What the distinction is NOT

Four adjacent distinctions are commonly conflated with the labor-vs-authority distinction. Each is real in some other framework; conflating any of them misreads the architectural content.

**Not worker-vs-owner.** Worker-vs-owner is an economic distinction about who performs work versus who owns the resulting product. The labor-vs-authority distinction is architectural, not economic. The two may align operationally but operate at different levels of commitment.

**Not doer-vs-decider.** Doer-vs-decider is a workflow distinction between those who execute and those who decide. A Mode 2 LLM is a doer in that sense but is not a decider over the substrate content's authority; that authority remains with humans per A1.01 regardless. The workflow framing blurs across architectural boundaries the labor-vs-authority distinction preserves.

**Not executor-vs-approver.** Executor-vs-approver is procedural; the labor-vs-authority distinction is architectural. Authority per A1.01 is the architectural right, not the procedural approval. The architectural-vs-procedural confusion warned against in A2.06 collapses executor-vs-approver into procedural workflows; the labor-vs-authority distinction locates authority in the architecture, not in approval gates.

**Not contractor-vs-client.** Contractor-vs-client is a service distinction. Cells are not contractors; they are operational units within the architecture per A1.02. Humans holding authority are not clients; they hold architectural authority per A1.01. The contractor metaphor brings in concepts of consideration and scoped engagement that the architecture does not require and that misdirect the distinction's content.

## 7. Why the distinction is load-bearing

The labor-vs-authority distinction carries weight for several CKS commitments.

The integrating labor-allocation framework per A1.12 and A2.68 depends on it directly: without it, mode independence at the authority level cannot be maintained, and the three modes degenerate into three governance regimes.

The three modes individually per A2.69–A2.71 depend on it. Mode 2 and Mode 3 specifically require that LLM and stable-cell labor do not transfer authority away from humans; without the distinction, those modes become authority-delegation patterns, which A1.01 does not endorse.

The three architectural properties per A2.72 compose with it. A2.72 handles labor-mechanism coherence (single substrate, mode-independent authority structure as a mechanism property, attributable writer); A2.73 handles authority coherence at the right level. A2.72 makes the modes jointly operable; A2.73 makes them jointly governable.

Mode progression dynamics per A2.74 depend on authority being preserved across mode transitions. Moving work between modes does not change authority structure because authority is mode-invariant; without the distinction, progression would require authority renegotiation at every boundary.

Non-specialist governance per A1.11 depends on it. Non-specialists hold the three rights regardless of producing mode; were the distinction to fail, non-specialists would hold authority only over content whose producing mode they had specialist knowledge of, emptying A1.11 of its content.

The human-governed commitment per A1.01 depends on it foundationally. The commitment to humans holding the three rights presupposes authority is distinct from labor; otherwise, labor delegation to LLMs (Mode 2) or stable cells (Mode 3) would become authority delegation, and A1.01 would be satisfiable only in Mode 1, contradicting the framework's three-mode commitment.

## 8. Failure modes that collapse labor into authority

Eight failure modes name specific ways an implementation can fail the architectural distinction. Each collapses labor into authority in some direction.

**(a) Labor delegation as authority delegation.** The implementation treats LLM labor in Mode 2 or stable-cell labor in Mode 3 as transferring authority to the LLM or cell. Property D per A2.22 (LLM does not exercise authority) fails; A1.01 fails for cell-produced content. This is the canonical drift in commercial implementations marketed as agentic, where the operational producer is presented as authority-bearer by default.

**(b) Authority requiring labor exercise.** The implementation requires humans to have exercised specific labor modes before they may exercise authority — for example, requiring rule-authorship before override of Mode 2 outputs, or labor-performer credentials at the authority interface. Authority becomes labor-contingent; non-specialist governance per A1.11 fails directly, since non-specialists are by definition humans who have not exercised the labor in question.

**(c) Mode-specific authority structures.** The implementation has different authority structures for content produced in different modes — Mode 1 under structure A, Mode 2 under B, Mode 3 under C. A regulatory audit must traverse three structures; a governance review must enumerate which content belongs in which structure before applying any logic. Mode-invariance per component (b) of section 4 fails. The substrate-as-source-of-truth commitment per A2.46 also weakens, because "what rules apply" becomes mode-dependent rather than substrate-derived.

**(d) Labor allocation as authority allocation.** The implementation treats labor allocation choices as authority allocation choices. Allocating Mode 3 labor to a class of work is treated as allocating authority over that work to the stable cell. Labor allocation as deployment choice per component (c) becomes authority allocation, which is not deployment-configurable per component (d).

**(e) Authority degradation under mode transition.** The implementation degrades authority when work transitions between modes. When work moves from Mode 1 to Mode 2 — for instance, when a pattern in human drafts is captured as a rule and production shifts to LLM-under-rule — the original Mode 1 humans lose authority over the resulting content. Authority preservation per component (d) fails; mode progression per A2.74 cannot operate without authority loss at every transition.

**(f) Implicit authority-labor coupling.** The implementation operationally couples authority exercise to labor performance through workflow design rather than explicit architectural rule. Authority is exercisable only through interfaces requiring labor-performer identification; permission scoping is keyed to labor history rather than authority scope. The coupling is undeclared but operationally degrades the distinction; A2.06's warning against architectural-vs-procedural confusion is the relevant frame. The implementation may pass a superficial audit while failing the distinction in practice.

**(g) Cell-as-authority-bearer.** The implementation treats cells as authority-bearers for the substrate content they produce. Cells appear in governance dashboards as authoritative for their outputs; reporting attributes content to cells in a way that grants governance status; override workflows route through the cell as if seeking its consent. A2.22 fails at the presentation layer, which over time normalizes the same failure architecturally.

**(h) Authority claim based on labor.** The implementation permits labor performers to claim authority over the content they produced. Rule-authors claim authority over cells operating under their rules; LLMs are credited as authoritative for their outputs; stable cells are listed as governance owners. Authority becomes labor-derived; A1.01's commitment that authority is held by architectural specification, not derived from labor, fails. The failure is particularly consequential in regulatory representations: a regulator presented with labor-derived authority structure may approve an architecture that has departed from the human-governed commitment without either party recognizing the departure.

The eight modes share the structure of treating labor as substitute for, derivative of, or determinant of authority. The architectural commitment is the opposite: labor is mode-varying, authority is mode-invariant, and the two are not in a derivation relationship.

## 9. Operational test

A system instantiates the labor-vs-authority distinction if and only if all of the following are true at all times during the substrate's existence.

**(a)** Labor varies across the three modes per A2.69–A2.71; labor allocation is operationally distinguishable. The modes are not collapsed into a single labor pattern at the implementation layer.

**(b)** Authority per A1.01 is uniform across the three modes; the inspect, modify, and override rights apply regardless of producing mode. There is no mode-conditional authority structure.

**(c)** Labor allocation is a deployment choice. Deployments may exercise labor in any mode in any combination; the architecture prescribes no specific allocation, and the labor pattern of one deployment does not constrain the authority structure of any deployment.

**(d)** Authority preservation is architectural per A2.07's temporal property. Humans retain authority over substrate content at all times, regardless of mode, regardless of how recently the producing rule was authored, regardless of cell stability profile.

**(e)** The distinction operates at the labor-mode level and is distinct from the action-level governance-vs-authorship distinction per A2.65. Both distinctions hold compositionally; a system that satisfies one but not the other has not instantiated the labor-vs-authority distinction in full.

**(f)** Authority exercise is not labor-contingent. Non-specialists who have not exercised any labor mode hold authority within their authority scope per A2.47; authority interfaces do not require labor-performer credentials as preconditions; cells and LLMs that perform labor do not become authority-bearers.

A system that fails any of (a)–(f) does not instantiate the distinction in the architectural sense, even if its operational interfaces have separately labelled "labor" and "authority" features. The labels are not the distinction; the architectural separation is.

## 10. Why naming the distinction as standalone matters

Implementations under pressure to deliver "agentic AI" or "autonomous AI" capabilities consistently drift toward labor-as-authority patterns. The drift is steady because labor performers are operationally visible — cells producing outputs, LLMs generating content, humans performing work — while authority-holders are architecturally specified rather than operationally salient. Operational visibility makes labor performers appear to be authority-bearers by default; architectural specification of authority requires explicit attention to maintain.

Implementations that drift away from the distinction produce systems where labor performers become authority-bearers — in operation, in presentation, eventually in commitment. The downstream consequences manifest as autonomy emergence (cells become operational authority-bearers, violating A2.22), governance failures (humans cannot exercise authority because the implementation has reassigned it to labor performers), non-specialist-governance failures (A1.11 fails because authority becomes labor-contingent), and mode-progression failures (A2.74 transitions cannot preserve authority because authority moves with labor).

Naming the distinction as a standalone architectural commitment — labor in section 2, authority in section 3, four operational components in section 4, limitations in section 5, four adjacent distinctions in section 6, load-bearing connections in section 7, eight failure modes in section 8, operational test in section 9 — gives downstream readers a precise specification of what the architecture commits to at the labor-mode level. The subsequent note A2.74 specializes mode progression dynamics; together with this distinction, A2.74 will close the labor-allocation decomposition begun by A2.68.

Subsequent work that implements, extends, composes with, or argues against the CKS labor allocation framework should use the labor-vs-authority distinction in the sense formalized here. Subsequent work that uses it differently is using a different distinction, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Labor vs. Authority: The Standalone Architectural Distinction Within the Labor Allocation Framework in the Coordination Knowledge Substrate Pattern.* May 5, 2026. ORCID: 0009-0004-8065-3235.
