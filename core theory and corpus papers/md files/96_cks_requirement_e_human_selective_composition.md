# Requirement E — Human-Selective Composition: Standalone Treatment of How Humans Choose What Composes in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the standalone architectural content of Requirement E — human-selective composition — as one of the five composition requirements committed to in the source paper at §13 and decomposed across the prior derivation notes A2.75 through A2.79.

## Abstract

The CKS source paper commits to five composition requirements that any multi-substrate or hybrid-systems composition must satisfy to remain CKS-coherent (§13). The integrating frame has been formalized as a derivation note (A2.75); the first four — per-substrate human governance preservation (A2.76), conflict preservation across boundaries (A2.77), addressable provenance across boundaries (A2.78), and AI-as-mediator at every layer (A2.79) — have each been formalized as standalone specifications. This note completes the decomposition by formalizing the fifth requirement — Requirement E, human-selective composition — with independent architectural content. The commitment is that humans with authority over a CKS substrate choose whether and how the substrate composes with another system, and that composition decisions are governance moments rather than automatic consequences of operational events. The note specifies four operational components, distinguishes Requirement E from four adjacent automatic-composition patterns, identifies its load-bearing role, enumerates ten failure modes, and supplies an operational test. With this specification in place, the composition-requirements decomposition (A2.75–A2.80) is fully formalized.

## 1. Why a standalone formalization is needed

The parent foundational note A1.13 commits the CKS pattern to five composition requirements. The integrating-frame note A2.75 named the requirements at the integrating level, including Requirement E as the commitment that humans hold authority over which compositions exist. A2.76 through A2.79 formalized Requirements A through D as having independent architectural content. This note treats Requirement E with the same standalone weight, with particular emphasis on the property that compositions are human governance decisions — moments at which humans exercise architectural authority — rather than automatic consequences of operational events.

Three motivations make the standalone treatment necessary. The first is operational: CKS substrates are commonly deployed into environments where mechanisms could form compositions without explicit human authorization — service-discovery infrastructure that detects and binds services automatically, deployment infrastructure that inherits default integrations, integration marketplaces that establish cross-system connections through "one-click" mechanics. In each case the architectural question is the same: whether the composition is a human governance decision or an automatic consequence. Requirement E is the commitment that the answer is the former.

The second is the strategic prior-art posture of the derivation-note series. Requirement E forecloses an entire family of architectures in which compositions form without human authority decisions; patentable derivations centered on automatic AI integration, vendor-mandated AI composition, infrastructure-driven AI orchestration, or marketplace-style AI composition occupy territory that this requirement, formalized publicly, identifies as outside CKS-coherence.

The third is the load-bearing relationship to A1.01 and to Requirement A per A2.76. A1.01 commits the pattern to humans holding authority over substrate content and orchestration rules through three rights, exercisable at any time. Requirement A preserves that authority *within each substrate during the composition's existence*. Requirement E preserves authority *over the composition decision itself*. Without Requirement E, A1.01 holds within each substrate but is circumvented at the meta-architectural level: substrates may compose with other systems without their humans authorizing the composition.

## 2. The Requirement E commitment, defined precisely

Requirement E commits the CKS pattern to four operational components. A composition that satisfies all four has Requirement E in the architectural sense.

**(a) Composition creation as human governance decision.** When CKS substrate S1 is composed with system S2, the creation of the composition is a governance moment in the sense formalized at A2.04. Humans with authority over S1 — as recorded in S1's authority structure per A2.47 (Category 5 source-of-truth: substrate authoritative for "who has what authority") — authorize the composition, and the authorization is recorded as substrate content with provenance: who authorized, when, under what authority, with what rationale. A composition that comes into being without an identifiable governance moment fails (a).

