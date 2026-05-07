# The Source-of-Truth Five-Categories Test as Standalone Operational Procedure in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the operational test that verifies the substrate-as-source-of-truth commitment across the five categories of coordination state for which a CKS substrate is authoritative — *what is the case*, *what is current*, *what is in conflict*, *what rules apply*, and *who has what authority* — as a standalone procedure, separable from the joint commitment it tests and from the procedures testing adjacent commitments, exercisable at deployment, composition, migration, and authority-change boundaries.

## Abstract

The CKS pattern's substrate-as-source-of-truth commitment names the substrate as authoritative for five categories of coordination state. The test that verifies the commitment is not a single yes/no over a unitary property; it is a composite procedure running five Category-specific checks, passing only when all five succeed, and on failure identifying which Category fails and which class of source-of-truth anti-pattern is present. This note formalizes the procedure as a standalone operational test: states what each Category check verifies, specifies pass/fail criteria, enumerates the canonical anti-patterns the test detects (LLM-as-source-of-truth, agent memory, LLM context, external tool state authoritative, substrate substitute, vendor-managed authoritative content, distributed-authority, and Category-specific violations), names the deployment-lifecycle moments at which the test should run, and states the test's deliberate limits.

## 1. Why the test needs to be formalized as a standalone procedure

Source-of-truth is the central architectural commitment specifying where coordination authority sits in a CKS deployment. Path retraceability traces through it; determinism on the substrate side of the governance boundary presupposes it; AI-as-substrate-mediator names the LLM's role with respect to it; conflict preservation places contradictions inside it; linear-cost scaling depends on selective reads from it. A deployment that fails source-of-truth fails every commitment that hangs from it.

The companion derivation note that formalizes substrate-as-source-of-truth as joint commitment provides a four-clause test for its presence as a whole. That test is correct as a final yes/no, but underspecifies the structure of the verification: substrate is authoritative for five distinct categories, and a deployment can satisfy four while failing one in a way that compromises the entire posture. A single yes/no does not surface which Category fails, which anti-pattern is present, or which remediation applies. The diagnostic resolution lives one level lower — and naming the verification as a standalone composite procedure, with per-Category verdicts, is what places it there. The composite framing also makes the test exercisable at the lifecycle moments where the commitment is threatened: initial deployment, composition, vendor migration, compliance-framework changes, and authority-distribution changes.

This note is the tenth in the Phase A5 sequence and continues the cluster on AI mediation and substrate state.

## 2. The architectural commitment under test

The commitment the test verifies is substrate-as-source-of-truth in its decomposed form: that for each of five categories of coordination state, substrate is authoritative; alternative locations holding state in that category are non-authoritative mirrors derived from substrate, not parallel sources; queries of that category resolve against substrate content rather than against vendor systems, external tools, agent memory, or LLM context; and the LLM does not exercise authority over content in that category — humans do, directly or through human-authored orchestration rules.

The five categories are:

**Category 1 — what is the case.** The substrate is authoritative for the current factual state the coordination work tracks: decisions made, content authored, specifications agreed, definitions accepted, outcomes recorded.

**Category 2 — what is current.** The substrate is authoritative for currentness — which content is the current version, which is superseded, which is in force as of a given moment, which is provisional pending resolution. The substrate's representation of supersession and lineage is itself substrate content.

**Category 3 — what is in conflict.** The substrate is authoritative for the conflict registry — which contradictions are unresolved, between which substrate elements, with what provenance attached, with what resolution recorded if any. Conflicts are first-class addressable substrate objects, not error states held outside.

**Category 4 — what rules apply.** The substrate is authoritative for orchestration rules — which rule governs which class of cell-level behavior, with what version history, authored by whom, in force from when. Rules are not vendor-policy configuration external to the substrate.

**Category 5 — who has what authority.** The substrate is authoritative for authority distribution — which humans hold which governance rights over which substrate scope, with what delegation if any. Authority is recorded as substrate content rather than held in external identity systems treated as authoritative.

For each Category the architectural form is the same: substrate-resident content, alternative sources documented as derived non-authoritative mirrors, queries returning substrate content, AI mediation rather than authority. Failing any one Category fails the joint commitment.

## 3. The test procedure

The composite procedure runs five Category-specific checks. Each check has the same structure, applied to its category's content.

**Check structure (applied to each Category in turn).**

(a) *Identify a sample of substrate content in the Category.* The sample is content the deployment treats as Category-authoritative — for Category 1, sample decisions or recorded content; for Category 2, current-version markers or supersession records; for Category 3, conflict registry entries; for Category 4, orchestration rules; for Category 5, authority-distribution records.

