# Self-Level Instinct/Reasoning Configuration: Decomposing the Self as Integrated Whole by Formalizing the Self Level as Architectural Locus for Instinct/Reasoning Separation Configuration

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 8, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the **Self level** as the architectural locus at which the instinct/reasoning separation is operationally configured — specifying which LLM instances function as instinct layer per B2.01, which substrate authoritative content constitutes reasoning layer per B2.02, and the separation configuration rules under which routing per B2.04, high-stakes pinning per B2.05, verification gating per B2.06, and mutation governance per B1.13 operate across the Self's aspects and cells — as a derivation of Paper 2's three-level structure under Paper 1's substrate/LLM division at the governance boundary.

## Abstract

Paper 2 commits to the separation of fast-pattern instinct from deliberate reasoning as two independently-evolving layers under unified human governance, with the LLM as instinct layer and the CKS substrate from Paper 1 as reasoning layer. Paper 2 also commits to a three-level structure — cell, aspect, Self — in which Paper 1's commitments hold recursively. The separation must be operationally configured somewhere in this structure: which LLM instance(s) function as instinct, which substrate constitutes reasoning, which rules govern routing, which decisions are pinned, which verification gates apply, and which mutation governance instruments operate must be specified concretely for the Self to behave as an integrated whole. This note formalizes the Self level as that locus. The Self is where separation configuration lives, is governed, and changes; aspects and cells operate within Self-level configuration rather than redefining it. The note states the architectural specification, distinguishes it from cell-level routing and aspect-level customization that operate within it, articulates the inherited Paper 1 commitments, enumerates operational implications, names the limits, and provides an operational test. This is the twenty-third Phase B2 note and the fourth of five notes decomposing B1.05 (Self as integrated whole).

## 1. Why Self-level instinct/reasoning configuration needs to be formalized as standalone

Paper 2 commits to two architectural moves whose composition this note formalizes. The first is the instinct/reasoning separation: the LLM is the instinct layer, the CKS substrate is the reasoning layer, and the two compose into one Self under unified human governance. The second is the three-level structure (cell, aspect, Self) in which Paper 1's commitments hold recursively. The composition raises an architectural question Paper 2 settles in passing but does not name as a standalone derivation: at which level of the structure is the separation operationally specified?

The answer Paper 2 commits to — and that this note formalizes — is the **Self level**. The Self is the integrated whole, and the separation is integrated-whole architecture. The separation itself — which LLM is the instinct, which substrate is the reasoning, which routing rules apply, which decisions are pinned, which verification gates are active, which mutation governance instruments operate — is configured at Self scope so that it holds consistently across all aspects and all cells participating in the Self. Cells route between instinct and reasoning per Self-level rules; aspects organize cells around purpose-defined modes within Self-level configuration.

Naming the Self level as the architectural locus has three consequences. It prevents the failure mode in which different aspects within the same Self use incompatible LLM/substrate configurations and the Self loses coherence as one integrated whole. It gives operational variants of the separation a single home: B2.04 routing patterns, B2.05 high-stakes identification, B2.06 verification gates, B1.13 mutation governance instruments, and B2.03 architectural-test scenarios all operate within Self-level configuration rather than being redefined per cell or per aspect. And it makes vendor changes and substrate upgrades into Self-scope governance events with deployment-wide consequences and recorded provenance, rather than per-cell patches with unpredictable composition. The strategic posture remains the same as the rest of the series: defensive publication of public prior art under the author's name.

## 2. The architectural specification, precisely stated

**Self-level instinct/reasoning configuration** is the substrate-resident authoritative content that operationally specifies the separation Paper 2 places at the Self level. It comprises four components.

**(a) LLM-instance specification (instinct layer per B2.01).** The Self's configuration names which LLM instance or instances function as the instinct layer for the cells the Self contains — vendor and model identification, deployment endpoint, and the access pattern under which the LLM is invoked, with credentials referenced through a substrate-resident indirection rather than embedded directly. Multiple LLM instances may be configured for different cell purposes within the Self, with the configuration recording which cells use which instance.

