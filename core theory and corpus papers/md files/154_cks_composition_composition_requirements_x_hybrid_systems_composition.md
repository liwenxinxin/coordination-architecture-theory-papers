# Selected, Not Defaulted: Human-Selective Composition Coherence as the Emergent Architectural Property When Composition Requirements Compose with Hybrid Systems Composition in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the architectural property that emerges when two of the source paper's foundational commitments — composition requirements (A1.13) and hybrid systems composition (A1.16) — compose: *human-selective composition coherence*, the pattern by which humans architecturally select which composition partners participate in a CKS deployment and through which of A1.16's three legitimate patterns each participates. With this note, the A1.13 cluster (A4.14–A4.18) closes: A1.13's five Requirements per A2.76–A2.80 are now operationalized through compositions with the foundational commitments most directly relevant to each.

## Abstract

Composition requirements (A1.13) names five constraints any multi-substrate composition must satisfy — including Requirement E per A2.80, *human-selective composition* — but does not specify the architectural mechanism by which selection occurs. Hybrid systems composition (A1.16) names three legitimate patterns for placing adjacent AI components relative to a CKS substrate (Pattern A consultation per A2.92, Pattern B derived view per A2.93, Pattern C separate concern per A2.94) and three composition anti-patterns per A2.95, but does not specify how a deployment chooses among them. Each commitment alone leaves the selection question unspecified; the composition specifies it. This note formalizes the emergent architectural property — *human-selective composition coherence* — as four operational components: humans select composition partners through orchestration-rule authoring per A2.04, the selection assigns each partner to one of A1.16's three patterns, A1.13's other Requirements per A2.76–A2.79 hold for the selected partners, and A2.95's three anti-patterns are excluded from selection by construction. Three sharpening properties operationalize the test. Vendor-determined, framework-default, and implementation-decided composition are canonical violations because each constitutes composition that occurs without human selection. The note closes the A1.13 composition cluster.

## 1. Why this composition pair needs a standalone formalization

A1.13 commits to five Requirements that any multi-substrate composition must satisfy. The fifth — Requirement E per A2.80 — is *human-selective composition*: authority over what gets composed remains human, the rules governing composition selection are human-authored, and the human's right to inspect, modify, and override those rules is preserved. The commitment is named at A1.13 but its operational realization is located elsewhere in the source paper: §4.5 places composition with adjacent AI components under the three patterns A1.16 names, and treats the choice among them as a deployment-level architectural decision.

A1.16, in turn, commits to three legitimate composition patterns and three composition anti-patterns per A2.95 (A3.21 ungoverned writer, A3.22 hidden bidirectional coupling, A3.23 adjacent component as substrate substitute). The patterns are positions; A1.16 specifies what each requires of the substrate–component boundary but not *how* a deployment selects which adjacent components participate or which pattern each occupies.

Each commitment points at the other for the part it does not specify. A1.13 names a Requirement whose realization is in A1.16's three patterns; A1.16 supplies three patterns whose selection is governed by A1.13's Requirement E and ultimately by A1.01's authority commitment realized at A2.04 (Moment 1, orchestration-rule authoring). The composition closes the loop. Without it explicitly named, deployment composition tends to be determined by whatever defaults exist in the surrounding tooling — none of which is governed by humans through architectural mechanism.

The strategic prior-art posture is consequential: as the term "AI composition governance" enters wider use, the composition formalized here is the source paper's prior-art answer. The formalization also closes the A1.13 cluster — A4.14, A4.15, A4.16, A4.17 having operationalized A1.13's other four Requirements through compositions with A1.04, A1.01, A1.07, and A1.10. With A4.18 in place, A1.13's five Requirements per A2.76–A2.80 are fully operationalized.

## 2. The emergent property as four operational components

The composition produces an architectural pattern with four jointly necessary components.

