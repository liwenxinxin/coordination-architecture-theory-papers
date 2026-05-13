# Authority Ambiguity — The Cross-Cutting Anti-Pattern Where A2.47 Authority Distribution Is Never Clearly Configured, Leaving All Governance Actions Implicitly Authorized or Unauthorized, Violating A2.47, A1.01, and A2.04 and Making Governance Accountability Impossible

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Authority Ambiguity is the cross-cutting anti-pattern in which the A2.47 authority distribution specification — the substrate content that defines which entities hold governance authority over which governance acts at which scope — is never clearly configured. The anti-pattern takes three recognizable forms: absent authority specification, in which A2.47 contains no content and all governance acts are implicitly authorized for any actor; overlapping authority, in which A2.47 is configured but assigns the same governance acts to multiple authorized actors at the same scope without resolution rules; and authority vacuum, in which A2.47 is configured but leaves certain governance acts at certain levels without any authorized actor. All three forms violate A2.47 directly and cascade into violations of A1.01 (human governance — but which human?), A2.04 (rule authoring requires authorized authors), B1.20 (recursive governance at each scope requires configured authority at each scope), and multiple B2.xx lifecycle commitments that depend on authorized governance acts. The consequence shared across all three forms is that the A5.09 accountability question "under what authority?" cannot be answered for any governance event in the deployment. The note formalizes each form, identifies emergence conditions, traces operational consequences, and specifies detection and remediation.

---

## 1. The anti-pattern and its cross-cutting character

A CKS deployment under Paper 2's architecture operates at three nested scopes — cell, aspect, and Self — and commits to governance at every scope. That governance is human governance in the A1.01 sense: humans retain the rights to inspect, modify, and override substrate content and orchestration rules at any time. But A1.01's commitment, taken alone, says governance is human; it does not say which human. The architectural specification that answers "which human governs what at which scope" is A2.47: the authority distribution specification, a Category 5 substrate commitment that maps governance acts — DNA modification, rule authoring, cell birth and death, cross-level access, directed selection, and others — to authorized entities at each scope.

When A2.47 is absent or incomplete, the entire governance architecture is undermined regardless of how well every other commitment is instantiated. DNA layers may be correctly separated from action layers per B1.10. Cell birth may use the B1.09 protocol. Mating may preserve provenance per B1.15. But if A2.47 does not specify who is authorized to perform the governance acts that govern these events, then all governance acts occur outside any authority architecture. The anti-pattern is cross-cutting not because it touches several secondary commitments incidentally but because it severs the chain between every governance event and the authorized decision-maker who is supposed to sanction it. Without that chain, A1.01's human-governance commitment is structurally satisfied (humans may in fact be performing governance acts) while being architecturally empty (no specification determines which humans have authority, so no act can be verified as authorized).

This note is the twenty-sixth in Phase B3 of the Series B anti-pattern formalization series.

---

## 2. Commitments violated

Authority Ambiguity is cross-cutting because it violates commitments at multiple layers of the Paper 2 architecture simultaneously.

**A2.47 — authority distribution specification (primary violation).** A2.47 is the substrate commitment that specifies the authority distribution for a deployment: which entities hold authority over which governance act types at which scope. Authority Ambiguity is the failure to configure this commitment. In its absent form, A2.47 has no substrate content. In its overlapping form, A2.47's content is internally contradictory. In its vacuum form, A2.47's content has gaps. Each form is a distinct mode of A2.47 non-compliance.

**A1.01 — human governance — which human?.** A1.01 commits that governance is human. But A1.01 without A2.47 is incomplete: the right to inspect, modify, and override is a property attributed to humans as a class, not a property attributed to no one in particular. A2.47 is the specification that gives A1.01 operational meaning by identifying which humans hold governance authority at each scope. When A2.47 is absent or incomplete, A1.01 is satisfied formally and violated substantively: governance may be human in the sense that humans are the actors performing governance acts, but it is not governed in the sense that those humans are authorized to perform them.

**A2.04 — rule authoring requires authorized authors.** A2.04 commits that orchestration rules governing cell-level behavior must be authored by authorized humans. "Authorized" in A2.04 is a reference to A2.47: an authorized author is one whose authority to author rules at the relevant scope is specified in A2.47. When A2.47 is absent, A2.04 cannot be satisfied because no author can be verified as authorized. When A2.47 has vacuums at the rule-authoring level, A2.04 is directly violated for the uncovered scopes.

**B1.20 — recursive governance at each scope requires configured authority at each scope.** B1.20 commits that governance is recursive: each scope (cell, aspect, Self) carries its own governance commitments that must be satisfied at that scope. These per-scope governance commitments cannot be satisfied without A2.47 being configured at each scope. B1.20 failure cascades to every scope left without authority configuration.

