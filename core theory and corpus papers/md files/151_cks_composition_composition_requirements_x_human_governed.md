# Governance Does Not Weaken at Composition Boundaries: The Emergent Architectural Property When Composition Requirements and Human-Governed Compose in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the emergent architectural property that arises when two of the source paper's foundational commitments — composition requirements (A1.13) and human-governed (A1.01) — are taken together rather than separately, and to specify operationally what governance preservation across every composition partner requires in a multi-substrate CKS deployment.

## Abstract

The CKS composition-requirements commitment (A1.13) names per-substrate human governance preservation as Requirement A among five requirements multi-substrate compositions must satisfy. The human-governed commitment (A1.01) specifies four governance rights — inspect, modify, override, and rule authoring — that humans retain over substrate content and orchestration rules at all times. Each commitment is operationally meaningful in isolation; neither, alone, specifies what governance preservation across composition partners requires. A1.13 names Requirement A but does not enumerate which rights are preserved at each partner; A1.01 enumerates four rights but does not extend them across substrate boundaries. This note formalizes the property the two commitments produce together: *governance preservation across composition* — A1.01's four rights uniformly preserved at every substrate participating in a CKS composition, with no asymmetry between primary and secondary substrates, no vendor mechanisms substituted for architectural rights, and no federation pattern under which different substrates carry different governance models. The note articulates four operational components, identifies the architectural decisions the composition forces, enumerates anti-patterns it specifically rules out, and provides an operational test with three sharpening properties.

## 1. Why the composition pair needs to be formalized as standalone

The CKS source paper introduces composition at the cell level (§2.1: a cell is "a coordinated collection of substrates, possibly just one for a simple task, together with human-authored orchestration rules") and reiterates the requirement set at every claim that touches multi-substrate deployment (§3.1, §6.1, §11.3, §13.3). It also introduces the human-governed commitment as the architectural anchor for substrate authority (§3, §3.3): humans retain rights over substrate content and orchestration rules at all times.

The two commitments meet at every multi-substrate composition. A deployment that composes two or more substrates into a cell, or composes cells across an organizational coordination fabric, must satisfy both at every substrate. The composition is not optional; it is what multi-substrate CKS systems are.

The composition is also under-specified by the two commitments taken separately. A1.13 names Requirement A — per-substrate human governance preservation — but does not enumerate which affordances are preserved. A1.01 enumerates four rights at the substrate level (inspect per A2.01, modify per A2.02, override per A2.03, rule authoring per A2.04), with architectural and temporal qualifiers (A2.05, A2.07), but is silent on multi-substrate scope. Neither alone says what happens when a deployment grows to two substrates, ten, or a federated fabric.

The composition pair supplies what each lacks. From A1.13, it takes the cross-substrate scope: the requirement applies at every composition boundary, regardless of whether the boundary sits inside a cell or across cells. From A1.01, it takes the operational specification: the four rights, plus the architectural and temporal qualifiers, are what gets preserved. The result — *governance preservation across composition* — has consequential prior-art weight in territory currently labeled "AI orchestration governance," "multi-substrate AI compliance," and adjacent vendor framings of multi-system governance integration.

This note is the second in the A1.13 composition cluster, following A4.14 (A1.13 × A1.04, mediator preservation per A2.79). Subsequent notes will formalize A1.13's remaining requirements through their compositions: retraceability preservation (A2.77, A1.13 × A1.07), determinism preservation (A2.78, A1.13 × A1.10), and human-selective composition (A2.80, A1.13 × A1.16). The cluster decomposes A1.13's five-requirement structure into five composition-pair operationalizations, each grounded in the substrate-level commitment its requirement preserves.

## 2. The emergent property: four operational components

A multi-substrate CKS deployment satisfies *governance preservation across composition* if and only if the following four components hold at every composition partner at all times during the composition's existence.

