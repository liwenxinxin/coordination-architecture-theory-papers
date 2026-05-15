# AP-12: Informal Resolution Rules

**Series D — Phase D3 Anti-Pattern Formalization, Note #582**
**Note ID:** D3.07
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

AP-12 formalizes the anti-pattern in which conflict resolution logic for a Full Aspect Integration (FAI) event is established through informal practitioner understanding — pre-event discussions, organizational custom, or institutional practice — rather than authored as orchestration rule content within the shared substrate. When conflicts arise during the event, they are resolved by applying this informal understanding rather than by executing authored governance rules. The violation is not whether the resolutions are substantively correct; informal understanding may produce the same outcomes as authored rules. The violation is architectural: rules that exist only as shared practitioner knowledge are not substrate content, cannot govern AI mediator behavior as substrate content, cannot be reproduced from governance records, and cannot be consulted as authoritative reference when disputes arise. A distinctive consequence unique to this anti-pattern is governance transfer risk: informal resolution logic is stored in practitioners' heads, not in the substrate, and is therefore lost when those practitioners leave their organizations. The remediation path is formalization of existing practice — governance practitioners convert their informal understanding into the four-part authored rule structure, making existing governance knowledge permanent and auditable without requiring the invention of new governance approaches.

---

## 1. Anti-Pattern Name and Category

**Name:** AP-12 — Informal Resolution Rules

**Taxonomy Category:** Category 2 — Conflict Handling Failures

AP-12 is the third of four Category 2 anti-patterns. Category 2 anti-patterns address failures in the conflict-handling layer of inter-Self coordination: configurations in which conflicts that arise during FAI events are not handled in accordance with the three-tier mechanism (preserve, resolve via orchestration, escalate to humans) that Paper 3 Claim 3 establishes. AP-12 addresses a specific form of handling failure: the resolution tier is operationally present — conflicts are in fact resolved — but the logic governing those resolutions is not authored substrate content. The anti-pattern is not silence on conflict (AP-10) or missing coverage of conflict classes (AP-11); it is the presence of resolution under the wrong governing instrument.

---

## 2. Description

AP-12 occurs when the conflict resolution logic for a FAI event is held informally between participating Selves' governance practitioners rather than authored as orchestration rule content within the shared substrate.

The informal understanding may take several forms. Practitioners from the two participating organizations may have discussed, in advance of the event, how certain categories of conflict should be handled. They may rely on long-standing institutional custom about how their organizations negotiate disagreements. They may draw on industry practice or professional norms that both parties recognize without having written anything down. In each case, the understanding is genuine and may be sophisticated — the practitioners are not operating arbitrarily. The understanding simply has not been given the form the architecture requires: a jointly authorized orchestration rule, authored as shared substrate content, specifying the conflict class, the resolution logic, the resolution record specification, and the rule scope.

When a conflict arises during the FAI event, practitioners apply their informal understanding to resolve it. The conflict registry is updated to RESOLVED status. The resolution may be entirely correct by any substantive measure. What is absent is the authored rule that should have governed it.

This is the architectural gap. The resolve via orchestration tier of the three-tier mechanism requires that when prebuilt orchestration logic exists for a conflict class, the rules within the shared substrate determine the response. Those rules must themselves be substrate content, authored under joint authority. An informal understanding that exists only as shared practitioner knowledge is not substrate content. It cannot govern the orchestration of AI mediator behavior in the way substrate content can. It cannot be read from the substrate by an independent reviewer. It cannot be cited as the authoritative governing instrument when a dispute later arises over whether the resolution was correct. It cannot be transferred to successor practitioners who were not party to the original discussions.

The anti-pattern is structurally distinct from having no resolution logic at all. Systems that rely on informal rules may appear to function well during the FAI event itself. The gap surfaces later: in audit, in dispute, in practitioner turnover, and in the progressive erosion of institutional memory that occurs as the practitioners who hold the informal understanding move on.

---

## 3. Detection Criteria

AP-12 is present when one or more of the following conditions are observed:

**Resolved conflicts without identifiable governing rules.** Conflict registry entries carry RESOLVED status, but no authored orchestration rule within the shared substrate can be identified as the instrument that governed the resolution. The registry records an outcome; it does not record a rule citation.

**Resolution records reference organizational practice rather than authored rules.** Resolution documentation references "agreed approach," "organizational practice," "established custom," or similar constructions without naming a specific authored rule in the shared substrate. The resolution record points to practitioner understanding rather than substrate content.

**Thin or absent orchestration rule content alongside a populated conflict registry.** The shared substrate's orchestration rule layer is absent or minimal, yet the conflict registry shows that conflicts have been resolved. This pattern — resolved conflicts, thin rule layer — is the structural signature of AP-12.

