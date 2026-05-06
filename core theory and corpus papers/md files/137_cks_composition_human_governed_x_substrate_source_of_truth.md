# Composition Pair: Human-Governed × Substrate-as-Source-of-Truth — The Emergent Architectural Property of Inspectable Authoritative Coordination as the Canonical CKS Operational Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 6 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the emergent architectural property that arises when two of the source paper's foundational commitments — that the substrate is human-governed and that the substrate is the source of truth for coordination questions — compose, producing what §3.1 of the source paper identifies as the canonical operational pattern of CKS systems: humans govern by acting against authoritative content directly, rather than against proxies, summaries, abstractions, or external representations of authoritative content.

## Abstract

The Coordination Knowledge Substrate (CKS) pattern names sixteen foundational architectural commitments. Two of them — that the substrate is human-governed and that the substrate is the source of truth for coordination questions — are individually load-bearing and have been formalized as standalone in prior derivation notes. This note formalizes the emergent architectural property that arises when the two compose. The composition produces something neither commitment yields independently: humans govern *against authoritative content directly* — inspection rights operate against the source of truth, modifications change authoritative state, overrides change authoritative state without external arbitration, and orchestration rules authored under the rule-authoring governance moment are themselves substrate-resident authoritative content under the same authority architecture as every other category of substrate state. The composition forces architectural anchoring of governance: governance is not abstract policy authored against a system that interprets it, but concrete substrate-content interaction. The note states the four operational components of the emergent property, identifies the architectural decisions the composition forces beyond either commitment in isolation, distinguishes composition violations from individual-commitment violations — the canonical case being LLM-gatekeeping — and provides an operational test sharpened by three composition-specific properties: governance-against-authority, authority-with-affordances, and rule-as-authority.

## 1. Why the composition needs to be formalized as standalone

The CKS pattern's two most foundational commitments — that the substrate is human-governed (§2.1, §3.3) and that the substrate is the authoritative answer to coordination questions (§11.3) — have each been formalized as standalone in prior derivation notes. Each carries independent operational content; each has its own decomposition into specializations (the four governance rights and the architectural and temporal qualifiers on the human-governed side; the integrating frame and five categories of authoritative state on the source-of-truth side); each has its own anti-patterns; each is independently testable.

The single-commitment treatment leaves a class of properties architecturally underspecified. There is an emergent property — *what governance operates against* — that depends on both commitments simultaneously, that is observable only when they are composed, and that the source paper §3.1 identifies as the operational pattern distinguishing CKS from adjacent governance architectures. A deployment can satisfy the human-governed commitment individually (humans hold inspect, modify, override, and rule-authoring rights over *something*) and satisfy the source-of-truth commitment individually (some persistent substrate is authoritative for coordination questions) and still fail the property §3.1 names — because nothing in either commitment alone forces that the *something* humans govern is *the same thing* the system treats as authoritative.

The composition forces that identity. Humans must govern *against* the source of truth. Inspection rights operate *on* authoritative content. Modifications change *authoritative* state. Rules authored under the rule-authoring moment are *themselves* substrate-resident authoritative content. The four governance rights and the five authority categories must align, not run in parallel.

Naming this composition explicitly makes the canonical CKS operational pattern available for review at design time, rather than implicit in the joint reading of the two commitments. It also produces a distinct anti-pattern class — composition violations — separate from individual-commitment violations: deployments that look governable and look authoritative but in which governance and authority are addressed to different objects. The framing matters most where the bifurcation is invisible by default, as in the dominant 2024–2026 commercial pattern of AI systems with "human-in-the-loop" governance over LLM-mediated authoritative content.

## 2. The emergent architectural property, defined precisely

The composition produces an emergent architectural property — *inspectable authoritative coordination* — with four operational components.

**(a) Governance operations target authoritative content directly.** The four governance rights of the human-governed commitment (inspect, modify, override, rule-authoring) operate *on* authoritative content, not on proxies, dashboards, summaries, abstract policy documents, or external representations that describe it. The architectural pattern is that rights and authority are addressed to the same object.

**(b) Inspection rights operate against the source of truth.** When a human inspects substrate, what they see is what is authoritative; the deployment provides no inspection path that reads from a non-authoritative location and presents the result as authoritative. The pattern is *inspect-against-authority*.

**(c) Modifications change authoritative state.** When a human modifies substrate under the modify or override rights, the change is to authoritative state directly — not to a derived view that is later (or never) reconciled to authority, and not to an input to a process that may or may not produce an authoritative change. The pattern is *modify-authority*.

**(d) Rules are substrate-resident authoritative content.** Orchestration rules authored under the rule-authoring moment are themselves authoritative content under the source-of-truth's rule-authority category — not external configuration compiled into the system, and not policy documents an LLM interprets at runtime. The pattern is *rules-as-authority*.

