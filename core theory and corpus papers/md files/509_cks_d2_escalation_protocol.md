# Escalation Routing and Governance Response Protocol

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

The three-tier conflict-handling mechanism established in Paper 3 culminates in an escalate-to-humans tier that routes unresolvable conflicts to governance authorities with cross-perimeter authority. This note is the operational decomposition of that tier (D2.14, deriving from D1.15). It formalizes the escalation routing protocol as three elements — trigger, destination, and notification content — and the governance response protocol as four options: authoring a resolution, directing preservation, authoring new orchestration rules, or authorizing early dissolution. The note establishes that both the routing destination and the response timeline are governance-configured substrate content, authored as part of the FAI configuration before the FAI event begins. The unresponsive escalation anti-pattern — an escalation that reaches no governance response and triggers no default action — is identified as a governance completeness violation. An operational test closes the note.

## 1. Position in the derivation series

D2.14 is the fourteenth Phase D2 note in the Paper 3 derivation series. Its parent is D1.15, which committed that the escalate tier of the three-tier conflict-handling mechanism routes unresolvable conflicts to human governance with cross-perimeter authority. D1.15 established the architectural commitment; D2.14 formalizes its operational mechanics: what triggers the escalation, where it is routed, what the notification contains, and what governance can do in response.

Phase D2 derives operational variants and decompositions from each D1 sub-commitment, following the pattern established in Series B. D2.14 occupies the escalation-mechanics position within the D1.13–D1.16 conflict-handling cluster. It inherits the conflict registry established at D2.13 and the FAI configuration established at D2.12, and it connects forward to D1.16 (cross-perimeter escalation as architectural commitment) and the dissolution governance requirements established at D2.02.

## 2. Why operational escalation mechanics require explicit formalization

The escalate tier is architecturally committed at D1.15: when the preserve tier (D1.13) and the resolve-via-orchestration tier (D1.14) cannot handle a conflict, governance authorities with cross-perimeter authority make the determination. That commitment is real and load-bearing, but it does not by itself specify the operational mechanics that make it reliably exercisable. Three gaps remain open after D1.15 that D2.14 closes.

The first gap is trigger definition. When exactly does the shared substrate's orchestration logic escalate rather than preserve or resolve? Without an explicit trigger definition authored as substrate content, the boundary between tiers is informal, and informal tier boundaries invite inconsistent application. The escalation trigger must be governed — the rules specifying when to escalate versus preserve are themselves substrate content under joint authority, not behavioral properties of an LLM or runtime middleware.

The second gap is destination specificity. "Governance authorities with cross-perimeter authority" is architecturally correct but operationally incomplete. At the moment an escalation fires, the orchestration logic must know exactly which entities to notify. If that routing destination is determined in the moment — through informal communication, runtime inference, or ad hoc decision — then governance is improvised rather than governed. The routing destination must be pre-specified as authored substrate content before the FAI event begins.

The third gap is response completeness. Even a correctly routed escalation can produce an open-ended waiting state if no constraints govern the governance response. An FAI event cannot remain indefinitely suspended awaiting a governance response; the coordinating Selves need either a resolved conflict or a clear default action within a bounded window. The governance response protocol must specify all admissible response options and must be paired with a timeline that triggers a default action if governance does not respond.

D2.14 closes all three gaps.

## 3. Escalation routing — three elements

Escalation routing is the process by which a conflict that the orchestration logic cannot handle within the shared substrate is surfaced to governance authorities. The routing protocol has three elements.

**Element 1 — Escalation trigger.** A conflict is escalated when the shared substrate's orchestration logic determines that two conditions hold simultaneously: (a) the conflict class is not covered by any rule in the resolve-via-orchestration tier (D1.14), and (b) the conflict requires governance resolution rather than preservation (D1.13). Both conditions are evaluated against authored substrate content — the conflict class taxonomy and the resolve-tier rule set are substrate content under joint authority. When both conditions hold, the orchestration logic fires the escalation trigger and creates an escalation record in the conflict registry (D2.13) with status ESCALATED.

