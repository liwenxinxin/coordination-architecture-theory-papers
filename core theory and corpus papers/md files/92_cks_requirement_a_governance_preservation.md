# Per-Substrate Human Governance Preservation: Requirement A as Standalone Architectural Commitment for Multi-Substrate Composition in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one of the five composition requirements named in the source paper's hybrid-systems composition framework — **Requirement A: per-substrate human governance preservation** — as a standalone architectural commitment with independent operational content, separable from the other four requirements (B through E) and from the integrating frame that names the requirements jointly.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern's hybrid-systems composition framework names five requirements that any composition of a CKS substrate with adjacent systems must satisfy. The first — Requirement A — commits to per-substrate human governance preservation: when a CKS substrate composes with another system, the human-governance structure of the composing substrate is preserved within that substrate across the composition's existence. A separate note formalizes the joint requirements at the integrating level. This note formalizes Requirement A as having independent architectural content that can be defended, implemented, and tested separately from Requirements B through E. The motivation is concrete: enterprise integration patterns consistently drift toward unified authority models that preserve operational simplicity at the cost of compromising per-substrate authority. The note states the requirement's four operational components, distinguishes it from four adjacent governance-preservation patterns commonly conflated with it (cross-system authentication, federated identity, shared governance, unified authority models), enumerates ten failure modes that violate it specifically, and provides an operational test for whether a given composition satisfies the requirement.

## 1. Why Requirement A needs to be formalized as standalone

The CKS pattern's hybrid-systems composition framework (A1.13) names five requirements that any composition must satisfy. The integrating-frame derivation note (A2.75) treats those requirements jointly, naming Requirement A at the level needed to support the joint treatment. The joint framing is correct as far as it goes, and this note does not contradict it. But Requirement A has independent architectural content that the joint framing leaves underspecified.

Three motivations make the standalone treatment necessary.

The first is concrete. CKS substrates compose with other systems in deployment contexts where authority preservation across the composition boundary is the load-bearing concern: a CKS substrate composing with another team's CKS substrate (each team retaining authority over its own substrate); a CKS substrate composing with an enterprise system (the substrate's humans retaining authority over the substrate while the enterprise system operates under its own authority); multiple CKS substrates within an organization composing for cross-domain coordination (each substrate retaining its own authority structure). Each scenario requires Requirement A specifically — per-substrate authority preservation across the composition — and treating it as one item in a five-item list does not articulate what each scenario architecturally needs.

The second is strategic. Enterprise integration patterns consistently drift toward unified authority models — one authority structure spanning the composing systems — because unification is operationally simpler to manage and commercially familiar. The drift is steady and silent. Naming Requirement A as a standalone architectural commitment, with its own operational content, its own failure modes, and its own test, gives implementers a principled vocabulary for resisting the drift and gives subsequent claims work a precise prior-art artifact for distinguishing CKS-coherent compositions from unified-authority alternatives.

The third is structural. Requirement A is the foundational composition requirement because it preserves the foundational architectural commitment — A1.01, "human-governed: authority not labor" — across composition boundaries. Without Requirement A formalized as standalone, the architectural condition that extends A1.01 to the composition layer is left underspecified, and composition becomes a mechanism for circumventing A1.01 specifically at the layer where the foundational commitment is most easily compromised.

## 2. The Requirement A commitment, defined precisely

In the CKS pattern, a composition satisfies **Requirement A** if and only if, when a CKS substrate S1 composes with a system S2, the human-governance structure of S1 is preserved within S1 across the composition's existence. The requirement has four operational components.

**(a) Each substrate's three rights preserved.** S1's humans retain the three rights — to inspect (A2.01), to modify (A2.02), and to override (A2.03) — over S1's substrate content and orchestration rules throughout the composition's existence. The rights are not diluted, shared, or transferred to S2's humans (if S2 is human-governed) or to S2 itself. If S2 is also a CKS substrate, S2's humans retain the analogous rights over S2's content as a distinct authority operating over a distinct substrate scope.

