# Substrate Authoritative for "Who Has What Authority": Standalone Treatment of Authority-Structure Authority in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, in standalone form, the fifth of the five categories of substrate authoritative state — substrate authority for *who has what authority* over substrate content — so that downstream work can adopt, extend, or argue against the commitment without ambiguity.

## Abstract

The CKS pattern commits to substrate as the source of truth across five categories of authoritative state. The integrating-frame note (A2.42) established the five-category structure; companion notes A2.43–A2.46 formalize Categories 1 through 4. This note formalizes Category 5 — substrate authority for *who has what authority* — as the fifth and final category. The commitment is to substrate authority over the deployment's authority structure: the record of which humans hold which of the three rights (inspect, modify, override) over which substrate scopes, with authoring provenance, applicability scope, and version history all substrate-resident. The note distinguishes Category 5 from four adjacent patterns commonly conflated with it (identity-provider-as-authoritative, RBAC-system-as-authoritative, OAuth/SAML-scopes-as-authoritative, organizational-directory-as-authoritative), names ten failure modes that violate the commitment, and provides an operational test for whether a system's authority-structure authority is CKS-coherent.

## 1. Why Category 5 needs to be formalized as standalone

The parent foundational note A1.08 commits to substrate as source of truth across five categories of authoritative state. The integrating-frame note A2.42 established the five-category structure with severable specialization; companion notes A2.43, A2.44, A2.45, and A2.46 formalize Categories 1 through 4. This note formalizes Category 5 — authority-structure authority — as having independent architectural content with particular weight on the substrate's authority over the deployment's governance structure.

The motivating cases are deployments where authority structure is enforced operationally but external identity systems are treated as authoritative for who has what authority: substrates that record authority assignments while external identity providers (Active Directory, Okta, LDAP) are queried for current authority status; substrates that carry role definitions while external role-based access control (RBAC) systems are authoritative for role-to-user mappings; substrates that record authority changes while external HR systems are treated as the official authority registry; substrates that operate over authority structure while external authorization services determine at runtime whether specific operations are permitted. Each pattern fragments authority in ways that fail the architectural commitment. Public formalization of Category 5 forecloses these architectures as derivable inventions; patentable derivations focused on AI-governance authority architectures, decision-authority systems, or authority-management patterns are substantially more defensibly contested when Category 5 is named as a standalone commitment.

Two compositional relationships clarify why the commitment is independently necessary. First, A1.01 (the human-governed commitment) commits to human governance through the three rights — inspect, modify, override — with authority-not-labor as the operative framing. A2.47 commits to substrate being architecturally authoritative for the structure A1.01 specifies. The two compose strictly: human governance must operate through the three-rights structure (per A1.01) AND substrate must be architecturally authoritative for the structure (per A2.47). An implementation that satisfies A1.01 nominally — humans hold the three rights — but holds the authoritative record of who holds them in external identity systems has human governance without substrate-authoritative governance. Second, A2.38 commits to authority context being recorded for every substrate write; for human writes, the authority context resolves into the writer's position in the authority structure. Without Category 5, A2.38's authority-context references would resolve to authority structure held in external systems, breaking the substrate-only paths formalized in A2.41.

## 2. The Category 5 commitment, defined precisely

State the commitment as four operational components.

**(a) The substrate is the architectural answer to authority-structure queries.** For queries about the deployment's governance — which humans participate in the authority structure, what rights each human holds, over which substrate scopes, when authority was granted or modified, under what authorization — the architectural answer is the substrate's record together with the six provenance fields specified in A2.40. External systems may be consulted for operational efficiency, visualization, or runtime convenience, but the substrate's answer is the authoritative answer when the two disagree.

**(b) The authority structure is substrate content across four dimensions.** The substrate carries the complete record across four operational dimensions. Each dimension is independently load-bearing; an implementation authoritative for some dimensions but not others fails the commitment.

- *Identity.* Which humans participate in the deployment's authority structure — the set of authority-holders. Identity providers and HR systems may carry many other attributes about humans (employment status, contact information, organizational position) that are not part of the authority structure; the architectural commitment does not extend to those attributes.

- *Rights.* Which of the three rights from A1.01 — inspect, modify, override — each human holds. The three rights themselves are formalized in A2.01, A2.02, and A2.03 as standalone architectural commitments; Category 5 makes substrate authoritative for which humans hold which of them.

- *Scope.* Over which substrate scopes each right applies. A human may hold modify rights over some substrate content (a business-rules cell, for example) and only inspect rights over other content (a regulatory-compliance cell). Partial-scope coverage in substrate, with the rest in external systems, fails the commitment.

- *Version history.* How the authority structure has evolved over time. Each authority-structure change is itself a substrate write committed per A2.10 with the six provenance fields per A2.40 — writer attribution, timestamp, antecedent reference, rationale where required, applicable rule reference, and relationship metadata where applicable. Current-state-only authority records, with history held externally, fail the commitment.

