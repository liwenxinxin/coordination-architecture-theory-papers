# Boundary Case: Mating With Maximum DNA Conflict — Governance Implications When Union-Pattern Mating of Substantially Different Parent DNA Produces a High-Conflict Offspring, Testing A1.03 Conflict-as-First-Class at Maximum Conflict Density and Governance Capacity for Conflict Resolution

**Note ID:** B6.06
**Series:** B — Paper 2 Derivation Notes
**Phase:** B6 — Boundary Cases

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 13, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

This boundary case formalizes what happens when two parent cells with substantially different DNA specifications — perhaps developed independently in different deployment contexts — are mated using the Union pattern, producing an offspring whose conflict registry at birth is very large. The case tests A1.03 conflict-as-first-class at maximum conflict density: every DNA-level disagreement between the parents must be registered as a first-class substrate object in the offspring, with no silent resolution and no deferral outside the substrate. The key architectural finding is that a high-conflict birth is not a birth failure. The offspring is validly born; the conflict registry is substrate state; birth verification acknowledges it; the governance challenge begins after birth, not at it. The boundary tests whether governance can address a large conflict backlog through directed selection, whether the offspring remains operationally viable during the resolution period, and whether the architecture implies any practical ceiling on conflict registry size at birth. The note also examines the mating pattern choice: Union maximizes conflict when parents are substantially different; Selective merge would have minimized it. This is a governance planning observation, not an anti-pattern designation. The stress points — Specification Integrity Collapse (B3.30) and Governance Theater (B3.22) — identify the two failure modes governance must actively resist after a high-conflict birth.

---

## 1. Configuration Description

Two parent cells — call them Parent A and Parent B — carry substantially different DNA specifications. The difference may arise from independent development in separate deployment contexts, from divergent governance histories that evolved the two cells along different trajectories, or from one parent being significantly more mature than the other. The common feature is that their DNA contains many rules governing overlapping operational territory, and those rules frequently disagree on what the correct behavior is.

Governance elects to mate Parent A and Parent B using the Union pattern per B2.46. Under Union, the offspring inherits all DNA from both parents. Where the parent DNA is compatible — where rules from Parent A and Parent B agree, or address non-overlapping territory — the offspring inherits cleanly. Where the parent DNA conflicts — where both parents have rules governing the same operational territory but specifying different behavior — the offspring inherits both rules, and A1.03 requires that each disagreement be registered as a first-class conflict object in the offspring's substrate at birth.

The mating is governed per B1.10: a mating decision has been made by humans with authority over the lifecycle event, mating records per A2.40 document the event, and the birth of the offspring per B1.09 is governed and verified. The offspring enters existence with a large A1.03 conflict registry. All commitments hold. No anti-pattern has been triggered. The architecture is operating as specified.

This is the configuration: a validly born offspring carrying a very large conflict registry as its opening substrate state.

---

## 2. Architectural Boundary Tested

Three boundary conditions are tested simultaneously in this configuration.

**A1.03 conflict-as-first-class at high density.** A1.03 requires that every conflict encountered in the substrate be registered as a first-class substrate object — with its own identity, provenance, and record of how it arrived. At low conflict density, this requirement is straightforward: a handful of conflicts at birth, each registered, each addressable. At high conflict density, the same requirement must hold across a large registry. The architecture draws no distinction between one conflict and many. A1.03 does not relax at scale, and it does not permit the offspring to be born with silent conflicts — conflicts that exist in the DNA but are not registered because their number would be inconvenient. The boundary being tested is whether A1.03 remains fully satisfied across a large conflict set or whether high density creates pressure toward non-registration. The answer the architecture gives is unambiguous: all conflicts register. The scale of the registry does not change the requirement.

**A5.06 determinism at conflicted birth.** A highly-conflicted offspring may exhibit nondeterministic behavior for inputs that fall within the scope of conflicting rules. Two rules addressing the same operational territory but specifying different behavior will, depending on which rule the expression mechanism activates, produce different outputs for the same input. This does not violate A1.10 as an architecture-level commitment — A1.10 permits documented, governance-acknowledged nondeterminism under specified conditions — but it does mean that the offspring cannot be certified deterministic in the conflicted regions until those conflicts are resolved. A5.06 tests determinism at birth. For a high-conflict offspring, the A5.06 test result will document a known governance-induced condition: the offspring is nondeterministic in the conflict-scope regions, and this nondeterminism is a consequence of the registered conflicts, not of an architectural violation.

**B1.14 directed selection capacity for conflict resolution.** Resolving a conflict in the A1.03 registry requires a directed selection event: a human authority reviews the conflicting rules, determines the correct behavior, and updates the offspring's DNA to reflect that determination. Resolving a large conflict registry requires many such events. The architecture supports this through directed selection as a first-class mechanism per B1.14, but the practical capacity of governance to execute directed selection events at scale is tested by a very large conflict backlog. This is the governance stress that this boundary case is designed to expose: the architecture can handle a large conflict registry structurally, but governance capacity for directed selection is a real resource with real limits.

