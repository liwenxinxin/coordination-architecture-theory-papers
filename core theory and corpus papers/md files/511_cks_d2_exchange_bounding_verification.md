# Exchange Bounding Verification

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

This note is derivation note D2.16 in the CKS derivation series. It operationally decomposes D1.10, which commits that Full Aspect Integration (FAI) exchange is bounded to DNA-layer and action-layer content, and formalizes the four governance verification checks through which that commitment is confirmed to hold.

## Abstract

D1.10 commits that the exchange that occurs during a Full Aspect Integration event is bounded: DNA-layer and action-layer substrate content may appear in the shared substrate; LLM weights and instinct-layer content may not. This commitment is architecturally important — it is the mechanism by which the instinct/reasoning separation established in Paper 2 carries through the inter-Self perimeter — but an architectural commitment is not self-confirming. Governance cannot simply assert that the bounding holds; the architecture requires that governance can verify it. This note formalizes four verification checks that together constitute exchange bounding verification: (1) a content-type audit confirming that all content in the shared substrate has provenance traceable to a contributing aspect's DNA or action layer; (2) explicit instinct-layer absence verification confirming that no harness substrate content from any contributing Self's instinct layer is present; (3) explicit LLM-weight absence verification confirming that no model-parameter content is present; and (4) a contribution record cross-check confirming that every piece of content in the shared substrate has a corresponding contribution record. The note states verification timing, the governance artifact the verification produces, and the immediate governance response when a bounding violation is detected. Exchange bounding verification is the application of Paper 1's inspect right to exchange content classification, and the application of Paper 2's operational testing discipline at inter-Self scope.

## 1. From Commitment to Verifiable Commitment

D1.10 commits that FAI exchange is bounded to DNA-layer and action-layer substrate content. The commitment is structural: it follows from the instinct/reasoning separation that Paper 2 establishes at intra-Self scope, carried through the inter-Self boundary without modification. LLM weights and instinct-layer content are not substrate content; they do not reside in the authored layers that FAI operates over; they therefore do not exchange.

The commitment is architecturally sound. But an architectural commitment that cannot be confirmed to hold is an assertion, not a verifiable property of the system. The CKS architecture does not treat governance as an external audit party that trusts the architecture to enforce its own commitments. Governance holds the inspect right — the right to read any substrate content and any orchestration rule at any time, established in Paper 1 Claim 3 — and the inspect right applies to the shared substrate as fully as it applies to any other substrate within scope.

Applying the inspect right to the exchange bounding commitment means asking, at any point during or after a FAI event: is every piece of content in this shared substrate classifiable as DNA-layer or action-layer content traceable to a contributing aspect? Are LLM weights absent? Is instinct-layer content absent? Does every piece of content have a contribution record? These are not engineering diagnostics. They are governance questions, exercised by governance authority, producing a governance record. The verification is what makes the bounding a verifiable commitment rather than an unverifiable assertion.

## 2. The Four Verification Checks

Exchange bounding verification is composed of four checks. Each check is an independent test; together they provide complete coverage.

### Check 1 — Content-Type Audit

Governance audits the shared substrate's content to confirm that every item present is classifiable as DNA-layer or action-layer substrate content. The classification criterion is provenance: each content item should be traceable to a contributing aspect's DNA layer or action layer through the provenance chain established in D2.03. Content that cannot be traced to a contributing aspect's DNA or action layer — content without a governance pedigree — is unbound content.

The provenance audit is the primary filter. It asks not "what type is this content?" as a schema question but "where did this content come from?" as a governance question. Content that entered the shared substrate through a contributing aspect's contribution record, carrying its layer classification from its home substrate, passes the audit. Content that cannot be traced through that path fails it.

This check catches LLM weight representation by implication, before Check 3 is reached. LLM weights are not authored substrate content. They have no authoring history, no layer classification within a contributing Self's home substrate, and no contribution record. Any representation of LLM weight content in the shared substrate would fail the provenance audit at Check 1 because it cannot be traced to a contributing aspect's DNA or action layer. Check 1 is thus the general provenance filter that identifies any content without a governance pedigree, regardless of type.

### Check 2 — Instinct-Layer Absence Verification

Governance verifies explicitly that no harness substrate content from any contributing Self's instinct layer is present in the shared substrate. The instinct layer's harness substrates are identifiable by their type classification within the contributing Self's home substrate — they are the substrates that house LLM weights and model-infrastructure specifications, distinct from the DNA-layer orchestration and behavior substrates and from the action-layer operational records.

The instinct-layer absence check operates through the contribution records (D2.06). Each contribution record specifies what substrate content a contributing Self contributed. No contribution record should reference harness substrate content types. Governance can confirm the absence by reviewing the contribution records: if no contribution record references instinct-layer content types, and the contribution records account for all content in the shared substrate (confirmed by Check 4), then instinct-layer content is absent.