**Component 1 — Humans select composition partners through orchestration-rule authoring per A2.04.** Selection is not a deployment-time configuration choice that lives outside substrate; it is a governance moment in the source paper's sense. Humans author orchestration rules that specify which adjacent components are part of the deployment, why each is included, and what role each occupies. The selection rules live in substrate, are subject to A1.01's three rights (inspect, modify, override) per A2.04, and change only through the same governance moment.

**Component 2 — The selection assigns each partner to one of A1.16's three patterns.** For each adjacent component included, the orchestration rules specify the pattern under which it operates: Pattern A (cell consults the component during execution per A2.92), Pattern B (substrate content is projected into the component as a derived view per A2.93), or Pattern C (the component handles a separate concern that does not affect coordination state per A2.94). A component without a specified pattern is not a selected component; the architecture treats it as an A2.95 anti-pattern instance regardless of how the component is used in practice.

**Component 3 — A1.13's other Requirements per A2.76–A2.79 hold for selected partners.** Selection alone does not satisfy A1.13. Each selected partner must additionally preserve the four other Requirements at the composition boundary: per-substrate human governance per A2.76, conflict preservation across boundaries per A2.77, addressable provenance across boundaries per A2.78 (path retraceability extending through the partner), and AI-as-substrate-mediator at every layer per A2.79 (the partner does not gain substrate-write authority outside cell mediation). A partner that fails any of these has been selected into a position A1.13 does not support, and the deployment is not CKS-coherent regardless of how Components 1 and 2 are realized.

**Component 4 — A2.95's three composition anti-patterns are excluded from selection by construction.** Because selection assigns each partner to Pattern A, B, or C, the three anti-patterns A2.95 names — A3.21, A3.22, A3.23 — are excluded from the selection space. They are not "patterns the deployment chose not to use"; they are configurations that are *not patterns at all* in A1.16's frame, and a deployment that drifts into one has stopped operating under the composition. Naming them explicitly is what makes their exclusion operational rather than aspirational.

The four components together are what *human-selective composition coherence* names. Each is necessary; jointly they are sufficient.

## 3. What the composition forces beyond either commitment alone

The composition has architectural consequences neither A1.13 nor A1.16 yields independently.

It forces A2.80 from a *named requirement* into an *architecturally specified procedure*. A1.13 alone says human-selective composition must hold; the composition specifies that selection occurs through orchestration-rule authoring per A2.04 and assigns one of three patterns per partner. The selection mechanism becomes part of the architecture rather than a procedural promise.

It forces vendor recommendations and framework defaults out of the composition decision. A vendor's "compatibility framework," an agent framework's default Pattern A consultation against an embedded retrieval index, a "best-practice" composition embedded in a starter template — each is, under the composition, a *non-selected* composition. The architectural test is whether the partners and patterns appear in human-authored orchestration rules subject to A1.01's three rights; vendor lists and framework defaults that do not surface as substrate-resident rules under A2.04 fail this test by definition, regardless of how reasonable the recommendations are.

It excludes A2.95's anti-patterns from the selection space. A3.21, A3.22, and A3.23 are not options humans can select among A1.16's three patterns; they are configurations that arise when partners are admitted without selection — when Component 1 of §2 fails. Naming them explicitly preempts the practical drift in which a non-selected partner gradually acquires capabilities matching an anti-pattern's profile.

It makes composition itself governable. Because selection rules live in substrate per A2.04, the deployment's composition is subject to A1.01's three rights: humans can inspect which partners are present and under which patterns, modify the selection, and override at any time. Composition becomes a substrate-resident object rather than an environmental fact about the deployment.

## 4. Anti-patterns specifically violating the composition

Each of the following names a configuration in which Component 1 of §2 fails — partners are present in the deployment without being human-selected through A2.04 rule-authoring.

**Vendor-determined composition.** A vendor recommends, certifies, or ships a "compatibility framework" specifying which adjacent components a deployment uses, and the recommendations are followed without surfacing in substrate-resident orchestration rules. Composition is determined by the vendor; humans inherit the decision rather than authoring it.

