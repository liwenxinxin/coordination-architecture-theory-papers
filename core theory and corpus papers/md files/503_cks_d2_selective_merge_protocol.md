# Selective Merge Governance Protocol

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI) — the canonical operation over the shared substrate in Paper 3 of the CKS theory series — supports three pattern variants: full merge (the architectural default), selective merge, and lineage-preserved union. This note formalizes the governance protocol for the selective merge variant. Selective merge differs from full merge in that governance curates which contributed content enters the shared substrate's combined state, rather than combining everything and registering conflicts after the fact. The curation is not a system default; it is a governed operation carried out in five steps: selective merge configuration, content review, selection decisions, selection record, and excluded content treatment. The note formalizes each step operationally, identifies the modify right (inherited from Paper 1 Claim 3 through Paper 3's inter-Self scope) as the governance foundation for selective merge, distinguishes selective merge from full merge as a governance tradeoff rather than a hierarchy, names the anti-pattern of pseudo-selective merge in which selection proceeds without explicit governance decisions, and provides an operational test for verifying that a selective merge event was genuinely governed.

---

## 1. Why selective merge requires explicit governance protocol

When governance configures an FAI event to use selective merge rather than full merge, it accepts a different distribution of governance work. In full merge, all contributed aspects enter the shared substrate's combined state; conflicts that arise from combining potentially incompatible content surface as first-class substrate state and are handled post-merge through the three-tier conflict-handling mechanism. The governance work is concentrated after the merge. In selective merge, governance intervenes before or during combination to decide which content enters the combined state at all. The governance work is concentrated before or during the merge.

The front-loading of work in selective merge has a structural implication: without an explicit protocol, there is nothing to distinguish a governed selection from a system-default filter. Any merge mechanism that includes or excludes content based on heuristics, field-type rules, or automatic compatibility checks performs a kind of selection — but that selection reflects system logic, not governance authority. The architectural commitment that separates FAI from opaque inter-agent merge (Paper 3, §5.2) is precisely that merge logic is authored substrate content under joint human authority, not a system default around which governance operates as a wrapper. Selective merge, as one of FAI's three pattern variants, must satisfy this commitment in the same way full merge does. The governance protocol is what makes it do so.

This note formalizes the protocol in five steps, then addresses its governance foundation, its tradeoff relationship with full merge, and the anti-pattern it must be distinguished from.

---

## 2. Step 1 — Selective merge configuration

Before the FAI event begins (or, in governance architectures that permit it, at the opening of the event), the jointly-configured governance specifies that this event will use selective merge rather than the full-merge default. That specification is itself substrate content under Paper 3's Claim 5 commitment that all configurable dimensions of FAI are substrate content with recursive applicability. The configuration records two things.

First, the **selection scope**: which content types or which aspects' content categories are candidates for curation. Selection scope may be defined broadly ("all DNA-layer rules from contributing aspects") or narrowly ("the behavior substrates from Aspect X of Self A and Aspect Y of Self B only"). The scope definition bounds what Step 2 reviews and what Step 3 decides; content outside scope is handled by the event's fallback behavior, which is itself a governance specification.

Second, the **approval mechanism**: how selection decisions in Step 3 will be authorized. The approval mechanism may designate specific human governance authorities, specify which Self's governance holds authority over which content categories, or define a joint-approval requirement for content that comes from more than one Self. The approval mechanism is what makes the selection decisions in Step 3 attributable to specific governance authorization rather than to a system process.

Both specifications are written as substrate content before the merge proceeds. Their presence is what activates the protocol; their absence means the event is not configured as a selective merge governed event.

---

## 3. Step 2 — Content review

Governance reviews the contributed aspects' content — DNA-layer content (orchestration substrates, behavior substrates, schemas, rules) and action-layer content (recorded task instances, outputs, lived experience) from all contributing Selves — within the selection scope specified in Step 1. The review has a defined purpose: to produce a categorization of contributed content along three axes that inform the Step 3 selection decisions.