**(b) Reasoning-substrate specification (reasoning layer per B2.02).** The Self's configuration names which substrate authoritative content per A1.08 and A2.46 constitutes the reasoning layer — which data stores, structured artifacts, orchestration substrates, and provenance stores compose into the reasoning Paper 1's substrate/LLM division at the governance boundary commits to keeping outside the LLM. The specification of which substrate is the reasoning layer is itself substrate-resident.

**(c) Separation configuration rules.** The Self's configuration carries the rule set that determines how the separation operates across the Self's aspects and cells. This includes the routing rules that direct each cell's processing between instinct and reasoning layers per B2.04; the high-stakes identification rules that determine which decisions are pinned to the reasoning layer per B2.05 regardless of how capable instinct becomes; the verification gate configuration — which LLM versions are admitted, which verification suites run at integration, which pass-rate thresholds apply — per B2.06; the mutation governance instruments (verification, routing, pinning) per B1.13 specified at Self level; and the separation-test configuration per B2.03 — which scenarios exercise the separation and what the architectural test requires the Self to satisfy.

**(d) Governance metadata.** Configuration changes carry the six provenance fields per A2.40. The configuration is governed authoritative content; changes to it are recorded with provenance the same way other authoritative content is.

The four components together are substrate-resident authoritative content per A2.46 (Category 4 — the configuration is governable architectural artifact, not host-environment configuration sitting outside the substrate). Configuration is governed per A1.01 — humans inspect, modify, and override at any time during the Self's existence. Configuration evolves through directed selection per B1.14 as the deployment matures. Cross-Self comparison is out of Paper 2's scope; the configuration this note formalizes is intra-Self.

## 3. What makes Self-level configuration architecturally distinctive

Conventional AI deployments often integrate LLMs through ad-hoc patterns: different application components invoke different model endpoints under different conditions; routing logic accretes in application code; high-stakes guarding is implemented per-feature; verification runs as deployment-pipeline checks against whatever the application happens to use. The integration is real and works in many cases, but it is not architecturally specified at any single locus. There is no answer to the question "what is the LLM-and-substrate configuration of this deployment as an integrated whole" because the deployment is not architecturally an integrated whole at the LLM-integration layer.

Self-level configuration commits something different. The integration is specified at the Self level as an architectural property: a Self has a configuration, the configuration names the LLM instances that function as instinct, names the substrate that functions as reasoning, names the rules that govern routing and pinning and verification and mutation, and the configuration is itself substrate content under the same authority architecture that governs every other substrate content. The Self is thereby an integrated whole at the LLM-integration layer specifically, not only at the cell-composition or aspect-coordination layer.

This is consequential for governance. Deployment-wide LLM behavior becomes a governance object; LLM changes propagate through Self configuration with provenance, not through silent substitution at each invocation site; high-stakes pinning applies consistently across the Self because the rules live at Self scope; the mutation governance instruments per B1.13 operate over a configuration humans inspect rather than over scattered application-layer code humans cannot inspect uniformly. Per-cell or per-aspect ad-hoc separation would fragment the architecture; Self-level configuration is what keeps the separation coherent as the Self scales.

## 4. The cognitive analog as conceptual scaffold

The cognitive analog Paper 2 carries forward — System 1 / System 2 organization in human cognition — operates at the level of the integrated person, not per task. A human's cognitive architecture is an integrated whole that holds System 1 and System 2 organization spanning all activity domains; the separation is a property of the architecture, not a per-domain configuration the person assembles for each task. The same conceptual shape applies to the Self: the separation is a property of the Self as integrated whole, not a per-cell or per-aspect arrangement.

The analog functions as conceptual scaffold readers absorb quickly because the parallel is intuitive. CKS Selves are not cognitive systems in any biological sense; the analog illuminates the architectural shape, and the configuration itself does the architectural work.

