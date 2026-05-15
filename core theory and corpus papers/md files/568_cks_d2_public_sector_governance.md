# FAI Governance for Non-Profit and Public-Sector Selves

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

This note is derivation note D2.73, the seventy-third Phase D2 operational variant note in the Series D derivation chain. It derives from D1.25 (joint authority as substrate content) and D2.44 (domain-agnosticism of the configuration architecture). Its sole contribution is to formalize, in operational form, how FAI governance configuration interacts with the distinctive governance authority structures of non-profit and public-sector organizations — so that practitioners deploying this architecture in such organizations can identify the configuration decisions that carry institutional weight.

## Abstract

D2.44 established that the FAI governance architecture is domain-agnostic: the configuration dimensions that govern joint authority, escalation routing, cross-organizational agreements, propagation restrictions, and documentation standards apply equally across commercial, non-profit, and public-sector organizational contexts. D2.73 applies this commitment to non-profit and public-sector organizations specifically, which carry three governance properties that commercial organizations typically do not share: public accountability obligations that may extend transparency requirements beyond what private deployments face; governance authority distributed across institutional roles rather than concentrated in named individuals; and procurement or contracting frameworks that constrain how cross-organizational governance agreements are formed. Four configuration implications follow from these properties: joint authority must be specified to institutional roles rather than to individuals; escalation routing must target institutional roles to preserve stability across personnel changes; documentation standards must address whether governance records are public documents; and sharing scope should be configured to reflect the organization's public mission. Two further governance considerations apply: cross-organizational FAI agreements between public-sector organizations may themselves be subject to freedom-of-information or equivalent disclosure laws; and non-profit organizations should use propagation restrictions to protect mission-critical governance architectures from flowing to organizations with different missions. The anti-pattern for this context is institutional governance bypass: FAI governance decisions made by individual staff without the institutional authority the organization's governance framework requires.

## 1. D2.73 as an application of domain-agnosticism

D2.44 established that the FAI governance configuration architecture does not prescribe any particular organizational form. The configurable dimensions governing joint authority, escalation routing, documentation standards, propagation restrictions, and cross-organizational agreement components are specified as substrate content within each participating Self's home governance perimeter. The content of those specifications is governed by the organization's own authority structure, not by the architecture's preferences about organizational form.

This domain-agnosticism is a feature of the architecture's design: it enables Selves operating under fundamentally different governance frameworks to participate in FAI events without requiring either party to abandon its home governance structure. A commercial enterprise and a public agency can coordinate via FAI provided each configures the relevant dimensions in conformity with its own governance requirements. The architecture does not impose a common governance model; it imposes a common structural requirement that governance be expressed as substrate content under joint authority.

D2.73 applies this commitment to the specific case of non-profit and public-sector organizations. These organizations present a cluster of governance properties that are uncommon in commercial deployments and that carry configuration implications the architecture enables but does not specify automatically. Identifying those implications is the work of this note.

## 2. Distinctive governance properties

Three properties distinguish non-profit and public-sector governance from the commercial baseline that most architecture discussions implicitly assume.

**Public accountability.** Public-sector organizations are accountable to the public or to a legally defined constituency rather than to shareholders or commercial investors. Non-profit organizations are accountable to their stated mission and, in many jurisdictions, to regulatory frameworks that govern tax-exempt status and mission fidelity. This accountability has a transparency dimension: governance decisions — including AI governance decisions — may be subject to disclosure requirements beyond what commercial organizations face. FAI governance records that a commercial organization would treat as internal documentation may, for a public-sector counterpart, be subject to freedom-of-information laws or equivalent statutory disclosure obligations.

**Institutional authority structures.** In public-sector organizations, governance authority is typically distributed across institutional roles — elected officials, appointed administrators, designated legal officers — rather than vested in identifiable individuals at will. The "who holds governance authority" question that underlies D1.25's joint authority configuration has institutional complexity in this context: authority follows the role, not the person. A named individual who holds governance authority today may not hold it after the next election, appointment cycle, or reorganization. Governance configurations that name individuals rather than roles break under normal institutional change, requiring constant maintenance and creating gaps during transitions.

**Procurement and contracting constraints.** Cross-organizational governance agreements between public-sector entities — such as the FAI agreements D2.34 formalizes — may need to follow procurement or contracting frameworks that commercial organizations do not face. Public procurement law may require competitive processes, legislative approval, or other procedural steps before cross-organizational governance commitments take legal effect. The agreement itself, not merely its subject matter, may require regulatory approval before it can bind the participating organizations.

## 3. Four configuration implications

The three distinctive properties generate four concrete implications for FAI governance configuration in non-profit and public-sector deployments.

### 3.1 Joint authority specification to institutional roles

D1.25 established that joint authority is substrate content: the specification of who holds governance authority across the shared substrate is authored within each participating Self's home governance perimeter. For public-sector organizations, this specification must identify institutional roles rather than named individuals. The joint authority configuration should name positions — Director of AI Policy, Chief Information Officer, Legal Counsel to the AI Governance Committee — rather than the persons currently occupying those positions.

