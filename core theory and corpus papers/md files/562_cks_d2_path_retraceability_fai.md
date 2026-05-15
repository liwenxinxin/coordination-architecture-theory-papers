# FAI and Path Retraceability at Inter-Self Scope

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Paper 1 of the CKS series commits to path retraceability as an architectural property: every governance output in a substrate must be traceable back through the authorization chain that produced it. At intra-Self scope — within a single organization's governed substrate — the authorization chain is structurally simple: one governance authority, one authorization locus. Full Aspect Integration (FAI), Paper 3's canonical operation over the shared substrate, extends governed coordination across organizational boundaries. At inter-Self scope, the authorization chain crosses governance authority boundaries, and the single-locus chain of Paper 1 becomes a four-link cross-organizational chain. This note, D2.67 in the derivation series, articulates the four-link structure, states the path retraceability requirement at inter-Self scope (backward traceability through all four links), identifies four break types that violate the requirement, and establishes the complete four-link chain as proof of governance sovereignty at every organizational boundary crossing. A distinction from D2.03 — which covers provenance structure — is stated precisely: provenance records are evidence; the authorization chain is proof of governance.

---

## 1. D2.67 as operational decomposition of D1.02 at inter-Self scope

D2.67 is an operational decomposition of D1.02, the six Paper 1 commitments as they extend across the inter-Self perimeter. The specific parent commitment is A1.07: path retraceability. Paper 1's path retraceability commitment holds that every governance output in a substrate — every decision, every conflict resolution, every content write attributed to an orchestration rule — must be traceable back through the path of antecedent substrate content, orchestration rules, and authorizations that produced it. Paper 1 states this commitment at intra-Self scope.

D2.67 derives the inter-Self scope instantiation of that commitment. When FAI events coordinate substrate content across organizational boundaries, governance outcomes arise that involve more than one organizational governance authority. The question D2.67 answers is: what does path retraceability require at inter-Self scope, and how does an observer execute the required backward trace when the traced path crosses organizational governance boundaries?

The answer has two parts. First, the authorization chain at inter-Self scope is not a single-organization chain; it consists of four links, each representing a distinct locus of governance authority. Second, path retraceability requires backward traceability through all four links — not just through the locally-visible records within any one Self's home substrate.

---

## 2. The distinction from D2.03: authorization chain vs. provenance structure

D2.03 covered the provenance chain structure at inter-Self scope: the six metadata fields that every piece of substrate content must carry (writer attribution, timestamp, orchestration rule identifier, antecedent content references, rationale, and contradiction relationship references), and how those fields function when content crosses the inter-Self boundary. D2.03 concerns the structural question: what records exist and what do they carry?

D2.67 covers the authorization chain: the sequence of human governance decisions that authorized each governance outcome. The authorization chain is not the provenance records themselves; it is the sequence of decisions those records evidence. The distinction matters because the two can diverge: a substrate may carry complete provenance records for every piece of content it holds while the authorization chain nonetheless has a gap — for instance, if content in the shared substrate carries its writer attribution and rule identifier, but no record links that content back to the organizational governance decision that authorized the contribution. Complete provenance structure does not guarantee an unbroken authorization chain; path retraceability requires the chain, not merely the records.

Stated precisely: provenance records are evidence. The authorization chain is what those records must be able to prove. D2.03 specified what evidence must be present; D2.67 specifies what that evidence must prove, and what an observer must be able to reconstruct from it.

---

## 3. The four-link cross-organizational authorization chain

For any governance outcome in the shared substrate or in a participating Self's home substrate that derives from an FAI event, the authorization chain at inter-Self scope consists of four links. The four links are not an arbitrary enumeration; each corresponds to a junction where governance authority transitions — where the entity responsible for authorization changes from one organizational governance structure to another or to joint governance.

**Link 1 — Home governance authorization of contribution.** The contributing Self's home governance authorized the contribution to the shared substrate. This link consists of the governance decision — recorded in the contributing Self's home substrate — to share specified aspect content in a specified FAI event configuration. It is the first governance authority junction: the intra-organizational decision that moves content from within one organization's home governance perimeter into the inter-Self shared substrate. Without this link, content in the shared substrate cannot be traced to an organizational governance decision to share; the content appears without a human-authorized origination point.