**Framework-default composition.** A deployment framework selects Pattern A consultations as defaults — embedded retrieval indexes, default fine-tuned models, default vector stores — and the deployment proceeds without authoring orchestration rules that name those partners. The defaults function as composition decisions humans did not make.

**Implementation-decided composition.** Developers integrate adjacent components during implementation without converting the decisions into orchestration rules under A2.04. The composition is operational; it is not governed.

**A3.21 (ungoverned writer).** An adjacent component writes substrate state without orchestration-rule authorization, operating as an unnamed fourth composition pattern A1.16 does not support.

**A3.22 (hidden bidirectional coupling).** An adjacent component and the substrate update each other through automated processes that no human-authored rule governs. Neither direction passes through the substrate's orchestration-rule layer.

**A3.23 (adjacent component as substrate substitute).** A derived view (Pattern B) gradually accumulates content the substrate cannot regenerate, then becomes the surface participants reach for first, then the place new content is written. The drift is not a different selection of pattern; it is the absence of selection allowing the component to acquire substrate-equivalent role without authorization.

**"Compatibility-driven" or "best-practice" composition without governance.** Composition is shaped by which adjacent components are listed as compatible by tooling, marketplaces, or integration catalogs, or is adopted from an industry "reference architecture" that bundles components in a recommended configuration. The recommendations may be sound; if they are not authored as orchestration rules subject to A1.01's rights, they are not selected in the architecture's sense.

## 5. Operational decisions the composition forces

Five decisions follow directly and are observable in any CKS deployment satisfying the composition. Composition partners are listed in substrate-resident orchestration rules per A2.04, with the listing subject to A1.01's three rights at all times. Each listed partner has an associated pattern specification — Pattern A, B, or C — with the requirements of the chosen pattern (per A2.92, A2.93, or A2.94) named in the rule. The other A1.13 Requirements are verified per partner: A2.76 governance preservation at the partner's substrate boundary, A2.77 conflict preservation across the boundary, A2.78 path retraceability through the partner, A2.79 AI-as-mediator at the partner's layer. Composition changes — adding, removing, or repositioning a partner — are governance moments per A2.04, recorded in substrate with the same provenance metadata A1.07 commits to per A2.78. Composition state is auditable through substrate alone: a reader can determine, without consulting external configuration, which partners are present, under which patterns, and when each was selected, modified, or removed.

## 6. What the composition is NOT

The property is not equivalent to either commitment alone, nor to several adjacent constructs. It is not A1.13 alone (which names Requirement E without specifying a selection mechanism). It is not A1.16 alone (which specifies three patterns without specifying how humans select among them). It is not vendor-recommended composition: vendor compatibility lists and certified-partner directories do not constitute selection but recommendations humans may *select from* through A2.04 authoring. It is not framework-default composition: defaults provided by deployment frameworks become selected only when authored into orchestration rules. It is not implicit composition that is "obvious," "implied," or "assumed" given the deployment's tooling. It is not auto-discovery composition: a deployment that programmatically discovers adjacent components and integrates them through service registries, marketplace APIs, or runtime probing is performing composition the architecture does not authorize. Discovery may produce candidates; selection is what admits them, and selection is human.

## 7. Why this composition is load-bearing

It closes the A1.13 composition cluster. With A4.14 (mediator preservation per A2.79), A4.15 (governance preservation per A2.76), A4.16 (retraceability preservation per A2.77), A4.17 (determinism preservation per A2.78), and A4.18 (this note, human-selective composition coherence per A2.80), all five A1.13 Requirements are operationalized through compositions with the foundational commitments most directly relevant to each. A1.13 is now fully specified through Phase A4 composition pairs.

It ties A1.16's three patterns to A1.01's authority commitment. Without the composition, A1.16's patterns are descriptive — they name what positions are legitimate, but the architectural mechanism that places adjacent components into those positions is unspecified. The composition specifies that placement is governance per A2.04, which is A1.01's commitment realized as Moment 1.

