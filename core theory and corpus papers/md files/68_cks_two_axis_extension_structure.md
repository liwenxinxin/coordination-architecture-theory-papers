# The Two-Axis Extension Structure as Standalone: How CKS Extends KO/OIDA Along the Governance Axis and the Multi-Human Axis Simultaneously

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize, as a standalone architectural commitment, the two-axis extension structure by which CKS extends Knowledge Objects (KO) and OIDA prior art simultaneously along the governance axis and the multi-human axis, so that downstream work can adopt, compose with, or argue against the structure without ambiguity.

## Abstract

The CKS pattern positions itself relative to two adjacent prior-art lines — KO and OIDA — and extends each along a structured pair of axes. The first axis, *the governance axis*, extends prior-art governance commitments from procedural form (workflows, approval cycles, scheduled audits) to architectural form (substrate-resident authority, three rights at all times, no-justification override, substrate-only path retraceability). The second axis, *the multi-human axis*, extends prior-art authority structure from single-human form to multi-human form (authority structure as substrate content, multi-human writer attribution, multi-human conflict-handling, distributed override). The architectural commitment is that CKS extends along both axes *simultaneously* — not sequentially, not as feature additions, but as a single architectural-pattern-level commitment whose two axes are operationally entangled, with each axis load-bearing for the other. This note states the structure precisely, defines what simultaneity requires architecturally, distinguishes the structure from sequential, feature-additive, and hybrid extensions, names eight failure modes, and provides an operational test. Subsequent notes formalize the architectural-difference-vs-feature-addition claim (A2.53) and the multi-human axis operational requirements (A2.54) that depend on the structure named here.

## 1. Why the two-axis extension structure needs to be formalized as standalone

The parent foundational note (A1.09) commits CKS to KO and OIDA inheritance along the multi-human axis. The integrating-frame note (A2.49) established the inheritance structure across both prior-art sources; A2.50 formalized what is inherited from KO alone; A2.51 formalized what is inherited from OIDA alone. The treatment that remains, which this note provides, is the structure of the *extension* itself — how the inheritance from each prior-art source is extended along two distinct axes simultaneously, rather than along one axis or as feature additions.

Without precise specification of the two-axis structure, CKS's extension of prior art appears in either of two simpler shapes, both of which are misreadings. Read as single-axis extension, CKS becomes "OIDA with multi-human access" or "KO with architectural governance" — descriptions that elide one of the two extensions and reduce the remaining one to a feature delta. Read as feature-additive composition, CKS becomes "OIDA plus multi-human capability plus architectural governance" — a description that allows the features to appear separately deployable. Both readings are coherent as descriptions of weaker architectures; neither describes CKS.

A second motivation is the strategic prior-art posture the source paper protects across §5.2 and §9.4. The phrase **architecturally different from OIDA on the multi-human axis, not OIDA plus multi-human** carries the weight of the architectural-difference-vs-feature-addition claim formalized at A2.53. That phrase is defensible only if the two-axis structure is itself architecturally substantive; without the structure, the phrase is rhetorical, and with it, the phrase has operational content that follows from the simultaneity property in §3.

A third motivation is the connection to two foundational commitments. A1.01 specifies the human-governed authority that constitutes the multi-human-axis content; A2.06 specifies the architectural-vs-procedural qualifier that constitutes the governance-axis content. This note articulates how those two commitments compose into the two-axis extension structure that distinguishes CKS from KO/OIDA prior art at the architectural-pattern level.

## 2. The two axes, defined precisely

Each axis carries its own operational content. The two are distinct; they do not collapse into a single extension axis.

**The governance axis** extends KO/OIDA from procedural governance to architectural governance. Its operational content is:

(a) *Authority is substrate-resident, not procedurally enforced.* The deployment's authority structure is itself substrate content (per A2.47, Category 5 of the source-of-truth treatment in A1.08): the substrate is authoritative for "who has what authority," and authority changes are substrate writes with provenance (per A2.40). External identity infrastructure is operational, not architectural; the substrate, not the identity provider, is the authority.

