# Home Perimeter Integrity During FAI

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series note:** D2.17 — derivation from D1.03 (Phase D2, #512)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When a CKS-governed organizational Self participates in a Full Aspect Integration (FAI) event, it contributes aspects to a temporary shared substrate that spans multiple Selves' home governance perimeters. D1.03 commits that the inter-Self perimeter is additive — it supplements each participating Self's home governance architecture rather than replacing or modifying it. This note operationalizes that commitment. It states four properties that must hold for a participating Self's home perimeter to be considered intact during an active FAI event: contributed DNA remains unmodified in the home substrate; home governance authority is undiminished; non-contributed aspects are unaffected; and home operations continue independently. It then states three verification checks by which governance can confirm after the fact that all four properties held. Finally, it names the sovereignty guarantee these properties compose and the anti-pattern their violation produces.

---

## 1. D2.17 as operational decomposition of D1.03

D1.03 established the foundational commitment for inter-Self FAI participation: the governance perimeter formed across participating Selves' home perimeters is additive, not substitutive. The shared substrate acquires its own governance scope — a joint-authority scope spanning each participant's home perimeter — but that joint scope does not consume, suspend, or diminish the home perimeters it spans. Each participating Self enters a FAI event with a home governance perimeter; it exits with the same home governance perimeter, unchanged by the fact of having participated.

D1.03's commitment is stated at the architectural level. D2.17 asks what that commitment means at the operational level: what must be true of home substrate records, governance actions, and DNA content during and after a FAI event for an observer to conclude that the additive perimeter commitment was honored?

Four properties answer the question. They are not independently derived; each one follows from a different facet of D1.03's additive commitment. Taken together, they constitute a completeness argument — if all four properties hold throughout a FAI event, the event was additive with respect to the participating Self's home governance architecture.

---

## 2. Property 1 — Home DNA unchanged by FAI contributions

When a participating Self's governance selects aspects for contribution to the shared substrate (as formalized in D2.06), the contribution event produces a contribution record in the home substrate. That record is new substrate content. What the record does not do is modify, delete, or move the contributed aspects within the home substrate. The contributed aspects remain in the home substrate exactly as they were before the contribution event. Their DNA content is unchanged; their governance records are unchanged; their structural position within the home substrate's aspect hierarchy is unchanged.

This property rests on the distinction between *contribution* and *transfer*. Transfer would remove content from the home substrate and place it in the shared substrate. Contribution copies a representation of selected aspects into the shared substrate while leaving the originals intact. The shared substrate and the home substrate hold different objects — the shared substrate holds the contributed representation; the home substrate holds the original aspects. The two are related by provenance, not by identity.

FAI-origin changes to home DNA — situations where content from the shared substrate becomes home DNA — can only occur through the directed selection absorption protocol formalized in D2.11. That protocol is explicitly home-governance-authorized: it requires a home governance decision to select, authorize, and record the absorption. The protocol is not triggered automatically by FAI participation; it requires an affirmative home governance action. Until that action occurs, what is in the shared substrate stays in the shared substrate.

A corollary: if an observer compares home DNA at the start and end of a FAI event and finds that contributed aspects have been modified, that modification is unexplained by FAI participation itself. The only valid explanations are home-governance-authorized directed selection events that operated on those aspects during the event period (independently of the FAI event), or an absorption event under D2.11. If neither explanation can be supplied, a governance anomaly has occurred.

---

## 3. Property 2 — Home governance authority undiminished

During a FAI event, the shared substrate is under joint governance authority — the governance structures of all participating Selves hold authority over the shared substrate's content together. That joint authority is scoped to the shared substrate. It does not extend into any participating Self's home perimeter.

A participating Self's governance retains full authority over its home substrate content during the entire FAI event period. The three governance rights — inspect, modify, override — apply to home content without restriction and without requiring joint authorization. Home governance can modify any aspect in the home substrate at any point during the FAI event. It can override any operation within the home substrate. It can inspect any home substrate content. None of these actions require coordination with, consent from, or notification to the governance structures of other participating Selves.

This property is what preserves organizational autonomy during inter-organizational FAI participation. An organization that retained full authority over its own substrate before entering a FAI event retains that full authority throughout the event and after it. FAI does not create a period during which home governance authority is suspended, shared with external parties, or conditioned on joint approval.

A misreading to preempt: the joint authority over the shared substrate is not a generalization of home authority. It is a separate governance scope, operating on a separate substrate object, under a separate governance architecture. The shared substrate's joint authority governs what happens to shared substrate content. Home authority governs what happens to home content. The two scopes are distinct; neither contains the other.

---

## 4. Property 3 — Non-contributed aspects unaffected

Not all of a participating Self's aspects are contributed to the shared substrate. D2.06 Step 1 specifies that contribution requires explicit selection by home governance. Aspects not selected — those that remain entirely within the home perimeter — are entirely unaffected by the FAI event.

"Unaffected" means three things. First, no content from other participating Selves enters the home substrate through non-contributed aspects. The shared substrate does not have write access to home substrate content that was not explicitly brought into it by contribution. Second, the existence of the FAI event creates no implicit exposure of non-contributed aspects to other participants. Other Selves can access only what has been explicitly contributed to the shared substrate; non-contributed aspects are not visible to them. Third, non-contributed aspects are not altered, annotated, or restructured by FAI operations. Whatever FAI operations occur within the shared substrate operate entirely within the shared substrate's scope.

This property is the foundation of the contribution-selection governance design. Home governance's authority to select which aspects to contribute is meaningful only if the selection is consequential — only if non-selected aspects are genuinely protected from FAI-event effects. Property 3 closes the loop: selection is not merely a formality that determines what gets copied; it is the boundary between what is within FAI scope and what is outside it.

---

## 5. Property 4 — Home operations continue independently

FAI events and home governance operations are concurrent. The FAI event does not suspend, pause, or interrupt home governance operations. During an active FAI event, the full range of home governance operations continues: directed selection events may occur, modifying home DNA through home-governance-authorized processes; mutation governance continues to operate; action-feedback evolution continues to process operational evidence and route proposals through the governance-authorization pathway; governance records continue to accumulate.

This property is an integrity requirement, not merely a permission. It would be operationally coherent for a governance team to choose to pause certain home governance activities while a FAI event is in progress — for instance, to avoid creating DNA changes that complicate the post-event comparison required by Check A. But the architecture does not require this pause, and governance should not pause home operations *because* a FAI event is in progress. Pausing home governance because FAI is active would be a form of home authority erosion — treating FAI participation as a condition that restricts home governance scope — which contradicts D1.03's additive commitment.

The continuity of home operations has a verification implication: home governance records should show continuous operation across the FAI event period. A gap in home governance records that coincides with a FAI event period is evidence that home operations were suspended during the event, which is an anomaly worth investigating.

---

## 6. Three verification checks

The four properties above are architectural commitments. Verification requires that governance be able to confirm, after a FAI event, whether each property held. Three checks compose an adequate verification protocol.

**Check A — Pre/post DNA comparison.** Governance compares home DNA at the start of the FAI event period with home DNA at the end. Any changes found must be attributable to one of two authorized channels: (a) home-governance-authorized directed selection events that occurred during the FAI period independently of FAI, or (b) DNA absorption events explicitly authorized under D2.11. This is an attribution requirement, not a prohibition on change. DNA can change during a FAI event period — it simply must change through authorized channels. Changes that cannot be attributed to either channel are unexplained DNA modifications, which constitute a governance failure requiring investigation. The check should include contributed aspects specifically: if a contributed aspect's DNA was modified during the FAI period and the modification cannot be attributed to a home-governance-authorized directed selection event, the modification is anomalous under Property 1.

**Check B — Home governance record continuity.** Governance reviews the home substrate's governance record for the FAI event period. The record should show continuous home governance operation — directed selection events, mutation governance actions, action-feedback proposals and authorizations — throughout the period. Gaps in the governance record that coincide with the FAI event period indicate that home governance operations were suspended during the event. Suspension is not automatically a property violation — governance may have had legitimate operational reasons — but it is a pattern inconsistent with Property 4 and warrants explanation. A continuous governance record, by contrast, is affirmative evidence that home operations ran independently of the FAI event.

**Check C — Contributed aspect integrity.** Governance confirms that aspects selected for contribution are present in the home substrate after the FAI event in the same structural state they occupied before. This means: the aspects exist, their DNA content is unchanged (absent Check A-accountable changes), their position in the home substrate's aspect hierarchy is unchanged, and no content from the shared substrate has been written into them other than through D2.11-authorized absorption. Check C is a targeted audit of the specific aspects that had a representation in the shared substrate during the event — the aspects that were most directly in contact with the inter-organizational boundary.

The three checks are designed to be executable from home substrate records alone, without access to the shared substrate's records. This is deliberate: a participating Self should be able to verify its own home perimeter integrity independently, without depending on cooperation from other participating Selves or on access to the shared substrate's governance records.

---

## 7. The sovereignty guarantee

The four properties and three checks compose a guarantee that home governance can communicate to its organizational stakeholders: participating in a FAI event does not change your home governance architecture, does not diminish your home governance authority, and does not expose your non-contributed aspects to other participating Selves.

This guarantee is not a post-hoc reassurance. It is an architectural commitment derivable from D1.03's additive perimeter principle: if the inter-Self perimeter is genuinely additive, then the existence of the shared substrate cannot modify what already exists in the home perimeter. Each property above is a direct consequence of the additive commitment applied to one facet of home governance.

The guarantee matters for a specific organizational reason. Before a CKS-governed organizational Self agrees to participate in a FAI event, its governance must have confidence that participation is bounded and reversible. Bounded: the scope of the inter-organizational exchange is limited to contributed aspects under joint authority, with no automatic propagation into home content beyond what home governance authorizes through D2.11. Reversible: after the FAI event dissolves, the participating Self's home governance architecture is exactly as it was before participation, except for explicitly authorized absorptions. Without this guarantee, governance teams would rationally treat FAI participation as a governance risk — a period during which some home governance authority is transferred to an external joint structure. The sovereignty guarantee eliminates that risk by specifying that no authority is transferred.

---

## 8. Anti-pattern: home perimeter erosion

The failure mode directly opposed to home perimeter integrity is home perimeter erosion — FAI participation that results in unintended changes to home DNA, reduced home governance authority, or involuntary exposure of non-contributed aspects.

Erosion can occur through several mechanisms. Unauthorized propagation occurs when content from the shared substrate enters home substrate content outside the D2.11 absorption protocol — for instance, through a technical implementation that writes shared-substrate content directly to home substrate fields during FAI operations. Authority dilution occurs when a participating Self's governance begins treating joint-authority decisions as binding over home content, effectively extending the shared substrate's joint authority into the home perimeter. Contribution creep occurs when aspects not explicitly selected for contribution are treated as implicitly contributed — for instance, when a FAI implementation traverses aspect dependencies and includes aspects that home governance did not explicitly select.

Each erosion mechanism is detectable by the three checks. Unauthorized propagation surfaces in Check A as unattributed DNA changes or in Check C as non-D2.11-authorized content appearing in contributed aspects. Authority dilution surfaces in Check B as gaps in home governance records or as home governance actions that reference joint-authority approvals as preconditions. Contribution creep surfaces in Check C as aspects that were not explicitly selected appearing to have been modified by FAI operations.

The anti-pattern is named here because implementation decisions can erode the home perimeter without architects or governance teams recognizing that erosion is occurring. Checking for the anti-pattern requires active verification using the three checks — passive observation of FAI outcomes is insufficient, because erosion that has not yet propagated to visible home content may be undetected until a later directed selection event makes the unauthorized change visible.

---

## 9. Operational test

After a FAI event in which a given Self participated, an observer with access to that Self's home substrate records can apply the following test to determine whether home perimeter integrity held throughout the event.

The test passes if and only if all of the following are true:

1. Every change to home DNA during the FAI event period can be attributed to either a home-governance-authorized directed selection event (independent of FAI) or a D2.11-authorized absorption event — and both types of change are recorded in the home governance record.

2. The home governance record shows continuous operation throughout the FAI event period, with no gaps attributable to FAI event activity.

3. Aspects selected for contribution to the FAI event are present in the home substrate in the same structural position as before the event, with DNA content that is either (a) unchanged, or (b) changed in a way fully accounted for by the attribution in item 1.

4. No content from other participating Selves appears in non-contributed aspects or in home DNA content outside of D2.11-authorized absorptions.

A test that passes on all four conditions constitutes confirmation that the participating Self's home governance architecture was not modified by FAI participation — that the inter-Self perimeter was additive, as D1.03 committed.

---

## References

- Li, W. (April 2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.*
- Li, W. (April 2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.*
- Li, W. (April 2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.*
