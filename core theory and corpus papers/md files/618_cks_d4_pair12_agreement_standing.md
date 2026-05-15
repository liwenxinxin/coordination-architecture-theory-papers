# Composition Pair 12: Cross-Organizational Agreement and Standing Configuration

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Two governance commitments from the CKS inter-Self coordination architecture — the Cross-Organizational Governance Agreement (D2.34) and Standing Configurations (D2.21) — compose into a governance architecture that neither commitment defines on its own. When both are active within a relationship, a parent-child document hierarchy emerges: the agreement is the parent governance document, and each standing configuration is a child that must remain consistent with it. This composition produces three non-obvious governance obligations: the parent-child hierarchy must be enforced at authoring time so that the agreement governs any dimension the two documents specify differently; agreement amendments must cascade to standing configuration review so that no standing configuration silently becomes inconsistent with the amended agreement; and agreement termination must revoke all standing configurations within the relationship so that no orphaned governance infrastructure remains active after its authority basis has ended. These obligations are requirements of the composition — neither commitment alone generates them — and any governance architecture that maintains both layers simultaneously must address all three.

---

## 1. Pair Identification

**Commitment A — Cross-Organizational Governance Agreement (D2.34)** formalizes an ongoing governance relationship between two organizations whose AI coordination systems interact through shared substrate. The agreement has five components: (1) mutual governance standards establishing the norms both parties apply to shared coordination activity; (2) an escalation governance framework specifying how unresolved conflicts are routed across organizational boundaries; (3) a conflict domain specification identifying which conflict classes are in scope for the agreement's handling; (4) an amendment protocol allowing the agreement to evolve under joint consent; and (5) a termination protocol specifying how the relationship can be dissolved with defined closure obligations. Commitment A is bilateral: both parties' governance perimeters are party to the agreement, and neither can unilaterally modify its substantive terms.

**Commitment B — Standing Configurations (D2.21)** provides reusable jointly-authorized governance templates for recurring FAI events within a relationship. Rather than specifying full governance parameters each time a recurring event type occurs, the parties author a standing configuration once, jointly authorize it, and invoke it by reference for subsequent events of the same class. Standing configurations specify, at minimum, the governance parameters — merge behavior, conflict handling, escalation routing — that apply whenever an event of the covered type occurs. Commitment B reduces governance overhead for high-frequency recurring event types; its value scales with the frequency of the events it covers.

The composition scenario is an ongoing relationship in which both governance layers are simultaneously active: the parties have established a cross-organizational agreement under Commitment A and have authored multiple standing configurations under Commitment B for recurring event types within that relationship. Both layers carry live governance obligations and must remain internally consistent and mutually consistent.

---

## 2. Governance Scenario Requiring Both Simultaneously

Two organizations have coordinated AI operations under a shared substrate for some time. Their working relationship has matured to the point where a formal cross-organizational agreement is in place, establishing mutual governance standards, an escalation framework for cross-boundary conflicts, and conflict domain definitions. Within that agreement, the parties have recognized several high-frequency recurring FAI event types — weekly synchronization runs, quarterly review integrations, ad-hoc conflict escalations of a defined class — and have authored standing configurations for each. The standing configurations reference the agreement's escalation framework rather than specifying escalation routing independently, and rely on the agreement's mutual governance standards as the baseline for their merge and conflict-handling rules.

At any given moment, the relationship is governed by both layers: the agreement sets the outer framework, the standing configurations provide the operational detail for recurring events. The governance challenge is maintaining consistency between them across the lifetime of the relationship — through agreement amendments, standing configuration additions, and eventual termination.

This is the scenario in which the composition's governance obligations become load-bearing. Neither layer alone creates the consistency obligations. It is the coexistence of both, within an active relationship, that generates them.

---

## 3. Non-Obvious Governance Requirements from the Combination

### Requirement 1 — Parent-Child Hierarchy: Agreement Governs Inconsistencies

The cross-organizational agreement is the parent governance document. Each standing configuration within the relationship is a child document that must be consistent with it. When the agreement and a standing configuration specify the same governance dimension differently, the agreement governs.

