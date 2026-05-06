# The Multi-Human Axis: Five Operational Requirements as Standalone Architectural Specification of the Multi-Human Extension in CKS

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the five operational requirements that the multi-human extension introduces — the operational content of the multi-human axis, distinct from the inheritance specifications that ground it, the two-axis extension structure that makes architectural room for it, and the architectural-difference claim that depends on it for operational specificity.

## Abstract

The CKS pattern's multi-human extension is named in §6.2 of the source paper as architectural rather than feature-additive (§9.4), and its inheritance from KO and OIDA is treated in §5.2 and §6.2. Companion notes formalize the inheritance specifications, the two-axis extension structure, and the architectural-difference claim; an integrating-frame note ties them together. What remains to be formalized is the operational content of the multi-human extension itself: precisely what the multi-human axis requires of CKS substrates at the operational level. This note formalizes that content as five operational requirements — authority structure as substrate content, multi-human writer attribution, multi-human conflict-handling rules, substrate-only paths across multi-human governance, and distributed override authority without architectural escalation hierarchy. It states what each requirement specifies, what the requirements jointly do not entail, what adjacent multi-user patterns they are not, and the failure modes that violate them. With this note complete, the KO/OIDA inheritance decomposition is fully formalized.

## 1. Why the multi-human axis operational requirements need to be formalized as standalone

The parent foundational note on KO/OIDA inheritance commits to that inheritance running along the multi-human axis. The integrating-frame note enumerated five operational requirements at the integrating level. The KO-inheritance and OIDA-inheritance notes formalized what is inherited from each prior-art line; the two-axis-extension note formalized the architectural structure (governance axis and multi-human axis, simultaneous); the architectural-difference note formalized the claim that CKS is architecturally different from OIDA on the multi-human axis rather than OIDA plus a multi-human feature. None of these notes specifies the operational content of the multi-human extension itself — the operational requirements that distinguish multi-human CKS architecture from single-human KO/OIDA prior art at the level a deployment must satisfy to instantiate the architectural commitment.

Without precise specification of those requirements, the multi-human axis appears as a generic multi-user capability that any multi-user system could provide through familiar mechanisms — role-based access control, audit infrastructure, consensus algorithms, escalation chains. The standalone treatment is what makes the multi-human axis operationally specific. It is also what gives the architectural-difference claim its operational specificity: that claim forecloses the "OIDA plus multi-human" reading at the architectural level; the five operational requirements specify what the architectural difference looks like at the level of what a substrate must do. The requirements likewise operationalize the human-governed commitment — the foundational position on human authority through the three-rights structure (inspect, modify, override) — for multi-human contexts.

## 2. The five operational requirements

The multi-human axis introduces five operational requirements. Each specifies architectural content; each traces to a specific commitment in the source paper that operationally distinguishes multi-human CKS from feature-additive multi-user extensions; and the five compose into the multi-human axis content of the two-axis extension. They are not separately deployable feature options.

### 2.1 Authority structure as substrate content

The first requirement is that the deployment's authority structure — which humans hold which rights over which substrate scopes — is itself substrate content per the Category 5 source-of-truth commitment ("substrate authoritative for who has what authority"). Single-human KO/OIDA architectures need not represent authority structure as substrate content because there is one authority-holder; multi-human architectures must, because the structure that distributes authority across multiple humans is itself a coordination object.

Operationally, the authority structure carries, for each human in the deployment's authority set, the rights that human holds and the substrate scopes those rights apply to; authority changes are substrate writes with provenance; the structure is queryable from substrate alone; and when the structure and external sources disagree (e.g., enterprise identity providers), substrate prevails. The requirement is operationally distinct from multi-user authorization workflows because authority is architectural substrate content, not procedural authorization configuration.

### 2.2 Multi-human writer attribution

The second requirement is that writer attribution distinguishes multiple human writers per the "by whom" accountability question. Single-human KO/OIDA architectures may carry writer attribution as binary (human-written vs. cell-written) because there is one human writer; multi-human architectures must distinguish among multiple humans, with attribution linking to each writer's position in the authority structure per requirement 2.1.

Operationally, every substrate write produced by deployment activity by a human carries attribution identifying which specific human authored the write; the attribution links to the writer's authority position at write time, not just to the human's identity in an external identity system; the attribution is committed atomically with the content; and multiple human writers operating on overlapping substrate scopes are architecturally distinguishable. The requirement is operationally distinct from multi-user audit logging because attribution is architectural substrate metadata, not external audit-log content.

### 2.3 Multi-human conflict-handling rules

The third requirement is that conflict-handling rules operate across human-authority boundaries per the conflict-as-first-class commitment and its decomposition. Single-human KO/OIDA architectures need not address conflicts between human authorities because there is one authority-holder; multi-human architectures must, because contradictions can arise between content authored by different humans and the architecture must specify how these are handled rather than silently resolving them.

