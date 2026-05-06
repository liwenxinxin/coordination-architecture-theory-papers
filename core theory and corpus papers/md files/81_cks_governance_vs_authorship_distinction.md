# Governance vs. Authorship: The Standalone Architectural Distinction Between Acting Over Substrate Content and Producing Substrate Content in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 5 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize as standalone the action-level architectural distinction between *governance* — the exercise of the three rights named by the human-governed commitment over substrate content that already exists — and *authorship* — the production of new substrate elements (schema, orchestration rules, cells, initial content). The integrating frame for the non-specialist-governance commitment treats the distinction as one component of a larger commitment; this note treats it as having independent architectural content with its own definition, components, limitations, failure modes, and operational test.

## Abstract

The CKS pattern's commitment to non-specialist governance (§7.4 of the source paper, formalized in Li, 28 April 2026) depends on a load-bearing distinction between two kinds of substrate-related action: *governance*, in which a human exercises authority over substrate content that already exists, and *authorship*, in which a human produces new architectural elements that did not exist before. The architecture commits to the first being accessible to non-specialists; it neither requires nor forbids the second from being so. Without the distinction precisely specified at the action level, the accessibility commitment either over-claims (treating authorship as architecturally accessible) or under-claims (treating governance as requiring authorship expertise). This note formalizes the distinction as standalone: governance is exercise of the three rights from the human-governed commitment over existing substrate content; authorship is production of new substrate elements per the four authorship roles. The note states the four operational components, distinguishes the distinction from four adjacent action distinctions (read-vs-write, consumption-vs-production, edit-vs-create, reviewer-vs-author), names eight failure modes, and provides an operational test.

## 1. Why the distinction needs to be formalized as standalone

The CKS pattern commits to non-specialist governance as an architectural property: the rights to inspect, modify, and override substrate content and orchestration rules are exercisable by humans without specialist expertise, in the host environment's commodity affordances, at any time during the substrate's existence. The companion note on non-specialist governance (Li, 28 April 2026) formalizes this commitment as the integrating frame for what follows.

Inside that frame, one distinction does most of the architectural work: between governance (acting over substrate content that already exists) and authorship (producing new substrate elements). The integrating note articulates the distinction as part of its definition and enumerates four authorship roles to make the asymmetry visible. It does not, however, treat the governance-vs-authorship distinction as having independent architectural content of its own, separable from the question of who can or cannot exercise it.

The motivating reason for separating it now is concrete. Implementations under pressure to deliver accessible AI architectures must answer a precise question for each kind of substrate-related action: is this action architecturally accessible to non-specialists, or is it not? Without the distinction specified at the action level, the answer is operationally ambiguous. Implementations drift in two directions: toward over-claimed accessibility (treating all substrate-related actions as architecturally accessible, with deployment failures when authorship complexity emerges) and toward under-claimed accessibility (treating governance as requiring authorship expertise, with the bottom-up adoption property foreclosed). Both drifts are common; both are addressable only by specifying which action category receives the architectural accessibility commitment and which does not.

A second motivation is the connection to the labor allocation framework (Li, 29 April 2026). That framework distinguishes labor from authority at the labor-mode level: Mode 1 (direct human labor), Mode 2 (LLM under rule), Mode 3 (stable-cell automation). The present distinction does parallel work at the action level: authorship is what is produced; governance is the authority-exercise dimension. Naming them separately is what allows the two to compose — labor mode and action category are independent axes, and a deployment can hold any combination of them under the same governance authority.

## 2. The governance side, defined precisely

In the CKS pattern, **governance** is the exercise of the three rights named by the human-governed commitment (Li, 24 April 2026) over substrate content that already exists. The three rights are:

**(a) The inspect right** (formalized as standalone in Li, 1 May 2026). Reading substrate content within authorized scope, in inspectable form, at the time of the reader's choosing. The reader is not producing new content; they are exercising the architectural right to see what content the substrate carries.

**(b) The modify right.** Altering substrate content within authorized scope. The human is changing what is already present. Modify operations are themselves recorded as substrate writes carrying provenance, and the resulting writes are themselves substrate content; but the architectural action is the alteration of existing content, which is governance.

**(c) The override right.** Substituting different content for substrate content within authorized scope, without architectural justification gating. The human is replacing what is there with what they direct. Override is governance because the action is exercise of authority over existing content — not the production of new architectural elements.

The three rights together constitute governance. Each is architecturally accessible to non-specialists by virtue of three architectural commitments — tool-agnosticism, authority-not-labor, and linear-cost — whose conjunction produces the accessibility property. The accessibility of governance is what the non-specialist-governance commitment commits to architecturally.