The trigger is itself governed. The rules specifying which conflict classes are out-of-scope for the resolve tier, and which conflicts require resolution rather than preservation, are authored orchestration rules within the shared substrate. They are not emergent behaviors, LLM inferences, or platform defaults. Governance authors them; governance can modify them. Unresolvable-conflict identification is a governance act, not a runtime computation.

**Element 2 — Routing destination.** Escalation is routed to governance authorities specified in the escalation routing configuration, which is authored substrate content within the FAI configuration (D2.12). The routing configuration specifies which governance authorities hold cross-perimeter authority for escalations arising in this FAI event. The configuration admits two principal forms: (a) per-Self governance designation, where each participating Self's governance authority is named and the authorities act jointly; or (b) pre-designated inter-organizational governance body, where the Selves' home governance structures have jointly established a standing body for inter-Self disputes before the FAI event begins.

The routing destination is pre-specified. Governance does not improvise who receives escalations during the event. At the moment an escalation trigger fires, the orchestration logic reads the routing configuration and dispatches the escalation notification to the named authorities. The routing configuration is subject to the same joint-authority, inspect-modify-override rights that apply to all shared substrate content; it can be updated between FAI events. It cannot be updated during an FAI event by any party acting unilaterally — the governance completeness commitment requires that the routing configuration in effect at event construction governs all escalations within that event.

**Element 3 — Escalation notification content.** The escalation notification is substrate content authored by the orchestration logic at the moment the trigger fires. It contains four items: (a) the conflict registry entry (D2.13), including both sides of the conflict preserved in full with provenance; (b) the conflict class classification and the basis for that classification; (c) the governance reasoning for escalation — which resolve-tier rules were consulted, why they did not apply, and why preservation was insufficient; and (d) the urgency level, specifying how long the FAI event can continue in the current state while awaiting a governance response before the default action is triggered.

The notification content is inspectable as substrate content. Governance authorities who receive the notification can find all of it in the shared substrate; nothing material to the escalation is communicated through out-of-band channels. This is the path retraceability property applied to the escalation tier: an observer reconstructing the escalation after the fact has access to everything that governance had access to.

## 4. Governance response protocol — four options

Upon receiving an escalation notification, governance authorities must take one of four actions within the response timeline specified in the FAI configuration. Each action has a defined effect on the conflict registry entry and on the FAI event.

**Option 1 — Author a resolution.** Governance authors a resolution specifying which side of the conflict prevails, or specifying a handling rule for the conflict that neither pure-prevail option captures. The resolution is authored as substrate content in the shared substrate with governance attribution — the identity of the authoring governance authorities, the date and time, and any rationale they choose to record. The conflict registry entry transitions to status RESOLVED-BY-ESCALATION. The FAI event proceeds under the resolution.

This option is appropriate when the conflict is discrete, its resolution has a clear basis in governance judgment, and the conflict class is unlikely to recur frequently. It provides immediate closure without expanding the rule set.

**Option 2 — Direct preservation.** Governance determines that the conflict should be preserved rather than resolved — carried into the FAI event output and forwarded to each participating Self's home substrate as a preserved annotation (D1.16). The governance direction is recorded as substrate content with attribution. The conflict registry entry transitions to status PRESERVED. The FAI event proceeds with the conflict carried as first-class state in the output.

This option is appropriate when resolution would require information not available during the FAI event, when the Selves' home governance structures are better positioned to resolve the conflict in their own operational context, or when preservation is the substantively correct response to the conflict class. Directing preservation is an active governance choice, not a failure to respond.

