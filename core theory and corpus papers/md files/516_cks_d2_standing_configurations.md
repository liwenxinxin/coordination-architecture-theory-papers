# Standing FAI Configurations for Recurring Partners

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

When the same Selves participate in Full Aspect Integration (FAI) events repeatedly, requiring full per-event configuration authoring and joint authorization at every occurrence imposes governance overhead that grows with event frequency. This note formalizes the standing FAI configuration: a governance-authorized configuration substrate established between events that pre-specifies the six FAI configuration dimensions for a defined class of recurring events between the same participating Selves. A standing configuration reduces per-event overhead without compromising governance integrity because the standing configuration is itself authored governance content — jointly authorized, versioned, and maintained through a defined amendment protocol. Every event that runs under a standing configuration runs under pre-established governance, not under governance absence. The note derives this architecture from D1.22 (the commitment that all six FAI dimensions are substrate content) and D0.05 (the commitment that FAI configuration is substrate content), states five governance requirements a valid standing configuration must satisfy, explains the governance efficiency versus governance integrity tradeoff, introduces the review cadence requirement that keeps standing configurations living governance content rather than historical artifacts, and states the anti-pattern of the forgotten standing configuration. An operational test closes the note.

---

## 1. Derivation context

D1.22 established that all six dimensions of FAI configuration — aspect scope, provenance carry-over depth at the perimeter, provenance preservation on internalization, persistence policy, conflict-handling configuration, and authority-articulation mechanics — are substrate content. D0.05 established that FAI configuration as such is substrate content under joint authority of the participating Selves' governance structures. D2.12 formalized the per-event authoring protocol: for any specific FAI event, the configuration is authored within the originating Self's governance, approved by the other participating Self's governance, and becomes part of the event's substrate record.

The per-event authoring protocol is complete and correct for events between Selves that interact infrequently or whose interactions are sufficiently varied that each event warrants distinct configuration decisions. It is not the only valid mode. When the same Selves interact repeatedly — under stable governance architectures, in stable domains, for a stable class of cooperation or competition events — requiring full per-event authoring and joint authorization at every occurrence is governance overhead that produces no proportional governance benefit. The governance decisions are the same; their repeated re-enactment adds cost without adding authority.

D2.21 addresses this case. It formalizes the standing FAI configuration as an operational decomposition of D1.22 and D0.05 for recurring-partner interactions: a mechanism that amortizes governance work across an event class rather than repeating it per event, while preserving the governance properties the underlying commitments require.

---

## 2. The standing FAI configuration defined

A **standing FAI configuration** is governance-authorized configuration substrate content established between events, prior to any specific event it governs, that pre-specifies the six FAI configuration dimensions for a defined class of FAI events between specified participating Selves.

Three structural features define what makes a standing configuration distinct from a per-event configuration:

**Scope extends across an event class.** A per-event configuration governs exactly one event. A standing configuration governs all events in the class it defines — subject to per-event override (§5). The class is defined by which Selves participate, what event types fall within scope (cooperation, competition, specific domains), and any categorical exclusions (aspects or domains that are never contributed under this standing arrangement regardless of event type).

**Establishment is between events.** A standing configuration is authored and jointly authorized outside the operational context of any specific event. This is not incidental; it is the architectural feature that produces the efficiency gain. Because the governance work is done when no event is pending, the Selves' governance structures can deliberate without the time pressure of an active event waiting for configuration, and the resulting configuration can be more carefully calibrated than per-event configurations produced under time pressure.

**It is substrate content by the same requirements as any FAI configuration.** A standing configuration is not a softer, lighter, or more informal governance artifact than a per-event configuration. It satisfies the same requirements. It is authored as substrate content in each participating Self's home governance and/or in a jointly-governed configuration registry. It is jointly authorized. It is versioned. It is subject to the same governance rights — inspect, modify, override — that apply to any substrate content under the CKS architecture.

The characterization that matters most: a standing configuration is not a shortcut past governance. It is governance done in advance. The governance work happened; it happened at configuration authoring and joint authorization time. Every event that subsequently runs under the standing configuration runs under that pre-established governance.

---

## 3. Five governance requirements

A standing FAI configuration is valid only if it satisfies all five of the following requirements.

### Requirement 1 — Established as substrate content

The standing configuration must be authored and maintained as substrate content in each participating Self's home governance, in a jointly-governed configuration registry, or in both. It must satisfy the same structural requirements as a per-event configuration under D2.12: it must specify all six FAI configuration dimensions, or explicitly defer specific dimensions to per-event decision. Unstated dimensions are not assumed to carry over from prior events; absence of specification is a gap, not a default.

The substrate-content requirement is not merely formal. It is what makes the standing configuration inspectable, modifiable, and auditable under the governance rights the CKS architecture preserves. A standing configuration that exists only as informal mutual understanding between governance representatives, undocumented in substrate, is not a standing configuration in the sense formalized here. It is a handshake arrangement, and handshake arrangements do not carry the governance properties this architecture requires.