(b) *Verify the content is substrate-resident.* The sample's authoritative location is substrate, not a vendor system, an external tool, agent memory, or LLM context. "Substrate-resident" means the content's primary, governing copy is in substrate; any other copy is derived.

(c) *Verify alternative sources are documented as non-authoritative mirrors.* Where alternative locations hold state of the same category — derived views, search indexes, vendor reporting tools, integration surfaces — the deployment documents them as mirrors, with derivation provenance running back to substrate, and treats them as discardable when they disagree with substrate.

(d) *Verify queries return substrate content.* A query against the Category — programmatic or human-issued — resolves against substrate. A derived view or cache used for performance is acceptable when it is substrate-derived; a query resolving against state with an independent authoritative origin fails the check.

(e) *Verify AI does not exercise authority for the Category.* Authoritative decisions are made by humans (Moment 2 of the human-governed commitment) or by cells executing under human-authored orchestration rules (Moment 1). LLM intermediation is permissible as mediation; LLM authority — the LLM deciding what counts as Category content without rule or human authorization — is not. This component echoes Property D of the AI-as-substrate-mediator commitment and overlaps with the mediator-role test, by design.

**Across change categories.** Each Category check is run not only against static state but across the change categories the deployment supports: a human modifying Category content; a human overriding a prior state; a human authoring or revising rules in Category 4; an authority-distribution adjustment in Category 5. After each change, Category authoritativeness must remain in substrate.

**Composite execution.** The five Category checks together constitute the source-of-truth-five-categories test. The test passes if and only if every Category check passes; the test fails if any Category check fails, and the failing Category identifies the class of anti-pattern present.

## 4. What the test outputs

The output is a per-Category verdict and a composite verdict.

**Pass.** All five Category checks succeed. The composite verdict is pass.

**Fail.** At least one Category check fails. The failing Category names the class of source-of-truth violation: Category 1 — current factual state authoritative outside substrate; Category 2 — currentness or supersession determined outside substrate; Category 3 — conflict registry held outside substrate; Category 4 — orchestration rules held as vendor or external configuration; Category 5 — authority distribution held externally. Multiple-Category failures compound; a deployment failing Categories 4 and 5 together typically has a vendor-policy-system-as-rule-and-authority-source pattern. The composite verdict's diagnostic value is precisely that it does not collapse to a single yes/no — a pass-with-Category-3-failure verdict names a precise architectural deficit downstream remediation can target.

## 5. Anti-patterns the test detects

The test detects two layers: canonical violations that present across multiple Categories, and Category-specific violations.

**Canonical source-of-truth violations.**

(a) *LLM-as-source-of-truth.* The LLM is queried as authoritative for Category content, and what the LLM returns is treated as the answer. Detected via any Category's check (e) failing.

(b) *Agent memory as source of truth.* An agent framework's memory (per-session, persistent, or cross-session) holds Category content treated as authoritative. Detected via check (b) placing authoritative content in agent memory rather than substrate.

(c) *LLM context as source of truth.* The LLM's context window across turns or sessions is treated as authoritative for Category content. Detected via check (b) placing authoritative content in LLM context.

(d) *External tool state authoritative.* An external system — project-management tool, ticketing system, chat log, vendor reporting product — is treated as the authoritative source for Category content. The acceptable converse — extracting external content into substrate under cell mediation — passes the check.

(e) *Substrate substitute.* An adjacent component is treated as substrate-equivalent for source-of-truth purposes, even though it does not satisfy the substrate commitments.

**Vendor-managed authoritative content.** A vendor system holds authoritative content for any Category, with the vendor able to revoke, modify, or restructure it without substrate's consent. Detected via check (b) placing authoritative content in a vendor-controlled location whose governance is not the deployment's.

**Distributed-authority.** Categories are split across multiple authoritative systems without a unifying substrate authority — Category 4 in one vendor's policy engine, Category 5 in an identity provider, Category 1 in a workflow tool. Detected by failures distributed across multiple Categories with different external authoritative locations.

**Category-specific anti-patterns.** Several violations present in only one Category and have well-defined names:

- *Rules-in-vendor-policy-system* — orchestration rules held in vendor-managed policy configuration. Specific Category 4 violation.
- *Conflict-in-vendor-case-management* — conflicts held in an external case-management or issue-tracking tool. Specific Category 3 violation.
- *Currentness-in-vendor-versioning* — currentness or supersession determined by a vendor's versioning behavior outside substrate. Specific Category 2 violation.
- *Authority-in-external-IAM* — authority distribution held in an external identity-and-access-management system, treated as the source of truth for "who can do what." Specific Category 5 violation.