**Link 2 — Joint governance authorization of FAI configuration.** The participating Selves' governance structures jointly authorized the FAI configuration: the orchestration rules operating over the shared substrate, the configuration of the shared substrate's persistence policy, the conflict-handling specifications, and the terms of exchange. This link consists of the joint authorization record — the inter-organizational governance agreement that governs how the shared substrate operates during the FAI event. It is the second governance authority junction: the moment at which governance authority transitions from each participating Self's home governance acting independently to joint governance acting over the shared substrate. Without this link, governance outcomes in the shared substrate — conflict routings, resolutions, escalations — cannot be traced to an agreement that the participating organizations jointly authorized; they appear to arise from orchestration rules of unverifiable origin.

**Link 3 — Shared substrate governance of content use.** Within the shared substrate, actions taken over contributed content — conflict routing, conflict resolution by orchestration rules, escalation to humans under the joint authority structure, cross-Self synthesis — are authorized by the jointly-authorized orchestration rules identified in Link 2. Each action within the shared substrate generates an authorization record: the rule under which it was taken, the governance authority (jointly-authorized orchestration) under which that rule operates. This link covers the period of the FAI event itself — the governance of what happens to contributed content while the shared substrate exists. Without this link, specific governance outcomes within the shared substrate have no traceable authorization path even when the shared substrate's configuration (Link 2) and each Self's contribution (Link 1) are both recorded.

**Link 4 — Home governance authorization of absorption.** What enters each Self's home evolution machinery from the shared substrate — through the action-feedback evolution feed, through DNA evolution candidate selection, through the governed ingestion of evolution outputs — is authorized by each receiving Self's home governance. This link consists of the directed selection record in the receiving Self's home substrate: the governance decision to incorporate specified FAI-origin content into the home substrate's evolution machinery. It is the fourth governance authority junction: the moment at which governance authority transitions from joint governance over the shared substrate back to each Self's home governance operating over its own substrate evolution. Without this link, FAI-origin content in a home substrate cannot be traced to a home governance decision to incorporate it; the content appears in the home substrate's evolution machinery without a traceable human authorization at the inter-Self → intra-Self re-entry boundary.

The four links correspond to the four governance authority transitions in any FAI event: (1) home governance deciding to share; (2) joint governance configuring the shared substrate; (3) jointly-authorized orchestration governing actions within the shared substrate; (4) home governance deciding to absorb. The link count is not a choice; it is a structural consequence of how governance authority is distributed across an inter-Self coordination event.

---

## 4. The path retraceability requirement at inter-Self scope

The path retraceability requirement at inter-Self scope follows directly from Paper 1's A1.07 commitment applied to the four-link structure: for any governance outcome in the shared substrate or in a participating Self's home substrate that derives from an FAI event, an observer must be able to trace backward through all four links to the originating governance authorizations.