**Component 1 — Each substrate has full A1.01 affordances.** Every substrate participating in the composition supports all four rights per A2.01–A2.04 over its content and orchestration rules. There are no substrates that support only inspection, no substrates that delegate modification authority elsewhere, no substrates whose rule-authoring authority is held externally, and no substrates whose override path runs through a workflow gate inside another substrate. Each substrate, as a unit, satisfies A1.01 in the same operational sense the source paper defends at single-substrate scope.

**Component 2 — Governance rights are uniform across composition partners.** The set of rights available at each partner is the same set. The composition does not produce a topology in which the primary substrate carries the four rights and secondary substrates carry only inspect and modify. Uniformity is not a strong-form claim about who exercises rights — labor remains allocable per A1.12 — but a claim about which rights are architecturally available. Wherever in the composition a human with appropriate authorization stands, the same four rights are available over the substrate they are inspecting.

**Component 3 — Composition partners cannot have weaker governance than the primary substrate.** The architecture forbids the deployment pattern in which one substrate (often the substrate the deployment was originally designed around) supports A1.01 in full while substrates added later support only a subset. The asymmetric pattern is the natural drift of a deployment that grows by accretion — adjacent components, vendor stores, federation with partner organizations — and the composition is what prevents the drift from rendering the deployment incoherent.

**Component 4 — Architectural and temporal qualifiers (A2.05, A2.07) are preserved across composition.** A1.01 commits not only to the four rights but to the architectural property that the rights are properties of the system's design rather than procedural promises (A2.05), and to the temporal property that the rights are exercisable at any time rather than at scheduled checkpoints (A2.07). The composition carries both qualifiers across every partner. A composition in which the primary substrate offers rights as architectural properties while secondary substrates offer them as procedural promises (subject to vendor revocation, runtime middleware, or workflow approval) violates A2.05. A composition in which the primary offers at-any-time rights while secondary substrates offer scheduled-window rights violates A2.07.

The four components together specify what A2.76 — Requirement A in A1.13's decomposition — operationally requires when grounded in A1.01's specific rights.

## 3. What the composition forces beyond either commitment alone

The composition forces four architectural decisions that neither A1.13 nor A1.01 forces independently.

*A2.76 must be grounded in A1.01's four rights.* A1.13 alone could in principle be operationalized through some other governance vocabulary — vendor-defined "admin authority," workflow-engine "approval scope," permissions-system "role-based access control." The composition with A1.01 forecloses those alternatives: Requirement A is grounded in inspect, modify, override, and rule authoring, not in any other vocabulary the host environment happens to provide.

*Vendor-managed governance must map to architectural rights.* When a partner is hosted in a vendor environment that provides its own governance mechanisms (admin features, sharing controls, audit dashboards, retention policies), those mechanisms must map onto A2.01–A2.04. Vendor mechanisms with no such mapping — for example, a "data steward" role that holds modify but not inspect, or an "approval workflow" that holds override only at scheduled checkpoints — fail the composition. The mapping is what makes vendor governance admissible.

*Primary/secondary asymmetry is prohibited.* The composition forbids any topology in which the primary substrate carries one set of affordances and secondary substrates carry a reduced set. The prohibition includes "read-only-secondary-substrate" patterns, "vendor-secondary-substrate" patterns (governed entirely through vendor mechanisms with no architectural-rights mapping), and "transient-secondary-substrate" patterns (whose affordances depend on the primary substrate's runtime state).

*Federated deployment requires uniform governance.* When a composition spans organizational or jurisdictional boundaries — a federated CKS fabric in which multiple substrates carry coordination state across a partnership — uniformity is the harder and more important constraint. Federation that results in each substrate carrying its own governance model (different administrators, different override authority, different rule-authoring authorities, different review windows) violates the composition. Federation may distribute administrative jurisdiction; it is not a license for governance heterogeneity. The architecture requires governance homogeneity even when administrative jurisdiction is heterogeneous. A documentary corollary follows: composition partners must be documented in terms that make their A1.01 affordances comparable, since a deployment cannot demonstrate uniformity it has not specified.

## 4. Anti-patterns the composition specifically rules out

Five anti-patterns violate the composition specifically. Each names a deployment shape that may satisfy A1.13 in name and A1.01 at the primary substrate while failing the emergent property.

*Asymmetric-governance-across-composition.* A1.01 holds at the primary substrate; secondary substrates have reduced affordances. Common shapes: a vendor-hosted "knowledge graph" with admin-only modify authority; a fine-tuned-model-as-substrate with no rule-authoring authority over the model's behavior (the model's "rules" are weights humans cannot author); an "archived substrate" tier where inspect is preserved but modify is gated by retention policy. Each fails Component 2.