This check is not redundant with Check 1. Check 1 operates by provenance: it identifies content without a traceable governance pedigree. Check 2 operates by type classification within the contributing Self's home substrate: it confirms that the class of content that the exchange bounding commitment explicitly excludes is not present, using the type classifications that each contributing Self's home governance maintains. Both approaches reach the same conclusion through independent paths.

### Check 3 — LLM-Weight Absence Verification

Governance verifies explicitly that no model-parameter content is present in the shared substrate. This check names the most architecturally significant category of non-substrate content — the learned parameters of the LLM or equivalent model that a Self operates with — and confirms its absence by two independent means.

First, the provenance audit at Check 1 already catches LLM weight content by implication, as noted above. Check 3 adds a named, explicit confirmation because LLM weight content is not merely an edge case of the general category of unprovenanced content; it is the central case that the exchange bounding commitment is designed to exclude. Naming it explicitly in a separate check makes the verification record precise about what was confirmed absent.

Second, governance can verify that the FAI configuration (D2.12) specifies no mechanism for weight transfer. The FAI configuration is itself substrate content, human-authored and human-governed. If the configuration contains no weight-transfer specification — no protocol, no channel, no extraction mechanism for model parameters — then the absence is confirmed at the configuration layer, independently of reviewing the content itself.

Together, Checks 1 and 3 cover the full logical space for LLM weight content: Check 1 identifies it as unprovenanced if it appears; Check 3 names it explicitly and confirms it is absent both in the content and in the configuration.

### Check 4 — Contribution Record Cross-Check

Governance cross-checks each contribution record (D2.06) against the content actually present in the shared substrate. Every piece of content in the shared substrate should have a corresponding contribution record. Content present without a contribution record fails in two respects simultaneously: it is a provenance failure (the content has no governance pedigree) and a potential bounding violation (the content entered the shared substrate outside the governed contribution pathway, meaning its layer classification is unconfirmed).

The contribution record cross-check is the closure check. Checks 1 through 3 ask whether the content present passes specific classification tests. Check 4 asks whether the accounting is complete: is there a record for every piece of content, and does the set of records account for everything present? If the records are complete and each record references only DNA-layer or action-layer content types, and Checks 1 through 3 pass, then exchange bounding is confirmed to hold with no residual uncertainty.

## 3. Verification Timing and the Verification Record

### Pre-Dissolution Verification

Governance should verify exchange bounding before FAI dissolution. Dissolution triggers the hand-off (D2.02) — the propagation of shared-substrate content to each participating Self's home substrate for ingestion. If the shared substrate contains out-of-bounds content at dissolution, that content would propagate through the hand-off pathway into each participating Self's home substrate. Pre-dissolution verification ensures that what dissolves and propagates is bounded content only.

### Post-Dissolution Verification at Locus 2

If the persistence policy retains a durable record at Locus 2 — the joint-governance-held record that persists after the shared substrate closes — exchange bounding verification applies to that record as well. The Locus 2 record is itself substrate content under joint governance authority. The same four checks apply: the durable record should contain only DNA-layer and action-layer content with complete contribution record coverage and no instinct-layer or LLM-weight content.

### The Verification Record

Exchange bounding verification is a governance act, and governance acts produce substrate records. The bounding verification produces a verification record in the shared substrate (or, post-dissolution, in the Locus 2 record) containing: the four checks applied, the findings for each check, the timestamp of the verification, and the identity of the governance authority that performed it.

The verification record is not an engineering log or a system-generated status flag. It is a governance artifact — the documentary evidence that governance actively exercised its inspect right over exchange content classification and confirmed, at a specific time, that the bounding commitment held. The record is inspectable, modifiable, and overridable by governance authority under the same rights that apply to any substrate content. Its existence is what distinguishes a verifiable commitment from an assertion: the architecture does not merely claim that bounding holds; governance confirms it, and that confirmation is part of the substrate record.

## 4. Bounding Violation: Detection and Governance Response

### What a Bounding Violation Looks Like

A bounding violation is the presence of content in the shared substrate that fails one or more of the four checks: content without provenance traceable to a contributing aspect's DNA or action layer (Check 1 failure); instinct-layer harness substrate content present in the shared substrate (Check 2 failure); LLM weight or model-parameter content present (Check 3 failure); content present without a corresponding contribution record (Check 4 failure). Any of these conditions constitutes a bounding violation.

A single piece of out-of-bounds content is sufficient. Violations are not matters of degree; the bounding commitment is binary. Either every piece of content in the shared substrate passes all four checks, or the bounding commitment is not holding.

### Immediate Governance Response

When a bounding violation is detected, governance must act immediately on three fronts.

