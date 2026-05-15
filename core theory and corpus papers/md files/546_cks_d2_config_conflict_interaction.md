# Configuration Governing Conflict Handling — Claims 5 and 3 Interaction

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** D2.51 — Inter-Claim Operational Synthesis, Note #546

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 3's Claim 3 establishes a three-tier inter-Self conflict-handling mechanism — preserve, resolve via orchestration, escalate to governance authority — operating over the shared substrate during Full Aspect Integration (FAI) events. Paper 3's Claim 5 establishes that every configurable dimension of the FAI architecture is authored substrate content governed under joint human authority. This note formalizes the operational intersection: Claim 3's three-tier mechanism is itself a configured system governed by Claim 5. Without its configuration, the three tiers are a structural framework without operational specification — they identify the tiers but cannot assign a conflict to any of them. Five configured objects constitute the operational content of the conflict-handling system: tier routing rules, resolve-tier orchestration rules, escalation routing destination, escalation response timeline, and conflict carry-through scope. Each of these is authored substrate content subject to governance amendment. Amendment effects are version-tracked: when governance modifies any configured object during an active FAI event, prior conflicts were handled under the preceding version and subsequent conflicts are handled under the amended version, yielding a full audit trace of how conflict handling governance evolved throughout the event. A system that implements three-tier conflict handling with routing determined by the system rather than by authored governance content violates the Claim 5 / Claim 3 conjunction and instantiates the hardcoded-conflict-routing anti-pattern.

---

## 1. Purpose of This Note

D2.51 is an inter-claim operational synthesis note. Its purpose is to formalize how Claim 5 governs Claim 3 in operational terms — not merely to note that such governance exists, but to enumerate precisely what it governs, what the consequences of that governance are, and what the architecture looks like when the governance is absent.

The prior D2 series has formalized each of Claims 1 through 5 individually and has developed sub-commitments for each claim. D2.51 takes a cross-claim direction: it asks what Claim 3's three-tier mechanism looks like when examined through the lens of Claim 5's configuration-as-substrate-content commitment. The answer is that Claim 3 describes a framework whose operational content is entirely supplied by Claim 5. They are not independent architectural contributions that happen to coexist in the same paper; they stand in a governed-system relationship, with Claim 5 as the governance layer and Claim 3 as the governed mechanism.

Formalizing this relationship matters for two reasons. First, it closes an interpretive gap: a reader who studies Claim 3 in isolation may treat the three tiers as fully specified, when in fact the operational question — which conflicts go where, resolved by what logic, escalated to whom, on what timeline, with what carry-through — is entirely left to Claim 5's configuration content. Second, it closes a prior-art gap: an implementer who introduces configurable conflict-routing as an addition to three-tier conflict handling is not introducing novelty — Paper 3 already commits to configured conflict handling as the only form of conflict handling its architecture admits.

---

## 2. The Inter-Claim Relationship: Claim 5 Over Claim 3

Claim 3's three-tier mechanism names three responses a conflict may receive during a FAI event. When a conflict is detected within the shared substrate, one of three fates is architecturally available: the conflict is preserved as first-class addressable substrate state and carried forward (preserve tier); the conflict is submitted to orchestration rules that resolve it under human-authored resolution logic (resolve tier); or the conflict is escalated to a governance authority capable of exercising direct judgment over it (escalate tier).

These three tiers specify the *structure* of conflict handling at inter-Self scope. They do not specify, and explicitly leave to governance, every operational parameter that makes the structure runnable. Which conflicts are routed to which tier — the routing rules — is not architecturally prescribed. What resolution logic the resolve tier applies — the resolution rules — is not architecturally prescribed. Which governance authority receives escalated conflicts, and on what timeline they must respond, are not architecturally prescribed. Which preserved conflicts carry through to home substrates as annotations is not architecturally prescribed. All of these operational parameters are Claim 5 territory: they are configurable dimensions of the FAI architecture, and Claim 5 commits that all configurable dimensions are authored substrate content governed under joint human authority.

The relationship is therefore structural: Claim 3 provides the framework; Claim 5 provides the operational content. The framework cannot operate without the content. The content has no structure to occupy without the framework. The Claim 5 / Claim 3 conjunction is not redundant — it is what makes the conflict-handling mechanism a governed system rather than a fixed mechanism.

---