**(b) Each substrate's authority structure preserved.** S1's authority structure — the answer to "who has what authority over which substrate scopes within S1" — is preserved within S1. Per the Category 5 source-of-truth commitment (A2.47), the authority structure is itself substrate-resident content; the composition does not modify it, and authority-structure changes within S1 remain governed by S1's own authority structure rather than by composition events.

**(c) No cross-substrate authority transfer.** The composition does not transfer authority from S1's humans to S2's humans, or vice versa. When S1 and S2 compose, S2's humans (if S2 is human-governed) do not gain authority over S1's substrate content; S1's humans do not gain authority over S2's content. Information may flow across the composition boundary per the three composition patterns (A1.16); authority does not.

**(d) Temporal preservation across the composition's existence.** Per the temporal property of governance (A2.07), the three rights are exercisable at any time during the substrate's existence; Requirement A extends this commitment to the composition layer. At any moment during the composition's existence — including during composition lifecycle events such as creation, modification, suspension, and termination — S1's humans can exercise the three rights over S1's content. The rights are not suspended during composition transitions and are not gated on composition state.

The four components together define Requirement A architecturally. A composition that satisfies all four has Requirement A in the architectural sense; failing any one fails the requirement, even with the other three robustly satisfied.

## 3. What Requirement A does NOT claim

Stating precisely what Requirement A does not claim is what keeps the standalone framing from drifting into something stronger than the source paper supports.

**It does not claim that substrates cannot share information.** Composition by definition involves substrates exchanging information per the three composition patterns (A1.16): input, derived view, separate concern. The architectural commitment is that information exchange does not transfer authority. Substrates may share content, expose derived views, and operate as separate concerns over shared infrastructure, all while preserving per-substrate authority structures.

**It does not require composing systems to be human-governed.** Compositions with non-CKS systems are architecturally supported per A1.16. The commitment is that the CKS substrate's authority is preserved at its boundary with the composing system; the composing system may have any governance model — or no governance role at all, in the case of pure infrastructure — and the requirement holds at the CKS substrate's boundary regardless.

**It does not foreclose organizational governance frameworks that operate across substrates.** Organizations frequently maintain broader governance structures — enterprise-wide compliance policies, organizational authority hierarchies, cross-system approval frameworks. Requirement A specifies the architectural commitment per substrate, which can coexist with organizational frameworks operating at higher levels as long as authority within each substrate is preserved.

**It does not specify implementation patterns for authority preservation.** Implementations may use various mechanisms — separate authority records per substrate, authentication scoped to substrate, authority validation at composition boundaries, substrate-resident access-control content per A2.47. The architectural commitment is to the four operational components being satisfied; specific implementations are deployment choices.

**It does not require all compositions to use the same authority preservation pattern.** Different compositions may use different operational mechanisms; the architectural commitment is to per-substrate preservation, not to cross-composition consistency in how preservation is realized.

**It does not foreclose authority delegation within a substrate.** Within S1, authority may be delegated per S1's own authority structure (A2.47) — one human delegating inspection authority to another, role-based scoping of modification authority, similar within-substrate patterns. Requirement A operates at the cross-substrate level; within-substrate delegation continues to operate per the substrate's own architecture.

## 4. What Requirement A is NOT

Four adjacent governance-preservation patterns are commonly conflated with Requirement A. Each is a real and reasonable commitment in some other architecture; naming what Requirement A is not is what prevents the misreading.

**Not cross-system authentication.** Cross-system authentication — single sign-on, OAuth flows, federated identity providers — is the operational pattern of authenticating users across systems. Requirement A is at the architectural-authority level, not the authentication-mechanism level. A composition may use shared authentication while preserving per-substrate authority: a single sign-on system that authenticates the same human across S1 and S2 does not by itself transfer authority across the substrates. A composition may have separate authentication while violating per-substrate authority: separate logins to S1 and S2 do not by themselves preserve authority if the underlying authority structure is unified. The commitment is to authority, not authentication.