**Compatibility axis**: which content is compatible across all contributing Selves in the sense that combining it would produce a coherent combined state. Compatible content is the strongest candidate for inclusion. Compatibility is a governance determination, not a system determination; governance evaluates whether combining this content would serve the coordination purpose of the FAI event, not merely whether the content can be mechanically joined.

**Specificity axis**: which content is specific to one Self's operational context in ways that make it unsuitable for a combined state shared across Selves. A rule calibrated to one Self's infrastructure, a behavior substrate tuned to one Self's user population, or a task record whose action-layer content only makes sense in one Self's history may be candidates for exclusion from the combined state while remaining valuable content within the contributing Self's home substrate.

**Conflict axis**: which content conflicts across contributing Selves — where the same aspect, rule, or content category carries incompatible versions from different Selves. Conflicts in selective merge are handled in one of two ways: governance may resolve the conflict by selecting one version for inclusion and excluding the other (with the exclusion recorded in Step 4 and the excluded content preserved in Step 5), or governance may hold the conflict as first-class substrate content without combining either side (the HOLD decision in Step 3, which produces an outcome equivalent to the preserve tier of the three-tier conflict-handling mechanism).

The content review produces an annotated inventory of contributed content, categorized by these three axes, that becomes the input to Step 3.

---

## 4. Step 3 — Selection decisions

For each content category identified in the Step 2 review, governance makes an explicit selection decision. There are three possible decisions.

**INCLUDE**: this content enters the shared substrate's combined state. An INCLUDE decision reflects governance judgment that combining this content serves the coordination purpose of the FAI event and that the combined state is a better representation of the contributing Selves' coordination than each Self's content individually.

**EXCLUDE**: this content is not included in the shared substrate's combined state for this FAI event. An EXCLUDE decision may reflect content that is context-specific, redundant, lower quality for the combined state's purposes, or otherwise inappropriate for combination — based on governance judgment. Excluded content is not discarded; the treatment of excluded content is formalized in Step 5.

**HOLD**: this content is preserved as first-class substrate content in the shared substrate but is not combined. HOLD is governance's election to treat a conflict or ambiguity like the preserve tier of the three-tier conflict-handling mechanism: both sides (or all versions) remain in the shared substrate as attributed content, available for governance inspection and for subsequent resolution, but they do not enter the combined state. The distinction between EXCLUDE and HOLD is that EXCLUDE reflects a determination that the content should not be part of the combined state, while HOLD reflects a determination that the content should remain present and addressable but that the combining question is not yet resolved.

Selection decisions apply at the content-category granularity that the Step 2 review produced. Every category must receive a decision; governance may not leave categories in an undecided state, because an undecided category would fall back on system defaults rather than governance authority — which is the pseudo-selective merge anti-pattern (§7 below).

---

## 5. Step 4 — Selection record

Every selection decision from Step 3 is written as substrate content in the shared substrate. The selection record is the governance artifact that makes selective merge a governed operation. Each record entry carries four components.

**What was decided**: the content category, the decision (INCLUDE, EXCLUDE, or HOLD), and any parameters of the decision (for example, which version of conflicting content was selected for INCLUDE, or what condition would need to be met for a HOLD to be resolved).

**Who authorized the decision**: the governance authority — specific humans, governance bodies, or governance instruments — whose authorization the decision carries. Attribution to the approval mechanism specified in Step 1.

**When**: the timestamp of the decision, establishing temporal position within the FAI event.

**Why**: the governance reasoning, in the form of a human-authored rationale that records what governance weighed in reaching the decision. The reasoning is not a system-generated justification; it is the authored record that makes the decision inspectable as a governance act rather than as a system output.

The selection record is the audit trail for the FAI event as a whole. It is the object that an observer, a future governance review, or a subsequent FAI event can consult to understand what was decided and why. Without the selection record, there is no way to verify that selection decisions were made under governance authority rather than system logic.