Operationally, conflicts between content authored by different humans are preserved as substrate-level first-class state; cell-level resolution rules may operate across multi-human conflicts under orchestration rules; direct human override of conflict resolutions respects the distributed authority structure per requirement 2.1 and the override-without-justification commitment; and provenance for conflict resolutions includes the human-authority context for each decision. The requirement is operationally distinct from multi-user consensus algorithms because conflict handling is architectural substrate-level state with rule-governed resolution, not orchestration-level consensus mechanism.

### 2.4 Substrate-only paths across multi-human governance

The fourth requirement is that substrate-only paths work across multi-human governance. Single-human KO/OIDA architectures may support retraceability through external audit infrastructure because there is one authority-holder whose authority is implicit; multi-human architectures must support retraceability through substrate alone, because the authority structure is itself substrate content per requirement 2.1 and paths must traverse the multi-human authority context.

Operationally, the four accountability questions ("what was decided," "by whom," "under what authority," "for what reason") are answerable from substrate alone, with answers that distinguish multiple humans where applicable; "by whom" distinguishes specific human writers per requirement 2.2; "under what authority" references the writer's position in the substrate-resident authority structure per requirement 2.1; and path traversal works across writes by different humans, following antecedent references through multi-human authority transitions. The requirement is operationally distinct from multi-user audit trails because retraceability is architectural substrate traversal, not external audit-log reconstruction.

### 2.5 Distributed override authority without architectural escalation hierarchy

The fifth requirement is that override authority distributes across humans without architectural escalation hierarchy per the override-right commitment. Single-human KO/OIDA architectures have unitary override authority because there is one authority-holder; multi-human architectures distribute override authority while preserving the no-justification-as-precondition commitment.

Operationally, override authority is distributed across humans according to the authority structure per requirement 2.1; each human holding override authority over a substrate scope can exercise that authority at any time within their scope; override exercise carries no architectural justification precondition (deployments may add procedural review at the deployment layer, but the architectural commitment is to no-justification-as-precondition); and disagreements between override exercises by different humans are themselves substrate state, producing conflicts per requirement 2.3 handled through conflict-handling rules rather than escalation chains. The requirement is operationally distinct from multi-user escalation chains because override authority is architecturally distributed without escalation precondition, not procedurally organized through hierarchy.

## 3. What the multi-human axis requirements do NOT claim

The standalone treatment is precise about what the requirements specify. It is equally important to state what they do not, because each of the following misreadings would overstate the architectural commitment.

*Not foreclosure of deployment-layer multi-user features.* Deployments may add multi-user collaboration interfaces, shared dashboards, multi-user search, and other operational features. The architectural commitment is to the five requirements being substrate-architectural; features built on top are deployment concerns the architecture neither requires nor forbids.

*Not a claim that all multi-user systems satisfy the requirements.* Multi-user systems may provide multi-user capabilities through procedural mechanisms — RBAC, approval workflows, audit infrastructure — without satisfying the architectural requirements. The requirements specify what the multi-human extension requires, not what any multi-user system might supply.

*Not specification of implementation patterns.* Implementations may realize each requirement in various ways: different authority schemas, different attribution encodings, different conflict-handling rule formats. The architectural commitment is to the operational content specified in §2, not to specific implementations.

*Not a requirement that all CKS deployments use multiple humans actively.* A deployment may operate with one human in the authority structure, and the architectural commitment to the five requirements still holds — with the structure carrying one human rather than many. Single-human deployments are instances of the multi-human pattern, not deployments of a single-human variant.

*Not specification of any specific size of authority structure.* Authority sets may be small or large; the commitment is to the requirements being satisfied operationally regardless of size.

## 4. What the multi-human axis requirements are NOT

Four adjacent multi-user patterns are commonly conflated with the multi-human axis. Each is a real and reasonable commitment in some other architecture, and none is what the multi-human axis specifies.

*Not multi-user authorization workflows.* These organize authority procedurally — who can do what, gated through workflows. Authority on the multi-human axis is architectural substrate content per requirement 2.1, not procedurally organized through workflows.

*Not role-based access control.* RBAC organizes authorization through roles assigned to users, with permissions attached to roles. The multi-human axis authority structure is substrate-resident with specific writer-to-scope mappings, not abstracted through roles that obscure specific writer identity per requirement 2.2.

*Not multi-tenant architectures.* These organize multiple tenants in shared infrastructure with isolation between tenants. On the multi-human axis, multiple humans participate in shared substrate as part of one authority structure, not as isolated tenants.

*Not federated authority systems.* These organize authority across multiple administrative domains with cross-domain delegation and trust. The multi-human axis authority structure is unified in substrate per requirement 2.1, not federated across domains.

## 5. Why the requirements are load-bearing for downstream commitments