This is not a stylistic preference. It is a stability requirement. Named-individual configurations require reconfiguration every time a role changes hands, which in public institutions occurs on cycles driven by election, appointment, and civil service processes rather than by operational continuity needs. Role-based configurations persist across personnel changes by design; the authority travels with the position rather than with the person. For organizations where the approval mechanics (D2.12) require board-level approval for certain FAI configurations, the configuration itself should specify the board function — e.g., "AI Governance Subcommittee of the Board of Directors" — rather than naming board members.

### 3.2 Escalation routing to institutional roles

D2.14 established that escalation routing — the configuration governing where unresolved inter-Self conflicts are sent for human resolution — is substrate content specified within the shared governance architecture. For public-sector organizations, escalation routing should target institutional roles for the same reason joint authority specification should: institutional roles persist through personnel changes; escalation pathways that route to named individuals break when those individuals leave.

An escalation configuration that routes a conflict to "the Director of Digital Services" rather than to "Jane Smith, Director of Digital Services" continues to function correctly after the current director departs, because the successor inherits the role and with it the designated escalation authority. This is the architectural implementation of the institutional principle that public governance authority attaches to offices rather than to officeholders. The escalation routing configuration for a public-sector Self should use the role title as the authoritative identifier, with current incumbency information maintained separately as a lookup outside the substrate configuration.

### 3.3 Transparency documentation standards

D2.36 established four documentation standards for FAI governance records as a minimum floor. Public-sector organizations may face statutory transparency requirements that exceed this floor. Freedom-of-information legislation, open-government mandates, legislative oversight requirements, and audit obligations specific to public institutions can all require disclosure of governance records beyond what D2.36's minimum standards produce.

The documentation standards component of the cross-organizational governance agreement (D2.34 Component 1) should address this explicitly. The agreement should specify whether FAI governance records are public documents; whether the governance records of one party are accessible to the public of the other party's jurisdiction; and whether specific categories of governance record — conflict logs, escalation records, configuration change histories — are subject to disclosure on request. This is not an architectural requirement; the architecture supports any documentation standard the governance agreement specifies. It is a governance configuration choice that, for public-sector organizations, cannot safely be left at the default minimum.

The configuration decision is binary but the implications are extensive: a governance record that is a public document is subject to disclosure requests by anyone, not only by the participating organizations. Configuration records that contain commercially sensitive information from a private-sector FAI partner may require careful scoping when one party's documentation standards include public disclosure obligations. The cross-organizational agreement should address this interface explicitly.

### 3.4 Mission-aligned sharing scope

D1.22 Dimension 1 governs sharing scope: the configuration of which aspects a Self contributes to the shared substrate during a FAI event. For non-profit and public-sector organizations, sharing scope should be configured to reflect the organization's public mission rather than uniform contribution across all aspects.

Aspects that govern mission-relevant operations — the governance architectures by which the organization carries out its core public or charitable function — often warrant broader contribution than aspects governing internal administration. An organization whose mission is public health research may configure broad sharing scope for its research coordination architecture and narrower sharing scope for its human-resources administration architecture. Mission-relevance is the natural criterion for calibrating sharing scope in mission-driven organizations, because the rationale for FAI participation is typically mission advancement rather than general operational efficiency.

The converse applies as well: aspects that the organization treats as internal administration, or that contain information subject to statutory confidentiality requirements (personal data, legally privileged communications, protected financial information), should be scoped narrowly or excluded from the sharing configuration, even if equivalent aspects in a commercial Self would be shared more broadly.

## 4. Public-sector cross-organizational agreement transparency

Cross-organizational FAI governance agreements between public-sector organizations may themselves be subject to disclosure obligations independent of the governance records they regulate. In many jurisdictions, contracts and agreements between public-sector entities are public documents accessible under freedom-of-information or equivalent legislation. The cross-organizational governance agreement (D2.34) may therefore need to be drafted as a public document from the outset.

This has several practical implications. Language in the agreement that would be unobjectionable in a confidential commercial contract — including characterizations of the other party's governance capabilities, operational vulnerabilities, or strategic priorities — may appear in public view. Participation in the agreement itself may be publicly known. Governance configurations that the participating organizations treat as sensitive may need to be separated from the agreement text proper and governed under a separate confidentiality arrangement, if applicable law permits.

Public-sector organizations entering FAI governance agreements should therefore specify in D2.34 Component 1 (mutual governance standards) whether the agreement is itself a public document; whether any components are subject to confidentiality treatment; and under what conditions the agreement or its components would be released in response to disclosure requests. This specification is a governance decision for the participating organizations and their legal counsel, not an architectural determination.

## 5. Non-profit mission protection in propagation

D2.31 Dimension B established propagation restrictions as a configurable dimension governing which governance architectures are permitted to flow outward from a participating Self to other Selves during or after FAI events. For non-profit organizations, propagation restrictions can serve an additional purpose beyond the competitive or security considerations that typically motivate them in commercial contexts: the protection of mission-distinctive governance architectures from migration to organizations with different missions.