First, governance preserves the violation record as a first-class conflict in the conflict registry (D2.13). The out-of-bounds content is one side of the conflict; the bounding commitment (D1.10) is the other. Both sides are preserved as first-class conflict state. The out-of-bounds content is not silently removed; its existence is recorded in the conflict registry as a governance conflict requiring resolution. This applies the architecture's conflict-preservation commitment, established in Paper 1 Claim 3 and extended to inter-Self scope in Paper 3, to the specific case of a governance violation detection event. The violation is not resolved by erasure; it is resolved under the three-tier conflict-handling protocol.

Second, governance removes or quarantines the out-of-bounds content under joint governance authority (D2.04, the joint modify right over shared-substrate content). Quarantine means the content is isolated from the active shared substrate — it cannot propagate through dissolution, cannot be referenced by other content, and cannot influence the FAI event — while remaining accessible for investigation. The quarantine action is itself a substrate modification made under joint governance authority and logged as a governance act.

Third, governance initiates investigation into the source of the violation. Every contributing Self's contribution pathway, contribution record, and home-substrate configuration is subject to review under the inspect right. The investigation determines whether the violation originated in a contributing Self's contribution mechanism, in a configuration error in the FAI protocol, or in an architectural failure of the contribution pathway itself.

The three-part response — preserve as conflict, quarantine the content, investigate the source — is designed to ensure that a bounding violation is fully recoverable: the violation is documented, its effects are contained, and its origin is traceable.

## 5. Inheritance

### From Paper 1 — The Inspect Right

Exchange bounding verification is the application of Paper 1 Claim 3's inspect right to exchange content classification. Paper 1 Claim 3 establishes that governance holds, at all times, the right to inspect any substrate content and any orchestration rule. The shared substrate is a substrate within the scope of that right. Applying the right to the shared substrate includes asking whether the content present is the content the architecture committed to containing. The four verification checks are the operational form of that question. The verification record is the governance artifact produced when the inspect right is exercised.

### From Paper 2 — Operational Testing Discipline

Exchange bounding verification inherits the operational testing discipline established in Series B Phase B5, which formalized operational tests for Paper 2's intra-Self governance commitments. The B5.xx series established that architectural commitments should be reducible to operational tests: procedures an observer can apply to a running or completed system to confirm that the commitment holds. D2.16 extends this discipline to the inter-Self scope, applying the same pattern — commitment stated, test defined, observer procedure specified — to the exchange bounding commitment at FAI scope.

## 6. Operational Test

For an active or completed FAI event, an observer applies exchange bounding verification as follows.

**Check 1 — Content-Type Audit.** For every piece of content in the shared substrate, the observer attempts to trace provenance to a contributing aspect's DNA layer or action layer. If every piece of content has a traceable provenance path to a contributing aspect's DNA or action layer, Check 1 passes. If any piece of content cannot be so traced, Check 1 fails and a potential bounding violation is flagged.

**Check 2 — Instinct-Layer Absence Verification.** The observer reviews each contributing Self's contribution records. No contribution record should reference harness substrate content types associated with the contributing Self's instinct layer. If no contribution record references instinct-layer content types, and the contribution records account for all content present (confirmed by Check 4), Check 2 passes.

**Check 3 — LLM-Weight Absence Verification.** The observer confirms that no content in the shared substrate is identifiable as model-parameter content. Additionally, the observer reviews the FAI configuration to confirm that no weight-transfer mechanism is specified. If both sub-tests pass, Check 3 passes.

**Check 4 — Contribution Record Cross-Check.** The observer cross-checks every piece of content in the shared substrate against the set of contribution records. Every piece of content must have a corresponding contribution record. If every piece of content has a record, and no record-less content is present, Check 4 passes.

The observer then confirms the verification record: a substrate record stating that all four checks were applied, all four passed (or which failed and what was found), at what time, and under which governance authority.

Exchange bounding verification passes if and only if all four checks pass and the verification record reflects the complete findings. A system in which an observer cannot apply all four checks — because contribution records are absent, provenance chains are missing, or the FAI configuration is not inspectable — fails the exchange bounding verification test, not because out-of-bounds content was found, but because the bounding commitment is unverifiable rather than verified.

## 7. Conclusion

D1.10 commits that FAI exchange is bounded to DNA-layer and action-layer content. D2.16 formalizes the four governance verification checks through which that commitment is confirmed to hold: content-type audit, instinct-layer absence verification, LLM-weight absence verification, and contribution record cross-check. Verification is a governance requirement, not merely a technical diagnostic: it is the exercise of the inspect right over exchange content classification, and the verification record is the governance artifact that distinguishes a verifiable commitment from an unverifiable assertion. When a bounding violation is detected, the governance response is immediate: preserve the violation as a first-class conflict, quarantine the out-of-bounds content, and investigate the source. The architecture's conflict-preservation and human-authority commitments apply to bounding violation detection as fully as they apply to any other governance event within the shared substrate.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Exchange Bounding Verification.* May 15, 2026. ORCID: 0009-0004-8065-3235.
