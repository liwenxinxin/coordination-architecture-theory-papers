# Vendor-Revocable Governance: An Anti-Pattern Formalization for the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** 6 May 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one anti-pattern — *vendor-revocable governance* — as a standalone failure mode of the source paper's "human-governed" commitment, with an explicit specification of what the failure consists of, which architectural commitments it violates, and what architectural correction is required.

## Abstract

The CKS pattern's foundational "human-governed" commitment names three rights — to inspect, to modify, and to override substrate content and orchestration rules — as exercisable at any time during the substrate's existence. The commitment is *architectural*: the rights must be available as a property of the system's design, not as a procedural promise that depends on a particular vendor, deployment, or workflow (§3.3, §6.3). This note formalizes the canonical failure of that commitment at the AI-infrastructure-vendor boundary. *Vendor-revocable governance* is the anti-pattern in which the deployment's exercise of the three rights is operationally contingent on the AI infrastructure vendor's continued cooperation: terms-of-service revisions, account suspensions, infrastructure modifications, vendor-side configuration changes, or platform-level policy enforcement can each, at vendor discretion, disable inspection, modification, or override. The rights appear architecturally exercisable but are not. The note specifies the anti-pattern as four operational components, identifies seven CKS commitments it violates, traces the failure mode, names the three-commitment architectural correction (substrate portability per the source paper's tool-agnosticism commitment, authority-structure substrate-residence per the source paper's source-of-truth commitment, governance exercisable through architectural mechanisms the vendor cannot remove), distinguishes the anti-pattern from four adjacent patterns commonly conflated with it, and provides an operational test with three sharpening properties.

## 1. Why vendor-revocable governance needs to be formalized as standalone

The source paper commits the human-governed property to architectural availability of the three rights at any time, not to procedural availability under particular conditions (§3.1, §3.3, §6.3). The two qualifiers — *architectural* and *at any time* — are what make the commitment portable across deployments and what distinguish it from review-workflow or compliance-procedure framings of governance.

Both qualifiers fail in a specific, common, and architecturally regular way at the AI-infrastructure-vendor boundary. A deployment whose substrate is hosted on commercial AI infrastructure typically inherits the vendor's discretion over a wide class of operational decisions: which features remain available, which user accounts retain access, which interfaces continue to function, which terms of service apply, which configurations the vendor enforces. When any of these decisions can in principle reach the user's exercise of the three rights, the rights are vendor-discretionary even when they are operationally available at the moment. The deployment looks human-governed; under revocation, it is not.

Naming this failure mode as a standalone anti-pattern serves three purposes. It gives downstream implementers a precise specification of the failure to avoid. It separates the failure from legitimate vendor-hosted deployments that preserve the architectural commitment through portability and authority residence. And it formalizes, as public prior art, the architectural distinction between governance held as an architectural property and governance held as a vendor-provided feature — a distinction load-bearing for any work that would compose CKS deployments with commercial AI infrastructure.

The failure is also upstream of several subsequent anti-patterns. When the foundational governance commitment is conditional on vendor cooperation, downstream commitments that rest on it — source-of-truth integrity at the authority layer, composition coherence across substrate boundaries, tool-agnosticism in the operational sense — become conditional too.

## 2. The anti-pattern, defined precisely

A deployment exhibits **vendor-revocable governance** when the AI infrastructure vendor — the provider of the platform, hosting environment, or operational layer on which the CKS substrate is deployed — can revoke the deployment's exercise of the three rights through vendor-discretionary mechanisms, in a manner the deployment's architecture provides no recourse against. The anti-pattern decomposes into four operational components.

**(a) Vendor-discretionary right revocation.** The deployment configuration permits the vendor to revoke the user's exercise of the inspect, modify, or override rights through unilateral mechanisms — terms-of-service changes restricting access, account suspensions denying access, infrastructure modifications removing operational paths, platform-level policy enforcement overriding user decisions, vendor-side configuration changes affecting governance operationally. The rights appear architecturally exercisable but their continued exercise is contingent on vendor permission.

**(b) Vendor-provided governance interfaces with vendor-removability.** The interfaces through which the rights are exercised — read paths, write paths, override paths, authorization mechanisms — are vendor-provided and vendor-removable. If the vendor removes or alters the interface, the user can no longer exercise the rights operationally even if architecturally entitled. The interface, not the architecture, becomes the binding constraint.

**(c) Vendor-controlled authority structure.** The structure determining who has which rights over which substrate content is held in vendor-controlled configuration — vendor account settings, vendor identity systems, vendor permission models — rather than as substrate content. The vendor can modify the authority structure through configuration changes the substrate has no record of and no authority over.

**(d) Vendor-locked substrate hosting.** The substrate is hosted on vendor-controlled infrastructure with no architectural provision for portability to alternative hosts. If vendor revocation occurs, the user cannot port the substrate to alternative infrastructure to preserve governance; the substrate is locked into the vendor relationship as a deployment-level fact, not only as a convenience-level one.

A deployment that exhibits any one of (a)–(d) partially exhibits the anti-pattern. A deployment exhibiting all four exhibits it fully. The four components are operationally inspectable; deployment review can identify each independently.

