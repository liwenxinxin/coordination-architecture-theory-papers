# Ungoverned Cross-Level Access — The Anti-Pattern That Arises When Entities Access Other Structural Levels Without Governance Authorization per B1.19

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

---

## Abstract

B1.19 of the CKS architectural framework establishes cross-level access as governed inter-level interaction: access between the cell, aspect, and Self levels is a positive architectural commitment, not incidental behavior, and it requires access rules, authority distribution per A2.47, and event recording per A2.40. This note formalizes the anti-pattern that arises when inter-level access occurs outside that governance framework — **Ungoverned Cross-Level Access**. The anti-pattern presents in three recognizable forms: access without A2.47 authorization, where entities traverse structural levels without holding authority for that direction and scope; unrecorded access, where cross-level influence is observable in the substrate but no access event records exist; and access-rule-absent design, where no authored cross-level access rules were ever configured. The note traces three emergence pathways that produce the anti-pattern in practice, identifies four operational consequences that compound as the pattern persists, specifies the detection procedures drawn from B2.97 cross-level access verification, and describes the remediation sequence required to restore B1.19 compliance.

---

## 1. Pattern name

**Ungoverned Cross-Level Access**

**Derivation note series identifier:** B3.20

**Commitment violated:** B1.19 — cross-level access as governed inter-level interaction with access rules, authority distribution, and event recording.

---

## 2. Commitment violated

B1.19 establishes that access between structural levels in the three-level CKS architecture — cell, aspect, and Self — is not incidental to implementation but is an architecturally committed operation subject to governance. Three components jointly constitute the B1.19 commitment.

First, cross-level access must be governed by **authored access rules** that specify which entities may access which levels, in which direction, and under which conditions. These rules are substrate content authored through human governance, not implicit conventions embedded in implementation code.

Second, cross-level access must be matched to **authority distribution** per A2.47. An entity that initiates a cross-level access operation must hold A2.47 authority for that access direction and scope. Authority distribution is configured at each level: cell-level authorities differ from aspect-level authorities, and both differ from Self-level authorities. Cross-level access that falls outside any entity's A2.47 allocation is unauthorized regardless of whether it succeeds technically.

Third, cross-level access events must be **recorded** per A2.40. The provenance requirement is not optional for cross-level operations: because cross-level access is how Self-level governance reaches cells and how cell-level behavior informs aspect or Self reasoning, the chain of influence must be retraceable. A2.40 recording for cross-level access events is the substrate mechanism that makes B1.19 operative rather than nominal.

The B2.94–B2.97 decomposition of B1.19 specifies the positive architecture. B2.94 establishes the cross-level access frame as an architectural commitment; B2.95 establishes that access without authority is a governance violation; B2.96 specifies the cross-level access patterns that constitute governed inter-level interaction; and B2.97 provides the verification procedure — cross-level access rule completeness, authority distribution correctness, and unauthorized access detection — that confirms B1.19 compliance in a deployed system.

Ungoverned Cross-Level Access is the failure mode that results when any of these three components — access rules, authority distribution, event recording — is absent or bypassed.

---

## 3. Recognizable form

The anti-pattern presents in three distinct forms. Each form is independently sufficient to constitute a B1.19 violation; they frequently co-occur.

### Form 1: Access without authorization

The most direct form: entities access entities at other structural levels without holding A2.47 authority for that access direction and scope.

The canonical example is a cell that directly accesses Self-level substrate without aspect-level mediation. In a governed architecture, a cell's reach into Self-level content must travel through the aspect level with authority at each step — cell holds cell-level authority, aspect holds authority to operate on cell content at aspect scope, Self-level access requires Self-level authority. When a cell crosses directly to the Self level, it bypasses both the aspect-level mediation step and the authority check at Self scope. The access may succeed technically — implementation barriers are not the same as governance barriers — but it occurs outside any A2.47 allocation.

A second recognizable instance: an aspect modifies Self DNA without Self-level authority per A2.47. Because aspects operate at the intermediate level, they may hold authority over cells within their scope, but authority over Self DNA is a distinct allocation that must be explicitly configured. An aspect that writes Self DNA without that allocation has crossed a level boundary without the authority that boundary requires.

