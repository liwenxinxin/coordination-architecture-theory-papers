# The Temporary and Persistent Shared Substrate Boundary

**Series note:** D6.10 — Phase D6 Boundary Case #660
**Type:** C (boundary definiteness)
**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3 commits the shared substrate to **temporary-by-design**: constructed for an interaction, existing for its duration, and dissolved at completion. A natural boundary question follows: when does a shared substrate cross from temporary (within FAI scope) to persistent (outside FAI scope)? This note establishes that the boundary criterion is **dissolution governance intent** — the presence or absence of governance's commitment to eventually dissolve the substrate and execute dissolution records — not duration. A shared substrate that has been running for five years under repeated governance amendments but with intact dissolution intent remains a FAI event; a shared substrate intended to run indefinitely from day one is outside FAI scope regardless of its age. The note applies this criterion to four temporal profiles, examines the governance-drift risk in extended-temporary arrangements, and establishes the standing-configuration model as the architecture's clean answer for organizations that want recurring inter-organizational coordination without permanent shared infrastructure.

---

## 1. The commitment at issue

Paper 3's Claim 1 commits the shared substrate to temporary construction: it is built for a bounded interaction — a Full Aspect Integration (FAI) event — and dissolves on that interaction's completion. The dissolution event is architecturally significant: it triggers the ingestion hand-off that feeds each participating organization's home substrate through the four-locus evolution-feed mechanism of Claim 4. The temporary-by-design property is not incidental; it is what makes the shared substrate a coordination medium rather than a coordination institution.

The boundary question this note addresses is a Type C (boundary definiteness) question: at what point does a shared substrate's temporal profile cross from temporary — satisfying the FAI commitment — into persistent — falling outside it?

---

## 2. The boundary criterion: dissolution governance intent

Duration is not the criterion. A shared substrate running for 90 days and one running for four years can both satisfy the temporary-by-design commitment, and a shared substrate that has existed for a single week can fail it. What determines compliance is whether governance has, and intends to execute, **dissolution governance**: the human-authorized records and processes that bring the shared substrate to a governed close.

A shared substrate is **temporary-by-design** in the FAI sense if and only if:

1. Governance holds dissolution intent — the shared substrate will eventually end, and governance expects to execute dissolution records at that end.
2. Dissolution governance is configured or configurable — the mechanism by which the shared substrate will be brought to a governed close is either already specified or is governed substrate content that governance can and will specify before the event closes.

A shared substrate is **persistent** — and therefore outside FAI scope — if governance intends for the substrate to operate indefinitely, with no dissolution event planned or contemplated.

Under this criterion, duration is *evidence* about governance intent, not the criterion itself. A very long-running shared substrate should prompt scrutiny of whether dissolution intent remains genuine. But the scrutiny is about intent, not about duration crossing some threshold.

---

## 3. Applying the criterion: four temporal profiles

Four shared substrates illustrate how the criterion resolves across the range of cases that arise in practice.

### 3.1 Clearly temporary

Two organizations establish a shared substrate for a 90-day coordination event. The configuration specifies a dissolution date, the dissolution governance process is documented, and at 90 days the substrate is dissolved with full dissolution records executed.

**Classification:** FAI event. Dissolution governance intent is present, specified, and executed. This is the paradigm case.

### 3.2 Extended temporary

A shared substrate starts as temporary — configured with a dissolution date and dissolution governance process. Before that date, governance amends the configuration to extend the event. This happens several times. The substrate has now been running for three years. Governance still intends to dissolve it; the dissolution governance process remains configured; the amendments are documented governance actions.

**Classification:** FAI event — an unusually long one, and one that warrants governance attention, but a FAI event. The temporary-by-design commitment is satisfied when dissolution governance intent is intact. The amendments are themselves governance records. The duration is long but does not by itself convert the event to persistent.

What warrants attention here is not the classification but the governance health of the arrangement. The extended-temporary profile is the grey zone examined in §4.