### Requirement 2 — Joint authorization

A standing configuration must be jointly authorized by all participating Selves' governance structures before it takes effect. Joint authorization is not satisfied by one Self's unilateral declaration that a standing configuration applies; it requires explicit approval from every Self the standing configuration binds. The joint authorization record is itself governance content — it establishes when the standing configuration came into effect and under what governance acts.

This requirement holds regardless of the informality or closeness of the relationship between the participating Selves' governance structures. Even Selves whose governance structures share leadership or organizational context must separately authorize a standing configuration as governance content. Informality of relationship does not substitute for formality of authorization.

### Requirement 3 — Scope definition

The standing configuration must define the class of events it governs with sufficient precision that, for any candidate event, a governance reader can determine whether the standing configuration applies or whether per-event configuration is required. The scope definition covers three dimensions:

*Participating Selves.* The standing configuration names the Selves it binds. A standing configuration between Self A and Self B does not automatically extend to Self C, even if Self C's governance is affiliated with A's or B's.

*Event type coverage.* The standing configuration specifies which event types fall within scope. Event types may be characterized by cooperation versus competition axis, by domain, by aspect class contributed, or by any combination. Event types outside the defined scope require per-event configuration.

*Categorical exclusions.* The standing configuration may specify aspects, domains, or event types that are explicitly excluded from standing-configuration coverage — aspects whose contribution always requires per-event deliberation regardless of how well the standing configuration covers adjacent territory. Categorical exclusions are not default denials; they are explicit governance decisions that certain territory always warrants fresh deliberation.

### Requirement 4 — Amendment protocol

A standing configuration is not frozen at establishment. Governance evolves; the participating Selves' architectures evolve; the appropriateness of any standing configuration's specified dimensions may change. The standing configuration must include, as part of its substrate content, an amendment protocol specifying how amendments are proposed, approved, and recorded.

Amendment by any participating Self proceeds through the joint modify right. Any participating Self's governance may propose an amendment; the amendment takes effect only upon joint authorization. The amendment record becomes part of the standing configuration's version history, and the version history is substrate content.

The amendment protocol requirement has a practical implication: a standing configuration without an amendment protocol is incomplete. The amendment protocol is not ancillary governance machinery; it is part of the standing configuration itself.

### Requirement 5 — Per-event override

Even with a valid standing configuration in effect, participating governance retains the authority to override specific dimensions for a specific event through per-event configuration decisions. Per-event override is not a sign of standing configuration failure; it is a deliberate design feature that preserves governance precision when event-specific circumstances require it.

Per-event overrides are recorded in the event's configuration record, adjacent to the reference to the standing configuration under which the event otherwise runs. The override record specifies which dimensions were overridden and what values replaced the standing configuration's specifications for this event. The standing configuration itself is not amended by a per-event override; the override applies only to the event for which it was issued.

The standing configuration is the default. It is not the mandate.

---

## 4. Governance efficiency versus governance integrity

The standing configuration offers a genuine efficiency gain: governance establishes the FAI configuration once, or infrequently at amendment junctures, rather than at every event occurrence. For Selves that interact frequently — hundreds or thousands of events per year, in stable domains under stable governance architectures — the difference between per-event authoring and standing configuration governance is substantial. Per-event authoring overhead scales with event frequency; standing configuration overhead scales with amendment frequency, which is bounded by governance architecture change velocity rather than event frequency.

The efficiency gain is real. It must not be misread as a governance relaxation.

The governance integrity of the standing-configuration architecture holds on three grounds. First, the standing configuration is authored governance content satisfying the same structural requirements as per-event configuration. Second, every event running under a standing configuration can be traced to the governing configuration through the standing configuration reference in the event's record, and from there to the joint authorization that established the standing configuration and the amendment history that maintained it. The governance path is complete; it is longer than a per-event path only in that it runs through the standing configuration's establishment record rather than through a per-event authoring record. Third, per-event override preserves the ability of governance to act with full precision when any specific event warrants deviation from the standing configuration's terms. Governance authority is never yielded; it is selectively pre-exercised.

The framing that clarifies the tradeoff: standing configurations amortize governance work. They do not eliminate it. The governance investment is made at establishment and at each amendment. The return on that investment is that subsequent events run under pre-established governance without requiring fresh governance labor per event. This is the same logic that applies to any governance instrument that establishes rules in advance of the cases those rules will govern — the investment is front-loaded, the benefit is amortized.

---

## 5. Review cadence requirement

A standing configuration that was carefully established and jointly authorized at one point in time may become progressively misaligned with the participating Selves' current governance architectures. Governance architectures evolve: aspect structures change, conflict-handling configurations are refined, authority-articulation mechanics are revised. A standing configuration established when Self A used one conflict-handling tier structure and Self B had one aspect architecture may specify wrong sharing scopes or obsolete conflict-handling rules when those architectures change without corresponding amendment to the standing configuration.