The recognition signals for Form 1 are: cross-level access events occur and are detectable in substrate records or implementation logs, but A2.47 authority records are absent for the accessing entity at the accessed level. B2.97 unauthorized access detection surfaces this condition by comparing access events against authority distribution records and identifying events that exceed authority boundaries. The A1.01 governance violation is sharp: cross-level access without A2.47 authority is not a gray-zone compliance question but a structural breach of the access framework.

### Form 2: Unrecorded access

The second form preserves the factual occurrence of cross-level access but removes it from the governance record. Access events happen — cells behave in ways that reflect Self-level DNA, aspects exercise influence over cell behavior — but the events are not recorded per A2.40 because they travel through implementation channels that bypass the substrate recording layer.

The recognition signal for Form 2 is an inferential gap: cross-level influence is observable at the substrate level (Self DNA correlates with cell behavior over time; aspect orchestration rules produce cell-level effects) but the access event records that should explain that correlation are absent. B2.97 unauthorized access detection finds access events with absent provenance — influence is present, records are not. The A5.08 provenance-completeness test fails for cross-level operations, returning incomplete lineage chains. A1.07 retraceability through cross-level access is broken because the events that constitute the causal chain are not in the substrate.

Form 2 frequently arises in systems where cross-level influence has been implemented but the architects did not recognise it as a governed operation requiring A2.40 recording. The implementation does what it was designed to do; the governance record does not capture it.

### Form 3: Access-rule-absent design

The third form is architectural rather than transactional: the deployment was never configured with authored cross-level access rules per B2.95. There are no rules to violate because no rules exist. All cross-level access — however frequent, however influential — happens through implicit implementation channels: function call stacks, shared configuration files, environment variables, framework-provided dependency injection.

The recognition signals for Form 3 are at the architecture level rather than the event level. B2.95 access rule completeness verification finds no authored access rules for cross-level operations. The B2.97 access rule completeness dimension fails not because rules are violated but because the dimension has no content. The Self integration architecture per B2.21 has no cross-level access configuration. Cross-level access patterns per B2.96 are not configured — the patterns described in B2.96 presuppose authored rules, and an architecture with no rules has instantiated none of them.

Form 3 is the most structurally complete version of the anti-pattern because it forecloses detection and remediation through event-level analysis. There are no access rule violations to find; there are no unauthorized accesses against an authority record because no authority record was authored; there are no missing A2.40 entries against a governed channel because no governed channels exist. The anti-pattern is present in the architecture's design, not in the behavior of individual access events.

---

## 4. Emergence conditions

Three conditions, independently sufficient and often concurrent, produce Ungoverned Cross-Level Access in practice.

**Implementation bypass.** Implementation teams building systems that instantiate the three-level CKS architecture encounter a design requirement to invoke behavior at a different level. The direct implementation path — a function call, a configuration dependency, a shared module reference — is available and produces the correct runtime behavior. Teams follow the direct path without recognising it as a governed cross-level access operation. The governing insight, "it's just a function call," is accurate at the implementation layer and incorrect at the governance layer. The function call does what function calls do; the governance framework requires that the same interaction travel through the access rule and authority distribution architecture. When implementation-layer reasoning governs architecture-layer decisions, ungoverned access follows.

**Framework inheritance.** Frameworks used to implement CKS deployments — dependency injection containers, service meshes, configuration management systems, orchestration platforms — provide cross-component access mechanisms as first-class features. These mechanisms create implicit cross-level dependencies that are invisible at the architecture level because they are presented as infrastructure rather than as access operations. An aspect that receives a Self-level configuration object through a dependency injection framework has accessed Self-level content, but the framework mediated the access in a way that does not surface it as a cross-level operation requiring governance. Architects who focus on the application layer do not see the governance gap; the framework fills the access mechanically and the gap is inherited without deliberate decision.

**Governance architecture incomplete.** A2.47 authority distribution must be configured for cross-level access at each level for B1.19 to be operative. In many deployments, A2.47 is configured for intra-level operations — cell-level authority, aspect-level authority, Self-level authority — without separately configuring the cross-level dimensions: which cell-level entities may access aspect-level content, which aspect-level entities may access Self-level content, and in which directions. When the cross-level dimensions of A2.47 are not configured, cross-level access defaults to unauthorized because no authority was allocated. The absence is not a violation by any entity — no entity exceeded its authority because no authority was defined — but the effect is that B1.19 cannot be operative. All cross-level access occurs outside an authority framework that does not cover it.

---

## 5. Operational consequences