## 3. The authorship side, defined precisely

**Authorship** is the production of new substrate elements that did not previously exist. The four authorship roles enumerated in the integrating note name the action categories.

**(a) Substrate schema authorship.** Producing the substrate's structure — entity types, relationships, field constraints, schema-evolution rules. Requires schema-design expertise and understanding of the coordination work the substrate represents.

**(b) Orchestration rule authorship.** Producing the rules that govern cell behavior over substrate content. Requires understanding of how cells operate, what conflict-preservation semantics apply, and how the AI-as-substrate-mediator commitment constrains LLM-under-rule behavior.

**(c) Cell construction.** Producing cell behavior under rules — selecting and configuring LLM components, integrating with the host environment, wiring orchestration rules to cell execution. Requires expertise spanning LLM mediation, orchestration, and the substrate-cell boundary.

**(d) Initial content authorship.** Producing the substrate content the deployment starts with — entities, relationships, decisions, rationale. Requires domain knowledge but not architectural expertise; the integrating note identifies it as the role the architecture's accessibility property bears most directly on.

Authorship is not architecturally required to be accessible to non-specialists. The architectural commitment is to *governance* accessibility; authorship-accessibility is a deployment goal that may or may not be pursued, supported by tooling additions the architecture neither commits to nor forbids.

A load-bearing nuance applies to one of the four roles. **Orchestration rule authorship has both a governance dimension and an authorship dimension simultaneously.** Rule authoring is identified in the human-governed commitment as one of the two moments at which governance is exercised: humans author rules under their preserved authority, and the act of authoring is itself an exercise of that authority. But rule authoring is also production of new substrate elements that did not previously exist, and that production typically requires rule-authoring expertise. The two dimensions decompose as follows. The *authority context* — that the human authoring the rule holds the architectural authority to do so, and that the rule does not become authoritative except through that authority — is governance, and the architectural accessibility commitment applies to it: no specialist gatekeeping is required for the authority itself. The *production* — the rule's content, its consequences for cell behavior, its interaction with the schema and other rules — is authorship, and typically requires rule-authoring expertise. The architectural commitment is to the governance dimension, not to the authorship dimension. Implementations that respect this decomposition support deployments in which non-specialists hold the authority to commission, accept, reject, or revise rule authorings without themselves performing the rule-authoring labor; implementations that collapse the two into one specialist gate or one non-specialist click both fail the architectural distinction in different directions.

## 4. The four operational components of the distinction

The distinction operates architecturally through four components. A system that satisfies all four instantiates the distinction in the architectural sense.

**(a) Governance-as-action-over-existing-content.** Governance actions take existing substrate content as input and have their effect on that content (inspecting it, altering it, overriding it). The existence of the content is a precondition for the action. The action does not produce new architectural elements; if it produces substrate writes (as modify and override do), those writes record the action's effect on existing content, and the action itself is the alteration, not the introduction of a new architectural kind.

**(b) Authorship-as-production-of-new-elements.** Authorship actions produce new architectural elements that did not previously exist. The action's input may include existing substrate content (schema authoring may reference existing entity types; rule authoring may reference existing cells), but the action's effect is the existence of new architectural elements — schema fields, rules, cells, or initial content — that did not exist before.

**(c) Governance-mode-independence.** Governance operates the same way regardless of which labor mode produced the substrate content it is exercised over. A non-specialist exercising the inspect right does so the same way regardless of whether the content was produced in Mode 1 (a human writing directly), Mode 2 (an LLM writing under a rule), or Mode 3 (a stable cell automating the work under stable rules). The governance authority is the same authority across all three, and the architectural property of accessibility holds across all three.

**(d) Authorship-expertise-specificity.** Authorship actions typically require expertise specific to the role being exercised. Schema authorship requires schema-design and domain expertise; rule authorship requires understanding of cell operation and orchestration logic; cell construction requires LLM mediation and integration expertise; initial content authorship requires domain knowledge. The expertise differs by role and is what distinguishes authorship from governance at the accessibility level. The four roles do not collapse into a single uniform "authorship expertise."

The four components are jointly necessary. A system that satisfies (a) and (b) but treats Mode 2 content as harder to govern than Mode 1 has organized actions into two named categories without preserving the architectural property the distinction is for. A system that satisfies (a)–(c) but treats all four authorship roles as requiring uniform "platform expertise" has lost the role-specificity that makes deployment-level role allocation meaningful.

## 5. What the distinction does not claim

The standalone treatment is not maximalist. Five limitations keep the framing from drifting into something stronger than the architecture supports.