The five requirements are operationally load-bearing for several CKS commitments. The architectural-difference claim depends on the multi-human extension producing architectural difference rather than feature-additive extension, and the five requirements specify what that difference looks like operationally on the multi-human axis. The two-axis extension structure includes the multi-human axis as one of two simultaneous extensions, and the five requirements specify the operational content of that axis; the simultaneity is what makes the requirements coherent, since each presupposes architectural governance on the governance axis. The foundational commitments that operate at multi-human scope — human-governed, conflict-as-first-class, path retraceability, source-of-truth — each operationalize through the five requirements: Category 5 of the source-of-truth commitment through requirement 2.1; the path-retraceability commitment and substrate-only paths through requirements 2.2 and 2.4; conflict-as-first-class through requirement 2.3; the override right through requirement 2.5. Without these requirements, the foundational commitments would fragment at multi-human boundaries.

## 6. Failure modes that violate the requirements

Implementations under pressure to support multi-user contexts consistently drift toward generic multi-user features that may provide multi-user capability operationally without satisfying the architectural requirements. The following anti-patterns each name a way an implementation can fail one or more requirements.

*Authority-as-RBAC-only.* Multi-human authority is realized through role-based access control without authority structure as substrate content per requirement 2.1; authority is procedurally organized through roles rather than architecturally substrate-resident.

*Generic-user-attribution.* Writer attribution distinguishes users by identifier without linking to authority position per requirement 2.2; multiple humans appear as undifferentiated users rather than as authority-distinct writers.

*Conflict-handling-as-consensus-only.* Multi-human conflicts are handled through orchestration-level consensus algorithms without first-class substrate state per requirement 2.3; the conflict commitment becomes feature-additive rather than architectural.

*Audit-trail-retraceability.* Multi-human retraceability relies on external audit trails rather than substrate-only paths per requirement 2.4; the retraceability commitment becomes procedurally enforced rather than architecturally substrate-resident.

*Escalation-gated override.* Multi-human override exercise requires escalation chains rather than distributed override authority per requirement 2.5; the override commitment becomes procedurally hierarchical rather than architecturally distributed.

*Selective-requirement satisfaction.* Some requirements are satisfied while others are not; the architectural commitment to all five is broken, and the implementation produces a partial multi-human extension that does not compose into the multi-human axis content of the two-axis extension.

*Requirement-decomposition-as-feature-options.* The five requirements are made configurable through deployment options; the architectural commitment is broken because the requirements become deployment choices rather than architectural commitments.

*Implementation-as-substitute.* Generic multi-user infrastructure (collaboration platforms, shared dashboards) is provided and treated as satisfying the multi-human axis; the architectural requirements specify architectural content, which generic multi-user infrastructure does not satisfy.

## 7. Operational test

A system instantiates the multi-human axis operational requirements if and only if all of the following are true.

1. Authority structure is substrate content per the Category 5 source-of-truth commitment, not procedural authorization configuration.
2. Multiple human writers are architecturally distinguished in writer attribution, with attribution linking to authority position rather than to opaque user identifiers alone.
3. Conflicts between content authored by different humans are preserved as substrate-level first-class state, not silently resolved by orchestration-level consensus mechanism.
4. Substrate-only paths work across multi-human governance, with the four accountability questions answerable for content authored by any human in the authority structure without recourse to external audit infrastructure.
5. Override authority is distributed across humans according to the authority structure, with no architectural escalation hierarchy and no architectural justification precondition.
6. The five requirements compose architecturally rather than being separately deployable as feature options; the multi-human axis content of the two-axis extension is coherent.

A system that fails any of (1)–(6) does not satisfy the multi-human axis operational requirements in the architectural sense, even if it provides multi-user capabilities operationally.

## Conclusion

The drift from architectural multi-human extension to feature-additive multi-user capability is steady, because generic multi-user features (RBAC, audit trails, consensus algorithms, escalation chains) are operationally familiar, well-tooled in enterprise contexts, and rhetorically accessible — audiences understand "multi-user via RBAC" more easily than "multi-human via architectural substrate-resident authority." Implementations that drift produce systems where multi-human capability is feature-additive rather than architectural, and the downstream consequences manifest as architectural-difference-claim failure, governance failures (authority is not architecturally substrate-resident), retraceability failures (paths fragment at multi-user boundaries), and source-of-truth fragmentation (Category 5 fails because authority structure is not substrate content). Naming the multi-human axis operational requirements as a standalone architectural commitment gives downstream readers a precise specification of what multi-human extension means operationally in CKS.

With this note complete, and with its companions on the integrating frame, KO inheritance, OIDA inheritance, the two-axis extension structure, and the architectural-difference claim already drafted, the KO/OIDA inheritance decomposition is fully formalized. The integrating frame established the inheritance structure; the inheritance specifications formalized what is inherited from each prior-art source; the two-axis extension structure formalized how the inheritance is extended; the architectural-difference claim formalized what the extension produces architecturally; this note formalizes what multi-human extension requires operationally. Together the six notes constitute the operational decomposition of the parent commitment to KO/OIDA inheritance along the multi-human axis.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion notes

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inheritance and Extension: How CKS Builds on Knowledge Objects and OIDA Along the Multi-Human Axis.* 27 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Multi-Human Axis: Five Operational Requirements as Standalone Architectural Specification of the Multi-Human Extension in CKS.* May 5, 2026. ORCID: 0009-0004-8065-3235.
