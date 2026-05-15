# FAI Governance for Knowledge Transfer Context

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

This note is D2.64 in the derivation note series for Paper 3. It derives from D2.62 (FAI participation modes) and D1.18 (DNA evolution feed locus). Its sole contribution is to specify the operational form of the knowledge transfer use case within the FAI governance architecture: how a structured, intentional transfer of governance patterns from one Self to another is configured, authorized, executed, and recorded under the FAI framework.

---

## Abstract

Standard FAI events are bidirectional: every participating Self both contributes aspects to the shared substrate and may absorb content from the shared substrate into its home evolution machinery. The knowledge transfer context is a structured variant with asymmetric participation intent — one Self (the contributor) explicitly intends to transfer governance patterns to another Self (the learner), while the learner intends to absorb rather than contribute. This note derives D2.64 as the operational decomposition for this use case. It specifies the knowledge transfer FAI configuration using the contribute-only and absorb-only participation modes from D2.62, explains why FAI is the appropriate mechanism for governance knowledge transfer (accountability as the architectural argument), states four governance requirements specific to the knowledge transfer context, establishes knowledge transfer as a structured onboarding mechanism for new Selves entering the FAI network, and names informal knowledge transfer as the anti-pattern the FAI architecture guards against. An operational test closes the note.

---

## 1. Why this decomposition is needed

FAI events accommodate a wide range of coordination purposes. The general case is symmetric participation: each Self contributes aspects the other can absorb, and both Selves emerge from the event with substrate content they did not have at the start. Much inter-organizational coordination fits this general case.

The knowledge transfer context differs from the general case in one structurally important way: the contribution intent is asymmetric from the start. One Self enters the event with the explicit purpose of making its governance patterns available to another. The other enters with the explicit purpose of absorbing those patterns, not of contributing its own. The participation intent is not bidirectional — it is directed, with a designated source and a designated recipient.

This asymmetry creates governance questions the general-case FAI architecture does not resolve by default. What participation configuration does the knowledge transfer context require? What authorizations apply to the contributing Self before the event begins? What governs the learner's selection among the contributed patterns? What record does the event produce, and what does that record contain? D2.64 addresses these questions as operational decompositions of the FAI framework, inheriting from D2.62's participation mode specifications and D1.18's DNA evolution feed locus.

---

## 2. The knowledge transfer FAI configuration

A knowledge transfer FAI event uses the asymmetric participation configuration that D2.62 establishes: the contributor Self operates in contribute-only participation mode, and the learner Self operates in absorb-only participation mode.

**The contributor Self's configuration.** In contribute-only mode, the contributor Self contributes aspects containing the governance patterns to be transferred and does not absorb from the shared substrate. The sharing scope (the D1.22 Dimension 1 configurable parameter) is set to include the aspects whose content the contributor intends to transfer — the orchestration rules, schemas, decision structures, and coordination patterns that constitute the substantive content of the transfer. The contribute-only configuration is the appropriate choice because it accurately represents the contributor's participation intent and bounds what the contributor exposes to the shared substrate to the specifically authorized transfer content.

**The learner Self's configuration.** In absorb-only mode, the learner Self does not contribute aspects and is positioned to absorb content from what the contributor has placed in the shared substrate. The learner's sharing scope is minimal or empty — the learner is present to receive, not to expose its own governance architecture to another organization's review. The absorb-only configuration protects the learner Self's home governance architecture from inadvertent exposure while keeping the learner positioned to access the contributed content.

**The cooperation variant.** The cooperation variant of FAI (D2.20) is the appropriate orchestration rule set for knowledge transfer events. The event is structured for cooperative benefit — the contributor is sharing governance patterns to help the learner, not competing for shared substrate territory. The cooperation variant's orchestration rules govern the event accordingly.

**The event as a whole.** The asymmetric configuration — contribute-only mode paired with absorb-only mode — is not a degenerate or incomplete FAI event. It is a fully valid instance of FAI operating under participation modes D2.62 establishes, with the cooperation variant, with sharing scopes appropriately set to the event's purpose. The FAI architecture supports it without modification.

---

## 3. Why FAI is the appropriate mechanism: accountability as the architectural argument

Organizations routinely transfer governance knowledge through informal channels: documentation, email, meetings, consultations, advisory relationships. Informal transfer can be effective and is often practical. The question is not whether informal transfer works in some deployments — it often does — but whether it provides the governance properties that transfer of governance patterns between CKS-governed organizations specifically requires.

The architectural argument for FAI as the appropriate mechanism rests on three accountability properties that informal transfer lacks.

**Governed contribution with provenance.** When the contributor Self places governance patterns in the shared substrate through a FAI event, those patterns enter as governed substrate content with full provenance — attributed to the contributing Self, timestamped, traceable through the substrate's provenance chain (D2.03). An organization receiving governance patterns through informal channels receives patterns without this provenance structure: the patterns may have arrived as email attachments, as documentation files, or as meeting notes. The receiving organization knows something about where the patterns came from, but that knowledge is not architectural — it is not encoded in the governance structure of the patterns themselves. If the patterns are later questioned, the provenance chain that would allow their authoring conditions to be reconstructed does not exist. FAI provides it.

