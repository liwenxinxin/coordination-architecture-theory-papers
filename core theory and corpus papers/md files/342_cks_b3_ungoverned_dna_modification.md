# Ungoverned DNA Modification: The Anti-Pattern That Arises When DNA Layer Changes Bypass Paper 1's Standard Authority Architecture per B1.14

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

B1.14 commits that directed selection — one of three evolution mechanisms operating in productive tension across CKS Selves — is governed through Paper 1's standard authority architecture. DNA layer changes require authorization at the appropriate level, provenance recording per A2.40, and prospective-only application per A6.02. The Ungoverned DNA Modification anti-pattern arises when DNA layer content is changed outside this framework: by an actor who lacks A2.47 authority for the level modified, without creating the provenance records that make the modification auditable, or in a retroactivity-violating manner that claims new DNA governed operations that preceded the modification. All three forms produce the same foundational failure — DNA layer content whose governance legitimacy cannot be established — but they do so through distinct mechanisms that require distinct responses. This note formalizes the anti-pattern structure, traces the three recognizable forms, identifies the emergence conditions that make each form likely, states the operational consequences, and provides detection and remediation guidance.

---

## 1. Pattern Name and Commitment Violated

**Pattern name:** Ungoverned DNA Modification

**Commitment violated:** B1.14 — directed selection as DNA evolution governed through Paper 1's standard authority architecture (A2.01–A2.04)

B1.14 establishes that directed selection is the canonical form of DNA evolution in CKS: human governance defines the goals, selection criteria are themselves substrate content, and changes to the DNA layer proceed under an authority architecture that specifies who can propose, who can authorize, what verification regime applies, and what reversion paths exist. Paper 1's standard authority architecture (A2.01–A2.04) carries the per-step governance machinery. A2.47 distributes authority across governance levels so that modifications at cell scope, aspect scope, and Self scope each have an appropriate authorizing party. A2.40 requires provenance records for every modification event. A6.02 specifies that governance commitments apply forward from the time they take effect — new rules govern future operations, not past ones.

Ungoverned DNA Modification violates B1.14 whenever a DNA layer change occurs outside the authority architecture this commitment specifies — whether through an unauthorized actor, a failure to create modification records, or a retroactive application that the architecture explicitly forbids.

---

## 2. Recognizable Form

The anti-pattern presents in three distinct sub-forms. Each names a different way the governance framework can be bypassed; each produces a different artifact state with different audit consequences.

### Form 1 — Unauthorized Modification

The DNA layer at some governance level is changed by an actor who lacks A2.47 authority to make modifications at that level. The canonical instance is a cell-level operator modifying Self-level DNA: the operator has authority over cell-scope content but not over the orchestration rules and DNA content that govern the Self as a whole. An external system modifying DNA without any human governance in the authorization chain is a second instance. A human with authority at one aspect modifying DNA belonging to a different aspect's scope is a third.

The defining characteristic is that the actor's authority is insufficient for the level at which the modification occurs. Authorization at a lower level does not extend upward. A2.47 distributes authority precisely to prevent the assumption — natural in systems where access controls are coarse — that anyone able to read and write the substrate may modify any content within it.

Recognition signals: Modification records per A2.40 show modification events without corresponding A2.47 authority records for the level modified. B2.72 directed selection verification finds that governance authorization is absent or insufficient for the scope of the change. The modification records cannot answer the accountability questions that A5.09 specifies — in particular, "under what authority?" returns either no authority record or an authority record at the wrong governance level.

### Form 2 — Unrecorded Modification

The DNA layer is changed by an actor who holds appropriate A2.47 authority, but the modification occurs without creating the A2.40 provenance records that make the change auditable. The modification is real — the DNA content has changed — but it is invisible to governance audit. The substrate's observable state differs from what the modification history says it should be.

Unrecorded modification is architecturally more insidious than unauthorized modification in one respect: the actor's authority is legitimate, which means the change might well have been acceptable if properly recorded. The failure is procedural rather than authority-based, but the consequence for auditability is the same. A governance audit cannot distinguish between "this change was authorized and properly recorded" and "this change was authorized but bypassed the recording requirement" without examining the modification records themselves. When the modification records have a gap, the audit cannot close.

Recognition signals: DNA content has changed when current DNA is compared against the prior version, but no modification event record per A2.40 is present for the change. B2.69 DNA version management is absent — no new version was created at the time of modification. A6.02 retroactivity analysis cannot be applied because the timing of the modification is unknown; without a timestamp, there is no basis for determining which operations fell under the prior DNA and which fall under the current DNA. A1.07 retraceability at cell scope is broken — the DNA evolution history has a gap that cannot be filled from the substrate record alone.

### Form 3 — Retroactivity-Violating Modification

The DNA layer is modified and the change is applied retroactively: either by rewriting prior Action layer records to reflect what the new DNA would have produced, or by claiming in governance documentation or compliance demonstrations that the new DNA governed behavior during a period before the modification actually occurred. A6.02 specifies that new DNA applies forward only — the modification timestamp establishes when the new DNA took effect, and operations that occurred before that timestamp were governed by the DNA version then in force.

