# Compliance Demonstration Test Suite: The Test Battery Governance Assembles to Demonstrate Paper 2 Architectural Compliance to External Parties

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its contribution is to specify, in operational form, the test battery governance assembles when demonstrating Paper 2 architectural compliance to external parties, and the five categories of evidence artifacts that battery produces.

## Abstract

The earlier notes in this series specify internal operational tests that produce internal *governance signals* — pass/fail readings that drive governance action. External-facing compliance demonstration is a distinct activity with a distinct output: not a governance signal but a package of *evidence artifacts* that auditors, regulators, partners, or other external parties can independently verify without taking governance's word for any underlying claim. This note formalizes the compliance demonstration test suite — the test battery governance assembles for this external-facing purpose. The suite produces five categories of evidence artifact corresponding to five compliance claims: (1) humans govern AI behavior at every structural level; (2) governance history is retraceable from current state to authoritative origin; (3) entities are created, combined, and closed through governed lifecycle events; (4) DNA evolution is governed across all three evolution mechanisms; (5) individual entities at each structural level independently satisfy Paper 1 commitments at their scope. Together the five demonstrations constitute a complete compliance evidence package whose distinguishing property is external-verifiability without privileged access — every artifact reconstructable from substrate state — and whose cross-reference structure is itself a substance-versus-ritual test.

## 1. Internal testing produces signals; compliance demonstration produces artifacts

The B5 phase of this series has developed an internal test battery: tests governance runs on its own deployment to read whether the architecture is currently operating per Paper 2 commitments. The output of an internal test is a *governance signal* — a pass/fail reading, an exception list, a coverage percentage — that governance uses as input to its own decisions about whether to authorize the next operation, repair a drift, or escalate. The recipient of an internal test result is governance itself.

Compliance demonstration is a different activity with a different recipient. The recipient is an *external party*: an auditor, a regulator, a partner performing diligence, a customer relying on the deployment for a regulated workflow. External parties are not given access to governance's internal signal stream and should not be expected to take governance's word that internal tests passed. They require *evidence artifacts* — records, traces, samples, and reconciliations whose authenticity and completeness can be verified against substrate state independently. The signal compresses substrate evidence into a verdict; the artifact preserves enough substrate evidence for an independent verdict to be reached.

This note formalizes the test suite governance assembles for the external-facing case. The suite reuses components developed in the earlier B5 notes (B5.02–B5.12), but selects, packages, and exports them as evidence artifacts rather than as signals. The five demonstrations are developed in §§2–6, the assembled package in §7, and the operational test in §8.

## 2. Demonstration 1 — Human governance of AI behavior

The first compliance claim is that humans govern AI behavior in the deployment, per the human-governed commitment (A1.01) carried recursively into Paper 2's structural levels (B1.20).

**(a) Governance decision records.** Ten recent governance acts — DNA modifications, birth authorizations, override events — drawn across cell scope, aspect scope, and Self scope. Each act carries the six-field A2.40 provenance metadata (what was decided, by whom, under what authority, with what rationale, against what conflicts, at what time), and each act's authorizing human is presented per A2.47.

**(b) Governance explanation sample.** For three of the ten acts, the authorizing human's written reasoning is included as substrate content — captured at the moment of authorization, not post-hoc. Substantive reasoning attached to authorization moments distinguishes governance that is being *exercised* from governance that is being *performed*.

**(c) Behavior-specification match.** Five cell operations are traced to the governing DNA specification under which each ran. For each trace, the four accountability questions of A5.09 are answered against substrate evidence: which DNA specification governed this operation; who authorized that specification; what substrate state the operation read; what substrate state it wrote.

**(d) Level-appropriate governance.** Governance acts at cell scope, aspect scope, and Self scope are presented separately and labeled by their level, demonstrating that the recursive structure of B1.20 is operative rather than collapsed: cell-scope acts govern cell-scope content, aspect-scope acts govern aspect-scope content, Self-scope acts govern Self-scope content.

**Package**: ten governance records, three governance reasoning statements, five operation-to-specification traces, and level-scope evidence demonstrating distinct governance at each of the three structural levels.

## 3. Demonstration 2 — Retraceable governance history

The second compliance claim is that the deployment's governance history is retraceable from any current state back to its authoritative origin, per path retraceability (A1.07) and substrate-as-source-of-truth (A1.08).

**(a) DNA version chain.** For one representative entity, the complete DNA version chain from birth to current state, presented per B2.69. Each version carries A2.40 provenance and references its predecessor, so an external party can walk the chain link by link.

