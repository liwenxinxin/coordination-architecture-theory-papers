# FAI Governance for Specialized Domain Coordination

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3's shared-substrate / Full Aspect Integration (FAI) architecture is domain-agnostic: it makes no assumptions about the organizational domain, regulatory environment, or governance culture of participating Selves. This note formalizes how that domain-agnosticism operates in practice — specifically, how compliance-sensitive domains (healthcare, finance, legal), regulated industry escalation requirements, and varying organizational governance cultures are addressed through governance configuration rather than through architectural modification. The note introduces the content analog of Paper 1's tool-agnosticism as the structural framing: just as tool-agnosticism separates the architecture's universal invariants from platform-configurable deployment choices, domain-agnosticism separates the architecture's universal invariants from domain-configurable governance choices. Both properties follow from the same move — universal commitments that hold regardless of context, plus a governed configuration space that absorbs context-specific requirements. The note also formalizes the anti-pattern of domain-specific architectural override, in which organizations claim that domain requirements justify relaxing core commitments, and establishes an operational test for distinguishing configuration from override.

---

## 1. Why Domain-Agnosticism Requires Explicit Formalization

A coordination architecture serving organizations in regulated industries faces a predictable pressure: the specificity of domain requirements can appear to demand architectural specificity in response. A healthcare organization subject to data-sharing restrictions may conclude that the architecture must be modified to accommodate those restrictions. A financial institution with audit-trail mandates may conclude that the architecture's documentation standards must be specialized for financial instruments. A legal organization with jurisdiction-specific escalation requirements may conclude that the escalation routing must be hard-coded for its domain.

Each of these conclusions represents the same error. The error is not about the legitimacy of the domain requirement — healthcare data-sharing restrictions, financial audit mandates, and jurisdiction-specific escalation rules are all genuine and consequential. The error is about where the domain-specific response should live: in the architecture's core commitments, or in the configuration choices that governance makes within the architecture.

Paper 3's domain-agnosticism commitment is the answer. Domain-specific requirements live in configuration, not in the architecture. The architecture supplies a governed configuration space wide enough to address the full range of domain requirements that participating Selves are likely to face. The configuration choices within that space are governance decisions, made under human authority, subject to the same inspectability and modifiability that apply to all substrate content under Paper 1's commitments. The architecture itself — its conflict-handling tier structure, its evolution feed mechanism, its exchange-bounding, its documentation requirements — holds invariant across domains.

This note formalizes the operational content of that commitment.

---

## 2. The Tool-Agnosticism Parallel

Paper 1 defends tool-agnosticism as one of its six architectural commitments: the architecture works on any compliant host regardless of technical platform. A CKS substrate instantiated in a spreadsheet environment and a CKS substrate instantiated in a document management system are both genuine CKS substrates — not because the underlying tools are equivalent, but because the architecture's properties hold on any platform that satisfies the structural requirements. The technical platform is a configurable deployment choice; the architecture's core commitments are not.

Domain-agnosticism is the content analog of that commitment, and the parallel is exact in structure:

**Tool-agnosticism:** The architecture works on any compliant technical platform. Platform choice is a configurable deployment decision. The architecture's invariants (conflict preservation, human governance, substrate-mediator structure, linear-cost composition) hold regardless of platform.

**Domain-agnosticism:** The architecture works for any organizational domain. Domain-specific governance choices are made through the configuration dimensions that Paper 3 specifies. The architecture's invariants (the six Paper 1 commitments within the shared substrate's scope, three-tier conflict handling, exchange-bounding to substrate content, evolution feed structure) hold regardless of domain.

Both properties arise from the same structural move: separating what is universal from what is contextual, and ensuring that the contextual dimension is addressed through a governed configuration space rather than through per-context architectural variation. An architecture that required technical specialization for each deployment platform would not be tool-agnostic; equally, an architecture that required structural modification for each organizational domain would not be domain-agnostic. Paper 3 claims the latter property for the same structural reason Paper 1 claims the former.

The configuration space that implements domain-agnosticism is specified across three levels: FAI-event-level dimensions (D1.22), conflict-handling-level dimensions, and evolution-feed-level dimensions. A domain-specific governance response selects configuration points within these levels. It does not modify the levels themselves.

---

## 3. Compliance-Sensitive Domain Requirements

Compliance-sensitive domains — healthcare, finance, legal, and others subject to regulatory data obligations — impose specific requirements on organizations that participate in FAI events. These requirements translate directly into configuration choices within the architecture's existing dimensions.