**Authorized absorption under home governance.** The learner's absorption of contributed patterns from the shared substrate is a directed selection event (D2.11) under home governance authorization — explicitly authorized, versioned, and recorded as a governance decision. When governance patterns are transferred informally, absorption happens through implementation: someone at the receiving organization reads the patterns and implements them. Implementation is not the same as governed absorption. Governed absorption requires that the learner Self's authority structure explicitly authorize the decision to accept specific patterns into the home substrate, that the authorization is recorded, and that the absorbed patterns carry the record of their origin in the learner's own substrate. Informal implementation produces no such record.

**Complete event record.** The knowledge transfer FAI event produces a complete governance record (D2.18) covering what was contributed, which patterns were absorbed, which were declined, and under what governance authorizations. This record is available for review by the governance structures of both participating organizations. Informal transfer produces no equivalent record — what was shared, what was taken, and what was declined exists, if at all, only as conversational memory or as informal documentation whose governance status is undefined.

The three accountabilities are jointly necessary. Provenance without absorption authorization produces patterns whose origin is traceable but whose acceptance is ungoverned. Absorption authorization without provenance produces a governed selection among patterns whose authoring conditions are unknown. Either without a complete event record produces a governance situation that is not reviewable after the fact. FAI provides all three simultaneously. Informal transfer provides none of them architecturally.

---

## 4. Four governance requirements for knowledge transfer FAI

The knowledge transfer context carries four governance requirements beyond the general FAI configuration requirements.

**Requirement 1 — Explicit contribution intent in configuration.** The FAI configuration (D2.12) should explicitly state the knowledge transfer intent. This is governance transparency about what the event is for. The configuration is itself substrate content under recursive governance, and a reader of the configuration — whether a human reviewer, a governance auditor, or a later FAI participant reviewing the event record — should be able to see that the event was structured as a knowledge transfer rather than a general bidirectional exchange. Events whose configuration does not state their purpose are less governable than events that do.

**Requirement 2 — Contributor governance authorization.** The contributor Self must have explicit governance authorization to share the specific governance patterns being transferred before the event begins. The contributor's contribute-only configuration places governance patterns in the shared substrate as content representing the contributor's governance architecture. Sharing governance architecture is not the same as sharing other substrate content: it exposes the rules, decision structures, and orchestration logics by which the contributor operates. The contributor Self's authority structure must have explicitly authorized this exposure for the patterns in question. Governance authorization for sharing is a precondition of the event, not an assumed default.

**Requirement 3 — Learner absorption governance.** The learner's absorption from the shared substrate is a directed selection event (D2.11) under home governance authorization. The learner Self's governance decides what to absorb and what to decline. This requirement has two components. First, the absorption must be explicitly authorized — the learner's governance structure must affirmatively decide which contributed patterns to accept into the home substrate. Second, the contributor cannot compel absorption. The asymmetric participation configuration gives the contributor a share-only role and the learner a select-from-what-was-shared role; it does not give the contributor any authority over what the learner selects. Home governance sovereignty is preserved even in a knowledge transfer context where the entire purpose is for the learner to absorb from the contributor.

**Requirement 4 — Knowledge transfer record.** The event record must document the knowledge transfer as a distinguishable event type. In addition to the standard FAI record categories (D2.18), the knowledge transfer record should capture: which patterns were contributed with the explicit transfer intent noted, which were absorbed by the learner with the governance authorization for each absorbed pattern, and which were declined with any recorded reason for declination. This record is what makes the knowledge transfer reviewable — by both organizations' governance structures, by any external audit, and by participants in later FAI events who need to know whether the learner Self's governance architecture includes patterns that originated with another Self.

---

## 5. Knowledge transfer as onboarding mechanism

The knowledge transfer use case has a particularly important application for new Selves entering the FAI network.

A new Self — one whose governance architecture is recently established and whose home substrate has not yet accumulated the orchestration patterns, decision schemas, and coordination rules that operational maturity requires — faces a governance development challenge. The path to mature governance under the FAI architecture's general mechanisms is through the Self's own evolution: direct human authoring, action-feedback evolution producing governance refinements over time, and DNA evolution incorporating proven patterns through directed selection. This path works, but it takes time. A new Self operating in domains where established Selves have already developed mature governance patterns for the same coordination problems is developing from scratch what the network already knows how to do.

Knowledge transfer FAI events between established Selves and new Selves address this directly. An established Self with proven governance patterns for a given domain can configure a contribute-only event that makes those patterns available to a new Self configured in absorb-only mode. The new Self's governance then selects among the contributed patterns under the directed selection authorization that Requirement 3 specifies — absorbing what fits the new Self's governance context, declining what does not.

The result is a structured onboarding mechanism with full governance properties. The new Self does not begin its governance development without any foundation; it absorbs proven patterns whose origin, authoring conditions, and performance history are traceable through the provenance chain. The acceleration is itself governed: the absorption is authorized, the selection is recorded, and the patterns in the learner's home substrate carry their provenance back to the contributing Self. This is governed capability transfer rather than copying.