**(b) Composition modification as human governance decision.** Once a composition exists, changes to it are themselves governance decisions. Switching the composition pattern (between the patterns named at A1.16, for example), changing which cross-boundary references are carried, or narrowing or broadening the composition's scope each requires authorization by humans with appropriate authority per A2.47, recorded with provenance. Modifications that take effect because of operational events, configuration changes, or vendor updates without governance authorization fail (b). The architectural commitment is that the composition is held in place by human authority decisions, not by operational continuity.

**(c) Composition lifecycle events as human governance decisions.** Composition suspension and termination are also governance decisions. A *suspension* halts the composition operationally while preserving substrate state for later resumption; a *termination* ends the composition permanently. Each requires authorization by humans with appropriate composition authority per A2.47, recorded with provenance, including the authority basis and rationale. The temporal property at A2.07 carries through: humans can exercise these decisions at any time, not only at scheduled review points. Compositions whose lifecycle events occur as side effects of infrastructure events, deployment changes, or vendor decisions fail (c).

**(d) Composition authority recorded as substrate content per A2.47.** The authority structure governing compositions — which humans can authorize, modify, suspend, or terminate which compositions — is itself substrate content per A2.47, inspectable per A2.01, modifiable per A2.02, and overridable per A2.03 (each within higher-level authority). Composition authority is not implicit, external, or held in a vendor configuration outside the substrate; it is part of the substrate's source-of-truth architecture, exercisable through the same three rights that govern substrate content generally. An implementation that has composition authority decisions but does not record the authority structure as substrate content fails (d).

The four components are operationally distinct: (a) governs creation; (b) governs ongoing modification; (c) governs end-of-life; (d) governs the authority structure itself. Partial satisfaction is possible, in which case Requirement E is partially satisfied and the implementation is not CKS-coherent at composition.

## 3. What Requirement E does NOT claim

The following are real and reasonable design choices that Requirement E does not foreclose.

**Not a commitment to manual implementation.** Once a composition is humanly authorized, the operational implementation may be automated. Service connections may be established programmatically; cross-boundary references may be created automatically per Requirement C as formalized at A2.78; conflict-detection may operate automatically per Requirement B as formalized at A2.77. The architectural commitment is to the composition *decision* being human-governed; the operational *mechanics* may use automation that the human authority enabled.

**Not per-operation human approval inside the composition.** Once authorized, operations within the composition's scope — cell executions, writes against composed views, conflict-detection cycles — operate under that authorization without per-operation governance moments. The commitment is to the composition decision and its lifecycle events, not to decision-by-decision approval of every operation.

**Not foreclosure of deployment-level decision tooling.** Implementations are free to provide composition dashboards, decision wizards, validation tooling, or comparison views. The commitment is that the underlying decision is human-governed; ergonomic tooling is admissible.

**Not a specification of decision-making patterns.** Implementations may use any combination of mechanisms to capture composition decisions — dedicated substrate entries, multi-party authorization workflows, validation rules. The commitment is to the four components of section 2; specific implementations are deployment choices.

**Not a requirement that all compositions involve the same humans.** Different compositions may involve different humans, depending on the substrate's authority structure per A2.47. The commitment is that the *appropriate* humans, as recorded in the authority structure, authorize each composition.

**Not a foreclosure of organizational composition policies.** Organizations may have policies that influence which compositions are encouraged, required, or forbidden. Requirement E specifies that the architectural decision is human-governed within the substrate's authority structure; the policies operate as constraints on what humans choose to authorize, not as substitutes for the authorization.

## 4. What Requirement E is NOT

Four adjacent patterns are commonly conflated with Requirement E or treated as substitutes for it. Each is a real and frequently-observed pattern in enterprise integration; each permits compositions to occur without governance authorization; each is therefore distinguishable from Requirement E.

**Not automatic service discovery.** Service-discovery infrastructure (DNS-based registries, Consul, Eureka, and similar) detects services and enables binding. Discovery may inform humans of available compositions; the composition decision remains a governance moment. A pattern in which a CKS substrate automatically composes with discovered services — establishing the composition as a consequence of discovery — violates Requirement E regardless of operational convenience.