## 3. Which CKS commitments are violated

Vendor-revocable governance violates seven CKS commitments, each through a specific mechanism that traces to vendor revocability rather than to vendor involvement per se.

**(i) The human-governed commitment (§3.1).** The foundational commitment to human authority over substrate content is conditional on vendor cooperation rather than architecturally guaranteed. The commitment fails at its load-bearing layer.

**(ii) The architectural-property qualifier (§3.3, §6.3).** The source paper distinguishes architectural commitments — which hold by design and cannot be disabled without breaking the architecture — from procedural promises that depend on a particular vendor, deployment, or workflow. Vendor-revocable governance treats the rights as vendor-discretionary features, which is the architectural failure the qualifier specifically preempts.

**(iii) The temporal-property qualifier (§3.3).** The commitment to the rights being exercisable *at any time* fails when the vendor can revoke the rights at the vendor's chosen time. The temporal property requires governance to be exercisable architecturally at any moment, not at any moment the vendor permits.

**(iv) The three rights individually.** The inspect right is compromised when the vendor restricts read access; the modify right is compromised when the vendor restricts write access or removes write interfaces; the override right is compromised when vendor policies override user decisions or vendor account control denies access entirely. Each right's standalone integrity, not only the joint commitment, fails under revocation.

**(v) The substrate-as-source-of-truth commitment (§11.3).** The substrate is the authoritative store for "who has what authority" over substrate content. Vendor-controlled authority structure means the source-of-truth migrates to vendor configuration; the substrate is no longer authoritative for the authority layer.

**(vi) The composition commitment, Requirement A — per-substrate human governance preservation.** Compositions involving the substrate must preserve per-substrate governance. The vendor-host relationship is a composition where the substrate composes with vendor infrastructure; vendor-revocable governance fails Requirement A at this composition, because the substrate's human governance is not preserved when the vendor revokes it.

**(vii) The tool-agnosticism commitment (§7.1).** The commitment to substrate operating across host environments that satisfy the three minimal requirements — persistent state, human read/write access, LLM access — is operationally undermined when the substrate is locked into a vendor relationship from which it cannot port. Tool-agnosticism in the architectural sense requires that the substrate *can* move across qualifying hosts; vendor-locked hosting denies this.

The seven violations are not redundant. Each names a distinct architectural property that vendor revocability specifically compromises.

## 4. The failure mode

Vendor-revocable governance produces deployments that present as human-governed under normal vendor operation and reveal their failure mode only under vendor revocation. The downstream consequences are operationally specific.

**Apparent governance is conditional.** Users exercise the three rights through vendor-provided interfaces and observe that the exercise works — until the vendor revokes it, at which point the apparent governance disappears as a deployment property. The architecture provides no test that distinguishes architectural governance from vendor-discretionary governance during normal operation.

**Architectural commitments fail at the moment of revocation.** When the vendor revokes governance — through ToS update, account suspension, infrastructure change, or policy enforcement — the foundational commitment fails at the deployment level. The user has no architectural recourse, because the rights were vendor-discretionary, not architectural.

**The substrate becomes ungovernable.** After revocation, substrate content may persist as data while becoming unreachable as substrate. The rights to inspect, modify, or override that content are no longer exercisable through any path the architecture authorized; the substrate is operationally retired from governance even when it remains physically present.

**Source-of-truth migrates to vendor configuration.** Because the authority structure was vendor-controlled, the operational source-of-truth for "who can do what to substrate content" was the vendor's configuration system, not the substrate itself. After revocation, this migration becomes legible: the substrate's source-of-truth status was always conditional on vendor permission.

**Composition coherence breaks at the vendor boundary.** Subsequent compositions involving the substrate may operate normally at the cell level while being incoherent at the foundational composition with vendor infrastructure. Requirement A holds within the deployment but fails at its outer boundary, and recovery typically requires the vendor's cooperation rather than any path the user controls unilaterally.

## 5. The architectural correction

The architectural correction operates through three foundational commitments together. None alone suffices; their joint operation is what closes the failure mode.

**Substrate portability per the tool-agnosticism commitment (§7.1).** The substrate's host environment must satisfy the three minimal requirements — persistent state across cell runs and human-governance moments, human read/write access through architecturally guaranteed interfaces, LLM access through standard protocols — and the user must be able, in practice and not only in principle, to port the substrate to an alternative host that also satisfies these requirements. The portability path must be exercisable without vendor cooperation. A deployment that satisfies tool-agnosticism nominally but cannot operationally port if the vendor revokes is not corrected.

**Authority-structure substrate-residence per the source-of-truth commitment (§11.3).** The structure that determines who has which rights over which substrate content is encoded as substrate content, not as vendor configuration. When the substrate ports to alternative infrastructure, the authority structure travels with it as substrate content; vendor revocation of vendor-side configuration does not modify the authority structure, because the structure is not held vendor-side. The substrate's authoritative role for "who has what authority" is preserved across host transitions.

