# Additional Composition Pair: Versioning and Amendment History and Process Disputes

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Two governance commitments in the inter-Self coordination architecture — Versioning and Amendment History (D2.38) and FAI Event Dispute Resolution (D2.45) — interact in a specific and non-obvious way when a process dispute turns on whether a configuration amendment was properly authorized. This note formalizes the composition of these two commitments and identifies three governance requirements that the composition surfaces but neither commitment supplies in isolation: version history must be structured for dispute-evidence use (not merely for audit traceability); the version history must be mutually accessible to both participating governance parties via the shared inspect right (not merely accessible to the amending party); and each amendment entry must contain a complete authorization chain sufficient for Level 1 dispute resolution without escalation. Any governed AI coordination architecture that combines amendment tracking with multi-level dispute resolution must address these three requirements.

---

## 1. Pair Identification

**Commitment A — Versioning and Amendment History (D2.38):** The governance record of all configuration changes made during a Full Aspect Integration (FAI) event, containing for each change a timestamp, the prior value, the new value, and the authorization record. The version history is the substrate-level artifact that makes configuration changes traceable and reversible. Its primary design purpose, as D2.38 specifies it, is audit traceability: a continuous record that any governance practitioner can read to understand how the shared configuration reached its current state.

**Commitment B — FAI Event Dispute Resolution (D2.45):** A three-level process for resolving governance disputes that arise during or after a FAI event. Level 1 is direct governance dialogue between the participating parties' governance practitioners, using governance records as the evidence base. Level 2 invokes the cross-organizational agreement that governs the FAI relationship. Level 3 escalates to the joint authority mechanism that governs the participating organizations' relationship. Each level is a distinct recourse with distinct participants, distinct authority, and distinct criteria for what constitutes resolution.

The two commitments occupy adjacent territory in the governance architecture: D2.38 creates the records; D2.45 uses them as evidence. The composition arises wherever a dispute under D2.45 turns on the content or authorization status of a change recorded under D2.38.

---

## 2. The Governance Scenario

A configuration amendment dispute is the paradigmatic case where both commitments apply simultaneously. One participating party — call it Self A — claims that a configuration change recorded in the shared substrate during a recent FAI event was unauthorized: the amending party (Self B) did not obtain the required joint authorization before making the change, or obtained it for a different amendment than the one recorded. Self A invokes the dispute resolution process under D2.45.

D2.45's Level 1 resolution requires both parties' governance practitioners to review the relevant governance records together. D2.38's version history is the primary evidence source: it contains the amendment in question, the prior value that was changed, the new value, the timestamp, and the authorization record. Both commitments are operationally active simultaneously. The version history must serve as evidence, and the dispute resolution process must be able to use it effectively.

This scenario is not pathological or rare. Any governance architecture in which configuration is substantive — where configurable parameters affect coordination behavior, resource allocation, or the scope of what a FAI event can accomplish — will produce amendment disputes whenever the parties' governance practitioners hold different understandings of what was authorized. The composition is a routine operational condition, not an edge case.

---

## 3. Non-Obvious Governance Requirements

Three governance requirements emerge from this composition that are not visible when either commitment is considered alone.

### Requirement 1 — Version History Must Be Structured for Dispute-Evidence Use

Audit design and dispute-evidence design are different design requirements, and a version history optimized for audit may be structurally inadequate for dispute resolution.

An audit-oriented version history answers the forward-looking question: what changed, and when? It records that a parameter was changed from some prior state to a new value at a given time. This suffices for traceability — a governance practitioner can reconstruct the sequence of changes and understand the current configuration's history.

A dispute-evidence-ready version history must answer a different set of questions. First, what was the prior value? The change can only be evaluated on its merits if the prior state is recorded, not merely the fact that a change occurred. A version history that records only new values — or that records prior values only in a form that requires consulting a separate artifact — places the burden of prior-state reconstruction on the disputing party and creates a gap that a well-resourced amending party could exploit. Second, which specific governance authority authorized the change? An authorization record that says "authorized" or "authorized per governance policy" does not enable Level 1 dispute resolution. The authorizing entity must be named and linked, so that the disputing party can verify that the named entity had the required authority and that the authorization was in fact obtained. Third, was the authorization contemporaneous with the amendment? An authorization obtained after the fact — or recorded after the fact — does not satisfy a joint-authorization requirement. The version history entry must permit an independent observer to determine whether authorization preceded or followed the amendment taking effect.

These three information requirements are not derivable from D2.38 alone, which specifies that the record contain a timestamp, prior value, new value, and authorization record. D2.38's specification is compatible with both dispute-evidence-ready and dispute-evidence-inadequate implementations. The composition with D2.45 closes this gap: dispute-evidence readiness becomes a governance obligation, not a design preference.

### Requirement 2 — Version History Must Be Mutually Accessible for Dispute Review

D2.38's version history is authored by the amending party. The record lives within that party's governance perimeter and is created by its governance practitioners. This is architecturally appropriate — the amending party is the source of truth for what its governance practitioners authorized.

But D2.45's Level 1 resolution requires both parties' governance practitioners to review the relevant records together. If the version history is not accessible to the disputing party via the shared inspect right, Level 1 is not merely difficult — it is structurally impossible. There is no shared evidentiary basis on which direct governance dialogue can proceed.