Two properties of this mechanism are architecturally important. First, the new Self's governance sovereignty remains intact — absorption is a directed selection under the new Self's own authority structure, not an imposition of the established Self's governance architecture. The new Self may absorb all, some, or none of what the established Self contributes. Second, the event record preserves the onboarding as a traceable governance event — later, if a question arises about where a specific governance pattern in the new Self's home substrate originated, the knowledge transfer event record answers it.

The knowledge transfer onboarding mechanism is available at any point in a Self's development, not only at initial entry into the FAI network. An established Self entering a new operational domain, or a Self whose governance has evolved away from patterns it once shared with another organization, may benefit from knowledge transfer events in either direction. The mechanism is not restricted to new Selves; it is merely most visible as an onboarding mechanism because the need is most acute at entry.

---

## 6. Anti-pattern: informal knowledge transfer

The knowledge transfer context makes the informal transfer anti-pattern especially visible, because the informal alternatives are not only common but often look adequate from the outside.

The informal knowledge transfer anti-pattern is the transfer of governance patterns between organizations through channels that bypass the FAI architecture: email correspondence, documentation exchange, consulting relationships, or direct human communication about how governance is done at the contributing organization. The patterns arrive at the receiving organization and are implemented — added to orchestration rules, incorporated into decision workflows, adapted for local use. This process can produce functioning governance that resembles the source, and it often does.

What it does not produce is governed transfer in the architectural sense. The three accountability properties named in §3 are absent:

- **No governed contribution.** The patterns were not placed in a shared substrate as governed content; they were transmitted as text or conversation. Their provenance as substrate content does not exist.
- **No absorption authorization.** The decision to implement the patterns was made by whoever implemented them — an individual developer, a team decision, an implicit default. It was not a directed selection event under home governance authorization, documented as such in the home substrate.
- **No event record.** The transfer has no governance record — no record of what was offered, what was taken, what was declined, or under what authorizations the decisions were made.

These absences are not minor procedural gaps. They are governance gaps. An organization that has informally absorbed another organization's governance patterns has no substrate record of having done so. Later governance review cannot determine which patterns originated externally, under what authority they were accepted, or what their authoring conditions were. The patterns are present in the implementation but absent from the governance record. In a governance architecture that depends on substrate-level accountability for coordination decisions, patterns that exist outside the substrate's record are patterns that are ungoverned regardless of how well they work.

The anti-pattern is not a failure of intent — organizations transfer governance knowledge informally because informal channels are available, fast, and familiar. The anti-pattern is a failure of architecture: using channels that do not provide the governance properties the architecture requires for accountable knowledge transfer.

---

## 7. Operational test

A knowledge transfer FAI event is correctly governed under D2.64 if and only if an independent observer can verify all of the following from the event configuration and event record:

1. The event configuration explicitly states the knowledge transfer intent, identifying the contributor Self as operating in contribute-only mode and the learner Self as operating in absorb-only mode, with the cooperation variant as the orchestration rule set.

2. The contributor Self has pre-event governance authorization — recorded as substrate content under the contributor's home governance — to share the specific patterns contributed in the event. An observer can trace each contributed pattern to the authorization under which it was cleared for sharing.

3. The learner Self's post-event home substrate records a directed selection event for each pattern absorbed, with the governance authorization for each selection identifiable. An observer can determine which patterns were absorbed, which were declined, and that each absorption was an authorized home governance decision, not an automatic or compelled acceptance.

4. The event record documents the knowledge transfer at the required level: what was contributed (with explicit knowledge transfer intent noted), what was absorbed (with per-pattern authorization), and what was declined (with any recorded reason).

5. The learner Self's governance authority remained intact throughout the event — the contributor did not exercise authority over the learner's absorption decisions, and the learner's governance structure made all selection determinations independently.

A knowledge transfer that fails any of (1)–(5) may have transferred governance patterns, and those patterns may be functional in the receiving organization's deployment. But the transfer is not a governed knowledge transfer in the FAI sense. It is an informal transfer with informal provenance, and it does not provide the accountability properties the FAI architecture exists to supply.

---

## 8. Conclusion

D2.64 derives the knowledge transfer context as an operational decomposition of the FAI participation mode architecture from D2.62. The knowledge transfer configuration — contribute-only mode for the contributor Self, absorb-only mode for the learner Self, cooperation variant, asymmetric sharing scopes — is a valid and fully governed FAI event form. The case for FAI as the appropriate mechanism for governance knowledge transfer rests on accountability: FAI provides governed contribution with provenance, authorized absorption under home governance, and a complete event record. Informal channels provide none of these architecturally.

Four governance requirements apply: explicit contribution intent in the configuration, contributor governance authorization for sharing, learner absorption governance that preserves home sovereignty, and a knowledge transfer record that documents contribution, absorption, and declination. The knowledge transfer mechanism has a specific and practically important application as a structured onboarding path for new Selves entering the FAI network — a governed alternative to governance development from scratch. The anti-pattern is informal transfer, which produces functioning governance patterns without the substrate-level accountability that makes those patterns governable over time.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI Governance for Knowledge Transfer Context.* May 15, 2026. ORCID: 0009-0004-8065-3235.