## 3. Five Configured Objects

The operational content that Claim 5 supplies to Claim 3's framework consists of five configured objects. Each is authored substrate content, subject to the three governance rights (inspect, modify, override) held by the participating Selves' governance authorities under joint authority.

### 3.1 Configured Object 1 — Tier Routing Rules

The tier routing rules specify which conflict classes route to which tier. Some conflict classes may be assigned to the preserve tier because the participating Selves' governance has determined that those conflicts require judgment rather than automated resolution and are not urgent enough to escalate. Other classes may be assigned to the resolve tier because resolution logic can be fully specified in advance and the governance authorities are prepared to delegate resolution under authored rules. Others may be assigned to the escalate tier because the conflict class is sufficiently consequential that the governance authorities require direct involvement.

These routing assignments are governance decisions. No architectural principle prescribes which conflict classes belong where; that is precisely what governance deliberation is for. The routing rules are authored as substrate content within the shared substrate, subject to governance amendment, and — as §4 develops — subject to version tracking. An FAI event that begins with a given set of routing rules will route conflicts under those rules unless and until governance amends them.

The routing rules are also the most consequential of the five configured objects, because they determine which of the remaining four objects is brought to bear on any given conflict. A conflict that routing rules assign to the preserve tier never reaches the resolve-tier rules; a conflict that routing rules assign to the resolve tier never reaches the escalation destination. The routing rules are the gateway to the entire mechanism.

### 3.2 Configured Object 2 — Resolve-Tier Orchestration Rules

The resolve-tier orchestration rules specify the resolution logic that applies when a conflict is assigned to the resolve tier. These rules are authored substrate content — specifically, human-authored orchestration rules in the CKS sense — that determine what the resolution outcome is for each conflict class the routing rules direct to this tier. The set of conflict classes covered by the resolve-tier rules, and the resolution logic for each class, are governance decisions. Coverage gaps — conflict classes that the routing rules direct to the resolve tier but that the resolve-tier rules do not address — are governance oversights that leave the mechanism unable to process those conflicts. Coverage expansions — adding new conflict classes to the resolve-tier rules — are governance acts that extend the mechanism's automated resolution capacity.

The resolve-tier rules are the operational heart of automated conflict handling: they are what allows the mechanism to process conflicts without governance escalation, under authority delegated by governance through the act of authoring the rules.

### 3.3 Configured Object 3 — Escalation Routing Destination

When a conflict is assigned to the escalate tier by the routing rules, it must be directed to a governance authority capable of acting on it. Which governance authority — which role, group, or individual within the participating Selves' governance structures — receives escalated conflicts is authored substrate content within the FAI configuration. The escalation routing destination is not architecturally fixed; it reflects a governance decision about which authority has the standing and capacity to resolve the conflict class in question.

Multiple escalation destinations may be configured — different conflict classes may escalate to different authorities, or a primary authority may be named with a fallback. The configuration is the governance expression of which human authorities are empowered to act during the event; it is not a technical routing choice made by the system.

### 3.4 Configured Object 4 — Escalation Response Timeline

Once a conflict reaches the escalation destination, the governance authority must act on it within some period or the FAI event faces an unresolved escalated conflict whose presence may affect the event's progress. The response timeline for escalated conflicts — how long the governance authority has to respond, and what default action applies if that timeline is exceeded — is authored governance content within the FAI configuration. The architecture does not prescribe response times; governance does.

The default action on timeline exhaustion is itself a governance decision. Governance may configure the default to treat the conflict as preserved (carry it forward unresolved), to apply a specified fallback resolution, or to pause the event pending resolution. The configured default is the governance authority's advance instruction for the scenario in which direct judgment does not arrive within the configured window.

### 3.5 Configured Object 5 — Conflict Carry-Through Scope

The preserve tier, by design, does not resolve conflicts — it keeps them as first-class addressable substrate state within the shared substrate. As the FAI event dissolves and evolution feeds carry outputs to participating Selves' home substrates, the question arises: which preserved conflicts carry through as annotations in those evolution outputs, and how are they attributed? The carry-through scope — which preserved conflicts are included in evolution outputs, with what attribution metadata — is authored governance content.