It distinguishes CKS from systems where composition is determined externally (agent frameworks with default integrations, orchestration platforms with marketplaces, vendor stacks with bundled components), and it supports A1.05 (tool-agnosticism) at the composition layer: because partners are human-selected through substrate-resident rules, a deployment can move between hosts, vendors, and tooling without inheriting a vendor's composition decisions. The composition is portable because the selection record is portable, and the selection record is portable because it lives in substrate.

## 8. Operational test

A CKS deployment instantiates the human-selective composition coherence property if and only if all of the following hold at all times during the deployment's existence.

**Property e.1 — Composition rules are substrate-resident.** Every composition partner present in the deployment appears by name in a substrate-resident orchestration rule authored under A2.04, with the rule inspectable, modifiable, and overridable per A1.01 at all times. A partner whose presence is determined by deployment configuration outside substrate, by a vendor's compatibility framework, or by a deployment framework's defaults — and which does not appear in a substrate-resident rule — fails the property regardless of how the partner is used.

**Property e.2 — Each partner has a documented pattern specification.** Each partner under e.1 has, in the same substrate-resident rule, an explicit pattern specification: Pattern A (with the consulting cell named), Pattern B (with the derived view's regeneration source named), or Pattern C (with the separate concern named). A partner present without a pattern specification fails the property; the deployment is operating an unnamed composition position regardless of intent.

**Property e.3 — A1.13's other Requirements are verified for each selected partner.** For each partner under e.1 with a pattern under e.2, the deployment can demonstrate that A2.76 (per-substrate governance preserved), A2.77 (conflict preservation across the boundary), A2.78 (path retraceability through the partner), and A2.79 (AI-as-substrate-mediator at the partner's layer) hold at the partner's composition boundary. A partner under a specified pattern that fails any of these has been selected into a position A1.13 does not support; the selection itself is incoherent.

A deployment that fails any of e.1, e.2, or e.3 may be useful and may instantiate other valid design patterns; it is not a deployment in which human-selective composition coherence holds in the sense the source paper's commitments compose to require.

## 9. One-sentence test

A CKS deployment satisfies human-selective composition coherence if and only if every adjacent AI component present in the deployment appears by name in a substrate-resident orchestration rule that assigns it to Pattern A, B, or C and at which A1.13's other four Requirements per A2.76–A2.79 are verifiable.

## 10. Why naming this composition as a standalone property matters; closing the A1.13 cluster

The composition produces an emergent architectural property neither commitment yields alone, and the property is the operational closure of A2.80. A1.13's Requirement E is a commitment in search of a mechanism; A1.16's three patterns are mechanisms in search of a selection rule; the composition supplies the selection rule. Naming it as a standalone property — rather than as an interpretation of either parent — makes the architectural pattern citable, testable, and defensible without requiring readers to reconstruct it from two separate decompositions.

The note also closes the A1.13 cluster. The cluster's logic is operationalization: each of A1.13's five Requirements is most naturally specified through composition with the foundational commitment to which it is most directly tied. A4.14 operationalized Requirement D through composition with A1.04. A4.15 operationalized Requirement A through composition with A1.01. A4.16 operationalized Requirement C through composition with A1.07. A4.17 operationalized Requirement B through composition with A1.10. A4.18 operationalizes Requirement E through composition with A1.16. The cluster is now complete.

Subsequent Phase A4 notes move beyond the A1.13 cluster — to A1.14 three adjacencies compositions, A1.15 orchestration layer distinctions, and A1.16 hybrid systems composition operationalizations of Pattern A, B, and C separately (distinct from this note in that they specify the patterns themselves rather than the selection coherence).

The composition is the architecture's answer to the practical question deployments face: which AI components participate, in which positions, under whose authority. The answer the architecture supports — and the answer this note formalizes — is that participation is selected, position is specified, and authority is human, with the selection living in substrate as a governance moment per A2.04.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Selected, Not Defaulted: Human-Selective Composition Coherence as the Emergent Architectural Property When Composition Requirements Compose with Hybrid Systems Composition in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
