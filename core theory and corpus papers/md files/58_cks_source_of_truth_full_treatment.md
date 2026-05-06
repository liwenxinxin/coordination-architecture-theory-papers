# Substrate as Source of Truth: Full Operational Treatment of the Five Authoritative Categories in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 4, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the integrating-frame structure of the substrate-as-source-of-truth commitment: the five categories of coordination question for which the substrate is architecturally authoritative, the source-of-truth-vs-mirror-of-truth distinction, and the connection to the path-retraceability commitment that operationally defends substrate authority.

## Abstract

The substrate-as-source-of-truth commitment introduced in the parent note A1.08 is the architectural anchor several other CKS commitments depend on: path retraceability, AI-as-substrate-mediator, conflict preservation, determinism on the substrate side of the governance boundary, and linear-cost scaling all lose operational meaning if the substrate is not the authoritative answer to coordination questions. This note formalizes the commitment at the integrating-frame level. It states the five categories of coordination question for which the substrate is architecturally authoritative ("what is the case," "what was decided," "what is in conflict," "what rules apply," "who has what authority"); states the source-of-truth-vs-mirror-of-truth distinction that differentiates CKS from architectures where the substrate is a derivative view of state held authoritatively elsewhere; identifies the path-retraceability commitment, recently decomposed in A1.07 / A2.35–A2.41, as the architectural foundation that operationalizes substrate authority; states what the commitment does NOT claim; and provides an integrating-level operational test. The note pairs with A2.43–A2.47 (each authoritative category as standalone) and A2.48 (the source-of-truth-vs-mirror-of-truth distinction as standalone) to give the full operational decomposition of A1.08.

## 1. Why the integrating frame needs to be formalized

The parent note A1.08 commits to substrate as source of truth and identifies the categories of coordination state that must live in the substrate together with categories that may legitimately live outside. The commitment is precise but compact; subsequent operational use surfaces three needs the integrating frame must address.

The first is the need to identify, with architectural precision, the categories of coordination question the substrate is authoritative *for*. Many enterprise architectures spread coordination state across workflow engines, decision-tracking applications, audit databases, identity providers, configuration repositories, conflict-tracking dashboards, and rule-management interfaces — and the question of which system is authoritative when systems disagree is often unanswered or answered ad hoc. Without an integrating-frame statement of what substrate authority covers, deployments cannot reliably establish substrate authority on the source-of-truth axis.

The second is the need to distinguish source-of-truth from mirror-of-truth. Two architectural patterns can carry identical content while reversing the direction of authority: in source-of-truth architectures, authoritative writes occur in substrate first; in mirror-of-truth architectures, authoritative writes occur in external systems first. The CKS commitment is to source-of-truth specifically; a substrate operating as mirror-of-truth fails the architectural commitment because its authority status is reversed regardless of content fidelity.

The third is the need to make explicit how source-of-truth connects to the just-completed path-retraceability decomposition. A1.07 / A2.35–A2.41 commit the substrate to retraceability and substrate-only paths; these commitments operationalize source-of-truth by giving the substrate the metadata infrastructure to support its authority. Retraceability without authority traces to non-authoritative state; authority without retraceability is undefended.

## 2. The five authoritative categories

The substrate is architecturally authoritative for five categories of coordination question. Each corresponds to an architectural commitment already named in the source paper or in A1.08; the present statement re-aggregates A1.08's commitments at the level of the question types the substrate must answer, with the provenance metadata supporting each category now treated under A1.07's six-field framework as decomposed in A2.35–A2.41.

**Category 1 — "What is the case."** The substrate is authoritative for the deployment's current coordination state. Queries about the present state of any coordination object — entity status, relationship between entities, current values of substrate-resident properties — are answered from substrate. External systems may carry derivative views (caches, projections, materialized views, search indexes); when substrate and external views disagree, the substrate prevails. A2.43 specializes.

**Category 2 — "What was decided."** The substrate is authoritative for the deployment's decision history. Queries about past decisions — what was decided, when, by whom, under what authority, with what rationale, against what antecedents — are answered from substrate, with the four accountability questions answerable per A2.36–A2.39 and the six provenance fields per A2.40 carrying the supporting metadata. A2.44 specializes.

**Category 3 — "What is in conflict."** The substrate is authoritative for the deployment's contradiction state per A1.03. Conflicts are preserved as first-class substrate objects with relationship metadata per A2.16; queries about what contradicts what, what each contradicting position says, and what relationship the substrate records between them are answered from substrate. A2.45 specializes.

**Category 4 — "What rules apply."** The substrate is authoritative for the deployment's orchestration rule set per A2.04. Rules are themselves substrate content, authored by humans at the rule-authoring moment; queries about which rules govern which content, what each rule specifies, when authored, under what authority, are answered from substrate. A2.46 specializes.