**Not infrastructure-driven composition.** Service-mesh configurations that enforce mandatory integrations, deployment templates that compose services automatically, and control-plane policies that establish bindings on deployment each compose systems based on infrastructure configuration. Once a composition is humanly authorized, infrastructure may operationalize it; the architectural objection is to compositions that come into being because of infrastructure configuration without an upstream human authorization.

**Not vendor-mandated integration.** A pattern in which a vendor requires specific integrations as preconditions for system functionality places the composition decision with the vendor. Requirement E is the commitment that the decision lies with the humans holding authority over the substrate per A2.47, not with the vendor relationship. Implementations that accept vendor-mandated compositions as composition decisions fail Requirement E even if the operational outcome would have been authorized had the question been asked.

**Not marketplace-style composition.** Marketplace patterns offering "one-click integration" violate Requirement E when a single user action through a marketplace establishes a composition by way of marketplace mechanics. Operational simplicity does not eliminate the architectural commitment; one-click composition is admissible only if the click is the human governance authorization, recorded with provenance per component (a), against the substrate's authority structure per component (d).

## 5. Why Requirement E is load-bearing

Requirement E is load-bearing for several CKS commitments, each of which fails specifically at composition decision points without it.

The composition-requirements specification per A1.13 and A2.75 is incomplete without Requirement E's standalone treatment. The human-governed commitment per A1.01 holds within each substrate but is circumvented at the meta-architectural level if compositions form without human authority over the composition itself; Requirement E closes that gap. Requirement A per A2.76 preserves authority within each substrate during composition existence; Requirement E preserves authority for the composition decision and its lifecycle events. The two compose: A is the within-composition authority commitment; E is the composition-decision authority commitment.

The three rights per A2.01–A2.03 extend to composition decisions through Requirement E — humans can inspect what compositions exist, modify composition parameters, and override lifecycle events. The temporal property per A2.07 carries through: composition decisions are exercisable at any time. The Category 5 source-of-truth commitment per A2.47 records composition authority as substrate content per component (d); without Requirement E, composition authority would sit outside the substrate, splitting the source of truth. The rule-authoring-as-governance commitment per A2.04 supplies the canonical governance-moment shape that composition creation, modification, and lifecycle events instantiate. The hybrid-systems composition framework per A1.16 supplies three composition patterns; Requirement E supplies the authority over which pattern is used, when, and with whom.

## 6. Failure modes that violate Requirement E

Each failure mode names a way an implementation can violate the requirement by permitting compositions to occur or change without human authority decisions.

**(a) Automatic service-discovery composition.** The implementation composes CKS substrates with discovered services without an upstream governance authorization. Component (a) of section 2 fails.

**(b) Infrastructure-mandated composition.** Deployment infrastructure composes systems based on configuration files or service-mesh policies without governance decisions. Component (a) fails structurally — the failure recurs at every deployment.

**(c) Vendor-required composition.** The implementation accepts vendor-mandated compositions as preconditions for vendor functionality. The composition is held in place by the vendor relationship rather than human authorization; components (a) and (d) fail.

**(d) Marketplace one-click composition without governance recording.** A one-click action establishes a composition without producing a recorded governance moment with provenance. Component (a) fails. (One-click composition that *is* the governance authorization, with provenance recorded, satisfies the requirement.)

**(e) Composition without provenance recording.** The implementation creates compositions through identifiable human actions but does not record provenance per A2.40. Component (a) fails on the recording obligation.

**(f) Composition modification without authorization.** Compositions can be modified operationally — changing patterns, scopes, or references — without re-authorization. Component (b) fails; the composition drifts under operational events.

**(g) Composition lifecycle events without authority.** Compositions are suspended or terminated by infrastructure events (deployment changes, vendor changes, configuration drift) without human authorization. Component (c) fails; lifecycle events occur as side effects rather than as governance decisions.