The backward trace has a specific direction and termination condition. Beginning from a governance outcome (a conflict resolution record in the shared substrate, an evolution output in a home substrate, a directed selection decision recorded in a home substrate's DNA evolution record), the observer reads backward: through the link-4 absorption authorization to the FAI event identifier; through the link-3 shared substrate action to the jointly-authorized orchestration rule; through the link-2 joint authorization record to the participating Selves' governance approval decisions; through the link-1 home governance contribution authorization to the originating human governance decision in the contributing Self's home substrate. The backward trace terminates at Link 1 records — human governance decisions in home substrates — which are the intra-Self-scope authorization records that D2.36 and prior work establishes as the base case.

The trace must be executable from substrate content alone. It cannot depend on external audit logs, human memory, or runtime systems outside the substrate. This is the Paper 1 path retraceability requirement carried through to inter-Self scope: the path runs through substrate content — the shared substrate and the participating Selves' home substrates — and the records in those substrates are what makes the trace possible.

The cross-organizational nature of the trace requires that the four links be connected across substrate boundaries. A full trace at inter-Self scope necessarily reads across multiple substrates: the receiving Self's home substrate (Link 4 record), the shared substrate (Link 3 action records and Link 2 configuration records), and the contributing Self's home substrate (Link 1 contribution authorization). The mechanism for this cross-substrate reading is the cross-perimeter reference structure: provenance records in the shared substrate must carry references that enable backward traversal to the contributing Self's governance history; provenance records in a home substrate that incorporates FAI-origin content must carry references back to the FAI event and, through it, to the shared substrate's Link 2 and Link 3 records.

---

## 5. Four break types that violate path retraceability at inter-Self scope

A break in any of the four links is an authorization chain gap. A chain with a gap cannot be fully traced; some governance outcome lacks traceable human authorization at the corresponding boundary crossing. Four break types correspond to the four links.

**Break Type 1 — Missing home authorization of contribution (Link 1 gap).** Content in the shared substrate that lacks a traceable link back to the contributing Self's home governance authorization. This occurs when the contribution record in the contributing Self's home substrate is absent, when the shared substrate's content does not carry a cross-perimeter reference to the contribution event, or when the contribution event identifier is present but does not resolve to a human governance decision record. Effect: an observer tracing backward from content in the shared substrate reaches the inter-Self perimeter boundary and cannot continue into the contributing Self's governance history.

**Break Type 2 — Missing joint authorization of FAI configuration (Link 2 gap).** Governance outcomes in the shared substrate — conflict routings, resolutions, content syntheses — that cannot be traced to a jointly-authorized configuration record. This occurs when the shared substrate's orchestration rules have no governance authorization record, or when the configuration record is present but does not identify the specific governance approvals from each participating Self's governance authority. Effect: actions taken within the shared substrate appear to arise from rules that were not jointly authorized; the inter-organizational governance agreement cannot be established from substrate content alone.

**Break Type 3 — Missing home authorization of absorption (Link 4 gap).** FAI-origin content in a home substrate that lacks the home governance absorption authorization record. This occurs when evolution outputs from an FAI event enter a Self's home substrate without a corresponding directed selection record, or when content is incorporated without the home governance authority's documented decision. Effect: the re-entry boundary — the point at which governance authority transfers from joint governance over the shared substrate back to home governance over the home substrate — has no authorization record; content in the home substrate cannot be traced to a home governance decision to incorporate it.

**Break Type 4 — Missing cross-organizational provenance continuity (cross-perimeter reference gap).** FAI-origin content in a home substrate that carries a local provenance record identifying the FAI event as origin, but does not carry cross-perimeter references that enable backward trace to the contributing Self's governance history. This break type is distinct from Break Types 1 through 3: the individual link records may all exist, but the references connecting them across substrate boundaries are absent or shallow. A home substrate record that notes "origin: FAI event X" without references enabling navigation to the shared substrate's Link 2 and Link 3 records — and through them to the contributing Self's Link 1 records — cannot support a complete backward trace even if all four link records exist elsewhere. The cross-perimeter reference structure is not optional; it is what makes the backward trace executable.

---

## 6. Path retraceability as governance sovereignty proof

The complete four-link authorization chain, unbroken, constitutes a proof of governance sovereignty at inter-Self scope. Governance sovereignty means that every governance outcome involving inter-Self coordination can be traced to human governance decisions — that no governance outcome occurred without traceable human authorization at each organizational boundary crossing.

The proof structure is straightforward. An unbroken four-link chain means: Link 1 — a human governance decision in the contributing Self's home substrate authorized the contribution; Link 2 — the governance authorities of all participating Selves jointly authorized the shared substrate configuration; Link 3 — all actions within the shared substrate were governed by the jointly-authorized orchestration rules; Link 4 — a human governance decision in the absorbing Self's home substrate authorized the absorption. No FAI-origin governance outcome entered any Self's home substrate without passing through all four links — each of which names a human governance decision. The existence of the complete chain is therefore a proof that governance authority, not autonomous AI system operation, authorized every boundary crossing.

This is the inter-Self scope fulfillment of Paper 1's governance sovereignty commitment. Paper 1 establishes that governance outcomes within a single substrate are traceable to human governance decisions within that substrate's single governance authority. Paper 3 extends coordinated substrate operation across organizational boundaries. D2.67 establishes that the governance sovereignty commitment extends with it: the four-link chain is the mechanism by which governed inter-Self coordination remains provably governed, even when the coordination crosses organizational boundaries and involves multiple independent governance authorities.

The governance sovereignty proof is also the architectural basis for the claim that FAI-mediated inter-Self coordination is genuinely governed rather than merely monitored. Monitoring records what happened; governance sovereignty proves that what happened was authorized. A system that logs FAI events but cannot support the complete four-link backward trace has monitoring without governance sovereignty. The four-link chain, fully connected, is what distinguishes the latter from the former.

---

## 7. Anti-pattern: Authorization chain gap

**Definition.** An authorization chain gap is any of the four break types described in §5. The anti-pattern is the implementation of FAI-mediated inter-Self coordination without maintaining the complete four-link authorization chain.

**Form 1 — Contribution without home authorization record.** Content is contributed to a shared substrate, the contribution is technically successful, but no governance decision record is created in the contributing Self's home substrate. The shared substrate holds the content and its provenance; the backward trace reaches the inter-Self perimeter boundary and terminates without resolving to a human governance authorization. This is the most common form of the anti-pattern, arising when the technical exchange mechanism is implemented but the governance record-keeping layer is treated as optional.

**Form 2 — Shared substrate operation under unattributed rules.** The shared substrate's orchestration rules operate without a joint authorization record. Conflict routings, resolutions, and syntheses are governed by rules whose origin cannot be established from substrate content. This form arises when the shared substrate configuration is treated as a technical deployment decision rather than a governance decision, so no joint authorization record is created at the inter-organizational agreement layer.

**Form 3 — Absorption without directed selection record.** FAI-origin content enters a home substrate's evolution machinery without a corresponding governance decision record in the home substrate. The home substrate holds the evolved content; its provenance identifies the FAI origin; but no record establishes that home governance authorized the incorporation. This form arises when the evolution feed mechanism is implemented as an automated ingestion pipeline that bypasses the home governance authorization step.

**Why the anti-pattern is not benign.** An authorization chain gap does not produce immediately visible operational failure. FAI events proceed; content is exchanged; evolution continues. What the gap destroys is the backward trace: a future observer — whether the organization's own governance audit, a regulatory review, or an inter-organizational accountability inquiry — cannot establish that the governance outcome was authorized. The gap is not a current operational defect; it is a future accountability defect. The anti-pattern is invisible at operation time and visible at audit time.

---

## 8. Operational test

D2.67 is satisfied at inter-Self scope if and only if the following is true for any governance outcome in the shared substrate or in any participating Self's home substrate that derives from an FAI event:

An observer, reading substrate content alone — the shared substrate and the participating Selves' home substrates — can trace backward through all four authorization chain links to the originating human governance decisions.

Concretely, the test requires: (1) from the governance outcome in the home substrate, read the FAI event identifier and the directed selection record that authorized absorption (Link 4); (2) from the FAI event identifier, read the shared substrate's configuration record and the joint authorization that established it (Link 2), and the specific action record and the orchestration rule under which the action was taken (Link 3); (3) from the shared substrate's cross-perimeter reference, read the contribution event identifier in the contributing Self's home substrate, and read the home governance authorization record that authorized the contribution (Link 1); (4) verify that each link terminates in a human governance decision record, not in an automated system action or an unanswered reference.

The test fails if any of the four steps fails to resolve, if any cross-perimeter reference cannot be followed, or if any link terminates at a record that is not a human governance decision. A partial trace — one that resolves two or three links but not all four — does not satisfy the requirement. Path retraceability at inter-Self scope requires the complete four-link backward trace.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *FAI and Path Retraceability at Inter-Self Scope.* May 15, 2026. ORCID: 0009-0004-8065-3235.
