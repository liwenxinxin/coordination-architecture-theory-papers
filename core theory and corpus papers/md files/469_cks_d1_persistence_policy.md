# Persistence Policy as Governed Substrate Content: What Remains After Shared-Substrate Dissolution Is Determined by an Authored Governance Configuration Ranging From Full Dissolution to Complete Audit Record, With Joint Authority Over the Policy

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

## Abstract

When the shared substrate constructed for an inter-Self coordination event (a Full Aspect Integration, or FAI, event) dissolves at event completion, what remains is not determined by infrastructure defaults, platform behavior, or any standing organizational policy. What remains is governed by a persistence policy — a governance-authored specification that is itself substrate content within the shared substrate, subject to the three governance rights (inspect, modify, override), and authorized jointly by all participating Selves' governance authorities. This note formalizes that sub-commitment. It distinguishes three persistence loci — the operational state of the shared substrate during an event, the durable record of the shared substrate after dissolution (which the persistence policy governs), and each Self's home-substrate evolution outputs (which home governance governs separately). It states the four properties of the persistence policy as governed substrate content: it is authored substrate content, it is subject to the three rights, it requires joint authority, and it is event-specific. It states the governance rationale for the range of admissible policies, from full dissolution to complete audit record. It identifies the inheritance from Papers 1 and 2. It names four failure modes the sub-commitment defends against. It closes with an operational test for verifying that a completed FAI event instantiates the commitment.

---

## 1. Why this sub-commitment needs separate statement

Paper 3's Claim 1 establishes the shared substrate as a temporary construction: built for an FAI event, operative during that event, and dissolved on the event's completion. The dissolution commitment is important in itself — the shared substrate is not a persistent integration layer but a bounded coordination medium. But dissolution raises an immediate and consequential question: what happens to the content the shared substrate held?

That question is not answered by the dissolution commitment alone. Three distinct answers could be architecturally consistent with dissolution: the infrastructure could determine what persists (a platform default); a standing organizational policy could determine what persists (uniform retention across all FAI events); or governance could determine what persists, per event, as part of the event's configuration. The architecture commits to the third. The sub-commitment being formalized here is the precise statement of that commitment: governance — not infrastructure, not standing policy — determines what persists, and the specification that governs persistence is itself substrate content authored and authorized by the participating Selves' governance authorities.

Without this sub-commitment stated separately, the dissolution commitment is ambiguous on a question that has significant practical consequences. Full deletion by default would eliminate audit capacity that governance might need. Full retention by default would impose storage and access obligations that governance might not want. Infrastructure-driven behavior either way substitutes the platform's judgment for governance authority over what belongs to governance: the decision about what the event's record is.

---

## 2. The sub-commitment stated precisely

In the CKS architecture, when a shared substrate dissolves at the completion of a Full Aspect Integration event, what remains is determined by a **persistence policy** that satisfies all of the following:

- The persistence policy is **authored substrate content**: it is written as part of the FAI event's configuration, lives in the shared substrate as governance-authored content, and is not a parameter, default, or behavior supplied by the underlying infrastructure.
- The persistence policy is **subject to the three governance rights**: participating governance authorities may inspect, modify, or override the policy at any time during the FAI event's operation, including after the event has begun and before dissolution occurs.
- The persistence policy is **jointly authorized**: all participating Selves' governance authorities must authorize what the policy specifies. What persists from a joint coordination event is a joint governance decision; no single participating Self's governance authority may unilaterally determine what persists from a shared-substrate event.
- The persistence policy is **event-specific**: it is configured per FAI event and is not a standing policy applied uniformly across all events. Different events with different coordination goals and different audit requirements may warrant different persistence policies, and governance determines the appropriate policy for each event.

---

## 3. Three persistence loci

The persistence policy's scope must be stated precisely because persistence is not uniform across the content associated with an FAI event. Paper 3 distinguishes three loci at which content persists, and the persistence policy governs only one of them.

**Locus 1 — Within the shared substrate during operation.** While the FAI event is active, the shared substrate holds all contributed aspect content, all conflicts surfaced by those contributions, and all provenance attached to that content. This is the live coordination medium — the substrate operating as intended. The persistence policy does not govern this locus; it governs what happens to this content after the event concludes, not what the substrate holds while it operates.

**Locus 2 — Within the shared substrate as durable record after dissolution.** This is the locus the persistence policy governs. When the shared substrate dissolves, what — if anything — remains as an inspectable record of the event is a governance decision. At one extreme, nothing is retained: the shared substrate fully dissolves and only Locus 3 content persists. At the other extreme, the full shared substrate is retained as a durable inter-organizational audit record, including all contributed aspects, all conflicts, and all provenance. Between these extremes, governance may specify partial retention — particular records, selected conflicts, or provenance of key governance decisions — according to the event's accountability requirements.