The review cadence requirement addresses this. As part of the standing configuration's substrate content, the participating Selves' governance must specify a cadence at which the standing configuration will be reviewed for continued accuracy. The review cadence is a governance commitment: at the scheduled interval, the participating Selves' governance will assess whether the standing configuration remains an accurate specification of their intended FAI interaction terms.

Review does not require amendment. A standing configuration reviewed and found current is reaffirmed by the review record; the review record becomes substrate content. A standing configuration reviewed and found to require amendment proceeds through Requirement 4's amendment protocol.

The review cadence is part of governance completeness for a standing configuration. A standing configuration without a review cadence is — from the moment of its establishment — on a trajectory toward the anti-pattern described in §6. Governance established a configuration; governance did not establish a plan for maintaining it. The absence of a review cadence is an incompleteness in the standing configuration as authored.

---

## 6. Anti-pattern: the forgotten standing configuration

A standing configuration that was established, jointly authorized, and then never reviewed or amended occupies a distinctive failure mode. It remains in the governance record as formally valid substrate content. Events continue to run under it. But it no longer accurately reflects the participating Selves' current governance intent.

This is the **forgotten standing configuration** anti-pattern: standing configuration substrate content that has drifted from the current governance reality it purports to represent. The danger is not that governance was bypassed — the standing configuration was legitimately established. The danger is that governance is being cited for parameters no longer representing what governance would currently authorize. FAI events running under a forgotten standing configuration are running under historical governance, not current governance, while the event record presents them as running under active governance.

The forgotten standing configuration is not an unusual failure mode. It is the natural trajectory of any standing configuration without an enforced review cadence, in a governance environment where the participating Selves' architectures evolve at any rate above zero.

Three conditions produce it: establishment without a review cadence, governance architecture change without triggering configuration amendment, and event volume sufficient that per-event review of whether the standing configuration remains accurate never occurs. All three conditions are common in active deployments.

The remedy is prevention: authoring the review cadence as part of the standing configuration's initial substrate content, so that the obligation to maintain the configuration's accuracy is built into the governance record from the beginning.

---

## 7. Operational test

For a FAI event that runs under a standing configuration, the following questions constitute the operational test of whether the standing configuration architecture has been correctly instantiated:

**1. Is the standing configuration findable as substrate content?** Can an observer locate the standing configuration as authored substrate content in the participating Selves' home governance or in a jointly-governed configuration registry? If the standing configuration exists only as an informal mutual understanding, the test fails.

**2. Is the joint authorization record present?** Does the standing configuration's substrate record include a joint authorization by all participating Selves' governance that the standing configuration applies to the defined event class? If only one Self's authorization is recorded, the test fails.

**3. Is the standing configuration current?** Does the amendment history show that the standing configuration has been reviewed and either reaffirmed or amended since the last material change in either participating Self's governance architecture? If the standing configuration predates significant governance architecture changes without corresponding amendment or reaffirmation, the test fails.

**4. Does this event fall within the standing configuration's defined scope?** Is the event in the class the standing configuration defines, or does it fall outside the defined scope and therefore require per-event configuration? If the event is outside scope and no per-event configuration was authored, the test fails.

**5. Are per-event overrides recorded?** If any dimension was overridden for this specific event, is the override documented in the event's configuration record, identifying the dimension, the replacement value, and the governance act that issued the override? If per-event overrides were applied without documentation, the test fails.

A standing FAI configuration architecture is correctly instantiated for a given event only if all five questions receive affirmative answers.

---

## 8. Conclusion

The standing FAI configuration is an operational decomposition of the commitment that FAI configuration is substrate content (D0.05) and the commitment that all six FAI configuration dimensions are substrate content (D1.22), applied to the recurring-partner case. It reduces per-event governance overhead by amortizing governance work across an event class. It preserves governance integrity because the standing configuration is itself authored governance content — jointly authorized, versioned, subject to amendment protocol, and continuously maintained through a review cadence. Events running under a standing configuration run under pre-established governance; the efficiency gain is in amortization, not circumvention.

Per-event override preserves governance precision: the standing configuration is the default, not the mandate, and any dimension can be overridden for any specific event, with the override recorded. The review cadence requirement prevents the standing configuration from becoming a frozen historical artifact; by requiring periodic reaffirmation or amendment, it keeps the standing configuration living governance content. The forgotten standing configuration anti-pattern names the failure trajectory when this discipline is absent.

Downstream work in the Series D derivation chain may elaborate amendment protocol mechanics, address standing configurations in multi-Self (more than two) interaction architectures, or specify how standing configurations interact with the six FAI dimensions at the level of specific dimension classes.

---

## Source papers

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Standing FAI Configurations for Recurring Partners.* May 15, 2026. ORCID: 0009-0004-8065-3235.