*Vendor-managed-governance-not-mapping-to-A2.01–A2.04.* A partner's governance is provided through vendor mechanisms that do not map onto the architectural rights. Examples: "platform admin" roles that hold heterogeneous authority not separable into the four rights; "compliance dashboards" that grant inspect through a derived view rather than over substrate content; "configuration UIs" that control orchestration-rule-equivalent behavior but are not authored as orchestration rules in the A1.01 sense. Each fails Component 1 and the architectural-rights-mapping decision in §3.

*A3.01-compounded-across-composition.* A3.01 (vendor-revocable governance) is the canonical A1.01 violation at single-substrate scope: a vendor's policy reservation can in principle revoke governance affordances regardless of how rarely it is exercised. Across multiple vendor-hosted partners, A3.01 compounds — each is independently subject to its vendor's revocation reservation, and revocation at any one partner can render governance heterogeneous, breaking Component 2 even when no partner has actually been revoked.

*A3.02-and-A3.03-compounded-across-composition.* A3.02 (scheduled-review-window) and A3.03 (workflow-approval-gated) are the canonical A2.07 violations at single-substrate scope. Across composition, they compound when partners impose different windows or different gates. A composition in which the primary offers at-any-time governance while a secondary substrate offers Tuesday-morning-only governance fails Component 4 — not because either partner's window is unreasonable in isolation but because the composition has heterogeneous temporal availability.*Federated-substrate-with-distinct-governance.* A federated CKS fabric in which each substrate carries its own governance model — separate administrators, separate rule-authoring authorities, separate override paths — often arises when CKS substrates are deployed across organizations in a partnership and each retains autonomy over governance configuration. The composition forbids the pattern: federation may distribute administrative jurisdiction, but governance affordances must remain uniform.

These five name the patterns into which deployments most commonly drift when the composition is not specified explicitly.

## 5. What the composition is NOT

Three negative framings rule out adjacent commitments it might be conflated with.

*Not A1.13-alone.* A deployment that satisfies A1.13's Requirement A under some other governance vocabulary — vendor-defined authority, workflow-defined approval, role-based access control — does not satisfy the composition. The composition specifies that A2.76 is grounded in A2.01–A2.04; A1.13-alone does not.

*Not A1.01-alone.* A deployment that satisfies A1.01 at its primary substrate while leaving secondary substrates outside A1.01's scope does not satisfy the composition. The composition specifies that A1.01 is preserved at every partner; A1.01-alone does not extend across substrate boundaries.

*Not "primary-substrate-only" governance with graceful degradation elsewhere.* The architecture does not support graceful degradation; uniformity is a strict-form requirement, not a soft target. A partner with degraded affordances is a violation regardless of how minor the degradation appears, because the architecture cannot reliably distinguish minor degradation from the larger failure modes a deployment slides into when the gradient is permitted at all.

## 6. Why the composition is load-bearing

The composition continues the A1.13 cluster opened by A4.14. A4.14 (A1.13 × A1.04) operationalizes A2.79 — Requirement D — by tying AI-as-substrate-mediator to every layer of composition. A4.15 operationalizes A2.76 — Requirement A — by tying the human-governed commitment to every partner. Together with the three remaining cluster notes, the cluster decomposes A1.13's five-requirement structure into five composition-pair operationalizations.