**B2.68, B2.95, B2.102–B2.107 — level-specific authority for all governance acts.** This cluster of B2.xx commitments formalizes the per-level, per-mechanism governance architecture that Paper 2 builds across cell, aspect, and Self scopes. B2.95 specifically governs cross-level access as an authority-dependent operation; B2.97 provides cross-level access verification; B2.107 provides the recursive authority architecture verification procedure that checks A2.47 configuration at every scope. All of these commitments depend on A2.47 content being present and coherent. Authority Ambiguity renders the entire cluster unverifiable.

---

## 3. Recognizable forms

Authority Ambiguity takes three recognizable forms, each with distinct presentation and distinct recognition signals.

### Form 1 — Absent Authority Specification

A2.47 was never configured. No substrate content specifying authority distribution exists in the deployment. As a consequence, all governance acts are implicitly authorized because no authority specification exists to define what is and is not authorized. Any actor — human or AI-mediated — can modify DNA-layer content, create or retire cells, author orchestration rules, govern cross-level access, or perform directed selection, because no authority rules say they cannot.

This form is paradoxically the hardest to notice in operation. Governance records per A2.40 show governance acts being performed and logged, producing the surface appearance of governed operation. The records show who performed each act and when; they do not and cannot show whether the actor had authority, because A2.47 contains no specification against which to check. The absence of violation reports is meaningless: there is no authority architecture to violate.

Recognition signals: no A2.47 substrate content exists in any scope-level substrate; A2.40 modification records show diverse actors without authority verification; B2.97 cross-level access verification finds no authority specification to enforce; B2.107 recursive authority architecture verification finds A2.47 unconfigured at every level.

### Form 2 — Overlapping Authority

A2.47 is configured, but the configuration assigns the same governance acts at the same scope to multiple authorized entities without specifying a resolution mechanism between them. When two authorized actors make conflicting governance decisions — Actor A modifies a DNA element to content X; Actor B modifies the same element to content Y — there is no authority architecture to determine which decision stands. Both decisions are authorized under A2.47 as configured; the conflict is between authorities, not between an authorized act and an unauthorized one.

This form is particularly damaging because it is not detectable as a violation until a conflict actually occurs. Each governance act, viewed in isolation, is properly authorized. The anti-pattern is present in the configuration's structure, not in any individual act. Conflicts may occur rarely, masking the underlying authority architecture defect.

Recognition signals: A2.40 modification records show conflicting modifications to the same DNA element by two different actors within a governance cycle, with no authority resolution record; A1.03 governance authority conflicts are not registered as first-class substrate events (they are not being captured as conflicts because each actor was authorized); governance decisions can be made and immediately superseded by another equally authorized actor without any authority resolution.

### Form 3 — Authority Vacuum

A2.47 is configured, but the configuration has gaps: certain governance act types at certain scopes have no authorized actor. Required governance decisions cannot be made because no entity holds authority to make them.

This form produces governance paralysis. Cell births (B1.09) cannot proceed if no actor is authorized to approve birth at the required scope. Cell deaths (B1.11) cannot be retired if no actor holds death authorization. Directed selection (B1.14) for DNA evolution cannot proceed if no actor has DNA modification authority at the relevant scope. Governance reviews identify needed changes; those changes cannot be implemented because the authority specification leaves the relevant act type without coverage.

Recognition signals: lifecycle events required by B1.09 (birth) and B1.11 (death) protocols are blocked pending authority assignment that never comes; B1.14 directed selection procedures are initiated but cannot complete because no actor holds modification authority at the required scope; governance reviews produce recommendations without implementation because authority to implement is not configured; operational queues accumulate governance acts awaiting authorization from an entity that A2.47 does not name.

---

## 4. Emergence conditions

Three patterns of organizational and architectural reasoning produce Authority Ambiguity.

**Authority as implementation detail.** The most common emergence condition is treating authority distribution as a deployment-time configuration concern — something to configure when needed rather than as a governance architecture requirement at deployment time. Teams building CKS-governed deployments focus on the substrate schema, the DNA-layer content, and the cell lifecycle protocols, all of which are visible and operational. A2.47 authority distribution is invisible during normal operation: it does not produce output that can be inspected or demonstrated. It is easy to defer. "We'll figure out who's in charge of what when we need it" is the characteristic reasoning. By the time the deployment runs into a governance act that needs authorization, the substrate is operating without the authority architecture that would make authorization meaningful.