**Not federated identity.** Federated identity is the operational pattern of identity assertions traveling across systems. It may operationally support Requirement A by enabling each substrate to recognize the same human as the holder of authority within that substrate, but federated identity is not itself the architectural commitment. A composition with federated identity may still violate Requirement A if the federation is treated as authority federation; a composition without federated identity may still satisfy Requirement A if each substrate maintains its own authority structure.

**Not shared governance.** Shared governance describes operational patterns where multiple systems share governance decisions — joint review boards, multi-party approval workflows, cross-system policy committees. Requirement A specifies that each substrate's authority remains its own at the architectural level. Compositions may participate in organizational governance involving multiple parties without violating Requirement A, provided each substrate's architectural authority is preserved within the substrate. Shared governance at the organizational level is compatible with per-substrate authority at the architectural level; the two operate at different layers.

**Not unified authority models.** Unified authority models are architectural patterns where a single authority structure spans multiple systems. Requirement A is the negation of unification at the architectural level: each substrate has its own authority structure, and unification across substrates would violate per-substrate preservation. Implementations that unify authority across compositions — typically because unification is operationally simpler — violate Requirement A regardless of operational benefit. The architectural commitment is non-negotiable on this point.

## 5. Why Requirement A is load-bearing for downstream commitments

Requirement A is load-bearing for several CKS commitments.

**The integrating composition-requirements specification (A1.13, A2.75).** Requirement A is the foundational composition requirement; without per-substrate authority preservation, Requirements B through E operate within a compromised authority foundation.

**The human-governed commitment (A1.01).** A1.01 is the foundational architectural commitment of the pattern; Requirement A preserves it across composition boundaries. Without Requirement A, composition becomes a mechanism for circumventing A1.01 specifically at the layer where the foundational commitment is most readily compromised.

**The three rights (A2.01, A2.02, A2.03).** Each right is exercisable within a substrate; Requirement A specifies that the rights remain exercisable when the substrate composes with other systems.

**The temporal property of governance (A2.07).** The temporal commitment specifies that the three rights are exercisable at any time; Requirement A extends this commitment to the composition layer — the rights remain exercisable at any time during the composition's existence, including during lifecycle transitions.

**Guarantee E: substrate is source of truth (A2.61).** The guarantee specifies that the determinism contract operates substrate-internally; Requirement A specifies the parallel commitment for authority — authority operates substrate-internally even when compositions exist. The two commitments compose: Guarantee E preserves determinism per substrate; Requirement A preserves authority per substrate.

**Category 5 source-of-truth: who has what authority (A2.47).** The substrate is authoritative for "who has what authority over which substrate scopes"; Requirement A specifies that this authority structure is preserved per substrate across compositions, not migrated to the composing system or to a unified cross-composition store.

**Non-specialist governance (A1.11).** Non-specialists exercise governance over their substrate per A1.01; Requirement A specifies that this governance is preserved when their substrate composes with other systems. Without the requirement, non-specialists would lose governance authority at composition boundaries — exactly the failure mode the non-specialist commitment was designed to prevent.

## 6. Failure modes that violate Requirement A

A composition can fail Requirement A specifically, even when it satisfies Requirements B through E and broader governance commitments. Ten failure modes name the most common ways implementations transfer or compromise authority across composition boundaries.

**(a) Cross-substrate authority pooling.** The implementation pools authority across composing substrates: humans with authority over S1 and humans with authority over S2 are treated as a unified pool with shared rights over both substrates' content. Per-substrate preservation per component (a) of section 2 fails.

**(b) Authority transfer through composition.** When S1 composes with S2, the implementation shifts authority over S1's content to S2's humans, or vice versa. The architectural commitment to per-substrate authority is broken.

**(c) Composition-creating-shared-governance.** The implementation requires composition to create a shared governance structure spanning the composing substrates — composition is treated as the act of creating a unified authority. Per-substrate preservation per component (b) fails.

**(d) Authority compromise during composition lifecycle events.** The implementation suspends or compromises authority during composition creation, modification, or termination — humans cannot exercise the three rights during transition periods, or rights are gated on composition state. Temporal preservation per component (d) fails.