---

## 3. Governance Implications

**Birth with high conflict registry: a governance challenge, not a birth failure.** The most important governance implication of this boundary case is the one that is easiest to misread. A large conflict registry at birth does not mean the birth has failed or that the mating was a mistake. The offspring is validly born. Birth verification per B2.44 documents the offspring's entry into existence, and that documentation must acknowledge the conflict registry: the verification record states that the offspring was born with a large registered conflict set, identifies the count and scope of those conflicts, and records the governance commitment to address them. This is the correct and complete verification posture. Birth verification that would refuse to verify a high-conflict offspring, or that would attempt to resolve conflicts as a precondition of birth, misreads the architecture. The conflicts are substrate state. They belong to the offspring from birth. Verification acknowledges them.

**The conflict resolution plan.** Because the conflict registry is large and the offspring's operational viability in conflict-scope regions is uncertain, governance should establish a conflict resolution plan at or before birth. The plan has three elements. First, prioritization: conflicts are not equivalent in operational impact. High-stakes conflicts — those where the two parent rules govern behavior in critical or high-frequency operational territory — should be resolved first. Low-stakes conflicts covering rare or peripheral operational territory can be deferred. The prioritization is itself a governance act, recorded in the substrate. Second, batching: directed selection events can be organized into batches, with each batch targeting a coherent set of related conflicts. Batching reduces the overhead of each individual directed selection event and makes the resolution process manageable as a sustained governance activity. Third, timeline: governance should establish a milestone schedule for conflict registry reduction, with review checkpoints at which the outstanding registry is assessed and the plan updated. A conflict resolution plan without a timeline is not a plan; it is a statement of intent that does not commit governance to any particular pace of resolution.

**Mating pattern reconsideration: a governance planning observation.** The Union pattern per B2.46 was the right tool for creating an offspring that inherits all of both parents' DNA — including all their conflict. If the governance goal was to combine as much of both parents' experience and operational knowledge as possible into one offspring, Union is the correct choice, and the large conflict registry is its predictable consequence. However, for parent cells that are substantially different, the Selective merge pattern per B2.47 offers an alternative: rather than inheriting everything from both parents and resolving conflicts post-birth, governance pre-curates what crosses from each parent into the offspring, accepting only the rules where governance has already determined which parent's approach is preferred. Selective merge reduces the conflict registry at birth — potentially to zero for the curated territory — at the cost of the curation work that must be done before the mating completes. This is not a criticism of the Union choice in this boundary case. It is a governance planning observation that should inform future mating decisions when the parent cells are known to be substantially different: Union front-loads conflict into post-birth governance; Selective merge front-loads curation into pre-birth governance. Neither is inherently superior. The tradeoff is a governance judgment, and the judgment should be made with awareness of both options.

**Operational viability during conflict resolution.** The offspring must operate while the conflict resolution plan is being executed. For inputs that fall outside the conflict-scope regions, the offspring operates normally: its inherited rules are internally consistent for those inputs, and behavior is deterministic. For inputs that fall within the conflict-scope regions, governance must determine a temporary operational posture. Three options are available. Governance may designate one parent's rules as operative for each conflict region pending resolution, recording the designation as a temporary substrate entry with explicit expiration upon directed selection resolution. Governance may restrict the offspring from operating on conflict-scope inputs until the relevant conflicts are resolved, recording the restriction as a substrate-level operational constraint. Or governance may permit the offspring to operate on conflict-scope inputs under explicit acknowledgment of nondeterminism, recording the acknowledgment as a governance decision with associated risk. All three options are architecturally admissible. The choice is a governance judgment. What is not admissible is operating the offspring in conflict-scope regions without any governance acknowledgment of the conflict condition.

---

## 4. Boundary Tests

The following tests define what must be true for this boundary case to be handled correctly.

**(a) Is the conflict registry populated per A1.03 for all parent DNA conflicts at birth?** The test passes only if every conflict between Parent A and Parent B DNA specifications that falls within the offspring's inherited operational territory has a registered first-class conflict object in the offspring's substrate at birth. Partial registration — where some conflicts are registered and others are silently resolved or silently deferred to one parent's rule without registration — is a violation of A1.03. The registry must be complete.

**(b) Does the birth record per B2.44 document the conflict registry as a known governance challenge?** The test passes if the birth verification record explicitly acknowledges the size and scope of the conflict registry, records it as a known governance condition, and includes or references a conflict resolution plan. A birth record that ignores the conflict registry, or that treats the birth as unconditional without registry acknowledgment, fails this test.

**(c) Is there a conflict resolution plan with governance timeline?** The test passes if governance has established a prioritized, batched, time-committed plan for resolving the conflict registry through directed selection. A plan without prioritization, batching, or timeline does not pass; a statement of intent to resolve conflicts "eventually" does not pass.

