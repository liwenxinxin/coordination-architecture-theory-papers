# Boundary Case: Authority Distribution Change — Formalizing the Architectural Treatment of Changes to Category 5 (Who Has What Authority) in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the architectural treatment of one boundary case: changes to the substrate's authoritative content for "who has what authority over what" — Category 5 of the source-of-truth decomposition — and how that treatment preserves the coherence of historical executions, in-flight operations, and future operations.

## Abstract

The CKS pattern's source-of-truth commitment names the substrate as authoritative for five categories of coordination state, of which Category 5 — who has what authority over what — is operationally distinctive. Authority distribution changes (role changes, organizational restructuring, delegation transfers) are common in deployment and pose a non-obvious question: when authority changes, how does the architecture handle prior cell executions authorized under the previous distribution, in-flight operations spanning the change, and the case where the new distribution conflicts with rules already in the substrate? This note formalizes the answer as a standalone architectural treatment. Authority distribution change is itself substrate-resident content authored under the rule-authoring discipline; historical cell executions retain the authority context operative at execution time through provenance; new executions use the current distribution; replay reaches back to historical authority context; transition conflicts are handled per the conflict-as-first-class commitment without automatic precedence; in-flight operations are handled per the authoring rule's specification. The note states the boundary case, identifies the architectural commitments stressed, articulates the treatment, names the anti-pattern treatments that would violate it, and describes the operational implications and limits.

## 1. Why this boundary needs to be formalized as standalone

The CKS source-of-truth commitment, formalized canonically in §3.1 and §11.3 of the source paper, decomposes the substrate's authoritative content into five categories: what was decided, by whom, with what rationale, what rules apply, and who has what authority over what. The fifth category — authority distribution — is load-bearing. It answers, at any moment, which actor was permitted to do what, under which conditions, with what scope, on what substrate content and which orchestration rules. Every other category presupposes this one: a decision is recorded with attribution, but the attribution is meaningful only because authority records say what that actor was permitted to decide; a rule reference travels with the content it governs, but the reference is meaningful only because authority records say who could author or amend that rule.

Authority distribution changes are operationally common: personnel turn over, projects start and end, delegations transfer, scopes expand and contract, organizational units reorganize, regulatory regimes adjust the boundaries of who may sign what. Each is, architecturally, a change to Category 5 substrate content. The question the boundary poses is how the architecture handles such a change without violating the source-of-truth commitment about what authority *was* operative at any historical moment.

The architectural treatment is non-obvious for two reasons. First, authority is self-referential: the question "who can change the authority distribution" is itself an authority question, answered by the same substrate the change modifies. Second, an authority change creates a temporal split — prior executions occurred under the old distribution, future executions occur under the new one, and in-flight operations may straddle the boundary. A naive treatment risks two failure modes: retroactively re-interpreting historical executions under new authority (which collapses the historical record), or refusing to allow the change at all (which collapses operational reality). Standalone formalization prevents both.

This note is the sixth in Phase A6 of the Series A derivation. It follows the rule conflict resolution and rule retroactivity treatments as siblings, shares structural elements with both, and is named as standalone because Category 5 changes carry stresses the generic rule retroactivity treatment does not foreground.

## 2. The boundary case scenario

The scenario is precise. At time T, the substrate's Category 5 content names a specific authority distribution: actor A has authority X over scope S, actor B has authority Y over scope S′, and so on. Cells have been executing under this distribution; the executions are recorded in substrate content with provenance referencing the authority that was operative.

At time T+1, a human authors a change. The change may add new authority assignments, revoke prior assignments, transfer authority between actors, change the scope of an authority, restructure the boundary between authorities, or any combination. The change takes effect as substrate state per the rule-authoring discipline.

The boundary case asks how the architecture handles, from T+1 onward, (a) prior cell executions whose provenance references the pre-change authority distribution; (b) in-flight operations begun under the pre-change distribution but completing under the post-change distribution; (c) new cell executions; (d) replay of executions that occurred before T+1; (e) the case where the new authority distribution conflicts with rules already in the substrate that were authored under the prior distribution.

What makes the case non-obvious is that all five questions appear, on a casual reading, to admit different answers depending on whether one prioritizes operational current-state coherence, historical fidelity, or some compromise. The standalone treatment names a single architectural answer that handles all five consistently. A scoping note: the boundary covers authority *change* events. Authority *exercise* — an actor with authority taking an action — is a routine substrate operation with provenance and is not the subject of this note.

## 3. Architectural commitments stressed

Six commitments are stressed by the boundary, and the treatment must respect all of them simultaneously.

**Substrate as source of truth for authority (Category 5).** What "authoritative" means is stressed when the authoritative content is itself changing. The substrate must answer, at any moment, both "what is authoritative now" and "what was authoritative then" without contradiction.

