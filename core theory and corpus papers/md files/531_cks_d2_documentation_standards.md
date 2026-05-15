# FAI Event Documentation Standards

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

It does not introduce new axioms. Its contribution is to derive, from D1.02's six Paper 1 commitments as they apply at inter-Self scope and from D2.18's seventeen record categories, the four minimum standards that FAI event governance records must satisfy to constitute externally auditable documentation.

---

## Abstract

D2.18 established seventeen record categories that constitute a complete FAI event governance record. Having categories is necessary but not sufficient for auditability: a record set whose entries exist in form but fail to meet minimum quality conditions cannot support external audit. This note formalizes four documentation standards that every record in the set must satisfy: (1) format accessibility — records must be readable by governance practitioners without specialized technical knowledge; (2) attribution completeness — every record must carry the six provenance fields established in D2.03; (3) mutual accessibility — within the shared substrate, all participating Selves' governance must be able to access records under the inspect right; and (4) retention period specification — the persistence policy must name a retention period for every Locus 2 record, with violation records subject to indefinite retention that overrides normal persistence-policy expiry. The four standards apply differentially to shared-substrate and home-substrate record categories. Records that exist in form while failing one or more standards instantiate governance theater — the documentation-level anti-pattern in which the appearance of documentation is present but the substance that supports genuine audit is absent.

---

## 1. D2.36 as Operational Decomposition of D1.02 and D2.18

D2.36 derives from two prior derivation nodes.

D1.02 carries forward the six Paper 1 architectural commitments to inter-Self scope: the substrate-as-source-of-truth commitment (A1.08), the path retraceability commitment (A1.07), the non-specialist governance commitment (A1.11), the persistence policy commitment (D1.04/A1.08), the conflict preservation commitment (Claim 3), and the inspect right as a property of the shared substrate. At inter-Self scope, each commitment has a documentation consequence: if governance records are substrate content, then the commitments that govern substrate content govern governance records. D1.02's derivation is therefore the prior-art foundation for all four standards this note formalizes.

D2.18 specified the seventeen categories that together constitute a complete FAI event governance record. Those categories span two distinct scopes — shared-substrate records produced during and after the event under joint authority, and home-substrate records produced within each participating Self's home governance perimeter. Having all seventeen categories populated means the event left a record of the right shape. It does not mean the records within those categories are adequate for external audit. D2.18 supplied the categories; D2.36 supplies the quality conditions.

The derivation question D2.36 answers is: *what properties must a record satisfy, beyond existing and falling into the right category, for the governance record set to constitute externally auditable documentation?*

---

## 2. The Four Documentation Standards

Four standards are necessary and jointly sufficient. Each inherits from a distinct Paper 1 commitment.

### Standard 1 — Format Accessibility

Every governance record must be in a format that governance practitioners without specialized technical knowledge can read and interpret directly. This standard inherits from Paper 1's A1.11 non-specialist governance commitment (see also the derivation note *Authority, Not Labor*, §5: "the rights are available to anyone who can read and write the substrate, not only to designated reviewers operating inside a specialized governance runtime").

The non-specialist governance commitment applies to governance activity during system operation. Format accessibility is the documentation-register application of that same commitment: a governance practitioner who holds the inspect right over the shared substrate must be able to read the governance records that document what happened in the substrate. A record authored in a format that requires a developer toolchain, binary decoder, platform-specific interpreter, or proprietary viewer to be read fails Standard 1 even if its content is technically complete and technically correct. Completeness within an opaque format does not satisfy the accessibility that governance authority requires.

The standard is satisfied by records authored in plain text, structured plain text, or widely legible structured formats (such as JSON or YAML rendered without specialized viewers) — formats in which the record's content is directly available to any person with access and appropriate permissions, without additional tooling. The test is not the format type as a category; the test is whether a governance practitioner can exercise the inspect right against the record's content by reading it.

### Standard 2 — Attribution Completeness

Every governance record must carry the six provenance fields established in D2.03, which formalizes Paper 1's A1.07 path retraceability commitment at the level of individual substrate entries: (a) what the record is — its type and scope; (b) who authored it — the person or automated process acting under authorization; (c) who authorized it — the human authority under which the record was produced; (d) when — the timestamp that makes the record's position in the event's sequence determinable; (e) why — the rationale or trigger that caused this record to be produced; and (f) what came before — the antecedent record or event state from which this record derives.