Four consequences compound as Ungoverned Cross-Level Access persists in a deployment.

**Level distinctions eroded.** The three-level CKS architecture — cell, aspect, Self — carries meaning because each level has distinct governance scope, distinct authority allocations, and distinct operational commitments per B1.20. When any entity can access any other level without governance, the three-level structure collapses functionally even if the labels remain. Cells that can directly access Self DNA do not operate at cell scope; aspects that can modify Self DNA without Self-level authority do not operate at aspect scope. Level membership becomes a labeling convention rather than a governance boundary. The commitments that depend on level-appropriateness — per-level authority, per-level evolution governance, per-level orchestration rules — cannot be maintained because the levels themselves are not enforced.

**Audit trail broken.** Governance at the Self level must reach cells through defined channels if compliance work is to be able to trace that reach. When cross-level access is unrecorded or ungoverned, compliance auditors encounter the following condition: cells are behaving in ways that reflect Self-level decisions, but the substrate records do not explain how those decisions reached the cells. The A5.09 four accountability questions — what happened, who authorized it, what governed it, what changed — cannot be answered for cross-level operations because the answer depends on event records that do not exist. This is not merely a compliance inconvenience; it is a structural failure of the accountability architecture that B1.19's recording requirement exists to prevent.

**Authority distribution meaningless.** A2.47 authority distribution provides actual governance only if cross-level access is checked against it. When cross-level access bypasses the authority framework entirely — through implementation channels, framework inheritance, or absent access rules — A2.47 continues to exist as substrate content but provides no operational constraint. Any entity can access any level regardless of what A2.47 specifies. The authority distribution has been authored but not enforced, and unenforced authority is nominal rather than operative. The governance that B2.95 requires cross-level access to pass through has been decoupled from the access itself.

**Vertical evolution ungoverned.** Vertical evolution per B1.16 — structural reorganization of the three-level architecture, including aspect splitting, merging, cell reassignment, and new aspect introduction — requires governed cross-level access to operate through the pathways per B2.81. When cross-level access is ungoverned, vertical evolution cannot be distinguished from ordinary ungoverned access. An operation that appears to be a governed structural reorganization — cells moving between aspects, a new aspect inheriting cell populations — may be ungoverned cross-level access producing structural side effects. The governed pathways that make vertical evolution a recognizable architectural event, rather than an observable side effect, depend on the cross-level access governance that B1.19 requires. In the anti-pattern's presence, vertical evolution loses its architectural identity.

---

## 6. Detection

Four procedures identify Ungoverned Cross-Level Access and locate which form or forms are present.

**B2.97 cross-level access verification.** The verification asks three questions jointly: are cross-level access rules complete (all access directions covered, all levels addressed); is authority correctly distributed (A2.47 covers cross-level access at each level and in each direction); and are unauthorized accesses absent (no access events exceed authority boundaries). A deployment that fails any of the three questions instantiates the anti-pattern. The third question identifies Form 1; the completeness questions identify Form 3. B2.97 is the primary detection instrument because it tests the full B1.19 commitment rather than individual access events.

**B2.97 unauthorized access detection.** Applied as a targeted sub-procedure: compare access events in the substrate against A2.47 authority records and identify events that exceed authority boundaries. This procedure specifically surfaces Form 1 — access without authorization — because it operates at the event level rather than the architecture level. Events that exist in implementation logs but not in the A2.47 authority record are the signature of unauthorized cross-level access.

**B2.95 access rules check.** Verify that authored cross-level access rules exist as substrate content. The check asks: has an authorized human authored rules that specify which entities may access which levels, in which directions, under which conditions? An affirmative answer does not establish B1.19 compliance, but a negative answer establishes Form 3 immediately and indicates that the anti-pattern is architecturally present regardless of the event-level record.

**A2.40 access event audit.** Audit cross-level access events against A2.40 recording requirements. For each observable instance of cross-level influence, verify that the corresponding access event record exists in the substrate. This procedure surfaces Form 2 directly: if influence is observable but records are absent, unrecorded access is present. A5.08 provenance-completeness testing provides the operational form of this audit for cross-level operations specifically.

---

## 7. Remediation

Remediation proceeds in sequence, with the most architecturally foundational steps first.