**(c) New authority assignments and authority changes are committed to substrate first.** When humans authorize an authority change — granting a right, revoking a right, modifying scope, adding or removing humans from the authority-holder set — the change is committed to substrate first per A2.10 with the six provenance fields per A2.40. External identity providers, role-management systems, and authorization services update downstream from substrate. Substrate-first ordering is what preserves substrate-only paths per A2.41, since the authoritative record exists in substrate before any external system has been notified.

**(d) Disagreements between substrate and external sources are resolved by substrate.** When substrate's authority structure and external sources' authority records disagree — different rights, different scope, different identity, different effective dates — substrate prevails. The architectural commitment is to update external sources to match substrate, not the other way around.

A system that satisfies fewer than all four components cannot reliably claim Category 5 authority, even if its authority-enforcement functions operate without observable failure at runtime.

## 3. What the commitment does NOT claim

The commitment is precise; misreading it as broader than it is inflates the prior-art claim and weakens defensibility.

**(a) Not authority over authentication infrastructure.** Runtime authentication infrastructure — identity providers, single sign-on systems, multi-factor authentication services — is operational and not Category 5 content. A deployment may use enterprise identity infrastructure for authentication; the infrastructure determines whether a claimed identity is verified, while substrate determines what authority that authenticated identity holds. The two commitments are orthogonal and compose without conflict.

**(b) Not all human attributes in substrate.** Identity providers and HR systems may carry many attributes about humans (employment status, contact information, organizational position, security clearance) that are not part of the authority structure. The architectural commitment is to substrate authority over the authority structure, not over all human attributes a deployment may track.

**(c) Not a specific authority-structure schema.** Implementations may represent the authority structure in any of the canonical schema families — role-based access control (RBAC), attribute-based access control (ABAC), relationship-based access control (ReBAC), capability-based systems, matrix-based assignments, or graph representations — provided the representation satisfies the four dimensions and operates as substrate content. The architectural commitment is technology-agnostic on schema choice; it commits only to where the authority record lives and what it covers.

**(d) Not human-mediation at execution time.** Per A2.04, rule authoring is itself a governance moment. Rules may automate certain authority-structure changes — automatic role grants on substrate-defined triggers, time-bound authority expirations, scope adjustments based on substrate state. The architectural commitment requires that the authority structure remain substrate content and that changes be governed by humans through rule authoring, not that every change be human-mediated at execution time.

**(e) Not absence of external identity systems.** Deployments may use enterprise identity providers, single sign-on systems, role-management platforms, and authorization services. The architectural commitment is that these systems are derivative; they may add operational value but cannot substitute for substrate authority over the authority structure.

**(f) Not a specific retention policy.** The authority structure persists in substrate per A2.08; how long deployments retain old authority-structure versions is a deployment concern. Category 5 authority holds for as long as substrate carries the authority structure.

## 4. What the commitment is NOT

Distinguish from four adjacent patterns commonly conflated with it.

**Not identity-provider-as-authoritative.** Some implementations use enterprise identity providers (Active Directory, Okta, LDAP) as the authoritative source for authority structure. The provider carries identities, group memberships, and role assignments; substrate may carry references but the provider is the source. This pattern fails the commitment because authority resolution requires consulting external infrastructure, breaking substrate-only paths per A2.41.

**Not RBAC-system-as-authoritative.** Some implementations use specialized RBAC platforms as the authoritative authority registry. Substrate operates under RBAC enforcement but does not carry the authority structure itself; the architectural authority is in the RBAC platform, even when the rights and scopes the platform enforces are nominally drawn from CKS commitments.

**Not OAuth/SAML-scopes-as-authoritative.** Some implementations use OAuth or SAML token scopes to convey authority at runtime, with the token-issuing identity provider treated as authoritative for which scopes a user has. Substrate reads scopes from tokens but does not carry the authority structure itself; the token issuer, not substrate, is the architectural authority.

**Not organizational-directory-as-authoritative.** Some implementations use organizational directories (HR systems, enterprise resource planning systems) as authoritative for who has what authority based on organizational position. Substrate may carry references to directory entries but the directory is the source; authority follows organizational hierarchy held externally rather than substrate-resident authority commitments.

## 5. Why Category 5 is load-bearing for downstream commitments

Category 5 is load-bearing for several CKS commitments. For the integrating source-of-truth commitment from A1.08, Category 5 makes substrate authoritative for one of the five categories; without it, source-of-truth would be partial — substrate authoritative for state, history, conflicts, and rules but not for who has authority over them. For the human-governed commitment from A1.01, Category 5 makes substrate architecturally authoritative for the three-rights structure A1.01 commits to; without it, A1.01 could be satisfied operationally while external systems are authoritative for the authority record itself. For the three-rights decomposition from A2.01–A2.03, Category 5 ensures the rights are not only defined in substrate but also assigned in substrate, preserving symmetry between rights definition and rights assignment. For the accountability question "under what authority" from A2.38, Category 5 ensures authority-context references for human writes resolve through substrate, preserving substrate-only paths per A2.41. For the non-specialist governance commitment from A1.11, Category 5 ensures the authority structure is accessible through commodity tools rather than requiring specialist tooling to interface with external identity infrastructure.

## 6. Failure modes that violate the commitment

Each failure mode names a way an implementation can fail the architectural commitment.