**Locus 3 — Within each participating Self's home substrate.** Each Self ingests evolution outputs from the FAI event into its own home substrate through Paper 2's evolution mechanisms. This content — DNA-layer updates, action-layer records, and preserved conflicts converted into home-substrate annotations — persists at the home perimeter under each Self's home governance. The persistence policy does not govern this locus. What each Self retains at home, at what provenance depth, through which evolution mechanisms, is governed by that Self's home governance authority independently of the shared-substrate persistence policy. The two governance domains are distinct: shared-substrate persistence is a joint governance decision over Locus 2; home-substrate retention is a separate home governance decision over Locus 3.

The precision of this three-locus structure matters. A system that conflates Locus 2 with Locus 3 — treating the persistence policy as governing what each Self retains in its home substrate — would extend the shared-substrate's joint governance authority into each Self's home perimeter. That extension is not warranted and not part of the architecture. Home governance governs home substrates; joint governance governs the shared substrate.

---

## 4. Properties of the persistence policy as governed substrate content

**Authored substrate content.** The persistence policy is not a configuration file supplied by the infrastructure or a vendor-defined default. It is authored as part of the FAI event's configuration substrate — the same substrate content that specifies which aspects each Self contributes, which conflict-handling rules apply, and what provenance depth travels with contributions. Claim 5 of Paper 3 establishes that all configurable dimensions of an FAI event are human-governed substrate content; the persistence policy is a specific instance of that commitment applied to the question of what persists after dissolution.

Because the persistence policy is substrate content, it is readable by any human with access to the shared substrate during the event's operation. There is no hidden infrastructure behavior that determines persistence; the specification is in the substrate and available for inspection.

**Three rights apply.** The three governance rights from Paper 1 — inspect, modify, override — apply to the persistence policy throughout the FAI event's operation. This has a practical implication: governance may modify the persistence policy after the event has begun, if circumstances during the event change the audit requirements. A coordination event that begins under conditions warranting minimal retention may encounter complications — a preserved conflict of organizational significance, a governance decision requiring traceability — that lead governance to modify the policy before dissolution. The architecture supports this. The persistence policy is not fixed at event configuration time; it remains subject to governance throughout.

**Joint authority.** An FAI event involves at minimum two Selves, each operating under its own home governance authority. The shared substrate spans both governance perimeters. What persists from the event is a question about the record of content that crossed both perimeters — contributions each Self made, conflicts that arose between them, provenance that records how the event proceeded. That record belongs to neither Self's home governance exclusively. Both governance authorities must authorize the persistence policy; neither may substitute its unilateral judgment for joint authorization. This is the inter-Self governance commitment: joint events produce joint records under joint authority.

**Event-specific.** The persistence policy is specified per FAI event, not imposed as a standing organizational policy across all events. An organization that conducts many FAI events — routine coordination on shared operational tasks, high-stakes joint governance decisions, exploratory exchanges for cross-organizational learning — faces different accountability requirements for different events. The architecture does not impose a uniform answer. Governance determines the appropriate policy for each event based on that event's coordination goals and the audit depth those goals require.

---

## 5. The range of admissible persistence policies

The architecture does not prescribe which persistence policy governance should adopt. It establishes the governance obligation (jointly authorized, event-specific, authored substrate content), the mechanism (the policy is substrate content subject to the three rights), and the range of admissible policies. Three positions in that range, each with its governance rationale:

**Minimal — full dissolution of the shared substrate.** Nothing is retained in the shared substrate after dissolution. Only Locus 3 content — each Self's home-substrate evolution outputs — persists. This policy is appropriate for routine coordination events where the coordination work is adequately represented by what each Self ingests into its home substrate, and where inter-organizational audit depth is not required. The coordination record exists at home perimeters; no separate shared record is necessary.

**Partial — governance-selected record retention.** Specific content from the shared substrate is retained after dissolution: a conflict registry, provenance of significant governance decisions, records of key coordination outcomes. This policy is appropriate for events where selective auditability is warranted — where some aspects of the event's record need to be available for later inspection by both parties, but where full retention is not required. Governance specifies precisely which content to retain and under what access permissions.

**Full — complete shared-substrate retention as durable audit record.** The entire shared substrate is retained after dissolution, including all contributed content, all conflicts, and all provenance. This policy is appropriate for high-stakes coordination events where full traceability across the shared perimeter is required — joint governance decisions with significant organizational consequences, events producing commitments that need to be referenced later, or events whose content is relevant to accountability obligations that extend beyond each Self's home perimeter. Full retention makes the shared substrate a durable inter-organizational record that either party's governance may inspect.

The three positions are not exhaustive; any governance-authorized specification of what content to retain, at what provenance depth, with what access permissions, is an admissible persistence policy. The range is defined by the extremes; the space between is governed by what each event's coordination goals and accountability requirements warrant.

---

## 6. Inheritance from Papers 1 and 2