This hierarchy is not apparent from either commitment alone. Commitment A defines the agreement's structure and content. Commitment B defines the standing configuration's structure and content. Neither commitment specifies what happens when they conflict on a shared dimension. The composition requires that this question be answered — and answered in the agreement's favor — for the governance architecture to be coherent.

The practical implication is an authoring obligation: when a standing configuration is being created or modified, its authors must check each governance dimension it specifies against the corresponding dimension in the parent agreement. A standing configuration that specifies escalation routing differently from the agreement's escalation framework is not merely inconsistent; it is invalid on that dimension, because the agreement governs. This check must occur at authoring time, not only at invocation time.

The hierarchy also enables a useful architectural pattern: standing configurations can reference the agreement's frameworks rather than independently specifying them. A standing configuration can state "escalation follows the agreement's Component 2 framework" rather than reproducing the escalation rules in full. This referencing and inheritance reduces duplication and ensures that agreement-level changes automatically propagate to any standing configuration that references the agreement's frameworks, rather than requiring separate updates to each.

### Requirement 2 — Agreement Amendment Cascades to Standing Configuration Review

When the cross-organizational agreement is amended under its Component 4 amendment protocol, all standing configurations derived from the agreement must be reviewed for consistency with the amendment. The amendment may have affected the governance dimensions that standing configurations rely on, reference, or specify.

Three amendment types generate specific review obligations. An amendment to Component 1 (mutual governance standards) requires review of any standing configuration that references those standards or specifies behavior calibrated to them: the standards may have shifted, and the standing configuration's behavior may no longer conform. An amendment to Component 2 (escalation governance framework) requires review of any standing configuration that specifies escalation routing: the routing rules may have changed, and the standing configuration may now direct escalation to a path the agreement has modified or superseded. An amendment to Component 3 (conflict domain specification) requires review of standing configurations with conflict routing rules: the definition of which conflict classes are in scope may have changed, and a standing configuration's conflict handling may reference a class that has been redefined or removed.

The governance process obligation this creates is specific: the amendment record for any agreement amendment must trigger standing configuration review records for each standing configuration within the relationship. The review may conclude that a given standing configuration remains consistent with the amendment and requires no update; but the review must occur and must be documented. Without this obligation, a standing configuration authored before the amendment will silently remain active under governance parameters the amendment has superseded. Silent inconsistency between the agreement and its derived standing configurations is the failure mode the cascade prevents.

Neither Commitment A nor Commitment B individually generates this obligation. Commitment A's amendment protocol specifies how the agreement is amended; it says nothing about downstream effects on standing configurations. Commitment B's standing configuration structure specifies what a standing configuration contains; it says nothing about triggers for review. The cascade is a composition requirement.

### Requirement 3 — Agreement Termination Revokes All Standing Configurations

When the cross-organizational agreement is terminated under its Component 5 termination protocol, all standing configurations within the relationship are automatically revoked. No standing configuration can survive its parent agreement's termination.

The reason is structural: standing configurations derive their authority basis from the agreement. The agreement's Component 1 supplies the mutual governance standards that standing configurations operate under. The agreement's Component 2 supplies the escalation framework that standing configurations route through. The agreement's bilateral authority is what makes a jointly-authorized standing configuration valid in the first place. When the agreement ends, the authority framework it supplied ends with it. A standing configuration that remains active after agreement termination has no valid authority basis — it is an orphaned governance artifact referencing frameworks that no longer exist.

The governance architecture failure that results from failing to revoke standing configurations at termination is directly analogous to AP-18 (Forgotten Standing Configuration): governance infrastructure that was created under valid authority remains active after the conditions justifying its authority have ended. The failure mode is not merely theoretical. If a standing configuration for a high-frequency recurring event type remains active after the agreement terminating the relationship, it may continue to be invoked — either through automated triggers or through parties acting on stale governance documentation — generating coordination activity that has no valid bilateral authorization.