(b) *The three rights — inspect, modify, override — operate at all times within authority scope.* The rights enumerated by A2.01–A2.03 are architectural rights held at all times, not procedurally granted at scheduled checkpoints (per A2.07's at-any-time-vs-scheduled-checkpoint qualifier).

(c) *Override carries no architectural justification precondition.* Procedural governance typically requires justification before override (approval workflows, review cycles); A2.03 forbids architectural justification preconditions, treating override as exercise of architectural authority rather than as a procedurally-gated event.

(d) *Path retraceability operates through substrate alone.* Procedural governance typically supports retraceability through external audit infrastructure; A2.41 commits to substrate-only retraceability paths.

**The multi-human axis** extends KO/OIDA from single-human authority to multi-human authority structure. Its operational content is:

(e) *Authority structure carries multiple humans with rights distributed across substrate scopes.* Single-human architectures need not represent authority structure as substrate content; multi-human architectures must (per A2.47).

(f) *Writer attribution distinguishes multiple human writers.* Single-human architectures may carry writer attribution as binary (human-written vs. cell-written); multi-human architectures must distinguish among multiple human writers (per A2.37).

(g) *Conflict-handling rules operate across human-authority boundaries.* Single-human architectures need not address conflicts between human authorities; multi-human architectures must (per A1.03 and its decomposition).

(h) *Override authority distributes across humans without architectural escalation hierarchy.* Single-human architectures have unitary override authority; multi-human architectures distribute override authority while preserving the no-justification-as-precondition property of A2.03.

The eight components together define the two-axis extension structure. Components (a)–(d) are the governance-axis content; components (e)–(h) are the multi-human-axis content. They are distinct: no component of one axis is a restatement of any component of the other.

## 3. The simultaneity of the two-axis extension

The architectural commitment is not merely that CKS extends KO/OIDA along both axes, but that it extends along both axes *simultaneously*. Simultaneity is the load-bearing content of the structure. It has three operational components.

**(a) The two axes operate together architecturally.** Multi-human authority is realized through architectural governance — the substrate-resident authority structure of A2.47 — not through procedural multi-human governance. A procedural multi-human governance is realizable: it is the world of multi-user approval workflows, role-based authorization workflows, escalation chains, ticket-driven access reviews. It is the obvious shape that prior-art KO/OIDA architectures take when extended to multiple users, and it is not what CKS commits to. Architectural governance is realized for multi-human authority — the three rights of A1.01 distributed across multiple humans — not for single-human authority. Single-human architectural governance is realizable: it is what every single-user system already is, dressed up with the three rights and called architectural. It is operationally indistinguishable from procedural single-user authorization, and it is not what CKS commits to. The composition that CKS does commit to is the diagonal: architectural governance *for* multi-human authority structure, with each axis providing the content the other requires to be operationally meaningful.

**(b) Each axis is load-bearing for the other.** The multi-human axis depends on the governance axis. Procedural governance fragments at multi-human scope: each human's procedural workflow may differ; reconciling those workflows requires further procedural machinery (workflow engines, approval routers, escalation services); the procedural-machinery layer itself becomes the de facto authority, and the human-governed commitment of A1.01 collapses into a vendor-or-runtime commitment. Architectural governance prevents this fragmentation by resolving authority at the substrate, where it is uniform across humans — the same three rights apply, the same substrate is the source of truth, the same provenance attaches to every authority exercise. Conversely, the governance axis depends on the multi-human axis. Architectural governance for a single-human authority structure has no operational consequences that procedural single-user authorization does not already deliver: a single user with full inspect/modify/override rights over their own substrate is operationally what every personal-tools deployment already provides. The architectural-vs-procedural distinction becomes operationally significant only when authority is distributed across multiple humans, because it is at multi-human scope that procedural and architectural governance produce observably different systems.

**(c) The composition is not feature stacking.** CKS does not deploy KO/OIDA inheritance, then add architectural governance, then add multi-human capability as separate feature increments. The two-axis extension is an architectural-pattern-level commitment that the implementation instantiates as a unified pattern. Implementations may build the pattern in various operational orders — they may scaffold architectural governance first and distribute multi-human authority across it, or they may model multi-human authority structure first and architecturalize its governance — but the architectural commitment is to the final pattern instantiating both axes simultaneously, not to a specific construction sequence and not to a feature inventory. The distinction matters because feature stacking permits, and indeed encourages, partial deployments in which some features are turned off; the two-axis structure does not.

The three components together define what simultaneity requires architecturally. An implementation that extends along both axes but treats the extensions as separable, deferrable, or sequenced is not honoring the architectural commitment, because the simultaneity property — not merely the two-axis presence — is what distinguishes CKS from feature-additive extensions of KO/OIDA.

## 4. What the two-axis structure is and is not

Two clarifications are needed: what the structure does not claim, so the standalone treatment is not overstated; and what the structure is not, distinguishing it from three adjacent extension patterns commonly conflated with it.

**What the two-axis structure does not claim.** It does not claim that the two axes are the only possible extensions of KO/OIDA: future architectures may add additional axes, and CKS work in adjacent papers introduces extensions on further axes that are out of scope for this note. It does not claim that the two axes are mathematically orthogonal: the axes are architecturally distinct (each has its own operational content per §2) but operationally entangled (each is load-bearing for the other per §3). It does not specify implementation order: implementations may construct the two-axis structure in various operational orders provided the final pattern instantiates both axes simultaneously. It does not require all CKS deployments to use the full multi-human capability: a deployment may operate with a single human in the authority structure, but the architectural commitment to multi-human authority structure (per A2.47) holds, with the structure carrying one human rather than many — the single-human deployment is an *instance* of the multi-human pattern, not a deployment of a single-human variant. It does not foreclose other extension structures: other architectures may extend KO/OIDA along different axes, and CKS does not claim exclusive succession over the prior-art space.

**What the two-axis structure is not.** Not *sequential single-axis extensions*: sequential extension would extend KO/OIDA first along one axis (producing an intermediate variant) and then along the second; the simultaneity property of §3 forbids treating intermediate single-axis variants as architecturally coherent. Not *feature-additive extensions*: feature-additive extension would treat multi-human capability and architectural governance as separate features each composing with KO/OIDA inheritance; the load-bearing-mutual-dependency property of §3(b) forbids treating the features as independently deployable. Not *hybrid extensions that mix axes*: a hybrid extension would extend KO/OIDA along axes that mix governance elements with multi-human elements (multi-human procedural governance, single-human architectural governance); the axis-distinctness of §2 forbids blurring the axis boundaries.

These three "is-not" patterns — sequential, feature-additive, hybrid — are the most common shapes implementations drift toward when positioning CKS against prior art; the architectural commitment is precisely *not* to any of them.

## 5. Failure modes that violate the two-axis structure

Eight failure modes name ways an implementation can fail the architectural commitment, each diagnostic of a specific violation.

**Single-axis extension only.** KO/OIDA is extended along one axis (governance or multi-human) without the other. The result is a single-axis extension of prior art, not the two-axis extension CKS commits to.

**Sequential extension presented as architectural.** Multi-human capability is built on top of KO/OIDA inheritance first, then architectural governance is layered on top, and the result is presented as CKS. The simultaneity of §3 is broken; intermediate single-axis variants are treated as if architecturally coherent.

**Feature-additive composition.** Multi-human capability and architectural governance are added as separate features composing independently with KO/OIDA inheritance, each deployable on its own. The mutual-dependency property of §3(b) is broken.

**Hybrid axis mixing.** KO/OIDA is extended along axes that mix multi-human elements with governance elements (multi-human procedural governance, single-human architectural governance). The axis-distinctness of §2 is broken; the two axes are blurred into hybrid axes.

**Procedural multi-human governance.** Multi-human authority is realized through procedural mechanisms — multi-user approval workflows, role-based authorization workflows, escalation chains — rather than through substrate-resident authority structure (per A2.47). The governance axis is not extended; only the multi-human axis is, and procedurally at that.

**Single-human architectural governance.** Governance is extended to architectural form without authority being extended to multi-human form. The result is operationally indistinguishable from procedural single-user authorization. The multi-human axis is not extended.

**Decomposable axis presentation.** The two axes are presented as architecturally decomposable, with the claim that one axis can be honored while the other is left for future extension. The simultaneity is denied at the level of architectural framing, even if the implementation happens to honor both axes.

**Feature-flag axes.** The two axes are made configurable through deployment flags, with deployments choosing whether to enable architectural governance, multi-human authority, both, or neither. The architectural commitment becomes a deployment configuration; the axes become options rather than commitments.

A system exhibiting any of these failure modes does not instantiate the two-axis extension structure in the architectural sense, even if its multi-human and governance features function operationally.

## 6. Operational test

A system instantiates the two-axis extension structure if and only if all of the following are true.

1. The system extends KO/OIDA inheritance along the governance axis from procedural to architectural governance per components (a)–(d) of §2.
2. The system extends KO/OIDA inheritance along the multi-human axis from single-human to multi-human authority per components (e)–(h) of §2.
3. The two axes are distinct (each has its own operational content per §2) but operationally entangled (each is load-bearing for the other per §3(b)).
4. The two axes are extended simultaneously, not sequentially: intermediate single-axis variants are not treated as architecturally coherent per §3(a).
5. The architecture is not feature-additive composition: the two axes are not separately deployable as independent features per §3(c).
6. The two-axis structure is architectural-pattern-level, not implementation-level: specific implementations may realize each axis operationally in different ways while satisfying the architectural commitment.

A system that fails any of (1)–(6) does not instantiate the two-axis extension structure in the architectural sense, regardless of how its multi-human and governance features function operationally.

## 7. Conclusion

The two-axis extension structure is the load-bearing architectural framing that distinguishes CKS from prior-art KO/OIDA architectures. It commits CKS to extend KO/OIDA along two distinct axes — the governance axis (procedural to architectural) and the multi-human axis (single-human to multi-human authority structure) — *simultaneously*, with each axis architecturally distinct in operational content but operationally entangled with the other in load-bearing dependency. The structure is a single architectural-pattern-level commitment that the implementation instantiates as a unified pattern, not as a feature inventory.

The structure is load-bearing for several downstream commitments. The architectural-difference-vs-feature-addition claim (A2.53) depends on the simultaneity property of §3, without which CKS could be defended as feature-additive extension of KO/OIDA. The multi-human axis operational requirements (A2.54) depend on the multi-human axis being one of two simultaneous extensions, without which the requirements would be feature additions rather than operational components of an architectural extension. The architectural-property qualifier on governance (A2.06), the human-governed commitment (A1.01), and the substrate-as-source-of-truth commitment in its authority-structure category (A1.08, A2.47) all depend on the same two-axis support.

Implementations under pressure to position CKS against prior art drift consistently toward simpler shapes — single-axis extensions are easier to describe; feature-additive compositions are easier to justify in incremental deployments. Naming the two-axis extension structure as a standalone architectural commitment, with the two axes specified in §2, the simultaneity in §3, the scope in §4, the failure modes in §5, and the operational test in §6, gives downstream work a precise specification of how CKS extends KO/OIDA architecturally. Subsequent work that adopts the CKS pattern, extends it, composes it with adjacent patterns, or argues against it should use "two-axis extension structure" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## Companion notes

Li, W. (2026). *Authority, Not Labor: A Precise Definition of "Human-Governed" in the Coordination Knowledge Substrate Pattern.* 24 April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inheritance and Extension: How CKS Builds on Knowledge Objects and OIDA Along the Multi-Human Axis.* 27 April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *The Two-Axis Extension Structure as Standalone: How CKS Extends KO/OIDA Along the Governance Axis and the Multi-Human Axis Simultaneously.* May 5, 2026. ORCID: 0009-0004-8065-3235.