Retroactivity-violating modification may arise from genuine error (misunderstanding A6.02's prospective-only commitment) or from deliberate concealment (rewriting the record to eliminate audit evidence of prior DNA that produced unwanted outcomes). The architectural consequence is the same in either case: operational records that are internally inconsistent — Action records per B2.26 that reference DNA versions post-dating the Action records' own timestamps — and compliance claims that cannot be verified against the substrate record.

Recognition signals: Action records reference DNA versions whose timestamps post-date the Action records' own timestamps. Compliance demonstrations use current DNA to validate past operations that occurred under prior DNA versions. B2.70 retroactivity treatment compliance check fails: the modification timestamp does not predate the operations the new DNA is claimed to govern.

---

## 3. Emergence Conditions

Three conditions make Ungoverned DNA Modification likely to arise in deployed systems.

**Technical expedience.** DNA modification feels like a technical implementation step, not a governance event. Practitioners working under time pressure treat the orchestration substrate as a configuration artifact — something to be updated in the same register as editing a configuration file or deploying a code change. The authority architecture, provenance recording, and retroactivity rules that B1.14 specifies are perceived as overhead on what feels like a trivial edit. This is the most common path to unrecorded modification (Form 2) and to unauthorized modification by technically capable actors who are not malicious but simply did not recognize that the governance framework distinguishes authority levels (Form 1).

**Audit fear.** When actors recognize — sometimes after the fact, sometimes prospectively — that prior DNA decisions were wrong or that a governance gap will be visible in an upcoming audit, the temptation to retroactively correct the record is real. The motivation is not to improve the system but to eliminate evidence of the prior state. Retroactivity-violating modification (Form 3) arising from audit fear is governance fraud in its clearest form: it claims governance legitimacy for a period during which that governance did not exist, using the substrate's apparent authority to manufacture a retrospective record. Systems under regulatory pressure or internal audit cycles are particularly exposed to this emergence pathway.

**Authority ambiguity.** When A2.47 authority distribution is not clearly configured — when the question "who has authority to modify DNA at this governance level?" does not have a legible answer in the substrate — actors may modify DNA simply because no one has explicitly forbidden them from doing so. Authority ambiguity is not the same as no authority framework: the framework may exist at the architectural level while being incompletely instantiated in the specific deployment. The gap between architectural commitment and operational configuration is where unauthorized modification (Form 1) most often emerges without malicious intent.

---

## 4. Operational Consequences

**Audit integrity failure.** Governance audit depends on the substrate record being complete and accurate: every DNA change has an authorization record, a provenance record, and a timestamp. Unauthorized or unrecorded modifications break this dependency. A governance auditor cannot determine from the substrate record alone whether a given DNA state was properly authorized; the record contains either a gap (unrecorded) or a mismatch between the claimed authority level and the level modified (unauthorized). Compliance demonstrations for DNA content cannot be made reliably when modification histories contain these failures. The substrate's function as the authoritative record — A1.08's source-of-truth commitment — is undermined precisely at the layer where governance claims are most consequential.

**Retroactivity fraud.** Retroactivity-violating modifications that claim governance for periods before the modification occurred are, architecturally, a form of fraud: they assert that a governance framework existed and operated during a period when it did not. When this occurs in regulated contexts — healthcare, finance, legal — the assertion may carry legal as well as architectural consequences. But even absent regulatory implications, retroactivity fraud corrupts the substrate record in a way that makes the record unreliable as an audit artifact. The substrate's ability to demonstrate governed operation depends on the modification record being an accurate account of when each governance regime actually took effect; retroactivity-violating modifications destroy that accuracy.

**Substrate authority compromised.** A1.08 establishes that the substrate is the source of truth for governed operations. This commitment depends on the substrate's content having been properly governed — that the DNA in the substrate was modified through authorized, recorded, prospective-only processes. Ungoverned DNA modifications, in any of the three forms, undermine the foundational claim that the substrate's content can be trusted as the authoritative record. A substrate that contains unauthorized modifications, unrecorded gaps, or retroactively falsified records is not a source of truth; it is a document that appears authoritative but whose content cannot be verified.

**Directed selection verification failure.** B2.72 directed selection verification is the operational test that confirms governance integrity for DNA evolution: it checks that modifications are authorized, recorded, and properly timestamped. When DNA content contains ungoverned modifications in any of the three forms, B2.72 cannot confirm governance integrity. The verification mechanism works correctly — its failure output is accurate — but the failure means that directed selection's governance claim cannot be made for the affected DNA content. The consequences cascade to any downstream governance claim that depends on the DNA layer's integrity.

---

## 5. Detection

**B2.72 directed selection verification.** The primary detection mechanism. B2.72 asks of every DNA modification event: Is the modification authorized under A2.47 for the level modified? Is the modification recorded under A2.40? Does the modification timestamp predate the operations it governs? A failure on any of these questions identifies an ungoverned modification. B2.72 is most effective when run as a continuous governance process rather than as a periodic audit, because the detection lag for periodic audits allows unrecorded modifications to persist without remediation.

**A2.40 modification record audit.** Direct inspection of the modification record completeness. The audit compares current DNA content against the modification history and asks whether every observed change has a corresponding modification event. Gaps — where the DNA content has changed but no modification event is recorded — identify Form 2 instances. This audit requires access to prior DNA versions or a version management system per B2.69.

**A2.47 authority audit.** For modification events that are recorded, the authority audit verifies that the modifying actor held appropriate authority for the governance level of the modified content. An actor with cell-scope authority who has modified Self-level DNA produces an authority mismatch that the audit identifies. This audit is straightforward when A2.47 distribution is clearly configured in the substrate; it is more complex when authority ambiguity (one of the emergence conditions above) has not been resolved.

**B2.70 retroactivity compliance check.** A targeted check for Form 3. The check examines whether modification timestamps consistently predate the operations the modifications are claimed to govern. Action records per B2.26 whose referenced DNA versions post-date the Action records' own timestamps fail this check. Compliance demonstrations that rely on current DNA to validate operations from prior periods also fail.

---

## 6. Remediation

Remediation differs by form and must respect one cardinal constraint: Action layer records are not altered to match retroactive DNA claims. The operational history is fixed; governance gaps are addressed going forward through explicit directed selection, not by rewriting what the system did.

**For unauthorized modifications (Form 1).** The modification event must be reviewed by governance actors with appropriate A2.47 authority for the level modified. The outcome is one of two: retroactive authorization, where the authorized party reviews the modification, confirms it is acceptable, and creates an authorization record establishing that the modification has now passed governance review; or reversal through directed selection, where the authorized party determines the modification should not stand and initiates a directed selection process to return the DNA to the prior state or to a corrected state. In either case, the modification record is updated to reflect the governance outcome, and the authority chain is made explicit.

**For unrecorded modifications (Form 2).** Modification records are created retroactively with governance review. The authorized party establishes the best available reconstruction of when the modification occurred — from version control artifacts, deployment logs, or other external records — and creates an A2.40 provenance record with the reconstructed timestamp. The record should be transparent about its reconstructed status: a modification record that accurately reflects reconstruction is more valuable than a modification record that implies contemporaneous recording it does not represent. A6.02 retroactivity analysis is then applied to the reconstructed timeline to establish which operations fall under the prior and current DNA versions.

**For retroactivity-violating modifications (Form 3).** Accurate modification records are created with correct timestamps that reflect when the modification actually occurred. Prior Action layer records that were rewritten to reflect the new DNA must be restored to their original state — the operational history is fixed and must reflect what the system actually did under the DNA actually in force at the time. If the prior operational history reflects behavior under the prior DNA that is now considered incorrect or non-compliant, the appropriate response is to address the compliance gap through explicit directed selection going forward and to document the gap accurately in the governance record, not to retroactively eliminate its evidence.

**Preventing recurrence.** A2.47 authority distribution should be configured clearly and verifiably so that actors cannot modify DNA at a level above their authority scope without encountering an explicit gate. Authority configuration is itself substrate content under the standard authority architecture; ambiguity in the configuration is a governance gap that should be resolved through directed selection at the appropriate authority level. Governance workflows for DNA modification — what steps must be completed before a modification event is recorded — should be documented as orchestration rules humans author, making the workflow's requirements legible to all actors who might modify DNA.

---

## 7. Relationship to Adjacent Commitments

Ungoverned DNA Modification is the primary failure mode for B1.14, but its consequences reach several adjacent commitments. A1.08 substrate-as-source-of-truth requires that the substrate's content was properly governed — ungoverned DNA modifications directly undermine this requirement at the DNA layer. A1.07 retraceability requires that the path from current state to prior state can be reconstructed from the substrate record — unrecorded modifications (Form 2) break this path directly. A6.02 retroactivity governs which DNA version applied to which operations — retroactivity-violating modifications (Form 3) corrupt this accounting. B2.68, B2.69, B2.70, and B2.72 collectively constitute the positive specification that the anti-pattern violates: DNA modification governance, DNA version management, retroactivity treatment, and directed selection verification are the operational machinery whose absence or corruption the anti-pattern describes.

The boundary between Ungoverned DNA Modification and the adjacent anti-pattern Silent DNA Drift (B3.16) is worth making explicit. Silent DNA Drift describes the case where the Action layer accumulates content that effectively changes how the DNA is interpreted or applied over time, without the DNA layer itself being modified — drift without modification. Ungoverned DNA Modification describes the case where the DNA layer is modified but without following the governance framework — modification without governance. The two failure modes are distinct, can co-occur, and require different detection and remediation approaches.

---

*This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).*