The composition requirement is that agreement termination governance must include standing configuration revocation as an explicit step. The termination record must enumerate the standing configurations being revoked and confirm their revocation as part of the closure sequence. This step is not implicit in either the termination protocol (which governs the agreement) or the standing configuration structure (which governs individual configurations). It is a composition obligation.

### Requirement 4 — Sequencing: Agreement Prerequisites Standing Configurations

The agreement's Component 1 (mutual governance standards) and Component 2 (escalation governance framework) must be established before standing configurations within the relationship can be validly authored. A standing configuration that references frameworks the agreement has not yet defined is referencing content that does not exist.

This sequencing requirement is the composition's temporal constraint. In practice it is usually satisfied naturally: parties who have not yet established a cross-organizational agreement are unlikely to be authoring standing configurations that reference it. But in governance architectures where standing configurations can be pre-authored and activated later, or where the agreement and standing configurations are being established simultaneously as part of a relationship launch, the sequencing constraint must be made explicit. The agreement's foundational components are prerequisites, not parallels.

---

## 4. Prior-Art Significance

The composition formalizes governance architecture requirements that are not visible from either commitment in isolation and that any sustained inter-Self coordination governance architecture must address when both governance layers are active.

Parent-child document hierarchy in governance systems is not novel in the abstract. Corporate policy frameworks routinely establish master policies governing subsidiary procedures. Legal agreements routinely govern subsidiary work orders. What the composition adds is the specific instantiation of this hierarchy in the context of AI coordination governance under joint authority across distinct organizational governance perimeters, with the specific amendment-cascade and termination-revocation obligations that the inter-Self coordination context generates.

The cascade requirement — that amendment of a parent document triggers review of child documents — is known in document management systems and regulated-industry compliance frameworks (pharmaceutical SOPs, financial policy hierarchies). The composition formalizes this requirement as a governance process obligation specific to the cross-organizational agreement / standing configuration pair: not a document management best practice, but an architectural requirement for maintaining valid governance state in an active inter-Self relationship.

The termination-revocation requirement has a clear prior-art gap. Agreement termination in legal and organizational frameworks typically addresses the agreement itself — what obligations survive, what assets are returned, what transition periods apply. It does not routinely address the revocation of standing operational configurations that derived their authority from the agreement. The composition makes this requirement explicit in the AI coordination governance context, where standing configurations may be embedded in automated invocation systems and may continue to be triggered absent explicit revocation.

Any "sustained AI coordination governance architecture" that operates cross-organizational relationships with both a governance agreement and standing configurations must address the four requirements this composition identifies. Prior art that addresses the agreement layer without the standing configuration layer, or the standing configuration layer without the agreement hierarchy, leaves the composition requirements unaddressed.

---

## 5. Operational Test

For a relationship in which both a cross-organizational agreement and standing configurations are active, an observer can verify governance compliance through three checks:

**(a) Parent reference check.** Can the observer verify, for each active standing configuration, that it references its parent agreement? A standing configuration that does not reference its parent agreement cannot be checked for consistency with it, and the hierarchy cannot be enforced. The check passes if each standing configuration carries an explicit parent agreement reference and the referenced agreement is the one governing the relationship.

**(b) Amendment cascade check.** When the observer examines the agreement's amendment records, can they find corresponding standing configuration review records for each amendment? For each amendment to Component 1, 2, or 3, there should be review records for standing configurations in scope. The check passes if every agreement amendment has triggered documented standing configuration reviews, even if the reviews concluded that no updates were required.

**(c) Termination closure check.** When the observer examines a terminated relationship's governance records, do the termination records include standing configuration revocation records? The check passes if the termination sequence includes an enumeration of revoked standing configurations and a revocation record for each, contemporaneous with the agreement termination record.

A governance architecture that passes all three checks has discharged the composition's primary obligations. A governance architecture that fails any check has a specific governance gap: missing parent references indicate an unenforced hierarchy; missing amendment cascades indicate a silent inconsistency risk; missing termination revocations indicate orphaned governance infrastructure.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Composition Pair 12: Cross-Organizational Agreement and Standing Configuration.* May 15, 2026. ORCID: 0009-0004-8065-3235.