**(d) Does A5.06 determinism test pass, or if not, is the nondeterminism documented as a known conflict-induced condition?** The test passes in one of two states: either the offspring is certified deterministic (because all conflict-scope inputs are operationally restricted pending resolution), or the offspring's nondeterminism in conflict-scope regions is explicitly documented as a governance-acknowledged condition arising from the registered conflicts. A5.06 failure that is undocumented and unacknowledged is a boundary case failure. A5.06 non-certification that is documented and governance-acknowledged is an acceptable boundary case state during the conflict resolution period.

---

## 5. Stress Points

**Conflict registry stagnation and Specification Integrity Collapse (B3.30).** The highest-risk failure mode following a high-conflict birth is conflict registry stagnation: the conflict registry is large, directed selection events are slow to occur, the resolution plan is not followed, and the offspring's DNA remains in a state of unresolved conflict indefinitely. When conflict registry stagnation persists, the offspring's DNA ceases to function as a reliable specification of its behavior. Humans who attempt to understand the offspring's behavior by reading its DNA find a mixture of inherited rules and registered conflicts, with no clear resolution. The offspring's operational behavior becomes unpredictable in the conflict-scope regions, and governance loses meaningful authority over what the offspring actually does — not because governance rights have been revoked, but because the DNA governance is nominally responsible for has become too internally inconsistent to govern coherently. This is Specification Integrity Collapse (B3.30): the DNA layer, intended to be the governed specification of offspring behavior, collapses as a reliable specification. The architectural remedy is sustained directed selection at pace — not a one-time cleanup but an ongoing governance commitment to conflict registry reduction until the registry reaches a manageable level.

**Governance Theater (B3.22).** A subtler failure mode is Governance Theater: the conflict resolution plan is executed on paper — directed selection events are recorded, conflicts are formally "resolved" — but the resolutions do not reflect genuine governance judgment. A nominal resolution may be produced by accepting one parent's rule in every case without examining the substance of the conflict, by delegating resolution to a process that is not genuine directed selection, or by recording resolution decisions that were never actually made by a human with authority. Governance Theater produces a conflict registry that appears to shrink but in which the resolutions do not represent authoritative determinations of correct behavior. The downstream cost is an offspring whose DNA appears to be clean but whose behavior in formerly-conflict-scope regions is governed by resolutions that nobody genuinely chose. The architectural remedy is the same as for all Governance Theater risk: governance must ensure that the authority behind directed selection events is genuine, and that the resolution record reflects actual governance decisions.

**Mating pattern misapplication.** A third stress point — lower severity than the two above — is the governance planning failure of applying Union when Selective merge would have been more appropriate. This is not an anti-pattern in the sense that A1.03 is violated or governance authority is compromised; the offspring is validly born and all commitments hold. But if governance chose Union without awareness of the Selective merge alternative, or without recognizing that the parent cells were substantially different, the large conflict registry is a consequence of a planning failure rather than a deliberate tradeoff. The remedy is not architectural but procedural: governance should assess parent DNA compatibility before selecting a mating pattern, and the mating decision record per A2.40 should document the pattern choice and its rationale.

---

## 6. Architectural Limits

The architecture requires A1.03 registration of all conflicts. It does not specify a maximum conflict registry size at birth. There is no architectural ceiling on how many conflicts a validly-born offspring may carry; the only architectural requirement is that all conflicts are registered, none are silent, and the registry is substrate state. A conflict registry of any size — large or arbitrarily large — is architecturally admissible.

The practical limit is governance capacity for directed selection. Every conflict in the registry requires a directed selection event to resolve. Directed selection events require human authority, time, and attention. At very high conflict density, the resolution timeline extends proportionally, and the risk of conflict registry stagnation increases. The architecture implies that governance can address registered conflicts through directed selection, but it does not guarantee that governance will have sufficient capacity to do so at any particular pace. The pace of resolution is a function of governance resources, not of architectural properties.

This means that the practical viability of Union-pattern mating for substantially different parent cells is governed by the same analysis as any large-scale governance commitment: it is architecturally valid, but it commits governance to a resolution workload whose size is proportional to the conflict density of the parents. Governance should be aware of this commitment before choosing Union over Selective merge for maximally-different parents.

The architecture also implies that during the conflict resolution period — from birth until the last registered conflict is resolved through directed selection — the offspring's status is governed-and-under-resolution. This is a distinct operational state from a conflict-free offspring, and it carries the operational posture governance has established per the implications in §3. It is not a degraded or invalid state; it is a defined and documented state in which the offspring carries unresolved conflicts as substrate content under active governance.

---

## Source Papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to Cite This Note

Li, W. (2026). *Boundary Case: Mating With Maximum DNA Conflict — Governance Implications When Union-Pattern Mating of Substantially Different Parent DNA Produces a High-Conflict Offspring, Testing A1.03 Conflict-as-First-Class at Maximum Conflict Density and Governance Capacity for Conflict Resolution.* May 13, 2026. ORCID: 0009-0004-8065-3235.