**Option 3 — Author new orchestration rules.** Governance determines that the conflict class is expected to recur in future FAI events and authors new orchestration rules to handle future instances in the resolve-via-orchestration tier. The new rules are authored as substrate content in the shared substrate under joint authority, with governance attribution. The current conflict may be resolved by the new rules (if the rules are designed to cover the current instance) or handled by one of the other three options simultaneously. The conflict registry entry transitions to status RESOLVED-BY-NEW-RULES or PRESERVED, as applicable.

This option differs from the other three in kind, not only in form. Options 1, 2, and 4 dispose of the current escalated conflict. Option 3 disposes of the current conflict and simultaneously expands the shared substrate's orchestration rule coverage for all future FAI events involving the same Selves. It converts a one-time governance response into a durable architectural change. The shared substrate's resolve-tier rule set grows; future conflicts of the same class will be handled without requiring escalation.

Governance should prefer Option 3 when the conflict class meets two conditions: (a) the class is likely to recur across future FAI events, and (b) a governable rule can be authored that handles the class consistently with the Selves' coordination commitments. When both conditions hold, the cost of authoring new rules is paid once and amortizes across all future FAI events; the alternative — repeated escalations of the same class — imposes recurring governance cost without producing durable coverage.

**Option 4 — Authorize early dissolution.** In cases where the conflict is irresolvable within the constraints of the FAI event and continuation would cause more harm than early termination, governance may determine that the FAI event should be dissolved before its planned completion. Early dissolution follows the standard dissolution governance requirements (D2.02) with one additional record: an escalation-triggered early dissolution notice authored as substrate content, stating the conflict that triggered the escalation, the governance reasoning for dissolution rather than the other three options, and the attribution of the authorizing governance authorities.

This option is the most consequential of the four. It terminates the FAI event and ends the operational coordination between the Selves for this event. The evolution feed at dissolution (D1.17) still operates: content already accumulated in the shared substrate at the point of early dissolution is handled per the dissolution hand-off protocol. Early dissolution is not a substrate-erasure event; it is a governed end-of-event with full record.

## 5. Response timeline as governance configuration

The governance response protocol operates within a bounded window. The FAI configuration (D2.12) must specify two items related to the response timeline.

First, the maximum wait duration: how long the FAI event will remain in an ESCALATED state before the default action is triggered. This duration may vary by urgency level — the FAI configuration may specify different wait windows for different urgency levels designated in the escalation notification content. What it cannot specify is an unbounded window.

Second, the default action: what happens automatically when the wait duration elapses without a governance response. Two default actions are architecturally admissible: preserve-and-continue (treat the conflict as directed-preserved under Option 2 and continue the FAI event) or early dissolution (treat the elapsed-without-response condition as triggering Option 4). The default action is itself authored governance content; it reflects the Selves' joint decision, made before the FAI event begins, about which outcome is preferable when governance is unresponsive within the window.

The default action record differs from a direct governance response in one respect: it does not carry governance attribution in the same sense as an intentional response. The conflict registry entry records the trigger condition (elapsed wait duration with no response) rather than a named authorizing body. This difference is architecturally noted but does not violate governance completeness — the default action was itself governed at the time the FAI configuration was authored. The authority for the default action traces to the governance act of authoring the FAI configuration.

## 6. Anti-pattern: unresponsive escalation

The unresponsive escalation anti-pattern occurs when an escalation is routed — the notification reaches the named governance authorities and the conflict registry entry records status ESCALATED — but no governance response is received within the wait window and no default action is triggered. The conflict remains in ESCALATED status indefinitely.

This anti-pattern violates the governance completeness commitment in two ways. First, it leaves a conflict in open state within the shared substrate indefinitely, which means the FAI event cannot proceed or dissolve in a governed manner. Second, it means the FAI configuration was authored without a required element — the default action — leaving the escalation protocol structurally incomplete.

The unresponsive escalation anti-pattern cannot arise if the FAI configuration was correctly authored. Correct authoring requires a wait duration and a default action for every urgency level the configuration recognizes. If the FAI configuration is missing either item, the configuration is incomplete, and the shared substrate construction process (D2.12) should flag the incompleteness before the FAI event begins rather than discovering it at escalation time.