The four components together define what *inspectable authoritative coordination* names. A deployment satisfying all four exhibits the canonical CKS operational pattern; a deployment failing any exhibits one of the composition-violation classes named in §4.

## 3. What the composition forces beyond either commitment in isolation

The composition forces architectural decisions that neither commitment alone forces. The human-governed commitment alone is satisfied by any architecture in which humans hold the four rights over *something*. None of the candidate "somethings" — a dashboard, a policy document, a configuration file, a derived view, an external representation — is necessarily authoritative for coordination questions. The source-of-truth commitment alone is satisfied by any architecture in which some persistent substrate is authoritative, regardless of whether humans can act against it. A vendor system whose state is "the source of truth" by configuration but whose governance is vendor-mediated satisfies the source-of-truth commitment; a database that is architecturally authoritative but operationally inaccessible to humans satisfies it. Each fails the composition.

The composition forces five decisions that neither alone forces. *Inspection cannot be against proxies:* where humans inspect must be where authority lives; an inspection path landing on a summary, dashboard, or derived view fails the composition even when the derived view is faithful at the moment of inspection. *Modifications cannot be of representations the system interprets:* modifications to a policy document that an LLM later interprets do not change authoritative state; they change input to a process that may or may not produce an authoritative change. *Source of truth cannot exist without governance affordances:* authoritative content must be reachable by the four rights; authority that is not human-governable through architectural mechanism (vendor-mediated, opaque, runtime-only, mediator-only) fails the composition. *Rules cannot be external compilation targets:* rules authored under the rule-authoring moment must be substrate-resident authoritative content; rules in external configuration files compiled into a runtime, in policy documents the LLM consumes, or in vendor-managed prompt scaffolds violate the composition even when authored by humans and correct in content. *Governance must be architecturally anchored:* governance operates at the architectural layer (against authoritative content), not at the policy layer (against rules that get applied elsewhere). The composition is what makes governance an architectural property rather than a procedural one.

These five forced decisions are operationally distinguishable from the individual commitments. They are what the standalone formalization of the composition contributes.

## 4. Anti-patterns that violate the composition specifically

The composition produces anti-patterns distinct from those that violate either commitment individually; distinguishing them is what allows architectural review to identify failures a single-commitment review would miss. The anti-pattern catalog of this derivation series treats each in detail; what matters here is the composition-specific framing.

**LLM-gatekeeping is the canonical composition violation.** Humans formally hold inspect rights and substrate is the source of truth — both individual commitments are satisfied — but the LLM is interposed between the human and substrate access. Inspection runs through LLM-filtered presentation; modifications are committed only after LLM-mediated translation; overrides require LLM cooperation. The composition fails because the human is not interacting with authoritative content directly; what the human inspects is what the LLM produces *from* authoritative content, not authoritative content itself.

**Authority-migration anti-patterns are composition violations through bifurcation.** When agent memory becomes authoritative for "what was decided," when LLM context becomes authoritative for the active state of an interaction, when hidden cell state holds coordination state between executions, when external tool state is treated as authoritative for coordination questions, or when caches are treated as the answer instead of as derived views — the deployment may have governance affordances on substrate, but authority has migrated outside what humans govern. The composition fails not because humans cannot govern but because what humans govern is not authoritative.

**Human-governed-commitment violations cascade into composition violations.** Vendor-revocable governance, scheduled-review-window governance, and workflow-approval-gated governance each fail the architectural-and-temporal qualifiers of the human-governed commitment individually; once that commitment fails, the composition has no foothold to be evaluated. These are composition violations as a downstream consequence rather than as the primary failure.

**Bifurcated governance and authority** is the general class — the deployment has both governance and authority but addresses them to different objects (humans govern policies the AI interprets, modify configuration while authority lives in vendor-managed state, or author rules in one system while authoritative content lives in another). *Governance through opaque proxies* and *source-of-truth without governance affordances* are the corresponding failure modes for components (a) and (b) of §2: the first targets governance operations at dashboards or summaries rather than authoritative content; the second leaves authoritative content architecturally unreachable by the four rights. Each is a composition violation that does not necessarily manifest as a single-commitment violation.

## 5. What the composition forces operationally, and what it is not

A deployment satisfies the composition by exhibiting specific architectural decisions across both the four governance rights and the five authority categories. Inspection must read substrate directly, in inspectable form, without LLM intermediation as a precondition; LLM tooling is permissible as adjacent assistance, not as a gate. Modifications and overrides must take effect as substrate state, not as input to an interpretation step, and must do so immediately and without architectural justification. Rule-authoring must produce substrate-resident rules under the same authority architecture as every other category. Each of the five authority categories — what was decided, decision provenance and rationale, active contradictions, orchestration rules, and authority assignments — must be reachable by the four rights. The architectural and temporal qualifiers of the human-governed commitment, and the source-of-truth-vs-mirror distinction of the source-of-truth commitment, each apply with respect to authoritative content: governance is a property of how the architecture is built, authoritative content remains permanently human-governable through the architectural mechanism, and humans govern source-of-truth rather than mirrors that happen to be faithful at the moment of operation.