## 5. Inheritance from Paper 1 commitments

Self-level instinct/reasoning configuration inherits a precise set of Paper 1 commitments without modification.

**A1.04 — AI-as-substrate-mediator.** The mediator role is specified at Self level through the LLM-instance component. The Self's configuration places the LLM in the mediator role across the cells the Self contains; the role is an architectural property of the Self, not an attribute of any single cell.

**A2.04 — Rule authoring as governance.** The configuration's separation rules are orchestration rules in Paper 1's sense; they are authored by humans, and LLM-drafted rules become governing rules only after passing under human authority.

**A2.46 — Substrate-resident authoritative content.** Self-level configuration is Category 4 substrate content — first-class governable substrate content, not host-environment configuration outside governance.

**A2.40 — Six provenance metadata fields.** Configuration changes are recorded with the six provenance fields. Vendor changes, new verification suites, modified pinning rules, revised routing patterns each appear as substrate edits with full provenance.

**A1.01 — Authority, not labor.** Configuration is human-governed: humans hold the rights to inspect, modify, and override at any time. The labor of authoring configuration may be allocated across humans, LLMs operating under human direction, and stable cells; the authority over the result is not.

**A1.05 — Tool-agnosticism.** Specific LLM vendors and reasoning-substrate platforms are not architecturally prescribed. Vendor migration is a configuration change at Self level — the configuration names a different LLM, the routing rules update, provenance records the change — not an architectural reconstruction.

**A2.21 — Property C of the mediator role.** The configuration ensures the LLM does not hold substrate-relevant state outside the substrate; the reasoning-substrate component is what the substrate-resident state is, and the LLM-instance component is configured to access it through the mediator role rather than to retain it.

**B1.13 — Mutation governance.** The three mutation governance instruments — verification, routing, and pinning — are operationally specified at Self scope through the configuration. Verification suites, routing patterns, and pinning rules are configuration content, not implicit deployment posture.

The inheritance is direct; Self-level configuration does not propose new commitments. It formalizes the locus at which Paper 1's commitments are operationally specified for the separation Paper 2 introduces.

## 6. Operational implications

Several implications follow from treating the Self level as the architectural locus for instinct/reasoning configuration.

**Configuration is per-deployment and evolves through directed selection.** Deployments configure the separation at Self level per their operational requirements — which LLMs to use, how cells route, which decisions are pinned, what verification suites run, what thresholds apply. As deployments mature — as instinct sharpens through LLM upgrades, as accumulated experience identifies new high-stakes paths, as verification regimes are tuned — the configuration evolves through directed selection per B1.14. The evolution is governed; configuration changes are recorded with provenance per A2.40.

**Configuration changes affect all participating aspects and cells.** When Self configuration changes, the change propagates through every aspect and every cell that operates under the Self. The Self is integrated whole at this layer, and changes have integrated-whole consequences. The propagation is itself a governance event subject to inspect, modify, and override authority.

**Boundary cases interact at Self scope.** A6.03 (vendor unavailable) triggers configuration changes at Self level — the unavailable vendor is replaced, routing updates, provenance records the change. A6.09 (vendor data-handling-policy change) triggers Self-level configuration review — whether the new policy is acceptable for the Self's purpose is a Self-scope governance question, not a per-cell question. Where a Self spans organizational boundaries (per A2.47), the configuration may need cross-partner authority to be authored, modified, or overridden, with the configuration remaining substrate-resident and the authority architecture extending to span the partners.

**Configuration is foundational for lower-scope operations.** B2.04 routing patterns operate within Self-level configuration; B2.05 high-stakes identification operates over Self-level rules; B2.06 verification gates operate at Self-level thresholds. The Self-level configuration is the framework; the lower-scope operations are realizations within it. A deployment may have multiple Selves with different configurations for different deployment contexts; each Self has one separation configuration. Paper 2 specifies intra-Self dynamics; the integration of multiple Selves is out of scope.

