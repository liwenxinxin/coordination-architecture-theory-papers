# Cross-Level Access Governance: Decomposing B1.19 by Formalizing How Access Rules Are Authored, Authority Is Distributed, Access Events Are Recorded, and Unauthorized Access Is Handled

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Cross-level access in a CKS Self — the pattern by which Self-level entities govern aspects, aspects coordinate cells, and cells report upward through aspects to the Self — requires a complete governance framework to be architecturally defensible. This note formalizes CROSS-LEVEL ACCESS GOVERNANCE as that framework, decomposing B1.19 (cross-level access) by specifying four governance dimensions: access rule authoring per A2.04 (downward and upward access rules authored as substrate-resident authoritative content per A2.46); authority distribution per A2.47 Category 5 (who has cross-level access authority at each level, with access outside the specified distribution constituting an unauthorized governance violation); access event recording per A2.40 (all cross-level interactions recorded with full provenance, supporting A1.07 retraceability through inter-level history); and unauthorized access handling (violation per A1.01, events recorded, governance notified, patterns triggering investigation). The note articulates what makes cross-level access governance architecturally distinctive relative to implicit API-based component access in conventional multi-component AI architectures, develops the biological analog of signaling pathway regulation by receptor specificity as a conceptual scaffold, enumerates the inherited Paper 1 commitments that load-bear the framework, states operational implications for deployments, and names the limits of the governance commitment. B2.95 is the second of four notes decomposing B1.19, following B2.94 (cross-level access integrating frame) and preceding B2.96 (cross-level access patterns) and B2.97 (cross-level access verification).

---

## 1. Why cross-level access governance needs to be formalized as a standalone operational variant

B1.19 establishes cross-level access as an architectural property of the CKS Self: the three-level structure of cell, aspect, and Self requires that entities at different levels can interact in governed ways, and that these interactions are not left as implicit capability but are specified, authorized, and recorded. B2.94 provides the integrating frame — the structural account of what cross-level access is, how the three directions (downward governance, lateral coordination, upward reporting) are organized, and why cross-level access is first-class in the CKS pattern rather than an afterthought to the within-level architecture.

B2.95 takes up the governance question that B2.94 frames but does not fully resolve: given that cross-level access occurs, how is it governed? The question is not merely procedural. In a CKS Self, cross-level interactions affect governance semantics — Self-level entities exercise authority over aspects, aspects coordinate cells, cells inform aspect and Self integration through reporting. Each of these interactions is a governance action or a governance input. The architecture's claim that the CKS Self operates under unified human governance (B1.19, A1.01) depends on cross-level interactions being governed, not merely occurring.

Cross-level access governance is what makes that claim operational. It covers four dimensions that together constitute a complete governance framework: who is authorized to access what across levels (authority distribution); what governs authorized access (access rules); what records each access event (event recording); and what happens when access occurs outside authorization (unauthorized access handling). Each dimension is traceable to specific Paper 1 commitments inherited through Paper 2. The four dimensions compose into a framework that the note names, places in the B1.19 decomposition sequence, and formalizes for the defensive-publication prior-art record.

The strategic purpose of naming cross-level access governance as a standalone operational variant is to establish, as public prior art, that the CKS pattern includes an explicit multi-dimensional governance framework for inter-level interaction — one that specifies rule authoring, authority distribution, event recording, and violation handling as distinct architectural commitments — and that this framework is not an incidental property of the enterprise brain vision but a derivation from Paper 2's core theory.

---

## 2. The four-dimension governance framework

### 2.1 Access rule authoring per A2.04

Cross-level access rules are authored as substrate-resident authoritative content per A2.46. Rule authoring follows the A2.04 governance moment: humans write the orchestration rules that determine which entities at which levels have access to which entities at which other levels, and under what conditions. Access rules are substrate content; they are subject to the inspect, modify, and override rights per A2.01–A2.03 at all times.

Cross-level access rules fall into two structural directions.

**Downward access rules** govern access from higher architectural levels to lower ones. Three downward directions apply within the CKS Self. Self governance over aspects specifies which aspects a given Self-level entity can govern, what governance operations are permitted (inspect, modify, override per A2.01–A2.03), and what scope limitations apply. Aspect coordination over cells specifies which cells a given aspect entity can invoke or coordinate, what coordination operations are permitted, and what conditions trigger coordination. Self-level influence on cells through expression — the mechanism per B2.30 by which Self DNA affects cell-level behavior through governed activation — is governed through Self DNA rules that specify which expression pathways are operative and under what conditions.

**Upward access rules** govern reporting and information flow from lower architectural levels to higher ones. Cell reporting to aspects specifies what operational results cells report, in what format, and at what conditions. Aspect reporting to the Self specifies what aspect-level outcomes inform Self integration, at what frequency, and with what provenance requirements.