The carry-through scope is the Claim 5 governance decision that determines how conflict history propagates from the shared substrate into participating Selves' home substrates after the event. A governance authority that configures broad carry-through ensures that home substrates inherit a rich conflict record; one that configures narrow carry-through limits what persists. Both are valid governance choices; neither is architecturally prescribed.

---

## 4. Amendment Effects on Conflict Handling

The five configured objects are not immutable for the duration of a FAI event. Claim 5's configuration-as-substrate-content commitment, under the governance amendment mechanism formalized in D2.38, allows governance to amend any configured object during an active event. Amendment effects on conflict handling are version-tracked.

When governance amends the tier routing rules, all conflicts detected after the amendment are routed under the new rules; conflicts detected before the amendment were routed under the prior version. The amendment record — which is itself authored substrate content — captures the governance act, the version superseded, and the effective time of the change. An observer examining the event record can therefore determine, for any specific conflict, which version of the routing rules governed its routing.

The same version-tracking principle applies to each of the five configured objects. If governance amends the resolve-tier orchestration rules, conflicts resolved before and after the amendment were resolved under different resolution logic, and the record shows this. If governance redirects the escalation routing destination mid-event — for example, because the originally configured authority is unavailable — subsequent escalations go to the new destination, and the record shows when the change took effect.

This version-tracking property is not incidental. It is the direct consequence of conflict handling being governed through authored substrate content rather than through hardcoded system logic. System logic has no version history in the governance sense; authored substrate content does. The version history is what enables a full audit of how conflict handling governance evolved during the event — not merely that conflicts were handled, but under what governance at each moment.

---

## 5. Configuration Completeness as Precondition

The three-tier mechanism cannot operate on a conflict whose class is not covered by the tier routing rules. If the routing rules do not assign a conflict class to any tier, the mechanism encounters that conflict without a routing assignment: no tier is triggered, and the conflict sits in the shared substrate as unaddressed state.

This observation carries a precondition: for a FAI event to handle conflicts adequately, the conflict handling configuration must be sufficiently complete at event start to cover the conflict classes the event is likely to produce. The minimum viable governance floor for a FAI event — the minimum content that must be present in the shared substrate before the event begins — includes at least basic conflict handling routing. An event that begins without any tier routing rules cannot route any conflict that arises; the three-tier mechanism is present as a structural commitment but absent as an operational capability.

Configuration completeness is therefore not a nice-to-have quality of the conflict handling configuration. It is the precondition for the mechanism having any operational effect. Governance authorities responsible for authoring the FAI configuration bear the responsibility for ensuring that the routing rules cover the conflict classes the event is expected to produce — recognizing that unanticipated conflict classes may arise and that governance amendment during the event is the mechanism for responding to gaps.

---

## 6. Prior-Art Significance

The Claim 5 / Claim 3 intersection established in this note forecloses a specific adversarial move: the claim that adding configurability to a three-tier conflict-handling mechanism is a novel architectural contribution.

That move would proceed as follows: an implementer independently designs a three-tier conflict-handling mechanism (preserve, resolve, escalate) and treats the tier routing rules as hardcoded system logic. Later, the implementer modifies the architecture to make tier routing configurable and seeks to claim this modification as a novel invention — configurable conflict routing over a three-tier mechanism.

Paper 3's prior art, as formalized in this note, defeats the novelty claim. Claim 5's configuration-as-substrate-content commitment applies to all configurable dimensions of the FAI architecture, and Claim 3's tier routing rules are explicitly a configurable dimension — one of five configured objects that constitute the operational content of the mechanism. Paper 3 does not treat configurable conflict routing as an optional enhancement to a fixed mechanism; it treats it as the only form the mechanism takes. A fixed-routing variant of the three-tier mechanism would violate Claim 5 for the conflict-routing dimension. Configured conflict routing is thus not an added feature; it is the default form.

This prior-art significance compounds across all five configured objects. Configurable escalation destinations, configurable response timelines, and configurable carry-through scope are all already in Paper 3's prior-art chain as consequences of Claim 5 applied to Claim 3. No subsequent claim of novelty for making any of these dimensions configurable is tenable against this prior art.

---

## 7. Anti-Pattern: Hardcoded Conflict Routing

The anti-pattern this note formalizes is **hardcoded conflict routing**: a design in which the tier routing rules — which conflict classes route to which tier — are determined by the system rather than by authored governance content within the shared substrate.

