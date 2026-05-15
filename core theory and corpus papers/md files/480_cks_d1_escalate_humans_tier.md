# Escalate-to-Humans Tier for Unresolvable Inter-Self Conflicts

**Derivation Note D1.15 — #480 in the CKS Defensive Publication Series**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes D1.15, the third and final sub-commitment in the conflict-handling tier set derived from Paper 3 Claim 3: the **escalate-to-humans tier**, which activates when a conflict in the shared substrate is neither appropriate for simple preservation (D1.13) nor covered by pre-authored orchestration rules (D1.14). The defining architectural property of this tier is **cross-perimeter governance authority**: the humans who receive the escalation must hold authority spanning the home governance perimeters of all participating Selves, not merely the authority of any one participating Self's home governance structure alone. The note states when escalation applies, characterizes the escalation record as substrate content with full provenance, enumerates four governance response options available at escalation, derives the tier's inheritance from Paper 1 Claim 3 (human governance as final authority), closes the three-tier Claim 3 sub-commitment set (D1.13–D1.15), identifies four failure modes the commitment defends against, and provides an operational test for verifying compliance after an FAI event in which escalation occurred.

---

## 1. Position in the Derivation Series

This note is the fifteenth Phase D1 sub-commitment (#480 overall). Phase D1 decomposes each of Paper 3's six Claims into foundational sub-commitments. D1.15 derives from D0.03 (the Paper 3 Claim 3 anchor: the three-tier inter-Self conflict-handling mechanism) and closes the three-note Claim 3 sub-commitment set:

- **D1.13** — Preserve tier: conflicts in the shared substrate preserved as first-class addressable substrate state when the task does not require resolution.
- **D1.14** — Resolve tier: conflicts of known classes resolved by pre-authored orchestration rules operating as substrate content within the shared substrate.
- **D1.15** (this note) — Escalate tier: conflicts that neither preserve alone nor pre-authored rules can handle surface to human governance authorities holding cross-perimeter authority over the participating Selves.

D1.16 will begin the Claim 4 (evolution feed) sub-commitment set.

---

## 2. Statement of D1.15

**D1.15 — Escalate-to-Humans Tier.** When a conflict in the shared substrate is neither addressable by simple preservation (D1.13 tier) nor covered by pre-authored orchestration rules (D1.14 tier), the conflict is **escalated to human governance authorities** who hold governance authority **crossing the home perimeters of all participating Selves**. The escalation event is recorded as substrate content in the shared substrate — or, where the shared substrate has dissolved, in a durable record whose governance-configured persistence policy governs its retention — with full provenance: the conflict's identity, content, timestamp, and the governance authorities notified. Upon receiving the escalation, the governance authorities may exercise any of four response options: author a resolution, direct that the conflict be preserved, author new orchestration rules for future instances of the conflict class, or authorize early dissolution of the shared substrate. The escalation record is subject to path retraceability.

---

## 3. When Escalation Applies

The escalate tier is a residual tier — it applies precisely when the two prior tiers do not. Its triggering conditions are:

**Condition 1 — No covering orchestration rule.** The conflict class is not addressed by any pre-authored orchestration rule operating within the shared substrate. Either the conflict class is genuinely novel, or the existing rules are silent on the specific configuration of aspects in conflict.

**Condition 2 — Governance stakes that exceed automated resolution.** The conflict bears on cross-organizational interests — resource allocations, authority boundaries, data rights, or coordination commitments — where resolution requires judgment that the orchestration rule layer is not authorized to supply. Automating such resolution without prior human authorization would conflict with the "humans decide resolution logic, not the LLM" axis that Paper 1 Claim 3 establishes and that Paper 3 inherits.

**Condition 3 — Cross-organizational judgment required.** The conflict cannot be resolved within any one participating Self's home governance alone because its resolution affects what each participating Self's governance holds as authoritative. The conflict sits at a boundary that requires all relevant governance authorities to participate in the resolution decision.

These three conditions are not independently sufficient; they characterize the space of conflicts for which the escalate tier is the architecturally correct response. A conflict meeting all three conditions cannot be left for automated resolution without violating the human-governance commitment. It must surface to human authority.

---

## 4. The Defining Property: Cross-Perimeter Authority

The architectural differentiator of the escalate tier — what distinguishes it from a conflict simply being flagged or logged — is the **cross-perimeter authority requirement**. The humans who receive the escalation must hold governance authority that spans the home governance perimeters of all participating Selves. Single-Self governance is insufficient: the authority of Participating Self A's governance structure extends to its own home perimeter and no further. It cannot commit Participating Self B's governance to a resolution; it cannot determine what becomes authoritative for both Selves jointly.

The cross-perimeter authority may be held in two structural forms. First, the governance authorities of each participating Self may act jointly — each home governance structure participating in a coordinated resolution decision, with no unilateral determination by any one party. Second, a higher-level governance authority with oversight spanning all participating Selves may hold the required cross-perimeter authority directly — a designated trustee arrangement, a joint committee pre-constituted for the coordination program, an arbitration panel with appropriate mandate, or an oversight body with regulatory or contractual authority over all participating Selves.

The architecture does not prescribe which structural form applies; that is a governance-configuration decision, enumerable under Paper 3 Claim 5 (configuration as substrate content). The architecture does prescribe the structural *property* the receiving authority must hold: its governance reach must cross all relevant home perimeters. An escalation that surfaces only to one Self's home governance, with that governance then issuing a resolution that purports to bind the others, is not a valid instantiation of the escalate tier. It is single-Self resolution dressed as joint governance — one of the four failure modes this sub-commitment defends against (§7).

The cross-perimeter authority requirement is not a procedural nicety. It is what gives the escalation its governance legitimacy at the inter-Self perimeter. Without it, the escalation path exists in name but cannot perform the function the tier is designed to serve: producing a resolution — or a decision to preserve, re-rule, or dissolve — that all participating Selves' governance structures recognize as authoritative.

---

## 5. The Escalation Record

Every escalation event produces a record that becomes substrate content. The record captures full provenance:

- **Conflict identity.** The identifier of the conflict record within the shared substrate, linking the escalation event to the specific conflicting aspects that triggered it.
- **Conflict content.** The substance of the conflict: which aspects are in conflict, on what dimension, and what the conflicting positions are. This content is preserved as first-class substrate state, not summarized or flattened.
- **Timestamp.** When the escalation occurred during the FAI event's lifecycle.
- **Governance authorities notified.** The identity of the governance authorities to whom the escalation was directed, establishing the chain of notification.
- **Tier-selection basis.** A record of why the preserve tier and the resolve tier were not applied — which orchestration rules were checked and found inapplicable, or what governance-stake determination led to the escalate-tier routing.

This record is subject to path retraceability — the Paper 1 accountability commitment (A1.07) that any governance-relevant event in the substrate must be traceable through its full decision path. An escalation event is a governance-relevant event: it activates human governance authority at the inter-Self perimeter. Failing to record it or recording it without provenance would break the accountability chain at the most consequential point in the conflict-handling mechanism.

Where the shared substrate has dissolved before the escalation record can be finalized — or where the escalation occurs during a dissolution sequence — the governance-configured persistence policy for the FAI event governs where and how the escalation record persists. It may be carried in a durable record at a Locus 2 persistence site, distributed to participating Selves' home substrates, or held under a separately configured governance arrangement. What the architecture requires is that the record exists in accessible, inspectable form and that its provenance is intact.

The escalation record is itself subject to the three Paper 1 governance rights: any authorized governance holder may inspect it, modify it to add governance annotations or response records, and override any automated characterization of the conflict it contains. These rights are preserved by the fact that the escalation record is substrate content governed by the same commitments that govern all other substrate content.

---

## 6. Four Governance Response Options

When a conflict reaches the escalate tier and the escalation record has notified the appropriate governance authorities, those authorities have four architecturally valid response options. The architecture supports all four; governance selects among them based on the specific conflict's character, the state of the FAI event, and the cross-organizational interests at stake.

**Option 1 — Author a resolution.** The governance authorities issue a governance decision that resolves the conflict. The resolution is added to the shared substrate as governed substrate content — authored under joint authority, inspectable, and subject to path retraceability. The resolved conflict record is updated to reflect the resolution decision, and the resolution becomes part of the FAI event's substrate record. This option is appropriate when the conflict is resolvable by a cross-perimeter governance judgment and the FAI event can productively continue with the conflict resolved.

**Option 2 — Direct preservation.** The governance authorities determine that the conflict should be preserved — carried in the shared substrate as first-class unresolved state — rather than resolved. This is a governance decision, not an absence of governance: the authorities are affirmatively directing that the conflict remain open, to be carried to participating Selves' home substrates for independent treatment under home governance authority. This option is appropriate when the conflict involves aspects of each Self's governance that should be addressed by each Self separately, and where joint resolution would improperly override home governance authority.

**Option 3 — Author new orchestration rules.** If the conflict class is recurring — or if the conflict that triggered the escalation is representative of a class the governance authorities wish to cover in advance — they may author new orchestration rules within the shared substrate to govern future instances. The new rules are substrate content under joint authority, subject to all Paper 1 commitments. Future conflicts of the same class will then route to the resolve tier (D1.14) rather than escalating. This option closes the gap between the escalate tier and the resolve tier for conflict classes that governance has now addressed.

**Option 4 — Authorize early dissolution.** In cases where the conflict is severe enough that the FAI event cannot productively continue — where the conflict concerns fundamental incompatibilities in what the participating Selves' governance structures will permit the shared substrate to contain — the governance authorities may authorize early dissolution of the shared substrate before the FAI event's normal conclusion. Dissolution is governed by the Paper 3 dissolution commitment (D1.05): it proceeds under governance authority, with appropriate persistence of records, provenance, and any outputs already produced. Early dissolution is not a failure of the architecture; it is the architecture functioning correctly by surfacing, to human governance, a conflict that cannot be resolved within the FAI event's scope.

These four options are architecturally equivalent at the tier level — each is a valid governance response to an escalated conflict. An implementation that restricts governance to a subset of the four options without pre-authorized governance-configured reasons would constrain governance authority in a way the architecture does not permit.

---

## 7. Inheritance from Paper 1 Claim 3

The escalate tier is the inter-Self instantiation of Paper 1 Claim 3 — the human-governance commitment. Paper 1 commits that human governance holds three rights at all times over all substrate content and orchestration rules: the right to inspect, the right to modify, and the right to override. These rights are unconditional: no automated resolution pathway may operate in a domain where human governance has not authorized it. The "humans decide resolution logic, not the LLM" axis is the mechanism by which this authority is exercised at the rule-authoring layer; the override right is the mechanism by which it is exercised at the intervention layer.

At cell scope (Paper 1) and intra-Self scope (Paper 2), the human-governance commitment operates within governance structures that are co-extensive with the substrate's governance perimeter. At inter-Self scope (Paper 3), the shared substrate spans governance perimeters that belong to distinct organizations. When neither preservation nor pre-authored rule-based resolution is appropriate for a conflict, the human-governance commitment cannot be satisfied by any one participating Self's home governance acting alone. The cross-perimeter shape of the escalate tier — escalation surfacing to governance authority that spans all relevant home perimeters — is what Paper 1 Claim 3's human-governance commitment produces when it extends to the inter-Self scope.

The three loci of fresh content that Paper 3 Claim 3 introduces at this tier (as Paper 3's publication-ready manuscript §6.1 identifies) are: the inter-Self specification of Paper 1 §5.3, the joint-authority shape of the escalate tier, and the substrate-content character of tier-decision logic. The escalate tier's joint-authority shape is the genuinely novel element at this scope — not a new governance commitment, but the cross-perimeter application of a governance commitment that Paper 1 established and Paper 3 extends. See T1.06 in the trilogy ambiguity map for the cross-paper disambiguation of conflict handling.

---

## 8. Closing the Three-Tier Set

D1.13, D1.14, and D1.15 together cover the full range of inter-Self conflict scenarios that can arise during FAI events within the shared substrate. The three tiers are exhaustive at the level of governance response type:

| Tier | Sub-commitment | Activation condition | Governance form |
|------|---------------|---------------------|-----------------|
| Preserve | D1.13 | Conflict present; resolution not required by task | Conflicts held as first-class substrate state; no resolution authored |
| Resolve | D1.14 | Conflict class covered by pre-authored orchestration rules | Automated rule application under joint authority; humans decide logic |
| Escalate | D1.15 | No applicable rule; governance stakes require cross-perimeter human judgment | Conflict surfaces to human authorities with cross-perimeter governance mandate |

Any conflict in the shared substrate falls into one of these three categories. The first tier handles the cases where governance has judged that resolution is not required at the inter-Self boundary. The second tier handles cases where governance has pre-authorized an automated response for the conflict class. The third tier handles everything else — the residual class where governance has not pre-authorized a response and must be activated directly.

This design — a residual tier that catches all cases the prior tiers do not handle — means the three-tier mechanism cannot produce a case where a conflict is simply dropped or silently resolved. Either it is preserved, resolved under a rule, or it escalates. There is no path by which a conflict disappears from the substrate without a governance decision, explicit or delegated.

D1.16 will begin the Claim 4 sub-commitment set, addressing the four-locus evolution feed mechanism at the FAI dissolution boundary.

---

## 9. Failure Modes This Sub-commitment Defends Against

D1.15 defends against four specific failure modes in inter-Self coordination architecture.

**Failure Mode 1 — No escalation path.** A system in which all conflicts are handled by automated resolution logic, with no provision for escalation to human governance when the automated logic has no applicable rule. This architecture treats automated resolution as unconditionally authoritative at the conflict boundary, violating the human-governance commitment: conflicts that exceed the authorized scope of automated resolution have no path to the human governance authority that Paper 1 Claim 3 reserves final authority for.

**Failure Mode 2 — Single-Self escalation.** A system in which escalation routes to one participating Self's home governance authority rather than to governance authority holding cross-perimeter mandate. This failure mode may appear to honor the escalation requirement (humans do receive the conflict) while actually violating its cross-perimeter property: the receiving authority lacks the governance reach to issue a resolution that all participating Selves' governance structures recognize as authoritative. Resolution issued under this arrangement is unilateral governance dressed as joint governance.

**Failure Mode 3 — Unrecorded escalation.** A system in which escalation occurs — humans are notified, responses may be issued — but no substrate content records the escalation event with provenance. Without the escalation record, the accountability chain at the most consequential point in the conflict-handling mechanism is broken: there is no inspectable record of which conflicts triggered escalation, which governance authorities were notified, or what response was issued. Path retraceability cannot be satisfied for the escalation event.

**Failure Mode 4 — Escalation without response options.** A system in which the escalation path exists and the escalation record is created, but the governance authorities who receive the escalation have only one available response (e.g., only resolution; no ability to direct preservation, author new rules, or authorize dissolution). This constrains governance authority below the level the architecture commits to: governance must be able to respond appropriately to the full range of conflict characters, and a restricted response option set imposes an architectural constraint that overrides governance judgment.

---

## 10. Operational Test

For a conflict that was escalated during an FAI event, the following verifications constitute a compliance test for D1.15.

1. **Locate the escalation record.** Can an observer — one with appropriate inspection authority — find substrate content (in the shared substrate, or in a durable record under the event's persistence policy) that records the escalation event? The record must exist as inspectable substrate content, not only as a notification log or an external message.

2. **Verify conflict provenance in the record.** Does the escalation record contain the conflict identity, the conflict content (the substance of the conflicting aspects), the timestamp, and the tier-selection basis (why the preserve and resolve tiers were not applied)?

3. **Verify cross-perimeter authority of the receiving governance bodies.** Are the governance authorities named in the escalation record ones whose governance mandate spans the home perimeters of all participating Selves? Can the observer verify that no single participating Self's home governance authority alone received and resolved the escalation?

4. **Locate the governance response.** Is there substrate content reflecting the governance response: a resolution decision authored under joint authority, a direction to preserve the conflict, new orchestration rules authored for the conflict class, or an early-dissolution authorization? If the FAI event concluded without a governance response (e.g., because the governance authorities have not yet acted), is the escalation record in a state that reflects the open escalation?

5. **Verify response traceability.** If a governance response was issued, can the observer trace the lineage from conflict → escalation record → response, with each step reflected in substrate content? Is the response itself substrate content under joint authority, subject to the three Paper 1 governance rights?

A system that passes all five verifications for a given escalation event instantiates D1.15. A system in which any verification fails — no record exists, the record lacks provenance, the receiving authority was single-Self, no response options were available or exercised, or the response cannot be traced — fails to instantiate D1.15 at that escalation event.

---

## 11. Relationship to Adjacent Sub-commitments

D1.15 is the terminal tier in the conflict-handling set. It inherits the conflict-as-first-class-state commitment from D1.13: conflicts that reach the escalate tier are already preserved as first-class substrate state; escalation does not require re-creating the conflict record. It inherits the rule-inspection and joint-authority framework from D1.14: the governance authorities who receive escalations may respond by authoring new orchestration rules, which become the same class of joint-authority substrate content that D1.14 formalizes.

D1.15 also inherits from the path retraceability commitment (Paper 1 A1.07), the human-governed commitment (Paper 1 Claim 3, as developed above in §7), and the dissolution commitment (D1.05, which governs early dissolution as a governed substrate event). All four responses available to governance authorities at escalation — resolution, directed preservation, new rule authoring, early dissolution — connect to commitments that earlier derivation notes have already placed in the prior-art record.

---

*End of Derivation Note D1.15.*