**Architectural exercisability of the three rights.** The rights are exercisable through mechanisms the vendor cannot remove without breaking the host's compliance with the three minimal requirements. Standard substrate interfaces — direct read, direct write, direct override over substrate content held in inspectable form — are the load-bearing path. Vendor-provided enhancements (specialized UIs, API conveniences, integrated tooling) may complement these but cannot substitute for them. Vendor revocation of vendor-provided enhancements still leaves the architectural rights exercisable through the standard path.

A correctly architected deployment additionally maintains operational portability paths — tested in practice, not only documented — and reviews vendor-relationship terms to verify that no vendor mechanism in scope can compromise the three rights, the temporal property, or the architectural property.

## 6. What vendor-revocable governance is NOT

Four adjacent patterns are commonly conflated with this anti-pattern. Naming each precisely is what keeps the anti-pattern's content sharp.

**Not vendor-hosted deployment with proper portability.** Vendor hosting per se is not the anti-pattern. A deployment hosted on commercial AI infrastructure that maintains substrate portability per §7.1, authority-structure substrate-residence per §11.3, and architectural exercisability of the rights satisfies the architecture, even when the day-to-day operational locus is on vendor infrastructure. The relevant question is what happens under revocation, not where the substrate lives during normal operation.

**Not enterprise-managed deployment with internal authority structure.** Deployments managed within an enterprise — where the enterprise plays an operational role analogous to a vendor — are not vendor-revocable governance when the authority structure is substrate-resident and the deployment maintains architectural portability. The architectural commitments are what distinguish governed from revocable.

**Not multi-tenant deployment with isolated authority.** Multi-tenant infrastructure where each tenant's substrate maintains an isolated, substrate-resident authority structure is not vendor-revocable governance, provided the multi-tenant boundary preserves the three rights for each tenant's authorized humans. The shared infrastructure is incidental; the architectural property is held per-tenant at the substrate layer.

**Not vendor partnership with contractual governance guarantees.** Contractual guarantees correct the anti-pattern when they bind the vendor to architectural commitments — maintaining the three minimal requirements, authority-substrate residence, and architectural exercisability of the rights. Contractual guarantees that bind only operational practices (uptime, response time, support availability) without binding the architectural commitments do not correct the anti-pattern; they constrain its frequency without changing its architecture.

## 7. Operational test

A deployment exhibits vendor-revocable governance if any of the following are true at any time during the deployment's existence.

1. The vendor can revoke any of the three rights — inspect, modify, override — through vendor-discretionary mechanisms (ToS changes, account suspension, infrastructure modification, policy enforcement) without architectural recourse for the user.

2. The vendor can remove the governance interfaces through vendor-discretionary mechanisms, leaving the user without operational means to exercise the rights even if architecturally entitled.

3. The structure determining who has which rights over which substrate content is held in vendor-controlled configuration rather than as substrate content.

4. The substrate cannot be ported to alternative infrastructure satisfying the three minimal requirements without vendor cooperation.

Three sharpening properties operationalize the test for deployment review.

*Revocation-mechanism inspection.* The reviewer enumerates the mechanisms by which the vendor can affect the three rights — ToS clauses, account-control policies, infrastructure-modification rights, policy-enforcement provisions — and identifies whether any reach the rights at the architectural layer.

*Host-portability test.* The reviewer verifies operationally that the substrate can be ported to an alternative host satisfying the three minimal requirements within a reasonable time, without vendor cooperation. Verification is by exercise, not by documentation.

*Authority-structure substrate-residence verification.* The reviewer verifies that the structure for "who has what authority over what substrate content" is held as substrate content — readable through the inspect right, modifiable through the modify right — and not as vendor-side configuration the substrate has no record of.

A deployment that fails any of (1)–(4), confirmed by any of the three sharpening properties, exhibits the anti-pattern. **In one sentence:** if a deployment's exercise of the three rights can be operationally revoked by the AI infrastructure vendor through vendor-discretionary mechanisms, and the substrate cannot port to alternative infrastructure satisfying the three minimal requirements without vendor cooperation, the deployment exhibits vendor-revocable governance and the architectural commitment to human-governed fails at the vendor-relationship boundary.

## Conclusion

Implementations under pressure to deliver AI coordination systems on commercial infrastructure consistently default to vendor-revocable governance, because commercial platforms are economically structured to maintain revocability for their own operational reasons. The drift is steady because audiences understand "we use vendor X for our AI infrastructure" as a deployment choice without recognizing the architectural consequence — that the foundational human-governed commitment becomes conditional on vendor cooperation absent deliberate correction.

Naming the anti-pattern as standalone gives downstream readers a precise specification of the failure mode and the three-commitment architectural correction that closes it. Subsequent work that adopts, extends, composes, or argues against the CKS human-governed commitment in deployments involving AI infrastructure vendors should use *vendor-revocable governance* in the sense formalized here. Subsequent work that uses the term differently is naming a different failure, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Vendor-Revocable Governance: An Anti-Pattern Formalization for the Coordination Knowledge Substrate Pattern.* 6 May 2026. ORCID: 0009-0004-8065-3235.
