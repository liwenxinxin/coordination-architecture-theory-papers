# AP-24: Automated Governance

**Series D — Phase D3 Anti-Pattern Formalization, Note D3.25 (#600)**
**Taxonomy: Category 6 — Governance Quality Failures (Closing Note)**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

AP-24 formalizes Automated Governance as a Full Aspect Integration (FAI) anti-pattern in which governance *authority* decisions — not merely governance labor — are delegated to automated systems. The anti-pattern is distinguished from the permitted practice of automated governance labor (executing pre-authorized governance decisions) by the location of the decision: compliant systems allow automated systems to execute what human governance has authorized; AP-24 allows automated systems to determine what governance should authorize. This distinction is the organizing spine of the note. AP-24 is the most severe anti-pattern in Category 6 (Governance Quality Failures): it does not weaken governance — it eliminates it. An FAI event affected by AP-24 is not a Paper 3-compliant governed event; it is an ungoverned inter-AI coordination event operating under a Paper 3 label, the inter-Self scope instantiation of the architecture's named foil. This note closes Category 6; Category 7 (Population-Scope Failures) follows.

---

## 1. Anti-Pattern Name and Category

**Anti-pattern:** AP-24 — Automated Governance

**Category:** 6 — Governance Quality Failures

**Position within category:** AP-21 through AP-24 together constitute Category 6's four governance quality failure anti-patterns. AP-24 is the fourth and final anti-pattern in the category, and the most severe: where AP-21 through AP-23 describe governance that is present but degraded in quality, AP-24 describes governance that has been structurally displaced by automation such that no human governance authority remains over the event's decisions.

---

## 2. Description

Automated Governance is a FAI event failure mode in which governance authority decisions are delegated to automated systems. The critical word is *authority*. Paper 3 commits, by inheritance from Paper 1 Claim 3, that humans hold governance authority over the coordination substrate at all times: the rights to inspect, modify, and override are available as architectural properties of the system's design, not merely as procedural options available in principle. An FAI event is Paper 3-compliant when those rights are structurally present and when the decisions exercising governance authority — what the configuration is, how conflicts are routed, what is absorbed, when the event dissolves — trace back to human governance authorization.

AP-24 arises when this chain breaks. The configuration governing the FAI event was not jointly authorized by human governance practitioners but was generated or selected by an optimization algorithm, a machine learning system, or an automated rule engine. Conflict routing decisions were made by an automated system applying learned or generated criteria rather than by orchestration rules authored under human governance authority. Absorption decisions were made by automated optimization rather than by directed selection events under human authorization. The automated systems may produce logs and records — the event may appear, from those records, to have been governed — but when those records are traced, they trace to automated system outputs rather than to human governance authorizations.

The distinction this anti-pattern turns on must be stated precisely: **automated execution of pre-authorized governance decisions is permitted governance labor; automated determination of what governance decisions should be is impermissible delegation of governance authority.** These two practices look similar at the surface — both involve automated systems performing actions during the FAI event — but they are architecturally distinct at the location of the decision.

A compliant system under the permitted practice: human governance practitioners author orchestration rules specifying how conflict class X is to be resolved; an automated system executes those rules when conflict class X arises during the FAI event. The decision — resolve conflict class X in manner Y — was made by humans when they authored the rules. The automation executes the decision.

An AP-24 system under the impermissible practice: an optimization algorithm or machine learning system determines how conflict class X should be resolved, generating or selecting the resolution criteria dynamically without those criteria having been authored under human governance authority. The decision — resolve conflict class X in manner Y — was made by the automated system. No human governance authorization underlies it.

The three rights (inspect, modify, override) are structurally available in AP-24 systems in the sense that no technical lock prevents them — humans can in principle read the logs, consult the automated system, and make post-hoc corrections. But the governance commitment is temporal: rights must be available *at any time*, not only in retrospect. Automated decisions happen faster than human governance can intervene in real time, and the decisions are made by systems whose determination criteria were not themselves human-authorized. The rights exist structurally but cannot be exercised at the decision point. That gap — available in principle, unrealizable in practice at decision time — is what makes AP-24 a structural governance failure rather than a procedural one.

---

## 3. Detection Criteria

AP-24 is detected by tracing governance decisions to their authorization source. Three indicators identify the anti-pattern:

**Decision records trace to automated system outputs rather than to human governance authorizations.** When the governance record of an FAI event is examined — what configuration was used, how conflicts were routed, what was absorbed — the record cites automated system outputs (algorithm selections, machine learning outputs, rule engine determinations) rather than human governance authorizations (jointly authored configuration documents, human-authorized orchestration rule sets, directed selection event records with human authorization). The records exist; they do not trace to human authority.

**Configuration, conflict routing, or absorption decisions were made by systems not themselves authored as governance-authorized orchestration.** The automated systems making governance decisions were not themselves instantiated through human-authorized orchestration rule authoring. An optimization algorithm that was deployed to configure FAI events, a machine learning system trained to route conflicts, or a rule engine that generates its own routing criteria all qualify. The test is whether the system making governance decisions was itself constituted through human governance authorization — not merely whether a human approved its deployment as a general capability.

**Human governance practitioners cannot identify when they exercised governance authority over specific FAI event decisions.** When practitioners are asked to identify the governance authorizations corresponding to specific decisions in the event — which configuration parameter was authorized when and by whom, which conflict routing rule was authored under whose authority — they cannot do so because the decisions were made by automated systems on their behalf, without their specific authorization. Practitioners may be able to identify that they authorized the automated systems generally; they cannot identify that they authorized the specific decisions those systems made.

---

## 4. Governance Commitment Violated

**Primary commitment violated:** Paper 1 Claim 3 — human-governed authority. The architecture commits that humans hold governance authority: the rights to inspect, modify, and override are available as structural properties of the system's design at all times. Automated Governance violates this commitment at every governance decision point in the event: configuration, conflict routing, absorption, and dissolution are each governed by automated system determinations rather than by human authority.

**Secondary commitment violated:** D2.43 — the FAI governance non-delegation principle. Governance authority cannot be delegated to non-governance actors, including automated systems. D2.43 establishes the authority-not-labor distinction as an operational principle: governance labor (executing pre-authorized decisions) is delegable; governance authority (determining what the decisions should be) is not. AP-24 violates D2.43 at every decision point where automated determination substitutes for human authorization.

**Tertiary commitment violated:** Paper 3's entire architectural commitment to human-governed inter-Self coordination. Paper 3's claims — shared substrate construction, Full Aspect Integration as the canonical operation, three-tier conflict handling, four-locus evolution feed, configuration as substrate content — are all premised on the event being human-governed in the sense Paper 1 establishes. When governance authority is automated, these claims do not apply: the shared substrate exists, the FAI operation executes, conflicts are handled, and evolution proceeds, but none of it occurs under the governance architecture Paper 3 commits to. The architecture's commitments are satisfied in form but not in substance.

---

## 5. Consequences

The consequences of AP-24 are more severe than those of any other Category 6 anti-pattern. AP-21 through AP-23 describe governance that is present but deficient — governance practitioners govern, but with incomplete records (AP-21), with improvised rather than authored criteria (AP-22), or with phantom rather than genuine joint authority (AP-23). AP-24 is categorically different: governance authority is absent from the event's decisions.

**The event is not a Paper 3-compliant FAI event.** An FAI event is Paper 3-compliant if and only if it proceeds under human governance authority across the participating Selves' governance perimeters. When governance decisions are made by automated systems, the event is an ungoverned inter-AI coordination event — automated systems coordinating with each other through a shared substrate without human governance authority over the decisions. It may be labeled an FAI event; architecturally it is the named foil Paper 3 commits to avoiding.

**The event is the inter-Self scope instantiation of the named foil.** Paper 3's named foil at §6's conflict-handling scope is opaque conflict resolution — coordination occurring without governable substrate, without first-class conflict state, without human authority over the resolution. AP-24 extends this foil to the entire governance dimension of the event: not merely conflict resolution but configuration, absorption, and dissolution are all determined by automated systems without human authority. The event is exactly the kind of ungoverned inter-AI coordination the architecture was designed to prevent, operating from within the architecture's own infrastructure.

**No governance decision in the event has human authorization.** Because configuration, conflict routing, absorption, and dissolution were all automated, no individual governance decision in the event traces to human authorization. This means there is no point in the event's governance record that represents an exercise of human authority. The three rights exist as structural properties of the substrate; they were never exercised. The event has governance infrastructure with no governance substance.

**Governance practitioners believe they are governing when they are not.** The most operationally dangerous consequence of AP-24 is epistemic: practitioners operating automated governance systems may sincerely believe they are governing FAI events. They authorized the automated systems' deployment; they receive the logs those systems produce; they may even review those logs. What they are doing is observing automated coordination and receiving reports about it. The governance authorization they believe they exercised — over the specific decisions of specific events — does not exist. The gap between perceived governance and actual governance is invisible until an audit traces decision records to their authorization source and finds none.

**Prior-art claims of human governance are voided for all affected events.** The Paper 3 defensive publication establishes, as one of its architectural commitments, that human governance holds structural authority across the inter-Self perimeter. AP-24 voids this claim for every event it affects: those events did not have human governance authority over their decisions, regardless of what the event labels say. Any prior-art claim that depends on human governance authority applying to those events is factually unsupported.

---

## 6. Intra-Self Analog

Paper 1's founding commitment establishes the hybrid architecture: the LLM operates as a substrate mediator under orchestration rules authored by humans. The LLM executes within the governance structure humans author; it does not author that governance structure. This commitment has a specific intra-Self failure mode: if the LLM authors its own orchestration rules — if the rules governing cell behavior are LLM-generated outputs committed as authoritative without human governance authorization — the hybrid commitment is violated. The LLM is no longer a mediator operating under human-governed rules; it is a governance actor determining its own operating constraints.

Automated Governance at inter-Self scope is the same violation at larger scope. When automated systems make FAI governance decisions — determining what the configuration is, how conflicts are routed, what is absorbed — they are making decisions that the architecture commits to humans. The scope is larger (inter-Self rather than intra-Self), the automated systems may be more capable, and the decisions are more complex; the structural violation is identical. In both cases, an automated system has assumed governance authority that the architecture places with humans.

The intra-Self analog also illuminates why sophistication does not resolve the violation. A highly capable LLM authoring its own orchestration rules is more dangerous as a governance failure than a less capable LLM doing so, because its rules will be more coherent and less obviously problematic. The same applies at inter-Self scope: a highly capable optimization algorithm generating FAI governance configurations is more dangerous than a naive one, because its configurations will be more defensible and harder to identify as ungoverned. The violation is structural, not capability-relative.

---

## 7. Resolution

The resolution to AP-24 is the consistent application of D2.43's authority-not-labor distinction across every governance decision in the FAI event. The distinction provides the operational framework: for every decision in the event, the question is whether the decision was made by human governance authority or by an automated system.

**Governance labor automation remains permitted.** Automated systems may execute governance decisions with full efficiency, speed, and sophistication, provided the decisions they execute were authorized by human governance. A rule engine that routes conflicts based on orchestration rules authored and approved by governance practitioners is executing permitted governance labor. The automated system's speed, scale, and capability are governance assets, not governance violations, as long as the rules it executes trace to human authorization.

**Pre-authorization is the governance-compliant path to efficiency.** Governance practitioners need not make real-time decisions during every FAI event to satisfy the governance commitment. They may author standing configurations applicable across classes of events. They may author orchestration rules covering the full range of conflict classes anticipated in a given coordination domain. They may authorize default absorption policies that apply unless overridden. Pre-authorization is governance authority exercised before the event; it satisfies the commitment because human governance determined what the decisions would be, before the automated systems executed them. The efficiency benefits of automation are available; the governance commitment is preserved.

**Configuration must trace to joint human authorization.** Every FAI event configuration must be traceable to a joint authorization by human governance practitioners of the participating Selves (D2.12). Configuration generated by optimization algorithms without that authorization is AP-24 regardless of its quality. The test is not whether the configuration is well-designed; it is whether humans authorized it.

**Conflict routing and resolution must trace to human-authored orchestration rules.** The orchestration rules governing conflict routing and resolution must be authored under human governance authority (D2.15). Rules generated by machine learning systems or optimization algorithms, without human governance authorization of the rules themselves, are AP-24. The test is whether a human governance practitioner can identify the specific orchestration rules that applied to each conflict class and confirm that those rules were authored under their governance authority.

**Absorption decisions must trace to directed selection events under human authorization (D2.11).** Absorption decisions made by automated optimization — selecting what to absorb based on learned or generated criteria without human authorization of those criteria — are AP-24. Directed selection events under human authorization, which may themselves be efficient and automated in their execution, satisfy the commitment.

The resolution in practice requires an audit of the event governance record sufficient to answer, for every governance decision: who authorized this decision, when, and under what governance authority? If that question cannot be answered — if the record traces to automated system outputs rather than to human governance authorizations — the event's governance record does not satisfy Paper 3's commitment, and the resolution requires establishing the authorization infrastructure that makes the question answerable for future events.

---

## Category 6 Closure

AP-21 through AP-24 together exhaust the four Governance Quality Failures in Phase D3's taxonomy:

- **AP-21** — Governance Record Incompleteness: governance decisions were made by humans but not recorded with sufficient traceability.
- **AP-22** — Ad Hoc Conflict Resolution: conflicts were resolved through improvised practitioner judgment rather than through authored orchestration rules.
- **AP-23** — Nominal Joint Authority: governance appeared joint across participating Selves but was in practice unilateral.
- **AP-24** — Automated Governance: governance authority decisions were made by automated systems rather than by human governance authorization.

The four anti-patterns form a progression: from governance that is present but under-documented (AP-21), to governance that is present but unstructured (AP-22), to governance that is structurally incomplete across the inter-Self perimeter (AP-23), to governance that is entirely displaced by automation (AP-24). AP-24 is the limiting case — not a degradation of governance quality but the elimination of governance authority.

Category 7, Population-Scope Failures, follows. Where Category 6 addresses failures in the governance quality of individual FAI events, Category 7 addresses failure modes that arise specifically at population scope, when accumulated FAI events across many Selves operate under conditions that undermine the population-scale collective evolution commitment Paper 3 Claim 6 establishes.

---

## Source Papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026c). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *AP-24: Automated Governance. Series D — Phase D3 Anti-Pattern Formalization, Note D3.25 (#600).* May 15, 2026. ORCID: 0009-0004-8065-3235.