**(b) Lineage chain.** The complete entity lineage for the same entity per B2.43: the birth record, any mating or supersession events the entity has participated in, and the chain of operational events that form the entity's history. Lineage chain and DNA version chain together account for both rule-layer history and entity-identity-layer history.

**(c) Governance traceability demonstration.** A current DNA rule is selected and its complete governance history is traced back to the entity's birth, demonstrating A1.07 path retraceability and A1.08 authority continuity at each point along the chain. Authority transitions along the chain are made explicit in substrate.

**(d) Provenance completeness report.** The A5.08 provenance completeness report, showing the percentage of events with complete A2.40 provenance across all event categories. Percentages below 100% are not concealed; their causes are stated as substrate content so external parties can assess whether the incompleteness is a known and accepted condition or a governance gap.

**Package**: the complete DNA version chain, the complete lineage chain, the governance traceability trace, and the A5.08 provenance completeness report.

## 4. Demonstration 3 — Entity lifecycle governance

The third compliance claim is that entities — cells, aspects, and Selves — come into existence, combine, and close through governed lifecycle events rather than through ungoverned processes, per B1.09 (birth), B1.10 (mating), and B1.11 (death).

**(a) Birth governance sample.** Five entity birth records per B2.44. Each carries the birth specification (what the entity is, what scope it covers, what initial DNA it inherits) and the governance authorization (which authority approved the birth, with what reasoning, against what conflicts).

**(b) Mating governance sample.** Two mating event records per B2.50 (if the deployment has performed mating). Each identifies the pattern applied (union, selective merge, or lineage-preserved union), the authorization, and the cross-lineage references tracing the merged entity to both parents.

**(c) Death governance sample.** Two death event records per B2.55 (if the deployment has performed entity retirements). Each identifies the death type (lineage supersession or functional obsolescence), the archival state of the entity's substrate content, and the closure of the entity's lineage.

**(d) Entity inventory reconciliation.** Current live-entity count alongside birth-count and death-count totals, with the relationship `live = births − deaths` verified against substrate. An external party can confirm the reconciliation independently.

**Package**: five birth records; mating records as applicable; death records as applicable; and the inventory reconciliation.

## 5. Demonstration 4 — Evolution governance

The fourth compliance claim is that DNA evolution is governed through all three evolution mechanisms — instinct evolution, DNA evolution, action-feedback evolution — per B1.12–B1.15.

**(a) Directed selection sample.** Five directed-selection event records per B2.72. Each demonstrates authorization (the authority under which the change proceeded), authoring (who wrote the change), recording (the substrate event capturing it), and retroactivity compliance (whether and how prior records remain unmodified).

**(b) Mutation governance sample.** Two mutation event records per B2.66. Each shows the verification gate execution that preceded the mutation, the routing through which it reached its applicable scope, and the high-stakes protections that applied if it crossed a high-stakes boundary.

**(c) Action-feedback sample.** For deployments mature enough to have run the loop end to end, one complete action-feedback pipeline execution per B2.76 — from evidence accumulation, through the Stage 2 approval that lifts evidence into a DNA change proposal, to the DNA change itself. The trace demonstrates that the loop closed through authoritative substrate at every transition.

**(d) No-silent-drift evidence.** The B2.78 anti-silent-drift check result, showing no DNA proposals integrated without Stage 2 approval over the demonstration window. The "no silent drift" claim is what makes action-feedback evolution distinguishable from drift; the evidence artifact is the absence — verifiable against substrate — of unapproved integrations.

**Package**: five directed-selection records, two mutation governance records, one action-feedback execution trace (where applicable), and the anti-drift check result.

## 6. Demonstration 5 — Entity-level Paper 1 compliance

The fifth compliance claim is that individual entities at each structural level *independently* satisfy Paper 1 commitments at their scope, per the recursive-levels principle of B1.20. The independence is the load-bearing word: a deployment in which only the Self satisfies Paper 1 — with cells and aspects covered by inclusion under Self-level compliance — does not satisfy this claim.

**(a) Cell-level compliance sample.** Inheritance verification results per B2.14 for two cells, demonstrating that each cell, on its own, satisfies the Paper 1 commitments (human-governed, substrate–cell boundary, conflict preservation, AI-as-substrate-mediator, tool-agnosticism, linear-cost scaling, path retraceability, substrate-as-source-of-truth) at cell scope.

**(b) Aspect-level compliance sample.** Aspect-level verification per B2.19 for one aspect, demonstrating that the aspect — as an entity at its own structural level — independently satisfies the same Paper 1 commitments at aspect scope. The verification is not a roll-up of cell-level results; it is a separate verification against aspect-scope substrate.