A system that instantiates this anti-pattern may still implement the three-tier structure in a recognizable form: conflicts may still be preserved, resolved, or escalated. What is absent is the governance layer that makes routing a governable decision. Because the routing rules are not authored substrate content, they cannot be inspected under governance's inspect right, amended under governance's modify right, or overridden under governance's override right without a system change. The routing behavior is outside governance reach.

This violates the Claim 5 commitment for the tier routing dimension and produces a conflict handling mechanism that is structurally similar to Paper 3's but architecturally distinct from it: it is a fixed mechanism dressed in three-tier structure, not a governed system whose three-tier structure is operationally specified through authored governance content.

Derivatives and partial implementations of the hardcoded-routing anti-pattern include: routing rules authored outside the shared substrate (in a separate configuration layer not subject to the six Paper 1 commitments); routing rules authored within the substrate but not subject to governance amendment; and routing rules that are nominally editable but require system redeployment to take effect. Each of these variants fails the configuration-as-substrate-content commitment for the routing dimension, because substrate content is subject to governance rights at all times without requiring infrastructure changes.

---

## 8. Operational Test

A FAI event implementation satisfies the Claim 5 / Claim 3 conjunction if and only if all of the following are true:

1. **Tier routing rules are present as authored substrate content.** The shared substrate contains explicit routing rules that assign conflict classes to tiers. The rules can be read by any governance authority with appropriate access without runtime intermediation.

2. **Resolve-tier orchestration rules are present as authored substrate content.** For every conflict class the routing rules direct to the resolve tier, a resolve-tier rule exists as authored substrate content specifying the resolution logic.

3. **Escalation routing destination is present as authored substrate content.** The FAI configuration contains explicit specification of which governance authority receives escalated conflicts.

4. **Escalation response timeline is present as authored substrate content.** The FAI configuration contains explicit specification of the response timeline for escalated conflicts and the default action on timeline exhaustion.

5. **Conflict carry-through scope is present as authored substrate content.** The FAI configuration contains explicit specification of which preserved conflicts carry through to home substrates in evolution outputs and how they are attributed.

6. **All five configured objects are subject to governance amendment.** Governance authorities holding joint authority over the FAI configuration can inspect, modify, and override any of the five configured objects during the event, with amendments taking effect as substrate content and recorded with version information.

7. **Conflict routing is version-traceable.** For any conflict detected during the event, an observer can determine which version of the tier routing rules governed its routing at the time of detection, by examining the amendment record in the shared substrate.

A FAI event implementation that fails any of (1)–(5) has an incomplete conflict handling configuration: some aspect of the three-tier mechanism's operational content is absent, leaving one or more conflict classes unaddressed. An implementation that fails (6) or (7) has conflict handling configuration that is present but not governed in the Claim 5 sense: the configuration cannot be amended by governance or its version history cannot be traced.

---

## 9. Conclusion

Claim 3's three-tier inter-Self conflict-handling mechanism and Claim 5's configuration-as-substrate-content commitment stand in a governed-system relationship: Claim 3 provides the structural framework; Claim 5 provides the operational content through five configured objects. The framework cannot fire without the content; the content has no structure to inhabit without the framework.

The five configured objects — tier routing rules, resolve-tier orchestration rules, escalation routing destination, escalation response timeline, and conflict carry-through scope — are authored substrate content subject to governance amendment and version tracking. When governance amends any configured object during an active FAI event, the amendment record enables full reconstruction of which governance rules governed which conflicts at each moment of the event. This version-tracking property is the direct consequence of conflict handling being governed through authored substrate content rather than fixed system logic.

A system in which tier routing is determined by the system rather than by authored governance content instantiates the hardcoded-conflict-routing anti-pattern and is architecturally outside the Claim 5 / Claim 3 conjunction regardless of whether it implements the three-tier structure in other respects.

Subsequent work that implements inter-Self conflict handling under a three-tier structure should treat all five configured objects as required authored substrate content under joint governance authority. The absence of any configured object is not an architectural simplification; it is a gap in the operational specification of the mechanism that leaves the corresponding conflict class unaddressed by governance.

---

## Source Papers

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Configuration Governing Conflict Handling — Claims 5 and 3 Interaction.* May 15, 2026. ORCID: 0009-0004-8065-3235. CKS Derivation Notes Series D2, Note #546.
