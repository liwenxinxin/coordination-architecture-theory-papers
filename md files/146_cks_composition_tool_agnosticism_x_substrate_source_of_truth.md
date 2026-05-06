# Composition Pair: Tool-Agnosticism × Substrate-as-Source-of-Truth — Vendor-Independent Authoritative Content as the Emergent Architectural Property

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 6 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the emergent architectural property produced when two CKS commitments — tool-agnosticism and substrate-as-source-of-truth — compose, so that downstream work can adopt or argue against the composition without ambiguity.

## Abstract

The CKS pattern names tool-agnosticism (§3.2, §7.1) and substrate-as-source-of-truth (§3.1, §11.3) as two of its architectural commitments. Each carries operational meaning on its own; the two also interact, and the interaction is itself an architectural property neither commitment yields independently. This note formalizes that property as **vendor-independent authoritative content**: the architectural pattern in which authoritative substrate content for the five coordination-state categories the source paper names — what was decided, by whom, under what authority, with what rationale, and what contradictions remain unresolved — survives vendor migration without changes to its authoritative status, because authority is determined by substrate architecture rather than by vendor-specific features. The note states the property in precise form, decomposes it into four operational components, distinguishes the composition from each commitment in isolation, identifies the anti-patterns that specifically violate the composition rather than only one of its parents, names the architectural decisions the composition forces, and provides an operational test sharpened by three sub-properties.

## 1. Why the composition pair needs to be formalized as a standalone derivation

The CKS pattern's tool-agnosticism commitment describes the substrate-host interface as three minimal requirements — persistent structured state, direct human read/write access, and LLM access to substrate content — and the pattern's substrate-as-source-of-truth commitment names the substrate as authoritative for coordination questions across five categories. Each commitment has been formalized as its own standalone derivation. The composition of the two — what arises when both hold simultaneously over the same substrate — is a distinct architectural object from either commitment alone.

Distinctness shows up most clearly when one of the two is satisfied while the other is not. Tool-agnosticism without source-of-truth produces a substrate whose host interface is portable but whose authoritative status is decoupled from the substrate itself: authority lives in vendor IAM, in vendor "verified state" features, in vendor-issued compliance certifications, or in adjacent vendor systems with their own trust models. The substrate may be migrated to a different host, but the answer to "what was decided, by what authority, under what rule" travels separately, and may not survive the migration at all. Source-of-truth without tool-agnosticism produces the inverse: the substrate is the authoritative answer to coordination questions, but the substrate is bound to a specific host whose architectural features supply the authoritative status. Switching the host reopens every authority question the substrate previously settled.

The composition is the architectural object that closes both gaps simultaneously. It is the property that lets a deployment answer "does authority survive vendor migration?" with "yes — authority is architectural, not vendor-architectural." Naming it as standalone matters because deployments routinely satisfy each parent commitment individually while failing the composition: tool-agnostic substrates whose authoritative status leaves with the vendor, and authoritative substrates whose host cannot be changed without rebuilding the authority story.

A4.10 follows A4.09 as the second of two composition pairs anchored on tool-agnosticism. A4.09 formalizes the composition with linear-cost scaling, which covers the *operational* dimension of vendor-portability. A4.10 (this note) covers the *authority* dimension. Together the two pairs cover how tool-agnosticism composes with the two foundational commitments most directly relevant to its operation: cost-scaling and authority. A deployment that satisfies one pair but not the other is vendor-portable in only one dimension.

## 2. The emergent property in four operational components

The composition produces vendor-independent authoritative content. Stated in operational form, the property has four components.

**(a) Authoritative content has vendor-independent representation.** Substrate content for each of the five categories the source paper names at §11.3 — what was decided, by whom, under what authority, with what rationale, what contradictions remain — is represented in a form whose authoritativeness does not depend on vendor-specific schemas, vendor-managed metadata, vendor-issued signatures, or vendor-controlled identifiers. The representation may be hosted in a vendor's environment, but its authoritative status is a property of how the substrate is structured, not of which vendor hosts it.

**(b) Authority is substrate-architectural, not vendor-architectural.** What makes substrate content authoritative is the architectural structure of the substrate — the human-governed authority over content and rules, the path-retraceable provenance of decisions, the first-class status of conflicts, the mediator role assigned to the LLM. None of these is supplied by a vendor feature. A vendor environment may provide auxiliary services that interoperate with substrate authority, but the authority itself is constituted by the architectural elements the substrate carries with it.