## 7. Limits

Naming Self-level configuration as the architectural locus is not a maximalist claim. Stating precisely what it does not commit to keeps the framing aligned with Paper 2's scope.

**Configuration does not replace cell-level routing.** B2.04 routing patterns continue to operate at cell scope; configuration sets the framework, routing operates within it. Cells still make per-invocation routing decisions per the rules the configuration specifies.

**Configuration does not eliminate aspect-level customization.** Aspects may carry additional configuration content within the Self framework — purpose-defined adjustments to verification thresholds, aspect-specific pinning rules, aspect-scoped substrates. The Self-level configuration is the framework; aspect customization is realization within it.

**Configuration does not prescribe specific LLMs or substrates, prevent LLM evolution, or stay static.** Tool-agnosticism per A1.05 holds; configuration names instances chosen for the deployment, not architecturally privileged products. Mutation per B1.13 governs evolution; the configuration is what the mutation governance instruments operate on, not a freeze on the layers the configuration names. The configuration evolves through directed selection per B1.14 as the Self matures.

**Configuration is not cross-Self.** Paper 2 specifies intra-Self dynamics. Multiple Selves may have different configurations, and how Selves with different configurations integrate is not within Paper 2's scope.

**Configuration does not bypass governance.** A1.01 holds throughout; humans hold the rights to inspect, modify, and override configuration at any time during the Self's existence.

## 8. Operational test

A Self instantiates the Self-level instinct/reasoning configuration commitment if and only if all of the following are true at all times during the Self's existence:

1. The Self has substrate-resident authoritative content that names which LLM instance(s) function as instinct layer per B2.01 and which substrate authoritative content per A1.08 and A2.46 constitutes reasoning layer per B2.02.
2. The same substrate-resident content carries the separation configuration rules that drive routing per B2.04, high-stakes identification per B2.05, verification gates per B2.06, mutation governance per B1.13, and the architectural test for separation per B2.03 across the Self's aspects and cells.
3. Changes to the configuration are recorded with the six provenance fields per A2.40.
4. Humans hold the rights to inspect, modify, and override the configuration at any time per A1.01, with no LLM operation, vendor policy, or runtime middleware able in principle to prevent the rights.
5. Aspect-level and cell-level operations operate within the Self-level configuration rather than redefining it.

A Self that fails any of (1)–(5) may operate, but does not instantiate Self-level instinct/reasoning configuration in the CKS sense.

## 9. Why naming Self-level configuration as standalone matters

This is the fourth of five notes decomposing B1.05 (Self as integrated whole). B2.20 formalized the Self as integrated whole as a standalone architectural commitment. B2.21 formalized the Self integration architecture — the substrate-shared topology and unified governance properties that make the integration architecturally available. B2.22 formalized the Self-aspect content-domain operationalization. B2.23 formalizes the locus at which the instinct/reasoning separation is operationally configured. B2.24 will close the B1.05 decomposition by formalizing Self-level inheritance verification. Subsequent Phase B2 notes will continue with B1.06 two-layers-within-every-cell decomposition (B2.25 onward).

This note's piece is the configuration locus. The Self level is the architectural home of instinct/reasoning separation configuration; per-cell and per-aspect ad-hoc configuration would fragment the architecture; the configuration is substrate-resident authoritative content under the same authority architecture that governs every other substrate content; the configuration is the framework within which routing, high-stakes pinning, verification gating, and mutation governance operate as realizations across the Self's aspects and cells.

Subsequent work that extends or composes the CKS pattern's Self-level architecture should treat Self-level instinct/reasoning configuration as the locus formalized here. Subsequent work that places the configuration at a different level of the structure is committing to a different architecture, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Self-Level Instinct/Reasoning Configuration: Decomposing the Self as Integrated Whole by Formalizing the Self Level as Architectural Locus for Instinct/Reasoning Separation Configuration.* May 8, 2026. ORCID: 0009-0004-8065-3235.