It does not claim that all governance actions are equally simple. Inspect actions may be operationally straightforward; modify and override over substantive content may require domain understanding to exercise meaningfully. The architectural commitment is that governance does not *require* authorship expertise, not that all governance actions are equally low-cost.

It does not claim that authorship is uniformly inaccessible to non-specialists. Some authorship actions may be exercisable by non-specialists in some deployments — initial content authorship in a domain a non-specialist holds expertise in, for instance. The architectural commitment is that *governance* is accessible regardless of who can author; it does not specify that authorship is uniformly inaccessible.

It does not specify implementation patterns, and it does not claim that governance and authorship are performed by different humans. Implementations may use various interfaces, tools, and workflows for governance and authorship actions; the commitment is to the action-level distinction being operationally satisfied, not to specific interface designs. The same human may perform both at different times — the distinction is at the action level, not the actor level — so a specialist authoring a rule and later exercising the override right has performed two distinct actions in two distinct categories.

It does not claim that governance produces no new substrate content. Modify and override produce substrate writes carrying provenance, and those writes are themselves substrate content. The distinction is at the action-type level: modify and override are governance actions because they alter existing content under authority, not because their effect produces no new bytes.

## 6. What the distinction is NOT

Four adjacent action distinctions are commonly conflated with governance-vs-authorship. Each is a real distinction in some operational vocabulary; none captures the architectural content of the present distinction.

**Not read-vs-write.** Read-vs-write is the operational distinction implementations most often reach for when they need a coarse action category. Modify and override are write actions but governance; schema authorship, rule authorship, and cell construction are write actions but authorship. The governance-vs-authorship distinction is orthogonal to read-vs-write.

**Not consumption-vs-production.** Consumption-vs-production is conceptually similar but loses the authority dimension. Modify and override produce new substrate writes, but they are governance because they exercise authority over existing content. Treating them as "production" obscures the architectural fact that they are exercises of authority, not introductions of new architectural elements.

**Not edit-vs-create.** Edit-vs-create is closer but too narrow. Edit captures modify; create captures the four authorship roles; but override is neither edit nor create in the conventional sense — it is replacement-by-authority, with the architectural property that no justification is required to the system. The governance-vs-authorship distinction includes override as governance, which edit-vs-create does not capture cleanly.

**Not reviewer-vs-author.** Reviewer-vs-author is adjacent but loses the architectural specificity. Inspect is closer to "review," but modify and override are not "review" actions. The reviewer-vs-author framing typically positions the reviewer as having less authority than the author; the governance-vs-authorship distinction reverses this — governance is the architectural authority, exercisable over substrate content authored by anyone, including by specialists.

## 7. Why the distinction is load-bearing for downstream commitments

The distinction is load-bearing for several CKS commitments. The integrating non-specialist-governance commitment depends on a precise specification of what is architecturally accessible and what is not. The four authorship roles depend on authorship being a distinct action category from governance. The three architectural commitments — tool-agnosticism, authority-not-labor, and linear-cost — produce the accessibility property over governance specifically, and conflating governance with authorship would either expand them into authorship territory the source paper does not commit to or contract them into a subset the source paper rules out. The labor allocation framework's labor-vs-authority distinction operates at the labor-mode level while the present distinction operates at the action level; the two compose to give the full architectural decomposition. The human-governed commitment's three rights are governance actions in the present distinction's sense, and the present distinction is what keeps the rights from drifting into an authorship commitment the source paper does not make.

## 8. Failure modes

Eight failure modes violate the distinction. The closing observation collects them under the two patterns that account for most commercial drift.

**(a) Treating modify or override as authorship.** The implementation requires authorship expertise (schema design, rule-authoring competence, cell-construction knowledge) to exercise modify or override. Non-specialists are blocked from exercising rights they architecturally hold under the human-governed commitment.

**(b) Treating inspect as authorship.** The implementation requires expertise to read substrate content — for instance, by encoding content in a representation only schema authors can interpret, or by gating direct read access behind tooling that requires authorship competence. The inspect right's accessibility fails not by direct prohibition but by representational opacity.

**(c) Treating authorship as governance.** The implementation claims that schema authorship, rule authorship, cell construction, or initial content authorship is architecturally accessible to non-specialists, over-claiming what the architecture commits to. Non-specialists are asked to perform authorship that exceeds their expertise, and the architectural commitment is criticized for failing a claim it never made.

**(d) Conflating rule-authoring's governance side with its authorship side.** The implementation either treats rule authoring as fully authorship (denying the authority context is itself accessible — for instance, by requiring specialist credentials to authorize rules even when the rule content is produced by others) or as fully governance (claiming non-specialists can author rule content directly, conflating the architectural authority with the rule-authoring expertise).