**(c) Vendor migration preserves authoritative status across all five categories.** When a substrate is moved between hosts that each satisfy tool-agnosticism's three minimal requirements, authoritative status is preserved for all five source-of-truth categories — what is the case, what is current, what is in conflict, what rules apply, and who has what authority. The migrated substrate answers the same coordination questions with the same authority on the destination host as it did on the source host, because the architectural elements that establish authority are part of the substrate, not the host.

**(d) Rules are vendor-independent authoritative content.** The orchestration rules that govern cell-level behavior — authoritative substrate content for the "what rules apply" category — are stored, addressed, and resolved as substrate content rather than as configuration in vendor-specific policy systems, vendor compliance frameworks, vendor IAM rule engines, or vendor "managed rule" services. Rule references travel with the content they govern; when the substrate moves, the rules move with it as the same kind of authoritative content the substrate was for the decisions they governed.

The four components are not independent restatements of the same idea. (a) is about *representation*; (b) is about *what makes authority hold*; (c) is about *what migration preserves*; and (d) is about *one specific category*, called out separately because it is the category where vendor-supplied mechanisms most aggressively offer themselves as substitutes — vendor policy engines, managed rule services, and compliance frameworks each compete to be the authoritative location for orchestration rules, and the composition specifically forbids accepting any of them.

## 3. What the composition forces beyond either commitment alone

Tool-agnosticism alone permits an authoritative store whose authority is established by vendor features. The substrate's host interface is the three minimal requirements, and migration between hosts is architecturally permitted; nothing in tool-agnosticism alone forbids the deployment from establishing authoritative status through vendor IAM, vendor-issued certificates, or vendor "trusted state" services. Such a deployment is tool-agnostic in the sense that its functional API is portable; it is not vendor-independent in the authoritative sense, because moving the substrate to a different host requires reconstituting authority through whatever the destination host happens to offer.

Substrate-as-source-of-truth alone permits an authoritative substrate whose authority is established by vendor mechanisms. The substrate is the source of truth for the five coordination categories; nothing in source-of-truth alone forbids the substrate's authoritative status from being supplied by a specific host's features. Such a deployment is authoritative in the source-of-truth sense; it is not vendor-portable in the authoritative sense, because the host that supplies the authority is also what binds the deployment to that host.

The composition forbids both. It requires that the architectural elements which establish authority are themselves part of the substrate — they are not host-supplied — and it requires that the host interface remain the three minimal requirements regardless of which host is in use. Vendor environments may be used; they may not be relied on as the source of authoritative status. The composition forces specific architectural decisions at deployment time:

- *Authoritative representation independent of vendor schema.* Substrate content carries the structural elements that make it authoritative — provenance, rule references, authority assignments, conflict status — within the substrate's own representation, not as side-cars maintained by the host.
- *Substrate-architectural authority rather than vendor-feature authority.* The authority story for the deployment is told in terms of the substrate's architectural commitments, not in terms of host capabilities. A deployment whose authority story requires the host's name to be told is not vendor-independent in the composition's sense.
- *Migration verification of authority preservation.* For the composition to hold operationally, vendor migrations must be verifiable as preserving authoritative status across all five categories — not only the substrate's content survives migration, but the authority of that content survives as well.
- *Vendor-independent rule storage.* Rules governing cell-level behavior are substrate content. The composition forbids the deployment from delegating rule storage or rule evaluation to vendor systems whose features supply the rule's authoritative status.
- *All five categories vendor-independent.* The composition does not selectively preserve some categories of authoritative state and surrender others. All five travel together with the substrate.

## 4. What the composition is NOT

Three readings of the composition that overstate or misstate the commitment.

**Not "tool-agnostic with vendor-supplied authority."** A deployment whose substrate is hostable on multiple vendors but whose authority is supplied by whichever vendor happens to be in use is not vendor-independent in the composition's sense. Authority that is reconstituted at each migration is not preserved by migration; the composition requires preservation, not reconstitution.