**Rule authoring as the mechanism of change.** Authority changes are themselves changes to the rule structure that defines who may do what. No other mechanism is admissible — not vendor IAM, not LLM inference, not implicit cascade.

**Path retraceability across the change.** The retraceability commitment requires every cell execution to be reconstructible in full, including the authority context under which it occurred. The change must not erase or reinterpret historical authority context.

**The determinism contract for replay.** Replay of a historical execution must produce the same result, which presupposes that replay uses the historical authority context — authority-as-of-execution-time, not authority-as-of-replay-time.

**Conflict as first-class object during transition.** A new authority distribution may conflict with rules authored under the prior one — a rule referencing an actor who no longer holds the relevant authority, or a rule whose conditions presupposed an authority structure now revised. Such conflicts must be registered as substrate content, not silently resolved or elided.

**Human governance as the source of the change.** The change must originate in human authoring, not in inferred policy, vendor-managed identity systems, or compliance-framework propagation. Authority changes are precisely the moments where the human-authority commitment is most visible.

## 4. The architectural treatment

The treatment is a single coherent pattern with five operational parts.

**The authority change is itself substrate-resident content authored under the rule-authoring discipline.** The new authority distribution is recorded as substrate content with full provenance: who authored the change, when, under what authority, with what rationale, with reference to whatever prior rule or distribution it supersedes. The change is visible to inspection, modifiable, and overridable at any time. Authority changes are not exceptional events handled outside the substrate; they are substrate changes handled by the same machinery as any other rule authoring.

**Historical cell executions remain associated with the authority distribution operative at execution time.** Cell-execution provenance records the specific authority context, not a generic identifier that resolves to "whatever the current distribution says." The historical association is immutable: the change at T+1 does not retroactively rewrite the provenance of executions recorded at T or earlier.

**New cell executions use the current authority distribution; replay uses the historical authority context.** From T+1 onward, executions are evaluated against the post-change distribution and recorded with provenance pointing to it. When an execution recorded at T or earlier is replayed, the reproducibility commitment reaches back through provenance to the authority distribution operative at that earlier time and uses it for the replay. Replay does not produce different results before and after the authority change.

**Transition conflicts are handled per the conflict-as-first-class commitment.** Where the new authority distribution creates contradictions with rules already in the substrate — a rule that presupposes the prior distribution, or an authorization the new distribution would not have permitted but has already been recorded — the contradiction is registered as substrate content with its own identity and provenance. No automatic precedence applies; a human-authored meta-rule resolves it. Worked example: a prior rule said "X can authorize purchases up to $1000," a new rule says "up to $500," and X's prior $700 authorizations are pending. The conflict is registered, and a human-authored meta-rule resolves it explicitly — by validating under the prior rule, re-authorizing under the new one, or some other choice.

**In-flight operations are handled per rule specification.** Where operations are executing across the boundary at T+1, the rule that authorizes the authority change specifies the in-flight handling: completion under prior authority, interruption and reauthorization under new authority, or queueing for human review. The choice is itself authored content; no implicit default applies.

The pattern supports authority versioning naturally: each change is substrate-resident with provenance, and humans inspecting historical state can determine the authority context that applied at any historical moment by following the provenance chain.

## 5. Anti-pattern treatments that violate the architecture

Seven anti-pattern treatments would violate the architecture, and naming each is part of the standalone formalization.

**Authority-retroactive-revocation.** An authority change rewrites historical authority context — for example, marking past executions as "now unauthorized" because the authorizing actor's authority has since been revoked. This violates path retraceability: the historical record no longer answers what was authoritative at time T.

**Authority-change-without-rule.** Authority changes happen outside the rule-authoring discipline — by direct database edit, vendor configuration change, undocumented runtime intervention. The change is not human-authored as substrate content and is operationally invisible to inspection and override.

**LLM-mediated authority changes.** An LLM authors changes to the authority distribution. The LLM operates as substrate mediator, not as source of authority; LLM-drafted authority changes are admissible only when subject to human authority before they take effect. LLM-committed authority changes outside human authority instantiate the LLM-as-authority anti-pattern.

**Vendor-managed authority.** The authority distribution is held in vendor IAM systems and the substrate merely references those systems' state. The substrate is not authoritative for Category 5 in this configuration; the vendor is. Vendor identity infrastructure may participate in identity verification or login enforcement without owning the authority record; what is ruled out is treating the vendor's representation as the substrate's source of truth for authority.