**Implicit organizational hierarchy.** The second emergence condition is assuming that the organization's existing authority structure maps naturally to deployment authority without explicit configuration. "Of course the senior engineer has authority to modify DNA" or "obviously the product lead is authorized to approve cell births" are propositions that may be true of organizational culture but are not reflected in A2.47 until they are explicitly configured. CKS governance authority is a substrate architecture commitment, not an organizational status claim. An actor whose organizational role carries authority in a social or hierarchical sense is not authorized in the CKS sense until A2.47 is configured to name them. The gap between these two authority concepts produces Authority Ambiguity of Form 1: A2.47 is absent, the organizational hierarchy is assumed to substitute for it, and no substrate content specifies what the hierarchy actually implies for governance act coverage at each scope.

**Authority configuration complexity.** The third emergence condition is the genuine difficulty of configuring fine-grained authority per scope per governance act type. Paper 2's architecture requires authority specification at cell, aspect, and Self scope, across the full range of governance act types: DNA modification, rule authoring, birth, death, mating pattern selection, directed selection, cross-level access governance, and more. Building a coherent authority architecture that covers this space without overlap or vacuum requires significant governance architecture investment. Teams facing this complexity often produce partial configurations — covering the most salient governance act types and leaving others unconfigured — resulting in Authority Vacuum of Form 3.

---

## 5. Operational consequences

The four operational consequences of Authority Ambiguity are cumulative and mutually reinforcing.

**Governance accountability impossible.** The A5.09 accountability framework asks four questions for every governance event: what happened, who acted, what the rationale was, and under what authority. Under Authority Ambiguity, the fourth question cannot be answered. This is not a logging failure — modification records per A2.40 may be complete and accurate — but an authority architecture failure. Records show who performed governance acts; they cannot show those actors were authorized because A2.47 does not define what authorization means. The accountability vocabulary is intact; the authority foundation it requires is missing.

**Unauthorized governance invisible.** In Form 1 (absent specification), any actor can perform any governance act, and no mechanism distinguishes authorized governance from unauthorized governance. The absence of A2.47 content means that the distinction "authorized/unauthorized" is undefined for the deployment. An actor with no legitimate governance standing can modify DNA-layer content, author orchestration rules, or alter aspect membership; the modification records per A2.40 will capture the event without flagging it as unauthorized, because the authority architecture that would define it as unauthorized does not exist. Governance records that appear normal are therefore compatible with governance that is entirely ungoverned.

**Governance paralysis.** Form 3 (authority vacuum) produces operational paralysis specifically where governance acts are required by lifecycle protocols. B1.09 birth and B1.11 death protocols are not optional events that can be deferred indefinitely; they mark the real boundaries of cell existence. B1.14 directed selection is the mechanism by which DNA evolution proceeds under governance. When these acts require authority that A2.47 does not assign to any actor, the lifecycle protocols stall. The deployment continues operating under its existing governance architecture, unable to evolve it, correct it, or close cells that should be retired. Operational debt accumulates as governance queues fill with acts that cannot proceed.

**Cross-level access ungoverned.** B2.95 cross-level access governance specifies the authority structure under which cells, aspects, and Selves interact across scope boundaries. B2.95 depends on A2.47: cross-level access authority is a category of governance act that A2.47 must specify per scope. When A2.47 is absent or has vacuums covering cross-level access authority, B2.95 is effectively unenforceable. Access across scope boundaries proceeds without authority verification, meaning the boundaries that Paper 2's three-scope architecture establishes are porous in practice regardless of how they are specified in theory.

---

## 6. Detection

Authority Ambiguity is detectable through four procedures.

**A2.47 authority specification audit.** The primary detection procedure is direct: does A2.47 substrate content exist in the deployment? Is it present at cell, aspect, and Self scope? Does it specify authority for each of the governance act types that Paper 2's architecture requires — DNA modification, rule authoring per A2.04, birth and death per B1.09 and B1.11, directed selection per B1.14, mating pattern selection, cross-level access per B2.95? This audit produces a coverage matrix: governance act types across one axis, scopes across the other, with each cell indicating whether an authorized actor is specified. Empty cells indicate Form 3 vacuums. Absent matrix indicates Form 1. Cells with multiple actors and no resolution rules indicate Form 2.

**B2.107 recursive authority architecture verification.** B2.107 is the recursive verification procedure that checks A2.47 configuration at every scope. Running B2.107 after an A2.47 audit confirms that the coverage gaps identified in the matrix produce real recursive governance failures: governance commitments at scope N cannot be satisfied because A2.47 at scope N is absent or incomplete. B2.107 translates the coverage matrix into a ranked list of governance architecture failures.