The consequence is automatic escalation. If the amending party's version history cannot be accessed by the disputing party, the inaccessible record itself becomes the subject of the dispute. The dispute is no longer "was this amendment authorized?" but rather "why can't we see the governance record for this amendment?" — a dispute that cannot be resolved at Level 1 because the evidence is unavailable, and that proceeds immediately to Level 2 (invocation of the cross-organizational agreement) with the access failure as its subject matter.

Mutual accessibility via the shared inspect right is therefore not a courtesy or a best-practice embellishment. It is a structural gate that determines whether any amendment dispute is Level 1-resolvable or is automatically elevated. Every amendment dispute over an inaccessible record is a Level 2 or Level 3 matter by architectural necessity, not by the severity of the underlying disagreement.

### Requirement 3 — Authorization Chain Completeness Enables Level 1 Resolution to Be Definitive

D2.45 specifies governance records as the evidence base for dispute resolution. The third requirement follows from asking what "evidence base" means in practice for an amendment dispute at Level 1.

If the authorization chain recorded in the version history entry is complete — naming the authorizing governance authority, identifying the joint authorization mechanism that was invoked, and recording whether authorization preceded the amendment taking effect — then Level 1 governance dialogue can close the dispute by reading the record. Either the chain is present, valid, and satisfies the applicable authorization requirement, or it is not. The resolution is definitive because the record is sufficient.

If the authorization chain is incomplete — if any link in the chain is missing, vague, or unverifiable from the record alone — then Level 1 governance dialogue cannot close the dispute even with full mutual access. The practitioners can read the record together and still not determine whether the amendment was authorized, because the record does not supply the necessary information. The dispute escalates to Level 2 not because the parties have exhausted Level 1 dialogue, but because Level 1 lacks the evidentiary foundation to produce a definitive answer.

Authorization chain completeness is therefore what makes the governance record the definitive evidence base that D2.45 requires. An incomplete record degrades the dispute resolution architecture from its intended form — a graduated recourse structure with Level 1 designed to resolve the majority of disputes through direct dialogue — into a structure where every substantive authorization dispute requires external mechanism invocation.

---

## 4. Prior-Art Significance

The governance properties formalized in this note — dispute-evidence-ready version history structure, mutual accessibility requirements for amendment records, and authorization chain completeness as a dispute resolution prerequisite — are specific to the composition of commitments D2.38 and D2.45 operating together within an inter-Self coordination architecture governed by a shared substrate.

Audit log design is mature across enterprise software, regulatory compliance, and records management literatures. Amendment tracking in multi-party contracts is well-established in legal governance. Multi-level dispute resolution ladders exist in joint venture agreements, data-sharing frameworks, and cross-organizational AI governance contracts. Version control systems provide prior-value tracking and change attribution.

None of these prior art traditions addresses the specific combination: a version history that must simultaneously serve audit traceability purposes, function as the evidentiary basis for a multi-level dispute resolution process, be mutually accessible across distinct governance perimeters via a shared inspect right, and contain authorization chain information sufficient to enable Level 1 resolution to be definitive without escalation. The combination is what the inter-Self coordination architecture produces, and the combination is what any implementation claiming this architectural territory must address.

Any "governed AI coordination amendment dispute resolution" architecture that fails to specify the three requirements identified in §3 — and that relies instead on audit-oriented record design, single-perimeter accessibility defaults, or incomplete authorization recording — will systematically underperform at Level 1 dispute resolution without a principled explanation for why.

---

## 5. Operational Test

For a version history record produced under the composition of D2.38 and D2.45, an independent observer should be able to verify the following:

**(a) Dispute-evidence structure:** Each version history entry includes the prior value of the changed parameter (not merely the new value), links the authorization to a named governance authority rather than a generic authorization assertion, and records the temporal relationship between authorization and amendment taking effect with sufficient precision to determine whether authorization was contemporaneous.

**(b) Mutual accessibility:** The version history is accessible to both participating governance parties via the shared inspect right — not only to the amending party that authored it. An observer from the non-amending party's governance perimeter can read the version history entry for any amendment that affects the shared coordination substrate without requiring the amending party's active cooperation.

**(c) Authorization chain completeness for Level 1 resolution:** Each amendment entry contains the identifying information needed for Level 1 dispute resolution to reach a definitive conclusion: which governance authority authorized the amendment, which joint authorization mechanism was invoked, and whether authorization was obtained before the amendment took effect. An observer can determine from the record alone — without consulting additional artifacts or requesting information from the amending party — whether the authorization chain is complete and valid.

A version history that satisfies all three parts of this test instantiates the composition correctly. A version history that satisfies (a) alone is audit-ready but not dispute-ready. A version history that satisfies (a) and (b) but not (c) supports Level 1 dialogue without enabling Level 1 to be definitive. A version history that fails (b) makes every amendment dispute a Level 2 or Level 3 matter regardless of its underlying merits.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Additional Composition Pair: Versioning and Amendment History and Process Disputes.* May 15, 2026. ORCID: 0009-0004-8065-3235.