No record may be present in the governance record set with any of the six fields absent or empty. A record present in the correct category (D2.18) but missing its authorization field, its timestamp, or its antecedent reference is an incomplete record. An incomplete record creates a gap in the path that an external auditor must be able to retrace. Gaps in path are not a problem of degree — they are a property that makes the path either retraceable or not. Standard 2 admits no partial credit: all six fields must be present for every record in the set.

### Standard 3 — Mutual Accessibility

For records within the shared substrate — that is, records falling under D2.18's Phases 1 through 3 — all participating Selves' governance must be able to access those records under the inspect right. This standard inherits from the inspect right as formalized under Claim 3 (human-governed authority) and from the joint-authority property of the shared substrate (Paper 3, §4).

The shared substrate during an FAI event is jointly governed: no participating Self's governance holds exclusive authority over it, and no record within it is the exclusive property of the Self whose governance produced it. A record that is readable by the initiating Self's governance but not by the other participating Selves' governance violates the joint-authority property. It also violates the inspect right: if a governance practitioner from a participating Self cannot read a record within the shared substrate, that record is not operating under the shared substrate's governance properties — it is operating under unilateral governance disguised as shared-substrate governance.

Standard 3 applies specifically to shared-substrate records. Home-substrate records (D2.18 Phase 4) are governed within each Self's home authority structure. Standard 3 applies to home-substrate records only to the extent that cross-organizational governance agreements (D2.34) specifically extend inspect-right access across organizational perimeters.

### Standard 4 — Retention Period Specification

The persistence policy (D1.04/D2.02) must explicitly specify a retention period for every Locus 2 record. Records with no specified retention period may be deleted through normal lifecycle management without governance accountability, since there is no authoritative specification of how long they should persist. A governance record set with unspecified retention for any of its categories is a governance record set whose completeness at audit time is not architecturally guaranteed.

Standard 4 includes one categorical override: violation records (D2.28) have indefinite retention. The persistence policy may not specify a retention expiry for violation records. This override is not a preference or a default — it is a constraint on the persistence policy's valid configuration space. Violation records must survive normal retention-policy expiry because their purpose extends beyond the event's operational lifecycle: they support post-event investigation, cross-organizational accountability, and institutional learning about governance failures. A violation record that expires before an audit need arises has ceased to exist precisely when its value is highest. The indefinite retention requirement forecloses persistence-policy configurations that would allow that outcome.

---

## 3. Applying the Standards to the Seventeen Record Categories

D2.18's seventeen categories divide into two scopes, and the four standards apply with different scope-specificity to each.

**Shared-substrate records (D2.18 Phases 1–3)** include: the event configuration record; each participating Self's contribution scope record; the joint-authority establishment record; each contributed aspect's provenance record; the shared substrate construction record; conflict records for each conflict surfaced during the event; conflict resolution or preservation records; the event dissolution record; the persistence-policy specification; and the durable-record retention configuration. All four standards apply to every record in this group. Standards 2 and 3 carry particular weight: attribution completeness is the mechanism by which joint-authority events remain reconstructable from records alone, and mutual accessibility is the mechanism by which the joint-authority property of the shared substrate extends to the records that document it.

**Home-substrate records (D2.18 Phase 4)** include: each participating Self's ingestion record; the evolution-feed annotation records produced from preserved conflicts; each Self's DNA evolution authorization record; and each Self's action-feedback evolution record from event content. Standards 1, 2, and 4 apply to every record in this group. Standard 3 applies conditionally — only where cross-organizational governance agreements (D2.34) extend inspect-right access to partner Selves for specific record categories.

The differential application of Standard 3 is not a weakening of the mutual accessibility requirement. It reflects the architectural distinction between the shared substrate (joint authority by design) and each Self's home substrate (home authority by design). Home-substrate governance records are governed within each Self's authority structure. Standard 3's force at the home-substrate level is the force of D2.34 cross-organizational agreements, which are themselves governance-configured substrate content.

---

## 4. Documentation Standard Failure Modes