**Not "authoritative with vendor lock-in."** A deployment whose substrate is the source of truth for coordination questions but whose host cannot be changed without rebuilding the authority story is not the composition either. Authority that does not survive migration is host-architectural authority that happens to live in a substrate, not architectural authority in the composition's sense.

**Not "authority transfer during migration."** The composition does not say that vendor migration is accompanied by an authority-transfer ritual that re-establishes authoritative status on the destination host. It says authoritative status is preserved by virtue of being substrate-architectural; nothing about the vendor change is supposed to alter the authority story at all.

**Not "vendor trust features as authority."** A vendor's "trusted state," "verified ledger," or "attested storage" feature may be useful auxiliary infrastructure; it is not what makes substrate content authoritative under the composition. Substituting any of these for substrate-architectural authority binds authority to the vendor providing the feature.

## 5. Anti-patterns that specifically violate the composition

Several anti-patterns formalized elsewhere in the derivation series violate one or both parent commitments. The composition is violated more sharply by patterns that simultaneously deny tool-agnosticism's host-interface portability *and* substrate-as-source-of-truth's authoritative status, by lodging authoritative content inside a vendor-specific architecture from which neither portability nor source-of-truth recovers.

**Adjacent component as substrate substitute — canonical severe violation.** When an adjacent component (a workflow engine, an agent framework, a specialized governance runtime) is treated as the substrate, authoritative coordination state lives inside vendor-specific architecture. The component's API gates direct human access (failing tool-agnosticism's second requirement) and the component's internal model establishes what counts as authoritative (failing source-of-truth's substrate-architectural authority). Migration to a different vendor requires re-architecting authority itself. Both parents fail simultaneously through the same mechanism.

**Pure context-window memory as substrate.** Authoritative coordination state held in an LLM's context window is bound to the LLM vendor's architecture. Authority is supplied by what the model does with the context, which is a vendor-specific behavior, and the substrate's host interface is the model itself. Migration is not even definable, because there is no substrate to migrate that exists outside the vendor's runtime.

**Black-box agent memory as substrate.** Authoritative coordination state held inside a proprietary agent memory framework is bound to the framework's internal model. Authority is supplied by the framework's mechanisms, which are vendor-specific and opaque, and the substrate's content is not portable as inspectable state.

**LLM-as-source-of-truth.** Treating LLM output as authoritative for coordination questions makes authoritative status a property of the LLM vendor's model, training, and inference behavior. Different vendors produce different "authoritative" answers to the same input. Source-of-truth is bound to a specific vendor; the composition fails because the vendor independence the architecture commits to disappears.

**Agent memory, LLM context, and external tool state treated as authoritative.** Each violates source-of-truth in a different specific way; each also violates the composition by lodging authoritative status in vendor-specific architecture. Agent memory binds it to the agent framework vendor; LLM context binds it to the LLM vendor; external tool state binds it to whatever vendor owns the tool. In each, vendor migration breaks the authority story.

**Vendor-IAM-as-authority-mechanism.** Treating a vendor's identity-and-access-management system as the architectural answer to "who has what authority" makes authority a vendor feature. The substrate may host content describing authority; if the operative authority is what vendor IAM enforces, the substrate is not the source of truth for authority and the composition fails.

**Vendor-compliance-certification-as-authority.** Treating a vendor's compliance certification as the basis for substrate content's authoritative status — "this content is authoritative because the host is certified" — makes authoritative status a property of the host rather than of the substrate. Migration to a non-certified host or to a different certifier reopens the authority question that the substrate was supposed to have settled.

**Vendor-managed-rule-storage.** Storing rules in vendor-specific policy systems, rule engines, or "managed rule" services places authoritative substrate content under vendor architecture. When the vendor changes, the rules' authoritative status changes with the vendor; the composition fails because rules are precisely the category most exposed to this substitution.

In each anti-pattern the operational signature is the same: the substrate's authoritative status cannot be told without naming the vendor that supplies it.

## 6. Why the composition is load-bearing

The composition is what underwrites several downstream architectural claims that the CKS pattern rests on.

It enables true vendor-portability — both operationally (per the cost-scaling pair) and authoritatively (per this note). Vendor-portability that loses the authority story at migration time is vendor-portability of the substrate's bytes only, not of its meaning.