It supports multi-substrate deployments at scale. CKS deployments at organizational scale are typically multi-substrate, often combining substrates with adjacent components per A1.16's three patterns (Pattern A consultations, Pattern B derived views, Pattern C separate concerns). Without an emergent property tying governance to composition, the architecture's claims at scale weaken to single-substrate claims repeated in parallel. It also extends A4.01 (A1.01 × A1.08, governance-against-authority) from single-substrate scope to composition scope: humans govern authoritative content at every substrate in the composition, which makes A4.01 hold in the multi-substrate case the source paper anticipates throughout §3.1, §11.3, and §13.3.

It distinguishes CKS deployments from asymmetric-governance multi-substrate systems. The broader landscape of "AI orchestration platforms," "multi-system governance integrations," and "federated AI compliance frameworks" routinely composes substrates with heterogeneous governance, often presented as a feature (jurisdictional autonomy, vendor independence, deployment flexibility). The composition specifies that CKS deployments are not in that landscape.

## 7. Operational test

A multi-substrate composition instantiates *governance preservation across composition* if and only if all of the following are true at every composition partner at all times during the composition's existence:

1. **Per-substrate-governance-rights.** At each partner, all four governance rights per A2.01–A2.04 are architecturally available — inspect (substrate content and orchestration rules), modify (same), override (without justification), and rule authoring (humans hold the authority; LLM-drafted rules subject to human authority before they take effect are admissible).
2. **Governance-uniformity.** The set of rights available at each partner is the same set, not a subset. No primary/secondary asymmetry, no read-only-secondary-substrate, no transient-secondary-substrate, no federation with distinct governance models.
3. **Architectural-rights-mapping.** Where vendor mechanisms, workflow features, or runtime middleware provide governance affordances at a partner, those affordances map onto A2.01–A2.04 in their architectural and temporal sense (A2.05, A2.07): rights are properties of the system's design rather than procedural promises subject to vendor revocation; rights are exercisable at any time, not only at scheduled checkpoints.

A composition that fails any of (1), (2), or (3) at any partner fails the property and is not CKS-coherent on the governance axis. The three sharpening properties identify failures specifically: (1) catches partners that do not provide one or more rights; (2) catches deployments whose partners individually pass (1) but collectively fail uniformity; (3) catches deployments that pass (1) and (2) in some weakened sense (procedural rather than architectural; scheduled rather than at-any-time).

The one-sentence test: *A multi-substrate CKS deployment satisfies governance preservation across composition if and only if every substrate participating in the composition supports the same four governance rights as architectural and temporal properties under the same operational specification, with no asymmetry, no degradation, and no substitution of vendor mechanisms that fail to map onto the rights themselves.*

## 8. Conclusion

Naming the A1.13 × A1.01 composition as a standalone derivation matters because it makes the architectural content visible at the level deployment operates at. A1.13 in isolation names per-substrate governance preservation but does not specify what the preservation requires. A1.01 in isolation specifies four rights but does not extend them across substrate boundaries. The composition supplies what each lacks, and the result is the property deployments at scale actually need: governance affordances uniformly available at every substrate, with no asymmetry, no temporal degradation, and no vendor substitution that escapes architectural specification.

The note is the second in the A1.13 composition cluster. Subsequent notes will continue the pattern: A4.16 (A1.13 × A1.07) for retraceability preservation per A2.77; A4.17 (A1.13 × A1.10) for determinism preservation per A2.78; A4.18 (A1.13 × A1.16) for human-selective composition coherence across hybrid composition patterns per A2.80. The cluster, when complete, articulates A1.13's composition framework not as five named requirements but as five operationalizations grounded in the substrate-level commitments each requirement preserves.

Subsequent work that adopts, extends, composes, or argues against the CKS multi-substrate composition framework should use *governance preservation across composition* in the sense formalized here. Work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Governance Does Not Weaken at Composition Boundaries: The Emergent Architectural Property When Composition Requirements and Human-Governed Compose in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