**Category 5 — "Who has what authority."** The substrate is authoritative for the deployment's governance structure per A1.01. The authority structure — which humans hold which inspect, modify, and override rights over which scopes — is itself substrate content. A2.47 specializes.

The five categories together define what the substrate is architecturally authoritative for; a substrate not authoritative for any one of them fails the architectural commitment. For each category, external systems (decision-logging applications, conflict-tracking dashboards, rule-management interfaces, identity providers, authorization services) may complement substrate as derivative views but cannot substitute for substrate authority. Section 6 elaborates the external-system relationship at the integrating level.

The relationship to A1.08's headline list is one of re-aggregation, not redefinition. A1.08 §2 names the categories at a different level of abstraction (what-was-decided / by-whom / under-what-authority / with-what-rationale / what-contradictions-remain), and §4 already includes orchestration rules and authority assignments under "state that must live in the substrate." The present aggregation promotes "current state," "rules," and "authority structure" to first-class categories and treats by-whom / authority / rationale as the metadata infrastructure supporting them — consistent with the parent commitment, specialized for the question-type framing the integrating frame requires.

## 3. The source-of-truth-vs-mirror-of-truth distinction

The CKS commitment is to source-of-truth specifically. The distinction matters because two architectural patterns can carry identical content while reversing the direction of authority.

In a **source-of-truth pattern** (the CKS commitment), the substrate is the architectural authority for the five categories. Authoritative writes occur in substrate first; derivative views (caches, projections, search indexes, dashboards, downstream materializations) are updated downstream from substrate. When substrate and external sources disagree on any of the five categories, the disagreement is resolved by the substrate — the external source is treated as stale, drifted, or incorrect, and the resolution path runs from substrate to external.

In a **mirror-of-truth pattern**, the substrate is a derivative view of state held authoritatively in external systems. Authoritative writes occur in external systems first; the substrate is updated downstream from them. When substrate and external sources disagree, the disagreement is resolved by the external system — the substrate is the stale view, and the resolution path runs from external to substrate.

The two patterns may coexist with comparable content fidelity at any given moment; what differs is the architectural commitment about authority. A substrate operating as mirror-of-truth fails the CKS commitment regardless of content match, because the property in question is the *direction* of authority, not the agreement of content. The standalone treatment is in A2.48; the integrating frame establishes the distinction here as the load-bearing differentiation that separates CKS substrates from architectures that look superficially similar.

## 4. How source-of-truth operationalizes through path retraceability

The substrate's authority for the five categories is operationally defended through path retraceability per A1.07 and the substrate-only-paths property per A2.41. Source-of-truth is the architectural commitment about authority; retraceability is the architectural commitment that operationally realizes it. The two interlock: authority without retraceability is undefended, and retraceability without authority traces to non-authoritative state. The interlock is specific for each authoritative category.

For **"what was decided,"** the substrate is authoritative because it carries the decision per A2.36, with the four accountability questions answerable per A2.36–A2.39 and the six provenance fields per A2.40 carrying the supporting metadata. Without that metadata the authority claim cannot be backed; with it, the substrate carries everything required to answer decision queries on its own terms.

For **"what is in conflict,"** the substrate is authoritative because it carries the contradicting content with relationship metadata per A2.16 — first-class addressable conflict objects with their own provenance, with conflict-handling rules and resolution decisions traceable per A2.15.

For **"what rules apply"** and **"who has what authority,"** the substrate is authoritative because rules per A2.04 and authority structure per A1.01 are themselves substrate content, with the rule-authoring moment's provenance and provenance for authority-structure changes carried per the six fields. Queries about which rule governs which scope, or which human holds which rights over which scope, answer from substrate without external reference.

For **"what is the case,"** the substrate is authoritative because it carries the current state with provenance for how that state was reached. Antecedent references per A2.40 chain back through prior substrate states to the originating writes, so current-state queries are not isolated facts but states with retraceable histories.

The substrate-only-paths property per A2.41 ensures the arrangement is operationally realizable. The substrate alone — without recourse to external logs, vendor metadata, conversational histories, or session traces — supports the authority claims source-of-truth makes. The claim and the metadata that backs it live in the same artifact and stay together as the substrate evolves.

## 5. What the commitment does NOT claim

The integrating-frame statement is precise about what substrate authority covers, and equally precise about what it does not.

(a) *It does not claim that the substrate carries all useful information about the deployment.* Operational telemetry, host-environment metrics, infrastructure state, deployment configuration, and business analytics may live in external systems without violating the commitment. The architectural commitment is to the five specific categories, not to substrate monopoly over all coordination-relevant information.