It supports AI-mediated authority preservation across vendors. The mediator role assigned to the LLM is exercisable across vendors precisely because authority is not a vendor property; the mediator changes (different LLM vendor) without changing what is authoritative.

It supports governance against authority across vendors. The three rights humans hold over substrate content are exercisable on whichever host the substrate is currently on, because the rights and the authoritative content they apply to are both substrate-architectural. A deployment in which governance is exercised through vendor-specific gates is not governance in the architecture's sense; it is delegation of governance to the vendor.

It distinguishes CKS from vendor-locked-authority architectures. A pattern that locates authority in vendor architecture may be operationally equivalent in many respects, but it cannot make the architectural claim that authority is vendor-portable. CKS, under the composition, can.

## 7. Operational test

A deployment instantiates the composition if and only if all of the following are true at all times during the substrate's existence.

1. Authoritative substrate content for each of the five source-of-truth categories is represented in a form whose authoritative status does not depend on vendor-specific schemas, vendor-issued metadata, vendor-supplied signatures, or vendor-controlled identifiers.
2. The architectural elements that establish authoritative status — human-governance rights, provenance metadata, conflict status, mediator-role assignment — are part of the substrate's own representation and travel with the substrate across hosts.
3. Orchestration rules are substrate content, not vendor-system configuration; rule references travel with the content they govern.
4. Vendor migration between hosts that each satisfy tool-agnosticism's three minimal requirements preserves authoritative status across all five source-of-truth categories without re-establishment, re-attestation, or transfer ritual.
5. The deployment's authority story can be told without naming any specific vendor as the source of authoritative status.

The test is sharpened by three sub-properties.

**(e.1) Vendor-migration-authority-preservation.** Moving the substrate from one host satisfying tool-agnosticism's requirements to another preserves authoritative status across all five categories. Verifiable by re-asking the same coordination questions on the destination host and confirming the answers' authoritative status is unchanged — not only do the same answers come back, they come back as authoritative for the same architectural reasons.

**(e.2) Substrate-architectural-authority.** The authority story for the deployment is told entirely in terms of substrate-architectural elements — governance rights, provenance, conflict status, mediator role — without reference to host-supplied features. Verifiable by drafting the authority story in plain prose and checking whether removing every vendor-specific reference leaves it intact. If the story collapses without the vendor's name, the property does not hold.

**(e.3) Vendor-feature-independence.** The deployment uses no vendor feature as the source of authoritative status. Vendor features may be used as auxiliary services (audit logs, observability, redundancy, performance) but not as the basis for authority. Verifiable by enumerating the vendor features the deployment uses and confirming that none is on the authority path.

A deployment that fails any of (1)–(5) or any of (e.1)–(e.3) may be a useful deployment, may be tool-agnostic in some weaker sense, and may be authoritative in some weaker sense, but does not instantiate the composition as the architecture defines it.

**One-sentence test.** A deployment instantiates the composition if and only if the question "who or what makes this content authoritative?" can be answered without naming any vendor.

## Conclusion

Tool-agnosticism and substrate-as-source-of-truth are each defensible on their own; deployments often satisfy one without the other, and deployments often claim to satisfy both while failing the composition. Naming the composition gives the architectural property a name and an operational test, which is what allows a deployment to be assessed for whether it actually has the property rather than only its parents. The property — vendor-independent authoritative content — is what makes a CKS deployment vendor-portable in the dimension that matters most when the question being asked is whether what was decided survives a vendor change.

A4.09 formalizes the composition of tool-agnosticism with linear-cost scaling; A4.10 (this note) formalizes the composition of tool-agnosticism with substrate-as-source-of-truth. Together the two complete the pair-set anchored on tool-agnosticism — they cover how the substrate-host interface composes with the two foundational commitments most directly relevant to its operation. Subsequent Phase A4 notes formalize approximately twenty additional architecturally significant pairs, each naming the architectural property the pair produces. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should treat vendor-independent authoritative content as the load-bearing emergent property it is, and should name where authoritative status actually sits in any system claiming to instantiate the pattern.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Composition Pair: Tool-Agnosticism × Substrate-as-Source-of-Truth — Vendor-Independent Authoritative Content as the Emergent Architectural Property.* 6 May 2026. ORCID: 0009-0004-8065-3235.