**Sharing scope (D1.22, Dimension 1).** Regulatory constraints on data sharing determine which aspects a participating Self may contribute to a shared substrate. A healthcare organization subject to patient data protection requirements may be restricted from contributing aspects whose constituent cells contain identifiable patient information. The sharing scope dimension accommodates this directly: the organization configures the sharing scope to exclude regulated content, without modifying the FAI mechanism or the shared substrate's structural commitments. The architecture neither forces contribution nor prevents it; governance decides.

**Provenance carry-over depth (Dimension 5).** Regulatory data lineage requirements — common in financial services, mandated for some categories of medical record, and emerging in AI governance frameworks — may require that evolution outputs retain deep provenance attributing each element to its source FAI event and contributing Self. The provenance carry-over depth dimension accommodates this: a compliant organization configures deep provenance carry-over, ensuring that the evolution outputs its home substrate ingests carry the lineage information its regulatory obligations require. A non-regulated organization in the same FAI event may configure shallower carry-over; the per-participant configurability of this dimension accommodates asymmetric regulatory positions within a single FAI event.

**Persistence policy (Dimension 3).** Regulatory retention requirements — minimum retention periods for financial transaction records, audit-trail requirements for regulated healthcare decisions — may mandate that the shared substrate's durable record be retained for specified periods at Locus 2. The persistence policy dimension accommodates this: the governance agreement for the FAI event specifies a retention period at Locus 2 consistent with the applicable regulatory requirement. The retention period is substrate content, human-authored, inspectable, and modifiable under authority.

**Documentation standards.** Compliance-sensitive domains frequently impose documentation standards that exceed the architecture's minimum requirements. The architecture's documentation commitment specifies minimum documentation sufficient for governance accountability; a regulated organization may configure documentation practices that exceed this minimum to satisfy domain-specific obligations. Exceeding a minimum is configuration, not override.

The pattern across all four mappings is the same: the regulatory obligation specifies a constraint; the constraint identifies a point in the configuration space; governance sets the configuration to satisfy the constraint. No architectural modification is required because the configuration space was designed to accommodate the full range of governance requirements participating Selves are likely to face.

---

## 4. Regulated Industry Escalation Routing

Compliance-sensitive domains impose specific requirements not only on data handling but on decision-making authority. Healthcare organizations may be required by regulation or institutional policy to route certain categories of conflict escalation to compliance officers or legal representatives. Financial institutions may face requirements that material discrepancies involving regulated instruments be reviewed by designated compliance personnel. Legal organizations may face jurisdiction-specific requirements about who may authorize certain categories of cross-organizational commitment.

The escalation routing configuration accommodates these requirements directly. When a FAI event's conflict reaches the third tier — escalation to humans across joint authority — the configuration specifies where that escalation routes. In a non-regulated context, the routing destination is a human or group with governance authority over the relevant participating Selves. In a compliance-sensitive context, the routing configuration adds the domain-specific requirement: escalation involving regulated categories routes to the legally designated representative or compliance officer, as the participating organization's governance specifies.

This is not a modification of the escalation tier's structural commitment — escalation still surfaces to humans holding joint governance authority, as the three-tier mechanism requires. It is a specification of which humans receive which escalations, made within the configuration space the escalation routing dimension provides. The routing destination is substrate content, human-authored, inspectable, and modifiable. A change in the regulatory environment — a new compliance requirement, a reorganization of the compliance function — is addressed by modifying the routing configuration, not by modifying the architecture.

The domain-specificity of the routing destination is the normal case, not a special accommodation. Every FAI event's escalation routing configuration is domain-specific in the sense that it reflects the participating organizations' governance structures; regulated industries simply impose additional specificity about which roles within those structures must receive which escalation categories.

---

## 5. Varying Organizational Governance Cultures

Organizations differ in governance culture as well as regulatory environment. Some operate through consensus-driven decision processes in which proposals circulate broadly before approval. Others operate through hierarchical authorization structures in which a designated authority holds unilateral approval rights. Still others operate through committee-based review with defined quorum and voting rules. These cultural differences are real, consequential, and architectural in the sense that they shape how organizations actually exercise governance authority.

The approval mechanics configuration (D1.25) accommodates this variation. The architecture does not prescribe a specific approval process for governance decisions over shared-substrate configuration. It requires that the process be human-governed — that humans hold the authority to approve, modify, and override configuration choices — and that the process be specified as substrate content. The specific form of the approval process is a governance decision.

A consensus-driven organization configures approval mechanics that require broad circulation and explicit endorsement before configuration changes take effect. A hierarchical organization configures approval mechanics that route to a single authority with fast approval cycles. A committee-based organization configures quorum requirements. All three configurations are valid instantiations of the architecture's governance commitment, because all three place configuration decisions under human authority, as substrate content, with the inspectability and modifiability that commitment requires.