(b) *It does not claim that the substrate is metaphysically correct or immune to errors.* The substrate is architecturally authoritative — when it disagrees with external sources, the substrate prevails — but its content can be wrong, outdated, or in need of revision. Humans exercising the modify and override rights per A2.02 and A2.03 may revise substrate content based on knowledge from external sources. The substrate is the authority for the questions; its content is mutable by authorized humans.

(c) *It does not forbid external systems from carrying related content.* Deployments may have decision-logging applications, identity providers, conflict-tracking dashboards, and rule-management interfaces that touch the same categories. The architectural commitment is that these systems do not substitute for substrate authority; they may complement it as derivative views or convenience interfaces.

(d) *It does not specify external-system synchronization mechanics.* How external systems stay synchronized with substrate is a deployment concern; the commitment is to substrate being the source, not to a particular synchronization pattern.

(e) *It does not require the substrate to be the only authority in the deployment.* External systems may be authoritative for their own concerns. The CKS commitment scopes substrate authority to the five coordination categories, not to authority over all categories.

## 6. How source-of-truth interacts with external systems

The architectural commitment that the substrate prevails when it disagrees with external sources — scoped to the five authoritative categories — has three operational implications.

First, **external systems are derivative for the five categories.** Caches, projections, dashboards, search indexes, and downstream materialized views that carry copies of substrate content are derivative views; their content is correct insofar as it matches substrate. When they drift, they are updated from substrate, not the reverse.

Second, **external systems are authoritative for their own concerns.** Operational telemetry systems are authoritative for operational metrics; infrastructure providers for infrastructure state; analytics platforms for analytics computations. Substrate authority is scoped to the five categories, not extended to all systems.

Third, **conflicts between substrate authority and external-system authority are resolved category-by-category.** For the five coordination categories, substrate prevails. For external-system categories, external systems prevail. Deployments must clearly distinguish which categories belong to which system; mixing them produces ambiguity that tends to be resolved opportunistically — typically in favor of whichever system happens to be more operationally accessible at the moment of the query, which is exactly the failure mode source-of-truth is designed to prevent.

## 7. Operational test

A system implements substrate as source of truth at the integrating-frame level if and only if all of the following are true at all times during the substrate's existence.

1. For each of the five authoritative categories, the substrate carries the authoritative content (current coordination state, decisions, conflicts, rules, authority structure).

2. When the substrate and external sources disagree on any of the five categories, the substrate prevails — the deployment resolves disagreements in favor of substrate.

3. Authoritative writes to the five-category content occur in substrate first; derivative views are updated downstream.

4. The substrate's authority is operationally realizable through substrate-only paths per A2.41 — answering questions about the five categories does not require consulting external systems for the answers.

5. External systems carrying related content are clearly scoped to derivative-view or operational-concern roles, not to authoritative roles for the five categories.

A system that fails any of (1)–(5) does not implement substrate as source of truth at the integrating-frame level. Per-category and distinction-specific operational tests are specified in A2.43–A2.48 and provide finer-grained checks for each individual commitment.

## 8. Why naming the integrating frame as standalone matters

Implementations under pressure to integrate with established enterprise systems or leverage existing infrastructure consistently drift toward architectures where the substrate carries some content but external systems carry the authoritative answers. The drift is steady because external systems are operationally familiar, well-tooled, and organizationally established; substrate authority is the novel commitment, and novel commitments lose to familiar infrastructure under sustained operational pressure.

Implementations that drift away from source-of-truth produce systems where substrate authority is partial — authoritative for some categories but not others, for current state but not history, for readers but not writers, for cases of agreement but not disagreement. The downstream consequences are predictable: authority ambiguity (which system to consult for which question), retraceability failures (substrate-only paths breaks because the substrate is not authoritative for the question being traced), and human-governance failures (humans cannot exercise meaningful inspect, modify, and override rights per A1.01 when they cannot identify the authoritative source for the content they govern).

Naming the source-of-truth integrating frame as a standalone architectural commitment gives downstream implementers a precise specification of what substrate authority requires. The subsequent notes A2.43–A2.47 specialize each authoritative category, and A2.48 specializes the source-of-truth-vs-mirror-of-truth distinction; together with the integrating frame established here, they give the full operational decomposition of A1.08. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should treat substrate-as-source-of-truth as an integrating-frame commitment with five specified categories, a load-bearing source-of-truth-vs-mirror-of-truth distinction, and an operational dependency on path retraceability per A1.07. Subsequent work that uses "source of truth" without those three properties is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Substrate as Source of Truth: Full Operational Treatment of the Five Authoritative Categories in CKS.* May 4, 2026. ORCID: 0009-0004-8065-3235.