**From Paper 1 — substrate as source of truth.** Paper 1's substrate-as-source-of-truth commitment establishes that the substrate is the authoritative record for coordination state: what was decided, by whom, under what authority, with what rationale, and what contradictions remain. The persistence policy governs what enters the inter-organizational authoritative record after dissolution. At full retention, the complete shared substrate is that record. At minimal retention, the record at the shared-substrate level is empty; the authoritative records reside in each Self's home substrate. In either case, the decision about what becomes part of the authoritative record is itself a governance act — consistent with Paper 1's commitment that governance, not infrastructure, determines what the substrate holds.

**From Paper 1 — path retraceability.** Paper 1's path-retraceability commitment specifies six provenance metadata fields that substrate content must carry: writer attribution, timestamp, antecedent reference, rule reference, rationale (where applicable), and relationship to contradicting content (where applicable). Whatever the persistence policy specifies as retained after dissolution must satisfy these provenance requirements. A partial-retention policy that retains records of key governance decisions without retaining the provenance fields those records require would produce a record that cannot be retraced — it would record outcomes without recording how they were reached. Path retraceability applies to what persists; the persistence policy must specify retention at the granularity provenance requirements demand.

**From Paper 2 — archival reactivatability.** Paper 2 establishes that governance may place entities in an archival state — suspended from operation, their content preserved as substrate content under governance authority, with the possibility of reactivation under new governance authorization. The persistence policy at FAI scope is the inter-Self analog: governance configures what the dissolved event's substrate contains and in what state it remains accessible. A fully retained shared substrate persisting after dissolution is, in Paper 2 terms, an archived coordination entity — content preserved under joint governance authority, available for inspection, not operationally active. The architectural commitment that archived state remains governed substrate content extends from Paper 2's entity lifecycle to Paper 3's FAI event lifecycle.

---

## 7. Failure modes the sub-commitment defends against

**Infrastructure-determined persistence.** The platform, hosting environment, or integration middleware determines what persists — retaining everything by its own default, or deleting everything by its own default — without reference to governance-authored policy. This substitutes infrastructure behavior for governance authority over a question that belongs to governance: what the inter-organizational record of a joint event is.

**Automatic full retention.** Everything the shared substrate held is always retained, without governance consideration of whether full retention is appropriate for the event's coordination goals and audit requirements. Full retention may be the right policy for some events; it is not the right default for all events. Automatic full retention imposes storage obligations, access permissions, and data governance burdens that governance has not authorized and may not want.

**Automatic full deletion.** Everything the shared substrate held is always deleted at dissolution, without governance consideration of audit requirements. Full deletion may be the right policy for routine coordination events; it is not the right default for all events. Automatic full deletion eliminates audit capacity that governance may need — for high-stakes decisions, for accountability obligations, for traceability requirements — without governance having made that determination.

**Uniform persistence policy.** A single persistence policy is applied uniformly across all FAI events — a standing policy that does not vary with event-specific coordination goals or audit requirements. Uniform policy replaces governance judgment about each event with a predetermined rule that cannot account for the variety of events a set of Selves may conduct. The architecture's event-specific commitment is precisely the refusal to allow a standing policy to substitute for governance.

---

## 8. Operational test

A completed FAI event instantiates the persistence policy sub-commitment if and only if all of the following are true:

1. **The persistence policy is locatable as authored substrate content.** An observer with access to the shared substrate (or its retained record, where Locus 2 retention applies) can find the persistence policy as an explicit authored specification within the configuration substrate — not inferred from infrastructure behavior, not reconstructed from what was retained, but present as governance-authored content.

2. **The persistence policy carries joint authorization.** The policy specification records authorization by all participating Selves' governance authorities. An observer can verify that no single Self's governance authority unilaterally determined the policy; joint authorization is itself substrate content carrying appropriate provenance.

3. **What actually persists matches the policy specification.** The content present in the shared substrate after dissolution (or the content absent, where full dissolution applies) corresponds to what the persistence policy specified. If the policy specified partial retention, only governance-selected records remain. If the policy specified full retention, the complete shared substrate is present. If the policy specified full dissolution, no content remains at Locus 2. Infrastructure behavior did not override the policy.

4. **The policy satisfies path-retraceability requirements for retained content.** Where the policy specifies that content is retained, the retained content carries the provenance metadata fields Paper 1's path-retraceability commitment requires — writer attribution, timestamp, antecedent reference, rule reference, and where applicable, rationale and relationship to contradicting content. Content retained without adequate provenance does not satisfy the sub-commitment even if its retention was governance-authorized.

A system that passes all four tests instantiates the persistence policy sub-commitment. A system that fails any one of them — because infrastructure determined what persists, because one Self's governance authorized the policy unilaterally, because what persists does not match the specification, or because retained content lacks the provenance its retraceability requires — does not instantiate the commitment regardless of how the policy was described or what governance intended.