**Author cross-level access rules per B2.95.** No event-level remediation is possible until authored access rules exist as substrate content. Cross-level access rules specify which entities hold access at which levels, in which directions, and under which conditions. Authoring these rules is itself a governance act conducted through directed selection per B1.14 — the rules are authored by authorized humans and governed as substrate content. Without this step, any event-level remediation lacks the normative framework against which access events can be assessed.

**Configure A2.47 authority distribution for cross-level access.** Authority distribution must be explicitly configured for cross-level dimensions at each level. Existing A2.47 configuration covering intra-level operations is insufficient; the cross-level dimensions — cell-to-aspect, aspect-to-Self, and reverse directions — must be separately specified. Configuration determines which entities hold authority for which access directions; the authored access rules from the prior step provide the governance specification that authority configuration implements.

**Establish recording infrastructure for cross-level access events.** If cross-level access has been occurring through implementation channels that bypass the substrate recording layer, the recording infrastructure must be established before governed cross-level access can operate. All cross-level access must route through channels that produce A2.40 records as a byproduct of access execution, not as a manual reporting step.

**For access-without-authorization (Form 1):** Retroactively review cross-level access events identified by B2.97 unauthorized access detection. For each event, either retroactively authorize the access path by configuring A2.47 for that entity and direction, or revoke the access path and reconfigure the implementation to route through governed channels. Entities whose access was unauthorized and is not subsequently authorized must be reconfigured.

**For unrecorded access (Form 2):** Identify the implementation channels through which unrecorded access has been occurring. Route those channels through recording infrastructure so that future access events produce A2.40 records. Assess whether historical unrecorded access has created audit gaps that require remediation at the compliance layer, independent of the architectural fix.

**Run B2.97 cross-level access verification after remediation.** The verification confirms that all three B2.97 dimensions — rule completeness, authority correctness, unauthorized access absence — are now satisfied. If the verification fails any dimension, remediation is incomplete and the anti-pattern persists. B2.97 is both the detection instrument and the post-remediation confirmation instrument; a passing B2.97 result is the operational evidence that B1.19 compliance has been restored.

---

## 8. Relationship to adjacent commitments

Ungoverned Cross-Level Access does not occur in isolation. Several adjacent commitments are degraded or rendered non-operative when B1.19 is violated.

**B1.20 deployment-level-only governance** — the subject of B3.21 — represents a related failure mode where governance is configured at only one level rather than at all three. Where B3.21 is a failure of governance coverage, B3.20 is a failure of the access framework that connects levels. The two anti-patterns can co-occur, but they are distinct: a deployment can have governance at all three levels and still have ungoverned cross-level access between them (B3.20 without B3.21), or can have governed cross-level access but only Self-level substantive governance (B3.21 without B3.20).

**B1.16 vertical evolution** cannot be distinguished from ungoverned cross-level access when B1.19 is violated. The governed pathways per B2.81 that give vertical evolution its architectural identity depend on the access framework B1.19 establishes. This means that in the presence of Ungoverned Cross-Level Access, observations of structural change cannot be confidently attributed to governed vertical evolution rather than to ungoverned access producing structural side effects.

**A1.01 human-governed** is indirectly at stake. When ungoverned cross-level access is present, the human authority architecture cannot maintain its scope: human authority over Self-level content does not constrain what cells do if cells can access Self-level content without going through governed channels. The authority architecture holds at each level independently but loses its vertical coherence.

---

## 9. Conclusion

B1.19 commits the three-level CKS architecture to governed inter-level interaction: not the prevention of cross-level access, but its governance. Access rules, authority distribution, and event recording are the three components that make cross-level interaction a governed architectural operation rather than an implementation artifact. Ungoverned Cross-Level Access is the failure mode that results when any of these components is absent — when access occurs without authority, when it occurs without records, or when no access rules were ever authored.

The anti-pattern is architecturally consequential because its operational effects are not local to individual access events. Level distinctions erode functionally, audit trails break at the vertical axis, authority distribution decouples from actual access, and vertical evolution loses its governed identity. These consequences compound over time and are difficult to observe directly because the anti-pattern is most visible in the absence of records rather than in the presence of detectable violations.

The remediation sequence — authored rules, authority configuration, recording infrastructure, event-level review, B2.97 verification — is sequentially constrained: event-level work cannot precede the architectural work of authoring rules and configuring authority. B2.97 cross-level access verification provides the detection instrument before remediation and the confirmation instrument after, making it the operational anchor for B1.19 compliance work.

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).