Four adjacent architectural patterns are commonly conflated with the composition; each is a real and reasonable commitment in some other architecture, and each is weaker than the composition along a specific axis. *Not human-governance-of-anything:* the human-governed commitment alone is satisfied by holding the four rights over some object; the composition requires the object to be authoritative. *Not source-of-truth-with-vendor-governance:* the source-of-truth commitment alone is satisfied by an authoritative substrate; the composition requires that authority be reachable by human governance through architectural mechanism. *Not governance-of-AI-system:* architectures in which humans govern an AI system through training, fine-tuning, prompt engineering, or vendor configuration — without architectural governance of the authoritative content the AI operates on — are weaker than the composition. *Not policy-based AI control:* architectures in which humans author policies that an AI interprets and applies require rules-as-input-to-interpretation rather than rules-as-authority. The distinction between architectural anchoring (the composition) and procedural anchoring (the four adjacent patterns) is the load-bearing one.

## 6. Operational test

A deployment satisfies the composition if and only if all of the following are true at all times during its existence.

1. Governance operations exercised under the four governance rights target authoritative content directly — not proxies, dashboards, summaries, derived views, or external representations.
2. Inspection rights operate against authoritative content across all five categories of source-of-truth (what was decided, provenance and rationale, active contradictions, orchestration rules and authority assignments).
3. Modifications and overrides change authoritative state directly, not by request to a process that may or may not produce an authoritative change.
4. Rules authored under the rule-authoring moment are substrate-resident authoritative content under the rule-authority category.
5. The architectural property of governance, the temporal property, and the source-of-truth-vs-mirror distinction are each satisfied with respect to authoritative content.

Three sharpening properties are operationally useful at deployment review.

**Governance-against-authority test.** Trace where governance interactions land. If they land on derived views, dashboards, summaries, policy documents the LLM interprets, or external representations rather than on authoritative content directly, the composition fails — even when both individual commitments are satisfied.

**Authority-with-affordances test.** Trace what governance affordances are available on authoritative content. If authoritative content cannot be inspected, modified, overridden, or governed by human-authored rules through architectural mechanism, the composition fails — even when some other object can be governed.

**Rule-as-authority test.** Trace where rules live. If rules live in external configuration compiled into the runtime, in policy documents the LLM interprets, in vendor-managed prompt scaffolds, or in any location other than substrate-resident authoritative content, the composition fails at the rule-authoring component — even when the other three components hold.

A deployment that satisfies (1)–(5) and the three sharpening tests satisfies the composition. A deployment that fails any may be useful, may satisfy the individual commitments, may be governed in some other sense; it does not satisfy the canonical CKS operational pattern.

The one-sentence test: if a deployment's governance operations under the four rights target authoritative content directly across the five source-of-truth categories, with rules authored under the rule-authoring moment as substrate-resident authoritative content (rules-as-authority, not rules-as-input-to-interpretation), and the deployment architecture forces direct interaction with source-of-truth rather than through proxies, summaries, or external representations, the deployment satisfies the composition.

## 7. Conclusion

The human-governed × source-of-truth composition is what makes a CKS deployment architecturally distinctive from adjacent governance architectures. Without the composition, the two foundational commitments produce a deployment that is governable in some sense and authoritative in some sense but in which what is governed and what is authoritative are not necessarily the same object. The composition forces them to be the same object. Humans govern authoritative content directly; the four governance rights operate against the five authority categories; rules authored under governance are themselves authoritative content under the same architecture.

This is the canonical CKS operational pattern §3.1 of the source paper names. It is the property that distinguishes CKS architecturally from policy-based AI control, from governance-of-AI-system architectures, from source-of-truth-without-governance-affordances architectures, and from bifurcated governance-and-authority architectures. It is what LLM-gatekeeping specifically violates and what authority-migration anti-patterns specifically violate. Naming it explicitly, and providing a sharpened operational test for it, makes the architectural choice visible at design time and at deployment review — rather than at the moment a deployment that looks governable and looks authoritative is asked a coordination question its bifurcated structure cannot answer correctly.

Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should treat the human-governed × source-of-truth composition as the canonical operational pattern, and should name where the bifurcation lies in any system claiming to instantiate the pattern that does not satisfy it. Subsequent notes in this derivation series will formalize additional architecturally significant composition pairs from the C(16,2) possible compositions of the sixteen foundational commitments — each formalizing an emergent architectural property neither constituent commitment yields independently.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Composition Pair: Human-Governed × Substrate-as-Source-of-Truth — The Emergent Architectural Property of Inspectable Authoritative Coordination as the Canonical CKS Operational Pattern.* 6 May 2026. ORCID: 0009-0004-8065-3235.