Each standard has a characteristic failure mode. Naming failure modes precisely is necessary for external auditors to identify deficiencies in governance record sets.

**Standard 1 failure — opaque format.** A record exists in the correct category, with complete attribution and correct retention specification, but is authored in a format that requires specialized tooling to read. Governance practitioners exercising the inspect right cannot access the record's content without developer assistance. The record passes category and attribution checks but fails the non-specialist accessibility the architecture requires. This failure mode is common in deployments where governance records are produced as automated outputs of technical processes that were not designed with governance practitioner access as a requirement.

**Standard 2 failure — incomplete provenance.** A record exists in the correct category and readable format, but one or more of the six attribution fields is absent. The most common variants are: records with no authorization field (produced by automated processes not explicitly authorized under a named rule); records with no antecedent reference (stand-alone entries that cannot be connected to the event state they document); and records with no timestamp (present in the record set but not placeable in the event's sequence). Each variant breaks path retraceability at a different point in the chain.

**Standard 3 failure — asymmetric accessibility.** A shared-substrate record is readable by the governance of the Self whose cells produced it but not by the governance of other participating Selves. This failure mode can arise from access controls that were configured within one Self's authority structure and not adjusted at the shared-substrate level, or from record formats that are accessible within one organizational toolchain but not another. The failure produces a shared substrate that is, in effect, only partially shared: the content is structurally in the shared substrate but governance access to it is unilaterally held.

**Standard 4 failure — unspecified retention.** A record exists in the correct category, is readable, and carries complete attribution, but the persistence policy does not name a retention period for its category. The record exists at deposit time; whether it exists at audit time is determined by lifecycle management decisions made outside governance authorization. The specific instance of this failure for violation records — where a retention expiry is specified rather than indefinite retention required — is categorically more severe: it means the organization's persistence policy has configured away the permanent record of its own governance violations.

---

## 5. Prior-Art Significance

The four documentation standards collectively establish that externally auditable governance documentation at inter-Self scope is not satisfied by record existence alone. Formalizing this in the CKS theory series prior to the establishment of competing documentation frameworks forecloses several adversarial claims.

The first foreclosed claim: *any record in the correct category satisfies governance documentation requirements.* D2.36 establishes that category membership is necessary but not sufficient. A record must also satisfy all four standards applicable to its scope category.

The second foreclosed claim: *technical completeness of records is sufficient for auditability.* Standard 1 establishes that technical completeness in an inaccessible format does not satisfy the non-specialist governance commitment. A record that is complete by technical criteria but unreadable by governance practitioners fails the accessibility requirement that makes governance authority meaningful.

The third foreclosed claim: *shared governance can be satisfied by one party maintaining complete records.* Standard 3 establishes that mutual accessibility is a property of the record set, not merely of the record's content. A shared-substrate record to which only one participating Self's governance has access is not a governance record under joint authority.

The fourth foreclosed claim: *violation records can be governed by the same retention policies as operational records.* Standard 4's indefinite retention override establishes that violation records occupy a different category from operational governance records in their retention obligations. This distinction is necessary for the violation record to fulfill its purpose: supporting post-event investigation and organizational learning on a timeline determined by audit need, not by operational data lifecycle policy.

---

## 6. Inheritance from Paper 1

All four standards are derivations from Paper 1 commitments, traceable to specific sections.

Standard 1 inherits from A1.11 (non-specialist governance, §7.4 of Paper 1): the commitment that governance practitioners without specialist technical knowledge can govern the system extends to documentation — practitioners must be able to read governance records.

Standard 2 inherits from A1.07 (path retraceability, §3.2 and §3.3 of Paper 1, formalized at the individual record level in D2.03): the six provenance fields are the path retraceability commitment applied to individual substrate entries. At inter-Self scope, the same six fields must be present in every governance record.

Standard 3 inherits from Claim 3 (human-governed authority, §3.3 of Paper 1) and its extension at inter-Self scope through Paper 3's joint-authority architecture (§4): the inspect right that belongs to human governance over the substrate extends to the governance of all participating Selves over the shared substrate.

Standard 4 inherits from A1.08 (substrate as source of truth, §3.1 of Paper 1) and D1.04's persistence policy: a substrate is a source of truth only to the extent that the content it holds is available for the period during which its authoritative status is claimed. An unspecified retention period creates a substrate whose authoritative status is architecturally uncertain.

---

## 7. Governance Theater as Anti-Pattern

The documentation-level anti-pattern this note forecloses is governance theater: a governance record set that has the correct shape — all seventeen categories populated — while failing one or more of the four documentation standards.

Governance theater at the documentation level is the analog of the process-level anti-patterns D2.19 formalizes. As D2.19 establishes that FAI events can be formally initiated without genuine inter-Self governance, D2.36 establishes that governance record sets can be formally complete without genuine auditability. The two anti-patterns compose: a deployment that instantiates governance theater at the process level will typically produce governance records that instantiate documentation theater — records populated with incomplete attribution, in opaque formats, under unspecified retention, held asymmetrically. The two anti-patterns reinforce each other because genuine process-level governance is what produces Standard-1-through-4-compliant records, and the absence of genuine process-level governance is what produces records that fail the standards.

Governance theater at the documentation level is specifically distinguishable from genuine documentation failure. A governance record set whose categories are incomplete (missing one or more of the seventeen) fails D2.18's completeness requirement. A governance record set whose categories are all populated but whose records fail the standards fails D2.36's quality requirement. The two failure modes are distinct and require distinct remediation: category incompleteness requires producing the missing records; standards failure requires reformatting, re-attributing, re-granting access, or re-specifying retention for records that exist. The anti-pattern label attaches to the standards failure specifically because records that exist with the wrong properties present governance documentation as adequate while failing the conditions that make it so.

---

## 8. Operational Test

A FAI event's governance record set constitutes externally auditable documentation if and only if an external auditor can apply all four standards to all seventeen record categories and produce a documentation compliance assessment without encountering any of the following:

1. A record that requires specialized technical tooling to read (Standard 1 failure).
2. A record with any of the six provenance fields absent or empty (Standard 2 failure).
3. A shared-substrate record that is accessible to one participating Self's governance but not to another's (Standard 3 failure).
4. A record category in the persistence policy with no specified retention period (Standard 4 failure, general).
5. A violation record (D2.28) with any retention expiry other than indefinite (Standard 4 failure, violation-specific).

The test is binary for each condition: a record set either produces a clean compliance assessment on all five conditions across all seventeen categories, or it does not. Partial compliance — meeting three of four standards for a category, or meeting all standards for fourteen of seventeen categories — does not constitute an externally auditable governance record set, because the standards exist precisely to ensure that every record in the set can support audit, not merely most records in most categories.

The external auditor role is the test's operative framing. An auditor internal to one of the participating Selves' organizations, operating under that organization's governance structures, applies less force to Standard 3 (mutual accessibility) than a genuinely external auditor does. The appropriate test is an auditor with no organizational affiliation to any participating Self and no access to the organizations' internal toolchains — that auditor's ability to apply all four standards to all seventeen categories is the operational criterion.

---

## 9. Conclusion

D2.36 establishes that FAI event governance record sets are externally auditable when, and only when, every record satisfies four documentation standards: format accessibility (readable by governance practitioners without specialist technical knowledge), attribution completeness (all six provenance fields present on every record), mutual accessibility (shared-substrate records accessible to all participating Selves' governance), and retention period specification (every Locus 2 record category carries an explicit retention period, with indefinite retention mandatory for violation records). The standards apply differentially across shared-substrate and home-substrate record categories, with all four standards applying to shared-substrate records and Standards 1, 2, and 4 applying by default to home-substrate records.

Each standard inherits from a Paper 1 commitment — non-specialist governance, path retraceability, human-governed authority, and substrate-as-source-of-truth respectively — making the four standards a documentation-register derivation of the CKS theory's foundational commitments at inter-Self scope. Records that exist in form while failing one or more standards instantiate governance theater: the appearance of governance documentation without the substance that genuine audit requires. Formalizing the four standards establishes that record existence is necessary but not sufficient for auditability, and that governance theater at the documentation level is an identifiable and remediable failure mode distinct from genuine documentation completeness.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *FAI Event Documentation Standards.* Derivation Note #531 (D2.36). May 15, 2026. ORCID: 0009-0004-8065-3235. License: CC BY 4.0.