### 3.3 Indefinite standing

A shared substrate is established with no dissolution date. The configuration does not include a dissolution governance process. The organizations intend for the substrate to function as permanent inter-organizational coordination infrastructure — a standing coordination layer between them, maintained and operated indefinitely.

**Classification:** Not a FAI event. Governance has no dissolution intent. The temporary-by-design commitment is not satisfied. This arrangement may be a legitimate form of inter-organizational coordination, but it requires a different governance model than Paper 3's FAI architecture. Treating it as a FAI event would misapply the architecture's scope.

### 3.4 Standing configuration with per-event re-instantiation

Organizations that coordinate repeatedly establish a standing configuration: governance content that specifies how each coordination event will be run — which aspects are contributed, the conflict-handling configuration, the persistence policy at dissolution, the dissolution governance process. At the start of each coordination cycle, a new shared substrate is instantiated per the standing configuration. At the cycle's close, it dissolves with dissolution records. Between cycles, no shared substrate exists; the standing configuration is governance content within each organization's home governance, not a persistent shared substrate.

**Classification:** Each instantiation is a FAI event. The standing configuration is not a shared substrate — it is governance content that governs how shared substrates are constructed. The architecture between events is exactly what the FAI model requires: substrate-level state lives in the shared substrate during events, dissolves at dissolution, and feeds each home substrate through the evolution-feed mechanism. The standing configuration model is discussed further in §5.

---

## 4. The grey zone: extended temporary and governance drift

Scenario 3.2 — extended temporary — is the case that most frequently produces governance ambiguity, because the transition from "temporary extended by amendment" to "effectively permanent without a decision" can happen incrementally without any single governance action constituting a conversion.

The governance risk is **dissolution-intent drift**: governance originally intended to dissolve the substrate at some point, but over time the organizational expectation shifts toward indefinite operation without any explicit governance decision to that effect. At some point the substrate is functionally permanent even though no governance record says so. When this happens, the FAI architecture is being applied to an arrangement its scope does not cover, and the governance properties the architecture provides — dissolution-triggered evolution feed, bounded perimeter scope, configurable persistence — are being presumed for an infrastructure that has outgrown the design.

Three governance practices guard against dissolution-intent drift in extended-temporary arrangements.

**First, specify a maximum event duration at configuration, even if extendable.** A shared substrate configured with a maximum duration of eighteen months, extendable by amendment with documented governance review, is structured differently than one with no duration ceiling. The ceiling is not a hard constraint — amendment can extend it — but it creates a governance checkpoint at which dissolution intent must be reaffirmed. Without a ceiling, extension becomes the default path of least resistance, and the checkpoint disappears.

**Second, review dissolution intent explicitly at each amendment.** When governance amends the event configuration to extend the duration, that amendment should include an explicit review of dissolution intent: does governance still intend to dissolve this substrate at some point, and is the dissolution governance process still configured? This review is not a formality. It is the governance action that keeps extended-temporary within FAI scope. If the review reveals that governance no longer has genuine dissolution intent — that the organizations have come to rely on the substrate as permanent infrastructure — that is the moment to convert explicitly to a different governance model rather than to continue under the FAI architecture.

**Third, consider whether the standing configuration model better serves the governance intent.** When organizations have extended a shared substrate repeatedly because the coordination need recurs, the recurrence is information. The extended-temporary arrangement may be a poorly-structured approximation of what the standing configuration model provides cleanly: recurring FAI events under shared governance content, with no persistent shared substrate between events. If the coordination need is genuinely recurring rather than genuinely bounded, the standing configuration model is architecturally more appropriate than an indefinitely-extended single event.

---

## 5. The standing configuration model as the clean architecture for recurring coordination

Organizations that want recurring coordination without permanent shared infrastructure face an apparent dilemma: they want the governance properties the FAI architecture provides, but their coordination need is ongoing rather than episodic. The extended-temporary arrangement is one response to this dilemma, but it is structurally awkward — it strains the temporary-by-design commitment in service of a pattern the architecture was not designed to sustain.