The rule content for any cross-level access rule specifies at minimum: which entities at which level have access to which entities at which other level; what type of access is permitted (read/inspect, invoke/call, modify/govern); what conditions trigger access; and what access scope limitations apply. Rules do not need to enumerate every possible interaction — they define what is permitted; what is not permitted is unauthorized. Rules are authored at deployment design time through the Self integration architecture per B2.21, and updated through directed selection per B1.14 when the governance requires.

### 2.2 Authority distribution per A2.47 Category 5

A2.47 Category 5 specifies who has cross-level access authority at each architectural level. The authority distribution is explicit: Self-level entities have authority to access the aspects they integrate; aspects have authority to access the cells they coordinate. The distribution is not uniform across all entities at a given level. Specific cross-level access may be scoped: only certain Self-level entities have access to certain aspects; only certain aspect entities have access to certain cells. The scoping is specified in the authored access rules and is inspectable substrate content.

Access outside the specified authority distribution is unauthorized. The boundary is architectural: if an entity attempts cross-level access that the authority distribution does not specify, the architecture treats this as an unauthorized access event — not as an access that happens to be undocumented, but as a violation. This is what "unauthorized" means in the cross-level access governance framework: access not covered by the authority distribution per A2.47 Category 5.

Cross-partner cross-level access — where entities from distinct CKS Selves interact across organizational boundaries — requires cross-partner authority specification. The authority distribution for such access must be explicitly authored; it does not follow from the within-Self authority distribution.

When cross-level access authority changes — when the authority distribution is modified to add, remove, or rescope which entities have access to which other entities at which levels — A6.06 authority distribution change boundary applies. Changing who can access what across levels is a significant governance event; it triggers the governance processes that accompany authority boundary changes.

### 2.3 Access event recording per A2.40

All cross-level access events are recorded with provenance per A2.40. The six provenance metadata fields apply to access event records: who accessed, what was accessed, at what level, when, under what access rule, and with what outcome. Access event records are substrate content; they are authoritative, inspectable, and subject to the governance affordances per A2.01–A2.03.

Access event recording serves A1.07 retraceability. Cross-level interactions — Self governance over aspects, aspect coordination of cells, cell reporting upward — are part of the operational history that the architecture commits to being retraceable. An access event record provides the entry in that history for each inter-level interaction. The accumulation of access event records produces a complete cross-level interaction history for the deployment, from which governance can reconstruct what happened, when, and by whom.

Access event records support governance audits: reviews of cross-level interaction history to verify that access conformed to authorized patterns, identify anomalous access, and surface patterns that warrant investigation.

### 2.4 Unauthorized access handling

Cross-level access without authority is a governance violation per A1.01. The architecture does not treat unauthorized access as a configuration error or an exception to be handled silently; it treats it as a governance violation in the same sense that any breach of the human-governed commitment is a violation. This framing follows from A1.01 inheritance: if cross-level access governance is the mechanism through which unified human governance is maintained across the three-level Self, then access that circumvents the governance framework circumvents unified human governance.

When unauthorized access occurs: the access event is recorded per A2.40 with a violation record; governance is notified; patterns of unauthorized access — repeated or systematic violations — trigger governance investigation. The unauthorized access handling framework does not prevent all unauthorized access technically; it governs the authorized channels and detects violations through event recording. Detection depends on event recording completeness. Incomplete event recording reduces the governance framework's ability to detect unauthorized access.

### 2.5 Governance affordances at cross-level access rules

The A2.01–A2.03 governance affordances apply to cross-level access rules as to all substrate content. Humans can inspect cross-level access rules (A2.01 inspect right): the authority distribution, the downward and upward rules, the scope limitations, and the conditions under which access is permitted are all inspectable substrate content. Humans can modify access rules through A2.04 rule authoring (A2.02 modify right): rule changes take effect as substrate state and are recorded with provenance. Humans can override specific cross-level access decisions (A2.03 override right): a particular access event may be overridden without requiring architectural justification.

### 2.6 Access governance configuration in Self integration architecture per B2.21

The Self integration architecture per B2.21 includes cross-level access configuration as a component. At deployment design time, the integration architecture specifies which access rules apply for a particular Self's governance over its aspects and cells. The configuration is where cross-level access governance is authored for a specific deployment: downward rules, upward rules, authority distribution, and scope limitations are configured as part of the Self integration architecture and updated through directed selection per B1.14 when governance requires.

---

## 3. What makes cross-level access governance architecturally distinctive

Conventional multi-component AI architectures typically manage inter-component interaction through API calls. One component calls another's API; the call may succeed or fail; the API contract specifies what inputs are valid. This is implicit access control: components can call each other by default within the API contract, there is no architectural specification of authority, and access events are not recorded at the architectural level as governance-carrying records.