Non-profit organizations often develop governance architectures that reflect years of institutional learning about how to operationalize a specific mission — the precise way an organization structures conflict-handling, authority delegation, and contribution scope to serve its charitable or public purpose. This mission-distinctive governance architecture may have operational value in organizations with the same mission and limited value, or actively misleading value, in organizations with different missions. Propagation to a mismatched organizational context could result in governance patterns that were designed for one mission being applied, unadapted, to an incompatible one.

Propagation restrictions configured under D2.31 Dimension B allow a non-profit Self to prevent its mission-critical governance architectures from propagating to organizations whose missions are not aligned. This is a legitimate use of the configurable propagation mechanism. The architecture does not impose any obligation to propagate; the domain-agnosticism commitment does not require indiscriminate sharing. Mission distinctiveness is a governance priority that the propagation restriction mechanism directly supports, and non-profit organizations should configure it explicitly rather than relying on a default assumption that propagation is unconstrained.

## 6. Anti-pattern: institutional governance bypass

The central failure mode for FAI governance in public-sector and non-profit organizations is institutional governance bypass: FAI governance decisions made by individual staff members operating without the institutional authority the organization's governance framework assigns to those decisions.

This anti-pattern takes several forms. A staff member configures joint authority by entering their own name rather than the relevant institutional role, effectively routing governance authority to themselves personally rather than to the position. A team reconfigures escalation routing to bypass an institutional approval process that the organization requires for AI governance decisions. A department enters a cross-organizational FAI agreement without the procurement review or board approval the organization's governance framework mandates. In each case, the FAI configuration is technically valid at the substrate level while being institutionally illegitimate at the organizational level.

The consequences of institutional governance bypass in public-sector contexts extend beyond governance quality concerns into legal and institutional risk. Decisions made without proper institutional authority may be legally invalid, exposing the organization to liability and requiring remediation that is more costly than the original process would have been. In some jurisdictions, public officials who commit their organizations without proper authority may face personal legal consequences. The FAI architecture cannot detect institutional governance bypass from within the substrate configuration — the substrate records whatever the configuring authority specifies. The protection against this anti-pattern is institutional process discipline applied at the governance layer, not at the technical substrate layer.

The remedy is the role-based configuration practice described in §§3.1 and 3.2: specifying governance authority by institutional role rather than by individual, and routing approval mechanics through the decision-making authority structure the organization's governance framework defines. When the configuration structure itself names institutional positions rather than individuals, it becomes harder to complete a configuration that bypasses institutional authority — the form of the configuration reflects the institutional structure rather than circumventing it.

## 7. Operational test

A FAI governance deployment for a public-sector or non-profit Self passes the D2.73 operational test if all of the following are true:

1. The joint authority configuration (D1.25) names institutional roles or positions as governance authorities, not named individuals. The configuration remains valid and operable without revision through a change in the person occupying any named role.

2. Escalation routing (D2.14) targets institutional roles. A conflict escalated through the routing configuration reaches the current occupant of the designated role without any configuration change being required after personnel changes.

3. The cross-organizational governance agreement (D2.34) specifies, in its Component 1 (mutual governance standards), whether the agreement is itself a public document and whether FAI governance records generated under the agreement are subject to public disclosure obligations.

4. The documentation standards configured for this deployment address, at a minimum, the public transparency requirements the organization faces — not only the D2.36 minimum floor.

5. Sharing scope (D1.22 Dimension 1) distinguishes between mission-relevant aspects and internal-administration aspects, with configuration reflecting mission relevance as a criterion.

6. For non-profit organizations: propagation restrictions (D2.31 Dimension B) have been explicitly configured with respect to mission alignment, not left at any default assumption of unconstrained propagation.

An observer reviewing a FAI event record for a public-sector Self can verify items (1) and (2) by inspecting whether governance authority identifiers in the configuration are role-designations or individual names. Items (3) and (4) are verifiable by examining the cross-organizational governance agreement's documentation-standards component. Items (5) and (6) are verifiable by examining the sharing-scope and propagation-restriction configuration records within the substrate.

## 8. Conclusion

D2.73 applies the domain-agnosticism established in D2.44 to the specific governance properties of non-profit and public-sector organizations. The architecture accommodates these organizations through the same configuration mechanisms it provides to all organizational types. What D2.73 formalizes is where those mechanisms require conscious governance decision in the non-profit and public-sector context: the joint authority and escalation routing configurations must use institutional roles rather than individuals; the documentation standards configuration must address statutory transparency obligations; the sharing scope configuration should reflect mission relevance; and the propagation restriction configuration should address mission alignment for non-profit Selves.

These are governance decisions, not architectural constraints. The architecture enables all of them through its configurable substrate-content commitment. The contribution of this note is to identify which decisions carry institutional weight in non-profit and public-sector contexts, so that deployments in those contexts are configured to the governance standard those organizations actually require rather than to a commercial default that may satisfy the architecture without satisfying the institution.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance for Non-Profit and Public-Sector Selves.* May 15, 2026. ORCID: 0009-0004-8065-3235.