**Automatic-authority-cascade.** Authority changes propagate automatically without an explicit authoring rule — for example, "manager X leaves, X's delegations to Y automatically revoke," or "project ends, all project-specific authorities expire." Cascades are legitimate when themselves authored: a human-authored rule specifies the cascade behavior, and the rule is substrate-resident with provenance. Cascades that operate as side effects of vendor systems or identity-management defaults — without an explicit rule — instantiate the anti-pattern.

**Authority-change-silently-changes-historical-interpretation.** Historical events are reinterpreted under new authority without explicit reprocessing — for example, audit reports that, after an authority change, retroactively present past decisions as if evaluated under the new authority. The legitimate pattern is explicit reprocessing as a separate substrate event with its own authority and provenance; silent reinterpretation collapses the distinction between what was authoritative and what is now considered correct.

**Compliance-framework-driven authority.** Compliance frameworks impose authority changes without human authoring — automated regulatory enforcement that adjusts the authority distribution outside the rule-authoring discipline. Compliance frameworks may inform what humans choose to author; they may not author authority changes themselves. The change must originate in human authoring, with the compliance rationale recorded as part of the change's provenance.

## 6. Operational implications

Three operational implications follow.

**Authority changes are governance events.** Every authority distribution change is an exercise of human authority, recorded as substrate content, visible to inspection, modifiable, overridable. Deployments encountering authority changes should treat them as governance moments, not as operational reconfigurations handled outside the substrate.

**In-flight handling is a rule decision.** The handling of operations that span an authority change is determined by the authoring rule, not by an implicit default. Deployments should specify the in-flight handling explicitly: complete under prior authority, interrupt and reauthorize, or queue for review.

**Historical authority is preserved through provenance, not through the current distribution.** Audit, replay, and historical inspection use the authority context recorded with the execution at the time it occurred. Deployments should not implement audit by querying the current authority distribution against historical events; that produces incorrect results when authority has changed and silently shifts the meaning of the historical record.

## 7. Limits of the architectural treatment

Three limits scope the treatment.

**The treatment applies to Category 5 changes specifically.** Other source-of-truth category changes — what was decided, by whom, with what rationale, what rules apply — follow the rule retroactivity treatment formalized separately. The Category 5 treatment shares structural elements with that treatment but emphasizes authority-specific stresses: self-reference, transition conflicts, in-flight handling.

**The treatment does not cover composition partner authority through composition reconfiguration.** Where multiple substrates compose, the authority distribution may be jointly determined by composition rules across substrates. Changes through composition reconfiguration follow the composition treatment, not this one. The boundary between the two is whether the change occurs within a single substrate's authority record (this note) or across substrates' joint authority structure.

**The treatment does not adjudicate the legitimacy of any specific authority change.** Whether a particular change is wise, lawful, or organizationally appropriate is outside the architectural commitment. The architecture handles whatever change a human authors as substrate content with provenance; it does not evaluate the change against external criteria. The legitimacy question is properly held by the humans authoring the change and by the broader governance regime in which the deployment sits.

## 8. Operational test

A system instantiates the authority distribution change treatment if and only if all of the following hold at all times the substrate is in operation:

1. Authority changes are substrate-resident content authored under the rule-authoring discipline, with full provenance recording who authored the change, when, under what authority, and with what rationale.
2. Cell-execution provenance records the authority context operative at execution time; that record is immutable to subsequent authority changes.
3. New cell executions use the current authority distribution; replay uses the historical authority context recorded in provenance.
4. Transition conflicts between new authority and existing rules are registered as first-class substrate content with their own identity and provenance, and resolved by human-authored meta-rules without automatic precedence.
5. In-flight operation handling at the moment of change is specified by the authoring rule, not by implicit default.

A system that fails any of (1)–(5) may be a useful system, and may handle authority changes in some other coherent way, but is not handling them in the CKS sense.

## 9. Why naming this boundary as standalone matters

The Phase A6 framing treats each boundary case as a standalone architectural specification, derived from the source paper's commitments without introducing new axioms. The authority distribution change boundary earns standalone treatment because authority changes are operationally common, the architectural treatment is non-obvious, and the canonical anti-patterns — retroactive revocation, automatic cascade, vendor-managed authority, compliance-framework propagation — are common enough in adjacent practice that naming each as a violation has prior-art value. Discussions of "AI authority" and "AI governance" in the surrounding literature frequently presuppose one or another of these anti-patterns without naming it; the standalone formalization here pins the architectural alternative in place.

The note completes the sixth Phase A6 entry. Subsequent notes cover substrate near-capacity, network partition, and additional boundary cases. The Phase A6 cumulative effect is a comprehensive catalog of the boundary cases the CKS pattern handles by explicit architectural specification rather than by deferral to ad hoc deployment practice.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Boundary Case: Authority Distribution Change — Formalizing the Architectural Treatment of Changes to Category 5 (Who Has What Authority) in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