The selection record is retained in the shared substrate through the event's persistence policy. Because it is substrate content, it is subject to the inspect right: governance can review the selection record at any time. Under a persistence policy that retains the Locus 2 durable record of the FAI event, the selection record is part of that durable record.

---

## 6. Step 5 — Excluded content treatment

Content that received an EXCLUDE decision in Step 3 is not discarded. This is the application of the conflict-preservation principle — first established in Paper 1 (Claim 2) and carrying through all three papers of the CKS trilogy — to the selection act itself. In the same way that full merge preserves both sides of a conflict as first-class substrate state rather than silently resolving it, selective merge preserves excluded content as attributed substrate content rather than losing it.

Specifically: excluded content remains in the shared substrate as attributed to its contributing Self's aspect. The attribution is explicit — the substrate record identifies the content's source Self, source aspect, and the FAI event during which it was contributed and excluded. The content is available to the inspect right: governance can examine it alongside the selection record from Step 4, which records the reasoning for exclusion. It is not part of the combined state, but it is not absent from the substrate.

If the shared substrate's persistence policy retains the Locus 2 durable record of the FAI event, excluded content is eligible to appear in that durable record alongside the selection record. This means that the evolution feed each participating Self draws from at FAI dissolution includes, potentially, both the combined state content and the attributed record of content that was excluded and why. A Self's subsequent governance may review the excluded content and decide to incorporate it into the Self's home substrate through a different mechanism, even though it did not enter the shared combined state.

Content that received a HOLD decision in Step 3 is treated similarly: it remains in the shared substrate as first-class content, attributed to its contributing sources, with the HOLD record from Step 4 identifying its status. It is available to the inspect right and eligible for the Locus 2 durable record.

The excluded-content treatment is not optional. A selective merge operation that discards excluded content rather than preserving it with attribution has violated the conflict-preservation principle at inter-Self scope, regardless of whether the selection decisions themselves were properly governed.

---

## 7. The modify right as governance foundation

Selective merge is an exercise of the joint modify right over what enters the shared substrate's combined state. The modify right — the right of human governance to modify any substrate content and any orchestration rule at any time — is one of the three governance rights Paper 1 formalizes (inspect right, modify right, override right) as the definition of "human-governed" at the CKS pattern level. That right carries through Paper 2 at intra-Self scope and through Paper 3 at inter-Self scope, where it becomes a joint authority across the participating Selves' governance.

In selective merge, the joint modify right is exercised at a specific moment: the moment of deciding what enters the combined state. The selection decisions in Step 3 are the acts of governance authority that determine the content of the combined state. The LLM operating as substrate mediator does not make these decisions; the shared substrate infrastructure does not make these decisions; the governance-configured orchestration does not make these decisions autonomously. The decisions are made by human governance under the joint authority structure and recorded as substrate content in Step 4.

This is what distinguishes selective merge from any filtering or transformation that a merge mechanism might apply to contributed content. A merge mechanism can reduce, clean, deduplicate, or transform content — but these are operations over content, not governance decisions about what enters the combined state. The modify-right foundation requires that the decisions about combined-state membership be made by governance, not by the system.

---

## 8. Selective merge versus full merge: the governance tradeoff

Selective merge and full merge are both valid FAI pattern variants. Neither is architecturally superior to the other; the choice between them is a governance judgment per FAI event, informed by the coordination purpose of the event and the governance capacity available.

The tradeoff is a distribution of governance work across the timeline of the FAI event:

Selective merge concentrates work before or during combination. Governance must conduct the content review (Step 2), make selection decisions for every content category (Step 3), and record those decisions (Step 4). This work is governance-intensive. Its benefit is a combined state that enters the post-merge shared substrate with fewer conflicts, because content that governance determined would produce unhelpful conflicts was excluded before combination.

Full merge concentrates work after combination. Everything enters the combined state, and conflicts that arise from combining potentially incompatible content surface as first-class substrate state. Those conflicts are then handled through the three-tier mechanism: preserve, resolve via orchestration, or escalate to humans. The work of reviewing and deciding which content belongs in the combined state does not disappear — it migrates into the conflict-handling phase.