**(c) Self-level compliance sample.** Self-level verification per B2.24 for one Self, demonstrating that the Self, as the largest structural entity, independently satisfies Paper 1 commitments at Self scope, again separately from its constituents.

**(d) Recursive commitments verification summary.** The B2.110 verification summary showing all entities at all levels passing their level-appropriate Paper 1 verification. Where any entity has not passed, its current remediation status is included as substrate evidence rather than concealed.

**Package**: two cell verifications, one aspect verification, one Self verification, and the B2.110 summary.

## 7. The compliance demonstration package as a whole

The five demonstrations together constitute a complete compliance evidence package. The package is structured so that an external party can perform three verifications against it. *Within-demonstration verification*: each demonstration's four artifacts together support its claim without requiring artifacts from elsewhere. *Cross-reference verification*: a governance act recorded in Demonstration 1 may correspond to a DNA version transition in Demonstration 2, a lifecycle event in Demonstration 3, or a directed-selection event in Demonstration 4; an entity named in Demonstration 3 should appear consistently in the lineage chain of Demonstration 2 and the recursive verification summary of Demonstration 5. *Overall-substance verification*: the external party can assess whether the deployment instantiates Paper 2 architectural commitments in *substance* rather than only in *claim* — a question any individual demonstration in isolation cannot answer.

The package's design property is *external-verifiability without privileged access*: every artifact is reconstructable from substrate state the deployment can expose to the external party under whatever access arrangement the parties agree to. No artifact requires the external party to trust governance's internal signal stream; the external party's verification work consists of reading substrate, not of trusting reports about substrate.

The cross-reference test is itself the substance test. A deployment whose authorizing humans attach substantive reasoning (Demonstration 1.b), whose lineage chains trace continuously to birth (Demonstration 2.b–c), whose lifecycle events carry complete authorization (Demonstration 3.a–c), whose evolution events show verification gate execution and Stage 2 approval (Demonstration 4), and whose entity-level verifications hold independently at each level (Demonstration 5) produces a package whose cross-references resolve. A deployment whose records are ritual — placeholder reasoning, decoupled lineage chains, checkbox provenance, inherited rather than independent verifications — cannot, because ritual records are decoupled in ways substantive records are not.

## 8. Operational test

A deployment can produce a Paper 2 compliance demonstration package per this note if and only if all of the following hold.

1. The five evidence packages of §§2–6 can be assembled in their entirety from substrate state, without reconstruction from sources outside the substrate.

2. Every artifact carries A2.40 provenance to a degree consistent with the A5.08 completeness report; incompleteness for any artifact is named and explained as substrate content rather than concealed.

3. Cross-references between the five demonstrations resolve: governance acts in Demonstration 1 locate in Demonstrations 2–5 where they apply; entities named in Demonstration 3 appear consistently in Demonstrations 2 and 5; evolution events in Demonstration 4 reconcile against DNA version chains in Demonstration 2; entity-level verifications in Demonstration 5 reference the same entities whose lineages appear in Demonstrations 2 and 3.

4. External parties presented with the package can independently verify each artifact against substrate state under the agreed access arrangement, without requiring access to governance's internal signal stream.

5. The package, taken together, supports the external assessment that the deployment instantiates each of the five compliance claims in substance, not only in claim — i.e., that substantive reasoning, resolving cross-references, and independent entity-level verifications are present.

A deployment that can produce the package per (1)–(5) is in a position to demonstrate Paper 2 architectural compliance to external parties. A deployment that cannot is not, regardless of the compliance claims it makes verbally or in its documentation.

## 9. Conclusion

Internal testing and external compliance demonstration share substrate state but differ in product: internal tests produce signals that drive governance action; compliance demonstration produces evidence artifacts external parties verify independently. The suite formalized here assembles five evidence packages — human governance of AI behavior, retraceable governance history, entity lifecycle governance, evolution governance, entity-level Paper 1 compliance — so that an external party with appropriate access can confirm each compliance claim against substrate content rather than against governance's self-report. By its structure the package demonstrates governance substance rather than ritual: an architecture instantiating Paper 2 commitments in substance can produce a package whose cross-references resolve and whose entity-level verifications independently hold; an architecture that has not cannot, even where its records appear in order at first glance. The suite is not additional governance burden but the externally-facing surface of governance work already being done internally — repackaged for a recipient who cannot consume governance signals directly, but to whom governance is itself accountable.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Compliance Demonstration Test Suite: The Test Battery Governance Assembles to Demonstrate Paper 2 Architectural Compliance to External Parties.* May 13, 2026. ORCID: 0009-0004-8065-3235.