Cross-organizational FAI events between organizations with different governance cultures require a shared approval mechanics configuration for shared-substrate governance. This configuration is itself a governance negotiation — the cross-organizational governance agreement (see Section 6) must include agreement on the approval mechanics that will govern shared-substrate configuration decisions. The cultural negotiation is real, but it is a governance negotiation resolved in configuration, not an architectural incompatibility.

---

## 6. Domain-Specific Cross-Organizational Agreements

Organizations in regulated domains should reflect their regulatory constraints explicitly in the cross-organizational governance agreements that establish the terms of FAI events. The agreement's mutual governance standards must reflect the regulatory requirements of the domain, for the same reason that individual-organization governance configurations reflect them: the agreement is the shared-substrate analog of each participating Self's home governance substrate, and it is subject to the same documentation and inspectability requirements.

Specifically, the agreement should address: which aspects each participating organization may contribute given its regulatory constraints; what provenance carry-over depth is required to satisfy the regulatory data lineage obligations of each participant; what persistence and retention policy satisfies the most restrictive applicable regulatory requirement among the participants; and which escalation routing destinations satisfy the compliance function requirements of each participating organization. These are governance decisions, not architectural ones, and they belong in the agreement as substrate content under joint authority.

Where regulatory obligations of different participating organizations conflict — one organization's retention requirement is longer than another's preference; one organization's data-sharing restriction is narrower than another's needs — the agreement must resolve the conflict at the governance level. The architecture's conflict-handling mechanism is available for this purpose: unresolved governance-level conflicts can be preserved as first-class state within the agreement substrate, documented for future resolution, rather than forcing a premature resolution that ignores one organization's legitimate constraint.

---

## 7. What Is Domain-Agnostic and What Is Domain-Specific

The domain-agnosticism commitment requires precision about what it covers. Not everything in a domain-specific FAI deployment is domain-agnostic; the claim is about the architecture's core commitments, not about the deployment as a whole.

**What is domain-agnostic:** The six Paper 1 commitments within the shared substrate's scope — conflict preservation as first-class state, human governance of substrate content, AI as substrate mediator, tool-agnosticism, linear-cost composition, the substrate-LLM division — hold regardless of domain. The three-tier conflict-handling structure — preserve, resolve via orchestration, escalate to humans — holds regardless of domain. The evolution feed mechanism — its four-locus structure, its layer-routing rule, its exchange-bounding to substrate content — holds regardless of domain. The shared-substrate lifecycle — construction for an event, dissolution on completion, evolution output hand-off — holds regardless of domain. A healthcare FAI event and a manufacturing FAI event use the same architecture. The difference is in the configuration choices within that architecture, not in the architecture itself.

**What is domain-specific:** The configuration choices within the dimensions the architecture specifies are governance decisions that reflect domain requirements. Sharing scope, persistence policy, provenance carry-over depth, documentation standards beyond the minimum, escalation routing destinations, and approval mechanics are all governance decisions. A healthcare organization's sharing scope configuration differs from a manufacturing organization's because their regulatory environments differ. Both are valid configuration choices within the same architecture.

The line between the two categories is the line between the architecture's core commitments and its governed configuration space. Domain-specific requirements belong on the configuration side of that line. Crossing the line — placing domain-specific responses on the commitment side, as modifications to the architecture — is the anti-pattern this note addresses.

---

## 8. Anti-Pattern: Domain-Specific Architectural Override

The domain-specific architectural override anti-pattern occurs when an organization or implementation claims that domain-specific requirements justify modifying the architecture's core commitments. The claim typically takes one of several forms:

**Form 1 — Compliance exception to conflict preservation.** A compliance-sensitive organization claims that its regulatory environment requires that certain conflicts be silently resolved rather than preserved as first-class state, on the grounds that preserving them creates an audit trail that the organization would prefer not to maintain. The anti-pattern is the claim that the regulatory environment justifies bypassing conflict preservation. The correct response is: conflict preservation is a core architectural commitment that holds regardless of domain. If preserving a conflict creates an audit trail, that audit trail is the expected governance record, not an architectural problem to be engineered around. Documentation standards are configurable upward; conflict preservation is not configurable away.

**Form 2 — Security exception to exchange bounding.** An organization claims that its domain requires exchanging instinct-layer content (LLM weights, model parameters) between Selves during FAI events, on the grounds that its domain's performance requirements cannot be met by exchanging only substrate content. The anti-pattern is the claim that domain requirements override the exchange-bounding commitment. The exchange-bounding to reasoning-layer content is a core architectural commitment inherited from Paper 2's instinct/reasoning separation. Domain-specific performance requirements should be addressed through configuration of what substrate content is exchanged, at what depth, under what provenance carry-over — not by extending the exchange boundary to instinct-layer content.