**(a) Identity-provider-primary.** The deployment treats an enterprise identity provider as the official authority registry; substrate carries references but is not authoritative.

**(b) RBAC-system-primary.** A specialized RBAC platform is treated as the authoritative authority registry; substrate operates under RBAC enforcement but does not carry the authority structure.

**(c) OAuth-token-scope-primary.** OAuth or SAML tokens convey authority at runtime; the token issuer is authoritative for scope; substrate reads scopes but does not carry the authority structure.

**(d) HR-system-driven authority.** The deployment derives authority from HR-system position; HR records are authoritative for who has what authority based on organizational role.

**(e) Substrate-summary-external-detail.** Substrate carries high-level role assignments; external systems carry scope details and per-content permission grants. Substrate authority is partial.

**(f) Authority-version-history-external.** Substrate carries current authority assignments; version history of authority changes lives in external audit logs or identity-provider history. Substrate authority is current-state-bound.

**(g) Authority-resolution-at-runtime.** Authority is resolved at runtime by external authorization services that consult multiple sources (identity provider, RBAC system, organizational directory) to determine whether a specific operation is permitted. Substrate is one input among several rather than the architectural answer.

**(h) External-authority-changes.** Authority changes occur in external identity systems and propagate to substrate downstream. The substrate's authority record lags external changes and depends on external systems for currency.

**(i) Group-membership-as-substitute.** Authority is conveyed through group memberships managed in external identity infrastructure; substrate references groups but does not carry the authority structure that the groups represent.

**(j) Token-scope-overrides.** Tokens issued by external identity infrastructure can carry scopes that override substrate authority for specific operations or sessions. Substrate authority is overridden by token-conveyed authority.

## 7. Operational test

A system satisfies the Category 5 commitment if and only if all of the following are true at all times during the substrate's existence.

1. Queries about the authority structure — which humans hold which rights over which substrate scopes, when authority was granted or modified, under what authorization — are answered authoritatively from substrate per A1.01 and the six provenance fields per A2.40.

2. The substrate carries the complete authority structure across all four dimensions, tested individually:
   - (2.i) *Identity completeness:* the full set of authority-holders is in substrate; none are recorded only externally.
   - (2.ii) *Rights completeness:* which of the three rights each human holds is in substrate; no rights mappings are external-only.
   - (2.iii) *Scope completeness:* the substrate-scope each right applies over is in substrate; no scope details are external-only.
   - (2.iv) *Version-history completeness:* the history of authority-structure changes with provenance is in substrate; no version history is held only in external audit logs or identity-provider histories.

3. New authority assignments and authority changes are committed to substrate first per A2.10's boundary crossings; external identity providers, role-management systems, and authorization services update downstream from substrate.

4. When substrate and external sources disagree on the authority structure, the deployment resolves in favor of substrate; external sources are updated to match substrate, not the other way around.

5. Authority resolution — determining whether a specific human holds a specific right over specific substrate content — operates from substrate alone for the architectural answer; runtime authorization services may participate in operational enforcement but do not determine the authoritative answer.

6. The authority structure is queryable from substrate alone through standard read operations per A2.25 Requirement 2 and substrate-only paths per A2.41.

A system that fails any of (1)–(6) does not satisfy the Category 5 commitment in the architectural sense, even if its authority-enforcement functions operate without observable failure at runtime.

## 8. Why naming Category 5 as standalone matters

Implementations under pressure to integrate with enterprise identity infrastructure, leverage existing authorization services, or support sophisticated runtime authority features consistently drift toward authority being held in external systems. The drift is steady because enterprise identity infrastructure is operationally familiar, organizationally established for authentication and authorization, and often regulatory-mandated. Each individual integration is locally rational; the cumulative effect is fragmentation of authority across substrate and a lengthening tail of external systems treated as architecturally authoritative for parts of the authority structure. The downstream consequences manifest as governance failures (humans cannot exercise meaningful governance over an authority record they cannot authoritatively access from substrate), accountability failures (the "under what authority" question per A2.38 cannot be answered from substrate alone for human writes), retraceability failures (authority-structure changes trace through substrate but the authoritative current authority is elsewhere), and source-of-truth fragmentation (substrate authoritative for Categories 1, 2, 3, 4 but external systems authoritative for Category 5).

Naming Category 5 as a standalone architectural commitment — with the four components in section 2, the limitations in section 3, the four adjacent-pattern distinctions in section 4, the load-bearing connections in section 5, the ten failure modes in section 6, and the operational test in section 7 — gives downstream implementers a precise specification of what substrate authority over the authority structure requires. With this note complete and its companions A2.43, A2.44, A2.45, A2.46 already drafted, the five authoritative categories are fully formalized as standalone commitments. The subsequent note A2.48 specializes the source-of-truth-vs-mirror-of-truth distinction; with A2.48 complete, the source-of-truth decomposition will be fully formalized.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Substrate Authoritative for "Who Has What Authority": Standalone Treatment of Authority-Structure Authority in the Coordination Knowledge Substrate Pattern.* May 4, 2026. ORCID: 0009-0004-8065-3235.