CKS cross-level access governance is explicitly distinct on three axes.

**Access rules are authored, not assumed.** Conventional component architectures treat inter-component access as a capability that exists unless blocked. CKS treats cross-level access as a capability that exists only when explicitly authorized through authored access rules. The default is not access; it is absence of access until a rule specifies it.

**Authority is distributed, not uniform.** Conventional architectures often grant components broad access to each other within the API surface. CKS specifies authority distribution precisely: which entities at which level have access to which entities at which other level. The distribution is explicit, inspectable, and subject to governance change processes.

**Access events are recorded as governance-carrying records.** In conventional architectures, API call logs may exist as infrastructure artifacts, but they do not carry the governance semantics of substrate-resident authoritative content. CKS access event records are substrate content with A2.40 provenance metadata; they support A1.07 retraceability and are part of the authoritative record of the deployment's inter-level interaction history.

The three axes together produce the architectural property that distinguishes cross-level access governance from implicit API-based access in architecturally complex deployments: explicit governance over who can interact, with what authority, recorded for retraceability. This property is what prevents unauthorized cross-level interactions from proceeding undetected in a CKS Self operating under unified human governance.

---

## 4. The biological analog

Biology offers an apt conceptual scaffold for cross-level access governance: signaling pathway regulation by receptor specificity. In biological organisms, not all cells respond to all signals. A cell's response to an extracellular signal depends on whether it carries the appropriate receptor; receptor specificity is the biological mechanism that governs which cells can receive which signals. Even when a signal is present in the organism's environment, a cell without the appropriate receptor does not respond — the signal does not constitute interaction unless the receptor-mediated access pathway is available.

CKS cross-level access governance is the architectural analog. Not all entities at one level can access all entities at another level by default. The authority distribution per A2.47 Category 5 is the architectural analog of receptor specificity: it specifies which entities can interact across levels, and access without the specified authority does not constitute governed interaction. The access rules authored per A2.04 are the analog of the signaling pathway specification: they define the conditions, types, and scope of cross-level interaction.

The analog functions as conceptual scaffold. The architectural substance is not biological; it is governed, authored access rules with explicit authority distribution and event recording. Paper 2 uses biology vocabulary as bounded load-bearing terminology where it does specific architectural work. The cross-level access governance framework is CKS's own architectural commitment, not a biological mechanism; the biological analog clarifies the governance intuition without substituting for the architectural specification.

---

## 5. Inherited Paper 1 commitments

Cross-level access governance inherits the following Paper 1 commitments as directly load-bearing:

**A2.47 Category 5 — authority distribution.** The authority distribution framework that specifies who has cross-level access authority at each level is a Paper 1 commitment applied at multi-level scope. Access outside the specified distribution is unauthorized.

**A2.04 — rule authoring as governance.** Cross-level access rules are authored through the Paper 1 rule authoring moment. Authoring is a governance action; rules are substrate-resident authoritative content.

**A2.46 — authoritative content.** Access rules authored per A2.04 are substrate-resident authoritative content per A2.46. Their authority status is what makes them the governing reference for cross-level access decisions.

**A2.40 — six provenance metadata fields.** Access event recording applies the six provenance metadata fields to cross-level interaction records. The same provenance structure that Paper 1 establishes for all substrate content applies to access event records.

**A1.07 — path retraceability.** Access event records support retraceability through cross-level interactions. The cross-level interaction history of a deployment is part of the retraceable path that A1.07 commits to making available.

**A2.01–A2.03 — governance affordances.** The inspect, modify, and override rights apply to cross-level access rules as to all substrate content. Governance affordances at the access rules layer are what keep cross-level access governance under unified human governance.

**A1.01 — human-governed.** Unauthorized cross-level access is a governance violation per A1.01. The human-governed commitment applies to the cross-level access framework: the architecture must preserve human authority over the access rules, the authority distribution, and the access event records.

**A6.06 — authority distribution change boundary.** When cross-level access authority changes, A6.06 applies. Modifying the authority distribution — who can access what at which level — is a boundary-crossing governance event subject to the boundary conditions A6.06 specifies.

---

## 6. Operational implications

Several operational implications follow from the cross-level access governance framework.

**Author access rules at deployment design time.** Deployments author cross-level access rules in the Self integration architecture per B2.21 when designing the Self. The downward and upward rules, the authority distribution, and the access scope limitations are deployment-specific content that must be specified before the Self operates. Rules are updated through directed selection per B1.14 when governance requires modification.

**Maintain explicit and inspectable authority distribution.** The authority distribution per A2.47 Category 5 is explicit substrate content. Deployments should ensure the distribution is complete — covering all entity-pairs that have cross-level access authority — and inspectable at all times per A2.01.