**(e) Mode-dependent governance.** The implementation treats governance differently depending on which labor mode produced the content — requiring more expertise to govern Mode 2 content than Mode 1, for instance, on the grounds that "interpreting LLM output requires AI literacy." Component (c) of section 4 fails; the labor-allocation framework's mode-independence-of-authority property is also violated.

**(f) Authorship-expertise uniformization.** The implementation treats all authorship as requiring the same uniform expertise — typically by adopting a single "platform engineer" or "AI architect" role expected to handle schema, rules, cells, and content. The four authorship roles are conflated, and the role-specificity that makes deployment-level role allocation meaningful is lost.

**(g) Over-claimed accessibility.** The implementation positions the architecture as enabling non-specialists to perform all substrate-related actions, including authorship. Deployments fail when authorship complexity emerges; the architectural commitment is criticized for failing an accessibility claim it never made.

**(h) Under-claimed accessibility.** The implementation treats governance as requiring specialist expertise, excluding non-specialists from governance roles. The bottom-up adoption property is foreclosed; deployments lose the benefits of non-specialist governance even though the architecture preserves them.

Of the eight modes, (a)–(d) are technical conflations at the action level, (e)–(f) violate the mode-independence and role-specificity components from section 4, and (g)–(h) are the meta-failures that account for most observed drift in commercial positioning of accessible AI architectures. Implementations drifting toward (g) typically reach for tooling additions to close the authorship gap — LLM-driven schema designers, rule synthesizers, automated cell builders — which may be useful as deployment choices but are not what non-specialist governance names. Implementations drifting toward (h) typically reach for governance gating to manage perceived risk — specialist-only review, approval-gated modify, audited override — which converts the architectural accessibility commitment into a procedural one and loses the property the architecture preserves.

## 9. Operational test

A system instantiates the governance-vs-authorship distinction in the architectural sense if and only if all of the following are true at all times during the substrate's existence:

1. Governance actions (inspect, modify, override) operate over existing substrate content, with the action's effect on the existing content rather than the introduction of new architectural elements.
2. Authorship actions (schema, rules, cells, initial content) produce new architectural elements that did not previously exist.
3. Governance is mode-independent: a non-specialist exercising any of the three rights does so the same way regardless of whether the content was produced in Mode 1, Mode 2, or Mode 3.
4. Authorship expertise is role-specific: the four authorship roles have distinct expertise requirements, and an implementation that treats them as requiring uniform expertise has lost the role-specificity component.
5. Rule authoring is recognized as having both a governance dimension (the authority context, architecturally accessible) and an authorship dimension (the production of new rule content, typically requiring rule-authoring expertise), with the architectural commitment applying to the governance dimension.
6. The distinction is at the action level, not the actor or content level: the same human may perform both governance and authorship at different times, and governance applies to substrate content authored by anyone — including by specialists.

A system that fails any of (1)–(6) does not instantiate the distinction in the architectural sense, even if its operational interfaces present separate "governance" and "authorship" surfaces.

## 10. Why naming the distinction as standalone matters

Implementations under pressure to deliver accessible AI architectures drift consistently toward the two patterns named at the close of section 8: over-claimed accessibility, in which authorship is positioned as architecturally accessible and deployments fail when authorship complexity emerges; and under-claimed accessibility, in which governance is treated as requiring authorship expertise and the bottom-up adoption property is foreclosed. The drift is steady because the action-level boundary between governance and authorship is operationally subtle — the same human may perform both, the actions occur in close sequence, and the architecturally consequential difference (whether the action operates over existing content or produces new architectural elements) is rhetorically harder to communicate than either extreme.

Naming the governance-vs-authorship distinction as a standalone architectural commitment gives downstream readers a precise specification of what action-level distinction the architecture commits to. Subsequent notes specialize the four authorship roles and the three architectural commitments that produce governance accessibility; together with the present distinction, they give the full decomposition of the non-specialist-governance commitment. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "governance" and "authorship" in the senses formalized here. Subsequent work that uses the terms differently is using different concepts, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion notes

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Non-Specialist Governance, Not Non-Specialist Authorship: What the Coordination Knowledge Substrate Pattern Makes Available to Whom.* 28 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *What Humans Own, What LLMs Do, What Stable Cells Automate: The Labor Allocation Framework in CKS.* 29 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Inspect Right as Standalone Architectural Commitment in the Coordination Knowledge Substrate Pattern.* 1 May 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Governance vs. Authorship: The Standalone Architectural Distinction Between Acting Over Substrate Content and Producing Substrate Content in the Coordination Knowledge Substrate Pattern.* 5 May 2026. ORCID: 0009-0004-8065-3235.