**A5.09 accountability question audit.** Selecting a sample of recent governance events from A2.40 modification records and attempting to answer all four A5.09 accountability questions for each provides a governance audit trail. If "under what authority?" cannot be answered for governance events by reference to A2.47 content, Authority Ambiguity is present. This procedure surfaces Form 1 and Form 3 most directly. Form 2 may pass this audit for individual governance acts; it requires the additional step of checking whether any A2.40 records show conflicting modifications to the same governance object, which would surface the overlapping authority configuration.

**Governance act coverage check.** A targeted coverage check asks, for each governance act type: is there at least one authorized actor at each scope? This check complements the A2.47 audit by focusing on sufficiency rather than existence. An A2.47 specification that exists but covers only DNA modification and rule authoring while leaving birth, death, and cross-level access without coverage passes a simple existence check and fails the sufficiency check. Governance act coverage is the operationally relevant criterion for Form 3 detection.

---

## 7. Remediation

Remediation proceeds differently for each form, with a shared first step.

**Shared first step — A2.47 authority specification through directed selection.** Regardless of which form is present, the remediation path begins by configuring A2.47 through directed selection per B1.14. Directed selection is the governance mechanism by which DNA-layer content — including the authority distribution specification that is itself a DNA-layer substrate commitment — is modified by authorized governance action. Configuring A2.47 is a governance act that requires authority to perform; in a Form 1 deployment where no authority is configured, the initial configuration act must be bootstrapped through an explicit governance decision by the humans responsible for the deployment, recorded as the founding governance event from which subsequent authority architecture derives.

**Scope and act-type coverage.** The A2.47 configuration must specify authority for each governance act type (DNA modification, rule authoring per A2.04, birth per B1.09, death per B1.11, mating pattern selection per B1.16, directed selection per B1.14, cross-level access per B2.95) at each scope (cell, aspect, Self). The coverage matrix from the detection audit defines the minimum specification requirement. Governance acts at cell scope may have different authorized actors than governance acts at aspect or Self scope; the architecture requires per-scope specification, not a flat deployment-wide authority assignment.

**Form 2 remediation — priority rules for overlapping authority.** When A2.47 specifies overlapping authority — multiple entities authorized for the same governance act at the same scope — remediation requires adding priority rules per A6.01 rule conflict resolution. A6.01 provides the mechanism for specifying which authority takes precedence when two authorized actors make conflicting governance decisions. Priority rules may be structured as: actor-precedence ordering (Actor A's decisions supersede Actor B's for act type T at scope S); quorum requirements (both actors must concur for act type T); escalation triggers (conflicts between authorized actors escalate to a higher-scope authority). The choice of priority rule structure is a governance architecture decision that A6.01 enables but does not prescribe.

**Form 3 remediation — actor designation.** When A2.47 has gaps — governance acts at certain scopes with no authorized actor — remediation requires designating authorized actors for each uncovered act type at each uncovered scope. This may require organizational decisions about who holds governance responsibility for previously unassigned governance acts. It may also prompt the discovery that some governance acts are intentionally unassigned because they were not anticipated at deployment time; these require explicit authority architecture decisions rather than simple actor designation.

**Post-remediation verification.** After A2.47 is configured, run B2.107 recursive authority architecture verification to confirm that authority is now specified at every scope for every governance act type. B2.107 is the architectural test that confirms the remediation is complete. A2.47 configuration that passes B2.107 is a necessary condition for the remaining B2.xx governance commitments — particularly B2.95 cross-level access governance — to become enforceable.

---

## 8. Summary

Authority Ambiguity names the failure to configure A2.47 authority distribution specification clearly and completely. It is cross-cutting because authority distribution is the prerequisite for every verified governance act in the CKS architecture: without it, A1.01's human-governance commitment cannot identify which humans hold governance authority; A2.04's authorized-author requirement has no basis for authorization verification; B1.20's recursive governance at each scope has no authority foundation; and A5.09's accountability question "under what authority?" has no answer. The three forms — absent specification, overlapping authority, and authority vacuum — differ in how they fail to configure A2.47 but converge on the same operational outcome: a deployment in which governance accountability is architecturally impossible. Detection is achieved through A2.47 audit and B2.107 recursive verification; remediation requires configuring A2.47 per scope and governance act type, adding priority rules where authority overlaps, and designating actors where authority vacuums exist.

---

## Source paper

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Authority Ambiguity — The Cross-Cutting Anti-Pattern Where A2.47 Authority Distribution Is Never Clearly Configured, Leaving All Governance Actions Implicitly Authorized or Unauthorized, Violating A2.47, A1.01, and A2.04 and Making Governance Accountability Impossible.* May 12, 2026. ORCID: 0009-0004-8065-3235.