**(h) Composition authority not recorded as substrate content.** The authority structure is held outside the substrate (in a vendor configuration, an external policy file, or implicit conventions). Component (d) fails; the authority structure is not exercisable through the three rights and not part of the substrate's source of truth.

**(i) Implicit composition through service connection.** The implementation treats any service connection as composition — any time S1 reads from S2, a composition is considered to exist — without an explicit composition decision distinct from the connection. Component (a) fails on the requirement that composition is a decision, not an emergent property of operations.

**(j) Composition authority bypass through inheritance.** Compositions are created based on inherited authority from broader organizational policies — "all teams in this department compose with the enterprise data platform" — without per-substrate authorization. Components (a) and (d) are bypassed by inheritance from a higher-level policy. Organizational policies are admissible as constraints, not as substitutes for substrate-level authorization.

## 7. Operational test, and why naming Requirement E as standalone matters

A composition satisfies Requirement E if and only if all of the following are true at all times during the composition's existence:

1. Composition creation was a human governance decision per component (a) — humans with authority per A2.47 authorized the composition through a governance moment, with provenance recorded.
2. Composition modifications are human governance decisions per component (b) — modifications are authorized by humans with appropriate authority and recorded with provenance.
3. Composition lifecycle events (suspension, termination) are human governance decisions per component (c); humans can exercise these decisions at any time per A2.07.
4. Composition authority is recorded as substrate content per A2.47 per component (d); the authority structure is inspectable, modifiable, and overridable per the three rights at A2.01–A2.03.
5. No automatic-composition mechanism — service discovery, infrastructure-driven composition, vendor-mandated integration, or marketplace-style composition — operates without an upstream human governance authorization. Operational automation of composition implementation is enabled by human authority decisions, not a substitute for them.
6. Composition decisions are part of the substrate's governance lifecycle per A2.04 — composition creation, modification, and lifecycle events are governance moments comparable to rule authoring.

A composition that fails any of (1)–(6) does not satisfy Requirement E in the architectural sense, even when compositions appear to function operationally.

Implementations under pressure to integrate AI systems with enterprise infrastructure consistently drift toward automatic-composition patterns that bypass human authority for composition decisions. The drift is steady because automatic composition is operationally efficient (no governance overhead per composition), commercially familiar (enterprise integration typically automates compositions through configuration), and marketplace-driven (vendors offer "easy" compositions as a competitive feature). Drift produces systems where compositions occur without human authority, with downstream consequences that include authority circumvention at the meta-architectural level (humans lose authority over what their substrate composes with, even where Requirement A preserves authority within each substrate); governance erosion (the commitment to humans holding authority through governance moments fails specifically at composition decision points); source-of-truth fragmentation (the Category 5 source-of-truth per A2.47 fails because composition authority is held outside the substrate); and architectural-commitment failure (A1.01 fails at composition decision points even when it holds elsewhere).

Naming Requirement E as a standalone commitment — with the four operational components, the limitations, the four adjacent-pattern distinctions, the load-bearing connections, the ten failure modes, and the operational test above — gives downstream readers a precise specification of what human authority over composition decisions the CKS architecture requires. With this note complete, the composition-requirements decomposition is fully formalized: A1.13 committed the pattern to five requirements; A2.75 established the integrating frame; A2.76 through A2.79 specialized Requirements A, B, C, and D; this note specializes Requirement E. Together the six notes constitute the operational decomposition of A1.13. Subsequent work that proposes composition primitives, composition-management mechanisms, or hybrid-systems integration patterns can be evaluated against the decomposition by name; subsequent work that argues against any of the requirements should name the specific requirement and the specific component, so the disagreement is precise.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Requirement E — Human-Selective Composition: Standalone Treatment of How Humans Choose What Composes in CKS.* May 5, 2026. ORCID: 0009-0004-8065-3235.