**(e) Implicit authority delegation through composition.** The implementation treats composition as implicit authority delegation — when S1 composes with S2, S1's humans are treated as having delegated authority to S2's humans by virtue of the composition itself, without human-governance-mediated delegation visible per S1's authority structure (A2.47).

**(f) External-authority-overrides through composition.** The implementation permits S2 to override S1's authority structure based on S2's policies — for instance, S2's compliance requirements override S1's authority decisions when the two compose. Cross-substrate authority transfer per component (c) fails.

**(g) Authentication-as-authority conflation.** The implementation conflates cross-system authentication with cross-system authority — assuming that because users authenticate across the composition, they hold authority across it. Per-substrate authority preservation fails operationally even if the authority structures are nominally separate.

**(h) Composition-without-authority-preservation-tooling.** The implementation supports composition operationally but does not preserve authority structure data across the composition; S1's authority structure is not enforced operationally at the composition boundary, relying on convention rather than architecture.

**(i) Cross-substrate-broadcast operations.** The implementation provides operations that broadcast across composing substrates without per-substrate authority checks — for instance, a "broadcast modify" that modifies content in both S1 and S2 with a single authorization, where the authorization is not validated against each substrate's authority structure independently. Per-substrate preservation per component (a) fails.

**(j) Composition-discovery-as-authority-acquisition.** The implementation treats composition discovery — service discovery, registry lookup, capability advertisement — as authority acquisition. Once S1 discovers S2, S1's humans are treated as having authority over S2's content; discovery becomes a mechanism for authority transfer.

A system exhibiting any of (a)–(j) does not satisfy Requirement A, and naming the failure precisely is what allows downstream remediation.

## 7. Operational test

A composition satisfies Requirement A if and only if all of the following are true at all times during the composition's existence:

1. Each composing substrate's three rights (A2.01–A2.03) are preserved within the substrate per component (a) of section 2.
2. Each composing substrate's authority structure (A2.47) is preserved within the substrate per component (b) of section 2.
3. Authority is not transferred across substrate boundaries in either direction per component (c) of section 2.
4. The temporal property (A2.07) holds across the composition's existence per component (d) of section 2; the three rights are exercisable at any moment.
5. Composition lifecycle events — creation, modification, suspension, termination — do not interrupt authority preservation; the requirement holds throughout.
6. Authority preservation is operationally enforced; the architectural commitment is not deployment-configurable. Deployments cannot disable per-substrate authority preservation while remaining architecturally compliant.

A composition that fails any of (1)–(6) does not satisfy Requirement A in the architectural sense, even if it operationally appears to preserve authority through deployment-level features.

## 8. Why naming Requirement A as standalone matters

Implementations under pressure to integrate AI systems with enterprise infrastructure consistently drift toward unified authority models that compromise per-substrate authority preservation. The drift is steady because unified authority is operationally simpler — one authority structure to manage rather than many — and commercially familiar — enterprise governance often unifies authority across systems by default. Implementations that drift away from Requirement A produce systems where composition becomes a mechanism for compromising the foundational human-governed commitment per A1.01. The downstream consequences manifest as authority leakage (humans lose authority over their substrate when composition occurs), governance erosion (composition shifts authority away from the original substrate's humans), source-of-truth fragmentation (the Category 5 commitment per A2.47 is compromised because authority structure is not preserved across composition), and architectural-commitment failure (the foundational A1.01 commitment fails at the layer where it is hardest to defend operationally and easiest to compromise silently).

Naming Requirement A as a standalone architectural commitment gives downstream readers a precise specification of what per-substrate authority preservation the architecture requires across compositions. Subsequent notes A2.77 through A2.80 specialize Requirements B through E; together with this specification, they close the decomposition of A1.13. Subsequent work that implements, extends, or argues against the CKS composition framework should use "Requirement A" in the sense formalized here; work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Per-Substrate Human Governance Preservation: Requirement A as Standalone Architectural Commitment for Multi-Substrate Composition in the Coordination Knowledge Substrate Pattern.* May 5, 2026. ORCID: 0009-0004-8065-3235.