**Coverage gap assessment would show relevant conflict classes have no authored rules.** A systematic review of the orchestration rule layer against the conflict classes that have arisen during FAI events (per D2.15's coverage gap assessment methodology) would reveal that the conflict classes governed by informal understanding have no corresponding authored rules. The gap assessment distinguishes AP-12 from AP-11 (missing coverage) only in that AP-12 involves resolutions that have actually occurred; in AP-11, the conflicts were preserved or escalated because no rule existed. In AP-12, the conflicts were resolved despite the absence of an authored rule, by application of informal understanding.

**Practitioner-dependent resolution consistency.** Resolutions are consistent only while the same practitioners are involved. When different practitioners attempt to resolve conflicts of the same class, inconsistencies appear, because there is no substrate-level rule to consult; each practitioner applies their own version of the informal understanding.

---

## 4. Governance Commitment Violated

AP-12 violates three governance commitments, ordered by directness of violation.

**Primary — Paper 1 Claim 4, AI-as-mediator property B.** Paper 1 Claim 4 commits that the AI operates as a substrate mediator: it writes to the substrate under orchestration rules, and those rules must be authored substrate content. An LLM mediator executing within the shared substrate cannot be governed by informal practitioner understanding, because informal understanding is not substrate content. It cannot be read from the substrate, cannot be applied consistently across AI executions, and cannot constrain AI behavior in the way authored rules can. Conflict resolution that proceeds through informal rules rather than authored substrate rules violates the foundational requirement of property B.

**Secondary — Paper 1 Claim 3, human-governed authority.** Paper 1 Claim 3 commits that governance is exercised as structural human authority over substrate content and orchestration rules — the right to inspect, modify, and override. Governance through informal practitioner understanding is not structural authority over substrate content. Informal rules can be unilaterally reinterpreted by either party's practitioners without any change to the substrate. They cannot be inspected in the substrate, because they are not there. They cannot be modified through the substrate's governance mechanisms. The three rights that constitute human-governed authority in the CKS sense are not exercisable over informal rules, because informal rules have no substrate representation over which those rights could be exercised.

**Tertiary — Determinism contract (D2.66).** The determinism contract requires that conflict resolutions be reproducible from substrate content alone: a reviewer with access to the shared substrate and the conflict registry should be able to reconstruct the resolution logic that governed each RESOLVED entry. Resolutions governed by informal rules cannot satisfy this requirement. The resolution logic is not in the substrate; it is in practitioners' heads. The determinism contract fails for every conflict governed by informal rules, regardless of whether the resolutions are substantively correct.

**Operational reference — D2.15, orchestration rule authoring requirements.** D2.15 specifies the four-part structure that orchestration rules must satisfy and the joint authorization requirement that attaches to inter-Self orchestration rules. Informal resolution rules violate both: they lack the four-part structure (conflict class definition, resolution logic, resolution record specification, rule scope), and they have not been jointly authorized as substrate content by the governance arrangements of both participating Selves.

---

## 5. Consequences

AP-12 produces five distinct consequences, each following from the architectural gap between informal understanding and authored substrate content.

**Non-reproducibility of resolutions.** An independent reviewer cannot verify from governance records alone that a resolved conflict was handled correctly. The resolution record shows an outcome; it does not show the rule that governed it. The review process depends on locating the practitioners who applied the informal understanding and querying their recollection — a process that is neither reliable nor scalable. Every informally-resolved conflict is a governance record gap.

**Determinism contract failure.** The determinism contract fails for every conflict governed by informal rules. This is not a probabilistic failure — it is a structural one. The contract requires substrate-reproducible resolutions; informal rules are categorically incapable of satisfying that requirement. The failure is complete for every informally-resolved conflict in the registry.

**Dispute risk without authoritative resolution.** If the participating Selves' practitioners hold subtly different versions of the informal understanding — which is common even among practitioners who believe they are aligned — disputes arise over whether a resolution was correct. There is no authored rule to consult as authoritative reference. Resolution of the dispute requires negotiation, escalation, or retrospective rule creation, all of which are more costly than having an authored rule in place before the conflict arose. The dispute (D2.45) has no authoritative resolution record to consult because no authoritative record exists.

**Governance transfer risk.** This is the consequence distinctive to AP-12 and absent from neighboring anti-patterns. Authored orchestration rules persist in the substrate independent of which practitioners wrote them. Informal resolution rules persist only in the memories and institutional knowledge of the practitioners who hold them. When those practitioners leave their organizations — through departure, retirement, reassignment, or organizational change — the informal rules are lost. The successor practitioners have no record to consult. They must either reconstruct the informal understanding from other sources, negotiate new informal rules from scratch, or operate without consistent resolution logic. The governance loss is proportional to the informality of the rules and the degree of practitioner turnover.

This consequence has a compounding structure. Each FAI event governed by informal rules increases the volume of governance knowledge held informally rather than in the substrate. As that volume grows, so does the organization's exposure to governance loss through practitioner departure. The risk is not static; it accumulates with each event conducted under informal governance.

**Path retraceability failure.** Path retraceability (D2.67) requires that the authorization chain for each governance action be reconstructible from substrate records. Informal resolution rules break this chain: the authorization for the resolution cannot be located in any authored substrate artifact, because the authorizing instrument — the informal understanding — is not a substrate artifact. The path from conflict to resolution cannot be retraced through substrate content.

---

## 6. Intra-Self Analog

The intra-Self analog of AP-12 is operating cell governance within a single Self through informal practitioner understanding rather than authored orchestration rules.

Paper 1 establishes that orchestration rules governing cell-level behavior must be human-authored substrate content. The requirement is not contingent on whether the cells are operating within an inter-Self shared substrate or within a Self's home substrate. A cell governed by informal practitioner understanding — where the practitioners who configured the cell share a common understanding of how it should behave, but have not authored that understanding as substrate rules — violates Paper 1's AI-as-mediator commitment at the cell scope.

The intra-Self case is less likely to persist undetected because the scope is smaller and the practitioners are typically co-located within a single organization with shared institutional knowledge. The inter-Self extension amplifies every dimension of the risk: the practitioners are from different organizations with different institutional contexts, the informal understanding must bridge organizational boundaries where interpretive divergence is structurally more probable, and the governance transfer risk operates across two organizations whose practitioner populations turn over independently.

AP-12 at inter-Self scope violates the same Paper 1 commitment as its intra-Self analog, but at a larger coordination scope where the consequences of the violation are amplified by organizational independence, cross-boundary interpretive risk, and the compounding of governance transfer exposure across two institutions.

---

## 7. Resolution

The complete prevention of AP-12 is the four-part authored rule structure specified in D2.15, jointly authorized before the FAI event begins. Each conflict class that might arise during the event must be covered by an orchestration rule that specifies:

1. **Conflict class definition** — the conditions that identify conflicts belonging to this class within the shared substrate.
2. **Resolution logic** — the algorithm or decision procedure that determines the resolution when a conflict of this class is surfaced.
3. **Resolution record specification** — what the conflict registry entry must record when this rule governs a resolution, including the rule identifier, the resolution outcome, and any escalation pathway that applied.
4. **Rule scope** — the FAI event or class of events to which the rule applies, and any conditions under which the rule is superseded or escalated.

Each authored rule is jointly authorized by the governance arrangements of both participating Selves, per D1.25's joint authorization requirement. The jointly authorized rule is the substrate-level instrument that governs the resolution; the resolution record cites it.

Where AP-12 is already present — where informal rules have been applied to past FAI events and the governance gap is discovered retrospectively — the remediation path is formalization of what already exists informally. This is an important framing: the remediation does not require the invention of new governance approaches. The practitioners who have been applying informal rules already know how conflicts should be resolved. That knowledge is the raw material for the authored rules. The task is to make it permanent and auditable.

The remediation sequence is:

**Step 1 — Documentation of informal understanding.** Governance practitioners from both participating Selves document their current informal understanding of how each conflict class should be resolved. The documentation is a working draft, not a governance artifact. Its purpose is to surface the understanding so it can be examined, compared across both organizations' practitioners, and prepared for formalization.

**Step 2 — Comparison and alignment.** The documented understanding from both sides is compared. Discrepancies — places where the practitioners believed they were aligned but held subtly different versions of the rule — are identified and resolved through deliberate negotiation. This step often reveals that the informal understanding was less uniformly held than the practitioners believed.

**Step 3 — Joint authoring of four-part rules.** Practitioners jointly author orchestration rules in the four-part structure for each conflict class. The rules formalize the aligned understanding as substrate content. The authoring process converts practitioner knowledge into a governance artifact that exists independent of the practitioners.

**Step 4 — Joint authorization.** The authored rules are jointly authorized by the governance arrangements of both participating Selves, per D1.25. Authorization records are written to the substrate.

**Step 5 — Retroactive rule citation for historical resolutions.** Where historical conflict registry entries lack rule citations, the newly authored rules are applied retroactively as the governing instruments for conflicts of the relevant class. This is a governance record repair that gives historical resolutions the authoritative citation they lacked. The repair is imperfect — the resolutions were not in fact governed by the authored rules at the time they occurred — but it establishes an authoritative standard against which historical resolutions can be assessed.

After remediation, subsequent conflicts of the covered classes are governed by authored substrate rules. The determinism contract is satisfied for those conflicts. Governance transfer risk is eliminated for the covered classes, because the resolution logic is now in the substrate rather than in practitioners' heads. The informal understanding has not been discarded — it has been made permanent.

---

## References

Li, W. (April 2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* [Paper 1 in the CKS theory series.]

Li, W. (April 2026). *The Instinct/Reasoning Separation Outside the Model.* [Paper 2 in the CKS theory series.]

Li, W. (April 2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* [Paper 3 in the CKS theory series.]

**Derivation note cross-references:** D1.25 (joint authorization requirement); D2.15 (orchestration rule authoring requirements and four-part rule structure); D2.45 (dispute anti-pattern); D2.66 (determinism contract); D2.67 (path retraceability); AP-10 (silent conflict resolution); AP-11 (missing coverage gap).