The practical guidance is this: selective merge is the better choice when governance can predict, in advance, that certain content from the contributing Selves will produce conflicts that are more efficiently managed by not combining the content at all. Full merge is the better choice when the conflicts that will arise are not predictable in advance, or when combining everything and surfacing conflicts post-merge is less expensive than conducting the upfront review selective merge requires. Governance makes this judgment per FAI event, and the configuration from Step 1 records the choice as substrate content.

---

## 9. Anti-pattern: pseudo-selective merge

The governance protocol formalized above identifies a specific failure mode: pseudo-selective merge.

Pseudo-selective merge occurs when governance nominally configures an FAI event as selective merge — specifying that only certain content will enter the combined state — but the selection decisions are made by system defaults rather than by explicit governance authority. The markers of pseudo-selective merge are: the absence of Step 3 selection records with governance attribution, the absence of an approval mechanism specification in Step 1, or selection results that can be fully explained by system-level heuristics (field-type compatibility, schema alignment, content deduplication logic) without reference to governance decisions.

Pseudo-selective merge violates the modify-right governance requirement in the same way that any opaque merge does: the decisions about what enters the combined state are not made by governance and are not inspectable as governance acts. The fact that the result may look similar to a governed selective merge does not satisfy the architectural commitment. The commitment requires that the selection be an act of governance authority, recorded as substrate content — not that the result happen to match what governance might have decided.

The test for pseudo-selective merge is the same as the operational test in §10 below: can an observer find the explicit selection decision records? If not, selective merge did not occur in the governed sense, regardless of how the event was configured.

---

## 10. Operational test

For an FAI event configured as a selective merge, the event satisfies the selective merge governance protocol if and only if all of the following are true.

1. The shared substrate contains a Step 1 configuration record specifying: that this event uses selective merge, the selection scope (which content categories are subject to selection decisions), and the approval mechanism (which governance authority authorizes selection decisions).

2. The shared substrate contains Step 3 selection decision records covering every content category within the selection scope. Each record carries an INCLUDE, EXCLUDE, or HOLD decision with explicit governance attribution — identifying who authorized the decision — a timestamp, and a human-authored governance reasoning statement.

3. Every content category within the selection scope received a selection decision. No category was left undecided (which would cause it to fall back on system defaults).

4. Content that received EXCLUDE or HOLD decisions is present in the shared substrate as attributed content — identified by source Self, source aspect, and event — and is not absent from the substrate. It is accessible to the inspect right.

5. The selection decisions are not fully explainable as system-default outputs. The governance reasoning from (2) records a governance judgment that goes beyond what the system would have done in the absence of explicit governance authority.

A selective merge event that fails any of (1) through (5) is either an unconfigured full merge, a pseudo-selective merge, or an incomplete governed selective merge. It does not satisfy the governance protocol this note formalizes.

---

## 11. Conclusion

Selective merge is not a softer version of full merge. It is a different distribution of governance work: front-loaded curation rather than post-merge conflict handling. The governance protocol it requires — five steps from configuration through excluded content treatment — is more demanding in the pre-merge phase precisely because it reduces the post-merge work. That tradeoff is what governance weighs when configuring an FAI event.

The selection record (Step 4) is the artifact that makes selective merge governed rather than filtered. Without explicit selection decision records carrying governance attribution, the operation is pseudo-selective merge, not governed merge. The excluded content treatment (Step 5) is the artifact that extends the conflict-preservation principle to the selection act itself: even content that governance chose not to combine is preserved with attribution, remains available to the inspect right, and can appear in the durable record of the event.

Both of these requirements — the selection record and the excluded content treatment — derive directly from Paper 1's substrate commitments carried through Paper 3's inter-Self scope. Selective merge at inter-Self scope is the same architectural commitment as selective merge at intra-Self scope, under the joint governance authority that Paper 3's shared substrate creates.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Selective Merge Governance Protocol.* May 15, 2026. ORCID: 0009-0004-8065-3235.