Detection of the anti-pattern in a running FAI event: a conflict registry entry with status ESCALATED whose escalation timestamp exceeds the configured wait duration, and no subsequent governance response record or default action record. Remediation requires governance intervention to provide one of the four response options manually, and amendment of the FAI configuration for future events to ensure the default action is specified.

## 7. Operational test

For an escalation that has occurred within a FAI event, a system instantiates the D2.14 escalation routing and governance response protocol if and only if all of the following are true.

**Test 1 — Escalation notification as substrate content.** An observer can find the escalation notification as substrate content within the shared substrate, containing the conflict registry entry with both sides preserved, the conflict class classification, the governance reasoning for escalation, and the urgency level. Nothing material to the escalation was communicated through out-of-band channels.

**Test 2 — Routing destination as authored configuration.** An observer can find the routing destination in the FAI configuration as authored substrate content with governance attribution, specifying the governance authorities who hold cross-perimeter authority for this event. The routing destination was not determined at the moment of escalation; it was pre-specified.

**Test 3 — Governance response record with authorization and attribution.** An observer can find a governance response record for the escalation — one of the four options — authored as substrate content with the identity of the responding governance authority and the response timestamp. If the response was a default action triggered by elapsed wait duration, the record states the trigger condition and traces to the FAI configuration that authorized the default.

**Test 4 — Conflict registry entry status.** The conflict registry entry for the escalated conflict has transitioned from ESCALATED to one of: RESOLVED-BY-ESCALATION (Option 1), PRESERVED (Option 2), RESOLVED-BY-NEW-RULES or PRESERVED (Option 3), or a dissolution record (Option 4). An entry remaining in ESCALATED status past the configured wait duration with no default action record indicates the unresponsive escalation anti-pattern.

**Test 5 — Option 3 substrate effect.** If the governance response was Option 3, an observer can find new orchestration rules authored as substrate content within the shared substrate's resolve-tier rule set, with governance attribution. The rules address the conflict class that triggered the escalation. Future FAI events between the same Selves can be inspected to verify that conflicts of the same class are handled at the resolve tier without requiring escalation.

A system that passes all five tests has instantiated the escalation routing and governance response protocol in the operational form D2.14 specifies. A system that fails any test has either an incomplete escalation record, an improvised routing destination, an open escalation without governance response, or a missing option-3 rule artifact — each of which is a distinct governance completeness violation.

## 8. Conclusion

The escalate-to-humans tier of the three-tier conflict-handling mechanism is architecturally committed at D1.15. D2.14 formalizes the operational mechanics that make the commitment reliably exercisable. Three routing elements — trigger, destination, and notification content — specify how an unresolvable conflict reaches governance. Four response options — resolution, preservation direction, new orchestration rules, and early dissolution — specify what governance can do and what each option produces in the conflict registry and the shared substrate.

The most consequential framing point is that two items in the protocol are governance-configured substrate content authored before the FAI event begins: the routing destination and the response timeline with its default action. Neither is determined at escalation time. The routing destination pre-specifies who holds cross-perimeter authority; the response timeline pre-specifies what happens if they do not respond. Together these two pre-specifications make the escalation protocol self-contained: it does not depend on ad hoc authority identification or open-ended waiting.

Option 3's lasting effect differentiates it from the other response options in kind. When governance authors new orchestration rules in response to an escalated conflict, the act is not only a conflict disposition — it is a DNA-level governance act that expands the shared substrate's rule coverage for all future coordination events between the participating Selves. Governance should consider it whenever the conflict class is likely to recur, because its cost amortizes across all future events and converts a recurring escalation burden into a governed rule.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Escalation Routing and Governance Response Protocol.* May 15, 2026. ORCID: 0009-0004-8065-3235. Derivation note D2.14 (#509) in the CKS defensive-publication series.