The standing configuration model resolves the dilemma cleanly. The standing configuration is governance content — authored under each participating organization's home governance, joint-authorized across organizations, and owned by each home substrate. It specifies: which aspects each organization contributes to each event, the conflict-handling configuration, the persistence policy at dissolution, the dissolution governance process, the trigger conditions under which a new event is initiated, and any other configurable dimensions the organizations need. The standing configuration is not a shared substrate. It is governance content that governs how shared substrates are constructed when events begin.

When a coordination need arises, a shared substrate is instantiated per the standing configuration. It operates as a FAI event: temporary, bounded, governed, with dissolution configured. At the event's close, dissolution records are executed, the evolution-feed hand-off propagates to each home substrate, and the shared substrate dissolves. The standing configuration remains as governance content, ready to govern the next event.

The key architectural property is that **no persistent shared substrate exists between events**. What persists is governance content within each organization's home substrate — which is precisely the architecture's intended design for inter-organizational knowledge: that organizational learning from FAI events persists within each home substrate under each organization's governance, not in a standing shared layer outside either organization's governance perimeter.

This model also handles the prior-art significance noted in the boundary case framing. A long-running or recurring inter-organizational coordination arrangement implemented through the standing configuration model is unambiguously within FAI scope, because each event is temporary with dissolution governance. Any adversarial claim about a "long-running" or "ongoing" mechanism must address whether the mechanism has dissolution governance intent at each event — the standing configuration model satisfies this test by construction.

---

## 6. The boundary test

For any shared substrate, the test is:

> Does governance have dissolution governance intent — will the substrate eventually be dissolved with dissolution governance records? 

If **yes**: the shared substrate is within FAI scope regardless of how long it has been running or how many amendments have extended it. Governance should monitor dissolution-intent health in extended arrangements per §4.

If **no** (governance intends permanent operation with no dissolution event): the shared substrate is outside FAI scope. It may be a legitimate governance arrangement, but it requires a different model — one designed for permanent inter-organizational infrastructure rather than temporary coordination events.

The test is governance-state, not calendar-state. Answering it requires reading governance records, not measuring elapsed time.

---

## 7. Prior-art significance

Establishing dissolution governance intent — rather than duration — as the temporary/persistent boundary has significant prior-art implications for the FAI architecture.

It means that an extended FAI event lasting years is not outside the architecture's scope if its dissolution governance intent is intact. Prior-art breadth therefore covers the full range of long-running but genuinely temporary coordination arrangements, not only short-duration events. Any attempt to claim a "long-duration AI governance coordination mechanism" as novel must address whether it has dissolution governance intent — if it does, it falls within the FAI prior art established here.

It also cleanly excludes permanently-intended inter-organizational coordination infrastructure from the FAI prior art, without requiring a duration threshold that would be arbitrary and gameable. The exclusion is based on governance intent, not on elapsed time, which means it is robust to arrangements designed to appear temporary while functioning as permanent.

---

## 8. Summary

The temporary/persistent boundary for shared substrates under the FAI architecture is dissolution governance intent. Duration is irrelevant as a direct criterion; it is evidence to be examined when intent is unclear. Four temporal profiles illustrate the boundary: clearly temporary (paradigm FAI event), extended temporary (FAI event with governance-drift risk that requires active management), indefinite standing (outside FAI scope, different governance model required), and standing configuration with per-event re-instantiation (cleanly FAI, the recommended architecture for recurring coordination). The standing configuration model is the architecture's resolution for organizations that want recurring inter-organizational coordination without permanent shared infrastructure — each event is temporary with dissolution governance, and no shared substrate persists between events.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Temporary and Persistent Shared Substrate Boundary.* Derivation Note D6.10 (#660), CKS Series D. May 15, 2026. ORCID: 0009-0004-8065-3235.