**Treat access event records as complete cross-level interaction history.** Access event records accumulate into the cross-level interaction history of the deployment. This history is governance-carrying: it is the substrate from which governance can reconstruct inter-level interaction patterns, verify authorized access, and identify violations. Treating it as complete requires that event recording not be selective; every cross-level access event, authorized or unauthorized, is recorded.

**Monitor for unauthorized access patterns.** Unauthorized access monitoring is an ongoing operational activity. Individual unauthorized access events are recorded and governance is notified per the violation handling framework. Patterns of unauthorized access — systematic circumvention of the access governance framework — require governance investigation. Monitoring is only as effective as event recording is complete.

**Specify cross-partner access authority explicitly.** Cross-partner cross-level access — interactions across organizational boundaries between entities in distinct CKS Selves — requires explicit authority specification in each Self's access rules. The within-Self authority distribution does not extend to cross-partner access by default.

**Conduct access governance audits.** Access governance audits review access event records for unauthorized patterns, verify that the authority distribution matches actual access behavior, and identify access rule gaps or ambiguities. Audits are the operational activity that turns the access event record history into actionable governance intelligence.

---

## 7. Limits

The cross-level access governance framework has specific limits that deployment design should account for.

Cross-level access governance does not prevent all unauthorized access. It governs authorized channels and detects violations through event recording. Detection depends on event recording completeness; gaps in recording reduce detection capability. The governance framework is not a technical enforcement mechanism that makes unauthorized access impossible; it is an architectural commitment that specifies what is authorized, records what occurs, and handles violations when they are detected.

Access rules are not exhaustive specifications of every possible inter-level interaction. They define what is permitted; everything not specified as permitted is unauthorized. Rules do not need to enumerate all possible interactions exhaustively to be complete governance specifications; they need to authorize the interactions the Self requires and to be inspectable and modifiable when those requirements change.

Cross-level access governance is not the same as content filtering or content governance. It governs which entities can interact across levels, not the content of those interactions. What a Self-level entity does once it has authorized access to an aspect, or what an aspect does once it has authorized access to a cell, is governed by separate substrate commitments — including the orchestration rules per A2.04 that govern cell-level behavior — but not by the access governance framework itself.

Access governance changes require governance per B1.14 directed selection. Modifying the authority distribution — changing who has cross-level access authority at which level — is a governance action subject to A6.06 authority distribution change boundary conditions. Changes do not take effect outside the governance process.

Cross-level access governance does not prescribe specific cross-level access patterns. Which patterns are architecturally available, how they are structured, and what operational purposes they serve is the subject of B2.96 (cross-level access patterns). B2.95 establishes the governance framework within which those patterns operate; it does not constrain which patterns a deployment may adopt.

---

## 8. One-sentence operational test

A CKS Self instantiates cross-level access governance if and only if: cross-level access rules are authored as substrate-resident authoritative content per A2.04 and A2.46, specifying downward and upward access with authority distribution per A2.47 Category 5; all cross-level access events are recorded per A2.40 with full provenance; access outside the specified authority distribution is treated as an A1.01 governance violation and recorded with governance notification; and the access rules are subject to the inspect, modify, and override rights per A2.01–A2.03 at all times.

---

## 9. Why naming as standalone matters; position in the B1.19 decomposition

The B1.19 decomposition unfolds over four notes. B2.94 provides the cross-level access integrating frame: the structural overview of what cross-level access is, the three directions it operates in, and how the framework composes in the CKS Self. B2.95 (this note) formalizes the governance dimension: the complete framework of access rule authoring, authority distribution, event recording, and unauthorized access handling that makes cross-level access a governed architectural property rather than an unregulated capability. B2.96 will formalize cross-level access patterns: the specific structural patterns through which cross-level access operates in deployed Selves. B2.97 will formalize cross-level access verification: how the governance framework is confirmed to hold in a deployment through verification substrates and governance review.

The four-note sequence produces a complete prior-art record for cross-level access as a governed architectural property in the CKS Self. Naming cross-level access governance as a standalone note within the sequence secures the specific territory of the governance framework — the four-dimension structure of access rule authoring, authority distribution, event recording, and violation handling — independently of the integrating frame, the access patterns, and the verification processes. Each note in the sequence forecloses a distinct area of potential later invention claims.

Following B2.97, Phase B2 notes turn to the decomposition of B1.20 (recursive Paper 1 commitments), continuing the Phase B2 operational-variant treatment of Paper 2's foundational architectural commitments across approximately B2.98–B2.110.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cross-Level Access Governance: Decomposing B1.19 by Formalizing How Access Rules Are Authored, Authority Is Distributed, Access Events Are Recorded, and Unauthorized Access Is Handled.* May 12, 2026. ORCID: 0009-0004-8065-3235.