**Form 3 — Governance culture exception to documentation standards.** An organization claims that its internal governance culture prefers minimal documentation, and therefore the FAI event's documentation standards should be reduced below the architecture's minimum. The anti-pattern is the claim that governance culture justifies weakening documentation standards. The architecture's minimum documentation standard is an architectural commitment that holds regardless of governance culture. Organizations that prefer minimal documentation may configure their internal processes outside the shared substrate as they choose; the shared substrate's documentation standards are not adjustable below the minimum.

The pattern across all three forms is the same: a legitimate contextual constraint (regulatory environment, performance requirement, governance culture preference) is used to justify a modification to a core architectural commitment rather than a selection of a configuration point within the governed configuration space. The architecture's answer in all cases is the same: configure appropriately for your domain within the space the architecture provides; do not override the core commitments.

An important clarification: the anti-pattern applies to claimed overrides, not to legitimate flexibility within the configuration space. An organization that configures deep provenance carry-over to satisfy regulatory requirements is not overriding anything — it is selecting a point within the architecture's governed configuration space. An organization that configures shorter Locus 2 retention because its domain has no retention requirements is not relaxing an architectural commitment — it is exercising the governance authority the architecture provides. The anti-pattern is the claim that core commitments may be bypassed, not the exercise of legitimate configuration authority.

---

## 9. Operational Test

For a FAI event in a compliance-sensitive domain, an observer can verify that domain-specific requirements are addressed through configuration rather than through architectural override by checking the following:

1. Each domain-specific governance requirement of participating Selves is traceable to a specific configuration choice within one of the architecture's governed configuration dimensions (sharing scope, cardinality, persistence policy, cooperation/competition variant, provenance carry-over depth, multi-mediator coordination at the FAI-event level; tier-selection rules, conflict-class definitions, escalation-path configurations, joint-authority configurations, recursive-governance depth, authority-articulation mechanics at the conflict-handling level; hand-off mode, per-mechanism feed configurability, ingestion policy, conflict-annotation propagation depth at the evolution-feed level).

2. The configuration choices made to address domain-specific requirements are recorded as substrate content within the shared substrate or the cross-organizational governance agreement, and are therefore subject to the architecture's standard inspectability and modifiability requirements.

3. No domain-specific requirement has been addressed by modifying the architecture's core commitments: conflict preservation is operating as specified; exchange bounding to substrate content is operating as specified; the three-tier conflict-handling structure is operating as specified; documentation standards are at or above the architecture's minimum; escalation surfaces to humans holding governance authority over the relevant participating Selves, as the three-tier mechanism requires.

4. Where regulatory obligations of different participating organizations conflict with each other, the conflict is addressed through the governance agreement as a first-class governance decision — either resolved in the agreement as a recorded choice or preserved as an unresolved conflict subject to future resolution — rather than silently collapsed by one organization's configuration overriding another's.

5. The approval mechanics for shared-substrate configuration decisions reflect a governance process agreed to by participating organizations and recorded as substrate content, rather than imposed unilaterally or left unspecified.

A FAI event that satisfies all five conditions addresses its domain-specific requirements through configuration and governance, without architectural override. A FAI event that fails condition (3) exhibits the domain-specific architectural override anti-pattern, regardless of how the override is framed.

---

## 10. Conclusion

Domain-agnosticism is the content analog of Paper 1's tool-agnosticism. Tool-agnosticism commits to the architecture operating on any compliant technical platform, with platform choice as a governed deployment decision. Domain-agnosticism commits to the architecture operating for any organizational domain, with domain-specific governance choices as governed configuration decisions. Both properties follow from the same structural move: universal invariants that hold regardless of context, plus a governed configuration space that absorbs context-specific requirements.

The practical consequence is that compliance-sensitive domain requirements — data-sharing restrictions, audit-trail mandates, retention obligations, compliance function escalation routing — translate directly into configuration choices within the architecture's existing dimensions. Organizations in regulated industries do not need a modified architecture; they need a governed deployment of the architecture with configuration choices that reflect their regulatory obligations.

The domain-specific architectural override anti-pattern — claiming that domain requirements justify relaxing conflict preservation, weakening exchange bounding, or bypassing documentation standards — misconstrues this relationship. Domain requirements are configuration inputs, not architectural overrides. The architecture's configuration space is wide enough to accommodate the full range of domain requirements that participating Selves are likely to face; the core commitments are stable enough to hold regardless.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *FAI Governance for Specialized Domain Coordination.* May 15, 2026. ORCID: 0009-0004-8065-3235.