For each anti-pattern, the test's per-Category verdicts name the violation rather than report a generic source-of-truth failure.

## 6. How the test integrates with deployment verification

Source-of-truth is threatened at predictable lifecycle moments. The test runs at each.

**Initial deployment validation.** Before activation, the test runs over the deployment as configured. A pass is precondition for activation; the initial run establishes a baseline subsequent runs compare against.

**Composition partner verification.** When a CKS deployment composes with adjacent components — agent memory frameworks, vector retrieval systems, workflow engines, governance middleware — composition can introduce alternative authoritative sources. The test runs as part of composition acceptance, verifying adjacent components are non-authoritative mirrors.

**Vendor migration verification.** When the host environment changes, the test runs after migration completes. The tool-agnosticism-migration test verifies a related but distinct property — that substrate state is preserved across migration; this test verifies the migrated state remains authoritative.

**Compliance-framework-update verification.** When external compliance frameworks change, the verification confirms the framework changes do not displace substrate's authority for Categories 4 and 5 in particular. A common failure mode is for compliance changes to introduce vendor-policy systems holding rule and authority content.

**Authority-distribution-change verification.** When the governance authority distribution itself changes — a role's scope is widened, a delegation is added or revoked, a new oversight role is established — the test runs against the post-change configuration. Category 5 specifically, plus any Category whose content the changed authority touches, must pass against the new distribution.

The test's role across these moments is constant: verify the five Categories remain substrate-authoritative, name which Category fails when one does, and give remediation a precise target.

## 7. Limits of the test

The test is deliberately scoped, and stating its limits keeps the standalone treatment from drifting into something stronger than the source paper supports.

**It does not verify the mediator role beyond Property D overlap.** Each Category's check (e) overlaps with Property D of the AI-as-substrate-mediator commitment. The mediator-role test verifies all five mediator properties together; this test verifies the source-of-truth-relevant component of Property D and no more.

**It does not verify path retraceability.** Source-of-truth places authoritative content in substrate; retraceability traces from substrate content through its provenance to its rationale and lineage. The test verifies the location of authority, not the completeness of provenance. The provenance-completeness and four-accountability-questions tests cover retraceability separately.

**It does not verify migration preservation.** Tool-agnosticism commits the architecture to preserving substrate state across host changes; this test verifies authoritativeness within a host. A deployment that passes this test before migration may fail to preserve the authoritative state across migration; the tool-agnosticism-migration test verifies the preservation property separately.

**It does not verify content correctness or coverage.** The test confirms substrate is the authoritative source for each Category; it does not confirm the substrate's content is correct, complete, or sufficient for the coordination work. A deployment can have substrate-authoritative content that is empty, wrong, or partial; the test passes if the locus of authority is right. Correctness and coverage are governance and deployment-quality concerns the architecture supports — through the inspect, modify, and override rights — but does not by itself verify.

A deployment that passes the source-of-truth-five-categories test has source-of-truth verified at the architectural locus; broader CKS verification is supplied by the Phase A5 sequence as a whole.

## 8. The test in one sentence

A deployment passes the source-of-truth-five-categories test if and only if for each of the five categories — what is the case, what is current, what is in conflict, what rules apply, and who has what authority — substrate-resident content is authoritative, alternative sources are documented as non-authoritative mirrors, queries return substrate content, and AI does not exercise Category-defining authority; failing any single Category fails the composite test and identifies the class of source-of-truth anti-pattern present.

## 9. Conclusion

Source-of-truth is the central commitment specifying authority distribution in a CKS deployment, and a deployment that fails it compromises every commitment that hangs from it. The integrated yes/no on the joint commitment is correct as a final verdict but underspecifies the verification work that underpins it; in practice, source-of-truth fails Category-by-Category, with precise anti-patterns associated with each failure mode. Naming the test as a composite five-Category procedure, with per-Category verdicts and a composite verdict, gives the verification the diagnostic resolution at which source-of-truth commitments actually break, and makes it exercisable at the lifecycle moments where the commitment is threatened.

The Phase A5 cluster on AI mediation and substrate state continues with the tool-agnosticism-migration test. Subsequent work that adopts, extends, or argues against the substrate-as-source-of-truth commitment should use the test specified here as the verification reference; subsequent work adopting a different procedure should name its differences against this one.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Source-of-Truth Five-Categories Test as Standalone Operational Procedure in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
